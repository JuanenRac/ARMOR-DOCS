import contextlib
import io
import json
import tempfile
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path
from unittest import mock

import _support  # noqa: F401  (puts tools/ on the path)

import brand_banner
import make_brand
import make_catalog
from make_readmes import ORDER

OLD_TABLE = "| Repository | Version | Responsibility | Maturity |\n|---|---|---|---|\n| ARMOR-OLD | 0.0.1 | old | Scaffolding |"


def fake_root():
    holder = tempfile.TemporaryDirectory()
    root = Path(holder.name)
    for index, name in enumerate(ORDER):
        (root / name).mkdir()
        (root / name / "armor.project.json").write_text(json.dumps({"version": f"0.{index}.1", "role": f"Role of {name}", "maturity": ["scaffolding", "functional", "established", "production"][index % 4]}), encoding="utf-8")
    return holder, root


class CatalogTests(unittest.TestCase):
    def setUp(self):
        self.holder, self.root = fake_root()
        self.addCleanup(self.holder.cleanup)
        self.catalog = self.root / "catalog.md"
        for target, value in (("ROOT", self.root), ("CATALOG", self.catalog)):
            patcher = mock.patch.object(make_catalog, target, value)
            patcher.start()
            self.addCleanup(patcher.stop)

    def run_main(self, *argv):
        out, err = io.StringIO(), io.StringIO()
        with mock.patch("sys.argv", ["make_catalog.py", *argv]), contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            code = make_catalog.main()
        return code, out.getvalue(), err.getvalue()

    def test_table_has_one_row_per_repository_in_order(self):
        rows = make_catalog.table().splitlines()
        self.assertEqual(len(rows), 2 + len(ORDER))
        for name, row in zip(ORDER, rows[2:], strict=True):
            self.assertTrue(row.startswith(f"| {name} |"), row)
        self.assertIn("| ARMOR-COMMON | 0.0.1 | Role of ARMOR-COMMON | Scaffolding |", rows)

    def test_first_run_replaces_the_hand_written_table_and_keeps_the_text_around_it(self):
        current = f"# Catalogue\n\nIntro.\n\n{OLD_TABLE}\n\nAfter the table.\n"
        new = make_catalog.render(current)
        self.assertNotIn("ARMOR-OLD", new)
        self.assertIn(make_catalog.BEGIN, new)
        self.assertIn(make_catalog.END, new)
        self.assertTrue(new.startswith("# Catalogue\n\nIntro.\n\n"))
        self.assertTrue(new.endswith("\n\nAfter the table.\n"))

    def test_render_is_idempotent(self):
        once = make_catalog.render(f"Intro\n\n{OLD_TABLE}\n\nEnd\n")
        self.assertEqual(make_catalog.render(once), once)

    def test_markers_limit_what_is_replaced(self):
        current = f"Top\n{make_catalog.BEGIN}\nstale\n{make_catalog.END}\nBottom\n"
        new = make_catalog.render(current)
        self.assertNotIn("stale", new)
        self.assertTrue(new.startswith("Top\n"))
        self.assertTrue(new.endswith("\nBottom\n"))

    def test_check_fails_on_a_stale_table_and_leaves_the_file(self):
        self.catalog.write_text(f"Intro\n{make_catalog.BEGIN}\nstale\n{make_catalog.END}\n", encoding="utf-8")
        before = self.catalog.read_text(encoding="utf-8")
        code, _out, err = self.run_main("--check")
        self.assertEqual(code, 1)
        self.assertIn("out of date", err)
        self.assertEqual(self.catalog.read_text(encoding="utf-8"), before)

    def test_write_then_check_passes_and_a_version_change_makes_it_stale(self):
        self.catalog.write_text(f"Intro\n\n{OLD_TABLE}\n\nEnd\n", encoding="utf-8")
        self.assertEqual(self.run_main()[0], 0)
        self.assertEqual(self.run_main("--check")[0], 0)
        manifest = self.root / "ARMOR-NODE-HMI" / "armor.project.json"
        data = json.loads(manifest.read_text(encoding="utf-8"))
        data["version"] = "9.9.9"
        manifest.write_text(json.dumps(data), encoding="utf-8")
        self.assertEqual(self.run_main("--check")[0], 1)
        self.assertEqual(self.run_main()[0], 0)
        self.assertIn("| ARMOR-NODE-HMI | 9.9.9 |", self.catalog.read_text(encoding="utf-8"))

    def test_windows_line_endings_in_the_file_are_not_a_difference(self):
        self.catalog.write_text(f"Intro\n\n{OLD_TABLE}\n\nEnd\n", encoding="utf-8")
        self.run_main()
        self.catalog.write_bytes(self.catalog.read_bytes().replace(b"\n", b"\r\n"))
        self.assertEqual(self.run_main("--check")[0], 0)

    def test_an_unknown_maturity_is_an_error_not_a_blank(self):
        manifest = self.root / "ARMOR-NODE-HMI" / "armor.project.json"
        manifest.write_text(json.dumps({"version": "1.0.0", "role": "x", "maturity": "nonsense"}), encoding="utf-8")
        with self.assertRaises(KeyError):
            make_catalog.table()


class BrandTests(unittest.TestCase):
    def test_every_repository_of_the_family_has_a_banner_entry_and_a_drawing(self):
        self.assertEqual(set(make_brand.REPOS), set(ORDER))
        self.assertEqual(set(make_brand.POSITIONS), set(ORDER))
        for name in ORDER:
            self.assertTrue(make_brand.glyph(name).strip(), name)

    def test_the_arrows_only_join_known_repositories(self):
        for source, target in make_brand.ARROWS:
            self.assertIn(source, make_brand.POSITIONS)
            self.assertIn(target, make_brand.POSITIONS)
            self.assertNotEqual(source, target)

    def test_no_two_repositories_share_a_place_in_the_map(self):
        places = list(make_brand.POSITIONS.values())
        self.assertEqual(len(places), len(set(places)))

    def test_every_asset_is_well_formed_xml(self):
        for name, entry in make_brand.REPOS.items():
            root = ET.fromstring(make_brand.banner(name, entry["kind"], entry["group"], entry["technologies"]))
            self.assertTrue(root.tag.endswith("svg"), name)
            ET.fromstring(make_brand.icon(name))
        ET.fromstring(make_brand.family_map())

    def test_text_is_escaped(self):
        svg = make_brand.banner("ARMOR-NODE-RADAR", "A & B <C>", "R&D", ["<TAG>", "x & y"])
        ET.fromstring(svg)
        self.assertIn("A.R.M.O.R. · A &amp; B &lt;C&gt;", svg)
        self.assertIn(">R&amp;D</text>", svg)
        self.assertIn("&lt;TAG&gt;", svg)
        self.assertNotIn("<TAG>", svg)

    def test_the_banner_names_the_repository_and_shows_its_kind_group_and_first_four_technologies(self):
        entry = make_brand.REPOS["ARMOR-NODE-RADAR"]
        svg = make_brand.banner("ARMOR-NODE-RADAR", entry["kind"], entry["group"], entry["technologies"])
        self.assertIn(">ARMOR-NODE-RADAR</text>", svg)
        self.assertIn(f">A.R.M.O.R. · {entry['kind']}</text>", svg)
        self.assertIn(f">{entry['group']}</text>", svg)
        for technology in entry["technologies"][:4]:
            self.assertIn(f">{technology.upper()}</text>", svg)

    def test_a_long_list_of_technologies_loses_whole_technologies_never_half_of_one(self):
        line = brand_banner.technology_line(["ONE", "T" * 40, "U" * 40, "LAST"])
        self.assertEqual(line, "ONE · " + "T" * 40)
        self.assertNotIn("...", line)

    def test_the_width_of_a_pill_and_of_the_label_follow_the_length_of_the_text(self):
        self.assertEqual([brand_banner.pill_width(text) for text in ("MQTT", "ESP-IDF", "TYPESCRIPT")], [60, 80, 100])
        self.assertEqual([brand_banner.label_width(f"A.R.M.O.R. · {kind}") for kind in ("APP", "FIRMWARE")], [182, 231])

    def test_a_long_name_is_set_smaller_so_that_it_ends_before_the_edge(self):
        self.assertEqual(brand_banner.name_size("ARMOR-NODE-ALARM"), 56)
        self.assertLess(brand_banner.name_size("ARMOR-ANDROID-CONTROL"), brand_banner.name_size("ARMOR-IOS-CONTROL"))

    def test_the_map_has_a_box_for_every_repository(self):
        svg = make_brand.family_map()
        for name in ORDER:
            self.assertIn(f">{name}</text>", svg)

    def test_outputs_are_a_banner_and_an_icon_per_repository_plus_the_two_family_files(self):
        root = Path("somewhere")
        files = make_brand.outputs(root)
        self.assertEqual(len(files), 2 * len(ORDER) + 2)
        self.assertIn(root / "ARMOR-NODE-RADAR" / "images" / "ARMOR_BANNER.svg", files)
        self.assertIn(root / "ARMOR-DOCS" / "images" / "ARMOR_FAMILY.svg", files)
        self.assertIn(root / "ARMOR-DOCS" / "brand" / "ARMOR_ICON.svg", files)

    def test_generation_is_deterministic(self):
        self.assertEqual(make_brand.outputs(Path("a")).keys() == make_brand.outputs(Path("a")).keys(), True)
        self.assertEqual(make_brand.family_map(), make_brand.family_map())

    def run_main(self, root, *argv):
        out, err = io.StringIO(), io.StringIO()
        with mock.patch("sys.argv", ["make_brand.py", "--root", str(root), *argv]), contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            code = make_brand.main()
        return code, out.getvalue(), err.getvalue()

    def test_write_then_check_and_a_hand_edit_is_reported(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            for name in ORDER:
                (root / name).mkdir()
            code, _out, err = self.run_main(root, "--check")
            self.assertEqual(code, 1)   # nothing written yet
            self.assertIn("out of date", err)
            self.assertFalse((root / "ARMOR-NODE-RADAR" / "images").exists())   # a check never writes
            self.assertEqual(self.run_main(root)[0], 0)
            self.assertEqual(self.run_main(root, "--check")[0], 0)
            banner = root / "ARMOR-VISION" / "images" / "ARMOR_BANNER.svg"
            banner.write_text("<svg/>", encoding="utf-8")
            code, _out, err = self.run_main(root, "--check")
            self.assertEqual(code, 1)
            self.assertIn("ARMOR_BANNER.svg", err)
            self.assertEqual(self.run_main(root)[0], 0)
            self.assertNotEqual(banner.read_text(encoding="utf-8"), "<svg/>")

    def test_a_repository_that_is_not_checked_out_is_skipped(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / "ARMOR-DOCS").mkdir()
            self.assertEqual(self.run_main(root)[0], 0)
            self.assertTrue((root / "ARMOR-DOCS" / "images" / "ARMOR_FAMILY.svg").is_file())
            self.assertFalse((root / "ARMOR-NODE-RADAR").exists())


if __name__ == "__main__":
    unittest.main()
