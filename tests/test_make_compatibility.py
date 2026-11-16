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

    def test_the_train_is_named_eco_and_a_number_with_no_date(self):
        self.assertEqual(make_compatibility.train_name(1), "eco-1")
        self.assertEqual(make_compatibility.train_name(12), "eco-12")
        with tempfile.TemporaryDirectory() as holder:
            data = make_compatibility.collect(self.fake_root(holder), 3)
        self.assertEqual(data["train"], "eco-3")
        self.assertIn("Release train: **eco-3**", make_compatibility.markdown(data))

    def test_a_new_train_goes_up_by_one_and_a_missing_file_means_the_first(self):
        with tempfile.TemporaryDirectory() as holder:
            file = Path(holder) / "release_train.json"
            self.assertEqual(make_compatibility.current_train(file), 1)
            self.assertEqual(make_compatibility.next_train(file), 2)
            self.assertEqual(make_compatibility.next_train(file), 3)
            self.assertEqual(make_compatibility.current_train(file), 3)
            self.assertEqual(json.loads(file.read_text(encoding="utf-8")), {"schema_version": "1.0", "current": 3})

    def test_the_train_file_of_the_repository_holds_a_positive_whole_number(self):
        number = make_compatibility.current_train()
        self.assertIsInstance(number, int)
        self.assertGreaterEqual(number, 1)

    def test_what_moved_on_since_the_train_is_listed(self):
        written = {"contracts_version": "1", "repositories": {"A": {"version": "1"}, "B": {"version": "2"}, "C": {"version": "3"}}}
        now = {"contracts_version": "2", "repositories": {"A": {"version": "1"}, "B": {"version": "3"}, "D": {"version": "1"}}}
        self.assertEqual(
            make_compatibility.moved_on(written, now),
            ["contracts: 1 in the lock, 2 now", "B: 2 in the lock, 3 now", "D: not in the lock", "C: in the lock but not in the family"],
        )
        self.assertEqual(make_compatibility.moved_on(written, written), [])

    def test_the_page_says_it_is_a_photograph_of_the_train(self):
        text = make_compatibility.markdown({"train": "eco-1", "contracts_version": "9", "repositories": {}})
        self.assertIn("when the train was prepared: **9**", text)
        self.assertNotIn("Current version", text)

    def test_the_page_of_the_repository_is_what_the_tool_writes_for_its_own_lock(self):
        docs = Path(make_compatibility.DOCS)
        data = json.loads((docs / "ecosystem.lock.json").read_text(encoding="utf-8"))
        self.assertEqual((docs / "COMPATIBILITY.md").read_text(encoding="utf-8").replace("\r\n", "\n"), make_compatibility.markdown(data))

    def test_the_lock_is_stable_json(self):
        data = {"schema_version": "1.0", "contracts_version": "1", "repositories": {}}
        self.assertEqual(json.loads(make_compatibility.lock_text(data)), data)


if __name__ == "__main__":
    unittest.main()
