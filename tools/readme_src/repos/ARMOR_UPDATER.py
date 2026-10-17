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
   "140",
   "2ea44f"
  ]
 ],
 "diagram": "",
 "build": "```bash\npip install -e \".[dev]\"                                # or \".[dev,gui]\" for the optional Qt Quick desktop shell\npython -m pytest tests -q                              # 140 tests\narmor-updater --cli status                              # local + GitHub state of every repository\narmor-updater --cli install ARMOR-NETWORK               # clone, build and install one repository that is not installed yet\narmor-updater --cli update ARMOR-NETWORK                # update an installed one (built and verified before it is put in place)\narmor-updater --cli rollback ARMOR-NETWORK              # put the newest backup of a replaced checkout back\n```",
 "structure": "```text\nARMOR-UPDATER/\n├── src/armor_updater/  project_manifest, registry, detect (local), github_client, install (staged install and update) + promotion (lock, journal, backups), signature (signed updates), evidence, main (CLI), settings, version_parse,\n│                       i18n + i18n_pt (eight languages), gui / qt_gui / qml (the Qt Quick shell)\n├── tools/              armor_ci_validate.py, _armor_readme_parity.py, armor_project_tool.py (vendored from ARMOR-COMMON), generate_app_icon.py\n├── tests/              13 test modules\n└── docs/               CLI_REFERENCE.md, QML_DESKTOP_GUI.md\n```",
 "tests": "140 (`python -m pytest tests -q`)",
 "requirements": [
  "Python 3.10+",
  "`git` and the build tools of the repositories you install",
  "optional: PySide6 for the desktop shell"
 ]
}

TEXT = {
 "en": {
  "tagline": "Detects, installs and updates every A.R.M.O.R. repository on the machine it runs on (a Python program with no required dependencies)",
  "honest": "The manifest discovery, the version comparison, the signature check, the staged install and update with its lock, journal, backups and rollback, the evidence log and the eight-language interface tables are tested (140 tests), and the Qt Quick shell has been run on Windows. It has not been run against every repository of the family end to end, and the installs it makes need `git` and each repository's own build tools on the machine.",
  "bullets": [
   "**Discovery, no fixed list:** a local folder joins the moment it carries a valid `armor.project.json` declaring `ecosystem: \"A.R.M.O.R.\"`; remotely, every public repository of the account is checked the same way. A `GITHUB_TOKEN` is optional: it only raises GitHub's limit of 60 requests an hour.",
   "**Install and update, never in place:** a new project and an update are both built and verified in an independent staging clone first, and only promoted - two journalled renames, the replaced checkout kept as a backup under `.armor-updater/backups/` (the newest three) - once that build succeeds; an update to the commit already installed does nothing; a genuinely uncommitted local edit is refused outright, never silently discarded; a crash between the renames is healed at the next run, and `rollback` puts the newest backup back.",
   "**One at a time, and ordered:** a lock stops two updaters working on a workspace together; a batch goes ARMOR-COMMON first (every build needs it), and a project is not built without it.",
   "**Evidence:** every attempt, successful or not, appends one line to a local log with the project, the version and commit before and after, and the reason for a failure.",
   "**A CLI and an optional desktop shell:** `armor-updater status`/`install`/`update`, and a Qt Quick interface (`pip install \".[gui]\"`) in the ecosystem's eight languages."
  ],
  "note": "See `docs/CLI_REFERENCE.md`.",
  "fit": "ARMOR-UPDATER is the desktop tool for the person who keeps a copy of the family on a PC: it finds the A.R.M.O.R. repositories on the machine, compares them with GitHub and installs or updates one at a time, verifying before it replaces anything. It is separate from the updates that [ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) drives on the CM5 (those go through [ARMOR-DEVOPS](https://github.com/JuanenRac/ARMOR-DEVOPS)): this one is for a developer's machine.",
  "hardware": "Not applicable: it is a desktop program; its Qt Quick shell has been run on Windows"
 },
 "es": {
  "tagline": "Detecta, instala y actualiza cada repositorio de A.R.M.O.R. en la máquina donde se ejecuta (un programa en Python sin dependencias obligatorias)",
  "honest": "El descubrimiento por manifiesto, la comparación de versiones, la comprobación de firma, la instalación y actualización por etapas con su bloqueo, su diario, sus copias y su vuelta atrás, el registro de evidencias y las tablas de la interfaz en ocho idiomas están probados (140 tests), y la interfaz Qt Quick se ha ejecutado en Windows. No se ha ejecutado contra todos los repositorios de la familia de principio a fin, y las instalaciones que hace necesitan `git` y las herramientas de compilación de cada repositorio en la máquina.",
  "bullets": [
   "**Descubrimiento, sin lista fija:** una carpeta local se une en cuanto lleva un `armor.project.json` válido que declara `ecosystem: \"A.R.M.O.R.\"`; en remoto, se revisa igual cada repositorio público de la cuenta. Un `GITHUB_TOKEN` es opcional: solo sube el límite de 60 peticiones a la hora de GitHub.",
   "**Instalar y actualizar, nunca en el sitio:** un proyecto nuevo y una actualización se construyen y verifican primero en un clon de ensayo independiente, y solo se promueven -dos renombrados con diario, la copia reemplazada guardada en `.armor-updater/backups/` (las tres más recientes)- cuando esa construcción tiene éxito; actualizar al commit ya instalado no hace nada; un cambio local de verdad sin commitear se rechaza sin más, nunca se descarta en silencio; un fallo entre los renombrados se repara en la siguiente ejecución, y `rollback` devuelve la copia más reciente.",
   "**De uno en uno y en orden:** un bloqueo impide que dos actualizadores trabajen a la vez en un espacio de trabajo; un lote empieza por ARMOR-COMMON (todas las construcciones lo necesitan) y no se construye un proyecto sin él.",
   "**Evidencia:** cada intento, con éxito o no, añade una línea a un registro local con el proyecto, la versión y el commit antes y después, y el motivo de un fallo.",
   "**Una CLI y una interfaz de escritorio opcional:** `armor-updater status`/`install`/`update`, y una interfaz Qt Quick (`pip install \".[gui]\"`) en los ocho idiomas del ecosistema."
  ],
  "note": "Véase `docs/CLI_REFERENCE.md`.",
  "fit": "ARMOR-UPDATER es la herramienta de escritorio para quien guarda una copia de la familia en un PC: encuentra los repositorios A.R.M.O.R. de la máquina, los compara con GitHub e instala o actualiza uno a uno, verificando antes de sustituir nada. Es distinta de las actualizaciones que [ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) gobierna en la CM5 (esas pasan por [ARMOR-DEVOPS](https://github.com/JuanenRac/ARMOR-DEVOPS)): esta es para la máquina de un desarrollador.",
  "hardware": "No aplica: es un programa de escritorio; su interfaz Qt Quick se ha ejecutado en Windows"
 },
 "fr": {
  "tagline": "Détecte, installe et met à jour chaque dépôt A.R.M.O.R. sur la machine où il tourne (un programme Python sans dépendance obligatoire)",
  "honest": "La découverte par manifeste, la comparaison des versions, la vérification de signature, l'installation et la mise à jour par étapes avec leur verrou, leur journal, leurs sauvegardes et leur retour arrière, le journal de preuves et les tables de l'interface en huit langues sont testés (140 tests), et l'interface Qt Quick a tourné sous Windows. Elle n'a pas été exécutée de bout en bout sur chaque dépôt de la famille, et les installations qu'elle fait exigent `git` et les outils de compilation de chaque dépôt sur la machine.",
  "bullets": [
   "**Découverte, sans liste fixe :** un dossier local rejoint l'écosystème dès qu'il porte un `armor.project.json` valide déclarant `ecosystem: \"A.R.M.O.R.\"` ; à distance, chaque dépôt public du compte est examiné de la même façon. Un `GITHUB_TOKEN` est facultatif : il relève seulement la limite de 60 requêtes par heure de GitHub.",
   "**Installer et mettre à jour, jamais sur place :** un nouveau projet et une mise à jour sont d'abord construits et vérifiés dans un clone de préparation indépendant, puis promus seulement - deux renommages journalisés, la copie remplacée gardée sous `.armor-updater/backups/` (les trois plus récentes) - quand cette construction réussit ; une mise à jour vers le commit déjà installé ne fait rien ; une vraie modification locale non validée est refusée net, jamais écartée en silence ; une panne entre les renommages est réparée à l'exécution suivante, et `rollback` remet la copie la plus récente.",
   "**Un à la fois, et dans l'ordre :** un verrou empêche deux outils de travailler ensemble sur un espace de travail ; un lot commence par ARMOR-COMMON (toute construction en a besoin) et un projet n'est pas construit sans lui.",
   "**Preuves :** chaque tentative, réussie ou non, ajoute une ligne à un journal local avec le projet, la version et le commit avant et après, et la raison d'un échec.",
   "**Une CLI et une interface de bureau optionnelle :** `armor-updater status`/`install`/`update`, et une interface Qt Quick (`pip install \".[gui]\"`) dans les huit langues de l'écosystème."
  ],
  "note": "Voir `docs/CLI_REFERENCE.md`.",
  "fit": "ARMOR-UPDATER est l'outil de bureau pour qui garde une copie de la famille sur un PC : il trouve les dépôts A.R.M.O.R. de la machine, les compare à GitHub et installe ou met à jour un par un, en vérifiant avant de remplacer quoi que ce soit. Il est distinct des mises à jour qu'[ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) pilote sur le CM5 (celles-ci passent par [ARMOR-DEVOPS](https://github.com/JuanenRac/ARMOR-DEVOPS)) : celui-ci est pour la machine d'un développeur.",
  "hardware": "Sans objet : c'est un programme de bureau ; son interface Qt Quick a été exécutée sous Windows"
 },
 "it": {
  "tagline": "Rileva, installa e aggiorna ogni repository A.R.M.O.R. sulla macchina in cui gira (un programma Python senza dipendenze obbligatorie)",
  "honest": "La scoperta per manifesto, il confronto delle versioni, il controllo della firma, l'installazione e l'aggiornamento a tappe con il loro blocco, il loro diario, le copie e il ritorno indietro, il registro delle prove e le tabelle dell'interfaccia in otto lingue sono testati (140 test), e l'interfaccia Qt Quick è stata eseguita su Windows. Non è stata eseguita su ogni repository della famiglia da cima a fondo, e le installazioni che fa richiedono `git` e gli strumenti di compilazione di ciascun repository sulla macchina.",
  "bullets": [
   "**Scoperta, senza elenco fisso:** una cartella locale entra appena porta un `armor.project.json` valido che dichiara `ecosystem: \"A.R.M.O.R.\"`; da remoto, ogni repository pubblico dell'account è controllato allo stesso modo. Un `GITHUB_TOKEN` è facoltativo: alza solo il limite di 60 richieste l'ora di GitHub.",
   "**Installare e aggiornare, mai sul posto:** un nuovo progetto e un aggiornamento sono prima costruiti e verificati in un clone di prova indipendente, e promossi solo - due rinominazioni registrate, la copia sostituita conservata in `.armor-updater/backups/` (le tre più recenti) - quando quella costruzione riesce; un aggiornamento al commit già installato non fa nulla; una vera modifica locale non salvata è rifiutata senza mezzi termini, mai scartata in silenzio; un guasto tra le rinominazioni viene riparato alla prossima esecuzione, e `rollback` rimette la copia più recente.",
   "**Uno alla volta, e in ordine:** un blocco impedisce a due aggiornatori di lavorare insieme su uno spazio di lavoro; un lotto parte da ARMOR-COMMON (ogni costruzione ne ha bisogno) e un progetto non viene costruito senza di esso.",
   "**Prove:** ogni tentativo, riuscito o no, aggiunge una riga a un registro locale con il progetto, la versione e il commit prima e dopo, e il motivo di un fallimento.",
   "**Una CLI e un'interfaccia desktop opzionale:** `armor-updater status`/`install`/`update`, e un'interfaccia Qt Quick (`pip install \".[gui]\"`) nelle otto lingue dell'ecosistema."
  ],
  "note": "Vedi `docs/CLI_REFERENCE.md`.",
  "fit": "ARMOR-UPDATER è lo strumento da scrivania per chi tiene una copia della famiglia su un PC: trova i repository A.R.M.O.R. della macchina, li confronta con GitHub e installa o aggiorna uno alla volta, verificando prima di sostituire qualcosa. È distinto dagli aggiornamenti che [ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) guida sulla CM5 (quelli passano per [ARMOR-DEVOPS](https://github.com/JuanenRac/ARMOR-DEVOPS)): questo è per la macchina di uno sviluppatore.",
  "hardware": "Non applicabile: è un programma da scrivania; la sua interfaccia Qt Quick è stata eseguita su Windows"
 },
 "de": {
  "tagline": "Erkennt, installiert und aktualisiert jedes A.R.M.O.R.-Repository auf dem Rechner, auf dem es läuft (ein Python-Programm ohne Pflichtabhängigkeiten)",
  "honest": "Die Manifest-Erkennung, der Versionsvergleich, die Signaturprüfung, die gestufte Installation und Aktualisierung mit Sperre, Journal, Sicherungen und Rückkehr, das Nachweisprotokoll und die Oberflächentabellen in acht Sprachen sind getestet (140 Tests), und die Qt-Quick-Oberfläche lief unter Windows. Sie wurde nicht gegen jedes Repository der Familie von Anfang bis Ende ausgeführt, und die Installationen brauchen `git` und die Build-Werkzeuge jedes Repositorys auf dem Rechner.",
  "bullets": [
   "**Erkennung ohne feste Liste:** Ein lokaler Ordner gehört dazu, sobald er ein gültiges `armor.project.json` mit `ecosystem: \"A.R.M.O.R.\"` trägt; entfernt wird jedes öffentliche Repository des Kontos genauso geprüft. Ein `GITHUB_TOKEN` ist optional: Er hebt nur GitHubs Grenze von 60 Anfragen pro Stunde an.",
   "**Installieren und aktualisieren, nie an Ort und Stelle:** Ein neues Projekt und eine Aktualisierung werden zuerst in einem unabhängigen Staging-Klon gebaut und geprüft und erst danach übernommen - zwei protokollierte Umbenennungen, die ersetzte Kopie unter `.armor-updater/backups/` aufbewahrt (die drei neuesten) -, wenn der Build gelingt; eine Aktualisierung auf den schon installierten Commit tut nichts; eine echte nicht eingecheckte lokale Änderung wird glatt abgelehnt, nie stillschweigend verworfen; ein Absturz zwischen den Umbenennungen wird beim nächsten Lauf geheilt, und `rollback` stellt die neueste Kopie wieder her.",
   "**Eines nach dem anderen, und der Reihe nach:** Eine Sperre verhindert, dass zwei Updater gleichzeitig an einem Arbeitsbereich arbeiten; ein Stapel beginnt mit ARMOR-COMMON (jeder Build braucht es), und ein Projekt wird ohne es nicht gebaut.",
   "**Nachweis:** jeder Versuch, erfolgreich oder nicht, fügt einer lokalen Protokolldatei eine Zeile mit Projekt, Version und Commit davor und danach sowie dem Grund eines Fehlschlags hinzu.",
   "**Eine CLI und eine optionale Desktop-Oberfläche:** `armor-updater status`/`install`/`update`, sowie eine Qt-Quick-Oberfläche (`pip install \".[gui]\"`) in den acht Sprachen des Ökosystems."
  ],
  "note": "Siehe `docs/CLI_REFERENCE.md`.",
  "fit": "ARMOR-UPDATER ist das Desktop-Werkzeug für alle, die eine Kopie der Familie auf einem PC halten: Es findet die A.R.M.O.R.-Repositorys der Maschine, vergleicht sie mit GitHub und installiert oder aktualisiert eines nach dem anderen und prüft, bevor es etwas ersetzt. Es ist getrennt von den Updates, die [ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) auf dem CM5 steuert (die laufen über [ARMOR-DEVOPS](https://github.com/JuanenRac/ARMOR-DEVOPS)): dieses ist für die Maschine eines Entwicklers.",
  "hardware": "Nicht zutreffend: es ist ein Desktop-Programm; seine Qt-Quick-Oberfläche wurde unter Windows ausgeführt"
 },
 "zh": {
  "tagline": "检测、安装并更新所在机器上的每个 A.R.M.O.R. 仓库（一个没有必需依赖的 Python 程序）",
  "honest": "清单发现、版本比较、签名检查、带锁、日志、备份和回退的分阶段安装与更新、证据日志以及八种语言的界面表格都已测试（140 个测试），Qt Quick 界面已在 Windows 上运行过。它没有对家族中的每个仓库从头到尾运行过，它所做的安装需要机器上有 `git` 和各仓库自己的构建工具。",
  "bullets": [
   "**无固定列表的发现：**本地文件夹只要带有声明 `ecosystem: \"A.R.M.O.R.\"` 的有效 `armor.project.json` 就会加入；远程则以同样方式检查账户的每个公开仓库。`GITHUB_TOKEN` 是可选的：它只是提高 GitHub 每小时 60 次请求的限制。",
   "**安装和更新，从不原地进行：**新项目和更新都先在独立的暂存克隆中构建并验证，构建成功后才升级——两次有日志的重命名，被替换的检出保存在 `.armor-updater/backups/`（最近三份）；更新到已安装的提交不会做任何事；真正未提交的本地修改会被直接拒绝，绝不会被悄悄丢弃；两次重命名之间的崩溃会在下次运行时修复，`rollback` 会放回最近的备份。",
   "**一次一个，并有顺序：**锁可防止两个更新器同时处理一个工作区；批量操作先处理 ARMOR-COMMON（每个构建都需要它），没有它就不会构建项目。",
   "**证据:** 每一次尝试,无论成功与否,都会在本地日志里追加一行,记录项目、前后的版本与提交,以及失败的原因。",
   "**一个命令行工具和一个可选的桌面界面:** `armor-updater status`/`install`/`update`,以及一个 Qt Quick 界面(`pip install \".[gui]\"`),覆盖生态系统的八种语言。"
  ],
  "note": "参见 `docs/CLI_REFERENCE.md`。",
  "fit": "ARMOR-UPDATER 是为在 PC 上保存家族副本的人准备的桌面工具：它找出机器上的 A.R.M.O.R. 仓库，与 GitHub 对比，并逐个安装或更新，替换任何东西之前都先验证。它与 [ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) 在 CM5 上驱动的更新不同（那些经过 [ARMOR-DEVOPS](https://github.com/JuanenRac/ARMOR-DEVOPS)）：这个是给开发者的机器用的。",
  "hardware": "不适用：这是桌面程序；其 Qt Quick 界面已在 Windows 上运行过"
 },
 "ja": {
  "tagline": "実行中のマシン上のすべての A.R.M.O.R. リポジトリを検出し、インストールし、更新します（必須の依存関係がない Python プログラム）",
  "honest": "マニフェストによる検出、バージョン比較、署名の確認、ロック・ジャーナル・バックアップ・ロールバックを備えた段階的なインストールと更新、証跡ログ、8 言語のインターフェース表はテスト済みです（140 件のテスト）。Qt Quick のシェルは Windows で実行されました。ファミリーのすべてのリポジトリに対して端から端まで実行したわけではなく、行うインストールにはマシンに `git` と各リポジトリ自身のビルドツールが必要です。",
  "bullets": [
   "**固定リストのない検出：**ローカルのフォルダーは、`ecosystem: \"A.R.M.O.R.\"` を宣言する有効な `armor.project.json` を持った時点で加わります。リモートでは、アカウントのすべての公開リポジトリが同じ方法で調べられます。`GITHUB_TOKEN` は任意で、GitHub の 1 時間 60 リクエストの上限を上げるだけです。",
   "**インストールも更新も、その場では行いません：**新しいプロジェクトも更新も、まず独立したステージングのクローンでビルドして検証し、ビルドが成功してから反映します。ジャーナルに記録された 2 回の名前変更を行い、置き換えたチェックアウトは `.armor-updater/backups/` に（最新の 3 件）保存されます。インストール済みと同じコミットへの更新は何もしません。コミットされていない実際のローカル変更は即座に拒否され、黙って破棄されることはありません。名前変更の間のクラッシュは次の実行で修復され、`rollback` は最新のバックアップを戻します。",
   "**一度に一つ、順番どおりに：**ロックにより、2 つの更新ツールが同じワークスペースで同時に動くことはありません。一括処理は ARMOR-COMMON から始まり（すべてのビルドが必要とします）、それがなければプロジェクトはビルドされません。",
   "**証跡:** 成功・失敗を問わず、すべての試行はプロジェクト名、前後のバージョンとコミット、失敗の理由をローカルのログに一行追加する。",
   "**CLI と任意のデスクトップシェル:** `armor-updater status`/`install`/`update`、およびエコシステムの 8 言語に対応した Qt Quick インターフェース(`pip install \".[gui]\"`)。"
  ],
  "note": "`docs/CLI_REFERENCE.md` を参照してください。",
  "fit": "ARMOR-UPDATER は、PC にファミリーのコピーを持つ人のためのデスクトップツールです。マシン上の A.R.M.O.R. リポジトリを見つけ、GitHub と比較し、何かを置き換える前に検証しながら 1 つずつインストール・更新します。[ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) が CM5 上で行う更新（[ARMOR-DEVOPS](https://github.com/JuanenRac/ARMOR-DEVOPS) を通るもの）とは別で、これは開発者のマシン用です。",
  "hardware": "該当なし：デスクトッププログラムで、Qt Quick シェルは Windows で動かしました"
 },
 "pt": {
  "tagline": "Deteta, instala e atualiza cada repositório A.R.M.O.R. na máquina onde corre (um programa em Python sem dependências obrigatórias)",
  "honest": "A descoberta por manifesto, a comparação de versões, a verificação de assinatura, a instalação e a atualização por etapas com o seu bloqueio, diário, cópias e volta atrás, o registo de evidências e as tabelas da interface em oito idiomas estão testados (140 testes), e a interface Qt Quick correu no Windows. Não foi executada contra todos os repositórios da família de ponta a ponta, e as instalações que faz precisam de `git` e das ferramentas de compilação de cada repositório na máquina.",
  "bullets": [
   "**Descoberta, sem lista fixa:** uma pasta local junta-se assim que tem um `armor.project.json` válido que declara `ecosystem: \"A.R.M.O.R.\"`; em remoto, cada repositório público da conta é verificado da mesma forma. Um `GITHUB_TOKEN` é opcional: só sobe o limite de 60 pedidos por hora do GitHub.",
   "**Instalar e atualizar, nunca no próprio sítio:** um projeto novo e uma atualização são primeiro construídos e verificados num clone de ensaio independente, e só depois promovidos - dois renomeamentos com diário, a cópia substituída guardada em `.armor-updater/backups/` (as três mais recentes) - quando essa construção tem êxito; atualizar para o commit já instalado não faz nada; uma alteração local a sério por commitar é recusada de vez, nunca descartada em silêncio; uma falha entre os renomeamentos é reparada na execução seguinte, e `rollback` repõe a cópia mais recente.",
   "**Um de cada vez, e por ordem:** um bloqueio impede que dois atualizadores trabalhem juntos num espaço de trabalho; um lote começa por ARMOR-COMMON (todas as construções precisam dele) e um projeto não é construído sem ele.",
   "**Provas:** cada tentativa, bem-sucedida ou não, acrescenta uma linha a um registo local com o projeto, a versão e o commit antes e depois, e o motivo de uma falha.",
   "**Uma CLI e uma consola de ambiente de trabalho opcional:** `armor-updater status`/`install`/`update`, e uma interface Qt Quick (`pip install \".[gui]\"`) nos oito idiomas do ecossistema."
  ],
  "note": "Veja `docs/CLI_REFERENCE.md`.",
  "fit": "O ARMOR-UPDATER é a ferramenta de ambiente de trabalho para quem guarda uma cópia da família num PC: encontra os repositórios A.R.M.O.R. da máquina, compara-os com o GitHub e instala ou atualiza um a um, verificando antes de substituir seja o que for. É distinto das atualizações que o [ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) comanda no CM5 (essas passam pelo [ARMOR-DEVOPS](https://github.com/JuanenRac/ARMOR-DEVOPS)): este é para a máquina de um programador.",
  "hardware": "Não se aplica: é um programa de ambiente de trabalho; a sua interface Qt Quick foi executada no Windows"
 }
}
