# Changelog

All notable changes to this project are documented here.

## [0.7.1] - What has run on real hardware, said the same way everywhere

- The capability matrix, the security baseline and the ARMOR-RADAR pages said, in different places, that the radar firmware had never run on a board or had run on one board without radars. Two real nodes (Waveshare ESP32-S3-ETH) run it: the firmware row and the link from Studio to a node's panel are now *Verified*, and what is still not recorded on a real node (the Wi-Fi bridge, mapped pins, joining a router's Wi-Fi, Bluetooth between a board and a phone, real targets for the track identities) is worded as "not yet recorded" instead of "never".

## [0.7.0] - The documentation follows what the system does today

- The capability matrix lists what was added: the node firmware update from a file or from GitHub (seen on a real radar board), the live map of a radar node, the weather radar of the app, the motion watching, the fifteen voice commands, the alarms to Telegram and Home Assistant, the configurator of a node in the app and Studio's administration of the machine - each at the honest level it has reached.
- `docs/INTERFACES.md` lists the new links (firmware to the nodes, Telegram and Home Assistant, the observation service, the administration agent) and points at the current OpenAPI file; the architecture says a spoken command is carried out with the session of the person who gave it.
- The catalogue's descriptions of SERVER, STUDIO, ANDROID-CONTROL, DEVOPS, RADAR, SERVER-AI and VOICE-AI name their new features.

## [0.6.9] - Catalog with the voice commands and the node configurator

- `docs/PROJECT_CATALOG.md` lists VOICE-AI 0.2.5, SERVER 0.5.0, SERVER-AI 0.2.3, COMMON 0.4.1 and ANDROID-CONTROL 0.4.9.

## [0.6.8] - Catalog with the observation service work

- `docs/PROJECT_CATALOG.md` lists SERVER 0.4.9, STUDIO 0.6.5, COMMON 0.4.0, DEVOPS 0.4.0 and SERVER-AI 0.2.2.

## [0.6.7] - Catalog with the notifications work

- `docs/PROJECT_CATALOG.md` lists SERVER 0.4.8, STUDIO 0.6.4 and COMMON 0.3.9.

## [0.6.6] - Catalog with the services fix

- `docs/PROJECT_CATALOG.md` lists ARMOR-SERVER 0.4.7.

## [0.6.5] - Catalog with the voice work

- `docs/PROJECT_CATALOG.md` lists SERVER 0.4.6, VOICE-AI 0.2.4 (its earlier 0.3.0 was renumbered, it skipped a minor), DEVOPS 0.3.9 and ANDROID-CONTROL 0.4.8.


## [0.6.4] - Catalog with the firmware progress work

- `docs/PROJECT_CATALOG.md` lists SERVER 0.4.5 and STUDIO 0.6.3.


## [0.6.3] - Catalog with the voice gateway version

- `docs/PROJECT_CATALOG.md` lists ARMOR-VOICE-AI 0.3.0 (seven languages).


## [0.6.2] - Catalog with the node firmware work

- `docs/PROJECT_CATALOG.md` lists SERVER 0.4.4, STUDIO 0.6.2 and COMMON 0.3.7 (updating the firmware of the nodes from Studio).


## [0.6.1] - Catalog with the Android and radar versions

- `docs/PROJECT_CATALOG.md` lists ARMOR-ANDROID-CONTROL 0.4.7 and ARMOR-RADAR 0.5.4.


## [0.6.0] - Catalog with the Android client version

- `docs/PROJECT_CATALOG.md` lists ARMOR-ANDROID-CONTROL 0.4.6 and this project's own row at 0.6.0.


## [0.5.9] - The catalog row of this project

- `docs/PROJECT_CATALOG.md` listed this project with a version several releases old; the row now carries the current one.


## [0.5.8] - Project catalog with the current versions

- The catalog also lists the versions of SERVER, VOICE-AI, UPDATER and ANDROID-CONTROL after their latest changes.

- `docs/PROJECT_CATALOG.md` lists the current versions of COMMON, RADAR, ELECTRICAL, HMI, DEVOPS, UPDATER and ANDROID-CONTROL.


## [0.5.6] - The version table, and what the capability matrix says about hardware

- **PROJECT_CATALOG.md:** every version number brought up to date.
- **CAPABILITY_MATRIX.md:** it said no radar or field-node board had ever been connected; one ARMOR-RADAR board with its LD2450 radars has been flashed and run on a bench, so it now says that (and that nothing else of the kind has).
- **Manifest:** `native_version` was behind `version`, which the CI check refuses; they are equal again.

## [0.5.5] - The version table catches up once more

- **PROJECT_CATALOG.md:** every version number brought up to date (ARMOR-RADAR 0.4.3, ARMOR-SOLAR 0.1.9, ARMOR-ELECTRICAL 0.1.5, ARMOR-HMI 0.0.9).

## [0.5.4] - The version table catches up once more

- **PROJECT_CATALOG.md:** every version number brought up to date (ARMOR-RADAR 0.3.9, ARMOR-SOLAR 0.1.7, ARMOR-ELECTRICAL 0.1.3, ARMOR-HMI 0.0.7).

## [0.5.3] - The version table catches up once more

- **PROJECT_CATALOG.md:** every version number brought up to date (ARMOR-COMMON 0.3.4, ARMOR-RADAR 0.3.8, ARMOR-SOLAR 0.1.6, ARMOR-ELECTRICAL 0.1.2, ARMOR-HMI 0.0.6, ARMOR-SERVER 0.4.1, ARMOR-STUDIO 0.6.0, ARMOR-DEVOPS 0.3.6).

## [0.5.2] - The version table catches up again, this time including itself

- **PROJECT_CATALOG.md:** every version number brought up to date (ARMOR-COMMON 0.3.3, ARMOR-RADAR 0.3.6, ARMOR-HMI 0.0.4, ARMOR-STUDIO 0.5.9, ARMOR-DEVOPS 0.3.5), and its own row corrected to 0.5.2 - 0.5.1's refresh had updated every other project but forgot to update the row for ARMOR-DOCS itself.

## [0.5.1] - The version table catches up

- **PROJECT_CATALOG.md:** every version number brought up to date (ARMOR-COMMON 0.3.2, ARMOR-RADAR 0.3.5, ARMOR-SOLAR 0.1.4, ARMOR-ELECTRICAL 0.1.0, ARMOR-HMI 0.0.3, ARMOR-SERVER 0.4.0, ARMOR-STUDIO 0.5.8, ARMOR-ANDROID-CONTROL 0.4.0), and the Server and Studio descriptions now mention the electrical, network, services and weather menus.

## [0.5.0] - Internal audit notes leave the public repository

- Three audit documents (in Spanish, dated, with working notes and a mention of private notes) sat in the root of this repository; they were never part of the documentation. They are removed from the repository. The capability matrix and the catalogue are the public record.

## [0.4.9] - The matrix and the catalog caught up

- **Capability matrix:** the touch panel's firmware now builds (it has not run on a board), the ESP32-S3-ETH firmware has run on one real board, the network node's orders on request and `inspect` with a device login, the machine metrics, the connection settings and the device logins have rows of their own.
- **Project catalog:** nine versions that had fallen behind are read again from each project's manifest.

## [0.4.8] - A CI baseline for the whole family, and ARMOR-UPDATER joins it

- **The new project ARMOR-UPDATER** (detects, installs and updates the ecosystem's repositories on the machine it runs on; the same atomic-by-verification install/update design as an established open ecosystem's updater, adapted for a private one) in the catalogue, the architecture and the capability matrix.

- **`tools/sync_ci_tools.py`**: vendors ARMOR-COMMON's canonical `armor_ci_validate.py`, `_armor_readme_parity.py`, `armor_project_tool.py` and `.github/workflows/ci.yml` into every one of the other fourteen repositories - the same "canonical here, vendored everywhere" pattern this file's own `make_readmes.py`/`publication_check.py` rules already use.

- Every repository's version bumped once for this shared addition; four real manifest/build drifts found and fixed along the way (ARMOR-RADAR, ARMOR-SOLAR, ARMOR-ELECTRICAL, ARMOR-SIMULATOR).

- A GitHub Actions CI baseline (`.github/workflows/ci.yml`) for this repository itself: validates the manifest, the version, CHANGELOG.md's heading, the seven README translations' structure and its own local Markdown links, then runs this project's real build/test through `tools/armor_project_tool.py build-test .`.

## [0.4.7] - ARMOR-NETWORK joins the family

- The new project **ARMOR-NETWORK** (the local network: devices, the internet and what changes) in the catalogue, the architecture, the interfaces and the capability matrix, in its README in the seven languages and in the brand (an icon, a banner and a place in the map of the family); the commands `armor_project_tool.py` runs for it and `tools/check_all.sh`, which runs its tests. The vector count is 330 now.

## [0.4.6] - The commands to a switch in the documentation and in the checks

- The READMEs of ARMOR-COMMON (266 conformance vectors and 36 tests now, the new topics `command` and `result`), ARMOR-ELECTRICAL (the commands to a switch, tested and not activated) and ARMOR-DEVOPS (the ACL step that makes a switch reachable) in the seven languages; the capability matrix has a row for electrical switching, marked local and not activated, and the interfaces guide the new vector count.

- `tools/check_all.sh` also runs `ARMOR-DEVOPS/scripts/test_mqtt_identity.sh`.

## [0.4.5] - The solar base board, the electrical screen and the batch of software that followed

- The capability matrix, the catalogue and the READMEs (seven languages) describe the mux profile of ARMOR-SOLAR 0.0.8, the second PV input and the parallel units (contract 0.2.3, 193 vectors), the electrical alarms and the Android screen (ARMOR-ANDROID-CONTROL 0.3.3), the simulator's `--electrical` (0.2.2) and the versions of the family.

## [0.4.4] - The documentation of the whole family checked against the code

- **The counts are the real ones:** ARMOR-SERVER 168 tests, ARMOR-STUDIO 203, ARMOR-COMMON 21 (and 177 vectors), ARMOR-SOLAR 765 host checks, ARMOR-ELECTRICAL 135,990 (254 apart from the switching rules), ARMOR-RADAR 859. The Italian README of ARMOR-SERVER said 159, and the ARMOR-SOLAR build block said 600 and patched "83 checks" into "100": both were wrong and the patch is gone.

- **The structure blocks match the trees:** ARMOR-SOLAR, ARMOR-RADAR, ARMOR-ELECTRICAL, ARMOR-ANDROID-CONTROL, ARMOR-DEVOPS, ARMOR-SIMULATOR, ARMOR-SERVER, ARMOR-STUDIO and ARMOR-COMMON list the files and folders they have now (the Bluetooth files, the electrical node, the Electrical Designer, the solar and electrical schemas). The Spanish structure block of ARMOR-SOLAR was in English. A `FIXES` table in `readme_data/meta_new.py` corrects the first-generation blocks, in English and in Spanish.

- **Bluetooth for the three kinds of node:** the matrix, the catalogue and the READMEs of ARMOR-SOLAR and ARMOR-ELECTRICAL (seven languages) say that a phone can set them up like the radar node.

- **The core documents know the whole family:** the architecture (solar and electrical nodes, the Bluetooth set-up boundary), the interfaces, the security baseline (read-only equipment, the Bluetooth channel), the contracts guide (the electrical message) and the server's integration notes (the solar and electrical topics and routes).

- **The server's broker ACL:** the documents say what ARMOR-DEVOPS now installs: `armor-server` reads `armor/electrical/#` too.

## [0.4.3] - Inverter dialects and the model catalogue in the matrix

- The capability matrix and the ARMOR-SOLAR README (seven languages) say that the node reads three inverter dialects and the newer Pylontech console layout, and that the catalogue lists more inverter families and battery models; the check counts are 684.

- The matrix and the READMEs say the battery health is in the shared contract (147 vectors) and that the console's `info` and `stat` are tested with text real batteries printed; the check counts of the solar node are 697.

- The matrix and the ARMOR-STUDIO README (seven languages) describe the Electrical Designer; Studio has 201 tests.

- The matrix and the READMEs count the 177 conformance vectors of the contract, which now has the electrical message.

- A new repository, **ARMOR-ELECTRICAL** (0.0.1, scaffolding), in the family map, the catalogue, the matrix, the READMEs (seven languages) and the check script.

## [0.4.2] - Reading an ANT-BMS's settings in the matrix

- The capability matrix and the ARMOR-SOLAR README (seven languages) say that the node can read an ANT-BMS's model, version and settings (read only, never tried on a BMS) and that writing to BMSs and inverters is not implemented on purpose; the check counts are 600.

## [0.4.1] - Solar alarms on the phone in the matrix

- The capability matrix and the Android README (seven languages) say that solar alarms are announced on the phone like device alarms (unit-tested, never on a phone); the catalogue has the new versions.

- The matrix, the security baseline and ARMOR-DEVOPS's README (seven languages) describe the core machine's host firewall (rules tested as text, never loaded) and keep the VLANs as a design; `check_all.sh` runs its tests.

## [0.4.0] - The four firmwares in the matrix

- The capability matrix and the READMEs of ARMOR-RADAR and ARMOR-SOLAR (seven languages) say that each node has a version for each board (with Ethernet on the Waveshare ESP32-S3-ETH, and Wi-Fi only on the ESP32-S3-WROOM-1 N16R8) and that none has run on a board; `check_all.sh` runs the tests of both board profiles.

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

