import contextlib
import io
import unittest
from unittest import mock

import _support  # noqa: F401  (puts tools/ on the path)
from _support import TempRepo

import publication_check as check


def scan(text, where="file.txt"):
    findings = []
    check.scan_text("REPO", where, text, findings)
    return findings


class ScanTextTests(unittest.TestCase):
    def test_private_key_header_blocks(self):
        findings = scan("-----BEGIN OPENSSH PRIVATE KEY-----")
        self.assertEqual([f[0] for f in findings], ["BLOCK"])
        self.assertIn("private key", findings[0][3])
        self.assertEqual(findings[0][2], "file.txt:1")

    def test_public_certificate_header_is_not_a_private_key(self):
        self.assertEqual(scan("-----BEGIN CERTIFICATE-----"), [])

    def test_personal_email_blocks_but_the_projects_own_does_not(self):
        findings = scan("write to somebody.private@gmail.com")
        self.assertEqual(len(findings), 1)
        self.assertEqual(findings[0][0], "BLOCK")
        self.assertNotIn("somebody.private", findings[0][3])   # the address itself is never printed in full
        self.assertEqual(scan("contact electrohobby3d@gmail.com"), [])
        self.assertEqual(scan("contact ELECTROHOBBY3D@GMAIL.COM"), [])

    def test_other_domains_are_not_personal_email(self):
        self.assertEqual(scan("mail user@example.org"), [])

    def test_public_ip_blocks_and_never_prints_the_whole_address(self):
        findings = scan("server at 93.184.216.34")
        self.assertEqual(len(findings), 1)
        self.assertEqual(findings[0][0], "BLOCK")
        self.assertIn("93.x.x.x", findings[0][3])
        self.assertNotIn("184", findings[0][3])

    def test_private_loopback_and_benign_addresses_pass(self):
        for text in ("192.168.0.180", "10.0.0.1", "127.0.0.1", "172.16.5.5", "169.254.1.1", "224.0.0.1", "8.8.8.8", "1.1.1.1"):
            self.assertEqual(scan(f"host {text}"), [], text)

    def test_version_numbers_that_look_like_addresses_pass(self):
        self.assertEqual(scan("firmware version 93.184.216.34"), [])
        self.assertEqual(scan("tag v93.184.216.34"), [])
        self.assertEqual(scan("build 93.184.216.34-rc1"), [])

    def test_out_of_range_octets_are_not_addresses(self):
        self.assertEqual(scan("value 999.184.216.34"), [])

    def test_public_ip_helper(self):
        self.assertTrue(check.public_ip("93.184.216.34"))
        self.assertFalse(check.public_ip("192.168.1.1"))
        self.assertFalse(check.public_ip("not an address"))
        self.assertFalse(check.public_ip("0.1.2.3"))
        self.assertFalse(check.public_ip("255.255.255.255"))

    def test_literal_password_goes_to_review(self):
        findings = scan('password = "Zx9qLmN42pT"')
        self.assertEqual([f[0] for f in findings], ["REVIEW"])
        self.assertIn("zx9", findings[0][3].lower())
        self.assertNotIn("Zx9qLmN42pT", findings[0][3])   # cut to the first characters

    def test_literal_variants(self):
        self.assertEqual(len(scan('"api_key": "Qw8rTy2uIo5p"')), 1)
        self.assertEqual(len(scan("token: 'Abcd1234Efgh'")), 1)
        self.assertEqual(len(scan('PSK="Mn73kLq92Ws"')), 1)

    def test_harmless_literals_are_ignored(self):
        for text in ('password = "changeme-please"', 'secret = "example-secret-value"', 'token = "fake-token-value"',
                     'password = "$ENV_PASSWORD_VALUE"', 'password = "short"', 'password = "aaaaaaaaaaaa"', 'password = "abababababab"'):
            self.assertEqual(scan(text), [], text)

    def test_harmless_word_on_the_line_clears_a_literal(self):
        self.assertEqual(scan('# test fixture: password = "Zx9qLmN42pT"'), [])

    def test_very_long_lines_are_skipped(self):
        self.assertEqual(scan("-----BEGIN PRIVATE KEY-----" + "x" * 2100), [])

    def test_line_numbers_are_reported(self):
        findings = scan("ok\nok\n-----BEGIN RSA PRIVATE KEY-----\n", where="a/b.pem")
        self.assertEqual(findings[0][2], "a/b.pem:3")

    def test_bad_path_patterns(self):
        for path in ("secrets/mqtt.txt", "a/b/secrets/token", ".env", "deploy/prod.env", "certs/server.pem", "certs/server.key", "id_ed25519", "x/id_rsa"):
            self.assertTrue(check.BAD_PATH.search(path), path)
        for path in ("secrets/example.txt", "docs/environment.md", "src/key_value.py", "README.md", "id_.txt"):
            self.assertFalse(check.BAD_PATH.search(path), path)

    def test_fixture_path_pattern(self):
        for path in ("tests/test_a.py", "src/tests/x.py", "conformance/a.json", "test_thing.py", "tools/test_thing.py"):
            self.assertTrue(check.FIXTURE_PATH.search(path), path)
        self.assertFalse(check.FIXTURE_PATH.search("src/contest/a.py"))


class CheckRepoTests(unittest.TestCase):
    def test_clean_repository_has_no_findings(self):
        with TempRepo() as repo:
            repo.write("README.md", "# Hello\nNothing to see.\n")
            repo.commit("Add readme")
            self.assertEqual(check.check_repo(repo.path, history=True), [])

    def test_tracked_env_and_key_files_block(self):
        with TempRepo() as repo:
            repo.write(".env", "A=1\n")
            repo.write("certs/server.key", "data\n")
            repo.write("secrets/example.txt", "ok\n")
            repo.commit()
            findings = check.check_repo(repo.path, history=False)
            paths = sorted(f[2] for f in findings if f[0] == "BLOCK")
            self.assertEqual(paths, [".env", "certs/server.key"])

    def test_binary_files_are_not_scanned(self):
        with TempRepo() as repo:
            repo.write("logo.png", "-----BEGIN PRIVATE KEY-----\n")
            repo.commit()
            self.assertEqual(check.check_repo(repo.path, history=False), [])

    def test_undecodable_files_are_skipped(self):
        with TempRepo() as repo:
            (repo.path / "blob.dat").write_bytes(b"\xff\xfe\x00-----BEGIN PRIVATE KEY-----")
            repo.commit()
            self.assertEqual(check.check_repo(repo.path, history=False), [])

    def test_foreign_author_blocks(self):
        with TempRepo() as repo:
            repo.write("a.txt", "x\n")
            repo.commit("Add", name="Somebody Else", email="else@example.org")
            findings = check.check_repo(repo.path, history=False)
            self.assertEqual(len(findings), 1)
            self.assertIn("author or committer", findings[0][3])
            self.assertTrue(findings[0][2].startswith("commit "))

    def test_both_names_of_the_owner_are_allowed(self):
        with TempRepo() as repo:
            repo.write("a.txt", "x\n")
            repo.commit("Add", name="Electro Hobby 3D", email="electrohobby3d@gmail.com")
            self.assertEqual(check.check_repo(repo.path, history=False), [])

    def test_trailers_and_ai_mentions_in_commit_messages_block(self):
        for message in ("Fix\n\nCo-Authored-By: Someone <a@b.c>", "Fix\n\nGenerated with a tool", "Fix\n\nSigned-off-by: X", "Ask " + "Cla" + "ude about it"):   # the word the check refuses, written in two pieces so that this file does not carry it
            with TempRepo() as repo:
                repo.write("a.txt", "x\n")
                repo.commit(message)
                findings = check.check_repo(repo.path, history=False)
                self.assertEqual(len(findings), 1, message)
                self.assertIn("trailer", findings[0][3])

    def test_a_secret_removed_later_is_still_found_in_history(self):
        with TempRepo() as repo:
            repo.write("config.txt", "key line\nhost 93.184.216.34\n")
            repo.commit("Add config")
            repo.write("config.txt", "key line\n")
            repo.commit("Remove address")
            self.assertEqual(check.check_repo(repo.path, history=False), [])
            findings = check.check_repo(repo.path, history=True)
            self.assertEqual(len(findings), 1)
            self.assertEqual(findings[0][0], "BLOCK")
            self.assertIn("a removed line", findings[0][2])
            self.assertIn("public IP", findings[0][3])

    def test_a_removed_address_in_a_test_fixture_is_not_a_finding(self):
        with TempRepo() as repo:
            repo.write("tests/test_a.py", "ADDR = '93.184.216.34'\n")
            repo.commit("Add test")
            repo.write("tests/test_a.py", "ADDR = None\n")
            repo.commit("Edit test")
            self.assertEqual(check.check_repo(repo.path, history=True), [])

    def test_a_key_file_deleted_later_is_found_in_history(self):
        with TempRepo() as repo:
            repo.write("deploy/server.pem", "data\n")
            repo.commit("Add")
            repo.git("rm", "-q", "deploy/server.pem")
            repo.commit("Remove")
            self.assertEqual(check.check_repo(repo.path, history=False), [])
            findings = check.check_repo(repo.path, history=True)
            self.assertTrue(any("tracked in the history" in f[3] for f in findings))

    def test_ref_limits_the_commits_that_are_read(self):
        with TempRepo() as repo:
            repo.write("a.txt", "x\n")
            repo.commit("Add")
            repo.git("branch", "clean")
            repo.write("b.txt", "y\n")
            repo.commit("Add b", name="Somebody Else", email="else@example.org")
            self.assertEqual(check.check_repo(repo.path, history=False, ref="clean"), [])
            self.assertEqual(len(check.check_repo(repo.path, history=False)), 1)

    def test_git_failure_raises(self):
        with TempRepo() as repo:
            with self.assertRaises(RuntimeError):
                check.git(repo.path, "no-such-command")


class MainTests(unittest.TestCase):
    def run_main(self, argv):
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            code = check.main(argv)
        return code, out.getvalue()

    def test_pass_and_fail_exit_codes(self):
        with TempRepo("ARMOR-CLEAN") as clean, TempRepo("ARMOR-DIRTY") as dirty:
            clean.write("a.txt", "x\n")
            clean.commit()
            dirty.write(".env", "A=1\n")
            dirty.commit()
            with mock.patch.object(check, "ROOT", clean.path.parent):
                code, out = self.run_main(["ARMOR-CLEAN", "--no-history"])
                self.assertEqual(code, 0)
                self.assertIn("PUBLICATION_CHECK=PASS", out)
            with mock.patch.object(check, "ROOT", dirty.path.parent):
                code, out = self.run_main(["ARMOR-DIRTY", "--no-history"])
                self.assertEqual(code, 1)
                self.assertIn("PUBLICATION_CHECK=FAIL", out)
                self.assertIn("BLOCK", out)

    def test_review_findings_do_not_fail_the_run(self):
        with TempRepo("ARMOR-REVIEW") as repo:
            repo.write("config.py", 'password = "Zx9qLmN42pT"\n')
            repo.commit()
            with mock.patch.object(check, "ROOT", repo.path.parent):
                code, out = self.run_main(["ARMOR-REVIEW", "--no-history"])
            self.assertEqual(code, 0)
            self.assertIn("REVIEW", out)
            self.assertNotIn("Zx9qLmN42pT", out)

    def test_without_names_every_git_repository_next_to_it_is_checked(self):
        with TempRepo("ARMOR-ONE") as repo:
            repo.write("a.txt", "x\n")
            repo.commit()
            (repo.path.parent / "ARMOR-NOGIT").mkdir()
            with mock.patch.object(check, "ROOT", repo.path.parent):
                code, out = self.run_main(["--no-history"])
            self.assertEqual(code, 0)
            self.assertIn("ARMOR-ONE", out)
            self.assertNotIn("ARMOR-NOGIT", out)

    def test_ref_option_is_passed_through(self):
        with TempRepo("ARMOR-REF") as repo:
            repo.write("a.txt", "x\n")
            repo.commit()
            with mock.patch.object(check, "ROOT", repo.path.parent):
                code, _out = self.run_main(["ARMOR-REF", "--ref=main"])
            self.assertEqual(code, 0)

    def test_long_reports_are_cut(self):
        with TempRepo("ARMOR-MANY") as repo:
            for index in range(70):
                repo.write(f"secrets/token{index}.txt", "x\n")
            repo.commit()
            with mock.patch.object(check, "ROOT", repo.path.parent):
                code, out = self.run_main(["ARMOR-MANY", "--no-history"])
            self.assertEqual(code, 1)
            self.assertIn("and 10 more", out)


if __name__ == "__main__":
    unittest.main()
