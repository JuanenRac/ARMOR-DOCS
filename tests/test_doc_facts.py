import json
import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest import mock

import _support  # noqa: F401  (puts tools/ on the path)

import doc_facts


def family_with_contracts(root: Path, vectors: dict[str, int], paths: int = 3) -> None:
    common = root / "ARMOR-COMMON"
    (common / "conformance").mkdir(parents=True)
    (common / "src" / "armor_common" / "schemas").mkdir(parents=True)
    (common / "openapi").mkdir()
    (common / "armor.project.json").write_text(json.dumps({"version": "1.2.3.4"}), encoding="utf-8")
    for kind, count in vectors.items():
        (common / "conformance" / f"{kind}.json").write_text(json.dumps({"kind": kind, "vectors": [{}] * count}), encoding="utf-8")
        (common / "src" / "armor_common" / "schemas" / f"{kind}.schema.json").write_text("{}", encoding="utf-8")
    routes = "".join(f"  /api/v1/r{n}:\n    get: {{}}\n" for n in range(paths))
    (common / "openapi" / "armor-server.yaml").write_text(f"openapi: 3.1.0\npaths:\n{routes}components:\n  schemas: {{}}\n", encoding="utf-8")


class FactTests(unittest.TestCase):
    def setUp(self):
        self.holder = tempfile.TemporaryDirectory()
        self.root = Path(self.holder.name)
        family_with_contracts(self.root, {"telemetry": 5, "network": 7}, paths=4)
        patcher = mock.patch.object(doc_facts, "FAMILY", self.root)
        patcher.start()
        self.addCleanup(patcher.stop)
        self.addCleanup(self.holder.cleanup)

    def test_the_figures_are_counted_in_the_repository(self):
        self.assertEqual(doc_facts.value("vectors"), "12")
        self.assertEqual(doc_facts.value("vectors:network"), "7")
        self.assertEqual(doc_facts.value("schemas"), "2")
        self.assertEqual(doc_facts.value("openapi_paths"), "4")
        self.assertEqual(doc_facts.value("version:ARMOR-COMMON"), "1.2.3.4")

    def test_the_tests_a_node_registers_with_ctest_are_counted_by_name_and_split_into_host_programs_and_python_checks(self):
        node = self.root / "ARMOR-NODE-X"
        (node / "tests").mkdir(parents=True)
        (node / "armor.project.json").write_text(json.dumps({"version": "0.0.1"}), encoding="utf-8")
        (node / "tests" / "CMakeLists.txt").write_text(
            "add_test(NAME core COMMAND test_core)\n"
            "add_test(NAME node COMMAND test_node ${CMAKE_CURRENT_SOURCE_DIR}/../x)\n"
            "if(Python3_FOUND)\n"
            "  add_test(NAME routes COMMAND ${Python3_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/check_routes.py)\n"
            "endif()\n"
            "if(TARGET stand_in)\n"
            "  add_test(NAME failover COMMAND ${Python3_EXECUTABLE} check.py $<TARGET_FILE:stand_in>)\n"
            "else()\n"
            "  add_test(NAME failover COMMAND ${Python3_EXECUTABLE} check.py)\n"
            "endif()\n", encoding="utf-8")
        self.assertEqual(doc_facts.value("ctest_cpp:ARMOR-NODE-X"), "2")
        self.assertEqual(doc_facts.value("ctest_python:ARMOR-NODE-X"), "2")   # the two branches of the if/else register one test
        with self.assertRaises(doc_facts.Unavailable):
            doc_facts.value("ctest_cpp:ARMOR-COMMON")   # no tests/CMakeLists.txt there

    def test_unittest_is_the_count_of_test_functions_under_another_name(self):
        common = self.root / "ARMOR-COMMON"
        (common / "tests").mkdir()
        (common / "tests" / "test_a.py").write_text("class T:\n    def test_one(self): pass\n    def test_two(self): pass\n", encoding="utf-8")
        self.assertEqual(doc_facts.value("unittest:ARMOR-COMMON"), doc_facts.value("tests:ARMOR-COMMON"))
        self.assertEqual(doc_facts.value("unittest:ARMOR-COMMON"), "2")

    def test_a_name_that_means_nothing_is_an_error_and_a_missing_repository_is_unavailable(self):
        with self.assertRaises(KeyError):
            doc_facts.value("lines")
        with self.assertRaises(KeyError):
            doc_facts.value("vectors:nothing")
        with self.assertRaises(doc_facts.Unavailable):
            doc_facts.value("version:ARMOR-SERVER")

    def test_render_rewrites_the_marked_figures_and_only_those(self):
        text = "has <!--fact:vectors-->1<!--/fact--> vectors, <!--fact:vectors:network-->7<!--/fact--> of network and 1318 typed by hand"
        new, changed, skipped = doc_facts.render(text)
        self.assertEqual(new, "has <!--fact:vectors-->12<!--/fact--> vectors, <!--fact:vectors:network-->7<!--/fact--> of network and 1318 typed by hand")
        self.assertEqual(changed, ["vectors: 1 -> 12"])
        self.assertEqual(skipped, [])

    def test_a_figure_whose_repository_is_missing_is_left_alone_and_said(self):
        text = "<!--fact:version:ARMOR-SERVER-->0.1<!--/fact-->"
        new, changed, skipped = doc_facts.render(text)
        self.assertEqual((new, changed), (text, []))
        self.assertEqual(len(skipped), 1)

    def test_the_committed_state_is_read_not_the_working_tree(self):
        common = self.root / "ARMOR-COMMON"
        environment = _support.git_environment()
        for args in (["init", "-q", "-b", "main"], ["add", "-A"], ["commit", "-q", "-m", "Add"]):
            subprocess.run(["git", "-C", str(common), *args], check=True, capture_output=True, env=environment)
        (common / "conformance" / "network.json").write_text(json.dumps({"vectors": [{}] * 70}), encoding="utf-8")   # edited, not committed
        self.assertEqual(doc_facts.value("vectors"), "12")
        with mock.patch.dict("os.environ", {"ARMOR_FACTS_SOURCE": "worktree"}):
            self.assertEqual(doc_facts.value("vectors"), "75")


class VerifiedTests(unittest.TestCase):
    def setUp(self):
        self.holder = tempfile.TemporaryDirectory()
        self.addCleanup(self.holder.cleanup)
        family_with_contracts(Path(self.holder.name), {"telemetry": 1})   # ARMOR-COMMON 1.2.3.4
        patcher = mock.patch.object(doc_facts, "FAMILY", Path(self.holder.name))
        patcher.start()
        self.addCleanup(patcher.stop)

    def test_the_markers_are_read_with_the_version_now(self):
        text = "| row | Verified | seen <!--verified:ARMOR-COMMON 1.2.0.1--> |\n<!--verified:ARMOR-SERVER 0.7--><!--verified:ARMOR-COMMON 1.2.3.4-->"
        self.assertEqual(doc_facts.verified(text), [("ARMOR-COMMON", "1.2.0.1", "1.2.3.4"), ("ARMOR-SERVER", "0.7", None), ("ARMOR-COMMON", "1.2.3.4", "1.2.3.4")])

    def test_a_row_verified_in_a_version_the_repository_does_not_have_yet_fails(self):
        self.assertEqual(doc_facts.verified_problems("<!--verified:ARMOR-COMMON 1.2.3.4--><!--verified:ARMOR-COMMON 1.2.0.9-->"), [])
        self.assertEqual(len(doc_facts.verified_problems("<!--verified:ARMOR-COMMON 1.10.0.0-->")), 1)   # compared as numbers, not as text


class DocumentsTests(unittest.TestCase):
    def test_the_figures_of_the_documents_of_this_repository_are_current(self):
        """The documents are checked against the contracts repository when it is next to this one (the CI of this repository fetches it)."""
        if not (doc_facts.FAMILY / "ARMOR-COMMON" / "armor.project.json").exists():
            self.skipTest("ARMOR-COMMON is not next to ARMOR-DOCS")
        self.assertEqual(doc_facts.main(["--check"]), 0)
