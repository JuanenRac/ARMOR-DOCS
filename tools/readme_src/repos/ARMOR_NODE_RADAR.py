# The facts that do not depend on the language, and the words of every language, of ARMOR-NODE-RADAR, in the universal README layout.
# Copyright (C) 2026 JuanenRac (Electro Hobby 3D). GPL-3.0-or-later.

FACTS = {
  "emoji": "📡",
  "layout": "universal",
  "license_badge": "License-GPL%203.0--or--later-blue",
  "status": [
    [
      "software",
      "green",
    ],
    [
      "tests",
      "green",
    ],
    [
      "protocols",
      "yellow",
    ],
    [
      "ui",
      "yellow",
    ],
    [
      "hardware",
      "yellow",
    ],
    [
      "security",
      "yellow",
    ],
    [
      "updates",
      "yellow",
    ],
    [
      "integration",
      "yellow",
    ],
    [
      "docs",
      "green",
    ],
  ],
  "badges": [
    [
      "Language",
      "C%2B%2B17",
      "00599c",
    ],
    [
      "Target",
      "ESP32--S3",
      "e7352c",
    ],
    [
      "Tests",
      "7371%20checks",
      "2ea44f",
    ],
  ],
}

TEXT = {
  "en": {
    "tagline": "Field-node firmware (Waveshare ESP32-S3-ETH, three radars or presence sensors, Ethernet and Wi-Fi) with its own web panel, and its host-tested core",
    "honest": "The radar node is the one node that exists as hardware: its firmware runs on a real Waveshare ESP32-S3-ETH board with a radar and reports to the CM5 test bench, and its web panel and over-the-air updates are in use on it. The hardware-independent core (7,371 checks in 14 test programs: the decoders of the LD2450, the LD2461 and four presence sensors, the LD2450 command channel, the settings and their checks, the pin table, users and sessions, the network plan, the message serialiser whose output ARMOR-COMMON accepts, and the release and signature checks) is tested on a computer, the **web panel** is exercised in a real browser against a stand-in node, and the **firmware image builds** in the ESP-IDF 5.5.5 container. What is **not** proven yet: the LD2461 and presence-sensor decoders match only the worked examples of their manuals, with no module behind them; the signature check of the updates and the Bluetooth PIN pairing are proven on a computer with real signatures but not yet on the board; the radar command channel is unchecked against a module; and the panel's HTTPS certificate (made by the node itself) is untried in every browser.",
    "glance": [
      [
        "Role",
        "Radar field node for ESP32-S3 (family: Field Nodes, parent: ARMOR-COMMON)",
      ],
      [
        "Stack",
        "C++17, ESP-IDF 5.5.5, ESP32-S3",
      ],
      [
        "Tests",
        "7371 checks in 14 host programs and 6 Python checks (`ctest`)",
      ],
      [
        "Boards",
        "Waveshare ESP32-S3-ETH (Ethernet) and ESP32-S3-WROOM-1 N16R8 (Wi-Fi only)",
      ],
      [
        "Sensors",
        "Up to 3 radars (LD2450, LD2461) or presence sensors per node, VEML7700 light sensor",
      ],
      [
        "Runs on",
        "Waveshare ESP32-S3-ETH or ESP32-S3-WROOM-1 N16R8; host tests on any computer",
      ],
      [
        "On real hardware",
        "Runs on a real Waveshare ESP32-S3-ETH board with a radar, reporting to the CM5 test bench",
      ],
      [
        "License",
        "GPL-3.0-or-later",
      ],
    ],
    "status": {
      "software": "The firmware builds in the ESP-IDF 5.5.5 container and runs on a real ESP32-S3-ETH board.",
      "tests": "7,371 checks in 14 host programs pass (`ctest`): the decoders, the settings, the pin table, the users, the network plan, the message serialiser and the release checks.",
      "protocols": "The LD2450 runs on a real radar; the LD2461 and the four presence-sensor decoders only match the worked examples of their manuals, and the radar command channel is unchecked against a module.",
      "ui": "The web panel is in use on the board and is exercised in a real browser against a stand-in node; its HTTPS certificate, made by the node itself, is untried in every browser.",
      "hardware": "It is the one node that exists as hardware: a real Waveshare ESP32-S3-ETH board with a radar reports to the CM5 test bench; no other sensor module is connected.",
      "security": "The Bluetooth PIN pairing and the update signature check are proven on a computer with real signatures but not yet on the board; there has been no independent review.",
      "updates": "Over-the-air updates are in use on the board; the signed-update check has not run there yet.",
      "integration": "The messages of the board reach the CM5 test bench server, and the same messages are accepted by the shared schemas and conformance vectors of ARMOR-COMMON. It has been seen on the bench only, not in an installation.",
      "docs": "Eight languages and the changelog are up to date.",
    },
    "docs": [
      "[Node panel](docs/NODE_PANEL.md): first start, users, network, the panel pages",
      "[Set-up code](docs/SETUP_CODE.md) and [Bluetooth provisioning](docs/BLE_PROVISIONING.md)",
      "[Sensors](docs/SENSORS.md): the six models and their decoders",
      "[Bench bring-up](docs/BENCH_BRINGUP.md), [bench tests](docs/BENCH_TESTS.md) and [hardware boundary](docs/HARDWARE_BOUNDARY.md)",
    ],
    "contributing_first": "Before a pull request run `ctest --test-dir build/host` and `python -I tools/armor_ci_validate.py`: it must pass. See [CONTRIBUTING.md](CONTRIBUTING.md) and the [code of conduct](CODE_OF_CONDUCT.md).",
    "languages_extra": "",
    "body": {
      "overview": r"""* **Two boards, one firmware:** the Waveshare ESP32-S3-ETH (Ethernet, the default) and an ESP32-S3-WROOM-1 N16R8 with no Ethernet (Wi-Fi only: its set-up asks for the Wi-Fi network to join and it always keeps its own network). The image is chosen when it is built (`tools/build_node.sh generic s3-eth` or `generic s3-wifi`); the pin table and the way in follow the board, the panel hides what the board does not have, and an image is only for its own board. Both build and are host-tested; neither has run on a board.
* **A node covers up to 270 degrees:** each Waveshare ESP32-S3-ETH reads up to three LD2450 radars on its three UARTs, mounted 75 degrees apart, over wired Ethernet (W5500) with DHCP or a fixed address, powered by PoE or USB. Studio's *Add a 270° node* creates the three radars already wired to the node.
* **A web panel on every node,** in the look of Studio and its eight languages, embedded in the firmware: overview, network, Wi-Fi, broker, radars, pins, users, firmware update and log. A node with no user opens the Wi-Fi `ARMOR-SETUP-xxxxxx` and creates its first administrator with a set-up code; passwords are salted PBKDF2, sessions are random tokens, and every setting lives in the node's flash, so one image serves every node and no password is compiled in ([the panel](docs/NODE_PANEL.md)).
* **One Wi-Fi from many nodes:** each node can offer an access point joined to its Ethernet port; give the nodes the same name and password and the channel on automatic (1, 6 or 11 by MAC) and phones and Wi-Fi sensors see one network with one DHCP server. It is not a radio mesh: every node keeps its cable. A node can instead join a router's Wi-Fi (with a search for networks), and one with no cable can be configured over **Bluetooth** from the Android app.
* **Pins for the server:** any free pin becomes an input, an output (with a safe state when the broker is lost), PWM or an analogue reading, and appears as a device of the server, so a relay or a contact needs no new firmware. The board's reserved pins are never offered.
* **Over-the-air updates with rollback** from the panel (two slots on the 16 MB flash), and a **link from Studio** to each node's panel, from the address the node publishes.
* **The panel over HTTPS:** the node makes its own certificate (self-signed, kept in flash) and serves the panel on port 443 as well as 80, or only on 443; the session cookie is marked Secure and the certificate fingerprint is shown to compare with the browser's warning.
* **Stable track identities:** each frame's targets are matched to the ones followed before, so a person keeps the same track id, a lost frame does not flicker and positions are smoothed a little.
* **Six sensor models, one per port:** a port carries an LD2450 or an LD2461 (trackers that feed the perimeter, with the model's own field in Studio) or a presence sensor (LD2410, LD2412, LD2410S, MR24HPC1) that becomes a device of the server and publishes presence and distance. Chosen in the panel; what each one is, its protocol and what was not verified are in `docs/SENSORS.md`.
* **LD2450 decoder, health and configuration:** a resynchronising framer finds frames in a noisy stream; each 30-byte frame gives up to three targets that become contract tracks; the console and the panel say per radar whether it reports, is silent or garbled. The panel can also read the module's version, choose one or three targets and set detection zones (a protocol that is unchecked against a module).
* **Ambient light and contract-exact messages:** the VEML7700 with automatic range; telemetry, health and information JSON that follow the published schemas and refuse to write anything invalid, with wall-clock timestamps (SNTP) and an MQTT last will. Telemetry is withheld while no radar reports, never an empty 'all clear'.
* **One image for every board, like a network product:** the firmware is the same and the MAC tells the boards apart (`armor-` and six digits until named); `adopt_node.py` gives a freshly flashed node its administrator, its broker identity and the fleet's shared settings over the network, with a set-up code computed from its MAC, so 5 nodes or 27 are the same work.
* **Bench tools:** flashing over USB-C, a stand-in node for working on the panel, and a converter from a log of raw frames to a test fixture ([bench bring-up](docs/BENCH_BRINGUP.md)).
* **Signed over-the-air updates:** the node installs from GitHub only an image whose SHA-256 matches and that carries a valid Ed25519 signature of the maintainer (the public key is in the firmware, the private one never leaves the maintainer); a file uploaded by hand by an administrator in the panel is still accepted. The pages and messages of the panel are in eight languages.
* **Bluetooth pairing with a PIN:** the six-digit PIN is derived from the set-up code, printed on the USB console and shown to an administrator in the panel; the phone has to enter it before it may write the node's settings.
* **Only the house may use the panel:** the panel answers the private network by default (or the networks its owner lists, such as a VPN), refuses a list that would lock out whoever saves it, counts wrong passwords for each person as well as each address, and works behind the server's proxy so that it can be reached from outside the house without publishing the node.
* **Optional encrypted link to the broker (TLS):** off by default, so the node talks plain MQTT as before. A switch and a box for the certificate of the installation's own authority (PEM, at most 2 KB) in the Broker page make it connect with `mqtts://`, trust that authority only and check that the broker's certificate was made for the address it reached; anything that is not one PEM certificate is refused. Covered by host tests; the handshake has not been run on a board yet.
* **Health report:** about once a minute the node publishes how long it has been up and why it last restarted, its free memory, its link and Wi-Fi signal, how many times it connected to the broker and the last error it logged (`armor/health/<node>`, the `node_health` contract of ARMOR-COMMON). The code that builds it is shared by every node and tested on a computer; it has not run on a board.
* **Control from the server:** Studio can restart the node cleanly, pause it for up to an hour (it resumes by itself), put its work in standby (no end, kept across restarts, the node stays connected and keeps answering), make it show itself, ask for a diagnostics snapshot and mark it as in maintenance (`armor/control/<node>/...`, the `node_control` contract of ARMOR-COMMON). Every order takes two steps with a one-time token that belongs to that operation, only the server may write them on the broker, and there is no factory reset, no erase and no deep sleep. While the node is paused or in standby it publishes no targets and no presence (the heartbeat still says it is there). The code is shared by every node and tested on a computer; it has not run on a board.
* **A perimeter engine on the node (off by default):** six detection zones and three exclusion zones, each a rectangle that can be turned by an angle, three tripwire lines that count crossings by direction, three entry paths, pet immunity and masking detection. It runs next to the sensors, so it works when the broker cannot be reached, keeps its events while the broker is away and publishes them on `armor/radar/<node>/events`; the zone editor is in the node's panel. None of it has run with a sensor on a board yet.
* **Who each sensor is, and its own Bluetooth closed:** at start the node reads the firmware version and the Bluetooth address of each sensor, closes the sensors' own Bluetooth (it asks for no PIN) by default, and can hand the serial line of one sensor to an administrator's PC tool for a few minutes (a transparent serial bridge). `GET /metrics` for administrators and an export and all-or-nothing import of the settings complete it.
* **Diagnostics without a cable:** after a start that was not clean (a crash, a watchdog, a sag of the supply, a failed allocation) the health report says why for ten minutes; a crash leaves its core dump to look at, download or erase from the panel; the stored settings are copied before every firmware install and recovered if an update damages them; and an administrator can ask the node, through the server, for a diagnostic package or its log with a one-time token.
* **Adoption over HTTPS with a pinned certificate:** `tools/adopt_node.py` accepts `https://<address>` with `--fingerprint` (the SHA-256 of the node's certificate, checked on the very connection that carries the request) or `--show-fingerprint` to read it; it warns about plain HTTP and about a fleet file with a fixed address or host name, and the panel warns too when such a file is imported.
* **The sensor reader waits for events instead of polling:** the reading task sleeps on the serial lines' event queues and drains everything that arrived, flushes a line that overflowed and counts overflows and errors per line; `system.reader_idle_ms` (100; 0 = the earlier 10 ms polling) sets how long it waits, and a queue that fails sends it back to polling by itself.
* **Optional sealing of stored secrets:** off by default (`security.seal_secrets`, or the server's `nodes.nvs_encryption`). When on, the passwords, tokens, keys, PINs and password hashes the node stores are kept sealed with ChaCha20-Poly1305 and everything else stays readable; turning it on or off rewrites them with nothing lost, even if the node stops half-way. No eFuse is burned and the flash is not encrypted: the key lives in a partition of the same chip, so it does **not** protect against someone who holds the board, and a node installed before that partition existed keeps its secrets as they were until it is flashed with the new partition table.""",
      "role": r"""ARMOR-NODE-RADAR is the eyes of the perimeter. Each node reads up to three radars or presence sensors and publishes tracks, light and health to [ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER) over MQTT; [ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) draws them on the site plan and [ARMOR-SERVER-AI](https://github.com/JuanenRac/ARMOR-SERVER-AI) weighs them against the cameras. Its firmware shares a base with the other nodes (the panel, Bluetooth set-up, signed updates, sign-in and the clock come from the firmware base of [ARMOR-COMMON](https://github.com/JuanenRac/ARMOR-COMMON)), so what you learn on one node holds on all of them.

| Name | How | What for |
|---|---|---|
| ARMOR-SERVER | MQTT `armor/node/<id>/telemetry|health|info|command` | Receives the radar messages (the CM5 test bench today) and orders the node |
| ARMOR-STUDIO | link to the panel | Opens the node's panel from the address the node publishes |
| ARMOR-ANDROID-CONTROL | Bluetooth | Sets the node up in the field |
| ARMOR-COMMON | contracts, firmware base | The messages are checked against its schemas; the common firmware is copied from it |""",
      "architecture": r"""<p align="center">
  <img src="images/architecture.svg" alt="ARMOR-NODE-RADAR architecture: who calls it, what it holds and what it depends on" width="100%">
</p>""",
      "security": r"""| Threat | Defence |
|---|---|
| Passwords in clear or compiled in | PBKDF2-HMAC-SHA256 with 10 000 rounds; no password in the firmware (a node with no user enters set-up); at most 4 users (admin or viewer) and 8 to 64 characters; at most 6 sessions, 30 minutes idle |
| Taking a freshly flashed node | Set-up needs a start-up code: the one of the build (`CONFIG_ARMOR_SETUP_CODE`) or a random one kept in flash and shown on the USB console; with a fleet secret it is `HMAC-SHA256(secret, MAC)`; it is also the key of the set-up Wi-Fi (WPA2, never bridged) |
| The panel reached from the internet | It answers the private networks of a house by default (10/8, 172.16/12, 192.168/16, 169.254/16, 127/8 and 100.64/10 where some VPNs live); the setting `web.admin_sources` lists other IPv4 addresses and networks (8 entries, 120 characters); anything outside is refused except the public identity `GET /api/v1/session`; a list that would lock out the person saving it is rejected |
| The panel in clear over HTTP | HTTPS on 443 with a certificate the node makes itself (self-signed, in flash, SHA-256 fingerprint shown to compare); the panel can be http, https or both; the session cookie is always HttpOnly and SameSite=Strict (and Secure over TLS) |
| A fake firmware from GitHub | An image is installed only with a matching SHA-256 and a valid Ed25519 signature made with the maintainer's key (`no_checksum`, `no_signature`, `bad_signature`, `checksum_mismatch`, `wrong_firmware`, `not_newer`, `version_mismatch` refuse it); a manual upload by an administrator is not checked: an explicit limit |
| Hijacking the Bluetooth set-up | A 6-digit PIN derived from the set-up code, shown on the USB console and to an administrator; the phone must type it before writing settings; the set-up window lasts `CONFIG_ARMOR_BLE_SETUP_MINUTES` (10 by default, 1 to 120) |
| A remote order that does harm | Two steps with a single-use token tied to that operation; only the server may write those topics to the broker; a pause lasts one hour at most; there is no factory reset, no erase and no deep sleep by remote order |
| Stored secrets read by someone who has the board | Optional (off by default, switch `security.seal_secrets` or the server's `nodes.nvs_encryption`): ChaCha20-Poly1305 for passwords, tokens, keys, PINs and hashes. It does not encrypt the flash or burn an eFuse: the key is in a partition of the same chip, so it does not protect against whoever holds the board |
| The broker link in clear | Optional TLS (`mqtts://`) with the owner's own authority (PEM up to 2 KB) and a check of the name; off by default. The handshake has only run in host tests, not on a board |
| A sensor's own Bluetooth | By default the node closes the Bluetooth of every LD sensor (it asks for no PIN); a transparent serial bridge to a computer opens only for a few minutes and only by an administrator |
| Adopting a node on an untrusted network | `tools/adopt_node.py https://<address> --fingerprint <SHA-256>` checks the certificate on the same connection; it warns about plain HTTP and about fleet files with a fixed address |
| A dangerous pin | The reserved pins of the board are never offered; an output has a safe state if the broker is lost; two functions cannot share a pin (checked) |
| A public firmware that carries a fleet secret | `CONFIG_ARMOR_FLEET_SECRET` is empty by default: the public build carries no secret |

Read [SECURITY.md](SECURITY.md) to report a vulnerability. There has been no independent review.""",
      "interfaces": r"""| Part | What it sets |
|---|---|
| MQTT | `armor/node/<id>/{telemetry,health,info,command}`, `armor/health/<id>` (its last will is `{"node_id":"..","online":false}`), `armor/control/<id>/{command,result,maintenance}` and `armor/control/all/command`, `armor/device/<id>/<pin>/{state,set}`, `armor/radar/<id>/events`, `armor/radar/<id>/control/armed` |
| Panel (HTTP 80, HTTPS 443) | Routes `session`, `login`, `logout`, `setup`, `status`, `config` (+ export, import), `wifi/scan`, `time`, `radars` (+ command), `perimeter` (+ armed, learn, zone), `pins` (+ command), `bridge` (+ open, close, io), `ota` (+ check, install, progress, copy, switch), `users` (see `account`), `ble-pin`, `log`, `coredump`, `factory-reset`, `reboot`; `/metrics` for administrators and the WebSocket `/ws/radar-map`; `tests/check_routes.py` checks that every route the panel calls exists |
| Panel texts | 76 error codes with a text in eight languages (832 rows in `panel/text.js`), checked by `tests/check_panel_text.py` |
| Hardware | 3 UARTs for LD2450, LD2461, LD2410, LD2412, LD2410S and MR24HPC1 (RX 16, 17, 18; TX 15, 21, 38); W5500 over SPI (MOSI 11, MISO 12, SCLK 13, CS 14, INT 10, RST 9, 20 MHz); VEML7700 on I2C (GPIO 1 and 2); BOOT button |""",
      "configuration": r"""| Variable | Default | What it sets |
|---|---|---|
| `CONFIG_ARMOR_NODE_ID` | `""` | The name; empty gives `armor-` and the last three bytes of the MAC |
| `CONFIG_ARMOR_SETUP_CODE`, `CONFIG_ARMOR_FLEET_SECRET` | `""` | The set-up code of the build (empty: a random one) and the fleet secret (16+ characters; never in the repository) |
| `CONFIG_ARMOR_RADAR_COUNT` | 3 (0-3) | How many radars are connected |
| `CONFIG_ARMOR_TRACK_STABILISER` | y | Keep a track's identity from frame to frame |
| `CONFIG_ARMOR_MQTT_URI`, `_USERNAME`, `_PASSWORD` | `""` | The first broker settings (they can be changed in the panel) |
| `CONFIG_ARMOR_HEARTBEAT_S` | 10 (2-300) | Seconds between health beats |
| `CONFIG_ARMOR_TELEMETRY_PERIOD_MS` | 200 (200-5000) | At most 5 messages per second |
| `CONFIG_ARMOR_BLE_SETUP_MINUTES` | 10 (1-120) | How long the Bluetooth set-up stays open |
| `CONFIG_ARMOR_BOARD_S3_ETH` / `_S3_WIFI` | eth | The board: Waveshare ESP32-S3-ETH or ESP32-S3-WROOM-1 N16R8 (Wi-Fi only) |
| `CONFIG_ARMOR_BOOT_FACTORY_RESET` | y | Hold BOOT for 8 s in the first 30 s to start again |
| `system.login_limit_per_minute` | 30 (0-120) | Wrong passwords per minute before the panel locks sign-in for everyone (0 = no global limit); read and change it from Studio (a button on every node) or with `POST /api/v1/admin/nodes/settings`, where the panel login is used once and never kept |

The settings that are tuned live in the panel and are kept in flash (for example `system.reader_idle_ms`, `security.seal_secrets`, the failed-login limit per minute (30, 0 to 120) and the zones of the perimeter engine); the defaults of the firmware are in `sdkconfig.defaults` and `sdkconfig.board.*`. The flash of 16 MB holds `nvs` (64 KB), `otadata`, `phy_init`, two 3 MB slots `ota_0` and `ota_1`, `coredump` (128 KB) and `nvs_keys` (4 KB) (`partitions.csv`).""",
      "quickstart": r"""**Requirements:** a C++17 compiler for the host tests; the ESP-IDF 5.5.5 container to build the image; a Waveshare ESP32-S3-ETH or an ESP32-S3-WROOM-1 N16R8.

```bash
cmake -S tests -B build/host && cmake --build build/host && ctest --test-dir build/host   # host tests, -Werror
node tools/panel_mock.mjs --user admin:adminpass123   # the panel without a board
python tools/make_fleet.py                             # once: the fleet secret and the shared settings
tools/build_node.sh generic                           # ONE image for every Waveshare board (dist/generic-s3-eth.bin), in the ESP-IDF container
tools/build_node.sh generic s3-wifi                   # the same firmware for an ESP32-S3-WROOM-1 N16R8 with no Ethernet
```

```bat
tools\flash.bat generic COM5 monitor                  # each Waveshare board, once, by USB-C (add s3-wifi for the other board)
```

```bash
tools/adopt_node.py 192.168.0.181 --id perimetro-3 --fleet secrets/fleet.json --broker-ssh-host <cm5> --broker-ssh-user <user>
```

The host tests need any C++17 compiler (Linux, WSL, MSYS2). See the [bench bring-up](docs/BENCH_BRINGUP.md), the [panel](docs/NODE_PANEL.md) and the [hardware boundary](docs/HARDWARE_BOUNDARY.md).""",
      "testing": r"""```bash
cmake -S tests -B build/host && cmake --build build/host && ctest --test-dir build/host
build/host/emit_samples | python tests/check_contract.py
python -I tools/armor_ci_validate.py
```

14 host test programs and 6 Python checks run under `ctest`; 7371 checks counted by the host programs, built with `-Werror`.

| Part | What it covers |
|---|---|
| `test_core`, `test_sensors`, `test_family`, `test_uart_wake` | The decoders (LD2450, LD2461, four presence sensors), the framer, the command channel, the sensor families and the wake of the UART |
| `test_node`, `test_base`, `test_shared`, `test_board_wifi` | The settings and their checks, the pin table, users and sessions, the network plan, the shared base and the Wi-Fi board |
| `test_logic`, `test_perimeter`, `test_control`, `test_diag` | The pin logic, the perimeter engine, the two-step control orders and the diagnostics |
| `test_mqtt_tls`, `test_release` | The TLS link to the broker (host only) and the release and signature checks |
| `check_panel_text`, `check_task_safety`, `check_save_paths`, `check_ble_session`, `check_routes`, `check_bridge_client` | Python: the eight-language panel texts (832 rows), the tasks, the save paths, the Bluetooth session under its lock, the routes and the serial-bridge client |

The web panel is also exercised in a real browser against a stand-in node (`tools/panel_mock.mjs`). The LD2461 and presence-sensor decoders match only the worked examples of their manuals.""",
      "build": "`tools/build_node.sh generic` builds ONE image for every Waveshare board in the ESP-IDF 5.5.5 container, and `tools/flash.bat` writes it by USB-C; the same firmware is built for the Wi-Fi-only board with `s3-wifi`. Releases carry the image, its SHA-256 and its Ed25519 signature, one per board.",
      "troubleshooting": r"""| You see | Because | Do |
|---|---|---|
| You lost the password or the node no longer joins the network | A node with set-up and no address after 90 s opens its own Wi-Fi `ARMOR-SETUP-xxxxxx` (open `http://192.168.4.1/`) | To start again hold BOOT for 8 seconds in the first 30 seconds after power-up (erases settings and users), or use *Factory reset* in the panel |
| An update from GitHub is refused | The release has no checksum or signature, they do not match (`e_no_checksum`, `e_no_signature`, `e_checksum_mismatch`, `e_bad_signature`), has no image for this board (`e_no_asset_for_board`) or is for another project (`e_wrong_firmware`) | Nothing changed on the node; try again or let an administrator upload the file by hand |
| The radar commands answer `no_answer`, `refused` or `disabled` | The radar's TX wire is not connected, the module hung, or the node closes its Bluetooth first | Check the wiring (see the bench bring-up), restart the module from the panel |
| The node shows no sensor 3 or lets a radar sleep | The module stopped talking (silence with no bad frames) | Use *restart module* in the radars page, then close the sensor's own Bluetooth |""",
      "structure": r"""<p align="center">
  <img src="images/repository-structure.svg" alt="Repository structure of ARMOR-NODE-RADAR" width="100%">
</p>

<details>
<summary>Text version of the tree</summary>

```text
ARMOR-NODE-RADAR/
├── main/                                the firmware: an ESP-IDF component
├── panel/                               the web panel embedded in the firmware
├── tests/                               host tests and Python checks
├── docs/                                7 guides for the bench and the panel
├── tools/                               build, flash, adopt, fleet and check tools
├── .github/                             CI workflow, issue and pull-request templates
├── images/                              banner, icon and the two pictures of this README
├── build.sh build.bat                   build through the shared project workflow
├── test.sh test.bat                     run the tests through the shared workflow
├── run.sh run.bat                       start through the shared project workflow
├── armor.project.json                   manifest: version, role, maturity, build command
├── CHANGELOG.md                         what changed in each version
├── SECURITY.md SUPPORT.md LICENSE       security policy, support and license
├── CONTRIBUTING.md CODE_OF_CONDUCT.md   how to contribute and the code of conduct
├── CMakeLists.txt                       the ESP-IDF project
├── partitions.csv                       the flash table
├── sdkconfig.defaults                   the firmware settings
├── sdkconfig.board.s3-eth               the Ethernet board
├── sdkconfig.board.s3-wifi              the Wi-Fi board
├── secrets/                             fleet and node file examples
├── build-test.sh build-test.bat         run the tests through the shared workflow
└── .gitattributes .gitignore            Git settings
```

</details>""",
      "roadmap": r"""**Known limits today**

* The LD2461 and presence-sensor decoders match only the worked examples of their manuals, with no module behind them; the radar command channel is unchecked against a module other than the LD2450.
* The signature check of the updates and the Bluetooth PIN pairing are proven on a computer with real signatures but not yet on the board; the TLS handshake with the broker has not run on a board.
* The health report and the control from the server have not run on the board; the perimeter engine has never run with a sensor; the panel's own HTTPS certificate is untried in every browser; the Wi-Fi board has no physical board (only the Ethernet board exists).

**Next**

* Run the perimeter engine, the health report and the control orders with real sensors and the CM5 test bench; try the TLS link to the broker and the signed update on the board.""",
    },
  },
  "es": {
    "tagline": "Firmware del nodo de campo (Waveshare ESP32-S3-ETH, tres radares o sensores de presencia, Ethernet y Wi-Fi) con su propio panel web, y su núcleo probado en el ordenador",
    "honest": "El nodo radar es el único nodo que existe como hardware: su firmware corre en una placa real Waveshare ESP32-S3-ETH con un radar y reporta al banco de pruebas de la CM5, y su panel web y las actualizaciones por aire se usan en ella. El núcleo independiente del hardware (4,633 comprobaciones en 14 programas de test: los decodificadores del LD2450, el LD2461 y cuatro sensores de presencia, el canal de órdenes del LD2450, los ajustes y sus comprobaciones, la tabla de pines, usuarios y sesiones, el plan de red, el serializador de mensajes cuya salida acepta ARMOR-COMMON, y las comprobaciones de versión y firma) se prueba en un ordenador, el **panel web** se ejercitó en un navegador real contra un nodo de pega y la **imagen del firmware compila** en el contenedor ESP-IDF 5.5.5. Lo que **todavía no** está probado: los decodificadores del LD2461 y de los sensores de presencia solo coinciden con los ejemplos resueltos de sus manuales, sin un módulo detrás; la comprobación de firma de las actualizaciones y el emparejamiento Bluetooth con PIN están probados en ordenador con firmas reales pero aún no en la placa; el canal de órdenes del radar no se ha contrastado con un módulo; y el certificado HTTPS del panel (lo hace el propio nodo) no se ha probado en todos los navegadores.",
    "glance": [
      [
        "Función",
        "Nodo de campo radar para ESP32-S3 (familia: Field Nodes, padre: ARMOR-COMMON)",
      ],
      [
        "Tecnología",
        "C++17, ESP-IDF 5.5.5, ESP32-S3",
      ],
      [
        "Pruebas",
        "7371 comprobaciones en 14 programas de host y 6 de Python (`ctest`)",
      ],
      [
        "Placas",
        "Waveshare ESP32-S3-ETH (Ethernet) y ESP32-S3-WROOM-1 N16R8 (solo Wi-Fi)",
      ],
      [
        "Sensores",
        "Hasta 3 radares (LD2450, LD2461) o sensores de presencia por nodo, sensor de luz VEML7700",
      ],
      [
        "Funciona en",
        "Waveshare ESP32-S3-ETH o ESP32-S3-WROOM-1 N16R8; pruebas de host en cualquier ordenador",
      ],
      [
        "En hardware real",
        "Corre en una placa real Waveshare ESP32-S3-ETH con un radar, reportando al banco de pruebas de la CM5",
      ],
      [
        "Licencia",
        "GPL-3.0-or-later",
      ],
    ],
    "status": {
      "software": "El firmware compila en el contenedor ESP-IDF 5.5.5 y funciona en una placa ESP32-S3-ETH real.",
      "tests": "Pasan 7.371 comprobaciones en 14 programas de host (`ctest`): los decodificadores, los ajustes, la tabla de pines, los usuarios, el plan de red, el serializador de mensajes y las comprobaciones de versión.",
      "protocols": "El LD2450 funciona con un radar real; los decodificadores del LD2461 y de los cuatro sensores de presencia solo coinciden con los ejemplos de sus manuales, y el canal de órdenes del radar no se ha comprobado con un módulo.",
      "ui": "El panel web se usa en la placa y se ejercita en un navegador real contra un nodo simulado; su certificado HTTPS, creado por el propio nodo, no se ha probado en todos los navegadores.",
      "hardware": "Es el único nodo que existe como hardware: una placa Waveshare ESP32-S3-ETH real con un radar informa al banco de pruebas CM5; no hay ningún otro módulo de sensor conectado.",
      "security": "El emparejamiento con PIN Bluetooth y la comprobación de la firma de las actualizaciones están probados en un ordenador con firmas reales, pero aún no en la placa; no ha habido una revisión independiente.",
      "updates": "Las actualizaciones por aire se usan en la placa; la comprobación de actualizaciones firmadas aún no se ha ejecutado allí.",
      "integration": "Los mensajes de la placa llegan al servidor del banco de pruebas CM5, y esos mismos mensajes los aceptan los esquemas compartidos y los vectores de conformidad de ARMOR-COMMON. Solo se ha visto en el banco, no en una instalación.",
      "docs": "Ocho idiomas y el historial de cambios están al día.",
    },
    "docs": [
      "[Panel del nodo](docs/NODE_PANEL.md): primer arranque, usuarios, red, las páginas del panel",
      "[Código de puesta en marcha](docs/SETUP_CODE.md) y [alta por Bluetooth](docs/BLE_PROVISIONING.md)",
      "[Sensores](docs/SENSORS.md): los seis modelos y sus decodificadores",
      "[Puesta en marcha en banco](docs/BENCH_BRINGUP.md), [pruebas de banco](docs/BENCH_TESTS.md) y [límite del hardware](docs/HARDWARE_BOUNDARY.md)",
    ],
    "contributing_first": "Antes de un pull request ejecuta `ctest --test-dir build/host` and `python -I tools/armor_ci_validate.py`: debe pasar. Consulta [CONTRIBUTING.md](CONTRIBUTING.md) y el [código de conducta](CODE_OF_CONDUCT.md).",
    "languages_extra": "",
    "body": {
      "overview": r"""* **Dos placas, un firmware:** la Waveshare ESP32-S3-ETH (Ethernet, la de serie) y una ESP32-S3-WROOM-1 N16R8 sin Ethernet (solo Wi-Fi: su configuración pide la red Wi-Fi a la que unirse y siempre conserva su propia red). La imagen se elige al compilar (`tools/build_node.sh generic s3-eth` o `generic s3-wifi`); la tabla de pines y la forma de acceso siguen a la placa, el panel oculta lo que la placa no tiene y una imagen es solo para su placa. Ambas compilan y tienen tests en el ordenador; ninguna ha funcionado en una placa.
* **Un nodo cubre hasta 270 grados:** cada Waveshare ESP32-S3-ETH lee hasta tres radares LD2450 en sus tres UART, montados con 75 grados de separación, por Ethernet cableada (W5500) con DHCP o dirección fija, alimentada por PoE o USB. *Añadir un nodo de 270°* en Studio crea los tres radares ya asignados al nodo.
* **Un panel web en cada nodo,** con el aspecto de Studio y sus ocho idiomas, integrado en el firmware: resumen, red, Wi-Fi, broker, radares, pines, usuarios, actualización del firmware y registro. Un nodo sin usuarios abre el Wi-Fi `ARMOR-SETUP-xxxxxx` y crea su primer administrador con un código de configuración; las contraseñas usan PBKDF2 con sal, las sesiones son tokens aleatorios y todos los ajustes viven en la flash del nodo, así que una imagen sirve para todos los nodos y no se compila ninguna contraseña ([el panel](docs/NODE_PANEL.md)).
* **Un solo Wi-Fi desde muchos nodos:** cada nodo puede ofrecer un punto de acceso unido a su puerto Ethernet; dales el mismo nombre y contraseña y el canal en automático (1, 6 u 11 según la MAC) y los móviles y sensores Wi-Fi ven una red con un servidor DHCP. No es una malla por radio: cada nodo conserva su cable. Un nodo puede en cambio unirse al Wi-Fi de un router (con búsqueda de redes), y uno sin cable se puede configurar por **Bluetooth** desde la app de Android.
* **Pines para el servidor:** cualquier pin libre pasa a ser una entrada, una salida (con estado seguro si se pierde el broker), PWM o una lectura analógica, y aparece como dispositivo del servidor, así que un relé o un contacto no necesita firmware nuevo. Los pines reservados de la placa nunca se ofrecen.
* **Actualizaciones por el aire con vuelta atrás** desde el panel (dos ranuras en la flash de 16 MB), y un **enlace desde Studio** al panel de cada nodo, a partir de la dirección que el nodo publica.
* **El panel por HTTPS:** el nodo crea su propio certificado (autofirmado, guardado en flash) y sirve el panel también por el puerto 443, o solo por él; la cookie de sesión va marcada como Secure y se muestra la huella del certificado para compararla con el aviso del navegador.
* **Identidades de pista estables:** los objetivos de cada trama se asocian a los que ya se seguían, así que una persona conserva su id, una trama perdida no hace parpadear y las posiciones se suavizan un poco.
* **Seis modelos de sensor, uno por puerto:** un puerto lleva un LD2450 o un LD2461 (rastreadores que alimentan el perímetro, con el campo propio del modelo en Studio) o un sensor de presencia (LD2410, LD2412, LD2410S, MR24HPC1) que pasa a ser un dispositivo del servidor y publica presencia y distancia. Se elige en el panel; qué es cada uno, su protocolo y lo que no se verificó está en `docs/SENSORS.md`.
* **Decodificador LD2450, salud y configuración:** un delimitador que se resincroniza encuentra tramas en un flujo ruidoso; cada trama de 30 bytes da hasta tres objetivos que pasan a ser pistas del contrato; la consola y el panel dicen por radar si informa, está en silencio o llega ininteligible. El panel también puede leer la versión del módulo, elegir uno o tres objetivos y fijar zonas de detección (un protocolo sin comprobar con un módulo).
* **Luz ambiente y mensajes exactos al contrato:** el VEML7700 con rango automático; JSON de telemetría, salud e información que sigue los esquemas publicados y se niega a escribir algo inválido, con marcas de tiempo reales (SNTP) y un last will de MQTT. La telemetría se retiene mientras ningún radar informa, nunca un «todo despejado» vacío.
* **Una imagen para todas las placas, como un producto de red:** el firmware es el mismo y la MAC distingue las placas (`armor-` y seis dígitos hasta que se le da nombre); `adopt_node.py` da a un nodo recién grabado su administrador, su identidad en el broker y los ajustes comunes de la flota por la red, con un código de configuración calculado desde su MAC, así que 5 nodos o 27 dan el mismo trabajo.
* **Herramientas de banco:** grabación por USB-C, un nodo simulado para trabajar en el panel y un conversor de un registro de tramas en bruto a un fixture de pruebas ([puesta en marcha](docs/BENCH_BRINGUP.md)).
* **Actualizaciones por aire firmadas:** el nodo solo instala desde GitHub una imagen cuyo SHA-256 coincide y que lleva una firma Ed25519 válida del responsable (la clave pública está en el firmware, la privada nunca sale del responsable); un archivo subido a mano por un administrador en el panel se sigue aceptando. Las páginas y mensajes del panel están en ocho idiomas.
* **Emparejamiento Bluetooth con PIN:** el PIN de seis cifras se deriva del código de configuración, se imprime en la consola USB y se muestra a un administrador en el panel; el móvil tiene que escribirlo antes de poder cambiar los ajustes del nodo.
* **Solo la casa puede usar el panel:** el panel responde por defecto a la red privada (o a las redes que su dueño indique, como una VPN), rechaza una lista que dejaría fuera a quien la guarda, cuenta las contraseñas erróneas por persona y por dirección, y funciona detrás del proxy del servidor para llegar a él desde fuera de casa sin publicar el nodo.
* **Enlace cifrado opcional con el broker (TLS):** desactivado por defecto, así que el nodo habla MQTT sin cifrar como antes. Un interruptor y una caja para el certificado de la autoridad propia de la instalación (PEM, 2 KB como máximo) en la página Broker hacen que se conecte con `mqtts://`, confíe solo en esa autoridad y compruebe que el certificado del broker se hizo para la dirección a la que llegó; lo que no sea un único certificado PEM se rechaza. Cubierto con pruebas en el ordenador; el handshake aún no se ha ejecutado en una placa.
* **Informe de salud:** cada minuto más o menos el nodo publica cuánto lleva encendido y por qué se reinició la última vez, su memoria libre, su enlace y su señal Wi-Fi, cuántas veces se conectó al broker y el último error que anotó (`armor/health/<nodo>`, el contrato `node_health` de ARMOR-COMMON). El código que lo construye lo comparten todos los nodos y está probado en un ordenador; no se ha ejecutado en una placa.
* **Control desde el servidor:** Studio puede reiniciar el nodo limpiamente, pausarlo hasta una hora (se reanuda solo), poner su trabajo en espera (sin fin, se conserva al reiniciar, el nodo sigue conectado y respondiendo), hacer que se muestre, pedirle una instantánea de diagnóstico y marcarlo en mantenimiento (`armor/control/<nodo>/...`, el contrato `node_control` de ARMOR-COMMON). Cada orden son dos pasos con un token de un solo uso que pertenece a esa operación, solo el servidor puede escribirlas en el broker, y no existe restablecimiento de fábrica, borrado ni sueño profundo. Mientras el nodo está en pausa o en espera no publica objetivos ni presencia (el latido sigue diciendo que está). El código es compartido por todos los nodos y se prueba en un ordenador; no ha funcionado en una placa.
* **Un motor de perímetro en el nodo (apagado por defecto):** seis zonas de detección y tres de exclusión, cada una un rectángulo que se puede girar un ángulo, tres líneas de cruce que cuentan los pasos por sentido, tres rutas de entrada, inmunidad a mascotas y detección de enmascaramiento. Funciona junto a los sensores, así que sigue funcionando sin acceso al broker, guarda sus eventos mientras el broker no está y los publica en `armor/radar/<nodo>/events`; el editor de zonas está en el panel del nodo. Nada de esto se ha probado aún con un sensor en una placa.
* **Quién es cada sensor y su Bluetooth propio cerrado:** al arrancar, el nodo lee la versión de firmware y la dirección Bluetooth de cada sensor, cierra por defecto el Bluetooth propio de los sensores (no pide PIN) y puede ceder la línea serie de un sensor a una herramienta de PC de un administrador durante unos minutos (un puente serie transparente). `GET /metrics` para administradores y una exportación e importación de todo o nada de los ajustes lo completan.
* **Diagnóstico sin cable:** tras un arranque que no fue limpio (un cuelgue, un watchdog, una caída de la alimentación, una reserva de memoria fallida) el informe de salud dice el motivo durante diez minutos; un fallo deja su volcado de núcleo (core dump) para verlo, descargarlo o borrarlo desde el panel; los ajustes guardados se copian antes de cada instalación de firmware y se recuperan si una actualización los daña; y un administrador puede pedir al nodo, a través del servidor, un paquete de diagnóstico o su registro con un token de un solo uso.
* **Adopción por HTTPS con huella fijada:** `tools/adopt_node.py` acepta `https://<dirección>` con `--fingerprint` (el SHA-256 del certificado del nodo, comprobado en la misma conexión que lleva la petición) o `--show-fingerprint` para leerla; avisa del HTTP en claro y de un fichero de flota con IP fija o nombre de host, y el panel también avisa al importar un fichero así.
* **El lector de sensores espera eventos en vez de sondear:** la tarea lectora duerme sobre las colas de eventos de las líneas serie y vacía todo lo recibido, vacía la línea si hubo desbordamiento y cuenta desbordamientos y errores por línea; `system.reader_idle_ms` (100; 0 = el sondeo de 10 ms de antes) fija cuánto espera, y si una cola falla vuelve sola al sondeo.
* **Sellado opcional de los secretos guardados:** desactivado por defecto (`security.seal_secrets`, o `nodes.nvs_encryption` del servidor). Activado, las contraseñas, tokens, claves, PIN y hashes de contraseña que guarda el nodo quedan sellados con ChaCha20-Poly1305 y todo lo demás sigue legible; activarlo o desactivarlo los reescribe sin perder nada, aunque el nodo se pare a medias. No se quema ningún eFuse ni se cifra la flash: la clave está en una partición del mismo chip, así que **no** protege frente a quien tenga la placa, y un nodo instalado antes de esa partición conserva sus secretos como estaban hasta que se grabe con la nueva tabla de particiones.""",
      "role": r"""ARMOR-NODE-RADAR son los ojos del perímetro. Cada nodo lee hasta tres radares o sensores de presencia y publica pistas, luz y salud a [ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER) por MQTT; [ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) las dibuja en el plano del sitio y [ARMOR-SERVER-AI](https://github.com/JuanenRac/ARMOR-SERVER-AI) las sopesa frente a las cámaras. Su firmware comparte una base con los demás nodos (el panel, la configuración por Bluetooth, las actualizaciones firmadas, el acceso y el reloj vienen de la base de firmware de [ARMOR-COMMON](https://github.com/JuanenRac/ARMOR-COMMON)), así que lo que aprendes en un nodo vale en todos.

| Nombre | Cómo | Para qué |
|---|---|---|
| ARMOR-SERVER | MQTT `armor/node/<id>/telemetry|health|info|command` | Recibe los mensajes del radar (hoy el banco CM5) y ordena al nodo |
| ARMOR-STUDIO | enlace al panel | Abre el panel del nodo desde la dirección que el nodo publica |
| ARMOR-ANDROID-CONTROL | Bluetooth | Configura el nodo en el campo |
| ARMOR-COMMON | contratos, base de firmware | Los mensajes se comprueban con sus esquemas; el firmware común se copia de él |""",
      "architecture": r"""<p align="center">
  <img src="images/architecture.svg" alt="Arquitectura de ARMOR-NODE-RADAR: quién lo llama, qué contiene y de qué depende" width="100%">
</p>""",
      "security": r"""| Amenaza | Defensa |
|---|---|
| Contraseñas en claro o compiladas | PBKDF2-HMAC-SHA256 con 10 000 rondas; ninguna contraseña en el firmware (un nodo sin usuario entra en puesta en marcha); máximo 4 usuarios (admin o visor) y de 8 a 64 caracteres; máximo 6 sesiones, 30 minutos de inactividad |
| Tomar un nodo recién grabado | La puesta en marcha exige un código: el de la compilación (`CONFIG_ARMOR_SETUP_CODE`) o uno aleatorio guardado en flash y mostrado en la consola USB; con secreto de flota es `HMAC-SHA256(secreto, MAC)`; también es la clave del Wi-Fi de configuración (WPA2, nunca puenteado) |
| El panel alcanzado desde internet | Responde por defecto a las redes privadas de una casa (10/8, 172.16/12, 192.168/16, 169.254/16, 127/8 y 100.64/10 donde viven algunas VPN); el ajuste `web.admin_sources` lista otras direcciones y redes IPv4 (8 entradas, 120 caracteres); lo de fuera se rechaza salvo la identidad pública `GET /api/v1/session`; se rechaza una lista que dejaría fuera a quien la guarda |
| El panel en claro por HTTP | HTTPS en el 443 con un certificado que el nodo hace él mismo (autofirmado, en flash, huella SHA-256 visible para comparar); el panel puede ser http, https o ambos; la cookie de sesión es siempre HttpOnly y SameSite=Strict (y Secure por TLS) |
| Un firmware falso desde GitHub | Una imagen solo se instala con un SHA-256 que coincide y una firma Ed25519 válida hecha con la clave del mantenedor (`no_checksum`, `no_signature`, `bad_signature`, `checksum_mismatch`, `wrong_firmware`, `not_newer`, `version_mismatch` la rechazan); una subida manual de un administrador no se comprueba: es un límite explícito |
| Secuestro de la puesta en marcha por Bluetooth | Un PIN de 6 dígitos derivado del código de puesta en marcha, visible en la consola USB y para el administrador; el móvil debe introducirlo antes de escribir ajustes; la ventana dura `CONFIG_ARMOR_BLE_SETUP_MINUTES` (10 por defecto, de 1 a 120) |
| Una orden remota que hace daño | Dos pasos con un token de un solo uso ligado a esa operación; solo el servidor puede escribir esos topics en el broker; la pausa dura una hora como máximo; no hay restablecimiento de fábrica, borrado ni sueño profundo por orden remota |
| Secretos guardados leídos por quien tiene la placa | Opcional (apagado por defecto, interruptor `security.seal_secrets` o `nodes.nvs_encryption` del servidor): ChaCha20-Poly1305 para contraseñas, tokens, claves, PIN y hashes. No cifra la flash ni quema un eFuse: la clave está en una partición del mismo chip, así que no protege frente a quien tenga la placa |
| El enlace con el broker en claro | TLS opcional (`mqtts://`) con la autoridad propia del dueño (PEM de hasta 2 KB) y comprobación del nombre; apagado por defecto. El handshake solo se ha ejecutado en pruebas de host, no en una placa |
| El Bluetooth propio de un sensor | Por defecto el nodo cierra el Bluetooth de cada sensor LD (no pide PIN); un puente serie transparente a un ordenador solo se abre unos minutos y por un administrador |
| Adoptar un nodo en una red no fiable | `tools/adopt_node.py https://<dirección> --fingerprint <SHA-256>` comprueba el certificado en la misma conexión; avisa del HTTP plano y de ficheros de flota con dirección fija |
| Un pin peligroso | Los pines reservados de la placa nunca se ofrecen; una salida tiene estado seguro si se pierde el broker; dos funciones no pueden compartir un pin (comprobado) |
| Un firmware público con secreto de flota | `CONFIG_ARMOR_FLEET_SECRET` está vacío por defecto: la compilación pública no lleva secreto |

Lee [SECURITY.md](SECURITY.md) para informar de una vulnerabilidad. No ha habido revisión independiente.""",
      "interfaces": r"""| Parte | Qué define |
|---|---|
| MQTT | `armor/node/<id>/{telemetry,health,info,command}`, `armor/health/<id>` (su última voluntad es `{"node_id":"..","online":false}`), `armor/control/<id>/{command,result,maintenance}` y `armor/control/all/command`, `armor/device/<id>/<pin>/{state,set}`, `armor/radar/<id>/events`, `armor/radar/<id>/control/armed` |
| Panel (HTTP 80, HTTPS 443) | Rutas `session`, `login`, `logout`, `setup`, `status`, `config` (+ export, import), `wifi/scan`, `time`, `radars` (+ command), `perimeter` (+ armed, learn, zone), `pins` (+ command), `bridge` (+ open, close, io), `ota` (+ check, install, progress, copy, switch), `account`, `ble-pin`, `log`, `coredump`, `factory-reset`, `reboot`; `/metrics` para administradores y el WebSocket `/ws/radar-map`; `tests/check_routes.py` comprueba que toda ruta que llama el panel existe |
| Textos del panel | 76 códigos de error con texto en ocho idiomas (832 filas en `panel/text.js`), comprobados por `tests/check_panel_text.py` |
| Hardware | 3 UART para LD2450, LD2461, LD2410, LD2412, LD2410S y MR24HPC1 (RX 16, 17, 18; TX 15, 21, 38); W5500 por SPI (MOSI 11, MISO 12, SCLK 13, CS 14, INT 10, RST 9, 20 MHz); VEML7700 en I2C (GPIO 1 y 2); botón BOOT |""",
      "configuration": r"""| Variable | Por defecto | Qué define |
|---|---|---|
| `CONFIG_ARMOR_NODE_ID` | `""` | El nombre; vacío da `armor-` y los tres últimos bytes de la MAC |
| `CONFIG_ARMOR_SETUP_CODE`, `CONFIG_ARMOR_FLEET_SECRET` | `""` | El código de puesta en marcha de la compilación (vacío: uno aleatorio) y el secreto de flota (16+ caracteres; nunca en el repositorio) |
| `CONFIG_ARMOR_RADAR_COUNT` | 3 (0-3) | Cuántos radares hay conectados |
| `CONFIG_ARMOR_TRACK_STABILISER` | y | Mantener la identidad de una pista de un cuadro a otro |
| `CONFIG_ARMOR_MQTT_URI`, `_USERNAME`, `_PASSWORD` | `""` | Los primeros ajustes del broker (se cambian en el panel) |
| `CONFIG_ARMOR_HEARTBEAT_S` | 10 (2-300) | Segundos entre latidos de salud |
| `CONFIG_ARMOR_TELEMETRY_PERIOD_MS` | 200 (200-5000) | Como máximo 5 mensajes por segundo |
| `CONFIG_ARMOR_BLE_SETUP_MINUTES` | 10 (1-120) | Cuánto dura abierta la puesta en marcha por Bluetooth |
| `CONFIG_ARMOR_BOARD_S3_ETH` / `_S3_WIFI` | eth | La placa: Waveshare ESP32-S3-ETH o ESP32-S3-WROOM-1 N16R8 (solo Wi-Fi) |
| `CONFIG_ARMOR_BOOT_FACTORY_RESET` | y | Mantén BOOT 8 s en los primeros 30 s para empezar de cero |
| `system.login_limit_per_minute` | 30 (0-120) | Contraseñas erróneas por minuto antes de que el panel bloquee el acceso a todos (0 = sin límite global); se lee y se cambia desde Studio (un botón en cada nodo) o con `POST /api/v1/admin/nodes/settings`, donde el acceso al panel se usa una vez y nunca se guarda |

Los ajustes que se afinan en vivo están en el panel y se guardan en flash (por ejemplo `system.reader_idle_ms`, `security.seal_secrets`, el límite de fallos de acceso por minuto (30, de 0 a 120) y las zonas del motor de perímetro); los valores por defecto del firmware están en `sdkconfig.defaults` y `sdkconfig.board.*`. La flash de 16 MB contiene `nvs` (64 KB), `otadata`, `phy_init`, dos ranuras de 3 MB `ota_0` y `ota_1`, `coredump` (128 KB) y `nvs_keys` (4 KB) (`partitions.csv`).""",
      "quickstart": r"""**Requisitos:** un compilador C++17 para las pruebas de host; el contenedor ESP-IDF 5.5.5 para compilar la imagen; una Waveshare ESP32-S3-ETH o una ESP32-S3-WROOM-1 N16R8.

```bash
cmake -S tests -B build/host && cmake --build build/host && ctest --test-dir build/host   # host tests, -Werror
node tools/panel_mock.mjs --user admin:adminpass123   # the panel without a board
python tools/make_fleet.py                             # once: the fleet secret and the shared settings
tools/build_node.sh generic                           # ONE image for every Waveshare board (dist/generic-s3-eth.bin), in the ESP-IDF container
tools/build_node.sh generic s3-wifi                   # the same firmware for an ESP32-S3-WROOM-1 N16R8 with no Ethernet
```

```bat
tools\flash.bat generic COM5 monitor                  # each Waveshare board, once, by USB-C (add s3-wifi for the other board)
```

```bash
tools/adopt_node.py 192.168.0.181 --id perimetro-3 --fleet secrets/fleet.json --broker-ssh-host <cm5> --broker-ssh-user <user>
```

Los tests en el ordenador necesitan cualquier compilador C++17 (Linux, WSL, MSYS2). Véanse la [puesta en marcha](docs/BENCH_BRINGUP.md), el [panel](docs/NODE_PANEL.md) y el [límite del hardware](docs/HARDWARE_BOUNDARY.md).""",
      "testing": r"""```bash
cmake -S tests -B build/host && cmake --build build/host && ctest --test-dir build/host
build/host/emit_samples | python tests/check_contract.py
python -I tools/armor_ci_validate.py
```

14 programas de prueba de host y 6 comprobaciones en Python se ejecutan con `ctest`; 7371 comprobaciones contadas por los programas de host, compilados con `-Werror`.

| Parte | Qué cubre |
|---|---|
| `test_core`, `test_sensors`, `test_family`, `test_uart_wake` | Los decodificadores (LD2450, LD2461, cuatro sensores de presencia), el delimitador de tramas, el canal de órdenes, las familias de sensores y el despertar de la UART |
| `test_node`, `test_base`, `test_shared`, `test_board_wifi` | Los ajustes y sus comprobaciones, la tabla de pines, usuarios y sesiones, el plan de red, la base compartida y la placa Wi-Fi |
| `test_logic`, `test_perimeter`, `test_control`, `test_diag` | La lógica de pines, el motor de perímetro, las órdenes de control en dos pasos y el diagnóstico |
| `test_mqtt_tls`, `test_release` | El enlace TLS con el broker (solo en host) y las comprobaciones de versión y firma |
| `check_panel_text`, `check_task_safety`, `check_save_paths`, `check_ble_session`, `check_routes`, `check_bridge_client` | Python: los textos del panel en ocho idiomas (832 filas), las tareas, las rutas de guardado, la sesión Bluetooth bajo su bloqueo, las rutas y el cliente del puente serie |

El panel web también se ejercita en un navegador real contra un nodo de pruebas (`tools/panel_mock.mjs`). Los decodificadores LD2461 y de presencia solo coinciden con los ejemplos de sus manuales.""",
      "build": "`tools/build_node.sh generic` construye UNA imagen para cada placa Waveshare en el contenedor ESP-IDF 5.5.5 y `tools/flash.bat` la graba por USB-C; el mismo firmware se compila para la placa solo Wi-Fi con `s3-wifi`. Las versiones llevan la imagen, su SHA-256 y su firma Ed25519, una por placa.",
      "troubleshooting": r"""| Ves | Porque | Haz |
|---|---|---|
| Perdiste la contraseña o el nodo ya no se une a la red | Un nodo con puesta en marcha y sin dirección tras 90 s abre su propio Wi-Fi `ARMOR-SETUP-xxxxxx` (abre `http://192.168.4.1/`) | Para empezar de cero mantén BOOT 8 segundos en los primeros 30 segundos tras encender (borra ajustes y usuarios), o usa *Restablecer de fábrica* en el panel |
| Se rechaza una actualización desde GitHub | La versión no trae suma de comprobación ni firma, no coinciden (`e_no_checksum`, `e_no_signature`, `e_checksum_mismatch`, `e_bad_signature`), no trae imagen para esta placa (`e_no_asset_for_board`) o es de otro proyecto (`e_wrong_firmware`) | El nodo no cambió; reintenta o deja que un administrador suba el fichero a mano |
| Las órdenes al radar responden `no_answer`, `refused` o `disabled` | El hilo TX del radar no está conectado, el módulo se colgó o el nodo cierra antes su Bluetooth | Revisa el cableado (mira la puesta en marcha en banco), reinicia el módulo desde el panel |
| El nodo no muestra el sensor 3 o deja dormir un radar | El módulo dejó de hablar (silencio sin tramas malas) | Usa *reiniciar módulo* en la página de radares y luego cierra el Bluetooth del propio sensor |""",
      "structure": r"""<p align="center">
  <img src="images/repository-structure.svg" alt="Estructura del repositorio de ARMOR-NODE-RADAR" width="100%">
</p>

<details>
<summary>Versión en texto del árbol</summary>

```text
ARMOR-NODE-RADAR/
├── main/                                el firmware: un componente de ESP-IDF
├── panel/                               el panel web embebido en el firmware
├── tests/                               pruebas de host y comprobaciones Python
├── docs/                                7 guías del banco y del panel
├── tools/                               herramientas de compilación, grabación, adopción, flota y comprobación
├── .github/                             flujo de CI y plantillas de issues y pull requests
├── images/                              banner, icono y las dos imágenes de este README
├── build.sh build.bat                   compilar con el flujo de proyecto compartido
├── test.sh test.bat                     ejecutar las pruebas con el flujo compartido
├── run.sh run.bat                       arrancar con el flujo de proyecto compartido
├── armor.project.json                   manifiesto: versión, rol, madurez, comando de build
├── CHANGELOG.md                         qué cambió en cada versión
├── SECURITY.md SUPPORT.md LICENSE       política de seguridad, soporte y licencia
├── CONTRIBUTING.md CODE_OF_CONDUCT.md   cómo contribuir y el código de conducta
├── CMakeLists.txt                       el proyecto ESP-IDF
├── partitions.csv                       la tabla de la flash
├── sdkconfig.defaults                   los ajustes del firmware
├── sdkconfig.board.s3-eth               la placa Ethernet
├── sdkconfig.board.s3-wifi              la placa Wi-Fi
├── secrets/                             ejemplos de ficheros de flota y nodo
├── build-test.sh build-test.bat         ejecutar las pruebas con el flujo compartido
└── .gitattributes .gitignore            ajustes de Git
```

</details>""",
      "roadmap": r"""**Límites conocidos hoy**

* Los decodificadores LD2461 y de presencia solo coinciden con los ejemplos de sus manuales, sin módulo detrás; el canal de órdenes del radar no se ha comprobado con otro módulo que el LD2450.
* La comprobación de la firma de las actualizaciones y el emparejado Bluetooth con PIN están probados en un ordenador con firmas reales pero no aún en la placa; el handshake TLS con el broker no se ha ejecutado en una placa.
* El informe de salud y el control desde el servidor no han corrido en la placa; el motor de perímetro nunca ha corrido con un sensor; el certificado HTTPS propio del panel no se ha probado en todos los navegadores; la placa Wi-Fi no tiene placa física (solo existe la de Ethernet).

**Lo siguiente**

* Ejecutar el motor de perímetro, el informe de salud y las órdenes de control con sensores reales y el banco CM5; probar el enlace TLS con el broker y la actualización firmada en la placa.""",
    },
  },
  "de": {
    "tagline": "Feldknoten-Firmware (Waveshare ESP32-S3-ETH, drei Radare oder Präsenzsensoren, Ethernet und WLAN) mit eigenem Web-Panel und ihrem am Rechner getesteten Kern",
    "honest": "Der Radarknoten ist der einzige Knoten, der als Hardware existiert: Seine Firmware läuft auf einer echten Waveshare-ESP32-S3-ETH-Platine mit einem Radar und meldet an den CM5-Testaufbau, und sein Web-Panel und die Over-the-Air-Updates werden dort genutzt. Der hardwareunabhängige Kern (4,633 Prüfungen in 14 Testprogrammen: die Decoder des LD2450, des LD2461 und von vier Präsenzsensoren, der Befehlskanal des LD2450, die Einstellungen und ihre Prüfungen, die Pin-Tabelle, Benutzer und Sitzungen, der Netzplan, der Nachrichten-Serialisierer, dessen Ausgabe ARMOR-COMMON akzeptiert, und die Versions- und Signaturprüfungen) wird auf einem Computer getestet, das **Web-Panel** wurde in einem echten Browser gegen einen Ersatzknoten geprüft und das **Firmware-Abbild baut** im ESP-IDF-5.5.5-Container. **Noch nicht** bewiesen: Die Decoder des LD2461 und der Präsenzsensoren entsprechen nur den durchgerechneten Beispielen ihrer Handbücher, ohne Modul dahinter; die Signaturprüfung der Updates und die Bluetooth-Kopplung mit PIN sind auf dem Computer mit echten Signaturen bewiesen, aber noch nicht auf der Platine; der Befehlskanal des Radars ist nicht gegen ein Modul geprüft; und das HTTPS-Zertifikat des Panels (vom Knoten selbst erzeugt) ist nicht in allen Browsern erprobt.",
    "glance": [
      [
        "Rolle",
        "Radar-Feldknoten für ESP32-S3 (Familie: Field Nodes, übergeordnet: ARMOR-COMMON)",
      ],
      [
        "Technik",
        "C++17, ESP-IDF 5.5.5, ESP32-S3",
      ],
      [
        "Tests",
        "7371 Prüfungen in 14 Host-Programmen und 6 Python-Prüfungen (`ctest`)",
      ],
      [
        "Platinen",
        "Waveshare ESP32-S3-ETH (Ethernet) und ESP32-S3-WROOM-1 N16R8 (nur WLAN)",
      ],
      [
        "Sensoren",
        "Bis zu 3 Radare (LD2450, LD2461) oder Präsenzsensoren je Knoten, Lichtsensor VEML7700",
      ],
      [
        "Läuft auf",
        "Waveshare ESP32-S3-ETH oder ESP32-S3-WROOM-1 N16R8; Host-Tests auf jedem Computer",
      ],
      [
        "Auf echter Hardware",
        "Läuft auf einer echten Waveshare-ESP32-S3-ETH-Platine mit einem Radar und meldet an den CM5-Testaufbau",
      ],
      [
        "Lizenz",
        "GPL-3.0-or-later",
      ],
    ],
    "status": {
      "software": "Die Firmware wird im ESP-IDF-5.5.5-Container gebaut und läuft auf einer echten ESP32-S3-ETH-Platine.",
      "tests": "7.371 Prüfungen in 14 Host-Programmen bestehen (`ctest`): die Dekoder, die Einstellungen, die Pin-Tabelle, die Benutzer, der Netzplan, der Nachrichten-Serialisierer und die Versionsprüfungen.",
      "protocols": "Der LD2450 läuft an einem echten Radar; die Dekoder des LD2461 und der vier Anwesenheitssensoren stimmen nur mit den Beispielen ihrer Handbücher überein, und der Befehlskanal des Radars ist nicht an einem Modul geprüft.",
      "ui": "Das Web-Panel wird auf der Platine genutzt und in einem echten Browser gegen einen nachgebildeten Knoten erprobt; sein vom Knoten selbst erzeugtes HTTPS-Zertifikat ist nicht in jedem Browser erprobt.",
      "hardware": "Es ist der einzige Knoten, den es als Hardware gibt: eine echte Waveshare-ESP32-S3-ETH-Platine mit einem Radar meldet an den CM5-Prüfstand; kein anderes Sensormodul ist angeschlossen.",
      "security": "Die Kopplung per Bluetooth-PIN und die Prüfung der Update-Signatur sind auf einem Rechner mit echten Signaturen belegt, aber noch nicht auf der Platine; es gab keine unabhängige Prüfung.",
      "updates": "Aktualisierungen über die Luft werden auf der Platine genutzt; die Prüfung signierter Aktualisierungen lief dort noch nicht.",
      "integration": "Die Nachrichten der Platine erreichen den Server des CM5-Prüfstands, und dieselben Nachrichten werden von den gemeinsamen Schemas und Konformitätsvektoren von ARMOR-COMMON akzeptiert. Nur auf dem Prüfstand gesehen, nicht in einer Installation.",
      "docs": "Acht Sprachen und das Änderungsprotokoll sind aktuell.",
    },
    "docs": [
      "[Knoten-Panel](docs/NODE_PANEL.md): erster Start, Benutzer, Netz, die Panel-Seiten",
      "[Einrichtungscode](docs/SETUP_CODE.md) und [Bluetooth-Einrichtung](docs/BLE_PROVISIONING.md)",
      "[Sensoren](docs/SENSORS.md): die sechs Modelle und ihre Decoder",
      "[Prüfstand-Inbetriebnahme](docs/BENCH_BRINGUP.md), [Prüfstandtests](docs/BENCH_TESTS.md) und [Hardware-Grenze](docs/HARDWARE_BOUNDARY.md)",
    ],
    "contributing_first": "Führe vor einem Pull Request `ctest --test-dir build/host` and `python -I tools/armor_ci_validate.py` aus: Es muss bestehen. Siehe [CONTRIBUTING.md](CONTRIBUTING.md) und den [Verhaltenskodex](CODE_OF_CONDUCT.md).",
    "languages_extra": "",
    "body": {
      "overview": r"""* **Zwei Platinen, eine Firmware:** die Waveshare ESP32-S3-ETH (Ethernet, Standard) und ein ESP32-S3-WROOM-1 N16R8 ohne Ethernet (nur WLAN: die Einrichtung fragt nach dem WLAN zum Beitreten, und der Knoten behält immer sein eigenes Netz). Das Image wird beim Bauen gewählt (`tools/build_node.sh generic s3-eth` oder `generic s3-wifi`); Pin-Tabelle und Zugangsweg folgen der Platine, das Panel blendet aus, was die Platine nicht hat, und ein Image gilt nur für seine Platine. Beide bauen und sind am Rechner getestet; keine lief je auf einer Platine.
* **Ein Knoten deckt bis zu 270 Grad ab:** jedes Waveshare ESP32-S3-ETH liest bis zu drei LD2450-Radare an seinen drei UARTs, im Abstand von 75 Grad montiert, über kabelgebundenes Ethernet (W5500) mit DHCP oder fester Adresse, gespeist per PoE oder USB. Studios *Add a 270° node* legt die drei Radare bereits dem Knoten zugeordnet an.
* **Ein Web-Panel auf jedem Knoten,** im Aussehen von Studio und in acht Sprachen, in die Firmware eingebettet: Übersicht, Netzwerk, WLAN, Broker, Radare, Pins, Benutzer, Firmware-Update und Protokoll. Ein Knoten ohne Benutzer öffnet das WLAN `ARMOR-SETUP-xxxxxx` und legt mit einem Einrichtungscode seinen ersten Administrator an; Passwörter sind gesalzenes PBKDF2, Sitzungen zufällige Token, und jede Einstellung liegt im Flash des Knotens, sodass ein Image alle Knoten bedient und kein Passwort einkompiliert ist ([das Panel](docs/NODE_PANEL.md)).
* **Ein WLAN aus vielen Knoten:** jeder Knoten kann einen an seinen Ethernet-Port angebundenen Access Point anbieten; mit gleichem Namen und Passwort und dem Kanal auf automatisch (1, 6 oder 11 nach MAC) sehen Telefone und WLAN-Sensoren ein Netz mit einem DHCP-Server. Es ist kein Funk-Mesh: jeder Knoten behält sein Kabel. Ein Knoten kann stattdessen dem WLAN eines Routers beitreten (mit Netzwerksuche), und einer ohne Kabel lässt sich per **Bluetooth** über die Android-App konfigurieren.
* **Pins für den Server:** jeder freie Pin wird zu einem Eingang, einem Ausgang (mit sicherem Zustand bei Verlust des Brokers), PWM oder einer analogen Messung und erscheint als Gerät des Servers, sodass ein Relais oder ein Kontakt keine neue Firmware braucht. Die reservierten Pins der Platine werden nie angeboten.
* **Over-the-Air-Updates mit Rollback** aus dem Panel (zwei Slots im 16-MB-Flash) und ein **Link aus Studio** zum Panel jedes Knotens, über die Adresse, die der Knoten veröffentlicht.
* **Das Panel über HTTPS:** der Knoten erzeugt sein eigenes Zertifikat (selbstsigniert, im Flash gehalten) und bedient das Panel auf Port 443 zusätzlich zu 80 oder nur auf 443; das Sitzungs-Cookie ist als Secure markiert und der Fingerabdruck des Zertifikats wird zum Vergleich mit der Browserwarnung angezeigt.
* **Stabile Spur-Identitäten:** die Ziele jedes Rahmens werden den zuvor verfolgten zugeordnet, sodass eine Person dieselbe Spur-ID behält, ein verlorener Rahmen nicht flackert und die Positionen leicht geglättet werden.
* **Sechs Sensormodelle, eines je Port:** ein Port trägt einen LD2450 oder LD2461 (Tracker, die den Perimeter speisen, mit dem eigenen Feld des Modells in Studio) oder einen Präsenzsensor (LD2410, LD2412, LD2410S, MR24HPC1), der zum Gerät des Servers wird und Anwesenheit und Entfernung veröffentlicht. Im Panel gewählt; was jeder ist, sein Protokoll und was nicht geprüft wurde, steht in `docs/SENSORS.md`.
* **LD2450-Dekoder, Zustand und Konfiguration:** ein neu synchronisierender Rahmenfinder findet Rahmen in einem verrauschten Strom; jeder 30-Byte-Rahmen liefert bis zu drei Ziele, die zu Vertragsspuren werden; Konsole und Panel sagen je Radar, ob es meldet, schweigt oder Unsinn sendet. Das Panel kann auch die Version des Moduls lesen, ein oder drei Ziele wählen und Erkennungszonen setzen (ein an einem Modul ungeprüftes Protokoll).
* **Umgebungslicht und vertragsgenaue Nachrichten:** der VEML7700 mit automatischem Bereich; Telemetrie-, Zustands- und Informations-JSON folgt den veröffentlichten Schemas und weigert sich, Ungültiges zu schreiben, mit Wanduhr-Zeitstempeln (SNTP) und einem MQTT-Last-Will. Telemetrie wird zurückgehalten, solange kein Radar meldet, nie eine leere „Entwarnung“.
* **Ein Image für jede Platine, wie ein Netzwerkprodukt:** die Firmware ist dieselbe und die MAC unterscheidet die Platinen (`armor-` und sechs Ziffern bis zur Benennung); `adopt_node.py` gibt einem frisch geflashten Knoten über das Netzwerk seinen Administrator, seine Broker-Identität und die gemeinsamen Einstellungen der Flotte, mit einem aus seiner MAC berechneten Einrichtungscode: 5 Knoten oder 27 sind dieselbe Arbeit.
* **Werkzeuge am Prüfstand:** Flashen per USB-C, ein Stellvertreter-Knoten zum Arbeiten am Panel und ein Konverter von einem Protokoll roher Rahmen zu einem Testfixture ([Inbetriebnahme am Prüfstand](docs/BENCH_BRINGUP.md)).
* **Signierte Over-the-Air-Updates:** der Knoten installiert von GitHub nur ein Abbild, dessen SHA-256 stimmt und das eine gültige Ed25519-Signatur des Betreuers trägt (der öffentliche Schlüssel steckt in der Firmware, der private verlässt den Betreuer nie); eine von einem Administrator im Panel von Hand hochgeladene Datei wird weiterhin akzeptiert. Seiten und Meldungen des Panels sind in acht Sprachen.
* **Bluetooth-Kopplung mit PIN:** die sechsstellige PIN wird aus dem Einrichtungscode abgeleitet, auf der USB-Konsole ausgegeben und einem Administrator im Panel angezeigt; das Telefon muss sie eingeben, bevor es die Einstellungen des Knotens schreiben darf.
* **Nur das Haus darf das Panel nutzen:** Das Panel antwortet standardmäßig dem privaten Netz (oder den Netzen, die der Besitzer nennt, etwa einem VPN), lehnt eine Liste ab, die den Speichernden aussperren würde, zählt falsche Passwörter je Person und je Adresse und funktioniert hinter dem Proxy des Servers, sodass man es von außerhalb des Hauses erreicht, ohne den Knoten zu veröffentlichen.
* **Optionale verschlüsselte Verbindung zum Broker (TLS):** standardmäßig aus, der Knoten spricht also wie bisher unverschlüsseltes MQTT. Ein Schalter und ein Feld für das Zertifikat der eigenen Zertifizierungsstelle der Anlage (PEM, höchstens 2 KB) auf der Broker-Seite sorgen dafür, dass er sich mit `mqtts://` verbindet, nur dieser Stelle vertraut und prüft, ob das Zertifikat des Brokers für die erreichte Adresse ausgestellt wurde; alles, was nicht genau ein PEM-Zertifikat ist, wird abgelehnt. Durch Host-Tests abgedeckt; der Handshake wurde auf einer Platine noch nicht ausgeführt.
* **Zustandsbericht:** etwa einmal pro Minute veröffentlicht der Knoten, wie lange er läuft und warum er zuletzt neu gestartet ist, seinen freien Speicher, seine Verbindung und sein WLAN-Signal, wie oft er sich mit dem Broker verbunden hat und den letzten protokollierten Fehler (`armor/health/<Knoten>`, der Vertrag `node_health` von ARMOR-COMMON). Der Code, der ihn erzeugt, wird von allen Knoten geteilt und auf einem Computer getestet; auf einer Platine ist er noch nicht gelaufen.
* **Steuerung vom Server aus:** Studio kann den Knoten sauber neu starten, bis zu einer Stunde pausieren (er läuft von selbst weiter), seine Arbeit in den Standby setzen (ohne Ende, über Neustarts hinweg gespeichert, der Knoten bleibt verbunden und antwortet weiter), ihn sich zeigen lassen, einen Diagnose-Schnappschuss anfordern und ihn als in Wartung markieren (`armor/control/<Knoten>/...`, der Vertrag `node_control` von ARMOR-COMMON). Jeder Befehl besteht aus zwei Schritten mit einem Einmal-Token, das zu dieser Operation gehört; nur der Server darf sie am Broker schreiben, und es gibt kein Zurücksetzen auf Werkseinstellungen, kein Löschen und keinen Tiefschlaf. Solange der Knoten pausiert oder im Standby ist, veröffentlicht er weder Ziele noch Anwesenheit (der Herzschlag meldet weiter, dass er da ist). Der Code wird von allen Knoten geteilt und auf einem Rechner getestet; auf einer Platine ist er noch nicht gelaufen.
* **Eine Perimeter-Engine auf dem Knoten (standardmäßig aus):** sechs Erkennungszonen und drei Ausschlusszonen, jeweils ein Rechteck, das um einen Winkel gedreht werden kann, drei Stolperdrahtlinien, die Überschreitungen nach Richtung zählen, drei Eintrittspfade, Haustier-Immunität und Maskierungserkennung. Sie läuft neben den Sensoren, funktioniert also auch ohne Broker-Verbindung, behält ihre Ereignisse, solange der Broker fehlt, und veröffentlicht sie auf `armor/radar/<Knoten>/events`; der Zoneneditor ist im Panel des Knotens. Nichts davon ist bisher mit einem Sensor auf einer Platine gelaufen.
* **Wer jeder Sensor ist, und sein eigenes Bluetooth geschlossen:** Beim Start liest der Knoten Firmware-Version und Bluetooth-Adresse jedes Sensors, schließt standardmäßig das eigene Bluetooth der Sensoren (es verlangt keine PIN) und kann die serielle Leitung eines Sensors für einige Minuten an ein PC-Werkzeug eines Administrators übergeben (eine transparente serielle Brücke). `GET /metrics` für Administratoren sowie Export und Alles-oder-nichts-Import der Einstellungen runden es ab.
* **Diagnose ohne Kabel:** Nach einem unsauberen Start (Absturz, Watchdog, Spannungseinbruch, fehlgeschlagene Speicherreservierung) nennt der Gesundheitsbericht zehn Minuten lang den Grund; ein Absturz hinterlässt sein Core-Dump, das man im Panel ansehen, herunterladen oder löschen kann; die gespeicherten Einstellungen werden vor jeder Firmware-Installation kopiert und wiederhergestellt, falls ein Update sie beschädigt; und ein Administrator kann den Knoten über den Server mit einem Einmal-Token nach einem Diagnosepaket oder seinem Protokoll fragen.
* **Übernahme per HTTPS mit festgelegtem Fingerabdruck:** `tools/adopt_node.py` akzeptiert `https://<Adresse>` mit `--fingerprint` (der SHA-256 des Knotenzertifikats, geprüft auf der Verbindung, die die Anfrage trägt) oder `--show-fingerprint`, um ihn zu lesen; es warnt vor unverschlüsseltem HTTP und vor einer Flottendatei mit fester Adresse oder Hostnamen, und auch das Panel warnt beim Import einer solchen Datei.
* **Der Sensorleser wartet auf Ereignisse statt abzufragen:** Die Lese-Task schläft auf den Ereigniswarteschlangen der seriellen Leitungen und leert alles Eingegangene, leert die Leitung bei einem Überlauf und zählt Überläufe und Fehler je Leitung; `system.reader_idle_ms` (100; 0 = die frühere Abfrage im 10-ms-Takt) legt die Wartezeit fest, und eine ausfallende Warteschlange führt von selbst zur Abfrage zurück.
* **Optionales Versiegeln gespeicherter Geheimnisse:** standardmäßig aus (`security.seal_secrets` oder `nodes.nvs_encryption` des Servers). Eingeschaltet werden die Passwörter, Token, Schlüssel, PINs und Passwort-Hashes, die der Knoten speichert, mit ChaCha20-Poly1305 versiegelt, alles andere bleibt lesbar; Ein- und Ausschalten schreibt sie ohne Verlust um, auch wenn der Knoten mittendrin stehen bleibt. Es wird kein eFuse gebrannt und der Flash nicht verschlüsselt: Der Schlüssel liegt in einer Partition desselben Chips und schützt daher **nicht** vor jemandem, der die Platine hat; ein Knoten, der vor dieser Partition installiert wurde, behält seine Geheimnisse unverändert, bis er mit der neuen Partitionstabelle geflasht wird.""",
      "role": r"""ARMOR-NODE-RADAR sind die Augen des Perimeters. Jeder Knoten liest bis zu drei Radare oder Präsenzsensoren und veröffentlicht Spuren, Licht und Zustand per MQTT an [ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER); [ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) zeichnet sie in den Standortplan, und [ARMOR-SERVER-AI](https://github.com/JuanenRac/ARMOR-SERVER-AI) wägt sie gegen die Kameras ab. Seine Firmware teilt eine Basis mit den anderen Knoten (Panel, Bluetooth-Einrichtung, signierte Updates, Anmeldung und Uhr stammen aus der Firmware-Basis von [ARMOR-COMMON](https://github.com/JuanenRac/ARMOR-COMMON)), sodass das, was man an einem Knoten lernt, für alle gilt.

| Name | Wie | Wozu |
|---|---|---|
| ARMOR-SERVER | MQTT `armor/node/<id>/telemetry|health|info|command` | Empfängt die Radarnachrichten (heute der CM5-Prüfstand) und steuert den Knoten |
| ARMOR-STUDIO | Link zum Panel | Öffnet das Panel des Knotens unter der vom Knoten veröffentlichten Adresse |
| ARMOR-ANDROID-CONTROL | Bluetooth | Richtet den Knoten vor Ort ein |
| ARMOR-COMMON | Verträge, Firmware-Basis | Die Nachrichten werden gegen seine Schemas geprüft; die gemeinsame Firmware stammt daraus |""",
      "architecture": r"""<p align="center">
  <img src="images/architecture.svg" alt="Architektur von ARMOR-NODE-RADAR: wer es aufruft, was es enthält und wovon es abhängt" width="100%">
</p>""",
      "security": r"""| Bedrohung | Abwehr |
|---|---|
| Passwörter im Klartext oder einkompiliert | PBKDF2-HMAC-SHA256 mit 10 000 Runden; kein Passwort in der Firmware (ein Knoten ohne Benutzer geht in die Einrichtung); höchstens 4 Benutzer (Admin oder Betrachter) und 8 bis 64 Zeichen; höchstens 6 Sitzungen, 30 Minuten Leerlauf |
| Einen frisch geflashten Knoten übernehmen | Die Einrichtung braucht einen Startcode: den des Builds (`CONFIG_ARMOR_SETUP_CODE`) oder einen zufälligen im Flash, der auf der USB-Konsole erscheint; mit Flottengeheimnis ist er `HMAC-SHA256(Geheimnis, MAC)`; er ist auch der Schlüssel des Einrichtungs-WLANs (WPA2, nie überbrückt) |
| Das Panel aus dem Internet erreicht | Es antwortet standardmäßig den privaten Netzen eines Hauses (10/8, 172.16/12, 192.168/16, 169.254/16, 127/8 und 100.64/10, wo manche VPNs liegen); die Einstellung `web.admin_sources` listet weitere IPv4-Adressen und Netze (8 Einträge, 120 Zeichen); alles außerhalb wird abgewiesen außer der öffentlichen Identität `GET /api/v1/session`; eine Liste, die den Speichernden aussperren würde, wird abgelehnt |
| Das Panel im Klartext über HTTP | HTTPS auf 443 mit einem vom Knoten selbst erzeugten Zertifikat (selbstsigniert, im Flash, SHA-256-Fingerabdruck zum Vergleichen sichtbar); das Panel kann http, https oder beides sein; das Sitzungscookie ist immer HttpOnly und SameSite=Strict (und Secure über TLS) |
| Eine gefälschte Firmware von GitHub | Ein Image wird nur mit passendem SHA-256 und gültiger Ed25519-Signatur mit dem Schlüssel des Maintainers installiert (`no_checksum`, `no_signature`, `bad_signature`, `checksum_mismatch`, `wrong_firmware`, `not_newer`, `version_mismatch` lehnen es ab); ein manueller Upload durch einen Administrator wird nicht geprüft: eine ausdrückliche Grenze |
| Kapern der Bluetooth-Einrichtung | Eine 6-stellige PIN, abgeleitet vom Einrichtungscode, auf der USB-Konsole und für einen Administrator sichtbar; das Telefon muss sie vor dem Schreiben von Einstellungen eingeben; das Einrichtungsfenster dauert `CONFIG_ARMOR_BLE_SETUP_MINUTES` (standardmäßig 10, 1 bis 120) |
| Ein ferner Befehl, der Schaden anrichtet | Zwei Schritte mit einem Einmal-Token, das an diese Operation gebunden ist; nur der Server darf diese Topics im Broker schreiben; eine Pause dauert höchstens eine Stunde; es gibt weder Werksreset noch Löschen noch Tiefschlaf per Fernbefehl |
| Gespeicherte Geheimnisse, gelesen von jemandem mit der Platine | Optional (standardmäßig aus, Schalter `security.seal_secrets` oder `nodes.nvs_encryption` des Servers): ChaCha20-Poly1305 für Passwörter, Token, Schlüssel, PINs und Hashes. Es verschlüsselt nicht den Flash und brennt kein eFuse: Der Schlüssel liegt in einer Partition desselben Chips und schützt daher nicht vor dem, der die Platine hat |
| Die Broker-Verbindung im Klartext | Optionales TLS (`mqtts://`) mit der eigenen Zertifizierungsstelle des Besitzers (PEM bis 2 KB) und Namensprüfung; standardmäßig aus. Der Handshake lief nur in Host-Tests, nicht auf einer Platine |
| Das eigene Bluetooth eines Sensors | Standardmäßig schließt der Knoten das Bluetooth jedes LD-Sensors (ohne PIN); eine transparente serielle Brücke zu einem Rechner öffnet nur für wenige Minuten und nur durch einen Administrator |
| Einen Knoten in einem nicht vertrauenswürdigen Netz übernehmen | `tools/adopt_node.py https://<Adresse> --fingerprint <SHA-256>` prüft das Zertifikat in derselben Verbindung; es warnt vor Klartext-HTTP und Flottendateien mit fester Adresse |
| Ein gefährlicher Pin | Die reservierten Pins der Platine werden nie angeboten; ein Ausgang hat einen sicheren Zustand, wenn der Broker verloren geht; zwei Funktionen können keinen Pin teilen (geprüft) |
| Eine öffentliche Firmware mit Flottengeheimnis | `CONFIG_ARMOR_FLEET_SECRET` ist standardmäßig leer: Der öffentliche Build trägt kein Geheimnis |

Lies [SECURITY.md](SECURITY.md), um eine Schwachstelle zu melden. Es gab keine unabhängige Prüfung.""",
      "interfaces": r"""| Teil | Was sie festlegt |
|---|---|
| MQTT | `armor/node/<id>/{telemetry,health,info,command}`, `armor/health/<id>` (sein Last Will ist `{"node_id":"..","online":false}`), `armor/control/<id>/{command,result,maintenance}` und `armor/control/all/command`, `armor/device/<id>/<pin>/{state,set}`, `armor/radar/<id>/events`, `armor/radar/<id>/control/armed` |
| Panel (HTTP 80, HTTPS 443) | Routen `session`, `login`, `logout`, `setup`, `status`, `config` (+ export, import), `wifi/scan`, `time`, `radars` (+ command), `perimeter` (+ armed, learn, zone), `pins` (+ command), `bridge` (+ open, close, io), `ota` (+ check, install, progress, copy, switch), `account`, `ble-pin`, `log`, `coredump`, `factory-reset`, `reboot`; `/metrics` für Administratoren und der WebSocket `/ws/radar-map`; `tests/check_routes.py` prüft, dass jede vom Panel aufgerufene Route existiert |
| Panel-Texte | 76 Fehlercodes mit Text in acht Sprachen (832 Zeilen in `panel/text.js`), geprüft von `tests/check_panel_text.py` |
| Hardware | 3 UARTs für LD2450, LD2461, LD2410, LD2412, LD2410S und MR24HPC1 (RX 16, 17, 18; TX 15, 21, 38); W5500 über SPI (MOSI 11, MISO 12, SCLK 13, CS 14, INT 10, RST 9, 20 MHz); VEML7700 am I2C (GPIO 1 und 2); BOOT-Taste |""",
      "configuration": r"""| Variable | Standard | Was sie festlegt |
|---|---|---|
| `CONFIG_ARMOR_NODE_ID` | `""` | Der Name; leer ergibt `armor-` und die letzten drei Bytes der MAC |
| `CONFIG_ARMOR_SETUP_CODE`, `CONFIG_ARMOR_FLEET_SECRET` | `""` | Der Einrichtungscode des Builds (leer: zufällig) und das Flottengeheimnis (16+ Zeichen; nie im Repository) |
| `CONFIG_ARMOR_RADAR_COUNT` | 3 (0-3) | Wie viele Radare angeschlossen sind |
| `CONFIG_ARMOR_TRACK_STABILISER` | y | Die Identität einer Spur von Bild zu Bild behalten |
| `CONFIG_ARMOR_MQTT_URI`, `_USERNAME`, `_PASSWORD` | `""` | Die ersten Broker-Einstellungen (im Panel änderbar) |
| `CONFIG_ARMOR_HEARTBEAT_S` | 10 (2-300) | Sekunden zwischen Gesundheitssignalen |
| `CONFIG_ARMOR_TELEMETRY_PERIOD_MS` | 200 (200-5000) | Höchstens 5 Nachrichten pro Sekunde |
| `CONFIG_ARMOR_BLE_SETUP_MINUTES` | 10 (1-120) | Wie lange die Bluetooth-Einrichtung offen bleibt |
| `CONFIG_ARMOR_BOARD_S3_ETH` / `_S3_WIFI` | eth | Die Platine: Waveshare ESP32-S3-ETH oder ESP32-S3-WROOM-1 N16R8 (nur WLAN) |
| `CONFIG_ARMOR_BOOT_FACTORY_RESET` | y | BOOT 8 s in den ersten 30 s halten, um neu zu beginnen |
| `system.login_limit_per_minute` | 30 (0-120) | Falsche Passwörter pro Minute, bevor das Panel die Anmeldung für alle sperrt (0 = kein globales Limit); in Studio (eine Schaltfläche an jedem Knoten) oder mit `POST /api/v1/admin/nodes/settings` lesen und ändern, wobei die Panel-Anmeldung einmal benutzt und nie gespeichert wird |

Die live abgestimmten Einstellungen stehen im Panel und liegen im Flash (zum Beispiel `system.reader_idle_ms`, `security.seal_secrets`, das Limit fehlgeschlagener Anmeldungen pro Minute (30, 0 bis 120) und die Zonen der Perimeter-Engine); die Standardwerte der Firmware stehen in `sdkconfig.defaults` und `sdkconfig.board.*`. Der 16-MB-Flash enthält `nvs` (64 KB), `otadata`, `phy_init`, zwei 3-MB-Slots `ota_0` und `ota_1`, `coredump` (128 KB) und `nvs_keys` (4 KB) (`partitions.csv`).""",
      "quickstart": r"""**Voraussetzungen:** ein C++17-Compiler für die Host-Tests; der ESP-IDF-5.5.5-Container zum Bauen des Images; ein Waveshare ESP32-S3-ETH oder ein ESP32-S3-WROOM-1 N16R8.

```bash
cmake -S tests -B build/host && cmake --build build/host && ctest --test-dir build/host   # host tests, -Werror
node tools/panel_mock.mjs --user admin:adminpass123   # the panel without a board
python tools/make_fleet.py                             # once: the fleet secret and the shared settings
tools/build_node.sh generic                           # ONE image for every Waveshare board (dist/generic-s3-eth.bin), in the ESP-IDF container
tools/build_node.sh generic s3-wifi                   # the same firmware for an ESP32-S3-WROOM-1 N16R8 with no Ethernet
```

```bat
tools\flash.bat generic COM5 monitor                  # each Waveshare board, once, by USB-C (add s3-wifi for the other board)
```

```bash
tools/adopt_node.py 192.168.0.181 --id perimetro-3 --fleet secrets/fleet.json --broker-ssh-host <cm5> --broker-ssh-user <user>
```

Die Rechnertests brauchen einen C++17-Compiler (Linux, WSL, MSYS2). Siehe die [Inbetriebnahme am Prüfstand](docs/BENCH_BRINGUP.md), das [Panel](docs/NODE_PANEL.md) und die [Hardwaregrenze](docs/HARDWARE_BOUNDARY.md).""",
      "testing": r"""```bash
cmake -S tests -B build/host && cmake --build build/host && ctest --test-dir build/host
build/host/emit_samples | python tests/check_contract.py
python -I tools/armor_ci_validate.py
```

14 Host-Testprogramme und 6 Python-Prüfungen laufen unter `ctest`; 7371 Prüfungen, gezählt von den Host-Programmen, mit `-Werror` gebaut.

| Teil | Was sie abdeckt |
|---|---|
| `test_core`, `test_sensors`, `test_family`, `test_uart_wake` | Die Decoder (LD2450, LD2461, vier Präsenzsensoren), der Framer, der Befehlskanal, die Sensorfamilien und das Wecken der UART |
| `test_node`, `test_base`, `test_shared`, `test_board_wifi` | Die Einstellungen und ihre Prüfungen, die Pin-Tabelle, Benutzer und Sitzungen, der Netzplan, die gemeinsame Basis und die WLAN-Platine |
| `test_logic`, `test_perimeter`, `test_control`, `test_diag` | Die Pin-Logik, die Perimeter-Engine, die zweistufigen Steuerbefehle und die Diagnose |
| `test_mqtt_tls`, `test_release` | Die TLS-Verbindung zum Broker (nur Host) und die Release- und Signaturprüfungen |
| `check_panel_text`, `check_task_safety`, `check_save_paths`, `check_ble_session`, `check_routes`, `check_bridge_client` | Python: die Panel-Texte in acht Sprachen (832 Zeilen), die Tasks, die Speicherpfade, die Bluetooth-Sitzung unter ihrer Sperre, die Routen und der Seriellbrücken-Client |

Das Web-Panel wird außerdem in einem echten Browser gegen einen Ersatzknoten (`tools/panel_mock.mjs`) geprüft. Die Decoder für LD2461 und Präsenz stimmen nur mit den Beispielen ihrer Handbücher überein.""",
      "build": "`tools/build_node.sh generic` baut EIN Image für jede Waveshare-Platine im ESP-IDF-5.5.5-Container, und `tools/flash.bat` schreibt es per USB-C; dieselbe Firmware wird mit `s3-wifi` für die reine WLAN-Platine gebaut. Releases tragen das Image, sein SHA-256 und seine Ed25519-Signatur, je eines pro Platine.",
      "troubleshooting": r"""| Sie sehen | Weil | Tun Sie |
|---|---|---|
| Du hast das Passwort verloren oder der Knoten tritt dem Netz nicht mehr bei | Ein Knoten in der Einrichtung ohne Adresse nach 90 s öffnet ein eigenes WLAN `ARMOR-SETUP-xxxxxx` (öffne `http://192.168.4.1/`) | Zum Neustart BOOT 8 Sekunden in den ersten 30 Sekunden nach dem Einschalten halten (löscht Einstellungen und Benutzer) oder im Panel *Werksreset* nutzen |
| Ein Update von GitHub wird abgelehnt | Die Version enthält keine Prüfsumme oder Signatur, sie passen nicht (`e_no_checksum`, `e_no_signature`, `e_checksum_mismatch`, `e_bad_signature`), hat kein Image für diese Platine (`e_no_asset_for_board`) oder gehört zu einem anderen Projekt (`e_wrong_firmware`) | Der Knoten blieb unverändert; erneut versuchen oder einen Administrator die Datei von Hand hochladen lassen |
| Die Radar-Befehle antworten `no_answer`, `refused` oder `disabled` | Die TX-Leitung des Radars ist nicht angeschlossen, das Modul hängt, oder der Knoten schließt zuerst sein Bluetooth | Prüfe die Verdrahtung (siehe Prüfstand-Inbetriebnahme), starte das Modul im Panel neu |
| Der Knoten zeigt Sensor 3 nicht oder lässt ein Radar schlafen | Das Modul hat aufgehört zu senden (Stille ohne fehlerhafte Frames) | Nutze *Modul neu starten* auf der Radar-Seite und schließe dann das eigene Bluetooth des Sensors |""",
      "structure": r"""<p align="center">
  <img src="images/repository-structure.svg" alt="Repository-Struktur von ARMOR-NODE-RADAR" width="100%">
</p>

<details>
<summary>Textversion des Baums</summary>

```text
ARMOR-NODE-RADAR/
├── main/                                die Firmware: eine ESP-IDF-Komponente
├── panel/                               das im Firmware eingebettete Web-Panel
├── tests/                               Host-Tests und Python-Prüfungen
├── docs/                                7 Anleitungen für Prüfstand und Panel
├── tools/                               Werkzeuge für Build, Flashen, Adoption, Flotte und Prüfung
├── .github/                             CI-Workflow sowie Vorlagen für Issues und Pull Requests
├── images/                              Banner, Symbol und die zwei Bilder dieses READMEs
├── build.sh build.bat                   Build über den gemeinsamen Projekt-Workflow
├── test.sh test.bat                     Tests über den gemeinsamen Workflow ausführen
├── run.sh run.bat                       Start über den gemeinsamen Projekt-Workflow
├── armor.project.json                   Manifest: Version, Rolle, Reifegrad, Build-Befehl
├── CHANGELOG.md                         was sich in jeder Version geändert hat
├── SECURITY.md SUPPORT.md LICENSE       Sicherheitsrichtlinie, Support und Lizenz
├── CONTRIBUTING.md CODE_OF_CONDUCT.md   Mitwirkung und Verhaltenskodex
├── CMakeLists.txt                       das ESP-IDF-Projekt
├── partitions.csv                       die Flash-Tabelle
├── sdkconfig.defaults                   die Firmware-Einstellungen
├── sdkconfig.board.s3-eth               die Ethernet-Platine
├── sdkconfig.board.s3-wifi              die WLAN-Platine
├── secrets/                             Beispiele für Flotten- und Knotendatei
├── build-test.sh build-test.bat         Tests über den gemeinsamen Workflow ausführen
└── .gitattributes .gitignore            Git-Einstellungen
```

</details>""",
      "roadmap": r"""**Bekannte Grenzen heute**

* Die Decoder für LD2461 und Präsenz stimmen nur mit den Beispielen ihrer Handbücher überein, ohne Modul dahinter; der Befehlskanal wurde nur am LD2450 geprüft.
* Die Signaturprüfung der Updates und die Bluetooth-PIN-Kopplung sind am Rechner mit echten Signaturen belegt, aber noch nicht auf der Platine; der TLS-Handshake mit dem Broker lief auf keiner Platine.
* Der Gesundheitsbericht und die Steuerung vom Server liefen nicht auf der Platine; die Perimeter-Engine lief nie mit einem Sensor; das eigene HTTPS-Zertifikat des Panels ist nicht in jedem Browser erprobt; die WLAN-Platine gibt es nicht physisch (nur die Ethernet-Platine existiert).

**Als Nächstes**

* Perimeter-Engine, Gesundheitsbericht und Steuerbefehle mit echten Sensoren und dem CM5-Prüfstand ausführen; die TLS-Verbindung zum Broker und das signierte Update auf der Platine erproben.""",
    },
  },
  "fr": {
    "tagline": "Firmware de nœud de terrain (Waveshare ESP32-S3-ETH, trois radars ou capteurs de présence, Ethernet et Wi-Fi) avec son propre panneau web, et son cœur testé sur ordinateur",
    "honest": "Le nœud radar est le seul nœud qui existe en matériel : son firmware tourne sur une vraie carte Waveshare ESP32-S3-ETH avec un radar et rapporte au banc de test CM5, et son panneau web et ses mises à jour par radio y sont utilisés. Le cœur indépendant du matériel (4,633 vérifications dans 14 programmes de test : les décodeurs du LD2450, du LD2461 et de quatre capteurs de présence, le canal de commande du LD2450, les réglages et leurs contrôles, la table des broches, utilisateurs et sessions, le plan réseau, le sérialiseur de messages dont la sortie est acceptée par ARMOR-COMMON, et les contrôles de version et de signature) est testé sur un ordinateur, le **panneau web** a été exercé dans un vrai navigateur contre un nœud factice et l'**image du firmware se compile** dans le conteneur ESP-IDF 5.5.5. Ce qui n'est **pas** encore prouvé : les décodeurs du LD2461 et des capteurs de présence ne correspondent qu'aux exemples détaillés de leurs manuels, sans module derrière ; le contrôle de signature des mises à jour et l'appairage Bluetooth avec PIN sont prouvés sur ordinateur avec de vraies signatures mais pas encore sur la carte ; le canal de commande du radar n'est pas vérifié contre un module ; et le certificat HTTPS du panneau (fait par le nœud lui-même) n'est pas essayé dans tous les navigateurs.",
    "glance": [
      [
        "Rôle",
        "Nœud de terrain radar pour ESP32-S3 (famille : Field Nodes, parent : ARMOR-COMMON)",
      ],
      [
        "Technologie",
        "C++17, ESP-IDF 5.5.5, ESP32-S3",
      ],
      [
        "Tests",
        "7371 vérifications dans 14 programmes hôte et 6 contrôles Python (`ctest`)",
      ],
      [
        "Cartes",
        "Waveshare ESP32-S3-ETH (Ethernet) et ESP32-S3-WROOM-1 N16R8 (Wi-Fi seul)",
      ],
      [
        "Capteurs",
        "Jusqu'à 3 radars (LD2450, LD2461) ou capteurs de présence par nœud, capteur de lumière VEML7700",
      ],
      [
        "Fonctionne sur",
        "Waveshare ESP32-S3-ETH ou ESP32-S3-WROOM-1 N16R8 ; tests sur hôte sur n'importe quel ordinateur",
      ],
      [
        "Sur matériel réel",
        "Tourne sur une vraie carte Waveshare ESP32-S3-ETH avec un radar, en rapportant au banc de test CM5",
      ],
      [
        "Licence",
        "GPL-3.0-or-later",
      ],
    ],
    "status": {
      "software": "Le firmware compile dans le conteneur ESP-IDF 5.5.5 et tourne sur une vraie carte ESP32-S3-ETH.",
      "tests": "7 371 vérifications dans 14 programmes d'hôte réussissent (`ctest`) : les décodeurs, les réglages, la table des broches, les utilisateurs, le plan réseau, le sérialiseur de messages et les contrôles de version.",
      "protocols": "Le LD2450 tourne avec un vrai radar ; les décodeurs du LD2461 et des quatre capteurs de présence ne correspondent qu'aux exemples de leurs notices, et le canal de commandes du radar n'a pas été vérifié avec un module.",
      "ui": "Le panneau web est utilisé sur la carte et essayé dans un vrai navigateur contre un nœud simulé ; son certificat HTTPS, créé par le nœud lui-même, n'a pas été essayé dans tous les navigateurs.",
      "hardware": "C'est le seul nœud qui existe en matériel : une vraie carte Waveshare ESP32-S3-ETH avec un radar rend compte au banc d'essai CM5 ; aucun autre module de capteur n'est branché.",
      "security": "L'appairage par PIN Bluetooth et la vérification de la signature des mises à jour sont prouvés sur un ordinateur avec de vraies signatures mais pas encore sur la carte ; il n'y a pas eu de revue indépendante.",
      "updates": "Les mises à jour par voie hertzienne sont utilisées sur la carte ; la vérification des mises à jour signées n'y a pas encore tourné.",
      "integration": "Les messages de la carte arrivent au serveur du banc d'essai CM5, et ces mêmes messages sont acceptés par les schémas partagés et les vecteurs de conformité d'ARMOR-COMMON. Vu uniquement sur le banc d'essai, pas dans une installation.",
      "docs": "Huit langues et le journal des modifications sont à jour.",
    },
    "docs": [
      "[Panneau du nœud](docs/NODE_PANEL.md) : premier démarrage, utilisateurs, réseau, les pages du panneau",
      "[Code de configuration](docs/SETUP_CODE.md) et [mise en service Bluetooth](docs/BLE_PROVISIONING.md)",
      "[Capteurs](docs/SENSORS.md) : les six modèles et leurs décodeurs",
      "[Mise en service sur banc](docs/BENCH_BRINGUP.md), [essais de banc](docs/BENCH_TESTS.md) et [limite du matériel](docs/HARDWARE_BOUNDARY.md)",
    ],
    "contributing_first": "Avant une pull request, lancez `ctest --test-dir build/host` and `python -I tools/armor_ci_validate.py` : il doit réussir. Voir [CONTRIBUTING.md](CONTRIBUTING.md) et le [code de conduite](CODE_OF_CONDUCT.md).",
    "languages_extra": "",
    "body": {
      "overview": r"""* **Deux cartes, un firmware :** la Waveshare ESP32-S3-ETH (Ethernet, par défaut) et une ESP32-S3-WROOM-1 N16R8 sans Ethernet (Wi-Fi seul : sa configuration demande le réseau Wi-Fi à rejoindre et le nœud garde toujours son propre réseau). L'image se choisit à la compilation (`tools/build_node.sh generic s3-eth` ou `generic s3-wifi`) ; la table des broches et l'accès suivent la carte, le panneau masque ce que la carte n'a pas, et une image ne vaut que pour sa carte. Les deux compilent et sont testées sur ordinateur ; aucune n'a tourné sur une carte.
* **Un nœud couvre jusqu'à 270 degrés :** chaque Waveshare ESP32-S3-ETH lit jusqu'à trois radars LD2450 sur ses trois UART, montés à 75 degrés l'un de l'autre, par Ethernet filaire (W5500) en DHCP ou adresse fixe, alimenté en PoE ou USB. *Add a 270° node* de Studio crée les trois radars déjà associés au nœud.
* **Un panneau web sur chaque nœud,** à l'apparence de Studio et en huit langues, intégré au firmware : vue d'ensemble, réseau, Wi-Fi, broker, radars, broches, utilisateurs, mise à jour du firmware et journal. Un nœud sans utilisateur ouvre le Wi-Fi `ARMOR-SETUP-xxxxxx` et crée son premier administrateur avec un code d'installation ; les mots de passe sont en PBKDF2 salé, les sessions sont des jetons aléatoires et tous les réglages sont dans la flash du nœud, si bien qu'une image sert tous les nœuds et qu'aucun mot de passe n'est compilé ([le panneau](docs/NODE_PANEL.md)).
* **Un seul Wi-Fi à partir de plusieurs nœuds :** chaque nœud peut offrir un point d'accès relié à son port Ethernet ; avec le même nom et mot de passe et le canal en automatique (1, 6 ou 11 selon la MAC), téléphones et capteurs Wi-Fi voient un seul réseau avec un seul serveur DHCP. Ce n'est pas un maillage radio : chaque nœud garde son câble. Un nœud peut aussi rejoindre le Wi-Fi d'un routeur (avec recherche de réseaux), et un nœud sans câble peut être configuré en **Bluetooth** depuis l'application Android.
* **Broches pour le serveur :** toute broche libre devient une entrée, une sortie (avec un état sûr si le broker est perdu), du PWM ou une lecture analogique, et apparaît comme un appareil du serveur : un relais ou un contact n'exige aucun nouveau firmware. Les broches réservées de la carte ne sont jamais proposées.
* **Mises à jour par radio (OTA) avec retour arrière** depuis le panneau (deux emplacements sur la flash de 16 Mo), et un **lien depuis Studio** vers le panneau de chaque nœud, à partir de l'adresse que le nœud publie.
* **Le panneau en HTTPS :** le nœud fabrique son propre certificat (auto-signé, conservé en flash) et sert le panneau sur le port 443 en plus du 80, ou seulement sur le 443 ; le cookie de session est marqué Secure et l'empreinte du certificat s'affiche pour la comparer à l'avertissement du navigateur.
* **Identités de pistes stables :** les cibles de chaque trame sont associées à celles suivies auparavant ; une personne garde donc le même identifiant, une trame perdue ne fait pas clignoter et les positions sont un peu lissées.
* **Six modèles de capteurs, un par port :** un port porte un LD2450 ou un LD2461 (traqueurs qui alimentent le périmètre, avec le champ propre du modèle dans Studio) ou un capteur de présence (LD2410, LD2412, LD2410S, MR24HPC1) qui devient un appareil du serveur et publie présence et distance. Choisi dans le panneau ; ce qu'est chacun, son protocole et ce qui n'a pas été vérifié sont dans `docs/SENSORS.md`.
* **Décodeur, santé et configuration du LD2450 :** un découpeur qui se resynchronise trouve les trames dans un flux bruité ; chaque trame de 30 octets donne jusqu'à trois cibles qui deviennent des pistes du contrat ; la console et le panneau indiquent par radar s'il émet, se tait ou envoie des données illisibles. Le panneau peut aussi lire la version du module, choisir une ou trois cibles et définir des zones de détection (un protocole non vérifié face à un module).
* **Lumière ambiante et messages conformes au contrat :** le VEML7700 avec plage automatique ; JSON de télémétrie, de santé et d'information qui suit les schémas publiés et refuse d'écrire quoi que ce soit d'invalide, avec des horodatages d'horloge murale (SNTP) et un testament MQTT. La télémétrie est retenue tant qu'aucun radar n'émet, jamais un « tout est calme » vide.
* **Une image pour toutes les cartes, comme un produit réseau :** le firmware est le même et l'adresse MAC distingue les cartes (`armor-` et six chiffres jusqu'au nommage) ; `adopt_node.py` donne à un nœud fraîchement flashé son administrateur, son identité de broker et les réglages communs de la flotte par le réseau, avec un code d'installation calculé depuis sa MAC : 5 nœuds ou 27, c'est le même travail.
* **Outils de banc :** flashage par USB-C, un nœud simulé pour travailler sur le panneau et un convertisseur d'un journal de trames brutes en jeu de test ([mise en service sur banc](docs/BENCH_BRINGUP.md)).
* **Mises à jour par radio signées :** le nœud n'installe depuis GitHub qu'une image dont le SHA-256 correspond et qui porte une signature Ed25519 valide du responsable (la clé publique est dans le firmware, la privée ne quitte jamais le responsable) ; un fichier envoyé à la main par un administrateur dans le panneau reste accepté. Les pages et messages du panneau sont en huit langues.
* **Appairage Bluetooth avec un PIN :** le PIN à six chiffres est dérivé du code de configuration, imprimé sur la console USB et montré à un administrateur dans le panneau ; le téléphone doit le saisir avant de pouvoir écrire les réglages du nœud.
* **Seule la maison peut utiliser le panneau :** le panneau répond par défaut au réseau privé (ou aux réseaux que son propriétaire indique, comme un VPN), refuse une liste qui exclurait celui qui l'enregistre, compte les mauvais mots de passe par personne et par adresse, et fonctionne derrière le proxy du serveur pour être atteint depuis l'extérieur sans publier le nœud.
* **Liaison chiffrée facultative avec le broker (TLS) :** désactivée par défaut, le nœud parle donc MQTT non chiffré comme avant. Un interrupteur et une zone pour le certificat de l'autorité propre à l'installation (PEM, 2 Ko au plus) dans la page Broker lui font se connecter en `mqtts://`, ne faire confiance qu'à cette autorité et vérifier que le certificat du broker a été établi pour l'adresse atteinte ; ce qui n'est pas un seul certificat PEM est refusé. Couvert par des tests sur ordinateur ; la poignée de main n'a pas encore été exécutée sur une carte.
* **Rapport de santé :** environ une fois par minute le nœud publie depuis combien de temps il tourne et pourquoi il a redémarré la dernière fois, sa mémoire libre, sa liaison et son signal Wi-Fi, combien de fois il s'est connecté au broker et la dernière erreur notée (`armor/health/<nœud>`, le contrat `node_health` d'ARMOR-COMMON). Le code qui le construit est partagé par tous les nœuds et testé sur un ordinateur ; il n'a pas tourné sur une carte.
* **Commande depuis le serveur :** Studio peut redémarrer le nœud proprement, le mettre en pause jusqu'à une heure (il reprend seul), mettre son travail en veille (sans fin, conservée aux redémarrages, le nœud reste connecté et continue de répondre), le faire se signaler, demander un instantané de diagnostic et le marquer en maintenance (`armor/control/<nœud>/...`, le contrat `node_control` d'ARMOR-COMMON). Chaque ordre se fait en deux temps avec un jeton à usage unique propre à cette opération, seul le serveur peut les écrire sur le broker, et il n'existe ni réinitialisation d'usine, ni effacement, ni sommeil profond. Tant que le nœud est en pause ou en veille, il ne publie ni cibles ni présence (le battement dit encore qu'il est là). Le code est partagé par tous les nœuds et testé sur un ordinateur ; il n'a pas tourné sur une carte.
* **Un moteur de périmètre sur le nœud (désactivé par défaut) :** six zones de détection et trois zones d'exclusion, chacune un rectangle qu'on peut tourner d'un angle, trois lignes de franchissement qui comptent les passages par sens, trois chemins d'entrée, immunité aux animaux et détection de masquage. Il tourne à côté des capteurs, donc il fonctionne sans accès au broker, garde ses événements tant que le broker est absent et les publie sur `armor/radar/<nœud>/events` ; l'éditeur de zones est dans le panneau du nœud. Rien de tout cela n'a encore tourné avec un capteur sur une carte.
* **Qui est chaque capteur, et son propre Bluetooth fermé :** au démarrage, le nœud lit la version du micrologiciel et l'adresse Bluetooth de chaque capteur, ferme par défaut le Bluetooth propre des capteurs (il ne demande aucun code PIN) et peut confier la ligne série d'un capteur à l'outil PC d'un administrateur pendant quelques minutes (un pont série transparent). `GET /metrics` pour les administrateurs et un export et import tout ou rien des réglages complètent l'ensemble.
* **Diagnostic sans câble :** après un démarrage qui n'était pas propre (plantage, chien de garde, chute d'alimentation, allocation échouée), le rapport de santé en donne la raison pendant dix minutes ; un plantage laisse son vidage mémoire (core dump) à consulter, télécharger ou effacer depuis le panneau ; les réglages enregistrés sont copiés avant chaque installation de micrologiciel et récupérés si une mise à jour les abîme ; et un administrateur peut demander au nœud, via le serveur, un paquet de diagnostic ou son journal avec un jeton à usage unique.
* **Adoption en HTTPS avec empreinte épinglée :** `tools/adopt_node.py` accepte `https://<adresse>` avec `--fingerprint` (le SHA-256 du certificat du nœud, vérifié sur la connexion même qui porte la requête) ou `--show-fingerprint` pour la lire ; il avertit du HTTP en clair et d'un fichier de flotte avec une IP fixe ou un nom d'hôte, et le panneau avertit aussi à l'import d'un tel fichier.
* **Le lecteur de capteurs attend des événements au lieu d'interroger :** la tâche de lecture dort sur les files d'événements des lignes série et vide tout ce qui est arrivé, vide la ligne en cas de débordement et compte débordements et erreurs par ligne ; `system.reader_idle_ms` (100 ; 0 = l'ancienne interrogation de 10 ms) fixe l'attente, et une file défaillante ramène seule à l'interrogation.
* **Scellement facultatif des secrets enregistrés :** désactivé par défaut (`security.seal_secrets`, ou `nodes.nvs_encryption` du serveur). Activé, les mots de passe, jetons, clés, codes PIN et empreintes de mots de passe que le nœud enregistre sont scellés avec ChaCha20-Poly1305 et tout le reste reste lisible ; l'activer ou le désactiver les réécrit sans rien perdre, même si le nœud s'arrête en route. Aucun eFuse n'est brûlé et la flash n'est pas chiffrée : la clé est dans une partition de la même puce, donc cela ne protège **pas** contre quelqu'un qui tient la carte, et un nœud installé avant cette partition garde ses secrets tels quels jusqu'à ce qu'il soit flashé avec la nouvelle table de partitions.""",
      "role": r"""ARMOR-NODE-RADAR est l'œil du périmètre. Chaque nœud lit jusqu'à trois radars ou capteurs de présence et publie pistes, lumière et santé vers [ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER) en MQTT ; [ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) les dessine sur le plan du site et [ARMOR-SERVER-AI](https://github.com/JuanenRac/ARMOR-SERVER-AI) les pèse face aux caméras. Son firmware partage une base avec les autres nœuds (le panneau, la configuration Bluetooth, les mises à jour signées, la connexion et l'horloge viennent de la base firmware d'[ARMOR-COMMON](https://github.com/JuanenRac/ARMOR-COMMON)), si bien que ce qu'on apprend sur un nœud vaut pour tous.

| Nom | Comment | À quoi ça sert |
|---|---|---|
| ARMOR-SERVER | MQTT `armor/node/<id>/telemetry|health|info|command` | Reçoit les messages du radar (aujourd'hui le banc CM5) et commande le nœud |
| ARMOR-STUDIO | lien vers le panneau | Ouvre le panneau du nœud à l'adresse que le nœud publie |
| ARMOR-ANDROID-CONTROL | Bluetooth | Configure le nœud sur le terrain |
| ARMOR-COMMON | contrats, base de firmware | Les messages sont vérifiés avec ses schémas ; le firmware commun en est copié |""",
      "architecture": r"""<p align="center">
  <img src="images/architecture.svg" alt="Architecture de ARMOR-NODE-RADAR : qui l'appelle, ce qu'il contient et de quoi il dépend" width="100%">
</p>""",
      "security": r"""| Menace | Défense |
|---|---|
| Mots de passe en clair ou compilés | PBKDF2-HMAC-SHA256 avec 10 000 tours ; aucun mot de passe dans le firmware (un nœud sans utilisateur passe en configuration) ; au plus 4 utilisateurs (admin ou lecteur) et de 8 à 64 caractères ; au plus 6 sessions, 30 minutes d'inactivité |
| Prendre un nœud tout juste flashé | La configuration exige un code de démarrage : celui du build (`CONFIG_ARMOR_SETUP_CODE`) ou un code aléatoire gardé en flash et affiché sur la console USB ; avec un secret de flotte c'est `HMAC-SHA256(secret, MAC)` ; c'est aussi la clé du Wi-Fi de configuration (WPA2, jamais ponté) |
| Le panneau atteint depuis Internet | Il répond par défaut aux réseaux privés d'une maison (10/8, 172.16/12, 192.168/16, 169.254/16, 127/8 et 100.64/10 où vivent certains VPN) ; le réglage `web.admin_sources` liste d'autres adresses et réseaux IPv4 (8 entrées, 120 caractères) ; tout le reste est refusé sauf l'identité publique `GET /api/v1/session` ; une liste qui exclurait celui qui l'enregistre est rejetée |
| Le panneau en clair en HTTP | HTTPS sur le 443 avec un certificat que le nœud fabrique lui-même (autosigné, en flash, empreinte SHA-256 visible pour comparer) ; le panneau peut être http, https ou les deux ; le cookie de session est toujours HttpOnly et SameSite=Strict (et Secure en TLS) |
| Un faux firmware depuis GitHub | Une image n'est installée qu'avec un SHA-256 concordant et une signature Ed25519 valide faite avec la clé du mainteneur (`no_checksum`, `no_signature`, `bad_signature`, `checksum_mismatch`, `wrong_firmware`, `not_newer`, `version_mismatch` la refusent) ; un envoi manuel par un administrateur n'est pas vérifié : une limite explicite |
| Détournement de la configuration Bluetooth | Un PIN à 6 chiffres dérivé du code de configuration, visible sur la console USB et pour un administrateur ; le téléphone doit le saisir avant d'écrire des réglages ; la fenêtre dure `CONFIG_ARMOR_BLE_SETUP_MINUTES` (10 par défaut, de 1 à 120) |
| Un ordre distant qui fait du mal | Deux étapes avec un jeton à usage unique lié à cette opération ; seul le serveur peut écrire ces topics dans le broker ; une pause dure une heure au plus ; il n'y a ni réinitialisation d'usine, ni effacement, ni sommeil profond par ordre distant |
| Secrets stockés lus par qui a la carte | Optionnel (désactivé par défaut, interrupteur `security.seal_secrets` ou `nodes.nvs_encryption` du serveur) : ChaCha20-Poly1305 pour mots de passe, jetons, clés, PIN et hachages. Il ne chiffre pas la flash et ne grille aucun eFuse : la clé est dans une partition de la même puce, il ne protège donc pas contre qui tient la carte |
| Le lien avec le broker en clair | TLS optionnel (`mqtts://`) avec l'autorité propre du propriétaire (PEM jusqu'à 2 Ko) et vérification du nom ; désactivé par défaut. Le handshake n'a tourné qu'en tests sur hôte, pas sur une carte |
| Le Bluetooth propre d'un capteur | Par défaut le nœud ferme le Bluetooth de chaque capteur LD (sans PIN) ; un pont série transparent vers un ordinateur ne s'ouvre que quelques minutes et par un administrateur |
| Adopter un nœud sur un réseau non fiable | `tools/adopt_node.py https://<adresse> --fingerprint <SHA-256>` vérifie le certificat dans la même connexion ; il prévient pour le HTTP en clair et les fichiers de flotte à adresse fixe |
| Une broche dangereuse | Les broches réservées de la carte ne sont jamais proposées ; une sortie a un état sûr si le broker est perdu ; deux fonctions ne peuvent pas partager une broche (vérifié) |
| Un firmware public avec secret de flotte | `CONFIG_ARMOR_FLEET_SECRET` est vide par défaut : le build public ne porte aucun secret |

Lisez [SECURITY.md](SECURITY.md) pour signaler une vulnérabilité. Il n'y a pas eu de revue indépendante.""",
      "interfaces": r"""| Partie | Ce qu'elle règle |
|---|---|
| MQTT | `armor/node/<id>/{telemetry,health,info,command}`, `armor/health/<id>` (son testament est `{"node_id":"..","online":false}`), `armor/control/<id>/{command,result,maintenance}` et `armor/control/all/command`, `armor/device/<id>/<pin>/{state,set}`, `armor/radar/<id>/events`, `armor/radar/<id>/control/armed` |
| Panneau (HTTP 80, HTTPS 443) | Routes `session`, `login`, `logout`, `setup`, `status`, `config` (+ export, import), `wifi/scan`, `time`, `radars` (+ command), `perimeter` (+ armed, learn, zone), `pins` (+ command), `bridge` (+ open, close, io), `ota` (+ check, install, progress, copy, switch), `account`, `ble-pin`, `log`, `coredump`, `factory-reset`, `reboot` ; `/metrics` pour les administrateurs et le WebSocket `/ws/radar-map` ; `tests/check_routes.py` vérifie que toute route appelée par le panneau existe |
| Textes du panneau | 76 codes d'erreur avec texte en huit langues (832 lignes dans `panel/text.js`), vérifiés par `tests/check_panel_text.py` |
| Matériel | 3 UART pour LD2450, LD2461, LD2410, LD2412, LD2410S et MR24HPC1 (RX 16, 17, 18 ; TX 15, 21, 38) ; W5500 en SPI (MOSI 11, MISO 12, SCLK 13, CS 14, INT 10, RST 9, 20 MHz) ; VEML7700 en I2C (GPIO 1 et 2) ; bouton BOOT |""",
      "configuration": r"""| Variable | Par défaut | Ce qu'elle règle |
|---|---|---|
| `CONFIG_ARMOR_NODE_ID` | `""` | Le nom ; vide donne `armor-` et les trois derniers octets de la MAC |
| `CONFIG_ARMOR_SETUP_CODE`, `CONFIG_ARMOR_FLEET_SECRET` | `""` | Le code de configuration du build (vide : aléatoire) et le secret de flotte (16+ caractères ; jamais dans le dépôt) |
| `CONFIG_ARMOR_RADAR_COUNT` | 3 (0-3) | Combien de radars sont connectés |
| `CONFIG_ARMOR_TRACK_STABILISER` | y | Garder l'identité d'une piste d'une image à l'autre |
| `CONFIG_ARMOR_MQTT_URI`, `_USERNAME`, `_PASSWORD` | `""` | Les premiers réglages du broker (modifiables dans le panneau) |
| `CONFIG_ARMOR_HEARTBEAT_S` | 10 (2-300) | Secondes entre battements de santé |
| `CONFIG_ARMOR_TELEMETRY_PERIOD_MS` | 200 (200-5000) | Au plus 5 messages par seconde |
| `CONFIG_ARMOR_BLE_SETUP_MINUTES` | 10 (1-120) | Combien de temps la configuration Bluetooth reste ouverte |
| `CONFIG_ARMOR_BOARD_S3_ETH` / `_S3_WIFI` | eth | La carte : Waveshare ESP32-S3-ETH ou ESP32-S3-WROOM-1 N16R8 (Wi-Fi seulement) |
| `CONFIG_ARMOR_BOOT_FACTORY_RESET` | y | Maintenez BOOT 8 s dans les 30 premières s pour recommencer |
| `system.login_limit_per_minute` | 30 (0-120) | Mots de passe erronés par minute avant que le panneau verrouille la connexion pour tous (0 = pas de limite globale) ; on le lit et le change depuis Studio (un bouton sur chaque nœud) ou avec `POST /api/v1/admin/nodes/settings`, l'identifiant du panneau étant utilisé une fois et jamais conservé |

Les réglages ajustés en direct sont dans le panneau et gardés en flash (par exemple `system.reader_idle_ms`, `security.seal_secrets`, la limite d'échecs de connexion par minute (30, de 0 à 120) et les zones du moteur de périmètre) ; les valeurs par défaut du firmware sont dans `sdkconfig.defaults` et `sdkconfig.board.*`. La flash de 16 Mo contient `nvs` (64 Ko), `otadata`, `phy_init`, deux emplacements de 3 Mo `ota_0` et `ota_1`, `coredump` (128 Ko) et `nvs_keys` (4 Ko) (`partitions.csv`).""",
      "quickstart": r"""**Prérequis:** un compilateur C++17 pour les tests sur hôte ; le conteneur ESP-IDF 5.5.5 pour construire l'image ; une Waveshare ESP32-S3-ETH ou une ESP32-S3-WROOM-1 N16R8.

```bash
cmake -S tests -B build/host && cmake --build build/host && ctest --test-dir build/host   # host tests, -Werror
node tools/panel_mock.mjs --user admin:adminpass123   # the panel without a board
python tools/make_fleet.py                             # once: the fleet secret and the shared settings
tools/build_node.sh generic                           # ONE image for every Waveshare board (dist/generic-s3-eth.bin), in the ESP-IDF container
tools/build_node.sh generic s3-wifi                   # the same firmware for an ESP32-S3-WROOM-1 N16R8 with no Ethernet
```

```bat
tools\flash.bat generic COM5 monitor                  # each Waveshare board, once, by USB-C (add s3-wifi for the other board)
```

```bash
tools/adopt_node.py 192.168.0.181 --id perimetro-3 --fleet secrets/fleet.json --broker-ssh-host <cm5> --broker-ssh-user <user>
```

Les tests sur ordinateur demandent un compilateur C++17 (Linux, WSL, MSYS2). Voir la [mise en service sur banc](docs/BENCH_BRINGUP.md), le [panneau](docs/NODE_PANEL.md) et la [frontière matérielle](docs/HARDWARE_BOUNDARY.md).""",
      "testing": r"""```bash
cmake -S tests -B build/host && cmake --build build/host && ctest --test-dir build/host
build/host/emit_samples | python tests/check_contract.py
python -I tools/armor_ci_validate.py
```

14 programmes de test sur hôte et 6 contrôles Python tournent sous `ctest` ; 7371 vérifications comptées par les programmes hôte, compilés avec `-Werror`.

| Partie | Ce qu'il couvre |
|---|---|
| `test_core`, `test_sensors`, `test_family`, `test_uart_wake` | Les décodeurs (LD2450, LD2461, quatre capteurs de présence), le délimiteur de trames, le canal de commandes, les familles de capteurs et le réveil de l'UART |
| `test_node`, `test_base`, `test_shared`, `test_board_wifi` | Les réglages et leurs contrôles, la table des broches, utilisateurs et sessions, le plan réseau, la base partagée et la carte Wi-Fi |
| `test_logic`, `test_perimeter`, `test_control`, `test_diag` | La logique des broches, le moteur de périmètre, les ordres de contrôle en deux étapes et le diagnostic |
| `test_mqtt_tls`, `test_release` | Le lien TLS avec le broker (hôte seulement) et les contrôles de version et de signature |
| `check_panel_text`, `check_task_safety`, `check_save_paths`, `check_ble_session`, `check_routes`, `check_bridge_client` | Python : les textes du panneau en huit langues (832 lignes), les tâches, les chemins de sauvegarde, la session Bluetooth sous son verrou, les routes et le client du pont série |

Le panneau web est aussi exercé dans un vrai navigateur contre un nœud de substitution (`tools/panel_mock.mjs`). Les décodeurs LD2461 et de présence ne correspondent qu'aux exemples de leurs manuels.""",
      "build": "`tools/build_node.sh generic` construit UNE image pour chaque carte Waveshare dans le conteneur ESP-IDF 5.5.5, et `tools/flash.bat` l'écrit par USB-C ; le même firmware est construit pour la carte Wi-Fi seul avec `s3-wifi`. Les versions portent l'image, son SHA-256 et sa signature Ed25519, une par carte.",
      "troubleshooting": r"""| Vous voyez | Parce que | Faites |
|---|---|---|
| Vous avez perdu le mot de passe ou le nœud ne rejoint plus le réseau | Un nœud en configuration sans adresse après 90 s ouvre son propre Wi-Fi `ARMOR-SETUP-xxxxxx` (ouvrez `http://192.168.4.1/`) | Pour recommencer, maintenez BOOT 8 secondes dans les 30 premières secondes après la mise sous tension (efface réglages et utilisateurs), ou utilisez *Réinitialisation d'usine* dans le panneau |
| Une mise à jour depuis GitHub est refusée | La version n'a ni somme de contrôle ni signature, elles ne concordent pas (`e_no_checksum`, `e_no_signature`, `e_checksum_mismatch`, `e_bad_signature`), n'a pas d'image pour cette carte (`e_no_asset_for_board`) ou est d'un autre projet (`e_wrong_firmware`) | Le nœud n'a pas changé ; réessayez ou laissez un administrateur envoyer le fichier à la main |
| Les commandes du radar répondent `no_answer`, `refused` ou `disabled` | Le fil TX du radar n'est pas connecté, le module s'est bloqué ou le nœud ferme d'abord son Bluetooth | Vérifiez le câblage (voir la mise en service sur banc), redémarrez le module depuis le panneau |
| Le nœud ne montre pas le capteur 3 ou laisse un radar dormir | Le module a cessé de parler (silence sans trame mauvaise) | Utilisez *redémarrer le module* dans la page des radars, puis fermez le Bluetooth du capteur |""",
      "structure": r"""<p align="center">
  <img src="images/repository-structure.svg" alt="Structure du dépôt de ARMOR-NODE-RADAR" width="100%">
</p>

<details>
<summary>Version texte de l'arborescence</summary>

```text
ARMOR-NODE-RADAR/
├── main/                                le firmware : un composant ESP-IDF
├── panel/                               le panneau web intégré au firmware
├── tests/                               tests sur hôte et contrôles Python
├── docs/                                7 guides du banc et du panneau
├── tools/                               outils de build, flashage, adoption, flotte et contrôle
├── .github/                             workflow CI et modèles d'issues et de pull requests
├── images/                              bannière, icône et les deux images de ce README
├── build.sh build.bat                   build par le flux de projet partagé
├── test.sh test.bat                     lancer les tests par le flux partagé
├── run.sh run.bat                       démarrer par le flux de projet partagé
├── armor.project.json                   manifeste : version, rôle, maturité, commande de build
├── CHANGELOG.md                         ce qui a changé à chaque version
├── SECURITY.md SUPPORT.md LICENSE       politique de sécurité, support et licence
├── CONTRIBUTING.md CODE_OF_CONDUCT.md   comment contribuer et le code de conduite
├── CMakeLists.txt                       le projet ESP-IDF
├── partitions.csv                       la table de la flash
├── sdkconfig.defaults                   les réglages du firmware
├── sdkconfig.board.s3-eth               la carte Ethernet
├── sdkconfig.board.s3-wifi              la carte Wi-Fi
├── secrets/                             exemples de fichiers de flotte et de nœud
├── build-test.sh build-test.bat         lancer les tests par le flux partagé
└── .gitattributes .gitignore            réglages Git
```

</details>""",
      "roadmap": r"""**Limites connues aujourd'hui**

* Les décodeurs LD2461 et de présence ne correspondent qu'aux exemples de leurs manuels, sans module derrière ; le canal de commandes n'a été vérifié qu'avec le LD2450.
* La vérification de signature des mises à jour et l'appariement Bluetooth par PIN sont prouvés sur ordinateur avec de vraies signatures mais pas encore sur la carte ; le handshake TLS avec le broker n'a pas tourné sur une carte.
* Le rapport de santé et le contrôle depuis le serveur n'ont pas tourné sur la carte ; le moteur de périmètre n'a jamais tourné avec un capteur ; le certificat HTTPS propre du panneau n'est pas essayé dans tous les navigateurs ; la carte Wi-Fi n'existe pas physiquement (seule la carte Ethernet existe).

**Ensuite**

* Faire tourner le moteur de périmètre, le rapport de santé et les ordres de contrôle avec de vrais capteurs et le banc CM5 ; essayer le lien TLS avec le broker et la mise à jour signée sur la carte.""",
    },
  },
  "it": {
    "tagline": "Firmware del nodo di campo (Waveshare ESP32-S3-ETH, tre radar o sensori di presenza, Ethernet e Wi-Fi) con un proprio pannello web e il nucleo testato su computer",
    "honest": "Il nodo radar è l'unico nodo che esiste come hardware: il suo firmware gira su una vera scheda Waveshare ESP32-S3-ETH con un radar e riferisce al banco di prova CM5, e il suo pannello web e gli aggiornamenti via etere vi sono in uso. Il nucleo indipendente dall'hardware (4,633 controlli in 14 programmi di test: i decodificatori dell'LD2450, dell'LD2461 e di quattro sensori di presenza, il canale di comando dell'LD2450, le impostazioni e i loro controlli, la tabella dei pin, utenti e sessioni, il piano di rete, il serializzatore di messaggi la cui uscita è accettata da ARMOR-COMMON, e i controlli di versione e firma) è provato su un computer, il **pannello web** è stato esercitato in un vero browser contro un nodo sostitutivo e l'**immagine del firmware si compila** nel contenitore ESP-IDF 5.5.5. Ciò che **non** è ancora provato: i decodificatori dell'LD2461 e dei sensori di presenza corrispondono solo agli esempi svolti dei loro manuali, senza un modulo dietro; il controllo della firma degli aggiornamenti e l'abbinamento Bluetooth con PIN sono provati su computer con firme vere ma non ancora sulla scheda; il canale di comando del radar non è verificato con un modulo; e il certificato HTTPS del pannello (fatto dal nodo stesso) non è provato in tutti i browser.",
    "glance": [
      [
        "Ruolo",
        "Nodo di campo radar per ESP32-S3 (famiglia: Field Nodes, padre: ARMOR-COMMON)",
      ],
      [
        "Tecnologia",
        "C++17, ESP-IDF 5.5.5, ESP32-S3",
      ],
      [
        "Test",
        "7371 verifiche in 14 programmi host e 6 verifiche Python (`ctest`)",
      ],
      [
        "Schede",
        "Waveshare ESP32-S3-ETH (Ethernet) e ESP32-S3-WROOM-1 N16R8 (solo Wi-Fi)",
      ],
      [
        "Sensori",
        "Fino a 3 radar (LD2450, LD2461) o sensori di presenza per nodo, sensore di luce VEML7700",
      ],
      [
        "Gira su",
        "Waveshare ESP32-S3-ETH o ESP32-S3-WROOM-1 N16R8; test su host su qualsiasi computer",
      ],
      [
        "Su hardware reale",
        "Gira su una vera scheda Waveshare ESP32-S3-ETH con un radar, riferendo al banco di prova CM5",
      ],
      [
        "Licenza",
        "GPL-3.0-or-later",
      ],
    ],
    "status": {
      "software": "Il firmware compila nel contenitore ESP-IDF 5.5.5 e gira su una scheda ESP32-S3-ETH reale.",
      "tests": "Superano 7.371 controlli in 14 programmi host (`ctest`): i decodificatori, le impostazioni, la tabella dei pin, gli utenti, il piano di rete, il serializzatore dei messaggi e i controlli di versione.",
      "protocols": "L'LD2450 funziona con un radar reale; i decodificatori dell'LD2461 e dei quattro sensori di presenza corrispondono solo agli esempi dei loro manuali e il canale di comando del radar non è stato verificato con un modulo.",
      "ui": "Il pannello web è in uso sulla scheda e provato in un browser reale contro un nodo simulato; il suo certificato HTTPS, creato dal nodo stesso, non è stato provato in tutti i browser.",
      "hardware": "È l'unico nodo che esiste come hardware: una scheda Waveshare ESP32-S3-ETH reale con un radar riferisce al banco di prova CM5; nessun altro modulo sensore è collegato.",
      "security": "L'abbinamento con PIN Bluetooth e il controllo della firma degli aggiornamenti sono provati su un computer con firme reali ma non ancora sulla scheda; non c'è stata una revisione indipendente.",
      "updates": "Gli aggiornamenti via etere sono in uso sulla scheda; il controllo degli aggiornamenti firmati non vi è ancora stato eseguito.",
      "integration": "I messaggi della scheda arrivano al server del banco di prova CM5 e gli stessi messaggi sono accettati dagli schemi condivisi e dai vettori di conformità di ARMOR-COMMON. Visto solo sul banco di prova, non in un'installazione.",
      "docs": "Otto lingue e il registro delle modifiche sono aggiornati.",
    },
    "docs": [
      "[Pannello del nodo](docs/NODE_PANEL.md): primo avvio, utenti, rete, le pagine del pannello",
      "[Codice di configurazione](docs/SETUP_CODE.md) e [provisioning Bluetooth](docs/BLE_PROVISIONING.md)",
      "[Sensori](docs/SENSORS.md): i sei modelli e i loro decodificatori",
      "[Messa in servizio al banco](docs/BENCH_BRINGUP.md), [prove al banco](docs/BENCH_TESTS.md) e [limite dell'hardware](docs/HARDWARE_BOUNDARY.md)",
    ],
    "contributing_first": "Prima di una pull request esegui `ctest --test-dir build/host` and `python -I tools/armor_ci_validate.py`: deve passare. Vedi [CONTRIBUTING.md](CONTRIBUTING.md) e il [codice di condotta](CODE_OF_CONDUCT.md).",
    "languages_extra": "",
    "body": {
      "overview": r"""* **Due schede, un solo firmware:** la Waveshare ESP32-S3-ETH (Ethernet, predefinita) e una ESP32-S3-WROOM-1 N16R8 senza Ethernet (solo Wi-Fi: la configurazione chiede la rete Wi-Fi a cui unirsi e il nodo tiene sempre la propria rete). L'immagine si sceglie in compilazione (`tools/build_node.sh generic s3-eth` o `generic s3-wifi`); la tabella dei pin e l'accesso seguono la scheda, il pannello nasconde ciò che la scheda non ha e un'immagine vale solo per la sua scheda. Entrambe compilano e sono testate sul computer; nessuna ha girato su una scheda.
* **Un nodo copre fino a 270 gradi:** ogni Waveshare ESP32-S3-ETH legge fino a tre radar LD2450 sulle sue tre UART, montati a 75 gradi l'uno dall'altro, via Ethernet cablata (W5500) con DHCP o indirizzo fisso, alimentato con PoE o USB. *Add a 270° node* di Studio crea i tre radar già associati al nodo.
* **Un pannello web su ogni nodo,** con l'aspetto di Studio e in otto lingue, incorporato nel firmware: panoramica, rete, Wi-Fi, broker, radar, pin, utenti, aggiornamento del firmware e registro. Un nodo senza utenti apre il Wi-Fi `ARMOR-SETUP-xxxxxx` e crea il suo primo amministratore con un codice di configurazione; le password sono PBKDF2 con sale, le sessioni sono token casuali e ogni impostazione è nella flash del nodo, quindi un'unica immagine serve tutti i nodi e nessuna password è compilata ([il pannello](docs/NODE_PANEL.md)).
* **Un solo Wi-Fi da più nodi:** ogni nodo può offrire un access point collegato alla sua porta Ethernet; con lo stesso nome e password e il canale in automatico (1, 6 o 11 secondo la MAC), telefoni e sensori Wi-Fi vedono una sola rete con un solo server DHCP. Non è una rete mesh radio: ogni nodo mantiene il suo cavo. Un nodo può invece unirsi al Wi-Fi di un router (con ricerca delle reti), e uno senza cavo può essere configurato via **Bluetooth** dall'app Android.
* **Pin per il server:** qualsiasi pin libero diventa un ingresso, un'uscita (con uno stato sicuro se il broker si perde), PWM o una lettura analogica, e appare come dispositivo del server: un relè o un contatto non richiede un nuovo firmware. I pin riservati della scheda non vengono mai offerti.
* **Aggiornamenti via radio (OTA) con ripristino** dal pannello (due slot sulla flash da 16 MB) e un **collegamento da Studio** al pannello di ogni nodo, dall'indirizzo che il nodo pubblica.
* **Il pannello in HTTPS:** il nodo crea il proprio certificato (autofirmato, conservato in flash) e serve il pannello sulla porta 443 oltre che sulla 80, o solo sulla 443; il cookie di sessione è marcato Secure e l'impronta del certificato viene mostrata per confrontarla con l'avviso del browser.
* **Identità di traccia stabili:** i bersagli di ogni frame sono associati a quelli seguiti prima, così una persona mantiene lo stesso id, un frame perso non fa sfarfallare e le posizioni sono un po' levigate.
* **Sei modelli di sensore, uno per porta:** una porta porta un LD2450 o un LD2461 (tracker che alimentano il perimetro, con il campo proprio del modello in Studio) o un sensore di presenza (LD2410, LD2412, LD2410S, MR24HPC1) che diventa un dispositivo del server e pubblica presenza e distanza. Si sceglie nel pannello; cos'è ciascuno, il suo protocollo e cosa non è stato verificato sono in `docs/SENSORS.md`.
* **Decodificatore, salute e configurazione dell'LD2450:** un framer che si risincronizza trova i frame in un flusso rumoroso; ogni frame da 30 byte dà fino a tre bersagli che diventano tracce del contratto; la console e il pannello dicono per radar se trasmette, tace o manda dati illeggibili. Il pannello può anche leggere la versione del modulo, scegliere uno o tre bersagli e impostare zone di rilevamento (un protocollo non verificato su un modulo).
* **Luce ambiente e messaggi esatti rispetto al contratto:** il VEML7700 con range automatico; JSON di telemetria, salute e informazioni che segue gli schemi pubblicati e rifiuta di scrivere qualsiasi cosa non valida, con timestamp di orologio reale (SNTP) e un last will MQTT. La telemetria è trattenuta finché nessun radar trasmette, mai un «tutto tranquillo» vuoto.
* **Un'immagine per tutte le schede, come un prodotto di rete:** il firmware è lo stesso e la MAC distingue le schede (`armor-` e sei cifre finché non ricevono un nome); `adopt_node.py` dà a un nodo appena flashato il suo amministratore, la sua identità di broker e le impostazioni comuni della flotta via rete, con un codice di configurazione calcolato dalla sua MAC: 5 nodi o 27 sono lo stesso lavoro.
* **Strumenti da banco:** flash via USB-C, un nodo finto per lavorare sul pannello e un convertitore da un registro di frame grezzi a un fixture di test ([messa in servizio da banco](docs/BENCH_BRINGUP.md)).
* **Aggiornamenti via etere firmati:** il nodo installa da GitHub solo un'immagine il cui SHA-256 coincide e che porta una firma Ed25519 valida del responsabile (la chiave pubblica è nel firmware, quella privata non lascia mai il responsabile); un file caricato a mano da un amministratore nel pannello resta accettato. Le pagine e i messaggi del pannello sono in otto lingue.
* **Abbinamento Bluetooth con PIN:** il PIN a sei cifre deriva dal codice di configurazione, è stampato sulla console USB e mostrato a un amministratore nel pannello; il telefono deve inserirlo prima di poter scrivere le impostazioni del nodo.
* **Solo la casa può usare il pannello:** il pannello risponde per impostazione predefinita alla rete privata (o alle reti indicate dal proprietario, come una VPN), rifiuta un elenco che escluderebbe chi lo salva, conta le password errate per persona e per indirizzo e funziona dietro il proxy del server per essere raggiunto da fuori casa senza pubblicare il nodo.
* **Collegamento cifrato facoltativo con il broker (TLS):** disattivato per impostazione predefinita, quindi il nodo parla MQTT non cifrato come prima. Un interruttore e una casella per il certificato dell'autorità propria dell'installazione (PEM, al massimo 2 KB) nella pagina Broker lo fanno collegare con `mqtts://`, fidarsi solo di quell'autorità e verificare che il certificato del broker sia stato fatto per l'indirizzo raggiunto; ciò che non è un solo certificato PEM viene rifiutato. Coperto da test sul computer; l'handshake non è ancora stato eseguito su una scheda.
* **Rapporto di salute:** circa una volta al minuto il nodo pubblica da quanto è acceso e perché si è riavviato l'ultima volta, la memoria libera, il collegamento e il segnale Wi-Fi, quante volte si è connesso al broker e l'ultimo errore registrato (`armor/health/<nodo>`, il contratto `node_health` di ARMOR-COMMON). Il codice che lo costruisce è condiviso da tutti i nodi e testato su un computer; non è mai girato su una scheda.
* **Controllo dal server:** Studio può riavviare il nodo in modo pulito, metterlo in pausa fino a un'ora (riprende da solo), mettere il suo lavoro in standby (senza fine, conservato ai riavvii, il nodo resta connesso e continua a rispondere), farlo mostrare, chiedere un'istantanea diagnostica e segnarlo in manutenzione (`armor/control/<nodo>/...`, il contratto `node_control` di ARMOR-COMMON). Ogni ordine è in due passi con un token monouso legato a quell'operazione, solo il server può scriverli sul broker e non esistono ripristino di fabbrica, cancellazione né sonno profondo. Finché il nodo è in pausa o in standby non pubblica bersagli né presenza (il battito continua a dire che c'è). Il codice è condiviso da tutti i nodi e provato su un computer; non ha ancora girato su una scheda.
* **Un motore di perimetro sul nodo (spento per impostazione predefinita):** sei zone di rilevamento e tre di esclusione, ciascuna un rettangolo ruotabile di un angolo, tre linee di attraversamento che contano i passaggi per direzione, tre percorsi d'ingresso, immunità agli animali domestici e rilevamento del mascheramento. Funziona accanto ai sensori, quindi continua senza accesso al broker, conserva i suoi eventi finché il broker è assente e li pubblica su `armor/radar/<nodo>/events`; l'editor delle zone è nel pannello del nodo. Nulla di tutto ciò è ancora stato provato con un sensore su una scheda.
* **Chi è ciascun sensore, e il suo Bluetooth proprio chiuso:** all'avvio il nodo legge la versione del firmware e l'indirizzo Bluetooth di ogni sensore, chiude per impostazione predefinita il Bluetooth dei sensori (non richiede PIN) e può affidare la linea seriale di un sensore allo strumento PC di un amministratore per qualche minuto (un ponte seriale trasparente). `GET /metrics` per gli amministratori e un'esportazione e importazione tutto o niente delle impostazioni completano il quadro.
* **Diagnostica senza cavo:** dopo un avvio non pulito (un blocco, un watchdog, un calo di alimentazione, un'allocazione fallita) il rapporto di salute ne indica la causa per dieci minuti; un arresto anomalo lascia il suo core dump da vedere, scaricare o cancellare dal pannello; le impostazioni salvate vengono copiate prima di ogni installazione del firmware e recuperate se un aggiornamento le danneggia; e un amministratore può chiedere al nodo, tramite il server, un pacchetto di diagnostica o il suo registro con un token monouso.
* **Adozione via HTTPS con impronta fissata:** `tools/adopt_node.py` accetta `https://<indirizzo>` con `--fingerprint` (lo SHA-256 del certificato del nodo, verificato sulla stessa connessione che porta la richiesta) o `--show-fingerprint` per leggerla; avverte del HTTP in chiaro e di un file di flotta con IP fisso o nome host, e anche il pannello avverte all'importazione di un file così.
* **Il lettore dei sensori attende eventi invece di interrogare:** il task di lettura dorme sulle code di eventi delle linee seriali e svuota tutto ciò che è arrivato, svuota la linea in caso di overflow e conta overflow ed errori per linea; `system.reader_idle_ms` (100; 0 = il polling da 10 ms di prima) fissa l'attesa, e una coda che si guasta riporta da sola al polling.
* **Sigillatura facoltativa dei segreti salvati:** disattivata per impostazione predefinita (`security.seal_secrets`, o `nodes.nvs_encryption` del server). Attiva, le password, i token, le chiavi, i PIN e gli hash delle password che il nodo salva restano sigillati con ChaCha20-Poly1305 e tutto il resto resta leggibile; attivarla o disattivarla li riscrive senza perdere nulla, anche se il nodo si ferma a metà. Nessun eFuse viene bruciato e la flash non è cifrata: la chiave si trova in una partizione dello stesso chip, quindi **non** protegge da chi ha la scheda, e un nodo installato prima di quella partizione mantiene i suoi segreti com'erano finché non viene flashato con la nuova tabella delle partizioni.""",
      "role": r"""ARMOR-NODE-RADAR sono gli occhi del perimetro. Ogni nodo legge fino a tre radar o sensori di presenza e pubblica tracce, luce e salute verso [ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER) via MQTT; [ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) le disegna sulla planimetria del sito e [ARMOR-SERVER-AI](https://github.com/JuanenRac/ARMOR-SERVER-AI) le pesa rispetto alle telecamere. Il suo firmware condivide una base con gli altri nodi (il pannello, la configurazione Bluetooth, gli aggiornamenti firmati, l'accesso e l'orologio vengono dalla base firmware di [ARMOR-COMMON](https://github.com/JuanenRac/ARMOR-COMMON)), così ciò che impari su un nodo vale per tutti.

| Nome | Come | A cosa serve |
|---|---|---|
| ARMOR-SERVER | MQTT `armor/node/<id>/telemetry|health|info|command` | Riceve i messaggi del radar (oggi il banco CM5) e comanda il nodo |
| ARMOR-STUDIO | collegamento al pannello | Apre il pannello del nodo dall'indirizzo che il nodo pubblica |
| ARMOR-ANDROID-CONTROL | Bluetooth | Configura il nodo sul campo |
| ARMOR-COMMON | contratti, base firmware | I messaggi sono verificati con i suoi schemi; il firmware comune è copiato da lì |""",
      "architecture": r"""<p align="center">
  <img src="images/architecture.svg" alt="Architettura di ARMOR-NODE-RADAR: chi lo chiama, cosa contiene e da cosa dipende" width="100%">
</p>""",
      "security": r"""| Minaccia | Difesa |
|---|---|
| Password in chiaro o compilate | PBKDF2-HMAC-SHA256 con 10 000 round; nessuna password nel firmware (un nodo senza utenti entra in configurazione); al massimo 4 utenti (admin o visualizzatore) e da 8 a 64 caratteri; al massimo 6 sessioni, 30 minuti di inattività |
| Prendere un nodo appena programmato | La configurazione richiede un codice di avvio: quello della build (`CONFIG_ARMOR_SETUP_CODE`) o uno casuale tenuto in flash e mostrato sulla console USB; con un segreto di flotta è `HMAC-SHA256(segreto, MAC)`; è anche la chiave del Wi-Fi di configurazione (WPA2, mai in bridge) |
| Il pannello raggiunto da Internet | Risponde di default alle reti private di una casa (10/8, 172.16/12, 192.168/16, 169.254/16, 127/8 e 100.64/10 dove vivono alcune VPN); l'impostazione `web.admin_sources` elenca altri indirizzi e reti IPv4 (8 voci, 120 caratteri); tutto il resto è rifiutato tranne l'identità pubblica `GET /api/v1/session`; una lista che escluderebbe chi la salva è rifiutata |
| Il pannello in chiaro su HTTP | HTTPS sulla 443 con un certificato che il nodo crea da sé (autofirmato, in flash, impronta SHA-256 visibile per confrontarla); il pannello può essere http, https o entrambi; il cookie di sessione è sempre HttpOnly e SameSite=Strict (e Secure su TLS) |
| Un firmware falso da GitHub | Un'immagine si installa solo con uno SHA-256 coincidente e una firma Ed25519 valida fatta con la chiave del manutentore (`no_checksum`, `no_signature`, `bad_signature`, `checksum_mismatch`, `wrong_firmware`, `not_newer`, `version_mismatch` la rifiutano); un caricamento manuale da un amministratore non è verificato: un limite esplicito |
| Dirottamento della configurazione Bluetooth | Un PIN a 6 cifre derivato dal codice di configurazione, visibile sulla console USB e a un amministratore; il telefono deve digitarlo prima di scrivere le impostazioni; la finestra dura `CONFIG_ARMOR_BLE_SETUP_MINUTES` (10 di default, da 1 a 120) |
| Un ordine remoto che fa danni | Due passi con un token monouso legato a quell'operazione; solo il server può scrivere quei topic nel broker; una pausa dura al massimo un'ora; non ci sono ripristino di fabbrica, cancellazione né sonno profondo da ordine remoto |
| Segreti memorizzati letti da chi ha la scheda | Opzionale (spento di default, interruttore `security.seal_secrets` o `nodes.nvs_encryption` del server): ChaCha20-Poly1305 per password, token, chiavi, PIN e hash. Non cifra la flash né brucia un eFuse: la chiave è in una partizione dello stesso chip, quindi non protegge da chi ha la scheda |
| Il collegamento al broker in chiaro | TLS opzionale (`mqtts://`) con l'autorità propria del proprietario (PEM fino a 2 KB) e verifica del nome; spento di default. L'handshake è girato solo nei test su host, non su una scheda |
| Il Bluetooth proprio di un sensore | Di default il nodo chiude il Bluetooth di ogni sensore LD (senza PIN); un ponte seriale trasparente verso un computer si apre solo per pochi minuti e da un amministratore |
| Adottare un nodo su una rete non fidata | `tools/adopt_node.py https://<indirizzo> --fingerprint <SHA-256>` verifica il certificato nella stessa connessione; avvisa per l'HTTP in chiaro e per i file di flotta con indirizzo fisso |
| Un pin pericoloso | I pin riservati della scheda non vengono mai offerti; un'uscita ha uno stato sicuro se si perde il broker; due funzioni non possono condividere un pin (verificato) |
| Un firmware pubblico con segreto di flotta | `CONFIG_ARMOR_FLEET_SECRET` è vuoto di default: la build pubblica non porta alcun segreto |

Leggi [SECURITY.md](SECURITY.md) per segnalare una vulnerabilità. Non c'è stata una revisione indipendente.""",
      "interfaces": r"""| Parte | Cosa imposta |
|---|---|
| MQTT | `armor/node/<id>/{telemetry,health,info,command}`, `armor/health/<id>` (il suo last will è `{"node_id":"..","online":false}`), `armor/control/<id>/{command,result,maintenance}` e `armor/control/all/command`, `armor/device/<id>/<pin>/{state,set}`, `armor/radar/<id>/events`, `armor/radar/<id>/control/armed` |
| Pannello (HTTP 80, HTTPS 443) | Percorsi `session`, `login`, `logout`, `setup`, `status`, `config` (+ export, import), `wifi/scan`, `time`, `radars` (+ command), `perimeter` (+ armed, learn, zone), `pins` (+ command), `bridge` (+ open, close, io), `ota` (+ check, install, progress, copy, switch), `account`, `ble-pin`, `log`, `coredump`, `factory-reset`, `reboot`; `/metrics` per gli amministratori e il WebSocket `/ws/radar-map`; `tests/check_routes.py` verifica che ogni percorso chiamato dal pannello esista |
| Testi del pannello | 76 codici di errore con testo in otto lingue (832 righe in `panel/text.js`), verificati da `tests/check_panel_text.py` |
| Hardware | 3 UART per LD2450, LD2461, LD2410, LD2412, LD2410S e MR24HPC1 (RX 16, 17, 18; TX 15, 21, 38); W5500 su SPI (MOSI 11, MISO 12, SCLK 13, CS 14, INT 10, RST 9, 20 MHz); VEML7700 su I2C (GPIO 1 e 2); pulsante BOOT |""",
      "configuration": r"""| Variabile | Predefinito | Cosa imposta |
|---|---|---|
| `CONFIG_ARMOR_NODE_ID` | `""` | Il nome; vuoto dà `armor-` e gli ultimi tre byte del MAC |
| `CONFIG_ARMOR_SETUP_CODE`, `CONFIG_ARMOR_FLEET_SECRET` | `""` | Il codice di configurazione della build (vuoto: casuale) e il segreto di flotta (16+ caratteri; mai nel repository) |
| `CONFIG_ARMOR_RADAR_COUNT` | 3 (0-3) | Quanti radar sono collegati |
| `CONFIG_ARMOR_TRACK_STABILISER` | y | Mantenere l'identità di una traccia da un fotogramma all'altro |
| `CONFIG_ARMOR_MQTT_URI`, `_USERNAME`, `_PASSWORD` | `""` | Le prime impostazioni del broker (modificabili nel pannello) |
| `CONFIG_ARMOR_HEARTBEAT_S` | 10 (2-300) | Secondi tra i battiti di salute |
| `CONFIG_ARMOR_TELEMETRY_PERIOD_MS` | 200 (200-5000) | Al massimo 5 messaggi al secondo |
| `CONFIG_ARMOR_BLE_SETUP_MINUTES` | 10 (1-120) | Quanto resta aperta la configurazione Bluetooth |
| `CONFIG_ARMOR_BOARD_S3_ETH` / `_S3_WIFI` | eth | La scheda: Waveshare ESP32-S3-ETH o ESP32-S3-WROOM-1 N16R8 (solo Wi-Fi) |
| `CONFIG_ARMOR_BOOT_FACTORY_RESET` | y | Tieni BOOT 8 s nei primi 30 s per ricominciare |
| `system.login_limit_per_minute` | 30 (0-120) | Password errate al minuto prima che il pannello blocchi l'accesso a tutti (0 = nessun limite globale); si legge e si cambia da Studio (un pulsante su ogni nodo) o con `POST /api/v1/admin/nodes/settings`, dove l'accesso al pannello è usato una volta e mai conservato |

Le impostazioni regolate dal vivo sono nel pannello e salvate in flash (ad esempio `system.reader_idle_ms`, `security.seal_secrets`, il limite di accessi falliti al minuto (30, da 0 a 120) e le zone del motore di perimetro); i valori predefiniti del firmware sono in `sdkconfig.defaults` e `sdkconfig.board.*`. La flash da 16 MB contiene `nvs` (64 KB), `otadata`, `phy_init`, due slot da 3 MB `ota_0` e `ota_1`, `coredump` (128 KB) e `nvs_keys` (4 KB) (`partitions.csv`).""",
      "quickstart": r"""**Requisiti:** un compilatore C++17 per i test su host; il container ESP-IDF 5.5.5 per costruire l'immagine; una Waveshare ESP32-S3-ETH o una ESP32-S3-WROOM-1 N16R8.

```bash
cmake -S tests -B build/host && cmake --build build/host && ctest --test-dir build/host   # host tests, -Werror
node tools/panel_mock.mjs --user admin:adminpass123   # the panel without a board
python tools/make_fleet.py                             # once: the fleet secret and the shared settings
tools/build_node.sh generic                           # ONE image for every Waveshare board (dist/generic-s3-eth.bin), in the ESP-IDF container
tools/build_node.sh generic s3-wifi                   # the same firmware for an ESP32-S3-WROOM-1 N16R8 with no Ethernet
```

```bat
tools\flash.bat generic COM5 monitor                  # each Waveshare board, once, by USB-C (add s3-wifi for the other board)
```

```bash
tools/adopt_node.py 192.168.0.181 --id perimetro-3 --fleet secrets/fleet.json --broker-ssh-host <cm5> --broker-ssh-user <user>
```

I test su computer richiedono un compilatore C++17 (Linux, WSL, MSYS2). Vedi la [messa in servizio da banco](docs/BENCH_BRINGUP.md), il [pannello](docs/NODE_PANEL.md) e il [confine hardware](docs/HARDWARE_BOUNDARY.md).""",
      "testing": r"""```bash
cmake -S tests -B build/host && cmake --build build/host && ctest --test-dir build/host
build/host/emit_samples | python tests/check_contract.py
python -I tools/armor_ci_validate.py
```

14 programmi di test su host e 6 verifiche Python girano con `ctest`; 7371 verifiche contate dai programmi host, compilati con `-Werror`.

| Parte | Cosa copre |
|---|---|
| `test_core`, `test_sensors`, `test_family`, `test_uart_wake` | I decodificatori (LD2450, LD2461, quattro sensori di presenza), il delimitatore di frame, il canale dei comandi, le famiglie di sensori e il risveglio della UART |
| `test_node`, `test_base`, `test_shared`, `test_board_wifi` | Le impostazioni e le loro verifiche, la tabella dei pin, utenti e sessioni, il piano di rete, la base condivisa e la scheda Wi-Fi |
| `test_logic`, `test_perimeter`, `test_control`, `test_diag` | La logica dei pin, il motore di perimetro, gli ordini di controllo in due passi e la diagnostica |
| `test_mqtt_tls`, `test_release` | Il collegamento TLS al broker (solo host) e le verifiche di versione e firma |
| `check_panel_text`, `check_task_safety`, `check_save_paths`, `check_ble_session`, `check_routes`, `check_bridge_client` | Python: i testi del pannello in otto lingue (832 righe), i task, i percorsi di salvataggio, la sessione Bluetooth sotto il suo lock, i percorsi e il client del ponte seriale |

Il pannello web è anche provato in un browser reale contro un nodo sostitutivo (`tools/panel_mock.mjs`). I decodificatori LD2461 e di presenza coincidono solo con gli esempi dei loro manuali.""",
      "build": "`tools/build_node.sh generic` costruisce UNA immagine per ogni scheda Waveshare nel container ESP-IDF 5.5.5, e `tools/flash.bat` la scrive via USB-C; lo stesso firmware è costruito per la scheda solo Wi-Fi con `s3-wifi`. Le versioni portano l'immagine, il suo SHA-256 e la sua firma Ed25519, una per scheda.",
      "troubleshooting": r"""| Vedi | Perché | Fai |
|---|---|---|
| Hai perso la password o il nodo non entra più in rete | Un nodo in configurazione senza indirizzo dopo 90 s apre un proprio Wi-Fi `ARMOR-SETUP-xxxxxx` (apri `http://192.168.4.1/`) | Per ricominciare tieni premuto BOOT per 8 secondi nei primi 30 secondi dopo l'accensione (cancella impostazioni e utenti), o usa *Ripristino di fabbrica* nel pannello |
| Un aggiornamento da GitHub è rifiutato | La versione non ha checksum o firma, non corrispondono (`e_no_checksum`, `e_no_signature`, `e_checksum_mismatch`, `e_bad_signature`), non ha un'immagine per questa scheda (`e_no_asset_for_board`) o è di un altro progetto (`e_wrong_firmware`) | Il nodo non è cambiato; riprova o lascia che un amministratore carichi il file a mano |
| I comandi al radar rispondono `no_answer`, `refused` o `disabled` | Il filo TX del radar non è collegato, il modulo si è bloccato o il nodo chiude prima il suo Bluetooth | Controlla il cablaggio (vedi la messa in servizio al banco), riavvia il modulo dal pannello |
| Il nodo non mostra il sensore 3 o lascia dormire un radar | Il modulo ha smesso di parlare (silenzio senza frame errati) | Usa *riavvia modulo* nella pagina dei radar, poi chiudi il Bluetooth del sensore |""",
      "structure": r"""<p align="center">
  <img src="images/repository-structure.svg" alt="Struttura del repository di ARMOR-NODE-RADAR" width="100%">
</p>

<details>
<summary>Versione testuale dell'albero</summary>

```text
ARMOR-NODE-RADAR/
├── main/                                il firmware: un componente ESP-IDF
├── panel/                               il pannello web incorporato nel firmware
├── tests/                               test su host e verifiche Python
├── docs/                                7 guide per il banco e il pannello
├── tools/                               strumenti di build, flash, adozione, flotta e verifica
├── .github/                             workflow CI e modelli per issue e pull request
├── images/                              banner, icona e le due immagini di questo README
├── build.sh build.bat                   build tramite il flusso di progetto condiviso
├── test.sh test.bat                     eseguire i test tramite il flusso condiviso
├── run.sh run.bat                       avvio tramite il flusso di progetto condiviso
├── armor.project.json                   manifesto: versione, ruolo, maturità, comando di build
├── CHANGELOG.md                         cosa è cambiato in ogni versione
├── SECURITY.md SUPPORT.md LICENSE       politica di sicurezza, supporto e licenza
├── CONTRIBUTING.md CODE_OF_CONDUCT.md   come contribuire e il codice di condotta
├── CMakeLists.txt                       il progetto ESP-IDF
├── partitions.csv                       la tabella della flash
├── sdkconfig.defaults                   le impostazioni del firmware
├── sdkconfig.board.s3-eth               la scheda Ethernet
├── sdkconfig.board.s3-wifi              la scheda Wi-Fi
├── secrets/                             esempi di file di flotta e nodo
├── build-test.sh build-test.bat         eseguire i test tramite il flusso condiviso
└── .gitattributes .gitignore            impostazioni di Git
```

</details>""",
      "roadmap": r"""**Limiti noti oggi**

* I decodificatori LD2461 e di presenza coincidono solo con gli esempi dei loro manuali, senza modulo dietro; il canale dei comandi è stato verificato solo con l'LD2450.
* La verifica della firma degli aggiornamenti e l'abbinamento Bluetooth con PIN sono dimostrati su un computer con firme reali ma non ancora sulla scheda; l'handshake TLS con il broker non è girato su una scheda.
* Il rapporto di salute e il controllo dal server non sono girati sulla scheda; il motore di perimetro non è mai girato con un sensore; il certificato HTTPS proprio del pannello non è provato in tutti i browser; la scheda Wi-Fi non esiste fisicamente (esiste solo quella Ethernet).

**Prossimi passi**

* Far girare il motore di perimetro, il rapporto di salute e gli ordini di controllo con sensori reali e il banco CM5; provare il collegamento TLS al broker e l'aggiornamento firmato sulla scheda.""",
    },
  },
  "ja": {
    "tagline": "フィールドノードのファームウェア（Waveshare ESP32-S3-ETH、レーダーまたは人感センサー 3 基、イーサネットと Wi-Fi）。独自の Web パネルと、コンピューターでテスト済みのコア付き",
    "honest": "レーダーノードはハードウェアとして実在する唯一のノードです。そのファームウェアはレーダー付きの実際の Waveshare ESP32-S3-ETH 基板で動作して CM5 テストベンチに報告し、Web パネルと無線アップデートもその基板で使われています。ハードウェアに依存しないコア（5 つのテストプログラムで 950 項目：LD2450・LD2461 と 4 種の人感センサーのデコーダー、LD2450 のコマンドチャネル、設定とその検査、ピン表、ユーザーとセッション、ネットワーク計画、ARMOR-COMMON が出力を受け付けるメッセージシリアライザー、バージョンと署名の検査）はコンピューター上でテストされ、**Web パネル**は代替ノードに対して実際のブラウザーで動かし、**ファームウェアイメージ**は ESP-IDF 5.5.5 コンテナーでビルドできます。**まだ**証明されていないもの：LD2461 と人感センサーのデコーダーはマニュアルの計算例にしか一致せず、実モジュールがありません。アップデートの署名検査と PIN 付き Bluetooth ペアリングは実際の署名でコンピューター上で証明済みですが、基板上ではまだです。レーダーのコマンドチャネルはモジュールで確認していません。パネルの HTTPS 証明書（ノード自身が作る）はすべてのブラウザーで試していません。",
    "glance": [
      [
        "役割",
        "ESP32-S3 用レーダーフィールドノード（ファミリー：Field Nodes、親：ARMOR-COMMON）",
      ],
      [
        "技術",
        "C++17, ESP-IDF 5.5.5, ESP32-S3",
      ],
      [
        "テスト",
        "7371 件の検査（ホスト用プログラム 14 本と Python 検査 6 個、`ctest`）",
      ],
      [
        "基板",
        "Waveshare ESP32-S3-ETH（Ethernet）と ESP32-S3-WROOM-1 N16R8（Wi-Fi のみ）",
      ],
      [
        "センサー",
        "ノードあたり最大 3 台のレーダー（LD2450、LD2461）または人感センサー、光センサー VEML7700",
      ],
      [
        "動作環境",
        "Waveshare ESP32-S3-ETH または ESP32-S3-WROOM-1 N16R8、ホストテストは任意のコンピューター",
      ],
      [
        "実機での確認",
        "レーダー付きの実際の Waveshare ESP32-S3-ETH 基板で動作し、CM5 テストベンチに報告",
      ],
      [
        "ライセンス",
        "GPL-3.0-or-later",
      ],
    ],
    "status": {
      "software": "ファームウェアは ESP-IDF 5.5.5 コンテナでビルドでき、実機の ESP32-S3-ETH ボードで動作しています。",
      "tests": "14 のホストプログラムで 7,371 件のチェックが通ります（`ctest`）：デコーダー、設定、ピン表、ユーザー、ネットワーク計画、メッセージのシリアライザー、バージョン確認。",
      "protocols": "LD2450 は実機のレーダーで動作しています。LD2461 と 4 種類の人感センサーのデコーダーはマニュアルの例と一致するだけで、レーダーのコマンドチャネルはモジュールでは未確認です。",
      "ui": "Web パネルはボード上で使われており、実ブラウザーで模擬ノードに対しても試しています。ノード自身が作る HTTPS 証明書は、すべてのブラウザーでは試していません。",
      "hardware": "ハードウェアとして存在する唯一のノードです。実機の Waveshare ESP32-S3-ETH ボードとレーダーが CM5 テストベンチに報告しています。他のセンサーモジュールは接続していません。",
      "security": "Bluetooth の PIN ペアリングとアップデート署名の確認は、本物の署名を使ってコンピューター上で確認済みですが、ボード上ではまだです。独立したレビューもありません。",
      "updates": "無線アップデートはボード上で使われています。署名付きアップデートの確認はまだ実機では実行していません。",
      "integration": "ボードのメッセージは CM5 テストベンチのサーバーに届き、同じメッセージは ARMOR-COMMON の共有スキーマと適合ベクターにも受理されます。実際の設置ではなく、テストベンチでのみ確認しています。",
      "docs": "8 言語と変更履歴は最新です。",
    },
    "docs": [
      "[ノードのパネル](docs/NODE_PANEL.md)：初回起動、ユーザー、ネットワーク、パネルのページ",
      "[セットアップコード](docs/SETUP_CODE.md)と [Bluetooth プロビジョニング](docs/BLE_PROVISIONING.md)",
      "[センサー](docs/SENSORS.md)：6 つのモデルとデコーダー",
      "[ベンチ立ち上げ](docs/BENCH_BRINGUP.md)、[ベンチテスト](docs/BENCH_TESTS.md)、[ハードウェアの境界](docs/HARDWARE_BOUNDARY.md)",
    ],
    "contributing_first": "Pull Request の前に `ctest --test-dir build/host` and `python -I tools/armor_ci_validate.py` を実行してください。通る必要があります。[CONTRIBUTING.md](CONTRIBUTING.md) と[行動規範](CODE_OF_CONDUCT.md)を参照してください。",
    "languages_extra": "",
    "body": {
      "overview": r"""* **2 種類のボード、1 つのファームウェア：** Waveshare ESP32-S3-ETH（Ethernet、標準）と、Ethernet のない ESP32-S3-WROOM-1 N16R8（Wi-Fi のみ：セットアップで参加する Wi-Fi ネットワークを尋ね、ノードは常に独自のネットワークも保ちます）。イメージはビルド時に選びます（`tools/build_node.sh generic s3-eth` または `generic s3-wifi`）。ピン表とアクセス方法はボードに従い、パネルはボードにないものを隠し、イメージは対応するボード専用です。どちらもビルドでき、コンピューター上でテスト済みですが、実機では動かしていません。
* **1 つのノードで最大 270 度をカバー：** 各 Waveshare ESP32-S3-ETH は 3 本の UART で最大 3 基の LD2450 レーダーを読み取ります。レーダーは 75 度ずつずらして取り付け、有線イーサネット（W5500）で DHCP または固定アドレス、給電は PoE か USB です。Studio の *Add a 270° node* は、ノードに割り当て済みの 3 基のレーダーを作成します。
* **すべてのノードに Web パネル：** Studio と同じ見た目で 8 言語に対応し、ファームウェアに組み込まれています。概要、ネットワーク、Wi-Fi、ブローカー、レーダー、ピン、ユーザー、ファームウェア更新、ログ。ユーザーのいないノードは Wi-Fi `ARMOR-SETUP-xxxxxx` を開き、セットアップコードで最初の管理者を作成します。パスワードはソルト付き PBKDF2、セッションはランダムなトークン、すべての設定はノードのフラッシュにあるので、1 つのイメージがすべてのノードに使え、パスワードはコンパイルされません（[パネル](docs/NODE_PANEL.md)）。
* **複数のノードで 1 つの Wi-Fi：** 各ノードはイーサネットポートにつながるアクセスポイントを提供できます。同じ名前とパスワードにしてチャネルを自動（MAC により 1、6、11）にすると、スマートフォンと Wi-Fi センサーには 1 つの DHCP サーバーを持つ 1 つのネットワークに見えます。無線メッシュではなく、各ノードはケーブルを保ちます。代わりにルーターの Wi-Fi に参加でき（ネットワーク検索付き）、ケーブルのないノードは Android アプリから **Bluetooth** で設定できます。
* **サーバー用のピン：** 空いているピンは入力、出力（ブローカーを失ったときの安全な状態付き）、PWM、アナログ読み取りになり、サーバーのデバイスとして現れるので、リレーや接点に新しいファームウェアは要りません。ボードの予約ピンは提示されません。
* **ロールバック付きのオーバーザエア更新**をパネルから行えます（16 MB のフラッシュに 2 スロット）。また Studio から各ノードのパネルへ、ノードが公開するアドレスを使う**リンク**があります。
* **パネルの HTTPS：** ノードは自分の証明書（自己署名、フラッシュに保存）を作り、80 番に加えて 443 番、または 443 番のみでパネルを提供します。セッションクッキーは Secure が付き、ブラウザーの警告と照合できるよう証明書のフィンガープリントを表示します。
* **安定したトラック ID：** 各フレームのターゲットは以前追跡していたものと対応づけられるため、人は同じトラック ID を保ち、フレーム欠落でちらつかず、位置は少し平滑化されます。
* **センサーモデルは 6 種類、ポートごとに 1 つ：** ポートには LD2450 または LD2461（周辺を担うトラッカーで、Studio にモデル固有の視野あり）か、人感センサー（LD2410、LD2412、LD2410S、MR24HPC1）を接続でき、後者はサーバーのデバイスになって在・不在と距離を公開します。パネルで選びます。各センサーの説明、プロトコル、未検証の点は `docs/SENSORS.md` にあります。
* **LD2450 のデコーダー、状態、設定：** 再同期するフレーム検出器がノイズの多いストリームからフレームを見つけ、30 バイトの各フレームから最大 3 つのターゲットが契約のトラックになります。コンソールとパネルはレーダーごとに、報告中か、沈黙か、文字化けかを示します。パネルはモジュールのバージョンを読み、1 つまたは 3 つのターゲットを選び、検出ゾーンを設定することもできます（モジュールでは未検証のプロトコル）。
* **周囲光と契約に厳密なメッセージ：** 自動レンジの VEML7700。公開スキーマに従い、無効なものは書き出さないテレメトリ・ヘルス・情報の JSON、壁時計のタイムスタンプ（SNTP）、MQTT の遺言。どのレーダーも報告していない間はテレメトリを控え、空の「異常なし」は決して送りません。
* **ネットワーク製品のように、全ボード共通の 1 つのイメージ：** ファームウェアは同一で、MAC がボードを区別します（名前を付けるまでは `armor-` と 6 桁）。`adopt_node.py` は、書き込んだばかりのノードにネットワーク経由で管理者、ブローカーの ID、フリート共通の設定を与えます。セットアップコードは MAC から計算されるので、5 台でも 27 台でも作業は同じです。
* **ベンチツール：** USB-C での書き込み、パネル開発用の代役ノード、生フレームのログをテスト用フィクスチャに変換するコンバーター（[ベンチでの立ち上げ](docs/BENCH_BRINGUP.md)）。
* **署名付きの無線アップデート：**ノードが GitHub からインストールするのは、SHA-256 が一致し、管理者の有効な Ed25519 署名を持つイメージだけです（公開鍵はファームウェア内、秘密鍵は管理者の手元から出ません）。管理者がパネルで手動アップロードしたファイルは引き続き受け付けます。パネルのページとメッセージは 8 言語です。
* **PIN 付きの Bluetooth ペアリング：**6 桁の PIN は設定コードから導出され、USB コンソールに表示され、管理者にはパネルにも表示されます。スマートフォンはこれを入力して初めてノードの設定を書き込めます。
* **パネルを使えるのは家だけ：**パネルは既定でプライベートネットワーク（または所有者が指定した VPN などのネットワーク）にだけ応答し、保存する本人を締め出す一覧は拒否します。誤ったパスワードは人ごと・アドレスごとに数え、サーバーのプロキシの背後でも動くので、ノードを公開せずに家の外から使えます。
* **ブローカーとの暗号化通信(TLS、任意):** 初期状態ではオフで、ノードはこれまでどおり暗号化なしの MQTT で通信します。ブローカーページのスイッチと、設備独自の認証局の証明書(PEM、最大 2 KB)の入力欄により、`mqtts://` で接続し、その認証局だけを信頼し、到達したアドレス向けに発行された証明書かを確認します。PEM 証明書 1 つでないものは拒否されます。ホストテストで検証済みで、ハンドシェイクはまだ基板では実行していません。
* **状態報告:** ノードは約 1 分ごとに、稼働時間と直前の再起動の理由、空きメモリ、回線と Wi-Fi 信号、ブローカーへの接続回数、最後に記録したエラーを公開します（`armor/health/<ノード>`、ARMOR-COMMON の `node_health` 契約）。作成するコードは全ノードで共有され、コンピューター上でテストされていますが、ボード上ではまだ動作していません。
* **サーバーからの制御：** Studio はノードをきれいに再起動し、最大 1 時間まで一時停止し（自動的に再開）、作業を待機にし（期限なし、再起動後も維持、ノードは接続したまま応答を続けます）、自分を表示させ、診断のスナップショットを求め、メンテナンス中として印を付けることができます（`armor/control/<ノード>/...`、ARMOR-COMMON の `node_control` 契約）。命令はすべて、その操作専用の使い捨てトークンによる 2 段階で、ブローカーに書き込めるのはサーバーだけです。工場出荷時リセットも消去もディープスリープもありません。一時停止中または待機中のノードは、ターゲットも在室も発行しません（ハートビートは送り続けます）。 このコードは全ノードで共有され、コンピューター上でテスト済みですが、実機ではまだ動作していません。
* **ノード上の境界エンジン（既定ではオフ）：** 6つの検知ゾーンと3つの除外ゾーン（それぞれ角度で回転できる長方形）、方向別に通過を数える3本のトリップワイヤー、3つの侵入経路、ペット除外、マスキング検知。センサーのそばで動作するため、ブローカーに接続できなくても機能し、ブローカー不在の間はイベントを保持して `armor/radar/<ノード>/events` に発行します。ゾーンエディターはノードのパネルにあります。これらはまだセンサーを接続した実機では動かしていません。
* **各センサーの正体と、センサー自身のBluetoothの停止：** 起動時にノードは各センサーのファームウェアバージョンとBluetoothアドレスを読み取り、センサー自身のBluetooth（PINを要求しません）を既定で閉じ、1台のセンサーのシリアル回線を数分間、管理者のPCツールに渡せます（透過シリアルブリッジ）。管理者向けの `GET /metrics` と、設定のエクスポートおよび全か無かのインポートがこれを補います。
* **ケーブルなしの診断：** 正常でない起動（クラッシュ、ウォッチドッグ、電源の電圧低下、メモリ確保の失敗）の後、ヘルスレポートが10分間その原因を伝えます。クラッシュするとコアダンプが残り、パネルから確認、ダウンロード、削除できます。保存された設定はファームウェアのインストールごとにコピーされ、更新で壊れた場合は復元されます。管理者はサーバー経由で、使い捨てトークンを使って、ノードに診断パッケージまたはログを要求できます。
* **証明書フィンガープリントを固定した HTTPS での登録:** `tools/adopt_node.py` は `https://<アドレス>` を受け付け、`--fingerprint`(ノード証明書の SHA-256。リクエストを運ぶ接続そのものの上で確認)または読み取り用の `--show-fingerprint` を使えます。平文の HTTP や、固定アドレス・ホスト名を含む構成ファイルには警告し、そのようなファイルをパネルに読み込むときも警告します。
* **センサーの読み取りはポーリングではなくイベント待ち:** 読み取りタスクはシリアル回線のイベントキューで待機し、届いた分をすべて取り出し、あふれた回線は空にして、回線ごとにあふれとエラーを数えます。`system.reader_idle_ms`(100。0 なら従来の 10 ms ポーリング)で待ち時間を決め、キューが失敗した場合は自動的にポーリングへ戻ります。
* **保存された秘密情報の任意の封印:** 既定ではオフです(`security.seal_secrets`、またはサーバーの `nodes.nvs_encryption`)。オンにすると、ノードが保存するパスワード、トークン、鍵、PIN、パスワードのハッシュが ChaCha20-Poly1305 で封印され、それ以外は読めるままです。オン/オフの切り替えは何も失わずに書き直し、途中で止まっても大丈夫です。eFuse は焼かれず、フラッシュも暗号化されません。鍵は同じチップのパーティションにあるため、基板を手にした人に対する保護には**なりません**。このパーティションがない時期にインストールされたノードは、新しいパーティションテーブルで書き込むまで従来のままです。""",
      "role": r"""ARMOR-NODE-RADAR は境界の目です。各ノードは最大 3 台のレーダーまたは人感センサーを読み取り、軌跡・照度・状態を MQTT で [ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER) に送ります。[ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) はそれをサイト図に描き、[ARMOR-SERVER-AI](https://github.com/JuanenRac/ARMOR-SERVER-AI) はカメラと照らし合わせます。ファームウェアは他のノードと土台を共有し（パネル、Bluetooth 設定、署名付きアップデート、サインイン、時計は [ARMOR-COMMON](https://github.com/JuanenRac/ARMOR-COMMON) のファームウェア基盤から）、1 つのノードで覚えたことがすべてに通用します。

| 名前 | 方法 | 用途 |
|---|---|---|
| ARMOR-SERVER | MQTT `armor/node/<id>/telemetry|health|info|command` | レーダーのメッセージを受け取り（現在は CM5 テストベンチ）、ノードに命令する |
| ARMOR-STUDIO | パネルへのリンク | ノードが公開するアドレスからノードのパネルを開く |
| ARMOR-ANDROID-CONTROL | Bluetooth | 現場でノードを設定 |
| ARMOR-COMMON | コントラクト、ファームウェア基盤 | メッセージはそのスキーマで検証し、共通ファームウェアはここからコピー |""",
      "architecture": r"""<p align="center">
  <img src="images/architecture.svg" alt="ARMOR-NODE-RADAR のアーキテクチャ：呼び出し元、内部、依存先" width="100%">
</p>""",
      "security": r"""| 脅威 | 対策 |
|---|---|
| 平文またはコンパイル済みのパスワード | PBKDF2-HMAC-SHA256 10 000 ラウンド。ファームウェアにパスワードはなく（ユーザーのないノードはセットアップに入る）、ユーザーは最大 4 人（管理者または閲覧者）、8〜64 文字、セッションは最大 6、無操作 30 分 |
| 書き込み直後のノードの乗っ取り | セットアップには起動コードが必要です。ビルドのもの（`CONFIG_ARMOR_SETUP_CODE`）か、フラッシュに保存して USB コンソールに表示するランダムなもの。フリートシークレットがあれば `HMAC-SHA256(シークレット, MAC)`。これはセットアップ用 Wi-Fi（WPA2、ブリッジなし）の鍵でもあります |
| インターネットからのパネルへのアクセス | 初期設定では家庭のプライベートネットワーク（10/8、172.16/12、192.168/16、169.254/16、127/8、一部の VPN が使う 100.64/10）にだけ応答します。設定 `web.admin_sources` で他の IPv4 アドレスやネットワークを追加でき（8 件、120 文字）、それ以外は公開の `GET /api/v1/session` を除き拒否します。保存した本人を締め出すリストは拒否されます |
| HTTP で平文のパネル | 443 番ポートで HTTPS。証明書はノード自身が作成（自己署名、フラッシュ保存、比較用に SHA-256 フィンガープリントを表示）。パネルは http、https、または両方を選べ、セッション Cookie は常に HttpOnly と SameSite=Strict（TLS では Secure も） |
| GitHub からの偽ファームウェア | SHA-256 が一致し、メンテナーの鍵による有効な Ed25519 署名があるイメージだけをインストールします（`no_checksum`、`no_signature`、`bad_signature`、`checksum_mismatch`、`wrong_firmware`、`not_newer`、`version_mismatch` は拒否）。管理者の手動アップロードは検証されません（明示した制限） |
| Bluetooth セットアップの乗っ取り | セットアップコードから導出した 6 桁の PIN を USB コンソールと管理者に表示し、設定を書き込む前にスマホで入力させます。セットアップの時間枠は `CONFIG_ARMOR_BLE_SETUP_MINUTES`（初期 10、1〜120） |
| 害を及ぼす遠隔命令 | その操作に結び付いた使い捨てトークンによる 2 段階。ブローカーのそのトピックに書き込めるのはサーバーだけで、一時停止は最長 1 時間。遠隔命令による工場出荷状態への復元、消去、ディープスリープはありません |
| 基板を持つ人による保存済みシークレットの読み取り | 任意（初期はオフ、スイッチ `security.seal_secrets` またはサーバーの `nodes.nvs_encryption`）：パスワード、トークン、鍵、PIN、ハッシュを ChaCha20-Poly1305 で保護。フラッシュ全体の暗号化や eFuse の焼き込みはしません。鍵は同じチップの別パーティションにあるため、基板を手にした人には防御になりません |
| ブローカーとの平文通信 | 任意の TLS（`mqtts://`）。所有者自身の認証局（PEM 2 KB まで）と名前の検証を使い、初期はオフです。ハンドシェイクはホストのテストでしか動いておらず、基板では未実行です |
| センサー自身の Bluetooth | 既定ではノードがすべての LD センサーの Bluetooth を閉じます（PIN なし）。コンピューターへの透過シリアルブリッジは管理者が数分間だけ開けます |
| 信頼できないネットワークでのノードの採用 | `tools/adopt_node.py https://<アドレス> --fingerprint <SHA-256>` は同じ接続で証明書を検証し、平文 HTTP や固定アドレスのフリートファイルを警告します |
| 危険なピン | 基板の予約ピンは提示されず、ブローカーを失うと出力は安全な状態になり、2 つの機能が同じピンを共有することはできません（検査済み） |
| フリートシークレットを含む公開ファームウェア | `CONFIG_ARMOR_FLEET_SECRET` は初期で空で、公開ビルドにシークレットは含まれません |

脆弱性の報告は [SECURITY.md](SECURITY.md) を参照してください。独立したレビューはありません。""",
      "interfaces": r"""| 部分 | 設定内容 |
|---|---|
| MQTT | `armor/node/<id>/{telemetry,health,info,command}`、`armor/health/<id>`（遺言は `{"node_id":"..","online":false}`）、`armor/control/<id>/{command,result,maintenance}` と `armor/control/all/command`、`armor/device/<id>/<pin>/{state,set}`、`armor/radar/<id>/events`、`armor/radar/<id>/control/armed` |
| パネル（HTTP 80、HTTPS 443） | ルート `session`、`login`、`logout`、`setup`、`status`、`config`（+ export、import）、`wifi/scan`、`time`、`radars`（+ command）、`perimeter`（+ armed、learn、zone）、`pins`（+ command）、`bridge`（+ open、close、io）、`ota`（+ check、install、progress、copy、switch）、`account`、`ble-pin`、`log`、`coredump`、`factory-reset`、`reboot`。管理者向けの `/metrics` と WebSocket `/ws/radar-map`。`tests/check_routes.py` がパネルの呼ぶルートがすべて存在することを検査します |
| パネルの文言 | 8 言語の文言つきエラーコード 76 個（`panel/text.js` に 832 行）。`tests/check_panel_text.py` が検査 |
| ハードウェア | LD2450、LD2461、LD2410、LD2412、LD2410S、MR24HPC1 用の UART 3 本（RX 16、17、18、TX 15、21、38）、SPI の W5500（MOSI 11、MISO 12、SCLK 13、CS 14、INT 10、RST 9、20 MHz）、I2C の VEML7700（GPIO 1 と 2）、BOOT ボタン |""",
      "configuration": r"""| 変数 | 既定値 | 設定内容 |
|---|---|---|
| `CONFIG_ARMOR_NODE_ID` | `""` | 名前。空なら `armor-` と MAC の下位 3 バイト |
| `CONFIG_ARMOR_SETUP_CODE`, `CONFIG_ARMOR_FLEET_SECRET` | `""` | ビルドのセットアップコード（空ならランダム）とフリートシークレット（16 文字以上、リポジトリには置かない） |
| `CONFIG_ARMOR_RADAR_COUNT` | 3 (0-3) | 接続されているレーダーの数 |
| `CONFIG_ARMOR_TRACK_STABILISER` | y | フレーム間でトラックの ID を保つ |
| `CONFIG_ARMOR_MQTT_URI`, `_USERNAME`, `_PASSWORD` | `""` | 最初のブローカー設定（パネルで変更可能） |
| `CONFIG_ARMOR_HEARTBEAT_S` | 10 (2-300) | ヘルスビートの間隔（秒） |
| `CONFIG_ARMOR_TELEMETRY_PERIOD_MS` | 200 (200-5000) | 毎秒最大 5 メッセージ |
| `CONFIG_ARMOR_BLE_SETUP_MINUTES` | 10 (1-120) | Bluetooth セットアップを開けておく時間 |
| `CONFIG_ARMOR_BOARD_S3_ETH` / `_S3_WIFI` | eth | 基板：Waveshare ESP32-S3-ETH または ESP32-S3-WROOM-1 N16R8（Wi-Fi のみ） |
| `CONFIG_ARMOR_BOOT_FACTORY_RESET` | y | 最初の 30 秒以内に BOOT を 8 秒押すと初期化 |
| `system.login_limit_per_minute` | 30 (0-120) | パネルが全員のログインをロックするまでの 1 分あたりの誤パスワード数（0 = 全体の上限なし）。Studio（各ノードのボタン）または `POST /api/v1/admin/nodes/settings` で読み取り・変更でき、パネルのログイン情報は 1 回だけ使われ保存されません |

ライブで調整する設定はパネルにあり、フラッシュに保存されます（例：`system.reader_idle_ms`、`security.seal_secrets`、1 分あたりのログイン失敗上限（30、0〜120）、境界エンジンのゾーン）。ファームウェアの既定値は `sdkconfig.defaults` と `sdkconfig.board.*` にあります。16 MB のフラッシュには `nvs`（64 KB）、`otadata`、`phy_init`、3 MB のスロット `ota_0` と `ota_1`、`coredump`（128 KB）、`nvs_keys`（4 KB）があります（`partitions.csv`）。""",
      "quickstart": r"""**必要なもの:** ホストテスト用の C++17 コンパイラ、イメージのビルド用の ESP-IDF 5.5.5 コンテナ、Waveshare ESP32-S3-ETH または ESP32-S3-WROOM-1 N16R8。

```bash
cmake -S tests -B build/host && cmake --build build/host && ctest --test-dir build/host   # host tests, -Werror
node tools/panel_mock.mjs --user admin:adminpass123   # the panel without a board
python tools/make_fleet.py                             # once: the fleet secret and the shared settings
tools/build_node.sh generic                           # ONE image for every Waveshare board (dist/generic-s3-eth.bin), in the ESP-IDF container
tools/build_node.sh generic s3-wifi                   # the same firmware for an ESP32-S3-WROOM-1 N16R8 with no Ethernet
```

```bat
tools\flash.bat generic COM5 monitor                  # each Waveshare board, once, by USB-C (add s3-wifi for the other board)
```

```bash
tools/adopt_node.py 192.168.0.181 --id perimetro-3 --fleet secrets/fleet.json --broker-ssh-host <cm5> --broker-ssh-user <user>
```

ホストテストには C++17 コンパイラー（Linux、WSL、MSYS2）が必要です。[ベンチでの立ち上げ](docs/BENCH_BRINGUP.md)、[パネル](docs/NODE_PANEL.md)、[ハードウェアの境界](docs/HARDWARE_BOUNDARY.md)を参照。""",
      "testing": r"""```bash
cmake -S tests -B build/host && cmake --build build/host && ctest --test-dir build/host
build/host/emit_samples | python tests/check_contract.py
python -I tools/armor_ci_validate.py
```

ホスト用テストプログラム 14 個と Python の検査 6 個を `ctest` で実行します。ホストのプログラムが数えた検査は 7371 件で、`-Werror` でビルドします。

| 部分 | 対象 |
|---|---|
| `test_core`, `test_sensors`, `test_family`, `test_uart_wake` | デコーダー（LD2450、LD2461、人感センサー 4 種）、フレーム分割、コマンドチャネル、センサーファミリー、UART のウェイク |
| `test_node`, `test_base`, `test_shared`, `test_board_wifi` | 設定とその検査、ピンテーブル、ユーザーとセッション、ネットワーク計画、共通基盤、Wi-Fi 基板 |
| `test_logic`, `test_perimeter`, `test_control`, `test_diag` | ピンのロジック、境界エンジン、2 段階の制御命令、診断 |
| `test_mqtt_tls`, `test_release` | ブローカーへの TLS 接続（ホストのみ）とリリース・署名の検査 |
| `check_panel_text`, `check_task_safety`, `check_save_paths`, `check_ble_session`, `check_routes`, `check_bridge_client` | Python：8 言語のパネル文言（832 行）、タスク、保存パス、ロック下の Bluetooth セッション、ルート、シリアルブリッジのクライアント |

Web パネルは、代役ノード（`tools/panel_mock.mjs`）を相手に実際のブラウザでも検証します。LD2461 と人感センサーのデコーダーはマニュアルの例とだけ一致しています。""",
      "build": "`tools/build_node.sh generic` は ESP-IDF 5.5.5 コンテナで全 Waveshare 基板共通の 1 つのイメージをビルドし、`tools/flash.bat` が USB-C で書き込みます。Wi-Fi のみの基板向けには `s3-wifi` で同じファームウェアをビルドします。リリースにはイメージ、その SHA-256 と Ed25519 署名が基板ごとに付きます。",
      "troubleshooting": r"""| 症状 | 原因 | 対処 |
|---|---|---|
| パスワードを忘れた、またはノードがネットワークに参加しない | セットアップ中でアドレスがないノードは 90 秒後に独自の Wi-Fi `ARMOR-SETUP-xxxxxx` を開きます（`http://192.168.4.1/` を開く） | 最初からやり直すには、電源投入後 30 秒以内に BOOT を 8 秒押し続ける（設定とユーザーを消去）か、パネルの*工場出荷状態に戻す*を使います |
| GitHub からの更新が拒否される | リリースにチェックサムや署名がない、一致しない（`e_no_checksum`、`e_no_signature`、`e_checksum_mismatch`、`e_bad_signature`）、この基板用のイメージがない（`e_no_asset_for_board`）、または別プロジェクトのもの（`e_wrong_firmware`） | ノードは変更されていません。再試行するか、管理者が手動でファイルをアップロード |
| レーダーのコマンドが `no_answer`、`refused`、`disabled` を返す | レーダーの TX 線が未接続、モジュールがフリーズ、またはノードが先に Bluetooth を閉じている | 配線（ベンチ立ち上げの手順）を確認し、パネルからモジュールを再起動 |
| センサー 3 が表示されない、またはレーダーが眠ったままになる | モジュールが応答しなくなった（不正フレームなしの無音） | レーダーページの*モジュール再起動*を使い、その後センサー自身の Bluetooth を閉じる |""",
      "structure": r"""<p align="center">
  <img src="images/repository-structure.svg" alt="ARMOR-NODE-RADAR のリポジトリ構造" width="100%">
</p>

<details>
<summary>ツリーのテキスト版</summary>

```text
ARMOR-NODE-RADAR/
├── main/                                ファームウェア（ESP-IDF コンポーネント）
├── panel/                               ファームウェアに埋め込まれた Web パネル
├── tests/                               ホストテストと Python 検査
├── docs/                                ベンチとパネルの 7 つのガイド
├── tools/                               ビルド・書き込み・採用・フリート・検査のツール
├── .github/                             CI ワークフローと Issue・Pull Request のテンプレート
├── images/                              バナー、アイコン、この README の 2 つの図
├── build.sh build.bat                   共通のプロジェクトワークフローでビルド
├── test.sh test.bat                     共通のワークフローでテストを実行
├── run.sh run.bat                       共通のプロジェクトワークフローで起動
├── armor.project.json                   マニフェスト：バージョン、役割、成熟度、ビルドコマンド
├── CHANGELOG.md                         各バージョンの変更点
├── SECURITY.md SUPPORT.md LICENSE       セキュリティポリシー、サポート、ライセンス
├── CONTRIBUTING.md CODE_OF_CONDUCT.md   貢献方法と行動規範
├── CMakeLists.txt                       ESP-IDF プロジェクト
├── partitions.csv                       フラッシュのテーブル
├── sdkconfig.defaults                   ファームウェアの設定
├── sdkconfig.board.s3-eth               Ethernet 基板
├── sdkconfig.board.s3-wifi              Wi-Fi 基板
├── secrets/                             フリートとノードのファイルの例
├── build-test.sh build-test.bat         共通のワークフローでテストを実行
└── .gitattributes .gitignore            Git の設定
```

</details>""",
      "roadmap": r"""**現時点の既知の制限**

* LD2461 と人感センサーのデコーダーはマニュアルの例とだけ一致し、実モジュールはありません。コマンドチャネルは LD2450 でしか確認していません。
* 更新の署名検証と Bluetooth の PIN ペアリングは実際の署名でコンピューター上では確認済みですが、基板ではまだです。ブローカーとの TLS ハンドシェイクは基板で未実行です。
* ヘルスレポートとサーバーからの制御は基板で未実行、境界エンジンはセンサーとは一度も動いておらず、パネル自身の HTTPS 証明書はすべてのブラウザで未検証、Wi-Fi 基板の実機はありません（Ethernet 基板のみ）。

**今後**

* 実センサーと CM5 テストベンチで境界エンジン、ヘルスレポート、制御命令を動かし、ブローカーへの TLS 接続と署名付き更新を基板で試す。""",
    },
  },
  "zh": {
    "tagline": "现场节点固件（Waveshare ESP32-S3-ETH，三个雷达或存在传感器，以太网和 Wi-Fi），自带网页面板，并有在电脑上测试过的核心",
    "honest": "雷达节点是目前唯一真正存在的硬件节点：它的固件运行在带雷达的真实 Waveshare ESP32-S3-ETH 板上，向 CM5 测试台报告，其网页面板和无线更新也在该板上使用。与硬件无关的核心（14 个测试程序中的 7,371 项检查：LD2450、LD2461 和四种存在传感器的解码器、LD2450 命令通道、设置及其检查、引脚表、用户和会话、网络方案、ARMOR-COMMON 接受其输出的消息序列化器，以及版本和签名检查）在计算机上测试，**网页面板**已在真实浏览器中对照替身节点验证，**固件镜像**可在 ESP-IDF 5.5.5 容器中构建。**尚未**证明的是：LD2461 和存在传感器的解码器只与其手册中的示例吻合，背后没有真实模块；更新的签名检查和带 PIN 的蓝牙配对已在计算机上用真实签名验证，但尚未在板上验证；雷达命令通道没有对照真实模块检查；面板的 HTTPS 证书（由节点自己生成）没有在所有浏览器中试过。",
    "glance": [
      [
        "角色",
        "ESP32-S3 雷达现场节点（家族：Field Nodes，上级：ARMOR-COMMON）",
      ],
      [
        "技术栈",
        "C++17, ESP-IDF 5.5.5, ESP32-S3",
      ],
      [
        "测试",
        "7371 项检查（14 个主机程序和 6 项 Python 检查，`ctest`）",
      ],
      [
        "电路板",
        "Waveshare ESP32-S3-ETH（以太网）和 ESP32-S3-WROOM-1 N16R8（仅 Wi-Fi）",
      ],
      [
        "传感器",
        "每个节点最多 3 台雷达（LD2450、LD2461）或存在传感器，以及 VEML7700 光传感器",
      ],
      [
        "运行位置",
        "Waveshare ESP32-S3-ETH 或 ESP32-S3-WROOM-1 N16R8；主机测试可在任何计算机上运行",
      ],
      [
        "真实硬件",
        "运行在带雷达的真实 Waveshare ESP32-S3-ETH 板上，向 CM5 测试台报告",
      ],
      [
        "许可证",
        "GPL-3.0-or-later",
      ],
    ],
    "status": {
      "software": "固件可在 ESP-IDF 5.5.5 容器中构建，并在真实的 ESP32-S3-ETH 板上运行。",
      "tests": "14 个主机程序中的 7,371 项检查通过（`ctest`）：解码器、设置、引脚表、用户、网络方案、消息序列化器和版本检查。",
      "protocols": "LD2450 已在真实雷达上运行；LD2461 和四种人体存在传感器的解码器只与其手册中的示例一致，雷达命令通道尚未对照模块检查。",
      "ui": "网页面板已在板子上使用，并在真实浏览器中对模拟节点做过测试；由节点自己生成的 HTTPS 证书尚未在所有浏览器中试过。",
      "hardware": "这是唯一实际存在的硬件节点：一块真实的 Waveshare ESP32-S3-ETH 板带着雷达向 CM5 测试台上报；没有连接其他传感器模块。",
      "security": "蓝牙 PIN 配对和更新签名检查已在电脑上用真实签名证明，但尚未在板子上验证；没有经过独立审查。",
      "updates": "空中更新已在板子上使用；签名更新的检查尚未在板子上运行过。",
      "integration": "板子的消息送达 CM5 测试台上的服务器，同样的消息也被 ARMOR-COMMON 的共享模式和一致性向量接受。仅在测试台上见过，尚未在实际安装中使用。",
      "docs": "八种语言和更新日志均为最新。",
    },
    "docs": [
      "[节点面板](docs/NODE_PANEL.md)：首次启动、用户、网络、面板页面",
      "[设置码](docs/SETUP_CODE.md)和[蓝牙配置](docs/BLE_PROVISIONING.md)",
      "[传感器](docs/SENSORS.md)：六种型号及其解码器",
      "[台架调试](docs/BENCH_BRINGUP.md)、[台架测试](docs/BENCH_TESTS.md)和[硬件边界](docs/HARDWARE_BOUNDARY.md)",
    ],
    "contributing_first": "提交 Pull Request 之前请运行 `ctest --test-dir build/host` and `python -I tools/armor_ci_validate.py`：必须通过。参见 [CONTRIBUTING.md](CONTRIBUTING.md) 和[行为准则](CODE_OF_CONDUCT.md)。",
    "languages_extra": "",
    "body": {
      "overview": r"""* **两种开发板，一套固件：** Waveshare ESP32-S3-ETH（以太网，默认）和不带以太网的 ESP32-S3-WROOM-1 N16R8（仅 Wi-Fi：设置时会询问要加入的 Wi-Fi 网络，节点始终保留自己的网络）。镜像在构建时选择（`tools/build_node.sh generic s3-eth` 或 `generic s3-wifi`）；引脚表和接入方式随开发板而定，面板会隐藏开发板没有的功能，镜像只适用于对应的开发板。两者都能构建并已在电脑上测试，但都没在开发板上运行过。
* **一个节点最多覆盖 270 度：** 每块 Waveshare ESP32-S3-ETH 在其三个 UART 上读取最多三个 LD2450 雷达，彼此相隔 75 度安装，通过有线以太网（W5500）使用 DHCP 或固定地址，由 PoE 或 USB 供电。Studio 的 *Add a 270° node* 会创建已与节点关联的三个雷达。
* **每个节点自带网页面板，** 外观与 Studio 一致，支持八种语言，内嵌于固件：概览、网络、Wi-Fi、代理、雷达、引脚、用户、固件更新和日志。没有用户的节点会开启 Wi-Fi `ARMOR-SETUP-xxxxxx`，并用设置码创建第一个管理员；密码使用加盐 PBKDF2，会话是随机令牌，所有设置都保存在节点的闪存中，因此一个镜像适用于所有节点，且不会把任何密码编译进去（[面板](docs/NODE_PANEL.md)）。
* **多个节点组成一个 Wi-Fi：** 每个节点可提供接到其以太网口的接入点；给节点设置相同的名称和密码，信道设为自动（按 MAC 取 1、6 或 11），手机和 Wi-Fi 传感器就会看到一个网络和一个 DHCP 服务器。这不是无线 mesh：每个节点仍保留自己的网线。节点也可以改为加入路由器的 Wi-Fi（可搜索网络），没有网线的节点可通过 Android 应用用**蓝牙**配置。
* **为服务器提供引脚：** 任何空闲引脚都可成为输入、输出（代理丢失时有安全状态）、PWM 或模拟读数，并显示为服务器的一个设备，因此继电器或触点无需新固件。开发板的保留引脚永远不会被提供。
* **通过面板进行带回滚的空中更新（OTA）**（16 MB 闪存上有两个槽位），以及从 Studio 到每个节点面板的**链接**，地址来自节点发布的信息。
* **通过 HTTPS 访问面板：** 节点生成自己的证书（自签名，保存在闪存中），除 80 端口外也在 443 端口提供面板，或只使用 443；会话 Cookie 标为 Secure，并显示证书指纹以便与浏览器的警告比对。
* **稳定的轨迹身份：** 每帧的目标会与之前跟踪的目标匹配，因此一个人保持同一轨迹编号，丢帧不会闪烁，位置也会略微平滑。
* **六种传感器型号，每个端口一种：** 端口可接 LD2450 或 LD2461（为周界提供数据的跟踪器，Studio 中有该型号自己的探测范围），或存在传感器（LD2410、LD2412、LD2410S、MR24HPC1），后者成为服务器的设备并发布存在与距离。在面板中选择；每种传感器是什么、其协议以及哪些未经验证，见 `docs/SENSORS.md`。
* **LD2450 解码器、健康状态与配置：** 可重新同步的分帧器能在有噪声的数据流中找到帧；每个 30 字节的帧给出最多三个目标，成为契约轨迹；控制台和面板会按雷达说明它是在上报、静默还是数据混乱。面板还能读取模块版本、选择一个或三个目标并设置检测区域（这一协议尚未对照模块检查）。
* **环境光与严格符合契约的消息：** 带自动量程的 VEML7700；遵循已发布模式的遥测、健康和信息 JSON，拒绝写入任何无效内容，带墙上时钟时间戳（SNTP）和 MQTT 遗嘱。没有雷达上报时会扣留遥测，绝不发出空的“一切正常”。
* **一个镜像适用于所有开发板，像网络产品一样：** 固件相同，由 MAC 区分开发板（命名前为 `armor-` 加六位数字）；`adopt_node.py` 通过网络给刚刷好的节点分配管理员、代理身份和整个节点群共用的设置，设置码由其 MAC 计算得出，因此 5 个节点和 27 个节点工作量相同。
* **台架工具：** 通过 USB-C 刷写、用于开发面板的替身节点，以及把原始帧日志转换成测试夹具的转换器（[台架调试](docs/BENCH_BRINGUP.md)）。
* **签名的无线更新：**节点只会从 GitHub 安装 SHA-256 匹配且带有维护者有效 Ed25519 签名的镜像（公钥在固件中，私钥从不离开维护者）；管理员在面板中手动上传的文件仍然被接受。面板的页面和消息有八种语言。
* **带 PIN 的蓝牙配对：**六位 PIN 由设置码派生，打印在 USB 控制台上并向管理员显示在面板中；手机必须输入它才能写入节点的设置。
* **只有家中才能使用面板：**面板默认只响应私有网络（或所有者列出的网络，如 VPN），拒绝会把保存者自己挡在外面的列表，按人和按地址统计错误密码，并可在服务器代理之后工作，从而无需公开节点就能在家外访问。
* **可选的与代理加密连接(TLS):** 默认关闭,因此节点仍像以前一样使用未加密的 MQTT。代理页面中的一个开关和一个用于填写本安装自有证书颁发机构证书(PEM,最大 2 KB)的框,会让节点用 `mqtts://` 连接、只信任该机构,并检查代理证书是否为其所到达的地址而签发;不是单个 PEM 证书的内容会被拒绝。已有主机测试覆盖;握手尚未在电路板上运行。
* **健康报告：** 节点大约每分钟发布一次：已运行多久、上次为何重启、可用内存、连接与 Wi-Fi 信号、连接代理的次数以及记录的最后一个错误（`armor/health/<节点>`，即 ARMOR-COMMON 的 `node_health` 契约）。生成它的代码由所有节点共享并在计算机上测试；尚未在开发板上运行。
* **由服务器控制：** Studio 可以干净地重启节点、将其暂停至多一小时（自动恢复）、让其工作进入待机（无期限，重启后仍保持，节点保持连接并继续应答）、让它显示自己、请求诊断快照，并把它标记为维护中（`armor/control/<节点>/...`，ARMOR-COMMON 的 `node_control` 契约）。每条命令分两步，使用只属于该操作的一次性令牌，只有服务器可以在代理上写入，并且没有恢复出厂设置、擦除或深度睡眠。节点处于暂停或待机时，不发布目标和人员存在信息（心跳仍表明它在线）。 该代码由所有节点共用，并已在计算机上测试；尚未在电路板上运行过。
* **节点上的周界引擎（默认关闭）：** 六个检测区和三个排除区，每个都是可按角度旋转的矩形，三条按方向统计穿越次数的绊线，三条进入路径，宠物免疫和遮挡检测。它与传感器一起在节点上运行，因此在无法连接 broker 时仍然工作，broker 不在时保存事件，并发布到 `armor/radar/<节点>/events`；区域编辑器在节点的面板中。以上功能尚未在带传感器的实际电路板上运行过。
* **每个传感器是谁，以及关闭其自带蓝牙：** 启动时，节点读取每个传感器的固件版本和蓝牙地址，默认关闭传感器自带的蓝牙（它不要求 PIN），并可在几分钟内把一个传感器的串口线交给管理员的电脑工具（透明串口桥）。面向管理员的 `GET /metrics`，以及设置的导出和全有或全无的导入，使之更加完整。
* **无需线缆的诊断：** 在一次不干净的启动之后（崩溃、看门狗、电源跌落、内存分配失败），健康报告会在十分钟内说明原因；崩溃会留下核心转储（core dump），可在面板中查看、下载或删除；已保存的设置会在每次固件安装前被复制，并在更新损坏它们时恢复；管理员还可以通过服务器，用一次性令牌向节点索取诊断包或其日志。
* **通过 HTTPS 并固定证书指纹进行接入:** `tools/adopt_node.py` 接受 `https://<地址>`,配合 `--fingerprint`(节点证书的 SHA-256,在承载请求的同一连接上校验)或 `--show-fingerprint` 读取指纹;对明文 HTTP 以及带固定地址或主机名的设备清单文件会给出警告,面板在导入这类文件时也会警告。
* **传感器读取任务改为等待事件而不是轮询:** 读取任务在串口线路的事件队列上休眠,并一次取走所有到达的数据,在溢出时清空该线路,并按线路统计溢出和错误;`system.reader_idle_ms`(100;0 = 之前的 10 ms 轮询)设定等待时间,某个队列出错时会自动退回轮询。
* **可选的已存储机密封存:** 默认关闭(`security.seal_secrets`,或服务器的 `nodes.nvs_encryption`)。开启后,节点保存的密码、令牌、密钥、PIN 和密码哈希会用 ChaCha20-Poly1305 封存,其余内容仍可读取;开启或关闭时会无损重写,即使节点中途停止也不会丢失。不会烧写 eFuse,闪存也不加密:密钥在同一芯片的一个分区中,因此**不能**防范持有电路板的人;在该分区出现之前安装的节点会保持原样,直到用新的分区表重新烧录。""",
      "role": r"""ARMOR-NODE-RADAR 是周界的眼睛。每个节点读取最多三个雷达或存在传感器，并通过 MQTT 向 [ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER) 发布轨迹、光照和健康状态；[ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) 把它们画在场地平面图上，[ARMOR-SERVER-AI](https://github.com/JuanenRac/ARMOR-SERVER-AI) 把它们与摄像头对照权衡。它的固件与其他节点共用一个基础（面板、蓝牙设置、签名更新、登录和时钟都来自 [ARMOR-COMMON](https://github.com/JuanenRac/ARMOR-COMMON) 的固件基础），所以在一个节点上学到的对所有节点都适用。

| 名称 | 方式 | 用途 |
|---|---|---|
| ARMOR-SERVER | MQTT `armor/node/<id>/telemetry|health|info|command` | 接收雷达消息（目前是 CM5 测试台）并向节点下达命令 |
| ARMOR-STUDIO | 面板链接 | 通过节点发布的地址打开节点面板 |
| ARMOR-ANDROID-CONTROL | Bluetooth | 在现场设置节点 |
| ARMOR-COMMON | 合约、固件基础 | 消息按其模式校验；公共固件由此复制 |""",
      "architecture": r"""<p align="center">
  <img src="images/architecture.svg" alt="ARMOR-NODE-RADAR 的架构：谁调用它、它包含什么、它依赖什么" width="100%">
</p>""",
      "security": r"""| 威胁 | 防御 |
|---|---|
| 明文或编译进固件的密码 | PBKDF2-HMAC-SHA256，10 000 轮；固件中没有密码（没有用户的节点会进入设置）；最多 4 个用户（管理员或查看者），8 到 64 个字符；最多 6 个会话，空闲 30 分钟 |
| 接管刚刷写的节点 | 设置需要启动码：构建时的码（`CONFIG_ARMOR_SETUP_CODE`），或保存在闪存中并显示在 USB 控制台上的随机码；有机群密钥时为 `HMAC-SHA256(密钥, MAC)`；它也是设置用 Wi-Fi 的密钥（WPA2，绝不桥接） |
| 从互联网访问面板 | 默认只响应家庭的私有网络（10/8、172.16/12、192.168/16、169.254/16、127/8，以及某些 VPN 使用的 100.64/10）；设置 `web.admin_sources` 可列出其他 IPv4 地址和网络（8 项，120 个字符）；除公开身份 `GET /api/v1/session` 外，其余一律拒绝；会把保存者自己锁在外面的列表会被拒绝 |
| 通过 HTTP 明文访问面板 | 在 443 端口提供 HTTPS，证书由节点自己生成（自签名、存于闪存，显示 SHA-256 指纹以便比对）；面板可设为 http、https 或两者；会话 Cookie 始终为 HttpOnly 和 SameSite=Strict（TLS 下还有 Secure） |
| 来自 GitHub 的伪造固件 | 只有 SHA-256 匹配且带有维护者密钥有效 Ed25519 签名的镜像才会被安装（`no_checksum`、`no_signature`、`bad_signature`、`checksum_mismatch`、`wrong_firmware`、`not_newer`、`version_mismatch` 会拒绝）；管理员手动上传不做校验：这是明确的限制 |
| 劫持蓝牙设置 | 由设置码派生的 6 位 PIN，显示在 USB 控制台并对管理员可见；手机必须先输入才能写入设置；设置窗口时长为 `CONFIG_ARMOR_BLE_SETUP_MINUTES`（默认 10，范围 1 到 120） |
| 造成危害的远程命令 | 两步操作，使用与该操作绑定的一次性令牌；只有服务器能向代理写入这些主题；暂停最长一小时；远程命令没有恢复出厂、擦除和深度睡眠 |
| 拿到电路板的人读取存储的机密 | 可选（默认关闭，开关为 `security.seal_secrets` 或服务器的 `nodes.nvs_encryption`）：用 ChaCha20-Poly1305 保护密码、令牌、密钥、PIN 和哈希。它不加密闪存也不烧写 eFuse：密钥位于同一芯片的分区中，因此无法防御拿到电路板的人 |
| 与代理的明文连接 | 可选 TLS（`mqtts://`），使用所有者自己的证书颁发机构（PEM 最大 2 KB）并检查名称；默认关闭。握手只在主机测试中运行过，没有在电路板上运行 |
| 传感器自带的蓝牙 | 默认情况下节点会关闭每个 LD 传感器的蓝牙（无需 PIN）；通向计算机的透明串口桥仅由管理员开启几分钟 |
| 在不可信网络上接入节点 | `tools/adopt_node.py https://<地址> --fingerprint <SHA-256>` 在同一连接中校验证书；对明文 HTTP 和使用固定地址的机群文件给出警告 |
| 危险的引脚 | 电路板的保留引脚从不提供；代理丢失时输出进入安全状态；两个功能不能共用一个引脚（已检查） |
| 带有机群密钥的公开固件 | `CONFIG_ARMOR_FLEET_SECRET` 默认为空：公开构建不含任何密钥 |

报告漏洞请阅读 [SECURITY.md](SECURITY.md)。没有经过独立审查。""",
      "interfaces": r"""| 部分 | 作用 |
|---|---|
| MQTT | `armor/node/<id>/{telemetry,health,info,command}`、`armor/health/<id>`（遗嘱为 `{"node_id":"..","online":false}`）、`armor/control/<id>/{command,result,maintenance}` 和 `armor/control/all/command`、`armor/device/<id>/<pin>/{state,set}`、`armor/radar/<id>/events`、`armor/radar/<id>/control/armed` |
| 面板（HTTP 80、HTTPS 443） | 路由 `session`、`login`、`logout`、`setup`、`status`、`config`（+ export、import）、`wifi/scan`、`time`、`radars`（+ command）、`perimeter`（+ armed、learn、zone）、`pins`（+ command）、`bridge`（+ open、close、io）、`ota`（+ check、install、progress、copy、switch）、`account`、`ble-pin`、`log`、`coredump`、`factory-reset`、`reboot`；面向管理员的 `/metrics` 和 WebSocket `/ws/radar-map`；`tests/check_routes.py` 检查面板调用的每条路由都存在 |
| 面板文字 | 76 个带八种语言文字的错误码（`panel/text.js` 中 832 行），由 `tests/check_panel_text.py` 检查 |
| 硬件 | 用于 LD2450、LD2461、LD2410、LD2412、LD2410S 和 MR24HPC1 的 3 个 UART（RX 16、17、18；TX 15、21、38）；SPI 接口的 W5500（MOSI 11、MISO 12、SCLK 13、CS 14、INT 10、RST 9、20 MHz）；I2C 上的 VEML7700（GPIO 1 和 2）；BOOT 按钮 |""",
      "configuration": r"""| 变量 | 默认值 | 作用 |
|---|---|---|
| `CONFIG_ARMOR_NODE_ID` | `""` | 名称；为空则为 `armor-` 加 MAC 的最后三个字节 |
| `CONFIG_ARMOR_SETUP_CODE`, `CONFIG_ARMOR_FLEET_SECRET` | `""` | 构建的设置码（为空则随机）和机群密钥（16 个字符以上，绝不放入仓库） |
| `CONFIG_ARMOR_RADAR_COUNT` | 3 (0-3) | 已连接的雷达数量 |
| `CONFIG_ARMOR_TRACK_STABILISER` | y | 在帧与帧之间保持轨迹身份 |
| `CONFIG_ARMOR_MQTT_URI`, `_USERNAME`, `_PASSWORD` | `""` | 最初的代理设置（可在面板中修改） |
| `CONFIG_ARMOR_HEARTBEAT_S` | 10 (2-300) | 健康心跳间隔（秒） |
| `CONFIG_ARMOR_TELEMETRY_PERIOD_MS` | 200 (200-5000) | 每秒最多 5 条消息 |
| `CONFIG_ARMOR_BLE_SETUP_MINUTES` | 10 (1-120) | 蓝牙设置保持开启的时间 |
| `CONFIG_ARMOR_BOARD_S3_ETH` / `_S3_WIFI` | eth | 电路板：Waveshare ESP32-S3-ETH 或 ESP32-S3-WROOM-1 N16R8（仅 Wi-Fi） |
| `CONFIG_ARMOR_BOOT_FACTORY_RESET` | y | 在前 30 秒内按住 BOOT 8 秒可重新开始 |
| `system.login_limit_per_minute` | 30 (0-120) | 面板对所有人锁定登录前每分钟允许的错误密码次数（0 = 无全局限制）；可在 Studio（每个节点上的按钮）或通过 `POST /api/v1/admin/nodes/settings` 读取和修改，面板登录信息只使用一次，绝不保存 |

现场调节的设置在面板中并保存在闪存里（例如 `system.reader_idle_ms`、`security.seal_secrets`、每分钟登录失败上限（30，范围 0 到 120）以及周界引擎的区域）；固件默认值在 `sdkconfig.defaults` 和 `sdkconfig.board.*` 中。16 MB 闪存包含 `nvs`（64 KB）、`otadata`、`phy_init`、两个 3 MB 槽位 `ota_0` 和 `ota_1`、`coredump`（128 KB）和 `nvs_keys`（4 KB）（`partitions.csv`）。""",
      "quickstart": r"""**要求:** 用于主机测试的 C++17 编译器；用于构建镜像的 ESP-IDF 5.5.5 容器；Waveshare ESP32-S3-ETH 或 ESP32-S3-WROOM-1 N16R8。

```bash
cmake -S tests -B build/host && cmake --build build/host && ctest --test-dir build/host   # host tests, -Werror
node tools/panel_mock.mjs --user admin:adminpass123   # the panel without a board
python tools/make_fleet.py                             # once: the fleet secret and the shared settings
tools/build_node.sh generic                           # ONE image for every Waveshare board (dist/generic-s3-eth.bin), in the ESP-IDF container
tools/build_node.sh generic s3-wifi                   # the same firmware for an ESP32-S3-WROOM-1 N16R8 with no Ethernet
```

```bat
tools\flash.bat generic COM5 monitor                  # each Waveshare board, once, by USB-C (add s3-wifi for the other board)
```

```bash
tools/adopt_node.py 192.168.0.181 --id perimetro-3 --fleet secrets/fleet.json --broker-ssh-host <cm5> --broker-ssh-user <user>
```

主机测试需要任意 C++17 编译器（Linux、WSL、MSYS2）。参见[台架调试](docs/BENCH_BRINGUP.md)、[面板](docs/NODE_PANEL.md)和[硬件边界](docs/HARDWARE_BOUNDARY.md)。""",
      "testing": r"""```bash
cmake -S tests -B build/host && cmake --build build/host && ctest --test-dir build/host
build/host/emit_samples | python tests/check_contract.py
python -I tools/armor_ci_validate.py
```

`ctest` 运行 14 个主机测试程序和 6 个 Python 检查；主机程序统计的检查共 7371 项，使用 `-Werror` 构建。

| 部分 | 覆盖内容 |
|---|---|
| `test_core`, `test_sensors`, `test_family`, `test_uart_wake` | 解码器（LD2450、LD2461、四种存在传感器）、帧切分、命令通道、传感器系列和 UART 唤醒 |
| `test_node`, `test_base`, `test_shared`, `test_board_wifi` | 设置及其检查、引脚表、用户与会话、网络方案、共享基础和 Wi-Fi 电路板 |
| `test_logic`, `test_perimeter`, `test_control`, `test_diag` | 引脚逻辑、周界引擎、两步控制命令和诊断 |
| `test_mqtt_tls`, `test_release` | 与代理的 TLS 连接（仅主机）以及发布和签名检查 |
| `check_panel_text`, `check_task_safety`, `check_save_paths`, `check_ble_session`, `check_routes`, `check_bridge_client` | Python：八种语言的面板文字（832 行）、任务、保存路径、受锁保护的蓝牙会话、路由和串口桥客户端 |

网页面板还会在真实浏览器中对着模拟节点（`tools/panel_mock.mjs`）进行验证。LD2461 和存在传感器的解码器只与其手册中的示例相符。""",
      "build": "`tools/build_node.sh generic` 在 ESP-IDF 5.5.5 容器中为所有 Waveshare 电路板构建同一个镜像，`tools/flash.bat` 通过 USB-C 写入；仅 Wi-Fi 的电路板用 `s3-wifi` 构建同一固件。每个发布版都带有镜像、其 SHA-256 和 Ed25519 签名，每块电路板一份。",
      "troubleshooting": r"""| 现象 | 原因 | 处理 |
|---|---|---|
| 忘记了密码，或节点不再加入网络 | 处于设置状态且 90 秒后仍无地址的节点会开启自己的 Wi-Fi `ARMOR-SETUP-xxxxxx`（打开 `http://192.168.4.1/`） | 要重新开始，请在上电后 30 秒内按住 BOOT 8 秒（会清除设置和用户），或使用面板中的*恢复出厂设置* |
| 来自 GitHub 的更新被拒绝 | 发布版缺少校验和或签名，或二者不匹配（`e_no_checksum`、`e_no_signature`、`e_checksum_mismatch`、`e_bad_signature`），没有适用于此电路板的镜像（`e_no_asset_for_board`），或属于另一个项目（`e_wrong_firmware`） | 节点未发生任何变化；请重试，或由管理员手动上传文件 |
| 雷达命令返回 `no_answer`、`refused` 或 `disabled` | 雷达的 TX 线未连接、模块卡死，或节点先关闭了其蓝牙 | 检查接线（见台架调试），在面板中重启模块 |
| 节点没有显示传感器 3，或让雷达休眠 | 模块不再发送数据（静默，且没有坏帧） | 在雷达页面使用*重启模块*，然后关闭传感器自带的蓝牙 |""",
      "structure": r"""<p align="center">
  <img src="images/repository-structure.svg" alt="ARMOR-NODE-RADAR 的仓库结构" width="100%">
</p>

<details>
<summary>目录树的文本版</summary>

```text
ARMOR-NODE-RADAR/
├── main/                                固件：一个 ESP-IDF 组件
├── panel/                               嵌入固件的网页面板
├── tests/                               主机测试和 Python 检查
├── docs/                                7 份台架与面板指南
├── tools/                               构建、刷写、接入、机群和检查工具
├── .github/                             CI 工作流以及 Issue 和 Pull Request 模板
├── images/                              横幅、图标和本 README 的两幅图
├── build.sh build.bat                   通过共享的项目工作流构建
├── test.sh test.bat                     通过共享工作流运行测试
├── run.sh run.bat                       通过共享的项目工作流启动
├── armor.project.json                   清单：版本、角色、成熟度、构建命令
├── CHANGELOG.md                         每个版本的变化
├── SECURITY.md SUPPORT.md LICENSE       安全策略、支持和许可证
├── CONTRIBUTING.md CODE_OF_CONDUCT.md   如何贡献与行为准则
├── CMakeLists.txt                       ESP-IDF 项目
├── partitions.csv                       闪存分区表
├── sdkconfig.defaults                   固件设置
├── sdkconfig.board.s3-eth               以太网电路板
├── sdkconfig.board.s3-wifi              Wi-Fi 电路板
├── secrets/                             机群和节点文件示例
├── build-test.sh build-test.bat         通过共享工作流运行测试
└── .gitattributes .gitignore            Git 设置
```

</details>""",
      "roadmap": r"""**目前已知的限制**

* LD2461 和存在传感器的解码器只与手册中的示例相符，没有真实模块；命令通道只对 LD2450 验证过。
* 更新的签名校验和蓝牙 PIN 配对已在计算机上用真实签名验证，但尚未在电路板上验证；与代理的 TLS 握手尚未在电路板上运行。
* 健康报告和服务器控制尚未在电路板上运行；周界引擎从未配合传感器运行；面板自己的 HTTPS 证书未在所有浏览器中试过；Wi-Fi 电路板没有实物（只有以太网电路板）。

**下一步**

* 用真实传感器和 CM5 测试台运行周界引擎、健康报告和控制命令；在电路板上试验与代理的 TLS 连接和签名更新。""",
    },
  },
  "pt": {
    "tagline": "Firmware de nó de campo (Waveshare ESP32-S3-ETH, três radares ou sensores de presença, Ethernet e Wi-Fi) com o seu próprio painel web, e o seu núcleo testado em anfitrião",
    "honest": "O nó radar é o único nó que existe como hardware: o seu firmware corre numa placa real Waveshare ESP32-S3-ETH com um radar e reporta à bancada de testes do CM5, e o seu painel web e as atualizações pelo ar são usados nela. O núcleo independente do hardware (4,633 verificações em 14 programas de teste: os descodificadores do LD2450, do LD2461 e de quatro sensores de presença, o canal de comandos do LD2450, as definições e as suas verificações, a tabela de pinos, utilizadores e sessões, o plano de rede, o serializador de mensagens cuja saída o ARMOR-COMMON aceita, e as verificações de versão e assinatura) é testado num computador, o **painel web** foi exercitado num navegador real contra um nó de substituição e a **imagem do firmware compila** no contentor ESP-IDF 5.5.5. O que **ainda não** está provado: os descodificadores do LD2461 e dos sensores de presença só coincidem com os exemplos resolvidos dos seus manuais, sem um módulo por trás; a verificação da assinatura das atualizações e o emparelhamento Bluetooth com PIN estão provados no computador com assinaturas reais mas ainda não na placa; o canal de comandos do radar não foi confrontado com um módulo; e o certificado HTTPS do painel (feito pelo próprio nó) não foi experimentado em todos os navegadores.",
    "glance": [
      [
        "Função",
        "Nó de campo radar para ESP32-S3 (família: Field Nodes, pai: ARMOR-COMMON)",
      ],
      [
        "Tecnologia",
        "C++17, ESP-IDF 5.5.5, ESP32-S3",
      ],
      [
        "Testes",
        "7371 verificações em 14 programas de anfitrião e 6 em Python (`ctest`)",
      ],
      [
        "Placas",
        "Waveshare ESP32-S3-ETH (Ethernet) e ESP32-S3-WROOM-1 N16R8 (só Wi-Fi)",
      ],
      [
        "Sensores",
        "Até 3 radares (LD2450, LD2461) ou sensores de presença por nó, sensor de luz VEML7700",
      ],
      [
        "Funciona em",
        "Waveshare ESP32-S3-ETH ou ESP32-S3-WROOM-1 N16R8; testes de anfitrião em qualquer computador",
      ],
      [
        "Em hardware real",
        "Corre numa placa real Waveshare ESP32-S3-ETH com um radar, reportando à bancada de testes do CM5",
      ],
      [
        "Licença",
        "GPL-3.0-or-later",
      ],
    ],
    "status": {
      "software": "O firmware compila no contentor ESP-IDF 5.5.5 e funciona numa placa ESP32-S3-ETH real.",
      "tests": "Passam 7.371 verificações em 14 programas de anfitrião (`ctest`): os descodificadores, as definições, a tabela de pinos, os utilizadores, o plano de rede, o serializador de mensagens e as verificações de versão.",
      "protocols": "O LD2450 funciona com um radar real; os descodificadores do LD2461 e dos quatro sensores de presença só coincidem com os exemplos dos seus manuais, e o canal de comandos do radar não foi verificado com um módulo.",
      "ui": "O painel web está em uso na placa e foi exercitado num navegador real contra um nó simulado; o seu certificado HTTPS, criado pelo próprio nó, não foi experimentado em todos os navegadores.",
      "hardware": "É o único nó que existe como hardware: uma placa Waveshare ESP32-S3-ETH real com um radar reporta à bancada de testes CM5; não há mais nenhum módulo de sensor ligado.",
      "security": "O emparelhamento por PIN Bluetooth e a verificação da assinatura das atualizações estão provados num computador com assinaturas reais, mas ainda não na placa; não houve revisão independente.",
      "updates": "As atualizações pelo ar estão em uso na placa; a verificação das atualizações assinadas ainda não foi executada lá.",
      "integration": "As mensagens da placa chegam ao servidor da bancada de testes CM5, e essas mesmas mensagens são aceites pelos esquemas partilhados e pelos vetores de conformidade do ARMOR-COMMON. Só foi visto na bancada, não numa instalação.",
      "docs": "Oito idiomas e o registo de alterações estão atualizados.",
    },
    "docs": [
      "[Painel do nó](docs/NODE_PANEL.md): primeiro arranque, utilizadores, rede, as páginas do painel",
      "[Código de configuração](docs/SETUP_CODE.md) e [provisionamento Bluetooth](docs/BLE_PROVISIONING.md)",
      "[Sensores](docs/SENSORS.md): os seis modelos e os seus descodificadores",
      "[Arranque em bancada](docs/BENCH_BRINGUP.md), [testes de bancada](docs/BENCH_TESTS.md) e [limite do hardware](docs/HARDWARE_BOUNDARY.md)",
    ],
    "contributing_first": "Antes de um pull request, execute `ctest --test-dir build/host` and `python -I tools/armor_ci_validate.py`: tem de passar. Consulte [CONTRIBUTING.md](CONTRIBUTING.md) e o [código de conduta](CODE_OF_CONDUCT.md).",
    "languages_extra": "",
    "body": {
      "overview": r"""* **Duas placas, um só firmware:** a Waveshare ESP32-S3-ETH (Ethernet, a predefinida) e um ESP32-S3-WROOM-1 N16R8 sem Ethernet (só Wi-Fi: a sua configuração pede a rede Wi-Fi a que se juntar e mantém sempre a sua própria rede). A imagem escolhe-se ao compilar (`tools/build_node.sh generic s3-eth` ou `generic s3-wifi`); a tabela de pinos e a forma de entrada seguem a placa, o painel oculta o que a placa não tem, e uma imagem só serve para a sua própria placa. Ambas compilam e estão testadas em anfitrião; nenhuma correu numa placa.
* **Um nó cobre até 270 graus:** cada Waveshare ESP32-S3-ETH lê até três radares LD2450 nas suas três UART, montados a 75 graus de distância, por Ethernet com fio (W5500) com DHCP ou um endereço fixo, alimentado por PoE ou USB. O *Adicionar um nó de 270°* do Studio cria os três radares já ligados ao nó.
* **Um painel web em cada nó,** com o aspeto do Studio e os seus idiomas, embutido no firmware: resumo, rede, Wi-Fi, broker, radares, pinos, utilizadores, atualização de firmware e registo. Um nó sem utilizador abre o Wi-Fi `ARMOR-SETUP-xxxxxx` e cria o seu primeiro administrador com um código de configuração; as palavras-passe são PBKDF2 com sal, as sessões são tokens aleatórios, e cada definição vive na flash do nó, por isso uma imagem serve todos os nós e nenhuma palavra-passe está compilada ([o painel](docs/NODE_PANEL.md)).
* **Um só Wi-Fi a partir de vários nós:** cada nó pode oferecer um ponto de acesso ligado à sua porta Ethernet; dê aos nós o mesmo nome e palavra-passe e o canal em automático (1, 6 ou 11 pelo MAC) e os telemóveis e sensores Wi-Fi veem uma só rede com um só servidor DHCP. Não é uma malha de rádio: cada nó mantém o seu cabo. Um nó pode, em vez disso, juntar-se ao Wi-Fi de um router (com uma pesquisa de redes), e um sem cabo pode configurar-se por **Bluetooth** a partir da aplicação Android.
* **Pinos para o servidor:** qualquer pino livre torna-se uma entrada, uma saída (com um estado seguro quando se perde o broker), PWM ou uma leitura analógica, e aparece como um dispositivo do servidor, por isso um relé ou um contacto não precisa de firmware novo. Os pinos reservados da placa nunca se oferecem.
* **Atualizações pelo ar com retrocesso** a partir do painel (duas ranhuras na flash de 16 MB), e uma **ligação do Studio** ao painel de cada nó, a partir do endereço que o nó publica.
* **O painel sobre HTTPS:** o nó faz o seu próprio certificado (autoassinado, guardado na flash) e serve o painel na porta 443 além da 80, ou só na 443; o cookie de sessão fica marcado como Secure e a impressão digital do certificado mostra-se para comparar com o aviso do navegador.
* **Identidades de rasto estáveis:** os alvos de cada trama associam-se aos seguidos antes, de modo que uma pessoa mantém o mesmo id de rasto, uma trama perdida não cintila e as posições suavizam-se um pouco.
* **Seis modelos de sensor, um por porta:** uma porta leva um LD2450 ou um LD2461 (seguidores que alimentam o perímetro, com o campo próprio do modelo no Studio) ou um sensor de presença (LD2410, LD2412, LD2410S, MR24HPC1) que se torna um dispositivo do servidor e publica presença e distância. Escolhido no painel; o que cada um é, o seu protocolo e o que não foi verificado estão em `docs/SENSORS.md`.
* **Descodificador, saúde e configuração do LD2450:** um enquadrador que ressincroniza encontra tramas num fluxo ruidoso; cada trama de 30 bytes dá até três alvos que se tornam rastos do contrato; a consola e o painel dizem por radar se reporta, está em silêncio ou ilegível. O painel também pode ler a versão do módulo, escolher um ou três alvos e definir zonas de deteção (um protocolo não verificado contra um módulo).
* **Luz ambiente e mensagens exatas ao contrato:** o VEML7700 com gama automática; JSON de telemetria, saúde e informação que seguem os esquemas publicados e recusam escrever o que for inválido, com instantes de relógio de parede (SNTP) e uma última vontade MQTT. A telemetria retém-se enquanto nenhum radar reporta, nunca um «tudo em ordem» vazio.
* **Uma imagem para todas as placas, como um produto de rede:** o firmware é o mesmo e o MAC distingue as placas (`armor-` e seis dígitos até lhes darem nome); `adopt_node.py` dá a um nó acabado de gravar o seu administrador, a sua identidade no broker e as definições partilhadas da frota pela rede, com um código de configuração calculado a partir do seu MAC, por isso 5 nós ou 27 dão o mesmo trabalho.
* **Ferramentas de bancada:** gravação por USB-C, um nó substituto para trabalhar no painel, e um conversor de um registo de tramas em bruto para um ficheiro de teste ([arranque de bancada](docs/BENCH_BRINGUP.md)).
* **Atualizações pelo ar assinadas:** o nó só instala do GitHub uma imagem cujo SHA-256 coincide e que leva uma assinatura Ed25519 válida do responsável (a chave pública está no firmware, a privada nunca sai do responsável); um ficheiro carregado à mão por um administrador no painel continua a ser aceite. As páginas e mensagens do painel estão em oito idiomas.
* **Emparelhamento Bluetooth com PIN:** o PIN de seis dígitos deriva do código de configuração, é impresso na consola USB e mostrado a um administrador no painel; o telemóvel tem de o introduzir antes de poder escrever as definições do nó.
* **Só a casa pode usar o painel:** o painel responde por omissão à rede privada (ou às redes que o dono indicar, como uma VPN), recusa uma lista que deixaria de fora quem a guarda, conta as palavras-passe erradas por pessoa e por endereço e funciona atrás do proxy do servidor para ser alcançado de fora de casa sem publicar o nó.
* **Ligação cifrada opcional ao broker (TLS):** desativada por predefinição, por isso o nó fala MQTT sem cifra como antes. Um interruptor e uma caixa para o certificado da autoridade própria da instalação (PEM, no máximo 2 KB) na página Broker fazem-no ligar-se com `mqtts://`, confiar só nessa autoridade e verificar que o certificado do broker foi feito para o endereço alcançado; o que não for um único certificado PEM é recusado. Coberto por testes no computador; o handshake ainda não foi executado numa placa.
* **Relatório de saúde:** cerca de uma vez por minuto o nó publica há quanto tempo está ligado e porque reiniciou da última vez, a memória livre, a ligação e o sinal Wi-Fi, quantas vezes se ligou ao broker e o último erro que registou (`armor/health/<nó>`, o contrato `node_health` do ARMOR-COMMON). O código que o constrói é partilhado por todos os nós e testado num computador; nunca correu numa placa.
* **Controlo a partir do servidor:** o Studio pode reiniciar o nó de forma limpa, pô-lo em pausa até uma hora (retoma sozinho), pôr o seu trabalho em espera (sem fim, mantida nos reinícios, o nó continua ligado e a responder), fazê-lo mostrar-se, pedir um instantâneo de diagnóstico e marcá-lo em manutenção (`armor/control/<nó>/...`, o contrato `node_control` do ARMOR-COMMON). Cada ordem tem dois passos com um token de uso único que pertence a essa operação, só o servidor as pode escrever no broker, e não existe reposição de fábrica, apagamento nem sono profundo. Enquanto o nó está em pausa ou em espera, não publica alvos nem presença (o batimento continua a dizer que está lá). O código é partilhado por todos os nós e testado num computador; ainda não correu numa placa.
* **Um motor de perímetro no nó (desligado por predefinição):** seis zonas de deteção e três de exclusão, cada uma um retângulo que pode ser rodado por um ângulo, três linhas de passagem que contam as travessias por sentido, três percursos de entrada, imunidade a animais e deteção de ocultação. Funciona junto dos sensores, por isso continua a funcionar sem acesso ao broker, guarda os seus eventos enquanto o broker está ausente e publica-os em `armor/radar/<nó>/events`; o editor de zonas está no painel do nó. Nada disto foi ainda experimentado com um sensor numa placa.
* **Quem é cada sensor, e o seu Bluetooth próprio fechado:** ao arrancar, o nó lê a versão de firmware e o endereço Bluetooth de cada sensor, fecha por predefinição o Bluetooth próprio dos sensores (não pede PIN) e pode ceder a linha série de um sensor à ferramenta de PC de um administrador durante alguns minutos (uma ponte série transparente). `GET /metrics` para administradores e uma exportação e importação de tudo ou nada das definições completam o conjunto.
* **Diagnóstico sem cabo:** depois de um arranque que não foi limpo (um bloqueio, um watchdog, uma quebra de alimentação, uma reserva de memória falhada), o relatório de saúde diz o motivo durante dez minutos; uma falha deixa o seu core dump para ver, descarregar ou apagar a partir do painel; as definições guardadas são copiadas antes de cada instalação de firmware e recuperadas se uma atualização as danificar; e um administrador pode pedir ao nó, através do servidor, um pacote de diagnóstico ou o seu registo com um token de utilização única.
* **Adoção por HTTPS com impressão digital fixada:** `tools/adopt_node.py` aceita `https://<endereço>` com `--fingerprint` (o SHA-256 do certificado do nó, verificado na própria ligação que leva o pedido) ou `--show-fingerprint` para a ler; avisa do HTTP em claro e de um ficheiro de frota com IP fixo ou nome de anfitrião, e o painel também avisa ao importar um ficheiro assim.
* **O leitor de sensores espera por eventos em vez de sondar:** a tarefa de leitura dorme nas filas de eventos das linhas série e esvazia tudo o que chegou, esvazia a linha se houve excesso e conta excessos e erros por linha; `system.reader_idle_ms` (100; 0 = a sondagem de 10 ms de antes) fixa a espera, e se uma fila falhar volta sozinha à sondagem.
* **Selagem opcional dos segredos guardados:** desativada por predefinição (`security.seal_secrets`, ou `nodes.nvs_encryption` do servidor). Ativada, as palavras-passe, os tokens, as chaves, os PIN e os hashes de palavras-passe que o nó guarda ficam selados com ChaCha20-Poly1305 e tudo o resto continua legível; ativá-la ou desativá-la reescreve-os sem perder nada, mesmo que o nó pare a meio. Não se queima nenhum eFuse nem se cifra a flash: a chave está numa partição do mesmo chip, pelo que **não** protege contra quem tenha a placa, e um nó instalado antes dessa partição mantém os segredos como estavam até ser gravado com a nova tabela de partições.""",
      "role": r"""O ARMOR-NODE-RADAR são os olhos do perímetro. Cada nó lê até três radares ou sensores de presença e publica pistas, luz e saúde para o [ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER) por MQTT; o [ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) desenha-os na planta do local e o [ARMOR-SERVER-AI](https://github.com/JuanenRac/ARMOR-SERVER-AI) pesa-os face às câmaras. O seu firmware partilha uma base com os outros nós (o painel, a configuração por Bluetooth, as atualizações assinadas, o acesso e o relógio vêm da base de firmware do [ARMOR-COMMON](https://github.com/JuanenRac/ARMOR-COMMON)), por isso o que se aprende num nó vale em todos.

| Nome | Como | Para quê |
|---|---|---|
| ARMOR-SERVER | MQTT `armor/node/<id>/telemetry|health|info|command` | Recebe as mensagens do radar (hoje a bancada CM5) e comanda o nó |
| ARMOR-STUDIO | ligação ao painel | Abre o painel do nó a partir do endereço que o nó publica |
| ARMOR-ANDROID-CONTROL | Bluetooth | Configura o nó no terreno |
| ARMOR-COMMON | contratos, base de firmware | As mensagens são verificadas com os seus esquemas; o firmware comum é copiado dele |""",
      "architecture": r"""<p align="center">
  <img src="images/architecture.svg" alt="Arquitetura de ARMOR-NODE-RADAR: quem o chama, o que contém e de que depende" width="100%">
</p>""",
      "security": r"""| Ameaça | Defesa |
|---|---|
| Palavras-passe em claro ou compiladas | PBKDF2-HMAC-SHA256 com 10 000 rondas; nenhuma palavra-passe no firmware (um nó sem utilizador entra em configuração); no máximo 4 utilizadores (admin ou visualizador) e de 8 a 64 caracteres; no máximo 6 sessões, 30 minutos de inatividade |
| Tomar um nó acabado de gravar | A configuração exige um código de arranque: o da compilação (`CONFIG_ARMOR_SETUP_CODE`) ou um aleatório guardado na flash e mostrado na consola USB; com segredo de frota é `HMAC-SHA256(segredo, MAC)`; é também a chave do Wi-Fi de configuração (WPA2, nunca em ponte) |
| O painel alcançado a partir da internet | Responde por omissão às redes privadas de uma casa (10/8, 172.16/12, 192.168/16, 169.254/16, 127/8 e 100.64/10 onde vivem algumas VPN); a definição `web.admin_sources` lista outros endereços e redes IPv4 (8 entradas, 120 caracteres); tudo o que está fora é recusado exceto a identidade pública `GET /api/v1/session`; uma lista que deixaria de fora quem a guarda é rejeitada |
| O painel em claro por HTTP | HTTPS no 443 com um certificado que o nó cria sozinho (autoassinado, na flash, impressão digital SHA-256 visível para comparar); o painel pode ser http, https ou ambos; o cookie de sessão é sempre HttpOnly e SameSite=Strict (e Secure por TLS) |
| Um firmware falso do GitHub | Uma imagem só se instala com um SHA-256 coincidente e uma assinatura Ed25519 válida feita com a chave do mantenedor (`no_checksum`, `no_signature`, `bad_signature`, `checksum_mismatch`, `wrong_firmware`, `not_newer`, `version_mismatch` recusam-na); um envio manual por um administrador não é verificado: um limite explícito |
| Sequestro da configuração Bluetooth | Um PIN de 6 dígitos derivado do código de configuração, visível na consola USB e ao administrador; o telemóvel tem de o introduzir antes de escrever definições; a janela dura `CONFIG_ARMOR_BLE_SETUP_MINUTES` (10 por omissão, de 1 a 120) |
| Uma ordem remota que faz mal | Dois passos com um token de uso único ligado a essa operação; só o servidor pode escrever esses tópicos no broker; uma pausa dura uma hora no máximo; não há reposição de fábrica, apagamento nem sono profundo por ordem remota |
| Segredos guardados lidos por quem tem a placa | Opcional (desligado por omissão, interruptor `security.seal_secrets` ou `nodes.nvs_encryption` do servidor): ChaCha20-Poly1305 para palavras-passe, tokens, chaves, PIN e hashes. Não cifra a flash nem queima um eFuse: a chave está numa partição do mesmo chip, por isso não protege contra quem tem a placa |
| A ligação ao broker em claro | TLS opcional (`mqtts://`) com a autoridade própria do dono (PEM até 2 KB) e verificação do nome; desligado por omissão. O handshake só correu em testes de anfitrião, não numa placa |
| O Bluetooth próprio de um sensor | Por omissão o nó fecha o Bluetooth de cada sensor LD (sem PIN); uma ponte série transparente para um computador só se abre por alguns minutos e por um administrador |
| Adotar um nó numa rede não fiável | `tools/adopt_node.py https://<endereço> --fingerprint <SHA-256>` verifica o certificado na mesma ligação; avisa sobre o HTTP simples e sobre ficheiros de frota com endereço fixo |
| Um pino perigoso | Os pinos reservados da placa nunca são oferecidos; uma saída tem estado seguro se o broker se perder; duas funções não podem partilhar um pino (verificado) |
| Um firmware público com segredo de frota | `CONFIG_ARMOR_FLEET_SECRET` está vazio por omissão: a compilação pública não leva segredo |

Leia [SECURITY.md](SECURITY.md) para comunicar uma vulnerabilidade. Não houve revisão independente.""",
      "interfaces": r"""| Parte | O que define |
|---|---|
| MQTT | `armor/node/<id>/{telemetry,health,info,command}`, `armor/health/<id>` (o seu testamento é `{"node_id":"..","online":false}`), `armor/control/<id>/{command,result,maintenance}` e `armor/control/all/command`, `armor/device/<id>/<pin>/{state,set}`, `armor/radar/<id>/events`, `armor/radar/<id>/control/armed` |
| Painel (HTTP 80, HTTPS 443) | Rotas `session`, `login`, `logout`, `setup`, `status`, `config` (+ export, import), `wifi/scan`, `time`, `radars` (+ command), `perimeter` (+ armed, learn, zone), `pins` (+ command), `bridge` (+ open, close, io), `ota` (+ check, install, progress, copy, switch), `account`, `ble-pin`, `log`, `coredump`, `factory-reset`, `reboot`; `/metrics` para administradores e o WebSocket `/ws/radar-map`; `tests/check_routes.py` verifica que toda a rota que o painel chama existe |
| Textos do painel | 76 códigos de erro com texto em oito línguas (832 linhas em `panel/text.js`), verificados por `tests/check_panel_text.py` |
| Hardware | 3 UART para LD2450, LD2461, LD2410, LD2412, LD2410S e MR24HPC1 (RX 16, 17, 18; TX 15, 21, 38); W5500 por SPI (MOSI 11, MISO 12, SCLK 13, CS 14, INT 10, RST 9, 20 MHz); VEML7700 em I2C (GPIO 1 e 2); botão BOOT |""",
      "configuration": r"""| Variável | Predefinição | O que define |
|---|---|---|
| `CONFIG_ARMOR_NODE_ID` | `""` | O nome; vazio dá `armor-` e os três últimos bytes do MAC |
| `CONFIG_ARMOR_SETUP_CODE`, `CONFIG_ARMOR_FLEET_SECRET` | `""` | O código de configuração da compilação (vazio: aleatório) e o segredo de frota (16+ caracteres; nunca no repositório) |
| `CONFIG_ARMOR_RADAR_COUNT` | 3 (0-3) | Quantos radares estão ligados |
| `CONFIG_ARMOR_TRACK_STABILISER` | y | Manter a identidade de uma pista de imagem para imagem |
| `CONFIG_ARMOR_MQTT_URI`, `_USERNAME`, `_PASSWORD` | `""` | As primeiras definições do broker (alteráveis no painel) |
| `CONFIG_ARMOR_HEARTBEAT_S` | 10 (2-300) | Segundos entre batimentos de saúde |
| `CONFIG_ARMOR_TELEMETRY_PERIOD_MS` | 200 (200-5000) | No máximo 5 mensagens por segundo |
| `CONFIG_ARMOR_BLE_SETUP_MINUTES` | 10 (1-120) | Quanto tempo a configuração Bluetooth fica aberta |
| `CONFIG_ARMOR_BOARD_S3_ETH` / `_S3_WIFI` | eth | A placa: Waveshare ESP32-S3-ETH ou ESP32-S3-WROOM-1 N16R8 (só Wi-Fi) |
| `CONFIG_ARMOR_BOOT_FACTORY_RESET` | y | Mantenha BOOT 8 s nos primeiros 30 s para recomeçar |
| `system.login_limit_per_minute` | 30 (0-120) | Palavras-passe erradas por minuto antes de o painel bloquear o início de sessão a todos (0 = sem limite global); lê-se e altera-se no Studio (um botão em cada nó) ou com `POST /api/v1/admin/nodes/settings`, onde o acesso ao painel é usado uma vez e nunca guardado |

As definições afinadas em direto estão no painel e guardam-se na flash (por exemplo `system.reader_idle_ms`, `security.seal_secrets`, o limite de falhas de início de sessão por minuto (30, de 0 a 120) e as zonas do motor de perímetro); os valores por omissão do firmware estão em `sdkconfig.defaults` e `sdkconfig.board.*`. A flash de 16 MB contém `nvs` (64 KB), `otadata`, `phy_init`, duas ranhuras de 3 MB `ota_0` e `ota_1`, `coredump` (128 KB) e `nvs_keys` (4 KB) (`partitions.csv`).""",
      "quickstart": r"""**Requisitos:** um compilador C++17 para os testes de anfitrião; o contentor ESP-IDF 5.5.5 para compilar a imagem; uma Waveshare ESP32-S3-ETH ou uma ESP32-S3-WROOM-1 N16R8.

```bash
cmake -S tests -B build/host && cmake --build build/host && ctest --test-dir build/host   # host tests, -Werror
node tools/panel_mock.mjs --user admin:adminpass123   # the panel without a board
python tools/make_fleet.py                             # once: the fleet secret and the shared settings
tools/build_node.sh generic                           # ONE image for every Waveshare board (dist/generic-s3-eth.bin), in the ESP-IDF container
tools/build_node.sh generic s3-wifi                   # the same firmware for an ESP32-S3-WROOM-1 N16R8 with no Ethernet
```

```bat
tools\flash.bat generic COM5 monitor                  # each Waveshare board, once, by USB-C (add s3-wifi for the other board)
```

```bash
tools/adopt_node.py 192.168.0.181 --id perimetro-3 --fleet secrets/fleet.json --broker-ssh-host <cm5> --broker-ssh-user <user>
```

Os testes de anfitrião precisam de qualquer compilador C++17 (Linux, WSL, MSYS2). Veja o [arranque de bancada](docs/BENCH_BRINGUP.md), o [painel](docs/NODE_PANEL.md) e a [fronteira de hardware](docs/HARDWARE_BOUNDARY.md).""",
      "testing": r"""```bash
cmake -S tests -B build/host && cmake --build build/host && ctest --test-dir build/host
build/host/emit_samples | python tests/check_contract.py
python -I tools/armor_ci_validate.py
```

14 programas de teste de anfitrião e 6 verificações Python correm com `ctest`; 7371 verificações contadas pelos programas de anfitrião, compiladas com `-Werror`.

| Parte | O que cobre |
|---|---|
| `test_core`, `test_sensors`, `test_family`, `test_uart_wake` | Os descodificadores (LD2450, LD2461, quatro sensores de presença), o delimitador de tramas, o canal de comandos, as famílias de sensores e o despertar da UART |
| `test_node`, `test_base`, `test_shared`, `test_board_wifi` | As definições e as suas verificações, a tabela de pinos, utilizadores e sessões, o plano de rede, a base partilhada e a placa Wi-Fi |
| `test_logic`, `test_perimeter`, `test_control`, `test_diag` | A lógica dos pinos, o motor de perímetro, as ordens de controlo em dois passos e o diagnóstico |
| `test_mqtt_tls`, `test_release` | A ligação TLS ao broker (só anfitrião) e as verificações de versão e assinatura |
| `check_panel_text`, `check_task_safety`, `check_save_paths`, `check_ble_session`, `check_routes`, `check_bridge_client` | Python: os textos do painel em oito línguas (832 linhas), as tarefas, os caminhos de gravação, a sessão Bluetooth sob o seu bloqueio, as rotas e o cliente da ponte série |

O painel web também é exercitado num navegador real contra um nó de substituição (`tools/panel_mock.mjs`). Os descodificadores LD2461 e de presença só coincidem com os exemplos dos seus manuais.""",
      "build": "`tools/build_node.sh generic` compila UMA imagem para cada placa Waveshare no contentor ESP-IDF 5.5.5, e `tools/flash.bat` grava-a por USB-C; o mesmo firmware compila-se para a placa só Wi-Fi com `s3-wifi`. As versões levam a imagem, o seu SHA-256 e a sua assinatura Ed25519, uma por placa.",
      "troubleshooting": r"""| Vê | Porque | Faça |
|---|---|---|
| Perdeu a palavra-passe ou o nó já não se liga à rede | Um nó em configuração e sem endereço após 90 s abre o seu próprio Wi-Fi `ARMOR-SETUP-xxxxxx` (abra `http://192.168.4.1/`) | Para recomeçar mantenha BOOT 8 segundos nos primeiros 30 segundos após ligar (apaga definições e utilizadores), ou use *Reposição de fábrica* no painel |
| Uma atualização do GitHub é recusada | A versão não traz soma de verificação nem assinatura, não coincidem (`e_no_checksum`, `e_no_signature`, `e_checksum_mismatch`, `e_bad_signature`), não traz imagem para esta placa (`e_no_asset_for_board`) ou é de outro projeto (`e_wrong_firmware`) | O nó não mudou; tente de novo ou deixe um administrador enviar o ficheiro à mão |
| Os comandos ao radar respondem `no_answer`, `refused` ou `disabled` | O fio TX do radar não está ligado, o módulo bloqueou ou o nó fecha primeiro o seu Bluetooth | Verifique a cablagem (veja o arranque em bancada), reinicie o módulo no painel |
| O nó não mostra o sensor 3 ou deixa um radar a dormir | O módulo deixou de falar (silêncio sem tramas más) | Use *reiniciar módulo* na página de radares e depois feche o Bluetooth do próprio sensor |""",
      "structure": r"""<p align="center">
  <img src="images/repository-structure.svg" alt="Estrutura do repositório de ARMOR-NODE-RADAR" width="100%">
</p>

<details>
<summary>Versão em texto da árvore</summary>

```text
ARMOR-NODE-RADAR/
├── main/                                o firmware: um componente ESP-IDF
├── panel/                               o painel web embebido no firmware
├── tests/                               testes de anfitrião e verificações Python
├── docs/                                7 guias da bancada e do painel
├── tools/                               ferramentas de compilação, gravação, adoção, frota e verificação
├── .github/                             fluxo de CI e modelos de issues e pull requests
├── images/                              faixa, ícone e as duas imagens deste README
├── build.sh build.bat                   compilar pelo fluxo de projeto partilhado
├── test.sh test.bat                     executar os testes pelo fluxo partilhado
├── run.sh run.bat                       arrancar pelo fluxo de projeto partilhado
├── armor.project.json                   manifesto: versão, função, maturidade, comando de build
├── CHANGELOG.md                         o que mudou em cada versão
├── SECURITY.md SUPPORT.md LICENSE       política de segurança, apoio e licença
├── CONTRIBUTING.md CODE_OF_CONDUCT.md   como contribuir e o código de conduta
├── CMakeLists.txt                       o projeto ESP-IDF
├── partitions.csv                       a tabela da flash
├── sdkconfig.defaults                   as definições do firmware
├── sdkconfig.board.s3-eth               a placa Ethernet
├── sdkconfig.board.s3-wifi              a placa Wi-Fi
├── secrets/                             exemplos de ficheiros de frota e nó
├── build-test.sh build-test.bat         executar os testes pelo fluxo partilhado
└── .gitattributes .gitignore            definições do Git
```

</details>""",
      "roadmap": r"""**Limites conhecidos hoje**

* Os descodificadores LD2461 e de presença só coincidem com os exemplos dos seus manuais, sem módulo atrás; o canal de comandos só foi verificado com o LD2450.
* A verificação da assinatura das atualizações e o emparelhamento Bluetooth com PIN estão provados num computador com assinaturas reais mas ainda não na placa; o handshake TLS com o broker não correu numa placa.
* O relatório de saúde e o controlo a partir do servidor não correram na placa; o motor de perímetro nunca correu com um sensor; o certificado HTTPS próprio do painel não foi experimentado em todos os navegadores; a placa Wi-Fi não existe fisicamente (só existe a Ethernet).

**A seguir**

* Correr o motor de perímetro, o relatório de saúde e as ordens de controlo com sensores reais e a bancada CM5; experimentar a ligação TLS ao broker e a atualização assinada na placa.""",
    },
  },
}
