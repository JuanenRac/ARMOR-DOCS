#!/usr/bin/env python3
"""ARMOR-DOCS - the figures of the documents, read from the repositories instead of typed.

Copyright (C) 2026 JuanenRac (Electro Hobby 3D). GPL-3.0-or-later.

    python tools/doc_facts.py            # rewrite every marked figure of docs/*.md
    python tools/doc_facts.py --check    # fail when one is out of date (a figure whose source is not next to this repository is skipped, and said)
    python tools/doc_facts.py --list     # print every figure and its value
    python tools/doc_facts.py --stale    # the rows verified in a version older than the one the repository has now
    python tools/doc_facts.py --structure  # the figures typed in the docs/structure.json of the repositories (tests, test modules, JSON Schemas, conformance payloads) against the real ones (--check does it too)

A figure in a document is written between two markers, which stay invisible when the page is rendered:

    <!--fact:vectors-->1334<!--/fact--> conformance vectors

The name says where the number comes from:

    vectors              every conformance vector of ARMOR-COMMON         vectors:network   the vectors of one schema (conformance/network.json); vectors:a+b adds those of several
    schemas              the JSON Schemas of ARMOR-COMMON                 openapi_paths     the paths of the OpenAPI file of the server
    openapi_operations   the operations (method and path) of that file
    conformance_files    the conformance files of ARMOR-COMMON (one per message)
    security_settings    the settings of the security file of ARMOR-SERVER (the keys of SECURITY_DEFAULTS in src/security_settings.ts)
    studio_security_options  the options the security screen of ARMOR-STUDIO offers (the entries of OPTIONS in src/SecurityPanel.tsx)
    tests:ARMOR-X        the test functions (`def test_`) of the Python tests of a repository (the count `python -m unittest discover` prints); ARMOR-DEVOPS keeps them in scripts/test_*.py
    unittest:ARMOR-X     the same figure under the name of the runner
    ctest_cpp:ARMOR-X    the host test programs a node registers with CTest (`add_test` in tests/CMakeLists.txt, each name once, without the Python checks)
    ctest_python:ARMOR-X the Python checks that file registers with CTest
    version:ARMOR-X      the version in the manifest of a repository

A row of the capability matrix says in which version it was verified with `<!--verified:ARMOR-NODE-RADAR 0.8.0.1-->` after its evidence. `--check` fails when that version is newer than the one the
repository has now (a typo or a row ahead of its repository), and `--stale` lists the rows whose repository has moved on since, so that a later change that could invalidate them is not forgotten.

The numbers are read from what is committed in the repository (git HEAD), the same state the CI of this repository fetches, so a file another person is editing and has not
committed yet does not move a document; ARMOR_FACTS_SOURCE=worktree reads the working tree instead.
"""
from __future__ import annotations

import json
import os
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FAMILY = ROOT.parent
DOCS = ROOT / "docs"
VERIFIED = re.compile(r"<!--verified:(ARMOR-[A-Z0-9-]+) (\d+(?:\.\d+){1,3})-->")
TESTS_NEXT_TO_SCRIPTS = {"ARMOR-DEVOPS"}
MARKER = re.compile(r"<!--fact:([A-Za-z0-9_:.\-]+)-->(.*?)<!--/fact-->", re.S)


class Unavailable(Exception):
    """The repository a figure is read from is not next to this one."""


def _repo(name: str) -> Path:
    path = FAMILY / name
    if not (path / "armor.project.json").exists():
        raise Unavailable(f"{name} is not next to ARMOR-DOCS")
    return path


def _worktree() -> bool:
    return os.environ.get("ARMOR_FACTS_SOURCE", "").lower() == "worktree"


def _tracked(repo: Path, folder: str, suffix: str) -> dict[str, str]:
    """The text of every file of `folder` with `suffix`, as committed (or as in the working tree when asked)."""
    files: dict[str, str] = {}
    if not _worktree() and (repo / ".git").exists():
        listing = subprocess.run(["git", "-C", str(repo), "ls-tree", "--name-only", "HEAD", folder.rstrip("/") + "/"], capture_output=True, text=True, encoding="utf-8")
        if listing.returncode == 0 and listing.stdout.strip():
            for name in listing.stdout.split("\n"):
                if name.endswith(suffix):
                    shown = subprocess.run(["git", "-C", str(repo), "show", f"HEAD:{name}"], capture_output=True, text=True, encoding="utf-8")
                    if shown.returncode == 0:
                        files[Path(name).name] = shown.stdout
            if files:
                return files
    for path in sorted((repo / folder).glob("*" + suffix)):
        files[path.name] = path.read_text(encoding="utf-8")
    return files


def vectors(kind: str | None = None) -> int:
    files = _tracked(_repo("ARMOR-COMMON"), "conformance", ".json")
    if kind:
        if f"{kind}.json" not in files:
            raise KeyError(f"no conformance file {kind}.json")
        files = {f"{kind}.json": files[f"{kind}.json"]}
    return sum(len(json.loads(text)["vectors"]) for text in files.values())


def schemas() -> int:
    return len(_tracked(_repo("ARMOR-COMMON"), "src/armor_common/schemas", ".schema.json"))


def conformance_files() -> int:
    return len(_tracked(_repo("ARMOR-COMMON"), "conformance", ".json"))


def _entries(repository: str, folder: str, suffix: str, name: str, start: str, end: str, entry: str) -> int:
    """How many lines matching `entry` sit between the line that matches `start` and the first line that matches `end` after it."""
    text = _tracked(_repo(repository), folder, suffix).get(name)
    if text is None:
        raise Unavailable(f"{repository} has no {folder}/{name}")
    begin = re.search(start, text, re.M)
    if begin is None:
        raise Unavailable(f"{folder}/{name} of {repository} has no block that starts with {start!r}")
    block = text[begin.end():]
    close = re.search(end, block, re.M)
    if close is None:
        raise Unavailable(f"the block of {folder}/{name} of {repository} does not end")
    return len(re.findall(entry, block[: close.start()], re.M))


def security_settings() -> int:
    return _entries("ARMOR-SERVER", "src", ".ts", "security_settings.ts", r"^export const SECURITY_DEFAULTS\b.*$", r"^\}\)", r'^\s+"[A-Za-z0-9_.]+":')


def studio_security_options() -> int:
    return _entries("ARMOR-STUDIO", "src", ".tsx", "SecurityPanel.tsx", r"^const OPTIONS\b.*$", r"^\];", r'^\s+\{ key: "[A-Za-z0-9_.]+"')


def openapi_paths() -> int:
    text = _tracked(_repo("ARMOR-COMMON"), "openapi", ".yaml").get("armor-server.yaml")
    if text is None:
        raise Unavailable("openapi/armor-server.yaml is missing")
    section = text.split("\npaths:", 1)[1]
    following = re.search(r"\n[A-Za-z]\w*:", section)
    section = section[: following.start()] if following else section
    return len(re.findall(r"^  /", section, re.M))


def openapi_operations() -> int:
    text = _tracked(_repo("ARMOR-COMMON"), "openapi", ".yaml").get("armor-server.yaml")
    if text is None:
        raise Unavailable("openapi/armor-server.yaml is missing")
    section = text.split("\npaths:", 1)[1]
    following = re.search(r"\n[A-Za-z]\w*:", section)
    section = section[: following.start()] if following else section
    return len(re.findall(r"^    (?:get|put|post|delete|patch):", section, re.M))


def tests(repository: str) -> int:
    """The test functions of a Python repository: every `def test_` of the files under tests/ as committed (ARMOR-DEVOPS keeps its tests next to its scripts: the scripts/test_*.py files)."""
    if repository in TESTS_NEXT_TO_SCRIPTS:
        files = {name: text for name, text in _tracked(_repo(repository), "scripts", ".py").items() if name.startswith("test_")}
    else:
        files = _tracked(_repo(repository), "tests", ".py")
    if not files:
        raise Unavailable(f"{repository} has no Python tests")
    return sum(len(re.findall(r"^\s*(?:async )?def test_", text, re.M)) for text in files.values())


def _ctest(repository: str, python: bool) -> int:
    """The tests registered with CTest in tests/CMakeLists.txt, by name: the two branches of an if/else that register the same test count once."""
    text = _tracked(_repo(repository), "tests", ".txt").get("CMakeLists.txt")
    if text is None:
        raise Unavailable(f"{repository} has no tests/CMakeLists.txt")
    names: dict[str, bool] = {}
    for match in re.finditer(r"^\s*add_test\(\s*NAME\s+(\S+)\s+COMMAND\s+([^\n]*)$", text, re.M):
        names.setdefault(match.group(1), "Python3_EXECUTABLE" in match.group(2))
    return sum(1 for is_python in names.values() if is_python == python)


def version(repository: str) -> str:
    return str(json.loads((_repo(repository) / "armor.project.json").read_text(encoding="utf-8"))["version"])


def value(name: str) -> str:
    """The value of the figure `name`; raises Unavailable when its source is not there and KeyError for a name that means nothing."""
    base, _, argument = name.partition(":")
    if base == "vectors":
        return str(sum(vectors(part) for part in argument.split("+")) if argument else vectors())
    if base == "schemas" and not argument:
        return str(schemas())
    if base == "conformance_files" and not argument:
        return str(conformance_files())
    if base == "security_settings" and not argument:
        return str(security_settings())
    if base == "studio_security_options" and not argument:
        return str(studio_security_options())
    if base == "openapi_paths" and not argument:
        return str(openapi_paths())
    if base == "openapi_operations" and not argument:
        return str(openapi_operations())
    if base in ("tests", "unittest") and argument:
        return str(tests(argument))
    if base in ("ctest_cpp", "ctest_python") and argument:
        return str(_ctest(argument, base == "ctest_python"))
    if base == "version" and argument:
        return version(argument)
    raise KeyError(name)


STRUCTURE_RULES = (
    # (name of the entry, what its English text must start with, the figure it states, how to read it)
    ("tests/", re.compile(r"^(\d+) tests?\b"), "tests"),
    ("tests/", re.compile(r"\bin (\d+) modules?\b"), "test modules"),
    ("schemas/", re.compile(r"^(\d+) JSON Schemas?\b"), "schemas"),
    ("conformance/", re.compile(r"^(\d+) accepted and rejected payloads\b"), "vectors"),
)


def test_modules(repository: str) -> int:
    """The test files of a Python repository (tests/test_*.py as committed)."""
    files = [name for name in _tracked(_repo(repository), "tests", ".py") if name.startswith("test_")]
    if not files:
        raise Unavailable(f"{repository} has no Python tests")
    return len(files)


def _structure_entries(node: object):
    """Every entry (a dict with a plain `name` and a `desc` per language) of a structure.json, at any depth."""
    if isinstance(node, dict):
        if isinstance(node.get("name"), str) and isinstance(node.get("desc"), dict):
            yield node
        for child in node.values():
            yield from _structure_entries(child)
    elif isinstance(node, list):
        for child in node:
            yield from _structure_entries(child)


def structure_problems(repositories: list[str] | None = None) -> list[str]:
    """The figures typed in docs/structure.json (tests, test modules, JSON Schemas, payloads) that are not the real ones, and the languages whose text does not carry the same figure
    as the English one. A repository whose figure cannot be read here (its tests are not Python, or it is not next to this one) is skipped."""
    names = repositories if repositories is not None else sorted(path.name for path in FAMILY.glob("ARMOR-*") if (path / "armor.project.json").exists())
    problems: list[str] = []
    for repository in names:
        try:
            text = _tracked(_repo(repository), "docs", ".json").get("structure.json")
        except Unavailable:
            continue
        if text is None:
            continue
        for entry in _structure_entries(json.loads(text)):
            english = entry["desc"].get("en", "")
            for name, pattern, figure in STRUCTURE_RULES:
                match = pattern.search(english) if entry["name"] == name else None
                if match is None:
                    continue
                try:
                    if figure == "tests":
                        real = tests(repository)
                    elif figure == "test modules":
                        real = test_modules(repository)
                    elif figure == "schemas":
                        real = schemas()
                    else:
                        real = vectors()
                except Unavailable:
                    continue
                if int(match.group(1)) != real:
                    problems.append(f"{repository}: docs/structure.json says {match.group(1)} {figure} in {entry['name']} but the repository has {real}")
                for language, words in entry["desc"].items():
                    if match.group(1) not in re.findall(r"\d+", str(words)):
                        problems.append(f"{repository}: docs/structure.json {entry['name']} does not carry the figure {match.group(1)} in {language}")
    return problems


def render(text: str) -> tuple[str, list[str], list[str]]:
    """The text with every figure brought up to date, the figures that changed and the ones that could not be read."""
    changed: list[str] = []
    skipped: list[str] = []

    def replace(match: re.Match[str]) -> str:
        name = match.group(1)
        try:
            current = value(name)
        except Unavailable as problem:
            skipped.append(f"{name} ({problem})")
            return match.group(0)
        if match.group(2) != current:
            changed.append(f"{name}: {match.group(2)} -> {current}")
        return f"<!--fact:{name}-->{current}<!--/fact-->"

    return MARKER.sub(replace, text), changed, skipped


def _parts(text: str) -> tuple[int, ...]:
    return tuple(int(piece) for piece in text.split("."))


def verified(text: str) -> list[tuple[str, str, str | None]]:
    """The `verified` markers of a text as (repository, version verified, version now); the last is None when the repository is not next to this one."""
    found = []
    for match in VERIFIED.finditer(text):
        try:
            current: str | None = version(match.group(1))
        except Unavailable:
            current = None
        found.append((match.group(1), match.group(2), current))
    return found


def verified_problems(text: str) -> list[str]:
    return [f"{repo} {then} is newer than the version of the repository ({now})" for repo, then, now in verified(text) if now and _parts(then) > _parts(now)]


def documents() -> list[Path]:
    return sorted(DOCS.glob("*.md"))


def main(argv: list[str]) -> int:
    check = "--check" in argv
    if "--stale" in argv:
        for path in documents():
            for repo, then, now in verified(path.read_text(encoding="utf-8")):
                if now and _parts(then) < _parts(now):
                    print(f"{path.name}: verified in {repo} {then}, now {now}")
        return 0
    if "--list" in argv:
        names = sorted({m.group(1) for path in documents() for m in MARKER.finditer(path.read_text(encoding="utf-8"))})
        for name in names:
            try:
                print(f"{name:32} {value(name)}")
            except Unavailable as problem:
                print(f"{name:32} unavailable ({problem})")
        return 0
    if "--structure" in argv:
        found = structure_problems()
        for item in found:
            print("FAIL " + item)
        print("STRUCTURE_FIGURES=" + ("FAIL" if found else "CURRENT"))
        return 1 if found else 0
    failed = False
    if check:
        for item in structure_problems():
            print("FAIL " + item)
            failed = True
    for path in documents():
        with open(path, encoding="utf-8", newline="") as handle:
            text = handle.read()
        try:
            new, changed, skipped = render(text)
        except KeyError as unknown:
            print(f"FAIL {path.name}: the figure {unknown} means nothing")
            failed = True
            continue
        for item in verified_problems(text):
            print(f"FAIL {path.name}: {item}")
            failed = True
        for item in skipped:
            print(f"SKIP {path.name}: {item}")
        if not changed:
            continue
        for item in changed:
            print(f"{'FAIL' if check else 'FIX '} {path.name}: {item}")
        if check:
            failed = True
        else:
            with open(path, "w", encoding="utf-8", newline="") as handle:
                handle.write(new)
    if check:
        print("DOC_FACTS=" + ("FAIL" if failed else "CURRENT"))
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
