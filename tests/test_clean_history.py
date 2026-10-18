import contextlib
import io
import unittest
from unittest import mock

import _support  # noqa: F401  (puts tools/ on the path)
from _support import TempRepo

import clean_history
import publication_check as check


def run(function, *args):
    out = io.StringIO()
    with contextlib.redirect_stdout(out):
        result = function(*args)
    return result, out.getvalue()


def committed_repo(name="ARMOR-CLEAN"):
    repo = TempRepo(name)
    repo.write("README.md", "# Title\n")
    repo.write("src/main.py", "print('hello')\n")
    repo.commit("First")
    repo.write("src/main.py", "print('hello world')\n")
    repo.commit("Second")
    return repo


class PrepareTests(unittest.TestCase):
    def test_dry_run_reports_and_changes_nothing(self):
        with committed_repo() as repo:
            ok, out = run(clean_history.prepare, repo.path, False)
            self.assertTrue(ok)
            self.assertIn("READY", out)
            self.assertIn("2 files", out)
            self.assertNotIn(clean_history.BRANCH, repo.git("branch", "--list"))

    def test_apply_makes_one_root_commit_with_the_same_tree(self):
        with committed_repo() as repo:
            ok, out = run(clean_history.prepare, repo.path, True)
            self.assertTrue(ok, out)
            self.assertIn("DONE", out)
            branch = clean_history.BRANCH
            self.assertEqual(repo.git("rev-list", "--count", branch), "1")
            self.assertEqual(repo.git("rev-parse", f"{branch}^{{tree}}"), repo.git("rev-parse", "HEAD^{tree}"))
            self.assertEqual(repo.git("log", "-1", "--format=%an <%ae>|%cn <%ce>|%s", branch),
                             f"{_support_author()}|{_support_author()}|Initial commit")
            # the working branch keeps its history
            self.assertEqual(repo.git("rev-list", "--count", "main"), "2")

    def test_the_new_commit_has_no_trailer_and_passes_the_publication_check(self):
        with committed_repo() as repo:
            run(clean_history.prepare, repo.path, True)
            self.assertEqual(repo.git("log", "-1", "--format=%B", clean_history.BRANCH).strip(), "Initial commit")
            self.assertEqual([f for f in check.check_repo(repo.path, history=True, ref=clean_history.BRANCH) if f[0] == "BLOCK"], [])

    def test_the_author_does_not_depend_on_the_one_configured_on_the_machine(self):
        with committed_repo() as repo:
            with mock.patch.dict("os.environ", {"GIT_AUTHOR_NAME": "Someone Else", "GIT_AUTHOR_EMAIL": "else@example.org"}):
                ok, _out = run(clean_history.prepare, repo.path, True)
            self.assertTrue(ok)
            self.assertEqual(repo.git("log", "-1", "--format=%an", clean_history.BRANCH), "JuanenRac (Electro Hobby 3D)")

    def test_uncommitted_changes_are_refused(self):
        with committed_repo() as repo:
            repo.write("new.txt", "pending\n")
            ok, out = run(clean_history.prepare, repo.path, True)
            self.assertFalse(ok)
            self.assertIn("REFUSED", out)
            self.assertIn("uncommitted", out)
            self.assertNotIn(clean_history.BRANCH, repo.git("branch", "--list"))

    def test_block_findings_in_the_files_are_refused(self):
        with committed_repo() as repo:
            repo.write("deploy/server.key", "data\n")
            repo.commit("Add a key")
            ok, out = run(clean_history.prepare, repo.path, True)
            self.assertFalse(ok)
            self.assertIn("BLOCK finding", out)
            self.assertNotIn(clean_history.BRANCH, repo.git("branch", "--list"))

    def test_a_bad_commit_in_the_old_history_does_not_stop_a_clean_copy(self):
        # the point of the tool: the files are clean, the history is not, and the copy has none of that history
        with TempRepo("ARMOR-OLD") as repo:
            repo.write("a.txt", "x\n")
            repo.commit("Add", name="Somebody Else", email="else@example.org")
            ok, out = run(clean_history.prepare, repo.path, True)
            self.assertTrue(ok, out)
            self.assertEqual(repo.git("rev-list", "--count", clean_history.BRANCH), "1")

    def test_a_second_run_replaces_the_branch(self):
        with committed_repo() as repo:
            run(clean_history.prepare, repo.path, True)
            repo.write("c.txt", "more\n")
            repo.commit("Third")
            ok, _out = run(clean_history.prepare, repo.path, True)
            self.assertTrue(ok)
            self.assertEqual(repo.git("rev-list", "--count", clean_history.BRANCH), "1")
            self.assertEqual(repo.git("rev-parse", f"{clean_history.BRANCH}^{{tree}}"), repo.git("rev-parse", "HEAD^{tree}"))


def _support_author():
    return "JuanenRac (Electro Hobby 3D) <electrohobby3d@gmail.com>"


class MainTests(unittest.TestCase):
    def test_without_arguments_it_prints_the_help_and_fails(self):
        code, out = run(clean_history.main, [])
        self.assertEqual(code, 2)
        self.assertIn("publishable copy", out)

    def test_a_dry_run_exits_zero_and_a_refusal_exits_one(self):
        with committed_repo("ARMOR-MAIN") as repo:
            with mock.patch.object(check, "ROOT", repo.path.parent):
                code, out = run(clean_history.main, ["ARMOR-MAIN"])
                self.assertEqual(code, 0)
                self.assertIn("READY", out)
                repo.write("pending.txt", "x\n")
                code, out = run(clean_history.main, ["ARMOR-MAIN", "--apply"])
                self.assertEqual(code, 1)
                self.assertIn("REFUSED", out)

    def test_all_covers_every_git_repository_and_one_refusal_fails_the_run(self):
        with committed_repo("ARMOR-ALL") as repo:
            (repo.path.parent / "ARMOR-NOGIT").mkdir()
            with mock.patch.object(check, "ROOT", repo.path.parent):
                code, out = run(clean_history.main, ["--all"])
                self.assertEqual(code, 0)
                self.assertIn("ARMOR-ALL", out)
                self.assertNotIn("ARMOR-NOGIT", out)
                repo.write("pending.txt", "x\n")
                code, out = run(clean_history.main, ["--all"])
                self.assertEqual(code, 1)


if __name__ == "__main__":
    unittest.main()
