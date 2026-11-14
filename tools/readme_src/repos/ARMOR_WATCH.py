# The facts that do not depend on the language, and the words of every language, of ARMOR-WATCH, in the universal README layout.
# Copyright (C) 2026 JuanenRac (Electro Hobby 3D). GPL-3.0-or-later.

FACTS = {'emoji': '⌚',
 'layout': 'universal',
 'license_badge': 'License-GPL%203.0--or--later-blue',
 'status': [['software', 'yellow'], ['tests', 'yellow'], ['hardware', 'red'], ['docs', 'yellow']],
 'badges': [['Wear OS', 'Kotlin', '7f52ff'], ['Tests', '{{fact:tests:ARMOR-WATCH}}%20passing', '2ea44f']]}

TEXT = {'en': {'tagline': 'The minimal A.R.M.O.R. watch: alarm notices and one tap to confirm an alarm',
        'honest': 'The message contract, the Kotlin and Swift cores and the watch session are tested on a computer, and the Wear OS app, the Apple Watch app and the sending side of the Android and iPhone apps are built and pass their tests in CI; **nothing has run on a real watch, an emulator or a simulator, and the Apple Watch app is not yet inside the iPhone app.**',
        'glance': [['Role', 'The minimal watch client of A.R.M.O.R. (family: Clients, parent: ARMOR-ANDROID-CONTROL)'],
                   ['Stack', 'Kotlin (JVM core and the Wear OS app with Compose, Gradle), Swift (core and the Apple Watch app with SwiftUI); Python 3.11+ for the checks'],
                   ['Tests', '{{fact:tests:ARMOR-WATCH}} in Python (`python -m unittest discover -s tests`) and the Kotlin tests (`./gradlew test`)'],
                   ['Messages', 'The switch of the relay, an alert, the clear of an alert and the confirmation back'],
                   ['Runs on', 'Any computer with a JDK 21 (Kotlin core) or a Mac (Swift core); a Wear OS 3+ watch or an Apple Watch paired with the phone (apps built in CI, never run)'],
                   ['On real hardware', 'None yet: no watch or emulator has run it'],
                   ['License', 'GPL-3.0-or-later']],
        'status': {'software': 'The Kotlin and Swift cores read and check every message and keep the alerts in memory; the Wear OS app, the Apple Watch app and the senders in the Android and iPhone apps are written.',
                   'tests': '{{fact:tests:ARMOR-WATCH}} Python tests and the Kotlin tests run the same accepted and rejected examples of the contract; the Kotlin tests '
                            'run in CI.',
                   'hardware': 'No watch, emulator or simulator has run them; the apps are only built and unit-tested in CI.',
                   'docs': 'Eight languages, the protocol notes and the contract are written and up to date.'},
        'docs': ['[Protocol notes](docs/PROTOCOL.md): how the phone and the watch talk',
                 '[Message contract](docs/watch_alert_contract.json): the messages, the limits and the accepted and rejected examples'],
        'contributing_first': 'Before a pull request run `python -m unittest discover -s tests` and `python -I tools/armor_ci_validate.py`: it must pass. See '
                              '[CONTRIBUTING.md](CONTRIBUTING.md) and the [code of conduct](CODE_OF_CONDUCT.md).',
        'languages_extra': '',
        'body': {'overview': '* **A minimal watch, not a second app.** ARMOR-ANDROID-CONTROL and ARMOR-IOS-CONTROL stay the full client; the watch only shows the alarms '
                             'and notices the phone chooses to send and lets the person confirm an alarm with one tap.\n'
                             '* **The phone is the only side that talks to ARMOR-SERVER.** The watch holds no session, no password and no key, and keeps nothing on the '
                             'watch: what it shows is in memory and is forgotten when the app closes.\n'
                             '* **Off by default.** Nothing reaches the watch until the person turns on the option of the watch alerts in the phone app; until the phone '
                             'says so, the watch drops every alert it receives.\n'
                             '* **Four small messages** (`relay`, `alert`, `alert_clear`, `alert_ack`) with limits and accepted and rejected examples in '
                             '`docs/watch_alert_contract.json`; the phone writes the texts in the language of the person, so the watch has nothing to translate.\n'
                             '* **No sound or vibration of its own:** the watch adds none beyond the standard notification of the system.',
                 'role': 'ARMOR-WATCH is the wrist end of the phone apps. [ARMOR-ANDROID-CONTROL](https://github.com/JuanenRac/ARMOR-ANDROID-CONTROL) and '
                         '[ARMOR-IOS-CONTROL](https://github.com/JuanenRac/ARMOR-IOS-CONTROL) keep the session with '
                         '[ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER); the watch receives a short alert from the phone and sends back the identifier of an '
                         'alarm the person confirmed, which the phone checks and carries out.',
                 'architecture': '<p align="center">\n'
                                 '  <img src="images/architecture.svg" alt="ARMOR-WATCH architecture: the person, the Kotlin core and its contract, the phone app and '
                                 'the server" width="100%">\n'
                                 '</p>',
                 'security': '| Threat | Defence |\n'
                             '|---|---|\n'
                             '| A watch that still shows alerts after the option is turned off | The phone sends `relay` with `enabled: false` and the watch forgets '
                             'what it showed; the inbox starts switched off |\n'
                             '| A forged or malformed message | Every message is checked against the contract (type, version, limits, exact kinds) and one that fails is '
                             'dropped without an error; nothing over 4096 characters is read |\n'
                             '| A stolen watch with a session on it | There is none: the watch holds no session, password or key and writes nothing to storage |\n'
                             '| A confirmation sent twice or for an alarm that is not there | The confirmation goes out once per alert, only for an alert that asks for '
                             'it and has not expired; the phone ignores an identifier it does not know |\n'
                             '| The alarm of a duress PIN shown on the wrist | The phone never sends it (as the banner of the phone apps never shows it) |',
                 'configuration': '| Setting | Default | What it does |\n'
                                  '|---|---|---|\n'
                                  '| `titleMax`, `textMax` | 60, 160 | Longest title and text of an alert, in characters |\n'
                                  '| `ttlSeconds` | 5 - 600 | How long an alert stays before it disappears by itself |\n'
                                  '| `pendingMax` | 8 | Alerts kept at once; a critical one is never dropped for a lesser one |\n'
                                  '| `rawMax` | 4096 | A message longer than this is not read |\n'
                                  '| `relay.enabled` | false | Set by the phone; the watch shows nothing until it is true |',
                 'quickstart': '**Requirements:** Python 3.11+ for the checks; a JDK 21 for the Kotlin core (the Gradle wrapper downloads Gradle itself).\n'
                               '\n'
                               '```powershell\n'
                               'python tools/watch_contract.py                  # the examples of the contract in Python\n'
                               'python -m unittest discover -s tests            # the contract, the Kotlin constants and the protocol notes\n'
                               './gradlew test                                  # the Kotlin core (WatchProtocol and AlertInbox)\n'
                               '```\n'
                               '\n'
                               'See the [protocol notes](docs/PROTOCOL.md) for the messages and what each side does.',
                 'testing': '```powershell\n'
                            'python -m unittest discover -s tests\n'
                            './gradlew test\n'
                            'python -I tools/armor_ci_validate.py\n'
                            '```\n'
                            '\n'
                            '| Test file | Tests | What it covers |\n'
                            '|---|---|---|\n'
                            '| `test_watch_contract.py` | 10 | Every example of the contract, the limits, the Kotlin constants and the protocol notes |\n'
                            '| `WatchProtocolTest.kt` | 6 | The same examples against the Kotlin parser, the limits and the acknowledgement |\n'
                            '| `AlertInboxTest.kt` | 10 | Off by default, order, replacement, expiry, clear, one confirmation, the limit of eight |\n'
                            '\n'
                            'The Kotlin tests run in CI; no test has run on a watch or an emulator.',
                 'troubleshooting': '| You see | Because | Do |\n'
                                    '|---|---|---|\n'
                                    '| Nothing appears on the watch | The option of the watch alerts is off in the phone app, or the phone has not sent `relay` with '
                                    '`enabled: true` | Turn the option on in the phone app |\n'
                                    '| An alert disappears by itself | Its `ttlSeconds` ran out or the phone cleared it | Raise it again from the phone |\n'
                                    '| The confirmation does nothing | The alert does not ask for one, it expired, or it was already confirmed once | Confirm the alarm '
                                    'in the phone app |',
                 'structure': '<p align="center">\n'
                              '  <img src="images/repository-structure.svg" alt="Repository structure of ARMOR-WATCH" width="100%">\n'
                              '</p>\n'
                              '\n'
                              '<details>\n'
                              '<summary>Text version of the tree</summary>\n'
                              '\n'
                              '```text\n'
                              'ARMOR-WATCH/\n'
                              '├── src/\n'
                              '│   ├── main/                               WatchProtocol (the messages and their checks) and AlertInbox (the alerts on the screen)\n'
                              '│   └── test/                               the same examples as the contract, and the rules of the inbox\n'
                              '├── wear/                               the Wear OS app: screen, Data Layer service and runtime\n'
                              '├── watchos/                            the Apple Watch app: Swift core, screen and WatchConnectivity\n'
                              '├── tests/                                  the contract checked in Python\n'
                              '├── docs/                                   the contract and the protocol\n'
                              '├── tools/                                  checks and contract\n'
                              '├── gradle/                                 Gradle wrapper\n'
                              '├── .github/                                CI workflow, issue and pull-request templates\n'
                              '├── images/                                 banner, icon and the two pictures of the README\n'
                              '├── armor.project.json                      manifest: version, role, maturity, build command\n'
                              '├── CHANGELOG.md                            what changed in each version\n'
                              '├── SECURITY.md SUPPORT.md LICENSE          security policy, support and license\n'
                              '├── CONTRIBUTING.md CODE_OF_CONDUCT.md      how to contribute and the code of conduct\n'
                              '├── build.gradle.kts settings.gradle.kts    the Kotlin build\n'
                              '├── gradle.properties gradlew gradlew.bat   Gradle settings and the wrapper scripts\n'
                              '└── .gitattributes .gitignore               Git settings\n'
                              '```\n'
                              '\n'
                              '</details>',
                 'roadmap': '**Known limits today**\n\n* The Wear OS app (`wear/`, built with `-ParmorWear`), the Apple Watch app (`watchos/`, built only on a Mac) and the senders in ARMOR-ANDROID-CONTROL and ARMOR-IOS-CONTROL (off by default) are built and pass their tests in CI, but nothing has run on a real watch, an emulator or a simulator.\n* The Apple Watch app is not yet inside the iPhone app, so the pairing of the two is still to be tried; an iPhone does not pair with a Wear OS watch and an Android phone does not pair with an Apple Watch.\n* The contract is kept here; the Kotlin core, the Swift core and the phone apps run the same examples.\n\n**Next**\n\n* Prove it on a real watch, one of each kind: pair it, switch the option on, raise a test alarm, see it on the watch, confirm it with a tap and see it confirmed in ARMOR-SERVER; then switch the option off and see the alert disappear.'}},
 'es': {'tagline': 'El reloj mínimo de A.R.M.O.R.: avisos de alarma y un toque para confirmar una alarma',
        'honest': 'El contrato de mensajes, los núcleos Kotlin y Swift y la sesión del reloj se prueban en un ordenador, y la app de Wear OS, la app del Apple Watch y el lado que envía de las apps Android e iPhone se compilan y pasan sus pruebas en CI; **nada ha corrido en un reloj real, un emulador ni un simulador, y la app del Apple Watch aún no está dentro de la app del iPhone.**',
        'glance': [['Rol', 'El cliente de reloj mínimo de A.R.M.O.R. (familia: Clients, padre: ARMOR-ANDROID-CONTROL)'],
                   ['Stack', 'Kotlin (núcleo JVM y la app de Wear OS con Compose, Gradle), Swift (núcleo y la app del Apple Watch con SwiftUI); Python 3.11+ para las comprobaciones'],
                   ['Pruebas', '{{fact:tests:ARMOR-WATCH}} en Python (`python -m unittest discover -s tests`) y las pruebas de Kotlin (`./gradlew test`)'],
                   ['Mensajes', 'El interruptor del relé, una alerta, el borrado de una alerta y la confirmación de vuelta'],
                   ['Funciona en', 'Cualquier ordenador con JDK 21 (núcleo Kotlin) o un Mac (núcleo Swift); un reloj Wear OS 3+ o un Apple Watch emparejado con el móvil (apps compiladas en CI, nunca ejecutadas)'],
                   ['En hardware real', 'Ninguno todavía: ningún reloj ni emulador lo ha ejecutado'],
                   ['Licencia', 'GPL-3.0-or-later']],
        'status': {'software': 'Los núcleos Kotlin y Swift leen y comprueban cada mensaje y guardan las alertas en memoria; la app de Wear OS, la app del Apple Watch y los emisores de las apps Android e iPhone están escritos.',
                   'tests': '{{fact:tests:ARMOR-WATCH}} pruebas de Python y las de Kotlin ejecutan los mismos ejemplos aceptados y rechazados del contrato; las de '
                            'Kotlin corren en CI.',
                   'hardware': 'Ningún reloj, emulador ni simulador las ha ejecutado; las apps solo se compilan y se prueban con pruebas unitarias en CI.',
                   'docs': 'Ocho idiomas, las notas del protocolo y el contrato están escritos y al día.'},
        'docs': ['[Notas del protocolo](docs/PROTOCOL.md): cómo hablan el móvil y el reloj',
                 '[Contrato de mensajes](docs/watch_alert_contract.json): los mensajes, los límites y los ejemplos aceptados y rechazados'],
        'contributing_first': 'Antes de un pull request ejecuta `python -m unittest discover -s tests` y `python -I tools/armor_ci_validate.py`: debe pasar. Mira '
                              '[CONTRIBUTING.md](CONTRIBUTING.md) y el [código de conducta](CODE_OF_CONDUCT.md).',
        'languages_extra': '',
        'body': {'overview': '* **Un reloj mínimo, no una segunda app.** ARMOR-ANDROID-CONTROL y ARMOR-IOS-CONTROL siguen siendo el cliente completo; el reloj solo '
                             'muestra las alarmas y avisos que el móvil elige enviar y deja confirmar una alarma con un toque.\n'
                             '* **El móvil es el único que habla con ARMOR-SERVER.** El reloj no guarda sesión, contraseña ni clave, y no guarda nada en el reloj: lo '
                             'que muestra está en memoria y se olvida al cerrar la app.\n'
                             '* **Apagado por defecto.** Nada llega al reloj hasta que la persona activa la opción de alertas del reloj en la app del móvil; mientras el '
                             'móvil no lo diga, el reloj descarta toda alerta que reciba.\n'
                             '* **Cuatro mensajes pequeños** (`relay`, `alert`, `alert_clear`, `alert_ack`) con límites y ejemplos aceptados y rechazados en '
                             '`docs/watch_alert_contract.json`; el móvil escribe los textos en el idioma de la persona, así que el reloj no tiene nada que traducir.\n'
                             '* **Sin sonido ni vibración propios:** el reloj no añade ninguno más allá de la notificación estándar del sistema.',
                 'role': 'ARMOR-WATCH es el extremo de muñeca de las apps del móvil. [ARMOR-ANDROID-CONTROL](https://github.com/JuanenRac/ARMOR-ANDROID-CONTROL) y '
                         '[ARMOR-IOS-CONTROL](https://github.com/JuanenRac/ARMOR-IOS-CONTROL) mantienen la sesión con '
                         '[ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER); el reloj recibe una alerta corta del móvil y devuelve el identificador de una '
                         'alarma que la persona confirmó, que el móvil comprueba y ejecuta.',
                 'architecture': '<p align="center">\n'
                                 '  <img src="images/architecture.svg" alt="ARMOR-WATCH architecture: the person, the Kotlin core and its contract, the phone app and '
                                 'the server" width="100%">\n'
                                 '</p>',
                 'security': '| Amenaza | Defensa |\n'
                             '|---|---|\n'
                             '| Un reloj que sigue mostrando alertas con la opción apagada | El móvil envía `relay` con `enabled: false` y el reloj olvida lo que '
                             'mostraba; la bandeja arranca apagada |\n'
                             '| Un mensaje falsificado o mal formado | Cada mensaje se comprueba contra el contrato (tipo, versión, límites, tipos exactos) y el que '
                             'falla se descarta sin error; no se lee nada de más de 4096 caracteres |\n'
                             '| Un reloj robado con una sesión dentro | No la hay: el reloj no guarda sesión, contraseña ni clave y no escribe nada en el almacenamiento '
                             '|\n'
                             '| Una confirmación enviada dos veces o de una alarma que no está | La confirmación sale una vez por alerta, solo si la alerta la pide y no '
                             'ha caducado; el móvil ignora un identificador que no conoce |\n'
                             '| La alarma de un PIN de coacción mostrada en la muñeca | El móvil no la envía nunca (igual que el aviso de las apps del móvil no la '
                             'muestra) |',
                 'configuration': '| Ajuste | Por defecto | Qué hace |\n'
                                  '|---|---|---|\n'
                                  '| `titleMax`, `textMax` | 60, 160 | Título y texto más largos de una alerta, en caracteres |\n'
                                  '| `ttlSeconds` | 5 - 600 | Cuánto dura una alerta antes de desaparecer sola |\n'
                                  '| `pendingMax` | 8 | Alertas guardadas a la vez; una crítica nunca se descarta por una menor |\n'
                                  '| `rawMax` | 4096 | Un mensaje más largo no se lee |\n'
                                  '| `relay.enabled` | false | Lo fija el móvil; el reloj no muestra nada hasta que es verdadero |',
                 'quickstart': '**Requisitos:** Python 3.11+ para las comprobaciones; un JDK 21 para el núcleo Kotlin (el wrapper de Gradle descarga el propio Gradle).\n'
                               '\n'
                               '```powershell\n'
                               'python tools/watch_contract.py                  # the examples of the contract in Python\n'
                               'python -m unittest discover -s tests            # the contract, the Kotlin constants and the protocol notes\n'
                               './gradlew test                                  # the Kotlin core (WatchProtocol and AlertInbox)\n'
                               '```\n'
                               '\n'
                               'Mira las [notas del protocolo](docs/PROTOCOL.md) para los mensajes y lo que hace cada lado.',
                 'testing': '```powershell\n'
                            'python -m unittest discover -s tests\n'
                            './gradlew test\n'
                            'python -I tools/armor_ci_validate.py\n'
                            '```\n'
                            '\n'
                            '| Fichero de pruebas | Pruebas | Qué cubre |\n'
                            '|---|---|---|\n'
                            '| `test_watch_contract.py` | 10 | Cada ejemplo del contrato, los límites, las constantes de Kotlin y las notas del protocolo |\n'
                            '| `WatchProtocolTest.kt` | 6 | Los mismos ejemplos contra el lector Kotlin, los límites y la confirmación |\n'
                            '| `AlertInboxTest.kt` | 10 | Apagado por defecto, orden, sustitución, caducidad, borrado, una sola confirmación, el límite de ocho |\n'
                            '\n'
                            'Las pruebas de Kotlin corren en CI; ninguna prueba ha corrido en un reloj ni en un emulador.',
                 'troubleshooting': '| Ves | Porque | Haz |\n'
                                    '|---|---|---|\n'
                                    '| No aparece nada en el reloj | La opción de alertas del reloj está apagada en la app del móvil, o el móvil no ha enviado `relay` '
                                    'con `enabled: true` | Activa la opción en la app del móvil |\n'
                                    '| Una alerta desaparece sola | Se acabó su `ttlSeconds` o el móvil la borró | Vuelve a lanzarla desde el móvil |\n'
                                    '| La confirmación no hace nada | La alerta no la pide, caducó o ya se confirmó una vez | Confirma la alarma en la app del móvil |',
                 'structure': '<p align="center">\n'
                              '  <img src="images/repository-structure.svg" alt="Repository structure of ARMOR-WATCH" width="100%">\n'
                              '</p>\n'
                              '\n'
                              '<details>\n'
                              '<summary>Versión en texto del árbol</summary>\n'
                              '\n'
                              '```text\n'
                              'ARMOR-WATCH/\n'
                              '├── src/\n'
                              '│   ├── main/                               WatchProtocol (los mensajes y sus comprobaciones) y AlertInbox (las alertas en pantalla)\n'
                              '│   └── test/                               los mismos ejemplos que el contrato y las reglas de la bandeja\n'
                              '├── wear/                               la app de Wear OS: pantalla, servicio del Data Layer y runtime\n'
                              '├── watchos/                            la app del Apple Watch: núcleo Swift, pantalla y WatchConnectivity\n'
                              '├── tests/                                  el contrato comprobado en Python\n'
                              '├── docs/                                   el contrato y el protocolo\n'
                              '├── tools/                                  comprobaciones y contrato\n'
                              '├── gradle/                                 wrapper de Gradle\n'
                              '├── .github/                                flujo de CI y plantillas de issues y pull requests\n'
                              '├── images/                                 banner, icono y los dos dibujos del README\n'
                              '├── armor.project.json                      manifiesto: versión, rol, madurez, comando de build\n'
                              '├── CHANGELOG.md                            qué cambió en cada versión\n'
                              '├── SECURITY.md SUPPORT.md LICENSE          política de seguridad, soporte y licencia\n'
                              '├── CONTRIBUTING.md CODE_OF_CONDUCT.md      cómo contribuir y el código de conducta\n'
                              '├── build.gradle.kts settings.gradle.kts    el build de Kotlin\n'
                              '├── gradle.properties gradlew gradlew.bat   ajustes de Gradle y scripts del wrapper\n'
                              '└── .gitattributes .gitignore               ajustes de Git\n'
                              '```\n'
                              '\n'
                              '</details>',
                 'roadmap': '**Límites conocidos hoy**\n\n* La app de Wear OS (`wear/`, se compila con `-ParmorWear`), la app del Apple Watch (`watchos/`, solo se compila en un Mac) y los emisores de ARMOR-ANDROID-CONTROL y ARMOR-IOS-CONTROL (apagados por defecto) se compilan y pasan sus pruebas en CI, pero nada ha corrido en un reloj real, un emulador ni un simulador.\n* La app del Apple Watch aún no está dentro de la app del iPhone, así que el emparejamiento de las dos está por probar; un iPhone no se empareja con un reloj Wear OS ni un móvil Android con un Apple Watch.\n* El contrato vive aquí; el núcleo Kotlin, el núcleo Swift y las apps del móvil ejecutan los mismos ejemplos.\n\n**Siguiente**\n\n* Probarlo en un reloj real de cada tipo: emparejarlo, activar la opción, lanzar una alarma de prueba, verla en el reloj, confirmarla con un toque y ver la confirmación en ARMOR-SERVER; después apagar la opción y ver desaparecer el aviso.'}},
 'de': {'tagline': 'Die minimale A.R.M.O.R.-Uhr: Alarmmeldungen und ein Tipp zum Bestätigen eines Alarms',
        'honest': 'Der Nachrichtenvertrag, die Kotlin- und Swift-Kerne und die Uhr-Sitzung werden auf einem Computer getestet, und die Wear-OS-App, die Apple-Watch-App und die Sendeseite der Android- und iPhone-Apps werden in CI gebaut und bestehen ihre Tests; **nichts lief auf einer echten Uhr, einem Emulator oder einem Simulator, und die Apple-Watch-App ist noch nicht in der iPhone-App.**',
        'glance': [['Rolle', 'Der minimale Uhren-Client von A.R.M.O.R. (Familie: Clients, Eltern: ARMOR-ANDROID-CONTROL)'],
                   ['Stack', 'Kotlin (JVM-Kern und die Wear-OS-App mit Compose, Gradle), Swift (Kern und die Apple-Watch-App mit SwiftUI); Python 3.11+ für die Prüfungen'],
                   ['Tests', '{{fact:tests:ARMOR-WATCH}} in Python (`python -m unittest discover -s tests`) und die Kotlin-Tests (`./gradlew test`)'],
                   ['Nachrichten', 'Der Schalter des Relays, ein Alarm, das Löschen eines Alarms und die Bestätigung zurück'],
                   ['Läuft auf', 'Jedem Computer mit JDK 21 (Kotlin-Kern) oder einem Mac (Swift-Kern); einer Wear-OS-3+-Uhr oder einer Apple Watch, gekoppelt mit dem Telefon (Apps in CI gebaut, nie ausgeführt)'],
                   ['Auf echter Hardware', 'Noch nicht: keine Uhr und kein Emulator hat es ausgeführt'],
                   ['Lizenz', 'GPL-3.0-or-later']],
        'status': {'software': 'Die Kotlin- und Swift-Kerne lesen und prüfen jede Nachricht und halten die Alarme im Speicher; die Wear-OS-App, die Apple-Watch-App und die Sender in den Android- und iPhone-Apps sind geschrieben.',
                   'tests': '{{fact:tests:ARMOR-WATCH}} Python-Tests und die Kotlin-Tests führen dieselben angenommenen und abgelehnten Beispiele des Vertrags aus; die '
                            'Kotlin-Tests laufen in der CI.',
                   'hardware': 'Keine Uhr, kein Emulator und kein Simulator hat sie ausgeführt; die Apps werden nur in CI gebaut und per Unit-Test geprüft.',
                   'docs': 'Acht Sprachen, die Protokollnotizen und der Vertrag sind geschrieben und aktuell.'},
        'docs': ['[Protokollnotizen](docs/PROTOCOL.md): wie Telefon und Uhr miteinander sprechen',
                 '[Nachrichtenvertrag](docs/watch_alert_contract.json): die Nachrichten, die Grenzen und die angenommenen und abgelehnten Beispiele'],
        'contributing_first': 'Führe vor einem Pull Request `python -m unittest discover -s tests` und `python -I tools/armor_ci_validate.py` aus: Es muss bestehen. '
                              'Siehe [CONTRIBUTING.md](CONTRIBUTING.md) und den [Verhaltenskodex](CODE_OF_CONDUCT.md).',
        'languages_extra': '',
        'body': {'overview': '* **Eine minimale Uhr, keine zweite App.** ARMOR-ANDROID-CONTROL und ARMOR-IOS-CONTROL bleiben der vollständige Client; die Uhr zeigt nur '
                             'die Alarme und Hinweise, die das Telefon senden will, und lässt einen Alarm mit einem Tipp bestätigen.\n'
                             '* **Nur das Telefon spricht mit ARMOR-SERVER.** Die Uhr hält keine Sitzung, kein Passwort und keinen Schlüssel und speichert nichts auf '
                             'der Uhr: Was sie zeigt, liegt im Speicher und wird beim Schließen der App vergessen.\n'
                             '* **Standardmäßig aus.** Nichts erreicht die Uhr, bis die Person die Option der Uhr-Alarme in der Telefon-App einschaltet; solange das '
                             'Telefon es nicht sagt, verwirft die Uhr jeden empfangenen Alarm.\n'
                             '* **Vier kleine Nachrichten** (`relay`, `alert`, `alert_clear`, `alert_ack`) mit Grenzen sowie angenommenen und abgelehnten Beispielen in '
                             '`docs/watch_alert_contract.json`; das Telefon schreibt die Texte in der Sprache der Person, die Uhr muss nichts übersetzen.\n'
                             '* **Kein eigener Ton und keine eigene Vibration:** Die Uhr fügt über die Standardbenachrichtigung des Systems hinaus nichts hinzu.',
                 'role': 'ARMOR-WATCH ist das Handgelenk-Ende der Telefon-Apps. [ARMOR-ANDROID-CONTROL](https://github.com/JuanenRac/ARMOR-ANDROID-CONTROL) und '
                         '[ARMOR-IOS-CONTROL](https://github.com/JuanenRac/ARMOR-IOS-CONTROL) halten die Sitzung mit '
                         '[ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER); die Uhr empfängt vom Telefon einen kurzen Alarm und sendet die Kennung eines '
                         'bestätigten Alarms zurück, die das Telefon prüft und ausführt.',
                 'architecture': '<p align="center">\n'
                                 '  <img src="images/architecture.svg" alt="ARMOR-WATCH architecture: the person, the Kotlin core and its contract, the phone app and '
                                 'the server" width="100%">\n'
                                 '</p>',
                 'security': '| Bedrohung | Abwehr |\n'
                             '|---|---|\n'
                             '| Eine Uhr, die nach dem Ausschalten der Option noch Alarme zeigt | Das Telefon sendet `relay` mit `enabled: false` und die Uhr vergisst, '
                             'was sie zeigte; der Posteingang startet ausgeschaltet |\n'
                             '| Eine gefälschte oder fehlerhafte Nachricht | Jede Nachricht wird gegen den Vertrag geprüft (Typ, Version, Grenzen, genaue Typen) und '
                             'eine, die durchfällt, wird ohne Fehler verworfen; über 4096 Zeichen wird nichts gelesen |\n'
                             '| Eine gestohlene Uhr mit einer Sitzung darauf | Es gibt keine: Die Uhr hält weder Sitzung noch Passwort oder Schlüssel und schreibt '
                             'nichts in den Speicher |\n'
                             '| Eine doppelt gesendete Bestätigung oder für einen nicht vorhandenen Alarm | Die Bestätigung geht einmal pro Alarm hinaus, nur für einen '
                             'Alarm, der sie verlangt und nicht abgelaufen ist; das Telefon ignoriert eine unbekannte Kennung |\n'
                             '| Der Alarm einer Zwangs-PIN am Handgelenk | Das Telefon sendet ihn nie (wie das Banner der Telefon-Apps ihn nie zeigt) |',
                 'configuration': '| Einstellung | Standard | Was sie tut |\n'
                                  '|---|---|---|\n'
                                  '| `titleMax`, `textMax` | 60, 160 | Längster Titel und Text eines Alarms in Zeichen |\n'
                                  '| `ttlSeconds` | 5 - 600 | Wie lange ein Alarm bleibt, bevor er von selbst verschwindet |\n'
                                  '| `pendingMax` | 8 | Gleichzeitig gehaltene Alarme; ein kritischer wird nie für einen geringeren verworfen |\n'
                                  '| `rawMax` | 4096 | Eine längere Nachricht wird nicht gelesen |\n'
                                  '| `relay.enabled` | false | Vom Telefon gesetzt; die Uhr zeigt nichts, bis er wahr ist |',
                 'quickstart': '**Voraussetzungen:** Python 3.11+ für die Prüfungen; ein JDK 21 für den Kotlin-Kern (der Gradle-Wrapper lädt Gradle selbst herunter).\n'
                               '\n'
                               '```powershell\n'
                               'python tools/watch_contract.py                  # the examples of the contract in Python\n'
                               'python -m unittest discover -s tests            # the contract, the Kotlin constants and the protocol notes\n'
                               './gradlew test                                  # the Kotlin core (WatchProtocol and AlertInbox)\n'
                               '```\n'
                               '\n'
                               'Die Nachrichten und was jede Seite tut, stehen in den [Protokollnotizen](docs/PROTOCOL.md).',
                 'testing': '```powershell\n'
                            'python -m unittest discover -s tests\n'
                            './gradlew test\n'
                            'python -I tools/armor_ci_validate.py\n'
                            '```\n'
                            '\n'
                            '| Testdatei | Tests | Was sie abdeckt |\n'
                            '|---|---|---|\n'
                            '| `test_watch_contract.py` | 10 | Jedes Beispiel des Vertrags, die Grenzen, die Kotlin-Konstanten und die Protokollnotizen |\n'
                            '| `WatchProtocolTest.kt` | 6 | Dieselben Beispiele gegen den Kotlin-Parser, die Grenzen und die Bestätigung |\n'
                            '| `AlertInboxTest.kt` | 10 | Standardmäßig aus, Reihenfolge, Ersetzen, Ablauf, Löschen, eine Bestätigung, das Limit von acht |\n'
                            '\n'
                            'Die Kotlin-Tests laufen in der CI; kein Test lief auf einer Uhr oder einem Emulator.',
                 'troubleshooting': '| Du siehst | Weil | Tu |\n'
                                    '|---|---|---|\n'
                                    '| Auf der Uhr erscheint nichts | Die Option der Uhr-Alarme ist in der Telefon-App aus, oder das Telefon hat kein `relay` mit '
                                    '`enabled: true` gesendet | Schalte die Option in der Telefon-App ein |\n'
                                    '| Ein Alarm verschwindet von selbst | Sein `ttlSeconds` ist abgelaufen oder das Telefon hat ihn gelöscht | Löse ihn vom Telefon aus '
                                    'erneut aus |\n'
                                    '| Die Bestätigung bewirkt nichts | Der Alarm verlangt keine, er ist abgelaufen oder wurde schon einmal bestätigt | Bestätige den '
                                    'Alarm in der Telefon-App |',
                 'structure': '<p align="center">\n'
                              '  <img src="images/repository-structure.svg" alt="Repository structure of ARMOR-WATCH" width="100%">\n'
                              '</p>\n'
                              '\n'
                              '<details>\n'
                              '<summary>Textversion des Baums</summary>\n'
                              '\n'
                              '```text\n'
                              'ARMOR-WATCH/\n'
                              '├── src/\n'
                              '│   ├── main/                               WatchProtocol (die Nachrichten und ihre Prüfungen) und AlertInbox (die Alarme auf dem '
                              'Bildschirm)\n'
                              '│   └── test/                               dieselben Beispiele wie der Vertrag und die Regeln des Posteingangs\n'
                              '├── wear/                               die Wear-OS-App: Bildschirm, Data-Layer-Dienst und Laufzeit\n'
                              '├── watchos/                            die Apple-Watch-App: Swift-Kern, Bildschirm und WatchConnectivity\n'
                              '├── tests/                                  der Vertrag in Python geprüft\n'
                              '├── docs/                                   der Vertrag und das Protokoll\n'
                              '├── tools/                                  Prüfungen, Vertrag\n'
                              '├── gradle/                                 Gradle-Wrapper\n'
                              '├── .github/                                CI-Workflow sowie Vorlagen für Issues und Pull Requests\n'
                              '├── images/                                 Banner, Symbol und die zwei Bilder des READMEs\n'
                              '├── armor.project.json                      Manifest: Version, Rolle, Reifegrad, Build-Befehl\n'
                              '├── CHANGELOG.md                            was sich in jeder Version geändert hat\n'
                              '├── SECURITY.md SUPPORT.md LICENSE          Sicherheitsrichtlinie, Support und Lizenz\n'
                              '├── CONTRIBUTING.md CODE_OF_CONDUCT.md      wie man beiträgt und der Verhaltenskodex\n'
                              '├── build.gradle.kts settings.gradle.kts    der Kotlin-Build\n'
                              '├── gradle.properties gradlew gradlew.bat   Gradle-Einstellungen und Wrapper-Skripte\n'
                              '└── .gitattributes .gitignore               Git-Einstellungen\n'
                              '```\n'
                              '\n'
                              '</details>',
                 'roadmap': '**Bekannte Grenzen heute**\n\n* Die Wear-OS-App (`wear/`, gebaut mit `-ParmorWear`), die Apple-Watch-App (`watchos/`, nur auf einem Mac gebaut) und die Sender in ARMOR-ANDROID-CONTROL und ARMOR-IOS-CONTROL (standardmäßig aus) werden in CI gebaut und bestehen ihre Unit-Tests, aber nichts lief auf einer echten Uhr, einem Emulator oder einem Simulator.\n* Die Apple-Watch-App ist noch nicht in der iPhone-App, die Kopplung beider ist also noch zu prüfen; ein iPhone koppelt nicht mit einer Wear-OS-Uhr und ein Android-Telefon nicht mit einer Apple Watch.\n* Der Vertrag liegt hier; der Kotlin-Kern, der Swift-Kern und die Telefon-Apps führen dieselben Beispiele aus.\n\n**Als Nächstes**\n\n* Auf einer echten Uhr jeder Art beweisen: koppeln, die Option einschalten, einen Testalarm auslösen, ihn auf der Uhr sehen, mit einem Tipp bestätigen und die Bestätigung in ARMOR-SERVER sehen; dann die Option ausschalten und die Meldung verschwinden sehen.'}},
 'fr': {'tagline': "La montre minimale d'A.R.M.O.R. : avis d'alarme et un toucher pour confirmer une alarme",
        'honest': "Le contrat des messages, les noyaux Kotlin et Swift et la session de la montre sont testés sur un ordinateur, et l'app Wear OS, l'app Apple Watch et le côté émetteur des apps Android et iPhone se compilent et passent leurs tests en CI ; **rien n'a tourné sur une vraie montre, un émulateur ou un simulateur, et l'app Apple Watch n'est pas encore dans l'app iPhone.**",
        'glance': [['Rôle', "Le client montre minimal d'A.R.M.O.R. (famille : Clients, parent : ARMOR-ANDROID-CONTROL)"],
                   ['Stack', "Kotlin (noyau JVM et l'app Wear OS avec Compose, Gradle), Swift (noyau et l'app Apple Watch avec SwiftUI) ; Python 3.11+ pour les vérifications"],
                   ['Tests', '{{fact:tests:ARMOR-WATCH}} en Python (`python -m unittest discover -s tests`) et les tests Kotlin (`./gradlew test`)'],
                   ['Messages', "L'interrupteur du relais, une alerte, l'effacement d'une alerte et la confirmation en retour"],
                   ['Fonctionne sur', 'Tout ordinateur avec un JDK 21 (noyau Kotlin) ou un Mac (noyau Swift) ; une montre Wear OS 3+ ou une Apple Watch appairée au téléphone (apps compilées en CI, jamais exécutées)'],
                   ['Sur matériel réel', "Aucun pour l'instant : aucune montre ni émulateur ne l'a exécuté"],
                   ['Licence', 'GPL-3.0-or-later']],
        'status': {'software': "Les noyaux Kotlin et Swift lisent et vérifient chaque message et gardent les alertes en mémoire ; l'app Wear OS, l'app Apple Watch et les émetteurs des apps Android et iPhone sont écrits.",
                   'tests': '{{fact:tests:ARMOR-WATCH}} tests Python et les tests Kotlin exécutent les mêmes exemples acceptés et refusés du contrat ; les tests Kotlin '
                            'tournent en CI.',
                   'hardware': 'Aucune montre, aucun émulateur ni simulateur ne les a exécutées ; les apps sont seulement compilées et testées unitairement en CI.',
                   'docs': 'Huit langues, les notes du protocole et le contrat sont écrits et à jour.'},
        'docs': ['[Notes du protocole](docs/PROTOCOL.md) : comment le téléphone et la montre se parlent',
                 '[Contrat des messages](docs/watch_alert_contract.json) : les messages, les limites et les exemples acceptés et refusés'],
        'contributing_first': 'Avant une pull request, lance `python -m unittest discover -s tests` et `python -I tools/armor_ci_validate.py` : cela doit passer. Voir '
                              '[CONTRIBUTING.md](CONTRIBUTING.md) et le [code de conduite](CODE_OF_CONDUCT.md).',
        'languages_extra': '',
        'body': {'overview': '* **Une montre minimale, pas une seconde app.** ARMOR-ANDROID-CONTROL et ARMOR-IOS-CONTROL restent le client complet ; la montre montre '
                             "seulement les alarmes et avis que le téléphone choisit d'envoyer et laisse confirmer une alarme d'un toucher.\n"
                             '* **Seul le téléphone parle à ARMOR-SERVER.** La montre ne détient ni session, ni mot de passe, ni clé, et ne garde rien sur la montre : '
                             "ce qu'elle montre est en mémoire et s'oublie à la fermeture de l'app.\n"
                             "* **Désactivé par défaut.** Rien n'arrive sur la montre tant que la personne n'active pas l'option des alertes de la montre dans l'app du "
                             'téléphone ; tant que le téléphone ne le dit pas, la montre jette toute alerte reçue.\n'
                             '* **Quatre petits messages** (`relay`, `alert`, `alert_clear`, `alert_ack`) avec limites et exemples acceptés et refusés dans '
                             "`docs/watch_alert_contract.json` ; le téléphone écrit les textes dans la langue de la personne, la montre n'a rien à traduire.\n"
                             "* **Aucun son ni vibration propres :** la montre n'en ajoute pas au-delà de la notification standard du système.",
                 'role': 'ARMOR-WATCH est le bout du poignet des apps du téléphone. [ARMOR-ANDROID-CONTROL](https://github.com/JuanenRac/ARMOR-ANDROID-CONTROL) et '
                         '[ARMOR-IOS-CONTROL](https://github.com/JuanenRac/ARMOR-IOS-CONTROL) gardent la session avec '
                         "[ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER) ; la montre reçoit une courte alerte du téléphone et renvoie l'identifiant d'une "
                         'alarme confirmée par la personne, que le téléphone vérifie et exécute.',
                 'architecture': '<p align="center">\n'
                                 '  <img src="images/architecture.svg" alt="ARMOR-WATCH architecture: the person, the Kotlin core and its contract, the phone app and '
                                 'the server" width="100%">\n'
                                 '</p>',
                 'security': '| Menace | Défense |\n'
                             '|---|---|\n'
                             "| Une montre qui montre encore des alertes après désactivation de l'option | Le téléphone envoie `relay` avec `enabled: false` et la "
                             "montre oublie ce qu'elle montrait ; la boîte démarre désactivée |\n"
                             '| Un message falsifié ou mal formé | Chaque message est vérifié contre le contrat (type, version, limites, types exacts) et celui qui '
                             "échoue est jeté sans erreur ; rien de plus de 4096 caractères n'est lu |\n"
                             "| Une montre volée avec une session dedans | Il n'y en a pas : la montre ne détient ni session, ni mot de passe, ni clé et n'écrit rien "
                             'dans le stockage |\n'
                             '| Une confirmation envoyée deux fois ou pour une alarme absente | La confirmation part une fois par alerte, seulement pour une alerte qui '
                             "la demande et n'a pas expiré ; le téléphone ignore un identifiant inconnu |\n"
                             "| L'alarme d'un PIN de contrainte affichée au poignet | Le téléphone ne l'envoie jamais (comme la bannière des apps du téléphone ne "
                             "l'affiche jamais) |",
                 'configuration': "| Réglage | Par défaut | Ce qu'il fait |\n"
                                  '|---|---|---|\n'
                                  "| `titleMax`, `textMax` | 60, 160 | Titre et texte les plus longs d'une alerte, en caractères |\n"
                                  "| `ttlSeconds` | 5 - 600 | Combien de temps une alerte reste avant de disparaître d'elle-même |\n"
                                  "| `pendingMax` | 8 | Alertes gardées à la fois ; une critique n'est jamais jetée pour une moindre |\n"
                                  "| `rawMax` | 4096 | Un message plus long n'est pas lu |\n"
                                  "| `relay.enabled` | false | Fixé par le téléphone ; la montre ne montre rien tant qu'il n'est pas vrai |",
                 'quickstart': '**Prérequis :** Python 3.11+ pour les vérifications ; un JDK 21 pour le noyau Kotlin (le wrapper Gradle télécharge Gradle lui-même).\n'
                               '\n'
                               '```powershell\n'
                               'python tools/watch_contract.py                  # the examples of the contract in Python\n'
                               'python -m unittest discover -s tests            # the contract, the Kotlin constants and the protocol notes\n'
                               './gradlew test                                  # the Kotlin core (WatchProtocol and AlertInbox)\n'
                               '```\n'
                               '\n'
                               'Voir les [notes du protocole](docs/PROTOCOL.md) pour les messages et ce que fait chaque côté.',
                 'testing': '```powershell\n'
                            'python -m unittest discover -s tests\n'
                            './gradlew test\n'
                            'python -I tools/armor_ci_validate.py\n'
                            '```\n'
                            '\n'
                            "| Fichier de tests | Tests | Ce qu'il couvre |\n"
                            '|---|---|---|\n'
                            '| `test_watch_contract.py` | 10 | Chaque exemple du contrat, les limites, les constantes Kotlin et les notes du protocole |\n'
                            '| `WatchProtocolTest.kt` | 6 | Les mêmes exemples contre le lecteur Kotlin, les limites et la confirmation |\n'
                            '| `AlertInboxTest.kt` | 10 | Désactivé par défaut, ordre, remplacement, expiration, effacement, une seule confirmation, la limite de huit '
                            '|\n'
                            '\n'
                            "Les tests Kotlin tournent en CI ; aucun test n'a tourné sur une montre ni sur un émulateur.",
                 'troubleshooting': '| Vous voyez | Parce que | Faites |\n'
                                    '|---|---|---|\n'
                                    "| Rien n'apparaît sur la montre | L'option des alertes de la montre est désactivée dans l'app du téléphone, ou le téléphone n'a pas "
                                    "envoyé `relay` avec `enabled: true` | Active l'option dans l'app du téléphone |\n"
                                    "| Une alerte disparaît d'elle-même | Son `ttlSeconds` est écoulé ou le téléphone l'a effacée | Relance-la depuis le téléphone |\n"
                                    "| La confirmation ne fait rien | L'alerte n'en demande pas, elle a expiré ou a déjà été confirmée une fois | Confirme l'alarme dans "
                                    "l'app du téléphone |",
                 'structure': '<p align="center">\n'
                              '  <img src="images/repository-structure.svg" alt="Repository structure of ARMOR-WATCH" width="100%">\n'
                              '</p>\n'
                              '\n'
                              '<details>\n'
                              "<summary>Version texte de l'arborescence</summary>\n"
                              '\n'
                              '```text\n'
                              'ARMOR-WATCH/\n'
                              '├── src/\n'
                              "│   ├── main/                               WatchProtocol (les messages et leurs contrôles) et AlertInbox (les alertes à l'écran)\n"
                              '│   └── test/                               les mêmes exemples que le contrat et les règles de la boîte\n'
                              '├── wear/                               l\'app Wear OS : écran, service Data Layer et runtime\n'
                              '├── watchos/                            l\'app Apple Watch : noyau Swift, écran et WatchConnectivity\n'
                              '├── tests/                                  le contrat vérifié en Python\n'
                              '├── docs/                                   le contrat et le protocole\n'
                              '├── tools/                                  contrôles et contrat\n'
                              '├── gradle/                                 wrapper Gradle\n'
                              "├── .github/                                workflow CI et modèles d'issues et de pull requests\n"
                              '├── images/                                 bannière, icône et les deux images du README\n'
                              '├── armor.project.json                      manifeste : version, rôle, maturité, commande de build\n'
                              '├── CHANGELOG.md                            ce qui a changé à chaque version\n'
                              '├── SECURITY.md SUPPORT.md LICENSE          politique de sécurité, support et licence\n'
                              '├── CONTRIBUTING.md CODE_OF_CONDUCT.md      comment contribuer et le code de conduite\n'
                              '├── build.gradle.kts settings.gradle.kts    le build Kotlin\n'
                              '├── gradle.properties gradlew gradlew.bat   réglages Gradle et scripts du wrapper\n'
                              '└── .gitattributes .gitignore               réglages de Git\n'
                              '```\n'
                              '\n'
                              '</details>',
                 'roadmap': "**Limites connues aujourd'hui**\n\n* L'app Wear OS (`wear/`, compilée avec `-ParmorWear`), l'app Apple Watch (`watchos/`, compilée seulement sur un Mac) et les émetteurs d'ARMOR-ANDROID-CONTROL et d'ARMOR-IOS-CONTROL (désactivés par défaut) se compilent et passent leurs tests en CI, mais rien n'a tourné sur une vraie montre, un émulateur ou un simulateur.\n* L'app Apple Watch n'est pas encore dans l'app iPhone : l'appairage des deux reste à essayer ; un iPhone ne s'appaire pas avec une montre Wear OS ni un téléphone Android avec une Apple Watch.\n* Le contrat est conservé ici ; le noyau Kotlin, le noyau Swift et les apps du téléphone exécutent les mêmes exemples.\n\n**Ensuite**\n\n* Le prouver sur une vraie montre de chaque type : l'appairer, activer l'option, lancer une alarme d'essai, la voir sur la montre, la confirmer d'un toucher et voir la confirmation dans ARMOR-SERVER ; puis désactiver l'option et voir l'alerte disparaître."}},
 'it': {'tagline': "L'orologio minimale di A.R.M.O.R.: avvisi di allarme e un tocco per confermare un allarme",
        'honest': "Il contratto dei messaggi, i nuclei Kotlin e Swift e la sessione dell'orologio sono testati su un computer, e l'app Wear OS, l'app Apple Watch e il lato che invia delle app Android e iPhone si compilano e superano i test in CI; **nulla è stato eseguito su un orologio reale, un emulatore o un simulatore, e l'app Apple Watch non è ancora dentro l'app iPhone.**",
        'glance': [['Ruolo', 'Il client orologio minimale di A.R.M.O.R. (famiglia: Clients, genitore: ARMOR-ANDROID-CONTROL)'],
                   ['Stack', 'Kotlin (nucleo JVM e app Wear OS con Compose, Gradle), Swift (nucleo e app Apple Watch con SwiftUI); Python 3.11+ per i controlli'],
                   ['Test', '{{fact:tests:ARMOR-WATCH}} in Python (`python -m unittest discover -s tests`) e i test Kotlin (`./gradlew test`)'],
                   ['Messaggi', "L'interruttore del relay, un avviso, la cancellazione di un avviso e la conferma di ritorno"],
                   ['Funziona su', 'Qualsiasi computer con JDK 21 (nucleo Kotlin) o un Mac (nucleo Swift); un orologio Wear OS 3+ o un Apple Watch associato al telefono (app compilate in CI, mai eseguite)'],
                   ['Su hardware reale', "Ancora nessuno: nessun orologio o emulatore l'ha eseguito"],
                   ['Licenza', 'GPL-3.0-or-later']],
        'status': {'software': "I nuclei Kotlin e Swift leggono e controllano ogni messaggio e tengono gli avvisi in memoria; l'app Wear OS, l'app Apple Watch e i mittenti delle app Android e iPhone sono scritti.",
                   'tests': '{{fact:tests:ARMOR-WATCH}} test Python e i test Kotlin eseguono gli stessi esempi accettati e rifiutati del contratto; i test Kotlin girano '
                            'in CI.',
                   'hardware': 'Nessun orologio, emulatore o simulatore le ha eseguite; le app sono solo compilate e provate con test unitari in CI.',
                   'docs': 'Otto lingue, le note del protocollo e il contratto sono scritti e aggiornati.'},
        'docs': ['[Note del protocollo](docs/PROTOCOL.md): come parlano telefono e orologio',
                 '[Contratto dei messaggi](docs/watch_alert_contract.json): i messaggi, i limiti e gli esempi accettati e rifiutati'],
        'contributing_first': 'Prima di una pull request esegui `python -m unittest discover -s tests` e `python -I tools/armor_ci_validate.py`: deve passare. Vedi '
                              '[CONTRIBUTING.md](CONTRIBUTING.md) e il [codice di condotta](CODE_OF_CONDUCT.md).',
        'languages_extra': '',
        'body': {'overview': "* **Un orologio minimale, non una seconda app.** ARMOR-ANDROID-CONTROL e ARMOR-IOS-CONTROL restano il client completo; l'orologio mostra "
                             'solo gli allarmi e gli avvisi che il telefono sceglie di inviare e permette di confermare un allarme con un tocco.\n'
                             "* **Solo il telefono parla con ARMOR-SERVER.** L'orologio non ha sessione, password né chiave e non conserva nulla sull'orologio: ciò che "
                             "mostra è in memoria e si dimentica alla chiusura dell'app.\n"
                             "* **Spento per impostazione predefinita.** Nulla arriva all'orologio finché la persona non attiva l'opzione degli avvisi dell'orologio "
                             "nell'app del telefono; finché il telefono non lo dice, l'orologio scarta ogni avviso ricevuto.\n"
                             '* **Quattro piccoli messaggi** (`relay`, `alert`, `alert_clear`, `alert_ack`) con limiti ed esempi accettati e rifiutati in '
                             "`docs/watch_alert_contract.json`; il telefono scrive i testi nella lingua della persona, l'orologio non ha nulla da tradurre.\n"
                             "* **Nessun suono o vibrazione propri:** l'orologio non ne aggiunge oltre alla notifica standard del sistema.",
                 'role': "ARMOR-WATCH è l'estremità al polso delle app del telefono. [ARMOR-ANDROID-CONTROL](https://github.com/JuanenRac/ARMOR-ANDROID-CONTROL) e "
                         '[ARMOR-IOS-CONTROL](https://github.com/JuanenRac/ARMOR-IOS-CONTROL) mantengono la sessione con '
                         "[ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER); l'orologio riceve un breve avviso dal telefono e restituisce l'identificatore di un "
                         'allarme confermato dalla persona, che il telefono controlla ed esegue.',
                 'architecture': '<p align="center">\n'
                                 '  <img src="images/architecture.svg" alt="ARMOR-WATCH architecture: the person, the Kotlin core and its contract, the phone app and '
                                 'the server" width="100%">\n'
                                 '</p>',
                 'security': '| Minaccia | Difesa |\n'
                             '|---|---|\n'
                             "| Un orologio che mostra ancora avvisi dopo aver spento l'opzione | Il telefono invia `relay` con `enabled: false` e l'orologio dimentica "
                             'ciò che mostrava; la casella parte spenta |\n'
                             '| Un messaggio falsificato o malformato | Ogni messaggio è controllato contro il contratto (tipo, versione, limiti, tipi esatti) e quello '
                             'che fallisce viene scartato senza errore; non si legge nulla oltre 4096 caratteri |\n'
                             "| Un orologio rubato con una sessione dentro | Non c'è: l'orologio non ha sessione, password né chiave e non scrive nulla nella memoria |\n"
                             '| Una conferma inviata due volte o per un allarme inesistente | La conferma parte una volta per avviso, solo per un avviso che la chiede e '
                             'non è scaduto; il telefono ignora un identificatore sconosciuto |\n'
                             "| L'allarme di un PIN di coercizione mostrato al polso | Il telefono non lo invia mai (come il banner delle app del telefono non lo mostra "
                             'mai) |',
                 'configuration': '| Impostazione | Predefinito | Cosa fa |\n'
                                  '|---|---|---|\n'
                                  '| `titleMax`, `textMax` | 60, 160 | Titolo e testo più lunghi di un avviso, in caratteri |\n'
                                  '| `ttlSeconds` | 5 - 600 | Quanto resta un avviso prima di sparire da solo |\n'
                                  '| `pendingMax` | 8 | Avvisi tenuti insieme; uno critico non viene mai scartato per uno minore |\n'
                                  '| `rawMax` | 4096 | Un messaggio più lungo non viene letto |\n'
                                  "| `relay.enabled` | false | Impostato dal telefono; l'orologio non mostra nulla finché non è vero |",
                 'quickstart': '**Requisiti:** Python 3.11+ per i controlli; un JDK 21 per il nucleo Kotlin (il wrapper di Gradle scarica Gradle stesso).\n'
                               '\n'
                               '```powershell\n'
                               'python tools/watch_contract.py                  # the examples of the contract in Python\n'
                               'python -m unittest discover -s tests            # the contract, the Kotlin constants and the protocol notes\n'
                               './gradlew test                                  # the Kotlin core (WatchProtocol and AlertInbox)\n'
                               '```\n'
                               '\n'
                               'Vedi le [note del protocollo](docs/PROTOCOL.md) per i messaggi e cosa fa ogni lato.',
                 'testing': '```powershell\n'
                            'python -m unittest discover -s tests\n'
                            './gradlew test\n'
                            'python -I tools/armor_ci_validate.py\n'
                            '```\n'
                            '\n'
                            '| File di test | Test | Cosa copre |\n'
                            '|---|---|---|\n'
                            '| `test_watch_contract.py` | 10 | Ogni esempio del contratto, i limiti, le costanti Kotlin e le note del protocollo |\n'
                            '| `WatchProtocolTest.kt` | 6 | Gli stessi esempi contro il parser Kotlin, i limiti e la conferma |\n'
                            '| `AlertInboxTest.kt` | 10 | Spento di default, ordine, sostituzione, scadenza, cancellazione, una sola conferma, il limite di otto |\n'
                            '\n'
                            'I test Kotlin girano in CI; nessun test è stato eseguito su un orologio o su un emulatore.',
                 'troubleshooting': '| Vedi | Perché | Fai |\n'
                                    '|---|---|---|\n'
                                    "| Sull'orologio non appare nulla | L'opzione degli avvisi dell'orologio è spenta nell'app del telefono, o il telefono non ha "
                                    "inviato `relay` con `enabled: true` | Attiva l'opzione nell'app del telefono |\n"
                                    "| Un avviso sparisce da solo | Il suo `ttlSeconds` è scaduto o il telefono l'ha cancellato | Rilancialo dal telefono |\n"
                                    "| La conferma non fa nulla | L'avviso non la richiede, è scaduto o è già stato confermato una volta | Conferma l'allarme nell'app "
                                    'del telefono |',
                 'structure': '<p align="center">\n'
                              '  <img src="images/repository-structure.svg" alt="Repository structure of ARMOR-WATCH" width="100%">\n'
                              '</p>\n'
                              '\n'
                              '<details>\n'
                              "<summary>Versione testuale dell'albero</summary>\n"
                              '\n'
                              '```text\n'
                              'ARMOR-WATCH/\n'
                              '├── src/\n'
                              '│   ├── main/                               WatchProtocol (i messaggi e i loro controlli) e AlertInbox (gli avvisi sullo schermo)\n'
                              '│   └── test/                               gli stessi esempi del contratto e le regole della casella\n'
                              '├── wear/                               l\'app Wear OS: schermo, servizio Data Layer e runtime\n'
                              '├── watchos/                            l\'app Apple Watch: nucleo Swift, schermo e WatchConnectivity\n'
                              '├── tests/                                  il contratto verificato in Python\n'
                              '├── docs/                                   il contratto e il protocollo\n'
                              '├── tools/                                  controlli e contratto\n'
                              '├── gradle/                                 wrapper Gradle\n'
                              '├── .github/                                workflow CI e modelli per issue e pull request\n'
                              '├── images/                                 banner, icona e le due immagini del README\n'
                              '├── armor.project.json                      manifesto: versione, ruolo, maturità, comando di build\n'
                              '├── CHANGELOG.md                            cosa è cambiato in ogni versione\n'
                              '├── SECURITY.md SUPPORT.md LICENSE          politica di sicurezza, supporto e licenza\n'
                              '├── CONTRIBUTING.md CODE_OF_CONDUCT.md      come contribuire e il codice di condotta\n'
                              '├── build.gradle.kts settings.gradle.kts    il build Kotlin\n'
                              '├── gradle.properties gradlew gradlew.bat   impostazioni Gradle e script del wrapper\n'
                              '└── .gitattributes .gitignore               impostazioni di Git\n'
                              '```\n'
                              '\n'
                              '</details>',
                 'roadmap': "**Limiti noti oggi**\n\n* L'app Wear OS (`wear/`, compilata con `-ParmorWear`), l'app Apple Watch (`watchos/`, compilata solo su un Mac) e i mittenti di ARMOR-ANDROID-CONTROL e ARMOR-IOS-CONTROL (spenti per impostazione predefinita) si compilano e superano i test in CI, ma nulla è stato eseguito su un orologio reale, un emulatore o un simulatore.\n* L'app Apple Watch non è ancora dentro l'app iPhone: l'associazione dei due è ancora da provare; un iPhone non si associa a un orologio Wear OS né un telefono Android a un Apple Watch.\n* Il contratto è custodito qui; il nucleo Kotlin, il nucleo Swift e le app del telefono eseguono gli stessi esempi.\n\n**Prossimi passi**\n\n* Provarlo su un orologio reale di ciascun tipo: associarlo, attivare l'opzione, lanciare un allarme di prova, vederlo sull'orologio, confermarlo con un tocco e vedere la conferma in ARMOR-SERVER; poi spegnere l'opzione e vedere sparire l'avviso."}},
 'ja': {'tagline': 'A.R.M.O.R. の最小ウォッチ：アラーム通知と、タップ 1 回でのアラーム確認',
        'honest': 'メッセージ契約、Kotlin と Swift のコア、ウォッチのセッションはコンピューター上でテストされ、Wear OS アプリ、Apple Watch アプリ、Android と iPhone アプリの送信側は CI でビルドされてテストに合格しています。**実機のウォッチ、エミュレーター、シミュレーターではまだ何も動かしていません。Apple Watch アプリはまだ iPhone アプリの中に入っていません。**',
        'glance': [['役割', 'A.R.M.O.R. の最小ウォッチクライアント（ファミリー：Clients、親：ARMOR-ANDROID-CONTROL）'],
                   ['スタック', 'Kotlin（JVM コアと Compose の Wear OS アプリ、Gradle）、Swift（コアと SwiftUI の Apple Watch アプリ）。検査は Python 3.11+'],
                   ['テスト', 'Python に {{fact:tests:ARMOR-WATCH}} 件（`python -m unittest discover -s tests`）と Kotlin テスト（`./gradlew test`）'],
                   ['メッセージ', 'リレーのスイッチ、アラート、アラートの解除、返信の確認'],
                   ['動作環境', 'JDK 21 のある任意のコンピューター（Kotlin コア）または Mac（Swift コア）、スマートフォンとペアリングした Wear OS 3+ ウォッチまたは Apple Watch（アプリは CI でビルド済み、実行は未）'],
                   ['実機での動作', 'まだなし：ウォッチでもエミュレーターでも実行されていません'],
                   ['ライセンス', 'GPL-3.0-or-later']],
        'status': {'software': 'Kotlin と Swift のコアはすべてのメッセージを読み取って検査し、アラートをメモリ上に保持します。Wear OS アプリ、Apple Watch アプリ、Android と iPhone アプリの送信側は実装済みです。',
                   'tests': 'Python テスト {{fact:tests:ARMOR-WATCH}} 件と Kotlin テストが、契約の同じ受理例・拒否例を実行します。Kotlin テストは CI で動きます。',
                   'hardware': 'ウォッチ、エミュレーター、シミュレーターのいずれでも実行されていません。アプリは CI でのビルドと単体テストのみです。',
                   'docs': '8 言語、プロトコルの説明、契約が書かれ、最新です。'},
        'docs': ['[プロトコルの説明](docs/PROTOCOL.md)：スマートフォンとウォッチの通信方法', '[メッセージ契約](docs/watch_alert_contract.json)：メッセージ、上限、受理される例と拒否される例'],
        'contributing_first': 'プルリクエストの前に `python -m unittest discover -s tests` と `python -I tools/armor_ci_validate.py` '
                              'を実行してください。合格する必要があります。[CONTRIBUTING.md](CONTRIBUTING.md) と[行動規範](CODE_OF_CONDUCT.md)を参照してください。',
        'languages_extra': '',
        'body': {'overview': '* **最小限のウォッチであり、2 つ目のアプリではありません。** ARMOR-ANDROID-CONTROL と ARMOR-IOS-CONTROL が引き続き完全なクライアントです。ウォッチはスマートフォンが送ると決めたアラームと通知を表示し、タップ 1 '
                             '回でアラームを確認できるだけです。\n'
                             '* **スマートフォンだけが ARMOR-SERVER と通信します。** ウォッチはセッション、パスワード、鍵を持たず、ウォッチには何も保存しません。表示内容はメモリ上にあり、アプリを閉じると忘れられます。\n'
                             '* **既定ではオフです。** スマートフォンアプリでウォッチのアラート設定をオンにするまで、何もウォッチには届きません。スマートフォンが許可するまで、ウォッチは受信したアラートをすべて破棄します。\n'
                             '* **4 つの小さなメッセージ**（`relay`、`alert`、`alert_clear`、`alert_ack`）。上限と受理例・拒否例は `docs/watch_alert_contract.json` '
                             'にあります。テキストはスマートフォンが本人の言語で書くので、ウォッチに翻訳するものはありません。\n'
                             '* **独自の音や振動はありません。** システム標準の通知以外は追加しません。',
                 'role': 'ARMOR-WATCH は、スマートフォンアプリの手首側です。[ARMOR-ANDROID-CONTROL](https://github.com/JuanenRac/ARMOR-ANDROID-CONTROL) と '
                         '[ARMOR-IOS-CONTROL](https://github.com/JuanenRac/ARMOR-IOS-CONTROL) が [ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER) '
                         'とのセッションを保持し、ウォッチはスマートフォンから短いアラートを受け取り、本人が確認したアラームの識別子を返します。スマートフォンがそれを検査して実行します。',
                 'architecture': '<p align="center">\n'
                                 '  <img src="images/architecture.svg" alt="ARMOR-WATCH architecture: the person, the Kotlin core and its contract, the phone app and '
                                 'the server" width="100%">\n'
                                 '</p>',
                 'security': '| 脅威 | 防御 |\n'
                             '|---|---|\n'
                             '| オプションをオフにした後もアラートを表示し続けるウォッチ | スマートフォンが `enabled: false` の `relay` を送り、ウォッチは表示していた内容を忘れます。受信箱はオフの状態で始まります |\n'
                             '| 偽造または不正な形式のメッセージ | すべてのメッセージを契約（種類、バージョン、上限、厳密な型）に照らして検査し、失敗したものはエラーなしで破棄します。4096 文字を超えるものは読みません |\n'
                             '| セッションが入ったまま盗まれたウォッチ | セッションはありません。ウォッチはセッション、パスワード、鍵を持たず、ストレージにも何も書きません |\n'
                             '| 2 回送られた確認や、存在しないアラームへの確認 | 確認はアラートごとに 1 回だけ、確認を求めていて期限が切れていないアラートに対してのみ送られます。スマートフォンは知らない識別子を無視します |\n'
                             '| 強制 PIN のアラームが手首に表示されること | スマートフォンは決して送りません（スマートフォンアプリのバナーも表示しません） |',
                 'configuration': '| 設定 | 既定値 | 内容 |\n'
                                  '|---|---|---|\n'
                                  '| `titleMax`, `textMax` | 60, 160 | アラートのタイトルと本文の最大文字数 |\n'
                                  '| `ttlSeconds` | 5 - 600 | アラートが自動で消えるまでの時間 |\n'
                                  '| `pendingMax` | 8 | 同時に保持するアラート数。重大なものは軽いもののために破棄されません |\n'
                                  '| `rawMax` | 4096 | これより長いメッセージは読みません |\n'
                                  '| `relay.enabled` | false | スマートフォンが設定。true になるまでウォッチは何も表示しません |',
                 'quickstart': '**要件：** 検査には Python 3.11+、Kotlin コアには JDK 21（Gradle ラッパーが Gradle 自体をダウンロードします）。\n'
                               '\n'
                               '```powershell\n'
                               'python tools/watch_contract.py                  # the examples of the contract in Python\n'
                               'python -m unittest discover -s tests            # the contract, the Kotlin constants and the protocol notes\n'
                               './gradlew test                                  # the Kotlin core (WatchProtocol and AlertInbox)\n'
                               '```\n'
                               '\n'
                               'メッセージと各側の動作は[プロトコルの説明](docs/PROTOCOL.md)を参照してください。',
                 'testing': '```powershell\n'
                            'python -m unittest discover -s tests\n'
                            './gradlew test\n'
                            'python -I tools/armor_ci_validate.py\n'
                            '```\n'
                            '\n'
                            '| テストファイル | テスト数 | 対象 |\n'
                            '|---|---|---|\n'
                            '| `test_watch_contract.py` | 10 | 契約のすべての例、上限、Kotlin の定数、プロトコルの説明 |\n'
                            '| `WatchProtocolTest.kt` | 6 | Kotlin パーサーに対する同じ例、上限、確認 |\n'
                            '| `AlertInboxTest.kt` | 10 | 既定でオフ、順序、置換、期限切れ、解除、確認は 1 回、上限 8 件 |\n'
                            '\n'
                            'Kotlin テストは CI で動きます。ウォッチでもエミュレーターでもテストは実行されていません。',
                 'troubleshooting': '| 表示 | 原因 | 対処 |\n'
                                    '|---|---|---|\n'
                                    '| ウォッチに何も表示されない | スマートフォンアプリでウォッチのアラートがオフ、またはスマートフォンが `enabled: true` の `relay` を送っていません | スマートフォンアプリでオプションをオンにする |\n'
                                    '| アラートが勝手に消える | `ttlSeconds` が切れたか、スマートフォンが解除しました | スマートフォンからもう一度発生させる |\n'
                                    '| 確認しても何も起きない | アラートが確認を求めていない、期限切れ、または既に 1 回確認済みです | スマートフォンアプリでアラームを確認する |',
                 'structure': '<p align="center">\n'
                              '  <img src="images/repository-structure.svg" alt="Repository structure of ARMOR-WATCH" width="100%">\n'
                              '</p>\n'
                              '\n'
                              '<details>\n'
                              '<summary>ツリーのテキスト版</summary>\n'
                              '\n'
                              '```text\n'
                              'ARMOR-WATCH/\n'
                              '├── src/\n'
                              '│   ├── main/                               WatchProtocol（メッセージとその検査）と AlertInbox（画面上のアラート）\n'
                              '│   └── test/                               契約と同じ例と受信箱のルール\n'
                              '├── wear/                               Wear OS アプリ：画面、Data Layer サービス、ランタイム\n'
                              '├── watchos/                            Apple Watch アプリ：Swift コア、画面、WatchConnectivity\n'
                              '├── tests/                                  Python で検査した契約\n'
                              '├── docs/                                   契約とプロトコル\n'
                              '├── tools/                                  検査と契約\n'
                              '├── gradle/                                 Gradle ラッパー\n'
                              '├── .github/                                CI ワークフローと Issue・Pull Request のテンプレート\n'
                              '├── images/                                 バナー、アイコン、README の 2 つの図\n'
                              '├── armor.project.json                      マニフェスト：バージョン、役割、成熟度、ビルドコマンド\n'
                              '├── CHANGELOG.md                            各バージョンの変更点\n'
                              '├── SECURITY.md SUPPORT.md LICENSE          セキュリティポリシー、サポート、ライセンス\n'
                              '├── CONTRIBUTING.md CODE_OF_CONDUCT.md      貢献方法と行動規範\n'
                              '├── build.gradle.kts settings.gradle.kts    Kotlin のビルド\n'
                              '├── gradle.properties gradlew gradlew.bat   Gradle 設定とラッパースクリプト\n'
                              '└── .gitattributes .gitignore               Git の設定\n'
                              '```\n'
                              '\n'
                              '</details>',
                 'roadmap': '**現時点の既知の制限**\n\n* Wear OS アプリ（`wear/`、`-ParmorWear` でビルド）、Apple Watch アプリ（`watchos/`、Mac でのみビルド）、ARMOR-ANDROID-CONTROL と ARMOR-IOS-CONTROL の送信側（既定ではオフ）は CI でビルドされ単体テストに合格していますが、実機のウォッチ、エミュレーター、シミュレーターでは何も動かしていません。\n* Apple Watch アプリはまだ iPhone アプリの中に入っていないため、両者のペアリングは未確認です。iPhone は Wear OS ウォッチと、Android スマートフォンは Apple Watch とペアリングできません。\n* 契約はここで管理されます。Kotlin コア、Swift コア、スマートフォンアプリは同じ例を実行します。\n\n**次のステップ**\n\n* 各種類の実機ウォッチで確認する：ペアリングし、オプションをオンにし、テストアラームを発生させ、ウォッチで見て、タップで確認し、ARMOR-SERVER で確認済みになるのを見る。その後オプションをオフにして通知が消えるのを見る。'}},
 'zh': {'tagline': 'A.R.M.O.R. 的极简手表：警报通知，轻点一下确认警报',
        'honest': '消息契约、Kotlin 和 Swift 核心以及手表会话已在电脑上测试，Wear OS 应用、Apple Watch 应用以及 Android 和 iPhone 应用的发送端在 CI 中构建并通过测试；**尚未在真实手表、模拟器或仿真器上运行，Apple Watch 应用也还没有放进 iPhone 应用。**',
        'glance': [['角色', 'A.R.M.O.R. 的极简手表客户端（家族：Clients，上级：ARMOR-ANDROID-CONTROL）'],
                   ['技术栈', 'Kotlin（JVM 核心和使用 Compose 的 Wear OS 应用，Gradle），Swift（核心和使用 SwiftUI 的 Apple Watch 应用）；检查用 Python 3.11+'],
                   ['测试', 'Python 中 {{fact:tests:ARMOR-WATCH}} 个（`python -m unittest discover -s tests`）和 Kotlin 测试（`./gradlew test`）'],
                   ['消息', '转发开关、一条警报、警报的清除以及回传的确认'],
                   ['运行于', '任何带 JDK 21 的电脑（Kotlin 核心）或 Mac（Swift 核心）；与手机配对的 Wear OS 3+ 手表或 Apple Watch（应用已在 CI 中构建，尚未运行）'],
                   ['真实硬件', '尚无：没有手表或模拟器运行过'],
                   ['许可证', 'GPL-3.0-or-later']],
        'status': {'software': 'Kotlin 和 Swift 核心读取并检查每条消息，并把警报保存在内存中；Wear OS 应用、Apple Watch 应用以及 Android 和 iPhone 应用中的发送端已编写。',
                   'tests': '{{fact:tests:ARMOR-WATCH}} 个 Python 测试和 Kotlin 测试运行契约中相同的被接受和被拒绝示例；Kotlin 测试在 CI 中运行。',
                   'hardware': '没有手表、模拟器或仿真器运行过它们；应用只在 CI 中构建并做单元测试。',
                   'docs': '八种语言、协议说明和契约均已编写并保持最新。'},
        'docs': ['[协议说明](docs/PROTOCOL.md)：手机与手表如何通信', '[消息契约](docs/watch_alert_contract.json)：消息、限制以及被接受和被拒绝的示例'],
        'contributing_first': '提交 Pull Request 之前运行 `python -m unittest discover -s tests` 和 `python -I tools/armor_ci_validate.py`：必须通过。参见 '
                              '[CONTRIBUTING.md](CONTRIBUTING.md) 和[行为准则](CODE_OF_CONDUCT.md)。',
        'languages_extra': '',
        'body': {'overview': '* **极简手表，而不是第二个应用。** ARMOR-ANDROID-CONTROL 和 ARMOR-IOS-CONTROL 仍是完整客户端；手表只显示手机选择发送的警报和通知，并允许轻点一下确认警报。\n'
                             '* **只有手机与 ARMOR-SERVER 通信。** 手表不持有会话、密码或密钥，也不在手表上保存任何内容：它显示的内容在内存中，关闭应用后即被遗忘。\n'
                             '* **默认关闭。** 在手机应用中打开手表警报选项之前，手表什么也收不到；手机未允许时，手表会丢弃收到的所有警报。\n'
                             '* **四条小消息**（`relay`、`alert`、`alert_clear`、`alert_ack`），限制及被接受和被拒绝的示例见 `docs/watch_alert_contract.json`；文本由手机按用户的语言写好，手表无需翻译。\n'
                             '* **没有自己的声音或振动：** 除系统标准通知外，手表不添加任何内容。',
                 'role': 'ARMOR-WATCH 是手机应用在手腕上的一端。[ARMOR-ANDROID-CONTROL](https://github.com/JuanenRac/ARMOR-ANDROID-CONTROL) 和 '
                         '[ARMOR-IOS-CONTROL](https://github.com/JuanenRac/ARMOR-IOS-CONTROL) 与 [ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER) '
                         '保持会话；手表从手机接收简短警报，并回传用户已确认警报的标识符，由手机检查并执行。',
                 'architecture': '<p align="center">\n'
                                 '  <img src="images/architecture.svg" alt="ARMOR-WATCH architecture: the person, the Kotlin core and its contract, the phone app and '
                                 'the server" width="100%">\n'
                                 '</p>',
                 'security': '| 威胁 | 防御 |\n'
                             '|---|---|\n'
                             '| 关闭选项后仍显示警报的手表 | 手机发送 `enabled: false` 的 `relay`，手表忘记已显示的内容；收件箱默认处于关闭状态 |\n'
                             '| 伪造或格式错误的消息 | 每条消息都会对照契约（类型、版本、限制、精确的类型）检查，不通过的会被无错误地丢弃；超过 4096 个字符的内容不会被读取 |\n'
                             '| 带着会话被偷走的手表 | 没有会话：手表不持有会话、密码或密钥，也不向存储写入任何内容 |\n'
                             '| 发送两次的确认，或针对不存在的警报的确认 | 每条警报只发出一次确认，且仅限要求确认且未过期的警报；手机会忽略它不认识的标识符 |\n'
                             '| 胁迫 PIN 的警报显示在手腕上 | 手机从不发送它（就像手机应用的横幅从不显示它一样） |',
                 'configuration': '| 设置 | 默认值 | 作用 |\n'
                                  '|---|---|---|\n'
                                  '| `titleMax`, `textMax` | 60, 160 | 警报标题和正文的最大字符数 |\n'
                                  '| `ttlSeconds` | 5 - 600 | 警报在自动消失前保留多久 |\n'
                                  '| `pendingMax` | 8 | 同时保留的警报数；严重警报不会为较轻的警报而被丢弃 |\n'
                                  '| `rawMax` | 4096 | 更长的消息不会被读取 |\n'
                                  '| `relay.enabled` | false | 由手机设置；在其为 true 之前手表不显示任何内容 |',
                 'quickstart': '**要求：** 检查需要 Python 3.11+；Kotlin 核心需要 JDK 21（Gradle 包装器会自行下载 Gradle）。\n'
                               '\n'
                               '```powershell\n'
                               'python tools/watch_contract.py                  # the examples of the contract in Python\n'
                               'python -m unittest discover -s tests            # the contract, the Kotlin constants and the protocol notes\n'
                               './gradlew test                                  # the Kotlin core (WatchProtocol and AlertInbox)\n'
                               '```\n'
                               '\n'
                               '消息以及双方的行为见[协议说明](docs/PROTOCOL.md)。',
                 'testing': '```powershell\n'
                            'python -m unittest discover -s tests\n'
                            './gradlew test\n'
                            'python -I tools/armor_ci_validate.py\n'
                            '```\n'
                            '\n'
                            '| 测试文件 | 测试数 | 覆盖内容 |\n'
                            '|---|---|---|\n'
                            '| `test_watch_contract.py` | 10 | 契约的每个示例、限制、Kotlin 常量和协议说明 |\n'
                            '| `WatchProtocolTest.kt` | 6 | 针对 Kotlin 解析器的相同示例、限制和确认 |\n'
                            '| `AlertInboxTest.kt` | 10 | 默认关闭、顺序、替换、过期、清除、仅一次确认、八条上限 |\n'
                            '\n'
                            'Kotlin 测试在 CI 中运行；没有任何测试在手表或模拟器上运行过。',
                 'troubleshooting': '| 你看到 | 原因 | 处理 |\n'
                                    '|---|---|---|\n'
                                    '| 手表上什么也没有出现 | 手机应用中手表警报选项已关闭，或手机未发送 `enabled: true` 的 `relay` | 在手机应用中打开该选项 |\n'
                                    '| 警报自己消失了 | 它的 `ttlSeconds` 已用完，或手机已将其清除 | 从手机重新触发 |\n'
                                    '| 确认没有任何反应 | 该警报不要求确认、已过期，或已确认过一次 | 在手机应用中确认警报 |',
                 'structure': '<p align="center">\n'
                              '  <img src="images/repository-structure.svg" alt="Repository structure of ARMOR-WATCH" width="100%">\n'
                              '</p>\n'
                              '\n'
                              '<details>\n'
                              '<summary>目录树的文本版本</summary>\n'
                              '\n'
                              '```text\n'
                              'ARMOR-WATCH/\n'
                              '├── src/\n'
                              '│   ├── main/                               WatchProtocol（消息及其检查）和 AlertInbox（屏幕上的警报）\n'
                              '│   └── test/                               与契约相同的示例以及收件箱的规则\n'
                              '├── wear/                               Wear OS 应用：界面、Data Layer 服务和运行时\n'
                              '├── watchos/                            Apple Watch 应用：Swift 核心、界面和 WatchConnectivity\n'
                              '├── tests/                                  用 Python 检查的契约\n'
                              '├── docs/                                   契约与协议\n'
                              '├── tools/                                  检查与契约\n'
                              '├── gradle/                                 Gradle 包装器\n'
                              '├── .github/                                CI 工作流以及 Issue 和 Pull Request 模板\n'
                              '├── images/                                 横幅图、图标和 README 的两幅图\n'
                              '├── armor.project.json                      清单：版本、角色、成熟度、构建命令\n'
                              '├── CHANGELOG.md                            每个版本的变化\n'
                              '├── SECURITY.md SUPPORT.md LICENSE          安全策略、支持和许可证\n'
                              '├── CONTRIBUTING.md CODE_OF_CONDUCT.md      如何贡献及行为准则\n'
                              '├── build.gradle.kts settings.gradle.kts    Kotlin 构建\n'
                              '├── gradle.properties gradlew gradlew.bat   Gradle 设置和包装器脚本\n'
                              '└── .gitattributes .gitignore               Git 设置\n'
                              '```\n'
                              '\n'
                              '</details>',
                 'roadmap': '**当前已知限制**\n\n* Wear OS 应用（`wear/`，用 `-ParmorWear` 构建）、Apple Watch 应用（`watchos/`，只在 Mac 上构建）以及 ARMOR-ANDROID-CONTROL 和 ARMOR-IOS-CONTROL 的发送端（默认关闭）在 CI 中构建并通过单元测试，但尚未在真实手表、模拟器或仿真器上运行。\n* Apple Watch 应用还没有放进 iPhone 应用，所以两者的配对尚待试验；iPhone 不能与 Wear OS 手表配对，Android 手机也不能与 Apple Watch 配对。\n* 契约保存在这里；Kotlin 核心、Swift 核心和手机应用运行相同的示例。\n\n**下一步**\n\n* 在每种真实手表上验证：配对，打开选项，触发测试警报，在手表上看到它，轻点确认，并在 ARMOR-SERVER 中看到已确认；然后关闭选项，看到提醒消失。'}},
 'pt': {'tagline': 'O relógio mínimo do A.R.M.O.R.: avisos de alarme e um toque para confirmar um alarme',
        'honest': 'O contrato das mensagens, os núcleos Kotlin e Swift e a sessão do relógio são testados num computador, e a app Wear OS, a app do Apple Watch e o lado que envia das apps Android e iPhone compilam e passam os seus testes na CI; **nada correu num relógio real, num emulador nem num simulador, e a app do Apple Watch ainda não está dentro da app do iPhone.**',
        'glance': [['Função', 'O cliente de relógio mínimo do A.R.M.O.R. (família: Clients, pai: ARMOR-ANDROID-CONTROL)'],
                   ['Stack', 'Kotlin (núcleo JVM e a app Wear OS com Compose, Gradle), Swift (núcleo e a app do Apple Watch com SwiftUI); Python 3.11+ para as verificações'],
                   ['Testes', '{{fact:tests:ARMOR-WATCH}} em Python (`python -m unittest discover -s tests`) e os testes Kotlin (`./gradlew test`)'],
                   ['Mensagens', 'O interruptor do relé, um alerta, a limpeza de um alerta e a confirmação de volta'],
                   ['Corre em', 'Qualquer computador com JDK 21 (núcleo Kotlin) ou um Mac (núcleo Swift); um relógio Wear OS 3+ ou um Apple Watch emparelhado com o telemóvel (apps compiladas na CI, nunca executadas)'],
                   ['Em hardware real', 'Nenhum ainda: nenhum relógio ou emulador o executou'],
                   ['Licença', 'GPL-3.0-or-later']],
        'status': {'software': 'Os núcleos Kotlin e Swift lêem e verificam cada mensagem e guardam os alertas em memória; a app Wear OS, a app do Apple Watch e os emissores das apps Android e iPhone estão escritos.',
                   'tests': '{{fact:tests:ARMOR-WATCH}} testes Python e os testes Kotlin executam os mesmos exemplos aceites e recusados do contrato; os testes Kotlin '
                            'correm na CI.',
                   'hardware': 'Nenhum relógio, emulador nem simulador as executou; as apps só são compiladas e testadas com testes unitários na CI.',
                   'docs': 'Oito idiomas, as notas do protocolo e o contrato estão escritos e atualizados.'},
        'docs': ['[Notas do protocolo](docs/PROTOCOL.md): como falam o telemóvel e o relógio',
                 '[Contrato das mensagens](docs/watch_alert_contract.json): as mensagens, os limites e os exemplos aceites e recusados'],
        'contributing_first': 'Antes de um pull request executa `python -m unittest discover -s tests` e `python -I tools/armor_ci_validate.py`: tem de passar. Vê '
                              '[CONTRIBUTING.md](CONTRIBUTING.md) e o [código de conduta](CODE_OF_CONDUCT.md).',
        'languages_extra': '',
        'body': {'overview': '* **Um relógio mínimo, não uma segunda app.** O ARMOR-ANDROID-CONTROL e o ARMOR-IOS-CONTROL continuam a ser o cliente completo; o relógio '
                             'só mostra os alarmes e avisos que o telemóvel escolhe enviar e deixa confirmar um alarme com um toque.\n'
                             '* **Só o telemóvel fala com o ARMOR-SERVER.** O relógio não guarda sessão, palavra-passe nem chave, e não guarda nada no relógio: o que '
                             'mostra está em memória e esquece-se ao fechar a app.\n'
                             '* **Desligado por predefinição.** Nada chega ao relógio até a pessoa ativar a opção dos alertas do relógio na app do telemóvel; enquanto o '
                             'telemóvel não o disser, o relógio descarta todo o alerta que receba.\n'
                             '* **Quatro mensagens pequenas** (`relay`, `alert`, `alert_clear`, `alert_ack`) com limites e exemplos aceites e recusados em '
                             '`docs/watch_alert_contract.json`; o telemóvel escreve os textos na língua da pessoa, por isso o relógio não tem nada para traduzir.\n'
                             '* **Sem som nem vibração próprios:** o relógio não acrescenta nenhum além da notificação normal do sistema.',
                 'role': 'O ARMOR-WATCH é o lado do pulso das apps do telemóvel. O [ARMOR-ANDROID-CONTROL](https://github.com/JuanenRac/ARMOR-ANDROID-CONTROL) e o '
                         '[ARMOR-IOS-CONTROL](https://github.com/JuanenRac/ARMOR-IOS-CONTROL) mantêm a sessão com o '
                         '[ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER); o relógio recebe um alerta curto do telemóvel e devolve o identificador de um '
                         'alarme que a pessoa confirmou, que o telemóvel verifica e executa.',
                 'architecture': '<p align="center">\n'
                                 '  <img src="images/architecture.svg" alt="ARMOR-WATCH architecture: the person, the Kotlin core and its contract, the phone app and '
                                 'the server" width="100%">\n'
                                 '</p>',
                 'security': '| Ameaça | Defesa |\n'
                             '|---|---|\n'
                             '| Um relógio que ainda mostra alertas com a opção desligada | O telemóvel envia `relay` com `enabled: false` e o relógio esquece o que '
                             'mostrava; a caixa arranca desligada |\n'
                             '| Uma mensagem falsificada ou mal formada | Cada mensagem é verificada contra o contrato (tipo, versão, limites, tipos exatos) e a que '
                             'falha é descartada sem erro; nada com mais de 4096 carateres é lido |\n'
                             '| Um relógio roubado com uma sessão lá dentro | Não há: o relógio não guarda sessão, palavra-passe nem chave e não escreve nada no '
                             'armazenamento |\n'
                             '| Uma confirmação enviada duas vezes ou para um alarme que não existe | A confirmação sai uma vez por alerta, só para um alerta que a peça '
                             'e não tenha caducado; o telemóvel ignora um identificador que não conhece |\n'
                             '| O alarme de um PIN de coação mostrado no pulso | O telemóvel nunca o envia (tal como o aviso das apps do telemóvel nunca o mostra) |',
                 'configuration': '| Definição | Predefinição | O que faz |\n'
                                  '|---|---|---|\n'
                                  '| `titleMax`, `textMax` | 60, 160 | Título e texto mais longos de um alerta, em carateres |\n'
                                  '| `ttlSeconds` | 5 - 600 | Quanto tempo um alerta fica antes de desaparecer sozinho |\n'
                                  '| `pendingMax` | 8 | Alertas guardados ao mesmo tempo; um crítico nunca é descartado por um menor |\n'
                                  '| `rawMax` | 4096 | Uma mensagem mais longa não é lida |\n'
                                  '| `relay.enabled` | false | Definido pelo telemóvel; o relógio não mostra nada até ser verdadeiro |',
                 'quickstart': '**Requisitos:** Python 3.11+ para as verificações; um JDK 21 para o núcleo Kotlin (o wrapper do Gradle descarrega o próprio Gradle).\n'
                               '\n'
                               '```powershell\n'
                               'python tools/watch_contract.py                  # the examples of the contract in Python\n'
                               'python -m unittest discover -s tests            # the contract, the Kotlin constants and the protocol notes\n'
                               './gradlew test                                  # the Kotlin core (WatchProtocol and AlertInbox)\n'
                               '```\n'
                               '\n'
                               'Vê as [notas do protocolo](docs/PROTOCOL.md) para as mensagens e o que faz cada lado.',
                 'testing': '```powershell\n'
                            'python -m unittest discover -s tests\n'
                            './gradlew test\n'
                            'python -I tools/armor_ci_validate.py\n'
                            '```\n'
                            '\n'
                            '| Ficheiro de testes | Testes | O que cobre |\n'
                            '|---|---|---|\n'
                            '| `test_watch_contract.py` | 10 | Cada exemplo do contrato, os limites, as constantes Kotlin e as notas do protocolo |\n'
                            '| `WatchProtocolTest.kt` | 6 | Os mesmos exemplos contra o leitor Kotlin, os limites e a confirmação |\n'
                            '| `AlertInboxTest.kt` | 10 | Desligado por predefinição, ordem, substituição, caducidade, limpeza, uma só confirmação, o limite de oito |\n'
                            '\n'
                            'Os testes Kotlin correm na CI; nenhum teste correu num relógio ou num emulador.',
                 'troubleshooting': '| Vê | Porque | Faça |\n'
                                    '|---|---|---|\n'
                                    '| Nada aparece no relógio | A opção dos alertas do relógio está desligada na app do telemóvel, ou o telemóvel não enviou `relay` '
                                    'com `enabled: true` | Ativa a opção na app do telemóvel |\n'
                                    '| Um alerta desaparece sozinho | O seu `ttlSeconds` acabou ou o telemóvel limpou-o | Volta a lançá-lo a partir do telemóvel |\n'
                                    '| A confirmação não faz nada | O alerta não a pede, caducou ou já foi confirmado uma vez | Confirma o alarme na app do telemóvel |',
                 'structure': '<p align="center">\n'
                              '  <img src="images/repository-structure.svg" alt="Repository structure of ARMOR-WATCH" width="100%">\n'
                              '</p>\n'
                              '\n'
                              '<details>\n'
                              '<summary>Versão em texto da árvore</summary>\n'
                              '\n'
                              '```text\n'
                              'ARMOR-WATCH/\n'
                              '├── src/\n'
                              '│   ├── main/                               WatchProtocol (as mensagens e as suas verificações) e AlertInbox (os alertas no ecrã)\n'
                              '│   └── test/                               os mesmos exemplos do contrato e as regras da caixa\n'
                              '├── wear/                               a app Wear OS: ecrã, serviço Data Layer e runtime\n'
                              '├── watchos/                            a app do Apple Watch: núcleo Swift, ecrã e WatchConnectivity\n'
                              '├── tests/                                  o contrato verificado em Python\n'
                              '├── docs/                                   o contrato e o protocolo\n'
                              '├── tools/                                  verificações e contrato\n'
                              '├── gradle/                                 wrapper do Gradle\n'
                              '├── .github/                                fluxo de CI e modelos de issues e pull requests\n'
                              '├── images/                                 banner, ícone e os dois desenhos do README\n'
                              '├── armor.project.json                      manifesto: versão, função, maturidade, comando de build\n'
                              '├── CHANGELOG.md                            o que mudou em cada versão\n'
                              '├── SECURITY.md SUPPORT.md LICENSE          política de segurança, suporte e licença\n'
                              '├── CONTRIBUTING.md CODE_OF_CONDUCT.md      como contribuir e o código de conduta\n'
                              '├── build.gradle.kts settings.gradle.kts    o build Kotlin\n'
                              '├── gradle.properties gradlew gradlew.bat   definições do Gradle e scripts do wrapper\n'
                              '└── .gitattributes .gitignore               definições do Git\n'
                              '```\n'
                              '\n'
                              '</details>',
                 'roadmap': '**Limites conhecidos hoje**\n\n* A app Wear OS (`wear/`, compilada com `-ParmorWear`), a app do Apple Watch (`watchos/`, compilada só num Mac) e os emissores do ARMOR-ANDROID-CONTROL e do ARMOR-IOS-CONTROL (desligados por predefinição) compilam e passam os testes unitários na CI, mas nada correu num relógio real, num emulador nem num simulador.\n* A app do Apple Watch ainda não está dentro da app do iPhone, por isso o emparelhamento das duas está por tentar; um iPhone não emparelha com um relógio Wear OS nem um telemóvel Android com um Apple Watch.\n* O contrato fica aqui; o núcleo Kotlin, o núcleo Swift e as apps do telemóvel executam os mesmos exemplos.\n\n**A seguir**\n\n* Prová-lo num relógio real de cada tipo: emparelhá-lo, ativar a opção, lançar um alarme de teste, vê-lo no relógio, confirmá-lo com um toque e ver a confirmação no ARMOR-SERVER; depois desligar a opção e ver o aviso desaparecer.'}}}
