"""The tool that copies the canonical CI files of ARMOR-COMMON into every repository."""
import contextlib
import io
import tempfile
import unittest
from pathlib import Path
from unittest import mock

import _support  # noqa: F401  (puts tools/ on the path)

import sync_ci_tools as sync

TARGET = "ARMOR-NODE-RADAR"


class SyncTests(unittest.TestCase):
    def setUp(self):
        holder = tempfile.TemporaryDirectory()
        self.addCleanup(holder.cleanup)
        self.root = Path(holder.name)
        source = self.root / "ARMOR-COMMON" / "tools"
        source.mkdir(parents=True)
        for name in (*sync.VENDORED_FILES, *sync.PICTURE_TOOLS, "ci.yml.template", "e2e.yml.template"):
            (source / name).write_text(f"# canonical {name}\nline two\n", encoding="utf-8", newline="\n")
        (self.root / TARGET).mkdir()
        (self.root / "ARMOR-STUDIO").mkdir()
        for target, value in (("ROOT", self.root), ("SOURCE", source)):
            patcher = mock.patch.object(sync, target, value)
            patcher.start()
            self.addCleanup(patcher.stop)
        self.targets = mock.patch.object(sync, "TARGETS", (TARGET, "ARMOR-NOT-CLONED"))
        self.targets.start()
        self.addCleanup(self.targets.stop)
        self.e2e_targets = mock.patch.object(sync, "E2E_TARGETS", ("ARMOR-STUDIO", "ARMOR-NOT-CLONED"))
        self.e2e_targets.start()
        self.addCleanup(self.e2e_targets.stop)

    def run_main(self, *argv):
        out = io.StringIO()
        with mock.patch("sys.argv", ["sync_ci_tools.py", *argv]), contextlib.redirect_stdout(out):
            code = sync.main()
        return code, out.getvalue()

    def test_a_check_before_the_first_sync_reports_stale_and_creates_nothing(self):
        code, out = self.run_main("--check")
        self.assertEqual(code, 1)
        self.assertIn("SYNC_CI_TOOLS=STALE", out)
        self.assertIn(f"{TARGET}/tools/armor_project_tool.py", out)
        self.assertIn(f"{TARGET}/.github/workflows/ci.yml", out)
        self.assertFalse((self.root / TARGET / "tools").exists())
        self.assertFalse((self.root / TARGET / ".github").exists())

    def test_sync_writes_every_file_and_the_check_then_passes(self):
        code, out = self.run_main()
        self.assertEqual(code, 0)
        # the tools and the picture tools, the workflow, the workflow of ARMOR-COMMON itself and the one that tries Studio and the server together
        self.assertIn(f"files_written={len(sync.VENDORED_FILES) + len(sync.PICTURE_TOOLS) + 3}", out)
        self.assertEqual((self.root / "ARMOR-STUDIO" / ".github" / "workflows" / "e2e.yml").read_text(encoding="utf-8"), "# canonical e2e.yml.template\nline two\n")
        self.assertFalse((self.root / TARGET / ".github" / "workflows" / "e2e.yml").exists(), "only the two repositories that run Studio and the server together carry it")
        for name in (*sync.VENDORED_FILES, *sync.PICTURE_TOOLS):
            self.assertEqual((self.root / TARGET / "tools" / name).read_text(encoding="utf-8"), f"# canonical {name}\nline two\n")
        self.assertEqual((self.root / TARGET / ".github" / "workflows" / "ci.yml").read_text(encoding="utf-8"), "# canonical ci.yml.template\nline two\n")
        self.assertEqual((self.root / "ARMOR-COMMON" / ".github" / "workflows" / "ci.yml").read_text(encoding="utf-8"), "# canonical ci.yml.template\nline two\n")
        code, out = self.run_main("--check")
        self.assertEqual((code, out.strip().splitlines()[-1]), (0, "SYNC_CI_TOOLS=CURRENT"))

    def test_a_second_sync_writes_nothing(self):
        self.run_main()
        code, out = self.run_main()
        self.assertEqual(code, 0)
        self.assertIn("files_written=0", out)

    def test_a_hand_edit_of_a_copy_is_detected_and_overwritten(self):
        self.run_main()
        copy = self.root / TARGET / "tools" / "armor_ci_validate.py"
        copy.write_text("# edited by hand\n", encoding="utf-8")
        code, out = self.run_main("--check")
        self.assertEqual(code, 1)
        self.assertIn(f"{TARGET}/tools/armor_ci_validate.py", out)
        self.assertNotIn("armor_project_tool", out)
        self.run_main()
        self.assertEqual(copy.read_text(encoding="utf-8"), "# canonical armor_ci_validate.py\nline two\n")

    def test_the_canonical_source_is_never_overwritten(self):
        self.run_main()
        for name in (*sync.VENDORED_FILES, *sync.PICTURE_TOOLS):
            self.assertEqual((self.root / "ARMOR-COMMON" / "tools" / name).read_text(encoding="utf-8"), f"# canonical {name}\nline two\n")
        self.assertFalse((self.root / "ARMOR-COMMON" / "tools" / "armor_project_tool.py.bak").exists())

    def test_a_repository_that_is_not_cloned_is_skipped_and_named(self):
        _code, out = self.run_main()
        self.assertIn("SKIP ARMOR-NOT-CLONED", out)
        self.assertFalse((self.root / "ARMOR-NOT-CLONED").exists())

    def test_windows_line_endings_in_a_copy_are_not_a_difference(self):
        self.run_main()
        for path in (self.root / TARGET).rglob("*"):
            if path.is_file():
                path.write_bytes(path.read_bytes().replace(b"\r\n", b"\n").replace(b"\n", b"\r\n"))
        code, out = self.run_main("--check")
        self.assertEqual((code, out.strip().splitlines()[-1]), (0, "SYNC_CI_TOOLS=CURRENT"))

    def test_the_real_list_of_targets_is_the_family(self):
        import importlib
        real = importlib.reload(sync)
        self.assertEqual(len(real.TARGETS), len(set(real.TARGETS)))
        self.assertNotIn("ARMOR-COMMON", real.TARGETS)   # the source never receives a copy of itself
        self.assertIn("ARMOR-DOCS", real.TARGETS)
        self.assertEqual(real.VENDORED_FILES, ("armor_project_tool.py", "armor_ci_validate.py", "_armor_readme_parity.py", "universal_readme_check.py"))


if __name__ == "__main__":
    unittest.main()
