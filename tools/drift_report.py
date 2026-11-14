#!/usr/bin/env python3
"""ARMOR-DOCS - the drift report: what the nightly family check found, as one small document a dashboard can show.

Copyright (C) 2026 JuanenRac (Electro Hobby 3D). GPL-3.0-or-later.

    python tools/drift_report.py                       # run the checks of the nightly run (every repository next to this one), print the table as Markdown, write drift.json
    python tools/drift_report.py --out FILE            # write the report somewhere else

The checks are the generated documents compared with their sources and the files copied into every repository (the same list the nightly workflow runs). A check whose script is not
there is reported as `skip`, never as `pass`. The report holds only the name and the result of each check (`pass`, `fail`, `skip`) and the counts, so that it can be sent to a dashboard
without a line of output; the last lines of a failing check stay in the log of the run, not in the report. The exit status is 1 when a check failed.
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from collections.abc import Callable
from pathlib import Path

HERE = Path(__file__).resolve().parent
DOCS_ROOT = HERE.parent
SCHEMA_VERSION = 1
#: (name, script relative to this repository, arguments). The same checks as the nightly workflow runs against the family.
CHECKS: tuple[tuple[str, str, tuple[str, ...]], ...] = (
    ("readmes", "tools/make_readmes.py", ("--check",)),
    ("banners", "tools/make_brand.py", ("--check",)),
    ("catalogue", "tools/make_catalog.py", ("--check",)),
    ("shared tools", "tools/sync_ci_tools.py", ("--check",)),
    ("figures", "tools/doc_facts.py", ("--check",)),
    ("claims", "tools/doc_claims.py", ()),
    ("markdown", "tools/doc_markdown.py", ("--all",)),
    ("firmware base", "../ARMOR-COMMON/tools/sync_firmware_base.py", ("check",)),
    ("generated types", "../ARMOR-COMMON/tools/generate_types.py", ("--check",)),
    ("conformance vectors", "../ARMOR-COMMON/tools/make_conformance.py", ("--check",)),
)

Runner = Callable[[list[str], Path], int]


def _run(command: list[str], cwd: Path) -> int:
    try:
        return subprocess.run(command, cwd=cwd, capture_output=True, text=True, timeout=600).returncode
    except (OSError, subprocess.TimeoutExpired):
        return 1


def run_checks(root: Path = DOCS_ROOT, runner: Runner = _run) -> dict:
    results = []
    for name, script, arguments in CHECKS:
        path = (root / script).resolve()
        if not path.is_file():
            results.append({"name": name, "result": "skip"})
            continue
        code = runner([sys.executable, str(path), *arguments], root)
        results.append({"name": name, "result": "pass" if code == 0 else "fail"})
    return {"schema_version": SCHEMA_VERSION, "total": len(results), "failed": sum(1 for r in results if r["result"] == "fail"),
            "skipped": sum(1 for r in results if r["result"] == "skip"), "checks": results}


def render_markdown(report: dict) -> str:
    lines = ["| Check | Result |", "|---|---|"] + [f"| {item['name']} | {item['result']} |" for item in report["checks"]]
    lines.append("")
    lines.append(f"{report['failed']} of {report['total']} checks failed, {report['skipped']} skipped.")
    return "\n".join(lines) + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Run the checks of the nightly family run and write the drift report.")
    parser.add_argument("--out", type=Path, default=DOCS_ROOT / "drift.json")
    args = parser.parse_args(argv)
    report = run_checks()
    args.out.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8", newline="\n")
    sys.stdout.write(render_markdown(report))
    print(f"DRIFT={'FAIL' if report['failed'] else 'PASS'} failed={report['failed']} total={report['total']}")
    return 1 if report["failed"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
