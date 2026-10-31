# The facts that do not depend on the language, and the words of every language, of ARMOR-ANDROID-CONTROL, in the universal README layout.
# Copyright (C) 2026 JuanenRac (Electro Hobby 3D). GPL-3.0-or-later.

FACTS = {
  "emoji": "📱",
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
      "Kotlin",
      "7f52ff",
    ],
    [
      "UI",
      "Jetpack%20Compose",
      "4285f4",
    ],
    [
      "Languages",
      "8",
      "00E5FF",
    ],
    [
      "Tests",
      "367%20passing",
      "2ea44f",
    ],
  ],
}

TEXT = {
  "en": {
    "tagline": "Mobile operator client for ARMOR-SERVER: alarms, cameras, radar, energy, the network and the set-up of the nodes, in eight languages",
    "honest": "The endpoint-safety, alarm-decision, alarm-watcher, translation and read-only-role rules are covered by 367 unit tests and the app builds (`gradlew testDebugUnitTest assembleDebug`). It runs on a real phone against the CM5 test bench: sign-in, the camera monitor, arming and alarms, the radar, the set-up of a node over Bluetooth and the updates from GitHub are in use. What is **not** proven yet: the solar, electrical and alarm-panel screens with real equipment (only a radar node exists), push through Firebase (it is in the app and needs a Firebase project of its own; it has not been tried on a phone yet) and the background alarm watch under the battery rules of every phone maker.",
    "glance": [
      [
        "Role",
        "Android operator client for ARMOR-SERVER (family: Clients, parent: ARMOR-SERVER)",
      ],
      [
        "Stack",
        "Kotlin / Jetpack Compose, Android 8.0+",
      ],
      [
        "Tests",
        "367 (`gradlew testDebugUnitTest`)",
      ],
      [
        "Languages",
        "8 (1345 phrases per language, every phrase checked in all tables)",
      ],
      [
        "Runs on",
        "An Android 8.0+ phone (minSdk 26)",
      ],
      [
        "On real hardware",
        "Used on a real phone against the CM5 test bench; the solar, electrical and alarm-panel screens wait for real nodes",
      ],
      [
        "License",
        "GPL-3.0-or-later",
      ],
    ],
    "status": {
      "software": "The app builds (`gradlew testDebugUnitTest assembleDebug`) and runs on a real phone against the CM5 test bench.",
      "tests": "367 unit tests pass (`gradlew testDebugUnitTest`): endpoint safety, alarm decision, alarm watcher, translations and the read-only role.",
      "ui": "Sign-in, the camera monitor, arming and alarms and the radar are in use on a real phone; the Bluetooth set-up of a node has not been confirmed against a real node, and the solar, electrical and alarm-panel screens have not met real equipment.",
      "hardware": "Used on a real phone against the CM5 test bench; the background alarm watch under the battery rules of every phone maker is not proven.",
      "security": "The endpoint-safety and read-only-role rules are covered by unit tests; there has been no independent review.",
      "updates": "The updates from GitHub are in use on the phone.",
      "integration": "Push through Firebase is in the app but needs a Firebase project of its own and has not been tried on a phone.",
      "docs": "Eight languages and the changelog are up to date.",
    },
    "docs": [
      "[Client boundary](docs/CLIENT_BOUNDARY.md): what the client does and never does",
      "[Push notifications](docs/PUSH_NOTIFICATIONS.md): the Firebase steps, in eight languages",
      "[Bench tests](docs/BENCH_TESTS.md): checks with a real phone",
    ],
    "contributing_first": "Before a pull request run `.\\gradlew.bat testDebugUnitTest` and `python -I tools/armor_ci_validate.py`: it must pass. See [CONTRIBUTING.md](CONTRIBUTING.md) and the [code of conduct](CODE_OF_CONDUCT.md).",
    "languages_extra": "",
    "body": {
      "overview": r"""* **Sign in with the server's own login:** IP, port, user and password; the password creates an HttpOnly session; it is stored on the phone only if you tick **Remember me** (off by default: user and password sealed with a Keystore key of their own, for that server only, forgotten the moment you untick it). A **viewer** role only looks: every button that changes something is off.
* **Lock with the phone:** the app asks for the fingerprint, the face or the PIN of the phone itself before arming, disarming, silencing a siren, unlocking and the other critical orders (on by default only when the phone has a fingerprint or a face), and, if you turn it on, to open the app. Your administrator can require it from Studio but never lower what you chose, a phone with no screen lock is never shut out, and the locked screen always offers signing in again with the password. Optionally (off by default, with a visible warning) the key that seals the saved session can be tied to unlocking the phone; then the alarm watch in the background waits for you to unlock the phone after a restart.
* **Camera monitor:** 1 to 16 tiles, a maximized view, live MJPEG that keeps the picture ratio, a bounded PTZ pad, snapshots and recordings, with a viewer and a delete confirmation for the recordings.
* **Arm and disarm,** after a **check before arming** (what is open, silent or down) and with the PIN to disarm; **alarms** to acknowledge, with a badge for those waiting; **devices** (smoke, gas, flood, door, window, motion, climate, plugs, lights, sirens, locks, shutters, gate and garage-door motors, water heaters) with their state and On / Off / Toggle.
* **Alarms that reach you:** a sound for every severity, an optional **spoken alarm**, notifications for a node reaching HIGH, a silent camera, a device alarm and (while armed) an offline node, and a **sounding alarm panel wakes the phone**; the background watch survives a reboot and backs off when the server is down.
* **Live radar, in 2D and 3D:** the Radar tab draws the site as designed in Studio and the people the radars see moving on it, refreshed every second and a half; drag, pinch and turn the 3D view.
* **Solar and electrical energy:** the sums (sun, consumption, batteries with their charge, whether the grid is present), every inverter and battery with the cells on demand, and the channels and alarms of the electrical nodes.
* **Alarm panels:** the state of every ARMOR-NODE-ALARM node, its zones and events, and arm / disarm commands when the server allows them.
* **Network:** the devices of the house's network, the internet's state and the **public address** with the provider and the place, as the network node reports them.
* **Set up a field node over Bluetooth** (from the login screen or *More > Set up a node*): finds the nodes that advertise `ARMOR-xxxxxx`, creates the administrator of a new one or signs in (with the node's PIN), searches for Wi-Fi networks and sets the node's name, a router's Wi-Fi or a fixed address and the broker; a **node finder** lists the ones already on the network.
* **The assistant:** written and spoken commands (a closed list, in eight languages, with a confirmation bound to you) to ask for the state of the house or to arm, disarm, silence and switch the lights.
* **Evidence library,** the perimeter and node state, a **history** of every alert, node, camera, device, alarm and mode change, the **weather map**, and the **services** and updates of the installation.
* **Eight languages** (English, Spanish, German, French, Italian, Japanese, Chinese and Portuguese), chosen in *More > Settings* or following the phone; every phrase is checked to be in the eight tables.
* **Careful with the password:** plain HTTP is allowed only to a private-LAN or loopback IPv4 *literal*; a host name that merely starts like a private address (`10.attacker.example`) or an address with a leading zero is refused. The look is made of icons: near-black surfaces, a cyan accent, amber for attention.
* **Security from the phone:** the second factor and its recovery codes, the open sessions, a check of how the server sees the phone, the new proof of identity for critical actions from outside, and, for an administrator, the VPN (devices with their configuration) and the dynamic DNS name.
* **The whole system on the status screen, and the way in from outside:** the status screen summarises the alarm panels, the services, the cameras that are recording and the security and remote access, each card opening its screen; and when the address typed is outside the house without https, the sign-in says why it cannot go on and a guide explains the two safe ways (VPN, or a public address with https).
* **Node health and arming modes:** a Node health screen in More (every node's uptime, why it restarted, memory, link and signal, broker connections, restarts, last error and the warnings the server raised) and, on the Alarm panels screen, a mode picker (Away, Home, Night and your own) that arms a panel in the chosen mode when its firmware knows the modes. Eight languages.
* **Connections in the history:** the History screen has a second list, read-only, with the devices and apps that connect to the server (Studio, this app, the panels of the nodes, the voice service), when each was last seen, its open sessions and its sign-ins and refusals; the app now says what it is to the server so it appears as itself. Addresses are shown to administrators only.
* **Battery maintenance (administrators):** the simple operations on a Pylontech battery - clock, counters and logs, restart, capacity, MOSFET test, fuse fault, outputs - in the same two steps as Studio (the server has the node read the battery, the screen shows exactly what will be done, then "Do it now" with the serial number typed again), with the result and what changed; limits, firmware and the expert console stay in Studio.
* **Control of the nodes (administrators):** More > Node control gives the same operations as Studio - restart, pause, resume, standby (work off, still connected), identify, diagnostics and maintenance on or off - to one node or to all of them, asking for the node's name (or the word RESTART, PAUSE or STANDBY for all) typed again and for the fresh proof of identity, showing how far each node went, and warning that an alarm panel or a radar paused or on standby leaves the house unprotected. There is no factory reset, no erase and no deep sleep.
* **An alarm window in the open app:** while an alarm waits for a person, a banner over every screen but the alarms pulses (red and fast for a critical one, amber for the rest, still when the phone has its animations off), says which alarm is the worst and how many wait, and lets the app be used under it; it can open the alarms, confirm from the banner or be closed until another alarm arrives.
* **From outside the house:** two addresses (the private one on the home Wi-Fi, the one for away on mobile data or the VPN) chosen by where the phone is, with the other tried if one is silent and a message that says what fails; the key of the installation's certificate is remembered the first time (or paired from the text of Studio's QR) and a different one is refused, plain http is refused for a host that was reached over https; a node's panel can be opened through the server; alarms can arrive as push messages with data only, announced once whether they come by push or by the watch; the open app and the watch share one reading of the server; the camera streams stop out of sight and come back with growing waits.
* **Notices you choose, with sounds and a voice of your own:** in the settings, silence every notice, show them without sound or vibration (and without saying them aloud), and switch off by severity (high, low) or by kind (radar alerts, cameras that do not answer, nodes offline or silent, and the alarms of devices, solar, electrical, network and alarm panels); a critical alarm always notifies unless every notice is silenced. A sound for each severity and each kind of notice, from the sounds of the phone or a file of your own (under 3 MB), each with a play button; and the voice that says the alarms (woman, man or any; child, adult or senior; plain, action hero or dark lord; speed; whether low-severity notices are said too) with a test button.
* **A banner that takes you to the right screen, and a quieter watch:** the banner of an alarm opens the screen that handles it (cameras, devices, inverters or batteries, the electrical screen, the network or the alarm panels); the phone tells the server its language when it registers for push so the notice is written in it, and a new Firebase token reaches the server at once from the background. A camera with two lenses in one stream is two windows of the camera list. While the push alerts work the background watch asks the server every 120 s instead of every 10 (*Settings > Watch with push alerts*: 10, 60, 120, 300 or 600 s).""",
      "role": r"""ARMOR-ANDROID-CONTROL is the phone's window on the same [ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER) that [ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) uses: it reads and orders through it and nothing else. It is where the alarms follow you (a sounding alarm panel wakes the phone), where you ask the assistant by voice, and the tool to set up a new node over Bluetooth in the field, standing next to it.

| Name | How | What for |
|---|---|---|
| ARMOR-SERVER | HTTP `/api/v1` (55 paths), MJPEG | Everything the app reads and orders |
| Field nodes | Bluetooth (`ARMOR-xxxxxx`) | Sets up a new node standing next to it |
| GitHub | HTTPS | Checks and downloads the signed update of the app itself |
| Open-Meteo | HTTPS | The public forecast, air quality and place search of the weather map |""",
      "architecture": r"""<p align="center">
  <img src="images/architecture.svg" alt="ARMOR-ANDROID-CONTROL architecture: who calls it, what it holds and what it depends on" width="100%">
</p>""",
      "security": r"""| Threat | Defence |
|---|---|
| A password kept on the phone | Only with *Remember me* (off by default): user and password sealed with a Keystore key of their own, for that server only, forgotten the moment you untick it; no backup (`allowBackup=false`) |
| Plain HTTP towards the internet | Allowed only to a private-LAN or loopback IPv4 *literal*; a host like `10.attacker.example` or an address with a leading zero (`010.0.0.1` reads as octal) is refused; plain http is refused for a host that was reached over https |
| A man in the middle over https | Trust is the system's authorities plus those you installed on the phone; the key of the installation's certificate is remembered the first time (or paired from the text of Studio's QR) and a different one is refused |
| A critical order with the phone in other hands | The fingerprint, the face or the PIN of the phone before arming, disarming, silencing a siren, unlocking and the other critical orders (on by default only when the phone has a fingerprint or a face); the administrator can require it from Studio but never lower what you chose; a phone with no screen lock is never shut out |
| A viewer changes something | The *viewer* role sees everything but every button that changes something is off (role tests) |
| A wrong disarm PIN | The PIN goes to the server only when disarming; `wrong_pin`, `pin_locked`, `pin_not_set` and `elevation_required` are translated into plain words |
| A fake update of the app | The SHA-256 of the signing certificates (history) of the installed app and of the candidate are compared before Android's installer is called; if they share none, it is said plainly |
| An alarm the phone does not see | A foreground service (`AlarmWatcherService`) polls every 10 s, waits 15 s for the phone to unlock, backs off up to 60 s, says *unreachable* after 6 failures, survives a reboot; an alarm older than 15 minutes is not announced |
| A camera password on the phone | The cameras are seen through the server's stream: the app has no camera password and no RTSP address |

### Permissions

`INTERNET`, `ACCESS_NETWORK_STATE`: the server. `USE_BIOMETRIC`: the lock of the phone. `POST_NOTIFICATIONS`: alarms. `FOREGROUND_SERVICE` (+ `DATA_SYNC`, `SPECIAL_USE`) and `RECEIVE_BOOT_COMPLETED`: the alarm watch. `REQUEST_INSTALL_PACKAGES`: the update of the app. `BLUETOOTH_SCAN`, `BLUETOOTH_CONNECT`: the set-up of a node; `BLUETOOTH`, `BLUETOOTH_ADMIN` and `ACCESS_FINE_LOCATION` only up to Android 11 (`maxSdkVersion=30`), for the Bluetooth scan.

No independent security review. Read [docs/CLIENT_BOUNDARY.md](docs/CLIENT_BOUNDARY.md) and [SECURITY.md](SECURITY.md).""",
      "interfaces": r"""| Part | What it sets |
|---|---|
| ARMOR-SERVER | 55 distinct paths of `/api/v1` in `network/ArmorApiClient.kt` (the interface is `network/ArmorApi.kt`); the radar is read every 1.5 s; the cameras by MJPEG through the server |
| Two addresses | The private one on the home Wi-Fi and the one for away (mobile data or the VPN), chosen by where the phone is; the other is tried if one is silent and the message says what fails |
| Bluetooth | Finds nodes that advertise `ARMOR-xxxxxx`, creates the administrator of a new one or signs in with the node's PIN, searches Wi-Fi networks and sets the name, the Wi-Fi or a fixed address and the broker; the protocol is `model/NodeBle.kt`; a node finder lists the ones already on the network |
| Voice | `POST /api/v1/voice/command`: a closed list of commands in eight languages, with a confirmation bound to you (`model/Voice.kt`, `VoiceScreens.kt`) |
| Push | `PushService`: alarms as messages with data only, announced once whether they come by push or by the watch; the Firebase steps are in [docs/PUSH_NOTIFICATIONS.md](docs/PUSH_NOTIFICATIONS.md) (eight languages) |""",
      "configuration": r"""| Name | Value | What it sets |
|---|---|---|
| `compileSdk` / `targetSdk` / `minSdk` | 37 / 37 / 26 | Android 8.0 or later on the phone |
| `versionName` | = `armor.project.json` | The build fails when the manifest and the version differ |
| JDK / Android SDK | 17+ / 37 | To build the app and run the tests |

In the app (not in files): the language (the eight or following the phone), the two addresses, *Remember me*, the lock of the phone, the spoken alarm and the notifications, in *More > Settings*. Limits in the code: the watch polls every 10 s, backs off to 60 s and ignores alarms older than 15 minutes.""",
      "quickstart": r"""**Requirements:** JDK 17+, the Android SDK (compile SDK 37), an Android 8.0+ phone (minSdk 26).

```powershell
.\gradlew.bat testDebugUnitTest assembleDebug   # 367 tests, then the debug APK
adb install -r app\build\outputs\apk\debug\app-debug.apk
```

Releases are published on GitHub, from where the app itself checks for updates; the APK is signed with the maintainer's own release key, kept outside the repository, and the app compares the signing certificate of a download with its own before it hands the file to Android's installer. See the [client boundary](docs/CLIENT_BOUNDARY.md).""",
      "testing": r"""```powershell
.\gradlew.bat testDebugUnitTest
python -I tools/armor_ci_validate.py
```

| Part | Tests | What it covers |
|---|---|---|
| Alarms | 67 | `AlarmPolicy`, `AlarmBanner`, `AlarmPanels`, `AlarmCodes`, `AlarmRoute`, `NoticeFilter`, `PushEvents`, `DevicesAndAlarms` |
| Server link, parsing, fixtures | 59 | `ApiClient`, `ApiError`, `ServerFixtures`, `ParsersTolerant`, `SavePayload`, `JsonText`, `Preflight`, `SharedFeed`, `Connections` |
| View model and roles | 41 | `ArmorViewModel`, `Viewer`, `ArmProfiles`, `NodeCensus`, `NodeHealth` |
| Lock, session vault, keys | 38 | `DeviceLock`, `SessionVault`, `CredentialVault`, `KeyBinding`, `Security` |
| Endpoint safety, addresses, certificates | 32 | `ServerEndpoint`, `ServerAddresses`, `Literals`, `NodeAddress`, `CertificatePins`, `RemoteAccess` |
| Energy and network | 34 | `Solar`, `Battery`, `Electrical`, `Network` |
| Nodes over Bluetooth, node control | 26 | `NodeBle`, `NodeControl` |
| Updates from GitHub | 17 | `GitHubReleaseUpdaterHttpFailure`, `SignerCheck`, `SemanticVersion`, `ReleaseMetadataParser` |
| Radar and cameras | 14 | `RadarGeometry`, `CameraTraits`, `CameraLenses` |
| Translations, plain words, voice | 14 | `Tr`, `Friendly`, `Voice` |

367 tests in 47 files, run with `testDebugUnitTest`; a fake server (`FakeServer.kt`) and fixtures taken from a real server (`tools/capture_fixtures.mjs`) feed them. Every phrase is checked to be in the eight language tables.""",
      "build": "Releases are published on GitHub, from where the app itself checks for updates; the app looks for the asset `ARMOR-ANDROID-CONTROL-release.apk`. The APK is signed with the maintainer's own release key, kept outside the repository, and the app compares the signing certificate of a download with its own before it hands the file to Android's installer. The `versionCode` goes up before each APK, or Android does not treat it as an update.",
      "troubleshooting": r"""| You see | Because | Do |
|---|---|---|
| `wrong_pin`, `pin_locked`, `pin_not_set`, `elevation_required` | The server refuses the disarm PIN or asks for a fresh proof of identity | Type the PIN again, wait for the lock to end, or confirm your identity |
| The sign-in says it cannot go on | The address is outside the house and has no https (plain http is refused) | Follow the guide: a VPN, or a public address with https |
| The connection is refused after it worked | The key of the installation's certificate changed | Pair again with the text of Studio's QR if you changed it on purpose |
| Alarms arrive late or not at all in the background | The battery rules of the phone maker stop the watch; push needs a Firebase project of its own | Exempt the app from battery saving; follow [docs/PUSH_NOTIFICATIONS.md](docs/PUSH_NOTIFICATIONS.md) |
| The update is refused | The signing certificate of the download shares none with the installed app | Do not install it; take the APK from the releases of this repository |""",
      "structure": r"""<p align="center">
  <img src="images/repository-structure.svg" alt="Repository structure of ARMOR-ANDROID-CONTROL" width="100%">
</p>

<details>
<summary>Text version of the tree</summary>

```text
ARMOR-ANDROID-CONTROL/
├── app/src/main/java/es/electrohobby3d/armor/   the app: screens, rules, network and updates
├── app/src/main/assets/                         eight language tables, alarm codes, weather map
├── app/src/test/                                367 tests and a fake server
├── docs/                                        the guides of this repository
├── tools/                                       the shared CI checks and project tooling
├── .github/                                     CI workflow, issue and pull-request templates
├── images/                                      banner, icon and the two pictures of this README
├── build.sh build.bat                           build through the shared project workflow
├── test.sh test.bat                             run the tests through the shared workflow
├── run.sh run.bat                               start through the shared project workflow
├── armor.project.json                           manifest: version, role, maturity, build command
├── CHANGELOG.md                                 what changed in each version
├── SECURITY.md SUPPORT.md LICENSE               security policy, support and license
├── CONTRIBUTING.md CODE_OF_CONDUCT.md           how to contribute and the code of conduct
├── build.gradle.kts settings.gradle.kts         the Gradle build of the project
├── gradle.properties                            Gradle settings
├── gradlew gradlew.bat gradle/                  the Gradle wrapper
├── build-test.sh build-test.bat                 run the tests through the shared workflow
└── .gitattributes .gitignore                    Git settings
```

</details>""",
      "roadmap": r"""**Known limits today**

* The solar, electrical and alarm-panel screens have not met real equipment (only a radar node exists).
* The Bluetooth set-up of a node has not been confirmed against a real node, and push through Firebase has not been tried on a phone.
* The background alarm watch under the battery rules of every phone maker is not proven.
* No independent security review.

**Next**

* Try the solar, electrical and alarm-panel screens with real nodes, and the Bluetooth set-up with a real node.
* Try push through Firebase with an installation's own project, and the alarm watch on several phone makers.""",
    },
  },
  "es": {
    "tagline": "Cliente móvil de operador para ARMOR-SERVER: alarmas, cámaras, radar, energía, la red y la configuración de los nodos, en ocho idiomas",
    "honest": "Las reglas de seguridad de la dirección, de decisión de alarmas, del vigilante de alarmas, de traducción y del rol de solo lectura están cubiertas por 367 tests unitarios y la app compila (`gradlew testDebugUnitTest assembleDebug`). Funciona en un móvil real contra el banco de pruebas de la CM5: el acceso, el monitor de cámaras, el armado y las alarmas, el radar, la configuración de un nodo por Bluetooth y las actualizaciones desde GitHub están en uso. Lo que **todavía no** está probado: las pantallas solar, eléctrica y de centrales de alarma con equipos reales (solo existe un nodo radar), el push por Firebase (está en la app y necesita un proyecto Firebase propio; aún no se ha probado en un móvil) y la vigilancia de alarmas en segundo plano bajo las reglas de batería de cada fabricante.",
    "glance": [
      [
        "Función",
        "Cliente de operador Android para ARMOR-SERVER (familia: Clients, padre: ARMOR-SERVER)",
      ],
      [
        "Tecnología",
        "Kotlin / Jetpack Compose, Android 8.0+",
      ],
      [
        "Pruebas",
        "367 (`gradlew testDebugUnitTest`)",
      ],
      [
        "Idiomas",
        "8 (1345 frases por idioma, cada frase comprobada en todas las tablas)",
      ],
      [
        "Funciona en",
        "Un móvil con Android 8.0+ (minSdk 26)",
      ],
      [
        "En hardware real",
        "Usada en un móvil real contra el banco de pruebas de la CM5; las pantallas solar, eléctrica y de centrales de alarma esperan nodos reales",
      ],
      [
        "Licencia",
        "GPL-3.0-or-later",
      ],
    ],
    "status": {
      "software": "La app compila (`gradlew testDebugUnitTest assembleDebug`) y funciona en un móvil real contra el banco de pruebas CM5.",
      "tests": "Pasan 367 pruebas unitarias (`gradlew testDebugUnitTest`): seguridad de las direcciones, decisión de alarma, vigilante de alarmas, traducciones y rol de solo lectura.",
      "ui": "El inicio de sesión, el monitor de cámaras, el armado y las alarmas y el radar se usan en un móvil real; la configuración de un nodo por Bluetooth no se ha confirmado con un nodo real, y las pantallas solar, eléctrica y de panel de alarma no han visto equipos reales.",
      "hardware": "Se usa en un móvil real contra el banco de pruebas CM5; la vigilancia de alarmas en segundo plano bajo las reglas de batería de cada fabricante no está probada.",
      "security": "Las reglas de seguridad de direcciones y de rol de solo lectura están cubiertas por pruebas unitarias; no ha habido una revisión independiente.",
      "updates": "Las actualizaciones desde GitHub se usan en el móvil.",
      "integration": "El push mediante Firebase está en la app pero necesita un proyecto Firebase propio y no se ha probado en un móvil.",
      "docs": "Ocho idiomas y el historial de cambios están al día.",
    },
    "docs": [
      "[Límites del cliente](docs/CLIENT_BOUNDARY.md): qué hace y qué nunca hace el cliente",
      "[Notificaciones push](docs/PUSH_NOTIFICATIONS.md): los pasos de Firebase, en ocho idiomas",
      "[Pruebas de banco](docs/BENCH_TESTS.md): comprobaciones con un móvil real",
    ],
    "contributing_first": "Antes de un pull request ejecuta `.\\gradlew.bat testDebugUnitTest` and `python -I tools/armor_ci_validate.py`: debe pasar. Consulta [CONTRIBUTING.md](CONTRIBUTING.md) y el [código de conducta](CODE_OF_CONDUCT.md).",
    "languages_extra": "",
    "body": {
      "overview": r"""* **Acceso con el login del propio servidor:** IP, puerto, usuario y contraseña; la contraseña crea una sesión HttpOnly; solo se guarda en el móvil si marcas **Recordarme** (apagado por defecto: usuario y contraseña sellados con una clave propia del Keystore, solo para ese servidor, y se olvidan en cuanto la desmarcas). Un rol **viewer** solo mira: todo botón que cambia algo está apagado.
* **Bloqueo con el teléfono:** la app pide la huella, el rostro o el PIN del propio teléfono antes de armar, desarmar, silenciar una sirena, desbloquear y las demás órdenes críticas (activado por defecto solo si el teléfono tiene huella o rostro) y, si lo activas, para abrir la app. Tu administrador puede exigirlo desde Studio pero nunca bajar lo que elegiste, un teléfono sin bloqueo de pantalla nunca se queda fuera y la pantalla bloqueada siempre ofrece entrar de nuevo con la contraseña. Opcionalmente (desactivado por defecto, con un aviso visible) la clave que sella la sesión guardada puede atarse al desbloqueo del teléfono; entonces la vigilancia de alarmas en segundo plano espera a que desbloquees el teléfono tras un reinicio.
* **Monitor de cámaras:** de 1 a 16 teselas, una vista ampliada, MJPEG en directo que conserva la proporción, un mando PTZ acotado, capturas y grabaciones, con visor y confirmación de borrado de las grabaciones.
* **Armar y desarmar,** tras una **comprobación antes de armar** (qué está abierto, mudo o caído) y con el PIN para desarmar; **alarmas** que reconocer, con una insignia para las que esperan; **dispositivos** (humo, gas, inundación, puerta, ventana, movimiento, clima, enchufes, luces, sirenas, cerraduras, persianas, motores de cancela y garaje, calentadores) con su estado y Encender / Apagar / Alternar.
* **Alarmas que te alcanzan:** un sonido para cada gravedad, una **alarma hablada** opcional, avisos de un nodo que llega a ALTA, una cámara muda, una alarma de dispositivo y (armado) un nodo desconectado, y **una central que suena despierta el móvil**; la vigilancia en segundo plano sobrevive a un reinicio y cede cuando el servidor está caído.
* **Radar en vivo, en 2D y 3D:** la pestaña Radar dibuja el sitio tal como se diseñó en Studio y las personas que ven los radares moviéndose sobre él, refrescado cada segundo y medio; arrastra, pellizca y gira la vista 3D.
* **Energía solar y eléctrica:** los totales (sol, consumo, baterías con su carga, si hay red), cada inversor y batería con las celdas a demanda, y los canales y alarmas de los nodos eléctricos.
* **Centrales de alarma:** el estado de cada nodo ARMOR-NODE-ALARM, sus zonas y eventos, y comandos de armar / desarmar cuando el servidor los permite.
* **Red:** los dispositivos de la red de la casa, el estado de internet y la **dirección pública** con el proveedor y el lugar, como los informa el nodo de red.
* **Configurar un nodo de campo por Bluetooth** (desde la pantalla de acceso o *Más > Configurar un nodo*): encuentra los nodos que anuncian `ARMOR-xxxxxx`, crea el administrador de uno nuevo o entra (con el PIN del nodo), busca redes Wi-Fi y fija el nombre del nodo, el Wi-Fi de un router o una dirección fija y el broker; un **buscador de nodos** lista los que ya están en la red.
* **El asistente:** comandos escritos y hablados (lista cerrada, en ocho idiomas, con una confirmación ligada a ti) para preguntar el estado de la casa o armar, desarmar, silenciar y encender o apagar luces.
* **Biblioteca de evidencias,** estado del perímetro y de los nodos, un **historial** de cada alerta, nodo, cámara, dispositivo, alarma y cambio de modo, el **mapa del tiempo**, y los **servicios** y actualizaciones de la instalación.
* **Ocho idiomas** (inglés, español, alemán, francés, italiano, japonés, chino y portugués), elegidos en *Más > Ajustes* o siguiendo al móvil; se comprueba que cada frase está en las ocho tablas.
* **Cuidado con la contraseña:** HTTP plano solo se permite a un *literal* IPv4 de LAN privada o loopback; se rechaza un nombre de host que solo empieza como una dirección privada (`10.attacker.example`) o una dirección con cero a la izquierda. El aspecto está hecho de iconos: superficies casi negras, acento cian, ámbar para la atención.
* **Seguridad desde el móvil:** el segundo factor y sus códigos de recuperación, las sesiones abiertas, una comprobación de cómo ve el servidor al móvil, la nueva prueba de identidad para acciones críticas desde fuera y, para un administrador, la VPN (dispositivos con su configuración) y el nombre de DNS dinámico.
* **Todo el sistema en la pantalla de estado y la entrada desde fuera:** la pantalla de estado resume las centrales de alarma, los servicios, las cámaras que graban y la seguridad y el acceso remoto, y cada tarjeta abre su pantalla; y cuando la dirección escrita está fuera de casa y sin https, el inicio de sesión dice por qué no puede seguir y una guía explica las dos vías seguras (VPN, o dirección pública con https).
* **Salud de los nodos y modos de armado:** una pantalla Salud de los nodos en Más (tiempo encendido, motivo del reinicio, memoria, enlace y señal, conexiones al broker, reinicios, último error y los avisos del servidor de cada nodo) y, en la pantalla de Centrales de alarma, un selector de modo (Fuera, En casa, Noche y los tuyos) que arma una central en el modo elegido cuando su firmware los conoce. Ocho idiomas.
* **Conexiones en el historial:** la pantalla Historial tiene una segunda lista, solo de lectura, con los dispositivos y apps que se conectan al servidor (Studio, esta app, los paneles de los nodos, el servicio de voz), cuándo se vio cada uno por última vez, sus sesiones abiertas y sus inicios de sesión y rechazos; la app ahora le dice al servidor qué es para aparecer como ella misma. Las direcciones solo las ven los administradores.
* **Mantenimiento de baterías (administradores):** las operaciones sencillas en una batería Pylontech - reloj, contadores y registros, reinicio, capacidad, prueba de MOSFET, fallo de fusible, salidas - en los mismos dos pasos que Studio (el servidor hace que el nodo lea la batería, la pantalla muestra exactamente lo que se hará y luego "Hacerlo ahora" con el número de serie escrito otra vez), con el resultado y lo que cambió; los límites, el firmware y la consola de experto se quedan en Studio.
* **Control de los nodos (administradores):** Más > Control de nodos da las mismas operaciones que Studio - reiniciar, pausar, reanudar, poner en espera (trabajo apagado, sigue conectado), identificar, diagnóstico y mantenimiento activado o desactivado - a un nodo o a todos, pidiendo que se escriba de nuevo el nombre del nodo (o la palabra RESTART, PAUSE o STANDBY para todos) y la prueba de identidad nueva, mostrando hasta dónde llegó cada nodo y avisando de que una central de alarma o un radar en pausa o en espera dejan la casa sin proteger. No existe restablecimiento de fábrica, borrado ni sueño profundo.
* **Una ventana de alarma en la app abierta:** mientras una alarma espera a una persona, un aviso sobre todas las pantallas menos la de alarmas late (rojo y rápido si es crítica, ámbar en las demás, quieto si el móvil tiene las animaciones apagadas), dice cuál es la peor alarma y cuántas esperan, y deja usar la app por debajo; puede abrir las alarmas, confirmar desde el aviso o cerrarse hasta que llegue otra alarma.
* **Desde fuera de casa:** dos direcciones (la privada en la wifi de casa, la de fuera con datos móviles o la VPN) elegidas según dónde esté el teléfono, probando la otra si una no responde y con un mensaje que dice qué falla; la clave del certificado de la instalación se recuerda la primera vez (o se empareja con el texto del QR de Studio) y una distinta se rechaza, y se rechaza el http plano a un servidor al que ya se llegó por https; el panel de un nodo puede abrirse a través del servidor; las alarmas pueden llegar como push solo con datos, anunciadas una vez lleguen por push o por la vigilancia; la app abierta y la vigilancia comparten una lectura del servidor; las cámaras se paran fuera de pantalla y vuelven con esperas crecientes.
* **Avisos a tu medida, con sonidos y una voz propios:** en los ajustes, silenciar todos los avisos, mostrarlos sin sonido ni vibración (y sin decirlos en voz alta) y desactivarlos por gravedad (alta, baja) o por tipo (alertas del radar, cámaras que no responden, nodos desconectados o callados, y las alarmas de dispositivos, solar, eléctrico, red y paneles de alarma); una alarma crítica siempre avisa salvo que se silencien todos. Un sonido para cada gravedad y cada tipo de aviso, de los sonidos del móvil o de un fichero propio (menos de 3 MB), cada uno con un botón de reproducir; y la voz que dice las alarmas (mujer, hombre o cualquiera; niño, adulto o mayor; normal, héroe de acción o señor oscuro; velocidad; y si también se dicen los avisos de gravedad baja) con un botón de prueba.
* **Un banner que te lleva a la pantalla correcta y una vigilancia más tranquila:** el banner de una alarma abre la pantalla que la atiende (cámaras, dispositivos, inversores o baterías, la pantalla eléctrica, la red o los paneles de alarma); el móvil dice su idioma al registrarse para push y el servidor escribe el aviso en él, y un token nuevo de Firebase llega al servidor enseguida desde segundo plano. Una cámara con dos lentes en una sola transmisión son dos ventanas de la lista de cámaras. Mientras los avisos push funcionan, la vigilancia en segundo plano consulta al servidor cada 120 s en lugar de cada 10 (*Ajustes > Vigilancia con avisos push*: 10, 60, 120, 300 o 600 s).""",
      "role": r"""ARMOR-ANDROID-CONTROL es la ventana del móvil al mismo [ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER) que usa [ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO): lee y ordena a través de él y de nada más. Es donde las alarmas te siguen (una central que suena despierta el móvil), donde preguntas al asistente por voz, y la herramienta para configurar un nodo nuevo por Bluetooth sobre el terreno, a su lado.

| Nombre | Cómo | Para qué |
|---|---|---|
| ARMOR-SERVER | HTTP `/api/v1` (55 paths), MJPEG | Todo lo que la app lee y ordena |
| Nodos de campo | Bluetooth (`ARMOR-xxxxxx`) | Configura un nodo nuevo estando a su lado |
| GitHub | HTTPS | Comprueba y descarga la actualización firmada de la propia app |
| Open-Meteo | HTTPS | La previsión, la calidad del aire y la búsqueda de lugares públicas del mapa del tiempo |""",
      "architecture": r"""<p align="center">
  <img src="images/architecture.svg" alt="Arquitectura de ARMOR-ANDROID-CONTROL: quién lo llama, qué contiene y de qué depende" width="100%">
</p>""",
      "security": r"""| Amenaza | Defensa |
|---|---|
| Una contraseña guardada en el móvil | Solo con *Recordarme* (apagado por defecto): usuario y contraseña sellados con una clave propia del Keystore, solo para ese servidor, olvidados al desmarcar; sin copia de seguridad (`allowBackup=false`) |
| HTTP plano hacia internet | Solo se permite a un *literal* IPv4 de red privada o loopback; un host como `10.attacker.example` o una dirección con cero inicial (`010.0.0.1` se lee octal) se rechaza; el http plano se rechaza para un host al que se llegó por https |
| Un intermediario en https | La confianza son las autoridades del sistema más las que instalaste en el móvil; la clave del certificado de la instalación se recuerda la primera vez (o se empareja con el texto del QR de Studio) y una distinta se rechaza |
| Una orden crítica con el móvil en otras manos | La huella, la cara o el PIN del móvil antes de armar, desarmar, silenciar una sirena, desbloquear y otras órdenes críticas (activo por defecto solo si el móvil tiene huella o cara); el administrador puede exigirlo desde Studio pero nunca bajar lo que elegiste; un móvil sin bloqueo nunca se queda fuera |
| Un visor cambia algo | El rol *visor* lo ve todo pero todos los botones que cambian algo están apagados (pruebas de rol) |
| Un PIN de desarmado incorrecto | El PIN solo se manda al servidor al desarmar; `wrong_pin`, `pin_locked`, `pin_not_set` y `elevation_required` se traducen a texto llano |
| Una falsa actualización de la app | Se comparan los SHA-256 de los certificados de firma (historial) de la app instalada y del candidato antes de llamar al instalador de Android; si no comparten ninguno, se dice claramente |
| Una alarma que el móvil no ve | Un servicio en primer plano (`AlarmWatcherService`) sondea cada 10 s, espera 15 s a que el móvil se desbloquee, retrocede hasta 60 s, dice *inalcanzable* tras 6 fallos y sobrevive al reinicio; una alarma de más de 15 minutos no se anuncia |
| Una contraseña de cámara en el móvil | Las cámaras se ven por el flujo del servidor: la app no tiene contraseña de cámara ni dirección RTSP |

### Permisos

`INTERNET`, `ACCESS_NETWORK_STATE`: el servidor. `USE_BIOMETRIC`: el bloqueo del móvil. `POST_NOTIFICATIONS`: las alarmas. `FOREGROUND_SERVICE` (+ `DATA_SYNC`, `SPECIAL_USE`) y `RECEIVE_BOOT_COMPLETED`: la vigilancia de alarmas. `REQUEST_INSTALL_PACKAGES`: la actualización de la app. `BLUETOOTH_SCAN`, `BLUETOOTH_CONNECT`: la configuración de un nodo; `BLUETOOTH`, `BLUETOOTH_ADMIN` y `ACCESS_FINE_LOCATION` solo hasta Android 11 (`maxSdkVersion=30`), para el escaneo Bluetooth.

No hay revisión de seguridad independiente. Lee [docs/CLIENT_BOUNDARY.md](docs/CLIENT_BOUNDARY.md) y [SECURITY.md](SECURITY.md).""",
      "interfaces": r"""| Parte | Qué define |
|---|---|
| ARMOR-SERVER | 55 rutas distintas de `/api/v1` en `network/ArmorApiClient.kt` (la interfaz es `network/ArmorApi.kt`); el radar se lee cada 1,5 s; las cámaras por MJPEG a través del servidor |
| Dos direcciones | La privada en el Wi-Fi de casa y la de fuera (datos móviles o la VPN), elegidas según dónde esté el móvil; si una no responde se prueba la otra y el mensaje dice qué falla |
| Bluetooth | Encuentra los nodos que anuncian `ARMOR-xxxxxx`, crea el administrador de uno nuevo o entra con el PIN del nodo, busca redes Wi-Fi y define el nombre, el Wi-Fi o una dirección fija y el broker; el protocolo es `model/NodeBle.kt`; un buscador de nodos lista los que ya están en la red |
| Voz | `POST /api/v1/voice/command`: una lista cerrada de órdenes en ocho idiomas, con una confirmación atada a ti (`model/Voice.kt`, `VoiceScreens.kt`) |
| Push | `PushService`: alarmas como mensajes solo con datos, anunciadas una vez lleguen por push o por la vigilancia; los pasos de Firebase están en [docs/PUSH_NOTIFICATIONS.md](docs/PUSH_NOTIFICATIONS.md) (ocho idiomas) |""",
      "configuration": r"""| Nombre | Valor | Qué define |
|---|---|---|
| `compileSdk` / `targetSdk` / `minSdk` | 37 / 37 / 26 | Android 8.0 o posterior en el móvil |
| `versionName` | = `armor.project.json` | La compilación falla si el manifiesto y la versión difieren |
| JDK / Android SDK | 17+ / 37 | Para compilar la app y ejecutar las pruebas |

En la app (no en ficheros): el idioma (los ocho o seguir al móvil), las dos direcciones, *Recordarme*, el bloqueo del móvil, la alarma hablada y las notificaciones, en *Más > Ajustes*. Límites en el código: la vigilancia sondea cada 10 s, retrocede hasta 60 s e ignora alarmas de más de 15 minutos.""",
      "quickstart": r"""**Requisitos:** JDK 17+, el SDK de Android (compile SDK 37), un móvil con Android 8.0+ (minSdk 26).

```powershell
.\gradlew.bat testDebugUnitTest assembleDebug   # 367 tests, then the debug APK
adb install -r app\build\outputs\apk\debug\app-debug.apk
```

Las versiones se publican en GitHub, desde donde la propia app busca actualizaciones; el APK se firma con la clave de publicación propia del responsable, guardada fuera del repositorio, y la app compara el certificado de firma de una descarga con el suyo antes de pasar el archivo al instalador de Android. Véase el [límite del cliente](docs/CLIENT_BOUNDARY.md).""",
      "testing": r"""```powershell
.\gradlew.bat testDebugUnitTest
python -I tools/armor_ci_validate.py
```

| Parte | Pruebas | Qué cubre |
|---|---|---|
| Alarmas | 67 | `AlarmPolicy`, `AlarmBanner`, `AlarmPanels`, `AlarmCodes`, `AlarmRoute`, `NoticeFilter`, `PushEvents`, `DevicesAndAlarms` |
| Enlace con el servidor, lectura, datos de prueba | 59 | `ApiClient`, `ApiError`, `ServerFixtures`, `ParsersTolerant`, `SavePayload`, `JsonText`, `Preflight`, `SharedFeed`, `Connections` |
| Modelo de vista y roles | 41 | `ArmorViewModel`, `Viewer`, `ArmProfiles`, `NodeCensus`, `NodeHealth` |
| Bloqueo, almacén de sesión, claves | 38 | `DeviceLock`, `SessionVault`, `CredentialVault`, `KeyBinding`, `Security` |
| Seguridad de direcciones, certificados | 32 | `ServerEndpoint`, `ServerAddresses`, `Literals`, `NodeAddress`, `CertificatePins`, `RemoteAccess` |
| Energía y red | 34 | `Solar`, `Battery`, `Electrical`, `Network` |
| Nodos por Bluetooth, control de nodos | 26 | `NodeBle`, `NodeControl` |
| Actualizaciones desde GitHub | 17 | `GitHubReleaseUpdaterHttpFailure`, `SignerCheck`, `SemanticVersion`, `ReleaseMetadataParser` |
| Radar y cámaras | 14 | `RadarGeometry`, `CameraTraits`, `CameraLenses` |
| Traducciones, palabras sencillas, voz | 14 | `Tr`, `Friendly`, `Voice` |

367 pruebas en 47 ficheros, con `testDebugUnitTest`; un servidor falso (`FakeServer.kt`) y datos tomados de un servidor real (`tools/capture_fixtures.mjs`) las alimentan. Se comprueba que cada frase esté en las ocho tablas de idioma.""",
      "build": "Las versiones se publican en GitHub, desde donde la propia app comprueba las actualizaciones; la app busca el recurso `ARMOR-ANDROID-CONTROL-release.apk`. El APK se firma con la clave de versión del mantenedor, guardada fuera del repositorio, y la app compara el certificado de firma de una descarga con el suyo antes de pasar el fichero al instalador de Android. El `versionCode` sube antes de cada APK, o Android no lo trata como actualización.",
      "troubleshooting": r"""| Ves | Porque | Haz |
|---|---|---|
| `wrong_pin`, `pin_locked`, `pin_not_set`, `elevation_required` | El servidor rechaza el PIN de desarmado o pide una prueba de identidad nueva | Escribe el PIN de nuevo, espera a que acabe el bloqueo o confirma tu identidad |
| El inicio de sesión dice que no puede continuar | La dirección está fuera de casa y no tiene https (el http plano se rechaza) | Sigue la guía: una VPN, o una dirección pública con https |
| La conexión se rechaza tras haber funcionado | Cambió la clave del certificado de la instalación | Vuelve a emparejar con el texto del QR de Studio si lo cambiaste a propósito |
| Las alarmas llegan tarde o no llegan en segundo plano | Las reglas de batería del fabricante detienen la vigilancia; el push necesita un proyecto Firebase propio | Excluye la app del ahorro de batería; sigue [docs/PUSH_NOTIFICATIONS.md](docs/PUSH_NOTIFICATIONS.md) |
| La actualización se rechaza | El certificado de firma de la descarga no comparte ninguno con la app instalada | No lo instales; toma el APK de las versiones de este repositorio |""",
      "structure": r"""<p align="center">
  <img src="images/repository-structure.svg" alt="Estructura del repositorio de ARMOR-ANDROID-CONTROL" width="100%">
</p>

<details>
<summary>Versión en texto del árbol</summary>

```text
ARMOR-ANDROID-CONTROL/
├── app/src/main/java/es/electrohobby3d/armor/   la app: pantallas, reglas, red y actualizaciones
├── app/src/main/assets/                         ocho tablas de idioma, códigos de alarma, mapa del tiempo
├── app/src/test/                                367 pruebas y un servidor falso
├── docs/                                        las guías de este repositorio
├── tools/                                       las comprobaciones de CI compartidas y las herramientas del proyecto
├── .github/                                     flujo de CI y plantillas de issues y pull requests
├── images/                                      banner, icono y las dos imágenes de este README
├── build.sh build.bat                           compilar con el flujo de proyecto compartido
├── test.sh test.bat                             ejecutar las pruebas con el flujo compartido
├── run.sh run.bat                               arrancar con el flujo de proyecto compartido
├── armor.project.json                           manifiesto: versión, rol, madurez, comando de build
├── CHANGELOG.md                                 qué cambió en cada versión
├── SECURITY.md SUPPORT.md LICENSE               política de seguridad, soporte y licencia
├── CONTRIBUTING.md CODE_OF_CONDUCT.md           cómo contribuir y el código de conducta
├── build.gradle.kts settings.gradle.kts         la compilación Gradle del proyecto
├── gradle.properties                            ajustes de Gradle
├── gradlew gradlew.bat gradle/                  el envoltorio de Gradle
├── build-test.sh build-test.bat                 ejecutar las pruebas con el flujo compartido
└── .gitattributes .gitignore                    ajustes de Git
```

</details>""",
      "roadmap": r"""**Límites conocidos hoy**

* Las pantallas de solar, eléctrico y panel de alarma no han conocido equipo real (solo existe un nodo radar).
* La configuración Bluetooth de un nodo no se ha confirmado con un nodo real, y el push de Firebase no se ha probado en un móvil.
* La vigilancia de alarmas en segundo plano bajo las reglas de batería de cada fabricante no está probada.
* No hay revisión de seguridad independiente.

**Lo siguiente**

* Probar las pantallas de solar, eléctrico y panel de alarma con nodos reales, y la configuración Bluetooth con un nodo real.
* Probar el push de Firebase con un proyecto propio de una instalación, y la vigilancia de alarmas en varios fabricantes.""",
    },
  },
  "de": {
    "tagline": "Mobiler Bediener-Client für ARMOR-SERVER: Alarme, Kameras, Radar, Energie, das Netzwerk und die Einrichtung der Knoten, in acht Sprachen",
    "honest": "Die Regeln für Adresssicherheit, Alarmentscheidung, Alarmwächter, Übersetzung und die Nur-Lese-Rolle sind von 367 Unit-Tests abgedeckt, und die App baut (`gradlew testDebugUnitTest assembleDebug`). Sie läuft auf einem echten Telefon gegen den CM5-Testaufbau: Anmeldung, Kameramonitor, Scharfschalten und Alarme, Radar, die Einrichtung eines Knotens per Bluetooth und die Updates von GitHub sind im Einsatz. **Noch nicht** bewiesen: die Solar-, Elektro- und Alarmzentralen-Bildschirme mit echten Geräten (es gibt nur einen Radarknoten), Push über Firebase (es ist in der App und braucht ein eigenes Firebase-Projekt; es wurde noch nicht auf einem Handy erprobt) und die Alarmüberwachung im Hintergrund unter den Akkuregeln jedes Herstellers.",
    "glance": [
      [
        "Rolle",
        "Android-Bedienclient für ARMOR-SERVER (Familie: Clients, übergeordnet: ARMOR-SERVER)",
      ],
      [
        "Technik",
        "Kotlin / Jetpack Compose, Android 8.0+",
      ],
      [
        "Tests",
        "367 (`gradlew testDebugUnitTest`)",
      ],
      [
        "Sprachen",
        "8 (1345 Sätze je Sprache, jeder Satz in allen Tabellen geprüft)",
      ],
      [
        "Läuft auf",
        "Ein Telefon mit Android 8.0+ (minSdk 26)",
      ],
      [
        "Auf echter Hardware",
        "Auf einem echten Telefon gegen den CM5-Testaufbau im Einsatz; die Solar-, Elektro- und Alarmzentralen-Bildschirme warten auf echte Knoten",
      ],
      [
        "Lizenz",
        "GPL-3.0-or-later",
      ],
    ],
    "status": {
      "software": "Die App wird gebaut (`gradlew testDebugUnitTest assembleDebug`) und läuft auf einem echten Telefon gegen den CM5-Prüfstand.",
      "tests": "367 Unit-Tests bestehen (`gradlew testDebugUnitTest`): Adresssicherheit, Alarmentscheidung, Alarmüberwachung, Übersetzungen und die Nur-Lese-Rolle.",
      "ui": "Anmeldung, Kameramonitor, Scharfschalten und Alarme sowie das Radar sind auf einem echten Telefon im Einsatz; die Bluetooth-Einrichtung eines Knotens ist an einem echten Knoten nicht bestätigt, und die Bildschirme für Solar, Elektrik und Alarmzentrale sind noch keinen echten Geräten begegnet.",
      "hardware": "Auf einem echten Telefon gegen den CM5-Prüfstand genutzt; die Alarmüberwachung im Hintergrund unter den Akkuregeln jedes Herstellers ist nicht belegt.",
      "security": "Die Regeln für Adresssicherheit und die Nur-Lese-Rolle sind durch Unit-Tests abgedeckt; es gab keine unabhängige Prüfung.",
      "updates": "Die Aktualisierungen von GitHub werden auf dem Telefon genutzt.",
      "integration": "Push über Firebase ist in der App, braucht aber ein eigenes Firebase-Projekt und wurde auf einem Telefon nicht erprobt.",
      "docs": "Acht Sprachen und das Änderungsprotokoll sind aktuell.",
    },
    "docs": [
      "[Client-Grenze](docs/CLIENT_BOUNDARY.md): was der Client tut und nie tut",
      "[Push-Benachrichtigungen](docs/PUSH_NOTIFICATIONS.md): die Firebase-Schritte in acht Sprachen",
      "[Prüfstandtests](docs/BENCH_TESTS.md): Prüfungen mit einem echten Telefon",
    ],
    "contributing_first": "Führe vor einem Pull Request `.\\gradlew.bat testDebugUnitTest` and `python -I tools/armor_ci_validate.py` aus: Es muss bestehen. Siehe [CONTRIBUTING.md](CONTRIBUTING.md) und den [Verhaltenskodex](CODE_OF_CONDUCT.md).",
    "languages_extra": "",
    "body": {
      "overview": r"""* **Anmeldung mit dem Login des Servers selbst:** IP, Port, Benutzer und Passwort; das Passwort erzeugt eine HttpOnly-Sitzung; es wird nur auf dem Telefon gespeichert, wenn Sie **Merken** ankreuzen (standardmäßig aus: Benutzer und Passwort mit einem eigenen Keystore-Schlüssel versiegelt, nur für diesen Server, und sofort vergessen, sobald Sie den Haken entfernen). Eine Rolle **Viewer** sieht nur an: Jede Schaltfläche, die etwas ändert, ist aus.
* **Sperre mit dem Telefon:** Die App verlangt Fingerabdruck, Gesicht oder PIN des Telefons selbst vor dem Scharfschalten, Entschärfen, Stummschalten einer Sirene, Entsperren und den anderen kritischen Befehlen (standardmäßig nur aktiv, wenn das Telefon Fingerabdruck oder Gesicht hat) und, wenn du es einschaltest, zum Öffnen der App. Dein Administrator kann es in Studio verlangen, aber nie unter deine Wahl senken; ein Telefon ohne Bildschirmsperre wird nie ausgesperrt, und der gesperrte Bildschirm bietet immer die erneute Anmeldung mit dem Passwort an. Optional (standardmäßig aus, mit sichtbarem Hinweis) lässt sich der Schlüssel, der die gespeicherte Sitzung versiegelt, an das Entsperren des Telefons binden; dann wartet die Alarmüberwachung im Hintergrund nach einem Neustart, bis Sie das Telefon entsperren.
* **Kameramonitor:** 1 bis 16 Kacheln, eine vergrößerte Ansicht, Live-MJPEG mit erhaltenem Seitenverhältnis, ein begrenztes PTZ-Pad, Schnappschüsse und Aufnahmen, mit Betrachter und Löschbestätigung für Aufnahmen.
* **Scharf- und Unscharfschalten** nach einer **Prüfung vor dem Scharfschalten** (was offen, stumm oder ausgefallen ist) und mit der PIN zum Unscharfschalten; **Alarme** zum Quittieren, mit einem Zähler für wartende; **Geräte** (Rauch, Gas, Wasser, Tür, Fenster, Bewegung, Klima, Steckdosen, Lichter, Sirenen, Schlösser, Rollläden, Tor- und Garagenantriebe, Warmwasserbereiter) mit Zustand und Ein / Aus / Umschalten.
* **Alarme, die Sie erreichen:** ein Ton für jede Stufe, ein optionaler **gesprochener Alarm**, Benachrichtigungen bei einem Knoten, der HOCH erreicht, einer stummen Kamera, einem Gerätealarm und (scharf) einem Offline-Knoten, und **eine Zentrale, die läutet, weckt das Telefon**; die Hintergrundüberwachung übersteht einen Neustart und hält sich zurück, wenn der Server aus ist.
* **Live-Radar in 2D und 3D:** der Reiter Radar zeichnet den Standort, wie er in Studio entworfen wurde, und die Personen, die die Radare darauf sich bewegen sehen, jede anderthalb Sekunden aktualisiert; ziehen, zoomen und drehen Sie die 3D-Ansicht.
* **Solar- und Elektroenergie:** die Summen (Sonne, Verbrauch, Batterien mit ihrer Ladung, ob das Netz da ist), jeder Wechselrichter und jede Batterie mit den Zellen auf Abruf sowie die Kanäle und Alarme der Elektroknoten.
* **Alarmzentralen:** der Zustand jedes ARMOR-NODE-ALARM-Knotens, seine Zonen und Ereignisse und Scharf-/Unscharf-Befehle, wenn der Server sie erlaubt.
* **Netzwerk:** die Geräte des Hausnetzes, der Internetzustand und die **öffentliche Adresse** mit Anbieter und Ort, wie der Netzwerkknoten sie meldet.
* **Einen Feldknoten per Bluetooth einrichten** (vom Anmeldebildschirm oder *Mehr > Knoten einrichten*): findet die Knoten, die `ARMOR-xxxxxx` senden, legt den Administrator eines neuen an oder meldet sich an (mit der PIN des Knotens), sucht WLAN-Netze und setzt Namen, das WLAN eines Routers oder eine feste Adresse und den Broker; ein **Knotenfinder** listet die bereits im Netz vorhandenen.
* **Der Assistent:** geschriebene und gesprochene Befehle (geschlossene Liste, in acht Sprachen, mit einer an Sie gebundenen Bestätigung), um den Zustand des Hauses zu erfragen oder scharf, unscharf, stumm und Licht ein oder aus zu schalten.
* **Beweisbibliothek,** Zustand von Perimeter und Knoten, ein **Verlauf** jedes Alarms, Knotens, jeder Kamera, jedes Geräts, Alarms und Moduswechsels, die **Wetterkarte** sowie die **Dienste** und Updates der Anlage.
* **Acht Sprachen** (Englisch, Spanisch, Deutsch, Französisch, Italienisch, Japanisch, Chinesisch und Portugiesisch), gewählt unter *Mehr > Einstellungen* oder dem Telefon folgend; geprüft wird, dass jeder Satz in den acht Tabellen steht.
* **Vorsicht mit dem Passwort:** Klartext-HTTP ist nur zu einem IPv4-*Literal* eines privaten LANs oder Loopbacks erlaubt; ein Hostname, der nur wie eine private Adresse beginnt (`10.attacker.example`), oder eine Adresse mit führender Null wird abgelehnt. Das Aussehen besteht aus Symbolen: fast schwarze Flächen, ein Cyan-Akzent, Bernstein für Aufmerksamkeit.
* **Sicherheit vom Handy aus:** der zweite Faktor und seine Wiederherstellungscodes, die offenen Sitzungen, eine Prüfung, wie der Server das Handy sieht, der neue Identitätsnachweis für kritische Aktionen von außen und, für einen Administrator, das VPN (Geräte mit ihrer Konfiguration) und der dynamische DNS-Name.
* **Das ganze System auf dem Statusbildschirm und der Weg von außen:** der Statusbildschirm fasst Alarmzentralen, Dienste, aufzeichnende Kameras sowie Sicherheit und Fernzugriff zusammen, jede Karte öffnet ihren Bildschirm; und ist die eingegebene Adresse außerhalb des Hauses und ohne https, sagt die Anmeldung, warum sie nicht weitergeht, und eine Anleitung erklärt die zwei sicheren Wege (VPN oder öffentliche Adresse mit https).
* **Zustand der Knoten und Scharfschaltmodi:** ein Bildschirm Zustand der Knoten unter Mehr (Laufzeit, Neustartgrund, Speicher, Verbindung und Signal, Brokerverbindungen, Neustarts, letzter Fehler und die Warnungen des Servers je Knoten) und auf dem Bildschirm der Alarmzentralen eine Modusauswahl (Abwesend, Zuhause, Nacht und eigene), die eine Zentrale im gewählten Modus scharf schaltet, wenn ihre Firmware die Modi kennt. Acht Sprachen.
* **Verbindungen im Verlauf:** Der Verlaufsbildschirm hat eine zweite Liste, nur lesend, mit den Geräten und Apps, die sich mit dem Server verbinden (Studio, diese App, die Panels der Knoten, der Sprachdienst), wann jedes zuletzt gesehen wurde, seinen offenen Sitzungen sowie Anmeldungen und Ablehnungen; die App sagt dem Server jetzt, was sie ist, und erscheint so als sie selbst. Adressen sehen nur Administratoren.
* **Batteriewartung (Administratoren):** die einfachen Operationen an einer Pylontech-Batterie - Uhr, Zähler und Protokolle, Neustart, Kapazität, MOSFET-Test, Sicherungsfehler, Ausgänge - in denselben zwei Schritten wie in Studio (der Server lässt den Knoten die Batterie lesen, der Bildschirm zeigt genau, was getan wird, dann "Jetzt ausführen" mit nochmals eingetippter Seriennummer), mit Ergebnis und Änderungen; Grenzwerte, Firmware und Expertenkonsole bleiben in Studio.
* **Steuerung der Knoten (Administratoren):** Mehr > Knotensteuerung bietet dieselben Operationen wie Studio - Neustart, Pause, Fortsetzen, Standby (Arbeit aus, bleibt verbunden), Identifizieren, Diagnose und Wartung ein oder aus - für einen Knoten oder alle, verlangt die erneute Eingabe des Knotennamens (oder des Wortes RESTART, PAUSE oder STANDBY für alle) und den frischen Identitätsnachweis, zeigt, wie weit jeder Knoten ist, und warnt, dass eine pausierte oder im Standby befindliche Alarmzentrale oder ein Radar das Haus ungeschützt lässt. Es gibt kein Zurücksetzen auf Werkseinstellungen, kein Löschen und keinen Tiefschlaf.
* **Ein Alarmfenster in der geöffneten App:** Solange ein Alarm auf eine Person wartet, pulsiert über jedem Bildschirm außer dem der Alarme ein Banner (rot und schnell bei kritischen, bernsteinfarben bei den übrigen, ruhig, wenn das Telefon die Animationen abgeschaltet hat), nennt den schlimmsten Alarm und wie viele warten und lässt die App darunter bedienen; es kann die Alarme öffnen, direkt bestätigen oder bis zum nächsten Alarm geschlossen werden.
* **Von außerhalb des Hauses:** zwei Adressen (die private im Heim-WLAN, die für unterwegs mit Mobilfunkdaten oder VPN), gewählt nach dem Aufenthaltsort des Telefons; antwortet eine nicht, wird die andere versucht, und eine Meldung sagt, was fehlschlägt; der Schlüssel des Zertifikats der Installation wird beim ersten Mal gemerkt (oder mit dem Text des QR-Codes von Studio gekoppelt) und ein anderer abgelehnt, und einfaches http wird für einen Server abgelehnt, der schon per https erreicht wurde; das Panel eines Knotens lässt sich über den Server öffnen; Alarme können als reine Daten-Push eintreffen und werden einmal gemeldet, ob per Push oder durch die Überwachung; die geöffnete App und die Überwachung teilen sich eine Abfrage des Servers; die Kamera-Streams stoppen außerhalb des Bildschirms und kommen mit wachsenden Wartezeiten zurück.
* **Meldungen nach Wunsch, mit eigenen Tönen und einer eigenen Stimme:** In den Einstellungen lassen sich alle Meldungen stummschalten, ohne Ton und Vibration zeigen (und nicht vorlesen) und nach Schweregrad (hoch, niedrig) oder Art (Radar-Alarme, Kameras ohne Antwort, Knoten offline oder still sowie die Alarme von Geräten, Solar, Elektro, Netzwerk und Alarmpanels) abschalten; ein kritischer Alarm meldet sich immer, außer wenn alle Meldungen stumm sind. Ein Ton für jeden Schweregrad und jede Art von Meldung, aus den Tönen des Telefons oder aus einer eigenen Datei (unter 3 MB), jeweils mit Abspielknopf; und die Stimme, die die Alarme spricht (Frau, Mann oder egal; Kind, Erwachsener oder Senior; sachlich, Actionheld oder dunkler Lord; Tempo; ob auch Meldungen niedrigen Schweregrads gesprochen werden) mit Testknopf.
* **Ein Banner, das zum richtigen Bildschirm führt, und eine ruhigere Überwachung:** Das Banner eines Alarms öffnet den Bildschirm, der ihn bearbeitet (Kameras, Geräte, Wechselrichter oder Batterien, der Elektro-Bildschirm, das Netzwerk oder die Alarmpanels); das Telefon nennt dem Server beim Push-Registrieren seine Sprache, damit die Meldung darin geschrieben wird, und ein neues Firebase-Token erreicht den Server sofort aus dem Hintergrund. Eine Kamera mit zwei Objektiven in einem Stream sind zwei Fenster der Kameraliste. Solange die Push-Meldungen funktionieren, fragt die Hintergrundüberwachung den Server alle 120 s statt alle 10 s (*Einstellungen > Überwachung mit Push-Meldungen*: 10, 60, 120, 300 oder 600 s).""",
      "role": r"""ARMOR-ANDROID-CONTROL ist das Fenster des Telefons auf denselben [ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER), den auch [ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) nutzt: Es liest und befiehlt nur über ihn. Hier folgen Ihnen die Alarme (eine läutende Alarmzentrale weckt das Telefon), hier fragen Sie den Assistenten per Sprache, und es ist das Werkzeug, um vor Ort einen neuen Knoten per Bluetooth einzurichten.

| Name | Wie | Wozu |
|---|---|---|
| ARMOR-SERVER | HTTP `/api/v1` (55 paths), MJPEG | Alles, was die App liest und anordnet |
| Feldknoten | Bluetooth (`ARMOR-xxxxxx`) | Richtet einen neuen Knoten direkt neben ihm ein |
| GitHub | HTTPS | Prüft und lädt das signierte Update der App selbst |
| Open-Meteo | HTTPS | Die öffentliche Vorhersage, Luftqualität und Ortssuche der Wetterkarte |""",
      "architecture": r"""<p align="center">
  <img src="images/architecture.svg" alt="Architektur von ARMOR-ANDROID-CONTROL: wer es aufruft, was es enthält und wovon es abhängt" width="100%">
</p>""",
      "security": r"""| Bedrohung | Abwehr |
|---|---|
| Ein auf dem Telefon gespeichertes Passwort | Nur mit *Angemeldet bleiben* (standardmäßig aus): Benutzer und Passwort mit einem eigenen Keystore-Schlüssel versiegelt, nur für diesen Server, beim Abwählen sofort vergessen; kein Backup (`allowBackup=false`) |
| Klartext-HTTP ins Internet | Nur erlaubt zu einem IPv4-*Literal* des privaten Netzes oder Loopback; ein Host wie `10.attacker.example` oder eine Adresse mit führender Null (`010.0.0.1` wird oktal gelesen) wird abgelehnt; Klartext-http wird für einen Host abgelehnt, der über https erreicht wurde |
| Ein Man-in-the-Middle über https | Vertrauen haben die Stellen des Systems plus die, die du auf dem Telefon installiert hast; der Schlüssel des Installationszertifikats wird beim ersten Mal gemerkt (oder mit dem QR-Text von Studio gekoppelt), ein anderer wird abgelehnt |
| Ein kritischer Befehl mit dem Telefon in fremden Händen | Fingerabdruck, Gesicht oder PIN des Telefons vor Scharf-/Unscharfschalten, Sirene stummschalten, Entriegeln und anderen kritischen Befehlen (standardmäßig nur an, wenn das Telefon Fingerabdruck oder Gesicht hat); der Administrator kann es in Studio verlangen, nie senken, was du gewählt hast; ein Telefon ohne Bildschirmsperre wird nie ausgesperrt |
| Ein Betrachter ändert etwas | Die Rolle *Betrachter* sieht alles, aber jede Schaltfläche, die etwas ändert, ist aus (Rollentests) |
| Eine falsche Entschärfungs-PIN | Die PIN geht nur beim Unscharfschalten an den Server; `wrong_pin`, `pin_locked`, `pin_not_set` und `elevation_required` werden in einfache Worte übersetzt |
| Ein gefälschtes App-Update | Die SHA-256 der Signaturzertifikate (Verlauf) der installierten App und des Kandidaten werden verglichen, bevor Androids Installer aufgerufen wird; teilen sie keines, wird es klar gesagt |
| Ein Alarm, den das Telefon nicht sieht | Ein Vordergrunddienst (`AlarmWatcherService`) fragt alle 10 s ab, wartet 15 s auf das Entsperren, weicht bis 60 s zurück, meldet nach 6 Fehlern *nicht erreichbar* und überlebt einen Neustart; ein Alarm, der älter als 15 Minuten ist, wird nicht angekündigt |
| Ein Kamerapasswort auf dem Telefon | Die Kameras werden über den Strom des Servers gesehen: Die App hat kein Kamerapasswort und keine RTSP-Adresse |

### Berechtigungen

`INTERNET`, `ACCESS_NETWORK_STATE`: der Server. `USE_BIOMETRIC`: die Telefonsperre. `POST_NOTIFICATIONS`: Alarme. `FOREGROUND_SERVICE` (+ `DATA_SYNC`, `SPECIAL_USE`) und `RECEIVE_BOOT_COMPLETED`: die Alarmüberwachung. `REQUEST_INSTALL_PACKAGES`: das Update der App. `BLUETOOTH_SCAN`, `BLUETOOTH_CONNECT`: die Einrichtung eines Knotens; `BLUETOOTH`, `BLUETOOTH_ADMIN` und `ACCESS_FINE_LOCATION` nur bis Android 11 (`maxSdkVersion=30`), für die Bluetooth-Suche.

Es gibt keine unabhängige Sicherheitsprüfung. Lies [docs/CLIENT_BOUNDARY.md](docs/CLIENT_BOUNDARY.md) und [SECURITY.md](SECURITY.md).""",
      "interfaces": r"""| Teil | Was sie festlegt |
|---|---|
| ARMOR-SERVER | 55 verschiedene Pfade von `/api/v1` in `network/ArmorApiClient.kt` (die Schnittstelle ist `network/ArmorApi.kt`); das Radar wird alle 1,5 s gelesen; die Kameras per MJPEG über den Server |
| Zwei Adressen | Die private im Heim-WLAN und die für unterwegs (Mobilfunk oder VPN), je nach Aufenthaltsort des Telefons; antwortet eine nicht, wird die andere versucht, und die Meldung sagt, was fehlschlägt |
| Bluetooth | Findet Knoten, die `ARMOR-xxxxxx` ankündigen, legt den Administrator eines neuen an oder meldet sich mit der Knoten-PIN an, sucht WLANs und setzt Name, WLAN oder feste Adresse und den Broker; das Protokoll ist `model/NodeBle.kt`; ein Knotenfinder listet die bereits im Netz befindlichen auf |
| Sprache | `POST /api/v1/voice/command`: eine geschlossene Befehlsliste in acht Sprachen, mit einer an dich gebundenen Bestätigung (`model/Voice.kt`, `VoiceScreens.kt`) |
| Push | `PushService`: Alarme als reine Datennachrichten, einmal angekündigt, ob per Push oder per Überwachung; die Firebase-Schritte stehen in [docs/PUSH_NOTIFICATIONS.md](docs/PUSH_NOTIFICATIONS.md) (acht Sprachen) |""",
      "configuration": r"""| Name | Wert | Was sie festlegt |
|---|---|---|
| `compileSdk` / `targetSdk` / `minSdk` | 37 / 37 / 26 | Android 8.0 oder neuer auf dem Telefon |
| `versionName` | = `armor.project.json` | Der Build schlägt fehl, wenn Manifest und Version abweichen |
| JDK / Android SDK | 17+ / 37 | Zum Bauen der App und Ausführen der Tests |

In der App (nicht in Dateien): die Sprache (die acht oder dem Telefon folgen), die zwei Adressen, *Angemeldet bleiben*, die Telefonsperre, der gesprochene Alarm und die Benachrichtigungen, unter *Mehr > Einstellungen*. Grenzen im Code: Die Überwachung fragt alle 10 s ab, weicht bis 60 s zurück und ignoriert Alarme, die älter als 15 Minuten sind.""",
      "quickstart": r"""**Voraussetzungen:** JDK 17+, das Android SDK (compile SDK 37), ein Telefon mit Android 8.0+ (minSdk 26).

```powershell
.\gradlew.bat testDebugUnitTest assembleDebug   # 367 tests, then the debug APK
adb install -r app\build\outputs\apk\debug\app-debug.apk
```

Die Versionen werden auf GitHub veröffentlicht, von wo die App selbst nach Updates sucht; die APK ist mit dem eigenen Release-Schlüssel des Betreuers signiert, der außerhalb des Repositorys liegt, und die App vergleicht das Signaturzertifikat eines Downloads mit dem eigenen, bevor sie die Datei an das Installationsprogramm von Android übergibt. Siehe die [Client-Grenze](docs/CLIENT_BOUNDARY.md).""",
      "testing": r"""```powershell
.\gradlew.bat testDebugUnitTest
python -I tools/armor_ci_validate.py
```

| Teil | Tests | Was sie abdeckt |
|---|---|---|
| Alarme | 67 | `AlarmPolicy`, `AlarmBanner`, `AlarmPanels`, `AlarmCodes`, `AlarmRoute`, `NoticeFilter`, `PushEvents`, `DevicesAndAlarms` |
| Serververbindung, Auswertung, Testdaten | 59 | `ApiClient`, `ApiError`, `ServerFixtures`, `ParsersTolerant`, `SavePayload`, `JsonText`, `Preflight`, `SharedFeed`, `Connections` |
| View-Model und Rollen | 41 | `ArmorViewModel`, `Viewer`, `ArmProfiles`, `NodeCensus`, `NodeHealth` |
| Sperre, Sitzungstresor, Schlüssel | 38 | `DeviceLock`, `SessionVault`, `CredentialVault`, `KeyBinding`, `Security` |
| Adresssicherheit, Zertifikate | 32 | `ServerEndpoint`, `ServerAddresses`, `Literals`, `NodeAddress`, `CertificatePins`, `RemoteAccess` |
| Energie und Netzwerk | 34 | `Solar`, `Battery`, `Electrical`, `Network` |
| Knoten per Bluetooth, Knotensteuerung | 26 | `NodeBle`, `NodeControl` |
| Updates von GitHub | 17 | `GitHubReleaseUpdaterHttpFailure`, `SignerCheck`, `SemanticVersion`, `ReleaseMetadataParser` |
| Radar und Kameras | 14 | `RadarGeometry`, `CameraTraits`, `CameraLenses` |
| Übersetzungen, einfache Worte, Sprache | 14 | `Tr`, `Friendly`, `Voice` |

367 Tests in 47 Dateien, ausgeführt mit `testDebugUnitTest`; ein Fake-Server (`FakeServer.kt`) und von einem echten Server geholte Daten (`tools/capture_fixtures.mjs`) speisen sie. Es wird geprüft, dass jeder Satz in den acht Sprachtabellen steht.""",
      "build": "Releases werden auf GitHub veröffentlicht, von wo die App selbst nach Updates sucht; die App sucht nach dem Asset `ARMOR-ANDROID-CONTROL-release.apk`. Die APK ist mit dem eigenen Release-Schlüssel des Maintainers signiert, der außerhalb des Repositorys liegt, und die App vergleicht das Signaturzertifikat eines Downloads mit ihrem eigenen, bevor sie die Datei an Androids Installer übergibt. Der `versionCode` steigt vor jeder APK, sonst gilt sie für Android nicht als Update.",
      "troubleshooting": r"""| Sie sehen | Weil | Tun Sie |
|---|---|---|
| `wrong_pin`, `pin_locked`, `pin_not_set`, `elevation_required` | Der Server lehnt die Entschärfungs-PIN ab oder verlangt einen frischen Identitätsnachweis | Gib die PIN erneut ein, warte das Ende der Sperre ab oder bestätige deine Identität |
| Die Anmeldung sagt, dass sie nicht fortfahren kann | Die Adresse liegt außerhalb des Hauses und hat kein https (Klartext-http wird abgelehnt) | Folge der Anleitung: ein VPN oder eine öffentliche Adresse mit https |
| Die Verbindung wird verweigert, nachdem sie funktionierte | Der Schlüssel des Installationszertifikats hat sich geändert | Koppele erneut mit dem QR-Text von Studio, wenn du es absichtlich geändert hast |
| Alarme kommen im Hintergrund spät oder gar nicht an | Die Akkuregeln des Herstellers stoppen die Überwachung; Push braucht ein eigenes Firebase-Projekt | Nimm die App vom Energiesparen aus; folge [docs/PUSH_NOTIFICATIONS.md](docs/PUSH_NOTIFICATIONS.md) |
| Das Update wird abgelehnt | Das Signaturzertifikat des Downloads teilt keines mit der installierten App | Installiere sie nicht; nimm die APK aus den Releases dieses Repositorys |""",
      "structure": r"""<p align="center">
  <img src="images/repository-structure.svg" alt="Repository-Struktur von ARMOR-ANDROID-CONTROL" width="100%">
</p>

<details>
<summary>Textversion des Baums</summary>

```text
ARMOR-ANDROID-CONTROL/
├── app/src/main/java/es/electrohobby3d/armor/   die App: Bildschirme, Regeln, Netz und Updates
├── app/src/main/assets/                         acht Sprachtabellen, Alarmcodes, Wetterkarte
├── app/src/test/                                367 Tests und ein Fake-Server
├── docs/                                        die Anleitungen dieses Repositorys
├── tools/                                       die gemeinsamen CI-Prüfungen und Projektwerkzeuge
├── .github/                                     CI-Workflow sowie Vorlagen für Issues und Pull Requests
├── images/                                      Banner, Symbol und die zwei Bilder dieses READMEs
├── build.sh build.bat                           Build über den gemeinsamen Projekt-Workflow
├── test.sh test.bat                             Tests über den gemeinsamen Workflow ausführen
├── run.sh run.bat                               Start über den gemeinsamen Projekt-Workflow
├── armor.project.json                           Manifest: Version, Rolle, Reifegrad, Build-Befehl
├── CHANGELOG.md                                 was sich in jeder Version geändert hat
├── SECURITY.md SUPPORT.md LICENSE               Sicherheitsrichtlinie, Support und Lizenz
├── CONTRIBUTING.md CODE_OF_CONDUCT.md           Mitwirkung und Verhaltenskodex
├── build.gradle.kts settings.gradle.kts         der Gradle-Build des Projekts
├── gradle.properties                            Gradle-Einstellungen
├── gradlew gradlew.bat gradle/                  der Gradle-Wrapper
├── build-test.sh build-test.bat                 Tests über den gemeinsamen Workflow ausführen
└── .gitattributes .gitignore                    Git-Einstellungen
```

</details>""",
      "roadmap": r"""**Bekannte Grenzen heute**

* Die Bildschirme für Solar, Elektro und Alarmzentrale kennen keine echte Ausrüstung (es gibt nur einen Radarknoten).
* Die Bluetooth-Einrichtung eines Knotens wurde nicht an einem echten Knoten bestätigt, und Push über Firebase wurde auf einem Telefon nicht erprobt.
* Die Alarmüberwachung im Hintergrund unter den Akkuregeln jedes Herstellers ist nicht erwiesen.
* Keine unabhängige Sicherheitsprüfung.

**Als Nächstes**

* Die Bildschirme für Solar, Elektro und Alarmzentrale mit echten Knoten und die Bluetooth-Einrichtung mit einem echten Knoten erproben.
* Push über Firebase mit dem eigenen Projekt einer Installation und die Alarmüberwachung bei mehreren Herstellern erproben.""",
    },
  },
  "fr": {
    "tagline": "Client mobile d'opérateur pour ARMOR-SERVER : alarmes, caméras, radar, énergie, réseau et configuration des nœuds, en huit langues",
    "honest": "Les règles de sécurité de l'adresse, de décision d'alarme, de veilleur d'alarmes, de traduction et de rôle en lecture seule sont couvertes par 367 tests unitaires et l'application se compile (`gradlew testDebugUnitTest assembleDebug`). Elle fonctionne sur un vrai téléphone contre le banc de test CM5 : la connexion, le moniteur de caméras, l'armement et les alarmes, le radar, la configuration d'un nœud en Bluetooth et les mises à jour depuis GitHub sont utilisés. Ce qui n'est **pas** encore prouvé : les écrans solaire, électrique et centrales d'alarme avec du vrai matériel (seul un nœud radar existe), le push via Firebase (il est dans l'application et demande un projet Firebase propre ; il n'a pas encore été essayé sur un téléphone) et la veille d'alarmes en arrière-plan sous les règles de batterie de chaque fabricant.",
    "glance": [
      [
        "Rôle",
        "Client opérateur Android pour ARMOR-SERVER (famille : Clients, parent : ARMOR-SERVER)",
      ],
      [
        "Technologie",
        "Kotlin / Jetpack Compose, Android 8.0+",
      ],
      [
        "Tests",
        "367 (`gradlew testDebugUnitTest`)",
      ],
      [
        "Langues",
        "8 (1345 phrases par langue, chaque phrase vérifiée dans toutes les tables)",
      ],
      [
        "Fonctionne sur",
        "Un téléphone Android 8.0+ (minSdk 26)",
      ],
      [
        "Sur matériel réel",
        "Utilisée sur un vrai téléphone contre le banc de test CM5 ; les écrans solaire, électrique et centrales d'alarme attendent de vrais nœuds",
      ],
      [
        "Licence",
        "GPL-3.0-or-later",
      ],
    ],
    "status": {
      "software": "L'application compile (`gradlew testDebugUnitTest assembleDebug`) et tourne sur un vrai téléphone contre le banc d'essai CM5.",
      "tests": "367 tests unitaires réussissent (`gradlew testDebugUnitTest`) : sécurité des adresses, décision d'alarme, veilleur d'alarmes, traductions et rôle en lecture seule.",
      "ui": "La connexion, le moniteur de caméras, l'armement et les alarmes et le radar sont utilisés sur un vrai téléphone ; la configuration d'un nœud par Bluetooth n'a pas été confirmée avec un vrai nœud, et les écrans solaire, électrique et de centrale d'alarme n'ont pas vu de vrais équipements.",
      "hardware": "Utilisée sur un vrai téléphone contre le banc d'essai CM5 ; la veille d'alarmes en arrière-plan sous les règles de batterie de chaque fabricant n'est pas prouvée.",
      "security": "Les règles de sécurité des adresses et du rôle en lecture seule sont couvertes par des tests unitaires ; il n'y a pas eu de revue indépendante.",
      "updates": "Les mises à jour depuis GitHub sont utilisées sur le téléphone.",
      "integration": "Le push via Firebase est dans l'application mais demande un projet Firebase propre et n'a pas été essayé sur un téléphone.",
      "docs": "Huit langues et le journal des modifications sont à jour.",
    },
    "docs": [
      "[Limites du client](docs/CLIENT_BOUNDARY.md) : ce que le client fait et ne fait jamais",
      "[Notifications push](docs/PUSH_NOTIFICATIONS.md) : les étapes Firebase, en huit langues",
      "[Essais de banc](docs/BENCH_TESTS.md) : contrôles avec un vrai téléphone",
    ],
    "contributing_first": "Avant une pull request, lancez `.\\gradlew.bat testDebugUnitTest` and `python -I tools/armor_ci_validate.py` : il doit réussir. Voir [CONTRIBUTING.md](CONTRIBUTING.md) et le [code de conduite](CODE_OF_CONDUCT.md).",
    "languages_extra": "",
    "body": {
      "overview": r"""* **Connexion avec le login du serveur lui-même :** IP, port, utilisateur et mot de passe ; le mot de passe crée une session HttpOnly ; il n'est stocké sur le téléphone que si vous cochez **Se souvenir de moi** (désactivé par défaut : utilisateur et mot de passe scellés avec une clé propre du Keystore, pour ce serveur seulement, oubliés dès que vous décochez). Un rôle **viewer** ne fait que regarder : tout bouton qui change quelque chose est désactivé.
* **Verrouillage avec le téléphone :** l'application demande l'empreinte, le visage ou le code du téléphone lui-même avant d'armer, de désarmer, de couper une sirène, de déverrouiller et pour les autres ordres critiques (activé par défaut seulement si le téléphone a une empreinte ou un visage) et, si tu l'actives, pour ouvrir l'application. Ton administrateur peut l'exiger depuis Studio mais jamais abaisser ton choix ; un téléphone sans verrouillage d'écran n'est jamais bloqué et l'écran verrouillé propose toujours de se reconnecter avec le mot de passe. En option (désactivé par défaut, avec un avertissement visible), la clé qui scelle la session enregistrée peut être liée au déverrouillage du téléphone ; la surveillance des alarmes en arrière-plan attend alors que vous déverrouilliez le téléphone après un redémarrage.
* **Moniteur de caméras :** de 1 à 16 tuiles, une vue agrandie, MJPEG en direct qui garde le rapport d'image, une télécommande PTZ bornée, captures et enregistrements, avec visionneuse et confirmation de suppression des enregistrements.
* **Armer et désarmer,** après une **vérification avant armement** (ce qui est ouvert, muet ou en panne) et avec le PIN pour désarmer ; **alarmes** à acquitter, avec un badge pour celles en attente ; **appareils** (fumée, gaz, inondation, porte, fenêtre, mouvement, climat, prises, lumières, sirènes, serrures, volets, moteurs de portail et de garage, chauffe-eau) avec leur état et Allumer / Éteindre / Basculer.
* **Des alarmes qui vous atteignent :** un son pour chaque gravité, une **alarme parlée** facultative, des notifications pour un nœud qui passe en HAUT, une caméra muette, une alarme d'appareil et (armé) un nœud hors ligne, et **une centrale qui sonne réveille le téléphone** ; la veille en arrière-plan survit à un redémarrage et lève le pied quand le serveur est en panne.
* **Radar en direct, en 2D et 3D :** l'onglet Radar dessine le site tel que conçu dans Studio et les personnes que voient les radars s'y déplacer, rafraîchi toutes les secondes et demie ; faites glisser, pincez et tournez la vue 3D.
* **Énergie solaire et électrique :** les totaux (soleil, consommation, batteries avec leur charge, présence du réseau), chaque onduleur et batterie avec les cellules à la demande, et les canaux et alarmes des nœuds électriques.
* **Centrales d'alarme :** l'état de chaque nœud ARMOR-NODE-ALARM, ses zones et événements, et des commandes d'armement / désarmement quand le serveur les permet.
* **Réseau :** les appareils du réseau de la maison, l'état d'internet et l'**adresse publique** avec le fournisseur et le lieu, comme les rapporte le nœud réseau.
* **Configurer un nœud de terrain en Bluetooth** (depuis l'écran de connexion ou *Plus > Configurer un nœud*) : trouve les nœuds qui annoncent `ARMOR-xxxxxx`, crée l'administrateur d'un nouveau ou se connecte (avec le PIN du nœud), cherche les réseaux Wi-Fi et règle le nom du nœud, le Wi-Fi d'un routeur ou une adresse fixe et le broker ; un **chercheur de nœuds** liste ceux déjà sur le réseau.
* **L'assistant :** commandes écrites et parlées (liste fermée, en huit langues, avec une confirmation liée à vous) pour demander l'état de la maison ou armer, désarmer, faire taire et allumer ou éteindre les lumières.
* **Bibliothèque de preuves,** état du périmètre et des nœuds, un **historique** de chaque alerte, nœud, caméra, appareil, alarme et changement de mode, la **carte météo**, et les **services** et mises à jour de l'installation.
* **Huit langues** (anglais, espagnol, allemand, français, italien, japonais, chinois et portugais), choisies dans *Plus > Réglages* ou suivant le téléphone ; on vérifie que chaque phrase est dans les huit tables.
* **Prudence avec le mot de passe :** le HTTP en clair n'est permis que vers un *littéral* IPv4 de LAN privé ou de boucle locale ; un nom d'hôte qui ressemble seulement à une adresse privée (`10.attacker.example`) ou une adresse avec un zéro initial est refusé. L'apparence est faite d'icônes : surfaces quasi noires, accent cyan, ambre pour l'attention.
* **La sécurité depuis le téléphone :** le second facteur et ses codes de récupération, les sessions ouvertes, une vérification de la façon dont le serveur voit le téléphone, la nouvelle preuve d'identité pour les actions critiques depuis l'extérieur et, pour un administrateur, le VPN (appareils avec leur configuration) et le nom DNS dynamique.
* **Tout le système sur l'écran d'état et l'entrée depuis l'extérieur :** l'écran d'état résume les centrales d'alarme, les services, les caméras qui enregistrent et la sécurité et l'accès à distance, chaque carte ouvrant son écran ; et quand l'adresse saisie est hors de la maison et sans https, la connexion dit pourquoi elle ne peut pas continuer et un guide explique les deux voies sûres (VPN, ou adresse publique avec https).
* **Santé des nœuds et modes d'armement :** un écran Santé des nœuds dans Plus (durée de marche, motif du redémarrage, mémoire, liaison et signal, connexions au broker, redémarrages, dernière erreur et avertissements du serveur de chaque nœud) et, sur l'écran des Centrales d'alarme, un sélecteur de mode (Absent, Présent, Nuit et les vôtres) qui arme une centrale dans le mode choisi quand son micrologiciel les connaît. Huit langues.
* **Connexions dans l'historique :** l'écran Historique a une seconde liste, en lecture seule, avec les appareils et applications qui se connectent au serveur (Studio, cette appli, les panneaux des nœuds, le service vocal), la dernière fois que chacun a été vu, ses sessions ouvertes, ses connexions et ses refus ; l'appli dit maintenant au serveur ce qu'elle est pour apparaître sous son nom. Les adresses ne sont visibles que des administrateurs.
* **Maintenance des batteries (administrateurs) :** les opérations simples sur une batterie Pylontech - horloge, compteurs et journaux, redémarrage, capacité, test MOSFET, défaut de fusible, sorties - en deux étapes comme dans Studio (le serveur fait lire la batterie par le nœud, l'écran montre exactement ce qui sera fait, puis "Le faire maintenant" avec le numéro de série saisi de nouveau), avec le résultat et ce qui a changé ; les limites, le firmware et la console expert restent dans Studio.
* **Commande des nœuds (administrateurs) :** Plus > Contrôle des nœuds offre les mêmes opérations que Studio - redémarrer, mettre en pause, reprendre, mettre en veille (travail arrêté, reste connecté), identifier, diagnostic et maintenance activée ou désactivée - à un nœud ou à tous, en demandant de saisir de nouveau le nom du nœud (ou le mot RESTART, PAUSE ou STANDBY pour tous) et la nouvelle preuve d'identité, en montrant où en est chaque nœud et en avertissant qu'une centrale d'alarme ou un radar en pause ou en veille laisse la maison sans protection. Il n'existe ni réinitialisation d'usine, ni effacement, ni sommeil profond.
* **Une fenêtre d'alarme dans l'appli ouverte :** tant qu'une alarme attend quelqu'un, une bannière pulse au-dessus de tous les écrans sauf celui des alarmes (rouge et rapide pour une critique, ambre pour les autres, fixe si le téléphone a les animations coupées), dit quelle alarme est la pire et combien attendent, et laisse utiliser l'appli en dessous ; elle peut ouvrir les alarmes, confirmer depuis la bannière ou être fermée jusqu'à l'arrivée d'une autre alarme.
* **Depuis l'extérieur :** deux adresses (la privée sur le Wi-Fi de la maison, celle de l'extérieur avec les données mobiles ou le VPN) choisies selon où est le téléphone, l'autre étant essayée si l'une ne répond pas, avec un message qui dit ce qui échoue ; la clé du certificat de l'installation est retenue la première fois (ou appairée avec le texte du QR de Studio) et une autre est refusée, et le http simple est refusé pour un serveur déjà joint en https ; le panneau d'un nœud peut s'ouvrir via le serveur ; les alarmes peuvent arriver en push de données seules, annoncées une fois qu'elles viennent du push ou de la surveillance ; l'app ouverte et la surveillance partagent une lecture du serveur ; les flux des caméras s'arrêtent hors de l'écran et reviennent avec des attentes croissantes.
* **Des notices à votre mesure, avec des sons et une voix à vous :** dans les réglages, couper toutes les notices, les afficher sans son ni vibration (et sans les dire à voix haute) et les désactiver par gravité (haute, basse) ou par type (alertes radar, caméras qui ne répondent pas, nœuds hors ligne ou muets, et les alarmes des appareils, du solaire, de l'électrique, du réseau et des panneaux d'alarme) ; une alarme critique notifie toujours sauf si toutes les notices sont coupées. Un son pour chaque gravité et chaque type de notice, pris parmi les sons du téléphone ou dans un fichier à vous (moins de 3 Mo), chacun avec un bouton d'écoute ; et la voix qui dit les alarmes (femme, homme ou indifférent ; enfant, adulte ou senior ; neutre, héros d'action ou seigneur obscur ; vitesse ; et si les notices de gravité basse sont dites aussi) avec un bouton d'essai.
* **Une bannière qui mène au bon écran et une surveillance plus calme :** la bannière d'une alarme ouvre l'écran qui la traite (caméras, appareils, onduleurs ou batteries, l'écran électrique, le réseau ou les panneaux d'alarme) ; le téléphone indique sa langue au serveur quand il s'inscrit au push pour que la notice soit écrite dans cette langue, et un nouveau jeton Firebase arrive tout de suite au serveur depuis l'arrière-plan. Une caméra à deux objectifs dans un seul flux fait deux fenêtres de la liste des caméras. Tant que les alertes push fonctionnent, la surveillance en arrière-plan interroge le serveur toutes les 120 s au lieu de 10 (*Réglages > Surveillance avec alertes push* : 10, 60, 120, 300 ou 600 s).""",
      "role": r"""ARMOR-ANDROID-CONTROL est la fenêtre du téléphone sur le même [ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER) qu'utilise [ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) : il lit et ordonne par lui et rien d'autre. C'est là que les alarmes vous suivent (une centrale qui sonne réveille le téléphone), que vous interrogez l'assistant à la voix, et l'outil pour configurer un nouveau nœud en Bluetooth sur le terrain, à côté de lui.

| Nom | Comment | À quoi ça sert |
|---|---|---|
| ARMOR-SERVER | HTTP `/api/v1` (55 paths), MJPEG | Tout ce que l'app lit et commande |
| Nœuds de terrain | Bluetooth (`ARMOR-xxxxxx`) | Configure un nouveau nœud à côté de lui |
| GitHub | HTTPS | Vérifie et télécharge la mise à jour signée de l'app elle-même |
| Open-Meteo | HTTPS | Les prévisions, la qualité de l'air et la recherche de lieu publiques de la carte météo |""",
      "architecture": r"""<p align="center">
  <img src="images/architecture.svg" alt="Architecture de ARMOR-ANDROID-CONTROL : qui l'appelle, ce qu'il contient et de quoi il dépend" width="100%">
</p>""",
      "security": r"""| Menace | Défense |
|---|---|
| Un mot de passe gardé sur le téléphone | Seulement avec *Se souvenir de moi* (désactivé par défaut) : utilisateur et mot de passe scellés par une clé Keystore propre, pour ce serveur seulement, oubliés dès que vous décochez ; pas de sauvegarde (`allowBackup=false`) |
| HTTP en clair vers Internet | Autorisé seulement vers un *littéral* IPv4 de réseau privé ou loopback ; un hôte comme `10.attacker.example` ou une adresse avec zéro initial (`010.0.0.1` se lit en octal) est refusé ; le http en clair est refusé pour un hôte atteint en https |
| Un homme du milieu en https | La confiance, ce sont les autorités du système plus celles que vous avez installées ; la clé du certificat de l'installation est mémorisée la première fois (ou appariée avec le texte du QR de Studio) et une autre est refusée |
| Un ordre critique avec le téléphone en d'autres mains | L'empreinte, le visage ou le PIN du téléphone avant d'armer, désarmer, couper une sirène, déverrouiller et les autres ordres critiques (actif par défaut seulement si le téléphone a une empreinte ou un visage) ; l'administrateur peut l'exiger depuis Studio, jamais abaisser votre choix ; un téléphone sans verrouillage n'est jamais exclu |
| Un lecteur change quelque chose | Le rôle *lecteur* voit tout mais tout bouton qui change quelque chose est désactivé (tests de rôle) |
| Un mauvais PIN de désarmement | Le PIN n'est envoyé au serveur que pour désarmer ; `wrong_pin`, `pin_locked`, `pin_not_set` et `elevation_required` sont traduits en mots simples |
| Une fausse mise à jour de l'app | Les SHA-256 des certificats de signature (historique) de l'app installée et du candidat sont comparés avant d'appeler l'installateur d'Android ; s'ils n'en partagent aucun, c'est dit clairement |
| Une alarme que le téléphone ne voit pas | Un service au premier plan (`AlarmWatcherService`) interroge toutes les 10 s, attend 15 s le déverrouillage, espace jusqu'à 60 s, dit *injoignable* après 6 échecs, survit au redémarrage ; une alarme de plus de 15 minutes n'est pas annoncée |
| Un mot de passe de caméra sur le téléphone | Les caméras se voient par le flux du serveur : l'app n'a ni mot de passe de caméra ni adresse RTSP |

### Autorisations

`INTERNET`, `ACCESS_NETWORK_STATE` : le serveur. `USE_BIOMETRIC` : le verrouillage du téléphone. `POST_NOTIFICATIONS` : les alarmes. `FOREGROUND_SERVICE` (+ `DATA_SYNC`, `SPECIAL_USE`) et `RECEIVE_BOOT_COMPLETED` : la surveillance des alarmes. `REQUEST_INSTALL_PACKAGES` : la mise à jour de l'app. `BLUETOOTH_SCAN`, `BLUETOOTH_CONNECT` : la configuration d'un nœud ; `BLUETOOTH`, `BLUETOOTH_ADMIN` et `ACCESS_FINE_LOCATION` seulement jusqu'à Android 11 (`maxSdkVersion=30`), pour la recherche Bluetooth.

Il n'y a pas eu de revue de sécurité indépendante. Lisez [docs/CLIENT_BOUNDARY.md](docs/CLIENT_BOUNDARY.md) et [SECURITY.md](SECURITY.md).""",
      "interfaces": r"""| Partie | Ce qu'elle règle |
|---|---|
| ARMOR-SERVER | 55 chemins distincts de `/api/v1` dans `network/ArmorApiClient.kt` (l'interface est `network/ArmorApi.kt`) ; le radar est lu toutes les 1,5 s ; les caméras en MJPEG via le serveur |
| Deux adresses | La privée sur le Wi-Fi de la maison et celle pour l'extérieur (données mobiles ou VPN), choisies selon l'endroit où se trouve le téléphone ; si l'une est muette l'autre est essayée et le message dit ce qui échoue |
| Bluetooth | Trouve les nœuds qui annoncent `ARMOR-xxxxxx`, crée l'administrateur d'un nouveau ou se connecte avec le PIN du nœud, cherche les réseaux Wi-Fi et règle le nom, le Wi-Fi ou une adresse fixe et le broker ; le protocole est `model/NodeBle.kt` ; un chercheur de nœuds liste ceux déjà sur le réseau |
| Voix | `POST /api/v1/voice/command` : une liste fermée de commandes en huit langues, avec une confirmation liée à vous (`model/Voice.kt`, `VoiceScreens.kt`) |
| Push | `PushService` : alarmes en messages de données seules, annoncées une fois qu'elles arrivent par push ou par la surveillance ; les étapes Firebase sont dans [docs/PUSH_NOTIFICATIONS.md](docs/PUSH_NOTIFICATIONS.md) (huit langues) |""",
      "configuration": r"""| Nom | Valeur | Ce qu'elle règle |
|---|---|---|
| `compileSdk` / `targetSdk` / `minSdk` | 37 / 37 / 26 | Android 8.0 ou plus récent sur le téléphone |
| `versionName` | = `armor.project.json` | Le build échoue si le manifeste et la version diffèrent |
| JDK / Android SDK | 17+ / 37 | Pour compiler l'app et lancer les tests |

Dans l'app (pas dans des fichiers) : la langue (les huit ou suivre le téléphone), les deux adresses, *Se souvenir de moi*, le verrouillage du téléphone, l'alarme parlée et les notifications, dans *Plus > Réglages*. Limites dans le code : la surveillance interroge toutes les 10 s, s'espace jusqu'à 60 s et ignore les alarmes de plus de 15 minutes.""",
      "quickstart": r"""**Prérequis:** JDK 17+, le SDK Android (compile SDK 37), un téléphone Android 8.0+ (minSdk 26).

```powershell
.\gradlew.bat testDebugUnitTest assembleDebug   # 367 tests, then the debug APK
adb install -r app\build\outputs\apk\debug\app-debug.apk
```

Les versions sont publiées sur GitHub, d'où l'application cherche elle-même les mises à jour ; l'APK est signé avec la clé de publication propre du responsable, conservée hors du dépôt, et l'application compare le certificat de signature d'un téléchargement avec le sien avant de passer le fichier à l'installateur d'Android. Voir la [frontière du client](docs/CLIENT_BOUNDARY.md).""",
      "testing": r"""```powershell
.\gradlew.bat testDebugUnitTest
python -I tools/armor_ci_validate.py
```

| Partie | Tests | Ce qu'il couvre |
|---|---|---|
| Alarmes | 67 | `AlarmPolicy`, `AlarmBanner`, `AlarmPanels`, `AlarmCodes`, `AlarmRoute`, `NoticeFilter`, `PushEvents`, `DevicesAndAlarms` |
| Lien avec le serveur, analyse, données de test | 59 | `ApiClient`, `ApiError`, `ServerFixtures`, `ParsersTolerant`, `SavePayload`, `JsonText`, `Preflight`, `SharedFeed`, `Connections` |
| Modèle de vue et rôles | 41 | `ArmorViewModel`, `Viewer`, `ArmProfiles`, `NodeCensus`, `NodeHealth` |
| Verrouillage, coffre de session, clés | 38 | `DeviceLock`, `SessionVault`, `CredentialVault`, `KeyBinding`, `Security` |
| Sécurité des adresses, certificats | 32 | `ServerEndpoint`, `ServerAddresses`, `Literals`, `NodeAddress`, `CertificatePins`, `RemoteAccess` |
| Énergie et réseau | 34 | `Solar`, `Battery`, `Electrical`, `Network` |
| Nœuds par Bluetooth, contrôle des nœuds | 26 | `NodeBle`, `NodeControl` |
| Mises à jour depuis GitHub | 17 | `GitHubReleaseUpdaterHttpFailure`, `SignerCheck`, `SemanticVersion`, `ReleaseMetadataParser` |
| Radar et caméras | 14 | `RadarGeometry`, `CameraTraits`, `CameraLenses` |
| Traductions, mots simples, voix | 14 | `Tr`, `Friendly`, `Voice` |

367 tests dans 47 fichiers, lancés avec `testDebugUnitTest` ; un faux serveur (`FakeServer.kt`) et des données prises sur un vrai serveur (`tools/capture_fixtures.mjs`) les alimentent. On vérifie que chaque phrase figure dans les huit tables de langue.""",
      "build": "Les versions sont publiées sur GitHub, d'où l'app vérifie elle-même les mises à jour ; l'app cherche l'élément `ARMOR-ANDROID-CONTROL-release.apk`. L'APK est signé avec la clé de version propre au mainteneur, gardée hors du dépôt, et l'app compare le certificat de signature d'un téléchargement au sien avant de passer le fichier à l'installateur d'Android. Le `versionCode` monte avant chaque APK, sinon Android ne le traite pas comme une mise à jour.",
      "troubleshooting": r"""| Vous voyez | Parce que | Faites |
|---|---|---|
| `wrong_pin`, `pin_locked`, `pin_not_set`, `elevation_required` | Le serveur refuse le PIN de désarmement ou demande une preuve d'identité récente | Saisissez de nouveau le PIN, attendez la fin du blocage ou confirmez votre identité |
| La connexion dit qu'elle ne peut pas continuer | L'adresse est hors de la maison et n'a pas de https (le http en clair est refusé) | Suivez le guide : un VPN, ou une adresse publique avec https |
| La connexion est refusée alors qu'elle marchait | La clé du certificat de l'installation a changé | Appariez de nouveau avec le texte du QR de Studio si vous l'avez changé exprès |
| Les alarmes arrivent en retard ou pas du tout en arrière-plan | Les règles de batterie du fabricant arrêtent la surveillance ; le push exige un projet Firebase propre | Exemptez l'app des économies de batterie ; suivez [docs/PUSH_NOTIFICATIONS.md](docs/PUSH_NOTIFICATIONS.md) |
| La mise à jour est refusée | Le certificat de signature du téléchargement n'en partage aucun avec l'app installée | Ne l'installez pas ; prenez l'APK dans les versions de ce dépôt |""",
      "structure": r"""<p align="center">
  <img src="images/repository-structure.svg" alt="Structure du dépôt de ARMOR-ANDROID-CONTROL" width="100%">
</p>

<details>
<summary>Version texte de l'arborescence</summary>

```text
ARMOR-ANDROID-CONTROL/
├── app/src/main/java/es/electrohobby3d/armor/   l'app : écrans, règles, réseau et mises à jour
├── app/src/main/assets/                         huit tables de langue, codes d'alarme, carte météo
├── app/src/test/                                367 tests et un faux serveur
├── docs/                                        les guides de ce dépôt
├── tools/                                       les contrôles CI partagés et les outils du projet
├── .github/                                     workflow CI et modèles d'issues et de pull requests
├── images/                                      bannière, icône et les deux images de ce README
├── build.sh build.bat                           build par le flux de projet partagé
├── test.sh test.bat                             lancer les tests par le flux partagé
├── run.sh run.bat                               démarrer par le flux de projet partagé
├── armor.project.json                           manifeste : version, rôle, maturité, commande de build
├── CHANGELOG.md                                 ce qui a changé à chaque version
├── SECURITY.md SUPPORT.md LICENSE               politique de sécurité, support et licence
├── CONTRIBUTING.md CODE_OF_CONDUCT.md           comment contribuer et le code de conduite
├── build.gradle.kts settings.gradle.kts         le build Gradle du projet
├── gradle.properties                            réglages Gradle
├── gradlew gradlew.bat gradle/                  l'enveloppe Gradle
├── build-test.sh build-test.bat                 lancer les tests par le flux partagé
└── .gitattributes .gitignore                    réglages Git
```

</details>""",
      "roadmap": r"""**Limites connues aujourd'hui**

* Les écrans solaire, électrique et centrale d'alarme n'ont pas connu de vrai matériel (seul un nœud radar existe).
* La configuration Bluetooth d'un nœud n'a pas été confirmée avec un vrai nœud, et le push via Firebase n'a pas été essayé sur un téléphone.
* La surveillance des alarmes en arrière-plan sous les règles de batterie de chaque fabricant n'est pas prouvée.
* Pas de revue de sécurité indépendante.

**Ensuite**

* Essayer les écrans solaire, électrique et centrale d'alarme avec de vrais nœuds, et la configuration Bluetooth avec un vrai nœud.
* Essayer le push via Firebase avec le projet propre d'une installation, et la surveillance des alarmes chez plusieurs fabricants.""",
    },
  },
  "it": {
    "tagline": "Client mobile da operatore per ARMOR-SERVER: allarmi, telecamere, radar, energia, la rete e la configurazione dei nodi, in otto lingue",
    "honest": "Le regole di sicurezza dell'indirizzo, di decisione degli allarmi, del guardiano degli allarmi, di traduzione e del ruolo di sola lettura sono coperte da 367 test unitari e l'app si compila (`gradlew testDebugUnitTest assembleDebug`). Funziona su un vero telefono contro il banco di prova CM5: l'accesso, il monitor delle telecamere, l'inserimento e gli allarmi, il radar, la configurazione di un nodo via Bluetooth e gli aggiornamenti da GitHub sono in uso. Ciò che **non** è ancora provato: le schermate solare, elettrica e delle centrali d'allarme con apparecchi reali (esiste solo un nodo radar), il push tramite Firebase (è nell'app e richiede un progetto Firebase proprio; non è ancora stato provato su un telefono) e la sorveglianza degli allarmi in background sotto le regole di batteria di ogni produttore.",
    "glance": [
      [
        "Ruolo",
        "Client operatore Android per ARMOR-SERVER (famiglia: Clients, padre: ARMOR-SERVER)",
      ],
      [
        "Tecnologia",
        "Kotlin / Jetpack Compose, Android 8.0+",
      ],
      [
        "Test",
        "367 (`gradlew testDebugUnitTest`)",
      ],
      [
        "Lingue",
        "8 (1345 frasi per lingua, ogni frase verificata in tutte le tabelle)",
      ],
      [
        "Gira su",
        "Un telefono con Android 8.0+ (minSdk 26)",
      ],
      [
        "Su hardware reale",
        "Usata su un vero telefono contro il banco di prova CM5; le schermate solare, elettrica e delle centrali d'allarme attendono nodi reali",
      ],
      [
        "Licenza",
        "GPL-3.0-or-later",
      ],
    ],
    "status": {
      "software": "L'app compila (`gradlew testDebugUnitTest assembleDebug`) e gira su un telefono reale contro il banco di prova CM5.",
      "tests": "Superano 367 test unitari (`gradlew testDebugUnitTest`): sicurezza degli indirizzi, decisione di allarme, sorvegliante degli allarmi, traduzioni e ruolo di sola lettura.",
      "ui": "L'accesso, il monitor delle telecamere, l'inserimento e gli allarmi e il radar sono in uso su un telefono reale; la configurazione di un nodo via Bluetooth non è stata confermata con un nodo reale e le schermate solare, elettrica e della centralina d'allarme non hanno incontrato apparecchiature reali.",
      "hardware": "Usata su un telefono reale contro il banco di prova CM5; la sorveglianza degli allarmi in background con le regole di batteria di ogni produttore non è provata.",
      "security": "Le regole di sicurezza degli indirizzi e del ruolo di sola lettura sono coperte da test unitari; non c'è stata una revisione indipendente.",
      "updates": "Gli aggiornamenti da GitHub sono in uso sul telefono.",
      "integration": "Il push tramite Firebase è nell'app ma richiede un progetto Firebase proprio e non è stato provato su un telefono.",
      "docs": "Otto lingue e il registro delle modifiche sono aggiornati.",
    },
    "docs": [
      "[Confini del client](docs/CLIENT_BOUNDARY.md): cosa fa e non fa mai il client",
      "[Notifiche push](docs/PUSH_NOTIFICATIONS.md): i passi di Firebase, in otto lingue",
      "[Prove al banco](docs/BENCH_TESTS.md): verifiche con un telefono reale",
    ],
    "contributing_first": "Prima di una pull request esegui `.\\gradlew.bat testDebugUnitTest` and `python -I tools/armor_ci_validate.py`: deve passare. Vedi [CONTRIBUTING.md](CONTRIBUTING.md) e il [codice di condotta](CODE_OF_CONDUCT.md).",
    "languages_extra": "",
    "body": {
      "overview": r"""* **Accesso con il login del server stesso:** IP, porta, utente e password; la password crea una sessione HttpOnly; viene memorizzata sul telefono solo se spunti **Ricordami** (disattivato per impostazione predefinita: utente e password sigillati con una chiave propria del Keystore, solo per quel server, dimenticati appena togli la spunta). Un ruolo **viewer** guarda soltanto: ogni pulsante che cambia qualcosa è spento.
* **Blocco con il telefono:** l'app chiede impronta, volto o PIN del telefono stesso prima di inserire, disinserire, silenziare una sirena, sbloccare e per gli altri ordini critici (attivo per impostazione predefinita solo se il telefono ha impronta o volto) e, se lo attivi, per aprire l'app. Il tuo amministratore può richiederlo da Studio ma mai abbassare ciò che hai scelto; un telefono senza blocco schermo non viene mai lasciato fuori e la schermata bloccata offre sempre di accedere di nuovo con la password. In via facoltativa (disattivata per impostazione predefinita, con un avviso ben visibile) la chiave che sigilla la sessione salvata può essere legata allo sblocco del telefono; in tal caso la sorveglianza degli allarmi in background, dopo un riavvio, attende che tu sblocchi il telefono.
* **Monitor delle telecamere:** da 1 a 16 riquadri, una vista ingrandita, MJPEG dal vivo che mantiene il rapporto dell'immagine, una pulsantiera PTZ limitata, istantanee e registrazioni, con visualizzatore e conferma di cancellazione delle registrazioni.
* **Inserire e disinserire,** dopo un **controllo prima di inserire** (cosa è aperto, muto o fermo) e con il PIN per disinserire; **allarmi** da riconoscere, con un badge per quelli in attesa; **dispositivi** (fumo, gas, allagamento, porta, finestra, movimento, clima, prese, luci, sirene, serrature, tapparelle, motori di cancello e garage, scaldabagni) con il loro stato e Accendi / Spegni / Alterna.
* **Allarmi che ti raggiungono:** un suono per ogni gravità, un **allarme parlato** facoltativo, notifiche per un nodo che arriva ad ALTO, una telecamera muta, un allarme di dispositivo e (a impianto inserito) un nodo offline, e **una centrale che suona sveglia il telefono**; la sorveglianza in background sopravvive a un riavvio e rallenta quando il server è fermo.
* **Radar dal vivo, in 2D e 3D:** la scheda Radar disegna il sito come progettato in Studio e le persone che i radar vedono muoversi su di esso, aggiornato ogni secondo e mezzo; trascina, pizzica e ruota la vista 3D.
* **Energia solare ed elettrica:** i totali (sole, consumo, batterie con la loro carica, se c'è la rete), ogni inverter e batteria con le celle a richiesta, e i canali e gli allarmi dei nodi elettrici.
* **Centrali d'allarme:** lo stato di ogni nodo ARMOR-NODE-ALARM, le sue zone ed eventi, e comandi di inserimento / disinserimento quando il server li consente.
* **Rete:** i dispositivi della rete della casa, lo stato di internet e l'**indirizzo pubblico** con il fornitore e il luogo, come li riferisce il nodo di rete.
* **Configurare un nodo di campo via Bluetooth** (dalla schermata di accesso o *Altro > Configura un nodo*): trova i nodi che annunciano `ARMOR-xxxxxx`, crea l'amministratore di uno nuovo o entra (con il PIN del nodo), cerca reti Wi-Fi e imposta il nome del nodo, il Wi-Fi di un router o un indirizzo fisso e il broker; un **cercatore di nodi** elenca quelli già in rete.
* **L'assistente:** comandi scritti e parlati (elenco chiuso, in otto lingue, con una conferma legata a te) per chiedere lo stato della casa o inserire, disinserire, tacitare e accendere o spegnere le luci.
* **Libreria delle prove,** stato del perimetro e dei nodi, uno **storico** di ogni allarme, nodo, telecamera, dispositivo, allarme e cambio di modalità, la **mappa meteo**, e i **servizi** e gli aggiornamenti dell'impianto.
* **Otto lingue** (inglese, spagnolo, tedesco, francese, italiano, giapponese, cinese e portoghese), scelte in *Altro > Impostazioni* o seguendo il telefono; si controlla che ogni frase sia nelle otto tabelle.
* **Attenzione alla password:** l'HTTP in chiaro è ammesso solo verso un *letterale* IPv4 di LAN privata o loopback; un nome host che inizia soltanto come un indirizzo privato (`10.attacker.example`) o un indirizzo con zero iniziale è rifiutato. L'aspetto è fatto di icone: superfici quasi nere, accento ciano, ambra per l'attenzione.
* **La sicurezza dal telefono:** il secondo fattore e i suoi codici di recupero, le sessioni aperte, un controllo di come il server vede il telefono, la nuova prova di identità per le azioni critiche da fuori e, per un amministratore, la VPN (dispositivi con la loro configurazione) e il nome DNS dinamico.
* **Tutto il sistema nella schermata di stato e l'ingresso da fuori:** la schermata di stato riassume le centrali d'allarme, i servizi, le telecamere che registrano e la sicurezza e l'accesso remoto, ogni scheda apre la sua schermata; e quando l'indirizzo scritto è fuori casa e senza https, l'accesso dice perché non può proseguire e una guida spiega le due vie sicure (VPN, o indirizzo pubblico con https).
* **Salute dei nodi e modalità di inserimento:** una schermata Salute dei nodi in Altro (tempo acceso, motivo del riavvio, memoria, collegamento e segnale, connessioni al broker, riavvii, ultimo errore e avvisi del server per ogni nodo) e, nella schermata delle Centrali d'allarme, un selettore di modalità (Fuori casa, In casa, Notte e le tue) che inserisce una centrale nella modalità scelta quando il suo firmware le conosce. Otto lingue.
* **Connessioni nella cronologia:** la schermata Cronologia ha un secondo elenco, di sola lettura, con i dispositivi e le app che si collegano al server (Studio, questa app, i pannelli dei nodi, il servizio vocale), quando ciascuno è stato visto l'ultima volta, le sue sessioni aperte, gli accessi e i rifiuti; l'app ora dice al server cos'è per comparire come se stessa. Gli indirizzi li vedono solo gli amministratori.
* **Manutenzione delle batterie (amministratori):** le operazioni semplici su una batteria Pylontech - orologio, contatori e registri, riavvio, capacità, test MOSFET, guasto al fusibile, uscite - nei due passi di Studio (il server fa leggere la batteria al nodo, la schermata mostra esattamente cosa verrà fatto, poi "Esegui ora" con il numero di serie digitato di nuovo), con il risultato e cosa è cambiato; limiti, firmware e console esperto restano in Studio.
* **Controllo dei nodi (amministratori):** Altro > Controllo dei nodi offre le stesse operazioni di Studio - riavvio, pausa, ripresa, standby (lavoro spento, resta connesso), identificazione, diagnostica e manutenzione attivata o disattivata - a un nodo o a tutti, chiedendo di digitare di nuovo il nome del nodo (o la parola RESTART, PAUSE o STANDBY per tutti) e la nuova prova di identità, mostrando a che punto è ogni nodo e avvisando che una centrale d'allarme o un radar in pausa o in standby lascia la casa senza protezione. Non esistono ripristino di fabbrica, cancellazione né sonno profondo.
* **Una finestra di allarme nell'app aperta:** finché un allarme aspetta una persona, un banner sopra tutte le schermate tranne quella degli allarmi pulsa (rosso e veloce per un critico, ambra per gli altri, fermo se il telefono ha le animazioni spente), dice qual è l'allarme peggiore e quanti aspettano, e lascia usare l'app sotto; può aprire gli allarmi, confermare dal banner o essere chiuso finché non arriva un altro allarme.
* **Da fuori casa:** due indirizzi (quello privato sul Wi-Fi di casa, quello per fuori con i dati mobili o la VPN) scelti secondo dove si trova il telefono, provando l'altro se uno non risponde e con un messaggio che dice cosa non va; la chiave del certificato dell'installazione viene ricordata la prima volta (o associata con il testo del QR di Studio) e una diversa viene rifiutata, e l'http semplice è rifiutato per un server già raggiunto in https; il pannello di un nodo si può aprire tramite il server; gli allarmi possono arrivare come push di soli dati, annunciati una volta sia che arrivino dal push sia dalla sorveglianza; l'app aperta e la sorveglianza condividono una lettura del server; i flussi delle telecamere si fermano fuori schermo e tornano con attese crescenti.
* **Avvisi a tua scelta, con suoni e una voce tuoi:** nelle impostazioni si possono silenziare tutti gli avvisi, mostrarli senza suono né vibrazione (e senza dirli ad alta voce) e disattivarli per gravità (alta, bassa) o per tipo (avvisi radar, telecamere che non rispondono, nodi offline o muti, e gli allarmi di dispositivi, solare, elettrico, rete e pannelli di allarme); un allarme critico avvisa sempre, salvo che tutti gli avvisi siano silenziati. Un suono per ogni gravità e per ogni tipo di avviso, dai suoni del telefono o da un file tuo (sotto i 3 MB), ciascuno con un pulsante di riproduzione; e la voce che dice gli allarmi (donna, uomo o indifferente; bambino, adulto o anziano; neutra, eroe d'azione o signore oscuro; velocità; e se vengono detti anche gli avvisi di gravità bassa) con un pulsante di prova.
* **Un banner che porta alla schermata giusta e una sorveglianza più tranquilla:** il banner di un allarme apre la schermata che lo gestisce (telecamere, dispositivi, inverter o batterie, la schermata elettrica, la rete o i pannelli di allarme); il telefono dice la propria lingua al server quando si registra al push, così l'avviso è scritto in essa, e un nuovo token Firebase arriva subito al server dallo sfondo. Una telecamera con due obiettivi in un solo flusso sono due finestre dell'elenco telecamere. Finché gli avvisi push funzionano, la sorveglianza in background interroga il server ogni 120 s invece di ogni 10 (*Impostazioni > Sorveglianza con avvisi push*: 10, 60, 120, 300 o 600 s).""",
      "role": r"""ARMOR-ANDROID-CONTROL è la finestra del telefono sullo stesso [ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER) usato da [ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO): legge e ordina attraverso di esso e nient'altro. È dove gli allarmi ti seguono (una centrale che suona sveglia il telefono), dove interroghi l'assistente a voce, e lo strumento per configurare un nuovo nodo via Bluetooth sul campo, accanto ad esso.

| Nome | Come | A cosa serve |
|---|---|---|
| ARMOR-SERVER | HTTP `/api/v1` (55 paths), MJPEG | Tutto ciò che l'app legge e ordina |
| Nodi di campo | Bluetooth (`ARMOR-xxxxxx`) | Configura un nuovo nodo stando accanto a esso |
| GitHub | HTTPS | Controlla e scarica l'aggiornamento firmato dell'app stessa |
| Open-Meteo | HTTPS | Le previsioni, la qualità dell'aria e la ricerca dei luoghi pubbliche della mappa meteo |""",
      "architecture": r"""<p align="center">
  <img src="images/architecture.svg" alt="Architettura di ARMOR-ANDROID-CONTROL: chi lo chiama, cosa contiene e da cosa dipende" width="100%">
</p>""",
      "security": r"""| Minaccia | Difesa |
|---|---|
| Una password salvata sul telefono | Solo con *Ricordami* (spento di default): utente e password sigillati con una chiave Keystore propria, solo per quel server, dimenticati appena lo togli; nessun backup (`allowBackup=false`) |
| HTTP in chiaro verso Internet | Consentito solo verso un *letterale* IPv4 di rete privata o loopback; un host come `10.attacker.example` o un indirizzo con zero iniziale (`010.0.0.1` si legge ottale) è rifiutato; l'http in chiaro è rifiutato per un host raggiunto via https |
| Un uomo nel mezzo su https | La fiducia sono le autorità del sistema più quelle installate sul telefono; la chiave del certificato dell'installazione è ricordata la prima volta (o associata dal testo del QR di Studio) e una diversa è rifiutata |
| Un ordine critico con il telefono in altre mani | L'impronta, il volto o il PIN del telefono prima di inserire, disinserire, silenziare una sirena, sbloccare e gli altri ordini critici (attivo di default solo se il telefono ha impronta o volto); l'amministratore può imporlo da Studio, mai abbassare la tua scelta; un telefono senza blocco schermo non resta mai escluso |
| Un visualizzatore cambia qualcosa | Il ruolo *visualizzatore* vede tutto ma ogni pulsante che cambia qualcosa è spento (test di ruolo) |
| Un PIN di disinserimento errato | Il PIN va al server solo per disinserire; `wrong_pin`, `pin_locked`, `pin_not_set` ed `elevation_required` sono tradotti in parole semplici |
| Un falso aggiornamento dell'app | Gli SHA-256 dei certificati di firma (storico) dell'app installata e del candidato sono confrontati prima di chiamare l'installer di Android; se non ne condividono nessuno, lo dice chiaramente |
| Un allarme che il telefono non vede | Un servizio in primo piano (`AlarmWatcherService`) interroga ogni 10 s, attende 15 s lo sblocco, rallenta fino a 60 s, dice *irraggiungibile* dopo 6 errori, sopravvive al riavvio; un allarme più vecchio di 15 minuti non viene annunciato |
| Una password di telecamera sul telefono | Le telecamere si vedono dal flusso del server: l'app non ha password di telecamera né indirizzo RTSP |

### Permessi

`INTERNET`, `ACCESS_NETWORK_STATE`: il server. `USE_BIOMETRIC`: il blocco del telefono. `POST_NOTIFICATIONS`: gli allarmi. `FOREGROUND_SERVICE` (+ `DATA_SYNC`, `SPECIAL_USE`) e `RECEIVE_BOOT_COMPLETED`: la sorveglianza degli allarmi. `REQUEST_INSTALL_PACKAGES`: l'aggiornamento dell'app. `BLUETOOTH_SCAN`, `BLUETOOTH_CONNECT`: la configurazione di un nodo; `BLUETOOTH`, `BLUETOOTH_ADMIN` e `ACCESS_FINE_LOCATION` solo fino ad Android 11 (`maxSdkVersion=30`), per la ricerca Bluetooth.

Non c'è stata una revisione di sicurezza indipendente. Leggi [docs/CLIENT_BOUNDARY.md](docs/CLIENT_BOUNDARY.md) e [SECURITY.md](SECURITY.md).""",
      "interfaces": r"""| Parte | Cosa imposta |
|---|---|
| ARMOR-SERVER | 55 percorsi distinti di `/api/v1` in `network/ArmorApiClient.kt` (l'interfaccia è `network/ArmorApi.kt`); il radar si legge ogni 1,5 s; le telecamere in MJPEG tramite il server |
| Due indirizzi | Quella privata sul Wi-Fi di casa e quella per fuori (dati mobili o VPN), scelte in base a dove si trova il telefono; se una tace si prova l'altra e il messaggio dice cosa fallisce |
| Bluetooth | Trova i nodi che annunciano `ARMOR-xxxxxx`, crea l'amministratore di uno nuovo o accede con il PIN del nodo, cerca reti Wi-Fi e imposta il nome, il Wi-Fi o un indirizzo fisso e il broker; il protocollo è `model/NodeBle.kt`; un cercatore di nodi elenca quelli già in rete |
| Voce | `POST /api/v1/voice/command`: una lista chiusa di comandi in otto lingue, con una conferma legata a te (`model/Voice.kt`, `VoiceScreens.kt`) |
| Push | `PushService`: allarmi come messaggi con soli dati, annunciati una volta sia che arrivino via push sia via sorveglianza; i passi di Firebase sono in [docs/PUSH_NOTIFICATIONS.md](docs/PUSH_NOTIFICATIONS.md) (otto lingue) |""",
      "configuration": r"""| Nome | Valore | Cosa imposta |
|---|---|---|
| `compileSdk` / `targetSdk` / `minSdk` | 37 / 37 / 26 | Android 8.0 o successivo sul telefono |
| `versionName` | = `armor.project.json` | La build fallisce se manifesto e versione differiscono |
| JDK / Android SDK | 17+ / 37 | Per compilare l'app ed eseguire i test |

Nell'app (non nei file): la lingua (le otto o seguire il telefono), i due indirizzi, *Ricordami*, il blocco del telefono, l'allarme parlato e le notifiche, in *Altro > Impostazioni*. Limiti nel codice: la sorveglianza interroga ogni 10 s, rallenta fino a 60 s e ignora gli allarmi più vecchi di 15 minuti.""",
      "quickstart": r"""**Requisiti:** JDK 17+, l'SDK Android (compile SDK 37), un telefono con Android 8.0+ (minSdk 26).

```powershell
.\gradlew.bat testDebugUnitTest assembleDebug   # 367 tests, then the debug APK
adb install -r app\build\outputs\apk\debug\app-debug.apk
```

Le versioni sono pubblicate su GitHub, da dove l'app stessa cerca gli aggiornamenti; l'APK è firmato con la chiave di rilascio propria del responsabile, conservata fuori dal repository, e l'app confronta il certificato di firma di un download con il proprio prima di passare il file al programma di installazione di Android. Vedi il [confine del client](docs/CLIENT_BOUNDARY.md).""",
      "testing": r"""```powershell
.\gradlew.bat testDebugUnitTest
python -I tools/armor_ci_validate.py
```

| Parte | Test | Cosa copre |
|---|---|---|
| Allarmi | 67 | `AlarmPolicy`, `AlarmBanner`, `AlarmPanels`, `AlarmCodes`, `AlarmRoute`, `NoticeFilter`, `PushEvents`, `DevicesAndAlarms` |
| Collegamento al server, lettura, dati di prova | 59 | `ApiClient`, `ApiError`, `ServerFixtures`, `ParsersTolerant`, `SavePayload`, `JsonText`, `Preflight`, `SharedFeed`, `Connections` |
| View model e ruoli | 41 | `ArmorViewModel`, `Viewer`, `ArmProfiles`, `NodeCensus`, `NodeHealth` |
| Blocco, deposito sessione, chiavi | 38 | `DeviceLock`, `SessionVault`, `CredentialVault`, `KeyBinding`, `Security` |
| Sicurezza degli indirizzi, certificati | 32 | `ServerEndpoint`, `ServerAddresses`, `Literals`, `NodeAddress`, `CertificatePins`, `RemoteAccess` |
| Energia e rete | 34 | `Solar`, `Battery`, `Electrical`, `Network` |
| Nodi via Bluetooth, controllo dei nodi | 26 | `NodeBle`, `NodeControl` |
| Aggiornamenti da GitHub | 17 | `GitHubReleaseUpdaterHttpFailure`, `SignerCheck`, `SemanticVersion`, `ReleaseMetadataParser` |
| Radar e telecamere | 14 | `RadarGeometry`, `CameraTraits`, `CameraLenses` |
| Traduzioni, parole semplici, voce | 14 | `Tr`, `Friendly`, `Voice` |

367 test in 47 file, eseguiti con `testDebugUnitTest`; un server finto (`FakeServer.kt`) e dati presi da un server reale (`tools/capture_fixtures.mjs`) li alimentano. Si verifica che ogni frase sia nelle otto tabelle di lingua.""",
      "build": "Le versioni sono pubblicate su GitHub, da dove l'app stessa controlla gli aggiornamenti; l'app cerca l'asset `ARMOR-ANDROID-CONTROL-release.apk`. L'APK è firmato con la chiave di rilascio del manutentore, tenuta fuori dal repository, e l'app confronta il certificato di firma di un download con il proprio prima di passare il file all'installer di Android. Il `versionCode` sale prima di ogni APK, altrimenti Android non lo tratta come aggiornamento.",
      "troubleshooting": r"""| Vedi | Perché | Fai |
|---|---|---|
| `wrong_pin`, `pin_locked`, `pin_not_set`, `elevation_required` | Il server rifiuta il PIN di disinserimento o chiede una nuova prova d'identità | Digita di nuovo il PIN, attendi la fine del blocco o conferma la tua identità |
| L'accesso dice che non può proseguire | L'indirizzo è fuori casa e non ha https (l'http in chiaro è rifiutato) | Segui la guida: una VPN, o un indirizzo pubblico con https |
| La connessione è rifiutata dopo aver funzionato | La chiave del certificato dell'installazione è cambiata | Associa di nuovo con il testo del QR di Studio se l'hai cambiato di proposito |
| Gli allarmi arrivano in ritardo o non arrivano in background | Le regole di batteria del produttore fermano la sorveglianza; il push richiede un progetto Firebase proprio | Escludi l'app dal risparmio batteria; segui [docs/PUSH_NOTIFICATIONS.md](docs/PUSH_NOTIFICATIONS.md) |
| L'aggiornamento è rifiutato | Il certificato di firma del download non ne condivide nessuno con l'app installata | Non installarlo; prendi l'APK dalle versioni di questo repository |""",
      "structure": r"""<p align="center">
  <img src="images/repository-structure.svg" alt="Struttura del repository di ARMOR-ANDROID-CONTROL" width="100%">
</p>

<details>
<summary>Versione testuale dell'albero</summary>

```text
ARMOR-ANDROID-CONTROL/
├── app/src/main/java/es/electrohobby3d/armor/   l'app: schermate, regole, rete e aggiornamenti
├── app/src/main/assets/                         otto tabelle di lingua, codici di allarme, mappa meteo
├── app/src/test/                                367 test e un server finto
├── docs/                                        le guide di questo repository
├── tools/                                       i controlli CI condivisi e gli strumenti del progetto
├── .github/                                     workflow CI e modelli per issue e pull request
├── images/                                      banner, icona e le due immagini di questo README
├── build.sh build.bat                           build tramite il flusso di progetto condiviso
├── test.sh test.bat                             eseguire i test tramite il flusso condiviso
├── run.sh run.bat                               avvio tramite il flusso di progetto condiviso
├── armor.project.json                           manifesto: versione, ruolo, maturità, comando di build
├── CHANGELOG.md                                 cosa è cambiato in ogni versione
├── SECURITY.md SUPPORT.md LICENSE               politica di sicurezza, supporto e licenza
├── CONTRIBUTING.md CODE_OF_CONDUCT.md           come contribuire e il codice di condotta
├── build.gradle.kts settings.gradle.kts         la build Gradle del progetto
├── gradle.properties                            impostazioni di Gradle
├── gradlew gradlew.bat gradle/                  il wrapper di Gradle
├── build-test.sh build-test.bat                 eseguire i test tramite il flusso condiviso
└── .gitattributes .gitignore                    impostazioni di Git
```

</details>""",
      "roadmap": r"""**Limiti noti oggi**

* Le schermate di solare, elettrico e centrale di allarme non hanno incontrato apparecchiature reali (esiste solo un nodo radar).
* La configurazione Bluetooth di un nodo non è stata confermata con un nodo reale, e il push via Firebase non è stato provato su un telefono.
* La sorveglianza degli allarmi in background con le regole di batteria di ogni produttore non è dimostrata.
* Nessuna revisione di sicurezza indipendente.

**Prossimi passi**

* Provare le schermate di solare, elettrico e centrale di allarme con nodi reali, e la configurazione Bluetooth con un nodo reale.
* Provare il push via Firebase con il progetto proprio di un'installazione, e la sorveglianza degli allarmi su più produttori.""",
    },
  },
  "ja": {
    "tagline": "ARMOR-SERVER のモバイルオペレータークライアント：警報、カメラ、レーダー、エネルギー、ネットワーク、ノードの設定。8 言語対応",
    "honest": "アドレスの安全性、警報の判断、警報ウォッチャー、翻訳、読み取り専用ロールのルールは 367 件のユニットテストでカバーされ、アプリはビルドできます（`gradlew testDebugUnitTest assembleDebug`）。実際のスマートフォンで CM5 テストベンチに対して動作し、サインイン、カメラモニター、警戒と警報、レーダー、Bluetooth でのノード設定、GitHub からのアップデートが使われています。**まだ**証明されていないもの：実機でのソーラー・電気・警報盤の画面（存在するのはレーダーノードのみ）、Firebase 経由のプッシュ（アプリには入っており、独自の Firebase プロジェクトが必要です。実機ではまだ試していません）、各メーカーのバッテリー規則下でのバックグラウンド警報監視。",
    "glance": [
      [
        "役割",
        "ARMOR-SERVER 用の Android オペレーター向けクライアント（ファミリー：Clients、親：ARMOR-SERVER）",
      ],
      [
        "技術",
        "Kotlin / Jetpack Compose, Android 8.0+",
      ],
      [
        "テスト",
        "367 (`gradlew testDebugUnitTest`)",
      ],
      [
        "言語",
        "8（言語ごとに 1345 フレーズ、すべての表で検査）",
      ],
      [
        "動作環境",
        "Android 8.0+ の電話（minSdk 26）",
      ],
      [
        "実機での確認",
        "実際のスマートフォンで CM5 テストベンチに対して使用。ソーラー・電気・警報盤の画面は実ノードを待っています",
      ],
      [
        "ライセンス",
        "GPL-3.0-or-later",
      ],
    ],
    "status": {
      "software": "アプリはビルドでき（`gradlew testDebugUnitTest assembleDebug`）、実機のスマートフォンで CM5 テストベンチに対して動作しています。",
      "tests": "367 件のユニットテストが通ります（`gradlew testDebugUnitTest`）：接続先の安全性、警報の判定、警報の監視、翻訳、読み取り専用ロール。",
      "ui": "サインイン、カメラモニター、警戒と警報、レーダーは実機のスマートフォンで使われています。Bluetooth でのノード設定は実機のノードではまだ確認しておらず、太陽光・電気・警報パネルの画面も実機の機器とは接続していません。",
      "hardware": "実機のスマートフォンで CM5 テストベンチに対して使っています。各メーカーのバッテリー規則の下でのバックグラウンド警報監視は確認できていません。",
      "security": "接続先の安全性と読み取り専用ロールの規則はユニットテストでカバーされています。独立したレビューはありません。",
      "updates": "GitHub からのアップデートはスマートフォンで使われています。",
      "integration": "Firebase 経由のプッシュはアプリに入っていますが、専用の Firebase プロジェクトが必要で、スマートフォンではまだ試していません。",
      "docs": "8 言語と変更履歴は最新です。",
    },
    "docs": [
      "[クライアントの境界](docs/CLIENT_BOUNDARY.md)：クライアントの役割と禁止事項",
      "[プッシュ通知](docs/PUSH_NOTIFICATIONS.md)：Firebase の手順（8 言語）",
      "[ベンチテスト](docs/BENCH_TESTS.md)：実機での確認",
    ],
    "contributing_first": "Pull Request の前に `.\\gradlew.bat testDebugUnitTest` and `python -I tools/armor_ci_validate.py` を実行してください。通る必要があります。[CONTRIBUTING.md](CONTRIBUTING.md) と[行動規範](CODE_OF_CONDUCT.md)を参照してください。",
    "languages_extra": "",
    "body": {
      "overview": r"""* **サーバー自身のログインでサインイン：**IP、ポート、ユーザー、パスワード。パスワードは HttpOnly セッションを作ります。スマートフォンに保存されるのは **保存する** にチェックしたときだけです（既定はオフ。ユーザー名とパスワードは Keystore の専用鍵で暗号化され、そのサーバー専用で、チェックを外すと直ちに消去されます）。**viewer** ロールは見るだけで、何かを変更するボタンはすべてオフです。
* **端末のロックによる保護：** アプリは、警戒の開始・解除、サイレン停止、解錠などの重要な命令の前に、端末自体の指紋・顔・PINを求めます（指紋または顔認証がある端末でのみ初期設定でオン）。オンにすればアプリを開くときにも求めます。管理者はStudioから必須にできますが、あなたが選んだ設定を下げることはできません。画面ロックのない端末が締め出されることはなく、ロック画面にはいつでもパスワードで再ログインする手段があります。任意で（既定ではオフ、目立つ警告付き）、保存されたセッションを封じる鍵をスマートフォンのロック解除に結び付けられます。その場合、再起動後はロックを解除するまでバックグラウンドの警報監視が待機します。
* **カメラモニター：**1〜16 タイル、拡大表示、縦横比を保つライブ MJPEG、範囲を限った PTZ パッド、スナップショットと録画（録画にはビューアーと削除確認付き）。
* **警戒と解除：**まず**警戒前のチェック**（開いている、無応答、停止しているもの）を行い、解除には PIN。確認する**警報**（待機中のものにはバッジ）、**デバイス**（煙、ガス、浸水、ドア、窓、動き、気候、プラグ、照明、サイレン、鍵、シャッター、門扉・ガレージドアのモーター、給湯器）の状態とオン / オフ / 切り替え。
* **あなたに届く警報：**重大度ごとの音、任意の**音声警報**、ノードが HIGH になった、カメラが無応答、デバイス警報、（警戒中に）ノードがオフラインになった通知、そして**鳴っている警報盤はスマートフォンを起こします**。バックグラウンド監視は再起動後も残り、サーバー停止中は間隔を空けます。
* **ライブレーダー（2D と 3D）：**レーダータブは Studio で設計したサイトと、レーダーが捉えて動く人を描き、1.5 秒ごとに更新します。3D 表示はドラッグ、ピンチ、回転できます。
* **ソーラーと電気のエネルギー：**合計（太陽、消費、充電状態付きのバッテリー、系統の有無）、各インバーターとバッテリー（セルは要求に応じて）、電気ノードのチャンネルと警報。
* **警報盤：**各 ARMOR-NODE-ALARM ノードの状態、ゾーンとイベント、サーバーが許可した場合の警戒・解除コマンド。
* **ネットワーク：**家のネットワークのデバイス、インターネットの状態、プロバイダーと場所付きの**公開アドレス**（ネットワークノードの報告どおり）。
* **Bluetooth でフィールドノードを設定**（サインイン画面または*その他 > ノードを設定*から）：`ARMOR-xxxxxx` を発信するノードを見つけ、新しいノードの管理者を作るか（ノードの PIN で）サインインし、Wi-Fi ネットワークを検索して、ノード名、ルーターの Wi-Fi または固定アドレス、ブローカーを設定します。**ノードファインダー**はすでにネットワーク上にあるものを一覧します。
* **アシスタント：**文字と音声のコマンド（クローズドなリスト、8 言語、あなたに結び付いた確認）で、家の状態を尋ねたり、警戒、解除、消音、照明のオン・オフができます。
* **証拠ライブラリ、**境界とノードの状態、すべての警報・ノード・カメラ・デバイス・警報・モード変更の**履歴**、**天気マップ**、設備の**サービス**とアップデート。
* **8 言語**（英語、スペイン語、ドイツ語、フランス語、イタリア語、日本語、中国語、ポルトガル語）を*その他 > 設定*で選ぶか端末に従います。すべての文が 8 つの表にあることを検査します。
* **パスワードの扱い：**平文 HTTP は、プライベート LAN またはループバックの IPv4 *リテラル*にのみ許可されます。プライベートアドレスのように始まるだけのホスト名（`10.attacker.example`）や先頭にゼロのあるアドレスは拒否されます。見た目はアイコン中心で、ほぼ黒の面、シアンのアクセント、注意にはアンバーを使います。
* **スマホからのセキュリティ：**2 段階認証と復旧コード、開いているセッション、サーバーから見たスマホの確認、外からの重要な操作での再認証、そして管理者向けに VPN（設定付きの端末）とダイナミック DNS の名前。
* **ステータス画面にシステム全体、そして外からの接続：** ステータス画面は警報パネル、サービス、録画中のカメラ、セキュリティとリモートアクセスをまとめ、各カードがその画面を開きます。入力したアドレスが自宅の外で https でない場合は、サインインが先に進めない理由を示し、2つの安全な方法（VPN、または https の公開アドレス）をガイドが説明します。
* **ノードの状態と警戒モード:** 「その他」にノードの状態画面（稼働時間、再起動の理由、メモリ、回線と信号、ブローカー接続、再起動、最後のエラー、サーバーの警告）があり、警報盤画面にはモード選択（外出、在宅、夜間、独自）があって、ファームウェアが対応していれば選んだモードで警戒します。8 言語対応です。
* **履歴の接続一覧:** 履歴画面に読み取り専用の2つ目の一覧があり、サーバーに接続するデバイスとアプリ（Studio、このアプリ、ノードのパネル、音声サービス）を、最終確認時刻、開いているセッション、サインインと拒否とともに表示します。アプリは自分が何者かをサーバーに伝えるため、自分自身として表示されます。アドレスは管理者にだけ表示されます。
* **バッテリーのメンテナンス（管理者向け）：** Pylontechバッテリーの簡単な操作——時計、カウンタとログ、再起動、容量、MOSFETテスト、ヒューズ故障、出力——を、Studioと同じ2段階（サーバーがノードにバッテリーを読み取らせ、画面に実行内容を正確に表示し、シリアル番号を再入力して「今すぐ実行」）で行い、結果と変更内容を表示します。制限値、ファームウェア、エキスパートコンソールはStudioで行います。
* **ノードの制御（管理者）：** その他 > ノード制御では、Studio と同じ操作（再起動、一時停止、再開、スタンバイ（動作停止、接続は維持）、識別、診断、メンテナンスのオン／オフ）を、1 台または全ノードに対して行えます。ノード名（全ノードの場合は RESTART、PAUSE、STANDBY のいずれかの単語）の再入力と新たな本人確認を求め、各ノードの進み具合を表示し、警報パネルやレーダーが一時停止またはスタンバイのとき家が無防備になることを警告します。工場出荷時リセット、消去、ディープスリープはありません。
* **開いているアプリのアラームウィンドウ：** 確認待ちのアラームがある間、アラーム画面以外のすべての画面の上にバナーが点滅します（重大は赤で速く、それ以外は琥珀色、端末のアニメーションがオフなら静止）。最も重大なアラームと待機件数を示し、その下でアプリを使い続けられます。アラームを開く、バナーから確認する、次のアラームが来るまで閉じる、のいずれもできます。
* **外出先から：** 2 つのアドレス（自宅の Wi-Fi ではプライベートなもの、モバイルデータまたは VPN では外出先用）を端末の場所に応じて選び、一方が応答しなければもう一方を試し、何が失敗したかを表示します。インストールの証明書の鍵は初回に記憶（または Studio の QR のテキストでペアリング）し、異なる鍵は拒否します。一度 https で接続したサーバーへの平文 http は拒否します。ノードのパネルはサーバー経由で開けます。警報はデータのみのプッシュとして届くことがあり、プッシュでも監視でも 1 度だけ通知します。開いているアプリとバックグラウンド監視はサーバーの読み取りを共有します。カメラの映像は画面外で停止し、待ち時間を延ばしながら再開します。
* **音と声まで選べる通知:** 設定で、すべての通知を消す、音や振動なし（読み上げもなし）で表示する、重大度（高・低）や種類（レーダー警報、応答しないカメラ、オフラインまたは無応答のノード、デバイス・ソーラー・電気・ネットワーク・アラームパネルのアラーム）ごとにオフにする、ができます。重大なアラームは、すべての通知を消していない限り必ず通知されます。重大度ごと・通知の種類ごとの音を、電話の音または自分のファイル（3 MB 未満）から選べ、それぞれ再生ボタン付きです。アラームを読み上げる声（女性・男性・どちらでも、子ども・大人・高齢者、標準・アクションヒーロー・ダークロード、速度、低重大度の通知も読み上げるか）もテストボタン付きで選べます。
* **正しい画面へ導くバナーと、静かになった監視:** アラームのバナーは、それを扱う画面（カメラ、デバイス、インバーターまたはバッテリー、電気画面、ネットワーク、アラームパネル）を開きます。電話はプッシュ登録時に自分の言語をサーバーに伝え、通知はその言語で書かれ、新しい Firebase トークンはバックグラウンドからすぐサーバーに届きます。1 本のストリームに 2 つのレンズがあるカメラは、カメラ一覧で 2 つのウィンドウになります。プッシュ通知が働いている間、バックグラウンド監視は 10 秒ではなく 120 秒ごとにサーバーへ問い合わせます（*設定 > プッシュ通知による監視*：10、60、120、300、600 秒）。""",
      "role": r"""ARMOR-ANDROID-CONTROL は [ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) と同じ [ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER) へのスマートフォンの窓口で、読み取りも指示もサーバーを通してのみ行います。警報があなたを追いかけ（鳴っている警報盤はスマートフォンを起こします）、アシスタントに声で尋ねられ、現場で新しいノードの横から Bluetooth で設定するためのツールでもあります。

| 名前 | 方法 | 用途 |
|---|---|---|
| ARMOR-SERVER | HTTP `/api/v1` (55 paths), MJPEG | アプリが読み取り・命令するすべて |
| フィールドノード | Bluetooth (`ARMOR-xxxxxx`) | 新しいノードのそばで設定 |
| GitHub | HTTPS | アプリ自身の署名付き更新を確認・取得 |
| Open-Meteo | HTTPS | 天気マップの公開予報、大気質、地名検索 |""",
      "architecture": r"""<p align="center">
  <img src="images/architecture.svg" alt="ARMOR-ANDROID-CONTROL のアーキテクチャ：呼び出し元、内部、依存先" width="100%">
</p>""",
      "security": r"""| 脅威 | 対策 |
|---|---|
| 電話に保存されたパスワード | *ログイン状態を保持*（初期はオフ）のときだけ：ユーザーとパスワードをそのサーバー専用の Keystore 鍵で封印し、チェックを外すと即消去。バックアップなし（`allowBackup=false`） |
| インターネットへの平文 HTTP | プライベート LAN またはループバックの IPv4 *リテラル* にのみ許可。`10.attacker.example` のようなホストや先頭が 0 のアドレス（`010.0.0.1` は 8 進数と解釈）は拒否。https で到達したホストへの平文 http も拒否 |
| https の中間者 | 信頼するのはシステムの認証局と、電話にインストールしたもの。設置環境の証明書の鍵は初回に記憶（または Studio の QR のテキストでペアリング）し、異なる鍵は拒否します |
| 電話が他人の手にあるときの重要な命令 | アーム、ディスアーム、サイレン停止、解錠などの重要な命令の前に、電話の指紋・顔・PIN を要求します（指紋か顔があるときのみ初期でオン）。管理者は Studio から必須にできますが、選んだ水準を下げることはできません。画面ロックのない電話が締め出されることはありません |
| 閲覧者が何かを変更する | *閲覧者* ロールはすべて見られますが、何かを変えるボタンはすべて無効です（ロールのテストあり） |
| 誤った解除 PIN | PIN は解除時にだけサーバーへ送られます。`wrong_pin`、`pin_locked`、`pin_not_set`、`elevation_required` は平易な言葉に翻訳されます |
| 偽のアプリ更新 | Android のインストーラーを呼ぶ前に、インストール済みアプリと候補の署名証明書（履歴）の SHA-256 を比較します。共通するものがなければ、はっきりそう伝えます |
| 電話が気づかないアラーム | フォアグラウンドサービス（`AlarmWatcherService`）が 10 秒ごとに問い合わせ、ロック解除を 15 秒待ち、最大 60 秒まで間隔を延ばし、6 回失敗で*到達不能*と表示し、再起動後も動きます。15 分より古いアラームは通知しません |
| 電話上のカメラのパスワード | カメラはサーバーのストリーム経由で見ます。アプリにはカメラのパスワードも RTSP アドレスもありません |

### 権限

`INTERNET`、`ACCESS_NETWORK_STATE`：サーバー。`USE_BIOMETRIC`：電話のロック。`POST_NOTIFICATIONS`：アラーム。`FOREGROUND_SERVICE`（+ `DATA_SYNC`、`SPECIAL_USE`）と `RECEIVE_BOOT_COMPLETED`：アラーム監視。`REQUEST_INSTALL_PACKAGES`：アプリの更新。`BLUETOOTH_SCAN`、`BLUETOOTH_CONNECT`：ノードの設定。`BLUETOOTH`、`BLUETOOTH_ADMIN`、`ACCESS_FINE_LOCATION` は Android 11 まで（`maxSdkVersion=30`）で、Bluetooth のスキャン用です。

独立したセキュリティレビューはありません。[docs/CLIENT_BOUNDARY.md](docs/CLIENT_BOUNDARY.md) と [SECURITY.md](SECURITY.md) を参照してください。""",
      "interfaces": r"""| 部分 | 設定内容 |
|---|---|
| ARMOR-SERVER | `network/ArmorApiClient.kt` に `/api/v1` の 55 種類のパス（インターフェースは `network/ArmorApi.kt`）。レーダーは 1.5 秒ごとに読み、カメラはサーバー経由の MJPEG |
| 2 つのアドレス | 自宅 Wi-Fi ではプライベートアドレス、外出先ではモバイル通信か VPN のアドレスを電話の場所で選びます。片方が応答しなければもう片方を試し、何が失敗したかを伝えます |
| Bluetooth | `ARMOR-xxxxxx` を発信しているノードを見つけ、新しいノードの管理者を作成するかノードの PIN でサインインし、Wi-Fi を検索して名前・Wi-Fi または固定アドレス・ブローカーを設定します。プロトコルは `model/NodeBle.kt`、ノードファインダーはすでにネットワーク上にあるものを一覧します |
| 音声 | `POST /api/v1/voice/command`：8 言語の固定コマンド一覧と、あなたに結び付いた確認（`model/Voice.kt`、`VoiceScreens.kt`） |
| Push | `PushService`：データのみのメッセージとして届くアラームは、プッシュ経由でも監視経由でも 1 回だけ通知します。Firebase の手順は [docs/PUSH_NOTIFICATIONS.md](docs/PUSH_NOTIFICATIONS.md)（8 言語） |""",
      "configuration": r"""| 名前 | 値 | 設定内容 |
|---|---|---|
| `compileSdk` / `targetSdk` / `minSdk` | 37 / 37 / 26 | 電話は Android 8.0 以降 |
| `versionName` | = `armor.project.json` | マニフェストとバージョンが違うとビルドが失敗 |
| JDK / Android SDK | 17+ / 37 | アプリのビルドとテストの実行用 |

アプリ内（ファイルではなく）：言語（8 言語または電話に従う）、2 つのアドレス、*ログイン状態を保持*、電話のロック、音声アラーム、通知は *その他 > 設定* にあります。コード内の制限：監視は 10 秒ごとに問い合わせ、最大 60 秒まで間隔を延ばし、15 分より古いアラームは無視します。""",
      "quickstart": r"""**必要なもの:** JDK 17+、Android SDK（compile SDK 37）、Android 8.0+ の電話（minSdk 26）。

```powershell
.\gradlew.bat testDebugUnitTest assembleDebug   # 367 tests, then the debug APK
adb install -r app\build\outputs\apk\debug\app-debug.apk
```

リリースは GitHub で公開され、アプリ自身がそこから更新を確認します。APK は管理者自身のリリース用の鍵（リポジトリの外に保管）で署名されており、アプリはダウンロードしたファイルを Android のインストーラーに渡す前に、その署名証明書を自身のものと照合します。[クライアントの境界](docs/CLIENT_BOUNDARY.md)を参照してください。""",
      "testing": r"""```powershell
.\gradlew.bat testDebugUnitTest
python -I tools/armor_ci_validate.py
```

| 部分 | テスト数 | 対象 |
|---|---|---|
| アラーム | 67 | `AlarmPolicy`、`AlarmBanner`、`AlarmPanels`、`AlarmCodes`、`AlarmRoute`、`NoticeFilter`、`PushEvents`、`DevicesAndAlarms` |
| サーバー接続、解析、試験データ | 59 | `ApiClient`, `ApiError`, `ServerFixtures`, `ParsersTolerant`, `SavePayload`, `JsonText`, `Preflight`, `SharedFeed`, `Connections` |
| ビューモデルとロール | 41 | `ArmorViewModel`, `Viewer`, `ArmProfiles`, `NodeCensus`, `NodeHealth` |
| ロック、セッション保管庫、鍵 | 38 | `DeviceLock`, `SessionVault`, `CredentialVault`, `KeyBinding`, `Security` |
| アドレスの安全性、証明書 | 32 | `ServerEndpoint`, `ServerAddresses`, `Literals`, `NodeAddress`, `CertificatePins`, `RemoteAccess` |
| エネルギーとネットワーク | 34 | `Solar`, `Battery`, `Electrical`, `Network` |
| Bluetooth のノードとノード制御 | 26 | `NodeBle`, `NodeControl` |
| GitHub からの更新 | 17 | `GitHubReleaseUpdaterHttpFailure`, `SignerCheck`, `SemanticVersion`, `ReleaseMetadataParser` |
| レーダーとカメラ | 14 | `RadarGeometry`, `CameraTraits`, `CameraLenses` |
| 翻訳、平易な言葉、音声 | 14 | `Tr`, `Friendly`, `Voice` |

47 ファイル 367 件のテストを `testDebugUnitTest` で実行します。擬似サーバー（`FakeServer.kt`）と実サーバーから取得したデータ（`tools/capture_fixtures.mjs`）を使います。すべてのフレーズが 8 つの言語表にあることも検査します。""",
      "build": "リリースは GitHub で公開され、アプリ自身がそこで更新を確認します。アプリはアセット `ARMOR-ANDROID-CONTROL-release.apk` を探します。APK はリポジトリ外に保管したメンテナー自身のリリース鍵で署名され、アプリはダウンロードした署名証明書を自分のものと比較してから Android のインストーラーに渡します。APK ごとに事前に `versionCode` を上げないと、Android は更新として扱いません。",
      "troubleshooting": r"""| 症状 | 原因 | 対処 |
|---|---|---|
| `wrong_pin`, `pin_locked`, `pin_not_set`, `elevation_required` | サーバーが解除 PIN を拒否、または新しい本人確認を要求 | PIN を入れ直す、ロック解除を待つ、または本人確認をする |
| サインインが先に進めない | アドレスが自宅外で https がない（平文 http は拒否） | ガイドに従う：VPN、または https の公開アドレス |
| 動いていた接続が拒否される | 設置環境の証明書の鍵が変わった | 意図して変えたなら Studio の QR テキストで再ペアリング |
| バックグラウンドでアラームが遅れる、または届かない | メーカーのバッテリー制限が監視を止める。プッシュには独自の Firebase プロジェクトが必要 | アプリを省電力の対象外にし、[docs/PUSH_NOTIFICATIONS.md](docs/PUSH_NOTIFICATIONS.md) に従う |
| 更新が拒否される | ダウンロードの署名証明書がインストール済みアプリと共通しない | インストールせず、このリポジトリのリリースから APK を取得する |""",
      "structure": r"""<p align="center">
  <img src="images/repository-structure.svg" alt="ARMOR-ANDROID-CONTROL のリポジトリ構造" width="100%">
</p>

<details>
<summary>ツリーのテキスト版</summary>

```text
ARMOR-ANDROID-CONTROL/
├── app/src/main/java/es/electrohobby3d/armor/   アプリ：画面、ルール、ネットワーク、更新
├── app/src/main/assets/                         8 言語の表、アラームコード、天気マップ
├── app/src/test/                                367 件のテストと擬似サーバー
├── docs/                                        このリポジトリのガイド
├── tools/                                       共通の CI チェックとプロジェクトツール
├── .github/                                     CI ワークフローと Issue・Pull Request のテンプレート
├── images/                                      バナー、アイコン、この README の 2 つの図
├── build.sh build.bat                           共通のプロジェクトワークフローでビルド
├── test.sh test.bat                             共通のワークフローでテストを実行
├── run.sh run.bat                               共通のプロジェクトワークフローで起動
├── armor.project.json                           マニフェスト：バージョン、役割、成熟度、ビルドコマンド
├── CHANGELOG.md                                 各バージョンの変更点
├── SECURITY.md SUPPORT.md LICENSE               セキュリティポリシー、サポート、ライセンス
├── CONTRIBUTING.md CODE_OF_CONDUCT.md           貢献方法と行動規範
├── build.gradle.kts settings.gradle.kts         プロジェクトの Gradle ビルド
├── gradle.properties                            Gradle の設定
├── gradlew gradlew.bat gradle/                  Gradle ラッパー
├── build-test.sh build-test.bat                 共通のワークフローでテストを実行
└── .gitattributes .gitignore                    Git の設定
```

</details>""",
      "roadmap": r"""**現時点の既知の制限**

* ソーラー、電気、アラームパネルの画面は実機に触れていません（レーダーノードしかありません）。
* ノードの Bluetooth 設定は実機で確認しておらず、Firebase のプッシュも電話で試していません。
* 各メーカーのバッテリー制限下でのバックグラウンドのアラーム監視は未証明です。
* 独立したセキュリティレビューはありません。

**今後**

* 実際のノードでソーラー・電気・アラームパネルの画面と Bluetooth 設定を試す。
* 設置環境独自のプロジェクトで Firebase のプッシュを、複数メーカーでアラーム監視を試す。""",
    },
  },
  "zh": {
    "tagline": "ARMOR-SERVER 的移动操作端：报警、摄像头、雷达、能源、网络和节点设置，支持八种语言",
    "honest": "地址安全、报警决策、报警监视器、翻译和只读角色的规则由 367 个单元测试覆盖，应用可以构建（`gradlew testDebugUnitTest assembleDebug`）。它在真实手机上对照 CM5 测试台运行：登录、摄像头监视器、布防和报警、雷达、通过蓝牙设置节点以及从 GitHub 更新都在使用中。**尚未**证明的是：使用真实设备的太阳能、电气和报警主机界面（目前只有雷达节点）、通过 Firebase 的推送（应用中已包含，需要自己的 Firebase 项目；尚未在手机上试过），以及在各手机厂商电池规则下的后台报警监视。",
    "glance": [
      [
        "角色",
        "ARMOR-SERVER 的 Android 操作客户端（家族：Clients，上级：ARMOR-SERVER）",
      ],
      [
        "技术栈",
        "Kotlin / Jetpack Compose, Android 8.0+",
      ],
      [
        "测试",
        "367 (`gradlew testDebugUnitTest`)",
      ],
      [
        "语言",
        "8（每种语言 1345 条，每条都在所有表中检查）",
      ],
      [
        "运行位置",
        "Android 8.0+ 手机（minSdk 26）",
      ],
      [
        "真实硬件",
        "在真实手机上对照 CM5 测试台使用；太阳能、电气和报警主机界面在等待真实节点",
      ],
      [
        "许可证",
        "GPL-3.0-or-later",
      ],
    ],
    "status": {
      "software": "应用可以构建（`gradlew testDebugUnitTest assembleDebug`），并在真实手机上对 CM5 测试台运行。",
      "tests": "367 项单元测试通过（`gradlew testDebugUnitTest`）：地址安全、报警判定、报警监视、翻译和只读角色。",
      "ui": "登录、摄像头监视、布防与报警和雷达已在真实手机上使用；通过蓝牙设置节点尚未在真实节点上确认，光伏、电气和报警面板界面也尚未接触真实设备。",
      "hardware": "已在真实手机上对 CM5 测试台使用；各手机厂商电池规则下的后台报警监视尚未证明。",
      "security": "地址安全和只读角色规则有单元测试覆盖；没有经过独立审查。",
      "updates": "来自 GitHub 的更新已在手机上使用。",
      "integration": "通过 Firebase 的推送已在应用中，但需要自己的 Firebase 项目，尚未在手机上试过。",
      "docs": "八种语言和更新日志均为最新。",
    },
    "docs": [
      "[客户端边界](docs/CLIENT_BOUNDARY.md)：客户端做什么、绝不做什么",
      "[推送通知](docs/PUSH_NOTIFICATIONS.md)：Firebase 步骤（八种语言）",
      "[台架测试](docs/BENCH_TESTS.md)：用真机进行的检查",
    ],
    "contributing_first": "提交 Pull Request 之前请运行 `.\\gradlew.bat testDebugUnitTest` and `python -I tools/armor_ci_validate.py`：必须通过。参见 [CONTRIBUTING.md](CONTRIBUTING.md) 和[行为准则](CODE_OF_CONDUCT.md)。",
    "languages_extra": "",
    "body": {
      "overview": r"""* **使用服务器自己的登录登录：**IP、端口、用户名和密码；密码创建一个 HttpOnly 会话；只有勾选 **记住我** 时才会保存在手机上（默认关闭：用户名和密码用 Keystore 专属密钥加密，仅用于该服务器，取消勾选后立即清除）。**viewer** 角色只能查看：所有会修改内容的按钮都被关闭。
* **使用手机锁定：** 在布防、撤防、关闭警报器、解锁以及其他关键指令之前，应用会要求验证手机自身的指纹、面部或 PIN（仅当手机有指纹或面部识别时默认开启）；如果你开启，打开应用时也会要求验证。管理员可以在 Studio 中强制要求，但不能降低你的选择；没有屏幕锁定的手机永远不会被拒之门外，锁定界面也始终提供改用密码重新登录。可选（默认关闭，并有醒目的提示）：可将封存已保存会话的密钥与手机解锁绑定；开启后，手机重启后后台报警监控会等到您解锁手机才恢复。
* **摄像头监视器：**1 到 16 个画面、放大视图、保持画面比例的实时 MJPEG、有限定范围的云台面板、快照和录像，录像带有查看器和删除确认。
* **布防和撤防：**先做**布防前检查**（哪些是打开、沉默或故障的），撤防需要 PIN；要确认的**报警**，等待中的显示角标；**设备**（烟雾、燃气、漏水、门、窗、移动、气候、插座、灯、警笛、门锁、卷帘、大门和车库门电机、热水器）及其状态和开 / 关 / 切换。
* **能找到你的报警：**每种严重级别有声音、可选的**语音报警**、节点达到高级、摄像头沉默、设备报警和（布防时）节点离线的通知，**响起的报警主机会唤醒手机**；后台监视在重启后仍然存在，并在服务器宕机时退避。
* **实时雷达，2D 和 3D：**雷达标签页按 Studio 中的设计绘制场地，以及雷达看到的人在其上移动，每秒半刷新一次；可拖动、捏合和旋转 3D 视图。
* **太阳能与电气能源：**合计（阳光、用电、带电量的电池、电网是否存在）、每个逆变器和电池（可按需查看电芯），以及电气节点的通道和报警。
* **报警主机：**每个 ARMOR-NODE-ALARM 节点的状态、其防区和事件，以及服务器允许时的布防 / 撤防命令。
* **网络：**住宅网络的设备、互联网状态以及带运营商和地点的**公网地址**，均由网络节点报告。
* **通过蓝牙设置现场节点**（从登录界面或*更多 > 设置节点*）：找到广播 `ARMOR-xxxxxx` 的节点，为新节点创建管理员或登录（使用节点的 PIN），搜索 Wi-Fi 网络并设置节点名称、路由器 Wi-Fi 或固定地址以及代理；**节点查找器**列出网络上已有的节点。
* **助手：**文字和语音命令（封闭列表，八种语言，确认与你绑定），可询问住宅状态，或布防、撤防、静音以及开关灯。
* **证据库、**周界和节点状态、每次警报、节点、摄像头、设备、报警和模式变化的**历史**、**天气地图**，以及系统的**服务**和更新。
* **八种语言**（英语、西班牙语、德语、法语、意大利语、日语、中文和葡萄牙语），在*更多 > 设置*中选择或跟随手机；会检查每一句话都在八张表中。
* **谨慎对待密码：**明文 HTTP 只允许用于私有局域网或回环的 IPv4 *字面量*；仅看起来像私有地址的主机名（`10.attacker.example`）或带前导零的地址会被拒绝。界面由图标构成：近黑色表面、青色强调、琥珀色表示注意。
* **在手机上管理安全：**第二重验证及其恢复码、已打开的会话、检查服务器如何看待手机、从外部执行关键操作时的重新身份验证，以及面向管理员的 VPN（带配置的设备）和动态 DNS 名称。
* **状态屏幕展示整个系统，以及从外部进入的方式：** 状态屏幕汇总报警主机、服务、正在录像的摄像头以及安全与远程访问，每张卡片都会打开对应屏幕；当输入的地址在家外且没有 https 时，登录会说明为何无法继续，并由向导讲解两种安全方式（VPN，或带 https 的公网地址）。
* **节点健康与布防模式：** “更多”中有节点健康画面（每个节点的运行时间、重启原因、内存、连接与信号、代理连接、重启、最后错误以及服务器发出的警告），报警主机画面有模式选择（离家、在家、夜间和自定义），主机固件支持时按所选模式布防。支持八种语言。
* **历史中的连接：** 历史页面新增了第二个只读列表，列出连接服务器的设备和应用（Studio、本应用、节点面板、语音服务），以及各自最后出现的时间、已打开的会话、登录与被拒次数；应用现在会向服务器表明自己的身份，因此会以自己的名义显示。地址只显示给管理员。
* **电池维护（管理员）：** 对 Pylontech 电池的简单操作——时钟、计数器和日志、重启、容量、MOSFET 测试、保险丝故障、输出——与 Studio 相同的两步（服务器让节点读取电池，界面准确显示将要执行的内容，再输入序列号点击“立即执行”），并显示结果和变化；限值、固件和专家控制台仍在 Studio 中操作。
* **节点控制（管理员）：** 更多 > 节点控制提供与 Studio 相同的操作——重启、暂停、恢复、待机（停止工作，保持连接）、识别、诊断以及开启或关闭维护——可用于一个节点或全部节点；需要再次输入节点名称（对所有节点则输入单词 RESTART、PAUSE 或 STANDBY）并重新验证身份，显示每个节点进行到哪一步，并警告报警主机或雷达处于暂停或待机时家中将失去保护。没有恢复出厂设置、擦除或深度睡眠。
* **已打开应用中的报警窗口：** 有报警等待人处理时，除报警页面外，每个页面上方都会出现脉动的横幅（严重报警为红色且更快，其余为琥珀色，手机关闭动画时保持静止），说明最严重的报警和等待的数量，并允许在其下继续使用应用；可打开报警、直接在横幅上确认，或关闭到下一个报警到来。
* **在家外使用：** 两个地址（家中 Wi-Fi 使用内网地址，移动数据或 VPN 使用外出地址），按手机所在位置选择；一个没有响应时尝试另一个，并提示哪里出了问题；安装证书的密钥在首次连接时记住（或用 Studio 二维码的文本配对），不同的密钥会被拒绝，对曾通过 https 访问过的服务器拒绝普通 http；可以通过服务器打开节点的面板；警报可以作为仅含数据的推送到达，无论经由推送还是后台监控，只播报一次；打开的应用与后台监控共用一次服务器读取；摄像头画面离开屏幕即停止，并以逐渐增长的等待时间恢复。
* **可自选声音与语音的通知:** 在设置中可以静音所有通知、不带声音和振动地显示（也不朗读），并按严重程度（高、低）或类型（雷达警报、无响应的摄像头、离线或沉默的节点，以及设备、太阳能、电气、网络和报警面板的报警）关闭；除非所有通知都被静音，否则严重报警一定会通知。每种严重程度和每种通知类型都可选声音，来自手机自带声音或自己的文件（小于 3 MB），各带播放按钮；朗读报警的语音（女声、男声或任意；儿童、成人或老人；平实、动作英雄或黑暗领主；语速；以及是否也朗读低严重程度的通知）带有试听按钮。
* **直达正确屏幕的横幅与更安静的监视:** 报警横幅会打开处理它的屏幕（摄像头、设备、逆变器或电池、电气屏幕、网络或报警面板）；手机在注册推送时告诉服务器它的语言，通知就用该语言书写，新的 Firebase 令牌会立刻从后台送达服务器。同一路流中有两个镜头的摄像头在摄像头列表中是两个窗口。推送提醒正常工作时，后台监视每 120 秒而不是每 10 秒询问一次服务器（*设置 > 推送提醒下的监视*：10、60、120、300 或 600 秒）。""",
      "role": r"""ARMOR-ANDROID-CONTROL 是手机上通往 [ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) 所用的同一个 [ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER) 的窗口：它只通过服务器读取和下达命令。报警会跟着你（响起的报警主机会唤醒手机），你可以用语音询问助手，也可以在现场站在新节点旁通过蓝牙设置它。

| 名称 | 方式 | 用途 |
|---|---|---|
| ARMOR-SERVER | HTTP `/api/v1` (55 paths), MJPEG | 应用读取和下达的一切 |
| 现场节点 | Bluetooth (`ARMOR-xxxxxx`) | 在新节点旁边完成设置 |
| GitHub | HTTPS | 检查并下载应用自身的签名更新 |
| Open-Meteo | HTTPS | 天气地图使用的公开预报、空气质量和地点搜索 |""",
      "architecture": r"""<p align="center">
  <img src="images/architecture.svg" alt="ARMOR-ANDROID-CONTROL 的架构：谁调用它、它包含什么、它依赖什么" width="100%">
</p>""",
      "security": r"""| 威胁 | 防御 |
|---|---|
| 保存在手机上的密码 | 仅在勾选*记住我*时（默认关闭）：用户名和密码用专属 Keystore 密钥加密，仅用于该服务器，取消勾选立即清除；不备份（`allowBackup=false`） |
| 面向互联网的明文 HTTP | 仅允许私有局域网或回环的 IPv4 *字面量*；`10.attacker.example` 之类的主机或带前导零的地址（`010.0.0.1` 会被当作八进制）会被拒绝；曾通过 https 访问的主机不允许改用明文 http |
| https 上的中间人 | 信任的是系统的证书颁发机构以及你在手机上安装的那些；首次记住安装环境证书的密钥（或用 Studio 二维码文本配对），不同的密钥会被拒绝 |
| 手机落入他人之手时的关键操作 | 在布防、撤防、静音警笛、解锁等关键操作前要求手机指纹、面部或 PIN（仅在手机有指纹或面部时默认开启）；管理员可在 Studio 中强制要求，但不能降低你的选择；没有屏幕锁的手机永远不会被拒之门外 |
| 查看者修改了内容 | *查看者*角色能看到一切，但所有会修改内容的按钮都被禁用（有角色测试） |
| 错误的撤防 PIN | PIN 仅在撤防时发送给服务器；`wrong_pin`、`pin_locked`、`pin_not_set` 和 `elevation_required` 会被翻译成通俗文字 |
| 伪造的应用更新 | 在调用 Android 安装程序之前，会比较已安装应用与候选版本的签名证书（历史）SHA-256；若没有任何共同项，会明确提示 |
| 手机没看到的报警 | 前台服务（`AlarmWatcherService`）每 10 秒轮询一次，等待手机解锁 15 秒，退避最多 60 秒，失败 6 次后提示*无法连接*，重启后依然运行；超过 15 分钟的报警不会播报 |
| 手机上的摄像头密码 | 摄像头通过服务器的视频流观看：应用没有摄像头密码，也没有 RTSP 地址 |

### 权限

`INTERNET`、`ACCESS_NETWORK_STATE`：服务器。`USE_BIOMETRIC`：手机锁。`POST_NOTIFICATIONS`：报警。`FOREGROUND_SERVICE`（+ `DATA_SYNC`、`SPECIAL_USE`）和 `RECEIVE_BOOT_COMPLETED`：报警监视。`REQUEST_INSTALL_PACKAGES`：应用更新。`BLUETOOTH_SCAN`、`BLUETOOTH_CONNECT`：设置节点；`BLUETOOTH`、`BLUETOOTH_ADMIN` 和 `ACCESS_FINE_LOCATION` 仅限 Android 11 及以下（`maxSdkVersion=30`），用于蓝牙扫描。

没有独立的安全审查。请阅读 [docs/CLIENT_BOUNDARY.md](docs/CLIENT_BOUNDARY.md) 和 [SECURITY.md](SECURITY.md)。""",
      "interfaces": r"""| 部分 | 作用 |
|---|---|
| ARMOR-SERVER | `network/ArmorApiClient.kt` 中有 55 条不同的 `/api/v1` 路径（接口在 `network/ArmorApi.kt`）；雷达每 1.5 秒读取一次；摄像头经服务器以 MJPEG 方式观看 |
| 两个地址 | 家庭 Wi-Fi 下用私有地址，外出时（移动数据或 VPN）用外出地址，按手机所在位置选择；一个无响应就尝试另一个，并说明失败原因 |
| Bluetooth | 查找广播 `ARMOR-xxxxxx` 的节点，创建新节点的管理员或用节点 PIN 登录，搜索 Wi-Fi 并设置名称、Wi-Fi 或固定地址和代理；协议在 `model/NodeBle.kt`；节点查找器会列出已在网络上的节点 |
| 语音 | `POST /api/v1/voice/command`：八种语言的封闭命令列表，并带有与你绑定的确认（`model/Voice.kt`、`VoiceScreens.kt`） |
| Push | `PushService`：报警以仅含数据的消息送达，无论经推送还是监视，只播报一次；Firebase 步骤见 [docs/PUSH_NOTIFICATIONS.md](docs/PUSH_NOTIFICATIONS.md)（八种语言） |""",
      "configuration": r"""| 名称 | 值 | 作用 |
|---|---|---|
| `compileSdk` / `targetSdk` / `minSdk` | 37 / 37 / 26 | 手机需 Android 8.0 或更高 |
| `versionName` | = `armor.project.json` | 清单与版本不一致时构建失败 |
| JDK / Android SDK | 17+ / 37 | 用于构建应用和运行测试 |

应用内（不在文件中）：语言（八种语言或跟随手机）、两个地址、*记住我*、手机锁、语音报警和通知，位于*更多 > 设置*。代码中的限制：监视每 10 秒轮询一次，最多退避到 60 秒，并忽略超过 15 分钟的报警。""",
      "quickstart": r"""**要求:** JDK 17+、Android SDK（compile SDK 37）、Android 8.0+ 手机（minSdk 26）。

```powershell
.\gradlew.bat testDebugUnitTest assembleDebug   # 367 tests, then the debug APK
adb install -r app\build\outputs\apk\debug\app-debug.apk
```

版本发布在 GitHub 上，应用自己会从那里检查更新；APK 使用维护者自己的发布密钥签名（密钥保存在仓库之外），应用在把文件交给 Android 安装程序之前，会先把下载文件的签名证书与自己的比对。参见[客户端边界](docs/CLIENT_BOUNDARY.md)。""",
      "testing": r"""```powershell
.\gradlew.bat testDebugUnitTest
python -I tools/armor_ci_validate.py
```

| 部分 | 测试数 | 覆盖内容 |
|---|---|---|
| 报警 | 67 | `AlarmPolicy`、`AlarmBanner`、`AlarmPanels`、`AlarmCodes`、`AlarmRoute`、`NoticeFilter`、`PushEvents`、`DevicesAndAlarms` |
| 服务器连接、解析、测试数据 | 59 | `ApiClient`, `ApiError`, `ServerFixtures`, `ParsersTolerant`, `SavePayload`, `JsonText`, `Preflight`, `SharedFeed`, `Connections` |
| 视图模型与角色 | 41 | `ArmorViewModel`, `Viewer`, `ArmProfiles`, `NodeCensus`, `NodeHealth` |
| 锁、会话保险库、密钥 | 38 | `DeviceLock`, `SessionVault`, `CredentialVault`, `KeyBinding`, `Security` |
| 地址安全、证书 | 32 | `ServerEndpoint`, `ServerAddresses`, `Literals`, `NodeAddress`, `CertificatePins`, `RemoteAccess` |
| 能源与网络 | 34 | `Solar`, `Battery`, `Electrical`, `Network` |
| 蓝牙节点与节点控制 | 26 | `NodeBle`, `NodeControl` |
| 来自 GitHub 的更新 | 17 | `GitHubReleaseUpdaterHttpFailure`, `SignerCheck`, `SemanticVersion`, `ReleaseMetadataParser` |
| 雷达与摄像头 | 14 | `RadarGeometry`, `CameraTraits`, `CameraLenses` |
| 翻译、通俗措辞、语音 | 14 | `Tr`, `Friendly`, `Voice` |

47 个文件共 367 个测试，用 `testDebugUnitTest` 运行；由模拟服务器（`FakeServer.kt`）和从真实服务器获取的数据（`tools/capture_fixtures.mjs`）驱动。还会检查每条短语都在八张语言表中。""",
      "build": "版本发布在 GitHub，应用自己从那里检查更新；应用查找资源 `ARMOR-ANDROID-CONTROL-release.apk`。APK 使用维护者自己的发布密钥签名（密钥保存在仓库之外），应用在把文件交给 Android 安装程序之前，会比较下载文件的签名证书与自身证书。每个 APK 之前都要提高 `versionCode`，否则 Android 不会把它当作更新。",
      "troubleshooting": r"""| 现象 | 原因 | 处理 |
|---|---|---|
| `wrong_pin`, `pin_locked`, `pin_not_set`, `elevation_required` | 服务器拒绝撤防 PIN 或要求重新验证身份 | 重新输入 PIN、等待锁定结束或确认身份 |
| 登录提示无法继续 | 地址在家庭之外且没有 https（明文 http 被拒绝） | 按指南操作：使用 VPN，或带 https 的公网地址 |
| 原本可用的连接被拒绝 | 安装环境证书的密钥发生了变化 | 若是有意更改，请用 Studio 二维码文本重新配对 |
| 后台报警延迟或收不到 | 手机厂商的电池策略会停止监视；推送需要自己的 Firebase 项目 | 将应用排除在省电限制之外；按 [docs/PUSH_NOTIFICATIONS.md](docs/PUSH_NOTIFICATIONS.md) 操作 |
| 更新被拒绝 | 下载文件的签名证书与已安装应用没有任何共同项 | 不要安装；请从本仓库的发布版本获取 APK |""",
      "structure": r"""<p align="center">
  <img src="images/repository-structure.svg" alt="ARMOR-ANDROID-CONTROL 的仓库结构" width="100%">
</p>

<details>
<summary>目录树的文本版</summary>

```text
ARMOR-ANDROID-CONTROL/
├── app/src/main/java/es/electrohobby3d/armor/   应用：界面、规则、网络与更新
├── app/src/main/assets/                         八种语言表、报警代码、天气地图
├── app/src/test/                                367 个测试和一个模拟服务器
├── docs/                                        本仓库的指南
├── tools/                                       共享的 CI 检查和项目工具
├── .github/                                     CI 工作流以及 Issue 和 Pull Request 模板
├── images/                                      横幅、图标和本 README 的两幅图
├── build.sh build.bat                           通过共享的项目工作流构建
├── test.sh test.bat                             通过共享工作流运行测试
├── run.sh run.bat                               通过共享的项目工作流启动
├── armor.project.json                           清单：版本、角色、成熟度、构建命令
├── CHANGELOG.md                                 每个版本的变化
├── SECURITY.md SUPPORT.md LICENSE               安全策略、支持和许可证
├── CONTRIBUTING.md CODE_OF_CONDUCT.md           如何贡献与行为准则
├── build.gradle.kts settings.gradle.kts         项目的 Gradle 构建
├── gradle.properties                            Gradle 设置
├── gradlew gradlew.bat gradle/                  Gradle 包装器
├── build-test.sh build-test.bat                 通过共享工作流运行测试
└── .gitattributes .gitignore                    Git 设置
```

</details>""",
      "roadmap": r"""**目前已知的限制**

* 太阳能、电气和报警面板的界面尚未接触过真实设备（目前只有一个雷达节点）。
* 节点的蓝牙设置尚未在真实节点上确认，Firebase 推送也未在手机上试过。
* 在各手机厂商的电池策略下，后台报警监视尚未得到验证。
* 没有独立的安全审查。

**下一步**

* 用真实节点试验太阳能、电气和报警面板界面以及蓝牙设置。
* 用某个安装环境自己的项目试验 Firebase 推送，并在多家手机厂商的设备上试验报警监视。""",
    },
  },
  "pt": {
    "tagline": "Cliente móvel de operador para o ARMOR-SERVER: alarmes, câmaras, radar, energia, a rede e a configuração dos nós, em oito idiomas",
    "honest": "As regras de segurança do endereço, de decisão de alarmes, do vigia de alarmes, de tradução e do papel só de leitura estão cobertas por 367 testes unitários e a aplicação compila (`gradlew testDebugUnitTest assembleDebug`). Funciona num telemóvel real contra a bancada de testes do CM5: o acesso, o monitor de câmaras, o armar e os alarmes, o radar, a configuração de um nó por Bluetooth e as atualizações a partir do GitHub estão em uso. O que **ainda não** está provado: os ecrãs solar, elétrico e de centrais de alarme com equipamentos reais (só existe um nó radar), o push por Firebase (está na aplicação e precisa de um projeto Firebase próprio; ainda não foi experimentado num telemóvel) e a vigilância de alarmes em segundo plano sob as regras de bateria de cada fabricante.",
    "glance": [
      [
        "Função",
        "Cliente de operador Android para o ARMOR-SERVER (família: Clients, pai: ARMOR-SERVER)",
      ],
      [
        "Tecnologia",
        "Kotlin / Jetpack Compose, Android 8.0+",
      ],
      [
        "Testes",
        "367 (`gradlew testDebugUnitTest`)",
      ],
      [
        "Línguas",
        "8 (1345 frases por língua, cada frase verificada em todas as tabelas)",
      ],
      [
        "Funciona em",
        "Um telemóvel com Android 8.0+ (minSdk 26)",
      ],
      [
        "Em hardware real",
        "Usada num telemóvel real contra a bancada de testes do CM5; os ecrãs solar, elétrico e de centrais de alarme esperam nós reais",
      ],
      [
        "Licença",
        "GPL-3.0-or-later",
      ],
    ],
    "status": {
      "software": "A app compila (`gradlew testDebugUnitTest assembleDebug`) e funciona num telemóvel real contra a bancada de testes CM5.",
      "tests": "Passam 367 testes unitários (`gradlew testDebugUnitTest`): segurança dos endereços, decisão de alarme, vigilante de alarmes, traduções e papel só de leitura.",
      "ui": "O início de sessão, o monitor de câmaras, o armar e os alarmes e o radar estão em uso num telemóvel real; a configuração de um nó por Bluetooth não foi confirmada com um nó real, e os ecrãs solar, elétrico e de painel de alarme não encontraram equipamentos reais.",
      "hardware": "Usada num telemóvel real contra a bancada de testes CM5; a vigilância de alarmes em segundo plano sob as regras de bateria de cada fabricante não está provada.",
      "security": "As regras de segurança dos endereços e do papel só de leitura estão cobertas por testes unitários; não houve revisão independente.",
      "updates": "As atualizações a partir do GitHub estão em uso no telemóvel.",
      "integration": "O push através do Firebase está na app, mas precisa de um projeto Firebase próprio e não foi experimentado num telemóvel.",
      "docs": "Oito idiomas e o registo de alterações estão atualizados.",
    },
    "docs": [
      "[Limites do cliente](docs/CLIENT_BOUNDARY.md): o que o cliente faz e nunca faz",
      "[Notificações push](docs/PUSH_NOTIFICATIONS.md): os passos do Firebase, em oito línguas",
      "[Testes de bancada](docs/BENCH_TESTS.md): verificações com um telemóvel real",
    ],
    "contributing_first": "Antes de um pull request, execute `.\\gradlew.bat testDebugUnitTest` and `python -I tools/armor_ci_validate.py`: tem de passar. Consulte [CONTRIBUTING.md](CONTRIBUTING.md) e o [código de conduta](CODE_OF_CONDUCT.md).",
    "languages_extra": "",
    "body": {
      "overview": r"""* **Acesso com o login do próprio servidor:** IP, porta, utilizador e palavra-passe; a palavra-passe cria uma sessão HttpOnly; só fica guardada no telemóvel se marcar **Lembrar-me** (desligado por defeito: utilizador e palavra-passe cifrados com uma chave própria do Keystore, só para esse servidor, e esquecidos assim que desmarcar). Um papel **viewer** só observa: todo o botão que altera algo está desligado.
* **Bloqueio com o telemóvel:** a aplicação pede a impressão digital, o rosto ou o PIN do próprio telemóvel antes de armar, desarmar, silenciar uma sirene, desbloquear e as outras ordens críticas (ativado por predefinição só se o telemóvel tiver impressão digital ou rosto) e, se o ativares, para abrir a aplicação. O teu administrador pode exigi-lo a partir do Studio mas nunca baixar o que escolheste; um telemóvel sem bloqueio de ecrã nunca fica de fora e o ecrã bloqueado oferece sempre iniciar sessão de novo com a palavra-passe. Opcionalmente (desativado por defeito, com um aviso visível) a chave que sela a sessão guardada pode ser ligada ao desbloqueio do telemóvel; então a vigilância de alarmes em segundo plano espera, depois de um reinício, que desbloqueie o telemóvel.
* **Monitor de câmaras:** de 1 a 16 mosaicos, uma vista ampliada, MJPEG em direto que mantém a proporção, um comando PTZ limitado, fotografias e gravações, com visualizador e confirmação de apagamento das gravações.
* **Armar e desarmar,** depois de uma **verificação antes de armar** (o que está aberto, mudo ou em baixo) e com o PIN para desarmar; **alarmes** a reconhecer, com um distintivo para os que esperam; **dispositivos** (fumo, gás, inundação, porta, janela, movimento, clima, tomadas, luzes, sirenes, fechaduras, estores, motores de portão e garagem, esquentadores) com o seu estado e Ligar / Desligar / Alternar.
* **Alarmes que o alcançam:** um som para cada gravidade, um **alarme falado** opcional, avisos de um nó que chega a ALTO, uma câmara muda, um alarme de dispositivo e (armado) um nó desligado, e **uma central que toca acorda o telemóvel**; a vigilância em segundo plano sobrevive a um reinício e recua quando o servidor está em baixo.
* **Radar em direto, em 2D e 3D:** o separador Radar desenha o local como foi desenhado no Studio e as pessoas que os radares veem a mover-se nele, atualizado a cada segundo e meio; arraste, aperte e rode a vista 3D.
* **Energia solar e elétrica:** os totais (sol, consumo, baterias com a sua carga, se há rede), cada inversor e bateria com as células a pedido, e os canais e alarmes dos nós elétricos.
* **Centrais de alarme:** o estado de cada nó ARMOR-NODE-ALARM, as suas zonas e eventos, e comandos de armar / desarmar quando o servidor os permite.
* **Rede:** os dispositivos da rede da casa, o estado da internet e o **endereço público** com o fornecedor e o local, como o nó de rede os comunica.
* **Configurar um nó de campo por Bluetooth** (a partir do ecrã de acesso ou *Mais > Configurar um nó*): encontra os nós que anunciam `ARMOR-xxxxxx`, cria o administrador de um novo ou entra (com o PIN do nó), procura redes Wi-Fi e define o nome do nó, o Wi-Fi de um router ou um endereço fixo e o broker; um **localizador de nós** lista os que já estão na rede.
* **O assistente:** comandos escritos e falados (lista fechada, em oito idiomas, com uma confirmação ligada a si) para perguntar o estado da casa ou armar, desarmar, silenciar e ligar ou desligar luzes.
* **Biblioteca de provas,** estado do perímetro e dos nós, um **histórico** de cada alerta, nó, câmara, dispositivo, alarme e mudança de modo, o **mapa do tempo**, e os **serviços** e atualizações da instalação.
* **Oito idiomas** (inglês, espanhol, alemão, francês, italiano, japonês, chinês e português), escolhidos em *Mais > Definições* ou seguindo o telemóvel; verifica-se que cada frase está nas oito tabelas.
* **Cuidado com a palavra-passe:** HTTP simples só é permitido para um *literal* IPv4 de LAN privada ou loopback; um nome de anfitrião que só começa como um endereço privado (`10.attacker.example`) ou um endereço com zero à esquerda é recusado. O aspeto é feito de ícones: superfícies quase pretas, um destaque ciano, âmbar para a atenção.
* **Segurança a partir do telemóvel:** o segundo fator e os seus códigos de recuperação, as sessões abertas, uma verificação de como o servidor vê o telemóvel, a nova prova de identidade para ações críticas de fora e, para um administrador, a VPN (dispositivos com a sua configuração) e o nome de DNS dinâmico.
* **Todo o sistema no ecrã de estado e a entrada a partir de fora:** o ecrã de estado resume as centrais de alarme, os serviços, as câmaras que gravam e a segurança e o acesso remoto, e cada cartão abre o seu ecrã; e quando o endereço escrito está fora de casa e sem https, o início de sessão diz porque não pode continuar e um guia explica as duas vias seguras (VPN, ou endereço público com https).
* **Saúde dos nós e modos de armar:** um ecrã Saúde dos nós em Mais (tempo ligado, motivo do reinício, memória, ligação e sinal, ligações ao broker, reinícios, último erro e os avisos do servidor de cada nó) e, no ecrã das Centrais de alarme, um seletor de modo (Ausente, Em casa, Noite e os seus) que arma uma central no modo escolhido quando o seu firmware os conhece. Oito idiomas.
* **Ligações no histórico:** o ecrã Histórico tem uma segunda lista, só de leitura, com os dispositivos e aplicações que se ligam ao servidor (o Studio, esta app, os painéis dos nós, o serviço de voz), quando cada um foi visto pela última vez, as suas sessões abertas e os seus inícios de sessão e recusas; a app diz agora ao servidor o que é, para aparecer como ela própria. Os endereços só os veem os administradores.
* **Manutenção de baterias (administradores):** as operações simples numa bateria Pylontech - relógio, contadores e registos, reinício, capacidade, teste de MOSFET, falha de fusível, saídas - nos mesmos dois passos do Studio (o servidor faz o nó ler a bateria, o ecrã mostra exatamente o que será feito e depois "Fazer agora" com o número de série escrito outra vez), com o resultado e o que mudou; os limites, o firmware e a consola de especialista ficam no Studio.
* **Controlo dos nós (administradores):** Mais > Controlo dos nós dá as mesmas operações do Studio - reiniciar, pausar, retomar, pôr em espera (trabalho desligado, continua ligado), identificar, diagnóstico e manutenção ligada ou desligada - a um nó ou a todos, pedindo que se escreva de novo o nome do nó (ou a palavra RESTART, PAUSE ou STANDBY para todos) e a nova prova de identidade, mostrando até onde chegou cada nó e avisando que uma central de alarme ou um radar em pausa ou em espera deixa a casa sem proteção. Não existe reposição de fábrica, apagamento nem sono profundo.
* **Uma janela de alarme na aplicação aberta:** enquanto um alarme aguarda uma pessoa, um aviso sobre todos os ecrãs exceto o dos alarmes pulsa (vermelho e rápido se for crítico, âmbar nos restantes, parado se o telemóvel tiver as animações desligadas), diz qual é o pior alarme e quantos aguardam, e deixa usar a aplicação por baixo; pode abrir os alarmes, confirmar a partir do aviso ou ser fechado até chegar outro alarme.
* **A partir de fora de casa:** dois endereços (o privado na Wi-Fi de casa, o de fora com dados móveis ou a VPN) escolhidos conforme onde está o telemóvel, tentando o outro se um não responder e com uma mensagem que diz o que falha; a chave do certificado da instalação é memorizada na primeira vez (ou emparelhada com o texto do QR do Studio) e uma diferente é recusada, e o http simples é recusado para um servidor a que já se chegou por https; o painel de um nó pode abrir-se através do servidor; os alarmes podem chegar como push só com dados, anunciados uma vez venham por push ou pela vigilância; a app aberta e a vigilância partilham uma leitura do servidor; as câmaras param fora do ecrã e voltam com esperas crescentes.
* **Avisos à sua medida, com sons e uma voz próprios:** nas definições, silenciar todos os avisos, mostrá-los sem som nem vibração (e sem os dizer em voz alta) e desativá-los por gravidade (alta, baixa) ou por tipo (alertas do radar, câmaras que não respondem, nós desligados ou calados, e os alarmes de dispositivos, solar, elétrico, rede e painéis de alarme); um alarme crítico avisa sempre, a menos que todos os avisos estejam silenciados. Um som para cada gravidade e cada tipo de aviso, dos sons do telemóvel ou de um ficheiro seu (menos de 3 MB), cada um com um botão de reprodução; e a voz que diz os alarmes (mulher, homem ou qualquer; criança, adulto ou idoso; normal, herói de ação ou senhor das trevas; velocidade; e se os avisos de gravidade baixa também são ditos) com um botão de teste.
* **Um banner que leva ao ecrã certo e uma vigilância mais calma:** o banner de um alarme abre o ecrã que o trata (câmaras, dispositivos, inversores ou baterias, o ecrã elétrico, a rede ou os painéis de alarme); o telemóvel diz a sua língua ao registar-se para push para o aviso ser escrito nela, e um novo token do Firebase chega logo ao servidor a partir do segundo plano. Uma câmara com duas lentes numa só transmissão são duas janelas da lista de câmaras. Enquanto os avisos push funcionam, a vigilância em segundo plano consulta o servidor a cada 120 s em vez de a cada 10 (*Definições > Vigilância com avisos push*: 10, 60, 120, 300 ou 600 s).""",
      "role": r"""O ARMOR-ANDROID-CONTROL é a janela do telemóvel para o mesmo [ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER) que o [ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) usa: lê e ordena através dele e de nada mais. É onde os alarmes o seguem (uma central que toca acorda o telemóvel), onde pergunta ao assistente por voz, e a ferramenta para configurar um nó novo por Bluetooth no terreno, ao lado dele.

| Nome | Como | Para quê |
|---|---|---|
| ARMOR-SERVER | HTTP `/api/v1` (55 paths), MJPEG | Tudo o que a app lê e ordena |
| Nós de campo | Bluetooth (`ARMOR-xxxxxx`) | Configura um nó novo estando ao lado dele |
| GitHub | HTTPS | Verifica e descarrega a atualização assinada da própria app |
| Open-Meteo | HTTPS | A previsão, a qualidade do ar e a pesquisa de locais públicas do mapa do tempo |""",
      "architecture": r"""<p align="center">
  <img src="images/architecture.svg" alt="Arquitetura de ARMOR-ANDROID-CONTROL: quem o chama, o que contém e de que depende" width="100%">
</p>""",
      "security": r"""| Ameaça | Defesa |
|---|---|
| Uma palavra-passe guardada no telemóvel | Só com *Lembrar-me* (desligado por omissão): utilizador e palavra-passe selados com uma chave Keystore própria, só para esse servidor, esquecidos ao desmarcar; sem cópia de segurança (`allowBackup=false`) |
| HTTP simples para a internet | Permitido só para um *literal* IPv4 de rede privada ou loopback; um anfitrião como `10.attacker.example` ou um endereço com zero à esquerda (`010.0.0.1` lê-se em octal) é recusado; o http simples é recusado para um anfitrião alcançado por https |
| Um homem do meio em https | A confiança são as autoridades do sistema mais as que instalou no telemóvel; a chave do certificado da instalação é memorizada à primeira vez (ou emparelhada pelo texto do QR do Studio) e uma diferente é recusada |
| Uma ordem crítica com o telemóvel noutras mãos | A impressão digital, o rosto ou o PIN do telemóvel antes de armar, desarmar, silenciar uma sirene, desbloquear e as outras ordens críticas (ativo por omissão só se o telemóvel tiver impressão digital ou rosto); o administrador pode exigi-lo no Studio, nunca baixar o que escolheu; um telemóvel sem bloqueio nunca fica de fora |
| Um visualizador altera algo | O papel *visualizador* vê tudo mas todos os botões que alteram algo estão desligados (testes de papel) |
| Um PIN de desarmar errado | O PIN só vai para o servidor ao desarmar; `wrong_pin`, `pin_locked`, `pin_not_set` e `elevation_required` são traduzidos em palavras simples |
| Uma atualização falsa da app | Os SHA-256 dos certificados de assinatura (histórico) da app instalada e do candidato são comparados antes de chamar o instalador do Android; se não partilharem nenhum, diz-se claramente |
| Um alarme que o telemóvel não vê | Um serviço em primeiro plano (`AlarmWatcherService`) consulta a cada 10 s, espera 15 s pelo desbloqueio, recua até 60 s, diz *inacessível* após 6 falhas e sobrevive ao reinício; um alarme com mais de 15 minutos não é anunciado |
| Uma palavra-passe de câmara no telemóvel | As câmaras veem-se pelo fluxo do servidor: a app não tem palavra-passe de câmara nem endereço RTSP |

### Permissões

`INTERNET`, `ACCESS_NETWORK_STATE`: o servidor. `USE_BIOMETRIC`: o bloqueio do telemóvel. `POST_NOTIFICATIONS`: os alarmes. `FOREGROUND_SERVICE` (+ `DATA_SYNC`, `SPECIAL_USE`) e `RECEIVE_BOOT_COMPLETED`: a vigilância de alarmes. `REQUEST_INSTALL_PACKAGES`: a atualização da app. `BLUETOOTH_SCAN`, `BLUETOOTH_CONNECT`: a configuração de um nó; `BLUETOOTH`, `BLUETOOTH_ADMIN` e `ACCESS_FINE_LOCATION` só até ao Android 11 (`maxSdkVersion=30`), para a procura Bluetooth.

Não houve revisão de segurança independente. Leia [docs/CLIENT_BOUNDARY.md](docs/CLIENT_BOUNDARY.md) e [SECURITY.md](SECURITY.md).""",
      "interfaces": r"""| Parte | O que define |
|---|---|
| ARMOR-SERVER | 55 caminhos distintos de `/api/v1` em `network/ArmorApiClient.kt` (a interface é `network/ArmorApi.kt`); o radar lê-se a cada 1,5 s; as câmaras por MJPEG através do servidor |
| Dois endereços | O privado no Wi-Fi de casa e o de fora (dados móveis ou a VPN), escolhidos conforme onde está o telemóvel; se um não responder tenta-se o outro e a mensagem diz o que falha |
| Bluetooth | Encontra os nós que anunciam `ARMOR-xxxxxx`, cria o administrador de um novo ou entra com o PIN do nó, procura redes Wi-Fi e define o nome, o Wi-Fi ou um endereço fixo e o broker; o protocolo é `model/NodeBle.kt`; um localizador de nós lista os que já estão na rede |
| Voz | `POST /api/v1/voice/command`: uma lista fechada de comandos em oito línguas, com uma confirmação ligada a si (`model/Voice.kt`, `VoiceScreens.kt`) |
| Push | `PushService`: alarmes como mensagens só com dados, anunciados uma vez venham por push ou pela vigilância; os passos do Firebase estão em [docs/PUSH_NOTIFICATIONS.md](docs/PUSH_NOTIFICATIONS.md) (oito línguas) |""",
      "configuration": r"""| Nome | Valor | O que define |
|---|---|---|
| `compileSdk` / `targetSdk` / `minSdk` | 37 / 37 / 26 | Android 8.0 ou posterior no telemóvel |
| `versionName` | = `armor.project.json` | A compilação falha se o manifesto e a versão diferirem |
| JDK / Android SDK | 17+ / 37 | Para compilar a app e executar os testes |

Na app (não em ficheiros): a língua (as oito ou seguir o telemóvel), os dois endereços, *Lembrar-me*, o bloqueio do telemóvel, o alarme falado e as notificações, em *Mais > Definições*. Limites no código: a vigilância consulta a cada 10 s, recua até 60 s e ignora alarmes com mais de 15 minutos.""",
      "quickstart": r"""**Requisitos:** JDK 17+, o Android SDK (compile SDK 37), um telemóvel com Android 8.0+ (minSdk 26).

```powershell
.\gradlew.bat testDebugUnitTest assembleDebug   # 367 tests, then the debug APK
adb install -r app\build\outputs\apk\debug\app-debug.apk
```

As versões são publicadas no GitHub, de onde a própria aplicação procura atualizações; o APK é assinado com a chave de publicação própria do responsável, guardada fora do repositório, e a aplicação compara o certificado de assinatura de uma transferência com o seu antes de passar o ficheiro ao instalador do Android. Veja o [limite do cliente](docs/CLIENT_BOUNDARY.md).""",
      "testing": r"""```powershell
.\gradlew.bat testDebugUnitTest
python -I tools/armor_ci_validate.py
```

| Parte | Testes | O que cobre |
|---|---|---|
| Alarmes | 67 | `AlarmPolicy`, `AlarmBanner`, `AlarmPanels`, `AlarmCodes`, `AlarmRoute`, `NoticeFilter`, `PushEvents`, `DevicesAndAlarms` |
| Ligação ao servidor, leitura, dados de teste | 59 | `ApiClient`, `ApiError`, `ServerFixtures`, `ParsersTolerant`, `SavePayload`, `JsonText`, `Preflight`, `SharedFeed`, `Connections` |
| Modelo de vista e papéis | 41 | `ArmorViewModel`, `Viewer`, `ArmProfiles`, `NodeCensus`, `NodeHealth` |
| Bloqueio, cofre da sessão, chaves | 38 | `DeviceLock`, `SessionVault`, `CredentialVault`, `KeyBinding`, `Security` |
| Segurança de endereços, certificados | 32 | `ServerEndpoint`, `ServerAddresses`, `Literals`, `NodeAddress`, `CertificatePins`, `RemoteAccess` |
| Energia e rede | 34 | `Solar`, `Battery`, `Electrical`, `Network` |
| Nós por Bluetooth, controlo de nós | 26 | `NodeBle`, `NodeControl` |
| Atualizações do GitHub | 17 | `GitHubReleaseUpdaterHttpFailure`, `SignerCheck`, `SemanticVersion`, `ReleaseMetadataParser` |
| Radar e câmaras | 14 | `RadarGeometry`, `CameraTraits`, `CameraLenses` |
| Traduções, palavras simples, voz | 14 | `Tr`, `Friendly`, `Voice` |

367 testes em 47 ficheiros, executados com `testDebugUnitTest`; um servidor falso (`FakeServer.kt`) e dados tirados de um servidor real (`tools/capture_fixtures.mjs`) alimentam-nos. Verifica-se que cada frase está nas oito tabelas de língua.""",
      "build": "As versões são publicadas no GitHub, de onde a própria app verifica as atualizações; a app procura o recurso `ARMOR-ANDROID-CONTROL-release.apk`. O APK é assinado com a chave de versão do mantenedor, guardada fora do repositório, e a app compara o certificado de assinatura de uma transferência com o seu antes de passar o ficheiro ao instalador do Android. O `versionCode` sobe antes de cada APK, senão o Android não o trata como atualização.",
      "troubleshooting": r"""| Vê | Porque | Faça |
|---|---|---|
| `wrong_pin`, `pin_locked`, `pin_not_set`, `elevation_required` | O servidor recusa o PIN de desarmar ou pede uma nova prova de identidade | Escreva o PIN de novo, espere o fim do bloqueio ou confirme a sua identidade |
| O início de sessão diz que não pode continuar | O endereço está fora de casa e não tem https (o http simples é recusado) | Siga o guia: uma VPN, ou um endereço público com https |
| A ligação é recusada depois de ter funcionado | A chave do certificado da instalação mudou | Emparelhe de novo com o texto do QR do Studio se o mudou de propósito |
| Os alarmes chegam tarde ou não chegam em segundo plano | As regras de bateria do fabricante param a vigilância; o push precisa de um projeto Firebase próprio | Exclua a app da poupança de bateria; siga [docs/PUSH_NOTIFICATIONS.md](docs/PUSH_NOTIFICATIONS.md) |
| A atualização é recusada | O certificado de assinatura da transferência não partilha nenhum com a app instalada | Não o instale; use o APK das versões deste repositório |""",
      "structure": r"""<p align="center">
  <img src="images/repository-structure.svg" alt="Estrutura do repositório de ARMOR-ANDROID-CONTROL" width="100%">
</p>

<details>
<summary>Versão em texto da árvore</summary>

```text
ARMOR-ANDROID-CONTROL/
├── app/src/main/java/es/electrohobby3d/armor/   a app: ecrãs, regras, rede e atualizações
├── app/src/main/assets/                         oito tabelas de língua, códigos de alarme, mapa do tempo
├── app/src/test/                                367 testes e um servidor falso
├── docs/                                        os guias deste repositório
├── tools/                                       as verificações de CI partilhadas e as ferramentas do projeto
├── .github/                                     fluxo de CI e modelos de issues e pull requests
├── images/                                      faixa, ícone e as duas imagens deste README
├── build.sh build.bat                           compilar pelo fluxo de projeto partilhado
├── test.sh test.bat                             executar os testes pelo fluxo partilhado
├── run.sh run.bat                               arrancar pelo fluxo de projeto partilhado
├── armor.project.json                           manifesto: versão, função, maturidade, comando de build
├── CHANGELOG.md                                 o que mudou em cada versão
├── SECURITY.md SUPPORT.md LICENSE               política de segurança, apoio e licença
├── CONTRIBUTING.md CODE_OF_CONDUCT.md           como contribuir e o código de conduta
├── build.gradle.kts settings.gradle.kts         a compilação Gradle do projeto
├── gradle.properties                            definições do Gradle
├── gradlew gradlew.bat gradle/                  o wrapper do Gradle
├── build-test.sh build-test.bat                 executar os testes pelo fluxo partilhado
└── .gitattributes .gitignore                    definições do Git
```

</details>""",
      "roadmap": r"""**Limites conhecidos hoje**

* Os ecrãs de solar, elétrico e painel de alarme não conheceram equipamento real (só existe um nó radar).
* A configuração Bluetooth de um nó não foi confirmada com um nó real, e o push via Firebase não foi experimentado num telemóvel.
* A vigilância de alarmes em segundo plano sob as regras de bateria de cada fabricante não está provada.
* Sem revisão de segurança independente.

**A seguir**

* Experimentar os ecrãs de solar, elétrico e painel de alarme com nós reais, e a configuração Bluetooth com um nó real.
* Experimentar o push via Firebase com o projeto próprio de uma instalação, e a vigilância de alarmes em vários fabricantes.""",
    },
  },
}
