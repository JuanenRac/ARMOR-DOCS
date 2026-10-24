# The facts that do not depend on the language, and the words of every language, of ARMOR-SERVER-AI.
# Copyright (C) 2026 JuanenRac (Electro Hobby 3D). GPL-3.0-or-later.

FACTS = {
 "emoji": "👁️",
 "status": [["software", "yellow"], ["tests", "green"], ["hardware", "yellow"], ["integration", "yellow"], ["docs", "green"]],
 "badges": [
  [
   "Language",
   "Python%203.11%2B",
   "3776ab"
  ],
  [
   "Target",
   "Jetson%20Orin%20NX",
   "76b900"
  ],
  [
   "Tests",
   "77%20passing",
   "2ea44f"
  ]
 ],
 "diagram": "",
 "build": "```powershell\n$env:PYTHONPATH=\"src\"\npython -m unittest discover -s tests   # 77 tests\necho '{\"label\":\"person\",\"confidence\":0.9,\"lux\":4,\"radar_tracks\":1}' | python -m armor_server_ai.cli\npython -m armor_server_ai.service --once   # one pass of the observation service\n```",
 "structure": "```text\nARMOR-SERVER-AI/\n├── src/armor_server_ai/   profile (day/night), policy (fusion), motion (movement and ignore zones), engine_registry, service (the observation service), cli\n├── tests/                 77 tests\n└── docs/                  INFERENCE_BOUNDARY.md, SERVICE.md\n```",
 "tests": "77 (`python -m unittest discover -s tests`)",
 "requirements": [
  "Python 3.11+",
  "optional: a Jetson Orin NX with TensorRT engines (not proven)"
 ]
}

TEXT = {
 "en": {
  "tagline": "Observation service: movement on the cameras weighed with the radars; it decides and explains, never actuates",
  "status": {"software": "The movement detector and the decision layer run as a service on the CM5 test bench, but there is no detection model yet: it cannot tell a person from a cat or a branch.", "tests": "77 tests pass (`python -m unittest discover -s tests`).", "hardware": "While the system is armed it looks at tiny grey frames of the real IP cameras of the CM5 test bench; nothing has run on a Jetson, with TensorRT or on a decoded RTSP stream.", "integration": "It reports movement weighed with the radars to the server of the CM5 test bench.", "docs": "Eight languages and the changelog are up to date."},
  "honest": "The decision layer and the movement detector are real and tested (77 tests), and the observation service **runs on the CM5 test bench**: while the system is armed it looks at tiny grey frames of the real IP cameras and reports movement weighed with the radars. It cannot tell a person from a cat or a branch: **there is no detection model yet**, and nothing has run on the Jetson, TensorRT or an RTSP stream decoded there.",
  "bullets": [
   "**The observation service:** `python -m armor_server_ai.service` is never called by the server (it asks the server, with its own token): while the system is **armed** it takes one tiny grey frame (64 x 36, from the camera's stream, never stored) of each camera every few seconds, measures how much of the picture moved and, when radar tracks agree, reports it to ARMOR-SERVER with its token.",
   "**Zones of the picture to ignore:** the server hands it the ignore zones of each camera and the pixels inside them count for nothing (a tree that waves, a road); a picture that is almost all ignored is not judged and at most sixteen zones count.",
   "**Day/night profile with hysteresis:** low-light below 30 lux, back to daylight only above 60 lux and never twice within 30 s, so dusk cannot make it flap.",
   "**Explainable fusion:** each detection or movement and the radar tracks give a severity (`ignore`, `review`, `high`) with the reasons behind it; strong movement **and** a radar track agree is `high`, weaker movement is a `review`.",
   "**Recommendations only:** a decision always carries `authorizes_action = false`. The central server authenticates and authorises every action.",
   "**Checksum-verified engines:** pre-built TensorRT engines are accepted only if present, non-empty and, with an `engines.json`, matching their SHA-256. Nothing is compiled or downloaded.",
   "**A service that says what is wrong:** it reports every new problem when it changes (`unreachable`, `unauthorized`…) and *the server answers again* when it is over; a JSONL worker keeps numbered, explained results and a bad line never stops the stream."
  ],
  "note": "See the [inference boundary](docs/INFERENCE_BOUNDARY.md) and the [service](docs/SERVICE.md).",
  "fit": "ARMOR-SERVER-AI is the part that watches the cameras for movement while the house is armed. It never acts: it tells [ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER) what it saw and why (movement and radar tracks agreeing is `high`), and the server decides what to do. A model that recognises a person, run on a Jetson, is the next step; [ARMOR-VISION](https://github.com/JuanenRac/ARMOR-VISION) holds the zones, masks and rules that model will use.",
  "hardware": "Running as a service on the CM5 test bench with the real IP cameras (movement only); nothing on a Jetson"
 },
 "es": {
  "tagline": "Servicio de observación: el movimiento en las cámaras sopesado con los radares; decide y explica, nunca actúa",
  "status": {"software": "El detector de movimiento y la capa de decisión funcionan como servicio en el banco de pruebas CM5, pero aún no hay modelo de detección: no distingue una persona de un gato o una rama.", "tests": "Pasan 77 pruebas (`python -m unittest discover -s tests`).", "hardware": "Mientras el sistema está armado mira fotogramas grises diminutos de las cámaras IP reales del banco de pruebas CM5; nada ha funcionado en una Jetson, con TensorRT ni sobre un flujo RTSP decodificado.", "integration": "Informa del movimiento ponderado con los radares al servidor del banco de pruebas.", "docs": "Ocho idiomas y el historial de cambios están al día."},
  "honest": "La capa de decisión y el detector de movimiento son reales y están probados (77 tests), y el servicio de observación **corre en el banco de pruebas de la CM5**: con el sistema armado mira pequeños fotogramas grises de las cámaras IP reales e informa del movimiento sopesado con los radares. No distingue a una persona de un gato o una rama: **todavía no hay modelo de detección**, y nada ha corrido en la Jetson, TensorRT ni un flujo RTSP decodificado allí.",
  "bullets": [
   "**El servicio de observación:** `python -m armor_server_ai.service` el servidor nunca lo llama (es él quien le pregunta al servidor, con su propio token): con el sistema **armado** toma un diminuto fotograma gris (64 x 36, del flujo de la cámara, nunca guardado) de cada cámara cada pocos segundos, mide cuánto de la imagen se movió y, cuando las pistas de radar coinciden, lo comunica a ARMOR-SERVER con su token.",
   "**Zonas de la imagen que se ignoran:** el servidor le da las zonas a ignorar de cada cámara y los píxeles dentro de ellas no cuentan (un árbol que se mueve, una carretera); una imagen casi toda ignorada no se juzga y cuentan como mucho dieciséis zonas.",
   "**Perfil día/noche con histéresis:** poca luz por debajo de 30 lux, vuelve a día solo por encima de 60 lux y nunca dos veces en 30 s, para que el crepúsculo no lo haga oscilar.",
   "**Fusión explicable:** cada detección o movimiento y las pistas de radar dan una gravedad (`ignore`, `review`, `high`) con las razones; movimiento fuerte **y** una pista de radar coincidente es `high`, un movimiento más débil es un `review`.",
   "**Solo recomendaciones:** una decisión siempre lleva `authorizes_action = false`. El servidor central autentica y autoriza cada acción.",
   "**Motores verificados por suma de comprobación:** los motores TensorRT precompilados solo se aceptan si existen, no están vacíos y, con un `engines.json`, coinciden con su SHA-256. No se compila ni descarga nada.",
   "**Un servicio que dice qué va mal:** informa de cada problema nuevo cuando cambia (`unreachable`, `unauthorized`…) y *el servidor responde otra vez* cuando termina; un trabajador JSONL guarda resultados numerados y explicados y una línea mala nunca detiene el flujo."
  ],
  "note": "Véanse el [límite de la inferencia](docs/INFERENCE_BOUNDARY.md) y el [servicio](docs/SERVICE.md).",
  "fit": "ARMOR-SERVER-AI es la parte que vigila el movimiento en las cámaras mientras la casa está armada. Nunca actúa: dice a [ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER) qué vio y por qué (movimiento y pistas de radar coincidentes es `high`), y el servidor decide qué hacer. Un modelo que reconozca a una persona, ejecutado en una Jetson, es el siguiente paso; [ARMOR-VISION](https://github.com/JuanenRac/ARMOR-VISION) guarda las zonas, máscaras y reglas que usará ese modelo.",
  "hardware": "Corriendo como servicio en el banco de pruebas de la CM5 con las cámaras IP reales (solo movimiento); nada en una Jetson",
  "requirements": [
   "Python 3.11+",
   "opcional: una Jetson Orin NX con motores TensorRT (sin probar)"
  ]
 },
 "fr": {
  "tagline": "Service d'observation : le mouvement sur les caméras pesé avec les radars ; il décide et explique, n'actionne jamais",
  "status": {"software": "Le détecteur de mouvement et la couche de décision tournent comme service sur le banc d'essai CM5, mais il n'y a pas encore de modèle de détection : il ne distingue pas une personne d'un chat ou d'une branche.", "tests": "77 tests réussissent (`python -m unittest discover -s tests`).", "hardware": "Tant que le système est armé, il regarde de minuscules images grises des vraies caméras IP du banc d'essai CM5 ; rien n'a tourné sur un Jetson, avec TensorRT ni sur un flux RTSP décodé.", "integration": "Il rend compte au serveur du banc d'essai du mouvement pondéré par les radars .", "docs": "Huit langues et le journal des modifications sont à jour."},
  "honest": "La couche de décision et le détecteur de mouvement sont réels et testés (77 tests), et le service d'observation **tourne sur le banc de test CM5** : système armé, il regarde de minuscules images grises des vraies caméras IP et signale le mouvement pesé avec les radars. Il ne distingue pas une personne d'un chat ou d'une branche : **il n'y a pas encore de modèle de détection**, et rien n'a tourné sur le Jetson, TensorRT ni un flux RTSP décodé là.",
  "bullets": [
   "**Le service d'observation :** `python -m armor_server_ai.service` n'est jamais appelé par le serveur (c'est lui qui interroge le serveur, avec son propre jeton) : système **armé**, il prend une minuscule image grise (64 x 36, du flux de la caméra, jamais stockée) de chaque caméra toutes les quelques secondes, mesure quelle part de l'image a bougé et, quand des pistes radar concordent, le signale à ARMOR-SERVER avec son jeton.",
   "**Zones de l'image à ignorer :** le serveur lui donne les zones à ignorer de chaque caméra et les pixels qu'elles contiennent ne comptent pas (un arbre qui bouge, une route) ; une image presque entièrement ignorée n'est pas jugée et seize zones au plus comptent.",
   "**Profil jour/nuit avec hystérésis :** faible lumière sous 30 lux, retour au jour seulement au-dessus de 60 lux et jamais deux fois en 30 s, pour que le crépuscule ne le fasse pas osciller.",
   "**Fusion explicable :** chaque détection ou mouvement et les pistes radar donnent une gravité (`ignore`, `review`, `high`) avec les raisons ; un mouvement fort **et** une piste radar concordante est `high`, un mouvement plus faible est un `review`.",
   "**Des recommandations seulement :** une décision porte toujours `authorizes_action = false`. Le serveur central authentifie et autorise chaque action.",
   "**Moteurs vérifiés par somme de contrôle :** les moteurs TensorRT précompilés ne sont acceptés que s'ils existent, ne sont pas vides et, avec un `engines.json`, correspondent à leur SHA-256. Rien n'est compilé ni téléchargé.",
   "**Un service qui dit ce qui ne va pas :** il signale chaque nouveau problème quand il change (`unreachable`, `unauthorized`…) et *le serveur répond de nouveau* quand c'est fini ; un travailleur JSONL garde des résultats numérotés et expliqués et une mauvaise ligne n'arrête jamais le flux."
  ],
  "note": "Voir la [frontière de l'inférence](docs/INFERENCE_BOUNDARY.md) et le [service](docs/SERVICE.md).",
  "fit": "ARMOR-SERVER-AI est la partie qui surveille le mouvement sur les caméras pendant que la maison est armée. Il n'agit jamais : il dit à [ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER) ce qu'il a vu et pourquoi (mouvement et pistes radar concordants valent `high`), et le serveur décide quoi faire. Un modèle qui reconnaît une personne, exécuté sur un Jetson, est l'étape suivante ; [ARMOR-VISION](https://github.com/JuanenRac/ARMOR-VISION) garde les zones, masques et règles que ce modèle utilisera.",
  "hardware": "Tourne comme service sur le banc de test CM5 avec les vraies caméras IP (mouvement seulement) ; rien sur un Jetson",
  "requirements": [
   "Python 3.11+",
   "facultatif : un Jetson Orin NX avec des moteurs TensorRT (non éprouvé)"
  ]
 },
 "it": {
  "tagline": "Servizio di osservazione: il movimento sulle telecamere pesato con i radar; decide e spiega, non aziona mai",
  "status": {"software": "Il rilevatore di movimento e il livello decisionale girano come servizio sul banco di prova CM5, ma non c'è ancora un modello di rilevamento: non distingue una persona da un gatto o da un ramo.", "tests": "Superano 77 test (`python -m unittest discover -s tests`).", "hardware": "Mentre il sistema è inserito guarda minuscoli fotogrammi grigi delle telecamere IP reali del banco di prova CM5; nulla ha girato su una Jetson, con TensorRT o su un flusso RTSP decodificato.", "integration": "Riferisce al server del banco di prova il movimento ponderato con i radar.", "docs": "Otto lingue e il registro delle modifiche sono aggiornati."},
  "honest": "Lo strato decisionale e il rilevatore di movimento sono reali e provati (77 test), e il servizio di osservazione **gira sul banco di prova CM5**: a sistema inserito guarda minuscoli fotogrammi grigi delle vere telecamere IP e riferisce il movimento pesato con i radar. Non distingue una persona da un gatto o da un ramo: **non c'è ancora un modello di rilevamento**, e nulla ha girato sul Jetson, TensorRT o su un flusso RTSP decodificato lì.",
  "bullets": [
   "**Il servizio di osservazione:** `python -m armor_server_ai.service` non viene mai chiamato dal server (è lui a interrogare il server, con il proprio token): a sistema **inserito** prende un minuscolo fotogramma grigio (64 x 36, dal flusso della telecamera, mai salvato) di ogni telecamera ogni pochi secondi, misura quanta parte dell'immagine si è mossa e, quando le tracce radar concordano, lo riferisce ad ARMOR-SERVER con il suo token.",
   "**Zone dell'immagine da ignorare:** il server gli dà le zone da ignorare di ogni telecamera e i pixel al loro interno non contano (un albero che si muove, una strada); un'immagine quasi tutta ignorata non è giudicata e contano al massimo sedici zone.",
   "**Profilo giorno/notte con isteresi:** poca luce sotto 30 lux, torna al giorno solo sopra 60 lux e mai due volte in 30 s, così il crepuscolo non lo fa oscillare.",
   "**Fusione spiegabile:** ogni rilevamento o movimento e le tracce radar danno una gravità (`ignore`, `review`, `high`) con le ragioni; movimento forte **e** una traccia radar concorde è `high`, un movimento più debole è una `review`.",
   "**Solo raccomandazioni:** una decisione porta sempre `authorizes_action = false`. Il server centrale autentica e autorizza ogni azione.",
   "**Motori verificati con checksum:** i motori TensorRT precompilati sono accettati solo se presenti, non vuoti e, con un `engines.json`, coincidenti con il loro SHA-256. Nulla è compilato né scaricato.",
   "**Un servizio che dice cosa non va:** riferisce ogni nuovo problema quando cambia (`unreachable`, `unauthorized`…) e *il server risponde di nuovo* quando è finito; un worker JSONL conserva risultati numerati e spiegati e una riga errata non ferma mai il flusso."
  ],
  "note": "Vedi il [confine dell'inferenza](docs/INFERENCE_BOUNDARY.md) e il [servizio](docs/SERVICE.md).",
  "fit": "ARMOR-SERVER-AI è la parte che sorveglia il movimento sulle telecamere mentre la casa è inserita. Non agisce mai: dice ad [ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER) cosa ha visto e perché (movimento e tracce radar concordi valgono `high`), e il server decide cosa fare. Un modello che riconosca una persona, eseguito su un Jetson, è il passo successivo; [ARMOR-VISION](https://github.com/JuanenRac/ARMOR-VISION) tiene le zone, le maschere e le regole che quel modello userà.",
  "hardware": "Gira come servizio sul banco di prova CM5 con le vere telecamere IP (solo movimento); nulla su un Jetson",
  "requirements": [
   "Python 3.11+",
   "facoltativo: un Jetson Orin NX con motori TensorRT (non provato)"
  ]
 },
 "de": {
  "tagline": "Beobachtungsdienst: Bewegung auf den Kameras, gegen die Radare abgewogen; er entscheidet und erklärt, schaltet nie",
  "status": {"software": "Der Bewegungsmelder und die Entscheidungsschicht laufen als Dienst auf dem CM5-Prüfstand, aber es gibt noch kein Erkennungsmodell: Er unterscheidet keine Person von einer Katze oder einem Ast.", "tests": "77 Tests bestehen (`python -m unittest discover -s tests`).", "hardware": "Solange das System scharf ist, betrachtet er winzige Graubilder der echten IP-Kameras des CM5-Prüfstands; nichts lief auf einem Jetson, mit TensorRT oder auf einem dekodierten RTSP-Strom.", "integration": "Er meldet die mit den Radaren gewichtete Bewegung an den Server des Prüfstands.", "docs": "Acht Sprachen und das Änderungsprotokoll sind aktuell."},
  "honest": "Die Entscheidungsschicht und der Bewegungsdetektor sind real und getestet (77 Tests), und der Beobachtungsdienst **läuft am CM5-Testaufbau**: Bei scharfem System sieht er winzige Graubilder der echten IP-Kameras an und meldet Bewegung, gegen die Radare abgewogen. Er kann eine Person nicht von einer Katze oder einem Ast unterscheiden: **Es gibt noch kein Erkennungsmodell**, und nichts lief auf dem Jetson, mit TensorRT oder einem dort dekodierten RTSP-Strom.",
  "bullets": [
   "**Der Beobachtungsdienst:** `python -m armor_server_ai.service` wird nie vom Server aufgerufen (er fragt den Server, mit seinem eigenen Token): Bei **scharfem** System nimmt er alle paar Sekunden ein winziges Graubild (64 x 36, aus dem Kamerastrom, nie gespeichert) jeder Kamera auf, misst, wie viel vom Bild sich bewegt hat, und meldet es, wenn Radarspuren übereinstimmen, mit seinem Token an ARMOR-SERVER.",
   "**Zu ignorierende Bildzonen:** der Server gibt ihm die zu ignorierenden Zonen jeder Kamera, und die Pixel darin zählen nicht (ein wehender Baum, eine Straße); ein fast ganz ignoriertes Bild wird nicht beurteilt, und höchstens sechzehn Zonen zählen.",
   "**Tag/Nacht-Profil mit Hysterese:** Dunkelheit unter 30 Lux, zurück zu Tageslicht erst über 60 Lux und nie zweimal innerhalb von 30 s, damit die Dämmerung es nicht flattern lässt.",
   "**Erklärbare Fusion:** jede Erkennung oder Bewegung und die Radarspuren ergeben eine Stufe (`ignore`, `review`, `high`) mit den Gründen; starke Bewegung **und** eine übereinstimmende Radarspur ist `high`, schwächere Bewegung ist `review`.",
   "**Nur Empfehlungen:** eine Entscheidung trägt immer `authorizes_action = false`. Der zentrale Server authentifiziert und autorisiert jede Aktion.",
   "**Per Prüfsumme verifizierte Engines:** vorgebaute TensorRT-Engines werden nur akzeptiert, wenn sie vorhanden, nicht leer und, mit einer `engines.json`, passend zu ihrem SHA-256 sind. Nichts wird kompiliert oder heruntergeladen.",
   "**Ein Dienst, der sagt, was falsch ist:** er meldet jedes neue Problem, wenn es sich ändert (`unreachable`, `unauthorized`…), und *der Server antwortet wieder*, wenn es vorbei ist; ein JSONL-Worker liefert nummerierte, erklärte Ergebnisse, und eine fehlerhafte Zeile stoppt nie den Strom."
  ],
  "note": "Siehe die [Inferenzgrenze](docs/INFERENCE_BOUNDARY.md) und den [Dienst](docs/SERVICE.md).",
  "fit": "ARMOR-SERVER-AI ist der Teil, der die Kameras auf Bewegung beobachtet, solange das Haus scharf ist. Er handelt nie: Er sagt [ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER), was er gesehen hat und warum (übereinstimmende Bewegung und Radarspuren ergeben `high`), und der Server entscheidet, was zu tun ist. Ein Modell, das eine Person erkennt, auf einem Jetson ausgeführt, ist der nächste Schritt; [ARMOR-VISION](https://github.com/JuanenRac/ARMOR-VISION) hält die Zonen, Masken und Regeln, die dieses Modell nutzen wird.",
  "hardware": "Läuft als Dienst am CM5-Testaufbau mit den echten IP-Kameras (nur Bewegung); nichts auf einem Jetson",
  "requirements": [
   "Python 3.11+",
   "optional: ein Jetson Orin NX mit TensorRT-Engines (nicht erprobt)"
  ]
 },
 "zh": {
  "tagline": "观察服务：把摄像头上的移动与雷达对照权衡；它做出决定并给出解释，从不执行动作",
  "status": {"software": "移动检测器和决策层在 CM5 测试台上作为服务运行，但目前还没有检测模型：它分不清人、猫或树枝。", "tests": "77 项测试通过（`python -m unittest discover -s tests`）。", "hardware": "系统布防期间，它查看 CM5 测试台上真实 IP 摄像头的微小灰度画面；还没有在 Jetson、TensorRT 或解码后的 RTSP 流上运行过。", "integration": "它把结合雷达加权后的移动情况报告给测试台的服务器。", "docs": "八种语言和更新日志均为最新。"},
  "honest": "决策层和移动检测器是真实的并经过测试（77 个测试），观察服务**在 CM5 测试台上运行**：系统布防时，它查看真实 IP 摄像头的微小灰度帧，并报告与雷达对照权衡后的移动。它分不清人、猫或树枝：**目前还没有检测模型**，也没有任何东西在 Jetson、TensorRT 或在那里解码的 RTSP 流上运行过。",
  "bullets": [
   "**观察服务：**`python -m armor_server_ai.service` 服务器从不调用它（是它用自己的令牌向服务器询问）：系统**布防**时，它每隔几秒从每个摄像头的码流取一帧微小的灰度图（64 x 36，从不保存），测量画面移动了多少，当雷达轨迹一致时，带着自己的令牌上报给 ARMOR-SERVER。",
   "**要忽略的画面区域：**服务器把每个摄像头的忽略区域交给它，区域内的像素不计入（摇动的树、公路）；几乎全被忽略的画面不做判断，最多计入十六个区域。",
   "**带滞回的昼夜配置：**低于 30 勒克斯为弱光，只有高于 60 勒克斯才回到白天，且 30 秒内绝不切换两次，因此黄昏不会让它来回抖动。",
   "**可解释的融合：**每次检测或移动与雷达轨迹给出一个严重级别（`ignore`、`review`、`high`）及理由；强移动**并且**有一致的雷达轨迹为 `high`，较弱的移动为 `review`。",
   "**只是建议：**决定总是带有 `authorizes_action = false`。中央服务器对每个动作进行认证和授权。",
   "**经校验和验证的引擎：**预先构建的 TensorRT 引擎只有在存在、非空，并且（有 `engines.json` 时）SHA-256 匹配时才会被接受。不会编译或下载任何东西。",
   "**会说明出了什么问题的服务：**每个新问题变化时都会报告（`unreachable`、`unauthorized`……），结束时会说明*服务器又有应答了*；JSONL 工作进程保留编号并带解释的结果，坏的一行绝不会中断数据流。"
  ],
  "note": "参见[推理边界](docs/INFERENCE_BOUNDARY.md)和[服务](docs/SERVICE.md)。",
  "fit": "ARMOR-SERVER-AI 是在住宅布防时观察摄像头移动的部分。它从不行动：它告诉 [ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER) 它看到了什么以及原因（移动与雷达轨迹一致即为 `high`），由服务器决定怎么做。下一步是在 Jetson 上运行能识别人的模型；[ARMOR-VISION](https://github.com/JuanenRac/ARMOR-VISION) 保存该模型将使用的区域、遮罩和规则。",
  "hardware": "在 CM5 测试台上用真实 IP 摄像头作为服务运行（仅移动）；Jetson 上没有任何东西",
  "requirements": [
   "Python 3.11+",
   "可选：带 TensorRT 引擎的 Jetson Orin NX（未经验证）"
  ]
 },
 "ja": {
  "tagline": "観察サービス：カメラ上の動きをレーダーと照らし合わせます。判断して説明するだけで、決して動作させません",
  "status": {"software": "動き検出と判断の層は CM5 テストベンチ上でサービスとして動いていますが、検出モデルはまだありません。人と猫や枝の区別はできません。", "tests": "77 件のテストが通ります（`python -m unittest discover -s tests`）。", "hardware": "警戒中は、CM5 テストベンチの実際の IP カメラの小さなグレー画像を見ています。Jetson、TensorRT、デコードした RTSP ストリームではまだ何も動かしていません。", "integration": "レーダーと照合した動きの結果をテストベンチのサーバーに報告します。", "docs": "8 言語と変更履歴は最新です。"},
  "honest": "判断レイヤーと動き検出器は実在し、テストされています（77 件）。観察サービスは **CM5 テストベンチで動作**しており、システムの警戒中に実際の IP カメラの小さなグレーフレームを見て、レーダーと照らし合わせた動きを報告します。人と猫や枝の区別はできません。**検出モデルはまだなく**、Jetson、TensorRT、そこでデコードした RTSP ストリームでは何も動いていません。",
  "bullets": [
   "**観察サービス：**`python -m armor_server_ai.service` はサーバーから呼び出されることはなく（自分のトークンでサーバーに問い合わせます）、システムが**警戒中**のあいだ、数秒ごとに各カメラのストリームから小さなグレーフレーム（64 x 36、保存しない）を 1 枚取り、画面のどれだけが動いたかを測り、レーダーの軌跡と一致すれば、自分のトークンで ARMOR-SERVER に報告します。",
   "**無視する映像ゾーン：**サーバーが各カメラの無視ゾーンを渡し、その中のピクセルは数えません（揺れる木、道路）。ほとんどが無視される画像は判断せず、数えるゾーンは最大 16 個です。",
   "**ヒステリシス付きの昼夜プロファイル：**30 ルクス未満で低照度、60 ルクスを超えたときだけ昼に戻り、30 秒以内に 2 度は切り替えないため、夕暮れでばたつきません。",
   "**説明できる融合：**検出や動きとレーダーの軌跡から、理由付きで重大度（`ignore`、`review`、`high`）を出します。強い動き**かつ**一致するレーダーの軌跡は `high`、弱い動きは `review` です。",
   "**推奨のみ：**判断には常に `authorizes_action = false` が付きます。中央サーバーがすべての動作を認証・認可します。",
   "**チェックサムで検証されるエンジン：**ビルド済みの TensorRT エンジンは、存在し、空でなく、`engines.json` があればその SHA-256 と一致するときだけ受け付けます。何もコンパイルもダウンロードもしません。",
   "**何が悪いかを伝えるサービス：**新しい問題が変わるたびに報告し（`unreachable`、`unauthorized` など）、終われば*サーバーがまた応答する*と伝えます。JSONL ワーカーは番号付きで説明付きの結果を保ち、不正な行がストリームを止めることはありません。"
  ],
  "note": "[推論の境界](docs/INFERENCE_BOUNDARY.md)と[サービス](docs/SERVICE.md)を参照してください。",
  "fit": "ARMOR-SERVER-AI は家が警戒中にカメラの動きを見張る部分です。決して動作せず、何を見たかとその理由（動きとレーダーの軌跡が一致すれば `high`）を [ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER) に伝え、サーバーが何をするかを決めます。次の段階は、Jetson で動く人を認識するモデルで、[ARMOR-VISION](https://github.com/JuanenRac/ARMOR-VISION) がそのモデルが使うゾーン、マスク、ルールを保持します。",
  "hardware": "CM5 テストベンチで実際の IP カメラとともにサービスとして動作（動きのみ）。Jetson 上では何もありません",
  "requirements": [
   "Python 3.11+",
   "任意：TensorRT エンジンを載せた Jetson Orin NX（未検証）"
  ]
 },
 "pt": {
  "tagline": "Serviço de observação: o movimento nas câmaras pesado com os radares; decide e explica, nunca aciona",
  "status": {"software": "O detetor de movimento e a camada de decisão funcionam como serviço na bancada de testes CM5, mas ainda não há modelo de deteção: não distingue uma pessoa de um gato ou de um ramo.", "tests": "Passam 77 testes (`python -m unittest discover -s tests`).", "hardware": "Enquanto o sistema está armado, olha para pequenas imagens cinzentas das câmaras IP reais da bancada de testes CM5; nada funcionou num Jetson, com TensorRT ou sobre um fluxo RTSP descodificado.", "integration": "Reporta ao servidor da bancada de testes o movimento ponderado com os radares.", "docs": "Oito idiomas e o registo de alterações estão atualizados."},
  "honest": "A camada de decisão e o detetor de movimento são reais e estão testados (77 testes), e o serviço de observação **corre na bancada de testes do CM5**: com o sistema armado olha para pequenas imagens cinzentas das câmaras IP reais e comunica o movimento pesado com os radares. Não distingue uma pessoa de um gato ou de um ramo: **ainda não há modelo de deteção**, e nada correu no Jetson, no TensorRT nem num fluxo RTSP descodificado aí.",
  "bullets": [
   "**O serviço de observação:** `python -m armor_server_ai.service` nunca é chamado pelo servidor (é ele que pergunta ao servidor, com o seu próprio token): com o sistema **armado** tira uma pequena imagem cinzenta (64 x 36, do fluxo da câmara, nunca guardada) de cada câmara de poucos em poucos segundos, mede quanto da imagem se moveu e, quando as pistas de radar coincidem, comunica-o ao ARMOR-SERVER com o seu token.",
   "**Zonas da imagem a ignorar:** o servidor dá-lhe as zonas a ignorar de cada câmara e os píxeis dentro delas não contam (uma árvore que se mexe, uma estrada); uma imagem quase toda ignorada não é julgada e contam no máximo dezasseis zonas.",
   "**Perfil dia/noite com histerese:** pouca luz abaixo de 30 lux, volta ao dia só acima de 60 lux e nunca duas vezes em 30 s, para que o crepúsculo não o faça oscilar.",
   "**Fusão explicável:** cada deteção ou movimento e as pistas de radar dão uma gravidade (`ignore`, `review`, `high`) com as razões; movimento forte **e** uma pista de radar coincidente é `high`, um movimento mais fraco é um `review`.",
   "**Só recomendações:** uma decisão leva sempre `authorizes_action = false`. O servidor central autentica e autoriza cada ação.",
   "**Motores verificados por soma de verificação:** os motores TensorRT pré-compilados só são aceites se existirem, não estiverem vazios e, com um `engines.json`, coincidirem com o seu SHA-256. Nada é compilado nem descarregado.",
   "**Um serviço que diz o que está mal:** comunica cada novo problema quando muda (`unreachable`, `unauthorized`…) e *o servidor responde outra vez* quando acaba; um trabalhador JSONL guarda resultados numerados e explicados e uma linha má nunca para o fluxo."
  ],
  "note": "Veja o [limite da inferência](docs/INFERENCE_BOUNDARY.md) e o [serviço](docs/SERVICE.md).",
  "fit": "O ARMOR-SERVER-AI é a parte que vigia o movimento nas câmaras enquanto a casa está armada. Nunca age: diz ao [ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER) o que viu e porquê (movimento e pistas de radar coincidentes é `high`), e o servidor decide o que fazer. Um modelo que reconheça uma pessoa, executado num Jetson, é o passo seguinte; o [ARMOR-VISION](https://github.com/JuanenRac/ARMOR-VISION) guarda as zonas, máscaras e regras que esse modelo usará.",
  "hardware": "A correr como serviço na bancada de testes do CM5 com as câmaras IP reais (só movimento); nada num Jetson",
  "requirements": [
   "Python 3.11+",
   "opcional: um Jetson Orin NX com motores TensorRT (não comprovado)"
  ]
 }
}
