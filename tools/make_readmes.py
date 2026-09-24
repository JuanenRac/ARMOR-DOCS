#!/usr/bin/env python3
"""Render the README.md / README_spa.md pair of the repositories that share the family layout.

Copyright (C) 2026 JuanenRac (Electro Hobby 3D). GPL-3.0-or-later.

Each repository is described once, in English and Spanish, so the two files can
never drift apart in structure. ARMOR-SERVER, ARMOR-STUDIO, ARMOR-COMMON and
ARMOR-DOCS have hand-written READMEs and are not rendered here.

    python tools/make_readmes.py          # write the READMEs
    python tools/make_readmes.py --check  # fail when one is out of date
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

LABELS = {
    "en": {"overview": "OVERVIEW", "build": "BUILD & RUN", "structure": "DIRECTORY STRUCTURE", "author": "AUTHOR", "license": "LICENSE",
           "honesty": "Honesty check - what runs today", "license_text": "GPL-3.0-or-later - see [LICENSE](LICENSE).", "lang": "🇺🇸 <b>English</b> | <a href=\"README_spa.md\">🇪🇸 Español</a>",
           "docs": "Documentation"},
    "es": {"overview": "DESCRIPCIÓN", "build": "COMPILAR Y EJECUTAR", "structure": "ESTRUCTURA DE DIRECTORIOS", "author": "AUTOR", "license": "LICENCIA",
           "honesty": "Comprobación de honestidad - qué funciona hoy", "license_text": "GPL-3.0-or-later - véase [LICENSE](LICENSE).", "lang": "<a href=\"README.md\">🇺🇸 English</a> | 🇪🇸 <b>Español</b>",
           "docs": "Documentación"},
}

REPOS: dict[str, dict] = {
    "ARMOR-SIMULATOR": {
        "emoji": "🧪", "badges": [("Language", "Python%203.11%2B", "3776ab"), ("Dependencies", "none", "2ea44f"), ("Maturity", "functional", "00E5FF")],
        "en": {
            "tagline": "Offline telemetry simulator with repeatable faults",
            "honest": "Scenarios, faults, delivery to a server and the 24 tests are real. The geometry is **illustrative**, not a model of the real LD2450 radar, and nothing here has been compared with real hardware.",
            "bullets": ["**Scenarios:** `patrol`, `crossing`, `two-intruders` and `empty`, on a three-sensor corner geometry, plus a day/night light cycle or a fixed night.",
                        "**Repeatable faults:** a silent node, out-of-order and duplicated messages, a flapping node, and deliberately invalid messages (lux over the limit, unknown field, too many tracks) for negative tests.",
                        "**Deterministic:** the same seed always prints the same lines; nothing is sent unless you give `--server-url` and `--ingest-token`.",
                        "**Checked against the contract:** `--validate` runs every message through ARMOR-COMMON before it is emitted.",
                        "**Careful delivery:** only a plain http(s) origin is accepted; a 4xx stops the run, a 5xx or a network error is retried."],
            "build": "```powershell\n$env:PYTHONPATH=\"src\"\npython -m armor_simulator --count 20 --scenario crossing --seed 1 --validate\npython -m unittest discover -s tests   # 24 tests\n```\n\nFull options, scenarios and faults: [usage](docs/USAGE.md).",
            "structure": "```text\nARMOR-SIMULATOR/\n├── src/armor_simulator/   scenarios, faults, publisher, cli\n├── tests/                 24 tests, including a local HTTP server\n└── docs/USAGE.md\n```"},
        "es": {
            "tagline": "Simulador de telemetría sin conexión con fallos repetibles",
            "honest": "Los escenarios, los fallos, la entrega a un servidor y los 24 tests son reales. La geometría es **ilustrativa**, no un modelo del radar LD2450 real, y nada de esto se ha comparado con hardware real.",
            "bullets": ["**Escenarios:** `patrol`, `crossing`, `two-intruders` y `empty`, con una geometría de esquina de tres sensores, más un ciclo de luz día/noche o una noche fija.",
                        "**Fallos repetibles:** nodo en silencio, mensajes desordenados y duplicados, nodo intermitente y mensajes inválidos a propósito (lux por encima del límite, campo desconocido, demasiadas pistas) para pruebas negativas.",
                        "**Determinista:** la misma semilla imprime siempre las mismas líneas; no se envía nada salvo que indiques `--server-url` y `--ingest-token`.",
                        "**Comprobado contra el contrato:** `--validate` pasa cada mensaje por ARMOR-COMMON antes de emitirlo.",
                        "**Entrega cuidadosa:** solo se acepta un origen http(s) simple; un 4xx detiene la ejecución, un 5xx o un error de red se reintenta."],
            "build": "```powershell\n$env:PYTHONPATH=\"src\"\npython -m armor_simulator --count 20 --scenario crossing --seed 1 --validate\npython -m unittest discover -s tests   # 24 tests\n```\n\nOpciones, escenarios y fallos completos: [uso](docs/USAGE.md).",
            "structure": "```text\nARMOR-SIMULATOR/\n├── src/armor_simulator/   scenarios, faults, publisher, cli\n├── tests/                 24 tests, con un servidor HTTP local\n└── docs/USAGE.md\n```"},
    },
    "ARMOR-SERVER-AI": {
        "emoji": "👁️", "badges": [("Language", "Python%203.11%2B", "3776ab"), ("Target", "Jetson%20Orin%20NX", "76b900"), ("Maturity", "functional%20baseline", "00E5FF")],
        "en": {
            "tagline": "Visual inference policy: decides and explains, never actuates",
            "honest": "The decision layer is real and tested (26 tests). **Nothing here runs a camera, RTSP or TensorRT yet**: that needs the Jetson, and it is not proven.",
            "bullets": ["**Day/night profile with hysteresis:** low-light below 30 lux, back to daylight only above 60 lux and never twice within 30 s, so dusk cannot make it flap.",
                        "**Explainable fusion:** each detection and the radar tracks give a severity (`ignore`, `review`, `high`) with the reasons behind it. A person seen at 80 % or more **and** a radar track is `high`; low light lowers only the review bar; a detection older than 10 s is ignored.",
                        "**Recommendations only:** a decision always carries `authorizes_action = false`. The central server authenticates and authorises every action.",
                        "**Checksum-verified engines:** pre-built TensorRT engines are accepted only if present, non-empty and, with an `engines.json`, matching their SHA-256. Nothing is compiled or downloaded.",
                        "**JSONL worker:** numbered, explained results; a bad line reports its number and never stops the stream."],
            "build": "```powershell\n$env:PYTHONPATH=\"src\"\npython -m unittest discover -s tests\necho '{\"label\":\"person\",\"confidence\":0.9,\"lux\":4,\"radar_tracks\":1}' | python -m armor_server_ai.cli\n```\n\nSee the [inference boundary](docs/INFERENCE_BOUNDARY.md).",
            "structure": "```text\nARMOR-SERVER-AI/\n├── src/armor_server_ai/   profile, policy, engine_registry, cli\n├── tests/\n└── docs/INFERENCE_BOUNDARY.md\n```"},
        "es": {
            "tagline": "Política de inferencia visual: decide y explica, nunca actúa",
            "honest": "La capa de decisión es real y está probada (26 tests). **Nada de esto ejecuta todavía una cámara, RTSP ni TensorRT**: eso necesita la Jetson y no está demostrado.",
            "bullets": ["**Perfil día/noche con histéresis:** poca luz por debajo de 30 lux, vuelve a luz diurna solo por encima de 60 lux y nunca dos veces en 30 s, de modo que el anochecer no lo hace oscilar.",
                        "**Fusión explicable:** cada detección y las pistas de radar dan una severidad (`ignore`, `review`, `high`) con sus motivos. Una persona vista al 80 % o más **y** una pista de radar es `high`; con poca luz solo baja el umbral de revisión; una detección de más de 10 s se ignora.",
                        "**Solo recomendaciones:** una decisión lleva siempre `authorizes_action = false`. El servidor central autentica y autoriza cada acción.",
                        "**Motores verificados por hash:** los motores TensorRT precompilados solo se aceptan si existen, no están vacíos y, con un `engines.json`, coinciden con su SHA-256. No se compila ni se descarga nada.",
                        "**Trabajador JSONL:** resultados numerados y explicados; una línea errónea indica su número y nunca detiene el flujo."],
            "build": "```powershell\n$env:PYTHONPATH=\"src\"\npython -m unittest discover -s tests\necho '{\"label\":\"person\",\"confidence\":0.9,\"lux\":4,\"radar_tracks\":1}' | python -m armor_server_ai.cli\n```\n\nVéase el [límite de inferencia](docs/INFERENCE_BOUNDARY.md).",
            "structure": "```text\nARMOR-SERVER-AI/\n├── src/armor_server_ai/   profile, policy, engine_registry, cli\n├── tests/\n└── docs/INFERENCE_BOUNDARY.md\n```"},
    },
    "ARMOR-VOICE-AI": {
        "emoji": "🎙️", "badges": [("Language", "Python%203.11%2B", "3776ab"), ("Mode", "offline", "2ea44f"), ("Maturity", "functional%20baseline", "00E5FF")],
        "en": {
            "tagline": "Offline voice intents with a confirmation the caller cannot forge",
            "honest": "The intent rules, the signed confirmation and the audit are real and tested (20 tests). **No speech recognition or synthesis engine is part of this repository yet.**",
            "bullets": ["**A closed allow-list:** `status`, `silence`, `arm` and `disarm`, in English and Spanish, after normalising accents, punctuation and polite filler. Anything else, or anything ambiguous, is not understood.",
                        "**A confirmation the service issues:** `arm` and `disarm` return a signed token on the first turn and are accepted only when a later turn echoes it for the same intent within 30 s. It cannot be forged, retargeted, reused or sent as a plain `confirmed: true` (that is refused).",
                        "**Decisions, not audio:** with `--audit-file` each decision records the intent, the outcome and a SHA-256 of the transcript, never audio or the raw words.",
                        "**Recommendations only:** an accepted command is passed to ARMOR-SERVER, which still authenticates and authorises it."],
            "build": "```powershell\n$env:PYTHONPATH=\"src\"\npython -m unittest discover -s tests\necho '{\"text\":\"arm the system\"}' | python -m armor_voice_ai.gateway\n```\n\nSee [voice safety](docs/SAFETY.md).",
            "structure": "```text\nARMOR-VOICE-AI/\n├── src/armor_voice_ai/   intent, confirmation, session, gateway\n├── tests/\n└── docs/SAFETY.md\n```"},
        "es": {
            "tagline": "Intenciones de voz sin conexión con una confirmación que el llamante no puede falsificar",
            "honest": "Las reglas de intención, la confirmación firmada y la auditoría son reales y están probadas (20 tests). **Ningún motor de reconocimiento o síntesis de voz forma parte todavía de este repositorio.**",
            "bullets": ["**Una lista cerrada:** `status`, `silence`, `arm` y `disarm`, en inglés y español, tras normalizar acentos, puntuación y muletillas de cortesía. Cualquier otra cosa, o algo ambiguo, no se entiende.",
                        "**Una confirmación que emite el servicio:** `arm` y `disarm` devuelven un token firmado en el primer turno y solo se aceptan cuando un turno posterior lo repite para la misma intención en 30 s. No se puede falsificar, reorientar, reutilizar ni enviar como un simple `confirmed: true` (se rechaza).",
                        "**Decisiones, no audio:** con `--audit-file` cada decisión guarda la intención, el resultado y el SHA-256 de la transcripción, nunca audio ni las palabras.",
                        "**Solo recomendaciones:** un comando aceptado pasa a ARMOR-SERVER, que sigue autenticándolo y autorizándolo."],
            "build": "```powershell\n$env:PYTHONPATH=\"src\"\npython -m unittest discover -s tests\necho '{\"text\":\"arm the system\"}' | python -m armor_voice_ai.gateway\n```\n\nVéase [seguridad de voz](docs/SAFETY.md).",
            "structure": "```text\nARMOR-VOICE-AI/\n├── src/armor_voice_ai/   intent, confirmation, session, gateway\n├── tests/\n└── docs/SAFETY.md\n```"},
    },
    "ARMOR-RADAR": {
        "emoji": "📡", "badges": [("Language", "C%2B%2B17", "00599c"), ("Target", "ESP32--S3", "e7352c"), ("Maturity", "scaffolding", "FFB020")],
        "en": {
            "tagline": "Field-node firmware and its host-tested core",
            "honest": "**Maturity: scaffolding.** The hardware-independent core (77 checks) and the firmware's JSON (validated by ARMOR-COMMON) are real. `main/app_main.cpp` is **not compiled here** (it needs ESP-IDF 5.x and a board), and the LD2450/LD2461 frame layout is **deliberately not decoded**: it must come from the vendor protocol document and captured UART data, so no track is ever invented.",
            "bullets": ["**Resynchronising framer:** finds frames in a noisy UART stream by header, length and tail, drops one byte on a mismatch and carries on. Its protocol spec for the real radar is unconfigured until the vendor document is added.",
                        "**Contract-exact messages:** the telemetry and health JSON follow the published schemas (15 tracks, 5 per sensor, lux range, node-id pattern) and refuse to write anything invalid.",
                        "**Climate and light logic:** dew point (Magnus), an anti-fog PTC heater controller with hysteresis that switches off on any bad reading, and a local day/night decision.",
                        "**Static-reflector map:** learned only during an operator's calibration and applied only to echoes that are both at a learned position and stationary, so a person standing still is never hidden.",
                        "**Safe start:** the node refuses to start with an invalid or placeholder identity or duplicate radar pins, uses wall-clock time (SNTP) for timestamps, and announces `offline` through an MQTT last will."],
            "build": "```bash\ncmake -S tests -B build/host && cmake --build build/host\nbuild/host/test_core                                  # 77 checks, -Werror\nbuild/host/emit_samples | python tests/check_contract.py\nidf.py build                                          # firmware, needs ESP-IDF 5.x\n```\n\nThe host tests need any C++17 compiler (Linux, WSL, MSYS2). See the [hardware boundary](docs/HARDWARE_BOUNDARY.md).",
            "structure": "```text\nARMOR-RADAR/\n├── main/\n│   ├── app_main.cpp        firmware (needs ESP-IDF)\n│   └── core/               framer, telemetry_json, climate, static_map, node_id\n├── tests/                  test_core.cpp, emit_samples.cpp, check_contract.py\n├── Kconfig.projbuild, sdkconfig.defaults\n└── docs/HARDWARE_BOUNDARY.md\n```"},
        "es": {
            "tagline": "Firmware del nodo de campo y su núcleo probado en el ordenador",
            "honest": "**Madurez: scaffolding.** El núcleo independiente del hardware (77 comprobaciones) y el JSON del firmware (validado por ARMOR-COMMON) son reales. `main/app_main.cpp` **no se compila aquí** (necesita ESP-IDF 5.x y una placa), y el formato de trama del LD2450/LD2461 **no se decodifica a propósito**: debe salir del documento de protocolo del fabricante y de capturas UART reales, de modo que nunca se inventa una pista.",
            "bullets": ["**Delimitador que se resincroniza:** encuentra tramas en un flujo UART ruidoso por cabecera, longitud y cola, descarta un byte si no coincide y sigue. Su especificación para el radar real está sin configurar hasta añadir el documento del fabricante.",
                        "**Mensajes exactos al contrato:** el JSON de telemetría y salud sigue los esquemas publicados (15 pistas, 5 por sensor, rango de lux, patrón de identificador) y se niega a escribir algo inválido.",
                        "**Lógica de clima y luz:** punto de rocío (Magnus), un control del calefactor PTC antivaho con histéresis que se apaga ante cualquier lectura errónea, y una decisión día/noche local.",
                        "**Mapa de reflectores estáticos:** se aprende solo durante una calibración del operador y se aplica solo a ecos que están en una posición aprendida y quietos, de modo que una persona parada nunca se oculta.",
                        "**Arranque seguro:** el nodo se niega a arrancar con una identidad inválida o de ejemplo o con pines de radar duplicados, usa hora real (SNTP) en las marcas de tiempo y anuncia `offline` mediante un last will de MQTT."],
            "build": "```bash\ncmake -S tests -B build/host && cmake --build build/host\nbuild/host/test_core                                  # 77 comprobaciones, -Werror\nbuild/host/emit_samples | python tests/check_contract.py\nidf.py build                                          # firmware, necesita ESP-IDF 5.x\n```\n\nLos tests en el ordenador necesitan cualquier compilador C++17 (Linux, WSL, MSYS2). Véase el [límite de hardware](docs/HARDWARE_BOUNDARY.md).",
            "structure": "```text\nARMOR-RADAR/\n├── main/\n│   ├── app_main.cpp        firmware (necesita ESP-IDF)\n│   └── core/               framer, telemetry_json, climate, static_map, node_id\n├── tests/                  test_core.cpp, emit_samples.cpp, check_contract.py\n├── Kconfig.projbuild, sdkconfig.defaults\n└── docs/HARDWARE_BOUNDARY.md\n```"},
    },
    "ARMOR-ANDROID-CONTROL": {
        "emoji": "📱", "badges": [("Language", "Kotlin", "7f52ff"), ("UI", "Jetpack%20Compose", "4285f4"), ("Maturity", "functional%20baseline", "00E5FF")],
        "en": {
            "tagline": "Mobile operator client for ARMOR-SERVER",
            "honest": "The endpoint-safety rules have unit tests and the app builds. It has **not been run on a phone against the server**, and it deliberately cannot arm or disarm the system.",
            "bullets": ["**Sign in with the server's own login:** IP, port, user and password; the password creates an HttpOnly session and is never stored on the phone.",
                        "**Camera monitor:** 1 to 16 tiles, a maximized view, live MJPEG that keeps the picture ratio, a bounded PTZ pad, snapshots and recordings.",
                        "**Evidence library** and the perimeter and node state.",
                        "**Careful with the password:** plain HTTP is allowed only to a private-LAN or loopback IPv4 *literal*. A host name that merely starts like a private address (`10.attacker.example`) or an address with a leading zero (some resolvers read `010.0.0.1` as the public `8.0.0.1`) is refused.",
                        "The Hydra look: near-black surfaces, a cyan accent, amber for attention."],
            "build": "```powershell\n.\\gradlew.bat testDebugUnitTest assembleDebug\nadb install -r app\\build\\outputs\\apk\\debug\\app-debug.apk\n```\n\nThe debug APK is not signed for distribution. See the [client boundary](docs/CLIENT_BOUNDARY.md).",
            "structure": "```text\nARMOR-ANDROID-CONTROL/\n├── app/src/main/java/es/electrohobby3d/armor/\n│   ├── ArmorActivity.kt, ArmorTheme.kt, ArmorViewModel.kt, ServerEndpoint.kt, MjpegFeed.kt\n│   ├── network/   model/\n└── app/src/test/   endpoint-safety tests\n```"},
        "es": {
            "tagline": "Cliente móvil de operador para ARMOR-SERVER",
            "honest": "Las reglas de seguridad de la dirección tienen tests unitarios y la app compila. **No se ha ejecutado en un teléfono contra el servidor**, y a propósito no puede armar ni desarmar el sistema.",
            "bullets": ["**Acceso con el login del propio servidor:** IP, puerto, usuario y contraseña; la contraseña crea una sesión HttpOnly y nunca se guarda en el teléfono.",
                        "**Monitor de cámaras:** de 1 a 16 mosaicos, vista ampliada, MJPEG en directo que respeta la proporción, mando PTZ acotado, capturas y grabaciones.",
                        "**Biblioteca de evidencias** y estado del perímetro y de los nodos.",
                        "**Cuidado con la contraseña:** el HTTP plano solo se permite hacia un *literal* IPv4 de LAN privada o loopback. Se rechaza un nombre de host que solo empieza como una dirección privada (`10.atacante.ejemplo`) o una dirección con cero a la izquierda (algunos resolvedores leen `010.0.0.1` como la pública `8.0.0.1`).",
                        "El aspecto Hydra: superficies casi negras, acento cian, ámbar para lo que requiere atención."],
            "build": "```powershell\n.\\gradlew.bat testDebugUnitTest assembleDebug\nadb install -r app\\build\\outputs\\apk\\debug\\app-debug.apk\n```\n\nEl APK de depuración no está firmado para distribución. Véase el [límite del cliente](docs/CLIENT_BOUNDARY.md).",
            "structure": "```text\nARMOR-ANDROID-CONTROL/\n├── app/src/main/java/es/electrohobby3d/armor/\n│   ├── ArmorActivity.kt, ArmorTheme.kt, ArmorViewModel.kt, ServerEndpoint.kt, MjpegFeed.kt\n│   ├── network/   model/\n└── app/src/test/   tests de seguridad de la dirección\n```"},
    },
    "ARMOR-HARDWARE": {
        "emoji": "🧱", "badges": [("CAD", "OpenSCAD", "f9d72c"), ("EDA", "KiCad", "314cb0"), ("Maturity", "mechanical%20baseline", "FFB020")],
        "en": {
            "tagline": "Enclosures, electronics and the bench acceptance matrix",
            "honest": "The enclosure is a **printable mechanical starting point, not an IP, RF or thermal rating.** Nothing has been measured on a prototype; every row of the [bench acceptance matrix](docs/BENCH_ACCEPTANCE.md) is *not tested*.",
            "bullets": ["**The real design is `CAD/CARCASA_SENSORES.scad`** (with STL, 3MF and AMF exports): a 90-degree corner base with a visor, roof and floor, retaining steps, a sliding 2 mm front cover and side flaps, all driven by named parameters. `scad/node_enclosure.scad` is only a placeholder box.",
                        "**Reserved volumes** for three radar modules, the ESP32-S3-ETH-PoE board, the sensor window, a cable gland, the PoE magnetics and the PTC heater. No metallic, conductive or carbon-loaded material in front of a 24 GHz aperture without measured attenuation.",
                        "**Bench acceptance matrix:** the radio, environment, power, network and camera checks with a method and a proposed pass criterion each, and a camera compatibility table to fill in.",
                        "Before fabrication, record exact board outlines, connectors, screw positions, antenna keep-outs, the thermal path and the ingress target ([design inputs](docs/DESIGN_INPUTS.md))."],
            "build": "```powershell\nopenscad -o build/CARCASA_SENSORES.stl CAD/CARCASA_SENSORES.scad\n```\n\nSee the [validation boundary](docs/VALIDATION.md). The intended hardware licence is CERN-OHL-S-2.0; add its full text before releasing the designs.",
            "structure": "```text\nARMOR-HARDWARE/\n├── CAD/     CARCASA_SENSORES.scad (+ stl, 3mf, amf)\n├── scad/    node_enclosure.scad (placeholder)\n├── EDA/     KiCad (empty)\n└── docs/    DESIGN_INPUTS, VALIDATION, BENCH_ACCEPTANCE\n```"},
        "es": {
            "tagline": "Carcasas, electrónica y la matriz de aceptación de banco",
            "honest": "La carcasa es un **punto de partida mecánico imprimible, no una clasificación IP, RF ni térmica.** No se ha medido nada en un prototipo; cada fila de la [matriz de aceptación de banco](docs/BENCH_ACCEPTANCE.md) está *sin probar*.",
            "bullets": ["**El diseño real es `CAD/CARCASA_SENSORES.scad`** (con exportaciones STL, 3MF y AMF): una base de esquina de 90 grados con visera, techo y suelo, escalones de retención, una tapa frontal deslizante de 2 mm y solapas laterales, todo gobernado por parámetros con nombre. `scad/node_enclosure.scad` es solo una caja de ejemplo.",
                        "**Volúmenes reservados** para tres módulos de radar, la placa ESP32-S3-ETH-PoE, la ventana del sensor, un prensaestopas, la magnética PoE y el calefactor PTC. Ningún material metálico, conductor o cargado de carbono delante de una apertura de 24 GHz sin atenuación medida.",
                        "**Matriz de aceptación de banco:** las comprobaciones de radio, entorno, alimentación, red y cámaras con un método y un criterio propuesto cada una, y una tabla de compatibilidad de cámaras por rellenar.",
                        "Antes de fabricar, registrar contornos exactos de placas, conectores, posición de tornillos, zonas libres de antena, el camino térmico y el objetivo de estanqueidad ([entradas de diseño](docs/DESIGN_INPUTS.md))."],
            "build": "```powershell\nopenscad -o build/CARCASA_SENSORES.stl CAD/CARCASA_SENSORES.scad\n```\n\nVéase el [límite de validación](docs/VALIDATION.md). La licencia de hardware prevista es CERN-OHL-S-2.0; añade su texto completo antes de publicar los diseños.",
            "structure": "```text\nARMOR-HARDWARE/\n├── CAD/     CARCASA_SENSORES.scad (+ stl, 3mf, amf)\n├── scad/    node_enclosure.scad (ejemplo)\n├── EDA/     KiCad (vacío)\n└── docs/    DESIGN_INPUTS, VALIDATION, BENCH_ACCEPTANCE\n```"},
    },
    "ARMOR-DEVOPS": {
        "emoji": "🚀", "badges": [("Deploy", "Docker%20Compose", "2496ed"), ("Bench", "systemd", "FFB020"), ("Maturity", "functional", "00E5FF")],
        "en": {
            "tagline": "Deployment topology and the isolated CM5 test bench",
            "honest": "The CM5 bench installer has been run on a real CM5 that hosts other software, which stayed healthy. The Docker Compose topology is **validated with `docker compose config` but has not been run**.",
            "bullets": ["**CM5 test bench:** `scripts/deploy_cm5.sh` builds in a clean copy, sends one archive and runs `scripts/install_cm5.sh`, which creates its own user, its own directory and two systemd units on their own ports, with resource limits, and never touches another project ([details](docs/CM5_TEST_BENCH.md)).",
                        "**Compose topology:** a non-anonymous Mosquitto broker with one identity per node, the server, and Studio behind an nginx that proxies `/api/`; only Studio is published, on loopback. Hardened containers, an internal core network and named volumes for state.",
                        "**Secrets:** `scripts/generate_secrets.sh` creates random secrets and prints none; `scripts/check-required-env.sh` refuses missing, placeholder, short or repeated values."],
            "build": "```bash\nscripts/generate_secrets.sh          # .env and secrets/ (Git-ignored)\nscripts/check-required-env.sh\ndocker compose config --quiet && docker compose up --build\nscripts/deploy_cm5.sh --host <cm5> --user <user> --key <key> --apply   # the test bench\n```\n\nSee the [deployment boundary](docs/DEPLOYMENT_BOUNDARY.md).",
            "structure": "```text\nARMOR-DEVOPS/\n├── docker-compose.yml, .env.example, mosquitto/\n├── scripts/   deploy_cm5.sh, install_cm5.sh, generate_secrets.sh, check-required-env.sh, validate-compose.sh\n└── docs/      DEPLOYMENT_BOUNDARY.md, CM5_TEST_BENCH.md\n```"},
        "es": {
            "tagline": "Topología de despliegue y el banco de pruebas aislado en CM5",
            "honest": "El instalador del banco CM5 se ha ejecutado en una CM5 real que aloja otro software, y este siguió sano. La topología de Docker Compose está **validada con `docker compose config` pero no se ha ejecutado**.",
            "bullets": ["**Banco de pruebas CM5:** `scripts/deploy_cm5.sh` compila en una copia limpia, envía un archivo y ejecuta `scripts/install_cm5.sh`, que crea su propio usuario, su propio directorio y dos unidades systemd en puertos propios, con límites de recursos, y nunca toca otro proyecto ([detalles](docs/CM5_TEST_BENCH.md)).",
                        "**Topología Compose:** un broker Mosquitto no anónimo con una identidad por nodo, el servidor y Studio tras un nginx que hace de proxy de `/api/`; solo se publica Studio, en loopback. Contenedores endurecidos, red interna y volúmenes con nombre para el estado.",
                        "**Secretos:** `scripts/generate_secrets.sh` crea secretos aleatorios sin imprimir ninguno; `scripts/check-required-env.sh` rechaza valores ausentes, de ejemplo, cortos o repetidos."],
            "build": "```bash\nscripts/generate_secrets.sh          # .env y secrets/ (ignorados por Git)\nscripts/check-required-env.sh\ndocker compose config --quiet && docker compose up --build\nscripts/deploy_cm5.sh --host <cm5> --user <usuario> --key <clave> --apply   # el banco de pruebas\n```\n\nVéase el [límite de despliegue](docs/DEPLOYMENT_BOUNDARY.md).",
            "structure": "```text\nARMOR-DEVOPS/\n├── docker-compose.yml, .env.example, mosquitto/\n├── scripts/   deploy_cm5.sh, install_cm5.sh, generate_secrets.sh, check-required-env.sh, validate-compose.sh\n└── docs/      DEPLOYMENT_BOUNDARY.md, CM5_TEST_BENCH.md\n```"},
    },
}


def render(name: str, language: str) -> str:
    repo, text, labels = REPOS[name], REPOS[name][language], LABELS[language]
    badges = "\n".join(f'  <img src="https://img.shields.io/badge/{label}-{value}-{color}.svg" alt="{label}">' for label, value, color in repo["badges"])
    bullets = "\n".join(f"* {item}" for item in text["bullets"])
    return f"""<p align="center">
  <img src="images/ARMOR_BANNER.svg" alt="{name} banner" width="100%">
</p>

# {repo['emoji']} {name}

<p align="center">{labels['lang']}</p>

### {text['tagline']}

<p align="center">
  <img src="https://img.shields.io/badge/License-GPL%203.0-blue.svg" alt="GPL 3.0">
{badges}
</p>

---

**{labels['honesty']}:** {text['honest']}

---

## 1. 🛠️ {labels['overview']}

{bullets}

---

## 2. 🔧 {labels['build']}

{text['build']}

---

## 📂 {labels['structure']}

{text['structure']}

---

## 👤 {labels['author']}

**JuanenRac (Electro Hobby 3D)** · electrohobby3d@gmail.com

## 📜 {labels['license']}

{labels['license_text']}
"""


def outputs() -> dict[Path, str]:
    files: dict[Path, str] = {}
    for name in REPOS:
        files[ROOT / name / "README.md"] = render(name, "en")
        files[ROOT / name / "README_spa.md"] = render(name, "es")
    return files


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    stale = []
    for path, content in outputs().items():
        current = path.read_text(encoding="utf-8") if path.exists() else None
        if current == content:
            continue
        stale.append(str(path))
        if not args.check:
            path.write_text(content, encoding="utf-8", newline="\n")
    if args.check and stale:
        print("READMEs out of date:", *stale, sep="\n  ", file=sys.stderr)
        return 1
    print("READMEs current" if args.check else f"READMEs written: {len(outputs())}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
