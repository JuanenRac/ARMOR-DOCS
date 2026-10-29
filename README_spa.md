<p align="center">
  <img src="images/ARMOR_BANNER.svg" alt="Banner de ARMOR-DOCS" width="100%">
</p>

# 📚 ARMOR-DOCS

<p align="center">
  <a href="README.md">🇺🇸 English</a> |
  🇪🇸 <b>Español</b> |
  <a href="README_fra.md">🇫🇷 Français</a> |
  <a href="README_ita.md">🇮🇹 Italiano</a> |
  <a href="README_deu.md">🇩🇪 Deutsch</a> |
  <a href="README_zho.md">🇨🇳 简体中文</a> |
  <a href="README_jpn.md">🇯🇵 日本語</a> |
  <a href="README_por.md">🇵🇹 Português</a>
</p>

### Arquitectura canónica, base de seguridad y la verdad sobre lo que está probado

<p align="center">
  <img src="https://img.shields.io/badge/License-GPL%203.0--or--later-blue.svg" alt="GPL 3.0 o posterior">
  <img src="https://img.shields.io/badge/Format-Markdown-083fa1.svg" alt="Format">
  <img src="https://img.shields.io/badge/Languages-8-00E5FF.svg" alt="Idiomas">
  <img src="https://img.shields.io/badge/Tests-199%20passing-2ea44f.svg" alt="Pruebas">
  <img src="https://img.shields.io/badge/Version-0.8.1.3-0f6cbd.svg" alt="Versión">
  <img src="https://img.shields.io/badge/Maturity-established-2EA44F.svg" alt="Madurez">
</p>

---

**Comprobación de honestidad - qué funciona hoy:** Este repositorio documenta interfaces y procedimientos que se han validado, y dice claramente lo que no. Lee la [matriz de capacidades](docs/CAPABILITY_MATRIX.md) antes de creer que una función está "hecha": dice de cada una si solo se simuló, se probó en un ordenador o se verificó en hardware real. Los README de los diecinueve repositorios se escriben desde una sola fuente (`tools/readme_src/`) en ocho idiomas, con la versión y la madurez de cada uno leídas de su propio manifiesto, de modo que no pueden decir algo distinto del proyecto.

---

## 📋 De un vistazo

| | |
|---|---|
| Versión | `0.8.1.3` |
| Madurez | Establecido |
| Función | Centro de documentación: arquitectura, base de seguridad, matriz de capacidades y las herramientas que escriben los README, el catálogo y los banners |
| Tecnología | Python 3.11+ (herramientas, biblioteca estándar), Markdown |
| Pruebas | 199 (`python -m unittest discover -s tests`, cerca de un minuto) |
| Interfaces | `make_readmes.py`, `make_catalog.py`, `make_brand.py`, `publication_check.py`, `clean_history.py`, `sync_ci_tools.py`, `check_all.sh` |
| Funciona en | Cualquier ordenador con Python; los repositorios de la familia junto a este |
| En hardware real | No aplica: es documentación; registra lo que los demás repositorios han corrido en hardware real |
| Licencia | GPL-3.0-or-later |

**Ir a:** [Resumen](#-resumen) · [Arquitectura](#-arquitectura) · [Seguridad](#-seguridad-y-protección) · [Interfaces](#-interfaces) · [Inicio rápido](#-inicio-rápido) · [Pruebas](#-pruebas) · [Problemas](#-resolución-de-problemas) · [Estructura](#-estructura-del-repositorio) · [Relacionados](#-proyectos-relacionados)

## 🚦 Estado del proyecto

Cada línea es una parte de este repositorio y la luz dice hasta dónde llega hoy. Está escrito con lo que el repositorio puede demostrar (pruebas, compilaciones, ejecuciones), no con lo que está planeado.

🟢 Hecho y verificado · 🟡 Funciona, con límites conocidos · 🟠 Parcial o sin verificar todavía · 🔴 No hecho o no funciona

| Área | Estado | Qué significa aquí |
|---|---|---|
| Software | 🟢 | Los generadores de READMEs, banners, catálogo y matriz de capacidades, y las herramientas de CI copiadas a cada repositorio, funcionan y están probados. |
| Pruebas | 🟢 | Pasan las 199 pruebas de las herramientas (`python -m unittest discover -s tests`): la comprobación de publicación, el limpiador de historial, los generadores de README, catálogo y marca, la copia de las herramientas de CI y la herramienta del flujo compartido. |
| Comprobaciones automáticas | 🟢 | Cada push comprueba que los READMEs, los banners y el catálogo estén al día y que cada repositorio del registro tenga su tabla de estado. |
| Integración | 🟢 | Los READMEs de todos los repositorios se escriben desde una sola fuente, con la versión y la madurez de cada uno leídas de su propio manifiesto. |
| Documentación | 🟢 | La matriz de capacidades dice, para cada función, si solo se simuló, se probó en un ordenador o se verificó en hardware real; los ocho idiomas y el historial de cambios están al día. |

## 🎯 Resumen

<p align="center">
  <img src="images/ARMOR_FAMILY.svg" alt="A.R.M.O.R. family" width="100%">
</p>

* [Matriz de capacidades](docs/CAPABILITY_MATRIX.md): de cada capacidad, ¿está simulada, probada en un ordenador o verificada en hardware?
* [Arquitectura](docs/ARCHITECTURE.md): redes, límites de confianza, tiempo y orden.
* [Base de seguridad](docs/SECURITY_BASELINE.md): el diseño de VLAN, lo que el código hace cumplir y lo que aún falta; y el [modelo de amenazas](docs/THREAT_MODEL.md).
* [Catálogo de proyectos](docs/PROJECT_CATALOG.md): los diecinueve repositorios, sus versiones y cómo dependen unos de otros.
* [Interfaces](docs/INTERFACES.md): quién produce y consume cada interfaz y dónde se confía en ella.
* [Primera rebanada vertical](docs/FIRST_VERTICAL_SLICE.md): qué demuestra la prueba del simulador a la consola y qué no.
* **Herramientas:** `make_readmes.py` escribe el README de cada repositorio en los ocho idiomas desde `readme_src/`, `make_catalog.py` escribe las versiones del catálogo, `make_brand.py` su banner e icono, `publication_check.py` busca cualquier cosa privada antes de una publicación, `clean_history.py` hace una copia publicable de un repositorio y `sync_ci_tools.py` mantiene iguales las comprobaciones de CI de la familia.

## 🧩 Papel en A.R.M.O.R.

ARMOR-DOCS es la memoria de la familia: es donde viven la arquitectura, la base de seguridad y la matriz de capacidades, y el lugar que dice, de cada repositorio, qué ha corrido de verdad en hardware. También guarda la herramienta que escribe los README de los diecinueve repositorios desde una sola fuente, para que los ocho idiomas no se separen.

| Habla con | Cómo | Para qué |
|---|---|---|
| Cada repositorio de la familia | su `armor.project.json` y sus ficheros README | las herramientas leen la versión y la madurez y escriben el README, el banner y las copias de CI |
| ARMOR-COMMON | `registry/repositories.json` | la lista única de repositorios de la familia, leída por `registry.py` |
| Quien publica | `publication_check.py`  `clean_history.py` | lo que se filtraría y una copia de un solo commit que se puede publicar |

## 🏛️ Arquitectura

<p align="center">
  <img src="images/architecture.svg" alt="ARMOR-DOCS architecture: what the tools read, the tools themselves and what they write in every repository" width="100%">
</p>

## 🔒 Seguridad y protección

| Amenaza | Defensa |
|---|---|
| Publicar algo privado | `publication_check.py` solo lee git (ficheros versionados e historial, nunca los ignorados) y nunca imprime el secreto. BLOCK: una clave privada, una IP pública, un correo personal, un `secrets/` o `.env` versionado, un commit con coautor o cola de IA, un autor de commit distinto del del proyecto; REVIEW: una línea que parece una contraseña o token literal; sale con 1 ante cualquier BLOCK |
| Un historial con restos | `clean_history.py` hace una copia publicable de un repositorio con un solo commit hecho por el autor del proyecto |
| Afirmar más de lo probado | `docs/CAPABILITY_MATRIX.md` tiene tres niveles (Simulated, Local, Verified) más None, Absent y Local-not-activated; solo las filas Verified han tocado hardware (el banco de la CM5 en uso diario) |
| Un README que dice algo distinto del proyecto | La versión y la madurez de cada README se leen de su propio manifiesto; cada push comprueba que los README, los banners y el catálogo están al día y que cada repositorio del registro tiene su tabla de estado |

Los documentos de seguridad de la familia son [docs/SECURITY_BASELINE.md](docs/SECURITY_BASELINE.md) (el diseño de VLAN, lo que el código hace cumplir y lo que aún falta) y [docs/THREAT_MODEL.md](docs/THREAT_MODEL.md). Nada de esto prueba la ausencia de un secreto.

## 🔌 Interfaces

| Ruta | Autenticación | Qué hace |
|---|---|---|
| `python tools/make_readmes.py [--check]` | - | escribe el README de cada repositorio en ocho idiomas desde `tools/readme_src/`; `--check` falla si alguno está desfasado. Reescribe todos los ficheros: cambia la fuente, nunca los README |
| `python tools/make_catalog.py [--check]`  `make_brand.py [--check]` | - | las versiones y madurez de `docs/PROJECT_CATALOG.md`, y los banners e iconos |
| `python tools/publication_check.py [REPO] [--no-history] [--ref=BRANCH]` | - | lo que se filtraría si se publicaran los repositorios; sale con 1 ante BLOCK |
| `python tools/clean_history.py` | - | una copia publicable de un repositorio con un solo commit |
| `python tools/sync_ci_tools.py [--check]` | - | copia las comprobaciones de CI y el lanzador en cada repositorio; `--check` falla si una copia se ha desviado |
| `bash tools/check_all.sh [--android] [--compose]` | - | las pruebas de cada repositorio de una vez; una comprobación sin su herramienta es SKIP, nunca PASS |

La fuente de cada README es `tools/readme_src/repos/<REPOSITORIO>.py` (los datos que no dependen del idioma y las palabras de los ocho idiomas), con `ui.py` para las palabras alrededor de cada README y `shots.py` para las capturas. `tools/registry.py` lee la lista de repositorios de ARMOR-COMMON. Mira también [docs/INTERFACES.md](docs/INTERFACES.md) y [docs/SETUP_CODE.md](docs/SETUP_CODE.md).

## 🚀 Inicio rápido

**Requisitos:** Python 3.11+ para las herramientas (solo biblioteca estándar); los repositorios de la familia junto a este para las comprobaciones que los leen.

```bash
python tools/make_readmes.py --check  # los README (8 idiomas) están al día
python tools/make_catalog.py --check  # las versiones y madurez del catálogo están al día
python tools/make_brand.py --check    # los banners e iconos están al día
python tools/publication_check.py     # nada privado saldría con una publicación
bash tools/check_all.sh               # las pruebas de cada repositorio, de una vez
python -m unittest discover -s tests  # 199 pruebas de estas herramientas; no necesitan otro repositorio
```

## 🧪 Pruebas

| Área | Qué cubre |
|---|---|
| El generador de README | los ocho idiomas y los apartados de cada repositorio |
| Catálogo y marca | `test_make_catalog_and_brand.py`, `test_repository_registry.py` |
| Publicación | qué es BLOCK y REVIEW, y la copia de un commit |
| Herramientas de CI y lanzador | `test_ci_validate.py`, `test_sync_ci_tools.py`, `test_project_tool.py`, `test_check_all_script.py` |

GitHub Actions ejecuta la base de A.R.M.O.R. en cada push y pull request: la validación del manifiesto, la versión, el registro de cambios y la paridad de los README, y luego la compilación y las pruebas del propio proyecto.

## 🏗️ Compilación y publicación

No hay nada que compilar. La versión vive en `armor.project.json` y en la insignia del README (leída del manifiesto); cada versión tiene su entrada en [CHANGELOG.md](CHANGELOG.md). Las versiones se publican en GitHub.

## 🩺 Resolución de problemas

| Ves | Porque | Haz |
|---|---|---|
| `READMEs out of date:` + a list | cambió una fuente de `tools/readme_src/` o un manifiesto y no se volvieron a escribir los README | ejecuta `python tools/make_readmes.py`, mira qué cambió en cada repositorio y haz commit allí |
| `Status tables incomplete:` | un repositorio del registro tiene una tabla de estado sin las filas o colores esperados | completa `FACTS["status"]` y las notas en su fuente |
| Una comprobación dice SKIP | falta su herramienta o el repositorio junto a este; una comprobación sin su herramienta nunca es PASS | instala la herramienta o clona el repositorio junto a este |
| `publication_check.py` BLOCK | se encontró algo que no debe publicarse (muestra el fichero, la línea y el tipo, nunca el valor) | quítalo y usa `clean_history.py` si está en el historial |

## 📂 Estructura del repositorio

<p align="center">
  <img src="images/repository-structure.svg" alt="Repository structure of ARMOR-DOCS" width="100%">
</p>

<details>
<summary>Versión en texto del árbol</summary>

```text
ARMOR-DOCS/
├── tools/
│   ├── make_readmes.py                          los README, desde una fuente, en ocho idiomas
│   ├── readme_src/                              los datos y las palabras de cada repositorio
│   ├── make_catalog.py make_brand.py            el catálogo; los banners e iconos
│   ├── brand_banner.py registry.py              el dibujo del banner; la lista de ARMOR-COMMON
│   ├── publication_check.py                     nada privado sale con una publicación
│   ├── clean_history.py sync_ci_tools.py        una copia publicable; comprobaciones de CI iguales
│   ├── check_all.sh                             las pruebas de cada repositorio de una vez
│   ├── armor_ci_validate.py                     la comprobación de CI que lleva cada repositorio
│   ├── armor_project_tool.py pretty_run.py      el lanzador y su panel en vivo
│   ├── make_architecture.py make_structure.py   las dos imágenes de los README
│   └── universal_readme_check.py                la comprobación del formato de los README
├── docs/                                        CAPABILITY_MATRIX, ARCHITECTURE, SECURITY_BASELINE, THREAT_MODEL, PROJECT_CATALOG, INTERFACES, FIRST_VERTICAL_SLICE, SETUP_CODE
├── tests/                                       las pruebas de estas herramientas
├── brand/                                       el emblema
├── images/                                      banner, icono, la imagen de la familia y las imágenes de este README
├── .github/                                     flujo de CI, aviso al panel, plantillas de incidencias y pull requests
├── armor.project.json                           manifiesto: versión, función, madurez
├── CHANGELOG.md                                 qué cambió en cada versión
├── run.sh run.bat                               arrancar, flujo compartido
├── build.sh build.bat                           construir y probar, flujo compartido
├── build-test.sh build-test.bat                 construir, probar y empaquetar
├── test.sh test.bat                             solo las pruebas, nunca la versión
└── SECURITY.md SUPPORT.md CONTRIBUTING.md CODE_OF_CONDUCT.md LICENSE
```

</details>

## 🗺️ Hoja de ruta y límites conocidos

**Límites conocidos hoy**

* La matriz de capacidades es la verdad sobre lo que ha corrido: hasta que una fila diga Verified, no ha tocado hardware real.
* Solo el nodo radar y el banco de la CM5 han corrido en hardware real.
* Sin revisión de seguridad independiente.

**Lo siguiente**

* Pasar filas de la matriz a Verified a medida que los otros nodos corran en sus placas.

## 🌍 Idiomas

El README y los textos existen en inglés, español, francés, italiano, alemán, chino, japonés y portugués de Portugal.

## 🔗 Proyectos relacionados

**A.R.M.O.R.** (Autonomous Radar & Multimodal Observation Range) es un sistema de seguridad perimetral hecho de repositorios independientes. Cada uno tiene su propia versión, sus propias pruebas y su propio README; esta es la familia:

* **[ARMOR-COMMON](https://github.com/JuanenRac/ARMOR-COMMON)** - Contratos de mensajes, validadores, vectores de conformidad y tipos generados
* **[ARMOR-NODE-RADAR](https://github.com/JuanenRac/ARMOR-NODE-RADAR)** - Firmware de nodo de campo para ESP32-S3 con tres radares y su propio panel web
* **[ARMOR-NODE-SOLAR](https://github.com/JuanenRac/ARMOR-NODE-SOLAR)** - Protocolos de inversores y baterías solares y los mensajes de un nodo pasarela
* **[ARMOR-NODE-ELECTRICAL](https://github.com/JuanenRac/ARMOR-NODE-ELECTRICAL)** - Nodo eléctrico: medidores, el mensaje de las lecturas de la red y las reglas de maniobra
* **[ARMOR-NODE-ALARM](https://github.com/JuanenRac/ARMOR-NODE-ALARM)** - Nodo y panel de alarma: zonas, armado, retardos, sirena y PIN, con el servidor o sin él
* **[ARMOR-NODE-HMI](https://github.com/JuanenRac/ARMOR-NODE-HMI)** - Panel táctil: el estado del sistema en una pantalla de pared, armar y reconocer, y el hogar del asistente de voz
* **[ARMOR-NETWORK](https://github.com/JuanenRac/ARMOR-NETWORK)** - La red local: sus dispositivos, internet y lo que cambia
* **[ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER)** - Coordinador central: telemetría, alarmas, dispositivos, lecturas solares y cámaras
* **[ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO)** - Consola web: cámaras, radar, alarmas, energía solar y el diseñador 2D/3D del emplazamiento
* **[ARMOR-ANDROID-CONTROL](https://github.com/JuanenRac/ARMOR-ANDROID-CONTROL)** - Cliente de operador Android con radar 2D/3D en vivo
* **[ARMOR-IOS-CONTROL](https://github.com/JuanenRac/ARMOR-IOS-CONTROL)** - Cliente de operador para iPhone
* **[ARMOR-SERVER-AI](https://github.com/JuanenRac/ARMOR-SERVER-AI)** - Política de inferencia visual que explica sus decisiones y nunca actúa
* **[ARMOR-VISION](https://github.com/JuanenRac/ARMOR-VISION)** - Zonas de cámara, máscaras y reglas de detección para la Jetson Orin NX
* **[ARMOR-VOICE-AI](https://github.com/JuanenRac/ARMOR-VOICE-AI)** - Intenciones de voz sin conexión con una confirmación que no se puede falsificar
* **[ARMOR-HARDWARE](https://github.com/JuanenRac/ARMOR-HARDWARE)** - Cajas, electrónica y la matriz de aceptación en banco
* **[ARMOR-DEVOPS](https://github.com/JuanenRac/ARMOR-DEVOPS)** - Despliegue, el banco de pruebas de la CM5, copias de seguridad y TLS
* **[ARMOR-SIMULATOR](https://github.com/JuanenRac/ARMOR-SIMULATOR)** - Simulador de telemetría sin conexión con fallos repetibles
* **[ARMOR-UPDATER](https://github.com/JuanenRac/ARMOR-UPDATER)** - Detecta, instala y actualiza los repositorios del propio ecosistema
* **ARMOR-DOCS** (este repositorio) - Arquitectura, base de seguridad y la matriz de capacidades

## 📚 Documentación

* [ARCHITECTURE](docs/ARCHITECTURE.md): redes, límites de confianza, tiempo y orden
* [SECURITY_BASELINE](docs/SECURITY_BASELINE.md): el diseño de VLAN, lo que el código hace cumplir y lo que falta
* [THREAT_MODEL](docs/THREAT_MODEL.md): de qué se defiende y de qué no
* [INTERFACES](docs/INTERFACES.md): quién produce y consume cada interfaz y dónde se confía en ella
* [FIRST_VERTICAL_SLICE](docs/FIRST_VERTICAL_SLICE.md): lo que prueba y lo que no prueba el ensayo del simulador a la consola
* [SETUP_CODE](docs/SETUP_CODE.md): el código de configuración de los nodos
* [Matriz de capacidades: qué está demostrado y qué no](docs/CAPABILITY_MATRIX.md)
* [Catálogo de proyectos: versiones y cómo dependen unos repositorios de otros](docs/PROJECT_CATALOG.md)
* [Registro de cambios de este repositorio](CHANGELOG.md)

## 🤝 Contribuir y comunidad

* Antes de un pull request ejecuta `python -I tools/armor_ci_validate.py` y las pruebas: ambos deben pasar. Mira [CONTRIBUTING.md](CONTRIBUTING.md) y el [código de conducta](CODE_OF_CONDUCT.md).
* El README existe en ocho idiomas y se genera desde las fuentes de ARMOR-DOCS: un cambio de texto se hace allí.
* Un cambio en un mensaje entre componentes empieza en ARMOR-COMMON.
* No describas como funcionando en una placa lo que solo se ha compilado.
* Informa de una vulnerabilidad en privado: [SECURITY.md](SECURITY.md). Preguntas, ideas e informes: electrohobby3d@gmail.com ([SUPPORT.md](SUPPORT.md)).

## 👤 AUTOR

**JuanenRac (Electro Hobby 3D)** · electrohobby3d@gmail.com

## 📜 LICENCIA

GPL-3.0-or-later - véase [LICENSE](LICENSE).
