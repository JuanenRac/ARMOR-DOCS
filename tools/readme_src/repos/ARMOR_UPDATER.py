# The facts that do not depend on the language, and the words of every language, of ARMOR-UPDATER, in the universal README layout.
# Copyright (C) 2026 JuanenRac (Electro Hobby 3D). GPL-3.0-or-later.
from readme_src._kit import *  # noqa: F401,F403

FACTS = {'emoji': '🛠️',
 'layout': 'universal',
 'license_badge': 'License-GPL%203.0--or--later-blue',
 'status': [['software', 'yellow'], ['tests', 'green'], ['ui', 'yellow'], ['security', 'yellow'], ['updates', 'yellow'], ['docs', 'green']],
 'badges': [['Language', 'Python%203.10%2B', '3776ab'], ['Dependencies', 'none', '2ea44f'], ['Languages', '8', '00E5FF'], ['Tests', '288', '2ea44f']]}

# the sentences of the previous layout that the new one keeps (already written in the eight languages)
LEGACY = {'en': {'tagline': 'Detects, installs and updates every A.R.M.O.R. repository on the machine it runs on (a Python program with no required dependencies)',
        'status': {'software': 'The manifest discovery, the version comparison and the staged install and update work; they have not been run end to end against every '
                               'repository of the family.',
                   'tests': '288 tests pass (`python -m pytest tests -q`): the discovery, the version comparison, the signature check, the staged install with its lock, '
                            'journal, backups and rollback, the evidence log and the eight-language tables.',
                   'ui': 'The Qt Quick shell has been run on Windows only.',
                   'security': 'The signature check and the evidence log are tested on the host; there has been no independent review.',
                   'updates': "The installs it makes need `git` and each repository's own build tools on the machine.",
                   'docs': 'Eight languages and the changelog are up to date.'},
        'honest': 'The manifest discovery, the version comparison, the signature check, the staged install and update with its lock, journal, backups and rollback, the '
                  'evidence log and the eight-language interface tables are tested (288 tests), and the Qt Quick shell has been run on Windows. It has not been run '
                  "against every repository of the family end to end, and the installs it makes need `git` and each repository's own build tools on the machine.",
        'bullets': ['**Discovery, no fixed list:** a local folder joins the moment it carries a valid `armor.project.json` declaring `ecosystem: "A.R.M.O.R."`; '
                    "remotely, every public repository of the account is checked the same way. A `GITHUB_TOKEN` is optional: it only raises GitHub's limit of 60 "
                    'requests an hour.',
                    '**Install and update, never in place:** a new project and an update are both built and verified in an independent staging clone first, and only '
                    'promoted - two journalled renames, the replaced checkout kept as a backup under `.armor-updater/backups/` (the newest three) - once that build '
                    'succeeds; an update to the commit already installed does nothing; a genuinely uncommitted local edit is refused outright, never silently discarded; '
                    'a crash between the renames is healed at the next run, and `rollback` puts the newest backup back.',
                    '**One at a time, and ordered:** a lock stops two updaters working on a workspace together; a batch goes ARMOR-COMMON first (every build needs it), '
                    'and a project is not built without it.',
                    '**Evidence:** every attempt, successful or not, appends one line to a local log with the project, the version and commit before and after, and the '
                    'reason for a failure.',
                    '**Requirements:** a manifest can list, in the optional `requires` field, the projects that must be installed first; a batch puts them first, and an '
                    'install or update is refused with a clear message, in the language of the window, when one of them is missing.',
                    '**Signatures, warn by default:** a revision without a valid signature is installed or updated all the same, and the window and the command line '
                    'state that it is not signed; choosing *require* in the settings (`"signature_policy": "require"`) refuses it instead.',
                    '**Previous copies:** the window can restore the previous copy of a project or delete the copies kept, and `status` shows how many there are and the '
                    'disk they take.',
                    '**A CLI and an optional desktop shell:** `armor-updater status`/`install`/`update`, and a Qt Quick interface (`pip install ".[gui]"`) in the '
                    "ecosystem's eight languages."],
        'note': 'See `docs/CLI_REFERENCE.md`.',
        'fit': 'ARMOR-UPDATER is the desktop tool for the person who keeps a copy of the family on a PC: it finds the A.R.M.O.R. repositories on the machine, compares '
               'them with GitHub and installs or updates one at a time, verifying before it replaces anything. It is separate from the updates that '
               '[ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) drives on the CM5 (those go through '
               "[ARMOR-DEVOPS](https://github.com/JuanenRac/ARMOR-DEVOPS)): this one is for a developer's machine.",
        'hardware': 'Not applicable: it is a desktop program; its Qt Quick shell has been run on Windows'},
 'es': {'tagline': 'Detecta, instala y actualiza cada repositorio de A.R.M.O.R. en la máquina donde se ejecuta (un programa en Python sin dependencias obligatorias)',
        'status': {'software': 'El descubrimiento de manifiestos, la comparación de versiones y la instalación y actualización por etapas funcionan; no se han ejecutado '
                               'de principio a fin contra todos los repositorios de la familia.',
                   'tests': 'Pasan 288 pruebas (`python -m pytest tests -q`): el descubrimiento, la comparación de versiones, la comprobación de la firma, la '
                            'instalación por etapas con su bloqueo, diario, copias y vuelta atrás, el registro de evidencias y las tablas de los ocho idiomas.',
                   'ui': 'La interfaz Qt Quick solo se ha ejecutado en Windows.',
                   'security': 'La comprobación de la firma y el registro de evidencias están probados en el host; no ha habido una revisión independiente.',
                   'updates': 'Las instalaciones que hace necesitan `git` y las herramientas de compilación propias de cada repositorio en la máquina.',
                   'docs': 'Ocho idiomas y el historial de cambios están al día.'},
        'honest': 'El descubrimiento por manifiesto, la comparación de versiones, la comprobación de firma, la instalación y actualización por etapas con su bloqueo, su '
                  'diario, sus copias y su vuelta atrás, el registro de evidencias y las tablas de la interfaz en ocho idiomas están probados (288 tests), y la interfaz '
                  'Qt Quick se ha ejecutado en Windows. No se ha ejecutado contra todos los repositorios de la familia de principio a fin, y las instalaciones que hace '
                  'necesitan `git` y las herramientas de compilación de cada repositorio en la máquina.',
        'bullets': ['**Descubrimiento, sin lista fija:** una carpeta local se une en cuanto lleva un `armor.project.json` válido que declara `ecosystem: "A.R.M.O.R."`; '
                    'en remoto, se revisa igual cada repositorio público de la cuenta. Un `GITHUB_TOKEN` es opcional: solo sube el límite de 60 peticiones a la hora de '
                    'GitHub.',
                    '**Instalar y actualizar, nunca en el sitio:** un proyecto nuevo y una actualización se construyen y verifican primero en un clon de ensayo '
                    'independiente, y solo se promueven -dos renombrados con diario, la copia reemplazada guardada en `.armor-updater/backups/` (las tres más '
                    'recientes)- cuando esa construcción tiene éxito; actualizar al commit ya instalado no hace nada; un cambio local de verdad sin commitear se rechaza '
                    'sin más, nunca se descarta en silencio; un fallo entre los renombrados se repara en la siguiente ejecución, y `rollback` devuelve la copia más '
                    'reciente.',
                    '**De uno en uno y en orden:** un bloqueo impide que dos actualizadores trabajen a la vez en un espacio de trabajo; un lote empieza por ARMOR-COMMON '
                    '(todas las construcciones lo necesitan) y no se construye un proyecto sin él.',
                    '**Evidencia:** cada intento, con éxito o no, añade una línea a un registro local con el proyecto, la versión y el commit antes y después, y el '
                    'motivo de un fallo.',
                    '**Requisitos:** un manifiesto puede listar, en el campo opcional `requires`, los proyectos que deben instalarse antes; un lote los pone primero, y '
                    'una instalación o actualización se rechaza con un mensaje claro, en el idioma de la ventana, si falta alguno.',
                    '**Firmas, avisar por defecto:** una revisión sin firma válida se instala o se actualiza igualmente, y la ventana y la línea de comandos indican que '
                    'no está firmada; elegir *exigir* en los ajustes (`"signature_policy": "require"`) la rechaza en su lugar.',
                    '**Copias anteriores:** la ventana puede restaurar la copia anterior de un proyecto o borrar las copias guardadas, y `status` muestra cuántas hay y '
                    'el disco que ocupan.',
                    '**Una CLI y una interfaz de escritorio opcional:** `armor-updater status`/`install`/`update`, y una interfaz Qt Quick (`pip install ".[gui]"`) en '
                    'los ocho idiomas del ecosistema.'],
        'note': 'Véase `docs/CLI_REFERENCE.md`.',
        'fit': 'ARMOR-UPDATER es la herramienta de escritorio para quien guarda una copia de la familia en un PC: encuentra los repositorios A.R.M.O.R. de la máquina, '
               'los compara con GitHub e instala o actualiza uno a uno, verificando antes de sustituir nada. Es distinta de las actualizaciones que '
               '[ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) gobierna en la CM5 (esas pasan por [ARMOR-DEVOPS](https://github.com/JuanenRac/ARMOR-DEVOPS)): '
               'esta es para la máquina de un desarrollador.',
        'hardware': 'No aplica: es un programa de escritorio; su interfaz Qt Quick se ha ejecutado en Windows',
        'requirements': ['Python 3.10+', '`git` y las herramientas de compilación de los repositorios que instales', 'opcional: PySide6 para la interfaz de escritorio']},
 'fr': {'tagline': 'Détecte, installe et met à jour chaque dépôt A.R.M.O.R. sur la machine où il tourne (un programme Python sans dépendance obligatoire)',
        'status': {'software': "La découverte des manifestes, la comparaison des versions et l'installation et mise à jour par étapes fonctionnent ; elles n'ont pas été "
                               'exécutées de bout en bout contre tous les dépôts de la famille.',
                   'tests': '288 tests réussissent (`python -m pytest tests -q`) : la découverte, la comparaison des versions, la vérification de la signature, '
                            "l'installation par étapes avec son verrou, son journal, ses sauvegardes et son retour arrière, le journal de preuves et les tables des huit "
                            'langues.',
                   'ui': "L'interface Qt Quick n'a été exécutée que sous Windows.",
                   'security': "La vérification de la signature et le journal de preuves sont testés sur l'hôte ; il n'y a pas eu de revue indépendante.",
                   'updates': "Les installations qu'il fait demandent `git` et les outils de compilation propres à chaque dépôt sur la machine.",
                   'docs': 'Huit langues et le journal des modifications sont à jour.'},
        'honest': "La découverte par manifeste, la comparaison des versions, la vérification de signature, l'installation et la mise à jour par étapes avec leur verrou, "
                  "leur journal, leurs sauvegardes et leur retour arrière, le journal de preuves et les tables de l'interface en huit langues sont testés (288 tests), "
                  "et l'interface Qt Quick a tourné sous Windows. Elle n'a pas été exécutée de bout en bout sur chaque dépôt de la famille, et les installations qu'elle "
                  'fait exigent `git` et les outils de compilation de chaque dépôt sur la machine.',
        'bullets': ["**Découverte, sans liste fixe :** un dossier local rejoint l'écosystème dès qu'il porte un `armor.project.json` valide déclarant `ecosystem: "
                    '"A.R.M.O.R."` ; à distance, chaque dépôt public du compte est examiné de la même façon. Un `GITHUB_TOKEN` est facultatif : il relève seulement la '
                    'limite de 60 requêtes par heure de GitHub.',
                    "**Installer et mettre à jour, jamais sur place :** un nouveau projet et une mise à jour sont d'abord construits et vérifiés dans un clone de "
                    'préparation indépendant, puis promus seulement - deux renommages journalisés, la copie remplacée gardée sous `.armor-updater/backups/` (les trois '
                    'plus récentes) - quand cette construction réussit ; une mise à jour vers le commit déjà installé ne fait rien ; une vraie modification locale non '
                    "validée est refusée net, jamais écartée en silence ; une panne entre les renommages est réparée à l'exécution suivante, et `rollback` remet la "
                    'copie la plus récente.',
                    "**Un à la fois, et dans l'ordre :** un verrou empêche deux outils de travailler ensemble sur un espace de travail ; un lot commence par "
                    "ARMOR-COMMON (toute construction en a besoin) et un projet n'est pas construit sans lui.",
                    '**Preuves :** chaque tentative, réussie ou non, ajoute une ligne à un journal local avec le projet, la version et le commit avant et après, et la '
                    "raison d'un échec.",
                    "**Prérequis :** un manifeste peut lister, dans le champ facultatif `requires`, les projets à installer d'abord ; un lot les place en premier, et "
                    "une installation ou une mise à jour est refusée avec un message clair, dans la langue de la fenêtre, si l'un d'eux manque.",
                    '**Signatures, avertir par défaut :** une révision sans signature valide est tout de même installée ou mise à jour, et la fenêtre comme la ligne de '
                    'commande indiquent qu\'elle n\'est pas signée ; choisir *exiger* dans les réglages (`"signature_policy": "require"`) la refuse à la place.',
                    "**Copies précédentes :** la fenêtre peut restaurer la copie précédente d'un projet ou supprimer les copies conservées, et `status` indique combien "
                    "il y en a et l'espace disque qu'elles occupent.",
                    '**Une CLI et une interface de bureau optionnelle :** `armor-updater status`/`install`/`update`, et une interface Qt Quick (`pip install ".[gui]"`) '
                    "dans les huit langues de l'écosystème."],
        'note': 'Voir `docs/CLI_REFERENCE.md`.',
        'fit': "ARMOR-UPDATER est l'outil de bureau pour qui garde une copie de la famille sur un PC : il trouve les dépôts A.R.M.O.R. de la machine, les compare à "
               'GitHub et installe ou met à jour un par un, en vérifiant avant de remplacer quoi que ce soit. Il est distinct des mises à jour '
               "qu'[ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) pilote sur le CM5 (celles-ci passent par "
               "[ARMOR-DEVOPS](https://github.com/JuanenRac/ARMOR-DEVOPS)) : celui-ci est pour la machine d'un développeur.",
        'hardware': "Sans objet : c'est un programme de bureau ; son interface Qt Quick a été exécutée sous Windows",
        'requirements': ['Python 3.10+', '`git` et les outils de compilation des dépôts que vous installez', "facultatif : PySide6 pour l'interface de bureau"]},
 'it': {'tagline': 'Rileva, installa e aggiorna ogni repository A.R.M.O.R. sulla macchina in cui gira (un programma Python senza dipendenze obbligatorie)',
        'status': {'software': "La scoperta dei manifesti, il confronto delle versioni e l'installazione e aggiornamento a fasi funzionano; non sono stati eseguiti end "
                               'to end contro tutti i repository della famiglia.',
                   'tests': "Superano 288 test (`python -m pytest tests -q`): la scoperta, il confronto delle versioni, il controllo della firma, l'installazione a fasi "
                            'con blocco, diario, copie e ripristino, il registro delle prove e le tabelle delle otto lingue.',
                   'ui': "L'interfaccia Qt Quick è stata eseguita solo su Windows.",
                   'security': "Il controllo della firma e il registro delle prove sono testati sull'host; non c'è stata una revisione indipendente.",
                   'updates': 'Le installazioni che esegue richiedono `git` e gli strumenti di compilazione propri di ciascun repository sulla macchina.',
                   'docs': 'Otto lingue e il registro delle modifiche sono aggiornati.'},
        'honest': "La scoperta per manifesto, il confronto delle versioni, il controllo della firma, l'installazione e l'aggiornamento a tappe con il loro blocco, il "
                  "loro diario, le copie e il ritorno indietro, il registro delle prove e le tabelle dell'interfaccia in otto lingue sono testati (288 test), e "
                  "l'interfaccia Qt Quick è stata eseguita su Windows. Non è stata eseguita su ogni repository della famiglia da cima a fondo, e le installazioni che fa "
                  'richiedono `git` e gli strumenti di compilazione di ciascun repository sulla macchina.',
        'bullets': ['**Scoperta, senza elenco fisso:** una cartella locale entra appena porta un `armor.project.json` valido che dichiara `ecosystem: "A.R.M.O.R."`; da '
                    "remoto, ogni repository pubblico dell'account è controllato allo stesso modo. Un `GITHUB_TOKEN` è facoltativo: alza solo il limite di 60 richieste "
                    "l'ora di GitHub.",
                    '**Installare e aggiornare, mai sul posto:** un nuovo progetto e un aggiornamento sono prima costruiti e verificati in un clone di prova '
                    'indipendente, e promossi solo - due rinominazioni registrate, la copia sostituita conservata in `.armor-updater/backups/` (le tre più recenti) - '
                    'quando quella costruzione riesce; un aggiornamento al commit già installato non fa nulla; una vera modifica locale non salvata è rifiutata senza '
                    'mezzi termini, mai scartata in silenzio; un guasto tra le rinominazioni viene riparato alla prossima esecuzione, e `rollback` rimette la copia più '
                    'recente.',
                    '**Uno alla volta, e in ordine:** un blocco impedisce a due aggiornatori di lavorare insieme su uno spazio di lavoro; un lotto parte da ARMOR-COMMON '
                    '(ogni costruzione ne ha bisogno) e un progetto non viene costruito senza di esso.',
                    '**Prove:** ogni tentativo, riuscito o no, aggiunge una riga a un registro locale con il progetto, la versione e il commit prima e dopo, e il motivo '
                    'di un fallimento.',
                    '**Requisiti:** un manifest può elencare, nel campo facoltativo `requires`, i progetti che devono essere installati prima; un blocco li mette per '
                    "primi, e un'installazione o un aggiornamento viene rifiutato con un messaggio chiaro, nella lingua della finestra, se ne manca uno.",
                    '**Firme, avvisa per impostazione predefinita:** una revisione senza firma valida viene comunque installata o aggiornata, e la finestra e la riga di '
                    'comando indicano che non è firmata; scegliere *richiedi* nelle impostazioni (`"signature_policy": "require"`) la rifiuta invece.',
                    '**Copie precedenti:** la finestra può ripristinare la copia precedente di un progetto o eliminare le copie conservate, e `status` mostra quante ce '
                    'ne sono e lo spazio su disco che occupano.',
                    '**Una CLI e un\'interfaccia desktop opzionale:** `armor-updater status`/`install`/`update`, e un\'interfaccia Qt Quick (`pip install ".[gui]"`) '
                    "nelle otto lingue dell'ecosistema."],
        'note': 'Vedi `docs/CLI_REFERENCE.md`.',
        'fit': 'ARMOR-UPDATER è lo strumento da scrivania per chi tiene una copia della famiglia su un PC: trova i repository A.R.M.O.R. della macchina, li confronta '
               'con GitHub e installa o aggiorna uno alla volta, verificando prima di sostituire qualcosa. È distinto dagli aggiornamenti che '
               '[ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) guida sulla CM5 (quelli passano per '
               '[ARMOR-DEVOPS](https://github.com/JuanenRac/ARMOR-DEVOPS)): questo è per la macchina di uno sviluppatore.',
        'hardware': 'Non applicabile: è un programma da scrivania; la sua interfaccia Qt Quick è stata eseguita su Windows',
        'requirements': ['Python 3.10+', '`git` e gli strumenti di compilazione dei repository che installi', "facoltativo: PySide6 per l'interfaccia desktop"]},
 'de': {'tagline': 'Erkennt, installiert und aktualisiert jedes A.R.M.O.R.-Repository auf dem Rechner, auf dem es läuft (ein Python-Programm ohne Pflichtabhängigkeiten)',
        'status': {'software': 'Die Manifest-Erkennung, der Versionsvergleich und die gestufte Installation und Aktualisierung funktionieren; sie wurden nicht '
                               'durchgängig gegen jedes Repository der Familie ausgeführt.',
                   'tests': '288 Tests bestehen (`python -m pytest tests -q`): die Erkennung, der Versionsvergleich, die Signaturprüfung, die gestufte Installation mit '
                            'Sperre, Journal, Sicherungen und Rückfall, das Beweisprotokoll und die Tabellen der acht Sprachen.',
                   'ui': 'Die Qt-Quick-Oberfläche lief nur unter Windows.',
                   'security': 'Die Signaturprüfung und das Beweisprotokoll sind auf dem Host getestet; es gab keine unabhängige Prüfung.',
                   'updates': 'Die Installationen, die er vornimmt, brauchen `git` und die eigenen Build-Werkzeuge jedes Repositorys auf dem Rechner.',
                   'docs': 'Acht Sprachen und das Änderungsprotokoll sind aktuell.'},
        'honest': 'Die Manifest-Erkennung, der Versionsvergleich, die Signaturprüfung, die gestufte Installation und Aktualisierung mit Sperre, Journal, Sicherungen und '
                  'Rückkehr, das Nachweisprotokoll und die Oberflächentabellen in acht Sprachen sind getestet (288 Tests), und die Qt-Quick-Oberfläche lief unter '
                  'Windows. Sie wurde nicht gegen jedes Repository der Familie von Anfang bis Ende ausgeführt, und die Installationen brauchen `git` und die '
                  'Build-Werkzeuge jedes Repositorys auf dem Rechner.',
        'bullets': ['**Erkennung ohne feste Liste:** Ein lokaler Ordner gehört dazu, sobald er ein gültiges `armor.project.json` mit `ecosystem: "A.R.M.O.R."` trägt; '
                    'entfernt wird jedes öffentliche Repository des Kontos genauso geprüft. Ein `GITHUB_TOKEN` ist optional: Er hebt nur GitHubs Grenze von 60 Anfragen '
                    'pro Stunde an.',
                    '**Installieren und aktualisieren, nie an Ort und Stelle:** Ein neues Projekt und eine Aktualisierung werden zuerst in einem unabhängigen '
                    'Staging-Klon gebaut und geprüft und erst danach übernommen - zwei protokollierte Umbenennungen, die ersetzte Kopie unter `.armor-updater/backups/` '
                    'aufbewahrt (die drei neuesten) -, wenn der Build gelingt; eine Aktualisierung auf den schon installierten Commit tut nichts; eine echte nicht '
                    'eingecheckte lokale Änderung wird glatt abgelehnt, nie stillschweigend verworfen; ein Absturz zwischen den Umbenennungen wird beim nächsten Lauf '
                    'geheilt, und `rollback` stellt die neueste Kopie wieder her.',
                    '**Eines nach dem anderen, und der Reihe nach:** Eine Sperre verhindert, dass zwei Updater gleichzeitig an einem Arbeitsbereich arbeiten; ein Stapel '
                    'beginnt mit ARMOR-COMMON (jeder Build braucht es), und ein Projekt wird ohne es nicht gebaut.',
                    '**Nachweis:** jeder Versuch, erfolgreich oder nicht, fügt einer lokalen Protokolldatei eine Zeile mit Projekt, Version und Commit davor und danach '
                    'sowie dem Grund eines Fehlschlags hinzu.',
                    '**Voraussetzungen:** Ein Manifest kann im optionalen Feld `requires` die Projekte nennen, die zuerst installiert sein müssen; eine Sammelaktion '
                    'stellt sie voran, und eine Installation oder Aktualisierung wird mit einer klaren Meldung in der Sprache des Fensters abgelehnt, wenn eines davon '
                    'fehlt.',
                    '**Signaturen, standardmäßig warnen:** Eine Revision ohne gültige Signatur wird trotzdem installiert oder aktualisiert, und das Fenster wie die '
                    'Befehlszeile weisen darauf hin, dass sie nicht signiert ist; wer in den Einstellungen *verlangen* wählt (`"signature_policy": "require"`), lehnt '
                    'sie stattdessen ab.',
                    '**Frühere Kopien:** Das Fenster kann die frühere Kopie eines Projekts wiederherstellen oder die aufbewahrten Kopien löschen, und `status` zeigt, '
                    'wie viele es sind und wie viel Speicherplatz sie belegen.',
                    '**Eine CLI und eine optionale Desktop-Oberfläche:** `armor-updater status`/`install`/`update`, sowie eine Qt-Quick-Oberfläche (`pip install '
                    '".[gui]"`) in den acht Sprachen des Ökosystems.'],
        'note': 'Siehe `docs/CLI_REFERENCE.md`.',
        'fit': 'ARMOR-UPDATER ist das Desktop-Werkzeug für alle, die eine Kopie der Familie auf einem PC halten: Es findet die A.R.M.O.R.-Repositorys der Maschine, '
               'vergleicht sie mit GitHub und installiert oder aktualisiert eines nach dem anderen und prüft, bevor es etwas ersetzt. Es ist getrennt von den Updates, '
               'die [ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) auf dem CM5 steuert (die laufen über '
               '[ARMOR-DEVOPS](https://github.com/JuanenRac/ARMOR-DEVOPS)): dieses ist für die Maschine eines Entwicklers.',
        'hardware': 'Nicht zutreffend: es ist ein Desktop-Programm; seine Qt-Quick-Oberfläche wurde unter Windows ausgeführt',
        'requirements': ['Python 3.10+', '`git` und die Build-Werkzeuge der Repositories, die Sie installieren', 'optional: PySide6 für die Desktop-Oberfläche']},
 'zh': {'tagline': '检测、安装并更新所在机器上的每个 A.R.M.O.R. 仓库（一个没有必需依赖的 Python 程序）',
        'status': {'software': '清单发现、版本比较以及分阶段安装与更新都能工作；尚未对家族中的每个仓库完整运行过。',
                   'tests': '288 项测试通过（`python -m pytest tests -q`）：发现、版本比较、签名检查、带锁、日志、备份和回滚的分阶段安装、证据日志以及八种语言的表。',
                   'ui': 'Qt Quick 界面只在 Windows 上运行过。',
                   'security': '签名检查和证据日志已在主机上测试；没有经过独立审查。',
                   'updates': '它所做的安装需要机器上有 `git` 以及每个仓库自己的构建工具。',
                   'docs': '八种语言和更新日志均为最新。'},
        'honest': '清单发现、版本比较、签名检查、带锁、日志、备份和回退的分阶段安装与更新、证据日志以及八种语言的界面表格都已测试（288 个测试），Qt Quick 界面已在 Windows 上运行过。它没有对家族中的每个仓库从头到尾运行过，它所做的安装需要机器上有 `git` 和各仓库自己的构建工具。',
        'bullets': ['**无固定列表的发现：**本地文件夹只要带有声明 `ecosystem: "A.R.M.O.R."` 的有效 `armor.project.json` 就会加入；远程则以同样方式检查账户的每个公开仓库。`GITHUB_TOKEN` 是可选的：它只是提高 GitHub 每小时 60 '
                    '次请求的限制。',
                    '**安装和更新，从不原地进行：**新项目和更新都先在独立的暂存克隆中构建并验证，构建成功后才升级——两次有日志的重命名，被替换的检出保存在 '
                    '`.armor-updater/backups/`（最近三份）；更新到已安装的提交不会做任何事；真正未提交的本地修改会被直接拒绝，绝不会被悄悄丢弃；两次重命名之间的崩溃会在下次运行时修复，`rollback` 会放回最近的备份。',
                    '**一次一个，并有顺序：**锁可防止两个更新器同时处理一个工作区；批量操作先处理 ARMOR-COMMON（每个构建都需要它），没有它就不会构建项目。',
                    '**证据:** 每一次尝试,无论成功与否,都会在本地日志里追加一行,记录项目、前后的版本与提交,以及失败的原因。',
                    '**前置要求：**清单可以在可选字段 `requires` 中列出必须先安装的项目；批量操作会把它们排在前面，若其中任何一个缺失，安装或更新会被拒绝，并以窗口所用的语言给出清晰的提示。',
                    '**签名，默认为警告：**没有有效签名的修订仍会被安装或更新，窗口和命令行都会明确指出它没有签名；在设置中选择*要求*（`"signature_policy": "require"`）则会改为拒绝它。',
                    '**先前副本：**窗口可以恢复项目的先前副本，或删除保留的副本，`status` 会显示副本数量及其占用的磁盘空间。',
                    '**一个命令行工具和一个可选的桌面界面:** `armor-updater status`/`install`/`update`,以及一个 Qt Quick 界面(`pip install ".[gui]"`),覆盖生态系统的八种语言。'],
        'note': '参见 `docs/CLI_REFERENCE.md`。',
        'fit': 'ARMOR-UPDATER 是为在 PC 上保存家族副本的人准备的桌面工具：它找出机器上的 A.R.M.O.R. 仓库，与 GitHub 对比，并逐个安装或更新，替换任何东西之前都先验证。它与 '
               '[ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) 在 CM5 上驱动的更新不同（那些经过 [ARMOR-DEVOPS](https://github.com/JuanenRac/ARMOR-DEVOPS)）：这个是给开发者的机器用的。',
        'hardware': '不适用：这是桌面程序；其 Qt Quick 界面已在 Windows 上运行过',
        'requirements': ['Python 3.10+', '`git` 以及你所安装仓库的构建工具', '可选：用于桌面界面的 PySide6']},
 'ja': {'tagline': '実行中のマシン上のすべての A.R.M.O.R. リポジトリを検出し、インストールし、更新します（必須の依存関係がない Python プログラム）',
        'status': {'software': 'マニフェストの検出、バージョン比較、段階的なインストールと更新は動作します。ファミリーのすべてのリポジトリに対して端から端まで実行したわけではありません。',
                   'tests': '288 件のテストが通ります（`python -m pytest tests -q`）：検出、バージョン比較、署名の確認、ロック・ジャーナル・バックアップ・ロールバック付きの段階的インストール、証拠ログ、8 言語の表。',
                   'ui': 'Qt Quick のシェルは Windows でのみ実行しています。',
                   'security': '署名の確認と証拠ログはホストでテスト済みです。独立したレビューはありません。',
                   'updates': '実行するインストールには、マシンに `git` と各リポジトリ固有のビルドツールが必要です。',
                   'docs': '8 言語と変更履歴は最新です。'},
        'honest': 'マニフェストによる検出、バージョン比較、署名の確認、ロック・ジャーナル・バックアップ・ロールバックを備えた段階的なインストールと更新、証跡ログ、8 言語のインターフェース表はテスト済みです（288 件のテスト）。Qt Quick のシェルは Windows '
                  'で実行されました。ファミリーのすべてのリポジトリに対して端から端まで実行したわけではなく、行うインストールにはマシンに `git` と各リポジトリ自身のビルドツールが必要です。',
        'bullets': ['**固定リストのない検出：**ローカルのフォルダーは、`ecosystem: "A.R.M.O.R."` を宣言する有効な `armor.project.json` を持った時点で加わります。リモートでは、アカウントのすべての公開リポジトリが同じ方法で調べられます。`GITHUB_TOKEN` '
                    'は任意で、GitHub の 1 時間 60 リクエストの上限を上げるだけです。',
                    '**インストールも更新も、その場では行いません：**新しいプロジェクトも更新も、まず独立したステージングのクローンでビルドして検証し、ビルドが成功してから反映します。ジャーナルに記録された 2 回の名前変更を行い、置き換えたチェックアウトは `.armor-updater/backups/` '
                    'に（最新の 3 件）保存されます。インストール済みと同じコミットへの更新は何もしません。コミットされていない実際のローカル変更は即座に拒否され、黙って破棄されることはありません。名前変更の間のクラッシュは次の実行で修復され、`rollback` は最新のバックアップを戻します。',
                    '**一度に一つ、順番どおりに：**ロックにより、2 つの更新ツールが同じワークスペースで同時に動くことはありません。一括処理は ARMOR-COMMON から始まり（すべてのビルドが必要とします）、それがなければプロジェクトはビルドされません。',
                    '**証跡:** 成功・失敗を問わず、すべての試行はプロジェクト名、前後のバージョンとコミット、失敗の理由をローカルのログに一行追加する。',
                    '**前提条件：**マニフェストは任意のフィールド `requires` に、先にインストールしておくべきプロジェクトを列挙できます。一括処理ではそれらが先頭に置かれ、いずれかが欠けている場合、インストールや更新は、ウィンドウの言語で分かりやすいメッセージとともに拒否されます。',
                    '**署名、既定は警告：**有効な署名のないリビジョンも、そのままインストールまたは更新され、ウィンドウとコマンドラインは署名されていないことを明示します。設定で*必須*（`"signature_policy": "require"`）を選ぶと、代わりに拒否されます。',
                    '**以前のコピー：**ウィンドウからプロジェクトの以前のコピーを復元したり、保管されているコピーを削除したりでき、`status` はコピーの数とそれが使うディスク容量を表示します。',
                    '**CLI と任意のデスクトップシェル:** `armor-updater status`/`install`/`update`、およびエコシステムの 8 言語に対応した Qt Quick インターフェース(`pip install ".[gui]"`)。'],
        'note': '`docs/CLI_REFERENCE.md` を参照してください。',
        'fit': 'ARMOR-UPDATER は、PC にファミリーのコピーを持つ人のためのデスクトップツールです。マシン上の A.R.M.O.R. リポジトリを見つけ、GitHub と比較し、何かを置き換える前に検証しながら 1 '
               'つずつインストール・更新します。[ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) が CM5 上で行う更新（[ARMOR-DEVOPS](https://github.com/JuanenRac/ARMOR-DEVOPS) '
               'を通るもの）とは別で、これは開発者のマシン用です。',
        'hardware': '該当なし：デスクトッププログラムで、Qt Quick シェルは Windows で動かしました',
        'requirements': ['Python 3.10+', '`git` と、インストールするリポジトリのビルドツール', '任意：デスクトップシェル用の PySide6']},
 'pt': {'tagline': 'Deteta, instala e atualiza cada repositório A.R.M.O.R. na máquina onde corre (um programa em Python sem dependências obrigatórias)',
        'status': {'software': 'A descoberta de manifestos, a comparação de versões e a instalação e atualização por fases funcionam; não foram executadas de ponta a '
                               'ponta contra todos os repositórios da família.',
                   'tests': 'Passam 288 testes (`python -m pytest tests -q`): a descoberta, a comparação de versões, a verificação da assinatura, a instalação por fases '
                            'com o seu bloqueio, diário, cópias e retrocesso, o registo de provas e as tabelas dos oito idiomas.',
                   'ui': 'A interface Qt Quick só foi executada em Windows.',
                   'security': 'A verificação da assinatura e o registo de provas estão testados no anfitrião; não houve revisão independente.',
                   'updates': 'As instalações que faz precisam de `git` e das ferramentas de compilação próprias de cada repositório na máquina.',
                   'docs': 'Oito idiomas e o registo de alterações estão atualizados.'},
        'honest': 'A descoberta por manifesto, a comparação de versões, a verificação de assinatura, a instalação e a atualização por etapas com o seu bloqueio, diário, '
                  'cópias e volta atrás, o registo de evidências e as tabelas da interface em oito idiomas estão testados (288 testes), e a interface Qt Quick correu no '
                  'Windows. Não foi executada contra todos os repositórios da família de ponta a ponta, e as instalações que faz precisam de `git` e das ferramentas de '
                  'compilação de cada repositório na máquina.',
        'bullets': ['**Descoberta, sem lista fixa:** uma pasta local junta-se assim que tem um `armor.project.json` válido que declara `ecosystem: "A.R.M.O.R."`; em '
                    'remoto, cada repositório público da conta é verificado da mesma forma. Um `GITHUB_TOKEN` é opcional: só sobe o limite de 60 pedidos por hora do '
                    'GitHub.',
                    '**Instalar e atualizar, nunca no próprio sítio:** um projeto novo e uma atualização são primeiro construídos e verificados num clone de ensaio '
                    'independente, e só depois promovidos - dois renomeamentos com diário, a cópia substituída guardada em `.armor-updater/backups/` (as três mais '
                    'recentes) - quando essa construção tem êxito; atualizar para o commit já instalado não faz nada; uma alteração local a sério por commitar é '
                    'recusada de vez, nunca descartada em silêncio; uma falha entre os renomeamentos é reparada na execução seguinte, e `rollback` repõe a cópia mais '
                    'recente.',
                    '**Um de cada vez, e por ordem:** um bloqueio impede que dois atualizadores trabalhem juntos num espaço de trabalho; um lote começa por ARMOR-COMMON '
                    '(todas as construções precisam dele) e um projeto não é construído sem ele.',
                    '**Provas:** cada tentativa, bem-sucedida ou não, acrescenta uma linha a um registo local com o projeto, a versão e o commit antes e depois, e o '
                    'motivo de uma falha.',
                    '**Requisitos:** um manifesto pode listar, no campo opcional `requires`, os projetos que têm de estar instalados primeiro; um lote coloca-os à '
                    'frente, e uma instalação ou atualização é recusada com uma mensagem clara, na língua da janela, se algum deles faltar.',
                    '**Assinaturas, avisar por omissão:** uma revisão sem assinatura válida é instalada ou atualizada na mesma, e a janela e a linha de comandos indicam '
                    'que não está assinada; escolher *exigir* nas definições (`"signature_policy": "require"`) recusa-a em vez disso.',
                    '**Cópias anteriores:** a janela pode restaurar a cópia anterior de um projeto ou apagar as cópias guardadas, e o `status` mostra quantas existem e '
                    'o disco que ocupam.',
                    '**Uma CLI e uma consola de ambiente de trabalho opcional:** `armor-updater status`/`install`/`update`, e uma interface Qt Quick (`pip install '
                    '".[gui]"`) nos oito idiomas do ecossistema.'],
        'note': 'Veja `docs/CLI_REFERENCE.md`.',
        'fit': 'O ARMOR-UPDATER é a ferramenta de ambiente de trabalho para quem guarda uma cópia da família num PC: encontra os repositórios A.R.M.O.R. da máquina, '
               'compara-os com o GitHub e instala ou atualiza um a um, verificando antes de substituir seja o que for. É distinto das atualizações que o '
               '[ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) comanda no CM5 (essas passam pelo [ARMOR-DEVOPS](https://github.com/JuanenRac/ARMOR-DEVOPS)): '
               'este é para a máquina de um programador.',
        'hardware': 'Não se aplica: é um programa de ambiente de trabalho; a sua interface Qt Quick foi executada no Windows',
        'requirements': ['Python 3.10+',
                         '`git` e as ferramentas de compilação dos repositórios que instalar',
                         'opcional: PySide6 para a interface de ambiente de trabalho']}}

# the text tree of docs/structure.json (make_structure.py --tree <language>); the repository's own check fails when it and the file disagree
TREE = {'en': 'ARMOR-UPDATER/\n'
       '├── src/armor_updater/\n'
       '│   ├── project_manifest.py registry.py ecosystem_catalog.py   the manifest, the list, the catalogue\n'
       '│   ├── detect.py github_client.py version_parse.py            local and remote discovery, versions\n'
       '│   ├── install.py git_ops.py staging.py                       staged install and update\n'
       '│   ├── promotion.py releases.py deploy_category.py            lock, journal, backups, layouts\n'
       '│   ├── signature.py                                           signed updates, pinned keys\n'
       '│   ├── evidence.py settings.py console_flags.py               the log, the settings, the flags\n'
       '│   ├── main.py                                                the command line\n'
       '│   ├── i18n.py i18n_pt.py i18n_recovery.py result_text.py     the eight languages\n'
       '│   ├── gui.py qt_gui.py qml/                                  the optional Qt Quick window\n'
       '│   └── data/ assets/                                          allowed_signers; the icon\n'
       '├── tests/                                                     288 tests in 25 modules\n'
       '├── docs/                                                      CLI_REFERENCE.md, QML_DESKTOP_GUI.md\n'
       '├── tools/                                                     the shared CI checks, the launcher and generate_app_icon.py\n'
       '├── images/                                                    banner, icon and the pictures of the README\n'
       '├── .github/                                                   CI workflow, dashboard notice, issue and pull-request templates\n'
       '├── armor.project.json                                         manifest: version, role, maturity\n'
       '├── pyproject.toml                                             package metadata, entry points\n'
       '├── CHANGELOG.md                                               what changed in each version\n'
       '├── run-gui.vbs                                                opens the window on Windows without a console\n'
       '├── run.sh run.bat                                             start, shared workflow\n'
       '├── build.sh build.bat                                         build and test, shared workflow\n'
       '├── build-test.sh build-test.bat                               build, test and package\n'
       '├── test.sh test.bat                                           only the tests, never the version\n'
       '└── SECURITY.md SUPPORT.md CONTRIBUTING.md CODE_OF_CONDUCT.md LICENSE',
 'es': 'ARMOR-UPDATER/\n'
       '├── src/armor_updater/\n'
       '│   ├── project_manifest.py registry.py ecosystem_catalog.py   el manifiesto, la lista, el catálogo\n'
       '│   ├── detect.py github_client.py version_parse.py            descubrimiento local y remoto, versiones\n'
       '│   ├── install.py git_ops.py staging.py                       instalación y actualización por etapas\n'
       '│   ├── promotion.py releases.py deploy_category.py            bloqueo, diario, copias, disposiciones\n'
       '│   ├── signature.py                                           actualizaciones firmadas, claves fijadas\n'
       '│   ├── evidence.py settings.py console_flags.py               el registro, los ajustes, las opciones\n'
       '│   ├── main.py                                                la línea de órdenes\n'
       '│   ├── i18n.py i18n_pt.py i18n_recovery.py result_text.py     los ocho idiomas\n'
       '│   ├── gui.py qt_gui.py qml/                                  la ventana Qt Quick opcional\n'
       '│   └── data/ assets/                                          allowed_signers; el icono\n'
       '├── tests/                                                     288 pruebas en 25 módulos\n'
       '├── docs/                                                      CLI_REFERENCE.md, QML_DESKTOP_GUI.md\n'
       '├── tools/                                                     las comprobaciones de CI, el lanzador y generate_app_icon.py\n'
       '├── images/                                                    banner, icono y las imágenes del README\n'
       '├── .github/                                                   flujo de CI, aviso al panel, plantillas de incidencias y pull requests\n'
       '├── armor.project.json                                         manifiesto: versión, función, madurez\n'
       '├── pyproject.toml                                             metadatos del paquete, entradas\n'
       '├── CHANGELOG.md                                               qué cambió en cada versión\n'
       '├── run-gui.vbs                                                abre la ventana en Windows sin consola\n'
       '├── run.sh run.bat                                             arrancar, flujo compartido\n'
       '├── build.sh build.bat                                         construir y probar, flujo compartido\n'
       '├── build-test.sh build-test.bat                               construir, probar y empaquetar\n'
       '├── test.sh test.bat                                           solo las pruebas, nunca la versión\n'
       '└── SECURITY.md SUPPORT.md CONTRIBUTING.md CODE_OF_CONDUCT.md LICENSE',
 'de': 'ARMOR-UPDATER/\n'
       '├── src/armor_updater/\n'
       '│   ├── project_manifest.py registry.py ecosystem_catalog.py   das Manifest, die Liste, der Katalog\n'
       '│   ├── detect.py github_client.py version_parse.py            lokale und entfernte Suche, Versionen\n'
       '│   ├── install.py git_ops.py staging.py                       gestufte Installation und Aktualisierung\n'
       '│   ├── promotion.py releases.py deploy_category.py            Sperre, Journal, Sicherungen, Layouts\n'
       '│   ├── signature.py                                           signierte Updates, fixierte Schlüssel\n'
       '│   ├── evidence.py settings.py console_flags.py               das Protokoll, die Einstellungen, die Optionen\n'
       '│   ├── main.py                                                die Kommandozeile\n'
       '│   ├── i18n.py i18n_pt.py i18n_recovery.py result_text.py     die acht Sprachen\n'
       '│   ├── gui.py qt_gui.py qml/                                  das optionale Qt-Quick-Fenster\n'
       '│   └── data/ assets/                                          allowed_signers; das Symbol\n'
       '├── tests/                                                     288 Tests in 25 Modulen\n'
       '├── docs/                                                      CLI_REFERENCE.md, QML_DESKTOP_GUI.md\n'
       '├── tools/                                                     die gemeinsamen CI-Prüfungen, der Starter und generate_app_icon.py\n'
       '├── images/                                                    Banner, Symbol und die Bilder des READMEs\n'
       '├── .github/                                                   CI-Workflow, Dashboard-Hinweis, Vorlagen für Issues und Pull Requests\n'
       '├── armor.project.json                                         Manifest: Version, Rolle, Reife\n'
       '├── pyproject.toml                                             Paket-Metadaten, Einstiege\n'
       '├── CHANGELOG.md                                               was sich in jeder Version geändert hat\n'
       '├── run-gui.vbs                                                öffnet das Fenster unter Windows ohne Konsole\n'
       '├── run.sh run.bat                                             Start, gemeinsamer Ablauf\n'
       '├── build.sh build.bat                                         Bauen und Testen, gemeinsamer Ablauf\n'
       '├── build-test.sh build-test.bat                               Bauen, Testen und Verpacken\n'
       '├── test.sh test.bat                                           nur die Tests, nie die Version\n'
       '└── SECURITY.md SUPPORT.md CONTRIBUTING.md CODE_OF_CONDUCT.md LICENSE',
 'fr': 'ARMOR-UPDATER/\n'
       '├── src/armor_updater/\n'
       '│   ├── project_manifest.py registry.py ecosystem_catalog.py   le manifeste, la liste, le catalogue\n'
       '│   ├── detect.py github_client.py version_parse.py            découverte locale et distante, versions\n'
       '│   ├── install.py git_ops.py staging.py                       installation et mise à jour par étapes\n'
       '│   ├── promotion.py releases.py deploy_category.py            verrou, journal, copies, dispositions\n'
       '│   ├── signature.py                                           mises à jour signées, clés épinglées\n'
       '│   ├── evidence.py settings.py console_flags.py               le journal, les réglages, les options\n'
       '│   ├── main.py                                                la ligne de commande\n'
       '│   ├── i18n.py i18n_pt.py i18n_recovery.py result_text.py     les huit langues\n'
       '│   ├── gui.py qt_gui.py qml/                                  la fenêtre Qt Quick facultative\n'
       "│   └── data/ assets/                                          allowed_signers ; l'icône\n"
       '├── tests/                                                     288 tests en 25 modules\n'
       '├── docs/                                                      CLI_REFERENCE.md, QML_DESKTOP_GUI.md\n'
       '├── tools/                                                     les vérifications CI, le lanceur et generate_app_icon.py\n'
       '├── images/                                                    bannière, icône et images du README\n'
       "├── .github/                                                   workflow CI, avis au tableau de bord, modèles d'issues et de pull requests\n"
       '├── armor.project.json                                         manifeste : version, rôle, maturité\n'
       '├── pyproject.toml                                             métadonnées du paquet, entrées\n'
       '├── CHANGELOG.md                                               ce qui a changé à chaque version\n'
       '├── run-gui.vbs                                                ouvre la fenêtre sous Windows sans console\n'
       '├── run.sh run.bat                                             démarrer, flux partagé\n'
       '├── build.sh build.bat                                         construire et tester, flux partagé\n'
       '├── build-test.sh build-test.bat                               construire, tester, empaqueter\n'
       '├── test.sh test.bat                                           seulement les tests, jamais la version\n'
       '└── SECURITY.md SUPPORT.md CONTRIBUTING.md CODE_OF_CONDUCT.md LICENSE',
 'it': 'ARMOR-UPDATER/\n'
       '├── src/armor_updater/\n'
       "│   ├── project_manifest.py registry.py ecosystem_catalog.py   il manifesto, l'elenco, il catalogo\n"
       '│   ├── detect.py github_client.py version_parse.py            scoperta locale e remota, versioni\n'
       '│   ├── install.py git_ops.py staging.py                       installazione e aggiornamento a fasi\n'
       '│   ├── promotion.py releases.py deploy_category.py            blocco, diario, copie, disposizioni\n'
       '│   ├── signature.py                                           aggiornamenti firmati, chiavi fissate\n'
       '│   ├── evidence.py settings.py console_flags.py               il registro, le impostazioni, le opzioni\n'
       '│   ├── main.py                                                la riga di comando\n'
       '│   ├── i18n.py i18n_pt.py i18n_recovery.py result_text.py     le otto lingue\n'
       '│   ├── gui.py qt_gui.py qml/                                  la finestra Qt Quick opzionale\n'
       "│   └── data/ assets/                                          allowed_signers; l'icona\n"
       '├── tests/                                                     288 test in 25 moduli\n'
       '├── docs/                                                      CLI_REFERENCE.md, QML_DESKTOP_GUI.md\n'
       "├── tools/                                                     i controlli CI, l'avviatore e generate_app_icon.py\n"
       '├── images/                                                    banner, icona e immagini del README\n'
       '├── .github/                                                   workflow CI, avviso alla dashboard, modelli per issue e pull request\n'
       '├── armor.project.json                                         manifesto: versione, ruolo, maturità\n'
       '├── pyproject.toml                                             metadati del pacchetto, ingressi\n'
       '├── CHANGELOG.md                                               cosa è cambiato in ogni versione\n'
       '├── run-gui.vbs                                                apre la finestra su Windows senza console\n'
       '├── run.sh run.bat                                             avvio, flusso condiviso\n'
       '├── build.sh build.bat                                         compila e prova, flusso condiviso\n'
       '├── build-test.sh build-test.bat                               compila, prova e impacchetta\n'
       '├── test.sh test.bat                                           solo i test, mai la versione\n'
       '└── SECURITY.md SUPPORT.md CONTRIBUTING.md CODE_OF_CONDUCT.md LICENSE',
 'ja': 'ARMOR-UPDATER/\n'
       '├── src/armor_updater/\n'
       '│   ├── project_manifest.py registry.py ecosystem_catalog.py   マニフェスト、一覧、カタログ\n'
       '│   ├── detect.py github_client.py version_parse.py            ローカルとリモートの検出、バージョン\n'
       '│   ├── install.py git_ops.py staging.py                       段階的なインストールと更新\n'
       '│   ├── promotion.py releases.py deploy_category.py            ロック、ジャーナル、バックアップ、配置\n'
       '│   ├── signature.py                                           署名付き更新と固定された鍵\n'
       '│   ├── evidence.py settings.py console_flags.py               ログ、設定、フラグ\n'
       '│   ├── main.py                                                コマンドライン\n'
       '│   ├── i18n.py i18n_pt.py i18n_recovery.py result_text.py     8 言語\n'
       '│   ├── gui.py qt_gui.py qml/                                  任意の Qt Quick ウィンドウ\n'
       '│   └── data/ assets/                                          allowed_signers とアイコン\n'
       '├── tests/                                                     25 モジュール 288 件\n'
       '├── docs/                                                      CLI_REFERENCE.md、QML_DESKTOP_GUI.md\n'
       '├── tools/                                                     共通の CI 検査、ランチャー、generate_app_icon.py\n'
       '├── images/                                                    バナー、アイコン、README の画像\n'
       '├── .github/                                                   CI ワークフロー、ダッシュボード通知、Issue と Pull Request のテンプレート\n'
       '├── armor.project.json                                         マニフェスト：版・役割・成熟度\n'
       '├── pyproject.toml                                             パッケージ情報とエントリー\n'
       '├── CHANGELOG.md                                               各バージョンの変更点\n'
       '├── run-gui.vbs                                                Windows でコンソールなしにウィンドウを開く\n'
       '├── run.sh run.bat                                             起動（共通フロー）\n'
       '├── build.sh build.bat                                         ビルドとテスト（共通フロー）\n'
       '├── build-test.sh build-test.bat                               ビルド、テスト、パッケージ化\n'
       '├── test.sh test.bat                                           テストのみ（版は変えません）\n'
       '└── SECURITY.md SUPPORT.md CONTRIBUTING.md CODE_OF_CONDUCT.md LICENSE',
 'zh': 'ARMOR-UPDATER/\n'
       '├── src/armor_updater/\n'
       '│   ├── project_manifest.py registry.py ecosystem_catalog.py   清单、列表、目录\n'
       '│   ├── detect.py github_client.py version_parse.py            本地与远程发现、版本\n'
       '│   ├── install.py git_ops.py staging.py                       分阶段安装与更新\n'
       '│   ├── promotion.py releases.py deploy_category.py            锁、日志、备份、布局\n'
       '│   ├── signature.py                                           签名更新与固定密钥\n'
       '│   ├── evidence.py settings.py console_flags.py               日志、设置、选项\n'
       '│   ├── main.py                                                命令行\n'
       '│   ├── i18n.py i18n_pt.py i18n_recovery.py result_text.py     八种语言\n'
       '│   ├── gui.py qt_gui.py qml/                                  可选的 Qt Quick 窗口\n'
       '│   └── data/ assets/                                          allowed_signers 与图标\n'
       '├── tests/                                                     25 个模块 288 项测试\n'
       '├── docs/                                                      CLI_REFERENCE.md、QML_DESKTOP_GUI.md\n'
       '├── tools/                                                     共用的 CI 检查、启动器和 generate_app_icon.py\n'
       '├── images/                                                    横幅图、图标和 README 的图片\n'
       '├── .github/                                                   CI 工作流、仪表板通知、议题和 pull request 模板\n'
       '├── armor.project.json                                         清单：版本、角色、成熟度\n'
       '├── pyproject.toml                                             包元数据、入口\n'
       '├── CHANGELOG.md                                               每个版本的变化\n'
       '├── run-gui.vbs                                                在 Windows 上无控制台地打开窗口\n'
       '├── run.sh run.bat                                             启动（共用流程）\n'
       '├── build.sh build.bat                                         构建并测试（共用流程）\n'
       '├── build-test.sh build-test.bat                               构建、测试并打包\n'
       '├── test.sh test.bat                                           只运行测试，不改版本\n'
       '└── SECURITY.md SUPPORT.md CONTRIBUTING.md CODE_OF_CONDUCT.md LICENSE',
 'pt': 'ARMOR-UPDATER/\n'
       '├── src/armor_updater/\n'
       '│   ├── project_manifest.py registry.py ecosystem_catalog.py   o manifesto, a lista, o catálogo\n'
       '│   ├── detect.py github_client.py version_parse.py            descoberta local e remota, versões\n'
       '│   ├── install.py git_ops.py staging.py                       instalação e atualização por fases\n'
       '│   ├── promotion.py releases.py deploy_category.py            bloqueio, diário, cópias, disposições\n'
       '│   ├── signature.py                                           atualizações assinadas, chaves fixadas\n'
       '│   ├── evidence.py settings.py console_flags.py               o registo, as definições, as opções\n'
       '│   ├── main.py                                                a linha de comandos\n'
       '│   ├── i18n.py i18n_pt.py i18n_recovery.py result_text.py     os oito idiomas\n'
       '│   ├── gui.py qt_gui.py qml/                                  a janela Qt Quick opcional\n'
       '│   └── data/ assets/                                          allowed_signers; o ícone\n'
       '├── tests/                                                     288 testes em 25 módulos\n'
       '├── docs/                                                      CLI_REFERENCE.md, QML_DESKTOP_GUI.md\n'
       '├── tools/                                                     as verificações de CI, o lançador e generate_app_icon.py\n'
       '├── images/                                                    faixa, ícone e as imagens do README\n'
       '├── .github/                                                   fluxo de CI, aviso ao painel, modelos de issues e pull requests\n'
       '├── armor.project.json                                         manifesto: versão, função, maturidade\n'
       '├── pyproject.toml                                             metadados do pacote, entradas\n'
       '├── CHANGELOG.md                                               o que mudou em cada versão\n'
       '├── run-gui.vbs                                                abre a janela no Windows sem consola\n'
       '├── run.sh run.bat                                             arrancar, fluxo partilhado\n'
       '├── build.sh build.bat                                         compilar e testar, fluxo partilhado\n'
       '├── build-test.sh build-test.bat                               compilar, testar e empacotar\n'
       '├── test.sh test.bat                                           só os testes, nunca a versão\n'
       '└── SECURITY.md SUPPORT.md CONTRIBUTING.md CODE_OF_CONDUCT.md LICENSE'}

DIAGRAM = ''

NT = "288"
FACTS["badges"] = [x for x in FACTS["badges"] if x[0] != "Tests"] + [["Tests", NT + "%20passing", "2ea44f"]]


def L(lg, key):
    return LEGACY[lg][key]


GLANCE = [
    (GL["role"], T("Desktop tool that installs and updates the family on a PC, one project at a time | Herramienta de escritorio que instala y actualiza la familia en un PC, un proyecto cada vez | Desktop-Werkzeug, das die Familie auf einem PC installiert und aktualisiert, ein Projekt nach dem anderen | Outil de bureau qui installe et met à jour la famille sur un PC, un projet à la fois | Strumento desktop che installa e aggiorna la famiglia su un PC, un progetto alla volta | 1 つずつ、PC 上のファミリーをインストール・更新するデスクトップツール | 在 PC 上逐个安装和更新整个家族的桌面工具 | Ferramenta de secretária que instala e atualiza a família num PC, um projeto de cada vez")),
    (GL["stack"], T("Python 3.10+, git; optional PySide6 (Qt Quick) | Python 3.10+, git; PySide6 (Qt Quick) opcional | Python 3.10+, git; optional PySide6 (Qt Quick) | Python 3.10+, git ; PySide6 (Qt Quick) facultatif | Python 3.10+, git; PySide6 (Qt Quick) facoltativo | Python 3.10+、git。任意で PySide6（Qt Quick） | Python 3.10+、git；可选 PySide6（Qt Quick） | Python 3.10+, git; PySide6 (Qt Quick) opcional")),
    (GL["tests"], T("288 (`python -m pytest tests -q`, about six minutes) | 288 (`python -m pytest tests -q`, unos seis minutos) | 288 (`python -m pytest tests -q`, etwa sechs Minuten) | 288 (`python -m pytest tests -q`, environ six minutes) | 288 (`python -m pytest tests -q`, circa sei minuti) | 288 件（`python -m pytest tests -q`、約 6 分） | 288 项（`python -m pytest tests -q`，约六分钟） | 288 (`python -m pytest tests -q`, cerca de seis minutos)")),
]
GLANCE += [
    (GL["interfaces"], P("`armor-updater --cli` with `status`, `install`, `update`, `rollback` and `backups`, and a Qt Quick window in eight languages", "`armor-updater --cli` con `status`, `install`, `update`, `rollback` y `backups`, y una ventana Qt Quick en ocho idiomas", "`armor-updater --cli` mit `status`, `install`, `update`, `rollback` und `backups` sowie ein Qt-Quick-Fenster in acht Sprachen",
                         "`armor-updater --cli` avec `status`, `install`, `update`, `rollback` et `backups`, et une fenêtre Qt Quick en huit langues", "`armor-updater --cli` con `status`, `install`, `update`, `rollback` e `backups`, e una finestra Qt Quick in otto lingue", "`armor-updater --cli`（`status`、`install`、`update`、`rollback`、`backups`）と 8 言語の Qt Quick ウィンドウ",
                         "`armor-updater --cli`（`status`、`install`、`update`、`rollback`、`backups`）以及八种语言的 Qt Quick 窗口", "`armor-updater --cli` com `status`, `install`, `update`, `rollback` e `backups`, e uma janela Qt Quick em oito idiomas")),
    (GL["runs"], T("A PC with Python and git (the window has only run on Windows) | Un PC con Python y git (la ventana solo ha corrido en Windows) | Ein PC mit Python und git (das Fenster lief nur unter Windows) | Un PC avec Python et git (la fenêtre n'a tourné que sous Windows) | Un PC con Python e git (la finestra ha girato solo su Windows) | Python と git のある PC（ウィンドウは Windows でのみ動作確認） | 装有 Python 和 git 的 PC（窗口只在 Windows 上运行过） | Um PC com Python e git (a janela só correu no Windows)")),
    (GL["hardware"], {lg: LEGACY[lg]["hardware"] for lg in LGS}),
    (GL["license"], LICENSE_VALUE),
]

ROLE_TABLE = [
    (T("Local workspace | Carpeta de trabajo local | Lokaler Arbeitsordner | Dossier de travail local | Cartella di lavoro locale | ローカルのワークスペース | 本地工作区 | Pasta de trabalho local"), T("folders with a valid `armor.project.json` | carpetas con un `armor.project.json` válido | Ordner mit gültiger `armor.project.json` | dossiers avec un `armor.project.json` valide | cartelle con un `armor.project.json` valido | 有効な `armor.project.json` を持つフォルダー | 带有效 `armor.project.json` 的文件夹 | pastas com um `armor.project.json` válido"), T("what is installed and in which version | qué está instalado y en qué versión | was installiert ist und in welcher Version | ce qui est installé et en quelle version | cosa è installato e in quale versione | インストール済みの内容とバージョン | 已安装什么、什么版本 | o que está instalado e em que versão")),
    ("GitHub", T("`api.github.com`, `raw.githubusercontent.com` and git; `GITHUB_TOKEN` optional | `api.github.com`, `raw.githubusercontent.com` y git; `GITHUB_TOKEN` opcional | `api.github.com`, `raw.githubusercontent.com` und git; `GITHUB_TOKEN` optional | `api.github.com`, `raw.githubusercontent.com` et git ; `GITHUB_TOKEN` facultatif | `api.github.com`, `raw.githubusercontent.com` e git; `GITHUB_TOKEN` facoltativo | `api.github.com`、`raw.githubusercontent.com`、git。`GITHUB_TOKEN` は任意 | `api.github.com`、`raw.githubusercontent.com` 和 git；`GITHUB_TOKEN` 可选 | `api.github.com`, `raw.githubusercontent.com` e git; `GITHUB_TOKEN` opcional"), T("the latest version of every repository of the account | la última versión de cada repositorio de la cuenta | die neueste Version jedes Repositorys des Kontos | la dernière version de chaque dépôt du compte | l'ultima versione di ogni repository dell'account | アカウントの各リポジトリの最新バージョン | 账户中每个仓库的最新版本 | a última versão de cada repositório da conta")),
    ("ARMOR-COMMON", T("a project may list it in `requires` | un proyecto puede listarlo en `requires` | ein Projekt kann es in `requires` aufführen | un projet peut le lister dans `requires` | un progetto può elencarlo in `requires` | プロジェクトは `requires` に挙げられる | 项目可在 `requires` 中列出它 | um projeto pode listá-lo em `requires`"), T("it goes first in every batch: every build needs it | va primero en cada lote: toda compilación lo necesita | es kommt in jedem Stapel zuerst: jeder Build braucht es | il passe en premier dans chaque lot : chaque build en a besoin | va per primo in ogni lotto: ogni compilazione ne ha bisogno | どのバッチでも最初：すべてのビルドが必要とする | 每批都排在最前：每次构建都需要它 | vai primeiro em cada lote: toda a compilação precisa dele")),
    ("ARMOR-DEVOPS", T("separate | aparte | getrennt | séparé | separato | 別物 | 另一套 | à parte"), T("the updates that ARMOR-STUDIO drives on the CM5 go through it, not through this tool | las actualizaciones que ARMOR-STUDIO dirige en la CM5 pasan por él, no por esta herramienta | die Updates, die ARMOR-STUDIO auf dem CM5 steuert, laufen darüber, nicht über dieses Werkzeug | les mises à jour que ARMOR-STUDIO pilote sur le CM5 passent par lui, pas par cet outil | gli aggiornamenti che ARMOR-STUDIO guida sulla CM5 passano da lui, non da questo strumento | ARMOR-STUDIO が CM5 で行う更新はこのツールではなくそちらを通る | ARMOR-STUDIO 在 CM5 上驱动的更新走它，而不是本工具 | as atualizações que o ARMOR-STUDIO conduz no CM5 passam por ele, não por esta ferramenta")),
]


def S(a, b):
    return (T(a), T(b))


SECURITY_ROWS = [
    S("Compromised code gets installed | Se instala código comprometido | Kompromittierter Code wird installiert | Du code compromis est installé | Viene installato codice compromesso | 侵害されたコードがインストールされる | 安装了被攻破的代码 | Instala-se código comprometido",
      "The commits are checked against signers in `data/allowed_signers` (OpenSSH format) whose fingerprint is pinned in `signature.py`; changing the file without the pin makes every check fail (closed); `signature_policy` is `warn` (default: installs and says it is not signed) or `require` (refuses) | Los commits se comprueban con firmantes de `data/allowed_signers` (formato OpenSSH) cuya huella está fijada en `signature.py`; cambiar el fichero sin cambiar la huella hace fallar toda comprobación (cierra en falso); `signature_policy` es `warn` (defecto: instala y dice que no está firmado) o `require` (rechaza) | Die Commits werden gegen Signierer in `data/allowed_signers` (OpenSSH-Format) geprüft, deren Fingerabdruck in `signature.py` fixiert ist; ändert man die Datei ohne den Pin, scheitert jede Prüfung (geschlossen); `signature_policy` ist `warn` (Standard: installiert und sagt, dass nicht signiert ist) oder `require` (lehnt ab) | Les commits sont vérifiés contre les signataires de `data/allowed_signers` (format OpenSSH) dont l'empreinte est épinglée dans `signature.py` ; modifier le fichier sans l'épingle fait échouer toute vérification (fermé) ; `signature_policy` vaut `warn` (défaut : installe et dit que ce n'est pas signé) ou `require` (refuse) | I commit sono verificati con i firmatari di `data/allowed_signers` (formato OpenSSH) la cui impronta è fissata in `signature.py`; cambiare il file senza il pin fa fallire ogni controllo (chiuso); `signature_policy` è `warn` (default: installa e dice che non è firmato) o `require` (rifiuta) | コミットは `data/allowed_signers`（OpenSSH 形式）の署名者で検証し、その指紋は `signature.py` に固定。ファイルだけ変えると全検査が失敗します（閉じる側）。`signature_policy` は `warn`（既定：インストールして未署名と表示）か `require`（拒否） | 提交会用 `data/allowed_signers`（OpenSSH 格式）中的签名者校验，其指纹固定在 `signature.py`；只改文件不改固定值会使所有检查失败（保持关闭）；`signature_policy` 为 `warn`（默认：照常安装并说明未签名）或 `require`（拒绝） | Os commits são verificados com assinantes de `data/allowed_signers` (formato OpenSSH) cuja impressão digital está fixada em `signature.py`; mudar o ficheiro sem mudar o pin faz falhar toda a verificação (fecha); `signature_policy` é `warn` (predefinição: instala e diz que não está assinado) ou `require` (recusa)"),
    S("A half-finished install or a replacement in place | Una instalación a medias o un reemplazo en caliente | Eine halbe Installation oder ein Ersatz an Ort und Stelle | Une installation à moitié faite ou un remplacement en place | Un'installazione a metà o una sostituzione sul posto | 中途半端なインストールや、その場での置き換え | 安装到一半或原地替换 | Uma instalação a meio ou uma substituição no sítio",
      "Never in place: everything is built and verified in an independent staging clone and promoted with two journalled renames (`promotion.json`); the replaced checkout is kept in `.armor-updater/backups/` (the newest three) | Nunca en sitio: todo se construye y verifica en un clon de preparación independiente y se promueve con dos renombrados con diario (`promotion.json`); la copia sustituida se guarda en `.armor-updater/backups/` (las tres más nuevas) | Nie an Ort und Stelle: alles wird in einem unabhängigen Staging-Klon gebaut und geprüft und mit zwei journalisierten Umbenennungen übernommen (`promotion.json`); der ersetzte Checkout bleibt in `.armor-updater/backups/` (die neuesten drei) | Jamais en place : tout est construit et vérifié dans un clone de préparation indépendant et promu par deux renommages journalisés (`promotion.json`) ; la copie remplacée est gardée dans `.armor-updater/backups/` (les trois plus récentes) | Mai sul posto: tutto è costruito e verificato in un clone di preparazione indipendente e promosso con due rinomine a diario (`promotion.json`); la copia sostituita resta in `.armor-updater/backups/` (le tre più recenti) | その場では置き換えません。独立したステージングクローンでビルドと検証を終え、ジャーナル付きの 2 回のリネーム（`promotion.json`）で昇格します。置き換えたチェックアウトは `.armor-updater/backups/` に最新 3 つ残します | 从不原地替换：全部在独立的暂存克隆中构建并验证，再用两次带日志的重命名（`promotion.json`）提升；被替换的副本保存在 `.armor-updater/backups/`（最新三份） | Nunca no sítio: tudo é construído e verificado num clone de preparação independente e promovido com duas mudanças de nome com diário (`promotion.json`); a cópia substituída fica em `.armor-updater/backups/` (as três mais recentes)"),
    S("Two updaters on one workspace | Dos actualizadores en una misma carpeta | Zwei Updater auf einem Arbeitsordner | Deux mises à jour sur un même dossier | Due aggiornatori sulla stessa cartella | 1 つのワークスペースで 2 つの更新が動く | 两个更新程序同时操作一个工作区 | Dois atualizadores na mesma pasta",
      "A lock (`.armor-updater/lock`) that goes stale after 6 hours | Un bloqueo (`.armor-updater/lock`) que caduca a las 6 horas | Eine Sperre (`.armor-updater/lock`), die nach 6 Stunden verfällt | Un verrou (`.armor-updater/lock`) qui expire après 6 heures | Un blocco (`.armor-updater/lock`) che scade dopo 6 ore | 6 時間で期限切れになるロック（`.armor-updater/lock`） | 6 小时后过期的锁（`.armor-updater/lock`） | Um bloqueio (`.armor-updater/lock`) que caduca às 6 horas"),
    S("A dependency that is not built | Una dependencia sin construir | Eine nicht gebaute Abhängigkeit | Une dépendance non construite | Una dipendenza non costruita | ビルドされていない依存 | 未构建的依赖 | Uma dependência por construir",
      "ARMOR-COMMON goes first and a project is not built without it; the optional `requires` field of the manifest orders a batch and refuses an install with a clear message in the language of the window | ARMOR-COMMON va primero y un proyecto no se construye sin él; el campo opcional `requires` del manifiesto ordena un lote y rechaza una instalación con un mensaje claro en el idioma de la ventana | ARMOR-COMMON kommt zuerst und ein Projekt wird ohne es nicht gebaut; das optionale Feld `requires` des Manifests ordnet einen Stapel und lehnt eine Installation mit klarer Meldung in der Sprache des Fensters ab | ARMOR-COMMON passe en premier et un projet n'est pas construit sans lui ; le champ facultatif `requires` du manifeste ordonne un lot et refuse une installation avec un message clair dans la langue de la fenêtre | ARMOR-COMMON va per primo e un progetto non si costruisce senza di lui; il campo facoltativo `requires` del manifesto ordina un lotto e rifiuta un'installazione con un messaggio chiaro nella lingua della finestra | ARMOR-COMMON が最初で、それなしではビルドしません。マニフェストの任意項目 `requires` でバッチの順序を決め、足りなければウィンドウの言語で分かりやすく拒否します | ARMOR-COMMON 排在最前，没有它就不构建项目；清单的可选字段 `requires` 决定批次顺序，并用窗口所用语言清楚地拒绝安装 | ARMOR-COMMON vai primeiro e um projeto não se constrói sem ele; o campo opcional `requires` do manifesto ordena um lote e recusa uma instalação com uma mensagem clara no idioma da janela"),
    S("Local edits lost | Cambios locales perdidos | Verlorene lokale Änderungen | Modifications locales perdues | Modifiche locali perse | ローカルの変更が失われる | 本地修改丢失 | Alterações locais perdidas",
      "An update to the commit already installed does nothing; a genuinely uncommitted local edit is refused outright | Una actualización al commit ya instalado no hace nada; un cambio local realmente sin guardar se rechaza de plano | Ein Update auf den bereits installierten Commit tut nichts; eine wirklich nicht committete lokale Änderung wird glatt abgelehnt | Une mise à jour vers le commit déjà installé ne fait rien ; une modification locale réellement non validée est refusée net | Un aggiornamento al commit già installato non fa nulla; una modifica locale davvero non committata viene rifiutata del tutto | すでに入っているコミットへの更新は何もしません。本当にコミットされていないローカル変更があれば完全に拒否します | 更新到已安装的提交时什么也不做；真正未提交的本地修改会被直接拒绝 | Uma atualização para o commit já instalado não faz nada; uma alteração local realmente sem commit é recusada de vez"),
    S("A fake discovery | Un descubrimiento falso | Eine gefälschte Entdeckung | Une fausse découverte | Una scoperta falsa | 偽の検出 | 虚假发现 | Uma descoberta falsa",
      "A project counts only with a valid `armor.project.json` that declares `ecosystem: \"A.R.M.O.R.\"`; remotely, every public repository of the account is checked the same way | Un proyecto solo cuenta con un `armor.project.json` válido que declare `ecosystem: \"A.R.M.O.R.\"`; en remoto, cada repositorio público de la cuenta se comprueba igual | Ein Projekt zählt nur mit gültiger `armor.project.json`, die `ecosystem: \"A.R.M.O.R.\"` erklärt; entfernt wird jedes öffentliche Repository des Kontos genauso geprüft | Un projet ne compte qu'avec un `armor.project.json` valide qui déclare `ecosystem: \"A.R.M.O.R.\"` ; à distance, chaque dépôt public du compte est vérifié de même | Un progetto conta solo con un `armor.project.json` valido che dichiari `ecosystem: \"A.R.M.O.R.\"`; da remoto, ogni repository pubblico dell'account è verificato allo stesso modo | `ecosystem: \"A.R.M.O.R.\"` を宣言する有効な `armor.project.json` があるプロジェクトだけが対象です。リモートでもアカウントの公開リポジトリを同様に検査します | 只有带有效 `armor.project.json` 且声明 `ecosystem: \"A.R.M.O.R.\"` 的项目才算数；远程时对账户的每个公开仓库做同样的检查 | Um projeto só conta com um `armor.project.json` válido que declare `ecosystem: \"A.R.M.O.R.\"`; remotamente, cada repositório público da conta é verificado do mesmo modo"),
    S("GitHub slow or down | GitHub lento o caído | GitHub langsam oder nicht erreichbar | GitHub lent ou en panne | GitHub lento o non raggiungibile | GitHub が遅い、または停止 | GitHub 缓慢或宕机 | GitHub lento ou em baixo",
      "Request timeout 10 s, up to 8 at a time, 3 retries (0.5 s base wait), `ls-remote` 20 s; the delay of minutes of `raw.githubusercontent.com` is allowed for | Tiempo de espera de 10 s, hasta 8 a la vez, 3 reintentos (espera base 0,5 s), `ls-remote` 20 s; se tiene en cuenta el retraso de minutos de `raw.githubusercontent.com` | Zeitlimit 10 s, bis zu 8 gleichzeitig, 3 Wiederholungen (Basiswartezeit 0,5 s), `ls-remote` 20 s; die Verzögerung von Minuten bei `raw.githubusercontent.com` ist eingeplant | Délai de 10 s, jusqu'à 8 à la fois, 3 nouvelles tentatives (attente de base 0,5 s), `ls-remote` 20 s ; le retard de quelques minutes de `raw.githubusercontent.com` est prévu | Timeout di 10 s, fino a 8 alla volta, 3 tentativi (attesa base 0,5 s), `ls-remote` 20 s; il ritardo di minuti di `raw.githubusercontent.com` è previsto | リクエストのタイムアウト 10 秒、同時 8 件まで、3 回再試行（基本待機 0.5 秒）、`ls-remote` は 20 秒。`raw.githubusercontent.com` の数分の遅れも考慮 | 请求超时 10 秒，最多同时 8 个，重试 3 次（基础等待 0.5 秒），`ls-remote` 20 秒；已考虑 `raw.githubusercontent.com` 数分钟的延迟 | Tempo limite de 10 s, até 8 de cada vez, 3 repetições (espera base de 0,5 s), `ls-remote` 20 s; o atraso de minutos de `raw.githubusercontent.com` está previsto"),
]
SEC_TAIL = P("Every attempt, successful or not, appends one line to the local evidence log (project, version and commit before and after, reason of a failure). The installs need `git` and the build tools of each repository; the signature is only warned about unless `require` is chosen; it has not been run against every repository of the family end to end, and there has been no independent review.",
             "Cada intento, bueno o malo, añade una línea al registro local de evidencias (proyecto, versión y commit antes y después, razón del fallo). Las instalaciones necesitan `git` y las herramientas de construcción de cada repositorio; la firma solo avisa salvo que se elija `require`; no se ha ejecutado contra todos los repositorios de la familia de punta a punta y no ha habido revisión independiente.",
             "Jeder Versuch, ob erfolgreich oder nicht, hängt eine Zeile an das lokale Nachweisprotokoll an (Projekt, Version und Commit vorher und nachher, Fehlergrund). Die Installationen brauchen `git` und die Build-Werkzeuge jedes Repositorys; die Signatur wird nur gemeldet, außer man wählt `require`; es lief nicht gegen jedes Repository der Familie von Anfang bis Ende, und eine unabhängige Prüfung gab es nicht.",
             "Chaque tentative, réussie ou non, ajoute une ligne au journal de preuves local (projet, version et commit avant et après, raison d'un échec). Les installations demandent `git` et les outils de construction de chaque dépôt ; la signature n'est qu'avertie sauf si l'on choisit `require` ; il n'a pas été exécuté contre tous les dépôts de la famille de bout en bout et il n'y a pas eu de revue indépendante.",
             "Ogni tentativo, riuscito o no, aggiunge una riga al registro locale delle prove (progetto, versione e commit prima e dopo, motivo di un fallimento). Le installazioni richiedono `git` e gli strumenti di compilazione di ogni repository; la firma viene solo segnalata salvo si scelga `require`; non è stato eseguito contro tutti i repository della famiglia da cima a fondo e non c'è stata una revisione indipendente.",
             "成功か失敗かを問わず、すべての試行がローカルの証跡ログに 1 行追加されます（プロジェクト、前後のバージョンとコミット、失敗の理由）。インストールには `git` と各リポジトリのビルドツールが必要です。署名は `require` を選ばない限り警告のみです。ファミリーの全リポジトリで通しで動かしたことはなく、第三者によるレビューもありません。",
             "每次尝试无论成败，都会在本地证据日志中追加一行（项目、前后的版本和提交、失败原因）。安装需要 `git` 和每个仓库的构建工具；除非选择 `require`，签名只给出警告；尚未对家族的每个仓库端到端运行，也没有独立审查。",
             "Cada tentativa, bem-sucedida ou não, acrescenta uma linha ao registo local de provas (projeto, versão e commit antes e depois, razão de uma falha). As instalações precisam de `git` e das ferramentas de compilação de cada repositório; a assinatura só avisa, a menos que se escolha `require`; não foi executado contra todos os repositórios da família de ponta a ponta e não houve revisão independente.")

CLI = [
    ("`armor-updater --cli status`", "-", T("what is installed, its version and the latest on GitHub; `--workspace D`, `--offline` (local only), `--notes` (the real notes of each project), `--json` (machine-readable) | qué está instalado, su versión y la última en GitHub; `--workspace D`, `--offline` (solo local), `--notes` (las notas reales de cada proyecto), `--json` (legible por máquina) | was installiert ist, seine Version und die neueste auf GitHub; `--workspace D`, `--offline` (nur lokal), `--notes` (die echten Notizen jedes Projekts), `--json` (maschinenlesbar) | ce qui est installé, sa version et la dernière sur GitHub ; `--workspace D`, `--offline` (local seulement), `--notes` (les vraies notes de chaque projet), `--json` (lisible par machine) | cosa è installato, la sua versione e l'ultima su GitHub; `--workspace D`, `--offline` (solo locale), `--notes` (le note reali di ogni progetto), `--json` (leggibile da macchina) | インストール済みの内容、バージョン、GitHub 上の最新。`--workspace D`、`--offline`（ローカルのみ）、`--notes`（各プロジェクトの実際のメモ）、`--json`（機械可読） | 已安装内容、其版本以及 GitHub 上的最新版本；`--workspace D`、`--offline`（仅本地）、`--notes`（各项目的真实说明）、`--json`（机器可读） | o que está instalado, a sua versão e a última no GitHub; `--workspace D`, `--offline` (só local), `--notes` (as notas reais de cada projeto), `--json` (legível por máquina)")),
    ("`armor-updater --cli install <project>`", "-", T("clone, build and install ONE project that is not installed yet; `--no-build` only clones | clona, construye e instala UN proyecto que aún no está instalado; `--no-build` solo clona | EIN noch nicht installiertes Projekt klonen, bauen und installieren; `--no-build` klont nur | clone, construit et installe UN projet pas encore installé ; `--no-build` clone seulement | clona, compila e installa UN progetto non ancora installato; `--no-build` clona soltanto | まだ入っていないプロジェクト 1 つをクローン・ビルド・インストール。`--no-build` はクローンのみ | 克隆、构建并安装一个尚未安装的项目；`--no-build` 只克隆 | clona, constrói e instala UM projeto ainda não instalado; `--no-build` só clona")),
    ("`armor-updater --cli update <project>`", "-", T("update an installed one, built and verified before it is put in place; `--no-build` only pulls | actualiza uno instalado, construido y verificado antes de ponerlo en su sitio; `--no-build` solo trae los cambios | ein installiertes aktualisieren, vor dem Einsetzen gebaut und geprüft; `--no-build` holt nur | met à jour un projet installé, construit et vérifié avant d'être mis en place ; `--no-build` récupère seulement | aggiorna uno installato, compilato e verificato prima di metterlo a posto; `--no-build` scarica soltanto | インストール済みを更新（置き換える前にビルドと検証）。`--no-build` は取得のみ | 更新已安装的项目，先构建并验证再就位；`--no-build` 只拉取 | atualiza um instalado, construído e verificado antes de o pôr no lugar; `--no-build` só obtém")),
    ("`armor-updater --cli rollback <project>`", "-", T("put the newest backup of the replaced checkout back | devuelve la copia más nueva del proyecto sustituido | die neueste Sicherung des ersetzten Checkouts zurückspielen | remet la copie la plus récente du dépôt remplacé | rimette la copia più recente del checkout sostituito | 置き換えたチェックアウトの最新バックアップを戻す | 放回被替换副本的最新备份 | repõe a cópia mais recente do checkout substituído")),
    ("`armor-updater --cli backups [<project>]`", "-", T("list the backups of replaced checkouts and the disk they take; `--prune N` keeps the newest N of each | lista las copias de proyectos sustituidos y el disco que ocupan; `--prune N` conserva las N más nuevas de cada uno | die Sicherungen ersetzter Checkouts und ihren Plattenbedarf auflisten; `--prune N` behält die neuesten N je Projekt | liste les copies des dépôts remplacés et le disque qu'elles occupent ; `--prune N` garde les N plus récentes de chacun | elenca le copie dei checkout sostituiti e il disco che occupano; `--prune N` tiene le N più recenti di ciascuno | 置き換えたチェックアウトのバックアップと使用ディスク量を一覧。`--prune N` で各プロジェクトの最新 N 個を残す | 列出被替换副本的备份及其占用磁盘；`--prune N` 每个项目只保留最新 N 份 | lista as cópias dos checkouts substituídos e o disco que ocupam; `--prune N` mantém as N mais recentes de cada um")),
    ("`armor-updater --version`", "-", T("the version of the tool | la versión de la herramienta | die Version des Werkzeugs | la version de l'outil | la versione dello strumento | ツールのバージョン | 工具版本 | a versão da ferramenta")),
]
IFACE_NOTE = P("The window (Qt Quick, `pip install \".[gui]\"`, started on Windows by `run-gui.vbs`) shows the same state, installs and updates one project, restores the previous copy of a project or deletes the copies kept, and states when a revision is not signed; it is worded in eight languages (`i18n.py`, `i18n_pt.py`, `i18n_recovery.py`, `result_text.py`) and has only been run on Windows. Full reference: [docs/CLI_REFERENCE.md](docs/CLI_REFERENCE.md) and [docs/QML_DESKTOP_GUI.md](docs/QML_DESKTOP_GUI.md).",
               "La ventana (Qt Quick, `pip install \".[gui]\"`, que en Windows arranca `run-gui.vbs`) muestra el mismo estado, instala y actualiza un proyecto, restaura la copia anterior de un proyecto o borra las copias guardadas, y dice cuándo una revisión no está firmada; está redactada en ocho idiomas (`i18n.py`, `i18n_pt.py`, `i18n_recovery.py`, `result_text.py`) y solo se ha ejecutado en Windows. Referencia completa: [docs/CLI_REFERENCE.md](docs/CLI_REFERENCE.md) y [docs/QML_DESKTOP_GUI.md](docs/QML_DESKTOP_GUI.md).",
               "Das Fenster (Qt Quick, `pip install \".[gui]\"`, unter Windows von `run-gui.vbs` gestartet) zeigt denselben Zustand, installiert und aktualisiert ein Projekt, stellt die vorige Kopie eines Projekts wieder her oder löscht die aufbewahrten Kopien und sagt, wenn eine Revision nicht signiert ist; es ist in acht Sprachen verfasst (`i18n.py`, `i18n_pt.py`, `i18n_recovery.py`, `result_text.py`) und lief nur unter Windows. Vollständige Referenz: [docs/CLI_REFERENCE.md](docs/CLI_REFERENCE.md) und [docs/QML_DESKTOP_GUI.md](docs/QML_DESKTOP_GUI.md).",
               "La fenêtre (Qt Quick, `pip install \".[gui]\"`, lancée sous Windows par `run-gui.vbs`) affiche le même état, installe et met à jour un projet, restaure la copie précédente d'un projet ou supprime les copies gardées, et dit quand une révision n'est pas signée ; elle est rédigée en huit langues (`i18n.py`, `i18n_pt.py`, `i18n_recovery.py`, `result_text.py`) et n'a tourné que sous Windows. Référence complète : [docs/CLI_REFERENCE.md](docs/CLI_REFERENCE.md) et [docs/QML_DESKTOP_GUI.md](docs/QML_DESKTOP_GUI.md).",
               "La finestra (Qt Quick, `pip install \".[gui]\"`, avviata su Windows da `run-gui.vbs`) mostra lo stesso stato, installa e aggiorna un progetto, ripristina la copia precedente di un progetto o elimina le copie conservate, e dice quando una revisione non è firmata; è scritta in otto lingue (`i18n.py`, `i18n_pt.py`, `i18n_recovery.py`, `result_text.py`) e ha girato solo su Windows. Riferimento completo: [docs/CLI_REFERENCE.md](docs/CLI_REFERENCE.md) e [docs/QML_DESKTOP_GUI.md](docs/QML_DESKTOP_GUI.md).",
               "ウィンドウ（Qt Quick、`pip install \".[gui]\"`、Windows では `run-gui.vbs` で起動）は同じ状態を表示し、プロジェクトを 1 つインストール・更新し、前のコピーを復元または保管コピーを削除し、リビジョンが未署名であることを表示します。8 言語で書かれており（`i18n.py`、`i18n_pt.py`、`i18n_recovery.py`、`result_text.py`）、Windows でのみ動作確認済みです。詳細は [docs/CLI_REFERENCE.md](docs/CLI_REFERENCE.md) と [docs/QML_DESKTOP_GUI.md](docs/QML_DESKTOP_GUI.md)。",
               "窗口（Qt Quick，`pip install \".[gui]\"`，在 Windows 上由 `run-gui.vbs` 启动）显示同样的状态，安装和更新一个项目，恢复某项目的上一份副本或删除保留的副本，并说明某个修订未签名；它有八种语言（`i18n.py`、`i18n_pt.py`、`i18n_recovery.py`、`result_text.py`），只在 Windows 上运行过。完整参考：[docs/CLI_REFERENCE.md](docs/CLI_REFERENCE.md) 和 [docs/QML_DESKTOP_GUI.md](docs/QML_DESKTOP_GUI.md)。",
               "A janela (Qt Quick, `pip install \".[gui]\"`, no Windows iniciada por `run-gui.vbs`) mostra o mesmo estado, instala e atualiza um projeto, restaura a cópia anterior de um projeto ou apaga as cópias guardadas, e diz quando uma revisão não está assinada; está redigida em oito idiomas (`i18n.py`, `i18n_pt.py`, `i18n_recovery.py`, `result_text.py`) e só correu no Windows. Referência completa: [docs/CLI_REFERENCE.md](docs/CLI_REFERENCE.md) e [docs/QML_DESKTOP_GUI.md](docs/QML_DESKTOP_GUI.md).")

CFG = [
    ("`--workspace`", T("the parent folder of the tool | la carpeta padre de la herramienta | der übergeordnete Ordner des Werkzeugs | le dossier parent de l'outil | la cartella superiore dello strumento | ツールの親フォルダー | 工具的上级文件夹 | a pasta-mãe da ferramenta"), T("the workspace root to scan | la raíz de la carpeta de trabajo que se escanea | die zu durchsuchende Wurzel des Arbeitsordners | la racine du dossier de travail à parcourir | la radice della cartella di lavoro da esaminare | スキャンするワークスペースのルート | 要扫描的工作区根目录 | a raiz da pasta de trabalho a examinar")),
    ("`GITHUB_TOKEN`", T("optional | opcional | optional | facultatif | facoltativo | 任意 | 可选 | opcional"), T("raises GitHub's limit of 60 requests an hour; it is only read, never written | sube el límite de GitHub de 60 peticiones por hora; solo se lee, nunca se escribe | hebt das GitHub-Limit von 60 Anfragen pro Stunde an; er wird nur gelesen, nie geschrieben | relève la limite de GitHub de 60 requêtes par heure ; il n'est que lu, jamais écrit | alza il limite di GitHub di 60 richieste all'ora; si legge soltanto, mai si scrive | GitHub の 1 時間 60 リクエストの上限を引き上げる（読むだけで書き込まない） | 提高 GitHub 每小时 60 次请求的限制；只读取，从不写入 | sobe o limite do GitHub de 60 pedidos por hora; só se lê, nunca se escreve")),
    ("`signature_policy`", "warn", T("`warn` installs and says it is not signed; `require` refuses; kept in `~/.armor_updater_settings.json` | `warn` instala y dice que no está firmado; `require` rechaza; se guarda en `~/.armor_updater_settings.json` | `warn` installiert und sagt, dass nicht signiert ist; `require` lehnt ab; gespeichert in `~/.armor_updater_settings.json` | `warn` installe et dit que ce n'est pas signé ; `require` refuse ; gardé dans `~/.armor_updater_settings.json` | `warn` installa e dice che non è firmato; `require` rifiuta; salvato in `~/.armor_updater_settings.json` | `warn` はインストールして未署名と表示、`require` は拒否。`~/.armor_updater_settings.json` に保存 | `warn` 照常安装并说明未签名；`require` 拒绝；保存在 `~/.armor_updater_settings.json` | `warn` instala e diz que não está assinado; `require` recusa; guardada em `~/.armor_updater_settings.json`")),
    (T("Backups kept | Copias guardadas | Gesicherte Kopien | Copies gardées | Copie conservate | 保管するバックアップ | 保留的备份 | Cópias guardadas"), "3", T("the newest three of each project; `backups --prune N` changes it | las tres más nuevas de cada proyecto; `backups --prune N` lo cambia | die neuesten drei je Projekt; `backups --prune N` ändert es | les trois plus récentes de chaque projet ; `backups --prune N` le change | le tre più recenti di ogni progetto; `backups --prune N` lo cambia | 各プロジェクトの最新 3 つ。`backups --prune N` で変更 | 每个项目最新的三份；`backups --prune N` 可更改 | as três mais recentes de cada projeto; `backups --prune N` muda-o")),
    (T("Lock | Bloqueo | Sperre | Verrou | Blocco | ロック | 锁 | Bloqueio"), "6 h", T("a lock older than this is ignored | un bloqueo más viejo se ignora | eine ältere Sperre wird ignoriert | un verrou plus ancien est ignoré | un blocco più vecchio viene ignorato | これより古いロックは無視 | 超过此时间的锁会被忽略 | um bloqueio mais antigo é ignorado")),
]
CFG_NOTE = P("`.env.example` shows the variables a repository build may read. The language of the window follows `~/.armor_updater_settings.json` (and the old `~/.armor_updater_lang.json`).",
             "`.env.example` muestra las variables que puede leer la construcción de un repositorio. El idioma de la ventana sigue a `~/.armor_updater_settings.json` (y al antiguo `~/.armor_updater_lang.json`).",
             "`.env.example` zeigt die Variablen, die der Build eines Repositorys lesen kann. Die Sprache des Fensters folgt `~/.armor_updater_settings.json` (und der alten `~/.armor_updater_lang.json`).",
             "`.env.example` montre les variables que la construction d'un dépôt peut lire. La langue de la fenêtre suit `~/.armor_updater_settings.json` (et l'ancien `~/.armor_updater_lang.json`).",
             "`.env.example` mostra le variabili che la compilazione di un repository può leggere. La lingua della finestra segue `~/.armor_updater_settings.json` (e il vecchio `~/.armor_updater_lang.json`).",
             "`.env.example` は、リポジトリのビルドが読む変数を示します。ウィンドウの言語は `~/.armor_updater_settings.json`（と旧 `~/.armor_updater_lang.json`）に従います。",
             "`.env.example` 列出仓库构建可能读取的变量。窗口语言跟随 `~/.armor_updater_settings.json`（以及旧的 `~/.armor_updater_lang.json`）。",
             "`.env.example` mostra as variáveis que a compilação de um repositório pode ler. O idioma da janela segue `~/.armor_updater_settings.json` (e o antigo `~/.armor_updater_lang.json`).")

QUICK_LEAD = P("**Requirements:** Python 3.10+, `git` and the build tools of the repositories you install; optional: PySide6 for the desktop window.", "**Requisitos:** Python 3.10+, `git` y las herramientas de construcción de los repositorios que instales; opcional: PySide6 para la ventana de escritorio.", "**Voraussetzungen:** Python 3.10+, `git` und die Build-Werkzeuge der Repositorys, die Sie installieren; optional: PySide6 für das Desktop-Fenster.",
               "**Prérequis :** Python 3.10+, `git` et les outils de construction des dépôts que vous installez ; facultatif : PySide6 pour la fenêtre de bureau.", "**Requisiti:** Python 3.10+, `git` e gli strumenti di compilazione dei repository che installi; facoltativo: PySide6 per la finestra desktop.", "**要件：** Python 3.10+、`git`、インストールするリポジトリのビルドツール。任意：デスクトップウィンドウ用の PySide6。",
               "**要求：** Python 3.10+、`git` 以及所装仓库的构建工具；可选：桌面窗口用的 PySide6。", "**Requisitos:** Python 3.10+, `git` e as ferramentas de compilação dos repositórios que instalar; opcional: PySide6 para a janela de secretária.")
QUICK_CODE = [
    ('pip install -e ".[dev]"', T("or \".[dev,gui]\" for the optional Qt Quick window | o \".[dev,gui]\" para la ventana Qt Quick opcional | oder \".[dev,gui]\" für das optionale Qt-Quick-Fenster | ou \".[dev,gui]\" pour la fenêtre Qt Quick facultative | oppure \".[dev,gui]\" per la finestra Qt Quick opzionale | または \".[dev,gui]\"（任意の Qt Quick ウィンドウ用） | 或 \".[dev,gui]\"（可选的 Qt Quick 窗口） | ou \".[dev,gui]\" para a janela Qt Quick opcional")),
    ("python -m pytest tests -q", T("288 tests, about six minutes | 288 pruebas, unos seis minutos | 288 Tests, etwa sechs Minuten | 288 tests, environ six minutes | 288 test, circa sei minuti | 288 件、約 6 分 | 288 项，约六分钟 | 288 testes, cerca de seis minutos")),
    ("armor-updater --cli status", T("local and GitHub state of every repository | estado local y de GitHub de cada repositorio | lokaler und GitHub-Zustand jedes Repositorys | état local et GitHub de chaque dépôt | stato locale e GitHub di ogni repository | 各リポジトリのローカルと GitHub の状態 | 每个仓库的本地和 GitHub 状态 | estado local e do GitHub de cada repositório")),
    ("armor-updater --cli install ARMOR-NETWORK", T("clone, build and install one repository that is not installed yet | clona, construye e instala un repositorio que aún no está instalado | ein noch nicht installiertes Repository klonen, bauen und installieren | clone, construit et installe un dépôt pas encore installé | clona, compila e installa un repository non ancora installato | まだ入っていないリポジトリを 1 つクローン・ビルド・インストール | 克隆、构建并安装一个尚未安装的仓库 | clona, constrói e instala um repositório ainda não instalado")),
    ("armor-updater --cli update ARMOR-NETWORK", T("update an installed one (built and verified before it is put in place) | actualiza uno instalado (construido y verificado antes de ponerlo) | ein installiertes aktualisieren (vor dem Einsetzen gebaut und geprüft) | met à jour un projet installé (construit et vérifié avant mise en place) | aggiorna uno installato (compilato e verificato prima di metterlo) | インストール済みを更新（置き換え前にビルドと検証） | 更新已安装的仓库（先构建并验证再就位） | atualiza um instalado (construído e verificado antes de o pôr)")),
    ("armor-updater --cli rollback ARMOR-NETWORK", T("put the newest backup of a replaced checkout back | devuelve la copia más nueva de un proyecto sustituido | die neueste Sicherung eines ersetzten Checkouts zurückspielen | remet la copie la plus récente d'un dépôt remplacé | rimette la copia più recente di un checkout sostituito | 置き換えたチェックアウトの最新バックアップを戻す | 放回被替换副本的最新备份 | repõe a cópia mais recente de um checkout substituído")),
]
QUICK_AFTER = P("See [docs/CLI_REFERENCE.md](docs/CLI_REFERENCE.md).", "Mira [docs/CLI_REFERENCE.md](docs/CLI_REFERENCE.md).", "Siehe [docs/CLI_REFERENCE.md](docs/CLI_REFERENCE.md).", "Voir [docs/CLI_REFERENCE.md](docs/CLI_REFERENCE.md).", "Vedi [docs/CLI_REFERENCE.md](docs/CLI_REFERENCE.md).", "[docs/CLI_REFERENCE.md](docs/CLI_REFERENCE.md) を参照してください。", "请参阅 [docs/CLI_REFERENCE.md](docs/CLI_REFERENCE.md)。", "Consulte [docs/CLI_REFERENCE.md](docs/CLI_REFERENCE.md).")

TEST_TABLE = [
    (T("Discovery and versions | Descubrimiento y versiones | Entdeckung und Versionen | Découverte et versions | Scoperta e versioni | 検出とバージョン | 发现与版本 | Descoberta e versões"), T("the manifest, the registry, local and remote detection, version parsing and the GitHub client | el manifiesto, el registro, la detección local y remota, el análisis de versiones y el cliente de GitHub | das Manifest, das Register, lokale und entfernte Erkennung, Versionsauswertung und der GitHub-Client | le manifeste, le registre, la détection locale et distante, l'analyse des versions et le client GitHub | il manifesto, il registro, il rilevamento locale e remoto, l'analisi delle versioni e il client GitHub | マニフェスト、レジストリ、ローカルとリモートの検出、バージョン解析、GitHub クライアント | 清单、注册表、本地与远程检测、版本解析和 GitHub 客户端 | o manifesto, o registo, a deteção local e remota, a análise de versões e o cliente do GitHub")),
    (T("Install and update | Instalación y actualización | Installation und Aktualisierung | Installation et mise à jour | Installazione e aggiornamento | インストールと更新 | 安装与更新 | Instalação e atualização"), T("staging, the lock, the journal, the backups and the rollback, requirements and the evidence log | la preparación, el bloqueo, el diario, las copias y la vuelta atrás, los requisitos y el registro de evidencias | Staging, Sperre, Journal, Sicherungen und Rückgängigmachen, Voraussetzungen und das Nachweisprotokoll | la préparation, le verrou, le journal, les copies et le retour arrière, les prérequis et le journal de preuves | la preparazione, il blocco, il diario, le copie e il ripristino, i requisiti e il registro delle prove | ステージング、ロック、ジャーナル、バックアップ、ロールバック、要件、証跡ログ | 暂存、锁、日志、备份与回滚、前置要求和证据日志 | a preparação, o bloqueio, o diário, as cópias e a reversão, os requisitos e o registo de provas")),
    (T("Signatures | Firmas | Signaturen | Signatures | Firme | 署名 | 签名 | Assinaturas"), T("the pinned keys, the closed failure and the two policies | las claves fijadas, el fallo cerrado y las dos políticas | die fixierten Schlüssel, das geschlossene Scheitern und die beiden Richtlinien | les clés épinglées, l'échec fermé et les deux politiques | le chiavi fissate, il fallimento chiuso e le due politiche | 固定された鍵、閉じる側の失敗、2 つのポリシー | 固定密钥、失败时关闭以及两种策略 | as chaves fixadas, a falha fechada e as duas políticas")),
    (T("Command line | Línea de órdenes | Kommandozeile | Ligne de commande | Riga di comando | コマンドライン | 命令行 | Linha de comandos"), T("`status`, `install`, `update`, `rollback` and `backups` with their options | `status`, `install`, `update`, `rollback` y `backups` con sus opciones | `status`, `install`, `update`, `rollback` und `backups` mit ihren Optionen | `status`, `install`, `update`, `rollback` et `backups` avec leurs options | `status`, `install`, `update`, `rollback` e `backups` con le loro opzioni | `status`、`install`、`update`、`rollback`、`backups` とそのオプション | `status`、`install`、`update`、`rollback`、`backups` 及其选项 | `status`, `install`, `update`, `rollback` e `backups` com as suas opções")),
    (T("Languages and window | Idiomas y ventana | Sprachen und Fenster | Langues et fenêtre | Lingue e finestra | 言語とウィンドウ | 语言与窗口 | Idiomas e janela"), T("the eight languages (`test_i18n.py`) and the texts of every result | los ocho idiomas (`test_i18n.py`) y los textos de cada resultado | die acht Sprachen (`test_i18n.py`) und die Texte jedes Ergebnisses | les huit langues (`test_i18n.py`) et les textes de chaque résultat | le otto lingue (`test_i18n.py`) e i testi di ogni risultato | 8 言語（`test_i18n.py`）と各結果の文言 | 八种语言（`test_i18n.py`）与每个结果的文本 | os oito idiomas (`test_i18n.py`) e os textos de cada resultado")),
]
TEST_NOTE = P("`python -m unittest` finds only three of them: the suite is written for pytest (`conftest.py` is in `tests/`) and takes close to six minutes. GitHub Actions runs the A.R.M.O.R. baseline on every push and pull request: the validation of the manifest, version, changelog and README parity, then the project's own build and tests.",
              "`python -m unittest` solo encuentra tres: la batería está escrita para pytest (`conftest.py` está en `tests/`) y tarda casi seis minutos. GitHub Actions ejecuta la base de A.R.M.O.R. en cada push y pull request: la validación del manifiesto, la versión, el registro de cambios y la paridad de los README, y luego la compilación y las pruebas del propio proyecto.",
              "`python -m unittest` findet nur drei davon: Die Suite ist für pytest geschrieben (`conftest.py` liegt in `tests/`) und braucht fast sechs Minuten. GitHub Actions führt bei jedem Push und Pull Request die A.R.M.O.R.-Basis aus: die Prüfung von Manifest, Version, Änderungsprotokoll und README-Parität, dann den eigenen Build und die eigenen Tests des Projekts.",
              "`python -m unittest` n'en trouve que trois : la suite est écrite pour pytest (`conftest.py` est dans `tests/`) et dure près de six minutes. GitHub Actions exécute la base A.R.M.O.R. à chaque push et pull request : la validation du manifeste, de la version, du journal des modifications et de la parité des README, puis le build et les tests propres au projet.",
              "`python -m unittest` ne trova che tre test: la suite è scritta per pytest (`conftest.py` è in `tests/`) e dura quasi sei minuti. GitHub Actions esegue la base A.R.M.O.R. a ogni push e pull request: la validazione di manifesto, versione, registro delle modifiche e parità dei README, poi la compilazione e i test del progetto.",
              "`python -m unittest` では 3 件しか見つかりません。テストは pytest 向けに書かれ（`conftest.py` は `tests/` にあります）、約 6 分かかります。GitHub Actions は push と pull request のたびに A.R.M.O.R. の基本検査（マニフェスト、バージョン、変更履歴、README の一致）と、プロジェクト自身のビルドとテストを実行します。",
              "`python -m unittest` 只能找到其中三项：测试套件是为 pytest 写的（`conftest.py` 在 `tests/` 中），耗时接近六分钟。GitHub Actions 在每次推送和拉取请求时运行 A.R.M.O.R. 基线：清单、版本、更新日志和 README 一致性的校验，然后是项目自身的构建和测试。",
              "`python -m unittest` só encontra três: a bateria está escrita para pytest (`conftest.py` está em `tests/`) e demora quase seis minutos. O GitHub Actions executa a base do A.R.M.O.R. em cada push e pull request: a validação do manifesto, da versão, do registo de alterações e da paridade dos README, e depois a compilação e os testes do próprio projeto.")

BUILD = P("It is plain Python: nothing to compile (`pip install -e .`). The version lives in `pyproject.toml`, in `armor.project.json` and in the README badge (read from the manifest); each version has its entry in [CHANGELOG.md](CHANGELOG.md). Releases are published on GitHub.",
          "Es Python puro: no hay nada que compilar (`pip install -e .`). La versión vive en `pyproject.toml`, en `armor.project.json` y en la insignia del README (leída del manifiesto); cada versión tiene su entrada en [CHANGELOG.md](CHANGELOG.md). Las versiones se publican en GitHub.",
          "Es ist reines Python: Es gibt nichts zu kompilieren (`pip install -e .`). Die Version steht in `pyproject.toml`, in `armor.project.json` und im README-Badge (aus dem Manifest gelesen); jede Version hat ihren Eintrag in [CHANGELOG.md](CHANGELOG.md). Releases werden auf GitHub veröffentlicht.",
          "C'est du Python pur : rien à compiler (`pip install -e .`). La version se trouve dans `pyproject.toml`, dans `armor.project.json` et dans le badge du README (lu depuis le manifeste) ; chaque version a son entrée dans [CHANGELOG.md](CHANGELOG.md). Les versions sont publiées sur GitHub.",
          "È Python puro: nulla da compilare (`pip install -e .`). La versione risiede in `pyproject.toml`, in `armor.project.json` e nel badge del README (letto dal manifesto); ogni versione ha la sua voce in [CHANGELOG.md](CHANGELOG.md). Le versioni sono pubblicate su GitHub.",
          "純粋な Python なので、コンパイルするものはありません（`pip install -e .`）。バージョンは `pyproject.toml`、`armor.project.json`、README のバッジ（マニフェストから読み取り）にあり、各バージョンには [CHANGELOG.md](CHANGELOG.md) にエントリーがあります。リリースは GitHub で公開されます。",
          "这是纯 Python：无需编译（`pip install -e .`）。版本记录在 `pyproject.toml`、`armor.project.json` 和 README 徽章中（读取自清单）；每个版本在 [CHANGELOG.md](CHANGELOG.md) 中都有对应条目。发布版本发布在 GitHub 上。",
          "É Python puro: não há nada para compilar (`pip install -e .`). A versão está em `pyproject.toml`, em `armor.project.json` e no emblema do README (lido do manifesto); cada versão tem a sua entrada em [CHANGELOG.md](CHANGELOG.md). As versões são publicadas no GitHub.")

TROUBLE = [
    (T("An update says nothing happened | Una actualización dice que no pasó nada | Ein Update sagt, es sei nichts passiert | Une mise à jour dit qu'il ne s'est rien passé | Un aggiornamento dice che non è successo nulla | 更新が「何も起きなかった」と言う | 更新提示什么也没发生 | Uma atualização diz que nada aconteceu"), T("the project is already at the commit that GitHub has | el proyecto ya está en el commit que tiene GitHub | das Projekt ist bereits auf dem Commit, den GitHub hat | le projet est déjà au commit que GitHub a | il progetto è già al commit che ha GitHub | プロジェクトはすでに GitHub と同じコミット | 项目已处于 GitHub 上的提交 | o projeto já está no commit que o GitHub tem"), T("nothing to do | nada que hacer | nichts zu tun | rien à faire | niente da fare | 対処不要 | 无需处理 | nada a fazer")),
    (T("An update is refused because of local changes | Una actualización se rechaza por cambios locales | Ein Update wird wegen lokaler Änderungen abgelehnt | Une mise à jour est refusée à cause de modifications locales | Un aggiornamento è rifiutato per modifiche locali | ローカルの変更のため更新が拒否される | 因本地修改而拒绝更新 | Uma atualização é recusada por alterações locais"), T("the checkout has an edit that is not committed | el proyecto tiene un cambio sin commit | der Checkout hat eine nicht committete Änderung | le dépôt a une modification non validée | il checkout ha una modifica non committata | チェックアウトにコミットされていない変更がある | 副本有未提交的修改 | o checkout tem uma alteração sem commit"), T("commit or stash it, then update | haz commit o guárdalo aparte y actualiza | committen oder beiseitelegen, dann aktualisieren | validez-la ou mettez-la de côté, puis mettez à jour | fai commit o mettila da parte, poi aggiorna | コミットまたは退避してから更新 | 提交或暂存后再更新 | faça commit ou guarde à parte e atualize")),
    (T("It says a requirement is not installed | Dice que un requisito no está instalado | Es meldet, eine Voraussetzung sei nicht installiert | Il dit qu'un prérequis n'est pas installé | Dice che un requisito non è installato | 要件が未インストールと表示される | 提示某个前置要求未安装 | Diz que um requisito não está instalado"), T("the manifest lists it in `requires` | el manifiesto lo lista en `requires` | das Manifest führt es in `requires` auf | le manifeste le liste dans `requires` | il manifesto lo elenca in `requires` | マニフェストの `requires` に挙がっている | 清单在 `requires` 中列出了它 | o manifesto lista-o em `requires`"), T("install that project first (a batch already orders them) | instala antes ese proyecto (un lote ya los ordena) | dieses Projekt zuerst installieren (ein Stapel ordnet sie schon) | installez d'abord ce projet (un lot les ordonne déjà) | installa prima quel progetto (un lotto li ordina già) | そのプロジェクトを先にインストール（バッチは順序付け済み） | 先安装该项目（批量操作已排好顺序） | instale primeiro esse projeto (um lote já os ordena)")),
    (T("The window or the command line says the revision is not signed | La ventana o la línea de órdenes dice que la revisión no está firmada | Fenster oder Kommandozeile sagen, die Revision sei nicht signiert | La fenêtre ou la ligne de commande dit que la révision n'est pas signée | La finestra o la riga di comando dice che la revisione non è firmata | ウィンドウやコマンドラインが未署名のリビジョンだと表示する | 窗口或命令行提示该修订未签名 | A janela ou a linha de comandos diz que a revisão não está assinada"), T("`signature_policy` is `warn`, so it installs and says so | `signature_policy` es `warn`, así que instala y lo dice | `signature_policy` ist `warn`, also installiert es und sagt es | `signature_policy` vaut `warn`, donc il installe et le dit | `signature_policy` è `warn`, quindi installa e lo dice | `signature_policy` が `warn` なのでインストールして知らせる | `signature_policy` 为 `warn`，所以照常安装并提示 | `signature_policy` é `warn`, por isso instala e di-lo"), T("choose `require` in the settings to refuse unsigned revisions | elige `require` en los ajustes para rechazar revisiones sin firma | in den Einstellungen `require` wählen, um unsignierte Revisionen abzulehnen | choisissez `require` dans les réglages pour refuser les révisions non signées | scegli `require` nelle impostazioni per rifiutare le revisioni non firmate | 設定で `require` を選ぶと未署名のリビジョンを拒否 | 在设置中选择 `require` 以拒绝未签名的修订 | escolha `require` nas definições para recusar revisões sem assinatura")),
    (T("An update broke something | Una actualización estropeó algo | Ein Update hat etwas kaputt gemacht | Une mise à jour a cassé quelque chose | Un aggiornamento ha rotto qualcosa | 更新で何かが壊れた | 更新弄坏了东西 | Uma atualização estragou algo"), T("the new revision builds but does not behave | la nueva revisión compila pero no se comporta bien | die neue Revision baut, verhält sich aber falsch | la nouvelle révision se construit mais se comporte mal | la nuova revisione compila ma non si comporta bene | 新しいリビジョンはビルドできるが挙動が悪い | 新修订能构建但行为不对 | a nova revisão compila mas não se comporta"), T("`armor-updater --cli rollback <project>` puts the newest backup back | `armor-updater --cli rollback <proyecto>` devuelve la copia más nueva | `armor-updater --cli rollback <Projekt>` spielt die neueste Sicherung zurück | `armor-updater --cli rollback <projet>` remet la copie la plus récente | `armor-updater --cli rollback <progetto>` rimette la copia più recente | `armor-updater --cli rollback <プロジェクト>` で最新のバックアップを戻す | `armor-updater --cli rollback <项目>` 放回最新备份 | `armor-updater --cli rollback <projeto>` repõe a cópia mais recente")),
]

ROADMAP = P(
    "**Known limits today**\n\n* The Qt Quick window has only been run on Windows.\n* It has not been run against every repository of the family end to end.\n* The installs need `git` and the build tools of each repository.\n* No independent security review.\n\n**Next**\n\n* Run it end to end against every repository of the family and on Linux and macOS.",
    "**Límites conocidos hoy**\n\n* La ventana Qt Quick solo se ha ejecutado en Windows.\n* No se ha ejecutado contra todos los repositorios de la familia de punta a punta.\n* Las instalaciones necesitan `git` y las herramientas de construcción de cada repositorio.\n* Sin revisión de seguridad independiente.\n\n**Lo siguiente**\n\n* Ejecutarlo de punta a punta contra todos los repositorios de la familia y en Linux y macOS.",
    "**Bekannte Grenzen heute**\n\n* Das Qt-Quick-Fenster lief nur unter Windows.\n* Es lief nicht gegen jedes Repository der Familie von Anfang bis Ende.\n* Die Installationen brauchen `git` und die Build-Werkzeuge jedes Repositorys.\n* Keine unabhängige Sicherheitsprüfung.\n\n**Als Nächstes**\n\n* Es von Anfang bis Ende gegen jedes Repository der Familie und unter Linux und macOS ausführen.",
    "**Limites connues aujourd'hui**\n\n* La fenêtre Qt Quick n'a tourné que sous Windows.\n* Il n'a pas été exécuté contre tous les dépôts de la famille de bout en bout.\n* Les installations demandent `git` et les outils de construction de chaque dépôt.\n* Pas de revue de sécurité indépendante.\n\n**Prochainement**\n\n* L'exécuter de bout en bout contre tous les dépôts de la famille, et sous Linux et macOS.",
    "**Limiti noti oggi**\n\n* La finestra Qt Quick ha girato solo su Windows.\n* Non è stato eseguito contro tutti i repository della famiglia da cima a fondo.\n* Le installazioni richiedono `git` e gli strumenti di compilazione di ogni repository.\n* Nessuna revisione di sicurezza indipendente.\n\n**Prossimi passi**\n\n* Eseguirlo da cima a fondo contro tutti i repository della famiglia e su Linux e macOS.",
    "**現時点の既知の制限**\n\n* Qt Quick ウィンドウは Windows でのみ動作確認済みです。\n* ファミリーの全リポジトリで通しで動かしたことはありません。\n* インストールには `git` と各リポジトリのビルドツールが必要です。\n* 第三者によるセキュリティレビューはありません。\n\n**今後**\n\n* ファミリーの全リポジトリで通しで動かし、Linux と macOS でも試す。",
    "**当前已知限制**\n\n* Qt Quick 窗口只在 Windows 上运行过。\n* 尚未对家族的每个仓库端到端运行。\n* 安装需要 `git` 和每个仓库的构建工具。\n* 没有独立的安全审查。\n\n**下一步**\n\n* 对家族的每个仓库端到端运行，并在 Linux 和 macOS 上试用。",
    "**Limites conhecidos hoje**\n\n* A janela Qt Quick só correu no Windows.\n* Não foi executado contra todos os repositórios da família de ponta a ponta.\n* As instalações precisam de `git` e das ferramentas de compilação de cada repositório.\n* Sem revisão de segurança independente.\n\n**A seguir**\n\n* Executá-lo de ponta a ponta contra todos os repositórios da família e em Linux e macOS.")

DOCS = [
    P("[Command-line reference](docs/CLI_REFERENCE.md): every command and option", "[Referencia de la línea de órdenes](docs/CLI_REFERENCE.md): cada orden y opción", "[Kommandozeilen-Referenz](docs/CLI_REFERENCE.md): jeder Befehl und jede Option", "[Référence de la ligne de commande](docs/CLI_REFERENCE.md) : chaque commande et option", "[Riferimento della riga di comando](docs/CLI_REFERENCE.md): ogni comando e opzione", "[コマンドラインリファレンス](docs/CLI_REFERENCE.md)：全コマンドとオプション", "[命令行参考](docs/CLI_REFERENCE.md)：每个命令和选项", "[Referência da linha de comandos](docs/CLI_REFERENCE.md): cada comando e opção"),
    P("[The Qt Quick window](docs/QML_DESKTOP_GUI.md): how the desktop window works", "[La ventana Qt Quick](docs/QML_DESKTOP_GUI.md): cómo funciona la ventana de escritorio", "[Das Qt-Quick-Fenster](docs/QML_DESKTOP_GUI.md): wie das Desktop-Fenster funktioniert", "[La fenêtre Qt Quick](docs/QML_DESKTOP_GUI.md) : comment fonctionne la fenêtre de bureau", "[La finestra Qt Quick](docs/QML_DESKTOP_GUI.md): come funziona la finestra desktop", "[Qt Quick ウィンドウ](docs/QML_DESKTOP_GUI.md)：デスクトップウィンドウの仕組み", "[Qt Quick 窗口](docs/QML_DESKTOP_GUI.md)：桌面窗口的工作方式", "[A janela Qt Quick](docs/QML_DESKTOP_GUI.md): como funciona a janela de secretária"),
]


def build_lg(lg):
    bullets = "\n".join(f"* {b}" for b in L(lg, "bullets"))
    body = {
        "overview": bullets,
        "role": f"{L(lg, 'fit')}\n\n{table(lg, 'talks', ROLE_TABLE)}",
        "architecture": arch(lg, "ARMOR-UPDATER", "ARMOR-UPDATER architecture: the person, the workspace and GitHub, the modules of the updater and the live checkout and build it changes", None),
        "security": table(lg, "threat", SECURITY_ROWS) + "\n\n" + SEC_TAIL[lg],
        "interfaces": table(lg, "route", CLI) + "\n\n" + IFACE_NOTE[lg],
        "configuration": table(lg, "setting", CFG) + "\n\n" + CFG_NOTE[lg],
        "quickstart": f"{QUICK_LEAD[lg]}\n\n" + code(lg, QUICK_CODE, "bash") + "\n\n" + QUICK_AFTER[lg],
        "testing": code(lg, [("python -m pytest tests -q", T("288 tests, about six minutes | 288 pruebas, unos seis minutos | 288 Tests, etwa sechs Minuten | 288 tests, environ six minutes | 288 test, circa sei minuti | 288 件、約 6 分 | 288 项，约六分钟 | 288 testes, cerca de seis minutos")), "python -I tools/armor_ci_validate.py"]) + "\n\n" + table(lg, "area", TEST_TABLE) + "\n\n" + TEST_NOTE[lg],
        "build": BUILD[lg],
        "troubleshooting": table(lg, "trouble", TROUBLE),
        "structure": structure(lg, "ARMOR-UPDATER", tree=TREE[lg]),
        "roadmap": ROADMAP[lg],
    }
    return text_for(lg, tagline=L(lg, "tagline"), honest=L(lg, "honest"), glance=GLANCE, status=dict(LEGACY[lg]["status"]), docs=DOCS, contributing_first=CONTRIB, body=body)


TEXT = {lg: build_lg(lg) for lg in LGS}
