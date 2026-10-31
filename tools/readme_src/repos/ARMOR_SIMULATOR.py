# The facts that do not depend on the language, and the words of every language, of ARMOR-SIMULATOR, in the universal README layout.
# Copyright (C) 2026 JuanenRac (Electro Hobby 3D). GPL-3.0-or-later.

FACTS = {
  "emoji": "🧪",
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
      "Python%203.11%2B",
      "3776ab",
    ],
    [
      "Dependencies",
      "none",
      "2ea44f",
    ],
    [
      "Tests",
      "127%20passing",
      "2ea44f",
    ],
  ],
}

TEXT = {
  "en": {
    "tagline": "Offline telemetry simulator with repeatable faults",
    "honest": "Scenarios, faults, delivery to a server and the 127 tests are real, and the simulator is what feeds a server on a computer when no node is plugged in. The geometry is **illustrative**, not a model of the real LD2450 radar, and nothing here has been compared with real hardware.",
    "glance": [
      [
        "Role",
        "Offline telemetry and environment simulator (family: Testing, parent: ARMOR-COMMON)",
      ],
      [
        "Stack",
        "Python 3.11+, standard library only",
      ],
      [
        "Tests",
        "127 (`python -m unittest discover -s tests`)",
      ],
      [
        "Scenarios and faults",
        "4 scenarios, 7 faults (3 break the contract on purpose)",
      ],
      [
        "Runs on",
        "Any computer, or CI",
      ],
      [
        "On real hardware",
        "Not applicable: it is the stand-in for hardware, used on a computer",
      ],
      [
        "License",
        "GPL-3.0-or-later",
      ],
    ],
    "status": {
      "software": "The scenarios, the faults and the delivery to a server work; it is what feeds a server on a computer when no node is plugged in.",
      "tests": "127 tests pass (`python -m unittest discover -s tests`).",
      "protocols": "The geometry is illustrative, not a model of the real LD2450 radar, and nothing has been compared with real hardware.",
      "integration": "It delivers its messages to a server in the tests, and the server of the CM5 test bench can be fed by it.",
      "docs": "Eight languages and the changelog are up to date.",
    },
    "docs": [
      "[Usage](docs/USAGE.md): every option, scenario and fault",
      "[Alarm scenarios](docs/ALARM_SCENARIOS.md): the file format and how to verify a server's answer",
      "[Energy model](docs/ENERGY_MODEL.md): the realistic solar and electrical data and its settings",
    ],
    "contributing_first": "Before a pull request run `python -m unittest discover -s tests` and `python -I tools/armor_ci_validate.py`: it must pass. See [CONTRIBUTING.md](CONTRIBUTING.md) and the [code of conduct](CODE_OF_CONDUCT.md).",
    "languages_extra": "",
    "body": {
      "overview": r"""* **Scenarios:** `patrol`, `crossing`, `two-intruders` and `empty`, on a 270 degree geometry with three sensors, plus a day/night light cycle or a fixed night.
* **Repeatable faults:** a silent node, out-of-order and duplicated messages, a flapping node, and deliberately invalid messages (lux over the limit, unknown field, too many tracks) for negative tests.
* **Deterministic:** the same seed always prints the same lines; nothing is sent unless you give `--server-url` and `--ingest-token`.
* **Checked against the contract:** `--validate` runs every message through ARMOR-COMMON before it is emitted.
* **Careful delivery:** only a plain http(s) origin is accepted; a 4xx stops the run, a 5xx or a network error is retried.
* **Electrical node:** `--electrical` adds the three channels of an electrical node (the grid input, a water heater and a DC bus) over a fast day, with a mains outage, a spell of high voltage and a meter alarm.
* **Solar equipment:** `--solar` adds an inverter and a two-module battery stack (fifteen cells each, capacities included) over a fast day of 240 samples, with a mains outage late in the day; the messages are checked against the solar contract of ARMOR-COMMON and delivered to `/api/v1/solar`.
* **Alarm scenarios in files:** `--alarm-scenario` plays a JSON file with a timeline (people crossing several zones, a pet, wind, a sensor that is stuck, noisy, drifting or dead, a node that loses its link, a mains outage, the mode and the calendar) and may say what the system is expected to answer; `--verify-alarms` compares the alarms a server raised with it, so the files are test cases for ARMOR-SERVER. The reading is strict: the whole file is refused at the first thing that is not understood.
* **Realistic energy data:** `--energy` emits an inverter, a battery stack and an electrical node from a real-time model (a sun with clouds, a house by the hour, a tariff, a Pylontech-style battery with cycles, a noisy meter with holes), deterministic for a seed and tuned from a JSON file. Without the new options the output is exactly what it was.""",
      "role": r"""ARMOR-SIMULATOR is how the rest of the family is tried without hardware: it plays the part of a radar node, a solar gateway or an electrical node and sends their messages to an [ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER), with faults you can repeat, so [ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) and the phone app can be seen working with a house that does not exist. Every message it makes is checked against the contracts of [ARMOR-COMMON](https://github.com/JuanenRac/ARMOR-COMMON).

| Name | How | What for |
|---|---|---|
| ARMOR-SERVER | `POST /api/v1/telemetry`, `/health`, `/solar`, `/electrical/readings` | Receives the simulated messages |
| ARMOR-COMMON | `--validate` | The contracts every message is checked against |
| ARMOR-STUDIO, ARMOR-ANDROID-CONTROL | through the server | Show the simulated house |""",
      "architecture": r"""<p align="center">
  <img src="images/architecture.svg" alt="ARMOR-SIMULATOR architecture: who calls it, what it holds and what it depends on" width="100%">
</p>""",
      "security": r"""| Threat | Defence |
|---|---|
| Sending to a strange destination | Only a plain http(s) origin is accepted (no path, no credentials); a 4xx stops the run, a 5xx or a network error is retried three times |
| The token shows in the process list | `--ingest-token` is discouraged; use `ARMOR_INGEST_TOKEN` or `--ingest-token-file`; nothing writes the token anywhere |
| A test reaches a real server by accident | Nothing is sent unless you give `--server-url` and a token; there is no broker client at all |
| Messages that break the contract on purpose | `corrupt-lux`, `unknown-field` and `oversized-targets` need `--allow-invalid` and cannot be combined with `--validate` |
| Hostile input on the command line | The node id must match `^[a-z0-9][a-z0-9_-]{0,63}$` and `--count` is 1 to 10 000 |

This is a test tool: it is not a safety function and its geometry is not a model of the real radar.""",
      "interfaces": r"""| Option | Default | What it sets |
|---|---|---|
| `--scenario` | `patrol` | `patrol`, `crossing`, `two-intruders`, `empty` |
| `--count` | `1` | Samples (1 to 10 000); one sample is one second |
| `--seed` | `0` | The same seed prints the same lines |
| `--light` | `cycle` | `cycle` (day and night) or `night` (fixed 0.3 lux) |
| `--solar`, `--electrical` | off | Also emit an inverter with batteries / an electrical node |
| `--alarm-scenario`, `--check-alarm-scenario`, `--verify-alarms` | - | Play an alarm scenario from a JSON file / only validate it / compare the alarms a server raised with what it expects (exit 1 when they differ) |
| `--energy`, `--energy-config`, `--energy-days`, `--energy-step-s` | off, -, `1`, `900` | Realistic solar and electrical data in real time instead of the fast day of `--solar`/`--electrical` |
| `--fault`, `--fault-every`, `--fault-topic` | `none`, `3`, `all` | Inject a repeatable fault into some messages |
| `--validate`, `--allow-invalid` | off | Check each message against ARMOR-COMMON / allow the faults that break it |
| `--server-url`, `--ingest-token-file`, `--per-node-token` | - | Deliver to ARMOR-SERVER; the token of each node when the server is strict |

Every option, scenario and fault is in [docs/USAGE.md](docs/USAGE.md). Messages: `armor/node/<id>/telemetry` and `health`, `armor/solar/<node>/<device>/state`, `armor/electrical/<node>/state`; delivery goes to `/api/v1/telemetry`, `/api/v1/health`, `/api/v1/solar` and `/api/v1/electrical/readings`.""",
      "configuration": r"""| Variable | Needed | What it sets |
|---|---|---|
| `ARMOR_INGEST_TOKEN` | with `--server-url` | The ingest token of the server (or a line `ARMOR_INGEST_TOKEN=...` in the file of `--ingest-token-file`) |
| `PYTHONPATH=src` | from a checkout | Where the package is found |

| Limit | Value |
|---|---|
| Samples per run | 1 - 10 000 |
| Sensors and field of view | 3 (-75, 0, +75°) × ±60°, 6000 mm |
| A day of light, solar and electrical | 240 samples |
| Delivery attempts / timeout | 3 / 5 s |""",
      "quickstart": r"""**Requirements:** Python 3.11+ (standard library only).

```powershell
$env:PYTHONPATH = "src"
python -m armor_simulator --count 20 --scenario crossing --seed 1 --validate
python -m armor_simulator --count 60 --scenario two-intruders --server-url http://127.0.0.1:8080 --ingest-token-file token.env
```""",
      "testing": r"""```powershell
$env:PYTHONPATH = "src"
python -m unittest discover -s tests
python -I tools/armor_ci_validate.py
```

| Test file | Tests | What it covers |
|---|---|---|
| `test_simulator.py` | 37 | Scenarios, faults, solar, electrical, validation, delivery to a local HTTP server |
| `test_cli_options.py` | 26 | The options, their limits and the refusals |
| `test_alarm_scenarios.py` | 32 | Alarm scenario files: strict reading, the stream, modes and calendar, verification of the answer, the options |
| `test_energy.py` | 32 | Energy model: physical properties for many seeds, tariff, meter, settings, contracts, the options |""",
      "build": "It is plain Python: nothing to compile. The version lives in `pyproject.toml` and `armor.project.json`.",
      "troubleshooting": r"""| You see | Because | Do |
|---|---|---|
| `--server-url needs a token ...` | A URL without a token, or a token without a URL | Give both |
| HTTP 401 / 403 | The ingest token is wrong; a strict server wants one token per node | `--per-node-token` |
| `--allow-invalid` | The fault breaks the contract on purpose | Add it, and do not use `--validate` |
| The server shows the messages as old | The default start date is 0 and the server replaces it | `--start-ms now` |""",
      "structure": r"""<p align="center">
  <img src="images/repository-structure.svg" alt="Repository structure of ARMOR-SIMULATOR" width="100%">
</p>

<details>
<summary>Text version of the tree</summary>

```text
ARMOR-SIMULATOR/
├── src/armor_simulator/
│   ├── cli.py                           the options and the run
│   ├── scenarios.py cycle.py            the four scenarios, the 270 degree geometry and the day of light
│   ├── alarm_scenarios.py               alarm scenarios from JSON files, their messages and the check of the answer
│   ├── solar.py                         an inverter and a two-module battery stack
│   ├── electrical.py                    the three channels of an electrical node
│   ├── energy.py                        realistic solar and electrical data: sun with clouds, house, tariff, battery, meter
│   ├── faults.py                        the seven repeatable faults
│   └── publisher.py                     delivery to a server with retries
├── tests/                               the tests
├── docs/                                the guides of this repository
├── tools/                               the shared CI checks and project tooling
├── .github/                             CI workflow, issue and pull-request templates
├── examples/                            alarm scenarios and settings of the energy model to start from
├── images/                              banner, icon and the two pictures of this README
├── build.sh build.bat                   build through the shared project workflow
├── test.sh test.bat                     run the tests through the shared workflow
├── run.sh run.bat                       start through the shared project workflow
├── armor.project.json                   manifest: version, role, maturity, build command
├── CHANGELOG.md                         what changed in each version
├── SECURITY.md SUPPORT.md LICENSE       security policy, support and license
├── CONTRIBUTING.md CODE_OF_CONDUCT.md   how to contribute and the code of conduct
├── build-test.sh build-test.bat         run the tests through the shared workflow
├── pyproject.toml                       package metadata
└── .gitattributes .gitignore            Git settings
```

</details>""",
      "roadmap": r"""**Known limits today**

* The geometry is illustrative, not a model of the real LD2450 radar, and nothing has been compared with real hardware.
* It speaks HTTP to a server only; publishing to an MQTT broker is deliberately not built in.

**Next**

* Compare the scenarios with recordings of the real radar once nodes are installed.""",
    },
  },
  "es": {
    "tagline": "Simulador de telemetría sin conexión con fallos repetibles",
    "honest": "Los escenarios, los fallos, la entrega a un servidor y los 127 tests son reales, y el simulador es lo que alimenta a un servidor en un ordenador cuando no hay ningún nodo conectado. La geometría es **ilustrativa**, no un modelo del radar LD2450 real, y nada de esto se ha comparado con hardware real.",
    "glance": [
      [
        "Función",
        "Simulador offline de telemetría y entorno (familia: Testing, padre: ARMOR-COMMON)",
      ],
      [
        "Tecnología",
        "Python 3.11+, solo biblioteca estándar",
      ],
      [
        "Pruebas",
        "127 (`python -m unittest discover -s tests`)",
      ],
      [
        "Escenarios y averías",
        "4 escenarios, 7 averías (3 rompen el contrato a propósito)",
      ],
      [
        "Funciona en",
        "Cualquier ordenador, o CI",
      ],
      [
        "En hardware real",
        "No aplica: es el sustituto del hardware, usado en un ordenador",
      ],
      [
        "Licencia",
        "GPL-3.0-or-later",
      ],
    ],
    "status": {
      "software": "Los escenarios, los fallos y la entrega a un servidor funcionan; es lo que alimenta a un servidor en un ordenador cuando no hay ningún nodo conectado.",
      "tests": "Pasan 127 pruebas (`python -m unittest discover -s tests`).",
      "protocols": "La geometría es ilustrativa, no un modelo del radar LD2450 real, y nada se ha comparado con hardware real.",
      "integration": "Entrega sus mensajes a un servidor en las pruebas, y el servidor del banco de pruebas CM5 puede alimentarse con él.",
      "docs": "Ocho idiomas y el historial de cambios están al día.",
    },
    "docs": [
      "[Uso](docs/USAGE.md): todas las opciones, escenarios y averías",
      "[Escenarios de alarma](docs/ALARM_SCENARIOS.md): el formato del fichero y cómo verificar la respuesta de un servidor",
      "[Modelo de energía](docs/ENERGY_MODEL.md): los datos solares y eléctricos realistas y sus ajustes",
    ],
    "contributing_first": "Antes de un pull request ejecuta `python -m unittest discover -s tests` and `python -I tools/armor_ci_validate.py`: debe pasar. Consulta [CONTRIBUTING.md](CONTRIBUTING.md) y el [código de conducta](CODE_OF_CONDUCT.md).",
    "languages_extra": "",
    "body": {
      "overview": r"""* **Escenarios:** `patrol`, `crossing`, `two-intruders` y `empty`, con una geometría de 270 grados de tres sensores, más un ciclo de luz día/noche o una noche fija.
* **Fallos repetibles:** nodo en silencio, mensajes desordenados y duplicados, nodo intermitente y mensajes inválidos a propósito (lux por encima del límite, campo desconocido, demasiadas pistas) para pruebas negativas.
* **Determinista:** la misma semilla imprime siempre las mismas líneas; no se envía nada salvo que indiques `--server-url` y `--ingest-token`.
* **Comprobado contra el contrato:** `--validate` pasa cada mensaje por ARMOR-COMMON antes de emitirlo.
* **Entrega cuidadosa:** solo se acepta un origen http(s) simple; un 4xx detiene la ejecución, un 5xx o un error de red se reintenta.
* **Nodo eléctrico:** `--electrical` añade los tres canales de un nodo eléctrico (la entrada de red, un termo y un bus de continua) durante un día rápido, con un corte de red, un periodo de tensión alta y una alarma de contador.
* **Equipo solar:** `--solar` añade un inversor y una pila de baterías de dos módulos (quince celdas cada uno, con capacidades) durante un día rápido de 240 muestras, con un corte de red al final de la tarde; los mensajes se comprueban contra el contrato solar de ARMOR-COMMON y se entregan a `/api/v1/solar`.
* **Escenarios de alarma en ficheros:** `--alarm-scenario` reproduce un fichero JSON con una línea de tiempo (personas que cruzan varias zonas, una mascota, viento, un sensor atascado, ruidoso, con deriva o muerto, un nodo que pierde el enlace, un corte de red, el modo y el calendario) y puede decir qué debe responder el sistema; `--verify-alarms` compara las alarmas que levantó un servidor con ello, así que los ficheros son casos de prueba para ARMOR-SERVER. La lectura es estricta: se rechaza todo el fichero ante lo primero que no se entiende.
* **Datos de energía realistas:** `--energy` emite un inversor, una pila de baterías y un nodo eléctrico a partir de un modelo en tiempo real (un sol con nubes, una casa hora a hora, una tarifa, una batería tipo Pylontech con ciclos, un contador con ruido y huecos), determinista para una semilla y ajustable desde un fichero JSON. Sin las opciones nuevas la salida es exactamente la de antes.""",
      "role": r"""ARMOR-SIMULATOR es cómo se prueba el resto de la familia sin hardware: hace de nodo radar, de pasarela solar o de nodo eléctrico y envía sus mensajes a un [ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER), con fallos que se pueden repetir, de modo que [ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) y la app móvil se vean funcionando con una casa que no existe. Cada mensaje que hace se comprueba contra los contratos de [ARMOR-COMMON](https://github.com/JuanenRac/ARMOR-COMMON).

| Nombre | Cómo | Para qué |
|---|---|---|
| ARMOR-SERVER | `POST /api/v1/telemetry`, `/health`, `/solar`, `/electrical/readings` | Recibe los mensajes simulados |
| ARMOR-COMMON | `--validate` | Los contratos contra los que se comprueba cada mensaje |
| ARMOR-STUDIO, ARMOR-ANDROID-CONTROL | a través del servidor | Muestran la casa simulada |""",
      "architecture": r"""<p align="center">
  <img src="images/architecture.svg" alt="Arquitectura de ARMOR-SIMULATOR: quién lo llama, qué contiene y de qué depende" width="100%">
</p>""",
      "security": r"""| Amenaza | Defensa |
|---|---|
| Enviar a un destino extraño | Solo se acepta un origen http(s) plano (sin ruta ni credenciales); un 4xx detiene la ejecución, un 5xx o un error de red se reintenta tres veces |
| El token se ve en la lista de procesos | `--ingest-token` se desaconseja; usa `ARMOR_INGEST_TOKEN` o `--ingest-token-file`; nada escribe el token en ningún sitio |
| Una prueba llega a un servidor real por error | No se envía nada salvo que des `--server-url` y un token; no hay ningún cliente de broker |
| Mensajes que rompen el contrato a propósito | `corrupt-lux`, `unknown-field` y `oversized-targets` exigen `--allow-invalid` y no se combinan con `--validate` |
| Entrada hostil en la línea de órdenes | El id del nodo debe cumplir `^[a-z0-9][a-z0-9_-]{0,63}$` y `--count` va de 1 a 10 000 |

Es una herramienta de pruebas: no es una función de seguridad y su geometría no es un modelo del radar real.""",
      "interfaces": r"""| Opción | Por defecto | Qué define |
|---|---|---|
| `--scenario` | `patrol` | `patrol`, `crossing`, `two-intruders`, `empty` |
| `--count` | `1` | Muestras (1 a 10 000); una muestra es un segundo |
| `--seed` | `0` | La misma semilla imprime las mismas líneas |
| `--light` | `cycle` | `cycle` (día y noche) o `night` (0,3 lux fijos) |
| `--solar`, `--electrical` | off | Emite también un inversor con baterías / un nodo eléctrico |
| `--alarm-scenario`, `--check-alarm-scenario`, `--verify-alarms` | - | Reproducir un escenario de alarma desde un fichero JSON / solo validarlo / comparar las alarmas que levantó un servidor con lo que espera (sale con 1 si difieren) |
| `--energy`, `--energy-config`, `--energy-days`, `--energy-step-s` | no, -, `1`, `900` | Datos solares y eléctricos realistas en tiempo real en lugar del día rápido de `--solar`/`--electrical` |
| `--fault`, `--fault-every`, `--fault-topic` | `none`, `3`, `all` | Inyecta una avería repetible en algunos mensajes |
| `--validate`, `--allow-invalid` | off | Comprueba cada mensaje con ARMOR-COMMON / permite las averías que lo rompen |
| `--server-url`, `--ingest-token-file`, `--per-node-token` | - | Entrega a ARMOR-SERVER; el token de cada nodo si el servidor es estricto |

Todas las opciones, escenarios y averías están en [docs/USAGE.md](docs/USAGE.md). Mensajes: `armor/node/<id>/telemetry` y `health`, `armor/solar/<nodo>/<dispositivo>/state`, `armor/electrical/<nodo>/state`; la entrega va a `/api/v1/telemetry`, `/api/v1/health`, `/api/v1/solar` y `/api/v1/electrical/readings`.""",
      "configuration": r"""| Variable | Necesaria | Qué define |
|---|---|---|
| `ARMOR_INGEST_TOKEN` | con `--server-url` | El token de ingesta del servidor (o una línea `ARMOR_INGEST_TOKEN=...` en el fichero de `--ingest-token-file`) |
| `PYTHONPATH=src` | desde el repositorio | Dónde se encuentra el paquete |

| Límite | Valor |
|---|---|
| Muestras por ejecución | 1 - 10 000 |
| Sensores y campo de visión | 3 (-75, 0, +75°) × ±60°, 6000 mm |
| Un día de luz, solar y eléctrico | 240 muestras |
| Intentos de entrega / límite de tiempo | 3 / 5 s |""",
      "quickstart": r"""**Requisitos:** Python 3.11+ (solo biblioteca estándar).

```powershell
$env:PYTHONPATH = "src"
python -m armor_simulator --count 20 --scenario crossing --seed 1 --validate
python -m armor_simulator --count 60 --scenario two-intruders --server-url http://127.0.0.1:8080 --ingest-token-file token.env
```""",
      "testing": r"""```powershell
$env:PYTHONPATH = "src"
python -m unittest discover -s tests
python -I tools/armor_ci_validate.py
```

| Fichero de pruebas | Pruebas | Qué cubre |
|---|---|---|
| `test_simulator.py` | 37 | Escenarios, averías, solar, eléctrico, validación, entrega a un servidor HTTP local |
| `test_cli_options.py` | 26 | Las opciones, sus límites y los rechazos |
| `test_alarm_scenarios.py` | 32 | Ficheros de escenarios de alarma: lectura estricta, el flujo, modos y calendario, verificación de la respuesta, las opciones |
| `test_energy.py` | 32 | Modelo de energía: propiedades físicas con muchas semillas, tarifa, contador, ajustes, contratos, las opciones |""",
      "build": "Es Python puro: no hay nada que compilar. La versión vive en `pyproject.toml` y `armor.project.json`.",
      "troubleshooting": r"""| Ves | Porque | Haz |
|---|---|---|
| `--server-url needs a token ...` | Una URL sin token, o un token sin URL | Da los dos |
| HTTP 401 / 403 | El token de ingesta es erróneo; un servidor estricto quiere un token por nodo | `--per-node-token` |
| `--allow-invalid` | La avería rompe el contrato a propósito | Añádelo y no uses `--validate` |
| El servidor ve los mensajes como antiguos | La fecha de inicio por defecto es 0 y el servidor la sustituye | `--start-ms now` |""",
      "structure": r"""<p align="center">
  <img src="images/repository-structure.svg" alt="Estructura del repositorio de ARMOR-SIMULATOR" width="100%">
</p>

<details>
<summary>Versión en texto del árbol</summary>

```text
ARMOR-SIMULATOR/
├── src/armor_simulator/
│   ├── cli.py                           las opciones y la ejecución
│   ├── scenarios.py cycle.py            los cuatro escenarios, la geometría de 270 grados y el día de luz
│   ├── alarm_scenarios.py               escenarios de alarma desde ficheros JSON, sus mensajes y la comprobación de la respuesta
│   ├── solar.py                         un inversor y una pila de dos módulos
│   ├── electrical.py                    los tres canales de un nodo eléctrico
│   ├── energy.py                        datos solares y eléctricos realistas: sol con nubes, casa, tarifa, batería, contador
│   ├── faults.py                        las siete averías repetibles
│   └── publisher.py                     entrega a un servidor con reintentos
├── tests/                               las pruebas
├── docs/                                las guías de este repositorio
├── tools/                               las comprobaciones de CI compartidas y las herramientas del proyecto
├── .github/                             flujo de CI y plantillas de issues y pull requests
├── examples/                            escenarios de alarma y ajustes del modelo de energía para empezar
├── images/                              banner, icono y las dos imágenes de este README
├── build.sh build.bat                   compilar con el flujo de proyecto compartido
├── test.sh test.bat                     ejecutar las pruebas con el flujo compartido
├── run.sh run.bat                       arrancar con el flujo de proyecto compartido
├── armor.project.json                   manifiesto: versión, rol, madurez, comando de build
├── CHANGELOG.md                         qué cambió en cada versión
├── SECURITY.md SUPPORT.md LICENSE       política de seguridad, soporte y licencia
├── CONTRIBUTING.md CODE_OF_CONDUCT.md   cómo contribuir y el código de conducta
├── build-test.sh build-test.bat         ejecutar las pruebas con el flujo compartido
├── pyproject.toml                       metadatos del paquete
└── .gitattributes .gitignore            ajustes de Git
```

</details>""",
      "roadmap": r"""**Límites conocidos hoy**

* La geometría es ilustrativa, no un modelo del radar LD2450 real, y nada se ha comparado con hardware real.
* Solo habla HTTP con un servidor; publicar en un broker MQTT no está incluido a propósito.

**Lo siguiente**

* Comparar los escenarios con grabaciones del radar real cuando haya nodos instalados.""",
    },
  },
  "de": {
    "tagline": "Offline-Telemetriesimulator mit wiederholbaren Fehlern",
    "honest": "Die Szenarien, die Fehler, die Zustellung an einen Server und die 127 Tests sind real, und der Simulator speist einen Server auf einem Computer, wenn kein Knoten angeschlossen ist. Die Geometrie ist **veranschaulichend**, kein Modell des echten LD2450-Radars, und nichts davon wurde mit echter Hardware verglichen.",
    "glance": [
      [
        "Rolle",
        "Offline-Simulator für Telemetrie und Umgebung (Familie: Testing, übergeordnet: ARMOR-COMMON)",
      ],
      [
        "Technik",
        "Python 3.11+, nur Standardbibliothek",
      ],
      [
        "Tests",
        "127 (`python -m unittest discover -s tests`)",
      ],
      [
        "Szenarien und Fehler",
        "4 Szenarien, 7 Fehler (3 brechen den Vertrag absichtlich)",
      ],
      [
        "Läuft auf",
        "Jeder Computer oder CI",
      ],
      [
        "Auf echter Hardware",
        "Nicht zutreffend: er ist der Hardware-Ersatz, auf einem Computer benutzt",
      ],
      [
        "Lizenz",
        "GPL-3.0-or-later",
      ],
    ],
    "status": {
      "software": "Die Szenarien, die Störungen und die Übergabe an einen Server funktionieren; er speist einen Server auf einem Rechner, wenn kein Knoten angeschlossen ist.",
      "tests": "127 Tests bestehen (`python -m unittest discover -s tests`).",
      "protocols": "Die Geometrie ist anschaulich und kein Modell des echten LD2450-Radars, und nichts wurde mit echter Hardware verglichen.",
      "integration": "Er übergibt seine Nachrichten in den Tests an einen Server, und der Server des CM5-Prüfstands kann damit gespeist werden.",
      "docs": "Acht Sprachen und das Änderungsprotokoll sind aktuell.",
    },
    "docs": [
      "[Verwendung](docs/USAGE.md): alle Optionen, Szenarien und Fehler",
      "[Alarmszenarien](docs/ALARM_SCENARIOS.md): das Dateiformat und wie man die Antwort eines Servers prüft",
      "[Energiemodell](docs/ENERGY_MODEL.md): die realistischen Solar- und Stromdaten und ihre Einstellungen",
    ],
    "contributing_first": "Führe vor einem Pull Request `python -m unittest discover -s tests` and `python -I tools/armor_ci_validate.py` aus: Es muss bestehen. Siehe [CONTRIBUTING.md](CONTRIBUTING.md) und den [Verhaltenskodex](CODE_OF_CONDUCT.md).",
    "languages_extra": "",
    "body": {
      "overview": r"""* **Szenarien:** `patrol`, `crossing`, `two-intruders` und `empty` auf einer 270-Grad-Geometrie mit drei Sensoren, dazu ein Tag/Nacht-Lichtzyklus oder eine feste Nacht.
* **Wiederholbare Fehler:** ein stummer Knoten, vertauschte und doppelte Nachrichten, ein flatternder Knoten und absichtlich ungültige Nachrichten (Lux über dem Limit, unbekanntes Feld, zu viele Spuren) für Negativtests.
* **Deterministisch:** derselbe Seed druckt immer dieselben Zeilen; gesendet wird nur mit `--server-url` und `--ingest-token`.
* **Gegen den Vertrag geprüft:** `--validate` schickt jede Nachricht vor dem Ausgeben durch ARMOR-COMMON.
* **Sorgfältige Übermittlung:** nur ein einfacher http(s)-Ursprung wird akzeptiert; ein 4xx stoppt den Lauf, ein 5xx oder ein Netzwerkfehler wird wiederholt.
* **Elektroknoten:** `--electrical` fügt die drei Kanäle eines Elektroknotens hinzu (den Netzanschluss, einen Warmwasserspeicher und einen Gleichstrombus) über einen schnellen Tag, mit einem Netzausfall, einer Phase hoher Spannung und einem Zähleralarm.
* **Solaranlage:** `--solar` fügt einen Wechselrichter und einen Batteriestapel aus zwei Modulen (je fünfzehn Zellen, mit Kapazitäten) über einen Zeitraffer-Tag von 240 Werten hinzu, mit einem Netzausfall am späten Tag; die Nachrichten werden gegen den Solar-Vertrag von ARMOR-COMMON geprüft und an `/api/v1/solar` geliefert.
* **Alarmszenarien in Dateien:** `--alarm-scenario` spielt eine JSON-Datei mit einem Zeitablauf ab (Personen, die mehrere Zonen durchqueren, ein Haustier, Wind, ein Sensor, der hängt, rauscht, driftet oder ausgefallen ist, ein Knoten, der die Verbindung verliert, ein Netzausfall, der Modus und der Kalender) und kann festlegen, was das System antworten soll; `--verify-alarms` vergleicht die Alarme, die ein Server ausgelöst hat, damit, die Dateien sind also Testfälle für ARMOR-SERVER. Das Lesen ist streng: Die ganze Datei wird beim ersten nicht verstandenen Punkt abgelehnt.
* **Realistische Energiedaten:** `--energy` gibt einen Wechselrichter, einen Batteriestapel und einen Elektroknoten aus einem Echtzeitmodell aus (Sonne mit Wolken, ein Haus im Stundenverlauf, ein Tarif, eine Pylontech-artige Batterie mit Zyklen, ein verrauschter Zähler mit Lücken), deterministisch für einen Seed und über eine JSON-Datei einstellbar. Ohne die neuen Optionen bleibt die Ausgabe genau wie zuvor.""",
      "role": r"""ARMOR-SIMULATOR ist die Art, den Rest der Familie ohne Hardware auszuprobieren: Er spielt die Rolle eines Radarknotens, eines Solar-Gateways oder eines Elektroknotens und sendet deren Nachrichten an einen [ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER), mit wiederholbaren Fehlern, sodass [ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) und die Handy-App mit einem Haus, das es nicht gibt, arbeiten. Jede erzeugte Nachricht wird gegen die Verträge von [ARMOR-COMMON](https://github.com/JuanenRac/ARMOR-COMMON) geprüft.

| Name | Wie | Wozu |
|---|---|---|
| ARMOR-SERVER | `POST /api/v1/telemetry`, `/health`, `/solar`, `/electrical/readings` | Empfängt die simulierten Nachrichten |
| ARMOR-COMMON | `--validate` | Die Verträge, gegen die jede Nachricht geprüft wird |
| ARMOR-STUDIO, ARMOR-ANDROID-CONTROL | über den Server | Zeigen das simulierte Haus |""",
      "architecture": r"""<p align="center">
  <img src="images/architecture.svg" alt="Architektur von ARMOR-SIMULATOR: wer es aufruft, was es enthält und wovon es abhängt" width="100%">
</p>""",
      "security": r"""| Bedrohung | Abwehr |
|---|---|
| Senden an ein fremdes Ziel | Nur ein einfacher http(s)-Ursprung wird akzeptiert (ohne Pfad und Zugangsdaten); ein 4xx stoppt den Lauf, ein 5xx oder Netzfehler wird dreimal wiederholt |
| Das Token erscheint in der Prozessliste | `--ingest-token` wird nicht empfohlen; nutze `ARMOR_INGEST_TOKEN` oder `--ingest-token-file`; nichts schreibt das Token irgendwohin |
| Ein Test erreicht versehentlich einen echten Server | Es wird nichts gesendet, außer du gibst `--server-url` und ein Token an; es gibt gar keinen Broker-Client |
| Absichtlich vertragsbrechende Nachrichten | `corrupt-lux`, `unknown-field` und `oversized-targets` brauchen `--allow-invalid` und sind nicht mit `--validate` kombinierbar |
| Feindliche Eingabe auf der Kommandozeile | Die Knoten-ID muss `^[a-z0-9][a-z0-9_-]{0,63}$` erfüllen und `--count` liegt zwischen 1 und 10 000 |

Dies ist ein Testwerkzeug: keine Sicherheitsfunktion, und seine Geometrie ist kein Modell des echten Radars.""",
      "interfaces": r"""| Option | Standard | Was sie festlegt |
|---|---|---|
| `--scenario` | `patrol` | `patrol`, `crossing`, `two-intruders`, `empty` |
| `--count` | `1` | Messwerte (1 bis 10 000); einer ist eine Sekunde |
| `--seed` | `0` | Gleicher Seed, gleiche Zeilen |
| `--light` | `cycle` | `cycle` (Tag und Nacht) oder `night` (fest 0,3 lx) |
| `--solar`, `--electrical` | off | Sendet zusätzlich Wechselrichter mit Batterien / einen Elektroknoten |
| `--alarm-scenario`, `--check-alarm-scenario`, `--verify-alarms` | - | Ein Alarmszenario aus einer JSON-Datei abspielen / nur prüfen / die Alarme eines Servers mit der Erwartung vergleichen (Exit 1 bei Abweichung) |
| `--energy`, `--energy-config`, `--energy-days`, `--energy-step-s` | aus, -, `1`, `900` | Realistische Solar- und Stromdaten in Echtzeit statt des schnellen Tages von `--solar`/`--electrical` |
| `--fault`, `--fault-every`, `--fault-topic` | `none`, `3`, `all` | Spielt in einige Nachrichten einen wiederholbaren Fehler ein |
| `--validate`, `--allow-invalid` | off | Prüft jede Nachricht gegen ARMOR-COMMON / erlaubt Fehler, die ihn brechen |
| `--server-url`, `--ingest-token-file`, `--per-node-token` | - | Zustellung an ARMOR-SERVER; das Token jedes Knotens bei striktem Server |

Alle Optionen, Szenarien und Fehler stehen in [docs/USAGE.md](docs/USAGE.md). Nachrichten: `armor/node/<id>/telemetry` und `health`, `armor/solar/<Knoten>/<Gerät>/state`, `armor/electrical/<Knoten>/state`; zugestellt wird an `/api/v1/telemetry`, `/api/v1/health`, `/api/v1/solar` und `/api/v1/electrical/readings`.""",
      "configuration": r"""| Variable | Nötig | Was sie festlegt |
|---|---|---|
| `ARMOR_INGEST_TOKEN` | mit `--server-url` | Das Ingest-Token des Servers (oder eine Zeile `ARMOR_INGEST_TOKEN=...` in der Datei von `--ingest-token-file`) |
| `PYTHONPATH=src` | aus dem Checkout | Wo das Paket gefunden wird |

| Grenze | Wert |
|---|---|
| Messwerte pro Lauf | 1 - 10 000 |
| Sensoren und Sichtfeld | 3 (-75, 0, +75°) × ±60°, 6000 mm |
| Ein Tag Licht, Solar und Elektro | 240 Messwerte |
| Zustellversuche / Zeitlimit | 3 / 5 s |""",
      "quickstart": r"""**Voraussetzungen:** Python 3.11+ (nur Standardbibliothek).

```powershell
$env:PYTHONPATH = "src"
python -m armor_simulator --count 20 --scenario crossing --seed 1 --validate
python -m armor_simulator --count 60 --scenario two-intruders --server-url http://127.0.0.1:8080 --ingest-token-file token.env
```""",
      "testing": r"""```powershell
$env:PYTHONPATH = "src"
python -m unittest discover -s tests
python -I tools/armor_ci_validate.py
```

| Testdatei | Tests | Was sie abdeckt |
|---|---|---|
| `test_simulator.py` | 37 | Szenarien, Fehler, Solar, Elektro, Validierung, Zustellung an einen lokalen HTTP-Server |
| `test_cli_options.py` | 26 | Die Optionen, ihre Grenzen und die Ablehnungen |
| `test_alarm_scenarios.py` | 32 | Alarmszenario-Dateien: strenges Lesen, der Nachrichtenstrom, Modi und Kalender, Prüfung der Antwort, die Optionen |
| `test_energy.py` | 32 | Energiemodell: physikalische Eigenschaften für viele Seeds, Tarif, Zähler, Einstellungen, Verträge, die Optionen |""",
      "build": "Es ist reines Python: nichts zu kompilieren. Die Version steht in `pyproject.toml` und `armor.project.json`.",
      "troubleshooting": r"""| Sie sehen | Weil | Tun Sie |
|---|---|---|
| `--server-url needs a token ...` | Eine URL ohne Token oder ein Token ohne URL | Gib beide an |
| HTTP 401 / 403 | Das Ingest-Token ist falsch; ein strikter Server will ein Token je Knoten | `--per-node-token` |
| `--allow-invalid` | Der Fehler bricht den Vertrag absichtlich | Füge es hinzu und nutze nicht `--validate` |
| Der Server hält die Nachrichten für alt | Das Standard-Startdatum ist 0 und der Server ersetzt es | `--start-ms now` |""",
      "structure": r"""<p align="center">
  <img src="images/repository-structure.svg" alt="Repository-Struktur von ARMOR-SIMULATOR" width="100%">
</p>

<details>
<summary>Textversion des Baums</summary>

```text
ARMOR-SIMULATOR/
├── src/armor_simulator/
│   ├── cli.py                           die Optionen und der Ablauf
│   ├── scenarios.py cycle.py            die vier Szenarien, die 270-Grad-Geometrie und der Lichttag
│   ├── alarm_scenarios.py               Alarmszenarien aus JSON-Dateien, ihre Nachrichten und die Prüfung der Antwort
│   ├── solar.py                         ein Wechselrichter und ein Batteriestapel aus zwei Modulen
│   ├── electrical.py                    die drei Kanäle eines Elektroknotens
│   ├── energy.py                        realistische Solar- und Stromdaten: Sonne mit Wolken, Haus, Tarif, Batterie, Zähler
│   ├── faults.py                        die sieben wiederholbaren Fehler
│   └── publisher.py                     Zustellung an einen Server mit Wiederholungen
├── tests/                               die Tests
├── docs/                                die Anleitungen dieses Repositorys
├── tools/                               die gemeinsamen CI-Prüfungen und Projektwerkzeuge
├── .github/                             CI-Workflow sowie Vorlagen für Issues und Pull Requests
├── examples/                            Alarmszenarien und Einstellungen des Energiemodells als Ausgangspunkt
├── images/                              Banner, Symbol und die zwei Bilder dieses READMEs
├── build.sh build.bat                   Build über den gemeinsamen Projekt-Workflow
├── test.sh test.bat                     Tests über den gemeinsamen Workflow ausführen
├── run.sh run.bat                       Start über den gemeinsamen Projekt-Workflow
├── armor.project.json                   Manifest: Version, Rolle, Reifegrad, Build-Befehl
├── CHANGELOG.md                         was sich in jeder Version geändert hat
├── SECURITY.md SUPPORT.md LICENSE       Sicherheitsrichtlinie, Support und Lizenz
├── CONTRIBUTING.md CODE_OF_CONDUCT.md   Mitwirkung und Verhaltenskodex
├── build-test.sh build-test.bat         Tests über den gemeinsamen Workflow ausführen
├── pyproject.toml                       Paketmetadaten
└── .gitattributes .gitignore            Git-Einstellungen
```

</details>""",
      "roadmap": r"""**Bekannte Grenzen heute**

* Die Geometrie ist illustrativ, kein Modell des echten LD2450-Radars, und nichts wurde mit echter Hardware verglichen.
* Er spricht nur HTTP mit einem Server; das Veröffentlichen an einen MQTT-Broker ist absichtlich nicht eingebaut.

**Als Nächstes**

* Die Szenarien mit Aufzeichnungen des echten Radars vergleichen, sobald Knoten installiert sind.""",
    },
  },
  "fr": {
    "tagline": "Simulateur de télémétrie hors ligne avec des pannes reproductibles",
    "honest": "Les scénarios, les pannes, la livraison à un serveur et les 127 tests sont réels, et le simulateur est ce qui alimente un serveur sur un ordinateur quand aucun nœud n'est branché. La géométrie est **illustrative**, pas un modèle du vrai radar LD2450, et rien de tout cela n'a été comparé à du matériel réel.",
    "glance": [
      [
        "Rôle",
        "Simulateur hors ligne de télémétrie et d'environnement (famille : Testing, parent : ARMOR-COMMON)",
      ],
      [
        "Technologie",
        "Python 3.11+, bibliothèque standard uniquement",
      ],
      [
        "Tests",
        "127 (`python -m unittest discover -s tests`)",
      ],
      [
        "Scénarios et pannes",
        "4 scénarios, 7 pannes (3 violent le contrat exprès)",
      ],
      [
        "Fonctionne sur",
        "N'importe quel ordinateur, ou la CI",
      ],
      [
        "Sur matériel réel",
        "Sans objet : c'est le substitut du matériel, utilisé sur un ordinateur",
      ],
      [
        "Licence",
        "GPL-3.0-or-later",
      ],
    ],
    "status": {
      "software": "Les scénarios, les pannes et la remise à un serveur fonctionnent ; c'est ce qui alimente un serveur sur un ordinateur quand aucun nœud n'est branché.",
      "tests": "127 tests réussissent (`python -m unittest discover -s tests`).",
      "protocols": "La géométrie est illustrative, pas un modèle du vrai radar LD2450, et rien n'a été comparé à du matériel réel.",
      "integration": "Il remet ses messages à un serveur dans les tests, et le serveur du banc d'essai CM5 peut être alimenté par lui.",
      "docs": "Huit langues et le journal des modifications sont à jour.",
    },
    "docs": [
      "[Utilisation](docs/USAGE.md) : toutes les options, scénarios et pannes",
      "[Scénarios d'alarme](docs/ALARM_SCENARIOS.md) : le format du fichier et comment vérifier la réponse d'un serveur",
      "[Modèle d'énergie](docs/ENERGY_MODEL.md) : les données solaires et électriques réalistes et leurs réglages",
    ],
    "contributing_first": "Avant une pull request, lancez `python -m unittest discover -s tests` and `python -I tools/armor_ci_validate.py` : il doit réussir. Voir [CONTRIBUTING.md](CONTRIBUTING.md) et le [code de conduite](CODE_OF_CONDUCT.md).",
    "languages_extra": "",
    "body": {
      "overview": r"""* **Scénarios :** `patrol`, `crossing`, `two-intruders` et `empty`, sur une géométrie de 270 degrés à trois capteurs, avec un cycle de lumière jour/nuit ou une nuit fixe.
* **Pannes reproductibles :** un nœud muet, des messages désordonnés ou dupliqués, un nœud instable et des messages volontairement invalides (lux hors limite, champ inconnu, trop de pistes) pour les tests négatifs.
* **Déterministe :** la même graine imprime toujours les mêmes lignes ; rien n'est envoyé sans `--server-url` et `--ingest-token`.
* **Vérifié contre le contrat :** `--validate` fait passer chaque message par ARMOR-COMMON avant de l'émettre.
* **Envoi prudent :** seule une origine http(s) simple est acceptée ; une erreur 4xx arrête l'exécution, une 5xx ou une erreur réseau est retentée.
* **Nœud électrique :** `--electrical` ajoute les trois canaux d'un nœud électrique (l'entrée du réseau, un chauffe-eau et un bus continu) sur une journée accélérée, avec une coupure du secteur, une période de tension élevée et une alarme de compteur.
* **Équipement solaire :** `--solar` ajoute un onduleur et une pile de batteries de deux modules (quinze cellules chacun, capacités comprises) sur une journée accélérée de 240 échantillons, avec une coupure du réseau en fin de journée ; les messages sont vérifiés contre le contrat solaire d'ARMOR-COMMON et envoyés à `/api/v1/solar`.
* **Scénarios d'alarme dans des fichiers :** `--alarm-scenario` joue un fichier JSON avec une chronologie (des personnes qui traversent plusieurs zones, un animal, le vent, un capteur bloqué, bruité, qui dérive ou mort, un nœud qui perd la liaison, une coupure du secteur, le mode et le calendrier) et peut dire ce que le système doit répondre ; `--verify-alarms` compare les alarmes levées par un serveur à ce fichier, qui sert donc de cas de test pour ARMOR-SERVER. La lecture est stricte : tout le fichier est refusé dès la première chose non comprise.
* **Données d'énergie réalistes :** `--energy` émet un onduleur, un empilement de batteries et un nœud électrique à partir d'un modèle en temps réel (un soleil avec des nuages, une maison heure par heure, un tarif, une batterie de type Pylontech avec cycles, un compteur bruité avec des trous), déterministe pour une graine et réglable depuis un fichier JSON. Sans les nouvelles options, la sortie est exactement celle d'avant.""",
      "role": r"""ARMOR-SIMULATOR est la façon d'essayer le reste de la famille sans matériel : il joue le rôle d'un nœud radar, d'une passerelle solaire ou d'un nœud électrique et envoie leurs messages à un [ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER), avec des pannes répétables, pour que [ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) et l'application mobile se voient fonctionner avec une maison qui n'existe pas. Chaque message qu'il fait est vérifié contre les contrats d'[ARMOR-COMMON](https://github.com/JuanenRac/ARMOR-COMMON).

| Nom | Comment | À quoi ça sert |
|---|---|---|
| ARMOR-SERVER | `POST /api/v1/telemetry`, `/health`, `/solar`, `/electrical/readings` | Reçoit les messages simulés |
| ARMOR-COMMON | `--validate` | Les contrats contre lesquels chaque message est vérifié |
| ARMOR-STUDIO, ARMOR-ANDROID-CONTROL | via le serveur | Affichent la maison simulée |""",
      "architecture": r"""<p align="center">
  <img src="images/architecture.svg" alt="Architecture de ARMOR-SIMULATOR : qui l'appelle, ce qu'il contient et de quoi il dépend" width="100%">
</p>""",
      "security": r"""| Menace | Défense |
|---|---|
| Envoi vers une destination étrange | Seule une origine http(s) simple est acceptée (sans chemin ni identifiants) ; un 4xx arrête l'exécution, un 5xx ou une erreur réseau est retenté trois fois |
| Le jeton apparaît dans la liste des processus | `--ingest-token` est déconseillé ; utilisez `ARMOR_INGEST_TOKEN` ou `--ingest-token-file` ; rien n'écrit le jeton nulle part |
| Un test atteint un vrai serveur par erreur | Rien n'est envoyé sans `--server-url` et un jeton ; il n'y a aucun client de broker |
| Messages qui violent le contrat exprès | `corrupt-lux`, `unknown-field` et `oversized-targets` exigent `--allow-invalid` et ne se combinent pas avec `--validate` |
| Entrée hostile en ligne de commande | L'identifiant du nœud doit respecter `^[a-z0-9][a-z0-9_-]{0,63}$` et `--count` va de 1 à 10 000 |

C'est un outil de test : ce n'est pas une fonction de sécurité et sa géométrie n'est pas un modèle du vrai radar.""",
      "interfaces": r"""| Option | Par défaut | Ce qu'elle règle |
|---|---|---|
| `--scenario` | `patrol` | `patrol`, `crossing`, `two-intruders`, `empty` |
| `--count` | `1` | Échantillons (1 à 10 000) ; un échantillon = une seconde |
| `--seed` | `0` | La même graine imprime les mêmes lignes |
| `--light` | `cycle` | `cycle` (jour et nuit) ou `night` (0,3 lux fixe) |
| `--solar`, `--electrical` | off | Émet aussi un onduleur avec batteries / un nœud électrique |
| `--alarm-scenario`, `--check-alarm-scenario`, `--verify-alarms` | - | Jouer un scénario d'alarme depuis un fichier JSON / seulement le valider / comparer les alarmes levées par un serveur à ce qu'il attend (code 1 si elles diffèrent) |
| `--energy`, `--energy-config`, `--energy-days`, `--energy-step-s` | non, -, `1`, `900` | Données solaires et électriques réalistes en temps réel au lieu du jour rapide de `--solar`/`--electrical` |
| `--fault`, `--fault-every`, `--fault-topic` | `none`, `3`, `all` | Injecte une panne répétable dans certains messages |
| `--validate`, `--allow-invalid` | off | Vérifie chaque message avec ARMOR-COMMON / autorise les pannes qui le violent |
| `--server-url`, `--ingest-token-file`, `--per-node-token` | - | Livraison à ARMOR-SERVER ; le jeton de chaque nœud si le serveur est strict |

Toutes les options, scénarios et pannes sont dans [docs/USAGE.md](docs/USAGE.md). Messages : `armor/node/<id>/telemetry` et `health`, `armor/solar/<nœud>/<appareil>/state`, `armor/electrical/<nœud>/state` ; la livraison va vers `/api/v1/telemetry`, `/api/v1/health`, `/api/v1/solar` et `/api/v1/electrical/readings`.""",
      "configuration": r"""| Variable | Requise | Ce qu'elle règle |
|---|---|---|
| `ARMOR_INGEST_TOKEN` | avec `--server-url` | Le jeton d'ingestion du serveur (ou une ligne `ARMOR_INGEST_TOKEN=...` dans le fichier de `--ingest-token-file`) |
| `PYTHONPATH=src` | depuis le dépôt | Où se trouve le paquet |

| Limite | Valeur |
|---|---|
| Échantillons par exécution | 1 - 10 000 |
| Capteurs et champ de vision | 3 (-75, 0, +75°) × ±60°, 6000 mm |
| Un jour de lumière, solaire et électrique | 240 échantillons |
| Tentatives de livraison / délai | 3 / 5 s |""",
      "quickstart": r"""**Prérequis:** Python 3.11+ (bibliothèque standard uniquement).

```powershell
$env:PYTHONPATH = "src"
python -m armor_simulator --count 20 --scenario crossing --seed 1 --validate
python -m armor_simulator --count 60 --scenario two-intruders --server-url http://127.0.0.1:8080 --ingest-token-file token.env
```""",
      "testing": r"""```powershell
$env:PYTHONPATH = "src"
python -m unittest discover -s tests
python -I tools/armor_ci_validate.py
```

| Fichier de tests | Tests | Ce qu'il couvre |
|---|---|---|
| `test_simulator.py` | 37 | Scénarios, pannes, solaire, électrique, validation, livraison à un serveur HTTP local |
| `test_cli_options.py` | 26 | Les options, leurs limites et les refus |
| `test_alarm_scenarios.py` | 32 | Fichiers de scénarios d'alarme : lecture stricte, le flux, modes et calendrier, vérification de la réponse, les options |
| `test_energy.py` | 32 | Modèle d'énergie : propriétés physiques pour beaucoup de graines, tarif, compteur, réglages, contrats, les options |""",
      "build": "C'est du Python pur : rien à compiler. La version est dans `pyproject.toml` et `armor.project.json`.",
      "troubleshooting": r"""| Vous voyez | Parce que | Faites |
|---|---|---|
| `--server-url needs a token ...` | Une URL sans jeton, ou un jeton sans URL | Donnez les deux |
| HTTP 401 / 403 | Le jeton est faux ; un serveur strict veut un jeton par nœud | `--per-node-token` |
| `--allow-invalid` | La panne viole le contrat exprès | Ajoutez-le et n'utilisez pas `--validate` |
| Le serveur voit les messages comme anciens | La date de départ par défaut est 0 et le serveur la remplace | `--start-ms now` |""",
      "structure": r"""<p align="center">
  <img src="images/repository-structure.svg" alt="Structure du dépôt de ARMOR-SIMULATOR" width="100%">
</p>

<details>
<summary>Version texte de l'arborescence</summary>

```text
ARMOR-SIMULATOR/
├── src/armor_simulator/
│   ├── cli.py                           les options et l'exécution
│   ├── scenarios.py cycle.py            les quatre scénarios, la géométrie de 270 degrés et le jour de lumière
│   ├── alarm_scenarios.py               scénarios d'alarme depuis des fichiers JSON, leurs messages et la vérification de la réponse
│   ├── solar.py                         un onduleur et une pile de deux modules
│   ├── electrical.py                    les trois canaux d'un nœud électrique
│   ├── energy.py                        données solaires et électriques réalistes : soleil et nuages, maison, tarif, batterie, compteur
│   ├── faults.py                        les sept pannes répétables
│   └── publisher.py                     livraison à un serveur avec nouvelles tentatives
├── tests/                               les tests
├── docs/                                les guides de ce dépôt
├── tools/                               les contrôles CI partagés et les outils du projet
├── .github/                             workflow CI et modèles d'issues et de pull requests
├── examples/                            scénarios d'alarme et réglages du modèle d'énergie pour commencer
├── images/                              bannière, icône et les deux images de ce README
├── build.sh build.bat                   build par le flux de projet partagé
├── test.sh test.bat                     lancer les tests par le flux partagé
├── run.sh run.bat                       démarrer par le flux de projet partagé
├── armor.project.json                   manifeste : version, rôle, maturité, commande de build
├── CHANGELOG.md                         ce qui a changé à chaque version
├── SECURITY.md SUPPORT.md LICENSE       politique de sécurité, support et licence
├── CONTRIBUTING.md CODE_OF_CONDUCT.md   comment contribuer et le code de conduite
├── build-test.sh build-test.bat         lancer les tests par le flux partagé
├── pyproject.toml                       métadonnées du paquet
└── .gitattributes .gitignore            réglages Git
```

</details>""",
      "roadmap": r"""**Limites connues aujourd'hui**

* La géométrie est illustrative, pas un modèle du vrai radar LD2450, et rien n'a été comparé à du matériel réel.
* Il ne parle que HTTP à un serveur ; la publication vers un broker MQTT n'est volontairement pas incluse.

**Ensuite**

* Comparer les scénarios à des enregistrements du vrai radar une fois des nœuds installés.""",
    },
  },
  "it": {
    "tagline": "Simulatore di telemetria offline con guasti ripetibili",
    "honest": "Gli scenari, i guasti, la consegna a un server e i 127 test sono reali, e il simulatore è ciò che alimenta un server su un computer quando nessun nodo è collegato. La geometria è **illustrativa**, non un modello del vero radar LD2450, e nulla di tutto ciò è stato confrontato con hardware reale.",
    "glance": [
      [
        "Ruolo",
        "Simulatore offline di telemetria e ambiente (famiglia: Testing, padre: ARMOR-COMMON)",
      ],
      [
        "Tecnologia",
        "Python 3.11+, solo libreria standard",
      ],
      [
        "Test",
        "127 (`python -m unittest discover -s tests`)",
      ],
      [
        "Scenari e guasti",
        "4 scenari, 7 guasti (3 violano il contratto di proposito)",
      ],
      [
        "Gira su",
        "Qualsiasi computer, o CI",
      ],
      [
        "Su hardware reale",
        "Non applicabile: è il sostituto dell'hardware, usato su un computer",
      ],
      [
        "Licenza",
        "GPL-3.0-or-later",
      ],
    ],
    "status": {
      "software": "Gli scenari, i guasti e la consegna a un server funzionano; è ciò che alimenta un server su un computer quando nessun nodo è collegato.",
      "tests": "Superano 127 test (`python -m unittest discover -s tests`).",
      "protocols": "La geometria è illustrativa, non un modello del vero radar LD2450, e nulla è stato confrontato con hardware reale.",
      "integration": "Consegna i suoi messaggi a un server nei test e il server del banco di prova CM5 può essere alimentato da esso.",
      "docs": "Otto lingue e il registro delle modifiche sono aggiornati.",
    },
    "docs": [
      "[Uso](docs/USAGE.md): tutte le opzioni, gli scenari e i guasti",
      "[Scenari d'allarme](docs/ALARM_SCENARIOS.md): il formato del file e come verificare la risposta di un server",
      "[Modello energetico](docs/ENERGY_MODEL.md): i dati solari ed elettrici realistici e le loro impostazioni",
    ],
    "contributing_first": "Prima di una pull request esegui `python -m unittest discover -s tests` and `python -I tools/armor_ci_validate.py`: deve passare. Vedi [CONTRIBUTING.md](CONTRIBUTING.md) e il [codice di condotta](CODE_OF_CONDUCT.md).",
    "languages_extra": "",
    "body": {
      "overview": r"""* **Scenari:** `patrol`, `crossing`, `two-intruders` ed `empty`, su una geometria di 270 gradi a tre sensori, con un ciclo di luce giorno/notte o una notte fissa.
* **Guasti ripetibili:** un nodo muto, messaggi fuori ordine o duplicati, un nodo instabile e messaggi volutamente non validi (lux oltre il limite, campo sconosciuto, troppe tracce) per i test negativi.
* **Deterministico:** lo stesso seme stampa sempre le stesse righe; non viene inviato nulla senza `--server-url` e `--ingest-token`.
* **Verificato contro il contratto:** `--validate` fa passare ogni messaggio per ARMOR-COMMON prima di emetterlo.
* **Invio prudente:** si accetta solo un'origine http(s) semplice; un 4xx ferma l'esecuzione, un 5xx o un errore di rete viene ritentato.
* **Nodo elettrico:** `--electrical` aggiunge i tre canali di un nodo elettrico (l'ingresso di rete, uno scaldabagno e un bus in continua) su una giornata accelerata, con un'interruzione di rete, un periodo di tensione alta e un allarme di contatore.
* **Impianto solare:** `--solar` aggiunge un inverter e un pacco batterie da due moduli (quindici celle ciascuno, con le capacità) su un giorno accelerato di 240 campioni, con un'interruzione di rete a fine giornata; i messaggi sono verificati contro il contratto solare di ARMOR-COMMON e consegnati a `/api/v1/solar`.
* **Scenari d'allarme in file:** `--alarm-scenario` riproduce un file JSON con una cronologia (persone che attraversano più zone, un animale, il vento, un sensore bloccato, rumoroso, che deriva o morto, un nodo che perde il collegamento, un'interruzione di rete, la modalità e il calendario) e può dire cosa deve rispondere il sistema; `--verify-alarms` confronta gli allarmi sollevati da un server con quel file, che quindi serve da caso di prova per ARMOR-SERVER. La lettura è rigorosa: l'intero file viene rifiutato alla prima cosa non compresa.
* **Dati energetici realistici:** `--energy` emette un inverter, una pila di batterie e un nodo elettrico da un modello in tempo reale (un sole con nuvole, una casa ora per ora, una tariffa, una batteria tipo Pylontech con cicli, un contatore rumoroso con buchi), deterministico per un seed e regolabile da un file JSON. Senza le nuove opzioni l'output è esattamente quello di prima.""",
      "role": r"""ARMOR-SIMULATOR è il modo per provare il resto della famiglia senza hardware: fa la parte di un nodo radar, di un gateway solare o di un nodo elettrico e invia i loro messaggi a un [ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER), con guasti ripetibili, così [ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) e l'app mobile si vedono funzionare con una casa che non esiste. Ogni messaggio che produce è controllato contro i contratti di [ARMOR-COMMON](https://github.com/JuanenRac/ARMOR-COMMON).

| Nome | Come | A cosa serve |
|---|---|---|
| ARMOR-SERVER | `POST /api/v1/telemetry`, `/health`, `/solar`, `/electrical/readings` | Riceve i messaggi simulati |
| ARMOR-COMMON | `--validate` | I contratti con cui si verifica ogni messaggio |
| ARMOR-STUDIO, ARMOR-ANDROID-CONTROL | tramite il server | Mostrano la casa simulata |""",
      "architecture": r"""<p align="center">
  <img src="images/architecture.svg" alt="Architettura di ARMOR-SIMULATOR: chi lo chiama, cosa contiene e da cosa dipende" width="100%">
</p>""",
      "security": r"""| Minaccia | Difesa |
|---|---|
| Invio a una destinazione strana | Si accetta solo un'origine http(s) semplice (senza percorso né credenziali); un 4xx ferma l'esecuzione, un 5xx o un errore di rete viene ritentato tre volte |
| Il token compare nell'elenco dei processi | `--ingest-token` è sconsigliato; usa `ARMOR_INGEST_TOKEN` o `--ingest-token-file`; nulla scrive il token da nessuna parte |
| Un test raggiunge per errore un server reale | Non si invia nulla senza `--server-url` e un token; non c'è alcun client di broker |
| Messaggi che violano il contratto di proposito | `corrupt-lux`, `unknown-field` e `oversized-targets` richiedono `--allow-invalid` e non si combinano con `--validate` |
| Input ostile sulla riga di comando | L'id del nodo deve rispettare `^[a-z0-9][a-z0-9_-]{0,63}$` e `--count` va da 1 a 10 000 |

È uno strumento di prova: non è una funzione di sicurezza e la sua geometria non è un modello del radar reale.""",
      "interfaces": r"""| Opzione | Predefinito | Cosa imposta |
|---|---|---|
| `--scenario` | `patrol` | `patrol`, `crossing`, `two-intruders`, `empty` |
| `--count` | `1` | Campioni (da 1 a 10 000); un campione è un secondo |
| `--seed` | `0` | Lo stesso seed stampa le stesse righe |
| `--light` | `cycle` | `cycle` (giorno e notte) o `night` (0,3 lux fissi) |
| `--solar`, `--electrical` | off | Emette anche un inverter con batterie / un nodo elettrico |
| `--alarm-scenario`, `--check-alarm-scenario`, `--verify-alarms` | - | Riprodurre uno scenario d'allarme da un file JSON / solo validarlo / confrontare gli allarmi sollevati da un server con quanto atteso (codice 1 se differiscono) |
| `--energy`, `--energy-config`, `--energy-days`, `--energy-step-s` | no, -, `1`, `900` | Dati solari ed elettrici realistici in tempo reale invece del giorno rapido di `--solar`/`--electrical` |
| `--fault`, `--fault-every`, `--fault-topic` | `none`, `3`, `all` | Inietta un guasto ripetibile in alcuni messaggi |
| `--validate`, `--allow-invalid` | off | Verifica ogni messaggio con ARMOR-COMMON / consente i guasti che lo violano |
| `--server-url`, `--ingest-token-file`, `--per-node-token` | - | Consegna a ARMOR-SERVER; il token di ogni nodo se il server è rigoroso |

Tutte le opzioni, gli scenari e i guasti sono in [docs/USAGE.md](docs/USAGE.md). Messaggi: `armor/node/<id>/telemetry` e `health`, `armor/solar/<nodo>/<dispositivo>/state`, `armor/electrical/<nodo>/state`; la consegna va a `/api/v1/telemetry`, `/api/v1/health`, `/api/v1/solar` e `/api/v1/electrical/readings`.""",
      "configuration": r"""| Variabile | Necessaria | Cosa imposta |
|---|---|---|
| `ARMOR_INGEST_TOKEN` | con `--server-url` | Il token di ingestione del server (o una riga `ARMOR_INGEST_TOKEN=...` nel file di `--ingest-token-file`) |
| `PYTHONPATH=src` | dal repository | Dove si trova il pacchetto |

| Limite | Valore |
|---|---|
| Campioni per esecuzione | 1 - 10 000 |
| Sensori e campo visivo | 3 (-75, 0, +75°) × ±60°, 6000 mm |
| Un giorno di luce, solare ed elettrico | 240 campioni |
| Tentativi di consegna / timeout | 3 / 5 s |""",
      "quickstart": r"""**Requisiti:** Python 3.11+ (solo libreria standard).

```powershell
$env:PYTHONPATH = "src"
python -m armor_simulator --count 20 --scenario crossing --seed 1 --validate
python -m armor_simulator --count 60 --scenario two-intruders --server-url http://127.0.0.1:8080 --ingest-token-file token.env
```""",
      "testing": r"""```powershell
$env:PYTHONPATH = "src"
python -m unittest discover -s tests
python -I tools/armor_ci_validate.py
```

| File di test | Test | Cosa copre |
|---|---|---|
| `test_simulator.py` | 37 | Scenari, guasti, solare, elettrico, validazione, consegna a un server HTTP locale |
| `test_cli_options.py` | 26 | Le opzioni, i loro limiti e i rifiuti |
| `test_alarm_scenarios.py` | 32 | File di scenari d'allarme: lettura rigorosa, il flusso, modalità e calendario, verifica della risposta, le opzioni |
| `test_energy.py` | 32 | Modello energetico: proprietà fisiche con molti seed, tariffa, contatore, impostazioni, contratti, le opzioni |""",
      "build": "È Python puro: nulla da compilare. La versione sta in `pyproject.toml` e `armor.project.json`.",
      "troubleshooting": r"""| Vedi | Perché | Fai |
|---|---|---|
| `--server-url needs a token ...` | Un URL senza token, o un token senza URL | Dai entrambi |
| HTTP 401 / 403 | Il token è errato; un server rigoroso vuole un token per nodo | `--per-node-token` |
| `--allow-invalid` | Il guasto viola il contratto di proposito | Aggiungilo e non usare `--validate` |
| Il server vede i messaggi come vecchi | La data di inizio predefinita è 0 e il server la sostituisce | `--start-ms now` |""",
      "structure": r"""<p align="center">
  <img src="images/repository-structure.svg" alt="Struttura del repository di ARMOR-SIMULATOR" width="100%">
</p>

<details>
<summary>Versione testuale dell'albero</summary>

```text
ARMOR-SIMULATOR/
├── src/armor_simulator/
│   ├── cli.py                           le opzioni e l'esecuzione
│   ├── scenarios.py cycle.py            i quattro scenari, la geometria a 270 gradi e il giorno di luce
│   ├── alarm_scenarios.py               scenari d'allarme da file JSON, i loro messaggi e la verifica della risposta
│   ├── solar.py                         un inverter e una pila di due moduli
│   ├── electrical.py                    i tre canali di un nodo elettrico
│   ├── energy.py                        dati solari ed elettrici realistici: sole con nuvole, casa, tariffa, batteria, contatore
│   ├── faults.py                        i sette guasti ripetibili
│   └── publisher.py                     consegna a un server con nuovi tentativi
├── tests/                               i test
├── docs/                                le guide di questo repository
├── tools/                               i controlli CI condivisi e gli strumenti del progetto
├── .github/                             workflow CI e modelli per issue e pull request
├── examples/                            scenari d'allarme e impostazioni del modello energetico da cui partire
├── images/                              banner, icona e le due immagini di questo README
├── build.sh build.bat                   build tramite il flusso di progetto condiviso
├── test.sh test.bat                     eseguire i test tramite il flusso condiviso
├── run.sh run.bat                       avvio tramite il flusso di progetto condiviso
├── armor.project.json                   manifesto: versione, ruolo, maturità, comando di build
├── CHANGELOG.md                         cosa è cambiato in ogni versione
├── SECURITY.md SUPPORT.md LICENSE       politica di sicurezza, supporto e licenza
├── CONTRIBUTING.md CODE_OF_CONDUCT.md   come contribuire e il codice di condotta
├── build-test.sh build-test.bat         eseguire i test tramite il flusso condiviso
├── pyproject.toml                       metadati del pacchetto
└── .gitattributes .gitignore            impostazioni di Git
```

</details>""",
      "roadmap": r"""**Limiti noti oggi**

* La geometria è illustrativa, non un modello del radar LD2450 reale, e nulla è stato confrontato con hardware reale.
* Parla solo HTTP con un server; la pubblicazione su un broker MQTT non è inclusa di proposito.

**Prossimi passi**

* Confrontare gli scenari con registrazioni del radar reale quando i nodi saranno installati.""",
    },
  },
  "ja": {
    "tagline": "再現可能な故障を備えたオフラインのテレメトリシミュレーター",
    "honest": "シナリオ、故障、サーバーへの送信、127 件のテストは実在し、ノードを接続していないときにコンピューター上のサーバーにデータを送るのがシミュレーターです。ジオメトリは**例示的**なもので、実際の LD2450 レーダーのモデルではなく、実機との比較は一切していません。",
    "glance": [
      [
        "役割",
        "オフラインのテレメトリ・環境シミュレーター（ファミリー：Testing、親：ARMOR-COMMON）",
      ],
      [
        "技術",
        "Python 3.11+、標準ライブラリのみ",
      ],
      [
        "テスト",
        "127 (`python -m unittest discover -s tests`)",
      ],
      [
        "シナリオと障害",
        "シナリオ 4、障害 7（うち 3 は意図的にコントラクト違反）",
      ],
      [
        "動作環境",
        "任意のコンピューターまたは CI",
      ],
      [
        "実機での確認",
        "該当なし：ハードウェアの代役で、コンピューター上で使います",
      ],
      [
        "ライセンス",
        "GPL-3.0-or-later",
      ],
    ],
    "status": {
      "software": "シナリオ、故障、サーバーへの配信は動作します。ノードを接続していないとき、コンピューター上のサーバーにデータを送るのがこれです。",
      "tests": "127 件のテストが通ります（`python -m unittest discover -s tests`）。",
      "protocols": "幾何は例示用で、実際の LD2450 レーダーのモデルではありません。実機との比較もしていません。",
      "integration": "テストではメッセージをサーバーに配信しており、CM5 テストベンチのサーバーにもこれでデータを送れます。",
      "docs": "8 言語と変更履歴は最新です。",
    },
    "docs": [
      "[使い方](docs/USAGE.md)：すべてのオプション、シナリオ、障害",
      "[アラームシナリオ](docs/ALARM_SCENARIOS.md)：ファイル形式とサーバーの応答の検証方法",
      "[エネルギーモデル](docs/ENERGY_MODEL.md)：現実的な太陽光・電力データとその設定",
    ],
    "contributing_first": "Pull Request の前に `python -m unittest discover -s tests` and `python -I tools/armor_ci_validate.py` を実行してください。通る必要があります。[CONTRIBUTING.md](CONTRIBUTING.md) と[行動規範](CODE_OF_CONDUCT.md)を参照してください。",
    "languages_extra": "",
    "body": {
      "overview": r"""* **シナリオ：** `patrol`、`crossing`、`two-intruders`、`empty`。センサー 3 基の 270 度配置で、昼夜の光サイクルまたは固定の夜を選べます。
* **再現可能な故障：** 沈黙するノード、順序が入れ替わったり重複したりするメッセージ、不安定なノード、そして否定テスト用にわざと無効にしたメッセージ（lux の上限超過、未知のフィールド、トラックが多すぎる）。
* **決定的：** 同じシードは常に同じ行を出力します。`--server-url` と `--ingest-token` を指定しない限り何も送信しません。
* **契約に照らして検査：** `--validate` は各メッセージを送り出す前に ARMOR-COMMON に通します。
* **慎重な送信：** 単純な http(s) オリジンのみ受け付けます。4xx は実行を止め、5xx やネットワークエラーは再試行します。
* **電気ノード：** `--electrical` は、電気ノードの 3 つのチャンネル（系統入力、給湯器、直流バス）を加速した 1 日にわたって出力し、停電、高電圧の期間、電力量計の警報を含みます。
* **太陽光設備：** `--solar` は、240 サンプルの早送りの 1 日の間に、インバーターと 2 モジュールのバッテリースタック（各 15 セル、容量付き）を加え、夕方に系統の停電を起こします。メッセージは ARMOR-COMMON の太陽光契約で検査され、`/api/v1/solar` に送られます。
* **ファイルで記述するアラームシナリオ:** `--alarm-scenario` は、時系列（複数のゾーンを横切る人、ペット、風、固着・ノイズ・ドリフト・故障したセンサー、通信が途絶えるノード、停電、モードとカレンダー）を記した JSON ファイルを再生し、システムが返すべき応答も記述できます。`--verify-alarms` はサーバーが発したアラームをそれと比較するので、このファイルは ARMOR-SERVER のテストケースになります。読み込みは厳格で、理解できない箇所が最初に見つかった時点でファイル全体を拒否します。
* **現実的なエネルギーデータ:** `--energy` は、リアルタイムのモデル（雲のある日射、1 時間ごとの住宅の消費、料金、サイクルを持つ Pylontech 型バッテリー、ノイズと欠測のあるメーター）からインバーター、バッテリースタック、電気ノードを出力します。シードで決定的で、JSON ファイルで調整できます。新しいオプションを使わなければ、出力は従来とまったく同じです。""",
      "role": r"""ARMOR-SIMULATOR は、ハードウェアなしでファミリーの他の部分を試す手段です。レーダーノード、ソーラーゲートウェイ、電気ノードの役を演じてそのメッセージを [ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER) に送り、再現できる故障も起こせるため、存在しない家で [ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) とスマートフォンアプリが動く様子を見られます。生成するメッセージはすべて [ARMOR-COMMON](https://github.com/JuanenRac/ARMOR-COMMON) のコントラクトで検査されます。

| 名前 | 方法 | 用途 |
|---|---|---|
| ARMOR-SERVER | `POST /api/v1/telemetry`, `/health`, `/solar`, `/electrical/readings` | 模擬メッセージを受け取る |
| ARMOR-COMMON | `--validate` | 各メッセージを検証するコントラクト |
| ARMOR-STUDIO, ARMOR-ANDROID-CONTROL | サーバー経由 | 模擬の家を表示する |""",
      "architecture": r"""<p align="center">
  <img src="images/architecture.svg" alt="ARMOR-SIMULATOR のアーキテクチャ：呼び出し元、内部、依存先" width="100%">
</p>""",
      "security": r"""| 脅威 | 対策 |
|---|---|
| 不審な宛先への送信 | パスや認証情報のない単純な http(s) オリジンのみ受け付けます。4xx は実行を止め、5xx やネットワークエラーは 3 回再試行します |
| トークンがプロセス一覧に表示される | `--ingest-token` は非推奨です。`ARMOR_INGEST_TOKEN` か `--ingest-token-file` を使ってください。トークンはどこにも書き込まれません |
| テストが誤って本番サーバーに届く | `--server-url` とトークンを指定しない限り何も送信されません。ブローカークライアントは一切ありません |
| 意図的にコントラクトを破るメッセージ | `corrupt-lux`、`unknown-field`、`oversized-targets` は `--allow-invalid` が必要で、`--validate` とは併用できません |
| コマンドラインへの悪意ある入力 | ノード ID は `^[a-z0-9][a-z0-9_-]{0,63}$` に合致する必要があり、`--count` は 1〜10 000 です |

これはテスト用ツールです。安全機能ではなく、配置は実際のレーダーのモデルではありません。""",
      "interfaces": r"""| オプション | 既定値 | 設定内容 |
|---|---|---|
| `--scenario` | `patrol` | `patrol`, `crossing`, `two-intruders`, `empty` |
| `--count` | `1` | サンプル数（1〜10 000）。1 サンプルは 1 秒 |
| `--seed` | `0` | 同じシードなら同じ出力 |
| `--light` | `cycle` | `cycle`（昼夜）または `night`（0.3 lux 固定） |
| `--solar`, `--electrical` | off | インバーターとバッテリー／電気ノードも出力 |
| `--alarm-scenario`, `--check-alarm-scenario`, `--verify-alarms` | - | JSON ファイルのアラームシナリオを再生 / 検証のみ / サーバーが発したアラームを期待と比較（差があれば終了コード 1） |
| `--energy`, `--energy-config`, `--energy-days`, `--energy-step-s` | オフ, -, `1`, `900` | `--solar`/`--electrical` の高速な 1 日の代わりに、リアルタイムの現実的な太陽光・電力データ |
| `--fault`, `--fault-every`, `--fault-topic` | `none`, `3`, `all` | 一部のメッセージに再現可能な障害を入れる |
| `--validate`, `--allow-invalid` | off | 各メッセージを ARMOR-COMMON で検証／違反する障害を許可 |
| `--server-url`, `--ingest-token-file`, `--per-node-token` | - | 配信先は ARMOR-SERVER。サーバーが厳格な場合はノードごとのトークン |

すべてのオプション、シナリオ、障害は [docs/USAGE.md](docs/USAGE.md) にあります。メッセージ：`armor/node/<id>/telemetry` と `health`、`armor/solar/<ノード>/<機器>/state`、`armor/electrical/<ノード>/state`。配信先は `/api/v1/telemetry`、`/api/v1/health`、`/api/v1/solar`、`/api/v1/electrical/readings` です。""",
      "configuration": r"""| 変数 | 必須 | 設定内容 |
|---|---|---|
| `ARMOR_INGEST_TOKEN` | `--server-url` 使用時 | サーバーの取り込みトークン（または `--ingest-token-file` のファイルの `ARMOR_INGEST_TOKEN=...` 行） |
| `PYTHONPATH=src` | チェックアウトから | パッケージの場所 |

| 制限 | 値 |
|---|---|
| 1 回あたりのサンプル数 | 1 - 10 000 |
| センサーと視野 | 3 (-75, 0, +75°) × ±60°, 6000 mm |
| 光・ソーラー・電気の 1 日 | 240 サンプル |
| 配信の試行回数／タイムアウト | 3 / 5 s |""",
      "quickstart": r"""**必要なもの:** Python 3.11+ (標準ライブラリのみ).

```powershell
$env:PYTHONPATH = "src"
python -m armor_simulator --count 20 --scenario crossing --seed 1 --validate
python -m armor_simulator --count 60 --scenario two-intruders --server-url http://127.0.0.1:8080 --ingest-token-file token.env
```""",
      "testing": r"""```powershell
$env:PYTHONPATH = "src"
python -m unittest discover -s tests
python -I tools/armor_ci_validate.py
```

| テストファイル | テスト数 | 対象 |
|---|---|---|
| `test_simulator.py` | 37 | シナリオ、障害、ソーラー、電気、検証、ローカル HTTP サーバーへの配信 |
| `test_cli_options.py` | 26 | オプション、その制限、拒否 |
| `test_alarm_scenarios.py` | 32 | アラームシナリオファイル：厳格な読み込み、メッセージ列、モードとカレンダー、応答の検証、オプション |
| `test_energy.py` | 32 | エネルギーモデル：多数のシードでの物理的性質、料金、メーター、設定、契約、オプション |""",
      "build": "純粋な Python なのでコンパイルは不要です。バージョンは `pyproject.toml` と `armor.project.json` にあります。",
      "troubleshooting": r"""| 症状 | 原因 | 対処 |
|---|---|---|
| `--server-url needs a token ...` | トークンなしの URL、または URL なしのトークン | 両方を指定する |
| HTTP 401 / 403 | 取り込みトークンが誤り。厳格なサーバーはノードごとのトークンを要求 | `--per-node-token` |
| `--allow-invalid` | その障害は意図的にコントラクトを破ります | 追加し、`--validate` は使わない |
| サーバーがメッセージを古いと判断する | 既定の開始日時は 0 でサーバーが置き換える | `--start-ms now` |""",
      "structure": r"""<p align="center">
  <img src="images/repository-structure.svg" alt="ARMOR-SIMULATOR のリポジトリ構造" width="100%">
</p>

<details>
<summary>ツリーのテキスト版</summary>

```text
ARMOR-SIMULATOR/
├── src/armor_simulator/
│   ├── cli.py                           オプションと実行
│   ├── scenarios.py cycle.py            4 つのシナリオ、270 度の配置、1 日の光
│   ├── alarm_scenarios.py               JSON ファイルのアラームシナリオ、そのメッセージ、応答の検証
│   ├── solar.py                         インバーターと 2 モジュールのバッテリー
│   ├── electrical.py                    電気ノードの 3 チャンネル
│   ├── energy.py                        現実的な太陽光・電力データ: 雲のある日射、住宅、料金、バッテリー、メーター
│   ├── faults.py                        再現可能な 7 つの障害
│   └── publisher.py                     再試行つきのサーバーへの配信
├── tests/                               テスト
├── docs/                                このリポジトリのガイド
├── tools/                               共通の CI チェックとプロジェクトツール
├── .github/                             CI ワークフローと Issue・Pull Request のテンプレート
├── examples/                            出発点となるアラームシナリオとエネルギーモデルの設定
├── images/                              バナー、アイコン、この README の 2 つの図
├── build.sh build.bat                   共通のプロジェクトワークフローでビルド
├── test.sh test.bat                     共通のワークフローでテストを実行
├── run.sh run.bat                       共通のプロジェクトワークフローで起動
├── armor.project.json                   マニフェスト：バージョン、役割、成熟度、ビルドコマンド
├── CHANGELOG.md                         各バージョンの変更点
├── SECURITY.md SUPPORT.md LICENSE       セキュリティポリシー、サポート、ライセンス
├── CONTRIBUTING.md CODE_OF_CONDUCT.md   貢献方法と行動規範
├── build-test.sh build-test.bat         共通のワークフローでテストを実行
├── pyproject.toml                       パッケージのメタデータ
└── .gitattributes .gitignore            Git の設定
```

</details>""",
      "roadmap": r"""**現時点の既知の制限**

* 配置は説明用で、実際の LD2450 レーダーのモデルではなく、実機との比較はしていません。
* サーバーとは HTTP のみで通信し、MQTT ブローカーへの発行は意図的に組み込んでいません。

**今後**

* ノードが設置されたら、実際のレーダーの記録とシナリオを比較する。""",
    },
  },
  "zh": {
    "tagline": "带可重复故障的离线遥测模拟器",
    "honest": "场景、故障、向服务器的投递和 127 个测试都是真实的，没有节点接入时，模拟器用来给计算机上的服务器供数据。几何是**示意性的**，不是真实 LD2450 雷达的模型，这里的一切都没有与真实硬件对比过。",
    "glance": [
      [
        "角色",
        "离线遥测与环境模拟器（家族：Testing，上级：ARMOR-COMMON）",
      ],
      [
        "技术栈",
        "Python 3.11+，仅标准库",
      ],
      [
        "测试",
        "127 (`python -m unittest discover -s tests`)",
      ],
      [
        "场景与故障",
        "4 个场景、7 种故障（其中 3 种故意违反合约）",
      ],
      [
        "运行位置",
        "任何计算机或 CI",
      ],
      [
        "真实硬件",
        "不适用：它是硬件的替身，在计算机上使用",
      ],
      [
        "许可证",
        "GPL-3.0-or-later",
      ],
    ],
    "status": {
      "software": "场景、故障和向服务器的投递都能工作；没有接入节点时，它为电脑上的服务器提供数据。",
      "tests": "127 项测试通过（`python -m unittest discover -s tests`）。",
      "protocols": "几何模型仅作示意，并不是真实 LD2450 雷达的模型，也没有与真实硬件对比过。",
      "integration": "测试中它会把消息投递到服务器，CM5 测试台的服务器也可以由它提供数据。",
      "docs": "八种语言和更新日志均为最新。",
    },
    "docs": [
      "[用法](docs/USAGE.md)：所有选项、场景和故障",
      "[报警场景](docs/ALARM_SCENARIOS.md)：文件格式以及如何验证服务器的响应",
      "[能源模型](docs/ENERGY_MODEL.md)：真实的太阳能与电力数据及其设置",
    ],
    "contributing_first": "提交 Pull Request 之前请运行 `python -m unittest discover -s tests` and `python -I tools/armor_ci_validate.py`：必须通过。参见 [CONTRIBUTING.md](CONTRIBUTING.md) 和[行为准则](CODE_OF_CONDUCT.md)。",
    "languages_extra": "",
    "body": {
      "overview": r"""* **场景：** `patrol`、`crossing`、`two-intruders` 和 `empty`，基于三传感器的 270 度几何，另有昼夜光照周期或固定夜晚。
* **可重复的故障：** 静默节点、乱序和重复的消息、抖动的节点，以及为负面测试特意构造的无效消息（lux 超限、未知字段、轨迹过多）。
* **确定性：** 相同的种子总是打印相同的行；除非提供 `--server-url` 和 `--ingest-token`，否则不会发送任何内容。
* **对照契约检查：** `--validate` 在发出每条消息之前先让它通过 ARMOR-COMMON。
* **谨慎投递：** 只接受简单的 http(s) 源；4xx 会终止运行，5xx 或网络错误会重试。
* **电气节点：** `--electrical` 会在加速的一天里加入电气节点的三个通道（电网入口、热水器和直流母线），其中包含一次停电、一段高电压和一次电表告警。
* **太阳能设备：** `--solar` 会在 240 个样本的快进一天中加入一台逆变器和一个两模块的电池组（每个模块十五个电芯，含容量），并在傍晚出现一次市电中断；消息会对照 ARMOR-COMMON 的太阳能契约检查，并投递到 `/api/v1/solar`。
* **用文件描述的报警场景：** `--alarm-scenario` 播放一个带时间线的 JSON 文件（人依次穿过多个区域、宠物、风、卡死/噪声/漂移/失效的传感器、失去链路的节点、市电中断、模式与日历），还可以写明系统应当如何响应；`--verify-alarms` 把服务器实际发出的报警与之比较，因此这些文件就是 ARMOR-SERVER 的测试用例。读取很严格：遇到第一处无法理解的内容就拒绝整个文件。
* **真实的能源数据：** `--energy` 根据实时模型（带云的日照、按小时变化的住宅用电、电价、带循环的 Pylontech 式电池、有噪声和缺失的电表）输出逆变器、电池组和电气节点的消息；对同一种子结果确定，并可通过 JSON 文件调整。不使用新选项时，输出与之前完全一致。""",
      "role": r"""ARMOR-SIMULATOR 让家族的其他部分无需硬件就能试用：它扮演雷达节点、太阳能网关或电气节点，把它们的消息发给 [ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER)，故障可重复，这样就能看到 [ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) 和手机应用在一个并不存在的住宅上运行。它生成的每条消息都对照 [ARMOR-COMMON](https://github.com/JuanenRac/ARMOR-COMMON) 的契约检查。

| 名称 | 方式 | 用途 |
|---|---|---|
| ARMOR-SERVER | `POST /api/v1/telemetry`, `/health`, `/solar`, `/electrical/readings` | 接收模拟消息 |
| ARMOR-COMMON | `--validate` | 每条消息所校验的合约 |
| ARMOR-STUDIO, ARMOR-ANDROID-CONTROL | 通过服务器 | 显示模拟的住宅 |""",
      "architecture": r"""<p align="center">
  <img src="images/architecture.svg" alt="ARMOR-SIMULATOR 的架构：谁调用它、它包含什么、它依赖什么" width="100%">
</p>""",
      "security": r"""| 威胁 | 防御 |
|---|---|
| 发送到可疑目标 | 只接受不带路径和凭据的普通 http(s) 源；4xx 会停止运行，5xx 或网络错误会重试三次 |
| 令牌出现在进程列表中 | 不建议使用 `--ingest-token`；请使用 `ARMOR_INGEST_TOKEN` 或 `--ingest-token-file`；令牌不会被写到任何地方 |
| 测试意外连到真实服务器 | 除非提供 `--server-url` 和令牌，否则不会发送任何内容；根本没有代理客户端 |
| 故意违反合约的消息 | `corrupt-lux`、`unknown-field` 和 `oversized-targets` 需要 `--allow-invalid`，且不能与 `--validate` 同用 |
| 命令行上的恶意输入 | 节点 ID 必须匹配 `^[a-z0-9][a-z0-9_-]{0,63}$`，`--count` 范围为 1 到 10 000 |

这是测试工具：不是安全功能，其几何也不是真实雷达的模型。""",
      "interfaces": r"""| 选项 | 默认值 | 作用 |
|---|---|---|
| `--scenario` | `patrol` | `patrol`, `crossing`, `two-intruders`, `empty` |
| `--count` | `1` | 采样数（1 到 10 000）；一个采样为一秒 |
| `--seed` | `0` | 相同种子输出相同的行 |
| `--light` | `cycle` | `cycle`（昼夜）或 `night`（固定 0.3 lux） |
| `--solar`, `--electrical` | off | 同时输出带电池的逆变器／电气节点 |
| `--alarm-scenario`, `--check-alarm-scenario`, `--verify-alarms` | - | 播放 JSON 文件中的报警场景 / 仅校验 / 把服务器发出的报警与期望比较（不一致时退出码为 1） |
| `--energy`, `--energy-config`, `--energy-days`, `--energy-step-s` | 关, -, `1`, `900` | 用实时的真实太阳能与电力数据取代 `--solar`/`--electrical` 的快速一天 |
| `--fault`, `--fault-every`, `--fault-topic` | `none`, `3`, `all` | 向部分消息注入可重复的故障 |
| `--validate`, `--allow-invalid` | off | 用 ARMOR-COMMON 校验每条消息／允许违反合约的故障 |
| `--server-url`, `--ingest-token-file`, `--per-node-token` | - | 投递到 ARMOR-SERVER；服务器严格时使用每个节点的令牌 |

所有选项、场景和故障见 [docs/USAGE.md](docs/USAGE.md)。消息：`armor/node/<id>/telemetry` 和 `health`、`armor/solar/<节点>/<设备>/state`、`armor/electrical/<节点>/state`；投递到 `/api/v1/telemetry`、`/api/v1/health`、`/api/v1/solar` 和 `/api/v1/electrical/readings`。""",
      "configuration": r"""| 变量 | 必需 | 作用 |
|---|---|---|
| `ARMOR_INGEST_TOKEN` | 配合 `--server-url` | 服务器的摄取令牌（或 `--ingest-token-file` 文件中的 `ARMOR_INGEST_TOKEN=...` 行） |
| `PYTHONPATH=src` | 从源码目录 | 包所在位置 |

| 限制 | 值 |
|---|---|
| 每次运行的采样数 | 1 - 10 000 |
| 传感器与视场 | 3 (-75, 0, +75°) × ±60°, 6000 mm |
| 光照、太阳能和电气的一天 | 240 个采样 |
| 投递尝试次数／超时 | 3 / 5 s |""",
      "quickstart": r"""**要求:** Python 3.11+ (仅标准库).

```powershell
$env:PYTHONPATH = "src"
python -m armor_simulator --count 20 --scenario crossing --seed 1 --validate
python -m armor_simulator --count 60 --scenario two-intruders --server-url http://127.0.0.1:8080 --ingest-token-file token.env
```""",
      "testing": r"""```powershell
$env:PYTHONPATH = "src"
python -m unittest discover -s tests
python -I tools/armor_ci_validate.py
```

| 测试文件 | 测试数 | 覆盖内容 |
|---|---|---|
| `test_simulator.py` | 37 | 场景、故障、太阳能、电气、校验、向本地 HTTP 服务器投递 |
| `test_cli_options.py` | 26 | 选项、其限制和拒绝情形 |
| `test_alarm_scenarios.py` | 32 | 报警场景文件：严格读取、消息流、模式与日历、响应验证、选项 |
| `test_energy.py` | 32 | 能源模型：多种子下的物理性质、电价、电表、设置、契约、选项 |""",
      "build": "纯 Python：无需编译。版本在 `pyproject.toml` 和 `armor.project.json` 中。",
      "troubleshooting": r"""| 现象 | 原因 | 处理 |
|---|---|---|
| `--server-url needs a token ...` | 有 URL 无令牌，或有令牌无 URL | 两者都提供 |
| HTTP 401 / 403 | 摄取令牌错误；严格的服务器要求每个节点一个令牌 | `--per-node-token` |
| `--allow-invalid` | 该故障故意违反合约 | 加上它，并且不要用 `--validate` |
| 服务器认为消息已过期 | 默认起始时间为 0，服务器会替换它 | `--start-ms now` |""",
      "structure": r"""<p align="center">
  <img src="images/repository-structure.svg" alt="ARMOR-SIMULATOR 的仓库结构" width="100%">
</p>

<details>
<summary>目录树的文本版</summary>

```text
ARMOR-SIMULATOR/
├── src/armor_simulator/
│   ├── cli.py                           选项与运行
│   ├── scenarios.py cycle.py            四种场景、270 度几何和一天的光照
│   ├── alarm_scenarios.py               来自 JSON 文件的报警场景、其消息以及对响应的检查
│   ├── solar.py                         逆变器和两模块电池组
│   ├── electrical.py                    电气节点的三个通道
│   ├── energy.py                        真实的太阳能与电力数据:带云的日照、住宅、电价、电池、电表
│   ├── faults.py                        七种可重复的故障
│   └── publisher.py                     带重试的服务器投递
├── tests/                               测试
├── docs/                                本仓库的指南
├── tools/                               共享的 CI 检查和项目工具
├── .github/                             CI 工作流以及 Issue 和 Pull Request 模板
├── examples/                            可供起步的报警场景与能源模型设置
├── images/                              横幅、图标和本 README 的两幅图
├── build.sh build.bat                   通过共享的项目工作流构建
├── test.sh test.bat                     通过共享工作流运行测试
├── run.sh run.bat                       通过共享的项目工作流启动
├── armor.project.json                   清单：版本、角色、成熟度、构建命令
├── CHANGELOG.md                         每个版本的变化
├── SECURITY.md SUPPORT.md LICENSE       安全策略、支持和许可证
├── CONTRIBUTING.md CODE_OF_CONDUCT.md   如何贡献与行为准则
├── build-test.sh build-test.bat         通过共享工作流运行测试
├── pyproject.toml                       包元数据
└── .gitattributes .gitignore            Git 设置
```

</details>""",
      "roadmap": r"""**目前已知的限制**

* 几何仅作演示，不是真实 LD2450 雷达的模型，也没有与真实硬件对比过。
* 只通过 HTTP 与服务器通信；刻意没有内置向 MQTT 代理发布。

**下一步**

* 节点安装后，用真实雷达的录制数据对比这些场景。""",
    },
  },
  "pt": {
    "tagline": "Simulador de telemetria offline com falhas repetíveis",
    "honest": "Os cenários, as falhas, a entrega a um servidor e os 127 testes são reais, e o simulador é o que alimenta um servidor num computador quando nenhum nó está ligado. A geometria é **ilustrativa**, não um modelo do radar LD2450 real, e nada disto foi comparado com hardware real.",
    "glance": [
      [
        "Função",
        "Simulador offline de telemetria e ambiente (família: Testing, pai: ARMOR-COMMON)",
      ],
      [
        "Tecnologia",
        "Python 3.11+, só biblioteca padrão",
      ],
      [
        "Testes",
        "127 (`python -m unittest discover -s tests`)",
      ],
      [
        "Cenários e falhas",
        "4 cenários, 7 falhas (3 violam o contrato de propósito)",
      ],
      [
        "Funciona em",
        "Qualquer computador, ou CI",
      ],
      [
        "Em hardware real",
        "Não se aplica: é o substituto do hardware, usado num computador",
      ],
      [
        "Licença",
        "GPL-3.0-or-later",
      ],
    ],
    "status": {
      "software": "Os cenários, as avarias e a entrega a um servidor funcionam; é o que alimenta um servidor num computador quando nenhum nó está ligado.",
      "tests": "Passam 127 testes (`python -m unittest discover -s tests`).",
      "protocols": "A geometria é ilustrativa, não um modelo do radar LD2450 real, e nada foi comparado com hardware real.",
      "integration": "Entrega as suas mensagens a um servidor nos testes, e o servidor da bancada de testes CM5 pode ser alimentado por ele.",
      "docs": "Oito idiomas e o registo de alterações estão atualizados.",
    },
    "docs": [
      "[Utilização](docs/USAGE.md): todas as opções, cenários e falhas",
      "[Cenários de alarme](docs/ALARM_SCENARIOS.md): o formato do ficheiro e como verificar a resposta de um servidor",
      "[Modelo de energia](docs/ENERGY_MODEL.md): os dados solares e elétricos realistas e as suas definições",
    ],
    "contributing_first": "Antes de um pull request, execute `python -m unittest discover -s tests` and `python -I tools/armor_ci_validate.py`: tem de passar. Consulte [CONTRIBUTING.md](CONTRIBUTING.md) e o [código de conduta](CODE_OF_CONDUCT.md).",
    "languages_extra": "",
    "body": {
      "overview": r"""* **Cenários:** `patrol`, `crossing`, `two-intruders` e `empty`, numa geometria de 270 graus com três sensores, mais um ciclo de luz dia/noite ou uma noite fixa.
* **Falhas repetíveis:** um nó silencioso, mensagens fora de ordem e duplicadas, um nó que oscila, e mensagens deliberadamente inválidas (lux acima do limite, campo desconhecido, demasiados rastos) para testes negativos.
* **Determinista:** a mesma semente imprime sempre as mesmas linhas; nada se envia a menos que indique `--server-url` e `--ingest-token`.
* **Verificado contra o contrato:** `--validate` passa cada mensagem pelo ARMOR-COMMON antes de a emitir.
* **Envio cuidadoso:** só se aceita uma origem http(s) simples; um 4xx pára a execução, um 5xx ou um erro de rede repete-se.
* **Nó elétrico:** `--electrical` acrescenta os três canais de um nó elétrico (a entrada da rede, um esquentador e um barramento DC) ao longo de um dia rápido, com um corte de energia, um período de tensão alta e um alarme do contador.
* **Equipamento solar:** `--solar` acrescenta um inversor e um conjunto de baterias de dois módulos (quinze células cada, capacidades incluídas) ao longo de um dia rápido de 240 amostras, com um corte de energia ao fim do dia; as mensagens verificam-se contra o contrato solar do ARMOR-COMMON e entregam-se em `/api/v1/solar`.
* **Cenários de alarme em ficheiros:** `--alarm-scenario` reproduz um ficheiro JSON com uma linha de tempo (pessoas que atravessam várias zonas, um animal de estimação, vento, um sensor preso, ruidoso, com deriva ou morto, um nó que perde a ligação, um corte de rede, o modo e o calendário) e pode dizer o que o sistema deve responder; `--verify-alarms` compara os alarmes que um servidor levantou com isso, pelo que os ficheiros são casos de teste para o ARMOR-SERVER. A leitura é estrita: o ficheiro inteiro é recusado à primeira coisa que não se entenda.
* **Dados de energia realistas:** `--energy` emite um inversor, uma pilha de baterias e um nó elétrico a partir de um modelo em tempo real (um sol com nuvens, uma casa hora a hora, uma tarifa, uma bateria do tipo Pylontech com ciclos, um contador com ruído e falhas), determinista para uma semente e ajustável a partir de um ficheiro JSON. Sem as novas opções, a saída é exatamente a de antes.""",
      "role": r"""O ARMOR-SIMULATOR é a forma de experimentar o resto da família sem hardware: faz de nó radar, de porta de ligação solar ou de nó elétrico e envia as suas mensagens para um [ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER), com falhas repetíveis, para que o [ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) e a aplicação móvel se vejam a funcionar com uma casa que não existe. Cada mensagem que faz é verificada contra os contratos do [ARMOR-COMMON](https://github.com/JuanenRac/ARMOR-COMMON).

| Nome | Como | Para quê |
|---|---|---|
| ARMOR-SERVER | `POST /api/v1/telemetry`, `/health`, `/solar`, `/electrical/readings` | Recebe as mensagens simuladas |
| ARMOR-COMMON | `--validate` | Os contratos contra os quais cada mensagem é verificada |
| ARMOR-STUDIO, ARMOR-ANDROID-CONTROL | através do servidor | Mostram a casa simulada |""",
      "architecture": r"""<p align="center">
  <img src="images/architecture.svg" alt="Arquitetura de ARMOR-SIMULATOR: quem o chama, o que contém e de que depende" width="100%">
</p>""",
      "security": r"""| Ameaça | Defesa |
|---|---|
| Enviar para um destino estranho | Só se aceita uma origem http(s) simples (sem caminho nem credenciais); um 4xx pára a execução, um 5xx ou um erro de rede é repetido três vezes |
| O token aparece na lista de processos | `--ingest-token` é desaconselhado; use `ARMOR_INGEST_TOKEN` ou `--ingest-token-file`; nada escreve o token em lado nenhum |
| Um teste chega por engano a um servidor real | Nada é enviado sem `--server-url` e um token; não há nenhum cliente de broker |
| Mensagens que violam o contrato de propósito | `corrupt-lux`, `unknown-field` e `oversized-targets` exigem `--allow-invalid` e não se combinam com `--validate` |
| Entrada hostil na linha de comandos | O id do nó tem de cumprir `^[a-z0-9][a-z0-9_-]{0,63}$` e `--count` vai de 1 a 10 000 |

É uma ferramenta de teste: não é uma função de segurança e a sua geometria não é um modelo do radar real.""",
      "interfaces": r"""| Opção | Predefinição | O que define |
|---|---|---|
| `--scenario` | `patrol` | `patrol`, `crossing`, `two-intruders`, `empty` |
| `--count` | `1` | Amostras (1 a 10 000); uma amostra é um segundo |
| `--seed` | `0` | A mesma semente imprime as mesmas linhas |
| `--light` | `cycle` | `cycle` (dia e noite) ou `night` (0,3 lux fixos) |
| `--solar`, `--electrical` | off | Emite também um inversor com baterias / um nó elétrico |
| `--alarm-scenario`, `--check-alarm-scenario`, `--verify-alarms` | - | Reproduzir um cenário de alarme a partir de um ficheiro JSON / só o validar / comparar os alarmes que um servidor levantou com o esperado (sai com 1 se diferirem) |
| `--energy`, `--energy-config`, `--energy-days`, `--energy-step-s` | não, -, `1`, `900` | Dados solares e elétricos realistas em tempo real em vez do dia rápido de `--solar`/`--electrical` |
| `--fault`, `--fault-every`, `--fault-topic` | `none`, `3`, `all` | Injeta uma falha repetível em algumas mensagens |
| `--validate`, `--allow-invalid` | off | Verifica cada mensagem com o ARMOR-COMMON / permite as falhas que o violam |
| `--server-url`, `--ingest-token-file`, `--per-node-token` | - | Entrega ao ARMOR-SERVER; o token de cada nó se o servidor for estrito |

Todas as opções, cenários e falhas estão em [docs/USAGE.md](docs/USAGE.md). Mensagens: `armor/node/<id>/telemetry` e `health`, `armor/solar/<nó>/<dispositivo>/state`, `armor/electrical/<nó>/state`; a entrega vai para `/api/v1/telemetry`, `/api/v1/health`, `/api/v1/solar` e `/api/v1/electrical/readings`.""",
      "configuration": r"""| Variável | Necessária | O que define |
|---|---|---|
| `ARMOR_INGEST_TOKEN` | com `--server-url` | O token de ingestão do servidor (ou uma linha `ARMOR_INGEST_TOKEN=...` no ficheiro de `--ingest-token-file`) |
| `PYTHONPATH=src` | a partir do repositório | Onde o pacote é encontrado |

| Limite | Valor |
|---|---|
| Amostras por execução | 1 - 10 000 |
| Sensores e campo de visão | 3 (-75, 0, +75°) × ±60°, 6000 mm |
| Um dia de luz, solar e elétrico | 240 amostras |
| Tentativas de entrega / limite de tempo | 3 / 5 s |""",
      "quickstart": r"""**Requisitos:** Python 3.11+ (só biblioteca padrão).

```powershell
$env:PYTHONPATH = "src"
python -m armor_simulator --count 20 --scenario crossing --seed 1 --validate
python -m armor_simulator --count 60 --scenario two-intruders --server-url http://127.0.0.1:8080 --ingest-token-file token.env
```""",
      "testing": r"""```powershell
$env:PYTHONPATH = "src"
python -m unittest discover -s tests
python -I tools/armor_ci_validate.py
```

| Ficheiro de testes | Testes | O que cobre |
|---|---|---|
| `test_simulator.py` | 37 | Cenários, falhas, solar, elétrico, validação, entrega a um servidor HTTP local |
| `test_cli_options.py` | 26 | As opções, os seus limites e as recusas |
| `test_alarm_scenarios.py` | 32 | Ficheiros de cenários de alarme: leitura estrita, o fluxo, modos e calendário, verificação da resposta, as opções |
| `test_energy.py` | 32 | Modelo de energia: propriedades físicas com muitas sementes, tarifa, contador, definições, contratos, as opções |""",
      "build": "É Python puro: nada a compilar. A versão está em `pyproject.toml` e `armor.project.json`.",
      "troubleshooting": r"""| Vê | Porque | Faça |
|---|---|---|
| `--server-url needs a token ...` | Um URL sem token, ou um token sem URL | Indique os dois |
| HTTP 401 / 403 | O token está errado; um servidor estrito quer um token por nó | `--per-node-token` |
| `--allow-invalid` | A falha viola o contrato de propósito | Acrescente-o e não use `--validate` |
| O servidor vê as mensagens como antigas | A data de início predefinida é 0 e o servidor substitui-a | `--start-ms now` |""",
      "structure": r"""<p align="center">
  <img src="images/repository-structure.svg" alt="Estrutura do repositório de ARMOR-SIMULATOR" width="100%">
</p>

<details>
<summary>Versão em texto da árvore</summary>

```text
ARMOR-SIMULATOR/
├── src/armor_simulator/
│   ├── cli.py                           as opções e a execução
│   ├── scenarios.py cycle.py            os quatro cenários, a geometria de 270 graus e o dia de luz
│   ├── alarm_scenarios.py               cenários de alarme a partir de ficheiros JSON, as suas mensagens e a verificação da resposta
│   ├── solar.py                         um inversor e uma pilha de dois módulos
│   ├── electrical.py                    os três canais de um nó elétrico
│   ├── energy.py                        dados solares e elétricos realistas: sol com nuvens, casa, tarifa, bateria, contador
│   ├── faults.py                        as sete falhas repetíveis
│   └── publisher.py                     entrega a um servidor com novas tentativas
├── tests/                               os testes
├── docs/                                os guias deste repositório
├── tools/                               as verificações de CI partilhadas e as ferramentas do projeto
├── .github/                             fluxo de CI e modelos de issues e pull requests
├── examples/                            cenários de alarme e definições do modelo de energia para começar
├── images/                              faixa, ícone e as duas imagens deste README
├── build.sh build.bat                   compilar pelo fluxo de projeto partilhado
├── test.sh test.bat                     executar os testes pelo fluxo partilhado
├── run.sh run.bat                       arrancar pelo fluxo de projeto partilhado
├── armor.project.json                   manifesto: versão, função, maturidade, comando de build
├── CHANGELOG.md                         o que mudou em cada versão
├── SECURITY.md SUPPORT.md LICENSE       política de segurança, apoio e licença
├── CONTRIBUTING.md CODE_OF_CONDUCT.md   como contribuir e o código de conduta
├── build-test.sh build-test.bat         executar os testes pelo fluxo partilhado
├── pyproject.toml                       metadados do pacote
└── .gitattributes .gitignore            definições do Git
```

</details>""",
      "roadmap": r"""**Limites conhecidos hoje**

* A geometria é ilustrativa, não um modelo do radar LD2450 real, e nada foi comparado com hardware real.
* Só fala HTTP com um servidor; publicar num broker MQTT não está incluído de propósito.

**A seguir**

* Comparar os cenários com gravações do radar real quando houver nós instalados.""",
    },
  },
}
