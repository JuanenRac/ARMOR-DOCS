"""The command lines of the two checkers of the sentences that depend on the code (doc_claims.py and doc_facts.py): what each prints and which code it returns, over a folder of documents
made for the test, so nothing reads the real family."""
import contextlib
import io
import json
import tempfile
import unittest
from pathlib import Path
from unittest import mock

import _support  # noqa: F401  (puts tools/ on the path)

import doc_claims
import doc_facts


def run(module, *arguments):
    out = io.StringIO()
    with contextlib.redirect_stdout(out):
        code = module.main(list(arguments))
    return code, out.getvalue()


class Folder(unittest.TestCase):
    def setUp(self):
        holder = tempfile.TemporaryDirectory()
        self.addCleanup(holder.cleanup)
        self.docs = Path(holder.name) / "docs"
        self.docs.mkdir()
        self.claims = Path(holder.name) / "claims.json"

    def write(self, name, text):
        (self.docs / name).write_text(text, encoding="utf-8", newline="")


class ClaimsCommandTests(Folder):
    def patched(self, claims):
        self.claims.write_text(json.dumps(claims), encoding="utf-8")
        return mock.patch.multiple(doc_claims, DOCS=self.docs, CLAIMS_FILE=self.claims)

    def test_without_claims_and_markers_it_passes(self):
        self.write("A.md", "Nothing here depends on the code.\n")
        with self.patched({}):
            code, out = run(doc_claims)
        self.assertEqual(code, 0)
        self.assertIn("DOC_CLAIMS=PASS (0 checked, 0 skipped)", out)

    def test_a_marker_without_an_entry_and_an_entry_without_a_marker_both_fail(self):
        self.write("A.md", "It holds 256 nodes. <!-- claim: server.max_nodes -->\n")
        with self.patched({"other.claim": {"repo": "ARMOR-NOPE", "file": "x", "pattern": "x"}}):
            code, out = run(doc_claims)
        self.assertEqual(code, 1)
        self.assertIn("FAIL server.max_nodes: written in A.md but missing from docs/claims.json", out)
        self.assertIn("FAIL other.claim: in docs/claims.json but no document carries its marker", out)
        self.assertIn("DOC_CLAIMS=FAIL", out)

    def test_a_repository_that_is_not_there_is_skipped_and_said(self):
        self.write("A.md", "It holds 256 nodes. <!-- claim: server.max_nodes -->\n")
        with self.patched({"server.max_nodes": {"repo": "ARMOR-NOT-A-REPOSITORY", "file": "src/a.ts", "pattern": "x"}}):
            code, out = run(doc_claims)
        self.assertEqual(code, 0)
        self.assertIn("SKIP server.max_nodes: ARMOR-NOT-A-REPOSITORY is not next to ARMOR-DOCS", out)
        self.assertIn("(0 checked, 1 skipped)", out)

    def test_the_list_shows_every_claim_and_where_it_is_written(self):
        self.write("A.md", "One. <!-- claim: a.one -->\n")
        self.write("B.md", "Two. <!-- claim:a.one -->\n")
        with self.patched({"a.one": {"repo": "ARMOR-X", "file": "f.ts", "pattern": "x"}, "a.lost": {"repo": "ARMOR-Y", "file": "g.ts", "pattern": "y"}}):
            code, out = run(doc_claims, "--list")
        self.assertEqual(code, 0)
        self.assertIn("a.one", out)
        self.assertIn("A.md, B.md", out)
        self.assertIn("(no marker)", out)

    def test_an_entry_without_one_of_its_keys_is_a_problem_named_for_the_key(self):
        problems, skipped = doc_claims.check({"a": {"repo": "ARMOR-X", "file": "f"}, "b": {"file": "f", "pattern": "x"}, "c": {"repo": "ARMOR-X", "pattern": "x"}}, {"a": ["T.md"], "b": ["T.md"], "c": ["T.md"]}, self.docs)
        self.assertEqual(skipped, [])
        self.assertEqual([item.split(":")[1].strip() for item in problems], ["the entry has no 'pattern'", "the entry has no 'repo'", "the entry has no 'file'"])

    def test_a_file_that_is_gone_is_a_problem(self):
        (self.docs / "ARMOR-X").mkdir()
        problems, _ = doc_claims.check({"a": {"repo": "ARMOR-X", "file": "gone.ts", "pattern": "x"}}, {"a": ["T.md"]}, self.docs)
        self.assertEqual(problems, ["a: ARMOR-X/gone.ts does not exist"])

    def test_the_markers_are_found_with_any_spacing_and_only_in_markdown(self):
        self.write("A.md", "<!--claim:a.b-->, <!--   claim:   c-d   -->, <!-- claim: bad name -->\n")
        self.write("B.txt", "<!-- claim: not.markdown -->\n")
        with mock.patch.object(doc_claims, "DOCS", self.docs):
            self.assertEqual(sorted(doc_claims.written()), ["a.b", "c-d"])


class FactsCommandTests(Folder):
    def patched(self):
        return mock.patch.object(doc_facts, "DOCS", self.docs)

    def test_documents_without_figures_are_current(self):
        self.write("A.md", "Plain text.\n")
        with self.patched():
            self.assertEqual(run(doc_facts, "--check"), (0, "DOC_FACTS=CURRENT\n"))
            self.assertEqual(run(doc_facts), (0, ""))

    def test_a_figure_that_means_nothing_fails_with_its_name(self):
        self.write("A.md", "There are <!--fact:no_such_fact-->9<!--/fact--> of them.\n")
        with self.patched():
            code, out = run(doc_facts, "--check")
        self.assertEqual(code, 1)
        self.assertIn("FAIL A.md: the figure 'no_such_fact' means nothing", out)
        self.assertIn("DOC_FACTS=FAIL", out)

    def test_a_verified_version_newer_than_the_repository_fails(self):
        self.write("A.md", "Checked against <!--verified:ARMOR-X 9.9.9-->.\n")
        with self.patched(), mock.patch.object(doc_facts, "version", return_value="1.2.3"):
            code, out = run(doc_facts, "--check")
        self.assertEqual(code, 1)
        self.assertIn("FAIL A.md: ARMOR-X 9.9.9 is newer than the version of the repository (1.2.3)", out)

    def test_the_stale_list_names_a_verification_the_repository_has_outgrown(self):
        self.write("A.md", "Checked against <!--verified:ARMOR-X 1.0.0-->, <!--verified:ARMOR-Y 3.0.0-->, <!--verified:ARMOR-Z 1.0-->.\n")
        versions = {"ARMOR-X": "1.2.0", "ARMOR-Y": "3.0.0"}

        def version(repo):
            if repo not in versions:
                raise doc_facts.Unavailable(repo)
            return versions[repo]

        with self.patched(), mock.patch.object(doc_facts, "version", side_effect=version):
            code, out = run(doc_facts, "--stale")
        self.assertEqual(code, 0)
        self.assertEqual(out.strip().splitlines(), ["A.md: verified in ARMOR-X 1.0.0, now 1.2.0"])

    def test_the_list_tells_what_is_unavailable_instead_of_failing(self):
        self.write("A.md", "Two <!--fact:tests:ARMOR-NOT-HERE-->1<!--/fact--> and <!--fact:tests:ARMOR-NOT-HERE-->2<!--/fact-->.\n")
        with self.patched(), mock.patch.object(doc_facts, "value", side_effect=doc_facts.Unavailable("not next to this repository")):
            code, out = run(doc_facts, "--list")
        self.assertEqual(code, 0)
        self.assertEqual(out.count("unavailable (not next to this repository)"), 1, "a figure is listed once")

    def test_a_figure_that_is_out_of_date_is_fixed_without_check_and_reported_with_it(self):
        self.write("A.md", "It has <!--fact:answer-->1<!--/fact--> tests.\r\n")
        with self.patched(), mock.patch.object(doc_facts, "value", return_value="42"):
            code, out = run(doc_facts, "--check")
            self.assertEqual(code, 1)
            self.assertIn("FAIL A.md", out)
            self.assertEqual((self.docs / "A.md").read_bytes(), b"It has <!--fact:answer-->1<!--/fact--> tests.\r\n")
            code, out = run(doc_facts)
            self.assertEqual(code, 0)
            self.assertIn("FIX  A.md", out)
            self.assertEqual((self.docs / "A.md").read_bytes(), b"It has <!--fact:answer-->42<!--/fact--> tests.\r\n", "the line ends are kept")
            self.assertEqual(run(doc_facts, "--check"), (0, "DOC_FACTS=CURRENT\n"))

    def test_a_figure_that_cannot_be_read_is_skipped_and_said(self):
        self.write("A.md", "It has <!--fact:answer-->1<!--/fact--> tests.\n")
        with self.patched(), mock.patch.object(doc_facts, "value", side_effect=doc_facts.Unavailable("not next to this repository")):
            code, out = run(doc_facts, "--check")
        self.assertEqual(code, 0)
        self.assertIn("SKIP A.md", out)


if __name__ == "__main__":
    unittest.main()
