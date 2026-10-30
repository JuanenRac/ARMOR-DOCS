# Changelog

All notable changes to this project are documented here.

## [Unreleased]

- **The shared workflow installs Mosquitto in the node repositories:** `sync_ci_tools.py` writes the updated workflow and project tool everywhere; the test counts of the Studio, Server and Android READMEs follow the code.

## [0.8.1.3] - The README generator writes the universal layout for every repository

- **The README of ARMOR-COMMON, ARMOR-SERVER, ARMOR-STUDIO, ARMOR-SERVER-AI, ARMOR-NETWORK, ARMOR-UPDATER, ARMOR-DEVOPS and of this repository follow the universal layout:** their sources in `tools/readme_src/repos/` hold the 14 required sections and the optional ones in eight languages, built with the new shared helpers of `tools/readme_src/_kit.py` (tables, code blocks, the Architecture and Repository Structure pictures read from `docs/architecture.json` and `docs/structure.json`). The capability matrix and the interfaces guide now say 1225 conformance vectors, and the catalogue shows the versions of the manifests.
- **The pictures of the README come from shared tools:** `tools/make_architecture.py` draws `images/architecture.svg` from `docs/architecture.json` and `tools/make_structure.py` draws the Repository Structure (the text tree and the animated picture) from `docs/structure.json`; both measure every text, and `--check` fails when a picture, its description or the code it points to disagree. They are vendored from ARMOR-COMMON like the shared CI checks.
- **The generator writes the README in the universal layout:** a repository whose source says `"layout": "universal"` (ARMOR-VOICE-AI is the first) is rendered with the 22 sections in their fixed order, the header, At a glance with its "Jump to" line and Project status, from `tools/readme_src/repos/<REPOSITORY>.py`; the names, icons and shared sentences of the sections are in `ui.py` in the eight languages. The hand-written README folder is no longer used for ARMOR-VOICE-AI.
- **The README of seven repositories no longer runs two bullets together in the Overview** (ARMOR-ANDROID-CONTROL, ARMOR-DEVOPS, ARMOR-NODE-ALARM, ARMOR-NODE-ELECTRICAL, ARMOR-NODE-HMI, ARMOR-NODE-SOLAR, ARMOR-STUDIO), and the README of this repository counts nineteen repositories.
- **The universal README check** (`tools/universal_readme_check.py`, canonical in ARMOR-COMMON) is vendored with the other shared tools and runs from the validator as a warning.

## [0.8.1.2] - The tools read the repositories from the registry of ARMOR-COMMON and the banners are written by the generator again

- **The tools read the repositories from the registry of ARMOR-COMMON:** the order of the READMEs, the brand pictures and the map of the family, the repositories that get the shared tools and the workflow of Studio and the server, and the catalogue no longer keep lists of their own; a test compares what is left (the script that checks everything, the firmware sync, the shared project tool) with the registry.
- **The banners are written by the generator again:** one animated drawing for the family with the name, kind, group and technologies of each repository (the technologies of the five nodes brought up to date, a long list loses whole technologies instead of a name cut in half), so `make_brand.py --check` passes against the banners of the repositories.
- The sync tool also vendors the workflow that tries Studio and the server together (`e2e.yml`) into ARMOR-STUDIO and ARMOR-SERVER, and lists the iPhone client in the family of the READMEs, the family map, the brand assets and the shared tools.

- **The security baseline records the way to HTTPS for the phones:** the house's own authority, the pin shown in Studio, the pairing in the app, the check and the order of the steps before plain http can be forbidden.
- **The README source of the Android app carries what the app now does:** the lock with the phone, the access from outside the house (two addresses, the key of the certificate remembered, push as data only), the files of the lock in the structure and the test count, in the eight languages, so that rendering the READMEs does not take them out.
- **README sources brought up to date with the repositories they describe:** the test and vector counts of ARMOR-COMMON, ARMOR-SERVER, ARMOR-STUDIO and ARMOR-NETWORK, the name check of ARMOR-NETWORK (`--dns-name`) and the room the maintenance helper of ARMOR-DEVOPS makes on a nearly full disk, in the eight languages.
- The repository has a security policy, a code of conduct, a contributing guide and a support file.
- The banner follows the animated style of the ecosystem banners, with the name, the kind and the technologies of the project.
## [0.8.1.1] - README sources for the new node versions, requirements and tests per language

- **README sources for the live channel and the binary voice turn:** the touch panel's README says that it listens to the server's live channel and sends the spoken turn as raw bytes, the server's README describes the channel, and the test counts follow the programs.
- **The interfaces table** lists the live channel of the wall panel and the binary voice turn (and says the older request is used also when the answer is 400 or 422).
- **The Android app's README source** counts 281 tests and says the key of the saved session can optionally be tied to unlocking the phone.
- **The README generator words the requirements and the test counts in each language** instead of copying the English line, and the family list is refreshed.
- **README sources for the new work:** diagnostics, the perimeter engine, reading quality and held values, and ESP-IDF 5.5.5 as the one toolchain.
- **The catalog says that ARMOR-VISION is a library no service imports yet,** and the VISION README commands are written for bash.
- **Threat model and capability matrix** cover the node diagnostics and the read-only diagnostic token.

## [0.8.1.0] - Live status, the alarm window and the table of routes in the READMEs, and a stricter check of the family list

- **Live status, the alarm window and the designers' keys in the READMEs:** the sources of the READMEs of Studio, the phone app and the server describe the live channel of the status, the alarm window of the open app, the keys of the designers and the table of routes, in the eight languages, and the test counters of the three are refreshed.
- **A check that no README draws an image twice or leaves a repository out of the family list:** every README of every repository in every language is rendered and counted.
- **The CI validator speaks eight languages:** the shared copy that every repository carries recognises the Portuguese labels of the version in the prose of a README.

## [0.8.0.9] - The self-protection of the nodes in the capability matrix and the threat model

- The capability matrix and the threat model describe how a node protects itself when its internal memory runs short, and the retained last will and birth of a node.

## [0.8.0.8] - Controlling the nodes: architecture, interfaces, security baseline, threat model and capability matrix

- **Controlling the nodes in the architecture and the interfaces:** a new section describes the eight operations an administrator can order (restart, pause, resume, standby, identify, diagnostics, maintenance on and off) for one node or for all, the topics, the two steps with a one-time token bound to the operation, the three states of a node (running, paused with its timer, standby kept across a restart) and the maintenance flag, what each kind of node does while paused or on standby, and what the server shows. Standby is described as the work off while the node stays connected, never as a power-off; there is no factory reset, no erase and no deep sleep. The interfaces table lists the two topics and the three server routes, and the contracts list names the two new messages.
- **Threat model and security baseline:** a new section of the threat model says what a stolen administrator session could do with node control (a restart storm, an alarm panel or a radar paused or on standby leaving the house unprotected, maintenance mode hiding an outage, a forged or replayed order, a node commanding the others) and what is done about each (administrator and fresh proof of identity, the node's name or a word typed again, a one-time token bound to the operation that lives thirty seconds, the broker's access list, rate limits, rolling restarts with the alarm panels last, a pause that ends by itself, a standby shown on the node and in the node health, the history and the audit trail) and what is left. The security baseline lists the capability.
- **Capability matrix:** two new rows, one for the control of the nodes through the server and the phone and one for the state machine shared by the five kinds of node, both local, with the honest note that nothing has run on a board or against real nodes.
- **READMEs:** the sources of the READMEs of the five field nodes, the server, the broker rules, Studio and the phone app carry a bullet about the control of the nodes in the eight languages, and the phone app's test counter and file list are refreshed.

## [0.8.0.7] - Writing to Pylontech batteries: architecture, security baseline, threat model and capability matrix

- **Writing to Pylontech batteries in the architecture, the security baseline and the threat model:** the statement that the solar and electrical nodes only read their equipment now says that a battery can be written to through typed operations, off by default in the node, the server and the broker, with a fresh proof of identity and the battery's serial number typed; a new section of the threat model lists what is done about each threat of that capability (a stolen or replayed order, the wrong battery, writing while the battery works, a harmful value, firmware that destroys it, the service password, a change that leaves no trace) and what is left.
- **Capability matrix:** two new rows, one for writing to a battery through its console (local, not activated, with the honest note that the form of several console lines is inferred and that nothing was tried on a real battery) and one for sending it firmware (simulated).
- **READMEs:** the README of the node, the server, Studio and the phone app mention the capability in the eight languages, and the test counters of those four are refreshed.

## [0.8.0.6] - Refresh the counters and the catalogue

- **The test counters and the versions** of the field nodes, the server, the app and the common library are refreshed, and the catalogue lists the new versions.

## [0.8.0.5] - Node test counters

- The test counters in the README of the five field nodes follow the new host tests.

## [0.8.0.4] - Test counts and node pages current

- The README sources of the five field nodes carry the counts of their host tests as they are now, and the catalogue the versions of the new node releases.
- The radar node's page says that one node covers up to 270 degrees with up to three radars, in the eight languages.

## [0.8.0.3] - The project catalogue is current again

- The project catalogue lists the versions the projects have now, and the README sources carry the new test counts of the server and the network watcher.
- The threat model describes using the system from outside the house (sign-in guessing, a stolen session, a new place, the panels of the nodes and what is not covered), and the capability matrix and the interfaces page state the number of conformance vectors of the contracts as it is.

## [0.8.0.2] - READMEs for the history of connections and the sign-in form

- The README sources of ARMOR-COMMON, ARMOR-SERVER, ARMOR-STUDIO and ARMOR-ANDROID-CONTROL describe the connection and system events of the history, the Connections list and the sign-in form for password managers, in the eight languages, with the counts of tests, vectors and routes brought up to date.

## [0.8.0.1] - README sources for health and arming profiles

- The README sources of ARMOR-COMMON, SERVER, ALARM, RADAR, SOLAR, ELECTRICAL, HMI, STUDIO, ANDROID-CONTROL and DEVOPS describe the node health report and the arming profiles in the eight languages, and the test count of ARMOR-NODE-ALARM.

## [0.8.0.0] - The README sources describe the optional encrypted link to the broker

- The sources of the READMEs of ARMOR-DEVOPS, ARMOR-COMMON, the five nodes, ARMOR-SERVER and ARMOR-STUDIO have a bullet in the eight languages about the optional encrypted link to the broker (TLS), and the file trees list the new script, tests and modules; the number of tests of the server is updated.

## [0.7.9] - The publication check no longer flags example addresses written in test fixtures

- The history scan of the publication check ignores public-looking addresses that only appear in lines removed from tests and conformance fixtures (they are there to stand for outside the house); keys, e-mail addresses and every other finding are still reported.

## [0.7.8] - The wall panel in the interfaces, and the READMEs of this batch

- **Interfaces:** the touch panel's own conversation with the server (its account, its four routes, its broker identity, the voice route) is in the table.
- **Catalogue and READMEs:** the versions of this batch of releases, and the pages of the projects that moved (the test counts, the honest lines and the structure of each).
- The generators of ARMOR-NETWORK, ARMOR-SERVER-AI, ARMOR-VISION, ARMOR-VOICE-AI, ARMOR-SIMULATOR, ARMOR-HARDWARE, ARMOR-DEVOPS, ARMOR-SERVER and ARMOR-UPDATER carry the new numbers and wording in the eight languages.

## [0.7.7] - The pages say what the code does, and the whole family is compared every night

- **Security pages brought up to date:** firmware is signed as a manifest (project, board, version, hash) and the server checks it too; Bluetooth pairing uses a PIN derived from the set-up code and what that leaves open is said; the nodes' relays and switch channel are named instead of "only read"; every command is an allow-list and the unknown-field rule says who drops and who rejects; the core machine is the CM5 of the bench, with the AI planned for a Jetson-class machine; and the CI is described as it is.
- **Architecture and interfaces:** the alarm, network and touch-panel nodes are in the diagram, Bluetooth set-up is listed for every node, time may be the node's uptime stamped by the server, the Zigbee feed and the orders of the network answer are interfaces, and the contract counts are 17 schemas and 523 vectors.
- **Capability matrix:** the counts match the vectors and the host programs, a table that was cut in two is whole, and the legend names the levels the table really uses.
- **Tools:** `sync_ci_tools.py` includes ARMOR-VISION and a check writes nothing; `check_all.sh` runs every host test a node registers (also the alarm node's), the vision and updater repositories, and the catalogue and tool checks; the publication check accepts both spellings of the author's name and follows renames; the history made for publishing says "Initial commit"; the catalogue and the READMEs know the maturity "production"; the family map and the banners include the alarm panel and the vision repository; the README of this repository shows the family picture once.
- **Nightly run:** `.github/workflows/nightly.yml` fetches every repository next to this one, compares what is generated and shared, runs the checks and opens an issue when something does not agree.

## [0.7.6] - Catalog versions and the alarm designer

- The project catalog carries the new versions, and the description of ARMOR-STUDIO mentions the Alarm Designer.

## [0.7.5] - Versions of the catalog

- The project catalog carries the versions of the projects changed in this batch of releases.

## [0.7.4] - The PIN to disarm, the restart that keeps the house armed and ARMOR-VISION in the documentation

- `docs/PROJECT_CATALOG.md` lists every version as its manifest says and the new ARMOR-VISION; `docs/CAPABILITY_MATRIX.md` has the rows of the PIN to disarm, the alarm node that keeps its mode through a restart, the publish queue and watchdog, the recovery of damaged files and ARMOR-VISION; `docs/INTERFACES.md` lists the alarm, info, electrical and relay topics and says that the node command topic is reserved; `docs/THREAT_MODEL.md` and `docs/SECURITY_BASELINE.md` say what the PIN, the recovery and the watchdog do and what they leave.

## [0.7.3] - The alarm node's radio takeover, and the solar board's ten ports

- **Capability matrix:** ARMOR-NODE-ALARM's firmware now says that it takes the Zigbee radio over itself (and what has and has not been tried: only frames on a computer), and the solar base board's row says ten ports in 4, 4 and 2, the LEDs (eight on a shift register, two on a pin each) and the warning for a pair that mixes hardware.
- **Threat model** (`docs/THREAT_MODEL.md`): what the system protects, from whom, where its pieces trust each other, what each piece does about each threat, what is left and what to do first, written from what the code does and honest that it is not an audit.
- **Catalogue:** the versions that moved (ARMOR-COMMON 0.4.4, ARMOR-NODE-SOLAR 0.3.2, ARMOR-NODE-ALARM 0.2.0) and ARMOR-NODE-ALARM's description.

## [0.7.2] - The alarm node joins the matrix

- **Capability matrix:** ARMOR-NODE-ALARM's firmware, its messages in the shared contract, the server's alarm nodes (commands off by default) and the Alarm panels of Studio and the phone, each with what has and has not been proven; nothing has run on a board.
- **Catalogue:** the versions of the projects that moved (ARMOR-COMMON 0.4.3, ARMOR-NODE-ALARM 0.1.0, the server, Studio, the phone, the electrical, solar, radar and touch-panel nodes and DevOps), and the interface file's new name.

## [0.7.1] - What has run on real hardware, said the same way everywhere

- The capability matrix, the security baseline and the ARMOR-NODE-RADAR pages said, in different places, that the radar firmware had never run on a board or had run on one board without radars. Two real nodes (Waveshare ESP32-S3-ETH) run it: the firmware row and the link from Studio to a node's panel are now *Verified*, and what is still not recorded on a real node (the Wi-Fi bridge, mapped pins, joining a router's Wi-Fi, Bluetooth between a board and a phone, real targets for the track identities) is worded as "not yet recorded" instead of "never".

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

- `docs/PROJECT_CATALOG.md` lists ARMOR-ANDROID-CONTROL 0.4.7 and ARMOR-NODE-RADAR 0.5.4.


## [0.6.0] - Catalog with the Android client version

- `docs/PROJECT_CATALOG.md` lists ARMOR-ANDROID-CONTROL 0.4.6 and this project's own row at 0.6.0.


## [0.5.9] - The catalog row of this project

- `docs/PROJECT_CATALOG.md` listed this project with a version several releases old; the row now carries the current one.


## [0.5.8] - Project catalog with the current versions

- The catalog also lists the versions of SERVER, VOICE-AI, UPDATER and ANDROID-CONTROL after their latest changes.

- `docs/PROJECT_CATALOG.md` lists the current versions of COMMON, RADAR, ELECTRICAL, HMI, DEVOPS, UPDATER and ANDROID-CONTROL.


## [0.5.6] - The version table, and what the capability matrix says about hardware

- **PROJECT_CATALOG.md:** every version number brought up to date.
- **CAPABILITY_MATRIX.md:** it said no radar or field-node board had ever been connected; one ARMOR-NODE-RADAR board with its LD2450 radars has been flashed and run on a bench, so it now says that (and that nothing else of the kind has).
- **Manifest:** `native_version` was behind `version`, which the CI check refuses; they are equal again.

## [0.5.5] - The version table catches up once more

- **PROJECT_CATALOG.md:** every version number brought up to date (ARMOR-NODE-RADAR 0.4.3, ARMOR-NODE-SOLAR 0.1.9, ARMOR-NODE-ELECTRICAL 0.1.5, ARMOR-NODE-HMI 0.0.9).

## [0.5.4] - The version table catches up once more

- **PROJECT_CATALOG.md:** every version number brought up to date (ARMOR-NODE-RADAR 0.3.9, ARMOR-NODE-SOLAR 0.1.7, ARMOR-NODE-ELECTRICAL 0.1.3, ARMOR-NODE-HMI 0.0.7).

## [0.5.3] - The version table catches up once more

- **PROJECT_CATALOG.md:** every version number brought up to date (ARMOR-COMMON 0.3.4, ARMOR-NODE-RADAR 0.3.8, ARMOR-NODE-SOLAR 0.1.6, ARMOR-NODE-ELECTRICAL 0.1.2, ARMOR-NODE-HMI 0.0.6, ARMOR-SERVER 0.4.1, ARMOR-STUDIO 0.6.0, ARMOR-DEVOPS 0.3.6).

## [0.5.2] - The version table catches up again, this time including itself

- **PROJECT_CATALOG.md:** every version number brought up to date (ARMOR-COMMON 0.3.3, ARMOR-NODE-RADAR 0.3.6, ARMOR-NODE-HMI 0.0.4, ARMOR-STUDIO 0.5.9, ARMOR-DEVOPS 0.3.5), and its own row corrected to 0.5.2 - 0.5.1's refresh had updated every other project but forgot to update the row for ARMOR-DOCS itself.

## [0.5.1] - The version table catches up

- **PROJECT_CATALOG.md:** every version number brought up to date (ARMOR-COMMON 0.3.2, ARMOR-NODE-RADAR 0.3.5, ARMOR-NODE-SOLAR 0.1.4, ARMOR-NODE-ELECTRICAL 0.1.0, ARMOR-NODE-HMI 0.0.3, ARMOR-SERVER 0.4.0, ARMOR-STUDIO 0.5.8, ARMOR-ANDROID-CONTROL 0.4.0), and the Server and Studio descriptions now mention the electrical, network, services and weather menus.

## [0.5.0] - Working notes leave the public repository

- Three working documents (in Spanish, dated, with working notes) sat in the root of this repository; they were never part of the documentation. They are removed from the repository. The capability matrix and the catalogue are the public record.

## [0.4.9] - The matrix and the catalog caught up

- **Capability matrix:** the touch panel's firmware now builds (it has not run on a board), the ESP32-S3-ETH firmware has run on one real board, the network node's orders on request and `inspect` with a device login, the machine metrics, the connection settings and the device logins have rows of their own.
- **Project catalog:** nine versions that had fallen behind are read again from each project's manifest.

## [0.4.8] - A CI baseline for the whole family, and ARMOR-UPDATER joins it

- **The new project ARMOR-UPDATER** (detects, installs and updates the ecosystem's repositories on the machine it runs on; the same atomic-by-verification install/update design as an established open ecosystem's updater, adapted for a private one) in the catalogue, the architecture and the capability matrix.

- **`tools/sync_ci_tools.py`**: vendors ARMOR-COMMON's canonical `armor_ci_validate.py`, `_armor_readme_parity.py`, `armor_project_tool.py` and `.github/workflows/ci.yml` into every one of the other fourteen repositories - the same "canonical here, vendored everywhere" pattern this file's own `make_readmes.py`/`publication_check.py` rules already use.

- Every repository's version bumped once for this shared addition; four real manifest/build drifts found and fixed along the way (ARMOR-NODE-RADAR, ARMOR-NODE-SOLAR, ARMOR-NODE-ELECTRICAL, ARMOR-SIMULATOR).

- A GitHub Actions CI baseline (`.github/workflows/ci.yml`) for this repository itself: validates the manifest, the version, CHANGELOG.md's heading, the seven README translations' structure and its own local Markdown links, then runs this project's real build/test through `tools/armor_project_tool.py build-test .`.

## [0.4.7] - ARMOR-NETWORK joins the family

- The new project **ARMOR-NETWORK** (the local network: devices, the internet and what changes) in the catalogue, the architecture, the interfaces and the capability matrix, in its README in the seven languages and in the brand (an icon, a banner and a place in the map of the family); the commands `armor_project_tool.py` runs for it and `tools/check_all.sh`, which runs its tests. The vector count is 330 now.

## [0.4.6] - The commands to a switch in the documentation and in the checks

- The READMEs of ARMOR-COMMON (266 conformance vectors and 36 tests now, the new topics `command` and `result`), ARMOR-NODE-ELECTRICAL (the commands to a switch, tested and not activated) and ARMOR-DEVOPS (the ACL step that makes a switch reachable) in the seven languages; the capability matrix has a row for electrical switching, marked local and not activated, and the interfaces guide the new vector count.

- `tools/check_all.sh` also runs `ARMOR-DEVOPS/scripts/test_mqtt_identity.sh`.

## [0.4.5] - The solar base board, the electrical screen and the batch of software that followed

- The capability matrix, the catalogue and the READMEs (seven languages) describe the mux profile of ARMOR-NODE-SOLAR 0.0.8, the second PV input and the parallel units (contract 0.2.3, 193 vectors), the electrical alarms and the Android screen (ARMOR-ANDROID-CONTROL 0.3.3), the simulator's `--electrical` (0.2.2) and the versions of the family.

## [0.4.4] - The documentation of the whole family checked against the code

- **The counts are the real ones:** ARMOR-SERVER 168 tests, ARMOR-STUDIO 203, ARMOR-COMMON 21 (and 177 vectors), ARMOR-NODE-SOLAR 765 host checks, ARMOR-NODE-ELECTRICAL 135,990 (254 apart from the switching rules), ARMOR-NODE-RADAR 859. The Italian README of ARMOR-SERVER said 159, and the ARMOR-NODE-SOLAR build block said 600 and patched "83 checks" into "100": both were wrong and the patch is gone.

- **The structure blocks match the trees:** ARMOR-NODE-SOLAR, ARMOR-NODE-RADAR, ARMOR-NODE-ELECTRICAL, ARMOR-ANDROID-CONTROL, ARMOR-DEVOPS, ARMOR-SIMULATOR, ARMOR-SERVER, ARMOR-STUDIO and ARMOR-COMMON list the files and folders they have now (the Bluetooth files, the electrical node, the Electrical Designer, the solar and electrical schemas). The Spanish structure block of ARMOR-NODE-SOLAR was in English. A `FIXES` table in `readme_data/meta_new.py` corrects the first-generation blocks, in English and in Spanish.

- **Bluetooth for the three kinds of node:** the matrix, the catalogue and the READMEs of ARMOR-NODE-SOLAR and ARMOR-NODE-ELECTRICAL (seven languages) say that a phone can set them up like the radar node.

- **The core documents know the whole family:** the architecture (solar and electrical nodes, the Bluetooth set-up boundary), the interfaces, the security baseline (read-only equipment, the Bluetooth channel), the contracts guide (the electrical message) and the server's integration notes (the solar and electrical topics and routes).

- **The server's broker ACL:** the documents say what ARMOR-DEVOPS now installs: `armor-server` reads `armor/electrical/#` too.

## [0.4.3] - Inverter dialects and the model catalogue in the matrix

- The capability matrix and the ARMOR-NODE-SOLAR README (seven languages) say that the node reads three inverter dialects and the newer Pylontech console layout, and that the catalogue lists more inverter families and battery models; the check counts are 684.

- The matrix and the READMEs say the battery health is in the shared contract (147 vectors) and that the console's `info` and `stat` are tested with text real batteries printed; the check counts of the solar node are 697.

- The matrix and the ARMOR-STUDIO README (seven languages) describe the Electrical Designer; Studio has 201 tests.

- The matrix and the READMEs count the 177 conformance vectors of the contract, which now has the electrical message.

- A new repository, **ARMOR-NODE-ELECTRICAL** (0.0.1, scaffolding), in the family map, the catalogue, the matrix, the READMEs (seven languages) and the check script.

## [0.4.2] - Reading an ANT-BMS's settings in the matrix

- The capability matrix and the ARMOR-NODE-SOLAR README (seven languages) say that the node can read an ANT-BMS's model, version and settings (read only, never tried on a BMS) and that writing to BMSs and inverters is not implemented on purpose; the check counts are 600.

## [0.4.1] - Solar alarms on the phone in the matrix

- The capability matrix and the Android README (seven languages) say that solar alarms are announced on the phone like device alarms (unit-tested, never on a phone); the catalogue has the new versions.

- The matrix, the security baseline and ARMOR-DEVOPS's README (seven languages) describe the core machine's host firewall (rules tested as text, never loaded) and keep the VLANs as a design; `check_all.sh` runs its tests.

## [0.4.0] - The four firmwares in the matrix

- The capability matrix and the READMEs of ARMOR-NODE-RADAR and ARMOR-NODE-SOLAR (seven languages) say that each node has a version for each board (with Ethernet on the Waveshare ESP32-S3-ETH, and Wi-Fi only on the ESP32-S3-WROOM-1 N16R8) and that none has run on a board; `check_all.sh` runs the tests of both board profiles.

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

## [0.3.4] - ARMOR-NODE-SOLAR enters the family

- **ARMOR-NODE-SOLAR** enters the catalogue, the README generator and `check_all.sh`; the matrix says what its protocols are and that nothing solar has met a real device. `check_all.sh` and the shared project tool now run every host test of ARMOR-NODE-RADAR (they only ran one of three).

## [0.3.3] - HTTPS, stable tracks, the new Android look and two tools for publishing

- The capability matrix says what the node's HTTPS panel, the stable track identities and the device states checked against the server are, and how much was checked; the Android rows describe the redesigned app, its live radar tab and what was exercised in an emulator; the catalogue and the READMEs carry the new versions and counts.

- **`tools/clean_history.py`** makes a publishable copy of a repository: its current files as one commit, on a new branch, by the project's author, with no history behind it (the working history is not touched, and nothing is pushed). It refuses a repository with uncommitted changes or with findings in its files, and checks the new branch. **`tools/publication_check.py`** (0.3.2) can now check only what one branch reaches.

## [0.3.2] - Six sensor models and the buttons of Studio

- The capability matrix says what the LD2461 and the four presence sensors are (decoded from the manufacturers' documents and tested against their worked examples, none connected), the per-port sensor model of the node's panel, and drops the row that said the LD2461 had no document; the catalogue has the new versions; the README generator says the new counts and the six models.

## [0.3.1] - Bluetooth configuration and the Wi-Fi station in the documentation

- The capability matrix says what the Wi-Fi station with a network search and the Bluetooth configuration (firmware and app) are, and how much was checked; the catalogue has the new versions; the README of ARMOR-NODE-RADAR and of the Android client describe them.

## [0.3.0] - The node panel, the information message and the new versions

- The capability matrix says what the node's web panel, the shared Wi-Fi, the mapped pins, the update path, the radar command channel, the panel link in Studio and the public-address login are, and how much of each was checked (all of it on a computer, none on a board).

- ARMOR-NODE-RADAR's README (English and Spanish) describes the panel and the new tools; the catalogue and the interfaces page carry the new versions and the 68 conformance vectors.

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

## [0.2.2] - Second review

- The capability matrix and interfaces follow the new behaviour.

## [0.2.1] - One-command checks

- `tools/check_all.sh` runs every check of every repository and prints one PASS, FAIL or SKIP line each.

- Updated the capability matrix, catalogue and interfaces.

## [0.2.0]

- Architecture, security baseline, project catalogue, interfaces, first vertical slice and capability matrix.

- Shared README generator for the family and brand tool with a `--check` mode.

