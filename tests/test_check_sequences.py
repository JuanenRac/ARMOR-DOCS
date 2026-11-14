"""The sequence page names only routes and topics that the contracts have, and the check fails on a name that is gone."""
import json
import tempfile
import unittest
from pathlib import Path

import _support  # noqa: F401  (puts tools/ on the path)

import check_sequences


class CheckSequencesTests(unittest.TestCase):
    def common(self, holder: str) -> Path:
        root = Path(holder) / "ARMOR-COMMON"
        (root / "openapi").mkdir(parents=True)
        (root / "asyncapi").mkdir()
        (root / "openapi" / "api.yaml").write_text("paths:\n  /api/v1/alarm/command:\n    post: {}\n  /api/v1/admin/firmware/jobs/{id}:\n    get: {}\n", encoding="utf-8")
        (root / "asyncapi" / "mqtt.json").write_text(json.dumps({"channels": {"c": {"address": "armor/alarm/{node_id}/command"}, "d": {"address": "armor/device/{node_id}/#"}}}), encoding="utf-8")
        return root

    def page(self, holder: str, text: str) -> Path:
        path = Path(holder) / "page.md"
        path.write_text(text, encoding="utf-8")
        return path

    def test_names_that_exist_pass_whatever_the_placeholder_is_called(self):
        with tempfile.TemporaryDirectory() as holder:
            page = self.page(holder, "POST /api/v1/alarm/command then armor/alarm/{node}/command and GET /api/v1/admin/firmware/jobs/{job}\n")
            self.assertEqual(check_sequences.problems(page, self.common(holder)), [])

    def test_a_route_or_topic_the_contracts_do_not_have_is_reported(self):
        with tempfile.TemporaryDirectory() as holder:
            page = self.page(holder, "POST /api/v1/alarm/gone then armor/alarm/{node_id}/missing\n")
            found = check_sequences.problems(page, self.common(holder))
        self.assertTrue(any("/api/v1/alarm/gone" in line for line in found))
        self.assertTrue(any("armor/alarm/{}/missing" in line for line in found))

    def test_a_wildcard_address_covers_the_topics_below_it(self):
        with tempfile.TemporaryDirectory() as holder:
            page = self.page(holder, "POST /api/v1/alarm/command and armor/device/{node_id}/lights/state\n")
            self.assertEqual(check_sequences.problems(page, self.common(holder)), [])

    def test_a_page_that_names_nothing_does_not_pass_on_nothing(self):
        with tempfile.TemporaryDirectory() as holder:
            found = check_sequences.problems(self.page(holder, "No names here.\n"), self.common(holder))
        self.assertTrue(any("passes on nothing" in line or "would pass on nothing" in line for line in found))

    def test_the_real_page_agrees_with_the_contracts_next_to_it(self):
        common = check_sequences.DOCS_ROOT.parent / "ARMOR-COMMON"
        if not (common / "openapi").is_dir():
            self.skipTest("ARMOR-COMMON is not next to this repository")
        self.assertEqual(check_sequences.problems(check_sequences.PAGE, common), [])

    def test_without_the_contracts_checkout_the_check_says_skip(self):
        with tempfile.TemporaryDirectory() as holder:
            self.assertEqual(check_sequences.main(["--common", str(Path(holder) / "none")]), 0)


if __name__ == "__main__":
    unittest.main()
