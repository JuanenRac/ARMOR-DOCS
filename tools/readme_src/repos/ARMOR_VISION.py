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
      "ui",
      "yellow",
    ],
    [
      "security",
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
      "{{fact:tests:ARMOR-VISION}}%20passing",
      "2ea44f",
    ],
  ],
}

TEXT = {
  "en": {
    "tagline": "Zones, masks and detection rules for the cameras",
    "honest": "The zones, the motion check, the tracker, the rules and the {{fact:tests:ARMOR-VISION}} tests are real. The detector for the Jetson Orin NX (TensorRT), the two streams, the clips, speed, left objects, PTZ follow, the schedule and the second phase are written and tested only with simulated engines and sources: nothing has run on a camera or on the Jetson Orin NX.",
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
        "{{fact:tests:ARMOR-VISION}} (`python -m unittest discover -s tests`)",
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
      "tests": "{{fact:tests:ARMOR-VISION}} tests pass (`python -m unittest discover -s tests`).",
      "hardware": "Nothing has run on a camera or on the Jetson Orin NX.",
      "ui": "The routes or messages it offers are documented and tested with a client; not every client has used them yet",
      "security": "Access control, input limits or signatures are implemented and tested on a computer; nobody outside the project has reviewed them",
      "integration": "Its messages are validated against the shared schemas and conformance vectors of ARMOR-COMMON; it has not run together with the real equipment",
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
| The activity pipeline stores or leaks pictures of people | It is off by default; it keeps only a count per cell of the grid (positions, labels and numbers), never a picture, a box or an identity; the export says `contains_images: false`. A file of detections that is malformed, goes back in time or is over 16 MiB is refused whole, and the map has a hard memory limit |

Nothing here is a safety function: there is no real detector model yet.""",
      "interfaces": r"""| Name | What it sets |
|---|---|
| `python -m armor_vision simulate [--config FILE] [--mode MODE]` | Runs a built-in scenario (a person crossing a driveway, a parked car, movement behind a masked tree) and prints one JSON line per event and a last line with the counters |
| `python -m armor_vision check-config FILE` | Validates a configuration and prints every problem; exit 0 good, 1 invalid, 2 unreadable |
| `python -m armor_vision simulate --simulate-events --activity-config FILE [--seed N] [--detections-file FILE]` | Activity pipeline, OFF unless the file says `"enabled": true` (exit 3 when off): a synthetic scene with a fixed seed, or recorded detections, gives one JSON line per event (`zone_enter`, `zone_exit`, `dwell`, `loiter`, `line_cross`) |
| `python -m armor_vision simulate --heatmap OUT --activity-config FILE` | Writes the heat map of activity (counts per cell, `OUT` ends in `.json`, `.png` or `.svg`); only aggregated positions, never pictures |
| `python -m armor_vision activity-example` / `check-activity-config FILE` | Prints an activity configuration to start from / validates one (exit 0 good, 1 invalid, 2 unreadable) |
| `ActivityEngine`, `heatmap_route` | As a library: the engine and the handler of `GET /heatmap?camera=ID&format=json` (`png` and `svg` too), for the service that mounts it; the route answers 404 while the pipeline is off |
| `python -m armor_vision heatmap-route --activity-config FILE [--detections-file FILE] [--camera ID] [--format json\|png\|svg] [--scale N]` | Answers one `GET /heatmap` query from recorded detections and prints the answer as one JSON line (`status`, `content_type`, `body_base64`); this is what a server that mounts the route runs. Exit 0 for every answer of the route (also 404 when the pipeline is off and 400 for a bad query), 1 for a wrong configuration, 2 for a file that cannot be read |
| `python -m armor_vision replay FILE [--config FILE] [--mode MODE]` | Runs recorded detections (JSON lines) through the zone rules and prints the events each zone would have raised, with the count per zone (exit 2 for a file that cannot be used or a camera that is not in the configuration) |
| `OnnxDetector`, `parse_onnx_settings` | As a library: a detector that runs an ONNX model on the CPU (needs `onnxruntime`, which is not a dependency; off unless it is built) |
| `python -m armor_vision serve --activity-config FILE [--config FILE] [--service-config FILE]` | Runs the live service: the activity engine stays in memory, detections come in one observation at a time (`POST /ingest`) and `GET /heatmap` answers from that memory. It listens on 127.0.0.1 unless the settings file says `allow_remote`, keeps no secret but the token it may ask for (it must have one, in a file, when it is open to other machines) and stores nothing on disk. Exit 1 for a wrong configuration or an activity pipeline that is off, 2 for a file that cannot be read or a port that cannot be opened Limits in the settings file: `request_timeout_s` (a client that goes quiet is dropped), `max_connections` (the next one is told to come back with 503) and `render_cache_entries` (how many drawn maps are kept; 0 turns it off). |

```json
{"schema": "armor.vision.event/v1", "type": "alert", "camera_id": "cam-front", "zone_id": "drive",
 "zone_name": "Driveway", "track_id": 1, "label": "person", "confidence": 0.9,
 "box": [0.41, 0.62, 0.47, 0.82], "timestamp": 1.0, "authorizes_action": false}
```

As a library: `parse_config`, `Pipeline.process_detections` and `process_frame`. `load_detector("tensorrt")` needs its settings and the Jetson packages, otherwise it raises `DetectorUnavailable`; with a simulated engine it runs anywhere and says its evidence is `simulator`. See [docs/USAGE.md](docs/USAGE.md).""",
      "configuration": r"""| Name | What it sets |
|---|---|
| `motion_threshold` | 1 to 255: the grey difference that counts as change |
| `motion_min_cells` | How many cells of the 16 x 9 grid must change before the detector is asked |
| `zones[]` | `id`, `name`, `kind` (`alert` or `detection`), `labels`, `min_frames`, `min_seconds`, `points` (polygon, 0 to 1); counted by the feet of the box |
| `masks[]` | Polygons where movement is ignored; detections whose centre is inside are dropped |
| `profiles` | Which zones are watched in each arming mode (`away`, `home`, ...) |
| `activity configuration (separate file)` | `enabled` (default `false`), `heatmap` (`cols`, `rows`, `window_seconds`, `half_life_seconds`, `slices`, `max_cells` up to 65536, `position`, `labels`) and `events` (`dwell_seconds`, `loiter_seconds`, `loiter_radius`, `lost_seconds`, `labels`, `lines[]` with `id`, `a`, `b`, `sensitivity_floor` (`low`, `normal`, `high`)); the heat map is normalised as weight divided by the maximum |

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
python -m unittest discover -s tests   # {{fact:tests:ARMOR-VISION}} tests
```

```bash
PYTHONPATH=src python -m armor_vision simulate --mode away
PYTHONPATH=src python -m armor_vision check-config my_cameras.json
PYTHONPATH=src python -m unittest discover -s tests   # {{fact:tests:ARMOR-VISION}} tests
```""",
      "testing": r"""```powershell
$env:PYTHONPATH = "src"
python -m unittest discover -s tests
python -I tools/armor_ci_validate.py
```

| Test file | Tests | What it covers |
|---|---|---|
| `test_vision.py` | 42 | Geometry, configuration, motion, tracker, rules, profiles, the pipeline and the command line |
| `test_vision_edges.py` | 19 | The edges: bad configurations, stationary objects, masked detections and the unavailable detector |
| `test_characterization.py` | 2 | Fixes the output of the built-in simulation byte for byte, so that it cannot change while the activity pipeline is off |
| `test_activity.py` | 27 | Activity configuration, synthetic and recorded sources, events, heat map (determinism, sum equals detections, nothing outside the grid, window, decay, memory), the `/heatmap` handler and the command line |
| `test_heatmap_service.py` | 7 | The heat map route as a command: off is 404 whatever the data, on with no data is an empty map, counts in the three formats, bad queries, and a wrong configuration or file is an error and never an empty map |
| `test_service.py` | 15 | The live service: the same map as the replayed file, off is 404 and 503, what is not understood is refused, the limits of the settings, bounded memory and the command |
| `test_service_load.py` | 7 | The live service under light load and with clients that misbehave: the new limits and their ranges, a client that goes quiet is dropped, the requests at once are bounded, exact counters under many threads, the drawing of an unchanged map is reused and bounded, and a map being drawn does not hold up the observations |
| `test_tensorrt_and_streams.py` | 21 | The TensorRT detector with a simulated engine, the pair of streams and the recorder, the clips with pre and post capture and the retention by type |
| `test_analytics_schedule_phase2.py` | 30 | Speed in a zone, left objects, the PTZ follower, the vectors of an event, the schedule by hour and the second phase off by default |""",
      "build": "It is plain Python: nothing to compile. The version lives in `pyproject.toml` and `armor.project.json`.",
      "troubleshooting": r"""| You see | Because | Do |
|---|---|---|
| `check-config` exits with 1 | The configuration has problems; it lists each one | Fix them all: unknown fields are errors |
| `check-config` exits with 2 | The file cannot be read | Check the path and that it is JSON |
| `DetectorUnavailable` | `load_detector("tensorrt")`: no settings, no engine file or no Jetson packages | Give `TensorrtSettings` and an engine file on the Jetson, or use `ScriptedDetector` |
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
│   ├── detector.py                      scripted, ONNX and TensorRT detectors (simulated engine off the Jetson)
│   ├── tracker.py                       identity between pictures; stationary objects
│   ├── rules.py                         zones to events: armor.vision.event/v1
│   ├── tensorrt_detector.py             the TensorRT detector for the Jetson; a simulated engine
│   ├── streams.py recording.py          sub stream to analyse, main stream to record; clips and retention
│   ├── analytics.py schedule.py         speed in a zone, left objects, PTZ follow; masks by hour
│   ├── phase2.py                        search by meaning, plates, faces: all off, with privacy notices
│   ├── activity_config.py               activity pipeline settings, off by default
│   ├── sources.py heatmap.py            synthetic and recorded sources; heat map
│   ├── activity.py                      events and the /heatmap handler
│   ├── heatmap_service.py               the /heatmap route as a command
│   ├── service.py                       the live service: the engine in memory, POST /ingest and GET /heatmap
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
* The camera or RTSP source of the activity pipeline is for the hardware and is not written: today it runs on a synthetic scene or a file of detections. The heat map has no HTTP server here, only the handler.
* The event is not part of the ARMOR-COMMON contract yet.
* The tracker and motion values are constants in the code, not in the configuration file.

**Next**

* Write the detector model for the Jetson Orin NX and try it with a real camera.
* Move the tracker and motion constants to the configuration file and put the event in the ARMOR-COMMON contract.""",
    },
  },
  "es": {
    "tagline": "Zonas, máscaras y reglas de detección para las cámaras",
    "honest": "Las zonas, la comprobación de movimiento, el seguimiento, las reglas y los {{fact:tests:ARMOR-VISION}} tests son reales. El detector para la Jetson Orin NX (TensorRT), las dos corrientes, los clips, la velocidad, los objetos abandonados, el seguimiento PTZ, el horario y la segunda fase están escritos y probados solo con motores y fuentes simulados: nada se ha ejecutado en una cámara ni en la Jetson Orin NX.",
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
        "{{fact:tests:ARMOR-VISION}} (`python -m unittest discover -s tests`)",
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
      "tests": "Pasan {{fact:tests:ARMOR-VISION}} pruebas (`python -m unittest discover -s tests`).",
      "hardware": "Nada ha funcionado en una cámara ni en la Jetson Orin NX.",
      "ui": "Las rutas o los mensajes que ofrece están documentados y probados con un cliente; aún no los han usado todos los clientes",
      "security": "El control de acceso, los límites de entrada o las firmas están implementados y probados en un ordenador; nadie ajeno al proyecto los ha revisado",
      "integration": "Sus mensajes se validan contra los esquemas compartidos y los vectores de conformidad de ARMOR-COMMON; no ha funcionado junto con el equipo real",
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
| El canal de actividad guarda o filtra imágenes de personas | Está apagado por defecto; solo guarda una cuenta por celda de la rejilla (posiciones, etiquetas y números), nunca una imagen, una caja ni una identidad; la exportación dice `contains_images: false`. Un fichero de detecciones mal formado, que va atrás en el tiempo o de más de 16 MiB se rechaza entero, y el mapa tiene un límite duro de memoria |

Nada de esto es una función de seguridad: aún no hay un modelo de detección real.""",
      "interfaces": r"""| Nombre | Qué define |
|---|---|
| `python -m armor_vision simulate [--config FILE] [--mode MODE]` | Ejecuta un escenario integrado (una persona cruza un camino, un coche aparcado, movimiento tras un árbol enmascarado) e imprime una línea JSON por evento y una última con los contadores |
| `python -m armor_vision check-config FILE` | Valida una configuración e imprime cada problema; salida 0 correcta, 1 inválida, 2 ilegible |
| `python -m armor_vision simulate --simulate-events --activity-config FILE [--seed N] [--detections-file FILE]` | Canal de actividad, APAGADO salvo que el fichero diga `"enabled": true` (código 3 si está apagado): una escena sintética con semilla fija, o detecciones grabadas, da una línea JSON por evento (`zone_enter`, `zone_exit`, `dwell`, `loiter`, `line_cross`) |
| `python -m armor_vision simulate --heatmap OUT --activity-config FILE` | Escribe el mapa de calor de actividad (cuentas por celda, `OUT` termina en `.json`, `.png` o `.svg`); solo posiciones agregadas, nunca imágenes |
| `python -m armor_vision activity-example` / `check-activity-config FILE` | Imprime una configuración de actividad de partida / valida una (código 0 bien, 1 no válida, 2 ilegible) |
| `ActivityEngine`, `heatmap_route` | Como biblioteca: el motor y el manejador de `GET /heatmap?camera=ID&format=json` (también `png` y `svg`), para el servicio que lo monte; la ruta responde 404 mientras el canal esté apagado |
| `python -m armor_vision heatmap-route --activity-config FILE [--detections-file FILE] [--camera ID] [--format json\|png\|svg] [--scale N]` | Responde una consulta `GET /heatmap` desde detecciones grabadas e imprime la respuesta como una línea JSON (`status`, `content_type`, `body_base64`); es lo que ejecuta un servidor que monta la ruta. Código 0 para cualquier respuesta de la ruta (también 404 con el canal apagado y 400 con una consulta mala), 1 si la configuración es errónea, 2 si no se puede leer un fichero |
| `python -m armor_vision replay FILE [--config FILE] [--mode MODE]` | Pasa detecciones grabadas (JSON lines) por las reglas de zona e imprime los eventos que habría levantado cada zona, con la cuenta por zona (salida 2 si el fichero no sirve o la cámara no está en la configuración) |
| `OnnxDetector`, `parse_onnx_settings` | Como biblioteca: un detector que ejecuta un modelo ONNX en la CPU (necesita `onnxruntime`, que no es dependencia; apagado salvo que se construya) |
| `python -m armor_vision serve --activity-config FILE [--config FILE] [--service-config FILE]` | Ejecuta el servicio vivo: el motor de actividad se queda en memoria, las detecciones entran de una observación en una (`POST /ingest`) y `GET /heatmap` responde desde esa memoria. Escucha en 127.0.0.1 salvo que el fichero de ajustes diga `allow_remote`, no guarda más secreto que el token que puede exigir (debe tenerlo, en un fichero, si está abierto a otras máquinas) y no escribe nada en disco. Sale con 1 si la configuración es errónea o la actividad está apagada, con 2 si un fichero no se puede leer o no se puede abrir el puerto Límites en el fichero de ajustes: `request_timeout_s` (se corta al cliente que se queda callado), `max_connections` (al siguiente se le dice que vuelva con un 503) y `render_cache_entries` (cuántos mapas dibujados se guardan; 0 lo apaga). |

```json
{"schema": "armor.vision.event/v1", "type": "alert", "camera_id": "cam-front", "zone_id": "drive",
 "zone_name": "Driveway", "track_id": 1, "label": "person", "confidence": 0.9,
 "box": [0.41, 0.62, 0.47, 0.82], "timestamp": 1.0, "authorizes_action": false}
```

Como biblioteca: `parse_config`, `Pipeline.process_detections` y `process_frame`. `load_detector("tensorrt")` necesita su configuración y los paquetes de la Jetson; si no, lanza `DetectorUnavailable`. Con un motor simulado funciona en cualquier sitio y declara que su evidencia es `simulator`. Consulta [docs/USAGE.md](docs/USAGE.md).""",
      "configuration": r"""| Nombre | Qué define |
|---|---|
| `motion_threshold` | 1 a 255: la diferencia de gris que cuenta como cambio |
| `motion_min_cells` | Cuántas celdas de la rejilla 16 x 9 deben cambiar antes de consultar al detector |
| `zones[]` | `id`, `name`, `kind` (`alert` o `detection`), `labels`, `min_frames`, `min_seconds`, `points` (polígono, 0 a 1); se cuenta por los pies de la caja |
| `masks[]` | Polígonos donde se ignora el movimiento; se descartan las detecciones cuyo centro está dentro |
| `profiles` | Qué zonas se vigilan en cada modo de armado (`away`, `home`, ...) |
| `configuración de actividad (fichero aparte)` | `enabled` (por defecto `false`), `heatmap` (`cols`, `rows`, `window_seconds`, `half_life_seconds`, `slices`, `max_cells` hasta 65536, `position`, `labels`) y `events` (`dwell_seconds`, `loiter_seconds`, `loiter_radius`, `lost_seconds`, `labels`, `lines[]` con `id`, `a`, `b`, `sensitivity_floor` (`low`, `normal`, `high`)); el mapa se normaliza como peso dividido por el máximo |

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
python -m unittest discover -s tests   # {{fact:tests:ARMOR-VISION}} tests
```

```bash
PYTHONPATH=src python -m armor_vision simulate --mode away
PYTHONPATH=src python -m armor_vision check-config my_cameras.json
PYTHONPATH=src python -m unittest discover -s tests   # {{fact:tests:ARMOR-VISION}} tests
```""",
      "testing": r"""```powershell
$env:PYTHONPATH = "src"
python -m unittest discover -s tests
python -I tools/armor_ci_validate.py
```

| Fichero de pruebas | Pruebas | Qué cubre |
|---|---|---|
| `test_vision.py` | 42 | Geometría, configuración, movimiento, seguimiento, reglas, perfiles, la cadena y la línea de órdenes |
| `test_vision_edges.py` | 19 | Los bordes: configuraciones erróneas, objetos quietos, detecciones enmascaradas y el detector no disponible |
| `test_characterization.py` | 2 | Fija byte a byte la salida de la simulación incorporada, para que no cambie mientras el canal de actividad esté apagado |
| `test_activity.py` | 27 | Configuración de actividad, fuentes sintética y grabada, eventos, mapa de calor (determinismo, suma igual a las detecciones, nada fuera de la rejilla, ventana, decaimiento, memoria), el manejador de `/heatmap` y la línea de comandos |
| `test_heatmap_service.py` | 7 | La ruta del mapa de calor como comando: apagado es 404 sea cual sea el dato, encendido sin datos es un mapa vacío, cuentas en los tres formatos, consultas malas, y una configuración o un fichero erróneos son un error y nunca un mapa vacío |
| `test_service.py` | 15 | El servicio vivo: el mismo mapa que el fichero reproducido, apagado da 404 y 503, lo que no se entiende se rechaza, los límites de los ajustes, memoria acotada y el comando |
| `test_service_load.py` | 7 | El servicio vivo con carga ligera y con clientes que se portan mal: los límites nuevos y sus rangos, se corta al cliente que se queda callado, las peticiones a la vez están acotadas, contadores exactos con muchos hilos, el dibujo de un mapa sin cambios se reutiliza y está acotado, y un mapa que se dibuja no retrasa las observaciones |
| `test_tensorrt_and_streams.py` | 21 | El detector TensorRT con un motor simulado, el par de corrientes y el grabador, los clips con pre y post captura y la retención por tipo |
| `test_analytics_schedule_phase2.py` | 30 | Velocidad en zona, objetos abandonados, el seguidor PTZ, los vectores de un evento, el horario y la segunda fase apagada por defecto |""",
      "build": "Es Python puro: no hay nada que compilar. La versión vive en `pyproject.toml` y `armor.project.json`.",
      "troubleshooting": r"""| Ves | Porque | Haz |
|---|---|---|
| `check-config` termina con 1 | La configuración tiene problemas; los lista todos | Corrígelos todos: los campos desconocidos son errores |
| `check-config` termina con 2 | No se puede leer el fichero | Comprueba la ruta y que sea JSON |
| `DetectorUnavailable` | `load_detector("tensorrt")`: sin configuración, sin fichero de motor o sin los paquetes de la Jetson | Da `TensorrtSettings` y un fichero de motor en la Jetson, o usa `ScriptedDetector` |
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
│   ├── detector.py                      detectores guionizado, ONNX y TensorRT (motor simulado fuera de la Jetson)
│   ├── tracker.py                       identidad entre imágenes; objetos quietos
│   ├── rules.py                         de zonas a eventos: armor.vision.event/v1
│   ├── tensorrt_detector.py             el detector TensorRT para la Jetson; un motor simulado
│   ├── streams.py recording.py          subcorriente para analizar, principal para grabar; clips y retención
│   ├── analytics.py schedule.py         velocidad en zona, objetos abandonados, seguimiento PTZ; máscaras por hora
│   ├── phase2.py                        búsqueda semántica, matrículas, caras: todo apagado, con avisos de privacidad
│   ├── activity_config.py               ajustes del canal de actividad, apagado por defecto
│   ├── sources.py heatmap.py            fuentes sintética y grabada; mapa de calor
│   ├── activity.py                      eventos y manejador de /heatmap
│   ├── heatmap_service.py               la ruta /heatmap como comando
│   ├── service.py                       el servicio vivo: el motor en memoria, POST /ingest y GET /heatmap
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
* La fuente de cámara o RTSP del canal de actividad es para el hardware y no está escrita: hoy funciona con una escena sintética o un fichero de detecciones. El mapa de calor no tiene aquí servidor HTTP, solo el manejador.
* El evento aún no forma parte del contrato de ARMOR-COMMON.
* Los valores del seguimiento y del movimiento son constantes del código, no del fichero de configuración.

**Lo siguiente**

* Escribir el modelo de detección para la Jetson Orin NX y probarlo con una cámara real.
* Pasar las constantes de seguimiento y movimiento al fichero de configuración y meter el evento en el contrato de ARMOR-COMMON.""",
    },
  },
  "de": {
    "tagline": "Zonen, Masken und Erkennungsregeln für die Kameras",
    "honest": "Die Zonen, die Bewegungsprüfung, die Verfolgung, die Regeln und die {{fact:tests:ARMOR-VISION}} Tests sind real. Der Detektor für den Jetson Orin NX (TensorRT), die zwei Streams, die Clips, Geschwindigkeit, zurückgelassene Objekte, PTZ-Verfolgung, der Zeitplan und die zweite Phase sind geschrieben und nur mit simulierten Engines und Quellen getestet: nichts lief auf einer Kamera oder auf dem Jetson Orin NX.",
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
        "{{fact:tests:ARMOR-VISION}} (`python -m unittest discover -s tests`)",
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
      "tests": "{{fact:tests:ARMOR-VISION}} Tests bestehen (`python -m unittest discover -s tests`).",
      "hardware": "Nichts lief an einer Kamera oder auf dem Jetson Orin NX.",
      "ui": "Die angebotenen Routen oder Nachrichten sind dokumentiert und mit einem Client getestet; noch nicht jeder Client hat sie benutzt",
      "security": "Zugriffskontrolle, Eingabegrenzen oder Signaturen sind umgesetzt und auf einem Rechner getestet; niemand außerhalb des Projekts hat sie geprüft",
      "integration": "Seine Nachrichten werden gegen die gemeinsamen Schemas und Konformitätsvektoren von ARMOR-COMMON geprüft; es lief noch nicht zusammen mit der echten Ausrüstung",
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
| Die Aktivitätspipeline speichert oder verrät Bilder von Personen | Sie ist standardmäßig aus; sie behält nur eine Zählung je Gitterzelle (Positionen, Labels und Zahlen), nie ein Bild, eine Box oder eine Identität; der Export sagt `contains_images: false`. Eine fehlerhafte Erkennungsdatei, die in der Zeit zurückgeht oder über 16 MiB hat, wird ganz abgelehnt, und die Karte hat eine harte Speichergrenze |

Nichts davon ist eine Sicherheitsfunktion: Es gibt noch kein echtes Erkennungsmodell.""",
      "interfaces": r"""| Name | Was sie festlegt |
|---|---|
| `python -m armor_vision simulate [--config FILE] [--mode MODE]` | Führt ein eingebautes Szenario aus (eine Person quert eine Einfahrt, ein geparktes Auto, Bewegung hinter einem maskierten Baum) und druckt je Ereignis eine JSON-Zeile und zuletzt die Zähler |
| `python -m armor_vision check-config FILE` | Prüft eine Konfiguration und druckt jedes Problem; Exit 0 gut, 1 ungültig, 2 nicht lesbar |
| `python -m armor_vision simulate --simulate-events --activity-config FILE [--seed N] [--detections-file FILE]` | Aktivitätspipeline, AUS, solange die Datei nicht `"enabled": true` sagt (Exit 3 wenn aus): eine synthetische Szene mit festem Seed oder aufgezeichnete Erkennungen ergibt eine JSON-Zeile je Ereignis (`zone_enter`, `zone_exit`, `dwell`, `loiter`, `line_cross`) |
| `python -m armor_vision simulate --heatmap OUT --activity-config FILE` | Schreibt die Heatmap der Aktivität (Zählungen je Zelle, `OUT` endet auf `.json`, `.png` oder `.svg`); nur aggregierte Positionen, niemals Bilder |
| `python -m armor_vision activity-example` / `check-activity-config FILE` | Gibt eine Aktivitätskonfiguration als Ausgangspunkt aus / prüft eine (Exit 0 gut, 1 ungültig, 2 nicht lesbar) |
| `ActivityEngine`, `heatmap_route` | Als Bibliothek: die Engine und der Handler für `GET /heatmap?camera=ID&format=json` (auch `png` und `svg`) für den Dienst, der ihn einbindet; die Route antwortet 404, solange die Pipeline aus ist |
| `python -m armor_vision heatmap-route --activity-config FILE [--detections-file FILE] [--camera ID] [--format json\|png\|svg] [--scale N]` | Beantwortet eine `GET /heatmap`-Anfrage aus aufgezeichneten Erkennungen und gibt die Antwort als eine JSON-Zeile aus (`status`, `content_type`, `body_base64`); das führt ein Server aus, der die Route einbindet. Exit 0 für jede Antwort der Route (auch 404 bei ausgeschalteter Pipeline und 400 bei einer fehlerhaften Anfrage), 1 bei falscher Konfiguration, 2 bei einer nicht lesbaren Datei |
| `python -m armor_vision replay FILE [--config FILE] [--mode MODE]` | Lässt aufgezeichnete Erkennungen (JSON Lines) durch die Zonenregeln laufen und gibt die Ereignisse aus, die jede Zone ausgelöst hätte, mit der Anzahl je Zone (Exit 2 bei unbrauchbarer Datei oder einer Kamera, die nicht in der Konfiguration steht) |
| `OnnxDetector`, `parse_onnx_settings` | Als Bibliothek: ein Detektor, der ein ONNX-Modell auf der CPU ausführt (braucht `onnxruntime`, keine Abhängigkeit; aus, solange er nicht gebaut wird) |
| `python -m armor_vision serve --activity-config FILE [--config FILE] [--service-config FILE]` | Startet den Live-Dienst: Die Aktivitäts-Engine bleibt im Speicher, Erkennungen kommen Beobachtung für Beobachtung herein (`POST /ingest`) und `GET /heatmap` antwortet aus diesem Speicher. Er lauscht auf 127.0.0.1, außer die Einstellungsdatei sagt `allow_remote`, hält kein Geheimnis außer dem Token, den es verlangen kann (offen für andere Rechner muss es einen in einer Datei haben), und schreibt nichts auf die Platte. Exit 1 bei falscher Konfiguration oder ausgeschalteter Aktivität, 2 bei unlesbarer Datei oder nicht zu öffnendem Port Grenzen in der Einstellungsdatei: `request_timeout_s` (ein Client, der verstummt, wird getrennt), `max_connections` (dem nächsten wird mit 503 gesagt, er solle wiederkommen) und `render_cache_entries` (wie viele gezeichnete Karten behalten werden; 0 schaltet es aus). |

```json
{"schema": "armor.vision.event/v1", "type": "alert", "camera_id": "cam-front", "zone_id": "drive",
 "zone_name": "Driveway", "track_id": 1, "label": "person", "confidence": 0.9,
 "box": [0.41, 0.62, 0.47, 0.82], "timestamp": 1.0, "authorizes_action": false}
```

Als Bibliothek: `parse_config`, `Pipeline.process_detections` und `process_frame`. `load_detector("tensorrt")` braucht seine Einstellungen und die Jetson-Pakete, sonst löst es `DetectorUnavailable` aus; mit einer simulierten Engine läuft es überall und nennt seine Evidenz `simulator`. Siehe [docs/USAGE.md](docs/USAGE.md).""",
      "configuration": r"""| Name | Was sie festlegt |
|---|---|
| `motion_threshold` | 1 bis 255: der Graustufenunterschied, der als Änderung zählt |
| `motion_min_cells` | Wie viele Zellen des 16-x-9-Rasters wechseln müssen, bevor der Detektor gefragt wird |
| `zones[]` | `id`, `name`, `kind` (`alert` oder `detection`), `labels`, `min_frames`, `min_seconds`, `points` (Polygon, 0 bis 1); gezählt wird an den Füßen der Box |
| `masks[]` | Polygone, in denen Bewegung ignoriert wird; Erkennungen mit Mittelpunkt darin entfallen |
| `profiles` | Welche Zonen in jedem Scharfschaltmodus überwacht werden (`away`, `home`, ...) |
| `Aktivitätskonfiguration (eigene Datei)` | `enabled` (Standard `false`), `heatmap` (`cols`, `rows`, `window_seconds`, `half_life_seconds`, `slices`, `max_cells` bis 65536, `position`, `labels`) und `events` (`dwell_seconds`, `loiter_seconds`, `loiter_radius`, `lost_seconds`, `labels`, `lines[]` mit `id`, `a`, `b`, `sensitivity_floor` (`low`, `normal`, `high`)); die Heatmap wird als Gewicht geteilt durch das Maximum normiert |

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
python -m unittest discover -s tests   # {{fact:tests:ARMOR-VISION}} tests
```

```bash
PYTHONPATH=src python -m armor_vision simulate --mode away
PYTHONPATH=src python -m armor_vision check-config my_cameras.json
PYTHONPATH=src python -m unittest discover -s tests   # {{fact:tests:ARMOR-VISION}} tests
```""",
      "testing": r"""```powershell
$env:PYTHONPATH = "src"
python -m unittest discover -s tests
python -I tools/armor_ci_validate.py
```

| Testdatei | Tests | Was sie abdeckt |
|---|---|---|
| `test_vision.py` | 42 | Geometrie, Konfiguration, Bewegung, Tracker, Regeln, Profile, die Kette und die Kommandozeile |
| `test_vision_edges.py` | 19 | Die Grenzfälle: falsche Konfigurationen, ruhende Objekte, maskierte Erkennungen und der nicht verfügbare Detektor |
| `test_characterization.py` | 2 | Legt die Ausgabe der eingebauten Simulation Byte für Byte fest, damit sie sich bei ausgeschalteter Aktivitätspipeline nicht ändert |
| `test_activity.py` | 27 | Aktivitätskonfiguration, synthetische und aufgezeichnete Quellen, Ereignisse, Heatmap (Determinismus, Summe gleich Erkennungen, nichts außerhalb des Gitters, Fenster, Abklingen, Speicher), der `/heatmap`-Handler und die Befehlszeile |
| `test_heatmap_service.py` | 7 | Die Heatmap-Route als Befehl: aus ist 404, egal welche Daten, an ohne Daten ist eine leere Karte, Zählungen in den drei Formaten, fehlerhafte Anfragen, und eine falsche Konfiguration oder Datei ist ein Fehler und nie eine leere Karte |
| `test_service.py` | 15 | Der Live-Dienst: dieselbe Karte wie die abgespielte Datei, aus ist 404 und 503, Unverstandenes wird abgelehnt, die Grenzen der Einstellungen, begrenzter Speicher und der Befehl |
| `test_service_load.py` | 7 | Der Live-Dienst unter leichter Last und mit sich schlecht benehmenden Clients: die neuen Grenzen und ihre Bereiche, ein verstummter Client wird getrennt, die gleichzeitigen Anfragen sind begrenzt, exakte Zähler bei vielen Threads, die Zeichnung einer unveränderten Karte wird wiederverwendet und begrenzt, und eine Karte, die gezeichnet wird, hält die Beobachtungen nicht auf |
| `test_tensorrt_and_streams.py` | 21 | Der TensorRT-Detektor mit simulierter Engine, das Streampaar und der Recorder, die Clips mit Vor- und Nachlauf und die Aufbewahrung nach Typ |
| `test_analytics_schedule_phase2.py` | 30 | Geschwindigkeit in einer Zone, zurückgelassene Objekte, der PTZ-Verfolger, die Vektoren eines Ereignisses, der Zeitplan und die standardmäßig ausgeschaltete zweite Phase |""",
      "build": "Es ist reines Python: nichts zu kompilieren. Die Version steht in `pyproject.toml` und `armor.project.json`.",
      "troubleshooting": r"""| Sie sehen | Weil | Tun Sie |
|---|---|---|
| `check-config` endet mit 1 | Die Konfiguration hat Probleme; es listet jedes auf | Behebe alle: Unbekannte Felder sind Fehler |
| `check-config` endet mit 2 | Die Datei kann nicht gelesen werden | Prüfe den Pfad und dass es JSON ist |
| `DetectorUnavailable` | `load_detector("tensorrt")`: keine Einstellungen, keine Engine-Datei oder keine Jetson-Pakete | Gib `TensorrtSettings` und eine Engine-Datei auf dem Jetson an oder nutze `ScriptedDetector` |
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
│   ├── detector.py                      geskriptete, ONNX- und TensorRT-Detektoren (simulierte Engine außerhalb des Jetson)
│   ├── tracker.py                       Identität zwischen Bildern; ruhende Objekte
│   ├── rules.py                         von Zonen zu Ereignissen: armor.vision.event/v1
│   ├── tensorrt_detector.py             der TensorRT-Detektor für den Jetson; eine simulierte Engine
│   ├── streams.py recording.py          Substream zum Analysieren, Hauptstream zum Aufnehmen; Clips und Aufbewahrung
│   ├── analytics.py schedule.py         Geschwindigkeit in einer Zone, zurückgelassene Objekte, PTZ-Verfolgung; Masken nach Uhrzeit
│   ├── phase2.py                        semantische Suche, Kennzeichen, Gesichter: alles aus, mit Datenschutzhinweisen
│   ├── activity_config.py               Einstellungen der Aktivitätspipeline, standardmäßig aus
│   ├── sources.py heatmap.py            synthetische und aufgezeichnete Quellen; Heatmap
│   ├── activity.py                      Ereignisse und der /heatmap-Handler
│   ├── heatmap_service.py               die /heatmap-Route als Befehl
│   ├── service.py                       der Live-Dienst: die Engine im Speicher, POST /ingest und GET /heatmap
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
* Die Kamera- oder RTSP-Quelle der Aktivitätspipeline gehört zur Hardware und ist nicht geschrieben: heute läuft sie mit einer synthetischen Szene oder einer Erkennungsdatei. Die Heatmap hat hier keinen HTTP-Server, nur den Handler.
* Das Ereignis ist noch nicht Teil des ARMOR-COMMON-Vertrags.
* Die Werte von Tracker und Bewegung sind Konstanten im Code, nicht in der Konfigurationsdatei.

**Als Nächstes**

* Das Erkennungsmodell für den Jetson Orin NX schreiben und mit einer echten Kamera erproben.
* Die Konstanten von Tracker und Bewegung in die Konfigurationsdatei verlegen und das Ereignis in den ARMOR-COMMON-Vertrag aufnehmen.""",
    },
  },
  "fr": {
    "tagline": "Zones, masques et règles de détection pour les caméras",
    "honest": "Les zones, le contrôle du mouvement, le suivi, les règles et les {{fact:tests:ARMOR-VISION}} tests sont réels. Le détecteur pour la Jetson Orin NX (TensorRT), les deux flux, les clips, la vitesse, les objets abandonnés, le suivi PTZ, l'horaire et la seconde phase sont écrits et testés seulement avec des moteurs et des sources simulés : rien n'a tourné sur une caméra ni sur la Jetson Orin NX.",
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
        "{{fact:tests:ARMOR-VISION}} (`python -m unittest discover -s tests`)",
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
      "tests": "{{fact:tests:ARMOR-VISION}} tests réussissent (`python -m unittest discover -s tests`).",
      "hardware": "Rien n'a tourné sur une caméra ni sur le Jetson Orin NX.",
      "ui": "Les routes ou les messages proposés sont documentés et testés avec un client ; tous les clients ne les ont pas encore utilisés",
      "security": "Le contrôle d'accès, les limites d'entrée ou les signatures sont implémentés et testés sur un ordinateur ; personne hors du projet ne les a relus",
      "integration": "Ses messages sont validés par rapport aux schémas partagés et aux vecteurs de conformité d'ARMOR-COMMON ; il n'a pas fonctionné avec l'équipement réel",
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
| La chaîne d'activité conserve ou divulgue des images de personnes | Elle est éteinte par défaut ; elle ne garde qu'un compte par cellule de la grille (positions, étiquettes et nombres), jamais une image, une boîte ou une identité ; l'export dit `contains_images: false`. Un fichier de détections mal formé, qui remonte le temps ou de plus de 16 Mio est refusé en entier, et la carte a une limite dure de mémoire |

Rien ici n'est une fonction de sécurité : il n'y a pas encore de vrai modèle de détection.""",
      "interfaces": r"""| Nom | Ce qu'elle règle |
|---|---|
| `python -m armor_vision simulate [--config FILE] [--mode MODE]` | Exécute un scénario intégré (une personne traverse une allée, une voiture garée, un mouvement derrière un arbre masqué) et imprime une ligne JSON par événement puis une ligne de compteurs |
| `python -m armor_vision check-config FILE` | Valide une configuration et imprime chaque problème ; sortie 0 bonne, 1 invalide, 2 illisible |
| `python -m armor_vision simulate --simulate-events --activity-config FILE [--seed N] [--detections-file FILE]` | Chaîne d'activité, ÉTEINTE sauf si le fichier dit `"enabled": true` (code 3 si éteinte) : une scène synthétique à graine fixe, ou des détections enregistrées, donne une ligne JSON par événement (`zone_enter`, `zone_exit`, `dwell`, `loiter`, `line_cross`) |
| `python -m armor_vision simulate --heatmap OUT --activity-config FILE` | Écrit la carte de chaleur de l'activité (comptes par cellule, `OUT` finit par `.json`, `.png` ou `.svg`) ; seulement des positions agrégées, jamais d'images |
| `python -m armor_vision activity-example` / `check-activity-config FILE` | Affiche une configuration d'activité de départ / en valide une (code 0 bon, 1 invalide, 2 illisible) |
| `ActivityEngine`, `heatmap_route` | En bibliothèque : le moteur et le gestionnaire de `GET /heatmap?camera=ID&format=json` (aussi `png` et `svg`), pour le service qui le monte ; la route répond 404 tant que la chaîne est éteinte |
| `python -m armor_vision heatmap-route --activity-config FILE [--detections-file FILE] [--camera ID] [--format json\|png\|svg] [--scale N]` | Répond à une requête `GET /heatmap` à partir de détections enregistrées et affiche la réponse en une ligne JSON (`status`, `content_type`, `body_base64`) ; c'est ce que lance un serveur qui monte la route. Code 0 pour toute réponse de la route (aussi 404 chaîne éteinte et 400 pour une requête fausse), 1 pour une configuration erronée, 2 pour un fichier illisible |
| `python -m armor_vision replay FILE [--config FILE] [--mode MODE]` | Fait passer des détections enregistrées (JSON Lines) par les règles de zone et affiche les événements que chaque zone aurait levés, avec le compte par zone (sortie 2 si le fichier est inutilisable ou la caméra absente de la configuration) |
| `OnnxDetector`, `parse_onnx_settings` | En bibliothèque : un détecteur qui exécute un modèle ONNX sur le CPU (demande `onnxruntime`, qui n'est pas une dépendance ; désactivé tant qu'on ne le construit pas) |
| `python -m armor_vision serve --activity-config FILE [--config FILE] [--service-config FILE]` | Lance le service vivant : le moteur d'activité reste en mémoire, les détections arrivent une observation à la fois (`POST /ingest`) et `GET /heatmap` répond depuis cette mémoire. Il écoute sur 127.0.0.1 sauf si le fichier de réglages dit `allow_remote`, ne détient d'autre secret que le jeton qu'il peut exiger (il doit en avoir un, dans un fichier, s'il est ouvert à d'autres machines) et n'écrit rien sur le disque. Sortie 1 pour une configuration fausse ou une activité éteinte, 2 pour un fichier illisible ou un port impossible à ouvrir Limites dans le fichier de réglages : `request_timeout_s` (un client qui se tait est coupé), `max_connections` (au suivant on dit de revenir avec un 503) et `render_cache_entries` (combien de cartes dessinées sont gardées ; 0 l'éteint). |

```json
{"schema": "armor.vision.event/v1", "type": "alert", "camera_id": "cam-front", "zone_id": "drive",
 "zone_name": "Driveway", "track_id": 1, "label": "person", "confidence": 0.9,
 "box": [0.41, 0.62, 0.47, 0.82], "timestamp": 1.0, "authorizes_action": false}
```

En bibliothèque : `parse_config`, `Pipeline.process_detections` et `process_frame`. `load_detector("tensorrt")` a besoin de ses réglages et des paquets du Jetson, sinon il lève `DetectorUnavailable` ; avec un moteur simulé il tourne partout et indique que sa preuve est `simulator`. Voir [docs/USAGE.md](docs/USAGE.md).""",
      "configuration": r"""| Nom | Ce qu'elle règle |
|---|---|
| `motion_threshold` | 1 à 255 : l'écart de gris qui compte comme changement |
| `motion_min_cells` | Combien de cellules de la grille 16 x 9 doivent changer avant de solliciter le détecteur |
| `zones[]` | `id`, `name`, `kind` (`alert` ou `detection`), `labels`, `min_frames`, `min_seconds`, `points` (polygone, 0 à 1) ; compté par les pieds de la boîte |
| `masks[]` | Polygones où le mouvement est ignoré ; les détections dont le centre est dedans sont écartées |
| `profiles` | Quelles zones sont surveillées dans chaque mode d'armement (`away`, `home`, ...) |
| `configuration d'activité (fichier à part)` | `enabled` (par défaut `false`), `heatmap` (`cols`, `rows`, `window_seconds`, `half_life_seconds`, `slices`, `max_cells` jusqu'à 65536, `position`, `labels`) et `events` (`dwell_seconds`, `loiter_seconds`, `loiter_radius`, `lost_seconds`, `labels`, `lines[]` avec `id`, `a`, `b`, `sensitivity_floor` (`low`, `normal`, `high`)) ; la carte est normalisée comme poids divisé par le maximum |

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
python -m unittest discover -s tests   # {{fact:tests:ARMOR-VISION}} tests
```

```bash
PYTHONPATH=src python -m armor_vision simulate --mode away
PYTHONPATH=src python -m armor_vision check-config my_cameras.json
PYTHONPATH=src python -m unittest discover -s tests   # {{fact:tests:ARMOR-VISION}} tests
```""",
      "testing": r"""```powershell
$env:PYTHONPATH = "src"
python -m unittest discover -s tests
python -I tools/armor_ci_validate.py
```

| Fichier de tests | Tests | Ce qu'il couvre |
|---|---|---|
| `test_vision.py` | 42 | Géométrie, configuration, mouvement, suivi, règles, profils, la chaîne et la ligne de commande |
| `test_vision_edges.py` | 19 | Les cas limites : mauvaises configurations, objets immobiles, détections masquées et détecteur indisponible |
| `test_characterization.py` | 2 | Fixe octet par octet la sortie de la simulation intégrée, pour qu'elle ne change pas tant que la chaîne d'activité est éteinte |
| `test_activity.py` | 27 | Configuration d'activité, sources synthétique et enregistrée, événements, carte de chaleur (déterminisme, somme égale aux détections, rien hors de la grille, fenêtre, décroissance, mémoire), le gestionnaire `/heatmap` et la ligne de commande |
| `test_heatmap_service.py` | 7 | La route de la carte de chaleur en commande : éteinte donne 404 quelles que soient les données, allumée sans données donne une carte vide, comptes dans les trois formats, requêtes fausses, et une configuration ou un fichier faux est une erreur et jamais une carte vide |
| `test_service.py` | 15 | Le service vivant : la même carte que le fichier rejoué, éteint donne 404 et 503, ce qui n'est pas compris est refusé, les limites des réglages, mémoire bornée et la commande |
| `test_service_load.py` | 7 | Le service vivant sous charge légère et avec des clients qui se conduisent mal : les nouvelles limites et leurs plages, un client qui se tait est coupé, les requêtes simultanées sont bornées, compteurs exacts avec beaucoup de fils, le dessin d'une carte inchangée est réutilisé et borné, et une carte en cours de dessin ne retarde pas les observations |
| `test_tensorrt_and_streams.py` | 21 | Le détecteur TensorRT avec un moteur simulé, la paire de flux et l'enregistreur, les clips avec pré et post-capture et la rétention par type |
| `test_analytics_schedule_phase2.py` | 30 | Vitesse dans une zone, objets abandonnés, le suiveur PTZ, les vecteurs d'un événement, l'horaire et la seconde phase éteinte par défaut |""",
      "build": "C'est du Python pur : rien à compiler. La version est dans `pyproject.toml` et `armor.project.json`.",
      "troubleshooting": r"""| Vous voyez | Parce que | Faites |
|---|---|---|
| `check-config` se termine par 1 | La configuration a des problèmes ; il les liste tous | Corrigez-les tous : les champs inconnus sont des erreurs |
| `check-config` se termine par 2 | Le fichier est illisible | Vérifiez le chemin et que c'est du JSON |
| `DetectorUnavailable` | `load_detector("tensorrt")` : pas de réglages, pas de fichier de moteur ou pas de paquets Jetson | Donnez `TensorrtSettings` et un fichier de moteur sur le Jetson, ou utilisez `ScriptedDetector` |
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
│   ├── detector.py                      détecteurs scripté, ONNX et TensorRT (moteur simulé hors Jetson)
│   ├── tracker.py                       identité entre images ; objets immobiles
│   ├── rules.py                         des zones aux événements : armor.vision.event/v1
│   ├── tensorrt_detector.py             le détecteur TensorRT pour le Jetson ; un moteur simulé
│   ├── streams.py recording.py          sous-flux à analyser, flux principal à enregistrer ; clips et rétention
│   ├── analytics.py schedule.py         vitesse dans une zone, objets abandonnés, suivi PTZ ; masques par heure
│   ├── phase2.py                        recherche sémantique, plaques, visages : tout éteint, avec avis de confidentialité
│   ├── activity_config.py               réglages de la chaîne d'activité, éteinte par défaut
│   ├── sources.py heatmap.py            sources synthétique et enregistrée ; carte de chaleur
│   ├── activity.py                      événements et gestionnaire /heatmap
│   ├── heatmap_service.py               la route /heatmap en commande
│   ├── service.py                       le service vivant : le moteur en mémoire, POST /ingest et GET /heatmap
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
* La source caméra ou RTSP de la chaîne d'activité relève du matériel et n'est pas écrite : aujourd'hui elle fonctionne sur une scène synthétique ou un fichier de détections. La carte de chaleur n'a pas ici de serveur HTTP, seulement le gestionnaire.
* L'événement ne fait pas encore partie du contrat d'ARMOR-COMMON.
* Les valeurs du suivi et du mouvement sont des constantes du code, pas du fichier de configuration.

**Ensuite**

* Écrire le modèle de détection pour le Jetson Orin NX et l'essayer avec une vraie caméra.
* Déplacer les constantes du suivi et du mouvement dans le fichier de configuration et mettre l'événement dans le contrat d'ARMOR-COMMON.""",
    },
  },
  "it": {
    "tagline": "Zone, maschere e regole di rilevamento per le telecamere",
    "honest": "Le zone, il controllo del movimento, il tracciamento, le regole e i {{fact:tests:ARMOR-VISION}} test sono reali. Il rilevatore per la Jetson Orin NX (TensorRT), i due flussi, le clip, la velocità, gli oggetti abbandonati, il tracciamento PTZ, l'orario e la seconda fase sono scritti e provati solo con motori e sorgenti simulati: nulla è stato eseguito su una telecamera o sulla Jetson Orin NX.",
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
        "{{fact:tests:ARMOR-VISION}} (`python -m unittest discover -s tests`)",
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
      "tests": "Superano {{fact:tests:ARMOR-VISION}} test (`python -m unittest discover -s tests`).",
      "hardware": "Nulla ha girato su una telecamera né sulla Jetson Orin NX.",
      "ui": "Le rotte o i messaggi offerti sono documentati e provati con un client; non tutti i client li hanno ancora usati",
      "security": "Il controllo degli accessi, i limiti d'ingresso o le firme sono implementati e provati su un computer; nessuno al di fuori del progetto li ha rivisti",
      "integration": "I suoi messaggi sono convalidati rispetto agli schemi condivisi e ai vettori di conformità di ARMOR-COMMON; non ha ancora funzionato insieme all'apparecchiatura reale",
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
| La pipeline di attività conserva o rivela immagini di persone | È spenta per impostazione predefinita; conserva solo un conteggio per cella della griglia (posizioni, etichette e numeri), mai un'immagine, un riquadro o un'identità; l'esportazione dice `contains_images: false`. Un file di rilevamenti malformato, che torna indietro nel tempo o oltre 16 MiB viene rifiutato per intero, e la mappa ha un limite rigido di memoria |

Nulla qui è una funzione di sicurezza: non esiste ancora un vero modello di rilevamento.""",
      "interfaces": r"""| Nome | Cosa imposta |
|---|---|
| `python -m armor_vision simulate [--config FILE] [--mode MODE]` | Esegue uno scenario integrato (una persona attraversa un vialetto, un'auto parcheggiata, movimento dietro un albero mascherato) e stampa una riga JSON per evento e una finale con i contatori |
| `python -m armor_vision check-config FILE` | Valida una configurazione e stampa ogni problema; uscita 0 buona, 1 non valida, 2 illeggibile |
| `python -m armor_vision simulate --simulate-events --activity-config FILE [--seed N] [--detections-file FILE]` | Pipeline di attività, SPENTA salvo che il file dica `"enabled": true` (codice 3 se spenta): una scena sintetica con seme fisso, o rilevamenti registrati, dà una riga JSON per evento (`zone_enter`, `zone_exit`, `dwell`, `loiter`, `line_cross`) |
| `python -m armor_vision simulate --heatmap OUT --activity-config FILE` | Scrive la mappa di calore dell'attività (conteggi per cella, `OUT` termina in `.json`, `.png` o `.svg`); solo posizioni aggregate, mai immagini |
| `python -m armor_vision activity-example` / `check-activity-config FILE` | Stampa una configurazione di attività di partenza / ne convalida una (codice 0 buono, 1 non valida, 2 illeggibile) |
| `ActivityEngine`, `heatmap_route` | Come libreria: il motore e il gestore di `GET /heatmap?camera=ID&format=json` (anche `png` e `svg`), per il servizio che lo monta; la rotta risponde 404 finché la pipeline è spenta |
| `python -m armor_vision heatmap-route --activity-config FILE [--detections-file FILE] [--camera ID] [--format json\|png\|svg] [--scale N]` | Risponde a una richiesta `GET /heatmap` da rilevamenti registrati e stampa la risposta come una riga JSON (`status`, `content_type`, `body_base64`); è ciò che esegue un server che monta la rotta. Codice 0 per ogni risposta della rotta (anche 404 a pipeline spenta e 400 per una richiesta errata), 1 per una configurazione errata, 2 per un file illeggibile |
| `python -m armor_vision replay FILE [--config FILE] [--mode MODE]` | Fa passare rilevamenti registrati (JSON Lines) per le regole di zona e stampa gli eventi che ogni zona avrebbe generato, con il conteggio per zona (uscita 2 se il file non è utilizzabile o la telecamera non è nella configurazione) |
| `OnnxDetector`, `parse_onnx_settings` | Come libreria: un rilevatore che esegue un modello ONNX sulla CPU (richiede `onnxruntime`, che non è una dipendenza; spento finché non lo si costruisce) |
| `python -m armor_vision serve --activity-config FILE [--config FILE] [--service-config FILE]` | Avvia il servizio vivo: il motore di attività resta in memoria, le rilevazioni arrivano un'osservazione alla volta (`POST /ingest`) e `GET /heatmap` risponde da quella memoria. Ascolta su 127.0.0.1 salvo che il file di impostazioni dica `allow_remote`, non custodisce altro segreto che il token che può richiedere (deve averne uno, in un file, se è aperto ad altre macchine) e non scrive nulla su disco. Esce con 1 per una configurazione errata o attività spenta, con 2 per un file illeggibile o una porta che non si apre Limiti nel file di impostazioni: `request_timeout_s` (un client che tace viene chiuso), `max_connections` (al successivo si dice di tornare con un 503) e `render_cache_entries` (quante mappe disegnate si tengono; 0 la spegne). |

```json
{"schema": "armor.vision.event/v1", "type": "alert", "camera_id": "cam-front", "zone_id": "drive",
 "zone_name": "Driveway", "track_id": 1, "label": "person", "confidence": 0.9,
 "box": [0.41, 0.62, 0.47, 0.82], "timestamp": 1.0, "authorizes_action": false}
```

Come libreria: `parse_config`, `Pipeline.process_detections` e `process_frame`. `load_detector("tensorrt")` richiede le sue impostazioni e i pacchetti del Jetson, altrimenti solleva `DetectorUnavailable`; con un motore simulato gira ovunque e dichiara che la sua evidenza è `simulator`. Vedi [docs/USAGE.md](docs/USAGE.md).""",
      "configuration": r"""| Nome | Cosa imposta |
|---|---|
| `motion_threshold` | da 1 a 255: la differenza di grigio che conta come cambiamento |
| `motion_min_cells` | Quante celle della griglia 16 x 9 devono cambiare prima di interpellare il rilevatore |
| `zones[]` | `id`, `name`, `kind` (`alert` o `detection`), `labels`, `min_frames`, `min_seconds`, `points` (poligono, da 0 a 1); si conta dai piedi del riquadro |
| `masks[]` | Poligoni dove il movimento è ignorato; i rilevamenti con il centro all'interno vengono scartati |
| `profiles` | Quali zone sono sorvegliate in ogni modalità di inserimento (`away`, `home`, ...) |
| `configurazione di attività (file a parte)` | `enabled` (predefinito `false`), `heatmap` (`cols`, `rows`, `window_seconds`, `half_life_seconds`, `slices`, `max_cells` fino a 65536, `position`, `labels`) ed `events` (`dwell_seconds`, `loiter_seconds`, `loiter_radius`, `lost_seconds`, `labels`, `lines[]` con `id`, `a`, `b`, `sensitivity_floor` (`low`, `normal`, `high`)); la mappa è normalizzata come peso diviso per il massimo |

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
python -m unittest discover -s tests   # {{fact:tests:ARMOR-VISION}} tests
```

```bash
PYTHONPATH=src python -m armor_vision simulate --mode away
PYTHONPATH=src python -m armor_vision check-config my_cameras.json
PYTHONPATH=src python -m unittest discover -s tests   # {{fact:tests:ARMOR-VISION}} tests
```""",
      "testing": r"""```powershell
$env:PYTHONPATH = "src"
python -m unittest discover -s tests
python -I tools/armor_ci_validate.py
```

| File di test | Test | Cosa copre |
|---|---|---|
| `test_vision.py` | 42 | Geometria, configurazione, movimento, tracker, regole, profili, la catena e la riga di comando |
| `test_vision_edges.py` | 19 | I casi limite: configurazioni errate, oggetti fermi, rilevamenti mascherati e rilevatore non disponibile |
| `test_characterization.py` | 2 | Fissa byte per byte l'uscita della simulazione integrata, così non cambia finché la pipeline di attività è spenta |
| `test_activity.py` | 27 | Configurazione di attività, sorgenti sintetica e registrata, eventi, mappa di calore (determinismo, somma uguale ai rilevamenti, niente fuori dalla griglia, finestra, decadimento, memoria), il gestore `/heatmap` e la riga di comando |
| `test_heatmap_service.py` | 7 | La rotta della mappa di calore come comando: spenta dà 404 qualunque siano i dati, accesa senza dati dà una mappa vuota, conteggi nei tre formati, richieste errate, e una configurazione o un file errati sono un errore e mai una mappa vuota |
| `test_service.py` | 15 | Il servizio vivo: la stessa mappa del file riprodotto, spento dà 404 e 503, ciò che non si capisce viene rifiutato, i limiti delle impostazioni, memoria limitata e il comando |
| `test_service_load.py` | 7 | Il servizio vivo sotto carico leggero e con client che si comportano male: i nuovi limiti e i loro intervalli, un client che tace viene chiuso, le richieste contemporanee sono limitate, contatori esatti con molti thread, il disegno di una mappa invariata viene riusato ed è limitato, e una mappa in corso di disegno non trattiene le osservazioni |
| `test_tensorrt_and_streams.py` | 21 | Il rilevatore TensorRT con motore simulato, la coppia di flussi e il registratore, le clip con pre e post-cattura e la conservazione per tipo |
| `test_analytics_schedule_phase2.py` | 30 | Velocità in una zona, oggetti abbandonati, il seguitore PTZ, i vettori di un evento, l'orario e la seconda fase spenta per impostazione predefinita |""",
      "build": "È Python puro: nulla da compilare. La versione sta in `pyproject.toml` e `armor.project.json`.",
      "troubleshooting": r"""| Vedi | Perché | Fai |
|---|---|---|
| `check-config` termina con 1 | La configurazione ha problemi; li elenca tutti | Correggili tutti: i campi sconosciuti sono errori |
| `check-config` termina con 2 | Il file non può essere letto | Controlla il percorso e che sia JSON |
| `DetectorUnavailable` | `load_detector("tensorrt")`: nessuna impostazione, nessun file di motore o nessun pacchetto Jetson | Dai `TensorrtSettings` e un file di motore sul Jetson, oppure usa `ScriptedDetector` |
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
│   ├── detector.py                      rilevatori scriptato, ONNX e TensorRT (motore simulato fuori dal Jetson)
│   ├── tracker.py                       identità tra immagini; oggetti fermi
│   ├── rules.py                         dalle zone agli eventi: armor.vision.event/v1
│   ├── tensorrt_detector.py             il rilevatore TensorRT per il Jetson; un motore simulato
│   ├── streams.py recording.py          sottoflusso da analizzare, flusso principale da registrare; clip e conservazione
│   ├── analytics.py schedule.py         velocità in una zona, oggetti abbandonati, tracciamento PTZ; maschere per ora
│   ├── phase2.py                        ricerca semantica, targhe, volti: tutto spento, con avvisi sulla privacy
│   ├── activity_config.py               impostazioni della pipeline di attività, spenta di default
│   ├── sources.py heatmap.py            sorgenti sintetica e registrata; mappa di calore
│   ├── activity.py                      eventi e gestore /heatmap
│   ├── heatmap_service.py               la rotta /heatmap come comando
│   ├── service.py                       il servizio vivo: il motore in memoria, POST /ingest e GET /heatmap
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
* La sorgente telecamera o RTSP della pipeline di attività è per l'hardware e non è scritta: oggi funziona su una scena sintetica o un file di rilevamenti. La mappa di calore qui non ha un server HTTP, solo il gestore.
* L'evento non fa ancora parte del contratto di ARMOR-COMMON.
* I valori di tracker e movimento sono costanti nel codice, non nel file di configurazione.

**Prossimi passi**

* Scrivere il modello di rilevamento per il Jetson Orin NX e provarlo con una telecamera reale.
* Spostare le costanti di tracker e movimento nel file di configurazione e inserire l'evento nel contratto di ARMOR-COMMON.""",
    },
  },
  "ja": {
    "tagline": "カメラのゾーン、マスク、検知ルール",
    "honest": "ゾーン、動きの確認、追跡、ルール、{{fact:tests:ARMOR-VISION}} 件のテストは実在します。Jetson Orin NX 用の検知器（TensorRT）、2 本のストリーム、クリップ、速度、置き去り物、PTZ 追従、時間帯設定、第 2 段階は書かれており、模擬のエンジンとソースでのみテストされています。カメラや Jetson Orin NX では何も動かしていません。",
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
        "{{fact:tests:ARMOR-VISION}} (`python -m unittest discover -s tests`)",
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
      "tests": "{{fact:tests:ARMOR-VISION}} 件のテストが通ります（`python -m unittest discover -s tests`）。",
      "hardware": "カメラや Jetson Orin NX ではまだ何も動かしていません。",
      "ui": "提供するルートやメッセージは文書化され、クライアントで試験済みです。すべてのクライアントがまだ使ったわけではありません",
      "security": "アクセス制御、入力の制限、署名のいずれかは実装されコンピューター上で試験済みですが、プロジェクト外の誰もレビューしていません",
      "integration": "メッセージは ARMOR-COMMON の共通スキーマと適合ベクターに照らして検証されていますが、実機と一緒に動かしたことはありません",
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
| アクティビティ処理が人物の画像を保存・漏えいする | 既定ではオフです。保持するのはグリッドのセルごとの件数（位置、ラベル、数値）だけで、画像、ボックス、個人の識別情報は決して保持しません。出力には `contains_images: false` と書かれます。形式が不正な検出ファイル、時間が戻るもの、16 MiB を超えるものは丸ごと拒否され、マップにはメモリの厳格な上限があります |

ここにある機能は安全機能ではありません。実際の検出モデルはまだありません。""",
      "interfaces": r"""| 名前 | 設定内容 |
|---|---|
| `python -m armor_vision simulate [--config FILE] [--mode MODE]` | 組み込みシナリオ（私道を横切る人、駐車中の車、マスクした木の陰の動き）を実行し、イベントごとに JSON 1 行と、最後にカウンターの行を出力します |
| `python -m armor_vision check-config FILE` | 設定を検証してすべての問題を表示します。終了コード 0 正常、1 不正、2 読み取り不可 |
| `python -m armor_vision simulate --simulate-events --activity-config FILE [--seed N] [--detections-file FILE]` | アクティビティ処理は、ファイルに `"enabled": true` と書かない限りオフです（オフのときは終了コード 3）。固定シードの合成シーンまたは記録済みの検出から、イベント（`zone_enter`、`zone_exit`、`dwell`、`loiter`、`line_cross`）ごとに JSON の 1 行を出力します |
| `python -m armor_vision simulate --heatmap OUT --activity-config FILE` | アクティビティのヒートマップ（セルごとの件数、`OUT` は `.json`、`.png`、`.svg` のいずれかで終わる）を書き出します。集計した位置だけで、画像は決して含みません |
| `python -m armor_vision activity-example` / `check-activity-config FILE` | 出発点となるアクティビティ設定を表示 / 設定を検証します（終了コード 0 正常、1 不正、2 読み取り不可） |
| `ActivityEngine`, `heatmap_route` | ライブラリとして：エンジンと `GET /heatmap?camera=ID&format=json`（`png`、`svg` も可）のハンドラ。これを載せるサービス向けで、処理がオフの間はルートは 404 を返します |
| `python -m armor_vision heatmap-route --activity-config FILE [--detections-file FILE] [--camera ID] [--format json\|png\|svg] [--scale N]` | 記録された検出から `GET /heatmap` の問い合わせ 1 件に答え、答えを 1 行の JSON（`status`、`content_type`、`body_base64`）で出力します。ルートを載せるサーバーが実行するものです。ルートの答えはすべて終了コード 0（処理オフの 404 と不正な問い合わせの 400 も）、設定が誤りなら 1、読めないファイルなら 2 |
| `python -m armor_vision replay FILE [--config FILE] [--mode MODE]` | 記録された検出（JSON Lines）をゾーンルールに通し、各ゾーンが上げたであろうイベントとゾーンごとの件数を表示します（使えないファイルや設定にないカメラは終了コード 2） |
| `OnnxDetector`, `parse_onnx_settings` | ライブラリとして: CPU で ONNX モデルを実行する検出器（`onnxruntime` が必要だが依存関係ではない。構築しない限りオフ） |
| `python -m armor_vision serve --activity-config FILE [--config FILE] [--service-config FILE]` | ライブサービスを起動します。アクティビティエンジンはメモリに残り、検出は観測ごとに入り（`POST /ingest`）、`GET /heatmap` はそのメモリから答えます。設定ファイルに `allow_remote` がない限り 127.0.0.1 で待ち受け、要求できるトークン以外の秘密は持たず（他のマシンに開く場合はファイルにトークンが必須）、ディスクには何も書きません。設定の誤りやアクティビティがオフの場合は終了コード 1、ファイルが読めない場合やポートを開けない場合は 2 設定ファイルの上限：`request_timeout_s`（黙り込んだクライアントは切断）、`max_connections`（次の接続には 503 で出直すよう伝える）、`render_cache_entries`（描画済みの地図を保持する数。0 で無効）。 |

```json
{"schema": "armor.vision.event/v1", "type": "alert", "camera_id": "cam-front", "zone_id": "drive",
 "zone_name": "Driveway", "track_id": 1, "label": "person", "confidence": 0.9,
 "box": [0.41, 0.62, 0.47, 0.82], "timestamp": 1.0, "authorizes_action": false}
```

ライブラリとして：`parse_config`、`Pipeline.process_detections`、`process_frame`。`load_detector("tensorrt")` にはその設定と Jetson のパッケージが必要で、無ければ `DetectorUnavailable` を送出します。模擬エンジンならどこでも動き、証拠は `simulator` と示されます。[docs/USAGE.md](docs/USAGE.md) を参照。""",
      "configuration": r"""| 名前 | 設定内容 |
|---|---|
| `motion_threshold` | 1〜255：変化とみなす濃淡差 |
| `motion_min_cells` | 検出器を呼ぶ前に変化が必要な 16 x 9 グリッドのセル数 |
| `zones[]` | `id`、`name`、`kind`（`alert` または `detection`）、`labels`、`min_frames`、`min_seconds`、`points`（多角形、0〜1）。ボックスの足元で判定 |
| `masks[]` | 動きを無視する多角形。中心が内側にある検出は破棄されます |
| `profiles` | 警戒モードごとに監視するゾーン（`away`、`home` など） |
| `アクティビティ設定（別ファイル）` | `enabled`（既定 `false`）、`heatmap`（`cols`、`rows`、`window_seconds`、`half_life_seconds`、`slices`、65536 までの `max_cells`、`position`、`labels`）、`events`（`dwell_seconds`、`loiter_seconds`、`loiter_radius`、`lost_seconds`、`labels`、`id`・`a`・`b` を持つ `lines[]`、`sensitivity_floor`（`low`、`normal`、`high`））。ヒートマップは重みを最大値で割って正規化します |

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
python -m unittest discover -s tests   # {{fact:tests:ARMOR-VISION}} tests
```

```bash
PYTHONPATH=src python -m armor_vision simulate --mode away
PYTHONPATH=src python -m armor_vision check-config my_cameras.json
PYTHONPATH=src python -m unittest discover -s tests   # {{fact:tests:ARMOR-VISION}} tests
```""",
      "testing": r"""```powershell
$env:PYTHONPATH = "src"
python -m unittest discover -s tests
python -I tools/armor_ci_validate.py
```

| テストファイル | テスト数 | 対象 |
|---|---|---|
| `test_vision.py` | 42 | 幾何、設定、動き、トラッカー、ルール、プロファイル、全体の流れ、コマンドライン |
| `test_vision_edges.py` | 19 | 境界条件：不正な設定、静止物、マスクされた検出、利用できない検出器 |
| `test_characterization.py` | 2 | 組み込みシミュレーションの出力をバイト単位で固定し、アクティビティ処理がオフの間は変わらないようにします |
| `test_activity.py` | 27 | アクティビティ設定、合成と記録のソース、イベント、ヒートマップ（決定性、合計が検出数と一致、グリッド外なし、ウィンドウ、減衰、メモリ）、`/heatmap` ハンドラ、コマンドライン |
| `test_heatmap_service.py` | 7 | コマンドとしてのヒートマップのルート：オフならデータに関係なく 404、オンでデータなしなら空の地図、3 つの形式での件数、不正な問い合わせ、誤った設定やファイルはエラーであり空の地図にはならない |
| `test_service.py` | 15 | ライブサービス：再生したファイルと同じマップ、オフなら 404 と 503、理解できないものは拒否、設定の上限、メモリの上限、コマンド |
| `test_service_load.py` | 7 | 軽い負荷と行儀の悪いクライアントの下でのライブサービス：新しい上限とその範囲、黙り込んだクライアントの切断、同時リクエストの上限、多数のスレッドでも正確なカウンター、変化のない地図の描画の再利用とその上限、描画中の地図が観測を妨げないこと |
| `test_tensorrt_and_streams.py` | 21 | 模擬エンジンの TensorRT 検知器、ストリームの組と録画、前後キャプチャ付きクリップ、種類別の保存期間 |
| `test_analytics_schedule_phase2.py` | 30 | ゾーン内の速度、置き去り物、PTZ 追従、イベントのベクトル、時間帯設定、既定でオフの第 2 段階 |""",
      "build": "純粋な Python なのでコンパイルは不要です。バージョンは `pyproject.toml` と `armor.project.json` にあります。",
      "troubleshooting": r"""| 症状 | 原因 | 対処 |
|---|---|---|
| `check-config` が終了コード 1 | 設定に問題があり、すべて表示される | すべて直す（未知のフィールドもエラー） |
| `check-config` が終了コード 2 | ファイルを読み取れない | パスと JSON 形式を確認する |
| `DetectorUnavailable` | `load_detector("tensorrt")`：設定、エンジンファイル、または Jetson のパッケージが無い | Jetson 上で `TensorrtSettings` とエンジンファイルを渡すか、`ScriptedDetector` を使う |
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
│   ├── detector.py                      スクリプト化・ONNX・TensorRT の検知器（Jetson 以外では模擬エンジン）
│   ├── tracker.py                       画像間の識別、静止物
│   ├── rules.py                         ゾーンからイベントへ：armor.vision.event/v1
│   ├── tensorrt_detector.py             Jetson 用の TensorRT 検知器。模擬エンジン
│   ├── streams.py recording.py          解析用サブストリームと録画用メインストリーム。クリップと保存期間
│   ├── analytics.py schedule.py         ゾーン内の速度、置き去り物、PTZ 追従。時間帯別マスク
│   ├── phase2.py                        意味検索、ナンバープレート、顔：すべて既定でオフ、プライバシー通知付き
│   ├── activity_config.py               アクティビティ処理の設定（既定でオフ）
│   ├── sources.py heatmap.py            合成・記録ソース、ヒートマップ
│   ├── activity.py                      イベントと /heatmap ハンドラ
│   ├── heatmap_service.py               /heatmap ルートをコマンドとして
│   ├── service.py                       ライブサービス：メモリ上のエンジン、POST /ingest と GET /heatmap
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
* アクティビティ処理のカメラまたは RTSP ソースはハードウェア向けで未実装です。現在は合成シーンまたは検出ファイルで動作します。ヒートマップにはここでは HTTP サーバーはなく、ハンドラだけがあります。
* イベントはまだ ARMOR-COMMON のコントラクトに含まれていません。
* トラッカーと動き判定の値は設定ファイルではなくコード内の定数です。

**今後**

* Jetson Orin NX 用の検出モデルを書き、実際のカメラで試す。
* トラッカーと動き判定の定数を設定ファイルへ移し、イベントを ARMOR-COMMON のコントラクトに入れる。""",
    },
  },
  "zh": {
    "tagline": "摄像头的区域、遮罩与检测规则",
    "honest": "区域、运动检查、跟踪、规则和 {{fact:tests:ARMOR-VISION}} 个测试都是真实的。面向 Jetson Orin NX 的检测器（TensorRT）、双码流、片段、速度、遗留物、PTZ 跟随、时间表和第二阶段都已编写，并且只用模拟的引擎和来源测试过：没有在任何摄像头或 Jetson Orin NX 上运行过。",
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
        "{{fact:tests:ARMOR-VISION}} (`python -m unittest discover -s tests`)",
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
      "tests": "{{fact:tests:ARMOR-VISION}} 项测试通过（`python -m unittest discover -s tests`）。",
      "hardware": "还没有在摄像头或 Jetson Orin NX 上运行过。",
      "ui": "提供的路由或消息已有文档，并用客户端测试过；尚未被所有客户端使用",
      "security": "访问控制、输入限制或签名已实现并在计算机上测试；项目之外无人审查过",
      "integration": "其消息已对照 ARMOR-COMMON 的共享模式和一致性向量验证；尚未与真实设备一起运行",
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
| 活动管线保存或泄露人的图像 | 默认关闭；只保留网格每个格子的计数（位置、标签和数字），绝不保留图像、框或身份；导出内容注明 `contains_images: false`。格式错误、时间倒退或超过 16 MiB 的检测文件会被整体拒绝，热力图有硬性的内存上限 |

这里没有任何安全功能：目前还没有真实的检测模型。""",
      "interfaces": r"""| 名称 | 作用 |
|---|---|
| `python -m armor_vision simulate [--config FILE] [--mode MODE]` | 运行内置场景（有人穿过车道、停放的汽车、被遮罩的树后有动静），每个事件输出一行 JSON，最后输出计数器 |
| `python -m armor_vision check-config FILE` | 校验配置并输出所有问题；退出码 0 正常、1 无效、2 无法读取 |
| `python -m armor_vision simulate --simulate-events --activity-config FILE [--seed N] [--detections-file FILE]` | 活动管线默认关闭，除非文件写明 `"enabled": true`（关闭时退出码为 3）：用固定种子的合成场景或已记录的检测，每个事件输出一行 JSON（`zone_enter`、`zone_exit`、`dwell`、`loiter`、`line_cross`） |
| `python -m armor_vision simulate --heatmap OUT --activity-config FILE` | 写出活动热力图（每个格子的计数，`OUT` 以 `.json`、`.png` 或 `.svg` 结尾）；只含汇总后的位置，绝不含图像 |
| `python -m armor_vision activity-example` / `check-activity-config FILE` | 打印一份可作起点的活动配置 / 校验一份配置（退出码 0 正常，1 无效，2 无法读取） |
| `ActivityEngine`, `heatmap_route` | 作为库：引擎以及 `GET /heatmap?camera=ID&format=json`（也支持 `png` 和 `svg`）的处理器，供挂载它的服务使用；管线关闭时该路由返回 404 |
| `python -m armor_vision heatmap-route --activity-config FILE [--detections-file FILE] [--camera ID] [--format json\|png\|svg] [--scale N]` | 根据记录的检测结果回答一次 `GET /heatmap` 查询，并把答案作为一行 JSON（`status`、`content_type`、`body_base64`）输出；挂载该路由的服务器运行的就是它。路由的每个答案都以 0 退出（管线关闭时的 404 和查询有误时的 400 也是），配置错误退出 1，文件无法读取退出 2 |
| `python -m armor_vision replay FILE [--config FILE] [--mode MODE]` | 让记录的检测（JSON Lines）通过区域规则，并打印每个区域本会触发的事件及各区域计数（文件不可用或摄像头不在配置中时退出码为 2） |
| `OnnxDetector`, `parse_onnx_settings` | 作为库：在 CPU 上运行 ONNX 模型的检测器（需要 `onnxruntime`，它不是依赖项；不构建就保持关闭） |
| `python -m armor_vision serve --activity-config FILE [--config FILE] [--service-config FILE]` | 运行实时服务：活动引擎常驻内存，检测逐次观测传入（`POST /ingest`），`GET /heatmap` 直接从该内存应答。除非设置文件写明 `allow_remote`，否则只监听 127.0.0.1，除可要求的令牌外不保存任何密钥（向其他机器开放时必须在文件中提供令牌），也不向磁盘写入任何内容。配置错误或活动管线关闭时退出码为 1，文件无法读取或端口无法打开时为 2 设置文件中的上限：`request_timeout_s`（沉默的客户端会被断开）、`max_connections`（下一个连接会收到 503，请稍后再来）、`render_cache_entries`（保留多少张已绘制的地图；0 为关闭）。 |

```json
{"schema": "armor.vision.event/v1", "type": "alert", "camera_id": "cam-front", "zone_id": "drive",
 "zone_name": "Driveway", "track_id": 1, "label": "person", "confidence": 0.9,
 "box": [0.41, 0.62, 0.47, 0.82], "timestamp": 1.0, "authorizes_action": false}
```

作为库使用：`parse_config`、`Pipeline.process_detections` 和 `process_frame`。`load_detector("tensorrt")` 需要它的设置和 Jetson 软件包，否则会抛出 `DetectorUnavailable`；使用模拟引擎时可在任何地方运行，并声明其证据为 `simulator`。参见 [docs/USAGE.md](docs/USAGE.md)。""",
      "configuration": r"""| 名称 | 作用 |
|---|---|
| `motion_threshold` | 1 到 255：被视为变化的灰度差 |
| `motion_min_cells` | 调用检测器前必须变化的 16 x 9 网格单元数 |
| `zones[]` | `id`、`name`、`kind`（`alert` 或 `detection`）、`labels`、`min_frames`、`min_seconds`、`points`（多边形，0 到 1）；按框的脚部计数 |
| `masks[]` | 忽略运动的多边形；中心位于其中的检测会被丢弃 |
| `profiles` | 每种布防模式下监视哪些区域（`away`、`home` 等） |
| `活动配置（单独的文件）` | `enabled`（默认 `false`）、`heatmap`（`cols`、`rows`、`window_seconds`、`half_life_seconds`、`slices`、最大 65536 的 `max_cells`、`position`、`labels`）和 `events`（`dwell_seconds`、`loiter_seconds`、`loiter_radius`、`lost_seconds`、`labels`、含 `id`、`a`、`b` 的 `lines[]`、`sensitivity_floor`（`low`、`normal`、`high`））；热力图按权重除以最大值归一化 |

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
python -m unittest discover -s tests   # {{fact:tests:ARMOR-VISION}} tests
```

```bash
PYTHONPATH=src python -m armor_vision simulate --mode away
PYTHONPATH=src python -m armor_vision check-config my_cameras.json
PYTHONPATH=src python -m unittest discover -s tests   # {{fact:tests:ARMOR-VISION}} tests
```""",
      "testing": r"""```powershell
$env:PYTHONPATH = "src"
python -m unittest discover -s tests
python -I tools/armor_ci_validate.py
```

| 测试文件 | 测试数 | 覆盖内容 |
|---|---|---|
| `test_vision.py` | 42 | 几何、配置、运动、跟踪、规则、配置文件、流程和命令行 |
| `test_vision_edges.py` | 19 | 边界情况：错误配置、静止物体、被遮罩的检测以及不可用的检测器 |
| `test_characterization.py` | 2 | 逐字节固定内置模拟的输出，使活动管线关闭时它不会改变 |
| `test_activity.py` | 27 | 活动配置、合成与记录的来源、事件、热力图（确定性、总和等于检测数、网格之外没有内容、窗口、衰减、内存）、`/heatmap` 处理器和命令行 |
| `test_heatmap_service.py` | 7 | 作为命令的热力图路由：关闭时无论数据如何都返回 404，开启但没有数据时返回空图，三种格式下的计数，错误的查询，以及错误的配置或文件会报错，绝不会变成空图 |
| `test_service.py` | 15 | 实时服务：与回放文件相同的地图，关闭时返回 404 和 503，无法理解的内容被拒绝，设置的限制，内存有上限，以及命令 |
| `test_service_load.py` | 7 | 轻负载和行为不良的客户端下的实时服务：新的上限及其范围、沉默的客户端被断开、同时请求数有上限、多线程下计数器精确、未变化地图的绘制被复用且有上限、正在绘制的地图不会阻塞观测 |
| `test_tensorrt_and_streams.py` | 21 | 使用模拟引擎的 TensorRT 检测器、码流对与录制器、带前后捕获的片段以及按类型的保留 |
| `test_analytics_schedule_phase2.py` | 30 | 区域内速度、遗留物、PTZ 跟随器、事件的向量、时间表以及默认关闭的第二阶段 |""",
      "build": "纯 Python：无需编译。版本在 `pyproject.toml` 和 `armor.project.json` 中。",
      "troubleshooting": r"""| 现象 | 原因 | 处理 |
|---|---|---|
| `check-config` 退出码为 1 | 配置有问题，会逐条列出 | 全部修正：未知字段也算错误 |
| `check-config` 退出码为 2 | 无法读取文件 | 检查路径以及是否为 JSON |
| `DetectorUnavailable` | `load_detector("tensorrt")`：没有设置、没有引擎文件或没有 Jetson 软件包 | 在 Jetson 上提供 `TensorrtSettings` 和引擎文件，或使用 `ScriptedDetector` |
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
│   ├── detector.py                      脚本化、ONNX 和 TensorRT 检测器（非 Jetson 上用模拟引擎）
│   ├── tracker.py                       跨画面的身份；静止物体
│   ├── rules.py                         从区域到事件：armor.vision.event/v1
│   ├── tensorrt_detector.py             Jetson 的 TensorRT 检测器；模拟引擎
│   ├── streams.py recording.py          用于分析的子码流和用于录制的主码流；片段与保留
│   ├── analytics.py schedule.py         区域内速度、遗留物、PTZ 跟随；按时间的遮罩
│   ├── phase2.py                        语义搜索、车牌、人脸：默认全部关闭，附隐私提示
│   ├── activity_config.py               活动管线设置，默认关闭
│   ├── sources.py heatmap.py            合成与记录的来源；热力图
│   ├── activity.py                      事件与 /heatmap 处理器
│   ├── heatmap_service.py               作为命令的 /heatmap 路由
│   ├── service.py                       实时服务：内存中的引擎、POST /ingest 与 GET /heatmap
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
* 活动管线的摄像头或 RTSP 来源属于硬件部分，尚未编写：目前使用合成场景或检测文件运行。热力图在这里没有 HTTP 服务器，只有处理器。
* 该事件尚未纳入 ARMOR-COMMON 合约。
* 跟踪与运动的数值是代码中的常量，不在配置文件中。

**下一步**

* 为 Jetson Orin NX 编写检测模型，并用真实摄像头试验。
* 把跟踪与运动常量移到配置文件，并将该事件纳入 ARMOR-COMMON 合约。""",
    },
  },
  "pt": {
    "tagline": "Zonas, máscaras e regras de deteção para as câmaras",
    "honest": "As zonas, a verificação de movimento, o seguidor, as regras e os {{fact:tests:ARMOR-VISION}} testes são reais. O detetor para o Jetson Orin NX (TensorRT), as duas correntes, os clipes, a velocidade, os objetos abandonados, o seguimento PTZ, o horário e a segunda fase estão escritos e testados só com motores e fontes simulados: nada correu numa câmara nem no Jetson Orin NX.",
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
        "{{fact:tests:ARMOR-VISION}} (`python -m unittest discover -s tests`)",
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
      "tests": "Passam {{fact:tests:ARMOR-VISION}} testes (`python -m unittest discover -s tests`).",
      "hardware": "Nada funcionou numa câmara nem no Jetson Orin NX.",
      "ui": "As rotas ou mensagens que oferece estão documentadas e testadas com um cliente; ainda nem todos os clientes as usaram",
      "security": "O controlo de acesso, os limites de entrada ou as assinaturas estão implementados e testados num computador; ninguém fora do projeto os reviu",
      "integration": "As suas mensagens são validadas contra os esquemas partilhados e os vetores de conformidade do ARMOR-COMMON; ainda não funcionou em conjunto com o equipamento real",
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
| A cadeia de atividade guarda ou divulga imagens de pessoas | Está desligada por defeito; guarda apenas uma contagem por célula da grelha (posições, etiquetas e números), nunca uma imagem, uma caixa ou uma identidade; a exportação diz `contains_images: false`. Um ficheiro de deteções mal formado, que recua no tempo ou com mais de 16 MiB é recusado por inteiro, e o mapa tem um limite rígido de memória |

Nada aqui é uma função de segurança: ainda não há um modelo de deteção real.""",
      "interfaces": r"""| Nome | O que define |
|---|---|
| `python -m armor_vision simulate [--config FILE] [--mode MODE]` | Executa um cenário integrado (uma pessoa atravessa um acesso, um carro estacionado, movimento atrás de uma árvore mascarada) e imprime uma linha JSON por evento e uma última com os contadores |
| `python -m armor_vision check-config FILE` | Valida uma configuração e imprime cada problema; saída 0 boa, 1 inválida, 2 ilegível |
| `python -m armor_vision simulate --simulate-events --activity-config FILE [--seed N] [--detections-file FILE]` | Cadeia de atividade, DESLIGADA salvo se o ficheiro disser `"enabled": true` (código 3 se estiver desligada): uma cena sintética com semente fixa, ou deteções gravadas, dá uma linha JSON por evento (`zone_enter`, `zone_exit`, `dwell`, `loiter`, `line_cross`) |
| `python -m armor_vision simulate --heatmap OUT --activity-config FILE` | Escreve o mapa de calor da atividade (contagens por célula, `OUT` termina em `.json`, `.png` ou `.svg`); só posições agregadas, nunca imagens |
| `python -m armor_vision activity-example` / `check-activity-config FILE` | Imprime uma configuração de atividade para começar / valida uma (código 0 bom, 1 inválida, 2 ilegível) |
| `ActivityEngine`, `heatmap_route` | Como biblioteca: o motor e o tratador de `GET /heatmap?camera=ID&format=json` (também `png` e `svg`), para o serviço que o monta; a rota responde 404 enquanto a cadeia estiver desligada |
| `python -m armor_vision heatmap-route --activity-config FILE [--detections-file FILE] [--camera ID] [--format json\|png\|svg] [--scale N]` | Responde a um pedido `GET /heatmap` a partir de deteções gravadas e imprime a resposta como uma linha JSON (`status`, `content_type`, `body_base64`); é o que executa um servidor que monta a rota. Código 0 para qualquer resposta da rota (também 404 com a cadeia desligada e 400 num pedido errado), 1 se a configuração estiver errada, 2 se um ficheiro não puder ser lido |
| `python -m armor_vision replay FILE [--config FILE] [--mode MODE]` | Passa deteções gravadas (JSON Lines) pelas regras de zona e imprime os eventos que cada zona teria gerado, com a contagem por zona (saída 2 se o ficheiro não servir ou a câmara não estiver na configuração) |
| `OnnxDetector`, `parse_onnx_settings` | Como biblioteca: um detetor que executa um modelo ONNX no CPU (precisa de `onnxruntime`, que não é dependência; desligado enquanto não for construído) |
| `python -m armor_vision serve --activity-config FILE [--config FILE] [--service-config FILE]` | Executa o serviço vivo: o motor de atividade fica em memória, as deteções entram uma observação de cada vez (`POST /ingest`) e `GET /heatmap` responde a partir dessa memória. Escuta em 127.0.0.1 a não ser que o ficheiro de definições diga `allow_remote`, não guarda mais segredo do que o token que pode exigir (tem de o ter, num ficheiro, se estiver aberto a outras máquinas) e não escreve nada em disco. Sai com 1 se a configuração estiver errada ou a atividade desligada, com 2 se um ficheiro não puder ser lido ou a porta não abrir Limites no ficheiro de definições: `request_timeout_s` (um cliente que fica calado é cortado), `max_connections` (ao seguinte diz-se que volte com um 503) e `render_cache_entries` (quantos mapas desenhados se guardam; 0 desliga-o). |

```json
{"schema": "armor.vision.event/v1", "type": "alert", "camera_id": "cam-front", "zone_id": "drive",
 "zone_name": "Driveway", "track_id": 1, "label": "person", "confidence": 0.9,
 "box": [0.41, 0.62, 0.47, 0.82], "timestamp": 1.0, "authorizes_action": false}
```

Como biblioteca: `parse_config`, `Pipeline.process_detections` e `process_frame`. `load_detector("tensorrt")` precisa das suas definições e dos pacotes do Jetson; se não, lança `DetectorUnavailable`. Com um motor simulado corre em qualquer lado e declara que a sua evidência é `simulator`. Consulte [docs/USAGE.md](docs/USAGE.md).""",
      "configuration": r"""| Nome | O que define |
|---|---|
| `motion_threshold` | 1 a 255: a diferença de cinzento que conta como mudança |
| `motion_min_cells` | Quantas células da grelha 16 x 9 têm de mudar antes de consultar o detetor |
| `zones[]` | `id`, `name`, `kind` (`alert` ou `detection`), `labels`, `min_frames`, `min_seconds`, `points` (polígono, 0 a 1); conta-se pelos pés da caixa |
| `masks[]` | Polígonos onde o movimento é ignorado; as deteções com o centro lá dentro são descartadas |
| `profiles` | Que zonas são vigiadas em cada modo de armação (`away`, `home`, ...) |
| `configuração de atividade (ficheiro à parte)` | `enabled` (por defeito `false`), `heatmap` (`cols`, `rows`, `window_seconds`, `half_life_seconds`, `slices`, `max_cells` até 65536, `position`, `labels`) e `events` (`dwell_seconds`, `loiter_seconds`, `loiter_radius`, `lost_seconds`, `labels`, `lines[]` com `id`, `a`, `b`, `sensitivity_floor` (`low`, `normal`, `high`)); o mapa é normalizado como peso dividido pelo máximo |

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
python -m unittest discover -s tests   # {{fact:tests:ARMOR-VISION}} tests
```

```bash
PYTHONPATH=src python -m armor_vision simulate --mode away
PYTHONPATH=src python -m armor_vision check-config my_cameras.json
PYTHONPATH=src python -m unittest discover -s tests   # {{fact:tests:ARMOR-VISION}} tests
```""",
      "testing": r"""```powershell
$env:PYTHONPATH = "src"
python -m unittest discover -s tests
python -I tools/armor_ci_validate.py
```

| Ficheiro de testes | Testes | O que cobre |
|---|---|---|
| `test_vision.py` | 42 | Geometria, configuração, movimento, seguimento, regras, perfis, a cadeia e a linha de comandos |
| `test_vision_edges.py` | 19 | Os casos-limite: configurações erradas, objetos parados, deteções mascaradas e o detetor indisponível |
| `test_characterization.py` | 2 | Fixa byte a byte a saída da simulação incorporada, para que não mude enquanto a cadeia de atividade estiver desligada |
| `test_activity.py` | 27 | Configuração de atividade, fontes sintética e gravada, eventos, mapa de calor (determinismo, soma igual às deteções, nada fora da grelha, janela, decaimento, memória), o tratador de `/heatmap` e a linha de comandos |
| `test_heatmap_service.py` | 7 | A rota do mapa de calor como comando: desligada dá 404 sejam quais forem os dados, ligada sem dados dá um mapa vazio, contagens nos três formatos, pedidos errados, e uma configuração ou um ficheiro errados são um erro e nunca um mapa vazio |
| `test_service.py` | 15 | O serviço vivo: o mesmo mapa que o ficheiro reproduzido, desligado dá 404 e 503, o que não se entende é recusado, os limites das definições, memória limitada e o comando |
| `test_service_load.py` | 7 | O serviço vivo com carga ligeira e com clientes que se portam mal: os novos limites e os seus intervalos, o cliente que fica calado é cortado, os pedidos em simultâneo são limitados, contadores exatos com muitos fios, o desenho de um mapa sem alterações é reutilizado e limitado, e um mapa em desenho não atrasa as observações |
| `test_tensorrt_and_streams.py` | 21 | O detetor TensorRT com motor simulado, o par de correntes e o gravador, os clipes com pré e pós-captura e a retenção por tipo |
| `test_analytics_schedule_phase2.py` | 30 | Velocidade numa zona, objetos abandonados, o seguidor PTZ, os vetores de um evento, o horário e a segunda fase desligada por omissão |""",
      "build": "É Python puro: nada a compilar. A versão está em `pyproject.toml` e `armor.project.json`.",
      "troubleshooting": r"""| Vê | Porque | Faça |
|---|---|---|
| `check-config` termina com 1 | A configuração tem problemas; lista-os todos | Corrija-os todos: os campos desconhecidos são erros |
| `check-config` termina com 2 | Não é possível ler o ficheiro | Verifique o caminho e que é JSON |
| `DetectorUnavailable` | `load_detector("tensorrt")`: sem definições, sem ficheiro do motor ou sem os pacotes do Jetson | Dê `TensorrtSettings` e um ficheiro do motor no Jetson, ou use `ScriptedDetector` |
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
│   ├── detector.py                      detetores com guião, ONNX e TensorRT (motor simulado fora do Jetson)
│   ├── tracker.py                       identidade entre imagens; objetos parados
│   ├── rules.py                         das zonas aos eventos: armor.vision.event/v1
│   ├── tensorrt_detector.py             o detetor TensorRT para o Jetson; um motor simulado
│   ├── streams.py recording.py          subcorrente a analisar, principal a gravar; clipes e retenção
│   ├── analytics.py schedule.py         velocidade numa zona, objetos abandonados, seguimento PTZ; máscaras por hora
│   ├── phase2.py                        pesquisa semântica, matrículas, rostos: tudo desligado, com avisos de privacidade
│   ├── activity_config.py               definições da cadeia de atividade, desligada por defeito
│   ├── sources.py heatmap.py            fontes sintética e gravada; mapa de calor
│   ├── activity.py                      eventos e tratador de /heatmap
│   ├── heatmap_service.py               a rota /heatmap como comando
│   ├── service.py                       o serviço vivo: o motor em memória, POST /ingest e GET /heatmap
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
* A fonte de câmara ou RTSP da cadeia de atividade é para o hardware e não está escrita: hoje funciona com uma cena sintética ou um ficheiro de deteções. O mapa de calor não tem aqui servidor HTTP, apenas o tratador.
* O evento ainda não faz parte do contrato do ARMOR-COMMON.
* Os valores do seguimento e do movimento são constantes no código, não no ficheiro de configuração.

**A seguir**

* Escrever o modelo de deteção para o Jetson Orin NX e experimentá-lo com uma câmara real.
* Passar as constantes do seguimento e do movimento para o ficheiro de configuração e pôr o evento no contrato do ARMOR-COMMON.""",
    },
  },
}
