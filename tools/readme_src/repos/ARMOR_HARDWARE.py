# The facts that do not depend on the language, and the words of every language, of ARMOR-HARDWARE, in the universal README layout.
# Copyright (C) 2026 JuanenRac (Electro Hobby 3D). GPL-3.0-or-later.

FACTS = {
  "emoji": "🧱",
  "layout": "universal",
  "license_badge": "License-GPL%203.0--or--later-blue",
  "status": [
    [
      "software",
      "yellow",
    ],
    [
      "tests",
      "yellow",
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
      "CAD",
      "OpenSCAD",
      "f9d72c",
    ],
    [
      "Tests",
      "22%20passing",
      "2ea44f",
    ],
  ],
}

TEXT = {
  "en": {
    "tagline": "Enclosures, electronics and the bench acceptance matrix",
    "honest": "The radar enclosure is a **printable mechanical starting point, not an IP, RF or thermal rating**, and the parametric box for the solar, electrical and alarm nodes is checked by the asserts of its source (the board fits, the cable holes fit, the lid clears the posts), but **none has been printed or measured** (the board sizes come from data sheets; the touch panel has no printed box, it keeps its factory enclosure). Every row of the [bench acceptance matrix](docs/BENCH_ACCEPTANCE.md) is *not tested*.",
    "glance": [
      [
        "Role",
        "Enclosures, electronics and the bench acceptance matrix (family: Hardware, parent: ARMOR-NODE-RADAR)",
      ],
      [
        "Stack",
        "OpenSCAD 2021.01+ (CAD), Python 3.11+ (checks)",
      ],
      [
        "Tests",
        "22 (`python -m unittest discover -s tests`)",
      ],
      [
        "Designs",
        "The radar enclosure and the box of 3 node presets (solar, electrical, alarm)",
      ],
      [
        "Runs on",
        "Any computer with OpenSCAD",
      ],
      [
        "On real hardware",
        "None yet: nothing has been printed or measured; the three boxes are only checked by the asserts of their source",
      ],
      [
        "License",
        "GPL-3.0-or-later",
      ],
    ],
    "status": {
      "software": "The radar enclosure and the parametric box of the solar, electrical and alarm nodes are OpenSCAD sources; the radar box is a printable starting point, not an IP, RF or thermal rating.",
      "tests": "22 tests pass (`python -m unittest discover -s tests`): the sources, the presets of the box, the model files and the numbers the documents quote. The boxes are also checked by the asserts of their source; none has been printed or measured.",
      "hardware": "Nothing has been printed or measured, the board sizes come from data sheets, and every row of the bench acceptance matrix is not tested.",
      "docs": "Eight languages, the design inputs and the bench acceptance matrix are written and up to date.",
    },
    "docs": [
      "[Design inputs](docs/DESIGN_INPUTS.md): what to record before fabrication",
      "[Validation boundary](docs/VALIDATION.md): what is and is not validated",
      "[Bench acceptance matrix](docs/BENCH_ACCEPTANCE.md): the checks, their methods and proposed pass criteria",
    ],
    "contributing_first": "Before a pull request run `python -m unittest discover -s tests` and `python -I tools/armor_ci_validate.py`: it must pass. See [CONTRIBUTING.md](CONTRIBUTING.md) and the [code of conduct](CODE_OF_CONDUCT.md).",
    "languages_extra": "",
    "body": {
      "overview": r"""* **The radar enclosure is `scad/node_enclosure_radar.scad`** (with STL, 3MF and AMF exports and two slicer projects, the base and the sliding cover): a 90-degree corner base with a visor, roof and floor, retaining steps, a sliding 2 mm front cover and side flaps, all driven by named parameters.
* **A parametric box for the solar, electrical and alarm nodes** (`scad/node_box.scad`, presets `solar`, `electrical` and `alarm`): walls, posts for the board, cable-gland holes, a vent, a pocket for a tamper micro-switch under the lid and a lid with a ring-shaped lip. It is a low-voltage box, not an enclosure for mains wiring.
* **Holders** for three radar modules, a cable gland and drain holes. There are no volumes yet for the ESP32-S3-ETH-PoE board, the PoE magnetics, the PTC heater or the light-sensor window that the bench matrix wants to test. No metallic, conductive or carbon-loaded material in front of a 24 GHz aperture without measuring it first.
* **Bench acceptance matrix:** the radio, environment, power, network and camera checks with a method and a proposed pass criterion each, and a camera compatibility table to fill in.
* Before fabrication, record exact board outlines, connectors, screw positions, antenna keep-outs, the thermal path and the ingress target ([design inputs](docs/DESIGN_INPUTS.md)).""",
      "role": "ARMOR-HARDWARE is what holds the nodes. It carries the enclosure of the radar node, the parametric box of the solar, electrical, alarm and touch-panel nodes, and the bench acceptance matrix that says how a prototype is to be judged before it goes on a wall. Its designs are the starting point for the boards that [ARMOR-NODE-RADAR](https://github.com/JuanenRac/ARMOR-NODE-RADAR), [ARMOR-NODE-SOLAR](https://github.com/JuanenRac/ARMOR-NODE-SOLAR), [ARMOR-NODE-ELECTRICAL](https://github.com/JuanenRac/ARMOR-NODE-ELECTRICAL), [ARMOR-NODE-ALARM](https://github.com/JuanenRac/ARMOR-NODE-ALARM) and [ARMOR-NODE-HMI](https://github.com/JuanenRac/ARMOR-NODE-HMI) run on.",
      "architecture": r"""<p align="center">
  <img src="images/architecture.svg" alt="ARMOR-HARDWARE architecture: who calls it, what it holds and what it depends on" width="100%">
</p>""",
      "security": r"""| Threat | Defence |
|---|---|
| Mains wiring in a plastic box | `node_box.scad` is a low-voltage box, not an enclosure for mains wiring |
| A blocked 24 GHz radar | No metallic, conductive or carbon-loaded material in front of a 24 GHz aperture without measuring it first; the 2 mm cover thickness is a row of the bench matrix |
| A preset or a part that does not exist | `assert` stops the render: `preset must be solar, electrical or alarm`, `part must be box, lid or both` |
| A print that does not fit | The asserts of the source catch it when the file is rendered: the board and its posts fit, the cable holes are not cut by a wall or a post nor taller than the inside, the lid lip is 1.2 to 3 mm |

The radar enclosure is a printable mechanical starting point, **not an IP, RF or thermal rating**. Nothing has been printed or measured.""",
      "configuration": r"""| Name | Value | What it sets |
|---|---|---|
| `wall`, `lid_t` | 3 mm, 3 mm | Wall and lid thickness of `node_box.scad` |
| `post_d`, `post_h`, `post_cap` | 7, 6, 9 mm | The posts for the board and for the lid screws |
| `screw_d` | 3.2 mm | M3 self-tapping screws into the posts |
| `clear`, `lip_w` | 0.3 mm, 1.6 mm | Play between lid and box; width of the ring-shaped lip (1.2 to 3 mm) |
| `preset`, `part` | `alarm` | `solar`, `electrical` or `alarm`; `box`, `lid` or `both` |
| `vent` | `true` | A row of slots in the lid so the heat can leave |

| Piece | Inside size (mm) | Board (mm) |
|---|---|---|
| `solar` | 110 × 80 × 45 | 66 × 53 |
| `electrical` | 140 × 100 × 50 | 120 × 80 |
| `alarm` | 150 × 110 × 60 | 120 × 80 |""",
      "quickstart": r"""**Requirements:** OpenSCAD 2021.01+ (to render the enclosures), a 3D printer (FDM) to try them.

```powershell
openscad -o build/node_enclosure_radar.stl scad/node_enclosure_radar.scad
openscad -D 'part="both"' -D 'preset="alarm"' -o build/node_box_alarm.stl scad/node_box.scad   # presets: solar, electrical, alarm
```

See the [validation boundary](docs/VALIDATION.md). The intended hardware licence is CERN-OHL-S-2.0; add its full text before releasing the designs.""",
      "testing": r"""```powershell
python -m unittest discover -s tests   # 22 tests, no OpenSCAD needed
python -I tools/armor_ci_validate.py
```

| Test file | Tests | What it covers |
|---|---|---|
| `test_enclosure_sources.py` | 22 | The sources, the presets of the box, the model files and the numbers the documents quote |

OpenSCAD renders every piece on a machine that has it: the radar base and cover, and the box and lid of the three presets. The [bench acceptance matrix](docs/BENCH_ACCEPTANCE.md) is where a printed prototype is judged.""",
      "troubleshooting": r"""| You see | Because | Do |
|---|---|---|
| `preset must be solar, electrical or alarm` | The `preset` is something else | `-D 'preset="alarm"'` |
| `the board and its posts do not fit inside the box` | A parameter made the posts too big for the inside | Restore `post_d` or choose a bigger preset |
| The lid does not close | Your printer is tighter than the 0.3 mm of play | Raise `clear` and print again |""",
      "structure": r"""<p align="center">
  <img src="images/repository-structure.svg" alt="Repository structure of ARMOR-HARDWARE" width="100%">
</p>

<details>
<summary>Text version of the tree</summary>

```text
ARMOR-HARDWARE/
├── scad/                                the enclosures and their model files
├── docs/                                the guides of this repository
├── tests/                               the tests
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
└── .gitattributes .gitignore            Git settings
```

</details>""",
      "roadmap": r"""**Known limits today**

* Nothing has been printed or measured; the board sizes come from data sheets and every row of the bench acceptance matrix is *not tested*.
* There are no volumes yet for the ESP32-S3-ETH-PoE board, the PoE magnetics, the PTC heater or the light-sensor window; the touch panel has no printed box (it keeps its factory enclosure).
* The hardware licence intended for the designs is CERN-OHL-S-2.0, and its full text is not in the repository yet.

**Next**

* Record the exact board outlines, connectors, screw positions, antenna keep-outs, the thermal path and the ingress target ([design inputs](docs/DESIGN_INPUTS.md)).
* Print the prototypes and fill in the bench acceptance matrix with dated measurements.""",
    },
  },
  "es": {
    "tagline": "Carcasas, electrónica y la matriz de aceptación de banco",
    "honest": "La carcasa del radar es un **punto de partida mecánico imprimible, no una clasificación IP, RF ni térmica**, y la caja paramétrica para los nodos solar, eléctrico y de alarma está comprobada por los `assert` de su fuente (la placa cabe, los agujeros de cables caben, la tapa libra los postes), pero **ninguna se ha imprimido ni medido** (los tamaños de las placas salen de las hojas de datos; el panel táctil no tiene caja impresa, conserva su carcasa de fábrica). Cada fila de la [matriz de aceptación en banco](docs/BENCH_ACCEPTANCE.md) está *sin probar*.",
    "glance": [
      [
        "Función",
        "Cajas, electrónica y la matriz de aceptación en banco (familia: Hardware, padre: ARMOR-NODE-RADAR)",
      ],
      [
        "Tecnología",
        "OpenSCAD 2021.01+ (CAD), Python 3.11+ (comprobaciones)",
      ],
      [
        "Pruebas",
        "22 (`python -m unittest discover -s tests`)",
      ],
      [
        "Diseños",
        "La caja del radar y la caja de 3 presets de nodo (solar, eléctrico, alarma)",
      ],
      [
        "Funciona en",
        "Cualquier ordenador con OpenSCAD",
      ],
      [
        "En hardware real",
        "Ninguno todavía: nada se ha impreso ni medido; las tres cajas solo las comprueban los `assert` de su fuente",
      ],
      [
        "Licencia",
        "GPL-3.0-or-later",
      ],
    ],
    "status": {
      "software": "La carcasa del radar y la caja paramétrica de los nodos solar, eléctrico y de alarma son fuentes de OpenSCAD; la caja del radar es un punto de partida imprimible, no una clasificación IP, RF ni térmica.",
      "tests": "Pasan 22 pruebas (`python -m unittest discover -s tests`): las fuentes, los presets de la caja, los ficheros de modelo y las cifras que citan los documentos. Las cajas también las comprueban los `assert` de su fuente; ninguna se ha impreso ni medido.",
      "hardware": "Nada se ha impreso ni medido, las medidas de las placas salen de hojas de datos, y cada fila de la matriz de aceptación en banco está sin probar.",
      "docs": "Ocho idiomas, los datos de diseño y la matriz de aceptación en banco están escritos y al día.",
    },
    "docs": [
      "[Entradas de diseño](docs/DESIGN_INPUTS.md): qué anotar antes de fabricar",
      "[Límite de la validación](docs/VALIDATION.md): qué está y qué no está validado",
      "[Matriz de aceptación en banco](docs/BENCH_ACCEPTANCE.md): las comprobaciones, sus métodos y criterios propuestos",
    ],
    "contributing_first": "Antes de un pull request ejecuta `python -m unittest discover -s tests` and `python -I tools/armor_ci_validate.py`: debe pasar. Consulta [CONTRIBUTING.md](CONTRIBUTING.md) y el [código de conducta](CODE_OF_CONDUCT.md).",
    "languages_extra": "",
    "body": {
      "overview": r"""* **La carcasa del radar es `scad/node_enclosure_radar.scad`** (con exportaciones STL, 3MF y AMF y dos proyectos de laminador, la base y la tapa corredera): una base de esquina de 90 grados con visera, techo y suelo, escalones de retención, una tapa frontal corredera de 2 mm y aletas laterales, todo gobernado por parámetros con nombre.
* **Una caja paramétrica para los nodos solar, eléctrico y de alarma** (`scad/node_box.scad`, preajustes `solar`, `electrical` y `alarm`): paredes, postes para la placa, agujeros para prensaestopas, una ventilación, un hueco para un microinterruptor antisabotaje bajo la tapa y una tapa con labio anular. Es una caja de baja tensión, no una envolvente para cableado de red.
* **Soportes** para tres módulos de radar, un prensaestopas y agujeros de drenaje. Todavía no hay volúmenes para la placa ESP32-S3-ETH-PoE, la magnética PoE, el calefactor PTC ni la ventana del sensor de luz que la matriz de banco quiere probar. Ningún material metálico, conductor o cargado de carbono delante de una apertura de 24 GHz sin medirlo antes.
* **Matriz de aceptación en banco:** las comprobaciones de radio, entorno, alimentación, red y cámara con un método y un criterio de aprobado propuesto cada una, y una tabla de compatibilidad de cámaras por rellenar.
* Antes de fabricar, anota los contornos exactos de las placas, conectores, posiciones de tornillos, zonas libres de antena, el camino térmico y el objetivo de protección ([datos de diseño](docs/DESIGN_INPUTS.md)).""",
      "role": "ARMOR-HARDWARE es lo que contiene a los nodos. Lleva la carcasa del nodo radar, la caja paramétrica de los nodos solar, eléctrico, de alarma y de panel táctil, y la matriz de aceptación en banco que dice cómo juzgar un prototipo antes de ponerlo en una pared. Sus diseños son el punto de partida para las placas en las que corren [ARMOR-NODE-RADAR](https://github.com/JuanenRac/ARMOR-NODE-RADAR), [ARMOR-NODE-SOLAR](https://github.com/JuanenRac/ARMOR-NODE-SOLAR), [ARMOR-NODE-ELECTRICAL](https://github.com/JuanenRac/ARMOR-NODE-ELECTRICAL), [ARMOR-NODE-ALARM](https://github.com/JuanenRac/ARMOR-NODE-ALARM) y [ARMOR-NODE-HMI](https://github.com/JuanenRac/ARMOR-NODE-HMI).",
      "architecture": r"""<p align="center">
  <img src="images/architecture.svg" alt="Arquitectura de ARMOR-HARDWARE: quién lo llama, qué contiene y de qué depende" width="100%">
</p>""",
      "security": r"""| Amenaza | Defensa |
|---|---|
| Cableado de red en una caja de plástico | `node_box.scad` es una caja de bajo voltaje, no una caja para cableado de red |
| Un radar de 24 GHz bloqueado | Ningún material metálico, conductor o con carbono delante de una apertura de 24 GHz sin medirlo antes; el grosor de 2 mm de la tapa es una fila de la matriz de banco |
| Un preset o una pieza que no existe | Un `assert` detiene el renderizado: `preset must be solar, electrical or alarm`, `part must be box, lid or both` |
| Una impresión que no encaja | Los `assert` de la fuente lo detectan al renderizar: la placa y sus postes caben, los agujeros de cable no los corta una pared o poste ni son más altos que el interior, el labio de la tapa mide de 1,2 a 3 mm |

La caja del radar es un punto de partida mecánico imprimible, **no una clasificación IP, RF ni térmica**. Nada se ha impreso ni medido.""",
      "configuration": r"""| Nombre | Valor | Qué define |
|---|---|---|
| `wall`, `lid_t` | 3 mm, 3 mm | Grosor de pared y tapa de `node_box.scad` |
| `post_d`, `post_h`, `post_cap` | 7, 6, 9 mm | Los postes de la placa y de los tornillos de la tapa |
| `screw_d` | 3.2 mm | Tornillos M3 autorroscantes en los postes |
| `clear`, `lip_w` | 0.3 mm, 1.6 mm | Holgura entre tapa y caja; ancho del labio anular (1,2 a 3 mm) |
| `preset`, `part` | `alarm` | `solar`, `electrical` o `alarm`; `box`, `lid` o `both` |
| `vent` | `true` | Una fila de ranuras en la tapa para que salga el calor |

| Pieza | Interior (mm) | Placa (mm) |
|---|---|---|
| `solar` | 110 × 80 × 45 | 66 × 53 |
| `electrical` | 140 × 100 × 50 | 120 × 80 |
| `alarm` | 150 × 110 × 60 | 120 × 80 |""",
      "quickstart": r"""**Requisitos:** OpenSCAD 2021.01+ (para renderizar las cajas), una impresora 3D (FDM) para probarlas.

```powershell
openscad -o build/node_enclosure_radar.stl scad/node_enclosure_radar.scad
openscad -D 'part="both"' -D 'preset="alarm"' -o build/node_box_alarm.stl scad/node_box.scad   # presets: solar, electrical, alarm
```

Véase el [límite de validación](docs/VALIDATION.md). La licencia de hardware prevista es CERN-OHL-S-2.0; añade su texto completo antes de publicar los diseños.""",
      "testing": r"""```powershell
python -m unittest discover -s tests   # 22 tests, no OpenSCAD needed
python -I tools/armor_ci_validate.py
```

| Fichero de pruebas | Pruebas | Qué cubre |
|---|---|---|
| `test_enclosure_sources.py` | 22 | Las fuentes, los presets de la caja, los ficheros de modelo y las cifras que citan los documentos |

OpenSCAD renderiza cada pieza en una máquina que lo tenga: la base y la tapa del radar, y la caja y la tapa de los tres presets. La [matriz de aceptación en banco](docs/BENCH_ACCEPTANCE.md) es donde se juzga un prototipo impreso.""",
      "troubleshooting": r"""| Ves | Porque | Haz |
|---|---|---|
| `preset must be solar, electrical or alarm` | El `preset` es otro valor | `-D 'preset="alarm"'` |
| `the board and its posts do not fit inside the box` | Un parámetro hizo los postes demasiado grandes para el interior | Restaura `post_d` o elige un preset mayor |
| La tapa no cierra | Tu impresora es más ajustada que los 0,3 mm de holgura | Sube `clear` y vuelve a imprimir |""",
      "structure": r"""<p align="center">
  <img src="images/repository-structure.svg" alt="Estructura del repositorio de ARMOR-HARDWARE" width="100%">
</p>

<details>
<summary>Versión en texto del árbol</summary>

```text
ARMOR-HARDWARE/
├── scad/                                las cajas y sus ficheros de modelo
├── docs/                                las guías de este repositorio
├── tests/                               las pruebas
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
└── .gitattributes .gitignore            ajustes de Git
```

</details>""",
      "roadmap": r"""**Límites conocidos hoy**

* Nada se ha impreso ni medido; los tamaños de placa salen de hojas de datos y cada fila de la matriz de aceptación en banco está *sin probar*.
* Aún no hay volúmenes para la placa ESP32-S3-ETH-PoE, las magnéticas PoE, el calefactor PTC ni la ventana del sensor de luz; el panel táctil no tiene caja impresa (conserva su carcasa de fábrica).
* La licencia de hardware prevista para los diseños es CERN-OHL-S-2.0 y su texto completo aún no está en el repositorio.

**Lo siguiente**

* Anotar los contornos exactos de placa, conectores, posiciones de tornillos, zonas libres de antena, el camino térmico y el objetivo de protección ([entradas de diseño](docs/DESIGN_INPUTS.md)).
* Imprimir los prototipos y rellenar la matriz de aceptación en banco con mediciones fechadas.""",
    },
  },
  "de": {
    "tagline": "Gehäuse, Elektronik und die Abnahmematrix am Prüfstand",
    "honest": "Das Radargehäuse ist ein **druckbarer mechanischer Ausgangspunkt, keine IP-, HF- oder Thermikeinstufung**, und die parametrische Box für die Knoten Solar, Elektro und Alarm wird von den `assert`-Prüfungen ihres Quelltexts geprüft (die Platine passt, die Kabellöcher passen, der Deckel liegt frei von den Pfosten), aber **keine wurde gedruckt oder vermessen** (die Platinengrößen stammen aus Datenblättern; das Touchpanel hat keine gedruckte Box, es behält sein Werksgehäuse). Jede Zeile der [Prüfstand-Abnahmematrix](docs/BENCH_ACCEPTANCE.md) ist *ungetestet*.",
    "glance": [
      [
        "Rolle",
        "Gehäuse, Elektronik und die Prüfstand-Abnahmematrix (Familie: Hardware, übergeordnet: ARMOR-NODE-RADAR)",
      ],
      [
        "Technik",
        "OpenSCAD 2021.01+ (CAD), Python 3.11+ (Prüfungen)",
      ],
      [
        "Tests",
        "22 (`python -m unittest discover -s tests`)",
      ],
      [
        "Entwürfe",
        "Das Radargehäuse und die Box für 3 Knoten-Presets (Solar, Elektro, Alarm)",
      ],
      [
        "Läuft auf",
        "Jeder Computer mit OpenSCAD",
      ],
      [
        "Auf echter Hardware",
        "Noch keiner: nichts wurde gedruckt oder vermessen; die drei Boxen werden nur durch die `assert`-Prüfungen ihres Quelltexts geprüft",
      ],
      [
        "Lizenz",
        "GPL-3.0-or-later",
      ],
    ],
    "status": {
      "software": "Das Radargehäuse und die parametrische Box der Solar-, Elektrik- und Alarmknoten sind OpenSCAD-Quellen; die Radarbox ist ein druckbarer Ausgangspunkt, keine IP-, HF- oder Temperatur-Einstufung.",
      "tests": "22 Tests bestehen (`python -m unittest discover -s tests`): die Quellen, die Presets der Box, die Modelldateien und die Zahlen, die die Dokumente nennen. Die Boxen prüfen auch die Asserts ihrer Quelle; keine wurde gedruckt oder gemessen.",
      "hardware": "Nichts wurde gedruckt oder vermessen, die Maße der Platinen stammen aus Datenblättern, und jede Zeile der Prüfstand-Abnahmematrix ist ungetestet.",
      "docs": "Acht Sprachen, die Entwurfsvorgaben und die Prüfstand-Abnahmematrix sind geschrieben und aktuell.",
    },
    "docs": [
      "[Entwurfseingaben](docs/DESIGN_INPUTS.md): was vor der Fertigung festzuhalten ist",
      "[Validierungsgrenze](docs/VALIDATION.md): was validiert ist und was nicht",
      "[Prüfstand-Abnahmematrix](docs/BENCH_ACCEPTANCE.md): die Prüfungen, ihre Methoden und vorgeschlagenen Kriterien",
    ],
    "contributing_first": "Führe vor einem Pull Request `python -m unittest discover -s tests` and `python -I tools/armor_ci_validate.py` aus: Es muss bestehen. Siehe [CONTRIBUTING.md](CONTRIBUTING.md) und den [Verhaltenskodex](CODE_OF_CONDUCT.md).",
    "languages_extra": "",
    "body": {
      "overview": r"""* **Das Radargehäuse ist `scad/node_enclosure_radar.scad`** (mit STL-, 3MF- und AMF-Exporten und zwei Slicer-Projekten, der Basis und dem Schiebedeckel): eine 90-Grad-Eckbasis mit Blende, Dach und Boden, Haltestufen, einem 2 mm dicken Schiebedeckel vorn und Seitenklappen, alles über benannte Parameter gesteuert.
* **Eine parametrische Box für die Knoten Solar, Elektro und Alarm** (`scad/node_box.scad`, Voreinstellungen `solar`, `electrical` und `alarm`): Wände, Pfosten für die Platine, Löcher für Kabelverschraubungen, eine Lüftung, eine Aufnahme für einen Sabotage-Mikroschalter unter dem Deckel und ein Deckel mit ringförmiger Lippe. Es ist eine Kleinspannungsbox, kein Gehäuse für Netzverdrahtung.
* **Halter** für drei Radarmodule, eine Kabelverschraubung und Ablaufbohrungen. Für die Platine ESP32-S3-ETH-PoE, die PoE-Magnetik, die PTC-Heizung und das Lichtsensorfenster, die die Prüfstandmatrix testen will, gibt es noch keine Volumina. Kein metallisches, leitendes oder kohlenstoffhaltiges Material vor einer 24-GHz-Öffnung, ohne es vorher zu messen.
* **Prüfstand-Abnahmematrix:** die Prüfungen für Funk, Umgebung, Stromversorgung, Netzwerk und Kamera, jeweils mit Methode und vorgeschlagenem Bestehenskriterium, und eine auszufüllende Kamera-Kompatibilitätstabelle.
* Vor der Fertigung genaue Platinenumrisse, Steckverbinder, Schraubpositionen, Antennenfreiräume, den Wärmepfad und das Schutzziel festhalten ([Entwurfsangaben](docs/DESIGN_INPUTS.md)).""",
      "role": "ARMOR-HARDWARE ist das, was die Knoten hält. Es enthält das Gehäuse des Radarknotens, die parametrische Box der Knoten Solar, Elektro, Alarm und Touchpanel und die Abnahmematrix, die sagt, wie ein Prototyp beurteilt wird, bevor er an die Wand kommt. Seine Entwürfe sind der Ausgangspunkt für die Platinen, auf denen [ARMOR-NODE-RADAR](https://github.com/JuanenRac/ARMOR-NODE-RADAR), [ARMOR-NODE-SOLAR](https://github.com/JuanenRac/ARMOR-NODE-SOLAR), [ARMOR-NODE-ELECTRICAL](https://github.com/JuanenRac/ARMOR-NODE-ELECTRICAL), [ARMOR-NODE-ALARM](https://github.com/JuanenRac/ARMOR-NODE-ALARM) und [ARMOR-NODE-HMI](https://github.com/JuanenRac/ARMOR-NODE-HMI) laufen.",
      "architecture": r"""<p align="center">
  <img src="images/architecture.svg" alt="Architektur von ARMOR-HARDWARE: wer es aufruft, was es enthält und wovon es abhängt" width="100%">
</p>""",
      "security": r"""| Bedrohung | Abwehr |
|---|---|
| Netzverdrahtung in einer Kunststoffbox | `node_box.scad` ist eine Kleinspannungsbox, kein Gehäuse für Netzverdrahtung |
| Ein blockiertes 24-GHz-Radar | Kein metallisches, leitfähiges oder kohlenstoffhaltiges Material vor einer 24-GHz-Öffnung, ohne es zuvor zu messen; die Deckeldicke von 2 mm ist eine Zeile der Prüfstandsmatrix |
| Ein Preset oder Teil, das es nicht gibt | Ein `assert` stoppt das Rendern: `preset must be solar, electrical or alarm`, `part must be box, lid or both` |
| Ein Druck, der nicht passt | Die Asserts der Quelle fangen es beim Rendern ab: Platine und Pfosten passen, Kabellöcher werden weder von Wand oder Pfosten geschnitten noch sind sie höher als das Innere, die Deckellippe misst 1,2 bis 3 mm |

Das Radargehäuse ist ein druckbarer mechanischer Ausgangspunkt, **keine IP-, HF- oder Wärmeklassifizierung**. Nichts wurde gedruckt oder gemessen.""",
      "configuration": r"""| Name | Wert | Was sie festlegt |
|---|---|---|
| `wall`, `lid_t` | 3 mm, 3 mm | Wand- und Deckelstärke von `node_box.scad` |
| `post_d`, `post_h`, `post_cap` | 7, 6, 9 mm | Die Pfosten für die Platine und die Deckelschrauben |
| `screw_d` | 3.2 mm | M3-Schneidschrauben in die Pfosten |
| `clear`, `lip_w` | 0.3 mm, 1.6 mm | Spiel zwischen Deckel und Box; Breite der ringförmigen Lippe (1,2 bis 3 mm) |
| `preset`, `part` | `alarm` | `solar`, `electrical` oder `alarm`; `box`, `lid` oder `both` |
| `vent` | `true` | Eine Reihe Schlitze im Deckel, damit die Wärme entweichen kann |

| Teil | Innenmaß (mm) | Platine (mm) |
|---|---|---|
| `solar` | 110 × 80 × 45 | 66 × 53 |
| `electrical` | 140 × 100 × 50 | 120 × 80 |
| `alarm` | 150 × 110 × 60 | 120 × 80 |""",
      "quickstart": r"""**Voraussetzungen:** OpenSCAD 2021.01+ (zum Rendern der Gehäuse), ein 3D-Drucker (FDM) zum Ausprobieren.

```powershell
openscad -o build/node_enclosure_radar.stl scad/node_enclosure_radar.scad
openscad -D 'part="both"' -D 'preset="alarm"' -o build/node_box_alarm.stl scad/node_box.scad   # presets: solar, electrical, alarm
```

Siehe die [Validierungsgrenze](docs/VALIDATION.md). Die vorgesehene Hardware-Lizenz ist CERN-OHL-S-2.0; fügen Sie ihren vollständigen Text hinzu, bevor Sie die Entwürfe veröffentlichen.""",
      "testing": r"""```powershell
python -m unittest discover -s tests   # 22 tests, no OpenSCAD needed
python -I tools/armor_ci_validate.py
```

| Testdatei | Tests | Was sie abdeckt |
|---|---|---|
| `test_enclosure_sources.py` | 22 | Die Quellen, die Presets der Box, die Modelldateien und die Zahlen, die die Dokumente nennen |

OpenSCAD rendert jedes Teil auf einem Rechner, der es hat: Radarbasis und -deckel sowie Box und Deckel der drei Presets. In der [Prüfstand-Abnahmematrix](docs/BENCH_ACCEPTANCE.md) wird ein gedruckter Prototyp beurteilt.""",
      "troubleshooting": r"""| Sie sehen | Weil | Tun Sie |
|---|---|---|
| `preset must be solar, electrical or alarm` | Das `preset` ist etwas anderes | `-D 'preset="alarm"'` |
| `the board and its posts do not fit inside the box` | Ein Parameter machte die Pfosten für das Innere zu groß | Setze `post_d` zurück oder wähle ein größeres Preset |
| Der Deckel schließt nicht | Dein Drucker ist enger als das Spiel von 0,3 mm | Erhöhe `clear` und drucke neu |""",
      "structure": r"""<p align="center">
  <img src="images/repository-structure.svg" alt="Repository-Struktur von ARMOR-HARDWARE" width="100%">
</p>

<details>
<summary>Textversion des Baums</summary>

```text
ARMOR-HARDWARE/
├── scad/                                die Gehäuse und ihre Modelldateien
├── docs/                                die Anleitungen dieses Repositorys
├── tests/                               die Tests
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
└── .gitattributes .gitignore            Git-Einstellungen
```

</details>""",
      "roadmap": r"""**Bekannte Grenzen heute**

* Nichts wurde gedruckt oder gemessen; die Platinengrößen stammen aus Datenblättern, und jede Zeile der Prüfstand-Abnahmematrix ist *nicht getestet*.
* Es gibt noch keine Volumen für die ESP32-S3-ETH-PoE-Platine, die PoE-Magnetik, die PTC-Heizung oder das Lichtsensorfenster; das Touchpanel hat keine gedruckte Box (es behält sein Werksgehäuse).
* Die für die Entwürfe vorgesehene Hardwarelizenz ist CERN-OHL-S-2.0; ihr vollständiger Text liegt noch nicht im Repository.

**Als Nächstes**

* Die genauen Platinenumrisse, Steckverbinder, Schraubenpositionen, Antennenfreiräume, den Wärmepfad und das Schutzziel festhalten ([Entwurfseingaben](docs/DESIGN_INPUTS.md)).
* Die Prototypen drucken und die Prüfstand-Abnahmematrix mit datierten Messungen füllen.""",
    },
  },
  "fr": {
    "tagline": "Boîtiers, électronique et matrice d'acceptation sur banc",
    "honest": "Le boîtier du radar est un **point de départ mécanique imprimable, pas un classement IP, RF ou thermique**, et la boîte paramétrique pour les nœuds solaire, électrique et alarme est vérifiée par les `assert` de sa source (la carte tient, les trous de câbles tiennent, le couvercle dégage les plots), mais **aucune n'a été imprimée ni mesurée** (les dimensions des cartes viennent des fiches techniques ; le panneau tactile n'a pas de boîte imprimée, il garde son boîtier d'origine). Chaque ligne de la [matrice d'acceptation sur banc](docs/BENCH_ACCEPTANCE.md) est *non testée*.",
    "glance": [
      [
        "Rôle",
        "Boîtiers, électronique et la matrice d'acceptation sur banc (famille : Hardware, parent : ARMOR-NODE-RADAR)",
      ],
      [
        "Technologie",
        "OpenSCAD 2021.01+ (CAO), Python 3.11+ (contrôles)",
      ],
      [
        "Tests",
        "22 (`python -m unittest discover -s tests`)",
      ],
      [
        "Conceptions",
        "Le boîtier du radar et la boîte de 3 préréglages de nœud (solaire, électrique, alarme)",
      ],
      [
        "Fonctionne sur",
        "N'importe quel ordinateur avec OpenSCAD",
      ],
      [
        "Sur matériel réel",
        "Aucun pour l'instant : rien n'a été imprimé ni mesuré ; les trois boîtes ne sont vérifiées que par les `assert` de leur source",
      ],
      [
        "Licence",
        "GPL-3.0-or-later",
      ],
    ],
    "status": {
      "software": "Le boîtier du radar et la boîte paramétrique des nœuds solaire, électrique et d'alarme sont des sources OpenSCAD ; la boîte du radar est un point de départ imprimable, pas une classe IP, RF ou thermique.",
      "tests": "22 tests réussissent (`python -m unittest discover -s tests`) : les sources, les préréglages de la boîte, les fichiers de modèle et les chiffres cités par les documents. Les boîtes sont aussi vérifiées par les `assert` de leur source ; aucune n'a été imprimée ni mesurée.",
      "hardware": "Rien n'a été imprimé ni mesuré, les dimensions des cartes viennent de fiches techniques, et chaque ligne de la matrice d'acceptation sur banc n'est pas testée.",
      "docs": "Huit langues, les données de conception et la matrice d'acceptation sur banc sont écrites et à jour.",
    },
    "docs": [
      "[Données de conception](docs/DESIGN_INPUTS.md) : à noter avant la fabrication",
      "[Limite de la validation](docs/VALIDATION.md) : ce qui est et n'est pas validé",
      "[Matrice d'acceptation sur banc](docs/BENCH_ACCEPTANCE.md) : les contrôles, leurs méthodes et critères proposés",
    ],
    "contributing_first": "Avant une pull request, lancez `python -m unittest discover -s tests` and `python -I tools/armor_ci_validate.py` : il doit réussir. Voir [CONTRIBUTING.md](CONTRIBUTING.md) et le [code de conduite](CODE_OF_CONDUCT.md).",
    "languages_extra": "",
    "body": {
      "overview": r"""* **Le boîtier du radar est `scad/node_enclosure_radar.scad`** (avec exports STL, 3MF et AMF et deux projets de trancheur, la base et le couvercle coulissant) : une base d'angle à 90 degrés avec visière, toit et plancher, des gradins de retenue, un couvercle avant coulissant de 2 mm et des volets latéraux, le tout piloté par des paramètres nommés.
* **Une boîte paramétrique pour les nœuds solaire, électrique et alarme** (`scad/node_box.scad`, préréglages `solar`, `electrical` et `alarm`) : parois, plots pour la carte, trous de presse-étoupe, une aération, un logement pour un micro-interrupteur anti-sabotage sous le couvercle et un couvercle à lèvre annulaire. C'est une boîte basse tension, pas un coffret pour câblage secteur.
* **Supports** pour trois modules radar, un presse-étoupe et des trous de drainage. Il n'y a pas encore de volumes pour la carte ESP32-S3-ETH-PoE, la magnétique PoE, le chauffage PTC ni la fenêtre du capteur de lumière que la matrice de banc veut tester. Aucun matériau métallique, conducteur ou chargé de carbone devant une ouverture 24 GHz sans l'avoir mesuré.
* **Matrice d'acceptation sur banc :** les contrôles radio, environnement, alimentation, réseau et caméra avec une méthode et un critère de réussite proposé chacun, et un tableau de compatibilité des caméras à remplir.
* Avant fabrication, notez les contours exacts des cartes, les connecteurs, les positions de vis, les zones libres d'antenne, le chemin thermique et l'objectif de protection ([données de conception](docs/DESIGN_INPUTS.md)).""",
      "role": "ARMOR-HARDWARE est ce qui contient les nœuds. Il porte le boîtier du nœud radar, la boîte paramétrique des nœuds solaire, électrique, alarme et panneau tactile, et la matrice d'acceptation sur banc qui dit comment juger un prototype avant de le mettre au mur. Ses conceptions sont le point de départ des cartes sur lesquelles tournent [ARMOR-NODE-RADAR](https://github.com/JuanenRac/ARMOR-NODE-RADAR), [ARMOR-NODE-SOLAR](https://github.com/JuanenRac/ARMOR-NODE-SOLAR), [ARMOR-NODE-ELECTRICAL](https://github.com/JuanenRac/ARMOR-NODE-ELECTRICAL), [ARMOR-NODE-ALARM](https://github.com/JuanenRac/ARMOR-NODE-ALARM) et [ARMOR-NODE-HMI](https://github.com/JuanenRac/ARMOR-NODE-HMI).",
      "architecture": r"""<p align="center">
  <img src="images/architecture.svg" alt="Architecture de ARMOR-HARDWARE : qui l'appelle, ce qu'il contient et de quoi il dépend" width="100%">
</p>""",
      "security": r"""| Menace | Défense |
|---|---|
| Câblage secteur dans une boîte en plastique | `node_box.scad` est une boîte basse tension, pas un boîtier pour câblage secteur |
| Un radar 24 GHz bloqué | Aucun matériau métallique, conducteur ou chargé de carbone devant une ouverture 24 GHz sans l'avoir mesuré ; l'épaisseur de 2 mm du couvercle est une ligne de la matrice de banc |
| Un préréglage ou une pièce qui n'existe pas | Un `assert` arrête le rendu : `preset must be solar, electrical or alarm`, `part must be box, lid or both` |
| Une impression qui ne s'ajuste pas | Les `assert` de la source l'attrapent au rendu : la carte et ses plots tiennent, les trous de câble ne sont coupés ni par un mur ni par un plot et ne dépassent pas l'intérieur, la lèvre du couvercle fait de 1,2 à 3 mm |

Le boîtier du radar est un point de départ mécanique imprimable, **pas une classe IP, RF ou thermique**. Rien n'a été imprimé ni mesuré.""",
      "configuration": r"""| Nom | Valeur | Ce qu'elle règle |
|---|---|---|
| `wall`, `lid_t` | 3 mm, 3 mm | Épaisseur de paroi et de couvercle de `node_box.scad` |
| `post_d`, `post_h`, `post_cap` | 7, 6, 9 mm | Les plots de la carte et des vis du couvercle |
| `screw_d` | 3.2 mm | Vis M3 autotaraudeuses dans les plots |
| `clear`, `lip_w` | 0.3 mm, 1.6 mm | Jeu entre couvercle et boîte ; largeur de la lèvre annulaire (1,2 à 3 mm) |
| `preset`, `part` | `alarm` | `solar`, `electrical` ou `alarm` ; `box`, `lid` ou `both` |
| `vent` | `true` | Une rangée de fentes dans le couvercle pour évacuer la chaleur |

| Pièce | Intérieur (mm) | Carte (mm) |
|---|---|---|
| `solar` | 110 × 80 × 45 | 66 × 53 |
| `electrical` | 140 × 100 × 50 | 120 × 80 |
| `alarm` | 150 × 110 × 60 | 120 × 80 |""",
      "quickstart": r"""**Prérequis:** OpenSCAD 2021.01+ (pour rendre les boîtiers), une imprimante 3D (FDM) pour les essayer.

```powershell
openscad -o build/node_enclosure_radar.stl scad/node_enclosure_radar.scad
openscad -D 'part="both"' -D 'preset="alarm"' -o build/node_box_alarm.stl scad/node_box.scad   # presets: solar, electrical, alarm
```

Voir la [frontière de validation](docs/VALIDATION.md). La licence matérielle prévue est CERN-OHL-S-2.0 ; ajoutez son texte complet avant de publier les conceptions.""",
      "testing": r"""```powershell
python -m unittest discover -s tests   # 22 tests, no OpenSCAD needed
python -I tools/armor_ci_validate.py
```

| Fichier de tests | Tests | Ce qu'il couvre |
|---|---|---|
| `test_enclosure_sources.py` | 22 | Les sources, les préréglages de la boîte, les fichiers de modèle et les chiffres cités par les documents |

OpenSCAD rend chaque pièce sur une machine qui l'a : la base et le couvercle du radar, la boîte et le couvercle des trois préréglages. La [matrice d'acceptation sur banc](docs/BENCH_ACCEPTANCE.md) sert à juger un prototype imprimé.""",
      "troubleshooting": r"""| Vous voyez | Parce que | Faites |
|---|---|---|
| `preset must be solar, electrical or alarm` | Le `preset` est autre chose | `-D 'preset="alarm"'` |
| `the board and its posts do not fit inside the box` | Un paramètre a rendu les plots trop grands pour l'intérieur | Rétablissez `post_d` ou choisissez un préréglage plus grand |
| Le couvercle ne ferme pas | Votre imprimante est plus serrée que le jeu de 0,3 mm | Augmentez `clear` et réimprimez |""",
      "structure": r"""<p align="center">
  <img src="images/repository-structure.svg" alt="Structure du dépôt de ARMOR-HARDWARE" width="100%">
</p>

<details>
<summary>Version texte de l'arborescence</summary>

```text
ARMOR-HARDWARE/
├── scad/                                les boîtiers et leurs fichiers de modèle
├── docs/                                les guides de ce dépôt
├── tests/                               les tests
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
└── .gitattributes .gitignore            réglages Git
```

</details>""",
      "roadmap": r"""**Limites connues aujourd'hui**

* Rien n'a été imprimé ni mesuré ; les tailles de carte viennent des fiches techniques et chaque ligne de la matrice d'acceptation sur banc est *non testée*.
* Il n'y a pas encore de volumes pour la carte ESP32-S3-ETH-PoE, les magnétiques PoE, le chauffage PTC ni la fenêtre du capteur de lumière ; le panneau tactile n'a pas de boîte imprimée (il garde son boîtier d'origine).
* La licence matérielle prévue pour les conceptions est CERN-OHL-S-2.0 et son texte complet n'est pas encore dans le dépôt.

**Ensuite**

* Noter les contours exacts des cartes, les connecteurs, les positions de vis, les zones libres d'antenne, le chemin thermique et l'objectif de protection ([données de conception](docs/DESIGN_INPUTS.md)).
* Imprimer les prototypes et remplir la matrice d'acceptation sur banc avec des mesures datées.""",
    },
  },
  "it": {
    "tagline": "Contenitori, elettronica e matrice di accettazione da banco",
    "honest": "L'involucro del radar è un **punto di partenza meccanico stampabile, non una classificazione IP, RF o termica**, e la scatola parametrica per i nodi solare, elettrico e allarme è verificata dagli `assert` del suo sorgente (la scheda ci sta, i fori dei cavi ci stanno, il coperchio libera le colonnine), ma **nessuna è stata stampata né misurata** (le dimensioni delle schede vengono dai datasheet; il pannello touch non ha una scatola stampata, mantiene il suo involucro di fabbrica). Ogni riga della [matrice di accettazione al banco](docs/BENCH_ACCEPTANCE.md) è *non provata*.",
    "glance": [
      [
        "Ruolo",
        "Involucri, elettronica e la matrice di accettazione al banco (famiglia: Hardware, padre: ARMOR-NODE-RADAR)",
      ],
      [
        "Tecnologia",
        "OpenSCAD 2021.01+ (CAD), Python 3.11+ (verifiche)",
      ],
      [
        "Test",
        "22 (`python -m unittest discover -s tests`)",
      ],
      [
        "Progetti",
        "L'involucro del radar e la scatola di 3 preset di nodo (solare, elettrico, allarme)",
      ],
      [
        "Gira su",
        "Qualsiasi computer con OpenSCAD",
      ],
      [
        "Su hardware reale",
        "Ancora nessuno: nulla è stato stampato né misurato; le tre scatole sono verificate solo dagli `assert` del sorgente",
      ],
      [
        "Licenza",
        "GPL-3.0-or-later",
      ],
    ],
    "status": {
      "software": "L'involucro del radar e la scatola parametrica dei nodi solare, elettrico e d'allarme sono sorgenti OpenSCAD; la scatola del radar è un punto di partenza stampabile, non una classificazione IP, RF o termica.",
      "tests": "22 test passano (`python -m unittest discover -s tests`): i sorgenti, i preset della scatola, i file di modello e i numeri citati dai documenti. Le scatole sono verificate anche dagli `assert` del loro sorgente; nessuna è stata stampata né misurata.",
      "hardware": "Nulla è stato stampato né misurato, le dimensioni delle schede vengono dai datasheet e ogni riga della matrice di accettazione al banco non è testata.",
      "docs": "Otto lingue, i dati di progetto e la matrice di accettazione al banco sono scritti e aggiornati.",
    },
    "docs": [
      "[Dati di progetto](docs/DESIGN_INPUTS.md): cosa registrare prima della fabbricazione",
      "[Limite della validazione](docs/VALIDATION.md): cosa è e cosa non è validato",
      "[Matrice di accettazione al banco](docs/BENCH_ACCEPTANCE.md): le verifiche, i metodi e i criteri proposti",
    ],
    "contributing_first": "Prima di una pull request esegui `python -m unittest discover -s tests` and `python -I tools/armor_ci_validate.py`: deve passare. Vedi [CONTRIBUTING.md](CONTRIBUTING.md) e il [codice di condotta](CODE_OF_CONDUCT.md).",
    "languages_extra": "",
    "body": {
      "overview": r"""* **L'involucro del radar è `scad/node_enclosure_radar.scad`** (con esportazioni STL, 3MF e AMF e due progetti dello slicer, la base e il coperchio scorrevole): una base d'angolo a 90 gradi con visiera, tetto e pavimento, gradini di ritenuta, un coperchio frontale scorrevole da 2 mm e alette laterali, tutto governato da parametri con nome.
* **Una scatola parametrica per i nodi solare, elettrico e allarme** (`scad/node_box.scad`, preset `solar`, `electrical` e `alarm`): pareti, colonnine per la scheda, fori per pressacavi, una ventilazione, un alloggiamento per un microinterruttore antimanomissione sotto il coperchio e un coperchio con labbro ad anello. È una scatola a bassa tensione, non un involucro per cablaggio di rete.
* **Supporti** per tre moduli radar, un pressacavo e fori di drenaggio. Non ci sono ancora volumi per la scheda ESP32-S3-ETH-PoE, la magnetica PoE, il riscaldatore PTC né la finestra del sensore di luce che la matrice di banco vuole provare. Nessun materiale metallico, conduttivo o caricato con carbonio davanti a un'apertura a 24 GHz senza averlo misurato.
* **Matrice di accettazione al banco:** i controlli di radio, ambiente, alimentazione, rete e telecamera con un metodo e un criterio di superamento proposto ciascuno, e una tabella di compatibilità delle telecamere da compilare.
* Prima della fabbricazione, registra i contorni esatti delle schede, i connettori, le posizioni delle viti, le zone libere d'antenna, il percorso termico e l'obiettivo di protezione ([dati di progetto](docs/DESIGN_INPUTS.md)).""",
      "role": "ARMOR-HARDWARE è ciò che contiene i nodi. Porta l'involucro del nodo radar, la scatola parametrica dei nodi solare, elettrico, allarme e pannello touch, e la matrice di accettazione al banco che dice come giudicare un prototipo prima di metterlo a una parete. I suoi progetti sono il punto di partenza per le schede su cui girano [ARMOR-NODE-RADAR](https://github.com/JuanenRac/ARMOR-NODE-RADAR), [ARMOR-NODE-SOLAR](https://github.com/JuanenRac/ARMOR-NODE-SOLAR), [ARMOR-NODE-ELECTRICAL](https://github.com/JuanenRac/ARMOR-NODE-ELECTRICAL), [ARMOR-NODE-ALARM](https://github.com/JuanenRac/ARMOR-NODE-ALARM) e [ARMOR-NODE-HMI](https://github.com/JuanenRac/ARMOR-NODE-HMI).",
      "architecture": r"""<p align="center">
  <img src="images/architecture.svg" alt="Architettura di ARMOR-HARDWARE: chi lo chiama, cosa contiene e da cosa dipende" width="100%">
</p>""",
      "security": r"""| Minaccia | Difesa |
|---|---|
| Cablaggio di rete in una scatola di plastica | `node_box.scad` è una scatola a bassa tensione, non un involucro per cablaggio di rete |
| Un radar a 24 GHz bloccato | Nessun materiale metallico, conduttivo o caricato di carbonio davanti a un'apertura a 24 GHz senza misurarlo; lo spessore di 2 mm del coperchio è una riga della matrice di banco |
| Un preset o un pezzo che non esiste | Un `assert` ferma il rendering: `preset must be solar, electrical or alarm`, `part must be box, lid or both` |
| Una stampa che non combacia | Gli `assert` del sorgente lo intercettano al rendering: la scheda e i suoi supporti ci stanno, i fori dei cavi non sono tagliati da una parete o un supporto né più alti dell'interno, il labbro del coperchio è tra 1,2 e 3 mm |

L'involucro del radar è un punto di partenza meccanico stampabile, **non una classificazione IP, RF o termica**. Nulla è stato stampato né misurato.""",
      "configuration": r"""| Nome | Valore | Cosa imposta |
|---|---|---|
| `wall`, `lid_t` | 3 mm, 3 mm | Spessore di parete e coperchio di `node_box.scad` |
| `post_d`, `post_h`, `post_cap` | 7, 6, 9 mm | I supporti della scheda e delle viti del coperchio |
| `screw_d` | 3.2 mm | Viti M3 autofilettanti nei supporti |
| `clear`, `lip_w` | 0.3 mm, 1.6 mm | Gioco tra coperchio e scatola; larghezza del labbro ad anello (da 1,2 a 3 mm) |
| `preset`, `part` | `alarm` | `solar`, `electrical` o `alarm`; `box`, `lid` o `both` |
| `vent` | `true` | Una fila di fessure nel coperchio per far uscire il calore |

| Pezzo | Interno (mm) | Scheda (mm) |
|---|---|---|
| `solar` | 110 × 80 × 45 | 66 × 53 |
| `electrical` | 140 × 100 × 50 | 120 × 80 |
| `alarm` | 150 × 110 × 60 | 120 × 80 |""",
      "quickstart": r"""**Requisiti:** OpenSCAD 2021.01+ (per renderizzare gli involucri), una stampante 3D (FDM) per provarli.

```powershell
openscad -o build/node_enclosure_radar.stl scad/node_enclosure_radar.scad
openscad -D 'part="both"' -D 'preset="alarm"' -o build/node_box_alarm.stl scad/node_box.scad   # presets: solar, electrical, alarm
```

Vedi il [confine di validazione](docs/VALIDATION.md). La licenza hardware prevista è CERN-OHL-S-2.0; aggiungi il suo testo completo prima di pubblicare i progetti.""",
      "testing": r"""```powershell
python -m unittest discover -s tests   # 22 tests, no OpenSCAD needed
python -I tools/armor_ci_validate.py
```

| File di test | Test | Cosa copre |
|---|---|---|
| `test_enclosure_sources.py` | 22 | I sorgenti, i preset della scatola, i file di modello e i numeri citati dai documenti |

OpenSCAD è in grado di renderizzare ogni pezzo su una macchina che lo ha: base e coperchio del radar, scatola e coperchio dei tre preset. Nella [matrice di accettazione al banco](docs/BENCH_ACCEPTANCE.md) si giudica un prototipo stampato.""",
      "troubleshooting": r"""| Vedi | Perché | Fai |
|---|---|---|
| `preset must be solar, electrical or alarm` | Il `preset` è un altro valore | `-D 'preset="alarm"'` |
| `the board and its posts do not fit inside the box` | Un parametro ha reso i supporti troppo grandi per l'interno | Ripristina `post_d` o scegli un preset più grande |
| Il coperchio non si chiude | La tua stampante è più stretta del gioco di 0,3 mm | Aumenta `clear` e ristampa |""",
      "structure": r"""<p align="center">
  <img src="images/repository-structure.svg" alt="Struttura del repository di ARMOR-HARDWARE" width="100%">
</p>

<details>
<summary>Versione testuale dell'albero</summary>

```text
ARMOR-HARDWARE/
├── scad/                                gli involucri e i loro file di modello
├── docs/                                le guide di questo repository
├── tests/                               i test
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
└── .gitattributes .gitignore            impostazioni di Git
```

</details>""",
      "roadmap": r"""**Limiti noti oggi**

* Nulla è stato stampato né misurato; le dimensioni delle schede vengono dai datasheet e ogni riga della matrice di accettazione al banco è *non testata*.
* Non ci sono ancora volumi per la scheda ESP32-S3-ETH-PoE, i magnetici PoE, il riscaldatore PTC né la finestra del sensore di luce; il pannello touch non ha una scatola stampata (conserva l'involucro di fabbrica).
* La licenza hardware prevista per i progetti è CERN-OHL-S-2.0 e il suo testo completo non è ancora nel repository.

**Prossimi passi**

* Registrare i contorni esatti delle schede, i connettori, le posizioni delle viti, le zone libere dell'antenna, il percorso termico e l'obiettivo di protezione ([dati di progetto](docs/DESIGN_INPUTS.md)).
* Stampare i prototipi e compilare la matrice di accettazione al banco con misure datate.""",
    },
  },
  "ja": {
    "tagline": "筐体、電子部品、ベンチ受け入れマトリクス",
    "honest": "レーダーの筐体は**印刷できる機構の出発点であり、IP・RF・熱の等級ではなく**、太陽光・電気・警報ノード用のパラメトリックボックスはソースの `assert` で検査されています（基板が収まる、ケーブル穴が収まる、蓋がポストを避ける）が、**どれも印刷も計測もされていません**（基板の寸法はデータシート由来で、タッチパネルには印刷ボックスはなく、出荷時の筐体を使います）。[ベンチ受入マトリクス](docs/BENCH_ACCEPTANCE.md)のすべての行は*未テスト*です。",
    "glance": [
      [
        "役割",
        "筐体、電子部品、ベンチ受け入れマトリクス（ファミリー：Hardware、親：ARMOR-NODE-RADAR）",
      ],
      [
        "技術",
        "OpenSCAD 2021.01+（CAD）、Python 3.11+（検査）",
      ],
      [
        "テスト",
        "22 (`python -m unittest discover -s tests`)",
      ],
      [
        "設計",
        "レーダー筐体と 3 つのノードプリセット（ソーラー、電気、アラーム）の箱",
      ],
      [
        "動作環境",
        "OpenSCAD のある任意のコンピューター",
      ],
      [
        "実機での確認",
        "まだありません：何も印刷も計測もされていません。3 つのボックスはソースの `assert` で検査されているだけです",
      ],
      [
        "ライセンス",
        "GPL-3.0-or-later",
      ],
    ],
    "status": {
      "software": "レーダーの筐体と、太陽光・電気・警報ノード用のパラメトリックなボックスは OpenSCAD のソースです。レーダーのボックスは印刷できる出発点で、IP・RF・熱の等級ではありません。",
      "tests": "22 件のテストが通ります（`python -m unittest discover -s tests`）：ソース、箱のプリセット、モデルファイル、文書が引用する数値。箱はソースの `assert` でも検証されますが、印刷も測定もしていません。",
      "hardware": "何も印刷も実測もしておらず、基板の寸法はデータシートに基づいています。ベンチ受け入れマトリクスの全行が未テストです。",
      "docs": "8 言語、設計の入力条件、ベンチ受け入れマトリクスが書かれていて最新です。",
    },
    "docs": [
      "[設計入力](docs/DESIGN_INPUTS.md)：製造前に記録すること",
      "[検証の境界](docs/VALIDATION.md)：検証済みの範囲と未検証の範囲",
      "[ベンチ受け入れマトリクス](docs/BENCH_ACCEPTANCE.md)：検査、方法、合格基準の案",
    ],
    "contributing_first": "Pull Request の前に `python -m unittest discover -s tests` and `python -I tools/armor_ci_validate.py` を実行してください。通る必要があります。[CONTRIBUTING.md](CONTRIBUTING.md) と[行動規範](CODE_OF_CONDUCT.md)を参照してください。",
    "languages_extra": "",
    "body": {
      "overview": r"""* **レーダーの筐体は `scad/node_enclosure_radar.scad`**（STL・3MF・AMF の出力と、ベースとスライドカバーの 2 つのスライサープロジェクト付き）：バイザー、屋根、床、固定用の段差、2 mm のスライド式フロントカバー、側面フラップを備えた 90 度コーナーのベースで、すべて名前付きパラメーターで動きます。
* **太陽光・電気・警報ノード用のパラメトリックボックス**（`scad/node_box.scad`、プリセット `solar`、`electrical`、`alarm`）：壁、基板用のポスト、ケーブルグランド用の穴、通気口、蓋の下の改ざん検知マイクロスイッチ用ポケット、リング状のリップ付きの蓋。低電圧用のボックスであり、商用電源配線用の筐体ではありません。
* **ホルダー**：3 つのレーダーモジュール、ケーブルグランド、排水穴用。ベンチマトリクスが試験したい ESP32-S3-ETH-PoE 基板、PoE マグネティクス、PTC ヒーター、光センサー窓の空間はまだありません。24 GHz の開口の前には、測定せずに金属・導電性・カーボン入りの材料を置かないでください。
* **ベンチ受入マトリクス：**無線、環境、電源、ネットワーク、カメラの検査それぞれに方法と合格基準の案があり、記入するカメラ互換表もあります。
* 製作前に、基板の正確な外形、コネクター、ネジ位置、アンテナの禁止領域、熱経路、侵入保護の目標を記録します（[設計入力](docs/DESIGN_INPUTS.md)）。""",
      "role": "ARMOR-HARDWARE はノードを収めるものです。レーダーノードの筐体、太陽光・電気・警報・タッチパネルノードのパラメトリックボックス、壁に付ける前に試作品をどう評価するかを示すベンチ受入マトリクスを含みます。その設計は、[ARMOR-NODE-RADAR](https://github.com/JuanenRac/ARMOR-NODE-RADAR)、[ARMOR-NODE-SOLAR](https://github.com/JuanenRac/ARMOR-NODE-SOLAR)、[ARMOR-NODE-ELECTRICAL](https://github.com/JuanenRac/ARMOR-NODE-ELECTRICAL)、[ARMOR-NODE-ALARM](https://github.com/JuanenRac/ARMOR-NODE-ALARM)、[ARMOR-NODE-HMI](https://github.com/JuanenRac/ARMOR-NODE-HMI) が動く基板の出発点です。",
      "architecture": r"""<p align="center">
  <img src="images/architecture.svg" alt="ARMOR-HARDWARE のアーキテクチャ：呼び出し元、内部、依存先" width="100%">
</p>""",
      "security": r"""| 脅威 | 対策 |
|---|---|
| プラスチックの箱での商用電源配線 | `node_box.scad` は低電圧用の箱で、商用電源配線用の筐体ではありません |
| 24 GHz レーダーの遮蔽 | 測定せずに 24 GHz の開口部の前へ金属・導電性・カーボン入り材料を置かない。カバー厚 2 mm はベンチマトリクスの 1 行です |
| 存在しないプリセットや部品 | `assert` がレンダリングを止めます：`preset must be solar, electrical or alarm`、`part must be box, lid or both` |
| 合わない造形物 | ソースの `assert` がレンダリング時に検出します：基板とポストが収まる、ケーブル穴が壁やポストで切られず内側より高くない、蓋のリップは 1.2〜3 mm |

レーダー筐体は印刷できる機構上の出発点であり、**IP・RF・熱の等級ではありません**。印刷も測定もしていません。""",
      "configuration": r"""| 名前 | 値 | 設定内容 |
|---|---|---|
| `wall`, `lid_t` | 3 mm, 3 mm | `node_box.scad` の壁と蓋の厚さ |
| `post_d`, `post_h`, `post_cap` | 7, 6, 9 mm | 基板と蓋ネジ用のポスト |
| `screw_d` | 3.2 mm | ポストにねじ込む M3 タッピングネジ |
| `clear`, `lip_w` | 0.3 mm, 1.6 mm | 蓋と箱の隙間、リング状リップの幅（1.2〜3 mm） |
| `preset`, `part` | `alarm` | `solar`、`electrical`、`alarm`／`box`、`lid`、`both` |
| `vent` | `true` | 熱を逃がすための蓋のスリット |

| 部品 | 内寸 (mm) | 基板 (mm) |
|---|---|---|
| `solar` | 110 × 80 × 45 | 66 × 53 |
| `electrical` | 140 × 100 × 50 | 120 × 80 |
| `alarm` | 150 × 110 × 60 | 120 × 80 |""",
      "quickstart": r"""**必要なもの:** OpenSCAD 2021.01+ (筐体のレンダリング用), 試作用の 3D プリンター（FDM）.

```powershell
openscad -o build/node_enclosure_radar.stl scad/node_enclosure_radar.scad
openscad -D 'part="both"' -D 'preset="alarm"' -o build/node_box_alarm.stl scad/node_box.scad   # presets: solar, electrical, alarm
```

[検証の境界](docs/VALIDATION.md)を参照してください。想定しているハードウェアライセンスは CERN-OHL-S-2.0 で、設計を公開する前に全文を追加してください。""",
      "testing": r"""```powershell
python -m unittest discover -s tests   # 22 tests, no OpenSCAD needed
python -I tools/armor_ci_validate.py
```

| テストファイル | テスト数 | 対象 |
|---|---|---|
| `test_enclosure_sources.py` | 22 | ソース、箱のプリセット、モデルファイル、文書が引用する数値 |

OpenSCAD が使える環境では各部品（レーダーのベースとカバー、3 つのプリセットの箱と蓋）をレンダリングします。印刷した試作品は[ベンチ受け入れマトリクス](docs/BENCH_ACCEPTANCE.md)で評価します。""",
      "troubleshooting": r"""| 症状 | 原因 | 対処 |
|---|---|---|
| `preset must be solar, electrical or alarm` | `preset` が別の値 | `-D 'preset="alarm"'` |
| `the board and its posts do not fit inside the box` | パラメーターのせいでポストが内側に収まらない | `post_d` を戻すか大きいプリセットを選ぶ |
| 蓋が閉まらない | プリンターの精度が 0.3 mm の隙間より厳しい | `clear` を大きくして再印刷 |""",
      "structure": r"""<p align="center">
  <img src="images/repository-structure.svg" alt="ARMOR-HARDWARE のリポジトリ構造" width="100%">
</p>

<details>
<summary>ツリーのテキスト版</summary>

```text
ARMOR-HARDWARE/
├── scad/                                筐体とそのモデルファイル
├── docs/                                このリポジトリのガイド
├── tests/                               テスト
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
└── .gitattributes .gitignore            Git の設定
```

</details>""",
      "roadmap": r"""**現時点の既知の制限**

* 印刷も測定もしておらず、基板サイズはデータシート由来で、ベンチ受け入れマトリクスの全行が*未試験*です。
* ESP32-S3-ETH-PoE 基板、PoE マグネティクス、PTC ヒーター、光センサー窓の立体はまだなく、タッチパネルには印刷した箱がありません（工場出荷時の筐体のままです）。
* 設計に予定しているハードウェアライセンスは CERN-OHL-S-2.0 で、全文はまだリポジトリにありません。

**今後**

* 正確な基板外形、コネクター、ネジ位置、アンテナの空き領域、放熱経路、防水目標を記録する（[設計入力](docs/DESIGN_INPUTS.md)）。
* 試作品を印刷し、日付入りの測定値でベンチ受け入れマトリクスを埋める。""",
    },
  },
  "zh": {
    "tagline": "外壳、电子器件和台架验收矩阵",
    "honest": "雷达外壳是**可打印的机械起点，不是 IP、射频或热学等级**；用于太阳能、电气和报警节点的参数化盒子由其源文件中的 `assert` 检查（板子放得下、电缆孔放得下、盖子避开立柱），但**都没有打印或测量过**（板子尺寸来自数据手册；触摸屏没有打印的盒子，沿用出厂外壳）。[台架验收矩阵](docs/BENCH_ACCEPTANCE.md)的每一行都是*未测试*。",
    "glance": [
      [
        "角色",
        "外壳、电子元件和台架验收矩阵（家族：Hardware，上级：ARMOR-NODE-RADAR）",
      ],
      [
        "技术栈",
        "OpenSCAD 2021.01+（CAD）、Python 3.11+（检查）",
      ],
      [
        "测试",
        "22 (`python -m unittest discover -s tests`)",
      ],
      [
        "设计",
        "雷达外壳和 3 种节点预设（太阳能、电气、报警）的盒子",
      ],
      [
        "运行位置",
        "任何装有 OpenSCAD 的计算机",
      ],
      [
        "真实硬件",
        "暂无：没有任何东西被打印或测量过；三个盒子只由源文件中的 `assert` 检查",
      ],
      [
        "许可证",
        "GPL-3.0-or-later",
      ],
    ],
    "status": {
      "software": "雷达外壳以及光伏、电气和报警节点的参数化盒子都是 OpenSCAD 源文件；雷达盒子是可打印的起点，并非 IP、射频或温度等级。",
      "tests": "22 个测试通过（`python -m unittest discover -s tests`）：源文件、盒子预设、模型文件以及文档中引用的数字。盒子也由其源码中的 `assert` 检查；都没有打印或测量过。",
      "hardware": "没有任何东西被打印或测量过，板子的尺寸来自数据手册，测试台验收矩阵的每一行都未测试。",
      "docs": "八种语言、设计输入和测试台验收矩阵均已编写并保持最新。",
    },
    "docs": [
      "[设计输入](docs/DESIGN_INPUTS.md)：制造前要记录的内容",
      "[验证边界](docs/VALIDATION.md)：哪些已验证、哪些未验证",
      "[台架验收矩阵](docs/BENCH_ACCEPTANCE.md)：检查项、方法和建议的通过标准",
    ],
    "contributing_first": "提交 Pull Request 之前请运行 `python -m unittest discover -s tests` and `python -I tools/armor_ci_validate.py`：必须通过。参见 [CONTRIBUTING.md](CONTRIBUTING.md) 和[行为准则](CODE_OF_CONDUCT.md)。",
    "languages_extra": "",
    "body": {
      "overview": r"""* **雷达外壳是 `scad/node_enclosure_radar.scad`**（带 STL、3MF 和 AMF 导出以及两个切片项目：底座和滑动盖）：带遮阳罩、顶和底的 90 度转角底座、固定台阶、2 毫米的滑动前盖和侧翼，全部由命名参数驱动。
* **用于太阳能、电气和报警节点的参数化盒子**（`scad/node_box.scad`，预设 `solar`、`electrical` 和 `alarm`）：墙壁、板子立柱、电缆格兰头孔、通风孔、盖下的防拆微动开关槽，以及带环形唇边的盖子。这是低压盒子，不是市电布线的外壳。
* **支架**用于三个雷达模块、一个电缆格兰头和排水孔。台架矩阵要测试的 ESP32-S3-ETH-PoE 板、PoE 磁件、PTC 加热器和光传感器窗口还没有预留空间。未经测量，24 GHz 孔径前不要放置金属、导电或含碳的材料。
* **台架验收矩阵：**射频、环境、电源、网络和摄像头检查，每项都有方法和建议的通过标准，另有待填写的摄像头兼容性表。
* 制造之前，记录板子的确切轮廓、连接器、螺丝位置、天线净空区、热路径和防护目标（[设计输入](docs/DESIGN_INPUTS.md)）。""",
      "role": "ARMOR-HARDWARE 是容纳各节点的部分。它包含雷达节点的外壳、太阳能、电气、报警和触摸屏节点的参数化盒子，以及说明原型上墙前如何评判的台架验收矩阵。它的设计是 [ARMOR-NODE-RADAR](https://github.com/JuanenRac/ARMOR-NODE-RADAR)、[ARMOR-NODE-SOLAR](https://github.com/JuanenRac/ARMOR-NODE-SOLAR)、[ARMOR-NODE-ELECTRICAL](https://github.com/JuanenRac/ARMOR-NODE-ELECTRICAL)、[ARMOR-NODE-ALARM](https://github.com/JuanenRac/ARMOR-NODE-ALARM) 和 [ARMOR-NODE-HMI](https://github.com/JuanenRac/ARMOR-NODE-HMI) 所运行的板子的起点。",
      "architecture": r"""<p align="center">
  <img src="images/architecture.svg" alt="ARMOR-HARDWARE 的架构：谁调用它、它包含什么、它依赖什么" width="100%">
</p>""",
      "security": r"""| 威胁 | 防御 |
|---|---|
| 在塑料盒中布设市电线路 | `node_box.scad` 是低压盒子，不是市电布线外壳 |
| 被遮挡的 24 GHz 雷达 | 未经测量，不要在 24 GHz 开口前放置金属、导电或含碳材料；盖板 2 mm 的厚度是台架矩阵中的一行 |
| 不存在的预设或部件 | `assert` 会中止渲染：`preset must be solar, electrical or alarm`、`part must be box, lid or both` |
| 无法装配的打印件 | 源码中的 `assert` 在渲染时拦截：电路板及其立柱能装下，电缆孔不被墙或立柱截断也不高于内部，盖唇宽 1.2 到 3 mm |

雷达外壳是可打印的机械起点，**不是 IP、射频或热学等级**。尚未打印或测量过任何东西。""",
      "configuration": r"""| 名称 | 值 | 作用 |
|---|---|---|
| `wall`, `lid_t` | 3 mm, 3 mm | `node_box.scad` 的壁厚与盖厚 |
| `post_d`, `post_h`, `post_cap` | 7, 6, 9 mm | 电路板与盖板螺钉的立柱 |
| `screw_d` | 3.2 mm | 拧入立柱的 M3 自攻螺钉 |
| `clear`, `lip_w` | 0.3 mm, 1.6 mm | 盖与盒之间的间隙；环形唇的宽度（1.2 到 3 mm） |
| `preset`, `part` | `alarm` | `solar`、`electrical` 或 `alarm`；`box`、`lid` 或 `both` |
| `vent` | `true` | 盖上用于散热的一排槽 |

| 部件 | 内部尺寸 (mm) | 电路板 (mm) |
|---|---|---|
| `solar` | 110 × 80 × 45 | 66 × 53 |
| `electrical` | 140 × 100 × 50 | 120 × 80 |
| `alarm` | 150 × 110 × 60 | 120 × 80 |""",
      "quickstart": r"""**要求:** OpenSCAD 2021.01+ (用于渲染外壳), 用于试制的 3D 打印机（FDM）.

```powershell
openscad -o build/node_enclosure_radar.stl scad/node_enclosure_radar.scad
openscad -D 'part="both"' -D 'preset="alarm"' -o build/node_box_alarm.stl scad/node_box.scad   # presets: solar, electrical, alarm
```

参见[验证边界](docs/VALIDATION.md)。预期的硬件许可证是 CERN-OHL-S-2.0；发布设计前请加入其完整文本。""",
      "testing": r"""```powershell
python -m unittest discover -s tests   # 22 tests, no OpenSCAD needed
python -I tools/armor_ci_validate.py
```

| 测试文件 | 测试数 | 覆盖内容 |
|---|---|---|
| `test_enclosure_sources.py` | 22 | 源文件、盒子预设、模型文件以及文档中引用的数字 |

在装有 OpenSCAD 的机器上会渲染每个部件：雷达底座和盖板，以及三种预设的盒子和盖子。打印出的原型由[台架验收矩阵](docs/BENCH_ACCEPTANCE.md)评判。""",
      "troubleshooting": r"""| 现象 | 原因 | 处理 |
|---|---|---|
| `preset must be solar, electrical or alarm` | `preset` 取了其他值 | `-D 'preset="alarm"'` |
| `the board and its posts do not fit inside the box` | 某个参数使立柱对内部来说太大 | 恢复 `post_d` 或选择更大的预设 |
| 盖子盖不上 | 打印机比 0.3 mm 的间隙更紧 | 增大 `clear` 后重新打印 |""",
      "structure": r"""<p align="center">
  <img src="images/repository-structure.svg" alt="ARMOR-HARDWARE 的仓库结构" width="100%">
</p>

<details>
<summary>目录树的文本版</summary>

```text
ARMOR-HARDWARE/
├── scad/                                外壳及其模型文件
├── docs/                                本仓库的指南
├── tests/                               测试
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
└── .gitattributes .gitignore            Git 设置
```

</details>""",
      "roadmap": r"""**目前已知的限制**

* 尚未打印或测量；电路板尺寸来自数据手册，台架验收矩阵的每一行都是*未测试*。
* 尚未绘制 ESP32-S3-ETH-PoE 电路板、PoE 磁性元件、PTC 加热器和光传感器窗口的立体模型；触摸面板没有打印的盒子（保留出厂外壳）。
* 设计拟采用的硬件许可证是 CERN-OHL-S-2.0，其全文尚未放入仓库。

**下一步**

* 记录精确的电路板轮廓、连接器、螺钉位置、天线净空区、散热路径和防护目标（[设计输入](docs/DESIGN_INPUTS.md)）。
* 打印原型，并用带日期的测量结果填写台架验收矩阵。""",
    },
  },
  "pt": {
    "tagline": "Caixas, eletrónica e a matriz de aceitação de bancada",
    "honest": "A caixa do radar é um **ponto de partida mecânico imprimível, não uma classificação IP, RF ou térmica**, e a caixa paramétrica para os nós solar, elétrico e de alarme é verificada pelos `assert` do seu código (a placa cabe, os furos dos cabos cabem, a tampa liberta os pilares), mas **nenhuma foi impressa nem medida** (os tamanhos das placas vêm das folhas de dados; o painel tátil não tem caixa impressa, mantém a sua caixa de fábrica). Cada linha da [matriz de aceitação em bancada](docs/BENCH_ACCEPTANCE.md) está *por testar*.",
    "glance": [
      [
        "Função",
        "Caixas, eletrónica e a matriz de aceitação em bancada (família: Hardware, pai: ARMOR-NODE-RADAR)",
      ],
      [
        "Tecnologia",
        "OpenSCAD 2021.01+ (CAD), Python 3.11+ (verificações)",
      ],
      [
        "Testes",
        "22 (`python -m unittest discover -s tests`)",
      ],
      [
        "Desenhos",
        "A caixa do radar e a caixa de 3 presets de nó (solar, elétrico, alarme)",
      ],
      [
        "Funciona em",
        "Qualquer computador com OpenSCAD",
      ],
      [
        "Em hardware real",
        "Nenhum ainda: nada foi impresso nem medido; as três caixas só são verificadas pelos `assert` do seu código",
      ],
      [
        "Licença",
        "GPL-3.0-or-later",
      ],
    ],
    "status": {
      "software": "A caixa do radar e a caixa paramétrica dos nós solar, elétrico e de alarme são fontes de OpenSCAD; a caixa do radar é um ponto de partida imprimível, não uma classificação IP, RF nem térmica.",
      "tests": "Passam 22 testes (`python -m unittest discover -s tests`): as fontes, os presets da caixa, os ficheiros de modelo e os números que os documentos citam. As caixas também são verificadas pelos `assert` da sua fonte; nenhuma foi impressa nem medida.",
      "hardware": "Nada foi impresso nem medido, as medidas das placas vêm de folhas de dados, e cada linha da matriz de aceitação em bancada está por testar.",
      "docs": "Oito idiomas, os dados de projeto e a matriz de aceitação em bancada estão escritos e atualizados.",
    },
    "docs": [
      "[Dados de projeto](docs/DESIGN_INPUTS.md): o que registar antes de fabricar",
      "[Limite da validação](docs/VALIDATION.md): o que está e o que não está validado",
      "[Matriz de aceitação em bancada](docs/BENCH_ACCEPTANCE.md): as verificações, os métodos e os critérios propostos",
    ],
    "contributing_first": "Antes de um pull request, execute `python -m unittest discover -s tests` and `python -I tools/armor_ci_validate.py`: tem de passar. Consulte [CONTRIBUTING.md](CONTRIBUTING.md) e o [código de conduta](CODE_OF_CONDUCT.md).",
    "languages_extra": "",
    "body": {
      "overview": r"""* **A caixa do radar é `scad/node_enclosure_radar.scad`** (com exportações STL, 3MF e AMF e dois projetos de fatiador, a base e a tampa deslizante): uma base de canto de 90 graus com viseira, teto e chão, degraus de retenção, uma tampa frontal deslizante de 2 mm e abas laterais, tudo governado por parâmetros com nome.
* **Uma caixa paramétrica para os nós solar, elétrico e de alarme** (`scad/node_box.scad`, predefinidos `solar`, `electrical` e `alarm`): paredes, pilares para a placa, furos para bucins, uma ventilação, um espaço para um microinterruptor antissabotagem sob a tampa e uma tampa com lábio anular. É uma caixa de baixa tensão, não um invólucro para cablagem de rede.
* **Suportes** para três módulos de radar, um bucim e furos de drenagem. Ainda não há volumes para a placa ESP32-S3-ETH-PoE, a magnética PoE, o aquecedor PTC nem a janela do sensor de luz que a matriz de bancada quer testar. Nenhum material metálico, condutor ou carregado de carbono à frente de uma abertura de 24 GHz sem o medir.
* **Matriz de aceitação em bancada:** as verificações de rádio, ambiente, alimentação, rede e câmara com um método e um critério de aprovação proposto cada uma, e uma tabela de compatibilidade de câmaras por preencher.
* Antes de fabricar, registe os contornos exatos das placas, conectores, posições de parafusos, zonas livres de antena, o caminho térmico e o objetivo de proteção ([dados de desenho](docs/DESIGN_INPUTS.md)).""",
      "role": "O ARMOR-HARDWARE é o que contém os nós. Leva a caixa do nó radar, a caixa paramétrica dos nós solar, elétrico, de alarme e de painel tátil, e a matriz de aceitação em bancada que diz como julgar um protótipo antes de o pôr numa parede. Os seus desenhos são o ponto de partida para as placas em que correm o [ARMOR-NODE-RADAR](https://github.com/JuanenRac/ARMOR-NODE-RADAR), o [ARMOR-NODE-SOLAR](https://github.com/JuanenRac/ARMOR-NODE-SOLAR), o [ARMOR-NODE-ELECTRICAL](https://github.com/JuanenRac/ARMOR-NODE-ELECTRICAL), o [ARMOR-NODE-ALARM](https://github.com/JuanenRac/ARMOR-NODE-ALARM) e o [ARMOR-NODE-HMI](https://github.com/JuanenRac/ARMOR-NODE-HMI).",
      "architecture": r"""<p align="center">
  <img src="images/architecture.svg" alt="Arquitetura de ARMOR-HARDWARE: quem o chama, o que contém e de que depende" width="100%">
</p>""",
      "security": r"""| Ameaça | Defesa |
|---|---|
| Cablagem de rede numa caixa de plástico | `node_box.scad` é uma caixa de baixa tensão, não uma caixa para cablagem de rede |
| Um radar de 24 GHz bloqueado | Nenhum material metálico, condutor ou com carbono diante de uma abertura de 24 GHz sem o medir; a espessura de 2 mm da tampa é uma linha da matriz de bancada |
| Um preset ou uma peça que não existe | Um `assert` pára a renderização: `preset must be solar, electrical or alarm`, `part must be box, lid or both` |
| Uma impressão que não encaixa | Os `assert` da fonte apanham-no ao renderizar: a placa e os seus postes cabem, os furos de cabo não são cortados por uma parede ou poste nem são mais altos que o interior, o lábio da tampa mede de 1,2 a 3 mm |

A caixa do radar é um ponto de partida mecânico imprimível, **não uma classificação IP, RF nem térmica**. Nada foi impresso nem medido.""",
      "configuration": r"""| Nome | Valor | O que define |
|---|---|---|
| `wall`, `lid_t` | 3 mm, 3 mm | Espessura da parede e da tampa de `node_box.scad` |
| `post_d`, `post_h`, `post_cap` | 7, 6, 9 mm | Os postes da placa e dos parafusos da tampa |
| `screw_d` | 3.2 mm | Parafusos M3 autorroscantes nos postes |
| `clear`, `lip_w` | 0.3 mm, 1.6 mm | Folga entre tampa e caixa; largura do lábio em anel (1,2 a 3 mm) |
| `preset`, `part` | `alarm` | `solar`, `electrical` ou `alarm`; `box`, `lid` ou `both` |
| `vent` | `true` | Uma fila de ranhuras na tampa para sair o calor |

| Peça | Interior (mm) | Placa (mm) |
|---|---|---|
| `solar` | 110 × 80 × 45 | 66 × 53 |
| `electrical` | 140 × 100 × 50 | 120 × 80 |
| `alarm` | 150 × 110 × 60 | 120 × 80 |""",
      "quickstart": r"""**Requisitos:** OpenSCAD 2021.01+ (para renderizar as caixas), uma impressora 3D (FDM) para as experimentar.

```powershell
openscad -o build/node_enclosure_radar.stl scad/node_enclosure_radar.scad
openscad -D 'part="both"' -D 'preset="alarm"' -o build/node_box_alarm.stl scad/node_box.scad   # presets: solar, electrical, alarm
```

Veja o [limite de validação](docs/VALIDATION.md). A licença de hardware prevista é CERN-OHL-S-2.0; acrescente o seu texto completo antes de publicar os desenhos.""",
      "testing": r"""```powershell
python -m unittest discover -s tests   # 22 tests, no OpenSCAD needed
python -I tools/armor_ci_validate.py
```

| Ficheiro de testes | Testes | O que cobre |
|---|---|---|
| `test_enclosure_sources.py` | 22 | As fontes, os presets da caixa, os ficheiros de modelo e os números que os documentos citam |

O OpenSCAD renderiza cada peça numa máquina que o tenha: a base e a tampa do radar, e a caixa e a tampa dos três presets. A [matriz de aceitação em bancada](docs/BENCH_ACCEPTANCE.md) é onde se avalia um protótipo impresso.""",
      "troubleshooting": r"""| Vê | Porque | Faça |
|---|---|---|
| `preset must be solar, electrical or alarm` | O `preset` é outro valor | `-D 'preset="alarm"'` |
| `the board and its posts do not fit inside the box` | Um parâmetro tornou os postes demasiado grandes para o interior | Reponha `post_d` ou escolha um preset maior |
| A tampa não fecha | A sua impressora é mais apertada do que a folga de 0,3 mm | Aumente `clear` e imprima de novo |""",
      "structure": r"""<p align="center">
  <img src="images/repository-structure.svg" alt="Estrutura do repositório de ARMOR-HARDWARE" width="100%">
</p>

<details>
<summary>Versão em texto da árvore</summary>

```text
ARMOR-HARDWARE/
├── scad/                                as caixas e os seus ficheiros de modelo
├── docs/                                os guias deste repositório
├── tests/                               os testes
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
└── .gitattributes .gitignore            definições do Git
```

</details>""",
      "roadmap": r"""**Limites conhecidos hoje**

* Nada foi impresso nem medido; os tamanhos das placas vêm de folhas de dados e cada linha da matriz de aceitação em bancada está *por testar*.
* Ainda não há volumes para a placa ESP32-S3-ETH-PoE, os magnéticos PoE, o aquecedor PTC nem a janela do sensor de luz; o painel tátil não tem caixa impressa (mantém a caixa de fábrica).
* A licença de hardware prevista para os desenhos é a CERN-OHL-S-2.0 e o seu texto completo ainda não está no repositório.

**A seguir**

* Registar os contornos exatos das placas, conectores, posições dos parafusos, zonas livres da antena, o caminho térmico e o objetivo de proteção ([dados de projeto](docs/DESIGN_INPUTS.md)).
* Imprimir os protótipos e preencher a matriz de aceitação em bancada com medições datadas.""",
    },
  },
}
