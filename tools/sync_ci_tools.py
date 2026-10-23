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
    "ARMOR-SERVER", "ARMOR-STUDIO", "ARMOR-ANDROID-CONTROL", "ARMOR-IOS-CONTROL", "ARMOR-NODE-RADAR", "ARMOR-NODE-SOLAR",
    "ARMOR-NODE-ELECTRICAL", "ARMOR-NODE-ALARM", "ARMOR-NODE-HMI", "ARMOR-HARDWARE", "ARMOR-DEVOPS", "ARMOR-DOCS", "ARMOR-SIMULATOR",
    "ARMOR-SERVER-AI", "ARMOR-VOICE-AI", "ARMOR-NETWORK", "ARMOR-UPDATER", "ARMOR-VISION",
)


# The workflow that tries Studio and the server together (nginx of the image, a real server, a real browser): the two repositories whose change can break the other carry it.
E2E_TARGETS = ("ARMOR-STUDIO", "ARMOR-SERVER")


def render_workflow() -> str:
    return (SOURCE / "ci.yml.template").read_text(encoding="utf-8")


def render_e2e_workflow() -> str:
    return (SOURCE / "e2e.yml.template").read_text(encoding="utf-8")


def main() -> int:
    check = "--check" in sys.argv
    workflow = render_workflow()
    stale: list[str] = []
    written = 0

    # ARMOR-COMMON is the canonical source of the vendored files below - it
    # never vendors a copy of its own tools/ onto itself - but it still
    # needs the workflow file to actually run CI, the same as everywhere
    # else. Found for real: this was missing outright (no
    # .github/workflows/ directory at all), so ARMOR-COMMON's own CI never
    # ran once - `gh api repos/.../actions/workflows` showed zero
    # registered workflows.
    workflow_only_targets = ("ARMOR-COMMON",)

    for name in workflow_only_targets:
        repo = ROOT / name
        if not repo.is_dir():
            print(f"SKIP {name}: no local checkout")
            continue
        if not check:
            (repo / ".github" / "workflows").mkdir(parents=True, exist_ok=True)
        destination = repo / ".github" / "workflows" / "ci.yml"
        current = destination.read_text(encoding="utf-8") if destination.is_file() else None
        if current != workflow:
            if check:
                stale.append(f"{name}/.github/workflows/ci.yml")
            else:
                destination.write_text(workflow, encoding="utf-8")
                written += 1

    for name in TARGETS:
        repo = ROOT / name
        if not repo.is_dir():
            print(f"SKIP {name}: no local checkout")
            continue
        if not check:   # a check reads and never creates
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

    e2e_workflow = render_e2e_workflow()
    for name in E2E_TARGETS:
        repo = ROOT / name
        if not repo.is_dir():
            print(f"SKIP {name}: no local checkout")
            continue
        destination = repo / ".github" / "workflows" / "e2e.yml"
        current = destination.read_text(encoding="utf-8") if destination.is_file() else None
        if current is not None:
            current = current.replace("\r\n", "\n")
        if current != e2e_workflow:
            if check:
                stale.append(f"{name}/.github/workflows/e2e.yml")
            else:
                (repo / ".github" / "workflows").mkdir(parents=True, exist_ok=True)
                destination.write_text(e2e_workflow, encoding="utf-8", newline="\n")
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
