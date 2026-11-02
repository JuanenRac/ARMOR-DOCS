#!/usr/bin/env python3
"""ARMOR-DOCS - the tables and the Mermaid diagrams of the Markdown files, checked without a browser.

Copyright (C) 2026 JuanenRac (Electro Hobby 3D). GPL-3.0-or-later.

    python tools/doc_markdown.py               # docs/*.md of this repository
    python tools/doc_markdown.py --all         # also the READMEs of every ARMOR-* repository next to this one
    python tools/doc_markdown.py file.md ...   # the files named

A table fails when a row has another number of cells than its header (a pipe inside a cell has to be written \| or inside backticks is still a cell separator on GitHub, so it is counted).
A Mermaid block fails when it does not start with a known diagram type, when `subgraph` and `end` do not pair, when a bracket or a quote is left open on a line, or when it is empty.
It is a parser for the mistakes that happen, not a renderer: a diagram that passes can still be drawn badly.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FAMILY = ROOT.parent
DIAGRAMS = {"flowchart", "graph", "sequenceDiagram", "classDiagram", "stateDiagram", "stateDiagram-v2", "erDiagram", "gantt", "pie", "journey", "gitGraph", "mindmap", "timeline", "quadrantChart", "block-beta"}
SEPARATOR = re.compile(r"^\s*\|?\s*:?-{1,}:?\s*(\|\s*:?-{1,}:?\s*)*\|?\s*$")
OPEN, CLOSE = "[({", "])}"


def cells(line: str) -> int:
    text = line.strip().replace("\|", "\0")
    if text.startswith("|"):
        text = text[1:]
    if text.endswith("|"):
        text = text[:-1]
    return text.count("|") + 1


def check_tables(lines: list[str], fenced: set[int]) -> list[str]:
    problems: list[str] = []
    index = 0
    while index < len(lines):
        if index in fenced or not lines[index].lstrip().startswith("|"):
            index += 1
            continue
        start = index
        while index < len(lines) and index not in fenced and lines[index].lstrip().startswith("|"):
            index += 1
        block = lines[start:index]
        if len(block) < 2 or not SEPARATOR.match(block[1]):
            continue   # a run of lines that starts with a pipe is not a table without its separator row
        expected = cells(block[0])
        if cells(block[1]) != expected:
            problems.append(f"line {start + 2}: the separator row has {cells(block[1])} cells and the header {expected}")
        for offset, row in enumerate(block[2:], start + 3):
            if cells(row) != expected:
                problems.append(f"line {offset}: a row of {cells(row)} cells in a table of {expected}")
    return problems


def check_mermaid(body: list[str], first: int) -> list[str]:
    content = [line for line in body if line.strip() and not line.strip().startswith("%%")]
    if not content:
        return [f"line {first}: an empty Mermaid block"]
    kind = content[0].strip().split()[0]
    problems: list[str] = []
    if kind not in DIAGRAMS:
        problems.append(f"line {first}: '{kind}' is not a Mermaid diagram type")
    depth = 0
    for number, line in enumerate(body, first + 1):
        text = line.strip()
        if text.startswith("%%"):
            continue
        if re.match(r"^subgraph\b", text):
            depth += 1
        elif text == "end":
            depth -= 1
            if depth < 0:
                problems.append(f"line {number}: 'end' without 'subgraph'")
                depth = 0
        if text.count('"') % 2:
            problems.append(f"line {number}: a quote is left open")
            continue
        stripped = re.sub(r'"[^"]*"', "", text)
        stack: list[str] = []
        for char in stripped:
            if char in OPEN:
                stack.append(char)
            elif char in CLOSE:
                if not stack or OPEN.index(stack.pop()) != CLOSE.index(char):
                    problems.append(f"line {number}: a closing '{char}' that does not match")
                    stack = []
                    break
        else:
            if stack and kind in {"flowchart", "graph"}:
                problems.append(f"line {number}: a '{stack[-1]}' is left open")
    if depth > 0 and kind in {"flowchart", "graph"}:
        problems.append(f"line {first}: {depth} 'subgraph' without 'end'")
    return problems


def check_text(text: str) -> list[str]:
    lines = text.splitlines()
    fenced: set[int] = set()
    problems: list[str] = []
    index = 0
    while index < len(lines):
        match = re.match(r"^(\s*)(`{3,}|~{3,})\s*([\w-]*)", lines[index])
        if not match:
            index += 1
            continue
        fence, language, start = match.group(2), match.group(3), index
        index += 1
        while index < len(lines) and not re.match(rf"^\s*{re.escape(fence[0])}{{{len(fence)},}}\s*$", lines[index]):
            index += 1
        if index >= len(lines):
            problems.append(f"line {start + 1}: a code block is never closed")
        fenced.update(range(start, min(index + 1, len(lines))))
        if language == "mermaid":
            problems.extend(check_mermaid(lines[start + 1:index], start + 1))
        index += 1
    return problems + check_tables(lines, fenced)


def files(argv: list[str]) -> list[Path]:
    named = [Path(a) for a in argv if not a.startswith("--")]
    if named:
        return named
    found = sorted((ROOT / "docs").glob("*.md"))
    if "--all" in argv:
        for repo in sorted(FAMILY.glob("ARMOR-*")):
            found += sorted(repo.glob("README*.md"))
    return found


def main(argv: list[str]) -> int:
    failed = 0
    count = 0
    for path in files(argv):
        count += 1
        for problem in check_text(path.read_text(encoding="utf-8")):
            failed += 1
            print(f"FAIL {path.parent.name}/{path.name}: {problem}")
    print(f"DOC_MARKDOWN={'FAIL' if failed else 'PASS'} ({count} files)")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
