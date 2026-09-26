"""Language-neutral parts (badges, diagram, build and structure blocks) of the repositories whose README used to be written by hand.

Copyright (C) 2026 JuanenRac (Electro Hobby 3D). GPL-3.0-or-later.
"""
from __future__ import annotations

META = {
    "ARMOR-SERVER": {
        "emoji": "🛡️",
        "badges": [("Language", "TypeScript", "3178c6"), ("Runtime", "Node%2020%2B", "43853d"), ("Tests", "161%20passing", "2ea44f"), ("Maturity", "functional", "00E5FF")],
        "diagram": """```mermaid
flowchart LR
    N["Field nodes (ESP32-S3)"] -->|MQTT / HTTP + ingest token| S["ARMOR-SERVER"]
    G["Solar gateway nodes"] -->|MQTT / HTTP + ingest token| S
    C["IP cameras"] -->|RTSP / ONVIF| S
    S -->|"MJPEG, JSON, WebSocket"| U["ARMOR-STUDIO"]
    S -->|"MJPEG, JSON"| A["ARMOR-ANDROID-CONTROL"]
    S --> D[("data/: cameras.json (AES-GCM), media/, audit.log")]
```""",
        "build": """```powershell
npm install
npm run typecheck   # tsc --noEmit
npm test            # 161 tests: unit + full HTTP integration
npm run build       # dist/server.mjs
.\\run.bat           # development server with hot reload
```""",
        "structure": """```text
ARMOR-SERVER/
├── src/            server, app, config, context, store, persistence, events, rules, notify, contracts, mqtt, audit,
│   │               alarms, automations, users, site, solar
│   ├── http/       auth primitives
│   ├── routes/     sessions, cameras, media, ingest, history, devices, alarms, automations, site, solar
│   ├── devices/    the device model, kinds and MQTT bridge
│   ├── cameras/    model, vault, digest, ptz, rtsp, discovery, health, errors
│   └── media/      relay, evidence
├── tests/          unit tests + full HTTP integration suite
├── docs/           state machine, camera gateway, integration
├── data/           runtime state (ignored by Git)
└── images/         brand assets
```""",
    },
    "ARMOR-STUDIO": {
        "emoji": "🎛️",
        "badges": [("Language", "TypeScript", "3178c6"), ("UI", "React%2019", "61dafb"), ("Languages", "7", "00E5FF"), ("Tests", "176%20passing", "2ea44f"), ("Maturity", "functional", "00E5FF")],
        "diagram": """```mermaid
flowchart LR
    B["Browser"] -->|"static files"| H["tools/serve.mjs (static host)"]
    B -->|"HttpOnly session, JSON, MJPEG"| S["ARMOR-SERVER"]
    H -->|"/armor-config.json"| B
```""",
        "build": """```powershell
npm install
npm run dev         # http://127.0.0.1:5178 against a server on 127.0.0.1:8080
npm run typecheck
npm test            # 176 tests: designer geometry, settings, cameras, radar map, solar arithmetic, every menu in seven languages, static host
npm run build       # dist/
$env:ARMOR_SERVER_ORIGIN="http://192.168.0.180:18080"; node tools/serve.mjs   # serve the build
```""",
        "structure": """```text
ARMOR-STUDIO/
├── src/
│   ├── App.tsx, domain.ts, settings.ts, cameras.ts, hooks.ts, api.ts, config.ts, i18n.ts
│   ├── components/   camera, chrome, SiteMap
│   ├── views/        overview, monitoring, RadarView, AlarmsView, DevicesView, AutomationsView, InvertersView, BatteriesView, SystemView
│   ├── designer/     geometry, ops, model, Plan2D, Viewport3D, Toolbox, Inspector
│   ├── solarModel.ts, solarGraphics.tsx, solarText.ts   the arithmetic, the drawings and the words of the solar menus
│   └── ...           ConfigurationPanel, UsersPanel, MediaLibrary, HistoryView, SiteDesignerInteractive, StudioLogin, one *Text.ts per area (7 languages)
├── tools/            serve.mjs (+ tests)
├── docs/             security model
└── images/           brand assets
```""",
    },
    "ARMOR-ELECTRICAL": {
        "emoji": "⚡",
        "badges": [("Language", "C%2B%2B17", "00599c"), ("Meters", "PZEM--004T%20%2F%20017", "ffb020"), ("Checks", "135%2C789", "2ea44f"), ("Maturity", "scaffolding", "ff9800")],
        "diagram": "",
        "build": """```bash
cmake -S tests -B build/host && cmake --build build/host && ctest --test-dir build/host   # the meters (53 checks) and the switching rules (135,736)
build/host/emit_samples | python tests/check_samples.py                                     # the messages, against ARMOR-COMMON
```""",
        "structure": """```text
ARMOR-ELECTRICAL/
├── core/    pzem.hpp (frames of the PZEM meters), pzem_bus.hpp (the line), electrical_json.hpp (the message), interlock.hpp (the rules for switching), json.hpp
├── tests/   test_meters.cpp, test_interlock.cpp, emit_samples.cpp + check_samples.py (the messages against ARMOR-COMMON)
├── docs/    DESIGN, SAFETY, SWITCHING, PROTOCOLS, ELECTRICAL_MESSAGES, HARDWARE
└── images/  brand assets
```""",
    },
    "ARMOR-COMMON": {
        "emoji": "🧾",
        "badges": [("Language", "Python%203.11%2B", "3776ab"), ("Dependencies", "none", "2ea44f"), ("Vectors", "177", "00E5FF"), ("Maturity", "functional", "00E5FF")],
        "diagram": """```mermaid
flowchart LR
    S["JSON Schemas (source of truth)"] --> P["armor_common (Python validator)"]
    S --> G["generated TS + Kotlin types"]
    S --> V["conformance vectors"]
    V --> P
    V --> T["ARMOR-SERVER tests"]
    V --> X["ARMOR-SOLAR checks"]
    S --> O["OpenAPI 0.2.0"]
```""",
        "build": """```powershell
python -m pip install -e .
python -m unittest discover -s tests      # 19 tests, 177 conformance vectors
python tools/generate_types.py --check    # generated types are current
python tools/make_conformance.py          # regenerate the vectors after editing the case list
```""",
        "structure": """```text
ARMOR-COMMON/
├── src/armor_common/   contracts, schema (validator), envelope, schemas/*.json (telemetry, health, command, info, solar_inverter, solar_battery)
├── conformance/        accepted and rejected payloads shared by every implementation
├── generated/          TypeScript and Kotlin types (generated, do not edit)
├── openapi/            armor-server-0.2.0.yaml
├── tools/              armor_project_tool.py, generate_types.py, make_conformance.py
├── tests/              unit tests and conformance runner
└── docs/               contracts guide
```""",
    },
    "ARMOR-DOCS": {
        "emoji": "📚",
        "badges": [("Format", "Markdown", "083fa1"), ("Languages", "7", "00E5FF"), ("Maturity", "functional", "00E5FF")],
        "diagram": "",
        "build": """```bash
python tools/make_readmes.py --check      # the READMEs (7 languages) are current
python tools/make_brand.py --check        # the banners and icons are current
python tools/publication_check.py         # nothing private would leave with a publication
bash tools/check_all.sh                   # every repository's own tests, in one run
```""",
        "structure": """```text
ARMOR-DOCS/
├── docs/     CAPABILITY_MATRIX, ARCHITECTURE, SECURITY_BASELINE, PROJECT_CATALOG, INTERFACES, FIRST_VERTICAL_SLICE
├── tools/    make_readmes.py (+ readme_data/), make_brand.py, publication_check.py, clean_history.py, check_all.sh
├── brand/    the emblem
└── images/   this repository's banner and icon
```""",
    },
}
