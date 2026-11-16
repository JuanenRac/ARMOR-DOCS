#!/usr/bin/env python3
"""Write docs/ecosystem.lock.json and docs/COMPATIBILITY.md: the version of every repository of the family next to the version of the contracts it was last checked against.

The versions come from the manifests of the repositories and the pins of ARMOR-COMMON (registry/contract_pins.json). The files are written when a version of the family is
prepared: they are a photograph of that train, and any repository may move on after that. `--check` says how far each one has moved (it never fails unless `--strict` is given).

Copyright (C) 2026 JuanenRac (Electro Hobby 3D). GPL-3.0-or-later.

    python tools/make_compatibility.py               write the two files for the current train
    python tools/make_compatibility.py --new-train   start the next train (eco-2 after eco-1, and so on) and write the files
    python tools/make_compatibility.py --check       list the repositories whose version is not the one of the train (exit 0); --strict exits 1 instead

The family is released in trains named `eco-N`, with N counting up one by one (docs/release_train.json); a train has no date in its name.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
DOCS = HERE.parent / "docs"
sys.path.insert(0, str(HERE))
from make_readmes import ORDER  # noqa: E402


TRAIN_FILE = DOCS / "release_train.json"


def train_name(number: int) -> str:
    """The name of a train of the family: `eco-` and a number that only goes up, one by one. It carries no date."""
    return f"eco-{number}"


def current_train(file: Path = TRAIN_FILE) -> int:
    return int(json.loads(file.read_text(encoding="utf-8"))["current"]) if file.is_file() else 1


def next_train(file: Path = TRAIN_FILE) -> int:
    """Start the next train: the number goes up by one (the one thing this does besides reading the file)."""
    number = current_train(file) + 1
    file.write_text(json.dumps({"schema_version": "1.0", "current": number}, indent=2) + "\n", encoding="utf-8", newline="\n")
    return number


def collect(root: Path, train: int = 1) -> dict:
    common = json.loads((root / "ARMOR-COMMON" / "armor.project.json").read_text(encoding="utf-8"))["version"]
    pins_file = root / "ARMOR-COMMON" / "registry" / "contract_pins.json"
    pins = json.loads(pins_file.read_text(encoding="utf-8"))["consumers"] if pins_file.is_file() else {}
    repositories = {}
    for name in ORDER:
        version = json.loads((root / name / "armor.project.json").read_text(encoding="utf-8"))["version"]
        repositories[name] = {"version": version, "contracts": pins.get(name)}
    return {"schema_version": "1.0", "train": train_name(train), "contracts_version": common, "repositories": repositories}


def moved_on(written: dict, now: dict) -> list[str]:
    """One line for every repository whose version, or the version of the contracts, is no longer the one written in the lock of the train."""
    lines = []
    if written.get("contracts_version") != now.get("contracts_version"):
        lines.append(f"contracts: {written.get('contracts_version')} in the lock, {now.get('contracts_version')} now")
    before = written.get("repositories", {})
    for name, entry in now.get("repositories", {}).items():
        if name not in before:
            lines.append(f"{name}: not in the lock")
        elif before[name].get("version") != entry["version"]:
            lines.append(f"{name}: {before[name].get('version')} in the lock, {entry['version']} now")
    for name in before:
        if name not in now.get("repositories", {}):
            lines.append(f"{name}: in the lock but not in the family")
    return lines


def lock_text(data: dict) -> str:
    return json.dumps(data, indent=2) + "\n"


def markdown(data: dict) -> str:
    rows = ["| Repository | Version | Contracts it was checked against |", "|---|---|---|"]
    for name, entry in data["repositories"].items():
        pin = entry["contracts"] or "-"
        mark = "" if pin in ("-", data["contracts_version"]) else " (behind)"
        rows.append(f"| {name} | {entry['version']} | {pin}{mark} |")
    return (
        "# Compatibility of the family\n\n"
        + (f"Release train: **{data['train']}** (a number that only goes up, one by one; `python tools/make_compatibility.py --new-train` starts the next one).\n\n" if data.get("train") else "")
        + f"Version of the contracts (ARMOR-COMMON) when the train was prepared: **{data['contracts_version']}**.\n\n"
        "This table is a photograph of the train, not of today: the versions are those of the repositories when it was prepared, and `python tools/make_compatibility.py --check` "
        "lists the ones that have moved on since. A repository is listed with its own version and the version of the contracts it was last checked against by the reverse-dependency "
        "run of ARMOR-COMMON. A pin below the version of the contracts is marked `(behind)`: that repository had not been checked against those contracts yet. "
        "`docs/ecosystem.lock.json` carries the same table for tools. Both are written by `tools/make_compatibility.py` when a version of the family is prepared.\n\n" + "\n".join(rows) + "\n"
    )


def main(argv: list[str] | None = None) -> int:
    args = argv if argv is not None else sys.argv[1:]
    if "--check" in args:
        lock_file = DOCS / "ecosystem.lock.json"
        if not lock_file.is_file():
            print("COMPATIBILITY=SKIP there is no docs/ecosystem.lock.json")
            return 0
        if not (ROOT / "ARMOR-COMMON" / "armor.project.json").is_file():
            print(f"COMPATIBILITY=SKIP the repositories of the family are not next to this one ({ROOT})")
            return 0
        written = json.loads(lock_file.read_text(encoding="utf-8"))
        lines = moved_on(written, collect(ROOT, current_train()))
        for line in lines:
            print("MOVED", line)
        print(f"COMPATIBILITY={'MOVED' if lines else 'PASS'} {len(lines)} difference(s) from the train {written.get('train')}")
        return 1 if lines and "--strict" in args else 0
    if "--new-train" in args:
        next_train()
    data = collect(ROOT, current_train())
    (DOCS / "ecosystem.lock.json").write_text(lock_text(data), encoding="utf-8", newline="\n")
    (DOCS / "COMPATIBILITY.md").write_text(markdown(data), encoding="utf-8", newline="\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
