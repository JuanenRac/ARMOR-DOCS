#!/usr/bin/env python3
"""ARMOR-DOCS - the sentences of the documents that depend on the code, checked against the code.

Copyright (C) 2026 JuanenRac (Electro Hobby 3D). GPL-3.0-or-later.

    python tools/doc_claims.py            # every claim of docs/*.md against the repository it names
    python tools/doc_claims.py --list     # the claims, where each is written and what it looks for
    python tools/doc_claims.py --coverage # the bullets of the security baseline that carry no claim marker (informative)

A sentence that states a fact about the code carries a marker right after it, `<!-- claim: server.max_nodes -->`, and docs/claims.json says where the fact is: the repository, the file and a regular
expression that has to match in it. The check fails when a marker has no entry, an entry has no marker, or the expression no longer matches (the code changed and the sentence did not follow).
A repository that is not next to this one is skipped and said; the nightly job, which has all of them, does not skip.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FAMILY = ROOT.parent
DOCS = ROOT / "docs"
CLAIMS_FILE = DOCS / "claims.json"
MARKER = re.compile(r"<!--\s*claim:\s*([A-Za-z0-9_.\-]+)\s*-->")
SLASH_SUFFIXES = {".ts", ".tsx", ".js", ".mjs", ".cjs", ".jsx", ".c", ".h", ".cc", ".cpp", ".hpp", ".java", ".kt", ".swift", ".go", ".rs"}
HASH_SUFFIXES = {".py", ".sh", ".yml", ".yaml", ".toml", ".cfg", ".ini", ".txt"}


def strip_comments(text: str, suffix: str) -> str:
    """The text without its comments (`//` and `/* */` for C-like files, `#` for scripts); what is inside a string is kept. A suffix that is not known is left as it is."""
    slash = suffix.lower() in SLASH_SUFFIXES
    if not slash and suffix.lower() not in HASH_SUFFIXES:
        return text
    out: list[str] = []
    i, size = 0, len(text)
    while i < size:
        c = text[i]
        if c in "\"'" or (c == "`" and slash):
            j = i + 1
            while j < size and text[j] != c and not (text[j] == "\n" and c != "`"):
                j += 2 if text[j] == "\\" else 1
            out.append(text[i : j + 1])
            i = j + 1
        elif slash and text.startswith("//", i):
            while i < size and text[i] != "\n":
                i += 1
        elif slash and text.startswith("/*", i):
            end = text.find("*/", i + 2)
            i = size if end < 0 else end + 2
            out.append(" ")
        elif not slash and c == "#":
            while i < size and text[i] != "\n":
                i += 1
        else:
            out.append(c)
            i += 1
    return "".join(out)


def written() -> dict[str, list[str]]:
    """Every claim marker of the documents and the files that carry it."""
    found: dict[str, list[str]] = {}
    for path in sorted(DOCS.glob("*.md")):
        for match in MARKER.finditer(path.read_text(encoding="utf-8")):
            found.setdefault(match.group(1), []).append(path.name)
    return found


def check(claims: dict[str, dict[str, str]], marked: dict[str, list[str]], family: Path = FAMILY) -> tuple[list[str], list[str]]:
    """The problems and the skipped claims."""
    problems: list[str] = []
    skipped: list[str] = []
    for name in sorted(set(marked) - set(claims)):
        problems.append(f"{name}: written in {', '.join(marked[name])} but missing from docs/claims.json")
    for name in sorted(set(claims) - set(marked)):
        problems.append(f"{name}: in docs/claims.json but no document carries its marker")
    for name, claim in sorted(claims.items()):
        if name not in marked:
            continue
        for key in ("repo", "file", "pattern"):
            if key not in claim:
                problems.append(f"{name}: the entry has no '{key}'")
                break
        else:
            repo = family / claim["repo"]
            if not repo.is_dir():
                skipped.append(f"{name}: {claim['repo']} is not next to ARMOR-DOCS")
                continue
            target = repo / claim["file"]
            if not target.is_file():
                problems.append(f"{name}: {claim['repo']}/{claim['file']} does not exist")
                continue
            body = target.read_text(encoding="utf-8", errors="replace")
            if claim.get("code_only", True):
                body = strip_comments(body, target.suffix)   # a comment that repeats the words does not back a sentence about the code
            if len(re.findall(claim["pattern"], body)) < int(claim.get("min_matches", 1)):
                problems.append(f"{name}: {claim['repo']}/{claim['file']} no longer matches /{claim['pattern']}/ ({claim.get('says', 'the sentence')})")
    return problems, skipped


BASELINE_HEADINGS = ("what the software already enforces", "application-level findings fixed")


def unmarked_bullets(text: str) -> tuple[int, list[str]]:
    """The bullets of the sections of the baseline that state what the software enforces, and those among them that carry no claim marker."""
    total, bare = 0, []
    inside = False
    for line in text.splitlines():
        if line.startswith("#"):
            inside = any(h in line.lower() for h in BASELINE_HEADINGS)
        elif inside and re.match(r"\s*[-*] ", line):
            total += 1
            if not MARKER.search(line):
                bare.append(line.strip()[:100])
    return total, bare


def coverage(docs: Path = DOCS) -> tuple[int, int]:
    """(bullets, bullets without a marker) of docs/SECURITY_BASELINE.md."""
    path = docs / "SECURITY_BASELINE.md"
    if not path.is_file():
        return 0, 0
    total, bare = unmarked_bullets(path.read_text(encoding="utf-8"))
    return total, len(bare)


def main(argv: list[str]) -> int:
    claims = json.loads(CLAIMS_FILE.read_text(encoding="utf-8"))
    marked = written()
    if "--list" in argv:
        for name, claim in sorted(claims.items()):
            print(f"{name:34} {', '.join(marked.get(name, ['(no marker)'])):28} {claim['repo']}/{claim['file']}")
        return 0
    if "--coverage" in argv:
        total, bare = coverage()
        print(f"CLAIM_COVERAGE bullets={total} without_marker={bare}")
        return 0
    problems, skipped = check(claims, marked)
    for item in skipped:
        print("SKIP", item)
    for item in problems:
        print("FAIL", item)
    print(f"DOC_CLAIMS={'FAIL' if problems else 'PASS'} ({len(claims) - len(skipped)} checked, {len(skipped)} skipped)")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
