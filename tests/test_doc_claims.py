import json
import tempfile
import unittest
from pathlib import Path

import _support  # noqa: F401  (puts tools/ on the path)

import doc_claims


class CheckTests(unittest.TestCase):
    def setUp(self):
        self.holder = tempfile.TemporaryDirectory()
        self.addCleanup(self.holder.cleanup)
        self.family = Path(self.holder.name)
        (self.family / "ARMOR-X" / "src").mkdir(parents=True)
        (self.family / "ARMOR-X" / "src" / "a.ts").write_text("export const MAX_NODES = 256;\n", encoding="utf-8")

    def claim(self, pattern="MAX_NODES\\s*=\\s*256"):
        return {"repo": "ARMOR-X", "file": "src/a.ts", "pattern": pattern, "says": "x"}

    def test_a_claim_that_matches_passes(self):
        problems, skipped = doc_claims.check({"a": self.claim()}, {"a": ["T.md"]}, self.family)
        self.assertEqual((problems, skipped), ([], []))

    def test_the_code_that_changed_fails_the_claim(self):
        problems, _ = doc_claims.check({"a": self.claim("MAX_NODES\\s*=\\s*128")}, {"a": ["T.md"]}, self.family)
        self.assertEqual(len(problems), 1)
        self.assertIn("no longer matches", problems[0])

    def test_a_marker_without_an_entry_and_an_entry_without_a_marker_fail(self):
        problems, _ = doc_claims.check({"b": self.claim()}, {"a": ["T.md"]}, self.family)
        self.assertEqual(sorted(p.split(":")[0] for p in problems), ["a", "b"])

    def test_a_missing_file_fails_and_a_missing_repository_is_skipped(self):
        broken = {"repo": "ARMOR-X", "file": "src/none.ts", "pattern": "x"}
        far = {"repo": "ARMOR-Y", "file": "a", "pattern": "x"}
        problems, skipped = doc_claims.check({"a": broken, "b": far}, {"a": ["T.md"], "b": ["T.md"]}, self.family)
        self.assertEqual(len(problems), 1)
        self.assertEqual(len(skipped), 1)

    def test_an_entry_missing_a_field_fails(self):
        problems, _ = doc_claims.check({"a": {"repo": "ARMOR-X"}}, {"a": ["T.md"]}, self.family)
        self.assertIn("no 'file'", problems[0])


class RepositoryTests(unittest.TestCase):
    def test_every_marker_of_the_documents_has_its_entry_and_the_entry_still_matches(self):
        claims = json.loads(doc_claims.CLAIMS_FILE.read_text(encoding="utf-8"))
        marked = doc_claims.written()
        self.assertTrue(marked, "the documents carry no claim marker")
        problems, _skipped = doc_claims.check(claims, marked)
        self.assertEqual(problems, [])
