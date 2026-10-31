<p align="center">
  <img src="images/ARMOR_BANNER.svg" alt="Banner di ARMOR-DOCS" width="100%">
</p>

# 📚 ARMOR-DOCS

<p align="center">
  <a href="README.md">🇺🇸 English</a> |
  <a href="README_spa.md">🇪🇸 Español</a> |
  <a href="README_fra.md">🇫🇷 Français</a> |
  🇮🇹 <b>Italiano</b> |
  <a href="README_deu.md">🇩🇪 Deutsch</a> |
  <a href="README_zho.md">🇨🇳 简体中文</a> |
  <a href="README_jpn.md">🇯🇵 日本語</a> |
  <a href="README_por.md">🇵🇹 Português</a>
</p>

### Architettura canonica, base di sicurezza e la verità su ciò che è provato

<p align="center">
  <img src="https://img.shields.io/badge/License-GPL%203.0--or--later-blue.svg" alt="GPL 3.0 o successiva">
  <img src="https://img.shields.io/badge/Format-Markdown-083fa1.svg" alt="Format">
  <img src="https://img.shields.io/badge/Languages-8-00E5FF.svg" alt="Lingue">
  <img src="https://img.shields.io/badge/Tests-199%20passing-2ea44f.svg" alt="Test">
  <img src="https://img.shields.io/badge/Version-0.8.1.3-0f6cbd.svg" alt="Versione">
  <img src="https://img.shields.io/badge/Maturity-established-2EA44F.svg" alt="Maturità">
</p>

---

**Controllo di onestà - cosa funziona oggi:** Questo repository documenta interfacce e procedure che sono state validate, e dice chiaramente ciò che non lo è. Leggi la [matrice delle capacità](docs/CAPABILITY_MATRIX.md) prima di credere che una funzione sia "fatta": dice per ciascuna se è stata solo simulata, provata su un computer o verificata su hardware reale. I README dei diciannove repository sono scritti da un'unica fonte (`tools/readme_src/`) in otto lingue, con la versione e la maturità di ciascuno lette dal suo manifesto, così non possono dire qualcosa di diverso dal progetto.

---

## 📋 In breve

| | |
|---|---|
| Versione | `0.8.1.3` |
| Maturità | Consolidato |
| Ruolo | Centro di documentazione: architettura, base di sicurezza, matrice delle capacità e gli strumenti che scrivono README, catalogo e banner |
| Tecnologia | Python 3.11+ (strumenti, libreria standard), Markdown |
| Test | 199 (`python -m unittest discover -s tests`, circa un minuto) |
| Interfacce | `make_readmes.py`, `make_catalog.py`, `make_brand.py`, `publication_check.py`, `clean_history.py`, `sync_ci_tools.py`, `check_all.sh` |
| Gira su | Qualsiasi computer con Python; i repository della famiglia accanto a questo |
| Su hardware reale | Non applicabile: è documentazione; registra ciò che gli altri repository hanno fatto girare su hardware reale |
| Licenza | GPL-3.0-or-later |

**Vai a:** [Panoramica](#-panoramica) · [Architettura](#-architettura) · [Sicurezza](#-sicurezza-e-protezione) · [Interfacce](#-interfacce) · [Avvio rapido](#-avvio-rapido) · [Test](#-test) · [Problemi](#-risoluzione-dei-problemi) · [Struttura](#-struttura-del-repository) · [Correlati](#-progetti-correlati)

## 🚦 Stato del progetto

Ogni riga è una parte di questo repository e il semaforo dice a che punto è oggi. È scritta in base a ciò che il repository può mostrare (test, compilazioni, esecuzioni), non a ciò che è previsto.

🟢 Fatto e verificato · 🟡 Funziona, con limiti noti · 🟠 Fatto a metà o non ancora verificato · 🔴 Non fatto o non funzionante

| Area | Stato | Cosa significa qui |
|---|---|---|
| Software | 🟢 | I generatori di README, banner, catalogo e matrice delle capacità, e gli strumenti di CI copiati in ogni repository, funzionano e sono testati. |
| Test | 🟢 | I 199 test degli strumenti passano (`python -m unittest discover -s tests`): il controllo di pubblicazione, il pulitore della cronologia, i generatori di README, catalogo e marchio, la copia degli strumenti CI e lo strumento del flusso condiviso. |
| Controlli automatici | 🟢 | Ogni push verifica che i README, i banner e il catalogo siano aggiornati e che ogni repository del registro abbia la sua tabella di stato. |
| Integrazione | 🟢 | I README di tutti i repository sono scritti da un'unica fonte, con la versione e la maturità di ciascuno lette dal proprio manifesto. |
| Documentazione | 🟢 | La matrice delle capacità dice, per ogni funzione, se è stata solo simulata, testata su un computer o verificata su hardware reale; le otto lingue e il registro delle modifiche sono aggiornati. |

## 🎯 Panoramica

<p align="center">
  <img src="images/ARMOR_FAMILY.svg" alt="A.R.M.O.R. family" width="100%">
</p>

* [Matrice delle capacità](docs/CAPABILITY_MATRIX.md): per ogni capacità, è simulata, provata su un computer o verificata su hardware?
* [Architettura](docs/ARCHITECTURE.md): reti, confini di fiducia, tempo e ordine.
* [Base di sicurezza](docs/SECURITY_BASELINE.md): il progetto delle VLAN, ciò che il codice impone e ciò che manca ancora; e il [modello delle minacce](docs/THREAT_MODEL.md).
* [Catalogo dei progetti](docs/PROJECT_CATALOG.md): i diciannove repository, le loro versioni e come dipendono l'uno dall'altro.
* [Interfacce](docs/INTERFACES.md): chi produce e consuma ogni interfaccia e dove ci si fida.
* [Prima fetta verticale](docs/FIRST_VERTICAL_SLICE.md): cosa dimostra il test dal simulatore alla console e cosa no.
* **Strumenti:** `make_readmes.py` scrive il README di ogni repository nelle otto lingue da `readme_src/`, `make_catalog.py` scrive le versioni del catalogo, `make_brand.py` il suo banner e l'icona, `publication_check.py` cerca qualsiasi cosa privata prima di una pubblicazione, `clean_history.py` fa una copia pubblicabile di un repository e `sync_ci_tools.py` mantiene uguali i controlli di CI della famiglia, ruff e mypy compresi (versioni fissate: ruff su tutto il repository, mypy su `src/` dove esiste una configurazione di mypy e su `tools/` e `scripts/`; `ci_lint = false` nel suo pyproject.toml li salta).

## 🧩 Ruolo in A.R.M.O.R.

ARMOR-DOCS è la memoria della famiglia: è dove vivono l'architettura, la base di sicurezza e la matrice delle capacità, e il luogo che dice, per ogni repository, cosa ha davvero girato su hardware. Tiene anche lo strumento che scrive i README di tutti e diciannove i repository da un'unica fonte, perché le otto lingue non divergano.

| Parla con | Come | A che scopo |
|---|---|---|
| Ogni repository della famiglia | il loro `armor.project.json` e i file README | gli strumenti leggono versione e maturità e scrivono README, banner e copie CI |
| ARMOR-COMMON | `registry/repositories.json` | l'unico elenco dei repository della famiglia, letto da `registry.py` |
| Chi pubblica | `publication_check.py`  `clean_history.py` | ciò che trapelerebbe e una copia a un solo commit pubblicabile |

## 🏛️ Architettura

<p align="center">
  <img src="images/architecture.svg" alt="ARMOR-DOCS architecture: what the tools read, the tools themselves and what they write in every repository" width="100%">
</p>

## 🔒 Sicurezza e protezione

| Minaccia | Difesa |
|---|---|
| Pubblicare qualcosa di privato | `publication_check.py` legge solo git (file versionati e cronologia, mai gli ignorati) e non stampa mai il segreto. BLOCK: una chiave privata, un IP pubblico, un'e-mail personale, un `secrets/` o `.env` versionato, un commit con coautore o riga di IA, un autore di commit diverso da quello del progetto; REVIEW: una riga che sembra una password o un token in chiaro; esce con 1 a ogni BLOCK |
| Una cronologia con residui | `clean_history.py` crea una copia pubblicabile di un repository con un solo commit fatto dall'autore del progetto |
| Affermare più di quanto provato | `docs/CAPABILITY_MATRIX.md` ha tre livelli (Simulated, Local, Verified) più None, Absent e Local-not-activated; solo le righe Verified hanno toccato hardware (il banco di prova CM5 in uso quotidiano) |
| Un README che dice altro dal progetto | La versione e la maturità di ogni README si leggono dal suo manifesto; ogni push verifica che README, banner e catalogo siano aggiornati e che ogni repository del registro abbia la sua tabella di stato |

I documenti di sicurezza della famiglia sono [docs/SECURITY_BASELINE.md](docs/SECURITY_BASELINE.md) (il progetto delle VLAN, cosa fa rispettare il codice e cosa manca ancora) e [docs/THREAT_MODEL.md](docs/THREAT_MODEL.md). Nulla di questo prova l'assenza di un segreto.

## 🔌 Interfacce

| Rotta | Autenticazione | Cosa fa |
|---|---|---|
| `python tools/make_readmes.py [--check]` | - | scrive il README di ogni repository in otto lingue da `tools/readme_src/`; `--check` fallisce se uno è vecchio. Riscrive ogni file: cambia la fonte, mai i README |
| `python tools/make_catalog.py [--check]`  `make_brand.py [--check]` | - | le versioni e la maturità di `docs/PROJECT_CATALOG.md`, e banner e icone |
| `python tools/publication_check.py [REPO] [--no-history] [--ref=BRANCH]` | - | ciò che trapelerebbe se i repository fossero pubblicati; esce con 1 a ogni BLOCK |
| `python tools/clean_history.py` | - | una copia pubblicabile di un repository con un solo commit |
| `python tools/sync_ci_tools.py [--check]` | - | copia i controlli CI e l'avviatore in ogni repository; `--check` fallisce se una copia è divergente |
| `python tools/status_lights.py --check|--suggest|--apply` | - | mantiene le luci della tabella di stato del progetto entro ciò che il manifesto consente (maturità ed evidenza); sposta luci, mai frasi; la CI di ogni repository esegue `--check` |
| `bash tools/check_all.sh [--android] [--compose]` | - | i test di ogni repository in un'esecuzione; un controllo senza il suo strumento è SKIP, mai PASS |

La fonte di ogni README è `tools/readme_src/repos/<REPOSITORY>.py` (i fatti indipendenti dalla lingua e le parole delle otto lingue), con `ui.py` per le parole attorno a ogni README e `shots.py` per le schermate. `tools/registry.py` legge l'elenco dei repository di ARMOR-COMMON. Vedi anche [docs/INTERFACES.md](docs/INTERFACES.md) e [docs/SETUP_CODE.md](docs/SETUP_CODE.md).

## 🚀 Avvio rapido

**Requisiti:** Python 3.11+ per gli strumenti (solo libreria standard); i repository della famiglia accanto a questo per i controlli che li leggono.

```bash
python tools/make_readmes.py --check  # i README (8 lingue) sono aggiornati
python tools/make_catalog.py --check  # versioni e maturità del catalogo sono aggiornate
python tools/make_brand.py --check    # banner e icone sono aggiornati
python tools/publication_check.py     # niente di privato uscirebbe con una pubblicazione
bash tools/check_all.sh               # i test di ogni repository, in un'esecuzione
python -m unittest discover -s tests  # 199 test di questi strumenti; non servono altri repository
```

## 🧪 Test

| Area | Cosa copre |
|---|---|
| Il generatore di README | le otto lingue e le sezioni di ogni repository |
| Catalogo e marchio | `test_make_catalog_and_brand.py`, `test_repository_registry.py` |
| Pubblicazione | cosa è BLOCK e REVIEW, e la copia a un commit |
| Strumenti CI e avviatore | `test_ci_validate.py`, `test_sync_ci_tools.py`, `test_project_tool.py`, `test_check_all_script.py` |

GitHub Actions esegue la base A.R.M.O.R. a ogni push e pull request: la validazione di manifesto, versione, registro delle modifiche e parità dei README, poi la compilazione e i test del progetto.

## 🏗️ Compilazione e rilascio

Non c'è nulla da compilare. La versione risiede in `armor.project.json` e nel badge del README (letto dal manifesto); ogni versione ha la sua voce in [CHANGELOG.md](CHANGELOG.md). Le versioni sono pubblicate su GitHub.

## 🩺 Risoluzione dei problemi

| Vedi | Perché | Fai |
|---|---|---|
| `READMEs out of date:` + a list | è cambiata una fonte di `tools/readme_src/` o un manifesto e i README non sono stati riscritti | esegui `python tools/make_readmes.py`, guarda cosa è cambiato in ogni repository e fai commit lì |
| `Status tables incomplete:` | un repository del registro ha una tabella di stato senza le righe o i colori attesi | completa `FACTS["status"]` e le note nella sua fonte |
| Un controllo dice SKIP | manca il suo strumento o il repository accanto a questo; un controllo senza il suo strumento non è mai PASS | installa lo strumento o clona il repository accanto a questo |
| `publication_check.py` BLOCK | è stato trovato qualcosa che non deve diventare pubblico (file, riga e tipo, mai il valore) | rimuovilo e usa `clean_history.py` se è nella cronologia |

## 📂 Struttura del repository

<p align="center">
  <img src="images/repository-structure.svg" alt="Repository structure of ARMOR-DOCS" width="100%">
</p>

<details>
<summary>Versione testuale dell'albero</summary>

```text
ARMOR-DOCS/
├── tools/
│   ├── make_readmes.py                          i README da una fonte, in otto lingue
│   ├── readme_src/                              i fatti e le parole di ogni repository
│   ├── make_catalog.py make_brand.py            il catalogo; banner e icone
│   ├── brand_banner.py registry.py              il disegno del banner; l'elenco di ARMOR-COMMON
│   ├── publication_check.py                     niente di privato esce con una pubblicazione
│   ├── clean_history.py sync_ci_tools.py        una copia pubblicabile; controlli CI uguali
│   ├── check_all.sh                             i test di ogni repository in un'esecuzione
│   ├── armor_ci_validate.py                     il controllo CI di ogni repository
│   ├── armor_project_tool.py pretty_run.py      l'avviatore e il suo pannello dal vivo
│   ├── make_architecture.py make_structure.py   le due immagini dei README
│   └── universal_readme_check.py                il controllo del formato dei README
├── docs/                                        CAPABILITY_MATRIX, ARCHITECTURE, SECURITY_BASELINE, THREAT_MODEL, PROJECT_CATALOG, INTERFACES, FIRST_VERTICAL_SLICE, SETUP_CODE
├── tests/                                       i test di questi strumenti
├── brand/                                       l'emblema
├── images/                                      banner, icona, l'immagine della famiglia e le immagini di questo README
├── .github/                                     workflow CI, avviso alla dashboard, modelli per issue e pull request
├── armor.project.json                           manifesto: versione, ruolo, maturità
├── CHANGELOG.md                                 cosa è cambiato in ogni versione
├── run.sh run.bat                               avvio, flusso condiviso
├── build.sh build.bat                           compila e prova, flusso condiviso
├── build-test.sh build-test.bat                 compila, prova e impacchetta
├── test.sh test.bat                             solo i test, mai la versione
└── SECURITY.md SUPPORT.md CONTRIBUTING.md CODE_OF_CONDUCT.md LICENSE
```

</details>

## 🗺️ Roadmap e limiti noti

**Limiti noti oggi**

* La matrice delle capacità dice la verità su ciò che è stato eseguito: finché una riga non dice Verified, non ha toccato hardware reale.
* Solo il nodo radar e il banco di prova CM5 hanno girato su hardware reale.
* Nessuna revisione di sicurezza indipendente.

**Prossimi passi**

* Portare righe della matrice a Verified man mano che gli altri nodi girano sulle loro schede.

## 🌍 Lingue

Il README e i testi esistono in inglese, spagnolo, francese, italiano, tedesco, cinese, giapponese e portoghese europeo.

## 🔗 Progetti correlati

**A.R.M.O.R.** (Autonomous Radar & Multimodal Observation Range) è un sistema di sicurezza perimetrale fatto di repository indipendenti. Ognuno ha la propria versione, i propri test e il proprio README; ecco la famiglia:

* **[ARMOR-COMMON](https://github.com/JuanenRac/ARMOR-COMMON)** - Contratti dei messaggi, validatori, vettori di conformità e tipi generati
* **[ARMOR-NODE-RADAR](https://github.com/JuanenRac/ARMOR-NODE-RADAR)** - Firmware del nodo di campo per ESP32-S3 con tre radar e un proprio pannello web
* **[ARMOR-NODE-SOLAR](https://github.com/JuanenRac/ARMOR-NODE-SOLAR)** - Protocolli di inverter e batterie solari e messaggi di un nodo gateway
* **[ARMOR-NODE-ELECTRICAL](https://github.com/JuanenRac/ARMOR-NODE-ELECTRICAL)** - Nodo elettrico: contatori, il messaggio delle letture della rete e le regole di manovra
* **[ARMOR-NODE-ALARM](https://github.com/JuanenRac/ARMOR-NODE-ALARM)** - Nodo e centrale d'allarme: zone, inserimento, ritardi, sirena e PIN, con il server o senza
* **[ARMOR-NODE-HMI](https://github.com/JuanenRac/ARMOR-NODE-HMI)** - Pannello touch: lo stato del sistema su uno schermo a parete, attivare e riconoscere gli allarmi, e la casa dell'assistente vocale
* **[ARMOR-NETWORK](https://github.com/JuanenRac/ARMOR-NETWORK)** - La rete locale: i suoi dispositivi, internet e ciò che cambia
* **[ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER)** - Coordinatore centrale: telemetria, allarmi, dispositivi, letture solari e telecamere
* **[ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO)** - Console web: telecamere, radar, allarmi, energia solare e progettista del sito 2D/3D
* **[ARMOR-ANDROID-CONTROL](https://github.com/JuanenRac/ARMOR-ANDROID-CONTROL)** - Client Android dell'operatore con radar 2D/3D in tempo reale
* **[ARMOR-IOS-CONTROL](https://github.com/JuanenRac/ARMOR-IOS-CONTROL)** - Client operatore per iPhone
* **[ARMOR-SERVER-AI](https://github.com/JuanenRac/ARMOR-SERVER-AI)** - Politica di inferenza visiva che spiega le sue decisioni e non agisce mai
* **[ARMOR-VISION](https://github.com/JuanenRac/ARMOR-VISION)** - Zone delle telecamere, maschere e regole di rilevamento per la Jetson Orin NX
* **[ARMOR-VOICE-AI](https://github.com/JuanenRac/ARMOR-VOICE-AI)** - Intenti vocali offline con una conferma impossibile da falsificare
* **[ARMOR-HARDWARE](https://github.com/JuanenRac/ARMOR-HARDWARE)** - Contenitori, elettronica e matrice di accettazione da banco
* **[ARMOR-DEVOPS](https://github.com/JuanenRac/ARMOR-DEVOPS)** - Distribuzione, banco di prova CM5, backup e TLS
* **[ARMOR-SIMULATOR](https://github.com/JuanenRac/ARMOR-SIMULATOR)** - Simulatore di telemetria offline con guasti ripetibili
* **[ARMOR-UPDATER](https://github.com/JuanenRac/ARMOR-UPDATER)** - Rileva, installa e aggiorna i repository stessi dell'ecosistema
* **ARMOR-DOCS** (questo repository) - Architettura, base di sicurezza e matrice delle capacità

## 📚 Documentazione

* [ARCHITECTURE](docs/ARCHITECTURE.md): reti, confini di fiducia, tempo e ordinamento
* [SECURITY_BASELINE](docs/SECURITY_BASELINE.md): il progetto delle VLAN, cosa fa rispettare il codice e cosa manca
* [THREAT_MODEL](docs/THREAT_MODEL.md): da cosa ci si difende e da cosa no
* [INTERFACES](docs/INTERFACES.md): chi produce e consuma ogni interfaccia e dove ci si fida
* [FIRST_VERTICAL_SLICE](docs/FIRST_VERTICAL_SLICE.md): cosa prova il test dal simulatore alla console e cosa no
* [SETUP_CODE](docs/SETUP_CODE.md): il codice di configurazione dei nodi
* [Matrice delle capacità: cosa è provato e cosa no](docs/CAPABILITY_MATRIX.md)
* [Catalogo dei progetti: versioni e dipendenze tra i repository](docs/PROJECT_CATALOG.md)
* [Cronologia delle modifiche di questo repository](CHANGELOG.md)

## 🤝 Contribuire e comunità

* Prima di una pull request esegui `python -I tools/armor_ci_validate.py` e i test: devono passare entrambi. Vedi [CONTRIBUTING.md](CONTRIBUTING.md) e il [codice di condotta](CODE_OF_CONDUCT.md).
* Il README esiste in otto lingue ed è generato dalle sorgenti in ARMOR-DOCS: una modifica al testo si fa lì.
* Una modifica a un messaggio tra componenti parte da ARMOR-COMMON.
* Non descrivere come funzionante su una scheda ciò che è stato solo compilato.
* Segnala una vulnerabilità in privato: [SECURITY.md](SECURITY.md). Domande, idee e segnalazioni: electrohobby3d@gmail.com ([SUPPORT.md](SUPPORT.md)).

## 👤 AUTORE

**JuanenRac (Electro Hobby 3D)** · electrohobby3d@gmail.com

## 📜 LICENZA

GPL-3.0-or-later - vedi [LICENSE](LICENSE).
