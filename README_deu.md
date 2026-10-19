<p align="center">
  <img src="images/ARMOR_BANNER.svg" alt="ARMOR-DOCS banner" width="100%">
</p>

# 📚 ARMOR-DOCS

<p align="center">
  <a href="README.md">🇺🇸 English</a> |
  <a href="README_spa.md">🇪🇸 Español</a> |
  <a href="README_fra.md">🇫🇷 Français</a> |
  <a href="README_ita.md">🇮🇹 Italiano</a> |
  🇩🇪 <b>Deutsch</b> |
  <a href="README_zho.md">🇨🇳 简体中文</a> |
  <a href="README_jpn.md">🇯🇵 日本語</a> |
  <a href="README_por.md">🇵🇹 Português</a>
</p>

### Kanonische Architektur, Sicherheitsgrundlage und die Wahrheit darüber, was belegt ist

<p align="center">
  <img src="https://img.shields.io/badge/License-GPL%203.0-blue.svg" alt="GPL 3.0">
  <img src="https://img.shields.io/badge/Format-Markdown-083fa1.svg" alt="Format">
  <img src="https://img.shields.io/badge/Languages-8-00E5FF.svg" alt="Languages">
  <img src="https://img.shields.io/badge/Version-0.8.0.7-0f6cbd.svg" alt="Version">
  <img src="https://img.shields.io/badge/Maturity-established-2EA44F.svg" alt="Maturity">
</p>

---

**Ehrlichkeitsprüfung - was heute läuft:** Dieses Repository dokumentiert Schnittstellen und Verfahren, die validiert wurden, und sagt klar, was nicht. Lesen Sie die [Fähigkeitsmatrix](docs/CAPABILITY_MATRIX.md), bevor Sie glauben, eine Funktion sei "fertig": Sie sagt für jede, ob sie nur simuliert, auf einem Computer getestet oder auf echter Hardware verifiziert wurde. Die READMEs der achtzehn Repositorys werden aus einer einzigen Quelle (`tools/readme_src/`) in acht Sprachen geschrieben, wobei Version und Reifegrad jedes Projekts aus seinem eigenen Manifest gelesen werden, sodass sie nichts anderes sagen können als das Projekt.

---

## 📋 Auf einen Blick

| | |
|---|---|
| Version | `0.8.0.7` |
| Reifegrad | Etabliert |
| Technik | Markdown / Mermaid |
| Auf echter Hardware | Nicht zutreffend: es ist Dokumentation; sie hält fest, was die anderen Repositorys auf echter Hardware ausgeführt haben |

## 🎯 Überblick

<p align="center">
  <img src="images/ARMOR_FAMILY.svg" alt="A.R.M.O.R. family" width="100%">
</p>

* [Fähigkeitsmatrix](docs/CAPABILITY_MATRIX.md): ist jede Fähigkeit simuliert, auf einem Computer getestet oder auf Hardware verifiziert?
* [Architektur](docs/ARCHITECTURE.md): Netze, Vertrauensgrenzen, Zeit und Reihenfolge.
* [Sicherheitsgrundlage](docs/SECURITY_BASELINE.md): der VLAN-Entwurf, was der Code durchsetzt und was noch fehlt; und das [Bedrohungsmodell](docs/THREAT_MODEL.md).
* [Projektkatalog](docs/PROJECT_CATALOG.md): die achtzehn Repositorys, ihre Versionen und wie sie voneinander abhängen.
* [Schnittstellen](docs/INTERFACES.md): wer jede Schnittstelle erzeugt und nutzt und wo ihr vertraut wird.
* [Erster vertikaler Schnitt](docs/FIRST_VERTICAL_SLICE.md): was der Test vom Simulator zur Konsole beweist und was nicht.
* **Werkzeuge:** `make_readmes.py` schreibt das README jedes Repositorys in den acht Sprachen aus `readme_src/`, `make_catalog.py` schreibt die Versionen des Katalogs, `make_brand.py` sein Banner und Symbol, `publication_check.py` sucht vor einer Veröffentlichung nach allem Privaten, `clean_history.py` macht eine veröffentlichbare Kopie eines Repositorys und `sync_ci_tools.py` hält die CI-Prüfungen der Familie gleich.

## 🧩 Rolle in A.R.M.O.R.

ARMOR-DOCS ist das Gedächtnis der Familie: Hier leben die Architektur, die Sicherheitsgrundlage und die Fähigkeitsmatrix, und es ist der Ort, der für jedes Repository sagt, was wirklich auf Hardware gelaufen ist. Es hält auch das Werkzeug, das die READMEs aller achtzehn Repositorys aus einer Quelle schreibt, damit die acht Sprachen nicht auseinanderlaufen.

## 📂 Struktur des Repositorys

```text
ARMOR-DOCS/
├── docs/     CAPABILITY_MATRIX, ARCHITECTURE, SECURITY_BASELINE, PROJECT_CATALOG, INTERFACES, THREAT_MODEL, FIRST_VERTICAL_SLICE
├── tools/    make_readmes.py (+ readme_src/: the facts and the words of every repository in eight languages), make_catalog.py, make_brand.py, publication_check.py, clean_history.py, sync_ci_tools.py, check_all.sh
├── tests/    the tests of these tools: the publication check, the history cleaner, the README, catalogue and brand generators, the copy of the CI tools and the shared workflow tool
├── brand/    the emblem
└── images/   this repository's banner, icon and the family picture
```

## 🛠️ Entwicklungsumgebung

**Voraussetzungen:** Python 3.11+ for the tools

```bash
python tools/make_readmes.py --check      # the READMEs (8 languages) are current
python tools/make_catalog.py --check     # the versions and maturity of the catalogue are current
python tools/make_brand.py --check        # the banners and icons are current
python tools/publication_check.py         # nothing private would leave with a publication
bash tools/check_all.sh                   # every repository's own tests, in one run
python -m unittest discover -s tests     # the tests of these tools (they need no other repository)
```

## 🔗 Verwandte Projekte

**A.R.M.O.R.** (Autonomous Radar & Multimodal Observation Range) ist ein Perimeter-Sicherheitssystem aus unabhängigen Repositorys. Jedes hat eine eigene Version, eigene Tests und ein eigenes README; hier ist die Familie:

* **[ARMOR-COMMON](https://github.com/JuanenRac/ARMOR-COMMON)** - Nachrichtenverträge, Validierer, Konformitätsvektoren und generierte Typen
* **[ARMOR-RADAR](https://github.com/JuanenRac/ARMOR-RADAR)** - Feldknoten-Firmware für ESP32-S3 mit drei Radaren und eigenem Web-Panel
* **[ARMOR-SOLAR](https://github.com/JuanenRac/ARMOR-SOLAR)** - Protokolle für Solar-Wechselrichter und -Batterien und die Nachrichten eines Gateway-Knotens
* **[ARMOR-ELECTRICAL](https://github.com/JuanenRac/ARMOR-ELECTRICAL)** - Elektroknoten: Zähler, die Nachricht der Netzmesswerte und die Regeln fürs Schalten
* **[ARMOR-ALARM](https://github.com/JuanenRac/ARMOR-ALARM)** - Alarmknoten und Alarmzentrale: Zonen, Scharfschalten, Verzögerungen, Sirene und PIN, mit dem Server oder ohne ihn
* **[ARMOR-HMI](https://github.com/JuanenRac/ARMOR-HMI)** - Touch-Panel: der Systemzustand auf einem Wandbildschirm, Scharf- und Quittieren sowie das Zuhause des Sprachassistenten
* **[ARMOR-NETWORK](https://github.com/JuanenRac/ARMOR-NETWORK)** - Das lokale Netzwerk: seine Geräte, das Internet und was sich ändert
* **[ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER)** - Zentraler Koordinator: Telemetrie, Alarme, Geräte, Solarmesswerte und Kameras
* **[ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO)** - Web-Konsole: Kameras, Radar, Alarme, Solarenergie und 2D/3D-Standortdesigner
* **[ARMOR-ANDROID-CONTROL](https://github.com/JuanenRac/ARMOR-ANDROID-CONTROL)** - Android-Bedienclient mit Live-Radar in 2D/3D
* **[ARMOR-SERVER-AI](https://github.com/JuanenRac/ARMOR-SERVER-AI)** - Visuelle Inferenzrichtlinie, die ihre Entscheidungen erklärt und nie handelt
* **[ARMOR-VISION](https://github.com/JuanenRac/ARMOR-VISION)** - Kamerazonen, Masken und Erkennungsregeln für den Jetson Orin NX
* **[ARMOR-VOICE-AI](https://github.com/JuanenRac/ARMOR-VOICE-AI)** - Offline-Sprachabsichten mit einer nicht fälschbaren Bestätigung
* **[ARMOR-HARDWARE](https://github.com/JuanenRac/ARMOR-HARDWARE)** - Gehäuse, Elektronik und die Abnahmematrix am Prüfstand
* **[ARMOR-DEVOPS](https://github.com/JuanenRac/ARMOR-DEVOPS)** - Bereitstellung, CM5-Prüfstand, Backup und TLS
* **[ARMOR-SIMULATOR](https://github.com/JuanenRac/ARMOR-SIMULATOR)** - Offline-Telemetriesimulator mit wiederholbaren Fehlern
* **[ARMOR-UPDATER](https://github.com/JuanenRac/ARMOR-UPDATER)** - Erkennt, installiert und aktualisiert die eigenen Repositories des Ökosystems
* **ARMOR-DOCS** (dieses Repository) - Architektur, Sicherheitsgrundlage und die Fähigkeitsmatrix

## 📚 Dokumentation und Community

Hier gibt es mehr zu lesen:

* [Fähigkeitsmatrix: was belegt ist und was nicht](docs/CAPABILITY_MATRIX.md)
* [Projektkatalog: Versionen und wie die Repositorys voneinander abhängen](docs/PROJECT_CATALOG.md)
* [Änderungsverlauf dieses Repositorys](CHANGELOG.md)
* [Lizenz (GPL-3.0-or-later)](LICENSE)
* Fragen, Ideen und Meldungen: electrohobby3d@gmail.com

## 👤 AUTOR

**JuanenRac (Electro Hobby 3D)** · electrohobby3d@gmail.com

## 📜 LIZENZ

GPL-3.0-or-later - siehe [LICENSE](LICENSE).
