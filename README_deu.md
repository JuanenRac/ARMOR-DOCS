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
  <a href="README_jpn.md">🇯🇵 日本語</a>
</p>

### Kanonische Architektur, Sicherheitsgrundlage und die Wahrheit darüber, was belegt ist

<p align="center">
  <img src="https://img.shields.io/badge/License-GPL%203.0-blue.svg" alt="GPL 3.0">
  <img src="https://img.shields.io/badge/Format-Markdown-083fa1.svg" alt="Format">
  <img src="https://img.shields.io/badge/Languages-7-00E5FF.svg" alt="Languages">
  <img src="https://img.shields.io/badge/Maturity-functional-00E5FF.svg" alt="Maturity">
</p>

---

**Ehrlichkeitsprüfung - was heute läuft:** Dieses Repository dokumentiert Schnittstellen und Verfahren, die validiert wurden, und sagt klar, was nicht. Lies die [Fähigkeitsmatrix](docs/CAPABILITY_MATRIX.md), bevor du glaubst, eine Funktion sei „fertig“: sie sagt für jede, ob sie nur simuliert, am Rechner getestet oder auf echter Hardware verifiziert wurde.

---

## 🎯 Überblick

<p align="center">
  <img src="images/ARMOR_FAMILY.svg" alt="A.R.M.O.R. family" width="100%">
</p>

* [Fähigkeitsmatrix](docs/CAPABILITY_MATRIX.md): ist jede Fähigkeit simuliert, lokal oder auf Hardware verifiziert?
* [Architektur](docs/ARCHITECTURE.md): Netze, Vertrauensgrenzen, Zeit und Reihenfolge.
* [Sicherheitsgrundlage](docs/SECURITY_BASELINE.md): das VLAN-Design, was der Code durchsetzt und was noch fehlt.
* [Projektkatalog](docs/PROJECT_CATALOG.md): die zwölf Repositorys, ihre Versionen und wie sie voneinander abhängen.
* [Schnittstellen](docs/INTERFACES.md): wer jede Schnittstelle erzeugt und verbraucht und wo ihr vertraut wird.
* [Erster vertikaler Schnitt](docs/FIRST_VERTICAL_SLICE.md): was der Test vom Simulator bis zur Konsole belegt und was nicht.
* **Werkzeuge:** `make_readmes.py` schreibt das README jedes Repositorys in sieben Sprachen, `make_brand.py` sein Banner und Symbol, `publication_check.py` sucht vor einer Veröffentlichung nach Privatem und `clean_history.py` erstellt eine veröffentlichbare Kopie eines Repositorys.

## 📂 Struktur des Repositorys

```text
ARMOR-DOCS/
├── docs/     CAPABILITY_MATRIX, ARCHITECTURE, SECURITY_BASELINE, PROJECT_CATALOG, INTERFACES, FIRST_VERTICAL_SLICE
├── tools/    make_readmes.py (+ readme_data/), make_brand.py, publication_check.py, clean_history.py, check_all.sh
├── brand/    the emblem
└── images/   this repository's banner and icon
```

## 🛠️ Entwicklungsumgebung

```bash
python tools/make_readmes.py --check      # the READMEs (7 languages) are current
python tools/make_brand.py --check        # the banners and icons are current
python tools/publication_check.py         # nothing private would leave with a publication
bash tools/check_all.sh                   # every repository's own tests, in one run
```

Die Audits der Familie (auf Spanisch) liegen im Stammverzeichnis dieses Repositorys.

## 🔗 Verwandte Projekte

**A.R.M.O.R.** (Autonomous Radar & Multimodal Observation Range) ist ein Perimeter-Sicherheitssystem aus unabhängigen Repositorys. Jedes hat eine eigene Version, eigene Tests und ein eigenes README; hier ist die Familie:

* **[ARMOR-COMMON](../ARMOR-COMMON)** - Nachrichtenverträge, Validierer, Konformitätsvektoren und generierte Typen
* **[ARMOR-RADAR](../ARMOR-RADAR)** - Feldknoten-Firmware für ESP32-S3 mit drei Radaren und eigenem Web-Panel
* **[ARMOR-SOLAR](../ARMOR-SOLAR)** - Protokolle für Solar-Wechselrichter und -Batterien und die Nachrichten eines Gateway-Knotens
* **[ARMOR-ELECTRICAL](../ARMOR-ELECTRICAL)** - Elektroknoten: Zähler, die Nachricht der Netzmesswerte und die Regeln fürs Schalten
* **[ARMOR-NETWORK](../ARMOR-NETWORK)** - Das lokale Netzwerk: seine Geräte, das Internet und was sich ändert
* **[ARMOR-SERVER](../ARMOR-SERVER)** - Zentraler Koordinator: Telemetrie, Alarme, Geräte, Solarmesswerte und Kameras
* **[ARMOR-STUDIO](../ARMOR-STUDIO)** - Web-Konsole: Kameras, Radar, Alarme, Solarenergie und 2D/3D-Standortdesigner
* **[ARMOR-ANDROID-CONTROL](../ARMOR-ANDROID-CONTROL)** - Android-Bedienclient mit Live-Radar in 2D/3D
* **[ARMOR-SERVER-AI](../ARMOR-SERVER-AI)** - Visuelle Inferenzrichtlinie, die ihre Entscheidungen erklärt und nie handelt
* **[ARMOR-VOICE-AI](../ARMOR-VOICE-AI)** - Offline-Sprachabsichten mit einer nicht fälschbaren Bestätigung
* **[ARMOR-HARDWARE](../ARMOR-HARDWARE)** - Gehäuse, Elektronik und die Abnahmematrix am Prüfstand
* **[ARMOR-DEVOPS](../ARMOR-DEVOPS)** - Bereitstellung, CM5-Prüfstand, Backup und TLS
* **[ARMOR-SIMULATOR](../ARMOR-SIMULATOR)** - Offline-Telemetriesimulator mit wiederholbaren Fehlern
* **[ARMOR-UPDATER](../ARMOR-UPDATER)** - Erkennt, installiert und aktualisiert die eigenen Repositories des Ökosystems
* **ARMOR-DOCS** (dieses Repository) - Architektur, Sicherheitsgrundlage und die Fähigkeitsmatrix

## 📚 Dokumentation und Community

Hier gibt es mehr zu lesen:

* [Fähigkeitsmatrix: was belegt ist und was nicht](../ARMOR-DOCS/docs/CAPABILITY_MATRIX.md)
* [Projektkatalog: Versionen und wie die Repositorys voneinander abhängen](../ARMOR-DOCS/docs/PROJECT_CATALOG.md)
* [Änderungsverlauf dieses Repositorys](CHANGELOG.md)
* [Lizenz (GPL-3.0-or-later)](LICENSE)
* Fragen, Ideen und Meldungen: electrohobby3d@gmail.com

## 👤 AUTOR

**JuanenRac (Electro Hobby 3D)** · electrohobby3d@gmail.com

## 📜 LIZENZ

GPL-3.0-or-later - siehe [LICENSE](LICENSE).
