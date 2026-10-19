<p align="center">
  <img src="images/ARMOR_BANNER.svg" alt="ARMOR-DOCS banner" width="100%">
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
  <img src="https://img.shields.io/badge/License-GPL%203.0-blue.svg" alt="GPL 3.0">
  <img src="https://img.shields.io/badge/Format-Markdown-083fa1.svg" alt="Format">
  <img src="https://img.shields.io/badge/Languages-8-00E5FF.svg" alt="Languages">
  <img src="https://img.shields.io/badge/Version-0.8.0.6-0f6cbd.svg" alt="Version">
  <img src="https://img.shields.io/badge/Maturity-established-2EA44F.svg" alt="Maturity">
</p>

---

**Comprobación de honestidad - qué funciona hoy:** Este repositorio documenta interfaces y procedimientos que se han validado, y dice claramente lo que no. Lee la [matriz de capacidades](docs/CAPABILITY_MATRIX.md) antes de creer que una función está "hecha": dice de cada una si solo se simuló, se probó en un ordenador o se verificó en hardware real. Los README de los dieciocho repositorios se escriben desde una sola fuente (`tools/readme_src/`) en ocho idiomas, con la versión y la madurez de cada uno leídas de su propio manifiesto, de modo que no pueden decir algo distinto del proyecto.

---

## 📋 De un vistazo

| | |
|---|---|
| Versión | `0.8.0.6` |
| Madurez | Establecido |
| Tecnología | Markdown / Mermaid |
| En hardware real | No aplica: es documentación; registra lo que los demás repositorios han corrido en hardware real |

## 🎯 Descripción general

<p align="center">
  <img src="images/ARMOR_FAMILY.svg" alt="A.R.M.O.R. family" width="100%">
</p>

* [Matriz de capacidades](docs/CAPABILITY_MATRIX.md): de cada capacidad, ¿está simulada, probada en un ordenador o verificada en hardware?
* [Arquitectura](docs/ARCHITECTURE.md): redes, límites de confianza, tiempo y orden.
* [Base de seguridad](docs/SECURITY_BASELINE.md): el diseño de VLAN, lo que el código hace cumplir y lo que aún falta; y el [modelo de amenazas](docs/THREAT_MODEL.md).
* [Catálogo de proyectos](docs/PROJECT_CATALOG.md): los dieciocho repositorios, sus versiones y cómo dependen unos de otros.
* [Interfaces](docs/INTERFACES.md): quién produce y consume cada interfaz y dónde se confía en ella.
* [Primera rebanada vertical](docs/FIRST_VERTICAL_SLICE.md): qué demuestra la prueba del simulador a la consola y qué no.
* **Herramientas:** `make_readmes.py` escribe el README de cada repositorio en los ocho idiomas desde `readme_src/`, `make_catalog.py` escribe las versiones del catálogo, `make_brand.py` su banner e icono, `publication_check.py` busca cualquier cosa privada antes de una publicación, `clean_history.py` hace una copia publicable de un repositorio y `sync_ci_tools.py` mantiene iguales las comprobaciones de CI de la familia.

## 🧩 Papel en A.R.M.O.R.

ARMOR-DOCS es la memoria de la familia: es donde viven la arquitectura, la base de seguridad y la matriz de capacidades, y el lugar que dice, de cada repositorio, qué ha corrido de verdad en hardware. También guarda la herramienta que escribe los README de los dieciocho repositorios desde una sola fuente, para que los ocho idiomas no se separen.

## 📂 Estructura del repositorio

```text
ARMOR-DOCS/
├── docs/     CAPABILITY_MATRIX, ARCHITECTURE, SECURITY_BASELINE, PROJECT_CATALOG, INTERFACES, THREAT_MODEL, FIRST_VERTICAL_SLICE
├── tools/    make_readmes.py (+ readme_src/: the facts and the words of every repository in eight languages), make_catalog.py, make_brand.py, publication_check.py, clean_history.py, sync_ci_tools.py, check_all.sh
├── tests/    the tests of these tools: the publication check, the history cleaner, the README, catalogue and brand generators, the copy of the CI tools and the shared workflow tool
├── brand/    the emblem
└── images/   this repository's banner, icon and the family picture
```

## 🛠️ Entorno de desarrollo

**Requisitos:** Python 3.11+ for the tools

```bash
python tools/make_readmes.py --check      # the READMEs (8 languages) are current
python tools/make_catalog.py --check     # the versions and maturity of the catalogue are current
python tools/make_brand.py --check        # the banners and icons are current
python tools/publication_check.py         # nothing private would leave with a publication
bash tools/check_all.sh                   # every repository's own tests, in one run
python -m unittest discover -s tests     # the tests of these tools (they need no other repository)
```

## 🔗 Proyectos relacionados

**A.R.M.O.R.** (Autonomous Radar & Multimodal Observation Range) es un sistema de seguridad perimetral hecho de repositorios independientes. Cada uno tiene su propia versión, sus propias pruebas y su propio README; esta es la familia:

* **[ARMOR-COMMON](https://github.com/JuanenRac/ARMOR-COMMON)** - Contratos de mensajes, validadores, vectores de conformidad y tipos generados
* **[ARMOR-RADAR](https://github.com/JuanenRac/ARMOR-RADAR)** - Firmware del nodo de campo para ESP32-S3 con tres radares y su propio panel web
* **[ARMOR-SOLAR](https://github.com/JuanenRac/ARMOR-SOLAR)** - Protocolos de inversores y baterías solares y los mensajes de un nodo pasarela
* **[ARMOR-ELECTRICAL](https://github.com/JuanenRac/ARMOR-ELECTRICAL)** - Nodo eléctrico: contadores, el mensaje de las lecturas de la red y las reglas para maniobrar
* **[ARMOR-ALARM](https://github.com/JuanenRac/ARMOR-ALARM)** - Nodo y central de alarma: zonas, armado, retardos, sirena y PIN, con el servidor o sin él
* **[ARMOR-HMI](https://github.com/JuanenRac/ARMOR-HMI)** - Panel táctil: el estado del sistema en una pantalla de pared, armar y reconocer alarmas, y el hogar del asistente de voz
* **[ARMOR-NETWORK](https://github.com/JuanenRac/ARMOR-NETWORK)** - La red local: sus dispositivos, internet y lo que cambia
* **[ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER)** - Coordinador central: telemetría, alarmas, dispositivos, lecturas solares y cámaras
* **[ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO)** - Consola web: cámaras, radar, alarmas, energía solar y el diseñador de sitio 2D/3D
* **[ARMOR-ANDROID-CONTROL](https://github.com/JuanenRac/ARMOR-ANDROID-CONTROL)** - Cliente Android del operador con radar 2D/3D en vivo
* **[ARMOR-SERVER-AI](https://github.com/JuanenRac/ARMOR-SERVER-AI)** - Política de inferencia visual que explica sus decisiones y nunca actúa
* **[ARMOR-VISION](https://github.com/JuanenRac/ARMOR-VISION)** - Zonas de cámara, máscaras y reglas de detección para la Jetson Orin NX
* **[ARMOR-VOICE-AI](https://github.com/JuanenRac/ARMOR-VOICE-AI)** - Intenciones de voz sin conexión con una confirmación imposible de falsificar
* **[ARMOR-HARDWARE](https://github.com/JuanenRac/ARMOR-HARDWARE)** - Cajas, electrónica y la matriz de aceptación en banco
* **[ARMOR-DEVOPS](https://github.com/JuanenRac/ARMOR-DEVOPS)** - Despliegue, el banco de pruebas de la CM5, copias de seguridad y TLS
* **[ARMOR-SIMULATOR](https://github.com/JuanenRac/ARMOR-SIMULATOR)** - Simulador de telemetría sin conexión con fallos repetibles
* **[ARMOR-UPDATER](https://github.com/JuanenRac/ARMOR-UPDATER)** - Detecta, instala y actualiza los propios repositorios del ecosistema
* **ARMOR-DOCS** (este repositorio) - Arquitectura, base de seguridad y la matriz de capacidades

## 📚 Documentación y comunidad

Dónde leer más:

* [Matriz de capacidades: qué está probado y qué no](docs/CAPABILITY_MATRIX.md)
* [Catálogo de proyectos: versiones y cómo dependen unos de otros](docs/PROJECT_CATALOG.md)
* [Historial de cambios de este repositorio](CHANGELOG.md)
* [Licencia (GPL-3.0-or-later)](LICENSE)
* Preguntas, ideas e informes: electrohobby3d@gmail.com

## 👤 AUTOR

**JuanenRac (Electro Hobby 3D)** · electrohobby3d@gmail.com

## 📜 LICENCIA

GPL-3.0-or-later - véase [LICENSE](LICENSE).
