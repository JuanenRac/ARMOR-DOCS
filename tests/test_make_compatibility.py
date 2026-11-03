import json
import tempfile
import unittest
from pathlib import Path

import _support  # noqa: F401  (puts tools/ on the path)

import make_compatibility
from make_readmes import ORDER


class CompatibilityTests(unittest.TestCase):
    def fake_root(self, holder):
        root = Path(holder)
        for index, name in enumerate(ORDER):
            (root / name).mkdir()
            (root / name / "armor.project.json").write_text(json.dumps({"version": f"0.{index}.1"}), encoding="utf-8")
        (root / "ARMOR-COMMON" / "registry").mkdir()
        (root / "ARMOR-COMMON" / "registry" / "contract_pins.json").write_text(json.dumps({"consumers": {"ARMOR-SERVER": "0.0.1"}}), encoding="utf-8")
        return root

    def test_it_lists_every_repository_with_its_version_and_pin(self):
        with tempfile.TemporaryDirectory() as holder:
            data = make_compatibility.collect(self.fake_root(holder))
        self.assertEqual(list(data["repositories"]), ORDER)
        self.assertEqual(data["contracts_version"], "0.0.1")
        self.assertEqual(data["repositories"]["ARMOR-SERVER"]["contracts"], "0.0.1")
        self.assertIsNone(data["repositories"]["ARMOR-STUDIO"]["contracts"])

    def test_a_pin_below_the_contracts_is_marked_behind(self):
        data = {"contracts_version": "0.8.0.6", "repositories": {"A": {"version": "1", "contracts": "0.8.0.5"}, "B": {"version": "1", "contracts": "0.8.0.6"}}}
        text = make_compatibility.markdown(data)
        self.assertIn("| A | 1 | 0.8.0.5 (behind) |", text)
        self.assertIn("| B | 1 | 0.8.0.6 |", text)

    def test_the_lock_is_stable_json(self):
        data = {"schema_version": "1.0", "contracts_version": "1", "repositories": {}}
        self.assertEqual(json.loads(make_compatibility.lock_text(data)), data)


if __name__ == "__main__":
    unittest.main()
