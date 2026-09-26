#!/usr/bin/env python3
"""ARMOR-DOCS - a publishable copy of a repository: its current files as ONE commit, with none of the history behind it.

Copyright (C) 2026 JuanenRac (Electro Hobby 3D). GPL-3.0-or-later.

    python tools/clean_history.py ARMOR-STUDIO            # a dry run: says what it would do and checks the files
    python tools/clean_history.py ARMOR-STUDIO --apply    # makes the branch `publicacion` with one root commit
    python tools/clean_history.py --all --apply           # every ARMOR-* repository

The working history is never touched: `main` (or whatever branch you are on) stays as it is, and the new branch is one commit whose tree is
exactly the current one, by the project's author and with a plain message, no trailer. Nothing is pushed: to publish, add the remote yourself and
push that branch (`git push <remote> publicacion:main`). The files are checked first with tools/publication_check.py (without history, because the
new branch has none) and the new branch is checked after; a repository with BLOCK findings, or with uncommitted changes, is refused.
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import publication_check as check  # noqa: E402

BRANCH = "publicacion"
MESSAGE = "Commit inicial"


def git(repo: Path, *args: str, env: dict[str, str] | None = None) -> str:
    import os
    result = subprocess.run(["git", "-C", str(repo), *args], capture_output=True, text=True, encoding="utf-8", errors="replace", env={**os.environ, **(env or {})})
    if result.returncode != 0:
        raise RuntimeError(f"git {' '.join(args)} failed in {repo.name}: {result.stderr.strip()[:200]}")
    return result.stdout.strip()


def prepare(repo: Path, apply: bool) -> bool:
    name = repo.name
    if git(repo, "status", "--porcelain"):
        print(f"{name:24} REFUSED  there are uncommitted changes: commit or stash them first")
        return False
    blocks = [f for f in check.check_repo(repo, history=False) if f[0] == "BLOCK" and not f[2].startswith("commit ")]
    if blocks:
        print(f"{name:24} REFUSED  the files have {len(blocks)} BLOCK finding(s); run tools/publication_check.py {name} --no-history")
        return False
    if not apply:
        print(f"{name:24} READY    would make `{BRANCH}` with one commit of {len(git(repo, 'ls-files').splitlines())} files (use --apply)")
        return True
    author = check.ALLOWED_AUTHOR
    who, email = author[:-1].split(" <")
    env = {"GIT_AUTHOR_NAME": who, "GIT_AUTHOR_EMAIL": email, "GIT_COMMITTER_NAME": who, "GIT_COMMITTER_EMAIL": email}
    tree = git(repo, "rev-parse", "HEAD^{tree}")
    commit = git(repo, "commit-tree", tree, "-m", MESSAGE, env=env)
    git(repo, "branch", "-f", BRANCH, commit)
    if git(repo, "rev-parse", f"{BRANCH}^{{tree}}") != tree:
        raise RuntimeError(f"{name}: the new branch does not have the tree of HEAD")
    remaining = [f for f in check.check_repo(repo, history=True, ref=BRANCH) if f[0] == "BLOCK"]
    if remaining:
        print(f"{name:24} FAILED   the new branch still has BLOCK findings:")
        for kind, _n, ref, what in remaining[:20]:
            print(f"   {kind} {ref}  {what}")
        return False
    print(f"{name:24} DONE     branch `{BRANCH}` = one commit {commit[:10]}, same files as HEAD, checked clean")
    return True


def main(argv: list[str]) -> int:
    apply = "--apply" in argv
    names = [a for a in argv if not a.startswith("--")]
    repos = sorted(p for p in check.ROOT.glob("ARMOR-*") if (p / ".git").exists()) if "--all" in argv else [check.ROOT / n for n in names]
    if not repos:
        print(__doc__)
        return 2
    ok = all([prepare(repo, apply) for repo in repos])
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
