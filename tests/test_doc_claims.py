import json
import tempfile
import unittest
from pathlib import Path

import _support  # noqa: F401  (puts tools/ on the path)

import doc_claims


class CommentTests(unittest.TestCase):
    def test_comments_are_taken_out_and_strings_are_kept(self):
        code = 'const a = "http://x"; // scrypt(here)\n/* scrypt( */ const b = 1;\nconst c = `a//b`;\n'
        text = doc_claims.strip_comments(code, ".ts")
        self.assertNotIn("scrypt", text)
        self.assertIn("http://x", text)
        self.assertIn("a//b", text)
        self.assertIn("const b = 1;", text)

    def test_hash_comments_of_a_script_and_an_unknown_suffix(self):
        self.assertEqual(doc_claims.strip_comments("x = 'a#b'  # note\ny = 1\n", ".py"), "x = 'a#b'  \ny = 1\n")
        self.assertEqual(doc_claims.strip_comments("// keep", ".md"), "// keep")

    def test_the_bullets_without_a_marker_are_counted(self):
        text = "# Baseline\n## What the software already enforces\n- one <!-- claim: a -->\n- two\n## Other\n- three\n"
        total, bare = doc_claims.unmarked_bullets(text)
        self.assertEqual((total, bare), (2, ["- two"]))


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

    def test_a_pattern_that_only_a_comment_holds_fails_unless_code_only_is_off(self):
        (self.family / "ARMOR-X" / "src" / "b.ts").write_text("// scrypt( is what we use\nexport const h = 1;\n", encoding="utf-8")
        claim = {"repo": "ARMOR-X", "file": "src/b.ts", "pattern": "scrypt\\(", "says": "x"}
        problems, _ = doc_claims.check({"a": claim}, {"a": ["T.md"]}, self.family)
        self.assertEqual(len(problems), 1)
        problems, _ = doc_claims.check({"a": dict(claim, code_only=False)}, {"a": ["T.md"]}, self.family)
        self.assertEqual(problems, [])

    def test_min_matches_asks_for_more_than_one(self):
        (self.family / "ARMOR-X" / "src" / "c.ts").write_text("a(); a();\n", encoding="utf-8")
        claim = {"repo": "ARMOR-X", "file": "src/c.ts", "pattern": "a\\(\\)", "says": "x"}
        self.assertEqual(doc_claims.check({"a": dict(claim, min_matches=2)}, {"a": ["T.md"]}, self.family)[0], [])
        self.assertEqual(len(doc_claims.check({"a": dict(claim, min_matches=3)}, {"a": ["T.md"]}, self.family)[0]), 1)

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
