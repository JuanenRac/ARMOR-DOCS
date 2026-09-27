#!/usr/bin/env python3
# =============================================================================
# ARMOR-DOCS - tools/sync_ci_tools.py
# Copyright (C) 2026 JuanenRac (Electro Hobby 3D)
# GPL-3.0-or-later - see LICENSE
# =============================================================================
"""Vendors ARMOR-COMMON's canonical CI tooling into every other A.R.M.O.R.
repository: `tools/armor_project_tool.py`, `tools/armor_ci_validate.py`,
`tools/_armor_readme_parity.py` and `.github/workflows/ci.yml` (rendered
from `tools/ci.yml.template`). Run this after changing any of those
canonical files in ARMOR-COMMON; it is the same "canonical here, vendored
everywhere" pattern this ecosystem already uses for `make_readmes.py` and
`publication_check.py`'s own rules.

    python tools/sync_ci_tools.py             # writes every vendored copy
    python tools/sync_ci_tools.py --check     # exit 1 if any copy is stale
"""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "ARMOR-COMMON" / "tools"
VENDORED_FILES = ("armor_project_tool.py", "armor_ci_validate.py", "_armor_readme_parity.py")
TARGETS = (
    "ARMOR-SERVER", "ARMOR-STUDIO", "ARMOR-ANDROID-CONTROL", "ARMOR-RADAR", "ARMOR-SOLAR",
    "ARMOR-ELECTRICAL", "ARMOR-HARDWARE", "ARMOR-DEVOPS", "ARMOR-DOCS", "ARMOR-SIMULATOR",
    "ARMOR-SERVER-AI", "ARMOR-VOICE-AI", "ARMOR-NETWORK", "ARMOR-UPDATER",
)


def render_workflow() -> str:
    return (SOURCE / "ci.yml.template").read_text(encoding="utf-8")


def main() -> int:
    check = "--check" in sys.argv
    workflow = render_workflow()
    stale: list[str] = []
    written = 0

    for name in TARGETS:
        repo = ROOT / name
        if not repo.is_dir():
            print(f"SKIP {name}: no local checkout")
            continue
        (repo / "tools").mkdir(exist_ok=True)
        (repo / ".github" / "workflows").mkdir(parents=True, exist_ok=True)

        for filename in VENDORED_FILES:
            source_text = (SOURCE / filename).read_text(encoding="utf-8")
            destination = repo / "tools" / filename
            current = destination.read_text(encoding="utf-8") if destination.is_file() else None
            if current == source_text:
                continue
            if check:
                stale.append(f"{name}/tools/{filename}")
                continue
            destination.write_text(source_text, encoding="utf-8")
            written += 1

        destination = repo / ".github" / "workflows" / "ci.yml"
        current = destination.read_text(encoding="utf-8") if destination.is_file() else None
        if current != workflow:
            if check:
                stale.append(f"{name}/.github/workflows/ci.yml")
            else:
                destination.write_text(workflow, encoding="utf-8")
                written += 1

    if check:
        if stale:
            print("SYNC_CI_TOOLS=STALE " + ", ".join(stale))
            return 1
        print("SYNC_CI_TOOLS=CURRENT")
        return 0

    print(f"SYNC_CI_TOOLS=DONE files_written={written}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
