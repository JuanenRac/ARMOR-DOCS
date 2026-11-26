# The facts that do not depend on the language, and the words of every language, of ARMOR-NODE-SOLAR-HMI, in the universal README layout.
# Copyright (C) 2026 JuanenRac (Electro Hobby 3D). GPL-3.0-or-later.

from readme_src._kit import DOES, DOES_NOT, LIMITS, NEXT, REQ, P, arch, code, structure, table

REPO = "ARMOR-NODE-SOLAR-HMI"
TESTS = "{{fact:ctest_cpp:ARMOR-NODE-SOLAR-HMI}}"


def url(name):
    return f"[{name}](https://github.com/JuanenRac/{name})"


SERVER, NODE, HMI = url("ARMOR-SERVER"), url("ARMOR-NODE-SOLAR"), url("ARMOR-NODE-HMI")

FACTS = {
    "emoji": "🔋",
    "layout": "universal",
    "license_badge": "License-GPL%203.0--or--later-blue",
    "status": [["software", "orange"], ["tests", "yellow"], ["ui", "red"], ["hardware", "red"], ["security", "orange"], ["updates", "red"], ["integration", "red"], ["docs", "yellow"]],
    "badges": [["Language", "C%2B%2B17", "00599c"], ["Board", "ESP32--P4%207%20inch%20(planned)", "e7352c"], ["Tests", TESTS + "%20host%20programs", "2ea44f"]],
}

TAGLINE = P(
    "The energy screen of the house: a 7-inch touch screen that will show the battery stacks, their cells and the inverters as ARMOR-SERVER knows them",
    "La pantalla de energía de la casa: una pantalla táctil de 7 pulgadas que mostrará las baterías, sus celdas y los inversores tal como los conoce ARMOR-SERVER",
    "Der Energiebildschirm des Hauses: ein 7-Zoll-Touchscreen, der die Batteriestapel, ihre Zellen und die Wechselrichter so zeigen wird, wie ARMOR-SERVER sie kennt",
    "L'écran d'énergie de la maison : un écran tactile de 7 pouces qui montrera les batteries, leurs cellules et les onduleurs tels qu'ARMOR-SERVER les connaît",
    "Lo schermo dell'energia di casa: uno schermo touch da 7 pollici che mostrerà le batterie, le loro celle e gli inverter come li conosce ARMOR-SERVER",
    "家のエネルギー画面：バッテリースタック、セル、インバーターを ARMOR-SERVER が把握している通りに表示する予定の 7 インチタッチ画面",
    "家中的能源屏幕：一块 7 英寸触摸屏，将按照 ARMOR-SERVER 掌握的情况显示电池组、电芯和逆变器",
    "O ecrã de energia da casa: um ecrã tátil de 7 polegadas que mostrará as baterias, as suas células e os inversores tal como o ARMOR-SERVER os conhece",
)

HONEST = P(
    f"The logic behind the screen and a simulator of an installation are written and tested on a computer ({TESTS} host programs). **There is no firmware, no screen and no connection to a server yet; nothing here sends an order to a battery, and nothing has run on a board.**",
    f"La lógica de la pantalla y un simulador de una instalación están escritos y probados en un ordenador ({TESTS} programas de host). **Todavía no hay firmware, ni pantallas, ni conexión con un servidor; nada de aquí envía órdenes a una batería y nada ha corrido en una placa.**",
    f"Die Logik hinter dem Bildschirm und ein Simulator einer Anlage sind geschrieben und auf einem Computer getestet ({TESTS} Host-Programme). **Es gibt noch keine Firmware, keine Bildschirme und keine Verbindung zu einem Server; nichts hier sendet einen Befehl an eine Batterie, und nichts lief auf einer Platine.**",
    f"La logique de l'écran et un simulateur d'installation sont écrits et testés sur un ordinateur ({TESTS} programmes hôte). **Il n'y a pas encore de firmware, d'écrans ni de connexion à un serveur ; rien ici n'envoie d'ordre à une batterie et rien n'a tourné sur une carte.**",
    f"La logica dello schermo e un simulatore di impianto sono scritti e provati su un computer ({TESTS} programmi host). **Non ci sono ancora firmware, schermate né connessione a un server; nulla qui invia ordini a una batteria e nulla è girato su una scheda.**",
    f"画面を支えるロジックと設備のシミュレータは作成済みで、コンピュータ上でテストしています（ホストプログラム {TESTS} 本）。**ファームウェア、画面、サーバーへの接続はまだありません。ここからバッテリーへ命令を送るものはなく、基板上で動いたものもありません。**",
    f"屏幕背后的逻辑和一个设备模拟器已经编写完成，并在电脑上测试（{TESTS} 个主机程序）。**目前还没有固件、界面，也没有与服务器的连接；这里没有任何东西向电池发送指令，也没有任何内容在电路板上运行过。**",
    f"A lógica do ecrã e um simulador de uma instalação estão escritos e testados num computador ({TESTS} programas de host). **Ainda não há firmware, ecrãs nem ligação a um servidor; nada aqui envia ordens a uma bateria e nada correu numa placa.**",
)

GLANCE_LABELS = {
    "en": ["Role", "Stack", "Tests", "Board", "Runs on", "On real hardware", "License"],
    "es": ["Función", "Tecnología", "Pruebas", "Placa", "Funciona en", "En hardware real", "Licencia"],
    "de": ["Rolle", "Technik", "Tests", "Platine", "Läuft auf", "Auf echter Hardware", "Lizenz"],
    "fr": ["Rôle", "Technologie", "Tests", "Carte", "Fonctionne sur", "Sur matériel réel", "Licence"],
    "it": ["Ruolo", "Tecnologia", "Test", "Scheda", "Gira su", "Su hardware reale", "Licenza"],
    "ja": ["役割", "技術", "テスト", "基板", "動作環境", "実機で", "ライセンス"],
    "zh": ["角色", "技术栈", "测试", "电路板", "运行环境", "真实硬件上", "许可证"],
    "pt": ["Função", "Tecnologia", "Testes", "Placa", "Funciona em", "Em hardware real", "Licença"],
}

GLANCE_VALUES = {
    "en": ["Solar touch screen of A.R.M.O.R. (family: Clients, parent: ARMOR-SERVER)", "C++17 core and simulator, CMake; Python checks", f"{TESTS} host programs",
           "Guition JC1060P470C (ESP32-P4 with ESP32-C6, 7-inch 1024 x 600); not yet supported by code", "A computer with CMake, a C++17 compiler and Python 3.11+", "Nothing has run on the board", "GPL-3.0-or-later"],
    "es": ["Pantalla táctil solar de A.R.M.O.R. (familia: Clients, padre: ARMOR-SERVER)", "Núcleo y simulador en C++17, CMake; comprobaciones en Python", f"{TESTS} programas de host",
           "Guition JC1060P470C (ESP32-P4 con ESP32-C6, 7 pulgadas, 1024 x 600); aún sin código de placa", "Un ordenador con CMake, un compilador C++17 y Python 3.11+", "Nada ha corrido en la placa", "GPL-3.0-or-later"],
    "de": ["Solar-Touchscreen von A.R.M.O.R. (Familie: Clients, übergeordnet: ARMOR-SERVER)", "Kern und Simulator in C++17, CMake; Prüfungen in Python", f"{TESTS} Host-Programme",
           "Guition JC1060P470C (ESP32-P4 mit ESP32-C6, 7 Zoll, 1024 x 600); noch ohne Platinencode", "Ein Computer mit CMake, C++17-Compiler und Python 3.11+", "Nichts lief auf der Platine", "GPL-3.0-or-later"],
    "fr": ["Écran tactile solaire d'A.R.M.O.R. (famille : Clients, parent : ARMOR-SERVER)", "Cœur et simulateur en C++17, CMake ; contrôles en Python", f"{TESTS} programmes hôte",
           "Guition JC1060P470C (ESP32-P4 avec ESP32-C6, 7 pouces, 1024 x 600) ; pas encore de code carte", "Un ordinateur avec CMake, un compilateur C++17 et Python 3.11+", "Rien n'a tourné sur la carte", "GPL-3.0-or-later"],
    "it": ["Schermo touch solare di A.R.M.O.R. (famiglia: Clients, genitore: ARMOR-SERVER)", "Nucleo e simulatore in C++17, CMake; controlli in Python", f"{TESTS} programmi host",
           "Guition JC1060P470C (ESP32-P4 con ESP32-C6, 7 pollici, 1024 x 600); ancora senza codice di scheda", "Un computer con CMake, un compilatore C++17 e Python 3.11+", "Nulla è girato sulla scheda", "GPL-3.0-or-later"],
    "ja": ["A.R.M.O.R. の太陽光タッチ画面（ファミリー：Clients、親：ARMOR-SERVER）", "C++17 のコアとシミュレータ、CMake、Python の検査", f"ホストプログラム {TESTS} 本",
           "Guition JC1060P470C（ESP32-P4 と ESP32-C6、7 インチ 1024 x 600）。基板用コードは未作成", "CMake、C++17 コンパイラ、Python 3.11+ を備えた PC", "基板上では何も動いていません", "GPL-3.0-or-later"],
    "zh": ["A.R.M.O.R. 的太阳能触摸屏（家族：Clients，上级：ARMOR-SERVER）", "C++17 核心与模拟器、CMake；Python 检查", f"{TESTS} 个主机程序",
           "Guition JC1060P470C（ESP32-P4 搭配 ESP32-C6，7 英寸 1024 x 600）；尚无板级代码", "装有 CMake、C++17 编译器和 Python 3.11+ 的电脑", "电路板上尚未运行任何内容", "GPL-3.0-or-later"],
    "pt": ["Ecrã tátil solar do A.R.M.O.R. (família: Clients, principal: ARMOR-SERVER)", "Núcleo e simulador em C++17, CMake; verificações em Python", f"{TESTS} programas de host",
           "Guition JC1060P470C (ESP32-P4 com ESP32-C6, 7 polegadas, 1024 x 600); ainda sem código de placa", "Um computador com CMake, um compilador C++17 e Python 3.11+", "Nada correu na placa", "GPL-3.0-or-later"],
}

STATUS = {
    "software": P("The core that reads, judges and guards is written; the firmware is not.", "El núcleo que lee, juzga y protege está escrito; el firmware no.", "Der Kern zum Lesen, Bewerten und Schützen ist geschrieben, die Firmware nicht.", "Le cœur qui lit, juge et protège est écrit ; pas le firmware.", "Il nucleo che legge, giudica e protegge è scritto; il firmware no.", "読み取り・判定・保護のコアは作成済み。ファームウェアは未作成。", "负责读取、判断和保护的核心已编写；固件尚未编写。", "O núcleo que lê, avalia e protege está escrito; o firmware não."),
    "tests": P("Host programs and two checks against ARMOR-COMMON; early stage.", "Programas de host y dos comprobaciones contra ARMOR-COMMON; fase inicial.", "Host-Programme und zwei Prüfungen gegen ARMOR-COMMON; frühes Stadium.", "Programmes hôte et deux contrôles avec ARMOR-COMMON ; stade précoce.", "Programmi host e due controlli con ARMOR-COMMON; fase iniziale.", "ホストプログラムと ARMOR-COMMON に対する 2 つの検査。初期段階。", "主机程序以及两项对照 ARMOR-COMMON 的检查；处于早期阶段。", "Programas de host e duas verificações face ao ARMOR-COMMON; fase inicial."),
    "ui": P("No screen is drawn yet.", "Todavía no se dibuja ninguna pantalla.", "Noch wird kein Bildschirm gezeichnet.", "Aucun écran n'est encore dessiné.", "Nessuna schermata è ancora disegnata.", "画面はまだ描画されません。", "尚未绘制任何界面。", "Ainda não se desenha nenhum ecrã."),
    "hardware": P("The board has no code and nothing has run on it.", "La placa no tiene código y nada ha corrido en ella.", "Für die Platine gibt es keinen Code, nichts lief darauf.", "La carte n'a pas de code et rien n'y a tourné.", "La scheda non ha codice e nulla vi è girato.", "基板用のコードはなく、何も動いていません。", "电路板没有代码，也没有运行过任何内容。", "A placa não tem código e nada correu nela."),
    "security": P("PIN and write checks are tested logic only; no independent review.", "El PIN y la compuerta de escritura son solo lógica probada; sin revisión independiente.", "PIN und Schreibprüfung sind nur getestete Logik; keine unabhängige Prüfung.", "PIN et contrôle d'écriture ne sont que de la logique testée ; aucune revue indépendante.", "PIN e controllo di scrittura sono solo logica provata; nessuna revisione indipendente.", "PIN と書き込み判定はテスト済みロジックのみ。第三者レビューなし。", "PIN 与写入检查仅是经过测试的逻辑；没有独立审查。", "O PIN e a verificação de escrita são apenas lógica testada; sem revisão independente."),
    "updates": P("There is nothing to update yet.", "Todavía no hay nada que actualizar.", "Es gibt noch nichts zu aktualisieren.", "Il n'y a encore rien à mettre à jour.", "Non c'è ancora nulla da aggiornare.", "更新する対象はまだありません。", "尚无可更新的内容。", "Ainda não há nada para atualizar."),
    "integration": P("No link to ARMOR-SERVER yet; the compact solar route it needs does not exist.", "Aún sin enlace con ARMOR-SERVER; la ruta solar compacta que necesita no existe.", "Noch keine Verbindung zu ARMOR-SERVER; die nötige kompakte Solar-Route fehlt.", "Pas encore de lien avec ARMOR-SERVER ; la route solaire compacte nécessaire n'existe pas.", "Nessun collegamento con ARMOR-SERVER; la rotta solare compatta necessaria non esiste.", "ARMOR-SERVER との接続は未実装。必要な簡潔な太陽光ルートもありません。", "尚未连接 ARMOR-SERVER；所需的精简太阳能接口还不存在。", "Ainda sem ligação ao ARMOR-SERVER; a rota solar compacta necessária não existe."),
    "docs": P("README in eight languages and the design note.", "README en ocho idiomas y la nota de diseño.", "README in acht Sprachen und die Entwurfsnotiz.", "README en huit langues et la note de conception.", "README in otto lingue e la nota di progetto.", "8 言語の README と設計メモ。", "八种语言的 README 和设计说明。", "README em oito línguas e a nota de conceção."),
}

OVERVIEW = P(
    ["Shows the energy side of an installation: totals, battery stacks, cells and inverters.", "Reads everything from the server over the network; it has no serial or battery cable.", "Becomes read-only, and says so, when the data is old."],
    ["Muestra la parte de energía de una instalación: totales, baterías, celdas e inversores.", "Lo lee todo del servidor por la red; no tiene cable serie ni de batería.", "Pasa a solo lectura, y lo dice, cuando los datos son antiguos."],
    ["Zeigt die Energieseite einer Anlage: Summen, Batteriestapel, Zellen und Wechselrichter.", "Liest alles über das Netz vom Server; kein serielles Kabel und keines zur Batterie.", "Wird bei alten Daten nur lesend und sagt das auch."],
    ["Montre le côté énergie d'une installation : totaux, batteries, cellules et onduleurs.", "Lit tout depuis le serveur par le réseau ; aucun câble série ni batterie.", "Passe en lecture seule, et le dit, quand les données sont anciennes."],
    ["Mostra la parte energetica di un impianto: totali, batterie, celle e inverter.", "Legge tutto dal server via rete; non ha cavi seriali né verso la batteria.", "Diventa di sola lettura, e lo dice, quando i dati sono vecchi."],
    ["設備のエネルギー面（合計、バッテリースタック、セル、インバーター）を表示します。", "すべてネットワーク経由でサーバーから読み取り、シリアルやバッテリーへの配線はありません。", "データが古いときは読み取り専用になり、そのことを表示します。"],
    ["显示设备的能源部分：总量、电池组、电芯和逆变器。", "全部通过网络从服务器读取；没有串口线或电池线。", "数据过旧时变为只读，并明确提示。"],
    ["Mostra a parte de energia de uma instalação: totais, baterias, células e inversores.", "Lê tudo do servidor pela rede; não tem cabo série nem de bateria.", "Passa a só de leitura, e di-lo, quando os dados são antigos."],
)

ROLE = P(
    f"{NODE} reads the equipment, {SERVER} keeps what it says and decides every order, and this screen shows it. {HMI} is the panel of the whole system; this one is only about energy.",
    f"{NODE} lee los equipos, {SERVER} guarda lo que dicen y decide cada orden, y esta pantalla lo muestra. {HMI} es el panel de todo el sistema; este es solo de energía.",
    f"{NODE} liest die Geräte, {SERVER} hält fest, was sie melden, und entscheidet jeden Befehl; dieser Bildschirm zeigt es. {HMI} ist das Panel des ganzen Systems; dieses hier betrifft nur die Energie.",
    f"{NODE} lit les équipements, {SERVER} garde ce qu'ils disent et décide de chaque ordre, et cet écran l'affiche. {HMI} est le panneau de tout le système ; celui-ci ne concerne que l'énergie.",
    f"{NODE} legge gli apparecchi, {SERVER} conserva ciò che dicono e decide ogni ordine, e questo schermo lo mostra. {HMI} è il pannello di tutto il sistema; questo riguarda solo l'energia.",
    f"{NODE} が機器を読み取り、{SERVER} がその内容を保持してすべての命令を判断し、この画面が表示します。{HMI} はシステム全体のパネルで、こちらはエネルギー専用です。",
    f"{NODE} 读取设备，{SERVER} 保存其数据并决定每一条指令，本屏幕负责显示。{HMI} 是整个系统的面板；本屏幕只关注能源。",
    f"O {NODE} lê os equipamentos, o {SERVER} guarda o que eles dizem e decide cada ordem, e este ecrã mostra-o. O {HMI} é o painel de todo o sistema; este é só de energia.",
)

FEATURES = P(
    ["A value that is missing or impossible is not shown, never as a zero.", "Cells, modules and stacks have a level with an icon and a word; only an alarm blinks, at most twice a second.", "A PIN kept as a salted hash, with growing locks and a short session.", "A battery operation is offered only when the server allows it, the data is fresh, the PIN is open and the person confirmed.", "A simulator with five scenarios, checked against the message schemas."],
    ["Un valor que falta o es imposible no se muestra, nunca como cero.", "Celdas, módulos y baterías tienen un nivel con icono y palabra; solo parpadea una alarma, como mucho dos veces por segundo.", "PIN guardado como hash con sal, con bloqueos crecientes y sesión corta.", "Una operación de batería solo se ofrece si el servidor lo permite, los datos son recientes, el PIN está abierto y la persona ha confirmado.", "Simulador con cinco escenarios, comprobado contra los esquemas de los mensajes."],
    ["Ein fehlender oder unmöglicher Wert wird nicht angezeigt, nie als Null.", "Zellen, Module und Stapel haben eine Stufe mit Symbol und Wort; nur ein Alarm blinkt, höchstens zweimal pro Sekunde.", "PIN als gesalzener Hash, mit wachsenden Sperren und kurzer Sitzung.", "Eine Batterieaktion wird nur angeboten, wenn der Server es erlaubt, die Daten frisch sind, die PIN offen ist und die Person bestätigt hat.", "Simulator mit fünf Szenarien, gegen die Nachrichtenschemas geprüft."],
    ["Une valeur absente ou impossible n'est pas affichée, jamais comme un zéro.", "Cellules, modules et batteries ont un niveau avec icône et mot ; seule une alarme clignote, deux fois par seconde au plus.", "PIN conservé sous forme de hachage salé, avec blocages croissants et session courte.", "Une opération batterie n'est proposée que si le serveur l'autorise, les données sont récentes, le PIN est ouvert et la personne a confirmé.", "Simulateur à cinq scénarios, vérifié contre les schémas des messages."],
    ["Un valore mancante o impossibile non viene mostrato, mai come zero.", "Celle, moduli e batterie hanno un livello con icona e parola; lampeggia solo un allarme, al massimo due volte al secondo.", "PIN conservato come hash con sale, con blocchi crescenti e sessione breve.", "Un'operazione sulla batteria è proposta solo se il server la consente, i dati sono recenti, il PIN è aperto e la persona ha confermato.", "Simulatore con cinque scenari, verificato con gli schemi dei messaggi."],
    ["欠けている値やあり得ない値は表示せず、ゼロにもしません。", "セル、モジュール、スタックにはアイコンと言葉付きのレベルがあり、点滅するのは警報のみで毎秒 2 回までです。", "PIN はソルト付きハッシュで保存し、ロックは次第に長くなり、セッションは短時間です。", "バッテリー操作は、サーバーが許可し、データが新しく、PIN が開かれ、本人が確認した場合のみ提示します。", "5 つのシナリオを持つシミュレータ。メッセージスキーマと照合します。"],
    ["缺失或不可能的数值不显示，也绝不显示为零。", "电芯、模块和电池组的级别带有图标和文字；只有警报闪烁，每秒最多两次。", "PIN 以加盐哈希保存，锁定时间递增，会话很短。", "仅当服务器允许、数据新鲜、PIN 已解锁且本人确认时，才提供电池操作。", "包含五个场景的模拟器，并对照消息模式进行检查。"],
    ["Um valor em falta ou impossível não é mostrado, nunca como zero.", "Células, módulos e baterias têm um nível com ícone e palavra; só um alarme pisca, no máximo duas vezes por segundo.", "PIN guardado como hash com sal, com bloqueios crescentes e sessão curta.", "Uma operação na bateria só é proposta se o servidor permitir, os dados forem recentes, o PIN estiver aberto e a pessoa tiver confirmado.", "Simulador com cinco cenários, verificado face aos esquemas das mensagens."],
)

SECURITY = {
    "en": [["Somebody guesses the PIN", "Growing locks that survive a restart; a short session that ends without touches"], ["Old data is acted on", "Without a fresh answer the screen only reads and offers no operation"], ["The flash is read", "A short PIN does not resist this: the board will have to encrypt its flash; the server still decides every order"]],
    "es": [["Alguien adivina el PIN", "Bloqueos crecientes que sobreviven a un reinicio; sesión corta que acaba sin toques"], ["Se actúa con datos antiguos", "Sin respuesta reciente la pantalla solo lee y no ofrece operaciones"], ["Alguien lee la flash", "Un PIN corto no resiste eso: la placa tendrá que cifrar su flash; el servidor sigue decidiendo cada orden"]],
    "de": [["Jemand errät die PIN", "Wachsende Sperren, die einen Neustart überdauern; kurze Sitzung, die ohne Berührung endet"], ["Handeln nach alten Daten", "Ohne frische Antwort liest der Bildschirm nur und bietet keine Aktion an"], ["Der Flash wird ausgelesen", "Eine kurze PIN hält dem nicht stand: Die Platine muss ihren Flash verschlüsseln; der Server entscheidet weiterhin jeden Befehl"]],
    "fr": [["Quelqu'un devine le PIN", "Blocages croissants qui survivent à un redémarrage ; session courte qui s'arrête sans contact"], ["Agir sur des données anciennes", "Sans réponse récente, l'écran ne fait que lire et ne propose rien"], ["La flash est lue", "Un PIN court n'y résiste pas : la carte devra chiffrer sa flash ; le serveur décide toujours de chaque ordre"]],
    "it": [["Qualcuno indovina il PIN", "Blocchi crescenti che sopravvivono a un riavvio; sessione breve che termina senza tocchi"], ["Si agisce su dati vecchi", "Senza una risposta recente lo schermo legge soltanto e non propone operazioni"], ["La flash viene letta", "Un PIN corto non resiste: la scheda dovrà cifrare la flash; il server decide comunque ogni ordine"]],
    "ja": [["PIN を推測される", "再起動後も続く段階的なロックと、操作がないと終わる短いセッション"], ["古いデータで操作する", "新しい応答がなければ画面は読み取り専用で、操作を提示しません"], ["フラッシュを読み出される", "短い PIN では防げません。基板のフラッシュ暗号化が必要で、命令の判断は常にサーバーが行います"]],
    "zh": [["有人猜测 PIN", "锁定时间递增且重启后仍有效；会话很短，无触摸即结束"], ["依据过旧数据操作", "没有最新应答时屏幕只读，不提供任何操作"], ["闪存被读取", "短 PIN 无法抵御：电路板需要加密闪存；每条指令仍由服务器决定"]],
    "pt": [["Alguém adivinha o PIN", "Bloqueios crescentes que sobrevivem a um reinício; sessão curta que acaba sem toques"], ["Agir sobre dados antigos", "Sem uma resposta recente o ecrã só lê e não propõe operações"], ["A flash é lida", "Um PIN curto não resiste: a placa terá de cifrar a flash; o servidor continua a decidir cada ordem"]],
}

CMD = P(
    "the host tests (needs CMake and a C++17 compiler)", "las pruebas de host (necesita CMake y un compilador C++17)", "die Host-Tests (braucht CMake und einen C++17-Compiler)", "les tests hôte (CMake et un compilateur C++17)",
    "i test host (servono CMake e un compilatore C++17)", "ホストテスト（CMake と C++17 コンパイラが必要）", "主机测试（需要 CMake 和 C++17 编译器）", "os testes de host (precisa de CMake e de um compilador C++17)",
)
SIM = P("one answer of the simulator", "una respuesta del simulador", "eine Antwort des Simulators", "une réponse du simulateur", "una risposta del simulatore", "シミュレータの応答を 1 件", "模拟器的一条应答", "uma resposta do simulador")
REQS = P("CMake 3.16+, a C++17 compiler and Python 3.11+.", "CMake 3.16+, un compilador C++17 y Python 3.11+.", "CMake 3.16+, ein C++17-Compiler und Python 3.11+.", "CMake 3.16+, un compilateur C++17 et Python 3.11+.",
         "CMake 3.16+, un compilatore C++17 e Python 3.11+.", "CMake 3.16 以降、C++17 コンパイラ、Python 3.11 以降。", "CMake 3.16+、C++17 编译器和 Python 3.11+。", "CMake 3.16+, um compilador C++17 e Python 3.11+.")

TEST_ROWS = [
    ["`test_solar_data.cpp`", P("what is read and what is left out", "qué se lee y qué se descarta", "was gelesen und was weggelassen wird", "ce qui est lu et ce qui est écarté", "cosa si legge e cosa si scarta", "読む値と除外する値", "读取与忽略的内容", "o que se lê e o que se descarta")],
    ["`test_solar_view.cpp`", P("old data, levels, blinking", "datos antiguos, niveles, parpadeo", "alte Daten, Stufen, Blinken", "données anciennes, niveaux, clignotement", "dati vecchi, livelli, lampeggio", "古いデータ、レベル、点滅", "旧数据、级别、闪烁", "dados antigos, níveis, intermitência")],
    ["`test_pin_gate.cpp`", P("PIN hash, locks, session", "hash del PIN, bloqueos, sesión", "PIN-Hash, Sperren, Sitzung", "hachage du PIN, blocages, session", "hash del PIN, blocchi, sessione", "PIN のハッシュ、ロック、セッション", "PIN 哈希、锁定、会话", "hash do PIN, bloqueios, sessão")],
    ["`test_write_gate.cpp`", P("every reason that stops an operation", "cada motivo que impide una operación", "jeder Grund, der eine Aktion verhindert", "chaque raison qui bloque une opération", "ogni motivo che blocca un'operazione", "操作を止めるすべての理由", "阻止操作的每一种原因", "cada motivo que impede uma operação")],
    ["`test_plant.cpp`", P("the five scenarios", "los cinco escenarios", "die fünf Szenarien", "les cinq scénarios", "i cinque scenari", "5 つのシナリオ", "五个场景", "os cinco cenários")],
    ["`check_simulator.py`", P("the simulator follows the schemas", "el simulador cumple los esquemas", "der Simulator folgt den Schemas", "le simulateur respecte les schémas", "il simulatore rispetta gli schemi", "シミュレータがスキーマに従う", "模拟器符合模式", "o simulador cumpre os esquemas")],
    ["`check_base_copies.py`", P("shared files match their source", "los ficheros compartidos coinciden con su origen", "gemeinsame Dateien entsprechen der Quelle", "les fichiers partagés correspondent à leur source", "i file condivisi coincidono con l'origine", "共有ファイルが元と一致", "共享文件与来源一致", "os ficheiros partilhados coincidem com a origem")],
]
TEST_HEAD = P(["File", "What it covers"], ["Fichero", "Qué cubre"], ["Datei", "Was sie abdeckt"], ["Fichier", "Ce qu'il couvre"], ["File", "Cosa copre"], ["ファイル", "対象"], ["文件", "覆盖内容"], ["Ficheiro", "O que cobre"])

BUILD = P(
    "There is no firmware to build and no release yet. When there is, it will be built in GitHub Actions only.",
    "Todavía no hay firmware que compilar ni release. Cuando lo haya, se compilará solo en GitHub Actions.",
    "Es gibt noch keine Firmware und kein Release. Sobald es sie gibt, wird sie nur in GitHub Actions gebaut.",
    "Il n'y a pas encore de firmware ni de version publiée. Quand il y en aura, il sera compilé uniquement dans GitHub Actions.",
    "Non ci sono ancora firmware né release. Quando ci saranno, si compileranno solo in GitHub Actions.",
    "ビルドするファームウェアもリリースもまだありません。用意できたら GitHub Actions のみでビルドします。",
    "目前还没有可编译的固件，也没有发布版本。将来只在 GitHub Actions 中编译。",
    "Ainda não há firmware para compilar nem release. Quando houver, será compilado apenas no GitHub Actions.",
)

DOES_TEXT = P(
    "Reads the server's solar answer, judges what it says and guards the PIN, on a computer.",
    "Lee la respuesta solar del servidor, juzga lo que dice y protege el PIN, en un ordenador.",
    "Liest die Solar-Antwort des Servers, bewertet sie und schützt die PIN, auf einem Computer.",
    "Lit la réponse solaire du serveur, la juge et protège le PIN, sur un ordinateur.",
    "Legge la risposta solare del server, la valuta e protegge il PIN, su un computer.",
    "サーバーの太陽光応答を読み取り、判定し、PIN を守ります（コンピュータ上）。",
    "在电脑上读取服务器的太阳能应答、进行判断并保护 PIN。",
    "Lê a resposta solar do servidor, avalia o que diz e protege o PIN, num computador.",
)
DOES_NOT_TEXT = P(
    "Draw a screen, connect to anything, send an order or run on the board.",
    "Dibujar una pantalla, conectarse a nada, enviar una orden ni correr en la placa.",
    "Einen Bildschirm zeichnen, sich verbinden, Befehle senden oder auf der Platine laufen.",
    "Dessiner un écran, se connecter, envoyer un ordre ou tourner sur la carte.",
    "Disegnare schermate, collegarsi, inviare ordini o girare sulla scheda.",
    "画面の描画、接続、命令の送信、基板上での動作。",
    "绘制界面、建立连接、发送指令或在电路板上运行。",
    "Desenhar ecrãs, ligar-se a nada, enviar ordens ou correr na placa.",
)
NEXT_ITEMS = P(
    ["A compact solar answer in ARMOR-SERVER for small screens, defined first in ARMOR-COMMON.", "The screens at 1024 x 600 drawn by a simulator on a computer, in eight languages.", "The board layer shared with ARMOR-NODE-HMI.", "The first power-up on the board."],
    ["Una respuesta solar compacta en ARMOR-SERVER para pantallas pequeñas, definida antes en ARMOR-COMMON.", "Las pantallas a 1024 x 600 dibujadas por un simulador en el ordenador, en ocho idiomas.", "La capa de placa compartida con ARMOR-NODE-HMI.", "El primer encendido en la placa."],
    ["Eine kompakte Solar-Antwort in ARMOR-SERVER für kleine Bildschirme, zuerst in ARMOR-COMMON festgelegt.", "Die Bildschirme in 1024 x 600, von einem Simulator am Computer gezeichnet, in acht Sprachen.", "Die mit ARMOR-NODE-HMI gemeinsame Platinenschicht.", "Das erste Einschalten auf der Platine."],
    ["Une réponse solaire compacte dans ARMOR-SERVER pour petits écrans, définie d'abord dans ARMOR-COMMON.", "Les écrans en 1024 x 600 dessinés par un simulateur sur ordinateur, en huit langues.", "La couche carte partagée avec ARMOR-NODE-HMI.", "La première mise sous tension de la carte."],
    ["Una risposta solare compatta in ARMOR-SERVER per piccoli schermi, definita prima in ARMOR-COMMON.", "Le schermate a 1024 x 600 disegnate da un simulatore su computer, in otto lingue.", "Lo strato di scheda condiviso con ARMOR-NODE-HMI.", "La prima accensione sulla scheda."],
    ["小型画面向けの簡潔な太陽光応答を ARMOR-SERVER に追加（先に ARMOR-COMMON で定義）。", "1024 x 600 の画面をコンピュータ上のシミュレータで 8 言語描画。", "ARMOR-NODE-HMI と共有する基板レイヤー。", "基板での初回起動。"],
    ["在 ARMOR-SERVER 中为小屏幕提供精简的太阳能应答，先在 ARMOR-COMMON 中定义。", "用电脑上的模拟器以八种语言绘制 1024 x 600 界面。", "与 ARMOR-NODE-HMI 共享的板级层。", "在电路板上首次上电。"],
    ["Uma resposta solar compacta no ARMOR-SERVER para ecrãs pequenos, definida primeiro no ARMOR-COMMON.", "Os ecrãs a 1024 x 600 desenhados por um simulador no computador, em oito línguas.", "A camada de placa partilhada com o ARMOR-NODE-HMI.", "O primeiro arranque na placa."],
)

ALT = P(
    "ARMOR-NODE-SOLAR-HMI architecture: the simulator, the tested core and the server",
    "Arquitectura de ARMOR-NODE-SOLAR-HMI: el simulador, el núcleo probado y el servidor",
    "Architektur von ARMOR-NODE-SOLAR-HMI: Simulator, getesteter Kern und Server",
    "Architecture d'ARMOR-NODE-SOLAR-HMI : le simulateur, le cœur testé et le serveur",
    "Architettura di ARMOR-NODE-SOLAR-HMI: il simulatore, il nucleo provato e il server",
    "ARMOR-NODE-SOLAR-HMI の構成：シミュレータ、テスト済みコア、サーバー",
    "ARMOR-NODE-SOLAR-HMI 架构：模拟器、经过测试的核心和服务器",
    "Arquitetura do ARMOR-NODE-SOLAR-HMI: o simulador, o núcleo testado e o servidor",
)
DESIGN = P("[Design](docs/DESIGN.md): the rules and the plan", "[Diseño](docs/DESIGN.md): las reglas y el plan", "[Entwurf](docs/DESIGN.md): Regeln und Plan", "[Conception](docs/DESIGN.md) : les règles et le plan",
           "[Progetto](docs/DESIGN.md): le regole e il piano", "[設計](docs/DESIGN.md)：ルールと計画", "[设计](docs/DESIGN.md)：规则与计划", "[Conceção](docs/DESIGN.md): as regras e o plano")
FIRST = P(
    "Before a pull request run `python tools/armor_project_tool.py build-test .` and `python -I tools/armor_ci_validate.py`: both must pass. See [CONTRIBUTING.md](CONTRIBUTING.md) and the [code of conduct](CODE_OF_CONDUCT.md).",
    "Antes de un pull request ejecuta `python tools/armor_project_tool.py build-test .` y `python -I tools/armor_ci_validate.py`: ambos deben pasar. Consulta [CONTRIBUTING.md](CONTRIBUTING.md) y el [código de conducta](CODE_OF_CONDUCT.md).",
    "Führe vor einem Pull Request `python tools/armor_project_tool.py build-test .` und `python -I tools/armor_ci_validate.py` aus: Beides muss bestehen. Siehe [CONTRIBUTING.md](CONTRIBUTING.md) und den [Verhaltenskodex](CODE_OF_CONDUCT.md).",
    "Avant une pull request, lancez `python tools/armor_project_tool.py build-test .` et `python -I tools/armor_ci_validate.py` : les deux doivent réussir. Voir [CONTRIBUTING.md](CONTRIBUTING.md) et le [code de conduite](CODE_OF_CONDUCT.md).",
    "Prima di una pull request esegui `python tools/armor_project_tool.py build-test .` e `python -I tools/armor_ci_validate.py`: devono passare entrambi. Vedi [CONTRIBUTING.md](CONTRIBUTING.md) e il [codice di condotta](CODE_OF_CONDUCT.md).",
    "プルリクエストの前に `python tools/armor_project_tool.py build-test .` と `python -I tools/armor_ci_validate.py` を実行してください。両方の成功が必要です。[CONTRIBUTING.md](CONTRIBUTING.md) と[行動規範](CODE_OF_CONDUCT.md)を参照してください。",
    "提交拉取请求前请运行 `python tools/armor_project_tool.py build-test .` 和 `python -I tools/armor_ci_validate.py`：两者都必须通过。参见 [CONTRIBUTING.md](CONTRIBUTING.md) 和[行为准则](CODE_OF_CONDUCT.md)。",
    "Antes de um pull request execute `python tools/armor_project_tool.py build-test .` e `python -I tools/armor_ci_validate.py`: ambos têm de passar. Consulte [CONTRIBUTING.md](CONTRIBUTING.md) e o [código de conduta](CODE_OF_CONDUCT.md).",
)


def bullets(items):
    return "\n".join(f"* {item}" for item in items)


def words(lg):
    run = code(lg, [("python tools/armor_project_tool.py build-test .", CMD), ("build/host/solar_sim cell-high", SIM)])
    return {
        "tagline": TAGLINE[lg],
        "honest": HONEST[lg],
        "glance": [list(row) for row in zip(GLANCE_LABELS[lg], GLANCE_VALUES[lg], strict=True)],
        "status": {area: note[lg] for area, note in STATUS.items()},
        "docs": [DESIGN[lg]],
        "contributing_first": FIRST[lg],
        "languages_extra": "",
        "body": {
            "overview": bullets(OVERVIEW[lg]),
            "role": ROLE[lg],
            "architecture": arch(lg, REPO, ALT[lg]),
            "features": bullets(FEATURES[lg]),
            "security": table(lg, "threat", SECURITY[lg]),
            "quickstart": f"{REQ[lg]} {REQS[lg]}\n\n{run}",
            "testing": code(lg, ["python tools/armor_project_tool.py build-test .", "python -I tools/armor_ci_validate.py"]) + "\n\n" + table(lg, TEST_HEAD[lg], TEST_ROWS),
            "build": BUILD[lg],
            "structure": structure(lg, REPO),
            "roadmap": f"{LIMITS[lg]}\n\n* {DOES[lg]}: {DOES_TEXT[lg]}\n* {DOES_NOT[lg]}: {DOES_NOT_TEXT[lg]}\n\n{NEXT[lg]}\n\n{bullets(NEXT_ITEMS[lg])}",
        },
    }


TEXT = {lg: words(lg) for lg in ("en", "es", "de", "fr", "it", "ja", "zh", "pt")}
