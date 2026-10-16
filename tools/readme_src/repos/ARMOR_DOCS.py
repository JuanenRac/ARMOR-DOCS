# The facts that do not depend on the language, and the words of every language, of ARMOR-DOCS.
# Copyright (C) 2026 JuanenRac (Electro Hobby 3D). GPL-3.0-or-later.

FACTS = {
 "emoji": "📚",
 "badges": [
  [
   "Format",
   "Markdown",
   "083fa1"
  ],
  [
   "Languages",
   "8",
   "00E5FF"
  ]
 ],
 "diagram": "",
 "build": "```bash\npython tools/make_readmes.py --check      # the READMEs (8 languages) are current\npython tools/make_catalog.py --check     # the versions and maturity of the catalogue are current\npython tools/make_brand.py --check        # the banners and icons are current\npython tools/publication_check.py         # nothing private would leave with a publication\nbash tools/check_all.sh                   # every repository's own tests, in one run\n```",
 "structure": "```text\nARMOR-DOCS/\n├── docs/     CAPABILITY_MATRIX, ARCHITECTURE, SECURITY_BASELINE, PROJECT_CATALOG, INTERFACES, THREAT_MODEL, FIRST_VERTICAL_SLICE\n├── tools/    make_readmes.py (+ readme_src/: the facts and the words of every repository in eight languages), make_catalog.py, make_brand.py, publication_check.py, clean_history.py, sync_ci_tools.py, check_all.sh\n├── brand/    the emblem\n└── images/   this repository's banner, icon and the family picture\n```",
 "requirements": [
  "Python 3.11+ for the tools"
 ]
}

TEXT = {
 "en": {
  "tagline": "Canonical architecture, security baseline and the truth about what is proven",
  "honest": "This repository documents interfaces and procedures that have been validated, and it says plainly what has not. Read the [capability matrix](docs/CAPABILITY_MATRIX.md) before believing any feature is \"done\": it says for each one whether it was only simulated, tested on a computer or verified on real hardware. The READMEs of the eighteen repositories are written from one source (`tools/readme_src/`) in eight languages, with the version and the maturity of each read from its own manifest, so they cannot say something different from the project.",
  "bullets": [
   "[Capability matrix](docs/CAPABILITY_MATRIX.md): for each capability, is it simulated, tested on a computer or verified on hardware?",
   "[Architecture](docs/ARCHITECTURE.md): networks, trust boundaries, time and ordering.",
   "[Security baseline](docs/SECURITY_BASELINE.md): the VLAN design, what the code enforces and what is still missing; and the [threat model](docs/THREAT_MODEL.md).",
   "[Project catalogue](docs/PROJECT_CATALOG.md): the eighteen repositories, their versions and how they depend on each other.",
   "[Interfaces](docs/INTERFACES.md): who produces and consumes each interface and where it is trusted.",
   "[First vertical slice](docs/FIRST_VERTICAL_SLICE.md): what the simulator-to-console test proves and what it does not.",
   "**Tools:** `make_readmes.py` writes the README of every repository in the eight languages from `readme_src/`, `make_catalog.py` writes the versions of the catalogue, `make_brand.py` its banner and icon, `publication_check.py` looks for anything private before a publication, `clean_history.py` makes a publishable copy of a repository and `sync_ci_tools.py` keeps the CI checks of the family equal."
  ],
  "intro": "<p align=\"center\">\n  <img src=\"images/ARMOR_FAMILY.svg\" alt=\"A.R.M.O.R. family\" width=\"100%\">\n</p>",
  "fit": "ARMOR-DOCS is the family's memory: it is where the architecture, the security baseline and the capability matrix live, and the place that says, for every repository, what has really run on hardware. It also holds the tool that writes the READMEs of all eighteen repositories from one source, so that the eight languages cannot drift apart.",
  "hardware": "Not applicable: it is documentation; it records what the other repositories have run on real hardware"
 },
 "es": {
  "tagline": "Arquitectura canónica, base de seguridad y la verdad sobre lo que está probado",
  "honest": "Este repositorio documenta interfaces y procedimientos que se han validado, y dice claramente lo que no. Lee la [matriz de capacidades](docs/CAPABILITY_MATRIX.md) antes de creer que una función está \"hecha\": dice de cada una si solo se simuló, se probó en un ordenador o se verificó en hardware real. Los README de los dieciocho repositorios se escriben desde una sola fuente (`tools/readme_src/`) en ocho idiomas, con la versión y la madurez de cada uno leídas de su propio manifiesto, de modo que no pueden decir algo distinto del proyecto.",
  "bullets": [
   "[Matriz de capacidades](docs/CAPABILITY_MATRIX.md): de cada capacidad, ¿está simulada, probada en un ordenador o verificada en hardware?",
   "[Arquitectura](docs/ARCHITECTURE.md): redes, límites de confianza, tiempo y orden.",
   "[Base de seguridad](docs/SECURITY_BASELINE.md): el diseño de VLAN, lo que el código hace cumplir y lo que aún falta; y el [modelo de amenazas](docs/THREAT_MODEL.md).",
   "[Catálogo de proyectos](docs/PROJECT_CATALOG.md): los dieciocho repositorios, sus versiones y cómo dependen unos de otros.",
   "[Interfaces](docs/INTERFACES.md): quién produce y consume cada interfaz y dónde se confía en ella.",
   "[Primera rebanada vertical](docs/FIRST_VERTICAL_SLICE.md): qué demuestra la prueba del simulador a la consola y qué no.",
   "**Herramientas:** `make_readmes.py` escribe el README de cada repositorio en los ocho idiomas desde `readme_src/`, `make_catalog.py` escribe las versiones del catálogo, `make_brand.py` su banner e icono, `publication_check.py` busca cualquier cosa privada antes de una publicación, `clean_history.py` hace una copia publicable de un repositorio y `sync_ci_tools.py` mantiene iguales las comprobaciones de CI de la familia."
  ],
  "intro": "<p align=\"center\">\n  <img src=\"images/ARMOR_FAMILY.svg\" alt=\"A.R.M.O.R. family\" width=\"100%\">\n</p>",
  "fit": "ARMOR-DOCS es la memoria de la familia: es donde viven la arquitectura, la base de seguridad y la matriz de capacidades, y el lugar que dice, de cada repositorio, qué ha corrido de verdad en hardware. También guarda la herramienta que escribe los README de los dieciocho repositorios desde una sola fuente, para que los ocho idiomas no se separen.",
  "hardware": "No aplica: es documentación; registra lo que los demás repositorios han corrido en hardware real"
 },
 "fr": {
  "tagline": "Architecture canonique, base de sécurité et vérité sur ce qui est prouvé",
  "honest": "Ce dépôt documente des interfaces et des procédures qui ont été validées, et dit clairement ce qui ne l'a pas été. Lisez la [matrice de capacités](docs/CAPABILITY_MATRIX.md) avant de croire qu'une fonction est « faite » : elle dit pour chacune si elle a seulement été simulée, testée sur un ordinateur ou vérifiée sur du matériel réel. Les README des dix-huit dépôts sont écrits à partir d'une seule source (`tools/readme_src/`) en huit langues, la version et la maturité de chacun étant lues dans son propre manifeste, si bien qu'ils ne peuvent pas dire autre chose que le projet.",
  "bullets": [
   "[Matrice de capacités](docs/CAPABILITY_MATRIX.md) : pour chaque capacité, est-elle simulée, testée sur un ordinateur ou vérifiée sur du matériel ?",
   "[Architecture](docs/ARCHITECTURE.md) : réseaux, frontières de confiance, temps et ordre.",
   "[Base de sécurité](docs/SECURITY_BASELINE.md) : la conception des VLAN, ce que le code impose et ce qui manque encore ; et le [modèle de menaces](docs/THREAT_MODEL.md).",
   "[Catalogue de projets](docs/PROJECT_CATALOG.md) : les dix-huit dépôts, leurs versions et leurs dépendances.",
   "[Interfaces](docs/INTERFACES.md) : qui produit et consomme chaque interface et où on lui fait confiance.",
   "[Première tranche verticale](docs/FIRST_VERTICAL_SLICE.md) : ce que prouve le test du simulateur à la console et ce qu'il ne prouve pas.",
   "**Outils :** `make_readmes.py` écrit le README de chaque dépôt dans les huit langues à partir de `readme_src/`, `make_catalog.py` écrit les versions du catalogue, `make_brand.py` sa bannière et son icône, `publication_check.py` cherche tout ce qui est privé avant une publication, `clean_history.py` fait une copie publiable d'un dépôt et `sync_ci_tools.py` garde égaux les contrôles de CI de la famille."
  ],
  "intro": "<p align=\"center\">\n  <img src=\"images/ARMOR_FAMILY.svg\" alt=\"A.R.M.O.R. family\" width=\"100%\">\n</p>",
  "fit": "ARMOR-DOCS est la mémoire de la famille : c'est là que vivent l'architecture, la base de sécurité et la matrice de capacités, et l'endroit qui dit, pour chaque dépôt, ce qui a vraiment tourné sur du matériel. Il garde aussi l'outil qui écrit les README des dix-huit dépôts à partir d'une seule source, pour que les huit langues ne dérivent pas.",
  "hardware": "Sans objet : c'est de la documentation ; elle consigne ce que les autres dépôts ont fait tourner sur du matériel réel"
 },
 "it": {
  "tagline": "Architettura canonica, base di sicurezza e la verità su ciò che è provato",
  "honest": "Questo repository documenta interfacce e procedure che sono state validate, e dice chiaramente ciò che non lo è. Leggi la [matrice delle capacità](docs/CAPABILITY_MATRIX.md) prima di credere che una funzione sia \"fatta\": dice per ciascuna se è stata solo simulata, provata su un computer o verificata su hardware reale. I README dei diciotto repository sono scritti da un'unica fonte (`tools/readme_src/`) in otto lingue, con la versione e la maturità di ciascuno lette dal suo manifesto, così non possono dire qualcosa di diverso dal progetto.",
  "bullets": [
   "[Matrice delle capacità](docs/CAPABILITY_MATRIX.md): per ogni capacità, è simulata, provata su un computer o verificata su hardware?",
   "[Architettura](docs/ARCHITECTURE.md): reti, confini di fiducia, tempo e ordine.",
   "[Base di sicurezza](docs/SECURITY_BASELINE.md): il progetto delle VLAN, ciò che il codice impone e ciò che manca ancora; e il [modello delle minacce](docs/THREAT_MODEL.md).",
   "[Catalogo dei progetti](docs/PROJECT_CATALOG.md): i diciotto repository, le loro versioni e come dipendono l'uno dall'altro.",
   "[Interfacce](docs/INTERFACES.md): chi produce e consuma ogni interfaccia e dove ci si fida.",
   "[Prima fetta verticale](docs/FIRST_VERTICAL_SLICE.md): cosa dimostra il test dal simulatore alla console e cosa no.",
   "**Strumenti:** `make_readmes.py` scrive il README di ogni repository nelle otto lingue da `readme_src/`, `make_catalog.py` scrive le versioni del catalogo, `make_brand.py` il suo banner e l'icona, `publication_check.py` cerca qualsiasi cosa privata prima di una pubblicazione, `clean_history.py` fa una copia pubblicabile di un repository e `sync_ci_tools.py` mantiene uguali i controlli di CI della famiglia."
  ],
  "intro": "<p align=\"center\">\n  <img src=\"images/ARMOR_FAMILY.svg\" alt=\"A.R.M.O.R. family\" width=\"100%\">\n</p>",
  "fit": "ARMOR-DOCS è la memoria della famiglia: è dove vivono l'architettura, la base di sicurezza e la matrice delle capacità, e il luogo che dice, per ogni repository, cosa ha davvero girato su hardware. Tiene anche lo strumento che scrive i README di tutti e diciotto i repository da un'unica fonte, perché le otto lingue non divergano.",
  "hardware": "Non applicabile: è documentazione; registra ciò che gli altri repository hanno fatto girare su hardware reale"
 },
 "de": {
  "tagline": "Kanonische Architektur, Sicherheitsgrundlage und die Wahrheit darüber, was belegt ist",
  "honest": "Dieses Repository dokumentiert Schnittstellen und Verfahren, die validiert wurden, und sagt klar, was nicht. Lesen Sie die [Fähigkeitsmatrix](docs/CAPABILITY_MATRIX.md), bevor Sie glauben, eine Funktion sei \"fertig\": Sie sagt für jede, ob sie nur simuliert, auf einem Computer getestet oder auf echter Hardware verifiziert wurde. Die READMEs der achtzehn Repositorys werden aus einer einzigen Quelle (`tools/readme_src/`) in acht Sprachen geschrieben, wobei Version und Reifegrad jedes Projekts aus seinem eigenen Manifest gelesen werden, sodass sie nichts anderes sagen können als das Projekt.",
  "bullets": [
   "[Fähigkeitsmatrix](docs/CAPABILITY_MATRIX.md): ist jede Fähigkeit simuliert, auf einem Computer getestet oder auf Hardware verifiziert?",
   "[Architektur](docs/ARCHITECTURE.md): Netze, Vertrauensgrenzen, Zeit und Reihenfolge.",
   "[Sicherheitsgrundlage](docs/SECURITY_BASELINE.md): der VLAN-Entwurf, was der Code durchsetzt und was noch fehlt; und das [Bedrohungsmodell](docs/THREAT_MODEL.md).",
   "[Projektkatalog](docs/PROJECT_CATALOG.md): die achtzehn Repositorys, ihre Versionen und wie sie voneinander abhängen.",
   "[Schnittstellen](docs/INTERFACES.md): wer jede Schnittstelle erzeugt und nutzt und wo ihr vertraut wird.",
   "[Erster vertikaler Schnitt](docs/FIRST_VERTICAL_SLICE.md): was der Test vom Simulator zur Konsole beweist und was nicht.",
   "**Werkzeuge:** `make_readmes.py` schreibt das README jedes Repositorys in den acht Sprachen aus `readme_src/`, `make_catalog.py` schreibt die Versionen des Katalogs, `make_brand.py` sein Banner und Symbol, `publication_check.py` sucht vor einer Veröffentlichung nach allem Privaten, `clean_history.py` macht eine veröffentlichbare Kopie eines Repositorys und `sync_ci_tools.py` hält die CI-Prüfungen der Familie gleich."
  ],
  "intro": "<p align=\"center\">\n  <img src=\"images/ARMOR_FAMILY.svg\" alt=\"A.R.M.O.R. family\" width=\"100%\">\n</p>",
  "fit": "ARMOR-DOCS ist das Gedächtnis der Familie: Hier leben die Architektur, die Sicherheitsgrundlage und die Fähigkeitsmatrix, und es ist der Ort, der für jedes Repository sagt, was wirklich auf Hardware gelaufen ist. Es hält auch das Werkzeug, das die READMEs aller achtzehn Repositorys aus einer Quelle schreibt, damit die acht Sprachen nicht auseinanderlaufen.",
  "hardware": "Nicht zutreffend: es ist Dokumentation; sie hält fest, was die anderen Repositorys auf echter Hardware ausgeführt haben"
 },
 "zh": {
  "tagline": "规范的架构、安全基线，以及关于哪些已被证实的真相",
  "honest": "本仓库记录已验证的接口和流程，并明确说明哪些尚未验证。在相信某项功能“已完成”之前，请先阅读[能力矩阵](docs/CAPABILITY_MATRIX.md)：它对每一项说明它只是模拟过、在计算机上测试过，还是在真实硬件上验证过。十八个仓库的 README 来自同一个来源（`tools/readme_src/`），以八种语言编写，每个项目的版本和成熟度都读自它自己的清单，因此不会与项目说的不一样。",
  "bullets": [
   "[能力矩阵](docs/CAPABILITY_MATRIX.md)：每项能力是模拟的、在计算机上测试的，还是在硬件上验证的？",
   "[架构](docs/ARCHITECTURE.md)：网络、信任边界、时间和顺序。",
   "[安全基线](docs/SECURITY_BASELINE.md)：VLAN 设计、代码强制实施的内容以及仍然缺少的内容；以及[威胁模型](docs/THREAT_MODEL.md)。",
   "[项目目录](docs/PROJECT_CATALOG.md)：十八个仓库、它们的版本以及相互依赖关系。",
   "[接口](docs/INTERFACES.md)：谁产生和使用每个接口，以及在哪里被信任。",
   "[第一个垂直切片](docs/FIRST_VERTICAL_SLICE.md)：从模拟器到控制台的测试证明了什么、没有证明什么。",
   "**工具：**`make_readmes.py` 从 `readme_src/` 以八种语言写出每个仓库的 README，`make_catalog.py` 写出目录中的版本，`make_brand.py` 写出其横幅和图标，`publication_check.py` 在发布前查找任何私有内容，`clean_history.py` 制作仓库的可发布副本，`sync_ci_tools.py` 让家族的 CI 检查保持一致。"
  ],
  "intro": "<p align=\"center\">\n  <img src=\"images/ARMOR_FAMILY.svg\" alt=\"A.R.M.O.R. family\" width=\"100%\">\n</p>",
  "fit": "ARMOR-DOCS 是家族的记忆：架构、安全基线和能力矩阵都在这里，也是说明每个仓库究竟在硬件上运行过什么的地方。它还保存着从同一个来源编写全部十八个仓库 README 的工具，使八种语言不会各行其是。",
  "hardware": "不适用：这是文档；它记录其他仓库在真实硬件上运行过的内容"
 },
 "ja": {
  "tagline": "正典のアーキテクチャ、セキュリティ基準、そして何が実証されているかの真実",
  "honest": "このリポジトリは検証済みのインターフェースと手順を文書化し、検証されていないものは率直に述べます。ある機能が「完成」と信じる前に[能力マトリクス](docs/CAPABILITY_MATRIX.md)を読んでください。各機能が、シミュレーションのみ、コンピューター上でのテスト、実機での検証のどれかを示しています。18 のリポジトリの README は 1 つのソース（`tools/readme_src/`）から 8 言語で作られ、各プロジェクトのバージョンと成熟度は自身のマニフェストから読み取るため、プロジェクトと違うことは書けません。",
  "bullets": [
   "[能力マトリクス](docs/CAPABILITY_MATRIX.md)：各能力はシミュレーションのみか、コンピューター上でテスト済みか、実機で検証済みか。",
   "[アーキテクチャ](docs/ARCHITECTURE.md)：ネットワーク、信頼境界、時刻と順序。",
   "[セキュリティベースライン](docs/SECURITY_BASELINE.md)：VLAN 設計、コードが強制するもの、まだ足りないもの。[脅威モデル](docs/THREAT_MODEL.md)も。",
   "[プロジェクトカタログ](docs/PROJECT_CATALOG.md)：18 のリポジトリ、そのバージョン、互いの依存関係。",
   "[インターフェース](docs/INTERFACES.md)：各インターフェースを誰が生成・利用し、どこで信頼されるか。",
   "[最初の垂直スライス](docs/FIRST_VERTICAL_SLICE.md)：シミュレーターからコンソールまでのテストが証明するものとしないもの。",
   "**ツール：**`make_readmes.py` は `readme_src/` から全リポジトリの README を 8 言語で作り、`make_catalog.py` はカタログのバージョンを書き、`make_brand.py` はバナーとアイコン、`publication_check.py` は公開前に非公開のものを探し、`clean_history.py` は公開用のコピーを作り、`sync_ci_tools.py` はファミリーの CI 検査を揃えます。"
  ],
  "intro": "<p align=\"center\">\n  <img src=\"images/ARMOR_FAMILY.svg\" alt=\"A.R.M.O.R. family\" width=\"100%\">\n</p>",
  "fit": "ARMOR-DOCS はファミリーの記憶です。アーキテクチャ、セキュリティベースライン、能力マトリクスがここにあり、各リポジトリで実際に実機で動いたものを示す場所です。18 のリポジトリすべての README を 1 つのソースから書くツールもここにあり、8 言語がずれないようにしています。",
  "hardware": "該当なし：ドキュメントで、他のリポジトリが実機で動かしたものを記録します"
 },
 "pt": {
  "tagline": "Arquitetura canónica, linha de base de segurança e a verdade sobre o que está provado",
  "honest": "Este repositório documenta interfaces e procedimentos que foram validados, e diz claramente o que não foi. Leia a [matriz de capacidades](docs/CAPABILITY_MATRIX.md) antes de acreditar que uma funcionalidade está \"feita\": diz de cada uma se foi apenas simulada, testada num computador ou verificada em hardware real. Os README dos dezoito repositórios são escritos a partir de uma única fonte (`tools/readme_src/`) em oito idiomas, com a versão e a maturidade de cada um lidas do seu próprio manifesto, pelo que não podem dizer algo diferente do projeto.",
  "bullets": [
   "[Matriz de capacidades](docs/CAPABILITY_MATRIX.md): de cada capacidade, está simulada, testada num computador ou verificada em hardware?",
   "[Arquitetura](docs/ARCHITECTURE.md): redes, limites de confiança, tempo e ordem.",
   "[Base de segurança](docs/SECURITY_BASELINE.md): o desenho de VLAN, o que o código impõe e o que ainda falta; e o [modelo de ameaças](docs/THREAT_MODEL.md).",
   "[Catálogo de projetos](docs/PROJECT_CATALOG.md): os dezoito repositórios, as suas versões e como dependem uns dos outros.",
   "[Interfaces](docs/INTERFACES.md): quem produz e consome cada interface e onde se confia nela.",
   "[Primeira fatia vertical](docs/FIRST_VERTICAL_SLICE.md): o que o teste do simulador à consola prova e o que não prova.",
   "**Ferramentas:** `make_readmes.py` escreve o README de cada repositório nos oito idiomas a partir de `readme_src/`, `make_catalog.py` escreve as versões do catálogo, `make_brand.py` o seu banner e ícone, `publication_check.py` procura qualquer coisa privada antes de uma publicação, `clean_history.py` faz uma cópia publicável de um repositório e `sync_ci_tools.py` mantém iguais as verificações de CI da família."
  ],
  "intro": "<p align=\"center\">\n  <img src=\"images/ARMOR_FAMILY.svg\" alt=\"A.R.M.O.R. family\" width=\"100%\">\n</p>",
  "fit": "O ARMOR-DOCS é a memória da família: é onde vivem a arquitetura, a base de segurança e a matriz de capacidades, e o sítio que diz, de cada repositório, o que correu mesmo em hardware. Guarda também a ferramenta que escreve os README dos dezoito repositórios a partir de uma só fonte, para que os oito idiomas não se separem.",
  "hardware": "Não se aplica: é documentação; regista o que os outros repositórios correram em hardware real"
 }
}
