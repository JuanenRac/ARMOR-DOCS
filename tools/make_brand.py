#!/usr/bin/env python3
"""Generate the A.R.M.O.R. brand assets for every repository.

Copyright (C) 2026 JuanenRac (Electro Hobby 3D). GPL-3.0-or-later.

The look follows the HYDRA-UMC family: a near-black gradient, thin cyan
circuit traces, a glowing line emblem and bold letter-spaced titles. The
emblem is a shield around a radar sweep, which is what A.R.M.O.R. is.

Usage:  python tools/make_brand.py            # writes brand/ and images/ in every repo
        python tools/make_brand.py --check    # fails if any asset is out of date
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

CYAN = "#00E5FF"
AMBER = "#FFB020"
BG_FROM, BG_TO = "#07090C", "#12161C"

# repository -> (tagline, hashtags)
REPOS: dict[str, tuple[str, list[str]]] = {
    "ARMOR-COMMON": ("MESSAGE CONTRACTS & VALIDATION", ["JSON-SCHEMA", "OPENAPI", "PYTHON", "TYPESCRIPT", "KOTLIN"]),
    "ARMOR-RADAR": ("FIELD-NODE FIRMWARE", ["ESP32-S3", "LD2450", "MQTT", "PoE", "C++"]),
    "ARMOR-SERVER-AI": ("VISUAL INFERENCE POLICY", ["JETSON", "TENSORRT", "YOLO", "RTSP", "PYTHON"]),
    "ARMOR-VOICE-AI": ("OFFLINE VOICE INTENT BOUNDARY", ["WHISPER", "PIPER", "WYOMING", "PYTHON"]),
    "ARMOR-SERVER": ("CENTRAL SECURITY COORDINATOR", ["NODE", "TYPESCRIPT", "MQTT", "WEBSOCKET", "FFMPEG"]),
    "ARMOR-STUDIO": ("OPERATIONS & DESIGN CONSOLE", ["REACT", "TYPESCRIPT", "VITE", "2D/3D", "I18N"]),
    "ARMOR-ANDROID-CONTROL": ("MOBILE OPERATOR CLIENT", ["KOTLIN", "COMPOSE", "MJPEG", "PTZ"]),
    "ARMOR-HARDWARE": ("ENCLOSURES & ELECTRONICS", ["OPENSCAD", "KICAD", "ASA/PETG", "24GHZ"]),
    "ARMOR-DEVOPS": ("DEPLOYMENT & OPERATIONS", ["DOCKER", "SYSTEMD", "ARM64", "BASH"]),
    "ARMOR-DOCS": ("TECHNICAL DOCUMENTATION", ["MARKDOWN", "MERMAID", "ARCHITECTURE"]),
    "ARMOR-SIMULATOR": ("OFFLINE TELEMETRY SIMULATOR", ["PYTHON", "MQTT", "RTSP", "TESTING"]),
}


def emblem(scale: float = 1.0) -> str:
    """A shield around a radar sweep, in the same glowing line style as HYDRA."""
    return f"""<g transform="scale({scale})" filter="url(#g)" fill="none" stroke="{CYAN}" stroke-width="4" stroke-linejoin="round" stroke-linecap="round">
    <path d="M0,-84 L66,-58 V4 C66,48 34,72 0,88 C-34,72 -66,48 -66,4 V-58 Z"/>
    <circle r="46" stroke-width="2" opacity=".55"/>
    <circle r="28" stroke-width="2" opacity=".55"/>
    <circle r="10" stroke-width="2" opacity=".55"/>
    <path d="M0,0 L34,-32" stroke-width="4"/>
    <path d="M0,-46 A46,46 0 0 1 32.5,-32.5" stroke="{AMBER}" stroke-width="3" opacity=".9"/>
    <circle cx="34" cy="-32" r="5" fill="{AMBER}" stroke="none"/>
    <circle r="4" fill="{CYAN}" stroke="none"/>
  </g>"""


def defs() -> str:
    return f"""<defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%"><stop stop-color="{BG_FROM}"/><stop offset="1" stop-color="{BG_TO}"/></linearGradient>
    <filter id="g"><feGaussianBlur stdDeviation="4" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
  </defs>"""


def banner(name: str, tagline: str, tags: list[str]) -> str:
    tag_x = [105 + index * 150 for index in range(len(tags))]
    tag_text = "".join(f'<text x="{x}" y="360">#{tag}</text>' for x, tag in zip(tag_x, tags))
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 400" role="img" aria-labelledby="title desc">
  <title id="title">{name}</title><desc id="desc">{name} | A.R.M.O.R. Autonomous Radar &amp; Multimodal Observation Range</desc>
  {defs()}
  <rect width="1200" height="400" fill="url(#bg)"/>
  <g fill="none" stroke="{CYAN}" stroke-width="1" opacity=".25"><path d="M0 100H200L250 150H600"/><path d="M1200 300H1000L950 250H600"/><path d="M1200 80H1040L1000 120H760"/></g>
  <g transform="translate(205 190)">{emblem()}</g>
  <text x="360" y="136" font-family="Arial,sans-serif" font-size="50" font-weight="bold" fill="#FFF" letter-spacing="8">A.R.M.O.R.</text>
  <text x="364" y="181" font-family="Arial,sans-serif" font-size="17" fill="{CYAN}" letter-spacing="4">AUTONOMOUS RADAR &amp; MULTIMODAL OBSERVATION RANGE</text>
  <text x="360" y="246" font-family="Arial,sans-serif" font-size="29" font-weight="bold" fill="#FFF">{name}</text>
  <text x="362" y="280" font-family="Arial,sans-serif" font-size="16" fill="{AMBER}" letter-spacing="3">{tagline}</text>
  <g font-family="monospace" font-size="12" fill="{CYAN}" opacity=".65">{tag_text}</g>
</svg>
"""


def icon() -> str:
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="-110 -110 220 220" role="img" aria-label="A.R.M.O.R.">
  {defs()}
  <rect x="-110" y="-110" width="220" height="220" rx="36" fill="url(#bg)"/>
  {emblem(0.95)}
</svg>
"""


def outputs(root: Path) -> dict[Path, str]:
    files: dict[Path, str] = {root / "ARMOR-DOCS" / "brand" / "ARMOR_ICON.svg": icon()}
    for name, (tagline, tags) in REPOS.items():
        target = root / name / "images"
        files[target / "ARMOR_BANNER.svg"] = banner(name, tagline, tags)
        files[target / "ARMOR_ICON.svg"] = icon()
    return files


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="only verify that every asset is current")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[2])
    args = parser.parse_args()
    stale = []
    for path, content in outputs(args.root).items():
        if not path.parent.parent.exists():
            continue
        current = path.read_text(encoding="utf-8") if path.exists() else None
        if current == content:
            continue
        stale.append(path)
        if not args.check:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8", newline="\n")
    if args.check and stale:
        print("out of date:", *(str(path) for path in stale), sep="\n  ", file=sys.stderr)
        return 1
    print(f"brand assets {'current' if args.check else 'written'}: {len(outputs(args.root))} files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
