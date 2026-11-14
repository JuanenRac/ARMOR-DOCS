#!/usr/bin/env python3
"""ARMOR-DOCS - a static site from the documents that are already public.

Copyright (C) 2026 JuanenRac (Electro Hobby 3D). GPL-3.0-or-later.

    python tools/make_site.py                 # write site/ (ignored by git) from docs/*.md, the contract documents of ARMOR-COMMON and the OpenAPI and AsyncAPI files
    python tools/make_site.py --out DIR       # write somewhere else
    python tools/make_site.py --check         # build in a temporary folder and fail when a page would carry something that must not go public

Only text that is already committed in public repositories goes in: the documents of this repository, and (when ARMOR-COMMON is next to it) its contract documents, the paths and
operations of the OpenAPI file and the channels of the AsyncAPI file. Every page is scanned with the rules of publication_check.py before it is written and a BLOCK finding stops the
build. Nothing is fetched from the network and nothing is published here: the `site` workflow builds the folder as an artifact.
"""
from __future__ import annotations

import argparse
import html
import json
import re
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import publication_check  # noqa: E402

DOCS_ROOT = HERE.parent
COMMON_DOCS = ("CONTRACTS.md", "CONTRACT_MATRIX.md", "FIRMWARE_BASE.md", "NODE_ROLES.md", "PORTS.md", "SIGNED_FIRMWARE.md")
METHODS = ("get", "put", "post", "delete", "patch")
STYLE = """:root{color-scheme:light dark;--bg:#fff;--fg:#1c2330;--muted:#5b6678;--line:#d5dae3;--accent:#0b5cad}
@media (prefers-color-scheme:dark){:root{--bg:#10151d;--fg:#e4e9f1;--muted:#9aa6b8;--line:#2b3442;--accent:#6ab0f3}}
body{margin:0;background:var(--bg);color:var(--fg);font:16px/1.55 system-ui,sans-serif}
main{max-width:60rem;margin:0 auto;padding:1rem 16px 3rem}nav a{margin-right:1rem}a{color:var(--accent)}
table{border-collapse:collapse;display:block;overflow-x:auto}th,td{border:1px solid var(--line);padding:.3rem .6rem;text-align:left}
pre{overflow-x:auto;padding:.7rem;border:1px solid var(--line)}code{font-family:ui-monospace,monospace}h1,h2,h3{line-height:1.25}"""


def inline(text: str) -> str:
    """Code, bold, italic and links of one line of Markdown (everything else is escaped)."""
    text = html.escape(text, quote=False)
    text = re.sub(r"`([^`]+)`", lambda m: f"<code>{m.group(1)}</code>", text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<![*\w])\*([^*\s][^*]*)\*(?!\*)", r"<em>\1</em>", text)

    def link(match: re.Match[str]) -> str:
        target = match.group(2)
        if re.fullmatch(r"[A-Za-z0-9_./-]+\.md(#[\w-]+)?", target) and not target.startswith("http"):
            target = re.sub(r"\.md(#|$)", r".html\1", target)
        elif not re.match(r"(https://|#|[A-Za-z0-9_./-]+\.html)", target):
            return match.group(1)   # a link that leads nowhere on the site (a relative file of a repository) stays as plain text
        return f'<a href="{target}">{match.group(1)}</a>'

    return re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", link, text)


def render_markdown(source: str) -> str:
    """A small subset of Markdown: headings, paragraphs, lists, tables, fenced code and block quotes. Raw HTML in the source is shown as text, never as markup."""
    out: list[str] = []
    lines = source.replace("\r\n", "\n").split("\n")
    index = 0
    paragraph: list[str] = []

    def flush() -> None:
        if paragraph:
            out.append("<p>" + inline(" ".join(paragraph)) + "</p>")
            paragraph.clear()

    while index < len(lines):
        line = lines[index]
        if line.startswith("```"):
            flush()
            index += 1
            block = []
            while index < len(lines) and not lines[index].startswith("```"):
                block.append(lines[index])
                index += 1
            out.append("<pre><code>" + html.escape("\n".join(block)) + "</code></pre>")
        elif re.match(r"#{1,6} ", line):
            flush()
            level = len(line.split(" ")[0])
            out.append(f"<h{level}>{inline(line[level + 1:].strip())}</h{level}>")
        elif line.startswith("|") and index + 1 < len(lines) and re.match(r"\|[\s:|-]+\|?$", lines[index + 1]):
            flush()
            head = [cell.strip() for cell in line.strip().strip("|").split("|")]
            out.append("<table><thead><tr>" + "".join(f"<th>{inline(cell)}</th>" for cell in head) + "</tr></thead><tbody>")
            index += 2
            while index < len(lines) and lines[index].startswith("|"):
                row = [cell.strip() for cell in lines[index].strip().strip("|").split("|")]
                out.append("<tr>" + "".join(f"<td>{inline(cell)}</td>" for cell in row) + "</tr>")
                index += 1
            out.append("</tbody></table>")
            continue
        elif re.match(r"\s*([*-]|\d+\.) ", line):
            flush()
            ordered = bool(re.match(r"\s*\d+\. ", line))
            out.append("<ol>" if ordered else "<ul>")
            while index < len(lines) and re.match(r"\s*([*-]|\d+\.) ", lines[index]):
                out.append("<li>" + inline(re.sub(r"^\s*([*-]|\d+\.) ", "", lines[index])) + "</li>")
                index += 1
            out.append("</ol>" if ordered else "</ul>")
            continue
        elif line.startswith(">"):
            flush()
            out.append("<blockquote>" + inline(line.lstrip("> ")) + "</blockquote>")
        elif not line.strip():
            flush()
        else:
            paragraph.append(line.strip())
        index += 1
    flush()
    return "\n".join(out)


def page(title: str, body: str, pages: list[tuple[str, str]]) -> str:
    links = " ".join(f'<a href="{name}">{html.escape(label)}</a>' for name, label in pages)
    return (f'<!doctype html>\n<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
            f"<title>{html.escape(title)}</title><style>{STYLE}</style></head><body><main><nav>{links}</nav>\n{body}\n</main></body></html>\n")


def openapi_table(path: Path) -> str:
    """The operations of an OpenAPI file (method, path, summary) as a Markdown table."""
    document = json.loads(path.read_text(encoding="utf-8")) if path.suffix == ".json" else _yaml(path)
    rows = ["| Method | Path | Summary |", "|---|---|---|"]
    for route in sorted(document.get("paths", {})):
        for method in METHODS:
            operation = document["paths"][route].get(method)
            if isinstance(operation, dict):
                rows.append(f"| {method.upper()} | `{route}` | {str(operation.get('summary', '')).replace('|', '/')} |")
    return "\n".join(rows)


def _yaml(path: Path) -> dict:
    import yaml  # type: ignore[import-untyped]  # the site build runs where the CI of the family already installs PyYAML

    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}


def asyncapi_table(path: Path) -> str:
    document = json.loads(path.read_text(encoding="utf-8"))
    rows = ["| Channel | Address |", "|---|---|"]
    channels = document.get("channels", {})
    for name in sorted(channels):
        rows.append(f"| `{name}` | `{channels[name].get('address', '')}` |")
    return "\n".join(rows)


def collect(common: Path | None) -> list[tuple[str, str, str]]:
    """(page file name, title, Markdown) of every page of the site."""
    found: list[tuple[str, str, str]] = []
    for file in sorted((DOCS_ROOT / "docs").glob("*.md")):
        found.append((file.stem.lower().replace("_", "-") + ".html", file.stem.replace("_", " ").title(), file.read_text(encoding="utf-8")))
    if common is not None and common.is_dir():
        for name in COMMON_DOCS:
            file = common / "docs" / name
            if file.is_file():
                found.append(("contract-" + file.stem.lower().replace("_", "-") + ".html", "Contract: " + file.stem.replace("_", " ").title(), file.read_text(encoding="utf-8")))
        for candidate in sorted((common / "openapi").glob("*.y*ml")) + sorted((common / "openapi").glob("*.json")):
            found.append(("rest-api.html", "REST API (OpenAPI)", "# REST API\n\nGenerated from the OpenAPI file of the shared contracts.\n\n" + openapi_table(candidate)))
            break
        for candidate in sorted((common / "asyncapi").glob("*.json")):
            found.append(("mqtt-api.html", "MQTT channels (AsyncAPI)", "# MQTT channels\n\nGenerated from the AsyncAPI file of the shared contracts.\n\n" + asyncapi_table(candidate)))
            break
    return found


def build(out: Path, common: Path | None) -> list[str]:
    """Write the site into `out` and return the problems (a BLOCK finding of the publication check)."""
    pages = collect(common)
    nav = [("index.html", "Home")] + [(name, title) for name, title, _ in pages]
    problems: list[str] = []
    out.mkdir(parents=True, exist_ok=True)
    index = "# A.R.M.O.R. documentation\n\nThe documents of the family, the shared contracts and the interfaces, generated from what is already public.\n\n" + "\n".join(f"* [{title}]({name})" for name, title, _ in pages)
    for name, title, source in [("index.html", "A.R.M.O.R. documentation", index)] + pages:
        findings: list[tuple[str, str, str, str]] = []
        publication_check.scan_text("site", name, source, findings)
        problems.extend(f"{where}: {what}" for level, _, where, what in findings if level == "BLOCK")
        (out / name).write_text(page(title, render_markdown(source), nav), encoding="utf-8", newline="\n")
    return problems


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Build the static documentation site from the public documents.")
    parser.add_argument("--out", type=Path, default=DOCS_ROOT / "site")
    parser.add_argument("--common", type=Path, default=DOCS_ROOT.parent / "ARMOR-COMMON", help="the ARMOR-COMMON checkout (optional)")
    parser.add_argument("--check", action="store_true", help="build in a temporary folder and fail on a BLOCK finding")
    args = parser.parse_args(argv)
    if args.check:
        with tempfile.TemporaryDirectory() as holder:
            problems = build(Path(holder) / "site", args.common)
    else:
        problems = build(args.out, args.common)
    for line in problems:
        print(line, file=sys.stderr)
    print(f"SITE={'FAIL' if problems else 'PASS'}")
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main())
