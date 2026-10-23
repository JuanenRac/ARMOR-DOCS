import contextlib
import io
import json
import re
import tempfile
import unittest
from pathlib import Path
from unittest import mock

import _support  # noqa: F401  (puts tools/ on the path)

import make_readmes
from make_readmes import LANGUAGES, ORDER, UI, RELATED, SHOTS, CAPTIONS

CODES = [code for code, *_ in LANGUAGES]


def fake_root(version="1.2.3", maturity="functional"):
    holder = tempfile.TemporaryDirectory()
    root = Path(holder.name)
    for name in ORDER:
        (root / name).mkdir()
        (root / name / "armor.project.json").write_text(json.dumps({"name": name, "version": version, "maturity": maturity, "stack": "Python / Test"}), encoding="utf-8")
    return holder, root


def headings(text):
    return re.findall(r"(?m)^## ", text)


class SourceConsistencyTests(unittest.TestCase):
    def test_the_eight_languages_of_the_family(self):
        self.assertEqual(CODES, ["en", "es", "fr", "it", "de", "zh", "ja", "pt"])
        self.assertEqual([file for _c, file, *_ in LANGUAGES], ["README.md", "README_spa.md", "README_fra.md", "README_ita.md", "README_deu.md", "README_zho.md", "README_jpn.md", "README_por.md"])

    def test_every_language_has_the_same_interface_words(self):
        expected = set(UI["en"])
        for code in CODES:
            self.assertEqual(set(UI[code]), expected, code)
            for key, value in UI[code].items():
                self.assertTrue(value.strip(), f"{code}.{key} is empty")

    def test_every_language_describes_every_repository_once(self):
        for code in CODES:
            self.assertEqual(set(RELATED[code]), set(ORDER), code)
            for name, text in RELATED[code].items():
                self.assertTrue(text.strip(), f"{code}.{name}")
        self.assertEqual(len(ORDER), len(set(ORDER)))

    def test_screenshot_captions_exist_in_every_language(self):
        for name, shots in SHOTS.items():
            self.assertIn(name, ORDER)
            for _file, key in shots:
                self.assertEqual(set(CAPTIONS[key]), set(CODES), key)

    def test_every_repository_has_its_text_in_every_language(self):
        for name in ORDER:
            data = make_readmes.load(name)
            self.assertEqual(set(data.TEXT), set(CODES), name)
            for code in CODES:
                text = data.TEXT[code]
                for key in ("tagline", "honest", "bullets"):
                    self.assertTrue(text.get(key), f"{name}.{code}.{key}")
                self.assertTrue(all(isinstance(item, str) and item.strip() for item in text["bullets"]), f"{name}.{code}")
            for key in ("emoji", "badges", "structure", "build"):
                self.assertIn(key, data.FACTS, name)

    def test_the_languages_of_a_repository_have_the_same_shape(self):
        for name in ORDER:
            data = make_readmes.load(name)
            reference = data.TEXT["en"]
            for code in CODES:
                text = data.TEXT[code]
                self.assertEqual(len(text["bullets"]), len(reference["bullets"]), f"{name}.{code} bullets")
                self.assertEqual(len(text.get("sections", [])), len(reference.get("sections", [])), f"{name}.{code} sections")
                for mine, theirs in zip(text.get("sections", []), reference.get("sections", [])):
                    self.assertEqual(len(mine["bullets"]), len(theirs["bullets"]), f"{name}.{code} {mine['title']}")
                self.assertEqual(bool(text.get("fit")), bool(reference.get("fit")), f"{name}.{code} fit")
                self.assertEqual(bool(text.get("hardware")), bool(reference.get("hardware")), f"{name}.{code} hardware")


class RenderTests(unittest.TestCase):
    def setUp(self):
        self.holder, self.root = fake_root()
        self.addCleanup(self.holder.cleanup)
        patcher = mock.patch.object(make_readmes, "ROOT", self.root)
        patcher.start()
        self.addCleanup(patcher.stop)

    def test_the_version_and_the_maturity_come_from_the_manifest(self):
        for name in ("ARMOR-NODE-RADAR", "ARMOR-DOCS"):
            text = make_readmes.render(name, "en")
            self.assertIn("Version-1.2.3-0f6cbd.svg", text)
            self.assertIn("Maturity-functional-00E5FF.svg", text)
        (self.root / "ARMOR-NODE-RADAR" / "armor.project.json").write_text(json.dumps({"version": "0.8.4.1", "maturity": "production", "stack": "C++"}), encoding="utf-8")
        text = make_readmes.render("ARMOR-NODE-RADAR", "en")
        self.assertIn("Version-0.8.4.1-0f6cbd.svg", text)
        self.assertIn("Maturity-production-1F883D.svg", text)
        self.assertNotIn("Version-1.2.3", text)

    def test_a_version_written_in_the_facts_is_replaced_not_duplicated(self):
        text = make_readmes.render("ARMOR-NODE-RADAR", "en")
        self.assertEqual(text.count("badge/Version-"), 1)
        self.assertEqual(text.count("badge/Maturity-"), 1)

    def test_every_repository_renders_in_every_language(self):
        for name in ORDER:
            for code in CODES:
                text = make_readmes.render(name, code)
                self.assertIn("# ", text)
                self.assertIn(name, text)
                self.assertTrue(text.endswith("\n"), (name, code))

    def test_all_languages_of_a_repository_have_the_same_section_structure(self):
        for name in ORDER:
            counts = {code: len(headings(make_readmes.render(name, code))) for code in CODES}
            self.assertEqual(len(set(counts.values())), 1, (name, counts))

    def test_the_language_bar_marks_the_current_language_and_links_the_rest(self):
        text = make_readmes.render("ARMOR-NODE-RADAR", "fr")
        self.assertIn("<b>Français</b>", text)
        self.assertIn('<a href="README.md">', text)
        self.assertIn('<a href="README_por.md">', text)
        self.assertNotIn('<a href="README_fra.md">', text)

    def test_the_list_of_the_family_marks_this_repository_and_links_the_others(self):
        text = make_readmes.render("ARMOR-VISION", "en")
        self.assertIn("**ARMOR-VISION** (this repository)", text)
        self.assertIn("**[ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER)**", text)
        for name in ORDER:
            self.assertIn(name, text)

    def test_no_image_appears_twice_in_a_readme_and_the_whole_family_is_listed_once(self):
        for name in ORDER:
            for code in CODES:
                text = make_readmes.render(name, code)
                images = re.findall(r"!\[[^\]]*\]\(([^)]+)\)", text)
                self.assertEqual(len(images), len(set(images)), (name, code, "an image is drawn twice"))
                listed = re.findall(r"(?m)^\* \*\*(?:\[)?(ARMOR-[A-Z-]+)", text)
                self.assertEqual(sorted(listed), sorted(ORDER), (name, code, "the family is not listed once each"))

    def test_the_documentation_repository_links_its_own_files_the_others_link_to_github(self):
        own = make_readmes.render("ARMOR-DOCS", "en")
        other = make_readmes.render("ARMOR-VISION", "en")
        self.assertIn("(docs/CAPABILITY_MATRIX.md)", own)
        self.assertIn("(https://github.com/JuanenRac/ARMOR-DOCS/blob/main/docs/CAPABILITY_MATRIX.md)", other)

    def test_the_banner_is_a_local_file_of_the_repository(self):
        self.assertIn('<img src="images/ARMOR_BANNER.svg"', make_readmes.render("ARMOR-NODE-HMI", "en"))

    def test_the_owner_is_the_only_personal_address(self):
        for code in CODES:
            text = make_readmes.render("ARMOR-COMMON", code)
            addresses = set(re.findall(r"[\w.+-]+@[\w-]+\.[a-z.]+", text))
            self.assertEqual(addresses, {"electrohobby3d@gmail.com"}, code)

    def test_the_glance_table_only_appears_when_the_repository_states_its_hardware(self):
        for name in ORDER:
            data = make_readmes.load(name)
            with_table = "## 📋" in make_readmes.render(name, "en")
            self.assertEqual(with_table, "hardware" in data.TEXT["en"], name)

    def test_screenshots_are_a_table_of_two_columns(self):
        name = next(iter(SHOTS))
        text = make_readmes.render(name, "en")
        self.assertIn("<table>", text)
        self.assertEqual(text.count("<td "), len(SHOTS[name]))
        for file, _key in SHOTS[name]:
            self.assertIn(f"images/screenshots/{file}.png", text)

    def test_outputs_are_eight_files_per_repository_in_its_folder(self):
        files = make_readmes.outputs()
        self.assertEqual(len(files), len(ORDER) * 8)
        self.assertIn(self.root / "ARMOR-NODE-RADAR" / "README_zho.md", files)


class MainTests(unittest.TestCase):
    def setUp(self):
        self.holder, self.root = fake_root()
        self.addCleanup(self.holder.cleanup)
        patcher = mock.patch.object(make_readmes, "ROOT", self.root)
        patcher.start()
        self.addCleanup(patcher.stop)

    def run_main(self, *argv):
        out, err = io.StringIO(), io.StringIO()
        with mock.patch("sys.argv", ["make_readmes.py", *argv]), contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            code = make_readmes.main()
        return code, out.getvalue(), err.getvalue()

    def test_check_fails_when_the_readmes_are_missing_and_does_not_write_them(self):
        code, _out, err = self.run_main("--check")
        self.assertEqual(code, 1)
        self.assertIn("out of date", err)
        self.assertFalse((self.root / "ARMOR-NODE-RADAR" / "README.md").exists())

    def test_writing_then_checking_is_stable(self):
        code, out, _err = self.run_main()
        self.assertEqual(code, 0)
        self.assertIn(f"written: {len(ORDER) * 8}", out)
        code, out, _err = self.run_main("--check")
        self.assertEqual(code, 0)
        self.assertIn("current", out)

    def test_windows_line_endings_do_not_count_as_a_difference(self):
        self.run_main()
        path = self.root / "ARMOR-NODE-HMI" / "README.md"
        path.write_bytes(path.read_bytes().replace(b"\n", b"\r\n"))
        self.assertEqual(self.run_main("--check")[0], 0)

    def test_check_names_the_stale_file_after_a_manifest_changes(self):
        self.run_main()
        manifest = self.root / "ARMOR-SERVER" / "armor.project.json"
        manifest.write_text(json.dumps({"version": "9.9.9", "maturity": "functional", "stack": "x"}), encoding="utf-8")
        code, _out, err = self.run_main("--check")
        self.assertEqual(code, 1)
        stale = [line.strip() for line in err.splitlines()[1:]]
        self.assertEqual(len(stale), 8)
        self.assertTrue(all("ARMOR-SERVER" in line for line in stale), stale)

    def test_written_files_use_unix_line_endings(self):
        self.run_main()
        self.assertNotIn(b"\r\n", (self.root / "ARMOR-NODE-RADAR" / "README_jpn.md").read_bytes())


if __name__ == "__main__":
    unittest.main()
