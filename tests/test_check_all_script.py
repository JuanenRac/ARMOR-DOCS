"""tools/check_all.sh runs every check of the family; here only what can be said about it without running the other repositories."""
import os
import re
import shutil
import subprocess
import unittest
from pathlib import Path

import _support  # noqa: F401  (puts tools/ on the path)

from make_readmes import ORDER

SCRIPT = Path(__file__).resolve().parents[1] / "tools" / "check_all.sh"
TEXT = SCRIPT.read_text(encoding="utf-8")


class CheckAllScriptTests(unittest.TestCase):
    def test_it_is_a_bash_script_that_stops_on_unset_variables_and_failed_pipes(self):
        self.assertTrue(TEXT.startswith("#!/usr/bin/env bash"))
        self.assertIn("set -uo pipefail", TEXT)

    def test_it_has_unix_line_endings_in_the_repository_blob(self):
        # a CRLF script fails on Linux with "$'\r': command not found"; the working tree may be converted by git, the check is on what the file declares
        if b"\r\n" in SCRIPT.read_bytes():
            self.skipTest("the working copy has Windows line endings (git converts them on commit)")
        self.assertNotIn(b"\r", SCRIPT.read_bytes())

    def test_every_repository_it_names_is_a_repository_of_the_family(self):
        named = set(re.findall(r"\b(ARMOR-[A-Z0-9-]*[A-Z0-9])\b", TEXT))
        self.assertTrue(named)
        self.assertLessEqual(named, set(ORDER), sorted(named - set(ORDER)))

    def test_every_tool_it_calls_exists(self):
        tools = Path(__file__).resolve().parents[1] / "tools"
        for name in set(re.findall(r"tools/([a-z_]+\.py)", TEXT)):
            if name == "sync_firmware_base.py":   # lives in ARMOR-COMMON
                continue
            self.assertTrue((tools / name).is_file() or name in ("armor_project_tool.py",), name)

    def test_a_missing_tool_is_a_skip_and_a_failure_changes_the_exit_status(self):
        self.assertIn('report "$name" FAIL', TEXT)
        self.assertIn("skip()", TEXT)
        self.assertIn("ARMOR_CHECK_ALL=FAIL", TEXT)
        self.assertRegex(TEXT, r'\[\[ "\$FAILED" -eq 0 \]\].*\n?.*ARMOR_CHECK_ALL=PASS')

    def test_the_syntax_is_valid(self):
        bash = shutil.which("bash")
        if bash is None or os.name == "nt":   # on Windows `bash` may be the WSL launcher, which cannot read a Windows path; the script is checked in WSL by hand
            self.skipTest("bash -n runs where bash is the native shell")
        result = subprocess.run([bash, "-n", str(SCRIPT)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)


if __name__ == "__main__":
    unittest.main()
