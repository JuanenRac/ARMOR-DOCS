#!/usr/bin/env python3
"""Write the table of docs/PROJECT_CATALOG.md from the manifests of the repositories, so that no version or maturity in it can be behind its project.

Copyright (C) 2026 JuanenRac (Electro Hobby 3D). GPL-3.0-or-later.

    python tools/make_catalog.py          # write the table
    python tools/make_catalog.py --check  # fail when the table is out of date
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CATALOG = Path(__file__).resolve().parents[1] / "docs" / "PROJECT_CATALOG.md"
sys.path.insert(0, str(Path(__file__).resolve().parent))
from make_readmes import ORDER  # noqa: E402

BEGIN, END = "<!-- catalog:begin -->", "<!-- catalog:end -->"
MATURITY = {"scaffolding": "Scaffolding", "functional": "Functional", "established": "Established"}


def table() -> str:
    rows = ["| Repository | Version | Responsibility | Maturity |", "|---|---|---|---|"]
    for name in ORDER:
        info = json.loads((ROOT / name / "armor.project.json").read_text(encoding="utf-8"))
        rows.append(f"| {name} | {info['version']} | {info['role']} | {MATURITY[info['maturity']]} |")
    return "\n".join(rows)


def render(current: str) -> str:
    if BEGIN in current and END in current:
        head, rest = current.split(BEGIN, 1)
        _, tail = rest.split(END, 1)
        return f"{head}{BEGIN}\n{table()}\n{END}{tail}"
    # first run: the old hand-written table is replaced
    start = current.index("| Repository |")
    end = current.index("\n\n", start)
    return f"{current[:start]}{BEGIN}\n{table()}\n{END}{current[end:]}"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    current = CATALOG.read_text(encoding="utf-8").replace("\r\n", "\n")
    new = render(current)
    if new == current:
        print("catalogue current")
        return 0
    if args.check:
        print("docs/PROJECT_CATALOG.md is out of date: run tools/make_catalog.py", file=sys.stderr)
        return 1
    CATALOG.write_text(new, encoding="utf-8", newline="\n")
    print("catalogue written")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
