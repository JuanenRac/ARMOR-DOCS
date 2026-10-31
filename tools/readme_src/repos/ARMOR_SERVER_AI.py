# The facts that do not depend on the language, and the words of every language, of ARMOR-SERVER-AI, in the universal README layout.
# Copyright (C) 2026 JuanenRac (Electro Hobby 3D). GPL-3.0-or-later.
from readme_src._kit import *  # noqa: F401,F403

FACTS = {'emoji': '👁️',
 'layout': 'universal',
 'license_badge': 'License-GPL%203.0--or--later-blue',
 'status': [['software', 'yellow'], ['tests', 'green'], ['hardware', 'yellow'], ['integration', 'yellow'], ['docs', 'green']],
 'badges': [['Language', 'Python%203.11%2B', '3776ab'], ['Target', 'Jetson%20Orin%20NX', '76b900'], ['Tests', '80%20passing', '2ea44f']]}

# the sentences of the previous layout that the new one keeps (already written in the eight languages)
LEGACY = {'en': {'tagline': 'Observation service: movement on the cameras weighed with the radars; it decides and explains, never actuates',
        'status': {'software': 'The movement detector and the decision layer run as a service on the CM5 test bench, but there is no detection model yet: it cannot tell '
                               'a person from a cat or a branch.',
                   'tests': '80 tests pass (`python -m unittest discover -s tests`).',
                   'hardware': 'While the system is armed it looks at tiny grey frames of the real IP cameras of the CM5 test bench; nothing has run on a Jetson, with '
                               'TensorRT or on a decoded RTSP stream.',
                   'integration': 'It reports movement weighed with the radars to the server of the CM5 test bench.',
                   'docs': 'Eight languages and the changelog are up to date.'},
        'honest': 'The decision layer and the movement detector are real and tested (80 tests), and the observation service **runs on the CM5 test bench**: while the '
                  'system is armed it looks at tiny grey frames of the real IP cameras and reports movement weighed with the radars. It cannot tell a person from a cat '
                  'or a branch: **there is no detection model yet**, and nothing has run on the Jetson, TensorRT or an RTSP stream decoded there.',
        'bullets': ['**The observation service:** `python -m armor_server_ai.service` is never called by the server (it asks the server, with its own token): while the '
                    "system is **armed** it takes one tiny grey frame (64 x 36, from the camera's stream, never stored) of each camera every few seconds, measures how "
                    'much of the picture moved and, when radar tracks agree, reports it to ARMOR-SERVER with its token.',
                    '**Zones of the picture to ignore:** the server hands it the ignore zones of each camera and the pixels inside them count for nothing (a tree that '
                    'waves, a road); a picture that is almost all ignored is not judged and at most sixteen zones count.',
                    '**Day/night profile with hysteresis:** low-light below 30 lux, back to daylight only above 60 lux and never twice within 30 s, so dusk cannot make '
                    'it flap.',
                    '**Explainable fusion:** each detection or movement and the radar tracks give a severity (`ignore`, `review`, `high`) with the reasons behind it; '
                    'strong movement **and** a radar track agree is `high`, weaker movement is a `review`.',
                    '**Recommendations only:** a decision always carries `authorizes_action = false`. The central server authenticates and authorises every action.',
                    '**Checksum-verified engines:** pre-built TensorRT engines are accepted only if present, non-empty and, with an `engines.json`, matching their '
                    'SHA-256. Nothing is compiled or downloaded.',
                    '**A service that says what is wrong:** it reports every new problem when it changes (`unreachable`, `unauthorized`…) and *the server answers again* '
                    'when it is over; a JSONL worker keeps numbered, explained results and a bad line never stops the stream.'],
        'note': 'See the [inference boundary](docs/INFERENCE_BOUNDARY.md) and the [service](docs/SERVICE.md).',
        'fit': 'ARMOR-SERVER-AI is the part that watches the cameras for movement while the house is armed. It never acts: it tells '
               '[ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER) what it saw and why (movement and radar tracks agreeing is `high`), and the server decides '
               'what to do. A model that recognises a person, run on a Jetson, is the next step; [ARMOR-VISION](https://github.com/JuanenRac/ARMOR-VISION) holds the '
               'zones, masks and rules that model will use.',
        'hardware': 'Running as a service on the CM5 test bench with the real IP cameras (movement only); nothing on a Jetson'},
 'es': {'tagline': 'Servicio de observación: el movimiento en las cámaras sopesado con los radares; decide y explica, nunca actúa',
        'status': {'software': 'El detector de movimiento y la capa de decisión funcionan como servicio en el banco de pruebas CM5, pero aún no hay modelo de detección: '
                               'no distingue una persona de un gato o una rama.',
                   'tests': 'Pasan 80 pruebas (`python -m unittest discover -s tests`).',
                   'hardware': 'Mientras el sistema está armado mira fotogramas grises diminutos de las cámaras IP reales del banco de pruebas CM5; nada ha funcionado '
                               'en una Jetson, con TensorRT ni sobre un flujo RTSP decodificado.',
                   'integration': 'Informa del movimiento ponderado con los radares al servidor del banco de pruebas.',
                   'docs': 'Ocho idiomas y el historial de cambios están al día.'},
        'honest': 'La capa de decisión y el detector de movimiento son reales y están probados (80 tests), y el servicio de observación **corre en el banco de pruebas '
                  'de la CM5**: con el sistema armado mira pequeños fotogramas grises de las cámaras IP reales e informa del movimiento sopesado con los radares. No '
                  'distingue a una persona de un gato o una rama: **todavía no hay modelo de detección**, y nada ha corrido en la Jetson, TensorRT ni un flujo RTSP '
                  'decodificado allí.',
        'bullets': ['**El servicio de observación:** `python -m armor_server_ai.service` el servidor nunca lo llama (es él quien le pregunta al servidor, con su propio '
                    'token): con el sistema **armado** toma un diminuto fotograma gris (64 x 36, del flujo de la cámara, nunca guardado) de cada cámara cada pocos '
                    'segundos, mide cuánto de la imagen se movió y, cuando las pistas de radar coinciden, lo comunica a ARMOR-SERVER con su token.',
                    '**Zonas de la imagen que se ignoran:** el servidor le da las zonas a ignorar de cada cámara y los píxeles dentro de ellas no cuentan (un árbol que '
                    'se mueve, una carretera); una imagen casi toda ignorada no se juzga y cuentan como mucho dieciséis zonas.',
                    '**Perfil día/noche con histéresis:** poca luz por debajo de 30 lux, vuelve a día solo por encima de 60 lux y nunca dos veces en 30 s, para que el '
                    'crepúsculo no lo haga oscilar.',
                    '**Fusión explicable:** cada detección o movimiento y las pistas de radar dan una gravedad (`ignore`, `review`, `high`) con las razones; movimiento '
                    'fuerte **y** una pista de radar coincidente es `high`, un movimiento más débil es un `review`.',
                    '**Solo recomendaciones:** una decisión siempre lleva `authorizes_action = false`. El servidor central autentica y autoriza cada acción.',
                    '**Motores verificados por suma de comprobación:** los motores TensorRT precompilados solo se aceptan si existen, no están vacíos y, con un '
                    '`engines.json`, coinciden con su SHA-256. No se compila ni descarga nada.',
                    '**Un servicio que dice qué va mal:** informa de cada problema nuevo cuando cambia (`unreachable`, `unauthorized`…) y *el servidor responde otra '
                    'vez* cuando termina; un trabajador JSONL guarda resultados numerados y explicados y una línea mala nunca detiene el flujo.'],
        'note': 'Véanse el [límite de la inferencia](docs/INFERENCE_BOUNDARY.md) y el [servicio](docs/SERVICE.md).',
        'fit': 'ARMOR-SERVER-AI es la parte que vigila el movimiento en las cámaras mientras la casa está armada. Nunca actúa: dice a '
               '[ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER) qué vio y por qué (movimiento y pistas de radar coincidentes es `high`), y el servidor decide '
               'qué hacer. Un modelo que reconozca a una persona, ejecutado en una Jetson, es el siguiente paso; '
               '[ARMOR-VISION](https://github.com/JuanenRac/ARMOR-VISION) guarda las zonas, máscaras y reglas que usará ese modelo.',
        'hardware': 'Corriendo como servicio en el banco de pruebas de la CM5 con las cámaras IP reales (solo movimiento); nada en una Jetson',
        'requirements': ['Python 3.11+', 'opcional: una Jetson Orin NX con motores TensorRT (sin probar)']},
 'fr': {'tagline': "Service d'observation : le mouvement sur les caméras pesé avec les radars ; il décide et explique, n'actionne jamais",
        'status': {'software': "Le détecteur de mouvement et la couche de décision tournent comme service sur le banc d'essai CM5, mais il n'y a pas encore de modèle de "
                               "détection : il ne distingue pas une personne d'un chat ou d'une branche.",
                   'tests': '80 tests réussissent (`python -m unittest discover -s tests`).',
                   'hardware': "Tant que le système est armé, il regarde de minuscules images grises des vraies caméras IP du banc d'essai CM5 ; rien n'a tourné sur un "
                               'Jetson, avec TensorRT ni sur un flux RTSP décodé.',
                   'integration': "Il rend compte au serveur du banc d'essai du mouvement pondéré par les radars .",
                   'docs': 'Huit langues et le journal des modifications sont à jour.'},
        'honest': "La couche de décision et le détecteur de mouvement sont réels et testés (80 tests), et le service d'observation **tourne sur le banc de test CM5** : "
                  'système armé, il regarde de minuscules images grises des vraies caméras IP et signale le mouvement pesé avec les radars. Il ne distingue pas une '
                  "personne d'un chat ou d'une branche : **il n'y a pas encore de modèle de détection**, et rien n'a tourné sur le Jetson, TensorRT ni un flux RTSP "
                  'décodé là.',
        'bullets': ["**Le service d'observation :** `python -m armor_server_ai.service` n'est jamais appelé par le serveur (c'est lui qui interroge le serveur, avec son "
                    'propre jeton) : système **armé**, il prend une minuscule image grise (64 x 36, du flux de la caméra, jamais stockée) de chaque caméra toutes les '
                    "quelques secondes, mesure quelle part de l'image a bougé et, quand des pistes radar concordent, le signale à ARMOR-SERVER avec son jeton.",
                    "**Zones de l'image à ignorer :** le serveur lui donne les zones à ignorer de chaque caméra et les pixels qu'elles contiennent ne comptent pas (un "
                    "arbre qui bouge, une route) ; une image presque entièrement ignorée n'est pas jugée et seize zones au plus comptent.",
                    '**Profil jour/nuit avec hystérésis :** faible lumière sous 30 lux, retour au jour seulement au-dessus de 60 lux et jamais deux fois en 30 s, pour '
                    'que le crépuscule ne le fasse pas osciller.',
                    '**Fusion explicable :** chaque détection ou mouvement et les pistes radar donnent une gravité (`ignore`, `review`, `high`) avec les raisons ; un '
                    'mouvement fort **et** une piste radar concordante est `high`, un mouvement plus faible est un `review`.',
                    '**Des recommandations seulement :** une décision porte toujours `authorizes_action = false`. Le serveur central authentifie et autorise chaque '
                    'action.',
                    "**Moteurs vérifiés par somme de contrôle :** les moteurs TensorRT précompilés ne sont acceptés que s'ils existent, ne sont pas vides et, avec un "
                    "`engines.json`, correspondent à leur SHA-256. Rien n'est compilé ni téléchargé.",
                    '**Un service qui dit ce qui ne va pas :** il signale chaque nouveau problème quand il change (`unreachable`, `unauthorized`…) et *le serveur répond '
                    "de nouveau* quand c'est fini ; un travailleur JSONL garde des résultats numérotés et expliqués et une mauvaise ligne n'arrête jamais le flux."],
        'note': "Voir la [frontière de l'inférence](docs/INFERENCE_BOUNDARY.md) et le [service](docs/SERVICE.md).",
        'fit': "ARMOR-SERVER-AI est la partie qui surveille le mouvement sur les caméras pendant que la maison est armée. Il n'agit jamais : il dit à "
               "[ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER) ce qu'il a vu et pourquoi (mouvement et pistes radar concordants valent `high`), et le serveur "
               "décide quoi faire. Un modèle qui reconnaît une personne, exécuté sur un Jetson, est l'étape suivante ; "
               '[ARMOR-VISION](https://github.com/JuanenRac/ARMOR-VISION) garde les zones, masques et règles que ce modèle utilisera.',
        'hardware': 'Tourne comme service sur le banc de test CM5 avec les vraies caméras IP (mouvement seulement) ; rien sur un Jetson',
        'requirements': ['Python 3.11+', 'facultatif : un Jetson Orin NX avec des moteurs TensorRT (non éprouvé)']},
 'it': {'tagline': 'Servizio di osservazione: il movimento sulle telecamere pesato con i radar; decide e spiega, non aziona mai',
        'status': {'software': "Il rilevatore di movimento e il livello decisionale girano come servizio sul banco di prova CM5, ma non c'è ancora un modello di "
                               'rilevamento: non distingue una persona da un gatto o da un ramo.',
                   'tests': 'Superano 80 test (`python -m unittest discover -s tests`).',
                   'hardware': 'Mentre il sistema è inserito guarda minuscoli fotogrammi grigi delle telecamere IP reali del banco di prova CM5; nulla ha girato su una '
                               'Jetson, con TensorRT o su un flusso RTSP decodificato.',
                   'integration': 'Riferisce al server del banco di prova il movimento ponderato con i radar.',
                   'docs': 'Otto lingue e il registro delle modifiche sono aggiornati.'},
        'honest': 'Lo strato decisionale e il rilevatore di movimento sono reali e provati (80 test), e il servizio di osservazione **gira sul banco di prova CM5**: a '
                  'sistema inserito guarda minuscoli fotogrammi grigi delle vere telecamere IP e riferisce il movimento pesato con i radar. Non distingue una persona da '
                  "un gatto o da un ramo: **non c'è ancora un modello di rilevamento**, e nulla ha girato sul Jetson, TensorRT o su un flusso RTSP decodificato lì.",
        'bullets': ['**Il servizio di osservazione:** `python -m armor_server_ai.service` non viene mai chiamato dal server (è lui a interrogare il server, con il '
                    'proprio token): a sistema **inserito** prende un minuscolo fotogramma grigio (64 x 36, dal flusso della telecamera, mai salvato) di ogni telecamera '
                    "ogni pochi secondi, misura quanta parte dell'immagine si è mossa e, quando le tracce radar concordano, lo riferisce ad ARMOR-SERVER con il suo "
                    'token.',
                    "**Zone dell'immagine da ignorare:** il server gli dà le zone da ignorare di ogni telecamera e i pixel al loro interno non contano (un albero che si "
                    "muove, una strada); un'immagine quasi tutta ignorata non è giudicata e contano al massimo sedici zone.",
                    '**Profilo giorno/notte con isteresi:** poca luce sotto 30 lux, torna al giorno solo sopra 60 lux e mai due volte in 30 s, così il crepuscolo non lo '
                    'fa oscillare.',
                    '**Fusione spiegabile:** ogni rilevamento o movimento e le tracce radar danno una gravità (`ignore`, `review`, `high`) con le ragioni; movimento '
                    'forte **e** una traccia radar concorde è `high`, un movimento più debole è una `review`.',
                    '**Solo raccomandazioni:** una decisione porta sempre `authorizes_action = false`. Il server centrale autentica e autorizza ogni azione.',
                    '**Motori verificati con checksum:** i motori TensorRT precompilati sono accettati solo se presenti, non vuoti e, con un `engines.json`, coincidenti '
                    'con il loro SHA-256. Nulla è compilato né scaricato.',
                    '**Un servizio che dice cosa non va:** riferisce ogni nuovo problema quando cambia (`unreachable`, `unauthorized`…) e *il server risponde di nuovo* '
                    'quando è finito; un worker JSONL conserva risultati numerati e spiegati e una riga errata non ferma mai il flusso.'],
        'note': "Vedi il [confine dell'inferenza](docs/INFERENCE_BOUNDARY.md) e il [servizio](docs/SERVICE.md).",
        'fit': 'ARMOR-SERVER-AI è la parte che sorveglia il movimento sulle telecamere mentre la casa è inserita. Non agisce mai: dice ad '
               '[ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER) cosa ha visto e perché (movimento e tracce radar concordi valgono `high`), e il server decide '
               'cosa fare. Un modello che riconosca una persona, eseguito su un Jetson, è il passo successivo; [ARMOR-VISION](https://github.com/JuanenRac/ARMOR-VISION) '
               'tiene le zone, le maschere e le regole che quel modello userà.',
        'hardware': 'Gira come servizio sul banco di prova CM5 con le vere telecamere IP (solo movimento); nulla su un Jetson',
        'requirements': ['Python 3.11+', 'facoltativo: un Jetson Orin NX con motori TensorRT (non provato)']},
 'de': {'tagline': 'Beobachtungsdienst: Bewegung auf den Kameras, gegen die Radare abgewogen; er entscheidet und erklärt, schaltet nie',
        'status': {'software': 'Der Bewegungsmelder und die Entscheidungsschicht laufen als Dienst auf dem CM5-Prüfstand, aber es gibt noch kein Erkennungsmodell: Er '
                               'unterscheidet keine Person von einer Katze oder einem Ast.',
                   'tests': '80 Tests bestehen (`python -m unittest discover -s tests`).',
                   'hardware': 'Solange das System scharf ist, betrachtet er winzige Graubilder der echten IP-Kameras des CM5-Prüfstands; nichts lief auf einem Jetson, '
                               'mit TensorRT oder auf einem dekodierten RTSP-Strom.',
                   'integration': 'Er meldet die mit den Radaren gewichtete Bewegung an den Server des Prüfstands.',
                   'docs': 'Acht Sprachen und das Änderungsprotokoll sind aktuell.'},
        'honest': 'Die Entscheidungsschicht und der Bewegungsdetektor sind real und getestet (80 Tests), und der Beobachtungsdienst **läuft am CM5-Testaufbau**: Bei '
                  'scharfem System sieht er winzige Graubilder der echten IP-Kameras an und meldet Bewegung, gegen die Radare abgewogen. Er kann eine Person nicht von '
                  'einer Katze oder einem Ast unterscheiden: **Es gibt noch kein Erkennungsmodell**, und nichts lief auf dem Jetson, mit TensorRT oder einem dort '
                  'dekodierten RTSP-Strom.',
        'bullets': ['**Der Beobachtungsdienst:** `python -m armor_server_ai.service` wird nie vom Server aufgerufen (er fragt den Server, mit seinem eigenen Token): Bei '
                    '**scharfem** System nimmt er alle paar Sekunden ein winziges Graubild (64 x 36, aus dem Kamerastrom, nie gespeichert) jeder Kamera auf, misst, wie '
                    'viel vom Bild sich bewegt hat, und meldet es, wenn Radarspuren übereinstimmen, mit seinem Token an ARMOR-SERVER.',
                    '**Zu ignorierende Bildzonen:** der Server gibt ihm die zu ignorierenden Zonen jeder Kamera, und die Pixel darin zählen nicht (ein wehender Baum, '
                    'eine Straße); ein fast ganz ignoriertes Bild wird nicht beurteilt, und höchstens sechzehn Zonen zählen.',
                    '**Tag/Nacht-Profil mit Hysterese:** Dunkelheit unter 30 Lux, zurück zu Tageslicht erst über 60 Lux und nie zweimal innerhalb von 30 s, damit die '
                    'Dämmerung es nicht flattern lässt.',
                    '**Erklärbare Fusion:** jede Erkennung oder Bewegung und die Radarspuren ergeben eine Stufe (`ignore`, `review`, `high`) mit den Gründen; starke '
                    'Bewegung **und** eine übereinstimmende Radarspur ist `high`, schwächere Bewegung ist `review`.',
                    '**Nur Empfehlungen:** eine Entscheidung trägt immer `authorizes_action = false`. Der zentrale Server authentifiziert und autorisiert jede Aktion.',
                    '**Per Prüfsumme verifizierte Engines:** vorgebaute TensorRT-Engines werden nur akzeptiert, wenn sie vorhanden, nicht leer und, mit einer '
                    '`engines.json`, passend zu ihrem SHA-256 sind. Nichts wird kompiliert oder heruntergeladen.',
                    '**Ein Dienst, der sagt, was falsch ist:** er meldet jedes neue Problem, wenn es sich ändert (`unreachable`, `unauthorized`…), und *der Server '
                    'antwortet wieder*, wenn es vorbei ist; ein JSONL-Worker liefert nummerierte, erklärte Ergebnisse, und eine fehlerhafte Zeile stoppt nie den Strom.'],
        'note': 'Siehe die [Inferenzgrenze](docs/INFERENCE_BOUNDARY.md) und den [Dienst](docs/SERVICE.md).',
        'fit': 'ARMOR-SERVER-AI ist der Teil, der die Kameras auf Bewegung beobachtet, solange das Haus scharf ist. Er handelt nie: Er sagt '
               '[ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER), was er gesehen hat und warum (übereinstimmende Bewegung und Radarspuren ergeben `high`), und '
               'der Server entscheidet, was zu tun ist. Ein Modell, das eine Person erkennt, auf einem Jetson ausgeführt, ist der nächste Schritt; '
               '[ARMOR-VISION](https://github.com/JuanenRac/ARMOR-VISION) hält die Zonen, Masken und Regeln, die dieses Modell nutzen wird.',
        'hardware': 'Läuft als Dienst am CM5-Testaufbau mit den echten IP-Kameras (nur Bewegung); nichts auf einem Jetson',
        'requirements': ['Python 3.11+', 'optional: ein Jetson Orin NX mit TensorRT-Engines (nicht erprobt)']},
 'zh': {'tagline': '观察服务：把摄像头上的移动与雷达对照权衡；它做出决定并给出解释，从不执行动作',
        'status': {'software': '移动检测器和决策层在 CM5 测试台上作为服务运行，但目前还没有检测模型：它分不清人、猫或树枝。',
                   'tests': '80 项测试通过（`python -m unittest discover -s tests`）。',
                   'hardware': '系统布防期间，它查看 CM5 测试台上真实 IP 摄像头的微小灰度画面；还没有在 Jetson、TensorRT 或解码后的 RTSP 流上运行过。',
                   'integration': '它把结合雷达加权后的移动情况报告给测试台的服务器。',
                   'docs': '八种语言和更新日志均为最新。'},
        'honest': '决策层和移动检测器是真实的并经过测试（80 个测试），观察服务**在 CM5 测试台上运行**：系统布防时，它查看真实 IP 摄像头的微小灰度帧，并报告与雷达对照权衡后的移动。它分不清人、猫或树枝：**目前还没有检测模型**，也没有任何东西在 Jetson、TensorRT 或在那里解码的 '
                  'RTSP 流上运行过。',
        'bullets': ['**观察服务：**`python -m armor_server_ai.service` 服务器从不调用它（是它用自己的令牌向服务器询问）：系统**布防**时，它每隔几秒从每个摄像头的码流取一帧微小的灰度图（64 x 36，从不保存），测量画面移动了多少，当雷达轨迹一致时，带着自己的令牌上报给 '
                    'ARMOR-SERVER。',
                    '**要忽略的画面区域：**服务器把每个摄像头的忽略区域交给它，区域内的像素不计入（摇动的树、公路）；几乎全被忽略的画面不做判断，最多计入十六个区域。',
                    '**带滞回的昼夜配置：**低于 30 勒克斯为弱光，只有高于 60 勒克斯才回到白天，且 30 秒内绝不切换两次，因此黄昏不会让它来回抖动。',
                    '**可解释的融合：**每次检测或移动与雷达轨迹给出一个严重级别（`ignore`、`review`、`high`）及理由；强移动**并且**有一致的雷达轨迹为 `high`，较弱的移动为 `review`。',
                    '**只是建议：**决定总是带有 `authorizes_action = false`。中央服务器对每个动作进行认证和授权。',
                    '**经校验和验证的引擎：**预先构建的 TensorRT 引擎只有在存在、非空，并且（有 `engines.json` 时）SHA-256 匹配时才会被接受。不会编译或下载任何东西。',
                    '**会说明出了什么问题的服务：**每个新问题变化时都会报告（`unreachable`、`unauthorized`……），结束时会说明*服务器又有应答了*；JSONL 工作进程保留编号并带解释的结果，坏的一行绝不会中断数据流。'],
        'note': '参见[推理边界](docs/INFERENCE_BOUNDARY.md)和[服务](docs/SERVICE.md)。',
        'fit': 'ARMOR-SERVER-AI 是在住宅布防时观察摄像头移动的部分。它从不行动：它告诉 [ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER) 它看到了什么以及原因（移动与雷达轨迹一致即为 `high`），由服务器决定怎么做。下一步是在 '
               'Jetson 上运行能识别人的模型；[ARMOR-VISION](https://github.com/JuanenRac/ARMOR-VISION) 保存该模型将使用的区域、遮罩和规则。',
        'hardware': '在 CM5 测试台上用真实 IP 摄像头作为服务运行（仅移动）；Jetson 上没有任何东西',
        'requirements': ['Python 3.11+', '可选：带 TensorRT 引擎的 Jetson Orin NX（未经验证）']},
 'ja': {'tagline': '観察サービス：カメラ上の動きをレーダーと照らし合わせます。判断して説明するだけで、決して動作させません',
        'status': {'software': '動き検出と判断の層は CM5 テストベンチ上でサービスとして動いていますが、検出モデルはまだありません。人と猫や枝の区別はできません。',
                   'tests': '80 件のテストが通ります（`python -m unittest discover -s tests`）。',
                   'hardware': '警戒中は、CM5 テストベンチの実際の IP カメラの小さなグレー画像を見ています。Jetson、TensorRT、デコードした RTSP ストリームではまだ何も動かしていません。',
                   'integration': 'レーダーと照合した動きの結果をテストベンチのサーバーに報告します。',
                   'docs': '8 言語と変更履歴は最新です。'},
        'honest': '判断レイヤーと動き検出器は実在し、テストされています（80 件）。観察サービスは **CM5 テストベンチで動作**しており、システムの警戒中に実際の IP '
                  'カメラの小さなグレーフレームを見て、レーダーと照らし合わせた動きを報告します。人と猫や枝の区別はできません。**検出モデルはまだなく**、Jetson、TensorRT、そこでデコードした RTSP ストリームでは何も動いていません。',
        'bullets': ['**観察サービス：**`python -m armor_server_ai.service` はサーバーから呼び出されることはなく（自分のトークンでサーバーに問い合わせます）、システムが**警戒中**のあいだ、数秒ごとに各カメラのストリームから小さなグレーフレーム（64 x '
                    '36、保存しない）を 1 枚取り、画面のどれだけが動いたかを測り、レーダーの軌跡と一致すれば、自分のトークンで ARMOR-SERVER に報告します。',
                    '**無視する映像ゾーン：**サーバーが各カメラの無視ゾーンを渡し、その中のピクセルは数えません（揺れる木、道路）。ほとんどが無視される画像は判断せず、数えるゾーンは最大 16 個です。',
                    '**ヒステリシス付きの昼夜プロファイル：**30 ルクス未満で低照度、60 ルクスを超えたときだけ昼に戻り、30 秒以内に 2 度は切り替えないため、夕暮れでばたつきません。',
                    '**説明できる融合：**検出や動きとレーダーの軌跡から、理由付きで重大度（`ignore`、`review`、`high`）を出します。強い動き**かつ**一致するレーダーの軌跡は `high`、弱い動きは `review` です。',
                    '**推奨のみ：**判断には常に `authorizes_action = false` が付きます。中央サーバーがすべての動作を認証・認可します。',
                    '**チェックサムで検証されるエンジン：**ビルド済みの TensorRT エンジンは、存在し、空でなく、`engines.json` があればその SHA-256 と一致するときだけ受け付けます。何もコンパイルもダウンロードもしません。',
                    '**何が悪いかを伝えるサービス：**新しい問題が変わるたびに報告し（`unreachable`、`unauthorized` など）、終われば*サーバーがまた応答する*と伝えます。JSONL ワーカーは番号付きで説明付きの結果を保ち、不正な行がストリームを止めることはありません。'],
        'note': '[推論の境界](docs/INFERENCE_BOUNDARY.md)と[サービス](docs/SERVICE.md)を参照してください。',
        'fit': 'ARMOR-SERVER-AI は家が警戒中にカメラの動きを見張る部分です。決して動作せず、何を見たかとその理由（動きとレーダーの軌跡が一致すれば `high`）を [ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER) '
               'に伝え、サーバーが何をするかを決めます。次の段階は、Jetson で動く人を認識するモデルで、[ARMOR-VISION](https://github.com/JuanenRac/ARMOR-VISION) がそのモデルが使うゾーン、マスク、ルールを保持します。',
        'hardware': 'CM5 テストベンチで実際の IP カメラとともにサービスとして動作（動きのみ）。Jetson 上では何もありません',
        'requirements': ['Python 3.11+', '任意：TensorRT エンジンを載せた Jetson Orin NX（未検証）']},
 'pt': {'tagline': 'Serviço de observação: o movimento nas câmaras pesado com os radares; decide e explica, nunca aciona',
        'status': {'software': 'O detetor de movimento e a camada de decisão funcionam como serviço na bancada de testes CM5, mas ainda não há modelo de deteção: não '
                               'distingue uma pessoa de um gato ou de um ramo.',
                   'tests': 'Passam 80 testes (`python -m unittest discover -s tests`).',
                   'hardware': 'Enquanto o sistema está armado, olha para pequenas imagens cinzentas das câmaras IP reais da bancada de testes CM5; nada funcionou num '
                               'Jetson, com TensorRT ou sobre um fluxo RTSP descodificado.',
                   'integration': 'Reporta ao servidor da bancada de testes o movimento ponderado com os radares.',
                   'docs': 'Oito idiomas e o registo de alterações estão atualizados.'},
        'honest': 'A camada de decisão e o detetor de movimento são reais e estão testados (80 testes), e o serviço de observação **corre na bancada de testes do CM5**: '
                  'com o sistema armado olha para pequenas imagens cinzentas das câmaras IP reais e comunica o movimento pesado com os radares. Não distingue uma pessoa '
                  'de um gato ou de um ramo: **ainda não há modelo de deteção**, e nada correu no Jetson, no TensorRT nem num fluxo RTSP descodificado aí.',
        'bullets': ['**O serviço de observação:** `python -m armor_server_ai.service` nunca é chamado pelo servidor (é ele que pergunta ao servidor, com o seu próprio '
                    'token): com o sistema **armado** tira uma pequena imagem cinzenta (64 x 36, do fluxo da câmara, nunca guardada) de cada câmara de poucos em poucos '
                    'segundos, mede quanto da imagem se moveu e, quando as pistas de radar coincidem, comunica-o ao ARMOR-SERVER com o seu token.',
                    '**Zonas da imagem a ignorar:** o servidor dá-lhe as zonas a ignorar de cada câmara e os píxeis dentro delas não contam (uma árvore que se mexe, uma '
                    'estrada); uma imagem quase toda ignorada não é julgada e contam no máximo dezasseis zonas.',
                    '**Perfil dia/noite com histerese:** pouca luz abaixo de 30 lux, volta ao dia só acima de 60 lux e nunca duas vezes em 30 s, para que o crepúsculo '
                    'não o faça oscilar.',
                    '**Fusão explicável:** cada deteção ou movimento e as pistas de radar dão uma gravidade (`ignore`, `review`, `high`) com as razões; movimento forte '
                    '**e** uma pista de radar coincidente é `high`, um movimento mais fraco é um `review`.',
                    '**Só recomendações:** uma decisão leva sempre `authorizes_action = false`. O servidor central autentica e autoriza cada ação.',
                    '**Motores verificados por soma de verificação:** os motores TensorRT pré-compilados só são aceites se existirem, não estiverem vazios e, com um '
                    '`engines.json`, coincidirem com o seu SHA-256. Nada é compilado nem descarregado.',
                    '**Um serviço que diz o que está mal:** comunica cada novo problema quando muda (`unreachable`, `unauthorized`…) e *o servidor responde outra vez* '
                    'quando acaba; um trabalhador JSONL guarda resultados numerados e explicados e uma linha má nunca para o fluxo.'],
        'note': 'Veja o [limite da inferência](docs/INFERENCE_BOUNDARY.md) e o [serviço](docs/SERVICE.md).',
        'fit': 'O ARMOR-SERVER-AI é a parte que vigia o movimento nas câmaras enquanto a casa está armada. Nunca age: diz ao '
               '[ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER) o que viu e porquê (movimento e pistas de radar coincidentes é `high`), e o servidor decide o '
               'que fazer. Um modelo que reconheça uma pessoa, executado num Jetson, é o passo seguinte; o [ARMOR-VISION](https://github.com/JuanenRac/ARMOR-VISION) '
               'guarda as zonas, máscaras e regras que esse modelo usará.',
        'hardware': 'A correr como serviço na bancada de testes do CM5 com as câmaras IP reais (só movimento); nada num Jetson',
        'requirements': ['Python 3.11+', 'opcional: um Jetson Orin NX com motores TensorRT (não comprovado)']}}

# the text tree of docs/structure.json (make_structure.py --tree <language>); the repository's own check fails when it and the file disagree
TREE = {'en': 'ARMOR-SERVER-AI/\n'
       '├── src/armor_server_ai/\n'
       '│   ├── service.py                 the observation service: one pass per interval\n'
       '│   ├── motion.py                  grey frame, zones to ignore, movement share\n'
       '│   ├── profile.py                 day or low light, with hysteresis\n'
       '│   ├── policy.py                  fusion: ignore, review, high\n'
       '│   ├── engine_registry.py         TensorRT engines checked by SHA-256\n'
       '│   └── cli.py                     the JSON-lines worker\n'
       '├── tests/                         80 tests: motion, policy, service, worker\n'
       '├── docs/                          INFERENCE_BOUNDARY.md, SERVICE.md\n'
       '├── tools/                         the shared CI checks and project tooling\n'
       '├── images/                        banner, icon and the pictures of the README\n'
       '├── .github/                       CI workflow, dashboard notice, issue and pull-request templates\n'
       '├── armor.project.json             manifest: version, role, maturity\n'
       '├── pyproject.toml                 package metadata, entry points\n'
       '├── CHANGELOG.md                   what changed in each version\n'
       '├── run.sh run.bat                 start, shared workflow\n'
       '├── build.sh build.bat             build and test, shared workflow\n'
       '├── build-test.sh build-test.bat   build, test and package\n'
       '├── test.sh test.bat               only the tests, never the version\n'
       '└── SECURITY.md SUPPORT.md CONTRIBUTING.md CODE_OF_CONDUCT.md LICENSE',
 'es': 'ARMOR-SERVER-AI/\n'
       '├── src/armor_server_ai/\n'
       '│   ├── service.py                 el servicio de observación: una pasada por intervalo\n'
       '│   ├── motion.py                  fotograma gris, zonas a ignorar, movimiento\n'
       '│   ├── profile.py                 día o poca luz, con histéresis\n'
       '│   ├── policy.py                  fusión: ignore, review, high\n'
       '│   ├── engine_registry.py         motores TensorRT comprobados por SHA-256\n'
       '│   └── cli.py                     el trabajador de líneas JSON\n'
       '├── tests/                         80 pruebas: movimiento, política, servicio, trabajador\n'
       '├── docs/                          INFERENCE_BOUNDARY.md, SERVICE.md\n'
       '├── tools/                         las comprobaciones de CI y las herramientas compartidas\n'
       '├── images/                        banner, icono y las imágenes del README\n'
       '├── .github/                       flujo de CI, aviso al panel, plantillas de incidencias y pull requests\n'
       '├── armor.project.json             manifiesto: versión, función, madurez\n'
       '├── pyproject.toml                 metadatos del paquete, entradas\n'
       '├── CHANGELOG.md                   qué cambió en cada versión\n'
       '├── run.sh run.bat                 arrancar, flujo compartido\n'
       '├── build.sh build.bat             construir y probar, flujo compartido\n'
       '├── build-test.sh build-test.bat   construir, probar y empaquetar\n'
       '├── test.sh test.bat               solo las pruebas, nunca la versión\n'
       '└── SECURITY.md SUPPORT.md CONTRIBUTING.md CODE_OF_CONDUCT.md LICENSE',
 'de': 'ARMOR-SERVER-AI/\n'
       '├── src/armor_server_ai/\n'
       '│   ├── service.py                 der Beobachtungsdienst: ein Durchgang je Intervall\n'
       '│   ├── motion.py                  Graubild, Ignorierzonen, Bewegungsanteil\n'
       '│   ├── profile.py                 Tag oder wenig Licht, mit Hysterese\n'
       '│   ├── policy.py                  Fusion: ignore, review, high\n'
       '│   ├── engine_registry.py         TensorRT-Engines per SHA-256 geprüft\n'
       '│   └── cli.py                     der JSON-Lines-Arbeiter\n'
       '├── tests/                         80 Tests: Bewegung, Richtlinie, Dienst, Arbeiter\n'
       '├── docs/                          INFERENCE_BOUNDARY.md, SERVICE.md\n'
       '├── tools/                         die gemeinsamen CI-Prüfungen und Werkzeuge\n'
       '├── images/                        Banner, Symbol und die Bilder des READMEs\n'
       '├── .github/                       CI-Workflow, Dashboard-Hinweis, Vorlagen für Issues und Pull Requests\n'
       '├── armor.project.json             Manifest: Version, Rolle, Reife\n'
       '├── pyproject.toml                 Paket-Metadaten, Einstiege\n'
       '├── CHANGELOG.md                   was sich in jeder Version geändert hat\n'
       '├── run.sh run.bat                 Start, gemeinsamer Ablauf\n'
       '├── build.sh build.bat             Bauen und Testen, gemeinsamer Ablauf\n'
       '├── build-test.sh build-test.bat   Bauen, Testen und Verpacken\n'
       '├── test.sh test.bat               nur die Tests, nie die Version\n'
       '└── SECURITY.md SUPPORT.md CONTRIBUTING.md CODE_OF_CONDUCT.md LICENSE',
 'fr': 'ARMOR-SERVER-AI/\n'
       '├── src/armor_server_ai/\n'
       "│   ├── service.py                 le service d'observation : une passe par intervalle\n"
       '│   ├── motion.py                  image grise, zones à ignorer, mouvement\n'
       '│   ├── profile.py                 jour ou faible lumière, avec hystérésis\n'
       '│   ├── policy.py                  fusion : ignore, review, high\n'
       '│   ├── engine_registry.py         moteurs TensorRT vérifiés par SHA-256\n'
       '│   └── cli.py                     le travailleur JSON lignes\n'
       '├── tests/                         80 tests : mouvement, politique, service, travailleur\n'
       '├── docs/                          INFERENCE_BOUNDARY.md, SERVICE.md\n'
       '├── tools/                         les vérifications CI et les outils partagés\n'
       '├── images/                        bannière, icône et images du README\n'
       "├── .github/                       workflow CI, avis au tableau de bord, modèles d'issues et de pull requests\n"
       '├── armor.project.json             manifeste : version, rôle, maturité\n'
       '├── pyproject.toml                 métadonnées du paquet, entrées\n'
       '├── CHANGELOG.md                   ce qui a changé à chaque version\n'
       '├── run.sh run.bat                 démarrer, flux partagé\n'
       '├── build.sh build.bat             construire et tester, flux partagé\n'
       '├── build-test.sh build-test.bat   construire, tester, empaqueter\n'
       '├── test.sh test.bat               seulement les tests, jamais la version\n'
       '└── SECURITY.md SUPPORT.md CONTRIBUTING.md CODE_OF_CONDUCT.md LICENSE',
 'it': 'ARMOR-SERVER-AI/\n'
       '├── src/armor_server_ai/\n'
       '│   ├── service.py                 il servizio di osservazione: un passaggio per intervallo\n'
       '│   ├── motion.py                  fotogramma grigio, zone da ignorare, movimento\n'
       '│   ├── profile.py                 giorno o poca luce, con isteresi\n'
       '│   ├── policy.py                  fusione: ignore, review, high\n'
       '│   ├── engine_registry.py         motori TensorRT verificati con SHA-256\n'
       '│   └── cli.py                     il worker di righe JSON\n'
       '├── tests/                         80 test: movimento, politica, servizio, worker\n'
       '├── docs/                          INFERENCE_BOUNDARY.md, SERVICE.md\n'
       '├── tools/                         i controlli CI e gli strumenti condivisi\n'
       '├── images/                        banner, icona e immagini del README\n'
       '├── .github/                       workflow CI, avviso alla dashboard, modelli per issue e pull request\n'
       '├── armor.project.json             manifesto: versione, ruolo, maturità\n'
       '├── pyproject.toml                 metadati del pacchetto, ingressi\n'
       '├── CHANGELOG.md                   cosa è cambiato in ogni versione\n'
       '├── run.sh run.bat                 avvio, flusso condiviso\n'
       '├── build.sh build.bat             compila e prova, flusso condiviso\n'
       '├── build-test.sh build-test.bat   compila, prova e impacchetta\n'
       '├── test.sh test.bat               solo i test, mai la versione\n'
       '└── SECURITY.md SUPPORT.md CONTRIBUTING.md CODE_OF_CONDUCT.md LICENSE',
 'ja': 'ARMOR-SERVER-AI/\n'
       '├── src/armor_server_ai/\n'
       '│   ├── service.py                 観察サービス：間隔ごとに 1 巡\n'
       '│   ├── motion.py                  グレーフレーム、無視ゾーン、動き\n'
       '│   ├── profile.py                 昼間か低照度（ヒステリシス付き）\n'
       '│   ├── policy.py                  融合：ignore、review、high\n'
       '│   ├── engine_registry.py         SHA-256 で検証する TensorRT エンジン\n'
       '│   └── cli.py                     JSON Lines ワーカー\n'
       '├── tests/                         80 件：動き、ポリシー、サービス、ワーカー\n'
       '├── docs/                          INFERENCE_BOUNDARY.md、SERVICE.md\n'
       '├── tools/                         共通の CI 検査とツール\n'
       '├── images/                        バナー、アイコン、README の画像\n'
       '├── .github/                       CI ワークフロー、ダッシュボード通知、Issue と Pull Request のテンプレート\n'
       '├── armor.project.json             マニフェスト：版・役割・成熟度\n'
       '├── pyproject.toml                 パッケージ情報とエントリー\n'
       '├── CHANGELOG.md                   各バージョンの変更点\n'
       '├── run.sh run.bat                 起動（共通フロー）\n'
       '├── build.sh build.bat             ビルドとテスト（共通フロー）\n'
       '├── build-test.sh build-test.bat   ビルド、テスト、パッケージ化\n'
       '├── test.sh test.bat               テストのみ（版は変えません）\n'
       '└── SECURITY.md SUPPORT.md CONTRIBUTING.md CODE_OF_CONDUCT.md LICENSE',
 'zh': 'ARMOR-SERVER-AI/\n'
       '├── src/armor_server_ai/\n'
       '│   ├── service.py                 观察服务：每个间隔一轮\n'
       '│   ├── motion.py                  灰度帧、忽略区、运动量\n'
       '│   ├── profile.py                 白天或弱光，带迟滞\n'
       '│   ├── policy.py                  融合：ignore、review、high\n'
       '│   ├── engine_registry.py         以 SHA-256 校验的 TensorRT 引擎\n'
       '│   └── cli.py                     JSON 行工作进程\n'
       '├── tests/                         80 项：运动、策略、服务、工作进程\n'
       '├── docs/                          INFERENCE_BOUNDARY.md、SERVICE.md\n'
       '├── tools/                         共用的 CI 检查和工具\n'
       '├── images/                        横幅图、图标和 README 的图片\n'
       '├── .github/                       CI 工作流、仪表板通知、议题和 pull request 模板\n'
       '├── armor.project.json             清单：版本、角色、成熟度\n'
       '├── pyproject.toml                 包元数据、入口\n'
       '├── CHANGELOG.md                   每个版本的变化\n'
       '├── run.sh run.bat                 启动（共用流程）\n'
       '├── build.sh build.bat             构建并测试（共用流程）\n'
       '├── build-test.sh build-test.bat   构建、测试并打包\n'
       '├── test.sh test.bat               只运行测试，不改版本\n'
       '└── SECURITY.md SUPPORT.md CONTRIBUTING.md CODE_OF_CONDUCT.md LICENSE',
 'pt': 'ARMOR-SERVER-AI/\n'
       '├── src/armor_server_ai/\n'
       '│   ├── service.py                 o serviço de observação: uma passagem por intervalo\n'
       '│   ├── motion.py                  imagem cinzenta, zonas a ignorar, movimento\n'
       '│   ├── profile.py                 dia ou pouca luz, com histerese\n'
       '│   ├── policy.py                  fusão: ignore, review, high\n'
       '│   ├── engine_registry.py         motores TensorRT verificados por SHA-256\n'
       '│   └── cli.py                     o trabalhador de linhas JSON\n'
       '├── tests/                         80 testes: movimento, política, serviço, trabalhador\n'
       '├── docs/                          INFERENCE_BOUNDARY.md, SERVICE.md\n'
       '├── tools/                         as verificações de CI e as ferramentas partilhadas\n'
       '├── images/                        faixa, ícone e as imagens do README\n'
       '├── .github/                       fluxo de CI, aviso ao painel, modelos de issues e pull requests\n'
       '├── armor.project.json             manifesto: versão, função, maturidade\n'
       '├── pyproject.toml                 metadados do pacote, entradas\n'
       '├── CHANGELOG.md                   o que mudou em cada versão\n'
       '├── run.sh run.bat                 arrancar, fluxo partilhado\n'
       '├── build.sh build.bat             compilar e testar, fluxo partilhado\n'
       '├── build-test.sh build-test.bat   compilar, testar e empacotar\n'
       '├── test.sh test.bat               só os testes, nunca a versão\n'
       '└── SECURITY.md SUPPORT.md CONTRIBUTING.md CODE_OF_CONDUCT.md LICENSE'}

DIAGRAM = ''

NT = "80"
FACTS["badges"] = [x for x in FACTS["badges"] if x[0] != "Tests"] + [["Tests", NT + "%20passing", "2ea44f"]]
FACTS["status"] = [x for x in FACTS["status"] if x[0] != "security"]
FACTS["status"].insert(len(FACTS["status"]) - 1, ["security", "yellow"])

SEC_NOTE = P("The service never acts (every decision carries `authorizes_action = false`), refuses a token under 24 characters and a server address that is not `https://` or this same machine, and never stores a picture; tested, with no independent review.",
             "El servicio nunca actúa (toda decisión lleva `authorizes_action = false`), rechaza un token de menos de 24 caracteres y una dirección de servidor que no sea `https://` ni esta misma máquina, y nunca guarda una imagen; probado, sin revisión independiente.",
             "Der Dienst handelt nie (jede Entscheidung trägt `authorizes_action = false`), lehnt ein Token unter 24 Zeichen und eine Serveradresse ab, die nicht `https://` oder dieselbe Maschine ist, und speichert nie ein Bild; getestet, ohne unabhängige Prüfung.",
             "Le service n'agit jamais (chaque décision porte `authorizes_action = false`), refuse un jeton de moins de 24 caractères et une adresse de serveur qui n'est ni `https://` ni cette même machine, et ne stocke jamais d'image ; testé, sans revue indépendante.",
             "Il servizio non agisce mai (ogni decisione porta `authorizes_action = false`), rifiuta un token sotto i 24 caratteri e un indirizzo di server che non sia `https://` o questa stessa macchina, e non salva mai un'immagine; provato, senza revisione indipendente.",
             "サービスは決して動作しません（すべての判定が `authorizes_action = false` を持つ）。24 文字未満のトークンと、`https://` でも同一マシンでもないサーバーアドレスを拒否し、画像は保存しません。テスト済みで、第三者レビューはありません。",
             "该服务从不执行动作（每个判定都带 `authorizes_action = false`），拒绝少于 24 个字符的令牌以及既不是 `https://` 也不是本机的服务器地址，从不保存图片；已测试，没有独立审查。",
             "O serviço nunca age (cada decisão leva `authorizes_action = false`), recusa um token com menos de 24 caracteres e um endereço de servidor que não seja `https://` nem esta mesma máquina, e nunca guarda uma imagem; testado, sem revisão independente.")


def L(lg, key):
    return LEGACY[lg][key]


GLANCE = [
    (GL["role"], T("Observation service: movement weighed with the radars, recommendations only | Servicio de observación: movimiento ponderado con los radares, solo recomienda | Beobachtungsdienst: Bewegung, mit den Radaren gewichtet, nur Empfehlungen | Service d'observation : mouvement pondéré avec les radars, recommandations seulement | Servizio di osservazione: movimento pesato con i radar, solo raccomandazioni | 観察サービス：レーダーと合わせて動きを評価し、推奨のみ | 观察服务：结合雷达评估运动，只给出建议 | Serviço de observação: movimento ponderado com os radares, só recomenda")),
    (GL["stack"], T("Python 3.11+, standard library only | Python 3.11+, solo biblioteca estándar | Python 3.11+, nur Standardbibliothek | Python 3.11+, bibliothèque standard seule | Python 3.11+, solo libreria standard | Python 3.11+（標準ライブラリのみ） | Python 3.11+，仅用标准库 | Python 3.11+, só biblioteca padrão")),
    (GL["tests"], T("80 (`python -m unittest discover -s tests`) | 80 (`python -m unittest discover -s tests`) | 80 (`python -m unittest discover -s tests`) | 80 (`python -m unittest discover -s tests`) | 80 (`python -m unittest discover -s tests`) | 80 件（`python -m unittest discover -s tests`） | 80 项（`python -m unittest discover -s tests`） | 80 (`python -m unittest discover -s tests`)")),
    (GL["contract"], T("Client of ARMOR-SERVER: 3 routes under `/api/v1/ai/`; it is never called | Cliente de ARMOR-SERVER: 3 rutas bajo `/api/v1/ai/`; nadie lo llama | Client von ARMOR-SERVER: 3 Routen unter `/api/v1/ai/`; er wird nie aufgerufen | Client d'ARMOR-SERVER : 3 routes sous `/api/v1/ai/` ; personne ne l'appelle | Client di ARMOR-SERVER: 3 rotte sotto `/api/v1/ai/`; nessuno lo chiama | ARMOR-SERVER のクライアント：`/api/v1/ai/` の 3 ルート。呼び出されることはありません | ARMOR-SERVER 的客户端：`/api/v1/ai/` 下的 3 条路由；从不被调用 | Cliente do ARMOR-SERVER: 3 rotas sob `/api/v1/ai/`; ninguém o chama")),
    (GL["runs"], T("The CM5 test bench (as a service, see ARMOR-DEVOPS) or any computer | El banco de la CM5 (como servicio, ver ARMOR-DEVOPS) o cualquier ordenador | Der CM5-Prüfstand (als Dienst, siehe ARMOR-DEVOPS) oder jeder Computer | Le banc d'essai CM5 (en service, voir ARMOR-DEVOPS) ou tout ordinateur | Il banco di prova CM5 (come servizio, vedi ARMOR-DEVOPS) o qualsiasi computer | CM5 テストベンチ（サービスとして。ARMOR-DEVOPS 参照）または任意のコンピューター | CM5 测试台（作为服务，见 ARMOR-DEVOPS）或任何计算机 | A bancada do CM5 (como serviço, ver ARMOR-DEVOPS) ou qualquer computador")),
    (GL["hardware"], {lg: LEGACY[lg]["hardware"] for lg in LGS}),
    (GL["license"], LICENSE_VALUE),
]

ROLE_TABLE = [
    ("ARMOR-SERVER", T("it asks the server (`/api/v1/ai/*`, token `ARMOR_AI_TOKEN`) | pregunta al servidor (`/api/v1/ai/*`, token `ARMOR_AI_TOKEN`) | er fragt den Server (`/api/v1/ai/*`, Token `ARMOR_AI_TOKEN`) | il interroge le serveur (`/api/v1/ai/*`, jeton `ARMOR_AI_TOKEN`) | interroga il server (`/api/v1/ai/*`, token `ARMOR_AI_TOKEN`) | サーバーに問い合わせる（`/api/v1/ai/*`、トークン `ARMOR_AI_TOKEN`） | 向服务器查询（`/api/v1/ai/*`，令牌 `ARMOR_AI_TOKEN`） | pergunta ao servidor (`/api/v1/ai/*`, token `ARMOR_AI_TOKEN`)"),
     T("the cameras, their grey frames and the zones to ignore in; the observation out | las cámaras, sus fotogramas grises y las zonas a ignorar entran; la observación sale | die Kameras, ihre Graubilder und die Ignorierzonen hinein; die Beobachtung hinaus | les caméras, leurs images grises et les zones à ignorer entrent ; l'observation sort | le telecamere, i loro fotogrammi grigi e le zone da ignorare entrano; l'osservazione esce | カメラ、グレーフレーム、無視ゾーンを受け取り、観察結果を送る | 摄像头、其灰度帧和忽略区进来，观察结果出去 | as câmaras, as suas imagens cinzentas e as zonas a ignorar entram; a observação sai")),
    ("ARMOR-NODE-RADAR", T("through the server | a través del servidor | über den Server | via le serveur | tramite il server | サーバー経由 | 经服务器 | através do servidor"), T("the radar tracks and the light of the nodes that cover each camera | las pistas de radar y la luz de los nodos que cubren cada cámara | die Radarspuren und das Licht der Knoten, die jede Kamera abdecken | les pistes radar et la lumière des nœuds qui couvrent chaque caméra | le tracce radar e la luce dei nodi che coprono ogni telecamera | 各カメラをカバーするノードのレーダートラックと明るさ | 覆盖每台摄像头的节点的雷达轨迹和光照 | as pistas de radar e a luz dos nós que cobrem cada câmara")),
    ("ARMOR-VISION", T("rules and masks (next step) | reglas y máscaras (siguiente paso) | Regeln und Masken (nächster Schritt) | règles et masques (prochaine étape) | regole e maschere (prossimo passo) | ルールとマスク（次の段階） | 规则与遮罩（下一步） | regras e máscaras (próximo passo)"), T("the zones, masks and rules the detection model will use | las zonas, máscaras y reglas que usará el modelo de detección | die Zonen, Masken und Regeln, die das Erkennungsmodell nutzen wird | les zones, masques et règles que le modèle de détection utilisera | le zone, maschere e regole che userà il modello di rilevamento | 検出モデルが使うゾーン、マスク、ルール | 检测模型将使用的区域、遮罩和规则 | as zonas, máscaras e regras que o modelo de deteção usará")),
    ("ARMOR-DEVOPS", T("installs it as a service | lo instala como servicio | installiert ihn als Dienst | l'installe comme service | lo installa come servizio | サービスとしてインストール | 将其安装为服务 | instala-o como serviço"), T("deployment on the CM5 test bench | despliegue en el banco de la CM5 | Bereitstellung auf dem CM5-Prüfstand | déploiement sur le banc d'essai CM5 | distribuzione sul banco di prova CM5 | CM5 テストベンチへのデプロイ | 在 CM5 测试台上部署 | implantação na bancada do CM5")),
]


def S(a, b):
    return (T(a), T(b))


SECURITY_ROWS = [
    S("The service acts on its own | El servicio actúa por su cuenta | Der Dienst handelt eigenmächtig | Le service agit de lui-même | Il servizio agisce di propria iniziativa | サービスが勝手に動く | 服务自行行动 | O serviço age por conta própria",
      "Never: every decision carries `authorizes_action = false`; the central server authenticates and authorises every action | Nunca: toda decisión lleva `authorizes_action = false`; el servidor central autentica y autoriza cada acción | Nie: jede Entscheidung trägt `authorizes_action = false`; der zentrale Server authentifiziert und autorisiert jede Aktion | Jamais : chaque décision porte `authorizes_action = false` ; le serveur central authentifie et autorise chaque action | Mai: ogni decisione porta `authorizes_action = false`; il server centrale autentica e autorizza ogni azione | 決してしません：すべての判定が `authorizes_action = false` を持ち、認証と認可は中央サーバーが行います | 绝不：每个判定都带 `authorizes_action = false`；每个动作都由中央服务器认证并授权 | Nunca: cada decisão leva `authorizes_action = false`; o servidor central autentica e autoriza cada ação"),
    S("The token crosses a network in clear | El token cruza una red en claro | Das Token läuft unverschlüsselt durchs Netz | Le jeton traverse un réseau en clair | Il token attraversa una rete in chiaro | トークンが平文でネットワークを通る | 令牌以明文穿过网络 | O token atravessa uma rede em claro",
      "`ARMOR_AI_SERVER_URL` must be `https://`, or `http://` to this same machine (`127.0.0.1`, `localhost`); otherwise the service refuses to start | `ARMOR_AI_SERVER_URL` debe ser `https://`, o `http://` a esta misma máquina (`127.0.0.1`, `localhost`); si no, el servicio se niega a arrancar | `ARMOR_AI_SERVER_URL` muss `https://` sein oder `http://` zur selben Maschine (`127.0.0.1`, `localhost`); sonst startet der Dienst nicht | `ARMOR_AI_SERVER_URL` doit être `https://`, ou `http://` vers cette même machine (`127.0.0.1`, `localhost`) ; sinon le service refuse de démarrer | `ARMOR_AI_SERVER_URL` deve essere `https://`, o `http://` verso questa stessa macchina (`127.0.0.1`, `localhost`); altrimenti il servizio rifiuta di partire | `ARMOR_AI_SERVER_URL` は `https://`、または同一マシンへの `http://`（`127.0.0.1`、`localhost`）でなければならず、違えばサービスは起動しません | `ARMOR_AI_SERVER_URL` 必须是 `https://`，或指向本机的 `http://`（`127.0.0.1`、`localhost`）；否则服务拒绝启动 | `ARMOR_AI_SERVER_URL` tem de ser `https://`, ou `http://` para esta mesma máquina (`127.0.0.1`, `localhost`); senão o serviço recusa arrancar"),
    S("A weak token | Un token débil | Ein schwaches Token | Un jeton faible | Un token debole | 弱いトークン | 弱令牌 | Um token fraco",
      "`ARMOR_AI_TOKEN` of at least 24 characters (the server asks the same) | `ARMOR_AI_TOKEN` de al menos 24 caracteres (el servidor exige lo mismo) | `ARMOR_AI_TOKEN` mit mindestens 24 Zeichen (der Server verlangt dasselbe) | `ARMOR_AI_TOKEN` d'au moins 24 caractères (le serveur exige la même chose) | `ARMOR_AI_TOKEN` di almeno 24 caratteri (lo richiede anche il server) | `ARMOR_AI_TOKEN` は 24 文字以上（サーバーも同じ要件） | `ARMOR_AI_TOKEN` 至少 24 个字符（服务器同样要求） | `ARMOR_AI_TOKEN` com pelo menos 24 caracteres (o servidor exige o mesmo)"),
    S("Huge answers from the server | Respuestas enormes del servidor | Riesige Antworten des Servers | Réponses énormes du serveur | Risposte enormi dal server | サーバーからの巨大な応答 | 服务器返回超大响应 | Respostas enormes do servidor",
      "The context is read up to 1 000 000 bytes and an answer to an observation up to 65 536; a frame is exactly 64 x 36 = 2304 bytes | El contexto se lee hasta 1 000 000 bytes y la respuesta a una observación hasta 65 536; un fotograma son exactamente 64 x 36 = 2304 bytes | Der Kontext wird bis 1 000 000 Bytes gelesen, die Antwort auf eine Beobachtung bis 65 536; ein Bild hat genau 64 x 36 = 2304 Bytes | Le contexte est lu jusqu'à 1 000 000 d'octets et une réponse à une observation jusqu'à 65 536 ; une image fait exactement 64 x 36 = 2304 octets | Il contesto si legge fino a 1 000 000 di byte e la risposta a un'osservazione fino a 65 536; un fotogramma è esattamente 64 x 36 = 2304 byte | コンテキストは 1 000 000 バイト、観察への応答は 65 536 バイトまで読み、フレームはちょうど 64 x 36 = 2304 バイト | 上下文最多读取 1 000 000 字节，对观察的响应最多 65 536 字节；一帧恰好是 64 x 36 = 2304 字节 | O contexto lê-se até 1 000 000 bytes e a resposta a uma observação até 65 536; uma imagem tem exatamente 64 x 36 = 2304 bytes"),
    S("Pictures kept | Imágenes guardadas | Gespeicherte Bilder | Images conservées | Immagini conservate | 保存される画像 | 被保存的图片 | Imagens guardadas",
      "The tiny grey frame is never stored | El fotograma gris pequeño no se guarda nunca | Das kleine Graubild wird nie gespeichert | La petite image grise n'est jamais conservée | Il piccolo fotogramma grigio non viene mai salvato | 小さなグレーフレームは保存されません | 小灰度帧从不保存 | A pequena imagem cinzenta nunca é guardada"),
    S("A tampered TensorRT engine | Un motor TensorRT manipulado | Eine manipulierte TensorRT-Engine | Un moteur TensorRT altéré | Un motore TensorRT manomesso | 改ざんされた TensorRT エンジン | 被篡改的 TensorRT 引擎 | Um motor TensorRT adulterado",
      "Only pre-built engines (`daylight`, `low_light`) that exist, are not empty and, with an `engines.json`, match their SHA-256; nothing is compiled or downloaded | Solo motores ya construidos (`daylight`, `low_light`) que existen, no están vacíos y, con un `engines.json`, coinciden en SHA-256; no se compila ni descarga nada | Nur fertig gebaute Engines (`daylight`, `low_light`), die existieren, nicht leer sind und mit einer `engines.json` ihrem SHA-256 entsprechen; nichts wird kompiliert oder geladen | Seulement des moteurs déjà construits (`daylight`, `low_light`) qui existent, ne sont pas vides et, avec un `engines.json`, correspondent à leur SHA-256 ; rien n'est compilé ni téléchargé | Solo motori già costruiti (`daylight`, `low_light`) che esistono, non sono vuoti e, con un `engines.json`, coincidono con lo SHA-256; non si compila né si scarica nulla | 既に構築済みのエンジン（`daylight`、`low_light`）のみ。存在し、空でなく、`engines.json` があれば SHA-256 が一致すること。コンパイルもダウンロードもしません | 只接受已构建好的引擎（`daylight`、`low_light`）：存在、非空，有 `engines.json` 时 SHA-256 须一致；不编译也不下载 | Só motores já construídos (`daylight`, `low_light`) que existam, não estejam vazios e, com um `engines.json`, coincidam no SHA-256; nada é compilado nem descarregado"),
    S("A false alarm from a change of light | Una falsa alarma por un cambio de luz | Ein Fehlalarm durch Lichtwechsel | Une fausse alarme due à un changement de lumière | Un falso allarme per un cambio di luce | 照明変化による誤報 | 光线变化造成的误报 | Um falso alarme por mudança de luz",
      "A change of more than 60 % of the picture is light, not movement; less than 1 % is not movement; pixel threshold 18; at least 64 pixels counted; at most 16 zones to ignore and a picture that is almost all ignored is not judged | Un cambio de más del 60 % de la imagen es luz, no movimiento; menos del 1 % no es movimiento; umbral de píxel 18; mínimo 64 píxeles contados; como mucho 16 zonas a ignorar y una imagen casi toda ignorada no se juzga | Eine Änderung von über 60 % des Bildes ist Licht, keine Bewegung; unter 1 % ist keine Bewegung; Pixelschwelle 18; mindestens 64 gezählte Pixel; höchstens 16 Ignorierzonen, und ein fast ganz ignoriertes Bild wird nicht beurteilt | Un changement de plus de 60 % de l'image est de la lumière, pas du mouvement ; moins de 1 % n'est pas du mouvement ; seuil de pixel 18 ; au moins 64 pixels comptés ; au plus 16 zones à ignorer et une image presque entièrement ignorée n'est pas jugée | Una variazione di oltre il 60 % dell'immagine è luce, non movimento; sotto l'1 % non è movimento; soglia di pixel 18; almeno 64 pixel contati; al massimo 16 zone da ignorare e un'immagine quasi tutta ignorata non viene giudicata | 画像の 60 % を超える変化は光であり動きではない。1 % 未満は動きではない。画素のしきい値は 18、カウントは最低 64 画素、無視ゾーンは最大 16、ほぼ全面が無視された画像は判定しない | 画面超过 60 % 的变化是光线而非运动；不足 1 % 不算运动；像素阈值 18；至少统计 64 个像素；最多 16 个忽略区，几乎全被忽略的画面不做判断 | Uma mudança de mais de 60 % da imagem é luz, não movimento; menos de 1 % não é movimento; limiar de píxel 18; pelo menos 64 píxeis contados; no máximo 16 zonas a ignorar e uma imagem quase toda ignorada não é julgada"),
    S("Day and night flicker; stale data; a hostile JSON line | Parpadeo día/noche; datos viejos; una línea JSON hostil | Tag/Nacht-Flackern; veraltete Daten; eine feindliche JSON-Zeile | Papillotement jour/nuit ; données périmées ; une ligne JSON hostile | Sfarfallio giorno/notte; dati vecchi; una riga JSON ostile | 昼夜のちらつき、古いデータ、悪意ある JSON 行 | 昼夜抖动；过期数据；恶意 JSON 行 | Cintilação dia/noite; dados antigos; uma linha JSON hostil",
      "Hysteresis (low light under 30 lux, daylight again over 60 lux, never twice within 30 s, lux up to 200 000); an observation older than 10 s never raises an alert; a JSON line over 4096 bytes is refused and the stream goes on | Histéresis (poca luz bajo 30 lux, luz de día de nuevo sobre 60 lux, nunca dos veces en 30 s, lux hasta 200 000); una observación de más de 10 s nunca da alerta; una línea JSON de más de 4096 bytes se rechaza y el flujo sigue | Hysterese (wenig Licht unter 30 Lux, wieder Tag über 60 Lux, nie zweimal in 30 s, Lux bis 200 000); eine Beobachtung über 10 s löst nie einen Alarm aus; eine JSON-Zeile über 4096 Bytes wird abgelehnt, der Strom läuft weiter | Hystérésis (faible lumière sous 30 lux, jour de nouveau au-dessus de 60 lux, jamais deux fois en 30 s, lux jusqu'à 200 000) ; une observation de plus de 10 s ne déclenche jamais d'alerte ; une ligne JSON de plus de 4096 octets est refusée et le flux continue | Isteresi (poca luce sotto 30 lux, di nuovo giorno sopra 60 lux, mai due volte in 30 s, lux fino a 200 000); un'osservazione più vecchia di 10 s non dà mai allarme; una riga JSON oltre 4096 byte è rifiutata e il flusso continua | ヒステリシス（30 lux 未満で低照度、60 lux 超で昼間に戻り、30 秒以内に 2 回は切り替えず、最大 200 000 lux）。10 秒より古い観察は警報にしません。4096 バイトを超える JSON 行は拒否し、ストリームは続きます | 迟滞（低于 30 lux 为弱光，高于 60 lux 才回到白天，30 秒内不会切换两次，照度至多 200 000）；超过 10 秒的观察从不触发警报；超过 4096 字节的 JSON 行被拒绝，流继续 | Histerese (pouca luz abaixo de 30 lux, dia outra vez acima de 60 lux, nunca duas vezes em 30 s, lux até 200 000); uma observação com mais de 10 s nunca dá alerta; uma linha JSON com mais de 4096 bytes é recusada e o fluxo continua"),
]

IFACE = [
    ("`GET /api/v1/ai/context`", T("token `ARMOR_AI_TOKEN` | token `ARMOR_AI_TOKEN` | Token `ARMOR_AI_TOKEN` | jeton `ARMOR_AI_TOKEN` | token `ARMOR_AI_TOKEN` | トークン `ARMOR_AI_TOKEN` | 令牌 `ARMOR_AI_TOKEN` | token `ARMOR_AI_TOKEN`"), T("the houses: nodes and cameras, and the zones to ignore of each camera | las casas: nodos y cámaras, y las zonas a ignorar de cada cámara | die Häuser: Knoten und Kameras sowie die Ignorierzonen jeder Kamera | les maisons : nœuds et caméras, et les zones à ignorer de chaque caméra | le case: nodi e telecamere, e le zone da ignorare di ogni telecamera | 家ごとのノードとカメラ、各カメラの無視ゾーン | 各住宅的节点和摄像头，以及每台摄像头的忽略区 | as casas: nós e câmaras, e as zonas a ignorar de cada câmara")),
    ("`GET /api/v1/ai/cameras/<id>/frame`", T("same | el mismo | dasselbe | le même | lo stesso | 同じ | 同上 | o mesmo"), T("the 64 x 36 grey frame of a camera (2304 bytes) | el fotograma gris de 64 x 36 de una cámara (2304 bytes) | das 64 x 36 Graubild einer Kamera (2304 Bytes) | l'image grise 64 x 36 d'une caméra (2304 octets) | il fotogramma grigio 64 x 36 di una telecamera (2304 byte) | カメラの 64 x 36 グレーフレーム（2304 バイト） | 摄像头的 64 x 36 灰度帧（2304 字节） | a imagem cinzenta de 64 x 36 de uma câmara (2304 bytes)")),
    ("`POST /api/v1/ai/observations`", T("same | el mismo | dasselbe | le même | lo stesso | 同じ | 同上 | o mesmo"), T("the report: what it saw, the severity and the reasons | el informe: lo que vio, la gravedad y las razones | der Bericht: was sie sah, der Schweregrad und die Gründe | le rapport : ce qu'elle a vu, la gravité et les raisons | il rapporto: cosa ha visto, la gravità e i motivi | 報告：見たもの、重大度、理由 | 报告：看到了什么、严重程度和原因 | o relatório: o que viu, a gravidade e as razões")),
    ("`python -m armor_server_ai.service [--once]`", "-", T("the observation service; `--once` makes one pass and ends | el servicio de observación; `--once` hace una pasada y termina | der Beobachtungsdienst; `--once` macht einen Durchgang und endet | le service d'observation ; `--once` fait une passe et s'arrête | il servizio di osservazione; `--once` fa un passaggio e termina | 観察サービス。`--once` は 1 巡して終了 | 观察服务；`--once` 只运行一轮就结束 | o serviço de observação; `--once` faz uma passagem e termina")),
    ("`python -m armor_server_ai.cli [--radar-tracks N]`", "-", T("JSON lines on standard input (`{\"label\", \"confidence\", \"lux\", \"radar_tracks\"}`), one numbered and explained decision per line | líneas JSON por la entrada estándar (`{\"label\", \"confidence\", \"lux\", \"radar_tracks\"}`), una decisión numerada y explicada por línea | JSON-Zeilen auf der Standardeingabe (`{\"label\", \"confidence\", \"lux\", \"radar_tracks\"}`), je Zeile eine nummerierte, erklärte Entscheidung | lignes JSON sur l'entrée standard (`{\"label\", \"confidence\", \"lux\", \"radar_tracks\"}`), une décision numérotée et expliquée par ligne | righe JSON sullo standard input (`{\"label\", \"confidence\", \"lux\", \"radar_tracks\"}`), una decisione numerata e spiegata per riga | 標準入力の JSON 行（`{\"label\", \"confidence\", \"lux\", \"radar_tracks\"}`）に対し、行ごとに番号付きで説明付きの判定 | 标准输入的 JSON 行（`{\"label\", \"confidence\", \"lux\", \"radar_tracks\"}`），每行一个带编号并有说明的判定 | linhas JSON na entrada padrão (`{\"label\", \"confidence\", \"lux\", \"radar_tracks\"}`), uma decisão numerada e explicada por linha")),
]
IFACE_NOTE = P("A decision is `{severity: ignore | review | high, reasons, authorizes_action: false}`. Labels: `person`, `vehicle`, `animal`, `unknown`, `motion`. **Fusion:** `high` is a person with confidence of 0.80 or more and at least one radar track, or strong movement and a radar track that agree; `review` is a confident detection (0.55 in daylight, 0.45 in low light) or a radar track with nothing seen; simple movement counts a radar track only with 30 % of certainty (about 3 % of the picture).",
               "Una decisión es `{severity: ignore | review | high, reasons, authorizes_action: false}`. Etiquetas: `person`, `vehicle`, `animal`, `unknown`, `motion`. **Fusión:** `high` es una persona con confianza de 0,80 o más y al menos una pista de radar, o un movimiento fuerte y una pista de radar que coinciden; `review` es una detección confiada (0,55 de día, 0,45 con poca luz) o una pista de radar sin nada visto; el movimiento simple cuenta una pista de radar solo con un 30 % de certeza (cerca del 3 % de la imagen).",
               "Eine Entscheidung ist `{severity: ignore | review | high, reasons, authorizes_action: false}`. Labels: `person`, `vehicle`, `animal`, `unknown`, `motion`. **Fusion:** `high` ist eine Person mit Konfidenz ab 0,80 und mindestens einer Radarspur oder starke Bewegung und eine übereinstimmende Radarspur; `review` ist eine sichere Erkennung (0,55 bei Tag, 0,45 bei wenig Licht) oder eine Radarspur ohne Sichtung; einfache Bewegung zählt eine Radarspur nur ab 30 % Sicherheit (etwa 3 % des Bildes).",
               "Une décision est `{severity: ignore | review | high, reasons, authorizes_action: false}`. Étiquettes : `person`, `vehicle`, `animal`, `unknown`, `motion`. **Fusion :** `high` est une personne avec une confiance d'au moins 0,80 et au moins une piste radar, ou un fort mouvement et une piste radar qui concordent ; `review` est une détection confiante (0,55 de jour, 0,45 en faible lumière) ou une piste radar sans rien de vu ; le simple mouvement ne compte une piste radar qu'à 30 % de certitude (environ 3 % de l'image).",
               "Una decisione è `{severity: ignore | review | high, reasons, authorizes_action: false}`. Etichette: `person`, `vehicle`, `animal`, `unknown`, `motion`. **Fusione:** `high` è una persona con confidenza di almeno 0,80 e almeno una traccia radar, oppure un forte movimento e una traccia radar concordi; `review` è un rilevamento sicuro (0,55 di giorno, 0,45 con poca luce) o una traccia radar senza nulla di visto; il semplice movimento conta una traccia radar solo con il 30 % di certezza (circa il 3 % dell'immagine).",
               "判定は `{severity: ignore | review | high, reasons, authorizes_action: false}` です。ラベル：`person`、`vehicle`、`animal`、`unknown`、`motion`。**融合：** `high` は信頼度 0.80 以上の人物かつレーダートラック 1 本以上、または強い動きとレーダートラックの一致。`review` は確かな検出（昼 0.55、低照度 0.45）、または何も見えないレーダートラック。単なる動きは確信度 30 %（画像の約 3 %）以上のときだけレーダートラックを数えます。",
               "判定为 `{severity: ignore | review | high, reasons, authorizes_action: false}`。标签：`person`、`vehicle`、`animal`、`unknown`、`motion`。**融合：** `high` 是置信度不低于 0.80 且至少有一条雷达轨迹的人，或强运动与雷达轨迹一致；`review` 是有把握的检测（白天 0.55、弱光 0.45）或看不到任何东西的雷达轨迹；单纯的运动只有在 30 % 把握（约占画面 3 %）时才计入雷达轨迹。",
               "Uma decisão é `{severity: ignore | review | high, reasons, authorizes_action: false}`. Etiquetas: `person`, `vehicle`, `animal`, `unknown`, `motion`. **Fusão:** `high` é uma pessoa com confiança de 0,80 ou mais e pelo menos uma pista de radar, ou movimento forte e uma pista de radar que coincidam; `review` é uma deteção confiante (0,55 de dia, 0,45 com pouca luz) ou uma pista de radar sem nada visto; o movimento simples só conta uma pista de radar com 30 % de certeza (cerca de 3 % da imagem).")

CFG = [
    ("`ARMOR_AI_TOKEN`", T("yes (24+ characters) | sí (24+ caracteres) | ja (24+ Zeichen) | oui (24+ caractères) | sì (24+ caratteri) | 必須（24 文字以上） | 是（24 个以上字符） | sim (24+ caracteres)"), T("the token the server gave the service | el token que el servidor dio al servicio | das Token, das der Server dem Dienst gab | le jeton que le serveur a donné au service | il token che il server ha dato al servizio | サーバーがサービスに渡したトークン | 服务器给服务的令牌 | o token que o servidor deu ao serviço")),
    ("`ARMOR_AI_SERVER_URL`", "http://127.0.0.1:18080", T("the server; `https://` or this same machine | el servidor; `https://` o esta misma máquina | der Server; `https://` oder dieselbe Maschine | le serveur ; `https://` ou cette même machine | il server; `https://` o questa stessa macchina | サーバー。`https://` か同一マシン | 服务器；`https://` 或本机 | o servidor; `https://` ou esta mesma máquina")),
    ("`ARMOR_AI_INTERVAL_S`", "3 (1-60)", T("seconds between passes; with many cameras the pass is spaced out to stay under 200 frames a minute | segundos entre pasadas; con muchas cámaras la pasada se alarga para no pasar de 200 imágenes por minuto | Sekunden zwischen Durchgängen; bei vielen Kameras wird der Durchgang gestreckt, um unter 200 Bildern pro Minute zu bleiben | secondes entre les passes ; avec beaucoup de caméras la passe s'allonge pour rester sous 200 images par minute | secondi tra i passaggi; con molte telecamere il passaggio si allunga per restare sotto 200 immagini al minuto | 巡回の間隔（秒）。カメラが多いと毎分 200 フレーム以内に収めるため間隔が延びます | 两轮之间的秒数；摄像头多时会拉长，使每分钟不超过 200 帧 | segundos entre passagens; com muitas câmaras a passagem alarga-se para não passar de 200 imagens por minuto")),
    ("`ARMOR_AI_CONFIRM_FRAMES`", "2 (1-20)", T("frames in a row that must show movement before it is told | fotogramas seguidos que deben mostrar movimiento antes de avisar | aufeinanderfolgende Bilder, die Bewegung zeigen müssen, bevor gemeldet wird | images consécutives qui doivent montrer du mouvement avant d'avertir | fotogrammi consecutivi che devono mostrare movimento prima di segnalare | 報告前に動きを示す必要がある連続フレーム数 | 报告前必须连续显示运动的帧数 | imagens seguidas que têm de mostrar movimento antes de avisar")),
    ("`ARMOR_AI_COOLDOWN_S`", "60 (0-3600)", T("seconds before the same camera is told again | segundos antes de avisar otra vez de la misma cámara | Sekunden, bevor dieselbe Kamera erneut gemeldet wird | secondes avant de signaler à nouveau la même caméra | secondi prima di segnalare di nuovo la stessa telecamera | 同じカメラを再報告するまでの秒数 | 同一摄像头再次报告前的秒数 | segundos antes de avisar outra vez da mesma câmara")),
]
CFG_NOTE = P("A value out of range stops the service with `<NAME> must be between a and b`. The thresholds of the decision (0.80, 0.55, 0.45, the radar bar of 30 %) and of the movement (18, 1 %, 60 %) are constants of the code described in [docs/INFERENCE_BOUNDARY.md](docs/INFERENCE_BOUNDARY.md); the settings of the service are in [docs/SERVICE.md](docs/SERVICE.md).",
             "Un valor fuera de rango detiene el servicio con `<NOMBRE> must be between a and b`. Los umbrales de la decisión (0,80, 0,55, 0,45, la barra del radar del 30 %) y del movimiento (18, 1 %, 60 %) son constantes del código descritas en [docs/INFERENCE_BOUNDARY.md](docs/INFERENCE_BOUNDARY.md); los ajustes del servicio están en [docs/SERVICE.md](docs/SERVICE.md).",
             "Ein Wert außerhalb des Bereichs stoppt den Dienst mit `<NAME> must be between a and b`. Die Schwellen der Entscheidung (0,80, 0,55, 0,45, die Radarschwelle von 30 %) und der Bewegung (18, 1 %, 60 %) sind Konstanten im Code, beschrieben in [docs/INFERENCE_BOUNDARY.md](docs/INFERENCE_BOUNDARY.md); die Einstellungen des Dienstes stehen in [docs/SERVICE.md](docs/SERVICE.md).",
             "Une valeur hors plage arrête le service avec `<NOM> must be between a and b`. Les seuils de la décision (0,80, 0,55, 0,45, la barre radar de 30 %) et du mouvement (18, 1 %, 60 %) sont des constantes du code décrites dans [docs/INFERENCE_BOUNDARY.md](docs/INFERENCE_BOUNDARY.md) ; les réglages du service sont dans [docs/SERVICE.md](docs/SERVICE.md).",
             "Un valore fuori intervallo ferma il servizio con `<NOME> must be between a and b`. Le soglie della decisione (0,80, 0,55, 0,45, la barra radar del 30 %) e del movimento (18, 1 %, 60 %) sono costanti del codice descritte in [docs/INFERENCE_BOUNDARY.md](docs/INFERENCE_BOUNDARY.md); le impostazioni del servizio sono in [docs/SERVICE.md](docs/SERVICE.md).",
             "範囲外の値があると、サービスは `<名前> must be between a and b` で停止します。判定のしきい値（0.80、0.55、0.45、レーダーの 30 %）と動きのしきい値（18、1 %、60 %）はコード内の定数で、[docs/INFERENCE_BOUNDARY.md](docs/INFERENCE_BOUNDARY.md) に記載されています。サービスの設定は [docs/SERVICE.md](docs/SERVICE.md) にあります。",
             "取值超出范围时，服务会以 `<名称> must be between a and b` 停止。判定阈值（0.80、0.55、0.45，雷达门槛 30 %）和运动阈值（18、1 %、60 %）是代码中的常量，见 [docs/INFERENCE_BOUNDARY.md](docs/INFERENCE_BOUNDARY.md)；服务的设置见 [docs/SERVICE.md](docs/SERVICE.md)。",
             "Um valor fora do intervalo pára o serviço com `<NOME> must be between a and b`. Os limiares da decisão (0,80, 0,55, 0,45, a barra do radar de 30 %) e do movimento (18, 1 %, 60 %) são constantes do código descritas em [docs/INFERENCE_BOUNDARY.md](docs/INFERENCE_BOUNDARY.md); as definições do serviço estão em [docs/SERVICE.md](docs/SERVICE.md).")

QUICK_LEAD = P("**Requirements:** Python 3.11+ (standard library only). Optional: a Jetson Orin NX with TensorRT engines (not proven).", "**Requisitos:** Python 3.11+ (solo biblioteca estándar). Opcional: una Jetson Orin NX con motores TensorRT (no probado).", "**Voraussetzungen:** Python 3.11+ (nur Standardbibliothek). Optional: ein Jetson Orin NX mit TensorRT-Engines (nicht erprobt).",
               "**Prérequis :** Python 3.11+ (bibliothèque standard seule). Facultatif : un Jetson Orin NX avec des moteurs TensorRT (non éprouvé).", "**Requisiti:** Python 3.11+ (solo libreria standard). Facoltativo: un Jetson Orin NX con motori TensorRT (non provato).", "**要件：** Python 3.11+（標準ライブラリのみ）。任意：TensorRT エンジンを載せた Jetson Orin NX（未検証）。",
               "**要求：** Python 3.11+（仅标准库）。可选：带 TensorRT 引擎的 Jetson Orin NX（未验证）。", "**Requisitos:** Python 3.11+ (só biblioteca padrão). Opcional: um Jetson Orin NX com motores TensorRT (não provado).")
QUICK_CODE = [
    ('$env:PYTHONPATH = "src"', ""),
    ("python -m unittest discover -s tests", T("80 tests | 80 pruebas | 80 Tests | 80 tests | 80 test | 80 件 | 80 项 | 80 testes")),
    ("""echo '{"label":"person","confidence":0.9,"lux":4,"radar_tracks":1}' | python -m armor_server_ai.cli""", T("one decision from a line | una decisión desde una línea | eine Entscheidung aus einer Zeile | une décision depuis une ligne | una decisione da una riga | 1 行から判定を得る | 从一行得到一个判定 | uma decisão a partir de uma linha")),
    ("python -m armor_server_ai.service --once", T("one pass of the observation service | una pasada del servicio de observación | ein Durchgang des Beobachtungsdienstes | une passe du service d'observation | un passaggio del servizio di osservazione | 観察サービスを 1 巡 | 观察服务运行一轮 | uma passagem do serviço de observação")),
]
QUICK_AFTER = P("See the [inference boundary](docs/INFERENCE_BOUNDARY.md) and the [service](docs/SERVICE.md).", "Mira el [límite de la inferencia](docs/INFERENCE_BOUNDARY.md) y el [servicio](docs/SERVICE.md).", "Siehe die [Grenze der Inferenz](docs/INFERENCE_BOUNDARY.md) und den [Dienst](docs/SERVICE.md).", "Voir la [frontière de l'inférence](docs/INFERENCE_BOUNDARY.md) et le [service](docs/SERVICE.md).",
                "Vedi il [confine dell'inferenza](docs/INFERENCE_BOUNDARY.md) e il [servizio](docs/SERVICE.md).", "[推論の境界](docs/INFERENCE_BOUNDARY.md)と[サービス](docs/SERVICE.md)を参照してください。", "请参阅[推理边界](docs/INFERENCE_BOUNDARY.md)和[服务](docs/SERVICE.md)。", "Consulte o [limite da inferência](docs/INFERENCE_BOUNDARY.md) e o [serviço](docs/SERVICE.md).")

TEST_TABLE = [
    ("`test_service.py`", "16", T("movement, the watcher, cooldown and which radars count | movimiento, el vigilante, el enfriamiento y qué radares cuentan | Bewegung, der Beobachter, Abkühlzeit und welche Radare zählen | mouvement, le surveillant, le délai et quels radars comptent | movimento, il sorvegliante, il raffreddamento e quali radar contano | 動き、監視ループ、クールダウン、どのレーダーを数えるか | 运动、监视器、冷却时间以及哪些雷达计入 | movimento, o vigilante, o arrefecimento e que radares contam")),
    ("`test_service_http.py`", "21", T("the link to the server, the address rules, the passes and the settings | el enlace con el servidor, las reglas de dirección, las pasadas y los ajustes | die Verbindung zum Server, Adressregeln, Durchgänge und Einstellungen | la liaison avec le serveur, les règles d'adresse, les passes et les réglages | il collegamento col server, le regole sull'indirizzo, i passaggi e le impostazioni | サーバーとの接続、アドレス規則、巡回、設定 | 与服务器的连接、地址规则、轮次与设置 | a ligação ao servidor, as regras de endereço, as passagens e as definições")),
    ("`test_vision_profile.py`", "20", T("day and night with hysteresis, the fusion policy and the worker | día y noche con histéresis, la política de fusión y el trabajador | Tag und Nacht mit Hysterese, die Fusionsrichtlinie und der Arbeiter | jour et nuit avec hystérésis, la politique de fusion et le travailleur | giorno e notte con isteresi, la politica di fusione e il worker | ヒステリシス付き昼夜、融合ポリシー、ワーカー | 带迟滞的昼夜、融合策略与工作进程 | dia e noite com histerese, a política de fusão e o trabalhador")),
    ("`test_cli_worker.py`", "10", T("the JSON-lines worker and its bad lines | el trabajador de líneas JSON y sus líneas malas | der JSON-Lines-Arbeiter und seine fehlerhaften Zeilen | le travailleur JSON lignes et ses lignes erronées | il worker di righe JSON e le sue righe errate | JSON Lines ワーカーと不正な行 | JSON 行工作进程及其坏行 | o trabalhador de linhas JSON e as suas linhas más")),
    ("`test_ignore_zones.py`, `test_registry.py`", "13", T("zones to ignore, and the checked TensorRT engines | zonas a ignorar y motores TensorRT comprobados | Ignorierzonen und geprüfte TensorRT-Engines | zones à ignorer et moteurs TensorRT vérifiés | zone da ignorare e motori TensorRT verificati | 無視ゾーンと検証済み TensorRT エンジン | 忽略区与经校验的 TensorRT 引擎 | zonas a ignorar e motores TensorRT verificados")),
]
TEST_NOTE = P("GitHub Actions runs the A.R.M.O.R. baseline on every push and pull request: the validation of the manifest, version, changelog and README parity, then the project's own build and tests. The sources pass the type checker: `python -m mypy src` reports nothing.",
              "GitHub Actions ejecuta la base de A.R.M.O.R. en cada push y pull request: la validación del manifiesto, la versión, el registro de cambios y la paridad de los README, y luego la compilación y las pruebas del propio proyecto. Los fuentes pasan el comprobador de tipos: `python -m mypy src` no informa de nada.",
              "GitHub Actions führt bei jedem Push und Pull Request die A.R.M.O.R.-Basis aus: die Prüfung von Manifest, Version, Änderungsprotokoll und README-Parität, dann den eigenen Build und die eigenen Tests des Projekts. Die Quellen bestehen die Typprüfung: `python -m mypy src` meldet nichts.",
              "GitHub Actions exécute la base A.R.M.O.R. à chaque push et pull request : la validation du manifeste, de la version, du journal des modifications et de la parité des README, puis le build et les tests propres au projet. Les sources passent le vérificateur de types : `python -m mypy src` ne signale rien.",
              "GitHub Actions esegue la base A.R.M.O.R. a ogni push e pull request: la validazione di manifesto, versione, registro delle modifiche e parità dei README, poi la compilazione e i test del progetto. I sorgenti superano il controllo dei tipi: `python -m mypy src` non segnala nulla.",
              "GitHub Actions は push と pull request のたびに A.R.M.O.R. の基本検査（マニフェスト、バージョン、変更履歴、README の一致）と、プロジェクト自身のビルドとテストを実行します。 ソースは型チェッカーを通ります。`python -m mypy src` は何も報告しません。",
              "GitHub Actions 在每次推送和拉取请求时运行 A.R.M.O.R. 基线：清单、版本、更新日志和 README 一致性的校验，然后是项目自身的构建和测试。 源代码通过类型检查：`python -m mypy src` 没有任何报告。",
              "O GitHub Actions executa a base do A.R.M.O.R. em cada push e pull request: a validação do manifesto, da versão, do registo de alterações e da paridade dos README, e depois a compilação e os testes do próprio projeto. As fontes passam o verificador de tipos: `python -m mypy src` não reporta nada.")

BUILD = P("It is plain Python: nothing to compile. The version lives in `pyproject.toml`, in `armor.project.json` and in the README badge (read from the manifest); each version has its entry in [CHANGELOG.md](CHANGELOG.md). Releases are published on GitHub.",
          "Es Python puro: no hay nada que compilar. La versión vive en `pyproject.toml`, en `armor.project.json` y en la insignia del README (leída del manifiesto); cada versión tiene su entrada en [CHANGELOG.md](CHANGELOG.md). Las versiones se publican en GitHub.",
          "Es ist reines Python: Es gibt nichts zu kompilieren. Die Version steht in `pyproject.toml`, in `armor.project.json` und im README-Badge (aus dem Manifest gelesen); jede Version hat ihren Eintrag in [CHANGELOG.md](CHANGELOG.md). Releases werden auf GitHub veröffentlicht.",
          "C'est du Python pur : rien à compiler. La version se trouve dans `pyproject.toml`, dans `armor.project.json` et dans le badge du README (lu depuis le manifeste) ; chaque version a son entrée dans [CHANGELOG.md](CHANGELOG.md). Les versions sont publiées sur GitHub.",
          "È Python puro: nulla da compilare. La versione risiede in `pyproject.toml`, in `armor.project.json` e nel badge del README (letto dal manifesto); ogni versione ha la sua voce in [CHANGELOG.md](CHANGELOG.md). Le versioni sono pubblicate su GitHub.",
          "純粋な Python なので、コンパイルするものはありません。バージョンは `pyproject.toml`、`armor.project.json`、README のバッジ（マニフェストから読み取り）にあり、各バージョンには [CHANGELOG.md](CHANGELOG.md) にエントリーがあります。リリースは GitHub で公開されます。",
          "这是纯 Python：无需编译。版本记录在 `pyproject.toml`、`armor.project.json` 和 README 徽章中（读取自清单）；每个版本在 [CHANGELOG.md](CHANGELOG.md) 中都有对应条目。发布版本发布在 GitHub 上。",
          "É Python puro: não há nada para compilar. A versão está em `pyproject.toml`, em `armor.project.json` e no emblema do README (lido do manifesto); cada versão tem a sua entrada em [CHANGELOG.md](CHANGELOG.md). As versões são publicadas no GitHub.")

TROUBLE = [
    ("`armor-ai: watching, every N s`", T("the service started | el servicio arrancó | der Dienst ist gestartet | le service a démarré | il servizio è partito | サービスが起動した | 服务已启动 | o serviço arrancou"), T("nothing to do | nada que hacer | nichts zu tun | rien à faire | niente da fare | 対処不要 | 无需处理 | nada a fazer")),
    ("`ARMOR_AI_TOKEN (at least 24 characters) is needed`", T("the token is missing or short | falta el token o es corto | das Token fehlt oder ist kurz | le jeton manque ou est court | manca il token o è corto | トークンがない、または短い | 缺少令牌或令牌太短 | falta o token ou é curto"), T("set a token of 24+ characters, the same one the server has | define un token de 24+ caracteres, el mismo que tiene el servidor | ein Token mit 24+ Zeichen setzen, dasselbe wie am Server | définissez un jeton de 24+ caractères, le même que celui du serveur | imposta un token di 24+ caratteri, lo stesso del server | 24 文字以上で、サーバーと同じトークンを設定 | 设置 24 个以上字符的令牌，与服务器所持相同 | defina um token de 24+ caracteres, o mesmo que o servidor tem")),
    ("`ARMOR_AI_SERVER_URL must be https://...`", T("the address would send the token in clear over a network | la dirección enviaría el token en claro por una red | die Adresse würde das Token unverschlüsselt durchs Netz senden | l'adresse enverrait le jeton en clair sur un réseau | l'indirizzo manderebbe il token in chiaro su una rete | そのアドレスではトークンが平文でネットワークを通る | 该地址会让令牌以明文穿过网络 | o endereço enviaria o token em claro por uma rede"), T("use `https://`, or `http://127.0.0.1` on the same machine | usa `https://`, o `http://127.0.0.1` en la misma máquina | `https://` verwenden oder `http://127.0.0.1` auf derselben Maschine | utilisez `https://`, ou `http://127.0.0.1` sur la même machine | usa `https://`, o `http://127.0.0.1` sulla stessa macchina | `https://` か、同一マシンの `http://127.0.0.1` を使う | 使用 `https://`，或同机的 `http://127.0.0.1` | use `https://`, ou `http://127.0.0.1` na mesma máquina")),
    ("`armor-ai: the observation of <camera> could not be told (<code>)`", T("the report did not reach the server (`unreachable`, `unauthorized`...) | el informe no llegó al servidor (`unreachable`, `unauthorized`...) | der Bericht erreichte den Server nicht (`unreachable`, `unauthorized`...) | le rapport n'a pas atteint le serveur (`unreachable`, `unauthorized`...) | il rapporto non è arrivato al server (`unreachable`, `unauthorized`...) | 報告がサーバーに届かなかった（`unreachable`、`unauthorized` など） | 报告未到达服务器（`unreachable`、`unauthorized` 等） | o relatório não chegou ao servidor (`unreachable`, `unauthorized`...)"), T("fix the cause; the next movement is told without waiting for the cooldown; `armor-ai: the server answers again` says when it is over | arregla la causa; el siguiente movimiento se avisa sin esperar al enfriamiento; `armor-ai: the server answers again` dice cuándo termina | die Ursache beheben; die nächste Bewegung wird ohne Abkühlzeit gemeldet; `armor-ai: the server answers again` meldet das Ende | corrigez la cause ; le mouvement suivant est signalé sans attendre le délai ; `armor-ai: the server answers again` dit quand c'est fini | correggi la causa; il prossimo movimento viene segnalato senza attendere il raffreddamento; `armor-ai: the server answers again` dice quando è finita | 原因を直す。次の動きはクールダウンなしで報告され、`armor-ai: the server answers again` で復旧が分かる | 排除原因；下一次运动不等冷却时间就会报告，`armor-ai: the server answers again` 表示已恢复 | corrija a causa; o movimento seguinte é avisado sem esperar o arrefecimento; `armor-ai: the server answers again` diz quando acabou")),
    ("`radar and light sensors not counted: the site design lists no nodes for this camera`", T("the camera names no nodes in the site design | la cámara no nombra nodos en el diseño del emplazamiento | die Kamera nennt im Standortentwurf keine Knoten | la caméra ne nomme aucun nœud dans la conception du site | la telecamera non nomina nodi nel progetto del sito | サイト設計でカメラにノードが指定されていない | 场地设计中该摄像头没有指定节点 | a câmara não nomeia nós no desenho do local"), T("in the Site Designer of Studio, list the radar nodes that cover the camera | en el Diseñador de emplazamiento de Studio, indica los nodos de radar que cubren la cámara | im Standort-Designer von Studio die Radar-Knoten eintragen, die die Kamera abdecken | dans le concepteur de site de Studio, indiquez les nœuds radar qui couvrent la caméra | nel progettista del sito di Studio, indica i nodi radar che coprono la telecamera | Studio のサイトデザイナーで、カメラをカバーするレーダーノードを指定 | 在 Studio 的场地设计器中列出覆盖该摄像头的雷达节点 | no desenhador do local do Studio, indique os nós de radar que cobrem a câmara")),
]

ROADMAP = P(
    "**Known limits today**\n\n* There is no detection model: it cannot tell a person from a cat or a branch.\n* Nothing has run on a Jetson, with TensorRT or on a decoded RTSP stream there.\n* No independent security review.\n\n**Next**\n\n* A model that recognises a person, run on a Jetson Orin NX, using the zones, masks and rules of ARMOR-VISION.",
    "**Límites conocidos hoy**\n\n* No hay modelo de detección: no distingue una persona de un gato o de una rama.\n* Nada ha corrido en una Jetson, con TensorRT ni con un flujo RTSP decodificado allí.\n* Sin revisión de seguridad independiente.\n\n**Lo siguiente**\n\n* Un modelo que reconozca a una persona, ejecutado en una Jetson Orin NX, con las zonas, máscaras y reglas de ARMOR-VISION.",
    "**Bekannte Grenzen heute**\n\n* Es gibt kein Erkennungsmodell: Es kann eine Person nicht von einer Katze oder einem Ast unterscheiden.\n* Nichts lief auf einem Jetson, mit TensorRT oder auf einem dort dekodierten RTSP-Strom.\n* Keine unabhängige Sicherheitsprüfung.\n\n**Als Nächstes**\n\n* Ein Modell, das eine Person erkennt, auf einem Jetson Orin NX mit den Zonen, Masken und Regeln von ARMOR-VISION.",
    "**Limites connues aujourd'hui**\n\n* Il n'y a pas de modèle de détection : il ne distingue pas une personne d'un chat ou d'une branche.\n* Rien n'a tourné sur un Jetson, avec TensorRT ni sur un flux RTSP décodé là-bas.\n* Pas de revue de sécurité indépendante.\n\n**Prochainement**\n\n* Un modèle qui reconnaît une personne, exécuté sur un Jetson Orin NX, avec les zones, masques et règles d'ARMOR-VISION.",
    "**Limiti noti oggi**\n\n* Non esiste un modello di rilevamento: non distingue una persona da un gatto o da un ramo.\n* Nulla ha girato su un Jetson, con TensorRT o su un flusso RTSP decodificato lì.\n* Nessuna revisione di sicurezza indipendente.\n\n**Prossimi passi**\n\n* Un modello che riconosca una persona, eseguito su un Jetson Orin NX, con le zone, maschere e regole di ARMOR-VISION.",
    "**現時点の既知の制限**\n\n* 検出モデルはまだなく、人と猫や枝を区別できません。\n* Jetson、TensorRT、そこでデコードした RTSP ストリームでは何も動かしていません。\n* 第三者によるセキュリティレビューはありません。\n\n**今後**\n\n* 人を認識するモデルを Jetson Orin NX で動かし、ARMOR-VISION のゾーン、マスク、ルールを使う。",
    "**当前已知限制**\n\n* 还没有检测模型：分不清人、猫或树枝。\n* 在 Jetson 上、使用 TensorRT 或在那里解码的 RTSP 流，都没有运行过任何东西。\n* 没有独立的安全审查。\n\n**下一步**\n\n* 在 Jetson Orin NX 上运行能识别人的模型，使用 ARMOR-VISION 的区域、遮罩和规则。",
    "**Limites conhecidos hoje**\n\n* Não há modelo de deteção: não distingue uma pessoa de um gato ou de um ramo.\n* Nada correu num Jetson, com TensorRT nem num fluxo RTSP descodificado lá.\n* Sem revisão de segurança independente.\n\n**A seguir**\n\n* Um modelo que reconheça uma pessoa, executado num Jetson Orin NX, com as zonas, máscaras e regras do ARMOR-VISION.")

DOCS = [
    P("[Inference boundary](docs/INFERENCE_BOUNDARY.md): what is decided here and what is left to a model", "[Límite de la inferencia](docs/INFERENCE_BOUNDARY.md): qué se decide aquí y qué se deja a un modelo", "[Grenze der Inferenz](docs/INFERENCE_BOUNDARY.md): was hier entschieden wird und was einem Modell bleibt", "[Frontière de l'inférence](docs/INFERENCE_BOUNDARY.md) : ce qui se décide ici et ce qui est laissé à un modèle", "[Confine dell'inferenza](docs/INFERENCE_BOUNDARY.md): cosa si decide qui e cosa resta a un modello", "[推論の境界](docs/INFERENCE_BOUNDARY.md)：ここで決めること、モデルに任せること", "[推理边界](docs/INFERENCE_BOUNDARY.md)：这里决定什么，留给模型什么", "[Limite da inferência](docs/INFERENCE_BOUNDARY.md): o que se decide aqui e o que fica para um modelo"),
    P("[The service](docs/SERVICE.md): the observation service and its settings", "[El servicio](docs/SERVICE.md): el servicio de observación y sus ajustes", "[Der Dienst](docs/SERVICE.md): der Beobachtungsdienst und seine Einstellungen", "[Le service](docs/SERVICE.md) : le service d'observation et ses réglages", "[Il servizio](docs/SERVICE.md): il servizio di osservazione e le sue impostazioni", "[サービス](docs/SERVICE.md)：観察サービスとその設定", "[服务](docs/SERVICE.md)：观察服务及其设置", "[O serviço](docs/SERVICE.md): o serviço de observação e as suas definições"),
]


def build_lg(lg):
    bullets = "\n".join(f"* {b}" for b in L(lg, "bullets"))
    status = dict(LEGACY[lg]["status"])
    status["security"] = SEC_NOTE[lg]
    body = {
        "overview": bullets,
        "role": f"{L(lg, 'fit')}\n\n{table(lg, 'talks', ROLE_TABLE)}",
        "architecture": arch(lg, "ARMOR-SERVER-AI", "ARMOR-SERVER-AI architecture: what it asks the server, the observation service with its modules, and what it tells", None),
        "security": table(lg, "threat", SECURITY_ROWS),
        "interfaces": table(lg, "route", IFACE) + "\n\n" + IFACE_NOTE[lg],
        "configuration": table(lg, "setting", CFG) + "\n\n" + CFG_NOTE[lg],
        "quickstart": f"{QUICK_LEAD[lg]}\n\n" + code(lg, QUICK_CODE) + "\n\n" + QUICK_AFTER[lg],
        "testing": code(lg, [("python -m unittest discover -s tests", T("80 tests | 80 pruebas | 80 Tests | 80 tests | 80 test | 80 件 | 80 项 | 80 testes")), "python -I tools/armor_ci_validate.py"]) + "\n\n" + table(lg, "tests", TEST_TABLE) + "\n\n" + TEST_NOTE[lg],
        "build": BUILD[lg],
        "troubleshooting": table(lg, "trouble", TROUBLE),
        "structure": structure(lg, "ARMOR-SERVER-AI", tree=TREE[lg]),
        "roadmap": ROADMAP[lg],
    }
    return text_for(lg, tagline=L(lg, "tagline"), honest=L(lg, "honest"), glance=GLANCE, status=status, docs=DOCS, contributing_first=CONTRIB, body=body)


TEXT = {lg: build_lg(lg) for lg in LGS}
