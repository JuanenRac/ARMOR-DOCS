"""Shared helpers of the tests of the documentation tools: the tools are loaded from tools/, and a throwaway git repository is built in a temporary folder (never the real ones)."""
from __future__ import annotations

import os
import subprocess
import sys
import tempfile
from pathlib import Path

TOOLS = Path(__file__).resolve().parents[1] / "tools"
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

AUTHOR_NAME = "JuanenRac (Electro Hobby 3D)"
AUTHOR_EMAIL = "electrohobby3d@gmail.com"


def git_environment(name: str = AUTHOR_NAME, email: str = AUTHOR_EMAIL) -> dict[str, str]:
    """The environment for git in a test: no global or system configuration (hooks, signing, templates) of the machine, and a fixed author."""
    environment = {key: value for key, value in os.environ.items() if not key.startswith("GIT_")}
    environment.update({
        "GIT_CONFIG_GLOBAL": os.devnull, "GIT_CONFIG_NOSYSTEM": "1",
        "GIT_AUTHOR_NAME": name, "GIT_AUTHOR_EMAIL": email, "GIT_COMMITTER_NAME": name, "GIT_COMMITTER_EMAIL": email,
    })
    return environment


class TempRepo:
    """A git repository in a temporary folder; use it as a context manager."""

    def __init__(self, prefix: str = "ARMOR-TEST") -> None:
        self._holder = tempfile.TemporaryDirectory()
        self.path = Path(self._holder.name) / prefix
        self.path.mkdir()
        self.git("init", "-q", "-b", "main")

    def git(self, *args: str, name: str = AUTHOR_NAME, email: str = AUTHOR_EMAIL) -> str:
        result = subprocess.run(["git", "-C", str(self.path), *args], capture_output=True, text=True, encoding="utf-8", env=git_environment(name, email))
        if result.returncode != 0:
            raise RuntimeError(f"git {' '.join(args)}: {result.stderr}")
        return result.stdout.strip()

    def write(self, relative: str, text: str) -> None:
        target = self.path / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(text, encoding="utf-8", newline="\n")

    def commit(self, message: str = "Add files", name: str = AUTHOR_NAME, email: str = AUTHOR_EMAIL) -> None:
        self.git("add", "-A")
        self.git("commit", "-q", "-m", message, name=name, email=email)

    def __enter__(self) -> "TempRepo":
        return self

    def __exit__(self, *exc: object) -> None:
        self._holder.cleanup()
