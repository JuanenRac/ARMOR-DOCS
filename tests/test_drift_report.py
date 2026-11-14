"""The drift report: the result of each nightly check and the counts, with no output of the checks in it."""
import json
import tempfile
import unittest
from pathlib import Path

import _support  # noqa: F401  (puts tools/ on the path)

import drift_report


class DriftReportTests(unittest.TestCase):
    def root(self, holder: str) -> Path:
        root = Path(holder) / "ARMOR-DOCS"
        for _name, script, _ in drift_report.CHECKS:
            path = (root / script).resolve()
            if "ARMOR-COMMON" not in script:
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text("", encoding="utf-8")
        return root

    def test_a_failing_check_is_counted_and_a_missing_script_is_skipped_never_passed(self):
        with tempfile.TemporaryDirectory() as holder:
            root = self.root(holder)
            report = drift_report.run_checks(root, lambda command, cwd: 1 if command[1].endswith("make_brand.py") else 0)
        by_name = {item["name"]: item["result"] for item in report["checks"]}
        self.assertEqual(by_name["banners"], "fail")
        self.assertEqual(by_name["readmes"], "pass")
        self.assertEqual(by_name["firmware base"], "skip")
        self.assertEqual(report["failed"], 1)
        self.assertEqual(report["skipped"], 3)
        self.assertEqual(report["total"], len(drift_report.CHECKS))

    def test_the_report_holds_only_names_results_and_counts(self):
        with tempfile.TemporaryDirectory() as holder:
            report = drift_report.run_checks(self.root(holder), lambda command, cwd: 0)
        self.assertEqual(set(report), {"schema_version", "total", "failed", "skipped", "checks"})
        for item in report["checks"]:
            self.assertEqual(set(item), {"name", "result"})
        json.dumps(report)

    def test_the_markdown_table_has_a_row_per_check_and_the_counts(self):
        text = drift_report.render_markdown({"schema_version": 1, "total": 2, "failed": 1, "skipped": 0, "checks": [{"name": "a", "result": "pass"}, {"name": "b", "result": "fail"}]})
        self.assertIn("| b | fail |", text)
        self.assertIn("1 of 2 checks failed", text)

    def test_the_names_of_the_checks_are_unique(self):
        names = [name for name, _, _ in drift_report.CHECKS]
        self.assertEqual(len(names), len(set(names)))


if __name__ == "__main__":
    unittest.main()
