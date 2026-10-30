# The facts that do not depend on the language, and the words of every language, of ARMOR-NODE-ELECTRICAL, in the universal README layout.
# Copyright (C) 2026 JuanenRac (Electro Hobby 3D). GPL-3.0-or-later.

FACTS = {
  "emoji": "⚡",
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
      "Meters",
      "PZEM--004T%20%2F%20017",
      "ffb020",
    ],
    [
      "Checks",
      "376%2C195",
      "2ea44f",
    ],
    [
      "Tests",
      "382264%20checks",
      "2ea44f",
    ],
  ],
}

TEXT = {
  "en": {
    "tagline": "Electrical node: reads the voltages, currents, power and energy of the house's AC and DC network and holds the rules for switching it (host-tested core and a firmware that builds; it has never run on a board)",
    "honest": "The core (the frames of the PZEM-004T v3 and PZEM-017 meters, the bus that asks them, the message of the node, the analogue inputs and the rules for switching: 382,264 checks in 19 test programs, 375,036 of them on the switching rules) is tested on a computer with stand-in meters and contactors, and the messages it makes are accepted by ARMOR-COMMON. The firmware of the node (the settings, the serial line, the Meters and Readings pages of its panel, Bluetooth, signed updates) builds in the ESP-IDF 5.5.5 container for both boards. **It has never run on a board, nothing has been connected to a meter or a contactor, and nothing here switches anything.**",
    "glance": [
      [
        "Role",
        "Electrical field node: meters, inputs and switching (family: Field Nodes, parent: ARMOR-COMMON)",
      ],
      [
        "Stack",
        "C++17, ESP-IDF 5.5.5, ESP32-S3",
      ],
      [
        "Tests",
        "382264 checks in 19 host programs and 5 Python checks (`ctest`)",
      ],
      [
        "Equipment",
        "PZEM-004T v3 and PZEM-017 meters (up to 16), analogue inputs, relays; switching off by default",
      ],
      [
        "Runs on",
        "An ESP32-S3 board (Ethernet or Wi-Fi); host tests on any computer",
      ],
      [
        "On real hardware",
        "None yet: no board built and no meter or contactor connected; nothing switches anything",
      ],
      [
        "License",
        "GPL-3.0-or-later",
      ],
    ],
    "status": {
      "software": "The firmware builds in the ESP-IDF 5.5.5 container for both boards (Wi-Fi and Ethernet).",
      "tests": "382,264 checks in 19 host programs pass (`ctest`), 375,036 of them on the switching rules; the meters and contactors are stand-ins.",
      "protocols": "The PZEM-004T v3 and PZEM-017 frames and readings are checked against the documented frames and recorded samples; no meter has answered yet.",
      "ui": "The Meters and Readings pages of the web panel are exercised in a browser against a stand-in node, not on a board.",
      "hardware": "No board built and no meter or contactor connected: nothing has run on real equipment yet.",
      "security": "The set-up code, the login with a limit on wrong passwords, the Bluetooth PIN and the signed updates are tested on the host; there has been no independent review.",
      "updates": "The hash and Ed25519 signature checks and the rollback logic pass on the host; an update over the air has never been run on a board.",
      "writing": "The rules for switching contactors are tested only against stand-in contactors; nothing here has switched anything real.",
      "integration": "The messages of the node are validated against the shared schemas and conformance vectors of ARMOR-COMMON. Its MQTT client is played against a real Mosquitto in the tests; no board has sent them to a server yet.",
      "docs": "Eight languages, the firmware guide, the wiring notes and the changelog are up to date.",
    },
    "docs": [
      "[Safety](docs/SAFETY.md) and [switching](docs/SWITCHING.md): what the design assumes and how a transfer goes",
      "[Messages](docs/ELECTRICAL_MESSAGES.md), [protocols](docs/PROTOCOLS.md) and [Zigbee](docs/ZIGBEE.md)",
      "[Design](docs/DESIGN.md), [hardware](docs/HARDWARE.md), [base board](docs/BASE_BOARD.md) and [node firmware](docs/NODE_FIRMWARE.md)",
      "[Bench tests](docs/BENCH_TESTS.md), [set-up code](docs/SETUP_CODE.md) and [Bluetooth provisioning](docs/BLE_PROVISIONING.md)",
    ],
    "contributing_first": "Before a pull request run `ctest --test-dir build/host` and `python -I tools/armor_ci_validate.py`: it must pass. See [CONTRIBUTING.md](CONTRIBUTING.md) and the [code of conduct](CODE_OF_CONDUCT.md).",
    "languages_extra": "",
    "body": {
      "overview": r"""* **Reading the meters:** the Modbus RTU frames of the Peacefair **PZEM-004T v3** (AC) and **PZEM-017** (DC): the CRC, the request that reads the registers and the decoding of the reply (voltage, current, power, energy, frequency, power factor, alarm). Only the read request is built: the ones that write to a meter (its address, its thresholds, the reset of its energy) are not built anywhere. A reply that does not fit, or holds a value no real meter could give, is refused.
* **The bus:** a line with several meters is asked one at a time, with a timeout; the last good reading of each is kept and a meter that goes silent stops being published after ten seconds.
* **The message** `armor/electrical/<node>/state`: one entry per channel (a circuit, a line, the grid input, a DC bus) with AC or DC, voltage, current, power, energy, frequency, power factor, the state of a switch as the node sees it and an alarm; it is in the shared contract and carries a state, never a command.
* **The rules for switching,** apart from any hardware: a controller for the transfer between two sources that never commands both, needs the switching allowed, the node armed just before, both contactors confirmed open for the whole dead time, and turns a contactor that does not show what it was told into a fault that stays until it is acknowledged. **Switching is off by default and nothing drives any hardware.**
* **The commands to a switch, not activated:** the state message can carry the state of the node's switches, and the shared contract has a command (`arm`, then `close_a` or `close_b` with a one-time token, `open`, `acknowledge`) and the node's answer; the core reads and answers them with the rules above, tested against the shared vectors and with stand-in contactors. No firmware image includes it, so nothing can drive a contactor, and ARMOR-SERVER refuses to send a command unless it was turned on (`ARMOR_ELECTRICAL_SWITCHING=1`) and the broker's ACL allows it.
* **Where it shows:** the *Electrical Designer* of ARMOR-STUDIO draws the house's network and shows on each element what its channel measures; ARMOR-SERVER keeps the readings, their history and the sums.
* **The firmware of the node** (ESP32-S3-WROOM-1 N16R8 on Wi-Fi, or the Waveshare ESP32-S3-ETH on its cable): the settings, one serial line for up to sixteen meters and the web panel of the other nodes (set-up, users, Wi-Fi, broker, update over the air, HTTPS) with its own Meters and Readings pages, in eight languages. It only reads: the rules for switching are not linked into it. See [the firmware](docs/NODE_FIRMWARE.md).
* **Configuration from a phone over Bluetooth,** the same channel as the radar node's: the ARMOR app finds the node as `ARMOR-XXXXXX` and sets its name, Wi-Fi, address, broker and Bluetooth mode with the panel's users and set-up code ([the protocol](docs/BLE_PROVISIONING.md)). It listens only while the node has no user, unless told otherwise. The radio side has never run on a board.
* **Signed over-the-air updates:** the node installs from GitHub only an image whose SHA-256 matches and that carries a valid Ed25519 signature of the maintainer (the public key is in the firmware, the private one never leaves the maintainer); a file uploaded by hand by an administrator in the panel is still accepted. The pages and messages of the panel are in eight languages.
* **Bluetooth pairing with a PIN:** the six-digit PIN is derived from the set-up code, printed on the USB console and shown to an administrator in the panel; the phone has to enter it before it may write the node's settings.
* **Not yet:** the firmware running on a board, the hardware, any measurement of a real installation and any switching.
* **Only the house may use the panel:** the panel answers the private network by default (or the networks its owner lists, such as a VPN), refuses a list that would lock out whoever saves it, counts wrong passwords for each person as well as each address, and works behind the server's proxy so that it can be reached from outside the house without publishing the node.
* **Estimates say so:** a channel made from a current input carries `power_estimated`, so Studio and the server show its power as an estimate (apparent power from a current and a nominal voltage) and mark a grid figure that includes one.
* **Optional encrypted link to the broker (TLS):** off by default, so the node talks plain MQTT as before. A switch and a box for the certificate of the installation's own authority (PEM, at most 2 KB) in the Broker page make it connect with `mqtts://`, trust that authority only and check that the broker's certificate was made for the address it reached; anything that is not one PEM certificate is refused. Covered by host tests; the handshake has not been run on a board yet.
* **Health report:** about once a minute the node publishes how long it has been up and why it last restarted, its free memory, its link and Wi-Fi signal, how many times it connected to the broker and the last error it logged (`armor/health/<node>`, the `node_health` contract of ARMOR-COMMON). The code that builds it is shared by every node and tested on a computer; it has not run on a board.
* **Control from the server:** Studio can restart the node cleanly, pause it for up to an hour (it resumes by itself), put its work in standby (no end, kept across restarts, the node stays connected and keeps answering), make it show itself, ask for a diagnostics snapshot and mark it as in maintenance (`armor/control/<node>/...`, the `node_control` contract of ARMOR-COMMON). Every order takes two steps with a one-time token that belongs to that operation, only the server may write them on the broker, and there is no factory reset, no erase and no deep sleep. While the node is paused or in standby every relay is opened and none moves, whoever asks (the panel, the broker or a central); the meters keep being read. The code is shared by every node and tested on a computer; it has not run on a board.
* **Readings that say how fresh they are:** each meter channel carries the age of its reading and how many requests to the meter failed, so the server tells a real 0 W from a meter that stopped answering; and a hung meters task restarts the board through the watchdog.
* **Diagnostics without a cable:** after a start that was not clean (a crash, a watchdog, a sag of the supply, a failed allocation) the health report says why for ten minutes; a crash leaves its core dump to look at, download or erase from the panel; the stored settings are copied before every firmware install and recovered if an update damages them; and an administrator can ask the node, through the server, for a diagnostic package or its log with a one-time token.
* **Relay interlock:** a relay can name another that must never be closed at the same time (the two sources of a load, the two directions of a motor); a request to close one while the other is closed is refused from the panel, the broker and the central alike, and the node never opens the partner by itself. Tested on a computer; not run on a board.
* **Read-only reading of the meters' own settings:** after the first good reading and every `bus.check_settings_s` (600 s, 0 = never) the node reads the PZEM holding registers (004T v3: power threshold and address; 017: voltage thresholds, address and shunt) in the same turn as the measurements, and warns when the stored address is not the one it uses; nothing is written to the meter.
* **Optional sealing of stored secrets:** off by default (`security.seal_secrets`, or the server's `nodes.nvs_encryption`). When on, the passwords, tokens, keys, PINs and password hashes the node stores are kept sealed with ChaCha20-Poly1305 and everything else stays readable; turning it on or off rewrites them with nothing lost, even if the node stops half-way. No eFuse is burned and the flash is not encrypted: the key lives in a partition of the same chip, so it does **not** protect against someone who holds the board, and a node installed before that partition existed keeps its secrets as they were until it is flashed with the new partition table.""",
      "role": r"""ARMOR-NODE-ELECTRICAL measures the house's AC and DC network through its meters and holds the rules for switching between sources. It publishes the readings for [ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER), which keeps their history and the energy of each day and raises the alarms; the *Electrical* menu and the *Electrical Designer* of [ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) and the electrical screen of [ARMOR-ANDROID-CONTROL](https://github.com/JuanenRac/ARMOR-ANDROID-CONTROL) show it. Switching is designed (arm, a one-time token, the interlock, the confirmation of both contactors) but not activated.

| Name | How | What for |
|---|---|---|
| ARMOR-SERVER | MQTT `armor/electrical/<id>/{state,command,result}` | Receives the channels and orders a transfer (only when switching is on in three places) |
| ARMOR-STUDIO | Electrical menu, Electrical Designer | Shows the channels and the alarms and opens the node's panel |
| ARMOR-ANDROID-CONTROL | Bluetooth | Sets the node up in the field and shows the channels |
| ARMOR-COMMON | electrical contract | The messages are checked against its schemas; the common firmware is copied from it |""",
      "architecture": r"""<p align="center">
  <img src="images/architecture.svg" alt="ARMOR-NODE-ELECTRICAL architecture: who calls it, what it holds and what it depends on" width="100%">
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
| Dangerous mains or DC on the board | The node only reads the PZEM modules (closed modules, isolated serial line) and never carries mains on its board; whatever switches is a separate stage tested on the bench with a lamp and an isolating transformer |
| Two sources closed at once | The transfer interlock never orders both: it needs switching allowed, the node armed just before and both contactors confirmed open for the whole dead time (`dead_time_ms` 2000 by default); a contactor that does not show what was ordered is a fault that stays until acknowledged (`kDidNotOpen`, `kDidNotClose`); a mechanical interlock between the contactors is still required |
| A repeated order, or switching nobody asked for | `arm` gives a single-use 64-bit token that `close_a` or `close_b` must carry, inside `arm_window_ms`; orders are never retained; at most 4 switches; switching is OFF unless the firmware allows it (`switching_enabled`), the server runs with `ARMOR_ELECTRICAL_SWITCHING=1` and the broker's access list is open for that node |
| A fault, a lost feedback or switching off | Each controller answers with ALL coils open (fail open; whether open is safe for the load is for the installation to decide); the state in the message is what the auxiliary contact shows, not what was ordered; relay pairs are interlocked and the node never opens the partner by itself |
| A stale reading shown as real | A mute meter stops being published after 10 s; each channel carries the age of its reading and the number of failed requests; a stuck meter task restarts the board by watchdog; every `bus.check_settings_s` (600 s, 0 = never) the meters' settings are read (read only) and a changed address is reported |

Mains (230 V AC) and the DC of a battery bank can kill and start fires. [docs/SAFETY.md](docs/SAFETY.md) says what the design assumes; it is not a design of an installation and it does not replace the regulations of the country or a qualified installer. Nothing here switches anything today.""",
      "interfaces": r"""| Part | What it sets |
|---|---|
| MQTT | `armor/electrical/<id>/state` (one channel per input: AC or DC, voltage, current, power, energy, frequency, power factor, switch state, alarm; ARMOR-COMMON contract), `armor/electrical/<id>/command` and `/result`, `armor/device/<id>/<relay>/{state,set}`, `armor/health/<id>`, `armor/control/<id>/...` |
| Commands | `arm`, `close_a`, `close_b` (with the token), `open` and `acknowledge` (clears a fault) |
| Meters | Peacefair PZEM-004T v3 (AC) and PZEM-017 (DC) by Modbus RTU, up to 16 on one serial line; only the read request is ever built (the one that writes address or thresholds does not exist); analogue inputs, contacts and relays on the base board; a Zigbee bridge ([docs/ZIGBEE.md](docs/ZIGBEE.md)) |""",
      "configuration": r"""| Variable | Default | What it sets |
|---|---|---|
| `bus.check_settings_s` | 600 | Seconds between the read-only checks of the meters' settings (0 = never) |
| `dead_time_ms`, `confirm_timeout_ms` | 2000 | The dead time of a transfer and how long a contactor has to show what was ordered |
| `switching_enabled` | off | Switching is OFF unless this setting, the server (`ARMOR_ELECTRICAL_SWITCHING=1`) and the broker's access list all allow it |
| `CONFIG_ARMOR_NODE_ID`, `_SETUP_CODE`, `_FLEET_SECRET`, `_MQTT_*`, `_HEARTBEAT_S`, `_BLE_SETUP_MINUTES`, `_BOOT_FACTORY_RESET` | - | The settings every node shares: the name (empty gives `armor-` and the last bytes of the MAC), the set-up code (empty: random), the fleet secret (16+ characters, never in the repository), the first broker settings, the heartbeat (2 to 300 s), the minutes of Bluetooth set-up (1 to 120) and the reset with BOOT (8 s in the first 30 s) |""",
      "quickstart": r"""**Requirements:** a C++17 compiler for the host tests; the ESP-IDF 5.5.5 container to build the image; an ESP32-S3 board (Ethernet or Wi-Fi).

```bash
cmake -S tests -B build/host && cmake --build build/host && ctest --test-dir build/host   # host tests, -Werror
node tools/panel_mock.mjs --user admin:adminpass123   # the panel without a board
tools/build_node.sh generic s3-wifi                  # the image in the ESP-IDF container (or s3-eth)
```

See the [firmware guide](docs/NODE_FIRMWARE.md) and the [Bluetooth channel](docs/BLE_PROVISIONING.md).

See the [design](docs/DESIGN.md), the [safety notes](docs/SAFETY.md), the [rules for switching](docs/SWITCHING.md), the [protocols](docs/PROTOCOLS.md) and the [messages](docs/ELECTRICAL_MESSAGES.md).""",
      "testing": r"""```bash
cmake -S tests -B build/host && cmake --build build/host && ctest --test-dir build/host
python -I tools/armor_ci_validate.py
```

19 host test programs and 5 Python checks run under `ctest`; 382264 checks counted by the host programs, built with `-Werror`.

Python checks: the panel texts in eight languages, the tasks, the save paths, the Bluetooth session under its lock and the routes the panel calls (and, in some nodes, the HTTP codes or the glyphs of the fonts)

The host tests need any C++17 compiler (Linux, WSL, MSYS2); the web panel is also exercised in a real browser against a stand-in node (`tools/panel_mock.mjs`, `tools/panel_browser_test.mjs`).

Most of the checks are exhaustive sweeps of the switching rules (`test_switch_set` and `test_interlock`: 375,036); the meters and contactors are stand-ins. `test_clock` prints only `ok`.""",
      "build": "`tools/build_node.sh` builds the image in the ESP-IDF 5.5.5 container and the release carries the image, its SHA-256 and its Ed25519 signature, one per board; the image is written by USB-C the first time and updated from the panel afterwards.",
      "troubleshooting": r"""| You see | Because | Do |
|---|---|---|
| You lost the password or the node no longer joins the network | A node with set-up and no address after 90 s opens its own Wi-Fi `ARMOR-SETUP-xxxxxx` (open `http://192.168.4.1/`) | To start again hold BOOT for 8 seconds in the first 30 seconds after power-up (erases settings and users), or use *Factory reset* in the panel |
| An update from GitHub is refused | The release has no checksum or signature, they do not match (`e_no_checksum`, `e_no_signature`, `e_checksum_mismatch`, `e_bad_signature`), has no image for this board (`e_no_asset_for_board`) or is for another project (`e_wrong_firmware`) | Nothing changed on the node; try again or let an administrator upload the file by hand |
| A switch shows a fault | The contactor did not show open or closed as ordered (`kDidNotOpen`, `kDidNotClose`); it stays until acknowledged | Check the wiring of the auxiliary contact, then send `acknowledge` |
| A command is refused | Switching is off (`switching_enabled` false), the token is invalid or expired, or the node was not armed just before | Arm again and send the order with the new token |""",
      "structure": r"""<p align="center">
  <img src="images/repository-structure.svg" alt="Repository structure of ARMOR-NODE-ELECTRICAL" width="100%">
</p>

<details>
<summary>Text version of the tree</summary>

```text
ARMOR-NODE-ELECTRICAL/
├── main/                                the firmware: an ESP-IDF component
├── core/                                the logic with no ESP-IDF, tested on a computer
├── panel/                               the web panel embedded in the firmware
├── tests/                               host tests and Python checks
├── docs/                                12 guides: safety, switching, messages, hardware
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

* The PZEM-004T v3 and PZEM-017 frames and readings are checked against the documented frames and recorded samples; no meter has answered yet.
* The Meters and Readings pages of the web panel are exercised in a browser against a stand-in node, not on a board.
* No board built and no meter or contactor connected: nothing has run on real equipment yet.
* The set-up code, the login with a limit on wrong passwords, the Bluetooth PIN and the signed updates are tested on the host; there has been no independent review.
* The hash and Ed25519 signature checks and the rollback logic pass on the host; an update over the air has never been run on a board.
* The rules for switching contactors are tested only against stand-in contactors; nothing here has switched anything real.

**Next**

* Try the meters, the contactors and the switching rules on a bench with a lamp and an isolating transformer, then a real board with the update over the air.""",
    },
  },
  "es": {
    "tagline": "Nodo eléctrico: lee las tensiones, corrientes, potencia y energía de la red AC y DC de la casa y guarda las reglas para maniobrarla (núcleo probado en el PC y un firmware que compila; nunca ha corrido en una placa)",
    "honest": "El núcleo (las tramas de los medidores PZEM-004T v3 y PZEM-017, el bus que los pregunta, el mensaje del nodo, las entradas analógicas y las reglas de conmutación: 382.264 comprobaciones en 19 programas de test, 375.036 de ellas sobre las reglas de conmutación) se prueba en un ordenador con medidores y contactores de pega, y los mensajes que hace los acepta ARMOR-COMMON. El firmware del nodo (los ajustes, la línea serie, las páginas Medidores y Lecturas de su panel, Bluetooth, actualizaciones firmadas) compila en el contenedor ESP-IDF 5.5.5 para las dos placas. **Nunca ha corrido en una placa, no se ha conectado nada a un medidor ni a un contactor, y nada de aquí conmuta nada.**",
    "glance": [
      [
        "Función",
        "Nodo de campo eléctrico: medidores, entradas y maniobra (familia: Field Nodes, padre: ARMOR-COMMON)",
      ],
      [
        "Tecnología",
        "C++17, ESP-IDF 5.5.5, ESP32-S3",
      ],
      [
        "Pruebas",
        "382264 comprobaciones en 19 programas de host y 5 de Python (`ctest`)",
      ],
      [
        "Equipos",
        "Medidores PZEM-004T v3 y PZEM-017 (hasta 16), entradas analógicas, relés; maniobra apagada por defecto",
      ],
      [
        "Funciona en",
        "Una placa ESP32-S3 (Ethernet o Wi-Fi); pruebas de host en cualquier ordenador",
      ],
      [
        "En hardware real",
        "Ninguno todavía: ninguna placa montada ni medidor o contactor conectado; nada conmuta nada",
      ],
      [
        "Licencia",
        "GPL-3.0-or-later",
      ],
    ],
    "status": {
      "software": "El firmware compila en el contenedor ESP-IDF 5.5.5 para las dos placas (Wi-Fi y Ethernet).",
      "tests": "Pasan 382.264 comprobaciones en 19 programas de host (`ctest`), 375.036 de ellas sobre las reglas de maniobra; los medidores y contactores son simulaciones.",
      "protocols": "Las tramas y lecturas de los PZEM-004T v3 y PZEM-017 se comprueban contra las tramas documentadas y muestras grabadas; ningún medidor ha respondido todavía.",
      "ui": "Las páginas de medidores y lecturas del panel web se han ejercitado en un navegador contra un nodo simulado, no en una placa.",
      "hardware": "Ninguna placa construida ni medidor o contactor conectados: nada ha funcionado todavía con equipos reales.",
      "security": "El código de configuración, el acceso con límite de contraseñas erróneas, el PIN Bluetooth y las actualizaciones firmadas están probados en el host; no ha habido una revisión independiente.",
      "updates": "Las comprobaciones de hash y de firma Ed25519 y la lógica de vuelta atrás pasan en el host; una actualización por aire nunca se ha ejecutado en una placa.",
      "writing": "Las reglas para maniobrar contactores solo se han probado contra contactores simulados; nada de aquí ha maniobrado nada real.",
      "integration": "Los mensajes del nodo se validan contra los esquemas compartidos y los vectores de conformidad de ARMOR-COMMON. Su cliente MQTT se prueba contra un Mosquitto real en los tests; ninguna placa los ha enviado aún a un servidor.",
      "docs": "Ocho idiomas, la guía del firmware, las notas de cableado y el historial de cambios están al día.",
    },
    "docs": [
      "[Seguridad](docs/SAFETY.md) y [maniobra](docs/SWITCHING.md): qué supone el diseño y cómo va una transferencia",
      "[Mensajes](docs/ELECTRICAL_MESSAGES.md), [protocolos](docs/PROTOCOLS.md) y [Zigbee](docs/ZIGBEE.md)",
      "[Diseño](docs/DESIGN.md), [hardware](docs/HARDWARE.md), [placa base](docs/BASE_BOARD.md) y [firmware del nodo](docs/NODE_FIRMWARE.md)",
      "[Pruebas de banco](docs/BENCH_TESTS.md), [código de puesta en marcha](docs/SETUP_CODE.md) y [alta por Bluetooth](docs/BLE_PROVISIONING.md)",
    ],
    "contributing_first": "Antes de un pull request ejecuta `ctest --test-dir build/host` and `python -I tools/armor_ci_validate.py`: debe pasar. Consulta [CONTRIBUTING.md](CONTRIBUTING.md) y el [código de conducta](CODE_OF_CONDUCT.md).",
    "languages_extra": "",
    "body": {
      "overview": r"""* **Lectura de contadores:** las tramas Modbus RTU de los **PZEM-004T v3** (AC) y **PZEM-017** (DC) de Peacefair: el CRC, la petición que lee los registros y la decodificación de la respuesta (tensión, corriente, potencia, energía, frecuencia, factor de potencia, alarma). Solo se construye la petición de lectura: las que escriben en un contador (su dirección, sus umbrales, el reinicio de su energía) no se construyen en ningún sitio. Se rechaza una respuesta que no cuadra o que trae un valor que ningún contador real podría dar.
* **El bus:** una línea con varios contadores se pregunta de uno en uno, con un tiempo de espera; se guarda la última lectura buena de cada uno y un contador que calla deja de publicarse a los diez segundos.
* **El mensaje** `armor/electrical/<nodo>/state`: una entrada por canal (un circuito, una línea, la entrada de red, un bus DC) con AC o DC, tensión, corriente, potencia, energía, frecuencia, factor de potencia, el estado de un interruptor tal como lo ve el nodo y una alarma; está en el contrato compartido y lleva un estado, nunca una orden.
* **Las reglas para maniobrar,** aparte de cualquier hardware: un controlador del cambio entre dos fuentes que nunca manda las dos, exige la maniobra permitida, el nodo armado justo antes y los dos contactores confirmados abiertos durante todo el tiempo muerto, y convierte un contactor que no muestra lo que se le ordenó en una avería que se queda hasta que se reconoce. **La maniobra está desactivada por defecto y nada maneja ningún hardware.**
* **Las órdenes a un conmutador, sin activar:** el mensaje de estado puede llevar el estado de los conmutadores del nodo, y el contrato compartido tiene una orden (`arm`, y después `close_a` o `close_b` con un token de un solo uso, `open`, `acknowledge`) y la respuesta del nodo; el núcleo las lee y las contesta con las reglas anteriores, probado con los vectores compartidos y con contactores simulados. Ninguna imagen del firmware lo incluye, así que nada puede accionar un contactor, y ARMOR-SERVER se niega a enviar una orden si no se activó (`ARMOR_ELECTRICAL_SWITCHING=1`) y el ACL del broker no lo permite.
* **Dónde se ve:** el *Diseñador eléctrico* de ARMOR-STUDIO dibuja la red de la casa y muestra en cada elemento lo que mide su canal; ARMOR-SERVER guarda las lecturas, su historial y las sumas.
* **El firmware del nodo** (ESP32-S3-WROOM-1 N16R8 por Wi-Fi, o la Waveshare ESP32-S3-ETH por su cable): los ajustes, una línea serie para hasta dieciséis contadores y el panel web de los otros nodos (puesta en marcha, usuarios, Wi-Fi, broker, actualización por aire, HTTPS) con sus propias páginas de Contadores y Lecturas, en ocho idiomas. Solo lee: las reglas para maniobrar no están enlazadas en él. Véase [el firmware](docs/NODE_FIRMWARE.md).
* **Configuración desde el móvil por Bluetooth,** el mismo canal que el del nodo radar: la app ARMOR encuentra el nodo como `ARMOR-XXXXXX` y ajusta su nombre, Wi-Fi, dirección, broker y modo de Bluetooth con los usuarios y el código de puesta en marcha del panel ([el protocolo](docs/BLE_PROVISIONING.md)). Solo escucha mientras el nodo no tiene usuarios, salvo que se indique otra cosa. La parte de radio nunca ha corrido en una placa.
* **Actualizaciones por aire firmadas:** el nodo solo instala desde GitHub una imagen cuyo SHA-256 coincide y que lleva una firma Ed25519 válida del responsable (la clave pública está en el firmware, la privada nunca sale del responsable); un archivo subido a mano por un administrador en el panel se sigue aceptando. Las páginas y mensajes del panel están en ocho idiomas.
* **Emparejamiento Bluetooth con PIN:** el PIN de seis cifras se deriva del código de configuración, se imprime en la consola USB y se muestra a un administrador en el panel; el móvil tiene que escribirlo antes de poder cambiar los ajustes del nodo.
* **Todavía no:** el firmware funcionando en una placa, el hardware, ninguna medida de una instalación real y ninguna maniobra.
* **Solo la casa puede usar el panel:** el panel responde por defecto a la red privada (o a las redes que su dueño indique, como una VPN), rechaza una lista que dejaría fuera a quien la guarda, cuenta las contraseñas erróneas por persona y por dirección, y funciona detrás del proxy del servidor para llegar a él desde fuera de casa sin publicar el nodo.
* **Las estimaciones lo dicen:** un canal hecho con una entrada de corriente lleva `power_estimated`, así que Studio y el servidor muestran su potencia como estimada (potencia aparente a partir de una corriente y una tensión nominal) y marcan una cifra de red que incluya una.
* **Enlace cifrado opcional con el broker (TLS):** desactivado por defecto, así que el nodo habla MQTT sin cifrar como antes. Un interruptor y una caja para el certificado de la autoridad propia de la instalación (PEM, 2 KB como máximo) en la página Broker hacen que se conecte con `mqtts://`, confíe solo en esa autoridad y compruebe que el certificado del broker se hizo para la dirección a la que llegó; lo que no sea un único certificado PEM se rechaza. Cubierto con pruebas en el ordenador; el handshake aún no se ha ejecutado en una placa.
* **Informe de salud:** cada minuto más o menos el nodo publica cuánto lleva encendido y por qué se reinició la última vez, su memoria libre, su enlace y su señal Wi-Fi, cuántas veces se conectó al broker y el último error que anotó (`armor/health/<nodo>`, el contrato `node_health` de ARMOR-COMMON). El código que lo construye lo comparten todos los nodos y está probado en un ordenador; no se ha ejecutado en una placa.
* **Control desde el servidor:** Studio puede reiniciar el nodo limpiamente, pausarlo hasta una hora (se reanuda solo), poner su trabajo en espera (sin fin, se conserva al reiniciar, el nodo sigue conectado y respondiendo), hacer que se muestre, pedirle una instantánea de diagnóstico y marcarlo en mantenimiento (`armor/control/<nodo>/...`, el contrato `node_control` de ARMOR-COMMON). Cada orden son dos pasos con un token de un solo uso que pertenece a esa operación, solo el servidor puede escribirlas en el broker, y no existe restablecimiento de fábrica, borrado ni sueño profundo. Mientras el nodo está en pausa o en espera todos los relés se abren y ninguno se mueve, lo pida quien lo pida (el panel, el broker o una central); los contadores se siguen leyendo. El código es compartido por todos los nodos y se prueba en un ordenador; no ha funcionado en una placa.
* **Lecturas que dicen lo frescas que son:** cada canal de medidor lleva la edad de su lectura y cuántas peticiones al medidor han fallado, así que el servidor distingue un 0 W real de un medidor que dejó de responder; y una tarea de medidores colgada reinicia la placa mediante el watchdog.
* **Diagnóstico sin cable:** tras un arranque que no fue limpio (un cuelgue, un watchdog, una caída de la alimentación, una reserva de memoria fallida) el informe de salud dice el motivo durante diez minutos; un fallo deja su volcado de núcleo (core dump) para verlo, descargarlo o borrarlo desde el panel; los ajustes guardados se copian antes de cada instalación de firmware y se recuperan si una actualización los daña; y un administrador puede pedir al nodo, a través del servidor, un paquete de diagnóstico o su registro con un token de un solo uso.
* **Enclavamiento de relés:** un relé puede nombrar otro que nunca debe estar cerrado a la vez (las dos fuentes de una carga, los dos sentidos de un motor); se rechaza cerrar uno mientras el otro está cerrado, desde el panel, el broker y la central por igual, y el nodo nunca abre el otro por su cuenta. Probado en un ordenador; no se ha ejecutado en una placa.
* **Lectura, solo lectura, de los ajustes propios de los contadores:** tras la primera lectura buena y cada `bus.check_settings_s` (600 s, 0 = nunca) el nodo lee los registros holding del PZEM (004T v3: umbral de potencia y dirección; 017: umbrales de tensión, dirección y shunt) en el mismo turno que las medidas, y avisa si la dirección guardada no es la que usa; no se escribe nada en el contador.
* **Sellado opcional de los secretos guardados:** desactivado por defecto (`security.seal_secrets`, o `nodes.nvs_encryption` del servidor). Activado, las contraseñas, tokens, claves, PIN y hashes de contraseña que guarda el nodo quedan sellados con ChaCha20-Poly1305 y todo lo demás sigue legible; activarlo o desactivarlo los reescribe sin perder nada, aunque el nodo se pare a medias. No se quema ningún eFuse ni se cifra la flash: la clave está en una partición del mismo chip, así que **no** protege frente a quien tenga la placa, y un nodo instalado antes de esa partición conserva sus secretos como estaban hasta que se grabe con la nueva tabla de particiones.""",
      "role": r"""ARMOR-NODE-ELECTRICAL mide la red de CA y CC de la casa con sus medidores y guarda las reglas para conmutar entre fuentes. Publica las lecturas para [ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER), que guarda su historial y la energía de cada día y genera las alarmas; el menú *Eléctrico* y el *Diseñador eléctrico* de [ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) y la pantalla eléctrica de [ARMOR-ANDROID-CONTROL](https://github.com/JuanenRac/ARMOR-ANDROID-CONTROL) lo muestran. La conmutación está diseñada (armar, un token de un solo uso, el enclavamiento, la confirmación de los dos contactores) pero no activada.

| Nombre | Cómo | Para qué |
|---|---|---|
| ARMOR-SERVER | MQTT `armor/electrical/<id>/{state,command,result}` | Recibe los canales y ordena una transferencia (solo si la maniobra está activada en tres sitios) |
| ARMOR-STUDIO | menú Eléctrico, Electrical Designer | Muestra los canales y las alarmas y abre el panel del nodo |
| ARMOR-ANDROID-CONTROL | Bluetooth | Configura el nodo en el campo y muestra los canales |
| ARMOR-COMMON | contrato eléctrico | Los mensajes se comprueban con sus esquemas; el firmware común se copia de él |""",
      "architecture": r"""<p align="center">
  <img src="images/architecture.svg" alt="Arquitectura de ARMOR-NODE-ELECTRICAL: quién lo llama, qué contiene y de qué depende" width="100%">
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
| Red o continua peligrosa en la placa | El nodo solo lee los módulos PZEM (módulos cerrados, línea serie aislada) y nunca lleva red en su placa; lo que conmuta es una etapa aparte probada en banco con lámpara y transformador de aislamiento |
| Dos fuentes cerradas a la vez | El controlador de transferencia nunca ordena las dos: exige maniobra permitida, nodo armado justo antes y ambos contactores confirmados abiertos durante todo el tiempo muerto (`dead_time_ms` 2000 por defecto); un contactor que no muestra lo ordenado es un fallo que se queda hasta reconocerlo (`kDidNotOpen`, `kDidNotClose`); sigue siendo obligatorio un enclavamiento mecánico entre los contactores |
| Una orden repetida, o una maniobra que nadie pidió | `arm` da un token de un solo uso de 64 bits que `close_a` o `close_b` deben llevar, dentro de `arm_window_ms`; las órdenes nunca se retienen; máximo 4 interruptores; la maniobra está APAGADA salvo que el firmware la permita (`switching_enabled`), el servidor corra con `ARMOR_ELECTRICAL_SWITCHING=1` y la lista de acceso del broker esté abierta para ese nodo |
| Un fallo, una realimentación perdida o la maniobra apagada | Cada controlador responde con TODAS las bobinas abiertas (fallo => abierto; si abierto es seguro para la carga lo decide la instalación); el estado del mensaje es lo que muestra el contacto auxiliar, no lo ordenado; las parejas de relés están enclavadas y el nodo nunca abre la pareja por sí mismo |
| Una lectura vieja mostrada como real | Un medidor mudo deja de publicarse a los 10 s; cada canal lleva la antigüedad de su lectura y el número de peticiones fallidas; una tarea de medidores colgada reinicia la placa por watchdog; cada `bus.check_settings_s` (600 s, 0 = nunca) se leen los ajustes de los medidores (solo lectura) y se avisa si cambió una dirección |

La red (230 V CA) y la corriente continua de un banco de baterías pueden matar y provocar incendios. [docs/SAFETY.md](docs/SAFETY.md) dice lo que supone el diseño; no es el diseño de una instalación y no sustituye la normativa del país ni a un instalador cualificado. Hoy nada de esto conmuta nada.""",
      "interfaces": r"""| Parte | Qué define |
|---|---|
| MQTT | `armor/electrical/<id>/state` (un canal por entrada: CA o CC, tensión, corriente, potencia, energía, frecuencia, factor de potencia, estado del interruptor, alarma; contrato de ARMOR-COMMON), `armor/electrical/<id>/command` y `/result`, `armor/device/<id>/<relé>/{state,set}`, `armor/health/<id>`, `armor/control/<id>/...` |
| Órdenes | `arm`, `close_a`, `close_b` (con el token), `open` y `acknowledge` (borra un fallo) |
| Medidores | Peacefair PZEM-004T v3 (CA) y PZEM-017 (CC) por Modbus RTU, hasta 16 en una línea serie; solo se construye la petición de lectura (la que escribe dirección o umbrales no existe); entradas analógicas, contactos y relés en la placa base; un puente Zigbee ([docs/ZIGBEE.md](docs/ZIGBEE.md)) |""",
      "configuration": r"""| Variable | Por defecto | Qué define |
|---|---|---|
| `bus.check_settings_s` | 600 | Segundos entre las comprobaciones de solo lectura de los ajustes de los medidores (0 = nunca) |
| `dead_time_ms`, `confirm_timeout_ms` | 2000 | El tiempo muerto de una transferencia y cuánto tiene un contactor para mostrar lo ordenado |
| `switching_enabled` | off | La maniobra está APAGADA salvo que este ajuste, el servidor (`ARMOR_ELECTRICAL_SWITCHING=1`) y la lista de acceso del broker la permitan |
| `CONFIG_ARMOR_NODE_ID`, `_SETUP_CODE`, `_FLEET_SECRET`, `_MQTT_*`, `_HEARTBEAT_S`, `_BLE_SETUP_MINUTES`, `_BOOT_FACTORY_RESET` | - | Los ajustes que comparten todos los nodos: el nombre (vacío da `armor-` y los últimos bytes de la MAC), el código de puesta en marcha (vacío: aleatorio), el secreto de flota (16+ caracteres, nunca en el repositorio), los primeros ajustes del broker, el latido (de 2 a 300 s), los minutos de puesta en marcha por Bluetooth (de 1 a 120) y el reinicio con BOOT (8 s en los primeros 30 s) |""",
      "quickstart": r"""**Requisitos:** un compilador C++17 para las pruebas de host; el contenedor ESP-IDF 5.5.5 para compilar la imagen; una placa ESP32-S3 (Ethernet o Wi-Fi).

```bash
cmake -S tests -B build/host && cmake --build build/host && ctest --test-dir build/host   # host tests, -Werror
node tools/panel_mock.mjs --user admin:adminpass123   # the panel without a board
tools/build_node.sh generic s3-wifi                  # the image in the ESP-IDF container (or s3-eth)
```

See the [firmware guide](docs/NODE_FIRMWARE.md) and the [Bluetooth channel](docs/BLE_PROVISIONING.md).

Véanse el [diseño](docs/DESIGN.md), las [notas de seguridad](docs/SAFETY.md), las [reglas para maniobrar](docs/SWITCHING.md), los [protocolos](docs/PROTOCOLS.md) y los [mensajes](docs/ELECTRICAL_MESSAGES.md).""",
      "testing": r"""```bash
cmake -S tests -B build/host && cmake --build build/host && ctest --test-dir build/host
python -I tools/armor_ci_validate.py
```

19 programas de prueba de host y 5 comprobaciones en Python se ejecutan con `ctest`; 382264 comprobaciones contadas por los programas de host, compilados con `-Werror`.

Comprobaciones Python: los textos del panel en ocho idiomas, las tareas, las rutas de guardado, la sesión Bluetooth bajo su bloqueo y las rutas que llama el panel (y, en algunos nodos, los códigos HTTP o los glifos de las fuentes)

Las pruebas de host necesitan cualquier compilador C++17 (Linux, WSL, MSYS2); el panel web también se ejercita en un navegador real contra un nodo de pruebas (`tools/panel_mock.mjs`, `tools/panel_browser_test.mjs`).

La mayoría de las comprobaciones son barridos exhaustivos de las reglas de maniobra (`test_switch_set` y `test_interlock`: 375 036); los medidores y contactores son sustitutos. `test_clock` solo imprime `ok`.""",
      "build": "`tools/build_node.sh` compila la imagen en el contenedor ESP-IDF 5.5.5 y la versión lleva la imagen, su SHA-256 y su firma Ed25519, una por placa; la imagen se graba por USB-C la primera vez y después se actualiza desde el panel.",
      "troubleshooting": r"""| Ves | Porque | Haz |
|---|---|---|
| Perdiste la contraseña o el nodo ya no se une a la red | Un nodo con puesta en marcha y sin dirección tras 90 s abre su propio Wi-Fi `ARMOR-SETUP-xxxxxx` (abre `http://192.168.4.1/`) | Para empezar de cero mantén BOOT 8 segundos en los primeros 30 segundos tras encender (borra ajustes y usuarios), o usa *Restablecer de fábrica* en el panel |
| Se rechaza una actualización desde GitHub | La versión no trae suma de comprobación ni firma, no coinciden (`e_no_checksum`, `e_no_signature`, `e_checksum_mismatch`, `e_bad_signature`), no trae imagen para esta placa (`e_no_asset_for_board`) o es de otro proyecto (`e_wrong_firmware`) | El nodo no cambió; reintenta o deja que un administrador suba el fichero a mano |
| Un conmutador muestra un fallo | El contactor no mostró abierto o cerrado como se ordenó (`kDidNotOpen`, `kDidNotClose`); se queda hasta reconocerlo | Revisa el cableado del contacto auxiliar y envía `acknowledge` |
| Se rechaza una orden | La maniobra está apagada (`switching_enabled` falso), el token no es válido o caducó, o el nodo no estaba armado justo antes | Arma otra vez y manda la orden con el token nuevo |""",
      "structure": r"""<p align="center">
  <img src="images/repository-structure.svg" alt="Estructura del repositorio de ARMOR-NODE-ELECTRICAL" width="100%">
</p>

<details>
<summary>Versión en texto del árbol</summary>

```text
ARMOR-NODE-ELECTRICAL/
├── main/                                el firmware: un componente de ESP-IDF
├── core/                                la lógica sin ESP-IDF, probada en un ordenador
├── panel/                               el panel web embebido en el firmware
├── tests/                               pruebas de host y comprobaciones Python
├── docs/                                12 guías: seguridad, maniobra, mensajes, hardware
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

* Las tramas y lecturas de los PZEM-004T v3 y PZEM-017 se comprueban contra las tramas documentadas y muestras grabadas; ningún medidor ha respondido todavía.
* Las páginas de medidores y lecturas del panel web se han ejercitado en un navegador contra un nodo simulado, no en una placa.
* Ninguna placa construida ni medidor o contactor conectados: nada ha funcionado todavía con equipos reales.
* El código de configuración, el acceso con límite de contraseñas erróneas, el PIN Bluetooth y las actualizaciones firmadas están probados en el host; no ha habido una revisión independiente.
* Las comprobaciones de hash y de firma Ed25519 y la lógica de vuelta atrás pasan en el host; una actualización por aire nunca se ha ejecutado en una placa.
* Las reglas para maniobrar contactores solo se han probado contra contactores simulados; nada de aquí ha maniobrado nada real.

**Lo siguiente**

* Probar los medidores, los contactores y las reglas de maniobra en un banco con lámpara y transformador de aislamiento, y después una placa real con la actualización por aire.""",
    },
  },
  "de": {
    "tagline": "Elektroknoten: liest Spannungen, Ströme, Leistung und Energie des AC- und DC-Netzes des Hauses und hält die Regeln fürs Schalten (am Rechner getesteter Kern und eine Firmware, die baut; sie lief noch nie auf einer Platine)",
    "honest": "Der Kern (die Rahmen der Zähler PZEM-004T v3 und PZEM-017, der Bus, der sie abfragt, die Nachricht des Knotens, die analogen Eingänge und die Schaltregeln: 382.264 Prüfungen in 19 Testprogrammen, davon 375.036 zu den Schaltregeln) wird auf einem Computer mit Ersatzzählern und -schützen getestet, und die von ihm erzeugten Nachrichten akzeptiert ARMOR-COMMON. Die Firmware des Knotens (die Einstellungen, die serielle Leitung, die Seiten Zähler und Messwerte seines Panels, Bluetooth, signierte Updates) baut im ESP-IDF-5.5.5-Container für beide Platinen. **Sie lief nie auf einer Platine, an keinen Zähler und kein Schütz wurde etwas angeschlossen, und nichts hier schaltet irgendetwas.**",
    "glance": [
      [
        "Rolle",
        "Elektro-Feldknoten: Zähler, Eingänge und Schalten (Familie: Field Nodes, übergeordnet: ARMOR-COMMON)",
      ],
      [
        "Technik",
        "C++17, ESP-IDF 5.5.5, ESP32-S3",
      ],
      [
        "Tests",
        "382264 Prüfungen in 19 Host-Programmen und 5 Python-Prüfungen (`ctest`)",
      ],
      [
        "Geräte",
        "Zähler PZEM-004T v3 und PZEM-017 (bis zu 16), analoge Eingänge, Relais; Schalten standardmäßig aus",
      ],
      [
        "Läuft auf",
        "Eine ESP32-S3-Platine (Ethernet oder WLAN); Host-Tests auf jedem Computer",
      ],
      [
        "Auf echter Hardware",
        "Noch keiner: keine Platine aufgebaut und kein Zähler oder Schütz angeschlossen; nichts schaltet irgendetwas",
      ],
      [
        "Lizenz",
        "GPL-3.0-or-later",
      ],
    ],
    "status": {
      "software": "Die Firmware wird im ESP-IDF-5.5.5-Container für beide Platinen (WLAN und Ethernet) gebaut.",
      "tests": "382.264 Prüfungen in 19 Host-Programmen bestehen (`ctest`), davon 375.036 zu den Schaltregeln; die Zähler und Schütze sind Nachbildungen.",
      "protocols": "Die Telegramme und Messwerte der PZEM-004T v3 und PZEM-017 werden gegen die dokumentierten Telegramme und aufgezeichnete Beispiele geprüft; noch hat kein Zähler geantwortet.",
      "ui": "Die Seiten für Zähler und Messwerte des Web-Panels wurden in einem Browser gegen einen nachgebildeten Knoten erprobt, nicht auf einer Platine.",
      "hardware": "Keine Platine gebaut und kein Zähler oder Schütz angeschlossen: Bisher lief nichts auf echten Geräten.",
      "security": "Der Einrichtungscode, die Anmeldung mit Begrenzung falscher Passwörter, die Bluetooth-PIN und die signierten Aktualisierungen sind auf dem Host getestet; es gab keine unabhängige Prüfung.",
      "updates": "Die Hash- und Ed25519-Signaturprüfungen und die Rückfalllogik bestehen auf dem Host; eine Aktualisierung über die Luft wurde nie auf einer Platine ausgeführt.",
      "writing": "Die Schaltregeln für Schütze sind nur gegen nachgebildete Schütze getestet; nichts hier hat bisher etwas Echtes geschaltet.",
      "integration": "Die Nachrichten des Knotens werden gegen die gemeinsamen Schemas und Konformitätsvektoren von ARMOR-COMMON geprüft. Sein MQTT-Client wird in den Tests gegen einen echten Mosquitto gespielt; noch keine Platine hat sie an einen Server geschickt.",
      "docs": "Acht Sprachen, die Firmware-Anleitung, die Verdrahtungshinweise und das Änderungsprotokoll sind aktuell.",
    },
    "docs": [
      "[Sicherheit](docs/SAFETY.md) und [Schalten](docs/SWITCHING.md): was der Entwurf voraussetzt und wie eine Umschaltung abläuft",
      "[Nachrichten](docs/ELECTRICAL_MESSAGES.md), [Protokolle](docs/PROTOCOLS.md) und [Zigbee](docs/ZIGBEE.md)",
      "[Entwurf](docs/DESIGN.md), [Hardware](docs/HARDWARE.md), [Basisplatine](docs/BASE_BOARD.md) und [Knoten-Firmware](docs/NODE_FIRMWARE.md)",
      "[Prüfstandtests](docs/BENCH_TESTS.md), [Einrichtungscode](docs/SETUP_CODE.md) und [Bluetooth-Einrichtung](docs/BLE_PROVISIONING.md)",
    ],
    "contributing_first": "Führe vor einem Pull Request `ctest --test-dir build/host` and `python -I tools/armor_ci_validate.py` aus: Es muss bestehen. Siehe [CONTRIBUTING.md](CONTRIBUTING.md) und den [Verhaltenskodex](CODE_OF_CONDUCT.md).",
    "languages_extra": "",
    "body": {
      "overview": r"""* **Zähler lesen:** die Modbus-RTU-Rahmen der Peacefair-Zähler **PZEM-004T v3** (AC) und **PZEM-017** (DC): die CRC, die Anfrage, die die Register liest, und die Auswertung der Antwort (Spannung, Strom, Leistung, Energie, Frequenz, Leistungsfaktor, Alarm). Nur die Leseanfrage wird gebaut: die schreibenden (Adresse, Schwellen, Zurücksetzen der Energie) werden nirgends gebaut. Eine Antwort, die nicht passt oder einen Wert enthält, den kein echter Zähler liefern könnte, wird abgelehnt.
* **Der Bus:** eine Leitung mit mehreren Zählern wird einzeln abgefragt, mit Zeitlimit; der letzte gute Wert jedes Zählers wird behalten, und ein Zähler, der schweigt, wird nach zehn Sekunden nicht mehr veröffentlicht.
* **Die Nachricht** `armor/electrical/<Knoten>/state`: ein Eintrag je Kanal (ein Stromkreis, eine Leitung, der Netzanschluss, ein DC-Bus) mit AC oder DC, Spannung, Strom, Leistung, Energie, Frequenz, Leistungsfaktor, dem Zustand eines Schalters, wie ihn der Knoten sieht, und einem Alarm; sie steht im gemeinsamen Vertrag und trägt einen Zustand, nie einen Befehl.
* **Die Regeln fürs Schalten,** unabhängig von jeder Hardware: ein Regler für den Wechsel zwischen zwei Quellen, der nie beide ansteuert, das erlaubte Schalten, den kurz zuvor scharfgeschalteten Knoten und beide Schütze über die ganze Totzeit als offen bestätigt verlangt und ein Schütz, das nicht zeigt, was ihm befohlen wurde, zu einer Störung macht, die bis zur Quittierung bleibt. **Schalten ist standardmäßig aus, und nichts steuert irgendeine Hardware.**
* **Die Befehle an einen Schalter, nicht aktiviert:** Die Zustandsnachricht kann den Zustand der Schalter des Knotens tragen, und der gemeinsame Vertrag kennt einen Befehl (`arm`, dann `close_a` oder `close_b` mit einem Einmal-Token, `open`, `acknowledge`) und die Antwort des Knotens; der Kern liest und beantwortet sie mit den obigen Regeln, geprüft mit den gemeinsamen Vektoren und mit simulierten Schützen. Kein Firmware-Abbild enthält es, also kann nichts ein Schütz ansteuern, und ARMOR-SERVER sendet keinen Befehl, solange er nicht eingeschaltet wurde (`ARMOR_ELECTRICAL_SWITCHING=1`) und die ACL des Brokers ihn nicht erlaubt.
* **Wo man es sieht:** der *Elektroplaner* von ARMOR-STUDIO zeichnet das Netz des Hauses und zeigt an jedem Element, was sein Kanal misst; ARMOR-SERVER speichert die Messwerte, ihren Verlauf und die Summen.
* **Die Firmware des Knotens** (ESP32-S3-WROOM-1 N16R8 über WLAN oder das Waveshare ESP32-S3-ETH am Kabel): die Einstellungen, eine serielle Leitung für bis zu sechzehn Zähler und das Web-Panel der anderen Knoten (Einrichtung, Benutzer, WLAN, Broker, Update über die Luft, HTTPS) mit eigenen Seiten für Zähler und Messwerte, in acht Sprachen. Sie liest nur: die Regeln fürs Schalten sind nicht eingebunden. Siehe [die Firmware](docs/NODE_FIRMWARE.md).
* **Konfiguration vom Handy über Bluetooth,** derselbe Kanal wie beim Radarknoten: Die ARMOR-App findet den Knoten als `ARMOR-XXXXXX` und stellt Name, WLAN, Adresse, Broker und Bluetooth-Modus mit den Benutzern und dem Einrichtungscode des Panels ein ([das Protokoll](docs/BLE_PROVISIONING.md)). Er lauscht nur, solange der Knoten keinen Benutzer hat, sofern nichts anderes eingestellt ist. Der Funkteil lief noch nie auf einer Platine.
* **Signierte Over-the-Air-Updates:** der Knoten installiert von GitHub nur ein Abbild, dessen SHA-256 stimmt und das eine gültige Ed25519-Signatur des Betreuers trägt (der öffentliche Schlüssel steckt in der Firmware, der private verlässt den Betreuer nie); eine von einem Administrator im Panel von Hand hochgeladene Datei wird weiterhin akzeptiert. Seiten und Meldungen des Panels sind in acht Sprachen.
* **Bluetooth-Kopplung mit PIN:** die sechsstellige PIN wird aus dem Einrichtungscode abgeleitet, auf der USB-Konsole ausgegeben und einem Administrator im Panel angezeigt; das Telefon muss sie eingeben, bevor es die Einstellungen des Knotens schreiben darf.
* **Noch nicht:** die Firmware auf einer Platine, die Hardware, jede Messung einer echten Anlage und jedes Schalten.
* **Nur das Haus darf das Panel nutzen:** Das Panel antwortet standardmäßig dem privaten Netz (oder den Netzen, die der Besitzer nennt, etwa einem VPN), lehnt eine Liste ab, die den Speichernden aussperren würde, zählt falsche Passwörter je Person und je Adresse und funktioniert hinter dem Proxy des Servers, sodass man es von außerhalb des Hauses erreicht, ohne den Knoten zu veröffentlichen.
* **Schätzungen sagen es:** ein aus einem Stromeingang gebildeter Kanal trägt `power_estimated`; Studio und Server zeigen seine Leistung als Schätzung (Scheinleistung aus Strom und Nennspannung) und kennzeichnen einen Netzwert, der eine enthält.
* **Optionale verschlüsselte Verbindung zum Broker (TLS):** standardmäßig aus, der Knoten spricht also wie bisher unverschlüsseltes MQTT. Ein Schalter und ein Feld für das Zertifikat der eigenen Zertifizierungsstelle der Anlage (PEM, höchstens 2 KB) auf der Broker-Seite sorgen dafür, dass er sich mit `mqtts://` verbindet, nur dieser Stelle vertraut und prüft, ob das Zertifikat des Brokers für die erreichte Adresse ausgestellt wurde; alles, was nicht genau ein PEM-Zertifikat ist, wird abgelehnt. Durch Host-Tests abgedeckt; der Handshake wurde auf einer Platine noch nicht ausgeführt.
* **Zustandsbericht:** etwa einmal pro Minute veröffentlicht der Knoten, wie lange er läuft und warum er zuletzt neu gestartet ist, seinen freien Speicher, seine Verbindung und sein WLAN-Signal, wie oft er sich mit dem Broker verbunden hat und den letzten protokollierten Fehler (`armor/health/<Knoten>`, der Vertrag `node_health` von ARMOR-COMMON). Der Code, der ihn erzeugt, wird von allen Knoten geteilt und auf einem Computer getestet; auf einer Platine ist er noch nicht gelaufen.
* **Steuerung vom Server aus:** Studio kann den Knoten sauber neu starten, bis zu einer Stunde pausieren (er läuft von selbst weiter), seine Arbeit in den Standby setzen (ohne Ende, über Neustarts hinweg gespeichert, der Knoten bleibt verbunden und antwortet weiter), ihn sich zeigen lassen, einen Diagnose-Schnappschuss anfordern und ihn als in Wartung markieren (`armor/control/<Knoten>/...`, der Vertrag `node_control` von ARMOR-COMMON). Jeder Befehl besteht aus zwei Schritten mit einem Einmal-Token, das zu dieser Operation gehört; nur der Server darf sie am Broker schreiben, und es gibt kein Zurücksetzen auf Werkseinstellungen, kein Löschen und keinen Tiefschlaf. Solange der Knoten pausiert oder im Standby ist, sind alle Relais offen und keines bewegt sich, wer auch fragt (Panel, Broker oder eine Zentrale); die Zähler werden weiter gelesen. Der Code wird von allen Knoten geteilt und auf einem Rechner getestet; auf einer Platine ist er noch nicht gelaufen.
* **Messwerte, die ihre Frische angeben:** Jeder Zählerkanal trägt das Alter seiner Messung und die Zahl der fehlgeschlagenen Anfragen an den Zähler, sodass der Server ein echtes 0 W von einem Zähler unterscheidet, der nicht mehr antwortet; und eine hängende Zähler-Task startet die Platine über den Watchdog neu.
* **Diagnose ohne Kabel:** Nach einem unsauberen Start (Absturz, Watchdog, Spannungseinbruch, fehlgeschlagene Speicherreservierung) nennt der Gesundheitsbericht zehn Minuten lang den Grund; ein Absturz hinterlässt sein Core-Dump, das man im Panel ansehen, herunterladen oder löschen kann; die gespeicherten Einstellungen werden vor jeder Firmware-Installation kopiert und wiederhergestellt, falls ein Update sie beschädigt; und ein Administrator kann den Knoten über den Server mit einem Einmal-Token nach einem Diagnosepaket oder seinem Protokoll fragen.
* **Relais-Verriegelung:** Ein Relais kann ein anderes benennen, das nie gleichzeitig geschlossen sein darf (die zwei Quellen einer Last, die zwei Richtungen eines Motors); das Schließen des einen wird abgelehnt, solange das andere geschlossen ist, vom Panel, vom Broker und von der Zentrale gleichermaßen, und der Knoten öffnet das andere nie von selbst. Auf einem Computer getestet; nicht auf einem Board ausgeführt.
* **Nur lesender Zugriff auf die eigenen Einstellungen der Zähler:** Nach der ersten guten Messung und alle `bus.check_settings_s` (600 s, 0 = nie) liest der Knoten die Holding-Register des PZEM (004T v3: Leistungsschwelle und Adresse; 017: Spannungsschwellen, Adresse und Shunt) im selben Durchgang wie die Messwerte und warnt, wenn die gespeicherte Adresse nicht die verwendete ist; in den Zähler wird nichts geschrieben.
* **Optionales Versiegeln gespeicherter Geheimnisse:** standardmäßig aus (`security.seal_secrets` oder `nodes.nvs_encryption` des Servers). Eingeschaltet werden die Passwörter, Token, Schlüssel, PINs und Passwort-Hashes, die der Knoten speichert, mit ChaCha20-Poly1305 versiegelt, alles andere bleibt lesbar; Ein- und Ausschalten schreibt sie ohne Verlust um, auch wenn der Knoten mittendrin stehen bleibt. Es wird kein eFuse gebrannt und der Flash nicht verschlüsselt: Der Schlüssel liegt in einer Partition desselben Chips und schützt daher **nicht** vor jemandem, der die Platine hat; ein Knoten, der vor dieser Partition installiert wurde, behält seine Geheimnisse unverändert, bis er mit der neuen Partitionstabelle geflasht wird.""",
      "role": r"""ARMOR-NODE-ELECTRICAL misst das AC- und DC-Netz des Hauses mit seinen Zählern und hält die Regeln zum Umschalten zwischen Quellen. Es veröffentlicht die Messwerte für [ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER), der Verlauf und Tagesenergie führt und die Alarme auslöst; das Menü *Elektro* und der *Elektro-Designer* von [ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) sowie der Elektro-Bildschirm von [ARMOR-ANDROID-CONTROL](https://github.com/JuanenRac/ARMOR-ANDROID-CONTROL) zeigen es. Das Schalten ist entworfen (Scharfstellen, ein Einmal-Token, die Verriegelung, die Bestätigung beider Schütze), aber nicht aktiviert.

| Name | Wie | Wozu |
|---|---|---|
| ARMOR-SERVER | MQTT `armor/electrical/<id>/{state,command,result}` | Empfängt die Kanäle und ordnet eine Umschaltung an (nur wenn das Schalten an drei Stellen aktiviert ist) |
| ARMOR-STUDIO | Menü Elektrik, Electrical Designer | Zeigt die Kanäle und Alarme und öffnet das Panel des Knotens |
| ARMOR-ANDROID-CONTROL | Bluetooth | Richtet den Knoten vor Ort ein und zeigt die Kanäle |
| ARMOR-COMMON | Elektro-Vertrag | Die Nachrichten werden gegen seine Schemas geprüft; die gemeinsame Firmware stammt daraus |""",
      "architecture": r"""<p align="center">
  <img src="images/architecture.svg" alt="Architektur von ARMOR-NODE-ELECTRICAL: wer es aufruft, was es enthält und wovon es abhängt" width="100%">
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
| Gefährliche Netz- oder Gleichspannung auf der Platine | Der Knoten liest nur die PZEM-Module (geschlossene Module, isolierte serielle Leitung) und führt nie Netzspannung auf seiner Platine; was schaltet, ist eine getrennte Stufe, am Prüfstand mit Lampe und Trenntransformator getestet |
| Zwei Quellen gleichzeitig geschlossen | Die Umschaltverriegelung befiehlt nie beide: Sie braucht erlaubtes Schalten, den kurz zuvor scharf gemachten Knoten und beide Schütze als offen bestätigt während der ganzen Totzeit (`dead_time_ms` standardmäßig 2000); ein Schütz, das nicht zeigt, was befohlen wurde, ist ein Fehler, der bis zur Quittierung bleibt (`kDidNotOpen`, `kDidNotClose`); eine mechanische Verriegelung zwischen den Schützen ist weiterhin Pflicht |
| Ein wiederholter Befehl oder ein Schalten, das niemand wollte | `arm` liefert ein 64-Bit-Einmal-Token, das `close_a` oder `close_b` innerhalb von `arm_window_ms` tragen müssen; Befehle werden nie zurückgehalten; höchstens 4 Schalter; Schalten ist AUS, außer die Firmware erlaubt es (`switching_enabled`), der Server läuft mit `ARMOR_ELECTRICAL_SWITCHING=1` und die Zugriffsliste des Brokers ist für diesen Knoten offen |
| Ein Fehler, verlorene Rückmeldung oder ausgeschaltetes Schalten | Jeder Regler antwortet mit ALLEN Spulen offen (Fehler => offen; ob offen für die Last sicher ist, entscheidet die Installation); der Zustand in der Nachricht ist das, was der Hilfskontakt zeigt, nicht das Befohlene; Relaispaare sind verriegelt, und der Knoten öffnet den Partner nie von sich aus |
| Ein alter Messwert als echt angezeigt | Ein stummer Zähler wird nach 10 s nicht mehr veröffentlicht; jeder Kanal trägt das Alter seines Messwerts und die Zahl fehlgeschlagener Anfragen; eine hängende Zähler-Task startet die Platine per Watchdog neu; alle `bus.check_settings_s` (600 s, 0 = nie) werden die Einstellungen der Zähler gelesen (nur lesend) und eine geänderte Adresse gemeldet |

Netzspannung (230 V AC) und die Gleichspannung einer Batteriebank können töten und Brände auslösen. [docs/SAFETY.md](docs/SAFETY.md) sagt, was der Entwurf voraussetzt; es ist kein Entwurf einer Installation und ersetzt weder die Vorschriften des Landes noch einen qualifizierten Installateur. Heute schaltet nichts hiervon irgendetwas.""",
      "interfaces": r"""| Teil | Was sie festlegt |
|---|---|
| MQTT | `armor/electrical/<id>/state` (ein Kanal je Eingang: AC oder DC, Spannung, Strom, Leistung, Energie, Frequenz, Leistungsfaktor, Schalterzustand, Alarm; ARMOR-COMMON-Vertrag), `armor/electrical/<id>/command` und `/result`, `armor/device/<id>/<Relais>/{state,set}`, `armor/health/<id>`, `armor/control/<id>/...` |
| Befehle | `arm`, `close_a`, `close_b` (mit dem Token), `open` und `acknowledge` (löscht einen Fehler) |
| Zähler | Peacefair PZEM-004T v3 (AC) und PZEM-017 (DC) per Modbus RTU, bis zu 16 an einer seriellen Leitung; nur die Leseanfrage wird gebaut (die zum Schreiben von Adresse oder Schwellen gibt es nicht); analoge Eingänge, Kontakte und Relais auf der Basisplatine; eine Zigbee-Brücke ([docs/ZIGBEE.md](docs/ZIGBEE.md)) |""",
      "configuration": r"""| Variable | Standard | Was sie festlegt |
|---|---|---|
| `bus.check_settings_s` | 600 | Sekunden zwischen den rein lesenden Prüfungen der Zählereinstellungen (0 = nie) |
| `dead_time_ms`, `confirm_timeout_ms` | 2000 | Die Totzeit einer Umschaltung und wie lange ein Schütz Zeit hat, das Befohlene zu zeigen |
| `switching_enabled` | off | Schalten ist AUS, außer diese Einstellung, der Server (`ARMOR_ELECTRICAL_SWITCHING=1`) und die Zugriffsliste des Brokers erlauben es |
| `CONFIG_ARMOR_NODE_ID`, `_SETUP_CODE`, `_FLEET_SECRET`, `_MQTT_*`, `_HEARTBEAT_S`, `_BLE_SETUP_MINUTES`, `_BOOT_FACTORY_RESET` | - | Die Einstellungen, die alle Knoten teilen: der Name (leer ergibt `armor-` und die letzten Bytes der MAC), der Einrichtungscode (leer: zufällig), das Flottengeheimnis (16+ Zeichen, nie im Repository), die ersten Broker-Einstellungen, der Herzschlag (2 bis 300 s), die Minuten der Bluetooth-Einrichtung (1 bis 120) und der Reset mit BOOT (8 s in den ersten 30 s) |""",
      "quickstart": r"""**Voraussetzungen:** ein C++17-Compiler für die Host-Tests; der ESP-IDF-5.5.5-Container zum Bauen des Images; eine ESP32-S3-Platine (Ethernet oder WLAN).

```bash
cmake -S tests -B build/host && cmake --build build/host && ctest --test-dir build/host   # host tests, -Werror
node tools/panel_mock.mjs --user admin:adminpass123   # the panel without a board
tools/build_node.sh generic s3-wifi                  # the image in the ESP-IDF container (or s3-eth)
```

See the [firmware guide](docs/NODE_FIRMWARE.md) and the [Bluetooth channel](docs/BLE_PROVISIONING.md).

Siehe den [Entwurf](docs/DESIGN.md), die [Sicherheitshinweise](docs/SAFETY.md), die [Regeln fürs Schalten](docs/SWITCHING.md), die [Protokolle](docs/PROTOCOLS.md) und die [Nachrichten](docs/ELECTRICAL_MESSAGES.md).""",
      "testing": r"""```bash
cmake -S tests -B build/host && cmake --build build/host && ctest --test-dir build/host
python -I tools/armor_ci_validate.py
```

19 Host-Testprogramme und 5 Python-Prüfungen laufen unter `ctest`; 382264 Prüfungen, gezählt von den Host-Programmen, mit `-Werror` gebaut.

Python-Prüfungen: die Panel-Texte in acht Sprachen, die Tasks, die Speicherpfade, die Bluetooth-Sitzung unter ihrer Sperre und die vom Panel aufgerufenen Routen (und in manchen Knoten die HTTP-Codes oder die Glyphen der Schriften)

Die Host-Tests brauchen einen beliebigen C++17-Compiler (Linux, WSL, MSYS2); das Web-Panel wird außerdem in einem echten Browser gegen einen Ersatzknoten geprüft (`tools/panel_mock.mjs`, `tools/panel_browser_test.mjs`).

Die meisten Prüfungen sind erschöpfende Durchläufe der Schaltregeln (`test_switch_set` und `test_interlock`: 375 036); Zähler und Schütze sind Ersatz. `test_clock` gibt nur `ok` aus.""",
      "build": "`tools/build_node.sh` baut das Image im ESP-IDF-5.5.5-Container, und die Version trägt das Image, sein SHA-256 und seine Ed25519-Signatur, je eines pro Platine; das Image wird beim ersten Mal per USB-C geschrieben und danach vom Panel aktualisiert.",
      "troubleshooting": r"""| Sie sehen | Weil | Tun Sie |
|---|---|---|
| Du hast das Passwort verloren oder der Knoten tritt dem Netz nicht mehr bei | Ein Knoten in der Einrichtung ohne Adresse nach 90 s öffnet ein eigenes WLAN `ARMOR-SETUP-xxxxxx` (öffne `http://192.168.4.1/`) | Zum Neustart BOOT 8 Sekunden in den ersten 30 Sekunden nach dem Einschalten halten (löscht Einstellungen und Benutzer) oder im Panel *Werksreset* nutzen |
| Ein Update von GitHub wird abgelehnt | Die Version enthält keine Prüfsumme oder Signatur, sie passen nicht (`e_no_checksum`, `e_no_signature`, `e_checksum_mismatch`, `e_bad_signature`), hat kein Image für diese Platine (`e_no_asset_for_board`) oder gehört zu einem anderen Projekt (`e_wrong_firmware`) | Der Knoten blieb unverändert; erneut versuchen oder einen Administrator die Datei von Hand hochladen lassen |
| Ein Schalter zeigt einen Fehler | Das Schütz zeigte nicht offen oder geschlossen wie befohlen (`kDidNotOpen`, `kDidNotClose`); es bleibt bis zur Quittierung | Prüfe die Verdrahtung des Hilfskontakts, dann sende `acknowledge` |
| Ein Befehl wird abgelehnt | Schalten ist aus (`switching_enabled` falsch), das Token ist ungültig oder abgelaufen, oder der Knoten war nicht kurz zuvor scharf gemacht | Erneut scharf machen und den Befehl mit dem neuen Token senden |""",
      "structure": r"""<p align="center">
  <img src="images/repository-structure.svg" alt="Repository-Struktur von ARMOR-NODE-ELECTRICAL" width="100%">
</p>

<details>
<summary>Textversion des Baums</summary>

```text
ARMOR-NODE-ELECTRICAL/
├── main/                                die Firmware: eine ESP-IDF-Komponente
├── core/                                die Logik ohne ESP-IDF, am Rechner getestet
├── panel/                               das in die Firmware eingebettete Web-Panel
├── tests/                               Host-Tests und Python-Prüfungen
├── docs/                                12 Anleitungen: Sicherheit, Schalten, Nachrichten, Hardware
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

* Die Telegramme und Messwerte der PZEM-004T v3 und PZEM-017 werden gegen die dokumentierten Telegramme und aufgezeichnete Beispiele geprüft; noch hat kein Zähler geantwortet.
* Die Seiten für Zähler und Messwerte des Web-Panels wurden in einem Browser gegen einen nachgebildeten Knoten erprobt, nicht auf einer Platine.
* Keine Platine gebaut und kein Zähler oder Schütz angeschlossen: Bisher lief nichts auf echten Geräten.
* Der Einrichtungscode, die Anmeldung mit Begrenzung falscher Passwörter, die Bluetooth-PIN und die signierten Aktualisierungen sind auf dem Host getestet; es gab keine unabhängige Prüfung.
* Die Hash- und Ed25519-Signaturprüfungen und die Rückfalllogik bestehen auf dem Host; eine Aktualisierung über die Luft wurde nie auf einer Platine ausgeführt.
* Die Schaltregeln für Schütze sind nur gegen nachgebildete Schütze getestet; nichts hier hat bisher etwas Echtes geschaltet.

**Als Nächstes**

* Die Zähler, die Schütze und die Schaltregeln am Prüfstand mit Lampe und Trenntransformator erproben, danach eine echte Platine mit dem Update über die Luft.""",
    },
  },
  "fr": {
    "tagline": "Nœud électrique : lit les tensions, courants, puissance et énergie du réseau AC et DC de la maison et détient les règles pour le commander (cœur testé sur ordinateur et un firmware qui compile ; il n'a jamais tourné sur une carte)",
    "honest": "Le cœur (les trames des compteurs PZEM-004T v3 et PZEM-017, le bus qui les interroge, le message du nœud, les entrées analogiques et les règles de commutation : 376 195 vérifications dans 11 programmes de test, dont 375 008 sur les règles de commutation) est testé sur un ordinateur avec des compteurs et contacteurs factices, et les messages qu'il produit sont acceptés par ARMOR-COMMON. Le firmware du nœud (les réglages, la ligne série, les pages Compteurs et Mesures de son panneau, Bluetooth, mises à jour signées) se compile dans le conteneur ESP-IDF 5.5.5 pour les deux cartes. **Il n'a jamais tourné sur une carte, rien n'a été connecté à un compteur ni à un contacteur, et rien ici ne commute quoi que ce soit.**",
    "glance": [
      [
        "Rôle",
        "Nœud de terrain électrique : compteurs, entrées et manœuvre (famille : Field Nodes, parent : ARMOR-COMMON)",
      ],
      [
        "Technologie",
        "C++17, ESP-IDF 5.5.5, ESP32-S3",
      ],
      [
        "Tests",
        "382264 vérifications dans 19 programmes hôte et 5 contrôles Python (`ctest`)",
      ],
      [
        "Équipements",
        "Compteurs PZEM-004T v3 et PZEM-017 (jusqu'à 16), entrées analogiques, relais ; manœuvre désactivée par défaut",
      ],
      [
        "Fonctionne sur",
        "Une carte ESP32-S3 (Ethernet ou Wi-Fi) ; tests sur hôte sur n'importe quel ordinateur",
      ],
      [
        "Sur matériel réel",
        "Aucun pour l'instant : aucune carte montée ni compteur ou contacteur connecté ; rien ne commute quoi que ce soit",
      ],
      [
        "Licence",
        "GPL-3.0-or-later",
      ],
    ],
    "status": {
      "software": "Le firmware compile dans le conteneur ESP-IDF 5.5.5 pour les deux cartes (Wi-Fi et Ethernet).",
      "tests": "382 264 vérifications dans 19 programmes d'hôte réussissent (`ctest`), dont 375 036 sur les règles de manœuvre ; les compteurs et contacteurs sont des simulations.",
      "protocols": "Les trames et lectures des PZEM-004T v3 et PZEM-017 sont vérifiées par rapport aux trames documentées et à des échantillons enregistrés ; aucun compteur n'a encore répondu.",
      "ui": "Les pages des compteurs et des mesures du panneau web ont été essayées dans un navigateur contre un nœud simulé, pas sur une carte.",
      "hardware": "Aucune carte construite ni compteur ou contacteur connectés : rien n'a encore tourné sur de vrais équipements.",
      "security": "Le code de configuration, la connexion avec une limite de mots de passe erronés, le PIN Bluetooth et les mises à jour signées sont testés sur l'hôte ; il n'y a pas eu de revue indépendante.",
      "updates": "Les contrôles de hash et de signature Ed25519 et la logique de retour arrière réussissent sur l'hôte ; une mise à jour par voie hertzienne n'a jamais été exécutée sur une carte.",
      "writing": "Les règles de manœuvre des contacteurs ne sont testées que contre des contacteurs simulés ; rien ici n'a encore commandé quoi que ce soit de réel.",
      "integration": "Les messages du nœud sont validés par rapport aux schémas partagés et aux vecteurs de conformité d'ARMOR-COMMON. Son client MQTT est joué contre un vrai Mosquitto dans les tests ; aucune carte ne les a encore envoyés à un serveur.",
      "docs": "Huit langues, le guide du firmware, les notes de câblage et le journal des modifications sont à jour.",
    },
    "docs": [
      "[Sécurité](docs/SAFETY.md) et [manœuvre](docs/SWITCHING.md) : ce que suppose la conception et comment se passe un transfert",
      "[Messages](docs/ELECTRICAL_MESSAGES.md), [protocoles](docs/PROTOCOLS.md) et [Zigbee](docs/ZIGBEE.md)",
      "[Conception](docs/DESIGN.md), [matériel](docs/HARDWARE.md), [carte de base](docs/BASE_BOARD.md) et [firmware du nœud](docs/NODE_FIRMWARE.md)",
      "[Essais de banc](docs/BENCH_TESTS.md), [code de configuration](docs/SETUP_CODE.md) et [mise en service Bluetooth](docs/BLE_PROVISIONING.md)",
    ],
    "contributing_first": "Avant une pull request, lancez `ctest --test-dir build/host` and `python -I tools/armor_ci_validate.py` : il doit réussir. Voir [CONTRIBUTING.md](CONTRIBUTING.md) et le [code de conduite](CODE_OF_CONDUCT.md).",
    "languages_extra": "",
    "body": {
      "overview": r"""* **Lecture des compteurs :** les trames Modbus RTU des **PZEM-004T v3** (AC) et **PZEM-017** (DC) de Peacefair : le CRC, la requête qui lit les registres et le décodage de la réponse (tension, courant, puissance, énergie, fréquence, facteur de puissance, alarme). Seule la requête de lecture est construite : celles qui écrivent dans un compteur (son adresse, ses seuils, la remise à zéro de son énergie) ne le sont nulle part. Une réponse qui ne convient pas, ou qui contient une valeur qu'aucun compteur réel ne pourrait donner, est refusée.
* **Le bus :** une ligne avec plusieurs compteurs est interrogée un par un, avec un délai ; la dernière bonne lecture de chacun est gardée et un compteur qui se tait n'est plus publié au bout de dix secondes.
* **Le message** `armor/electrical/<nœud>/state` : une entrée par canal (un circuit, une ligne, l'entrée réseau, un bus DC) avec AC ou DC, tension, courant, puissance, énergie, fréquence, facteur de puissance, l'état d'un interrupteur tel que le nœud le voit et une alarme ; il est dans le contrat partagé et porte un état, jamais un ordre.
* **Les règles de commutation,** indépendantes de tout matériel : un contrôleur du transfert entre deux sources qui ne commande jamais les deux, exige la commutation autorisée, le nœud armé juste avant et les deux contacteurs confirmés ouverts pendant tout le temps mort, et transforme un contacteur qui ne montre pas ce qu'on lui a demandé en défaut qui reste jusqu'à son acquittement. **La commutation est désactivée par défaut et rien ne pilote de matériel.**
* **Les ordres à un commutateur, non activés :** le message d'état peut porter l'état des commutateurs du nœud, et le contrat partagé a un ordre (`arm`, puis `close_a` ou `close_b` avec un jeton à usage unique, `open`, `acknowledge`) et la réponse du nœud ; le cœur les lit et y répond avec les règles ci-dessus, testé avec les vecteurs partagés et des contacteurs simulés. Aucune image du firmware ne l'inclut, donc rien ne peut piloter un contacteur, et ARMOR-SERVER refuse d'envoyer un ordre tant qu'il n'a pas été activé (`ARMOR_ELECTRICAL_SWITCHING=1`) et que l'ACL du broker ne l'autorise pas.
* **Où on le voit :** le *Concepteur électrique* d'ARMOR-STUDIO dessine le réseau de la maison et montre sur chaque élément ce que mesure son canal ; ARMOR-SERVER conserve les mesures, leur historique et les sommes.
* **Le firmware du nœud** (ESP32-S3-WROOM-1 N16R8 en Wi-Fi, ou la Waveshare ESP32-S3-ETH sur son câble) : les réglages, une ligne série pour jusqu'à seize compteurs et le panneau web des autres nœuds (mise en service, utilisateurs, Wi-Fi, broker, mise à jour par voie hertzienne, HTTPS) avec ses propres pages Compteurs et Relevés, en huit langues. Il ne fait que lire : les règles de commutation n'y sont pas liées. Voir [le firmware](docs/NODE_FIRMWARE.md).
* **Configuration depuis le téléphone en Bluetooth,** le même canal que celui du nœud radar : l'app ARMOR trouve le nœud sous le nom `ARMOR-XXXXXX` et règle son nom, son Wi-Fi, son adresse, son broker et son mode Bluetooth avec les utilisateurs et le code de mise en service du panneau ([le protocole](docs/BLE_PROVISIONING.md)). Il n'écoute que tant que le nœud n'a pas d'utilisateur, sauf réglage contraire. La partie radio n'a jamais tourné sur une carte.
* **Mises à jour par radio signées :** le nœud n'installe depuis GitHub qu'une image dont le SHA-256 correspond et qui porte une signature Ed25519 valide du responsable (la clé publique est dans le firmware, la privée ne quitte jamais le responsable) ; un fichier envoyé à la main par un administrateur dans le panneau reste accepté. Les pages et messages du panneau sont en huit langues.
* **Appairage Bluetooth avec un PIN :** le PIN à six chiffres est dérivé du code de configuration, imprimé sur la console USB et montré à un administrateur dans le panneau ; le téléphone doit le saisir avant de pouvoir écrire les réglages du nœud.
* **Pas encore :** le firmware qui tourne sur une carte, le matériel, toute mesure d'une installation réelle et toute commutation.
* **Seule la maison peut utiliser le panneau :** le panneau répond par défaut au réseau privé (ou aux réseaux que son propriétaire indique, comme un VPN), refuse une liste qui exclurait celui qui l'enregistre, compte les mauvais mots de passe par personne et par adresse, et fonctionne derrière le proxy du serveur pour être atteint depuis l'extérieur sans publier le nœud.
* **Les estimations le disent :** un canal fait à partir d'une entrée de courant porte `power_estimated` ; Studio et le serveur affichent sa puissance comme une estimation (puissance apparente à partir d'un courant et d'une tension nominale) et signalent une valeur réseau qui en contient une.
* **Liaison chiffrée facultative avec le broker (TLS) :** désactivée par défaut, le nœud parle donc MQTT non chiffré comme avant. Un interrupteur et une zone pour le certificat de l'autorité propre à l'installation (PEM, 2 Ko au plus) dans la page Broker lui font se connecter en `mqtts://`, ne faire confiance qu'à cette autorité et vérifier que le certificat du broker a été établi pour l'adresse atteinte ; ce qui n'est pas un seul certificat PEM est refusé. Couvert par des tests sur ordinateur ; la poignée de main n'a pas encore été exécutée sur une carte.
* **Rapport de santé :** environ une fois par minute le nœud publie depuis combien de temps il tourne et pourquoi il a redémarré la dernière fois, sa mémoire libre, sa liaison et son signal Wi-Fi, combien de fois il s'est connecté au broker et la dernière erreur notée (`armor/health/<nœud>`, le contrat `node_health` d'ARMOR-COMMON). Le code qui le construit est partagé par tous les nœuds et testé sur un ordinateur ; il n'a pas tourné sur une carte.
* **Commande depuis le serveur :** Studio peut redémarrer le nœud proprement, le mettre en pause jusqu'à une heure (il reprend seul), mettre son travail en veille (sans fin, conservée aux redémarrages, le nœud reste connecté et continue de répondre), le faire se signaler, demander un instantané de diagnostic et le marquer en maintenance (`armor/control/<nœud>/...`, le contrat `node_control` d'ARMOR-COMMON). Chaque ordre se fait en deux temps avec un jeton à usage unique propre à cette opération, seul le serveur peut les écrire sur le broker, et il n'existe ni réinitialisation d'usine, ni effacement, ni sommeil profond. Tant que le nœud est en pause ou en veille, tous les relais sont ouverts et aucun ne bouge, quoi qu'on demande (le panneau, le broker ou une centrale) ; les compteurs continuent d'être lus. Le code est partagé par tous les nœuds et testé sur un ordinateur ; il n'a pas tourné sur une carte.
* **Des mesures qui disent leur fraîcheur :** chaque canal de compteur porte l'âge de sa mesure et le nombre de requêtes échouées vers le compteur, si bien que le serveur distingue un vrai 0 W d'un compteur qui ne répond plus ; et une tâche des compteurs bloquée redémarre la carte grâce au chien de garde.
* **Diagnostic sans câble :** après un démarrage qui n'était pas propre (plantage, chien de garde, chute d'alimentation, allocation échouée), le rapport de santé en donne la raison pendant dix minutes ; un plantage laisse son vidage mémoire (core dump) à consulter, télécharger ou effacer depuis le panneau ; les réglages enregistrés sont copiés avant chaque installation de micrologiciel et récupérés si une mise à jour les abîme ; et un administrateur peut demander au nœud, via le serveur, un paquet de diagnostic ou son journal avec un jeton à usage unique.
* **Verrouillage de relais :** un relais peut en désigner un autre qui ne doit jamais être fermé en même temps (les deux sources d'une charge, les deux sens d'un moteur) ; la demande de fermer l'un alors que l'autre est fermé est refusée depuis le panneau, le broker et la centrale, et le nœud n'ouvre jamais l'autre de lui-même. Testé sur un ordinateur ; non exécuté sur une carte.
* **Lecture seule des réglages propres des compteurs :** après la première bonne lecture et tous les `bus.check_settings_s` (600 s, 0 = jamais), le nœud lit les registres holding du PZEM (004T v3 : seuil de puissance et adresse ; 017 : seuils de tension, adresse et shunt) dans le même tour que les mesures, et avertit si l'adresse enregistrée n'est pas celle qu'il utilise ; rien n'est écrit dans le compteur.
* **Scellement facultatif des secrets enregistrés :** désactivé par défaut (`security.seal_secrets`, ou `nodes.nvs_encryption` du serveur). Activé, les mots de passe, jetons, clés, codes PIN et empreintes de mots de passe que le nœud enregistre sont scellés avec ChaCha20-Poly1305 et tout le reste reste lisible ; l'activer ou le désactiver les réécrit sans rien perdre, même si le nœud s'arrête en route. Aucun eFuse n'est brûlé et la flash n'est pas chiffrée : la clé est dans une partition de la même puce, donc cela ne protège **pas** contre quelqu'un qui tient la carte, et un nœud installé avant cette partition garde ses secrets tels quels jusqu'à ce qu'il soit flashé avec la nouvelle table de partitions.""",
      "role": r"""ARMOR-NODE-ELECTRICAL mesure le réseau AC et DC de la maison avec ses compteurs et garde les règles pour commuter entre sources. Il publie les mesures pour [ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER), qui garde leur historique et l'énergie de chaque jour et déclenche les alarmes ; le menu *Électrique* et le *Concepteur électrique* d'[ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) et l'écran électrique d'[ARMOR-ANDROID-CONTROL](https://github.com/JuanenRac/ARMOR-ANDROID-CONTROL) le montrent. La commutation est conçue (armer, un jeton à usage unique, l'interverrouillage, la confirmation des deux contacteurs) mais pas activée.

| Nom | Comment | À quoi ça sert |
|---|---|---|
| ARMOR-SERVER | MQTT `armor/electrical/<id>/{state,command,result}` | Reçoit les canaux et commande un transfert (seulement si la manœuvre est activée à trois endroits) |
| ARMOR-STUDIO | menu Électrique, Electrical Designer | Montre les canaux et les alarmes et ouvre le panneau du nœud |
| ARMOR-ANDROID-CONTROL | Bluetooth | Configure le nœud sur le terrain et montre les canaux |
| ARMOR-COMMON | contrat électrique | Les messages sont vérifiés avec ses schémas ; le firmware commun en est copié |""",
      "architecture": r"""<p align="center">
  <img src="images/architecture.svg" alt="Architecture de ARMOR-NODE-ELECTRICAL : qui l'appelle, ce qu'il contient et de quoi il dépend" width="100%">
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
| Secteur ou continu dangereux sur la carte | Le nœud ne fait que lire les modules PZEM (modules fermés, ligne série isolée) et ne porte jamais le secteur sur sa carte ; ce qui commute est un étage séparé testé sur banc avec une lampe et un transformateur d'isolement |
| Deux sources fermées en même temps | Le contrôleur de transfert n'ordonne jamais les deux : il exige la manœuvre permise, le nœud armé juste avant et les deux contacteurs confirmés ouverts pendant tout le temps mort (`dead_time_ms` 2000 par défaut) ; un contacteur qui ne montre pas ce qui a été ordonné est un défaut qui reste jusqu'à l'acquittement (`kDidNotOpen`, `kDidNotClose`) ; un enclenchement mécanique entre les contacteurs reste obligatoire |
| Un ordre répété, ou une manœuvre que personne n'a demandée | `arm` donne un jeton à usage unique de 64 bits que `close_a` ou `close_b` doivent porter, dans `arm_window_ms` ; les ordres ne sont jamais retenus ; au plus 4 interrupteurs ; la manœuvre est DÉSACTIVÉE sauf si le firmware l'autorise (`switching_enabled`), si le serveur tourne avec `ARMOR_ELECTRICAL_SWITCHING=1` et si la liste d'accès du broker est ouverte pour ce nœud |
| Un défaut, un retour perdu ou la manœuvre désactivée | Chaque contrôleur répond avec TOUTES les bobines ouvertes (défaut => ouvert ; si ouvert est sûr pour la charge, c'est à l'installation de le décider) ; l'état dans le message est ce que montre le contact auxiliaire, pas ce qui a été ordonné ; les paires de relais sont verrouillées et le nœud n'ouvre jamais le partenaire de lui-même |
| Une mesure ancienne présentée comme réelle | Un compteur muet cesse d'être publié après 10 s ; chaque canal porte l'âge de sa mesure et le nombre de requêtes échouées ; une tâche de compteurs bloquée redémarre la carte par watchdog ; tous les `bus.check_settings_s` (600 s, 0 = jamais) les réglages des compteurs sont lus (lecture seule) et une adresse modifiée est signalée |

Le secteur (230 V CA) et le courant continu d'un banc de batteries peuvent tuer et provoquer des incendies. [docs/SAFETY.md](docs/SAFETY.md) dit ce que suppose la conception ; ce n'est pas la conception d'une installation et cela ne remplace ni la réglementation du pays ni un installateur qualifié. Aujourd'hui rien ici ne commute quoi que ce soit.""",
      "interfaces": r"""| Partie | Ce qu'elle règle |
|---|---|
| MQTT | `armor/electrical/<id>/state` (un canal par entrée : CA ou CC, tension, courant, puissance, énergie, fréquence, facteur de puissance, état de l'interrupteur, alarme ; contrat d'ARMOR-COMMON), `armor/electrical/<id>/command` et `/result`, `armor/device/<id>/<relais>/{state,set}`, `armor/health/<id>`, `armor/control/<id>/...` |
| Commandes | `arm`, `close_a`, `close_b` (avec le jeton), `open` et `acknowledge` (efface un défaut) |
| Compteurs | Peacefair PZEM-004T v3 (CA) et PZEM-017 (CC) en Modbus RTU, jusqu'à 16 sur une ligne série ; seule la requête de lecture est construite (celle qui écrit adresse ou seuils n'existe pas) ; entrées analogiques, contacts et relais sur la carte de base ; un pont Zigbee ([docs/ZIGBEE.md](docs/ZIGBEE.md)) |""",
      "configuration": r"""| Variable | Par défaut | Ce qu'elle règle |
|---|---|---|
| `bus.check_settings_s` | 600 | Secondes entre les contrôles en lecture seule des réglages des compteurs (0 = jamais) |
| `dead_time_ms`, `confirm_timeout_ms` | 2000 | Le temps mort d'un transfert et le temps dont un contacteur dispose pour montrer ce qui a été ordonné |
| `switching_enabled` | off | La manœuvre est DÉSACTIVÉE sauf si ce réglage, le serveur (`ARMOR_ELECTRICAL_SWITCHING=1`) et la liste d'accès du broker l'autorisent |
| `CONFIG_ARMOR_NODE_ID`, `_SETUP_CODE`, `_FLEET_SECRET`, `_MQTT_*`, `_HEARTBEAT_S`, `_BLE_SETUP_MINUTES`, `_BOOT_FACTORY_RESET` | - | Les réglages que tous les nœuds partagent : le nom (vide donne `armor-` et les derniers octets de la MAC), le code de configuration (vide : aléatoire), le secret de flotte (16+ caractères, jamais dans le dépôt), les premiers réglages du broker, le battement (de 2 à 300 s), les minutes de configuration Bluetooth (de 1 à 120) et la réinitialisation avec BOOT (8 s dans les 30 premières s) |""",
      "quickstart": r"""**Prérequis:** un compilateur C++17 pour les tests sur hôte ; le conteneur ESP-IDF 5.5.5 pour construire l'image ; une carte ESP32-S3 (Ethernet ou Wi-Fi).

```bash
cmake -S tests -B build/host && cmake --build build/host && ctest --test-dir build/host   # host tests, -Werror
node tools/panel_mock.mjs --user admin:adminpass123   # the panel without a board
tools/build_node.sh generic s3-wifi                  # the image in the ESP-IDF container (or s3-eth)
```

See the [firmware guide](docs/NODE_FIRMWARE.md) and the [Bluetooth channel](docs/BLE_PROVISIONING.md).

Voir la [conception](docs/DESIGN.md), les [notes de sécurité](docs/SAFETY.md), les [règles de commutation](docs/SWITCHING.md), les [protocoles](docs/PROTOCOLS.md) et les [messages](docs/ELECTRICAL_MESSAGES.md).""",
      "testing": r"""```bash
cmake -S tests -B build/host && cmake --build build/host && ctest --test-dir build/host
python -I tools/armor_ci_validate.py
```

19 programmes de test sur hôte et 5 contrôles Python tournent sous `ctest` ; 382264 vérifications comptées par les programmes hôte, compilés avec `-Werror`.

Contrôles Python : les textes du panneau en huit langues, les tâches, les chemins de sauvegarde, la session Bluetooth sous son verrou et les routes appelées par le panneau (et, dans certains nœuds, les codes HTTP ou les glyphes des polices)

Les tests sur hôte demandent un compilateur C++17 quelconque (Linux, WSL, MSYS2) ; le panneau web est aussi exercé dans un vrai navigateur contre un nœud de substitution (`tools/panel_mock.mjs`, `tools/panel_browser_test.mjs`).

La plupart des vérifications sont des balayages exhaustifs des règles de manœuvre (`test_switch_set` et `test_interlock` : 375 036) ; les compteurs et contacteurs sont des substituts. `test_clock` n'imprime que `ok`.""",
      "build": "`tools/build_node.sh` construit l'image dans le conteneur ESP-IDF 5.5.5 et la version porte l'image, son SHA-256 et sa signature Ed25519, une par carte ; l'image est écrite par USB-C la première fois, puis mise à jour depuis le panneau.",
      "troubleshooting": r"""| Vous voyez | Parce que | Faites |
|---|---|---|
| Vous avez perdu le mot de passe ou le nœud ne rejoint plus le réseau | Un nœud en configuration sans adresse après 90 s ouvre son propre Wi-Fi `ARMOR-SETUP-xxxxxx` (ouvrez `http://192.168.4.1/`) | Pour recommencer, maintenez BOOT 8 secondes dans les 30 premières secondes après la mise sous tension (efface réglages et utilisateurs), ou utilisez *Réinitialisation d'usine* dans le panneau |
| Une mise à jour depuis GitHub est refusée | La version n'a ni somme de contrôle ni signature, elles ne concordent pas (`e_no_checksum`, `e_no_signature`, `e_checksum_mismatch`, `e_bad_signature`), n'a pas d'image pour cette carte (`e_no_asset_for_board`) ou est d'un autre projet (`e_wrong_firmware`) | Le nœud n'a pas changé ; réessayez ou laissez un administrateur envoyer le fichier à la main |
| Un interrupteur montre un défaut | Le contacteur n'a pas montré ouvert ou fermé comme ordonné (`kDidNotOpen`, `kDidNotClose`) ; il reste jusqu'à l'acquittement | Vérifiez le câblage du contact auxiliaire, puis envoyez `acknowledge` |
| Une commande est refusée | La manœuvre est désactivée (`switching_enabled` faux), le jeton est invalide ou expiré, ou le nœud n'était pas armé juste avant | Armez de nouveau et envoyez l'ordre avec le nouveau jeton |""",
      "structure": r"""<p align="center">
  <img src="images/repository-structure.svg" alt="Structure du dépôt de ARMOR-NODE-ELECTRICAL" width="100%">
</p>

<details>
<summary>Version texte de l'arborescence</summary>

```text
ARMOR-NODE-ELECTRICAL/
├── main/                                le firmware : un composant ESP-IDF
├── core/                                la logique sans ESP-IDF, testée sur ordinateur
├── panel/                               le panneau web intégré au firmware
├── tests/                               tests sur hôte et contrôles Python
├── docs/                                12 guides : sécurité, manœuvre, messages, matériel
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

* Les trames et lectures des PZEM-004T v3 et PZEM-017 sont vérifiées par rapport aux trames documentées et à des échantillons enregistrés ; aucun compteur n'a encore répondu.
* Les pages des compteurs et des mesures du panneau web ont été essayées dans un navigateur contre un nœud simulé, pas sur une carte.
* Aucune carte construite ni compteur ou contacteur connectés : rien n'a encore tourné sur de vrais équipements.
* Le code de configuration, la connexion avec une limite de mots de passe erronés, le PIN Bluetooth et les mises à jour signées sont testés sur l'hôte ; il n'y a pas eu de revue indépendante.
* Les contrôles de hash et de signature Ed25519 et la logique de retour arrière réussissent sur l'hôte ; une mise à jour par voie hertzienne n'a jamais été exécutée sur une carte.
* Les règles de manœuvre des contacteurs ne sont testées que contre des contacteurs simulés ; rien ici n'a encore commandé quoi que ce soit de réel.

**Ensuite**

* Essayer les compteurs, les contacteurs et les règles de manœuvre sur un banc avec une lampe et un transformateur d'isolement, puis une vraie carte avec la mise à jour par voie aérienne.""",
    },
  },
  "it": {
    "tagline": "Nodo elettrico: legge tensioni, correnti, potenza ed energia della rete AC e DC della casa e custodisce le regole per manovrarla (nucleo testato sul PC e un firmware che compila; non ha mai girato su una scheda)",
    "honest": "Il nucleo (i frame dei contatori PZEM-004T v3 e PZEM-017, il bus che li interroga, il messaggio del nodo, gli ingressi analogici e le regole di commutazione: 382.264 controlli in 19 programmi di test, 375.036 dei quali sulle regole di commutazione) è provato su un computer con contatori e contattori sostitutivi, e i messaggi che produce sono accettati da ARMOR-COMMON. Il firmware del nodo (le impostazioni, la linea seriale, le pagine Contatori e Letture del suo pannello, Bluetooth, aggiornamenti firmati) si compila nel contenitore ESP-IDF 5.5.5 per entrambe le schede. **Non ha mai girato su una scheda, nulla è stato collegato a un contatore o a un contattore, e nulla qui commuta niente.**",
    "glance": [
      [
        "Ruolo",
        "Nodo di campo elettrico: contatori, ingressi e manovra (famiglia: Field Nodes, padre: ARMOR-COMMON)",
      ],
      [
        "Tecnologia",
        "C++17, ESP-IDF 5.5.5, ESP32-S3",
      ],
      [
        "Test",
        "382264 verifiche in 19 programmi host e 5 verifiche Python (`ctest`)",
      ],
      [
        "Apparecchiature",
        "Contatori PZEM-004T v3 e PZEM-017 (fino a 16), ingressi analogici, relè; manovra spenta di default",
      ],
      [
        "Gira su",
        "Una scheda ESP32-S3 (Ethernet o Wi-Fi); test su host su qualsiasi computer",
      ],
      [
        "Su hardware reale",
        "Ancora nessuno: nessuna scheda montata né contatore o contattore collegati; nulla commuta niente",
      ],
      [
        "Licenza",
        "GPL-3.0-or-later",
      ],
    ],
    "status": {
      "software": "Il firmware compila nel contenitore ESP-IDF 5.5.5 per entrambe le schede (Wi-Fi ed Ethernet).",
      "tests": "Superano 382.264 controlli in 19 programmi host (`ctest`), 375.036 dei quali sulle regole di manovra; i contatori e i contattori sono simulazioni.",
      "protocols": "I frame e le letture dei PZEM-004T v3 e PZEM-017 sono verificati contro i frame documentati e campioni registrati; nessun contatore ha ancora risposto.",
      "ui": "Le pagine dei contatori e delle letture del pannello web sono state provate in un browser contro un nodo simulato, non su una scheda.",
      "hardware": "Nessuna scheda costruita e nessun contatore o contattore collegati: nulla ha ancora funzionato su apparecchiature reali.",
      "security": "Il codice di configurazione, l'accesso con limite di password errate, il PIN Bluetooth e gli aggiornamenti firmati sono testati sull'host; non c'è stata una revisione indipendente.",
      "updates": "I controlli di hash e firma Ed25519 e la logica di ripristino passano sull'host; un aggiornamento via etere non è mai stato eseguito su una scheda.",
      "writing": "Le regole di manovra dei contattori sono provate solo contro contattori simulati; nulla qui ha ancora comandato qualcosa di reale.",
      "integration": "I messaggi del nodo sono validati contro gli schemi condivisi e i vettori di conformità di ARMOR-COMMON. Il suo client MQTT viene provato contro un vero Mosquitto nei test; nessuna scheda li ha ancora inviati a un server.",
      "docs": "Otto lingue, la guida del firmware, le note di cablaggio e il registro delle modifiche sono aggiornati.",
    },
    "docs": [
      "[Sicurezza](docs/SAFETY.md) e [manovra](docs/SWITCHING.md): cosa presuppone il progetto e come avviene un trasferimento",
      "[Messaggi](docs/ELECTRICAL_MESSAGES.md), [protocolli](docs/PROTOCOLS.md) e [Zigbee](docs/ZIGBEE.md)",
      "[Progetto](docs/DESIGN.md), [hardware](docs/HARDWARE.md), [scheda base](docs/BASE_BOARD.md) e [firmware del nodo](docs/NODE_FIRMWARE.md)",
      "[Prove al banco](docs/BENCH_TESTS.md), [codice di configurazione](docs/SETUP_CODE.md) e [provisioning Bluetooth](docs/BLE_PROVISIONING.md)",
    ],
    "contributing_first": "Prima di una pull request esegui `ctest --test-dir build/host` and `python -I tools/armor_ci_validate.py`: deve passare. Vedi [CONTRIBUTING.md](CONTRIBUTING.md) e il [codice di condotta](CODE_OF_CONDUCT.md).",
    "languages_extra": "",
    "body": {
      "overview": r"""* **Lettura dei contatori:** i frame Modbus RTU dei **PZEM-004T v3** (AC) e **PZEM-017** (DC) di Peacefair: il CRC, la richiesta che legge i registri e la decodifica della risposta (tensione, corrente, potenza, energia, frequenza, fattore di potenza, allarme). Si costruisce solo la richiesta di lettura: quelle che scrivono in un contatore (indirizzo, soglie, azzeramento dell'energia) non si costruiscono da nessuna parte. Una risposta che non torna, o con un valore che nessun contatore reale potrebbe dare, viene rifiutata.
* **Il bus:** una linea con più contatori si interroga uno alla volta, con un timeout; si conserva l'ultima lettura buona di ciascuno e un contatore che tace non viene più pubblicato dopo dieci secondi.
* **Il messaggio** `armor/electrical/<nodo>/state`: una voce per canale (un circuito, una linea, l'ingresso di rete, un bus DC) con AC o DC, tensione, corrente, potenza, energia, frequenza, fattore di potenza, lo stato di un interruttore come lo vede il nodo e un allarme; è nel contratto condiviso e porta uno stato, mai un comando.
* **Le regole di manovra,** a prescindere da qualsiasi hardware: un controllore dello scambio tra due sorgenti che non comanda mai entrambe, richiede la manovra consentita, il nodo armato poco prima e i due contattori confermati aperti per tutto il tempo morto, e trasforma un contattore che non mostra ciò che gli è stato ordinato in un guasto che resta finché non viene riconosciuto. **La manovra è disattivata per impostazione predefinita e nulla pilota alcun hardware.**
* **I comandi a un commutatore, non attivati:** il messaggio di stato può portare lo stato dei commutatori del nodo, e il contratto condiviso ha un comando (`arm`, poi `close_a` o `close_b` con un token monouso, `open`, `acknowledge`) e la risposta del nodo; il nucleo li legge e risponde con le regole sopra, provato con i vettori condivisi e con contattori simulati. Nessuna immagine del firmware lo include, quindi nulla può azionare un contattore, e ARMOR-SERVER rifiuta di inviare un comando se non è stato attivato (`ARMOR_ELECTRICAL_SWITCHING=1`) e l'ACL del broker non lo consente.
* **Dove si vede:** il *Progettista elettrico* di ARMOR-STUDIO disegna la rete della casa e mostra su ogni elemento ciò che misura il suo canale; ARMOR-SERVER conserva le letture, la loro cronologia e le somme.
* **Il firmware del nodo** (ESP32-S3-WROOM-1 N16R8 in Wi-Fi, o la Waveshare ESP32-S3-ETH sul suo cavo): le impostazioni, una linea seriale per fino a sedici contatori e il pannello web degli altri nodi (messa in servizio, utenti, Wi-Fi, broker, aggiornamento via etere, HTTPS) con le sue pagine Contatori e Letture, in otto lingue. Legge soltanto: le regole di manovra non sono collegate. Vedi [il firmware](docs/NODE_FIRMWARE.md).
* **Configurazione dal telefono via Bluetooth,** lo stesso canale del nodo radar: l'app ARMOR trova il nodo come `ARMOR-XXXXXX` e ne imposta nome, Wi-Fi, indirizzo, broker e modo Bluetooth con gli utenti e il codice di messa in servizio del pannello ([il protocollo](docs/BLE_PROVISIONING.md)). Ascolta solo finché il nodo non ha utenti, salvo diversa impostazione. La parte radio non ha mai girato su una scheda.
* **Aggiornamenti via etere firmati:** il nodo installa da GitHub solo un'immagine il cui SHA-256 coincide e che porta una firma Ed25519 valida del responsabile (la chiave pubblica è nel firmware, quella privata non lascia mai il responsabile); un file caricato a mano da un amministratore nel pannello resta accettato. Le pagine e i messaggi del pannello sono in otto lingue.
* **Abbinamento Bluetooth con PIN:** il PIN a sei cifre deriva dal codice di configurazione, è stampato sulla console USB e mostrato a un amministratore nel pannello; il telefono deve inserirlo prima di poter scrivere le impostazioni del nodo.
* **Non ancora:** il firmware in funzione su una scheda, l'hardware, qualsiasi misura di un impianto reale e qualsiasi manovra.
* **Solo la casa può usare il pannello:** il pannello risponde per impostazione predefinita alla rete privata (o alle reti indicate dal proprietario, come una VPN), rifiuta un elenco che escluderebbe chi lo salva, conta le password errate per persona e per indirizzo e funziona dietro il proxy del server per essere raggiunto da fuori casa senza pubblicare il nodo.
* **Le stime lo dicono:** un canale ricavato da un ingresso di corrente porta `power_estimated`; Studio e il server mostrano la sua potenza come stima (potenza apparente da una corrente e una tensione nominale) e segnalano un valore di rete che ne include una.
* **Collegamento cifrato facoltativo con il broker (TLS):** disattivato per impostazione predefinita, quindi il nodo parla MQTT non cifrato come prima. Un interruttore e una casella per il certificato dell'autorità propria dell'installazione (PEM, al massimo 2 KB) nella pagina Broker lo fanno collegare con `mqtts://`, fidarsi solo di quell'autorità e verificare che il certificato del broker sia stato fatto per l'indirizzo raggiunto; ciò che non è un solo certificato PEM viene rifiutato. Coperto da test sul computer; l'handshake non è ancora stato eseguito su una scheda.
* **Rapporto di salute:** circa una volta al minuto il nodo pubblica da quanto è acceso e perché si è riavviato l'ultima volta, la memoria libera, il collegamento e il segnale Wi-Fi, quante volte si è connesso al broker e l'ultimo errore registrato (`armor/health/<nodo>`, il contratto `node_health` di ARMOR-COMMON). Il codice che lo costruisce è condiviso da tutti i nodi e testato su un computer; non è mai girato su una scheda.
* **Controllo dal server:** Studio può riavviare il nodo in modo pulito, metterlo in pausa fino a un'ora (riprende da solo), mettere il suo lavoro in standby (senza fine, conservato ai riavvii, il nodo resta connesso e continua a rispondere), farlo mostrare, chiedere un'istantanea diagnostica e segnarlo in manutenzione (`armor/control/<nodo>/...`, il contratto `node_control` di ARMOR-COMMON). Ogni ordine è in due passi con un token monouso legato a quell'operazione, solo il server può scriverli sul broker e non esistono ripristino di fabbrica, cancellazione né sonno profondo. Finché il nodo è in pausa o in standby tutti i relè sono aperti e nessuno si muove, chiunque lo chieda (il pannello, il broker o una centrale); i contatori continuano a essere letti. Il codice è condiviso da tutti i nodi e provato su un computer; non ha ancora girato su una scheda.
* **Letture che dicono quanto sono fresche:** ogni canale del contatore porta l'età della sua lettura e quante richieste al contatore sono fallite, così il server distingue uno 0 W reale da un contatore che ha smesso di rispondere; e un task dei contatori bloccato riavvia la scheda tramite il watchdog.
* **Diagnostica senza cavo:** dopo un avvio non pulito (un blocco, un watchdog, un calo di alimentazione, un'allocazione fallita) il rapporto di salute ne indica la causa per dieci minuti; un arresto anomalo lascia il suo core dump da vedere, scaricare o cancellare dal pannello; le impostazioni salvate vengono copiate prima di ogni installazione del firmware e recuperate se un aggiornamento le danneggia; e un amministratore può chiedere al nodo, tramite il server, un pacchetto di diagnostica o il suo registro con un token monouso.
* **Interblocco dei relè:** un relè può indicarne un altro che non deve mai essere chiuso contemporaneamente (le due sorgenti di un carico, i due sensi di un motore); la richiesta di chiuderne uno mentre l'altro è chiuso viene rifiutata dal pannello, dal broker e dalla centrale, e il nodo non apre mai l'altro da sé. Provato su un computer; non eseguito su una scheda.
* **Lettura, solo lettura, delle impostazioni proprie dei contatori:** dopo la prima lettura buona e ogni `bus.check_settings_s` (600 s, 0 = mai) il nodo legge i registri holding del PZEM (004T v3: soglia di potenza e indirizzo; 017: soglie di tensione, indirizzo e shunt) nello stesso turno delle misure, e avverte se l'indirizzo salvato non è quello usato; nel contatore non si scrive nulla.
* **Sigillatura facoltativa dei segreti salvati:** disattivata per impostazione predefinita (`security.seal_secrets`, o `nodes.nvs_encryption` del server). Attiva, le password, i token, le chiavi, i PIN e gli hash delle password che il nodo salva restano sigillati con ChaCha20-Poly1305 e tutto il resto resta leggibile; attivarla o disattivarla li riscrive senza perdere nulla, anche se il nodo si ferma a metà. Nessun eFuse viene bruciato e la flash non è cifrata: la chiave si trova in una partizione dello stesso chip, quindi **non** protegge da chi ha la scheda, e un nodo installato prima di quella partizione mantiene i suoi segreti com'erano finché non viene flashato con la nuova tabella delle partizioni.""",
      "role": r"""ARMOR-NODE-ELECTRICAL misura la rete CA e CC della casa con i suoi contatori e conserva le regole per commutare fra sorgenti. Pubblica le letture per [ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER), che conserva lo storico e l'energia di ogni giorno e genera gli allarmi; il menu *Elettrico* e il *Progettista elettrico* di [ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) e la schermata elettrica di [ARMOR-ANDROID-CONTROL](https://github.com/JuanenRac/ARMOR-ANDROID-CONTROL) lo mostrano. La commutazione è progettata (inserire, un token monouso, l'interblocco, la conferma di entrambi i contattori) ma non attivata.

| Nome | Come | A cosa serve |
|---|---|---|
| ARMOR-SERVER | MQTT `armor/electrical/<id>/{state,command,result}` | Riceve i canali e ordina un trasferimento (solo se la manovra è attiva in tre punti) |
| ARMOR-STUDIO | menu Elettrico, Electrical Designer | Mostra i canali e gli allarmi e apre il pannello del nodo |
| ARMOR-ANDROID-CONTROL | Bluetooth | Configura il nodo sul campo e mostra i canali |
| ARMOR-COMMON | contratto elettrico | I messaggi sono verificati con i suoi schemi; il firmware comune è copiato da lì |""",
      "architecture": r"""<p align="center">
  <img src="images/architecture.svg" alt="Architettura di ARMOR-NODE-ELECTRICAL: chi lo chiama, cosa contiene e da cosa dipende" width="100%">
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
| Rete o continua pericolosa sulla scheda | Il nodo legge solo i moduli PZEM (moduli chiusi, linea seriale isolata) e non porta mai la rete sulla sua scheda; ciò che commuta è uno stadio separato provato al banco con una lampada e un trasformatore di isolamento |
| Due sorgenti chiuse insieme | Il controllore di trasferimento non ordina mai entrambe: richiede manovra consentita, nodo armato poco prima ed entrambi i contattori confermati aperti per tutto il tempo morto (`dead_time_ms` 2000 di default); un contattore che non mostra ciò che è stato ordinato è un guasto che resta fino al riconoscimento (`kDidNotOpen`, `kDidNotClose`); resta obbligatorio un interblocco meccanico tra i contattori |
| Un ordine ripetuto, o una manovra che nessuno ha chiesto | `arm` dà un token monouso a 64 bit che `close_a` o `close_b` devono portare, entro `arm_window_ms`; gli ordini non vengono mai trattenuti; al massimo 4 interruttori; la manovra è SPENTA salvo che il firmware la consenta (`switching_enabled`), il server giri con `ARMOR_ELECTRICAL_SWITCHING=1` e la lista di accesso del broker sia aperta per quel nodo |
| Un guasto, un feedback perso o la manovra spenta | Ogni controllore risponde con TUTTE le bobine aperte (guasto => aperto; se aperto è sicuro per il carico lo decide l'impianto); lo stato nel messaggio è ciò che mostra il contatto ausiliario, non ciò che è stato ordinato; le coppie di relè sono interbloccate e il nodo non apre mai il partner da solo |
| Una lettura vecchia mostrata come reale | Un contatore muto smette di essere pubblicato dopo 10 s; ogni canale porta l'età della sua lettura e il numero di richieste fallite; un task dei contatori bloccato riavvia la scheda tramite watchdog; ogni `bus.check_settings_s` (600 s, 0 = mai) le impostazioni dei contatori vengono lette (sola lettura) e un indirizzo cambiato viene segnalato |

La rete (230 V CA) e la corrente continua di un banco di batterie possono uccidere e provocare incendi. [docs/SAFETY.md](docs/SAFETY.md) dice cosa presuppone il progetto; non è il progetto di un impianto e non sostituisce le norme del paese né un installatore qualificato. Oggi nulla di tutto ciò commuta nulla.""",
      "interfaces": r"""| Parte | Cosa imposta |
|---|---|
| MQTT | `armor/electrical/<id>/state` (un canale per ingresso: CA o CC, tensione, corrente, potenza, energia, frequenza, fattore di potenza, stato dell'interruttore, allarme; contratto di ARMOR-COMMON), `armor/electrical/<id>/command` e `/result`, `armor/device/<id>/<relè>/{state,set}`, `armor/health/<id>`, `armor/control/<id>/...` |
| Comandi | `arm`, `close_a`, `close_b` (con il token), `open` e `acknowledge` (cancella un guasto) |
| Contatori | Peacefair PZEM-004T v3 (CA) e PZEM-017 (CC) via Modbus RTU, fino a 16 su una linea seriale; si costruisce solo la richiesta di lettura (quella che scrive indirizzo o soglie non esiste); ingressi analogici, contatti e relè sulla scheda base; un ponte Zigbee ([docs/ZIGBEE.md](docs/ZIGBEE.md)) |""",
      "configuration": r"""| Variabile | Predefinito | Cosa imposta |
|---|---|---|
| `bus.check_settings_s` | 600 | Secondi tra le verifiche in sola lettura delle impostazioni dei contatori (0 = mai) |
| `dead_time_ms`, `confirm_timeout_ms` | 2000 | Il tempo morto di un trasferimento e quanto tempo ha un contattore per mostrare ciò che è stato ordinato |
| `switching_enabled` | off | La manovra è SPENTA salvo che questa impostazione, il server (`ARMOR_ELECTRICAL_SWITCHING=1`) e la lista di accesso del broker la consentano |
| `CONFIG_ARMOR_NODE_ID`, `_SETUP_CODE`, `_FLEET_SECRET`, `_MQTT_*`, `_HEARTBEAT_S`, `_BLE_SETUP_MINUTES`, `_BOOT_FACTORY_RESET` | - | Le impostazioni che tutti i nodi condividono: il nome (vuoto dà `armor-` e gli ultimi byte del MAC), il codice di configurazione (vuoto: casuale), il segreto di flotta (16+ caratteri, mai nel repository), le prime impostazioni del broker, il battito (da 2 a 300 s), i minuti di configurazione Bluetooth (da 1 a 120) e il ripristino con BOOT (8 s nei primi 30 s) |""",
      "quickstart": r"""**Requisiti:** un compilatore C++17 per i test su host; il container ESP-IDF 5.5.5 per costruire l'immagine; una scheda ESP32-S3 (Ethernet o Wi-Fi).

```bash
cmake -S tests -B build/host && cmake --build build/host && ctest --test-dir build/host   # host tests, -Werror
node tools/panel_mock.mjs --user admin:adminpass123   # the panel without a board
tools/build_node.sh generic s3-wifi                  # the image in the ESP-IDF container (or s3-eth)
```

See the [firmware guide](docs/NODE_FIRMWARE.md) and the [Bluetooth channel](docs/BLE_PROVISIONING.md).

Vedi il [progetto](docs/DESIGN.md), le [note di sicurezza](docs/SAFETY.md), le [regole di manovra](docs/SWITCHING.md), i [protocolli](docs/PROTOCOLS.md) e i [messaggi](docs/ELECTRICAL_MESSAGES.md).""",
      "testing": r"""```bash
cmake -S tests -B build/host && cmake --build build/host && ctest --test-dir build/host
python -I tools/armor_ci_validate.py
```

19 programmi di test su host e 5 verifiche Python girano con `ctest`; 382264 verifiche contate dai programmi host, compilati con `-Werror`.

Verifiche Python: i testi del pannello in otto lingue, i task, i percorsi di salvataggio, la sessione Bluetooth sotto il suo lock e i percorsi chiamati dal pannello (e, in alcuni nodi, i codici HTTP o i glifi dei caratteri)

I test su host richiedono un qualsiasi compilatore C++17 (Linux, WSL, MSYS2); il pannello web è anche provato in un browser reale contro un nodo sostitutivo (`tools/panel_mock.mjs`, `tools/panel_browser_test.mjs`).

La maggior parte delle verifiche sono scansioni esaustive delle regole di manovra (`test_switch_set` e `test_interlock`: 375 036); contatori e contattori sono sostituti. `test_clock` stampa solo `ok`.""",
      "build": "`tools/build_node.sh` costruisce l'immagine nel container ESP-IDF 5.5.5 e la versione porta l'immagine, il suo SHA-256 e la sua firma Ed25519, una per scheda; l'immagine si scrive via USB-C la prima volta e poi si aggiorna dal pannello.",
      "troubleshooting": r"""| Vedi | Perché | Fai |
|---|---|---|
| Hai perso la password o il nodo non entra più in rete | Un nodo in configurazione senza indirizzo dopo 90 s apre un proprio Wi-Fi `ARMOR-SETUP-xxxxxx` (apri `http://192.168.4.1/`) | Per ricominciare tieni premuto BOOT per 8 secondi nei primi 30 secondi dopo l'accensione (cancella impostazioni e utenti), o usa *Ripristino di fabbrica* nel pannello |
| Un aggiornamento da GitHub è rifiutato | La versione non ha checksum o firma, non corrispondono (`e_no_checksum`, `e_no_signature`, `e_checksum_mismatch`, `e_bad_signature`), non ha un'immagine per questa scheda (`e_no_asset_for_board`) o è di un altro progetto (`e_wrong_firmware`) | Il nodo non è cambiato; riprova o lascia che un amministratore carichi il file a mano |
| Un interruttore mostra un guasto | Il contattore non ha mostrato aperto o chiuso come ordinato (`kDidNotOpen`, `kDidNotClose`); resta fino al riconoscimento | Controlla il cablaggio del contatto ausiliario, poi invia `acknowledge` |
| Un comando è rifiutato | La manovra è spenta (`switching_enabled` falso), il token non è valido o è scaduto, o il nodo non era armato poco prima | Arma di nuovo e invia l'ordine con il nuovo token |""",
      "structure": r"""<p align="center">
  <img src="images/repository-structure.svg" alt="Struttura del repository di ARMOR-NODE-ELECTRICAL" width="100%">
</p>

<details>
<summary>Versione testuale dell'albero</summary>

```text
ARMOR-NODE-ELECTRICAL/
├── main/                                il firmware: un componente ESP-IDF
├── core/                                la logica senza ESP-IDF, testata su un computer
├── panel/                               il pannello web incorporato nel firmware
├── tests/                               test su host e verifiche Python
├── docs/                                12 guide: sicurezza, manovra, messaggi, hardware
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

* I frame e le letture dei PZEM-004T v3 e PZEM-017 sono verificati contro i frame documentati e campioni registrati; nessun contatore ha ancora risposto.
* Le pagine dei contatori e delle letture del pannello web sono state provate in un browser contro un nodo simulato, non su una scheda.
* Nessuna scheda costruita e nessun contatore o contattore collegati: nulla ha ancora funzionato su apparecchiature reali.
* Il codice di configurazione, l'accesso con limite di password errate, il PIN Bluetooth e gli aggiornamenti firmati sono testati sull'host; non c'è stata una revisione indipendente.
* I controlli di hash e firma Ed25519 e la logica di ripristino passano sull'host; un aggiornamento via etere non è mai stato eseguito su una scheda.
* Le regole di manovra dei contattori sono provate solo contro contattori simulati; nulla qui ha ancora comandato qualcosa di reale.

**Prossimi passi**

* Provare i contatori, i contattori e le regole di manovra su un banco con una lampada e un trasformatore di isolamento, poi una scheda reale con l'aggiornamento via etere.""",
    },
  },
  "ja": {
    "tagline": "電気ノード：住宅の AC・DC ネットワークの電圧、電流、電力、エネルギーを読み取り、その開閉のルールを持ちます（PC でテスト済みのコアとビルドできるファームウェア。基板ではまだ動作していません）",
    "honest": "コア（PZEM-004T v3 と PZEM-017 メーターのフレーム、それらに問い合わせるバス、ノードのメッセージ、アナログ入力、切り替えのルール：19 のテストプログラムで 382,264 項目、うち 375,036 項目が切り替えルール）は代替メーターと接触器を使ってコンピューター上でテストされ、生成するメッセージは ARMOR-COMMON に受け付けられます。ノードのファームウェア（設定、シリアルライン、パネルのメーターと測定値のページ、Bluetooth、署名付きアップデート）は ESP-IDF 5.5.5 コンテナーで両方の基板向けにビルドできます。**基板上で動いたことはなく、メーターにも接触器にも何も接続されておらず、ここには何かを切り替えるものはありません。**",
    "glance": [
      [
        "役割",
        "電気フィールドノード：メーター、入力、開閉（ファミリー：Field Nodes、親：ARMOR-COMMON）",
      ],
      [
        "技術",
        "C++17, ESP-IDF 5.5.5, ESP32-S3",
      ],
      [
        "テスト",
        "382264 件の検査（ホスト用プログラム 19 本と Python 検査 5 個、`ctest`）",
      ],
      [
        "機器",
        "PZEM-004T v3 と PZEM-017 のメーター（最大 16）、アナログ入力、リレー。開閉は初期でオフ",
      ],
      [
        "動作環境",
        "ESP32-S3 基板（Ethernet または Wi-Fi）、ホストテストは任意のコンピューター",
      ],
      [
        "実機での確認",
        "まだありません：基板は未製作で、メーターも接触器も未接続。何も切り替えません",
      ],
      [
        "ライセンス",
        "GPL-3.0-or-later",
      ],
    ],
    "status": {
      "software": "ファームウェアは ESP-IDF 5.5.5 コンテナで両方のボード（Wi-Fi とイーサネット）向けにビルドできます。",
      "tests": "19 のホストプログラムで 382,264 件のチェックが通ります（`ctest`）。そのうち 375,036 件は切り替え規則です。メーターとコンタクターは模擬です。",
      "protocols": "PZEM-004T v3 と PZEM-017 のフレームと読み取り値は、文書化されたフレームと記録したサンプルに対して検証済みです。実際のメーターはまだ応答していません。",
      "ui": "Web パネルのメーターと読み取り値のページは、ブラウザーで模擬ノードに対して試しており、ボード上では試していません。",
      "hardware": "ボードは未製作で、メーターやコンタクターも接続していません。実機ではまだ何も動かしていません。",
      "security": "設定コード、誤ったパスワードの回数制限付きログイン、Bluetooth の PIN、署名付きアップデートはホストでテスト済みです。独立したレビューはまだありません。",
      "updates": "ハッシュと Ed25519 署名の確認、ロールバックの処理はホストで通ります。無線アップデートはボード上で一度も実行していません。",
      "writing": "コンタクターの切り替え規則は模擬のコンタクターに対してのみテストしています。実機を切り替えたことはまだありません。",
      "integration": "ノードのメッセージは ARMOR-COMMON の共有スキーマと適合ベクターに対して検証されています。MQTT クライアントはテストで本物の Mosquitto を相手に動かしていますが、ボードからサーバーへ送ったことはまだありません。",
      "docs": "8 言語、ファームウェアガイド、配線メモ、変更履歴は最新です。",
    },
    "docs": [
      "[安全](docs/SAFETY.md)と[開閉](docs/SWITCHING.md)：設計の前提と切替の流れ",
      "[メッセージ](docs/ELECTRICAL_MESSAGES.md)、[プロトコル](docs/PROTOCOLS.md)、[Zigbee](docs/ZIGBEE.md)",
      "[設計](docs/DESIGN.md)、[ハードウェア](docs/HARDWARE.md)、[ベース基板](docs/BASE_BOARD.md)、[ノードのファームウェア](docs/NODE_FIRMWARE.md)",
      "[ベンチテスト](docs/BENCH_TESTS.md)、[セットアップコード](docs/SETUP_CODE.md)、[Bluetooth プロビジョニング](docs/BLE_PROVISIONING.md)",
    ],
    "contributing_first": "Pull Request の前に `ctest --test-dir build/host` and `python -I tools/armor_ci_validate.py` を実行してください。通る必要があります。[CONTRIBUTING.md](CONTRIBUTING.md) と[行動規範](CODE_OF_CONDUCT.md)を参照してください。",
    "languages_extra": "",
    "body": {
      "overview": r"""* **電力量計の読み取り：** Peacefair の **PZEM-004T v3**（AC）と **PZEM-017**（DC）の Modbus RTU フレーム。CRC、レジスタを読む要求、応答の解読（電圧、電流、電力、エネルギー、周波数、力率、警報）。作るのは読み取り要求だけで、電力量計に書き込むもの（アドレス、しきい値、エネルギーのリセット）はどこにも作りません。合わない応答や、実際の電力量計が出せない値を含む応答は拒否します。
* **バス：** 複数の電力量計がつながる回線には 1 台ずつタイムアウト付きで問い合わせ、それぞれの最後の正常な読み取りを保持します。応答のない電力量計は 10 秒後に公開されなくなります。
* **メッセージ** `armor/electrical/<ノード>/state`：チャンネル（回路、線、系統入力、DC バス）ごとの項目に、AC/DC、電圧、電流、電力、エネルギー、周波数、力率、ノードが見ている開閉器の状態、警報を入れます。共有契約に含まれ、状態を運び、命令は運びません。
* **開閉のルール：** ハードウェアとは別に、2 つの電源の切り替えを制御するコントローラー。両方を同時に指令せず、開閉の許可、直前のノードの武装、デッドタイム中ずっと両接触器が開と確認されていることを要求し、指令どおりの状態を示さない接触器は確認応答まで残る故障として扱います。**開閉は初期設定でオフで、どのハードウェアも駆動しません。**
* **開閉器へのコマンド（有効化していません）：** 状態メッセージにはノードの開閉器の状態を載せることができ、共有コントラクトにはコマンド（`arm`、続いて 1 回限りのトークン付きの `close_a` または `close_b`、`open`、`acknowledge`）とノードの応答があります。コアは上記のルールでそれらを読み取り応答し、共有ベクターと模擬の接触器でテスト済みです。どのファームウェアイメージにも含まれていないため接触器を動かすことはできず、ARMOR-SERVER は有効化（`ARMOR_ELECTRICAL_SWITCHING=1`）され、かつブローカーの ACL が許可しない限りコマンドを送りません。
* **見える場所：** ARMOR-STUDIO の*電気設計*が住宅のネットワークを描き、各要素にそのチャンネルの計測値を表示します。ARMOR-SERVER が読み取り値、履歴、合計を保持します。
* **ノードのファームウェア**（Wi-Fi の ESP32-S3-WROOM-1 N16R8、またはケーブル接続の Waveshare ESP32-S3-ETH）：設定、最大 16 台の電力量計のための 1 本のシリアル回線、他のノードと同じ Web パネル（セットアップ、ユーザー、Wi-Fi、ブローカー、無線アップデート、HTTPS）に電力量計ページと測定値ページを加えたもの（8 言語）。読み取り専用で、開閉のルールは組み込まれていません。[ファームウェア](docs/NODE_FIRMWARE.md)を参照。
* **スマートフォンから Bluetooth で設定：** レーダーノードと同じチャンネルです。ARMOR アプリがノードを `ARMOR-XXXXXX` として見つけ、パネルのユーザーとセットアップコードを使って、名前、Wi-Fi、アドレス、ブローカー、Bluetooth モードを設定します（[プロトコル](docs/BLE_PROVISIONING.md)）。設定を変えない限り、ノードにユーザーがいない間だけ待ち受けます。無線部分は基板ではまだ動作していません。
* **署名付きの無線アップデート：**ノードが GitHub からインストールするのは、SHA-256 が一致し、管理者の有効な Ed25519 署名を持つイメージだけです（公開鍵はファームウェア内、秘密鍵は管理者の手元から出ません）。管理者がパネルで手動アップロードしたファイルは引き続き受け付けます。パネルのページとメッセージは 8 言語です。
* **PIN 付きの Bluetooth ペアリング：**6 桁の PIN は設定コードから導出され、USB コンソールに表示され、管理者にはパネルにも表示されます。スマートフォンはこれを入力して初めてノードの設定を書き込めます。
* **まだ：** 基板上で動作するファームウェア、ハードウェア、実際の設備での計測、そして開閉。
* **パネルを使えるのは家だけ：**パネルは既定でプライベートネットワーク（または所有者が指定した VPN などのネットワーク）にだけ応答し、保存する本人を締め出す一覧は拒否します。誤ったパスワードは人ごと・アドレスごとに数え、サーバーのプロキシの背後でも動くので、ノードを公開せずに家の外から使えます。
* **推定値はそう示されます：** 電流入力から作られたチャンネルには `power_estimated` が付き、Studio とサーバーはその電力を推定値（電流と公称電圧からの皮相電力）として表示し、それを含む系統値にも印を付けます。
* **ブローカーとの暗号化通信(TLS、任意):** 初期状態ではオフで、ノードはこれまでどおり暗号化なしの MQTT で通信します。ブローカーページのスイッチと、設備独自の認証局の証明書(PEM、最大 2 KB)の入力欄により、`mqtts://` で接続し、その認証局だけを信頼し、到達したアドレス向けに発行された証明書かを確認します。PEM 証明書 1 つでないものは拒否されます。ホストテストで検証済みで、ハンドシェイクはまだ基板では実行していません。
* **状態報告:** ノードは約 1 分ごとに、稼働時間と直前の再起動の理由、空きメモリ、回線と Wi-Fi 信号、ブローカーへの接続回数、最後に記録したエラーを公開します（`armor/health/<ノード>`、ARMOR-COMMON の `node_health` 契約）。作成するコードは全ノードで共有され、コンピューター上でテストされていますが、ボード上ではまだ動作していません。
* **サーバーからの制御：** Studio はノードをきれいに再起動し、最大 1 時間まで一時停止し（自動的に再開）、作業を待機にし（期限なし、再起動後も維持、ノードは接続したまま応答を続けます）、自分を表示させ、診断のスナップショットを求め、メンテナンス中として印を付けることができます（`armor/control/<ノード>/...`、ARMOR-COMMON の `node_control` 契約）。命令はすべて、その操作専用の使い捨てトークンによる 2 段階で、ブローカーに書き込めるのはサーバーだけです。工場出荷時リセットも消去もディープスリープもありません。一時停止中または待機中のノードは、誰が要求しても（パネル、ブローカー、セントラル）すべてのリレーを開いたままにして動かしません。電力量計の読み取りは続けます。 このコードは全ノードで共有され、コンピューター上でテスト済みですが、実機ではまだ動作していません。
* **鮮度を示す測定値：** 各メーターチャンネルには測定値の経過時間とメーターへの失敗したリクエスト数が付くため、サーバーは本当の0 Wと応答しなくなったメーターを区別できます。メータータスクが固まった場合はウォッチドッグがボードを再起動します。
* **ケーブルなしの診断：** 正常でない起動（クラッシュ、ウォッチドッグ、電源の電圧低下、メモリ確保の失敗）の後、ヘルスレポートが10分間その原因を伝えます。クラッシュするとコアダンプが残り、パネルから確認、ダウンロード、削除できます。保存された設定はファームウェアのインストールごとにコピーされ、更新で壊れた場合は復元されます。管理者はサーバー経由で、使い捨てトークンを使って、ノードに診断パッケージまたはログを要求できます。
* **リレーのインターロック：**リレーは、同時に閉じてはならない別のリレーを指定できます（1つの負荷の2系統の電源、モーターの正転と逆転など）。一方が閉じている間にもう一方を閉じる要求は、パネル、ブローカー、セントラルのいずれからでも拒否され、ノードがもう一方を勝手に開くことはありません。コンピューター上でテスト済みで、ボード上ではまだ動作していません。
* **メーター自身の設定の読み取り専用の確認:** 最初の正常な読み取りの後と `bus.check_settings_s` ごと(600 秒、0 = なし)に、測定と同じ巡回で PZEM のホールディングレジスタ(004T v3:電力のしきい値とアドレス、017:電圧のしきい値、アドレス、シャント)を読み、保存されたアドレスが使用中のものと違う場合は警告します。メーターには何も書き込みません。
* **保存された秘密情報の任意の封印:** 既定ではオフです(`security.seal_secrets`、またはサーバーの `nodes.nvs_encryption`)。オンにすると、ノードが保存するパスワード、トークン、鍵、PIN、パスワードのハッシュが ChaCha20-Poly1305 で封印され、それ以外は読めるままです。オン/オフの切り替えは何も失わずに書き直し、途中で止まっても大丈夫です。eFuse は焼かれず、フラッシュも暗号化されません。鍵は同じチップのパーティションにあるため、基板を手にした人に対する保護には**なりません**。このパーティションがない時期にインストールされたノードは、新しいパーティションテーブルで書き込むまで従来のままです。""",
      "role": r"""ARMOR-NODE-ELECTRICAL はメーターで家の AC・DC ネットワークを測定し、電源間の切り替えのルールを保持します。測定値を [ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER) に送ると、サーバーが履歴と日ごとのエネルギーを保持して警報を出し、[ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) の*電気*メニューと*電気デザイナー*、[ARMOR-ANDROID-CONTROL](https://github.com/JuanenRac/ARMOR-ANDROID-CONTROL) の電気画面が表示します。切り替えは設計済み（待機、1 回限りのトークン、インターロック、両方の接触器の確認）ですが、有効化はされていません。

| 名前 | 方法 | 用途 |
|---|---|---|
| ARMOR-SERVER | MQTT `armor/electrical/<id>/{state,command,result}` | チャンネルを受け取り、切り替えを命令する（開閉が 3 か所で有効なときのみ） |
| ARMOR-STUDIO | 電気メニュー、Electrical Designer | チャンネルとアラームを表示し、ノードのパネルを開く |
| ARMOR-ANDROID-CONTROL | Bluetooth | 現場でノードを設定し、チャンネルを表示 |
| ARMOR-COMMON | 電気のコントラクト | メッセージはそのスキーマで検証し、共通ファームウェアはここからコピー |""",
      "architecture": r"""<p align="center">
  <img src="images/architecture.svg" alt="ARMOR-NODE-ELECTRICAL のアーキテクチャ：呼び出し元、内部、依存先" width="100%">
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
| 基板上の危険な商用電源や直流 | ノードは PZEM モジュール（密閉型、絶縁されたシリアル線）を読むだけで、基板に商用電源を通しません。開閉する部分は別の段で、ランプと絶縁トランスを使ってベンチで試験します |
| 2 つの電源が同時に閉じる | 切替インターロックは両方を同時に命令しません。開閉が許可され、直前にノードがアームされ、デッドタイムの間ずっと両方の接触器が開と確認されている必要があります（`dead_time_ms` は既定 2000）。命令どおりの状態を示さない接触器は、確認応答するまで残る故障です（`kDidNotOpen`、`kDidNotClose`）。接触器間の機械的インターロックも引き続き必須です |
| 繰り返された命令、または誰も頼んでいない開閉 | `arm` が 64 ビットの使い捨てトークンを返し、`close_a` か `close_b` は `arm_window_ms` 内にそれを付ける必要があります。命令は保持されず、スイッチは最大 4 つ。開閉は、ファームウェアが許可し（`switching_enabled`）、サーバーが `ARMOR_ELECTRICAL_SWITCHING=1` で動き、ブローカーのアクセスリストがそのノードに開いていない限りオフです |
| 故障、フィードバックの喪失、開閉のオフ | 各コントローラーは故障・フィードバック喪失・開閉オフのとき、すべてのコイルを開いた状態で応答します（開が負荷にとって安全かどうかは設置側が判断）。メッセージの状態は命令ではなく補助接点が示すもの。リレーのペアはインターロックされ、ノードが勝手に相手を開くことはありません |
| 古い測定値が実測値として表示される | 応答しないメーターは 10 秒後に発行を止め、各チャンネルは測定値の古さと失敗した要求の数を持ちます。メーターのタスクが固まるとウォッチドッグで基板を再起動。`bus.check_settings_s`（600 秒、0 = なし）ごとにメーターの設定を読み取り（読み取りのみ）、アドレスが変わっていれば報告します |

商用電源（230 V AC）やバッテリーバンクの直流は命を奪い、火災を起こすことがあります。[docs/SAFETY.md](docs/SAFETY.md) は設計が前提とする事柄を述べたもので、設備の設計ではなく、その国の規則や有資格の施工者の代わりにはなりません。現時点では、ここにあるものは何も開閉しません。""",
      "interfaces": r"""| 部分 | 設定内容 |
|---|---|
| MQTT | `armor/electrical/<id>/state`（入力ごとに 1 チャンネル：AC または DC、電圧、電流、電力、エネルギー、周波数、力率、スイッチの状態、アラーム。ARMOR-COMMON のコントラクト）、`armor/electrical/<id>/command` と `/result`、`armor/device/<id>/<リレー>/{state,set}`、`armor/health/<id>`、`armor/control/<id>/...` |
| コマンド | `arm`、`close_a`、`close_b`（トークン付き）、`open`、`acknowledge`（故障を解除） |
| メーター | Peacefair PZEM-004T v3（AC）と PZEM-017（DC）を Modbus RTU で、1 本のシリアル線に最大 16 台。組み立てるのは読み取り要求だけで（アドレスやしきい値を書き込む要求は存在しません）、アナログ入力、接点、リレーはベース基板上、Zigbee ブリッジあり（[docs/ZIGBEE.md](docs/ZIGBEE.md)） |""",
      "configuration": r"""| 変数 | 既定値 | 設定内容 |
|---|---|---|
| `bus.check_settings_s` | 600 | メーター設定の読み取り専用チェックの間隔（秒、0 = なし） |
| `dead_time_ms`, `confirm_timeout_ms` | 2000 | 切替のデッドタイムと、接触器が命令どおりの状態を示すまでの猶予 |
| `switching_enabled` | off | この設定、サーバー（`ARMOR_ELECTRICAL_SWITCHING=1`）、ブローカーのアクセスリストのすべてが許可しない限り開閉はオフ |
| `CONFIG_ARMOR_NODE_ID`, `_SETUP_CODE`, `_FLEET_SECRET`, `_MQTT_*`, `_HEARTBEAT_S`, `_BLE_SETUP_MINUTES`, `_BOOT_FACTORY_RESET` | - | すべてのノードに共通する設定：名前（空なら `armor-` と MAC の下位バイト）、セットアップコード（空ならランダム）、フリートシークレット（16 文字以上、リポジトリには置かない）、最初のブローカー設定、ハートビート（2〜300 秒）、Bluetooth セットアップの分数（1〜120）、BOOT によるリセット（最初の 30 秒に 8 秒） |""",
      "quickstart": r"""**必要なもの:** ホストテスト用の C++17 コンパイラ、イメージのビルド用の ESP-IDF 5.5.5 コンテナ、ESP32-S3 基板（Ethernet または Wi-Fi）。

```bash
cmake -S tests -B build/host && cmake --build build/host && ctest --test-dir build/host   # host tests, -Werror
node tools/panel_mock.mjs --user admin:adminpass123   # the panel without a board
tools/build_node.sh generic s3-wifi                  # the image in the ESP-IDF container (or s3-eth)
```

See the [firmware guide](docs/NODE_FIRMWARE.md) and the [Bluetooth channel](docs/BLE_PROVISIONING.md).

[設計](docs/DESIGN.md)、[安全に関する注意](docs/SAFETY.md)、[開閉のルール](docs/SWITCHING.md)、[プロトコル](docs/PROTOCOLS.md)、[メッセージ](docs/ELECTRICAL_MESSAGES.md)を参照してください。""",
      "testing": r"""```bash
cmake -S tests -B build/host && cmake --build build/host && ctest --test-dir build/host
python -I tools/armor_ci_validate.py
```

ホスト用テストプログラム 19 個と Python の検査 5 個を `ctest` で実行します。ホストのプログラムが数えた検査は 382264 件で、`-Werror` でビルドします。

Python の検査：8 言語のパネル文言、タスク、保存パス、ロック下の Bluetooth セッション、パネルが呼ぶルート（ノードによっては HTTP コードやフォントのグリフも）

ホストテストには任意の C++17 コンパイラ（Linux、WSL、MSYS2）が必要です。Web パネルは代役ノード（`tools/panel_mock.mjs`、`tools/panel_browser_test.mjs`）を相手に実際のブラウザでも検証します。

検査の大半は開閉ルールの網羅的な総当たりです（`test_switch_set` と `test_interlock`：375 036）。メーターと接触器は代役です。`test_clock` は `ok` だけを出力します。""",
      "build": "`tools/build_node.sh` が ESP-IDF 5.5.5 コンテナでイメージをビルドし、リリースにはイメージ、その SHA-256 と Ed25519 署名が基板ごとに付きます。イメージは初回のみ USB-C で書き込み、その後はパネルから更新します。",
      "troubleshooting": r"""| 症状 | 原因 | 対処 |
|---|---|---|
| パスワードを忘れた、またはノードがネットワークに参加しない | セットアップ中でアドレスがないノードは 90 秒後に独自の Wi-Fi `ARMOR-SETUP-xxxxxx` を開きます（`http://192.168.4.1/` を開く） | 最初からやり直すには、電源投入後 30 秒以内に BOOT を 8 秒押し続ける（設定とユーザーを消去）か、パネルの*工場出荷状態に戻す*を使います |
| GitHub からの更新が拒否される | リリースにチェックサムや署名がない、一致しない（`e_no_checksum`、`e_no_signature`、`e_checksum_mismatch`、`e_bad_signature`）、この基板用のイメージがない（`e_no_asset_for_board`）、または別プロジェクトのもの（`e_wrong_firmware`） | ノードは変更されていません。再試行するか、管理者が手動でファイルをアップロード |
| スイッチが故障を示す | 接触器が命令どおりの開閉を示さなかった（`kDidNotOpen`、`kDidNotClose`）。確認応答するまで残ります | 補助接点の配線を確認してから `acknowledge` を送る |
| コマンドが拒否される | 開閉がオフ（`switching_enabled` が false）、トークンが無効か期限切れ、または直前にノードがアームされていない | もう一度アームして新しいトークンで命令を送る |""",
      "structure": r"""<p align="center">
  <img src="images/repository-structure.svg" alt="ARMOR-NODE-ELECTRICAL のリポジトリ構造" width="100%">
</p>

<details>
<summary>ツリーのテキスト版</summary>

```text
ARMOR-NODE-ELECTRICAL/
├── main/                                ファームウェア（ESP-IDF コンポーネント）
├── core/                                ESP-IDF なしのロジック（コンピューターでテスト）
├── panel/                               ファームウェアに埋め込まれた Web パネル
├── tests/                               ホストテストと Python 検査
├── docs/                                12 のガイド：安全、開閉、メッセージ、ハードウェア
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

* PZEM-004T v3 と PZEM-017 のフレームと読み取り値は、文書化されたフレームと記録したサンプルに対して検証済みです。実際のメーターはまだ応答していません。
* Web パネルのメーターと読み取り値のページは、ブラウザーで模擬ノードに対して試しており、ボード上では試していません。
* ボードは未製作で、メーターやコンタクターも接続していません。実機ではまだ何も動かしていません。
* 設定コード、誤ったパスワードの回数制限付きログイン、Bluetooth の PIN、署名付きアップデートはホストでテスト済みです。独立したレビューはまだありません。
* ハッシュと Ed25519 署名の確認、ロールバックの処理はホストで通ります。無線アップデートはボード上で一度も実行していません。
* コンタクターの切り替え規則は模擬のコンタクターに対してのみテストしています。実機を切り替えたことはまだありません。

**今後**

* ランプと絶縁トランスを使ったベンチでメーター、接触器、開閉ルールを試し、次に実際の基板で OTA 更新を試す。""",
    },
  },
  "zh": {
    "tagline": "电气节点：读取住宅交流和直流电网的电压、电流、功率和电能，并保存其开关规则（已在电脑上测试的核心和可编译的固件；尚未在电路板上运行过）",
    "honest": "核心（PZEM-004T v3 和 PZEM-017 电表的帧、轮询它们的总线、节点的消息、模拟输入和切换规则：19 个测试程序中的 382,264 项检查，其中 375,036 项针对切换规则）在计算机上用替身电表和接触器测试，它生成的消息被 ARMOR-COMMON 接受。节点固件（设置、串行线路、面板的电表和读数页面、蓝牙、签名更新）可在 ESP-IDF 5.5.5 容器中为两种板子构建。**它从未在板上运行，没有连接任何电表或接触器，这里的任何东西都不会切换任何设备。**",
    "glance": [
      [
        "角色",
        "电气现场节点：电表、输入和开关操作（家族：Field Nodes，上级：ARMOR-COMMON）",
      ],
      [
        "技术栈",
        "C++17, ESP-IDF 5.5.5, ESP32-S3",
      ],
      [
        "测试",
        "382264 项检查（19 个主机程序和 5 项 Python 检查，`ctest`）",
      ],
      [
        "设备",
        "PZEM-004T v3 和 PZEM-017 电表（最多 16 台）、模拟输入、继电器；开关操作默认关闭",
      ],
      [
        "运行位置",
        "ESP32-S3 电路板（以太网或 Wi-Fi）；主机测试可在任何计算机上运行",
      ],
      [
        "真实硬件",
        "暂无：没有制作板子，也没有连接电表或接触器；不会切换任何设备",
      ],
      [
        "许可证",
        "GPL-3.0-or-later",
      ],
    ],
    "status": {
      "software": "固件可在 ESP-IDF 5.5.5 容器中为两块板（Wi-Fi 和以太网）构建。",
      "tests": "19 个主机程序中的 382,264 项检查通过（`ctest`），其中 375,036 项针对切换规则；电表和接触器均为模拟。",
      "protocols": "PZEM-004T v3 和 PZEM-017 的帧与读数已对照文档中的帧和录制的样本检查；目前还没有电表响应过。",
      "ui": "网页面板的电表和读数页面已在浏览器中对模拟节点测试过，尚未在板子上测试。",
      "hardware": "尚未制作板子，也没有连接电表或接触器：还没有在真实设备上运行过。",
      "security": "设置码、限制错误密码次数的登录、蓝牙 PIN 和签名更新已在主机上测试；没有经过独立审查。",
      "updates": "哈希和 Ed25519 签名检查以及回滚逻辑在主机上通过；空中更新从未在板子上运行过。",
      "writing": "切换接触器的规则只对照模拟接触器测试过；这里还没有切换过任何真实设备。",
      "integration": "节点的消息已对照 ARMOR-COMMON 的共享模式和一致性向量验证。其 MQTT 客户端在测试中与真实的 Mosquitto 对接；还没有任何板子把这些消息发到服务器。",
      "docs": "八种语言、固件指南、接线说明和更新日志均为最新。",
    },
    "docs": [
      "[安全](docs/SAFETY.md)和[开关操作](docs/SWITCHING.md)：设计的假设以及转换如何进行",
      "[消息](docs/ELECTRICAL_MESSAGES.md)、[协议](docs/PROTOCOLS.md)和 [Zigbee](docs/ZIGBEE.md)",
      "[设计](docs/DESIGN.md)、[硬件](docs/HARDWARE.md)、[底板](docs/BASE_BOARD.md)和[节点固件](docs/NODE_FIRMWARE.md)",
      "[台架测试](docs/BENCH_TESTS.md)、[设置码](docs/SETUP_CODE.md)和[蓝牙配置](docs/BLE_PROVISIONING.md)",
    ],
    "contributing_first": "提交 Pull Request 之前请运行 `ctest --test-dir build/host` and `python -I tools/armor_ci_validate.py`：必须通过。参见 [CONTRIBUTING.md](CONTRIBUTING.md) 和[行为准则](CODE_OF_CONDUCT.md)。",
    "languages_extra": "",
    "body": {
      "overview": r"""* **读取电表：** Peacefair **PZEM-004T v3**（交流）和 **PZEM-017**（直流）的 Modbus RTU 帧：CRC、读寄存器的请求以及应答的解码（电压、电流、功率、电能、频率、功率因数、报警）。只构造读请求：向电表写入的请求（地址、阈值、电能清零）在任何地方都不构造。不匹配的应答，或包含任何真实电表都给不出的数值的应答，会被拒绝。
* **总线：** 带多个电表的线路逐个轮询并带超时；保留每个电表最后一次正常读数，静默的电表在十秒后不再发布。
* **消息** `armor/electrical/<节点>/state`：每个通道（一条回路、一条线路、电网入口、一条直流母线）一项，含交流或直流、电压、电流、功率、电能、频率、功率因数、节点所见的开关状态和报警；它属于共享契约，只带状态，绝不带命令。
* **开关规则，** 与任何硬件无关：两个电源之间转换的控制器，绝不同时指令两者，要求开关操作被允许、节点在刚才已布防、两个接触器在整个死区时间内都被确认断开，并把没有显示所指令状态的接触器当作故障，直到被确认才消除。**开关默认关闭，没有任何硬件被驱动。**
* **对开关的命令（未启用）：** 状态消息可以携带节点各开关的状态，共享契约中有一条命令（`arm`，然后带一次性令牌的 `close_a` 或 `close_b`、`open`、`acknowledge`）以及节点的应答；核心按上述规则读取并应答，已用共享向量和模拟接触器测试。没有任何固件镜像包含它，因此不能驱动任何接触器；除非已启用（`ARMOR_ELECTRICAL_SWITCHING=1`）且代理的 ACL 允许，ARMOR-SERVER 不会发送命令。
* **在哪里显示：** ARMOR-STUDIO 的*电气设计器*绘制住宅的电网，并在每个元件上显示其通道的测量值；ARMOR-SERVER 保存读数、历史和合计。
* **节点固件**（Wi-Fi 的 ESP32-S3-WROOM-1 N16R8，或有线的 Waveshare ESP32-S3-ETH）：设置、供最多十六块电表使用的一条串口线路，以及与其他节点相同的网页面板（设置、用户、Wi-Fi、代理、无线更新、HTTPS），另有自己的电表页和读数页（八种语言）。只读取：开关规则没有链接进去。参见[固件](docs/NODE_FIRMWARE.md)。
* **通过蓝牙用手机配置：** 与雷达节点相同的通道。ARMOR 应用会以 `ARMOR-XXXXXX` 找到节点，并使用面板的用户和设置码来设置其名称、Wi-Fi、地址、代理和蓝牙模式（[协议](docs/BLE_PROVISIONING.md)）。除非另行设置，它只在节点还没有用户时监听。无线部分从未在电路板上运行过。
* **签名的无线更新：**节点只会从 GitHub 安装 SHA-256 匹配且带有维护者有效 Ed25519 签名的镜像（公钥在固件中，私钥从不离开维护者）；管理员在面板中手动上传的文件仍然被接受。面板的页面和消息有八种语言。
* **带 PIN 的蓝牙配对：**六位 PIN 由设置码派生，打印在 USB 控制台上并向管理员显示在面板中；手机必须输入它才能写入节点的设置。
* **尚未完成：** 在电路板上运行的固件、硬件、对真实设施的任何测量以及任何开关操作。
* **只有家中才能使用面板：**面板默认只响应私有网络（或所有者列出的网络，如 VPN），拒绝会把保存者自己挡在外面的列表，按人和按地址统计错误密码，并可在服务器代理之后工作，从而无需公开节点就能在家外访问。
* **估算值会标明：** 由电流输入生成的通道带有 `power_estimated`，Studio 和服务器会把它的功率显示为估算值（由电流和额定电压得出的视在功率），并标记包含它的电网数值。
* **可选的与代理加密连接(TLS):** 默认关闭,因此节点仍像以前一样使用未加密的 MQTT。代理页面中的一个开关和一个用于填写本安装自有证书颁发机构证书(PEM,最大 2 KB)的框,会让节点用 `mqtts://` 连接、只信任该机构,并检查代理证书是否为其所到达的地址而签发;不是单个 PEM 证书的内容会被拒绝。已有主机测试覆盖;握手尚未在电路板上运行。
* **健康报告：** 节点大约每分钟发布一次：已运行多久、上次为何重启、可用内存、连接与 Wi-Fi 信号、连接代理的次数以及记录的最后一个错误（`armor/health/<节点>`，即 ARMOR-COMMON 的 `node_health` 契约）。生成它的代码由所有节点共享并在计算机上测试；尚未在开发板上运行。
* **由服务器控制：** Studio 可以干净地重启节点、将其暂停至多一小时（自动恢复）、让其工作进入待机（无期限，重启后仍保持，节点保持连接并继续应答）、让它显示自己、请求诊断快照，并把它标记为维护中（`armor/control/<节点>/...`，ARMOR-COMMON 的 `node_control` 契约）。每条命令分两步，使用只属于该操作的一次性令牌，只有服务器可以在代理上写入，并且没有恢复出厂设置、擦除或深度睡眠。节点处于暂停或待机时，所有继电器保持断开，无论谁请求（面板、代理或中央）都不会动作；电表仍继续读取。 该代码由所有节点共用，并已在计算机上测试；尚未在电路板上运行过。
* **说明自身新鲜度的读数：** 每个电表通道都带有其读数的时间和对该电表失败的请求次数，因此服务器能区分真实的 0 W 与已停止应答的电表；电表任务卡死时，看门狗会重启电路板。
* **无需线缆的诊断：** 在一次不干净的启动之后（崩溃、看门狗、电源跌落、内存分配失败），健康报告会在十分钟内说明原因；崩溃会留下核心转储（core dump），可在面板中查看、下载或删除；已保存的设置会在每次固件安装前被复制，并在更新损坏它们时恢复；管理员还可以通过服务器，用一次性令牌向节点索取诊断包或其日志。
* **继电器互锁：**一个继电器可以指定另一个绝不能同时闭合的继电器（同一负载的两路电源、电机的两个转向）；在另一个闭合时要求闭合此继电器，无论来自面板、broker 还是中心，都会被拒绝，节点也绝不会自行断开另一个。已在计算机上测试；尚未在开发板上运行。
* **只读方式读取电表自身的设置:** 在第一次成功读数之后,以及每隔 `bus.check_settings_s`(600 秒,0 = 从不),节点会在读取测量值的同一轮中读取 PZEM 的保持寄存器(004T v3:功率阈值和地址;017:电压阈值、地址和分流器),并在保存的地址与所用地址不一致时发出警告;不会向电表写入任何内容。
* **可选的已存储机密封存:** 默认关闭(`security.seal_secrets`,或服务器的 `nodes.nvs_encryption`)。开启后,节点保存的密码、令牌、密钥、PIN 和密码哈希会用 ChaCha20-Poly1305 封存,其余内容仍可读取;开启或关闭时会无损重写,即使节点中途停止也不会丢失。不会烧写 eFuse,闪存也不加密:密钥在同一芯片的一个分区中,因此**不能**防范持有电路板的人;在该分区出现之前安装的节点会保持原样,直到用新的分区表重新烧录。""",
      "role": r"""ARMOR-NODE-ELECTRICAL 通过电表测量住宅的交流和直流网络，并保存在电源之间切换的规则。它把读数发布给 [ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER)，由后者保存历史和每日能量并触发报警；[ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) 的*电气*菜单和*电气设计器*以及 [ARMOR-ANDROID-CONTROL](https://github.com/JuanenRac/ARMOR-ANDROID-CONTROL) 的电气界面显示这些内容。切换已经设计好（预备、一次性令牌、互锁、两个接触器的确认）但未启用。

| 名称 | 方式 | 用途 |
|---|---|---|
| ARMOR-SERVER | MQTT `armor/electrical/<id>/{state,command,result}` | 接收通道并下达转换命令（仅当三处都开启开关操作时） |
| ARMOR-STUDIO | 电气菜单、Electrical Designer | 显示通道和报警并打开节点面板 |
| ARMOR-ANDROID-CONTROL | Bluetooth | 在现场设置节点并显示通道 |
| ARMOR-COMMON | 电气合约 | 消息按其模式校验；公共固件由此复制 |""",
      "architecture": r"""<p align="center">
  <img src="images/architecture.svg" alt="ARMOR-NODE-ELECTRICAL 的架构：谁调用它、它包含什么、它依赖什么" width="100%">
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
| 电路板上的危险市电或直流电 | 节点只读取 PZEM 模块（封闭模块，串口线已隔离），电路板上从不带市电；负责开关的是单独的一级，在台架上用灯泡和隔离变压器测试 |
| 两个电源同时闭合 | 转换互锁从不同时命令两者：需要允许开关操作、节点刚刚布防，并且在整个死区时间内两个接触器都确认为断开（`dead_time_ms` 默认 2000）；未显示所命令状态的接触器是持续到被确认的故障（`kDidNotOpen`、`kDidNotClose`）；接触器之间仍必须有机械互锁 |
| 被重放的命令，或没人要求的开关操作 | `arm` 返回一个 64 位一次性令牌，`close_a` 或 `close_b` 必须在 `arm_window_ms` 内携带它；命令从不被保留；最多 4 个开关；除非固件允许（`switching_enabled`）、服务器以 `ARMOR_ELECTRICAL_SWITCHING=1` 运行且代理的访问列表对该节点开放，否则开关操作处于关闭状态 |
| 故障、反馈丢失或开关操作关闭 | 每个控制器在故障、反馈丢失或开关操作关闭时都以所有线圈断开作答（故障即断开；断开对负载是否安全由安装方决定）；消息中的状态是辅助触点显示的状态，而不是被命令的状态；继电器对相互联锁，节点从不自行断开其搭档 |
| 过期读数被当作真实值显示 | 无响应的电表在 10 秒后不再发布；每个通道带有读数的时效和失败请求次数；电表任务卡死会由看门狗重启电路板；每隔 `bus.check_settings_s`（600 秒，0 = 从不）读取电表设置（只读），若地址变化则报告 |

市电（230 V 交流）和电池组的直流电可能致命并引发火灾。[docs/SAFETY.md](docs/SAFETY.md) 说明了设计的假设；它不是安装设计，也不能取代所在国家的法规或合格的安装人员。目前这里的一切都不会控制任何开关。""",
      "interfaces": r"""| 部分 | 作用 |
|---|---|
| MQTT | `armor/electrical/<id>/state`（每路输入一个通道：交流或直流、电压、电流、功率、电能、频率、功率因数、开关状态、报警；ARMOR-COMMON 合约）、`armor/electrical/<id>/command` 和 `/result`、`armor/device/<id>/<继电器>/{state,set}`、`armor/health/<id>`、`armor/control/<id>/...` |
| 命令 | `arm`、`close_a`、`close_b`（带令牌）、`open` 和 `acknowledge`（清除故障） |
| 电表 | Peacefair PZEM-004T v3（交流）和 PZEM-017（直流），通过 Modbus RTU，一条串口线上最多 16 台；只会构造读取请求（写地址或阈值的请求根本不存在）；模拟输入、触点和继电器在底板上；还有 Zigbee 桥（[docs/ZIGBEE.md](docs/ZIGBEE.md)） |""",
      "configuration": r"""| 变量 | 默认值 | 作用 |
|---|---|---|
| `bus.check_settings_s` | 600 | 电表设置只读检查之间的秒数（0 = 从不） |
| `dead_time_ms`, `confirm_timeout_ms` | 2000 | 转换的死区时间以及接触器显示所命令状态的时限 |
| `switching_enabled` | off | 除非此设置、服务器（`ARMOR_ELECTRICAL_SWITCHING=1`）和代理的访问列表都允许，否则开关操作为关闭 |
| `CONFIG_ARMOR_NODE_ID`, `_SETUP_CODE`, `_FLEET_SECRET`, `_MQTT_*`, `_HEARTBEAT_S`, `_BLE_SETUP_MINUTES`, `_BOOT_FACTORY_RESET` | - | 所有节点共有的设置：名称（为空则为 `armor-` 加 MAC 的最后字节）、设置码（为空则随机）、机群密钥（16 个字符以上，绝不放入仓库）、最初的代理设置、心跳（2 到 300 秒）、蓝牙设置的分钟数（1 到 120）以及用 BOOT 重置（前 30 秒内按 8 秒） |""",
      "quickstart": r"""**要求:** 用于主机测试的 C++17 编译器；用于构建镜像的 ESP-IDF 5.5.5 容器；ESP32-S3 电路板（以太网或 Wi-Fi）。

```bash
cmake -S tests -B build/host && cmake --build build/host && ctest --test-dir build/host   # host tests, -Werror
node tools/panel_mock.mjs --user admin:adminpass123   # the panel without a board
tools/build_node.sh generic s3-wifi                  # the image in the ESP-IDF container (or s3-eth)
```

See the [firmware guide](docs/NODE_FIRMWARE.md) and the [Bluetooth channel](docs/BLE_PROVISIONING.md).

参见[设计](docs/DESIGN.md)、[安全说明](docs/SAFETY.md)、[开关规则](docs/SWITCHING.md)、[协议](docs/PROTOCOLS.md)和[消息](docs/ELECTRICAL_MESSAGES.md)。""",
      "testing": r"""```bash
cmake -S tests -B build/host && cmake --build build/host && ctest --test-dir build/host
python -I tools/armor_ci_validate.py
```

`ctest` 运行 19 个主机测试程序和 5 个 Python 检查；主机程序统计的检查共 382264 项，使用 `-Werror` 构建。

Python 检查：八种语言的面板文字、任务、保存路径、受锁保护的蓝牙会话以及面板调用的路由（部分节点还包括 HTTP 状态码或字体字形）

主机测试需要任意 C++17 编译器（Linux、WSL、MSYS2）；网页面板还会在真实浏览器中对着模拟节点（`tools/panel_mock.mjs`、`tools/panel_browser_test.mjs`）进行验证。

大部分检查是对开关规则的穷举遍历（`test_switch_set` 和 `test_interlock`：375 036）；电表和接触器是替身。`test_clock` 只输出 `ok`。""",
      "build": "`tools/build_node.sh` 在 ESP-IDF 5.5.5 容器中构建镜像，发布版带有镜像、其 SHA-256 和 Ed25519 签名，每块电路板一份；镜像第一次通过 USB-C 写入，之后从面板更新。",
      "troubleshooting": r"""| 现象 | 原因 | 处理 |
|---|---|---|
| 忘记了密码，或节点不再加入网络 | 处于设置状态且 90 秒后仍无地址的节点会开启自己的 Wi-Fi `ARMOR-SETUP-xxxxxx`（打开 `http://192.168.4.1/`） | 要重新开始，请在上电后 30 秒内按住 BOOT 8 秒（会清除设置和用户），或使用面板中的*恢复出厂设置* |
| 来自 GitHub 的更新被拒绝 | 发布版缺少校验和或签名，或二者不匹配（`e_no_checksum`、`e_no_signature`、`e_checksum_mismatch`、`e_bad_signature`），没有适用于此电路板的镜像（`e_no_asset_for_board`），或属于另一个项目（`e_wrong_firmware`） | 节点未发生任何变化；请重试，或由管理员手动上传文件 |
| 开关显示故障 | 接触器没有按命令显示断开或闭合（`kDidNotOpen`、`kDidNotClose`）；会保持到被确认 | 检查辅助触点的接线，然后发送 `acknowledge` |
| 命令被拒绝 | 开关操作已关闭（`switching_enabled` 为 false）、令牌无效或已过期，或节点刚才没有布防 | 重新布防并用新令牌发送命令 |""",
      "structure": r"""<p align="center">
  <img src="images/repository-structure.svg" alt="ARMOR-NODE-ELECTRICAL 的仓库结构" width="100%">
</p>

<details>
<summary>目录树的文本版</summary>

```text
ARMOR-NODE-ELECTRICAL/
├── main/                                固件：一个 ESP-IDF 组件
├── core/                                不依赖 ESP-IDF 的逻辑，在计算机上测试
├── panel/                               嵌入固件的网页面板
├── tests/                               主机测试和 Python 检查
├── docs/                                12 份指南：安全、开关、消息、硬件
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

* PZEM-004T v3 和 PZEM-017 的帧与读数已对照文档中的帧和录制的样本检查；目前还没有电表响应过。
* 网页面板的电表和读数页面已在浏览器中对模拟节点测试过，尚未在板子上测试。
* 尚未制作板子，也没有连接电表或接触器：还没有在真实设备上运行过。
* 设置码、限制错误密码次数的登录、蓝牙 PIN 和签名更新已在主机上测试；没有经过独立审查。
* 哈希和 Ed25519 签名检查以及回滚逻辑在主机上通过；空中更新从未在板子上运行过。
* 切换接触器的规则只对照模拟接触器测试过；这里还没有切换过任何真实设备。

**下一步**

* 在带灯泡和隔离变压器的台架上试验电表、接触器和开关规则，然后在真实电路板上试验空中更新。""",
    },
  },
  "pt": {
    "tagline": "Nó elétrico: lê as tensões, correntes, potência e energia da rede AC e DC da casa e guarda as regras para a comutar (núcleo testado em anfitrião e um firmware que compila; nunca correu numa placa)",
    "honest": "O núcleo (as tramas dos contadores PZEM-004T v3 e PZEM-017, o barramento que os interroga, a mensagem do nó, as entradas analógicas e as regras de comutação: 376 195 verificações em 11 programas de teste, 375 008 delas sobre as regras de comutação) é testado num computador com contadores e contactores de substituição, e as mensagens que produz são aceites pelo ARMOR-COMMON. O firmware do nó (as definições, a linha série, as páginas Contadores e Leituras do seu painel, Bluetooth, atualizações assinadas) compila no contentor ESP-IDF 5.5.5 para as duas placas. **Nunca correu numa placa, nada foi ligado a um contador nem a um contactor, e nada aqui comuta coisa alguma.**",
    "glance": [
      [
        "Função",
        "Nó de campo elétrico: contadores, entradas e manobra (família: Field Nodes, pai: ARMOR-COMMON)",
      ],
      [
        "Tecnologia",
        "C++17, ESP-IDF 5.5.5, ESP32-S3",
      ],
      [
        "Testes",
        "382264 verificações em 19 programas de anfitrião e 5 em Python (`ctest`)",
      ],
      [
        "Equipamentos",
        "Contadores PZEM-004T v3 e PZEM-017 (até 16), entradas analógicas, relés; manobra desligada por omissão",
      ],
      [
        "Funciona em",
        "Uma placa ESP32-S3 (Ethernet ou Wi-Fi); testes de anfitrião em qualquer computador",
      ],
      [
        "Em hardware real",
        "Nenhum ainda: nenhuma placa montada nem contador ou contactor ligados; nada comuta coisa alguma",
      ],
      [
        "Licença",
        "GPL-3.0-or-later",
      ],
    ],
    "status": {
      "software": "O firmware compila no contentor ESP-IDF 5.5.5 para as duas placas (Wi-Fi e Ethernet).",
      "tests": "Passam 382.264 verificações em 19 programas de anfitrião (`ctest`), 375.036 delas sobre as regras de manobra; os contadores e contactores são simulações.",
      "protocols": "As tramas e leituras dos PZEM-004T v3 e PZEM-017 são verificadas contra as tramas documentadas e amostras gravadas; nenhum contador respondeu ainda.",
      "ui": "As páginas de contadores e leituras do painel web foram exercitadas num navegador contra um nó simulado, não numa placa.",
      "hardware": "Nenhuma placa construída nem contador ou contactor ligados: nada funcionou ainda em equipamentos reais.",
      "security": "O código de configuração, o acesso com limite de palavras-passe erradas, o PIN Bluetooth e as atualizações assinadas estão testados no anfitrião; não houve revisão independente.",
      "updates": "As verificações de hash e de assinatura Ed25519 e a lógica de retrocesso passam no anfitrião; uma atualização pelo ar nunca foi executada numa placa.",
      "writing": "As regras para manobrar contactores só foram testadas contra contactores simulados; nada aqui manobrou ainda nada real.",
      "integration": "As mensagens do nó são validadas contra os esquemas partilhados e os vetores de conformidade do ARMOR-COMMON. O seu cliente MQTT é exercitado contra um Mosquitto real nos testes; nenhuma placa os enviou ainda a um servidor.",
      "docs": "Oito idiomas, o guia do firmware, as notas de cablagem e o registo de alterações estão atualizados.",
    },
    "docs": [
      "[Segurança](docs/SAFETY.md) e [manobra](docs/SWITCHING.md): o que o desenho pressupõe e como decorre uma transferência",
      "[Mensagens](docs/ELECTRICAL_MESSAGES.md), [protocolos](docs/PROTOCOLS.md) e [Zigbee](docs/ZIGBEE.md)",
      "[Desenho](docs/DESIGN.md), [hardware](docs/HARDWARE.md), [placa base](docs/BASE_BOARD.md) e [firmware do nó](docs/NODE_FIRMWARE.md)",
      "[Testes de bancada](docs/BENCH_TESTS.md), [código de configuração](docs/SETUP_CODE.md) e [provisionamento Bluetooth](docs/BLE_PROVISIONING.md)",
    ],
    "contributing_first": "Antes de um pull request, execute `ctest --test-dir build/host` and `python -I tools/armor_ci_validate.py`: tem de passar. Consulte [CONTRIBUTING.md](CONTRIBUTING.md) e o [código de conduta](CODE_OF_CONDUCT.md).",
    "languages_extra": "",
    "body": {
      "overview": r"""* **Ler os contadores:** as tramas Modbus RTU dos **PZEM-004T v3** (AC) e **PZEM-017** (DC) da Peacefair: o CRC, o pedido que lê os registos e a descodificação da resposta (tensão, corrente, potência, energia, frequência, fator de potência, alarme). Só se constrói o pedido de leitura: os que escrevem num contador (o seu endereço, os seus limiares, a reposição da sua energia) não se constroem em lado nenhum. Uma resposta que não encaixa, ou que traz um valor que nenhum contador real poderia dar, recusa-se.
* **O barramento:** uma linha com vários contadores consulta-se um de cada vez, com um limite de tempo; guarda-se a última boa leitura de cada um e um contador que fica em silêncio deixa de se publicar após dez segundos.
* **A mensagem** `armor/electrical/<node>/state`: uma entrada por canal (um circuito, uma linha, a entrada da rede, um barramento DC) com AC ou DC, tensão, corrente, potência, energia, frequência, fator de potência, o estado de um interruptor como o nó o vê e um alarme; está no contrato partilhado e leva um estado, nunca um comando.
* **As regras de comutação,** à parte de qualquer hardware: um controlador para a transferência entre duas fontes que nunca comanda as duas, precisa de a comutação estar permitida, do nó armado mesmo antes, de ambos os contactores confirmados abertos durante todo o tempo morto, e converte um contactor que não mostra o que lhe foi dito numa avaria que fica até ser reconhecida. **A comutação está desativada por omissão e nada aciona hardware algum.**
* **Os comandos a um interruptor, não ativados:** a mensagem de estado pode levar o estado dos interruptores do nó, e o contrato partilhado tem um comando (`arm`, depois `close_a` ou `close_b` com um token de uso único, `open`, `acknowledge`) e a resposta do nó; o núcleo lê-os e responde-lhes com as regras acima, testado contra os vetores partilhados e com contactores substitutos. Nenhuma imagem de firmware o inclui, por isso nada pode acionar um contactor, e o ARMOR-SERVER recusa enviar um comando a menos que se ligue (`ARMOR_ELECTRICAL_SWITCHING=1`) e a ACL do broker o permita.
* **Onde se mostra:** o *Desenhador elétrico* do ARMOR-STUDIO desenha a rede da casa e mostra em cada elemento o que o seu canal mede; o ARMOR-SERVER guarda as leituras, o seu histórico e as somas.
* **O firmware do nó** (ESP32-S3-WROOM-1 N16R8 em Wi-Fi, ou a Waveshare ESP32-S3-ETH no seu cabo): as definições, uma linha série para até dezasseis contadores e o painel web dos outros nós (configuração, utilizadores, Wi-Fi, broker, atualização pelo ar, HTTPS) com as suas próprias páginas Contadores e Leituras, em oito idiomas. Só lê: as regras de comutação não estão ligadas nele. Veja [o firmware](docs/NODE_FIRMWARE.md).
* **Configuração a partir de um telemóvel por Bluetooth,** o mesmo canal que o do nó de radar: a aplicação ARMOR encontra o nó como `ARMOR-XXXXXX` e define o seu nome, Wi-Fi, endereço, broker e modo Bluetooth com os utilizadores do painel e o código de configuração ([o protocolo](docs/BLE_PROVISIONING.md)). Só escuta enquanto o nó não tem utilizador, a menos que se diga o contrário. O lado de rádio nunca correu numa placa.
* **Atualizações pelo ar assinadas:** o nó só instala do GitHub uma imagem cujo SHA-256 coincide e que leva uma assinatura Ed25519 válida do responsável (a chave pública está no firmware, a privada nunca sai do responsável); um ficheiro carregado à mão por um administrador no painel continua a ser aceite. As páginas e mensagens do painel estão em oito idiomas.
* **Emparelhamento Bluetooth com PIN:** o PIN de seis dígitos deriva do código de configuração, é impresso na consola USB e mostrado a um administrador no painel; o telemóvel tem de o introduzir antes de poder escrever as definições do nó.
* **Ainda não:** o firmware a correr numa placa, o hardware, qualquer medição de uma instalação real e qualquer comutação.
* **Só a casa pode usar o painel:** o painel responde por omissão à rede privada (ou às redes que o dono indicar, como uma VPN), recusa uma lista que deixaria de fora quem a guarda, conta as palavras-passe erradas por pessoa e por endereço e funciona atrás do proxy do servidor para ser alcançado de fora de casa sem publicar o nó.
* **As estimativas dizem-no:** um canal feito a partir de uma entrada de corrente leva `power_estimated`, por isso o Studio e o servidor mostram a sua potência como estimada (potência aparente a partir de uma corrente e uma tensão nominal) e marcam um valor de rede que inclua uma.
* **Ligação cifrada opcional ao broker (TLS):** desativada por predefinição, por isso o nó fala MQTT sem cifra como antes. Um interruptor e uma caixa para o certificado da autoridade própria da instalação (PEM, no máximo 2 KB) na página Broker fazem-no ligar-se com `mqtts://`, confiar só nessa autoridade e verificar que o certificado do broker foi feito para o endereço alcançado; o que não for um único certificado PEM é recusado. Coberto por testes no computador; o handshake ainda não foi executado numa placa.
* **Relatório de saúde:** cerca de uma vez por minuto o nó publica há quanto tempo está ligado e porque reiniciou da última vez, a memória livre, a ligação e o sinal Wi-Fi, quantas vezes se ligou ao broker e o último erro que registou (`armor/health/<nó>`, o contrato `node_health` do ARMOR-COMMON). O código que o constrói é partilhado por todos os nós e testado num computador; nunca correu numa placa.
* **Controlo a partir do servidor:** o Studio pode reiniciar o nó de forma limpa, pô-lo em pausa até uma hora (retoma sozinho), pôr o seu trabalho em espera (sem fim, mantida nos reinícios, o nó continua ligado e a responder), fazê-lo mostrar-se, pedir um instantâneo de diagnóstico e marcá-lo em manutenção (`armor/control/<nó>/...`, o contrato `node_control` do ARMOR-COMMON). Cada ordem tem dois passos com um token de uso único que pertence a essa operação, só o servidor as pode escrever no broker, e não existe reposição de fábrica, apagamento nem sono profundo. Enquanto o nó está em pausa ou em espera, todos os relés ficam abertos e nenhum se move, peça quem pedir (o painel, o broker ou uma central); os contadores continuam a ser lidos. O código é partilhado por todos os nós e testado num computador; ainda não correu numa placa.
* **Leituras que dizem quão frescas são:** cada canal de contador leva a idade da sua leitura e quantos pedidos ao contador falharam, pelo que o servidor distingue um 0 W real de um contador que deixou de responder; e uma tarefa de contadores bloqueada reinicia a placa através do watchdog.
* **Diagnóstico sem cabo:** depois de um arranque que não foi limpo (um bloqueio, um watchdog, uma quebra de alimentação, uma reserva de memória falhada), o relatório de saúde diz o motivo durante dez minutos; uma falha deixa o seu core dump para ver, descarregar ou apagar a partir do painel; as definições guardadas são copiadas antes de cada instalação de firmware e recuperadas se uma atualização as danificar; e um administrador pode pedir ao nó, através do servidor, um pacote de diagnóstico ou o seu registo com um token de utilização única.
* **Intertravamento de relés:** um relé pode indicar outro que nunca deve estar fechado ao mesmo tempo (as duas fontes de uma carga, os dois sentidos de um motor); pedir para fechar um enquanto o outro está fechado é recusado, venha do painel, do broker ou da central, e o nó nunca abre o outro por si. Testado num computador; não executado numa placa.
* **Leitura, apenas de leitura, das definições próprias dos contadores:** após a primeira leitura boa e a cada `bus.check_settings_s` (600 s, 0 = nunca) o nó lê os registos holding do PZEM (004T v3: limiar de potência e endereço; 017: limiares de tensão, endereço e shunt) no mesmo turno das medidas, e avisa se o endereço guardado não é o que usa; não se escreve nada no contador.
* **Selagem opcional dos segredos guardados:** desativada por predefinição (`security.seal_secrets`, ou `nodes.nvs_encryption` do servidor). Ativada, as palavras-passe, os tokens, as chaves, os PIN e os hashes de palavras-passe que o nó guarda ficam selados com ChaCha20-Poly1305 e tudo o resto continua legível; ativá-la ou desativá-la reescreve-os sem perder nada, mesmo que o nó pare a meio. Não se queima nenhum eFuse nem se cifra a flash: a chave está numa partição do mesmo chip, pelo que **não** protege contra quem tenha a placa, e um nó instalado antes dessa partição mantém os segredos como estavam até ser gravado com a nova tabela de partições.""",
      "role": r"""O ARMOR-NODE-ELECTRICAL mede a rede CA e CC da casa com os seus contadores e guarda as regras para comutar entre fontes. Publica as leituras para o [ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER), que guarda o histórico e a energia de cada dia e gera os alarmes; o menu *Elétrico* e o *Desenhador elétrico* do [ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) e o ecrã elétrico do [ARMOR-ANDROID-CONTROL](https://github.com/JuanenRac/ARMOR-ANDROID-CONTROL) mostram-no. A comutação está desenhada (armar, um token de uso único, o intertravamento, a confirmação dos dois contactores) mas não ativada.

| Nome | Como | Para quê |
|---|---|---|
| ARMOR-SERVER | MQTT `armor/electrical/<id>/{state,command,result}` | Recebe os canais e ordena uma transferência (só se a manobra estiver ativa em três sítios) |
| ARMOR-STUDIO | menu Elétrico, Electrical Designer | Mostra os canais e os alarmes e abre o painel do nó |
| ARMOR-ANDROID-CONTROL | Bluetooth | Configura o nó no terreno e mostra os canais |
| ARMOR-COMMON | contrato elétrico | As mensagens são verificadas com os seus esquemas; o firmware comum é copiado dele |""",
      "architecture": r"""<p align="center">
  <img src="images/architecture.svg" alt="Arquitetura de ARMOR-NODE-ELECTRICAL: quem o chama, o que contém e de que depende" width="100%">
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
| Rede ou contínua perigosa na placa | O nó só lê os módulos PZEM (módulos fechados, linha série isolada) e nunca leva rede na sua placa; o que comuta é um andar separado testado em bancada com uma lâmpada e um transformador de isolamento |
| Duas fontes fechadas ao mesmo tempo | O controlador de transferência nunca ordena as duas: exige manobra permitida, nó armado mesmo antes e ambos os contactores confirmados abertos durante todo o tempo morto (`dead_time_ms` 2000 por omissão); um contactor que não mostra o que foi ordenado é uma falha que fica até ser reconhecida (`kDidNotOpen`, `kDidNotClose`); continua a ser obrigatório um bloqueio mecânico entre os contactores |
| Uma ordem repetida, ou uma manobra que ninguém pediu | `arm` dá um token de uso único de 64 bits que `close_a` ou `close_b` têm de levar, dentro de `arm_window_ms`; as ordens nunca são retidas; no máximo 4 interruptores; a manobra está DESLIGADA a não ser que o firmware a permita (`switching_enabled`), o servidor corra com `ARMOR_ELECTRICAL_SWITCHING=1` e a lista de acesso do broker esteja aberta para esse nó |
| Uma falha, um retorno perdido ou a manobra desligada | Cada controlador responde com TODAS as bobines abertas (falha => aberto; se aberto é seguro para a carga decide a instalação); o estado na mensagem é o que o contacto auxiliar mostra, não o que foi ordenado; os pares de relés estão bloqueados e o nó nunca abre o par por si mesmo |
| Uma leitura velha mostrada como real | Um contador mudo deixa de ser publicado após 10 s; cada canal leva a idade da sua leitura e o número de pedidos falhados; uma tarefa de contadores bloqueada reinicia a placa por watchdog; a cada `bus.check_settings_s` (600 s, 0 = nunca) as definições dos contadores são lidas (só leitura) e um endereço alterado é comunicado |

A rede (230 V CA) e a corrente contínua de um banco de baterias podem matar e provocar incêndios. [docs/SAFETY.md](docs/SAFETY.md) diz o que o desenho pressupõe; não é o desenho de uma instalação e não substitui a regulamentação do país nem um instalador qualificado. Hoje nada disto comuta nada.""",
      "interfaces": r"""| Parte | O que define |
|---|---|
| MQTT | `armor/electrical/<id>/state` (um canal por entrada: CA ou CC, tensão, corrente, potência, energia, frequência, fator de potência, estado do interruptor, alarme; contrato do ARMOR-COMMON), `armor/electrical/<id>/command` e `/result`, `armor/device/<id>/<relé>/{state,set}`, `armor/health/<id>`, `armor/control/<id>/...` |
| Ordens | `arm`, `close_a`, `close_b` (com o token), `open` e `acknowledge` (limpa uma falha) |
| Contadores | Peacefair PZEM-004T v3 (CA) e PZEM-017 (CC) por Modbus RTU, até 16 numa linha série; só o pedido de leitura é construído (o que escreve endereço ou limiares não existe); entradas analógicas, contactos e relés na placa base; uma ponte Zigbee ([docs/ZIGBEE.md](docs/ZIGBEE.md)) |""",
      "configuration": r"""| Variável | Predefinição | O que define |
|---|---|---|
| `bus.check_settings_s` | 600 | Segundos entre as verificações só de leitura das definições dos contadores (0 = nunca) |
| `dead_time_ms`, `confirm_timeout_ms` | 2000 | O tempo morto de uma transferência e quanto tempo tem um contactor para mostrar o que foi ordenado |
| `switching_enabled` | off | A manobra está DESLIGADA a não ser que esta definição, o servidor (`ARMOR_ELECTRICAL_SWITCHING=1`) e a lista de acesso do broker a permitam |
| `CONFIG_ARMOR_NODE_ID`, `_SETUP_CODE`, `_FLEET_SECRET`, `_MQTT_*`, `_HEARTBEAT_S`, `_BLE_SETUP_MINUTES`, `_BOOT_FACTORY_RESET` | - | As definições que todos os nós partilham: o nome (vazio dá `armor-` e os últimos bytes do MAC), o código de configuração (vazio: aleatório), o segredo de frota (16+ caracteres, nunca no repositório), as primeiras definições do broker, o batimento (de 2 a 300 s), os minutos de configuração Bluetooth (de 1 a 120) e a reposição com BOOT (8 s nos primeiros 30 s) |""",
      "quickstart": r"""**Requisitos:** um compilador C++17 para os testes de anfitrião; o contentor ESP-IDF 5.5.5 para compilar a imagem; uma placa ESP32-S3 (Ethernet ou Wi-Fi).

```bash
cmake -S tests -B build/host && cmake --build build/host && ctest --test-dir build/host   # host tests, -Werror
node tools/panel_mock.mjs --user admin:adminpass123   # the panel without a board
tools/build_node.sh generic s3-wifi                  # the image in the ESP-IDF container (or s3-eth)
```

Veja o [guia do firmware](docs/NODE_FIRMWARE.md) e o [canal Bluetooth](docs/BLE_PROVISIONING.md).

Veja o [desenho](docs/DESIGN.md), as [notas de segurança](docs/SAFETY.md), as [regras de comutação](docs/SWITCHING.md), os [protocolos](docs/PROTOCOLS.md) e as [mensagens](docs/ELECTRICAL_MESSAGES.md).""",
      "testing": r"""```bash
cmake -S tests -B build/host && cmake --build build/host && ctest --test-dir build/host
python -I tools/armor_ci_validate.py
```

19 programas de teste de anfitrião e 5 verificações Python correm com `ctest`; 382264 verificações contadas pelos programas de anfitrião, compiladas com `-Werror`.

Verificações Python: os textos do painel em oito línguas, as tarefas, os caminhos de gravação, a sessão Bluetooth sob o seu bloqueio e as rotas que o painel chama (e, em alguns nós, os códigos HTTP ou os glifos dos tipos de letra)

Os testes de anfitrião precisam de qualquer compilador C++17 (Linux, WSL, MSYS2); o painel web também é exercitado num navegador real contra um nó de substituição (`tools/panel_mock.mjs`, `tools/panel_browser_test.mjs`).

A maior parte das verificações são varrimentos exaustivos das regras de manobra (`test_switch_set` e `test_interlock`: 375 036); os contadores e contactores são substitutos. O `test_clock` só imprime `ok`.""",
      "build": "`tools/build_node.sh` compila a imagem no contentor ESP-IDF 5.5.5 e a versão leva a imagem, o seu SHA-256 e a sua assinatura Ed25519, uma por placa; a imagem grava-se por USB-C da primeira vez e depois atualiza-se a partir do painel.",
      "troubleshooting": r"""| Vê | Porque | Faça |
|---|---|---|
| Perdeu a palavra-passe ou o nó já não se liga à rede | Um nó em configuração e sem endereço após 90 s abre o seu próprio Wi-Fi `ARMOR-SETUP-xxxxxx` (abra `http://192.168.4.1/`) | Para recomeçar mantenha BOOT 8 segundos nos primeiros 30 segundos após ligar (apaga definições e utilizadores), ou use *Reposição de fábrica* no painel |
| Uma atualização do GitHub é recusada | A versão não traz soma de verificação nem assinatura, não coincidem (`e_no_checksum`, `e_no_signature`, `e_checksum_mismatch`, `e_bad_signature`), não traz imagem para esta placa (`e_no_asset_for_board`) ou é de outro projeto (`e_wrong_firmware`) | O nó não mudou; tente de novo ou deixe um administrador enviar o ficheiro à mão |
| Um interruptor mostra uma falha | O contactor não mostrou aberto ou fechado como ordenado (`kDidNotOpen`, `kDidNotClose`); fica até ser reconhecido | Verifique a cablagem do contacto auxiliar e envie `acknowledge` |
| Uma ordem é recusada | A manobra está desligada (`switching_enabled` falso), o token é inválido ou expirou, ou o nó não estava armado mesmo antes | Arme de novo e envie a ordem com o novo token |""",
      "structure": r"""<p align="center">
  <img src="images/repository-structure.svg" alt="Estrutura do repositório de ARMOR-NODE-ELECTRICAL" width="100%">
</p>

<details>
<summary>Versão em texto da árvore</summary>

```text
ARMOR-NODE-ELECTRICAL/
├── main/                                o firmware: um componente ESP-IDF
├── core/                                a lógica sem ESP-IDF, testada num computador
├── panel/                               o painel web embebido no firmware
├── tests/                               testes de anfitrião e verificações Python
├── docs/                                12 guias: segurança, manobra, mensagens, hardware
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

* As tramas e leituras dos PZEM-004T v3 e PZEM-017 são verificadas contra as tramas documentadas e amostras gravadas; nenhum contador respondeu ainda.
* As páginas de contadores e leituras do painel web foram exercitadas num navegador contra um nó simulado, não numa placa.
* Nenhuma placa construída nem contador ou contactor ligados: nada funcionou ainda em equipamentos reais.
* O código de configuração, o acesso com limite de palavras-passe erradas, o PIN Bluetooth e as atualizações assinadas estão testados no anfitrião; não houve revisão independente.
* As verificações de hash e de assinatura Ed25519 e a lógica de retrocesso passam no anfitrião; uma atualização pelo ar nunca foi executada numa placa.
* As regras para manobrar contactores só foram testadas contra contactores simulados; nada aqui manobrou ainda nada real.

**A seguir**

* Experimentar os contadores, os contactores e as regras de manobra numa bancada com lâmpada e transformador de isolamento, e depois uma placa real com a atualização pelo ar.""",
    },
  },
}
