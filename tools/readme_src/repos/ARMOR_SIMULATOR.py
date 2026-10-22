# The facts that do not depend on the language, and the words of every language, of ARMOR-SIMULATOR.
# Copyright (C) 2026 JuanenRac (Electro Hobby 3D). GPL-3.0-or-later.

FACTS = {
 "emoji": "🧪",
 "badges": [
  [
   "Language",
   "Python%203.11%2B",
   "3776ab"
  ],
  [
   "Dependencies",
   "none",
   "2ea44f"
  ],
  [
   "Tests",
   "57%20passing",
   "2ea44f"
  ]
 ],
 "diagram": "",
 "build": "```powershell\n$env:PYTHONPATH=\"src\"\npython -m armor_simulator --count 20 --scenario crossing --seed 1 --validate\npython -m unittest discover -s tests   # 57 tests\n```",
 "structure": "```text\nARMOR-SIMULATOR/\n├── src/armor_simulator/   scenarios, faults, solar (inverter and battery messages), electrical (an electrical node), publisher, cli\n├── tests/                 57 tests, including a local HTTP server\n└── docs/USAGE.md\n```",
 "tests": "57 (`python -m unittest discover -s tests`)",
 "requirements": [
  "Python 3.11+ (standard library only)"
 ]
}

TEXT = {
 "en": {
  "tagline": "Offline telemetry simulator with repeatable faults",
  "honest": "Scenarios, faults, delivery to a server and the 57 tests are real, and the simulator is what feeds a server on a computer when no node is plugged in. The geometry is **illustrative**, not a model of the real LD2450 radar, and nothing here has been compared with real hardware.",
  "bullets": [
   "**Scenarios:** `patrol`, `crossing`, `two-intruders` and `empty`, on a three-sensor corner geometry, plus a day/night light cycle or a fixed night.",
   "**Repeatable faults:** a silent node, out-of-order and duplicated messages, a flapping node, and deliberately invalid messages (lux over the limit, unknown field, too many tracks) for negative tests.",
   "**Deterministic:** the same seed always prints the same lines; nothing is sent unless you give `--server-url` and `--ingest-token`.",
   "**Checked against the contract:** `--validate` runs every message through ARMOR-COMMON before it is emitted.",
   "**Careful delivery:** only a plain http(s) origin is accepted; a 4xx stops the run, a 5xx or a network error is retried.",
   "**Electrical node:** `--electrical` adds the three channels of an electrical node (the grid input, a water heater and a DC bus) over a fast day, with a mains outage, a spell of high voltage and a meter alarm.",
   "**Solar equipment:** `--solar` adds an inverter and a two-module battery stack (fifteen cells each, capacities included) over a fast day of 240 samples, with a mains outage late in the day; the messages are checked against the solar contract of ARMOR-COMMON and delivered to `/api/v1/solar`."
  ],
  "note": "Full options, scenarios and faults: [usage](docs/USAGE.md).",
  "fit": "ARMOR-SIMULATOR is how the rest of the family is tried without hardware: it plays the part of a radar node, a solar gateway or an electrical node and sends their messages to an [ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER), with faults you can repeat, so [ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) and the phone app can be seen working with a house that does not exist. Every message it makes is checked against the contracts of [ARMOR-COMMON](https://github.com/JuanenRac/ARMOR-COMMON).",
  "hardware": "Not applicable: it is the stand-in for hardware, used on a computer"
 },
 "es": {
  "tagline": "Simulador de telemetría sin conexión con fallos repetibles",
  "honest": "Los escenarios, los fallos, la entrega a un servidor y los 57 tests son reales, y el simulador es lo que alimenta a un servidor en un ordenador cuando no hay ningún nodo conectado. La geometría es **ilustrativa**, no un modelo del radar LD2450 real, y nada de esto se ha comparado con hardware real.",
  "bullets": [
   "**Escenarios:** `patrol`, `crossing`, `two-intruders` y `empty`, con una geometría de esquina de tres sensores, más un ciclo de luz día/noche o una noche fija.",
   "**Fallos repetibles:** nodo en silencio, mensajes desordenados y duplicados, nodo intermitente y mensajes inválidos a propósito (lux por encima del límite, campo desconocido, demasiadas pistas) para pruebas negativas.",
   "**Determinista:** la misma semilla imprime siempre las mismas líneas; no se envía nada salvo que indiques `--server-url` y `--ingest-token`.",
   "**Comprobado contra el contrato:** `--validate` pasa cada mensaje por ARMOR-COMMON antes de emitirlo.",
   "**Entrega cuidadosa:** solo se acepta un origen http(s) simple; un 4xx detiene la ejecución, un 5xx o un error de red se reintenta.",
   "**Nodo eléctrico:** `--electrical` añade los tres canales de un nodo eléctrico (la entrada de red, un termo y un bus de continua) durante un día rápido, con un corte de red, un periodo de tensión alta y una alarma de contador.",
   "**Equipo solar:** `--solar` añade un inversor y una pila de baterías de dos módulos (quince celdas cada uno, con capacidades) durante un día rápido de 240 muestras, con un corte de red al final de la tarde; los mensajes se comprueban contra el contrato solar de ARMOR-COMMON y se entregan a `/api/v1/solar`."
  ],
  "note": "Opciones, escenarios y fallos completos: [uso](docs/USAGE.md).",
  "fit": "ARMOR-SIMULATOR es cómo se prueba el resto de la familia sin hardware: hace de nodo radar, de pasarela solar o de nodo eléctrico y envía sus mensajes a un [ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER), con fallos que se pueden repetir, de modo que [ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) y la app móvil se vean funcionando con una casa que no existe. Cada mensaje que hace se comprueba contra los contratos de [ARMOR-COMMON](https://github.com/JuanenRac/ARMOR-COMMON).",
  "hardware": "No aplica: es el sustituto del hardware, usado en un ordenador",
  "requirements": [
   "Python 3.11+ (solo la biblioteca estándar)"
  ]
 },
 "fr": {
  "tagline": "Simulateur de télémétrie hors ligne avec des pannes reproductibles",
  "honest": "Les scénarios, les pannes, la livraison à un serveur et les 57 tests sont réels, et le simulateur est ce qui alimente un serveur sur un ordinateur quand aucun nœud n'est branché. La géométrie est **illustrative**, pas un modèle du vrai radar LD2450, et rien de tout cela n'a été comparé à du matériel réel.",
  "bullets": [
   "**Scénarios :** `patrol`, `crossing`, `two-intruders` et `empty`, sur une géométrie d'angle à trois capteurs, avec un cycle de lumière jour/nuit ou une nuit fixe.",
   "**Pannes reproductibles :** un nœud muet, des messages désordonnés ou dupliqués, un nœud instable et des messages volontairement invalides (lux hors limite, champ inconnu, trop de pistes) pour les tests négatifs.",
   "**Déterministe :** la même graine imprime toujours les mêmes lignes ; rien n'est envoyé sans `--server-url` et `--ingest-token`.",
   "**Vérifié contre le contrat :** `--validate` fait passer chaque message par ARMOR-COMMON avant de l'émettre.",
   "**Envoi prudent :** seule une origine http(s) simple est acceptée ; une erreur 4xx arrête l'exécution, une 5xx ou une erreur réseau est retentée.",
   "**Nœud électrique :** `--electrical` ajoute les trois canaux d'un nœud électrique (l'entrée du réseau, un chauffe-eau et un bus continu) sur une journée accélérée, avec une coupure du secteur, une période de tension élevée et une alarme de compteur.",
   "**Équipement solaire :** `--solar` ajoute un onduleur et une pile de batteries de deux modules (quinze cellules chacun, capacités comprises) sur une journée accélérée de 240 échantillons, avec une coupure du réseau en fin de journée ; les messages sont vérifiés contre le contrat solaire d'ARMOR-COMMON et envoyés à `/api/v1/solar`."
  ],
  "note": "Toutes les options, scénarios et pannes : [utilisation](docs/USAGE.md).",
  "fit": "ARMOR-SIMULATOR est la façon d'essayer le reste de la famille sans matériel : il joue le rôle d'un nœud radar, d'une passerelle solaire ou d'un nœud électrique et envoie leurs messages à un [ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER), avec des pannes répétables, pour que [ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) et l'application mobile se voient fonctionner avec une maison qui n'existe pas. Chaque message qu'il fait est vérifié contre les contrats d'[ARMOR-COMMON](https://github.com/JuanenRac/ARMOR-COMMON).",
  "hardware": "Sans objet : c'est le substitut du matériel, utilisé sur un ordinateur",
  "requirements": [
   "Python 3.11+ (bibliothèque standard uniquement)"
  ]
 },
 "it": {
  "tagline": "Simulatore di telemetria offline con guasti ripetibili",
  "honest": "Gli scenari, i guasti, la consegna a un server e i 57 test sono reali, e il simulatore è ciò che alimenta un server su un computer quando nessun nodo è collegato. La geometria è **illustrativa**, non un modello del vero radar LD2450, e nulla di tutto ciò è stato confrontato con hardware reale.",
  "bullets": [
   "**Scenari:** `patrol`, `crossing`, `two-intruders` ed `empty`, su una geometria d'angolo a tre sensori, con un ciclo di luce giorno/notte o una notte fissa.",
   "**Guasti ripetibili:** un nodo muto, messaggi fuori ordine o duplicati, un nodo instabile e messaggi volutamente non validi (lux oltre il limite, campo sconosciuto, troppe tracce) per i test negativi.",
   "**Deterministico:** lo stesso seme stampa sempre le stesse righe; non viene inviato nulla senza `--server-url` e `--ingest-token`.",
   "**Verificato contro il contratto:** `--validate` fa passare ogni messaggio per ARMOR-COMMON prima di emetterlo.",
   "**Invio prudente:** si accetta solo un'origine http(s) semplice; un 4xx ferma l'esecuzione, un 5xx o un errore di rete viene ritentato.",
   "**Nodo elettrico:** `--electrical` aggiunge i tre canali di un nodo elettrico (l'ingresso di rete, uno scaldabagno e un bus in continua) su una giornata accelerata, con un'interruzione di rete, un periodo di tensione alta e un allarme di contatore.",
   "**Impianto solare:** `--solar` aggiunge un inverter e un pacco batterie da due moduli (quindici celle ciascuno, con le capacità) su un giorno accelerato di 240 campioni, con un'interruzione di rete a fine giornata; i messaggi sono verificati contro il contratto solare di ARMOR-COMMON e consegnati a `/api/v1/solar`."
  ],
  "note": "Tutte le opzioni, gli scenari e i guasti: [uso](docs/USAGE.md).",
  "fit": "ARMOR-SIMULATOR è il modo per provare il resto della famiglia senza hardware: fa la parte di un nodo radar, di un gateway solare o di un nodo elettrico e invia i loro messaggi a un [ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER), con guasti ripetibili, così [ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) e l'app mobile si vedono funzionare con una casa che non esiste. Ogni messaggio che produce è controllato contro i contratti di [ARMOR-COMMON](https://github.com/JuanenRac/ARMOR-COMMON).",
  "hardware": "Non applicabile: è il sostituto dell'hardware, usato su un computer",
  "requirements": [
   "Python 3.11+ (solo la libreria standard)"
  ]
 },
 "de": {
  "tagline": "Offline-Telemetriesimulator mit wiederholbaren Fehlern",
  "honest": "Die Szenarien, die Fehler, die Zustellung an einen Server und die 57 Tests sind real, und der Simulator speist einen Server auf einem Computer, wenn kein Knoten angeschlossen ist. Die Geometrie ist **veranschaulichend**, kein Modell des echten LD2450-Radars, und nichts davon wurde mit echter Hardware verglichen.",
  "bullets": [
   "**Szenarien:** `patrol`, `crossing`, `two-intruders` und `empty` auf einer Eckgeometrie mit drei Sensoren, dazu ein Tag/Nacht-Lichtzyklus oder eine feste Nacht.",
   "**Wiederholbare Fehler:** ein stummer Knoten, vertauschte und doppelte Nachrichten, ein flatternder Knoten und absichtlich ungültige Nachrichten (Lux über dem Limit, unbekanntes Feld, zu viele Spuren) für Negativtests.",
   "**Deterministisch:** derselbe Seed druckt immer dieselben Zeilen; gesendet wird nur mit `--server-url` und `--ingest-token`.",
   "**Gegen den Vertrag geprüft:** `--validate` schickt jede Nachricht vor dem Ausgeben durch ARMOR-COMMON.",
   "**Sorgfältige Übermittlung:** nur ein einfacher http(s)-Ursprung wird akzeptiert; ein 4xx stoppt den Lauf, ein 5xx oder ein Netzwerkfehler wird wiederholt.",
   "**Elektroknoten:** `--electrical` fügt die drei Kanäle eines Elektroknotens hinzu (den Netzanschluss, einen Warmwasserspeicher und einen Gleichstrombus) über einen schnellen Tag, mit einem Netzausfall, einer Phase hoher Spannung und einem Zähleralarm.",
   "**Solaranlage:** `--solar` fügt einen Wechselrichter und einen Batteriestapel aus zwei Modulen (je fünfzehn Zellen, mit Kapazitäten) über einen Zeitraffer-Tag von 240 Werten hinzu, mit einem Netzausfall am späten Tag; die Nachrichten werden gegen den Solar-Vertrag von ARMOR-COMMON geprüft und an `/api/v1/solar` geliefert."
  ],
  "note": "Alle Optionen, Szenarien und Fehler: [Verwendung](docs/USAGE.md).",
  "fit": "ARMOR-SIMULATOR ist die Art, den Rest der Familie ohne Hardware auszuprobieren: Er spielt die Rolle eines Radarknotens, eines Solar-Gateways oder eines Elektroknotens und sendet deren Nachrichten an einen [ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER), mit wiederholbaren Fehlern, sodass [ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) und die Handy-App mit einem Haus, das es nicht gibt, arbeiten. Jede erzeugte Nachricht wird gegen die Verträge von [ARMOR-COMMON](https://github.com/JuanenRac/ARMOR-COMMON) geprüft.",
  "hardware": "Nicht zutreffend: er ist der Hardware-Ersatz, auf einem Computer benutzt",
  "requirements": [
   "Python 3.11+ (nur die Standardbibliothek)"
  ]
 },
 "zh": {
  "tagline": "带可重复故障的离线遥测模拟器",
  "honest": "场景、故障、向服务器的投递和 57 个测试都是真实的，没有节点接入时，模拟器用来给计算机上的服务器供数据。几何是**示意性的**，不是真实 LD2450 雷达的模型，这里的一切都没有与真实硬件对比过。",
  "bullets": [
   "**场景：** `patrol`、`crossing`、`two-intruders` 和 `empty`，基于三传感器的拐角几何，另有昼夜光照周期或固定夜晚。",
   "**可重复的故障：** 静默节点、乱序和重复的消息、抖动的节点，以及为负面测试特意构造的无效消息（lux 超限、未知字段、轨迹过多）。",
   "**确定性：** 相同的种子总是打印相同的行；除非提供 `--server-url` 和 `--ingest-token`，否则不会发送任何内容。",
   "**对照契约检查：** `--validate` 在发出每条消息之前先让它通过 ARMOR-COMMON。",
   "**谨慎投递：** 只接受简单的 http(s) 源；4xx 会终止运行，5xx 或网络错误会重试。",
   "**电气节点：** `--electrical` 会在加速的一天里加入电气节点的三个通道（电网入口、热水器和直流母线），其中包含一次停电、一段高电压和一次电表告警。",
   "**太阳能设备：** `--solar` 会在 240 个样本的快进一天中加入一台逆变器和一个两模块的电池组（每个模块十五个电芯，含容量），并在傍晚出现一次市电中断；消息会对照 ARMOR-COMMON 的太阳能契约检查，并投递到 `/api/v1/solar`。"
  ],
  "note": "完整的选项、场景和故障：[用法](docs/USAGE.md)。",
  "fit": "ARMOR-SIMULATOR 让家族的其他部分无需硬件就能试用：它扮演雷达节点、太阳能网关或电气节点，把它们的消息发给 [ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER)，故障可重复，这样就能看到 [ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) 和手机应用在一个并不存在的住宅上运行。它生成的每条消息都对照 [ARMOR-COMMON](https://github.com/JuanenRac/ARMOR-COMMON) 的契约检查。",
  "hardware": "不适用：它是硬件的替身，在计算机上使用",
  "requirements": [
   "Python 3.11+（仅标准库）"
  ]
 },
 "ja": {
  "tagline": "再現可能な故障を備えたオフラインのテレメトリシミュレーター",
  "honest": "シナリオ、故障、サーバーへの送信、57 件のテストは実在し、ノードを接続していないときにコンピューター上のサーバーにデータを送るのがシミュレーターです。ジオメトリは**例示的**なもので、実際の LD2450 レーダーのモデルではなく、実機との比較は一切していません。",
  "bullets": [
   "**シナリオ：** `patrol`、`crossing`、`two-intruders`、`empty`。センサー 3 基のコーナー配置で、昼夜の光サイクルまたは固定の夜を選べます。",
   "**再現可能な故障：** 沈黙するノード、順序が入れ替わったり重複したりするメッセージ、不安定なノード、そして否定テスト用にわざと無効にしたメッセージ（lux の上限超過、未知のフィールド、トラックが多すぎる）。",
   "**決定的：** 同じシードは常に同じ行を出力します。`--server-url` と `--ingest-token` を指定しない限り何も送信しません。",
   "**契約に照らして検査：** `--validate` は各メッセージを送り出す前に ARMOR-COMMON に通します。",
   "**慎重な送信：** 単純な http(s) オリジンのみ受け付けます。4xx は実行を止め、5xx やネットワークエラーは再試行します。",
   "**電気ノード：** `--electrical` は、電気ノードの 3 つのチャンネル（系統入力、給湯器、直流バス）を加速した 1 日にわたって出力し、停電、高電圧の期間、電力量計の警報を含みます。",
   "**太陽光設備：** `--solar` は、240 サンプルの早送りの 1 日の間に、インバーターと 2 モジュールのバッテリースタック（各 15 セル、容量付き）を加え、夕方に系統の停電を起こします。メッセージは ARMOR-COMMON の太陽光契約で検査され、`/api/v1/solar` に送られます。"
  ],
  "note": "全オプション、シナリオ、故障：[使い方](docs/USAGE.md)。",
  "fit": "ARMOR-SIMULATOR は、ハードウェアなしでファミリーの他の部分を試す手段です。レーダーノード、ソーラーゲートウェイ、電気ノードの役を演じてそのメッセージを [ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER) に送り、再現できる故障も起こせるため、存在しない家で [ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) とスマートフォンアプリが動く様子を見られます。生成するメッセージはすべて [ARMOR-COMMON](https://github.com/JuanenRac/ARMOR-COMMON) のコントラクトで検査されます。",
  "hardware": "該当なし：ハードウェアの代役で、コンピューター上で使います",
  "requirements": [
   "Python 3.11+（標準ライブラリのみ）"
  ]
 },
 "pt": {
  "tagline": "Simulador de telemetria offline com falhas repetíveis",
  "honest": "Os cenários, as falhas, a entrega a um servidor e os 57 testes são reais, e o simulador é o que alimenta um servidor num computador quando nenhum nó está ligado. A geometria é **ilustrativa**, não um modelo do radar LD2450 real, e nada disto foi comparado com hardware real.",
  "bullets": [
   "**Cenários:** `patrol`, `crossing`, `two-intruders` e `empty`, numa geometria de canto com três sensores, mais um ciclo de luz dia/noite ou uma noite fixa.",
   "**Falhas repetíveis:** um nó silencioso, mensagens fora de ordem e duplicadas, um nó que oscila, e mensagens deliberadamente inválidas (lux acima do limite, campo desconhecido, demasiados rastos) para testes negativos.",
   "**Determinista:** a mesma semente imprime sempre as mesmas linhas; nada se envia a menos que indique `--server-url` e `--ingest-token`.",
   "**Verificado contra o contrato:** `--validate` passa cada mensagem pelo ARMOR-COMMON antes de a emitir.",
   "**Envio cuidadoso:** só se aceita uma origem http(s) simples; um 4xx pára a execução, um 5xx ou um erro de rede repete-se.",
   "**Nó elétrico:** `--electrical` acrescenta os três canais de um nó elétrico (a entrada da rede, um esquentador e um barramento DC) ao longo de um dia rápido, com um corte de energia, um período de tensão alta e um alarme do contador.",
   "**Equipamento solar:** `--solar` acrescenta um inversor e um conjunto de baterias de dois módulos (quinze células cada, capacidades incluídas) ao longo de um dia rápido de 240 amostras, com um corte de energia ao fim do dia; as mensagens verificam-se contra o contrato solar do ARMOR-COMMON e entregam-se em `/api/v1/solar`."
  ],
  "note": "Opções, cenários e falhas completos: [utilização](docs/USAGE.md).",
  "fit": "O ARMOR-SIMULATOR é a forma de experimentar o resto da família sem hardware: faz de nó radar, de porta de ligação solar ou de nó elétrico e envia as suas mensagens para um [ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER), com falhas repetíveis, para que o [ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) e a aplicação móvel se vejam a funcionar com uma casa que não existe. Cada mensagem que faz é verificada contra os contratos do [ARMOR-COMMON](https://github.com/JuanenRac/ARMOR-COMMON).",
  "hardware": "Não se aplica: é o substituto do hardware, usado num computador",
  "requirements": [
   "Python 3.11+ (apenas a biblioteca padrão)"
  ]
 }
}
