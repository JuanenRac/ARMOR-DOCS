# The facts that do not depend on the language, and the words of every language, of ARMOR-UPDATER.
# Copyright (C) 2026 JuanenRac (Electro Hobby 3D). GPL-3.0-or-later.

FACTS = {
 "emoji": "🛠️",
 "badges": [
  [
   "Language",
   "Python%203.10%2B",
   "3776ab"
  ],
  [
   "Dependencies",
   "none",
   "2ea44f"
  ],
  [
   "Languages",
   "8",
   "00E5FF"
  ],
  [
   "Tests",
   "116",
   "2ea44f"
  ]
 ],
 "diagram": "",
 "build": "```bash\npip install -e \".[dev]\"                                # or \".[dev,gui]\" for the optional Qt Quick desktop shell\npython -m pytest tests -q                              # 116 tests (4 skipped without a display)\narmor-updater status                                    # local + GitHub state of every repository\narmor-updater install ARMOR-NETWORK                     # clone and build one repository that is not installed yet\narmor-updater update ARMOR-NETWORK                      # atomic-by-verification update of an installed one\n```",
 "structure": "```text\nARMOR-UPDATER/\n├── src/armor_updater/  project_manifest, registry, detect (local), github_client, install (atomic staging-clone update), signature (signed updates), evidence, main (CLI), settings, version_parse,\n│                       i18n + i18n_pt (eight languages), gui / qt_gui / qml (the Qt Quick shell)\n├── tools/              armor_ci_validate.py, _armor_readme_parity.py, armor_project_tool.py (vendored from ARMOR-COMMON), generate_app_icon.py\n├── tests/              13 test modules\n└── docs/               CLI_REFERENCE.md, QML_DESKTOP_GUI.md\n```",
 "tests": "116 (`python -m pytest tests -q`, 4 skipped)",
 "requirements": [
  "Python 3.10+",
  "`git` and the build tools of the repositories you install",
  "optional: PySide6 for the desktop shell"
 ]
}

TEXT = {
 "en": {
  "tagline": "Detects, installs and updates every A.R.M.O.R. repository on the machine it runs on (a Python program with no required dependencies, built for a private ecosystem from the start)",
  "honest": "The manifest discovery, version comparison, signature check, atomic-by-verification install and update, evidence log and the eight-language interface tables are tested (116 tests, 4 skipped without a display), and the Qt Quick shell has been run on Windows. It has not been run against every repository of the family end to end, and the installs it makes need `git` and each repository's own build tools on the machine.",
  "bullets": [
   "**Discovery, no fixed list:** a local folder joins the moment it carries a valid `armor.project.json` declaring `ecosystem: \"A.R.M.O.R.\"`; remotely, every repository a `GITHUB_TOKEN` can see on GitHub is checked the same way - every A.R.M.O.R. repository is private, so that token is required throughout, with no 60-requests-an-hour fallback a public ecosystem could fall back to.",
   "**Install and update, never in place:** an update is built and verified in an independent staging clone first, and only promoted - two directory renames, the previous install kept as a backup - once that build actually succeeds; a genuinely uncommitted local edit is refused outright, never silently discarded.",
   "**Evidence:** every attempt, successful or not, appends one line to a local log with the project, the version and commit before and after, and the reason for a failure.",
   "**A CLI and an optional desktop shell:** `armor-updater status`/`install`/`update`, and a Qt Quick interface (`pip install \".[gui]\"`) in the ecosystem's eight languages."
  ],
  "note": "See `docs/CLI_REFERENCE.md`.\n\nSee `CONTRIBUTING.md` for how a repository joins the ecosystem `armor.project.json` describes.",
  "fit": "ARMOR-UPDATER is the desktop tool for the person who keeps a copy of the family on a PC: it finds the A.R.M.O.R. repositories on the machine, compares them with GitHub and installs or updates one at a time, verifying before it replaces anything. It is separate from the updates that [ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) drives on the CM5 (those go through [ARMOR-DEVOPS](https://github.com/JuanenRac/ARMOR-DEVOPS)): this one is for a developer's machine.",
  "hardware": "Not applicable: it is a desktop program; its Qt Quick shell has been run on Windows"
 },
 "es": {
  "tagline": "Detecta, instala y actualiza cada repositorio de A.R.M.O.R. en la máquina donde se ejecuta (un programa en Python sin dependencias obligatorias, construido desde cero para un ecosistema privado)",
  "honest": "El descubrimiento por manifiesto, la comparación de versiones, la comprobación de firma, la instalación y actualización atómica por verificación, el registro de evidencias y las tablas de la interfaz en ocho idiomas están probados (116 tests, 4 omitidos sin pantalla), y la interfaz Qt Quick se ha ejecutado en Windows. No se ha ejecutado contra todos los repositorios de la familia de principio a fin, y las instalaciones que hace necesitan `git` y las herramientas de compilación de cada repositorio en la máquina.",
  "bullets": [
   "**Descubrimiento, sin lista fija:** una carpeta local se une en cuanto lleva un `armor.project.json` válido que declara `ecosystem: \"A.R.M.O.R.\"`; en remoto, se revisa igual cada repositorio que un `GITHUB_TOKEN` pueda ver en GitHub - todos los repositorios de A.R.M.O.R. son privados, así que ese token es obligatorio en todo momento, sin el respaldo de 60 peticiones a la hora al que recurriría un ecosistema público.",
   "**Instalar y actualizar, nunca en el sitio:** una actualización se construye y verifica primero en un clon de ensayo independiente, y solo se promueve -dos renombrados de carpeta, la instalación anterior guardada como copia de seguridad- cuando esa construcción realmente tiene éxito; un cambio local de verdad sin commitear se rechaza sin más, nunca se descarta en silencio.",
   "**Evidencia:** cada intento, con éxito o no, añade una línea a un registro local con el proyecto, la versión y el commit antes y después, y el motivo de un fallo.",
   "**Una CLI y una interfaz de escritorio opcional:** `armor-updater status`/`install`/`update`, y una interfaz Qt Quick (`pip install \".[gui]\"`) en los ocho idiomas del ecosistema."
  ],
  "note": "See `docs/CLI_REFERENCE.md`.\n\nVer `CONTRIBUTING.md` para saber cómo se une un repositorio al ecosistema que describe `armor.project.json`.",
  "fit": "ARMOR-UPDATER es la herramienta de escritorio para quien guarda una copia de la familia en un PC: encuentra los repositorios A.R.M.O.R. de la máquina, los compara con GitHub e instala o actualiza uno a uno, verificando antes de sustituir nada. Es distinta de las actualizaciones que [ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) gobierna en la CM5 (esas pasan por [ARMOR-DEVOPS](https://github.com/JuanenRac/ARMOR-DEVOPS)): esta es para la máquina de un desarrollador.",
  "hardware": "No aplica: es un programa de escritorio; su interfaz Qt Quick se ha ejecutado en Windows"
 },
 "fr": {
  "tagline": "Détecte, installe et met à jour chaque dépôt A.R.M.O.R. sur la machine où il s'exécute (un programme Python sans dépendance obligatoire, conçu depuis le départ pour un écosystème privé)",
  "honest": "La découverte par manifeste, la comparaison de versions, la vérification de signature, l'installation et la mise à jour atomiques par vérification, le journal de preuves et les tables de l'interface en huit langues sont testés (116 tests, 4 ignorés sans écran), et l'interface Qt Quick a été exécutée sous Windows. Elle n'a pas été exécutée de bout en bout contre tous les dépôts de la famille, et les installations qu'elle fait demandent `git` et les outils de compilation de chaque dépôt sur la machine.",
  "bullets": [
   "**Découverte, sans liste fixe :** un dossier local rejoint l'écosystème dès qu'il porte un `armor.project.json` valide déclarant `ecosystem: \"A.R.M.O.R.\"` ; à distance, chaque dépôt qu'un `GITHUB_TOKEN` peut voir sur GitHub est vérifié de la même façon - chaque dépôt A.R.M.O.R. étant privé, ce jeton est requis partout, sans le repli à 60 requêtes par heure d'un écosystème public.",
   "**Installer et mettre à jour, jamais sur place :** une mise à jour est construite et vérifiée d'abord dans un clone de test indépendant, et n'est promue - deux renommages de dossier, l'installation précédente gardée en sauvegarde - qu'une fois cette construction réellement réussie ; une modification locale réellement non validée est refusée d'emblée, jamais silencieusement écartée.",
   "**Preuves :** chaque tentative, réussie ou non, ajoute une ligne à un journal local avec le projet, la version et le commit avant et après, et la raison d'un échec.",
   "**Une CLI et une interface de bureau optionnelle :** `armor-updater status`/`install`/`update`, et une interface Qt Quick (`pip install \".[gui]\"`) dans les huit langues de l'écosystème."
  ],
  "note": "See `docs/CLI_REFERENCE.md`.\n\nVoir `CONTRIBUTING.md` pour savoir comment un dépôt rejoint l'écosystème que décrit `armor.project.json`.",
  "fit": "ARMOR-UPDATER est l'outil de bureau pour qui garde une copie de la famille sur un PC : il trouve les dépôts A.R.M.O.R. de la machine, les compare à GitHub et installe ou met à jour un par un, en vérifiant avant de remplacer quoi que ce soit. Il est distinct des mises à jour qu'[ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) pilote sur le CM5 (celles-ci passent par [ARMOR-DEVOPS](https://github.com/JuanenRac/ARMOR-DEVOPS)) : celui-ci est pour la machine d'un développeur.",
  "hardware": "Sans objet : c'est un programme de bureau ; son interface Qt Quick a été exécutée sous Windows"
 },
 "it": {
  "tagline": "Rileva, installa e aggiorna ogni repository A.R.M.O.R. sulla macchina su cui viene eseguito (un programma Python senza dipendenze obbligatorie, costruito da zero per un ecosistema privato)",
  "honest": "La scoperta tramite manifesto, il confronto delle versioni, il controllo della firma, l'installazione e l'aggiornamento atomici per verifica, il registro delle prove e le tabelle dell'interfaccia in otto lingue sono provati (116 test, 4 saltati senza schermo), e l'interfaccia Qt Quick è stata eseguita su Windows. Non è stata eseguita da capo a fondo contro tutti i repository della famiglia, e le installazioni che fa richiedono `git` e gli strumenti di compilazione di ogni repository sulla macchina.",
  "bullets": [
   "**Scoperta, senza elenco fisso:** una cartella locale entra a far parte dell'ecosistema non appena porta un `armor.project.json` valido che dichiara `ecosystem: \"A.R.M.O.R.\"`; da remoto, ogni repository che un `GITHUB_TOKEN` può vedere su GitHub viene controllato allo stesso modo - ogni repository A.R.M.O.R. è privato, quindi quel token è sempre obbligatorio, senza il ripiego di 60 richieste all'ora di un ecosistema pubblico.",
   "**Installare e aggiornare, mai sul posto:** un aggiornamento viene prima costruito e verificato in un clone di staging indipendente, e viene promosso - due rinomine di cartella, l'installazione precedente conservata come backup - solo quando quella build ha davvero successo; una modifica locale realmente non committata viene rifiutata subito, mai scartata in silenzio.",
   "**Prove:** ogni tentativo, riuscito o no, aggiunge una riga a un registro locale con il progetto, la versione e il commit prima e dopo, e il motivo di un fallimento.",
   "**Una CLI e un'interfaccia desktop opzionale:** `armor-updater status`/`install`/`update`, e un'interfaccia Qt Quick (`pip install \".[gui]\"`) nelle otto lingue dell'ecosistema."
  ],
  "note": "See `docs/CLI_REFERENCE.md`.\n\nVedi `CONTRIBUTING.md` per come un repository entra a far parte dell'ecosistema descritto da `armor.project.json`.",
  "fit": "ARMOR-UPDATER è lo strumento da scrivania per chi tiene una copia della famiglia su un PC: trova i repository A.R.M.O.R. della macchina, li confronta con GitHub e installa o aggiorna uno alla volta, verificando prima di sostituire qualcosa. È distinto dagli aggiornamenti che [ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) guida sulla CM5 (quelli passano per [ARMOR-DEVOPS](https://github.com/JuanenRac/ARMOR-DEVOPS)): questo è per la macchina di uno sviluppatore.",
  "hardware": "Non applicabile: è un programma da scrivania; la sua interfaccia Qt Quick è stata eseguita su Windows"
 },
 "de": {
  "tagline": "Erkennt, installiert und aktualisiert jedes A.R.M.O.R.-Repository auf dem Rechner, auf dem es läuft (ein Python-Programm ohne zwingende Abhängigkeiten, von Grund auf für ein privates Ökosystem gebaut)",
  "honest": "Die Manifest-Erkennung, der Versionsvergleich, die Signaturprüfung, die atomare Installation und das Update per Verifikation, das Beweisprotokoll und die Oberflächentabellen in acht Sprachen sind getestet (116 Tests, 4 ohne Bildschirm übersprungen), und die Qt-Quick-Oberfläche wurde unter Windows ausgeführt. Sie wurde nicht durchgängig gegen alle Repositorys der Familie ausgeführt, und ihre Installationen brauchen `git` und die Build-Werkzeuge jedes Repositorys auf der Maschine.",
  "bullets": [
   "**Erkennung, ohne feste Liste:** ein lokaler Ordner tritt dem Ökosystem bei, sobald er ein gültiges `armor.project.json` mit `ecosystem: \"A.R.M.O.R.\"` trägt; entfernt wird jedes Repository, das ein `GITHUB_TOKEN` auf GitHub sehen kann, genauso geprüft - jedes A.R.M.O.R.-Repository ist privat, daher ist dieses Token überall erforderlich, ohne den 60-Anfragen-pro-Stunde-Rückfall eines öffentlichen Ökosystems.",
   "**Installieren und aktualisieren, nie an Ort und Stelle:** eine Aktualisierung wird zuerst in einem unabhängigen Staging-Klon gebaut und verifiziert und erst befördert - zwei Ordnerumbenennungen, die vorherige Installation als Sicherung behalten -, sobald dieser Build tatsächlich gelingt; eine echte, nicht committete lokale Änderung wird von vornherein abgelehnt, nie stillschweigend verworfen.",
   "**Nachweis:** jeder Versuch, erfolgreich oder nicht, fügt einer lokalen Protokolldatei eine Zeile mit Projekt, Version und Commit davor und danach sowie dem Grund eines Fehlschlags hinzu.",
   "**Eine CLI und eine optionale Desktop-Oberfläche:** `armor-updater status`/`install`/`update`, sowie eine Qt-Quick-Oberfläche (`pip install \".[gui]\"`) in den acht Sprachen des Ökosystems."
  ],
  "note": "See `docs/CLI_REFERENCE.md`.\n\nSiehe `CONTRIBUTING.md`, wie ein Repository dem Ökosystem beitritt, das `armor.project.json` beschreibt.",
  "fit": "ARMOR-UPDATER ist das Desktop-Werkzeug für alle, die eine Kopie der Familie auf einem PC halten: Es findet die A.R.M.O.R.-Repositorys der Maschine, vergleicht sie mit GitHub und installiert oder aktualisiert eines nach dem anderen und prüft, bevor es etwas ersetzt. Es ist getrennt von den Updates, die [ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) auf dem CM5 steuert (die laufen über [ARMOR-DEVOPS](https://github.com/JuanenRac/ARMOR-DEVOPS)): dieses ist für die Maschine eines Entwicklers.",
  "hardware": "Nicht zutreffend: es ist ein Desktop-Programm; seine Qt-Quick-Oberfläche wurde unter Windows ausgeführt"
 },
 "zh": {
  "tagline": "在运行它的机器上发现、安装并更新每一个 A.R.M.O.R. 仓库(一个不需要依赖的 Python 程序,从一开始就为私有生态系统而设计)",
  "honest": "清单发现、版本比较、签名检查、按验证的原子安装和更新、证据日志以及八种语言的界面表格都经过测试（116 个测试，无显示器时跳过 4 个），Qt Quick 界面已在 Windows 上运行过。它还没有对家族的所有仓库端到端运行过，它所做的安装需要机器上有 `git` 和各仓库自己的构建工具。",
  "bullets": [
   "**发现,没有固定列表:** 本地文件夹只要携带一个有效的、声明 `ecosystem: \"A.R.M.O.R.\"` 的 `armor.project.json` 就会加入;远程方面,`GITHUB_TOKEN` 能在 GitHub 上看到的每一个仓库都以同样方式核实——每个 A.R.M.O.R. 仓库都是私有的,所以这个令牌始终是必需的,没有公开生态系统那种每小时 60 次请求的退路。",
   "**安装与更新,从不就地进行:** 更新先在一个独立的暂存克隆中构建并验证,只有在构建真正成功后才会被提升——两次目录改名,原来的安装保留为备份;真正未提交的本地改动会被直接拒绝,绝不会被悄悄丢弃。",
   "**证据:** 每一次尝试,无论成功与否,都会在本地日志里追加一行,记录项目、前后的版本与提交,以及失败的原因。",
   "**一个命令行工具和一个可选的桌面界面:** `armor-updater status`/`install`/`update`,以及一个 Qt Quick 界面(`pip install \".[gui]\"`),覆盖生态系统的八种语言。"
  ],
  "note": "See `docs/CLI_REFERENCE.md`.\n\n关于仓库如何加入 `armor.project.json` 描述的生态系统,见 `CONTRIBUTING.md`。",
  "fit": "ARMOR-UPDATER 是为在 PC 上保存家族副本的人准备的桌面工具：它找出机器上的 A.R.M.O.R. 仓库，与 GitHub 对比，并逐个安装或更新，替换任何东西之前都先验证。它与 [ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) 在 CM5 上驱动的更新不同（那些经过 [ARMOR-DEVOPS](https://github.com/JuanenRac/ARMOR-DEVOPS)）：这个是给开发者的机器用的。",
  "hardware": "不适用：这是桌面程序；其 Qt Quick 界面已在 Windows 上运行过"
 },
 "ja": {
  "tagline": "実行しているマシン上であらゆる A.R.M.O.R. リポジトリを検出し、インストールし、更新する(必須の依存関係のない Python プログラムで、最初から非公開のエコシステム向けに作られたもの)",
  "honest": "マニフェストによる検出、バージョン比較、署名検査、検証によるアトミックなインストールと更新、証拠ログ、8 言語のインターフェース表はテストされ（116 件、ディスプレイなしでは 4 件スキップ）、Qt Quick シェルは Windows で動かしました。ファミリーのすべてのリポジトリに対して最初から最後まで実行したわけではなく、そのインストールにはマシン上の `git` と各リポジトリのビルドツールが必要です。",
  "bullets": [
   "**固定リストのない発見:** ローカルのフォルダは `ecosystem: \"A.R.M.O.R.\"` を宣言する有効な `armor.project.json` を持てばその時点でエコシステムに加わる。リモートでは `GITHUB_TOKEN` が GitHub 上で見られるすべてのリポジトリを同じ方法で確認する — すべての A.R.M.O.R. リポジトリは非公開なので、このトークンは常に必須であり、公開エコシステムのような 1 時間 60 リクエストという代替手段は存在しない。",
   "**その場では行わないインストールと更新:** 更新はまず独立したステージング用クローンで構築・検証され、そのビルドが実際に成功したときにのみ昇格される — 2 回のディレクトリ名変更で、以前のインストールはバックアップとして残される。本当にコミットされていないローカルの変更は即座に拒否され、黙って捨てられることはない。",
   "**証跡:** 成功・失敗を問わず、すべての試行はプロジェクト名、前後のバージョンとコミット、失敗の理由をローカルのログに一行追加する。",
   "**CLI と任意のデスクトップシェル:** `armor-updater status`/`install`/`update`、およびエコシステムの 8 言語に対応した Qt Quick インターフェース(`pip install \".[gui]\"`)。"
  ],
  "note": "See `docs/CLI_REFERENCE.md`.\n\nリポジトリが `armor.project.json` の説明するエコシステムに加わる方法は `CONTRIBUTING.md` を参照。",
  "fit": "ARMOR-UPDATER は、PC にファミリーのコピーを持つ人のためのデスクトップツールです。マシン上の A.R.M.O.R. リポジトリを見つけ、GitHub と比較し、何かを置き換える前に検証しながら 1 つずつインストール・更新します。[ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) が CM5 上で行う更新（[ARMOR-DEVOPS](https://github.com/JuanenRac/ARMOR-DEVOPS) を通るもの）とは別で、これは開発者のマシン用です。",
  "hardware": "該当なし：デスクトッププログラムで、Qt Quick シェルは Windows で動かしました"
 },
 "pt": {
  "tagline": "Deteta, instala e atualiza cada repositório A.R.M.O.R. da máquina onde corre (um programa Python sem dependências obrigatórias, feito desde o início para um ecossistema privado)",
  "honest": "A descoberta por manifesto, a comparação de versões, a verificação da assinatura, a instalação e atualização atómicas por verificação, o registo de provas e as tabelas da interface em oito idiomas estão testados (116 testes, 4 ignorados sem ecrã), e a interface Qt Quick foi executada no Windows. Não foi executada de ponta a ponta contra todos os repositórios da família, e as instalações que faz precisam de `git` e das ferramentas de compilação de cada repositório na máquina.",
  "bullets": [
   "**Deteção, sem lista fixa:** uma pasta local junta-se no momento em que traz um `armor.project.json` válido que declare `ecosystem: \"A.R.M.O.R.\"`; remotamente, cada repositório que um `GITHUB_TOKEN` veja no GitHub verifica-se da mesma forma - todos os repositórios A.R.M.O.R. são privados, por isso esse token é necessário em todo o lado, sem o recurso de 60 pedidos por hora que um ecossistema público poderia usar.",
   "**Instalar e atualizar, nunca no local:** uma atualização constrói-se e verifica-se primeiro num clone de preparação independente, e só se promove - duas mudanças de nome de pasta, ficando a instalação anterior como cópia de segurança - quando essa construção realmente tem êxito; uma edição local realmente por confirmar recusa-se à partida, nunca se descarta em silêncio.",
   "**Provas:** cada tentativa, bem-sucedida ou não, acrescenta uma linha a um registo local com o projeto, a versão e o commit antes e depois, e o motivo de uma falha.",
   "**Uma CLI e uma consola de ambiente de trabalho opcional:** `armor-updater status`/`install`/`update`, e uma interface Qt Quick (`pip install \".[gui]\"`) nos oito idiomas do ecossistema."
  ],
  "note": "Veja `docs/CLI_REFERENCE.md`.\n\nVeja `CONTRIBUTING.md` para saber como um repositório se junta ao ecossistema que o `armor.project.json` descreve.",
  "fit": "O ARMOR-UPDATER é a ferramenta de ambiente de trabalho para quem guarda uma cópia da família num PC: encontra os repositórios A.R.M.O.R. da máquina, compara-os com o GitHub e instala ou atualiza um a um, verificando antes de substituir seja o que for. É distinto das atualizações que o [ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) comanda no CM5 (essas passam pelo [ARMOR-DEVOPS](https://github.com/JuanenRac/ARMOR-DEVOPS)): este é para a máquina de um programador.",
  "hardware": "Não se aplica: é um programa de ambiente de trabalho; a sua interface Qt Quick foi executada no Windows"
 }
}
