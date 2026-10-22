#!/usr/bin/env python3
"""Render the README of every A.R.M.O.R. repository in the eight languages of the family.

Copyright (C) 2026 JuanenRac (Electro Hobby 3D). GPL-3.0-or-later.

Every repository is described once, in tools/readme_src/repos/<REPOSITORY>.py: the FACTS that do not depend on the language (the badges, the diagram, the commands, the structure) and the
TEXT of each language. The words around every README and the one-line description of each repository are in tools/readme_src/ui.py. The eight files of a repository are rendered
from the same data, so they can never drift apart in structure: README.md (English) and README_spa / _fra / _ita / _deu / _zho / _jpn / _por.

    python tools/make_readmes.py          # write the READMEs
    python tools/make_readmes.py --check  # fail when one is out of date
"""
from __future__ import annotations

import argparse
import importlib
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from readme_src.shots import CAPTIONS, HEADING as SHOTS_HEADING, NOTE as SHOTS_NOTE, SHOTS  # noqa: E402
from readme_src.ui import RELATED, UI  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
GITHUB_OWNER = "JuanenRac"

# code, README file name, flag and name of each language, in the order of the language bar
LANGUAGES = [
    ("en", "README.md", "🇺🇸", "English"), ("es", "README_spa.md", "🇪🇸", "Español"), ("fr", "README_fra.md", "🇫🇷", "Français"),
    ("it", "README_ita.md", "🇮🇹", "Italiano"), ("de", "README_deu.md", "🇩🇪", "Deutsch"), ("zh", "README_zho.md", "🇨🇳", "简体中文"),
    ("ja", "README_jpn.md", "🇯🇵", "日本語"), ("pt", "README_por.md", "🇵🇹", "Português"),
]
# the order of the repositories in the family list (every repository of the family appears in it)
ORDER = ["ARMOR-COMMON", "ARMOR-RADAR", "ARMOR-SOLAR", "ARMOR-ELECTRICAL", "ARMOR-ALARM", "ARMOR-HMI", "ARMOR-NETWORK", "ARMOR-SERVER", "ARMOR-STUDIO", "ARMOR-ANDROID-CONTROL",
         "ARMOR-SERVER-AI", "ARMOR-VISION", "ARMOR-VOICE-AI", "ARMOR-HARDWARE", "ARMOR-DEVOPS", "ARMOR-SIMULATOR", "ARMOR-UPDATER", "ARMOR-DOCS"]
SECTION_ICONS = ["🔒", "🌐", "⚙️"]


def load(name: str):
    return importlib.import_module(f"readme_src.repos.{name.replace('-', '_')}")


MATURITY_COLOR = {"scaffolding": "FFB020", "functional": "00E5FF", "established": "2EA44F", "production": "1F883D"}


def manifest(name: str) -> dict:
    return json.loads((ROOT / name / "armor.project.json").read_text(encoding="utf-8"))


def glance(name: str, language: str, info: dict, facts: dict, text: dict, ui: dict) -> str:
    """A small table with the facts that go stale first: version and maturity (from the manifest), the tests, the stack and what has run on real hardware."""
    if "hardware" not in text:
        return ""
    rows = [(ui["g_version"], f"`{info['version']}`"), (ui["g_maturity"], ui["m_" + info["maturity"]])]
    if facts.get("tests"):
        rows.append((ui["g_tests"], text.get("tests", facts["tests"])))   # a language may word it (text["tests"]); the number is the same
    rows.append((ui["g_stack"], info.get("stack", "")))
    rows.append((ui["g_hardware"], text["hardware"]))
    body = "\n".join(f"| {a} | {b} |" for a, b in rows)
    return f"## 📋 {ui['glance']}\n\n| | |\n|---|---|\n{body}\n\n"


def render(name: str, language: str) -> str:
    data = load(name)
    facts, text, ui = data.FACTS, data.TEXT[language], UI[language]
    emoji = text.get("emoji_own", facts["emoji"])
    info = manifest(name)
    # the version and the maturity are never written by hand: they come from the manifest of the repository, so a README cannot be behind its project
    badges = [badge for badge in text.get("badges_own", facts["badges"]) if badge[0] not in ("Maturity", "Version")]
    badges.append(["Version", info["version"], "0f6cbd"])
    badges.append(["Maturity", info["maturity"], MATURITY_COLOR[info["maturity"]]])
    badge_html = "\n".join(f'  <img src="https://img.shields.io/badge/{label}-{value}-{color}.svg" alt="{label}">' for label, value, color in badges)
    bar = " |\n  ".join(f"{flag} <b>{title}</b>" if code == language else f'<a href="{file}">{flag} {title}</a>' for code, file, flag, title in LANGUAGES)
    structure = text.get("structure_own", facts["structure"])
    build = text.get("build_own", facts["build"])
    diagram = text.get("diagram_own", facts.get("diagram", ""))
    parts = [f'''<p align="center">
  <img src="images/ARMOR_BANNER.svg" alt="{name} banner" width="100%">
</p>

# {emoji} {name}

<p align="center">
  {bar}
</p>

### {text['tagline']}

<p align="center">
  <img src="https://img.shields.io/badge/License-GPL%203.0-blue.svg" alt="GPL 3.0">
{badge_html}
</p>

---

{ui['honesty_prefix']}{text['honest']}

---

{glance(name, language, info, facts, text, ui)}## 🎯 {ui['overview']}
''']
    if text.get("intro"):
        parts.append(text["intro"] + "\n")
    parts.append("\n".join(f"* {item}" for item in text["bullets"]) + "\n")
    if SHOTS.get(name):
        cells = [f'<td width="50%" valign="top"><img src="images/screenshots/{file}.png" alt="{CAPTIONS[key][language]}" width="100%"><br><sub>{CAPTIONS[key][language]}</sub></td>' for file, key in SHOTS[name]]
        rows = "\n".join("<tr>" + "".join(cells[i:i + 2]) + "</tr>" for i in range(0, len(cells), 2))
        parts.append(f"## 🖼️ {SHOTS_HEADING[language]}\n\n{SHOTS_NOTE[language]}\n\n<table>\n{rows}\n</table>\n")
    if text.get("fit"):
        parts.append(f"## 🧩 {ui['fit']}\n\n{text['fit']}\n")
    if diagram:
        parts.append(f"## 🔄 {ui['architecture']}\n\n{diagram}\n")
    for section in text.get("sections", []):
        parts.append(f"## {section['icon']} {section['title']}\n\n" + "\n".join(f"* {item}" for item in section["bullets"]) + "\n")
    parts.append(f"## 📂 {ui['structure']}\n\n{structure}\n")
    requirements = text.get("requirements", facts.get("requirements"))   # worded in each language when text["requirements"] exists
    needs = f"**{ui['requirements']}:** " + ", ".join(requirements) + "\n\n" if requirements else ""
    parts.append(f"## 🛠️ {ui['dev']}\n\n{needs}{build}\n" + (f"\n{text['note']}\n" if text.get("note") else ""))

    def repo_url(repo: str) -> str:
        return f"https://github.com/{GITHUB_OWNER}/{repo}"

    related = "\n".join(
        f"* **[{other}]({repo_url(other)})** - {RELATED[language][other]}" if other != name else f"* **{other}** ({ui['here']}) - {RELATED[language][other]}"
        for other in ORDER)
    parts.append(f"## 🔗 {ui['related']}\n\n{ui['family']}\n\n{related}\n")
    matrix = "docs/CAPABILITY_MATRIX.md" if name == "ARMOR-DOCS" else f"{repo_url('ARMOR-DOCS')}/blob/main/docs/CAPABILITY_MATRIX.md"
    catalog = "docs/PROJECT_CATALOG.md" if name == "ARMOR-DOCS" else f"{repo_url('ARMOR-DOCS')}/blob/main/docs/PROJECT_CATALOG.md"
    parts.append(f"## 📚 {ui['community']}\n\n{ui['docs_intro']}\n\n"
                 f"* [{ui['doc_matrix']}]({matrix})\n* [{ui['doc_catalog']}]({catalog})\n"
                 f"* [{ui['doc_changelog']}](CHANGELOG.md)\n* [{ui['doc_license']}](LICENSE)\n* {ui['contact']}\n")
    parts.append(f"## 👤 {ui['author']}\n\n**JuanenRac (Electro Hobby 3D)** · electrohobby3d@gmail.com\n\n## 📜 {ui['license']}\n\n{ui['license_text']}\n")
    return "\n".join(parts)


def outputs() -> dict[Path, str]:
    files: dict[Path, str] = {}
    for name in ORDER:
        for code, file, *_ in LANGUAGES:
            files[ROOT / name / file] = render(name, code)
    return files


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    stale = []
    files = outputs()
    for path, content in files.items():
        current = path.read_text(encoding="utf-8").replace("\r\n", "\n") if path.exists() else None
        if current == content:
            continue
        stale.append(str(path))
        if not args.check:
            path.write_text(content, encoding="utf-8", newline="\n")
    if args.check and stale:
        print("READMEs out of date:", *stale, sep="\n  ", file=sys.stderr)
        return 1
    print("READMEs current" if args.check else f"READMEs written: {len(files)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
