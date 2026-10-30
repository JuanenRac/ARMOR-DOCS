# The facts that do not depend on the language, and the words of every language, of ARMOR-NODE-SOLAR, in the universal README layout.
# Copyright (C) 2026 JuanenRac (Electro Hobby 3D). GPL-3.0-or-later.

FACTS = {
  "emoji": "☀️",
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
      "red",
    ],
    [
      "security",
      "yellow",
    ],
    [
      "updates",
      "orange",
    ],
    [
      "writing",
      "orange",
    ],
    [
      "integration",
      "orange",
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
      "Devices",
      "Voltronic%20%C2%B7%20Pylontech",
      "ffb020",
    ],
    [
      "Tests",
      "11824%20checks",
      "2ea44f",
    ],
  ],
}

TEXT = {
  "en": {
    "tagline": "Solar gateway node: reads inverters and batteries through up to ten serial ports (ESP32-S3 firmware, its web panel and the protocol library)",
    "honest": "The firmware builds in the ESP-IDF 5.5.5 container, its core (the settings, the exchange with each kind of equipment, the arithmetic of the emulated UART, the Bluetooth channel, the release and signature checks: 11,824 checks in 18 test programs) is tested on a computer with stand-in equipment, the messages it makes are accepted by ARMOR-COMMON and the panel was exercised in a browser against a stand-in node. **It has never run on a board and no inverter or battery has been connected**: the Wi-Fi, the panel over TLS, the update, the hardware and emulated UARTs and the formats of the protocols (written from public documents and from memory) are untried. The ANT-BMS frames in its tests were captured by other people on their own units: this project has not read one itself.",
    "glance": [
      [
        "Role",
        "Solar field node for ESP32-S3: inverters and batteries (family: Field Nodes, parent: ARMOR-COMMON)",
      ],
      [
        "Stack",
        "C++17, ESP-IDF 5.5.5, ESP32-S3",
      ],
      [
        "Tests",
        "11824 checks in 18 host programs and 6 Python checks (`ctest`)",
      ],
      [
        "Equipment",
        "Voltronic / MPP Solar inverters, Pylontech batteries, ANT-BMS; 10 serial ports",
      ],
      [
        "Runs on",
        "ESP32-S3-WROOM-1 N16R8 or Waveshare ESP32-S3-ETH; host tests on any computer",
      ],
      [
        "On real hardware",
        "None yet: no board built and no inverter or battery connected (host tests, the build and the panel in a browser only)",
      ],
      [
        "License",
        "GPL-3.0-or-later",
      ],
    ],
    "status": {
      "software": "The firmware builds in the ESP-IDF 5.5.5 container for both boards (Wi-Fi and Ethernet).",
      "tests": "11,824 checks in 18 host programs pass (`ctest`): the settings, the exchange with each kind of equipment, the emulated UART, the Bluetooth channel and the release checks.",
      "protocols": "The Voltronic, Pylontech and ANT-BMS frames, checksums and readings are checked against the documented frames and recorded samples; none has talked to a real inverter or battery yet.",
      "ui": "The web panel is exercised in a browser against a mock of the node, not on a board.",
      "hardware": "No board built and no inverter or battery connected: nothing has run on real equipment yet.",
      "security": "The set-up code, the login with a limit on wrong passwords, the Bluetooth PIN and the signed updates are tested on the host; there has been no independent review.",
      "updates": "The hash and Ed25519 signature checks and the rollback logic pass on the host; an update over the air has never been run on a board.",
      "writing": "Writing to Pylontech batteries is off by default and has only been tested against a simulator.",
      "integration": "The messages of the node are validated against the shared schemas and conformance vectors of ARMOR-COMMON. Its MQTT client is played against a real Mosquitto in the tests; no board has sent them to a server yet.",
      "docs": "Eight languages, the firmware guide, the wiring notes and the changelog are up to date.",
    },
    "docs": [
      "[Node firmware](docs/NODE_FIRMWARE.md): the board, the ports, the first start and the bench checklist",
      "[Wiring](docs/NODE_HARDWARE.md), [protocols](docs/PROTOCOLS.md) and [messages](docs/SOLAR_MESSAGES.md)",
      "[Battery maintenance](docs/BATTERY_MAINTENANCE.md) and its [bench test plan](docs/BATTERY_BENCH_TEST_PLAN.md)",
      "[Studio menus](docs/STUDIO_MENUS.md), [bench tests](docs/BENCH_TESTS.md), [set-up code](docs/SETUP_CODE.md) and [Bluetooth provisioning](docs/BLE_PROVISIONING.md)",
    ],
    "contributing_first": "Before a pull request run `ctest --test-dir build/host` and `python -I tools/armor_ci_validate.py`: it must pass. See [CONTRIBUTING.md](CONTRIBUTING.md) and the [code of conduct](CODE_OF_CONDUCT.md).",
    "languages_extra": "",
    "body": {
      "overview": r"""* **Two boards, one firmware:** an ESP32-S3-WROOM-1 N16R8 on Wi-Fi (the default) and the Waveshare ESP32-S3-ETH on its Ethernet cable (DHCP or a fixed address; its own Wi-Fi network is kept to reach it from a phone). The image is chosen when it is built (`tools/build_node.sh generic s3-wifi` or `generic s3-eth`); the pin table, the default pins of the ports and the way in follow the board, and an image is only for its own board. Both build and are host-tested; neither has run on a board.
* **The firmware of the node** (ESP32-S3-WROOM-1 N16R8 on Wi-Fi, or the Waveshare ESP32-S3-ETH on its cable): ten serial ports, three hardware UARTs and seven emulated ones (up to 19200 baud), each independent and each reading an inverter, a battery or a raw monitor, so a node may read only inverters, only batteries or a mix.
* **The node's web panel,** the radar nodes' too: set-up with a code shown on the USB console, login and users, Wi-Fi (station and access point), broker, update over the air with rollback, log, HTTPS, and the pages of the ports (with what each one hears, for protocols not decoded yet) and of the readings, in eight languages.
* **Voltronic / MPP Solar inverters** (Axpert, PIP, InfiniSolar and clones), RS232 at 2400 baud: the frames and their CRC, and the readings `QPIGS` (grid, output, battery, PV, status bits), `QMOD` (mode), `QPIWS` (warnings and faults by name) and `QPIRI` (ratings). Only reading commands can be built: a setting changes how the house is fed. Three dialects, chosen on the port or found by it (*auto*): PI30, REVO (another `QPIGS`, checksum replies) and PI18 (`^P005GS`: InfiniSolar V, LV5048, SunGoldPower), read only.
* **Pylontech batteries** (US2000, US3000, US5000): the console's `pwr` table (every module's voltage, current, temperatures and state of charge), `bat <n>` (the voltage and temperature of every cell) and `info <n>` (model, remaining and full capacity, cycles), summarised as one stack with its total capacity and energy, and the RS485 frame with its two checks. The formats are written from memory of the public console and may differ between firmwares. The columns are found by the header's names (the US5000 V2.3 layout with its Id columns, MosTempr and SysAlarm.St included), the remaining charge and the balancing come from `bat`, and the model, rated capacity and cycles from `info` and `stat`, asked once and kept for half an hour.
* **What a Pylontech module tells about itself:** its model and the versions of its board and software, its cells and the current it allows, the counters of its life (`stat`), the health of each cell (`soh`, the abnormal one marked) and the newest entry of its event log, with the protection names exactly as the console prints them. The console only reads, and an administrator can download what a port heard as a text file.
* **The messages of the node** (`armor/solar/<node>/<device>/state`, one per inverter or battery stack), defined in ARMOR-COMMON with schemas and conformance vectors; what the ports make is checked against them.
* **ANT-BMS batteries** (the black boards of home-made packs, 7S to 32S), 3.3 V UART at 19200 baud: both protocols of its firmware (the node asks in one and then in the other and keeps to the one that answers), with the cells, temperatures, state of charge, current, capacities and the states of the MOSFETs and the balancer, checked against frames captured on four real models. Reading only: its write commands can disconnect a battery under load. A button on the ports page also reads the BMS's model, version and 56 protection and balancing settings (newer protocol), read only.
* **Configuration from a phone over Bluetooth,** the same channel as the radar node's: the ARMOR app finds the node as `ARMOR-XXXXXX` and sets its name, Wi-Fi, address, broker and Bluetooth mode with the panel's users and set-up code ([the protocol](docs/BLE_PROVISIONING.md)). It listens only while the node has no user, unless told otherwise. The radio side has never run on a board.
* **The base board with multiplexers (the *mux* profile):** three hardware UARTs, each behind a 74HC4052, serve up to eight ports in groups of 4, 2 and 2 that take turns on their line, each port with its own speed and polarity, and one LED per port through a 74HC595; the cells of a tall Pylontech stack can be read in rotation. For an inverter in the standard dialect, the **second PV input** (`QPIGS2`) and the **units of a parallel system** (`QPGS`) are optional readings. None of it has run on a board.
* **Signed over-the-air updates:** the node installs from GitHub only an image whose SHA-256 matches and that carries a valid Ed25519 signature of the maintainer (the public key is in the firmware, the private one never leaves the maintainer); a file uploaded by hand by an administrator in the panel is still accepted. The pages and messages of the panel are in eight languages.
* **Bluetooth pairing with a PIN:** the six-digit PIN is derived from the set-up code, printed on the USB console and shown to an administrator in the panel; the phone has to enter it before it may write the node's settings.
* **Not yet:** the ANT-BMS's Bluetooth link (the node uses the cable, the more stable of the two) and a run on a real board with real equipment.
* **Only the house may use the panel:** the panel answers the private network by default (or the networks its owner lists, such as a VPN), refuses a list that would lock out whoever saves it, counts wrong passwords for each person as well as each address, and works behind the server's proxy so that it can be reached from outside the house without publishing the node.
* **Unknown is not none:** a REVO inverter has no warning query, so its message carries `warnings_known: false` and Studio shows the warnings as unknown instead of "none".
* **Optional encrypted link to the broker (TLS):** off by default, so the node talks plain MQTT as before. A switch and a box for the certificate of the installation's own authority (PEM, at most 2 KB) in the Broker page make it connect with `mqtts://`, trust that authority only and check that the broker's certificate was made for the address it reached; anything that is not one PEM certificate is refused. Covered by host tests; the handshake has not been run on a board yet.
* **Health report:** about once a minute the node publishes how long it has been up and why it last restarted, its free memory, its link and Wi-Fi signal, how many times it connected to the broker and the last error it logged (`armor/health/<node>`, the `node_health` contract of ARMOR-COMMON). The code that builds it is shared by every node and tested on a computer; it has not run on a board.
* **Writing to Pylontech batteries (off by default):** typed operations only - clock, counters and logs, restart, capacity, the reset of the charge level, limits and protections, outputs, serial number, external memory, firmware by XMODEM-1K and an expert console with a block list - in two steps (arm, then execute with a one-time token), with the battery read before and after, the service password kept only in the node and a simulated console for the tests. Untried on a real battery: see the [bench test plan](docs/BATTERY_BENCH_TEST_PLAN.md).
* **Control from the server:** Studio can restart the node cleanly, pause it for up to an hour (it resumes by itself), put its work in standby (no end, kept across restarts, the node stays connected and keeps answering), make it show itself, ask for a diagnostics snapshot and mark it as in maintenance (`armor/control/<node>/...`, the `node_control` contract of ARMOR-COMMON). Every order takes two steps with a one-time token that belongs to that operation, only the server may write them on the broker, and there is no factory reset, no erase and no deep sleep. While the node is paused or in standby it writes no battery (a running operation can still be cancelled) and keeps reading the inverters and batteries. The code is shared by every node and tested on a computer; it has not run on a board.
* **Absurd values are named, not hidden:** when an inverter sends a number beyond what is possible, the node holds it at the contract's limit and names it in `clamped`, so the server shows it as not real; and the raw dump of a port is only made while the panel is looking at it.
* **Diagnostics without a cable:** after a start that was not clean (a crash, a watchdog, a sag of the supply, a failed allocation) the health report says why for ten minutes; a crash leaves its core dump to look at, download or erase from the panel; the stored settings are copied before every firmware install and recovered if an update damages them; and an administrator can ask the node, through the server, for a diagnostic package or its log with a one-time token.
* **Optional sealing of stored secrets:** off by default (`security.seal_secrets`, or the server's `nodes.nvs_encryption`). When on, the passwords, tokens, keys, PINs and password hashes the node stores are kept sealed with ChaCha20-Poly1305 and everything else stays readable; turning it on or off rewrites them with nothing lost, even if the node stops half-way. No eFuse is burned and the flash is not encrypted: the key lives in a partition of the same chip, so it does **not** protect against someone who holds the board, and a node installed before that partition existed keeps its secrets as they were until it is flashed with the new partition table.""",
      "role": r"""ARMOR-NODE-SOLAR is the gateway between the house's solar equipment and the family. It reads inverters and batteries through up to ten serial ports and publishes what it reads for [ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER), which keeps the history, the sums and the alarms; the *Inverters* and *Batteries* menus of [ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) and the Solar screen of [ARMOR-ANDROID-CONTROL](https://github.com/JuanenRac/ARMOR-ANDROID-CONTROL) show it. It only reads: it never writes a setting to any equipment.

| Name | How | What for |
|---|---|---|
| ARMOR-SERVER | MQTT `armor/solar/<node>/<device>/state` | Receives one message per inverter or battery stack; orders the maintenance of a battery |
| ARMOR-STUDIO | menus, panel link | Shows inverters and batteries and opens the node's panel |
| ARMOR-ANDROID-CONTROL | Bluetooth | Sets the node up in the field and shows the energy screens |
| ARMOR-COMMON | solar contract | The messages are checked against its schemas; the common firmware is copied from it |""",
      "architecture": r"""<p align="center">
  <img src="images/architecture.svg" alt="ARMOR-NODE-SOLAR architecture: who calls it, what it holds and what it depends on" width="100%">
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
| A battery written by mistake or by an attacker | Three locks: the node setting `battery.write_enabled` (administrators) with the battery's service password, the server's `ARMOR_BATTERY_WRITE=1`, and the broker's access list for `armor/solar/<node>/maintenance/command` and `.../result` |
| A repeated or stolen write order | Two steps (arm, then run with a single-use token), an arming window of 120 s, 30 s of cooldown between writes to a port, 3 failures in 10 minutes lock it for 5; the battery's serial number is typed again, the battery must be idle and without a critical alarm, and a firmware image is kept for 30 minutes and checked |
| Writing to an inverter or an ANT-BMS | The write commands of an inverter (a setting changes how the house is fed) and of an ANT-BMS (it can disconnect a battery under load) cannot even be built |
| Absurd numbers shown as real | A value beyond what is possible is held at the limit of the contract and named in `clamped`, so the server shows it as not real; a REVO inverter has no warning query, so its message says `warnings_known: false` instead of claiming no warnings |

No frame has been read from a real inverter or battery; the formats are written from public documents and from memory, and the ANT-BMS frames of the tests were captured by other people. Read [docs/BATTERY_MAINTENANCE.md](docs/BATTERY_MAINTENANCE.md) and [SECURITY.md](SECURITY.md).""",
      "interfaces": r"""| Part | What it sets |
|---|---|
| MQTT | `armor/solar/<node>/<device>/state` (one message per inverter or battery stack, kind `inverter` or `battery` of the ARMOR-COMMON contract), `armor/solar/<node>/maintenance/{command,result}`, `armor/health/<node>` (last will), `armor/control/<id>/{command,result,maintenance}` and `armor/control/all/command` |
| Ports | 10 serial ports (3 hardware UARTs and 7 emulated, up to 19200 baud when emulated); per port a type: `voltronic` (2400 baud, every 5 s), `pylontech` (115200, every 10 s), `ant` (19200, every 5 s) or `raw` (9600, listen only, publishes nothing); inverter dialects `auto`, `pi30`, `revo`, `pi18`; the mux profile has 3 groups of ports |
| Queries | Voltronic: `QPIGS`, `QMOD`, `QPIWS`, `QPIRI` (and `QPIGS2`, `QPGS` on a standard inverter with the mux); Pylontech console: `pwr`, `bat <n>`, `info <n>`, `stat`, `soh`, event log, up to 8 modules asked cell by cell |
| Panel | The family routes (`tests/check_routes.py` checks that every route the panel calls exists) plus the ports and readings pages; 51 error codes with a text in eight languages (772 rows in `panel/text.js`); see [docs/STUDIO_MENUS.md](docs/STUDIO_MENUS.md) for the menus of Studio |""",
      "configuration": r"""| Variable | Default | What it sets |
|---|---|---|
| `enabled`, `kind`, `name`, `baud`, `rx`, `tx`, `de`, `poll_s`, `modules`, `dialect` | - | The settings of each port: on or off, the type, the device name in the topic, the speed (0 = the type's own), the pins (and the DE/RE pin of an RS485), the polling period (0 = the type's own), the number of modules and the inverter dialect; at most 3 backup networks and 2 backup brokers |
| `battery.write_enabled` | off | The node's lock for writing to a Pylontech battery (administrators, with the battery's service password, which never leaves the node) |
| `CONFIG_ARMOR_BOARD_S3_WIFI` / `_S3_ETH` | wifi | The board: ESP32-S3-WROOM-1 N16R8 on Wi-Fi (the default) or the Waveshare ESP32-S3-ETH |
| `CONFIG_ARMOR_NODE_ID`, `_SETUP_CODE`, `_FLEET_SECRET`, `_MQTT_*`, `_HEARTBEAT_S`, `_BLE_SETUP_MINUTES`, `_BOOT_FACTORY_RESET` | - | The settings every node shares: the name (empty gives `armor-` and the last bytes of the MAC), the set-up code (empty: random), the fleet secret (16+ characters, never in the repository), the first broker settings, the heartbeat (2 to 300 s), the minutes of Bluetooth set-up (1 to 120) and the reset with BOOT (8 s in the first 30 s) |""",
      "quickstart": r"""**Requirements:** a C++17 compiler for the host tests; the ESP-IDF 5.5.5 container to build the image; an ESP32-S3-WROOM-1 N16R8 or a Waveshare ESP32-S3-ETH.

```bash
cmake -S tests -B build/host && cmake --build build/host && ctest --test-dir build/host   # host tests, -Werror
build/host/emit_poller_samples | python tests/check_samples.py   # what the ports make is accepted by ARMOR-COMMON
tools/build_node.sh generic                       # the image for the N16R8 board in the ESP-IDF container: dist/generic-s3-wifi.bin
tools/build_node.sh generic s3-eth               # the same firmware for the Waveshare ESP32-S3-ETH (Ethernet): dist/generic-s3-eth.bin
node tools/panel_mock.mjs --user admin:adminpass123   # the panel without a board
```

See the [firmware guide](docs/NODE_FIRMWARE.md) (the board, the ports, the first start and the bench checklist) and the [wiring notes](docs/NODE_HARDWARE.md).""",
      "testing": r"""```bash
cmake -S tests -B build/host && cmake --build build/host && ctest --test-dir build/host
python -I tools/armor_ci_validate.py
```

18 host test programs and 6 Python checks run under `ctest`; 11824 checks counted by the host programs, built with `-Werror`.

Python checks: the panel texts in eight languages, the tasks, the save paths, the Bluetooth session under its lock and the routes the panel calls (and, in some nodes, the HTTP codes or the glyphs of the fonts)

The host tests need any C++17 compiler (Linux, WSL, MSYS2); the web panel is also exercised in a real browser against a stand-in node (`tools/panel_mock.mjs`, `tools/panel_browser_test.mjs`).

`test_clock` prints only `ok` and has no counter; every other program reports its checks. The real frames of the tests are in `tests/pylontech_real.hpp`, `pylontech_us2000_real.hpp`, `pylontech_logs_real.hpp`, `ant_frames.hpp` and `battery_bench.hpp`.""",
      "build": "`tools/build_node.sh` builds the image in the ESP-IDF 5.5.5 container and the release carries the image, its SHA-256 and its Ed25519 signature, one per board; the image is written by USB-C the first time and updated from the panel afterwards.",
      "troubleshooting": r"""| You see | Because | Do |
|---|---|---|
| You lost the password or the node no longer joins the network | A node with set-up and no address after 90 s opens its own Wi-Fi `ARMOR-SETUP-xxxxxx` (open `http://192.168.4.1/`) | To start again hold BOOT for 8 seconds in the first 30 seconds after power-up (erases settings and users), or use *Factory reset* in the panel |
| An update from GitHub is refused | The release has no checksum or signature, they do not match (`e_no_checksum`, `e_no_signature`, `e_checksum_mismatch`, `e_bad_signature`), has no image for this board (`e_no_asset_for_board`) or is for another project (`e_wrong_firmware`) | Nothing changed on the node; try again or let an administrator upload the file by hand |
| A write to a battery is refused with a code | `serial_mismatch`, `not_pylontech`, `no_battery`, `unknown_model`, `not_idle`, `critical_alarm`, `busy`, `cooldown`, `locked`, `not_armed`, `bad_token`, `expired`, `disabled`, `image_missing`, `image_mismatch`...: the node refuses what is not exactly the operation armed | Read the code in the result, fix the cause and arm the operation again (see [docs/BATTERY_MAINTENANCE.md](docs/BATTERY_MAINTENANCE.md)) |
| A port publishes nothing | The port is off, its type is `raw` (listen only), the speed or the pins do not match the equipment, or the equipment does not answer | Check the port settings and the wiring in [docs/NODE_HARDWARE.md](docs/NODE_HARDWARE.md); the panel shows the raw dump of a port while it looks at it |""",
      "structure": r"""<p align="center">
  <img src="images/repository-structure.svg" alt="Repository structure of ARMOR-NODE-SOLAR" width="100%">
</p>

<details>
<summary>Text version of the tree</summary>

```text
ARMOR-NODE-SOLAR/
├── main/                                the firmware: an ESP-IDF component
├── core/                                the logic with no ESP-IDF, tested on a computer
├── panel/                               the web panel embedded in the firmware
├── tests/                               host tests and Python checks
├── docs/                                10 guides: protocols, messages, maintenance, hardware
├── tools/                               build, pack and check tools
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
├── sdkconfig.board.s3-eth               the settings of one board
├── sdkconfig.board.s3-wifi              the settings of one board
├── secrets/                             example of the node file (the real ones are not versioned)
├── build-test.sh build-test.bat         run the tests through the shared workflow
└── .gitattributes .gitignore            Git settings
```

</details>""",
      "roadmap": r"""**Known limits today**

* The Voltronic, Pylontech and ANT-BMS frames, checksums and readings are checked against the documented frames and recorded samples; none has talked to a real inverter or battery yet.
* The web panel is exercised in a browser against a mock of the node, not on a board.
* No board built and no inverter or battery connected: nothing has run on real equipment yet.
* The set-up code, the login with a limit on wrong passwords, the Bluetooth PIN and the signed updates are tested on the host; there has been no independent review.
* The hash and Ed25519 signature checks and the rollback logic pass on the host; an update over the air has never been run on a board.
* Writing to Pylontech batteries is off by default and has only been tested against a simulator.

**Next**

* Run the node on a real board with a real inverter and batteries, then the Bluetooth link of the ANT-BMS (the cable is used today), the update over the air and the writes to a battery.""",
    },
  },
  "es": {
    "tagline": "Nodo pasarela solar: lee inversores y baterías por hasta diez puertos serie (firmware para ESP32-S3, su panel web y la biblioteca de protocolos)",
    "honest": "El firmware compila en el contenedor ESP-IDF 5.5.5, su núcleo (los ajustes, el intercambio con cada tipo de equipo, la aritmética de la UART emulada, el canal Bluetooth, las comprobaciones de versión y firma: 11.824 comprobaciones en 18 programas de test) se prueba en un ordenador con equipos de pega, los mensajes que hace los acepta ARMOR-COMMON y el panel se ejercitó en un navegador contra un nodo de pega. **Nunca ha corrido en una placa y no se ha conectado ningún inversor ni batería**: el Wi-Fi, el panel sobre TLS, la actualización, las UART de hardware y emuladas y los formatos de los protocolos (escritos a partir de documentos públicos y de memoria) están sin probar. Las tramas ANT-BMS de sus tests las capturaron otras personas en sus propias unidades: este proyecto no ha leído ninguna por sí mismo.",
    "glance": [
      [
        "Función",
        "Nodo de campo solar para ESP32-S3: inversores y baterías (familia: Field Nodes, padre: ARMOR-COMMON)",
      ],
      [
        "Tecnología",
        "C++17, ESP-IDF 5.5.5, ESP32-S3",
      ],
      [
        "Pruebas",
        "11824 comprobaciones en 18 programas de host y 6 de Python (`ctest`)",
      ],
      [
        "Equipos",
        "Inversores Voltronic / MPP Solar, baterías Pylontech, ANT-BMS; 10 puertos serie",
      ],
      [
        "Funciona en",
        "ESP32-S3-WROOM-1 N16R8 o Waveshare ESP32-S3-ETH; pruebas de host en cualquier ordenador",
      ],
      [
        "En hardware real",
        "Ninguno todavía: ninguna placa montada ni inversor o batería conectado (solo tests en ordenador, la compilación y el panel en un navegador)",
      ],
      [
        "Licencia",
        "GPL-3.0-or-later",
      ],
    ],
    "status": {
      "software": "El firmware compila en el contenedor ESP-IDF 5.5.5 para las dos placas (Wi-Fi y Ethernet).",
      "tests": "Pasan 11.824 comprobaciones en 18 programas de host (`ctest`): los ajustes, el intercambio con cada tipo de equipo, la UART emulada, el canal Bluetooth y las comprobaciones de versión.",
      "protocols": "Las tramas, sumas de control y lecturas de Voltronic, Pylontech y ANT-BMS se comprueban contra las tramas documentadas y muestras grabadas; ninguno ha hablado todavía con un inversor o una batería reales.",
      "ui": "El panel web se ha ejercitado en un navegador contra una simulación del nodo, no en una placa.",
      "hardware": "Ninguna placa construida ni inversor o batería conectados: nada ha funcionado todavía con equipos reales.",
      "security": "El código de configuración, el acceso con límite de contraseñas erróneas, el PIN Bluetooth y las actualizaciones firmadas están probados en el host; no ha habido una revisión independiente.",
      "updates": "Las comprobaciones de hash y de firma Ed25519 y la lógica de vuelta atrás pasan en el host; una actualización por aire nunca se ha ejecutado en una placa.",
      "writing": "La escritura en baterías Pylontech está desactivada por defecto y solo se ha probado contra un simulador.",
      "integration": "Los mensajes del nodo se validan contra los esquemas compartidos y los vectores de conformidad de ARMOR-COMMON. Su cliente MQTT se prueba contra un Mosquitto real en los tests; ninguna placa los ha enviado aún a un servidor.",
      "docs": "Ocho idiomas, la guía del firmware, las notas de cableado y el historial de cambios están al día.",
    },
    "docs": [
      "[Firmware del nodo](docs/NODE_FIRMWARE.md): la placa, los puertos, el primer arranque y la lista de banco",
      "[Cableado](docs/NODE_HARDWARE.md), [protocolos](docs/PROTOCOLS.md) y [mensajes](docs/SOLAR_MESSAGES.md)",
      "[Mantenimiento de baterías](docs/BATTERY_MAINTENANCE.md) y su [plan de pruebas de banco](docs/BATTERY_BENCH_TEST_PLAN.md)",
      "[Menús de Studio](docs/STUDIO_MENUS.md), [pruebas de banco](docs/BENCH_TESTS.md), [código de puesta en marcha](docs/SETUP_CODE.md) y [alta por Bluetooth](docs/BLE_PROVISIONING.md)",
    ],
    "contributing_first": "Antes de un pull request ejecuta `ctest --test-dir build/host` and `python -I tools/armor_ci_validate.py`: debe pasar. Consulta [CONTRIBUTING.md](CONTRIBUTING.md) y el [código de conducta](CODE_OF_CONDUCT.md).",
    "languages_extra": "",
    "body": {
      "overview": r"""* **Dos placas, un firmware:** una ESP32-S3-WROOM-1 N16R8 por Wi-Fi (la de serie) y la Waveshare ESP32-S3-ETH por su cable Ethernet (DHCP o una dirección fija; conserva su propia red Wi-Fi para llegar a ella desde un móvil). La imagen se elige al compilar (`tools/build_node.sh generic s3-wifi` o `generic s3-eth`); la tabla de pines, los pines por defecto de los puertos y la forma de acceso siguen a la placa, y una imagen es solo para su placa. Ambas compilan y tienen tests en el ordenador; ninguna ha funcionado en una placa.
* **El firmware del nodo** (ESP32-S3-WROOM-1 N16R8 por Wi-Fi, o Waveshare ESP32-S3-ETH por cable): diez puertos serie, tres UART de hardware y siete emuladas (hasta 19200 baudios), cada una independiente y cada una lee un inversor, una batería o un monitor en crudo, de modo que un nodo puede leer solo inversores, solo baterías o una mezcla.
* **El panel web del nodo,** el mismo de los nodos radar: configuración con un código que se muestra en la consola USB, acceso y usuarios, Wi-Fi (estación y punto de acceso), broker, actualización por aire con vuelta atrás, registro, HTTPS, y las páginas de los puertos (con lo que oye cada uno, para protocolos aún sin decodificar) y de las lecturas, en ocho idiomas.
* **Inversores Voltronic / MPP Solar** (Axpert, PIP, InfiniSolar y clones), RS232 a 2400 baudios: las tramas y su CRC, y las lecturas `QPIGS` (red, salida, batería, FV, bits de estado), `QMOD` (modo), `QPIWS` (avisos y averías por nombre) y `QPIRI` (valores nominales). Solo se pueden construir comandos de lectura: un ajuste cambia cómo se alimenta la casa. Tres dialectos, elegidos en el puerto o encontrados por él (*auto*): PI30, REVO (otro `QPIGS`, respuestas con suma de comprobación) y PI18 (`^P005GS`: InfiniSolar V, LV5048, SunGoldPower), solo lectura.
* **Baterías Pylontech** (US2000, US3000, US5000): la tabla `pwr` de la consola (tensión, corriente, temperaturas y estado de carga de cada módulo), `bat <n>` (tensión y temperatura de cada celda) e `info <n>` (modelo, capacidad restante y total, ciclos), resumidas como una pila con su capacidad y energía totales, y la trama RS485 con sus dos comprobaciones. Los formatos están escritos de memoria de la consola pública y pueden variar entre firmwares. Las columnas se encuentran por los nombres de la cabecera (incluido el formato de la US5000 V2.3 con sus columnas Id, MosTempr y SysAlarm.St), la carga restante y el equilibrado salen de `bat`, y el modelo, la capacidad nominal y los ciclos de `info` y `stat`, que se piden una vez y se guardan media hora.
* **Lo que dice de sí mismo un módulo Pylontech:** su modelo y las versiones de su placa y su software, sus celdas y la corriente que admite, los contadores de su vida (`stat`), la salud de cada celda (`soh`, marcando la anormal) y la entrada más reciente de su registro de eventos, con los nombres de las protecciones tal como los imprime la consola. La consola solo lee, y un administrador puede descargar como archivo de texto lo que oyó un puerto.
* **Los mensajes del nodo** (`armor/solar/<nodo>/<dispositivo>/state`, uno por inversor o pila de baterías), definidos en ARMOR-COMMON con esquemas y vectores de conformidad; lo que producen los puertos se comprueba contra ellos.
* **Baterías con ANT-BMS** (las placas negras de los packs caseros, de 7S a 32S), UART de 3,3 V a 19200 baudios: los dos protocolos de su firmware (el nodo pregunta en uno y luego en el otro y se queda con el que responde), con las celdas, temperaturas, estado de carga, corriente, capacidades y los estados de los MOSFET y del equilibrador, comprobados con tramas capturadas en cuatro modelos reales. Solo lectura: sus comandos de escritura pueden desconectar una batería en carga. Un botón de la página de puertos lee además el modelo, la versión y los 56 ajustes de protección y equilibrado de la BMS (protocolo nuevo), solo lectura.
* **Configuración desde el móvil por Bluetooth,** el mismo canal que el del nodo radar: la app ARMOR encuentra el nodo como `ARMOR-XXXXXX` y ajusta su nombre, Wi-Fi, dirección, broker y modo de Bluetooth con los usuarios y el código de puesta en marcha del panel ([el protocolo](docs/BLE_PROVISIONING.md)). Solo escucha mientras el nodo no tiene usuarios, salvo que se indique otra cosa. La parte de radio nunca ha corrido en una placa.
* **La placa base con multiplexores (perfil *mux*):** tres UART de hardware, cada una detrás de un 74HC4052, atienden hasta ocho puertos en grupos de 4, 2 y 2 que se turnan en su línea, cada puerto con su propia velocidad y polaridad, y un LED por puerto a través de un 74HC595; las celdas de una pila Pylontech alta pueden leerse por turnos. Para un inversor en el dialecto estándar, la **segunda entrada fotovoltaica** (`QPIGS2`) y las **unidades de un sistema en paralelo** (`QPGS`) son lecturas opcionales. Nada de esto ha corrido en una placa.
* **Actualizaciones por aire firmadas:** el nodo solo instala desde GitHub una imagen cuyo SHA-256 coincide y que lleva una firma Ed25519 válida del responsable (la clave pública está en el firmware, la privada nunca sale del responsable); un archivo subido a mano por un administrador en el panel se sigue aceptando. Las páginas y mensajes del panel están en ocho idiomas.
* **Emparejamiento Bluetooth con PIN:** el PIN de seis cifras se deriva del código de configuración, se imprime en la consola USB y se muestra a un administrador en el panel; el móvil tiene que escribirlo antes de poder cambiar los ajustes del nodo.
* **Todavía no:** el enlace Bluetooth del ANT-BMS (el nodo usa el cable, el más estable de los dos) y una prueba en una placa real con equipos reales.
* **Solo la casa puede usar el panel:** el panel responde por defecto a la red privada (o a las redes que su dueño indique, como una VPN), rechaza una lista que dejaría fuera a quien la guarda, cuenta las contraseñas erróneas por persona y por dirección, y funciona detrás del proxy del servidor para llegar a él desde fuera de casa sin publicar el nodo.
* **Desconocido no es ninguno:** un inversor REVO no tiene consulta de avisos, así que su mensaje lleva `warnings_known: false` y Studio muestra los avisos como desconocidos en vez de "ninguno".
* **Enlace cifrado opcional con el broker (TLS):** desactivado por defecto, así que el nodo habla MQTT sin cifrar como antes. Un interruptor y una caja para el certificado de la autoridad propia de la instalación (PEM, 2 KB como máximo) en la página Broker hacen que se conecte con `mqtts://`, confíe solo en esa autoridad y compruebe que el certificado del broker se hizo para la dirección a la que llegó; lo que no sea un único certificado PEM se rechaza. Cubierto con pruebas en el ordenador; el handshake aún no se ha ejecutado en una placa.
* **Informe de salud:** cada minuto más o menos el nodo publica cuánto lleva encendido y por qué se reinició la última vez, su memoria libre, su enlace y su señal Wi-Fi, cuántas veces se conectó al broker y el último error que anotó (`armor/health/<nodo>`, el contrato `node_health` de ARMOR-COMMON). El código que lo construye lo comparten todos los nodos y está probado en un ordenador; no se ha ejecutado en una placa.
* **Escritura en baterías Pylontech (desactivada por defecto):** solo operaciones tipadas - reloj, contadores y registros, reinicio, capacidad, el reinicio del nivel de carga, límites y protecciones, salidas, número de serie, memoria externa, firmware por XMODEM-1K y una consola de experto con lista de bloqueo - en dos pasos (preparar y ejecutar con un token de un solo uso), leyendo la batería antes y después, con la contraseña de servicio guardada solo en el nodo y una consola simulada para las pruebas. Sin probar en una batería real: mira el [plan de pruebas de banco](docs/BATTERY_BENCH_TEST_PLAN.md).
* **Control desde el servidor:** Studio puede reiniciar el nodo limpiamente, pausarlo hasta una hora (se reanuda solo), poner su trabajo en espera (sin fin, se conserva al reiniciar, el nodo sigue conectado y respondiendo), hacer que se muestre, pedirle una instantánea de diagnóstico y marcarlo en mantenimiento (`armor/control/<nodo>/...`, el contrato `node_control` de ARMOR-COMMON). Cada orden son dos pasos con un token de un solo uso que pertenece a esa operación, solo el servidor puede escribirlas en el broker, y no existe restablecimiento de fábrica, borrado ni sueño profundo. Mientras el nodo está en pausa o en espera no escribe ninguna batería (una operación en curso aún se puede cancelar) y sigue leyendo inversores y baterías. El código es compartido por todos los nodos y se prueba en un ordenador; no ha funcionado en una placa.
* **Los valores absurdos se nombran, no se esconden:** cuando un inversor envía un número imposible, el nodo lo mantiene en el límite del contrato y lo nombra en `clamped`, así que el servidor lo muestra como no real; y el volcado en bruto de un puerto solo se genera mientras el panel lo está mirando.
* **Diagnóstico sin cable:** tras un arranque que no fue limpio (un cuelgue, un watchdog, una caída de la alimentación, una reserva de memoria fallida) el informe de salud dice el motivo durante diez minutos; un fallo deja su volcado de núcleo (core dump) para verlo, descargarlo o borrarlo desde el panel; los ajustes guardados se copian antes de cada instalación de firmware y se recuperan si una actualización los daña; y un administrador puede pedir al nodo, a través del servidor, un paquete de diagnóstico o su registro con un token de un solo uso.
* **Sellado opcional de los secretos guardados:** desactivado por defecto (`security.seal_secrets`, o `nodes.nvs_encryption` del servidor). Activado, las contraseñas, tokens, claves, PIN y hashes de contraseña que guarda el nodo quedan sellados con ChaCha20-Poly1305 y todo lo demás sigue legible; activarlo o desactivarlo los reescribe sin perder nada, aunque el nodo se pare a medias. No se quema ningún eFuse ni se cifra la flash: la clave está en una partición del mismo chip, así que **no** protege frente a quien tenga la placa, y un nodo instalado antes de esa partición conserva sus secretos como estaban hasta que se grabe con la nueva tabla de particiones.""",
      "role": r"""ARMOR-NODE-SOLAR es la pasarela entre el equipo solar de la casa y la familia. Lee inversores y baterías por hasta diez puertos serie y publica lo que lee para [ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER), que guarda el historial, los totales y las alarmas; los menús *Inversores* y *Baterías* de [ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) y la pantalla Solar de [ARMOR-ANDROID-CONTROL](https://github.com/JuanenRac/ARMOR-ANDROID-CONTROL) lo muestran. Solo lee: nunca escribe un ajuste en ningún equipo.

| Nombre | Cómo | Para qué |
|---|---|---|
| ARMOR-SERVER | MQTT `armor/solar/<node>/<device>/state` | Recibe un mensaje por inversor o pila de baterías; ordena el mantenimiento de una batería |
| ARMOR-STUDIO | menús, enlace al panel | Muestra inversores y baterías y abre el panel del nodo |
| ARMOR-ANDROID-CONTROL | Bluetooth | Configura el nodo en el campo y muestra las pantallas de energía |
| ARMOR-COMMON | contrato solar | Los mensajes se comprueban con sus esquemas; el firmware común se copia de él |""",
      "architecture": r"""<p align="center">
  <img src="images/architecture.svg" alt="Arquitectura de ARMOR-NODE-SOLAR: quién lo llama, qué contiene y de qué depende" width="100%">
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
| Una batería escrita por error o por un atacante | Tres cerrojos: el ajuste del nodo `battery.write_enabled` (administradores) con la contraseña de servicio de la batería, `ARMOR_BATTERY_WRITE=1` del servidor, y la lista de acceso del broker para `armor/solar/<nodo>/maintenance/command` y `.../result` |
| Una orden de escritura repetida o robada | Dos pasos (armar y ejecutar con un token de un solo uso), ventana de armado de 120 s, 30 s de enfriamiento entre escrituras a un puerto, 3 fallos en 10 minutos lo bloquean 5; se vuelve a teclear el número de serie de la batería, la batería debe estar en reposo y sin alarma crítica, y la imagen de firmware se conserva 30 minutos y se comprueba |
| Escribir en un inversor o un ANT-BMS | Los comandos de escritura de un inversor (un ajuste cambia cómo se alimenta la casa) y de un ANT-BMS (puede desconectar una batería bajo carga) ni siquiera se pueden construir |
| Números absurdos mostrados como reales | Un valor imposible se retiene en el límite del contrato y se nombra en `clamped`, para que el servidor lo muestre como no real; un inversor REVO no tiene consulta de avisos, así que su mensaje dice `warnings_known: false` en vez de afirmar que no hay avisos |

Ninguna trama se ha leído de un inversor o una batería reales; los formatos están escritos de documentos públicos y de memoria, y las tramas ANT-BMS de las pruebas las capturaron otras personas. Lee [docs/BATTERY_MAINTENANCE.md](docs/BATTERY_MAINTENANCE.md) y [SECURITY.md](SECURITY.md).""",
      "interfaces": r"""| Parte | Qué define |
|---|---|
| MQTT | `armor/solar/<nodo>/<dispositivo>/state` (un mensaje por inversor o pila de baterías, tipo `inverter` o `battery` del contrato de ARMOR-COMMON), `armor/solar/<nodo>/maintenance/{command,result}`, `armor/health/<nodo>` (última voluntad), `armor/control/<id>/{command,result,maintenance}` y `armor/control/all/command` |
| Puertos | 10 puertos serie (3 UART de hardware y 7 emuladas, hasta 19200 baudios si son emuladas); por puerto un tipo: `voltronic` (2400 baudios, cada 5 s), `pylontech` (115200, cada 10 s), `ant` (19200, cada 5 s) o `raw` (9600, solo escucha, no publica); dialectos de inversor `auto`, `pi30`, `revo`, `pi18`; el perfil mux tiene 3 grupos de puertos |
| Consultas | Voltronic: `QPIGS`, `QMOD`, `QPIWS`, `QPIRI` (y `QPIGS2`, `QPGS` en un inversor estándar con el mux); consola Pylontech: `pwr`, `bat <n>`, `info <n>`, `stat`, `soh`, registro de eventos, hasta 8 módulos pedidos celda a celda |
| Panel | Las rutas de la familia (`tests/check_routes.py` comprueba que toda ruta que llama el panel existe) más las páginas de puertos y lecturas; 51 códigos de error con texto en ocho idiomas (772 filas en `panel/text.js`); los menús de Studio, en [docs/STUDIO_MENUS.md](docs/STUDIO_MENUS.md) |""",
      "configuration": r"""| Variable | Por defecto | Qué define |
|---|---|---|
| `enabled`, `kind`, `name`, `baud`, `rx`, `tx`, `de`, `poll_s`, `modules`, `dialect` | - | Los ajustes de cada puerto: activado o no, el tipo, el nombre del dispositivo en el topic, la velocidad (0 = la del tipo), los pines (y el pin DE/RE de un RS485), el periodo de sondeo (0 = el del tipo), el número de módulos y el dialecto del inversor; como máximo 3 redes de reserva y 2 brokers de reserva |
| `battery.write_enabled` | off | El cerrojo del nodo para escribir en una batería Pylontech (administradores, con la contraseña de servicio de la batería, que nunca sale del nodo) |
| `CONFIG_ARMOR_BOARD_S3_WIFI` / `_S3_ETH` | wifi | La placa: ESP32-S3-WROOM-1 N16R8 por Wi-Fi (por defecto) o la Waveshare ESP32-S3-ETH |
| `CONFIG_ARMOR_NODE_ID`, `_SETUP_CODE`, `_FLEET_SECRET`, `_MQTT_*`, `_HEARTBEAT_S`, `_BLE_SETUP_MINUTES`, `_BOOT_FACTORY_RESET` | - | Los ajustes que comparten todos los nodos: el nombre (vacío da `armor-` y los últimos bytes de la MAC), el código de puesta en marcha (vacío: aleatorio), el secreto de flota (16+ caracteres, nunca en el repositorio), los primeros ajustes del broker, el latido (de 2 a 300 s), los minutos de puesta en marcha por Bluetooth (de 1 a 120) y el reinicio con BOOT (8 s en los primeros 30 s) |""",
      "quickstart": r"""**Requisitos:** un compilador C++17 para las pruebas de host; el contenedor ESP-IDF 5.5.5 para compilar la imagen; una ESP32-S3-WROOM-1 N16R8 o una Waveshare ESP32-S3-ETH.

```bash
cmake -S tests -B build/host && cmake --build build/host && ctest --test-dir build/host   # host tests, -Werror
build/host/emit_poller_samples | python tests/check_samples.py   # what the ports make is accepted by ARMOR-COMMON
tools/build_node.sh generic                       # the image for the N16R8 board in the ESP-IDF container: dist/generic-s3-wifi.bin
tools/build_node.sh generic s3-eth               # the same firmware for the Waveshare ESP32-S3-ETH (Ethernet): dist/generic-s3-eth.bin
node tools/panel_mock.mjs --user admin:adminpass123   # the panel without a board
```

Véase la [guía del firmware](docs/NODE_FIRMWARE.md) (la placa, los puertos, el primer arranque y la lista de pruebas en banco) y las [notas de cableado](docs/NODE_HARDWARE.md).""",
      "testing": r"""```bash
cmake -S tests -B build/host && cmake --build build/host && ctest --test-dir build/host
python -I tools/armor_ci_validate.py
```

18 programas de prueba de host y 6 comprobaciones en Python se ejecutan con `ctest`; 11824 comprobaciones contadas por los programas de host, compilados con `-Werror`.

Comprobaciones Python: los textos del panel en ocho idiomas, las tareas, las rutas de guardado, la sesión Bluetooth bajo su bloqueo y las rutas que llama el panel (y, en algunos nodos, los códigos HTTP o los glifos de las fuentes)

Las pruebas de host necesitan cualquier compilador C++17 (Linux, WSL, MSYS2); el panel web también se ejercita en un navegador real contra un nodo de pruebas (`tools/panel_mock.mjs`, `tools/panel_browser_test.mjs`).

`test_clock` solo imprime `ok` y no tiene contador; los demás programas informan de sus comprobaciones. Las tramas reales de las pruebas están en `tests/pylontech_real.hpp`, `pylontech_us2000_real.hpp`, `pylontech_logs_real.hpp`, `ant_frames.hpp` y `battery_bench.hpp`.""",
      "build": "`tools/build_node.sh` compila la imagen en el contenedor ESP-IDF 5.5.5 y la versión lleva la imagen, su SHA-256 y su firma Ed25519, una por placa; la imagen se graba por USB-C la primera vez y después se actualiza desde el panel.",
      "troubleshooting": r"""| Ves | Porque | Haz |
|---|---|---|
| Perdiste la contraseña o el nodo ya no se une a la red | Un nodo con puesta en marcha y sin dirección tras 90 s abre su propio Wi-Fi `ARMOR-SETUP-xxxxxx` (abre `http://192.168.4.1/`) | Para empezar de cero mantén BOOT 8 segundos en los primeros 30 segundos tras encender (borra ajustes y usuarios), o usa *Restablecer de fábrica* en el panel |
| Se rechaza una actualización desde GitHub | La versión no trae suma de comprobación ni firma, no coinciden (`e_no_checksum`, `e_no_signature`, `e_checksum_mismatch`, `e_bad_signature`), no trae imagen para esta placa (`e_no_asset_for_board`) o es de otro proyecto (`e_wrong_firmware`) | El nodo no cambió; reintenta o deja que un administrador suba el fichero a mano |
| Se rechaza una escritura a una batería con un código | `serial_mismatch`, `not_pylontech`, `no_battery`, `unknown_model`, `not_idle`, `critical_alarm`, `busy`, `cooldown`, `locked`, `not_armed`, `bad_token`, `expired`, `disabled`, `image_missing`, `image_mismatch`...: el nodo rechaza lo que no es exactamente la operación armada | Lee el código del resultado, corrige la causa y arma la operación otra vez (mira [docs/BATTERY_MAINTENANCE.md](docs/BATTERY_MAINTENANCE.md)) |
| Un puerto no publica nada | El puerto está apagado, su tipo es `raw` (solo escucha), la velocidad o los pines no coinciden con el equipo, o el equipo no contesta | Revisa los ajustes del puerto y el cableado en [docs/NODE_HARDWARE.md](docs/NODE_HARDWARE.md); el panel muestra el volcado crudo de un puerto mientras lo mira |""",
      "structure": r"""<p align="center">
  <img src="images/repository-structure.svg" alt="Estructura del repositorio de ARMOR-NODE-SOLAR" width="100%">
</p>

<details>
<summary>Versión en texto del árbol</summary>

```text
ARMOR-NODE-SOLAR/
├── main/                                el firmware: un componente de ESP-IDF
├── core/                                la lógica sin ESP-IDF, probada en un ordenador
├── panel/                               el panel web embebido en el firmware
├── tests/                               pruebas de host y comprobaciones Python
├── docs/                                10 guías: protocolos, mensajes, mantenimiento, hardware
├── tools/                               herramientas de compilación, empaquetado y comprobación
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
├── sdkconfig.board.s3-eth               los ajustes de una placa
├── sdkconfig.board.s3-wifi              los ajustes de una placa
├── secrets/                             ejemplo del fichero del nodo (los reales no se versionan)
├── build-test.sh build-test.bat         ejecutar las pruebas con el flujo compartido
└── .gitattributes .gitignore            ajustes de Git
```

</details>""",
      "roadmap": r"""**Límites conocidos hoy**

* Las tramas, sumas de control y lecturas de Voltronic, Pylontech y ANT-BMS se comprueban contra las tramas documentadas y muestras grabadas; ninguno ha hablado todavía con un inversor o una batería reales.
* El panel web se ha ejercitado en un navegador contra una simulación del nodo, no en una placa.
* Ninguna placa construida ni inversor o batería conectados: nada ha funcionado todavía con equipos reales.
* El código de configuración, el acceso con límite de contraseñas erróneas, el PIN Bluetooth y las actualizaciones firmadas están probados en el host; no ha habido una revisión independiente.
* Las comprobaciones de hash y de firma Ed25519 y la lógica de vuelta atrás pasan en el host; una actualización por aire nunca se ha ejecutado en una placa.
* La escritura en baterías Pylontech está desactivada por defecto y solo se ha probado contra un simulador.

**Lo siguiente**

* Ejecutar el nodo en una placa real con un inversor y baterías reales, y luego el enlace Bluetooth del ANT-BMS (hoy se usa el cable), la actualización por aire y las escrituras a una batería.""",
    },
  },
  "de": {
    "tagline": "Solar-Gateway-Knoten: liest Wechselrichter und Batterien über bis zu zehn serielle Ports (ESP32-S3-Firmware, sein Web-Panel und die Protokollbibliothek)",
    "honest": "Die Firmware baut im ESP-IDF-5.5.5-Container, ihr Kern (die Einstellungen, der Austausch mit jeder Geräteart, die Arithmetik der emulierten UART, der Bluetooth-Kanal, die Versions- und Signaturprüfungen: 11.824 Prüfungen in 18 Testprogrammen) wird auf einem Computer mit Ersatzgeräten getestet, die von ihr erzeugten Nachrichten akzeptiert ARMOR-COMMON, und das Panel wurde in einem Browser gegen einen Ersatzknoten geprüft. **Sie lief nie auf einer Platine, und es wurde kein Wechselrichter und keine Batterie angeschlossen**: das WLAN, das Panel über TLS, das Update, die Hardware- und die emulierten UARTs und die Formate der Protokolle (nach öffentlichen Dokumenten und aus dem Gedächtnis geschrieben) sind unerprobt. Die ANT-BMS-Rahmen in den Tests wurden von anderen Personen an ihren eigenen Geräten aufgezeichnet: dieses Projekt hat selbst noch keinen gelesen.",
    "glance": [
      [
        "Rolle",
        "Solar-Feldknoten für ESP32-S3: Wechselrichter und Batterien (Familie: Field Nodes, übergeordnet: ARMOR-COMMON)",
      ],
      [
        "Technik",
        "C++17, ESP-IDF 5.5.5, ESP32-S3",
      ],
      [
        "Tests",
        "11824 Prüfungen in 18 Host-Programmen und 6 Python-Prüfungen (`ctest`)",
      ],
      [
        "Geräte",
        "Voltronic- / MPP-Solar-Wechselrichter, Pylontech-Batterien, ANT-BMS; 10 serielle Ports",
      ],
      [
        "Läuft auf",
        "ESP32-S3-WROOM-1 N16R8 oder Waveshare ESP32-S3-ETH; Host-Tests auf jedem Computer",
      ],
      [
        "Auf echter Hardware",
        "Noch keiner: keine Platine aufgebaut und kein Wechselrichter oder keine Batterie angeschlossen (nur Computertests, der Build und das Panel im Browser)",
      ],
      [
        "Lizenz",
        "GPL-3.0-or-later",
      ],
    ],
    "status": {
      "software": "Die Firmware wird im ESP-IDF-5.5.5-Container für beide Platinen (WLAN und Ethernet) gebaut.",
      "tests": "11.824 Prüfungen in 18 Host-Programmen bestehen (`ctest`): die Einstellungen, der Austausch mit jeder Geräteart, die emulierte UART, der Bluetooth-Kanal und die Versionsprüfungen.",
      "protocols": "Die Telegramme, Prüfsummen und Messwerte von Voltronic, Pylontech und ANT-BMS werden gegen die dokumentierten Telegramme und aufgezeichnete Beispiele geprüft; keines hat bisher mit einem echten Wechselrichter oder einer echten Batterie gesprochen.",
      "ui": "Das Web-Panel wurde in einem Browser gegen eine Nachbildung des Knotens erprobt, nicht auf einer Platine.",
      "hardware": "Keine Platine gebaut und kein Wechselrichter oder keine Batterie angeschlossen: Bisher lief nichts auf echten Geräten.",
      "security": "Der Einrichtungscode, die Anmeldung mit Begrenzung falscher Passwörter, die Bluetooth-PIN und die signierten Aktualisierungen sind auf dem Host getestet; es gab keine unabhängige Prüfung.",
      "updates": "Die Hash- und Ed25519-Signaturprüfungen und die Rückfalllogik bestehen auf dem Host; eine Aktualisierung über die Luft wurde nie auf einer Platine ausgeführt.",
      "writing": "Das Schreiben auf Pylontech-Batterien ist standardmäßig aus und wurde nur gegen einen Simulator getestet.",
      "integration": "Die Nachrichten des Knotens werden gegen die gemeinsamen Schemas und Konformitätsvektoren von ARMOR-COMMON geprüft. Sein MQTT-Client wird in den Tests gegen einen echten Mosquitto gespielt; noch keine Platine hat sie an einen Server geschickt.",
      "docs": "Acht Sprachen, die Firmware-Anleitung, die Verdrahtungshinweise und das Änderungsprotokoll sind aktuell.",
    },
    "docs": [
      "[Knoten-Firmware](docs/NODE_FIRMWARE.md): die Platine, die Ports, der erste Start und die Prüfstand-Checkliste",
      "[Verdrahtung](docs/NODE_HARDWARE.md), [Protokolle](docs/PROTOCOLS.md) und [Nachrichten](docs/SOLAR_MESSAGES.md)",
      "[Batteriewartung](docs/BATTERY_MAINTENANCE.md) und ihr [Prüfstandsplan](docs/BATTERY_BENCH_TEST_PLAN.md)",
      "[Studio-Menüs](docs/STUDIO_MENUS.md), [Prüfstandtests](docs/BENCH_TESTS.md), [Einrichtungscode](docs/SETUP_CODE.md) und [Bluetooth-Einrichtung](docs/BLE_PROVISIONING.md)",
    ],
    "contributing_first": "Führe vor einem Pull Request `ctest --test-dir build/host` and `python -I tools/armor_ci_validate.py` aus: Es muss bestehen. Siehe [CONTRIBUTING.md](CONTRIBUTING.md) und den [Verhaltenskodex](CODE_OF_CONDUCT.md).",
    "languages_extra": "",
    "body": {
      "overview": r"""* **Zwei Platinen, eine Firmware:** ein ESP32-S3-WROOM-1 N16R8 per WLAN (Standard) und die Waveshare ESP32-S3-ETH am Ethernet-Kabel (DHCP oder feste Adresse; ihr eigenes WLAN bleibt, um sie vom Handy aus zu erreichen). Das Image wird beim Bauen gewählt (`tools/build_node.sh generic s3-wifi` oder `generic s3-eth`); Pin-Tabelle, Standard-Pins der Ports und Zugangsweg folgen der Platine, und ein Image gilt nur für seine Platine. Beide bauen und sind am Rechner getestet; keine lief je auf einer Platine.
* **Die Firmware des Knotens** (ESP32-S3-WROOM-1 N16R8 per WLAN oder Waveshare ESP32-S3-ETH am Kabel): zehn serielle Ports, drei Hardware-UARTs und sieben emulierte (bis 19200 Baud), jeder unabhängig und jeder liest einen Wechselrichter, eine Batterie oder einen Rohmonitor, sodass ein Knoten nur Wechselrichter, nur Batterien oder eine Mischung lesen kann.
* **Das Web-Panel des Knotens,** auch das der Radarknoten: Einrichtung mit einem Code, der auf der USB-Konsole erscheint, Anmeldung und Benutzer, WLAN (Station und Access Point), Broker, Update per Funk mit Rollback, Protokoll, HTTPS und die Seiten der Ports (mit dem, was jeder hört, für noch nicht dekodierte Protokolle) und der Messwerte, in acht Sprachen.
* **Voltronic- / MPP-Solar-Wechselrichter** (Axpert, PIP, InfiniSolar und Klone), RS232 mit 2400 Baud: die Rahmen und ihre CRC sowie die Messwerte `QPIGS` (Netz, Ausgang, Batterie, PV, Statusbits), `QMOD` (Modus), `QPIWS` (Warnungen und Störungen mit Namen) und `QPIRI` (Nennwerte). Nur lesende Befehle lassen sich bauen: eine Einstellung ändert, wie das Haus versorgt wird. Drei Dialekte, am Port gewählt oder von ihm gefunden (*auto*): PI30, REVO (ein anderes `QPIGS`, Antworten mit Prüfsumme) und PI18 (`^P005GS`: InfiniSolar V, LV5048, SunGoldPower), nur lesend.
* **Pylontech-Batterien** (US2000, US3000, US5000): die `pwr`-Tabelle der Konsole (Spannung, Strom, Temperaturen und Ladezustand jedes Moduls), `bat <n>` (Spannung und Temperatur jeder Zelle) und `info <n>` (Modell, Rest- und Gesamtkapazität, Zyklen), zusammengefasst als ein Stapel mit Gesamtkapazität und -energie, und der RS485-Rahmen mit seinen zwei Prüfungen. Die Formate sind aus dem Gedächtnis der öffentlichen Konsole geschrieben und können sich je nach Firmware unterscheiden. Die Spalten werden über die Namen der Kopfzeile gefunden (auch das Format der US5000 V2.3 mit Id-Spalten, MosTempr und SysAlarm.St), die Restladung und das Balancing kommen aus `bat`, Modell, Nennkapazität und Zyklen aus `info` und `stat`, die einmal abgefragt und eine halbe Stunde behalten werden.
* **Was ein Pylontech-Modul über sich sagt:** sein Modell und die Versionen von Platine und Software, seine Zellen und der zulässige Strom, die Zähler seines Lebens (`stat`), der Zustand jeder Zelle (`soh`, die auffällige markiert) und der neueste Eintrag seines Ereignisprotokolls, mit den Schutznamen genau so, wie die Konsole sie ausgibt. Die Konsole liest nur, und ein Administrator kann herunterladen, was ein Anschluss gehört hat, als Textdatei.
* **Die Nachrichten des Knotens** (`armor/solar/<Knoten>/<Gerät>/state`, eine je Wechselrichter oder Batteriestapel), in ARMOR-COMMON mit Schemas und Konformitätsvektoren definiert; was die Ports erzeugen, wird dagegen geprüft.
* **ANT-BMS-Batterien** (die schwarzen Platinen selbstgebauter Akkus, 7S bis 32S), 3,3-V-UART mit 19200 Baud: beide Protokolle seiner Firmware (der Knoten fragt im einen und dann im anderen und bleibt bei dem, das antwortet), mit Zellen, Temperaturen, Ladezustand, Strom, Kapazitäten sowie den Zuständen der MOSFETs und des Balancers, geprüft an Frames, die an vier echten Modellen aufgezeichnet wurden. Nur Lesen: seine Schreibbefehle können eine Batterie unter Last trennen. Eine Schaltfläche auf der Port-Seite liest außerdem Modell, Version und 56 Schutz- und Balancing-Einstellungen des BMS (neueres Protokoll), nur lesend.
* **Konfiguration vom Handy über Bluetooth,** derselbe Kanal wie beim Radarknoten: Die ARMOR-App findet den Knoten als `ARMOR-XXXXXX` und stellt Name, WLAN, Adresse, Broker und Bluetooth-Modus mit den Benutzern und dem Einrichtungscode des Panels ein ([das Protokoll](docs/BLE_PROVISIONING.md)). Er lauscht nur, solange der Knoten keinen Benutzer hat, sofern nichts anderes eingestellt ist. Der Funkteil lief noch nie auf einer Platine.
* **Die Basisplatine mit Multiplexern (das *mux*-Profil):** drei Hardware-UARTs, je eines hinter einem 74HC4052, bedienen bis zu acht Ports in Gruppen zu 4, 2 und 2, die sich auf ihrer Leitung abwechseln, jeder Port mit eigener Geschwindigkeit und Polarität, und eine LED pro Port über ein 74HC595; die Zellen eines hohen Pylontech-Stapels lassen sich im Wechsel lesen. Für einen Wechselrichter im Standarddialekt sind der **zweite PV-Eingang** (`QPIGS2`) und die **Einheiten eines Parallelsystems** (`QPGS`) optionale Messungen. Nichts davon lief bisher auf einer Platine.
* **Signierte Over-the-Air-Updates:** der Knoten installiert von GitHub nur ein Abbild, dessen SHA-256 stimmt und das eine gültige Ed25519-Signatur des Betreuers trägt (der öffentliche Schlüssel steckt in der Firmware, der private verlässt den Betreuer nie); eine von einem Administrator im Panel von Hand hochgeladene Datei wird weiterhin akzeptiert. Seiten und Meldungen des Panels sind in acht Sprachen.
* **Bluetooth-Kopplung mit PIN:** die sechsstellige PIN wird aus dem Einrichtungscode abgeleitet, auf der USB-Konsole ausgegeben und einem Administrator im Panel angezeigt; das Telefon muss sie eingeben, bevor es die Einstellungen des Knotens schreiben darf.
* **Noch nicht:** die Bluetooth-Verbindung des ANT-BMS (der Knoten nutzt das Kabel, das stabilere von beiden) und ein Lauf auf einer echten Platine mit echten Geräten.
* **Nur das Haus darf das Panel nutzen:** Das Panel antwortet standardmäßig dem privaten Netz (oder den Netzen, die der Besitzer nennt, etwa einem VPN), lehnt eine Liste ab, die den Speichernden aussperren würde, zählt falsche Passwörter je Person und je Adresse und funktioniert hinter dem Proxy des Servers, sodass man es von außerhalb des Hauses erreicht, ohne den Knoten zu veröffentlichen.
* **Unbekannt ist nicht keine:** ein REVO-Wechselrichter hat keine Warnungsabfrage, deshalb trägt seine Nachricht `warnings_known: false` und Studio zeigt die Warnungen als unbekannt statt als "keine".
* **Optionale verschlüsselte Verbindung zum Broker (TLS):** standardmäßig aus, der Knoten spricht also wie bisher unverschlüsseltes MQTT. Ein Schalter und ein Feld für das Zertifikat der eigenen Zertifizierungsstelle der Anlage (PEM, höchstens 2 KB) auf der Broker-Seite sorgen dafür, dass er sich mit `mqtts://` verbindet, nur dieser Stelle vertraut und prüft, ob das Zertifikat des Brokers für die erreichte Adresse ausgestellt wurde; alles, was nicht genau ein PEM-Zertifikat ist, wird abgelehnt. Durch Host-Tests abgedeckt; der Handshake wurde auf einer Platine noch nicht ausgeführt.
* **Zustandsbericht:** etwa einmal pro Minute veröffentlicht der Knoten, wie lange er läuft und warum er zuletzt neu gestartet ist, seinen freien Speicher, seine Verbindung und sein WLAN-Signal, wie oft er sich mit dem Broker verbunden hat und den letzten protokollierten Fehler (`armor/health/<Knoten>`, der Vertrag `node_health` von ARMOR-COMMON). Der Code, der ihn erzeugt, wird von allen Knoten geteilt und auf einem Computer getestet; auf einer Platine ist er noch nicht gelaufen.
* **Schreiben auf Pylontech-Batterien (standardmäßig aus):** nur typisierte Operationen - Uhr, Zähler und Protokolle, Neustart, Kapazität, das Zurücksetzen des Ladezustands, Grenzwerte und Schutzfunktionen, Ausgänge, Seriennummer, externer Speicher, Firmware per XMODEM-1K und eine Expertenkonsole mit Sperrliste - in zwei Schritten (vorbereiten, dann mit einem Einmal-Token ausführen), die Batterie wird davor und danach gelesen, das Service-Passwort liegt nur im Knoten, und die Tests laufen gegen eine simulierte Konsole. An einer echten Batterie nicht erprobt: siehe den [Prüfstandsplan](docs/BATTERY_BENCH_TEST_PLAN.md).
* **Steuerung vom Server aus:** Studio kann den Knoten sauber neu starten, bis zu einer Stunde pausieren (er läuft von selbst weiter), seine Arbeit in den Standby setzen (ohne Ende, über Neustarts hinweg gespeichert, der Knoten bleibt verbunden und antwortet weiter), ihn sich zeigen lassen, einen Diagnose-Schnappschuss anfordern und ihn als in Wartung markieren (`armor/control/<Knoten>/...`, der Vertrag `node_control` von ARMOR-COMMON). Jeder Befehl besteht aus zwei Schritten mit einem Einmal-Token, das zu dieser Operation gehört; nur der Server darf sie am Broker schreiben, und es gibt kein Zurücksetzen auf Werkseinstellungen, kein Löschen und keinen Tiefschlaf. Solange der Knoten pausiert oder im Standby ist, beschreibt er keine Batterie (eine laufende Operation lässt sich noch abbrechen) und liest weiter Wechselrichter und Batterien. Der Code wird von allen Knoten geteilt und auf einem Rechner getestet; auf einer Platine ist er noch nicht gelaufen.
* **Absurde Werte werden benannt, nicht versteckt:** Sendet ein Wechselrichter eine unmögliche Zahl, hält der Knoten sie am Grenzwert des Vertrags fest und nennt sie in `clamped`, sodass der Server sie als nicht echt anzeigt; und der Rohdaten-Dump eines Ports wird nur erzeugt, solange das Panel ihn ansieht.
* **Diagnose ohne Kabel:** Nach einem unsauberen Start (Absturz, Watchdog, Spannungseinbruch, fehlgeschlagene Speicherreservierung) nennt der Gesundheitsbericht zehn Minuten lang den Grund; ein Absturz hinterlässt sein Core-Dump, das man im Panel ansehen, herunterladen oder löschen kann; die gespeicherten Einstellungen werden vor jeder Firmware-Installation kopiert und wiederhergestellt, falls ein Update sie beschädigt; und ein Administrator kann den Knoten über den Server mit einem Einmal-Token nach einem Diagnosepaket oder seinem Protokoll fragen.
* **Optionales Versiegeln gespeicherter Geheimnisse:** standardmäßig aus (`security.seal_secrets` oder `nodes.nvs_encryption` des Servers). Eingeschaltet werden die Passwörter, Token, Schlüssel, PINs und Passwort-Hashes, die der Knoten speichert, mit ChaCha20-Poly1305 versiegelt, alles andere bleibt lesbar; Ein- und Ausschalten schreibt sie ohne Verlust um, auch wenn der Knoten mittendrin stehen bleibt. Es wird kein eFuse gebrannt und der Flash nicht verschlüsselt: Der Schlüssel liegt in einer Partition desselben Chips und schützt daher **nicht** vor jemandem, der die Platine hat; ein Knoten, der vor dieser Partition installiert wurde, behält seine Geheimnisse unverändert, bis er mit der neuen Partitionstabelle geflasht wird.""",
      "role": r"""ARMOR-NODE-SOLAR ist das Gateway zwischen den Solargeräten des Hauses und der Familie. Es liest Wechselrichter und Batterien über bis zu zehn serielle Ports und veröffentlicht, was es liest, für [ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER), der Verlauf, Summen und Alarme führt; die Menüs *Wechselrichter* und *Batterien* von [ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) und der Solar-Bildschirm von [ARMOR-ANDROID-CONTROL](https://github.com/JuanenRac/ARMOR-ANDROID-CONTROL) zeigen es. Es liest nur: Es schreibt nie eine Einstellung in ein Gerät.

| Name | Wie | Wozu |
|---|---|---|
| ARMOR-SERVER | MQTT `armor/solar/<node>/<device>/state` | Empfängt eine Nachricht je Wechselrichter oder Batteriestapel; ordnet die Wartung einer Batterie an |
| ARMOR-STUDIO | Menüs, Link zum Panel | Zeigt Wechselrichter und Batterien und öffnet das Panel des Knotens |
| ARMOR-ANDROID-CONTROL | Bluetooth | Richtet den Knoten vor Ort ein und zeigt die Energie-Bildschirme |
| ARMOR-COMMON | Solar-Vertrag | Die Nachrichten werden gegen seine Schemas geprüft; die gemeinsame Firmware stammt daraus |""",
      "architecture": r"""<p align="center">
  <img src="images/architecture.svg" alt="Architektur von ARMOR-NODE-SOLAR: wer es aufruft, was es enthält und wovon es abhängt" width="100%">
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
| Eine Batterie, die versehentlich oder von einem Angreifer beschrieben wird | Drei Riegel: die Knoteneinstellung `battery.write_enabled` (Administratoren) mit dem Servicepasswort der Batterie, `ARMOR_BATTERY_WRITE=1` des Servers und die Zugriffsliste des Brokers für `armor/solar/<Knoten>/maintenance/command` und `.../result` |
| Ein wiederholter oder gestohlener Schreibbefehl | Zwei Schritte (Scharfmachen, dann Ausführen mit einem Einmal-Token), ein Scharfmachfenster von 120 s, 30 s Abkühlzeit zwischen Schreibzugriffen auf einen Port, 3 Fehler in 10 Minuten sperren ihn für 5; die Seriennummer der Batterie wird erneut eingetippt, die Batterie muss im Leerlauf und ohne kritischen Alarm sein, und ein Firmware-Image wird 30 Minuten behalten und geprüft |
| Schreiben auf einen Wechselrichter oder ein ANT-BMS | Die Schreibbefehle eines Wechselrichters (eine Einstellung ändert, wie das Haus versorgt wird) und eines ANT-BMS (es kann eine Batterie unter Last trennen) lassen sich nicht einmal bauen |
| Absurde Zahlen als echt angezeigt | Ein unmöglicher Wert wird an der Grenze des Vertrags gehalten und in `clamped` benannt, damit der Server ihn als nicht echt zeigt; ein REVO-Wechselrichter hat keine Warnungsabfrage, daher sagt seine Nachricht `warnings_known: false`, statt keine Warnungen zu behaupten |

Es wurde noch kein Frame von einem echten Wechselrichter oder einer echten Batterie gelesen; die Formate sind aus öffentlichen Dokumenten und aus dem Gedächtnis geschrieben, und die ANT-BMS-Frames der Tests wurden von anderen aufgezeichnet. Lies [docs/BATTERY_MAINTENANCE.md](docs/BATTERY_MAINTENANCE.md) und [SECURITY.md](SECURITY.md).""",
      "interfaces": r"""| Teil | Was sie festlegt |
|---|---|
| MQTT | `armor/solar/<Knoten>/<Gerät>/state` (eine Nachricht je Wechselrichter oder Batteriestapel, Art `inverter` oder `battery` des ARMOR-COMMON-Vertrags), `armor/solar/<Knoten>/maintenance/{command,result}`, `armor/health/<Knoten>` (Last Will), `armor/control/<id>/{command,result,maintenance}` und `armor/control/all/command` |
| Ports | 10 serielle Ports (3 Hardware-UARTs und 7 emulierte, emuliert bis 19200 Baud); je Port ein Typ: `voltronic` (2400 Baud, alle 5 s), `pylontech` (115200, alle 10 s), `ant` (19200, alle 5 s) oder `raw` (9600, nur hören, veröffentlicht nichts); Wechselrichter-Dialekte `auto`, `pi30`, `revo`, `pi18`; das Mux-Profil hat 3 Portgruppen |
| Abfragen | Voltronic: `QPIGS`, `QMOD`, `QPIWS`, `QPIRI` (und `QPIGS2`, `QPGS` bei einem Standard-Wechselrichter mit dem Mux); Pylontech-Konsole: `pwr`, `bat <n>`, `info <n>`, `stat`, `soh`, Ereignisprotokoll, bis zu 8 Module zellenweise abgefragt |
| Panel | Die Familien-Routen (`tests/check_routes.py` prüft, dass jede vom Panel aufgerufene Route existiert) plus die Seiten für Ports und Messwerte; 51 Fehlercodes mit Text in acht Sprachen (772 Zeilen in `panel/text.js`); die Menüs von Studio stehen in [docs/STUDIO_MENUS.md](docs/STUDIO_MENUS.md) |""",
      "configuration": r"""| Variable | Standard | Was sie festlegt |
|---|---|---|
| `enabled`, `kind`, `name`, `baud`, `rx`, `tx`, `de`, `poll_s`, `modules`, `dialect` | - | Die Einstellungen jedes Ports: ein oder aus, der Typ, der Gerätename im Topic, die Geschwindigkeit (0 = die des Typs), die Pins (und der DE/RE-Pin eines RS485), die Abfrageperiode (0 = die des Typs), die Modulzahl und der Wechselrichter-Dialekt; höchstens 3 Ersatznetze und 2 Ersatz-Broker |
| `battery.write_enabled` | off | Der Riegel des Knotens für das Schreiben auf eine Pylontech-Batterie (Administratoren, mit dem Servicepasswort der Batterie, das den Knoten nie verlässt) |
| `CONFIG_ARMOR_BOARD_S3_WIFI` / `_S3_ETH` | wifi | Die Platine: ESP32-S3-WROOM-1 N16R8 per WLAN (Standard) oder die Waveshare ESP32-S3-ETH |
| `CONFIG_ARMOR_NODE_ID`, `_SETUP_CODE`, `_FLEET_SECRET`, `_MQTT_*`, `_HEARTBEAT_S`, `_BLE_SETUP_MINUTES`, `_BOOT_FACTORY_RESET` | - | Die Einstellungen, die alle Knoten teilen: der Name (leer ergibt `armor-` und die letzten Bytes der MAC), der Einrichtungscode (leer: zufällig), das Flottengeheimnis (16+ Zeichen, nie im Repository), die ersten Broker-Einstellungen, der Herzschlag (2 bis 300 s), die Minuten der Bluetooth-Einrichtung (1 bis 120) und der Reset mit BOOT (8 s in den ersten 30 s) |""",
      "quickstart": r"""**Voraussetzungen:** ein C++17-Compiler für die Host-Tests; der ESP-IDF-5.5.5-Container zum Bauen des Images; ein ESP32-S3-WROOM-1 N16R8 oder ein Waveshare ESP32-S3-ETH.

```bash
cmake -S tests -B build/host && cmake --build build/host && ctest --test-dir build/host   # host tests, -Werror
build/host/emit_poller_samples | python tests/check_samples.py   # what the ports make is accepted by ARMOR-COMMON
tools/build_node.sh generic                       # the image for the N16R8 board in the ESP-IDF container: dist/generic-s3-wifi.bin
tools/build_node.sh generic s3-eth               # the same firmware for the Waveshare ESP32-S3-ETH (Ethernet): dist/generic-s3-eth.bin
node tools/panel_mock.mjs --user admin:adminpass123   # the panel without a board
```

Siehe die [Firmware-Anleitung](docs/NODE_FIRMWARE.md) (die Platine, die Ports, der erste Start und die Prüfliste am Prüfstand) und die [Verdrahtungshinweise](docs/NODE_HARDWARE.md).""",
      "testing": r"""```bash
cmake -S tests -B build/host && cmake --build build/host && ctest --test-dir build/host
python -I tools/armor_ci_validate.py
```

18 Host-Testprogramme und 6 Python-Prüfungen laufen unter `ctest`; 11824 Prüfungen, gezählt von den Host-Programmen, mit `-Werror` gebaut.

Python-Prüfungen: die Panel-Texte in acht Sprachen, die Tasks, die Speicherpfade, die Bluetooth-Sitzung unter ihrer Sperre und die vom Panel aufgerufenen Routen (und in manchen Knoten die HTTP-Codes oder die Glyphen der Schriften)

Die Host-Tests brauchen einen beliebigen C++17-Compiler (Linux, WSL, MSYS2); das Web-Panel wird außerdem in einem echten Browser gegen einen Ersatzknoten geprüft (`tools/panel_mock.mjs`, `tools/panel_browser_test.mjs`).

`test_clock` gibt nur `ok` aus und hat keinen Zähler; jedes andere Programm meldet seine Prüfungen. Die echten Frames der Tests liegen in `tests/pylontech_real.hpp`, `pylontech_us2000_real.hpp`, `pylontech_logs_real.hpp`, `ant_frames.hpp` und `battery_bench.hpp`.""",
      "build": "`tools/build_node.sh` baut das Image im ESP-IDF-5.5.5-Container, und die Version trägt das Image, sein SHA-256 und seine Ed25519-Signatur, je eines pro Platine; das Image wird beim ersten Mal per USB-C geschrieben und danach vom Panel aktualisiert.",
      "troubleshooting": r"""| Sie sehen | Weil | Tun Sie |
|---|---|---|
| Du hast das Passwort verloren oder der Knoten tritt dem Netz nicht mehr bei | Ein Knoten in der Einrichtung ohne Adresse nach 90 s öffnet ein eigenes WLAN `ARMOR-SETUP-xxxxxx` (öffne `http://192.168.4.1/`) | Zum Neustart BOOT 8 Sekunden in den ersten 30 Sekunden nach dem Einschalten halten (löscht Einstellungen und Benutzer) oder im Panel *Werksreset* nutzen |
| Ein Update von GitHub wird abgelehnt | Die Version enthält keine Prüfsumme oder Signatur, sie passen nicht (`e_no_checksum`, `e_no_signature`, `e_checksum_mismatch`, `e_bad_signature`), hat kein Image für diese Platine (`e_no_asset_for_board`) oder gehört zu einem anderen Projekt (`e_wrong_firmware`) | Der Knoten blieb unverändert; erneut versuchen oder einen Administrator die Datei von Hand hochladen lassen |
| Ein Schreibzugriff auf eine Batterie wird mit einem Code abgelehnt | `serial_mismatch`, `not_pylontech`, `no_battery`, `unknown_model`, `not_idle`, `critical_alarm`, `busy`, `cooldown`, `locked`, `not_armed`, `bad_token`, `expired`, `disabled`, `image_missing`, `image_mismatch`...: Der Knoten lehnt ab, was nicht genau die scharf gemachte Operation ist | Lies den Code im Ergebnis, behebe die Ursache und mache die Operation erneut scharf (siehe [docs/BATTERY_MAINTENANCE.md](docs/BATTERY_MAINTENANCE.md)) |
| Ein Port veröffentlicht nichts | Der Port ist aus, sein Typ ist `raw` (nur hören), Geschwindigkeit oder Pins passen nicht zum Gerät, oder das Gerät antwortet nicht | Prüfe die Port-Einstellungen und die Verdrahtung in [docs/NODE_HARDWARE.md](docs/NODE_HARDWARE.md); das Panel zeigt den Rohdump eines Ports, solange es ihn ansieht |""",
      "structure": r"""<p align="center">
  <img src="images/repository-structure.svg" alt="Repository-Struktur von ARMOR-NODE-SOLAR" width="100%">
</p>

<details>
<summary>Textversion des Baums</summary>

```text
ARMOR-NODE-SOLAR/
├── main/                                die Firmware: eine ESP-IDF-Komponente
├── core/                                die Logik ohne ESP-IDF, am Rechner getestet
├── panel/                               das in die Firmware eingebettete Web-Panel
├── tests/                               Host-Tests und Python-Prüfungen
├── docs/                                10 Anleitungen: Protokolle, Nachrichten, Wartung, Hardware
├── tools/                               Werkzeuge für Build, Packen und Prüfung
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
├── sdkconfig.board.s3-eth               die Einstellungen einer Platine
├── sdkconfig.board.s3-wifi              die Einstellungen einer Platine
├── secrets/                             Beispiel der Knotendatei (die echten sind nicht versioniert)
├── build-test.sh build-test.bat         Tests über den gemeinsamen Workflow ausführen
└── .gitattributes .gitignore            Git-Einstellungen
```

</details>""",
      "roadmap": r"""**Bekannte Grenzen heute**

* Die Telegramme, Prüfsummen und Messwerte von Voltronic, Pylontech und ANT-BMS werden gegen die dokumentierten Telegramme und aufgezeichnete Beispiele geprüft; keines hat bisher mit einem echten Wechselrichter oder einer echten Batterie gesprochen.
* Das Web-Panel wurde in einem Browser gegen eine Nachbildung des Knotens erprobt, nicht auf einer Platine.
* Keine Platine gebaut und kein Wechselrichter oder keine Batterie angeschlossen: Bisher lief nichts auf echten Geräten.
* Der Einrichtungscode, die Anmeldung mit Begrenzung falscher Passwörter, die Bluetooth-PIN und die signierten Aktualisierungen sind auf dem Host getestet; es gab keine unabhängige Prüfung.
* Die Hash- und Ed25519-Signaturprüfungen und die Rückfalllogik bestehen auf dem Host; eine Aktualisierung über die Luft wurde nie auf einer Platine ausgeführt.
* Das Schreiben auf Pylontech-Batterien ist standardmäßig aus und wurde nur gegen einen Simulator getestet.

**Als Nächstes**

* Den Knoten auf einer echten Platine mit echtem Wechselrichter und Batterien betreiben, danach die Bluetooth-Verbindung des ANT-BMS (heute wird das Kabel genutzt), das Update über die Luft und die Schreibzugriffe auf eine Batterie.""",
    },
  },
  "fr": {
    "tagline": "Nœud passerelle solaire : lit onduleurs et batteries par jusqu'à dix ports série (firmware ESP32-S3, son panneau web et la bibliothèque de protocoles)",
    "honest": "Le firmware se compile dans le conteneur ESP-IDF 5.5.5, son cœur (les réglages, l'échange avec chaque type d'équipement, l'arithmétique de l'UART émulée, le canal Bluetooth, les contrôles de version et de signature : 3 013 vérifications dans 10 programmes de test) est testé sur un ordinateur avec des équipements factices, les messages qu'il produit sont acceptés par ARMOR-COMMON et le panneau a été exercé dans un navigateur contre un nœud factice. **Il n'a jamais tourné sur une carte et aucun onduleur ni batterie n'a été connecté** : le Wi-Fi, le panneau sur TLS, la mise à jour, les UART matérielles et émulées et les formats des protocoles (écrits d'après des documents publics et de mémoire) ne sont pas essayés. Les trames ANT-BMS de ses tests ont été capturées par d'autres personnes sur leurs propres unités : ce projet n'en a lu aucune lui-même.",
    "glance": [
      [
        "Rôle",
        "Nœud de terrain solaire pour ESP32-S3 : onduleurs et batteries (famille : Field Nodes, parent : ARMOR-COMMON)",
      ],
      [
        "Technologie",
        "C++17, ESP-IDF 5.5.5, ESP32-S3",
      ],
      [
        "Tests",
        "11824 vérifications dans 18 programmes hôte et 6 contrôles Python (`ctest`)",
      ],
      [
        "Équipements",
        "Onduleurs Voltronic / MPP Solar, batteries Pylontech, ANT-BMS ; 10 ports série",
      ],
      [
        "Fonctionne sur",
        "ESP32-S3-WROOM-1 N16R8 ou Waveshare ESP32-S3-ETH ; tests sur hôte sur n'importe quel ordinateur",
      ],
      [
        "Sur matériel réel",
        "Aucun pour l'instant : aucune carte montée ni onduleur ou batterie connecté (seulement des tests sur ordinateur, la compilation et le panneau dans un navigateur)",
      ],
      [
        "Licence",
        "GPL-3.0-or-later",
      ],
    ],
    "status": {
      "software": "Le firmware compile dans le conteneur ESP-IDF 5.5.5 pour les deux cartes (Wi-Fi et Ethernet).",
      "tests": "11 824 vérifications dans 18 programmes d'hôte réussissent (`ctest`) : les réglages, l'échange avec chaque type d'équipement, l'UART émulée, le canal Bluetooth et les contrôles de version.",
      "protocols": "Les trames, sommes de contrôle et lectures de Voltronic, Pylontech et ANT-BMS sont vérifiées par rapport aux trames documentées et à des échantillons enregistrés ; aucun n'a encore parlé à un vrai onduleur ou à une vraie batterie.",
      "ui": "Le panneau web a été essayé dans un navigateur contre une simulation du nœud, pas sur une carte.",
      "hardware": "Aucune carte construite ni onduleur ou batterie connectés : rien n'a encore tourné sur de vrais équipements.",
      "security": "Le code de configuration, la connexion avec une limite de mots de passe erronés, le PIN Bluetooth et les mises à jour signées sont testés sur l'hôte ; il n'y a pas eu de revue indépendante.",
      "updates": "Les contrôles de hash et de signature Ed25519 et la logique de retour arrière réussissent sur l'hôte ; une mise à jour par voie hertzienne n'a jamais été exécutée sur une carte.",
      "writing": "L'écriture sur les batteries Pylontech est désactivée par défaut et n'a été testée que contre un simulateur.",
      "integration": "Les messages du nœud sont validés par rapport aux schémas partagés et aux vecteurs de conformité d'ARMOR-COMMON. Son client MQTT est joué contre un vrai Mosquitto dans les tests ; aucune carte ne les a encore envoyés à un serveur.",
      "docs": "Huit langues, le guide du firmware, les notes de câblage et le journal des modifications sont à jour.",
    },
    "docs": [
      "[Firmware du nœud](docs/NODE_FIRMWARE.md) : la carte, les ports, le premier démarrage et la liste de contrôle du banc",
      "[Câblage](docs/NODE_HARDWARE.md), [protocoles](docs/PROTOCOLS.md) et [messages](docs/SOLAR_MESSAGES.md)",
      "[Maintenance des batteries](docs/BATTERY_MAINTENANCE.md) et son [plan d'essais de banc](docs/BATTERY_BENCH_TEST_PLAN.md)",
      "[Menus de Studio](docs/STUDIO_MENUS.md), [essais de banc](docs/BENCH_TESTS.md), [code de configuration](docs/SETUP_CODE.md) et [mise en service Bluetooth](docs/BLE_PROVISIONING.md)",
    ],
    "contributing_first": "Avant une pull request, lancez `ctest --test-dir build/host` and `python -I tools/armor_ci_validate.py` : il doit réussir. Voir [CONTRIBUTING.md](CONTRIBUTING.md) et le [code de conduite](CODE_OF_CONDUCT.md).",
    "languages_extra": "",
    "body": {
      "overview": r"""* **Deux cartes, un firmware :** une ESP32-S3-WROOM-1 N16R8 en Wi-Fi (par défaut) et la Waveshare ESP32-S3-ETH sur son câble Ethernet (DHCP ou adresse fixe ; son propre réseau Wi-Fi est conservé pour la joindre depuis un téléphone). L'image se choisit à la compilation (`tools/build_node.sh generic s3-wifi` ou `generic s3-eth`) ; la table des broches, les broches par défaut des ports et l'accès suivent la carte, et une image ne vaut que pour sa carte. Les deux compilent et sont testées sur ordinateur ; aucune n'a tourné sur une carte.
* **Le firmware du nœud** (ESP32-S3-WROOM-1 N16R8 en Wi-Fi, ou Waveshare ESP32-S3-ETH sur câble) : dix ports série, trois UART matériels et sept émulés (jusqu'à 19200 bauds), chacun indépendant et lisant un onduleur, une batterie ou un moniteur brut, si bien qu'un nœud peut lire seulement des onduleurs, seulement des batteries ou un mélange.
* **Le panneau web du nœud,** celui des nœuds radar aussi : configuration avec un code affiché sur la console USB, connexion et utilisateurs, Wi-Fi (station et point d'accès), broker, mise à jour par radio avec retour arrière, journal, HTTPS, et les pages des ports (avec ce que chacun entend, pour les protocoles pas encore décodés) et des relevés, en huit langues.
* **Onduleurs Voltronic / MPP Solar** (Axpert, PIP, InfiniSolar et clones), RS232 à 2400 bauds : les trames et leur CRC, et les relevés `QPIGS` (réseau, sortie, batterie, PV, bits d'état), `QMOD` (mode), `QPIWS` (avertissements et pannes par nom) et `QPIRI` (valeurs nominales). Seules les commandes de lecture peuvent être construites : un réglage change la façon dont la maison est alimentée. Trois dialectes, choisis sur le port ou trouvés par lui (*auto*) : PI30, REVO (un autre `QPIGS`, réponses avec somme de contrôle) et PI18 (`^P005GS` : InfiniSolar V, LV5048, SunGoldPower), en lecture seule.
* **Batteries Pylontech** (US2000, US3000, US5000) : le tableau `pwr` de la console (tension, courant, températures et état de charge de chaque module), `bat <n>` (tension et température de chaque cellule) et `info <n>` (modèle, capacité restante et totale, cycles), résumés en une pile avec sa capacité et son énergie totales, et la trame RS485 avec ses deux contrôles. Les formats sont écrits de mémoire de la console publique et peuvent varier selon les firmwares. Les colonnes sont trouvées par les noms de l'en-tête (y compris le format de l'US5000 V2.3 avec ses colonnes Id, MosTempr et SysAlarm.St), la charge restante et l'équilibrage viennent de `bat`, et le modèle, la capacité nominale et les cycles de `info` et `stat`, demandés une fois et gardés une demi-heure.
* **Ce qu'un module Pylontech dit de lui-même :** son modèle et les versions de sa carte et de son logiciel, ses cellules et le courant qu'il admet, les compteurs de sa vie (`stat`), la santé de chaque cellule (`soh`, l'anormale marquée) et l'entrée la plus récente de son journal d'événements, avec les noms des protections tels que la console les imprime. La console ne fait que lire, et un administrateur peut télécharger sous forme de fichier texte ce qu'un port a entendu.
* **Les messages du nœud** (`armor/solar/<nœud>/<appareil>/state`, un par onduleur ou pile de batteries), définis dans ARMOR-COMMON avec schémas et vecteurs de conformité ; ce que produisent les ports est vérifié contre eux.
* **Batteries ANT-BMS** (les cartes noires des packs faits maison, 7S à 32S), UART 3,3 V à 19200 bauds : les deux protocoles de son firmware (le nœud demande dans l'un puis dans l'autre et garde celui qui répond), avec les cellules, les températures, l'état de charge, le courant, les capacités et les états des MOSFET et de l'équilibreur, vérifiés sur des trames capturées sur quatre modèles réels. Lecture seule : ses commandes d'écriture peuvent déconnecter une batterie en charge. Un bouton de la page des ports lit aussi le modèle, la version et les 56 réglages de protection et d'équilibrage du BMS (protocole récent), en lecture seule.
* **Configuration depuis le téléphone en Bluetooth,** le même canal que celui du nœud radar : l'app ARMOR trouve le nœud sous le nom `ARMOR-XXXXXX` et règle son nom, son Wi-Fi, son adresse, son broker et son mode Bluetooth avec les utilisateurs et le code de mise en service du panneau ([le protocole](docs/BLE_PROVISIONING.md)). Il n'écoute que tant que le nœud n'a pas d'utilisateur, sauf réglage contraire. La partie radio n'a jamais tourné sur une carte.
* **La carte de base avec multiplexeurs (le profil *mux*) :** trois UART matériels, chacun derrière un 74HC4052, desservent jusqu'à huit ports en groupes de 4, 2 et 2 qui se relaient sur leur ligne, chaque port avec sa propre vitesse et sa propre polarité, et une LED par port via un 74HC595 ; les cellules d'une grande pile Pylontech peuvent être lues à tour de rôle. Pour un onduleur en dialecte standard, la **seconde entrée photovoltaïque** (`QPIGS2`) et les **unités d'un système en parallèle** (`QPGS`) sont des lectures facultatives. Rien de tout cela n'a tourné sur une carte.
* **Mises à jour par radio signées :** le nœud n'installe depuis GitHub qu'une image dont le SHA-256 correspond et qui porte une signature Ed25519 valide du responsable (la clé publique est dans le firmware, la privée ne quitte jamais le responsable) ; un fichier envoyé à la main par un administrateur dans le panneau reste accepté. Les pages et messages du panneau sont en huit langues.
* **Appairage Bluetooth avec un PIN :** le PIN à six chiffres est dérivé du code de configuration, imprimé sur la console USB et montré à un administrateur dans le panneau ; le téléphone doit le saisir avant de pouvoir écrire les réglages du nœud.
* **Pas encore :** la liaison Bluetooth de l'ANT-BMS (le nœud utilise le câble, le plus stable des deux) et un essai sur une vraie carte avec de vrais équipements.
* **Seule la maison peut utiliser le panneau :** le panneau répond par défaut au réseau privé (ou aux réseaux que son propriétaire indique, comme un VPN), refuse une liste qui exclurait celui qui l'enregistre, compte les mauvais mots de passe par personne et par adresse, et fonctionne derrière le proxy du serveur pour être atteint depuis l'extérieur sans publier le nœud.
* **Inconnu ne veut pas dire aucun :** un onduleur REVO n'a pas de requête d'avertissements, son message porte donc `warnings_known: false` et Studio affiche les avertissements comme inconnus et non comme "aucun".
* **Liaison chiffrée facultative avec le broker (TLS) :** désactivée par défaut, le nœud parle donc MQTT non chiffré comme avant. Un interrupteur et une zone pour le certificat de l'autorité propre à l'installation (PEM, 2 Ko au plus) dans la page Broker lui font se connecter en `mqtts://`, ne faire confiance qu'à cette autorité et vérifier que le certificat du broker a été établi pour l'adresse atteinte ; ce qui n'est pas un seul certificat PEM est refusé. Couvert par des tests sur ordinateur ; la poignée de main n'a pas encore été exécutée sur une carte.
* **Rapport de santé :** environ une fois par minute le nœud publie depuis combien de temps il tourne et pourquoi il a redémarré la dernière fois, sa mémoire libre, sa liaison et son signal Wi-Fi, combien de fois il s'est connecté au broker et la dernière erreur notée (`armor/health/<nœud>`, le contrat `node_health` d'ARMOR-COMMON). Le code qui le construit est partagé par tous les nœuds et testé sur un ordinateur ; il n'a pas tourné sur une carte.
* **Écriture sur les batteries Pylontech (désactivée par défaut) :** uniquement des opérations typées - horloge, compteurs et journaux, redémarrage, capacité, la réinitialisation du niveau de charge, limites et protections, sorties, numéro de série, mémoire externe, firmware par XMODEM-1K et une console expert avec liste de blocage - en deux étapes (préparer, puis exécuter avec un jeton à usage unique), la batterie étant lue avant et après, le mot de passe de service gardé seulement dans le nœud et une console simulée pour les tests. Non essayé sur une vraie batterie : voir le [plan d'essais sur banc](docs/BATTERY_BENCH_TEST_PLAN.md).
* **Commande depuis le serveur :** Studio peut redémarrer le nœud proprement, le mettre en pause jusqu'à une heure (il reprend seul), mettre son travail en veille (sans fin, conservée aux redémarrages, le nœud reste connecté et continue de répondre), le faire se signaler, demander un instantané de diagnostic et le marquer en maintenance (`armor/control/<nœud>/...`, le contrat `node_control` d'ARMOR-COMMON). Chaque ordre se fait en deux temps avec un jeton à usage unique propre à cette opération, seul le serveur peut les écrire sur le broker, et il n'existe ni réinitialisation d'usine, ni effacement, ni sommeil profond. Tant que le nœud est en pause ou en veille, il n'écrit dans aucune batterie (une opération en cours peut encore être annulée) et continue de lire onduleurs et batteries. Le code est partagé par tous les nœuds et testé sur un ordinateur ; il n'a pas tourné sur une carte.
* **Les valeurs absurdes sont nommées, pas cachées :** quand un onduleur envoie un nombre impossible, le nœud le retient à la limite du contrat et le nomme dans `clamped`, si bien que le serveur l'affiche comme non réel ; et le vidage brut d'un port n'est produit que pendant que le panneau le regarde.
* **Diagnostic sans câble :** après un démarrage qui n'était pas propre (plantage, chien de garde, chute d'alimentation, allocation échouée), le rapport de santé en donne la raison pendant dix minutes ; un plantage laisse son vidage mémoire (core dump) à consulter, télécharger ou effacer depuis le panneau ; les réglages enregistrés sont copiés avant chaque installation de micrologiciel et récupérés si une mise à jour les abîme ; et un administrateur peut demander au nœud, via le serveur, un paquet de diagnostic ou son journal avec un jeton à usage unique.
* **Scellement facultatif des secrets enregistrés :** désactivé par défaut (`security.seal_secrets`, ou `nodes.nvs_encryption` du serveur). Activé, les mots de passe, jetons, clés, codes PIN et empreintes de mots de passe que le nœud enregistre sont scellés avec ChaCha20-Poly1305 et tout le reste reste lisible ; l'activer ou le désactiver les réécrit sans rien perdre, même si le nœud s'arrête en route. Aucun eFuse n'est brûlé et la flash n'est pas chiffrée : la clé est dans une partition de la même puce, donc cela ne protège **pas** contre quelqu'un qui tient la carte, et un nœud installé avant cette partition garde ses secrets tels quels jusqu'à ce qu'il soit flashé avec la nouvelle table de partitions.""",
      "role": r"""ARMOR-NODE-SOLAR est la passerelle entre le matériel solaire de la maison et la famille. Il lit onduleurs et batteries par jusqu'à dix ports série et publie ce qu'il lit pour [ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER), qui garde l'historique, les totaux et les alarmes ; les menus *Onduleurs* et *Batteries* d'[ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) et l'écran Solaire d'[ARMOR-ANDROID-CONTROL](https://github.com/JuanenRac/ARMOR-ANDROID-CONTROL) le montrent. Il ne fait que lire : il n'écrit jamais un réglage dans un équipement.

| Nom | Comment | À quoi ça sert |
|---|---|---|
| ARMOR-SERVER | MQTT `armor/solar/<node>/<device>/state` | Reçoit un message par onduleur ou pile de batteries ; commande la maintenance d'une batterie |
| ARMOR-STUDIO | menus, lien vers le panneau | Montre onduleurs et batteries et ouvre le panneau du nœud |
| ARMOR-ANDROID-CONTROL | Bluetooth | Configure le nœud sur le terrain et montre les écrans d'énergie |
| ARMOR-COMMON | contrat solaire | Les messages sont vérifiés avec ses schémas ; le firmware commun en est copié |""",
      "architecture": r"""<p align="center">
  <img src="images/architecture.svg" alt="Architecture de ARMOR-NODE-SOLAR : qui l'appelle, ce qu'il contient et de quoi il dépend" width="100%">
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
| Une batterie écrite par erreur ou par un attaquant | Trois verrous : le réglage du nœud `battery.write_enabled` (administrateurs) avec le mot de passe de service de la batterie, `ARMOR_BATTERY_WRITE=1` du serveur, et la liste d'accès du broker pour `armor/solar/<nœud>/maintenance/command` et `.../result` |
| Un ordre d'écriture répété ou volé | Deux étapes (armer, puis exécuter avec un jeton à usage unique), fenêtre d'armement de 120 s, 30 s de refroidissement entre écritures sur un port, 3 échecs en 10 minutes le bloquent 5 ; le numéro de série de la batterie est ressaisi, la batterie doit être au repos et sans alarme critique, et l'image de firmware est gardée 30 minutes et vérifiée |
| Écrire sur un onduleur ou un ANT-BMS | Les commandes d'écriture d'un onduleur (un réglage change l'alimentation de la maison) et d'un ANT-BMS (il peut déconnecter une batterie sous charge) ne peuvent même pas être construites |
| Des nombres absurdes présentés comme réels | Une valeur impossible est retenue à la limite du contrat et nommée dans `clamped`, pour que le serveur l'affiche comme non réelle ; un onduleur REVO n'a pas de requête d'avertissements, son message dit donc `warnings_known: false` au lieu d'affirmer l'absence d'avertissements |

Aucune trame n'a été lue d'un vrai onduleur ou d'une vraie batterie ; les formats sont écrits d'après des documents publics et de mémoire, et les trames ANT-BMS des tests ont été capturées par d'autres personnes. Lisez [docs/BATTERY_MAINTENANCE.md](docs/BATTERY_MAINTENANCE.md) et [SECURITY.md](SECURITY.md).""",
      "interfaces": r"""| Partie | Ce qu'elle règle |
|---|---|
| MQTT | `armor/solar/<nœud>/<appareil>/state` (un message par onduleur ou pile de batteries, type `inverter` ou `battery` du contrat d'ARMOR-COMMON), `armor/solar/<nœud>/maintenance/{command,result}`, `armor/health/<nœud>` (testament), `armor/control/<id>/{command,result,maintenance}` et `armor/control/all/command` |
| Ports | 10 ports série (3 UART matérielles et 7 émulées, jusqu'à 19200 bauds en émulation) ; par port un type : `voltronic` (2400 bauds, toutes les 5 s), `pylontech` (115200, toutes les 10 s), `ant` (19200, toutes les 5 s) ou `raw` (9600, écoute seule, ne publie rien) ; dialectes d'onduleur `auto`, `pi30`, `revo`, `pi18` ; le profil mux a 3 groupes de ports |
| Requêtes | Voltronic : `QPIGS`, `QMOD`, `QPIWS`, `QPIRI` (et `QPIGS2`, `QPGS` sur un onduleur standard avec le mux) ; console Pylontech : `pwr`, `bat <n>`, `info <n>`, `stat`, `soh`, journal d'événements, jusqu'à 8 modules interrogés cellule par cellule |
| Panneau | Les routes de la famille (`tests/check_routes.py` vérifie que toute route appelée par le panneau existe) plus les pages des ports et des mesures ; 51 codes d'erreur avec texte en huit langues (772 lignes dans `panel/text.js`) ; les menus de Studio sont dans [docs/STUDIO_MENUS.md](docs/STUDIO_MENUS.md) |""",
      "configuration": r"""| Variable | Par défaut | Ce qu'elle règle |
|---|---|---|
| `enabled`, `kind`, `name`, `baud`, `rx`, `tx`, `de`, `poll_s`, `modules`, `dialect` | - | Les réglages de chaque port : activé ou non, le type, le nom de l'appareil dans le topic, la vitesse (0 = celle du type), les broches (et la broche DE/RE d'un RS485), la période d'interrogation (0 = celle du type), le nombre de modules et le dialecte de l'onduleur ; au plus 3 réseaux de secours et 2 brokers de secours |
| `battery.write_enabled` | off | Le verrou du nœud pour écrire sur une batterie Pylontech (administrateurs, avec le mot de passe de service de la batterie, qui ne quitte jamais le nœud) |
| `CONFIG_ARMOR_BOARD_S3_WIFI` / `_S3_ETH` | wifi | La carte : ESP32-S3-WROOM-1 N16R8 en Wi-Fi (par défaut) ou la Waveshare ESP32-S3-ETH |
| `CONFIG_ARMOR_NODE_ID`, `_SETUP_CODE`, `_FLEET_SECRET`, `_MQTT_*`, `_HEARTBEAT_S`, `_BLE_SETUP_MINUTES`, `_BOOT_FACTORY_RESET` | - | Les réglages que tous les nœuds partagent : le nom (vide donne `armor-` et les derniers octets de la MAC), le code de configuration (vide : aléatoire), le secret de flotte (16+ caractères, jamais dans le dépôt), les premiers réglages du broker, le battement (de 2 à 300 s), les minutes de configuration Bluetooth (de 1 à 120) et la réinitialisation avec BOOT (8 s dans les 30 premières s) |""",
      "quickstart": r"""**Prérequis:** un compilateur C++17 pour les tests sur hôte ; le conteneur ESP-IDF 5.5.5 pour construire l'image ; une ESP32-S3-WROOM-1 N16R8 ou une Waveshare ESP32-S3-ETH.

```bash
cmake -S tests -B build/host && cmake --build build/host && ctest --test-dir build/host   # host tests, -Werror
build/host/emit_poller_samples | python tests/check_samples.py   # what the ports make is accepted by ARMOR-COMMON
tools/build_node.sh generic                       # the image for the N16R8 board in the ESP-IDF container: dist/generic-s3-wifi.bin
tools/build_node.sh generic s3-eth               # the same firmware for the Waveshare ESP32-S3-ETH (Ethernet): dist/generic-s3-eth.bin
node tools/panel_mock.mjs --user admin:adminpass123   # the panel without a board
```

Voir le [guide du firmware](docs/NODE_FIRMWARE.md) (la carte, les ports, le premier démarrage et la liste d'essais sur banc) et les [notes de câblage](docs/NODE_HARDWARE.md).""",
      "testing": r"""```bash
cmake -S tests -B build/host && cmake --build build/host && ctest --test-dir build/host
python -I tools/armor_ci_validate.py
```

18 programmes de test sur hôte et 6 contrôles Python tournent sous `ctest` ; 11824 vérifications comptées par les programmes hôte, compilés avec `-Werror`.

Contrôles Python : les textes du panneau en huit langues, les tâches, les chemins de sauvegarde, la session Bluetooth sous son verrou et les routes appelées par le panneau (et, dans certains nœuds, les codes HTTP ou les glyphes des polices)

Les tests sur hôte demandent un compilateur C++17 quelconque (Linux, WSL, MSYS2) ; le panneau web est aussi exercé dans un vrai navigateur contre un nœud de substitution (`tools/panel_mock.mjs`, `tools/panel_browser_test.mjs`).

`test_clock` n'imprime que `ok` et n'a pas de compteur ; chaque autre programme rapporte ses vérifications. Les vraies trames des tests sont dans `tests/pylontech_real.hpp`, `pylontech_us2000_real.hpp`, `pylontech_logs_real.hpp`, `ant_frames.hpp` et `battery_bench.hpp`.""",
      "build": "`tools/build_node.sh` construit l'image dans le conteneur ESP-IDF 5.5.5 et la version porte l'image, son SHA-256 et sa signature Ed25519, une par carte ; l'image est écrite par USB-C la première fois, puis mise à jour depuis le panneau.",
      "troubleshooting": r"""| Vous voyez | Parce que | Faites |
|---|---|---|
| Vous avez perdu le mot de passe ou le nœud ne rejoint plus le réseau | Un nœud en configuration sans adresse après 90 s ouvre son propre Wi-Fi `ARMOR-SETUP-xxxxxx` (ouvrez `http://192.168.4.1/`) | Pour recommencer, maintenez BOOT 8 secondes dans les 30 premières secondes après la mise sous tension (efface réglages et utilisateurs), ou utilisez *Réinitialisation d'usine* dans le panneau |
| Une mise à jour depuis GitHub est refusée | La version n'a ni somme de contrôle ni signature, elles ne concordent pas (`e_no_checksum`, `e_no_signature`, `e_checksum_mismatch`, `e_bad_signature`), n'a pas d'image pour cette carte (`e_no_asset_for_board`) ou est d'un autre projet (`e_wrong_firmware`) | Le nœud n'a pas changé ; réessayez ou laissez un administrateur envoyer le fichier à la main |
| Une écriture vers une batterie est refusée avec un code | `serial_mismatch`, `not_pylontech`, `no_battery`, `unknown_model`, `not_idle`, `critical_alarm`, `busy`, `cooldown`, `locked`, `not_armed`, `bad_token`, `expired`, `disabled`, `image_missing`, `image_mismatch`... : le nœud refuse ce qui n'est pas exactement l'opération armée | Lisez le code du résultat, corrigez la cause et armez de nouveau l'opération (voir [docs/BATTERY_MAINTENANCE.md](docs/BATTERY_MAINTENANCE.md)) |
| Un port ne publie rien | Le port est désactivé, son type est `raw` (écoute seule), la vitesse ou les broches ne correspondent pas à l'équipement, ou l'équipement ne répond pas | Vérifiez les réglages du port et le câblage dans [docs/NODE_HARDWARE.md](docs/NODE_HARDWARE.md) ; le panneau montre le vidage brut d'un port pendant qu'il le regarde |""",
      "structure": r"""<p align="center">
  <img src="images/repository-structure.svg" alt="Structure du dépôt de ARMOR-NODE-SOLAR" width="100%">
</p>

<details>
<summary>Version texte de l'arborescence</summary>

```text
ARMOR-NODE-SOLAR/
├── main/                                le firmware : un composant ESP-IDF
├── core/                                la logique sans ESP-IDF, testée sur ordinateur
├── panel/                               le panneau web intégré au firmware
├── tests/                               tests sur hôte et contrôles Python
├── docs/                                10 guides : protocoles, messages, maintenance, matériel
├── tools/                               outils de build, d'empaquetage et de contrôle
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
├── sdkconfig.board.s3-eth               les réglages d'une carte
├── sdkconfig.board.s3-wifi              les réglages d'une carte
├── secrets/                             exemple du fichier de nœud (les vrais ne sont pas versionnés)
├── build-test.sh build-test.bat         lancer les tests par le flux partagé
└── .gitattributes .gitignore            réglages Git
```

</details>""",
      "roadmap": r"""**Limites connues aujourd'hui**

* Les trames, sommes de contrôle et lectures de Voltronic, Pylontech et ANT-BMS sont vérifiées par rapport aux trames documentées et à des échantillons enregistrés ; aucun n'a encore parlé à un vrai onduleur ou à une vraie batterie.
* Le panneau web a été essayé dans un navigateur contre une simulation du nœud, pas sur une carte.
* Aucune carte construite ni onduleur ou batterie connectés : rien n'a encore tourné sur de vrais équipements.
* Le code de configuration, la connexion avec une limite de mots de passe erronés, le PIN Bluetooth et les mises à jour signées sont testés sur l'hôte ; il n'y a pas eu de revue indépendante.
* Les contrôles de hash et de signature Ed25519 et la logique de retour arrière réussissent sur l'hôte ; une mise à jour par voie hertzienne n'a jamais été exécutée sur une carte.
* L'écriture sur les batteries Pylontech est désactivée par défaut et n'a été testée que contre un simulateur.

**Ensuite**

* Faire tourner le nœud sur une vraie carte avec un vrai onduleur et de vraies batteries, puis le lien Bluetooth de l'ANT-BMS (le câble est utilisé aujourd'hui), la mise à jour par voie aérienne et les écritures vers une batterie.""",
    },
  },
  "it": {
    "tagline": "Nodo gateway solare: legge inverter e batterie da fino a dieci porte seriali (firmware ESP32-S3, il suo pannello web e la libreria dei protocolli)",
    "honest": "Il firmware si compila nel contenitore ESP-IDF 5.5.5, il suo nucleo (le impostazioni, lo scambio con ogni tipo di apparecchio, l'aritmetica dell'UART emulata, il canale Bluetooth, i controlli di versione e firma: 11.824 controlli in 18 programmi di test) è provato su un computer con apparecchi sostitutivi, i messaggi che produce sono accettati da ARMOR-COMMON e il pannello è stato esercitato in un browser contro un nodo sostitutivo. **Non ha mai girato su una scheda e nessun inverter o batteria è stato collegato**: il Wi-Fi, il pannello su TLS, l'aggiornamento, le UART hardware ed emulate e i formati dei protocolli (scritti da documenti pubblici e a memoria) non sono provati. I frame ANT-BMS dei suoi test sono stati catturati da altre persone sulle loro unità: questo progetto non ne ha letto nessuno di persona.",
    "glance": [
      [
        "Ruolo",
        "Nodo di campo solare per ESP32-S3: inverter e batterie (famiglia: Field Nodes, padre: ARMOR-COMMON)",
      ],
      [
        "Tecnologia",
        "C++17, ESP-IDF 5.5.5, ESP32-S3",
      ],
      [
        "Test",
        "11824 verifiche in 18 programmi host e 6 verifiche Python (`ctest`)",
      ],
      [
        "Apparecchiature",
        "Inverter Voltronic / MPP Solar, batterie Pylontech, ANT-BMS; 10 porte seriali",
      ],
      [
        "Gira su",
        "ESP32-S3-WROOM-1 N16R8 o Waveshare ESP32-S3-ETH; test su host su qualsiasi computer",
      ],
      [
        "Su hardware reale",
        "Ancora nessuno: nessuna scheda montata né inverter o batteria collegati (solo test su computer, la compilazione e il pannello in un browser)",
      ],
      [
        "Licenza",
        "GPL-3.0-or-later",
      ],
    ],
    "status": {
      "software": "Il firmware compila nel contenitore ESP-IDF 5.5.5 per entrambe le schede (Wi-Fi ed Ethernet).",
      "tests": "Superano 11.824 controlli in 18 programmi host (`ctest`): le impostazioni, lo scambio con ogni tipo di apparecchiatura, la UART emulata, il canale Bluetooth e i controlli di versione.",
      "protocols": "I frame, i checksum e le letture di Voltronic, Pylontech e ANT-BMS sono verificati contro i frame documentati e campioni registrati; nessuno ha ancora parlato con un inverter o una batteria reali.",
      "ui": "Il pannello web è stato provato in un browser contro una simulazione del nodo, non su una scheda.",
      "hardware": "Nessuna scheda costruita e nessun inverter o batteria collegati: nulla ha ancora funzionato su apparecchiature reali.",
      "security": "Il codice di configurazione, l'accesso con limite di password errate, il PIN Bluetooth e gli aggiornamenti firmati sono testati sull'host; non c'è stata una revisione indipendente.",
      "updates": "I controlli di hash e firma Ed25519 e la logica di ripristino passano sull'host; un aggiornamento via etere non è mai stato eseguito su una scheda.",
      "writing": "La scrittura sulle batterie Pylontech è disattivata per impostazione predefinita ed è stata provata solo contro un simulatore.",
      "integration": "I messaggi del nodo sono validati contro gli schemi condivisi e i vettori di conformità di ARMOR-COMMON. Il suo client MQTT viene provato contro un vero Mosquitto nei test; nessuna scheda li ha ancora inviati a un server.",
      "docs": "Otto lingue, la guida del firmware, le note di cablaggio e il registro delle modifiche sono aggiornati.",
    },
    "docs": [
      "[Firmware del nodo](docs/NODE_FIRMWARE.md): la scheda, le porte, il primo avvio e la lista di controllo del banco",
      "[Cablaggio](docs/NODE_HARDWARE.md), [protocolli](docs/PROTOCOLS.md) e [messaggi](docs/SOLAR_MESSAGES.md)",
      "[Manutenzione delle batterie](docs/BATTERY_MAINTENANCE.md) e il suo [piano di prove al banco](docs/BATTERY_BENCH_TEST_PLAN.md)",
      "[Menu di Studio](docs/STUDIO_MENUS.md), [prove al banco](docs/BENCH_TESTS.md), [codice di configurazione](docs/SETUP_CODE.md) e [provisioning Bluetooth](docs/BLE_PROVISIONING.md)",
    ],
    "contributing_first": "Prima di una pull request esegui `ctest --test-dir build/host` and `python -I tools/armor_ci_validate.py`: deve passare. Vedi [CONTRIBUTING.md](CONTRIBUTING.md) e il [codice di condotta](CODE_OF_CONDUCT.md).",
    "languages_extra": "",
    "body": {
      "overview": r"""* **Due schede, un solo firmware:** una ESP32-S3-WROOM-1 N16R8 via Wi-Fi (predefinita) e la Waveshare ESP32-S3-ETH sul suo cavo Ethernet (DHCP o indirizzo fisso; tiene la propria rete Wi-Fi per raggiungerla da un telefono). L'immagine si sceglie in compilazione (`tools/build_node.sh generic s3-wifi` o `generic s3-eth`); la tabella dei pin, i pin predefiniti delle porte e l'accesso seguono la scheda, e un'immagine vale solo per la sua scheda. Entrambe compilano e sono testate sul computer; nessuna ha girato su una scheda.
* **Il firmware del nodo** (ESP32-S3-WROOM-1 N16R8 via Wi-Fi, o Waveshare ESP32-S3-ETH via cavo): dieci porte seriali, tre UART hardware e sette emulate (fino a 19200 baud), ognuna indipendente e ognuna legge un inverter, una batteria o un monitor grezzo, così un nodo può leggere solo inverter, solo batterie o un misto.
* **Il pannello web del nodo,** lo stesso dei nodi radar: configurazione con un codice mostrato sulla console USB, accesso e utenti, Wi-Fi (stazione e punto di accesso), broker, aggiornamento via radio con ripristino, registro, HTTPS, e le pagine delle porte (con ciò che ognuna sente, per protocolli non ancora decodificati) e delle letture, in otto lingue.
* **Inverter Voltronic / MPP Solar** (Axpert, PIP, InfiniSolar e cloni), RS232 a 2400 baud: i frame e il loro CRC, e le letture `QPIGS` (rete, uscita, batteria, FV, bit di stato), `QMOD` (modo), `QPIWS` (avvisi e guasti per nome) e `QPIRI` (valori nominali). Si possono costruire solo comandi di lettura: un'impostazione cambia come viene alimentata la casa. Tre dialetti, scelti sulla porta o trovati da essa (*auto*): PI30, REVO (un altro `QPIGS`, risposte con checksum) e PI18 (`^P005GS`: InfiniSolar V, LV5048, SunGoldPower), sola lettura.
* **Batterie Pylontech** (US2000, US3000, US5000): la tabella `pwr` della console (tensione, corrente, temperature e stato di carica di ogni modulo), `bat <n>` (tensione e temperatura di ogni cella) e `info <n>` (modello, capacità residua e totale, cicli), riassunte come un unico pacco con capacità ed energia totali, e il frame RS485 con i suoi due controlli. I formati sono scritti a memoria dalla console pubblica e possono variare tra i firmware. Le colonne si trovano dai nomi dell'intestazione (anche il formato della US5000 V2.3 con le colonne Id, MosTempr e SysAlarm.St), la carica residua e il bilanciamento vengono da `bat`, e modello, capacità nominale e cicli da `info` e `stat`, richiesti una volta e conservati mezz'ora.
* **Cosa dice di sé un modulo Pylontech:** il suo modello e le versioni della sua scheda e del suo software, le sue celle e la corrente che ammette, i contatori della sua vita (`stat`), la salute di ogni cella (`soh`, con quella anomala segnata) e la voce più recente del suo registro eventi, con i nomi delle protezioni come li stampa la console. La console si limita a leggere, e un amministratore può scaricare come file di testo ciò che una porta ha sentito.
* **I messaggi del nodo** (`armor/solar/<nodo>/<dispositivo>/state`, uno per inverter o pacco di batterie), definiti in ARMOR-COMMON con schemi e vettori di conformità; ciò che producono le porte è verificato contro di essi.
* **Batterie ANT-BMS** (le schede nere dei pacchi autocostruiti, da 7S a 32S), UART a 3,3 V a 19200 baud: entrambi i protocolli del suo firmware (il nodo chiede nell'uno e poi nell'altro e resta con quello che risponde), con celle, temperature, stato di carica, corrente, capacità e stati dei MOSFET e del bilanciatore, verificati su frame catturati su quattro modelli reali. Solo lettura: i suoi comandi di scrittura possono scollegare una batteria sotto carico. Un pulsante della pagina delle porte legge anche modello, versione e le 56 impostazioni di protezione e bilanciamento del BMS (protocollo nuovo), in sola lettura.
* **Configurazione dal telefono via Bluetooth,** lo stesso canale del nodo radar: l'app ARMOR trova il nodo come `ARMOR-XXXXXX` e ne imposta nome, Wi-Fi, indirizzo, broker e modo Bluetooth con gli utenti e il codice di messa in servizio del pannello ([il protocollo](docs/BLE_PROVISIONING.md)). Ascolta solo finché il nodo non ha utenti, salvo diversa impostazione. La parte radio non ha mai girato su una scheda.
* **La scheda base con multiplexer (il profilo *mux*):** tre UART hardware, ciascuna dietro un 74HC4052, servono fino a otto porte in gruppi da 4, 2 e 2 che si alternano sulla loro linea, ogni porta con la propria velocità e polarità, e un LED per porta tramite un 74HC595; le celle di una pila Pylontech alta si possono leggere a rotazione. Per un inverter nel dialetto standard, il **secondo ingresso fotovoltaico** (`QPIGS2`) e le **unità di un sistema in parallelo** (`QPGS`) sono letture facoltative. Nulla di tutto ciò ha mai girato su una scheda.
* **Aggiornamenti via etere firmati:** il nodo installa da GitHub solo un'immagine il cui SHA-256 coincide e che porta una firma Ed25519 valida del responsabile (la chiave pubblica è nel firmware, quella privata non lascia mai il responsabile); un file caricato a mano da un amministratore nel pannello resta accettato. Le pagine e i messaggi del pannello sono in otto lingue.
* **Abbinamento Bluetooth con PIN:** il PIN a sei cifre deriva dal codice di configurazione, è stampato sulla console USB e mostrato a un amministratore nel pannello; il telefono deve inserirlo prima di poter scrivere le impostazioni del nodo.
* **Non ancora:** il collegamento Bluetooth dell'ANT-BMS (il nodo usa il cavo, il più stabile dei due) e una prova su una scheda reale con dispositivi reali.
* **Solo la casa può usare il pannello:** il pannello risponde per impostazione predefinita alla rete privata (o alle reti indicate dal proprietario, come una VPN), rifiuta un elenco che escluderebbe chi lo salva, conta le password errate per persona e per indirizzo e funziona dietro il proxy del server per essere raggiunto da fuori casa senza pubblicare il nodo.
* **Sconosciuto non è nessuno:** un inverter REVO non ha una richiesta degli avvisi, quindi il suo messaggio porta `warnings_known: false` e Studio mostra gli avvisi come sconosciuti invece di "nessuno".
* **Collegamento cifrato facoltativo con il broker (TLS):** disattivato per impostazione predefinita, quindi il nodo parla MQTT non cifrato come prima. Un interruttore e una casella per il certificato dell'autorità propria dell'installazione (PEM, al massimo 2 KB) nella pagina Broker lo fanno collegare con `mqtts://`, fidarsi solo di quell'autorità e verificare che il certificato del broker sia stato fatto per l'indirizzo raggiunto; ciò che non è un solo certificato PEM viene rifiutato. Coperto da test sul computer; l'handshake non è ancora stato eseguito su una scheda.
* **Rapporto di salute:** circa una volta al minuto il nodo pubblica da quanto è acceso e perché si è riavviato l'ultima volta, la memoria libera, il collegamento e il segnale Wi-Fi, quante volte si è connesso al broker e l'ultimo errore registrato (`armor/health/<nodo>`, il contratto `node_health` di ARMOR-COMMON). Il codice che lo costruisce è condiviso da tutti i nodi e testato su un computer; non è mai girato su una scheda.
* **Scrittura sulle batterie Pylontech (disattivata di default):** solo operazioni tipizzate - orologio, contatori e registri, riavvio, capacità, il ripristino del livello di carica, limiti e protezioni, uscite, numero di serie, memoria esterna, firmware via XMODEM-1K e una console esperto con lista di blocco - in due passi (prepara, poi esegui con un token monouso), leggendo la batteria prima e dopo, con la password di servizio conservata solo nel nodo e una console simulata per i test. Non provato su una batteria reale: vedi il [piano di prove al banco](docs/BATTERY_BENCH_TEST_PLAN.md).
* **Controllo dal server:** Studio può riavviare il nodo in modo pulito, metterlo in pausa fino a un'ora (riprende da solo), mettere il suo lavoro in standby (senza fine, conservato ai riavvii, il nodo resta connesso e continua a rispondere), farlo mostrare, chiedere un'istantanea diagnostica e segnarlo in manutenzione (`armor/control/<nodo>/...`, il contratto `node_control` di ARMOR-COMMON). Ogni ordine è in due passi con un token monouso legato a quell'operazione, solo il server può scriverli sul broker e non esistono ripristino di fabbrica, cancellazione né sonno profondo. Finché il nodo è in pausa o in standby non scrive su nessuna batteria (un'operazione in corso si può ancora annullare) e continua a leggere inverter e batterie. Il codice è condiviso da tutti i nodi e provato su un computer; non ha ancora girato su una scheda.
* **I valori assurdi sono nominati, non nascosti:** quando un inverter invia un numero impossibile, il nodo lo trattiene al limite del contratto e lo nomina in `clamped`, così il server lo mostra come non reale; e il dump grezzo di una porta viene prodotto solo mentre il pannello lo sta guardando.
* **Diagnostica senza cavo:** dopo un avvio non pulito (un blocco, un watchdog, un calo di alimentazione, un'allocazione fallita) il rapporto di salute ne indica la causa per dieci minuti; un arresto anomalo lascia il suo core dump da vedere, scaricare o cancellare dal pannello; le impostazioni salvate vengono copiate prima di ogni installazione del firmware e recuperate se un aggiornamento le danneggia; e un amministratore può chiedere al nodo, tramite il server, un pacchetto di diagnostica o il suo registro con un token monouso.
* **Sigillatura facoltativa dei segreti salvati:** disattivata per impostazione predefinita (`security.seal_secrets`, o `nodes.nvs_encryption` del server). Attiva, le password, i token, le chiavi, i PIN e gli hash delle password che il nodo salva restano sigillati con ChaCha20-Poly1305 e tutto il resto resta leggibile; attivarla o disattivarla li riscrive senza perdere nulla, anche se il nodo si ferma a metà. Nessun eFuse viene bruciato e la flash non è cifrata: la chiave si trova in una partizione dello stesso chip, quindi **non** protegge da chi ha la scheda, e un nodo installato prima di quella partizione mantiene i suoi segreti com'erano finché non viene flashato con la nuova tabella delle partizioni.""",
      "role": r"""ARMOR-NODE-SOLAR è il gateway fra gli apparecchi solari della casa e la famiglia. Legge inverter e batterie attraverso fino a dieci porte seriali e pubblica ciò che legge per [ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER), che conserva lo storico, i totali e gli allarmi; i menu *Inverter* e *Batterie* di [ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) e la schermata Solare di [ARMOR-ANDROID-CONTROL](https://github.com/JuanenRac/ARMOR-ANDROID-CONTROL) lo mostrano. Si limita a leggere: non scrive mai un'impostazione in nessun apparecchio.

| Nome | Come | A cosa serve |
|---|---|---|
| ARMOR-SERVER | MQTT `armor/solar/<node>/<device>/state` | Riceve un messaggio per inverter o pila di batterie; ordina la manutenzione di una batteria |
| ARMOR-STUDIO | menu, collegamento al pannello | Mostra inverter e batterie e apre il pannello del nodo |
| ARMOR-ANDROID-CONTROL | Bluetooth | Configura il nodo sul campo e mostra le schermate dell'energia |
| ARMOR-COMMON | contratto solare | I messaggi sono verificati con i suoi schemi; il firmware comune è copiato da lì |""",
      "architecture": r"""<p align="center">
  <img src="images/architecture.svg" alt="Architettura di ARMOR-NODE-SOLAR: chi lo chiama, cosa contiene e da cosa dipende" width="100%">
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
| Una batteria scritta per errore o da un attaccante | Tre serrature: l'impostazione del nodo `battery.write_enabled` (amministratori) con la password di servizio della batteria, `ARMOR_BATTERY_WRITE=1` del server, e la lista di accesso del broker per `armor/solar/<nodo>/maintenance/command` e `.../result` |
| Un ordine di scrittura ripetuto o rubato | Due passi (armare, poi eseguire con un token monouso), finestra di armamento di 120 s, 30 s di raffreddamento tra scritture su una porta, 3 errori in 10 minuti la bloccano per 5; il numero di serie della batteria si digita di nuovo, la batteria deve essere a riposo e senza allarme critico, e l'immagine del firmware è tenuta 30 minuti e verificata |
| Scrivere su un inverter o un ANT-BMS | I comandi di scrittura di un inverter (un'impostazione cambia come è alimentata la casa) e di un ANT-BMS (può scollegare una batteria sotto carico) non si possono nemmeno costruire |
| Numeri assurdi mostrati come reali | Un valore impossibile viene trattenuto al limite del contratto e nominato in `clamped`, così il server lo mostra come non reale; un inverter REVO non ha una richiesta di avvisi, quindi il suo messaggio dice `warnings_known: false` invece di affermare che non ci sono avvisi |

Nessun frame è stato letto da un vero inverter o da una vera batteria; i formati sono scritti da documenti pubblici e a memoria, e i frame ANT-BMS dei test sono stati catturati da altre persone. Leggi [docs/BATTERY_MAINTENANCE.md](docs/BATTERY_MAINTENANCE.md) e [SECURITY.md](SECURITY.md).""",
      "interfaces": r"""| Parte | Cosa imposta |
|---|---|
| MQTT | `armor/solar/<nodo>/<dispositivo>/state` (un messaggio per inverter o pila di batterie, tipo `inverter` o `battery` del contratto di ARMOR-COMMON), `armor/solar/<nodo>/maintenance/{command,result}`, `armor/health/<nodo>` (last will), `armor/control/<id>/{command,result,maintenance}` e `armor/control/all/command` |
| Porte | 10 porte seriali (3 UART hardware e 7 emulate, fino a 19200 baud se emulate); per porta un tipo: `voltronic` (2400 baud, ogni 5 s), `pylontech` (115200, ogni 10 s), `ant` (19200, ogni 5 s) o `raw` (9600, solo ascolto, non pubblica nulla); dialetti dell'inverter `auto`, `pi30`, `revo`, `pi18`; il profilo mux ha 3 gruppi di porte |
| Richieste | Voltronic: `QPIGS`, `QMOD`, `QPIWS`, `QPIRI` (e `QPIGS2`, `QPGS` su un inverter standard con il mux); console Pylontech: `pwr`, `bat <n>`, `info <n>`, `stat`, `soh`, registro eventi, fino a 8 moduli richiesti cella per cella |
| Pannello | I percorsi della famiglia (`tests/check_routes.py` verifica che ogni percorso chiamato dal pannello esista) più le pagine di porte e letture; 51 codici di errore con testo in otto lingue (772 righe in `panel/text.js`); i menu di Studio sono in [docs/STUDIO_MENUS.md](docs/STUDIO_MENUS.md) |""",
      "configuration": r"""| Variabile | Predefinito | Cosa imposta |
|---|---|---|
| `enabled`, `kind`, `name`, `baud`, `rx`, `tx`, `de`, `poll_s`, `modules`, `dialect` | - | Le impostazioni di ogni porta: attiva o no, il tipo, il nome del dispositivo nel topic, la velocità (0 = quella del tipo), i pin (e il pin DE/RE di un RS485), il periodo di interrogazione (0 = quello del tipo), il numero di moduli e il dialetto dell'inverter; al massimo 3 reti di riserva e 2 broker di riserva |
| `battery.write_enabled` | off | La serratura del nodo per scrivere su una batteria Pylontech (amministratori, con la password di servizio della batteria, che non lascia mai il nodo) |
| `CONFIG_ARMOR_BOARD_S3_WIFI` / `_S3_ETH` | wifi | La scheda: ESP32-S3-WROOM-1 N16R8 via Wi-Fi (predefinita) o la Waveshare ESP32-S3-ETH |
| `CONFIG_ARMOR_NODE_ID`, `_SETUP_CODE`, `_FLEET_SECRET`, `_MQTT_*`, `_HEARTBEAT_S`, `_BLE_SETUP_MINUTES`, `_BOOT_FACTORY_RESET` | - | Le impostazioni che tutti i nodi condividono: il nome (vuoto dà `armor-` e gli ultimi byte del MAC), il codice di configurazione (vuoto: casuale), il segreto di flotta (16+ caratteri, mai nel repository), le prime impostazioni del broker, il battito (da 2 a 300 s), i minuti di configurazione Bluetooth (da 1 a 120) e il ripristino con BOOT (8 s nei primi 30 s) |""",
      "quickstart": r"""**Requisiti:** un compilatore C++17 per i test su host; il container ESP-IDF 5.5.5 per costruire l'immagine; una ESP32-S3-WROOM-1 N16R8 o una Waveshare ESP32-S3-ETH.

```bash
cmake -S tests -B build/host && cmake --build build/host && ctest --test-dir build/host   # host tests, -Werror
build/host/emit_poller_samples | python tests/check_samples.py   # what the ports make is accepted by ARMOR-COMMON
tools/build_node.sh generic                       # the image for the N16R8 board in the ESP-IDF container: dist/generic-s3-wifi.bin
tools/build_node.sh generic s3-eth               # the same firmware for the Waveshare ESP32-S3-ETH (Ethernet): dist/generic-s3-eth.bin
node tools/panel_mock.mjs --user admin:adminpass123   # the panel without a board
```

Vedi la [guida al firmware](docs/NODE_FIRMWARE.md) (la scheda, le porte, il primo avvio e l'elenco delle prove da banco) e le [note di cablaggio](docs/NODE_HARDWARE.md).""",
      "testing": r"""```bash
cmake -S tests -B build/host && cmake --build build/host && ctest --test-dir build/host
python -I tools/armor_ci_validate.py
```

18 programmi di test su host e 6 verifiche Python girano con `ctest`; 11824 verifiche contate dai programmi host, compilati con `-Werror`.

Verifiche Python: i testi del pannello in otto lingue, i task, i percorsi di salvataggio, la sessione Bluetooth sotto il suo lock e i percorsi chiamati dal pannello (e, in alcuni nodi, i codici HTTP o i glifi dei caratteri)

I test su host richiedono un qualsiasi compilatore C++17 (Linux, WSL, MSYS2); il pannello web è anche provato in un browser reale contro un nodo sostitutivo (`tools/panel_mock.mjs`, `tools/panel_browser_test.mjs`).

`test_clock` stampa solo `ok` e non ha un contatore; ogni altro programma riporta le sue verifiche. I frame reali dei test sono in `tests/pylontech_real.hpp`, `pylontech_us2000_real.hpp`, `pylontech_logs_real.hpp`, `ant_frames.hpp` e `battery_bench.hpp`.""",
      "build": "`tools/build_node.sh` costruisce l'immagine nel container ESP-IDF 5.5.5 e la versione porta l'immagine, il suo SHA-256 e la sua firma Ed25519, una per scheda; l'immagine si scrive via USB-C la prima volta e poi si aggiorna dal pannello.",
      "troubleshooting": r"""| Vedi | Perché | Fai |
|---|---|---|
| Hai perso la password o il nodo non entra più in rete | Un nodo in configurazione senza indirizzo dopo 90 s apre un proprio Wi-Fi `ARMOR-SETUP-xxxxxx` (apri `http://192.168.4.1/`) | Per ricominciare tieni premuto BOOT per 8 secondi nei primi 30 secondi dopo l'accensione (cancella impostazioni e utenti), o usa *Ripristino di fabbrica* nel pannello |
| Un aggiornamento da GitHub è rifiutato | La versione non ha checksum o firma, non corrispondono (`e_no_checksum`, `e_no_signature`, `e_checksum_mismatch`, `e_bad_signature`), non ha un'immagine per questa scheda (`e_no_asset_for_board`) o è di un altro progetto (`e_wrong_firmware`) | Il nodo non è cambiato; riprova o lascia che un amministratore carichi il file a mano |
| Una scrittura su una batteria è rifiutata con un codice | `serial_mismatch`, `not_pylontech`, `no_battery`, `unknown_model`, `not_idle`, `critical_alarm`, `busy`, `cooldown`, `locked`, `not_armed`, `bad_token`, `expired`, `disabled`, `image_missing`, `image_mismatch`...: il nodo rifiuta ciò che non è esattamente l'operazione armata | Leggi il codice nel risultato, correggi la causa e arma di nuovo l'operazione (vedi [docs/BATTERY_MAINTENANCE.md](docs/BATTERY_MAINTENANCE.md)) |
| Una porta non pubblica nulla | La porta è spenta, il suo tipo è `raw` (solo ascolto), la velocità o i pin non corrispondono all'apparecchio, o l'apparecchio non risponde | Controlla le impostazioni della porta e il cablaggio in [docs/NODE_HARDWARE.md](docs/NODE_HARDWARE.md); il pannello mostra il dump grezzo di una porta mentre la guarda |""",
      "structure": r"""<p align="center">
  <img src="images/repository-structure.svg" alt="Struttura del repository di ARMOR-NODE-SOLAR" width="100%">
</p>

<details>
<summary>Versione testuale dell'albero</summary>

```text
ARMOR-NODE-SOLAR/
├── main/                                il firmware: un componente ESP-IDF
├── core/                                la logica senza ESP-IDF, testata su un computer
├── panel/                               il pannello web incorporato nel firmware
├── tests/                               test su host e verifiche Python
├── docs/                                10 guide: protocolli, messaggi, manutenzione, hardware
├── tools/                               strumenti di build, impacchettamento e verifica
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
├── sdkconfig.board.s3-eth               le impostazioni di una scheda
├── sdkconfig.board.s3-wifi              le impostazioni di una scheda
├── secrets/                             esempio del file del nodo (quelli veri non sono versionati)
├── build-test.sh build-test.bat         eseguire i test tramite il flusso condiviso
└── .gitattributes .gitignore            impostazioni di Git
```

</details>""",
      "roadmap": r"""**Limiti noti oggi**

* I frame, i checksum e le letture di Voltronic, Pylontech e ANT-BMS sono verificati contro i frame documentati e campioni registrati; nessuno ha ancora parlato con un inverter o una batteria reali.
* Il pannello web è stato provato in un browser contro una simulazione del nodo, non su una scheda.
* Nessuna scheda costruita e nessun inverter o batteria collegati: nulla ha ancora funzionato su apparecchiature reali.
* Il codice di configurazione, l'accesso con limite di password errate, il PIN Bluetooth e gli aggiornamenti firmati sono testati sull'host; non c'è stata una revisione indipendente.
* I controlli di hash e firma Ed25519 e la logica di ripristino passano sull'host; un aggiornamento via etere non è mai stato eseguito su una scheda.
* La scrittura sulle batterie Pylontech è disattivata per impostazione predefinita ed è stata provata solo contro un simulatore.

**Prossimi passi**

* Far girare il nodo su una scheda reale con un vero inverter e vere batterie, poi il collegamento Bluetooth dell'ANT-BMS (oggi si usa il cavo), l'aggiornamento via etere e le scritture su una batteria.""",
    },
  },
  "ja": {
    "tagline": "太陽光ゲートウェイノード：最大 10 個のシリアルポートでインバーターとバッテリーを読み取る（ESP32-S3 ファームウェア、その Web パネル、プロトコルライブラリ）",
    "honest": "ファームウェアは ESP-IDF 5.5.5 コンテナーでビルドでき、そのコア（設定、各種機器とのやり取り、エミュレートした UART の計算、Bluetooth チャネル、バージョンと署名の検査：18 のテストプログラムで 9,319 項目）は代替機器を使ってコンピューター上でテストされ、生成するメッセージは ARMOR-COMMON に受け付けられ、パネルは代替ノードに対してブラウザーで動かしました。**基板上で動いたことはなく、インバーターやバッテリーも接続されていません**：Wi-Fi、TLS のパネル、アップデート、ハードウェアとエミュレートした UART、プロトコルの形式（公開資料と記憶から作成）は未検証です。テスト内の ANT-BMS フレームは他の人が自分の機器で取得したもので、このプロジェクト自身はまだ 1 つも読み取っていません。",
    "glance": [
      [
        "役割",
        "ESP32-S3 用ソーラーフィールドノード：インバーターとバッテリー（ファミリー：Field Nodes、親：ARMOR-COMMON）",
      ],
      [
        "技術",
        "C++17, ESP-IDF 5.5.5, ESP32-S3",
      ],
      [
        "テスト",
        "11824 件の検査（ホスト用プログラム 18 本と Python 検査 6 個、`ctest`）",
      ],
      [
        "機器",
        "Voltronic / MPP Solar インバーター、Pylontech バッテリー、ANT-BMS、シリアルポート 10 本",
      ],
      [
        "動作環境",
        "ESP32-S3-WROOM-1 N16R8 または Waveshare ESP32-S3-ETH、ホストテストは任意のコンピューター",
      ],
      [
        "実機での確認",
        "まだありません：基板は未製作で、インバーターやバッテリーも未接続（コンピューター上のテスト、ビルド、ブラウザーでのパネルのみ）",
      ],
      [
        "ライセンス",
        "GPL-3.0-or-later",
      ],
    ],
    "status": {
      "software": "ファームウェアは ESP-IDF 5.5.5 コンテナで両方のボード（Wi-Fi とイーサネット）向けにビルドできます。",
      "tests": "18 のホストプログラムで 11,824 件のチェックが通ります（`ctest`）：設定、各種機器とのやり取り、エミュレートした UART、Bluetooth チャネル、バージョン確認。",
      "protocols": "Voltronic、Pylontech、ANT-BMS のフレーム、チェックサム、読み取り値は、文書化されたフレームと記録したサンプルに対して検証済みです。実際のインバーターやバッテリーとはまだ通信していません。",
      "ui": "Web パネルはブラウザーでノードの模擬に対して試しており、ボード上では試していません。",
      "hardware": "ボードは未製作で、インバーターやバッテリーも接続していません。実機ではまだ何も動かしていません。",
      "security": "設定コード、誤ったパスワードの回数制限付きログイン、Bluetooth の PIN、署名付きアップデートはホストでテスト済みです。独立したレビューはまだありません。",
      "updates": "ハッシュと Ed25519 署名の確認、ロールバックの処理はホストで通ります。無線アップデートはボード上で一度も実行していません。",
      "writing": "Pylontech バッテリーへの書き込みは既定でオフで、シミュレーターに対してのみテストしています。",
      "integration": "ノードのメッセージは ARMOR-COMMON の共有スキーマと適合ベクターに対して検証されています。MQTT クライアントはテストで本物の Mosquitto を相手に動かしていますが、ボードからサーバーへ送ったことはまだありません。",
      "docs": "8 言語、ファームウェアガイド、配線メモ、変更履歴は最新です。",
    },
    "docs": [
      "[ノードのファームウェア](docs/NODE_FIRMWARE.md)：基板、ポート、初回起動、ベンチのチェックリスト",
      "[配線](docs/NODE_HARDWARE.md)、[プロトコル](docs/PROTOCOLS.md)、[メッセージ](docs/SOLAR_MESSAGES.md)",
      "[バッテリー保守](docs/BATTERY_MAINTENANCE.md)と[ベンチテスト計画](docs/BATTERY_BENCH_TEST_PLAN.md)",
      "[Studio のメニュー](docs/STUDIO_MENUS.md)、[ベンチテスト](docs/BENCH_TESTS.md)、[セットアップコード](docs/SETUP_CODE.md)、[Bluetooth プロビジョニング](docs/BLE_PROVISIONING.md)",
    ],
    "contributing_first": "Pull Request の前に `ctest --test-dir build/host` and `python -I tools/armor_ci_validate.py` を実行してください。通る必要があります。[CONTRIBUTING.md](CONTRIBUTING.md) と[行動規範](CODE_OF_CONDUCT.md)を参照してください。",
    "languages_extra": "",
    "body": {
      "overview": r"""* **2 種類のボード、1 つのファームウェア：** Wi-Fi の ESP32-S3-WROOM-1 N16R8（標準）と、Ethernet ケーブルの Waveshare ESP32-S3-ETH（DHCP または固定アドレス。スマートフォンから接続できるよう独自の Wi-Fi ネットワークは残ります）。イメージはビルド時に選びます（`tools/build_node.sh generic s3-wifi` または `generic s3-eth`）。ピン表、ポートの既定ピン、アクセス方法はボードに従い、イメージは対応するボード専用です。どちらもビルドでき、コンピューター上でテスト済みですが、実機では動かしていません。
* **ノードのファームウェア**（Wi-Fi の ESP32-S3-WROOM-1 N16R8、または有線の Waveshare ESP32-S3-ETH）：シリアルポートは 10 個（ハードウェア UART 3 つとエミュレート 7 つ、最大 19200 ボー）。それぞれ独立し、インバーター、バッテリー、ローモニターのいずれかを読むため、ノードはインバーターのみ、バッテリーのみ、または両方を読めます。
* **ノードの Web パネル**（レーダーノードと同じもの）：USB コンソールに表示されるコードによるセットアップ、ログインとユーザー、Wi-Fi（ステーションとアクセスポイント）、ブローカー、ロールバック付きのオーバーザエア更新、ログ、HTTPS、そしてポート（各ポートが受信している内容を表示。未デコードのプロトコル用）と測定値のページ。8 言語対応。
* **Voltronic / MPP Solar インバーター**（Axpert、PIP、InfiniSolar とその互換機）、RS232 2400 ボー：フレームとその CRC、および読み取り値 `QPIGS`（系統、出力、バッテリー、PV、状態ビット）、`QMOD`（モード）、`QPIWS`（名前付きの警告と故障）、`QPIRI`（定格）。組み立てられるのは読み取りコマンドだけです。設定は家への給電方法を変えてしまうからです。3 つの方言（ポートで選ぶか、ポート自身が見つけます＝*auto*）：PI30、REVO（別の配置の `QPIGS`、チェックサムで終わる応答）、PI18（`^P005GS`：InfiniSolar V、LV5048、SunGoldPower）。読み取り専用。
* **Pylontech バッテリー**（US2000、US3000、US5000）：コンソールの `pwr` 表（各モジュールの電圧、電流、温度、充電状態）、`bat <n>`（各セルの電圧と温度）、`info <n>`（型式、残容量と満容量、サイクル数）を、総容量と総エネルギーを持つ 1 つのスタックとして要約し、2 つのチェックを持つ RS485 フレームも扱います。書式は公開されているコンソールの記憶から書いたもので、ファームウェアによって異なる可能性があります。列はヘッダーの名前で見つけます（Id 列、MosTempr、SysAlarm.St を持つ US5000 V2.3 の形式を含みます）。残りの充電量とバランス状態は `bat` から、型式・定格容量・サイクル数は `info` と `stat` から得て、1 回だけ問い合わせて 30 分間保持します。
* **Pylontech モジュールが自分について伝える内容：** モデル、基板とソフトウェアのバージョン、セルと許容電流、寿命のカウンター（`stat`）、各セルの健康状態（`soh`、異常なものに印）、およびイベントログの最新項目を、保護名をコンソールが出力するとおりに表示します。コンソールは読み取り専用で、管理者はポートが受信した内容をテキストファイルとしてダウンロードできます。
* **ノードのメッセージ**（`armor/solar/<ノード>/<デバイス>/state`、インバーターまたはバッテリースタックごとに 1 つ）。ARMOR-COMMON でスキーマと適合性ベクトルとともに定義され、各ポートが作るものはそれに照らして検査されます。
* **ANT-BMS バッテリー**（自作バッテリーパック用の黒い基板、7S～32S）、3.3 V UART・19200 ボー：ファームウェアの 2 種類のプロトコルの両方に対応（ノードは一方で問い合わせ、答えがなければもう一方で問い合わせ、答えたほうを使い続けます）。セル、温度、充電状態、電流、容量、MOSFET とバランサーの状態を読み取り、実機 4 機種で採取されたフレームで検証しています。読み取り専用：書き込みコマンドは負荷のかかった電池を切断しかねません。ポートのページのボタンで BMS の型式、バージョン、保護とバランスの 56 の設定も読み取れます（新しいプロトコル、読み取り専用）。
* **スマートフォンから Bluetooth で設定：** レーダーノードと同じチャンネルです。ARMOR アプリがノードを `ARMOR-XXXXXX` として見つけ、パネルのユーザーとセットアップコードを使って、名前、Wi-Fi、アドレス、ブローカー、Bluetooth モードを設定します（[プロトコル](docs/BLE_PROVISIONING.md)）。設定を変えない限り、ノードにユーザーがいない間だけ待ち受けます。無線部分は基板ではまだ動作していません。
* **マルチプレクサ付きベース基板（*mux* プロファイル）：** 3 つのハードウェア UART が、それぞれ 74HC4052 を介して、最大 8 ポート（4・2・2 のグループ）を回線ごとに順番に受け持ちます。各ポートは独自の速度と極性を持ち、74HC595 でポートごとに LED が 1 つ付きます。背の高い Pylontech スタックのセルは順番に読めます。標準方言のインバーターでは、**2 つ目の PV 入力**（`QPIGS2`）と**並列システムのユニット**（`QPGS`）が任意の読み取りです。いずれも基板ではまだ動作していません。
* **署名付きの無線アップデート：**ノードが GitHub からインストールするのは、SHA-256 が一致し、管理者の有効な Ed25519 署名を持つイメージだけです（公開鍵はファームウェア内、秘密鍵は管理者の手元から出ません）。管理者がパネルで手動アップロードしたファイルは引き続き受け付けます。パネルのページとメッセージは 8 言語です。
* **PIN 付きの Bluetooth ペアリング：**6 桁の PIN は設定コードから導出され、USB コンソールに表示され、管理者にはパネルにも表示されます。スマートフォンはこれを入力して初めてノードの設定を書き込めます。
* **まだ：** ANT-BMS の Bluetooth 接続（ノードは、より安定なケーブルを使います）、そして実機と実際の機器での動作確認。
* **パネルを使えるのは家だけ：**パネルは既定でプライベートネットワーク（または所有者が指定した VPN などのネットワーク）にだけ応答し、保存する本人を締め出す一覧は拒否します。誤ったパスワードは人ごと・アドレスごとに数え、サーバーのプロキシの背後でも動くので、ノードを公開せずに家の外から使えます。
* **「不明」は「なし」ではありません：** REVO インバーターには警告の問い合わせがないため、メッセージに `warnings_known: false` が付き、Studio は警告を「なし」ではなく「不明」と表示します。
* **ブローカーとの暗号化通信(TLS、任意):** 初期状態ではオフで、ノードはこれまでどおり暗号化なしの MQTT で通信します。ブローカーページのスイッチと、設備独自の認証局の証明書(PEM、最大 2 KB)の入力欄により、`mqtts://` で接続し、その認証局だけを信頼し、到達したアドレス向けに発行された証明書かを確認します。PEM 証明書 1 つでないものは拒否されます。ホストテストで検証済みで、ハンドシェイクはまだ基板では実行していません。
* **状態報告:** ノードは約 1 分ごとに、稼働時間と直前の再起動の理由、空きメモリ、回線と Wi-Fi 信号、ブローカーへの接続回数、最後に記録したエラーを公開します（`armor/health/<ノード>`、ARMOR-COMMON の `node_health` 契約）。作成するコードは全ノードで共有され、コンピューター上でテストされていますが、ボード上ではまだ動作していません。
* **Pylontechバッテリーへの書き込み（初期状態は無効）：** 定型操作のみ——時計、カウンタとログ、再起動、容量、充電レベルのリセット、制限値と保護、出力、シリアル番号、外部メモリ、XMODEM-1Kによるファームウェア、ブロックリスト付きのエキスパートコンソール——を2段階（準備、続いてワンタイムトークンで実行）で行い、前後でバッテリーを読み取り、サービスパスワードはノード内にのみ保存し、テストには模擬コンソールを使います。実機のバッテリーでは未検証：[ベンチテスト計画](docs/BATTERY_BENCH_TEST_PLAN.md)を参照してください。
* **サーバーからの制御：** Studio はノードをきれいに再起動し、最大 1 時間まで一時停止し（自動的に再開）、作業を待機にし（期限なし、再起動後も維持、ノードは接続したまま応答を続けます）、自分を表示させ、診断のスナップショットを求め、メンテナンス中として印を付けることができます（`armor/control/<ノード>/...`、ARMOR-COMMON の `node_control` 契約）。命令はすべて、その操作専用の使い捨てトークンによる 2 段階で、ブローカーに書き込めるのはサーバーだけです。工場出荷時リセットも消去もディープスリープもありません。一時停止中または待機中のノードは、バッテリーへの書き込みを行いません（実行中の操作は取り消せます）。インバーターとバッテリーの読み取りは続けます。 このコードは全ノードで共有され、コンピューター上でテスト済みですが、実機ではまだ動作していません。
* **ありえない値は隠さず名前を付ける：** インバーターがありえない数値を送ると、ノードはそれを契約の上限に留め、`clamped` にその名前を載せるので、サーバーは実測でない値として表示できます。ポートの生ダンプはパネルが見ている間だけ生成されます。
* **ケーブルなしの診断：** 正常でない起動（クラッシュ、ウォッチドッグ、電源の電圧低下、メモリ確保の失敗）の後、ヘルスレポートが10分間その原因を伝えます。クラッシュするとコアダンプが残り、パネルから確認、ダウンロード、削除できます。保存された設定はファームウェアのインストールごとにコピーされ、更新で壊れた場合は復元されます。管理者はサーバー経由で、使い捨てトークンを使って、ノードに診断パッケージまたはログを要求できます。
* **保存された秘密情報の任意の封印:** 既定ではオフです(`security.seal_secrets`、またはサーバーの `nodes.nvs_encryption`)。オンにすると、ノードが保存するパスワード、トークン、鍵、PIN、パスワードのハッシュが ChaCha20-Poly1305 で封印され、それ以外は読めるままです。オン/オフの切り替えは何も失わずに書き直し、途中で止まっても大丈夫です。eFuse は焼かれず、フラッシュも暗号化されません。鍵は同じチップのパーティションにあるため、基板を手にした人に対する保護には**なりません**。このパーティションがない時期にインストールされたノードは、新しいパーティションテーブルで書き込むまで従来のままです。""",
      "role": r"""ARMOR-NODE-SOLAR は家のソーラー機器とファミリーをつなぐゲートウェイです。最大 10 本のシリアルポートでインバーターとバッテリーを読み取り、読み取った内容を [ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER) に送ります。サーバーが履歴、合計、警報を保持し、[ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) の*インバーター*と*バッテリー*メニュー、[ARMOR-ANDROID-CONTROL](https://github.com/JuanenRac/ARMOR-ANDROID-CONTROL) のソーラー画面が表示します。読み取るだけで、どの機器にも設定を書き込みません。

| 名前 | 方法 | 用途 |
|---|---|---|
| ARMOR-SERVER | MQTT `armor/solar/<node>/<device>/state` | インバーターまたはバッテリースタックごとに 1 メッセージを受け取り、バッテリーの保守を命令する |
| ARMOR-STUDIO | メニュー、パネルへのリンク | インバーターとバッテリーを表示し、ノードのパネルを開く |
| ARMOR-ANDROID-CONTROL | Bluetooth | 現場でノードを設定し、エネルギー画面を表示 |
| ARMOR-COMMON | ソーラーのコントラクト | メッセージはそのスキーマで検証し、共通ファームウェアはここからコピー |""",
      "architecture": r"""<p align="center">
  <img src="images/architecture.svg" alt="ARMOR-NODE-SOLAR のアーキテクチャ：呼び出し元、内部、依存先" width="100%">
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
| 誤りまたは攻撃者によるバッテリーへの書き込み | 3 つの錠：ノードの設定 `battery.write_enabled`（管理者）とバッテリーのサービスパスワード、サーバーの `ARMOR_BATTERY_WRITE=1`、`armor/solar/<ノード>/maintenance/command` と `.../result` に対するブローカーのアクセスリスト |
| 繰り返された、または盗まれた書き込み命令 | 2 段階（アームしてから使い捨てトークンで実行）、アーム猶予 120 秒、ポートへの書き込み間隔 30 秒、10 分間に 3 回失敗すると 5 分ロック。バッテリーのシリアル番号を再入力し、バッテリーは待機中で重大アラームがないこと、ファームウェアイメージは 30 分保持して検証 |
| インバーターや ANT-BMS への書き込み | インバーター（設定で家への給電が変わる）と ANT-BMS（負荷中のバッテリーを切り離す恐れ）の書き込みコマンドは、組み立てることすらできません |
| ありえない数値が実測値として表示される | ありえない値は契約の上限で止め、`clamped` に名前を載せるので、サーバーは実測でないものとして表示できます。REVO インバーターには警告の問い合わせがないため、メッセージは「警告なし」とは言わず `warnings_known: false` と伝えます |

実際のインバーターやバッテリーからフレームを読んだことはありません。フォーマットは公開文書と記憶から書いたもので、テストの ANT-BMS フレームは他の人が取得したものです。[docs/BATTERY_MAINTENANCE.md](docs/BATTERY_MAINTENANCE.md) と [SECURITY.md](SECURITY.md) を参照してください。""",
      "interfaces": r"""| 部分 | 設定内容 |
|---|---|
| MQTT | `armor/solar/<ノード>/<機器>/state`（インバーターまたはバッテリースタックごとに 1 メッセージ、ARMOR-COMMON のコントラクトの種別 `inverter` または `battery`）、`armor/solar/<ノード>/maintenance/{command,result}`、`armor/health/<ノード>`（遺言）、`armor/control/<id>/{command,result,maintenance}`、`armor/control/all/command` |
| ポート | シリアルポート 10 本（ハードウェア UART 3 本とエミュレート 7 本、エミュレート時は最大 19200 ボー）。ポートごとの種別：`voltronic`（2400 ボー、5 秒ごと）、`pylontech`（115200、10 秒ごと）、`ant`（19200、5 秒ごと）、`raw`（9600、受信のみで何も発行しない）。インバーターの方言は `auto`、`pi30`、`revo`、`pi18`。mux プロファイルにはポートのグループが 3 つあります |
| 問い合わせ | Voltronic：`QPIGS`、`QMOD`、`QPIWS`、`QPIRI`（mux 付きの標準インバーターでは `QPIGS2`、`QPGS` も）。Pylontech コンソール：`pwr`、`bat <n>`、`info <n>`、`stat`、`soh`、イベントログ。最大 8 モジュールをセル単位で問い合わせます |
| パネル | ファミリー共通のルート（`tests/check_routes.py` がパネルの呼ぶルートの存在を検査）に加え、ポートと測定値のページ。8 言語の文言つきエラーコード 51 個（`panel/text.js` に 772 行）。Studio のメニューは [docs/STUDIO_MENUS.md](docs/STUDIO_MENUS.md) |""",
      "configuration": r"""| 変数 | 既定値 | 設定内容 |
|---|---|---|
| `enabled`, `kind`, `name`, `baud`, `rx`, `tx`, `de`, `poll_s`, `modules`, `dialect` | - | ポートごとの設定：有効かどうか、種別、トピック内の機器名、速度（0 = 種別の既定値）、ピン（RS485 の DE/RE ピンを含む）、問い合わせ周期（0 = 種別の既定値）、モジュール数、インバーターの方言。予備ネットワークは最大 3、予備ブローカーは最大 2 |
| `battery.write_enabled` | off | Pylontech バッテリーへの書き込みに対するノードの錠（管理者、バッテリーのサービスパスワードを使い、パスワードはノードの外に出ません） |
| `CONFIG_ARMOR_BOARD_S3_WIFI` / `_S3_ETH` | wifi | 基板：ESP32-S3-WROOM-1 N16R8（Wi-Fi、既定）または Waveshare ESP32-S3-ETH |
| `CONFIG_ARMOR_NODE_ID`, `_SETUP_CODE`, `_FLEET_SECRET`, `_MQTT_*`, `_HEARTBEAT_S`, `_BLE_SETUP_MINUTES`, `_BOOT_FACTORY_RESET` | - | すべてのノードに共通する設定：名前（空なら `armor-` と MAC の下位バイト）、セットアップコード（空ならランダム）、フリートシークレット（16 文字以上、リポジトリには置かない）、最初のブローカー設定、ハートビート（2〜300 秒）、Bluetooth セットアップの分数（1〜120）、BOOT によるリセット（最初の 30 秒に 8 秒） |""",
      "quickstart": r"""**必要なもの:** ホストテスト用の C++17 コンパイラ、イメージのビルド用の ESP-IDF 5.5.5 コンテナ、ESP32-S3-WROOM-1 N16R8 または Waveshare ESP32-S3-ETH。

```bash
cmake -S tests -B build/host && cmake --build build/host && ctest --test-dir build/host   # host tests, -Werror
build/host/emit_poller_samples | python tests/check_samples.py   # what the ports make is accepted by ARMOR-COMMON
tools/build_node.sh generic                       # the image for the N16R8 board in the ESP-IDF container: dist/generic-s3-wifi.bin
tools/build_node.sh generic s3-eth               # the same firmware for the Waveshare ESP32-S3-ETH (Ethernet): dist/generic-s3-eth.bin
node tools/panel_mock.mjs --user admin:adminpass123   # the panel without a board
```

[ファームウェアガイド](docs/NODE_FIRMWARE.md)（ボード、ポート、初回起動、ベンチ確認リスト）と[配線メモ](docs/NODE_HARDWARE.md)を参照。""",
      "testing": r"""```bash
cmake -S tests -B build/host && cmake --build build/host && ctest --test-dir build/host
python -I tools/armor_ci_validate.py
```

ホスト用テストプログラム 18 個と Python の検査 6 個を `ctest` で実行します。ホストのプログラムが数えた検査は 11824 件で、`-Werror` でビルドします。

Python の検査：8 言語のパネル文言、タスク、保存パス、ロック下の Bluetooth セッション、パネルが呼ぶルート（ノードによっては HTTP コードやフォントのグリフも）

ホストテストには任意の C++17 コンパイラ（Linux、WSL、MSYS2）が必要です。Web パネルは代役ノード（`tools/panel_mock.mjs`、`tools/panel_browser_test.mjs`）を相手に実際のブラウザでも検証します。

`test_clock` は `ok` だけを出力しカウンターを持ちません。他のプログラムは検査数を報告します。テストの実フレームは `tests/pylontech_real.hpp`、`pylontech_us2000_real.hpp`、`pylontech_logs_real.hpp`、`ant_frames.hpp`、`battery_bench.hpp` にあります。""",
      "build": "`tools/build_node.sh` が ESP-IDF 5.5.5 コンテナでイメージをビルドし、リリースにはイメージ、その SHA-256 と Ed25519 署名が基板ごとに付きます。イメージは初回のみ USB-C で書き込み、その後はパネルから更新します。",
      "troubleshooting": r"""| 症状 | 原因 | 対処 |
|---|---|---|
| パスワードを忘れた、またはノードがネットワークに参加しない | セットアップ中でアドレスがないノードは 90 秒後に独自の Wi-Fi `ARMOR-SETUP-xxxxxx` を開きます（`http://192.168.4.1/` を開く） | 最初からやり直すには、電源投入後 30 秒以内に BOOT を 8 秒押し続ける（設定とユーザーを消去）か、パネルの*工場出荷状態に戻す*を使います |
| GitHub からの更新が拒否される | リリースにチェックサムや署名がない、一致しない（`e_no_checksum`、`e_no_signature`、`e_checksum_mismatch`、`e_bad_signature`）、この基板用のイメージがない（`e_no_asset_for_board`）、または別プロジェクトのもの（`e_wrong_firmware`） | ノードは変更されていません。再試行するか、管理者が手動でファイルをアップロード |
| バッテリーへの書き込みがコード付きで拒否される | `serial_mismatch`、`not_pylontech`、`no_battery`、`unknown_model`、`not_idle`、`critical_alarm`、`busy`、`cooldown`、`locked`、`not_armed`、`bad_token`、`expired`、`disabled`、`image_missing`、`image_mismatch` など：アームした操作と完全に同じでないものは拒否します | 結果のコードを読み、原因を直して操作をもう一度アームする（[docs/BATTERY_MAINTENANCE.md](docs/BATTERY_MAINTENANCE.md) を参照） |
| ポートが何も発行しない | ポートがオフ、種別が `raw`（受信のみ）、速度やピンが機器と合っていない、または機器が応答しない | ポートの設定と配線を [docs/NODE_HARDWARE.md](docs/NODE_HARDWARE.md) で確認する。パネルは見ている間だけポートの生ダンプを表示 |""",
      "structure": r"""<p align="center">
  <img src="images/repository-structure.svg" alt="ARMOR-NODE-SOLAR のリポジトリ構造" width="100%">
</p>

<details>
<summary>ツリーのテキスト版</summary>

```text
ARMOR-NODE-SOLAR/
├── main/                                ファームウェア（ESP-IDF コンポーネント）
├── core/                                ESP-IDF なしのロジック（コンピューターでテスト）
├── panel/                               ファームウェアに埋め込まれた Web パネル
├── tests/                               ホストテストと Python 検査
├── docs/                                10 のガイド：プロトコル、メッセージ、保守、ハードウェア
├── tools/                               ビルド・パッケージ・検査のツール
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
├── sdkconfig.board.s3-eth               基板ごとの設定
├── sdkconfig.board.s3-wifi              基板ごとの設定
├── secrets/                             ノードファイルの例（本物はバージョン管理しません）
├── build-test.sh build-test.bat         共通のワークフローでテストを実行
└── .gitattributes .gitignore            Git の設定
```

</details>""",
      "roadmap": r"""**現時点の既知の制限**

* Voltronic、Pylontech、ANT-BMS のフレーム、チェックサム、読み取り値は、文書化されたフレームと記録したサンプルに対して検証済みです。実際のインバーターやバッテリーとはまだ通信していません。
* Web パネルはブラウザーでノードの模擬に対して試しており、ボード上では試していません。
* ボードは未製作で、インバーターやバッテリーも接続していません。実機ではまだ何も動かしていません。
* 設定コード、誤ったパスワードの回数制限付きログイン、Bluetooth の PIN、署名付きアップデートはホストでテスト済みです。独立したレビューはまだありません。
* ハッシュと Ed25519 署名の確認、ロールバックの処理はホストで通ります。無線アップデートはボード上で一度も実行していません。
* Pylontech バッテリーへの書き込みは既定でオフで、シミュレーターに対してのみテストしています。

**今後**

* 実際の基板で実際のインバーターとバッテリーを使ってノードを動かし、続いて ANT-BMS の Bluetooth 接続（現在はケーブルを使用）、OTA 更新、バッテリーへの書き込みを試す。""",
    },
  },
  "zh": {
    "tagline": "太阳能网关节点：通过最多十个串口读取逆变器和电池（ESP32-S3 固件、其网页面板和协议库）",
    "honest": "固件可在 ESP-IDF 5.5.5 容器中构建，其核心（设置、与每种设备的交互、模拟 UART 的运算、蓝牙通道、版本和签名检查：18 个测试程序中的 11,824 项检查）在计算机上用替身设备测试，它生成的消息被 ARMOR-COMMON 接受，面板已在浏览器中对照替身节点验证。**它从未在板上运行，也没有连接过任何逆变器或电池**：Wi-Fi、TLS 上的面板、更新、硬件和模拟 UART 以及协议格式（根据公开文档和记忆编写）都未经尝试。其测试中的 ANT-BMS 帧由其他人在自己的设备上捕获：本项目自己还没有读取过任何一帧。",
    "glance": [
      [
        "角色",
        "ESP32-S3 太阳能现场节点：逆变器和电池（家族：Field Nodes，上级：ARMOR-COMMON）",
      ],
      [
        "技术栈",
        "C++17, ESP-IDF 5.5.5, ESP32-S3",
      ],
      [
        "测试",
        "11824 项检查（18 个主机程序和 6 项 Python 检查，`ctest`）",
      ],
      [
        "设备",
        "Voltronic / MPP Solar 逆变器、Pylontech 电池、ANT-BMS；10 个串口",
      ],
      [
        "运行位置",
        "ESP32-S3-WROOM-1 N16R8 或 Waveshare ESP32-S3-ETH；主机测试可在任何计算机上运行",
      ],
      [
        "真实硬件",
        "暂无：没有制作板子，也没有连接逆变器或电池（仅有计算机测试、构建和浏览器中的面板）",
      ],
      [
        "许可证",
        "GPL-3.0-or-later",
      ],
    ],
    "status": {
      "software": "固件可在 ESP-IDF 5.5.5 容器中为两块板（Wi-Fi 和以太网）构建。",
      "tests": "18 个主机程序中的 11,824 项检查通过（`ctest`）：设置、与各类设备的交换、模拟 UART、蓝牙通道和版本检查。",
      "protocols": "Voltronic、Pylontech 和 ANT-BMS 的帧、校验和与读数已对照文档中的帧和录制的样本检查；目前还没有与真实的逆变器或电池通信过。",
      "ui": "网页面板已在浏览器中对节点的模拟进行过测试，尚未在板子上测试。",
      "hardware": "尚未制作板子，也没有连接逆变器或电池：还没有在真实设备上运行过。",
      "security": "设置码、限制错误密码次数的登录、蓝牙 PIN 和签名更新已在主机上测试；没有经过独立审查。",
      "updates": "哈希和 Ed25519 签名检查以及回滚逻辑在主机上通过；空中更新从未在板子上运行过。",
      "writing": "对 Pylontech 电池的写入默认关闭，只对照模拟器测试过。",
      "integration": "节点的消息已对照 ARMOR-COMMON 的共享模式和一致性向量验证。其 MQTT 客户端在测试中与真实的 Mosquitto 对接；还没有任何板子把这些消息发到服务器。",
      "docs": "八种语言、固件指南、接线说明和更新日志均为最新。",
    },
    "docs": [
      "[节点固件](docs/NODE_FIRMWARE.md)：电路板、端口、首次启动和台架检查清单",
      "[接线](docs/NODE_HARDWARE.md)、[协议](docs/PROTOCOLS.md)和[消息](docs/SOLAR_MESSAGES.md)",
      "[电池维护](docs/BATTERY_MAINTENANCE.md)及其[台架测试计划](docs/BATTERY_BENCH_TEST_PLAN.md)",
      "[Studio 菜单](docs/STUDIO_MENUS.md)、[台架测试](docs/BENCH_TESTS.md)、[设置码](docs/SETUP_CODE.md)和[蓝牙配置](docs/BLE_PROVISIONING.md)",
    ],
    "contributing_first": "提交 Pull Request 之前请运行 `ctest --test-dir build/host` and `python -I tools/armor_ci_validate.py`：必须通过。参见 [CONTRIBUTING.md](CONTRIBUTING.md) 和[行为准则](CODE_OF_CONDUCT.md)。",
    "languages_extra": "",
    "body": {
      "overview": r"""* **两种开发板，一套固件：** 走 Wi-Fi 的 ESP32-S3-WROOM-1 N16R8（默认）和走以太网线的 Waveshare ESP32-S3-ETH（DHCP 或固定地址；保留自己的 Wi-Fi 网络以便从手机访问）。镜像在构建时选择（`tools/build_node.sh generic s3-wifi` 或 `generic s3-eth`）；引脚表、端口的默认引脚和接入方式随开发板而定，镜像只适用于对应的开发板。两者都能构建并已在电脑上测试，但都没在开发板上运行过。
* **节点固件**（Wi-Fi 的 ESP32-S3-WROOM-1 N16R8，或有线的 Waveshare ESP32-S3-ETH）：十个串口，三个硬件 UART 和七个模拟 UART（最高 19200 波特），每个都独立，可读取逆变器、电池或原始监视，因此一个节点可以只读逆变器、只读电池或两者混合。
* **节点的网页面板，** 与雷达节点相同：用 USB 控制台显示的代码进行设置、登录和用户、Wi-Fi（站点和接入点）、代理、带回滚的空中更新、日志、HTTPS，以及串口页面（显示每个端口收到的内容，用于尚未解码的协议）和读数页面，支持八种语言。
* **Voltronic / MPP Solar 逆变器**（Axpert、PIP、InfiniSolar 及其克隆），RS232 2400 波特：帧及其 CRC，以及读数 `QPIGS`（电网、输出、电池、光伏、状态位）、`QMOD`（模式）、`QPIWS`（按名称列出的警告和故障）和 `QPIRI`（额定值）。只能构造读取命令：设置会改变房屋的供电方式。三种方言，可在端口上选择或由端口自动找到（*auto*）：PI30、REVO（另一种 `QPIGS`，以校验和结尾的应答）和 PI18（`^P005GS`：InfiniSolar V、LV5048、SunGoldPower），仅读取。
* **Pylontech 电池**（US2000、US3000、US5000）：控制台的 `pwr` 表（每个模块的电压、电流、温度和电量）、`bat <n>`（每个电芯的电压和温度）以及 `info <n>`（型号、剩余和满容量、循环次数），汇总为一个电池组及其总容量和能量，还有带两项校验的 RS485 帧。这些格式是凭对公开控制台的记忆写成的，不同固件可能不同。各列按表头名称查找（包括带 Id 列、MosTempr 和 SysAlarm.St 的 US5000 V2.3 格式），剩余电量和均衡来自 `bat`，型号、额定容量和循环次数来自 `info` 和 `stat`，只询问一次并保留半小时。
* **Pylontech 模块自述的信息：** 型号、电路板和软件版本、电芯数量和允许的电流、寿命计数器（`stat`）、每个电芯的健康状态（`soh`，标出异常的一个），以及其事件日志的最新条目，保护名称与控制台打印的完全一致。控制台只读，管理员可以把端口收到的内容下载为文本文件。
* **节点的消息**（`armor/solar/<节点>/<设备>/state`，每台逆变器或电池组一条），在 ARMOR-COMMON 中以模式和一致性向量定义；各端口生成的内容会对照它们检查。
* **ANT-BMS 电池**（自制电池组上的黑色板，7S 至 32S），3.3 V UART，19200 波特：支持其固件的两种协议（节点先用一种询问，无应答再用另一种，并保持在有应答的那种），读取电芯、温度、荷电状态、电流、容量以及 MOSFET 和均衡器状态，并用在四种真实型号上抓取的帧做了验证。只读：其写入命令可能在带载时断开电池。端口页面上的按钮还可读取 BMS 的型号、版本以及 56 项保护和均衡设置（新协议，只读）。
* **通过蓝牙用手机配置：** 与雷达节点相同的通道。ARMOR 应用会以 `ARMOR-XXXXXX` 找到节点，并使用面板的用户和设置码来设置其名称、Wi-Fi、地址、代理和蓝牙模式（[协议](docs/BLE_PROVISIONING.md)）。除非另行设置，它只在节点还没有用户时监听。无线部分从未在电路板上运行过。
* **带多路复用器的底板（*mux* 配置）：** 三个硬件 UART，每个前面有一个 74HC4052，为最多八个端口（分为 4、2、2 三组）轮流使用各自的线路；每个端口有自己的速度和极性，并通过 74HC595 为每个端口提供一个指示灯；较高的 Pylontech 电池堆的电芯可以轮流读取。对标准方言的逆变器，**第二路光伏输入**（`QPIGS2`）和**并联系统的单元**（`QPGS`）是可选的读数。以上均未在电路板上运行过。
* **签名的无线更新：**节点只会从 GitHub 安装 SHA-256 匹配且带有维护者有效 Ed25519 签名的镜像（公钥在固件中，私钥从不离开维护者）；管理员在面板中手动上传的文件仍然被接受。面板的页面和消息有八种语言。
* **带 PIN 的蓝牙配对：**六位 PIN 由设置码派生，打印在 USB 控制台上并向管理员显示在面板中；手机必须输入它才能写入节点的设置。
* **尚未完成：** ANT-BMS 的蓝牙连接（节点使用更稳定的线缆）、Android 标签页，以及在真实开发板上用真实设备的运行。
* **只有家中才能使用面板：**面板默认只响应私有网络（或所有者列出的网络，如 VPN），拒绝会把保存者自己挡在外面的列表，按人和按地址统计错误密码，并可在服务器代理之后工作，从而无需公开节点就能在家外访问。
* **未知不等于没有：** REVO 逆变器没有警告查询，因此其消息带有 `warnings_known: false`，Studio 会把警告显示为“未知”而不是“无”。
* **可选的与代理加密连接(TLS):** 默认关闭,因此节点仍像以前一样使用未加密的 MQTT。代理页面中的一个开关和一个用于填写本安装自有证书颁发机构证书(PEM,最大 2 KB)的框,会让节点用 `mqtts://` 连接、只信任该机构,并检查代理证书是否为其所到达的地址而签发;不是单个 PEM 证书的内容会被拒绝。已有主机测试覆盖;握手尚未在电路板上运行。
* **健康报告：** 节点大约每分钟发布一次：已运行多久、上次为何重启、可用内存、连接与 Wi-Fi 信号、连接代理的次数以及记录的最后一个错误（`armor/health/<节点>`，即 ARMOR-COMMON 的 `node_health` 契约）。生成它的代码由所有节点共享并在计算机上测试；尚未在开发板上运行。
* **写入 Pylontech 电池（默认关闭）：** 只有定型操作——时钟、计数器和日志、重启、容量、电量重置、限值与保护、输出、序列号、外部存储器、通过 XMODEM-1K 升级固件，以及带禁用清单的专家控制台——分两步进行（准备，再用一次性令牌执行），操作前后都读取电池，服务密码只保存在节点中，测试使用模拟控制台。尚未在真实电池上试过：见[台架测试计划](docs/BATTERY_BENCH_TEST_PLAN.md)。
* **由服务器控制：** Studio 可以干净地重启节点、将其暂停至多一小时（自动恢复）、让其工作进入待机（无期限，重启后仍保持，节点保持连接并继续应答）、让它显示自己、请求诊断快照，并把它标记为维护中（`armor/control/<节点>/...`，ARMOR-COMMON 的 `node_control` 契约）。每条命令分两步，使用只属于该操作的一次性令牌，只有服务器可以在代理上写入，并且没有恢复出厂设置、擦除或深度睡眠。节点处于暂停或待机时，不向任何电池写入（正在进行的操作仍可取消），并继续读取逆变器和电池。 该代码由所有节点共用，并已在计算机上测试；尚未在电路板上运行过。
* **荒谬的数值会被点名，而不是被隐藏：** 当逆变器发来不可能的数字时，节点会把它限制在合同的上限，并在 `clamped` 中点名，因此服务器会把它显示为不真实；端口的原始转储只在面板正在查看时才生成。
* **无需线缆的诊断：** 在一次不干净的启动之后（崩溃、看门狗、电源跌落、内存分配失败），健康报告会在十分钟内说明原因；崩溃会留下核心转储（core dump），可在面板中查看、下载或删除；已保存的设置会在每次固件安装前被复制，并在更新损坏它们时恢复；管理员还可以通过服务器，用一次性令牌向节点索取诊断包或其日志。
* **可选的已存储机密封存:** 默认关闭(`security.seal_secrets`,或服务器的 `nodes.nvs_encryption`)。开启后,节点保存的密码、令牌、密钥、PIN 和密码哈希会用 ChaCha20-Poly1305 封存,其余内容仍可读取;开启或关闭时会无损重写,即使节点中途停止也不会丢失。不会烧写 eFuse,闪存也不加密:密钥在同一芯片的一个分区中,因此**不能**防范持有电路板的人;在该分区出现之前安装的节点会保持原样,直到用新的分区表重新烧录。""",
      "role": r"""ARMOR-NODE-SOLAR 是住宅太阳能设备与家族之间的网关。它通过最多十个串口读取逆变器和电池，并把读到的内容发布给 [ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER)，由后者保存历史、合计和报警；[ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) 的*逆变器*和*电池*菜单以及 [ARMOR-ANDROID-CONTROL](https://github.com/JuanenRac/ARMOR-ANDROID-CONTROL) 的太阳能界面显示这些内容。它只读取：从不向任何设备写入设置。

| 名称 | 方式 | 用途 |
|---|---|---|
| ARMOR-SERVER | MQTT `armor/solar/<node>/<device>/state` | 每个逆变器或电池组接收一条消息；下达电池维护命令 |
| ARMOR-STUDIO | 菜单、面板链接 | 显示逆变器和电池并打开节点面板 |
| ARMOR-ANDROID-CONTROL | Bluetooth | 在现场设置节点并显示能源界面 |
| ARMOR-COMMON | 太阳能合约 | 消息按其模式校验；公共固件由此复制 |""",
      "architecture": r"""<p align="center">
  <img src="images/architecture.svg" alt="ARMOR-NODE-SOLAR 的架构：谁调用它、它包含什么、它依赖什么" width="100%">
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
| 因错误或攻击者而写入电池 | 三道锁：节点设置 `battery.write_enabled`（管理员）加电池的服务密码，服务器的 `ARMOR_BATTERY_WRITE=1`，以及代理对 `armor/solar/<节点>/maintenance/command` 和 `.../result` 的访问列表 |
| 被重放或窃取的写入命令 | 两步（先布防，再用一次性令牌执行），布防窗口 120 秒，对同一端口的两次写入间隔 30 秒，10 分钟内失败 3 次则锁定 5 分钟；需要再次输入电池序列号，电池必须空闲且无严重报警，固件镜像保留 30 分钟并经过校验 |
| 向逆变器或 ANT-BMS 写入 | 逆变器（设置会改变住宅的供电方式）和 ANT-BMS（可能在负载下断开电池）的写入命令甚至无法构造 |
| 荒谬的数值被当作真实值显示 | 不可能的数值会被限制在合约上限并在 `clamped` 中列出，服务器据此将其显示为非真实值；REVO 逆变器没有告警查询，所以其消息写 `warnings_known: false`，而不是声称没有告警 |

从未从真实逆变器或电池读取过任何帧；格式依据公开文档和记忆编写，测试中的 ANT-BMS 帧由他人捕获。请阅读 [docs/BATTERY_MAINTENANCE.md](docs/BATTERY_MAINTENANCE.md) 和 [SECURITY.md](SECURITY.md)。""",
      "interfaces": r"""| 部分 | 作用 |
|---|---|
| MQTT | `armor/solar/<节点>/<设备>/state`（每个逆变器或电池组一条消息，类型为 ARMOR-COMMON 合约中的 `inverter` 或 `battery`）、`armor/solar/<节点>/maintenance/{command,result}`、`armor/health/<节点>`（遗嘱）、`armor/control/<id>/{command,result,maintenance}` 和 `armor/control/all/command` |
| 端口 | 10 个串口（3 个硬件 UART 和 7 个模拟 UART，模拟时最高 19200 波特）；每个端口有一个类型：`voltronic`（2400 波特，每 5 秒）、`pylontech`（115200，每 10 秒）、`ant`（19200，每 5 秒）或 `raw`（9600，仅监听，不发布任何内容）；逆变器方言有 `auto`、`pi30`、`revo`、`pi18`；mux 方案有 3 组端口 |
| 查询 | Voltronic：`QPIGS`、`QMOD`、`QPIWS`、`QPIRI`（带 mux 的标准逆变器还有 `QPIGS2`、`QPGS`）；Pylontech 控制台：`pwr`、`bat <n>`、`info <n>`、`stat`、`soh`、事件日志，最多 8 个模块逐个电芯查询 |
| 面板 | 系列共有的路由（`tests/check_routes.py` 检查面板调用的每条路由都存在）加上端口和读数页面；51 个带八种语言文字的错误码（`panel/text.js` 中 772 行）；Studio 的菜单见 [docs/STUDIO_MENUS.md](docs/STUDIO_MENUS.md) |""",
      "configuration": r"""| 变量 | 默认值 | 作用 |
|---|---|---|
| `enabled`, `kind`, `name`, `baud`, `rx`, `tx`, `de`, `poll_s`, `modules`, `dialect` | - | 每个端口的设置：是否启用、类型、主题中的设备名、速度（0 = 该类型的默认值）、引脚（以及 RS485 的 DE/RE 引脚）、轮询周期（0 = 该类型的默认值）、模块数和逆变器方言；备用网络最多 3 个，备用代理最多 2 个 |
| `battery.write_enabled` | off | 节点对 Pylontech 电池写入的锁（管理员，使用电池的服务密码，该密码从不离开节点） |
| `CONFIG_ARMOR_BOARD_S3_WIFI` / `_S3_ETH` | wifi | 电路板：ESP32-S3-WROOM-1 N16R8（Wi-Fi，默认）或 Waveshare ESP32-S3-ETH |
| `CONFIG_ARMOR_NODE_ID`, `_SETUP_CODE`, `_FLEET_SECRET`, `_MQTT_*`, `_HEARTBEAT_S`, `_BLE_SETUP_MINUTES`, `_BOOT_FACTORY_RESET` | - | 所有节点共有的设置：名称（为空则为 `armor-` 加 MAC 的最后字节）、设置码（为空则随机）、机群密钥（16 个字符以上，绝不放入仓库）、最初的代理设置、心跳（2 到 300 秒）、蓝牙设置的分钟数（1 到 120）以及用 BOOT 重置（前 30 秒内按 8 秒） |""",
      "quickstart": r"""**要求:** 用于主机测试的 C++17 编译器；用于构建镜像的 ESP-IDF 5.5.5 容器；ESP32-S3-WROOM-1 N16R8 或 Waveshare ESP32-S3-ETH。

```bash
cmake -S tests -B build/host && cmake --build build/host && ctest --test-dir build/host   # host tests, -Werror
build/host/emit_poller_samples | python tests/check_samples.py   # what the ports make is accepted by ARMOR-COMMON
tools/build_node.sh generic                       # the image for the N16R8 board in the ESP-IDF container: dist/generic-s3-wifi.bin
tools/build_node.sh generic s3-eth               # the same firmware for the Waveshare ESP32-S3-ETH (Ethernet): dist/generic-s3-eth.bin
node tools/panel_mock.mjs --user admin:adminpass123   # the panel without a board
```

参见[固件指南](docs/NODE_FIRMWARE.md)（开发板、端口、首次启动和台架检查清单）以及[接线说明](docs/NODE_HARDWARE.md)。""",
      "testing": r"""```bash
cmake -S tests -B build/host && cmake --build build/host && ctest --test-dir build/host
python -I tools/armor_ci_validate.py
```

`ctest` 运行 18 个主机测试程序和 6 个 Python 检查；主机程序统计的检查共 11824 项，使用 `-Werror` 构建。

Python 检查：八种语言的面板文字、任务、保存路径、受锁保护的蓝牙会话以及面板调用的路由（部分节点还包括 HTTP 状态码或字体字形）

主机测试需要任意 C++17 编译器（Linux、WSL、MSYS2）；网页面板还会在真实浏览器中对着模拟节点（`tools/panel_mock.mjs`、`tools/panel_browser_test.mjs`）进行验证。

`test_clock` 只输出 `ok`，没有计数器；其余每个程序都会报告其检查数。测试用的真实帧在 `tests/pylontech_real.hpp`、`pylontech_us2000_real.hpp`、`pylontech_logs_real.hpp`、`ant_frames.hpp` 和 `battery_bench.hpp` 中。""",
      "build": "`tools/build_node.sh` 在 ESP-IDF 5.5.5 容器中构建镜像，发布版带有镜像、其 SHA-256 和 Ed25519 签名，每块电路板一份；镜像第一次通过 USB-C 写入，之后从面板更新。",
      "troubleshooting": r"""| 现象 | 原因 | 处理 |
|---|---|---|
| 忘记了密码，或节点不再加入网络 | 处于设置状态且 90 秒后仍无地址的节点会开启自己的 Wi-Fi `ARMOR-SETUP-xxxxxx`（打开 `http://192.168.4.1/`） | 要重新开始，请在上电后 30 秒内按住 BOOT 8 秒（会清除设置和用户），或使用面板中的*恢复出厂设置* |
| 来自 GitHub 的更新被拒绝 | 发布版缺少校验和或签名，或二者不匹配（`e_no_checksum`、`e_no_signature`、`e_checksum_mismatch`、`e_bad_signature`），没有适用于此电路板的镜像（`e_no_asset_for_board`），或属于另一个项目（`e_wrong_firmware`） | 节点未发生任何变化；请重试，或由管理员手动上传文件 |
| 对电池的写入被拒绝并带有代码 | `serial_mismatch`、`not_pylontech`、`no_battery`、`unknown_model`、`not_idle`、`critical_alarm`、`busy`、`cooldown`、`locked`、`not_armed`、`bad_token`、`expired`、`disabled`、`image_missing`、`image_mismatch` 等：节点拒绝任何与已布防操作不完全一致的内容 | 查看结果中的代码，修复原因后重新布防该操作（见 [docs/BATTERY_MAINTENANCE.md](docs/BATTERY_MAINTENANCE.md)） |
| 端口没有发布任何内容 | 端口已关闭，类型为 `raw`（仅监听），速度或引脚与设备不符，或设备没有响应 | 检查端口设置和接线（见 [docs/NODE_HARDWARE.md](docs/NODE_HARDWARE.md)）；面板在查看某个端口时会显示其原始转储 |""",
      "structure": r"""<p align="center">
  <img src="images/repository-structure.svg" alt="ARMOR-NODE-SOLAR 的仓库结构" width="100%">
</p>

<details>
<summary>目录树的文本版</summary>

```text
ARMOR-NODE-SOLAR/
├── main/                                固件：一个 ESP-IDF 组件
├── core/                                不依赖 ESP-IDF 的逻辑，在计算机上测试
├── panel/                               嵌入固件的网页面板
├── tests/                               主机测试和 Python 检查
├── docs/                                10 份指南：协议、消息、维护、硬件
├── tools/                               构建、打包和检查工具
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
├── sdkconfig.board.s3-eth               某块电路板的设置
├── sdkconfig.board.s3-wifi              某块电路板的设置
├── secrets/                             节点文件示例（真实文件不纳入版本管理）
├── build-test.sh build-test.bat         通过共享工作流运行测试
└── .gitattributes .gitignore            Git 设置
```

</details>""",
      "roadmap": r"""**目前已知的限制**

* Voltronic、Pylontech 和 ANT-BMS 的帧、校验和与读数已对照文档中的帧和录制的样本检查；目前还没有与真实的逆变器或电池通信过。
* 网页面板已在浏览器中对节点的模拟进行过测试，尚未在板子上测试。
* 尚未制作板子，也没有连接逆变器或电池：还没有在真实设备上运行过。
* 设置码、限制错误密码次数的登录、蓝牙 PIN 和签名更新已在主机上测试；没有经过独立审查。
* 哈希和 Ed25519 签名检查以及回滚逻辑在主机上通过；空中更新从未在板子上运行过。
* 对 Pylontech 电池的写入默认关闭，只对照模拟器测试过。

**下一步**

* 在真实电路板上连接真实逆变器和电池运行节点，然后试验 ANT-BMS 的蓝牙连接（目前使用线缆）、空中更新以及对电池的写入。""",
    },
  },
  "pt": {
    "tagline": "Nó de ligação solar: lê inversores e baterias através de até dez portas série (firmware ESP32-S3, o seu painel web e a biblioteca de protocolos)",
    "honest": "O firmware compila no contentor ESP-IDF 5.5.5, o seu núcleo (as definições, a troca com cada tipo de equipamento, a aritmética da UART emulada, o canal Bluetooth, as verificações de versão e assinatura: 2885 verificações em 10 programas de teste) é testado num computador com equipamentos de substituição, as mensagens que produz são aceites pelo ARMOR-COMMON e o painel foi exercitado num navegador contra um nó de substituição. **Nunca correu numa placa e nenhum inversor ou bateria foi ligado**: o Wi-Fi, o painel sobre TLS, a atualização, as UART de hardware e emuladas e os formatos dos protocolos (escritos a partir de documentos públicos e de memória) estão por experimentar. As tramas ANT-BMS dos seus testes foram capturadas por outras pessoas nas suas próprias unidades: este projeto ainda não leu nenhuma por si.",
    "glance": [
      [
        "Função",
        "Nó de campo solar para ESP32-S3: inversores e baterias (família: Field Nodes, pai: ARMOR-COMMON)",
      ],
      [
        "Tecnologia",
        "C++17, ESP-IDF 5.5.5, ESP32-S3",
      ],
      [
        "Testes",
        "11824 verificações em 18 programas de anfitrião e 6 em Python (`ctest`)",
      ],
      [
        "Equipamentos",
        "Inversores Voltronic / MPP Solar, baterias Pylontech, ANT-BMS; 10 portas série",
      ],
      [
        "Funciona em",
        "ESP32-S3-WROOM-1 N16R8 ou Waveshare ESP32-S3-ETH; testes de anfitrião em qualquer computador",
      ],
      [
        "Em hardware real",
        "Nenhum ainda: nenhuma placa montada nem inversor ou bateria ligados (só testes no computador, a compilação e o painel num navegador)",
      ],
      [
        "Licença",
        "GPL-3.0-or-later",
      ],
    ],
    "status": {
      "software": "O firmware compila no contentor ESP-IDF 5.5.5 para as duas placas (Wi-Fi e Ethernet).",
      "tests": "Passam 11.824 verificações em 18 programas de anfitrião (`ctest`): as definições, a troca com cada tipo de equipamento, a UART emulada, o canal Bluetooth e as verificações de versão.",
      "protocols": "As tramas, somas de verificação e leituras de Voltronic, Pylontech e ANT-BMS são verificadas contra as tramas documentadas e amostras gravadas; nenhum falou ainda com um inversor ou uma bateria reais.",
      "ui": "O painel web foi exercitado num navegador contra uma simulação do nó, não numa placa.",
      "hardware": "Nenhuma placa construída nem inversor ou bateria ligados: nada funcionou ainda em equipamentos reais.",
      "security": "O código de configuração, o acesso com limite de palavras-passe erradas, o PIN Bluetooth e as atualizações assinadas estão testados no anfitrião; não houve revisão independente.",
      "updates": "As verificações de hash e de assinatura Ed25519 e a lógica de retrocesso passam no anfitrião; uma atualização pelo ar nunca foi executada numa placa.",
      "writing": "A escrita nas baterias Pylontech está desativada por predefinição e só foi testada contra um simulador.",
      "integration": "As mensagens do nó são validadas contra os esquemas partilhados e os vetores de conformidade do ARMOR-COMMON. O seu cliente MQTT é exercitado contra um Mosquitto real nos testes; nenhuma placa os enviou ainda a um servidor.",
      "docs": "Oito idiomas, o guia do firmware, as notas de cablagem e o registo de alterações estão atualizados.",
    },
    "docs": [
      "[Firmware do nó](docs/NODE_FIRMWARE.md): a placa, as portas, o primeiro arranque e a lista de verificação da bancada",
      "[Cablagem](docs/NODE_HARDWARE.md), [protocolos](docs/PROTOCOLS.md) e [mensagens](docs/SOLAR_MESSAGES.md)",
      "[Manutenção de baterias](docs/BATTERY_MAINTENANCE.md) e o seu [plano de testes de bancada](docs/BATTERY_BENCH_TEST_PLAN.md)",
      "[Menus do Studio](docs/STUDIO_MENUS.md), [testes de bancada](docs/BENCH_TESTS.md), [código de configuração](docs/SETUP_CODE.md) e [provisionamento Bluetooth](docs/BLE_PROVISIONING.md)",
    ],
    "contributing_first": "Antes de um pull request, execute `ctest --test-dir build/host` and `python -I tools/armor_ci_validate.py`: tem de passar. Consulte [CONTRIBUTING.md](CONTRIBUTING.md) e o [código de conduta](CODE_OF_CONDUCT.md).",
    "languages_extra": "",
    "body": {
      "overview": r"""* **Duas placas, um só firmware:** um ESP32-S3-WROOM-1 N16R8 em Wi-Fi (o predefinido) e a Waveshare ESP32-S3-ETH no seu cabo Ethernet (DHCP ou um endereço fixo; a sua própria rede Wi-Fi mantém-se para lhe chegar a partir de um telemóvel). A imagem escolhe-se ao compilar (`tools/build_node.sh generic s3-wifi` ou `generic s3-eth`); a tabela de pinos, os pinos predefinidos das portas e a forma de entrada seguem a placa, e uma imagem só serve para a sua própria placa. Ambas compilam e estão testadas em anfitrião; nenhuma correu numa placa.
* **O firmware do nó** (ESP32-S3-WROOM-1 N16R8 em Wi-Fi, ou a Waveshare ESP32-S3-ETH no seu cabo): dez portas série, três UART de hardware e sete emuladas (até 19200 baud), cada uma independente e cada uma a ler um inversor, uma bateria ou um monitor em bruto, de modo que um nó pode ler só inversores, só baterias ou uma mistura.
* **O painel web do nó,** também o dos nós de radar: configuração com um código mostrado na consola USB, início de sessão e utilizadores, Wi-Fi (estação e ponto de acesso), broker, atualização pelo ar com retrocesso, registo, HTTPS, e as páginas das portas (com o que cada uma ouve, para protocolos ainda não descodificados) e das leituras, em oito idiomas.
* **Inversores Voltronic / MPP Solar** (Axpert, PIP, InfiniSolar e clones), RS232 a 2400 baud: as tramas e o seu CRC, e as leituras `QPIGS` (rede, saída, bateria, FV, bits de estado), `QMOD` (modo), `QPIWS` (avisos e avarias por nome) e `QPIRI` (valores nominais). Só se podem construir comandos de leitura: uma definição muda a forma como a casa é alimentada. Três dialetos, escolhidos na porta ou encontrados por ela (*auto*): PI30, REVO (outro `QPIGS`, respostas com soma de controlo) e PI18 (`^P005GS`: InfiniSolar V, LV5048, SunGoldPower), só de leitura.
* **Baterias Pylontech** (US2000, US3000, US5000): a tabela `pwr` da consola (tensão, corrente, temperaturas e estado de carga de cada módulo), `bat <n>` (a tensão e temperatura de cada célula) e `info <n>` (modelo, capacidade restante e total, ciclos), resumidas como um só conjunto com a sua capacidade e energia totais, e a trama RS485 com as suas duas verificações. Os formatos estão escritos de memória da consola pública e podem diferir entre firmwares. As colunas encontram-se pelos nomes do cabeçalho (o formato do US5000 V2.3 com as suas colunas Id, MosTempr e SysAlarm.St incluídas), a carga restante e o equilíbrio vêm de `bat`, e o modelo, a capacidade nominal e os ciclos de `info` e `stat`, pedidos uma vez e guardados durante meia hora.
* **O que um módulo Pylontech diz de si mesmo:** o seu modelo e as versões da sua placa e do seu software, as suas células e a corrente que admite, os contadores da sua vida (`stat`), a saúde de cada célula (`soh`, marcando a anormal) e a entrada mais recente do seu registo de eventos, com os nomes das proteções tal como a consola os imprime. A consola só lê, e um administrador pode descarregar como ficheiro de texto o que uma porta ouviu.
* **As mensagens do nó** (`armor/solar/<node>/<device>/state`, uma por inversor ou conjunto de baterias), definidas no ARMOR-COMMON com esquemas e vetores de conformidade; o que as portas produzem verifica-se contra elas.
* **Baterias ANT-BMS** (as placas pretas de baterias caseiras, 7S a 32S), UART de 3,3 V a 19200 baud: os dois protocolos do seu firmware (o nó pergunta num e depois no outro e fica com o que responde), com as células, temperaturas, estado de carga, corrente, capacidades e os estados dos MOSFET e do equilibrador, verificados contra tramas capturadas em quatro modelos reais. Só leitura: os seus comandos de escrita podem desligar uma bateria em carga. Um botão na página das portas lê também o modelo, a versão e as 56 definições de proteção e equilíbrio do BMS (protocolo mais recente), só de leitura.
* **Configuração a partir de um telemóvel por Bluetooth,** o mesmo canal que o do nó de radar: a aplicação ARMOR encontra o nó como `ARMOR-XXXXXX` e define o seu nome, Wi-Fi, endereço, broker e modo Bluetooth com os utilizadores do painel e o código de configuração ([o protocolo](docs/BLE_PROVISIONING.md)). Só escuta enquanto o nó não tem utilizador, a menos que se diga o contrário. O lado de rádio nunca correu numa placa.
* **A placa base com multiplexadores (o perfil *mux*):** três UART de hardware, cada uma atrás de um 74HC4052, servem até oito portas em grupos de 4, 2 e 2 que se revezam na sua linha, cada porta com a sua própria velocidade e polaridade, e um LED por porta através de um 74HC595; as células de um conjunto Pylontech alto podem ler-se em rotação. Para um inversor no dialeto padrão, a **segunda entrada FV** (`QPIGS2`) e as **unidades de um sistema em paralelo** (`QPGS`) são leituras opcionais. Nada disto correu numa placa.
* **Atualizações pelo ar assinadas:** o nó só instala do GitHub uma imagem cujo SHA-256 coincide e que leva uma assinatura Ed25519 válida do responsável (a chave pública está no firmware, a privada nunca sai do responsável); um ficheiro carregado à mão por um administrador no painel continua a ser aceite. As páginas e mensagens do painel estão em oito idiomas.
* **Emparelhamento Bluetooth com PIN:** o PIN de seis dígitos deriva do código de configuração, é impresso na consola USB e mostrado a um administrador no painel; o telemóvel tem de o introduzir antes de poder escrever as definições do nó.
* **Ainda não:** a ligação Bluetooth do ANT-BMS (o nó usa o cabo, o mais estável dos dois) e uma execução numa placa real com equipamento real.
* **Só a casa pode usar o painel:** o painel responde por omissão à rede privada (ou às redes que o dono indicar, como uma VPN), recusa uma lista que deixaria de fora quem a guarda, conta as palavras-passe erradas por pessoa e por endereço e funciona atrás do proxy do servidor para ser alcançado de fora de casa sem publicar o nó.
* **Desconhecido não é nenhum:** um inversor REVO não tem consulta de avisos, por isso a sua mensagem leva `warnings_known: false` e o Studio mostra os avisos como desconhecidos em vez de "nenhum".
* **Ligação cifrada opcional ao broker (TLS):** desativada por predefinição, por isso o nó fala MQTT sem cifra como antes. Um interruptor e uma caixa para o certificado da autoridade própria da instalação (PEM, no máximo 2 KB) na página Broker fazem-no ligar-se com `mqtts://`, confiar só nessa autoridade e verificar que o certificado do broker foi feito para o endereço alcançado; o que não for um único certificado PEM é recusado. Coberto por testes no computador; o handshake ainda não foi executado numa placa.
* **Relatório de saúde:** cerca de uma vez por minuto o nó publica há quanto tempo está ligado e porque reiniciou da última vez, a memória livre, a ligação e o sinal Wi-Fi, quantas vezes se ligou ao broker e o último erro que registou (`armor/health/<nó>`, o contrato `node_health` do ARMOR-COMMON). O código que o constrói é partilhado por todos os nós e testado num computador; nunca correu numa placa.
* **Escrita em baterias Pylontech (desligada por omissão):** só operações tipificadas - relógio, contadores e registos, reinício, capacidade, a reposição do nível de carga, limites e proteções, saídas, número de série, memória externa, firmware por XMODEM-1K e uma consola de especialista com lista de bloqueio - em dois passos (preparar e executar com um token de uso único), lendo a bateria antes e depois, com a palavra-passe de serviço guardada só no nó e uma consola simulada para os testes. Não experimentado numa bateria real: veja o [plano de testes de bancada](docs/BATTERY_BENCH_TEST_PLAN.md).
* **Controlo a partir do servidor:** o Studio pode reiniciar o nó de forma limpa, pô-lo em pausa até uma hora (retoma sozinho), pôr o seu trabalho em espera (sem fim, mantida nos reinícios, o nó continua ligado e a responder), fazê-lo mostrar-se, pedir um instantâneo de diagnóstico e marcá-lo em manutenção (`armor/control/<nó>/...`, o contrato `node_control` do ARMOR-COMMON). Cada ordem tem dois passos com um token de uso único que pertence a essa operação, só o servidor as pode escrever no broker, e não existe reposição de fábrica, apagamento nem sono profundo. Enquanto o nó está em pausa ou em espera, não escreve em nenhuma bateria (uma operação em curso ainda pode ser cancelada) e continua a ler inversores e baterias. O código é partilhado por todos os nós e testado num computador; ainda não correu numa placa.
* **Os valores absurdos são nomeados, não escondidos:** quando um inversor envia um número impossível, o nó mantém-no no limite do contrato e nomeia-o em `clamped`, pelo que o servidor o mostra como não real; e o despejo em bruto de uma porta só é feito enquanto o painel o está a ver.
* **Diagnóstico sem cabo:** depois de um arranque que não foi limpo (um bloqueio, um watchdog, uma quebra de alimentação, uma reserva de memória falhada), o relatório de saúde diz o motivo durante dez minutos; uma falha deixa o seu core dump para ver, descarregar ou apagar a partir do painel; as definições guardadas são copiadas antes de cada instalação de firmware e recuperadas se uma atualização as danificar; e um administrador pode pedir ao nó, através do servidor, um pacote de diagnóstico ou o seu registo com um token de utilização única.
* **Selagem opcional dos segredos guardados:** desativada por predefinição (`security.seal_secrets`, ou `nodes.nvs_encryption` do servidor). Ativada, as palavras-passe, os tokens, as chaves, os PIN e os hashes de palavras-passe que o nó guarda ficam selados com ChaCha20-Poly1305 e tudo o resto continua legível; ativá-la ou desativá-la reescreve-os sem perder nada, mesmo que o nó pare a meio. Não se queima nenhum eFuse nem se cifra a flash: a chave está numa partição do mesmo chip, pelo que **não** protege contra quem tenha a placa, e um nó instalado antes dessa partição mantém os segredos como estavam até ser gravado com a nova tabela de partições.""",
      "role": r"""O ARMOR-NODE-SOLAR é a porta de ligação entre o equipamento solar da casa e a família. Lê inversores e baterias por até dez portas série e publica o que lê para o [ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER), que guarda o histórico, os totais e os alarmes; os menus *Inversores* e *Baterias* do [ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) e o ecrã Solar do [ARMOR-ANDROID-CONTROL](https://github.com/JuanenRac/ARMOR-ANDROID-CONTROL) mostram-no. Só lê: nunca escreve uma definição em nenhum equipamento.

| Nome | Como | Para quê |
|---|---|---|
| ARMOR-SERVER | MQTT `armor/solar/<node>/<device>/state` | Recebe uma mensagem por inversor ou pilha de baterias; ordena a manutenção de uma bateria |
| ARMOR-STUDIO | menus, ligação ao painel | Mostra inversores e baterias e abre o painel do nó |
| ARMOR-ANDROID-CONTROL | Bluetooth | Configura o nó no terreno e mostra os ecrãs de energia |
| ARMOR-COMMON | contrato solar | As mensagens são verificadas com os seus esquemas; o firmware comum é copiado dele |""",
      "architecture": r"""<p align="center">
  <img src="images/architecture.svg" alt="Arquitetura de ARMOR-NODE-SOLAR: quem o chama, o que contém e de que depende" width="100%">
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
| Uma bateria escrita por engano ou por um atacante | Três trancas: a definição do nó `battery.write_enabled` (administradores) com a palavra-passe de serviço da bateria, `ARMOR_BATTERY_WRITE=1` do servidor, e a lista de acesso do broker para `armor/solar/<nó>/maintenance/command` e `.../result` |
| Uma ordem de escrita repetida ou roubada | Dois passos (armar, depois executar com um token de uso único), janela de armação de 120 s, 30 s de arrefecimento entre escritas numa porta, 3 falhas em 10 minutos bloqueiam-na 5; o número de série da bateria digita-se de novo, a bateria tem de estar em repouso e sem alarme crítico, e a imagem de firmware guarda-se 30 minutos e verifica-se |
| Escrever num inversor ou num ANT-BMS | Os comandos de escrita de um inversor (uma definição muda como a casa é alimentada) e de um ANT-BMS (pode desligar uma bateria sob carga) nem sequer se podem construir |
| Números absurdos mostrados como reais | Um valor impossível é retido no limite do contrato e nomeado em `clamped`, para o servidor o mostrar como não real; um inversor REVO não tem consulta de avisos, por isso a sua mensagem diz `warnings_known: false` em vez de afirmar que não há avisos |

Nenhuma trama foi lida de um inversor ou bateria reais; os formatos estão escritos a partir de documentos públicos e de memória, e as tramas ANT-BMS dos testes foram capturadas por outras pessoas. Leia [docs/BATTERY_MAINTENANCE.md](docs/BATTERY_MAINTENANCE.md) e [SECURITY.md](SECURITY.md).""",
      "interfaces": r"""| Parte | O que define |
|---|---|
| MQTT | `armor/solar/<nó>/<dispositivo>/state` (uma mensagem por inversor ou pilha de baterias, tipo `inverter` ou `battery` do contrato do ARMOR-COMMON), `armor/solar/<nó>/maintenance/{command,result}`, `armor/health/<nó>` (testamento), `armor/control/<id>/{command,result,maintenance}` e `armor/control/all/command` |
| Portas | 10 portas série (3 UART de hardware e 7 emuladas, até 19200 baud se emuladas); por porta um tipo: `voltronic` (2400 baud, a cada 5 s), `pylontech` (115200, a cada 10 s), `ant` (19200, a cada 5 s) ou `raw` (9600, só escuta, não publica nada); dialetos de inversor `auto`, `pi30`, `revo`, `pi18`; o perfil mux tem 3 grupos de portas |
| Consultas | Voltronic: `QPIGS`, `QMOD`, `QPIWS`, `QPIRI` (e `QPIGS2`, `QPGS` num inversor padrão com o mux); consola Pylontech: `pwr`, `bat <n>`, `info <n>`, `stat`, `soh`, registo de eventos, até 8 módulos pedidos célula a célula |
| Painel | As rotas da família (`tests/check_routes.py` verifica que toda a rota que o painel chama existe) mais as páginas de portas e leituras; 51 códigos de erro com texto em oito línguas (772 linhas em `panel/text.js`); os menus do Studio estão em [docs/STUDIO_MENUS.md](docs/STUDIO_MENUS.md) |""",
      "configuration": r"""| Variável | Predefinição | O que define |
|---|---|---|
| `enabled`, `kind`, `name`, `baud`, `rx`, `tx`, `de`, `poll_s`, `modules`, `dialect` | - | As definições de cada porta: ativada ou não, o tipo, o nome do dispositivo no tópico, a velocidade (0 = a do tipo), os pinos (e o pino DE/RE de um RS485), o período de consulta (0 = o do tipo), o número de módulos e o dialeto do inversor; no máximo 3 redes de reserva e 2 brokers de reserva |
| `battery.write_enabled` | off | A tranca do nó para escrever numa bateria Pylontech (administradores, com a palavra-passe de serviço da bateria, que nunca sai do nó) |
| `CONFIG_ARMOR_BOARD_S3_WIFI` / `_S3_ETH` | wifi | A placa: ESP32-S3-WROOM-1 N16R8 por Wi-Fi (predefinição) ou a Waveshare ESP32-S3-ETH |
| `CONFIG_ARMOR_NODE_ID`, `_SETUP_CODE`, `_FLEET_SECRET`, `_MQTT_*`, `_HEARTBEAT_S`, `_BLE_SETUP_MINUTES`, `_BOOT_FACTORY_RESET` | - | As definições que todos os nós partilham: o nome (vazio dá `armor-` e os últimos bytes do MAC), o código de configuração (vazio: aleatório), o segredo de frota (16+ caracteres, nunca no repositório), as primeiras definições do broker, o batimento (de 2 a 300 s), os minutos de configuração Bluetooth (de 1 a 120) e a reposição com BOOT (8 s nos primeiros 30 s) |""",
      "quickstart": r"""**Requisitos:** um compilador C++17 para os testes de anfitrião; o contentor ESP-IDF 5.5.5 para compilar a imagem; uma ESP32-S3-WROOM-1 N16R8 ou uma Waveshare ESP32-S3-ETH.

```bash
cmake -S tests -B build/host && cmake --build build/host && ctest --test-dir build/host   # host tests, -Werror
build/host/emit_poller_samples | python tests/check_samples.py   # what the ports make is accepted by ARMOR-COMMON
tools/build_node.sh generic                       # the image for the N16R8 board in the ESP-IDF container: dist/generic-s3-wifi.bin
tools/build_node.sh generic s3-eth               # the same firmware for the Waveshare ESP32-S3-ETH (Ethernet): dist/generic-s3-eth.bin
node tools/panel_mock.mjs --user admin:adminpass123   # the panel without a board
```

Veja o [guia do firmware](docs/NODE_FIRMWARE.md) (a placa, as portas, o primeiro arranque e a lista de verificação de bancada) e as [notas de ligação](docs/NODE_HARDWARE.md).""",
      "testing": r"""```bash
cmake -S tests -B build/host && cmake --build build/host && ctest --test-dir build/host
python -I tools/armor_ci_validate.py
```

18 programas de teste de anfitrião e 6 verificações Python correm com `ctest`; 11824 verificações contadas pelos programas de anfitrião, compiladas com `-Werror`.

Verificações Python: os textos do painel em oito línguas, as tarefas, os caminhos de gravação, a sessão Bluetooth sob o seu bloqueio e as rotas que o painel chama (e, em alguns nós, os códigos HTTP ou os glifos dos tipos de letra)

Os testes de anfitrião precisam de qualquer compilador C++17 (Linux, WSL, MSYS2); o painel web também é exercitado num navegador real contra um nó de substituição (`tools/panel_mock.mjs`, `tools/panel_browser_test.mjs`).

O `test_clock` só imprime `ok` e não tem contador; cada um dos outros programas comunica as suas verificações. As tramas reais dos testes estão em `tests/pylontech_real.hpp`, `pylontech_us2000_real.hpp`, `pylontech_logs_real.hpp`, `ant_frames.hpp` e `battery_bench.hpp`.""",
      "build": "`tools/build_node.sh` compila a imagem no contentor ESP-IDF 5.5.5 e a versão leva a imagem, o seu SHA-256 e a sua assinatura Ed25519, uma por placa; a imagem grava-se por USB-C da primeira vez e depois atualiza-se a partir do painel.",
      "troubleshooting": r"""| Vê | Porque | Faça |
|---|---|---|
| Perdeu a palavra-passe ou o nó já não se liga à rede | Um nó em configuração e sem endereço após 90 s abre o seu próprio Wi-Fi `ARMOR-SETUP-xxxxxx` (abra `http://192.168.4.1/`) | Para recomeçar mantenha BOOT 8 segundos nos primeiros 30 segundos após ligar (apaga definições e utilizadores), ou use *Reposição de fábrica* no painel |
| Uma atualização do GitHub é recusada | A versão não traz soma de verificação nem assinatura, não coincidem (`e_no_checksum`, `e_no_signature`, `e_checksum_mismatch`, `e_bad_signature`), não traz imagem para esta placa (`e_no_asset_for_board`) ou é de outro projeto (`e_wrong_firmware`) | O nó não mudou; tente de novo ou deixe um administrador enviar o ficheiro à mão |
| Uma escrita numa bateria é recusada com um código | `serial_mismatch`, `not_pylontech`, `no_battery`, `unknown_model`, `not_idle`, `critical_alarm`, `busy`, `cooldown`, `locked`, `not_armed`, `bad_token`, `expired`, `disabled`, `image_missing`, `image_mismatch`...: o nó recusa o que não é exatamente a operação armada | Leia o código no resultado, corrija a causa e arme a operação de novo (veja [docs/BATTERY_MAINTENANCE.md](docs/BATTERY_MAINTENANCE.md)) |
| Uma porta não publica nada | A porta está desligada, o seu tipo é `raw` (só escuta), a velocidade ou os pinos não coincidem com o equipamento, ou o equipamento não responde | Verifique as definições da porta e a cablagem em [docs/NODE_HARDWARE.md](docs/NODE_HARDWARE.md); o painel mostra o despejo bruto de uma porta enquanto a observa |""",
      "structure": r"""<p align="center">
  <img src="images/repository-structure.svg" alt="Estrutura do repositório de ARMOR-NODE-SOLAR" width="100%">
</p>

<details>
<summary>Versão em texto da árvore</summary>

```text
ARMOR-NODE-SOLAR/
├── main/                                o firmware: um componente ESP-IDF
├── core/                                a lógica sem ESP-IDF, testada num computador
├── panel/                               o painel web embebido no firmware
├── tests/                               testes de anfitrião e verificações Python
├── docs/                                10 guias: protocolos, mensagens, manutenção, hardware
├── tools/                               ferramentas de compilação, empacotamento e verificação
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
├── sdkconfig.board.s3-eth               as definições de uma placa
├── sdkconfig.board.s3-wifi              as definições de uma placa
├── secrets/                             exemplo do ficheiro do nó (os verdadeiros não são versionados)
├── build-test.sh build-test.bat         executar os testes pelo fluxo partilhado
└── .gitattributes .gitignore            definições do Git
```

</details>""",
      "roadmap": r"""**Limites conhecidos hoje**

* As tramas, somas de verificação e leituras de Voltronic, Pylontech e ANT-BMS são verificadas contra as tramas documentadas e amostras gravadas; nenhum falou ainda com um inversor ou uma bateria reais.
* O painel web foi exercitado num navegador contra uma simulação do nó, não numa placa.
* Nenhuma placa construída nem inversor ou bateria ligados: nada funcionou ainda em equipamentos reais.
* O código de configuração, o acesso com limite de palavras-passe erradas, o PIN Bluetooth e as atualizações assinadas estão testados no anfitrião; não houve revisão independente.
* As verificações de hash e de assinatura Ed25519 e a lógica de retrocesso passam no anfitrião; uma atualização pelo ar nunca foi executada numa placa.
* A escrita nas baterias Pylontech está desativada por predefinição e só foi testada contra um simulador.

**A seguir**

* Correr o nó numa placa real com um inversor e baterias reais, e depois a ligação Bluetooth do ANT-BMS (hoje usa-se o cabo), a atualização pelo ar e as escritas numa bateria.""",
    },
  },
}
