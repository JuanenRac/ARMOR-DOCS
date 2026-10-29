# The facts that do not depend on the language, and the words of every language, of ARMOR-NODE-HMI, in the universal README layout.
# Copyright (C) 2026 JuanenRac (Electro Hobby 3D). GPL-3.0-or-later.

FACTS = {
  "emoji": "🖥️",
  "layout": "universal",
  "license_badge": "License-GPL%203.0--or--later-blue",
  "status": [
    [
      "software",
      "orange",
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
      "orange",
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
      "Board",
      "ESP32--S3--Touch--LCD--7C--BOX",
      "e7352c",
    ],
    [
      "Checks",
      "1%2C759",
      "2ea44f",
    ],
    [
      "Tests",
      "93081%20checks",
      "2ea44f",
    ],
  ],
}

TEXT = {
  "en": {
    "tagline": "The touch panel of the house: a 7-inch screen on the wall that shows the state of the system, arms and disarms it and acknowledges alarms, with a microphone and a speaker for the voice assistant to come (a node of the family on the ESP32-S3-Touch-LCD-7C-BOX, with its own web page for the settings)",
    "honest": "What does not depend on the board is real and tested on a computer (the settings, what the panel knows of the server and when that is stale, the duress alarm that is never shown, the voice conversation and the long answer of the speech service, the board's pins, the words of the screen in eight languages and the glyphs of its fonts, the release and signature checks: 93,081 checks in 18 test programs) and so is the web page (run against a stand-in in a real browser). **The firmware has been built once (ESP-IDF 5.5.5, not checked by the continuous integration) and has never run on a board:** the screen, the touch, the sound and the link to the server are written from Waveshare's examples for this family of boards and need their first power-up. The speech service (ARMOR-VOICE-AI) answers this panel's requests, there is no wake word: it is push to talk.",
    "glance": [
      [
        "Role",
        "Wall touch panel for ARMOR-SERVER (family: Clients, parent: ARMOR-SERVER)",
      ],
      [
        "Stack",
        "C++17, ESP-IDF 5.5.5, LVGL, ESP32-S3",
      ],
      [
        "Tests",
        "93081 checks in 18 host programs and 6 Python checks (`ctest`)",
      ],
      [
        "Board",
        "Waveshare ESP32-S3-Touch-LCD-7C-BOX (800x480, GT911)",
      ],
      [
        "Runs on",
        "A Waveshare ESP32-S3-Touch-LCD-7C-BOX; host tests on any computer",
      ],
      [
        "On real hardware",
        "None yet: the firmware builds (ESP-IDF 5.5.5, not checked by CI) but has not run on the board",
      ],
      [
        "License",
        "GPL-3.0-or-later",
      ],
    ],
    "status": {
      "software": "The firmware has been built once (ESP-IDF 5.5.5), but the build is not checked by the continuous integration and it has never run on a board.",
      "tests": "93,081 checks in 18 host programs pass (`ctest`): the settings, what the panel knows of the server and when that is stale, the duress alarm that is never shown, the voice exchange, the pins, the words of the screen in eight languages and the glyphs of its fonts.",
      "protocols": "The exchange with the server and with the speech service ARMOR-VOICE-AI is tested against stand-ins; it is push to talk, with no wake word.",
      "ui": "The web page runs against a stand-in in a real browser; the screen, the touch and the sound are written from Waveshare's examples and wait for their first power-up.",
      "hardware": "The firmware has not run on the board: nothing has run on real equipment yet.",
      "security": "The set-up code, the login limit, the Bluetooth PIN, the duress handling and the signed updates are tested on the host; there has been no independent review.",
      "updates": "The hash and signature checks pass on the host; an update over the air has never been run on a board.",
      "integration": "The messages are validated against the shared schemas of ARMOR-COMMON; the link to the server and to the speech service has not been tried from a board.",
      "docs": "Eight languages, the firmware guide, the wiring notes and the changelog are up to date.",
    },
    "docs": [
      "[Design](docs/DESIGN.md) and [hardware](docs/HARDWARE.md): what the panel shows and the board",
      "[Voice](docs/VOICE.md) and [fonts](docs/FONTS.md)",
      "[Node firmware](docs/NODE_FIRMWARE.md) and [firmware build actions](docs/FIRMWARE_BUILD_ACTIONS.md)",
      "[Bench tests](docs/BENCH_TESTS.md), [set-up code](docs/SETUP_CODE.md) and [Bluetooth provisioning](docs/BLE_PROVISIONING.md)",
    ],
    "contributing_first": "Before a pull request run `ctest --test-dir build/host` and `python -I tools/armor_ci_validate.py`: it must pass. See [CONTRIBUTING.md](CONTRIBUTING.md) and the [code of conduct](CODE_OF_CONDUCT.md).",
    "languages_extra": "",
    "body": {
      "overview": r"""* **A client of ARMOR-SERVER, like the Android app:** it signs in with a user an administrator made for it, asks `GET /api/v1/panel/summary` (a few hundred bytes: the mode, the nodes online and the alarms that need a person) every few seconds and, when the person touches the button and confirms, arms, disarms or acknowledges. If the server stops answering the screen says that what it shows is old and the button is disabled. It listens to the server's live channel (a WebSocket) so a change shows at once, and asks as before when the channel is missing, silent or turned off.
* **The screen (800x480, LVGL):** the mode in the colour of the worst alarm nobody has seen, a large arm/disarm button with a question first, the nodes online, the alarms (the unseen first), a night that dims it, a sleep after a time without touches, a tone and a wake-up when a new alarm arrives, and eight languages with accents, Japanese and Chinese drawn with fonts generated for exactly the characters used.
* **A node like the others:** the same settings store, Wi-Fi, web page in eight languages, Bluetooth set-up from the phone, firmware update with roll-back and HTTPS as ARMOR-NODE-RADAR, ARMOR-NODE-SOLAR and ARMOR-NODE-ELECTRICAL (they share `ARMOR-COMMON/firmware_base`), plus pages for the server, the screen, the sound and the voice; it tells Studio it exists over MQTT so Studio lists it with its page.
* **The voice assistant, push to talk:** a touch opens the microphone, the audio goes only to the speech service whose address is in the settings (off by default), the reply is shown and spoken; the order of the steps, the time limits and what a touch does are a tested state machine, and the panel carries out no command by itself ([the contract](docs/VOICE.md)). The recording goes as raw bytes in a binary request and the spoken answer comes back as bytes; a server that does not accept it is sent the older request.
* **The board:** Waveshare ESP32-S3-Touch-LCD-7C-BOX (32 MB flash, 16 MB PSRAM, a 7-inch RGB screen with a GT911 touch, four microphones, a speaker); the pins come from Waveshare's examples and a test proves that no two functions share a GPIO ([the board](docs/HARDWARE.md)).
* **Signed over-the-air updates:** the node installs from GitHub only an image whose SHA-256 matches and that carries a valid Ed25519 signature of the maintainer (the public key is in the firmware, the private one never leaves the maintainer); a file uploaded by hand by an administrator in the panel is still accepted. The pages and messages of the panel are in eight languages.
* **Bluetooth pairing with a PIN:** the six-digit PIN is derived from the set-up code, printed on the USB console and shown to an administrator in the panel; the phone has to enter it before it may write the node's settings.
* **Not yet:** a first compilation and power-up of the firmware, a wake word, the speech service on the Jetson, and a view of the cameras on the screen.
* **Only the house may use the panel:** the panel answers the private network by default (or the networks its owner lists, such as a VPN), refuses a list that would lock out whoever saves it, counts wrong passwords for each person as well as each address, and works behind the server's proxy so that it can be reached from outside the house without publishing the node.
* **It says what happens:** the screen knows the text, in eight languages, of every alarm code the server raises (network, solar, electrical, alarm zones...), and it tells the server that it is a wall panel, so it is listed as one and does not count as a radar.
* **Optional encrypted link to the broker (TLS):** off by default, so the node talks plain MQTT as before. A switch and a box for the certificate of the installation's own authority (PEM, at most 2 KB) in the Broker page make it connect with `mqtts://`, trust that authority only and check that the broker's certificate was made for the address it reached; anything that is not one PEM certificate is refused. Covered by host tests; the handshake has not been run on a board yet.
* **Health report:** about once a minute the node publishes how long it has been up and why it last restarted, its free memory, its link and Wi-Fi signal, how many times it connected to the broker and the last error it logged (`armor/health/<node>`, the `node_health` contract of ARMOR-COMMON). The code that builds it is shared by every node and tested on a computer; it has not run on a board.
* **Control from the server:** Studio can restart the node cleanly, pause it for up to an hour (it resumes by itself), put its work in standby (no end, kept across restarts, the node stays connected and keeps answering), make it show itself, ask for a diagnostics snapshot and mark it as in maintenance (`armor/control/<node>/...`, the `node_control` contract of ARMOR-COMMON). Every order takes two steps with a one-time token that belongs to that operation, only the server may write them on the broker, and there is no factory reset, no erase and no deep sleep. While the panel is paused or in standby the screen shows a screen of its own that says so and takes no touch; while it is asked to identify itself, a bar blinks at the top (never a sound). The code is shared by every node and tested on a computer; it has not run on a board.
* **Diagnostics without a cable:** after a start that was not clean (a crash, a watchdog, a sag of the supply, a failed allocation) the health report says why for ten minutes; a crash leaves its core dump to look at, download or erase from the panel; the stored settings are copied before every firmware install and recovered if an update damages them; and an administrator can ask the node, through the server, for a diagnostic package or its log with a one-time token.
* **A siren that repeats, and sounds in order:** every sound goes through one priority queue (siren, alarm, voice, confirmation, notice); the siren repeats while critical alarms nobody has acknowledged remain (`audio.siren_repeat_s` 30, `audio.siren_max_repeats` 10) and alarms keep a minimum volume (`audio.critical_min_volume` 40); a voice yields to an alarm.
* **A battery-backed clock:** the board's PCF85063A chip gives the time at start when the node has no real time yet and the chip can be trusted, and it is corrected whenever the time is synchronised or set (`time.rtc_enabled`, on by default).
* **The state of an order, on the screen:** the footer says the order is being sent while it is on its way and that it was confirmed for a few seconds when it went through; a refusal keeps its reason there, as before.
* **Optional sealing of stored secrets:** off by default (`security.seal_secrets`, or the server's `nodes.nvs_encryption`). When on, the passwords, tokens, keys, PINs and password hashes the node stores are kept sealed with ChaCha20-Poly1305 and everything else stays readable; turning it on or off rewrites them with nothing lost, even if the node stops half-way. No eFuse is burned and the flash is not encrypted: the key lives in a partition of the same chip, so it does **not** protect against someone who holds the board, and a node installed before that partition existed keeps its secrets as they were until it is flashed with the new partition table.""",
      "role": r"""ARMOR-NODE-HMI is the wall panel: a client of [ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER), like the Android app, with a 7-inch screen, a microphone and a speaker. It shows the mode, the nodes online and the alarms that need a person, arms and disarms (with the PIN) and acknowledges alarms. It is where the voice assistant ([ARMOR-VOICE-AI](https://github.com/JuanenRac/ARMOR-VOICE-AI)) will live once its speech service exists, and, like every node, it is set up and updated from [ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO).

| Name | How | What for |
|---|---|---|
| ARMOR-SERVER | HTTPS `GET /api/v1/panel/summary`, WebSocket `/api/v1/panel/events` | The summary of the house (modes, alarms, nodes, energy) and its changes; the server decides what an order does |
| ARMOR-VOICE-AI | through the server | The audio of one turn goes to the speech service; the reply is shown and spoken |
| ARMOR-STUDIO | Touch panel menu | Shows the health of the panel and opens its web panel |
| ARMOR-COMMON | firmware base | The common firmware (panel, logins, signed update, Bluetooth set-up) is copied from it |""",
      "architecture": r"""<p align="center">
  <img src="images/architecture.svg" alt="ARMOR-NODE-HMI architecture: who calls it, what it holds and what it depends on" width="100%">
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
| The duress alarm shown on the screen | It is never shown (a host test checks it); and what the panel knows of the server is marked as stale when it is old |
| A server that is not the server | The certificate of the server is pinned (`server_pin`), for the requests and for the WebSocket of the live channel; the panel signs in with its own user, created by an administrator, with the role `panel` (it cannot use Studio) |
| Disarming without a PIN | Arming and disarming ask first and take the PIN on the screen (`pin_entry`); the server checks it again |
| Voice audio to an unexpected place | Off by default (`voice.enabled` false); the audio goes only to the service whose address is in the settings (the address is validated and changing the host erases the token); the panel carries out no command by itself and there is no wake word: it is push to talk |
| A siren that nobody hears | One priority queue (siren, alarm, voice, confirmation, notice); the siren repeats while critical alarms are unconfirmed (`audio.siren_repeat_s` 30, 10 to 600, 0 = no repeats; `audio.siren_max_repeats` 10) and the critical volume never goes under `audio.critical_min_volume` (40 %) |

The firmware has been built once and has never run on a board: the screen, the touch, the sound and the link to the server are written from the examples of Waveshare, waiting for the first power-up. Read [SECURITY.md](SECURITY.md) to report a vulnerability.""",
      "interfaces": r"""| Part | What it sets |
|---|---|
| ARMOR-SERVER | `GET /api/v1/panel/summary` every `server.poll_s` (3 s, 1 to 60) only while the live channel is down, and the WebSocket `/api/v1/panel/events` while `server.live_events` is true (the default): the summary arrives when the mode, the alarms, the nodes or the energy change; the panel's own user has the role `panel` |
| Voice | The audio of one turn goes to ARMOR-VOICE-AI through the server (`/api/v1/voice/turn`, with an optional multipart body); `core/voice_session.hpp` is the state machine (order of the steps, time limits, what a touch does); see [docs/VOICE.md](docs/VOICE.md) |
| Hardware | Waveshare ESP32-S3-Touch-LCD-7C-BOX: 7 inch RGB screen 800x480, GT911 touch, four microphones, a speaker, RTC PCF85063A (`time.rtc_enabled`, true by default), 32 MB of flash and 16 MB of PSRAM; a test proves that no function shares a GPIO |""",
      "configuration": r"""| Variable | Default | What it sets |
|---|---|---|
| `server.poll_s`, `server.live_events` | 3 (1-60), true | The polling period of the summary and the live channel by WebSocket |
| `display.sleep_s` | 300 (0-3600) | Seconds until the screen sleeps (0 = never); the brightness and the night brightness are also settings |
| `audio.critical_min_volume`, `audio.siren_repeat_s`, `audio.siren_max_repeats` | 40 (0-100), 30, 10 | The lowest volume of a critical sound, the siren repeat period (0 or 10 to 600 s) and its maximum repeats |
| `audio.tone_by_source` | by severity | The sound of each alarm source (device, solar, electrical, network, central, other): as its severity says, as a notice, as an alarm, as a siren, or no sound; a chosen sound plays even below the minimum severity |
| `voice.enabled`, `voice.url`, `voice.token` | false, "", - | The voice service: off by default; the address is at most 160 characters and is validated (`required` or `invalid` otherwise); the token is erased when the host changes |
| `CONFIG_ARMOR_NODE_ID`, `_SETUP_CODE`, `_FLEET_SECRET`, `_MQTT_*`, `_HEARTBEAT_S`, `_BLE_SETUP_MINUTES`, `_BOOT_FACTORY_RESET` | - | The settings every node shares: the name (empty gives `armor-` and the last bytes of the MAC), the set-up code (empty: random), the fleet secret (16+ characters, never in the repository), the first broker settings, the heartbeat (2 to 300 s), the minutes of Bluetooth set-up (1 to 120) and the reset with BOOT (8 s in the first 30 s) |""",
      "quickstart": r"""**Requirements:** a C++17 compiler for the host tests; the ESP-IDF 5.5.5 container to build the image; a Waveshare ESP32-S3-Touch-LCD-7C-BOX.

```bash
cmake -S tests -B build/host && cmake --build build/host && ctest --test-dir build/host   # host tests, -Werror
node tools/panel_mock.mjs --user admin:adminpass123   # the panel of the node without a board
tools/build_node.sh                                   # the image in the ESP-IDF container
```

See the [firmware guide](docs/NODE_FIRMWARE.md) and the [Bluetooth channel](docs/BLE_PROVISIONING.md).

See the [design](docs/DESIGN.md), the [board](docs/HARDWARE.md), the [voice assistant](docs/VOICE.md), the [firmware guide](docs/NODE_FIRMWARE.md) and the [fonts](docs/FONTS.md).

To build the firmware by hand on GitHub Actions, see [building on GitHub Actions](docs/FIRMWARE_BUILD_ACTIONS.md).""",
      "testing": r"""```bash
cmake -S tests -B build/host && cmake --build build/host && ctest --test-dir build/host
python -I tools/armor_ci_validate.py
```

18 host test programs and 6 Python checks run under `ctest`; 93081 checks counted by the host programs, built with `-Werror`.

Python checks: the panel texts in eight languages, the tasks, the save paths, the Bluetooth session under its lock and the routes the panel calls (and, in some nodes, the HTTP codes or the glyphs of the fonts)

The host tests need any C++17 compiler (Linux, WSL, MSYS2); the web panel is also exercised in a real browser against a stand-in node (`tools/panel_mock.mjs`, `tools/panel_browser_test.mjs`).

`check_font_glyphs.py` checks that the fonts hold every glyph of the eight languages (98 rows); `test_clock` prints only `ok`.""",
      "build": "`tools/build_node.sh` builds the image in the ESP-IDF 5.5.5 container and the release carries the image, its SHA-256 and its Ed25519 signature, one per board; the image is written by USB-C the first time and updated from the panel afterwards.",
      "troubleshooting": r"""| You see | Because | Do |
|---|---|---|
| You lost the password or the node no longer joins the network | A node with set-up and no address after 90 s opens its own Wi-Fi `ARMOR-SETUP-xxxxxx` (open `http://192.168.4.1/`) | To start again hold BOOT for 8 seconds in the first 30 seconds after power-up (erases settings and users), or use *Factory reset* in the panel |
| An update from GitHub is refused | The release has no checksum or signature, they do not match (`e_no_checksum`, `e_no_signature`, `e_checksum_mismatch`, `e_bad_signature`), has no image for this board (`e_no_asset_for_board`) or is for another project (`e_wrong_firmware`) | Nothing changed on the node; try again or let an administrator upload the file by hand |
| The voice does not start | `voice.enabled` is off, or `voice.url` is `required` or `invalid` | Turn it on in the panel and give a valid address; changing the host erases the token |
| The footer says sending, then confirmed or the reason | An order is on its way, was confirmed for a few seconds, or was refused and keeps its reason | Read the reason; the server decides, not the panel |""",
      "structure": r"""<p align="center">
  <img src="images/repository-structure.svg" alt="Repository structure of ARMOR-NODE-HMI" width="100%">
</p>

<details>
<summary>Text version of the tree</summary>

```text
ARMOR-NODE-HMI/
├── main/                                the firmware: an ESP-IDF component
├── core/                                the logic with no ESP-IDF, tested on a computer
├── panel/                               the web panel embedded in the firmware
├── tests/                               host tests and Python checks
├── docs/                                9 guides: design, voice, fonts, hardware
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
├── sdkconfig.board.lcd7box              the settings of one board
├── secrets/                             example of the node file (the real ones are not versioned)
├── dependencies.lock                    the pinned versions of the ESP-IDF components
├── build-test.sh build-test.bat         run the tests through the shared workflow
└── .gitattributes .gitignore            Git settings
```

</details>""",
      "roadmap": r"""**Known limits today**

* The firmware has been built once (ESP-IDF 5.5.5), but the build is not checked by the continuous integration and it has never run on a board.
* The exchange with the server and with the speech service ARMOR-VOICE-AI is tested against stand-ins; it is push to talk, with no wake word.
* The web page runs against a stand-in in a real browser; the screen, the touch and the sound are written from Waveshare's examples and wait for their first power-up.
* The firmware has not run on the board: nothing has run on real equipment yet.
* The set-up code, the login limit, the Bluetooth PIN, the duress handling and the signed updates are tested on the host; there has been no independent review.
* The hash and signature checks pass on the host; an update over the air has never been run on a board.
* The messages are validated against the shared schemas of ARMOR-COMMON; the link to the server and to the speech service has not been tried from a board.

**Next**

* Do the first full build and the first power-up on the board, then the speech service on the Jetson, a wake word and the camera view on the screen.""",
    },
  },
  "es": {
    "tagline": "El panel táctil de la casa: una pantalla de 7 pulgadas en la pared que muestra el estado del sistema, lo arma y desarma y reconoce alarmas, con micrófono y altavoz para el asistente de voz que vendrá (un nodo de la familia en la ESP32-S3-Touch-LCD-7C-BOX, con su propia página web de ajustes)",
    "honest": "Lo que no depende de la placa es real y está probado en un ordenador (los ajustes, lo que el panel sabe del servidor y cuándo está desfasado, la alarma de coacción que nunca se muestra, la conversación de voz y la respuesta larga del servicio de voz, los pines de la placa, los textos de la pantalla en ocho idiomas y los glifos de sus fuentes, las comprobaciones de versión y firma: 30,783 comprobaciones en 18 programas de test) y también lo está la página web (ejecutada contra un sustituto en un navegador real). **El firmware se ha compilado una vez (ESP-IDF 5.5.5, que la integración continua no comprueba) y nunca ha corrido en una placa:** la pantalla, el táctil, el sonido y el enlace con el servidor están escritos a partir de los ejemplos de Waveshare para esta familia de placas y necesitan su primer encendido. El servicio de voz (ARMOR-VOICE-AI) atiende las peticiones de este panel; no hay palabra de activación: es pulsar para hablar.",
    "glance": [
      [
        "Función",
        "Panel táctil de pared para ARMOR-SERVER (familia: Clients, padre: ARMOR-SERVER)",
      ],
      [
        "Tecnología",
        "C++17, ESP-IDF 5.5.5, LVGL, ESP32-S3",
      ],
      [
        "Pruebas",
        "93081 comprobaciones en 18 programas de host y 6 de Python (`ctest`)",
      ],
      [
        "Placa",
        "Waveshare ESP32-S3-Touch-LCD-7C-BOX (800x480, GT911)",
      ],
      [
        "Funciona en",
        "Una Waveshare ESP32-S3-Touch-LCD-7C-BOX; pruebas de host en cualquier ordenador",
      ],
      [
        "En hardware real",
        "Ninguno todavía: el firmware compila (ESP-IDF 5.5.5, sin comprobar en CI) pero no ha corrido en la placa",
      ],
      [
        "Licencia",
        "GPL-3.0-or-later",
      ],
    ],
    "status": {
      "software": "El firmware se ha compilado una vez (ESP-IDF 5.5.5), pero la compilación no la comprueba la integración continua y nunca ha funcionado en una placa.",
      "tests": "Pasan 93.081 comprobaciones en 18 programas de host (`ctest`): los ajustes, lo que el panel sabe del servidor y cuándo está obsoleto, la alarma de coacción que nunca se muestra, el intercambio de voz, los pines, los textos de la pantalla en ocho idiomas y los glifos de sus fuentes.",
      "protocols": "El intercambio con el servidor y con el servicio de voz ARMOR-VOICE-AI se prueba contra simulaciones; es pulsar para hablar, sin palabra de activación.",
      "ui": "La página web se ha ejecutado contra una simulación en un navegador real; la pantalla, el táctil y el sonido están escritos a partir de los ejemplos de Waveshare y esperan su primer encendido.",
      "hardware": "El firmware no ha funcionado en la placa: nada ha funcionado todavía con equipos reales.",
      "security": "El código de configuración, el límite de accesos, el PIN Bluetooth, el manejo de la coacción y las actualizaciones firmadas están probados en el host; no ha habido una revisión independiente.",
      "updates": "Las comprobaciones de hash y de firma pasan en el host; una actualización por aire nunca se ha ejecutado en una placa.",
      "integration": "Los mensajes se validan contra los esquemas compartidos de ARMOR-COMMON; el enlace con el servidor y con el servicio de voz no se ha probado desde una placa.",
      "docs": "Ocho idiomas, la guía del firmware, las notas de cableado y el historial de cambios están al día.",
    },
    "docs": [
      "[Diseño](docs/DESIGN.md) y [hardware](docs/HARDWARE.md): lo que muestra la central y la placa",
      "[Voz](docs/VOICE.md) y [fuentes](docs/FONTS.md)",
      "[Firmware del nodo](docs/NODE_FIRMWARE.md) y [acciones de compilación](docs/FIRMWARE_BUILD_ACTIONS.md)",
      "[Pruebas de banco](docs/BENCH_TESTS.md), [código de puesta en marcha](docs/SETUP_CODE.md) y [alta por Bluetooth](docs/BLE_PROVISIONING.md)",
    ],
    "contributing_first": "Antes de un pull request ejecuta `ctest --test-dir build/host` and `python -I tools/armor_ci_validate.py`: debe pasar. Consulta [CONTRIBUTING.md](CONTRIBUTING.md) y el [código de conducta](CODE_OF_CONDUCT.md).",
    "languages_extra": "",
    "body": {
      "overview": r"""* **Cliente de ARMOR-SERVER, como la app de Android:** entra con un usuario que un administrador creó para él, pide `GET /api/v1/panel/summary` (unos cientos de bytes: el modo, los nodos conectados y las alarmas que necesitan a una persona) cada pocos segundos y, cuando la persona toca el botón y confirma, arma, desarma o reconoce. Si el servidor deja de responder, la pantalla avisa de que lo que muestra es antiguo y el botón se desactiva. Escucha el canal en directo del servidor (un WebSocket) para que un cambio se vea al instante, y pregunta como antes cuando el canal falta, calla o está desactivado.
* **La pantalla (800x480, LVGL):** el modo en el color de la peor alarma que nadie ha visto, un botón grande de armar/desarmar con pregunta previa, los nodos conectados, las alarmas (las no vistas primero), una noche que la atenúa, un reposo tras un tiempo sin toques, un aviso sonoro y que se despierte cuando llega una alarma nueva, y ocho idiomas con acentos, japonés y chino dibujados con fuentes generadas justo para los caracteres usados.
* **Un nodo como los demás:** el mismo almacén de ajustes, Wi-Fi, página web en ocho idiomas, configuración por Bluetooth desde el móvil, actualización de firmware con vuelta atrás y HTTPS que ARMOR-NODE-RADAR, ARMOR-NODE-SOLAR y ARMOR-NODE-ELECTRICAL (comparten `ARMOR-COMMON/firmware_base`), más páginas para el servidor, la pantalla, el sonido y la voz; avisa a Studio de que existe por MQTT para que lo liste con su página.
* **El asistente de voz, pulsar para hablar:** un toque abre el micrófono, el audio va solo al servicio de voz cuya dirección está en los ajustes (apagado por defecto), la respuesta se muestra y se dice; el orden de los pasos, los límites de tiempo y lo que hace un toque son una máquina de estados probada, y el panel no ejecuta ninguna orden por sí mismo ([el contrato](docs/VOICE.md)). La grabación va como bytes en una petición binaria y la respuesta hablada vuelve como bytes; a un servidor que no la acepta se le envía la petición antigua.
* **La placa:** Waveshare ESP32-S3-Touch-LCD-7C-BOX (32 MB de flash, 16 MB de PSRAM, pantalla RGB de 7 pulgadas con tacto GT911, cuatro micrófonos, un altavoz); los pines vienen de los ejemplos de Waveshare y una prueba demuestra que dos funciones no comparten un GPIO ([la placa](docs/HARDWARE.md)).
* **Actualizaciones por aire firmadas:** el nodo solo instala desde GitHub una imagen cuyo SHA-256 coincide y que lleva una firma Ed25519 válida del responsable (la clave pública está en el firmware, la privada nunca sale del responsable); un archivo subido a mano por un administrador en el panel se sigue aceptando. Las páginas y mensajes del panel están en ocho idiomas.
* **Emparejamiento Bluetooth con PIN:** el PIN de seis cifras se deriva del código de configuración, se imprime en la consola USB y se muestra a un administrador en el panel; el móvil tiene que escribirlo antes de poder cambiar los ajustes del nodo.
* **Todavía no:** una primera compilación y encendido del firmware, una palabra de activación, el servicio de voz en la Jetson y una vista de las cámaras en la pantalla.
* **Solo la casa puede usar el panel:** el panel responde por defecto a la red privada (o a las redes que su dueño indique, como una VPN), rechaza una lista que dejaría fuera a quien la guarda, cuenta las contraseñas erróneas por persona y por dirección, y funciona detrás del proxy del servidor para llegar a él desde fuera de casa sin publicar el nodo.
* **Dice qué pasa:** la pantalla conoce el texto, en ocho idiomas, de cada código de alarma que levanta el servidor (red, solar, eléctrica, zonas de alarma...), y avisa al servidor de que es un panel de pared, así que se lista como tal y no cuenta como radar.
* **Enlace cifrado opcional con el broker (TLS):** desactivado por defecto, así que el nodo habla MQTT sin cifrar como antes. Un interruptor y una caja para el certificado de la autoridad propia de la instalación (PEM, 2 KB como máximo) en la página Broker hacen que se conecte con `mqtts://`, confíe solo en esa autoridad y compruebe que el certificado del broker se hizo para la dirección a la que llegó; lo que no sea un único certificado PEM se rechaza. Cubierto con pruebas en el ordenador; el handshake aún no se ha ejecutado en una placa.
* **Informe de salud:** cada minuto más o menos el nodo publica cuánto lleva encendido y por qué se reinició la última vez, su memoria libre, su enlace y su señal Wi-Fi, cuántas veces se conectó al broker y el último error que anotó (`armor/health/<nodo>`, el contrato `node_health` de ARMOR-COMMON). El código que lo construye lo comparten todos los nodos y está probado en un ordenador; no se ha ejecutado en una placa.
* **Control desde el servidor:** Studio puede reiniciar el nodo limpiamente, pausarlo hasta una hora (se reanuda solo), poner su trabajo en espera (sin fin, se conserva al reiniciar, el nodo sigue conectado y respondiendo), hacer que se muestre, pedirle una instantánea de diagnóstico y marcarlo en mantenimiento (`armor/control/<nodo>/...`, el contrato `node_control` de ARMOR-COMMON). Cada orden son dos pasos con un token de un solo uso que pertenece a esa operación, solo el servidor puede escribirlas en el broker, y no existe restablecimiento de fábrica, borrado ni sueño profundo. Mientras el panel está en pausa o en espera la pantalla muestra una pantalla propia que lo dice y no atiende toques; cuando se le pide que se identifique, parpadea una barra arriba (nunca un sonido). El código es compartido por todos los nodos y se prueba en un ordenador; no ha funcionado en una placa.
* **Diagnóstico sin cable:** tras un arranque que no fue limpio (un cuelgue, un watchdog, una caída de la alimentación, una reserva de memoria fallida) el informe de salud dice el motivo durante diez minutos; un fallo deja su volcado de núcleo (core dump) para verlo, descargarlo o borrarlo desde el panel; los ajustes guardados se copian antes de cada instalación de firmware y se recuperan si una actualización los daña; y un administrador puede pedir al nodo, a través del servidor, un paquete de diagnóstico o su registro con un token de un solo uso.
* **Una sirena que se repite y suena por orden:** todo sonido pasa por una cola con prioridades (sirena, alarma, voz, confirmación, aviso); la sirena se repite mientras haya alarmas críticas sin reconocer (`audio.siren_repeat_s` 30, `audio.siren_max_repeats` 10) y las alarmas mantienen un volumen mínimo (`audio.critical_min_volume` 40); la voz cede ante una alarma.
* **Un reloj con batería:** el chip PCF85063A de la placa da la hora al arrancar cuando el nodo aún no tiene hora real y el chip es de fiar, y se corrige cada vez que se sincroniza o se pone la hora (`time.rtc_enabled`, activado por defecto).
* **El estado de una orden, en la pantalla:** el pie dice que la orden se está enviando mientras va de camino y que se confirmó durante unos segundos cuando se cumplió; un rechazo conserva ahí su motivo, como antes.
* **Sellado opcional de los secretos guardados:** desactivado por defecto (`security.seal_secrets`, o `nodes.nvs_encryption` del servidor). Activado, las contraseñas, tokens, claves, PIN y hashes de contraseña que guarda el nodo quedan sellados con ChaCha20-Poly1305 y todo lo demás sigue legible; activarlo o desactivarlo los reescribe sin perder nada, aunque el nodo se pare a medias. No se quema ningún eFuse ni se cifra la flash: la clave está en una partición del mismo chip, así que **no** protege frente a quien tenga la placa, y un nodo instalado antes de esa partición conserva sus secretos como estaban hasta que se grabe con la nueva tabla de particiones.""",
      "role": r"""ARMOR-NODE-HMI es el panel de pared: un cliente de [ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER), como la app Android, con una pantalla de 7 pulgadas, micrófono y altavoz. Muestra el modo, los nodos en línea y las alarmas que necesitan a una persona, arma y desarma (con el PIN) y reconoce alarmas. Es donde vivirá el asistente de voz ([ARMOR-VOICE-AI](https://github.com/JuanenRac/ARMOR-VOICE-AI)) cuando exista su servicio de voz y, como todo nodo, se configura y actualiza desde [ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO).

| Nombre | Cómo | Para qué |
|---|---|---|
| ARMOR-SERVER | HTTPS `GET /api/v1/panel/summary`, WebSocket `/api/v1/panel/events` | El resumen de la casa (modos, alarmas, nodos, energía) y sus cambios; el servidor decide qué hace una orden |
| ARMOR-VOICE-AI | a través del servidor | El audio de un turno va al servicio de voz; la respuesta se muestra y se dice |
| ARMOR-STUDIO | menú Panel táctil | Muestra la salud del panel y abre su panel web |
| ARMOR-COMMON | base de firmware | El firmware común (panel, accesos, actualización firmada, puesta en marcha por Bluetooth) se copia de él |""",
      "architecture": r"""<p align="center">
  <img src="images/architecture.svg" alt="Arquitectura de ARMOR-NODE-HMI: quién lo llama, qué contiene y de qué depende" width="100%">
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
| La alarma de coacción mostrada en pantalla | Nunca se muestra (una prueba de host lo comprueba); y lo que la central sabe del servidor se marca como caducado cuando es viejo |
| Un servidor que no es el servidor | El certificado del servidor está fijado (`server_pin`), para las peticiones y para el WebSocket del canal vivo; la central entra con su propio usuario, creado por un administrador, con el rol `panel` (no puede usar Studio) |
| Desarmar sin PIN | Armar y desarmar preguntan antes y piden el PIN en pantalla (`pin_entry`); el servidor lo vuelve a comprobar |
| Audio de voz a un lugar inesperado | Apagada por defecto (`voice.enabled` falso); el audio va solo al servicio cuya dirección está en los ajustes (la dirección se valida y cambiar de host borra el token); la central no ejecuta ninguna orden por sí sola y no hay palabra de activación: es pulsar para hablar |
| Una sirena que nadie oye | Una sola cola de prioridad (sirena, alarma, voz, confirmación, aviso); la sirena se repite mientras haya alarmas críticas sin reconocer (`audio.siren_repeat_s` 30, de 10 a 600, 0 = sin repeticiones; `audio.siren_max_repeats` 10) y el volumen crítico nunca baja de `audio.critical_min_volume` (40 %) |

El firmware se compiló una vez y nunca ha corrido en una placa: la pantalla, el táctil, el sonido y el enlace con el servidor están escritos a partir de los ejemplos de Waveshare, a la espera del primer encendido. Lee [SECURITY.md](SECURITY.md) para informar de una vulnerabilidad.""",
      "interfaces": r"""| Parte | Qué define |
|---|---|
| ARMOR-SERVER | `GET /api/v1/panel/summary` cada `server.poll_s` (3 s, de 1 a 60) solo mientras el canal vivo está caído, y el WebSocket `/api/v1/panel/events` mientras `server.live_events` sea verdadero (por defecto): el resumen llega cuando cambian el modo, las alarmas, los nodos o la energía; el usuario propio de la central tiene el rol `panel` |
| Voz | El audio de un turno va a ARMOR-VOICE-AI a través del servidor (`/api/v1/voice/turn`, con cuerpo multipart opcional); `core/voice_session.hpp` es la máquina de estados (orden de los pasos, límites de tiempo, qué hace un toque); mira [docs/VOICE.md](docs/VOICE.md) |
| Hardware | Waveshare ESP32-S3-Touch-LCD-7C-BOX: pantalla RGB de 7 pulgadas 800x480, táctil GT911, cuatro micrófonos, un altavoz, RTC PCF85063A (`time.rtc_enabled`, verdadero por defecto), 32 MB de flash y 16 MB de PSRAM; una prueba demuestra que ninguna función comparte un GPIO |""",
      "configuration": r"""| Variable | Por defecto | Qué define |
|---|---|---|
| `server.poll_s`, `server.live_events` | 3 (1-60), true | El periodo de sondeo del resumen y el canal vivo por WebSocket |
| `display.sleep_s` | 300 (0-3600) | Segundos hasta que la pantalla duerme (0 = nunca); el brillo y el brillo nocturno también son ajustes |
| `audio.critical_min_volume`, `audio.siren_repeat_s`, `audio.siren_max_repeats` | 40 (0-100), 30, 10 | El volumen mínimo de un sonido crítico, el periodo de repetición de la sirena (0 o de 10 a 600 s) y sus repeticiones máximas |
| `audio.tone_by_source` | según la gravedad | El sonido de cada origen de alarma (dispositivo, solar, eléctrico, red, central, otro): el que dice su gravedad, como aviso, como alarma, como sirena o sin sonido; un sonido elegido suena aunque la gravedad esté por debajo del mínimo |
| `voice.enabled`, `voice.url`, `voice.token` | false, "", - | El servicio de voz: apagado por defecto; la dirección tiene como máximo 160 caracteres y se valida (`required` o `invalid` si no); el token se borra al cambiar de host |
| `CONFIG_ARMOR_NODE_ID`, `_SETUP_CODE`, `_FLEET_SECRET`, `_MQTT_*`, `_HEARTBEAT_S`, `_BLE_SETUP_MINUTES`, `_BOOT_FACTORY_RESET` | - | Los ajustes que comparten todos los nodos: el nombre (vacío da `armor-` y los últimos bytes de la MAC), el código de puesta en marcha (vacío: aleatorio), el secreto de flota (16+ caracteres, nunca en el repositorio), los primeros ajustes del broker, el latido (de 2 a 300 s), los minutos de puesta en marcha por Bluetooth (de 1 a 120) y el reinicio con BOOT (8 s en los primeros 30 s) |""",
      "quickstart": r"""**Requisitos:** un compilador C++17 para las pruebas de host; el contenedor ESP-IDF 5.5.5 para compilar la imagen; una Waveshare ESP32-S3-Touch-LCD-7C-BOX.

```bash
cmake -S tests -B build/host && cmake --build build/host && ctest --test-dir build/host   # host tests, -Werror
node tools/panel_mock.mjs --user admin:adminpass123   # the panel of the node without a board
tools/build_node.sh                                   # the image in the ESP-IDF container
```

See the [firmware guide](docs/NODE_FIRMWARE.md) and the [Bluetooth channel](docs/BLE_PROVISIONING.md).

Mira el [diseño](docs/DESIGN.md), la [placa](docs/HARDWARE.md), el [asistente de voz](docs/VOICE.md), la [guía del firmware](docs/NODE_FIRMWARE.md) y las [fuentes](docs/FONTS.md).

Para compilar el firmware a mano en GitHub Actions, mira [compilar en GitHub Actions](docs/FIRMWARE_BUILD_ACTIONS.md).""",
      "testing": r"""```bash
cmake -S tests -B build/host && cmake --build build/host && ctest --test-dir build/host
python -I tools/armor_ci_validate.py
```

18 programas de prueba de host y 6 comprobaciones en Python se ejecutan con `ctest`; 93081 comprobaciones contadas por los programas de host, compilados con `-Werror`.

Comprobaciones Python: los textos del panel en ocho idiomas, las tareas, las rutas de guardado, la sesión Bluetooth bajo su bloqueo y las rutas que llama el panel (y, en algunos nodos, los códigos HTTP o los glifos de las fuentes)

Las pruebas de host necesitan cualquier compilador C++17 (Linux, WSL, MSYS2); el panel web también se ejercita en un navegador real contra un nodo de pruebas (`tools/panel_mock.mjs`, `tools/panel_browser_test.mjs`).

`check_font_glyphs.py` comprueba que las fuentes tienen todos los glifos de los ocho idiomas (98 filas); `test_clock` solo imprime `ok`.""",
      "build": "`tools/build_node.sh` compila la imagen en el contenedor ESP-IDF 5.5.5 y la versión lleva la imagen, su SHA-256 y su firma Ed25519, una por placa; la imagen se graba por USB-C la primera vez y después se actualiza desde el panel.",
      "troubleshooting": r"""| Ves | Porque | Haz |
|---|---|---|
| Perdiste la contraseña o el nodo ya no se une a la red | Un nodo con puesta en marcha y sin dirección tras 90 s abre su propio Wi-Fi `ARMOR-SETUP-xxxxxx` (abre `http://192.168.4.1/`) | Para empezar de cero mantén BOOT 8 segundos en los primeros 30 segundos tras encender (borra ajustes y usuarios), o usa *Restablecer de fábrica* en el panel |
| Se rechaza una actualización desde GitHub | La versión no trae suma de comprobación ni firma, no coinciden (`e_no_checksum`, `e_no_signature`, `e_checksum_mismatch`, `e_bad_signature`), no trae imagen para esta placa (`e_no_asset_for_board`) o es de otro proyecto (`e_wrong_firmware`) | El nodo no cambió; reintenta o deja que un administrador suba el fichero a mano |
| La voz no arranca | `voice.enabled` está apagado, o `voice.url` es `required` o `invalid` | Enciéndelo en el panel y da una dirección válida; cambiar de host borra el token |
| El pie dice enviando, luego confirmada o el motivo | Una orden va en camino, se confirmó unos segundos, o se rechazó y conserva su motivo | Lee el motivo; decide el servidor, no el panel |""",
      "structure": r"""<p align="center">
  <img src="images/repository-structure.svg" alt="Estructura del repositorio de ARMOR-NODE-HMI" width="100%">
</p>

<details>
<summary>Versión en texto del árbol</summary>

```text
ARMOR-NODE-HMI/
├── main/                                el firmware: un componente de ESP-IDF
├── core/                                la lógica sin ESP-IDF, probada en un ordenador
├── panel/                               el panel web embebido en el firmware
├── tests/                               pruebas de host y comprobaciones Python
├── docs/                                9 guías: diseño, voz, fuentes, hardware
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
├── sdkconfig.board.lcd7box              los ajustes de una placa
├── secrets/                             ejemplo del fichero del nodo (los reales no se versionan)
├── dependencies.lock                    las versiones fijadas de los componentes de ESP-IDF
├── build-test.sh build-test.bat         ejecutar las pruebas con el flujo compartido
└── .gitattributes .gitignore            ajustes de Git
```

</details>""",
      "roadmap": r"""**Límites conocidos hoy**

* El firmware se ha compilado una vez (ESP-IDF 5.5.5), pero la compilación no la comprueba la integración continua y nunca ha funcionado en una placa.
* El intercambio con el servidor y con el servicio de voz ARMOR-VOICE-AI se prueba contra simulaciones; es pulsar para hablar, sin palabra de activación.
* La página web se ha ejecutado contra una simulación en un navegador real; la pantalla, el táctil y el sonido están escritos a partir de los ejemplos de Waveshare y esperan su primer encendido.
* El firmware no ha funcionado en la placa: nada ha funcionado todavía con equipos reales.
* El código de configuración, el límite de accesos, el PIN Bluetooth, el manejo de la coacción y las actualizaciones firmadas están probados en el host; no ha habido una revisión independiente.
* Las comprobaciones de hash y de firma pasan en el host; una actualización por aire nunca se ha ejecutado en una placa.
* Los mensajes se validan contra los esquemas compartidos de ARMOR-COMMON; el enlace con el servidor y con el servicio de voz no se ha probado desde una placa.

**Lo siguiente**

* Hacer la primera compilación completa y el primer encendido en la placa, y después el servicio de voz en la Jetson, una palabra de activación y la vista de cámaras en la pantalla.""",
    },
  },
  "de": {
    "tagline": "Das Touch-Panel des Hauses: ein 7-Zoll-Bildschirm an der Wand, der den Systemzustand zeigt, es scharf und unscharf schaltet und Alarme quittiert, mit Mikrofon und Lautsprecher für den kommenden Sprachassistenten (ein Knoten der Familie auf dem ESP32-S3-Touch-LCD-7C-BOX mit eigener Webseite für die Einstellungen)",
    "honest": "Was nicht von der Platine abhängt, ist real und auf einem Computer getestet (die Einstellungen, was das Panel vom Server weiß und wann das veraltet ist, der Zwangsalarm, der nie angezeigt wird, das Sprachgespräch und die lange Antwort des Sprachdienstes, die Pins der Platine, die Texte des Bildschirms in acht Sprachen und die Glyphen seiner Schriften, die Release- und Signaturprüfungen: 30,783 Prüfungen in 18 Testprogrammen), ebenso die Webseite (gegen einen Ersatz in einem echten Browser ausgeführt). **Die Firmware wurde einmal gebaut (ESP-IDF 5.5.5, von der kontinuierlichen Integration nicht geprüft) und lief nie auf einer Platine:** Bildschirm, Touch, Ton und die Verbindung zum Server sind nach Waveshares Beispielen für diese Platinenfamilie geschrieben und brauchen ihr erstes Einschalten. Der Sprachdienst (ARMOR-VOICE-AI) beantwortet die Anfragen dieses Panels; es gibt kein Aktivierungswort: Man tippt zum Sprechen.",
    "glance": [
      [
        "Rolle",
        "Wand-Touchpanel für ARMOR-SERVER (Familie: Clients, übergeordnet: ARMOR-SERVER)",
      ],
      [
        "Technik",
        "C++17, ESP-IDF 5.5.5, LVGL, ESP32-S3",
      ],
      [
        "Tests",
        "93081 Prüfungen in 18 Host-Programmen und 6 Python-Prüfungen (`ctest`)",
      ],
      [
        "Platine",
        "Waveshare ESP32-S3-Touch-LCD-7C-BOX (800x480, GT911)",
      ],
      [
        "Läuft auf",
        "Ein Waveshare ESP32-S3-Touch-LCD-7C-BOX; Host-Tests auf jedem Computer",
      ],
      [
        "Auf echter Hardware",
        "Noch keiner: die Firmware baut (ESP-IDF 5.5.5, von der CI nicht geprüft), lief aber nicht auf der Platine",
      ],
      [
        "Lizenz",
        "GPL-3.0-or-later",
      ],
    ],
    "status": {
      "software": "Die Firmware wurde einmal gebaut (ESP-IDF 5.5.5), der Build wird aber nicht von der kontinuierlichen Integration geprüft, und sie lief nie auf einer Platine.",
      "tests": "93.081 Prüfungen in 18 Host-Programmen bestehen (`ctest`): die Einstellungen, was das Panel vom Server weiß und wann das veraltet ist, der nie angezeigte Zwangsalarm, der Sprachaustausch, die Pins, die Texte des Bildschirms in acht Sprachen und die Glyphen seiner Schriften.",
      "protocols": "Der Austausch mit dem Server und mit dem Sprachdienst ARMOR-VOICE-AI ist gegen Nachbildungen getestet; es ist Push-to-Talk, ohne Weckwort.",
      "ui": "Die Webseite lief gegen eine Nachbildung in einem echten Browser; Bildschirm, Touch und Ton sind nach den Beispielen von Waveshare geschrieben und warten auf das erste Einschalten.",
      "hardware": "Die Firmware lief nicht auf der Platine: Bisher lief nichts auf echten Geräten.",
      "security": "Der Einrichtungscode, die Anmeldebegrenzung, die Bluetooth-PIN, der Umgang mit Zwang und die signierten Aktualisierungen sind auf dem Host getestet; es gab keine unabhängige Prüfung.",
      "updates": "Die Hash- und Signaturprüfungen bestehen auf dem Host; eine Aktualisierung über die Luft wurde nie auf einer Platine ausgeführt.",
      "integration": "Die Nachrichten werden gegen die gemeinsamen Schemas von ARMOR-COMMON geprüft; die Verbindung zum Server und zum Sprachdienst wurde nicht von einer Platine aus erprobt.",
      "docs": "Acht Sprachen, die Firmware-Anleitung, die Verdrahtungshinweise und das Änderungsprotokoll sind aktuell.",
    },
    "docs": [
      "[Entwurf](docs/DESIGN.md) und [Hardware](docs/HARDWARE.md): was das Panel zeigt und die Platine",
      "[Sprache](docs/VOICE.md) und [Schriften](docs/FONTS.md)",
      "[Knoten-Firmware](docs/NODE_FIRMWARE.md) und [Build-Aktionen](docs/FIRMWARE_BUILD_ACTIONS.md)",
      "[Prüfstandtests](docs/BENCH_TESTS.md), [Einrichtungscode](docs/SETUP_CODE.md) und [Bluetooth-Einrichtung](docs/BLE_PROVISIONING.md)",
    ],
    "contributing_first": "Führe vor einem Pull Request `ctest --test-dir build/host` and `python -I tools/armor_ci_validate.py` aus: Es muss bestehen. Siehe [CONTRIBUTING.md](CONTRIBUTING.md) und den [Verhaltenskodex](CODE_OF_CONDUCT.md).",
    "languages_extra": "",
    "body": {
      "overview": r"""* **Ein Client von ARMOR-SERVER wie die Android-App:** Es meldet sich mit einem Benutzer an, den ein Administrator dafür angelegt hat, fragt alle paar Sekunden `GET /api/v1/panel/summary` ab (wenige hundert Byte: Modus, Knoten online und die Alarme, die einen Menschen brauchen) und schaltet scharf, unscharf oder quittiert, wenn die Person die Taste berührt und bestätigt. Antwortet der Server nicht mehr, sagt der Bildschirm, dass das Gezeigte alt ist, und die Taste ist gesperrt. Er hört den Live-Kanal des Servers ab (ein WebSocket), damit eine Änderung sofort erscheint, und fragt wie bisher, wenn der Kanal fehlt, schweigt oder abgeschaltet ist.
* **Der Bildschirm (800x480, LVGL):** der Modus in der Farbe des schlimmsten ungesehenen Alarms, eine große Scharf/Unscharf-Taste mit vorheriger Rückfrage, die Knoten online, die Alarme (die ungesehenen zuerst), eine Nacht, die ihn dimmt, Ruhezustand nach einer Zeit ohne Berührung, ein Ton und Aufwecken bei neuem Alarm sowie acht Sprachen mit Akzenten, Japanisch und Chinesisch mit genau für die verwendeten Zeichen erzeugten Schriften.
* **Ein Knoten wie die anderen:** derselbe Einstellungsspeicher, WLAN, Webseite in acht Sprachen, Bluetooth-Einrichtung vom Handy, Firmware-Update mit Rückfall und HTTPS wie ARMOR-NODE-RADAR, ARMOR-NODE-SOLAR und ARMOR-NODE-ELECTRICAL (sie teilen `ARMOR-COMMON/firmware_base`), dazu Seiten für Server, Bildschirm, Ton und Sprache; es meldet sich per MQTT bei Studio an, damit Studio es mit seiner Seite auflistet.
* **Der Sprachassistent, Push-to-talk:** Eine Berührung öffnet das Mikrofon, das Audio geht nur an den Sprachdienst, dessen Adresse in den Einstellungen steht (standardmäßig aus), die Antwort wird angezeigt und gesprochen; Reihenfolge der Schritte, Zeitlimits und die Wirkung einer Berührung sind ein getesteter Zustandsautomat, und das Panel führt keinen Befehl von selbst aus ([der Vertrag](docs/VOICE.md)). Die Aufnahme geht als Rohbytes in einer Binäranfrage hinaus und die gesprochene Antwort kommt als Bytes zurück; einem Server, der das nicht annimmt, wird die ältere Anfrage geschickt.
* **Das Board:** Waveshare ESP32-S3-Touch-LCD-7C-BOX (32 MB Flash, 16 MB PSRAM, 7-Zoll-RGB-Bildschirm mit GT911-Touch, vier Mikrofone, ein Lautsprecher); die Pins stammen aus Waveshares Beispielen, und ein Test beweist, dass keine zwei Funktionen einen GPIO teilen ([das Board](docs/HARDWARE.md)).
* **Signierte Over-the-Air-Updates:** der Knoten installiert von GitHub nur ein Abbild, dessen SHA-256 stimmt und das eine gültige Ed25519-Signatur des Betreuers trägt (der öffentliche Schlüssel steckt in der Firmware, der private verlässt den Betreuer nie); eine von einem Administrator im Panel von Hand hochgeladene Datei wird weiterhin akzeptiert. Seiten und Meldungen des Panels sind in acht Sprachen.
* **Bluetooth-Kopplung mit PIN:** die sechsstellige PIN wird aus dem Einrichtungscode abgeleitet, auf der USB-Konsole ausgegeben und einem Administrator im Panel angezeigt; das Telefon muss sie eingeben, bevor es die Einstellungen des Knotens schreiben darf.
* **Noch nicht:** eine erste Kompilierung und ein erster Start der Firmware, ein Aktivierungswort, der Sprachdienst auf dem Jetson und eine Kameraansicht auf dem Bildschirm.
* **Nur das Haus darf das Panel nutzen:** Das Panel antwortet standardmäßig dem privaten Netz (oder den Netzen, die der Besitzer nennt, etwa einem VPN), lehnt eine Liste ab, die den Speichernden aussperren würde, zählt falsche Passwörter je Person und je Adresse und funktioniert hinter dem Proxy des Servers, sodass man es von außerhalb des Hauses erreicht, ohne den Knoten zu veröffentlichen.
* **Es sagt, was passiert:** der Bildschirm kennt den Text jedes Alarmcodes des Servers (Netzwerk, Solar, Elektrik, Alarmzonen...) in acht Sprachen und meldet dem Server, dass er ein Wandpanel ist; so wird er als solches gelistet und zählt nicht als Radar.
* **Optionale verschlüsselte Verbindung zum Broker (TLS):** standardmäßig aus, der Knoten spricht also wie bisher unverschlüsseltes MQTT. Ein Schalter und ein Feld für das Zertifikat der eigenen Zertifizierungsstelle der Anlage (PEM, höchstens 2 KB) auf der Broker-Seite sorgen dafür, dass er sich mit `mqtts://` verbindet, nur dieser Stelle vertraut und prüft, ob das Zertifikat des Brokers für die erreichte Adresse ausgestellt wurde; alles, was nicht genau ein PEM-Zertifikat ist, wird abgelehnt. Durch Host-Tests abgedeckt; der Handshake wurde auf einer Platine noch nicht ausgeführt.
* **Zustandsbericht:** etwa einmal pro Minute veröffentlicht der Knoten, wie lange er läuft und warum er zuletzt neu gestartet ist, seinen freien Speicher, seine Verbindung und sein WLAN-Signal, wie oft er sich mit dem Broker verbunden hat und den letzten protokollierten Fehler (`armor/health/<Knoten>`, der Vertrag `node_health` von ARMOR-COMMON). Der Code, der ihn erzeugt, wird von allen Knoten geteilt und auf einem Computer getestet; auf einer Platine ist er noch nicht gelaufen.
* **Steuerung vom Server aus:** Studio kann den Knoten sauber neu starten, bis zu einer Stunde pausieren (er läuft von selbst weiter), seine Arbeit in den Standby setzen (ohne Ende, über Neustarts hinweg gespeichert, der Knoten bleibt verbunden und antwortet weiter), ihn sich zeigen lassen, einen Diagnose-Schnappschuss anfordern und ihn als in Wartung markieren (`armor/control/<Knoten>/...`, der Vertrag `node_control` von ARMOR-COMMON). Jeder Befehl besteht aus zwei Schritten mit einem Einmal-Token, das zu dieser Operation gehört; nur der Server darf sie am Broker schreiben, und es gibt kein Zurücksetzen auf Werkseinstellungen, kein Löschen und keinen Tiefschlaf. Solange das Panel pausiert oder im Standby ist, zeigt der Bildschirm eine eigene Anzeige, die das sagt, und nimmt keine Berührung an; bei der Aufforderung, sich zu melden, blinkt oben ein Balken (nie ein Ton). Der Code wird von allen Knoten geteilt und auf einem Rechner getestet; auf einer Platine ist er noch nicht gelaufen.
* **Diagnose ohne Kabel:** Nach einem unsauberen Start (Absturz, Watchdog, Spannungseinbruch, fehlgeschlagene Speicherreservierung) nennt der Gesundheitsbericht zehn Minuten lang den Grund; ein Absturz hinterlässt sein Core-Dump, das man im Panel ansehen, herunterladen oder löschen kann; die gespeicherten Einstellungen werden vor jeder Firmware-Installation kopiert und wiederhergestellt, falls ein Update sie beschädigt; und ein Administrator kann den Knoten über den Server mit einem Einmal-Token nach einem Diagnosepaket oder seinem Protokoll fragen.
* **Eine Sirene, die sich wiederholt, und Töne in Reihenfolge:** Jeder Ton läuft durch eine Prioritätswarteschlange (Sirene, Alarm, Stimme, Bestätigung, Hinweis); die Sirene wiederholt sich, solange es unquittierte kritische Alarme gibt (`audio.siren_repeat_s` 30, `audio.siren_max_repeats` 10), und Alarme behalten eine Mindestlautstärke (`audio.critical_min_volume` 40); die Stimme weicht einem Alarm.
* **Eine batteriegepufferte Uhr:** Der Chip PCF85063A der Platine liefert beim Start die Uhrzeit, wenn der Knoten noch keine echte Zeit hat und der Chip vertrauenswürdig ist, und wird bei jeder Synchronisierung oder Zeiteinstellung korrigiert (`time.rtc_enabled`, standardmäßig an).
* **Der Zustand eines Befehls auf dem Bildschirm:** Die Fußzeile zeigt, dass der Befehl gesendet wird, solange er unterwegs ist, und einige Sekunden lang, dass er bestätigt wurde; eine Ablehnung behält dort wie bisher ihren Grund.
* **Optionales Versiegeln gespeicherter Geheimnisse:** standardmäßig aus (`security.seal_secrets` oder `nodes.nvs_encryption` des Servers). Eingeschaltet werden die Passwörter, Token, Schlüssel, PINs und Passwort-Hashes, die der Knoten speichert, mit ChaCha20-Poly1305 versiegelt, alles andere bleibt lesbar; Ein- und Ausschalten schreibt sie ohne Verlust um, auch wenn der Knoten mittendrin stehen bleibt. Es wird kein eFuse gebrannt und der Flash nicht verschlüsselt: Der Schlüssel liegt in einer Partition desselben Chips und schützt daher **nicht** vor jemandem, der die Platine hat; ein Knoten, der vor dieser Partition installiert wurde, behält seine Geheimnisse unverändert, bis er mit der neuen Partitionstabelle geflasht wird.""",
      "role": r"""ARMOR-NODE-HMI ist das Wandpanel: ein Client von [ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER), wie die Android-App, mit einem 7-Zoll-Bildschirm, Mikrofon und Lautsprecher. Es zeigt den Modus, die Knoten online und die Alarme, die eine Person brauchen, schaltet scharf und unscharf (mit der PIN) und quittiert Alarme. Hier wird der Sprachassistent ([ARMOR-VOICE-AI](https://github.com/JuanenRac/ARMOR-VOICE-AI)) wohnen, sobald sein Sprachdienst existiert, und wie jeder Knoten wird es von [ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) aus eingerichtet und aktualisiert.

| Name | Wie | Wozu |
|---|---|---|
| ARMOR-SERVER | HTTPS `GET /api/v1/panel/summary`, WebSocket `/api/v1/panel/events` | Die Zusammenfassung des Hauses (Modi, Alarme, Knoten, Energie) und ihre Änderungen; der Server entscheidet, was ein Befehl bewirkt |
| ARMOR-VOICE-AI | über den Server | Das Audio eines Turns geht an den Sprachdienst; die Antwort wird angezeigt und gesprochen |
| ARMOR-STUDIO | Menü Touchpanel | Zeigt die Gesundheit des Panels und öffnet sein Web-Panel |
| ARMOR-COMMON | Firmware-Basis | Die gemeinsame Firmware (Panel, Anmeldungen, signiertes Update, Bluetooth-Einrichtung) stammt daraus |""",
      "architecture": r"""<p align="center">
  <img src="images/architecture.svg" alt="Architektur von ARMOR-NODE-HMI: wer es aufruft, was es enthält und wovon es abhängt" width="100%">
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
| Der Zwangsalarm auf dem Bildschirm | Er wird nie angezeigt (ein Host-Test prüft es); und was das Panel vom Server weiß, wird als veraltet markiert, wenn es alt ist |
| Ein Server, der nicht der Server ist | Das Zertifikat des Servers ist festgelegt (`server_pin`), für die Anfragen und für den WebSocket des Live-Kanals; das Panel meldet sich mit einem eigenen, von einem Administrator angelegten Benutzer mit der Rolle `panel` an (es kann Studio nicht benutzen) |
| Unscharfschalten ohne PIN | Scharf- und Unscharfschalten fragen zuerst und nehmen die PIN am Bildschirm entgegen (`pin_entry`); der Server prüft sie erneut |
| Sprachaudio an einen unerwarteten Ort | Standardmäßig aus (`voice.enabled` falsch); das Audio geht nur an den Dienst, dessen Adresse in den Einstellungen steht (die Adresse wird geprüft, und ein Hostwechsel löscht das Token); das Panel führt von sich aus keinen Befehl aus, und es gibt kein Aktivierungswort: Es ist Push-to-Talk |
| Eine Sirene, die niemand hört | Eine einzige Prioritätswarteschlange (Sirene, Alarm, Sprache, Bestätigung, Hinweis); die Sirene wiederholt sich, solange kritische Alarme unquittiert sind (`audio.siren_repeat_s` 30, 10 bis 600, 0 = keine Wiederholung; `audio.siren_max_repeats` 10), und die kritische Lautstärke sinkt nie unter `audio.critical_min_volume` (40 %) |

Die Firmware wurde einmal gebaut und lief nie auf einer Platine: Bildschirm, Touch, Ton und Serververbindung sind nach den Beispielen von Waveshare geschrieben und warten auf das erste Einschalten. Lies [SECURITY.md](SECURITY.md), um eine Schwachstelle zu melden.""",
      "interfaces": r"""| Teil | Was sie festlegt |
|---|---|
| ARMOR-SERVER | `GET /api/v1/panel/summary` alle `server.poll_s` (3 s, 1 bis 60) nur solange der Live-Kanal ausgefallen ist, und der WebSocket `/api/v1/panel/events`, solange `server.live_events` wahr ist (Standard): Die Zusammenfassung kommt, wenn sich Modus, Alarme, Knoten oder Energie ändern; der eigene Benutzer des Panels hat die Rolle `panel` |
| Sprache | Das Audio eines Turns geht über den Server an ARMOR-VOICE-AI (`/api/v1/voice/turn`, mit optionalem Multipart-Body); `core/voice_session.hpp` ist die Zustandsmaschine (Reihenfolge der Schritte, Zeitgrenzen, was eine Berührung bewirkt); siehe [docs/VOICE.md](docs/VOICE.md) |
| Hardware | Waveshare ESP32-S3-Touch-LCD-7C-BOX: 7-Zoll-RGB-Bildschirm 800x480, GT911-Touch, vier Mikrofone, ein Lautsprecher, RTC PCF85063A (`time.rtc_enabled`, standardmäßig wahr), 32 MB Flash und 16 MB PSRAM; ein Test belegt, dass keine Funktion ein GPIO teilt |""",
      "configuration": r"""| Variable | Standard | Was sie festlegt |
|---|---|---|
| `server.poll_s`, `server.live_events` | 3 (1-60), true | Die Abfrageperiode der Zusammenfassung und der Live-Kanal per WebSocket |
| `display.sleep_s` | 300 (0-3600) | Sekunden bis der Bildschirm schläft (0 = nie); Helligkeit und Nachthelligkeit sind ebenfalls Einstellungen |
| `audio.critical_min_volume`, `audio.siren_repeat_s`, `audio.siren_max_repeats` | 40 (0-100), 30, 10 | Die niedrigste Lautstärke eines kritischen Tons, die Wiederholperiode der Sirene (0 oder 10 bis 600 s) und ihre maximalen Wiederholungen |
| `audio.tone_by_source` | nach Schweregrad | Der Ton jeder Alarmquelle (Gerät, Solar, Elektrik, Netz, Zentrale, andere): wie es der Schweregrad vorgibt, als Hinweis, als Alarm, als Sirene oder ohne Ton; ein gewählter Ton erklingt auch unterhalb des Mindestschweregrads |
| `voice.enabled`, `voice.url`, `voice.token` | false, "", - | Der Sprachdienst: standardmäßig aus; die Adresse hat höchstens 160 Zeichen und wird geprüft (sonst `required` oder `invalid`); das Token wird beim Hostwechsel gelöscht |
| `CONFIG_ARMOR_NODE_ID`, `_SETUP_CODE`, `_FLEET_SECRET`, `_MQTT_*`, `_HEARTBEAT_S`, `_BLE_SETUP_MINUTES`, `_BOOT_FACTORY_RESET` | - | Die Einstellungen, die alle Knoten teilen: der Name (leer ergibt `armor-` und die letzten Bytes der MAC), der Einrichtungscode (leer: zufällig), das Flottengeheimnis (16+ Zeichen, nie im Repository), die ersten Broker-Einstellungen, der Herzschlag (2 bis 300 s), die Minuten der Bluetooth-Einrichtung (1 bis 120) und der Reset mit BOOT (8 s in den ersten 30 s) |""",
      "quickstart": r"""**Voraussetzungen:** ein C++17-Compiler für die Host-Tests; der ESP-IDF-5.5.5-Container zum Bauen des Images; ein Waveshare ESP32-S3-Touch-LCD-7C-BOX.

```bash
cmake -S tests -B build/host && cmake --build build/host && ctest --test-dir build/host   # host tests, -Werror
node tools/panel_mock.mjs --user admin:adminpass123   # the panel of the node without a board
tools/build_node.sh                                   # the image in the ESP-IDF container
```

See the [firmware guide](docs/NODE_FIRMWARE.md) and the [Bluetooth channel](docs/BLE_PROVISIONING.md).

Siehe den [Entwurf](docs/DESIGN.md), das [Board](docs/HARDWARE.md), den [Sprachassistenten](docs/VOICE.md), die [Firmware-Anleitung](docs/NODE_FIRMWARE.md) und die [Schriften](docs/FONTS.md).

Um die Firmware von Hand in GitHub Actions zu bauen, siehe [Bauen in GitHub Actions](docs/FIRMWARE_BUILD_ACTIONS.md).""",
      "testing": r"""```bash
cmake -S tests -B build/host && cmake --build build/host && ctest --test-dir build/host
python -I tools/armor_ci_validate.py
```

18 Host-Testprogramme und 6 Python-Prüfungen laufen unter `ctest`; 93081 Prüfungen, gezählt von den Host-Programmen, mit `-Werror` gebaut.

Python-Prüfungen: die Panel-Texte in acht Sprachen, die Tasks, die Speicherpfade, die Bluetooth-Sitzung unter ihrer Sperre und die vom Panel aufgerufenen Routen (und in manchen Knoten die HTTP-Codes oder die Glyphen der Schriften)

Die Host-Tests brauchen einen beliebigen C++17-Compiler (Linux, WSL, MSYS2); das Web-Panel wird außerdem in einem echten Browser gegen einen Ersatzknoten geprüft (`tools/panel_mock.mjs`, `tools/panel_browser_test.mjs`).

`check_font_glyphs.py` prüft, dass die Schriften alle Glyphen der acht Sprachen enthalten (98 Zeilen); `test_clock` gibt nur `ok` aus.""",
      "build": "`tools/build_node.sh` baut das Image im ESP-IDF-5.5.5-Container, und die Version trägt das Image, sein SHA-256 und seine Ed25519-Signatur, je eines pro Platine; das Image wird beim ersten Mal per USB-C geschrieben und danach vom Panel aktualisiert.",
      "troubleshooting": r"""| Sie sehen | Weil | Tun Sie |
|---|---|---|
| Du hast das Passwort verloren oder der Knoten tritt dem Netz nicht mehr bei | Ein Knoten in der Einrichtung ohne Adresse nach 90 s öffnet ein eigenes WLAN `ARMOR-SETUP-xxxxxx` (öffne `http://192.168.4.1/`) | Zum Neustart BOOT 8 Sekunden in den ersten 30 Sekunden nach dem Einschalten halten (löscht Einstellungen und Benutzer) oder im Panel *Werksreset* nutzen |
| Ein Update von GitHub wird abgelehnt | Die Version enthält keine Prüfsumme oder Signatur, sie passen nicht (`e_no_checksum`, `e_no_signature`, `e_checksum_mismatch`, `e_bad_signature`), hat kein Image für diese Platine (`e_no_asset_for_board`) oder gehört zu einem anderen Projekt (`e_wrong_firmware`) | Der Knoten blieb unverändert; erneut versuchen oder einen Administrator die Datei von Hand hochladen lassen |
| Die Sprache startet nicht | `voice.enabled` ist aus, oder `voice.url` ist `required` oder `invalid` | Schalte es im Panel ein und gib eine gültige Adresse an; ein Hostwechsel löscht das Token |
| Die Fußzeile sagt „sendet“, dann „bestätigt“ oder den Grund | Ein Befehl ist unterwegs, wurde einige Sekunden bestätigt oder abgelehnt und behält seinen Grund | Lies den Grund; der Server entscheidet, nicht das Panel |""",
      "structure": r"""<p align="center">
  <img src="images/repository-structure.svg" alt="Repository-Struktur von ARMOR-NODE-HMI" width="100%">
</p>

<details>
<summary>Textversion des Baums</summary>

```text
ARMOR-NODE-HMI/
├── main/                                die Firmware: eine ESP-IDF-Komponente
├── core/                                die Logik ohne ESP-IDF, am Rechner getestet
├── panel/                               das in die Firmware eingebettete Web-Panel
├── tests/                               Host-Tests und Python-Prüfungen
├── docs/                                9 Anleitungen: Entwurf, Sprache, Schriften, Hardware
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
├── sdkconfig.board.lcd7box              die Einstellungen einer Platine
├── secrets/                             Beispiel der Knotendatei (die echten sind nicht versioniert)
├── dependencies.lock                    die festgelegten Versionen der ESP-IDF-Komponenten
├── build-test.sh build-test.bat         Tests über den gemeinsamen Workflow ausführen
└── .gitattributes .gitignore            Git-Einstellungen
```

</details>""",
      "roadmap": r"""**Bekannte Grenzen heute**

* Die Firmware wurde einmal gebaut (ESP-IDF 5.5.5), der Build wird aber nicht von der kontinuierlichen Integration geprüft, und sie lief nie auf einer Platine.
* Der Austausch mit dem Server und mit dem Sprachdienst ARMOR-VOICE-AI ist gegen Nachbildungen getestet; es ist Push-to-Talk, ohne Weckwort.
* Die Webseite lief gegen eine Nachbildung in einem echten Browser; Bildschirm, Touch und Ton sind nach den Beispielen von Waveshare geschrieben und warten auf das erste Einschalten.
* Die Firmware lief nicht auf der Platine: Bisher lief nichts auf echten Geräten.
* Der Einrichtungscode, die Anmeldebegrenzung, die Bluetooth-PIN, der Umgang mit Zwang und die signierten Aktualisierungen sind auf dem Host getestet; es gab keine unabhängige Prüfung.
* Die Hash- und Signaturprüfungen bestehen auf dem Host; eine Aktualisierung über die Luft wurde nie auf einer Platine ausgeführt.
* Die Nachrichten werden gegen die gemeinsamen Schemas von ARMOR-COMMON geprüft; die Verbindung zum Server und zum Sprachdienst wurde nicht von einer Platine aus erprobt.

**Als Nächstes**

* Den ersten vollständigen Build und das erste Einschalten auf der Platine machen, danach den Sprachdienst auf dem Jetson, ein Aktivierungswort und die Kameraansicht auf dem Bildschirm.""",
    },
  },
  "fr": {
    "tagline": "Le panneau tactile de la maison : un écran de 7 pouces au mur qui montre l'état du système, l'arme et le désarme et acquitte les alarmes, avec un micro et un haut-parleur pour l'assistant vocal à venir (un nœud de la famille sur l'ESP32-S3-Touch-LCD-7C-BOX, avec sa propre page web de réglages)",
    "honest": "Ce qui ne dépend pas de la carte est réel et testé sur un ordinateur (les réglages, ce que le panneau sait du serveur et quand cela est périmé, l'alarme de contrainte qui n'est jamais affichée, la conversation vocale et la longue réponse du service vocal, les broches de la carte, les textes de l'écran en huit langues et les glyphes de ses polices, les contrôles de version et de signature : 30,783 vérifications en 18 programmes de test), de même que la page web (exécutée contre un substitut dans un vrai navigateur). **Le firmware a été compilé une fois (ESP-IDF 5.5.5, non vérifié par l'intégration continue) et n'a jamais tourné sur une carte :** l'écran, le tactile, le son et la liaison avec le serveur sont écrits d'après les exemples de Waveshare pour cette famille de cartes et attendent leur première mise sous tension. Le service vocal (ARMOR-VOICE-AI) répond aux requêtes de ce panneau ; il n'y a pas de mot d'activation : c'est appuyer pour parler.",
    "glance": [
      [
        "Rôle",
        "Panneau tactile mural pour ARMOR-SERVER (famille : Clients, parent : ARMOR-SERVER)",
      ],
      [
        "Technologie",
        "C++17, ESP-IDF 5.5.5, LVGL, ESP32-S3",
      ],
      [
        "Tests",
        "93081 vérifications dans 18 programmes hôte et 6 contrôles Python (`ctest`)",
      ],
      [
        "Carte",
        "Waveshare ESP32-S3-Touch-LCD-7C-BOX (800x480, GT911)",
      ],
      [
        "Fonctionne sur",
        "Une Waveshare ESP32-S3-Touch-LCD-7C-BOX ; tests sur hôte sur n'importe quel ordinateur",
      ],
      [
        "Sur matériel réel",
        "Aucun pour l'instant : le firmware se compile (ESP-IDF 5.5.5, non vérifié par la CI) mais n'a pas tourné sur la carte",
      ],
      [
        "Licence",
        "GPL-3.0-or-later",
      ],
    ],
    "status": {
      "software": "Le firmware a été compilé une fois (ESP-IDF 5.5.5), mais la compilation n'est pas contrôlée par l'intégration continue et il n'a jamais tourné sur une carte.",
      "tests": "93 081 vérifications dans 18 programmes d'hôte réussissent (`ctest`) : les réglages, ce que le panneau sait du serveur et quand c'est périmé, l'alarme sous contrainte qui n'est jamais affichée, l'échange vocal, les broches, les textes de l'écran en huit langues et les glyphes de ses polices.",
      "protocols": "L'échange avec le serveur et avec le service vocal ARMOR-VOICE-AI est testé contre des simulations ; c'est du push-to-talk, sans mot d'activation.",
      "ui": "La page web a tourné contre une simulation dans un vrai navigateur ; l'écran, le tactile et le son sont écrits d'après les exemples de Waveshare et attendent leur première mise sous tension.",
      "hardware": "Le firmware n'a pas tourné sur la carte : rien n'a encore tourné sur de vrais équipements.",
      "security": "Le code de configuration, la limite de connexions, le PIN Bluetooth, la gestion de la contrainte et les mises à jour signées sont testés sur l'hôte ; il n'y a pas eu de revue indépendante.",
      "updates": "Les contrôles de hash et de signature réussissent sur l'hôte ; une mise à jour par voie hertzienne n'a jamais été exécutée sur une carte.",
      "integration": "Les messages sont validés par rapport aux schémas partagés d'ARMOR-COMMON ; la liaison avec le serveur et avec le service vocal n'a pas été essayée depuis une carte.",
      "docs": "Huit langues, le guide du firmware, les notes de câblage et le journal des modifications sont à jour.",
    },
    "docs": [
      "[Conception](docs/DESIGN.md) et [matériel](docs/HARDWARE.md) : ce que montre le panneau et la carte",
      "[Voix](docs/VOICE.md) et [polices](docs/FONTS.md)",
      "[Firmware du nœud](docs/NODE_FIRMWARE.md) et [actions de build](docs/FIRMWARE_BUILD_ACTIONS.md)",
      "[Essais de banc](docs/BENCH_TESTS.md), [code de configuration](docs/SETUP_CODE.md) et [mise en service Bluetooth](docs/BLE_PROVISIONING.md)",
    ],
    "contributing_first": "Avant une pull request, lancez `ctest --test-dir build/host` and `python -I tools/armor_ci_validate.py` : il doit réussir. Voir [CONTRIBUTING.md](CONTRIBUTING.md) et le [code de conduite](CODE_OF_CONDUCT.md).",
    "languages_extra": "",
    "body": {
      "overview": r"""* **Un client d'ARMOR-SERVER, comme l'application Android :** il se connecte avec un utilisateur qu'un administrateur a créé pour lui, demande `GET /api/v1/panel/summary` (quelques centaines d'octets : le mode, les nœuds en ligne et les alarmes qui demandent une personne) toutes les quelques secondes et, quand la personne touche le bouton et confirme, arme, désarme ou acquitte. Si le serveur ne répond plus, l'écran dit que ce qu'il montre est ancien et le bouton est désactivé. Il écoute le canal en direct du serveur (un WebSocket) pour qu'un changement s'affiche aussitôt, et interroge comme avant quand le canal est absent, silencieux ou désactivé.
* **L'écran (800x480, LVGL) :** le mode dans la couleur de la pire alarme que personne n'a vue, un grand bouton armer/désarmer avec une question d'abord, les nœuds en ligne, les alarmes (les non vues d'abord), une nuit qui l'atténue, une veille après un temps sans toucher, un son et un réveil à l'arrivée d'une nouvelle alarme, et huit langues avec accents, japonais et chinois dessinés avec des polices générées pour exactement les caractères utilisés.
* **Un nœud comme les autres :** le même stockage de réglages, Wi-Fi, page web en huit langues, configuration Bluetooth depuis le téléphone, mise à jour du firmware avec retour arrière et HTTPS comme ARMOR-NODE-RADAR, ARMOR-NODE-SOLAR et ARMOR-NODE-ELECTRICAL (ils partagent `ARMOR-COMMON/firmware_base`), plus des pages pour le serveur, l'écran, le son et la voix ; il signale son existence à Studio par MQTT pour que Studio le liste avec sa page.
* **L'assistant vocal, appuyer pour parler :** un toucher ouvre le micro, le son part seulement vers le service vocal dont l'adresse est dans les réglages (désactivé par défaut), la réponse est affichée et dite ; l'ordre des étapes, les limites de temps et ce que fait un toucher sont une machine à états testée, et le panneau n'exécute aucune commande de lui-même ([le contrat](docs/VOICE.md)). L'enregistrement part en octets dans une requête binaire et la réponse parlée revient en octets ; à un serveur qui ne l'accepte pas, on envoie l'ancienne requête.
* **La carte :** Waveshare ESP32-S3-Touch-LCD-7C-BOX (32 Mo de flash, 16 Mo de PSRAM, écran RGB de 7 pouces avec tactile GT911, quatre micros, un haut-parleur) ; les broches viennent des exemples de Waveshare et un test prouve que deux fonctions ne partagent pas un GPIO ([la carte](docs/HARDWARE.md)).
* **Mises à jour par radio signées :** le nœud n'installe depuis GitHub qu'une image dont le SHA-256 correspond et qui porte une signature Ed25519 valide du responsable (la clé publique est dans le firmware, la privée ne quitte jamais le responsable) ; un fichier envoyé à la main par un administrateur dans le panneau reste accepté. Les pages et messages du panneau sont en huit langues.
* **Appairage Bluetooth avec un PIN :** le PIN à six chiffres est dérivé du code de configuration, imprimé sur la console USB et montré à un administrateur dans le panneau ; le téléphone doit le saisir avant de pouvoir écrire les réglages du nœud.
* **Pas encore :** une première compilation et mise sous tension du firmware, un mot de réveil, le service vocal sur le Jetson et une vue des caméras à l'écran.
* **Seule la maison peut utiliser le panneau :** le panneau répond par défaut au réseau privé (ou aux réseaux que son propriétaire indique, comme un VPN), refuse une liste qui exclurait celui qui l'enregistre, compte les mauvais mots de passe par personne et par adresse, et fonctionne derrière le proxy du serveur pour être atteint depuis l'extérieur sans publier le nœud.
* **Il dit ce qui se passe :** l'écran connaît le texte, en huit langues, de chaque code d'alarme que lève le serveur (réseau, solaire, électrique, zones d'alarme...) et il indique au serveur qu'il est un panneau mural ; il est donc listé comme tel et ne compte pas comme un radar.
* **Liaison chiffrée facultative avec le broker (TLS) :** désactivée par défaut, le nœud parle donc MQTT non chiffré comme avant. Un interrupteur et une zone pour le certificat de l'autorité propre à l'installation (PEM, 2 Ko au plus) dans la page Broker lui font se connecter en `mqtts://`, ne faire confiance qu'à cette autorité et vérifier que le certificat du broker a été établi pour l'adresse atteinte ; ce qui n'est pas un seul certificat PEM est refusé. Couvert par des tests sur ordinateur ; la poignée de main n'a pas encore été exécutée sur une carte.
* **Rapport de santé :** environ une fois par minute le nœud publie depuis combien de temps il tourne et pourquoi il a redémarré la dernière fois, sa mémoire libre, sa liaison et son signal Wi-Fi, combien de fois il s'est connecté au broker et la dernière erreur notée (`armor/health/<nœud>`, le contrat `node_health` d'ARMOR-COMMON). Le code qui le construit est partagé par tous les nœuds et testé sur un ordinateur ; il n'a pas tourné sur une carte.
* **Commande depuis le serveur :** Studio peut redémarrer le nœud proprement, le mettre en pause jusqu'à une heure (il reprend seul), mettre son travail en veille (sans fin, conservée aux redémarrages, le nœud reste connecté et continue de répondre), le faire se signaler, demander un instantané de diagnostic et le marquer en maintenance (`armor/control/<nœud>/...`, le contrat `node_control` d'ARMOR-COMMON). Chaque ordre se fait en deux temps avec un jeton à usage unique propre à cette opération, seul le serveur peut les écrire sur le broker, et il n'existe ni réinitialisation d'usine, ni effacement, ni sommeil profond. Tant que le panneau est en pause ou en veille, l'écran affiche un écran propre qui le dit et ne prend aucun toucher ; quand on lui demande de se signaler, une barre clignote en haut (jamais un son). Le code est partagé par tous les nœuds et testé sur un ordinateur ; il n'a pas tourné sur une carte.
* **Diagnostic sans câble :** après un démarrage qui n'était pas propre (plantage, chien de garde, chute d'alimentation, allocation échouée), le rapport de santé en donne la raison pendant dix minutes ; un plantage laisse son vidage mémoire (core dump) à consulter, télécharger ou effacer depuis le panneau ; les réglages enregistrés sont copiés avant chaque installation de micrologiciel et récupérés si une mise à jour les abîme ; et un administrateur peut demander au nœud, via le serveur, un paquet de diagnostic ou son journal avec un jeton à usage unique.
* **Une sirène qui se répète et des sons dans l'ordre :** tout son passe par une file à priorités (sirène, alarme, voix, confirmation, avis) ; la sirène se répète tant qu'il reste des alarmes critiques non acquittées (`audio.siren_repeat_s` 30, `audio.siren_max_repeats` 10) et les alarmes gardent un volume minimal (`audio.critical_min_volume` 40) ; la voix cède devant une alarme.
* **Une horloge sur batterie :** la puce PCF85063A de la carte donne l'heure au démarrage quand le nœud n'a pas encore d'heure réelle et que la puce est fiable, et elle est corrigée à chaque synchronisation ou réglage de l'heure (`time.rtc_enabled`, activé par défaut).
* **L'état d'un ordre, à l'écran :** le pied de page dit que l'ordre est en cours d'envoi tant qu'il est en route et qu'il a été confirmé pendant quelques secondes lorsqu'il est passé ; un refus y garde sa raison, comme avant.
* **Scellement facultatif des secrets enregistrés :** désactivé par défaut (`security.seal_secrets`, ou `nodes.nvs_encryption` du serveur). Activé, les mots de passe, jetons, clés, codes PIN et empreintes de mots de passe que le nœud enregistre sont scellés avec ChaCha20-Poly1305 et tout le reste reste lisible ; l'activer ou le désactiver les réécrit sans rien perdre, même si le nœud s'arrête en route. Aucun eFuse n'est brûlé et la flash n'est pas chiffrée : la clé est dans une partition de la même puce, donc cela ne protège **pas** contre quelqu'un qui tient la carte, et un nœud installé avant cette partition garde ses secrets tels quels jusqu'à ce qu'il soit flashé avec la nouvelle table de partitions.""",
      "role": r"""ARMOR-NODE-HMI est le panneau mural : un client d'[ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER), comme l'application Android, avec un écran de 7 pouces, un microphone et un haut-parleur. Il montre le mode, les nœuds en ligne et les alarmes qui demandent une personne, arme et désarme (avec le PIN) et acquitte les alarmes. C'est là que vivra l'assistant vocal ([ARMOR-VOICE-AI](https://github.com/JuanenRac/ARMOR-VOICE-AI)) quand son service vocal existera et, comme tout nœud, il se configure et se met à jour depuis [ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO).

| Nom | Comment | À quoi ça sert |
|---|---|---|
| ARMOR-SERVER | HTTPS `GET /api/v1/panel/summary`, WebSocket `/api/v1/panel/events` | Le résumé de la maison (modes, alarmes, nœuds, énergie) et ses changements ; le serveur décide de ce que fait un ordre |
| ARMOR-VOICE-AI | via le serveur | L'audio d'un tour va au service vocal ; la réponse est affichée et dite |
| ARMOR-STUDIO | menu Panneau tactile | Montre la santé du panneau et ouvre son panneau web |
| ARMOR-COMMON | base de firmware | Le firmware commun (panneau, connexions, mise à jour signée, configuration Bluetooth) en est copié |""",
      "architecture": r"""<p align="center">
  <img src="images/architecture.svg" alt="Architecture de ARMOR-NODE-HMI : qui l'appelle, ce qu'il contient et de quoi il dépend" width="100%">
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
| L'alarme de contrainte affichée à l'écran | Elle n'est jamais affichée (un test sur hôte le vérifie) ; et ce que le panneau sait du serveur est marqué périmé quand il est ancien |
| Un serveur qui n'est pas le serveur | Le certificat du serveur est épinglé (`server_pin`), pour les requêtes et pour le WebSocket du canal en direct ; le panneau se connecte avec son propre utilisateur, créé par un administrateur, avec le rôle `panel` (il ne peut pas utiliser Studio) |
| Désarmer sans PIN | Armer et désarmer demandent d'abord et prennent le PIN à l'écran (`pin_entry`) ; le serveur le revérifie |
| Audio vocal vers un endroit inattendu | Désactivée par défaut (`voice.enabled` faux) ; l'audio ne va qu'au service dont l'adresse est dans les réglages (l'adresse est validée et changer d'hôte efface le jeton) ; le panneau n'exécute aucun ordre de lui-même et il n'y a pas de mot d'activation : c'est appuyer pour parler |
| Une sirène que personne n'entend | Une seule file de priorité (sirène, alarme, voix, confirmation, avis) ; la sirène se répète tant que des alarmes critiques ne sont pas acquittées (`audio.siren_repeat_s` 30, de 10 à 600, 0 = pas de répétition ; `audio.siren_max_repeats` 10) et le volume critique ne descend jamais sous `audio.critical_min_volume` (40 %) |

Le firmware a été compilé une fois et n'a jamais tourné sur une carte : l'écran, le tactile, le son et la liaison avec le serveur sont écrits d'après les exemples de Waveshare, en attendant la première mise sous tension. Lisez [SECURITY.md](SECURITY.md) pour signaler une vulnérabilité.""",
      "interfaces": r"""| Partie | Ce qu'elle règle |
|---|---|
| ARMOR-SERVER | `GET /api/v1/panel/summary` toutes les `server.poll_s` (3 s, de 1 à 60) seulement quand le canal en direct est tombé, et le WebSocket `/api/v1/panel/events` tant que `server.live_events` est vrai (par défaut) : le résumé arrive quand le mode, les alarmes, les nœuds ou l'énergie changent ; l'utilisateur propre du panneau a le rôle `panel` |
| Voix | L'audio d'un tour va à ARMOR-VOICE-AI via le serveur (`/api/v1/voice/turn`, avec un corps multipart facultatif) ; `core/voice_session.hpp` est la machine d'états (ordre des étapes, limites de temps, ce que fait un toucher) ; voir [docs/VOICE.md](docs/VOICE.md) |
| Matériel | Waveshare ESP32-S3-Touch-LCD-7C-BOX : écran RGB 7 pouces 800x480, tactile GT911, quatre microphones, un haut-parleur, RTC PCF85063A (`time.rtc_enabled`, vrai par défaut), 32 Mo de flash et 16 Mo de PSRAM ; un test prouve qu'aucune fonction ne partage un GPIO |""",
      "configuration": r"""| Variable | Par défaut | Ce qu'elle règle |
|---|---|---|
| `server.poll_s`, `server.live_events` | 3 (1-60), true | La période d'interrogation du résumé et le canal en direct par WebSocket |
| `display.sleep_s` | 300 (0-3600) | Secondes avant la mise en veille de l'écran (0 = jamais) ; la luminosité et la luminosité de nuit sont aussi des réglages |
| `audio.critical_min_volume`, `audio.siren_repeat_s`, `audio.siren_max_repeats` | 40 (0-100), 30, 10 | Le volume minimal d'un son critique, la période de répétition de la sirène (0 ou de 10 à 600 s) et ses répétitions maximales |
| `audio.tone_by_source` | selon la gravité | Le son de chaque origine d'alarme (appareil, solaire, électrique, réseau, centrale, autre) : celui que dicte sa gravité, en avis, en alarme, en sirène ou sans son ; un son choisi retentit même sous la gravité minimale |
| `voice.enabled`, `voice.url`, `voice.token` | false, "", - | Le service vocal : désactivé par défaut ; l'adresse fait au plus 160 caractères et est validée (sinon `required` ou `invalid`) ; le jeton est effacé quand l'hôte change |
| `CONFIG_ARMOR_NODE_ID`, `_SETUP_CODE`, `_FLEET_SECRET`, `_MQTT_*`, `_HEARTBEAT_S`, `_BLE_SETUP_MINUTES`, `_BOOT_FACTORY_RESET` | - | Les réglages que tous les nœuds partagent : le nom (vide donne `armor-` et les derniers octets de la MAC), le code de configuration (vide : aléatoire), le secret de flotte (16+ caractères, jamais dans le dépôt), les premiers réglages du broker, le battement (de 2 à 300 s), les minutes de configuration Bluetooth (de 1 à 120) et la réinitialisation avec BOOT (8 s dans les 30 premières s) |""",
      "quickstart": r"""**Prérequis:** un compilateur C++17 pour les tests sur hôte ; le conteneur ESP-IDF 5.5.5 pour construire l'image ; une Waveshare ESP32-S3-Touch-LCD-7C-BOX.

```bash
cmake -S tests -B build/host && cmake --build build/host && ctest --test-dir build/host   # host tests, -Werror
node tools/panel_mock.mjs --user admin:adminpass123   # the panel of the node without a board
tools/build_node.sh                                   # the image in the ESP-IDF container
```

See the [firmware guide](docs/NODE_FIRMWARE.md) and the [Bluetooth channel](docs/BLE_PROVISIONING.md).

Voir la [conception](docs/DESIGN.md), la [carte](docs/HARDWARE.md), l'[assistant vocal](docs/VOICE.md), le [guide du firmware](docs/NODE_FIRMWARE.md) et les [polices](docs/FONTS.md).

Pour compiler le firmware à la main dans GitHub Actions, voir [compiler dans GitHub Actions](docs/FIRMWARE_BUILD_ACTIONS.md).""",
      "testing": r"""```bash
cmake -S tests -B build/host && cmake --build build/host && ctest --test-dir build/host
python -I tools/armor_ci_validate.py
```

18 programmes de test sur hôte et 6 contrôles Python tournent sous `ctest` ; 93081 vérifications comptées par les programmes hôte, compilés avec `-Werror`.

Contrôles Python : les textes du panneau en huit langues, les tâches, les chemins de sauvegarde, la session Bluetooth sous son verrou et les routes appelées par le panneau (et, dans certains nœuds, les codes HTTP ou les glyphes des polices)

Les tests sur hôte demandent un compilateur C++17 quelconque (Linux, WSL, MSYS2) ; le panneau web est aussi exercé dans un vrai navigateur contre un nœud de substitution (`tools/panel_mock.mjs`, `tools/panel_browser_test.mjs`).

`check_font_glyphs.py` vérifie que les polices ont tous les glyphes des huit langues (98 lignes) ; `test_clock` n'imprime que `ok`.""",
      "build": "`tools/build_node.sh` construit l'image dans le conteneur ESP-IDF 5.5.5 et la version porte l'image, son SHA-256 et sa signature Ed25519, une par carte ; l'image est écrite par USB-C la première fois, puis mise à jour depuis le panneau.",
      "troubleshooting": r"""| Vous voyez | Parce que | Faites |
|---|---|---|
| Vous avez perdu le mot de passe ou le nœud ne rejoint plus le réseau | Un nœud en configuration sans adresse après 90 s ouvre son propre Wi-Fi `ARMOR-SETUP-xxxxxx` (ouvrez `http://192.168.4.1/`) | Pour recommencer, maintenez BOOT 8 secondes dans les 30 premières secondes après la mise sous tension (efface réglages et utilisateurs), ou utilisez *Réinitialisation d'usine* dans le panneau |
| Une mise à jour depuis GitHub est refusée | La version n'a ni somme de contrôle ni signature, elles ne concordent pas (`e_no_checksum`, `e_no_signature`, `e_checksum_mismatch`, `e_bad_signature`), n'a pas d'image pour cette carte (`e_no_asset_for_board`) ou est d'un autre projet (`e_wrong_firmware`) | Le nœud n'a pas changé ; réessayez ou laissez un administrateur envoyer le fichier à la main |
| La voix ne démarre pas | `voice.enabled` est désactivé, ou `voice.url` est `required` ou `invalid` | Activez-la dans le panneau et donnez une adresse valide ; changer d'hôte efface le jeton |
| Le pied d'écran dit envoi, puis confirmée ou le motif | Un ordre est en route, a été confirmé quelques secondes, ou refusé et garde son motif | Lisez le motif ; c'est le serveur qui décide, pas le panneau |""",
      "structure": r"""<p align="center">
  <img src="images/repository-structure.svg" alt="Structure du dépôt de ARMOR-NODE-HMI" width="100%">
</p>

<details>
<summary>Version texte de l'arborescence</summary>

```text
ARMOR-NODE-HMI/
├── main/                                le firmware : un composant ESP-IDF
├── core/                                la logique sans ESP-IDF, testée sur ordinateur
├── panel/                               le panneau web intégré au firmware
├── tests/                               tests sur hôte et contrôles Python
├── docs/                                9 guides : conception, voix, polices, matériel
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
├── sdkconfig.board.lcd7box              les réglages d'une carte
├── secrets/                             exemple du fichier de nœud (les vrais ne sont pas versionnés)
├── dependencies.lock                    les versions épinglées des composants ESP-IDF
├── build-test.sh build-test.bat         lancer les tests par le flux partagé
└── .gitattributes .gitignore            réglages Git
```

</details>""",
      "roadmap": r"""**Limites connues aujourd'hui**

* Le firmware a été compilé une fois (ESP-IDF 5.5.5), mais la compilation n'est pas contrôlée par l'intégration continue et il n'a jamais tourné sur une carte.
* L'échange avec le serveur et avec le service vocal ARMOR-VOICE-AI est testé contre des simulations ; c'est du push-to-talk, sans mot d'activation.
* La page web a tourné contre une simulation dans un vrai navigateur ; l'écran, le tactile et le son sont écrits d'après les exemples de Waveshare et attendent leur première mise sous tension.
* Le firmware n'a pas tourné sur la carte : rien n'a encore tourné sur de vrais équipements.
* Le code de configuration, la limite de connexions, le PIN Bluetooth, la gestion de la contrainte et les mises à jour signées sont testés sur l'hôte ; il n'y a pas eu de revue indépendante.
* Les contrôles de hash et de signature réussissent sur l'hôte ; une mise à jour par voie hertzienne n'a jamais été exécutée sur une carte.
* Les messages sont validés par rapport aux schémas partagés d'ARMOR-COMMON ; la liaison avec le serveur et avec le service vocal n'a pas été essayée depuis une carte.

**Ensuite**

* Faire la première compilation complète et la première mise sous tension sur la carte, puis le service vocal sur le Jetson, un mot d'activation et la vue des caméras à l'écran.""",
    },
  },
  "it": {
    "tagline": "Il pannello touch della casa: uno schermo da 7 pollici a parete che mostra lo stato del sistema, lo attiva e disattiva e riconosce gli allarmi, con microfono e altoparlante per l'assistente vocale che arriverà (un nodo della famiglia sull'ESP32-S3-Touch-LCD-7C-BOX, con la sua pagina web per le impostazioni)",
    "honest": "Ciò che non dipende dalla scheda è reale e provato su un computer (le impostazioni, ciò che il pannello sa del server e quando è obsoleto, l'allarme di coercizione che non viene mai mostrato, la conversazione vocale e la lunga risposta del servizio vocale, i pin della scheda, i testi dello schermo in otto lingue e i glifi dei suoi caratteri, i controlli di versione e firma: 30,783 verifiche in 18 programmi di test) e lo è anche la pagina web (eseguita contro un sostituto in un browser reale). **Il firmware è stato compilato una volta (ESP-IDF 5.5.5, non verificato dall'integrazione continua) e non è mai girato su una scheda:** lo schermo, il touch, l'audio e il collegamento al server sono scritti dagli esempi di Waveshare per questa famiglia di schede e attendono la prima accensione. Il servizio vocale (ARMOR-VOICE-AI) risponde alle richieste di questo pannello; non c'è una parola di attivazione: si tocca per parlare.",
    "glance": [
      [
        "Ruolo",
        "Pannello touch a parete per ARMOR-SERVER (famiglia: Clients, padre: ARMOR-SERVER)",
      ],
      [
        "Tecnologia",
        "C++17, ESP-IDF 5.5.5, LVGL, ESP32-S3",
      ],
      [
        "Test",
        "93081 verifiche in 18 programmi host e 6 verifiche Python (`ctest`)",
      ],
      [
        "Scheda",
        "Waveshare ESP32-S3-Touch-LCD-7C-BOX (800x480, GT911)",
      ],
      [
        "Gira su",
        "Una Waveshare ESP32-S3-Touch-LCD-7C-BOX; test su host su qualsiasi computer",
      ],
      [
        "Su hardware reale",
        "Ancora nessuno: il firmware si compila (ESP-IDF 5.5.5, non verificato dalla CI) ma non è girato sulla scheda",
      ],
      [
        "Licenza",
        "GPL-3.0-or-later",
      ],
    ],
    "status": {
      "software": "Il firmware è stato compilato una volta (ESP-IDF 5.5.5), ma la compilazione non è controllata dall'integrazione continua e non ha mai girato su una scheda.",
      "tests": "Superano 93.081 controlli in 18 programmi host (`ctest`): le impostazioni, ciò che il pannello sa del server e quando è obsoleto, l'allarme sotto minaccia che non viene mai mostrato, lo scambio vocale, i pin, i testi dello schermo in otto lingue e i glifi dei suoi caratteri.",
      "protocols": "Lo scambio con il server e con il servizio vocale ARMOR-VOICE-AI è provato contro simulazioni; è push to talk, senza parola di attivazione.",
      "ui": "La pagina web è stata eseguita contro una simulazione in un browser reale; lo schermo, il tocco e l'audio sono scritti dagli esempi di Waveshare e attendono la prima accensione.",
      "hardware": "Il firmware non ha mai girato sulla scheda: nulla ha ancora funzionato su apparecchiature reali.",
      "security": "Il codice di configurazione, il limite di accessi, il PIN Bluetooth, la gestione della minaccia e gli aggiornamenti firmati sono testati sull'host; non c'è stata una revisione indipendente.",
      "updates": "I controlli di hash e firma passano sull'host; un aggiornamento via etere non è mai stato eseguito su una scheda.",
      "integration": "I messaggi sono validati contro gli schemi condivisi di ARMOR-COMMON; il collegamento con il server e con il servizio vocale non è stato provato da una scheda.",
      "docs": "Otto lingue, la guida del firmware, le note di cablaggio e il registro delle modifiche sono aggiornati.",
    },
    "docs": [
      "[Progetto](docs/DESIGN.md) e [hardware](docs/HARDWARE.md): cosa mostra il pannello e la scheda",
      "[Voce](docs/VOICE.md) e [caratteri](docs/FONTS.md)",
      "[Firmware del nodo](docs/NODE_FIRMWARE.md) e [azioni di build](docs/FIRMWARE_BUILD_ACTIONS.md)",
      "[Prove al banco](docs/BENCH_TESTS.md), [codice di configurazione](docs/SETUP_CODE.md) e [provisioning Bluetooth](docs/BLE_PROVISIONING.md)",
    ],
    "contributing_first": "Prima di una pull request esegui `ctest --test-dir build/host` and `python -I tools/armor_ci_validate.py`: deve passare. Vedi [CONTRIBUTING.md](CONTRIBUTING.md) e il [codice di condotta](CODE_OF_CONDUCT.md).",
    "languages_extra": "",
    "body": {
      "overview": r"""* **Un client di ARMOR-SERVER, come l'app Android:** accede con un utente creato per lui da un amministratore, chiede `GET /api/v1/panel/summary` (poche centinaia di byte: la modalità, i nodi online e gli allarmi che richiedono una persona) ogni pochi secondi e, quando la persona tocca il pulsante e conferma, attiva, disattiva o riconosce. Se il server smette di rispondere, lo schermo dice che ciò che mostra è vecchio e il pulsante è disattivato. Ascolta il canale in diretta del server (un WebSocket) così un cambiamento si vede subito, e interroga come prima quando il canale manca, tace o è disattivato.
* **Lo schermo (800x480, LVGL):** la modalità nel colore del peggior allarme che nessuno ha visto, un grande pulsante attiva/disattiva con domanda prima, i nodi online, gli allarmi (quelli non visti per primi), una notte che lo attenua, un riposo dopo un tempo senza tocchi, un suono e un risveglio all'arrivo di un nuovo allarme, e otto lingue con accenti, giapponese e cinese disegnati con font generati per esattamente i caratteri usati.
* **Un nodo come gli altri:** la stessa memoria delle impostazioni, Wi-Fi, pagina web in otto lingue, configurazione Bluetooth dal telefono, aggiornamento del firmware con ripristino e HTTPS come ARMOR-NODE-RADAR, ARMOR-NODE-SOLAR e ARMOR-NODE-ELECTRICAL (condividono `ARMOR-COMMON/firmware_base`), più pagine per server, schermo, suono e voce; segnala a Studio di esistere via MQTT perché Studio lo elenchi con la sua pagina.
* **L'assistente vocale, premi per parlare:** un tocco apre il microfono, l'audio va solo al servizio vocale il cui indirizzo è nelle impostazioni (disattivato per impostazione predefinita), la risposta viene mostrata e detta; l'ordine dei passi, i limiti di tempo e ciò che fa un tocco sono una macchina a stati provata, e il pannello non esegue alcun comando da solo ([il contratto](docs/VOICE.md)). La registrazione parte come byte in una richiesta binaria e la risposta parlata torna come byte; a un server che non la accetta si invia la richiesta precedente.
* **La scheda:** Waveshare ESP32-S3-Touch-LCD-7C-BOX (32 MB di flash, 16 MB di PSRAM, schermo RGB da 7 pollici con tocco GT911, quattro microfoni, un altoparlante); i pin vengono dagli esempi di Waveshare e un test dimostra che due funzioni non condividono un GPIO ([la scheda](docs/HARDWARE.md)).
* **Aggiornamenti via etere firmati:** il nodo installa da GitHub solo un'immagine il cui SHA-256 coincide e che porta una firma Ed25519 valida del responsabile (la chiave pubblica è nel firmware, quella privata non lascia mai il responsabile); un file caricato a mano da un amministratore nel pannello resta accettato. Le pagine e i messaggi del pannello sono in otto lingue.
* **Abbinamento Bluetooth con PIN:** il PIN a sei cifre deriva dal codice di configurazione, è stampato sulla console USB e mostrato a un amministratore nel pannello; il telefono deve inserirlo prima di poter scrivere le impostazioni del nodo.
* **Non ancora:** una prima compilazione e accensione del firmware, una parola di attivazione, il servizio vocale sul Jetson e una vista delle telecamere sullo schermo.
* **Solo la casa può usare il pannello:** il pannello risponde per impostazione predefinita alla rete privata (o alle reti indicate dal proprietario, come una VPN), rifiuta un elenco che escluderebbe chi lo salva, conta le password errate per persona e per indirizzo e funziona dietro il proxy del server per essere raggiunto da fuori casa senza pubblicare il nodo.
* **Dice cosa succede:** lo schermo conosce il testo, in otto lingue, di ogni codice d'allarme che il server solleva (rete, solare, elettrico, zone d'allarme...) e dice al server di essere un pannello a parete, quindi viene elencato come tale e non conta come radar.
* **Collegamento cifrato facoltativo con il broker (TLS):** disattivato per impostazione predefinita, quindi il nodo parla MQTT non cifrato come prima. Un interruttore e una casella per il certificato dell'autorità propria dell'installazione (PEM, al massimo 2 KB) nella pagina Broker lo fanno collegare con `mqtts://`, fidarsi solo di quell'autorità e verificare che il certificato del broker sia stato fatto per l'indirizzo raggiunto; ciò che non è un solo certificato PEM viene rifiutato. Coperto da test sul computer; l'handshake non è ancora stato eseguito su una scheda.
* **Rapporto di salute:** circa una volta al minuto il nodo pubblica da quanto è acceso e perché si è riavviato l'ultima volta, la memoria libera, il collegamento e il segnale Wi-Fi, quante volte si è connesso al broker e l'ultimo errore registrato (`armor/health/<nodo>`, il contratto `node_health` di ARMOR-COMMON). Il codice che lo costruisce è condiviso da tutti i nodi e testato su un computer; non è mai girato su una scheda.
* **Controllo dal server:** Studio può riavviare il nodo in modo pulito, metterlo in pausa fino a un'ora (riprende da solo), mettere il suo lavoro in standby (senza fine, conservato ai riavvii, il nodo resta connesso e continua a rispondere), farlo mostrare, chiedere un'istantanea diagnostica e segnarlo in manutenzione (`armor/control/<nodo>/...`, il contratto `node_control` di ARMOR-COMMON). Ogni ordine è in due passi con un token monouso legato a quell'operazione, solo il server può scriverli sul broker e non esistono ripristino di fabbrica, cancellazione né sonno profondo. Finché il pannello è in pausa o in standby lo schermo mostra una schermata propria che lo dice e non accetta tocchi; quando gli si chiede di identificarsi, in alto lampeggia una barra (mai un suono). Il codice è condiviso da tutti i nodi e provato su un computer; non ha ancora girato su una scheda.
* **Diagnostica senza cavo:** dopo un avvio non pulito (un blocco, un watchdog, un calo di alimentazione, un'allocazione fallita) il rapporto di salute ne indica la causa per dieci minuti; un arresto anomalo lascia il suo core dump da vedere, scaricare o cancellare dal pannello; le impostazioni salvate vengono copiate prima di ogni installazione del firmware e recuperate se un aggiornamento le danneggia; e un amministratore può chiedere al nodo, tramite il server, un pacchetto di diagnostica o il suo registro con un token monouso.
* **Una sirena che si ripete e suoni in ordine:** ogni suono passa per una coda con priorità (sirena, allarme, voce, conferma, avviso); la sirena si ripete finché restano allarmi critici non riconosciuti (`audio.siren_repeat_s` 30, `audio.siren_max_repeats` 10) e gli allarmi mantengono un volume minimo (`audio.critical_min_volume` 40); la voce cede a un allarme.
* **Un orologio con batteria:** il chip PCF85063A della scheda dà l'ora all'avvio quando il nodo non ha ancora un'ora reale e il chip è affidabile, e viene corretto a ogni sincronizzazione o impostazione dell'ora (`time.rtc_enabled`, attivo per impostazione predefinita).
* **Lo stato di un comando, sullo schermo:** il piè di pagina dice che il comando è in invio finché è in viaggio e che è stato confermato per qualche secondo quando è andato a buon fine; un rifiuto vi mantiene il suo motivo, come prima.
* **Sigillatura facoltativa dei segreti salvati:** disattivata per impostazione predefinita (`security.seal_secrets`, o `nodes.nvs_encryption` del server). Attiva, le password, i token, le chiavi, i PIN e gli hash delle password che il nodo salva restano sigillati con ChaCha20-Poly1305 e tutto il resto resta leggibile; attivarla o disattivarla li riscrive senza perdere nulla, anche se il nodo si ferma a metà. Nessun eFuse viene bruciato e la flash non è cifrata: la chiave si trova in una partizione dello stesso chip, quindi **non** protegge da chi ha la scheda, e un nodo installato prima di quella partizione mantiene i suoi segreti com'erano finché non viene flashato con la nuova tabella delle partizioni.""",
      "role": r"""ARMOR-NODE-HMI è il pannello a muro: un client di [ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER), come l'app Android, con uno schermo da 7 pollici, un microfono e un altoparlante. Mostra la modalità, i nodi online e gli allarmi che richiedono una persona, inserisce e disinserisce (con il PIN) e riconosce gli allarmi. È dove vivrà l'assistente vocale ([ARMOR-VOICE-AI](https://github.com/JuanenRac/ARMOR-VOICE-AI)) quando esisterà il suo servizio vocale e, come ogni nodo, si configura e si aggiorna da [ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO).

| Nome | Come | A cosa serve |
|---|---|---|
| ARMOR-SERVER | HTTPS `GET /api/v1/panel/summary`, WebSocket `/api/v1/panel/events` | Il riepilogo della casa (modalità, allarmi, nodi, energia) e le sue variazioni; il server decide cosa fa un ordine |
| ARMOR-VOICE-AI | tramite il server | L'audio di un turno va al servizio vocale; la risposta è mostrata e pronunciata |
| ARMOR-STUDIO | menu Pannello touch | Mostra la salute del pannello e apre il suo pannello web |
| ARMOR-COMMON | base firmware | Il firmware comune (pannello, accessi, aggiornamento firmato, configurazione Bluetooth) è copiato da lì |""",
      "architecture": r"""<p align="center">
  <img src="images/architecture.svg" alt="Architettura di ARMOR-NODE-HMI: chi lo chiama, cosa contiene e da cosa dipende" width="100%">
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
| L'allarme sotto coercizione mostrato sullo schermo | Non viene mai mostrato (un test su host lo verifica); e ciò che il pannello sa del server è segnato come scaduto quando è vecchio |
| Un server che non è il server | Il certificato del server è fissato (`server_pin`), per le richieste e per il WebSocket del canale live; il pannello accede con un proprio utente, creato da un amministratore, con il ruolo `panel` (non può usare Studio) |
| Disinserire senza PIN | Inserire e disinserire chiedono prima e prendono il PIN sullo schermo (`pin_entry`); il server lo ricontrolla |
| Audio vocale verso un posto inatteso | Spenta di default (`voice.enabled` falso); l'audio va solo al servizio il cui indirizzo è nelle impostazioni (l'indirizzo è validato e cambiare host cancella il token); il pannello non esegue alcun ordine da solo e non c'è parola di attivazione: è premi per parlare |
| Una sirena che nessuno sente | Una sola coda di priorità (sirena, allarme, voce, conferma, avviso); la sirena si ripete finché ci sono allarmi critici non confermati (`audio.siren_repeat_s` 30, da 10 a 600, 0 = nessuna ripetizione; `audio.siren_max_repeats` 10) e il volume critico non scende mai sotto `audio.critical_min_volume` (40 %) |

Il firmware è stato compilato una volta e non è mai girato su una scheda: schermo, touch, suono e collegamento al server sono scritti dagli esempi di Waveshare, in attesa della prima accensione. Leggi [SECURITY.md](SECURITY.md) per segnalare una vulnerabilità.""",
      "interfaces": r"""| Parte | Cosa imposta |
|---|---|
| ARMOR-SERVER | `GET /api/v1/panel/summary` ogni `server.poll_s` (3 s, da 1 a 60) solo mentre il canale live è caduto, e il WebSocket `/api/v1/panel/events` finché `server.live_events` è vero (predefinito): il riepilogo arriva quando cambiano modalità, allarmi, nodi o energia; l'utente proprio del pannello ha il ruolo `panel` |
| Voce | L'audio di un turno va a ARMOR-VOICE-AI tramite il server (`/api/v1/voice/turn`, con corpo multipart facoltativo); `core/voice_session.hpp` è la macchina a stati (ordine dei passi, limiti di tempo, cosa fa un tocco); vedi [docs/VOICE.md](docs/VOICE.md) |
| Hardware | Waveshare ESP32-S3-Touch-LCD-7C-BOX: schermo RGB da 7 pollici 800x480, touch GT911, quattro microfoni, un altoparlante, RTC PCF85063A (`time.rtc_enabled`, vero di default), 32 MB di flash e 16 MB di PSRAM; un test dimostra che nessuna funzione condivide un GPIO |""",
      "configuration": r"""| Variabile | Predefinito | Cosa imposta |
|---|---|---|
| `server.poll_s`, `server.live_events` | 3 (1-60), true | Il periodo di interrogazione del riepilogo e il canale live via WebSocket |
| `display.sleep_s` | 300 (0-3600) | Secondi prima che lo schermo vada a riposo (0 = mai); anche la luminosità e la luminosità notturna sono impostazioni |
| `audio.critical_min_volume`, `audio.siren_repeat_s`, `audio.siren_max_repeats` | 40 (0-100), 30, 10 | Il volume minimo di un suono critico, il periodo di ripetizione della sirena (0 o da 10 a 600 s) e le sue ripetizioni massime |
| `audio.tone_by_source` | secondo la gravità | Il suono di ogni origine di allarme (dispositivo, solare, elettrico, rete, centrale, altro): quello che dice la sua gravità, come avviso, come allarme, come sirena o senza suono; un suono scelto suona anche sotto la gravità minima |
| `voice.enabled`, `voice.url`, `voice.token` | false, "", - | Il servizio vocale: spento di default; l'indirizzo è lungo al massimo 160 caratteri e viene validato (altrimenti `required` o `invalid`); il token si cancella quando cambia l'host |
| `CONFIG_ARMOR_NODE_ID`, `_SETUP_CODE`, `_FLEET_SECRET`, `_MQTT_*`, `_HEARTBEAT_S`, `_BLE_SETUP_MINUTES`, `_BOOT_FACTORY_RESET` | - | Le impostazioni che tutti i nodi condividono: il nome (vuoto dà `armor-` e gli ultimi byte del MAC), il codice di configurazione (vuoto: casuale), il segreto di flotta (16+ caratteri, mai nel repository), le prime impostazioni del broker, il battito (da 2 a 300 s), i minuti di configurazione Bluetooth (da 1 a 120) e il ripristino con BOOT (8 s nei primi 30 s) |""",
      "quickstart": r"""**Requisiti:** un compilatore C++17 per i test su host; il container ESP-IDF 5.5.5 per costruire l'immagine; una Waveshare ESP32-S3-Touch-LCD-7C-BOX.

```bash
cmake -S tests -B build/host && cmake --build build/host && ctest --test-dir build/host   # host tests, -Werror
node tools/panel_mock.mjs --user admin:adminpass123   # the panel of the node without a board
tools/build_node.sh                                   # the image in the ESP-IDF container
```

See the [firmware guide](docs/NODE_FIRMWARE.md) and the [Bluetooth channel](docs/BLE_PROVISIONING.md).

Vedi la [progettazione](docs/DESIGN.md), la [scheda](docs/HARDWARE.md), l'[assistente vocale](docs/VOICE.md), la [guida al firmware](docs/NODE_FIRMWARE.md) e i [font](docs/FONTS.md).

Per compilare il firmware a mano in GitHub Actions, vedi [compilare in GitHub Actions](docs/FIRMWARE_BUILD_ACTIONS.md).""",
      "testing": r"""```bash
cmake -S tests -B build/host && cmake --build build/host && ctest --test-dir build/host
python -I tools/armor_ci_validate.py
```

18 programmi di test su host e 6 verifiche Python girano con `ctest`; 93081 verifiche contate dai programmi host, compilati con `-Werror`.

Verifiche Python: i testi del pannello in otto lingue, i task, i percorsi di salvataggio, la sessione Bluetooth sotto il suo lock e i percorsi chiamati dal pannello (e, in alcuni nodi, i codici HTTP o i glifi dei caratteri)

I test su host richiedono un qualsiasi compilatore C++17 (Linux, WSL, MSYS2); il pannello web è anche provato in un browser reale contro un nodo sostitutivo (`tools/panel_mock.mjs`, `tools/panel_browser_test.mjs`).

`check_font_glyphs.py` verifica che i caratteri abbiano tutti i glifi delle otto lingue (98 righe); `test_clock` stampa solo `ok`.""",
      "build": "`tools/build_node.sh` costruisce l'immagine nel container ESP-IDF 5.5.5 e la versione porta l'immagine, il suo SHA-256 e la sua firma Ed25519, una per scheda; l'immagine si scrive via USB-C la prima volta e poi si aggiorna dal pannello.",
      "troubleshooting": r"""| Vedi | Perché | Fai |
|---|---|---|
| Hai perso la password o il nodo non entra più in rete | Un nodo in configurazione senza indirizzo dopo 90 s apre un proprio Wi-Fi `ARMOR-SETUP-xxxxxx` (apri `http://192.168.4.1/`) | Per ricominciare tieni premuto BOOT per 8 secondi nei primi 30 secondi dopo l'accensione (cancella impostazioni e utenti), o usa *Ripristino di fabbrica* nel pannello |
| Un aggiornamento da GitHub è rifiutato | La versione non ha checksum o firma, non corrispondono (`e_no_checksum`, `e_no_signature`, `e_checksum_mismatch`, `e_bad_signature`), non ha un'immagine per questa scheda (`e_no_asset_for_board`) o è di un altro progetto (`e_wrong_firmware`) | Il nodo non è cambiato; riprova o lascia che un amministratore carichi il file a mano |
| La voce non parte | `voice.enabled` è spento, o `voice.url` è `required` o `invalid` | Accendila nel pannello e dai un indirizzo valido; cambiare host cancella il token |
| Il piè di pagina dice invio, poi confermata o il motivo | Un ordine è in viaggio, è stato confermato per qualche secondo, o è stato rifiutato e conserva il suo motivo | Leggi il motivo; decide il server, non il pannello |""",
      "structure": r"""<p align="center">
  <img src="images/repository-structure.svg" alt="Struttura del repository di ARMOR-NODE-HMI" width="100%">
</p>

<details>
<summary>Versione testuale dell'albero</summary>

```text
ARMOR-NODE-HMI/
├── main/                                il firmware: un componente ESP-IDF
├── core/                                la logica senza ESP-IDF, testata su un computer
├── panel/                               il pannello web incorporato nel firmware
├── tests/                               test su host e verifiche Python
├── docs/                                9 guide: progetto, voce, caratteri, hardware
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
├── sdkconfig.board.lcd7box              le impostazioni di una scheda
├── secrets/                             esempio del file del nodo (quelli veri non sono versionati)
├── dependencies.lock                    le versioni fissate dei componenti ESP-IDF
├── build-test.sh build-test.bat         eseguire i test tramite il flusso condiviso
└── .gitattributes .gitignore            impostazioni di Git
```

</details>""",
      "roadmap": r"""**Limiti noti oggi**

* Il firmware è stato compilato una volta (ESP-IDF 5.5.5), ma la compilazione non è controllata dall'integrazione continua e non ha mai girato su una scheda.
* Lo scambio con il server e con il servizio vocale ARMOR-VOICE-AI è provato contro simulazioni; è push to talk, senza parola di attivazione.
* La pagina web è stata eseguita contro una simulazione in un browser reale; lo schermo, il tocco e l'audio sono scritti dagli esempi di Waveshare e attendono la prima accensione.
* Il firmware non ha mai girato sulla scheda: nulla ha ancora funzionato su apparecchiature reali.
* Il codice di configurazione, il limite di accessi, il PIN Bluetooth, la gestione della minaccia e gli aggiornamenti firmati sono testati sull'host; non c'è stata una revisione indipendente.
* I controlli di hash e firma passano sull'host; un aggiornamento via etere non è mai stato eseguito su una scheda.
* I messaggi sono validati contro gli schemi condivisi di ARMOR-COMMON; il collegamento con il server e con il servizio vocale non è stato provato da una scheda.

**Prossimi passi**

* Fare la prima compilazione completa e la prima accensione sulla scheda, poi il servizio vocale sul Jetson, una parola di attivazione e la vista delle telecamere sullo schermo.""",
    },
  },
  "ja": {
    "tagline": "家のタッチパネル：壁に掛ける7インチ画面でシステムの状態を表示し、警戒・解除とアラームの確認ができ、将来の音声アシスタント用にマイクとスピーカーを備えています（ESP32-S3-Touch-LCD-7C-BOX 上のファミリーのノードで、設定用の専用Webページ付き）",
    "honest": "ボードに依存しない部分は実在し、コンピューター上でテストされています（設定、パネルがサーバーについて知っていることとそれが古くなる時点、決して表示されない強要警報、音声会話と音声サービスの長い応答、ボードのピン、8言語の画面テキストとフォントのグリフ、リリースと署名の検査：18つのテストプログラムで 93,081 項目）。Webページも同様です（実ブラウザで代替機に対して実行）。**ファームウェアは一度ビルドされましたが（ESP-IDF 5.5.5、継続的インテグレーションでは確認していません）、ボード上で動作したことはありません。**画面、タッチ、音、サーバーとの接続は、このボード系列向けの Waveshare のサンプルをもとに書かれており、初めての電源投入が必要です。音声サービス（ARMOR-VOICE-AI）はこのパネルの要求に応答します。ウェイクワードはなく、タッチして話します。",
    "glance": [
      [
        "役割",
        "ARMOR-SERVER 用の壁掛けタッチパネル（ファミリー：Clients、親：ARMOR-SERVER）",
      ],
      [
        "技術",
        "C++17, ESP-IDF 5.5.5, LVGL, ESP32-S3",
      ],
      [
        "テスト",
        "93081 件の検査（ホスト用プログラム 18 本と Python 検査 6 個、`ctest`）",
      ],
      [
        "基板",
        "Waveshare ESP32-S3-Touch-LCD-7C-BOX (800x480, GT911)",
      ],
      [
        "動作環境",
        "Waveshare ESP32-S3-Touch-LCD-7C-BOX、ホストテストは任意のコンピューター",
      ],
      [
        "実機での確認",
        "まだありません：ファームウェアはビルドできます（ESP-IDF 5.5.5、CI では未確認）が、ボード上では動作していません",
      ],
      [
        "ライセンス",
        "GPL-3.0-or-later",
      ],
    ],
    "status": {
      "software": "ファームウェアは一度ビルドしました（ESP-IDF 5.5.5）が、そのビルドは継続的インテグレーションでは確認されておらず、ボード上でも動かしていません。",
      "tests": "18 のホストプログラムで 93,081 件のチェックが通ります（`ctest`）：設定、パネルがサーバーについて知っていることとその古さ、決して表示しない脅迫警報、音声のやり取り、ピン、8 言語の画面文言とフォントのグリフ。",
      "protocols": "サーバーおよび音声サービス ARMOR-VOICE-AI とのやり取りは模擬に対してテストしています。プッシュトゥトークで、ウェイクワードはありません。",
      "ui": "Web ページは実ブラウザーで模擬に対して動かしました。画面、タッチ、音声は Waveshare のサンプルをもとに書いたもので、初回の電源投入を待っています。",
      "hardware": "ファームウェアはボード上で動かしていません。実機ではまだ何も動かしていません。",
      "security": "設定コード、ログイン制限、Bluetooth の PIN、脅迫時の扱い、署名付きアップデートはホストでテスト済みです。独立したレビューはまだありません。",
      "updates": "ハッシュと署名の確認はホストで通ります。無線アップデートはボード上で一度も実行していません。",
      "integration": "メッセージは ARMOR-COMMON の共有スキーマに対して検証されています。サーバーおよび音声サービスとの接続は、ボードからはまだ試していません。",
      "docs": "8 言語、ファームウェアガイド、配線メモ、変更履歴は最新です。",
    },
    "docs": [
      "[設計](docs/DESIGN.md)と[ハードウェア](docs/HARDWARE.md)：パネルの表示内容と基板",
      "[音声](docs/VOICE.md)と[フォント](docs/FONTS.md)",
      "[ノードのファームウェア](docs/NODE_FIRMWARE.md)と[ビルド手順](docs/FIRMWARE_BUILD_ACTIONS.md)",
      "[ベンチテスト](docs/BENCH_TESTS.md)、[セットアップコード](docs/SETUP_CODE.md)、[Bluetooth プロビジョニング](docs/BLE_PROVISIONING.md)",
    ],
    "contributing_first": "Pull Request の前に `ctest --test-dir build/host` and `python -I tools/armor_ci_validate.py` を実行してください。通る必要があります。[CONTRIBUTING.md](CONTRIBUTING.md) と[行動規範](CODE_OF_CONDUCT.md)を参照してください。",
    "languages_extra": "",
    "body": {
      "overview": r"""* **Android アプリと同じく ARMOR-SERVER のクライアント：** 管理者がこのパネル用に作成したユーザーでサインインし、数秒ごとに `GET /api/v1/panel/summary`（数百バイト：モード、オンラインのノード、人の対応が必要なアラーム）を取得し、人がボタンに触れて確認すると警戒・解除・確認を行います。サーバーが応答しなくなると、画面は表示が古いことを伝え、ボタンは無効になります。サーバーのライブチャンネル（WebSocket）を受信して変化をすぐに表示し、チャンネルが無い・無音・無効のときは従来どおり問い合わせます。
* **画面（800x480、LVGL）：** 誰も見ていない最も重大なアラームの色でモードを表示し、確認の質問付きの大きな警戒/解除ボタン、オンラインのノード、アラーム（未確認を先頭に）、夜間の減光、無操作でのスリープ、新しいアラームでの音と点灯、アクセント付きの言語と、使用する文字だけのために生成したフォントで描く日本語と中国語を含む7言語に対応します。
* **他と同じノード：** ARMOR-NODE-RADAR、ARMOR-NODE-SOLAR、ARMOR-NODE-ELECTRICAL と同じ設定ストア、Wi-Fi、8言語のWebページ、スマートフォンからのBluetooth設定、ロールバック付きファームウェア更新、HTTPS を備え（`ARMOR-COMMON/firmware_base` を共有）、サーバー・画面・サウンド・音声のページが加わります。MQTT で Studio に存在を知らせ、Studio がそのページ付きで一覧表示します。
* **音声アシスタント（プッシュトゥトーク）：** タッチでマイクが開き、音声は設定したアドレスの音声サービスにのみ送られ（既定ではオフ）、返答が表示・読み上げされます。手順の順序、時間制限、タッチの動作はテスト済みのステートマシンで、パネルが自らコマンドを実行することはありません（[契約](docs/VOICE.md)）。録音はバイナリ要求で生のバイト列として送られ、音声の返答もバイト列で戻ります。受け付けないサーバーには従来の要求を送ります。
* **ボード：** Waveshare ESP32-S3-Touch-LCD-7C-BOX（フラッシュ32 MB、PSRAM 16 MB、GT911タッチ付き7インチRGB画面、マイク4個、スピーカー）。ピンはWaveshareのサンプル由来で、2つの機能が同じGPIOを共有しないことをテストで証明しています（[ボード](docs/HARDWARE.md)）。
* **未対応：** ファームウェアの最初のコンパイルと電源投入、ウェイクワード、Jetson 上の音声サービス、画面上のカメラ表示。
* **署名付きの無線アップデート：**ノードが GitHub からインストールするのは、SHA-256 が一致し、管理者の有効な Ed25519 署名を持つイメージだけです（公開鍵はファームウェア内、秘密鍵は管理者の手元から出ません）。管理者がパネルで手動アップロードしたファイルは引き続き受け付けます。パネルのページとメッセージは 8 言語です。
* **PIN 付きの Bluetooth ペアリング：**6 桁の PIN は設定コードから導出され、USB コンソールに表示され、管理者にはパネルにも表示されます。スマートフォンはこれを入力して初めてノードの設定を書き込めます。
* **パネルを使えるのは家だけ：**パネルは既定でプライベートネットワーク（または所有者が指定した VPN などのネットワーク）にだけ応答し、保存する本人を締め出す一覧は拒否します。誤ったパスワードは人ごと・アドレスごとに数え、サーバーのプロキシの背後でも動くので、ノードを公開せずに家の外から使えます。
* **何が起きたかを伝えます：** 画面はサーバーが発する全てのアラームコード（ネットワーク、太陽光、電気、警報ゾーンなど）の文言を8言語で持ち、サーバーに壁掛けパネルであることを伝えるため、レーダーとして数えられず、パネルとして一覧されます。
* **ブローカーとの暗号化通信(TLS、任意):** 初期状態ではオフで、ノードはこれまでどおり暗号化なしの MQTT で通信します。ブローカーページのスイッチと、設備独自の認証局の証明書(PEM、最大 2 KB)の入力欄により、`mqtts://` で接続し、その認証局だけを信頼し、到達したアドレス向けに発行された証明書かを確認します。PEM 証明書 1 つでないものは拒否されます。ホストテストで検証済みで、ハンドシェイクはまだ基板では実行していません。
* **状態報告:** ノードは約 1 分ごとに、稼働時間と直前の再起動の理由、空きメモリ、回線と Wi-Fi 信号、ブローカーへの接続回数、最後に記録したエラーを公開します（`armor/health/<ノード>`、ARMOR-COMMON の `node_health` 契約）。作成するコードは全ノードで共有され、コンピューター上でテストされていますが、ボード上ではまだ動作していません。
* **サーバーからの制御：** Studio はノードをきれいに再起動し、最大 1 時間まで一時停止し（自動的に再開）、作業を待機にし（期限なし、再起動後も維持、ノードは接続したまま応答を続けます）、自分を表示させ、診断のスナップショットを求め、メンテナンス中として印を付けることができます（`armor/control/<ノード>/...`、ARMOR-COMMON の `node_control` 契約）。命令はすべて、その操作専用の使い捨てトークンによる 2 段階で、ブローカーに書き込めるのはサーバーだけです。工場出荷時リセットも消去もディープスリープもありません。一時停止中または待機中のパネルは、その旨を示す専用画面を表示してタッチを受け付けません。識別を求められると、画面上部のバーが点滅します（音は鳴らしません）。 このコードは全ノードで共有され、コンピューター上でテスト済みですが、実機ではまだ動作していません。
* **ケーブルなしの診断：** 正常でない起動（クラッシュ、ウォッチドッグ、電源の電圧低下、メモリ確保の失敗）の後、ヘルスレポートが10分間その原因を伝えます。クラッシュするとコアダンプが残り、パネルから確認、ダウンロード、削除できます。保存された設定はファームウェアのインストールごとにコピーされ、更新で壊れた場合は復元されます。管理者はサーバー経由で、使い捨てトークンを使って、ノードに診断パッケージまたはログを要求できます。
* **繰り返すサイレンと順序のある音:** すべての音は優先度付きキュー(サイレン、警報、音声、確認、通知)を通ります。確認されていない重大な警報がある間はサイレンが繰り返され(`audio.siren_repeat_s` 30、`audio.siren_max_repeats` 10)、警報は最小音量を保ちます(`audio.critical_min_volume` 40)。音声は警報に道を譲ります。
* **バッテリーバックアップ付きの時計:** ノードがまだ実時刻を持たず、チップが信頼できる場合は、起動時にボードの PCF85063A チップから時刻を得ます。時刻の同期や設定のたびにチップも補正されます(`time.rtc_enabled`、既定でオン)。
* **画面に出る命令の状態:** 命令が送信中の間はフッターに送信中と表示され、成功すると数秒間「実行しました」と表示されます。拒否された場合は、これまでどおり理由がそこに残ります。
* **保存された秘密情報の任意の封印:** 既定ではオフです(`security.seal_secrets`、またはサーバーの `nodes.nvs_encryption`)。オンにすると、ノードが保存するパスワード、トークン、鍵、PIN、パスワードのハッシュが ChaCha20-Poly1305 で封印され、それ以外は読めるままです。オン/オフの切り替えは何も失わずに書き直し、途中で止まっても大丈夫です。eFuse は焼かれず、フラッシュも暗号化されません。鍵は同じチップのパーティションにあるため、基板を手にした人に対する保護には**なりません**。このパーティションがない時期にインストールされたノードは、新しいパーティションテーブルで書き込むまで従来のままです。""",
      "role": r"""ARMOR-NODE-HMI は壁掛けパネルです。Android アプリと同じく [ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER) のクライアントで、7 インチ画面、マイク、スピーカーを備えます。モード、オンラインのノード、人が必要な警報を表示し、警戒・解除（PIN 付き）と警報の確認を行います。音声サービスができれば、音声アシスタント（[ARMOR-VOICE-AI](https://github.com/JuanenRac/ARMOR-VOICE-AI)）はここに住み、他のノードと同じく [ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) から設定・更新します。

| 名前 | 方法 | 用途 |
|---|---|---|
| ARMOR-SERVER | HTTPS `GET /api/v1/panel/summary`, WebSocket `/api/v1/panel/events` | 家の概要（モード、アラーム、ノード、エネルギー）とその変化。命令の扱いはサーバーが決める |
| ARMOR-VOICE-AI | サーバー経由 | 1 ターンの音声が音声サービスに送られ、返答が表示・発話される |
| ARMOR-STUDIO | タッチパネルメニュー | パネルの状態を表示し、その Web パネルを開く |
| ARMOR-COMMON | ファームウェア基盤 | 共通ファームウェア（パネル、ログイン、署名付き更新、Bluetooth セットアップ）はここからコピー |""",
      "architecture": r"""<p align="center">
  <img src="images/architecture.svg" alt="ARMOR-NODE-HMI のアーキテクチャ：呼び出し元、内部、依存先" width="100%">
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
| 強要アラームが画面に表示される | 表示されません（ホストのテストで検査）。パネルがサーバーについて知っていることは、古くなると期限切れと表示されます |
| サーバーになりすました相手 | サーバーの証明書は固定され（`server_pin`）、要求とライブチャネルの WebSocket の両方に使われます。パネルは管理者が作った専用ユーザー（ロール `panel`、Studio は使えません）でサインインします |
| PIN なしのディスアーム | アームとディスアームは先に確認し、画面で PIN を受け付けます（`pin_entry`）。サーバーも再確認します |
| 音声が想定外の場所へ送られる | 初期はオフ（`voice.enabled` が false）。音声は設定にあるアドレスのサービスにだけ送られ（アドレスは検証され、ホストを変えるとトークンは消えます）、パネルが自分でコマンドを実行することはなく、ウェイクワードもなくプッシュトゥトークです |
| 誰にも聞こえないサイレン | 優先度つきキューは 1 つだけ（サイレン、アラーム、音声、確認、通知）。重大アラームが未確認の間はサイレンを繰り返し（`audio.siren_repeat_s` 30、10〜600、0 = 繰り返しなし、`audio.siren_max_repeats` 10）、重大時の音量は `audio.critical_min_volume`（40 %）を下回りません |

ファームウェアは一度ビルドしただけで、基板では一度も動いていません。画面、タッチ、音、サーバーとの接続は Waveshare のサンプルから書いたもので、初めての電源投入を待っています。脆弱性の報告は [SECURITY.md](SECURITY.md) を参照してください。""",
      "interfaces": r"""| 部分 | 設定内容 |
|---|---|
| ARMOR-SERVER | ライブチャネルが落ちている間だけ `server.poll_s`（3 秒、1〜60）ごとに `GET /api/v1/panel/summary`、`server.live_events` が true（既定）の間は WebSocket `/api/v1/panel/events`。モード、アラーム、ノード、エネルギーが変わると概要が届きます。パネル専用ユーザーのロールは `panel` |
| 音声 | 1 ターンの音声はサーバー経由で ARMOR-VOICE-AI に送られます（`/api/v1/voice/turn`、multipart ボディは任意）。`core/voice_session.hpp` が状態機械（手順の順序、時間制限、タッチの動作）です。[docs/VOICE.md](docs/VOICE.md) を参照 |
| ハードウェア | Waveshare ESP32-S3-Touch-LCD-7C-BOX：7 インチ RGB 画面 800x480、GT911 タッチ、マイク 4 個、スピーカー、RTC PCF85063A（`time.rtc_enabled`、既定は true）、フラッシュ 32 MB、PSRAM 16 MB。どの機能も GPIO を共有しないことをテストで確認 |""",
      "configuration": r"""| 変数 | 既定値 | 設定内容 |
|---|---|---|
| `server.poll_s`, `server.live_events` | 3 (1-60), true | 概要の問い合わせ周期と WebSocket のライブチャネル |
| `display.sleep_s` | 300 (0-3600) | 画面がスリープするまでの秒数（0 = なし）。明るさと夜間の明るさも設定です |
| `audio.critical_min_volume`, `audio.siren_repeat_s`, `audio.siren_max_repeats` | 40 (0-100), 30, 10 | 重大な音の最小音量、サイレンの繰り返し周期（0 または 10〜600 秒）、最大繰り返し回数 |
| `audio.tone_by_source` | 重大度に従う | 警報の発生元ごと(デバイス、ソーラー、電気、ネットワーク、中央、その他)の音:重大度どおり、通知、警報、サイレン、または無音。選んだ音は最低重大度を下回っても鳴ります |
| `voice.enabled`, `voice.url`, `voice.token` | false, "", - | 音声サービス：初期はオフ。アドレスは 160 文字以内で検証され（満たさないと `required` か `invalid`）、ホストが変わるとトークンは消えます |
| `CONFIG_ARMOR_NODE_ID`, `_SETUP_CODE`, `_FLEET_SECRET`, `_MQTT_*`, `_HEARTBEAT_S`, `_BLE_SETUP_MINUTES`, `_BOOT_FACTORY_RESET` | - | すべてのノードに共通する設定：名前（空なら `armor-` と MAC の下位バイト）、セットアップコード（空ならランダム）、フリートシークレット（16 文字以上、リポジトリには置かない）、最初のブローカー設定、ハートビート（2〜300 秒）、Bluetooth セットアップの分数（1〜120）、BOOT によるリセット（最初の 30 秒に 8 秒） |""",
      "quickstart": r"""**必要なもの:** ホストテスト用の C++17 コンパイラ、イメージのビルド用の ESP-IDF 5.5.5 コンテナ、Waveshare ESP32-S3-Touch-LCD-7C-BOX。

```bash
cmake -S tests -B build/host && cmake --build build/host && ctest --test-dir build/host   # host tests, -Werror
node tools/panel_mock.mjs --user admin:adminpass123   # the panel of the node without a board
tools/build_node.sh                                   # the image in the ESP-IDF container
```

See the [firmware guide](docs/NODE_FIRMWARE.md) and the [Bluetooth channel](docs/BLE_PROVISIONING.md).

[設計](docs/DESIGN.md)、[ボード](docs/HARDWARE.md)、[音声アシスタント](docs/VOICE.md)、[ファームウェアガイド](docs/NODE_FIRMWARE.md)、[フォント](docs/FONTS.md)を参照してください。

GitHub Actions で手動でファームウェアをビルドするには、[GitHub Actions でのビルド](docs/FIRMWARE_BUILD_ACTIONS.md)を参照してください。""",
      "testing": r"""```bash
cmake -S tests -B build/host && cmake --build build/host && ctest --test-dir build/host
python -I tools/armor_ci_validate.py
```

ホスト用テストプログラム 18 個と Python の検査 6 個を `ctest` で実行します。ホストのプログラムが数えた検査は 93081 件で、`-Werror` でビルドします。

Python の検査：8 言語のパネル文言、タスク、保存パス、ロック下の Bluetooth セッション、パネルが呼ぶルート（ノードによっては HTTP コードやフォントのグリフも）

ホストテストには任意の C++17 コンパイラ（Linux、WSL、MSYS2）が必要です。Web パネルは代役ノード（`tools/panel_mock.mjs`、`tools/panel_browser_test.mjs`）を相手に実際のブラウザでも検証します。

`check_font_glyphs.py` が、フォントに 8 言語のすべてのグリフがあることを検査します（98 行）。`test_clock` は `ok` だけを出力します。""",
      "build": "`tools/build_node.sh` が ESP-IDF 5.5.5 コンテナでイメージをビルドし、リリースにはイメージ、その SHA-256 と Ed25519 署名が基板ごとに付きます。イメージは初回のみ USB-C で書き込み、その後はパネルから更新します。",
      "troubleshooting": r"""| 症状 | 原因 | 対処 |
|---|---|---|
| パスワードを忘れた、またはノードがネットワークに参加しない | セットアップ中でアドレスがないノードは 90 秒後に独自の Wi-Fi `ARMOR-SETUP-xxxxxx` を開きます（`http://192.168.4.1/` を開く） | 最初からやり直すには、電源投入後 30 秒以内に BOOT を 8 秒押し続ける（設定とユーザーを消去）か、パネルの*工場出荷状態に戻す*を使います |
| GitHub からの更新が拒否される | リリースにチェックサムや署名がない、一致しない（`e_no_checksum`、`e_no_signature`、`e_checksum_mismatch`、`e_bad_signature`）、この基板用のイメージがない（`e_no_asset_for_board`）、または別プロジェクトのもの（`e_wrong_firmware`） | ノードは変更されていません。再試行するか、管理者が手動でファイルをアップロード |
| 音声が始まらない | `voice.enabled` がオフ、または `voice.url` が `required` か `invalid` | パネルでオンにして有効なアドレスを入れる（ホストを変えるとトークンは消える） |
| フッターが「送信中」のあと「確認済み」か理由を表示する | 命令が送信中、数秒間確認済み、または拒否されて理由が残っている状態 | 理由を読む（決めるのはサーバーでパネルではない） |""",
      "structure": r"""<p align="center">
  <img src="images/repository-structure.svg" alt="ARMOR-NODE-HMI のリポジトリ構造" width="100%">
</p>

<details>
<summary>ツリーのテキスト版</summary>

```text
ARMOR-NODE-HMI/
├── main/                                ファームウェア（ESP-IDF コンポーネント）
├── core/                                ESP-IDF なしのロジック（コンピューターでテスト）
├── panel/                               ファームウェアに埋め込まれた Web パネル
├── tests/                               ホストテストと Python 検査
├── docs/                                9 つのガイド：設計、音声、フォント、ハードウェア
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
├── sdkconfig.board.lcd7box              基板ごとの設定
├── secrets/                             ノードファイルの例（本物はバージョン管理しません）
├── dependencies.lock                    ESP-IDF コンポーネントの固定バージョン
├── build-test.sh build-test.bat         共通のワークフローでテストを実行
└── .gitattributes .gitignore            Git の設定
```

</details>""",
      "roadmap": r"""**現時点の既知の制限**

* ファームウェアは一度ビルドしました（ESP-IDF 5.5.5）が、そのビルドは継続的インテグレーションでは確認されておらず、ボード上でも動かしていません。
* サーバーおよび音声サービス ARMOR-VOICE-AI とのやり取りは模擬に対してテストしています。プッシュトゥトークで、ウェイクワードはありません。
* Web ページは実ブラウザーで模擬に対して動かしました。画面、タッチ、音声は Waveshare のサンプルをもとに書いたもので、初回の電源投入を待っています。
* ファームウェアはボード上で動かしていません。実機ではまだ何も動かしていません。
* 設定コード、ログイン制限、Bluetooth の PIN、脅迫時の扱い、署名付きアップデートはホストでテスト済みです。独立したレビューはまだありません。
* ハッシュと署名の確認はホストで通ります。無線アップデートはボード上で一度も実行していません。
* メッセージは ARMOR-COMMON の共有スキーマに対して検証されています。サーバーおよび音声サービスとの接続は、ボードからはまだ試していません。

**今後**

* 基板での最初のフルビルドと初めての電源投入を行い、続いて Jetson の音声サービス、ウェイクワード、画面でのカメラ表示に進む。""",
    },
  },
  "zh": {
    "tagline": "家用触摸面板：挂在墙上的7英寸屏幕，显示系统状态、布防与撤防并确认警报，配有麦克风和扬声器供将来的语音助手使用（家族中基于 ESP32-S3-Touch-LCD-7C-BOX 的节点，带有自己的设置网页）",
    "honest": "不依赖板子的部分是真实的，并已在计算机上测试（设置、面板对服务器的了解及其何时过期、永不显示的胁迫告警、语音对话和语音服务的长回复、板子的引脚、八种语言的屏幕文字及其字体字形、发布与签名检查：18 个测试程序共 93,081 项检查），网页也是如此（在真实浏览器中对替身运行）。**固件已构建过一次（ESP-IDF 5.5.5，持续集成不检查），但从未在板上运行：**屏幕、触摸、声音和与服务器的连接是根据 Waveshare 对这一系列板子的示例编写的，等待首次上电。语音服务（ARMOR-VOICE-AI）会应答此面板的请求；没有唤醒词，需点按说话。",
    "glance": [
      [
        "角色",
        "ARMOR-SERVER 的壁挂触摸面板（家族：Clients，上级：ARMOR-SERVER）",
      ],
      [
        "技术栈",
        "C++17, ESP-IDF 5.5.5, LVGL, ESP32-S3",
      ],
      [
        "测试",
        "93081 项检查（18 个主机程序和 6 项 Python 检查，`ctest`）",
      ],
      [
        "电路板",
        "Waveshare ESP32-S3-Touch-LCD-7C-BOX (800x480, GT911)",
      ],
      [
        "运行位置",
        "Waveshare ESP32-S3-Touch-LCD-7C-BOX；主机测试可在任何计算机上运行",
      ],
      [
        "真实硬件",
        "暂无：固件可以构建（ESP-IDF 5.5.5，CI 未检查），但还没有在板上运行",
      ],
      [
        "许可证",
        "GPL-3.0-or-later",
      ],
    ],
    "status": {
      "software": "固件构建过一次（ESP-IDF 5.5.5），但该构建不在持续集成的检查范围内，也从未在板子上运行过。",
      "tests": "18 个主机程序中的 93,081 项检查通过（`ctest`）：设置、面板对服务器的了解及其何时过期、从不显示的胁迫报警、语音交换、引脚、屏幕上八种语言的文字及其字体的字形。",
      "protocols": "与服务器和语音服务 ARMOR-VOICE-AI 的交互已对照模拟测试；采用按键说话，没有唤醒词。",
      "ui": "网页已在真实浏览器中对模拟运行过；屏幕、触摸和声音依据 Waveshare 的示例编写，等待首次上电。",
      "hardware": "固件尚未在板子上运行过：还没有在真实设备上运行过。",
      "security": "设置码、登录限制、蓝牙 PIN、胁迫处理和签名更新已在主机上测试；没有经过独立审查。",
      "updates": "哈希和签名检查在主机上通过；空中更新从未在板子上运行过。",
      "integration": "消息已对照 ARMOR-COMMON 的共享模式验证；与服务器和语音服务的连接尚未从板子上试过。",
      "docs": "八种语言、固件指南、接线说明和更新日志均为最新。",
    },
    "docs": [
      "[设计](docs/DESIGN.md)和[硬件](docs/HARDWARE.md)：面板显示的内容和电路板",
      "[语音](docs/VOICE.md)和[字体](docs/FONTS.md)",
      "[节点固件](docs/NODE_FIRMWARE.md)和[固件构建操作](docs/FIRMWARE_BUILD_ACTIONS.md)",
      "[台架测试](docs/BENCH_TESTS.md)、[设置码](docs/SETUP_CODE.md)和[蓝牙配置](docs/BLE_PROVISIONING.md)",
    ],
    "contributing_first": "提交 Pull Request 之前请运行 `ctest --test-dir build/host` and `python -I tools/armor_ci_validate.py`：必须通过。参见 [CONTRIBUTING.md](CONTRIBUTING.md) 和[行为准则](CODE_OF_CONDUCT.md)。",
    "languages_extra": "",
    "body": {
      "overview": r"""* **像 Android 应用一样是 ARMOR-SERVER 的客户端：** 使用管理员为它创建的用户登录，每隔几秒请求 `GET /api/v1/panel/summary`（几百字节：模式、在线节点和需要人处理的警报），当人触摸按钮并确认后进行布防、撤防或确认。如果服务器不再响应，屏幕会提示所显示内容已过期，并禁用按钮。它监听服务器的实时通道（WebSocket），使变化立即显示；通道缺失、无响应或被关闭时，仍像以前一样查询。
* **屏幕（800x480，LVGL）：** 以无人查看的最严重警报的颜色显示模式，带先行确认的大号布防/撤防按钮、在线节点、警报（未查看的优先）、夜间调暗、一段时间无触摸后休眠、新警报到来时发声并唤醒，支持八种语言（含重音字符，日文和中文使用专为所用字符生成的字体绘制）。
* **与其他节点相同的节点：** 与 ARMOR-NODE-RADAR、ARMOR-NODE-SOLAR、ARMOR-NODE-ELECTRICAL 相同的设置存储、Wi-Fi、八种语言的网页、手机蓝牙设置、可回滚的固件更新和 HTTPS（共享 `ARMOR-COMMON/firmware_base`），另有服务器、屏幕、声音和语音页面；它通过 MQTT 告知 Studio 自己的存在，使 Studio 带着其页面列出它。
* **语音助手，按键说话：** 触摸打开麦克风，音频只会发送到设置中填写地址的语音服务（默认关闭），回答会显示并朗读；步骤顺序、时间限制以及触摸的作用是一个经过测试的状态机，面板自己不执行任何命令（[契约](docs/VOICE.md)）。录音以二进制请求中的原始字节发送，语音回复也以字节返回；对不接受的服务器则发送旧式请求。
* **开发板：** Waveshare ESP32-S3-Touch-LCD-7C-BOX（32 MB 闪存、16 MB PSRAM、带 GT911 触摸的7英寸RGB屏幕、四个麦克风、一个扬声器）；引脚来自 Waveshare 的示例，并有测试证明没有两个功能共用同一个 GPIO（[开发板](docs/HARDWARE.md)）。
* **签名的无线更新：**节点只会从 GitHub 安装 SHA-256 匹配且带有维护者有效 Ed25519 签名的镜像（公钥在固件中，私钥从不离开维护者）；管理员在面板中手动上传的文件仍然被接受。面板的页面和消息有八种语言。
* **带 PIN 的蓝牙配对：**六位 PIN 由设置码派生，打印在 USB 控制台上并向管理员显示在面板中；手机必须输入它才能写入节点的设置。
* **尚未完成：** 固件的第一次编译和上电、唤醒词、Jetson 上的语音服务，以及屏幕上的摄像头视图。
* **只有家中才能使用面板：**面板默认只响应私有网络（或所有者列出的网络，如 VPN），拒绝会把保存者自己挡在外面的列表，按人和按地址统计错误密码，并可在服务器代理之后工作，从而无需公开节点就能在家外访问。
* **它会说明发生了什么：** 屏幕知道服务器发出的每个报警代码（网络、太阳能、电气、报警防区等）的八种语言文字，并告诉服务器自己是壁挂面板，因此会作为面板列出，不计为雷达。
* **可选的与代理加密连接(TLS):** 默认关闭,因此节点仍像以前一样使用未加密的 MQTT。代理页面中的一个开关和一个用于填写本安装自有证书颁发机构证书(PEM,最大 2 KB)的框,会让节点用 `mqtts://` 连接、只信任该机构,并检查代理证书是否为其所到达的地址而签发;不是单个 PEM 证书的内容会被拒绝。已有主机测试覆盖;握手尚未在电路板上运行。
* **健康报告：** 节点大约每分钟发布一次：已运行多久、上次为何重启、可用内存、连接与 Wi-Fi 信号、连接代理的次数以及记录的最后一个错误（`armor/health/<节点>`，即 ARMOR-COMMON 的 `node_health` 契约）。生成它的代码由所有节点共享并在计算机上测试；尚未在开发板上运行。
* **由服务器控制：** Studio 可以干净地重启节点、将其暂停至多一小时（自动恢复）、让其工作进入待机（无期限，重启后仍保持，节点保持连接并继续应答）、让它显示自己、请求诊断快照，并把它标记为维护中（`armor/control/<节点>/...`，ARMOR-COMMON 的 `node_control` 契约）。每条命令分两步，使用只属于该操作的一次性令牌，只有服务器可以在代理上写入，并且没有恢复出厂设置、擦除或深度睡眠。面板处于暂停或待机时，屏幕显示专门的提示画面且不响应触摸；被要求识别自己时，顶部的横条会闪烁（绝不发声）。 该代码由所有节点共用，并已在计算机上测试；尚未在电路板上运行过。
* **无需线缆的诊断：** 在一次不干净的启动之后（崩溃、看门狗、电源跌落、内存分配失败），健康报告会在十分钟内说明原因；崩溃会留下核心转储（core dump），可在面板中查看、下载或删除；已保存的设置会在每次固件安装前被复制，并在更新损坏它们时恢复；管理员还可以通过服务器，用一次性令牌向节点索取诊断包或其日志。
* **会重复的警笛与有序的声音:** 所有声音都经过一个优先级队列(警笛、报警、语音、确认、提示);只要还有未确认的严重报警,警笛就会重复(`audio.siren_repeat_s` 30,`audio.siren_max_repeats` 10),报警保持最低音量(`audio.critical_min_volume` 40);语音会让位于报警。
* **带电池的时钟:** 当节点还没有真实时间且芯片可信时,开机时使用电路板上 PCF85063A 芯片提供的时间;每次同步或设置时间时都会校正该芯片(`time.rtc_enabled`,默认开启)。
* **屏幕上的指令状态:** 指令在途中时页脚显示正在发送,指令完成后会显示已确认几秒钟;被拒绝时仍像以前一样在页脚显示原因。
* **可选的已存储机密封存:** 默认关闭(`security.seal_secrets`,或服务器的 `nodes.nvs_encryption`)。开启后,节点保存的密码、令牌、密钥、PIN 和密码哈希会用 ChaCha20-Poly1305 封存,其余内容仍可读取;开启或关闭时会无损重写,即使节点中途停止也不会丢失。不会烧写 eFuse,闪存也不加密:密钥在同一芯片的一个分区中,因此**不能**防范持有电路板的人;在该分区出现之前安装的节点会保持原样,直到用新的分区表重新烧录。""",
      "role": r"""ARMOR-NODE-HMI 是壁挂面板：与 Android 应用一样是 [ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER) 的客户端，配有 7 英寸屏幕、麦克风和扬声器。它显示模式、在线节点和需要人处理的报警，可布防和撤防（需 PIN）并确认报警。语音助手（[ARMOR-VOICE-AI](https://github.com/JuanenRac/ARMOR-VOICE-AI)）在其语音服务存在后将住在这里，并且和所有节点一样，从 [ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) 进行设置和更新。

| 名称 | 方式 | 用途 |
|---|---|---|
| ARMOR-SERVER | HTTPS `GET /api/v1/panel/summary`, WebSocket `/api/v1/panel/events` | 住宅概要（模式、报警、节点、能源）及其变化；命令的效果由服务器决定 |
| ARMOR-VOICE-AI | 通过服务器 | 一轮对话的音频发送到语音服务；回复会被显示并朗读 |
| ARMOR-STUDIO | 触摸面板菜单 | 显示面板的健康状态并打开其网页面板 |
| ARMOR-COMMON | 固件基础 | 公共固件（面板、登录、签名更新、蓝牙设置）由此复制 |""",
      "architecture": r"""<p align="center">
  <img src="images/architecture.svg" alt="ARMOR-NODE-HMI 的架构：谁调用它、它包含什么、它依赖什么" width="100%">
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
| 胁迫报警显示在屏幕上 | 绝不显示（有主机测试检查）；面板所知的服务器信息一旦过时就会标记为过期 |
| 冒充服务器的对象 | 服务器证书被固定（`server_pin`），同时用于请求和实时通道的 WebSocket；面板用管理员创建的专属用户登录，角色为 `panel`（不能使用 Studio） |
| 不用 PIN 撤防 | 布防和撤防先询问，并在屏幕上接收 PIN（`pin_entry`）；服务器会再次检查 |
| 语音音频被发送到意外的地方 | 默认关闭（`voice.enabled` 为 false）；音频只发送到设置中地址对应的服务（地址会被校验，更换主机会清除令牌）；面板不会自行执行任何命令，也没有唤醒词：按住说话 |
| 没人听见的警笛 | 只有一个优先级队列（警笛、报警、语音、确认、通知）；只要有严重报警未确认，警笛就会重复（`audio.siren_repeat_s` 30，范围 10 到 600，0 = 不重复；`audio.siren_max_repeats` 10），严重音量不会低于 `audio.critical_min_volume`（40 %） |

固件只构建过一次，从未在电路板上运行：屏幕、触摸、声音和与服务器的连接都是依据 Waveshare 的示例编写的，等待首次通电。报告漏洞请阅读 [SECURITY.md](SECURITY.md)。""",
      "interfaces": r"""| 部分 | 作用 |
|---|---|
| ARMOR-SERVER | 仅在实时通道中断时每 `server.poll_s`（3 秒，范围 1 到 60）调用一次 `GET /api/v1/panel/summary`；`server.live_events` 为 true（默认）时使用 WebSocket `/api/v1/panel/events`：模式、报警、节点或能源变化时会收到概要；面板自己的用户角色为 `panel` |
| 语音 | 一轮对话的音频经服务器发送到 ARMOR-VOICE-AI（`/api/v1/voice/turn`，可选 multipart 正文）；`core/voice_session.hpp` 是状态机（步骤顺序、时间限制、触摸的作用）；见 [docs/VOICE.md](docs/VOICE.md) |
| 硬件 | Waveshare ESP32-S3-Touch-LCD-7C-BOX：7 英寸 RGB 屏幕 800x480、GT911 触摸、四个麦克风、一个扬声器、RTC PCF85063A（`time.rtc_enabled`，默认 true）、32 MB 闪存和 16 MB PSRAM；有测试证明没有任何功能共用 GPIO |""",
      "configuration": r"""| 变量 | 默认值 | 作用 |
|---|---|---|
| `server.poll_s`, `server.live_events` | 3 (1-60), true | 概要的轮询周期以及通过 WebSocket 的实时通道 |
| `display.sleep_s` | 300 (0-3600) | 屏幕休眠前的秒数（0 = 从不）；亮度和夜间亮度也是设置项 |
| `audio.critical_min_volume`, `audio.siren_repeat_s`, `audio.siren_max_repeats` | 40 (0-100), 30, 10 | 严重提示音的最低音量、警笛重复周期（0 或 10 到 600 秒）及其最大重复次数 |
| `audio.tone_by_source` | 按严重程度 | 每个告警来源(设备、太阳能、电气、网络、中心、其他)的声音:按其严重程度、作为通知、作为告警、作为警笛或静音;所选声音即使严重程度低于最低值也会响起 |
| `voice.enabled`, `voice.url`, `voice.token` | false, "", - | 语音服务：默认关闭；地址最长 160 个字符并会被校验（否则为 `required` 或 `invalid`）；更换主机时令牌会被清除 |
| `CONFIG_ARMOR_NODE_ID`, `_SETUP_CODE`, `_FLEET_SECRET`, `_MQTT_*`, `_HEARTBEAT_S`, `_BLE_SETUP_MINUTES`, `_BOOT_FACTORY_RESET` | - | 所有节点共有的设置：名称（为空则为 `armor-` 加 MAC 的最后字节）、设置码（为空则随机）、机群密钥（16 个字符以上，绝不放入仓库）、最初的代理设置、心跳（2 到 300 秒）、蓝牙设置的分钟数（1 到 120）以及用 BOOT 重置（前 30 秒内按 8 秒） |""",
      "quickstart": r"""**要求:** 用于主机测试的 C++17 编译器；用于构建镜像的 ESP-IDF 5.5.5 容器；Waveshare ESP32-S3-Touch-LCD-7C-BOX。

```bash
cmake -S tests -B build/host && cmake --build build/host && ctest --test-dir build/host   # host tests, -Werror
node tools/panel_mock.mjs --user admin:adminpass123   # the panel of the node without a board
tools/build_node.sh                                   # the image in the ESP-IDF container
```

See the [firmware guide](docs/NODE_FIRMWARE.md) and the [Bluetooth channel](docs/BLE_PROVISIONING.md).

参见[设计](docs/DESIGN.md)、[开发板](docs/HARDWARE.md)、[语音助手](docs/VOICE.md)、[固件指南](docs/NODE_FIRMWARE.md)和[字体](docs/FONTS.md)。

要在 GitHub Actions 中手动编译固件，参见[在 GitHub Actions 中编译](docs/FIRMWARE_BUILD_ACTIONS.md)。""",
      "testing": r"""```bash
cmake -S tests -B build/host && cmake --build build/host && ctest --test-dir build/host
python -I tools/armor_ci_validate.py
```

`ctest` 运行 18 个主机测试程序和 6 个 Python 检查；主机程序统计的检查共 93081 项，使用 `-Werror` 构建。

Python 检查：八种语言的面板文字、任务、保存路径、受锁保护的蓝牙会话以及面板调用的路由（部分节点还包括 HTTP 状态码或字体字形）

主机测试需要任意 C++17 编译器（Linux、WSL、MSYS2）；网页面板还会在真实浏览器中对着模拟节点（`tools/panel_mock.mjs`、`tools/panel_browser_test.mjs`）进行验证。

`check_font_glyphs.py` 检查字体包含八种语言的所有字形（98 行）；`test_clock` 只输出 `ok`。""",
      "build": "`tools/build_node.sh` 在 ESP-IDF 5.5.5 容器中构建镜像，发布版带有镜像、其 SHA-256 和 Ed25519 签名，每块电路板一份；镜像第一次通过 USB-C 写入，之后从面板更新。",
      "troubleshooting": r"""| 现象 | 原因 | 处理 |
|---|---|---|
| 忘记了密码，或节点不再加入网络 | 处于设置状态且 90 秒后仍无地址的节点会开启自己的 Wi-Fi `ARMOR-SETUP-xxxxxx`（打开 `http://192.168.4.1/`） | 要重新开始，请在上电后 30 秒内按住 BOOT 8 秒（会清除设置和用户），或使用面板中的*恢复出厂设置* |
| 来自 GitHub 的更新被拒绝 | 发布版缺少校验和或签名，或二者不匹配（`e_no_checksum`、`e_no_signature`、`e_checksum_mismatch`、`e_bad_signature`），没有适用于此电路板的镜像（`e_no_asset_for_board`），或属于另一个项目（`e_wrong_firmware`） | 节点未发生任何变化；请重试，或由管理员手动上传文件 |
| 语音无法启动 | `voice.enabled` 已关闭，或 `voice.url` 为 `required` 或 `invalid` | 在面板中开启并填写有效地址；更换主机会清除令牌 |
| 页脚先显示发送中，然后显示已确认或原因 | 命令正在发送、已确认数秒，或被拒绝并保留原因 | 阅读原因；决定权在服务器而非面板 |""",
      "structure": r"""<p align="center">
  <img src="images/repository-structure.svg" alt="ARMOR-NODE-HMI 的仓库结构" width="100%">
</p>

<details>
<summary>目录树的文本版</summary>

```text
ARMOR-NODE-HMI/
├── main/                                固件：一个 ESP-IDF 组件
├── core/                                不依赖 ESP-IDF 的逻辑，在计算机上测试
├── panel/                               嵌入固件的网页面板
├── tests/                               主机测试和 Python 检查
├── docs/                                9 份指南：设计、语音、字体、硬件
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
├── sdkconfig.board.lcd7box              某块电路板的设置
├── secrets/                             节点文件示例（真实文件不纳入版本管理）
├── dependencies.lock                    ESP-IDF 组件的固定版本
├── build-test.sh build-test.bat         通过共享工作流运行测试
└── .gitattributes .gitignore            Git 设置
```

</details>""",
      "roadmap": r"""**目前已知的限制**

* 固件构建过一次（ESP-IDF 5.5.5），但该构建不在持续集成的检查范围内，也从未在板子上运行过。
* 与服务器和语音服务 ARMOR-VOICE-AI 的交互已对照模拟测试；采用按键说话，没有唤醒词。
* 网页已在真实浏览器中对模拟运行过；屏幕、触摸和声音依据 Waveshare 的示例编写，等待首次上电。
* 固件尚未在板子上运行过：还没有在真实设备上运行过。
* 设置码、登录限制、蓝牙 PIN、胁迫处理和签名更新已在主机上测试；没有经过独立审查。
* 哈希和签名检查在主机上通过；空中更新从未在板子上运行过。
* 消息已对照 ARMOR-COMMON 的共享模式验证；与服务器和语音服务的连接尚未从板子上试过。

**下一步**

* 在电路板上完成首次完整构建和首次通电，然后是 Jetson 上的语音服务、唤醒词和屏幕上的摄像头视图。""",
    },
  },
  "pt": {
    "tagline": "O painel tátil da casa: um ecrã de 7 polegadas na parede que mostra o estado do sistema, arma e desarma e reconhece alarmes, com um microfone e um altifalante para o assistente de voz que virá (um nó da família na ESP32-S3-Touch-LCD-7C-BOX, com a sua própria página web para as definições)",
    "honest": "O que não depende da placa é real e está testado num computador (as definições, o que o painel sabe do servidor e quando está desatualizado, o alarme de coação que nunca é mostrado, a conversa de voz e a resposta longa do serviço de voz, os pinos da placa, os textos do ecrã em oito idiomas e os glifos das suas fontes, as verificações de versão e assinatura: 30,783 verificações em 18 programas de teste), e a página web também (executada contra um substituto num navegador real). **O firmware foi compilado uma vez (ESP-IDF 5.5.5, não verificado pela integração contínua) e nunca correu numa placa:** o ecrã, o toque, o som e a ligação ao servidor estão escritos a partir dos exemplos da Waveshare para esta família de placas e precisam do primeiro arranque. O serviço de voz (ARMOR-VOICE-AI) responde aos pedidos deste painel; não há palavra de ativação: toca-se para falar.",
    "glance": [
      [
        "Função",
        "Painel tátil de parede para o ARMOR-SERVER (família: Clients, pai: ARMOR-SERVER)",
      ],
      [
        "Tecnologia",
        "C++17, ESP-IDF 5.5.5, LVGL, ESP32-S3",
      ],
      [
        "Testes",
        "93081 verificações em 18 programas de anfitrião e 6 em Python (`ctest`)",
      ],
      [
        "Placa",
        "Waveshare ESP32-S3-Touch-LCD-7C-BOX (800x480, GT911)",
      ],
      [
        "Funciona em",
        "Uma Waveshare ESP32-S3-Touch-LCD-7C-BOX; testes de anfitrião em qualquer computador",
      ],
      [
        "Em hardware real",
        "Nenhum ainda: o firmware compila (ESP-IDF 5.5.5, não verificado pela CI) mas não correu na placa",
      ],
      [
        "Licença",
        "GPL-3.0-or-later",
      ],
    ],
    "status": {
      "software": "O firmware foi compilado uma vez (ESP-IDF 5.5.5), mas a compilação não é verificada pela integração contínua e nunca funcionou numa placa.",
      "tests": "Passam 93.081 verificações em 18 programas de anfitrião (`ctest`): as definições, o que o painel sabe do servidor e quando isso está desatualizado, o alarme de coação que nunca se mostra, a troca de voz, os pinos, os textos do ecrã em oito idiomas e os glifos dos seus tipos de letra.",
      "protocols": "A troca com o servidor e com o serviço de voz ARMOR-VOICE-AI é testada contra simulações; é premir para falar, sem palavra de ativação.",
      "ui": "A página web correu contra uma simulação num navegador real; o ecrã, o toque e o som foram escritos a partir dos exemplos da Waveshare e esperam a primeira ligação.",
      "hardware": "O firmware não funcionou na placa: nada funcionou ainda em equipamentos reais.",
      "security": "O código de configuração, o limite de acessos, o PIN Bluetooth, o tratamento da coação e as atualizações assinadas estão testados no anfitrião; não houve revisão independente.",
      "updates": "As verificações de hash e de assinatura passam no anfitrião; uma atualização pelo ar nunca foi executada numa placa.",
      "integration": "As mensagens são validadas contra os esquemas partilhados do ARMOR-COMMON; a ligação ao servidor e ao serviço de voz não foi experimentada a partir de uma placa.",
      "docs": "Oito idiomas, o guia do firmware, as notas de cablagem e o registo de alterações estão atualizados.",
    },
    "docs": [
      "[Desenho](docs/DESIGN.md) e [hardware](docs/HARDWARE.md): o que o painel mostra e a placa",
      "[Voz](docs/VOICE.md) e [tipos de letra](docs/FONTS.md)",
      "[Firmware do nó](docs/NODE_FIRMWARE.md) e [ações de compilação](docs/FIRMWARE_BUILD_ACTIONS.md)",
      "[Testes de bancada](docs/BENCH_TESTS.md), [código de configuração](docs/SETUP_CODE.md) e [provisionamento Bluetooth](docs/BLE_PROVISIONING.md)",
    ],
    "contributing_first": "Antes de um pull request, execute `ctest --test-dir build/host` and `python -I tools/armor_ci_validate.py`: tem de passar. Consulte [CONTRIBUTING.md](CONTRIBUTING.md) e o [código de conduta](CODE_OF_CONDUCT.md).",
    "languages_extra": "",
    "body": {
      "overview": r"""* **Um cliente do ARMOR-SERVER, como a aplicação Android:** inicia sessão com um utilizador que um administrador criou para ele, pede `GET /api/v1/panel/summary` (algumas centenas de bytes: o modo, os nós ligados e os alarmes que precisam de uma pessoa) a cada poucos segundos e, quando a pessoa toca no botão e confirma, arma, desarma ou reconhece. Se o servidor deixa de responder, o ecrã diz que o que mostra é antigo e o botão fica desativado. Ouve o canal em direto do servidor (um WebSocket) para que uma alteração se veja de imediato, e pergunta como antes quando o canal falta, se cala ou está desligado.
* **O ecrã (800x480, LVGL):** o modo na cor do pior alarme que ninguém viu, um grande botão de armar/desarmar com uma pergunta primeiro, os nós ligados, os alarmes (os não vistos primeiro), uma noite que o escurece, um repouso após algum tempo sem toques, um som e um despertar quando chega um alarme novo, e oito idiomas com acentos, japonês e chinês desenhados com tipos de letra gerados exatamente para os carateres usados.
* **Um nó como os outros:** o mesmo armazenamento de definições, Wi-Fi, página web em oito idiomas, configuração por Bluetooth a partir do telemóvel, atualização de firmware com retrocesso e HTTPS como o ARMOR-NODE-RADAR, o ARMOR-NODE-SOLAR e o ARMOR-NODE-ELECTRICAL (partilham `ARMOR-COMMON/firmware_base`), mais páginas para o servidor, o ecrã, o som e a voz; diz ao Studio que existe por MQTT para que o Studio o liste com a sua página.
* **O assistente de voz, premir para falar:** um toque abre o microfone, o áudio vai só para o serviço de fala cujo endereço está nas definições (desativado por omissão), a resposta mostra-se e diz-se em voz alta; a ordem dos passos, os limites de tempo e o que faz um toque são uma máquina de estados testada, e o painel não executa nenhum comando por si só ([o contrato](docs/VOICE.md)). A gravação segue como bytes num pedido binário e a resposta falada volta como bytes; a um servidor que não a aceite envia-se o pedido antigo.
* **A placa:** Waveshare ESP32-S3-Touch-LCD-7C-BOX (32 MB de flash, 16 MB de PSRAM, um ecrã RGB de 7 polegadas com toque GT911, quatro microfones, um altifalante); os pinos vêm dos exemplos da Waveshare e um teste prova que nenhumas duas funções partilham um GPIO ([a placa](docs/HARDWARE.md)).
* **Atualizações pelo ar assinadas:** o nó só instala do GitHub uma imagem cujo SHA-256 coincide e que leva uma assinatura Ed25519 válida do responsável (a chave pública está no firmware, a privada nunca sai do responsável); um ficheiro carregado à mão por um administrador no painel continua a ser aceite. As páginas e mensagens do painel estão em oito idiomas.
* **Emparelhamento Bluetooth com PIN:** o PIN de seis dígitos deriva do código de configuração, é impresso na consola USB e mostrado a um administrador no painel; o telemóvel tem de o introduzir antes de poder escrever as definições do nó.
* **Ainda não:** uma primeira compilação e arranque do firmware, uma palavra de ativação, o serviço de fala no Jetson, e uma vista das câmaras no ecrã.
* **Só a casa pode usar o painel:** o painel responde por omissão à rede privada (ou às redes que o dono indicar, como uma VPN), recusa uma lista que deixaria de fora quem a guarda, conta as palavras-passe erradas por pessoa e por endereço e funciona atrás do proxy do servidor para ser alcançado de fora de casa sem publicar o nó.
* **Diz o que se passa:** o ecrã conhece o texto, em oito idiomas, de cada código de alarme que o servidor levanta (rede, solar, elétrica, zonas de alarme...) e avisa o servidor de que é um painel de parede, por isso é listado como tal e não conta como radar.
* **Ligação cifrada opcional ao broker (TLS):** desativada por predefinição, por isso o nó fala MQTT sem cifra como antes. Um interruptor e uma caixa para o certificado da autoridade própria da instalação (PEM, no máximo 2 KB) na página Broker fazem-no ligar-se com `mqtts://`, confiar só nessa autoridade e verificar que o certificado do broker foi feito para o endereço alcançado; o que não for um único certificado PEM é recusado. Coberto por testes no computador; o handshake ainda não foi executado numa placa.
* **Relatório de saúde:** cerca de uma vez por minuto o nó publica há quanto tempo está ligado e porque reiniciou da última vez, a memória livre, a ligação e o sinal Wi-Fi, quantas vezes se ligou ao broker e o último erro que registou (`armor/health/<nó>`, o contrato `node_health` do ARMOR-COMMON). O código que o constrói é partilhado por todos os nós e testado num computador; nunca correu numa placa.
* **Controlo a partir do servidor:** o Studio pode reiniciar o nó de forma limpa, pô-lo em pausa até uma hora (retoma sozinho), pôr o seu trabalho em espera (sem fim, mantida nos reinícios, o nó continua ligado e a responder), fazê-lo mostrar-se, pedir um instantâneo de diagnóstico e marcá-lo em manutenção (`armor/control/<nó>/...`, o contrato `node_control` do ARMOR-COMMON). Cada ordem tem dois passos com um token de uso único que pertence a essa operação, só o servidor as pode escrever no broker, e não existe reposição de fábrica, apagamento nem sono profundo. Enquanto o painel está em pausa ou em espera, o ecrã mostra um ecrã próprio que o diz e não aceita toques; quando lhe pedem que se identifique, pisca uma barra no topo (nunca um som). O código é partilhado por todos os nós e testado num computador; ainda não correu numa placa.
* **Diagnóstico sem cabo:** depois de um arranque que não foi limpo (um bloqueio, um watchdog, uma quebra de alimentação, uma reserva de memória falhada), o relatório de saúde diz o motivo durante dez minutos; uma falha deixa o seu core dump para ver, descarregar ou apagar a partir do painel; as definições guardadas são copiadas antes de cada instalação de firmware e recuperadas se uma atualização as danificar; e um administrador pode pedir ao nó, através do servidor, um pacote de diagnóstico ou o seu registo com um token de utilização única.
* **Uma sirene que se repete e sons por ordem:** todo o som passa por uma fila com prioridades (sirene, alarme, voz, confirmação, aviso); a sirene repete-se enquanto houver alarmes críticos por reconhecer (`audio.siren_repeat_s` 30, `audio.siren_max_repeats` 10) e os alarmes mantêm um volume mínimo (`audio.critical_min_volume` 40); a voz cede perante um alarme.
* **Um relógio com bateria:** o chip PCF85063A da placa dá a hora no arranque quando o nó ainda não tem hora real e o chip é de confiança, e é corrigido sempre que a hora é sincronizada ou acertada (`time.rtc_enabled`, ativado por predefinição).
* **O estado de uma ordem, no ecrã:** o rodapé diz que a ordem está a ser enviada enquanto vai a caminho e que foi confirmada durante alguns segundos quando passou; uma recusa mantém aí o seu motivo, como antes.
* **Selagem opcional dos segredos guardados:** desativada por predefinição (`security.seal_secrets`, ou `nodes.nvs_encryption` do servidor). Ativada, as palavras-passe, os tokens, as chaves, os PIN e os hashes de palavras-passe que o nó guarda ficam selados com ChaCha20-Poly1305 e tudo o resto continua legível; ativá-la ou desativá-la reescreve-os sem perder nada, mesmo que o nó pare a meio. Não se queima nenhum eFuse nem se cifra a flash: a chave está numa partição do mesmo chip, pelo que **não** protege contra quem tenha a placa, e um nó instalado antes dessa partição mantém os segredos como estavam até ser gravado com a nova tabela de partições.""",
      "role": r"""O ARMOR-NODE-HMI é o painel de parede: um cliente do [ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER), como a aplicação Android, com um ecrã de 7 polegadas, microfone e altifalante. Mostra o modo, os nós ligados e os alarmes que precisam de uma pessoa, arma e desarma (com o PIN) e reconhece alarmes. É onde viverá o assistente de voz ([ARMOR-VOICE-AI](https://github.com/JuanenRac/ARMOR-VOICE-AI)) quando existir o seu serviço de voz e, como todos os nós, é configurado e atualizado a partir do [ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO).

| Nome | Como | Para quê |
|---|---|---|
| ARMOR-SERVER | HTTPS `GET /api/v1/panel/summary`, WebSocket `/api/v1/panel/events` | O resumo da casa (modos, alarmes, nós, energia) e as suas mudanças; o servidor decide o que faz uma ordem |
| ARMOR-VOICE-AI | através do servidor | O áudio de um turno vai para o serviço de voz; a resposta é mostrada e dita |
| ARMOR-STUDIO | menu Painel tátil | Mostra a saúde do painel e abre o seu painel web |
| ARMOR-COMMON | base de firmware | O firmware comum (painel, acessos, atualização assinada, configuração Bluetooth) é copiado dele |""",
      "architecture": r"""<p align="center">
  <img src="images/architecture.svg" alt="Arquitetura de ARMOR-NODE-HMI: quem o chama, o que contém e de que depende" width="100%">
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
| O alarme de coação mostrado no ecrã | Nunca é mostrado (um teste de anfitrião verifica-o); e o que o painel sabe do servidor é marcado como caducado quando é antigo |
| Um servidor que não é o servidor | O certificado do servidor está fixado (`server_pin`), para os pedidos e para o WebSocket do canal em direto; o painel entra com um utilizador próprio, criado por um administrador, com o papel `panel` (não pode usar o Studio) |
| Desarmar sem PIN | Armar e desarmar perguntam primeiro e recebem o PIN no ecrã (`pin_entry`); o servidor volta a verificar |
| Áudio de voz para um sítio inesperado | Desligada por omissão (`voice.enabled` falso); o áudio só vai para o serviço cujo endereço está nas definições (o endereço é validado e mudar de anfitrião apaga o token); o painel não executa nenhuma ordem por si e não há palavra de ativação: é premir para falar |
| Uma sirene que ninguém ouve | Uma única fila de prioridade (sirene, alarme, voz, confirmação, aviso); a sirene repete-se enquanto houver alarmes críticos por reconhecer (`audio.siren_repeat_s` 30, de 10 a 600, 0 = sem repetições; `audio.siren_max_repeats` 10) e o volume crítico nunca desce de `audio.critical_min_volume` (40 %) |

O firmware foi compilado uma vez e nunca correu numa placa: o ecrã, o tátil, o som e a ligação ao servidor estão escritos a partir dos exemplos da Waveshare, à espera do primeiro arranque. Leia [SECURITY.md](SECURITY.md) para comunicar uma vulnerabilidade.""",
      "interfaces": r"""| Parte | O que define |
|---|---|
| ARMOR-SERVER | `GET /api/v1/panel/summary` a cada `server.poll_s` (3 s, de 1 a 60) só enquanto o canal em direto está em baixo, e o WebSocket `/api/v1/panel/events` enquanto `server.live_events` for verdadeiro (predefinição): o resumo chega quando mudam o modo, os alarmes, os nós ou a energia; o utilizador próprio do painel tem o papel `panel` |
| Voz | O áudio de um turno vai para o ARMOR-VOICE-AI através do servidor (`/api/v1/voice/turn`, com corpo multipart opcional); `core/voice_session.hpp` é a máquina de estados (ordem dos passos, limites de tempo, o que faz um toque); veja [docs/VOICE.md](docs/VOICE.md) |
| Hardware | Waveshare ESP32-S3-Touch-LCD-7C-BOX: ecrã RGB de 7 polegadas 800x480, tátil GT911, quatro microfones, um altifalante, RTC PCF85063A (`time.rtc_enabled`, verdadeiro por omissão), 32 MB de flash e 16 MB de PSRAM; um teste prova que nenhuma função partilha um GPIO |""",
      "configuration": r"""| Variável | Predefinição | O que define |
|---|---|---|
| `server.poll_s`, `server.live_events` | 3 (1-60), true | O período de consulta do resumo e o canal em direto por WebSocket |
| `display.sleep_s` | 300 (0-3600) | Segundos até o ecrã adormecer (0 = nunca); o brilho e o brilho noturno também são definições |
| `audio.critical_min_volume`, `audio.siren_repeat_s`, `audio.siren_max_repeats` | 40 (0-100), 30, 10 | O volume mínimo de um som crítico, o período de repetição da sirene (0 ou de 10 a 600 s) e as suas repetições máximas |
| `audio.tone_by_source` | conforme a gravidade | O som de cada origem de alarme (dispositivo, solar, elétrico, rede, central, outro): o que a sua gravidade indica, como aviso, como alarme, como sirene ou sem som; um som escolhido toca mesmo abaixo da gravidade mínima |
| `voice.enabled`, `voice.url`, `voice.token` | false, "", - | O serviço de voz: desligado por omissão; o endereço tem no máximo 160 caracteres e é validado (senão `required` ou `invalid`); o token apaga-se quando o anfitrião muda |
| `CONFIG_ARMOR_NODE_ID`, `_SETUP_CODE`, `_FLEET_SECRET`, `_MQTT_*`, `_HEARTBEAT_S`, `_BLE_SETUP_MINUTES`, `_BOOT_FACTORY_RESET` | - | As definições que todos os nós partilham: o nome (vazio dá `armor-` e os últimos bytes do MAC), o código de configuração (vazio: aleatório), o segredo de frota (16+ caracteres, nunca no repositório), as primeiras definições do broker, o batimento (de 2 a 300 s), os minutos de configuração Bluetooth (de 1 a 120) e a reposição com BOOT (8 s nos primeiros 30 s) |""",
      "quickstart": r"""**Requisitos:** um compilador C++17 para os testes de anfitrião; o contentor ESP-IDF 5.5.5 para compilar a imagem; uma Waveshare ESP32-S3-Touch-LCD-7C-BOX.

```bash
cmake -S tests -B build/host && cmake --build build/host && ctest --test-dir build/host   # host tests, -Werror
node tools/panel_mock.mjs --user admin:adminpass123   # the panel of the node without a board
tools/build_node.sh                                   # the image in the ESP-IDF container
```

Veja o [guia do firmware](docs/NODE_FIRMWARE.md) e o [canal Bluetooth](docs/BLE_PROVISIONING.md).

Veja o [desenho](docs/DESIGN.md), a [placa](docs/HARDWARE.md), o [assistente de voz](docs/VOICE.md), o [guia do firmware](docs/NODE_FIRMWARE.md) e os [tipos de letra](docs/FONTS.md).

Para compilar o firmware à mão no GitHub Actions, veja [compilar no GitHub Actions](docs/FIRMWARE_BUILD_ACTIONS.md).""",
      "testing": r"""```bash
cmake -S tests -B build/host && cmake --build build/host && ctest --test-dir build/host
python -I tools/armor_ci_validate.py
```

18 programas de teste de anfitrião e 6 verificações Python correm com `ctest`; 93081 verificações contadas pelos programas de anfitrião, compiladas com `-Werror`.

Verificações Python: os textos do painel em oito línguas, as tarefas, os caminhos de gravação, a sessão Bluetooth sob o seu bloqueio e as rotas que o painel chama (e, em alguns nós, os códigos HTTP ou os glifos dos tipos de letra)

Os testes de anfitrião precisam de qualquer compilador C++17 (Linux, WSL, MSYS2); o painel web também é exercitado num navegador real contra um nó de substituição (`tools/panel_mock.mjs`, `tools/panel_browser_test.mjs`).

O `check_font_glyphs.py` verifica que os tipos de letra têm todos os glifos das oito línguas (98 linhas); o `test_clock` só imprime `ok`.""",
      "build": "`tools/build_node.sh` compila a imagem no contentor ESP-IDF 5.5.5 e a versão leva a imagem, o seu SHA-256 e a sua assinatura Ed25519, uma por placa; a imagem grava-se por USB-C da primeira vez e depois atualiza-se a partir do painel.",
      "troubleshooting": r"""| Vê | Porque | Faça |
|---|---|---|
| Perdeu a palavra-passe ou o nó já não se liga à rede | Um nó em configuração e sem endereço após 90 s abre o seu próprio Wi-Fi `ARMOR-SETUP-xxxxxx` (abra `http://192.168.4.1/`) | Para recomeçar mantenha BOOT 8 segundos nos primeiros 30 segundos após ligar (apaga definições e utilizadores), ou use *Reposição de fábrica* no painel |
| Uma atualização do GitHub é recusada | A versão não traz soma de verificação nem assinatura, não coincidem (`e_no_checksum`, `e_no_signature`, `e_checksum_mismatch`, `e_bad_signature`), não traz imagem para esta placa (`e_no_asset_for_board`) ou é de outro projeto (`e_wrong_firmware`) | O nó não mudou; tente de novo ou deixe um administrador enviar o ficheiro à mão |
| A voz não arranca | `voice.enabled` está desligado, ou `voice.url` é `required` ou `invalid` | Ligue-a no painel e dê um endereço válido; mudar de anfitrião apaga o token |
| O rodapé diz a enviar, depois confirmada ou o motivo | Uma ordem vai a caminho, foi confirmada durante alguns segundos, ou foi recusada e guarda o seu motivo | Leia o motivo; decide o servidor, não o painel |""",
      "structure": r"""<p align="center">
  <img src="images/repository-structure.svg" alt="Estrutura do repositório de ARMOR-NODE-HMI" width="100%">
</p>

<details>
<summary>Versão em texto da árvore</summary>

```text
ARMOR-NODE-HMI/
├── main/                                o firmware: um componente ESP-IDF
├── core/                                a lógica sem ESP-IDF, testada num computador
├── panel/                               o painel web embebido no firmware
├── tests/                               testes de anfitrião e verificações Python
├── docs/                                9 guias: desenho, voz, tipos de letra, hardware
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
├── sdkconfig.board.lcd7box              as definições de uma placa
├── secrets/                             exemplo do ficheiro do nó (os verdadeiros não são versionados)
├── dependencies.lock                    as versões fixadas dos componentes ESP-IDF
├── build-test.sh build-test.bat         executar os testes pelo fluxo partilhado
└── .gitattributes .gitignore            definições do Git
```

</details>""",
      "roadmap": r"""**Limites conhecidos hoje**

* O firmware foi compilado uma vez (ESP-IDF 5.5.5), mas a compilação não é verificada pela integração contínua e nunca funcionou numa placa.
* A troca com o servidor e com o serviço de voz ARMOR-VOICE-AI é testada contra simulações; é premir para falar, sem palavra de ativação.
* A página web correu contra uma simulação num navegador real; o ecrã, o toque e o som foram escritos a partir dos exemplos da Waveshare e esperam a primeira ligação.
* O firmware não funcionou na placa: nada funcionou ainda em equipamentos reais.
* O código de configuração, o limite de acessos, o PIN Bluetooth, o tratamento da coação e as atualizações assinadas estão testados no anfitrião; não houve revisão independente.
* As verificações de hash e de assinatura passam no anfitrião; uma atualização pelo ar nunca foi executada numa placa.
* As mensagens são validadas contra os esquemas partilhados do ARMOR-COMMON; a ligação ao servidor e ao serviço de voz não foi experimentada a partir de uma placa.

**A seguir**

* Fazer a primeira compilação completa e o primeiro arranque na placa, e depois o serviço de voz no Jetson, uma palavra de ativação e a vista de câmaras no ecrã.""",
    },
  },
}
