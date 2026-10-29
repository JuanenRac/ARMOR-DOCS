# The facts that do not depend on the language, and the words of every language, of ARMOR-NODE-ALARM, in the universal README layout.
# Copyright (C) 2026 JuanenRac (Electro Hobby 3D). GPL-3.0-or-later.

FACTS = {
  "emoji": "🚨",
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
      "orange",
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
      "green",
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
      "Zones",
      "wired%20%2B%20Zigbee",
      "ffb020",
    ],
    [
      "Checks",
      "482%2C535",
      "2ea44f",
    ],
    [
      "Tests",
      "488930%20checks",
      "2ea44f",
    ],
  ],
}

TEXT = {
  "en": {
    "tagline": "Alarm node and panel: the zones, the arming, the delays, the siren and the PIN of the house's alarm, with the firmware of the node and the rules tested on a computer (nothing has run on a board)",
    "honest": "What exists is the **core of the alarm** (what a zone is, how a wired loop read by the ADC becomes a state, the panel's rules: arming, delays, the alarm, the siren, the PIN with lockout) and the **firmware of the node** built on it (settings, web panel, messages with the server, the Zigbee radio's bridge, a Zigbee coordinator on the network, relays, Bluetooth, signed updates), which builds for both boards; the core, the settings, the messages and the panel in a real browser against a stand-in node are tested on a computer with 488,930 checks in 18 test programs. **Nothing has run on a board or on a real installation, no zone has been wired and no siren connected, the node's own Zigbee conversation with a coordinator (local or on the network) is written and tested against a stand-in coordinator but has never run against a real coordinator or a real sensor, and this is not a certified alarm system.**",
    "glance": [
      [
        "Role",
        "Alarm panel field node for ESP32-S3 (family: Field Nodes, parent: ARMOR-COMMON)",
      ],
      [
        "Stack",
        "C++17, ESP-IDF 5.5.5, ESP32-S3",
      ],
      [
        "Tests",
        "488930 checks in 18 host programs and 5 Python checks (`ctest`)",
      ],
      [
        "Inputs",
        "Up to 8 wired loops, Zigbee sensors (IAS Zone) and siren (IAS WD), 4 buttons",
      ],
      [
        "Runs on",
        "An ESP32-S3 board (Ethernet or Wi-Fi) with the base board; host tests on any computer",
      ],
      [
        "On real hardware",
        "None yet: no board, zone, siren or Zigbee coordinator connected (host tests, the build and the panel in a browser only)",
      ],
      [
        "License",
        "GPL-3.0-or-later",
      ],
    ],
    "status": {
      "software": "The firmware builds in the ESP-IDF 5.5.5 container for both boards (Wi-Fi and Ethernet).",
      "tests": "488,930 checks in 18 host programs pass (`ctest`): the zones, the wired loops read by the ADC, the arming, delays, siren and PIN rules, the settings and the messages.",
      "protocols": "The node's own Zigbee conversation with a coordinator, local or on the network, is tested only against a stand-in coordinator; it has never met a real coordinator or sensor.",
      "ui": "The web panel is exercised in a real browser against a stand-in node, not on a board.",
      "hardware": "No board built, no zone wired and no siren or Zigbee coordinator connected: nothing has run on a real installation.",
      "security": "The PIN with lockout, the set-up code, the login limit and the signed updates are tested on the host; there has been no independent review and this is not a certified alarm system.",
      "updates": "The hash and Ed25519 signature checks and the rollback logic pass on the host; an update over the air has never been run on a board.",
      "writing": "The siren and the relays are driven by the alarm rules and tested against stand-ins; none has been connected to a real siren or relay.",
      "integration": "The messages of the node are validated against the shared schemas and conformance vectors of ARMOR-COMMON.",
      "docs": "Eight languages, the firmware guide, the wiring notes and the changelog are up to date.",
    },
    "docs": [
      "[Safety](docs/SAFETY.md): what the panel promises and what it does not",
      "[Alarm messages](docs/ALARM_MESSAGES.md), [Zigbee](docs/ZIGBEE.md) and [failover](docs/FAILOVER.md)",
      "[Design](docs/DESIGN.md), [hardware](docs/HARDWARE.md), [base board](docs/BASE_BOARD.md) and [node firmware](docs/NODE_FIRMWARE.md)",
      "[Bench tests](docs/BENCH_TESTS.md), [set-up code](docs/SETUP_CODE.md) and [Bluetooth provisioning](docs/BLE_PROVISIONING.md)",
    ],
    "contributing_first": "Before a pull request run `ctest --test-dir build/host` and `python -I tools/armor_ci_validate.py`: it must pass. See [CONTRIBUTING.md](CONTRIBUTING.md) and the [code of conduct](CODE_OF_CONDUCT.md).",
    "languages_extra": "",
    "body": {
      "overview": r"""* **Zones:** four kinds - *instant* (a door, a window), *entry* (the door you come in through: it starts the entry delay), *interior* (motion: only in "away") and *always* (smoke, gas, panic: armed or not). A zone may be a wired loop or a Zigbee sensor.
* **The wired loop:** a contact with an end-of-line resistor, read as a voltage, gives four states in one pin - normal, triggered, and tamper for a shorted or a cut wire. The limits are settings; a debouncer keeps a bouncing contact from raising the alarm.
* **The panel:** *away* and *stay* arming, an exit delay that does not treat the person leaving as an intruder, an entry delay, an alarm that **latches** until a correct disarm, a siren that stops by itself after a time, bypass of open zones when forced (never a sounding smoke detector), and a log of the last hundred events.
* **The PIN:** arming needs none, disarming and silencing do; wrong PINs are counted and, after a few, everything is refused for a while, even the right PIN.
* **Silence without disarming:** while the siren sounds, a correct PIN stops it at once with the system still armed - the alarm stays latched and recorded, a zone that has not sounded yet may sound it again, and a wrong PIN counts toward the lockout like a wrong disarm PIN.
* **The plan:** a gateway on the electrical node's board (a Zigbee radio, wired zones, a siren relay) that works with ARMOR-SERVER and **keeps guarding when the server is away**: a panel takes the radio over from the server through the Zigbee bridge of ARMOR-NODE-ELECTRICAL. See [the design](docs/DESIGN.md) and [the failover](docs/FAILOVER.md).
* **The node:** firmware for the ESP32-S3 (PoE Ethernet or Wi-Fi) with up to eight wired zones, the siren on a relay, the web panel of every node in eight languages, the Zigbee radio lent to Zigbee2MQTT, and the messages `armor/alarm/<node>/state|command|result`; the server may arm and disarm only when three independent switches allow it. See [the firmware](docs/NODE_FIRMWARE.md), [the messages](docs/ALARM_MESSAGES.md) and [the hardware](docs/HARDWARE.md).
* **Taking the radio over:** after the server's Zigbee2MQTT has been away for a set time the node brings the coordinator up itself (ZNP), reads the sensors of the zones that name one (IAS Zone) and commands Zigbee sirens (IAS WD), and lets go the moment the client returns.
* **Not yet:** a real coordinator or sensor, the hardware and any test on a real installation.
* **A restart does not disarm the house:** the mode, a running alarm and the zones left out are kept in flash and taken back at start; a cut or shorted loop is never left out; messages go through a queue (no deadlock with the broker) and the watchdog restarts the board if the task that reads the zones stops.
* **Signed over-the-air updates:** the node installs from GitHub only an image whose SHA-256 matches and that carries a valid Ed25519 signature of the maintainer (the public key is in the firmware, the private one never leaves the maintainer); a file uploaded by hand by an administrator in the panel is still accepted. The pages and messages of the panel are in eight languages.
* **Bluetooth pairing with a PIN:** the six-digit PIN is derived from the set-up code, printed on the USB console and shown to an administrator in the panel; the phone has to enter it before it may write the node's settings.
* **Siren and restarts:** the siren's relay belongs to the alarm alone (the broker, the central and the panel cannot move it, and it does not fall back to open when the broker is lost); a zone that has not sounded yet sounds the siren again after it timed out; an alarm of smoke or panic with the system disarmed, a silenced alarm and a lockout come back after a restart; a reset by hand is refused while the alarm is armed; a Zigbee sensor that never speaks counts as lost.
* **Only the house may use the panel:** the panel answers the private network by default (or the networks its owner lists, such as a VPN), refuses a list that would lock out whoever saves it, counts wrong passwords for each person as well as each address, and works behind the server's proxy so that it can be reached from outside the house without publishing the node.
* **A zone that cannot be read is not shown as closed:** if the converter does not start or a loop gives no reading for five rounds in a row, the zone is in *trouble* - it is not guarding, it never sounds the siren, it stops an arming (unless forced, and then it is left out and noted) and the server warns.
* **Optional encrypted link to the broker (TLS):** off by default, so the node talks plain MQTT as before. A switch and a box for the certificate of the installation's own authority (PEM, at most 2 KB) in the Broker page make it connect with `mqtts://`, trust that authority only and check that the broker's certificate was made for the address it reached; anything that is not one PEM certificate is refused. Covered by host tests; the handshake has not been run on a board yet.
* **Arming profiles:** an arm command may carry a profile (Away, Home, Night, your own) that chooses, for that arming, which zones guard, which alarm at once or after the entry delay, the exit and entry delays and whether the siren sounds (a silent alarm is still latched, recorded and told). It never touches smoke, panic or tamper zones, the PIN, the lockout, the silence, a forced arming or a zone in trouble; the profile survives a restart, and an arm without one behaves exactly as before. Tested against the old rules with a random run and against the shared contract.
* **Health report:** about once a minute the node publishes how long it has been up and why it last restarted, its free memory, its link and Wi-Fi signal, how many times it connected to the broker and the last error it logged (`armor/health/<node>`, the `node_health` contract of ARMOR-COMMON). The code that builds it is shared by every node and tested on a computer; it has not run on a board.
* **Control from the server:** Studio can restart the node cleanly, pause it for up to an hour (it resumes by itself), put its work in standby (no end, kept across restarts, the node stays connected and keeps answering), make it show itself, ask for a diagnostics snapshot and mark it as in maintenance (`armor/control/<node>/...`, the `node_control` contract of ARMOR-COMMON). Every order takes two steps with a one-time token that belongs to that operation, only the server may write them on the broker, and there is no factory reset, no erase and no deep sleep. While the node is paused or in standby its zones are not read, nothing is evaluated, armed or sounded, no state is published and the siren relay is held open: the house is NOT protected, and the health report says so. The code is shared by every node and tested on a computer; it has not run on a board.
* **Diagnostics without a cable:** after a start that was not clean (a crash, a watchdog, a sag of the supply, a failed allocation) the health report says why for ten minutes; a crash leaves its core dump to look at, download or erase from the panel; the stored settings are copied before every firmware install and recovered if an update damages them; and an administrator can ask the node, through the server, for a diagnostic package or its log with a one-time token.
* **The server's security options:** the panel applies the options the server keeps for it (`armor/alarm/<node>/policy`) and each can be fixed on the node itself: the saved armed state is tied to the zones and the PIN, the server's Zigbee zone messages can be switched off, and when signed they are checked (signature with a key typed in the panel, and a sequence number that only goes up). Tested on a computer against the values the contract and the server compute; not run on a board.
* **Optional sealing of stored secrets:** off by default (`security.seal_secrets`, or the server's `nodes.nvs_encryption`). When on, the passwords, tokens, keys, PINs and password hashes the node stores are kept sealed with ChaCha20-Poly1305 and everything else stays readable; turning it on or off rewrites them with nothing lost, even if the node stops half-way. No eFuse is burned and the flash is not encrypted: the key lives in a partition of the same chip, so it does **not** protect against someone who holds the board, and a node installed before that partition existed keeps its secrets as they were until it is flashed with the new partition table.""",
      "role": r"""ARMOR-NODE-ALARM is the alarm panel: the zones, the arming, the delays, the siren and the PIN are decided on the node itself, so the house is still guarded when the server is away. [ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER) shows it, ties Zigbee sensors to its zones and, when you allow it, arms and disarms it; the *Alarm panels* menu and the *Alarm Designer* of [ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) and the [ARMOR-ANDROID-CONTROL](https://github.com/JuanenRac/ARMOR-ANDROID-CONTROL) app drive it. Its Zigbee radio can be on the board or a coordinator on the network.

| Name | How | What for |
|---|---|---|
| ARMOR-SERVER | MQTT `armor/alarm/<id>/{state,command,result,zigbee,policy}` | Receives the state of the panel; orders arming, disarming and silencing only behind three switches |
| ARMOR-STUDIO | alarm panels menu | Shows the zones, the events and the policy, and opens the node's panel |
| ARMOR-ANDROID-CONTROL | Bluetooth | Sets the node up in the field and shows the alarm panels |
| ARMOR-COMMON | alarm contract | The messages are checked against its schemas; the common firmware is copied from it |""",
      "architecture": r"""<p align="center">
  <img src="images/architecture.svg" alt="ARMOR-NODE-ALARM architecture: who calls it, what it holds and what it depends on" width="100%">
</p>""",
      "security": r"""| Threat | Defence |
|---|---|
| Passwords in clear or compiled in | PBKDF2-HMAC-SHA256 with 10 000 rounds; no password in the firmware (a node with no user enters set-up); at most 4 users (admin or viewer) and 8 to 64 characters; at most 6 sessions, 30 minutes idle |
| Taking a freshly flashed node | Set-up needs a start-up code: the one of the build (`CONFIG_ARMOR_SETUP_CODE`) or a random one kept in flash and shown on the USB console; with a fleet secret it is `HMAC-SHA256(secret, MAC)`; it is also the key of the set-up Wi-Fi (WPA2, never bridged) |
| The panel reached from the internet | It answers the private networks of a house by default (10/8, 172.16/12, 192.168/16, 169.254/16, 127/8 and 100.64/10 where some VPNs live); the setting `web.admin_sources` lists other IPv4 addresses and networks (8 entries, 120 characters); anything outside is refused except the public identity `GET /api/v1/session`; a list that would lock out the person saving it is rejected |
| The panel in clear over HTTP | HTTPS on 443 with a certificate the node makes itself (self-signed, in flash, SHA-256 fingerprint shown to compare); the panel can be http, https or both; the session cookie is always HttpOnly and SameSite=Strict (and Secure over TLS) |
| A fake firmware from GitHub | An image is installed only with a matching SHA-256 and a valid Ed25519 signature made with the maintainer's key (`no_checksum`, `no_signature`, `bad_signature`, `checksum_mismatch`, `wrong_firmware`, `not_newer`, `version_mismatch` refuse it); a manual upload by an administrator is not checked: an explicit limit |
| Hijacking the Bluetooth set-up | A 6-digit PIN derived from the set-up code, shown on the USB console and to an administrator; the phone must type it before writing settings; the set-up window lasts `CONFIG_ARMOR_BLE_SETUP_MINUTES` (10 by default, 1 to 120) |
| Stored secrets read by someone who has the board | Optional (off by default, switch `security.seal_secrets` or the server's `nodes.nvs_encryption`): ChaCha20-Poly1305 for passwords, tokens, keys, PINs and hashes. It does not encrypt the flash or burn an eFuse: the key is in a partition of the same chip, so it does not protect against whoever holds the board |
| The broker link in clear | Optional TLS (`mqtts://`) with the owner's own authority (PEM up to 2 KB) and a check of the name; off by default. The handshake has only run in host tests, not on a board |
| Guessing the panel PIN | The comparison does not leak where it differs; failures in a row lock the panel for `lockout_s` (60 s by default, 1 to 3600) times 1, 5 and 15 for the first three lockouts, even for the right PIN; a lockout in progress is restored after a restart; arming needs no PIN, disarming and silencing do |
| A restart that disarms the house | The mode, the alarm in progress and the excluded zones are kept in flash and recovered; a cut or shorted loop is never left out; smoke, panic and tamper that fired while disarmed come back after a restart; the BOOT reset only erases with the panel DISARMED |
| A zone that cannot be read looks closed | It shows `trouble` (the converter does not start or 5 rounds gave no reading) and the panel does not arm with it unless forced, and then it is excluded and noted; a smoke or panic detector that is sounding is never excluded |
| An order from the server that nobody authorised | Arming, disarming and silencing from the server need THREE switches (the node setting, the broker's access list and `ARMOR_ALARM_COMMANDS=1` on the server), the server asks the user's PIN before sending a disarm or a silence, and all of it is off by default; the siren relay belongs to the alarm alone (the broker, the central and the panel cannot move it) |
| Forged Zigbee messages | The topic `armor/alarm/<id>/zigbee` carries an HMAC-SHA256 over node, zone, state, battery and sequence with the panel's key (64 hex typed in the panel), and the sequence only goes up; the policy topic carries `config_hash`, `zone_feed` and its signature, each of which can be pinned on the node |

This is not a certified alarm system ([docs/SAFETY.md](docs/SAFETY.md)): it is a home project and has never run on a board or in a real installation. If the server is gone the panel decides alone, and if the node or its radio also fails nobody is watching. Read [SECURITY.md](SECURITY.md) to report a vulnerability.""",
      "interfaces": r"""| Part | What it sets |
|---|---|
| MQTT | `armor/alarm/<id>/state` (not retained: zones with id, name, kind, state and bypass, the phase), `/command`, `/result`, `/zigbee` and `/policy` (server to panel); `armor/device/<id>/<relay>/{state,set}`, `armor/health/<id>`, `armor/control/<id>/...` |
| Zones | Kind `instant`, `entry`, `interior` or `always`; state `normal`, `triggered`, `tamper` or `trouble`; up to 8 wired loops (a contact with an end-of-line resistor read by the ADC gives four states on one pin; the Ethernet board has 6 valid analogue pins, the Wi-Fi board 8), 4 buttons and a log of 100 events |
| Zigbee | A serial bridge (ZNP) to a coordinator, IAS Zone sensors and IAS WD sirens; the node takes the radio when the server's Zigbee2MQTT goes silent for `zigbee_silence_min` and gives it back when the server returns ([docs/ZIGBEE.md](docs/ZIGBEE.md), [docs/FAILOVER.md](docs/FAILOVER.md)) |""",
      "configuration": r"""| Variable | Default | What it sets |
|---|---|---|
| `panel.exit_delay_s`, `panel.entry_delay_s` | 30, 30 (0-600) | The exit and entry delays; the exit does not treat the person leaving as an intruder |
| `panel.lockout_s` | 60 (1-3600) | The PIN lockout, times 1, 5 and 15 for the first three |
| `zigbee_silence_min` | - | How long the server's Zigbee may be silent before the node takes the radio |
| `CONFIG_ARMOR_NODE_ID`, `_SETUP_CODE`, `_FLEET_SECRET`, `_MQTT_*`, `_HEARTBEAT_S`, `_BLE_SETUP_MINUTES`, `_BOOT_FACTORY_RESET` | - | The settings every node shares: the name (empty gives `armor-` and the last bytes of the MAC), the set-up code (empty: random), the fleet secret (16+ characters, never in the repository), the first broker settings, the heartbeat (2 to 300 s), the minutes of Bluetooth set-up (1 to 120) and the reset with BOOT (8 s in the first 30 s) |

Re-sounds after a silence are limited to 3 (`kMaxResounds`). The siren relay starts open on every restart and does not fall open when the broker is lost.""",
      "quickstart": r"""**Requirements:** a C++17 compiler for the host tests; the ESP-IDF 5.5.5 container to build the image; an ESP32-S3 board (Ethernet or Wi-Fi) with the base board.

```bash
cmake -S tests -B build/host && cmake --build build/host && ctest --test-dir build/host   # host tests, -Werror
node tools/panel_mock.mjs --user admin:adminpass123   # the panel without a board
tools/build_node.sh generic s3-wifi                  # the image in the ESP-IDF container (or s3-eth)
```

See the [design](docs/DESIGN.md), [how the panel takes over from the server](docs/FAILOVER.md) and the [safety notes](docs/SAFETY.md).""",
      "testing": r"""```bash
cmake -S tests -B build/host && cmake --build build/host && ctest --test-dir build/host
python -I tools/armor_ci_validate.py
```

18 host test programs and 5 Python checks run under `ctest`; 488930 checks counted by the host programs, built with `-Werror`.

Python checks: the panel texts in eight languages, the tasks, the save paths, the Bluetooth session under its lock and the routes the panel calls (and, in some nodes, the HTTP codes or the glyphs of the fonts)

The host tests need any C++17 compiler (Linux, WSL, MSYS2); the web panel is also exercised in a real browser against a stand-in node (`tools/panel_mock.mjs`, `tools/panel_browser_test.mjs`).

Most of the checks are exhaustive sweeps of the panel rules; the loops, the siren and the Zigbee link are stand-ins.""",
      "build": "`tools/build_node.sh` builds the image in the ESP-IDF 5.5.5 container and the release carries the image, its SHA-256 and its Ed25519 signature, one per board; the image is written by USB-C the first time and updated from the panel afterwards.",
      "troubleshooting": r"""| You see | Because | Do |
|---|---|---|
| You lost the password or the node no longer joins the network | A node with set-up and no address after 90 s opens its own Wi-Fi `ARMOR-SETUP-xxxxxx` (open `http://192.168.4.1/`) | To start again hold BOOT for 8 seconds in the first 30 seconds after power-up (erases settings and users), or use *Factory reset* in the panel |
| An update from GitHub is refused | The release has no checksum or signature, they do not match (`e_no_checksum`, `e_no_signature`, `e_checksum_mismatch`, `e_bad_signature`), has no image for this board (`e_no_asset_for_board`) or is for another project (`e_wrong_firmware`) | Nothing changed on the node; try again or let an administrator upload the file by hand |
| The panel will not arm | A zone is in `trouble` (the converter does not start or 5 rounds gave no reading) | Fix the wiring, or force the arming (the zone is then excluded and noted) |
| The PIN is refused even when it is right | The panel is locked after failed attempts (even the right PIN is refused) | Wait `lockout_s`; the lockout survives a restart |
| The BOOT reset does nothing | The panel is armed: the reset only erases a disarmed panel | Disarm with the PIN first |""",
      "structure": r"""<p align="center">
  <img src="images/repository-structure.svg" alt="Repository structure of ARMOR-NODE-ALARM" width="100%">
</p>

<details>
<summary>Text version of the tree</summary>

```text
ARMOR-NODE-ALARM/
├── main/                                the firmware: an ESP-IDF component
├── core/                                the logic with no ESP-IDF, tested on a computer
├── panel/                               the web panel embedded in the firmware
├── tests/                               host tests and Python checks
├── docs/                                11 guides: safety, messages, Zigbee, failover
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

* The node's own Zigbee conversation with a coordinator, local or on the network, is tested only against a stand-in coordinator; it has never met a real coordinator or sensor.
* The web panel is exercised in a real browser against a stand-in node, not on a board.
* No board built, no zone wired and no siren or Zigbee coordinator connected: nothing has run on a real installation.
* The PIN with lockout, the set-up code, the login limit and the signed updates are tested on the host; there has been no independent review and this is not a certified alarm system.
* The hash and Ed25519 signature checks and the rollback logic pass on the host; an update over the air has never been run on a board.
* The siren and the relays are driven by the alarm rules and tested against stand-ins; none has been connected to a real siren or relay.

**Next**

* Wire real loops and a siren, try the Zigbee link with a real coordinator and sensors, and run the panel in a real installation before anything more is claimed.""",
    },
  },
  "es": {
    "tagline": "Nodo y central de alarma: las zonas, el armado, los retardos, la sirena y el PIN de la alarma de la casa, con el firmware del nodo y las reglas probadas en un ordenador (nada ha corrido en una placa)",
    "honest": "Lo que existe es el **núcleo de la alarma** (qué es una zona, cómo un bucle cableado leído por el ADC se convierte en un estado, las reglas de la central: armado, retardos, la alarma, la sirena, el PIN con bloqueo) y el **firmware del nodo** construido sobre él (ajustes, panel web, mensajes con el servidor, el puente de la radio Zigbee, un coordinador Zigbee en la red, relés, Bluetooth, actualizaciones firmadas), que compila para las dos placas; el núcleo, los ajustes, los mensajes y el panel en un navegador real contra un nodo de pega se prueban en un ordenador con 488.930 comprobaciones en 18 programas de test. **Nada ha corrido en una placa ni en una instalación real, no se ha cableado ninguna zona ni conectado ninguna sirena, la conversación Zigbee del propio nodo con un coordinador (local o en la red) está escrita y probada contra un coordinador de pega pero nunca ha corrido contra un coordinador ni un sensor reales, y esto no es un sistema de alarma certificado.**",
    "glance": [
      [
        "Función",
        "Nodo de campo central de alarma para ESP32-S3 (familia: Field Nodes, padre: ARMOR-COMMON)",
      ],
      [
        "Tecnología",
        "C++17, ESP-IDF 5.5.5, ESP32-S3",
      ],
      [
        "Pruebas",
        "488930 comprobaciones en 18 programas de host y 5 de Python (`ctest`)",
      ],
      [
        "Entradas",
        "Hasta 8 lazos cableados, sensores Zigbee (IAS Zone) y sirena (IAS WD), 4 botones",
      ],
      [
        "Funciona en",
        "Una placa ESP32-S3 (Ethernet o Wi-Fi) con la placa base; pruebas de host en cualquier ordenador",
      ],
      [
        "En hardware real",
        "Ninguno todavía: ninguna placa, zona, sirena ni coordinador Zigbee conectados (solo tests en ordenador, la compilación y el panel en un navegador)",
      ],
      [
        "Licencia",
        "GPL-3.0-or-later",
      ],
    ],
    "status": {
      "software": "El firmware compila en el contenedor ESP-IDF 5.5.5 para las dos placas (Wi-Fi y Ethernet).",
      "tests": "Pasan 488.930 comprobaciones en 18 programas de host (`ctest`): las zonas, los lazos cableados leídos por el ADC, las reglas de armado, retardos, sirena y PIN, los ajustes y los mensajes.",
      "protocols": "La conversación Zigbee del propio nodo con un coordinador, local o en la red, solo se ha probado contra un coordinador simulado; nunca se ha encontrado con un coordinador o un sensor reales.",
      "ui": "El panel web se ha ejercitado en un navegador real contra un nodo simulado, no en una placa.",
      "hardware": "Ninguna placa construida, ninguna zona cableada y ninguna sirena o coordinador Zigbee conectados: nada ha funcionado en una instalación real.",
      "security": "El PIN con bloqueo, el código de configuración, el límite de accesos y las actualizaciones firmadas están probados en el host; no ha habido una revisión independiente y esto no es un sistema de alarma certificado.",
      "updates": "Las comprobaciones de hash y de firma Ed25519 y la lógica de vuelta atrás pasan en el host; una actualización por aire nunca se ha ejecutado en una placa.",
      "writing": "La sirena y los relés los gobiernan las reglas de la alarma y se han probado contra simulaciones; ninguno se ha conectado a una sirena o un relé reales.",
      "integration": "Los mensajes del nodo se validan contra los esquemas compartidos y los vectores de conformidad de ARMOR-COMMON.",
      "docs": "Ocho idiomas, la guía del firmware, las notas de cableado y el historial de cambios están al día.",
    },
    "docs": [
      "[Seguridad](docs/SAFETY.md): lo que promete la central y lo que no",
      "[Mensajes de alarma](docs/ALARM_MESSAGES.md), [Zigbee](docs/ZIGBEE.md) y [relevo](docs/FAILOVER.md)",
      "[Diseño](docs/DESIGN.md), [hardware](docs/HARDWARE.md), [placa base](docs/BASE_BOARD.md) y [firmware del nodo](docs/NODE_FIRMWARE.md)",
      "[Pruebas de banco](docs/BENCH_TESTS.md), [código de puesta en marcha](docs/SETUP_CODE.md) y [alta por Bluetooth](docs/BLE_PROVISIONING.md)",
    ],
    "contributing_first": "Antes de un pull request ejecuta `ctest --test-dir build/host` and `python -I tools/armor_ci_validate.py`: debe pasar. Consulta [CONTRIBUTING.md](CONTRIBUTING.md) y el [código de conducta](CODE_OF_CONDUCT.md).",
    "languages_extra": "",
    "body": {
      "overview": r"""* **Zonas:** cuatro tipos - *instantánea* (una puerta, una ventana), *de entrada* (la puerta por la que entras: inicia el retardo de entrada), *interior* (movimiento: solo en "fuera") y *siempre* (humo, gas, pánico: armada o no). Una zona puede ser un bucle cableado o un sensor Zigbee.
* **El bucle cableado:** un contacto con resistencia de fin de línea, leído como tensión, da cuatro estados en un solo pin - normal, disparada y sabotaje por un cable en cortocircuito o cortado. Los límites son ajustes; un filtro antirrebote evita que un contacto que rebota dispare la alarma.
* **La central:** armado *fuera* y *en casa*, un retardo de salida que no trata como intruso a quien se va, un retardo de entrada, una alarma que **se mantiene** hasta un desarmado correcto, una sirena que se para sola pasado un tiempo, anulación de zonas abiertas si se fuerza (nunca un detector de humo sonando) y un registro de los últimos cien eventos.
* **El PIN:** armar no lo pide, desarmar y silenciar sí; los PIN erróneos se cuentan y, tras unos pocos, se rechaza todo durante un tiempo, incluso el PIN correcto.
* **Silenciar sin desarmar:** mientras suena la sirena, un PIN correcto la para al instante con el sistema aún armado: la alarma sigue enclavada y registrada, una zona que aún no ha sonado puede volver a hacerla sonar, y un PIN erróneo cuenta para el bloqueo como uno erróneo de desarmar.
* **El plan:** una pasarela en la placa del nodo eléctrico (radio Zigbee, zonas cableadas, relé de sirena) que trabaja con ARMOR-SERVER y **sigue vigilando cuando el servidor falta**: una central toma la radio al servidor por el puente Zigbee de ARMOR-NODE-ELECTRICAL. Véanse [el diseño](docs/DESIGN.md) y [el relevo](docs/FAILOVER.md).
* **El nodo:** firmware para el ESP32-S3 (Ethernet PoE o Wi-Fi) con hasta ocho zonas cableadas, la sirena en un relé, el panel web de todos los nodos en ocho idiomas, la radio Zigbee prestada a Zigbee2MQTT y los mensajes `armor/alarm/<nodo>/state|command|result`; el servidor solo puede armar y desarmar si tres interruptores independientes lo permiten. Véanse [el firmware](docs/NODE_FIRMWARE.md), [los mensajes](docs/ALARM_MESSAGES.md) y [el hardware](docs/HARDWARE.md).
* **Tomar la radio:** cuando Zigbee2MQTT del servidor lleva un tiempo ausente, el nodo levanta el coordinador por sí mismo (ZNP), lee los sensores de las zonas que nombran uno (IAS Zone) y manda a sirenas Zigbee (IAS WD), y lo suelta en cuanto vuelve el cliente.
* **Todavía no:** un coordinador o sensor reales, el hardware y cualquier prueba en una instalación real.
* **Un reinicio no desarma la casa:** el modo, una alarma en marcha y las zonas excluidas se guardan en la flash y se recuperan al arrancar; un lazo cortado o en cortocircuito nunca se excluye; los mensajes pasan por una cola (sin bloqueo mutuo con el broker) y el perro guardián reinicia la placa si se para la tarea que lee las zonas.
* **Actualizaciones por aire firmadas:** el nodo solo instala desde GitHub una imagen cuyo SHA-256 coincide y que lleva una firma Ed25519 válida del responsable (la clave pública está en el firmware, la privada nunca sale del responsable); un archivo subido a mano por un administrador en el panel se sigue aceptando. Las páginas y mensajes del panel están en ocho idiomas.
* **Emparejamiento Bluetooth con PIN:** el PIN de seis cifras se deriva del código de configuración, se imprime en la consola USB y se muestra a un administrador en el panel; el móvil tiene que escribirlo antes de poder cambiar los ajustes del nodo.
* **Sirena y reinicios:** el relé de la sirena es solo de la alarma (ni el broker, ni la central, ni el panel pueden moverlo, y no se abre al perder el broker); una zona que aún no había sonado vuelve a hacer sonar la sirena pasado su tiempo; tras un reinicio vuelven una alarma de humo o pánico con el sistema desarmado, una alarma silenciada y un bloqueo; un reset a mano se rechaza con la alarma armada; un sensor Zigbee que nunca habla cuenta como perdido.
* **Solo la casa puede usar el panel:** el panel responde por defecto a la red privada (o a las redes que su dueño indique, como una VPN), rechaza una lista que dejaría fuera a quien la guarda, cuenta las contraseñas erróneas por persona y por dirección, y funciona detrás del proxy del servidor para llegar a él desde fuera de casa sin publicar el nodo.
* **Una zona que no se puede leer no se muestra como cerrada:** si el conversor no arranca o un lazo no da lectura cinco rondas seguidas, la zona pasa a *avería* (trouble): no vigila, nunca hace sonar la sirena, impide armar (salvo forzando, y entonces queda excluida y anotada) y el servidor avisa.
* **Enlace cifrado opcional con el broker (TLS):** desactivado por defecto, así que el nodo habla MQTT sin cifrar como antes. Un interruptor y una caja para el certificado de la autoridad propia de la instalación (PEM, 2 KB como máximo) en la página Broker hacen que se conecte con `mqtts://`, confíe solo en esa autoridad y compruebe que el certificado del broker se hizo para la dirección a la que llegó; lo que no sea un único certificado PEM se rechaza. Cubierto con pruebas en el ordenador; el handshake aún no se ha ejecutado en una placa.
* **Perfiles de armado:** un comando de armar puede llevar un perfil (Fuera, En casa, Noche, el tuyo) que elige, para ese armado, qué zonas vigilan, cuáles disparan la alarma al instante o tras el retardo de entrada, los retardos de salida y entrada y si suena la sirena (una alarma silenciosa se queda enganchada, anotada y avisada). Nunca toca las zonas de humo, pánico o sabotaje, el PIN, el bloqueo, el silencio, un armado forzado ni una zona con problema; el perfil sobrevive a un reinicio y un armado sin perfil se comporta exactamente como antes. Probado contra las reglas antiguas con una ejecución aleatoria y contra el contrato compartido.
* **Informe de salud:** cada minuto más o menos el nodo publica cuánto lleva encendido y por qué se reinició la última vez, su memoria libre, su enlace y su señal Wi-Fi, cuántas veces se conectó al broker y el último error que anotó (`armor/health/<nodo>`, el contrato `node_health` de ARMOR-COMMON). El código que lo construye lo comparten todos los nodos y está probado en un ordenador; no se ha ejecutado en una placa.
* **Control desde el servidor:** Studio puede reiniciar el nodo limpiamente, pausarlo hasta una hora (se reanuda solo), poner su trabajo en espera (sin fin, se conserva al reiniciar, el nodo sigue conectado y respondiendo), hacer que se muestre, pedirle una instantánea de diagnóstico y marcarlo en mantenimiento (`armor/control/<nodo>/...`, el contrato `node_control` de ARMOR-COMMON). Cada orden son dos pasos con un token de un solo uso que pertenece a esa operación, solo el servidor puede escribirlas en el broker, y no existe restablecimiento de fábrica, borrado ni sueño profundo. Mientras el nodo está en pausa o en espera no se leen sus zonas, no se evalúa, arma ni hace sonar nada, no se publica estado y el relé de la sirena se mantiene abierto: la casa NO está protegida, y el informe de salud lo dice. El código es compartido por todos los nodos y se prueba en un ordenador; no ha funcionado en una placa.
* **Diagnóstico sin cable:** tras un arranque que no fue limpio (un cuelgue, un watchdog, una caída de la alimentación, una reserva de memoria fallida) el informe de salud dice el motivo durante diez minutos; un fallo deja su volcado de núcleo (core dump) para verlo, descargarlo o borrarlo desde el panel; los ajustes guardados se copian antes de cada instalación de firmware y se recuperan si una actualización los daña; y un administrador puede pedir al nodo, a través del servidor, un paquete de diagnóstico o su registro con un token de un solo uso.
* **Las opciones de seguridad del servidor:** la central aplica las opciones que el servidor guarda para ella (`armor/alarm/<nodo>/policy`) y cada una puede fijarse en el propio nodo: el estado armado guardado se ata a las zonas y al PIN, los mensajes de zona Zigbee del servidor pueden apagarse y, si van firmados, se comprueban (firma con una clave escrita en el panel y un número de secuencia que solo crece). Probado en un ordenador con los valores que calculan el contrato y el servidor; no se ha ejecutado en una placa.
* **Sellado opcional de los secretos guardados:** desactivado por defecto (`security.seal_secrets`, o `nodes.nvs_encryption` del servidor). Activado, las contraseñas, tokens, claves, PIN y hashes de contraseña que guarda el nodo quedan sellados con ChaCha20-Poly1305 y todo lo demás sigue legible; activarlo o desactivarlo los reescribe sin perder nada, aunque el nodo se pare a medias. No se quema ningún eFuse ni se cifra la flash: la clave está en una partición del mismo chip, así que **no** protege frente a quien tenga la placa, y un nodo instalado antes de esa partición conserva sus secretos como estaban hasta que se grabe con la nueva tabla de particiones.""",
      "role": r"""ARMOR-NODE-ALARM es la central de alarma: las zonas, el armado, los retardos, la sirena y el PIN se deciden en el propio nodo, así que la casa sigue vigilada cuando el servidor no está. [ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER) la muestra, ata sensores Zigbee a sus zonas y, cuando lo permites, la arma y desarma; el menú *Centrales de alarma* y el *Diseñador de alarma* de [ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) y la app [ARMOR-ANDROID-CONTROL](https://github.com/JuanenRac/ARMOR-ANDROID-CONTROL) la manejan. Su radio Zigbee puede estar en la placa o ser un coordinador en la red.

| Nombre | Cómo | Para qué |
|---|---|---|
| ARMOR-SERVER | MQTT `armor/alarm/<id>/{state,command,result,zigbee,policy}` | Recibe el estado de la central; ordena armar, desarmar y silenciar solo tras tres interruptores |
| ARMOR-STUDIO | menú de centrales de alarma | Muestra las zonas, los eventos y la política, y abre el panel del nodo |
| ARMOR-ANDROID-CONTROL | Bluetooth | Configura el nodo en el campo y muestra las centrales de alarma |
| ARMOR-COMMON | contrato de alarma | Los mensajes se comprueban con sus esquemas; el firmware común se copia de él |""",
      "architecture": r"""<p align="center">
  <img src="images/architecture.svg" alt="Arquitectura de ARMOR-NODE-ALARM: quién lo llama, qué contiene y de qué depende" width="100%">
</p>""",
      "security": r"""| Amenaza | Defensa |
|---|---|
| Contraseñas en claro o compiladas | PBKDF2-HMAC-SHA256 con 10 000 rondas; ninguna contraseña en el firmware (un nodo sin usuario entra en puesta en marcha); máximo 4 usuarios (admin o visor) y de 8 a 64 caracteres; máximo 6 sesiones, 30 minutos de inactividad |
| Tomar un nodo recién grabado | La puesta en marcha exige un código: el de la compilación (`CONFIG_ARMOR_SETUP_CODE`) o uno aleatorio guardado en flash y mostrado en la consola USB; con secreto de flota es `HMAC-SHA256(secreto, MAC)`; también es la clave del Wi-Fi de configuración (WPA2, nunca puenteado) |
| El panel alcanzado desde internet | Responde por defecto a las redes privadas de una casa (10/8, 172.16/12, 192.168/16, 169.254/16, 127/8 y 100.64/10 donde viven algunas VPN); el ajuste `web.admin_sources` lista otras direcciones y redes IPv4 (8 entradas, 120 caracteres); lo de fuera se rechaza salvo la identidad pública `GET /api/v1/session`; se rechaza una lista que dejaría fuera a quien la guarda |
| El panel en claro por HTTP | HTTPS en el 443 con un certificado que el nodo hace él mismo (autofirmado, en flash, huella SHA-256 visible para comparar); el panel puede ser http, https o ambos; la cookie de sesión es siempre HttpOnly y SameSite=Strict (y Secure por TLS) |
| Un firmware falso desde GitHub | Una imagen solo se instala con un SHA-256 que coincide y una firma Ed25519 válida hecha con la clave del mantenedor (`no_checksum`, `no_signature`, `bad_signature`, `checksum_mismatch`, `wrong_firmware`, `not_newer`, `version_mismatch` la rechazan); una subida manual de un administrador no se comprueba: es un límite explícito |
| Secuestro de la puesta en marcha por Bluetooth | Un PIN de 6 dígitos derivado del código de puesta en marcha, visible en la consola USB y para el administrador; el móvil debe introducirlo antes de escribir ajustes; la ventana dura `CONFIG_ARMOR_BLE_SETUP_MINUTES` (10 por defecto, de 1 a 120) |
| Secretos guardados leídos por quien tiene la placa | Opcional (apagado por defecto, interruptor `security.seal_secrets` o `nodes.nvs_encryption` del servidor): ChaCha20-Poly1305 para contraseñas, tokens, claves, PIN y hashes. No cifra la flash ni quema un eFuse: la clave está en una partición del mismo chip, así que no protege frente a quien tenga la placa |
| El enlace con el broker en claro | TLS opcional (`mqtts://`) con la autoridad propia del dueño (PEM de hasta 2 KB) y comprobación del nombre; apagado por defecto. El handshake solo se ha ejecutado en pruebas de host, no en una placa |
| Adivinar el PIN de la central | La comparación no filtra dónde difiere; los fallos seguidos bloquean la central `lockout_s` (60 s por defecto, de 1 a 3600) multiplicado por 1, 5 y 15 en los tres primeros bloqueos, incluso para el PIN correcto; un bloqueo en curso se restaura tras reiniciar; armar no lleva PIN, desarmar y silenciar sí |
| Un reinicio que desarma la casa | El modo, la alarma en marcha y las zonas excluidas se guardan en flash y se recuperan; un lazo cortado o en corto nunca se deja fuera; humo, pánico y sabotaje que saltaron con el sistema desarmado vuelven tras reiniciar; el reinicio de fábrica con BOOT solo borra con la central DESARMADA |
| Una zona ilegible parece cerrada | Muestra `trouble` (el convertidor no arranca o 5 rondas sin lectura) y la central no arma con ella salvo forzado, y entonces queda excluida y anotada; un detector de humo o pánico que está sonando nunca se excluye |
| Una orden del servidor que nadie autorizó | Armar, desarmar y silenciar desde el servidor exigen TRES interruptores (el ajuste del nodo, la lista de acceso del broker y `ARMOR_ALARM_COMMANDS=1` en el servidor), el servidor pide el PIN del usuario antes de enviar un desarme o un silencio, y todo está apagado por defecto; el relé de la sirena pertenece solo a la alarma (ni el broker, ni la central ni el panel pueden moverlo) |
| Mensajes Zigbee falsos | El topic `armor/alarm/<id>/zigbee` lleva un HMAC-SHA256 sobre nodo, zona, estado, batería y secuencia con la clave de la central (64 hex tecleados en el panel), y la secuencia solo sube; el topic de política lleva `config_hash`, `zone_feed` y su firma, cada uno de los cuales se puede fijar en el nodo |

No es un sistema de alarma certificado ([docs/SAFETY.md](docs/SAFETY.md)): es un proyecto doméstico y nunca ha corrido en una placa ni en una instalación real. Si falta el servidor la central decide sola, y si además falla el nodo o su radio nadie vigila. Lee [SECURITY.md](SECURITY.md) para informar de una vulnerabilidad.""",
      "interfaces": r"""| Parte | Qué define |
|---|---|
| MQTT | `armor/alarm/<id>/state` (no retenido: zonas con id, nombre, tipo, estado y exclusión, la fase), `/command`, `/result`, `/zigbee` y `/policy` (servidor a central); `armor/device/<id>/<relé>/{state,set}`, `armor/health/<id>`, `armor/control/<id>/...` |
| Zonas | Tipo `instant`, `entry`, `interior` o `always`; estado `normal`, `triggered`, `tamper` o `trouble`; hasta 8 lazos cableados (un contacto con resistencia de fin de línea leído por el ADC da cuatro estados en un pin; la placa Ethernet tiene 6 pines analógicos válidos, la Wi-Fi 8), 4 botones y un registro de 100 eventos |
| Zigbee | Un puente serie (ZNP) a un coordinador, sensores IAS Zone y sirenas IAS WD; el nodo toma la radio si el Zigbee2MQTT del servidor calla durante `zigbee_silence_min` y la devuelve cuando vuelve el servidor ([docs/ZIGBEE.md](docs/ZIGBEE.md), [docs/FAILOVER.md](docs/FAILOVER.md)) |""",
      "configuration": r"""| Variable | Por defecto | Qué define |
|---|---|---|
| `panel.exit_delay_s`, `panel.entry_delay_s` | 30, 30 (0-600) | Los retardos de salida y de entrada; la salida no trata como intruso a quien se va |
| `panel.lockout_s` | 60 (1-3600) | El bloqueo del PIN, multiplicado por 1, 5 y 15 en los tres primeros |
| `zigbee_silence_min` | - | Cuánto puede callar el Zigbee del servidor antes de que el nodo tome la radio |
| `CONFIG_ARMOR_NODE_ID`, `_SETUP_CODE`, `_FLEET_SECRET`, `_MQTT_*`, `_HEARTBEAT_S`, `_BLE_SETUP_MINUTES`, `_BOOT_FACTORY_RESET` | - | Los ajustes que comparten todos los nodos: el nombre (vacío da `armor-` y los últimos bytes de la MAC), el código de puesta en marcha (vacío: aleatorio), el secreto de flota (16+ caracteres, nunca en el repositorio), los primeros ajustes del broker, el latido (de 2 a 300 s), los minutos de puesta en marcha por Bluetooth (de 1 a 120) y el reinicio con BOOT (8 s en los primeros 30 s) |

Los resonidos tras un silencio se limitan a 3 (`kMaxResounds`). El relé de la sirena arranca abierto en cada reinicio y no cae a abierto si se pierde el broker.""",
      "quickstart": r"""**Requisitos:** un compilador C++17 para las pruebas de host; el contenedor ESP-IDF 5.5.5 para compilar la imagen; una placa ESP32-S3 (Ethernet o Wi-Fi) con la placa base.

```bash
cmake -S tests -B build/host && cmake --build build/host && ctest --test-dir build/host   # host tests, -Werror
node tools/panel_mock.mjs --user admin:adminpass123   # the panel without a board
tools/build_node.sh generic s3-wifi                  # the image in the ESP-IDF container (or s3-eth)
```

Véanse [el diseño](docs/DESIGN.md), [cómo la central toma el relevo del servidor](docs/FAILOVER.md) y las [notas de seguridad](docs/SAFETY.md).""",
      "testing": r"""```bash
cmake -S tests -B build/host && cmake --build build/host && ctest --test-dir build/host
python -I tools/armor_ci_validate.py
```

18 programas de prueba de host y 5 comprobaciones en Python se ejecutan con `ctest`; 488930 comprobaciones contadas por los programas de host, compilados con `-Werror`.

Comprobaciones Python: los textos del panel en ocho idiomas, las tareas, las rutas de guardado, la sesión Bluetooth bajo su bloqueo y las rutas que llama el panel (y, en algunos nodos, los códigos HTTP o los glifos de las fuentes)

Las pruebas de host necesitan cualquier compilador C++17 (Linux, WSL, MSYS2); el panel web también se ejercita en un navegador real contra un nodo de pruebas (`tools/panel_mock.mjs`, `tools/panel_browser_test.mjs`).

La mayoría de las comprobaciones son barridos exhaustivos de las reglas de la central; los lazos, la sirena y el enlace Zigbee son sustitutos.""",
      "build": "`tools/build_node.sh` compila la imagen en el contenedor ESP-IDF 5.5.5 y la versión lleva la imagen, su SHA-256 y su firma Ed25519, una por placa; la imagen se graba por USB-C la primera vez y después se actualiza desde el panel.",
      "troubleshooting": r"""| Ves | Porque | Haz |
|---|---|---|
| Perdiste la contraseña o el nodo ya no se une a la red | Un nodo con puesta en marcha y sin dirección tras 90 s abre su propio Wi-Fi `ARMOR-SETUP-xxxxxx` (abre `http://192.168.4.1/`) | Para empezar de cero mantén BOOT 8 segundos en los primeros 30 segundos tras encender (borra ajustes y usuarios), o usa *Restablecer de fábrica* en el panel |
| Se rechaza una actualización desde GitHub | La versión no trae suma de comprobación ni firma, no coinciden (`e_no_checksum`, `e_no_signature`, `e_checksum_mismatch`, `e_bad_signature`), no trae imagen para esta placa (`e_no_asset_for_board`) o es de otro proyecto (`e_wrong_firmware`) | El nodo no cambió; reintenta o deja que un administrador suba el fichero a mano |
| La central no arma | Una zona está en `trouble` (el convertidor no arranca o 5 rondas sin lectura) | Arregla el cableado, o fuerza el armado (la zona queda entonces excluida y anotada) |
| Se rechaza el PIN aunque sea correcto | La central está bloqueada tras intentos fallidos (se rechaza incluso el PIN correcto) | Espera `lockout_s`; el bloqueo sobrevive a un reinicio |
| El reinicio con BOOT no hace nada | La central está armada: el reinicio solo borra una central desarmada | Desarma primero con el PIN |""",
      "structure": r"""<p align="center">
  <img src="images/repository-structure.svg" alt="Estructura del repositorio de ARMOR-NODE-ALARM" width="100%">
</p>

<details>
<summary>Versión en texto del árbol</summary>

```text
ARMOR-NODE-ALARM/
├── main/                                el firmware: un componente de ESP-IDF
├── core/                                la lógica sin ESP-IDF, probada en un ordenador
├── panel/                               el panel web embebido en el firmware
├── tests/                               pruebas de host y comprobaciones Python
├── docs/                                11 guías: seguridad, mensajes, Zigbee, relevo
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

* La conversación Zigbee del propio nodo con un coordinador, local o en la red, solo se ha probado contra un coordinador simulado; nunca se ha encontrado con un coordinador o un sensor reales.
* El panel web se ha ejercitado en un navegador real contra un nodo simulado, no en una placa.
* Ninguna placa construida, ninguna zona cableada y ninguna sirena o coordinador Zigbee conectados: nada ha funcionado en una instalación real.
* El PIN con bloqueo, el código de configuración, el límite de accesos y las actualizaciones firmadas están probados en el host; no ha habido una revisión independiente y esto no es un sistema de alarma certificado.
* Las comprobaciones de hash y de firma Ed25519 y la lógica de vuelta atrás pasan en el host; una actualización por aire nunca se ha ejecutado en una placa.
* La sirena y los relés los gobiernan las reglas de la alarma y se han probado contra simulaciones; ninguno se ha conectado a una sirena o un relé reales.

**Lo siguiente**

* Cablear lazos y una sirena reales, probar el enlace Zigbee con un coordinador y sensores reales, y ejecutar la central en una instalación real antes de afirmar nada más.""",
    },
  },
  "de": {
    "tagline": "Alarmknoten und Alarmzentrale: die Zonen, das Scharfschalten, die Verzögerungen, die Sirene und die PIN der Hausalarmanlage, mit der Firmware des Knotens und den auf einem Rechner getesteten Regeln (nichts lief auf einer Platine)",
    "honest": "Es existiert der **Alarmkern** (was eine Zone ist, wie eine vom ADC gelesene verdrahtete Schleife zum Zustand wird, die Regeln der Zentrale: Scharfschalten, Verzögerungen, der Alarm, die Sirene, die PIN mit Sperre) und die darauf gebaute **Firmware des Knotens** (Einstellungen, Web-Panel, Nachrichten mit dem Server, die Brücke des Zigbee-Funkmoduls, ein Zigbee-Koordinator im Netzwerk, Relais, Bluetooth, signierte Updates), die für beide Platinen baut; der Kern, die Einstellungen, die Nachrichten und das Panel in einem echten Browser gegen einen Ersatzknoten werden auf einem Computer mit 488.930 Prüfungen in 18 Testprogrammen getestet. **Nichts lief auf einer Platine oder einer echten Anlage, keine Zone wurde verdrahtet und keine Sirene angeschlossen, die Zigbee-Kommunikation des Knotens mit einem Koordinator (lokal oder im Netzwerk) ist geschrieben und gegen einen Ersatzkoordinator getestet, lief aber nie gegen einen echten Koordinator oder Sensor, und dies ist keine zertifizierte Alarmanlage.**",
    "glance": [
      [
        "Rolle",
        "Alarmzentralen-Feldknoten für ESP32-S3 (Familie: Field Nodes, übergeordnet: ARMOR-COMMON)",
      ],
      [
        "Technik",
        "C++17, ESP-IDF 5.5.5, ESP32-S3",
      ],
      [
        "Tests",
        "488930 Prüfungen in 18 Host-Programmen und 5 Python-Prüfungen (`ctest`)",
      ],
      [
        "Eingänge",
        "Bis zu 8 verdrahtete Schleifen, Zigbee-Sensoren (IAS Zone) und Sirene (IAS WD), 4 Tasten",
      ],
      [
        "Läuft auf",
        "Eine ESP32-S3-Platine (Ethernet oder WLAN) mit Basisplatine; Host-Tests auf jedem Computer",
      ],
      [
        "Auf echter Hardware",
        "Noch keiner: keine Platine, Zone, Sirene oder kein Zigbee-Koordinator angeschlossen (nur Computertests, der Build und das Panel im Browser)",
      ],
      [
        "Lizenz",
        "GPL-3.0-or-later",
      ],
    ],
    "status": {
      "software": "Die Firmware wird im ESP-IDF-5.5.5-Container für beide Platinen (WLAN und Ethernet) gebaut.",
      "tests": "488.930 Prüfungen in 18 Host-Programmen bestehen (`ctest`): die Zonen, die vom ADC gelesenen verdrahteten Schleifen, die Regeln für Scharfschalten, Verzögerungen, Sirene und PIN, die Einstellungen und die Nachrichten.",
      "protocols": "Die Zigbee-Kommunikation des Knotens selbst mit einem Koordinator, lokal oder im Netz, ist nur gegen einen nachgebildeten Koordinator getestet; sie ist nie auf einen echten Koordinator oder Sensor getroffen.",
      "ui": "Das Web-Panel wurde in einem echten Browser gegen einen nachgebildeten Knoten erprobt, nicht auf einer Platine.",
      "hardware": "Keine Platine gebaut, keine Zone verdrahtet und weder Sirene noch Zigbee-Koordinator angeschlossen: Bisher lief nichts an einer echten Anlage.",
      "security": "Die PIN mit Sperre, der Einrichtungscode, die Anmeldebegrenzung und die signierten Aktualisierungen sind auf dem Host getestet; es gab keine unabhängige Prüfung, und dies ist kein zertifiziertes Alarmsystem.",
      "updates": "Die Hash- und Ed25519-Signaturprüfungen und die Rückfalllogik bestehen auf dem Host; eine Aktualisierung über die Luft wurde nie auf einer Platine ausgeführt.",
      "writing": "Die Sirene und die Relais werden von den Alarmregeln gesteuert und gegen Nachbildungen getestet; keines wurde an eine echte Sirene oder ein echtes Relais angeschlossen.",
      "integration": "Die Nachrichten des Knotens werden gegen die gemeinsamen Schemas und Konformitätsvektoren von ARMOR-COMMON geprüft.",
      "docs": "Acht Sprachen, die Firmware-Anleitung, die Verdrahtungshinweise und das Änderungsprotokoll sind aktuell.",
    },
    "docs": [
      "[Sicherheit](docs/SAFETY.md): was das Panel verspricht und was nicht",
      "[Alarmnachrichten](docs/ALARM_MESSAGES.md), [Zigbee](docs/ZIGBEE.md) und [Ausfallübernahme](docs/FAILOVER.md)",
      "[Entwurf](docs/DESIGN.md), [Hardware](docs/HARDWARE.md), [Basisplatine](docs/BASE_BOARD.md) und [Knoten-Firmware](docs/NODE_FIRMWARE.md)",
      "[Prüfstandtests](docs/BENCH_TESTS.md), [Einrichtungscode](docs/SETUP_CODE.md) und [Bluetooth-Einrichtung](docs/BLE_PROVISIONING.md)",
    ],
    "contributing_first": "Führe vor einem Pull Request `ctest --test-dir build/host` and `python -I tools/armor_ci_validate.py` aus: Es muss bestehen. Siehe [CONTRIBUTING.md](CONTRIBUTING.md) und den [Verhaltenskodex](CODE_OF_CONDUCT.md).",
    "languages_extra": "",
    "body": {
      "overview": r"""* **Zonen:** vier Arten - *sofort* (eine Tür, ein Fenster), *Eingang* (die Tür, durch die man hereinkommt: sie startet die Eingangsverzögerung), *Innenraum* (Bewegung: nur bei „abwesend“) und *immer* (Rauch, Gas, Panik: scharf oder nicht). Eine Zone kann eine verdrahtete Schleife oder ein Zigbee-Sensor sein.
* **Die verdrahtete Schleife:** ein Kontakt mit Abschlusswiderstand, als Spannung gelesen, ergibt vier Zustände an einem Pin - normal, ausgelöst und Sabotage bei kurzgeschlossenem oder durchtrenntem Draht. Die Grenzwerte sind Einstellungen; ein Entpreller verhindert, dass ein prellender Kontakt den Alarm auslöst.
* **Die Zentrale:** Scharfschalten *abwesend* und *anwesend*, eine Ausgangsverzögerung, die den Gehenden nicht als Eindringling behandelt, eine Eingangsverzögerung, ein Alarm, der **bis zum richtigen Unscharfschalten bleibt**, eine Sirene, die nach einer Zeit von selbst aufhört, das Überbrücken offener Zonen bei Erzwingen (nie ein ertönender Rauchmelder) und ein Protokoll der letzten hundert Ereignisse.
* **Die PIN:** zum Scharfschalten ist keine nötig, zum Unscharfschalten und Stummschalten schon; falsche PINs werden gezählt, und nach einigen wird alles eine Weile abgelehnt, auch die richtige PIN.
* **Stummschalten ohne Unscharfschalten:** solange die Sirene ertönt, stoppt eine richtige PIN sie sofort bei weiterhin scharfem System - der Alarm bleibt verriegelt und gespeichert, eine Zone, die noch nicht ausgelöst hat, kann sie erneut ertönen lassen, und eine falsche PIN zählt für die Sperre wie eine falsche PIN beim Unscharfschalten.
* **Der Plan:** ein Gateway auf der Platine des Elektroknotens (Zigbee-Funk, verdrahtete Zonen, Sirenenrelais), das mit ARMOR-SERVER arbeitet und **weiter überwacht, wenn der Server fehlt**: eine Zentrale übernimmt das Funkmodul vom Server über die Zigbee-Brücke von ARMOR-NODE-ELECTRICAL. Siehe [den Entwurf](docs/DESIGN.md) und [die Übernahme](docs/FAILOVER.md).
* **Der Knoten:** Firmware für den ESP32-S3 (PoE-Ethernet oder WLAN) mit bis zu acht verdrahteten Zonen, der Sirene an einem Relais, dem Webpanel aller Knoten in acht Sprachen, dem an Zigbee2MQTT verliehenen Zigbee-Funk und den Nachrichten `armor/alarm/<Knoten>/state|command|result`; der Server darf nur scharf- und unscharfschalten, wenn drei unabhängige Schalter es erlauben. Siehe [die Firmware](docs/NODE_FIRMWARE.md), [die Nachrichten](docs/ALARM_MESSAGES.md) und [die Hardware](docs/HARDWARE.md).
* **Funkmodul übernehmen:** ist Zigbee2MQTT des Servers eine festgelegte Zeit weg, startet der Knoten den Koordinator selbst (ZNP), liest die Sensoren der Zonen, die einen nennen (IAS Zone), und steuert Zigbee-Sirenen (IAS WD); er gibt es frei, sobald der Client zurück ist.
* **Noch nicht:** ein echter Koordinator oder Sensor, die Hardware und jeder Test an einer echten Anlage.
* **Ein Neustart schaltet das Haus nicht unscharf:** Modus, ein laufender Alarm und die ausgeschlossenen Zonen werden im Flash gehalten und beim Start zurückgeholt; eine unterbrochene oder kurzgeschlossene Schleife wird nie ausgeschlossen; Nachrichten laufen über eine Warteschlange (kein Deadlock mit dem Broker), und der Watchdog startet die Platine neu, wenn die Aufgabe, die die Zonen liest, stehen bleibt.
* **Signierte Over-the-Air-Updates:** der Knoten installiert von GitHub nur ein Abbild, dessen SHA-256 stimmt und das eine gültige Ed25519-Signatur des Betreuers trägt (der öffentliche Schlüssel steckt in der Firmware, der private verlässt den Betreuer nie); eine von einem Administrator im Panel von Hand hochgeladene Datei wird weiterhin akzeptiert. Seiten und Meldungen des Panels sind in acht Sprachen.
* **Bluetooth-Kopplung mit PIN:** die sechsstellige PIN wird aus dem Einrichtungscode abgeleitet, auf der USB-Konsole ausgegeben und einem Administrator im Panel angezeigt; das Telefon muss sie eingeben, bevor es die Einstellungen des Knotens schreiben darf.
* **Sirene und Neustarts:** Das Sirenenrelais gehört allein der Alarmanlage (weder Broker noch Zentrale noch Panel können es bewegen, und es öffnet sich beim Verlust des Brokers nicht); eine Zone, die noch nicht gelöst hatte, lässt die Sirene nach ihrer Zeit erneut ertönen; nach einem Neustart kehren ein Rauch- oder Panikalarm bei unscharfem System, ein stummgeschalteter Alarm und eine Sperre zurück; ein Zurücksetzen von Hand wird bei scharfer Anlage abgelehnt; ein Zigbee-Sensor, der nie spricht, gilt als verloren.
* **Nur das Haus darf das Panel nutzen:** Das Panel antwortet standardmäßig dem privaten Netz (oder den Netzen, die der Besitzer nennt, etwa einem VPN), lehnt eine Liste ab, die den Speichernden aussperren würde, zählt falsche Passwörter je Person und je Adresse und funktioniert hinter dem Proxy des Servers, sodass man es von außerhalb des Hauses erreicht, ohne den Knoten zu veröffentlichen.
* **Eine Zone, die sich nicht lesen lässt, gilt nicht als geschlossen:** startet der Wandler nicht oder liefert eine Schleife fünf Runden lang keinen Wert, steht die Zone auf *Störung* (trouble) - sie überwacht nicht, löst nie die Sirene aus, verhindert das Scharfschalten (außer erzwungen; dann wird sie ausgelassen und vermerkt) und der Server warnt.
* **Optionale verschlüsselte Verbindung zum Broker (TLS):** standardmäßig aus, der Knoten spricht also wie bisher unverschlüsseltes MQTT. Ein Schalter und ein Feld für das Zertifikat der eigenen Zertifizierungsstelle der Anlage (PEM, höchstens 2 KB) auf der Broker-Seite sorgen dafür, dass er sich mit `mqtts://` verbindet, nur dieser Stelle vertraut und prüft, ob das Zertifikat des Brokers für die erreichte Adresse ausgestellt wurde; alles, was nicht genau ein PEM-Zertifikat ist, wird abgelehnt. Durch Host-Tests abgedeckt; der Handshake wurde auf einer Platine noch nicht ausgeführt.
* **Scharfschaltprofile:** Ein Scharfschaltbefehl kann ein Profil tragen (Abwesend, Zuhause, Nacht, eigenes), das für dieses Scharfschalten festlegt, welche Zonen überwachen, welche sofort oder nach der Eingangsverzögerung alarmieren, die Ausgangs- und Eingangsverzögerung und ob die Sirene ertönt (ein stiller Alarm bleibt verriegelt, protokolliert und gemeldet). Es berührt nie Rauch-, Panik- oder Sabotagezonen, die PIN, die Sperre, das Stummschalten, ein erzwungenes Scharfschalten oder eine Zone mit Störung; das Profil übersteht einen Neustart, und ein Scharfschalten ohne Profil verhält sich genau wie zuvor. Getestet gegen die alten Regeln mit einem Zufallslauf und gegen den gemeinsamen Vertrag.
* **Zustandsbericht:** etwa einmal pro Minute veröffentlicht der Knoten, wie lange er läuft und warum er zuletzt neu gestartet ist, seinen freien Speicher, seine Verbindung und sein WLAN-Signal, wie oft er sich mit dem Broker verbunden hat und den letzten protokollierten Fehler (`armor/health/<Knoten>`, der Vertrag `node_health` von ARMOR-COMMON). Der Code, der ihn erzeugt, wird von allen Knoten geteilt und auf einem Computer getestet; auf einer Platine ist er noch nicht gelaufen.
* **Steuerung vom Server aus:** Studio kann den Knoten sauber neu starten, bis zu einer Stunde pausieren (er läuft von selbst weiter), seine Arbeit in den Standby setzen (ohne Ende, über Neustarts hinweg gespeichert, der Knoten bleibt verbunden und antwortet weiter), ihn sich zeigen lassen, einen Diagnose-Schnappschuss anfordern und ihn als in Wartung markieren (`armor/control/<Knoten>/...`, der Vertrag `node_control` von ARMOR-COMMON). Jeder Befehl besteht aus zwei Schritten mit einem Einmal-Token, das zu dieser Operation gehört; nur der Server darf sie am Broker schreiben, und es gibt kein Zurücksetzen auf Werkseinstellungen, kein Löschen und keinen Tiefschlaf. Solange der Knoten pausiert oder im Standby ist, werden seine Zonen nicht gelesen, nichts wird ausgewertet, scharf geschaltet oder ausgelöst, kein Zustand wird veröffentlicht und das Sirenenrelais bleibt offen: Das Haus ist NICHT geschützt, und der Gesundheitsbericht sagt es. Der Code wird von allen Knoten geteilt und auf einem Rechner getestet; auf einer Platine ist er noch nicht gelaufen.
* **Diagnose ohne Kabel:** Nach einem unsauberen Start (Absturz, Watchdog, Spannungseinbruch, fehlgeschlagene Speicherreservierung) nennt der Gesundheitsbericht zehn Minuten lang den Grund; ein Absturz hinterlässt sein Core-Dump, das man im Panel ansehen, herunterladen oder löschen kann; die gespeicherten Einstellungen werden vor jeder Firmware-Installation kopiert und wiederhergestellt, falls ein Update sie beschädigt; und ein Administrator kann den Knoten über den Server mit einem Einmal-Token nach einem Diagnosepaket oder seinem Protokoll fragen.
* **Die Sicherheitsoptionen des Servers:** Die Zentrale wendet die Optionen an, die der Server für sie führt (`armor/alarm/<Knoten>/policy`), und jede lässt sich am Knoten selbst festlegen: Der gespeicherte scharfe Zustand ist an Zonen und PIN gebunden, die Zigbee-Zonenmeldungen des Servers lassen sich abschalten und werden, wenn sie signiert sind, geprüft (Signatur mit einem im Panel eingegebenen Schlüssel und eine nur steigende Folgenummer). Auf einem Computer gegen die Werte getestet, die Vertrag und Server berechnen; nicht auf einem Board ausgeführt.
* **Optionales Versiegeln gespeicherter Geheimnisse:** standardmäßig aus (`security.seal_secrets` oder `nodes.nvs_encryption` des Servers). Eingeschaltet werden die Passwörter, Token, Schlüssel, PINs und Passwort-Hashes, die der Knoten speichert, mit ChaCha20-Poly1305 versiegelt, alles andere bleibt lesbar; Ein- und Ausschalten schreibt sie ohne Verlust um, auch wenn der Knoten mittendrin stehen bleibt. Es wird kein eFuse gebrannt und der Flash nicht verschlüsselt: Der Schlüssel liegt in einer Partition desselben Chips und schützt daher **nicht** vor jemandem, der die Platine hat; ein Knoten, der vor dieser Partition installiert wurde, behält seine Geheimnisse unverändert, bis er mit der neuen Partitionstabelle geflasht wird.""",
      "role": r"""ARMOR-NODE-ALARM ist die Alarmzentrale: Zonen, Scharfschalten, Verzögerungen, Sirene und PIN werden auf dem Knoten selbst entschieden, sodass das Haus bewacht bleibt, wenn der Server fehlt. [ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER) zeigt sie, ordnet Zigbee-Sensoren ihren Zonen zu und schaltet sie, wenn Sie es erlauben, scharf und unscharf; das Menü *Alarmzentralen* und der *Alarm-Designer* von [ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) sowie die App [ARMOR-ANDROID-CONTROL](https://github.com/JuanenRac/ARMOR-ANDROID-CONTROL) steuern sie. Ihr Zigbee-Funkmodul kann auf der Platine sein oder ein Koordinator im Netzwerk.

| Name | Wie | Wozu |
|---|---|---|
| ARMOR-SERVER | MQTT `armor/alarm/<id>/{state,command,result,zigbee,policy}` | Empfängt den Zustand der Zentrale; ordnet Scharf-, Unscharfschalten und Stummschalten nur hinter drei Schaltern an |
| ARMOR-STUDIO | Menü Alarmzentralen | Zeigt die Zonen, die Ereignisse und die Richtlinie und öffnet das Panel des Knotens |
| ARMOR-ANDROID-CONTROL | Bluetooth | Richtet den Knoten vor Ort ein und zeigt die Alarmzentralen |
| ARMOR-COMMON | Alarm-Vertrag | Die Nachrichten werden gegen seine Schemas geprüft; die gemeinsame Firmware stammt daraus |""",
      "architecture": r"""<p align="center">
  <img src="images/architecture.svg" alt="Architektur von ARMOR-NODE-ALARM: wer es aufruft, was es enthält und wovon es abhängt" width="100%">
</p>""",
      "security": r"""| Bedrohung | Abwehr |
|---|---|
| Passwörter im Klartext oder einkompiliert | PBKDF2-HMAC-SHA256 mit 10 000 Runden; kein Passwort in der Firmware (ein Knoten ohne Benutzer geht in die Einrichtung); höchstens 4 Benutzer (Admin oder Betrachter) und 8 bis 64 Zeichen; höchstens 6 Sitzungen, 30 Minuten Leerlauf |
| Einen frisch geflashten Knoten übernehmen | Die Einrichtung braucht einen Startcode: den des Builds (`CONFIG_ARMOR_SETUP_CODE`) oder einen zufälligen im Flash, der auf der USB-Konsole erscheint; mit Flottengeheimnis ist er `HMAC-SHA256(Geheimnis, MAC)`; er ist auch der Schlüssel des Einrichtungs-WLANs (WPA2, nie überbrückt) |
| Das Panel aus dem Internet erreicht | Es antwortet standardmäßig den privaten Netzen eines Hauses (10/8, 172.16/12, 192.168/16, 169.254/16, 127/8 und 100.64/10, wo manche VPNs liegen); die Einstellung `web.admin_sources` listet weitere IPv4-Adressen und Netze (8 Einträge, 120 Zeichen); alles außerhalb wird abgewiesen außer der öffentlichen Identität `GET /api/v1/session`; eine Liste, die den Speichernden aussperren würde, wird abgelehnt |
| Das Panel im Klartext über HTTP | HTTPS auf 443 mit einem vom Knoten selbst erzeugten Zertifikat (selbstsigniert, im Flash, SHA-256-Fingerabdruck zum Vergleichen sichtbar); das Panel kann http, https oder beides sein; das Sitzungscookie ist immer HttpOnly und SameSite=Strict (und Secure über TLS) |
| Eine gefälschte Firmware von GitHub | Ein Image wird nur mit passendem SHA-256 und gültiger Ed25519-Signatur mit dem Schlüssel des Maintainers installiert (`no_checksum`, `no_signature`, `bad_signature`, `checksum_mismatch`, `wrong_firmware`, `not_newer`, `version_mismatch` lehnen es ab); ein manueller Upload durch einen Administrator wird nicht geprüft: eine ausdrückliche Grenze |
| Kapern der Bluetooth-Einrichtung | Eine 6-stellige PIN, abgeleitet vom Einrichtungscode, auf der USB-Konsole und für einen Administrator sichtbar; das Telefon muss sie vor dem Schreiben von Einstellungen eingeben; das Einrichtungsfenster dauert `CONFIG_ARMOR_BLE_SETUP_MINUTES` (standardmäßig 10, 1 bis 120) |
| Gespeicherte Geheimnisse, gelesen von jemandem mit der Platine | Optional (standardmäßig aus, Schalter `security.seal_secrets` oder `nodes.nvs_encryption` des Servers): ChaCha20-Poly1305 für Passwörter, Token, Schlüssel, PINs und Hashes. Es verschlüsselt nicht den Flash und brennt kein eFuse: Der Schlüssel liegt in einer Partition desselben Chips und schützt daher nicht vor dem, der die Platine hat |
| Die Broker-Verbindung im Klartext | Optionales TLS (`mqtts://`) mit der eigenen Zertifizierungsstelle des Besitzers (PEM bis 2 KB) und Namensprüfung; standardmäßig aus. Der Handshake lief nur in Host-Tests, nicht auf einer Platine |
| Erraten der Panel-PIN | Der Vergleich verrät nicht, wo er abweicht; aufeinanderfolgende Fehler sperren das Panel für `lockout_s` (standardmäßig 60 s, 1 bis 3600) mal 1, 5 und 15 bei den ersten drei Sperren, auch für die richtige PIN; eine laufende Sperre wird nach einem Neustart wiederhergestellt; Scharfschalten braucht keine PIN, Unscharfschalten und Stummschalten schon |
| Ein Neustart, der das Haus unscharf macht | Der Modus, der laufende Alarm und die ausgeschlossenen Zonen werden im Flash gehalten und wiederhergestellt; eine unterbrochene oder kurzgeschlossene Schleife wird nie ausgelassen; Rauch, Panik und Sabotage, die im unscharfen Zustand ausgelöst haben, kommen nach einem Neustart zurück; der BOOT-Reset löscht nur bei UNSCHARFEM Panel |
| Eine nicht lesbare Zone sieht geschlossen aus | Sie zeigt `trouble` (der Wandler startet nicht oder 5 Runden ohne Messwert), und das Panel schaltet mit ihr nur erzwungen scharf, dann wird sie ausgeschlossen und vermerkt; ein klingelnder Rauch- oder Panikmelder wird nie ausgeschlossen |
| Ein Befehl vom Server, den niemand erlaubt hat | Scharf-, Unscharfschalten und Stummschalten vom Server brauchen DREI Schalter (die Knoteneinstellung, die Zugriffsliste des Brokers und `ARMOR_ALARM_COMMANDS=1` am Server), der Server fragt die PIN des Benutzers vor dem Senden eines Unscharf- oder Stummbefehls, und alles ist standardmäßig aus; das Sirenenrelais gehört allein dem Alarm (Broker, Zentrale und Panel können es nicht bewegen) |
| Gefälschte Zigbee-Nachrichten | Das Topic `armor/alarm/<id>/zigbee` trägt einen HMAC-SHA256 über Knoten, Zone, Zustand, Batterie und Folgenummer mit dem Schlüssel der Zentrale (64 Hex, im Panel eingetippt), und die Folgenummer steigt nur; das Richtlinien-Topic trägt `config_hash`, `zone_feed` und seine Signatur, die jeweils am Knoten festgelegt werden können |

Dies ist kein zertifiziertes Alarmsystem ([docs/SAFETY.md](docs/SAFETY.md)): Es ist ein Heimprojekt und lief nie auf einer Platine oder in einer echten Installation. Fehlt der Server, entscheidet die Zentrale allein, und fällt zusätzlich der Knoten oder sein Funkmodul aus, überwacht niemand. Lies [SECURITY.md](SECURITY.md), um eine Schwachstelle zu melden.""",
      "interfaces": r"""| Teil | Was sie festlegt |
|---|---|
| MQTT | `armor/alarm/<id>/state` (nicht retained: Zonen mit ID, Name, Art, Zustand und Überbrückung, die Phase), `/command`, `/result`, `/zigbee` und `/policy` (Server zur Zentrale); `armor/device/<id>/<Relais>/{state,set}`, `armor/health/<id>`, `armor/control/<id>/...` |
| Zonen | Art `instant`, `entry`, `interior` oder `always`; Zustand `normal`, `triggered`, `tamper` oder `trouble`; bis zu 8 verdrahtete Schleifen (ein Kontakt mit Abschlusswiderstand, vom ADC gelesen, ergibt vier Zustände an einem Pin; die Ethernet-Platine hat 6 gültige Analogpins, die WLAN-Platine 8), 4 Tasten und ein Protokoll von 100 Ereignissen |
| Zigbee | Eine serielle Brücke (ZNP) zu einem Koordinator, IAS-Zone-Sensoren und IAS-WD-Sirenen; der Knoten übernimmt das Funkmodul, wenn der Zigbee2MQTT des Servers `zigbee_silence_min` lang schweigt, und gibt es zurück, wenn der Server wiederkommt ([docs/ZIGBEE.md](docs/ZIGBEE.md), [docs/FAILOVER.md](docs/FAILOVER.md)) |""",
      "configuration": r"""| Variable | Standard | Was sie festlegt |
|---|---|---|
| `panel.exit_delay_s`, `panel.entry_delay_s` | 30, 30 (0-600) | Die Ausgangs- und Eingangsverzögerung; beim Gehen gilt die Person nicht als Eindringling |
| `panel.lockout_s` | 60 (1-3600) | Die PIN-Sperre, mal 1, 5 und 15 bei den ersten drei |
| `zigbee_silence_min` | - | Wie lange das Zigbee des Servers schweigen darf, bevor der Knoten das Funkmodul übernimmt |
| `CONFIG_ARMOR_NODE_ID`, `_SETUP_CODE`, `_FLEET_SECRET`, `_MQTT_*`, `_HEARTBEAT_S`, `_BLE_SETUP_MINUTES`, `_BOOT_FACTORY_RESET` | - | Die Einstellungen, die alle Knoten teilen: der Name (leer ergibt `armor-` und die letzten Bytes der MAC), der Einrichtungscode (leer: zufällig), das Flottengeheimnis (16+ Zeichen, nie im Repository), die ersten Broker-Einstellungen, der Herzschlag (2 bis 300 s), die Minuten der Bluetooth-Einrichtung (1 bis 120) und der Reset mit BOOT (8 s in den ersten 30 s) |

Erneutes Auslösen nach einem Stummschalten ist auf 3 begrenzt (`kMaxResounds`). Das Sirenenrelais startet bei jedem Neustart offen und fällt nicht auf offen, wenn der Broker verloren geht.""",
      "quickstart": r"""**Voraussetzungen:** ein C++17-Compiler für die Host-Tests; der ESP-IDF-5.5.5-Container zum Bauen des Images; eine ESP32-S3-Platine (Ethernet oder WLAN) mit der Basisplatine.

```bash
cmake -S tests -B build/host && cmake --build build/host && ctest --test-dir build/host   # host tests, -Werror
node tools/panel_mock.mjs --user admin:adminpass123   # the panel without a board
tools/build_node.sh generic s3-wifi                  # the image in the ESP-IDF container (or s3-eth)
```

Siehe [den Entwurf](docs/DESIGN.md), [wie die Zentrale vom Server übernimmt](docs/FAILOVER.md) und die [Sicherheitshinweise](docs/SAFETY.md).""",
      "testing": r"""```bash
cmake -S tests -B build/host && cmake --build build/host && ctest --test-dir build/host
python -I tools/armor_ci_validate.py
```

18 Host-Testprogramme und 5 Python-Prüfungen laufen unter `ctest`; 488930 Prüfungen, gezählt von den Host-Programmen, mit `-Werror` gebaut.

Python-Prüfungen: die Panel-Texte in acht Sprachen, die Tasks, die Speicherpfade, die Bluetooth-Sitzung unter ihrer Sperre und die vom Panel aufgerufenen Routen (und in manchen Knoten die HTTP-Codes oder die Glyphen der Schriften)

Die Host-Tests brauchen einen beliebigen C++17-Compiler (Linux, WSL, MSYS2); das Web-Panel wird außerdem in einem echten Browser gegen einen Ersatzknoten geprüft (`tools/panel_mock.mjs`, `tools/panel_browser_test.mjs`).

Die meisten Prüfungen sind erschöpfende Durchläufe der Panel-Regeln; Schleifen, Sirene und Zigbee-Verbindung sind Ersatz.""",
      "build": "`tools/build_node.sh` baut das Image im ESP-IDF-5.5.5-Container, und die Version trägt das Image, sein SHA-256 und seine Ed25519-Signatur, je eines pro Platine; das Image wird beim ersten Mal per USB-C geschrieben und danach vom Panel aktualisiert.",
      "troubleshooting": r"""| Sie sehen | Weil | Tun Sie |
|---|---|---|
| Du hast das Passwort verloren oder der Knoten tritt dem Netz nicht mehr bei | Ein Knoten in der Einrichtung ohne Adresse nach 90 s öffnet ein eigenes WLAN `ARMOR-SETUP-xxxxxx` (öffne `http://192.168.4.1/`) | Zum Neustart BOOT 8 Sekunden in den ersten 30 Sekunden nach dem Einschalten halten (löscht Einstellungen und Benutzer) oder im Panel *Werksreset* nutzen |
| Ein Update von GitHub wird abgelehnt | Die Version enthält keine Prüfsumme oder Signatur, sie passen nicht (`e_no_checksum`, `e_no_signature`, `e_checksum_mismatch`, `e_bad_signature`), hat kein Image für diese Platine (`e_no_asset_for_board`) oder gehört zu einem anderen Projekt (`e_wrong_firmware`) | Der Knoten blieb unverändert; erneut versuchen oder einen Administrator die Datei von Hand hochladen lassen |
| Das Panel schaltet nicht scharf | Eine Zone steht auf `trouble` (der Wandler startet nicht oder 5 Runden ohne Messwert) | Behebe die Verdrahtung oder erzwinge das Scharfschalten (die Zone wird dann ausgeschlossen und vermerkt) |
| Die PIN wird abgelehnt, auch wenn sie stimmt | Das Panel ist nach Fehlversuchen gesperrt (auch die richtige PIN wird abgelehnt) | Warte `lockout_s`; die Sperre überlebt einen Neustart |
| Der BOOT-Reset bewirkt nichts | Das Panel ist scharf: Der Reset löscht nur ein unscharfes Panel | Zuerst mit der PIN unscharf schalten |""",
      "structure": r"""<p align="center">
  <img src="images/repository-structure.svg" alt="Repository-Struktur von ARMOR-NODE-ALARM" width="100%">
</p>

<details>
<summary>Textversion des Baums</summary>

```text
ARMOR-NODE-ALARM/
├── main/                                die Firmware: eine ESP-IDF-Komponente
├── core/                                die Logik ohne ESP-IDF, am Rechner getestet
├── panel/                               das in die Firmware eingebettete Web-Panel
├── tests/                               Host-Tests und Python-Prüfungen
├── docs/                                11 Anleitungen: Sicherheit, Nachrichten, Zigbee, Ausfallübernahme
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

* Die Zigbee-Kommunikation des Knotens selbst mit einem Koordinator, lokal oder im Netz, ist nur gegen einen nachgebildeten Koordinator getestet; sie ist nie auf einen echten Koordinator oder Sensor getroffen.
* Das Web-Panel wurde in einem echten Browser gegen einen nachgebildeten Knoten erprobt, nicht auf einer Platine.
* Keine Platine gebaut, keine Zone verdrahtet und weder Sirene noch Zigbee-Koordinator angeschlossen: Bisher lief nichts an einer echten Anlage.
* Die PIN mit Sperre, der Einrichtungscode, die Anmeldebegrenzung und die signierten Aktualisierungen sind auf dem Host getestet; es gab keine unabhängige Prüfung, und dies ist kein zertifiziertes Alarmsystem.
* Die Hash- und Ed25519-Signaturprüfungen und die Rückfalllogik bestehen auf dem Host; eine Aktualisierung über die Luft wurde nie auf einer Platine ausgeführt.
* Die Sirene und die Relais werden von den Alarmregeln gesteuert und gegen Nachbildungen getestet; keines wurde an eine echte Sirene oder ein echtes Relais angeschlossen.

**Als Nächstes**

* Echte Schleifen und eine Sirene verdrahten, die Zigbee-Verbindung mit einem echten Koordinator und Sensoren erproben und das Panel in einer echten Installation betreiben, bevor mehr behauptet wird.""",
    },
  },
  "fr": {
    "tagline": "Nœud et centrale d'alarme : les zones, l'armement, les temporisations, la sirène et le code PIN de l'alarme de la maison, avec le firmware du nœud et les règles testées sur un ordinateur (rien n'a tourné sur une carte)",
    "honest": "Ce qui existe, c'est le **cœur de l'alarme** (ce qu'est une zone, comment une boucle câblée lue par l'ADC devient un état, les règles de la centrale : armement, temporisations, l'alarme, la sirène, le PIN avec verrouillage) et le **firmware du nœud** construit dessus (réglages, panneau web, messages avec le serveur, le pont de la radio Zigbee, un coordinateur Zigbee sur le réseau, relais, Bluetooth, mises à jour signées), qui se compile pour les deux cartes ; le cœur, les réglages, les messages et le panneau dans un vrai navigateur contre un nœud factice sont testés sur un ordinateur avec 477 588 vérifications dans 6 programmes de test. **Rien n'a tourné sur une carte ni sur une installation réelle, aucune zone n'a été câblée ni aucune sirène connectée, la conversation Zigbee du nœud avec un coordinateur (local ou sur le réseau) est écrite et testée contre un coordinateur factice mais n'a jamais tourné contre un vrai coordinateur ni un vrai capteur, et ce n'est pas un système d'alarme certifié.**",
    "glance": [
      [
        "Rôle",
        "Nœud de terrain centrale d'alarme pour ESP32-S3 (famille : Field Nodes, parent : ARMOR-COMMON)",
      ],
      [
        "Technologie",
        "C++17, ESP-IDF 5.5.5, ESP32-S3",
      ],
      [
        "Tests",
        "488930 vérifications dans 18 programmes hôte et 5 contrôles Python (`ctest`)",
      ],
      [
        "Entrées",
        "Jusqu'à 8 boucles câblées, capteurs Zigbee (IAS Zone) et sirène (IAS WD), 4 boutons",
      ],
      [
        "Fonctionne sur",
        "Une carte ESP32-S3 (Ethernet ou Wi-Fi) avec la carte de base ; tests sur hôte sur n'importe quel ordinateur",
      ],
      [
        "Sur matériel réel",
        "Aucun pour l'instant : ni carte, ni zone, ni sirène, ni coordinateur Zigbee connectés (seulement des tests sur ordinateur, la compilation et le panneau dans un navigateur)",
      ],
      [
        "Licence",
        "GPL-3.0-or-later",
      ],
    ],
    "status": {
      "software": "Le firmware compile dans le conteneur ESP-IDF 5.5.5 pour les deux cartes (Wi-Fi et Ethernet).",
      "tests": "488 930 vérifications dans 18 programmes d'hôte réussissent (`ctest`) : les zones, les boucles câblées lues par le CAN, les règles d'armement, de temporisation, de sirène et de PIN, les réglages et les messages.",
      "protocols": "La conversation Zigbee du nœud lui-même avec un coordinateur, local ou sur le réseau, n'est testée que contre un coordinateur simulé ; elle n'a jamais rencontré un vrai coordinateur ni un vrai capteur.",
      "ui": "Le panneau web a été essayé dans un vrai navigateur contre un nœud simulé, pas sur une carte.",
      "hardware": "Aucune carte construite, aucune zone câblée et ni sirène ni coordinateur Zigbee connectés : rien n'a tourné sur une installation réelle.",
      "security": "Le PIN avec verrouillage, le code de configuration, la limite de connexions et les mises à jour signées sont testés sur l'hôte ; il n'y a pas eu de revue indépendante et ce n'est pas un système d'alarme certifié.",
      "updates": "Les contrôles de hash et de signature Ed25519 et la logique de retour arrière réussissent sur l'hôte ; une mise à jour par voie hertzienne n'a jamais été exécutée sur une carte.",
      "writing": "La sirène et les relais sont pilotés par les règles de l'alarme et testés contre des simulations ; aucun n'a été relié à une vraie sirène ou à un vrai relais.",
      "integration": "Les messages du nœud sont validés par rapport aux schémas partagés et aux vecteurs de conformité d'ARMOR-COMMON.",
      "docs": "Huit langues, le guide du firmware, les notes de câblage et le journal des modifications sont à jour.",
    },
    "docs": [
      "[Sécurité](docs/SAFETY.md) : ce que la centrale promet et ce qu'elle ne promet pas",
      "[Messages d'alarme](docs/ALARM_MESSAGES.md), [Zigbee](docs/ZIGBEE.md) et [relève](docs/FAILOVER.md)",
      "[Conception](docs/DESIGN.md), [matériel](docs/HARDWARE.md), [carte de base](docs/BASE_BOARD.md) et [firmware du nœud](docs/NODE_FIRMWARE.md)",
      "[Essais de banc](docs/BENCH_TESTS.md), [code de configuration](docs/SETUP_CODE.md) et [mise en service Bluetooth](docs/BLE_PROVISIONING.md)",
    ],
    "contributing_first": "Avant une pull request, lancez `ctest --test-dir build/host` and `python -I tools/armor_ci_validate.py` : il doit réussir. Voir [CONTRIBUTING.md](CONTRIBUTING.md) et le [code de conduite](CODE_OF_CONDUCT.md).",
    "languages_extra": "",
    "body": {
      "overview": r"""* **Zones :** quatre types - *instantanée* (une porte, une fenêtre), *d'entrée* (la porte par laquelle on entre : elle lance la temporisation d'entrée), *intérieure* (mouvement : seulement en « absent ») et *toujours* (fumée, gaz, panique : armée ou non). Une zone peut être une boucle câblée ou un capteur Zigbee.
* **La boucle câblée :** un contact avec résistance de fin de ligne, lu comme une tension, donne quatre états sur une seule broche - normal, déclenché, et sabotage pour un fil en court-circuit ou coupé. Les seuils sont des réglages ; un filtre anti-rebond évite qu'un contact qui rebondit déclenche l'alarme.
* **La centrale :** armement *absent* et *présent*, une temporisation de sortie qui ne traite pas comme un intrus celui qui part, une temporisation d'entrée, une alarme qui **reste verrouillée** jusqu'à un désarmement correct, une sirène qui s'arrête seule au bout d'un moment, l'inhibition des zones ouvertes si on force (jamais un détecteur de fumée qui sonne) et un journal des cent derniers événements.
* **Le PIN :** l'armement n'en demande pas, le désarmement et l'arrêt de l'alarme si ; les PIN faux sont comptés et, après quelques-uns, tout est refusé un moment, même le bon PIN.
* **Couper la sirène sans désarmer :** tant que la sirène sonne, un PIN correct l'arrête aussitôt alors que le système reste armé - l'alarme reste verrouillée et enregistrée, une zone qui n'a pas encore sonné peut la relancer, et un PIN faux compte pour le verrouillage comme un faux PIN de désarmement.
* **Le plan :** une passerelle sur la carte du nœud électrique (radio Zigbee, zones câblées, relais de sirène) qui travaille avec ARMOR-SERVER et **continue de surveiller quand le serveur est absent** : une centrale reprend la radio au serveur par le pont Zigbee d'ARMOR-NODE-ELECTRICAL. Voir [la conception](docs/DESIGN.md) et [la reprise](docs/FAILOVER.md).
* **Le nœud :** firmware pour l'ESP32-S3 (Ethernet PoE ou Wi-Fi) avec jusqu'à huit zones câblées, la sirène sur un relais, le panneau web de tous les nœuds en huit langues, la radio Zigbee prêtée à Zigbee2MQTT et les messages `armor/alarm/<nœud>/state|command|result` ; le serveur ne peut armer et désarmer que si trois interrupteurs indépendants l'autorisent. Voir [le firmware](docs/NODE_FIRMWARE.md), [les messages](docs/ALARM_MESSAGES.md) et [le matériel](docs/HARDWARE.md).
* **Prendre la radio :** quand Zigbee2MQTT du serveur est absent depuis un temps donné, le nœud démarre lui-même le coordinateur (ZNP), lit les capteurs des zones qui en nomment un (IAS Zone) et commande des sirènes Zigbee (IAS WD), et la rend dès que le client revient.
* **Pas encore :** un vrai coordinateur ou capteur, le matériel et tout essai sur une installation réelle.
* **Un redémarrage ne désarme pas la maison :** le mode, une alarme en cours et les zones exclues sont gardés en flash et repris au démarrage ; une boucle coupée ou en court-circuit n'est jamais exclue ; les messages passent par une file (pas d'interblocage avec le broker) et le chien de garde redémarre la carte si la tâche qui lit les zones s'arrête.
* **Mises à jour par radio signées :** le nœud n'installe depuis GitHub qu'une image dont le SHA-256 correspond et qui porte une signature Ed25519 valide du responsable (la clé publique est dans le firmware, la privée ne quitte jamais le responsable) ; un fichier envoyé à la main par un administrateur dans le panneau reste accepté. Les pages et messages du panneau sont en huit langues.
* **Appairage Bluetooth avec un PIN :** le PIN à six chiffres est dérivé du code de configuration, imprimé sur la console USB et montré à un administrateur dans le panneau ; le téléphone doit le saisir avant de pouvoir écrire les réglages du nœud.
* **Sirène et redémarrages :** le relais de la sirène appartient à l'alarme seule (ni le broker, ni la centrale, ni le panneau ne peuvent le bouger, et il ne s'ouvre pas à la perte du broker) ; une zone qui n'avait pas encore sonné refait sonner la sirène après son délai ; après un redémarrage reviennent une alarme de fumée ou de panique système désarmé, une alarme silencieuse et un blocage ; une réinitialisation à la main est refusée alarme armée ; un capteur Zigbee qui ne parle jamais compte comme perdu.
* **Seule la maison peut utiliser le panneau :** le panneau répond par défaut au réseau privé (ou aux réseaux que son propriétaire indique, comme un VPN), refuse une liste qui exclurait celui qui l'enregistre, compte les mauvais mots de passe par personne et par adresse, et fonctionne derrière le proxy du serveur pour être atteint depuis l'extérieur sans publier le nœud.
* **Une zone illisible n'est pas affichée comme fermée :** si le convertisseur ne démarre pas ou qu'une boucle ne donne aucune lecture pendant cinq tours de suite, la zone passe en *défaut* (trouble) - elle ne surveille pas, ne fait jamais sonner la sirène, empêche l'armement (sauf en le forçant, et elle est alors exclue et notée) et le serveur avertit.
* **Liaison chiffrée facultative avec le broker (TLS) :** désactivée par défaut, le nœud parle donc MQTT non chiffré comme avant. Un interrupteur et une zone pour le certificat de l'autorité propre à l'installation (PEM, 2 Ko au plus) dans la page Broker lui font se connecter en `mqtts://`, ne faire confiance qu'à cette autorité et vérifier que le certificat du broker a été établi pour l'adresse atteinte ; ce qui n'est pas un seul certificat PEM est refusé. Couvert par des tests sur ordinateur ; la poignée de main n'a pas encore été exécutée sur une carte.
* **Profils d'armement :** une commande d'armer peut porter un profil (Absent, Présent, Nuit, le vôtre) qui choisit, pour cet armement, quelles zones surveillent, lesquelles déclenchent l'alarme tout de suite ou après la temporisation d'entrée, les temporisations de sortie et d'entrée et si la sirène sonne (une alarme silencieuse reste verrouillée, notée et signalée). Il ne touche jamais les zones fumée, panique ou sabotage, le PIN, le verrouillage, le silence, un armement forcé ni une zone en défaut ; le profil survit à un redémarrage et un armement sans profil se comporte exactement comme avant. Testé contre les anciennes règles par une exécution aléatoire et contre le contrat partagé.
* **Rapport de santé :** environ une fois par minute le nœud publie depuis combien de temps il tourne et pourquoi il a redémarré la dernière fois, sa mémoire libre, sa liaison et son signal Wi-Fi, combien de fois il s'est connecté au broker et la dernière erreur notée (`armor/health/<nœud>`, le contrat `node_health` d'ARMOR-COMMON). Le code qui le construit est partagé par tous les nœuds et testé sur un ordinateur ; il n'a pas tourné sur une carte.
* **Commande depuis le serveur :** Studio peut redémarrer le nœud proprement, le mettre en pause jusqu'à une heure (il reprend seul), mettre son travail en veille (sans fin, conservée aux redémarrages, le nœud reste connecté et continue de répondre), le faire se signaler, demander un instantané de diagnostic et le marquer en maintenance (`armor/control/<nœud>/...`, le contrat `node_control` d'ARMOR-COMMON). Chaque ordre se fait en deux temps avec un jeton à usage unique propre à cette opération, seul le serveur peut les écrire sur le broker, et il n'existe ni réinitialisation d'usine, ni effacement, ni sommeil profond. Tant que le nœud est en pause ou en veille, ses zones ne sont pas lues, rien n'est évalué, armé ni sonné, aucun état n'est publié et le relais de la sirène reste ouvert : la maison n'est PAS protégée, et le rapport de santé le dit. Le code est partagé par tous les nœuds et testé sur un ordinateur ; il n'a pas tourné sur une carte.
* **Diagnostic sans câble :** après un démarrage qui n'était pas propre (plantage, chien de garde, chute d'alimentation, allocation échouée), le rapport de santé en donne la raison pendant dix minutes ; un plantage laisse son vidage mémoire (core dump) à consulter, télécharger ou effacer depuis le panneau ; les réglages enregistrés sont copiés avant chaque installation de micrologiciel et récupérés si une mise à jour les abîme ; et un administrateur peut demander au nœud, via le serveur, un paquet de diagnostic ou son journal avec un jeton à usage unique.
* **Les options de sécurité du serveur :** la centrale applique les options que le serveur garde pour elle (`armor/alarm/<nœud>/policy`) et chacune peut être fixée sur le nœud lui-même : l'état armé enregistré est lié aux zones et au code PIN, les messages de zone Zigbee du serveur peuvent être coupés et, s'ils sont signés, ils sont vérifiés (signature avec une clé saisie dans le panneau et un numéro de séquence qui ne fait qu'augmenter). Testé sur un ordinateur avec les valeurs que calculent le contrat et le serveur ; non exécuté sur une carte.
* **Scellement facultatif des secrets enregistrés :** désactivé par défaut (`security.seal_secrets`, ou `nodes.nvs_encryption` du serveur). Activé, les mots de passe, jetons, clés, codes PIN et empreintes de mots de passe que le nœud enregistre sont scellés avec ChaCha20-Poly1305 et tout le reste reste lisible ; l'activer ou le désactiver les réécrit sans rien perdre, même si le nœud s'arrête en route. Aucun eFuse n'est brûlé et la flash n'est pas chiffrée : la clé est dans une partition de la même puce, donc cela ne protège **pas** contre quelqu'un qui tient la carte, et un nœud installé avant cette partition garde ses secrets tels quels jusqu'à ce qu'il soit flashé avec la nouvelle table de partitions.""",
      "role": r"""ARMOR-NODE-ALARM est la centrale d'alarme : les zones, l'armement, les temporisations, la sirène et le PIN se décident sur le nœud lui-même, si bien que la maison reste surveillée quand le serveur est absent. [ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER) la montre, lie des capteurs Zigbee à ses zones et, quand vous l'autorisez, l'arme et la désarme ; le menu *Centrales d'alarme* et le *Concepteur d'alarme* d'[ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) et l'application [ARMOR-ANDROID-CONTROL](https://github.com/JuanenRac/ARMOR-ANDROID-CONTROL) la pilotent. Sa radio Zigbee peut être sur la carte ou un coordinateur sur le réseau.

| Nom | Comment | À quoi ça sert |
|---|---|---|
| ARMOR-SERVER | MQTT `armor/alarm/<id>/{state,command,result,zigbee,policy}` | Reçoit l'état de la centrale ; commande l'armement, le désarmement et le silence seulement derrière trois interrupteurs |
| ARMOR-STUDIO | menu des centrales d'alarme | Montre les zones, les événements et la politique, et ouvre le panneau du nœud |
| ARMOR-ANDROID-CONTROL | Bluetooth | Configure le nœud sur le terrain et montre les centrales d'alarme |
| ARMOR-COMMON | contrat d'alarme | Les messages sont vérifiés avec ses schémas ; le firmware commun en est copié |""",
      "architecture": r"""<p align="center">
  <img src="images/architecture.svg" alt="Architecture de ARMOR-NODE-ALARM : qui l'appelle, ce qu'il contient et de quoi il dépend" width="100%">
</p>""",
      "security": r"""| Menace | Défense |
|---|---|
| Mots de passe en clair ou compilés | PBKDF2-HMAC-SHA256 avec 10 000 tours ; aucun mot de passe dans le firmware (un nœud sans utilisateur passe en configuration) ; au plus 4 utilisateurs (admin ou lecteur) et de 8 à 64 caractères ; au plus 6 sessions, 30 minutes d'inactivité |
| Prendre un nœud tout juste flashé | La configuration exige un code de démarrage : celui du build (`CONFIG_ARMOR_SETUP_CODE`) ou un code aléatoire gardé en flash et affiché sur la console USB ; avec un secret de flotte c'est `HMAC-SHA256(secret, MAC)` ; c'est aussi la clé du Wi-Fi de configuration (WPA2, jamais ponté) |
| Le panneau atteint depuis Internet | Il répond par défaut aux réseaux privés d'une maison (10/8, 172.16/12, 192.168/16, 169.254/16, 127/8 et 100.64/10 où vivent certains VPN) ; le réglage `web.admin_sources` liste d'autres adresses et réseaux IPv4 (8 entrées, 120 caractères) ; tout le reste est refusé sauf l'identité publique `GET /api/v1/session` ; une liste qui exclurait celui qui l'enregistre est rejetée |
| Le panneau en clair en HTTP | HTTPS sur le 443 avec un certificat que le nœud fabrique lui-même (autosigné, en flash, empreinte SHA-256 visible pour comparer) ; le panneau peut être http, https ou les deux ; le cookie de session est toujours HttpOnly et SameSite=Strict (et Secure en TLS) |
| Un faux firmware depuis GitHub | Une image n'est installée qu'avec un SHA-256 concordant et une signature Ed25519 valide faite avec la clé du mainteneur (`no_checksum`, `no_signature`, `bad_signature`, `checksum_mismatch`, `wrong_firmware`, `not_newer`, `version_mismatch` la refusent) ; un envoi manuel par un administrateur n'est pas vérifié : une limite explicite |
| Détournement de la configuration Bluetooth | Un PIN à 6 chiffres dérivé du code de configuration, visible sur la console USB et pour un administrateur ; le téléphone doit le saisir avant d'écrire des réglages ; la fenêtre dure `CONFIG_ARMOR_BLE_SETUP_MINUTES` (10 par défaut, de 1 à 120) |
| Secrets stockés lus par qui a la carte | Optionnel (désactivé par défaut, interrupteur `security.seal_secrets` ou `nodes.nvs_encryption` du serveur) : ChaCha20-Poly1305 pour mots de passe, jetons, clés, PIN et hachages. Il ne chiffre pas la flash et ne grille aucun eFuse : la clé est dans une partition de la même puce, il ne protège donc pas contre qui tient la carte |
| Le lien avec le broker en clair | TLS optionnel (`mqtts://`) avec l'autorité propre du propriétaire (PEM jusqu'à 2 Ko) et vérification du nom ; désactivé par défaut. Le handshake n'a tourné qu'en tests sur hôte, pas sur une carte |
| Deviner le PIN de la centrale | La comparaison ne révèle pas où elle diffère ; des échecs consécutifs bloquent la centrale `lockout_s` (60 s par défaut, de 1 à 3600) fois 1, 5 et 15 pour les trois premiers blocages, même pour le bon PIN ; un blocage en cours est restauré après un redémarrage ; armer ne demande pas de PIN, désarmer et faire taire en demandent un |
| Un redémarrage qui désarme la maison | Le mode, l'alarme en cours et les zones exclues sont gardés en flash et récupérés ; une boucle coupée ou en court-circuit n'est jamais laissée de côté ; fumée, panique et sabotage déclenchés pendant le désarmement reviennent après un redémarrage ; la réinitialisation par BOOT n'efface que centrale DÉSARMÉE |
| Une zone illisible semble fermée | Elle montre `trouble` (le convertisseur ne démarre pas ou 5 tours sans lecture) et la centrale n'arme pas avec elle sauf forçage, auquel cas elle est exclue et notée ; un détecteur de fumée ou de panique qui sonne n'est jamais exclu |
| Un ordre du serveur que personne n'a autorisé | Armer, désarmer et faire taire depuis le serveur exigent TROIS interrupteurs (le réglage du nœud, la liste d'accès du broker et `ARMOR_ALARM_COMMANDS=1` sur le serveur), le serveur demande le PIN de l'utilisateur avant d'envoyer un désarmement ou un silence, et tout est désactivé par défaut ; le relais de la sirène appartient à l'alarme seule (ni le broker, ni la centrale, ni le panneau ne peuvent le bouger) |
| Faux messages Zigbee | Le topic `armor/alarm/<id>/zigbee` porte un HMAC-SHA256 sur nœud, zone, état, batterie et séquence avec la clé de la centrale (64 hex saisis dans le panneau), et la séquence ne fait que monter ; le topic de politique porte `config_hash`, `zone_feed` et sa signature, chacun pouvant être fixé sur le nœud |

Ce n'est pas un système d'alarme certifié ([docs/SAFETY.md](docs/SAFETY.md)) : c'est un projet domestique qui n'a jamais tourné sur une carte ni dans une vraie installation. Si le serveur est absent, la centrale décide seule, et si le nœud ou sa radio tombe aussi, personne ne surveille. Lisez [SECURITY.md](SECURITY.md) pour signaler une vulnérabilité.""",
      "interfaces": r"""| Partie | Ce qu'elle règle |
|---|---|
| MQTT | `armor/alarm/<id>/state` (non retenu : zones avec id, nom, type, état et exclusion, la phase), `/command`, `/result`, `/zigbee` et `/policy` (serveur vers centrale) ; `armor/device/<id>/<relais>/{state,set}`, `armor/health/<id>`, `armor/control/<id>/...` |
| Zones | Type `instant`, `entry`, `interior` ou `always` ; état `normal`, `triggered`, `tamper` ou `trouble` ; jusqu'à 8 boucles câblées (un contact avec résistance de fin de ligne lu par l'ADC donne quatre états sur une broche ; la carte Ethernet a 6 broches analogiques valides, la carte Wi-Fi 8), 4 boutons et un journal de 100 événements |
| Zigbee | Un pont série (ZNP) vers un coordinateur, des capteurs IAS Zone et des sirènes IAS WD ; le nœud prend la radio quand le Zigbee2MQTT du serveur se tait pendant `zigbee_silence_min` et la rend au retour du serveur ([docs/ZIGBEE.md](docs/ZIGBEE.md), [docs/FAILOVER.md](docs/FAILOVER.md)) |""",
      "configuration": r"""| Variable | Par défaut | Ce qu'elle règle |
|---|---|---|
| `panel.exit_delay_s`, `panel.entry_delay_s` | 30, 30 (0-600) | Les retards de sortie et d'entrée ; la sortie ne traite pas celui qui part en intrus |
| `panel.lockout_s` | 60 (1-3600) | Le blocage du PIN, fois 1, 5 et 15 pour les trois premiers |
| `zigbee_silence_min` | - | Combien de temps le Zigbee du serveur peut se taire avant que le nœud prenne la radio |
| `CONFIG_ARMOR_NODE_ID`, `_SETUP_CODE`, `_FLEET_SECRET`, `_MQTT_*`, `_HEARTBEAT_S`, `_BLE_SETUP_MINUTES`, `_BOOT_FACTORY_RESET` | - | Les réglages que tous les nœuds partagent : le nom (vide donne `armor-` et les derniers octets de la MAC), le code de configuration (vide : aléatoire), le secret de flotte (16+ caractères, jamais dans le dépôt), les premiers réglages du broker, le battement (de 2 à 300 s), les minutes de configuration Bluetooth (de 1 à 120) et la réinitialisation avec BOOT (8 s dans les 30 premières s) |

Les nouvelles sonneries après un silence sont limitées à 3 (`kMaxResounds`). Le relais de la sirène démarre ouvert à chaque redémarrage et ne retombe pas ouvert si le broker est perdu.""",
      "quickstart": r"""**Prérequis:** un compilateur C++17 pour les tests sur hôte ; le conteneur ESP-IDF 5.5.5 pour construire l'image ; une carte ESP32-S3 (Ethernet ou Wi-Fi) avec la carte de base.

```bash
cmake -S tests -B build/host && cmake --build build/host && ctest --test-dir build/host   # host tests, -Werror
node tools/panel_mock.mjs --user admin:adminpass123   # the panel without a board
tools/build_node.sh generic s3-wifi                  # the image in the ESP-IDF container (or s3-eth)
```

Voir [la conception](docs/DESIGN.md), [comment la centrale prend le relais du serveur](docs/FAILOVER.md) et les [notes de sécurité](docs/SAFETY.md).""",
      "testing": r"""```bash
cmake -S tests -B build/host && cmake --build build/host && ctest --test-dir build/host
python -I tools/armor_ci_validate.py
```

18 programmes de test sur hôte et 5 contrôles Python tournent sous `ctest` ; 488930 vérifications comptées par les programmes hôte, compilés avec `-Werror`.

Contrôles Python : les textes du panneau en huit langues, les tâches, les chemins de sauvegarde, la session Bluetooth sous son verrou et les routes appelées par le panneau (et, dans certains nœuds, les codes HTTP ou les glyphes des polices)

Les tests sur hôte demandent un compilateur C++17 quelconque (Linux, WSL, MSYS2) ; le panneau web est aussi exercé dans un vrai navigateur contre un nœud de substitution (`tools/panel_mock.mjs`, `tools/panel_browser_test.mjs`).

La plupart des vérifications sont des balayages exhaustifs des règles de la centrale ; les boucles, la sirène et la liaison Zigbee sont des substituts.""",
      "build": "`tools/build_node.sh` construit l'image dans le conteneur ESP-IDF 5.5.5 et la version porte l'image, son SHA-256 et sa signature Ed25519, une par carte ; l'image est écrite par USB-C la première fois, puis mise à jour depuis le panneau.",
      "troubleshooting": r"""| Vous voyez | Parce que | Faites |
|---|---|---|
| Vous avez perdu le mot de passe ou le nœud ne rejoint plus le réseau | Un nœud en configuration sans adresse après 90 s ouvre son propre Wi-Fi `ARMOR-SETUP-xxxxxx` (ouvrez `http://192.168.4.1/`) | Pour recommencer, maintenez BOOT 8 secondes dans les 30 premières secondes après la mise sous tension (efface réglages et utilisateurs), ou utilisez *Réinitialisation d'usine* dans le panneau |
| Une mise à jour depuis GitHub est refusée | La version n'a ni somme de contrôle ni signature, elles ne concordent pas (`e_no_checksum`, `e_no_signature`, `e_checksum_mismatch`, `e_bad_signature`), n'a pas d'image pour cette carte (`e_no_asset_for_board`) ou est d'un autre projet (`e_wrong_firmware`) | Le nœud n'a pas changé ; réessayez ou laissez un administrateur envoyer le fichier à la main |
| La centrale n'arme pas | Une zone est en `trouble` (le convertisseur ne démarre pas ou 5 tours sans lecture) | Réparez le câblage, ou forcez l'armement (la zone est alors exclue et notée) |
| Le PIN est refusé même quand il est bon | La centrale est bloquée après des échecs (même le bon PIN est refusé) | Attendez `lockout_s` ; le blocage survit à un redémarrage |
| La réinitialisation par BOOT ne fait rien | La centrale est armée : la réinitialisation n'efface qu'une centrale désarmée | Désarmez d'abord avec le PIN |""",
      "structure": r"""<p align="center">
  <img src="images/repository-structure.svg" alt="Structure du dépôt de ARMOR-NODE-ALARM" width="100%">
</p>

<details>
<summary>Version texte de l'arborescence</summary>

```text
ARMOR-NODE-ALARM/
├── main/                                le firmware : un composant ESP-IDF
├── core/                                la logique sans ESP-IDF, testée sur ordinateur
├── panel/                               le panneau web intégré au firmware
├── tests/                               tests sur hôte et contrôles Python
├── docs/                                11 guides : sécurité, messages, Zigbee, relève
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

* La conversation Zigbee du nœud lui-même avec un coordinateur, local ou sur le réseau, n'est testée que contre un coordinateur simulé ; elle n'a jamais rencontré un vrai coordinateur ni un vrai capteur.
* Le panneau web a été essayé dans un vrai navigateur contre un nœud simulé, pas sur une carte.
* Aucune carte construite, aucune zone câblée et ni sirène ni coordinateur Zigbee connectés : rien n'a tourné sur une installation réelle.
* Le PIN avec verrouillage, le code de configuration, la limite de connexions et les mises à jour signées sont testés sur l'hôte ; il n'y a pas eu de revue indépendante et ce n'est pas un système d'alarme certifié.
* Les contrôles de hash et de signature Ed25519 et la logique de retour arrière réussissent sur l'hôte ; une mise à jour par voie hertzienne n'a jamais été exécutée sur une carte.
* La sirène et les relais sont pilotés par les règles de l'alarme et testés contre des simulations ; aucun n'a été relié à une vraie sirène ou à un vrai relais.

**Ensuite**

* Câbler de vraies boucles et une sirène, essayer la liaison Zigbee avec un vrai coordinateur et de vrais capteurs, et faire tourner la centrale dans une vraie installation avant d'affirmer quoi que ce soit de plus.""",
    },
  },
  "it": {
    "tagline": "Nodo e centrale d'allarme: le zone, l'inserimento, i ritardi, la sirena e il PIN dell'allarme di casa, con il firmware del nodo e le regole provate su un computer (nulla ha girato su una scheda)",
    "honest": "Ciò che esiste è il **nucleo dell'allarme** (cos'è una zona, come un anello cablato letto dall'ADC diventa uno stato, le regole della centrale: inserimento, ritardi, l'allarme, la sirena, il PIN con blocco) e il **firmware del nodo** costruito su di esso (impostazioni, pannello web, messaggi con il server, il ponte della radio Zigbee, un coordinatore Zigbee in rete, relè, Bluetooth, aggiornamenti firmati), che si compila per entrambe le schede; il nucleo, le impostazioni, i messaggi e il pannello in un vero browser contro un nodo sostitutivo sono provati su un computer con 488.930 controlli in 18 programmi di test. **Nulla ha girato su una scheda né su un impianto reale, nessuna zona è stata cablata né sirena collegata, la conversazione Zigbee del nodo con un coordinatore (locale o in rete) è scritta e provata contro un coordinatore sostitutivo ma non ha mai girato contro un coordinatore o un sensore reali, e questo non è un sistema d'allarme certificato.**",
    "glance": [
      [
        "Ruolo",
        "Nodo di campo centrale di allarme per ESP32-S3 (famiglia: Field Nodes, padre: ARMOR-COMMON)",
      ],
      [
        "Tecnologia",
        "C++17, ESP-IDF 5.5.5, ESP32-S3",
      ],
      [
        "Test",
        "488930 verifiche in 18 programmi host e 5 verifiche Python (`ctest`)",
      ],
      [
        "Ingressi",
        "Fino a 8 anelli cablati, sensori Zigbee (IAS Zone) e sirena (IAS WD), 4 pulsanti",
      ],
      [
        "Gira su",
        "Una scheda ESP32-S3 (Ethernet o Wi-Fi) con la scheda base; test su host su qualsiasi computer",
      ],
      [
        "Su hardware reale",
        "Ancora nessuno: nessuna scheda, zona, sirena o coordinatore Zigbee collegati (solo test su computer, la compilazione e il pannello in un browser)",
      ],
      [
        "Licenza",
        "GPL-3.0-or-later",
      ],
    ],
    "status": {
      "software": "Il firmware compila nel contenitore ESP-IDF 5.5.5 per entrambe le schede (Wi-Fi ed Ethernet).",
      "tests": "Superano 488.930 controlli in 18 programmi host (`ctest`): le zone, i circuiti cablati letti dall'ADC, le regole di inserimento, ritardi, sirena e PIN, le impostazioni e i messaggi.",
      "protocols": "La conversazione Zigbee del nodo stesso con un coordinatore, locale o in rete, è provata solo contro un coordinatore simulato; non ha mai incontrato un coordinatore o un sensore reali.",
      "ui": "Il pannello web è stato provato in un browser reale contro un nodo simulato, non su una scheda.",
      "hardware": "Nessuna scheda costruita, nessuna zona cablata e nessuna sirena o coordinatore Zigbee collegati: nulla ha funzionato su un impianto reale.",
      "security": "Il PIN con blocco, il codice di configurazione, il limite di accessi e gli aggiornamenti firmati sono testati sull'host; non c'è stata una revisione indipendente e non è un sistema di allarme certificato.",
      "updates": "I controlli di hash e firma Ed25519 e la logica di ripristino passano sull'host; un aggiornamento via etere non è mai stato eseguito su una scheda.",
      "writing": "La sirena e i relè sono comandati dalle regole dell'allarme e provati contro simulazioni; nessuno è stato collegato a una sirena o a un relè reali.",
      "integration": "I messaggi del nodo sono validati contro gli schemi condivisi e i vettori di conformità di ARMOR-COMMON.",
      "docs": "Otto lingue, la guida del firmware, le note di cablaggio e il registro delle modifiche sono aggiornati.",
    },
    "docs": [
      "[Sicurezza](docs/SAFETY.md): cosa promette la centrale e cosa no",
      "[Messaggi di allarme](docs/ALARM_MESSAGES.md), [Zigbee](docs/ZIGBEE.md) e [subentro](docs/FAILOVER.md)",
      "[Progetto](docs/DESIGN.md), [hardware](docs/HARDWARE.md), [scheda base](docs/BASE_BOARD.md) e [firmware del nodo](docs/NODE_FIRMWARE.md)",
      "[Prove al banco](docs/BENCH_TESTS.md), [codice di configurazione](docs/SETUP_CODE.md) e [provisioning Bluetooth](docs/BLE_PROVISIONING.md)",
    ],
    "contributing_first": "Prima di una pull request esegui `ctest --test-dir build/host` and `python -I tools/armor_ci_validate.py`: deve passare. Vedi [CONTRIBUTING.md](CONTRIBUTING.md) e il [codice di condotta](CODE_OF_CONDUCT.md).",
    "languages_extra": "",
    "body": {
      "overview": r"""* **Zone:** quattro tipi - *istantanea* (una porta, una finestra), *d'ingresso* (la porta da cui si entra: avvia il ritardo d'ingresso), *interna* (movimento: solo in "fuori casa") e *sempre* (fumo, gas, panico: inserita o no). Una zona può essere un anello cablato o un sensore Zigbee.
* **L'anello cablato:** un contatto con resistenza di fine linea, letto come tensione, dà quattro stati su un solo pin - normale, scattato e manomissione per un filo in cortocircuito o tagliato. I limiti sono impostazioni; un filtro antirimbalzo impedisce che un contatto che rimbalza faccia scattare l'allarme.
* **La centrale:** inserimento *fuori casa* e *in casa*, un ritardo di uscita che non tratta da intruso chi esce, un ritardo d'ingresso, un allarme che **resta memorizzato** fino a un disinserimento corretto, una sirena che si ferma da sola dopo un po', l'esclusione delle zone aperte se si forza (mai un rilevatore di fumo che suona) e un registro degli ultimi cento eventi.
* **Il PIN:** l'inserimento non lo chiede, il disinserimento e il silenziamento sì; i PIN errati vengono contati e, dopo alcuni, tutto viene rifiutato per un po', anche il PIN giusto.
* **Silenziare senza disinserire:** finché la sirena suona, un PIN corretto la ferma subito con il sistema ancora inserito - l'allarme resta agganciato e registrato, una zona che non ha ancora suonato può farla suonare di nuovo, e un PIN errato conta per il blocco come uno errato di disinserimento.
* **Il piano:** un gateway sulla scheda del nodo elettrico (radio Zigbee, zone cablate, relè della sirena) che lavora con ARMOR-SERVER e **continua a sorvegliare quando il server manca**: una centrale prende la radio al server tramite il ponte Zigbee di ARMOR-NODE-ELECTRICAL. Vedi [il progetto](docs/DESIGN.md) e [il passaggio di consegne](docs/FAILOVER.md).
* **Il nodo:** firmware per l'ESP32-S3 (Ethernet PoE o Wi-Fi) con fino a otto zone cablate, la sirena su un relè, il pannello web di tutti i nodi in otto lingue, la radio Zigbee prestata a Zigbee2MQTT e i messaggi `armor/alarm/<nodo>/state|command|result`; il server può inserire e disinserire solo se tre interruttori indipendenti lo permettono. Vedi [il firmware](docs/NODE_FIRMWARE.md), [i messaggi](docs/ALARM_MESSAGES.md) e [l'hardware](docs/HARDWARE.md).
* **Prendere la radio:** quando Zigbee2MQTT del server è assente da un certo tempo, il nodo avvia da sé il coordinatore (ZNP), legge i sensori delle zone che ne nominano uno (IAS Zone) e comanda sirene Zigbee (IAS WD), e la rilascia appena il client torna.
* **Non ancora:** un coordinatore o sensore reali, l'hardware e qualsiasi prova su un impianto reale.
* **Un riavvio non disinserisce la casa:** la modalità, un allarme in corso e le zone escluse vengono conservati nella flash e ripresi all'avvio; un anello tagliato o in cortocircuito non viene mai escluso; i messaggi passano da una coda (nessuno stallo con il broker) e il watchdog riavvia la scheda se si ferma il task che legge le zone.
* **Aggiornamenti via etere firmati:** il nodo installa da GitHub solo un'immagine il cui SHA-256 coincide e che porta una firma Ed25519 valida del responsabile (la chiave pubblica è nel firmware, quella privata non lascia mai il responsabile); un file caricato a mano da un amministratore nel pannello resta accettato. Le pagine e i messaggi del pannello sono in otto lingue.
* **Abbinamento Bluetooth con PIN:** il PIN a sei cifre deriva dal codice di configurazione, è stampato sulla console USB e mostrato a un amministratore nel pannello; il telefono deve inserirlo prima di poter scrivere le impostazioni del nodo.
* **Sirena e riavvii:** il relè della sirena appartiene solo all'allarme (né il broker, né la centrale, né il pannello possono muoverlo, e non si apre alla perdita del broker); una zona che non aveva ancora suonato fa suonare di nuovo la sirena dopo il suo tempo; dopo un riavvio tornano un allarme di fumo o panico a sistema disinserito, un allarme silenziato e un blocco; un ripristino a mano viene rifiutato con l'allarme inserito; un sensore Zigbee che non parla mai conta come perso.
* **Solo la casa può usare il pannello:** il pannello risponde per impostazione predefinita alla rete privata (o alle reti indicate dal proprietario, come una VPN), rifiuta un elenco che escluderebbe chi lo salva, conta le password errate per persona e per indirizzo e funziona dietro il proxy del server per essere raggiunto da fuori casa senza pubblicare il nodo.
* **Una zona illeggibile non viene mostrata come chiusa:** se il convertitore non parte o un anello non dà lettura per cinque giri di fila, la zona passa in *guasto* (trouble) - non sorveglia, non fa mai suonare la sirena, impedisce l'inserimento (salvo forzandolo, e allora viene esclusa e annotata) e il server avvisa.
* **Collegamento cifrato facoltativo con il broker (TLS):** disattivato per impostazione predefinita, quindi il nodo parla MQTT non cifrato come prima. Un interruttore e una casella per il certificato dell'autorità propria dell'installazione (PEM, al massimo 2 KB) nella pagina Broker lo fanno collegare con `mqtts://`, fidarsi solo di quell'autorità e verificare che il certificato del broker sia stato fatto per l'indirizzo raggiunto; ciò che non è un solo certificato PEM viene rifiutato. Coperto da test sul computer; l'handshake non è ancora stato eseguito su una scheda.
* **Profili di inserimento:** un comando di inserimento può portare un profilo (Fuori casa, In casa, Notte, il tuo) che sceglie, per quell'inserimento, quali zone sorvegliano, quali fanno scattare l'allarme subito o dopo il ritardo d'ingresso, i ritardi di uscita e d'ingresso e se la sirena suona (un allarme silenzioso resta memorizzato, registrato e segnalato). Non tocca mai le zone di fumo, panico o manomissione, il PIN, il blocco, il silenziamento, un inserimento forzato né una zona in guasto; il profilo sopravvive a un riavvio e un inserimento senza profilo si comporta esattamente come prima. Provato contro le vecchie regole con un'esecuzione casuale e contro il contratto condiviso.
* **Rapporto di salute:** circa una volta al minuto il nodo pubblica da quanto è acceso e perché si è riavviato l'ultima volta, la memoria libera, il collegamento e il segnale Wi-Fi, quante volte si è connesso al broker e l'ultimo errore registrato (`armor/health/<nodo>`, il contratto `node_health` di ARMOR-COMMON). Il codice che lo costruisce è condiviso da tutti i nodi e testato su un computer; non è mai girato su una scheda.
* **Controllo dal server:** Studio può riavviare il nodo in modo pulito, metterlo in pausa fino a un'ora (riprende da solo), mettere il suo lavoro in standby (senza fine, conservato ai riavvii, il nodo resta connesso e continua a rispondere), farlo mostrare, chiedere un'istantanea diagnostica e segnarlo in manutenzione (`armor/control/<nodo>/...`, il contratto `node_control` di ARMOR-COMMON). Ogni ordine è in due passi con un token monouso legato a quell'operazione, solo il server può scriverli sul broker e non esistono ripristino di fabbrica, cancellazione né sonno profondo. Finché il nodo è in pausa o in standby le sue zone non vengono lette, nulla viene valutato, attivato o fatto suonare, nessuno stato viene pubblicato e il relè della sirena resta aperto: la casa NON è protetta, e il rapporto di salute lo dice. Il codice è condiviso da tutti i nodi e provato su un computer; non ha ancora girato su una scheda.
* **Diagnostica senza cavo:** dopo un avvio non pulito (un blocco, un watchdog, un calo di alimentazione, un'allocazione fallita) il rapporto di salute ne indica la causa per dieci minuti; un arresto anomalo lascia il suo core dump da vedere, scaricare o cancellare dal pannello; le impostazioni salvate vengono copiate prima di ogni installazione del firmware e recuperate se un aggiornamento le danneggia; e un amministratore può chiedere al nodo, tramite il server, un pacchetto di diagnostica o il suo registro con un token monouso.
* **Le opzioni di sicurezza del server:** la centrale applica le opzioni che il server tiene per lei (`armor/alarm/<nodo>/policy`) e ciascuna può essere fissata sul nodo stesso: lo stato inserito salvato è legato alle zone e al PIN, i messaggi di zona Zigbee del server possono essere spenti e, se firmati, vengono verificati (firma con una chiave digitata nel pannello e un numero di sequenza che può solo crescere). Provato su un computer con i valori che calcolano il contratto e il server; non eseguito su una scheda.
* **Sigillatura facoltativa dei segreti salvati:** disattivata per impostazione predefinita (`security.seal_secrets`, o `nodes.nvs_encryption` del server). Attiva, le password, i token, le chiavi, i PIN e gli hash delle password che il nodo salva restano sigillati con ChaCha20-Poly1305 e tutto il resto resta leggibile; attivarla o disattivarla li riscrive senza perdere nulla, anche se il nodo si ferma a metà. Nessun eFuse viene bruciato e la flash non è cifrata: la chiave si trova in una partizione dello stesso chip, quindi **non** protegge da chi ha la scheda, e un nodo installato prima di quella partizione mantiene i suoi segreti com'erano finché non viene flashato con la nuova tabella delle partizioni.""",
      "role": r"""ARMOR-NODE-ALARM è la centrale d'allarme: le zone, l'inserimento, i ritardi, la sirena e il PIN si decidono sul nodo stesso, così la casa resta sorvegliata quando il server è assente. [ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER) la mostra, lega sensori Zigbee alle sue zone e, quando lo permetti, la inserisce e disinserisce; il menu *Centrali d'allarme* e il *Progettista dell'allarme* di [ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) e l'app [ARMOR-ANDROID-CONTROL](https://github.com/JuanenRac/ARMOR-ANDROID-CONTROL) la comandano. La sua radio Zigbee può essere sulla scheda o un coordinatore in rete.

| Nome | Come | A cosa serve |
|---|---|---|
| ARMOR-SERVER | MQTT `armor/alarm/<id>/{state,command,result,zigbee,policy}` | Riceve lo stato della centrale; ordina inserimento, disinserimento e silenzio solo dietro tre interruttori |
| ARMOR-STUDIO | menu delle centrali di allarme | Mostra le zone, gli eventi e la politica, e apre il pannello del nodo |
| ARMOR-ANDROID-CONTROL | Bluetooth | Configura il nodo sul campo e mostra le centrali di allarme |
| ARMOR-COMMON | contratto di allarme | I messaggi sono verificati con i suoi schemi; il firmware comune è copiato da lì |""",
      "architecture": r"""<p align="center">
  <img src="images/architecture.svg" alt="Architettura di ARMOR-NODE-ALARM: chi lo chiama, cosa contiene e da cosa dipende" width="100%">
</p>""",
      "security": r"""| Minaccia | Difesa |
|---|---|
| Password in chiaro o compilate | PBKDF2-HMAC-SHA256 con 10 000 round; nessuna password nel firmware (un nodo senza utenti entra in configurazione); al massimo 4 utenti (admin o visualizzatore) e da 8 a 64 caratteri; al massimo 6 sessioni, 30 minuti di inattività |
| Prendere un nodo appena programmato | La configurazione richiede un codice di avvio: quello della build (`CONFIG_ARMOR_SETUP_CODE`) o uno casuale tenuto in flash e mostrato sulla console USB; con un segreto di flotta è `HMAC-SHA256(segreto, MAC)`; è anche la chiave del Wi-Fi di configurazione (WPA2, mai in bridge) |
| Il pannello raggiunto da Internet | Risponde di default alle reti private di una casa (10/8, 172.16/12, 192.168/16, 169.254/16, 127/8 e 100.64/10 dove vivono alcune VPN); l'impostazione `web.admin_sources` elenca altri indirizzi e reti IPv4 (8 voci, 120 caratteri); tutto il resto è rifiutato tranne l'identità pubblica `GET /api/v1/session`; una lista che escluderebbe chi la salva è rifiutata |
| Il pannello in chiaro su HTTP | HTTPS sulla 443 con un certificato che il nodo crea da sé (autofirmato, in flash, impronta SHA-256 visibile per confrontarla); il pannello può essere http, https o entrambi; il cookie di sessione è sempre HttpOnly e SameSite=Strict (e Secure su TLS) |
| Un firmware falso da GitHub | Un'immagine si installa solo con uno SHA-256 coincidente e una firma Ed25519 valida fatta con la chiave del manutentore (`no_checksum`, `no_signature`, `bad_signature`, `checksum_mismatch`, `wrong_firmware`, `not_newer`, `version_mismatch` la rifiutano); un caricamento manuale da un amministratore non è verificato: un limite esplicito |
| Dirottamento della configurazione Bluetooth | Un PIN a 6 cifre derivato dal codice di configurazione, visibile sulla console USB e a un amministratore; il telefono deve digitarlo prima di scrivere le impostazioni; la finestra dura `CONFIG_ARMOR_BLE_SETUP_MINUTES` (10 di default, da 1 a 120) |
| Segreti memorizzati letti da chi ha la scheda | Opzionale (spento di default, interruttore `security.seal_secrets` o `nodes.nvs_encryption` del server): ChaCha20-Poly1305 per password, token, chiavi, PIN e hash. Non cifra la flash né brucia un eFuse: la chiave è in una partizione dello stesso chip, quindi non protegge da chi ha la scheda |
| Il collegamento al broker in chiaro | TLS opzionale (`mqtts://`) con l'autorità propria del proprietario (PEM fino a 2 KB) e verifica del nome; spento di default. L'handshake è girato solo nei test su host, non su una scheda |
| Indovinare il PIN della centrale | Il confronto non rivela dove differisce; errori consecutivi bloccano la centrale per `lockout_s` (60 s di default, da 1 a 3600) per 1, 5 e 15 nei primi tre blocchi, anche con il PIN giusto; un blocco in corso è ripristinato dopo un riavvio; inserire non richiede PIN, disinserire e silenziare sì |
| Un riavvio che disinserisce la casa | Il modo, l'allarme in corso e le zone escluse sono tenuti in flash e recuperati; un anello interrotto o in corto non viene mai lasciato fuori; fumo, panico e manomissione scattati a sistema disinserito tornano dopo un riavvio; il ripristino con BOOT cancella solo a centrale DISINSERITA |
| Una zona illeggibile sembra chiusa | Mostra `trouble` (il convertitore non parte o 5 giri senza lettura) e la centrale non inserisce con essa salvo forzatura, e allora è esclusa e annotata; un rilevatore di fumo o panico che sta suonando non viene mai escluso |
| Un ordine del server che nessuno ha autorizzato | Inserire, disinserire e silenziare dal server richiedono TRE interruttori (l'impostazione del nodo, la lista di accesso del broker e `ARMOR_ALARM_COMMANDS=1` sul server), il server chiede il PIN dell'utente prima di inviare un disinserimento o un silenzio, e tutto è spento di default; il relè della sirena appartiene solo all'allarme (né il broker, né la centrale, né il pannello possono muoverlo) |
| Messaggi Zigbee falsi | Il topic `armor/alarm/<id>/zigbee` porta un HMAC-SHA256 su nodo, zona, stato, batteria e sequenza con la chiave della centrale (64 hex digitati nel pannello), e la sequenza può solo salire; il topic della politica porta `config_hash`, `zone_feed` e la sua firma, ciascuno fissabile sul nodo |

Non è un sistema di allarme certificato ([docs/SAFETY.md](docs/SAFETY.md)): è un progetto domestico e non è mai girato su una scheda né in un impianto reale. Se manca il server la centrale decide da sola, e se cade anche il nodo o la sua radio nessuno sorveglia. Leggi [SECURITY.md](SECURITY.md) per segnalare una vulnerabilità.""",
      "interfaces": r"""| Parte | Cosa imposta |
|---|---|
| MQTT | `armor/alarm/<id>/state` (non retained: zone con id, nome, tipo, stato ed esclusione, la fase), `/command`, `/result`, `/zigbee` e `/policy` (server verso centrale); `armor/device/<id>/<relè>/{state,set}`, `armor/health/<id>`, `armor/control/<id>/...` |
| Zone | Tipo `instant`, `entry`, `interior` o `always`; stato `normal`, `triggered`, `tamper` o `trouble`; fino a 8 anelli cablati (un contatto con resistenza di fine linea letto dall'ADC dà quattro stati su un pin; la scheda Ethernet ha 6 pin analogici validi, la Wi-Fi 8), 4 pulsanti e un registro di 100 eventi |
| Zigbee | Un ponte seriale (ZNP) verso un coordinatore, sensori IAS Zone e sirene IAS WD; il nodo prende la radio quando lo Zigbee2MQTT del server tace per `zigbee_silence_min` e la restituisce al ritorno del server ([docs/ZIGBEE.md](docs/ZIGBEE.md), [docs/FAILOVER.md](docs/FAILOVER.md)) |""",
      "configuration": r"""| Variabile | Predefinito | Cosa imposta |
|---|---|---|
| `panel.exit_delay_s`, `panel.entry_delay_s` | 30, 30 (0-600) | I ritardi di uscita e di ingresso; l'uscita non tratta come intruso chi se ne va |
| `panel.lockout_s` | 60 (1-3600) | Il blocco del PIN, per 1, 5 e 15 nei primi tre |
| `zigbee_silence_min` | - | Quanto può tacere lo Zigbee del server prima che il nodo prenda la radio |
| `CONFIG_ARMOR_NODE_ID`, `_SETUP_CODE`, `_FLEET_SECRET`, `_MQTT_*`, `_HEARTBEAT_S`, `_BLE_SETUP_MINUTES`, `_BOOT_FACTORY_RESET` | - | Le impostazioni che tutti i nodi condividono: il nome (vuoto dà `armor-` e gli ultimi byte del MAC), il codice di configurazione (vuoto: casuale), il segreto di flotta (16+ caratteri, mai nel repository), le prime impostazioni del broker, il battito (da 2 a 300 s), i minuti di configurazione Bluetooth (da 1 a 120) e il ripristino con BOOT (8 s nei primi 30 s) |

I nuovi suoni dopo un silenzio sono limitati a 3 (`kMaxResounds`). Il relè della sirena parte aperto a ogni riavvio e non cade aperto se si perde il broker.""",
      "quickstart": r"""**Requisiti:** un compilatore C++17 per i test su host; il container ESP-IDF 5.5.5 per costruire l'immagine; una scheda ESP32-S3 (Ethernet o Wi-Fi) con la scheda base.

```bash
cmake -S tests -B build/host && cmake --build build/host && ctest --test-dir build/host   # host tests, -Werror
node tools/panel_mock.mjs --user admin:adminpass123   # the panel without a board
tools/build_node.sh generic s3-wifi                  # the image in the ESP-IDF container (or s3-eth)
```

Vedi [il progetto](docs/DESIGN.md), [come la centrale subentra al server](docs/FAILOVER.md) e le [note di sicurezza](docs/SAFETY.md).""",
      "testing": r"""```bash
cmake -S tests -B build/host && cmake --build build/host && ctest --test-dir build/host
python -I tools/armor_ci_validate.py
```

18 programmi di test su host e 5 verifiche Python girano con `ctest`; 488930 verifiche contate dai programmi host, compilati con `-Werror`.

Verifiche Python: i testi del pannello in otto lingue, i task, i percorsi di salvataggio, la sessione Bluetooth sotto il suo lock e i percorsi chiamati dal pannello (e, in alcuni nodi, i codici HTTP o i glifi dei caratteri)

I test su host richiedono un qualsiasi compilatore C++17 (Linux, WSL, MSYS2); il pannello web è anche provato in un browser reale contro un nodo sostitutivo (`tools/panel_mock.mjs`, `tools/panel_browser_test.mjs`).

La maggior parte delle verifiche sono scansioni esaustive delle regole della centrale; anelli, sirena e collegamento Zigbee sono sostituti.""",
      "build": "`tools/build_node.sh` costruisce l'immagine nel container ESP-IDF 5.5.5 e la versione porta l'immagine, il suo SHA-256 e la sua firma Ed25519, una per scheda; l'immagine si scrive via USB-C la prima volta e poi si aggiorna dal pannello.",
      "troubleshooting": r"""| Vedi | Perché | Fai |
|---|---|---|
| Hai perso la password o il nodo non entra più in rete | Un nodo in configurazione senza indirizzo dopo 90 s apre un proprio Wi-Fi `ARMOR-SETUP-xxxxxx` (apri `http://192.168.4.1/`) | Per ricominciare tieni premuto BOOT per 8 secondi nei primi 30 secondi dopo l'accensione (cancella impostazioni e utenti), o usa *Ripristino di fabbrica* nel pannello |
| Un aggiornamento da GitHub è rifiutato | La versione non ha checksum o firma, non corrispondono (`e_no_checksum`, `e_no_signature`, `e_checksum_mismatch`, `e_bad_signature`), non ha un'immagine per questa scheda (`e_no_asset_for_board`) o è di un altro progetto (`e_wrong_firmware`) | Il nodo non è cambiato; riprova o lascia che un amministratore carichi il file a mano |
| La centrale non inserisce | Una zona è in `trouble` (il convertitore non parte o 5 giri senza lettura) | Correggi il cablaggio, o forza l'inserimento (la zona viene allora esclusa e annotata) |
| Il PIN è rifiutato anche se è giusto | La centrale è bloccata dopo tentativi falliti (anche il PIN giusto è rifiutato) | Attendi `lockout_s`; il blocco sopravvive a un riavvio |
| Il ripristino con BOOT non fa nulla | La centrale è inserita: il ripristino cancella solo una centrale disinserita | Disinserisci prima con il PIN |""",
      "structure": r"""<p align="center">
  <img src="images/repository-structure.svg" alt="Struttura del repository di ARMOR-NODE-ALARM" width="100%">
</p>

<details>
<summary>Versione testuale dell'albero</summary>

```text
ARMOR-NODE-ALARM/
├── main/                                il firmware: un componente ESP-IDF
├── core/                                la logica senza ESP-IDF, testata su un computer
├── panel/                               il pannello web incorporato nel firmware
├── tests/                               test su host e verifiche Python
├── docs/                                11 guide: sicurezza, messaggi, Zigbee, subentro
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

* La conversazione Zigbee del nodo stesso con un coordinatore, locale o in rete, è provata solo contro un coordinatore simulato; non ha mai incontrato un coordinatore o un sensore reali.
* Il pannello web è stato provato in un browser reale contro un nodo simulato, non su una scheda.
* Nessuna scheda costruita, nessuna zona cablata e nessuna sirena o coordinatore Zigbee collegati: nulla ha funzionato su un impianto reale.
* Il PIN con blocco, il codice di configurazione, il limite di accessi e gli aggiornamenti firmati sono testati sull'host; non c'è stata una revisione indipendente e non è un sistema di allarme certificato.
* I controlli di hash e firma Ed25519 e la logica di ripristino passano sull'host; un aggiornamento via etere non è mai stato eseguito su una scheda.
* La sirena e i relè sono comandati dalle regole dell'allarme e provati contro simulazioni; nessuno è stato collegato a una sirena o a un relè reali.

**Prossimi passi**

* Cablare anelli e una sirena reali, provare il collegamento Zigbee con un coordinatore e sensori reali, e far girare la centrale in un impianto reale prima di affermare altro.""",
    },
  },
  "ja": {
    "tagline": "警報ノードと警報盤：住宅の警報の警戒区域、警戒セット、遅延、サイレン、PIN を、ノードのファームウェアとコンピューターでテストしたルールを含みます（基板では動作していません）",
    "honest": "存在するのは**警報のコア**（警戒区域とは何か、ADC が読む配線ループがどう状態になるか、警報盤のルール：警戒、遅延、警報、サイレン、ロックアウト付き PIN）と、その上に作られた**ノードのファームウェア**（設定、Web パネル、サーバーとのメッセージ、Zigbee 無線のブリッジ、ネットワーク上の Zigbee コーディネーター、リレー、Bluetooth、署名付きアップデート）で、両方の基板向けにビルドできます。コア、設定、メッセージ、実際のブラウザーでの代替ノードに対するパネルは、18 つのテストプログラムで 488,930 項目としてコンピューター上でテストされています。**基板上でも実際の設備でも何も動いたことはなく、警戒区域の配線もサイレンの接続もなく、ノード自身の Zigbee コーディネーター（ローカルまたはネットワーク上）との通信は書かれて代替コーディネーターに対してテストされていますが、実際のコーディネーターやセンサーに対して動いたことはなく、これは認証済みの警報システムではありません。**",
    "glance": [
      [
        "役割",
        "ESP32-S3 用アラームパネルのフィールドノード（ファミリー：Field Nodes、親：ARMOR-COMMON）",
      ],
      [
        "技術",
        "C++17, ESP-IDF 5.5.5, ESP32-S3",
      ],
      [
        "テスト",
        "488930 件の検査（ホスト用プログラム 18 本と Python 検査 5 個、`ctest`）",
      ],
      [
        "入力",
        "最大 8 本の配線ループ、Zigbee センサー（IAS Zone）とサイレン（IAS WD）、ボタン 4 個",
      ],
      [
        "動作環境",
        "ベース基板付きの ESP32-S3 基板（Ethernet または Wi-Fi）、ホストテストは任意のコンピューター",
      ],
      [
        "実機での確認",
        "まだありません：基板、警戒区域、サイレン、Zigbee コーディネーターはいずれも未接続（コンピューター上のテスト、ビルド、ブラウザーでのパネルのみ）",
      ],
      [
        "ライセンス",
        "GPL-3.0-or-later",
      ],
    ],
    "status": {
      "software": "ファームウェアは ESP-IDF 5.5.5 コンテナで両方のボード（Wi-Fi とイーサネット）向けにビルドできます。",
      "tests": "18 のホストプログラムで 488,930 件のチェックが通ります（`ctest`）：ゾーン、ADC で読む有線ループ、警戒・遅延・サイレン・PIN の規則、設定、メッセージ。",
      "protocols": "ノード自身のコーディネーター（ローカルまたはネットワーク上）との Zigbee のやり取りは、模擬のコーディネーターに対してのみテストしています。本物のコーディネーターやセンサーとはまだ接続していません。",
      "ui": "Web パネルは実ブラウザーで模擬ノードに対して試しており、ボード上では試していません。",
      "hardware": "ボードは未製作で、ゾーンの配線もサイレンや Zigbee コーディネーターの接続もありません。実際の設備ではまだ何も動かしていません。",
      "security": "ロックアウト付きの PIN、設定コード、ログイン制限、署名付きアップデートはホストでテスト済みです。独立したレビューはなく、認証を受けた警報システムでもありません。",
      "updates": "ハッシュと Ed25519 署名の確認、ロールバックの処理はホストで通ります。無線アップデートはボード上で一度も実行していません。",
      "writing": "サイレンとリレーは警報の規則で駆動され、模擬に対してテストしています。本物のサイレンやリレーには接続していません。",
      "integration": "ノードのメッセージは ARMOR-COMMON の共有スキーマと適合ベクターに対して検証されています。",
      "docs": "8 言語、ファームウェアガイド、配線メモ、変更履歴は最新です。",
    },
    "docs": [
      "[安全](docs/SAFETY.md)：パネルが約束することとしないこと",
      "[アラームメッセージ](docs/ALARM_MESSAGES.md)、[Zigbee](docs/ZIGBEE.md)、[フェイルオーバー](docs/FAILOVER.md)",
      "[設計](docs/DESIGN.md)、[ハードウェア](docs/HARDWARE.md)、[ベース基板](docs/BASE_BOARD.md)、[ノードのファームウェア](docs/NODE_FIRMWARE.md)",
      "[ベンチテスト](docs/BENCH_TESTS.md)、[セットアップコード](docs/SETUP_CODE.md)、[Bluetooth プロビジョニング](docs/BLE_PROVISIONING.md)",
    ],
    "contributing_first": "Pull Request の前に `ctest --test-dir build/host` and `python -I tools/armor_ci_validate.py` を実行してください。通る必要があります。[CONTRIBUTING.md](CONTRIBUTING.md) と[行動規範](CODE_OF_CONDUCT.md)を参照してください。",
    "languages_extra": "",
    "body": {
      "overview": r"""* **警戒区域：** 4 種類 - *即時*（ドア、窓）、*進入*（入る側のドア：進入遅延を開始）、*室内*（動き：「外出」のときだけ）、*常時*（煙、ガス、非常ボタン：警戒中でなくても）。区域は配線ループでも Zigbee センサーでもかまいません。
* **配線ループ：** 終端抵抗付きの接点を電圧として読み、1 本のピンで 4 つの状態 - 正常、作動、そして配線のショートや断線による改ざん - を得ます。しきい値は設定で、チャタリング除去により、バウンドする接点が警報を鳴らすことはありません。
* **警報盤：** *外出*と*在宅*の警戒セット、出て行く人を侵入者扱いしない退出遅延、進入遅延、正しい解除まで**保持される警報**、一定時間で自動的に止まるサイレン、強制時に開いている区域をバイパス（鳴っている煙感知器は決してバイパスしません）、そして直近 100 件のイベントログ。
* **PIN：** 警戒セットには不要、解除と消音には必要です。誤った PIN は数えられ、数回で一定時間すべて拒否されます（正しい PIN も）。
* **解除せずにサイレンを止める：** サイレンが鳴っている間、正しい PIN で警戒を保ったままサイレンをすぐ止められます - 警報はラッチされたまま記録に残り、まだ鳴っていない警戒区域は再びサイレンを鳴らせ、誤った PIN は解除時の誤った PIN と同じようにロックアウトに数えられます。
* **計画：** 電気ノードの基板上のゲートウェイ（Zigbee 無線、配線区域、サイレン用リレー）。ARMOR-SERVER と連携し、**サーバーが不在でも警戒を続けます**：警報盤が ARMOR-NODE-ELECTRICAL の Zigbee ブリッジ経由でサーバーから無線を引き継ぎます。[設計](docs/DESIGN.md)と[引き継ぎ](docs/FAILOVER.md)を参照。
* **ノード：** ESP32-S3 用ファームウェア（PoE イーサネットまたは Wi-Fi）。最大 8 つの配線区域、リレーに接続したサイレン、全ノード共通の 8 言語の Web パネル、Zigbee2MQTT に貸し出す Zigbee 無線、そしてメッセージ `armor/alarm/<ノード>/state|command|result`。サーバーが警戒セット・解除できるのは、独立した 3 つのスイッチがすべて許可した場合だけです。[ファームウェア](docs/NODE_FIRMWARE.md)、[メッセージ](docs/ALARM_MESSAGES.md)、[ハードウェア](docs/HARDWARE.md)を参照。
* **無線の引き継ぎ：** サーバーの Zigbee2MQTT が設定時間いないと、ノードが自分でコーディネーターを起動し（ZNP）、センサーを指定した区域を読み取り（IAS Zone）、Zigbee サイレンを制御し（IAS WD）、クライアントが戻った瞬間に手放します。
* **まだ：** 実機のコーディネーターやセンサー、ハードウェア、実際の設備でのテスト。
* **再起動しても家の警戒は解除されません：** モード、進行中の警報、除外したゾーンはフラッシュに保存され、起動時に復元されます。断線や短絡したループは決して除外されません。メッセージはキューを通る（ブローカーとのデッドロックなし）ため、ゾーンを読むタスクが止まるとウォッチドッグが基板を再起動します。
* **署名付きの無線アップデート：**ノードが GitHub からインストールするのは、SHA-256 が一致し、管理者の有効な Ed25519 署名を持つイメージだけです（公開鍵はファームウェア内、秘密鍵は管理者の手元から出ません）。管理者がパネルで手動アップロードしたファイルは引き続き受け付けます。パネルのページとメッセージは 8 言語です。
* **PIN 付きの Bluetooth ペアリング：**6 桁の PIN は設定コードから導出され、USB コンソールに表示され、管理者にはパネルにも表示されます。スマートフォンはこれを入力して初めてノードの設定を書き込めます。
* **サイレンと再起動：**サイレンのリレーは警報だけのものです（ブローカー、センター、パネルは動かせず、ブローカーを失っても開きません）。まだ鳴っていないゾーンは、サイレンがタイムアウトした後に再び鳴らします。再起動後は、解除状態の煙・パニック警報、消音された警報、ロックアウトが復元されます。警戒中は手動リセットを拒否します。一度も応答しない Zigbee センサーは失われたものとして扱います。
* **パネルを使えるのは家だけ：**パネルは既定でプライベートネットワーク（または所有者が指定した VPN などのネットワーク）にだけ応答し、保存する本人を締め出す一覧は拒否します。誤ったパスワードは人ごと・アドレスごとに数え、サーバーのプロキシの背後でも動くので、ノードを公開せずに家の外から使えます。
* **読み取れないゾーンは「閉」と表示されません：** コンバーターが起動しない、またはループが5ラウンド続けて値を返さない場合、ゾーンは*障害*（trouble）になります。監視せず、サイレンを鳴らすことはなく、警戒開始を止め（強制時は除外して記録）、サーバーが警告します。
* **ブローカーとの暗号化通信(TLS、任意):** 初期状態ではオフで、ノードはこれまでどおり暗号化なしの MQTT で通信します。ブローカーページのスイッチと、設備独自の認証局の証明書(PEM、最大 2 KB)の入力欄により、`mqtts://` で接続し、その認証局だけを信頼し、到達したアドレス向けに発行された証明書かを確認します。PEM 証明書 1 つでないものは拒否されます。ホストテストで検証済みで、ハンドシェイクはまだ基板では実行していません。
* **警戒プロファイル:** 警戒コマンドにはプロファイル（外出、在宅、夜間、独自）を付けられ、その警戒について、どのゾーンが警戒するか、どれがすぐに、またはエントリー遅延の後に警報を出すか、退出・進入の遅延、サイレンを鳴らすか（無音の警報も保持・記録・通知されます）を決めます。煙・非常ボタン・改ざんのゾーン、PIN、ロックアウト、消音、強制警戒、異常のゾーンには一切触れません。プロファイルは再起動後も残り、プロファイルなしの警戒はこれまでとまったく同じ動作です。ランダム実行で旧ルールと、共有契約に対してテスト済みです。
* **状態報告:** ノードは約 1 分ごとに、稼働時間と直前の再起動の理由、空きメモリ、回線と Wi-Fi 信号、ブローカーへの接続回数、最後に記録したエラーを公開します（`armor/health/<ノード>`、ARMOR-COMMON の `node_health` 契約）。作成するコードは全ノードで共有され、コンピューター上でテストされていますが、ボード上ではまだ動作していません。
* **サーバーからの制御：** Studio はノードをきれいに再起動し、最大 1 時間まで一時停止し（自動的に再開）、作業を待機にし（期限なし、再起動後も維持、ノードは接続したまま応答を続けます）、自分を表示させ、診断のスナップショットを求め、メンテナンス中として印を付けることができます（`armor/control/<ノード>/...`、ARMOR-COMMON の `node_control` 契約）。命令はすべて、その操作専用の使い捨てトークンによる 2 段階で、ブローカーに書き込めるのはサーバーだけです。工場出荷時リセットも消去もディープスリープもありません。一時停止中または待機中のノードは、ゾーンを読まず、判定・警戒・鳴動を行わず、状態も発行せず、サイレンのリレーを開いたままにします。家は守られていません。健全性レポートがそれを示します。 このコードは全ノードで共有され、コンピューター上でテスト済みですが、実機ではまだ動作していません。
* **ケーブルなしの診断：** 正常でない起動（クラッシュ、ウォッチドッグ、電源の電圧低下、メモリ確保の失敗）の後、ヘルスレポートが10分間その原因を伝えます。クラッシュするとコアダンプが残り、パネルから確認、ダウンロード、削除できます。保存された設定はファームウェアのインストールごとにコピーされ、更新で壊れた場合は復元されます。管理者はサーバー経由で、使い捨てトークンを使って、ノードに診断パッケージまたはログを要求できます。
* **サーバーのセキュリティ設定：**パネルはサーバーが保持する設定（`armor/alarm/<ノード>/policy`）を適用し、それぞれをノード側で固定することもできます。保存された警戒状態はゾーンとPINに結び付けられ、サーバーのZigbeeゾーンメッセージはオフにでき、署名付きの場合は検証されます（パネルに入力した鍵による署名と、増える一方のシーケンス番号）。契約とサーバーが計算する値でコンピューター上でテスト済みで、ボード上ではまだ動作していません。
* **保存された秘密情報の任意の封印:** 既定ではオフです(`security.seal_secrets`、またはサーバーの `nodes.nvs_encryption`)。オンにすると、ノードが保存するパスワード、トークン、鍵、PIN、パスワードのハッシュが ChaCha20-Poly1305 で封印され、それ以外は読めるままです。オン/オフの切り替えは何も失わずに書き直し、途中で止まっても大丈夫です。eFuse は焼かれず、フラッシュも暗号化されません。鍵は同じチップのパーティションにあるため、基板を手にした人に対する保護には**なりません**。このパーティションがない時期にインストールされたノードは、新しいパーティションテーブルで書き込むまで従来のままです。""",
      "role": r"""ARMOR-NODE-ALARM は警報盤です。警戒区域、警戒、遅延、サイレン、PIN はノード自身で判断されるため、サーバーがいなくても家は守られます。[ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER) がこれを表示し、Zigbee センサーをゾーンに結び付け、許可すれば警戒・解除も行います。[ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) の*警報盤*メニューと*警報デザイナー*、[ARMOR-ANDROID-CONTROL](https://github.com/JuanenRac/ARMOR-ANDROID-CONTROL) アプリが操作します。Zigbee 無線は基板上でも、ネットワーク上のコーディネーターでも構いません。

| 名前 | 方法 | 用途 |
|---|---|---|
| ARMOR-SERVER | MQTT `armor/alarm/<id>/{state,command,result,zigbee,policy}` | パネルの状態を受け取り、アーム・ディスアーム・サイレンの命令は 3 つのスイッチを通した場合のみ |
| ARMOR-STUDIO | アラームパネルのメニュー | ゾーン、イベント、ポリシーを表示し、ノードのパネルを開く |
| ARMOR-ANDROID-CONTROL | Bluetooth | 現場でノードを設定し、アラームパネルを表示 |
| ARMOR-COMMON | アラームのコントラクト | メッセージはそのスキーマで検証し、共通ファームウェアはここからコピー |""",
      "architecture": r"""<p align="center">
  <img src="images/architecture.svg" alt="ARMOR-NODE-ALARM のアーキテクチャ：呼び出し元、内部、依存先" width="100%">
</p>""",
      "security": r"""| 脅威 | 対策 |
|---|---|
| 平文またはコンパイル済みのパスワード | PBKDF2-HMAC-SHA256 10 000 ラウンド。ファームウェアにパスワードはなく（ユーザーのないノードはセットアップに入る）、ユーザーは最大 4 人（管理者または閲覧者）、8〜64 文字、セッションは最大 6、無操作 30 分 |
| 書き込み直後のノードの乗っ取り | セットアップには起動コードが必要です。ビルドのもの（`CONFIG_ARMOR_SETUP_CODE`）か、フラッシュに保存して USB コンソールに表示するランダムなもの。フリートシークレットがあれば `HMAC-SHA256(シークレット, MAC)`。これはセットアップ用 Wi-Fi（WPA2、ブリッジなし）の鍵でもあります |
| インターネットからのパネルへのアクセス | 初期設定では家庭のプライベートネットワーク（10/8、172.16/12、192.168/16、169.254/16、127/8、一部の VPN が使う 100.64/10）にだけ応答します。設定 `web.admin_sources` で他の IPv4 アドレスやネットワークを追加でき（8 件、120 文字）、それ以外は公開の `GET /api/v1/session` を除き拒否します。保存した本人を締め出すリストは拒否されます |
| HTTP で平文のパネル | 443 番ポートで HTTPS。証明書はノード自身が作成（自己署名、フラッシュ保存、比較用に SHA-256 フィンガープリントを表示）。パネルは http、https、または両方を選べ、セッション Cookie は常に HttpOnly と SameSite=Strict（TLS では Secure も） |
| GitHub からの偽ファームウェア | SHA-256 が一致し、メンテナーの鍵による有効な Ed25519 署名があるイメージだけをインストールします（`no_checksum`、`no_signature`、`bad_signature`、`checksum_mismatch`、`wrong_firmware`、`not_newer`、`version_mismatch` は拒否）。管理者の手動アップロードは検証されません（明示した制限） |
| Bluetooth セットアップの乗っ取り | セットアップコードから導出した 6 桁の PIN を USB コンソールと管理者に表示し、設定を書き込む前にスマホで入力させます。セットアップの時間枠は `CONFIG_ARMOR_BLE_SETUP_MINUTES`（初期 10、1〜120） |
| 基板を持つ人による保存済みシークレットの読み取り | 任意（初期はオフ、スイッチ `security.seal_secrets` またはサーバーの `nodes.nvs_encryption`）：パスワード、トークン、鍵、PIN、ハッシュを ChaCha20-Poly1305 で保護。フラッシュ全体の暗号化や eFuse の焼き込みはしません。鍵は同じチップの別パーティションにあるため、基板を手にした人には防御になりません |
| ブローカーとの平文通信 | 任意の TLS（`mqtts://`）。所有者自身の認証局（PEM 2 KB まで）と名前の検証を使い、初期はオフです。ハンドシェイクはホストのテストでしか動いておらず、基板では未実行です |
| パネルの PIN の推測 | 比較はどこが違うかを漏らしません。連続した失敗は `lockout_s`（既定 60 秒、1〜3600）の 1、5、15 倍で最初の 3 回ロックし、正しい PIN でも拒否します。ロック中の状態は再起動後も復元されます。アームに PIN は不要ですが、ディスアームとサイレンには必要です |
| 家を無防備にする再起動 | モード、進行中のアラーム、除外したゾーンはフラッシュに保存して復元します。断線や短絡のループが除外されることはなく、ディスアーム中に作動した煙・パニック・改ざんは再起動後に戻ります。BOOT によるリセットはパネルがディスアームのときだけ消去します |
| 読み取れないゾーンが閉じて見える | `trouble` を表示し（コンバーターが起動しない、または 5 周期読み取りなし）、強制しない限りパネルはその状態でアームしません。強制すると除外して記録します。鳴動中の煙・パニック検知器は除外されません |
| 誰も許可していないサーバーからの命令 | サーバーからのアーム・ディスアーム・サイレンには 3 つのスイッチ（ノードの設定、ブローカーのアクセスリスト、サーバーの `ARMOR_ALARM_COMMANDS=1`）が必要で、サーバーはディスアームやサイレンの前にユーザーの PIN を求め、すべて初期はオフです。サイレンのリレーはアラームだけのもので、ブローカー、センター、パネルは動かせません |
| 偽の Zigbee メッセージ | トピック `armor/alarm/<id>/zigbee` は、ノード・ゾーン・状態・電池・シーケンスに対するパネルの鍵（パネルに入力した 64 桁の 16 進数）による HMAC-SHA256 を運び、シーケンスは増えるだけです。ポリシーのトピックは `config_hash`、`zone_feed` とその署名を運び、それぞれノード側で固定できます |

これは認証を受けた警報システムではありません（[docs/SAFETY.md](docs/SAFETY.md)）。家庭用プロジェクトで、基板でも実際の設置でも動いたことがありません。サーバーがなければパネルが単独で判断し、ノードやその無線も止まれば誰も見張っていません。脆弱性の報告は [SECURITY.md](SECURITY.md) を参照してください。""",
      "interfaces": r"""| 部分 | 設定内容 |
|---|---|
| MQTT | `armor/alarm/<id>/state`（保持なし：ID・名前・種類・状態・バイパスを持つゾーン、フェーズ）、`/command`、`/result`、`/zigbee`、`/policy`（サーバーからパネルへ）、`armor/device/<id>/<リレー>/{state,set}`、`armor/health/<id>`、`armor/control/<id>/...` |
| ゾーン | 種類は `instant`、`entry`、`interior`、`always`、状態は `normal`、`triggered`、`tamper`、`trouble`。配線ループは最大 8（終端抵抗つき接点を ADC で読み 1 ピンで 4 状態。Ethernet 基板のアナログピンは有効な 6 本、Wi-Fi 基板は 8 本）、ボタン 4 個、100 件のイベントログ |
| Zigbee | コーディネーターへのシリアルブリッジ（ZNP）、IAS Zone センサー、IAS WD サイレン。サーバーの Zigbee2MQTT が `zigbee_silence_min` の間沈黙するとノードが無線を引き継ぎ、サーバーが戻ると返します（[docs/ZIGBEE.md](docs/ZIGBEE.md)、[docs/FAILOVER.md](docs/FAILOVER.md)） |""",
      "configuration": r"""| 変数 | 既定値 | 設定内容 |
|---|---|---|
| `panel.exit_delay_s`, `panel.entry_delay_s` | 30, 30 (0-600) | 退出と入場の遅延。退出する人は侵入者として扱われません |
| `panel.lockout_s` | 60 (1-3600) | PIN のロック時間（最初の 3 回は 1、5、15 倍） |
| `zigbee_silence_min` | - | サーバーの Zigbee が沈黙してよい時間（超えるとノードが無線を引き継ぐ） |
| `CONFIG_ARMOR_NODE_ID`, `_SETUP_CODE`, `_FLEET_SECRET`, `_MQTT_*`, `_HEARTBEAT_S`, `_BLE_SETUP_MINUTES`, `_BOOT_FACTORY_RESET` | - | すべてのノードに共通する設定：名前（空なら `armor-` と MAC の下位バイト）、セットアップコード（空ならランダム）、フリートシークレット（16 文字以上、リポジトリには置かない）、最初のブローカー設定、ハートビート（2〜300 秒）、Bluetooth セットアップの分数（1〜120）、BOOT によるリセット（最初の 30 秒に 8 秒） |

サイレン停止後の再鳴動は 3 回までです（`kMaxResounds`）。サイレンのリレーは再起動のたびに開いた状態で始まり、ブローカーを失っても開きません。""",
      "quickstart": r"""**必要なもの:** ホストテスト用の C++17 コンパイラ、イメージのビルド用の ESP-IDF 5.5.5 コンテナ、ベース基板付きの ESP32-S3 基板（Ethernet または Wi-Fi）。

```bash
cmake -S tests -B build/host && cmake --build build/host && ctest --test-dir build/host   # host tests, -Werror
node tools/panel_mock.mjs --user admin:adminpass123   # the panel without a board
tools/build_node.sh generic s3-wifi                  # the image in the ESP-IDF container (or s3-eth)
```

[設計](docs/DESIGN.md)、[警報盤がサーバーから引き継ぐ方法](docs/FAILOVER.md)、[安全に関する注意](docs/SAFETY.md)を参照してください。""",
      "testing": r"""```bash
cmake -S tests -B build/host && cmake --build build/host && ctest --test-dir build/host
python -I tools/armor_ci_validate.py
```

ホスト用テストプログラム 18 個と Python の検査 5 個を `ctest` で実行します。ホストのプログラムが数えた検査は 488930 件で、`-Werror` でビルドします。

Python の検査：8 言語のパネル文言、タスク、保存パス、ロック下の Bluetooth セッション、パネルが呼ぶルート（ノードによっては HTTP コードやフォントのグリフも）

ホストテストには任意の C++17 コンパイラ（Linux、WSL、MSYS2）が必要です。Web パネルは代役ノード（`tools/panel_mock.mjs`、`tools/panel_browser_test.mjs`）を相手に実際のブラウザでも検証します。

検査の大半はパネルのルールの網羅的な総当たりで、ループ、サイレン、Zigbee 接続は代役です。""",
      "build": "`tools/build_node.sh` が ESP-IDF 5.5.5 コンテナでイメージをビルドし、リリースにはイメージ、その SHA-256 と Ed25519 署名が基板ごとに付きます。イメージは初回のみ USB-C で書き込み、その後はパネルから更新します。",
      "troubleshooting": r"""| 症状 | 原因 | 対処 |
|---|---|---|
| パスワードを忘れた、またはノードがネットワークに参加しない | セットアップ中でアドレスがないノードは 90 秒後に独自の Wi-Fi `ARMOR-SETUP-xxxxxx` を開きます（`http://192.168.4.1/` を開く） | 最初からやり直すには、電源投入後 30 秒以内に BOOT を 8 秒押し続ける（設定とユーザーを消去）か、パネルの*工場出荷状態に戻す*を使います |
| GitHub からの更新が拒否される | リリースにチェックサムや署名がない、一致しない（`e_no_checksum`、`e_no_signature`、`e_checksum_mismatch`、`e_bad_signature`）、この基板用のイメージがない（`e_no_asset_for_board`）、または別プロジェクトのもの（`e_wrong_firmware`） | ノードは変更されていません。再試行するか、管理者が手動でファイルをアップロード |
| パネルがアームできない | ゾーンが `trouble`（コンバーターが起動しない、または 5 周期読み取りなし） | 配線を直すか、強制アームする（その場合ゾーンは除外され記録される） |
| 正しい PIN でも拒否される | 失敗が続いてパネルがロック中（正しい PIN も拒否） | `lockout_s` だけ待つ（ロックは再起動後も続く） |
| BOOT のリセットが効かない | パネルがアーム中：リセットはディスアーム中のパネルだけを消去する | 先に PIN でディスアームする |""",
      "structure": r"""<p align="center">
  <img src="images/repository-structure.svg" alt="ARMOR-NODE-ALARM のリポジトリ構造" width="100%">
</p>

<details>
<summary>ツリーのテキスト版</summary>

```text
ARMOR-NODE-ALARM/
├── main/                                ファームウェア（ESP-IDF コンポーネント）
├── core/                                ESP-IDF なしのロジック（コンピューターでテスト）
├── panel/                               ファームウェアに埋め込まれた Web パネル
├── tests/                               ホストテストと Python 検査
├── docs/                                11 のガイド：安全、メッセージ、Zigbee、フェイルオーバー
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

* ノード自身のコーディネーター（ローカルまたはネットワーク上）との Zigbee のやり取りは、模擬のコーディネーターに対してのみテストしています。本物のコーディネーターやセンサーとはまだ接続していません。
* Web パネルは実ブラウザーで模擬ノードに対して試しており、ボード上では試していません。
* ボードは未製作で、ゾーンの配線もサイレンや Zigbee コーディネーターの接続もありません。実際の設備ではまだ何も動かしていません。
* ロックアウト付きの PIN、設定コード、ログイン制限、署名付きアップデートはホストでテスト済みです。独立したレビューはなく、認証を受けた警報システムでもありません。
* ハッシュと Ed25519 署名の確認、ロールバックの処理はホストで通ります。無線アップデートはボード上で一度も実行していません。
* サイレンとリレーは警報の規則で駆動され、模擬に対してテストしています。本物のサイレンやリレーには接続していません。

**今後**

* 実際のループとサイレンを配線し、実際のコーディネーターとセンサーで Zigbee 接続を試し、実際の設置でパネルを動かしてから、それ以上のことを主張する。""",
    },
  },
  "zh": {
    "tagline": "报警节点与报警主机：住宅报警的防区、布防、延时、警笛和 PIN，含节点固件和在电脑上测试过的规则（没有在电路板上运行过）",
    "honest": "目前存在的是**报警核心**（什么是防区、ADC 读取的有线回路如何变成状态、主机的规则：布防、延时、报警、警笛、带锁定的 PIN）以及建立在其上的**节点固件**（设置、网页面板、与服务器的消息、Zigbee 无线电的桥接、网络上的 Zigbee 协调器、继电器、蓝牙、签名更新），可为两种板子构建；核心、设置、消息以及在真实浏览器中对照替身节点的面板，在计算机上用 18 个测试程序中的 488,930 项检查进行测试。**没有任何东西在板上或真实安装中运行过，没有接过任何防区，也没有连接过警笛；节点自己与协调器（本地或网络上）的 Zigbee 对话已编写并对照替身协调器测试，但从未对照真实的协调器或传感器运行，而且这不是经过认证的报警系统。**",
    "glance": [
      [
        "角色",
        "ESP32-S3 报警面板现场节点（家族：Field Nodes，上级：ARMOR-COMMON）",
      ],
      [
        "技术栈",
        "C++17, ESP-IDF 5.5.5, ESP32-S3",
      ],
      [
        "测试",
        "488930 项检查（18 个主机程序和 5 项 Python 检查，`ctest`）",
      ],
      [
        "输入",
        "最多 8 个有线回路、Zigbee 传感器（IAS Zone）和警笛（IAS WD）、4 个按钮",
      ],
      [
        "运行位置",
        "带底板的 ESP32-S3 电路板（以太网或 Wi-Fi）；主机测试可在任何计算机上运行",
      ],
      [
        "真实硬件",
        "暂无：没有连接板子、防区、警笛或 Zigbee 协调器（仅有计算机测试、构建和浏览器中的面板）",
      ],
      [
        "许可证",
        "GPL-3.0-or-later",
      ],
    ],
    "status": {
      "software": "固件可在 ESP-IDF 5.5.5 容器中为两块板（Wi-Fi 和以太网）构建。",
      "tests": "18 个主机程序中的 488,930 项检查通过（`ctest`）：防区、由 ADC 读取的有线回路、布防、延时、警笛和 PIN 规则、设置和消息。",
      "protocols": "节点自身与协调器（本地或网络上）的 Zigbee 通信只对照模拟协调器测试过；从未遇到过真实的协调器或传感器。",
      "ui": "网页面板已在真实浏览器中对模拟节点测试过，尚未在板子上测试。",
      "hardware": "尚未制作板子，没有接线的防区，也没有连接警笛或 Zigbee 协调器：还没有在真实的安装中运行过。",
      "security": "带锁定的 PIN、设置码、登录限制和签名更新已在主机上测试；没有经过独立审查，这也不是经过认证的报警系统。",
      "updates": "哈希和 Ed25519 签名检查以及回滚逻辑在主机上通过；空中更新从未在板子上运行过。",
      "writing": "警笛和继电器由报警规则驱动，并对照模拟测试过；都没有连接到真实的警笛或继电器。",
      "integration": "节点的消息已对照 ARMOR-COMMON 的共享模式和一致性向量验证。",
      "docs": "八种语言、固件指南、接线说明和更新日志均为最新。",
    },
    "docs": [
      "[安全](docs/SAFETY.md)：面板承诺什么、不承诺什么",
      "[报警消息](docs/ALARM_MESSAGES.md)、[Zigbee](docs/ZIGBEE.md)和[故障接管](docs/FAILOVER.md)",
      "[设计](docs/DESIGN.md)、[硬件](docs/HARDWARE.md)、[底板](docs/BASE_BOARD.md)和[节点固件](docs/NODE_FIRMWARE.md)",
      "[台架测试](docs/BENCH_TESTS.md)、[设置码](docs/SETUP_CODE.md)和[蓝牙配置](docs/BLE_PROVISIONING.md)",
    ],
    "contributing_first": "提交 Pull Request 之前请运行 `ctest --test-dir build/host` and `python -I tools/armor_ci_validate.py`：必须通过。参见 [CONTRIBUTING.md](CONTRIBUTING.md) 和[行为准则](CODE_OF_CONDUCT.md)。",
    "languages_extra": "",
    "body": {
      "overview": r"""* **防区：** 四种类型 - *即时*（门、窗）、*进入*（进门用的门：触发进入延时）、*内部*（移动探测：仅在“离家”时）和*全天*（烟雾、燃气、紧急按钮：无论布防与否）。防区可以是有线回路或 Zigbee 传感器。
* **有线回路：** 带终端电阻的触点，以电压方式读取，一个引脚给出四种状态 - 正常、触发，以及线路短路或剪断的防拆。阈值是设置项；去抖器避免抖动的触点引发报警。
* **主机：** *离家*和*在家*两种布防，不把离开的人当作入侵者的退出延时，进入延时，需要正确撤防才会解除的**锁定报警**，一段时间后自动停止的警笛，强制布防时旁路已打开的防区（响着的烟雾探测器永远不会被旁路），以及最近一百条事件的日志。
* **PIN：** 布防不需要，撤防和消音需要；输错的 PIN 会被计数，几次之后一段时间内一切都会被拒绝，连正确的 PIN 也不例外。
* **不撤防也能消音：** 警笛鸣响时，正确的 PIN 可让它立即停止，而系统仍保持布防 - 报警保持锁定并被记录，尚未响过的防区可再次触发警笛，输错的 PIN 与撤防时输错的 PIN 一样计入锁定。
* **计划：** 在电气节点电路板上的网关（Zigbee 无线电、有线防区、警笛继电器），与 ARMOR-SERVER 配合，并在**服务器离线时继续守护**：主机通过 ARMOR-NODE-ELECTRICAL 的 Zigbee 桥接从服务器手中接管无线电。参见[设计](docs/DESIGN.md)和[接管](docs/FAILOVER.md)。
* **节点：** ESP32-S3 固件（PoE 以太网或 Wi-Fi），最多八个有线防区，警笛接在继电器上，所有节点通用的八种语言网页面板，借给 Zigbee2MQTT 的 Zigbee 无线电，以及消息 `armor/alarm/<节点>/state|command|result`；只有三个相互独立的开关都允许时，服务器才能布防和撤防。参见[固件](docs/NODE_FIRMWARE.md)、[消息](docs/ALARM_MESSAGES.md)和[硬件](docs/HARDWARE.md)。
* **接管无线电：** 服务器的 Zigbee2MQTT 缺席设定时间后，节点自行启动协调器（ZNP），读取指定了传感器的防区（IAS Zone）并控制 Zigbee 警笛（IAS WD），客户端一回来就交还。
* **尚未完成：** 真实的协调器或传感器、硬件，以及在真实设施上的任何测试。
* **重启不会让房子撤防：** 模式、正在进行的报警和被旁路的防区保存在闪存中，启动时恢复；被剪断或短路的回路永远不会被旁路；消息经队列发送（与代理不会死锁），读取防区的任务停止时看门狗会重启开发板。
* **签名的无线更新：**节点只会从 GitHub 安装 SHA-256 匹配且带有维护者有效 Ed25519 签名的镜像（公钥在固件中，私钥从不离开维护者）；管理员在面板中手动上传的文件仍然被接受。面板的页面和消息有八种语言。
* **带 PIN 的蓝牙配对：**六位 PIN 由设置码派生，打印在 USB 控制台上并向管理员显示在面板中；手机必须输入它才能写入节点的设置。
* **警笛与重启：**警笛继电器只属于报警系统（代理、中心和面板都不能控制它，失去代理时它也不会断开）；尚未鸣响过的防区会在警笛超时后让它再次鸣响；重启后，撤防状态下的烟雾或紧急报警、已静音的报警和锁定都会恢复；布防时拒绝手动复位；从未发声的 Zigbee 传感器视为丢失。
* **只有家中才能使用面板：**面板默认只响应私有网络（或所有者列出的网络，如 VPN），拒绝会把保存者自己挡在外面的列表，按人和按地址统计错误密码，并可在服务器代理之后工作，从而无需公开节点就能在家外访问。
* **无法读取的防区不会显示为已闭合：** 如果转换器无法启动，或某回路连续五轮没有读数，该防区会进入*故障*（trouble）状态：它不守护、从不触发警笛、会阻止布防（强制布防时将其排除并记录），服务器会发出警告。
* **可选的与代理加密连接(TLS):** 默认关闭,因此节点仍像以前一样使用未加密的 MQTT。代理页面中的一个开关和一个用于填写本安装自有证书颁发机构证书(PEM,最大 2 KB)的框,会让节点用 `mqtts://` 连接、只信任该机构,并检查代理证书是否为其所到达的地址而签发;不是单个 PEM 证书的内容会被拒绝。已有主机测试覆盖;握手尚未在电路板上运行。
* **布防配置：** 布防命令可以带一个配置（离家、在家、夜间或自定义），为这次布防选择哪些分区守护、哪些分区立即报警或在进入延时后报警、退出和进入延时，以及警笛是否鸣响（静音报警仍会锁定、记录和通知）。它绝不触及烟雾、紧急按钮或防拆分区、PIN、锁定、消音、强制布防或故障分区；配置在重启后保留，不带配置的布防行为与以前完全一致。已通过随机运行对照旧规则测试，并对照共享契约测试。
* **健康报告：** 节点大约每分钟发布一次：已运行多久、上次为何重启、可用内存、连接与 Wi-Fi 信号、连接代理的次数以及记录的最后一个错误（`armor/health/<节点>`，即 ARMOR-COMMON 的 `node_health` 契约）。生成它的代码由所有节点共享并在计算机上测试；尚未在开发板上运行。
* **由服务器控制：** Studio 可以干净地重启节点、将其暂停至多一小时（自动恢复）、让其工作进入待机（无期限，重启后仍保持，节点保持连接并继续应答）、让它显示自己、请求诊断快照，并把它标记为维护中（`armor/control/<节点>/...`，ARMOR-COMMON 的 `node_control` 契约）。每条命令分两步，使用只属于该操作的一次性令牌，只有服务器可以在代理上写入，并且没有恢复出厂设置、擦除或深度睡眠。节点处于暂停或待机时，不读取防区，不做任何判断、布防或鸣响，不发布状态，警笛继电器保持断开：住宅没有受到保护，健康报告会如实说明。 该代码由所有节点共用，并已在计算机上测试；尚未在电路板上运行过。
* **无需线缆的诊断：** 在一次不干净的启动之后（崩溃、看门狗、电源跌落、内存分配失败），健康报告会在十分钟内说明原因；崩溃会留下核心转储（core dump），可在面板中查看、下载或删除；已保存的设置会在每次固件安装前被复制，并在更新损坏它们时恢复；管理员还可以通过服务器，用一次性令牌向节点索取诊断包或其日志。
* **服务器的安全选项：**面板会应用服务器为它保存的选项（`armor/alarm/<节点>/policy`），每一项也可以在节点本身固定：已保存的布防状态与防区和 PIN 绑定，服务器的 Zigbee 防区消息可以关闭，带签名时会被校验（用在面板中输入的密钥验签，序列号只增不减）。已在计算机上按合同和服务器计算的值测试；尚未在开发板上运行。
* **可选的已存储机密封存:** 默认关闭(`security.seal_secrets`,或服务器的 `nodes.nvs_encryption`)。开启后,节点保存的密码、令牌、密钥、PIN 和密码哈希会用 ChaCha20-Poly1305 封存,其余内容仍可读取;开启或关闭时会无损重写,即使节点中途停止也不会丢失。不会烧写 eFuse,闪存也不加密:密钥在同一芯片的一个分区中,因此**不能**防范持有电路板的人;在该分区出现之前安装的节点会保持原样,直到用新的分区表重新烧录。""",
      "role": r"""ARMOR-NODE-ALARM 是报警主机：防区、布防、延时、警笛和 PIN 都在节点自身上决定，因此服务器不在时住宅仍受守护。[ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER) 显示它，把 Zigbee 传感器绑定到其防区，并在你允许时对它布防和撤防；[ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) 的*报警主机*菜单和*报警设计器*以及 [ARMOR-ANDROID-CONTROL](https://github.com/JuanenRac/ARMOR-ANDROID-CONTROL) 应用可控制它。它的 Zigbee 无线电可以在板上，也可以是网络上的协调器。

| 名称 | 方式 | 用途 |
|---|---|---|
| ARMOR-SERVER | MQTT `armor/alarm/<id>/{state,command,result,zigbee,policy}` | 接收面板状态；仅在三个开关都开启时下达布防、撤防和静音命令 |
| ARMOR-STUDIO | 报警面板菜单 | 显示区域、事件和策略，并打开节点面板 |
| ARMOR-ANDROID-CONTROL | Bluetooth | 在现场设置节点并显示报警面板 |
| ARMOR-COMMON | 报警合约 | 消息按其模式校验；公共固件由此复制 |""",
      "architecture": r"""<p align="center">
  <img src="images/architecture.svg" alt="ARMOR-NODE-ALARM 的架构：谁调用它、它包含什么、它依赖什么" width="100%">
</p>""",
      "security": r"""| 威胁 | 防御 |
|---|---|
| 明文或编译进固件的密码 | PBKDF2-HMAC-SHA256，10 000 轮；固件中没有密码（没有用户的节点会进入设置）；最多 4 个用户（管理员或查看者），8 到 64 个字符；最多 6 个会话，空闲 30 分钟 |
| 接管刚刷写的节点 | 设置需要启动码：构建时的码（`CONFIG_ARMOR_SETUP_CODE`），或保存在闪存中并显示在 USB 控制台上的随机码；有机群密钥时为 `HMAC-SHA256(密钥, MAC)`；它也是设置用 Wi-Fi 的密钥（WPA2，绝不桥接） |
| 从互联网访问面板 | 默认只响应家庭的私有网络（10/8、172.16/12、192.168/16、169.254/16、127/8，以及某些 VPN 使用的 100.64/10）；设置 `web.admin_sources` 可列出其他 IPv4 地址和网络（8 项，120 个字符）；除公开身份 `GET /api/v1/session` 外，其余一律拒绝；会把保存者自己锁在外面的列表会被拒绝 |
| 通过 HTTP 明文访问面板 | 在 443 端口提供 HTTPS，证书由节点自己生成（自签名、存于闪存，显示 SHA-256 指纹以便比对）；面板可设为 http、https 或两者；会话 Cookie 始终为 HttpOnly 和 SameSite=Strict（TLS 下还有 Secure） |
| 来自 GitHub 的伪造固件 | 只有 SHA-256 匹配且带有维护者密钥有效 Ed25519 签名的镜像才会被安装（`no_checksum`、`no_signature`、`bad_signature`、`checksum_mismatch`、`wrong_firmware`、`not_newer`、`version_mismatch` 会拒绝）；管理员手动上传不做校验：这是明确的限制 |
| 劫持蓝牙设置 | 由设置码派生的 6 位 PIN，显示在 USB 控制台并对管理员可见；手机必须先输入才能写入设置；设置窗口时长为 `CONFIG_ARMOR_BLE_SETUP_MINUTES`（默认 10，范围 1 到 120） |
| 拿到电路板的人读取存储的机密 | 可选（默认关闭，开关为 `security.seal_secrets` 或服务器的 `nodes.nvs_encryption`）：用 ChaCha20-Poly1305 保护密码、令牌、密钥、PIN 和哈希。它不加密闪存也不烧写 eFuse：密钥位于同一芯片的分区中，因此无法防御拿到电路板的人 |
| 与代理的明文连接 | 可选 TLS（`mqtts://`），使用所有者自己的证书颁发机构（PEM 最大 2 KB）并检查名称；默认关闭。握手只在主机测试中运行过，没有在电路板上运行 |
| 猜测面板 PIN | 比较不会泄露差异所在；连续失败会把面板锁定 `lockout_s`（默认 60 秒，1 到 3600），前三次锁定分别乘以 1、5、15，即使输入正确 PIN 也会拒绝；进行中的锁定在重启后会恢复；布防不需要 PIN，撤防和静音需要 |
| 让住宅撤防的重启 | 模式、进行中的报警和被排除的区域都保存在闪存中并会恢复；断线或短路的回路绝不会被排除；撤防时触发的烟雾、紧急和防拆报警在重启后会重新出现；BOOT 重置只在面板已撤防时才擦除 |
| 无法读取的区域看起来是闭合的 | 显示 `trouble`（转换器无法启动或连续 5 轮无读数），除非强制，否则面板不会带着它布防，强制后它会被排除并记录；正在鸣响的烟雾或紧急探测器绝不会被排除 |
| 无人授权的服务器命令 | 来自服务器的布防、撤防和静音需要三个开关（节点设置、代理的访问列表和服务器上的 `ARMOR_ALARM_COMMANDS=1`），服务器在发送撤防或静音前会询问用户的 PIN，且一切默认关闭；警笛继电器只属于报警本身（代理、中心和面板都无法驱动它） |
| 伪造的 Zigbee 消息 | 主题 `armor/alarm/<id>/zigbee` 携带用面板密钥（在面板中输入的 64 位十六进制）对节点、区域、状态、电池和序号计算的 HMAC-SHA256，且序号只会增加；策略主题携带 `config_hash`、`zone_feed` 及其签名，每一项都可以在节点上固定 |

这不是经过认证的报警系统（[docs/SAFETY.md](docs/SAFETY.md)）：它是家庭项目，从未在电路板或真实安装中运行过。服务器缺失时面板独自决策，若节点或其无线电也失效，则无人监视。报告漏洞请阅读 [SECURITY.md](SECURITY.md)。""",
      "interfaces": r"""| 部分 | 作用 |
|---|---|
| MQTT | `armor/alarm/<id>/state`（不保留：含 ID、名称、类型、状态和旁路的区域，以及阶段）、`/command`、`/result`、`/zigbee` 和 `/policy`（服务器到面板）；`armor/device/<id>/<继电器>/{state,set}`、`armor/health/<id>`、`armor/control/<id>/...` |
| 区域 | 类型为 `instant`、`entry`、`interior` 或 `always`；状态为 `normal`、`triggered`、`tamper` 或 `trouble`；最多 8 个有线回路（带终端电阻的触点由 ADC 读取，一个引脚给出四种状态；以太网电路板有 6 个可用模拟引脚，Wi-Fi 电路板有 8 个）、4 个按钮和 100 条事件日志 |
| Zigbee | 通往协调器的串口桥（ZNP）、IAS Zone 传感器和 IAS WD 警笛；当服务器的 Zigbee2MQTT 沉默超过 `zigbee_silence_min` 时，节点接管无线电，服务器恢复后归还（[docs/ZIGBEE.md](docs/ZIGBEE.md)、[docs/FAILOVER.md](docs/FAILOVER.md)） |""",
      "configuration": r"""| 变量 | 默认值 | 作用 |
|---|---|---|
| `panel.exit_delay_s`, `panel.entry_delay_s` | 30, 30 (0-600) | 离开和进入的延时；离开的人不会被当作入侵者 |
| `panel.lockout_s` | 60 (1-3600) | PIN 锁定时间，前三次分别乘以 1、5、15 |
| `zigbee_silence_min` | - | 服务器的 Zigbee 可沉默多久，之后节点接管无线电 |
| `CONFIG_ARMOR_NODE_ID`, `_SETUP_CODE`, `_FLEET_SECRET`, `_MQTT_*`, `_HEARTBEAT_S`, `_BLE_SETUP_MINUTES`, `_BOOT_FACTORY_RESET` | - | 所有节点共有的设置：名称（为空则为 `armor-` 加 MAC 的最后字节）、设置码（为空则随机）、机群密钥（16 个字符以上，绝不放入仓库）、最初的代理设置、心跳（2 到 300 秒）、蓝牙设置的分钟数（1 到 120）以及用 BOOT 重置（前 30 秒内按 8 秒） |

静音后的再次鸣响限制为 3 次（`kMaxResounds`）。警笛继电器每次重启时处于断开状态，代理丢失时也不会自动断开。""",
      "quickstart": r"""**要求:** 用于主机测试的 C++17 编译器；用于构建镜像的 ESP-IDF 5.5.5 容器；带底板的 ESP32-S3 电路板（以太网或 Wi-Fi）。

```bash
cmake -S tests -B build/host && cmake --build build/host && ctest --test-dir build/host   # host tests, -Werror
node tools/panel_mock.mjs --user admin:adminpass123   # the panel without a board
tools/build_node.sh generic s3-wifi                  # the image in the ESP-IDF container (or s3-eth)
```

参见[设计](docs/DESIGN.md)、[主机如何接替服务器](docs/FAILOVER.md)和[安全说明](docs/SAFETY.md)。""",
      "testing": r"""```bash
cmake -S tests -B build/host && cmake --build build/host && ctest --test-dir build/host
python -I tools/armor_ci_validate.py
```

`ctest` 运行 18 个主机测试程序和 5 个 Python 检查；主机程序统计的检查共 488930 项，使用 `-Werror` 构建。

Python 检查：八种语言的面板文字、任务、保存路径、受锁保护的蓝牙会话以及面板调用的路由（部分节点还包括 HTTP 状态码或字体字形）

主机测试需要任意 C++17 编译器（Linux、WSL、MSYS2）；网页面板还会在真实浏览器中对着模拟节点（`tools/panel_mock.mjs`、`tools/panel_browser_test.mjs`）进行验证。

大部分检查是对面板规则的穷举遍历；回路、警笛和 Zigbee 连接都是替身。""",
      "build": "`tools/build_node.sh` 在 ESP-IDF 5.5.5 容器中构建镜像，发布版带有镜像、其 SHA-256 和 Ed25519 签名，每块电路板一份；镜像第一次通过 USB-C 写入，之后从面板更新。",
      "troubleshooting": r"""| 现象 | 原因 | 处理 |
|---|---|---|
| 忘记了密码，或节点不再加入网络 | 处于设置状态且 90 秒后仍无地址的节点会开启自己的 Wi-Fi `ARMOR-SETUP-xxxxxx`（打开 `http://192.168.4.1/`） | 要重新开始，请在上电后 30 秒内按住 BOOT 8 秒（会清除设置和用户），或使用面板中的*恢复出厂设置* |
| 来自 GitHub 的更新被拒绝 | 发布版缺少校验和或签名，或二者不匹配（`e_no_checksum`、`e_no_signature`、`e_checksum_mismatch`、`e_bad_signature`），没有适用于此电路板的镜像（`e_no_asset_for_board`），或属于另一个项目（`e_wrong_firmware`） | 节点未发生任何变化；请重试，或由管理员手动上传文件 |
| 面板无法布防 | 某个区域处于 `trouble`（转换器无法启动或连续 5 轮无读数） | 修复接线，或强制布防（该区域随后被排除并记录） |
| 即使 PIN 正确也被拒绝 | 多次失败后面板被锁定（即使正确 PIN 也会被拒绝） | 等待 `lockout_s`；锁定在重启后仍然有效 |
| BOOT 重置没有反应 | 面板处于布防状态：重置只会擦除已撤防的面板 | 先用 PIN 撤防 |""",
      "structure": r"""<p align="center">
  <img src="images/repository-structure.svg" alt="ARMOR-NODE-ALARM 的仓库结构" width="100%">
</p>

<details>
<summary>目录树的文本版</summary>

```text
ARMOR-NODE-ALARM/
├── main/                                固件：一个 ESP-IDF 组件
├── core/                                不依赖 ESP-IDF 的逻辑，在计算机上测试
├── panel/                               嵌入固件的网页面板
├── tests/                               主机测试和 Python 检查
├── docs/                                11 份指南：安全、消息、Zigbee、故障接管
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

* 节点自身与协调器（本地或网络上）的 Zigbee 通信只对照模拟协调器测试过；从未遇到过真实的协调器或传感器。
* 网页面板已在真实浏览器中对模拟节点测试过，尚未在板子上测试。
* 尚未制作板子，没有接线的防区，也没有连接警笛或 Zigbee 协调器：还没有在真实的安装中运行过。
* 带锁定的 PIN、设置码、登录限制和签名更新已在主机上测试；没有经过独立审查，这也不是经过认证的报警系统。
* 哈希和 Ed25519 签名检查以及回滚逻辑在主机上通过；空中更新从未在板子上运行过。
* 警笛和继电器由报警规则驱动，并对照模拟测试过；都没有连接到真实的警笛或继电器。

**下一步**

* 连接真实的回路和警笛，用真实的协调器和传感器试验 Zigbee 连接，并在真实安装中运行面板，之后才能做出更多声明。""",
    },
  },
  "pt": {
    "tagline": "Nó e central de alarme: as zonas, a armação, os atrasos, a sirene e o PIN do alarme da casa, com o firmware do nó e as regras testadas num computador (nada correu numa placa)",
    "honest": "O que existe é o **núcleo do alarme** (o que é uma zona, como um laço com fios lido pelo ADC se torna um estado, as regras da central: armar, atrasos, o alarme, a sirene, o PIN com bloqueio) e o **firmware do nó** construído sobre ele (definições, painel web, mensagens com o servidor, a ponte do rádio Zigbee, um coordenador Zigbee na rede, relés, Bluetooth, atualizações assinadas), que compila para as duas placas; o núcleo, as definições, as mensagens e o painel num navegador real contra um nó de substituição são testados num computador com 477 588 verificações em 6 programas de teste. **Nada correu numa placa nem numa instalação real, nenhuma zona foi ligada com fios nem sirene ligada, a conversa Zigbee do próprio nó com um coordenador (local ou na rede) está escrita e testada contra um coordenador de substituição mas nunca correu contra um coordenador ou sensor reais, e isto não é um sistema de alarme certificado.**",
    "glance": [
      [
        "Função",
        "Nó de campo central de alarme para ESP32-S3 (família: Field Nodes, pai: ARMOR-COMMON)",
      ],
      [
        "Tecnologia",
        "C++17, ESP-IDF 5.5.5, ESP32-S3",
      ],
      [
        "Testes",
        "488930 verificações em 18 programas de anfitrião e 5 em Python (`ctest`)",
      ],
      [
        "Entradas",
        "Até 8 laços cablados, sensores Zigbee (IAS Zone) e sirene (IAS WD), 4 botões",
      ],
      [
        "Funciona em",
        "Uma placa ESP32-S3 (Ethernet ou Wi-Fi) com a placa base; testes de anfitrião em qualquer computador",
      ],
      [
        "Em hardware real",
        "Nenhum ainda: nenhuma placa, zona, sirene ou coordenador Zigbee ligados (só testes no computador, a compilação e o painel num navegador)",
      ],
      [
        "Licença",
        "GPL-3.0-or-later",
      ],
    ],
    "status": {
      "software": "O firmware compila no contentor ESP-IDF 5.5.5 para as duas placas (Wi-Fi e Ethernet).",
      "tests": "Passam 488.930 verificações em 18 programas de anfitrião (`ctest`): as zonas, os laços cablados lidos pelo ADC, as regras de armar, atrasos, sirene e PIN, as definições e as mensagens.",
      "protocols": "A conversa Zigbee do próprio nó com um coordenador, local ou na rede, só foi testada contra um coordenador simulado; nunca encontrou um coordenador ou um sensor reais.",
      "ui": "O painel web foi exercitado num navegador real contra um nó simulado, não numa placa.",
      "hardware": "Nenhuma placa construída, nenhuma zona cablada e nenhuma sirene ou coordenador Zigbee ligados: nada funcionou numa instalação real.",
      "security": "O PIN com bloqueio, o código de configuração, o limite de acessos e as atualizações assinadas estão testados no anfitrião; não houve revisão independente e este não é um sistema de alarme certificado.",
      "updates": "As verificações de hash e de assinatura Ed25519 e a lógica de retrocesso passam no anfitrião; uma atualização pelo ar nunca foi executada numa placa.",
      "writing": "A sirene e os relés são comandados pelas regras do alarme e testados contra simulações; nenhum foi ligado a uma sirene ou a um relé reais.",
      "integration": "As mensagens do nó são validadas contra os esquemas partilhados e os vetores de conformidade do ARMOR-COMMON.",
      "docs": "Oito idiomas, o guia do firmware, as notas de cablagem e o registo de alterações estão atualizados.",
    },
    "docs": [
      "[Segurança](docs/SAFETY.md): o que a central promete e o que não",
      "[Mensagens de alarme](docs/ALARM_MESSAGES.md), [Zigbee](docs/ZIGBEE.md) e [redundância](docs/FAILOVER.md)",
      "[Desenho](docs/DESIGN.md), [hardware](docs/HARDWARE.md), [placa base](docs/BASE_BOARD.md) e [firmware do nó](docs/NODE_FIRMWARE.md)",
      "[Testes de bancada](docs/BENCH_TESTS.md), [código de configuração](docs/SETUP_CODE.md) e [provisionamento Bluetooth](docs/BLE_PROVISIONING.md)",
    ],
    "contributing_first": "Antes de um pull request, execute `ctest --test-dir build/host` and `python -I tools/armor_ci_validate.py`: tem de passar. Consulte [CONTRIBUTING.md](CONTRIBUTING.md) e o [código de conduta](CODE_OF_CONDUCT.md).",
    "languages_extra": "",
    "body": {
      "overview": r"""* **Zonas:** quatro tipos - *instantânea* (uma porta, uma janela), *de entrada* (a porta por onde entra: inicia o atraso de entrada), *interior* (movimento: só em «ausente») e *sempre* (fumo, gás, pânico: armada ou não). Uma zona pode ser um laço com fio ou um sensor Zigbee.
* **O laço com fio:** um contacto com uma resistência de fim de linha, lido como tensão, dá quatro estados num só pino - normal, disparado, e violação por um fio em curto-circuito ou cortado. Os limites são definições; um filtro de repique impede que um contacto que salta dispare o alarme.
* **A central:** armação *ausente* e *em casa*, um atraso de saída que não trata como intruso quem sai, um atraso de entrada, um alarme que **fica retido** até um desarme correto, uma sirene que pára sozinha passado um tempo, desvio de zonas abertas quando forçado (nunca um detetor de fumo a soar), e um registo dos últimos cem eventos.
* **O PIN:** armar não precisa de nenhum, desarmar e silenciar sim; os PIN errados contam-se e, passados alguns, tudo se recusa durante um tempo, mesmo o PIN certo.
* **Silenciar sem desarmar:** enquanto a sirene soa, um PIN certo pára-a logo com o sistema ainda armado - o alarme fica retido e registado, uma zona que ainda não soou pode voltar a fazê-la soar, e um PIN errado conta para o bloqueio como um errado de desarmar.
* **O plano:** uma ponte na placa do nó elétrico (um rádio Zigbee, zonas com fio, um relé de sirene) que funciona com o ARMOR-SERVER e **continua a vigiar quando o servidor está ausente**: uma central toma o rádio ao servidor através da ponte Zigbee do ARMOR-NODE-ELECTRICAL. Veja [o desenho](docs/DESIGN.md) e [a continuidade](docs/FAILOVER.md).
* **O nó:** firmware para o ESP32-S3 (Ethernet PoE ou Wi-Fi) com até oito zonas com fio, a sirene num relé, o painel web de cada nó em oito idiomas, o rádio Zigbee emprestado ao Zigbee2MQTT, e as mensagens `armor/alarm/<node>/state|command|result`; o servidor só pode armar e desarmar quando três interruptores independentes o permitem. Veja [o firmware](docs/NODE_FIRMWARE.md), [as mensagens](docs/ALARM_MESSAGES.md) e [o hardware](docs/HARDWARE.md).
* **Tomar o rádio:** depois de o Zigbee2MQTT do servidor ter estado ausente durante um tempo definido, o nó levanta ele próprio o coordenador (ZNP), lê os sensores das zonas que o nomeiam (IAS Zone) e comanda sirenes Zigbee (IAS WD), e larga-o assim que o cliente volta.
* **Ainda não:** um coordenador ou sensor real, o hardware e qualquer teste numa instalação real.
* **Um reinício não desarma a casa:** o modo, um alarme em curso e as zonas deixadas de fora guardam-se na flash e retomam-se no arranque; um laço cortado ou em curto-circuito nunca se deixa de fora; as mensagens passam por uma fila (sem bloqueio mútuo com o broker) e o cão de guarda reinicia a placa se a tarefa que lê as zonas parar.
* **Atualizações pelo ar assinadas:** o nó só instala do GitHub uma imagem cujo SHA-256 coincide e que leva uma assinatura Ed25519 válida do responsável (a chave pública está no firmware, a privada nunca sai do responsável); um ficheiro carregado à mão por um administrador no painel continua a ser aceite. As páginas e mensagens do painel estão em oito idiomas.
* **Emparelhamento Bluetooth com PIN:** o PIN de seis dígitos deriva do código de configuração, é impresso na consola USB e mostrado a um administrador no painel; o telemóvel tem de o introduzir antes de poder escrever as definições do nó.
* **Sirene e reinícios:** o relé da sirene pertence só ao alarme (nem o broker, nem a central, nem o painel o podem mover, e não abre ao perder o broker); uma zona que ainda não tinha tocado volta a fazer soar a sirene depois do seu tempo; após um reinício voltam um alarme de fumo ou pânico com o sistema desarmado, um alarme silenciado e um bloqueio; um reset à mão é recusado com o alarme armado; um sensor Zigbee que nunca fala conta como perdido.
* **Só a casa pode usar o painel:** o painel responde por omissão à rede privada (ou às redes que o dono indicar, como uma VPN), recusa uma lista que deixaria de fora quem a guarda, conta as palavras-passe erradas por pessoa e por endereço e funciona atrás do proxy do servidor para ser alcançado de fora de casa sem publicar o nó.
* **Uma zona que não pode ser lida não aparece como fechada:** se o conversor não arranca ou um laço não dá leitura cinco rondas seguidas, a zona passa a *avaria* (trouble) - não vigia, nunca faz soar a sirene, impede armar (salvo forçando, e então fica excluída e registada) e o servidor avisa.
* **Ligação cifrada opcional ao broker (TLS):** desativada por predefinição, por isso o nó fala MQTT sem cifra como antes. Um interruptor e uma caixa para o certificado da autoridade própria da instalação (PEM, no máximo 2 KB) na página Broker fazem-no ligar-se com `mqtts://`, confiar só nessa autoridade e verificar que o certificado do broker foi feito para o endereço alcançado; o que não for um único certificado PEM é recusado. Coberto por testes no computador; o handshake ainda não foi executado numa placa.
* **Perfis de armar:** um comando de armar pode levar um perfil (Ausente, Em casa, Noite, o seu) que escolhe, para esse armar, que zonas vigiam, quais disparam o alarme logo ou após o atraso de entrada, os atrasos de saída e de entrada e se a sirene toca (um alarme silencioso fica trancado, registado e avisado). Nunca toca nas zonas de fumo, pânico ou sabotagem, no PIN, no bloqueio, no silêncio, num armar forçado nem numa zona com problema; o perfil sobrevive a um reinício e um armar sem perfil comporta-se exatamente como antes. Testado contra as regras antigas com uma execução aleatória e contra o contrato partilhado.
* **Relatório de saúde:** cerca de uma vez por minuto o nó publica há quanto tempo está ligado e porque reiniciou da última vez, a memória livre, a ligação e o sinal Wi-Fi, quantas vezes se ligou ao broker e o último erro que registou (`armor/health/<nó>`, o contrato `node_health` do ARMOR-COMMON). O código que o constrói é partilhado por todos os nós e testado num computador; nunca correu numa placa.
* **Controlo a partir do servidor:** o Studio pode reiniciar o nó de forma limpa, pô-lo em pausa até uma hora (retoma sozinho), pôr o seu trabalho em espera (sem fim, mantida nos reinícios, o nó continua ligado e a responder), fazê-lo mostrar-se, pedir um instantâneo de diagnóstico e marcá-lo em manutenção (`armor/control/<nó>/...`, o contrato `node_control` do ARMOR-COMMON). Cada ordem tem dois passos com um token de uso único que pertence a essa operação, só o servidor as pode escrever no broker, e não existe reposição de fábrica, apagamento nem sono profundo. Enquanto o nó está em pausa ou em espera, as suas zonas não são lidas, nada é avaliado, armado ou tocado, nenhum estado é publicado e o relé da sirene fica aberto: a casa NÃO está protegida, e o relatório de saúde di-lo. O código é partilhado por todos os nós e testado num computador; ainda não correu numa placa.
* **Diagnóstico sem cabo:** depois de um arranque que não foi limpo (um bloqueio, um watchdog, uma quebra de alimentação, uma reserva de memória falhada), o relatório de saúde diz o motivo durante dez minutos; uma falha deixa o seu core dump para ver, descarregar ou apagar a partir do painel; as definições guardadas são copiadas antes de cada instalação de firmware e recuperadas se uma atualização as danificar; e um administrador pode pedir ao nó, através do servidor, um pacote de diagnóstico ou o seu registo com um token de utilização única.
* **As opções de segurança do servidor:** a central aplica as opções que o servidor guarda para ela (`armor/alarm/<nó>/policy`) e cada uma pode ser fixada no próprio nó: o estado armado guardado fica atado às zonas e ao PIN, as mensagens de zona Zigbee do servidor podem ser desligadas e, se assinadas, são verificadas (assinatura com uma chave escrita no painel e um número de sequência que só aumenta). Testado num computador com os valores que o contrato e o servidor calculam; não executado numa placa.
* **Selagem opcional dos segredos guardados:** desativada por predefinição (`security.seal_secrets`, ou `nodes.nvs_encryption` do servidor). Ativada, as palavras-passe, os tokens, as chaves, os PIN e os hashes de palavras-passe que o nó guarda ficam selados com ChaCha20-Poly1305 e tudo o resto continua legível; ativá-la ou desativá-la reescreve-os sem perder nada, mesmo que o nó pare a meio. Não se queima nenhum eFuse nem se cifra a flash: a chave está numa partição do mesmo chip, pelo que **não** protege contra quem tenha a placa, e um nó instalado antes dessa partição mantém os segredos como estavam até ser gravado com a nova tabela de partições.""",
      "role": r"""O ARMOR-NODE-ALARM é a central de alarme: as zonas, o armar, os atrasos, a sirene e o PIN decidem-se no próprio nó, por isso a casa continua vigiada quando o servidor não está. O [ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER) mostra-a, liga sensores Zigbee às suas zonas e, quando o permitir, arma-a e desarma-a; o menu *Centrais de alarme* e o *Desenhador de alarme* do [ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) e a aplicação [ARMOR-ANDROID-CONTROL](https://github.com/JuanenRac/ARMOR-ANDROID-CONTROL) comandam-na. O seu rádio Zigbee pode estar na placa ou ser um coordenador na rede.

| Nome | Como | Para quê |
|---|---|---|
| ARMOR-SERVER | MQTT `armor/alarm/<id>/{state,command,result,zigbee,policy}` | Recebe o estado da central; ordena armar, desarmar e silenciar só atrás de três interruptores |
| ARMOR-STUDIO | menu de centrais de alarme | Mostra as zonas, os eventos e a política, e abre o painel do nó |
| ARMOR-ANDROID-CONTROL | Bluetooth | Configura o nó no terreno e mostra as centrais de alarme |
| ARMOR-COMMON | contrato de alarme | As mensagens são verificadas com os seus esquemas; o firmware comum é copiado dele |""",
      "architecture": r"""<p align="center">
  <img src="images/architecture.svg" alt="Arquitetura de ARMOR-NODE-ALARM: quem o chama, o que contém e de que depende" width="100%">
</p>""",
      "security": r"""| Ameaça | Defesa |
|---|---|
| Palavras-passe em claro ou compiladas | PBKDF2-HMAC-SHA256 com 10 000 rondas; nenhuma palavra-passe no firmware (um nó sem utilizador entra em configuração); no máximo 4 utilizadores (admin ou visualizador) e de 8 a 64 caracteres; no máximo 6 sessões, 30 minutos de inatividade |
| Tomar um nó acabado de gravar | A configuração exige um código de arranque: o da compilação (`CONFIG_ARMOR_SETUP_CODE`) ou um aleatório guardado na flash e mostrado na consola USB; com segredo de frota é `HMAC-SHA256(segredo, MAC)`; é também a chave do Wi-Fi de configuração (WPA2, nunca em ponte) |
| O painel alcançado a partir da internet | Responde por omissão às redes privadas de uma casa (10/8, 172.16/12, 192.168/16, 169.254/16, 127/8 e 100.64/10 onde vivem algumas VPN); a definição `web.admin_sources` lista outros endereços e redes IPv4 (8 entradas, 120 caracteres); tudo o que está fora é recusado exceto a identidade pública `GET /api/v1/session`; uma lista que deixaria de fora quem a guarda é rejeitada |
| O painel em claro por HTTP | HTTPS no 443 com um certificado que o nó cria sozinho (autoassinado, na flash, impressão digital SHA-256 visível para comparar); o painel pode ser http, https ou ambos; o cookie de sessão é sempre HttpOnly e SameSite=Strict (e Secure por TLS) |
| Um firmware falso do GitHub | Uma imagem só se instala com um SHA-256 coincidente e uma assinatura Ed25519 válida feita com a chave do mantenedor (`no_checksum`, `no_signature`, `bad_signature`, `checksum_mismatch`, `wrong_firmware`, `not_newer`, `version_mismatch` recusam-na); um envio manual por um administrador não é verificado: um limite explícito |
| Sequestro da configuração Bluetooth | Um PIN de 6 dígitos derivado do código de configuração, visível na consola USB e ao administrador; o telemóvel tem de o introduzir antes de escrever definições; a janela dura `CONFIG_ARMOR_BLE_SETUP_MINUTES` (10 por omissão, de 1 a 120) |
| Segredos guardados lidos por quem tem a placa | Opcional (desligado por omissão, interruptor `security.seal_secrets` ou `nodes.nvs_encryption` do servidor): ChaCha20-Poly1305 para palavras-passe, tokens, chaves, PIN e hashes. Não cifra a flash nem queima um eFuse: a chave está numa partição do mesmo chip, por isso não protege contra quem tem a placa |
| A ligação ao broker em claro | TLS opcional (`mqtts://`) com a autoridade própria do dono (PEM até 2 KB) e verificação do nome; desligado por omissão. O handshake só correu em testes de anfitrião, não numa placa |
| Adivinhar o PIN da central | A comparação não revela onde difere; falhas seguidas bloqueiam a central `lockout_s` (60 s por omissão, de 1 a 3600) vezes 1, 5 e 15 nos três primeiros bloqueios, mesmo para o PIN certo; um bloqueio em curso é restaurado após um reinício; armar não leva PIN, desarmar e silenciar sim |
| Um reinício que desarma a casa | O modo, o alarme em curso e as zonas excluídas guardam-se na flash e recuperam-se; um laço cortado ou em curto nunca fica de fora; fumo, pânico e sabotagem disparados com o sistema desarmado voltam após reiniciar; o reset com BOOT só apaga com a central DESARMADA |
| Uma zona ilegível parece fechada | Mostra `trouble` (o conversor não arranca ou 5 rondas sem leitura) e a central não arma com ela a não ser forçado, e então fica excluída e anotada; um detetor de fumo ou pânico que está a soar nunca é excluído |
| Uma ordem do servidor que ninguém autorizou | Armar, desarmar e silenciar a partir do servidor exigem TRÊS interruptores (a definição do nó, a lista de acesso do broker e `ARMOR_ALARM_COMMANDS=1` no servidor), o servidor pede o PIN do utilizador antes de enviar um desarme ou um silêncio, e tudo está desligado por omissão; o relé da sirene pertence só ao alarme (nem o broker, nem a central nem o painel o podem mover) |
| Mensagens Zigbee forjadas | O tópico `armor/alarm/<id>/zigbee` leva um HMAC-SHA256 sobre nó, zona, estado, bateria e sequência com a chave da central (64 hex digitados no painel), e a sequência só sobe; o tópico da política leva `config_hash`, `zone_feed` e a sua assinatura, cada um dos quais pode ser fixado no nó |

Não é um sistema de alarme certificado ([docs/SAFETY.md](docs/SAFETY.md)): é um projeto doméstico e nunca correu numa placa nem numa instalação real. Se o servidor faltar a central decide sozinha, e se também falhar o nó ou o seu rádio ninguém vigia. Leia [SECURITY.md](SECURITY.md) para comunicar uma vulnerabilidade.""",
      "interfaces": r"""| Parte | O que define |
|---|---|
| MQTT | `armor/alarm/<id>/state` (não retido: zonas com id, nome, tipo, estado e exclusão, a fase), `/command`, `/result`, `/zigbee` e `/policy` (servidor para central); `armor/device/<id>/<relé>/{state,set}`, `armor/health/<id>`, `armor/control/<id>/...` |
| Zonas | Tipo `instant`, `entry`, `interior` ou `always`; estado `normal`, `triggered`, `tamper` ou `trouble`; até 8 laços cablados (um contacto com resistência de fim de linha lido pelo ADC dá quatro estados num pino; a placa Ethernet tem 6 pinos analógicos válidos, a Wi-Fi 8), 4 botões e um registo de 100 eventos |
| Zigbee | Uma ponte série (ZNP) para um coordenador, sensores IAS Zone e sirenes IAS WD; o nó toma o rádio quando o Zigbee2MQTT do servidor se cala durante `zigbee_silence_min` e devolve-o quando o servidor volta ([docs/ZIGBEE.md](docs/ZIGBEE.md), [docs/FAILOVER.md](docs/FAILOVER.md)) |""",
      "configuration": r"""| Variável | Predefinição | O que define |
|---|---|---|
| `panel.exit_delay_s`, `panel.entry_delay_s` | 30, 30 (0-600) | Os atrasos de saída e de entrada; a saída não trata como intruso quem se vai |
| `panel.lockout_s` | 60 (1-3600) | O bloqueio do PIN, vezes 1, 5 e 15 nos três primeiros |
| `zigbee_silence_min` | - | Quanto tempo o Zigbee do servidor se pode calar antes de o nó tomar o rádio |
| `CONFIG_ARMOR_NODE_ID`, `_SETUP_CODE`, `_FLEET_SECRET`, `_MQTT_*`, `_HEARTBEAT_S`, `_BLE_SETUP_MINUTES`, `_BOOT_FACTORY_RESET` | - | As definições que todos os nós partilham: o nome (vazio dá `armor-` e os últimos bytes do MAC), o código de configuração (vazio: aleatório), o segredo de frota (16+ caracteres, nunca no repositório), as primeiras definições do broker, o batimento (de 2 a 300 s), os minutos de configuração Bluetooth (de 1 a 120) e a reposição com BOOT (8 s nos primeiros 30 s) |

Os novos toques depois de um silêncio estão limitados a 3 (`kMaxResounds`). O relé da sirene arranca aberto a cada reinício e não cai para aberto se o broker se perder.""",
      "quickstart": r"""**Requisitos:** um compilador C++17 para os testes de anfitrião; o contentor ESP-IDF 5.5.5 para compilar a imagem; uma placa ESP32-S3 (Ethernet ou Wi-Fi) com a placa base.

```bash
cmake -S tests -B build/host && cmake --build build/host && ctest --test-dir build/host   # host tests, -Werror
node tools/panel_mock.mjs --user admin:adminpass123   # the panel without a board
tools/build_node.sh generic s3-wifi                  # the image in the ESP-IDF container (or s3-eth)
```

Veja o [desenho](docs/DESIGN.md), [como a central toma o lugar do servidor](docs/FAILOVER.md) e as [notas de segurança](docs/SAFETY.md).""",
      "testing": r"""```bash
cmake -S tests -B build/host && cmake --build build/host && ctest --test-dir build/host
python -I tools/armor_ci_validate.py
```

18 programas de teste de anfitrião e 5 verificações Python correm com `ctest`; 488930 verificações contadas pelos programas de anfitrião, compiladas com `-Werror`.

Verificações Python: os textos do painel em oito línguas, as tarefas, os caminhos de gravação, a sessão Bluetooth sob o seu bloqueio e as rotas que o painel chama (e, em alguns nós, os códigos HTTP ou os glifos dos tipos de letra)

Os testes de anfitrião precisam de qualquer compilador C++17 (Linux, WSL, MSYS2); o painel web também é exercitado num navegador real contra um nó de substituição (`tools/panel_mock.mjs`, `tools/panel_browser_test.mjs`).

A maior parte das verificações são varrimentos exaustivos das regras da central; os laços, a sirene e a ligação Zigbee são substitutos.""",
      "build": "`tools/build_node.sh` compila a imagem no contentor ESP-IDF 5.5.5 e a versão leva a imagem, o seu SHA-256 e a sua assinatura Ed25519, uma por placa; a imagem grava-se por USB-C da primeira vez e depois atualiza-se a partir do painel.",
      "troubleshooting": r"""| Vê | Porque | Faça |
|---|---|---|
| Perdeu a palavra-passe ou o nó já não se liga à rede | Um nó em configuração e sem endereço após 90 s abre o seu próprio Wi-Fi `ARMOR-SETUP-xxxxxx` (abra `http://192.168.4.1/`) | Para recomeçar mantenha BOOT 8 segundos nos primeiros 30 segundos após ligar (apaga definições e utilizadores), ou use *Reposição de fábrica* no painel |
| Uma atualização do GitHub é recusada | A versão não traz soma de verificação nem assinatura, não coincidem (`e_no_checksum`, `e_no_signature`, `e_checksum_mismatch`, `e_bad_signature`), não traz imagem para esta placa (`e_no_asset_for_board`) ou é de outro projeto (`e_wrong_firmware`) | O nó não mudou; tente de novo ou deixe um administrador enviar o ficheiro à mão |
| A central não arma | Uma zona está em `trouble` (o conversor não arranca ou 5 rondas sem leitura) | Corrija a cablagem, ou force a armação (a zona fica então excluída e anotada) |
| O PIN é recusado mesmo estando certo | A central está bloqueada após tentativas falhadas (até o PIN certo é recusado) | Espere `lockout_s`; o bloqueio sobrevive a um reinício |
| O reset com BOOT não faz nada | A central está armada: o reset só apaga uma central desarmada | Desarme primeiro com o PIN |""",
      "structure": r"""<p align="center">
  <img src="images/repository-structure.svg" alt="Estrutura do repositório de ARMOR-NODE-ALARM" width="100%">
</p>

<details>
<summary>Versão em texto da árvore</summary>

```text
ARMOR-NODE-ALARM/
├── main/                                o firmware: um componente ESP-IDF
├── core/                                a lógica sem ESP-IDF, testada num computador
├── panel/                               o painel web embebido no firmware
├── tests/                               testes de anfitrião e verificações Python
├── docs/                                11 guias: segurança, mensagens, Zigbee, redundância
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

* A conversa Zigbee do próprio nó com um coordenador, local ou na rede, só foi testada contra um coordenador simulado; nunca encontrou um coordenador ou um sensor reais.
* O painel web foi exercitado num navegador real contra um nó simulado, não numa placa.
* Nenhuma placa construída, nenhuma zona cablada e nenhuma sirene ou coordenador Zigbee ligados: nada funcionou numa instalação real.
* O PIN com bloqueio, o código de configuração, o limite de acessos e as atualizações assinadas estão testados no anfitrião; não houve revisão independente e este não é um sistema de alarme certificado.
* As verificações de hash e de assinatura Ed25519 e a lógica de retrocesso passam no anfitrião; uma atualização pelo ar nunca foi executada numa placa.
* A sirene e os relés são comandados pelas regras do alarme e testados contra simulações; nenhum foi ligado a uma sirene ou a um relé reais.

**A seguir**

* Cablar laços e uma sirene reais, experimentar a ligação Zigbee com um coordenador e sensores reais, e correr a central numa instalação real antes de afirmar mais seja o que for.""",
    },
  },
}
