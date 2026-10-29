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
  <img src="https://img.shields.io/badge/License-GPL%203.0--or--later-blue.svg" alt="GPL 3.0 or later">
  <img src="https://img.shields.io/badge/Format-Markdown-083fa1.svg" alt="Format">
  <img src="https://img.shields.io/badge/Languages-8-00E5FF.svg" alt="Languages">
  <img src="https://img.shields.io/badge/Tests-199%20passing-2ea44f.svg" alt="Tests">
  <img src="https://img.shields.io/badge/Version-0.8.1.3-0f6cbd.svg" alt="Version">
  <img src="https://img.shields.io/badge/Maturity-established-2EA44F.svg" alt="Maturity">
</p>

---

**Honesty check - what runs today:** This repository documents interfaces and procedures that have been validated, and it says plainly what has not. Read the [capability matrix](docs/CAPABILITY_MATRIX.md) before believing any feature is "done": it says for each one whether it was only simulated, tested on a computer or verified on real hardware. The READMEs of the nineteen repositories are written from one source (`tools/readme_src/`) in eight languages, with the version and the maturity of each read from its own manifest, so they cannot say something different from the project.

---

## 📋 At a glance

| | |
|---|---|
| Version | `0.8.1.3` |
| Maturity | Established |
| Role | Documentation hub: architecture, security baseline, capability matrix, and the tools that write the READMEs, catalogue and banners |
| Stack | Python 3.11+ (tools, standard library), Markdown |
| Tests | 199 (`python -m unittest discover -s tests`, about a minute) |
| Interfaces | `make_readmes.py`, `make_catalog.py`, `make_brand.py`, `publication_check.py`, `clean_history.py`, `sync_ci_tools.py`, `check_all.sh` |
| Runs on | Any computer with Python; the repositories of the family next to this one |
| On real hardware | Not applicable: it is documentation; it records what the other repositories have run on real hardware |
| License | GPL-3.0-or-later |

**Jump to:** [Overview](#-overview) · [Architecture](#-architecture) · [Security](#-security--safety) · [Interfaces](#-interfaces) · [Quick start](#-quick-start) · [Testing](#-testing) · [Troubleshooting](#-troubleshooting) · [Structure](#-repository-structure) · [Related](#-related-projects)

## 🚦 Project status

Each line is one part of this repository and the light says how far it is today. It is written from what the repository can show (tests, builds, runs), not from what is planned.

🟢 Done and verified · 🟡 Works, with known limits · 🟠 Partly done or not verified yet · 🔴 Not done or not working

| Area | State | What it means here |
|---|---|---|
| Software | 🟢 | The generators for the READMEs, the banners, the catalogue and the capability matrix, and the CI tools copied into every repository, run and are tested. |
| Tests | 🟢 | The 199 tests of the tools pass (`python -m unittest discover -s tests`): the publication check, the history cleaner, the README, catalogue and brand generators, the copy of the CI tools and the shared workflow tool. |
| Automatic checks | 🟢 | Every push checks that the READMEs, the banners and the catalogue are up to date and that every repository of the registry has its status table. |
| Integration | 🟢 | The READMEs of all the repositories are written from one source with the version and the maturity of each read from its own manifest. |
| Documentation | 🟢 | The capability matrix says for each feature whether it was only simulated, tested on a computer or verified on real hardware; the eight languages and the changelog are up to date. |

## 🎯 Overview

<p align="center">
  <img src="images/ARMOR_FAMILY.svg" alt="A.R.M.O.R. family" width="100%">
</p>

* [Capability matrix](docs/CAPABILITY_MATRIX.md): for each capability, is it simulated, tested on a computer or verified on hardware?
* [Architecture](docs/ARCHITECTURE.md): networks, trust boundaries, time and ordering.
* [Security baseline](docs/SECURITY_BASELINE.md): the VLAN design, what the code enforces and what is still missing; and the [threat model](docs/THREAT_MODEL.md).
* [Project catalogue](docs/PROJECT_CATALOG.md): the nineteen repositories, their versions and how they depend on each other.
* [Interfaces](docs/INTERFACES.md): who produces and consumes each interface and where it is trusted.
* [First vertical slice](docs/FIRST_VERTICAL_SLICE.md): what the simulator-to-console test proves and what it does not.
* **Tools:** `make_readmes.py` writes the README of every repository in the eight languages from `readme_src/`, `make_catalog.py` writes the versions of the catalogue, `make_brand.py` its banner and icon, `publication_check.py` looks for anything private before a publication, `clean_history.py` makes a publishable copy of a repository and `sync_ci_tools.py` keeps the CI checks of the family equal.

## 🧩 Role in A.R.M.O.R.

ARMOR-DOCS is the family's memory: it is where the architecture, the security baseline and the capability matrix live, and the place that says, for every repository, what has really run on hardware. It also holds the tool that writes the READMEs of all nineteen repositories from one source, so that the eight languages cannot drift apart.

| It talks to | How | What for |
|---|---|---|
| Every repository of the family | their `armor.project.json` and their README files | the tools read the version and the maturity and write the README, the banner and the CI copies |
| ARMOR-COMMON | `registry/repositories.json` | the one list of the repositories of the family, read by `registry.py` |
| The person who publishes | `publication_check.py`  `clean_history.py` | what would leak, and a copy of one commit that can be published |

## 🏛️ Architecture

<p align="center">
  <img src="images/architecture.svg" alt="ARMOR-DOCS architecture: what the tools read, the tools themselves and what they write in every repository" width="100%">
</p>

## 🔒 Security & Safety

| Threat | Defence |
|---|---|
| Publishing something private | `publication_check.py` reads only git (tracked files and history, never ignored files) and never prints the secret. BLOCK: a private key, a public IP address, a personal e-mail address, a tracked `secrets/` or `.env`, a commit with a co-author or an AI trailer, a commit author other than the project's; REVIEW: a line that looks like a literal password or token; it exits 1 on any BLOCK |
| A history with leftovers | `clean_history.py` makes a publishable copy of a repository with a single commit made by the project's author |
| Claiming more than has been proven | `docs/CAPABILITY_MATRIX.md` has three levels (Simulated, Local, Verified) plus None, Absent and Local-not-activated; only the Verified rows have touched hardware (the CM5 test bench in daily use) |
| A README that says something else than the project | The version and the maturity of each README are read from its own manifest; every push checks that the READMEs, the banners and the catalogue are current and that every repository of the registry has its status table |

The security documents of the family are [docs/SECURITY_BASELINE.md](docs/SECURITY_BASELINE.md) (the VLAN design, what the code enforces and what is still missing) and [docs/THREAT_MODEL.md](docs/THREAT_MODEL.md). Nothing here proves the absence of a secret.

## 🔌 Interfaces

| Route | Auth | What it does |
|---|---|---|
| `python tools/make_readmes.py [--check]` | - | writes the README of every repository in eight languages from `tools/readme_src/`; `--check` fails when one is out of date. It rewrites every file: change the source, never the READMEs |
| `python tools/make_catalog.py [--check]`  `make_brand.py [--check]` | - | the versions and maturity of `docs/PROJECT_CATALOG.md`, and the banners and icons |
| `python tools/publication_check.py [REPO] [--no-history] [--ref=BRANCH]` | - | what would leak if the repositories were published; exits 1 on BLOCK |
| `python tools/clean_history.py` | - | a publishable copy of a repository with one commit |
| `python tools/sync_ci_tools.py [--check]` | - | copies the shared CI checks and the launcher into every repository; `--check` fails when a copy has drifted |
| `bash tools/check_all.sh [--android] [--compose]` | - | the tests of every repository in one run; a check without its tool is SKIP, never PASS |

The source of each README is `tools/readme_src/repos/<REPOSITORY>.py` (the facts that do not depend on the language, and the words of the eight languages), with `ui.py` for the words around every README and `shots.py` for the captures. `tools/registry.py` reads the list of repositories of ARMOR-COMMON. See also [docs/INTERFACES.md](docs/INTERFACES.md) and [docs/SETUP_CODE.md](docs/SETUP_CODE.md).

## 🚀 Quick start

**Requirements:** Python 3.11+ for the tools (standard library only); the repositories of the family next to this one for the checks that read them.

```bash
python tools/make_readmes.py --check  # the READMEs (8 languages) are current
python tools/make_catalog.py --check  # the versions and maturity of the catalogue are current
python tools/make_brand.py --check    # the banners and icons are current
python tools/publication_check.py     # nothing private would leave with a publication
bash tools/check_all.sh               # every repository's own tests, in one run
python -m unittest discover -s tests  # 199 tests of these tools; they need no other repository
```

## 🧪 Testing

| Area | What it covers |
|---|---|
| The README generator | `test_make_readmes.py`, `test_verbatim_readmes.py`: the eight languages and the sections of every repository |
| Catalogue and brand | `test_make_catalog_and_brand.py`, `test_repository_registry.py` |
| Publication | `test_publication_check.py`, `test_clean_history.py`: what is BLOCK and REVIEW, and the one-commit copy |
| CI tools and launcher | `test_ci_validate.py`, `test_sync_ci_tools.py`, `test_project_tool.py`, `test_check_all_script.py` |

GitHub Actions runs the A.R.M.O.R. baseline on every push and pull request: the validation of the manifest, version, changelog and README parity, then the project's own build and tests.

## 🏗️ Build & Release

There is nothing to compile. The version lives in `armor.project.json` and in the README badge (read from the manifest); each version has its entry in [CHANGELOG.md](CHANGELOG.md). Releases are published on GitHub.

## 🩺 Troubleshooting

| You see | Because | Do |
|---|---|---|
| `READMEs out of date:` + a list | a source of `tools/readme_src/` changed, or a manifest did, and the READMEs were not written again | run `python tools/make_readmes.py`, look at what changed in each repository and commit there |
| `Status tables incomplete:` | a repository of the registry has a status table without the expected rows or colours | complete `FACTS["status"]` and the notes in its source |
| A check says SKIP | its tool or the repository next to this one is missing; a check without its tool is never PASS | install the tool or clone the repository next to this one |
| `publication_check.py` BLOCK | something that must not go public was found (it shows the file, the line and the kind, never the value) | remove it, and use `clean_history.py` if it is in the history |

## 📂 Repository Structure

<p align="center">
  <img src="images/repository-structure.svg" alt="Repository structure of ARMOR-DOCS" width="100%">
</p>

<details>
<summary>Text version of the tree</summary>

```text
ARMOR-DOCS/
├── tools/
│   ├── make_readmes.py                          the READMEs, from one source, in eight languages
│   ├── readme_src/                              the facts and the words of each repository
│   ├── make_catalog.py make_brand.py            the catalogue; the banners and icons
│   ├── brand_banner.py registry.py              the banner drawing; the list of ARMOR-COMMON
│   ├── publication_check.py                     nothing private leaves with a publication
│   ├── clean_history.py sync_ci_tools.py        a publishable copy; equal CI checks
│   ├── check_all.sh                             every repository's tests in one run
│   ├── armor_ci_validate.py                     the CI check every repository carries
│   ├── armor_project_tool.py pretty_run.py      the launcher and its live panel
│   ├── make_architecture.py make_structure.py   the two pictures of the READMEs
│   └── universal_readme_check.py                the layout check of the READMEs
├── docs/                                        CAPABILITY_MATRIX, ARCHITECTURE, SECURITY_BASELINE, THREAT_MODEL, PROJECT_CATALOG, INTERFACES, FIRST_VERTICAL_SLICE, SETUP_CODE
├── tests/                                       the tests of these tools
├── brand/                                       the emblem
├── images/                                      banner, icon, the family picture and the pictures of this README
├── .github/                                     CI workflow, dashboard notice, issue and pull-request templates
├── armor.project.json                           manifest: version, role, maturity
├── CHANGELOG.md                                 what changed in each version
├── run.sh run.bat                               start, shared workflow
├── build.sh build.bat                           build and test, shared workflow
├── build-test.sh build-test.bat                 build, test and package
├── test.sh test.bat                             only the tests, never the version
└── SECURITY.md SUPPORT.md CONTRIBUTING.md CODE_OF_CONDUCT.md LICENSE
```

</details>

## 🗺️ Roadmap & Known limits

**Known limits today**

* The capability matrix is the truth about what has run: until a row says Verified, it has not touched real hardware.
* Only the radar node and the CM5 test bench have run on real hardware.
* No independent security review.

**Next**

* Move rows of the matrix to Verified as the other nodes run on their boards.

## 🌍 Languages

README and texts exist in English, Spanish, French, Italian, German, Chinese, Japanese and European Portuguese.

## 🔗 Related Projects

**A.R.M.O.R.** (Autonomous Radar & Multimodal Observation Range) is a perimeter-security system made of independent repositories. Each one has its own version, its own tests and its own README; this is the family:

* **[ARMOR-COMMON](https://github.com/JuanenRac/ARMOR-COMMON)** - Message contracts, validators, conformance vectors and generated types
* **[ARMOR-NODE-RADAR](https://github.com/JuanenRac/ARMOR-NODE-RADAR)** - Field-node firmware for ESP32-S3 with three radars and its own web panel
* **[ARMOR-NODE-SOLAR](https://github.com/JuanenRac/ARMOR-NODE-SOLAR)** - Solar inverter and battery protocols and the messages of a gateway node
* **[ARMOR-NODE-ELECTRICAL](https://github.com/JuanenRac/ARMOR-NODE-ELECTRICAL)** - Electrical node: meters, the message of the network's readings and the rules for switching
* **[ARMOR-NODE-ALARM](https://github.com/JuanenRac/ARMOR-NODE-ALARM)** - Alarm node and panel: zones, arming, delays, siren and PIN, with the server or without it
* **[ARMOR-NODE-HMI](https://github.com/JuanenRac/ARMOR-NODE-HMI)** - Touch panel: the state of the system on a wall screen, arming and acknowledging, and the home of the voice assistant
* **[ARMOR-NETWORK](https://github.com/JuanenRac/ARMOR-NETWORK)** - The local network: its devices, the internet and what changes
* **[ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER)** - Central coordinator: telemetry, alarms, devices, solar readings and cameras
* **[ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO)** - Web console: cameras, radar, alarms, solar energy and the 2D/3D site designer
* **[ARMOR-ANDROID-CONTROL](https://github.com/JuanenRac/ARMOR-ANDROID-CONTROL)** - Android operator client with a live 2D/3D radar
* **[ARMOR-IOS-CONTROL](https://github.com/JuanenRac/ARMOR-IOS-CONTROL)** - iPhone operator client
* **[ARMOR-SERVER-AI](https://github.com/JuanenRac/ARMOR-SERVER-AI)** - Visual inference policy that explains its decisions and never actuates
* **[ARMOR-VISION](https://github.com/JuanenRac/ARMOR-VISION)** - Camera zones, masks and detection rules for the Jetson Orin NX
* **[ARMOR-VOICE-AI](https://github.com/JuanenRac/ARMOR-VOICE-AI)** - Offline voice intents with a confirmation that cannot be forged
* **[ARMOR-HARDWARE](https://github.com/JuanenRac/ARMOR-HARDWARE)** - Enclosures, electronics and the bench acceptance matrix
* **[ARMOR-DEVOPS](https://github.com/JuanenRac/ARMOR-DEVOPS)** - Deployment, the CM5 test bench, backup and TLS
* **[ARMOR-SIMULATOR](https://github.com/JuanenRac/ARMOR-SIMULATOR)** - Offline telemetry simulator with repeatable faults
* **[ARMOR-UPDATER](https://github.com/JuanenRac/ARMOR-UPDATER)** - Detects, installs and updates the ecosystem's own repositories
* **ARMOR-DOCS** (this repository) - Architecture, security baseline and the capability matrix

## 📚 Documentation

* [ARCHITECTURE](docs/ARCHITECTURE.md): networks, trust boundaries, time and ordering
* [SECURITY_BASELINE](docs/SECURITY_BASELINE.md): the VLAN design, what the code enforces and what is missing
* [THREAT_MODEL](docs/THREAT_MODEL.md): what is defended against and what is not
* [INTERFACES](docs/INTERFACES.md): who produces and consumes each interface and where it is trusted
* [FIRST_VERTICAL_SLICE](docs/FIRST_VERTICAL_SLICE.md): what the simulator-to-console test proves and what it does not
* [SETUP_CODE](docs/SETUP_CODE.md): the set-up code of the nodes
* [Capability matrix: what is proven and what is not](docs/CAPABILITY_MATRIX.md)
* [Project catalogue: versions and how the repositories depend on each other](docs/PROJECT_CATALOG.md)
* [Changelog of this repository](CHANGELOG.md)

## 🤝 Contributing & Community

* Before a pull request run `python -I tools/armor_ci_validate.py` and the tests: both must pass. See [CONTRIBUTING.md](CONTRIBUTING.md) and the [code of conduct](CODE_OF_CONDUCT.md).
* The README exists in eight languages and is generated from the sources in ARMOR-DOCS: a change to the text is made there.
* A change to a message between components starts in ARMOR-COMMON.
* Do not describe as working on a board what has only been built.
* Report a vulnerability privately: [SECURITY.md](SECURITY.md). Questions, ideas and reports: electrohobby3d@gmail.com ([SUPPORT.md](SUPPORT.md)).

## 👤 AUTHOR

**JuanenRac (Electro Hobby 3D)** · electrohobby3d@gmail.com

## 📜 LICENSE

GPL-3.0-or-later - see [LICENSE](LICENSE).
