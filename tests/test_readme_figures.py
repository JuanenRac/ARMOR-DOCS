import tempfile
import unittest
from pathlib import Path
from unittest import mock

import _support  # noqa: F401  (puts tools/ on the path)

import doc_facts
import make_readmes
from test_doc_facts import family_with_contracts


class FigureTests(unittest.TestCase):
    def family(self, vectors, paths=3):
        holder = tempfile.TemporaryDirectory()
        self.addCleanup(holder.cleanup)
        root = Path(holder.name)
        family_with_contracts(root, vectors, paths)
        (root / "ARMOR-COMMON" / "tests").mkdir()
        (root / "ARMOR-COMMON" / "tests" / "test_a.py").write_text("def test_one(): pass\n    def test_two(): pass\nasync def test_three(): pass\n", encoding="utf-8")
        patches = [mock.patch.object(doc_facts, "FAMILY", root), mock.patch.dict("os.environ", {"ARMOR_FACTS_SOURCE": "worktree"}), mock.patch.object(make_readmes, "ROOT", root), mock.patch.dict(make_readmes._FACTS, clear=True)]
        for patch in patches:
            patch.start()
            self.addCleanup(patch.stop)

    def test_the_figures_are_read_from_the_files_of_the_contracts(self):
        self.family({"a": 4, "b": 6}, paths=5)
        self.assertEqual(doc_facts.value("vectors"), "10")
        self.assertEqual(doc_facts.value("vectors:a+b"), "10")
        self.assertEqual(doc_facts.value("openapi_paths"), "5")
        self.assertEqual(doc_facts.value("openapi_operations"), "5")
        self.assertEqual(doc_facts.value("tests:ARMOR-COMMON"), "3")   # test functions and methods, also the async ones

    def test_a_token_in_a_source_becomes_the_figure(self):
        self.family({"a": 4, "b": 6})
        self.assertEqual(make_readmes.facts_in("{{fact:vectors}} vectors, {{fact:vectors:a}} of one", "x"), "10 vectors, 4 of one")
        with self.assertRaises(SystemExit):
            make_readmes.facts_in("{{fact:nothing}}", "x")

    def test_a_typed_figure_that_is_not_the_real_one_is_found(self):
        self.family({"a": 4, "b": 6}, paths=5)
        self.assertEqual(make_readmes.typed_figure_problems(Path("ARMOR-X/README.md"), "10 conformance vectors, and 4 conformance vectors of one message"), [])
        wrong = make_readmes.typed_figure_problems(Path("ARMOR-X/README.md"), "1370 conformance vectors and 1380 vectores de conformidad")
        self.assertEqual(len(wrong), 2)
        self.assertEqual(make_readmes.typed_figure_problems(Path("ARMOR-X/README.md"), "the OpenAPI file describes 190 paths"), ["ARMOR-X: '190 paths' but the repository has 5 (openapi_paths)"])
        self.assertEqual(make_readmes.typed_figure_problems(Path("ARMOR-X/README.md"), "its own API has 55 paths"), [])


if __name__ == "__main__":
    unittest.main()
