"""The update profiles of the machine roles (data/update-profiles.json): the schema, the eight languages and that the composition is marked as a proposal."""
import json
import unittest
from pathlib import Path

import _support  # noqa: F401  (puts tools/ on the path)

import registry

FILE = Path(__file__).resolve().parents[1] / "data" / "update-profiles.json"
LANGUAGES = {"en", "es", "de", "fr", "it", "ja", "zh", "pt"}


class UpdateProfilesTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads(FILE.read_text(encoding="utf-8"))

    def test_the_file_has_the_schema_and_says_it_is_a_proposal(self):
        self.assertEqual(self.data["schema_version"], "1.0")
        self.assertIs(self.data["proposal"], True)
        self.assertEqual(set(self.data["proposal_note"]), LANGUAGES)

    def test_every_profile_has_its_texts_in_eight_languages_and_components_of_the_registry(self):
        ids = [item["id"] for item in self.data["profiles"]]
        self.assertEqual(ids, ["cm5", "cm5-minimal", "cm5-standard", "cm5-complete", "operator-pc", "development-pc"])
        for item in self.data["profiles"]:
            self.assertEqual(set(item["title"]), LANGUAGES, item["id"])
            self.assertEqual(set(item["description"]), LANGUAGES, item["id"])
            for name in item["components"]:
                self.assertIn(name, registry.NAMES, f"{name} in {item['id']} is not a repository of the family")

    def test_the_roles_have_the_proposed_composition(self):
        by_id = {item["id"]: item for item in self.data["profiles"]}
        self.assertEqual(by_id["cm5"]["components"], ["ARMOR-SERVER", "ARMOR-STUDIO", "ARMOR-NETWORK", "ARMOR-SERVER-AI", "ARMOR-VOICE-AI", "ARMOR-VISION", "ARMOR-DEVOPS"])
        self.assertEqual(by_id["cm5-minimal"]["components"], ["ARMOR-SERVER", "ARMOR-STUDIO", "ARMOR-COMMON"])
        self.assertEqual(by_id["cm5-standard"]["components"], ["ARMOR-SERVER", "ARMOR-STUDIO", "ARMOR-COMMON", "ARMOR-UPDATER", "ARMOR-DEVOPS", "ARMOR-VISION", "ARMOR-NETWORK"])
        self.assertTrue(set(by_id["cm5-complete"]["components"]) >= set(by_id["cm5-standard"]["components"]) | set(by_id["cm5"]["components"]))
        self.assertEqual(by_id["operator-pc"]["components"], ["ARMOR-STUDIO", "ARMOR-UPDATER"])
        self.assertTrue(by_id["development-pc"]["all_installable"])
        self.assertIn("ARMOR-SIMULATOR", by_id["development-pc"]["components"])


if __name__ == "__main__":
    unittest.main()
