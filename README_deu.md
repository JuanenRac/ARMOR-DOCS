<p align="center">
  <img src="images/ARMOR_BANNER.svg" alt="ARMOR-DOCS-Banner" width="100%">
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
  <img src="https://img.shields.io/badge/License-GPL%203.0--or--later-blue.svg" alt="GPL 3.0 oder neuer">
  <img src="https://img.shields.io/badge/Format-Markdown-083fa1.svg" alt="Format">
  <img src="https://img.shields.io/badge/Languages-8-00E5FF.svg" alt="Sprachen">
  <img src="https://img.shields.io/badge/Tests-199%20passing-2ea44f.svg" alt="Tests">
  <img src="https://img.shields.io/badge/Version-0.8.1.2-0f6cbd.svg" alt="Version">
  <img src="https://img.shields.io/badge/Maturity-established-2EA44F.svg" alt="Reifegrad">
</p>

---

**Ehrlichkeitsprüfung - was heute läuft:** Dieses Repository dokumentiert Schnittstellen und Verfahren, die validiert wurden, und sagt klar, was nicht. Lesen Sie die [Fähigkeitsmatrix](docs/CAPABILITY_MATRIX.md), bevor Sie glauben, eine Funktion sei "fertig": Sie sagt für jede, ob sie nur simuliert, auf einem Computer getestet oder auf echter Hardware verifiziert wurde. Die READMEs der neunzehn Repositorys werden aus einer einzigen Quelle (`tools/readme_src/`) in acht Sprachen geschrieben, wobei Version und Reifegrad jedes Projekts aus seinem eigenen Manifest gelesen werden, sodass sie nichts anderes sagen können als das Projekt.

---

## 📋 Auf einen Blick

| | |
|---|---|
| Version | `0.8.1.2` |
| Reifegrad | Etabliert |
| Rolle | Dokumentationszentrale: Architektur, Sicherheitsbasis, Fähigkeitsmatrix und die Werkzeuge, die READMEs, Katalog und Banner schreiben |
| Technik | Python 3.11+ (Werkzeuge, Standardbibliothek), Markdown |
| Tests | 199 (`python -m unittest discover -s tests`, etwa eine Minute) |
| Schnittstellen | `make_readmes.py`, `make_catalog.py`, `make_brand.py`, `publication_check.py`, `clean_history.py`, `sync_ci_tools.py`, `check_all.sh` |
| Läuft auf | Jeder Computer mit Python; die Repositorys der Familie neben diesem |
| Auf echter Hardware | Nicht zutreffend: es ist Dokumentation; sie hält fest, was die anderen Repositorys auf echter Hardware ausgeführt haben |
| Lizenz | GPL-3.0-or-later |

**Springe zu:** [Überblick](#-überblick) · [Architektur](#-architektur) · [Sicherheit](#-sicherheit-und-schutz) · [Schnittstellen](#-schnittstellen) · [Schnellstart](#-schnellstart) · [Tests](#-tests) · [Probleme](#-fehlerbehebung) · [Struktur](#-struktur-des-repositorys) · [Verwandte](#-verwandte-projekte)

## 🚦 Projektstatus

Jede Zeile ist ein Teil dieses Repositorys, und die Ampel sagt, wie weit er heute ist. Sie beruht auf dem, was das Repository zeigen kann (Tests, Builds, Läufe), nicht auf dem, was geplant ist.

🟢 Fertig und überprüft · 🟡 Funktioniert, mit bekannten Grenzen · 🟠 Teilweise fertig oder noch nicht überprüft · 🔴 Nicht gemacht oder funktioniert nicht

| Bereich | Stand | Was das hier bedeutet |
|---|---|---|
| Software | 🟢 | Die Generatoren für READMEs, Banner, Katalog und Fähigkeitenmatrix sowie die in jedes Repository kopierten CI-Werkzeuge laufen und sind getestet. |
| Tests | 🟢 | Die 199 Tests der Werkzeuge bestehen (`python -m unittest discover -s tests`): die Veröffentlichungsprüfung, der Verlaufsbereiniger, die Generatoren für README, Katalog und Marke, die Kopie der CI-Werkzeuge und das Werkzeug des gemeinsamen Ablaufs. |
| Automatische Prüfungen | 🟢 | Jeder Push prüft, dass die READMEs, die Banner und der Katalog aktuell sind und dass jedes Repository des Registers seine Statustabelle hat. |
| Integration | 🟢 | Die READMEs aller Repositorys entstehen aus einer Quelle, wobei Version und Reifegrad jedes Repositorys aus dessen eigenem Manifest gelesen werden. |
| Dokumentation | 🟢 | Die Fähigkeitenmatrix sagt für jede Funktion, ob sie nur simuliert, auf einem Rechner getestet oder an echter Hardware überprüft wurde; die acht Sprachen und das Änderungsprotokoll sind aktuell. |

## 🎯 Überblick

<p align="center">
  <img src="images/ARMOR_FAMILY.svg" alt="A.R.M.O.R. family" width="100%">
</p>

* [Fähigkeitsmatrix](docs/CAPABILITY_MATRIX.md): ist jede Fähigkeit simuliert, auf einem Computer getestet oder auf Hardware verifiziert?
* [Architektur](docs/ARCHITECTURE.md): Netze, Vertrauensgrenzen, Zeit und Reihenfolge.
* [Sicherheitsgrundlage](docs/SECURITY_BASELINE.md): der VLAN-Entwurf, was der Code durchsetzt und was noch fehlt; und das [Bedrohungsmodell](docs/THREAT_MODEL.md).
* [Projektkatalog](docs/PROJECT_CATALOG.md): die neunzehn Repositorys, ihre Versionen und wie sie voneinander abhängen.
* [Schnittstellen](docs/INTERFACES.md): wer jede Schnittstelle erzeugt und nutzt und wo ihr vertraut wird.
* [Erster vertikaler Schnitt](docs/FIRST_VERTICAL_SLICE.md): was der Test vom Simulator zur Konsole beweist und was nicht.
* **Werkzeuge:** `make_readmes.py` schreibt das README jedes Repositorys in den acht Sprachen aus `readme_src/`, `make_catalog.py` schreibt die Versionen des Katalogs, `make_brand.py` sein Banner und Symbol, `publication_check.py` sucht vor einer Veröffentlichung nach allem Privaten, `clean_history.py` macht eine veröffentlichbare Kopie eines Repositorys und `sync_ci_tools.py` hält die CI-Prüfungen der Familie gleich.

## 🧩 Rolle in A.R.M.O.R.

ARMOR-DOCS ist das Gedächtnis der Familie: Hier leben die Architektur, die Sicherheitsgrundlage und die Fähigkeitsmatrix, und es ist der Ort, der für jedes Repository sagt, was wirklich auf Hardware gelaufen ist. Es hält auch das Werkzeug, das die READMEs aller neunzehn Repositorys aus einer Quelle schreibt, damit die acht Sprachen nicht auseinanderlaufen.

| Er spricht mit | Wie | Wozu |
|---|---|---|
| Jedes Repository der Familie | ihre `armor.project.json` und ihre README-Dateien | die Werkzeuge lesen Version und Reife und schreiben README, Banner und CI-Kopien |
| ARMOR-COMMON | `registry/repositories.json` | die eine Liste der Repositorys der Familie, gelesen von `registry.py` |
| Wer veröffentlicht | `publication_check.py`  `clean_history.py` | was durchsickern würde und eine veröffentlichbare Kopie mit einem Commit |

## 🏛️ Architektur

<p align="center">
  <img src="images/architecture.svg" alt="ARMOR-DOCS architecture: what the tools read, the tools themselves and what they write in every repository" width="100%">
</p>

## 🔒 Sicherheit und Schutz

| Bedrohung | Abwehr |
|---|---|
| Etwas Privates veröffentlichen | `publication_check.py` liest nur git (versionierte Dateien und Verlauf, nie ignorierte) und gibt das Geheimnis nie aus. BLOCK: ein privater Schlüssel, eine öffentliche IP-Adresse, eine persönliche E-Mail-Adresse, ein versioniertes `secrets/` oder `.env`, ein Commit mit Co-Autor oder KI-Zeile, ein Commit-Autor, der nicht der des Projekts ist; REVIEW: eine Zeile, die wie ein Klartext-Passwort oder -Token aussieht; Ausstieg mit 1 bei jedem BLOCK |
| Ein Verlauf mit Überresten | `clean_history.py` erzeugt eine veröffentlichbare Kopie eines Repositorys mit einem einzigen Commit des Projektautors |
| Mehr behaupten, als belegt ist | `docs/CAPABILITY_MATRIX.md` hat drei Stufen (Simulated, Local, Verified) sowie None, Absent und Local-not-activated; nur die Verified-Zeilen haben Hardware berührt (der CM5-Prüfstand im Alltag) |
| Ein README, das etwas anderes sagt als das Projekt | Version und Reife jedes READMEs werden aus dessen eigenem Manifest gelesen; jeder Push prüft, dass READMEs, Banner und Katalog aktuell sind und jedes Repository des Registers seine Statustabelle hat |

Die Sicherheitsdokumente der Familie sind [docs/SECURITY_BASELINE.md](docs/SECURITY_BASELINE.md) (das VLAN-Design, was der Code durchsetzt und was noch fehlt) und [docs/THREAT_MODEL.md](docs/THREAT_MODEL.md). Nichts davon beweist die Abwesenheit eines Geheimnisses.

## 🔌 Schnittstellen

| Route | Authentifizierung | Was sie tut |
|---|---|---|
| `python tools/make_readmes.py [--check]` | - | schreibt das README jedes Repositorys in acht Sprachen aus `tools/readme_src/`; `--check` schlägt fehl, wenn eines veraltet ist. Es überschreibt jede Datei: die Quelle ändern, nie die READMEs |
| `python tools/make_catalog.py [--check]`  `make_brand.py [--check]` | - | die Versionen und Reife in `docs/PROJECT_CATALOG.md` sowie Banner und Symbole |
| `python tools/publication_check.py [REPO] [--no-history] [--ref=BRANCH]` | - | was durchsickern würde, wenn die Repositorys veröffentlicht würden; Ausstieg mit 1 bei BLOCK |
| `python tools/clean_history.py` | - | eine veröffentlichbare Kopie eines Repositorys mit einem Commit |
| `python tools/sync_ci_tools.py [--check]` | - | kopiert die gemeinsamen CI-Prüfungen und den Starter in jedes Repository; `--check` schlägt fehl, wenn eine Kopie abweicht |
| `bash tools/check_all.sh [--android] [--compose]` | - | die Tests jedes Repositorys in einem Lauf; eine Prüfung ohne ihr Werkzeug ist SKIP, nie PASS |

Die Quelle jedes READMEs ist `tools/readme_src/repos/<REPOSITORY>.py` (die sprachunabhängigen Fakten und die Worte der acht Sprachen), mit `ui.py` für die Worte rund um jedes README und `shots.py` für die Aufnahmen. `tools/registry.py` liest die Repository-Liste von ARMOR-COMMON. Siehe auch [docs/INTERFACES.md](docs/INTERFACES.md) und [docs/SETUP_CODE.md](docs/SETUP_CODE.md).

## 🚀 Schnellstart

**Voraussetzungen:** Python 3.11+ für die Werkzeuge (nur Standardbibliothek); die Repositorys der Familie neben diesem für die Prüfungen, die sie lesen.

```bash
python tools/make_readmes.py --check  # die READMEs (8 Sprachen) sind aktuell
python tools/make_catalog.py --check  # Versionen und Reife des Katalogs sind aktuell
python tools/make_brand.py --check    # Banner und Symbole sind aktuell
python tools/publication_check.py     # nichts Privates würde mit einer Veröffentlichung hinausgehen
bash tools/check_all.sh               # die Tests jedes Repositorys in einem Lauf
python -m unittest discover -s tests  # 199 Tests dieser Werkzeuge; sie brauchen kein anderes Repository
```

## 🧪 Tests

| Bereich | Was er abdeckt |
|---|---|
| Der README-Generator | die acht Sprachen und die Abschnitte jedes Repositorys |
| Katalog und Marke | `test_make_catalog_and_brand.py`, `test_repository_registry.py` |
| Veröffentlichung | was BLOCK und REVIEW ist, und die Ein-Commit-Kopie |
| CI-Werkzeuge und Starter | `test_ci_validate.py`, `test_sync_ci_tools.py`, `test_project_tool.py`, `test_check_all_script.py` |

GitHub Actions führt bei jedem Push und Pull Request die A.R.M.O.R.-Basis aus: die Prüfung von Manifest, Version, Änderungsprotokoll und README-Parität, dann den eigenen Build und die eigenen Tests des Projekts.

## 🏗️ Build und Veröffentlichung

Es gibt nichts zu kompilieren. Die Version steht in `armor.project.json` und im README-Badge (aus dem Manifest gelesen); jede Version hat ihren Eintrag in [CHANGELOG.md](CHANGELOG.md). Releases werden auf GitHub veröffentlicht.

## 🩺 Fehlerbehebung

| Du siehst | Weil | Tu |
|---|---|---|
| `READMEs out of date:` + a list | eine Quelle in `tools/readme_src/` oder ein Manifest hat sich geändert und die READMEs wurden nicht neu geschrieben | `python tools/make_readmes.py` ausführen, in jedem Repository ansehen, was sich geändert hat, und dort committen |
| `Status tables incomplete:` | ein Repository des Registers hat eine Statustabelle ohne die erwarteten Zeilen oder Farben | `FACTS["status"]` und die Hinweise in seiner Quelle vervollständigen |
| Eine Prüfung sagt SKIP | sein Werkzeug oder das Repository neben diesem fehlt; eine Prüfung ohne Werkzeug ist nie PASS | das Werkzeug installieren oder das Repository neben diesem klonen |
| `publication_check.py` BLOCK | etwas, das nicht öffentlich werden darf, wurde gefunden (Datei, Zeile und Art, nie der Wert) | entfernen, und `clean_history.py` nutzen, wenn es im Verlauf steht |

## 📂 Struktur des Repositorys

<p align="center">
  <img src="images/repository-structure.svg" alt="Repository structure of ARMOR-DOCS" width="100%">
</p>

<details>
<summary>Textversion des Baums</summary>

```text
ARMOR-DOCS/
├── tools/
│   ├── make_readmes.py                          die READMEs aus einer Quelle, in acht Sprachen
│   ├── readme_src/                              die Fakten und Worte jedes Repositorys
│   ├── make_catalog.py make_brand.py            der Katalog; Banner und Symbole
│   ├── brand_banner.py registry.py              die Banner-Zeichnung; die Liste von ARMOR-COMMON
│   ├── publication_check.py                     nichts Privates verlässt das Haus
│   ├── clean_history.py sync_ci_tools.py        eine veröffentlichbare Kopie; gleiche CI-Prüfungen
│   ├── check_all.sh                             die Tests jedes Repositorys in einem Lauf
│   ├── armor_ci_validate.py                     die CI-Prüfung jedes Repositorys
│   ├── armor_project_tool.py pretty_run.py      der Starter und sein Live-Panel
│   ├── make_architecture.py make_structure.py   die zwei Bilder der READMEs
│   └── universal_readme_check.py                die Layout-Prüfung der READMEs
├── docs/                                        CAPABILITY_MATRIX, ARCHITECTURE, SECURITY_BASELINE, THREAT_MODEL, PROJECT_CATALOG, INTERFACES, FIRST_VERTICAL_SLICE, SETUP_CODE
├── tests/                                       die Tests dieser Werkzeuge
├── brand/                                       das Emblem
├── images/                                      Banner, Symbol, das Familienbild und die Bilder dieses READMEs
├── .github/                                     CI-Workflow, Dashboard-Hinweis, Vorlagen für Issues und Pull Requests
├── armor.project.json                           Manifest: Version, Rolle, Reife
├── CHANGELOG.md                                 was sich in jeder Version geändert hat
├── run.sh run.bat                               Start, gemeinsamer Ablauf
├── build.sh build.bat                           Bauen und Testen, gemeinsamer Ablauf
├── build-test.sh build-test.bat                 Bauen, Testen und Verpacken
├── test.sh test.bat                             nur die Tests, nie die Version
└── SECURITY.md SUPPORT.md CONTRIBUTING.md CODE_OF_CONDUCT.md LICENSE
```

</details>

## 🗺️ Roadmap und bekannte Grenzen

**Bekannte Grenzen heute**

* Die Fähigkeitsmatrix ist die Wahrheit darüber, was gelaufen ist: Solange eine Zeile nicht Verified sagt, hat sie keine echte Hardware berührt.
* Nur der Radar-Knoten und der CM5-Prüfstand liefen auf echter Hardware.
* Keine unabhängige Sicherheitsprüfung.

**Als Nächstes**

* Zeilen der Matrix auf Verified setzen, sobald die anderen Knoten auf ihren Platinen laufen.

## 🌍 Sprachen

README und Texte gibt es auf Englisch, Spanisch, Französisch, Italienisch, Deutsch, Chinesisch, Japanisch und europäischem Portugiesisch.

## 🔗 Verwandte Projekte

**A.R.M.O.R.** (Autonomous Radar & Multimodal Observation Range) ist ein Perimeter-Sicherheitssystem aus unabhängigen Repositorys. Jedes hat eine eigene Version, eigene Tests und ein eigenes README; hier ist die Familie:

* **[ARMOR-COMMON](https://github.com/JuanenRac/ARMOR-COMMON)** - Nachrichtenverträge, Validierer, Konformitätsvektoren und generierte Typen
* **[ARMOR-NODE-RADAR](https://github.com/JuanenRac/ARMOR-NODE-RADAR)** - Feldknoten-Firmware für ESP32-S3 mit drei Radaren und eigenem Web-Panel
* **[ARMOR-NODE-SOLAR](https://github.com/JuanenRac/ARMOR-NODE-SOLAR)** - Protokolle für Solar-Wechselrichter und -Batterien und die Nachrichten eines Gateway-Knotens
* **[ARMOR-NODE-ELECTRICAL](https://github.com/JuanenRac/ARMOR-NODE-ELECTRICAL)** - Elektroknoten: Zähler, die Nachricht der Netzmesswerte und die Regeln fürs Schalten
* **[ARMOR-NODE-ALARM](https://github.com/JuanenRac/ARMOR-NODE-ALARM)** - Alarmknoten und Alarmzentrale: Zonen, Scharfschalten, Verzögerungen, Sirene und PIN, mit dem Server oder ohne ihn
* **[ARMOR-NODE-HMI](https://github.com/JuanenRac/ARMOR-NODE-HMI)** - Touch-Panel: der Systemzustand auf einem Wandbildschirm, Scharf- und Quittieren sowie das Zuhause des Sprachassistenten
* **[ARMOR-NETWORK](https://github.com/JuanenRac/ARMOR-NETWORK)** - Das lokale Netzwerk: seine Geräte, das Internet und was sich ändert
* **[ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER)** - Zentraler Koordinator: Telemetrie, Alarme, Geräte, Solarmesswerte und Kameras
* **[ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO)** - Web-Konsole: Kameras, Radar, Alarme, Solarenergie und 2D/3D-Standortdesigner
* **[ARMOR-ANDROID-CONTROL](https://github.com/JuanenRac/ARMOR-ANDROID-CONTROL)** - Android-Bedienclient mit Live-Radar in 2D/3D
* **[ARMOR-IOS-CONTROL](https://github.com/JuanenRac/ARMOR-IOS-CONTROL)** - iPhone-Bedienclient
* **[ARMOR-SERVER-AI](https://github.com/JuanenRac/ARMOR-SERVER-AI)** - Visuelle Inferenzrichtlinie, die ihre Entscheidungen erklärt und nie handelt
* **[ARMOR-VISION](https://github.com/JuanenRac/ARMOR-VISION)** - Kamerazonen, Masken und Erkennungsregeln für den Jetson Orin NX
* **[ARMOR-VOICE-AI](https://github.com/JuanenRac/ARMOR-VOICE-AI)** - Offline-Sprachabsichten mit einer nicht fälschbaren Bestätigung
* **[ARMOR-HARDWARE](https://github.com/JuanenRac/ARMOR-HARDWARE)** - Gehäuse, Elektronik und die Abnahmematrix am Prüfstand
* **[ARMOR-DEVOPS](https://github.com/JuanenRac/ARMOR-DEVOPS)** - Bereitstellung, CM5-Prüfstand, Backup und TLS
* **[ARMOR-SIMULATOR](https://github.com/JuanenRac/ARMOR-SIMULATOR)** - Offline-Telemetriesimulator mit wiederholbaren Fehlern
* **[ARMOR-UPDATER](https://github.com/JuanenRac/ARMOR-UPDATER)** - Erkennt, installiert und aktualisiert die eigenen Repositorys des Ökosystems
* **ARMOR-DOCS** (dieses Repository) - Architektur, Sicherheitsgrundlage und die Fähigkeitsmatrix

## 📚 Dokumentation

* [ARCHITECTURE](docs/ARCHITECTURE.md): Netze, Vertrauensgrenzen, Zeit und Reihenfolge
* [SECURITY_BASELINE](docs/SECURITY_BASELINE.md): das VLAN-Design, was der Code durchsetzt und was fehlt
* [THREAT_MODEL](docs/THREAT_MODEL.md): wogegen verteidigt wird und wogegen nicht
* [INTERFACES](docs/INTERFACES.md): wer jede Schnittstelle erzeugt und nutzt und wo ihr vertraut wird
* [FIRST_VERTICAL_SLICE](docs/FIRST_VERTICAL_SLICE.md): was der Test vom Simulator zur Konsole beweist und was nicht
* [SETUP_CODE](docs/SETUP_CODE.md): der Einrichtungscode der Knoten
* [Fähigkeitsmatrix: was belegt ist und was nicht](docs/CAPABILITY_MATRIX.md)
* [Projektkatalog: Versionen und wie die Repositorys voneinander abhängen](docs/PROJECT_CATALOG.md)
* [Änderungsverlauf dieses Repositorys](CHANGELOG.md)

## 🤝 Mitwirken und Community

* Führe vor einem Pull Request `python -I tools/armor_ci_validate.py` und die Tests aus: Beide müssen bestehen. Siehe [CONTRIBUTING.md](CONTRIBUTING.md) und den [Verhaltenskodex](CODE_OF_CONDUCT.md).
* Das README gibt es in acht Sprachen, und es wird aus den Quellen in ARMOR-DOCS erzeugt: Eine Textänderung erfolgt dort.
* Eine Änderung an einer Nachricht zwischen Komponenten beginnt in ARMOR-COMMON.
* Beschreibe nichts als auf einer Platine funktionierend, was nur gebaut wurde.
* Melde eine Schwachstelle privat: [SECURITY.md](SECURITY.md). Fragen, Ideen und Meldungen: electrohobby3d@gmail.com ([SUPPORT.md](SUPPORT.md)).

## 👤 AUTOR

**JuanenRac (Electro Hobby 3D)** · electrohobby3d@gmail.com

## 📜 LIZENZ

GPL-3.0-or-later - siehe [LICENSE](LICENSE).
