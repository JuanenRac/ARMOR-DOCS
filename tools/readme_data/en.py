"""English: the words around every README, the one-line description of each repository, and the texts of the repositories that changed since the first
generation (the rest are in legacy.py).

Copyright (C) 2026 JuanenRac (Electro Hobby 3D). GPL-3.0-or-later.
"""
from __future__ import annotations

UI = {
    "overview": "Overview", "structure": "Repository Structure", "dev": "Development Environment", "architecture": "Architecture",
    "related": "Related Projects", "community": "Documentation & Community", "author": "AUTHOR", "license": "LICENSE",
    "honesty": "Honesty check - what runs today", "license_text": "GPL-3.0-or-later - see [LICENSE](LICENSE).",
    "family": "**A.R.M.O.R.** (Autonomous Radar & Multimodal Observation Range) is a perimeter-security system made of independent repositories. Each one has its own version, its own tests and its own README; this is the family:",
    "here": "this repository",
    "docs_intro": "Where to read more:",
    "doc_matrix": "Capability matrix: what is proven and what is not",
    "doc_catalog": "Project catalogue: versions and how the repositories depend on each other",
    "doc_changelog": "Changelog of this repository",
    "doc_license": "License (GPL-3.0-or-later)",
    "contact": "Questions, ideas and reports: electrohobby3d@gmail.com",
}

RELATED = {
    "ARMOR-COMMON": "Message contracts, validators, conformance vectors and generated types",
    "ARMOR-RADAR": "Field-node firmware for ESP32-S3 with three radars and its own web panel",
    "ARMOR-SOLAR": "Solar inverter and battery protocols and the messages of a gateway node",
    "ARMOR-SERVER": "Central coordinator: telemetry, alarms, devices, solar readings and cameras",
    "ARMOR-STUDIO": "Web console: cameras, radar, alarms, solar energy and the 2D/3D site designer",
    "ARMOR-ANDROID-CONTROL": "Android operator client with a live 2D/3D radar",
    "ARMOR-SERVER-AI": "Visual inference policy that explains its decisions and never actuates",
    "ARMOR-VOICE-AI": "Offline voice intents with a confirmation that cannot be forged",
    "ARMOR-HARDWARE": "Enclosures, electronics and the bench acceptance matrix",
    "ARMOR-DEVOPS": "Deployment, the CM5 test bench, backup and TLS",
    "ARMOR-SIMULATOR": "Offline telemetry simulator with repeatable faults",
    "ARMOR-DOCS": "Architecture, security baseline and the capability matrix",
}

TEXT = {
    "ARMOR-SOLAR": {
        "tagline": "Solar gateway node: reads inverters and batteries through up to ten serial ports (ESP32-S3 firmware, its web panel and the protocol library)",
        "honest": "**Maturity: scaffolding.** The firmware builds in the ESP-IDF 5.4.2 container, its core (the settings, the exchange with each kind of equipment, the arithmetic of the emulated UART: 697 checks) is tested on a computer with stand-in equipment, the messages it makes are accepted by ARMOR-COMMON and the panel was exercised in a browser against a stand-in node. **It has never run on a board and no inverter or battery has been connected**: the Wi-Fi, the panel over TLS, the update, the hardware and emulated UARTs and the formats of the protocols (written from public documents and from memory) are untried. The ANT-BMS frames in its tests were captured by other people on their own units: this project has not read one itself.",
        "bullets": [
            "**Two boards, one firmware:** an ESP32-S3-WROOM-1 N16R8 on Wi-Fi (the default) and the Waveshare ESP32-S3-ETH on its Ethernet cable (DHCP or a fixed address; its own Wi-Fi network is kept to reach it from a phone). The image is chosen when it is built (`tools/build_node.sh generic s3-wifi` or `generic s3-eth`); the pin table, the default pins of the ports and the way in follow the board, and an image is only for its own board. Both build and are host-tested; neither has run on a board.",
            "**The firmware of the node** (ESP32-S3-WROOM-1 N16R8 on Wi-Fi, or the Waveshare ESP32-S3-ETH on its cable): ten serial ports, three hardware UARTs and seven emulated ones (up to 19200 baud), each independent and each reading an inverter, a battery or a raw monitor, so a node may read only inverters, only batteries or a mix.",
            "**The node's web panel,** the radar nodes' too: set-up with a code shown on the USB console, login and users, Wi-Fi (station and access point), broker, update over the air with rollback, log, HTTPS, and the pages of the ports (with what each one hears, for protocols not decoded yet) and of the readings, in seven languages.",
            "**Voltronic / MPP Solar inverters** (Axpert, PIP, InfiniSolar and clones), RS232 at 2400 baud: the frames and their CRC, and the readings `QPIGS` (grid, output, battery, PV, status bits), `QMOD` (mode), `QPIWS` (warnings and faults by name) and `QPIRI` (ratings). Only reading commands can be built: a setting changes how the house is fed. Three dialects, chosen on the port or found by it (*auto*): PI30, REVO (another `QPIGS`, checksum replies) and PI18 (`^P005GS`: InfiniSolar V, LV5048, SunGoldPower), read only.",
            "**Pylontech batteries** (US2000, US3000, US5000): the console's `pwr` table (every module's voltage, current, temperatures and state of charge), `bat <n>` (the voltage and temperature of every cell) and `info <n>` (model, remaining and full capacity, cycles), summarised as one stack with its total capacity and energy, and the RS485 frame with its two checks. The formats are written from memory of the public console and may differ between firmwares. The columns are found by the header's names (the US5000 V2.3 layout with its Id columns, MosTempr and SysAlarm.St included), the remaining charge and the balancing come from `bat`, and the model, rated capacity and cycles from `info` and `stat`, asked once and kept for half an hour.",
            "**The messages of the node** (`armor/solar/<node>/<device>/state`, one per inverter or battery stack), defined in ARMOR-COMMON with schemas and conformance vectors; what the ports make is checked against them.",
            "**ANT-BMS batteries** (the black boards of home-made packs, 7S to 32S), 3.3 V UART at 19200 baud: both protocols of its firmware (the node asks in one and then in the other and keeps to the one that answers), with the cells, temperatures, state of charge, current, capacities and the states of the MOSFETs and the balancer, checked against frames captured on four real models. Reading only: its write commands can disconnect a battery under load. A button on the ports page also reads the BMS's model, version and 56 protection and balancing settings (newer protocol), read only.",
            "**Not yet:** the ANT-BMS's Bluetooth link (the node uses the cable, the more stable of the two) and a run on a real board with real equipment.",
        ],
        "note": "See the [firmware guide](docs/NODE_FIRMWARE.md) (the board, the ports, the first start and the bench checklist) and the [wiring notes](docs/NODE_HARDWARE.md).",
    },
    "ARMOR-DEVOPS": {
        "bullets_replace": {
            'Devices on the bench broker': '**Devices and readings on the bench broker:** the server may listen on and command `armor/device/#` and read `armor/node/+/info` and `armor/solar/#`; `scripts/mqtt_identity.sh add device NAME` gives one device its own topics and `add bridge NAME` a Zigbee2MQTT or Shelly bridge all of them.',
        },
    },
    "ARMOR-SERVER": {
        "tagline": "Central security coordinator: telemetry ingress, alarms, devices, solar readings and the camera gateway",
        "honest": "Every route, session, encryption and evidence rule below is real and covered by tests (`npm test`, 161 tests, including a full HTTP integration suite against an isolated server). It has run against a real MQTT broker on the CM5 (with scripts, not field-node firmware), and has streamed live video, saved a snapshot and recorded from five real IP cameras through FFmpeg. What is **not** proven yet: ONVIF against a real ONVIF camera, PTZ on every camera firmware (it works on the Hi3510 unit), any Jetson hardware, and the solar routes against a real gateway node (they are tested with generated readings).",
        "intro": "**ARMOR-SERVER** is the trusted centre of A.R.M.O.R. Field nodes publish radar, light and health observations; this service validates them, keeps the last known state of every node, and serves that state to the Studio console and the Android client. It also owns everything that touches a camera, so that **no browser and no phone ever holds a camera password or an RTSP address**.",
        "bullets": [
            "**Validated ingest:** HTTP and MQTT observations are checked at the boundary (identifier, timestamps, lux range, at most 15 tracks) before they reach the state projection.",
            "**Honest node state:** a node that stops talking is shown as *stale* and *offline* after a configurable window, never as online on old data. Disarming clears a high alert at once.",
            "**Camera gateway:** encrypted camera vault, ONVIF / Hi3510 / PSIA PTZ, RTSP path discovery, one shared FFmpeg relay per camera, snapshots and MP4 recording, and a watchdog that turns a camera that stops answering into an event and, while armed, an alarm.",
            "**Evidence library:** oldest-first retention by age and size, **protected evidence** that is never pruned, and a SHA-256 for chain of custody. One audit line per security-relevant action, with credentials scrubbed.",
            "**State that survives:** the security mode and every node's last observation are restored after a restart (a restart never silently disarms the perimeter). Every alert-level, node-status and mode change is kept in an event history.",
            "**Alarm output:** high alerts and, while armed, silent or offline nodes go to MQTT `armor/server/alert` and an optional HMAC-signed webhook; a dwell time before HIGH and ignore zones are tuned from Studio.",
            "**Users:** names and passwords (scrypt hashes), an `admin` role that manages users and an `operator` role that operates; a changed password or role ends that user's other sessions.",
            "**Devices, alarms and automations:** smoke, gas, flood, door, window, motion, climate, plug, light, siren and lock devices over MQTT or an authenticated push, with normalised state, availability and commands; alarms with a raised / acknowledged / cleared lifecycle; rules that switch devices when something happens; arm and disarm from a signed-in session; and the site design kept on the server for every client.",
            "**Solar readings:** inverters and battery stacks (with each cell and the capacities) arrive by HTTP or MQTT, are validated by the shared contract, kept with a history (a sample every 30 s for a day) and totals, marked stale after two minutes, and raise four alarms (inverter fault, battery low, battery alarm, device silent).",
        ],
        "sections": [
            {"title": "Security model", "bullets": [
                "Four separate secrets: **ingest** (posting telemetry, health and solar readings), **control** (arm / disarm, events), **operator** (automation) and the **Studio login**; each is compared in constant time and none stands in for another.",
                "Every route that configures, moves, captures, records, protects or deletes needs an operator. Live video needs an operator or a short-lived stream ticket tied to one camera.",
                "Camera passwords live only in `data/cameras.json`, AES-256-GCM encrypted, and no API returns them; ONVIF addresses must stay on the camera's host and redirects are refused.",
                "Studio sessions are HttpOnly and SameSite=Strict for 8 hours, login is rate limited and errors never carry a stack trace.",
                "The server listens on 127.0.0.1 unless `ARMOR_HOST` is set on purpose, and then a Studio password shorter than 12 characters is refused.",
            ]},
            {"title": "API", "bullets": [
                "Public: `GET /healthz`. For an operator: status, information, cameras, media, history, rules, devices, alarms, automations, the site design, and `GET /api/v1/solar` with its history.",
                "For the field nodes and the gateways: `POST /api/v1/telemetry`, `/health` and `/solar` with the ingest token, and the MQTT topics `armor/node/#` and `armor/solar/#`. Events reach the consoles by the WebSocket `/api/v1/events`.",
                "Every route, its access rule and its schema is in the OpenAPI file of [ARMOR-COMMON](../ARMOR-COMMON), and a test checks that no route is missing from it.",
            ]},
            {"title": "Configuration", "bullets": [
                "Copy `.env.example` to `.env` (ignored by Git), or let `run.bat` / `run.sh` generate random secrets on the first run.",
                "Required: `ARMOR_INGEST_TOKEN` and `ARMOR_CONTROL_TOKEN` (24 characters or more, all different) and `ARMOR_STUDIO_USERNAME` / `ARMOR_STUDIO_PASSWORD` (the first administrator).",
                "Common: `ARMOR_HOST` / `ARMOR_PORT`, `ARMOR_DATA_DIR`, `ARMOR_FFMPEG_PATH` (live video and capture), `ARMOR_MQTT_URL`, `ARMOR_STUDIO_ORIGIN`, `ARMOR_NODE_STALE_AFTER_S`, `ARMOR_CAMERA_CHECK_S`, `ARMOR_ALERT_DWELL_MS`, `ARMOR_ALERT_WEBHOOK_URL` and `ARMOR_COOKIE_SECURE` (set it to `1` behind TLS).",
            ]},
        ],
        "note": "To install on the CM5 test bench (isolated from every other project, own user, own ports) see [ARMOR-DEVOPS](../ARMOR-DEVOPS).",
    },
    "ARMOR-STUDIO": {
        "tagline": "Operations and design console: cameras, radar, alarms, solar energy, evidence and the site plan",
        "honest": "Studio talks to [ARMOR-SERVER](../ARMOR-SERVER) and is covered by 201 unit tests (settings parsing, camera merging, the arithmetic of the solar charts, every menu rendered in the seven languages, the static host). What has **not** been proven is live video and PTZ against every real camera, the solar menus with a real inverter or battery, and a formal accessibility or usability review. While the server cannot be reached Studio shows demonstration data and says so in the top bar.",
        "intro": "**ARMOR-STUDIO** is the operator's console. It never holds a camera password, an RTSP address or a token: it signs in to the server with a username and password, receives an 8-hour **HttpOnly** session, and everything privileged travels through that session.",
        "bullets": [
            "**Camera monitor:** 1, 2, 4, 6, 8, 9, 12 or 16 tiles that fit their frame (16:9, the whole matrix visible, no cropping), a maximized view with a bounded PTZ pad, snapshot and MP4 record; a **record library** to filter, preview, play, protect and delete evidence.",
            "**Alarms, devices and automations:** what needs a person right now with acknowledge and the closed record; smoke, gas, flood, door, window, motion, climate, plug, light, siren and lock devices over Wi-Fi, Zigbee, Bluetooth or a wire (presets for Zigbee2MQTT, Tasmota and Shelly); rules that switch devices when something happens; a big arm / disarm button.",
            "**Solar energy:** the *Inverters* menu draws the house as an animated energy flow (panels, grid, inverter, battery and load, with dashes that run faster for more power), gauges, readings, warnings in words and history charts; the *Batteries* menu shows each stack with a liquid level, its **capacities** (remaining and full, Ah and kWh, cycles, model), each module and **every cell** as a bar with its voltage and the spread in millivolts, and charts of charge, voltage, current, cell range and temperature.",
            "**Overview and system:** the state of the perimeter, one tile per part, a live map of the design with every device, and a system page with the audit trail for an administrator.",
            "**Radar:** a live map drawn from your site design (terrain, buildings, cameras, radars and their coverage) with the targets each radar reports, their recent path and the ignore zones; live node state, with silent nodes shown as *stale*; each node's own panel is one click away.",
            "**Site designer:** draw the terrain (rectangle or any shape, with typed lengths), place buildings of several floors with five kinds of roof, doors and windows at any floor and height, lamps, chimneys, solar panels, antennas, pillars, masts, roads and paths, then cameras and radars anywhere; a CAD-style 2D plan and a 3D view you can orbit, cut floor by floor and edit; undo and redo.",
            "**Configuration:** server address, cameras (ONVIF/RTSP), discovery, users (your account and, for an administrator, the list of users, roles and passwords), theme and language; a portable site export **without credentials**.",
            "**Seven languages** (English, Spanish, German, French, Italian, Japanese, Chinese) and eleven themes, the default one called *Armor*.",
            "**Declare your equipment:** in the Inverters and Batteries menus you add each inverter or battery stack with its name, model (Voltronic, MPP Solar, Pylontech US2000 / US3000 / US5000, ANT-BMS), connection (RS232, RS485, USB, CAN, Wi-Fi) and gateway node; it waits for its first real reading, and *Show example readings* lets you try the menu meanwhile.",
            "**Electrical Designer:** draw the house's electrical diagram (grid, meter, protections, transfer switches, distribution, PV, inverters, batteries and loads, AC and DC) with ports and wires, group it in panels, tie inverters and batteries to the solar devices the server reads to see their live values, and let the checks review it (two sources on one line, breakers and cables against the current, missing protections, DC voltages). The drawing is kept on the server; it is a drawing: nothing switches or measures anything yet.",
        ],
        "sections": [
            {"title": "Security model", "bullets": [
                "**No secrets in the browser.** Camera passwords are entered once, sent to the server and shown afterwards only as a masked \"stored\" state. Site exports drop usernames and credential flags.",
                "**Stored settings are untrusted input.** They are parsed value by value: an invalid origin, theme, language or shape is dropped, positions are clamped and lists are capped.",
                "**No third-party requests.** Fonts are local stacks; the static host sends `Content-Security-Policy: default-src 'self'` limited to the configured server, `frame-ancestors 'none'`, `nosniff` and `no-referrer`.",
                "Live video is shown only through a stream address the server issues to an operator.",
            ]},
        ],
        "note": "`tools/serve.mjs` reads `ARMOR_STUDIO_HOST` (default `127.0.0.1`), `ARMOR_STUDIO_PORT` (`5178`), `ARMOR_STUDIO_DIST` and `ARMOR_SERVER_ORIGIN`. To install the whole stack on the CM5 test bench see [ARMOR-DEVOPS](../ARMOR-DEVOPS).",
    },
    "ARMOR-COMMON": {
        "tagline": "Message contracts, validation and the shared project launcher",
        "honest": "The schemas, the Python validator, the 147 shared conformance vectors, the generated TypeScript and Kotlin types and the shared project launcher are real and tested (19 tests). The Kotlin file is generated but **not yet consumed** by ARMOR-ANDROID-CONTROL, and the `set_thresholds` command carries a single `sensitivity` field because the real radar parameters are not defined until firmware exists.",
        "intro": "**ARMOR-COMMON** owns what every A.R.M.O.R. message means. Radar nodes, solar gateway nodes and the simulator produce these messages; the server, the visual AI and the voice service consume them. If two projects disagree about a field, this repository decides.",
        "bullets": [
            "**One source of truth:** JSON Schemas in `src/armor_common/schemas/` for telemetry, health, command, node information and the two solar messages (inverter, battery with cells and capacities). Unknown fields are rejected everywhere.",
            "**A validator that cannot skip a rule:** it interprets the schema directly and refuses a schema that uses a keyword it does not implement.",
            "**Conformance vectors:** 147 accepted and rejected payloads run by every implementation (Python here, TypeScript in ARMOR-SERVER, the checks of ARMOR-SOLAR), so drift fails a build.",
            "**Generated clients:** TypeScript and Kotlin types come from the schemas (`tools/generate_types.py --check` keeps them current).",
            "**HTTP contract:** `openapi/armor-server-0.2.0.yaml` describes every server route, its access rule and its schema.",
            "**Shared launcher:** `tools/armor_project_tool.py` gives every repository of the family the same `build`, `build-test` and `run` workflow.",
        ],
        "sections": [],
        "note": "Broker topics: `armor/node/{node_id}/telemetry | health | command | info` and `armor/solar/{node_id}/{device}/state`. See the [contracts guide](docs/CONTRACTS.md). The shared launcher creates an ignored `.env` on the first ARMOR-SERVER run with random secrets and a random administrator password; nothing is printed or committed.",
    },
    "ARMOR-DOCS": {
        "tagline": "Canonical architecture, security baseline and the truth about what is proven",
        "honest": "This repository documents interfaces and procedures that have been validated, and it says plainly what has not. Read the [capability matrix](docs/CAPABILITY_MATRIX.md) before believing any feature is \"done\": it says for each one whether it was only simulated, tested on a computer or verified on real hardware.",
        "intro": "",
        "bullets": [
            "[Capability matrix](docs/CAPABILITY_MATRIX.md): for each capability, is it simulated, local or verified on hardware?",
            "[Architecture](docs/ARCHITECTURE.md): networks, trust boundaries, time and ordering.",
            "[Security baseline](docs/SECURITY_BASELINE.md): the VLAN design, what the code enforces and what is still missing.",
            "[Project catalogue](docs/PROJECT_CATALOG.md): the twelve repositories, their versions and how they depend on each other.",
            "[Interfaces](docs/INTERFACES.md): who produces and consumes each interface and where it is trusted.",
            "[First vertical slice](docs/FIRST_VERTICAL_SLICE.md): what the simulator-to-console test proves and what it does not.",
            "**Tools:** `make_readmes.py` writes the README of every repository in the seven languages, `make_brand.py` its banner and icon, `publication_check.py` looks for anything private before a publication and `clean_history.py` makes a publishable copy of a repository.",
        ],
        "sections": [],
        "note": "The audits of the family (in Spanish) are kept in this repository's root.",
    },
}
