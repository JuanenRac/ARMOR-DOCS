"""The baseline validation every repository runs in CI (manifest, version restated in the docs, changelog order, README parity, local links)."""
import contextlib
import io
import json
import tempfile
import unittest
from pathlib import Path
from unittest import mock

import _support  # noqa: F401  (puts tools/ on the path)

import armor_ci_validate as validate
import _armor_readme_parity as parity

VERSION = "0.8.2.1"


def manifest(**changes):
    data = {
        "schema_version": "1.0", "ecosystem": "A.R.M.O.R.", "name": "ARMOR-TEST", "version": VERSION, "role": "r", "stack": "s", "technologies": ["x"],
        "deployment_target": "d", "maturity": "functional", "family": "f", "parent": None, "build": "b", "notes": "n", "native_version": VERSION,
    }
    data.update(changes)
    return data


README = "# ARMOR-TEST\n\n## Overview\n\ntext [site](https://example.org)\n\n## Usage\n\nmore\n"


class Project:
    def __init__(self):
        self.holder = tempfile.TemporaryDirectory()
        self.root = Path(self.holder.name) / "ARMOR-TEST"
        self.root.mkdir()
        self.write("armor.project.json", json.dumps(manifest()))
        for name in validate.REQUIRED_DOCUMENTS:
            self.write(name, README if name.startswith("README") else "text")
        self.write("CHANGELOG.md", f"# Changelog\n\n## [{VERSION}] - 2000-01-01\n\n- Now.\n\n## [0.8.2.0] - 2000-01-01\n\n- Before.\n")

    def write(self, relative, text):
        (self.root / relative).write_text(text, encoding="utf-8", newline="\n")

    def run(self):
        err = io.StringIO()
        out = io.StringIO()
        with mock.patch.object(validate, "ROOT", self.root), mock.patch.object(validate, "MANIFEST_PATH", self.root / "armor.project.json"), \
                mock.patch.dict("os.environ", {"GITHUB_ACTIONS": "", "GITHUB_REPOSITORY": ""}), contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            try:
                code = validate.main()
            except SystemExit as stop:
                code = stop.code
        return code, out.getvalue(), err.getvalue()


class ValidateTests(unittest.TestCase):
    def setUp(self):
        self.project = Project()
        self.addCleanup(self.project.holder.cleanup)

    def assertFails(self, fragment):
        code, _out, err = self.project.run()
        self.assertEqual(code, 1, err)
        self.assertIn("CI_VALIDATION=FAIL", err)
        self.assertIn(fragment, err)

    def test_a_consistent_project_passes(self):
        code, out, _err = self.project.run()
        self.assertEqual(code, 0)
        self.assertIn(f"CI_VALIDATION=PASS project=ARMOR-TEST version={VERSION}", out)

    def test_unreadable_manifest(self):
        self.project.write("armor.project.json", "{ not json")
        self.assertFails("cannot read manifest")

    def test_missing_manifest_key(self):
        data = manifest()
        del data["role"]
        self.project.write("armor.project.json", json.dumps(data))
        self.assertFails("role")

    def test_other_ecosystem(self):
        self.project.write("armor.project.json", json.dumps(manifest(ecosystem="Other")))
        self.assertFails("ecosystem")

    def test_bad_versions(self):
        for bad in ("1.2", "1.2.3.4.5", "v1.2.3", "1.2.x", 3):
            self.project.write("armor.project.json", json.dumps(manifest(version=bad, native_version=bad)))
            self.assertFails("MAJOR.MINOR.PATCH")

    def test_native_version_must_equal_version(self):
        self.project.write("armor.project.json", json.dumps(manifest(native_version="0.8.2.0")))
        self.assertFails("differs from version")

    def test_unknown_maturity_and_empty_technologies(self):
        self.project.write("armor.project.json", json.dumps(manifest(maturity="beta")))
        self.assertFails("maturity")
        self.project.write("armor.project.json", json.dumps(manifest(technologies=[])))
        self.assertFails("technologies")

    def test_missing_required_document(self):
        (self.project.root / "README_por.md").unlink()
        self.assertFails("README_por.md")

    def test_changelog_head_must_be_the_manifest_version(self):
        self.project.write("CHANGELOG.md", "# Changelog\n\n## [0.8.2.0] - x\n")
        self.assertFails("latest changelog version 0.8.2.0 differs")
        self.project.write("CHANGELOG.md", "# Changelog\n\nnothing\n")
        self.assertFails("<none>")

    def test_a_stale_version_in_a_readme_label(self):
        self.project.write("README_fra.md", README + "\nVersion: 0.1.0\n")
        self.assertFails("README_fra.md")

    def test_a_current_version_in_a_readme_label_passes(self):
        for name in validate.REQUIRED_DOCUMENTS:
            if name.startswith("README"):
                self.project.write(name, README + f"\nVersion: {VERSION}\nARMOR-TEST v{VERSION}\n")
        self.assertEqual(self.project.run()[0], 0)

    def test_the_odometer_description_is_exempt_from_the_stale_version_check(self):
        for name in validate.REQUIRED_DOCUMENTS:
            if name.startswith("README"):
                self.project.write(name, README + "\nVersion: 0.0.9 -> 0.1.0\nStatus: 0.7.9 → 0.8.0.0\n")
        self.assertEqual(self.project.run()[0], 0)

    def test_the_project_name_followed_by_another_version_is_stale(self):
        self.project.write("README.md", README + "\nARMOR-TEST v0.1.0 does things\n")
        self.assertFails("states 0.1.0")

    def test_unreleased_must_be_at_the_top(self):
        self.project.write("CHANGELOG.md", f"# Changelog\n\n## [{VERSION}] - x\n\n## [Unreleased]\n\n## [0.8.2.0] - x\n")
        self.assertFails("Unreleased")

    def test_unreleased_at_the_top_is_allowed(self):
        self.project.write("CHANGELOG.md", f"# Changelog\n\n## [Unreleased]\n\n## [{VERSION}] - x\n")
        # the first version heading is what is compared with the manifest
        self.assertEqual(self.project.run()[0], 0)

    def test_changelog_duplicates_and_disorder(self):
        self.project.write("CHANGELOG.md", f"# Changelog\n\n## [{VERSION}] - x\n\n## [{VERSION}] - y\n")
        self.assertFails("two entries")
        self.project.write("CHANGELOG.md", f"# Changelog\n\n## [{VERSION}] - x\n\n## [0.9.0.0] - y\n")
        self.assertFails("newest first")

    def test_the_changelog_order_compares_numbers_not_text(self):
        self.project.write("armor.project.json", json.dumps(manifest(version="0.10.0", native_version="0.10.0")))
        self.project.write("CHANGELOG.md", "# Changelog\n\n## [0.10.0] - x\n\n## [0.9.0] - y\n")
        self.assertEqual(self.project.run()[0], 0)

    def test_pyproject_and_package_versions_must_match(self):
        self.project.write("pyproject.toml", '[project]\nversion = "0.0.1"\n')
        self.assertFails("pyproject.toml version 0.0.1")
        self.project.write("pyproject.toml", f'[project]\nversion = "{VERSION}"\n')
        self.assertEqual(self.project.run()[0], 0)
        self.project.write("pyproject.toml", "[project]\nname = 'x'\n")
        self.assertFails("missing its own")
        self.project.write("pyproject.toml", f'[project]\nversion = "{VERSION}"\n')
        (self.project.root / "src" / "pkg").mkdir(parents=True)
        (self.project.root / "src" / "pkg" / "__init__.py").write_text('__version__ = "0.0.2"\n', encoding="utf-8")
        self.assertFails("__version__ 0.0.2")

    def test_an_env_file_must_be_ignored_by_git(self):
        self.project.write(".env", "A=1\n")
        self.assertFails(".env")
        self.project.write(".gitignore", "node_modules/\n.env\n")
        self.assertEqual(self.project.run()[0], 0)
        self.project.write(".gitignore", "# .env\nenvironment.txt\n")
        self.assertFails(".env")

    def test_a_broken_local_link(self):
        self.project.write("docs.md", "see [this](nowhere.md) and [web](https://example.org/x.md)")
        self.assertFails("docs.md:1 -> nowhere.md")

    def test_links_that_are_not_files_are_ignored(self):
        self.project.write("docs.md", "[a](https://x.org) [b](mailto:a@b.c) [c](#anchor) [d](/abs/path) [e](data:text/plain,x) ![img](nowhere.png)")
        self.assertEqual(self.project.run()[0], 0)

    def test_anchor_and_query_are_stripped_before_the_file_is_looked_up(self):
        self.project.write("target.md", "x")
        self.project.write("docs.md", '[a](target.md#section) [b](target.md?x=1) [c](<target.md>) [d](target.md "title")')
        self.assertEqual(self.project.run()[0], 0)

    def test_folders_of_dependencies_are_not_scanned(self):
        (self.project.root / "node_modules").mkdir()
        (self.project.root / "node_modules" / "x.md").write_text("[bad](missing.md)", encoding="utf-8")
        self.assertEqual(self.project.run()[0], 0)

    def test_translations_must_have_the_structure_of_the_english_readme(self):
        self.project.write("README_ita.md", README.replace("## Usage", "## Other"))
        self.assertFails("README_ita.md section structure")
        self.project.write("README_ita.md", README.replace("https://example.org", "https://example.net"))
        self.assertFails("links do not match")

    def test_a_manifest_name_that_differs_from_the_folder_only_warns_outside_ci(self):
        self.project.write("armor.project.json", json.dumps(manifest(name="ARMOR-OTHER")))
        code, _out, err = self.project.run()
        self.assertEqual(code, 0)
        self.assertIn("warning", err)

    def test_in_github_the_manifest_name_must_be_the_repository(self):
        self.project.write("armor.project.json", json.dumps(manifest(name="ARMOR-OTHER")))
        err = io.StringIO()
        with mock.patch.object(validate, "ROOT", self.project.root), mock.patch.object(validate, "MANIFEST_PATH", self.project.root / "armor.project.json"), \
                mock.patch.dict("os.environ", {"GITHUB_ACTIONS": "true", "GITHUB_REPOSITORY": "JuanenRac/ARMOR-TEST"}), contextlib.redirect_stderr(err):
            with self.assertRaises(SystemExit):
                validate.main()
        self.assertIn("must match the repository", err.getvalue())


class ReadmeParityTests(unittest.TestCase):
    def test_signature_and_links(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "README.md"
            path.write_text("# T\n## 1. Overview\n### sub\n## Usage\n[a](https://x.org/a) [b](./local.md)\n", encoding="utf-8")
            self.assertEqual(parity.readme_section_signature(path), ["Overview", "Usage"])
            self.assertEqual(parity.readme_link_set(path), {"https://x.org/a"})

    def test_no_headings_is_an_empty_signature(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "README.md"
            path.write_text("just text", encoding="utf-8")
            self.assertEqual(parity.readme_section_signature(path), [])

    def test_missing_english_readme(self):
        with tempfile.TemporaryDirectory() as folder:
            problems = parity.check_readme_section_parity(Path(folder))
            self.assertEqual(len(problems), 1)
            self.assertIn("README.md is missing", problems[0])

    def test_missing_translations_are_not_a_parity_problem(self):
        with tempfile.TemporaryDirectory() as folder:
            (Path(folder) / "README.md").write_text("## A\n", encoding="utf-8")
            self.assertEqual(parity.check_readme_section_parity(Path(folder)), [])

    def test_missing_and_extra_links_are_named(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / "README.md").write_text("## A\n[x](https://one.org)\n", encoding="utf-8")
            (root / "README_spa.md").write_text("## A\n[x](https://two.org)\n", encoding="utf-8")
            (problem,) = parity.check_readme_section_parity(root)
            self.assertIn("https://one.org", problem)
            self.assertIn("https://two.org", problem)


if __name__ == "__main__":
    unittest.main()
