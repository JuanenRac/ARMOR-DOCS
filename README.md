<p align="center">
  <img src="images/ARMOR_BANNER.svg" alt="ARMOR-DOCS banner" width="100%">
</p>

# 📚 ARMOR-DOCS

<p align="center">
  🇺🇸 <b>English</b> |
  <a href="README_spa.md">🇪🇸 Español</a> |
  <a href="README_fra.md">🇫🇷 Français</a> |
  <a href="README_ita.md">🇮🇹 Italiano</a> |
  <a href="README_deu.md">🇩🇪 Deutsch</a> |
  <a href="README_zho.md">🇨🇳 简体中文</a> |
  <a href="README_jpn.md">🇯🇵 日本語</a> |
  <a href="README_por.md">🇵🇹 Português</a>
</p>

### Canonical architecture, security baseline and the truth about what is proven

<p align="center">
  <img src="https://img.shields.io/badge/License-GPL%203.0-blue.svg" alt="GPL 3.0">
  <img src="https://img.shields.io/badge/Format-Markdown-083fa1.svg" alt="Format">
  <img src="https://img.shields.io/badge/Languages-8-00E5FF.svg" alt="Languages">
  <img src="https://img.shields.io/badge/Version-0.8.0.1-0f6cbd.svg" alt="Version">
  <img src="https://img.shields.io/badge/Maturity-established-2EA44F.svg" alt="Maturity">
</p>

---

**Honesty check - what runs today:** This repository documents interfaces and procedures that have been validated, and it says plainly what has not. Read the [capability matrix](docs/CAPABILITY_MATRIX.md) before believing any feature is "done": it says for each one whether it was only simulated, tested on a computer or verified on real hardware. The READMEs of the eighteen repositories are written from one source (`tools/readme_src/`) in eight languages, with the version and the maturity of each read from its own manifest, so they cannot say something different from the project.

---

## 📋 At a glance

| | |
|---|---|
| Version | `0.8.0.1` |
| Maturity | Established |
| Stack | Markdown / Mermaid |
| On real hardware | Not applicable: it is documentation; it records what the other repositories have run on real hardware |

## 🎯 Overview

<p align="center">
  <img src="images/ARMOR_FAMILY.svg" alt="A.R.M.O.R. family" width="100%">
</p>

* [Capability matrix](docs/CAPABILITY_MATRIX.md): for each capability, is it simulated, tested on a computer or verified on hardware?
* [Architecture](docs/ARCHITECTURE.md): networks, trust boundaries, time and ordering.
* [Security baseline](docs/SECURITY_BASELINE.md): the VLAN design, what the code enforces and what is still missing; and the [threat model](docs/THREAT_MODEL.md).
* [Project catalogue](docs/PROJECT_CATALOG.md): the eighteen repositories, their versions and how they depend on each other.
* [Interfaces](docs/INTERFACES.md): who produces and consumes each interface and where it is trusted.
* [First vertical slice](docs/FIRST_VERTICAL_SLICE.md): what the simulator-to-console test proves and what it does not.
* **Tools:** `make_readmes.py` writes the README of every repository in the eight languages from `readme_src/`, `make_catalog.py` writes the versions of the catalogue, `make_brand.py` its banner and icon, `publication_check.py` looks for anything private before a publication, `clean_history.py` makes a publishable copy of a repository and `sync_ci_tools.py` keeps the CI checks of the family equal.

## 🧩 Role in A.R.M.O.R.

ARMOR-DOCS is the family's memory: it is where the architecture, the security baseline and the capability matrix live, and the place that says, for every repository, what has really run on hardware. It also holds the tool that writes the READMEs of all eighteen repositories from one source, so that the eight languages cannot drift apart.

## 📂 Repository Structure

```text
ARMOR-DOCS/
├── docs/     CAPABILITY_MATRIX, ARCHITECTURE, SECURITY_BASELINE, PROJECT_CATALOG, INTERFACES, THREAT_MODEL, FIRST_VERTICAL_SLICE
├── tools/    make_readmes.py (+ readme_src/: the facts and the words of every repository in eight languages), make_catalog.py, make_brand.py, publication_check.py, clean_history.py, sync_ci_tools.py, check_all.sh
├── brand/    the emblem
└── images/   this repository's banner, icon and the family picture
```

## 🛠️ Development Environment

**Requirements:** Python 3.11+ for the tools

```bash
python tools/make_readmes.py --check      # the READMEs (8 languages) are current
python tools/make_catalog.py --check     # the versions and maturity of the catalogue are current
python tools/make_brand.py --check        # the banners and icons are current
python tools/publication_check.py         # nothing private would leave with a publication
bash tools/check_all.sh                   # every repository's own tests, in one run
```

## 🔗 Related Projects

**A.R.M.O.R.** (Autonomous Radar & Multimodal Observation Range) is a perimeter-security system made of independent repositories. Each one has its own version, its own tests and its own README; this is the family:

* **[ARMOR-COMMON](https://github.com/JuanenRac/ARMOR-COMMON)** - Message contracts, validators, conformance vectors and generated types
* **[ARMOR-RADAR](https://github.com/JuanenRac/ARMOR-RADAR)** - Field-node firmware for ESP32-S3 with three radars and its own web panel
* **[ARMOR-SOLAR](https://github.com/JuanenRac/ARMOR-SOLAR)** - Solar inverter and battery protocols and the messages of a gateway node
* **[ARMOR-ELECTRICAL](https://github.com/JuanenRac/ARMOR-ELECTRICAL)** - Electrical node: meters, the message of the network's readings and the rules for switching
* **[ARMOR-ALARM](https://github.com/JuanenRac/ARMOR-ALARM)** - Alarm node and panel: zones, arming, delays, siren and PIN, with the server or without it
* **[ARMOR-HMI](https://github.com/JuanenRac/ARMOR-HMI)** - Touch panel: the state of the system on a wall screen, arming and acknowledging, and the home of the voice assistant
* **[ARMOR-NETWORK](https://github.com/JuanenRac/ARMOR-NETWORK)** - The local network: its devices, the internet and what changes
* **[ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER)** - Central coordinator: telemetry, alarms, devices, solar readings and cameras
* **[ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO)** - Web console: cameras, radar, alarms, solar energy and the 2D/3D site designer
* **[ARMOR-ANDROID-CONTROL](https://github.com/JuanenRac/ARMOR-ANDROID-CONTROL)** - Android operator client with a live 2D/3D radar
* **[ARMOR-SERVER-AI](https://github.com/JuanenRac/ARMOR-SERVER-AI)** - Visual inference policy that explains its decisions and never actuates
* **[ARMOR-VISION](https://github.com/JuanenRac/ARMOR-VISION)** - Camera zones, masks and detection rules for the Jetson Orin NX
* **[ARMOR-VOICE-AI](https://github.com/JuanenRac/ARMOR-VOICE-AI)** - Offline voice intents with a confirmation that cannot be forged
* **[ARMOR-HARDWARE](https://github.com/JuanenRac/ARMOR-HARDWARE)** - Enclosures, electronics and the bench acceptance matrix
* **[ARMOR-DEVOPS](https://github.com/JuanenRac/ARMOR-DEVOPS)** - Deployment, the CM5 test bench, backup and TLS
* **[ARMOR-SIMULATOR](https://github.com/JuanenRac/ARMOR-SIMULATOR)** - Offline telemetry simulator with repeatable faults
* **[ARMOR-UPDATER](https://github.com/JuanenRac/ARMOR-UPDATER)** - Detects, installs and updates the ecosystem's own repositories
* **ARMOR-DOCS** (this repository) - Architecture, security baseline and the capability matrix

## 📚 Documentation & Community

Where to read more:

* [Capability matrix: what is proven and what is not](docs/CAPABILITY_MATRIX.md)
* [Project catalogue: versions and how the repositories depend on each other](docs/PROJECT_CATALOG.md)
* [Changelog of this repository](CHANGELOG.md)
* [License (GPL-3.0-or-later)](LICENSE)
* Questions, ideas and reports: electrohobby3d@gmail.com

## 👤 AUTHOR

**JuanenRac (Electro Hobby 3D)** · electrohobby3d@gmail.com

## 📜 LICENSE

GPL-3.0-or-later - see [LICENSE](LICENSE).
