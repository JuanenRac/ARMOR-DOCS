# Changelog

All notable changes to this project are documented here.

## [0.3.9] - The Android app's solar screen in the matrix

- The capability matrix and the Android README (seven languages) say what the app's Solar screen is and how much was checked (unit tests and an emulator with example readings, never real equipment); the catalogue has the new versions.

## [0.3.8] - The solar node's firmware in the matrix

- The capability matrix says what the solar node's firmware, its panel, its ten ports, its ANT-BMS decoder and its emulated UART are and how much was checked (builds, host-tested with stand-in equipment, never on a board); the catalogue has the new versions and `check_all.sh` runs the node's tests.

## [0.3.7] - Declaring solar equipment in the matrix

- The capability matrix says what declaring equipment, the example readings and the simulator's solar scenario are and how much was checked; the catalogue has the new versions.

## [0.3.6] - The READMEs in seven languages, a banner and an icon for every project

- **Every repository has its README in English, Spanish, French, Italian, German, Chinese and Japanese** (`README.md` and `README_spa`, `_fra`, `_ita`, `_deu`, `_zho`, `_jpn`), all written by `tools/make_readmes.py` from `tools/readme_data/` (one module per language) with the same sections: overview, the architecture and the security model where they apply, the repository structure, the development environment, the family of projects, the documentation and the author. The four READMEs that used to be written by hand are generated too, with their numbers brought up to date (tests, vectors, menus, the solar readings).
- **A banner and an icon for every project**, each with its own drawing inside the shield (a radar sweep, a sun, a rack, a monitor, a phone, an eye, a microphone, a cube, a gear, a flask, braces, a book), and `images/ARMOR_FAMILY.svg`, a map of who feeds whom. `tools/make_brand.py` writes them and escapes the `&` that broke four of the old banners.
- The matrix no longer says that nothing has met hardware (the cameras and the CM5 bench have) and counts the 142 conformance vectors; the catalogue describes the solar work of the server and of Studio.

## [0.3.5] - Solar in the matrix and the catalogue

- The capability matrix says what the solar contract, the server's ingestion and alarms and Studio's two menus are and how much was checked (all with generated readings, none with a real inverter or battery); the catalogue has the new versions; the interfaces document counts the vectors and names the current OpenAPI file.

## [0.3.4] - ARMOR-SOLAR enters the family

- **ARMOR-SOLAR** enters the catalogue, the README generator and `check_all.sh`; the matrix says what its protocols are and that nothing solar has met a real device. `check_all.sh` and the shared project tool now run every host test of ARMOR-RADAR (they only ran one of three).

## [0.3.3] - HTTPS, stable tracks, the new Android look and two tools for publishing

- The capability matrix says what the node's HTTPS panel, the stable track identities and the device states checked against the server are, and how much was checked; the Android rows describe the redesigned app, its live radar tab and what was exercised in an emulator; the catalogue and the READMEs carry the new versions and counts.
- **`tools/clean_history.py`** makes a publishable copy of a repository: its current files as one commit, on a new branch, by the project's author, with no history behind it (the working history is not touched, and nothing is pushed). It refuses a repository with uncommitted changes or with findings in its files, and checks the new branch. **`tools/publication_check.py`** (0.3.2) can now check only what one branch reaches.

## [0.3.2] - Six sensor models and the buttons of Studio

- The capability matrix says what the LD2461 and the four presence sensors are (decoded from the manufacturers' documents and tested against their worked examples, none connected), the per-port sensor model of the node's panel, and drops the row that said the LD2461 had no document; the catalogue has the new versions; the README generator says the new counts and the six models.

## [0.3.1] - Bluetooth configuration and the Wi-Fi station in the documentation

- The capability matrix says what the Wi-Fi station with a network search and the Bluetooth configuration (firmware and app) are, and how much was checked; the catalogue has the new versions; the README of ARMOR-RADAR and of the Android client describe them.

## [0.3.0] - The node panel, the information message and the new versions

- The capability matrix says what the node's web panel, the shared Wi-Fi, the mapped pins, the update path, the radar command channel, the panel link in Studio and the public-address login are, and how much of each was checked (all of it on a computer, none on a board).
- ARMOR-RADAR's README (English and Spanish) describes the panel and the new tools; the catalogue and the interfaces page carry the new versions and the 68 conformance vectors.

## [0.2.9] - Catalogue versions

- Studio 0.2.5 and DevOps 0.2.5 in the project catalogue.

## [0.2.8] - Colours and camera view in the capability matrix

- One row for the designer's colours, names and per-camera field of view, with what was checked (tests and a rendered session) and that the 2D plan shows only some of the colours.

## [0.2.7] - Firmware and the 270° node in the capability matrix

- The field-node rows say what now exists (a firmware image that builds in the ESP-IDF container, the W5500 and VEML7700 drivers, the 270° node in Studio) and, unchanged, that none of it has run on a board.

## [0.2.6] - Android with alarms, devices and arming in the capability matrix

- The Android rows say what the phone can do now (arm and disarm, alarms, devices, device-alarm notifications) and what was checked, and the client boundary no longer says it cannot arm.

## [0.2.5] - Devices, alarms, automations and the shared design in the capability matrix

- Capability matrix rows for devices, alarms, automations, arm and disarm from Studio, the design kept on the server and the radar configuration, each with what it was checked against and what was not; the project catalogue shows the new versions.

## [0.2.4] - Studio users, the radar map and the designer in the capability matrix

- Capability matrix rows for user management, the radar map and the redesigned site designer, with what each was checked against and what was not; the project catalogue shows the new versions.

## [0.2.3] - PTZ, history and designer verified

- The capability matrix records PTZ against the real cameras (one answers, one refuses the stored login, two have no PTZ), the history management and the new designer.

## [0.2.2] - Second audit pass

- The audit document records the second pass: what was found, fixed and left open. The capability matrix and interfaces follow the new behaviour.

## [0.2.1] - Full audit and one-command checks

- `tools/check_all.sh` runs every check of every repository and prints one PASS, FAIL or SKIP line each.
- Added the general audit and updated the capability matrix, catalogue and interfaces.

## [0.2.0]

- Architecture, security baseline, project catalogue, interfaces, first vertical slice and capability matrix.
- Shared README generator for the family and brand tool with a `--check` mode.
