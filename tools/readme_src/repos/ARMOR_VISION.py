# The facts that do not depend on the language, and the words of every language, of ARMOR-VISION, in the universal README layout.
# Copyright (C) 2026 JuanenRac (Electro Hobby 3D). GPL-3.0-or-later.

FACTS = {
  "emoji": "👁️",
  "layout": "universal",
  "license_badge": "License-GPL%203.0--or--later-blue",
  "status": [
    [
      "software",
      "yellow",
    ],
    [
      "tests",
      "green",
    ],
    [
      "hardware",
      "red",
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
      "61%20passing",
      "2ea44f",
    ],
  ],
}

TEXT = {
  "en": {
    "tagline": "Zones, masks and detection rules for the cameras",
    "honest": "The zones, the motion check, the tracker, the rules and the 61 tests are real. There is **no real detector model yet** and nothing has run on a camera or on the Jetson Orin NX: the simulation uses scripted detections.",
    "glance": [
      [
        "Role",
        "Camera zones, masks and detection rules (family: Core Services, parent: ARMOR-SERVER)",
      ],
      [
        "Stack",
        "Python 3.11+, standard library only",
      ],
      [
        "Tests",
        "61 (`python -m unittest discover -s tests`)",
      ],
      [
        "Runs on",
        "Any computer",
      ],
      [
        "On real hardware",
        "None yet: no real detector, camera or Jetson (a simulation with scripted detections)",
      ],
      [
        "License",
        "GPL-3.0-or-later",
      ],
    ],
    "status": {
      "software": "The zones, the motion check, the tracker and the rules work, but there is no real detector model yet: the simulation uses scripted detections.",
      "tests": "61 tests pass (`python -m unittest discover -s tests`).",
      "hardware": "Nothing has run on a camera or on the Jetson Orin NX.",
      "docs": "Eight languages and the changelog are up to date.",
    },
    "docs": [
      "[Usage](docs/USAGE.md): the commands, the configuration, the event and the library",
    ],
    "contributing_first": "Before a pull request run `python -m unittest discover -s tests` and `python -I tools/armor_ci_validate.py`: it must pass. See [CONTRIBUTING.md](CONTRIBUTING.md) and the [code of conduct](CODE_OF_CONDUCT.md).",
    "languages_extra": "",
    "body": {
      "overview": r"""* **Zones and masks:** polygons drawn on normalised coordinates (0 to 1), so one drawing works at any resolution; a zone counts detections, a mask ignores movement. Each zone has a label filter, a kind (`alert` or `detection`) and an inertia in pictures and seconds.
* **Motion first:** the expensive detector runs only when enough of the picture, outside the masks, has changed.
* **A tracker:** each object keeps its identity between pictures, and what stands still (a parked car) is remembered and makes no new events.
* **Arming profiles:** `away`, `home` and the like choose which zones are watched; an unknown mode watches everything.
* **Events that only report:** an alert or a detection always carries `authorizes_action: false`; the server decides what to do.""",
      "role": r"""ARMOR-VISION is the part that decides what a camera's picture means, apart from any detector: the zones and masks drawn on it, the motion check that runs before the expensive detector, the tracker, the arming profiles and the rules that turn detections into events. [ARMOR-SERVER-AI](https://github.com/JuanenRac/ARMOR-SERVER-AI) is the service that watches the cameras today; ARMOR-VISION is where the rules for a real detection model are ready, waiting for it. It only reports: the events never authorise an action.

| Name | How | What for |
|---|---|---|
| ARMOR-SERVER-AI | same rules, once a model exists | Watches the cameras today |
| ARMOR-SERVER | `armor.vision.event/v1` | Decides what to do with an event (not part of the ARMOR-COMMON contract yet) |""",
      "architecture": r"""<p align="center">
  <img src="images/architecture.svg" alt="ARMOR-VISION architecture: who calls it, what it holds and what it depends on" width="100%">
</p>""",
      "security": r"""| Threat | Defence |
|---|---|
| The rule engine acts on its own | Every event carries `authorizes_action: false` (schema `armor.vision.event/v1`); the server decides |
| A wrong camera configuration | `check-config` lists every problem and one problem means nothing is accepted; coordinates are 0 to 1, a zone is `alert` or `detection`, unknown fields are errors |
| The costly detector runs for nothing | Motion comes first: the detector is asked only when enough cells of the 16 x 9 grid changed outside the masks |
| A parked car raises event after event | The tracker remembers what stands still (drift under 0.01 in 3 s) for 300 s and it makes no new events |
| An unknown arming mode | Every zone is watched; only `disarmed` without a profile silences the `alert` zones, and `detection` zones still record |

Nothing here is a safety function: there is no real detector model yet.""",
      "interfaces": r"""| Name | What it sets |
|---|---|
| `python -m armor_vision simulate [--config FILE] [--mode MODE]` | Runs a built-in scenario (a person crossing a driveway, a parked car, movement behind a masked tree) and prints one JSON line per event and a last line with the counters |
| `python -m armor_vision check-config FILE` | Validates a configuration and prints every problem; exit 0 good, 1 invalid, 2 unreadable |

```json
{"schema": "armor.vision.event/v1", "type": "alert", "camera_id": "cam-front", "zone_id": "drive",
 "zone_name": "Driveway", "track_id": 1, "label": "person", "confidence": 0.9,
 "box": [0.41, 0.62, 0.47, 0.82], "timestamp": 1.0, "authorizes_action": false}
```

As a library: `parse_config`, `Pipeline.process_detections` and `process_frame`. Asking `load_detector("tensorrt")` raises `DetectorUnavailable` because the model for the Jetson Orin NX is not written. See [docs/USAGE.md](docs/USAGE.md).""",
      "configuration": r"""| Name | What it sets |
|---|---|
| `motion_threshold` | 1 to 255: the grey difference that counts as change |
| `motion_min_cells` | How many cells of the 16 x 9 grid must change before the detector is asked |
| `zones[]` | `id`, `name`, `kind` (`alert` or `detection`), `labels`, `min_frames`, `min_seconds`, `points` (polygon, 0 to 1); counted by the feet of the box |
| `masks[]` | Polygons where movement is ignored; detections whose centre is inside are dropped |
| `profiles` | Which zones are watched in each arming mode (`away`, `home`, ...) |

| Limit | Value |
|---|---|
| Matching of a detection to a track (overlap / reach) | 0.3 / 1.0 |
| A moving track not seen is dropped after | 2 s |
| Stationary: window / drift / remembered for | 3 s / 0.01 / 300 s |
| Motion grid | 16 x 9 |

These values are constants of `tracker.py` and `motion.py` today; the configuration file holds the zones, masks, profiles and the motion thresholds.""",
      "quickstart": r"""**Requirements:** Python 3.11+ (standard library only).

```powershell
$env:PYTHONPATH = "src"
python -m armor_vision simulate --mode away
python -m armor_vision check-config my_cameras.json
python -m unittest discover -s tests   # 61 tests
```

```bash
PYTHONPATH=src python -m armor_vision simulate --mode away
PYTHONPATH=src python -m armor_vision check-config my_cameras.json
PYTHONPATH=src python -m unittest discover -s tests   # 61 tests
```""",
      "testing": r"""```powershell
$env:PYTHONPATH = "src"
python -m unittest discover -s tests
python -I tools/armor_ci_validate.py
```

| Test file | Tests | What it covers |
|---|---|---|
| `test_vision.py` | 42 | Geometry, configuration, motion, tracker, rules, profiles, the pipeline and the command line |
| `test_vision_edges.py` | 19 | The edges: bad configurations, stationary objects, masked detections and the unavailable detector |""",
      "build": "It is plain Python: nothing to compile. The version lives in `pyproject.toml` and `armor.project.json`.",
      "troubleshooting": r"""| You see | Because | Do |
|---|---|---|
| `check-config` exits with 1 | The configuration has problems; it lists each one | Fix them all: unknown fields are errors |
| `check-config` exits with 2 | The file cannot be read | Check the path and that it is JSON |
| `DetectorUnavailable` | `load_detector("tensorrt")`: the real model is not written | Use `ScriptedDetector` |
| A zone never fires | The feet are outside the polygon, the label is not accepted, a mask hides it, or the mode has no profile with that zone | Run `simulate` with the same file and mode |""",
      "structure": r"""<p align="center">
  <img src="images/repository-structure.svg" alt="Repository structure of ARMOR-VISION" width="100%">
</p>

<details>
<summary>Text version of the tree</summary>

```text
ARMOR-VISION/
├── src/armor_vision/
│   ├── geometry.py                      polygons on normalised coordinates
│   ├── config.py                        zones, masks, profiles and their validation
│   ├── motion.py                        the 16 x 9 motion check, masks ignored
│   ├── detector.py                      scripted detections; the real model is not written
│   ├── tracker.py                       identity between pictures; stationary objects
│   ├── rules.py                         zones to events: armor.vision.event/v1
│   └── pipeline.py cli.py __main__.py   the whole chain and the command line
├── tests/                               the tests
├── docs/                                the guides of this repository
├── tools/                               the shared CI checks and project tooling
├── .github/                             CI workflow, issue and pull-request templates
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

* There is no real detector model yet, and nothing has run on a camera or on the Jetson Orin NX: the simulation uses scripted detections.
* The event is not part of the ARMOR-COMMON contract yet.
* The tracker and motion values are constants in the code, not in the configuration file.

**Next**

* Write the detector model for the Jetson Orin NX and try it with a real camera.
* Move the tracker and motion constants to the configuration file and put the event in the ARMOR-COMMON contract.""",
    },
  },
  "es": {
    "tagline": "Zonas, máscaras y reglas de detección para las cámaras",
    "honest": "Las zonas, la comprobación de movimiento, el seguimiento, las reglas y los 61 tests son reales. **Todavía no existe un modelo de detección real** y nada se ha ejecutado en una cámara ni en la Jetson Orin NX: la simulación usa detecciones guionizadas.",
    "glance": [
      [
        "Función",
        "Zonas, máscaras y reglas de detección de cámaras (familia: Core Services, padre: ARMOR-SERVER)",
      ],
      [
        "Tecnología",
        "Python 3.11+, solo biblioteca estándar",
      ],
      [
        "Pruebas",
        "61 (`python -m unittest discover -s tests`)",
      ],
      [
        "Funciona en",
        "Cualquier ordenador",
      ],
      [
        "En hardware real",
        "Ninguno todavía: ni detector real, ni cámara ni Jetson (una simulación con detecciones guionizadas)",
      ],
      [
        "Licencia",
        "GPL-3.0-or-later",
      ],
    ],
    "status": {
      "software": "Las zonas, la comprobación de movimiento, el seguimiento y las reglas funcionan, pero aún no hay un modelo detector real: la simulación usa detecciones guionizadas.",
      "tests": "Pasan 61 pruebas (`python -m unittest discover -s tests`).",
      "hardware": "Nada ha funcionado en una cámara ni en la Jetson Orin NX.",
      "docs": "Ocho idiomas y el historial de cambios están al día.",
    },
    "docs": [
      "[Uso](docs/USAGE.md): las órdenes, la configuración, el evento y la biblioteca",
    ],
    "contributing_first": "Antes de un pull request ejecuta `python -m unittest discover -s tests` and `python -I tools/armor_ci_validate.py`: debe pasar. Consulta [CONTRIBUTING.md](CONTRIBUTING.md) y el [código de conducta](CODE_OF_CONDUCT.md).",
    "languages_extra": "",
    "body": {
      "overview": r"""* **Zonas y máscaras:** polígonos dibujados en coordenadas normalizadas (de 0 a 1), así un mismo dibujo vale a cualquier resolución; una zona cuenta detecciones, una máscara ignora el movimiento. Cada zona tiene un filtro de etiquetas, un tipo (`alert` o `detection`) y una inercia en fotogramas y segundos.
* **Primero el movimiento:** el detector, que es caro, solo se ejecuta cuando ha cambiado lo bastante de la imagen fuera de las máscaras.
* **Un seguimiento:** cada objeto conserva su identidad entre imágenes, y lo que está quieto (un coche aparcado) se recuerda y no genera eventos nuevos.
* **Perfiles de armado:** `away`, `home` y similares eligen qué zonas se vigilan; un modo desconocido vigila todo.
* **Eventos que solo informan:** una alerta o una detección lleva siempre `authorizes_action: false`; el servidor decide qué hacer.""",
      "role": r"""ARMOR-VISION es la parte que decide qué significa la imagen de una cámara, al margen de cualquier detector: las zonas y máscaras dibujadas sobre ella, la comprobación de movimiento que corre antes del detector costoso, el seguidor, los perfiles de armado y las reglas que convierten detecciones en eventos. [ARMOR-SERVER-AI](https://github.com/JuanenRac/ARMOR-SERVER-AI) es el servicio que vigila hoy las cámaras; ARMOR-VISION es donde las reglas para un modelo de detección real están listas, esperándolo. Solo informa: los eventos nunca autorizan una acción.

| Nombre | Cómo | Para qué |
|---|---|---|
| ARMOR-SERVER-AI | las mismas reglas, cuando haya un modelo | Vigila las cámaras hoy |
| ARMOR-SERVER | `armor.vision.event/v1` | Decide qué hacer con un evento (aún no forma parte del contrato de ARMOR-COMMON) |""",
      "architecture": r"""<p align="center">
  <img src="images/architecture.svg" alt="Arquitectura de ARMOR-VISION: quién lo llama, qué contiene y de qué depende" width="100%">
</p>""",
      "security": r"""| Amenaza | Defensa |
|---|---|
| El motor de reglas actúa por su cuenta | Todo evento lleva `authorizes_action: false` (esquema `armor.vision.event/v1`); decide el servidor |
| Una configuración de cámara errónea | `check-config` lista todos los problemas y uno solo impide aceptar nada; las coordenadas van de 0 a 1, una zona es `alert` o `detection`, los campos desconocidos son errores |
| El detector costoso se ejecuta sin motivo | Primero el movimiento: el detector solo se consulta si cambian suficientes celdas de la rejilla 16 x 9 fuera de las máscaras |
| Un coche aparcado genera evento tras evento | El seguimiento recuerda lo que está quieto (deriva menor de 0,01 en 3 s) durante 300 s y no genera eventos nuevos |
| Un modo de armado desconocido | Se vigilan todas las zonas; solo `disarmed` sin perfil silencia las zonas `alert` y las `detection` siguen registrando |

Nada de esto es una función de seguridad: aún no hay un modelo de detección real.""",
      "interfaces": r"""| Nombre | Qué define |
|---|---|
| `python -m armor_vision simulate [--config FILE] [--mode MODE]` | Ejecuta un escenario integrado (una persona cruza un camino, un coche aparcado, movimiento tras un árbol enmascarado) e imprime una línea JSON por evento y una última con los contadores |
| `python -m armor_vision check-config FILE` | Valida una configuración e imprime cada problema; salida 0 correcta, 1 inválida, 2 ilegible |

```json
{"schema": "armor.vision.event/v1", "type": "alert", "camera_id": "cam-front", "zone_id": "drive",
 "zone_name": "Driveway", "track_id": 1, "label": "person", "confidence": 0.9,
 "box": [0.41, 0.62, 0.47, 0.82], "timestamp": 1.0, "authorizes_action": false}
```

Como biblioteca: `parse_config`, `Pipeline.process_detections` y `process_frame`. Pedir `load_detector("tensorrt")` lanza `DetectorUnavailable` porque el modelo para la Jetson Orin NX no está escrito. Consulta [docs/USAGE.md](docs/USAGE.md).""",
      "configuration": r"""| Nombre | Qué define |
|---|---|
| `motion_threshold` | 1 a 255: la diferencia de gris que cuenta como cambio |
| `motion_min_cells` | Cuántas celdas de la rejilla 16 x 9 deben cambiar antes de consultar al detector |
| `zones[]` | `id`, `name`, `kind` (`alert` o `detection`), `labels`, `min_frames`, `min_seconds`, `points` (polígono, 0 a 1); se cuenta por los pies de la caja |
| `masks[]` | Polígonos donde se ignora el movimiento; se descartan las detecciones cuyo centro está dentro |
| `profiles` | Qué zonas se vigilan en cada modo de armado (`away`, `home`, ...) |

| Límite | Valor |
|---|---|
| Emparejado de una detección con una pista (solape / alcance) | 0.3 / 1.0 |
| Una pista en movimiento no vista se descarta tras | 2 s |
| Quieto: ventana / deriva / se recuerda durante | 3 s / 0.01 / 300 s |
| Rejilla de movimiento | 16 x 9 |

Hoy estos valores son constantes de `tracker.py` y `motion.py`; el fichero de configuración contiene las zonas, máscaras, perfiles y los umbrales de movimiento.""",
      "quickstart": r"""**Requisitos:** Python 3.11+ (solo biblioteca estándar).

```powershell
$env:PYTHONPATH = "src"
python -m armor_vision simulate --mode away
python -m armor_vision check-config my_cameras.json
python -m unittest discover -s tests   # 61 tests
```

```bash
PYTHONPATH=src python -m armor_vision simulate --mode away
PYTHONPATH=src python -m armor_vision check-config my_cameras.json
PYTHONPATH=src python -m unittest discover -s tests   # 61 tests
```""",
      "testing": r"""```powershell
$env:PYTHONPATH = "src"
python -m unittest discover -s tests
python -I tools/armor_ci_validate.py
```

| Fichero de pruebas | Pruebas | Qué cubre |
|---|---|---|
| `test_vision.py` | 42 | Geometría, configuración, movimiento, seguimiento, reglas, perfiles, la cadena y la línea de órdenes |
| `test_vision_edges.py` | 19 | Los bordes: configuraciones erróneas, objetos quietos, detecciones enmascaradas y el detector no disponible |""",
      "build": "Es Python puro: no hay nada que compilar. La versión vive en `pyproject.toml` y `armor.project.json`.",
      "troubleshooting": r"""| Ves | Porque | Haz |
|---|---|---|
| `check-config` termina con 1 | La configuración tiene problemas; los lista todos | Corrígelos todos: los campos desconocidos son errores |
| `check-config` termina con 2 | No se puede leer el fichero | Comprueba la ruta y que sea JSON |
| `DetectorUnavailable` | `load_detector("tensorrt")`: el modelo real no está escrito | Usa `ScriptedDetector` |
| Una zona nunca salta | Los pies están fuera del polígono, la etiqueta no se acepta, una máscara la oculta, o el modo no tiene un perfil con esa zona | Ejecuta `simulate` con el mismo fichero y modo |""",
      "structure": r"""<p align="center">
  <img src="images/repository-structure.svg" alt="Estructura del repositorio de ARMOR-VISION" width="100%">
</p>

<details>
<summary>Versión en texto del árbol</summary>

```text
ARMOR-VISION/
├── src/armor_vision/
│   ├── geometry.py                      polígonos en coordenadas normalizadas
│   ├── config.py                        zonas, máscaras, perfiles y su validación
│   ├── motion.py                        la comprobación de movimiento 16 x 9, máscaras ignoradas
│   ├── detector.py                      detecciones guionizadas; el modelo real no está escrito
│   ├── tracker.py                       identidad entre imágenes; objetos quietos
│   ├── rules.py                         de zonas a eventos: armor.vision.event/v1
│   └── pipeline.py cli.py __main__.py   toda la cadena y la línea de órdenes
├── tests/                               las pruebas
├── docs/                                las guías de este repositorio
├── tools/                               las comprobaciones de CI compartidas y las herramientas del proyecto
├── .github/                             flujo de CI y plantillas de issues y pull requests
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

* Aún no hay un modelo de detección real y nada se ha ejecutado en una cámara ni en la Jetson Orin NX: la simulación usa detecciones guionizadas.
* El evento aún no forma parte del contrato de ARMOR-COMMON.
* Los valores del seguimiento y del movimiento son constantes del código, no del fichero de configuración.

**Lo siguiente**

* Escribir el modelo de detección para la Jetson Orin NX y probarlo con una cámara real.
* Pasar las constantes de seguimiento y movimiento al fichero de configuración y meter el evento en el contrato de ARMOR-COMMON.""",
    },
  },
  "de": {
    "tagline": "Zonen, Masken und Erkennungsregeln für die Kameras",
    "honest": "Die Zonen, die Bewegungsprüfung, die Verfolgung, die Regeln und die 61 Tests sind real. Es gibt **noch kein echtes Erkennungsmodell**, und nichts lief auf einer Kamera oder auf dem Jetson Orin NX: die Simulation nutzt vorgegebene Erkennungen.",
    "glance": [
      [
        "Rolle",
        "Kamerazonen, Masken und Erkennungsregeln (Familie: Core Services, übergeordnet: ARMOR-SERVER)",
      ],
      [
        "Technik",
        "Python 3.11+, nur Standardbibliothek",
      ],
      [
        "Tests",
        "61 (`python -m unittest discover -s tests`)",
      ],
      [
        "Läuft auf",
        "Jeder Computer",
      ],
      [
        "Auf echter Hardware",
        "Noch keiner: weder echter Detektor noch Kamera noch Jetson (eine Simulation mit geskripteten Erkennungen)",
      ],
      [
        "Lizenz",
        "GPL-3.0-or-later",
      ],
    ],
    "status": {
      "software": "Die Zonen, die Bewegungsprüfung, die Verfolgung und die Regeln funktionieren, aber es gibt noch kein echtes Erkennungsmodell: Die Simulation nutzt geskriptete Erkennungen.",
      "tests": "61 Tests bestehen (`python -m unittest discover -s tests`).",
      "hardware": "Nichts lief an einer Kamera oder auf dem Jetson Orin NX.",
      "docs": "Acht Sprachen und das Änderungsprotokoll sind aktuell.",
    },
    "docs": [
      "[Verwendung](docs/USAGE.md): die Befehle, die Konfiguration, das Ereignis und die Bibliothek",
    ],
    "contributing_first": "Führe vor einem Pull Request `python -m unittest discover -s tests` and `python -I tools/armor_ci_validate.py` aus: Es muss bestehen. Siehe [CONTRIBUTING.md](CONTRIBUTING.md) und den [Verhaltenskodex](CODE_OF_CONDUCT.md).",
    "languages_extra": "",
    "body": {
      "overview": r"""* **Zonen und Masken:** Polygone in normalisierten Koordinaten (0 bis 1), eine Zeichnung gilt also bei jeder Auflösung; eine Zone zählt Erkennungen, eine Maske ignoriert Bewegung. Jede Zone hat einen Label-Filter, eine Art (`alert` oder `detection`) und eine Trägheit in Bildern und Sekunden.
* **Zuerst die Bewegung:** der teure Detektor läuft nur, wenn sich außerhalb der Masken genug vom Bild verändert hat.
* **Eine Verfolgung:** jedes Objekt behält seine Identität von Bild zu Bild, und was stillsteht (ein geparktes Auto), wird gemerkt und erzeugt keine neuen Ereignisse.
* **Scharfschaltprofile:** `away`, `home` und ähnliche wählen, welche Zonen überwacht werden; ein unbekannter Modus überwacht alles.
* **Ereignisse, die nur melden:** ein Alarm oder eine Erkennung trägt immer `authorizes_action: false`; der Server entscheidet, was zu tun ist.""",
      "role": r"""ARMOR-VISION ist der Teil, der entscheidet, was das Bild einer Kamera bedeutet, unabhängig von jedem Detektor: die darauf gezeichneten Zonen und Masken, die Bewegungsprüfung, die vor dem teuren Detektor läuft, der Tracker, die Scharfschaltprofile und die Regeln, die Erkennungen zu Ereignissen machen. [ARMOR-SERVER-AI](https://github.com/JuanenRac/ARMOR-SERVER-AI) ist der Dienst, der heute die Kameras beobachtet; ARMOR-VISION ist der Ort, an dem die Regeln für ein echtes Erkennungsmodell bereitliegen und darauf warten. Es meldet nur: Die Ereignisse autorisieren nie eine Aktion.

| Name | Wie | Wozu |
|---|---|---|
| ARMOR-SERVER-AI | dieselben Regeln, sobald es ein Modell gibt | Überwacht heute die Kameras |
| ARMOR-SERVER | `armor.vision.event/v1` | Entscheidet, was mit einem Ereignis geschieht (noch nicht Teil des ARMOR-COMMON-Vertrags) |""",
      "architecture": r"""<p align="center">
  <img src="images/architecture.svg" alt="Architektur von ARMOR-VISION: wer es aufruft, was es enthält und wovon es abhängt" width="100%">
</p>""",
      "security": r"""| Bedrohung | Abwehr |
|---|---|
| Die Regelmaschine handelt auf eigene Faust | Jedes Ereignis trägt `authorizes_action: false` (Schema `armor.vision.event/v1`); der Server entscheidet |
| Eine falsche Kamerakonfiguration | `check-config` listet jedes Problem auf, und ein Problem bedeutet, dass nichts akzeptiert wird; Koordinaten liegen zwischen 0 und 1, eine Zone ist `alert` oder `detection`, unbekannte Felder sind Fehler |
| Der teure Detektor läuft ohne Grund | Erst die Bewegung: Der Detektor wird nur gefragt, wenn genug Zellen des 16-x-9-Rasters außerhalb der Masken wechseln |
| Ein geparktes Auto löst Ereignis um Ereignis aus | Der Tracker merkt sich Ruhendes (Drift unter 0,01 in 3 s) 300 s lang, es gibt keine neuen Ereignisse |
| Ein unbekannter Scharfschaltmodus | Alle Zonen werden überwacht; nur `disarmed` ohne Profil schaltet die `alert`-Zonen stumm, `detection`-Zonen zeichnen weiter auf |

Nichts davon ist eine Sicherheitsfunktion: Es gibt noch kein echtes Erkennungsmodell.""",
      "interfaces": r"""| Name | Was sie festlegt |
|---|---|
| `python -m armor_vision simulate [--config FILE] [--mode MODE]` | Führt ein eingebautes Szenario aus (eine Person quert eine Einfahrt, ein geparktes Auto, Bewegung hinter einem maskierten Baum) und druckt je Ereignis eine JSON-Zeile und zuletzt die Zähler |
| `python -m armor_vision check-config FILE` | Prüft eine Konfiguration und druckt jedes Problem; Exit 0 gut, 1 ungültig, 2 nicht lesbar |

```json
{"schema": "armor.vision.event/v1", "type": "alert", "camera_id": "cam-front", "zone_id": "drive",
 "zone_name": "Driveway", "track_id": 1, "label": "person", "confidence": 0.9,
 "box": [0.41, 0.62, 0.47, 0.82], "timestamp": 1.0, "authorizes_action": false}
```

Als Bibliothek: `parse_config`, `Pipeline.process_detections` und `process_frame`. `load_detector("tensorrt")` löst `DetectorUnavailable` aus, weil das Modell für den Jetson Orin NX nicht geschrieben ist. Siehe [docs/USAGE.md](docs/USAGE.md).""",
      "configuration": r"""| Name | Was sie festlegt |
|---|---|
| `motion_threshold` | 1 bis 255: der Graustufenunterschied, der als Änderung zählt |
| `motion_min_cells` | Wie viele Zellen des 16-x-9-Rasters wechseln müssen, bevor der Detektor gefragt wird |
| `zones[]` | `id`, `name`, `kind` (`alert` oder `detection`), `labels`, `min_frames`, `min_seconds`, `points` (Polygon, 0 bis 1); gezählt wird an den Füßen der Box |
| `masks[]` | Polygone, in denen Bewegung ignoriert wird; Erkennungen mit Mittelpunkt darin entfallen |
| `profiles` | Welche Zonen in jedem Scharfschaltmodus überwacht werden (`away`, `home`, ...) |

| Grenze | Wert |
|---|---|
| Zuordnung einer Erkennung zu einer Spur (Überlappung / Reichweite) | 0.3 / 1.0 |
| Eine bewegte, nicht gesehene Spur entfällt nach | 2 s |
| Ruhend: Fenster / Drift / gemerkt für | 3 s / 0.01 / 300 s |
| Bewegungsraster | 16 x 9 |

Diese Werte sind heute Konstanten in `tracker.py` und `motion.py`; die Konfigurationsdatei enthält Zonen, Masken, Profile und die Bewegungsschwellen.""",
      "quickstart": r"""**Voraussetzungen:** Python 3.11+ (nur Standardbibliothek).

```powershell
$env:PYTHONPATH = "src"
python -m armor_vision simulate --mode away
python -m armor_vision check-config my_cameras.json
python -m unittest discover -s tests   # 61 tests
```

```bash
PYTHONPATH=src python -m armor_vision simulate --mode away
PYTHONPATH=src python -m armor_vision check-config my_cameras.json
PYTHONPATH=src python -m unittest discover -s tests   # 61 tests
```""",
      "testing": r"""```powershell
$env:PYTHONPATH = "src"
python -m unittest discover -s tests
python -I tools/armor_ci_validate.py
```

| Testdatei | Tests | Was sie abdeckt |
|---|---|---|
| `test_vision.py` | 42 | Geometrie, Konfiguration, Bewegung, Tracker, Regeln, Profile, die Kette und die Kommandozeile |
| `test_vision_edges.py` | 19 | Die Grenzfälle: falsche Konfigurationen, ruhende Objekte, maskierte Erkennungen und der nicht verfügbare Detektor |""",
      "build": "Es ist reines Python: nichts zu kompilieren. Die Version steht in `pyproject.toml` und `armor.project.json`.",
      "troubleshooting": r"""| Sie sehen | Weil | Tun Sie |
|---|---|---|
| `check-config` endet mit 1 | Die Konfiguration hat Probleme; es listet jedes auf | Behebe alle: Unbekannte Felder sind Fehler |
| `check-config` endet mit 2 | Die Datei kann nicht gelesen werden | Prüfe den Pfad und dass es JSON ist |
| `DetectorUnavailable` | `load_detector("tensorrt")`: Das echte Modell fehlt | Nutze `ScriptedDetector` |
| Eine Zone löst nie aus | Die Füße liegen außerhalb, das Label wird nicht akzeptiert, eine Maske verdeckt sie, oder der Modus hat kein Profil mit dieser Zone | Starte `simulate` mit derselben Datei und demselben Modus |""",
      "structure": r"""<p align="center">
  <img src="images/repository-structure.svg" alt="Repository-Struktur von ARMOR-VISION" width="100%">
</p>

<details>
<summary>Textversion des Baums</summary>

```text
ARMOR-VISION/
├── src/armor_vision/
│   ├── geometry.py                      Polygone in normalisierten Koordinaten
│   ├── config.py                        Zonen, Masken, Profile und ihre Prüfung
│   ├── motion.py                        die 16-x-9-Bewegungsprüfung ohne Masken
│   ├── detector.py                      geskriptete Erkennungen; das echte Modell fehlt
│   ├── tracker.py                       Identität zwischen Bildern; ruhende Objekte
│   ├── rules.py                         von Zonen zu Ereignissen: armor.vision.event/v1
│   └── pipeline.py cli.py __main__.py   die ganze Kette und die Kommandozeile
├── tests/                               die Tests
├── docs/                                die Anleitungen dieses Repositorys
├── tools/                               die gemeinsamen CI-Prüfungen und Projektwerkzeuge
├── .github/                             CI-Workflow sowie Vorlagen für Issues und Pull Requests
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

* Es gibt noch kein echtes Erkennungsmodell, und nichts lief auf einer Kamera oder dem Jetson Orin NX: Die Simulation nutzt geskriptete Erkennungen.
* Das Ereignis ist noch nicht Teil des ARMOR-COMMON-Vertrags.
* Die Werte von Tracker und Bewegung sind Konstanten im Code, nicht in der Konfigurationsdatei.

**Als Nächstes**

* Das Erkennungsmodell für den Jetson Orin NX schreiben und mit einer echten Kamera erproben.
* Die Konstanten von Tracker und Bewegung in die Konfigurationsdatei verlegen und das Ereignis in den ARMOR-COMMON-Vertrag aufnehmen.""",
    },
  },
  "fr": {
    "tagline": "Zones, masques et règles de détection pour les caméras",
    "honest": "Les zones, le contrôle du mouvement, le suivi, les règles et les 61 tests sont réels. **Il n'existe pas encore de vrai modèle de détection** et rien n'a tourné sur une caméra ni sur la Jetson Orin NX : la simulation utilise des détections scénarisées.",
    "glance": [
      [
        "Rôle",
        "Zones, masques et règles de détection des caméras (famille : Core Services, parent : ARMOR-SERVER)",
      ],
      [
        "Technologie",
        "Python 3.11+, bibliothèque standard uniquement",
      ],
      [
        "Tests",
        "61 (`python -m unittest discover -s tests`)",
      ],
      [
        "Fonctionne sur",
        "N'importe quel ordinateur",
      ],
      [
        "Sur matériel réel",
        "Aucun pour l'instant : ni détecteur réel, ni caméra, ni Jetson (une simulation avec des détections scriptées)",
      ],
      [
        "Licence",
        "GPL-3.0-or-later",
      ],
    ],
    "status": {
      "software": "Les zones, le contrôle du mouvement, le suivi et les règles fonctionnent, mais il n'y a pas encore de vrai modèle détecteur : la simulation utilise des détections scénarisées.",
      "tests": "61 tests réussissent (`python -m unittest discover -s tests`).",
      "hardware": "Rien n'a tourné sur une caméra ni sur le Jetson Orin NX.",
      "docs": "Huit langues et le journal des modifications sont à jour.",
    },
    "docs": [
      "[Utilisation](docs/USAGE.md) : les commandes, la configuration, l'événement et la bibliothèque",
    ],
    "contributing_first": "Avant une pull request, lancez `python -m unittest discover -s tests` and `python -I tools/armor_ci_validate.py` : il doit réussir. Voir [CONTRIBUTING.md](CONTRIBUTING.md) et le [code de conduite](CODE_OF_CONDUCT.md).",
    "languages_extra": "",
    "body": {
      "overview": r"""* **Zones et masques :** des polygones dessinés en coordonnées normalisées (de 0 à 1), un même dessin sert donc à toute résolution ; une zone compte les détections, un masque ignore le mouvement. Chaque zone a un filtre d'étiquettes, un type (`alert` ou `detection`) et une inertie en images et en secondes.
* **D'abord le mouvement :** le détecteur, coûteux, ne s'exécute que lorsque assez de l'image a changé en dehors des masques.
* **Un suivi :** chaque objet garde son identité d'une image à l'autre, et ce qui reste immobile (une voiture garée) est mémorisé et ne produit pas de nouveaux événements.
* **Profils d'armement :** `away`, `home` et similaires choisissent les zones surveillées ; un mode inconnu surveille tout.
* **Des événements qui informent seulement :** une alerte ou une détection porte toujours `authorizes_action: false` ; le serveur décide quoi faire.""",
      "role": r"""ARMOR-VISION est la partie qui décide de ce que signifie l'image d'une caméra, indépendamment de tout détecteur : les zones et masques dessinés dessus, le contrôle de mouvement qui s'exécute avant le détecteur coûteux, le suiveur, les profils d'armement et les règles qui transforment des détections en événements. [ARMOR-SERVER-AI](https://github.com/JuanenRac/ARMOR-SERVER-AI) est le service qui surveille les caméras aujourd'hui ; ARMOR-VISION est l'endroit où les règles pour un vrai modèle de détection sont prêtes, en l'attendant. Il ne fait que rapporter : les événements n'autorisent jamais une action.

| Nom | Comment | À quoi ça sert |
|---|---|---|
| ARMOR-SERVER-AI | les mêmes règles, dès qu'un modèle existe | Surveille les caméras aujourd'hui |
| ARMOR-SERVER | `armor.vision.event/v1` | Décide quoi faire d'un événement (pas encore dans le contrat d'ARMOR-COMMON) |""",
      "architecture": r"""<p align="center">
  <img src="images/architecture.svg" alt="Architecture de ARMOR-VISION : qui l'appelle, ce qu'il contient et de quoi il dépend" width="100%">
</p>""",
      "security": r"""| Menace | Défense |
|---|---|
| Le moteur de règles agit de lui-même | Chaque événement porte `authorizes_action: false` (schéma `armor.vision.event/v1`) ; le serveur décide |
| Une mauvaise configuration de caméra | `check-config` liste chaque problème et un seul problème fait tout refuser ; les coordonnées vont de 0 à 1, une zone est `alert` ou `detection`, les champs inconnus sont des erreurs |
| Le détecteur coûteux tourne pour rien | Le mouvement d'abord : le détecteur n'est sollicité que si assez de cellules de la grille 16 x 9 changent hors des masques |
| Une voiture garée déclenche événement sur événement | Le suivi mémorise ce qui est immobile (dérive sous 0,01 en 3 s) pendant 300 s sans nouvel événement |
| Un mode d'armement inconnu | Toutes les zones sont surveillées ; seul `disarmed` sans profil réduit au silence les zones `alert`, les zones `detection` enregistrent encore |

Rien ici n'est une fonction de sécurité : il n'y a pas encore de vrai modèle de détection.""",
      "interfaces": r"""| Nom | Ce qu'elle règle |
|---|---|
| `python -m armor_vision simulate [--config FILE] [--mode MODE]` | Exécute un scénario intégré (une personne traverse une allée, une voiture garée, un mouvement derrière un arbre masqué) et imprime une ligne JSON par événement puis une ligne de compteurs |
| `python -m armor_vision check-config FILE` | Valide une configuration et imprime chaque problème ; sortie 0 bonne, 1 invalide, 2 illisible |

```json
{"schema": "armor.vision.event/v1", "type": "alert", "camera_id": "cam-front", "zone_id": "drive",
 "zone_name": "Driveway", "track_id": 1, "label": "person", "confidence": 0.9,
 "box": [0.41, 0.62, 0.47, 0.82], "timestamp": 1.0, "authorizes_action": false}
```

En bibliothèque : `parse_config`, `Pipeline.process_detections` et `process_frame`. `load_detector("tensorrt")` lève `DetectorUnavailable` car le modèle pour le Jetson Orin NX n'est pas écrit. Voir [docs/USAGE.md](docs/USAGE.md).""",
      "configuration": r"""| Nom | Ce qu'elle règle |
|---|---|
| `motion_threshold` | 1 à 255 : l'écart de gris qui compte comme changement |
| `motion_min_cells` | Combien de cellules de la grille 16 x 9 doivent changer avant de solliciter le détecteur |
| `zones[]` | `id`, `name`, `kind` (`alert` ou `detection`), `labels`, `min_frames`, `min_seconds`, `points` (polygone, 0 à 1) ; compté par les pieds de la boîte |
| `masks[]` | Polygones où le mouvement est ignoré ; les détections dont le centre est dedans sont écartées |
| `profiles` | Quelles zones sont surveillées dans chaque mode d'armement (`away`, `home`, ...) |

| Limite | Valeur |
|---|---|
| Appariement d'une détection à une piste (recouvrement / portée) | 0.3 / 1.0 |
| Une piste en mouvement non vue est abandonnée après | 2 s |
| Immobile : fenêtre / dérive / mémorisé pendant | 3 s / 0.01 / 300 s |
| Grille de mouvement | 16 x 9 |

Ces valeurs sont aujourd'hui des constantes de `tracker.py` et `motion.py` ; le fichier de configuration contient les zones, masques, profils et seuils de mouvement.""",
      "quickstart": r"""**Prérequis:** Python 3.11+ (bibliothèque standard uniquement).

```powershell
$env:PYTHONPATH = "src"
python -m armor_vision simulate --mode away
python -m armor_vision check-config my_cameras.json
python -m unittest discover -s tests   # 61 tests
```

```bash
PYTHONPATH=src python -m armor_vision simulate --mode away
PYTHONPATH=src python -m armor_vision check-config my_cameras.json
PYTHONPATH=src python -m unittest discover -s tests   # 61 tests
```""",
      "testing": r"""```powershell
$env:PYTHONPATH = "src"
python -m unittest discover -s tests
python -I tools/armor_ci_validate.py
```

| Fichier de tests | Tests | Ce qu'il couvre |
|---|---|---|
| `test_vision.py` | 42 | Géométrie, configuration, mouvement, suivi, règles, profils, la chaîne et la ligne de commande |
| `test_vision_edges.py` | 19 | Les cas limites : mauvaises configurations, objets immobiles, détections masquées et détecteur indisponible |""",
      "build": "C'est du Python pur : rien à compiler. La version est dans `pyproject.toml` et `armor.project.json`.",
      "troubleshooting": r"""| Vous voyez | Parce que | Faites |
|---|---|---|
| `check-config` se termine par 1 | La configuration a des problèmes ; il les liste tous | Corrigez-les tous : les champs inconnus sont des erreurs |
| `check-config` se termine par 2 | Le fichier est illisible | Vérifiez le chemin et que c'est du JSON |
| `DetectorUnavailable` | `load_detector("tensorrt")` : le vrai modèle n'est pas écrit | Utilisez `ScriptedDetector` |
| Une zone ne se déclenche jamais | Les pieds sont hors du polygone, l'étiquette n'est pas acceptée, un masque la cache, ou le mode n'a pas de profil avec cette zone | Lancez `simulate` avec le même fichier et mode |""",
      "structure": r"""<p align="center">
  <img src="images/repository-structure.svg" alt="Structure du dépôt de ARMOR-VISION" width="100%">
</p>

<details>
<summary>Version texte de l'arborescence</summary>

```text
ARMOR-VISION/
├── src/armor_vision/
│   ├── geometry.py                      polygones en coordonnées normalisées
│   ├── config.py                        zones, masques, profils et leur validation
│   ├── motion.py                        le contrôle de mouvement 16 x 9, masques ignorés
│   ├── detector.py                      détections scriptées ; le vrai modèle n'est pas écrit
│   ├── tracker.py                       identité entre images ; objets immobiles
│   ├── rules.py                         des zones aux événements : armor.vision.event/v1
│   └── pipeline.py cli.py __main__.py   toute la chaîne et la ligne de commande
├── tests/                               les tests
├── docs/                                les guides de ce dépôt
├── tools/                               les contrôles CI partagés et les outils du projet
├── .github/                             workflow CI et modèles d'issues et de pull requests
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

* Il n'y a pas encore de vrai modèle de détection et rien n'a tourné sur une caméra ni sur le Jetson Orin NX : la simulation utilise des détections scriptées.
* L'événement ne fait pas encore partie du contrat d'ARMOR-COMMON.
* Les valeurs du suivi et du mouvement sont des constantes du code, pas du fichier de configuration.

**Ensuite**

* Écrire le modèle de détection pour le Jetson Orin NX et l'essayer avec une vraie caméra.
* Déplacer les constantes du suivi et du mouvement dans le fichier de configuration et mettre l'événement dans le contrat d'ARMOR-COMMON.""",
    },
  },
  "it": {
    "tagline": "Zone, maschere e regole di rilevamento per le telecamere",
    "honest": "Le zone, il controllo del movimento, il tracciamento, le regole e i 61 test sono reali. **Non esiste ancora un vero modello di rilevamento** e nulla è stato eseguito su una telecamera o sulla Jetson Orin NX: la simulazione usa rilevamenti scriptati.",
    "glance": [
      [
        "Ruolo",
        "Zone, maschere e regole di rilevamento delle telecamere (famiglia: Core Services, padre: ARMOR-SERVER)",
      ],
      [
        "Tecnologia",
        "Python 3.11+, solo libreria standard",
      ],
      [
        "Test",
        "61 (`python -m unittest discover -s tests`)",
      ],
      [
        "Gira su",
        "Qualsiasi computer",
      ],
      [
        "Su hardware reale",
        "Ancora nessuno: né rilevatore reale, né telecamera, né Jetson (una simulazione con rilevamenti scriptati)",
      ],
      [
        "Licenza",
        "GPL-3.0-or-later",
      ],
    ],
    "status": {
      "software": "Le zone, il controllo del movimento, il tracciamento e le regole funzionano, ma non c'è ancora un vero modello di rilevamento: la simulazione usa rilevamenti da script.",
      "tests": "Superano 61 test (`python -m unittest discover -s tests`).",
      "hardware": "Nulla ha girato su una telecamera né sulla Jetson Orin NX.",
      "docs": "Otto lingue e il registro delle modifiche sono aggiornati.",
    },
    "docs": [
      "[Uso](docs/USAGE.md): i comandi, la configurazione, l'evento e la libreria",
    ],
    "contributing_first": "Prima di una pull request esegui `python -m unittest discover -s tests` and `python -I tools/armor_ci_validate.py`: deve passare. Vedi [CONTRIBUTING.md](CONTRIBUTING.md) e il [codice di condotta](CODE_OF_CONDUCT.md).",
    "languages_extra": "",
    "body": {
      "overview": r"""* **Zone e maschere:** poligoni disegnati in coordinate normalizzate (da 0 a 1), così lo stesso disegno vale a qualsiasi risoluzione; una zona conta i rilevamenti, una maschera ignora il movimento. Ogni zona ha un filtro di etichette, un tipo (`alert` o `detection`) e un'inerzia in immagini e secondi.
* **Prima il movimento:** il rilevatore, costoso, viene eseguito solo quando è cambiata abbastanza immagine fuori dalle maschere.
* **Un tracciamento:** ogni oggetto mantiene la sua identità da un'immagine all'altra, e ciò che sta fermo (un'auto parcheggiata) viene ricordato e non genera nuovi eventi.
* **Profili di inserimento:** `away`, `home` e simili scelgono quali zone sono sorvegliate; una modalità sconosciuta sorveglia tutto.
* **Eventi che informano soltanto:** un allarme o un rilevamento porta sempre `authorizes_action: false`; il server decide cosa fare.""",
      "role": r"""ARMOR-VISION è la parte che decide cosa significa l'immagine di una telecamera, a prescindere da qualsiasi rilevatore: le zone e le maschere disegnate su di essa, il controllo di movimento che gira prima del rilevatore costoso, il tracker, i profili di inserimento e le regole che trasformano i rilevamenti in eventi. [ARMOR-SERVER-AI](https://github.com/JuanenRac/ARMOR-SERVER-AI) è il servizio che oggi sorveglia le telecamere; ARMOR-VISION è dove le regole per un vero modello di rilevamento sono pronte, in attesa. Si limita a riferire: gli eventi non autorizzano mai un'azione.

| Nome | Come | A cosa serve |
|---|---|---|
| ARMOR-SERVER-AI | le stesse regole, quando ci sarà un modello | Oggi sorveglia le telecamere |
| ARMOR-SERVER | `armor.vision.event/v1` | Decide cosa fare di un evento (non ancora nel contratto di ARMOR-COMMON) |""",
      "architecture": r"""<p align="center">
  <img src="images/architecture.svg" alt="Architettura di ARMOR-VISION: chi lo chiama, cosa contiene e da cosa dipende" width="100%">
</p>""",
      "security": r"""| Minaccia | Difesa |
|---|---|
| Il motore di regole agisce da solo | Ogni evento porta `authorizes_action: false` (schema `armor.vision.event/v1`); decide il server |
| Una configurazione di telecamera errata | `check-config` elenca ogni problema e uno solo basta a non accettare nulla; le coordinate vanno da 0 a 1, una zona è `alert` o `detection`, i campi sconosciuti sono errori |
| Il rilevatore costoso gira senza motivo | Prima il movimento: il rilevatore è interpellato solo se cambiano abbastanza celle della griglia 16 x 9 fuori dalle maschere |
| Un'auto parcheggiata genera un evento dopo l'altro | Il tracker ricorda ciò che è fermo (deriva sotto 0,01 in 3 s) per 300 s e non genera nuovi eventi |
| Una modalità di inserimento sconosciuta | Si sorvegliano tutte le zone; solo `disarmed` senza profilo mette a tacere le zone `alert` e le `detection` registrano ancora |

Nulla qui è una funzione di sicurezza: non esiste ancora un vero modello di rilevamento.""",
      "interfaces": r"""| Nome | Cosa imposta |
|---|---|
| `python -m armor_vision simulate [--config FILE] [--mode MODE]` | Esegue uno scenario integrato (una persona attraversa un vialetto, un'auto parcheggiata, movimento dietro un albero mascherato) e stampa una riga JSON per evento e una finale con i contatori |
| `python -m armor_vision check-config FILE` | Valida una configurazione e stampa ogni problema; uscita 0 buona, 1 non valida, 2 illeggibile |

```json
{"schema": "armor.vision.event/v1", "type": "alert", "camera_id": "cam-front", "zone_id": "drive",
 "zone_name": "Driveway", "track_id": 1, "label": "person", "confidence": 0.9,
 "box": [0.41, 0.62, 0.47, 0.82], "timestamp": 1.0, "authorizes_action": false}
```

Come libreria: `parse_config`, `Pipeline.process_detections` e `process_frame`. `load_detector("tensorrt")` solleva `DetectorUnavailable` perché il modello per il Jetson Orin NX non è scritto. Vedi [docs/USAGE.md](docs/USAGE.md).""",
      "configuration": r"""| Nome | Cosa imposta |
|---|---|
| `motion_threshold` | da 1 a 255: la differenza di grigio che conta come cambiamento |
| `motion_min_cells` | Quante celle della griglia 16 x 9 devono cambiare prima di interpellare il rilevatore |
| `zones[]` | `id`, `name`, `kind` (`alert` o `detection`), `labels`, `min_frames`, `min_seconds`, `points` (poligono, da 0 a 1); si conta dai piedi del riquadro |
| `masks[]` | Poligoni dove il movimento è ignorato; i rilevamenti con il centro all'interno vengono scartati |
| `profiles` | Quali zone sono sorvegliate in ogni modalità di inserimento (`away`, `home`, ...) |

| Limite | Valore |
|---|---|
| Abbinamento di un rilevamento a una traccia (sovrapposizione / portata) | 0.3 / 1.0 |
| Una traccia in movimento non vista viene scartata dopo | 2 s |
| Fermo: finestra / deriva / ricordato per | 3 s / 0.01 / 300 s |
| Griglia di movimento | 16 x 9 |

Oggi questi valori sono costanti di `tracker.py` e `motion.py`; il file di configurazione contiene zone, maschere, profili e soglie di movimento.""",
      "quickstart": r"""**Requisiti:** Python 3.11+ (solo libreria standard).

```powershell
$env:PYTHONPATH = "src"
python -m armor_vision simulate --mode away
python -m armor_vision check-config my_cameras.json
python -m unittest discover -s tests   # 61 tests
```

```bash
PYTHONPATH=src python -m armor_vision simulate --mode away
PYTHONPATH=src python -m armor_vision check-config my_cameras.json
PYTHONPATH=src python -m unittest discover -s tests   # 61 tests
```""",
      "testing": r"""```powershell
$env:PYTHONPATH = "src"
python -m unittest discover -s tests
python -I tools/armor_ci_validate.py
```

| File di test | Test | Cosa copre |
|---|---|---|
| `test_vision.py` | 42 | Geometria, configurazione, movimento, tracker, regole, profili, la catena e la riga di comando |
| `test_vision_edges.py` | 19 | I casi limite: configurazioni errate, oggetti fermi, rilevamenti mascherati e rilevatore non disponibile |""",
      "build": "È Python puro: nulla da compilare. La versione sta in `pyproject.toml` e `armor.project.json`.",
      "troubleshooting": r"""| Vedi | Perché | Fai |
|---|---|---|
| `check-config` termina con 1 | La configurazione ha problemi; li elenca tutti | Correggili tutti: i campi sconosciuti sono errori |
| `check-config` termina con 2 | Il file non può essere letto | Controlla il percorso e che sia JSON |
| `DetectorUnavailable` | `load_detector("tensorrt")`: il modello reale non è scritto | Usa `ScriptedDetector` |
| Una zona non scatta mai | I piedi sono fuori dal poligono, l'etichetta non è accettata, una maschera la nasconde, o la modalità non ha un profilo con quella zona | Esegui `simulate` con lo stesso file e modalità |""",
      "structure": r"""<p align="center">
  <img src="images/repository-structure.svg" alt="Struttura del repository di ARMOR-VISION" width="100%">
</p>

<details>
<summary>Versione testuale dell'albero</summary>

```text
ARMOR-VISION/
├── src/armor_vision/
│   ├── geometry.py                      poligoni in coordinate normalizzate
│   ├── config.py                        zone, maschere, profili e la loro validazione
│   ├── motion.py                        il controllo del movimento 16 x 9, maschere ignorate
│   ├── detector.py                      rilevamenti scriptati; il modello reale non c'è
│   ├── tracker.py                       identità tra immagini; oggetti fermi
│   ├── rules.py                         dalle zone agli eventi: armor.vision.event/v1
│   └── pipeline.py cli.py __main__.py   tutta la catena e la riga di comando
├── tests/                               i test
├── docs/                                le guide di questo repository
├── tools/                               i controlli CI condivisi e gli strumenti del progetto
├── .github/                             workflow CI e modelli per issue e pull request
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

* Non esiste ancora un vero modello di rilevamento e nulla ha girato su una telecamera né sul Jetson Orin NX: la simulazione usa rilevamenti scriptati.
* L'evento non fa ancora parte del contratto di ARMOR-COMMON.
* I valori di tracker e movimento sono costanti nel codice, non nel file di configurazione.

**Prossimi passi**

* Scrivere il modello di rilevamento per il Jetson Orin NX e provarlo con una telecamera reale.
* Spostare le costanti di tracker e movimento nel file di configurazione e inserire l'evento nel contratto di ARMOR-COMMON.""",
    },
  },
  "ja": {
    "tagline": "カメラのゾーン、マスク、検知ルール",
    "honest": "ゾーン、動きの確認、追跡、ルール、61 件のテストは実在します。**実際の検知モデルはまだありません**。カメラや Jetson Orin NX では何も動かしていません。シミュレーションは台本どおりの検知結果を使います。",
    "glance": [
      [
        "役割",
        "カメラのゾーン、マスク、検出ルール（ファミリー：Core Services、親：ARMOR-SERVER）",
      ],
      [
        "技術",
        "Python 3.11+、標準ライブラリのみ",
      ],
      [
        "テスト",
        "61 (`python -m unittest discover -s tests`)",
      ],
      [
        "動作環境",
        "任意のコンピューター",
      ],
      [
        "実機での確認",
        "まだありません：実際の検出器、カメラ、Jetson はなく、スクリプト化した検出によるシミュレーションのみ",
      ],
      [
        "ライセンス",
        "GPL-3.0-or-later",
      ],
    ],
    "status": {
      "software": "ゾーン、動きの確認、トラッカー、規則は動作しますが、実際の検出モデルはまだありません。シミュレーションはスクリプト化した検出結果を使います。",
      "tests": "61 件のテストが通ります（`python -m unittest discover -s tests`）。",
      "hardware": "カメラや Jetson Orin NX ではまだ何も動かしていません。",
      "docs": "8 言語と変更履歴は最新です。",
    },
    "docs": [
      "[使い方](docs/USAGE.md)：コマンド、設定、イベント、ライブラリ",
    ],
    "contributing_first": "Pull Request の前に `python -m unittest discover -s tests` and `python -I tools/armor_ci_validate.py` を実行してください。通る必要があります。[CONTRIBUTING.md](CONTRIBUTING.md) と[行動規範](CODE_OF_CONDUCT.md)を参照してください。",
    "languages_extra": "",
    "body": {
      "overview": r"""* **ゾーンとマスク:** 正規化座標（0 から 1）で描いた多角形なので、同じ図がどの解像度でも使えます。ゾーンは検知を数え、マスクは動きを無視します。各ゾーンにはラベルのフィルター、種類（`alert` または `detection`）、画像数と秒数の慣性があります。
* **まず動き:** 高価な検知器は、マスクの外で画面が十分に変化したときだけ動きます。
* **追跡:** 各物体は画像間で同一性を保ち、止まっているもの（駐車中の車）は記憶されて新しいイベントを出しません。
* **警戒プロファイル:** `away`、`home` などが監視するゾーンを選びます。未知のモードはすべてを監視します。
* **報告するだけのイベント:** 警報や検知には常に `authorizes_action: false` が付き、何をするかはサーバーが決めます。""",
      "role": r"""ARMOR-VISION は、検出器とは別に、カメラの映像が何を意味するかを決める部分です。映像に描くゾーンとマスク、高価な検出器の前に走る動き検査、トラッカー、警戒プロファイル、検出をイベントに変えるルール。現在カメラを見張っているのは [ARMOR-SERVER-AI](https://github.com/JuanenRac/ARMOR-SERVER-AI) で、ARMOR-VISION は実際の検出モデルのためのルールを用意して待っています。報告するだけで、イベントが動作を認可することはありません。

| 名前 | 方法 | 用途 |
|---|---|---|
| ARMOR-SERVER-AI | モデルができたら同じルールを使う | 現在カメラを監視する |
| ARMOR-SERVER | `armor.vision.event/v1` | イベントの扱いを決める（ARMOR-COMMON のコントラクトにはまだ含まれない） |""",
      "architecture": r"""<p align="center">
  <img src="images/architecture.svg" alt="ARMOR-VISION のアーキテクチャ：呼び出し元、内部、依存先" width="100%">
</p>""",
      "security": r"""| 脅威 | 対策 |
|---|---|
| ルールエンジンが勝手に動く | すべてのイベントに `authorizes_action: false`（スキーマ `armor.vision.event/v1`）が付き、決めるのはサーバーです |
| カメラ設定の誤り | `check-config` はすべての問題を列挙し、1 つでもあれば何も受け付けません。座標は 0〜1、ゾーンは `alert` か `detection`、未知のフィールドはエラーです |
| 高コストな検出器が無駄に動く | まず動き判定：マスク外で 16 x 9 グリッドの十分なセルが変化したときだけ検出器を呼びます |
| 駐車中の車が何度もイベントを出す | トラッカーは静止物（3 秒で 0.01 未満の移動）を 300 秒覚え、新しいイベントを出しません |
| 未知の警戒モード | すべてのゾーンを監視します。プロファイルのない `disarmed` だけが `alert` ゾーンを止め、`detection` ゾーンは記録を続けます |

ここにある機能は安全機能ではありません。実際の検出モデルはまだありません。""",
      "interfaces": r"""| 名前 | 設定内容 |
|---|---|
| `python -m armor_vision simulate [--config FILE] [--mode MODE]` | 組み込みシナリオ（私道を横切る人、駐車中の車、マスクした木の陰の動き）を実行し、イベントごとに JSON 1 行と、最後にカウンターの行を出力します |
| `python -m armor_vision check-config FILE` | 設定を検証してすべての問題を表示します。終了コード 0 正常、1 不正、2 読み取り不可 |

```json
{"schema": "armor.vision.event/v1", "type": "alert", "camera_id": "cam-front", "zone_id": "drive",
 "zone_name": "Driveway", "track_id": 1, "label": "person", "confidence": 0.9,
 "box": [0.41, 0.62, 0.47, 0.82], "timestamp": 1.0, "authorizes_action": false}
```

ライブラリとして：`parse_config`、`Pipeline.process_detections`、`process_frame`。`load_detector("tensorrt")` は Jetson Orin NX 用のモデルが未実装のため `DetectorUnavailable` を送出します。[docs/USAGE.md](docs/USAGE.md) を参照。""",
      "configuration": r"""| 名前 | 設定内容 |
|---|---|
| `motion_threshold` | 1〜255：変化とみなす濃淡差 |
| `motion_min_cells` | 検出器を呼ぶ前に変化が必要な 16 x 9 グリッドのセル数 |
| `zones[]` | `id`、`name`、`kind`（`alert` または `detection`）、`labels`、`min_frames`、`min_seconds`、`points`（多角形、0〜1）。ボックスの足元で判定 |
| `masks[]` | 動きを無視する多角形。中心が内側にある検出は破棄されます |
| `profiles` | 警戒モードごとに監視するゾーン（`away`、`home` など） |

| 制限 | 値 |
|---|---|
| 検出とトラックの対応付け（重なり／到達範囲） | 0.3 / 1.0 |
| 動いているトラックが見えなくなって破棄されるまで | 2 s |
| 静止：判定窓／ずれ／保持時間 | 3 s / 0.01 / 300 s |
| 動き判定グリッド | 16 x 9 |

これらの値は現在 `tracker.py` と `motion.py` の定数です。設定ファイルにはゾーン、マスク、プロファイル、動きのしきい値があります。""",
      "quickstart": r"""**必要なもの:** Python 3.11+（標準ライブラリのみ）。

```powershell
$env:PYTHONPATH = "src"
python -m armor_vision simulate --mode away
python -m armor_vision check-config my_cameras.json
python -m unittest discover -s tests   # 61 tests
```

```bash
PYTHONPATH=src python -m armor_vision simulate --mode away
PYTHONPATH=src python -m armor_vision check-config my_cameras.json
PYTHONPATH=src python -m unittest discover -s tests   # 61 tests
```""",
      "testing": r"""```powershell
$env:PYTHONPATH = "src"
python -m unittest discover -s tests
python -I tools/armor_ci_validate.py
```

| テストファイル | テスト数 | 対象 |
|---|---|---|
| `test_vision.py` | 42 | 幾何、設定、動き、トラッカー、ルール、プロファイル、全体の流れ、コマンドライン |
| `test_vision_edges.py` | 19 | 境界条件：不正な設定、静止物、マスクされた検出、利用できない検出器 |""",
      "build": "純粋な Python なのでコンパイルは不要です。バージョンは `pyproject.toml` と `armor.project.json` にあります。",
      "troubleshooting": r"""| 症状 | 原因 | 対処 |
|---|---|---|
| `check-config` が終了コード 1 | 設定に問題があり、すべて表示される | すべて直す（未知のフィールドもエラー） |
| `check-config` が終了コード 2 | ファイルを読み取れない | パスと JSON 形式を確認する |
| `DetectorUnavailable` | `load_detector("tensorrt")`：実モデルは未実装 | `ScriptedDetector` を使う |
| ゾーンが反応しない | 足元がポリゴン外、ラベルが非対象、マスクで隠れている、またはそのモードのプロファイルにゾーンがない | 同じファイルとモードで `simulate` を実行 |""",
      "structure": r"""<p align="center">
  <img src="images/repository-structure.svg" alt="ARMOR-VISION のリポジトリ構造" width="100%">
</p>

<details>
<summary>ツリーのテキスト版</summary>

```text
ARMOR-VISION/
├── src/armor_vision/
│   ├── geometry.py                      正規化座標の多角形
│   ├── config.py                        ゾーン、マスク、プロファイルとその検証
│   ├── motion.py                        16 x 9 の動き判定（マスクは無視）
│   ├── detector.py                      スクリプト化した検出。実モデルは未実装
│   ├── tracker.py                       画像間の識別、静止物
│   ├── rules.py                         ゾーンからイベントへ：armor.vision.event/v1
│   └── pipeline.py cli.py __main__.py   全体の流れとコマンドライン
├── tests/                               テスト
├── docs/                                このリポジトリのガイド
├── tools/                               共通の CI チェックとプロジェクトツール
├── .github/                             CI ワークフローと Issue・Pull Request のテンプレート
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

* 実際の検出モデルはまだなく、カメラや Jetson Orin NX では何も動いていません。シミュレーションはスクリプト化した検出を使います。
* イベントはまだ ARMOR-COMMON のコントラクトに含まれていません。
* トラッカーと動き判定の値は設定ファイルではなくコード内の定数です。

**今後**

* Jetson Orin NX 用の検出モデルを書き、実際のカメラで試す。
* トラッカーと動き判定の定数を設定ファイルへ移し、イベントを ARMOR-COMMON のコントラクトに入れる。""",
    },
  },
  "zh": {
    "tagline": "摄像头的区域、遮罩与检测规则",
    "honest": "区域、运动检查、跟踪、规则和 61 个测试都是真实的。**目前还没有真正的检测模型**，也没有在任何摄像头或 Jetson Orin NX 上运行过：模拟使用的是预设的检测结果。",
    "glance": [
      [
        "角色",
        "摄像头区域、遮罩和检测规则（家族：Core Services，上级：ARMOR-SERVER）",
      ],
      [
        "技术栈",
        "Python 3.11+，仅标准库",
      ],
      [
        "测试",
        "61 (`python -m unittest discover -s tests`)",
      ],
      [
        "运行位置",
        "任何计算机",
      ],
      [
        "真实硬件",
        "暂无：没有真实的检测器、摄像头或 Jetson（使用脚本化检测的模拟）",
      ],
      [
        "许可证",
        "GPL-3.0-or-later",
      ],
    ],
    "status": {
      "software": "防区、移动检查、跟踪器和规则都能工作，但目前还没有真实的检测模型：模拟使用的是脚本化的检测结果。",
      "tests": "61 项测试通过（`python -m unittest discover -s tests`）。",
      "hardware": "还没有在摄像头或 Jetson Orin NX 上运行过。",
      "docs": "八种语言和更新日志均为最新。",
    },
    "docs": [
      "[用法](docs/USAGE.md)：命令、配置、事件和库",
    ],
    "contributing_first": "提交 Pull Request 之前请运行 `python -m unittest discover -s tests` and `python -I tools/armor_ci_validate.py`：必须通过。参见 [CONTRIBUTING.md](CONTRIBUTING.md) 和[行为准则](CODE_OF_CONDUCT.md)。",
    "languages_extra": "",
    "body": {
      "overview": r"""* **区域与遮罩：** 用归一化坐标（0 到 1）绘制的多边形，因此同一张图在任何分辨率下都适用；区域统计检测结果，遮罩忽略运动。每个区域有标签过滤、类型（`alert` 或 `detection`）以及以帧数和秒数表示的惰性。
* **先看运动：** 只有当遮罩之外的画面变化足够多时，开销很大的检测器才会运行。
* **跟踪：** 每个物体在画面之间保持身份，静止的物体（停着的汽车）会被记住，不再产生新事件。
* **布防配置：** `away`、`home` 等决定监视哪些区域；未知模式则监视全部。
* **只报告的事件：** 告警或检测始终带有 `authorizes_action: false`；做什么由服务器决定。""",
      "role": r"""ARMOR-VISION 是独立于任何检测器、决定摄像头画面含义的部分：画在上面的区域和遮罩、先于昂贵检测器运行的移动检查、跟踪器、布防配置，以及把检测变成事件的规则。如今观察摄像头的是 [ARMOR-SERVER-AI](https://github.com/JuanenRac/ARMOR-SERVER-AI) 服务；ARMOR-VISION 则为真正的检测模型准备好了规则，等待它的到来。它只报告：事件从不授权任何动作。

| 名称 | 方式 | 用途 |
|---|---|---|
| ARMOR-SERVER-AI | 有模型后使用同样的规则 | 目前负责监视摄像头 |
| ARMOR-SERVER | `armor.vision.event/v1` | 决定如何处理事件（尚未纳入 ARMOR-COMMON 合约） |""",
      "architecture": r"""<p align="center">
  <img src="images/architecture.svg" alt="ARMOR-VISION 的架构：谁调用它、它包含什么、它依赖什么" width="100%">
</p>""",
      "security": r"""| 威胁 | 防御 |
|---|---|
| 规则引擎自行行动 | 每个事件都带有 `authorizes_action: false`（模式 `armor.vision.event/v1`）；由服务器决定 |
| 错误的摄像头配置 | `check-config` 会列出所有问题，只要有一个问题就不接受任何配置；坐标为 0 到 1，区域为 `alert` 或 `detection`，未知字段视为错误 |
| 耗资源的检测器无故运行 | 先检测运动：只有遮罩之外 16 x 9 网格中足够多的单元发生变化，才会调用检测器 |
| 停放的汽车不断触发事件 | 跟踪器会记住静止物体（3 秒内漂移小于 0.01）300 秒，不再产生新事件 |
| 未知的布防模式 | 监视所有区域；只有没有配置文件的 `disarmed` 会让 `alert` 区域静默，`detection` 区域仍会记录 |

这里没有任何安全功能：目前还没有真实的检测模型。""",
      "interfaces": r"""| 名称 | 作用 |
|---|---|
| `python -m armor_vision simulate [--config FILE] [--mode MODE]` | 运行内置场景（有人穿过车道、停放的汽车、被遮罩的树后有动静），每个事件输出一行 JSON，最后输出计数器 |
| `python -m armor_vision check-config FILE` | 校验配置并输出所有问题；退出码 0 正常、1 无效、2 无法读取 |

```json
{"schema": "armor.vision.event/v1", "type": "alert", "camera_id": "cam-front", "zone_id": "drive",
 "zone_name": "Driveway", "track_id": 1, "label": "person", "confidence": 0.9,
 "box": [0.41, 0.62, 0.47, 0.82], "timestamp": 1.0, "authorizes_action": false}
```

作为库使用：`parse_config`、`Pipeline.process_detections` 和 `process_frame`。调用 `load_detector("tensorrt")` 会抛出 `DetectorUnavailable`，因为 Jetson Orin NX 的模型尚未编写。参见 [docs/USAGE.md](docs/USAGE.md)。""",
      "configuration": r"""| 名称 | 作用 |
|---|---|
| `motion_threshold` | 1 到 255：被视为变化的灰度差 |
| `motion_min_cells` | 调用检测器前必须变化的 16 x 9 网格单元数 |
| `zones[]` | `id`、`name`、`kind`（`alert` 或 `detection`）、`labels`、`min_frames`、`min_seconds`、`points`（多边形，0 到 1）；按框的脚部计数 |
| `masks[]` | 忽略运动的多边形；中心位于其中的检测会被丢弃 |
| `profiles` | 每种布防模式下监视哪些区域（`away`、`home` 等） |

| 限制 | 值 |
|---|---|
| 检测与轨迹的匹配（重叠／范围） | 0.3 / 1.0 |
| 移动轨迹未被看到则在此时间后丢弃 | 2 s |
| 静止：窗口／漂移／记忆时长 | 3 s / 0.01 / 300 s |
| 运动网格 | 16 x 9 |

这些值目前是 `tracker.py` 和 `motion.py` 中的常量；配置文件包含区域、遮罩、配置文件和运动阈值。""",
      "quickstart": r"""**要求:** Python 3.11+（仅标准库）。

```powershell
$env:PYTHONPATH = "src"
python -m armor_vision simulate --mode away
python -m armor_vision check-config my_cameras.json
python -m unittest discover -s tests   # 61 tests
```

```bash
PYTHONPATH=src python -m armor_vision simulate --mode away
PYTHONPATH=src python -m armor_vision check-config my_cameras.json
PYTHONPATH=src python -m unittest discover -s tests   # 61 tests
```""",
      "testing": r"""```powershell
$env:PYTHONPATH = "src"
python -m unittest discover -s tests
python -I tools/armor_ci_validate.py
```

| 测试文件 | 测试数 | 覆盖内容 |
|---|---|---|
| `test_vision.py` | 42 | 几何、配置、运动、跟踪、规则、配置文件、流程和命令行 |
| `test_vision_edges.py` | 19 | 边界情况：错误配置、静止物体、被遮罩的检测以及不可用的检测器 |""",
      "build": "纯 Python：无需编译。版本在 `pyproject.toml` 和 `armor.project.json` 中。",
      "troubleshooting": r"""| 现象 | 原因 | 处理 |
|---|---|---|
| `check-config` 退出码为 1 | 配置有问题，会逐条列出 | 全部修正：未知字段也算错误 |
| `check-config` 退出码为 2 | 无法读取文件 | 检查路径以及是否为 JSON |
| `DetectorUnavailable` | `load_detector("tensorrt")`：真实模型尚未编写 | 使用 `ScriptedDetector` |
| 区域从不触发 | 脚部在多边形之外、标签不被接受、被遮罩挡住，或该模式的配置文件不含此区域 | 用同样的文件和模式运行 `simulate` |""",
      "structure": r"""<p align="center">
  <img src="images/repository-structure.svg" alt="ARMOR-VISION 的仓库结构" width="100%">
</p>

<details>
<summary>目录树的文本版</summary>

```text
ARMOR-VISION/
├── src/armor_vision/
│   ├── geometry.py                      归一化坐标的多边形
│   ├── config.py                        区域、遮罩、配置文件及其校验
│   ├── motion.py                        16 x 9 运动检测（忽略遮罩）
│   ├── detector.py                      脚本化检测；真实模型尚未编写
│   ├── tracker.py                       跨画面的身份；静止物体
│   ├── rules.py                         从区域到事件：armor.vision.event/v1
│   └── pipeline.py cli.py __main__.py   整个流程与命令行
├── tests/                               测试
├── docs/                                本仓库的指南
├── tools/                               共享的 CI 检查和项目工具
├── .github/                             CI 工作流以及 Issue 和 Pull Request 模板
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

* 目前还没有真实的检测模型，也没有在摄像头或 Jetson Orin NX 上运行过：模拟使用脚本化的检测。
* 该事件尚未纳入 ARMOR-COMMON 合约。
* 跟踪与运动的数值是代码中的常量，不在配置文件中。

**下一步**

* 为 Jetson Orin NX 编写检测模型，并用真实摄像头试验。
* 把跟踪与运动常量移到配置文件，并将该事件纳入 ARMOR-COMMON 合约。""",
    },
  },
  "pt": {
    "tagline": "Zonas, máscaras e regras de deteção para as câmaras",
    "honest": "As zonas, a verificação de movimento, o seguidor, as regras e os 61 testes são reais. **Ainda não há nenhum modelo detetor real** e nada correu numa câmara nem no Jetson Orin NX: a simulação usa deteções com guião.",
    "glance": [
      [
        "Função",
        "Zonas, máscaras e regras de deteção de câmaras (família: Core Services, pai: ARMOR-SERVER)",
      ],
      [
        "Tecnologia",
        "Python 3.11+, só biblioteca padrão",
      ],
      [
        "Testes",
        "61 (`python -m unittest discover -s tests`)",
      ],
      [
        "Funciona em",
        "Qualquer computador",
      ],
      [
        "Em hardware real",
        "Nenhum ainda: nem detetor real, nem câmara, nem Jetson (uma simulação com deteções guionizadas)",
      ],
      [
        "Licença",
        "GPL-3.0-or-later",
      ],
    ],
    "status": {
      "software": "As zonas, a verificação de movimento, o seguimento e as regras funcionam, mas ainda não há um modelo detetor real: a simulação usa deteções com guião.",
      "tests": "Passam 61 testes (`python -m unittest discover -s tests`).",
      "hardware": "Nada funcionou numa câmara nem no Jetson Orin NX.",
      "docs": "Oito idiomas e o registo de alterações estão atualizados.",
    },
    "docs": [
      "[Utilização](docs/USAGE.md): os comandos, a configuração, o evento e a biblioteca",
    ],
    "contributing_first": "Antes de um pull request, execute `python -m unittest discover -s tests` and `python -I tools/armor_ci_validate.py`: tem de passar. Consulte [CONTRIBUTING.md](CONTRIBUTING.md) e o [código de conduta](CODE_OF_CONDUCT.md).",
    "languages_extra": "",
    "body": {
      "overview": r"""* **Zonas e máscaras:** polígonos desenhados em coordenadas normalizadas (0 a 1), para que um só desenho funcione em qualquer resolução; uma zona conta deteções, uma máscara ignora o movimento. Cada zona tem um filtro de etiquetas, um tipo (`alert` ou `detection`) e uma inércia em imagens e segundos.
* **Primeiro o movimento:** o detetor caro só corre quando mudou o suficiente da imagem, fora das máscaras.
* **Um seguidor:** cada objeto mantém a sua identidade entre imagens, e o que está parado (um carro estacionado) é lembrado e não gera eventos novos.
* **Perfis de armação:** `away`, `home` e semelhantes escolhem que zonas se vigiam; um modo desconhecido vigia tudo.
* **Eventos que só reportam:** um alerta ou uma deteção leva sempre `authorizes_action: false`; o servidor decide o que fazer.""",
      "role": r"""O ARMOR-VISION é a parte que decide o que significa a imagem de uma câmara, à parte de qualquer detetor: as zonas e máscaras desenhadas nela, a verificação de movimento que corre antes do detetor dispendioso, o seguidor, os perfis de armar e as regras que transformam deteções em eventos. O [ARMOR-SERVER-AI](https://github.com/JuanenRac/ARMOR-SERVER-AI) é o serviço que hoje vigia as câmaras; o ARMOR-VISION é onde as regras para um modelo de deteção real estão prontas, à sua espera. Só comunica: os eventos nunca autorizam uma ação.

| Nome | Como | Para quê |
|---|---|---|
| ARMOR-SERVER-AI | as mesmas regras, quando houver um modelo | Hoje vigia as câmaras |
| ARMOR-SERVER | `armor.vision.event/v1` | Decide o que fazer com um evento (ainda fora do contrato do ARMOR-COMMON) |""",
      "architecture": r"""<p align="center">
  <img src="images/architecture.svg" alt="Arquitetura de ARMOR-VISION: quem o chama, o que contém e de que depende" width="100%">
</p>""",
      "security": r"""| Ameaça | Defesa |
|---|---|
| O motor de regras age por conta própria | Todo o evento leva `authorizes_action: false` (esquema `armor.vision.event/v1`); quem decide é o servidor |
| Uma configuração de câmara errada | `check-config` lista todos os problemas e basta um para nada ser aceite; as coordenadas vão de 0 a 1, uma zona é `alert` ou `detection`, os campos desconhecidos são erros |
| O detetor caro corre sem motivo | Primeiro o movimento: o detetor só é consultado se células suficientes da grelha 16 x 9 mudarem fora das máscaras |
| Um carro estacionado gera evento após evento | O seguimento lembra o que está parado (deriva abaixo de 0,01 em 3 s) durante 300 s e não gera eventos novos |
| Um modo de armação desconhecido | Vigiam-se todas as zonas; só `disarmed` sem perfil silencia as zonas `alert` e as `detection` continuam a registar |

Nada aqui é uma função de segurança: ainda não há um modelo de deteção real.""",
      "interfaces": r"""| Nome | O que define |
|---|---|
| `python -m armor_vision simulate [--config FILE] [--mode MODE]` | Executa um cenário integrado (uma pessoa atravessa um acesso, um carro estacionado, movimento atrás de uma árvore mascarada) e imprime uma linha JSON por evento e uma última com os contadores |
| `python -m armor_vision check-config FILE` | Valida uma configuração e imprime cada problema; saída 0 boa, 1 inválida, 2 ilegível |

```json
{"schema": "armor.vision.event/v1", "type": "alert", "camera_id": "cam-front", "zone_id": "drive",
 "zone_name": "Driveway", "track_id": 1, "label": "person", "confidence": 0.9,
 "box": [0.41, 0.62, 0.47, 0.82], "timestamp": 1.0, "authorizes_action": false}
```

Como biblioteca: `parse_config`, `Pipeline.process_detections` e `process_frame`. Pedir `load_detector("tensorrt")` lança `DetectorUnavailable` porque o modelo para o Jetson Orin NX não está escrito. Consulte [docs/USAGE.md](docs/USAGE.md).""",
      "configuration": r"""| Nome | O que define |
|---|---|
| `motion_threshold` | 1 a 255: a diferença de cinzento que conta como mudança |
| `motion_min_cells` | Quantas células da grelha 16 x 9 têm de mudar antes de consultar o detetor |
| `zones[]` | `id`, `name`, `kind` (`alert` ou `detection`), `labels`, `min_frames`, `min_seconds`, `points` (polígono, 0 a 1); conta-se pelos pés da caixa |
| `masks[]` | Polígonos onde o movimento é ignorado; as deteções com o centro lá dentro são descartadas |
| `profiles` | Que zonas são vigiadas em cada modo de armação (`away`, `home`, ...) |

| Limite | Valor |
|---|---|
| Emparelhamento de uma deteção com uma pista (sobreposição / alcance) | 0.3 / 1.0 |
| Uma pista em movimento não vista é descartada após | 2 s |
| Parado: janela / deriva / lembrado durante | 3 s / 0.01 / 300 s |
| Grelha de movimento | 16 x 9 |

Estes valores são hoje constantes de `tracker.py` e `motion.py`; o ficheiro de configuração contém as zonas, máscaras, perfis e os limiares de movimento.""",
      "quickstart": r"""**Requisitos:** Python 3.11+ (só biblioteca padrão).

```powershell
$env:PYTHONPATH = "src"
python -m armor_vision simulate --mode away
python -m armor_vision check-config my_cameras.json
python -m unittest discover -s tests   # 61 tests
```

```bash
PYTHONPATH=src python -m armor_vision simulate --mode away
PYTHONPATH=src python -m armor_vision check-config my_cameras.json
PYTHONPATH=src python -m unittest discover -s tests   # 61 tests
```""",
      "testing": r"""```powershell
$env:PYTHONPATH = "src"
python -m unittest discover -s tests
python -I tools/armor_ci_validate.py
```

| Ficheiro de testes | Testes | O que cobre |
|---|---|---|
| `test_vision.py` | 42 | Geometria, configuração, movimento, seguimento, regras, perfis, a cadeia e a linha de comandos |
| `test_vision_edges.py` | 19 | Os casos-limite: configurações erradas, objetos parados, deteções mascaradas e o detetor indisponível |""",
      "build": "É Python puro: nada a compilar. A versão está em `pyproject.toml` e `armor.project.json`.",
      "troubleshooting": r"""| Vê | Porque | Faça |
|---|---|---|
| `check-config` termina com 1 | A configuração tem problemas; lista-os todos | Corrija-os todos: os campos desconhecidos são erros |
| `check-config` termina com 2 | Não é possível ler o ficheiro | Verifique o caminho e que é JSON |
| `DetectorUnavailable` | `load_detector("tensorrt")`: o modelo real não está escrito | Use `ScriptedDetector` |
| Uma zona nunca dispara | Os pés estão fora do polígono, a etiqueta não é aceite, uma máscara esconde-a, ou o modo não tem um perfil com essa zona | Execute `simulate` com o mesmo ficheiro e modo |""",
      "structure": r"""<p align="center">
  <img src="images/repository-structure.svg" alt="Estrutura do repositório de ARMOR-VISION" width="100%">
</p>

<details>
<summary>Versão em texto da árvore</summary>

```text
ARMOR-VISION/
├── src/armor_vision/
│   ├── geometry.py                      polígonos em coordenadas normalizadas
│   ├── config.py                        zonas, máscaras, perfis e a sua validação
│   ├── motion.py                        a verificação de movimento 16 x 9, máscaras ignoradas
│   ├── detector.py                      deteções guionizadas; o modelo real não está escrito
│   ├── tracker.py                       identidade entre imagens; objetos parados
│   ├── rules.py                         das zonas aos eventos: armor.vision.event/v1
│   └── pipeline.py cli.py __main__.py   toda a cadeia e a linha de comandos
├── tests/                               os testes
├── docs/                                os guias deste repositório
├── tools/                               as verificações de CI partilhadas e as ferramentas do projeto
├── .github/                             fluxo de CI e modelos de issues e pull requests
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

* Ainda não há um modelo de deteção real e nada correu numa câmara nem no Jetson Orin NX: a simulação usa deteções guionizadas.
* O evento ainda não faz parte do contrato do ARMOR-COMMON.
* Os valores do seguimento e do movimento são constantes no código, não no ficheiro de configuração.

**A seguir**

* Escrever o modelo de deteção para o Jetson Orin NX e experimentá-lo com uma câmara real.
* Passar as constantes do seguimento e do movimento para o ficheiro de configuração e pôr o evento no contrato do ARMOR-COMMON.""",
    },
  },
}
