"""The list of the repositories of the family, read from the one place that keeps it: registry/repositories.json of ARMOR-COMMON.

Copyright (C) 2026 JuanenRac (Electro Hobby 3D). GPL-3.0-or-later.

Every tool of this repository that has to name the repositories (the order of the READMEs, the brand pictures and the map of the family, the repositories that get the shared tools and the
workflow of Studio and the server, the catalogue) reads them from here, so a repository is added once. ARMOR-COMMON must be next to this repository (the workflow of the CI fetches it);
ARMOR_REGISTRY names another file when it is elsewhere.
"""
from __future__ import annotations

import json
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REGISTRY_FILE = Path(os.environ.get("ARMOR_REGISTRY") or ROOT / "ARMOR-COMMON" / "registry" / "repositories.json")


def load() -> dict:
    try:
        return json.loads(REGISTRY_FILE.read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise SystemExit(f"the registry of the repositories was not found at {REGISTRY_FILE}: ARMOR-COMMON has to be next to ARMOR-DOCS (or set ARMOR_REGISTRY)") from None


REGISTRY = load()
REPOSITORIES: list[dict] = REGISTRY["repositories"]
NAMES: list[str] = [entry["name"] for entry in REPOSITORIES]
COLUMN_TITLES: list[str] = REGISTRY["columns"]


def names_where(field: str) -> list[str]:
    """The repositories whose flag `field` is on, in the order of the registry."""
    return [entry["name"] for entry in REPOSITORIES if entry.get(field)]
