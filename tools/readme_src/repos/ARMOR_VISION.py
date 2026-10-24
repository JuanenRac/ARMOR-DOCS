# The facts that do not depend on the language, and the words of every language, of ARMOR-VISION.
# Copyright (C) 2026 JuanenRac (Electro Hobby 3D). GPL-3.0-or-later.

FACTS = {
 "emoji": "👁️",
 "status": [["software", "yellow"], ["tests", "green"], ["hardware", "red"], ["docs", "green"]],
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
   "61%20passing",
   "2ea44f"
  ]
 ],
 "diagram": "",
 "build": "```powershell\n$env:PYTHONPATH=\"src\"\npython -m armor_vision simulate --mode away\npython -m armor_vision check-config my_cameras.json\npython -m unittest discover -s tests   # 61 tests\n```\n\n```bash\nPYTHONPATH=src python -m armor_vision simulate --mode away\nPYTHONPATH=src python -m armor_vision check-config my_cameras.json\nPYTHONPATH=src python -m unittest discover -s tests   # 61 tests\n```",
 "structure": "```text\nARMOR-VISION/\n├── src/armor_vision/   geometry, config (zones, masks, profiles), motion, tracker, rules, detector, pipeline, cli\n├── tests/              61 tests\n└── docs/USAGE.md\n```",
 "tests": "61 (`python -m unittest discover -s tests`)",
 "requirements": [
  "Python 3.11+ (standard library only)"
 ]
}

TEXT = {
 "en": {
  "tagline": "Zones, masks and detection rules for the cameras",
  "status": {"software": "The zones, the motion check, the tracker and the rules work, but there is no real detector model yet: the simulation uses scripted detections.", "tests": "61 tests pass (`python -m unittest discover -s tests`).", "hardware": "Nothing has run on a camera or on the Jetson Orin NX.", "docs": "Eight languages and the changelog are up to date."},
  "honest": "The zones, the motion check, the tracker, the rules and the 61 tests are real. There is **no real detector model yet** and nothing has run on a camera or on the Jetson Orin NX: the simulation uses scripted detections.",
  "bullets": [
   "**Zones and masks:** polygons drawn on normalised coordinates (0 to 1), so one drawing works at any resolution; a zone counts detections, a mask ignores movement. Each zone has a label filter, a kind (`alert` or `detection`) and an inertia in pictures and seconds.",
   "**Motion first:** the expensive detector runs only when enough of the picture, outside the masks, has changed.",
   "**A tracker:** each object keeps its identity between pictures, and what stands still (a parked car) is remembered and makes no new events.",
   "**Arming profiles:** `away`, `home` and the like choose which zones are watched; an unknown mode watches everything.",
   "**Events that only report:** an alert or a detection always carries `authorizes_action: false`; the server decides what to do."
  ],
  "note": "Options and the configuration format: [usage](docs/USAGE.md).",
  "fit": "ARMOR-VISION is the part that decides what a camera's picture means, apart from any detector: the zones and masks drawn on it, the motion check that runs before the expensive detector, the tracker, the arming profiles and the rules that turn detections into events. [ARMOR-SERVER-AI](https://github.com/JuanenRac/ARMOR-SERVER-AI) is the service that watches the cameras today; ARMOR-VISION is where the rules for a real detection model are ready, waiting for it. It only reports: the events never authorise an action.",
  "hardware": "None yet: no real detector, camera or Jetson (a simulation with scripted detections)"
 },
 "es": {
  "tagline": "Zonas, máscaras y reglas de detección para las cámaras",
  "status": {"software": "Las zonas, la comprobación de movimiento, el seguimiento y las reglas funcionan, pero aún no hay un modelo detector real: la simulación usa detecciones guionizadas.", "tests": "Pasan 61 pruebas (`python -m unittest discover -s tests`).", "hardware": "Nada ha funcionado en una cámara ni en la Jetson Orin NX.", "docs": "Ocho idiomas y el historial de cambios están al día."},
  "honest": "Las zonas, la comprobación de movimiento, el seguimiento, las reglas y los 61 tests son reales. **Todavía no existe un modelo de detección real** y nada se ha ejecutado en una cámara ni en la Jetson Orin NX: la simulación usa detecciones guionizadas.",
  "bullets": [
   "**Zonas y máscaras:** polígonos dibujados en coordenadas normalizadas (de 0 a 1), así un mismo dibujo vale a cualquier resolución; una zona cuenta detecciones, una máscara ignora el movimiento. Cada zona tiene un filtro de etiquetas, un tipo (`alert` o `detection`) y una inercia en fotogramas y segundos.",
   "**Primero el movimiento:** el detector, que es caro, solo se ejecuta cuando ha cambiado lo bastante de la imagen fuera de las máscaras.",
   "**Un seguimiento:** cada objeto conserva su identidad entre imágenes, y lo que está quieto (un coche aparcado) se recuerda y no genera eventos nuevos.",
   "**Perfiles de armado:** `away`, `home` y similares eligen qué zonas se vigilan; un modo desconocido vigila todo.",
   "**Eventos que solo informan:** una alerta o una detección lleva siempre `authorizes_action: false`; el servidor decide qué hacer."
  ],
  "note": "Opciones y formato de la configuración: [uso](docs/USAGE.md).",
  "fit": "ARMOR-VISION es la parte que decide qué significa la imagen de una cámara, al margen de cualquier detector: las zonas y máscaras dibujadas sobre ella, la comprobación de movimiento que corre antes del detector costoso, el seguidor, los perfiles de armado y las reglas que convierten detecciones en eventos. [ARMOR-SERVER-AI](https://github.com/JuanenRac/ARMOR-SERVER-AI) es el servicio que vigila hoy las cámaras; ARMOR-VISION es donde las reglas para un modelo de detección real están listas, esperándolo. Solo informa: los eventos nunca autorizan una acción.",
  "hardware": "Ninguno todavía: ni detector real, ni cámara ni Jetson (una simulación con detecciones guionizadas)",
  "requirements": [
   "Python 3.11+ (solo la biblioteca estándar)"
  ]
 },
 "fr": {
  "tagline": "Zones, masques et règles de détection pour les caméras",
  "status": {"software": "Les zones, le contrôle du mouvement, le suivi et les règles fonctionnent, mais il n'y a pas encore de vrai modèle détecteur : la simulation utilise des détections scénarisées.", "tests": "61 tests réussissent (`python -m unittest discover -s tests`).", "hardware": "Rien n'a tourné sur une caméra ni sur le Jetson Orin NX.", "docs": "Huit langues et le journal des modifications sont à jour."},
  "honest": "Les zones, le contrôle du mouvement, le suivi, les règles et les 61 tests sont réels. **Il n'existe pas encore de vrai modèle de détection** et rien n'a tourné sur une caméra ni sur la Jetson Orin NX : la simulation utilise des détections scénarisées.",
  "bullets": [
   "**Zones et masques :** des polygones dessinés en coordonnées normalisées (de 0 à 1), un même dessin sert donc à toute résolution ; une zone compte les détections, un masque ignore le mouvement. Chaque zone a un filtre d'étiquettes, un type (`alert` ou `detection`) et une inertie en images et en secondes.",
   "**D'abord le mouvement :** le détecteur, coûteux, ne s'exécute que lorsque assez de l'image a changé en dehors des masques.",
   "**Un suivi :** chaque objet garde son identité d'une image à l'autre, et ce qui reste immobile (une voiture garée) est mémorisé et ne produit pas de nouveaux événements.",
   "**Profils d'armement :** `away`, `home` et similaires choisissent les zones surveillées ; un mode inconnu surveille tout.",
   "**Des événements qui informent seulement :** une alerte ou une détection porte toujours `authorizes_action: false` ; le serveur décide quoi faire."
  ],
  "note": "Options et format de la configuration : [usage](docs/USAGE.md).",
  "fit": "ARMOR-VISION est la partie qui décide de ce que signifie l'image d'une caméra, indépendamment de tout détecteur : les zones et masques dessinés dessus, le contrôle de mouvement qui s'exécute avant le détecteur coûteux, le suiveur, les profils d'armement et les règles qui transforment des détections en événements. [ARMOR-SERVER-AI](https://github.com/JuanenRac/ARMOR-SERVER-AI) est le service qui surveille les caméras aujourd'hui ; ARMOR-VISION est l'endroit où les règles pour un vrai modèle de détection sont prêtes, en l'attendant. Il ne fait que rapporter : les événements n'autorisent jamais une action.",
  "hardware": "Aucun pour l'instant : ni détecteur réel, ni caméra, ni Jetson (une simulation avec des détections scriptées)",
  "requirements": [
   "Python 3.11+ (bibliothèque standard uniquement)"
  ]
 },
 "it": {
  "tagline": "Zone, maschere e regole di rilevamento per le telecamere",
  "status": {"software": "Le zone, il controllo del movimento, il tracciamento e le regole funzionano, ma non c'è ancora un vero modello di rilevamento: la simulazione usa rilevamenti da script.", "tests": "Superano 61 test (`python -m unittest discover -s tests`).", "hardware": "Nulla ha girato su una telecamera né sulla Jetson Orin NX.", "docs": "Otto lingue e il registro delle modifiche sono aggiornati."},
  "honest": "Le zone, il controllo del movimento, il tracciamento, le regole e i 61 test sono reali. **Non esiste ancora un vero modello di rilevamento** e nulla è stato eseguito su una telecamera o sulla Jetson Orin NX: la simulazione usa rilevamenti scriptati.",
  "bullets": [
   "**Zone e maschere:** poligoni disegnati in coordinate normalizzate (da 0 a 1), così lo stesso disegno vale a qualsiasi risoluzione; una zona conta i rilevamenti, una maschera ignora il movimento. Ogni zona ha un filtro di etichette, un tipo (`alert` o `detection`) e un'inerzia in immagini e secondi.",
   "**Prima il movimento:** il rilevatore, costoso, viene eseguito solo quando è cambiata abbastanza immagine fuori dalle maschere.",
   "**Un tracciamento:** ogni oggetto mantiene la sua identità da un'immagine all'altra, e ciò che sta fermo (un'auto parcheggiata) viene ricordato e non genera nuovi eventi.",
   "**Profili di inserimento:** `away`, `home` e simili scelgono quali zone sono sorvegliate; una modalità sconosciuta sorveglia tutto.",
   "**Eventi che informano soltanto:** un allarme o un rilevamento porta sempre `authorizes_action: false`; il server decide cosa fare."
  ],
  "note": "Opzioni e formato della configurazione: [uso](docs/USAGE.md).",
  "fit": "ARMOR-VISION è la parte che decide cosa significa l'immagine di una telecamera, a prescindere da qualsiasi rilevatore: le zone e le maschere disegnate su di essa, il controllo di movimento che gira prima del rilevatore costoso, il tracker, i profili di inserimento e le regole che trasformano i rilevamenti in eventi. [ARMOR-SERVER-AI](https://github.com/JuanenRac/ARMOR-SERVER-AI) è il servizio che oggi sorveglia le telecamere; ARMOR-VISION è dove le regole per un vero modello di rilevamento sono pronte, in attesa. Si limita a riferire: gli eventi non autorizzano mai un'azione.",
  "hardware": "Ancora nessuno: né rilevatore reale, né telecamera, né Jetson (una simulazione con rilevamenti scriptati)",
  "requirements": [
   "Python 3.11+ (solo la libreria standard)"
  ]
 },
 "de": {
  "tagline": "Zonen, Masken und Erkennungsregeln für die Kameras",
  "status": {"software": "Die Zonen, die Bewegungsprüfung, die Verfolgung und die Regeln funktionieren, aber es gibt noch kein echtes Erkennungsmodell: Die Simulation nutzt geskriptete Erkennungen.", "tests": "61 Tests bestehen (`python -m unittest discover -s tests`).", "hardware": "Nichts lief an einer Kamera oder auf dem Jetson Orin NX.", "docs": "Acht Sprachen und das Änderungsprotokoll sind aktuell."},
  "honest": "Die Zonen, die Bewegungsprüfung, die Verfolgung, die Regeln und die 61 Tests sind real. Es gibt **noch kein echtes Erkennungsmodell**, und nichts lief auf einer Kamera oder auf dem Jetson Orin NX: die Simulation nutzt vorgegebene Erkennungen.",
  "bullets": [
   "**Zonen und Masken:** Polygone in normalisierten Koordinaten (0 bis 1), eine Zeichnung gilt also bei jeder Auflösung; eine Zone zählt Erkennungen, eine Maske ignoriert Bewegung. Jede Zone hat einen Label-Filter, eine Art (`alert` oder `detection`) und eine Trägheit in Bildern und Sekunden.",
   "**Zuerst die Bewegung:** der teure Detektor läuft nur, wenn sich außerhalb der Masken genug vom Bild verändert hat.",
   "**Eine Verfolgung:** jedes Objekt behält seine Identität von Bild zu Bild, und was stillsteht (ein geparktes Auto), wird gemerkt und erzeugt keine neuen Ereignisse.",
   "**Scharfschaltprofile:** `away`, `home` und ähnliche wählen, welche Zonen überwacht werden; ein unbekannter Modus überwacht alles.",
   "**Ereignisse, die nur melden:** ein Alarm oder eine Erkennung trägt immer `authorizes_action: false`; der Server entscheidet, was zu tun ist."
  ],
  "note": "Optionen und Format der Konfiguration: [Nutzung](docs/USAGE.md).",
  "fit": "ARMOR-VISION ist der Teil, der entscheidet, was das Bild einer Kamera bedeutet, unabhängig von jedem Detektor: die darauf gezeichneten Zonen und Masken, die Bewegungsprüfung, die vor dem teuren Detektor läuft, der Tracker, die Scharfschaltprofile und die Regeln, die Erkennungen zu Ereignissen machen. [ARMOR-SERVER-AI](https://github.com/JuanenRac/ARMOR-SERVER-AI) ist der Dienst, der heute die Kameras beobachtet; ARMOR-VISION ist der Ort, an dem die Regeln für ein echtes Erkennungsmodell bereitliegen und darauf warten. Es meldet nur: Die Ereignisse autorisieren nie eine Aktion.",
  "hardware": "Noch keiner: weder echter Detektor noch Kamera noch Jetson (eine Simulation mit geskripteten Erkennungen)",
  "requirements": [
   "Python 3.11+ (nur die Standardbibliothek)"
  ]
 },
 "zh": {
  "tagline": "摄像头的区域、遮罩与检测规则",
  "status": {"software": "防区、移动检查、跟踪器和规则都能工作，但目前还没有真实的检测模型：模拟使用的是脚本化的检测结果。", "tests": "61 项测试通过（`python -m unittest discover -s tests`）。", "hardware": "还没有在摄像头或 Jetson Orin NX 上运行过。", "docs": "八种语言和更新日志均为最新。"},
  "honest": "区域、运动检查、跟踪、规则和 61 个测试都是真实的。**目前还没有真正的检测模型**，也没有在任何摄像头或 Jetson Orin NX 上运行过：模拟使用的是预设的检测结果。",
  "bullets": [
   "**区域与遮罩：** 用归一化坐标（0 到 1）绘制的多边形，因此同一张图在任何分辨率下都适用；区域统计检测结果，遮罩忽略运动。每个区域有标签过滤、类型（`alert` 或 `detection`）以及以帧数和秒数表示的惰性。",
   "**先看运动：** 只有当遮罩之外的画面变化足够多时，开销很大的检测器才会运行。",
   "**跟踪：** 每个物体在画面之间保持身份，静止的物体（停着的汽车）会被记住，不再产生新事件。",
   "**布防配置：** `away`、`home` 等决定监视哪些区域；未知模式则监视全部。",
   "**只报告的事件：** 告警或检测始终带有 `authorizes_action: false`；做什么由服务器决定。"
  ],
  "note": "选项与配置格式：[用法](docs/USAGE.md)。",
  "fit": "ARMOR-VISION 是独立于任何检测器、决定摄像头画面含义的部分：画在上面的区域和遮罩、先于昂贵检测器运行的移动检查、跟踪器、布防配置，以及把检测变成事件的规则。如今观察摄像头的是 [ARMOR-SERVER-AI](https://github.com/JuanenRac/ARMOR-SERVER-AI) 服务；ARMOR-VISION 则为真正的检测模型准备好了规则，等待它的到来。它只报告：事件从不授权任何动作。",
  "hardware": "暂无：没有真实的检测器、摄像头或 Jetson（使用脚本化检测的模拟）",
  "requirements": [
   "Python 3.11+（仅标准库）"
  ]
 },
 "ja": {
  "tagline": "カメラのゾーン、マスク、検知ルール",
  "status": {"software": "ゾーン、動きの確認、トラッカー、規則は動作しますが、実際の検出モデルはまだありません。シミュレーションはスクリプト化した検出結果を使います。", "tests": "61 件のテストが通ります（`python -m unittest discover -s tests`）。", "hardware": "カメラや Jetson Orin NX ではまだ何も動かしていません。", "docs": "8 言語と変更履歴は最新です。"},
  "honest": "ゾーン、動きの確認、追跡、ルール、61 件のテストは実在します。**実際の検知モデルはまだありません**。カメラや Jetson Orin NX では何も動かしていません。シミュレーションは台本どおりの検知結果を使います。",
  "bullets": [
   "**ゾーンとマスク:** 正規化座標（0 から 1）で描いた多角形なので、同じ図がどの解像度でも使えます。ゾーンは検知を数え、マスクは動きを無視します。各ゾーンにはラベルのフィルター、種類（`alert` または `detection`）、画像数と秒数の慣性があります。",
   "**まず動き:** 高価な検知器は、マスクの外で画面が十分に変化したときだけ動きます。",
   "**追跡:** 各物体は画像間で同一性を保ち、止まっているもの（駐車中の車）は記憶されて新しいイベントを出しません。",
   "**警戒プロファイル:** `away`、`home` などが監視するゾーンを選びます。未知のモードはすべてを監視します。",
   "**報告するだけのイベント:** 警報や検知には常に `authorizes_action: false` が付き、何をするかはサーバーが決めます。"
  ],
  "note": "オプションと設定の形式: [使い方](docs/USAGE.md)。",
  "fit": "ARMOR-VISION は、検出器とは別に、カメラの映像が何を意味するかを決める部分です。映像に描くゾーンとマスク、高価な検出器の前に走る動き検査、トラッカー、警戒プロファイル、検出をイベントに変えるルール。現在カメラを見張っているのは [ARMOR-SERVER-AI](https://github.com/JuanenRac/ARMOR-SERVER-AI) で、ARMOR-VISION は実際の検出モデルのためのルールを用意して待っています。報告するだけで、イベントが動作を認可することはありません。",
  "hardware": "まだありません：実際の検出器、カメラ、Jetson はなく、スクリプト化した検出によるシミュレーションのみ",
  "requirements": [
   "Python 3.11+（標準ライブラリのみ）"
  ]
 },
 "pt": {
  "tagline": "Zonas, máscaras e regras de deteção para as câmaras",
  "status": {"software": "As zonas, a verificação de movimento, o seguimento e as regras funcionam, mas ainda não há um modelo detetor real: a simulação usa deteções com guião.", "tests": "Passam 61 testes (`python -m unittest discover -s tests`).", "hardware": "Nada funcionou numa câmara nem no Jetson Orin NX.", "docs": "Oito idiomas e o registo de alterações estão atualizados."},
  "honest": "As zonas, a verificação de movimento, o seguidor, as regras e os 61 testes são reais. **Ainda não há nenhum modelo detetor real** e nada correu numa câmara nem no Jetson Orin NX: a simulação usa deteções com guião.",
  "bullets": [
   "**Zonas e máscaras:** polígonos desenhados em coordenadas normalizadas (0 a 1), para que um só desenho funcione em qualquer resolução; uma zona conta deteções, uma máscara ignora o movimento. Cada zona tem um filtro de etiquetas, um tipo (`alert` ou `detection`) e uma inércia em imagens e segundos.",
   "**Primeiro o movimento:** o detetor caro só corre quando mudou o suficiente da imagem, fora das máscaras.",
   "**Um seguidor:** cada objeto mantém a sua identidade entre imagens, e o que está parado (um carro estacionado) é lembrado e não gera eventos novos.",
   "**Perfis de armação:** `away`, `home` e semelhantes escolhem que zonas se vigiam; um modo desconhecido vigia tudo.",
   "**Eventos que só reportam:** um alerta ou uma deteção leva sempre `authorizes_action: false`; o servidor decide o que fazer."
  ],
  "note": "Opções e formato de configuração: [utilização](docs/USAGE.md).",
  "fit": "O ARMOR-VISION é a parte que decide o que significa a imagem de uma câmara, à parte de qualquer detetor: as zonas e máscaras desenhadas nela, a verificação de movimento que corre antes do detetor dispendioso, o seguidor, os perfis de armar e as regras que transformam deteções em eventos. O [ARMOR-SERVER-AI](https://github.com/JuanenRac/ARMOR-SERVER-AI) é o serviço que hoje vigia as câmaras; o ARMOR-VISION é onde as regras para um modelo de deteção real estão prontas, à sua espera. Só comunica: os eventos nunca autorizam uma ação.",
  "hardware": "Nenhum ainda: nem detetor real, nem câmara, nem Jetson (uma simulação com deteções guionizadas)",
  "requirements": [
   "Python 3.11+ (apenas a biblioteca padrão)"
  ]
 }
}
