# The facts that do not depend on the language, and the words of every language, of ARMOR-IOS-CONTROL, in the universal README layout.
# Copyright (C) 2026 JuanenRac (Electro Hobby 3D). GPL-3.0-or-later.

FACTS = {
  "emoji": "📱",
  "layout": "universal",
  "license_badge": "License-GPL%203.0--or--later-blue",
  "status": [
    [
      "software",
      "orange",
    ],
    [
      "tests",
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
      "orange",
    ],
    [
      "integration",
      "orange",
    ],
    [
      "docs",
      "yellow",
    ],
  ],
  "badges": [
    [
      "Language",
      "Swift",
      "f05138",
    ],
    [
      "UI",
      "SwiftUI",
      "0a84ff",
    ],
    [
      "Languages",
      "8",
      "00E5FF",
    ],
    [
      "Tests",
      "146%20passing",
      "2ea44f",
    ],
  ],
}

TEXT = {
  "en": {
    "tagline": "iPhone operator client for ARMOR-SERVER: status, arming, alarms, alarm panels, cameras and the assistant, in eight languages",
    "honest": "the rules of the app (server link, parsing, choice of address, lock of the phone, vault of the session, trust in the certificate, alarm policy, use cases, MJPEG cutting) are the Swift package `ArmorCore`, covered by 146 unit tests that run with `swift test` on macOS or Linux, and `tools/ios_lint.py` checks the structure, the eight language tables and the contract without a Mac. What is **not** proven yet: the SwiftUI screens and the parts that need an iPhone (Face ID, Keychain, certificate rules, live camera, push through Firebase) have not been built in Xcode or run on a device.",
    "glance": [
      [
        "Role",
        "iPhone operator client for ARMOR-SERVER (family: Clients, parent: ARMOR-SERVER)",
      ],
      [
        "Stack",
        "Swift 5.9+ / SwiftUI, iOS 16+",
      ],
      [
        "Tests",
        "146 (`swift test`)",
      ],
      [
        "Languages",
        "8 (241 phrases per language, checked by `ios_lint.py`)",
      ],
      [
        "Runs on",
        "An iPhone with iOS 16+; the tests run on macOS or Linux",
      ],
      [
        "On real hardware",
        "Not run on an iPhone yet; the rules are tested on Linux",
      ],
      [
        "License",
        "GPL-3.0-or-later",
      ],
    ],
    "status": {
      "software": "The rules of the app are a Swift package (`ArmorCore`); the SwiftUI screens have not been built in Xcode.",
      "tests": "146 unit tests pass with `swift test` on macOS or Linux, and `tools/ios_lint.py` checks the structure, the eight language tables and the contract without a Mac; no test runs on a device.",
      "ui": "The SwiftUI screens are written but have not been built in Xcode or run on an iPhone.",
      "hardware": "It has not run on an iPhone: the rules are tested on Linux only.",
      "security": "The lock of the phone, the session vault and the trust in the certificate are rules tested on Linux; Face ID, the Keychain and the certificate rules have not run on a device.",
      "integration": "Live camera and push through Firebase have not been tried; the server link and the parsing are tested against the shared contract.",
      "docs": "Eight languages and the changelog are up to date.",
    },
    "docs": [
      "[Client boundary](docs/CLIENT_BOUNDARY.md): what the client does and never does, and how to build it",
    ],
    "contributing_first": "Before a pull request run `swift test` and `python tools/ios_lint.py` and `python -I tools/armor_ci_validate.py`: it must pass. See [CONTRIBUTING.md](CONTRIBUTING.md) and the [code of conduct](CODE_OF_CONDUCT.md).",
    "languages_extra": "",
    "body": {
      "overview": r"""* **Sign in with the server's own login:** the addresses of the house (at home and away), user and password; the password creates an HttpOnly session; it is kept only if you tick **Remember me** (in the Keychain of this phone, never backed up). A **viewer** role only looks: every button that changes something is off.
* **Two addresses:** the private one on the home Wi-Fi, the one for away (a dynamic DNS name or the VPN) on mobile data; if one does not answer the other is tried, and the message says what failed.
* **Lock with the phone:** Face ID, Touch ID or the passcode before arming, disarming, silencing a siren, unlocking and the other critical orders (on by default only with Face ID or Touch ID), and, if you turn it on, to open the app. Your administrator can require it, never lower what you chose; a phone with no passcode is never shut out and the locked screen always offers signing in with the password. Optionally (off by default, with a warning) the saved session is readable only while the phone is unlocked.
* **Arm and disarm** after a check of what would be left blind or noisy, with the PIN to disarm; **alarms** to confirm, with a badge; the **alarm panels** (arm away or at home, disarm, silence the siren) and the **history**; **devices** with On / Off and a confirmation for circuits and critical ones.
* **Cameras** through the server (the app never has a camera password): a grid where only the pictures on screen run, a full view with a pad to move the camera and a snapshot, and a stream asked for again with growing waits when it drops.
* **Notices you choose:** silence everything or show it without sound; switch severities and kinds off (a critical alarm is never hidden, except by the switch that silences all); a sound file of your own for each severity and each kind, with a play button; and the voice that says the alarms (woman, man, age, style, speed, low-severity notices), with a test button. A camera with two lenses in one picture is shown as two windows.
* **The assistant:** written commands (the keyboard's microphone dictates), with a confirmation bound to you for arming and disarming, behind the lock.
* **Trust in the certificate:** the key of the installation's certificate is remembered the first time or paired with the QR of Studio; if it changes the connection is refused and you are told.
* **Eight languages** (English, Spanish, German, French, Italian, Japanese, Chinese and Portuguese of Portugal), chosen in *More > Language* or following the phone, with a help for every screen.""",
      "role": r"""ARMOR-IOS-CONTROL is the iPhone's window on the same [ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER) that [ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) and [ARMOR-ANDROID-CONTROL](https://github.com/JuanenRac/ARMOR-ANDROID-CONTROL) use: it reads and orders through it and nothing else, and it speaks the same contract as the Android app.

| Name | How | What for |
|---|---|---|
| ARMOR-SERVER | HTTP `/api/v1`, MJPEG | Everything the app reads and orders; the app talks to nothing else |
| ARMOR-ANDROID-CONTROL | same contract | `ios_lint.py` checks that the app calls only paths the Android client calls |
| ARMOR-STUDIO | QR | Pairs the key of the certificate of the installation |""",
      "architecture": r"""<p align="center">
  <img src="images/architecture.svg" alt="ARMOR-IOS-CONTROL architecture: who calls it, what it holds and what it depends on" width="100%">
</p>""",
      "security": r"""| Threat | Defence |
|---|---|
| The password on the phone | Kept only with *Remember me*, in the Keychain of this phone and never backed up; the session is an HttpOnly cookie of the server |
| A critical order with the phone in other hands | Face ID, Touch ID or the passcode before arming, disarming, silencing a siren, unlocking and the other critical orders; the administrator can require it, never lower what you chose; a phone with no passcode is never shut out |
| A changed or forged certificate | The key of the installation's certificate is remembered the first time or paired with the QR of Studio; if it changes the connection is refused and you are told |
| The password sent in clear | Plain HTTP only for a private-network or loopback address (`NSAllowsLocalNetworking`); anything else needs https and the app refuses to send the password otherwise |
| A camera password on the phone | The cameras pass through the server: the app has no camera password and no RTSP address |
| A viewer changes something | The *viewer* role only looks: every button that changes something is off; the server checks it again |
| The assistant arms or disarms by mistake | Written commands only (the keyboard's microphone dictates); arming and disarming need a confirmation bound to you, behind the lock of the phone |

Permission texts (Face ID, local network) exist in all eight languages. Nothing here has run on an iPhone: Face ID, the Keychain and the certificate rules are untested on a device. Read [docs/CLIENT_BOUNDARY.md](docs/CLIENT_BOUNDARY.md) and [SECURITY.md](SECURITY.md).""",
      "interfaces": r"""It is a client: it calls 26 paths of ARMOR-SERVER (`tools/ios_lint.py` counts them and checks that the Android client calls them too), and cuts the MJPEG stream of the cameras with its own parser (`MjpegParser.swift`).

| Part | What it sets |
|---|---|
| Two addresses | The private one on the home Wi-Fi and the one for away (a dynamic DNS name or the VPN) on mobile data; if one does not answer the other is tried, and the message says what failed (`Reach.swift`, `Connector.swift`) |
| Cameras | A grid where only the pictures on screen run, a full view with a pad to move the camera and a snapshot, and a stream asked for again with growing waits when it drops |
| Push | Alarms reach a closed app only through push (`Push.swift`, Firebase), and only when the server has push on and the installation brings its own `GoogleService-Info.plist`; not tried |""",
      "configuration": r"""| Name | Value | What it sets |
|---|---|---|
| iOS | 16.0+ | Minimum version, set in `project.yml` |
| Xcode / Swift | 15+ / 5.9+ | To build the app / to run the tests |
| `MARKETING_VERSION`, `CURRENT_PROJECT_VERSION` | 0.0.1, 1 | The version of the app, from `project.yml` |
| `GoogleService-Info.plist` | for push | The installation's own file, never kept in the repository |

In the app: the two addresses, *Remember me*, the lock of the phone and the language (the eight languages or following the phone) in *More > Language*.""",
      "quickstart": r"""**Requirements:** a Mac with Xcode 15+ and iOS 16+ to build the app; Swift 5.9+ (macOS or Linux) for the tests; Python 3.11 for the checks.

```sh
swift test                  # 146 tests of ArmorCore (macOS or Linux)
python tools/ios_lint.py    # structure, eight languages, contract (any system)
xcodegen generate           # then open ARMOR-IOS-CONTROL.xcodeproj in Xcode (on a Mac)
```

The Xcode project is made from `project.yml` with XcodeGen. Choose a signing team, add the app icon and, for push, the installation's `GoogleService-Info.plist` (never kept in the repository). See the [client boundary](docs/CLIENT_BOUNDARY.md).""",
      "testing": r"""```sh
swift test                  # macOS or Linux
python tools/ios_lint.py    # any system, no Mac needed
python -I tools/armor_ci_validate.py
```

| Test file | Tests | What it covers |
|---|---|---|
| `ControllerTests.swift` | 15 | The use cases of the controller |
| `ClientTests.swift` | 14 | The link to the server and its parsing |
| `LockTests.swift` | 12 | The lock of the phone |
| `ModelsTests.swift` | 12 | The models read from the server |
| `ReachTests.swift` | 11 | The choice between the two addresses |
| `SecurityTests.swift` | 8 | The session vault and the trust in the certificate |
| `EndpointTests.swift`, `MjpegTests.swift`, `TranslatorTests.swift` | 7 + 7 + 7 | The address parsing, the MJPEG cutting and the translator |
| `PolicyTests.swift`, `AlarmCodesTests.swift` | 6 + 4 | The alarm policy and the alarm codes |

The 146 tests run with fixtures of a real server. `tools/ios_lint.py` passes without a Mac: 31 Swift files, 241 phrases in 8 languages, 26 server paths. No test runs on a device.""",
      "build": "The Xcode project is generated from `project.yml` with XcodeGen: choose a signing team, add the app icon to `App/Resources/Assets.xcassets/AppIcon.appiconset` and, for push, the installation's `GoogleService-Info.plist`. It has never been built in Xcode.",
      "troubleshooting": r"""| You see | Because | Do |
|---|---|---|
| The connection is refused and you are told | The key of the installation's certificate changed | Pair again with the QR of Studio if you changed it on purpose |
| Neither address answers | Wrong address, no network, or http to a place outside the home (refused: the password is not sent in clear) | Check both addresses; use https away from home |
| `wrong_pin`, `pin_locked`, `pin_not_set` | The server refuses the disarm PIN; the app shows the code in your language | Type the PIN again or wait for the lock to end; set it in Studio |""",
      "structure": r"""<p align="center">
  <img src="images/repository-structure.svg" alt="Repository structure of ARMOR-IOS-CONTROL" width="100%">
</p>

<details>
<summary>Text version of the tree</summary>

```text
ARMOR-IOS-CONTROL/
├── Sources/ArmorCore/                   the rules of the app: a Swift package
├── App/                                 the SwiftUI screens and the parts that need an iPhone
├── Tests/                               146 tests and fixtures of a real server
├── docs/                                the guides of this repository
├── tools/                               the shared CI checks and project tooling
├── .github/                             CI workflow, issue and pull-request templates
├── images/                              banner, icon and the two pictures of this README
├── armor.project.json                   manifest: version, role, maturity, build command
├── CHANGELOG.md                         what changed in each version
├── SECURITY.md SUPPORT.md LICENSE       security policy, support and license
├── CONTRIBUTING.md CODE_OF_CONDUCT.md   how to contribute and the code of conduct
├── Package.swift                        the Swift package: ArmorCore and its tests
├── project.yml                          XcodeGen: the Xcode project is generated from it
└── .gitattributes .gitignore            Git settings
```

</details>""",
      "roadmap": r"""**Known limits today**

* Nothing has run on an iPhone: the SwiftUI screens have not been built in Xcode; Face ID, the Keychain, the certificate rules, the live camera, the sounds of the notices, the voice and push through Firebase are untested.
* Only the rules (`ArmorCore`) are tested, and only on Linux.
* The app does not watch in the background: iOS does not let a closed app query the server.

**Next**

* Build the screens in Xcode and run the app on an iPhone against the CM5 test bench.
* Try Face ID, the Keychain, the certificate rules, the live camera and push.""",
    },
  },
  "es": {
    "tagline": "Cliente de operador para iPhone de ARMOR-SERVER: estado, armado, alarmas, centrales de alarma, cámaras y el asistente, en ocho idiomas",
    "honest": "las reglas de la app (enlace con el servidor, lectura de las respuestas, elección de dirección, bloqueo del teléfono, caja de la sesión, confianza en el certificado, política de alarmas, casos de uso, corte del MJPEG) son el paquete Swift `ArmorCore`, cubierto por 146 pruebas unitarias que se ejecutan con `swift test` en macOS o Linux, y `tools/ios_lint.py` comprueba la estructura, las ocho tablas de idiomas y el contrato sin Mac. Lo que **no** está demostrado todavía: las pantallas SwiftUI y las partes que necesitan un iPhone (Face ID, llavero, reglas de certificado, cámara en vivo, push con Firebase) no se han compilado en Xcode ni ejecutado en un dispositivo.",
    "glance": [
      [
        "Función",
        "Cliente de operador para iPhone de ARMOR-SERVER (familia: Clients, padre: ARMOR-SERVER)",
      ],
      [
        "Tecnología",
        "Swift 5.9+ / SwiftUI, iOS 16+",
      ],
      [
        "Pruebas",
        "146 (`swift test`)",
      ],
      [
        "Idiomas",
        "8 (241 frases por idioma, comprobadas por `ios_lint.py`)",
      ],
      [
        "Funciona en",
        "Un iPhone con iOS 16+; las pruebas corren en macOS o Linux",
      ],
      [
        "En hardware real",
        "Aún no se ha ejecutado en un iPhone; las reglas se prueban en Linux",
      ],
      [
        "Licencia",
        "GPL-3.0-or-later",
      ],
    ],
    "status": {
      "software": "Las reglas de la app son un paquete Swift (`ArmorCore`); las pantallas SwiftUI no se han compilado en Xcode.",
      "tests": "Pasan 146 pruebas unitarias con `swift test` en macOS o Linux, y `tools/ios_lint.py` comprueba la estructura, las tablas de los ocho idiomas y el contrato sin un Mac; ninguna prueba se ejecuta en un dispositivo.",
      "ui": "Las pantallas SwiftUI están escritas pero no se han compilado en Xcode ni ejecutado en un iPhone.",
      "hardware": "No ha funcionado en un iPhone: las reglas solo se prueban en Linux.",
      "security": "El bloqueo del teléfono, la caja de la sesión y la confianza en el certificado son reglas probadas en Linux; Face ID, el llavero y las reglas del certificado no se han ejecutado en un dispositivo.",
      "integration": "La cámara en vivo y el push mediante Firebase no se han probado; el enlace con el servidor y el análisis se prueban contra el contrato compartido.",
      "docs": "Ocho idiomas y el historial de cambios están al día.",
    },
    "docs": [
      "[Límites del cliente](docs/CLIENT_BOUNDARY.md): qué hace y qué nunca hace el cliente, y cómo compilarlo",
    ],
    "contributing_first": "Antes de un pull request ejecuta `swift test` and `python tools/ios_lint.py` and `python -I tools/armor_ci_validate.py`: debe pasar. Consulta [CONTRIBUTING.md](CONTRIBUTING.md) y el [código de conducta](CODE_OF_CONDUCT.md).",
    "languages_extra": "",
    "body": {
      "overview": r"""* **Inicia sesión con el acceso del propio servidor:** las direcciones de la casa (en casa y fuera), usuario y contraseña; la contraseña crea una sesión HttpOnly; solo se guarda si marcas **Recordarme** (en el llavero de este teléfono, sin copia de seguridad). El rol **viewer** solo mira: todo botón que cambia algo queda apagado.
* **Dos direcciones:** la privada en la wifi de casa y la de fuera (un nombre DNS dinámico o la VPN) con datos móviles; si una no responde se prueba la otra y el mensaje dice qué falla.
* **Bloqueo con el teléfono:** Face ID, Touch ID o el código antes de armar, desarmar, silenciar una sirena, desbloquear y las demás órdenes críticas (activado por defecto solo con Face ID o Touch ID) y, si lo activas, para abrir la app. Tu administrador puede exigirlo, nunca bajar lo que elegiste; un teléfono sin código nunca se queda fuera y la pantalla de bloqueo siempre ofrece entrar con la contraseña. Opcionalmente (desactivado, con aviso) la sesión guardada solo se lee con el teléfono desbloqueado.
* **Armar y desarmar** tras comprobar lo que quedaría ciego o ruidoso, con el PIN para desarmar; **alarmas** que confirmar, con contador; las **centrales de alarma** (armar fuera o en casa, desarmar, silenciar la sirena) y el **historial**; **dispositivos** con Encender / Apagar y confirmación para circuitos y críticos.
* **Cámaras** a través del servidor (la app nunca tiene la contraseña de la cámara): una cuadrícula donde solo corren las imágenes visibles, una vista completa con cruceta para mover la cámara y foto, y un flujo que se pide de nuevo con esperas crecientes si se corta.
* **Avisos a tu medida:** silenciar todo o mostrarlo sin sonido; apagar gravedades y tipos (una alarma crítica nunca se oculta, salvo con el interruptor que silencia todo); un archivo de sonido propio para cada gravedad y cada tipo, con botón de reproducir; y la voz que dice las alarmas (mujer, hombre, edad, estilo, velocidad, avisos de gravedad baja), con botón de prueba. Una cámara con dos objetivos en una imagen se muestra como dos ventanas.
* **El asistente:** órdenes escritas (el micrófono del teclado dicta), con una confirmación ligada a ti para armar y desarmar, detrás del bloqueo.
* **Confianza en el certificado:** la clave del certificado de la instalación se recuerda la primera vez o se empareja con el QR de Studio; si cambia, la conexión se rechaza y se te avisa.
* **Ocho idiomas** (inglés, español, alemán, francés, italiano, japonés, chino y portugués de Portugal), a elegir en *Más > Idioma* o siguiendo al teléfono, con ayuda para cada pantalla.""",
      "role": r"""ARMOR-IOS-CONTROL es la ventana del iPhone al mismo [ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER) que usan [ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) y [ARMOR-ANDROID-CONTROL](https://github.com/JuanenRac/ARMOR-ANDROID-CONTROL): lee y ordena a través de él y nada más, y habla el mismo contrato que la app de Android.

| Nombre | Cómo | Para qué |
|---|---|---|
| ARMOR-SERVER | HTTP `/api/v1`, MJPEG | Todo lo que la app lee y ordena; no habla con nada más |
| ARMOR-ANDROID-CONTROL | mismo contrato | `ios_lint.py` comprueba que la app solo llama a rutas que llama el cliente Android |
| ARMOR-STUDIO | QR | Empareja la clave del certificado de la instalación |""",
      "architecture": r"""<p align="center">
  <img src="images/architecture.svg" alt="Arquitectura de ARMOR-IOS-CONTROL: quién lo llama, qué contiene y de qué depende" width="100%">
</p>""",
      "security": r"""| Amenaza | Defensa |
|---|---|
| La contraseña en el teléfono | Solo se guarda con *Recordarme*, en el Keychain de este teléfono y nunca en copias de seguridad; la sesión es una cookie HttpOnly del servidor |
| Una orden crítica con el teléfono en otras manos | Face ID, Touch ID o el código antes de armar, desarmar, silenciar una sirena, desbloquear y otras órdenes críticas; el administrador puede exigirlo, nunca bajar lo que elegiste; un teléfono sin código nunca se queda fuera |
| Un certificado cambiado o falsificado | Se recuerda la clave del certificado de la instalación la primera vez o se empareja con el QR de Studio; si cambia se rechaza la conexión y se te avisa |
| La contraseña enviada en claro | HTTP plano solo para una dirección de red privada o loopback (`NSAllowsLocalNetworking`); lo demás exige https y la app se niega a enviar la contraseña de otro modo |
| Una contraseña de cámara en el teléfono | Las cámaras pasan por el servidor: la app no tiene contraseña de cámara ni dirección RTSP |
| Un visor cambia algo | El rol *visor* solo mira: todos los botones que cambian algo están apagados; el servidor lo vuelve a comprobar |
| El asistente arma o desarma por error | Solo órdenes escritas (el micrófono del teclado dicta); armar y desarmar exigen una confirmación atada a ti, tras el bloqueo del teléfono |

Los textos de permisos (Face ID, red local) existen en los ocho idiomas. Nada de esto ha corrido en un iPhone: Face ID, el Keychain y las reglas de certificado no se han probado en un dispositivo. Lee [docs/CLIENT_BOUNDARY.md](docs/CLIENT_BOUNDARY.md) y [SECURITY.md](SECURITY.md).""",
      "interfaces": r"""Es un cliente: llama a 26 rutas de ARMOR-SERVER (`tools/ios_lint.py` las cuenta y comprueba que el cliente Android también las llama) y corta el flujo MJPEG de las cámaras con su propio intérprete (`MjpegParser.swift`).

| Parte | Qué define |
|---|---|
| Dos direcciones | La privada en el Wi-Fi de casa y la de fuera (un nombre DNS dinámico o la VPN) con datos móviles; si una no responde se prueba la otra y el mensaje dice qué falló (`Reach.swift`, `Connector.swift`) |
| Cámaras | Una rejilla donde solo corren las imágenes visibles, una vista completa con mando para mover la cámara y una instantánea, y un flujo que se pide de nuevo con esperas crecientes si se corta |
| Push | Las alarmas llegan a una app cerrada solo por push (`Push.swift`, Firebase) y solo si el servidor tiene push activado y la instalación aporta su propio `GoogleService-Info.plist`; sin probar |""",
      "configuration": r"""| Nombre | Valor | Qué define |
|---|---|---|
| iOS | 16.0+ | Versión mínima, definida en `project.yml` |
| Xcode / Swift | 15+ / 5.9+ | Para compilar la app / para ejecutar las pruebas |
| `MARKETING_VERSION`, `CURRENT_PROJECT_VERSION` | 0.0.1, 1 | La versión de la app, de `project.yml` |
| `GoogleService-Info.plist` | para push | El fichero propio de la instalación, nunca guardado en el repositorio |

En la app: las dos direcciones, *Recordarme*, el bloqueo del teléfono y el idioma (los ocho o seguir al teléfono) en *Más > Idioma*.""",
      "quickstart": r"""**Requisitos:** un Mac con Xcode 15+ e iOS 16+ para compilar la app; Swift 5.9+ (macOS o Linux) para las pruebas; Python 3.11 para las comprobaciones.

```sh
swift test                  # 146 tests of ArmorCore (macOS or Linux)
python tools/ios_lint.py    # structure, eight languages, contract (any system)
xcodegen generate           # then open ARMOR-IOS-CONTROL.xcodeproj in Xcode (on a Mac)
```

El proyecto de Xcode se genera desde `project.yml` con XcodeGen. Elige un equipo de firma, añade el icono de la app y, para el push, el `GoogleService-Info.plist` de la instalación (nunca se guarda en el repositorio). Consulta el [límite del cliente](docs/CLIENT_BOUNDARY.md).""",
      "testing": r"""```sh
swift test                  # macOS or Linux
python tools/ios_lint.py    # any system, no Mac needed
python -I tools/armor_ci_validate.py
```

| Fichero de pruebas | Pruebas | Qué cubre |
|---|---|---|
| `ControllerTests.swift` | 15 | Los casos de uso del controlador |
| `ClientTests.swift` | 14 | El enlace con el servidor y su interpretación |
| `LockTests.swift` | 12 | El bloqueo del teléfono |
| `ModelsTests.swift` | 12 | Los modelos leídos del servidor |
| `ReachTests.swift` | 11 | La elección entre las dos direcciones |
| `SecurityTests.swift` | 8 | El almacén de sesión y la confianza en el certificado |
| `EndpointTests.swift`, `MjpegTests.swift`, `TranslatorTests.swift` | 7 + 7 + 7 | La lectura de direcciones, el corte MJPEG y el traductor |
| `PolicyTests.swift`, `AlarmCodesTests.swift` | 6 + 4 | La política de alarmas y los códigos de alarma |

Las 146 pruebas usan datos de un servidor real. `tools/ios_lint.py` pasa sin Mac: 31 ficheros Swift, 241 frases en 8 idiomas, 26 rutas del servidor. Ninguna prueba corre en un dispositivo.""",
      "build": "El proyecto de Xcode se genera desde `project.yml` con XcodeGen: elige un equipo de firma, añade el icono de la app a `App/Resources/Assets.xcassets/AppIcon.appiconset` y, para push, el `GoogleService-Info.plist` de la instalación. Nunca se ha compilado en Xcode.",
      "troubleshooting": r"""| Ves | Porque | Haz |
|---|---|---|
| Se rechaza la conexión y se te avisa | Cambió la clave del certificado de la instalación | Vuelve a emparejar con el QR de Studio si lo cambiaste a propósito |
| Ninguna de las dos direcciones responde | Dirección errónea, sin red, o http a un lugar fuera de casa (rechazado: la contraseña no se envía en claro) | Revisa las dos direcciones; usa https fuera de casa |
| `wrong_pin`, `pin_locked`, `pin_not_set` | El servidor rechaza el PIN de desarmado; la app muestra el código en tu idioma | Escribe el PIN de nuevo o espera a que acabe el bloqueo; defínelo en Studio |""",
      "structure": r"""<p align="center">
  <img src="images/repository-structure.svg" alt="Estructura del repositorio de ARMOR-IOS-CONTROL" width="100%">
</p>

<details>
<summary>Versión en texto del árbol</summary>

```text
ARMOR-IOS-CONTROL/
├── Sources/ArmorCore/                   las reglas de la app: un paquete Swift
├── App/                                 las pantallas SwiftUI y las partes que necesitan un iPhone
├── Tests/                               146 pruebas y datos de un servidor real
├── docs/                                las guías de este repositorio
├── tools/                               las comprobaciones de CI compartidas y las herramientas del proyecto
├── .github/                             flujo de CI y plantillas de issues y pull requests
├── images/                              banner, icono y las dos imágenes de este README
├── armor.project.json                   manifiesto: versión, rol, madurez, comando de build
├── CHANGELOG.md                         qué cambió en cada versión
├── SECURITY.md SUPPORT.md LICENSE       política de seguridad, soporte y licencia
├── CONTRIBUTING.md CODE_OF_CONDUCT.md   cómo contribuir y el código de conducta
├── Package.swift                        el paquete Swift: ArmorCore y sus pruebas
├── project.yml                          XcodeGen: de aquí se genera el proyecto de Xcode
└── .gitattributes .gitignore            ajustes de Git
```

</details>""",
      "roadmap": r"""**Límites conocidos hoy**

* Nada ha corrido en un iPhone: las pantallas SwiftUI no se han compilado en Xcode; Face ID, el Keychain, las reglas de certificado, la cámara en vivo, los sonidos de los avisos, la voz y el push de Firebase están sin probar.
* Solo las reglas (`ArmorCore`) están probadas, y solo en Linux.
* La app no vigila en segundo plano: iOS no deja que una app cerrada consulte al servidor.

**Lo siguiente**

* Compilar las pantallas en Xcode y ejecutar la app en un iPhone contra el banco de pruebas CM5.
* Probar Face ID, el Keychain, las reglas de certificado, la cámara en vivo y el push.""",
    },
  },
  "de": {
    "tagline": "iPhone-Bedienclient für ARMOR-SERVER: Status, Scharfschaltung, Alarme, Alarmzentralen, Kameras und der Assistent, in acht Sprachen",
    "honest": "Die Regeln der App (Serververbindung, Auswertung der Antworten, Adressauswahl, Telefonsperre, Tresor der Sitzung, Vertrauen in das Zertifikat, Alarmrichtlinie, Anwendungsfälle, MJPEG-Zerlegung) sind das Swift-Paket `ArmorCore`, abgedeckt durch 146 Unit-Tests, die mit `swift test` unter macOS oder Linux laufen; `tools/ios_lint.py` prüft Struktur, die acht Sprachtabellen und den Vertrag ohne Mac. **Noch nicht** belegt: Die SwiftUI-Bildschirme und die Teile, die ein iPhone brauchen (Face ID, Schlüsselbund, Zertifikatsregeln, Live-Kamera, Push über Firebase), wurden weder in Xcode gebaut noch auf einem Gerät ausgeführt.",
    "glance": [
      [
        "Rolle",
        "iPhone-Bedienclient für ARMOR-SERVER (Familie: Clients, übergeordnet: ARMOR-SERVER)",
      ],
      [
        "Technik",
        "Swift 5.9+ / SwiftUI, iOS 16+",
      ],
      [
        "Tests",
        "146 (`swift test`)",
      ],
      [
        "Sprachen",
        "8 (241 Sätze je Sprache, von `ios_lint.py` geprüft)",
      ],
      [
        "Läuft auf",
        "Ein iPhone mit iOS 16+; die Tests laufen auf macOS oder Linux",
      ],
      [
        "Auf echter Hardware",
        "Noch nicht auf einem iPhone ausgeführt; die Regeln werden unter Linux getestet",
      ],
      [
        "Lizenz",
        "GPL-3.0-or-later",
      ],
    ],
    "status": {
      "software": "Die Regeln der App sind ein Swift-Paket (`ArmorCore`); die SwiftUI-Bildschirme wurden nicht in Xcode gebaut.",
      "tests": "146 Unit-Tests bestehen mit `swift test` unter macOS oder Linux, und `tools/ios_lint.py` prüft Struktur, die Tabellen der acht Sprachen und den Vertrag ohne Mac; auf einem Gerät läuft kein Test.",
      "ui": "Die SwiftUI-Bildschirme sind geschrieben, wurden aber weder in Xcode gebaut noch auf einem iPhone ausgeführt.",
      "hardware": "Sie lief nicht auf einem iPhone: Die Regeln sind nur unter Linux getestet.",
      "security": "Die Sperre des Telefons, der Tresor der Sitzung und das Vertrauen ins Zertifikat sind unter Linux getestete Regeln; Face ID, der Schlüsselbund und die Zertifikatsregeln liefen nicht auf einem Gerät.",
      "integration": "Live-Kamera und Push über Firebase wurden nicht erprobt; die Serververbindung und das Parsen sind gegen den gemeinsamen Vertrag getestet.",
      "docs": "Acht Sprachen und das Änderungsprotokoll sind aktuell.",
    },
    "docs": [
      "[Client-Grenze](docs/CLIENT_BOUNDARY.md): was der Client tut und nie tut, und wie man ihn baut",
    ],
    "contributing_first": "Führe vor einem Pull Request `swift test` and `python tools/ios_lint.py` and `python -I tools/armor_ci_validate.py` aus: Es muss bestehen. Siehe [CONTRIBUTING.md](CONTRIBUTING.md) und den [Verhaltenskodex](CODE_OF_CONDUCT.md).",
    "languages_extra": "",
    "body": {
      "overview": r"""* **Anmeldung mit dem Login des Servers:** die Adressen des Hauses (zu Hause und unterwegs), Benutzer und Passwort; das Passwort erzeugt eine HttpOnly-Sitzung; es wird nur gespeichert, wenn Sie **Angemeldet bleiben** ankreuzen (im Schlüsselbund dieses Telefons, nie im Backup). Die Rolle **viewer** schaut nur: jede Schaltfläche, die etwas ändert, ist aus.
* **Zwei Adressen:** die private im Heim-WLAN, die für unterwegs (ein dynamischer DNS-Name oder das VPN) mit Mobilfunkdaten; antwortet eine nicht, wird die andere versucht, und die Meldung sagt, was fehlschlägt.
* **Sperre mit dem Telefon:** Face ID, Touch ID oder der Code vor Scharf- und Unscharfschalten, Sirene stummschalten, Entriegeln und den anderen kritischen Befehlen (standardmäßig nur mit Face ID oder Touch ID an) und, wenn Sie es einschalten, zum Öffnen der App. Ihr Administrator kann es verlangen, aber nie unter Ihre Wahl senken; ein Telefon ohne Code wird nie ausgesperrt, und der Sperrbildschirm bietet immer die Anmeldung mit dem Passwort an. Optional (aus, mit Warnung) ist die gespeicherte Sitzung nur bei entsperrtem Telefon lesbar.
* **Scharf- und Unscharfschalten** nach einer Prüfung dessen, was blind oder laut bliebe, mit der PIN zum Unscharfschalten; **Alarme** zum Bestätigen, mit Zähler; die **Alarmzentralen** (scharf abwesend oder zu Hause, unscharf, Sirene stumm) und der **Verlauf**; **Geräte** mit Ein / Aus und Bestätigung für Stromkreise und kritische Geräte.
* **Kameras** über den Server (die App hat nie das Kamerapasswort): ein Raster, in dem nur die sichtbaren Bilder laufen, eine Vollansicht mit Steuerkreuz zum Bewegen der Kamera und Foto, und ein Stream, der bei Abbruch mit wachsenden Wartezeiten neu angefordert wird.
* **Meldungen nach Wahl:** alles stummschalten oder ohne Ton anzeigen; Dringlichkeiten und Arten abschalten (ein kritischer Alarm wird nie ausgeblendet, außer mit dem Schalter, der alles stumm schaltet); eine eigene Tondatei für jede Dringlichkeit und jede Art mit Wiedergabetaste; und die Stimme, die die Alarme spricht (Frau, Mann, Alter, Stil, Tempo, Meldungen niedriger Dringlichkeit) mit Testtaste. Eine Kamera mit zwei Objektiven in einem Bild erscheint als zwei Fenster.
* **Der Assistent:** geschriebene Befehle (das Mikrofon der Tastatur diktiert), mit einer an Sie gebundenen Bestätigung für Scharf- und Unscharfschalten, hinter der Sperre.
* **Vertrauen in das Zertifikat:** Der Schlüssel des Zertifikats der Installation wird beim ersten Mal gemerkt oder mit dem QR-Code von Studio gekoppelt; ändert er sich, wird die Verbindung abgelehnt und Sie werden informiert.
* **Acht Sprachen** (Englisch, Spanisch, Deutsch, Französisch, Italienisch, Japanisch, Chinesisch und Portugiesisch aus Portugal), wählbar unter *Mehr > Sprache* oder dem Telefon folgend, mit einer Hilfe zu jedem Bildschirm.""",
      "role": r"""ARMOR-IOS-CONTROL ist das Fenster des iPhones zum selben [ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER), den auch [ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) und [ARMOR-ANDROID-CONTROL](https://github.com/JuanenRac/ARMOR-ANDROID-CONTROL) nutzen: Es liest und befiehlt nur über ihn und spricht denselben Vertrag wie die Android-App.

| Name | Wie | Wozu |
|---|---|---|
| ARMOR-SERVER | HTTP `/api/v1`, MJPEG | Alles, was die App liest und anordnet; sie spricht mit nichts anderem |
| ARMOR-ANDROID-CONTROL | gleicher Vertrag | `ios_lint.py` prüft, dass die App nur Pfade aufruft, die auch der Android-Client aufruft |
| ARMOR-STUDIO | QR | Koppelt den Schlüssel des Zertifikats der Installation |""",
      "architecture": r"""<p align="center">
  <img src="images/architecture.svg" alt="Architektur von ARMOR-IOS-CONTROL: wer es aufruft, was es enthält und wovon es abhängt" width="100%">
</p>""",
      "security": r"""| Bedrohung | Abwehr |
|---|---|
| Das Passwort auf dem Telefon | Nur mit *Angemeldet bleiben* gespeichert, im Keychain dieses Telefons und nie in Backups; die Sitzung ist ein HttpOnly-Cookie des Servers |
| Ein kritischer Befehl mit dem Telefon in fremden Händen | Face ID, Touch ID oder der Code vor Scharfschalten, Unscharfschalten, Sirene stummschalten, Entriegeln und den anderen kritischen Befehlen; der Administrator kann es verlangen, nie senken, was du gewählt hast; ein Telefon ohne Code wird nie ausgesperrt |
| Ein geändertes oder gefälschtes Zertifikat | Der Schlüssel des Installationszertifikats wird beim ersten Mal gemerkt oder mit dem QR von Studio gekoppelt; ändert er sich, wird die Verbindung verweigert und du wirst benachrichtigt |
| Das Passwort im Klartext gesendet | Klartext-HTTP nur für eine Adresse im privaten Netz oder Loopback (`NSAllowsLocalNetworking`); alles andere braucht https, sonst weigert sich die App, das Passwort zu senden |
| Ein Kamerapasswort auf dem Telefon | Die Kameras laufen über den Server: Die App hat kein Kamerapasswort und keine RTSP-Adresse |
| Ein Betrachter ändert etwas | Die Rolle *Betrachter* schaut nur: Jede Schaltfläche, die etwas ändert, ist aus; der Server prüft es erneut |
| Der Assistent schaltet versehentlich scharf oder unscharf | Nur geschriebene Befehle (das Mikrofon der Tastatur diktiert); Scharf- und Unscharfschalten brauchen eine an dich gebundene Bestätigung, hinter der Telefonsperre |

Die Berechtigungstexte (Face ID, lokales Netzwerk) gibt es in allen acht Sprachen. Nichts davon lief auf einem iPhone: Face ID, der Keychain und die Zertifikatsregeln sind nicht auf einem Gerät getestet. Lies [docs/CLIENT_BOUNDARY.md](docs/CLIENT_BOUNDARY.md) und [SECURITY.md](SECURITY.md).""",
      "interfaces": r"""Er ist ein Client: Er ruft 26 Pfade von ARMOR-SERVER auf (`tools/ios_lint.py` zählt sie und prüft, dass auch der Android-Client sie aufruft) und zerlegt den MJPEG-Strom der Kameras mit eigenem Parser (`MjpegParser.swift`).

| Teil | Was sie festlegt |
|---|---|
| Zwei Adressen | Die private im Heim-WLAN und die für unterwegs (ein dynamischer DNS-Name oder das VPN) im Mobilfunk; antwortet eine nicht, wird die andere versucht, und die Meldung sagt, was fehlschlug (`Reach.swift`, `Connector.swift`) |
| Kameras | Ein Raster, in dem nur die sichtbaren Bilder laufen, eine Vollansicht mit Steuerkreuz und Schnappschuss, und ein Strom, der bei Abbruch mit wachsenden Wartezeiten neu angefordert wird |
| Push | Alarme erreichen eine geschlossene App nur per Push (`Push.swift`, Firebase), und nur wenn der Server Push aktiviert hat und die Installation ihre eigene `GoogleService-Info.plist` mitbringt; nicht erprobt |""",
      "configuration": r"""| Name | Wert | Was sie festlegt |
|---|---|---|
| iOS | 16.0+ | Mindestversion, in `project.yml` festgelegt |
| Xcode / Swift | 15+ / 5.9+ | Zum Bauen der App / zum Ausführen der Tests |
| `MARKETING_VERSION`, `CURRENT_PROJECT_VERSION` | 0.0.1, 1 | Die Version der App, aus `project.yml` |
| `GoogleService-Info.plist` | für Push | Die eigene Datei der Installation, nie im Repository |

In der App: die zwei Adressen, *Angemeldet bleiben*, die Telefonsperre und die Sprache (die acht Sprachen oder dem Telefon folgen) unter *Mehr > Sprache*.""",
      "quickstart": r"""**Voraussetzungen:** ein Mac mit Xcode 15+ und iOS 16+ zum Bauen der App; Swift 5.9+ (macOS oder Linux) für die Tests; Python 3.11 für die Prüfungen.

```sh
swift test                  # 146 tests of ArmorCore (macOS or Linux)
python tools/ios_lint.py    # structure, eight languages, contract (any system)
xcodegen generate           # then open ARMOR-IOS-CONTROL.xcodeproj in Xcode (on a Mac)
```

Das Xcode-Projekt wird aus `project.yml` mit XcodeGen erzeugt. Wählen Sie ein Signierteam, fügen Sie das App-Symbol und für Push die `GoogleService-Info.plist` der Installation hinzu (nie im Repository). Siehe die [Client-Grenze](docs/CLIENT_BOUNDARY.md).""",
      "testing": r"""```sh
swift test                  # macOS or Linux
python tools/ios_lint.py    # any system, no Mac needed
python -I tools/armor_ci_validate.py
```

| Testdatei | Tests | Was sie abdeckt |
|---|---|---|
| `ControllerTests.swift` | 15 | Die Anwendungsfälle des Controllers |
| `ClientTests.swift` | 14 | Die Verbindung zum Server und ihre Auswertung |
| `LockTests.swift` | 12 | Die Telefonsperre |
| `ModelsTests.swift` | 12 | Die vom Server gelesenen Modelle |
| `ReachTests.swift` | 11 | Die Wahl zwischen den zwei Adressen |
| `SecurityTests.swift` | 8 | Der Sitzungstresor und das Zertifikatsvertrauen |
| `EndpointTests.swift`, `MjpegTests.swift`, `TranslatorTests.swift` | 7 + 7 + 7 | Die Adressauswertung, das MJPEG-Zerlegen und der Übersetzer |
| `PolicyTests.swift`, `AlarmCodesTests.swift` | 6 + 4 | Die Alarmrichtlinie und die Alarmcodes |

Die 146 Tests laufen mit Daten eines echten Servers. `tools/ios_lint.py` besteht ohne Mac: 31 Swift-Dateien, 241 Sätze in 8 Sprachen, 26 Serverpfade. Kein Test läuft auf einem Gerät.""",
      "build": "Das Xcode-Projekt wird aus `project.yml` mit XcodeGen erzeugt: Wähle ein Signing-Team, füge das App-Symbol zu `App/Resources/Assets.xcassets/AppIcon.appiconset` hinzu und für Push die `GoogleService-Info.plist` der Installation. Es wurde nie in Xcode gebaut.",
      "troubleshooting": r"""| Sie sehen | Weil | Tun Sie |
|---|---|---|
| Die Verbindung wird verweigert und du wirst benachrichtigt | Der Schlüssel des Installationszertifikats hat sich geändert | Koppele erneut mit dem QR von Studio, wenn du es absichtlich geändert hast |
| Keine der beiden Adressen antwortet | Falsche Adresse, kein Netz oder http zu einem Ziel außerhalb des Hauses (abgelehnt: das Passwort wird nicht im Klartext gesendet) | Prüfe beide Adressen; nutze unterwegs https |
| `wrong_pin`, `pin_locked`, `pin_not_set` | Der Server lehnt die Entschärfungs-PIN ab; die App zeigt den Code in deiner Sprache | Gib die PIN erneut ein oder warte das Ende der Sperre ab; lege sie in Studio fest |""",
      "structure": r"""<p align="center">
  <img src="images/repository-structure.svg" alt="Repository-Struktur von ARMOR-IOS-CONTROL" width="100%">
</p>

<details>
<summary>Textversion des Baums</summary>

```text
ARMOR-IOS-CONTROL/
├── Sources/ArmorCore/                   die Regeln der App: ein Swift-Paket
├── App/                                 die SwiftUI-Bildschirme und die Teile, die ein iPhone brauchen
├── Tests/                               146 Tests und Daten eines echten Servers
├── docs/                                die Anleitungen dieses Repositorys
├── tools/                               die gemeinsamen CI-Prüfungen und Projektwerkzeuge
├── .github/                             CI-Workflow sowie Vorlagen für Issues und Pull Requests
├── images/                              Banner, Symbol und die zwei Bilder dieses READMEs
├── armor.project.json                   Manifest: Version, Rolle, Reifegrad, Build-Befehl
├── CHANGELOG.md                         was sich in jeder Version geändert hat
├── SECURITY.md SUPPORT.md LICENSE       Sicherheitsrichtlinie, Support und Lizenz
├── CONTRIBUTING.md CODE_OF_CONDUCT.md   Mitwirkung und Verhaltenskodex
├── Package.swift                        das Swift-Paket: ArmorCore und seine Tests
├── project.yml                          XcodeGen: daraus wird das Xcode-Projekt erzeugt
└── .gitattributes .gitignore            Git-Einstellungen
```

</details>""",
      "roadmap": r"""**Bekannte Grenzen heute**

* Nichts lief auf einem iPhone: Die SwiftUI-Bildschirme wurden nie in Xcode gebaut; Face ID, der Keychain, die Zertifikatsregeln, die Live-Kamera, die Töne der Meldungen, die Stimme und Push über Firebase sind ungetestet.
* Nur die Regeln (`ArmorCore`) sind getestet, und nur unter Linux.
* Die App überwacht nicht im Hintergrund: iOS lässt eine geschlossene App den Server nicht abfragen.

**Als Nächstes**

* Die Bildschirme in Xcode bauen und die App auf einem iPhone gegen den CM5-Prüfstand ausführen.
* Face ID, den Keychain, die Zertifikatsregeln, die Live-Kamera und Push ausprobieren.""",
    },
  },
  "fr": {
    "tagline": "Client opérateur iPhone d'ARMOR-SERVER : état, armement, alarmes, centrales d'alarme, caméras et assistant, en huit langues",
    "honest": "les règles de l'app (liaison au serveur, lecture des réponses, choix de l'adresse, verrou du téléphone, coffre de la session, confiance dans le certificat, politique d'alarmes, cas d'usage, découpage du MJPEG) forment le paquet Swift `ArmorCore`, couvert par 146 tests unitaires qui s'exécutent avec `swift test` sous macOS ou Linux, et `tools/ios_lint.py` vérifie la structure, les huit tables de langues et le contrat sans Mac. Ce qui n'est **pas** encore prouvé : les écrans SwiftUI et les parties qui exigent un iPhone (Face ID, trousseau, règles de certificat, caméra en direct, push via Firebase) n'ont pas été compilés dans Xcode ni exécutés sur un appareil.",
    "glance": [
      [
        "Rôle",
        "Client opérateur iPhone pour ARMOR-SERVER (famille : Clients, parent : ARMOR-SERVER)",
      ],
      [
        "Technologie",
        "Swift 5.9+ / SwiftUI, iOS 16+",
      ],
      [
        "Tests",
        "146 (`swift test`)",
      ],
      [
        "Langues",
        "8 (241 phrases par langue, vérifiées par `ios_lint.py`)",
      ],
      [
        "Fonctionne sur",
        "Un iPhone avec iOS 16+ ; les tests tournent sous macOS ou Linux",
      ],
      [
        "Sur matériel réel",
        "Pas encore exécuté sur un iPhone ; les règles sont testées sous Linux",
      ],
      [
        "Licence",
        "GPL-3.0-or-later",
      ],
    ],
    "status": {
      "software": "Les règles de l'application forment un paquet Swift (`ArmorCore`) ; les écrans SwiftUI n'ont pas été compilés dans Xcode.",
      "tests": "146 tests unitaires réussissent avec `swift test` sous macOS ou Linux, et `tools/ios_lint.py` vérifie la structure, les tables des huit langues et le contrat sans Mac ; aucun test ne tourne sur un appareil.",
      "ui": "Les écrans SwiftUI sont écrits mais n'ont été ni compilés dans Xcode ni exécutés sur un iPhone.",
      "hardware": "Elle n'a pas tourné sur un iPhone : les règles ne sont testées que sous Linux.",
      "security": "Le verrouillage du téléphone, le coffre de la session et la confiance dans le certificat sont des règles testées sous Linux ; Face ID, le trousseau et les règles du certificat n'ont pas tourné sur un appareil.",
      "integration": "La caméra en direct et le push via Firebase n'ont pas été essayés ; la liaison au serveur et l'analyse sont testées contre le contrat partagé.",
      "docs": "Huit langues et le journal des modifications sont à jour.",
    },
    "docs": [
      "[Limites du client](docs/CLIENT_BOUNDARY.md) : ce que le client fait et ne fait jamais, et comment le compiler",
    ],
    "contributing_first": "Avant une pull request, lancez `swift test` and `python tools/ios_lint.py` and `python -I tools/armor_ci_validate.py` : il doit réussir. Voir [CONTRIBUTING.md](CONTRIBUTING.md) et le [code de conduite](CODE_OF_CONDUCT.md).",
    "languages_extra": "",
    "body": {
      "overview": r"""* **Connexion avec l'identifiant du serveur lui-même :** les adresses de la maison (à la maison et à l'extérieur), utilisateur et mot de passe ; le mot de passe crée une session HttpOnly ; il n'est conservé que si vous cochez **Se souvenir de moi** (dans le trousseau de ce téléphone, jamais sauvegardé). Le rôle **viewer** regarde seulement : tout bouton qui modifie quelque chose est désactivé.
* **Deux adresses :** la privée sur le Wi-Fi de la maison, celle de l'extérieur (un nom DNS dynamique ou le VPN) avec les données mobiles ; si l'une ne répond pas, l'autre est essayée et le message dit ce qui échoue.
* **Verrou du téléphone :** Face ID, Touch ID ou le code avant d'armer, de désarmer, de couper une sirène, de déverrouiller et les autres ordres critiques (activé par défaut seulement avec Face ID ou Touch ID) et, si vous l'activez, pour ouvrir l'app. Votre administrateur peut l'exiger, jamais baisser ce que vous avez choisi ; un téléphone sans code n'est jamais bloqué et l'écran verrouillé propose toujours de se connecter avec le mot de passe. En option (désactivé, avec avertissement), la session enregistrée n'est lisible que téléphone déverrouillé.
* **Armer et désarmer** après vérification de ce qui resterait aveugle ou bruyant, avec le PIN pour désarmer ; **alarmes** à acquitter, avec compteur ; les **centrales d'alarme** (armer absent ou présent, désarmer, couper la sirène) et l'**historique** ; **appareils** avec Marche / Arrêt et confirmation pour les circuits et les appareils critiques.
* **Caméras** via le serveur (l'app n'a jamais le mot de passe de la caméra) : une grille où seules les images à l'écran tournent, une vue complète avec une croix pour déplacer la caméra et une photo, et un flux redemandé avec des attentes croissantes s'il se coupe.
* **Des avis à votre mesure :** tout mettre en sourdine ou l'afficher sans son ; désactiver des gravités et des types (une alarme critique n'est jamais masquée, sauf par l'interrupteur qui coupe tout) ; un fichier de son à vous pour chaque gravité et chaque type, avec un bouton de lecture ; et la voix qui dit les alarmes (femme, homme, âge, style, vitesse, avis de faible gravité), avec un bouton d'essai. Une caméra à deux objectifs dans une même image apparaît comme deux fenêtres.
* **L'assistant :** commandes écrites (le micro du clavier dicte), avec une confirmation liée à vous pour armer et désarmer, derrière le verrou.
* **Confiance dans le certificat :** la clé du certificat de l'installation est retenue la première fois ou appairée avec le QR de Studio ; si elle change, la connexion est refusée et vous êtes prévenu.
* **Huit langues** (anglais, espagnol, allemand, français, italien, japonais, chinois et portugais du Portugal), choisies dans *Plus > Langue* ou suivant le téléphone, avec une aide pour chaque écran.""",
      "role": r"""ARMOR-IOS-CONTROL est la fenêtre de l'iPhone sur le même [ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER) que celui d'[ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) et d'[ARMOR-ANDROID-CONTROL](https://github.com/JuanenRac/ARMOR-ANDROID-CONTROL) : il lit et ordonne par lui et rien d'autre, et parle le même contrat que l'app Android.

| Nom | Comment | À quoi ça sert |
|---|---|---|
| ARMOR-SERVER | HTTP `/api/v1`, MJPEG | Tout ce que l'app lit et commande ; elle ne parle à rien d'autre |
| ARMOR-ANDROID-CONTROL | même contrat | `ios_lint.py` vérifie que l'app n'appelle que des chemins appelés par le client Android |
| ARMOR-STUDIO | QR | Apparie la clé du certificat de l'installation |""",
      "architecture": r"""<p align="center">
  <img src="images/architecture.svg" alt="Architecture de ARMOR-IOS-CONTROL : qui l'appelle, ce qu'il contient et de quoi il dépend" width="100%">
</p>""",
      "security": r"""| Menace | Défense |
|---|---|
| Le mot de passe sur le téléphone | Conservé seulement avec *Se souvenir de moi*, dans le Keychain de ce téléphone et jamais sauvegardé ; la session est un cookie HttpOnly du serveur |
| Un ordre critique avec le téléphone en d'autres mains | Face ID, Touch ID ou le code avant d'armer, désarmer, couper une sirène, déverrouiller et les autres ordres critiques ; l'administrateur peut l'exiger, jamais abaisser votre choix ; un téléphone sans code n'est jamais exclu |
| Un certificat changé ou falsifié | La clé du certificat de l'installation est mémorisée la première fois ou appariée avec le QR de Studio ; si elle change, la connexion est refusée et vous êtes prévenu |
| Le mot de passe envoyé en clair | HTTP en clair seulement pour une adresse de réseau privé ou loopback (`NSAllowsLocalNetworking`) ; tout le reste exige https, sinon l'app refuse d'envoyer le mot de passe |
| Un mot de passe de caméra sur le téléphone | Les caméras passent par le serveur : l'app n'a ni mot de passe de caméra ni adresse RTSP |
| Un lecteur change quelque chose | Le rôle *lecteur* ne fait que regarder : tout bouton qui change quelque chose est désactivé ; le serveur revérifie |
| L'assistant arme ou désarme par erreur | Seulement des ordres écrits (le micro du clavier dicte) ; armer et désarmer exigent une confirmation liée à vous, derrière le verrouillage du téléphone |

Les textes d'autorisation (Face ID, réseau local) existent dans les huit langues. Rien de tout cela n'a tourné sur un iPhone : Face ID, le Keychain et les règles de certificat ne sont pas testés sur un appareil. Lisez [docs/CLIENT_BOUNDARY.md](docs/CLIENT_BOUNDARY.md) et [SECURITY.md](SECURITY.md).""",
      "interfaces": r"""C'est un client : il appelle 26 chemins d'ARMOR-SERVER (`tools/ios_lint.py` les compte et vérifie que le client Android les appelle aussi) et découpe le flux MJPEG des caméras avec son propre analyseur (`MjpegParser.swift`).

| Partie | Ce qu'elle règle |
|---|---|
| Deux adresses | La privée sur le Wi-Fi de la maison et celle pour l'extérieur (un nom DNS dynamique ou le VPN) en données mobiles ; si l'une ne répond pas, l'autre est essayée et le message dit ce qui a échoué (`Reach.swift`, `Connector.swift`) |
| Caméras | Une grille où seules les images à l'écran tournent, une vue complète avec une croix pour bouger la caméra et un instantané, et un flux redemandé avec des attentes croissantes en cas de coupure |
| Push | Les alarmes n'atteignent une app fermée que par push (`Push.swift`, Firebase), et seulement si le serveur a le push activé et que l'installation apporte son propre `GoogleService-Info.plist` ; non essayé |""",
      "configuration": r"""| Nom | Valeur | Ce qu'elle règle |
|---|---|---|
| iOS | 16.0+ | Version minimale, définie dans `project.yml` |
| Xcode / Swift | 15+ / 5.9+ | Pour compiler l'app / pour lancer les tests |
| `MARKETING_VERSION`, `CURRENT_PROJECT_VERSION` | 0.0.1, 1 | La version de l'app, de `project.yml` |
| `GoogleService-Info.plist` | pour le push | Le fichier propre à l'installation, jamais gardé dans le dépôt |

Dans l'app : les deux adresses, *Se souvenir de moi*, le verrouillage du téléphone et la langue (les huit langues ou suivre le téléphone) dans *Plus > Langue*.""",
      "quickstart": r"""**Prérequis:** un Mac avec Xcode 15+ et iOS 16+ pour compiler l'app ; Swift 5.9+ (macOS ou Linux) pour les tests ; Python 3.11 pour les contrôles.

```sh
swift test                  # 146 tests of ArmorCore (macOS or Linux)
python tools/ios_lint.py    # structure, eight languages, contract (any system)
xcodegen generate           # then open ARMOR-IOS-CONTROL.xcodeproj in Xcode (on a Mac)
```

Le projet Xcode est généré depuis `project.yml` avec XcodeGen. Choisissez une équipe de signature, ajoutez l'icône de l'app et, pour le push, le `GoogleService-Info.plist` de l'installation (jamais conservé dans le dépôt). Voir la [frontière du client](docs/CLIENT_BOUNDARY.md).""",
      "testing": r"""```sh
swift test                  # macOS or Linux
python tools/ios_lint.py    # any system, no Mac needed
python -I tools/armor_ci_validate.py
```

| Fichier de tests | Tests | Ce qu'il couvre |
|---|---|---|
| `ControllerTests.swift` | 15 | Les cas d'usage du contrôleur |
| `ClientTests.swift` | 14 | Le lien avec le serveur et son analyse |
| `LockTests.swift` | 12 | Le verrouillage du téléphone |
| `ModelsTests.swift` | 12 | Les modèles lus depuis le serveur |
| `ReachTests.swift` | 11 | Le choix entre les deux adresses |
| `SecurityTests.swift` | 8 | Le coffre de session et la confiance dans le certificat |
| `EndpointTests.swift`, `MjpegTests.swift`, `TranslatorTests.swift` | 7 + 7 + 7 | L'analyse d'adresses, le découpage MJPEG et le traducteur |
| `PolicyTests.swift`, `AlarmCodesTests.swift` | 6 + 4 | La politique d'alarme et les codes d'alarme |

Les 146 tests utilisent des données d'un vrai serveur. `tools/ios_lint.py` réussit sans Mac : 31 fichiers Swift, 241 phrases en 8 langues, 26 chemins du serveur. Aucun test ne tourne sur un appareil.""",
      "build": "Le projet Xcode est généré depuis `project.yml` avec XcodeGen : choisissez une équipe de signature, ajoutez l'icône de l'app à `App/Resources/Assets.xcassets/AppIcon.appiconset` et, pour le push, le `GoogleService-Info.plist` de l'installation. Il n'a jamais été compilé dans Xcode.",
      "troubleshooting": r"""| Vous voyez | Parce que | Faites |
|---|---|---|
| La connexion est refusée et vous êtes prévenu | La clé du certificat de l'installation a changé | Appariez de nouveau avec le QR de Studio si vous l'avez changé exprès |
| Aucune des deux adresses ne répond | Mauvaise adresse, pas de réseau, ou http vers un lieu hors de la maison (refusé : le mot de passe n'est pas envoyé en clair) | Vérifiez les deux adresses ; utilisez https hors de la maison |
| `wrong_pin`, `pin_locked`, `pin_not_set` | Le serveur refuse le PIN de désarmement ; l'app affiche le code dans votre langue | Saisissez de nouveau le PIN ou attendez la fin du blocage ; définissez-le dans Studio |""",
      "structure": r"""<p align="center">
  <img src="images/repository-structure.svg" alt="Structure du dépôt de ARMOR-IOS-CONTROL" width="100%">
</p>

<details>
<summary>Version texte de l'arborescence</summary>

```text
ARMOR-IOS-CONTROL/
├── Sources/ArmorCore/                   les règles de l'app : un paquet Swift
├── App/                                 les écrans SwiftUI et les parties qui exigent un iPhone
├── Tests/                               146 tests et données d'un vrai serveur
├── docs/                                les guides de ce dépôt
├── tools/                               les contrôles CI partagés et les outils du projet
├── .github/                             workflow CI et modèles d'issues et de pull requests
├── images/                              bannière, icône et les deux images de ce README
├── armor.project.json                   manifeste : version, rôle, maturité, commande de build
├── CHANGELOG.md                         ce qui a changé à chaque version
├── SECURITY.md SUPPORT.md LICENSE       politique de sécurité, support et licence
├── CONTRIBUTING.md CODE_OF_CONDUCT.md   comment contribuer et le code de conduite
├── Package.swift                        le paquet Swift : ArmorCore et ses tests
├── project.yml                          XcodeGen : le projet Xcode en est généré
└── .gitattributes .gitignore            réglages Git
```

</details>""",
      "roadmap": r"""**Limites connues aujourd'hui**

* Rien n'a tourné sur un iPhone : les écrans SwiftUI n'ont pas été compilés dans Xcode ; Face ID, le Keychain, les règles de certificat, la caméra en direct, les sons des avis, la voix et le push via Firebase ne sont pas testés.
* Seules les règles (`ArmorCore`) sont testées, et seulement sous Linux.
* L'app ne surveille pas en arrière-plan : iOS ne laisse pas une app fermée interroger le serveur.

**Ensuite**

* Compiler les écrans dans Xcode et lancer l'app sur un iPhone contre le banc d'essai CM5.
* Essayer Face ID, le Keychain, les règles de certificat, la caméra en direct et le push.""",
    },
  },
  "it": {
    "tagline": "Client operatore per iPhone di ARMOR-SERVER: stato, armamento, allarmi, centrali di allarme, telecamere e assistente, in otto lingue",
    "honest": "le regole dell'app (collegamento al server, lettura delle risposte, scelta dell'indirizzo, blocco del telefono, cassaforte della sessione, fiducia nel certificato, politica degli allarmi, casi d'uso, taglio dell'MJPEG) sono il pacchetto Swift `ArmorCore`, coperto da 146 test unitari che girano con `swift test` su macOS o Linux, e `tools/ios_lint.py` controlla la struttura, le otto tabelle delle lingue e il contratto senza Mac. Ciò che **non** è ancora provato: le schermate SwiftUI e le parti che richiedono un iPhone (Face ID, portachiavi, regole del certificato, telecamera dal vivo, push con Firebase) non sono state compilate in Xcode né eseguite su un dispositivo.",
    "glance": [
      [
        "Ruolo",
        "Client operatore per iPhone di ARMOR-SERVER (famiglia: Clients, padre: ARMOR-SERVER)",
      ],
      [
        "Tecnologia",
        "Swift 5.9+ / SwiftUI, iOS 16+",
      ],
      [
        "Test",
        "146 (`swift test`)",
      ],
      [
        "Lingue",
        "8 (241 frasi per lingua, verificate da `ios_lint.py`)",
      ],
      [
        "Gira su",
        "Un iPhone con iOS 16+; i test girano su macOS o Linux",
      ],
      [
        "Su hardware reale",
        "Non ancora eseguito su un iPhone; le regole sono testate su Linux",
      ],
      [
        "Licenza",
        "GPL-3.0-or-later",
      ],
    ],
    "status": {
      "software": "Le regole dell'app sono un pacchetto Swift (`ArmorCore`); le schermate SwiftUI non sono state compilate in Xcode.",
      "tests": "Superano 146 test unitari con `swift test` su macOS o Linux, e `tools/ios_lint.py` controlla la struttura, le tabelle delle otto lingue e il contratto senza un Mac; nessun test gira su un dispositivo.",
      "ui": "Le schermate SwiftUI sono scritte ma non sono state compilate in Xcode né eseguite su un iPhone.",
      "hardware": "Non ha girato su un iPhone: le regole sono provate solo su Linux.",
      "security": "Il blocco del telefono, il deposito della sessione e la fiducia nel certificato sono regole provate su Linux; Face ID, il portachiavi e le regole del certificato non sono stati eseguiti su un dispositivo.",
      "integration": "La telecamera dal vivo e il push tramite Firebase non sono stati provati; il collegamento al server e il parsing sono provati contro il contratto condiviso.",
      "docs": "Otto lingue e il registro delle modifiche sono aggiornati.",
    },
    "docs": [
      "[Confini del client](docs/CLIENT_BOUNDARY.md): cosa fa e non fa mai il client, e come compilarlo",
    ],
    "contributing_first": "Prima di una pull request esegui `swift test` and `python tools/ios_lint.py` and `python -I tools/armor_ci_validate.py`: deve passare. Vedi [CONTRIBUTING.md](CONTRIBUTING.md) e il [codice di condotta](CODE_OF_CONDUCT.md).",
    "languages_extra": "",
    "body": {
      "overview": r"""* **Accedi con il login del server stesso:** gli indirizzi di casa (in casa e fuori), utente e password; la password crea una sessione HttpOnly; viene conservata solo se spunti **Ricordami** (nel portachiavi di questo telefono, mai nel backup). Il ruolo **viewer** guarda soltanto: ogni pulsante che cambia qualcosa è spento.
* **Due indirizzi:** quello privato sul Wi-Fi di casa, quello per fuori (un nome DNS dinamico o la VPN) con i dati mobili; se uno non risponde si prova l'altro e il messaggio dice cosa non va.
* **Blocco con il telefono:** Face ID, Touch ID o il codice prima di armare, disarmare, silenziare una sirena, sbloccare e gli altri ordini critici (attivo di default solo con Face ID o Touch ID) e, se lo attivi, per aprire l'app. Il tuo amministratore può imporlo, mai abbassare ciò che hai scelto; un telefono senza codice non resta mai fuori e la schermata di blocco offre sempre di accedere con la password. Facoltativamente (disattivato, con avviso) la sessione salvata è leggibile solo con il telefono sbloccato.
* **Armare e disarmare** dopo il controllo di ciò che resterebbe cieco o rumoroso, con il PIN per disarmare; **allarmi** da confermare, con contatore; le **centrali di allarme** (armare fuori o in casa, disarmare, silenziare la sirena) e lo **storico**; **dispositivi** con Acceso / Spento e conferma per circuiti e critici.
* **Telecamere** tramite il server (l'app non ha mai la password della telecamera): una griglia in cui girano solo le immagini visibili, una vista completa con croce direzionale per muovere la telecamera e foto, e un flusso richiesto di nuovo con attese crescenti se si interrompe.
* **Avvisi a tua scelta:** silenziare tutto o mostrarlo senza suono; disattivare gravità e tipi (un allarme critico non viene mai nascosto, salvo con l'interruttore che silenzia tutto); un file audio tuo per ogni gravità e ogni tipo, con pulsante di riproduzione; e la voce che dice gli allarmi (donna, uomo, età, stile, velocità, avvisi di bassa gravità), con pulsante di prova. Una telecamera con due obiettivi in un'unica immagine appare come due finestre.
* **L'assistente:** comandi scritti (il microfono della tastiera detta), con una conferma legata a te per armare e disarmare, dietro il blocco.
* **Fiducia nel certificato:** la chiave del certificato dell'installazione viene ricordata la prima volta o associata con il QR di Studio; se cambia, la connessione viene rifiutata e ti viene detto.
* **Otto lingue** (inglese, spagnolo, tedesco, francese, italiano, giapponese, cinese e portoghese del Portogallo), scelte in *Altro > Lingua* o seguendo il telefono, con un aiuto per ogni schermata.""",
      "role": r"""ARMOR-IOS-CONTROL è la finestra dell'iPhone sullo stesso [ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER) che usano [ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) e [ARMOR-ANDROID-CONTROL](https://github.com/JuanenRac/ARMOR-ANDROID-CONTROL): legge e ordina attraverso di esso e nient'altro, e parla lo stesso contratto dell'app Android.

| Nome | Come | A cosa serve |
|---|---|---|
| ARMOR-SERVER | HTTP `/api/v1`, MJPEG | Tutto ciò che l'app legge e ordina; non parla con nient'altro |
| ARMOR-ANDROID-CONTROL | stesso contratto | `ios_lint.py` verifica che l'app chiami solo percorsi chiamati dal client Android |
| ARMOR-STUDIO | QR | Associa la chiave del certificato dell'installazione |""",
      "architecture": r"""<p align="center">
  <img src="images/architecture.svg" alt="Architettura di ARMOR-IOS-CONTROL: chi lo chiama, cosa contiene e da cosa dipende" width="100%">
</p>""",
      "security": r"""| Minaccia | Difesa |
|---|---|
| La password sul telefono | Salvata solo con *Ricordami*, nel Keychain di questo telefono e mai nei backup; la sessione è un cookie HttpOnly del server |
| Un ordine critico con il telefono in altre mani | Face ID, Touch ID o il codice prima di inserire, disinserire, silenziare una sirena, sbloccare e gli altri ordini critici; l'amministratore può imporlo, mai abbassare la tua scelta; un telefono senza codice non resta mai escluso |
| Un certificato cambiato o falsificato | La chiave del certificato dell'installazione viene ricordata la prima volta o associata con il QR di Studio; se cambia, la connessione è rifiutata e ne sei avvisato |
| La password inviata in chiaro | HTTP in chiaro solo per un indirizzo di rete privata o loopback (`NSAllowsLocalNetworking`); tutto il resto richiede https, altrimenti l'app rifiuta di inviare la password |
| Una password di telecamera sul telefono | Le telecamere passano dal server: l'app non ha password di telecamera né indirizzo RTSP |
| Un visualizzatore cambia qualcosa | Il ruolo *visualizzatore* guarda soltanto: ogni pulsante che cambia qualcosa è spento; il server lo ricontrolla |
| L'assistente inserisce o disinserisce per errore | Solo comandi scritti (il microfono della tastiera detta); inserire e disinserire richiedono una conferma legata a te, dietro il blocco del telefono |

I testi dei permessi (Face ID, rete locale) esistono in tutte e otto le lingue. Nulla di tutto ciò è girato su un iPhone: Face ID, il Keychain e le regole del certificato non sono testati su un dispositivo. Leggi [docs/CLIENT_BOUNDARY.md](docs/CLIENT_BOUNDARY.md) e [SECURITY.md](SECURITY.md).""",
      "interfaces": r"""È un client: chiama 26 percorsi di ARMOR-SERVER (`tools/ios_lint.py` li conta e verifica che li chiami anche il client Android) e taglia il flusso MJPEG delle telecamere con un parser proprio (`MjpegParser.swift`).

| Parte | Cosa imposta |
|---|---|
| Due indirizzi | Quella privata sul Wi-Fi di casa e quella per fuori (un nome DNS dinamico o la VPN) con i dati mobili; se una non risponde si prova l'altra e il messaggio dice cosa è fallito (`Reach.swift`, `Connector.swift`) |
| Telecamere | Una griglia dove girano solo le immagini a schermo, una vista completa con un pad per muovere la telecamera e un'istantanea, e un flusso richiesto di nuovo con attese crescenti se cade |
| Push | Gli allarmi raggiungono un'app chiusa solo via push (`Push.swift`, Firebase), e solo se il server ha il push attivo e l'installazione porta il proprio `GoogleService-Info.plist`; non provato |""",
      "configuration": r"""| Nome | Valore | Cosa imposta |
|---|---|---|
| iOS | 16.0+ | Versione minima, definita in `project.yml` |
| Xcode / Swift | 15+ / 5.9+ | Per compilare l'app / per eseguire i test |
| `MARKETING_VERSION`, `CURRENT_PROJECT_VERSION` | 0.0.1, 1 | La versione dell'app, da `project.yml` |
| `GoogleService-Info.plist` | per il push | Il file proprio dell'installazione, mai conservato nel repository |

Nell'app: i due indirizzi, *Ricordami*, il blocco del telefono e la lingua (le otto lingue o seguire il telefono) in *Altro > Lingua*.""",
      "quickstart": r"""**Requisiti:** un Mac con Xcode 15+ e iOS 16+ per compilare l'app; Swift 5.9+ (macOS o Linux) per i test; Python 3.11 per le verifiche.

```sh
swift test                  # 146 tests of ArmorCore (macOS or Linux)
python tools/ios_lint.py    # structure, eight languages, contract (any system)
xcodegen generate           # then open ARMOR-IOS-CONTROL.xcodeproj in Xcode (on a Mac)
```

Il progetto Xcode si genera da `project.yml` con XcodeGen. Scegli un team di firma, aggiungi l'icona dell'app e, per il push, il `GoogleService-Info.plist` dell'installazione (mai conservato nel repository). Vedi il [confine del client](docs/CLIENT_BOUNDARY.md).""",
      "testing": r"""```sh
swift test                  # macOS or Linux
python tools/ios_lint.py    # any system, no Mac needed
python -I tools/armor_ci_validate.py
```

| File di test | Test | Cosa copre |
|---|---|---|
| `ControllerTests.swift` | 15 | I casi d'uso del controller |
| `ClientTests.swift` | 14 | Il collegamento al server e la sua interpretazione |
| `LockTests.swift` | 12 | Il blocco del telefono |
| `ModelsTests.swift` | 12 | I modelli letti dal server |
| `ReachTests.swift` | 11 | La scelta tra i due indirizzi |
| `SecurityTests.swift` | 8 | Il deposito della sessione e la fiducia nel certificato |
| `EndpointTests.swift`, `MjpegTests.swift`, `TranslatorTests.swift` | 7 + 7 + 7 | La lettura degli indirizzi, il taglio MJPEG e il traduttore |
| `PolicyTests.swift`, `AlarmCodesTests.swift` | 6 + 4 | La politica degli allarmi e i codici di allarme |

I 146 test usano dati di un server reale. `tools/ios_lint.py` passa senza Mac: 31 file Swift, 241 frasi in 8 lingue, 26 percorsi del server. Nessun test gira su un dispositivo.""",
      "build": "Il progetto Xcode si genera da `project.yml` con XcodeGen: scegli un team di firma, aggiungi l'icona dell'app a `App/Resources/Assets.xcassets/AppIcon.appiconset` e, per il push, il `GoogleService-Info.plist` dell'installazione. Non è mai stato compilato in Xcode.",
      "troubleshooting": r"""| Vedi | Perché | Fai |
|---|---|---|
| La connessione è rifiutata e ne sei avvisato | La chiave del certificato dell'installazione è cambiata | Associa di nuovo con il QR di Studio se l'hai cambiato di proposito |
| Nessuno dei due indirizzi risponde | Indirizzo errato, nessuna rete, o http verso un luogo fuori casa (rifiutato: la password non si invia in chiaro) | Controlla i due indirizzi; usa https fuori casa |
| `wrong_pin`, `pin_locked`, `pin_not_set` | Il server rifiuta il PIN di disinserimento; l'app mostra il codice nella tua lingua | Digita di nuovo il PIN o attendi la fine del blocco; impostalo in Studio |""",
      "structure": r"""<p align="center">
  <img src="images/repository-structure.svg" alt="Struttura del repository di ARMOR-IOS-CONTROL" width="100%">
</p>

<details>
<summary>Versione testuale dell'albero</summary>

```text
ARMOR-IOS-CONTROL/
├── Sources/ArmorCore/                   le regole dell'app: un pacchetto Swift
├── App/                                 le schermate SwiftUI e le parti che richiedono un iPhone
├── Tests/                               146 test e dati di un server reale
├── docs/                                le guide di questo repository
├── tools/                               i controlli CI condivisi e gli strumenti del progetto
├── .github/                             workflow CI e modelli per issue e pull request
├── images/                              banner, icona e le due immagini di questo README
├── armor.project.json                   manifesto: versione, ruolo, maturità, comando di build
├── CHANGELOG.md                         cosa è cambiato in ogni versione
├── SECURITY.md SUPPORT.md LICENSE       politica di sicurezza, supporto e licenza
├── CONTRIBUTING.md CODE_OF_CONDUCT.md   come contribuire e il codice di condotta
├── Package.swift                        il pacchetto Swift: ArmorCore e i suoi test
├── project.yml                          XcodeGen: da qui si genera il progetto Xcode
└── .gitattributes .gitignore            impostazioni di Git
```

</details>""",
      "roadmap": r"""**Limiti noti oggi**

* Nulla è girato su un iPhone: le schermate SwiftUI non sono state compilate in Xcode; Face ID, il Keychain, le regole del certificato, la telecamera dal vivo, i suoni degli avvisi, la voce e il push via Firebase non sono testati.
* Solo le regole (`ArmorCore`) sono testate, e solo su Linux.
* L'app non sorveglia in background: iOS non lascia che un'app chiusa interroghi il server.

**Prossimi passi**

* Compilare le schermate in Xcode e far girare l'app su un iPhone contro il banco di prova CM5.
* Provare Face ID, il Keychain, le regole del certificato, la telecamera dal vivo e il push.""",
    },
  },
  "ja": {
    "tagline": "ARMOR-SERVER の iPhone オペレータークライアント：状態、警戒、警報、警報盤、カメラ、アシスタント。8 言語対応",
    "honest": "アプリのルール（サーバー接続、応答の解析、アドレスの選択、端末ロック、セッションの保管庫、証明書の信頼、警報ポリシー、ユースケース、MJPEG の切り出し）は Swift パッケージ `ArmorCore` にあり、macOS または Linux で `swift test` により実行される 146 件の単体テストでカバーされています。`tools/ios_lint.py` は Mac なしで構造、8 言語の表、契約を検査します。**まだ**証明されていないもの：SwiftUI の画面と iPhone が必要な部分（Face ID、キーチェーン、証明書ルール、ライブカメラ、Firebase 経由のプッシュ）は、Xcode でのビルドも実機での実行もしていません。",
    "glance": [
      [
        "役割",
        "ARMOR-SERVER 用の iPhone オペレーター向けクライアント（ファミリー：Clients、親：ARMOR-SERVER）",
      ],
      [
        "技術",
        "Swift 5.9+ / SwiftUI, iOS 16+",
      ],
      [
        "テスト",
        "146 (`swift test`)",
      ],
      [
        "言語",
        "8（言語ごとに 241 フレーズ、`ios_lint.py` が検査）",
      ],
      [
        "動作環境",
        "iOS 16+ の iPhone。テストは macOS または Linux で実行",
      ],
      [
        "実機での確認",
        "iPhone ではまだ実行していません。ルールは Linux でテスト済みです",
      ],
      [
        "ライセンス",
        "GPL-3.0-or-later",
      ],
    ],
    "status": {
      "software": "アプリの規則は Swift パッケージ（`ArmorCore`）です。SwiftUI の画面は Xcode ではまだビルドしていません。",
      "tests": "146 件のユニットテストが macOS または Linux の `swift test` で通り、`tools/ios_lint.py` が Mac なしで構造、8 言語の表、契約を確認します。実機で動くテストはありません。",
      "ui": "SwiftUI の画面は書いてありますが、Xcode でのビルドも iPhone での実行もしていません。",
      "hardware": "iPhone 上ではまだ動かしていません。規則は Linux でのみテストしています。",
      "security": "端末のロック、セッションの保管庫、証明書の信頼は Linux でテストした規則です。Face ID、キーチェーン、証明書の規則は実機では動かしていません。",
      "integration": "ライブカメラと Firebase 経由のプッシュは試していません。サーバーとの接続と解析は共有の契約に対してテストしています。",
      "docs": "8 言語と変更履歴は最新です。",
    },
    "docs": [
      "[クライアントの境界](docs/CLIENT_BOUNDARY.md)：クライアントがすることとしないこと、ビルド方法",
    ],
    "contributing_first": "Pull Request の前に `swift test` and `python tools/ios_lint.py` and `python -I tools/armor_ci_validate.py` を実行してください。通る必要があります。[CONTRIBUTING.md](CONTRIBUTING.md) と[行動規範](CODE_OF_CONDUCT.md)を参照してください。",
    "languages_extra": "",
    "body": {
      "overview": r"""* **サーバー自身のログインでサインイン：** 家のアドレス（自宅と外出先）、ユーザー名、パスワード。パスワードは HttpOnly セッションを作り、**記憶**にチェックした場合のみ保存されます（この iPhone のキーチェーン内、バックアップなし）。**viewer** ロールは閲覧のみで、変更するボタンはすべて無効です。
* **2 つのアドレス：** 自宅の Wi-Fi ではプライベートなアドレス、モバイルデータでは外出先用（ダイナミック DNS 名または VPN）。一方が応答しなければもう一方を試し、何が失敗したかを表示します。
* **端末ロック：** 警戒、解除、サイレンの消音、解錠などの重要な操作の前に Face ID、Touch ID またはパスコードを要求します（既定では Face ID / Touch ID がある場合のみオン）。オンにするとアプリを開くときにも要求します。管理者は必須にできますが、あなたの選択を下げることはできません。パスコードのない iPhone が締め出されることはなく、ロック画面には常にパスワードでのサインインがあります。任意（既定でオフ、警告付き）：保存したセッションは iPhone のロック解除中のみ読めます。
* **警戒と解除**：死角やノイズになる箇所を確認した上で行い、解除には PIN が必要です。確認すべき**警報**（バッジ付き）、**警報盤**（外出警戒・在宅警戒、解除、サイレン消音）と**履歴**、オン / オフできる**デバイス**（回路と重要機器は確認付き）。
* **カメラ**はサーバー経由（アプリがカメラのパスワードを持つことはありません）：画面に見えている映像だけが動くグリッド、カメラを動かす十字キーと写真付きのフルビュー、途切れたときに待ち時間を延ばしながら再取得するストリーム。
* **通知を自分で選べます：** すべてを消音するか、音なしで表示します。重大度や種類ごとにオフにできます（重大なアラームは、すべてを消音するスイッチを除き、隠されません）。重大度ごと・種類ごとに自分の音声ファイルを選べ、再生ボタンで聞けます。アラームを読み上げる声（女性、男性、年齢、スタイル、速度、重大度の低い通知）も選べ、試し再生ボタンがあります。1枚の映像に2つのレンズがあるカメラは2つのウィンドウで表示されます。
* **アシスタント：** 文字コマンド（キーボードのマイクで音声入力可）。警戒と解除にはご本人に結び付いた確認が必要で、ロックの内側にあります。
* **証明書の信頼：** インストールの証明書の鍵を初回に記憶するか、Studio の QR コードでペアリングします。変更されると接続を拒否して通知します。
* **8 言語**（英語、スペイン語、ドイツ語、フランス語、イタリア語、日本語、中国語、ポルトガル（ポルトガル）語）を*その他 > 言語*で選択、または iPhone に従い、各画面にヘルプがあります。""",
      "role": r"""ARMOR-IOS-CONTROL は、[ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) と [ARMOR-ANDROID-CONTROL](https://github.com/JuanenRac/ARMOR-ANDROID-CONTROL) が使うのと同じ [ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER) への iPhone の窓口です。読み取りも命令もサーバー経由のみで、Android アプリと同じ契約を使います。

| 名前 | 方法 | 用途 |
|---|---|---|
| ARMOR-SERVER | HTTP `/api/v1`, MJPEG | アプリが読み取り・命令するすべて。他とは通信しません |
| ARMOR-ANDROID-CONTROL | 同じコントラクト | `ios_lint.py` が、アプリが Android クライアントも呼ぶパスだけを呼ぶことを検査 |
| ARMOR-STUDIO | QR | 設置環境の証明書の鍵をペアリング |""",
      "architecture": r"""<p align="center">
  <img src="images/architecture.svg" alt="ARMOR-IOS-CONTROL のアーキテクチャ：呼び出し元、内部、依存先" width="100%">
</p>""",
      "security": r"""| 脅威 | 対策 |
|---|---|
| 電話上のパスワード | *ログイン状態を保持* のときだけこの電話のキーチェーンに保存し、バックアップされません。セッションはサーバーの HttpOnly Cookie です |
| 電話が他人の手にあるときの重要な命令 | アーム、ディスアーム、サイレン停止、解錠などの重要な命令の前に Face ID、Touch ID またはパスコードを要求します。管理者は必須にできますが、選んだ水準を下げることはできません。パスコードのない電話が締め出されることはありません |
| 変更または偽造された証明書 | 設置環境の証明書の鍵は初回に記憶するか Studio の QR でペアリングします。変わると接続を拒否して知らせます |
| 平文で送られるパスワード | 平文 HTTP はプライベートネットワークまたはループバックのアドレスのみ（`NSAllowsLocalNetworking`）。それ以外は https が必要で、そうでなければアプリはパスワードを送りません |
| 電話上のカメラのパスワード | カメラはサーバー経由で、アプリにはカメラのパスワードも RTSP アドレスもありません |
| 閲覧者が何かを変更する | *閲覧者* ロールは見るだけで、何かを変えるボタンはすべて無効です。サーバーも再確認します |
| アシスタントが誤ってアーム・ディスアームする | 入力したコマンドのみ（音声入力はキーボードのマイク）。アームとディスアームには、あなたに結び付いた確認が必要で、電話のロックの内側で行います |

権限のテキスト（Face ID、ローカルネットワーク）は 8 言語すべてにあります。ここにあるものは iPhone では一度も動いていません。Face ID、キーチェーン、証明書ルールは実機で未検証です。[docs/CLIENT_BOUNDARY.md](docs/CLIENT_BOUNDARY.md) と [SECURITY.md](SECURITY.md) を参照してください。""",
      "interfaces": r"""これはクライアントです。ARMOR-SERVER の 26 のパスを呼び出し（`tools/ios_lint.py` が数え、Android クライアントも呼ぶことを検査）、カメラの MJPEG ストリームを独自のパーサー（`MjpegParser.swift`）で切り出します。

| 部分 | 設定内容 |
|---|---|
| 2 つのアドレス | 自宅 Wi-Fi ではプライベートアドレス、外出先のモバイル通信では動的 DNS 名または VPN のアドレスを使います。片方が応答しなければもう片方を試し、何が失敗したかをメッセージで伝えます（`Reach.swift`、`Connector.swift`） |
| カメラ | 画面に出ている映像だけが動くグリッド、カメラを動かすパッドとスナップショット付きの全画面表示、切れたら待ち時間を延ばしながら再要求するストリーム |
| プッシュ | 閉じたアプリにアラームが届くのはプッシュ（`Push.swift`、Firebase）経由のみで、サーバーでプッシュが有効かつ設置環境が自前の `GoogleService-Info.plist` を用意した場合に限ります。未検証です |""",
      "configuration": r"""| 名前 | 値 | 設定内容 |
|---|---|---|
| iOS | 16.0+ | 最低バージョン（`project.yml` で設定） |
| Xcode / Swift | 15+ / 5.9+ | アプリのビルド／テスト実行用 |
| `MARKETING_VERSION`, `CURRENT_PROJECT_VERSION` | 0.0.1, 1 | アプリのバージョン（`project.yml` より） |
| `GoogleService-Info.plist` | プッシュ用 | 設置環境ごとのファイル。リポジトリには置きません |

アプリ内：2 つのアドレス、*ログイン状態を保持*、電話のロック、言語（8 言語または電話に従う）は *その他 > 言語* にあります。""",
      "quickstart": r"""**必要なもの:** アプリのビルドには Xcode 15+ と iOS 16+ の Mac、テストには Swift 5.9+（macOS または Linux）、検査には Python 3.11。

```sh
swift test                  # 146 tests of ArmorCore (macOS or Linux)
python tools/ios_lint.py    # structure, eight languages, contract (any system)
xcodegen generate           # then open ARMOR-IOS-CONTROL.xcodeproj in Xcode (on a Mac)
```

Xcode プロジェクトは `project.yml` から XcodeGen で生成します。署名チームを選び、アプリアイコンを追加し、プッシュにはインストール専用の `GoogleService-Info.plist` を追加してください（リポジトリには保存しません）。[クライアントの境界](docs/CLIENT_BOUNDARY.md)を参照してください。""",
      "testing": r"""```sh
swift test                  # macOS or Linux
python tools/ios_lint.py    # any system, no Mac needed
python -I tools/armor_ci_validate.py
```

| テストファイル | テスト数 | 対象 |
|---|---|---|
| `ControllerTests.swift` | 15 | コントローラーのユースケース |
| `ClientTests.swift` | 14 | サーバーとの接続とその解析 |
| `LockTests.swift` | 12 | 電話のロック |
| `ModelsTests.swift` | 12 | サーバーから読むモデル |
| `ReachTests.swift` | 11 | 2 つのアドレスの選択 |
| `SecurityTests.swift` | 8 | セッション保管庫と証明書への信頼 |
| `EndpointTests.swift`, `MjpegTests.swift`, `TranslatorTests.swift` | 7 + 7 + 7 | アドレス解析、MJPEG の切り出し、翻訳 |
| `PolicyTests.swift`, `AlarmCodesTests.swift` | 6 + 4 | アラームポリシーとアラームコード |

146 件のテストは実サーバーのデータで動きます。`tools/ios_lint.py` は Mac なしで通ります：Swift ファイル 31、8 言語の 241 フレーズ、サーバーパス 26。実機で動くテストはありません。""",
      "build": "Xcode プロジェクトは XcodeGen で `project.yml` から生成します。署名チームを選び、アプリのアイコンを `App/Resources/Assets.xcassets/AppIcon.appiconset` に、プッシュ用に設置環境の `GoogleService-Info.plist` を追加してください。Xcode でビルドしたことはありません。",
      "troubleshooting": r"""| 症状 | 原因 | 対処 |
|---|---|---|
| 接続が拒否され通知される | 設置環境の証明書の鍵が変わった | 意図して変えたなら Studio の QR で再ペアリング |
| どちらのアドレスも応答しない | アドレスの誤り、ネットワークなし、または自宅外への http（拒否：パスワードは平文で送りません） | 両方のアドレスを確認し、外出先では https を使う |
| `wrong_pin`、`pin_locked`、`pin_not_set` | サーバーが解除 PIN を拒否。アプリはコードをあなたの言語で表示します | PIN を入れ直すかロック解除を待つ。PIN は Studio で設定 |""",
      "structure": r"""<p align="center">
  <img src="images/repository-structure.svg" alt="ARMOR-IOS-CONTROL のリポジトリ構造" width="100%">
</p>

<details>
<summary>ツリーのテキスト版</summary>

```text
ARMOR-IOS-CONTROL/
├── Sources/ArmorCore/                   アプリのルール：Swift パッケージ
├── App/                                 SwiftUI 画面と iPhone が必要な部分
├── Tests/                               146 件のテストと実サーバーのデータ
├── docs/                                このリポジトリのガイド
├── tools/                               共通の CI チェックとプロジェクトツール
├── .github/                             CI ワークフローと Issue・Pull Request のテンプレート
├── images/                              バナー、アイコン、この README の 2 つの図
├── armor.project.json                   マニフェスト：バージョン、役割、成熟度、ビルドコマンド
├── CHANGELOG.md                         各バージョンの変更点
├── SECURITY.md SUPPORT.md LICENSE       セキュリティポリシー、サポート、ライセンス
├── CONTRIBUTING.md CODE_OF_CONDUCT.md   貢献方法と行動規範
├── Package.swift                        Swift パッケージ：ArmorCore とそのテスト
├── project.yml                          XcodeGen：ここから Xcode プロジェクトを生成
└── .gitattributes .gitignore            Git の設定
```

</details>""",
      "roadmap": r"""**現時点の既知の制限**

* iPhone では何も動いていません。SwiftUI 画面は Xcode でビルドしておらず、Face ID、キーチェーン、証明書ルール、ライブカメラ、通知の音、読み上げの声、Firebase のプッシュは未検証です。
* テスト済みなのはルール（`ArmorCore`）だけで、Linux 上のみです。
* アプリはバックグラウンドで監視しません。iOS では閉じたアプリがサーバーに問い合わせることはできません。

**今後**

* Xcode で画面をビルドし、iPhone で CM5 テストベンチに対してアプリを動かす。
* Face ID、キーチェーン、証明書ルール、ライブカメラ、プッシュを試す。""",
    },
  },
  "zh": {
    "tagline": "ARMOR-SERVER 的 iPhone 操作员客户端：状态、布防、警报、报警主机、摄像头和助手，支持八种语言",
    "honest": "应用的规则（服务器连接、响应解析、地址选择、手机锁、会话保险库、证书信任、警报策略、用例、MJPEG 切分）是 Swift 包 `ArmorCore`，由 146 个单元测试覆盖，可在 macOS 或 Linux 上用 `swift test` 运行；`tools/ios_lint.py` 无需 Mac 即可检查结构、八张语言表和接口契约。**尚未**证明的部分：SwiftUI 界面以及需要 iPhone 的部分（Face ID、钥匙串、证书规则、实时摄像头、通过 Firebase 的推送）尚未在 Xcode 中构建，也未在设备上运行。",
    "glance": [
      [
        "角色",
        "ARMOR-SERVER 的 iPhone 操作客户端（家族：Clients，上级：ARMOR-SERVER）",
      ],
      [
        "技术栈",
        "Swift 5.9+ / SwiftUI, iOS 16+",
      ],
      [
        "测试",
        "146 (`swift test`)",
      ],
      [
        "语言",
        "8（每种语言 241 条短语，由 `ios_lint.py` 检查）",
      ],
      [
        "运行位置",
        "iOS 16+ 的 iPhone；测试在 macOS 或 Linux 上运行",
      ],
      [
        "真实硬件",
        "尚未在 iPhone 上运行；规则在 Linux 上测试",
      ],
      [
        "许可证",
        "GPL-3.0-or-later",
      ],
    ],
    "status": {
      "software": "应用的规则是一个 Swift 包（`ArmorCore`）；SwiftUI 界面尚未在 Xcode 中构建。",
      "tests": "146 项单元测试在 macOS 或 Linux 上通过 `swift test` 运行，`tools/ios_lint.py` 无需 Mac 即可检查结构、八种语言表和契约；没有任何测试在设备上运行。",
      "ui": "SwiftUI 界面已编写，但尚未在 Xcode 中构建，也没有在 iPhone 上运行。",
      "hardware": "尚未在 iPhone 上运行过：规则只在 Linux 上测试。",
      "security": "手机锁定、会话保险库和对证书的信任是在 Linux 上测试的规则；Face ID、钥匙串和证书规则尚未在设备上运行过。",
      "integration": "实时摄像头和通过 Firebase 的推送尚未试过；与服务器的连接和解析已对照共享契约测试。",
      "docs": "八种语言和更新日志均为最新。",
    },
    "docs": [
      "[客户端边界](docs/CLIENT_BOUNDARY.md)：客户端做什么、绝不做什么，以及如何构建",
    ],
    "contributing_first": "提交 Pull Request 之前请运行 `swift test` and `python tools/ios_lint.py` and `python -I tools/armor_ci_validate.py`：必须通过。参见 [CONTRIBUTING.md](CONTRIBUTING.md) 和[行为准则](CODE_OF_CONDUCT.md)。",
    "languages_extra": "",
    "body": {
      "overview": r"""* **使用服务器自身的登录：** 家里的地址（在家与外出）、用户名和密码；密码创建 HttpOnly 会话；只有勾选**记住我**才会保存（存放在这部手机的钥匙串中，不会备份）。**viewer** 角色只能查看：所有会修改内容的按钮都会关闭。
* **两个地址：** 家中 Wi-Fi 使用内网地址，移动数据使用外出地址（动态 DNS 名称或 VPN）；其中一个没有响应时会尝试另一个，并提示哪里出了问题。
* **手机锁：** 在布防、撤防、静音警笛、解锁及其他关键操作之前要求 Face ID、Touch ID 或密码（默认仅在手机有 Face ID 或 Touch ID 时开启），如果您开启，打开应用时也会要求。管理员可以强制要求，但不能降低您的选择；没有密码的手机永远不会被拒之门外，锁定界面始终提供用密码登录。可选（默认关闭，带警告）：仅在手机解锁时才能读取已保存的会话。
* **布防与撤防**：先检查哪些部分会成为盲区或产生误报，撤防需要 PIN；待确认的**警报**及其角标；**报警主机**（外出布防或在家布防、撤防、警笛静音）和**历史记录**；带开/关的**设备**，对回路和关键设备需要确认。
* **摄像头**通过服务器查看（应用永远没有摄像头密码）：只有屏幕上可见的画面才会播放的网格、带方向键用于移动摄像头的全屏视图以及拍照，画面中断时以逐渐增长的等待时间重新请求。
* **按你的意愿设置通知：** 可全部静音，或无声显示；可按严重级别和类型关闭（严重警报绝不会被隐藏，除非使用“全部静音”开关）；可为每个严重级别和每种类型选择自己的声音文件，并带有播放按钮；还可设置朗读警报的声音（女声、男声、年龄、风格、语速、低严重级别通知），并带有试听按钮。一个画面中含两个镜头的摄像头会显示为两个窗口。
* **助手：** 文字指令（键盘麦克风可听写），布防和撤防需要与您绑定的确认，并位于手机锁之后。
* **证书信任：** 首次连接时记住安装证书的密钥，或通过 Studio 的二维码配对；如果发生变化，连接会被拒绝并通知您。
* **八种语言**（英语、西班牙语、德语、法语、意大利语、日语、中文和葡萄牙（葡萄牙）语），可在*更多 > 语言*中选择或跟随手机，每个界面都有帮助。""",
      "role": r"""ARMOR-IOS-CONTROL 是 iPhone 通往同一个 [ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER) 的窗口，[ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) 和 [ARMOR-ANDROID-CONTROL](https://github.com/JuanenRac/ARMOR-ANDROID-CONTROL) 也使用它：只通过它读取和下达命令，并使用与 Android 应用相同的接口契约。

| 名称 | 方式 | 用途 |
|---|---|---|
| ARMOR-SERVER | HTTP `/api/v1`, MJPEG | 应用读取和下达的一切；不与其他对象通信 |
| ARMOR-ANDROID-CONTROL | 相同合约 | `ios_lint.py` 检查应用只调用 Android 客户端也调用的路径 |
| ARMOR-STUDIO | QR | 配对安装环境证书的密钥 |""",
      "architecture": r"""<p align="center">
  <img src="images/architecture.svg" alt="ARMOR-IOS-CONTROL 的架构：谁调用它、它包含什么、它依赖什么" width="100%">
</p>""",
      "security": r"""| 威胁 | 防御 |
|---|---|
| 手机上的密码 | 仅在勾选*记住我*时保存，存于本机钥匙串且绝不备份；会话是服务器的 HttpOnly Cookie |
| 手机落入他人之手时的关键操作 | 在布防、撤防、静音警笛、解锁等关键操作前要求 Face ID、Touch ID 或密码；管理员可以强制要求，但不能降低你的选择；没有密码的手机永远不会被拒之门外 |
| 被更改或伪造的证书 | 首次记住安装环境证书的密钥，或用 Studio 的二维码配对；若发生变化，则拒绝连接并通知你 |
| 以明文发送的密码 | 仅对私有网络或回环地址使用明文 HTTP（`NSAllowsLocalNetworking`）；其他情况需要 https，否则应用拒绝发送密码 |
| 手机上的摄像头密码 | 摄像头经服务器转发：应用没有摄像头密码，也没有 RTSP 地址 |
| 查看者修改了内容 | *查看者*角色只能查看：所有会修改内容的按钮都被禁用；服务器会再次检查 |
| 助手误操作布防或撤防 | 仅限文字命令（键盘麦克风负责听写）；布防和撤防需要与你绑定的确认，并位于手机锁之后 |

权限文字（Face ID、本地网络）有全部八种语言。这里的一切都没有在 iPhone 上运行过：Face ID、钥匙串和证书规则都没有在真机上测试。请阅读 [docs/CLIENT_BOUNDARY.md](docs/CLIENT_BOUNDARY.md) 和 [SECURITY.md](SECURITY.md)。""",
      "interfaces": r"""它是客户端：调用 ARMOR-SERVER 的 26 条路径（`tools/ios_lint.py` 会统计并检查 Android 客户端也调用它们），并用自己的解析器切分摄像头的 MJPEG 流（`MjpegParser.swift`）。

| 部分 | 作用 |
|---|---|
| 两个地址 | 在家庭 Wi-Fi 下使用私有地址，在移动数据下使用外出地址（动态 DNS 名称或 VPN）；一个无响应就尝试另一个，并说明失败原因（`Reach.swift`、`Connector.swift`） |
| 摄像头 | 只有屏幕上可见的画面才会运行的网格、带方向盘和快照的全屏视图，以及中断后以递增等待时间重新请求的视频流 |
| 推送 | 报警只能通过推送（`Push.swift`、Firebase）到达已关闭的应用，且仅当服务器开启推送且安装环境提供自己的 `GoogleService-Info.plist` 时才可行；未经试验 |""",
      "configuration": r"""| 名称 | 值 | 作用 |
|---|---|---|
| iOS | 16.0+ | 最低版本，在 `project.yml` 中设置 |
| Xcode / Swift | 15+ / 5.9+ | 用于构建应用／运行测试 |
| `MARKETING_VERSION`, `CURRENT_PROJECT_VERSION` | 0.0.1, 1 | 应用版本，来自 `project.yml` |
| `GoogleService-Info.plist` | 用于推送 | 安装环境自己的文件，绝不保存在仓库中 |

应用内：两个地址、*记住我*、手机锁和语言（八种语言或跟随手机）位于*更多 > 语言*。""",
      "quickstart": r"""**要求:** 构建应用需要装有 Xcode 15+ 和 iOS 16+ 的 Mac；测试需要 Swift 5.9+（macOS 或 Linux）；检查需要 Python 3.11。

```sh
swift test                  # 146 tests of ArmorCore (macOS or Linux)
python tools/ios_lint.py    # structure, eight languages, contract (any system)
xcodegen generate           # then open ARMOR-IOS-CONTROL.xcodeproj in Xcode (on a Mac)
```

Xcode 工程由 `project.yml` 通过 XcodeGen 生成。请选择签名团队、添加应用图标，并为推送添加安装专用的 `GoogleService-Info.plist`（绝不保存在仓库中）。参见[客户端边界](docs/CLIENT_BOUNDARY.md)。""",
      "testing": r"""```sh
swift test                  # macOS or Linux
python tools/ios_lint.py    # any system, no Mac needed
python -I tools/armor_ci_validate.py
```

| 测试文件 | 测试数 | 覆盖内容 |
|---|---|---|
| `ControllerTests.swift` | 15 | 控制器的用例 |
| `ClientTests.swift` | 14 | 与服务器的连接及解析 |
| `LockTests.swift` | 12 | 手机锁 |
| `ModelsTests.swift` | 12 | 从服务器读取的模型 |
| `ReachTests.swift` | 11 | 两个地址之间的选择 |
| `SecurityTests.swift` | 8 | 会话保险库和对证书的信任 |
| `EndpointTests.swift`, `MjpegTests.swift`, `TranslatorTests.swift` | 7 + 7 + 7 | 地址解析、MJPEG 切分和翻译器 |
| `PolicyTests.swift`, `AlarmCodesTests.swift` | 6 + 4 | 报警策略和报警代码 |

这 146 个测试使用真实服务器的数据。`tools/ios_lint.py` 无需 Mac 即可通过：31 个 Swift 文件、8 种语言的 241 条短语、26 条服务器路径。没有任何测试在真机上运行。""",
      "build": "Xcode 项目由 XcodeGen 根据 `project.yml` 生成：选择签名团队，把应用图标加入 `App/Resources/Assets.xcassets/AppIcon.appiconset`，推送还需加入安装环境的 `GoogleService-Info.plist`。从未在 Xcode 中构建过。",
      "troubleshooting": r"""| 现象 | 原因 | 处理 |
|---|---|---|
| 连接被拒绝并通知你 | 安装环境证书的密钥发生了变化 | 若是有意更改，请用 Studio 的二维码重新配对 |
| 两个地址都无响应 | 地址错误、没有网络，或对家庭之外使用 http（会被拒绝：密码不会以明文发送） | 检查两个地址；在外时使用 https |
| `wrong_pin`、`pin_locked`、`pin_not_set` | 服务器拒绝撤防 PIN；应用会用你的语言显示该代码 | 重新输入 PIN 或等待锁定结束；在 Studio 中设置 |""",
      "structure": r"""<p align="center">
  <img src="images/repository-structure.svg" alt="ARMOR-IOS-CONTROL 的仓库结构" width="100%">
</p>

<details>
<summary>目录树的文本版</summary>

```text
ARMOR-IOS-CONTROL/
├── Sources/ArmorCore/                   应用的规则：一个 Swift 包
├── App/                                 SwiftUI 界面和需要 iPhone 的部分
├── Tests/                               146 个测试和真实服务器的数据
├── docs/                                本仓库的指南
├── tools/                               共享的 CI 检查和项目工具
├── .github/                             CI 工作流以及 Issue 和 Pull Request 模板
├── images/                              横幅、图标和本 README 的两幅图
├── armor.project.json                   清单：版本、角色、成熟度、构建命令
├── CHANGELOG.md                         每个版本的变化
├── SECURITY.md SUPPORT.md LICENSE       安全策略、支持和许可证
├── CONTRIBUTING.md CODE_OF_CONDUCT.md   如何贡献与行为准则
├── Package.swift                        Swift 包：ArmorCore 及其测试
├── project.yml                          XcodeGen：由此生成 Xcode 项目
└── .gitattributes .gitignore            Git 设置
```

</details>""",
      "roadmap": r"""**目前已知的限制**

* 尚未在 iPhone 上运行过：SwiftUI 界面没有在 Xcode 中构建；Face ID、钥匙串、证书规则、实时摄像头、通知声音、朗读声音和 Firebase 推送均未测试。
* 只有规则（`ArmorCore`）经过测试，而且仅在 Linux 上。
* 应用不会在后台监视：iOS 不允许已关闭的应用查询服务器。

**下一步**

* 在 Xcode 中构建界面，并在 iPhone 上对 CM5 测试台运行应用。
* 试验 Face ID、钥匙串、证书规则、实时摄像头和推送。""",
    },
  },
  "pt": {
    "tagline": "Cliente de operador para iPhone do ARMOR-SERVER: estado, armar, alarmes, centrais de alarme, câmaras e o assistente, em oito idiomas",
    "honest": "as regras da app (ligação ao servidor, leitura das respostas, escolha do endereço, bloqueio do telemóvel, cofre da sessão, confiança no certificado, política de alarmes, casos de uso, corte do MJPEG) são o pacote Swift `ArmorCore`, coberto por 146 testes unitários que correm com `swift test` em macOS ou Linux, e `tools/ios_lint.py` verifica a estrutura, as oito tabelas de idiomas e o contrato sem Mac. O que **ainda não** está provado: os ecrãs SwiftUI e as partes que precisam de um iPhone (Face ID, porta-chaves, regras de certificado, câmara em direto, push com Firebase) não foram compilados no Xcode nem executados num dispositivo.",
    "glance": [
      [
        "Função",
        "Cliente de operador para iPhone do ARMOR-SERVER (família: Clients, pai: ARMOR-SERVER)",
      ],
      [
        "Tecnologia",
        "Swift 5.9+ / SwiftUI, iOS 16+",
      ],
      [
        "Testes",
        "146 (`swift test`)",
      ],
      [
        "Línguas",
        "8 (241 frases por língua, verificadas pelo `ios_lint.py`)",
      ],
      [
        "Funciona em",
        "Um iPhone com iOS 16+; os testes correm em macOS ou Linux",
      ],
      [
        "Em hardware real",
        "Ainda não foi executado num iPhone; as regras são testadas em Linux",
      ],
      [
        "Licença",
        "GPL-3.0-or-later",
      ],
    ],
    "status": {
      "software": "As regras da app são um pacote Swift (`ArmorCore`); os ecrãs SwiftUI não foram compilados no Xcode.",
      "tests": "Passam 146 testes unitários com `swift test` em macOS ou Linux, e o `tools/ios_lint.py` verifica a estrutura, as tabelas dos oito idiomas e o contrato sem um Mac; nenhum teste corre num dispositivo.",
      "ui": "Os ecrãs SwiftUI estão escritos, mas não foram compilados no Xcode nem executados num iPhone.",
      "hardware": "Não correu num iPhone: as regras só são testadas em Linux.",
      "security": "O bloqueio do telefone, o cofre da sessão e a confiança no certificado são regras testadas em Linux; o Face ID, o porta-chaves e as regras do certificado não correram num dispositivo.",
      "integration": "A câmara em direto e o push através do Firebase não foram experimentados; a ligação ao servidor e a análise são testadas contra o contrato partilhado.",
      "docs": "Oito idiomas e o registo de alterações estão atualizados.",
    },
    "docs": [
      "[Limites do cliente](docs/CLIENT_BOUNDARY.md): o que o cliente faz e nunca faz, e como o compilar",
    ],
    "contributing_first": "Antes de um pull request, execute `swift test` and `python tools/ios_lint.py` and `python -I tools/armor_ci_validate.py`: tem de passar. Consulte [CONTRIBUTING.md](CONTRIBUTING.md) e o [código de conduta](CODE_OF_CONDUCT.md).",
    "languages_extra": "",
    "body": {
      "overview": r"""* **Inicie sessão com o acesso do próprio servidor:** os endereços da casa (em casa e fora), utilizador e palavra-passe; a palavra-passe cria uma sessão HttpOnly; só é guardada se marcar **Lembrar-me** (na porta-chaves deste telemóvel, sem cópia de segurança). O papel **viewer** só olha: todo o botão que altera algo fica desligado.
* **Dois endereços:** o privado na Wi-Fi de casa e o de fora (um nome DNS dinâmico ou a VPN) com dados móveis; se um não responder tenta-se o outro e a mensagem diz o que falha.
* **Bloqueio com o telemóvel:** Face ID, Touch ID ou o código antes de armar, desarmar, silenciar uma sirene, desbloquear e as outras ordens críticas (ativo por defeito só com Face ID ou Touch ID) e, se o ativar, para abrir a app. O administrador pode exigi-lo, nunca baixar o que escolheu; um telemóvel sem código nunca fica de fora e o ecrã de bloqueio oferece sempre entrar com a palavra-passe. Opcionalmente (desligado, com aviso) a sessão guardada só se lê com o telemóvel desbloqueado.
* **Armar e desarmar** depois de verificar o que ficaria cego ou ruidoso, com o PIN para desarmar; **alarmes** a confirmar, com contador; as **centrais de alarme** (armar ausente ou em casa, desarmar, silenciar a sirene) e o **histórico**; **dispositivos** com Ligar / Desligar e confirmação para circuitos e críticos.
* **Câmaras** através do servidor (a app nunca tem a palavra-passe da câmara): uma grelha onde só correm as imagens visíveis, uma vista completa com cruzeta para mover a câmara e foto, e um fluxo pedido de novo com esperas crescentes se se cortar.
* **Avisos à tua medida:** silenciar tudo ou mostrá-lo sem som; desligar gravidades e tipos (um alarme crítico nunca é escondido, a não ser com o interruptor que silencia tudo); um ficheiro de som teu para cada gravidade e cada tipo, com botão de reprodução; e a voz que diz os alarmes (mulher, homem, idade, estilo, velocidade, avisos de baixa gravidade), com botão de teste. Uma câmara com duas lentes numa só imagem aparece como duas janelas.
* **O assistente:** ordens escritas (o microfone do teclado dita), com uma confirmação ligada a si para armar e desarmar, atrás do bloqueio.
* **Confiança no certificado:** a chave do certificado da instalação é memorizada na primeira vez ou emparelhada com o QR do Studio; se mudar, a ligação é recusada e é avisado.
* **Oito idiomas** (inglês, espanhol, alemão, francês, italiano, japonês, chinês e português de Portugal), a escolher em *Mais > Idioma* ou a seguir o telemóvel, com ajuda para cada ecrã.""",
      "role": r"""O ARMOR-IOS-CONTROL é a janela do iPhone para o mesmo [ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER) que o [ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) e o [ARMOR-ANDROID-CONTROL](https://github.com/JuanenRac/ARMOR-ANDROID-CONTROL) usam: lê e ordena através dele e nada mais, e fala o mesmo contrato que a app Android.

| Nome | Como | Para quê |
|---|---|---|
| ARMOR-SERVER | HTTP `/api/v1`, MJPEG | Tudo o que a app lê e ordena; não fala com mais nada |
| ARMOR-ANDROID-CONTROL | mesmo contrato | O `ios_lint.py` verifica que a app só chama caminhos que o cliente Android também chama |
| ARMOR-STUDIO | QR | Emparelha a chave do certificado da instalação |""",
      "architecture": r"""<p align="center">
  <img src="images/architecture.svg" alt="Arquitetura de ARMOR-IOS-CONTROL: quem o chama, o que contém e de que depende" width="100%">
</p>""",
      "security": r"""| Ameaça | Defesa |
|---|---|
| A palavra-passe no telemóvel | Guardada só com *Lembrar-me*, no Keychain deste telemóvel e nunca em cópias de segurança; a sessão é um cookie HttpOnly do servidor |
| Uma ordem crítica com o telemóvel noutras mãos | Face ID, Touch ID ou o código antes de armar, desarmar, silenciar uma sirene, desbloquear e as outras ordens críticas; o administrador pode exigi-lo, nunca baixar o que escolheu; um telemóvel sem código nunca fica de fora |
| Um certificado alterado ou forjado | A chave do certificado da instalação é memorizada à primeira vez ou emparelhada com o QR do Studio; se mudar, a ligação é recusada e é avisado |
| A palavra-passe enviada em claro | HTTP simples só para um endereço de rede privada ou loopback (`NSAllowsLocalNetworking`); tudo o resto exige https, senão a app recusa enviar a palavra-passe |
| Uma palavra-passe de câmara no telemóvel | As câmaras passam pelo servidor: a app não tem palavra-passe de câmara nem endereço RTSP |
| Um visualizador altera algo | O papel *visualizador* só vê: todos os botões que alteram algo estão desligados; o servidor volta a verificar |
| O assistente arma ou desarma por engano | Só ordens escritas (o microfone do teclado dita); armar e desarmar exigem uma confirmação ligada a si, atrás do bloqueio do telemóvel |

Os textos de permissões (Face ID, rede local) existem nas oito línguas. Nada disto correu num iPhone: o Face ID, o Keychain e as regras de certificado não foram testados num dispositivo. Leia [docs/CLIENT_BOUNDARY.md](docs/CLIENT_BOUNDARY.md) e [SECURITY.md](SECURITY.md).""",
      "interfaces": r"""É um cliente: chama 26 caminhos do ARMOR-SERVER (o `tools/ios_lint.py` conta-os e verifica que o cliente Android também os chama) e corta o fluxo MJPEG das câmaras com um analisador próprio (`MjpegParser.swift`).

| Parte | O que define |
|---|---|
| Dois endereços | O privado no Wi-Fi de casa e o de fora (um nome DNS dinâmico ou a VPN) com dados móveis; se um não responder tenta-se o outro e a mensagem diz o que falhou (`Reach.swift`, `Connector.swift`) |
| Câmaras | Uma grelha onde só correm as imagens visíveis, uma vista completa com comando para mover a câmara e um instantâneo, e um fluxo pedido de novo com esperas crescentes se cair |
| Push | Os alarmes só chegam a uma app fechada por push (`Push.swift`, Firebase), e só se o servidor tiver o push ativo e a instalação trouxer o seu próprio `GoogleService-Info.plist`; não experimentado |""",
      "configuration": r"""| Nome | Valor | O que define |
|---|---|---|
| iOS | 16.0+ | Versão mínima, definida em `project.yml` |
| Xcode / Swift | 15+ / 5.9+ | Para compilar a app / para executar os testes |
| `MARKETING_VERSION`, `CURRENT_PROJECT_VERSION` | 0.0.1, 1 | A versão da app, de `project.yml` |
| `GoogleService-Info.plist` | para push | O ficheiro próprio da instalação, nunca guardado no repositório |

Na app: os dois endereços, *Lembrar-me*, o bloqueio do telemóvel e a língua (as oito ou seguir o telemóvel) em *Mais > Língua*.""",
      "quickstart": r"""**Requisitos:** um Mac com Xcode 15+ e iOS 16+ para compilar a app; Swift 5.9+ (macOS ou Linux) para os testes; Python 3.11 para as verificações.

```sh
swift test                  # 146 tests of ArmorCore (macOS or Linux)
python tools/ios_lint.py    # structure, eight languages, contract (any system)
xcodegen generate           # then open ARMOR-IOS-CONTROL.xcodeproj in Xcode (on a Mac)
```

O projeto Xcode gera-se a partir de `project.yml` com o XcodeGen. Escolha uma equipa de assinatura, adicione o ícone da app e, para o push, o `GoogleService-Info.plist` da instalação (nunca guardado no repositório). Veja o [limite do cliente](docs/CLIENT_BOUNDARY.md).""",
      "testing": r"""```sh
swift test                  # macOS or Linux
python tools/ios_lint.py    # any system, no Mac needed
python -I tools/armor_ci_validate.py
```

| Ficheiro de testes | Testes | O que cobre |
|---|---|---|
| `ControllerTests.swift` | 15 | Os casos de uso do controlador |
| `ClientTests.swift` | 14 | A ligação ao servidor e a sua interpretação |
| `LockTests.swift` | 12 | O bloqueio do telemóvel |
| `ModelsTests.swift` | 12 | Os modelos lidos do servidor |
| `ReachTests.swift` | 11 | A escolha entre os dois endereços |
| `SecurityTests.swift` | 8 | O cofre da sessão e a confiança no certificado |
| `EndpointTests.swift`, `MjpegTests.swift`, `TranslatorTests.swift` | 7 + 7 + 7 | A leitura de endereços, o corte MJPEG e o tradutor |
| `PolicyTests.swift`, `AlarmCodesTests.swift` | 6 + 4 | A política de alarmes e os códigos de alarme |

Os 146 testes usam dados de um servidor real. O `tools/ios_lint.py` passa sem Mac: 31 ficheiros Swift, 241 frases em 8 línguas, 26 caminhos do servidor. Nenhum teste corre num dispositivo.""",
      "build": "O projeto Xcode gera-se a partir de `project.yml` com o XcodeGen: escolha uma equipa de assinatura, junte o ícone da app a `App/Resources/Assets.xcassets/AppIcon.appiconset` e, para push, o `GoogleService-Info.plist` da instalação. Nunca foi compilado no Xcode.",
      "troubleshooting": r"""| Vê | Porque | Faça |
|---|---|---|
| A ligação é recusada e é avisado | A chave do certificado da instalação mudou | Emparelhe de novo com o QR do Studio se o mudou de propósito |
| Nenhum dos dois endereços responde | Endereço errado, sem rede, ou http para um sítio fora de casa (recusado: a palavra-passe não é enviada em claro) | Verifique os dois endereços; use https fora de casa |
| `wrong_pin`, `pin_locked`, `pin_not_set` | O servidor recusa o PIN de desarmar; a app mostra o código na sua língua | Escreva o PIN de novo ou espere o fim do bloqueio; defina-o no Studio |""",
      "structure": r"""<p align="center">
  <img src="images/repository-structure.svg" alt="Estrutura do repositório de ARMOR-IOS-CONTROL" width="100%">
</p>

<details>
<summary>Versão em texto da árvore</summary>

```text
ARMOR-IOS-CONTROL/
├── Sources/ArmorCore/                   as regras da app: um pacote Swift
├── App/                                 os ecrãs SwiftUI e as partes que precisam de um iPhone
├── Tests/                               146 testes e dados de um servidor real
├── docs/                                os guias deste repositório
├── tools/                               as verificações de CI partilhadas e as ferramentas do projeto
├── .github/                             fluxo de CI e modelos de issues e pull requests
├── images/                              faixa, ícone e as duas imagens deste README
├── armor.project.json                   manifesto: versão, função, maturidade, comando de build
├── CHANGELOG.md                         o que mudou em cada versão
├── SECURITY.md SUPPORT.md LICENSE       política de segurança, apoio e licença
├── CONTRIBUTING.md CODE_OF_CONDUCT.md   como contribuir e o código de conduta
├── Package.swift                        o pacote Swift: ArmorCore e os seus testes
├── project.yml                          XcodeGen: daqui gera-se o projeto Xcode
└── .gitattributes .gitignore            definições do Git
```

</details>""",
      "roadmap": r"""**Limites conhecidos hoje**

* Nada correu num iPhone: os ecrãs SwiftUI não foram compilados no Xcode; o Face ID, o Keychain, as regras de certificado, a câmara em direto, os sons dos avisos, a voz e o push via Firebase não foram testados.
* Só as regras (`ArmorCore`) estão testadas, e só em Linux.
* A app não vigia em segundo plano: o iOS não deixa uma app fechada consultar o servidor.

**A seguir**

* Compilar os ecrãs no Xcode e correr a app num iPhone contra a bancada de testes CM5.
* Experimentar o Face ID, o Keychain, as regras de certificado, a câmara em direto e o push.""",
    },
  },
}
