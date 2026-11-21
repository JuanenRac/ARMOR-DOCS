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

    def test_kotlin_tests_are_counted_in_every_test_folder_and_added_to_the_python_ones(self):
        watch = self.root / "ARMOR-X"
        files = {
            "src/test/kotlin/a/ATest.kt": "class A {\n    @Test\n    fun one() {}\n    @Test fun two() {}\n    @TestOnly fun not() {}\n}\n",
            "wear/src/test/kotlin/b/BTest.kt": "class B {\n    @Test\n    fun three() {}\n}\n",
            "src/main/kotlin/c/CTest.kt": "class C {\n    @Test\n    fun ignored() {}\n}\n",
        }
        watch.mkdir()
        (watch / "armor.project.json").write_text("{}", encoding="utf-8")
        for name, body in files.items():
            (watch / name).parent.mkdir(parents=True, exist_ok=True)
            (watch / name).write_text(body, encoding="utf-8")
        (watch / "tests").mkdir()
        (watch / "tests" / "test_a.py").write_text("def test_x(): pass\n", encoding="utf-8")
        self.assertEqual(doc_facts.value("kotlin_tests:ARMOR-X"), "3")
        self.assertEqual(doc_facts.value("tests_all:ARMOR-X"), "4")

    def test_kotlin_tests_of_a_repository_without_any_are_unavailable_not_zero(self):
        with self.assertRaises(doc_facts.Unavailable):
            doc_facts.value("kotlin_tests:ARMOR-COMMON")

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


class SourceFigureTests(unittest.TestCase):
    """The figures read from the source of the server and of Studio, and the figures typed in docs/structure.json."""

    def setUp(self):
        self.holder = tempfile.TemporaryDirectory()
        self.root = Path(self.holder.name)
        family_with_contracts(self.root, {"telemetry": 5, "network": 7})
        patcher = mock.patch.object(doc_facts, "FAMILY", self.root)
        patcher.start()
        self.addCleanup(patcher.stop)
        self.addCleanup(self.holder.cleanup)

    def repository(self, name: str) -> Path:
        path = self.root / name
        (path / "src").mkdir(parents=True, exist_ok=True)
        (path / "armor.project.json").write_text(json.dumps({"version": "0.0.1"}), encoding="utf-8")
        return path

    def test_the_conformance_files_are_counted(self):
        self.assertEqual(doc_facts.value("conformance_files"), "2")

    def test_the_settings_of_the_security_file_are_the_keys_of_its_defaults_and_nothing_after_them(self):
        server = self.repository("ARMOR-SERVER")
        (server / "src" / "security_settings.ts").write_text(
            'export const OTHER = {\n  "not.counted": 1,\n};\n'
            'export const SECURITY_DEFAULTS: Readonly<Values> = Object.freeze({\n'
            '  "alarm.disarm_pin": "if_set",\n  "voice.turn_max_bytes": TURN.default,\n  "vision.service_url": "",\n});\n'
            'const NUMBER_RANGES = {\n  "voice.turn_max_bytes": TURN,\n};\n', encoding="utf-8")
        self.assertEqual(doc_facts.value("security_settings"), "3")

    def test_the_options_of_the_security_screen_are_the_entries_of_its_table(self):
        studio = self.repository("ARMOR-STUDIO")
        (studio / "src" / "SecurityPanel.tsx").write_text(
            'const OPTIONS: Array<Option> = [\n'
            '  { key: "alarm.disarm_pin", id: "pin", values: ["always"] },\n'
            '  { key: "voice.wake_word", id: "wakeword", values: [false, true], optional: true },   // a comment\n'
            '];\n'
            'const LIMITS = [\n  { key: "voice.turn_max_bytes", id: "turn" },\n];\n', encoding="utf-8")
        self.assertEqual(doc_facts.value("studio_security_options"), "2")

    def test_a_source_without_the_table_is_unavailable_not_zero(self):
        server = self.repository("ARMOR-SERVER")
        (server / "src" / "security_settings.ts").write_text("export const NOTHING = 1;\n", encoding="utf-8")
        with self.assertRaises(doc_facts.Unavailable):
            doc_facts.value("security_settings")
        with self.assertRaises(doc_facts.Unavailable):
            doc_facts.value("studio_security_options")   # Studio is not next to this repository

    def write_structure(self, name: str, entries: list[dict]) -> None:
        folder = self.repository(name) / "docs"
        folder.mkdir(exist_ok=True)
        (folder / "structure.json").write_text(json.dumps({"repo": name, "cards": [{"name": "group", "rows": entries}]}), encoding="utf-8")

    @staticmethod
    def entry(name: str, english: str, other: str) -> dict:
        return {"name": name, "desc": {"en": english, "es": other}}

    def test_a_structure_that_states_the_real_figures_has_no_problem(self):
        common = self.root / "ARMOR-COMMON"
        (common / "tests").mkdir()
        (common / "tests" / "test_a.py").write_text("def test_one(): pass\ndef test_two(): pass\n", encoding="utf-8")
        (common / "tests" / "test_b.py").write_text("def test_three(): pass\n", encoding="utf-8")
        self.write_structure("ARMOR-COMMON", [
            self.entry("tests/", "3 tests in 2 modules", "3 pruebas en 2 modulos"),
            self.entry("schemas/", "2 JSON Schemas", "2 JSON Schema"),
            self.entry("conformance/", "12 accepted and rejected payloads", "12 casos"),
        ])
        self.assertEqual(doc_facts.structure_problems(["ARMOR-COMMON"]), [])

    def test_a_figure_that_is_not_the_real_one_or_that_a_language_does_not_carry_is_named(self):
        common = self.root / "ARMOR-COMMON"
        (common / "tests").mkdir()
        (common / "tests" / "test_a.py").write_text("def test_one(): pass\n", encoding="utf-8")
        self.write_structure("ARMOR-COMMON", [
            self.entry("tests/", "9 tests in 4 modules", "9 pruebas en 4 modulos"),
            self.entry("schemas/", "2 JSON Schemas", "dos JSON Schema"),
        ])
        found = doc_facts.structure_problems(["ARMOR-COMMON"])
        self.assertEqual(len(found), 3)
        self.assertTrue(any("9 tests in tests/ but the repository has 1" in item for item in found))
        self.assertTrue(any("4 test modules in tests/ but the repository has 1" in item for item in found))
        self.assertTrue(any("does not carry the figure 2 in es" in item for item in found))

    def test_a_repository_whose_tests_are_not_python_is_skipped(self):
        self.write_structure("ARMOR-SERVER", [self.entry("tests/", "1389 tests, unit and HTTP", "1389 pruebas")])
        self.assertEqual(doc_facts.structure_problems(["ARMOR-SERVER"]), [])

    def test_the_structure_flag_and_the_check_fail_on_a_wrong_figure(self):
        self.write_structure("ARMOR-COMMON", [self.entry("schemas/", "7 JSON Schemas", "7 JSON Schema")])
        with mock.patch("builtins.print") as shown:
            self.assertEqual(doc_facts.main(["--structure"]), 1)
        self.assertIn("STRUCTURE_FIGURES=FAIL", [call.args[0] for call in shown.call_args_list])

    def test_the_test_modules_and_the_tests_of_one_file_are_counted(self):
        common = self.root / "ARMOR-COMMON"
        (common / "tests").mkdir()
        (common / "tests" / "test_a.py").write_text("def test_one(): pass\ndef test_two(): pass\n", encoding="utf-8")
        (common / "tests" / "test_b.py").write_text("def test_three(): pass\n", encoding="utf-8")
        (common / "tests" / "helper.py").write_text("def test_not_a_module(): pass\n", encoding="utf-8")
        self.assertEqual(doc_facts.value("test_modules:ARMOR-COMMON"), "2")
        self.assertEqual(doc_facts.value("tests_in:ARMOR-COMMON:test_a.py"), "2")
        with self.assertRaises(doc_facts.Unavailable):
            doc_facts.value("tests_in:ARMOR-COMMON:test_missing.py")

    def test_a_figure_of_a_description_is_written_as_a_marker_with_its_last_value(self):
        common = self.root / "ARMOR-COMMON"
        (common / "tests").mkdir()
        (common / "tests" / "test_a.py").write_text("def test_one(): pass\n", encoding="utf-8")
        self.write_structure("ARMOR-COMMON", [
            self.entry("tests/", "{{fact:tests:ARMOR-COMMON|1}} tests", "{{fact:tests:ARMOR-COMMON|1}} pruebas"),
            self.entry("schemas/", "{{fact:schemas|2}} JSON Schemas", "{{fact:schemas|2}} JSON Schema"),
        ])
        self.assertEqual(doc_facts.structure_problems(["ARMOR-COMMON"]), [])

    def test_a_marker_whose_last_value_is_not_the_figure_is_named_and_fix_rewrites_it(self):
        common = self.root / "ARMOR-COMMON"
        (common / "tests").mkdir()
        (common / "tests" / "test_a.py").write_text("def test_one(): pass\ndef test_two(): pass\n", encoding="utf-8")
        self.write_structure("ARMOR-COMMON", [self.entry("docs/", "{{fact:tests:ARMOR-COMMON|9}} checks", "{{fact:tests:ARMOR-COMMON|9}} comprobaciones")])
        found = doc_facts.structure_problems(["ARMOR-COMMON"])
        self.assertEqual(len(found), 2)
        self.assertTrue(all("{{fact:tests:ARMOR-COMMON|9}} but the figure is 2" in item for item in found))
        self.assertEqual(doc_facts.fix_structure(["ARMOR-COMMON"]), ["ARMOR-COMMON"])
        self.assertEqual(doc_facts.structure_problems(["ARMOR-COMMON"]), [])
        self.assertEqual(doc_facts.fix_structure(["ARMOR-COMMON"]), [])   # nothing left to write

    def test_a_marker_whose_source_is_not_here_keeps_its_last_value_and_one_that_means_nothing_is_named(self):
        self.write_structure("ARMOR-COMMON", [self.entry("docs/", "{{fact:tests:ARMOR-VISION|43}} checks", "{{fact:tests:ARMOR-VISION|43}} comprobaciones")])
        self.assertEqual(doc_facts.structure_problems(["ARMOR-COMMON"]), [])
        self.write_structure("ARMOR-COMMON", [self.entry("docs/", "{{fact:no_such_figure|1}} checks", "{{fact:no_such_figure|1}} comprobaciones")])
        self.assertTrue(any("means nothing" in item for item in doc_facts.structure_problems(["ARMOR-COMMON"])))

    def test_the_picture_tool_writes_the_figure_where_doc_facts_can_read_it_and_the_last_value_where_it_cannot(self):
        import make_structure   # noqa: PLC0415

        spec = {"a": ["{{fact:schemas|99}} schemas"], "b": {"c": "{{fact:vectors:network|98}} vectors, {{fact:tests:ARMOR-VISION|43}} tests"}, "n": 3}
        self.assertEqual(make_structure.resolve_facts(spec), {"a": ["2 schemas"], "b": {"c": "7 vectors, 43 tests"}, "n": 3})
        with self.assertRaises(make_structure.SpecError):
            make_structure.resolve_facts("{{fact:no_such_figure|1}}")
        with mock.patch.dict("sys.modules", {"doc_facts": None}):   # a repository that does not have the tool
            self.assertEqual(make_structure.resolve_facts(spec["a"]), ["99 schemas"])


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
