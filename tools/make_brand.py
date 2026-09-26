#!/usr/bin/env python3
"""Generate the A.R.M.O.R. brand assets: one banner and one icon per repository, and the map of the family.

Copyright (C) 2026 JuanenRac (Electro Hobby 3D). GPL-3.0-or-later.

The look: a near-black gradient, thin cyan circuit traces, a glowing line emblem and bold letter-spaced titles. Every repository wears the same shield,
with its own drawing inside it (a radar sweep for the radar firmware, a sun for the solar monitor, a rack for the server, and so on), so that the
banners and icons tell the projects apart at a glance.

Usage:  python tools/make_brand.py            # writes brand/ and images/ in every repo
        python tools/make_brand.py --check    # fails if any asset is out of date
"""
from __future__ import annotations

import argparse
import html
import sys
from pathlib import Path

CYAN = "#00E5FF"
AMBER = "#FFB020"
GREEN = "#5DF0C4"
BG_FROM, BG_TO = "#07090C", "#12161C"

# repository -> (tagline, hashtags)
REPOS: dict[str, tuple[str, list[str]]] = {
    "ARMOR-COMMON": ("MESSAGE CONTRACTS & VALIDATION", ["JSON-SCHEMA", "OPENAPI", "PYTHON", "TYPESCRIPT", "KOTLIN"]),
    "ARMOR-RADAR": ("FIELD-NODE FIRMWARE", ["ESP32-S3", "LD2450", "MQTT", "PoE", "C++"]),
    "ARMOR-SOLAR": ("SOLAR INVERTER & BATTERY MONITORING", ["VOLTRONIC", "PYLONTECH", "RS232", "RS485", "C++"]),
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

S = 'fill="none" stroke-linecap="round" stroke-linejoin="round"'   # the common attributes of a line drawing


def glyph(name: str) -> str:
    """The drawing inside the shield, in a box of about 84 by 84 around the origin."""
    g = {
        "ARMOR-RADAR": f"""<circle r="46" stroke-width="2" opacity=".55"/><circle r="28" stroke-width="2" opacity=".55"/><circle r="10" stroke-width="2" opacity=".55"/>
    <path d="M0,0 L34,-32" stroke-width="4"/><path d="M0,-46 A46,46 0 0 1 32.5,-32.5" stroke="{AMBER}" stroke-width="3" opacity=".9"/>
    <circle cx="34" cy="-32" r="5" fill="{AMBER}" stroke="none"/><circle r="4" fill="{CYAN}" stroke="none"/>""",
        "ARMOR-SOLAR": f"""<circle cy="-14" r="13" stroke="{AMBER}" stroke-width="4"/>
    <path d="M0,-40 v-6 M0,12 v6 M-26,-14 h-6 M26,-14 h6 M-18,-32 l-4,-4 M18,-32 l4,-4 M-18,4 l-4,4 M18,4 l4,4" stroke="{AMBER}" stroke-width="3"/>
    <path d="M-40,34 q10,-18 20,0 t20,0 t20,0 t20,0" stroke-width="4"/>""",
        "ARMOR-SERVER": f"""<rect x="-34" y="-40" width="68" height="24" rx="5"/><rect x="-34" y="-12" width="68" height="24" rx="5"/><rect x="-34" y="16" width="68" height="24" rx="5"/>
    <circle cx="-22" cy="-28" r="3" fill="{AMBER}" stroke="none"/><circle cx="-22" cy="0" r="3" fill="{AMBER}" stroke="none"/><circle cx="-22" cy="28" r="3" fill="{AMBER}" stroke="none"/>
    <path d="M-8,-28 h30 M-8,0 h30 M-8,28 h30" stroke-width="2" opacity=".6"/>""",
        "ARMOR-STUDIO": f"""<rect x="-42" y="-38" width="84" height="58" rx="6"/><path d="M-14,36 h28 M0,20 v16"/>
    <path d="M-32,10 l16,-18 l14,10 l16,-24 l16,14" stroke="{AMBER}" stroke-width="3.4"/>""",
        "ARMOR-ANDROID-CONTROL": f"""<rect x="-24" y="-46" width="48" height="90" rx="9"/><path d="M-6,-38 h12" stroke-width="3"/>
    <circle r="6" cy="-4" stroke-width="2" opacity=".6"/><circle r="15" cy="-4" stroke-width="2" opacity=".6"/><path d="M0,-4 L11,-15" stroke="{AMBER}" stroke-width="3"/>
    <circle cy="34" r="3" fill="{CYAN}" stroke="none"/>""",
        "ARMOR-SERVER-AI": f"""<path d="M-46,0 Q0,-44 46,0 Q0,44 -46,0 Z"/><circle r="15" stroke="{AMBER}" stroke-width="3.4"/><circle r="5" fill="{AMBER}" stroke="none"/>
    <path d="M-30,-30 l-6,-8 M0,-38 v-8 M30,-30 l6,-8" stroke-width="2" opacity=".6"/>""",
        "ARMOR-VOICE-AI": f"""<rect x="-13" y="-42" width="26" height="46" rx="13"/><path d="M-26,-6 a26,26 0 0 0 52,0 M0,20 v18 M-14,38 h28"/>
    <path d="M-42,-22 q-6,16 0,32 M42,-22 q6,16 0,32" stroke="{AMBER}" stroke-width="3"/>""",
        "ARMOR-HARDWARE": f"""<path d="M0,-44 L38,-22 V22 L0,44 L-38,22 V-22 Z"/><path d="M-38,-22 L0,0 L38,-22 M0,0 V44" stroke-width="2.4" opacity=".7"/>
    <circle r="5" fill="{AMBER}" stroke="none"/>""",
        "ARMOR-DEVOPS": f"""<circle r="16"/><circle r="6" stroke="{AMBER}" stroke-width="3"/>
    <path d="M0,-44 v14 M0,44 v-14 M-44,0 h14 M44,0 h-14 M-31,-31 l10,10 M31,31 l-10,-10 M31,-31 l-10,10 M-31,31 l10,-10" stroke-width="7"/>""",
        "ARMOR-DOCS": f"""<path d="M-42,-30 Q-20,-38 0,-26 Q20,-38 42,-30 V30 Q20,22 0,34 Q-20,22 -42,30 Z"/><path d="M0,-26 V34" stroke-width="2.4" opacity=".7"/>
    <path d="M-32,-14 q12,-4 22,4 M-32,0 q12,-4 22,4 M10,-10 q10,-8 22,-4 M10,4 q10,-8 22,-4" stroke="{AMBER}" stroke-width="2.4"/>""",
        "ARMOR-SIMULATOR": f"""<path d="M-14,-44 h28 M-8,-44 v26 L-38,36 Q-40,44 -32,44 H32 Q40,44 38,36 L8,-18 v-26"/>
    <path d="M-24,22 h48" stroke="{AMBER}" stroke-width="3"/><circle cx="-6" cy="10" r="3" fill="{AMBER}" stroke="none"/><circle cx="8" cy="-2" r="2.4" fill="{AMBER}" stroke="none"/><circle cx="4" cy="30" r="3.4" fill="{AMBER}" stroke="none"/>""",
        "ARMOR-COMMON": f"""<path d="M-14,-42 q-14,0 -14,14 v10 q0,10 -10,18 q10,8 10,18 v10 q0,14 14,14"/><path d="M14,-42 q14,0 14,14 v10 q0,10 10,18 q-10,8 -10,18 v10 q0,14 -14,14"/>
    <circle r="6" fill="{AMBER}" stroke="none"/><path d="M-10,0 h-2 M12,0 h-2" stroke="{AMBER}" stroke-width="3"/>""",
    }
    return g[name]


def emblem(name: str, scale: float = 1.0) -> str:
    """A shield with the drawing of the repository inside, in a glowing line style."""
    return f"""<g transform="scale({scale})" filter="url(#g)" {S} stroke="{CYAN}" stroke-width="4">
    <path d="M0,-84 L66,-58 V4 C66,48 34,72 0,88 C-34,72 -66,48 -66,4 V-58 Z"/>
    <g transform="scale(.78) translate(0 4)" stroke-width="4">
    {glyph(name)}
    </g>
  </g>"""


def defs() -> str:
    return f"""<defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%"><stop stop-color="{BG_FROM}"/><stop offset="1" stop-color="{BG_TO}"/></linearGradient>
    <filter id="g"><feGaussianBlur stdDeviation="4" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
  </defs>"""


def banner(name: str, tagline: str, tags: list[str]) -> str:
    tag_x = [105 + index * 150 for index in range(len(tags))]
    tagline = html.escape(tagline)
    tag_text = "".join(f'<text x="{x}" y="360">#{html.escape(tag)}</text>' for x, tag in zip(tag_x, tags))
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 400" role="img" aria-labelledby="title desc">
  <title id="title">{name}</title><desc id="desc">{name} | A.R.M.O.R. Autonomous Radar &amp; Multimodal Observation Range</desc>
  {defs()}
  <rect width="1200" height="400" fill="url(#bg)"/>
  <g fill="none" stroke="{CYAN}" stroke-width="1" opacity=".25"><path d="M0 100H200L250 150H600"/><path d="M1200 300H1000L950 250H600"/><path d="M1200 80H1040L1000 120H760"/></g>
  <g transform="translate(205 190)">{emblem(name)}</g>
  <text x="360" y="136" font-family="Arial,sans-serif" font-size="50" font-weight="bold" fill="#FFF" letter-spacing="8">A.R.M.O.R.</text>
  <text x="364" y="181" font-family="Arial,sans-serif" font-size="17" fill="{CYAN}" letter-spacing="4">AUTONOMOUS RADAR &amp; MULTIMODAL OBSERVATION RANGE</text>
  <text x="360" y="246" font-family="Arial,sans-serif" font-size="29" font-weight="bold" fill="#FFF">{name}</text>
  <text x="362" y="280" font-family="Arial,sans-serif" font-size="16" fill="{AMBER}" letter-spacing="3">{tagline}</text>
  <g font-family="monospace" font-size="12" fill="{CYAN}" opacity=".65">{tag_text}</g>
</svg>
"""


def icon(name: str) -> str:
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="-110 -110 220 220" role="img" aria-label="{name}">
  {defs()}
  <rect x="-110" y="-110" width="220" height="220" rx="36" fill="url(#bg)"/>
  {emblem(name, 0.95)}
</svg>
"""


# ---- the map of the family ------------------------------------------------------------------------------------------------------------------

# name -> (column, row) in the map, and the arrows (from, to) that show who feeds whom
POSITIONS = {
    "ARMOR-RADAR": (0, 0), "ARMOR-SOLAR": (0, 1), "ARMOR-SIMULATOR": (0, 2), "ARMOR-HARDWARE": (0, 3),
    "ARMOR-COMMON": (1, 1.5),
    "ARMOR-SERVER-AI": (2, 0), "ARMOR-SERVER": (2, 1.5), "ARMOR-VOICE-AI": (2, 3),
    "ARMOR-STUDIO": (3, 0.75), "ARMOR-ANDROID-CONTROL": (3, 2.25),
    "ARMOR-DEVOPS": (4, 0.75), "ARMOR-DOCS": (4, 2.25),
}
ARROWS = [("ARMOR-RADAR", "ARMOR-SERVER"), ("ARMOR-SOLAR", "ARMOR-SERVER"), ("ARMOR-SIMULATOR", "ARMOR-SERVER"), ("ARMOR-SERVER-AI", "ARMOR-SERVER"),
          ("ARMOR-VOICE-AI", "ARMOR-SERVER"), ("ARMOR-SERVER", "ARMOR-STUDIO"), ("ARMOR-SERVER", "ARMOR-ANDROID-CONTROL"), ("ARMOR-DEVOPS", "ARMOR-STUDIO")]
COLUMN_TITLES = ["FIELD", "CONTRACTS", "CORE", "CLIENTS", "OPERATIONS"]


def family_map() -> str:
    width, height, box_w, box_h = 1200, 560, 190, 62
    def centre(name: str) -> tuple[float, float]:
        column, row = POSITIONS[name]
        return 40 + column * 236 + box_w / 2, 110 + row * 110 + box_h / 2
    parts = [f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">
  <title id="title">A.R.M.O.R.</title><desc id="desc">The repositories of A.R.M.O.R. and who feeds whom</desc>
  {defs()}
  <rect width="{width}" height="{height}" fill="url(#bg)"/>
  <text x="600" y="46" text-anchor="middle" font-family="Arial,sans-serif" font-size="26" font-weight="bold" fill="#FFF" letter-spacing="6">A.R.M.O.R. FAMILY</text>"""]
    for index, title in enumerate(COLUMN_TITLES):
        parts.append(f'<text x="{40 + index * 236 + box_w / 2}" y="84" text-anchor="middle" font-family="monospace" font-size="13" fill="{CYAN}" opacity=".7" letter-spacing="3">{title}</text>')
    for source, target in ARROWS:
        (x1, y1), (x2, y2) = centre(source), centre(target)
        sx = x1 + box_w / 2 if x2 > x1 else x1 - box_w / 2
        tx = x2 - box_w / 2 if x2 > x1 else x2 + box_w / 2
        mid = (sx + tx) / 2
        parts.append(f'<path d="M{sx} {y1} C{mid} {y1}, {mid} {y2}, {tx} {y2}" fill="none" stroke="{CYAN}" stroke-width="1.6" opacity=".45"/>')
        parts.append(f'<circle cx="{tx}" cy="{y2}" r="3.4" fill="{AMBER}"/>')
    cx, cy = centre("ARMOR-COMMON")
    for name in POSITIONS:
        if name in ("ARMOR-COMMON", "ARMOR-DOCS", "ARMOR-DEVOPS"):
            continue
        x, y = centre(name)
        if name in ("ARMOR-SERVER-AI", "ARMOR-VOICE-AI", "ARMOR-SERVER", "ARMOR-STUDIO", "ARMOR-ANDROID-CONTROL"):
            continue
        parts.append(f'<path d="M{x + box_w / 2} {y} L{cx - box_w / 2} {cy}" fill="none" stroke="{GREEN}" stroke-width="1" stroke-dasharray="4 6" opacity=".35"/>')
    for name, (column, row) in POSITIONS.items():
        x, y = 40 + column * 236, 110 + row * 110
        is_common = name == "ARMOR-COMMON"
        parts.append(f'<g transform="translate({x} {y})"><rect width="{box_w}" height="{box_h}" rx="12" fill="#0d1a22" stroke="{AMBER if is_common else CYAN}" stroke-width="{2 if is_common else 1.4}" opacity=".95"/>'
                     f'<text x="{box_w / 2}" y="{box_h / 2 + 5}" text-anchor="middle" font-family="Arial,sans-serif" font-size="{13 if len(name) > 16 else 15}" font-weight="bold" fill="#FFF">{name}</text></g>')
    parts.append(f'<text x="600" y="{height - 26}" text-anchor="middle" font-family="monospace" font-size="12" fill="{GREEN}" opacity=".7">dashed: every message follows the contract of ARMOR-COMMON  ·  solid: who feeds whom</text>')
    parts.append("</svg>\n")
    return "\n  ".join(parts)


def outputs(root: Path) -> dict[Path, str]:
    files: dict[Path, str] = {root / "ARMOR-DOCS" / "brand" / "ARMOR_ICON.svg": icon("ARMOR-RADAR"), root / "ARMOR-DOCS" / "images" / "ARMOR_FAMILY.svg": family_map()}
    for name, (tagline, tags) in REPOS.items():
        target = root / name / "images"
        files[target / "ARMOR_BANNER.svg"] = banner(name, tagline, tags)
        files[target / "ARMOR_ICON.svg"] = icon(name)
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
