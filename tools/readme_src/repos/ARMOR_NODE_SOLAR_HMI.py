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
    "status": [["software", "orange"], ["tests", "yellow"], ["ui", "orange"], ["hardware", "red"], ["security", "orange"], ["updates", "red"], ["integration", "red"], ["docs", "yellow"]],
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
    f"The logic behind the screen, a simulator of an installation and the screens are written and tested on a computer ({TESTS} host programs), and a firmware for the board compiles, with the sign-in, the reading of the server, the settings kept in flash, Wi-Fi and signed updates all off until somebody turns them on. **It has never run on a board and nothing here sends an order to a battery.**",
    f"La lógica de la pantalla, un simulador de una instalación y las pantallas están escritos y probados en un ordenador ({TESTS} programas de host), y hay un firmware para la placa que compila, con el inicio de sesión, la lectura del servidor, los ajustes en flash, la Wi-Fi y las actualizaciones firmadas, todo apagado hasta que alguien lo encienda. **Nunca ha corrido en una placa y nada de aquí envía órdenes a una batería.**",
    f"Die Logik, ein Anlagensimulator und die Bildschirme sind geschrieben und auf einem Computer getestet ({TESTS} Host-Programme), und eine Firmware für die Platine wird übersetzt, mit Anmeldung, Lesen des Servers, Einstellungen im Flash, WLAN und signierten Updates, alles aus, bis jemand es einschaltet. **Sie lief noch nie auf einer Platine und nichts hier sendet einen Befehl an eine Batterie.**",
    f"La logique de l'écran, un simulateur d'installation et les écrans sont écrits et testés sur un ordinateur ({TESTS} programmes hôte), et un firmware pour la carte se compile, avec la connexion, la lecture du serveur, les réglages en flash, le Wi-Fi et les mises à jour signées, tout désactivé tant que personne ne l'active. **Il n'a jamais tourné sur une carte et rien ici n'envoie d'ordre à une batterie.**",
    f"La logica dello schermo, un simulatore di impianto e le schermate sono scritti e provati su un computer ({TESTS} programmi host), e un firmware per la scheda si compila, con accesso, lettura del server, impostazioni in flash, Wi-Fi e aggiornamenti firmati, tutto spento finché qualcuno non lo accende. **Non è mai girato su una scheda e nulla qui invia ordini a una batteria.**",
    f"画面のロジック、設備シミュレータ、画面表示は作成済みでコンピュータ上でテストしており（ホストプログラム {TESTS} 本）、基板向けファームウェアはビルドできます。サインイン、サーバーの読み取り、フラッシュへの設定保存、Wi-Fi、署名付き更新を備えますが、有効にするまではすべて無効です。**基板上で動かしたことはなく、ここからバッテリーへ命令を送るものはありません。**",
    f"屏幕逻辑、设备模拟器和界面已编写并在电脑上测试（{TESTS} 个主机程序），面向电路板的固件可以编译，包含登录、读取服务器、闪存中的设置、Wi-Fi 和签名更新，全部默认关闭。**它从未在电路板上运行过，这里没有任何东西向电池发送指令。**",
    f"A lógica do ecrã, um simulador de uma instalação e os ecrãs estão escritos e testados num computador ({TESTS} programas de host), e há um firmware para a placa que compila, com o início de sessão, a leitura do servidor, as definições na flash, o Wi-Fi e as atualizações assinadas, tudo desligado até alguém o ligar. **Nunca correu numa placa e nada aqui envia ordens a uma bateria.**",
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
           "Guition JC1060P470C (ESP32-P4 with ESP32-C6, 7-inch 1024 x 600); code that compiles, never run on it", "A computer with CMake, a C++17 compiler and Python 3.11+", "Nothing has run on the board", "GPL-3.0-or-later"],
    "es": ["Pantalla táctil solar de A.R.M.O.R. (familia: Clients, padre: ARMOR-SERVER)", "Núcleo y simulador en C++17, CMake; comprobaciones en Python", f"{TESTS} programas de host",
           "Guition JC1060P470C (ESP32-P4 con ESP32-C6, 7 pulgadas, 1024 x 600); código que compila, nunca ejecutado en ella", "Un ordenador con CMake, un compilador C++17 y Python 3.11+", "Nada ha corrido en la placa", "GPL-3.0-or-later"],
    "de": ["Solar-Touchscreen von A.R.M.O.R. (Familie: Clients, übergeordnet: ARMOR-SERVER)", "Kern und Simulator in C++17, CMake; Prüfungen in Python", f"{TESTS} Host-Programme",
           "Guition JC1060P470C (ESP32-P4 mit ESP32-C6, 7 Zoll, 1024 x 600); Code wird übersetzt, lief nie darauf", "Ein Computer mit CMake, C++17-Compiler und Python 3.11+", "Nichts lief auf der Platine", "GPL-3.0-or-later"],
    "fr": ["Écran tactile solaire d'A.R.M.O.R. (famille : Clients, parent : ARMOR-SERVER)", "Cœur et simulateur en C++17, CMake ; contrôles en Python", f"{TESTS} programmes hôte",
           "Guition JC1060P470C (ESP32-P4 avec ESP32-C6, 7 pouces, 1024 x 600) ; code qui se compile, jamais exécuté dessus", "Un ordinateur avec CMake, un compilateur C++17 et Python 3.11+", "Rien n'a tourné sur la carte", "GPL-3.0-or-later"],
    "it": ["Schermo touch solare di A.R.M.O.R. (famiglia: Clients, genitore: ARMOR-SERVER)", "Nucleo e simulatore in C++17, CMake; controlli in Python", f"{TESTS} programmi host",
           "Guition JC1060P470C (ESP32-P4 con ESP32-C6, 7 pollici, 1024 x 600); codice che si compila, mai eseguito su di essa", "Un computer con CMake, un compilatore C++17 e Python 3.11+", "Nulla è girato sulla scheda", "GPL-3.0-or-later"],
    "ja": ["A.R.M.O.R. の太陽光タッチ画面（ファミリー：Clients、親：ARMOR-SERVER）", "C++17 のコアとシミュレータ、CMake、Python の検査", f"ホストプログラム {TESTS} 本",
           "Guition JC1060P470C（ESP32-P4 と ESP32-C6、7 インチ 1024 x 600）。コードはビルド可能、基板上では未実行", "CMake、C++17 コンパイラ、Python 3.11+ を備えた PC", "基板上では何も動いていません", "GPL-3.0-or-later"],
    "zh": ["A.R.M.O.R. 的太阳能触摸屏（家族：Clients，上级：ARMOR-SERVER）", "C++17 核心与模拟器、CMake；Python 检查", f"{TESTS} 个主机程序",
           "Guition JC1060P470C（ESP32-P4 搭配 ESP32-C6，7 英寸 1024 x 600）；代码可编译，从未在板上运行", "装有 CMake、C++17 编译器和 Python 3.11+ 的电脑", "电路板上尚未运行任何内容", "GPL-3.0-or-later"],
    "pt": ["Ecrã tátil solar do A.R.M.O.R. (família: Clients, principal: ARMOR-SERVER)", "Núcleo e simulador em C++17, CMake; verificações em Python", f"{TESTS} programas de host",
           "Guition JC1060P470C (ESP32-P4 com ESP32-C6, 7 polegadas, 1024 x 600); código que compila, nunca executado nela", "Um computador com CMake, um compilador C++17 e Python 3.11+", "Nada correu na placa", "GPL-3.0-or-later"],
}

STATUS = {
    "software": P("Core, screens and a firmware with a reading link are written; none has run on a board.", "Núcleo, pantallas y un firmware con enlace de lectura escritos; nada ha corrido en una placa.", "Kern, Bildschirme und eine Firmware mit Leseanbindung sind geschrieben; nichts lief auf einer Platine.", "Cœur, écrans et un firmware avec lien de lecture écrits ; rien n'a tourné sur une carte.", "Nucleo, schermate e un firmware con collegamento di lettura scritti; nulla è girato su una scheda.", "コア、画面、読み取り接続を持つファームウェアは作成済み。基板上では未実行。", "核心、界面和带读取连接的固件已编写；均未在电路板上运行。", "Núcleo, ecrãs e um firmware com ligação de leitura escritos; nada correu numa placa."),
    "tests": P("Host programs and two checks against ARMOR-COMMON; early stage.", "Programas de host y dos comprobaciones contra ARMOR-COMMON; fase inicial.", "Host-Programme und zwei Prüfungen gegen ARMOR-COMMON; frühes Stadium.", "Programmes hôte et deux contrôles avec ARMOR-COMMON ; stade précoce.", "Programmi host e due controlli con ARMOR-COMMON; fase iniziale.", "ホストプログラムと ARMOR-COMMON に対する 2 つの検査。初期段階。", "主机程序以及两项对照 ARMOR-COMMON 的检查；处于早期阶段。", "Programas de host e duas verificações face ao ARMOR-COMMON; fase inicial."),
    "ui": P("The screens are drawn by a simulator on a computer; never on the panel.", "Las pantallas las dibuja un simulador en el ordenador; nunca en el panel.", "Die Bildschirme zeichnet ein Simulator am Computer; nie auf dem Panel.", "Les écrans sont dessinés par un simulateur sur ordinateur ; jamais sur la dalle.", "Le schermate sono disegnate da un simulatore su computer; mai sul pannello.", "画面はコンピュータ上のシミュレータで描画。実機パネルでは未表示。", "界面由电脑上的模拟器绘制；从未在面板上显示。", "Os ecrãs são desenhados por um simulador no computador; nunca no painel."),
    "hardware": P("The firmware compiles; nothing has run on the board.", "El firmware compila; nada ha corrido en la placa.", "Die Firmware wird übersetzt; nichts lief auf der Platine.", "Le firmware se compile ; rien n'a tourné sur la carte.", "Il firmware si compila; nulla è girato sulla scheda.", "ファームウェアはビルド可能。基板上では何も動いていません。", "固件可编译；电路板上尚未运行任何内容。", "O firmware compila; nada correu na placa."),
    "security": P("PIN, sealed settings and signed updates are tested logic and compiled code only; no independent review.", "PIN, ajustes sellados y actualizaciones firmadas son solo lógica probada y código compilado; sin revisión independiente.", "PIN, versiegelte Einstellungen und signierte Updates sind nur getestete Logik und übersetzter Code; keine unabhängige Prüfung.", "PIN, réglages scellés et mises à jour signées ne sont que de la logique testée et du code compilé ; aucune revue indépendante.", "PIN, impostazioni sigillate e aggiornamenti firmati sono solo logica provata e codice compilato; nessuna revisione indipendente.", "PIN、封印された設定、署名付き更新はテスト済みロジックとビルド済みコードのみ。第三者レビューなし。", "PIN、加封设置和签名更新仅是经过测试的逻辑和编译过的代码；没有独立审查。", "PIN, definições seladas e atualizações assinadas são apenas lógica testada e código compilado; sem revisão independente."),
    "updates": P("Signed updates are written and off; no signed image is published and none has been installed on a board.", "Las actualizaciones firmadas están escritas y apagadas; no hay imagen firmada publicada ni instalada en una placa.", "Signierte Updates sind geschrieben und aus; es gibt kein veröffentlichtes signiertes Abbild und keines wurde installiert.", "Les mises à jour signées sont écrites et désactivées ; aucune image signée n'est publiée ni installée.", "Gli aggiornamenti firmati sono scritti e spenti; nessuna immagine firmata è pubblicata o installata.", "署名付き更新は作成済みで無効。署名済みイメージの公開も基板への導入もありません。", "签名更新已编写但默认关闭；尚未发布签名映像，也未安装到任何电路板。", "As atualizações assinadas estão escritas e desligadas; não há imagem assinada publicada nem instalada numa placa."),
    "integration": P("The firmware has the sign-in and the reading link, off by default; tried on a computer against the simulator, never against a server from a board.", "El firmware tiene el inicio de sesión y el enlace de lectura, apagados por defecto; probados en el ordenador con el simulador, nunca desde una placa contra un servidor.", "Die Firmware hat Anmeldung und Leseanbindung, standardmäßig aus; am Computer gegen den Simulator erprobt, nie von einer Platine gegen einen Server.", "Le firmware a la connexion et le lien de lecture, désactivés par défaut ; essayés sur ordinateur avec le simulateur, jamais depuis une carte vers un serveur.", "Il firmware ha accesso e collegamento di lettura, spenti per difetto; provati al computer con il simulatore, mai da una scheda verso un server.", "ファームウェアはサインインと読み取り接続を備え、既定では無効。コンピュータ上でシミュレータに対して試験済みで、基板からサーバーへは未実施。", "固件具备登录和读取连接，默认关闭；在电脑上对照模拟器试验过，从未由电路板连接服务器。", "O firmware tem o início de sessão e a ligação de leitura, desligados por omissão; experimentados no computador com o simulador, nunca de uma placa para um servidor."),
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
    ["A value that is missing or impossible is not shown, never as a zero.", "Cells, modules and stacks have a level with an icon and a word; only an alarm blinks, at most twice a second.", "A PIN kept as a salted hash, with growing locks and a short session.", "A battery operation is offered only when the server allows it, the data is fresh, the PIN is open and the person confirmed.", "Who made the equipment, and what a battery says of itself in three levels: a notice, a protection and a fault of its electronics, which is red and still.", "A simulator with six scenarios, checked against the message schemas.", "Screens at 1024 x 600 in eight languages, drawn on a computer by the same code as the firmware.", "A board check screen for the first day: chip, memory, panel, touch, I2C, cable network, colour bars and corners."],
    ["Un valor que falta o es imposible no se muestra, nunca como cero.", "Celdas, módulos y baterías tienen un nivel con icono y palabra; solo parpadea una alarma, como mucho dos veces por segundo.", "PIN guardado como hash con sal, con bloqueos crecientes y sesión corta.", "Una operación de batería solo se ofrece si el servidor lo permite, los datos son recientes, el PIN está abierto y la persona ha confirmado.", "Quién fabricó el equipo y lo que dice la batería en tres niveles: aviso, protección y fallo de su electrónica, en rojo fijo.", "Simulador con seis escenarios, comprobado contra los esquemas de los mensajes.", "Pantallas a 1024 x 600 en ocho idiomas, dibujadas en el ordenador con el mismo código que el firmware.", "Pantalla de comprobación para el primer día: chip, memoria, panel, táctil, I2C, red por cable, barras de color y esquinas."],
    ["Ein fehlender oder unmöglicher Wert wird nicht angezeigt, nie als Null.", "Zellen, Module und Stapel haben eine Stufe mit Symbol und Wort; nur ein Alarm blinkt, höchstens zweimal pro Sekunde.", "PIN als gesalzener Hash, mit wachsenden Sperren und kurzer Sitzung.", "Eine Batterieaktion wird nur angeboten, wenn der Server es erlaubt, die Daten frisch sind, die PIN offen ist und die Person bestätigt hat.", "Wer das Gerät baute und was die Batterie in drei Stufen meldet: Hinweis, Schutz und Fehler der Elektronik, der rot und ruhig steht.", "Simulator mit sechs Szenarien, gegen die Nachrichtenschemas geprüft.", "Bildschirme in 1024 x 600 in acht Sprachen, am Computer mit demselben Code wie die Firmware gezeichnet.", "Platinentest für den ersten Tag: Chip, Speicher, Panel, Touch, I2C, Kabelnetz, Farbbalken und Ecken."],
    ["Une valeur absente ou impossible n'est pas affichée, jamais comme un zéro.", "Cellules, modules et batteries ont un niveau avec icône et mot ; seule une alarme clignote, deux fois par seconde au plus.", "PIN conservé sous forme de hachage salé, avec blocages croissants et session courte.", "Une opération batterie n'est proposée que si le serveur l'autorise, les données sont récentes, le PIN est ouvert et la personne a confirmé.", "Qui a fabriqué l'équipement et ce que dit la batterie sur trois niveaux : avis, protection et panne de l'électronique, en rouge fixe.", "Simulateur à six scénarios, vérifié contre les schémas des messages.", "Écrans 1024 x 600 en huit langues, dessinés sur ordinateur par le même code que le firmware.", "Écran de contrôle pour le premier jour : puce, mémoire, dalle, tactile, I2C, réseau filaire, barres de couleur et coins."],
    ["Un valore mancante o impossibile non viene mostrato, mai come zero.", "Celle, moduli e batterie hanno un livello con icona e parola; lampeggia solo un allarme, al massimo due volte al secondo.", "PIN conservato come hash con sale, con blocchi crescenti e sessione breve.", "Un'operazione sulla batteria è proposta solo se il server la consente, i dati sono recenti, il PIN è aperto e la persona ha confermato.", "Chi ha prodotto l'apparecchio e cosa dice la batteria su tre livelli: avviso, protezione e guasto dell'elettronica, in rosso fisso.", "Simulatore con sei scenari, verificato con gli schemi dei messaggi.", "Schermate 1024 x 600 in otto lingue, disegnate al computer dallo stesso codice del firmware.", "Schermata di controllo per il primo giorno: chip, memoria, pannello, tocco, I2C, rete via cavo, barre di colore e angoli."],
    ["欠けている値やあり得ない値は表示せず、ゼロにもしません。", "セル、モジュール、スタックにはアイコンと言葉付きのレベルがあり、点滅するのは警報のみで毎秒 2 回までです。", "PIN はソルト付きハッシュで保存し、ロックは次第に長くなり、セッションは短時間です。", "バッテリー操作は、サーバーが許可し、データが新しく、PIN が開かれ、本人が確認した場合のみ提示します。", "機器の製造元と、電池が伝える内容を注意・保護・回路故障の 3 段階で表示します。回路故障は点滅しない赤です。", "6 つのシナリオを持つシミュレータ。メッセージスキーマと照合します。", "1024 x 600 の画面を 8 言語で表示。ファームウェアと同じコードをコンピュータ上で描画します。", "初日用の基板確認画面：チップ、メモリ、パネル、タッチ、I2C、有線ネットワーク、カラーバーと四隅。"],
    ["缺失或不可能的数值不显示，也绝不显示为零。", "电芯、模块和电池组的级别带有图标和文字；只有警报闪烁，每秒最多两次。", "PIN 以加盐哈希保存，锁定时间递增，会话很短。", "仅当服务器允许、数据新鲜、PIN 已解锁且本人确认时，才提供电池操作。", "显示设备制造商以及电池自述的三个级别：提示、保护和电路故障（红色常亮不闪烁）。", "包含六个场景的模拟器，并对照消息模式进行检查。", "八种语言的 1024 x 600 界面，用与固件相同的代码在电脑上绘制。", "首日使用的电路板检查界面：芯片、内存、面板、触摸、I2C、有线网络、色条和四角。"],
    ["Um valor em falta ou impossível não é mostrado, nunca como zero.", "Células, módulos e baterias têm um nível com ícone e palavra; só um alarme pisca, no máximo duas vezes por segundo.", "PIN guardado como hash com sal, com bloqueios crescentes e sessão curta.", "Uma operação na bateria só é proposta se o servidor permitir, os dados forem recentes, o PIN estiver aberto e a pessoa tiver confirmado.", "Quem fez o equipamento e o que a bateria diz em três níveis: aviso, proteção e falha da eletrónica, a vermelho fixo.", "Simulador com seis cenários, verificado face aos esquemas das mensagens.", "Ecrãs a 1024 x 600 em oito línguas, desenhados no computador com o mesmo código do firmware.", "Ecrã de verificação para o primeiro dia: chip, memória, painel, toque, I2C, rede por cabo, barras de cor e cantos."],
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
    ["`test_plant.cpp`", P("the six scenarios", "los seis escenarios", "die sechs Szenarien", "les six scénarios", "i sei scenari", "6 つのシナリオ", "六个场景", "os seis cenários")],
    ["`test_screen_text.cpp`", P("every word in the eight languages", "cada texto en los ocho idiomas", "jeder Text in acht Sprachen", "chaque texte en huit langues", "ogni testo nelle otto lingue", "全文言の 8 言語", "每条文字的八种语言", "cada texto nas oito línguas")],
    ["`test_server_link.cpp`", P("the reading of the server: cuts, refusals", "la lectura del servidor: cortes, rechazos", "das Lesen des Servers: Abbrüche, Absagen", "la lecture du serveur : coupures, refus", "la lettura del server: interruzioni, rifiuti", "サーバー読取：切断と拒否", "读取服务器：中断与拒绝", "a leitura do servidor: cortes, recusas")],
    ["`test_panel.cpp`", P("settings, serial console, session, update check", "ajustes, consola serie, sesión, comprobación de actualización", "Einstellungen, serielle Konsole, Sitzung, Update-Prüfung", "réglages, console série, session, contrôle de mise à jour", "impostazioni, console seriale, sessione, verifica aggiornamento", "設定、シリアルコンソール、セッション、更新の確認", "设置、串口控制台、会话、更新校验", "definições, consola série, sessão, verificação de atualização")],
    ["`test_screen_model.cpp`", P("the alarms listed, numbers, board pins", "las alarmas listadas, cifras, pines", "gelistete Alarme, Zahlen, Pins", "alarmes listées, chiffres, broches", "allarmi elencati, cifre, pin", "警報一覧、数値、ピン", "警报列表、数值、引脚", "alarmes listados, números, pinos")],
    ["`check_font_glyphs.py`", P("the fonts hold every character", "las fuentes tienen cada carácter", "die Schriften haben jedes Zeichen", "les polices ont chaque caractère", "i font hanno ogni carattere", "フォントに全文字がある", "字体包含全部字符", "os tipos de letra têm cada carácter")],
    ["`check_simulator.py`", P("the simulator follows the schemas", "el simulador cumple los esquemas", "der Simulator folgt den Schemas", "le simulateur respecte les schémas", "il simulatore rispetta gli schemi", "シミュレータがスキーマに従う", "模拟器符合模式", "o simulador cumpre os esquemas")],
    ["`check_base_copies.py`", P("shared files match their source", "los ficheros compartidos coinciden con su origen", "gemeinsame Dateien entsprechen der Quelle", "les fichiers partagés correspondent à leur source", "i file condivisi coincidono con l'origine", "共有ファイルが元と一致", "共享文件与来源一致", "os ficheiros partilhados coincidem com a origem")],
]
TEST_HEAD = P(["File", "What it covers"], ["Fichero", "Qué cubre"], ["Datei", "Was sie abdeckt"], ["Fichier", "Ce qu'il couvre"], ["File", "Cosa copre"], ["ファイル", "対象"], ["文件", "覆盖内容"], ["Ficheiro", "O que cobre"])

BUILD = P(
    "The first release carries one file per variant (screen revision and chip), built in GitHub Actions and written at address 0 with `esptool`. **It is not tested on hardware: it has never run on a board.** The workflow `Screen pictures (simulator)` draws the screens.",
    "La primera release lleva un fichero por variante (revisión de pantalla y chip), compilado en GitHub Actions y grabado en la dirección 0 con `esptool`. **No está probado en hardware: nunca ha corrido en una placa.** El flujo `Screen pictures (simulator)` dibuja las pantallas.",
    "Das erste Release enthält eine Datei je Variante (Bildschirm- und Chiprevision), in GitHub Actions gebaut und mit `esptool` ab Adresse 0 geschrieben. **Nicht auf Hardware getestet: Sie lief noch nie auf einer Platine.** Der Workflow `Screen pictures (simulator)` zeichnet die Bildschirme.",
    "La première version publiée contient un fichier par variante (révision de l'écran et de la puce), compilé dans GitHub Actions et écrit à l'adresse 0 avec `esptool`. **Non testée sur matériel : elle n'a jamais tourné sur une carte.** Le workflow `Screen pictures (simulator)` dessine les écrans.",
    "La prima release contiene un file per variante (revisione dello schermo e del chip), compilato in GitHub Actions e scritto all'indirizzo 0 con `esptool`. **Non provata su hardware: non è mai girata su una scheda.** Il workflow `Screen pictures (simulator)` disegna le schermate.",
    "最初のリリースには、画面とチップのリビジョンごとに1つのファイルがあります。GitHub Actions でビルドし、`esptool` でアドレス 0 に書き込みます。**実機ではテストしていません。基板上で動かしたことはありません。** ワークフロー `Screen pictures (simulator)` が画面を描画します。",
    "首个发布版本为每个变体（屏幕和芯片版本）提供一个文件，在 GitHub Actions 中编译，用 `esptool` 写入地址 0。**未经硬件测试：从未在电路板上运行过。** 工作流 `Screen pictures (simulator)` 绘制各个屏幕。",
    "A primeira release traz um ficheiro por variante (revisão do ecrã e do chip), compilado no GitHub Actions e gravado no endereço 0 com `esptool`. **Não testada em hardware: nunca correu numa placa.** O workflow `Screen pictures (simulator)` desenha os ecrãs.",
)

DOES_TEXT = P(
    "Reads the server's solar answer, judges it, guards the PIN, draws the screens on a computer and compiles a firmware for the board that can sign in, keep its settings, join Wi-Fi and take a signed update, all off by default and set up from the serial console.",
    "Lee la respuesta solar del servidor, la juzga, protege el PIN, dibuja las pantallas en el ordenador y compila un firmware para la placa que puede iniciar sesión, guardar sus ajustes, usar Wi-Fi y aceptar una actualización firmada, todo apagado por defecto y configurado por la consola serie.",
    "Liest die Solar-Antwort des Servers, bewertet sie, schützt die PIN, zeichnet die Bildschirme am Computer und übersetzt eine Firmware, die sich anmelden, Einstellungen speichern, WLAN nutzen und ein signiertes Update annehmen kann, alles standardmäßig aus und über die serielle Konsole eingerichtet.",
    "Lit la réponse solaire du serveur, la juge, protège le PIN, dessine les écrans sur ordinateur et compile un firmware qui peut se connecter, garder ses réglages, rejoindre le Wi-Fi et accepter une mise à jour signée, tout désactivé par défaut et réglé par la console série.",
    "Legge la risposta solare del server, la valuta, protegge il PIN, disegna le schermate al computer e compila un firmware che può accedere, conservare le impostazioni, usare il Wi-Fi e accettare un aggiornamento firmato, tutto spento per difetto e impostato dalla console seriale.",
    "サーバーの太陽光応答の読み取りと判定、PIN の保護、コンピュータ上での画面描画、そしてサインイン、設定保存、Wi-Fi 接続、署名付き更新に対応するファームウェアのビルド（すべて既定で無効、シリアルコンソールで設定）。",
    "读取并判断服务器的太阳能应答、保护 PIN、在电脑上绘制界面，并编译可登录、保存设置、连接 Wi-Fi 和接受签名更新的固件（全部默认关闭，通过串口控制台设置）。",
    "Lê a resposta solar do servidor, avalia-a, protege o PIN, desenha os ecrãs no computador e compila um firmware que pode iniciar sessão, guardar as definições, usar Wi-Fi e aceitar uma atualização assinada, tudo desligado por omissão e configurado pela consola série.",
)
DOES_NOT_TEXT = P(
    "Send an order to a battery, set itself up from the screen, or run on the board (never tried).",
    "Enviar órdenes a una batería, configurarse desde la pantalla ni correr en la placa (nunca probado).",
    "Befehle an eine Batterie senden, sich am Bildschirm einrichten lassen oder auf der Platine laufen (nie versucht).",
    "Envoyer un ordre à une batterie, se configurer depuis l'écran ou tourner sur la carte (jamais essayé).",
    "Inviare ordini a una batteria, configurarsi dallo schermo o girare sulla scheda (mai provato).",
    "バッテリーへの命令送信、画面上での初期設定、基板上での動作（未実施）。",
    "向电池发送指令、在屏幕上完成设置，或在电路板上运行（从未尝试）。",
    "Enviar ordens a uma bateria, configurar-se a partir do ecrã ou correr na placa (nunca tentado).",
)
NEXT_ITEMS = P(
    ["The first power-up on the board with the board check screen.", "Try the sign-in, the reading link, Wi-Fi and an update on the board.", "Setting up from the screen instead of the serial console.", "The board layer shared with ARMOR-NODE-HMI."],
    ["El primer encendido en la placa con la pantalla de comprobación.", "Probar en la placa el inicio de sesión, el enlace de lectura, la Wi-Fi y una actualización.", "Configurar desde la pantalla en lugar de la consola serie.", "La capa de placa compartida con ARMOR-NODE-HMI."],
    ["Das erste Einschalten auf der Platine mit dem Platinentest.", "Anmeldung, Leseanbindung, WLAN und ein Update auf der Platine erproben.", "Einrichtung am Bildschirm statt über die serielle Konsole.", "Die mit ARMOR-NODE-HMI gemeinsame Platinenschicht."],
    ["La première mise sous tension avec l'écran de contrôle.", "Essayer sur la carte la connexion, le lien de lecture, le Wi-Fi et une mise à jour.", "La configuration depuis l'écran au lieu de la console série.", "La couche carte partagée avec ARMOR-NODE-HMI."],
    ["La prima accensione sulla scheda con la schermata di controllo.", "Provare sulla scheda l'accesso, il collegamento di lettura, il Wi-Fi e un aggiornamento.", "La configurazione dallo schermo invece che dalla console seriale.", "Lo strato di scheda condiviso con ARMOR-NODE-HMI."],
    ["基板確認画面を使った基板での初回起動。", "基板上でサインイン、読み取り接続、Wi-Fi、更新を試す。", "シリアルコンソールの代わりに画面で設定する。", "ARMOR-NODE-HMI と共有する基板レイヤー。"],
    ["借助电路板检查界面在板上首次上电。", "在板上试验登录、读取连接、Wi-Fi 和更新。", "用屏幕代替串口控制台进行设置。", "与 ARMOR-NODE-HMI 共享的板级层。"],
    ["O primeiro arranque na placa com o ecrã de verificação.", "Experimentar na placa o início de sessão, a ligação de leitura, o Wi-Fi e uma atualização.", "Configurar a partir do ecrã em vez da consola série.", "A camada de placa partilhada com o ARMOR-NODE-HMI."],
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
