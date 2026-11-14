#!/usr/bin/env python3
"""ARMOR-DOCS - the routes and topics named in docs/SEQUENCES.md exist in the contracts.

Copyright (C) 2026 JuanenRac (Electro Hobby 3D). GPL-3.0-or-later.

    python tools/check_sequences.py            # compare with the OpenAPI and AsyncAPI files of the ARMOR-COMMON next to this repository
    python tools/check_sequences.py --common DIR

Every `/api/v1/...` path in the page must be a path of the OpenAPI file and every `armor/...` topic must be the address of a channel of the AsyncAPI document (the names between
braces stand for any value). Without ARMOR-COMMON next to this repository the check says so and exits 0 (the nightly run has it).
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

DOCS_ROOT = Path(__file__).resolve().parents[1]
PAGE = DOCS_ROOT / "docs" / "SEQUENCES.md"
ROUTE = re.compile(r"/api/v1/[A-Za-z0-9_{}/.-]*[A-Za-z0-9}]")
TOPIC = re.compile(r"armor/[A-Za-z0-9_{}/#+-]*[A-Za-z0-9}#]")


def shape(text: str) -> str:
    """A path or topic with every `{name}` made the same, so that {id} and {node_id} compare equal."""
    return re.sub(r"\{[^}]*\}", "{}", text)


def paths_of_openapi(file: Path) -> set[str]:
    text = file.read_text(encoding="utf-8")
    if file.suffix == ".json":
        return {shape(path) for path in json.loads(text).get("paths", {})}
    return {shape(match.group(1)) for match in re.finditer(r"^  (/api/v1/[^:\s]+):\s*$", text, re.M)}


def addresses_of_asyncapi(file: Path) -> set[str]:
    channels = json.loads(file.read_text(encoding="utf-8")).get("channels", {})
    return {shape(str(channel.get("address", ""))) for channel in channels.values()}


def _covered(topic: str, address: str) -> bool:
    """A topic written with a placeholder is covered by a wildcard address (`#`) of the document."""
    return address.endswith("/#") and topic.startswith(address[:-1])


def problems(page: Path, common: Path) -> list[str]:
    text = page.read_text(encoding="utf-8")
    routes = {shape(item) for item in ROUTE.findall(text)}
    topics = {shape(item) for item in TOPIC.findall(text)}
    known_routes: set[str] = set()
    for file in sorted((common / "openapi").glob("*.y*ml")) + sorted((common / "openapi").glob("*.json")):
        known_routes |= paths_of_openapi(file)
    known_topics: set[str] = set()
    for file in sorted((common / "asyncapi").glob("*.json")):
        known_topics |= addresses_of_asyncapi(file)
    found = [f"route {route} is not in the OpenAPI file" for route in sorted(routes - known_routes)]
    found += [f"topic {topic} is not an address of the AsyncAPI document" for topic in sorted(topics - known_topics) if not any(_covered(topic, address) for address in known_topics)]
    if not routes or not topics:
        found.append("the page names no route or no topic: the check would pass on nothing")
    return found


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Check that the routes and topics of docs/SEQUENCES.md exist in the contracts.")
    parser.add_argument("--common", type=Path, default=DOCS_ROOT.parent / "ARMOR-COMMON")
    parser.add_argument("--page", type=Path, default=PAGE)
    args = parser.parse_args(argv)
    if not (args.common / "openapi").is_dir():
        print(f"SEQUENCES=SKIP ARMOR-COMMON is not next to this repository ({args.common})")
        return 0
    found = problems(args.page, args.common)
    for line in found:
        print(line, file=sys.stderr)
    print(f"SEQUENCES={'FAIL' if found else 'PASS'}")
    return 1 if found else 0


if __name__ == "__main__":
    raise SystemExit(main())
