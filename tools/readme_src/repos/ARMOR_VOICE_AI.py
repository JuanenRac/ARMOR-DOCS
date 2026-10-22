# The facts that do not depend on the language, and the words of every language, of ARMOR-VOICE-AI.
# Copyright (C) 2026 JuanenRac (Electro Hobby 3D). GPL-3.0-or-later.

FACTS = {
 "emoji": "🎙️",
 "badges": [
  [
   "Language",
   "Python%203.11%2B",
   "3776ab"
  ],
  [
   "Mode",
   "offline",
   "2ea44f"
  ],
  [
   "Languages",
   "8",
   "00E5FF"
  ],
  [
   "Tests",
   "83%20passing",
   "2ea44f"
  ]
 ],
 "diagram": "",
 "build": "```powershell\n$env:PYTHONPATH=\"src\"\npython -m unittest discover -s tests   # 83 tests\necho '{\"text\":\"arm the system\"}' | python -m armor_voice_ai.gateway\npython -m armor_voice_ai.service        # the local HTTP service the server asks (loopback only)\n```",
 "structure": "```text\nARMOR-VOICE-AI/\n├── src/armor_voice_ai/   phrases, intent, confirmation, session, gateway (stdin), service (HTTP), turn (speech to text, order, text to speech)\n├── tests/                gateway, languages, service and turn tests\n└── docs/                 SAFETY.md, SERVICE.md\n```",
 "tests": "83 (`python -m unittest discover -s tests`)",
 "requirements": [
  "Python 3.11+ (standard library only)",
  "optional: a speech-to-text and a text-to-speech command for `/v1/turn`"
 ]
}

TEXT = {
 "en": {
  "tagline": "Offline voice intents in eight languages, with a confirmation the caller cannot forge",
  "honest": "The intent rules, the eight languages, the signed confirmation tied to its speaker, the local service, the turn endpoint and the audit are real and tested (83 tests), and the server asks the service on the CM5 test bench. **No speech recognition or synthesis engine is part of this repository**: `/v1/turn` runs the commands you configure for them, and none has been tried with a real microphone yet; the touch panel that is meant to carry the assistant has not run on a board.",
  "bullets": [
   "**A closed allow-list of fifteen commands:** `status`, `silence`, `arm`, `disarm`, and the ones that ask - `alarms`, `nodes`, `cameras`, `radar`, `solar`, `electrical`, `network`, `time`, `help` - plus switching the lights on and off, in **eight languages** (English, Spanish, German, French, Italian, Japanese, Chinese and Portuguese), after normalising accents, punctuation and polite filler. Anything else, or anything ambiguous, is not understood.",
   "**A confirmation the service issues:** `arm` and `disarm` return a signed token on the first turn and are accepted only when a later turn echoes it for the same intent within 30 s, **for the same user**. It cannot be forged by the caller, a stale one is refused and the nonces of the unexpired ones are never forgotten to make room.",
   "**A local HTTP service:** `python -m armor_voice_ai.service` listens on the loopback address only, wants a token and answers `POST /v1/command` with the decision in the language asked for; the server's Services menu shows which version runs.",
   "**A turn endpoint:** `POST /v1/turn` takes a recording, runs the speech-to-text command you configure, runs the order through the engine and answers with a recording made by the text-to-speech command; the commands, the server address and its token come from the environment.",
   "**Decisions, not audio:** with `--audit-file` each decision records the intent, the outcome and a SHA-256 of the transcript, never audio or the raw words.",
   "**Recommendations only:** an accepted command is passed to ARMOR-SERVER, which still authenticates and authorises it; from the wall panel disarming by voice is never possible (the PIN is typed on the screen); from the app it follows the server's `ARMOR_DISARM_PIN` (set it to `required`)."
  ],
  "note": "See [voice safety](docs/SAFETY.md) and the [service](docs/SERVICE.md).",
  "fit": "ARMOR-VOICE-AI turns what is said into one of a closed list of commands and never does anything by itself: [ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER) asks it, then authenticates and authorises the command exactly as it would a click in [ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO). It is meant to live behind the microphone of the [ARMOR-HMI](https://github.com/JuanenRac/ARMOR-HMI) wall panel and answers the written and spoken assistant of the Android app.",
  "hardware": "Running as a service on the CM5 test bench, asked by the server; no microphone or speech engine has been tried"
 },
 "es": {
  "tagline": "Órdenes de voz sin conexión en ocho idiomas, con una confirmación que quien llama no puede falsificar",
  "honest": "Las reglas de intención, los ocho idiomas, la confirmación firmada ligada a quien habla, el servicio local, el punto de turno y la auditoría son reales y están probados (83 tests), y el servidor pregunta al servicio en el banco de pruebas de la CM5. **Ningún motor de reconocimiento ni de síntesis de voz forma parte de este repositorio**: `/v1/turn` ejecuta los comandos que configures para ellos, y ninguno se ha probado todavía con un micrófono real; el panel táctil pensado para llevar al asistente no ha corrido en una placa.",
  "bullets": [
   "**Una lista cerrada de quince comandos:** `status`, `silence`, `arm`, `disarm`, y los que preguntan - `alarms`, `nodes`, `cameras`, `radar`, `solar`, `electrical`, `network`, `time`, `help` - más encender y apagar las luces, en **ocho idiomas** (inglés, español, alemán, francés, italiano, japonés, chino y portugués), tras normalizar acentos, puntuación y muletillas de cortesía. Cualquier otra cosa, o cualquier cosa ambigua, no se entiende.",
   "**Una confirmación que emite el servicio:** `arm` y `disarm` devuelven un token firmado en el primer turno y solo se aceptan cuando un turno posterior lo repite para la misma intención en 30 s, **del mismo usuario**. El que llama no puede falsificarla, una caducada se rechaza y los nonces de las no caducadas nunca se olvidan para hacer sitio.",
   "**Un servicio HTTP local:** `python -m armor_voice_ai.service` escucha solo en la dirección de loopback, pide un token y responde `POST /v1/command` con la decisión en el idioma pedido; el menú Servicios del servidor muestra qué versión corre.",
   "**Un punto de turno:** `POST /v1/turn` recibe una grabación, ejecuta el comando de voz a texto que configures, pasa la orden por el motor y responde con una grabación hecha por el comando de texto a voz; los comandos, la dirección del servidor y su token vienen del entorno.",
   "**Decisiones, no audio:** con `--audit-file` cada decisión registra la intención, el resultado y un SHA-256 de la transcripción, nunca audio ni las palabras sin procesar.",
   "**Solo recomendaciones:** un comando aceptado se pasa a ARMOR-SERVER, que sigue autenticándolo y autorizándolo; desde el panel de pared desarmar por voz nunca es posible (el PIN se teclea en la pantalla); desde la app sigue `ARMOR_DISARM_PIN` del servidor (ponlo en `required`)."
  ],
  "note": "Véanse la [seguridad de la voz](docs/SAFETY.md) y el [servicio](docs/SERVICE.md).",
  "fit": "ARMOR-VOICE-AI convierte lo que se dice en uno de una lista cerrada de comandos y nunca hace nada por sí mismo: [ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER) le pregunta y luego autentica y autoriza el comando exactamente como un clic en [ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO). Está pensado para vivir tras el micrófono del panel de pared [ARMOR-HMI](https://github.com/JuanenRac/ARMOR-HMI) y atiende al asistente escrito y hablado de la app Android.",
  "hardware": "Corriendo como servicio en el banco de pruebas de la CM5, consultado por el servidor; no se ha probado ningún micrófono ni motor de voz",
  "requirements": [
   "Python 3.11+ (solo la biblioteca estándar)",
   "opcional: un comando de voz a texto y otro de texto a voz para `/v1/turn`"
  ]
 },
 "fr": {
  "tagline": "Intentions vocales hors ligne en huit langues, avec une confirmation que l'appelant ne peut pas falsifier",
  "honest": "Les règles d'intention, les huit langues, la confirmation signée liée à son locuteur, le service local, le point de tour et l'audit sont réels et testés (83 tests), et le serveur interroge le service sur le banc de test CM5. **Aucun moteur de reconnaissance ni de synthèse vocale ne fait partie de ce dépôt** : `/v1/turn` exécute les commandes que vous configurez pour eux, et aucun n'a encore été essayé avec un vrai microphone ; le panneau tactile censé porter l'assistant n'a pas tourné sur une carte.",
  "bullets": [
   "**Une liste fermée de quinze commandes :** `status`, `silence`, `arm`, `disarm`, et celles qui interrogent - `alarms`, `nodes`, `cameras`, `radar`, `solar`, `electrical`, `network`, `time`, `help` - plus allumer et éteindre les lumières, en **huit langues** (anglais, espagnol, allemand, français, italien, japonais, chinois et portugais), après normalisation des accents, de la ponctuation et des politesses. Tout le reste, ou tout ce qui est ambigu, n'est pas compris.",
   "**Une confirmation émise par le service :** `arm` et `disarm` renvoient un jeton signé au premier tour et ne sont acceptés que lorsqu'un tour suivant le répète pour la même intention en 30 s, **pour le même utilisateur**. L'appelant ne peut pas la falsifier, une confirmation périmée est refusée et les nonces de celles non périmées ne sont jamais oubliés pour faire de la place.",
   "**Un service HTTP local :** `python -m armor_voice_ai.service` n'écoute que sur l'adresse de boucle locale, exige un jeton et répond à `POST /v1/command` avec la décision dans la langue demandée ; le menu Services du serveur montre quelle version tourne.",
   "**Un point de tour :** `POST /v1/turn` reçoit un enregistrement, exécute la commande de reconnaissance vocale que vous configurez, passe l'ordre dans le moteur et répond avec un enregistrement fait par la commande de synthèse vocale ; les commandes, l'adresse du serveur et son jeton viennent de l'environnement.",
   "**Des décisions, pas de l'audio :** avec `--audit-file` chaque décision enregistre l'intention, le résultat et un SHA-256 de la transcription, jamais d'audio ni les mots bruts.",
   "**Des recommandations seulement :** une commande acceptée est transmise à ARMOR-SERVER, qui l'authentifie et l'autorise toujours ; depuis le panneau mural, désarmer à la voix n'est jamais possible (le PIN se saisit sur l'écran) ; depuis l'appli, cela suit `ARMOR_DISARM_PIN` du serveur (mettez-le à `required`)."
  ],
  "note": "Voir la [sécurité de la voix](docs/SAFETY.md) et le [service](docs/SERVICE.md).",
  "fit": "ARMOR-VOICE-AI transforme ce qui est dit en l'une des commandes d'une liste fermée et ne fait jamais rien de lui-même : [ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER) l'interroge, puis authentifie et autorise la commande exactement comme un clic dans [ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO). Il est destiné à vivre derrière le microphone du panneau mural [ARMOR-HMI](https://github.com/JuanenRac/ARMOR-HMI) et répond à l'assistant écrit et parlé de l'application Android.",
  "hardware": "Tourne comme service sur le banc de test CM5, interrogé par le serveur ; aucun microphone ni moteur vocal n'a été essayé",
  "requirements": [
   "Python 3.11+ (bibliothèque standard uniquement)",
   "facultatif : une commande de reconnaissance vocale et une de synthèse vocale pour `/v1/turn`"
  ]
 },
 "it": {
  "tagline": "Intenti vocali offline in otto lingue, con una conferma che chi chiama non può falsificare",
  "honest": "Le regole di intento, le otto lingue, la conferma firmata legata a chi parla, il servizio locale, l'endpoint di turno e l'audit sono reali e provati (83 test), e il server interroga il servizio sul banco di prova CM5. **Nessun motore di riconoscimento o sintesi vocale fa parte di questo repository**: `/v1/turn` esegue i comandi che configuri per essi, e nessuno è stato ancora provato con un vero microfono; il pannello touch destinato a ospitare l'assistente non ha girato su una scheda.",
  "bullets": [
   "**Un elenco chiuso di quindici comandi:** `status`, `silence`, `arm`, `disarm`, e quelli che chiedono - `alarms`, `nodes`, `cameras`, `radar`, `solar`, `electrical`, `network`, `time`, `help` - più accendere e spegnere le luci, in **otto lingue** (inglese, spagnolo, tedesco, francese, italiano, giapponese, cinese e portoghese), dopo aver normalizzato accenti, punteggiatura e formule di cortesia. Qualsiasi altra cosa, o qualsiasi cosa ambigua, non è compresa.",
   "**Una conferma emessa dal servizio:** `arm` e `disarm` restituiscono un token firmato al primo turno e sono accettati solo quando un turno successivo lo ripete per lo stesso intento entro 30 s, **dallo stesso utente**. Chi chiama non può falsificarla, una scaduta è rifiutata e i nonce di quelle non scadute non sono mai dimenticati per fare spazio.",
   "**Un servizio HTTP locale:** `python -m armor_voice_ai.service` ascolta solo sull'indirizzo di loopback, richiede un token e risponde a `POST /v1/command` con la decisione nella lingua richiesta; il menu Servizi del server mostra quale versione gira.",
   "**Un endpoint di turno:** `POST /v1/turn` riceve una registrazione, esegue il comando di riconoscimento vocale che configuri, passa l'ordine nel motore e risponde con una registrazione fatta dal comando di sintesi vocale; i comandi, l'indirizzo del server e il suo token vengono dall'ambiente.",
   "**Decisioni, non audio:** con `--audit-file` ogni decisione registra l'intento, l'esito e uno SHA-256 della trascrizione, mai audio né le parole grezze.",
   "**Solo raccomandazioni:** un comando accettato è passato ad ARMOR-SERVER, che lo autentica e lo autorizza comunque; dal pannello a muro disinserire a voce non è mai possibile (il PIN si digita sullo schermo); dall'app segue `ARMOR_DISARM_PIN` del server (impostalo su `required`)."
  ],
  "note": "Vedi la [sicurezza della voce](docs/SAFETY.md) e il [servizio](docs/SERVICE.md).",
  "fit": "ARMOR-VOICE-AI trasforma ciò che si dice in uno di un elenco chiuso di comandi e non fa mai nulla da solo: [ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER) lo interroga, poi autentica e autorizza il comando esattamente come un clic in [ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO). È pensato per vivere dietro il microfono del pannello a muro [ARMOR-HMI](https://github.com/JuanenRac/ARMOR-HMI) e serve l'assistente scritto e parlato dell'app Android.",
  "hardware": "Gira come servizio sul banco di prova CM5, interrogato dal server; nessun microfono né motore vocale è stato provato",
  "requirements": [
   "Python 3.11+ (solo la libreria standard)",
   "facoltativo: un comando da voce a testo e uno da testo a voce per `/v1/turn`"
  ]
 },
 "de": {
  "tagline": "Offline-Sprachbefehle in acht Sprachen, mit einer Bestätigung, die der Aufrufer nicht fälschen kann",
  "honest": "Die Absichtsregeln, die acht Sprachen, die signierte Bestätigung, die an ihren Sprecher gebunden ist, der lokale Dienst, der Turn-Endpunkt und das Audit sind real und getestet (83 Tests), und der Server fragt den Dienst am CM5-Testaufbau ab. **Keine Spracherkennungs- oder Synthese-Engine ist Teil dieses Repositorys**: `/v1/turn` führt die Befehle aus, die Sie dafür einstellen, und keiner wurde bisher mit einem echten Mikrofon erprobt; das Touchpanel, das den Assistenten tragen soll, lief noch nicht auf einer Platine.",
  "bullets": [
   "**Eine geschlossene Liste von fünfzehn Befehlen:** `status`, `silence`, `arm`, `disarm` und die fragenden - `alarms`, `nodes`, `cameras`, `radar`, `solar`, `electrical`, `network`, `time`, `help` - sowie Licht an und aus, in **acht Sprachen** (Englisch, Spanisch, Deutsch, Französisch, Italienisch, Japanisch, Chinesisch und Portugiesisch), nach Normalisierung von Akzenten, Zeichensetzung und Höflichkeitsfloskeln. Alles andere oder Mehrdeutige wird nicht verstanden.",
   "**Eine vom Dienst ausgestellte Bestätigung:** `arm` und `disarm` liefern im ersten Zug ein signiertes Token und werden nur akzeptiert, wenn ein späterer Zug es für dieselbe Absicht innerhalb von 30 s zurückgibt, **vom selben Benutzer**. Der Aufrufer kann sie nicht fälschen, eine abgelaufene wird abgelehnt und die Nonces der nicht abgelaufenen werden nie vergessen, um Platz zu schaffen.",
   "**Ein lokaler HTTP-Dienst:** `python -m armor_voice_ai.service` lauscht nur auf der Loopback-Adresse, verlangt ein Token und beantwortet `POST /v1/command` mit der Entscheidung in der gewünschten Sprache; das Menü Dienste des Servers zeigt, welche Version läuft.",
   "**Ein Turn-Endpunkt:** `POST /v1/turn` nimmt eine Aufnahme entgegen, führt den von Ihnen eingestellten Sprache-zu-Text-Befehl aus, schickt den Auftrag durch die Engine und antwortet mit einer vom Text-zu-Sprache-Befehl erzeugten Aufnahme; die Befehle, die Serveradresse und ihr Token stammen aus der Umgebung.",
   "**Entscheidungen, kein Audio:** mit `--audit-file` hält jede Entscheidung die Absicht, das Ergebnis und einen SHA-256 des Transkripts fest, nie Audio oder die rohen Worte.",
   "**Nur Empfehlungen:** ein akzeptierter Befehl wird an ARMOR-SERVER weitergegeben, der ihn weiterhin authentifiziert und autorisiert; vom Wandpanel aus ist Unscharfschalten per Sprache nie möglich (die PIN wird auf dem Bildschirm eingegeben); in der App folgt es `ARMOR_DISARM_PIN` des Servers (auf `required` setzen)."
  ],
  "note": "Siehe die [Sprachsicherheit](docs/SAFETY.md) und den [Dienst](docs/SERVICE.md).",
  "fit": "ARMOR-VOICE-AI macht aus dem Gesagten einen Befehl aus einer geschlossenen Liste und tut nie etwas von selbst: [ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER) fragt es ab und authentifiziert und autorisiert den Befehl dann genau wie einen Klick in [ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO). Es soll hinter dem Mikrofon des Wandpanels [ARMOR-HMI](https://github.com/JuanenRac/ARMOR-HMI) leben und bedient den geschriebenen und gesprochenen Assistenten der Android-App.",
  "hardware": "Läuft als Dienst am CM5-Testaufbau, vom Server abgefragt; weder Mikrofon noch Sprach-Engine wurden erprobt",
  "requirements": [
   "Python 3.11+ (nur die Standardbibliothek)",
   "optional: je ein Sprache-zu-Text- und Text-zu-Sprache-Befehl für `/v1/turn`"
  ]
 },
 "zh": {
  "tagline": "八种语言的离线语音意图，带有调用方无法伪造的确认",
  "honest": "意图规则、八种语言、绑定到说话人的签名确认、本地服务、轮次端点和审计都是真实的并经过测试（83 个测试），服务器在 CM5 测试台上向该服务发起请求。**本仓库不包含任何语音识别或合成引擎**：`/v1/turn` 运行你为它们配置的命令，目前都还没有用真实麦克风试过；打算承载助手的触摸面板还没有在板上运行过。",
  "bullets": [
   "**十五个命令组成的封闭白名单：**`status`、`silence`、`arm`、`disarm`，以及用于询问的 `alarms`、`nodes`、`cameras`、`radar`、`solar`、`electrical`、`network`、`time`、`help`，还有开关灯，支持**八种语言**（英语、西班牙语、德语、法语、意大利语、日语、中文和葡萄牙语），先规范化重音、标点和客套话。其他任何内容或有歧义的内容都不会被理解。",
   "**由服务签发的确认：**`arm` 和 `disarm` 在第一轮返回签名令牌，只有在 30 秒内的后续一轮为**同一用户**的同一意图回传它时才被接受。调用方无法伪造，过期的会被拒绝，未过期令牌的随机数也绝不会为腾出空间而被忘记。",
   "**本地 HTTP 服务：**`python -m armor_voice_ai.service` 只监听回环地址，需要令牌，对 `POST /v1/command` 以所要求的语言返回决定；服务器的“服务”菜单会显示运行的是哪个版本。",
   "**轮次端点：**`POST /v1/turn` 接收一段录音，运行你配置的语音转文字命令，把指令交给引擎，并用文字转语音命令生成的录音作答；命令、服务器地址及其令牌来自环境变量。",
   "**只记录决定，不记录音频：**使用 `--audit-file` 时，每个决定记录意图、结果和转写文本的 SHA-256，绝不记录音频或原话。",
   "**只是建议：**被接受的命令会交给 ARMOR-SERVER，由它继续认证和授权；在墙面面板上绝不可能用语音撤防（PIN 在屏幕上输入）；在应用中则遵循服务器的 `ARMOR_DISARM_PIN`（请设为 `required`）。"
  ],
  "note": "参见[语音安全](docs/SAFETY.md)和[服务](docs/SERVICE.md)。",
  "fit": "ARMOR-VOICE-AI 把所说的话变成封闭列表中的某个命令，自己从不做任何事：[ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER) 向它询问，然后像对待 [ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) 中的一次点击那样认证并授权该命令。它打算放在壁挂面板 [ARMOR-HMI](https://github.com/JuanenRac/ARMOR-HMI) 的麦克风之后，并为 Android 应用的文字和语音助手服务。",
  "hardware": "在 CM5 测试台上作为服务运行，由服务器调用；尚未试过麦克风或语音引擎",
  "requirements": [
   "Python 3.11+（仅标准库）",
   "可选：用于 `/v1/turn` 的语音转文字和文字转语音命令"
  ]
 },
 "ja": {
  "tagline": "8 言語のオフライン音声インテント。呼び出し側が偽造できない確認付き",
  "honest": "インテントのルール、8 言語、話者に結び付いた署名付き確認、ローカルサービス、ターンエンドポイント、監査は実在し、テストされています（83 件）。サーバーは CM5 テストベンチでこのサービスに問い合わせています。**音声認識・合成エンジンはこのリポジトリに含まれません**：`/v1/turn` は設定されたコマンドを実行するだけで、実際のマイクではまだ試されていません。アシスタントを載せる予定のタッチパネルは基板上で動いたことがありません。",
  "bullets": [
   "**15 個のコマンドからなる閉じた許可リスト：**`status`、`silence`、`arm`、`disarm`、尋ねる系の `alarms`、`nodes`、`cameras`、`radar`、`solar`、`electrical`、`network`、`time`、`help`、さらに照明のオン・オフを、アクセント・句読点・丁寧語の除去後に **8 言語**（英語、スペイン語、ドイツ語、フランス語、イタリア語、日本語、中国語、ポルトガル語）で。それ以外や曖昧なものは理解されません。",
   "**サービスが発行する確認：**`arm` と `disarm` は最初のターンで署名付きトークンを返し、30 秒以内の後続ターンで**同じユーザー**が同じインテントについてそれを返したときだけ受け付けます。呼び出し側は偽造できず、期限切れは拒否され、期限内のトークンのノンスは場所を空けるために忘れられることはありません。",
   "**ローカル HTTP サービス：**`python -m armor_voice_ai.service` はループバックアドレスのみで待ち受け、トークンを要求し、`POST /v1/command` に求められた言語で判断を返します。サーバーのサービスメニューで動作中のバージョンが分かります。",
   "**ターンエンドポイント：**`POST /v1/turn` は録音を受け取り、設定した音声認識コマンドを実行し、指示をエンジンに通し、音声合成コマンドで作った録音で答えます。コマンド、サーバーアドレス、そのトークンは環境変数から読みます。",
   "**音声ではなく判断を記録：**`--audit-file` を使うと、各判断はインテント、結果、文字起こしの SHA-256 を記録し、音声や生の言葉は決して記録しません。",
   "**推奨のみ：**受け付けたコマンドは ARMOR-SERVER に渡され、サーバーが引き続き認証と認可を行います。壁パネルでは音声での解除は決してできません（PIN は画面で入力します）。アプリではサーバーの `ARMOR_DISARM_PIN` に従います（`required` に設定してください）。"
  ],
  "note": "[音声の安全性](docs/SAFETY.md)と[サービス](docs/SERVICE.md)を参照してください。",
  "fit": "ARMOR-VOICE-AI は、話された内容を閉じたリストのコマンドのひとつに変えるだけで、自分では何もしません。[ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER) が問い合わせ、[ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) でのクリックと同じようにコマンドを認証・認可します。壁掛けパネル [ARMOR-HMI](https://github.com/JuanenRac/ARMOR-HMI) のマイクの背後で動く想定で、Android アプリの文字・音声アシスタントにも応えます。",
  "hardware": "CM5 テストベンチでサービスとして動作し、サーバーが問い合わせます。マイクや音声エンジンは未検証",
  "requirements": [
   "Python 3.11+（標準ライブラリのみ）",
   "任意：`/v1/turn` 用の音声認識コマンドと音声合成コマンド"
  ]
 },
 "pt": {
  "tagline": "Intenções de voz offline em oito idiomas, com uma confirmação que quem chama não pode forjar",
  "honest": "As regras de intenção, os oito idiomas, a confirmação assinada ligada a quem fala, o serviço local, o ponto de turno e a auditoria são reais e estão testados (83 testes), e o servidor pergunta ao serviço na bancada de testes do CM5. **Nenhum motor de reconhecimento ou síntese de voz faz parte deste repositório**: `/v1/turn` executa os comandos que configurar para eles, e nenhum foi ainda experimentado com um microfone real; o painel tátil destinado a levar o assistente não correu numa placa.",
  "bullets": [
   "**Uma lista fechada de quinze comandos:** `status`, `silence`, `arm`, `disarm`, e os que perguntam - `alarms`, `nodes`, `cameras`, `radar`, `solar`, `electrical`, `network`, `time`, `help` - mais ligar e desligar as luzes, em **oito idiomas** (inglês, espanhol, alemão, francês, italiano, japonês, chinês e português), depois de normalizar acentos, pontuação e fórmulas de cortesia. Qualquer outra coisa, ou qualquer coisa ambígua, não é entendida.",
   "**Uma confirmação emitida pelo serviço:** `arm` e `disarm` devolvem um token assinado no primeiro turno e só são aceites quando um turno posterior o repete para a mesma intenção em 30 s, **do mesmo utilizador**. Quem chama não a pode forjar, uma caducada é recusada e os nonces das não caducadas nunca são esquecidos para arranjar espaço.",
   "**Um serviço HTTP local:** `python -m armor_voice_ai.service` escuta só no endereço de loopback, exige um token e responde a `POST /v1/command` com a decisão no idioma pedido; o menu Serviços do servidor mostra que versão corre.",
   "**Um ponto de turno:** `POST /v1/turn` recebe uma gravação, executa o comando de voz para texto que configurar, passa a ordem pelo motor e responde com uma gravação feita pelo comando de texto para voz; os comandos, o endereço do servidor e o seu token vêm do ambiente.",
   "**Decisões, não áudio:** com `--audit-file` cada decisão regista a intenção, o resultado e um SHA-256 da transcrição, nunca áudio nem as palavras em bruto.",
   "**Só recomendações:** um comando aceite é passado ao ARMOR-SERVER, que continua a autenticá-lo e autorizá-lo; a partir do painel de parede desarmar por voz nunca é possível (o PIN digita-se no ecrã); a partir da app segue o `ARMOR_DISARM_PIN` do servidor (ponha-o em `required`)."
  ],
  "note": "Veja a [segurança da voz](docs/SAFETY.md) e o [serviço](docs/SERVICE.md).",
  "fit": "O ARMOR-VOICE-AI transforma o que é dito num de uma lista fechada de comandos e nunca faz nada por si: o [ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER) pergunta-lhe e depois autentica e autoriza o comando exatamente como um clique no [ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO). Destina-se a viver atrás do microfone do painel de parede [ARMOR-HMI](https://github.com/JuanenRac/ARMOR-HMI) e serve o assistente escrito e falado da aplicação Android.",
  "hardware": "A correr como serviço na bancada de testes do CM5, consultado pelo servidor; nenhum microfone ou motor de voz foi experimentado",
  "requirements": [
   "Python 3.11+ (apenas a biblioteca padrão)",
   "opcional: um comando de voz para texto e outro de texto para voz para `/v1/turn`"
  ]
 }
}
