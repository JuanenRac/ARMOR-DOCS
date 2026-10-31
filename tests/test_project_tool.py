"""The workflow tool that every repository carries a copy of (version odometer, version bump, local secrets, link check). This is the copy of ARMOR-DOCS."""
import contextlib
import io
import json
import os
import sys
import types
import tempfile
import unittest
from pathlib import Path
from unittest import mock

import _support  # noqa: F401  (puts tools/ on the path)

import armor_project_tool as tool


class NextVersionTests(unittest.TestCase):
    def test_the_odometer_never_reaches_ten(self):
        table = {
            "0.0.0": "0.0.1", "0.0.9": "0.1.0", "0.1.9": "0.2.0", "0.6.9": "0.7.0",
            "0.7.8": "0.7.9", "0.7.9": "0.8.0.0",
            "0.8.0.0": "0.8.0.1", "0.8.0.9": "0.8.1.0", "0.8.9.9": "0.9.0.0", "0.9.9.9": "1.0.0.0",
            "0.8.4.3": "0.8.4.4",
        }
        for before, after in table.items():
            self.assertEqual(tool.next_version(before), after, before)

    def test_a_three_component_version_from_0_8_gains_its_fourth_component(self):
        self.assertEqual(tool.next_version("0.8.0"), "0.8.0.0")
        self.assertEqual(tool.next_version("0.8.3"), "0.8.3.0")
        self.assertEqual(tool.next_version("0.9.1"), "0.9.1.0")

    def test_no_component_of_the_result_is_two_digits(self):
        version = "0.0.0"
        for _ in range(400):
            version = tool.next_version(version)
            self.assertTrue(all(len(part) == 1 for part in version.split(".")), version)

    def test_the_result_is_always_greater_than_the_input(self):
        def key(value):
            return tuple((list(map(int, value.split("."))) + [0] * 4)[:4])
        version = "0.7.0"
        for _ in range(60):
            following = tool.next_version(version)
            self.assertGreater(key(following), key(version))
            version = following

    def test_garbage_is_rejected(self):
        for bad in ("", "a.b.c"):
            with self.assertRaises(ValueError, msg=bad):
                tool.next_version(bad)


def make_project(name="ARMOR-NETWORK", version="0.7.9", changelog=True, pyproject=True, init=True):
    holder = tempfile.TemporaryDirectory()
    project = Path(holder.name) / name
    project.mkdir()
    manifest = {"schema_version": "1.0", "ecosystem": "A.R.M.O.R.", "name": name, "version": version, "native_version": version}
    (project / "armor.project.json").write_text(json.dumps(manifest), encoding="utf-8")
    if changelog:
        (project / "CHANGELOG.md").write_text("# Changelog\n\nAll notable changes.\n\n## [%s] - 2000-01-01\n\n- Something.\n" % version, encoding="utf-8")
    if pyproject:
        (project / "pyproject.toml").write_text(f'[project]\nname = "x"\nversion = "{version}"\n', encoding="utf-8")
    if init:
        (project / "src" / "package").mkdir(parents=True)
        (project / "src" / "package" / "__init__.py").write_text(f'"""Doc."""\n__version__ = "{version}"\n', encoding="utf-8")
    return holder, project, manifest


class BumpTests(unittest.TestCase):
    def test_the_manifest_changelog_pyproject_and_package_move_together(self):
        holder, project, manifest = make_project(version="0.7.9")
        self.addCleanup(holder.cleanup)
        before, after = tool.bump(project, manifest)
        self.assertEqual((before, after), ("0.7.9", "0.8.0.0"))
        saved = json.loads((project / "armor.project.json").read_text(encoding="utf-8"))
        self.assertEqual((saved["version"], saved["native_version"]), ("0.8.0.0", "0.8.0.0"))
        self.assertIn('version = "0.8.0.0"', (project / "pyproject.toml").read_text(encoding="utf-8"))
        self.assertIn('__version__ = "0.8.0.0"', (project / "src" / "package" / "__init__.py").read_text(encoding="utf-8"))
        changelog = (project / "CHANGELOG.md").read_text(encoding="utf-8")
        self.assertIn("## [0.8.0.0] - ", changelog)
        # the new entry goes on top, above the old one
        self.assertLess(changelog.index("[0.8.0.0]"), changelog.index("[0.7.9]"))

    def test_a_manifest_that_is_not_numeric_is_refused_and_nothing_changes(self):
        for bad in ("1.2", "1.2.x", "1.2.3.4.5", "v1.2.3"):
            holder, project, manifest = make_project(version="0.1.1")
            self.addCleanup(holder.cleanup)
            manifest["version"] = bad
            before = (project / "armor.project.json").read_text(encoding="utf-8")
            with self.assertRaises(RuntimeError):
                tool.bump(project, manifest)
            self.assertEqual((project / "armor.project.json").read_text(encoding="utf-8"), before)

    def test_a_project_without_changelog_gets_one(self):
        holder, project, manifest = make_project(version="0.1.1", changelog=False)
        self.addCleanup(holder.cleanup)
        tool.bump(project, manifest)
        text = (project / "CHANGELOG.md").read_text(encoding="utf-8")
        self.assertTrue(text.startswith("# Changelog"))
        self.assertIn("## [0.1.2]", text)

    def test_other_projects_do_not_get_a_pyproject_written(self):
        holder, project, manifest = make_project(name="ARMOR-SERVER", version="0.1.1", pyproject=False, init=False)
        self.addCleanup(holder.cleanup)
        tool.bump(project, manifest)
        self.assertFalse((project / "pyproject.toml").exists())

    def test_the_android_client_keeps_gradle_in_step(self):
        holder, project, manifest = make_project(name="ARMOR-ANDROID-CONTROL", version="0.8.0.9", pyproject=False, init=False)
        self.addCleanup(holder.cleanup)
        (project / "app").mkdir()
        gradle = project / "app" / "build.gradle.kts"
        gradle.write_text('android {\n  defaultConfig {\n    versionCode = 41\n    versionName = "0.8.0.9"\n  }\n}\n', encoding="utf-8")
        tool.bump(project, manifest)
        text = gradle.read_text(encoding="utf-8")
        self.assertIn("versionCode = 42", text)
        self.assertIn('versionName = "0.8.1.0"', text)

    def test_the_android_client_without_gradle_fields_is_an_error(self):
        holder, project, manifest = make_project(name="ARMOR-ANDROID-CONTROL", version="0.8.0.9", pyproject=False, init=False)
        self.addCleanup(holder.cleanup)
        with self.assertRaises(RuntimeError):
            tool.bump(project, manifest)
        (project / "app").mkdir()
        (project / "app" / "build.gradle.kts").write_text("android {}\n", encoding="utf-8")
        with self.assertRaises(RuntimeError):
            tool.bump(project, manifest)


class LocalSecretsTests(unittest.TestCase):
    def test_a_first_run_creates_distinct_high_entropy_values(self):
        with tempfile.TemporaryDirectory() as folder:
            project = Path(folder)
            with contextlib.redirect_stdout(io.StringIO()) as out:
                environment = tool.load_server_environment(project, {})
            self.assertIn("CREATED", out.getvalue())
            tokens = [environment[key] for key in ("ARMOR_INGEST_TOKEN", "ARMOR_CONTROL_TOKEN", "ARMOR_OPERATOR_TOKEN", "ARMOR_CAMERA_CONFIG_KEY", "ARMOR_STUDIO_PASSWORD")]
            self.assertEqual(len(set(tokens)), 5)
            for token in tokens:
                self.assertGreaterEqual(len(token), 32 if token != environment["ARMOR_STUDIO_PASSWORD"] else 24)
            self.assertEqual(environment["ARMOR_PORT"], "8080")
            self.assertEqual(environment["ARMOR_STUDIO_ORIGIN"], "http://127.0.0.1:5178")

    def test_the_file_is_created_once_and_read_afterwards(self):
        with tempfile.TemporaryDirectory() as folder:
            project = Path(folder)
            with contextlib.redirect_stdout(io.StringIO()):
                first = tool.load_server_environment(project, {})
            written = (project / ".env").read_text(encoding="utf-8")
            with contextlib.redirect_stdout(io.StringIO()) as out:
                second = tool.load_server_environment(project, {})
            self.assertNotIn("CREATED", out.getvalue())
            self.assertEqual((project / ".env").read_text(encoding="utf-8"), written)
            self.assertEqual(first["ARMOR_INGEST_TOKEN"], second["ARMOR_INGEST_TOKEN"])

    def test_the_operating_system_value_wins_but_an_empty_one_does_not_shadow_the_file(self):
        with tempfile.TemporaryDirectory() as folder:
            project = Path(folder)
            (project / ".env").write_text("# comment\n\nA=from-file\nB=from-file\nC=from-file\nD=from-file\nno equals sign\n E = spaced \n", encoding="utf-8")
            environment = tool.load_server_environment(project, {"A": "from-os", "B": "", "C": "replace-with-your-value"})
            self.assertEqual(environment["A"], "from-os")
            self.assertEqual(environment["B"], "from-file")
            self.assertEqual(environment["C"], "from-file")
            self.assertEqual(environment["D"], "from-file")
            self.assertEqual(environment["E"], "spaced")
            self.assertNotIn("no equals sign", environment)

    def test_a_value_with_an_equals_sign_is_kept_whole(self):
        with tempfile.TemporaryDirectory() as folder:
            project = Path(folder)
            (project / ".env").write_text("TOKEN=abc==def=\n", encoding="utf-8")
            self.assertEqual(tool.load_server_environment(project, {})["TOKEN"], "abc==def=")


class LinkCheckTests(unittest.TestCase):
    def check(self, files):
        with tempfile.TemporaryDirectory() as folder:
            project = Path(folder)
            for relative, text in files.items():
                target = project / relative
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_text(text, encoding="utf-8")
            out = io.StringIO()
            with contextlib.redirect_stdout(out):
                tool.validate_markdown_links(project)
            return out.getvalue()

    def test_valid_links_pass(self):
        out = self.check({"README.md": "[doc](docs/A.md) [anchor](docs/A.md#top) [web](https://example.org) [mail](mailto:a@b.c) [self](#x)", "docs/A.md": "[up](../README.md)"})
        self.assertIn("ARMOR_DOCS_LINKS=PASS", out)

    def test_a_missing_target_is_reported_with_its_file(self):
        with self.assertRaises(RuntimeError) as caught:
            self.check({"README.md": "[gone](docs/nowhere.md)", "docs/A.md": "ok"})
        self.assertIn("README.md -> docs/nowhere.md", str(caught.exception))

    def test_every_broken_link_is_listed(self):
        with self.assertRaises(RuntimeError) as caught:
            self.check({"a.md": "[x](one.md) [y](two.md)"})
        self.assertIn("one.md", str(caught.exception))
        self.assertIn("two.md", str(caught.exception))


class LintTests(unittest.TestCase):
    """The lint and type-check step: ruff and mypy at pinned versions, over src/ where a repository has a mypy configuration and over tools/ and scripts/ wherever they hold Python."""

    def project(self, files: dict[str, str]) -> Path:
        folder = tempfile.TemporaryDirectory()
        self.addCleanup(folder.cleanup)
        root = Path(folder.name)
        for relative, text in files.items():
            target = root / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(text, encoding="utf-8")
        return root

    def run_lint(self, root: Path, manifest: dict[str, object]):
        calls: list[list[str]] = []
        out = io.StringIO()
        with mock.patch.object(tool, "command", side_effect=lambda cwd, args, env=None: calls.append(list(args))), contextlib.redirect_stdout(out):
            tool.lint(root, manifest)
        return calls, out.getvalue()

    def test_the_versions_are_pinned_and_the_rules_are_the_agreed_ones(self):
        self.assertEqual(tool.LINT_PINS, ("ruff==0.17.1", "mypy==2.4.0"))
        self.assertEqual(tool.LINT_RULES, "F,E9,B")

    def test_a_repository_with_source_and_a_mypy_configuration_runs_both_tools(self):
        root = self.project({"src/pkg/a.py": "x = 1\n", "pyproject.toml": "[tool.mypy]\nfiles = ['src']\n"})
        calls, out = self.run_lint(root, {})
        self.assertEqual([call[1:4] for call in calls], [["-m", "pip", "install"], ["-m", "ruff", "check"], ["-m", "mypy"]])
        self.assertIn("ruff==0.17.1", calls[0])
        self.assertIn("mypy==2.4.0", calls[0])
        self.assertEqual(calls[1][calls[1].index("--select") + 1], "F,E9,B")
        self.assertNotIn("PySide6-Essentials", calls[0])
        self.assertIn("ARMOR_LINT=PASS", out)

    def test_mypy_ini_and_setup_cfg_count_as_a_configuration(self):
        for name, text in (("mypy.ini", "[mypy]\n"), ("setup.cfg", "[mypy]\nfiles = src\n")):
            root = self.project({"src/pkg/a.py": "x = 1\n", name: text})
            self.assertEqual(tool.lint_plan(root, {}), (True, ""), name)

    def test_qt_stubs_are_installed_only_where_the_code_imports_qt(self):
        root = self.project({"src/pkg/gui.py": "from PySide6 import QtCore\n", "pyproject.toml": "[tool.mypy]\n"})
        calls, _out = self.run_lint(root, {})
        self.assertIn("PySide6-Essentials", calls[0])

    def test_without_a_mypy_configuration_the_step_is_skipped(self):
        root = self.project({"src/pkg/a.py": "x = 1\n", "pyproject.toml": "[project]\nname = 'x'\n"})
        calls, out = self.run_lint(root, {})
        self.assertEqual(calls, [])
        self.assertIn("ARMOR_LINT=SKIP no mypy configuration", out)

    def test_without_python_source_the_step_is_skipped(self):
        for files in ({"pyproject.toml": "[tool.mypy]\n"}, {"pyproject.toml": "[tool.mypy]\n", "src/readme.txt": "no code"}, {"tools/readme.txt": "no code"}):
            root = self.project(files)
            calls, out = self.run_lint(root, {})
            self.assertEqual(calls, [])
            self.assertIn("ARMOR_LINT=SKIP no mypy configuration and no Python under tools/ or scripts/", out)

    def test_tools_and_scripts_are_type_checked_on_their_own_wherever_they_hold_python(self):
        for folder in ("tools", "scripts"):
            root = self.project({f"{folder}/a.py": "x = 1\n"})
            calls, out = self.run_lint(root, {})
            self.assertEqual([call[1:4] for call in calls], [["-m", "pip", "install"], ["-m", "ruff", "check"], ["-m", "mypy", "--config-file="]], folder)
            self.assertEqual(calls[2][-1], folder)
            self.assertIn("--platform", calls[2])   # the platform of CI, so a Windows checkout sees what CI sees
            self.assertIn("ARMOR_LINT=PASS", out)

    def test_a_repository_with_source_and_tools_checks_both_and_the_tools_ignore_its_mypy_settings(self):
        root = self.project({"src/pkg/a.py": "x = 1\n", "tools/b.py": "y = 2\n", "scripts/c.py": "z = 3\n", "pyproject.toml": "[tool.mypy]\nfiles = ['src']\n"})
        calls, _out = self.run_lint(root, {})
        self.assertEqual(calls[2][1:], ["-m", "mypy"])
        self.assertEqual(calls[3][1:3], ["-m", "mypy"])
        self.assertIn("--config-file=", calls[3])
        self.assertEqual(calls[3][-2:], ["tools", "scripts"])

    def test_lint_tools_false_leaves_out_only_the_tools(self):
        text = "[tool.mypy]\nfiles = ['src']\n\n[tool.armor]\nlint_tools = false\n"
        both = self.project({"src/pkg/a.py": "x = 1\n", "tools/b.py": "y = 2\n", "pyproject.toml": text})
        calls, _out = self.run_lint(both, {})
        self.assertEqual([call[1:3] for call in calls], [["-m", "pip"], ["-m", "ruff"], ["-m", "mypy"]])
        self.assertNotIn("--config-file=", calls[2])
        alone = self.project({"tools/b.py": "y = 2\n", "pyproject.toml": "[tool.armor]\nlint_tools = false\n"})
        calls, out = self.run_lint(alone, {})
        self.assertEqual(calls, [])
        self.assertIn("lint_tools", out)

    def test_two_findings_of_the_shared_host_tests_are_the_only_ones_tolerated(self):
        root = self.project({"tools/a.py": "x = 1\n"})
        calls, _out = self.run_lint(root, {})
        self.assertEqual(calls[1][calls[1].index("--per-file-ignores") + 1], "**/check_mosquitto.py:B904,**/check_task_safety.py:B007")

    def test_qt_stubs_are_also_installed_where_a_tool_imports_qt(self):
        root = self.project({"tools/icon.py": "from PySide6 import QtGui\n"})
        calls, _out = self.run_lint(root, {})
        self.assertIn("PySide6-Essentials", calls[0])

    def test_the_switch_in_pyproject_skips_a_repository_that_would_run(self):
        off = self.project({"src/pkg/a.py": "x = 1\n", "pyproject.toml": "[tool.mypy]\nfiles = ['src']\n\n[tool.armor]\nci_lint = false\n"})
        calls, out = self.run_lint(off, {})
        self.assertEqual(calls, [])
        self.assertIn("ci_lint", out)
        on = self.project({"src/pkg/a.py": "x = 1\n", "pyproject.toml": "[tool.armor]\nci_lint = true\n\n[tool.mypy]\n"})
        self.assertEqual(self.run_lint(on, {})[0][1][1:3], ["-m", "ruff"])
        other_table = self.project({"src/pkg/a.py": "x = 1\n", "pyproject.toml": "[tool.mypy]\n\n[tool.other]\nci_lint = false\n"})
        self.assertTrue(tool.lint_plan(other_table, {})[0])

    def test_the_action_reaches_the_step_and_a_skip_is_not_an_error(self):
        root = self.project({"armor.project.json": json.dumps({"ecosystem": "A.R.M.O.R.", "name": "ARMOR-X", "version": "0.0.1"})})
        out = io.StringIO()
        with mock.patch.object(sys, "argv", ["armor_project_tool.py", "lint", str(root)]), contextlib.redirect_stdout(out):
            self.assertEqual(tool.main(), 0)
        self.assertIn("ARMOR_LINT=SKIP", out.getvalue())


class SmallHelpersTests(unittest.TestCase):
    def test_siblings_required_follows_the_environment(self):
        for value, expected in (("", False), ("0", False), ("1", True), ("yes", True)):
            with mock.patch.dict(os.environ, {"ARMOR_REQUIRE_SIBLINGS": value}):
                self.assertEqual(tool.siblings_required(), expected, value)
        with mock.patch.dict(os.environ, {}, clear=False):
            os.environ.pop("ARMOR_REQUIRE_SIBLINGS", None)
            self.assertFalse(tool.siblings_required())

    def test_check_tool_names_what_is_missing(self):
        with self.assertRaises(RuntimeError) as caught:
            tool.check_tool("no-such-program-armor", "install the thing")
        self.assertEqual(str(caught.exception), "install the thing")
        self.assertTrue(tool.check_tool("python" if os.name == "nt" else "sh", "x"))

    def test_command_reports_exit_codes_and_missing_programs(self):
        with tempfile.TemporaryDirectory() as folder, contextlib.redirect_stdout(io.StringIO()):
            project = Path(folder)
            tool.command(project, [sys.executable, "-c", "pass"])
            with self.assertRaises(RuntimeError) as caught:
                tool.command(project, [sys.executable, "-c", "raise SystemExit(3)"])
            self.assertIn("exit code 3", str(caught.exception))
            with self.assertRaises(RuntimeError) as caught:
                tool.command(project, ["no-such-program-armor"])
            self.assertIn("was not found", str(caught.exception))

    def test_an_unregistered_project_has_no_build_rule(self):
        with tempfile.TemporaryDirectory() as folder:
            with self.assertRaises(RuntimeError):
                tool.test_project(Path(folder), {"name": "ARMOR-UNKNOWN"})
            with self.assertRaises(RuntimeError):
                tool.run_project(Path(folder), {"name": "ARMOR-UNKNOWN"})


class UnitTestRunnerTests(unittest.TestCase):
    def test_a_repository_without_a_tests_folder_says_so_and_goes_on(self):
        with tempfile.TemporaryDirectory() as folder, contextlib.redirect_stdout(io.StringIO()) as out:
            tool.unit_tests(Path(folder))
        self.assertIn("UNIT_TESTS=SKIPPED", out.getvalue())

    def test_the_tests_of_the_folder_are_run_and_a_failure_fails_the_build(self):
        with tempfile.TemporaryDirectory() as folder, contextlib.redirect_stdout(io.StringIO()):
            project = Path(folder)
            (project / "tests").mkdir()
            (project / "tests" / "test_good.py").write_text("import unittest\nclass T(unittest.TestCase):\n    def test_ok(self):\n        self.assertTrue(True)\n", encoding="utf-8")
            (project / "tests" / "helper.py").write_text("raise SystemExit('only files named test_*.py are collected')\n", encoding="utf-8")
            tool.unit_tests(project)
            (project / "tests" / "test_bad.py").write_text("import unittest\nclass T(unittest.TestCase):\n    def test_no(self):\n        self.assertTrue(False)\n", encoding="utf-8")
            real_run = tool.subprocess.run
            quiet = lambda *args, **options: real_run(*args, **{**options, "capture_output": True})   # the failing test of the example is not news in this run
            with mock.patch.object(tool.subprocess, "run", side_effect=quiet), self.assertRaises(RuntimeError):
                tool.unit_tests(project)

    def test_the_deployment_project_runs_its_tests_where_it_can_and_names_what_it_leaves_out(self):
        self.assertEqual(tool.DEVOPS_SHELL_TESTS_LEFT_OUT, {"test_compose.sh", "test_admin_agent.sh", "test_maintenance_agent.sh"})
        with tempfile.TemporaryDirectory() as folder, contextlib.redirect_stdout(io.StringIO()) as out, mock.patch.object(tool, "os", types.SimpleNamespace(name="nt")):
            tool.devops_tests(Path(folder))
        self.assertIn("DEVOPS_TESTS=SKIPPED", out.getvalue())

    def test_the_deployment_tests_run_every_shell_test_except_the_ones_left_out(self):
        with tempfile.TemporaryDirectory() as folder:
            project = Path(folder)
            (project / "scripts").mkdir()
            for name in ("test_backup.sh", "test_ddns.sh", "test_compose.sh", "test_admin_agent.sh", "test_maintenance_agent.sh", "helper.sh"):
                (project / "scripts" / name).write_text("exit 0\n", encoding="utf-8")
            calls = []
            with mock.patch.object(tool, "os", types.SimpleNamespace(name="posix")), mock.patch.object(tool, "command", side_effect=lambda cwd, args, env=None: calls.append(args)), \
                    mock.patch.object(tool, "check_tool", return_value="bash"):
                tool.devops_tests(project)
        self.assertEqual(calls[0][1:3], ["-W", "ignore"])
        self.assertEqual([Path(call[1]).name for call in calls[1:]], ["test_backup.sh", "test_ddns.sh"])


class DispatchTests(unittest.TestCase):
    """What build-test runs for each kind of project, with the commands recorded instead of run (a toolchain is not needed to know what would be asked of it)."""

    def run_for(self, name, files=()):
        calls = []
        with tempfile.TemporaryDirectory() as folder:
            project = Path(folder) / name
            project.mkdir()
            for relative in files:
                (project / relative).parent.mkdir(parents=True, exist_ok=True)
                (project / relative).write_text("", encoding="utf-8")
            with mock.patch.object(tool, "command", side_effect=lambda cwd, args, env=None: calls.append((list(args), env))), \
                    mock.patch.object(tool, "check_tool", side_effect=lambda tool_name, message: tool_name), \
                    mock.patch.object(tool, "project_python", return_value="venv-python"), \
                    mock.patch.object(tool, "devops_tests"), contextlib.redirect_stdout(io.StringIO()):
                tool.test_project(project, {"name": name})
        return calls

    def test_python_projects_run_their_unit_tests_with_src_on_the_path(self):
        for name in sorted(tool.PYTHON_PROJECTS - {"ARMOR-COMMON"}):
            ((args, env),) = self.run_for(name)
            self.assertEqual(args[1:], ["-m", "unittest", "discover", "-s", "tests"], name)
            self.assertTrue(env["PYTHONPATH"].startswith(str(Path(tempfile.gettempdir()))) or "src" in env["PYTHONPATH"], name)

    def test_the_updater_runs_pytest_from_its_own_environment(self):
        ((args, env),) = self.run_for("ARMOR-UPDATER")
        self.assertEqual(args, ["venv-python", "-m", "pytest", "tests", "-q"])
        self.assertIn("src", env["PYTHONPATH"])

    def test_node_projects_install_once_then_check_test_and_build(self):
        for name in sorted(tool.NODE_PROJECTS):
            calls = [args for args, _env in self.run_for(name)]
            self.assertEqual([call[1:] for call in calls], [["ci"], ["run", "typecheck"], ["test"], ["run", "build"]], name)

    def test_an_installed_node_project_is_not_reinstalled(self):
        calls = [args for args, _env in self.run_for("ARMOR-SERVER", files=("node_modules/.keep",))]
        self.assertEqual([call[1:] for call in calls], [["run", "typecheck"], ["test"], ["run", "build"]])

    def test_the_hardware_project_renders_every_piece_and_every_preset(self):
        calls = [args for args, _env in self.run_for("ARMOR-HARDWARE")]
        self.assertEqual(len(calls), 1 + 2 + 6)
        rendered = [" ".join(call) for call in calls]
        self.assertTrue(any("view_mode=2" in line for line in rendered))
        self.assertTrue(any("view_mode=3" in line for line in rendered))
        for preset in ("solar", "electrical", "alarm"):
            for part in ("box", "lid"):
                self.assertTrue(any(f'part="{part}"' in line and f'preset="{preset}"' in line for line in rendered), (preset, part))

    def test_the_deployment_project_checks_the_compose_topology(self):
        calls = [args for args, _env in self.run_for("ARMOR-DEVOPS", files=(".env",))]
        self.assertEqual(calls, [["docker", "compose", "config", "--quiet"]])

    def test_the_deployment_project_makes_throwaway_secrets_only_when_it_has_none(self):
        calls = [args for args, _env in self.run_for("ARMOR-DEVOPS")]
        self.assertEqual(calls[0], ["bash", "scripts/generate_secrets.sh"])

    def test_the_documentation_project_checks_its_links_and_runs_its_tests(self):
        calls = [args for args, _env in self.run_for("ARMOR-DOCS", files=("tests/test_x.py",))]
        self.assertEqual(calls[0][1:], ["-m", "unittest", "discover", "-s", "tests", "-p", "test_*.py"])


class MainTests(unittest.TestCase):
    def run_main(self, *argv):
        out, err = io.StringIO(), io.StringIO()
        with mock.patch("sys.argv", ["armor_project_tool.py", *argv]), contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            try:
                code = tool.main()
            except RuntimeError as error:
                code = f"error: {error}"
        return code, out.getvalue()

    def test_a_folder_without_a_manifest_is_refused(self):
        with tempfile.TemporaryDirectory() as folder:
            code, _out = self.run_main("build-test", folder)
            self.assertIn("manifest not found", code)

    def test_a_manifest_of_another_ecosystem_is_refused(self):
        with tempfile.TemporaryDirectory() as folder:
            (Path(folder) / "armor.project.json").write_text(json.dumps({"ecosystem": "Other", "name": "X", "version": "1.0.0"}), encoding="utf-8")
            code, _out = self.run_main("build-test", folder)
            self.assertIn("non-A.R.M.O.R.", code)

    def test_the_docs_project_runs_the_link_check_and_the_unit_tests(self):
        holder, project, manifest = make_project(name="ARMOR-DOCS", version="0.1.1", pyproject=False, init=False)
        self.addCleanup(holder.cleanup)
        manifest["ecosystem"] = "A.R.M.O.R."
        (project / "armor.project.json").write_text(json.dumps(manifest), encoding="utf-8")
        (project / "README.md").write_text("[broken](missing.md)", encoding="utf-8")
        code, _out = self.run_main("build-test", str(project))
        self.assertIn("broken local Markdown links", code)

    def test_build_test_does_not_touch_the_version_files(self):
        holder, project, manifest = make_project(name="ARMOR-DOCS", version="0.1.1", pyproject=False, init=False)
        self.addCleanup(holder.cleanup)
        (project / "README.md").write_text("no links", encoding="utf-8")
        before = (project / "armor.project.json").read_text(encoding="utf-8"), (project / "CHANGELOG.md").read_text(encoding="utf-8")
        code, out = self.run_main("build-test", str(project))
        self.assertEqual(code, 0)
        self.assertIn("BUILD_TEST=PASS", out)
        self.assertEqual(before, ((project / "armor.project.json").read_text(encoding="utf-8"), (project / "CHANGELOG.md").read_text(encoding="utf-8")))


if __name__ == "__main__":
    unittest.main()
