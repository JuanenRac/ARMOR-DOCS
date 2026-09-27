#!/usr/bin/env python3
"""Render the README of every A.R.M.O.R. repository in the seven languages of the family.

Copyright (C) 2026 JuanenRac (Electro Hobby 3D). GPL-3.0-or-later.

Each repository is described once per language, so the seven files of a repository can never drift apart in structure:
README.md (English) and README_spa / _deu / _fra / _ita / _jpn / _zho. The texts live in tools/readme_data/ (one module per language, the
language-neutral badges, build and structure blocks in legacy.py and meta_new.py).

    python tools/make_readmes.py          # write the READMEs
    python tools/make_readmes.py --check  # fail when one is out of date
"""
from __future__ import annotations

import argparse
import importlib
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from readme_data.legacy import REPOS as LEGACY  # noqa: E402
from readme_data.meta_new import FIXES, META as META_NEW  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]

# code, README file name, flag and name of each language, in the order of the language bar
LANGUAGES = [
    ("en", "README.md", "🇺🇸", "English"), ("es", "README_spa.md", "🇪🇸", "Español"), ("fr", "README_fra.md", "🇫🇷", "Français"),
    ("it", "README_ita.md", "🇮🇹", "Italiano"), ("de", "README_deu.md", "🇩🇪", "Deutsch"), ("zh", "README_zho.md", "🇨🇳", "简体中文"), ("ja", "README_jpn.md", "🇯🇵", "日本語"),
]
# the order of the repositories in the family list
ORDER = ["ARMOR-COMMON", "ARMOR-RADAR", "ARMOR-SOLAR", "ARMOR-ELECTRICAL", "ARMOR-NETWORK", "ARMOR-SERVER", "ARMOR-STUDIO", "ARMOR-ANDROID-CONTROL", "ARMOR-SERVER-AI", "ARMOR-VOICE-AI",
         "ARMOR-HARDWARE", "ARMOR-DEVOPS", "ARMOR-SIMULATOR", "ARMOR-UPDATER", "ARMOR-DOCS"]
SECTION_ICONS = ["🔒", "🌐", "⚙️"]
PATCHES: dict = {}

_modules = {code: importlib.import_module(f"readme_data.{code}") for code, *_ in LANGUAGES}


def split_build(block: str) -> tuple[str, str]:
    """A legacy build block is code fences followed by a sentence; split them."""
    end = block.rfind("```") + 3
    return block[:end], block[end:].strip()


def meta(name: str) -> dict:
    if name in META_NEW:
        return META_NEW[name]
    legacy = LEGACY[name]
    code, _ = split_build(legacy["en"]["build"])
    for old, new in PATCHES.get(name, []):
        code = code.replace(old, new)
    result = {"emoji": legacy["emoji"], "badges": legacy["badges"], "diagram": "", "build": code, "structure": legacy["en"]["structure"]}
    result.update({k: v for k, v in FIXES.get(name, {}).items() if k in ("build", "structure", "badges")})
    return result


def texts(name: str, language: str) -> dict:
    """The words of one repository in one language: the module of the language wins over the first generation (legacy)."""
    own = _modules[language].TEXT.get(name, {})
    if name in LEGACY and language in ("en", "es"):
        base = dict(LEGACY[name][language])
        _, base["note"] = split_build(base["build"])
        base["bullets"] = list(base["bullets"])
        for old, new in PATCHES.get(name, []):
            base["honest"] = base["honest"].replace(old, new)
        replace = own.get("bullets_replace", {})
        for prefix, new in replace.items():
            matches = [i for i, item in enumerate(base["bullets"]) if prefix in item]
            assert len(matches) == 1, (name, language, prefix)
            base["bullets"][matches[0]] = new
        base.update({k: v for k, v in own.items() if k != "bullets_replace"})
        base["structure_text"] = LEGACY[name][language]["structure"]
        return base
    assert own and "tagline" in own, f"no text for {name} in {language}"
    return own


def render(name: str, language: str) -> str:
    m, text, ui = meta(name), texts(name, language), _modules[language].UI
    badges = "\n".join(f'  <img src="https://img.shields.io/badge/{label}-{value}-{color}.svg" alt="{label}">' for label, value, color in m["badges"])
    bar = " |\n  ".join(f"{flag} <b>{title}</b>" if code == language else f'<a href="{file}">{flag} {title}</a>' for code, file, flag, title in LANGUAGES)
    bullets = "\n".join(f"* {item}" for item in text["bullets"])
    structure = text.get("structure_text") if language == "es" and "structure_text" in text else m["structure"]
    if language == "es" and "structure_es" in FIXES.get(name, {}):
        structure = FIXES[name]["structure_es"]
    parts = [f'''<p align="center">
  <img src="images/ARMOR_BANNER.svg" alt="{name} banner" width="100%">
</p>

# {m['emoji']} {name}

<p align="center">
  {bar}
</p>

### {text['tagline']}

<p align="center">
  <img src="https://img.shields.io/badge/License-GPL%203.0-blue.svg" alt="GPL 3.0">
{badges}
</p>

---

**{ui['honesty']}:** {text['honest']}

---

## 🎯 {ui['overview']}
''']
    if text.get("intro"):
        parts.append(text["intro"] + "\n")
    if name == "ARMOR-DOCS":
        parts.append('<p align="center">\n  <img src="images/ARMOR_FAMILY.svg" alt="A.R.M.O.R. family" width="100%">\n</p>\n')
    parts.append(bullets + "\n")
    if m.get("diagram"):
        parts.append(f"## 🔄 {ui['architecture']}\n\n{m['diagram']}\n")
    for index, section in enumerate(text.get("sections", [])):
        parts.append(f"## {SECTION_ICONS[index % len(SECTION_ICONS)]} {section['title']}\n\n" + "\n".join(f"* {item}" for item in section["bullets"]) + "\n")
    parts.append(f"## 📂 {ui['structure']}\n\n{structure}\n")
    parts.append(f"## 🛠️ {ui['dev']}\n\n{m['build']}\n" + (f"\n{text['note']}\n" if text.get("note") else ""))
    # A relative link like `../ARMOR-COMMON` only ever worked for someone
    # Browse a local sibling-folder checkout: each A.R.M.O.R. repository is
    # its own separate GitHub repository, not a folder inside a monorepo, so
    # `../` resolves to a nonexistent path on github.com (relative to the
    # FILE's own blob path, not the account) and 404s. Cross-repository
    # links use the real, absolute GitHub URL instead; a same-repository
    # link (docs/*.md within ARMOR-DOCS's own README, or another file
    # already relative in this function) is unaffected and stays relative.
    GITHUB_OWNER = "JuanenRac"
    def repo_url(repo: str) -> str:
        return f"https://github.com/{GITHUB_OWNER}/{repo}"
    related = "\n".join(
        f"* **[{other}]({repo_url(other)})** - {_modules[language].RELATED[other]}" if other != name else f"* **{other}** ({ui['here']}) - {_modules[language].RELATED[other]}"
        for other in ORDER)
    parts.append(f"## 🔗 {ui['related']}\n\n{ui['family']}\n\n{related}\n")
    doc_matrix_link = "docs/CAPABILITY_MATRIX.md" if name == "ARMOR-DOCS" else f"{repo_url('ARMOR-DOCS')}/blob/main/docs/CAPABILITY_MATRIX.md"
    doc_catalog_link = "docs/PROJECT_CATALOG.md" if name == "ARMOR-DOCS" else f"{repo_url('ARMOR-DOCS')}/blob/main/docs/PROJECT_CATALOG.md"
    parts.append(f"## 📚 {ui['community']}\n\n{ui['docs_intro']}\n\n"
                 f"* [{ui['doc_matrix']}]({doc_matrix_link})\n* [{ui['doc_catalog']}]({doc_catalog_link})\n"
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
    for path, content in outputs().items():
        current = path.read_text(encoding="utf-8") if path.exists() else None
        if current == content:
            continue
        stale.append(str(path))
        if not args.check:
            path.write_text(content, encoding="utf-8", newline="\n")
    if args.check and stale:
        print("READMEs out of date:", *stale, sep="\n  ", file=sys.stderr)
        return 1
    print("READMEs current" if args.check else f"READMEs written: {len(outputs())}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
