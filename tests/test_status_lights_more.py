"""status_lights.py: what the answer of the CI becomes, how a repository without a manifest or with a broken one is refused, and what --suggest says about a light that could be better or is
above its ceiling. The call to gh is replaced by a double, so nothing here reaches a network."""
from __future__ import annotations

import contextlib
import importlib.util
import io
import json
import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest import mock

TOOL = Path(__file__).resolve().parents[1] / "tools" / "status_lights.py"
spec = importlib.util.spec_from_file_location("status_lights_more", TOOL)
status_lights = importlib.util.module_from_spec(spec)
spec.loader.exec_module(status_lights)


def answer(runs):
    return subprocess.CompletedProcess([], 0, stdout=json.dumps(runs), stderr="")


class CiStateTest(unittest.TestCase):
    def state(self, **kwargs):
        with mock.patch.object(status_lights.subprocess, "run", **kwargs):
            return status_lights.ci_state(Path("."))

    def test_the_last_completed_run_of_the_main_branch_decides(self):
        runs = [{"status": "in_progress", "conclusion": "", "headBranch": "main"}, {"status": "completed", "conclusion": "success", "headBranch": "feature"},
                {"status": "completed", "conclusion": "failure", "headBranch": "main"}, {"status": "completed", "conclusion": "success", "headBranch": "main"}]
        self.assertEqual(self.state(return_value=answer(runs)), "red")
        self.assertEqual(self.state(return_value=answer(runs[3:])), "green")
        self.assertEqual(self.state(return_value=answer([{"status": "completed", "conclusion": "success", "headBranch": "master"}])), "green")

    def test_a_cancelled_run_is_not_green(self):
        self.assertEqual(self.state(return_value=answer([{"status": "completed", "conclusion": "cancelled", "headBranch": "main"}])), "red")

    def test_no_run_of_the_main_branch_and_no_answer_are_unknown(self):
        self.assertEqual(self.state(return_value=answer([])), "unknown")
        self.assertEqual(self.state(return_value=answer([{"status": "completed", "conclusion": "success", "headBranch": "feature"}])), "unknown")
        self.assertEqual(self.state(return_value=subprocess.CompletedProcess([], 1, stdout="", stderr="no")), "unknown")
        self.assertEqual(self.state(return_value=subprocess.CompletedProcess([], 0, stdout="not json", stderr="")), "unknown")

    def test_a_missing_gh_a_timeout_and_an_os_error_are_unknown(self):
        for error in (FileNotFoundError("gh"), subprocess.TimeoutExpired("gh", 60), OSError("busy")):
            self.assertEqual(self.state(side_effect=error), "unknown", repr(error))


class RepositoryTest(unittest.TestCase):
    def setUp(self):
        holder = tempfile.TemporaryDirectory()
        self.addCleanup(holder.cleanup)
        self.root = Path(holder.name)

    def test_a_folder_without_a_manifest_is_refused(self):
        with contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit):
            status_lights.manifest_of(self.root)

    def test_a_manifest_that_is_not_json_is_refused(self):
        (self.root / "x.project.json").write_text("{not json", encoding="utf-8")
        with contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit):
            status_lights.manifest_of(self.root)

    def test_the_first_manifest_by_name_is_the_one_read(self):
        (self.root / "b.project.json").write_text('{"name": "B"}', encoding="utf-8")
        (self.root / "a.project.json").write_text('{"name": "A"}', encoding="utf-8")
        self.assertEqual(status_lights.manifest_of(self.root)["name"], "A")

    def test_a_workflow_file_with_either_extension_is_a_ci(self):
        self.assertFalse(status_lights.has_ci(self.root))
        workflows = self.root / ".github" / "workflows"
        workflows.mkdir(parents=True)
        self.assertFalse(status_lights.has_ci(self.root))
        (workflows / "notes.txt").write_text("x", encoding="utf-8")
        self.assertFalse(status_lights.has_ci(self.root))
        (workflows / "ci.yaml").write_text("x", encoding="utf-8")
        self.assertTrue(status_lights.has_ci(self.root))

    def test_a_test_in_a_folder_that_is_skipped_does_not_count(self):
        skipped = sorted(status_lights.SKIP_DIRS)[0]
        (self.root / skipped / "tests").mkdir(parents=True)
        (self.root / skipped / "tests" / "test_a.py").write_text("x", encoding="utf-8")
        self.assertFalse(status_lights.has_tests(self.root))
        (self.root / "tests").mkdir()
        self.assertFalse(status_lights.has_tests(self.root), "an empty tests folder is not a test")
        (self.root / "tests" / "one.py").write_text("x", encoding="utf-8")
        self.assertTrue(status_lights.has_tests(self.root))


class SuggestTest(unittest.TestCase):
    def run_main(self, state):
        out = io.StringIO()
        with mock.patch.object(status_lights, "evaluate", return_value=state), contextlib.redirect_stdout(out):
            code = status_lights.main(["--suggest", "--repo", str(Path(__file__).resolve().parents[1])])
        return code, out.getvalue()

    def test_a_light_below_its_ceiling_and_one_above_it_are_said_and_one_at_it_is_not(self):
        G, Y, O = status_lights.GREEN, status_lights.YELLOW, status_lights.ORANGE
        state = {"items": [
            {"label": "Tests", "light": O, "ceiling": G, "kind": "software", "why": "w1"},
            {"label": "Hardware", "light": G, "ceiling": Y, "kind": "hardware", "why": "nothing ran on a board"},
            {"label": "Integration", "light": Y, "ceiling": Y, "kind": "software", "why": "w3"},
            {"label": "Other", "light": "?", "ceiling": G, "kind": "software", "why": "w4"},
        ]}
        code, text = self.run_main(state)
        self.assertEqual(code, 0)
        lines = text.strip().splitlines()
        self.assertEqual(len(lines), 2)
        self.assertIn("Tests: orange could reach green", lines[0])
        self.assertIn("Hardware: green is ABOVE its ceiling yellow (nothing ran on a board)", lines[1])


if __name__ == "__main__":
    unittest.main()


class WhiteLightTest(unittest.TestCase):
    """A white light says that a row does not apply: only a hardware or integration row of a repository with no hardware may carry it."""

    def problems(self, kind, light, manifest=None, ceiling=None):
        manifest = {"evidence": "host-test", **(manifest or {})}
        item = {"index": 0, "label": "row", "kind": kind, "light": light, "ceiling": ceiling or status_lights.GREEN, "why": "test"}
        with tempfile.TemporaryDirectory() as folder:
            return status_lights.problems_of(Path(folder), {"manifest": manifest, "items": [item]})

    def test_white_is_a_light_the_names_know(self):
        self.assertEqual(status_lights.NAMES["white"], status_lights.WHITE)

    def test_a_software_tests_or_docs_row_is_never_white(self):
        for kind in ("software", "tests", "docs"):
            self.assertTrue(any("always applies" in found for found in self.problems(kind, status_lights.WHITE)), kind)

    def test_a_hardware_row_is_white_only_when_the_manifest_says_hardware_bound_false(self):
        for kind in ("hardware", "integration"):
            self.assertTrue(any("hardware_bound false" in found for found in self.problems(kind, status_lights.WHITE)), kind)
            self.assertEqual(self.problems(kind, status_lights.WHITE, {"hardware_bound": False}), [])

    def test_a_green_hardware_row_of_a_repository_with_no_hardware_is_refused(self):
        found = self.problems("hardware", status_lights.GREEN, {"hardware_bound": False})
        self.assertTrue(any("not applicable is white" in line for line in found))
        self.assertEqual(self.problems("hardware", status_lights.GREEN, {"hardware_bound": True}), [])
