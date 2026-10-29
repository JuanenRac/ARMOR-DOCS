<p align="center">
  <img src="images/ARMOR_BANNER.svg" alt="Bannière d'ARMOR-DOCS" width="100%">
</p>

# 📚 ARMOR-DOCS

<p align="center">
  <a href="README.md">🇺🇸 English</a> |
  <a href="README_spa.md">🇪🇸 Español</a> |
  🇫🇷 <b>Français</b> |
  <a href="README_ita.md">🇮🇹 Italiano</a> |
  <a href="README_deu.md">🇩🇪 Deutsch</a> |
  <a href="README_zho.md">🇨🇳 简体中文</a> |
  <a href="README_jpn.md">🇯🇵 日本語</a> |
  <a href="README_por.md">🇵🇹 Português</a>
</p>

### Architecture canonique, base de sécurité et vérité sur ce qui est prouvé

<p align="center">
  <img src="https://img.shields.io/badge/License-GPL%203.0--or--later-blue.svg" alt="GPL 3.0 ou ultérieure">
  <img src="https://img.shields.io/badge/Format-Markdown-083fa1.svg" alt="Format">
  <img src="https://img.shields.io/badge/Languages-8-00E5FF.svg" alt="Langues">
  <img src="https://img.shields.io/badge/Tests-199%20passing-2ea44f.svg" alt="Tests">
  <img src="https://img.shields.io/badge/Version-0.8.1.2-0f6cbd.svg" alt="Version">
  <img src="https://img.shields.io/badge/Maturity-established-2EA44F.svg" alt="Maturité">
</p>

---

**Vérification d'honnêteté - ce qui fonctionne aujourd'hui :** Ce dépôt documente des interfaces et des procédures qui ont été validées, et dit clairement ce qui ne l'a pas été. Lisez la [matrice de capacités](docs/CAPABILITY_MATRIX.md) avant de croire qu'une fonction est « faite » : elle dit pour chacune si elle a seulement été simulée, testée sur un ordinateur ou vérifiée sur du matériel réel. Les README des dix-neuf dépôts sont écrits à partir d'une seule source (`tools/readme_src/`) en huit langues, la version et la maturité de chacun étant lues dans son propre manifeste, si bien qu'ils ne peuvent pas dire autre chose que le projet.

---

## 📋 En un coup d'œil

| | |
|---|---|
| Version | `0.8.1.2` |
| Maturité | Établi |
| Rôle | Centre de documentation : architecture, base de sécurité, matrice des capacités et outils qui écrivent les README, le catalogue et les bannières |
| Technologie | Python 3.11+ (outils, bibliothèque standard), Markdown |
| Tests | 199 (`python -m unittest discover -s tests`, environ une minute) |
| Interfaces | `make_readmes.py`, `make_catalog.py`, `make_brand.py`, `publication_check.py`, `clean_history.py`, `sync_ci_tools.py`, `check_all.sh` |
| Fonctionne sur | Tout ordinateur avec Python ; les dépôts de la famille à côté de celui-ci |
| Sur matériel réel | Sans objet : c'est de la documentation ; elle consigne ce que les autres dépôts ont fait tourner sur du matériel réel |
| Licence | GPL-3.0-or-later |

**Aller à :** [Présentation](#-présentation) · [Architecture](#-architecture) · [Sécurité](#-sécurité-et-protection) · [Interfaces](#-interfaces) · [Démarrage rapide](#-démarrage-rapide) · [Tests](#-tests) · [Dépannage](#-dépannage) · [Structure](#-structure-du-dépôt) · [Liés](#-projets-liés)

## 🚦 État du projet

Chaque ligne est une partie de ce dépôt et le feu dit où elle en est aujourd'hui. Elle est écrite d'après ce que le dépôt peut montrer (tests, compilations, exécutions), pas d'après ce qui est prévu.

🟢 Fait et vérifié · 🟡 Fonctionne, avec des limites connues · 🟠 À moitié fait ou pas encore vérifié · 🔴 Pas fait ou ne fonctionne pas

| Domaine | État | Ce que cela veut dire ici |
|---|---|---|
| Logiciel | 🟢 | Les générateurs de README, de bannières, de catalogue et de matrice de capacités, et les outils de CI copiés dans chaque dépôt, fonctionnent et sont testés. |
| Tests | 🟢 | Les 199 tests des outils réussissent (`python -m unittest discover -s tests`) : le contrôle de publication, le nettoyeur d'historique, les générateurs de README, catalogue et marque, la copie des outils CI et l'outil du flux partagé. |
| Contrôles automatiques | 🟢 | Chaque push vérifie que les README, les bannières et le catalogue sont à jour et que chaque dépôt du registre a son tableau d'état. |
| Intégration | 🟢 | Les README de tous les dépôts sont écrits à partir d'une seule source, avec la version et la maturité de chacun lues dans son propre manifeste. |
| Documentation | 🟢 | La matrice de capacités dit, pour chaque fonction, si elle n'a été que simulée, testée sur un ordinateur ou vérifiée sur du matériel réel ; les huit langues et le journal des modifications sont à jour. |

## 🎯 Présentation

<p align="center">
  <img src="images/ARMOR_FAMILY.svg" alt="A.R.M.O.R. family" width="100%">
</p>

* [Matrice de capacités](docs/CAPABILITY_MATRIX.md) : pour chaque capacité, est-elle simulée, testée sur un ordinateur ou vérifiée sur du matériel ?
* [Architecture](docs/ARCHITECTURE.md) : réseaux, frontières de confiance, temps et ordre.
* [Base de sécurité](docs/SECURITY_BASELINE.md) : la conception des VLAN, ce que le code impose et ce qui manque encore ; et le [modèle de menaces](docs/THREAT_MODEL.md).
* [Catalogue de projets](docs/PROJECT_CATALOG.md) : les dix-neuf dépôts, leurs versions et leurs dépendances.
* [Interfaces](docs/INTERFACES.md) : qui produit et consomme chaque interface et où on lui fait confiance.
* [Première tranche verticale](docs/FIRST_VERTICAL_SLICE.md) : ce que prouve le test du simulateur à la console et ce qu'il ne prouve pas.
* **Outils :** `make_readmes.py` écrit le README de chaque dépôt dans les huit langues à partir de `readme_src/`, `make_catalog.py` écrit les versions du catalogue, `make_brand.py` sa bannière et son icône, `publication_check.py` cherche tout ce qui est privé avant une publication, `clean_history.py` fait une copie publiable d'un dépôt et `sync_ci_tools.py` garde égaux les contrôles de CI de la famille.

## 🧩 Rôle dans A.R.M.O.R.

ARMOR-DOCS est la mémoire de la famille : c'est là que vivent l'architecture, la base de sécurité et la matrice de capacités, et l'endroit qui dit, pour chaque dépôt, ce qui a vraiment tourné sur du matériel. Il garde aussi l'outil qui écrit les README des dix-neuf dépôts à partir d'une seule source, pour que les huit langues ne dérivent pas.

| Il parle à | Comment | Pour quoi faire |
|---|---|---|
| Chaque dépôt de la famille | leur `armor.project.json` et leurs fichiers README | les outils lisent la version et la maturité et écrivent le README, la bannière et les copies CI |
| ARMOR-COMMON | `registry/repositories.json` | la liste unique des dépôts de la famille, lue par `registry.py` |
| Qui publie | `publication_check.py`  `clean_history.py` | ce qui fuirait et une copie en un seul commit publiable |

## 🏛️ Architecture

<p align="center">
  <img src="images/architecture.svg" alt="ARMOR-DOCS architecture: what the tools read, the tools themselves and what they write in every repository" width="100%">
</p>

## 🔒 Sécurité et protection

| Menace | Défense |
|---|---|
| Publier quelque chose de privé | `publication_check.py` ne lit que git (fichiers versionnés et historique, jamais les ignorés) et n'imprime jamais le secret. BLOCK : une clé privée, une adresse IP publique, une adresse e-mail personnelle, un `secrets/` ou `.env` versionné, un commit avec coauteur ou ligne d'IA, un auteur de commit autre que celui du projet ; REVIEW : une ligne qui ressemble à un mot de passe ou jeton en clair ; sortie 1 en cas de BLOCK |
| Un historique avec des restes | `clean_history.py` fait une copie publiable d'un dépôt avec un seul commit fait par l'auteur du projet |
| Affirmer plus que ce qui est prouvé | `docs/CAPABILITY_MATRIX.md` a trois niveaux (Simulated, Local, Verified) plus None, Absent et Local-not-activated ; seules les lignes Verified ont touché du matériel (le banc d'essai CM5 en usage quotidien) |
| Un README qui dit autre chose que le projet | La version et la maturité de chaque README sont lues dans son propre manifeste ; chaque push vérifie que les README, les bannières et le catalogue sont à jour et que chaque dépôt du registre a son tableau d'état |

Les documents de sécurité de la famille sont [docs/SECURITY_BASELINE.md](docs/SECURITY_BASELINE.md) (la conception des VLAN, ce que le code fait respecter et ce qui manque encore) et [docs/THREAT_MODEL.md](docs/THREAT_MODEL.md). Rien de cela ne prouve l'absence d'un secret.

## 🔌 Interfaces

| Route | Authentification | Ce qu'elle fait |
|---|---|---|
| `python tools/make_readmes.py [--check]` | - | écrit le README de chaque dépôt en huit langues depuis `tools/readme_src/` ; `--check` échoue si l'un est périmé. Il réécrit tous les fichiers : changez la source, jamais les README |
| `python tools/make_catalog.py [--check]`  `make_brand.py [--check]` | - | les versions et la maturité de `docs/PROJECT_CATALOG.md`, et les bannières et icônes |
| `python tools/publication_check.py [REPO] [--no-history] [--ref=BRANCH]` | - | ce qui fuirait si les dépôts étaient publiés ; sortie 1 en cas de BLOCK |
| `python tools/clean_history.py` | - | une copie publiable d'un dépôt avec un seul commit |
| `python tools/sync_ci_tools.py [--check]` | - | copie les vérifications CI et le lanceur dans chaque dépôt ; `--check` échoue si une copie a dérivé |
| `bash tools/check_all.sh [--android] [--compose]` | - | les tests de chaque dépôt en un lancement ; un contrôle sans son outil est SKIP, jamais PASS |

La source de chaque README est `tools/readme_src/repos/<DÉPÔT>.py` (les faits indépendants de la langue et les mots des huit langues), avec `ui.py` pour les mots autour de chaque README et `shots.py` pour les captures. `tools/registry.py` lit la liste des dépôts d'ARMOR-COMMON. Voir aussi [docs/INTERFACES.md](docs/INTERFACES.md) et [docs/SETUP_CODE.md](docs/SETUP_CODE.md).

## 🚀 Démarrage rapide

**Prérequis :** Python 3.11+ pour les outils (bibliothèque standard seule) ; les dépôts de la famille à côté de celui-ci pour les vérifications qui les lisent.

```bash
python tools/make_readmes.py --check  # les README (8 langues) sont à jour
python tools/make_catalog.py --check  # les versions et la maturité du catalogue sont à jour
python tools/make_brand.py --check    # les bannières et icônes sont à jour
python tools/publication_check.py     # rien de privé ne sortirait avec une publication
bash tools/check_all.sh               # les tests de chaque dépôt, en un lancement
python -m unittest discover -s tests  # 199 tests de ces outils ; ils n'ont besoin d'aucun autre dépôt
```

## 🧪 Tests

| Domaine | Ce qu'il couvre |
|---|---|
| Le générateur de README | les huit langues et les sections de chaque dépôt |
| Catalogue et marque | `test_make_catalog_and_brand.py`, `test_repository_registry.py` |
| Publication | ce qui est BLOCK et REVIEW, et la copie à un commit |
| Outils CI et lanceur | `test_ci_validate.py`, `test_sync_ci_tools.py`, `test_project_tool.py`, `test_check_all_script.py` |

GitHub Actions exécute la base A.R.M.O.R. à chaque push et pull request : la validation du manifeste, de la version, du journal des modifications et de la parité des README, puis le build et les tests propres au projet.

## 🏗️ Compilation et publication

Il n'y a rien à compiler. La version se trouve dans `armor.project.json` et dans le badge du README (lu depuis le manifeste) ; chaque version a son entrée dans [CHANGELOG.md](CHANGELOG.md). Les versions sont publiées sur GitHub.

## 🩺 Dépannage

| Vous voyez | Parce que | Faites |
|---|---|---|
| `READMEs out of date:` + a list | une source de `tools/readme_src/` ou un manifeste a changé et les README n'ont pas été réécrits | lancez `python tools/make_readmes.py`, regardez ce qui a changé dans chaque dépôt et validez là |
| `Status tables incomplete:` | un dépôt du registre a un tableau d'état sans les lignes ou couleurs attendues | complétez `FACTS["status"]` et les notes dans sa source |
| Un contrôle dit SKIP | son outil ou le dépôt à côté de celui-ci manque ; un contrôle sans son outil n'est jamais PASS | installez l'outil ou clonez le dépôt à côté de celui-ci |
| `publication_check.py` BLOCK | quelque chose qui ne doit pas devenir public a été trouvé (fichier, ligne et genre, jamais la valeur) | retirez-le et utilisez `clean_history.py` s'il est dans l'historique |

## 📂 Structure du dépôt

<p align="center">
  <img src="images/repository-structure.svg" alt="Repository structure of ARMOR-DOCS" width="100%">
</p>

<details>
<summary>Version texte de l'arborescence</summary>

```text
ARMOR-DOCS/
├── tools/
│   ├── make_readmes.py                          les README depuis une source, en huit langues
│   ├── readme_src/                              les faits et les mots de chaque dépôt
│   ├── make_catalog.py make_brand.py            le catalogue ; bannières et icônes
│   ├── brand_banner.py registry.py              le dessin de la bannière ; la liste d'ARMOR-COMMON
│   ├── publication_check.py                     rien de privé ne sort avec une publication
│   ├── clean_history.py sync_ci_tools.py        une copie publiable ; vérifications CI égales
│   ├── check_all.sh                             les tests de chaque dépôt en un lancement
│   ├── armor_ci_validate.py                     la vérification CI de chaque dépôt
│   ├── armor_project_tool.py pretty_run.py      le lanceur et son panneau en direct
│   ├── make_architecture.py make_structure.py   les deux images des README
│   └── universal_readme_check.py                la vérification de mise en page des README
├── docs/                                        CAPABILITY_MATRIX, ARCHITECTURE, SECURITY_BASELINE, THREAT_MODEL, PROJECT_CATALOG, INTERFACES, FIRST_VERTICAL_SLICE, SETUP_CODE
├── tests/                                       les tests de ces outils
├── brand/                                       l'emblème
├── images/                                      bannière, icône, l'image de la famille et les images de ce README
├── .github/                                     workflow CI, avis au tableau de bord, modèles d'issues et de pull requests
├── armor.project.json                           manifeste : version, rôle, maturité
├── CHANGELOG.md                                 ce qui a changé à chaque version
├── run.sh run.bat                               démarrer, flux partagé
├── build.sh build.bat                           construire et tester, flux partagé
├── build-test.sh build-test.bat                 construire, tester, empaqueter
├── test.sh test.bat                             seulement les tests, jamais la version
└── SECURITY.md SUPPORT.md CONTRIBUTING.md CODE_OF_CONDUCT.md LICENSE
```

</details>

## 🗺️ Feuille de route et limites connues

**Limites connues aujourd'hui**

* La matrice des capacités dit la vérité sur ce qui a tourné : tant qu'une ligne ne dit pas Verified, elle n'a pas touché de vrai matériel.
* Seuls le nœud radar et le banc d'essai CM5 ont tourné sur du vrai matériel.
* Pas de revue de sécurité indépendante.

**Prochainement**

* Passer des lignes de la matrice à Verified à mesure que les autres nœuds tournent sur leurs cartes.

## 🌍 Langues

Le README et les textes existent en anglais, espagnol, français, italien, allemand, chinois, japonais et portugais européen.

## 🔗 Projets liés

**A.R.M.O.R.** (Autonomous Radar & Multimodal Observation Range) est un système de sécurité périmétrique composé de dépôts indépendants. Chacun a sa propre version, ses propres tests et son propre README ; voici la famille :

* **[ARMOR-COMMON](https://github.com/JuanenRac/ARMOR-COMMON)** - Contrats de messages, validateurs, vecteurs de conformité et types générés
* **[ARMOR-NODE-RADAR](https://github.com/JuanenRac/ARMOR-NODE-RADAR)** - Firmware du nœud de terrain pour ESP32-S3 avec trois radars et son propre panneau web
* **[ARMOR-NODE-SOLAR](https://github.com/JuanenRac/ARMOR-NODE-SOLAR)** - Protocoles des onduleurs et batteries solaires et messages d'un nœud passerelle
* **[ARMOR-NODE-ELECTRICAL](https://github.com/JuanenRac/ARMOR-NODE-ELECTRICAL)** - Nœud électrique : compteurs, le message des mesures du réseau et les règles de commutation
* **[ARMOR-NODE-ALARM](https://github.com/JuanenRac/ARMOR-NODE-ALARM)** - Nœud et centrale d'alarme : zones, armement, temporisations, sirène et PIN, avec ou sans le serveur
* **[ARMOR-NODE-HMI](https://github.com/JuanenRac/ARMOR-NODE-HMI)** - Panneau tactile : l'état du système sur un écran mural, armer et acquitter, et la maison de l'assistant vocal
* **[ARMOR-NETWORK](https://github.com/JuanenRac/ARMOR-NETWORK)** - Le réseau local : ses appareils, internet et ce qui change
* **[ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER)** - Coordinateur central : télémétrie, alarmes, appareils, relevés solaires et caméras
* **[ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO)** - Console web : caméras, radar, alarmes, énergie solaire et concepteur de site 2D/3D
* **[ARMOR-ANDROID-CONTROL](https://github.com/JuanenRac/ARMOR-ANDROID-CONTROL)** - Client Android de l'opérateur avec radar 2D/3D en direct
* **[ARMOR-IOS-CONTROL](https://github.com/JuanenRac/ARMOR-IOS-CONTROL)** - Client opérateur iPhone
* **[ARMOR-SERVER-AI](https://github.com/JuanenRac/ARMOR-SERVER-AI)** - Politique d'inférence visuelle qui explique ses décisions et n'agit jamais
* **[ARMOR-VISION](https://github.com/JuanenRac/ARMOR-VISION)** - Zones de caméra, masques et règles de détection pour la Jetson Orin NX
* **[ARMOR-VOICE-AI](https://github.com/JuanenRac/ARMOR-VOICE-AI)** - Intentions vocales hors ligne avec une confirmation impossible à falsifier
* **[ARMOR-HARDWARE](https://github.com/JuanenRac/ARMOR-HARDWARE)** - Boîtiers, électronique et matrice d'acceptation sur banc
* **[ARMOR-DEVOPS](https://github.com/JuanenRac/ARMOR-DEVOPS)** - Déploiement, banc d'essai CM5, sauvegarde et TLS
* **[ARMOR-SIMULATOR](https://github.com/JuanenRac/ARMOR-SIMULATOR)** - Simulateur de télémétrie hors ligne avec des pannes reproductibles
* **[ARMOR-UPDATER](https://github.com/JuanenRac/ARMOR-UPDATER)** - Détecte, installe et met à jour les propres dépôts de l'écosystème
* **ARMOR-DOCS** (ce dépôt) - Architecture, base de sécurité et matrice des capacités

## 📚 Documentation

* [ARCHITECTURE](docs/ARCHITECTURE.md) : réseaux, frontières de confiance, temps et ordre
* [SECURITY_BASELINE](docs/SECURITY_BASELINE.md) : la conception des VLAN, ce que le code fait respecter et ce qui manque
* [THREAT_MODEL](docs/THREAT_MODEL.md) : contre quoi on se défend et contre quoi non
* [INTERFACES](docs/INTERFACES.md) : qui produit et consomme chaque interface et où on lui fait confiance
* [FIRST_VERTICAL_SLICE](docs/FIRST_VERTICAL_SLICE.md) : ce que prouve le test du simulateur à la console et ce qu'il ne prouve pas
* [SETUP_CODE](docs/SETUP_CODE.md) : le code de configuration des nœuds
* [Matrice des capacités : ce qui est prouvé et ce qui ne l'est pas](docs/CAPABILITY_MATRIX.md)
* [Catalogue des projets : versions et dépendances entre les dépôts](docs/PROJECT_CATALOG.md)
* [Historique des modifications de ce dépôt](CHANGELOG.md)

## 🤝 Contribuer et communauté

* Avant une pull request, exécutez `python -I tools/armor_ci_validate.py` et les tests : les deux doivent réussir. Voir [CONTRIBUTING.md](CONTRIBUTING.md) et le [code de conduite](CODE_OF_CONDUCT.md).
* Le README existe en huit langues et est généré à partir des sources d'ARMOR-DOCS : une modification du texte se fait là-bas.
* Une modification d'un message entre composants commence dans ARMOR-COMMON.
* Ne décrivez pas comme fonctionnant sur une carte ce qui a seulement été compilé.
* Signalez une vulnérabilité en privé : [SECURITY.md](SECURITY.md). Questions, idées et rapports : electrohobby3d@gmail.com ([SUPPORT.md](SUPPORT.md)).

## 👤 AUTEUR

**JuanenRac (Electro Hobby 3D)** · electrohobby3d@gmail.com

## 📜 LICENCE

GPL-3.0-or-later - voir [LICENSE](LICENSE).
