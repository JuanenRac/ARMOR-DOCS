# The facts that do not depend on the language, and the words of every language, of ARMOR-DOCS, in the universal README layout.
# Copyright (C) 2026 JuanenRac (Electro Hobby 3D). GPL-3.0-or-later.
from readme_src._kit import *  # noqa: F401,F403

FACTS = {'emoji': '📚',
 'layout': 'universal',
 'license_badge': 'License-GPL%203.0--or--later-blue',
 'status': [['software', 'green'], ['ci', 'green'], ['integration', 'green'], ['docs', 'green']],
 'badges': [['Format', 'Markdown', '083fa1'], ['Languages', '8', '00E5FF']]}

# the sentences of the previous layout that the new one keeps (already written in the eight languages)
LEGACY = {'en': {'tagline': 'Canonical architecture, security baseline and the truth about what is proven',
        'status': {'software': 'The generators for the READMEs, the banners, the catalogue and the capability matrix, and the CI tools copied into every repository, run '
                               'and are tested.',
                   'ci': 'Every push checks that the READMEs, the banners and the catalogue are up to date and that every repository of the registry has its status '
                         'table.',
                   'integration': 'The READMEs of all the repositories are written from one source with the version and the maturity of each read from its own manifest.',
                   'docs': 'The capability matrix says for each feature whether it was only simulated, tested on a computer or verified on real hardware; the eight '
                           'languages and the changelog are up to date.'},
        'honest': 'This repository documents interfaces and procedures that have been validated, and it says plainly what has not. Read the [capability '
                  'matrix](docs/CAPABILITY_MATRIX.md) before believing any feature is "done": it says for each one whether it was only simulated, tested on a computer '
                  'or verified on real hardware. The READMEs of the nineteen repositories are written from one source (`tools/readme_src/`) in eight languages, with the '
                  'version and the maturity of each read from its own manifest, so they cannot say something different from the project.',
        'bullets': ['[Capability matrix](docs/CAPABILITY_MATRIX.md): for each capability, is it simulated, tested on a computer or verified on hardware?',
                    '[Architecture](docs/ARCHITECTURE.md): networks, trust boundaries, time and ordering.',
                    '[Security baseline](docs/SECURITY_BASELINE.md): the VLAN design, what the code enforces and what is still missing; and the [threat '
                    'model](docs/THREAT_MODEL.md).',
                    '[Project catalogue](docs/PROJECT_CATALOG.md): the nineteen repositories, their versions and how they depend on each other.',
                    '[Interfaces](docs/INTERFACES.md): who produces and consumes each interface and where it is trusted.',
                    '[First vertical slice](docs/FIRST_VERTICAL_SLICE.md): what the simulator-to-console test proves and what it does not.',
                    '**Tools:** `make_readmes.py` writes the README of every repository in the eight languages from `readme_src/`, `make_catalog.py` writes the versions '
                    'of the catalogue, `make_brand.py` its banner and icon, `publication_check.py` looks for anything private before a publication, `clean_history.py` '
                    'makes a publishable copy of a repository and `sync_ci_tools.py` keeps the CI checks of the family equal, ruff and mypy included (pinned versions, only where a repository has a mypy configuration; `"ci_lint": false` in its manifest skips them).'],
        'intro': '<p align="center">\n  <img src="images/ARMOR_FAMILY.svg" alt="A.R.M.O.R. family" width="100%">\n</p>',
        'fit': "ARMOR-DOCS is the family's memory: it is where the architecture, the security baseline and the capability matrix live, and the place that says, for "
               'every repository, what has really run on hardware. It also holds the tool that writes the READMEs of all nineteen repositories from one source, so that '
               'the eight languages cannot drift apart.',
        'hardware': 'Not applicable: it is documentation; it records what the other repositories have run on real hardware'},
 'es': {'tagline': 'Arquitectura canónica, base de seguridad y la verdad sobre lo que está probado',
        'status': {'software': 'Los generadores de READMEs, banners, catálogo y matriz de capacidades, y las herramientas de CI copiadas a cada repositorio, funcionan y '
                               'están probados.',
                   'ci': 'Cada push comprueba que los READMEs, los banners y el catálogo estén al día y que cada repositorio del registro tenga su tabla de estado.',
                   'integration': 'Los READMEs de todos los repositorios se escriben desde una sola fuente, con la versión y la madurez de cada uno leídas de su propio '
                                  'manifiesto.',
                   'docs': 'La matriz de capacidades dice, para cada función, si solo se simuló, se probó en un ordenador o se verificó en hardware real; los ocho '
                           'idiomas y el historial de cambios están al día.'},
        'honest': 'Este repositorio documenta interfaces y procedimientos que se han validado, y dice claramente lo que no. Lee la [matriz de '
                  'capacidades](docs/CAPABILITY_MATRIX.md) antes de creer que una función está "hecha": dice de cada una si solo se simuló, se probó en un ordenador o '
                  'se verificó en hardware real. Los README de los diecinueve repositorios se escriben desde una sola fuente (`tools/readme_src/`) en ocho idiomas, con '
                  'la versión y la madurez de cada uno leídas de su propio manifiesto, de modo que no pueden decir algo distinto del proyecto.',
        'bullets': ['[Matriz de capacidades](docs/CAPABILITY_MATRIX.md): de cada capacidad, ¿está simulada, probada en un ordenador o verificada en hardware?',
                    '[Arquitectura](docs/ARCHITECTURE.md): redes, límites de confianza, tiempo y orden.',
                    '[Base de seguridad](docs/SECURITY_BASELINE.md): el diseño de VLAN, lo que el código hace cumplir y lo que aún falta; y el [modelo de '
                    'amenazas](docs/THREAT_MODEL.md).',
                    '[Catálogo de proyectos](docs/PROJECT_CATALOG.md): los diecinueve repositorios, sus versiones y cómo dependen unos de otros.',
                    '[Interfaces](docs/INTERFACES.md): quién produce y consume cada interfaz y dónde se confía en ella.',
                    '[Primera rebanada vertical](docs/FIRST_VERTICAL_SLICE.md): qué demuestra la prueba del simulador a la consola y qué no.',
                    '**Herramientas:** `make_readmes.py` escribe el README de cada repositorio en los ocho idiomas desde `readme_src/`, `make_catalog.py` escribe las '
                    'versiones del catálogo, `make_brand.py` su banner e icono, `publication_check.py` busca cualquier cosa privada antes de una publicación, '
                    '`clean_history.py` hace una copia publicable de un repositorio y `sync_ci_tools.py` mantiene iguales las comprobaciones de CI de la familia, ruff y mypy incluidos (versiones fijadas, solo donde un repositorio tiene configuración de mypy; `"ci_lint": false` en su manifiesto los omite).'],
        'intro': '<p align="center">\n  <img src="images/ARMOR_FAMILY.svg" alt="A.R.M.O.R. family" width="100%">\n</p>',
        'fit': 'ARMOR-DOCS es la memoria de la familia: es donde viven la arquitectura, la base de seguridad y la matriz de capacidades, y el lugar que dice, de cada '
               'repositorio, qué ha corrido de verdad en hardware. También guarda la herramienta que escribe los README de los diecinueve repositorios desde una sola '
               'fuente, para que los ocho idiomas no se separen.',
        'hardware': 'No aplica: es documentación; registra lo que los demás repositorios han corrido en hardware real',
        'requirements': ['Python 3.11+ para las herramientas']},
 'fr': {'tagline': 'Architecture canonique, base de sécurité et vérité sur ce qui est prouvé',
        'status': {'software': 'Les générateurs de README, de bannières, de catalogue et de matrice de capacités, et les outils de CI copiés dans chaque dépôt, '
                               'fonctionnent et sont testés.',
                   'ci': "Chaque push vérifie que les README, les bannières et le catalogue sont à jour et que chaque dépôt du registre a son tableau d'état.",
                   'integration': "Les README de tous les dépôts sont écrits à partir d'une seule source, avec la version et la maturité de chacun lues dans son propre "
                                  'manifeste.',
                   'docs': "La matrice de capacités dit, pour chaque fonction, si elle n'a été que simulée, testée sur un ordinateur ou vérifiée sur du matériel réel ; "
                           'les huit langues et le journal des modifications sont à jour.'},
        'honest': "Ce dépôt documente des interfaces et des procédures qui ont été validées, et dit clairement ce qui ne l'a pas été. Lisez la [matrice de "
                  "capacités](docs/CAPABILITY_MATRIX.md) avant de croire qu'une fonction est « faite » : elle dit pour chacune si elle a seulement été simulée, testée "
                  "sur un ordinateur ou vérifiée sur du matériel réel. Les README des dix-neuf dépôts sont écrits à partir d'une seule source (`tools/readme_src/`) en "
                  "huit langues, la version et la maturité de chacun étant lues dans son propre manifeste, si bien qu'ils ne peuvent pas dire autre chose que le projet.",
        'bullets': ['[Matrice de capacités](docs/CAPABILITY_MATRIX.md) : pour chaque capacité, est-elle simulée, testée sur un ordinateur ou vérifiée sur du matériel ?',
                    '[Architecture](docs/ARCHITECTURE.md) : réseaux, frontières de confiance, temps et ordre.',
                    '[Base de sécurité](docs/SECURITY_BASELINE.md) : la conception des VLAN, ce que le code impose et ce qui manque encore ; et le [modèle de '
                    'menaces](docs/THREAT_MODEL.md).',
                    '[Catalogue de projets](docs/PROJECT_CATALOG.md) : les dix-neuf dépôts, leurs versions et leurs dépendances.',
                    '[Interfaces](docs/INTERFACES.md) : qui produit et consomme chaque interface et où on lui fait confiance.',
                    "[Première tranche verticale](docs/FIRST_VERTICAL_SLICE.md) : ce que prouve le test du simulateur à la console et ce qu'il ne prouve pas.",
                    '**Outils :** `make_readmes.py` écrit le README de chaque dépôt dans les huit langues à partir de `readme_src/`, `make_catalog.py` écrit les '
                    'versions du catalogue, `make_brand.py` sa bannière et son icône, `publication_check.py` cherche tout ce qui est privé avant une publication, '
                    "`clean_history.py` fait une copie publiable d'un dépôt et `sync_ci_tools.py` garde égaux les contrôles de CI de la famille, ruff et mypy compris (versions fixées, seulement là où un dépôt a une configuration mypy ; `\"ci_lint\": false` dans son manifeste les saute)."],
        'intro': '<p align="center">\n  <img src="images/ARMOR_FAMILY.svg" alt="A.R.M.O.R. family" width="100%">\n</p>',
        'fit': "ARMOR-DOCS est la mémoire de la famille : c'est là que vivent l'architecture, la base de sécurité et la matrice de capacités, et l'endroit qui dit, pour "
               "chaque dépôt, ce qui a vraiment tourné sur du matériel. Il garde aussi l'outil qui écrit les README des dix-neuf dépôts à partir d'une seule source, "
               'pour que les huit langues ne dérivent pas.',
        'hardware': "Sans objet : c'est de la documentation ; elle consigne ce que les autres dépôts ont fait tourner sur du matériel réel",
        'requirements': ['Python 3.11+ pour les outils']},
 'it': {'tagline': 'Architettura canonica, base di sicurezza e la verità su ciò che è provato',
        'status': {'software': 'I generatori di README, banner, catalogo e matrice delle capacità, e gli strumenti di CI copiati in ogni repository, funzionano e sono '
                               'testati.',
                   'ci': 'Ogni push verifica che i README, i banner e il catalogo siano aggiornati e che ogni repository del registro abbia la sua tabella di stato.',
                   'integration': "I README di tutti i repository sono scritti da un'unica fonte, con la versione e la maturità di ciascuno lette dal proprio manifesto.",
                   'docs': 'La matrice delle capacità dice, per ogni funzione, se è stata solo simulata, testata su un computer o verificata su hardware reale; le otto '
                           'lingue e il registro delle modifiche sono aggiornati.'},
        'honest': 'Questo repository documenta interfacce e procedure che sono state validate, e dice chiaramente ciò che non lo è. Leggi la [matrice delle '
                  'capacità](docs/CAPABILITY_MATRIX.md) prima di credere che una funzione sia "fatta": dice per ciascuna se è stata solo simulata, provata su un '
                  "computer o verificata su hardware reale. I README dei diciannove repository sono scritti da un'unica fonte (`tools/readme_src/`) in otto lingue, con "
                  'la versione e la maturità di ciascuno lette dal suo manifesto, così non possono dire qualcosa di diverso dal progetto.',
        'bullets': ['[Matrice delle capacità](docs/CAPABILITY_MATRIX.md): per ogni capacità, è simulata, provata su un computer o verificata su hardware?',
                    '[Architettura](docs/ARCHITECTURE.md): reti, confini di fiducia, tempo e ordine.',
                    '[Base di sicurezza](docs/SECURITY_BASELINE.md): il progetto delle VLAN, ciò che il codice impone e ciò che manca ancora; e il [modello delle '
                    'minacce](docs/THREAT_MODEL.md).',
                    "[Catalogo dei progetti](docs/PROJECT_CATALOG.md): i diciannove repository, le loro versioni e come dipendono l'uno dall'altro.",
                    '[Interfacce](docs/INTERFACES.md): chi produce e consuma ogni interfaccia e dove ci si fida.',
                    '[Prima fetta verticale](docs/FIRST_VERTICAL_SLICE.md): cosa dimostra il test dal simulatore alla console e cosa no.',
                    '**Strumenti:** `make_readmes.py` scrive il README di ogni repository nelle otto lingue da `readme_src/`, `make_catalog.py` scrive le versioni del '
                    "catalogo, `make_brand.py` il suo banner e l'icona, `publication_check.py` cerca qualsiasi cosa privata prima di una pubblicazione, "
                    '`clean_history.py` fa una copia pubblicabile di un repository e `sync_ci_tools.py` mantiene uguali i controlli di CI della famiglia, ruff e mypy compresi (versioni fissate, solo dove un repository ha una configurazione di mypy; `"ci_lint": false` nel manifesto li salta).'],
        'intro': '<p align="center">\n  <img src="images/ARMOR_FAMILY.svg" alt="A.R.M.O.R. family" width="100%">\n</p>',
        'fit': "ARMOR-DOCS è la memoria della famiglia: è dove vivono l'architettura, la base di sicurezza e la matrice delle capacità, e il luogo che dice, per ogni "
               "repository, cosa ha davvero girato su hardware. Tiene anche lo strumento che scrive i README di tutti e diciannove i repository da un'unica fonte, "
               'perché le otto lingue non divergano.',
        'hardware': 'Non applicabile: è documentazione; registra ciò che gli altri repository hanno fatto girare su hardware reale',
        'requirements': ['Python 3.11+ per gli strumenti']},
 'de': {'tagline': 'Kanonische Architektur, Sicherheitsgrundlage und die Wahrheit darüber, was belegt ist',
        'status': {'software': 'Die Generatoren für READMEs, Banner, Katalog und Fähigkeitenmatrix sowie die in jedes Repository kopierten CI-Werkzeuge laufen und sind '
                               'getestet.',
                   'ci': 'Jeder Push prüft, dass die READMEs, die Banner und der Katalog aktuell sind und dass jedes Repository des Registers seine Statustabelle hat.',
                   'integration': 'Die READMEs aller Repositorys entstehen aus einer Quelle, wobei Version und Reifegrad jedes Repositorys aus dessen eigenem Manifest '
                                  'gelesen werden.',
                   'docs': 'Die Fähigkeitenmatrix sagt für jede Funktion, ob sie nur simuliert, auf einem Rechner getestet oder an echter Hardware überprüft wurde; die '
                           'acht Sprachen und das Änderungsprotokoll sind aktuell.'},
        'honest': 'Dieses Repository dokumentiert Schnittstellen und Verfahren, die validiert wurden, und sagt klar, was nicht. Lesen Sie die '
                  '[Fähigkeitsmatrix](docs/CAPABILITY_MATRIX.md), bevor Sie glauben, eine Funktion sei "fertig": Sie sagt für jede, ob sie nur simuliert, auf einem '
                  'Computer getestet oder auf echter Hardware verifiziert wurde. Die READMEs der neunzehn Repositorys werden aus einer einzigen Quelle '
                  '(`tools/readme_src/`) in acht Sprachen geschrieben, wobei Version und Reifegrad jedes Projekts aus seinem eigenen Manifest gelesen werden, sodass sie '
                  'nichts anderes sagen können als das Projekt.',
        'bullets': ['[Fähigkeitsmatrix](docs/CAPABILITY_MATRIX.md): ist jede Fähigkeit simuliert, auf einem Computer getestet oder auf Hardware verifiziert?',
                    '[Architektur](docs/ARCHITECTURE.md): Netze, Vertrauensgrenzen, Zeit und Reihenfolge.',
                    '[Sicherheitsgrundlage](docs/SECURITY_BASELINE.md): der VLAN-Entwurf, was der Code durchsetzt und was noch fehlt; und das '
                    '[Bedrohungsmodell](docs/THREAT_MODEL.md).',
                    '[Projektkatalog](docs/PROJECT_CATALOG.md): die neunzehn Repositorys, ihre Versionen und wie sie voneinander abhängen.',
                    '[Schnittstellen](docs/INTERFACES.md): wer jede Schnittstelle erzeugt und nutzt und wo ihr vertraut wird.',
                    '[Erster vertikaler Schnitt](docs/FIRST_VERTICAL_SLICE.md): was der Test vom Simulator zur Konsole beweist und was nicht.',
                    '**Werkzeuge:** `make_readmes.py` schreibt das README jedes Repositorys in den acht Sprachen aus `readme_src/`, `make_catalog.py` schreibt die '
                    'Versionen des Katalogs, `make_brand.py` sein Banner und Symbol, `publication_check.py` sucht vor einer Veröffentlichung nach allem Privaten, '
                    '`clean_history.py` macht eine veröffentlichbare Kopie eines Repositorys und `sync_ci_tools.py` hält die CI-Prüfungen der Familie gleich, auch ruff und mypy (feste Versionen, nur wo ein Repository eine mypy-Konfiguration hat; `"ci_lint": false` im Manifest überspringt sie).'],
        'intro': '<p align="center">\n  <img src="images/ARMOR_FAMILY.svg" alt="A.R.M.O.R. family" width="100%">\n</p>',
        'fit': 'ARMOR-DOCS ist das Gedächtnis der Familie: Hier leben die Architektur, die Sicherheitsgrundlage und die Fähigkeitsmatrix, und es ist der Ort, der für '
               'jedes Repository sagt, was wirklich auf Hardware gelaufen ist. Es hält auch das Werkzeug, das die READMEs aller neunzehn Repositorys aus einer Quelle '
               'schreibt, damit die acht Sprachen nicht auseinanderlaufen.',
        'hardware': 'Nicht zutreffend: es ist Dokumentation; sie hält fest, was die anderen Repositorys auf echter Hardware ausgeführt haben',
        'requirements': ['Python 3.11+ für die Werkzeuge']},
 'zh': {'tagline': '规范的架构、安全基线，以及关于哪些已被证实的真相',
        'status': {'software': 'README、横幅、目录和能力矩阵的生成器，以及复制到每个仓库中的 CI 工具都能运行并经过测试。',
                   'ci': '每次推送都会检查 README、横幅和目录是否为最新，以及注册表中的每个仓库是否都有状态表。',
                   'integration': '所有仓库的 README 都由同一份源文件生成，每个仓库的版本和成熟度均读取自其自身的清单。',
                   'docs': '能力矩阵为每项功能说明它只是被模拟、在电脑上测试过，还是在真实硬件上验证过；八种语言和更新日志均为最新。'},
        'honest': '本仓库记录已验证的接口和流程，并明确说明哪些尚未验证。在相信某项功能“已完成”之前，请先阅读[能力矩阵](docs/CAPABILITY_MATRIX.md)：它对每一项说明它只是模拟过、在计算机上测试过，还是在真实硬件上验证过。十九个仓库的 README '
                  '来自同一个来源（`tools/readme_src/`），以八种语言编写，每个项目的版本和成熟度都读自它自己的清单，因此不会与项目说的不一样。',
        'bullets': ['[能力矩阵](docs/CAPABILITY_MATRIX.md)：每项能力是模拟的、在计算机上测试的，还是在硬件上验证的？',
                    '[架构](docs/ARCHITECTURE.md)：网络、信任边界、时间和顺序。',
                    '[安全基线](docs/SECURITY_BASELINE.md)：VLAN 设计、代码强制实施的内容以及仍然缺少的内容；以及[威胁模型](docs/THREAT_MODEL.md)。',
                    '[项目目录](docs/PROJECT_CATALOG.md)：十九个仓库、它们的版本以及相互依赖关系。',
                    '[接口](docs/INTERFACES.md)：谁产生和使用每个接口，以及在哪里被信任。',
                    '[第一个垂直切片](docs/FIRST_VERTICAL_SLICE.md)：从模拟器到控制台的测试证明了什么、没有证明什么。',
                    '**工具：**`make_readmes.py` 从 `readme_src/` 以八种语言写出每个仓库的 README，`make_catalog.py` 写出目录中的版本，`make_brand.py` 写出其横幅和图标，`publication_check.py` '
                    '在发布前查找任何私有内容，`clean_history.py` 制作仓库的可发布副本，`sync_ci_tools.py` 让家族的 CI 检查保持一致，其中包括 ruff 和 mypy（版本固定，仅在仓库有 mypy 配置时运行；清单中的 `"ci_lint": false` 会跳过它们）。'],
        'intro': '<p align="center">\n  <img src="images/ARMOR_FAMILY.svg" alt="A.R.M.O.R. family" width="100%">\n</p>',
        'fit': 'ARMOR-DOCS 是家族的记忆：架构、安全基线和能力矩阵都在这里，也是说明每个仓库究竟在硬件上运行过什么的地方。它还保存着从同一个来源编写全部十九个仓库 README 的工具，使八种语言不会各行其是。',
        'hardware': '不适用：这是文档；它记录其他仓库在真实硬件上运行过的内容',
        'requirements': ['用于工具的 Python 3.11+']},
 'ja': {'tagline': '正典のアーキテクチャ、セキュリティ基準、そして何が実証されているかの真実',
        'status': {'software': 'README、バナー、カタログ、機能マトリクスのジェネレーターと、各リポジトリにコピーする CI ツールは動作し、テスト済みです。',
                   'ci': 'プッシュのたびに、README、バナー、カタログが最新であること、そしてレジストリのすべてのリポジトリに状況の表があることを確認します。',
                   'integration': 'すべてのリポジトリの README は 1 つのソースから作られ、各リポジトリのバージョンと成熟度はそれぞれのマニフェストから読み取ります。',
                   'docs': '機能マトリクスは、各機能がシミュレーションのみか、コンピューターでテスト済みか、実機で検証済みかを示します。8 言語と変更履歴は最新です。'},
        'honest': 'このリポジトリは検証済みのインターフェースと手順を文書化し、検証されていないものは率直に述べます。ある機能が「完成」と信じる前に[能力マトリクス](docs/CAPABILITY_MATRIX.md)を読んでください。各機能が、シミュレーションのみ、コンピューター上でのテスト、実機での検証のどれかを示しています。19 '
                  'のリポジトリの README は 1 つのソース（`tools/readme_src/`）から 8 言語で作られ、各プロジェクトのバージョンと成熟度は自身のマニフェストから読み取るため、プロジェクトと違うことは書けません。',
        'bullets': ['[能力マトリクス](docs/CAPABILITY_MATRIX.md)：各能力はシミュレーションのみか、コンピューター上でテスト済みか、実機で検証済みか。',
                    '[アーキテクチャ](docs/ARCHITECTURE.md)：ネットワーク、信頼境界、時刻と順序。',
                    '[セキュリティベースライン](docs/SECURITY_BASELINE.md)：VLAN 設計、コードが強制するもの、まだ足りないもの。[脅威モデル](docs/THREAT_MODEL.md)も。',
                    '[プロジェクトカタログ](docs/PROJECT_CATALOG.md)：19 のリポジトリ、そのバージョン、互いの依存関係。',
                    '[インターフェース](docs/INTERFACES.md)：各インターフェースを誰が生成・利用し、どこで信頼されるか。',
                    '[最初の垂直スライス](docs/FIRST_VERTICAL_SLICE.md)：シミュレーターからコンソールまでのテストが証明するものとしないもの。',
                    '**ツール：**`make_readmes.py` は `readme_src/` から全リポジトリの README を 8 言語で作り、`make_catalog.py` はカタログのバージョンを書き、`make_brand.py` '
                    'はバナーとアイコン、`publication_check.py` は公開前に非公開のものを探し、`clean_history.py` は公開用のコピーを作り、`sync_ci_tools.py` はファミリーの CI 検査を揃え、ruff と mypy も含みます（バージョン固定、mypy の設定があるリポジトリのみ。マニフェストの `"ci_lint": false` で省略できます）。'],
        'intro': '<p align="center">\n  <img src="images/ARMOR_FAMILY.svg" alt="A.R.M.O.R. family" width="100%">\n</p>',
        'fit': 'ARMOR-DOCS はファミリーの記憶です。アーキテクチャ、セキュリティベースライン、能力マトリクスがここにあり、各リポジトリで実際に実機で動いたものを示す場所です。19 のリポジトリすべての README を 1 つのソースから書くツールもここにあり、8 言語がずれないようにしています。',
        'hardware': '該当なし：ドキュメントで、他のリポジトリが実機で動かしたものを記録します',
        'requirements': ['ツール用の Python 3.11+']},
 'pt': {'tagline': 'Arquitetura canónica, linha de base de segurança e a verdade sobre o que está provado',
        'status': {'software': 'Os geradores de READMEs, faixas, catálogo e matriz de capacidades, e as ferramentas de CI copiadas para cada repositório, funcionam e '
                               'estão testados.',
                   'ci': 'Cada push verifica que os READMEs, as faixas e o catálogo estão atualizados e que cada repositório do registo tem a sua tabela de estado.',
                   'integration': 'Os READMEs de todos os repositórios são escritos a partir de uma só fonte, com a versão e a maturidade de cada um lidas do seu '
                                  'próprio manifesto.',
                   'docs': 'A matriz de capacidades diz, para cada função, se foi apenas simulada, testada num computador ou verificada em hardware real; os oito '
                           'idiomas e o registo de alterações estão atualizados.'},
        'honest': 'Este repositório documenta interfaces e procedimentos que foram validados, e diz claramente o que não foi. Leia a [matriz de '
                  'capacidades](docs/CAPABILITY_MATRIX.md) antes de acreditar que uma funcionalidade está "feita": diz de cada uma se foi apenas simulada, testada num '
                  'computador ou verificada em hardware real. Os README dos dezanove repositórios são escritos a partir de uma única fonte (`tools/readme_src/`) em oito '
                  'idiomas, com a versão e a maturidade de cada um lidas do seu próprio manifesto, pelo que não podem dizer algo diferente do projeto.',
        'bullets': ['[Matriz de capacidades](docs/CAPABILITY_MATRIX.md): de cada capacidade, está simulada, testada num computador ou verificada em hardware?',
                    '[Arquitetura](docs/ARCHITECTURE.md): redes, limites de confiança, tempo e ordem.',
                    '[Base de segurança](docs/SECURITY_BASELINE.md): o desenho de VLAN, o que o código impõe e o que ainda falta; e o [modelo de '
                    'ameaças](docs/THREAT_MODEL.md).',
                    '[Catálogo de projetos](docs/PROJECT_CATALOG.md): os dezanove repositórios, as suas versões e como dependem uns dos outros.',
                    '[Interfaces](docs/INTERFACES.md): quem produz e consome cada interface e onde se confia nela.',
                    '[Primeira fatia vertical](docs/FIRST_VERTICAL_SLICE.md): o que o teste do simulador à consola prova e o que não prova.',
                    '**Ferramentas:** `make_readmes.py` escreve o README de cada repositório nos oito idiomas a partir de `readme_src/`, `make_catalog.py` escreve as '
                    'versões do catálogo, `make_brand.py` o seu banner e ícone, `publication_check.py` procura qualquer coisa privada antes de uma publicação, '
                    '`clean_history.py` faz uma cópia publicável de um repositório e `sync_ci_tools.py` mantém iguais as verificações de CI da família, incluindo ruff e mypy (versões fixas, apenas onde um repositório tem configuração do mypy; `"ci_lint": false` no manifesto ignora-as).'],
        'intro': '<p align="center">\n  <img src="images/ARMOR_FAMILY.svg" alt="A.R.M.O.R. family" width="100%">\n</p>',
        'fit': 'O ARMOR-DOCS é a memória da família: é onde vivem a arquitetura, a base de segurança e a matriz de capacidades, e o sítio que diz, de cada repositório, '
               'o que correu mesmo em hardware. Guarda também a ferramenta que escreve os README dos dezanove repositórios a partir de uma só fonte, para que os oito '
               'idiomas não se separem.',
        'hardware': 'Não se aplica: é documentação; regista o que os outros repositórios correram em hardware real',
        'requirements': ['Python 3.11+ para as ferramentas']}}

# the text tree of docs/structure.json (make_structure.py --tree <language>); the repository's own check fails when it and the file disagree
TREE = {'en': 'ARMOR-DOCS/\n'
       '├── tools/\n'
       '│   ├── make_readmes.py                          the READMEs, from one source, in eight languages\n'
       '│   ├── readme_src/                              the facts and the words of each repository\n'
       '│   ├── make_catalog.py make_brand.py            the catalogue; the banners and icons\n'
       '│   ├── brand_banner.py registry.py              the banner drawing; the list of ARMOR-COMMON\n'
       '│   ├── publication_check.py                     nothing private leaves with a publication\n'
       '│   ├── clean_history.py sync_ci_tools.py        a publishable copy; equal CI checks\n'
       "│   ├── check_all.sh                             every repository's tests in one run\n"
       '│   ├── armor_ci_validate.py                     the CI check every repository carries\n'
       '│   ├── armor_project_tool.py pretty_run.py      the launcher and its live panel\n'
       '│   ├── make_architecture.py make_structure.py   the two pictures of the READMEs\n'
       '│   └── universal_readme_check.py                the layout check of the READMEs\n'
       '├── docs/                                        CAPABILITY_MATRIX, ARCHITECTURE, SECURITY_BASELINE, THREAT_MODEL, PROJECT_CATALOG, INTERFACES, '
       'FIRST_VERTICAL_SLICE, SETUP_CODE\n'
       '├── tests/                                       the tests of these tools\n'
       '├── brand/                                       the emblem\n'
       '├── images/                                      banner, icon, the family picture and the pictures of this README\n'
       '├── .github/                                     CI workflow, dashboard notice, issue and pull-request templates\n'
       '├── armor.project.json                           manifest: version, role, maturity\n'
       '├── CHANGELOG.md                                 what changed in each version\n'
       '├── run.sh run.bat                               start, shared workflow\n'
       '├── build.sh build.bat                           build and test, shared workflow\n'
       '├── build-test.sh build-test.bat                 build, test and package\n'
       '├── test.sh test.bat                             only the tests, never the version\n'
       '└── SECURITY.md SUPPORT.md CONTRIBUTING.md CODE_OF_CONDUCT.md LICENSE',
 'es': 'ARMOR-DOCS/\n'
       '├── tools/\n'
       '│   ├── make_readmes.py                          los README, desde una fuente, en ocho idiomas\n'
       '│   ├── readme_src/                              los datos y las palabras de cada repositorio\n'
       '│   ├── make_catalog.py make_brand.py            el catálogo; los banners e iconos\n'
       '│   ├── brand_banner.py registry.py              el dibujo del banner; la lista de ARMOR-COMMON\n'
       '│   ├── publication_check.py                     nada privado sale con una publicación\n'
       '│   ├── clean_history.py sync_ci_tools.py        una copia publicable; comprobaciones de CI iguales\n'
       '│   ├── check_all.sh                             las pruebas de cada repositorio de una vez\n'
       '│   ├── armor_ci_validate.py                     la comprobación de CI que lleva cada repositorio\n'
       '│   ├── armor_project_tool.py pretty_run.py      el lanzador y su panel en vivo\n'
       '│   ├── make_architecture.py make_structure.py   las dos imágenes de los README\n'
       '│   └── universal_readme_check.py                la comprobación del formato de los README\n'
       '├── docs/                                        CAPABILITY_MATRIX, ARCHITECTURE, SECURITY_BASELINE, THREAT_MODEL, PROJECT_CATALOG, INTERFACES, '
       'FIRST_VERTICAL_SLICE, SETUP_CODE\n'
       '├── tests/                                       las pruebas de estas herramientas\n'
       '├── brand/                                       el emblema\n'
       '├── images/                                      banner, icono, la imagen de la familia y las imágenes de este README\n'
       '├── .github/                                     flujo de CI, aviso al panel, plantillas de incidencias y pull requests\n'
       '├── armor.project.json                           manifiesto: versión, función, madurez\n'
       '├── CHANGELOG.md                                 qué cambió en cada versión\n'
       '├── run.sh run.bat                               arrancar, flujo compartido\n'
       '├── build.sh build.bat                           construir y probar, flujo compartido\n'
       '├── build-test.sh build-test.bat                 construir, probar y empaquetar\n'
       '├── test.sh test.bat                             solo las pruebas, nunca la versión\n'
       '└── SECURITY.md SUPPORT.md CONTRIBUTING.md CODE_OF_CONDUCT.md LICENSE',
 'de': 'ARMOR-DOCS/\n'
       '├── tools/\n'
       '│   ├── make_readmes.py                          die READMEs aus einer Quelle, in acht Sprachen\n'
       '│   ├── readme_src/                              die Fakten und Worte jedes Repositorys\n'
       '│   ├── make_catalog.py make_brand.py            der Katalog; Banner und Symbole\n'
       '│   ├── brand_banner.py registry.py              die Banner-Zeichnung; die Liste von ARMOR-COMMON\n'
       '│   ├── publication_check.py                     nichts Privates verlässt das Haus\n'
       '│   ├── clean_history.py sync_ci_tools.py        eine veröffentlichbare Kopie; gleiche CI-Prüfungen\n'
       '│   ├── check_all.sh                             die Tests jedes Repositorys in einem Lauf\n'
       '│   ├── armor_ci_validate.py                     die CI-Prüfung jedes Repositorys\n'
       '│   ├── armor_project_tool.py pretty_run.py      der Starter und sein Live-Panel\n'
       '│   ├── make_architecture.py make_structure.py   die zwei Bilder der READMEs\n'
       '│   └── universal_readme_check.py                die Layout-Prüfung der READMEs\n'
       '├── docs/                                        CAPABILITY_MATRIX, ARCHITECTURE, SECURITY_BASELINE, THREAT_MODEL, PROJECT_CATALOG, INTERFACES, '
       'FIRST_VERTICAL_SLICE, SETUP_CODE\n'
       '├── tests/                                       die Tests dieser Werkzeuge\n'
       '├── brand/                                       das Emblem\n'
       '├── images/                                      Banner, Symbol, das Familienbild und die Bilder dieses READMEs\n'
       '├── .github/                                     CI-Workflow, Dashboard-Hinweis, Vorlagen für Issues und Pull Requests\n'
       '├── armor.project.json                           Manifest: Version, Rolle, Reife\n'
       '├── CHANGELOG.md                                 was sich in jeder Version geändert hat\n'
       '├── run.sh run.bat                               Start, gemeinsamer Ablauf\n'
       '├── build.sh build.bat                           Bauen und Testen, gemeinsamer Ablauf\n'
       '├── build-test.sh build-test.bat                 Bauen, Testen und Verpacken\n'
       '├── test.sh test.bat                             nur die Tests, nie die Version\n'
       '└── SECURITY.md SUPPORT.md CONTRIBUTING.md CODE_OF_CONDUCT.md LICENSE',
 'fr': 'ARMOR-DOCS/\n'
       '├── tools/\n'
       '│   ├── make_readmes.py                          les README depuis une source, en huit langues\n'
       '│   ├── readme_src/                              les faits et les mots de chaque dépôt\n'
       '│   ├── make_catalog.py make_brand.py            le catalogue ; bannières et icônes\n'
       "│   ├── brand_banner.py registry.py              le dessin de la bannière ; la liste d'ARMOR-COMMON\n"
       '│   ├── publication_check.py                     rien de privé ne sort avec une publication\n'
       '│   ├── clean_history.py sync_ci_tools.py        une copie publiable ; vérifications CI égales\n'
       '│   ├── check_all.sh                             les tests de chaque dépôt en un lancement\n'
       '│   ├── armor_ci_validate.py                     la vérification CI de chaque dépôt\n'
       '│   ├── armor_project_tool.py pretty_run.py      le lanceur et son panneau en direct\n'
       '│   ├── make_architecture.py make_structure.py   les deux images des README\n'
       '│   └── universal_readme_check.py                la vérification de mise en page des README\n'
       '├── docs/                                        CAPABILITY_MATRIX, ARCHITECTURE, SECURITY_BASELINE, THREAT_MODEL, PROJECT_CATALOG, INTERFACES, '
       'FIRST_VERTICAL_SLICE, SETUP_CODE\n'
       '├── tests/                                       les tests de ces outils\n'
       "├── brand/                                       l'emblème\n"
       "├── images/                                      bannière, icône, l'image de la famille et les images de ce README\n"
       "├── .github/                                     workflow CI, avis au tableau de bord, modèles d'issues et de pull requests\n"
       '├── armor.project.json                           manifeste : version, rôle, maturité\n'
       '├── CHANGELOG.md                                 ce qui a changé à chaque version\n'
       '├── run.sh run.bat                               démarrer, flux partagé\n'
       '├── build.sh build.bat                           construire et tester, flux partagé\n'
       '├── build-test.sh build-test.bat                 construire, tester, empaqueter\n'
       '├── test.sh test.bat                             seulement les tests, jamais la version\n'
       '└── SECURITY.md SUPPORT.md CONTRIBUTING.md CODE_OF_CONDUCT.md LICENSE',
 'it': 'ARMOR-DOCS/\n'
       '├── tools/\n'
       '│   ├── make_readmes.py                          i README da una fonte, in otto lingue\n'
       '│   ├── readme_src/                              i fatti e le parole di ogni repository\n'
       '│   ├── make_catalog.py make_brand.py            il catalogo; banner e icone\n'
       "│   ├── brand_banner.py registry.py              il disegno del banner; l'elenco di ARMOR-COMMON\n"
       '│   ├── publication_check.py                     niente di privato esce con una pubblicazione\n'
       '│   ├── clean_history.py sync_ci_tools.py        una copia pubblicabile; controlli CI uguali\n'
       "│   ├── check_all.sh                             i test di ogni repository in un'esecuzione\n"
       '│   ├── armor_ci_validate.py                     il controllo CI di ogni repository\n'
       "│   ├── armor_project_tool.py pretty_run.py      l'avviatore e il suo pannello dal vivo\n"
       '│   ├── make_architecture.py make_structure.py   le due immagini dei README\n'
       '│   └── universal_readme_check.py                il controllo del formato dei README\n'
       '├── docs/                                        CAPABILITY_MATRIX, ARCHITECTURE, SECURITY_BASELINE, THREAT_MODEL, PROJECT_CATALOG, INTERFACES, '
       'FIRST_VERTICAL_SLICE, SETUP_CODE\n'
       '├── tests/                                       i test di questi strumenti\n'
       "├── brand/                                       l'emblema\n"
       "├── images/                                      banner, icona, l'immagine della famiglia e le immagini di questo README\n"
       '├── .github/                                     workflow CI, avviso alla dashboard, modelli per issue e pull request\n'
       '├── armor.project.json                           manifesto: versione, ruolo, maturità\n'
       '├── CHANGELOG.md                                 cosa è cambiato in ogni versione\n'
       '├── run.sh run.bat                               avvio, flusso condiviso\n'
       '├── build.sh build.bat                           compila e prova, flusso condiviso\n'
       '├── build-test.sh build-test.bat                 compila, prova e impacchetta\n'
       '├── test.sh test.bat                             solo i test, mai la versione\n'
       '└── SECURITY.md SUPPORT.md CONTRIBUTING.md CODE_OF_CONDUCT.md LICENSE',
 'ja': 'ARMOR-DOCS/\n'
       '├── tools/\n'
       '│   ├── make_readmes.py                          1 つのソースから 8 言語の README\n'
       '│   ├── readme_src/                              各リポジトリの事実と文言\n'
       '│   ├── make_catalog.py make_brand.py            カタログ、バナーとアイコン\n'
       '│   ├── brand_banner.py registry.py              バナーの描画、ARMOR-COMMON の一覧\n'
       '│   ├── publication_check.py                     公開物に非公開情報を含めない\n'
       '│   ├── clean_history.py sync_ci_tools.py        公開用コピー、同一の CI 検査\n'
       '│   ├── check_all.sh                             各リポジトリのテストを一度に\n'
       '│   ├── armor_ci_validate.py                     各リポジトリが持つ CI 検査\n'
       '│   ├── armor_project_tool.py pretty_run.py      ランチャーとライブパネル\n'
       '│   ├── make_architecture.py make_structure.py   README の 2 つの図\n'
       '│   └── universal_readme_check.py                README のレイアウト検査\n'
       '├── docs/                                        '
       'CAPABILITY_MATRIX、ARCHITECTURE、SECURITY_BASELINE、THREAT_MODEL、PROJECT_CATALOG、INTERFACES、FIRST_VERTICAL_SLICE、SETUP_CODE\n'
       '├── tests/                                       これらのツールのテスト\n'
       '├── brand/                                       エンブレム\n'
       '├── images/                                      バナー、アイコン、ファミリーの図、この README の図\n'
       '├── .github/                                     CI ワークフロー、ダッシュボード通知、Issue と Pull Request のテンプレート\n'
       '├── armor.project.json                           マニフェスト：版・役割・成熟度\n'
       '├── CHANGELOG.md                                 各バージョンの変更点\n'
       '├── run.sh run.bat                               起動（共通フロー）\n'
       '├── build.sh build.bat                           ビルドとテスト（共通フロー）\n'
       '├── build-test.sh build-test.bat                 ビルド、テスト、パッケージ化\n'
       '├── test.sh test.bat                             テストのみ（版は変えません）\n'
       '└── SECURITY.md SUPPORT.md CONTRIBUTING.md CODE_OF_CONDUCT.md LICENSE',
 'zh': 'ARMOR-DOCS/\n'
       '├── tools/\n'
       '│   ├── make_readmes.py                          由单一来源生成八种语言 README\n'
       '│   ├── readme_src/                              每个仓库的事实与文字\n'
       '│   ├── make_catalog.py make_brand.py            目录；横幅图与图标\n'
       '│   ├── brand_banner.py registry.py              横幅图绘制；ARMOR-COMMON 的清单\n'
       '│   ├── publication_check.py                     发布时不泄露私有内容\n'
       '│   ├── clean_history.py sync_ci_tools.py        可发布的副本；统一的 CI 检查\n'
       '│   ├── check_all.sh                             一次运行每个仓库的测试\n'
       '│   ├── armor_ci_validate.py                     每个仓库自带的 CI 检查\n'
       '│   ├── armor_project_tool.py pretty_run.py      启动器及其实时面板\n'
       '│   ├── make_architecture.py make_structure.py   README 的两张图\n'
       '│   └── universal_readme_check.py                README 版式检查\n'
       '├── docs/                                        '
       'CAPABILITY_MATRIX、ARCHITECTURE、SECURITY_BASELINE、THREAT_MODEL、PROJECT_CATALOG、INTERFACES、FIRST_VERTICAL_SLICE、SETUP_CODE\n'
       '├── tests/                                       这些工具的测试\n'
       '├── brand/                                       徽标\n'
       '├── images/                                      横幅图、图标、家族图和本 README 的图片\n'
       '├── .github/                                     CI 工作流、仪表板通知、议题和 pull request 模板\n'
       '├── armor.project.json                           清单：版本、角色、成熟度\n'
       '├── CHANGELOG.md                                 每个版本的变化\n'
       '├── run.sh run.bat                               启动（共用流程）\n'
       '├── build.sh build.bat                           构建并测试（共用流程）\n'
       '├── build-test.sh build-test.bat                 构建、测试并打包\n'
       '├── test.sh test.bat                             只运行测试，不改版本\n'
       '└── SECURITY.md SUPPORT.md CONTRIBUTING.md CODE_OF_CONDUCT.md LICENSE',
 'pt': 'ARMOR-DOCS/\n'
       '├── tools/\n'
       '│   ├── make_readmes.py                          os README a partir de uma fonte, em oito idiomas\n'
       '│   ├── readme_src/                              os factos e as palavras de cada repositório\n'
       '│   ├── make_catalog.py make_brand.py            o catálogo; as faixas e os ícones\n'
       '│   ├── brand_banner.py registry.py              o desenho da faixa; a lista do ARMOR-COMMON\n'
       '│   ├── publication_check.py                     nada privado sai com uma publicação\n'
       '│   ├── clean_history.py sync_ci_tools.py        uma cópia publicável; verificações de CI iguais\n'
       '│   ├── check_all.sh                             os testes de cada repositório numa execução\n'
       '│   ├── armor_ci_validate.py                     a verificação de CI de cada repositório\n'
       '│   ├── armor_project_tool.py pretty_run.py      o lançador e o seu painel em direto\n'
       '│   ├── make_architecture.py make_structure.py   as duas imagens dos README\n'
       '│   └── universal_readme_check.py                a verificação do formato dos README\n'
       '├── docs/                                        CAPABILITY_MATRIX, ARCHITECTURE, SECURITY_BASELINE, THREAT_MODEL, PROJECT_CATALOG, INTERFACES, '
       'FIRST_VERTICAL_SLICE, SETUP_CODE\n'
       '├── tests/                                       os testes destas ferramentas\n'
       '├── brand/                                       o emblema\n'
       '├── images/                                      faixa, ícone, a imagem da família e as imagens deste README\n'
       '├── .github/                                     fluxo de CI, aviso ao painel, modelos de issues e pull requests\n'
       '├── armor.project.json                           manifesto: versão, função, maturidade\n'
       '├── CHANGELOG.md                                 o que mudou em cada versão\n'
       '├── run.sh run.bat                               arrancar, fluxo partilhado\n'
       '├── build.sh build.bat                           compilar e testar, fluxo partilhado\n'
       '├── build-test.sh build-test.bat                 compilar, testar e empacotar\n'
       '├── test.sh test.bat                             só os testes, nunca a versão\n'
       '└── SECURITY.md SUPPORT.md CONTRIBUTING.md CODE_OF_CONDUCT.md LICENSE'}

DIAGRAM = ''

NT = "199"
FACTS["badges"] = [x for x in FACTS["badges"] if x[0] != "Tests"] + [["Tests", NT + "%20passing", "2ea44f"]]
FACTS["status"] = [x for x in FACTS["status"] if x[0] != "tests"]
FACTS["status"].insert(1, ["tests", "green"])


def L(lg, key):
    return LEGACY[lg][key]


TESTS_NOTE = P("The 199 tests of the tools pass (`python -m unittest discover -s tests`): the publication check, the history cleaner, the README, catalogue and brand generators, the copy of the CI tools and the shared workflow tool.",
               "Pasan las 199 pruebas de las herramientas (`python -m unittest discover -s tests`): la comprobación de publicación, el limpiador de historial, los generadores de README, catálogo y marca, la copia de las herramientas de CI y la herramienta del flujo compartido.",
               "Die 199 Tests der Werkzeuge bestehen (`python -m unittest discover -s tests`): die Veröffentlichungsprüfung, der Verlaufsbereiniger, die Generatoren für README, Katalog und Marke, die Kopie der CI-Werkzeuge und das Werkzeug des gemeinsamen Ablaufs.",
               "Les 199 tests des outils réussissent (`python -m unittest discover -s tests`) : le contrôle de publication, le nettoyeur d'historique, les générateurs de README, catalogue et marque, la copie des outils CI et l'outil du flux partagé.",
               "I 199 test degli strumenti passano (`python -m unittest discover -s tests`): il controllo di pubblicazione, il pulitore della cronologia, i generatori di README, catalogo e marchio, la copia degli strumenti CI e lo strumento del flusso condiviso.",
               "ツールの 199 件のテストが通ります（`python -m unittest discover -s tests`）：公開前検査、履歴クリーナー、README・カタログ・ブランドのジェネレーター、CI ツールのコピー、共通ワークフローツール。",
               "这些工具的 199 项测试通过（`python -m unittest discover -s tests`）：发布检查、历史清理器、README、目录和品牌的生成器、CI 工具的副本以及共用流程工具。",
               "Os 199 testes das ferramentas passam (`python -m unittest discover -s tests`): a verificação de publicação, o limpador de histórico, os geradores de README, catálogo e marca, a cópia das ferramentas de CI e a ferramenta do fluxo partilhado.")
status_tests = P(*[t for t in TESTS_NOTE.values()])

GLANCE = [
    (GL["role"], T("Documentation hub: architecture, security baseline, capability matrix, and the tools that write the READMEs, catalogue and banners | Centro de documentación: arquitectura, base de seguridad, matriz de capacidades y las herramientas que escriben los README, el catálogo y los banners | Dokumentationszentrale: Architektur, Sicherheitsbasis, Fähigkeitsmatrix und die Werkzeuge, die READMEs, Katalog und Banner schreiben | Centre de documentation : architecture, base de sécurité, matrice des capacités et outils qui écrivent les README, le catalogue et les bannières | Centro di documentazione: architettura, base di sicurezza, matrice delle capacità e gli strumenti che scrivono README, catalogo e banner | ドキュメントの拠点：アーキテクチャ、セキュリティ基盤、機能マトリクス、README・カタログ・バナーを書くツール | 文档中心：架构、安全基线、能力矩阵，以及生成 README、目录和横幅图的工具 | Centro de documentação: arquitetura, base de segurança, matriz de capacidades e as ferramentas que escrevem os README, o catálogo e as faixas")),
    (GL["stack"], T("Python 3.11+ (tools, standard library), Markdown | Python 3.11+ (herramientas, biblioteca estándar), Markdown | Python 3.11+ (Werkzeuge, Standardbibliothek), Markdown | Python 3.11+ (outils, bibliothèque standard), Markdown | Python 3.11+ (strumenti, libreria standard), Markdown | Python 3.11+（ツール、標準ライブラリ）、Markdown | Python 3.11+（工具，标准库）、Markdown | Python 3.11+ (ferramentas, biblioteca padrão), Markdown")),
    (GL["tests"], T("199 (`python -m unittest discover -s tests`, about a minute) | 199 (`python -m unittest discover -s tests`, cerca de un minuto) | 199 (`python -m unittest discover -s tests`, etwa eine Minute) | 199 (`python -m unittest discover -s tests`, environ une minute) | 199 (`python -m unittest discover -s tests`, circa un minuto) | 199 件（`python -m unittest discover -s tests`、約 1 分） | 199 项（`python -m unittest discover -s tests`，约一分钟） | 199 (`python -m unittest discover -s tests`, cerca de um minuto)")),
    (GL["interfaces"], T("`make_readmes.py`, `make_catalog.py`, `make_brand.py`, `publication_check.py`, `clean_history.py`, `sync_ci_tools.py`, `check_all.sh` | `make_readmes.py`, `make_catalog.py`, `make_brand.py`, `publication_check.py`, `clean_history.py`, `sync_ci_tools.py`, `check_all.sh` | `make_readmes.py`, `make_catalog.py`, `make_brand.py`, `publication_check.py`, `clean_history.py`, `sync_ci_tools.py`, `check_all.sh` | `make_readmes.py`, `make_catalog.py`, `make_brand.py`, `publication_check.py`, `clean_history.py`, `sync_ci_tools.py`, `check_all.sh` | `make_readmes.py`, `make_catalog.py`, `make_brand.py`, `publication_check.py`, `clean_history.py`, `sync_ci_tools.py`, `check_all.sh` | `make_readmes.py`、`make_catalog.py`、`make_brand.py`、`publication_check.py`、`clean_history.py`、`sync_ci_tools.py`、`check_all.sh` | `make_readmes.py`、`make_catalog.py`、`make_brand.py`、`publication_check.py`、`clean_history.py`、`sync_ci_tools.py`、`check_all.sh` | `make_readmes.py`, `make_catalog.py`, `make_brand.py`, `publication_check.py`, `clean_history.py`, `sync_ci_tools.py`, `check_all.sh`")),
    (GL["runs"], T("Any computer with Python; the repositories of the family next to this one | Cualquier ordenador con Python; los repositorios de la familia junto a este | Jeder Computer mit Python; die Repositorys der Familie neben diesem | Tout ordinateur avec Python ; les dépôts de la famille à côté de celui-ci | Qualsiasi computer con Python; i repository della famiglia accanto a questo | Python のある任意のコンピューター（ファミリーのリポジトリをこの隣に置く） | 装有 Python 的任意计算机；家族的各仓库放在本仓库旁边 | Qualquer computador com Python; os repositórios da família ao lado deste")),
    (GL["hardware"], {lg: LEGACY[lg]["hardware"] for lg in LGS}),
    (GL["license"], LICENSE_VALUE),
]

ROLE_TABLE = [
    (T("Every repository of the family | Cada repositorio de la familia | Jedes Repository der Familie | Chaque dépôt de la famille | Ogni repository della famiglia | ファミリーの全リポジトリ | 家族的每个仓库 | Cada repositório da família"), T("their `armor.project.json` and their README files | su `armor.project.json` y sus ficheros README | ihre `armor.project.json` und ihre README-Dateien | leur `armor.project.json` et leurs fichiers README | il loro `armor.project.json` e i file README | 各 `armor.project.json` と README ファイル | 其 `armor.project.json` 和 README 文件 | o seu `armor.project.json` e os seus ficheiros README"), T("the tools read the version and the maturity and write the README, the banner and the CI copies | las herramientas leen la versión y la madurez y escriben el README, el banner y las copias de CI | die Werkzeuge lesen Version und Reife und schreiben README, Banner und CI-Kopien | les outils lisent la version et la maturité et écrivent le README, la bannière et les copies CI | gli strumenti leggono versione e maturità e scrivono README, banner e copie CI | ツールがバージョンと成熟度を読み、README、バナー、CI コピーを書く | 工具读取版本和成熟度，写出 README、横幅图和 CI 副本 | as ferramentas leem a versão e a maturidade e escrevem o README, a faixa e as cópias de CI")),
    ("ARMOR-COMMON", T("`registry/repositories.json` | `registry/repositories.json` | `registry/repositories.json` | `registry/repositories.json` | `registry/repositories.json` | `registry/repositories.json` | `registry/repositories.json` | `registry/repositories.json`"), T("the one list of the repositories of the family, read by `registry.py` | la lista única de repositorios de la familia, leída por `registry.py` | die eine Liste der Repositorys der Familie, gelesen von `registry.py` | la liste unique des dépôts de la famille, lue par `registry.py` | l'unico elenco dei repository della famiglia, letto da `registry.py` | ファミリーのリポジトリの唯一の一覧（`registry.py` が読む） | 家族仓库的唯一清单，由 `registry.py` 读取 | a lista única dos repositórios da família, lida por `registry.py`")),
    (T("The person who publishes | Quien publica | Wer veröffentlicht | Qui publie | Chi pubblica | 公開する人 | 发布者 | Quem publica"), "`publication_check.py`  `clean_history.py`", T("what would leak, and a copy of one commit that can be published | lo que se filtraría y una copia de un solo commit que se puede publicar | was durchsickern würde und eine veröffentlichbare Kopie mit einem Commit | ce qui fuirait et une copie en un seul commit publiable | ciò che trapelerebbe e una copia a un solo commit pubblicabile | 漏れるものと、公開できる 1 コミットのコピー | 会泄露什么，以及可发布的单提交副本 | o que vazaria e uma cópia de um só commit que se pode publicar")),
]


def S(a, b):
    return (T(a), T(b))


SECURITY_ROWS = [
    S("Publishing something private | Publicar algo privado | Etwas Privates veröffentlichen | Publier quelque chose de privé | Pubblicare qualcosa di privato | 非公開情報の公開 | 发布私有内容 | Publicar algo privado",
      "`publication_check.py` reads only git (tracked files and history, never ignored files) and never prints the secret. BLOCK: a private key, a public IP address, a personal e-mail address, a tracked `secrets/` or `.env`, a commit with a co-author or an AI trailer, a commit author other than the project's; REVIEW: a line that looks like a literal password or token; it exits 1 on any BLOCK | `publication_check.py` solo lee git (ficheros versionados e historial, nunca los ignorados) y nunca imprime el secreto. BLOCK: una clave privada, una IP pública, un correo personal, un `secrets/` o `.env` versionado, un commit con coautor o cola de IA, un autor de commit distinto del del proyecto; REVIEW: una línea que parece una contraseña o token literal; sale con 1 ante cualquier BLOCK | `publication_check.py` liest nur git (versionierte Dateien und Verlauf, nie ignorierte) und gibt das Geheimnis nie aus. BLOCK: ein privater Schlüssel, eine öffentliche IP-Adresse, eine persönliche E-Mail-Adresse, ein versioniertes `secrets/` oder `.env`, ein Commit mit Co-Autor oder KI-Zeile, ein Commit-Autor, der nicht der des Projekts ist; REVIEW: eine Zeile, die wie ein Klartext-Passwort oder -Token aussieht; Ausstieg mit 1 bei jedem BLOCK | `publication_check.py` ne lit que git (fichiers versionnés et historique, jamais les ignorés) et n'imprime jamais le secret. BLOCK : une clé privée, une adresse IP publique, une adresse e-mail personnelle, un `secrets/` ou `.env` versionné, un commit avec coauteur ou ligne d'IA, un auteur de commit autre que celui du projet ; REVIEW : une ligne qui ressemble à un mot de passe ou jeton en clair ; sortie 1 en cas de BLOCK | `publication_check.py` legge solo git (file versionati e cronologia, mai gli ignorati) e non stampa mai il segreto. BLOCK: una chiave privata, un IP pubblico, un'e-mail personale, un `secrets/` o `.env` versionato, un commit con coautore o riga di IA, un autore di commit diverso da quello del progetto; REVIEW: una riga che sembra una password o un token in chiaro; esce con 1 a ogni BLOCK | `publication_check.py` は git だけを読み（追跡ファイルと履歴。無視ファイルは読まない）、秘密は決して表示しません。BLOCK：秘密鍵、公開 IP アドレス、個人のメールアドレス、追跡された `secrets/` や `.env`、共著者や AI の行を含むコミット、プロジェクト以外の作者のコミット。REVIEW：平文のパスワードやトークンに見える行。BLOCK があれば終了コード 1 | `publication_check.py` 只读 git（已跟踪文件与历史，从不读被忽略的文件），且从不打印密钥。BLOCK：私钥、公网 IP 地址、个人邮箱、被跟踪的 `secrets/` 或 `.env`、带共同作者或 AI 尾注的提交、作者不是项目作者的提交；REVIEW：看起来像明文密码或令牌的行；出现任何 BLOCK 时退出码为 1 | `publication_check.py` só lê o git (ficheiros versionados e histórico, nunca os ignorados) e nunca imprime o segredo. BLOCK: uma chave privada, um IP público, um e-mail pessoal, um `secrets/` ou `.env` versionado, um commit com coautor ou linha de IA, um autor de commit diferente do do projeto; REVIEW: uma linha que parece uma palavra-passe ou token literal; sai com 1 perante qualquer BLOCK"),
    S("A history with leftovers | Un historial con restos | Ein Verlauf mit Überresten | Un historique avec des restes | Una cronologia con residui | 残骸の残る履歴 | 带残留物的历史 | Um histórico com restos",
      "`clean_history.py` makes a publishable copy of a repository with a single commit made by the project's author | `clean_history.py` hace una copia publicable de un repositorio con un solo commit hecho por el autor del proyecto | `clean_history.py` erzeugt eine veröffentlichbare Kopie eines Repositorys mit einem einzigen Commit des Projektautors | `clean_history.py` fait une copie publiable d'un dépôt avec un seul commit fait par l'auteur du projet | `clean_history.py` crea una copia pubblicabile di un repository con un solo commit fatto dall'autore del progetto | `clean_history.py` は、プロジェクトの作者による 1 コミットだけの公開用コピーを作ります | `clean_history.py` 生成仓库的可发布副本，只有项目作者提交的一个提交 | `clean_history.py` faz uma cópia publicável de um repositório com um só commit feito pelo autor do projeto"),
    S("Claiming more than has been proven | Afirmar más de lo probado | Mehr behaupten, als belegt ist | Affirmer plus que ce qui est prouvé | Affermare più di quanto provato | 実証以上の主張 | 声称超过已证实的内容 | Afirmar mais do que foi provado",
      "`docs/CAPABILITY_MATRIX.md` has three levels (Simulated, Local, Verified) plus None, Absent and Local-not-activated; only the Verified rows have touched hardware (the CM5 test bench in daily use) | `docs/CAPABILITY_MATRIX.md` tiene tres niveles (Simulated, Local, Verified) más None, Absent y Local-not-activated; solo las filas Verified han tocado hardware (el banco de la CM5 en uso diario) | `docs/CAPABILITY_MATRIX.md` hat drei Stufen (Simulated, Local, Verified) sowie None, Absent und Local-not-activated; nur die Verified-Zeilen haben Hardware berührt (der CM5-Prüfstand im Alltag) | `docs/CAPABILITY_MATRIX.md` a trois niveaux (Simulated, Local, Verified) plus None, Absent et Local-not-activated ; seules les lignes Verified ont touché du matériel (le banc d'essai CM5 en usage quotidien) | `docs/CAPABILITY_MATRIX.md` ha tre livelli (Simulated, Local, Verified) più None, Absent e Local-not-activated; solo le righe Verified hanno toccato hardware (il banco di prova CM5 in uso quotidiano) | `docs/CAPABILITY_MATRIX.md` は 3 段階（Simulated、Local、Verified）に None、Absent、Local-not-activated を加えたもの。実機に触れたのは Verified の行だけです（日常運用中の CM5 テストベンチ） | `docs/CAPABILITY_MATRIX.md` 分三级（Simulated、Local、Verified），另有 None、Absent 和 Local-not-activated；只有 Verified 行接触过硬件（日常使用的 CM5 测试台） | `docs/CAPABILITY_MATRIX.md` tem três níveis (Simulated, Local, Verified) mais None, Absent e Local-not-activated; só as linhas Verified tocaram em hardware (a bancada do CM5 em uso diário)"),
    S("A README that says something else than the project | Un README que dice algo distinto del proyecto | Ein README, das etwas anderes sagt als das Projekt | Un README qui dit autre chose que le projet | Un README che dice altro dal progetto | プロジェクトと食い違う README | README 与项目说法不一致 | Um README que diz outra coisa do que o projeto",
      "The version and the maturity of each README are read from its own manifest; every push checks that the READMEs, the banners and the catalogue are current and that every repository of the registry has its status table | La versión y la madurez de cada README se leen de su propio manifiesto; cada push comprueba que los README, los banners y el catálogo están al día y que cada repositorio del registro tiene su tabla de estado | Version und Reife jedes READMEs werden aus dessen eigenem Manifest gelesen; jeder Push prüft, dass READMEs, Banner und Katalog aktuell sind und jedes Repository des Registers seine Statustabelle hat | La version et la maturité de chaque README sont lues dans son propre manifeste ; chaque push vérifie que les README, les bannières et le catalogue sont à jour et que chaque dépôt du registre a son tableau d'état | La versione e la maturità di ogni README si leggono dal suo manifesto; ogni push verifica che README, banner e catalogo siano aggiornati e che ogni repository del registro abbia la sua tabella di stato | 各 README のバージョンと成熟度は自身のマニフェストから読み取ります。push のたびに、README、バナー、カタログが最新で、レジストリの全リポジトリに状態表があることを検査します | 每个 README 的版本和成熟度都从其自己的清单读取；每次推送都会检查 README、横幅图和目录是否最新，以及注册表中的每个仓库是否都有状态表 | A versão e a maturidade de cada README são lidas do seu próprio manifesto; cada push verifica que os README, as faixas e o catálogo estão atualizados e que cada repositório do registo tem a sua tabela de estado"),
]
SEC_TAIL = P("The security documents of the family are [docs/SECURITY_BASELINE.md](docs/SECURITY_BASELINE.md) (the VLAN design, what the code enforces and what is still missing) and [docs/THREAT_MODEL.md](docs/THREAT_MODEL.md). Nothing here proves the absence of a secret.",
             "Los documentos de seguridad de la familia son [docs/SECURITY_BASELINE.md](docs/SECURITY_BASELINE.md) (el diseño de VLAN, lo que el código hace cumplir y lo que aún falta) y [docs/THREAT_MODEL.md](docs/THREAT_MODEL.md). Nada de esto prueba la ausencia de un secreto.",
             "Die Sicherheitsdokumente der Familie sind [docs/SECURITY_BASELINE.md](docs/SECURITY_BASELINE.md) (das VLAN-Design, was der Code durchsetzt und was noch fehlt) und [docs/THREAT_MODEL.md](docs/THREAT_MODEL.md). Nichts davon beweist die Abwesenheit eines Geheimnisses.",
             "Les documents de sécurité de la famille sont [docs/SECURITY_BASELINE.md](docs/SECURITY_BASELINE.md) (la conception des VLAN, ce que le code fait respecter et ce qui manque encore) et [docs/THREAT_MODEL.md](docs/THREAT_MODEL.md). Rien de cela ne prouve l'absence d'un secret.",
             "I documenti di sicurezza della famiglia sono [docs/SECURITY_BASELINE.md](docs/SECURITY_BASELINE.md) (il progetto delle VLAN, cosa fa rispettare il codice e cosa manca ancora) e [docs/THREAT_MODEL.md](docs/THREAT_MODEL.md). Nulla di questo prova l'assenza di un segreto.",
             "ファミリーのセキュリティ文書は [docs/SECURITY_BASELINE.md](docs/SECURITY_BASELINE.md)（VLAN 設計、コードが強制すること、まだ足りないこと）と [docs/THREAT_MODEL.md](docs/THREAT_MODEL.md) です。ここで秘密がないことが証明されるわけではありません。",
             "家族的安全文档是 [docs/SECURITY_BASELINE.md](docs/SECURITY_BASELINE.md)（VLAN 设计、代码强制执行的内容和仍缺少的部分）和 [docs/THREAT_MODEL.md](docs/THREAT_MODEL.md)。这里的任何内容都不能证明不存在密钥。",
             "Os documentos de segurança da família são [docs/SECURITY_BASELINE.md](docs/SECURITY_BASELINE.md) (o desenho das VLAN, o que o código impõe e o que ainda falta) e [docs/THREAT_MODEL.md](docs/THREAT_MODEL.md). Nada disto prova a ausência de um segredo.")

TOOLS = [
    ("`python tools/make_readmes.py [--check]`", "-", T("writes the README of every repository in eight languages from `tools/readme_src/`; `--check` fails when one is out of date. It rewrites every file: change the source, never the READMEs | escribe el README de cada repositorio en ocho idiomas desde `tools/readme_src/`; `--check` falla si alguno está desfasado. Reescribe todos los ficheros: cambia la fuente, nunca los README | schreibt das README jedes Repositorys in acht Sprachen aus `tools/readme_src/`; `--check` schlägt fehl, wenn eines veraltet ist. Es überschreibt jede Datei: die Quelle ändern, nie die READMEs | écrit le README de chaque dépôt en huit langues depuis `tools/readme_src/` ; `--check` échoue si l'un est périmé. Il réécrit tous les fichiers : changez la source, jamais les README | scrive il README di ogni repository in otto lingue da `tools/readme_src/`; `--check` fallisce se uno è vecchio. Riscrive ogni file: cambia la fonte, mai i README | `tools/readme_src/` から全リポジトリの README を 8 言語で書き出す。`--check` は古いものがあると失敗。全ファイルを書き直すので、README ではなくソースを変更する | 从 `tools/readme_src/` 写出每个仓库八种语言的 README；`--check` 在有过期时失败。它会重写所有文件：改源文件，不要改 README | escreve o README de cada repositório em oito idiomas a partir de `tools/readme_src/`; `--check` falha se algum estiver desatualizado. Reescreve todos os ficheiros: mude a fonte, nunca os README")),
    ("`python tools/make_catalog.py [--check]`  `make_brand.py [--check]`", "-", T("the versions and maturity of `docs/PROJECT_CATALOG.md`, and the banners and icons | las versiones y madurez de `docs/PROJECT_CATALOG.md`, y los banners e iconos | die Versionen und Reife in `docs/PROJECT_CATALOG.md` sowie Banner und Symbole | les versions et la maturité de `docs/PROJECT_CATALOG.md`, et les bannières et icônes | le versioni e la maturità di `docs/PROJECT_CATALOG.md`, e banner e icone | `docs/PROJECT_CATALOG.md` のバージョンと成熟度、バナーとアイコン | `docs/PROJECT_CATALOG.md` 的版本与成熟度，以及横幅图和图标 | as versões e a maturidade de `docs/PROJECT_CATALOG.md`, e as faixas e os ícones")),
    ("`python tools/publication_check.py [REPO] [--no-history] [--ref=BRANCH]`", "-", T("what would leak if the repositories were published; exits 1 on BLOCK | lo que se filtraría si se publicaran los repositorios; sale con 1 ante BLOCK | was durchsickern würde, wenn die Repositorys veröffentlicht würden; Ausstieg mit 1 bei BLOCK | ce qui fuirait si les dépôts étaient publiés ; sortie 1 en cas de BLOCK | ciò che trapelerebbe se i repository fossero pubblicati; esce con 1 a ogni BLOCK | リポジトリを公開した場合に漏れるもの。BLOCK で終了コード 1 | 如果公开这些仓库会泄露什么；出现 BLOCK 时退出码为 1 | o que vazaria se os repositórios fossem publicados; sai com 1 perante BLOCK")),
    ("`python tools/clean_history.py`", "-", T("a publishable copy of a repository with one commit | una copia publicable de un repositorio con un solo commit | eine veröffentlichbare Kopie eines Repositorys mit einem Commit | une copie publiable d'un dépôt avec un seul commit | una copia pubblicabile di un repository con un solo commit | 1 コミットだけの公開用コピー | 只有一个提交的可发布仓库副本 | uma cópia publicável de um repositório com um só commit")),
    ("`python tools/sync_ci_tools.py [--check]`", "-", T("copies the shared CI checks and the launcher into every repository; `--check` fails when a copy has drifted | copia las comprobaciones de CI y el lanzador en cada repositorio; `--check` falla si una copia se ha desviado | kopiert die gemeinsamen CI-Prüfungen und den Starter in jedes Repository; `--check` schlägt fehl, wenn eine Kopie abweicht | copie les vérifications CI et le lanceur dans chaque dépôt ; `--check` échoue si une copie a dérivé | copia i controlli CI e l'avviatore in ogni repository; `--check` fallisce se una copia è divergente | 共通の CI 検査とランチャーを各リポジトリにコピー。コピーがずれると `--check` が失敗 | 把共用的 CI 检查和启动器复制到每个仓库；副本偏离时 `--check` 失败 | copia as verificações de CI e o lançador para cada repositório; `--check` falha se uma cópia divergiu")),
    ("`python tools/status_lights.py --check|--suggest|--apply`", "-", T("keeps the lights of the Project status table below what the manifest allows (maturity and evidence); it moves lights, never sentences; the CI of every repository runs `--check` | mantiene las luces de la tabla de estado del proyecto por debajo de lo que permite el manifiesto (madurez y evidencia); mueve luces, nunca frases; la CI de cada repositorio ejecuta `--check` | hält die Ampeln der Projektstatus-Tabelle unter dem, was das Manifest erlaubt (Reife und Nachweis); sie bewegt Ampeln, nie Sätze; die CI jedes Repositorys führt `--check` aus | garde les feux du tableau d'état du projet sous ce que le manifeste permet (maturité et preuve) ; il déplace des feux, jamais des phrases ; la CI de chaque dépôt exécute `--check` | mantiene le luci della tabella di stato del progetto entro ciò che il manifesto consente (maturità ed evidenza); sposta luci, mai frasi; la CI di ogni repository esegue `--check` | プロジェクト状況表の信号をマニフェスト(成熟度と実証)が許す範囲に保つ。動かすのは信号だけで文は変えない。各リポジトリの CI が `--check` を実行 | 让项目状态表的信号灯不超过清单允许的范围（成熟度与实证）；只移动信号灯，不改句子；每个仓库的 CI 都运行 `--check` | mantém as luzes da tabela de estado do projeto abaixo do que o manifesto permite (maturidade e evidência); move luzes, nunca frases; a CI de cada repositório executa `--check`")),
    ("`bash tools/check_all.sh [--android] [--compose]`", "-", T("the tests of every repository in one run; a check without its tool is SKIP, never PASS | las pruebas de cada repositorio de una vez; una comprobación sin su herramienta es SKIP, nunca PASS | die Tests jedes Repositorys in einem Lauf; eine Prüfung ohne ihr Werkzeug ist SKIP, nie PASS | les tests de chaque dépôt en un lancement ; un contrôle sans son outil est SKIP, jamais PASS | i test di ogni repository in un'esecuzione; un controllo senza il suo strumento è SKIP, mai PASS | 全リポジトリのテストを一度に実行。ツールがない検査は PASS ではなく SKIP | 一次运行每个仓库的测试；缺少工具的检查记为 SKIP，绝不是 PASS | os testes de cada repositório numa execução; uma verificação sem a sua ferramenta é SKIP, nunca PASS")),
]
TOOLS_NOTE = P("The source of each README is `tools/readme_src/repos/<REPOSITORY>.py` (the facts that do not depend on the language, and the words of the eight languages), with `ui.py` for the words around every README and `shots.py` for the captures. `tools/registry.py` reads the list of repositories of ARMOR-COMMON. See also [docs/INTERFACES.md](docs/INTERFACES.md) and [docs/SETUP_CODE.md](docs/SETUP_CODE.md).",
               "La fuente de cada README es `tools/readme_src/repos/<REPOSITORIO>.py` (los datos que no dependen del idioma y las palabras de los ocho idiomas), con `ui.py` para las palabras alrededor de cada README y `shots.py` para las capturas. `tools/registry.py` lee la lista de repositorios de ARMOR-COMMON. Mira también [docs/INTERFACES.md](docs/INTERFACES.md) y [docs/SETUP_CODE.md](docs/SETUP_CODE.md).",
               "Die Quelle jedes READMEs ist `tools/readme_src/repos/<REPOSITORY>.py` (die sprachunabhängigen Fakten und die Worte der acht Sprachen), mit `ui.py` für die Worte rund um jedes README und `shots.py` für die Aufnahmen. `tools/registry.py` liest die Repository-Liste von ARMOR-COMMON. Siehe auch [docs/INTERFACES.md](docs/INTERFACES.md) und [docs/SETUP_CODE.md](docs/SETUP_CODE.md).",
               "La source de chaque README est `tools/readme_src/repos/<DÉPÔT>.py` (les faits indépendants de la langue et les mots des huit langues), avec `ui.py` pour les mots autour de chaque README et `shots.py` pour les captures. `tools/registry.py` lit la liste des dépôts d'ARMOR-COMMON. Voir aussi [docs/INTERFACES.md](docs/INTERFACES.md) et [docs/SETUP_CODE.md](docs/SETUP_CODE.md).",
               "La fonte di ogni README è `tools/readme_src/repos/<REPOSITORY>.py` (i fatti indipendenti dalla lingua e le parole delle otto lingue), con `ui.py` per le parole attorno a ogni README e `shots.py` per le schermate. `tools/registry.py` legge l'elenco dei repository di ARMOR-COMMON. Vedi anche [docs/INTERFACES.md](docs/INTERFACES.md) e [docs/SETUP_CODE.md](docs/SETUP_CODE.md).",
               "各 README のソースは `tools/readme_src/repos/<リポジトリ>.py`（言語に依存しない事実と 8 言語の文言）で、README の周囲の文言は `ui.py`、スクリーンショットは `shots.py` にあります。`tools/registry.py` は ARMOR-COMMON のリポジトリ一覧を読みます。[docs/INTERFACES.md](docs/INTERFACES.md) と [docs/SETUP_CODE.md](docs/SETUP_CODE.md) も参照。",
               "每个 README 的源文件是 `tools/readme_src/repos/<仓库>.py`（与语言无关的事实和八种语言的文字），README 周围的文字在 `ui.py`，截图在 `shots.py`。`tools/registry.py` 读取 ARMOR-COMMON 的仓库清单。另见 [docs/INTERFACES.md](docs/INTERFACES.md) 和 [docs/SETUP_CODE.md](docs/SETUP_CODE.md)。",
               "A fonte de cada README é `tools/readme_src/repos/<REPOSITÓRIO>.py` (os factos que não dependem do idioma e as palavras dos oito idiomas), com `ui.py` para as palavras à volta de cada README e `shots.py` para as capturas. `tools/registry.py` lê a lista de repositórios do ARMOR-COMMON. Veja também [docs/INTERFACES.md](docs/INTERFACES.md) e [docs/SETUP_CODE.md](docs/SETUP_CODE.md).")

QUICK_LEAD = P("**Requirements:** Python 3.11+ for the tools (standard library only); the repositories of the family next to this one for the checks that read them.", "**Requisitos:** Python 3.11+ para las herramientas (solo biblioteca estándar); los repositorios de la familia junto a este para las comprobaciones que los leen.", "**Voraussetzungen:** Python 3.11+ für die Werkzeuge (nur Standardbibliothek); die Repositorys der Familie neben diesem für die Prüfungen, die sie lesen.",
               "**Prérequis :** Python 3.11+ pour les outils (bibliothèque standard seule) ; les dépôts de la famille à côté de celui-ci pour les vérifications qui les lisent.", "**Requisiti:** Python 3.11+ per gli strumenti (solo libreria standard); i repository della famiglia accanto a questo per i controlli che li leggono.", "**要件：** ツール用の Python 3.11+（標準ライブラリのみ）。それらを読む検査には、ファミリーのリポジトリをこの隣に置きます。",
               "**要求：** 工具需要 Python 3.11+（仅标准库）；读取其他仓库的检查需要把家族的各仓库放在本仓库旁边。", "**Requisitos:** Python 3.11+ para as ferramentas (só biblioteca padrão); os repositórios da família ao lado deste para as verificações que os leem.")
QUICK_CODE = [
    ("python tools/make_readmes.py --check", T("the READMEs (8 languages) are current | los README (8 idiomas) están al día | die READMEs (8 Sprachen) sind aktuell | les README (8 langues) sont à jour | i README (8 lingue) sono aggiornati | README（8 言語）は最新 | README（八种语言）是最新的 | os README (8 idiomas) estão atualizados")),
    ("python tools/make_catalog.py --check", T("the versions and maturity of the catalogue are current | las versiones y madurez del catálogo están al día | Versionen und Reife des Katalogs sind aktuell | les versions et la maturité du catalogue sont à jour | versioni e maturità del catalogo sono aggiornate | カタログのバージョンと成熟度は最新 | 目录的版本与成熟度是最新的 | as versões e a maturidade do catálogo estão atualizadas")),
    ("python tools/make_brand.py --check", T("the banners and icons are current | los banners e iconos están al día | Banner und Symbole sind aktuell | les bannières et icônes sont à jour | banner e icone sono aggiornati | バナーとアイコンは最新 | 横幅图和图标是最新的 | as faixas e os ícones estão atualizados")),
    ("python tools/publication_check.py", T("nothing private would leave with a publication | nada privado saldría con una publicación | nichts Privates würde mit einer Veröffentlichung hinausgehen | rien de privé ne sortirait avec une publication | niente di privato uscirebbe con una pubblicazione | 公開しても非公開情報は出ない | 发布时不会泄露私有内容 | nada privado sairia com uma publicação")),
    ("bash tools/check_all.sh", T("every repository's own tests, in one run | las pruebas de cada repositorio, de una vez | die Tests jedes Repositorys in einem Lauf | les tests de chaque dépôt, en un lancement | i test di ogni repository, in un'esecuzione | 各リポジトリのテストを一度に | 一次运行每个仓库的测试 | os testes de cada repositório, numa execução")),
    ("python -m unittest discover -s tests", T("199 tests of these tools; they need no other repository | 199 pruebas de estas herramientas; no necesitan otro repositorio | 199 Tests dieser Werkzeuge; sie brauchen kein anderes Repository | 199 tests de ces outils ; ils n'ont besoin d'aucun autre dépôt | 199 test di questi strumenti; non servono altri repository | これらのツールの 199 件のテスト（他のリポジトリは不要） | 这些工具的 199 项测试；无需其他仓库 | 199 testes destas ferramentas; não precisam de outro repositório")),
]

TEST_TABLE = [
    (T("The README generator | El generador de README | Der README-Generator | Le générateur de README | Il generatore di README | README ジェネレーター | README 生成器 | O gerador de README"), T("`test_make_readmes.py`, `test_verbatim_readmes.py`: the eight languages and the sections of every repository | los ocho idiomas y los apartados de cada repositorio | die acht Sprachen und die Abschnitte jedes Repositorys | les huit langues et les sections de chaque dépôt | le otto lingue e le sezioni di ogni repository | 各リポジトリの 8 言語とセクション | 每个仓库的八种语言和各章节 | os oito idiomas e as secções de cada repositório")),
    (T("Catalogue and brand | Catálogo y marca | Katalog und Marke | Catalogue et marque | Catalogo e marchio | カタログとブランド | 目录与品牌 | Catálogo e marca"), T("`test_make_catalog_and_brand.py`, `test_repository_registry.py` | `test_make_catalog_and_brand.py`, `test_repository_registry.py` | `test_make_catalog_and_brand.py`, `test_repository_registry.py` | `test_make_catalog_and_brand.py`, `test_repository_registry.py` | `test_make_catalog_and_brand.py`, `test_repository_registry.py` | `test_make_catalog_and_brand.py`、`test_repository_registry.py` | `test_make_catalog_and_brand.py`、`test_repository_registry.py` | `test_make_catalog_and_brand.py`, `test_repository_registry.py`")),
    (T("Publication | Publicación | Veröffentlichung | Publication | Pubblicazione | 公開 | 发布 | Publicação"), T("`test_publication_check.py`, `test_clean_history.py`: what is BLOCK and REVIEW, and the one-commit copy | qué es BLOCK y REVIEW, y la copia de un commit | was BLOCK und REVIEW ist, und die Ein-Commit-Kopie | ce qui est BLOCK et REVIEW, et la copie à un commit | cosa è BLOCK e REVIEW, e la copia a un commit | BLOCK と REVIEW の基準、1 コミットのコピー | 什么算 BLOCK 和 REVIEW，以及单提交副本 | o que é BLOCK e REVIEW, e a cópia de um commit")),
    (T("CI tools and launcher | Herramientas de CI y lanzador | CI-Werkzeuge und Starter | Outils CI et lanceur | Strumenti CI e avviatore | CI ツールとランチャー | CI 工具与启动器 | Ferramentas de CI e lançador"), T("`test_ci_validate.py`, `test_sync_ci_tools.py`, `test_project_tool.py`, `test_check_all_script.py` | `test_ci_validate.py`, `test_sync_ci_tools.py`, `test_project_tool.py`, `test_check_all_script.py` | `test_ci_validate.py`, `test_sync_ci_tools.py`, `test_project_tool.py`, `test_check_all_script.py` | `test_ci_validate.py`, `test_sync_ci_tools.py`, `test_project_tool.py`, `test_check_all_script.py` | `test_ci_validate.py`, `test_sync_ci_tools.py`, `test_project_tool.py`, `test_check_all_script.py` | `test_ci_validate.py`、`test_sync_ci_tools.py`、`test_project_tool.py`、`test_check_all_script.py` | `test_ci_validate.py`、`test_sync_ci_tools.py`、`test_project_tool.py`、`test_check_all_script.py` | `test_ci_validate.py`, `test_sync_ci_tools.py`, `test_project_tool.py`, `test_check_all_script.py`")),
]
TEST_NOTE = P("GitHub Actions runs the A.R.M.O.R. baseline on every push and pull request: the validation of the manifest, version, changelog and README parity, then the project's own build and tests.",
              "GitHub Actions ejecuta la base de A.R.M.O.R. en cada push y pull request: la validación del manifiesto, la versión, el registro de cambios y la paridad de los README, y luego la compilación y las pruebas del propio proyecto.",
              "GitHub Actions führt bei jedem Push und Pull Request die A.R.M.O.R.-Basis aus: die Prüfung von Manifest, Version, Änderungsprotokoll und README-Parität, dann den eigenen Build und die eigenen Tests des Projekts.",
              "GitHub Actions exécute la base A.R.M.O.R. à chaque push et pull request : la validation du manifeste, de la version, du journal des modifications et de la parité des README, puis le build et les tests propres au projet.",
              "GitHub Actions esegue la base A.R.M.O.R. a ogni push e pull request: la validazione di manifesto, versione, registro delle modifiche e parità dei README, poi la compilazione e i test del progetto.",
              "GitHub Actions は push と pull request のたびに A.R.M.O.R. の基本検査（マニフェスト、バージョン、変更履歴、README の一致）と、プロジェクト自身のビルドとテストを実行します。",
              "GitHub Actions 在每次推送和拉取请求时运行 A.R.M.O.R. 基线：清单、版本、更新日志和 README 一致性的校验，然后是项目自身的构建和测试。",
              "O GitHub Actions executa a base do A.R.M.O.R. em cada push e pull request: a validação do manifesto, da versão, do registo de alterações e da paridade dos README, e depois a compilação e os testes do próprio projeto.")

BUILD = P("There is nothing to compile. The version lives in `armor.project.json` and in the README badge (read from the manifest); each version has its entry in [CHANGELOG.md](CHANGELOG.md). Releases are published on GitHub.",
          "No hay nada que compilar. La versión vive en `armor.project.json` y en la insignia del README (leída del manifiesto); cada versión tiene su entrada en [CHANGELOG.md](CHANGELOG.md). Las versiones se publican en GitHub.",
          "Es gibt nichts zu kompilieren. Die Version steht in `armor.project.json` und im README-Badge (aus dem Manifest gelesen); jede Version hat ihren Eintrag in [CHANGELOG.md](CHANGELOG.md). Releases werden auf GitHub veröffentlicht.",
          "Il n'y a rien à compiler. La version se trouve dans `armor.project.json` et dans le badge du README (lu depuis le manifeste) ; chaque version a son entrée dans [CHANGELOG.md](CHANGELOG.md). Les versions sont publiées sur GitHub.",
          "Non c'è nulla da compilare. La versione risiede in `armor.project.json` e nel badge del README (letto dal manifesto); ogni versione ha la sua voce in [CHANGELOG.md](CHANGELOG.md). Le versioni sono pubblicate su GitHub.",
          "コンパイルするものはありません。バージョンは `armor.project.json` と README のバッジ（マニフェストから読み取り）にあり、各バージョンには [CHANGELOG.md](CHANGELOG.md) にエントリーがあります。リリースは GitHub で公開されます。",
          "无需编译。版本记录在 `armor.project.json` 和 README 徽章中（读取自清单）；每个版本在 [CHANGELOG.md](CHANGELOG.md) 中都有对应条目。发布版本发布在 GitHub 上。",
          "Não há nada para compilar. A versão está em `armor.project.json` e no emblema do README (lido do manifesto); cada versão tem a sua entrada em [CHANGELOG.md](CHANGELOG.md). As versões são publicadas no GitHub.")

TROUBLE = [
    ("`READMEs out of date:` + a list", T("a source of `tools/readme_src/` changed, or a manifest did, and the READMEs were not written again | cambió una fuente de `tools/readme_src/` o un manifiesto y no se volvieron a escribir los README | eine Quelle in `tools/readme_src/` oder ein Manifest hat sich geändert und die READMEs wurden nicht neu geschrieben | une source de `tools/readme_src/` ou un manifeste a changé et les README n'ont pas été réécrits | è cambiata una fonte di `tools/readme_src/` o un manifesto e i README non sono stati riscritti | `tools/readme_src/` のソースかマニフェストが変わり、README が書き直されていない | `tools/readme_src/` 的源文件或某个清单变了，而 README 没有重新生成 | mudou uma fonte de `tools/readme_src/` ou um manifesto e os README não foram reescritos"), T("run `python tools/make_readmes.py`, look at what changed in each repository and commit there | ejecuta `python tools/make_readmes.py`, mira qué cambió en cada repositorio y haz commit allí | `python tools/make_readmes.py` ausführen, in jedem Repository ansehen, was sich geändert hat, und dort committen | lancez `python tools/make_readmes.py`, regardez ce qui a changé dans chaque dépôt et validez là | esegui `python tools/make_readmes.py`, guarda cosa è cambiato in ogni repository e fai commit lì | `python tools/make_readmes.py` を実行し、各リポジトリの変更を確認してそこでコミット | 运行 `python tools/make_readmes.py`，查看每个仓库中变了什么并在该仓库提交 | execute `python tools/make_readmes.py`, veja o que mudou em cada repositório e faça commit lá")),
    ("`Status tables incomplete:`", T("a repository of the registry has a status table without the expected rows or colours | un repositorio del registro tiene una tabla de estado sin las filas o colores esperados | ein Repository des Registers hat eine Statustabelle ohne die erwarteten Zeilen oder Farben | un dépôt du registre a un tableau d'état sans les lignes ou couleurs attendues | un repository del registro ha una tabella di stato senza le righe o i colori attesi | レジストリのリポジトリの状態表に、必要な行や色がない | 注册表中某个仓库的状态表缺少应有的行或颜色 | um repositório do registo tem uma tabela de estado sem as linhas ou cores esperadas"), T("complete `FACTS[\"status\"]` and the notes in its source | completa `FACTS[\"status\"]` y las notas en su fuente | `FACTS[\"status\"]` und die Hinweise in seiner Quelle vervollständigen | complétez `FACTS[\"status\"]` et les notes dans sa source | completa `FACTS[\"status\"]` e le note nella sua fonte | そのソースの `FACTS[\"status\"]` と注記を補う | 补全其源文件中的 `FACTS[\"status\"]` 和说明 | complete `FACTS[\"status\"]` e as notas na sua fonte")),
    (T("A check says SKIP | Una comprobación dice SKIP | Eine Prüfung sagt SKIP | Un contrôle dit SKIP | Un controllo dice SKIP | 検査が SKIP と出る | 某项检查显示 SKIP | Uma verificação diz SKIP"), T("its tool or the repository next to this one is missing; a check without its tool is never PASS | falta su herramienta o el repositorio junto a este; una comprobación sin su herramienta nunca es PASS | sein Werkzeug oder das Repository neben diesem fehlt; eine Prüfung ohne Werkzeug ist nie PASS | son outil ou le dépôt à côté de celui-ci manque ; un contrôle sans son outil n'est jamais PASS | manca il suo strumento o il repository accanto a questo; un controllo senza il suo strumento non è mai PASS | そのツールまたは隣のリポジトリがない（ツールがない検査は PASS にならない） | 缺少其工具或本仓库旁边的仓库；缺少工具的检查绝不会是 PASS | falta a sua ferramenta ou o repositório ao lado deste; uma verificação sem a sua ferramenta nunca é PASS"), T("install the tool or clone the repository next to this one | instala la herramienta o clona el repositorio junto a este | das Werkzeug installieren oder das Repository neben diesem klonen | installez l'outil ou clonez le dépôt à côté de celui-ci | installa lo strumento o clona il repository accanto a questo | ツールを入れるか、隣にリポジトリをクローンする | 安装该工具，或把仓库克隆到本仓库旁边 | instale a ferramenta ou clone o repositório ao lado deste")),
    ("`publication_check.py` BLOCK", T("something that must not go public was found (it shows the file, the line and the kind, never the value) | se encontró algo que no debe publicarse (muestra el fichero, la línea y el tipo, nunca el valor) | etwas, das nicht öffentlich werden darf, wurde gefunden (Datei, Zeile und Art, nie der Wert) | quelque chose qui ne doit pas devenir public a été trouvé (fichier, ligne et genre, jamais la valeur) | è stato trovato qualcosa che non deve diventare pubblico (file, riga e tipo, mai il valore) | 公開してはならないものが見つかった（ファイル、行、種類を表示。値は表示しない） | 发现了不能公开的内容（显示文件、行和类型，绝不显示值） | foi encontrado algo que não deve ficar público (ficheiro, linha e tipo, nunca o valor)"), T("remove it, and use `clean_history.py` if it is in the history | quítalo y usa `clean_history.py` si está en el historial | entfernen, und `clean_history.py` nutzen, wenn es im Verlauf steht | retirez-le et utilisez `clean_history.py` s'il est dans l'historique | rimuovilo e usa `clean_history.py` se è nella cronologia | 取り除き、履歴にある場合は `clean_history.py` を使う | 删除它；如果在历史中，使用 `clean_history.py` | retire-o e use `clean_history.py` se estiver no histórico")),
]

ROADMAP = P(
    "**Known limits today**\n\n* The capability matrix is the truth about what has run: until a row says Verified, it has not touched real hardware.\n* Only the radar node and the CM5 test bench have run on real hardware.\n* No independent security review.\n\n**Next**\n\n* Move rows of the matrix to Verified as the other nodes run on their boards.",
    "**Límites conocidos hoy**\n\n* La matriz de capacidades es la verdad sobre lo que ha corrido: hasta que una fila diga Verified, no ha tocado hardware real.\n* Solo el nodo radar y el banco de la CM5 han corrido en hardware real.\n* Sin revisión de seguridad independiente.\n\n**Lo siguiente**\n\n* Pasar filas de la matriz a Verified a medida que los otros nodos corran en sus placas.",
    "**Bekannte Grenzen heute**\n\n* Die Fähigkeitsmatrix ist die Wahrheit darüber, was gelaufen ist: Solange eine Zeile nicht Verified sagt, hat sie keine echte Hardware berührt.\n* Nur der Radar-Knoten und der CM5-Prüfstand liefen auf echter Hardware.\n* Keine unabhängige Sicherheitsprüfung.\n\n**Als Nächstes**\n\n* Zeilen der Matrix auf Verified setzen, sobald die anderen Knoten auf ihren Platinen laufen.",
    "**Limites connues aujourd'hui**\n\n* La matrice des capacités dit la vérité sur ce qui a tourné : tant qu'une ligne ne dit pas Verified, elle n'a pas touché de vrai matériel.\n* Seuls le nœud radar et le banc d'essai CM5 ont tourné sur du vrai matériel.\n* Pas de revue de sécurité indépendante.\n\n**Prochainement**\n\n* Passer des lignes de la matrice à Verified à mesure que les autres nœuds tournent sur leurs cartes.",
    "**Limiti noti oggi**\n\n* La matrice delle capacità dice la verità su ciò che è stato eseguito: finché una riga non dice Verified, non ha toccato hardware reale.\n* Solo il nodo radar e il banco di prova CM5 hanno girato su hardware reale.\n* Nessuna revisione di sicurezza indipendente.\n\n**Prossimi passi**\n\n* Portare righe della matrice a Verified man mano che gli altri nodi girano sulle loro schede.",
    "**現時点の既知の制限**\n\n* 機能マトリクスは、何が動いたかについての真実です。Verified と書かれるまで、その行は実機に触れていません。\n* 実機で動いたのはレーダーノードと CM5 テストベンチだけです。\n* 第三者によるセキュリティレビューはありません。\n\n**今後**\n\n* 他のノードが各基板で動いた分だけ、マトリクスの行を Verified にする。",
    "**当前已知限制**\n\n* 能力矩阵是关于什么已经运行过的事实：某行在写成 Verified 之前，都没有接触过真实硬件。\n* 只有雷达节点和 CM5 测试台在真实硬件上运行过。\n* 没有独立的安全审查。\n\n**下一步**\n\n* 随着其他节点在各自开发板上运行，把矩阵中的行改为 Verified。",
    "**Limites conhecidos hoje**\n\n* A matriz de capacidades é a verdade sobre o que correu: até uma linha dizer Verified, não tocou em hardware real.\n* Só o nó de radar e a bancada do CM5 correram em hardware real.\n* Sem revisão de segurança independente.\n\n**A seguir**\n\n* Passar linhas da matriz a Verified à medida que os outros nós correm nas suas placas.")


def doc(name, desc):
    seps = [": ", ": ", ": ", " : ", ": ", "：", "：", ": "]
    return P(*[f"[{name}](docs/{name}.md)" + s + d for s, d in zip(seps, desc)])


DOCS = [
    doc("ARCHITECTURE", ("networks, trust boundaries, time and ordering", "redes, límites de confianza, tiempo y orden", "Netze, Vertrauensgrenzen, Zeit und Reihenfolge", "réseaux, frontières de confiance, temps et ordre", "reti, confini di fiducia, tempo e ordinamento", "ネットワーク、信頼境界、時刻と順序", "网络、信任边界、时间与顺序", "redes, fronteiras de confiança, tempo e ordenação")),
    doc("SECURITY_BASELINE", ("the VLAN design, what the code enforces and what is missing", "el diseño de VLAN, lo que el código hace cumplir y lo que falta", "das VLAN-Design, was der Code durchsetzt und was fehlt", "la conception des VLAN, ce que le code fait respecter et ce qui manque", "il progetto delle VLAN, cosa fa rispettare il codice e cosa manca", "VLAN 設計、コードが強制すること、足りないこと", "VLAN 设计、代码强制执行的内容和缺少的部分", "o desenho das VLAN, o que o código impõe e o que falta")),
    doc("THREAT_MODEL", ("what is defended against and what is not", "de qué se defiende y de qué no", "wogegen verteidigt wird und wogegen nicht", "contre quoi on se défend et contre quoi non", "da cosa ci si difende e da cosa no", "守るものと守らないもの", "防御什么、不防御什么", "contra o que se defende e contra o que não")),
    doc("INTERFACES", ("who produces and consumes each interface and where it is trusted", "quién produce y consume cada interfaz y dónde se confía en ella", "wer jede Schnittstelle erzeugt und nutzt und wo ihr vertraut wird", "qui produit et consomme chaque interface et où on lui fait confiance", "chi produce e consuma ogni interfaccia e dove ci si fida", "各インターフェースの提供側と利用側、信頼する場所", "每个接口的生产者、消费者及信任位置", "quem produz e consome cada interface e onde se confia nela")),
    doc("FIRST_VERTICAL_SLICE", ("what the simulator-to-console test proves and what it does not", "lo que prueba y lo que no prueba el ensayo del simulador a la consola", "was der Test vom Simulator zur Konsole beweist und was nicht", "ce que prouve le test du simulateur à la console et ce qu'il ne prouve pas", "cosa prova il test dal simulatore alla console e cosa no", "シミュレーターからコンソールまでのテストが証明すること、しないこと", "从模拟器到控制台的测试证明了什么、没有证明什么", "o que prova o teste do simulador à consola e o que não prova")),
    doc("SETUP_CODE", ("the set-up code of the nodes", "el código de configuración de los nodos", "der Einrichtungscode der Knoten", "le code de configuration des nœuds", "il codice di configurazione dei nodi", "ノードの設定コード", "节点的设置码", "o código de configuração dos nós")),
]


def build_lg(lg):
    bullets = "\n".join(f"* {b}" for b in L(lg, "bullets"))
    status = dict(LEGACY[lg]["status"])
    status["tests"] = TESTS_NOTE[lg]
    body = {
        "overview": f"{L(lg, 'intro')}\n\n{bullets}",
        "role": f"{L(lg, 'fit')}\n\n{table(lg, 'talks', ROLE_TABLE)}",
        "architecture": arch(lg, "ARMOR-DOCS", "ARMOR-DOCS architecture: what the tools read, the tools themselves and what they write in every repository", None),
        "security": table(lg, "threat", SECURITY_ROWS) + "\n\n" + SEC_TAIL[lg],
        "interfaces": table(lg, "route", TOOLS) + "\n\n" + TOOLS_NOTE[lg],
        "quickstart": f"{QUICK_LEAD[lg]}\n\n" + code(lg, QUICK_CODE, "bash"),
        "testing": table(lg, "area", TEST_TABLE) + "\n\n" + TEST_NOTE[lg],
        "build": BUILD[lg],
        "troubleshooting": table(lg, "trouble", TROUBLE),
        "structure": structure(lg, "ARMOR-DOCS", tree=TREE[lg]),
        "roadmap": ROADMAP[lg],
    }
    return text_for(lg, tagline=L(lg, "tagline"), honest=L(lg, "honest"), glance=GLANCE, status=status, docs=DOCS, contributing_first=CONTRIB, body=body)


TEXT = {lg: build_lg(lg) for lg in LGS}
