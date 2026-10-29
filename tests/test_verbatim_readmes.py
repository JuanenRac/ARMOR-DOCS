"""READMEs written by hand in the universal layout (readme_src/verbatim/<REPOSITORY>/): the generator fills in only the version and the maturity colour."""
import tempfile
import unittest
from pathlib import Path
from unittest import mock

import _support  # noqa: F401  (puts tools/ on the path)

import make_readmes
from make_readmes import LANGUAGES

NAME = "ARMOR-TEST"
BODY = "# T\n\n![v](https://img.shields.io/badge/Version-{{VERSION}}-0f6cbd.svg) ![m](https://img.shields.io/badge/Maturity-established-{{MATURITY_COLOR}}.svg)\n\n## 📋 Glance\n\n## 🚦 Status\n\n## 🎯 Overview\n"


def build(files=None, body=BODY):
    holder = tempfile.TemporaryDirectory()
    root = Path(holder.name)
    (root / NAME).mkdir()
    (root / NAME / "armor.project.json").write_text('{"version": "1.2.3", "maturity": "established"}', encoding="utf-8")
    verbatim = root / "verbatim"
    (verbatim / NAME).mkdir(parents=True)
    for _code, file, *_ in LANGUAGES:
        if files is None or file in files:
            (verbatim / NAME / (file + ".tpl")).write_text(body, encoding="utf-8")
    return holder, root, verbatim


class VerbatimReadmes(unittest.TestCase):
    def render(self, root, verbatim, code="en"):
        with mock.patch.object(make_readmes, "ROOT", root), mock.patch.object(make_readmes, "VERBATIM", verbatim):
            return make_readmes.render(NAME, code), make_readmes.verbatim_problems(NAME)

    def test_the_version_and_the_colour_come_from_the_manifest(self):
        holder, root, verbatim = build()
        with holder:
            text, problems = self.render(root, verbatim)
            self.assertIn("Version-1.2.3-0f6cbd", text)
            self.assertIn("Maturity-established-2EA44F", text)
            self.assertNotIn("{{", text)
            self.assertEqual(problems, [])

    def test_a_missing_language_is_a_problem(self):
        holder, root, verbatim = build(files={"README.md"})
        with holder:
            _text, problems = self.render(root, verbatim)
            self.assertTrue(any("README_spa.md is missing" in p for p in problems))

    def test_no_status_table_is_a_problem(self):
        holder, root, verbatim = build(body=BODY.replace("## 🚦 Status\n\n", ""))
        with holder:
            _text, problems = self.render(root, verbatim)
            self.assertTrue(any("no project status table" in p for p in problems))

    def test_different_headings_between_languages_are_a_problem(self):
        holder, root, verbatim = build()
        with holder:
            (verbatim / NAME / "README_fra.md.tpl").write_text(BODY.replace("## 🎯 Overview", "## 🔒 Overview"), encoding="utf-8")
            _text, problems = self.render(root, verbatim)
            self.assertTrue(any("headings of the fr README" in p for p in problems))

    def test_no_repository_keeps_a_hand_written_readme_once_it_has_a_source(self):
        """ARMOR-VOICE-AI was the first README in the universal layout and is now written from its source (readme_src/repos/ARMOR_VOICE_AI.py)."""
        self.assertFalse((make_readmes.VERBATIM / "ARMOR-VOICE-AI").exists())
        self.assertEqual(make_readmes.load("ARMOR-VOICE-AI").FACTS["layout"], "universal")


if __name__ == "__main__":
    unittest.main()
