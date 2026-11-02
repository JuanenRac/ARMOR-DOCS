"""The Screenshots section: read from docs/screenshots.json, checked (eight languages, files, weight) and rendered as picture plus caption."""
from __future__ import annotations

import contextlib
import importlib.util
import io
import json
import tempfile
import unittest
from pathlib import Path

import _support  # noqa: F401  (puts tools/ on the path)

from readme_src import shots

TOOL = Path(__file__).resolve().parents[1] / "tools" / "screenshots_check.py"
PNG = shots.PNG_MAGIC + b"\x00" * 32


def texts(prefix: str) -> dict[str, str]:
    return {lg: f"{prefix} {lg}" for lg in shots.LANGS}


def screen(name: str = "overview.png") -> dict:
    return {"file": name, "alt": texts("alt"), "caption": texts("caption")}


def load_tool():
    spec = importlib.util.spec_from_file_location("shots_check_tool", TOOL)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class ShotsTest(unittest.TestCase):
    def make_repo(self, screens: list[dict], files: dict[str, bytes] | None = None) -> Path:
        holder = tempfile.TemporaryDirectory()
        self.addCleanup(holder.cleanup)
        repo = Path(holder.name) / "ARMOR-DEMO"
        (repo / "docs").mkdir(parents=True)
        (repo / "images" / "screenshots").mkdir(parents=True)
        (repo / "docs" / "screenshots.json").write_text(json.dumps({"screens": screens}), encoding="utf-8")
        for name, data in (files or {}).items():
            (repo / "images" / "screenshots" / name).write_bytes(data)
        return repo

    def test_a_repository_without_the_file_has_no_section(self):
        with tempfile.TemporaryDirectory() as folder:
            self.assertFalse(shots.has(Path(folder)))
            self.assertEqual(shots.problems(Path(folder)), [])

    def test_a_good_manifest_renders_picture_and_caption_in_every_language(self):
        repo = self.make_repo([screen()], {"overview.png": PNG})
        self.assertEqual(shots.problems(repo), [])
        for lg in shots.LANGS:
            body = shots.section(lg, repo)
            self.assertTrue(body.startswith(shots.NOTE[lg]))
            self.assertIn(f'<img src="images/screenshots/overview.png" alt="alt {lg}" width="100%">', body)
            self.assertIn(f'<p align="center"><em>caption {lg}</em></p>', body)

    def test_the_heading_and_the_note_exist_in_eight_languages(self):
        self.assertEqual(set(shots.NOTE), set(shots.LANGS))
        self.assertEqual(set(shots.HEADING), set(shots.LANGS))

    def test_problems_name_a_missing_file_a_heavy_one_and_a_missing_language(self):
        broken = screen("gone.png")
        del broken["caption"]["ja"]
        repo = self.make_repo([broken, screen("heavy.png"), screen("fake.png")],
                              {"heavy.png": PNG + b"\x00" * shots.MAX_BYTES, "fake.png": b"GIF89a"})
        found = " | ".join(shots.problems(repo))
        for part in ("'caption' lacks ja", "gone.png", "does not exist", "heavy.png", "at most", "fake.png: not a PNG"):
            self.assertIn(part, found)
        with self.assertRaises(ValueError):
            shots.section("en", repo)

    def test_more_than_eight_screens_or_a_repeated_one_are_refused(self):
        many = [screen(f"s{i}.png") for i in range(shots.MAX_SHOTS + 1)]
        repo = self.make_repo(many, {f"s{i}.png": PNG for i in range(shots.MAX_SHOTS + 1)})
        self.assertTrue(any("at most 8" in problem for problem in shots.problems(repo)))
        twice = self.make_repo([screen(), screen()], {"overview.png": PNG})
        self.assertTrue(any("listed twice" in problem for problem in shots.problems(twice)))

    def test_the_check_tool_wants_the_pictures_in_the_file_tree(self):
        tool = load_tool()
        repo = self.make_repo([screen()], {"overview.png": PNG})
        self.assertEqual(tool.check_repository(repo), [])
        (repo / "docs" / "structure.json").write_text('{"items": ["overview.png"]}', encoding="utf-8")
        self.assertIn("does not mention the screenshots", tool.check_repository(repo)[0])
        (repo / "docs" / "structure.json").write_text('{"desc": "README banner and screenshots"}', encoding="utf-8")
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            self.assertEqual(tool.main(["--repo", str(repo)]), 0)
        self.assertIn("SCREENSHOTS=PASS", out.getvalue())


if __name__ == "__main__":
    unittest.main()
