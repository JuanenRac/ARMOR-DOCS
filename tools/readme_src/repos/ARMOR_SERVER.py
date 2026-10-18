# The facts that do not depend on the language, and the words of every language, of ARMOR-SERVER.
# Copyright (C) 2026 JuanenRac (Electro Hobby 3D). GPL-3.0-or-later.

FACTS = {
 "emoji": "🛡️",
 "badges": [
  [
   "Language",
   "TypeScript",
   "3178c6"
  ],
  [
   "Runtime",
   "Node%2022%2B",
   "43853d"
  ],
  [
   "Tests",
   "510%20passing",
   "2ea44f"
  ],
  [
   "Maturity",
   "established",
   "00E5FF"
  ]
 ],
 "diagram": "```mermaid\nflowchart LR\n    N[\"Field nodes (ESP32-S3)\"] -->|MQTT / HTTP + ingest token| S[\"ARMOR-SERVER\"]\n    G[\"Solar gateway nodes\"] -->|MQTT / HTTP + ingest token| S\n    E[\"Electrical nodes\"] -->|MQTT / HTTP + ingest token| S\n    C[\"IP cameras\"] -->|RTSP / ONVIF| S\n    S -->|\"MJPEG, JSON, WebSocket\"| U[\"ARMOR-STUDIO\"]\n    S -->|\"MJPEG, JSON\"| A[\"ARMOR-ANDROID-CONTROL\"]\n    S --> D[(\"data/: cameras.json (AES-GCM), media/, audit.log\")]\n```",
 "build": "```powershell\nnpm install\nnpm run typecheck   # tsc --noEmit\nnpm test            # 510 tests: unit + full HTTP integration (every route must be in the OpenAPI file)\nnpm run build       # dist/server.mjs\n.\\run.bat           # development server with hot reload\n```",
 "structure": "```text\nARMOR-SERVER/\n├── src/            server, app, config, context, store, persistence, events, contracts, rules, mqtt, mqtt_tls, audit, notify, channels,\n│   │               alarms, alarm, alarm_design, alarm_commands, alarm_zone_feed, escalation, preflight, automations, users,\n│   │               site, solar, solar_registry, electrical, electrical_energy, electrical_switching, network, network_commands,\n│   │               firmware, installation, admin, voice, voice_actions, ai, capture_on_detect, ignore_zones, push_fcm, ...\n│   ├── http/       auth, per-node tokens, sealed credentials\n│   ├── routes/     sessions, users, cameras, media, ingest, history, devices, alarms, alarm, alarm_design, solar, electrical,\n│   │               network, firmware, maintenance, admin, notifications, voice, ai, push, preferences, system\n│   ├── devices/    catalog, registry, commands, mapping (the device model and its MQTT bridge)\n│   ├── cameras/    model, vault, digest, ptz, rtsp, discovery, health, errors\n│   └── media/      relay, evidence\n├── tests/          510 tests: unit + full HTTP integration\n├── docs/           state machine, camera gateway, integration, node firmware\n├── tools/          project tooling and the CI checks\n├── data/           runtime state (ignored by Git)\n└── images/         brand assets\n```",
 "tests": "510 (`npm test`)",
 "requirements": [
  "Node.js 22+",
  "FFmpeg (live video and capture)",
  "an MQTT broker (Mosquitto)"
 ]
}

TEXT = {
 "en": {
  "tagline": "Central security coordinator: nodes, alarms, devices, energy, cameras, the local network and the upkeep of the installation",
  "honest": "Every route, session, encryption and evidence rule below is real and covered by tests (`npm test`: 510 tests, including a full HTTP integration suite against an isolated server and a check that every route is documented in the OpenAPI file). It runs in daily use on the CM5 test bench with a real MQTT broker, the firmware of a real radar node on an ESP32-S3 board, real IP cameras (live video, snapshots, recordings, PTZ on the Hi3510 units), the Studio console, the Android app and the voice and observation services. What is **not** proven yet: ONVIF against a real ONVIF camera, any Jetson hardware, the solar, electrical, alarm-panel and touch-panel routes against real nodes (they are tested with generated messages: only the radar board exists) and push through Firebase against a real Firebase project.",
  "bullets": [
   "**Validated ingest:** HTTP and MQTT messages of every kind of node (radar, solar, electrical, alarm panel, network) are checked at the boundary by the shared contract before they reach the state; a node may have its own token (derived from the shared one) and a strict mode accepts nothing else.",
   "**Honest node state:** a node that stops talking is shown as *stale* and *offline* after a configurable window, never as online on old data; one that reconnects is counted from its return, not from its old messages. Disarming clears a high alert at once.",
   "**Camera gateway:** encrypted camera vault, ONVIF / Hi3510 / PSIA PTZ, RTSP path discovery, one shared FFmpeg relay per camera, snapshots and MP4 recording, a watchdog that turns a silent camera into an event and, while armed, an alarm, **zones of the picture to ignore** and **photos and video taken by themselves** when a camera sees something while armed.",
   "**Evidence library:** oldest-first retention by age and size, **protected evidence** that is never pruned, a SHA-256 for chain of custody and a **proof of custody** file signed by the server. One audit line per security-relevant action, with credentials scrubbed.",
   "**State that survives:** the security mode and every node's last observation are restored after a restart (a restart never silently disarms the perimeter); files are written atomically and a damaged one is recovered. Every alert, node and mode change is kept in an event history.",
   "**Alarms:** one alarm centre with a raised / acknowledged / cleared lifecycle, escalation of a critical alarm that waits unseen, a **check before arming** (what is open, silent or down), a PIN to disarm (and a duress PIN) and alarms from nodes, cameras, devices, solar, electrical, network and alarm panels. They reach Studio, the phones (ntfy, Telegram, Home Assistant, a signed webhook, Firebase push when you configure it) and the MQTT topic `armor/server/alert`.",
   "**Users and roles:** names and passwords (scrypt hashes), an `admin` role that manages users, an `operator` role that operates and a `viewer` role that only looks; a changed password or role ends that user's other sessions.",
   "**Devices and automations:** smoke, gas, flood, door, window, motion, climate, plug, light, siren, lock, shutter, gate and garage-door, and water-heater devices over MQTT or an authenticated push, with normalised state, availability and commands; rules that switch devices when anything happens (including threshold triggers).",
   "**Energy:** inverters and battery stacks (with each cell and the capacities) and electrical nodes arrive by HTTP or MQTT, are validated by the shared contract, kept with a history and a per-day energy, marked stale when silent, and raise alarms (inverter fault, battery low, grid lost, voltage, switch fault…). The electrical design and the rules for switching a circuit are kept on the server.",
   "**Alarm panels:** the state of the ARMOR-ALARM nodes, the **design of the alarm** kept with its versions, the **Zigbee devices tied to the zones** (the server tells a panel how a zone is while it holds the radio) and arm / disarm commands to a panel (off unless `ARMOR_ALARM_COMMANDS=1`).",
   "**Local network:** what the ARMOR-NETWORK node reports (devices, internet, the public address and who gives it), orders for the node (sweep, ping, ports, inspect a device with a login you give), names, hidden and watched devices, and logins that travel **sealed for the node alone**.",
   "**Voice, observation and the nodes' upkeep:** written and spoken commands (a closed list, in eight languages, with a confirmation bound to the person), the context for the observation service (which radars cover which camera), the firmware of the nodes updated from Studio one by one with progress, and the installation's own updates from GitHub, the system's updates and an optional root console, all through the maintenance helper.",
   "**Using it from outside the house:** the server tells the house from the outside (a VPN counts as the house), keeps shorter sessions from outside, asks for a second factor (an authenticator app, with recovery codes) and for the password again before critical actions, lets you choose what a session from outside may do (everything, operate the alarm only, only look), tells the places the alarms go to when someone signs in from a new place, and opens the web panel of a node through the server - pinned to the certificate of the node, with its cookie kept on the server - so that no node is ever published.",
   "**Optional encrypted link to the broker (mqtts):** `ARMOR_MQTT_CA_FILE` names the certificate of the installation's own authority; with an `mqtts://` address the server trusts that authority only and checks the broker's name, and it refuses to start if the file is not one valid certificate or the address is not `mqtts://`. Studio shows whether the link is encrypted and the authority's fingerprint. Tested against a TLS broker stand-in and against a real Mosquitto 2.0.",
   "**Node health and arming modes:** keeps the latest report and the restart log of every node and raises four warnings (low memory, restarting too often, a broker that keeps dropping, a weak Wi-Fi signal); keeps the arming profiles (Away, Home, Night and your own) and puts the chosen one inside the arm command, only for a node that says it understands them. A loud or a quiet alarm follows the profile; an arm without one is the command it always was.",
   "**History of connections and of the system:** besides the alerts, nodes, cameras, devices and alarms, the history records which devices and apps connect (Studio sessions, the Android app, the panels of the nodes, the voice service: sign-ins, refusals, sign-outs, expired sessions, use of the second factor, first and last seen) and the events of the system (nodes that appear or disappear with their firmware, the broker link, settings changed and by whom, services, updates, arming with its profile). It can be filtered by kind, category, client and user; the address and the user agent are shown to administrators only, and no password, token, cookie or PIN is ever recorded."
  ],
  "intro": "**ARMOR-SERVER** is the trusted centre of A.R.M.O.R. Field nodes publish radar, light and health observations; this service validates them, keeps the last known state of every node, and serves that state to the Studio console and the Android client. It also owns everything that touches a camera, so that **no browser and no phone ever holds a camera password or an RTSP address**.",
  "sections": [
   {
    "icon": "🔒",
    "title": "Security model",
    "bullets": [
     "Separate secrets: **ingest** (the nodes post their messages; each node may also have its own token, derived from the shared one, and a strict mode accepts only those), **control** (arm / disarm, events), **operator** (automation) and the **Studio login**; each is compared in constant time and none stands in for another. A login given to a network node travels sealed for that node alone.",
     "Three roles: **admin**, **operator** and **viewer** (reads, never changes). Every route that configures, moves, captures, records, protects, deletes or arms needs an operator; live video needs an operator or a short-lived stream ticket tied to one camera. Dangerous commands (disarming, switching a circuit, the root console) ask for an administrator and, for disarming, the PIN.",
     "Camera passwords live only in `data/cameras.json`, AES-256-GCM encrypted, and no API returns them; ONVIF addresses must stay on the camera's host and redirects are refused.",
     "Studio sessions are HttpOnly and SameSite=Strict, login is rate limited and errors never carry a stack trace.",
     "The server listens on 127.0.0.1 unless `ARMOR_HOST` is set on purpose, and then a Studio password shorter than 12 characters is refused.",
     "From outside the house: the second factor (TOTP, RFC 6238), a new proof of identity for users, firmware and the node panels, a policy that keeps administering in the house or on the VPN, only signed firmware releases, and a proxy for node panels that never takes an address from the request, only passes what is needed and refuses a node whose certificate is not the trusted one."
    ]
   },
   {
    "icon": "🌐",
    "title": "API",
    "bullets": [
     "Public: `GET /healthz`. For a signed-in user: status, information, cameras, media, history, rules, devices, alarms, automations, the designs (site, alarm, electrical, network), solar and electrical readings, the local network, notifications and preferences, and for an administrator users, services, firmware, updates and the console.",
     "For the nodes: `POST /api/v1/telemetry`, `/health`, `/solar`, `/electrical/readings`, `/alarm/state`, `/network/state` and `/devices/state` with the ingest token, and the MQTT topics `armor/node/#`, `armor/solar/#`, `armor/electrical/#`, `armor/alarm/#` and `armor/network/#`. Events reach the consoles by the WebSocket `/api/v1/events`.",
     "Every route (135 paths today), its access rule and its schema is in the OpenAPI file of [ARMOR-COMMON](https://github.com/JuanenRac/ARMOR-COMMON), and a test checks that no route is missing from it."
    ]
   },
   {
    "icon": "⚙️",
    "title": "Configuration",
    "bullets": [
     "Copy `.env.example` to `.env` (ignored by Git), or let `run.bat` / `run.sh` generate random secrets on the first run.",
     "Required: `ARMOR_INGEST_TOKEN` and `ARMOR_CONTROL_TOKEN` (24 characters or more, all different) and `ARMOR_STUDIO_USERNAME` / `ARMOR_STUDIO_PASSWORD` (the first administrator).",
     "Common: `ARMOR_HOST` / `ARMOR_PORT`, `ARMOR_DATA_DIR`, `ARMOR_FFMPEG_PATH` (live video and capture), `ARMOR_MQTT_URL`, `ARMOR_MQTT_CA_FILE`, `ARMOR_STUDIO_ORIGIN`, `ARMOR_NODE_STALE_AFTER_S`, `ARMOR_CAMERA_CHECK_S`, `ARMOR_ALERT_DWELL_MS`, `ARMOR_ALERT_WEBHOOK_URL` and `ARMOR_COOKIE_SECURE` (set it to `1` behind TLS).",
     "Optional, all off by default: `ARMOR_NTFY_URL`, `ARMOR_TELEGRAM_BOT_TOKEN`, `ARMOR_HOMEASSISTANT_URL`, `ARMOR_FCM_SERVICE_ACCOUNT` (push through the installation's own Firebase project), `ARMOR_ALARM_COMMANDS=1` (let the server arm and disarm alarm panels), `ARMOR_ELECTRICAL_SWITCHING` and `ARMOR_INGEST_STRICT=1`."
    ]
   }
  ],
  "note": "To install on the CM5 test bench (isolated from every other project, own user, own ports) see [ARMOR-DEVOPS](https://github.com/JuanenRac/ARMOR-DEVOPS).",
  "fit": "ARMOR-SERVER is the one trusted centre of the family. The field nodes ([ARMOR-RADAR](https://github.com/JuanenRac/ARMOR-RADAR), [ARMOR-SOLAR](https://github.com/JuanenRac/ARMOR-SOLAR), [ARMOR-ELECTRICAL](https://github.com/JuanenRac/ARMOR-ELECTRICAL), [ARMOR-ALARM](https://github.com/JuanenRac/ARMOR-ALARM), [ARMOR-HMI](https://github.com/JuanenRac/ARMOR-HMI)) and [ARMOR-NETWORK](https://github.com/JuanenRac/ARMOR-NETWORK) speak to it over MQTT or HTTP; [ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) and [ARMOR-ANDROID-CONTROL](https://github.com/JuanenRac/ARMOR-ANDROID-CONTROL) read it and give it orders; [ARMOR-SERVER-AI](https://github.com/JuanenRac/ARMOR-SERVER-AI) weighs what the cameras see against the radars and only recommends; [ARMOR-VOICE-AI](https://github.com/JuanenRac/ARMOR-VOICE-AI) turns speech into a closed list of commands; [ARMOR-DEVOPS](https://github.com/JuanenRac/ARMOR-DEVOPS) installs and updates all of it on the CM5. The server decides: nothing else arms, disarms or switches anything.",
  "hardware": "The CM5 test bench, in daily use: a real MQTT broker, real IP cameras, a real radar node on an ESP32-S3 board, Studio, the Android app and the voice and observation services against it"
 },
 "es": {
  "tagline": "Coordinador central de seguridad: nodos, alarmas, dispositivos, energía, cámaras, la red local y el mantenimiento de la instalación",
  "honest": "Cada ruta, sesión, cifrado y regla de evidencias de abajo es real y está cubierta por tests (`npm test`: 510 tests, con una suite completa de integración HTTP contra un servidor aislado y una comprobación de que cada ruta está documentada en el fichero OpenAPI). Funciona en uso diario en el banco de pruebas de la CM5 con un broker MQTT real, el firmware de un nodo radar real en una placa ESP32-S3, cámaras IP reales (vídeo en directo, capturas, grabaciones, PTZ en las unidades Hi3510), la consola Studio, la app Android y los servicios de voz y de observación. Lo que **todavía no** está probado: ONVIF con una cámara ONVIF real, cualquier hardware Jetson, las rutas solares, eléctricas, de centrales de alarma y de panel táctil con nodos reales (se prueban con mensajes generados: solo existe la placa radar) y el push por Firebase con un proyecto Firebase real.",
  "bullets": [
   "**Entrada validada:** los mensajes HTTP y MQTT de cada tipo de nodo (radar, solar, eléctrico, central de alarma, red) se comprueban en la frontera con el contrato compartido antes de llegar al estado; un nodo puede tener su propio token (derivado del compartido) y un modo estricto no acepta otra cosa.",
   "**Estado honesto de los nodos:** un nodo que deja de hablar se muestra como *obsoleto* y *desconectado* tras una ventana configurable, nunca como en línea con datos viejos; uno que se reconecta cuenta desde su regreso, no desde sus mensajes antiguos. Desarmar borra una alerta alta al instante.",
   "**Pasarela de cámaras:** bóveda cifrada de cámaras, PTZ ONVIF / Hi3510 / PSIA, descubrimiento de rutas RTSP, un relé FFmpeg compartido por cámara, capturas y grabación MP4, un vigilante que convierte una cámara muda en un evento y, armado, en una alarma, **zonas de la imagen que se ignoran** y **fotos y vídeo hechos solos** cuando una cámara ve algo estando armado.",
   "**Biblioteca de evidencias:** retención por antigüedad y tamaño, **evidencias protegidas** que nunca se borran, un SHA-256 para la cadena de custodia y un fichero de **prueba de custodia** firmado por el servidor. Una línea de auditoría por acción relevante, con las credenciales borradas.",
   "**Estado que sobrevive:** el modo de seguridad y la última observación de cada nodo se restauran tras un reinicio (un reinicio nunca desarma el perímetro en silencio); los ficheros se escriben de forma atómica y uno dañado se recupera. Cada cambio de alerta, nodo y modo se guarda en un historial de eventos.",
   "**Alarmas:** un centro de alarmas con ciclo generada / reconocida / cerrada, escalado de una alarma crítica que espera sin verse, una **comprobación antes de armar** (qué está abierto, mudo o caído), un PIN para desarmar (y un PIN de coacción) y alarmas de nodos, cámaras, dispositivos, solar, eléctrico, red y centrales de alarma. Llegan a Studio, a los móviles (ntfy, Telegram, Home Assistant, un webhook firmado, push por Firebase si lo configuras) y al tema MQTT `armor/server/alert`.",
   "**Usuarios y roles:** nombres y contraseñas (hashes scrypt), un rol `admin` que gestiona usuarios, un rol `operator` que opera y un rol `viewer` que solo mira; cambiar la contraseña o el rol cierra las demás sesiones de ese usuario.",
   "**Dispositivos y automatizaciones:** humo, gas, inundación, puerta, ventana, movimiento, clima, enchufe, luz, sirena, cerradura, persiana, puerta de garaje o cancela y calentador de agua, por MQTT o push autenticado, con estado normalizado, disponibilidad y comandos; reglas que accionan dispositivos cuando algo ocurre (también por umbrales).",
   "**Energía:** inversores y pilas de baterías (con cada celda y las capacidades) y nodos eléctricos llegan por HTTP o MQTT, se validan con el contrato compartido, se guardan con historial y energía por día, se marcan obsoletos si callan y generan alarmas (avería de inversor, batería baja, red perdida, tensión, fallo de conmutación…). El diseño eléctrico y las reglas para conmutar un circuito se guardan en el servidor.",
   "**Centrales de alarma:** el estado de los nodos ARMOR-ALARM, el **diseño de la alarma** con sus versiones, los **dispositivos Zigbee atados a las zonas** (el servidor le dice a una central cómo está una zona mientras él tiene la radio) y comandos de armar / desarmar a una central (apagado salvo `ARMOR_ALARM_COMMANDS=1`).",
   "**Red local:** lo que informa el nodo ARMOR-NETWORK (dispositivos, internet, la dirección pública y quién la da), órdenes para el nodo (barrido, ping, puertos, inspeccionar un dispositivo con un acceso que tú das), nombres, dispositivos ocultos y vigilados, y accesos que viajan **sellados solo para el nodo**.",
   "**Voz, observación y mantenimiento:** comandos escritos y hablados (lista cerrada, en ocho idiomas, con una confirmación ligada a la persona), el contexto para el servicio de observación (qué radares cubren qué cámara), el firmware de los nodos actualizado desde Studio de uno en uno con progreso, y las actualizaciones de la propia instalación desde GitHub, las del sistema y una consola root opcional, todo por el ayudante de mantenimiento.",
   "**Uso desde fuera de casa:** el servidor distingue la casa del exterior (una VPN cuenta como la casa), mantiene sesiones más cortas desde fuera, pide un segundo factor (una app autenticadora, con códigos de recuperación) y la contraseña otra vez antes de las acciones críticas, deja elegir qué puede hacer una sesión de fuera (todo, solo operar la alarma, solo mirar), avisa a los sitios de las alarmas cuando alguien entra desde un lugar nuevo y abre el panel web de un nodo a través del servidor -fijado al certificado del nodo y con su cookie guardada en el servidor- para que ningún nodo se publique nunca.",
   "**Enlace cifrado opcional con el broker (mqtts):** `ARMOR_MQTT_CA_FILE` indica el certificado de la autoridad propia de la instalación; con una dirección `mqtts://` el servidor confía solo en esa autoridad y comprueba el nombre del broker, y se niega a arrancar si el fichero no es un certificado válido o la dirección no es `mqtts://`. Studio muestra si el enlace está cifrado y la huella de la autoridad. Probado contra un broker TLS de pruebas y contra un Mosquitto 2.0 real.",
   "**Salud de los nodos y modos de armado:** guarda el último informe y el registro de reinicios de cada nodo y levanta cuatro avisos (poca memoria, reinicios demasiado frecuentes, un broker que se corta una y otra vez, señal Wi-Fi débil); guarda los perfiles de armado (Fuera, En casa, Noche y los tuyos) y pone el elegido dentro del comando de armar, solo para un nodo que dice entenderlos. Una alarma fuerte o discreta sigue el perfil; un armado sin perfil es el comando de siempre.",
   "**Historial de conexiones y del sistema:** además de las alertas, nodos, cámaras, dispositivos y alarmas, el historial registra qué dispositivos y apps se conectan (sesiones de Studio, la app Android, los paneles de los nodos, el servicio de voz: inicios de sesión, rechazos, cierres, sesiones caducadas, uso del segundo factor, primera y última vez vistos) y los eventos del sistema (nodos que aparecen o desaparecen con su firmware, el enlace con el broker, ajustes cambiados y por quién, servicios, actualizaciones, armado con su perfil). Se filtra por tipo, categoría, cliente y usuario; la dirección y el agente de usuario solo los ven los administradores, y nunca se registra una contraseña, un token, una cookie ni un PIN."
  ],
  "intro": "**ARMOR-SERVER** es el centro de confianza de A.R.M.O.R. Los nodos de campo publican observaciones de radar, luz y salud; este servicio las valida, guarda el último estado conocido de cada nodo y lo sirve a la consola Studio y al cliente Android. También es dueño de todo lo que toca una cámara, de modo que **ningún navegador ni teléfono guarda jamás una contraseña de cámara ni una dirección RTSP**.",
  "sections": [
   {
    "icon": "🔒",
    "title": "Modelo de seguridad",
    "bullets": [
     "Secretos separados: **ingest** (los nodos publican sus mensajes; cada nodo puede tener además su propio token, derivado del compartido, y un modo estricto acepta solo esos), **control** (armar / desarmar, eventos), **operator** (automatización) y el **login de Studio**; cada uno se compara en tiempo constante y ninguno sustituye a otro. Un acceso dado a un nodo de red viaja sellado solo para ese nodo.",
     "Tres roles: **admin**, **operator** y **viewer** (lee, nunca cambia). Cada ruta que configura, mueve, captura, graba, protege, borra o arma necesita un operador; el vídeo en directo necesita un operador o un ticket de emisión de corta vida ligado a una cámara. Los comandos peligrosos (desarmar, conmutar un circuito, la consola root) piden un administrador y, para desarmar, el PIN.",
     "Las contraseñas de las cámaras viven solo en `data/cameras.json`, cifradas con AES-256-GCM, y ninguna API las devuelve; las direcciones ONVIF deben quedarse en el host de la cámara y las redirecciones se rechazan.",
     "Las sesiones de Studio son HttpOnly y SameSite=Strict, el login tiene límite de intentos y los errores nunca llevan traza de pila.",
     "El servidor escucha en 127.0.0.1 salvo que `ARMOR_HOST` se ponga a propósito, y entonces se rechaza una contraseña de Studio de menos de 12 caracteres.",
     "Desde fuera de casa: segundo factor (TOTP, RFC 6238), una prueba de identidad nueva para usuarios, firmware y paneles de nodos, una política que deja administrar solo desde casa o la VPN, solo releases de firmware firmadas y un proxy de paneles de nodos que nunca toma una dirección de la petición, solo pasa lo necesario y rechaza un nodo cuyo certificado no sea el de confianza."
    ]
   },
   {
    "icon": "🌐",
    "title": "API",
    "bullets": [
     "Pública: `GET /healthz`. Para un usuario con sesión: estado, información, cámaras, medios, historial, reglas, dispositivos, alarmas, automatizaciones, los diseños (sitio, alarma, eléctrico, red), lecturas solares y eléctricas, la red local, notificaciones y preferencias, y para un administrador usuarios, servicios, firmware, actualizaciones y la consola.",
     "Para los nodos: `POST /api/v1/telemetry`, `/health`, `/solar`, `/electrical/readings`, `/alarm/state`, `/network/state` y `/devices/state` con el token de ingest, y los temas MQTT `armor/node/#`, `armor/solar/#`, `armor/electrical/#`, `armor/alarm/#` y `armor/network/#`. Los eventos llegan a las consolas por el WebSocket `/api/v1/events`.",
     "Cada ruta (135 rutas hoy), su regla de acceso y su esquema están en el fichero OpenAPI de [ARMOR-COMMON](https://github.com/JuanenRac/ARMOR-COMMON), y un test comprueba que no falta ninguna."
    ]
   },
   {
    "icon": "⚙️",
    "title": "Configuración",
    "bullets": [
     "Copia `.env.example` a `.env` (ignorado por Git), o deja que `run.bat` / `run.sh` generen secretos aleatorios la primera vez.",
     "Obligatorios: `ARMOR_INGEST_TOKEN` y `ARMOR_CONTROL_TOKEN` (24 caracteres o más, todos distintos) y `ARMOR_STUDIO_USERNAME` / `ARMOR_STUDIO_PASSWORD` (el primer administrador).",
     "Habituales: `ARMOR_HOST` / `ARMOR_PORT`, `ARMOR_DATA_DIR`, `ARMOR_FFMPEG_PATH` (vídeo en directo y captura), `ARMOR_MQTT_URL`, `ARMOR_MQTT_CA_FILE`, `ARMOR_STUDIO_ORIGIN`, `ARMOR_NODE_STALE_AFTER_S`, `ARMOR_CAMERA_CHECK_S`, `ARMOR_ALERT_DWELL_MS`, `ARMOR_ALERT_WEBHOOK_URL` y `ARMOR_COOKIE_SECURE` (ponlo a `1` tras TLS).",
     "Opcionales, todos apagados por defecto: `ARMOR_NTFY_URL`, `ARMOR_TELEGRAM_BOT_TOKEN`, `ARMOR_HOMEASSISTANT_URL`, `ARMOR_FCM_SERVICE_ACCOUNT` (push por el proyecto Firebase de la propia instalación), `ARMOR_ALARM_COMMANDS=1` (deja que el servidor arme y desarme las centrales), `ARMOR_ELECTRICAL_SWITCHING` y `ARMOR_INGEST_STRICT=1`."
    ]
   }
  ],
  "note": "Para instalar en el banco de pruebas de la CM5 (aislado de todo otro proyecto, con usuario y puertos propios) véase [ARMOR-DEVOPS](https://github.com/JuanenRac/ARMOR-DEVOPS).",
  "fit": "ARMOR-SERVER es el único centro de confianza de la familia. Los nodos de campo ([ARMOR-RADAR](https://github.com/JuanenRac/ARMOR-RADAR), [ARMOR-SOLAR](https://github.com/JuanenRac/ARMOR-SOLAR), [ARMOR-ELECTRICAL](https://github.com/JuanenRac/ARMOR-ELECTRICAL), [ARMOR-ALARM](https://github.com/JuanenRac/ARMOR-ALARM), [ARMOR-HMI](https://github.com/JuanenRac/ARMOR-HMI)) y [ARMOR-NETWORK](https://github.com/JuanenRac/ARMOR-NETWORK) le hablan por MQTT o HTTP; [ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) y [ARMOR-ANDROID-CONTROL](https://github.com/JuanenRac/ARMOR-ANDROID-CONTROL) lo leen y le dan órdenes; [ARMOR-SERVER-AI](https://github.com/JuanenRac/ARMOR-SERVER-AI) sopesa lo que ven las cámaras frente a los radares y solo recomienda; [ARMOR-VOICE-AI](https://github.com/JuanenRac/ARMOR-VOICE-AI) convierte la voz en una lista cerrada de comandos; [ARMOR-DEVOPS](https://github.com/JuanenRac/ARMOR-DEVOPS) lo instala y actualiza todo en la CM5. El servidor decide: nada más arma, desarma ni acciona nada.",
  "hardware": "El banco de pruebas de la CM5, en uso diario: un broker MQTT real, cámaras IP reales, un nodo radar real en una placa ESP32-S3, Studio, la app Android y los servicios de voz y observación contra él"
 },
 "fr": {
  "tagline": "Coordinateur central de sécurité : nœuds, alarmes, appareils, énergie, caméras, réseau local et entretien de l'installation",
  "honest": "Chaque route, session, chiffrement et règle de preuves ci-dessous est réel et couvert par des tests (`npm test` : 510 tests, dont une suite complète d'intégration HTTP contre un serveur isolé et une vérification que chaque route est documentée dans le fichier OpenAPI). Il fonctionne en usage quotidien sur le banc de test CM5 avec un vrai broker MQTT, le firmware d'un vrai nœud radar sur une carte ESP32-S3, de vraies caméras IP (vidéo en direct, captures, enregistrements, PTZ sur les unités Hi3510), la console Studio, l'application Android et les services de voix et d'observation. Ce qui n'est **pas** encore prouvé : ONVIF avec une vraie caméra ONVIF, tout matériel Jetson, les routes solaires, électriques, de centrales d'alarme et de panneau tactile avec de vrais nœuds (testées avec des messages générés : seule la carte radar existe) et le push via Firebase avec un vrai projet Firebase.",
  "bullets": [
   "**Entrée validée :** les messages HTTP et MQTT de chaque type de nœud (radar, solaire, électrique, centrale d'alarme, réseau) sont vérifiés à la frontière par le contrat partagé avant d'atteindre l'état ; un nœud peut avoir son propre jeton (dérivé du jeton partagé) et un mode strict n'accepte rien d'autre.",
   "**État honnête des nœuds :** un nœud qui se tait est affiché *périmé* et *hors ligne* après une fenêtre configurable, jamais en ligne sur de vieilles données ; un nœud qui se reconnecte est compté depuis son retour, pas depuis ses anciens messages. Désarmer efface une alerte haute aussitôt.",
   "**Passerelle de caméras :** coffre chiffré des caméras, PTZ ONVIF / Hi3510 / PSIA, découverte des chemins RTSP, un relais FFmpeg partagé par caméra, captures et enregistrement MP4, un chien de garde qui transforme une caméra muette en événement et, armé, en alarme, **zones de l'image à ignorer** et **photos et vidéo prises seules** quand une caméra voit quelque chose pendant l'armement.",
   "**Bibliothèque de preuves :** rétention par ancienneté et taille, **preuves protégées** jamais effacées, un SHA-256 pour la chaîne de conservation et un fichier de **preuve de conservation** signé par le serveur. Une ligne d'audit par action sensible, avec les identifiants effacés.",
   "**État qui survit :** le mode de sécurité et la dernière observation de chaque nœud sont restaurés après un redémarrage (un redémarrage ne désarme jamais le périmètre en silence) ; les fichiers sont écrits de façon atomique et un fichier abîmé est récupéré. Chaque changement d'alerte, de nœud et de mode est conservé dans un historique d'événements.",
   "**Alarmes :** un centre d'alarmes avec cycle déclenchée / acquittée / terminée, escalade d'une alarme critique qui attend sans être vue, une **vérification avant armement** (ce qui est ouvert, muet ou en panne), un PIN pour désarmer (et un PIN de contrainte) et des alarmes de nœuds, caméras, appareils, solaire, électrique, réseau et centrales d'alarme. Elles arrivent à Studio, aux téléphones (ntfy, Telegram, Home Assistant, un webhook signé, push Firebase si vous le configurez) et au sujet MQTT `armor/server/alert`.",
   "**Utilisateurs et rôles :** noms et mots de passe (hachages scrypt), un rôle `admin` qui gère les utilisateurs, un rôle `operator` qui opère et un rôle `viewer` qui ne fait que regarder ; changer le mot de passe ou le rôle ferme les autres sessions de cet utilisateur.",
   "**Appareils et automatisations :** fumée, gaz, inondation, porte, fenêtre, mouvement, climat, prise, lumière, sirène, serrure, volet, portail ou porte de garage et chauffe-eau, par MQTT ou push authentifié, avec état normalisé, disponibilité et commandes ; des règles qui actionnent des appareils quand quelque chose arrive (aussi par seuils).",
   "**Énergie :** onduleurs et blocs de batteries (avec chaque cellule et les capacités) et nœuds électriques arrivent par HTTP ou MQTT, sont validés par le contrat partagé, conservés avec un historique et l'énergie par jour, marqués périmés s'ils se taisent, et déclenchent des alarmes (panne d'onduleur, batterie faible, réseau perdu, tension, défaut de commutation…). Le schéma électrique et les règles pour commuter un circuit sont conservés sur le serveur.",
   "**Centrales d'alarme :** l'état des nœuds ARMOR-ALARM, la **conception de l'alarme** avec ses versions, les **appareils Zigbee liés aux zones** (le serveur dit à une centrale l'état d'une zone tant qu'il tient la radio) et des commandes d'armement / désarmement vers une centrale (désactivé sauf `ARMOR_ALARM_COMMANDS=1`).",
   "**Réseau local :** ce que rapporte le nœud ARMOR-NETWORK (appareils, internet, l'adresse publique et qui la donne), des ordres pour le nœud (balayage, ping, ports, inspecter un appareil avec un identifiant que vous donnez), noms, appareils masqués et surveillés, et identifiants qui voyagent **scellés pour le seul nœud**.",
   "**Voix, observation et entretien :** commandes écrites et parlées (liste fermée, en huit langues, avec une confirmation liée à la personne), le contexte pour le service d'observation (quels radars couvrent quelle caméra), le firmware des nœuds mis à jour depuis Studio un par un avec progression, et les mises à jour de l'installation depuis GitHub, celles du système et une console root optionnelle, le tout par l'assistant de maintenance.",
   "**Usage depuis l'extérieur :** le serveur distingue la maison de l'extérieur (un VPN compte comme la maison), garde des sessions plus courtes depuis l'extérieur, demande un second facteur (une application d'authentification, avec des codes de récupération) et le mot de passe à nouveau avant les actions critiques, permet de choisir ce qu'une session extérieure peut faire (tout, seulement manœuvrer l'alarme, seulement regarder), prévient les destinations des alarmes quand quelqu'un se connecte depuis un nouvel endroit et ouvre le panneau web d'un nœud via le serveur - épinglé au certificat du nœud, avec son cookie gardé sur le serveur - pour qu'aucun nœud ne soit jamais publié.",
   "**Liaison chiffrée facultative avec le broker (mqtts) :** `ARMOR_MQTT_CA_FILE` désigne le certificat de l'autorité propre à l'installation ; avec une adresse `mqtts://` le serveur ne fait confiance qu'à cette autorité et vérifie le nom du broker, et il refuse de démarrer si le fichier n'est pas un certificat valide ou si l'adresse n'est pas `mqtts://`. Studio montre si la liaison est chiffrée et l'empreinte de l'autorité. Testé contre un faux broker TLS et contre un vrai Mosquitto 2.0.",
   "**Santé des nœuds et modes d'armement :** conserve le dernier rapport et le journal des redémarrages de chaque nœud et lève quatre avertissements (peu de mémoire, redémarrages trop fréquents, un broker qui décroche à répétition, signal Wi-Fi faible) ; conserve les profils d'armement (Absent, Présent, Nuit et les vôtres) et met celui choisi dans la commande d'armer, seulement pour un nœud qui dit les comprendre. Une alarme forte ou discrète suit le profil ; un armement sans profil est la commande de toujours.",
   "**Historique des connexions et du système :** en plus des alertes, nœuds, caméras, appareils et alarmes, l'historique enregistre quels appareils et applications se connectent (sessions Studio, appli Android, panneaux des nœuds, service vocal : connexions, refus, déconnexions, sessions expirées, usage du second facteur, première et dernière fois vus) et les événements du système (nœuds qui apparaissent ou disparaissent avec leur firmware, lien avec le broker, réglages changés et par qui, services, mises à jour, armement avec son profil). Filtrable par type, catégorie, client et utilisateur ; l'adresse et l'agent utilisateur ne sont visibles que des administrateurs, et aucun mot de passe, jeton, cookie ni PIN n'est jamais enregistré."
  ],
  "intro": "**ARMOR-SERVER** est le centre de confiance d'A.R.M.O.R. Les nœuds de terrain publient des observations de radar, de lumière et de santé ; ce service les valide, garde le dernier état connu de chaque nœud et le sert à la console Studio et au client Android. Il possède aussi tout ce qui touche une caméra, de sorte qu'**aucun navigateur ni téléphone ne détient jamais un mot de passe de caméra ni une adresse RTSP**.",
  "sections": [
   {
    "icon": "🔒",
    "title": "Modèle de sécurité",
    "bullets": [
     "Secrets séparés : **ingest** (les nœuds publient leurs messages ; chaque nœud peut aussi avoir son propre jeton, dérivé du jeton partagé, et un mode strict n'accepte que ceux-là), **control** (armer / désarmer, événements), **operator** (automatisation) et la **connexion Studio** ; chacun est comparé en temps constant et aucun n'en remplace un autre. Un identifiant donné à un nœud réseau voyage scellé pour ce seul nœud.",
     "Trois rôles : **admin**, **operator** et **viewer** (lit, ne change jamais). Toute route qui configure, déplace, capture, enregistre, protège, supprime ou arme exige un opérateur ; la vidéo en direct exige un opérateur ou un ticket de flux de courte durée lié à une caméra. Les commandes dangereuses (désarmer, commuter un circuit, la console root) demandent un administrateur et, pour désarmer, le PIN.",
     "Les mots de passe des caméras ne vivent que dans `data/cameras.json`, chiffrés en AES-256-GCM, et aucune API ne les renvoie ; les adresses ONVIF doivent rester sur l'hôte de la caméra et les redirections sont refusées.",
     "Les sessions Studio sont HttpOnly et SameSite=Strict, la connexion est limitée en débit et les erreurs ne portent jamais de trace de pile.",
     "Le serveur écoute sur 127.0.0.1 sauf si `ARMOR_HOST` est défini volontairement, et alors un mot de passe Studio de moins de 12 caractères est refusé.",
     "Depuis l'extérieur : second facteur (TOTP, RFC 6238), une nouvelle preuve d'identité pour les utilisateurs, le firmware et les panneaux des nœuds, une politique qui réserve l'administration à la maison ou au VPN, uniquement des versions de firmware signées et un proxy de panneaux de nœuds qui ne prend jamais une adresse dans la requête, ne transmet que le nécessaire et refuse un nœud dont le certificat n'est pas celui de confiance."
    ]
   },
   {
    "icon": "🌐",
    "title": "API",
    "bullets": [
     "Publique : `GET /healthz`. Pour un utilisateur connecté : état, informations, caméras, médias, historique, règles, appareils, alarmes, automatisations, les conceptions (site, alarme, électrique, réseau), mesures solaires et électriques, le réseau local, notifications et préférences, et pour un administrateur utilisateurs, services, firmware, mises à jour et la console.",
     "Pour les nœuds : `POST /api/v1/telemetry`, `/health`, `/solar`, `/electrical/readings`, `/alarm/state`, `/network/state` et `/devices/state` avec le jeton d'ingestion, et les sujets MQTT `armor/node/#`, `armor/solar/#`, `armor/electrical/#`, `armor/alarm/#` et `armor/network/#`. Les événements atteignent les consoles par le WebSocket `/api/v1/events`.",
     "Chaque route (135 chemins aujourd'hui), sa règle d'accès et son schéma figurent dans le fichier OpenAPI d'[ARMOR-COMMON](https://github.com/JuanenRac/ARMOR-COMMON), et un test vérifie qu'aucune route n'y manque."
    ]
   },
   {
    "icon": "⚙️",
    "title": "Configuration",
    "bullets": [
     "Copiez `.env.example` vers `.env` (ignoré par Git), ou laissez `run.bat` / `run.sh` générer des secrets aléatoires au premier lancement.",
     "Obligatoires : `ARMOR_INGEST_TOKEN` et `ARMOR_CONTROL_TOKEN` (24 caractères ou plus, tous différents) et `ARMOR_STUDIO_USERNAME` / `ARMOR_STUDIO_PASSWORD` (le premier administrateur).",
     "Courantes : `ARMOR_HOST` / `ARMOR_PORT`, `ARMOR_DATA_DIR`, `ARMOR_FFMPEG_PATH` (vidéo en direct et capture), `ARMOR_MQTT_URL`, `ARMOR_MQTT_CA_FILE`, `ARMOR_STUDIO_ORIGIN`, `ARMOR_NODE_STALE_AFTER_S`, `ARMOR_CAMERA_CHECK_S`, `ARMOR_ALERT_DWELL_MS`, `ARMOR_ALERT_WEBHOOK_URL` et `ARMOR_COOKIE_SECURE` (à `1` derrière TLS).",
     "Optionnelles, toutes désactivées par défaut : `ARMOR_NTFY_URL`, `ARMOR_TELEGRAM_BOT_TOKEN`, `ARMOR_HOMEASSISTANT_URL`, `ARMOR_FCM_SERVICE_ACCOUNT` (push via le projet Firebase propre à l'installation), `ARMOR_ALARM_COMMANDS=1` (laisse le serveur armer et désarmer les centrales), `ARMOR_ELECTRICAL_SWITCHING` et `ARMOR_INGEST_STRICT=1`."
    ]
   }
  ],
  "note": "Pour installer sur le banc d'essai CM5 (isolé de tout autre projet, avec utilisateur et ports propres), voir [ARMOR-DEVOPS](https://github.com/JuanenRac/ARMOR-DEVOPS).",
  "fit": "ARMOR-SERVER est l'unique centre de confiance de la famille. Les nœuds de terrain ([ARMOR-RADAR](https://github.com/JuanenRac/ARMOR-RADAR), [ARMOR-SOLAR](https://github.com/JuanenRac/ARMOR-SOLAR), [ARMOR-ELECTRICAL](https://github.com/JuanenRac/ARMOR-ELECTRICAL), [ARMOR-ALARM](https://github.com/JuanenRac/ARMOR-ALARM), [ARMOR-HMI](https://github.com/JuanenRac/ARMOR-HMI)) et [ARMOR-NETWORK](https://github.com/JuanenRac/ARMOR-NETWORK) lui parlent en MQTT ou HTTP ; [ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) et [ARMOR-ANDROID-CONTROL](https://github.com/JuanenRac/ARMOR-ANDROID-CONTROL) le lisent et lui donnent des ordres ; [ARMOR-SERVER-AI](https://github.com/JuanenRac/ARMOR-SERVER-AI) pèse ce que voient les caméras face aux radars et ne fait que recommander ; [ARMOR-VOICE-AI](https://github.com/JuanenRac/ARMOR-VOICE-AI) transforme la parole en une liste fermée de commandes ; [ARMOR-DEVOPS](https://github.com/JuanenRac/ARMOR-DEVOPS) installe et met à jour tout cela sur la CM5. Le serveur décide : rien d'autre n'arme, ne désarme ni ne commute quoi que ce soit.",
  "hardware": "Le banc de test CM5, en usage quotidien : un vrai broker MQTT, de vraies caméras IP, un vrai nœud radar sur une carte ESP32-S3, Studio, l'application Android et les services de voix et d'observation contre lui"
 },
 "it": {
  "tagline": "Coordinatore centrale di sicurezza: nodi, allarmi, dispositivi, energia, telecamere, rete locale e manutenzione dell'impianto",
  "honest": "Ogni rotta, sessione, cifratura e regola delle prove qui sotto è reale e coperta da test (`npm test`: 510 test, compresa una suite completa di integrazione HTTP contro un server isolato e un controllo che ogni rotta sia documentata nel file OpenAPI). Funziona in uso quotidiano sul banco di prova CM5 con un vero broker MQTT, il firmware di un vero nodo radar su una scheda ESP32-S3, vere telecamere IP (video dal vivo, istantanee, registrazioni, PTZ sulle unità Hi3510), la console Studio, l'app Android e i servizi di voce e di osservazione. Ciò che **non** è ancora provato: ONVIF con una vera telecamera ONVIF, qualsiasi hardware Jetson, le rotte solari, elettriche, delle centrali d'allarme e del pannello touch con nodi reali (si provano con messaggi generati: esiste solo la scheda radar) e il push tramite Firebase con un vero progetto Firebase.",
  "bullets": [
   "**Ingresso validato:** i messaggi HTTP e MQTT di ogni tipo di nodo (radar, solare, elettrico, centrale d'allarme, rete) sono controllati al confine dal contratto condiviso prima di arrivare allo stato; un nodo può avere il proprio token (derivato da quello condiviso) e una modalità rigorosa non accetta altro.",
   "**Stato onesto dei nodi:** un nodo che smette di parlare appare *obsoleto* e *offline* dopo una finestra configurabile, mai online su dati vecchi; uno che si riconnette è contato dal suo ritorno, non dai vecchi messaggi. Disinserire cancella subito un allarme alto.",
   "**Gateway delle telecamere:** cassaforte cifrata delle telecamere, PTZ ONVIF / Hi3510 / PSIA, scoperta dei percorsi RTSP, un relay FFmpeg condiviso per telecamera, istantanee e registrazione MP4, un guardiano che trasforma una telecamera muta in un evento e, a impianto inserito, in un allarme, **zone dell'immagine da ignorare** e **foto e video fatti da soli** quando una telecamera vede qualcosa a impianto inserito.",
   "**Libreria delle prove:** conservazione per età e dimensione, **prove protette** mai cancellate, un SHA-256 per la catena di custodia e un file di **prova di custodia** firmato dal server. Una riga di audit per azione rilevante, con le credenziali rimosse.",
   "**Stato che sopravvive:** la modalità di sicurezza e l'ultima osservazione di ogni nodo sono ripristinate dopo un riavvio (un riavvio non disinserisce mai il perimetro in silenzio); i file sono scritti in modo atomico e uno danneggiato viene recuperato. Ogni cambio di allarme, nodo e modalità è conservato in uno storico degli eventi.",
   "**Allarmi:** un centro allarmi con ciclo generato / riconosciuto / chiuso, escalation di un allarme critico che attende senza essere visto, un **controllo prima di inserire** (cosa è aperto, muto o fermo), un PIN per disinserire (e un PIN di coercizione) e allarmi da nodi, telecamere, dispositivi, solare, elettrico, rete e centrali d'allarme. Arrivano a Studio, ai telefoni (ntfy, Telegram, Home Assistant, un webhook firmato, push Firebase se lo configuri) e al topic MQTT `armor/server/alert`.",
   "**Utenti e ruoli:** nomi e password (hash scrypt), un ruolo `admin` che gestisce gli utenti, un ruolo `operator` che opera e un ruolo `viewer` che guarda soltanto; cambiare la password o il ruolo chiude le altre sessioni di quell'utente.",
   "**Dispositivi e automazioni:** fumo, gas, allagamento, porta, finestra, movimento, clima, presa, luce, sirena, serratura, tapparella, cancello o porta del garage e scaldabagno, via MQTT o push autenticato, con stato normalizzato, disponibilità e comandi; regole che azionano dispositivi quando succede qualcosa (anche a soglia).",
   "**Energia:** inverter e pacchi batteria (con ogni cella e le capacità) e nodi elettrici arrivano via HTTP o MQTT, sono validati dal contratto condiviso, conservati con storico ed energia per giorno, segnati obsoleti se tacciono, e generano allarmi (guasto inverter, batteria scarica, rete persa, tensione, guasto di commutazione…). Lo schema elettrico e le regole per commutare un circuito sono conservati sul server.",
   "**Centrali d'allarme:** lo stato dei nodi ARMOR-ALARM, il **progetto dell'allarme** con le sue versioni, i **dispositivi Zigbee legati alle zone** (il server dice a una centrale com'è una zona mentre tiene la radio) e comandi di inserimento / disinserimento a una centrale (spenti salvo `ARMOR_ALARM_COMMANDS=1`).",
   "**Rete locale:** ciò che riferisce il nodo ARMOR-NETWORK (dispositivi, internet, l'indirizzo pubblico e chi lo dà), ordini per il nodo (scansione, ping, porte, ispezionare un dispositivo con un accesso che dai tu), nomi, dispositivi nascosti e sorvegliati, e accessi che viaggiano **sigillati per il solo nodo**.",
   "**Voce, osservazione e manutenzione:** comandi scritti e parlati (elenco chiuso, in otto lingue, con una conferma legata alla persona), il contesto per il servizio di osservazione (quali radar coprono quale telecamera), il firmware dei nodi aggiornato da Studio uno alla volta con avanzamento, e gli aggiornamenti dell'impianto da GitHub, quelli del sistema e una console root opzionale, tutto tramite l'assistente di manutenzione.",
   "**Uso da fuori casa:** il server distingue la casa dall'esterno (una VPN conta come la casa), mantiene sessioni più brevi da fuori, chiede un secondo fattore (un'app di autenticazione, con codici di recupero) e di nuovo la password prima delle azioni critiche, permette di scegliere cosa può fare una sessione esterna (tutto, solo gestire l'allarme, solo guardare), avvisa le destinazioni degli allarmi quando qualcuno accede da un luogo nuovo e apre il pannello web di un nodo tramite il server - vincolato al certificato del nodo, con il suo cookie tenuto sul server - così nessun nodo viene mai pubblicato.",
   "**Collegamento cifrato facoltativo con il broker (mqtts):** `ARMOR_MQTT_CA_FILE` indica il certificato dell'autorità propria dell'installazione; con un indirizzo `mqtts://` il server si fida solo di quell'autorità e controlla il nome del broker, e si rifiuta di partire se il file non è un certificato valido o l'indirizzo non è `mqtts://`. Studio mostra se il collegamento è cifrato e l'impronta dell'autorità. Provato contro un broker TLS di prova e contro un vero Mosquitto 2.0.",
   "**Salute dei nodi e modalità di inserimento:** conserva l'ultimo rapporto e il registro dei riavvii di ogni nodo e solleva quattro avvisi (poca memoria, riavvii troppo frequenti, un broker che cade di continuo, segnale Wi-Fi debole); conserva i profili di inserimento (Fuori casa, In casa, Notte e i tuoi) e mette quello scelto dentro il comando di inserimento, solo per un nodo che dice di capirli. Un allarme forte o discreto segue il profilo; un inserimento senza profilo è il comando di sempre.",
   "**Cronologia delle connessioni e del sistema:** oltre ad avvisi, nodi, telecamere, dispositivi e allarmi, la cronologia registra quali dispositivi e app si collegano (sessioni di Studio, app Android, pannelli dei nodi, servizio vocale: accessi, rifiuti, uscite, sessioni scadute, uso del secondo fattore, prima e ultima volta visti) e gli eventi del sistema (nodi che appaiono o scompaiono con il loro firmware, il collegamento con il broker, impostazioni cambiate e da chi, servizi, aggiornamenti, inserimento con il suo profilo). Si filtra per tipo, categoria, client e utente; indirizzo e user agent li vedono solo gli amministratori, e non si registra mai una password, un token, un cookie o un PIN."
  ],
  "intro": "**ARMOR-SERVER** è il centro di fiducia di A.R.M.O.R. I nodi di campo pubblicano osservazioni di radar, luce e salute; questo servizio le valida, conserva l'ultimo stato noto di ogni nodo e lo serve alla console Studio e al client Android. Possiede anche tutto ciò che tocca una telecamera, così **nessun browser né telefono detiene mai una password di telecamera o un indirizzo RTSP**.",
  "sections": [
   {
    "icon": "🔒",
    "title": "Modello di sicurezza",
    "bullets": [
     "Segreti separati: **ingest** (i nodi pubblicano i loro messaggi; ogni nodo può avere anche un proprio token, derivato da quello condiviso, e una modalità rigorosa accetta solo quelli), **control** (inserire / disinserire, eventi), **operator** (automazione) e il **login di Studio**; ciascuno è confrontato in tempo costante e nessuno sostituisce un altro. Un accesso dato a un nodo di rete viaggia sigillato per quel solo nodo.",
     "Tre ruoli: **admin**, **operator** e **viewer** (legge, non cambia mai). Ogni rotta che configura, sposta, cattura, registra, protegge, cancella o inserisce richiede un operatore; il video dal vivo richiede un operatore o un ticket di flusso di breve durata legato a una telecamera. I comandi pericolosi (disinserire, commutare un circuito, la console root) chiedono un amministratore e, per disinserire, il PIN.",
     "Le password delle telecamere vivono solo in `data/cameras.json`, cifrate con AES-256-GCM, e nessuna API le restituisce; gli indirizzi ONVIF devono restare sull'host della telecamera e i reindirizzamenti sono rifiutati.",
     "Le sessioni di Studio sono HttpOnly e SameSite=Strict, il login ha un limite di tentativi e gli errori non portano mai una traccia di stack.",
     "Il server ascolta su 127.0.0.1 a meno che `ARMOR_HOST` sia impostato di proposito, e allora una password di Studio di meno di 12 caratteri è rifiutata.",
     "Da fuori casa: secondo fattore (TOTP, RFC 6238), una nuova prova di identità per utenti, firmware e pannelli dei nodi, una politica che riserva l'amministrazione alla casa o alla VPN, solo release di firmware firmate e un proxy dei pannelli dei nodi che non prende mai un indirizzo dalla richiesta, passa solo il necessario e rifiuta un nodo il cui certificato non è quello attendibile."
    ]
   },
   {
    "icon": "🌐",
    "title": "API",
    "bullets": [
     "Pubblica: `GET /healthz`. Per un utente autenticato: stato, informazioni, telecamere, media, storico, regole, dispositivi, allarmi, automazioni, i progetti (sito, allarme, elettrico, rete), letture solari ed elettriche, la rete locale, notifiche e preferenze, e per un amministratore utenti, servizi, firmware, aggiornamenti e la console.",
     "Per i nodi: `POST /api/v1/telemetry`, `/health`, `/solar`, `/electrical/readings`, `/alarm/state`, `/network/state` e `/devices/state` con il token di ingest, e i topic MQTT `armor/node/#`, `armor/solar/#`, `armor/electrical/#`, `armor/alarm/#` e `armor/network/#`. Gli eventi raggiungono le console via WebSocket `/api/v1/events`.",
     "Ogni rotta (135 percorsi oggi), la sua regola di accesso e il suo schema sono nel file OpenAPI di [ARMOR-COMMON](https://github.com/JuanenRac/ARMOR-COMMON), e un test controlla che nessuna manchi."
    ]
   },
   {
    "icon": "⚙️",
    "title": "Configurazione",
    "bullets": [
     "Copia `.env.example` in `.env` (ignorato da Git), oppure lascia che `run.bat` / `run.sh` generino segreti casuali al primo avvio.",
     "Obbligatori: `ARMOR_INGEST_TOKEN` e `ARMOR_CONTROL_TOKEN` (24 caratteri o più, tutti diversi) e `ARMOR_STUDIO_USERNAME` / `ARMOR_STUDIO_PASSWORD` (il primo amministratore).",
     "Comuni: `ARMOR_HOST` / `ARMOR_PORT`, `ARMOR_DATA_DIR`, `ARMOR_FFMPEG_PATH` (video dal vivo e cattura), `ARMOR_MQTT_URL`, `ARMOR_MQTT_CA_FILE`, `ARMOR_STUDIO_ORIGIN`, `ARMOR_NODE_STALE_AFTER_S`, `ARMOR_CAMERA_CHECK_S`, `ARMOR_ALERT_DWELL_MS`, `ARMOR_ALERT_WEBHOOK_URL` e `ARMOR_COOKIE_SECURE` (a `1` dietro TLS).",
     "Opzionali, tutti spenti per impostazione predefinita: `ARMOR_NTFY_URL`, `ARMOR_TELEGRAM_BOT_TOKEN`, `ARMOR_HOMEASSISTANT_URL`, `ARMOR_FCM_SERVICE_ACCOUNT` (push tramite il progetto Firebase dell'impianto stesso), `ARMOR_ALARM_COMMANDS=1` (lascia che il server inserisca e disinserisca le centrali), `ARMOR_ELECTRICAL_SWITCHING` e `ARMOR_INGEST_STRICT=1`."
    ]
   }
  ],
  "note": "Per installare sul banco di prova CM5 (isolato da ogni altro progetto, con utente e porte proprie) vedi [ARMOR-DEVOPS](https://github.com/JuanenRac/ARMOR-DEVOPS).",
  "fit": "ARMOR-SERVER è l'unico centro di fiducia della famiglia. I nodi di campo ([ARMOR-RADAR](https://github.com/JuanenRac/ARMOR-RADAR), [ARMOR-SOLAR](https://github.com/JuanenRac/ARMOR-SOLAR), [ARMOR-ELECTRICAL](https://github.com/JuanenRac/ARMOR-ELECTRICAL), [ARMOR-ALARM](https://github.com/JuanenRac/ARMOR-ALARM), [ARMOR-HMI](https://github.com/JuanenRac/ARMOR-HMI)) e [ARMOR-NETWORK](https://github.com/JuanenRac/ARMOR-NETWORK) gli parlano via MQTT o HTTP; [ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) e [ARMOR-ANDROID-CONTROL](https://github.com/JuanenRac/ARMOR-ANDROID-CONTROL) lo leggono e gli danno ordini; [ARMOR-SERVER-AI](https://github.com/JuanenRac/ARMOR-SERVER-AI) pesa ciò che vedono le telecamere rispetto ai radar e si limita a raccomandare; [ARMOR-VOICE-AI](https://github.com/JuanenRac/ARMOR-VOICE-AI) trasforma la voce in un elenco chiuso di comandi; [ARMOR-DEVOPS](https://github.com/JuanenRac/ARMOR-DEVOPS) installa e aggiorna tutto sulla CM5. Il server decide: nient'altro inserisce, disinserisce o aziona qualcosa.",
  "hardware": "Il banco di prova CM5, in uso quotidiano: un vero broker MQTT, vere telecamere IP, un vero nodo radar su una scheda ESP32-S3, Studio, l'app Android e i servizi di voce e osservazione contro di esso"
 },
 "de": {
  "tagline": "Zentraler Sicherheitskoordinator: Knoten, Alarme, Geräte, Energie, Kameras, das lokale Netz und die Wartung der Anlage",
  "honest": "Jede Route, Sitzung, Verschlüsselung und Beweisregel unten ist real und durch Tests abgedeckt (`npm test`: 510 Tests, darunter eine vollständige HTTP-Integrationssuite gegen einen isolierten Server und eine Prüfung, dass jede Route in der OpenAPI-Datei dokumentiert ist). Er läuft im täglichen Einsatz auf dem CM5-Testaufbau mit einem echten MQTT-Broker, der Firmware eines echten Radarknotens auf einer ESP32-S3-Platine, echten IP-Kameras (Livevideo, Schnappschüsse, Aufnahmen, PTZ an den Hi3510-Geräten), der Studio-Konsole, der Android-App sowie den Sprach- und Beobachtungsdiensten. Was **noch nicht** bewiesen ist: ONVIF mit einer echten ONVIF-Kamera, jegliche Jetson-Hardware, die Solar-, Elektro-, Alarmzentralen- und Touchpanel-Routen mit echten Knoten (sie werden mit erzeugten Nachrichten getestet: nur die Radarplatine existiert) und Push über Firebase mit einem echten Firebase-Projekt.",
  "bullets": [
   "**Geprüfter Eingang:** HTTP- und MQTT-Nachrichten jeder Knotenart (Radar, Solar, Elektro, Alarmzentrale, Netzwerk) werden an der Grenze vom gemeinsamen Vertrag geprüft, bevor sie den Zustand erreichen; ein Knoten kann ein eigenes Token haben (vom gemeinsamen abgeleitet), und ein strenger Modus akzeptiert nichts anderes.",
   "**Ehrlicher Knotenzustand:** ein Knoten, der verstummt, wird nach einem einstellbaren Fenster als *veraltet* und *offline* angezeigt, nie als online mit alten Daten; ein sich wieder verbindender wird ab seiner Rückkehr gezählt, nicht ab seinen alten Nachrichten. Unscharfschalten löscht einen hohen Alarm sofort.",
   "**Kamera-Gateway:** verschlüsselter Kamera-Tresor, PTZ per ONVIF / Hi3510 / PSIA, RTSP-Pfadsuche, ein gemeinsames FFmpeg-Relay pro Kamera, Schnappschüsse und MP4-Aufnahme, ein Wächter, der eine stumme Kamera zu einem Ereignis und, wenn scharf, zu einem Alarm macht, **zu ignorierende Bildzonen** und **von selbst gemachte Fotos und Videos**, wenn eine Kamera im scharfen Zustand etwas sieht.",
   "**Beweisbibliothek:** Aufbewahrung nach Alter und Größe, **geschützte Beweise**, die nie gelöscht werden, ein SHA-256 für die Beweiskette und eine vom Server signierte **Verwahrungsnachweis**-Datei. Eine Audit-Zeile pro sicherheitsrelevanter Aktion, mit entfernten Zugangsdaten.",
   "**Zustand, der überlebt:** der Sicherheitsmodus und die letzte Beobachtung jedes Knotens werden nach einem Neustart wiederhergestellt (ein Neustart schaltet den Perimeter nie stillschweigend unscharf); Dateien werden atomar geschrieben und eine beschädigte wird wiederhergestellt. Jede Alarm-, Knoten- und Moduswechsel steht in einem Ereignisverlauf.",
   "**Alarme:** eine Alarmzentrale mit Lebenslauf ausgelöst / quittiert / beendet, Eskalation eines kritischen Alarms, der ungesehen wartet, eine **Prüfung vor dem Scharfschalten** (was offen, stumm oder ausgefallen ist), eine PIN zum Unscharfschalten (und eine Nötigungs-PIN) sowie Alarme von Knoten, Kameras, Geräten, Solar, Elektro, Netzwerk und Alarmzentralen. Sie erreichen Studio, die Telefone (ntfy, Telegram, Home Assistant, einen signierten Webhook, Firebase-Push bei Konfiguration) und das MQTT-Thema `armor/server/alert`.",
   "**Benutzer und Rollen:** Namen und Passwörter (scrypt-Hashes), eine Rolle `admin`, die Benutzer verwaltet, eine Rolle `operator`, die bedient, und eine Rolle `viewer`, die nur ansieht; ein geändertes Passwort oder eine geänderte Rolle beendet die anderen Sitzungen dieses Benutzers.",
   "**Geräte und Automationen:** Rauch, Gas, Wasser, Tür, Fenster, Bewegung, Klima, Steckdose, Licht, Sirene, Schloss, Rollladen, Tor oder Garagentor und Warmwasserbereiter über MQTT oder authentifizierten Push, mit normalisiertem Zustand, Verfügbarkeit und Befehlen; Regeln, die Geräte schalten, wenn etwas geschieht (auch per Schwellwert).",
   "**Energie:** Wechselrichter und Batteriestapel (mit jeder Zelle und den Kapazitäten) sowie Elektroknoten kommen per HTTP oder MQTT, werden vom gemeinsamen Vertrag geprüft, mit Verlauf und Energie pro Tag gespeichert, bei Schweigen als veraltet markiert und lösen Alarme aus (Wechselrichterfehler, Batterie schwach, Netz verloren, Spannung, Schaltfehler…). Der Elektroplan und die Regeln zum Schalten eines Stromkreises liegen auf dem Server.",
   "**Alarmzentralen:** der Zustand der ARMOR-ALARM-Knoten, der **Alarmplan** mit seinen Versionen, die **den Zonen zugeordneten Zigbee-Geräte** (der Server sagt einer Zentrale, wie eine Zone ist, solange er das Funkmodul hält) und Scharf-/Unscharf-Befehle an eine Zentrale (aus, außer mit `ARMOR_ALARM_COMMANDS=1`).",
   "**Lokales Netz:** was der ARMOR-NETWORK-Knoten meldet (Geräte, Internet, die öffentliche Adresse und wer sie liefert), Aufträge für den Knoten (Scan, Ping, Ports, ein Gerät mit einem von Ihnen gegebenen Login prüfen), Namen, versteckte und beobachtete Geräte sowie Zugangsdaten, die **nur für den Knoten versiegelt** reisen.",
   "**Sprache, Beobachtung und Wartung:** geschriebene und gesprochene Befehle (geschlossene Liste, in acht Sprachen, mit einer an die Person gebundenen Bestätigung), der Kontext für den Beobachtungsdienst (welche Radare welche Kamera abdecken), die Firmware der Knoten, von Studio aus nacheinander mit Fortschritt aktualisiert, sowie die Updates der Anlage selbst von GitHub, die des Systems und eine optionale Root-Konsole, alles über den Wartungshelfer.",
   "**Nutzung von außerhalb des Hauses:** Der Server unterscheidet das Haus vom Außen (ein VPN zählt als Haus), hält Sitzungen von außen kürzer, verlangt einen zweiten Faktor (Authenticator-App, mit Wiederherstellungscodes) und vor kritischen Aktionen erneut das Passwort, lässt wählen, was eine Sitzung von außen darf (alles, nur den Alarm bedienen, nur ansehen), meldet den Alarmzielen, wenn sich jemand von einem neuen Ort anmeldet, und öffnet das Web-Panel eines Knotens über den Server - an das Zertifikat des Knotens gebunden, mit seinem Cookie auf dem Server -, sodass nie ein Knoten veröffentlicht wird.",
   "**Optionale verschlüsselte Verbindung zum Broker (mqtts):** `ARMOR_MQTT_CA_FILE` nennt das Zertifikat der eigenen Zertifizierungsstelle der Anlage; bei einer `mqtts://`-Adresse vertraut der Server nur dieser Stelle und prüft den Namen des Brokers, und er startet nicht, wenn die Datei kein gültiges Zertifikat ist oder die Adresse nicht `mqtts://` lautet. Studio zeigt, ob die Verbindung verschlüsselt ist, und den Fingerabdruck der Stelle. Getestet gegen einen TLS-Broker-Ersatz und gegen einen echten Mosquitto 2.0.",
   "**Zustand der Knoten und Scharfschaltmodi:** speichert den letzten Bericht und das Neustartprotokoll jedes Knotens und löst vier Warnungen aus (wenig Speicher, zu häufige Neustarts, ein Broker, der immer wieder abreißt, schwaches WLAN-Signal); verwaltet die Scharfschaltprofile (Abwesend, Zuhause, Nacht und eigene) und legt das gewählte in den Scharfschaltbefehl, nur für einen Knoten, der sie versteht. Ein lauter oder leiser Alarm folgt dem Profil; ein Scharfschalten ohne Profil ist der Befehl wie immer.",
   "**Verlauf der Verbindungen und des Systems:** Neben Warnungen, Knoten, Kameras, Geräten und Alarmen zeichnet der Verlauf auf, welche Geräte und Apps sich verbinden (Studio-Sitzungen, die Android-App, die Panels der Knoten, der Sprachdienst: Anmeldungen, Ablehnungen, Abmeldungen, abgelaufene Sitzungen, Nutzung des zweiten Faktors, erste und letzte Sichtung) und die Ereignisse des Systems (Knoten, die mit ihrer Firmware auftauchen oder verschwinden, die Broker-Verbindung, geänderte Einstellungen und von wem, Dienste, Updates, Scharfschalten mit Profil). Filter nach Art, Kategorie, Client und Benutzer; Adresse und User-Agent sehen nur Administratoren, und nie wird ein Passwort, Token, Cookie oder PIN aufgezeichnet."
  ],
  "intro": "**ARMOR-SERVER** ist das vertrauenswürdige Zentrum von A.R.M.O.R. Feldknoten veröffentlichen Radar-, Licht- und Zustandsbeobachtungen; dieser Dienst validiert sie, hält den letzten bekannten Zustand jedes Knotens und stellt ihn der Studio-Konsole und dem Android-Client bereit. Er besitzt auch alles, was eine Kamera berührt, sodass **kein Browser und kein Telefon je ein Kamerapasswort oder eine RTSP-Adresse hält**.",
  "sections": [
   {
    "icon": "🔒",
    "title": "Sicherheitsmodell",
    "bullets": [
     "Getrennte Geheimnisse: **ingest** (die Knoten senden ihre Nachrichten; jeder Knoten kann außerdem ein eigenes, vom gemeinsamen abgeleitetes Token haben, und ein strenger Modus akzeptiert nur diese), **control** (scharf / unscharf, Ereignisse), **operator** (Automation) und das **Studio-Login**; jedes wird in konstanter Zeit verglichen, und keines ersetzt ein anderes. Ein einem Netzwerkknoten gegebener Login reist nur für diesen Knoten versiegelt.",
     "Drei Rollen: **admin**, **operator** und **viewer** (liest, ändert nie). Jede Route, die konfiguriert, bewegt, aufnimmt, aufzeichnet, schützt, löscht oder scharf schaltet, braucht einen Operator; Livevideo braucht einen Operator oder ein kurzlebiges Stream-Ticket für eine Kamera. Gefährliche Befehle (Unscharfschalten, einen Stromkreis schalten, die Root-Konsole) verlangen einen Administrator und zum Unscharfschalten die PIN.",
     "Kamerapasswörter liegen nur in `data/cameras.json`, mit AES-256-GCM verschlüsselt, und keine API gibt sie zurück; ONVIF-Adressen müssen auf dem Host der Kamera bleiben, und Weiterleitungen werden abgelehnt.",
     "Studio-Sitzungen sind HttpOnly und SameSite=Strict, das Login ist ratenbegrenzt, und Fehler tragen nie einen Stacktrace.",
     "Der Server lauscht auf 127.0.0.1, außer `ARMOR_HOST` wird absichtlich gesetzt; dann wird ein Studio-Passwort unter 12 Zeichen abgelehnt.",
     "Von außerhalb des Hauses: zweiter Faktor (TOTP, RFC 6238), ein neuer Identitätsnachweis für Benutzer, Firmware und Knoten-Panels, eine Richtlinie, die Verwaltung nur im Haus oder über das VPN erlaubt, nur signierte Firmware-Releases und ein Proxy für Knoten-Panels, der nie eine Adresse aus der Anfrage übernimmt, nur das Nötige weiterreicht und einen Knoten ablehnt, dessen Zertifikat nicht das vertrauenswürdige ist."
    ]
   },
   {
    "icon": "🌐",
    "title": "API",
    "bullets": [
     "Öffentlich: `GET /healthz`. Für einen angemeldeten Benutzer: Status, Informationen, Kameras, Medien, Verlauf, Regeln, Geräte, Alarme, Automationen, die Pläne (Standort, Alarm, Elektro, Netzwerk), Solar- und Elektrowerte, das lokale Netz, Benachrichtigungen und Einstellungen und für einen Administrator Benutzer, Dienste, Firmware, Updates und die Konsole.",
     "Für die Knoten: `POST /api/v1/telemetry`, `/health`, `/solar`, `/electrical/readings`, `/alarm/state`, `/network/state` und `/devices/state` mit dem Ingest-Token sowie die MQTT-Themen `armor/node/#`, `armor/solar/#`, `armor/electrical/#`, `armor/alarm/#` und `armor/network/#`. Ereignisse erreichen die Konsolen über den WebSocket `/api/v1/events`.",
     "Jede Route (heute 135 Pfade), ihre Zugriffsregel und ihr Schema stehen in der OpenAPI-Datei von [ARMOR-COMMON](https://github.com/JuanenRac/ARMOR-COMMON), und ein Test prüft, dass keine fehlt."
    ]
   },
   {
    "icon": "⚙️",
    "title": "Konfiguration",
    "bullets": [
     "Kopieren Sie `.env.example` nach `.env` (von Git ignoriert), oder lassen Sie `run.bat` / `run.sh` beim ersten Start zufällige Geheimnisse erzeugen.",
     "Erforderlich: `ARMOR_INGEST_TOKEN` und `ARMOR_CONTROL_TOKEN` (24 Zeichen oder mehr, alle verschieden) sowie `ARMOR_STUDIO_USERNAME` / `ARMOR_STUDIO_PASSWORD` (der erste Administrator).",
     "Üblich: `ARMOR_HOST` / `ARMOR_PORT`, `ARMOR_DATA_DIR`, `ARMOR_FFMPEG_PATH` (Livevideo und Aufnahme), `ARMOR_MQTT_URL`, `ARMOR_MQTT_CA_FILE`, `ARMOR_STUDIO_ORIGIN`, `ARMOR_NODE_STALE_AFTER_S`, `ARMOR_CAMERA_CHECK_S`, `ARMOR_ALERT_DWELL_MS`, `ARMOR_ALERT_WEBHOOK_URL` und `ARMOR_COOKIE_SECURE` (auf `1` hinter TLS).",
     "Optional, alle standardmäßig aus: `ARMOR_NTFY_URL`, `ARMOR_TELEGRAM_BOT_TOKEN`, `ARMOR_HOMEASSISTANT_URL`, `ARMOR_FCM_SERVICE_ACCOUNT` (Push über das eigene Firebase-Projekt der Anlage), `ARMOR_ALARM_COMMANDS=1` (lässt den Server Alarmzentralen scharf und unscharf schalten), `ARMOR_ELECTRICAL_SWITCHING` und `ARMOR_INGEST_STRICT=1`."
    ]
   }
  ],
  "note": "Zur Installation auf dem CM5-Prüfstand (isoliert von jedem anderen Projekt, eigener Benutzer, eigene Ports) siehe [ARMOR-DEVOPS](https://github.com/JuanenRac/ARMOR-DEVOPS).",
  "fit": "ARMOR-SERVER ist das eine vertrauenswürdige Zentrum der Familie. Die Feldknoten ([ARMOR-RADAR](https://github.com/JuanenRac/ARMOR-RADAR), [ARMOR-SOLAR](https://github.com/JuanenRac/ARMOR-SOLAR), [ARMOR-ELECTRICAL](https://github.com/JuanenRac/ARMOR-ELECTRICAL), [ARMOR-ALARM](https://github.com/JuanenRac/ARMOR-ALARM), [ARMOR-HMI](https://github.com/JuanenRac/ARMOR-HMI)) und [ARMOR-NETWORK](https://github.com/JuanenRac/ARMOR-NETWORK) sprechen per MQTT oder HTTP mit ihm; [ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) und [ARMOR-ANDROID-CONTROL](https://github.com/JuanenRac/ARMOR-ANDROID-CONTROL) lesen es und geben ihm Befehle; [ARMOR-SERVER-AI](https://github.com/JuanenRac/ARMOR-SERVER-AI) wägt ab, was die Kameras sehen, gegen die Radare und empfiehlt nur; [ARMOR-VOICE-AI](https://github.com/JuanenRac/ARMOR-VOICE-AI) macht aus Sprache eine geschlossene Liste von Befehlen; [ARMOR-DEVOPS](https://github.com/JuanenRac/ARMOR-DEVOPS) installiert und aktualisiert alles auf dem CM5. Der Server entscheidet: nichts sonst schaltet scharf, unscharf oder irgendetwas.",
  "hardware": "Der CM5-Testaufbau im täglichen Einsatz: ein echter MQTT-Broker, echte IP-Kameras, ein echter Radarknoten auf einer ESP32-S3-Platine, Studio, die Android-App und die Sprach- und Beobachtungsdienste daran"
 },
 "zh": {
  "tagline": "中央安全协调器：节点、报警、设备、能源、摄像头、本地网络和系统维护",
  "honest": "下面的每条路由、会话、加密和证据规则都是真实的，并有测试覆盖（`npm test`：510 个测试，包括针对隔离服务器的完整 HTTP 集成测试套件，以及检查每条路由都已写入 OpenAPI 文件）。它在 CM5 测试台上日常运行，配有真实的 MQTT 代理、ESP32-S3 板上真实雷达节点的固件、真实的 IP 摄像头（实时视频、快照、录像、Hi3510 设备上的 PTZ）、Studio 控制台、Android 应用以及语音和观察服务。**尚未**证明的是：用真实 ONVIF 摄像头测试 ONVIF、任何 Jetson 硬件、用真实节点测试太阳能、电气、报警主机和触摸屏的路由（它们用生成的消息测试：目前只有雷达板存在），以及用真实 Firebase 项目测试 Firebase 推送。",
  "bullets": [
   "**经过验证的接入：**每种节点（雷达、太阳能、电气、报警主机、网络）的 HTTP 和 MQTT 消息在到达状态之前，都由共享契约在边界处检查；节点可以有自己的令牌（由共享令牌派生），严格模式则不接受其他令牌。",
   "**诚实的节点状态：**停止通信的节点在可配置的时间窗口后显示为*过期*和*离线*，绝不会用旧数据显示为在线；重新连接的节点从其返回时开始计时，而不是从旧消息算起。撤防会立即清除高级警报。",
   "**摄像头网关：**加密的摄像头保险库、ONVIF / Hi3510 / PSIA 云台、RTSP 路径发现、每个摄像头一个共享的 FFmpeg 中继、快照和 MP4 录像、把沉默的摄像头变成事件（布防时变成报警）的看门狗、**要忽略的画面区域**，以及摄像头在布防时看到东西时**自动拍照和录像**。",
   "**证据库：**按时间和大小保留、**永不清理的受保护证据**、用于保管链的 SHA-256，以及由服务器签名的**保管证明**文件。每个安全相关操作一条审计记录，凭据已被清除。",
   "**可延续的状态：**安全模式和每个节点的最后观测在重启后恢复（重启绝不会悄悄撤防）；文件以原子方式写入，损坏的文件会被恢复。每次警报、节点和模式变化都保存在事件历史中。",
   "**报警：**一个报警中心，生命周期为触发 / 确认 / 解除，无人查看的严重报警会升级，**布防前检查**（哪些是打开、沉默或故障的）、撤防 PIN（以及胁迫 PIN），以及来自节点、摄像头、设备、太阳能、电气、网络和报警主机的报警。它们会送达 Studio、手机（ntfy、Telegram、Home Assistant、签名的 webhook、配置后的 Firebase 推送）以及 MQTT 主题 `armor/server/alert`。",
   "**用户与角色：**用户名和密码（scrypt 哈希）、管理用户的 `admin` 角色、负责操作的 `operator` 角色，以及只看不改的 `viewer` 角色；更改密码或角色会终止该用户的其他会话。",
   "**设备与自动化：**烟雾、燃气、漏水、门、窗、移动、气候、插座、灯、警笛、门锁、卷帘、大门或车库门和热水器设备，通过 MQTT 或经认证的推送接入，状态规范化，带可用性和命令；在发生事件时（包括阈值触发）切换设备的规则。",
   "**能源：**逆变器和电池组（含每个电芯和容量）以及电气节点通过 HTTP 或 MQTT 到达，由共享契约验证，保存历史和每日能量，沉默时标记为过期，并触发报警（逆变器故障、电池电量低、电网丢失、电压、开关故障……）。电气设计和切换回路的规则保存在服务器上。",
   "**报警主机：**ARMOR-ALARM 节点的状态、带版本的**报警设计**、**绑定到防区的 Zigbee 设备**（服务器持有无线电时，由它告诉主机某防区的状态），以及发给主机的布防 / 撤防命令（除非设置 `ARMOR_ALARM_COMMANDS=1`，否则关闭）。",
   "**本地网络：**ARMOR-NETWORK 节点报告的内容（设备、互联网、公网地址及其来源）、给节点的指令（扫描、ping、端口、用你提供的登录信息检查设备）、名称、隐藏和监视的设备，以及**仅为该节点加密封装**后传输的登录信息。",
   "**语音、观察与维护：**文字和语音命令（封闭列表，八种语言，确认与人绑定）、观察服务的上下文（哪些雷达覆盖哪个摄像头）、从 Studio 逐个更新并显示进度的节点固件，以及通过维护助手完成的、来自 GitHub 的系统自身更新、操作系统更新和可选的 root 控制台。",
   "**从家外使用：**服务器区分家中和外部（VPN 视为家中），外部会话更短，要求第二重验证（验证器应用，附恢复码），并在关键操作前再次要求密码；可选择外部会话能做什么（全部、仅操作警报、仅查看）；有人从新地点登录时通知警报接收渠道；并通过服务器打开节点的网页面板（绑定节点证书，其 Cookie 保存在服务器上），因此永远不需要公开任何节点。",
   "**可选的与代理加密连接(mqtts):** `ARMOR_MQTT_CA_FILE` 指向本安装自有证书颁发机构的证书;使用 `mqtts://` 地址时,服务器只信任该机构并检查代理名称;如果文件不是有效证书或地址不是 `mqtts://`,服务器拒绝启动。Studio 显示连接是否加密以及机构的指纹。已针对 TLS 代理替身和真实的 Mosquitto 2.0 测试。",
   "**节点健康与布防模式：** 保存每个节点的最新报告和重启记录，并发出四种警告（内存不足、重启过于频繁、代理反复断开、Wi-Fi 信号弱）；保存布防配置（离家、在家、夜间和您自己的），并把所选配置放进布防命令，只发给声明支持它的节点。警报的强弱遵循配置；不带配置的布防仍是原来的命令。",
   "**连接与系统历史：** 除警报、节点、摄像头、设备和报警外，历史还记录哪些设备和应用连接了服务器（Studio 会话、Android 应用、节点面板、语音服务：登录、被拒、退出、会话过期、第二重验证的使用、首次与最近出现），以及系统事件（带固件版本出现或消失的节点、代理连接、被更改的设置及操作人、服务、更新、含方案的布防）。可按类型、类别、客户端和用户筛选；地址和用户代理只显示给管理员，密码、令牌、Cookie 和 PIN 绝不会被记录。"
  ],
  "intro": "**ARMOR-SERVER** 是 A.R.M.O.R. 的可信中心。现场节点发布雷达、光照和健康观测；本服务验证它们，保存每个节点最后已知的状态，并提供给 Studio 控制台和 Android 客户端。它还掌管一切接触摄像头的事务，因此**没有任何浏览器或手机持有摄像头密码或 RTSP 地址**。",
  "sections": [
   {
    "icon": "🔒",
    "title": "安全模型",
    "bullets": [
     "彼此独立的密钥：**ingest**（节点发送消息；每个节点也可以有自己的、由共享令牌派生的令牌，严格模式只接受这些）、**control**（布防 / 撤防、事件）、**operator**（自动化）和 **Studio 登录**；每一种都以恒定时间比较，且互不替代。给网络节点的登录信息仅为该节点加密封装后传输。",
     "三种角色：**admin**、**operator** 和 **viewer**（只读，从不修改）。所有配置、移动、抓拍、录像、保护、删除或布防的路由都需要 operator；实时视频需要 operator 或绑定到某个摄像头的短期流票据。危险命令（撤防、切换回路、root 控制台）需要管理员，撤防还需要 PIN。",
     "摄像头密码只保存在 `data/cameras.json` 中，使用 AES-256-GCM 加密，任何 API 都不会返回它们；ONVIF 地址必须停留在摄像头自身的主机上，重定向会被拒绝。",
     "Studio 会话为 HttpOnly 和 SameSite=Strict，登录有速率限制，错误从不携带堆栈跟踪。",
     "服务器默认只监听 127.0.0.1，除非有意设置 `ARMOR_HOST`；此时短于 12 个字符的 Studio 密码会被拒绝。",
     "从家外使用：第二重验证（TOTP，RFC 6238）、对用户、固件和节点面板的重新身份验证、仅限家中或 VPN 管理的策略、只接受已签名的固件版本，以及节点面板代理——它从不从请求中获取地址、只转发必要内容，并拒绝证书与受信任证书不一致的节点。"
    ]
   },
   {
    "icon": "🌐",
    "title": "API",
    "bullets": [
     "公开：`GET /healthz`。对已登录用户：状态、信息、摄像头、媒体、历史、规则、设备、报警、自动化、各类设计（场地、报警、电气、网络）、太阳能和电气读数、本地网络、通知和偏好设置；对管理员还有用户、服务、固件、更新和控制台。",
     "面向节点：使用 ingest 令牌的 `POST /api/v1/telemetry`、`/health`、`/solar`、`/electrical/readings`、`/alarm/state`、`/network/state` 和 `/devices/state`，以及 MQTT 主题 `armor/node/#`、`armor/solar/#`、`armor/electrical/#`、`armor/alarm/#` 和 `armor/network/#`。事件通过 WebSocket `/api/v1/events` 送达控制台。",
     "每条路由（目前 135 个路径）、其访问规则和模式都写在 [ARMOR-COMMON](https://github.com/JuanenRac/ARMOR-COMMON) 的 OpenAPI 文件中，并有测试检查没有遗漏。"
    ]
   },
   {
    "icon": "⚙️",
    "title": "配置",
    "bullets": [
     "把 `.env.example` 复制为 `.env`（被 Git 忽略），或让 `run.bat` / `run.sh` 在首次运行时生成随机密钥。",
     "必填：`ARMOR_INGEST_TOKEN` 和 `ARMOR_CONTROL_TOKEN`（24 个字符以上，彼此不同），以及 `ARMOR_STUDIO_USERNAME` / `ARMOR_STUDIO_PASSWORD`（第一位管理员）。",
     "常用：`ARMOR_HOST` / `ARMOR_PORT`、`ARMOR_DATA_DIR`、`ARMOR_FFMPEG_PATH`（实时视频和抓拍）、`ARMOR_MQTT_URL`、`ARMOR_MQTT_CA_FILE`、`ARMOR_STUDIO_ORIGIN`、`ARMOR_NODE_STALE_AFTER_S`、`ARMOR_CAMERA_CHECK_S`、`ARMOR_ALERT_DWELL_MS`、`ARMOR_ALERT_WEBHOOK_URL` 和 `ARMOR_COOKIE_SECURE`（在 TLS 之后设为 `1`）。",
     "可选，默认全部关闭：`ARMOR_NTFY_URL`、`ARMOR_TELEGRAM_BOT_TOKEN`、`ARMOR_HOMEASSISTANT_URL`、`ARMOR_FCM_SERVICE_ACCOUNT`（通过本系统自己的 Firebase 项目推送）、`ARMOR_ALARM_COMMANDS=1`（让服务器对报警主机布防和撤防）、`ARMOR_ELECTRICAL_SWITCHING` 和 `ARMOR_INGEST_STRICT=1`。"
    ]
   }
  ],
  "note": "要安装到 CM5 测试台（与其他项目隔离，使用独立用户和端口），参见 [ARMOR-DEVOPS](https://github.com/JuanenRac/ARMOR-DEVOPS)。",
  "fit": "ARMOR-SERVER 是整个家族唯一可信的中心。现场节点（[ARMOR-RADAR](https://github.com/JuanenRac/ARMOR-RADAR)、[ARMOR-SOLAR](https://github.com/JuanenRac/ARMOR-SOLAR)、[ARMOR-ELECTRICAL](https://github.com/JuanenRac/ARMOR-ELECTRICAL)、[ARMOR-ALARM](https://github.com/JuanenRac/ARMOR-ALARM)、[ARMOR-HMI](https://github.com/JuanenRac/ARMOR-HMI)）和 [ARMOR-NETWORK](https://github.com/JuanenRac/ARMOR-NETWORK) 通过 MQTT 或 HTTP 与它通信；[ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) 和 [ARMOR-ANDROID-CONTROL](https://github.com/JuanenRac/ARMOR-ANDROID-CONTROL) 读取它并向它下达命令；[ARMOR-SERVER-AI](https://github.com/JuanenRac/ARMOR-SERVER-AI) 把摄像头看到的与雷达对照权衡，只给出建议；[ARMOR-VOICE-AI](https://github.com/JuanenRac/ARMOR-VOICE-AI) 把语音变成封闭的命令列表；[ARMOR-DEVOPS](https://github.com/JuanenRac/ARMOR-DEVOPS) 在 CM5 上安装并更新这一切。由服务器做决定：其他任何东西都不能布防、撤防或切换任何设备。",
  "hardware": "CM5 测试台的日常使用：真实的 MQTT 代理、真实的 IP 摄像头、ESP32-S3 板上的真实雷达节点，以及与之配合的 Studio、Android 应用和语音、观察服务"
 },
 "ja": {
  "tagline": "中央セキュリティコーディネーター：ノード、警報、デバイス、エネルギー、カメラ、ローカルネットワーク、設備の保守",
  "honest": "以下のすべてのルート、セッション、暗号化、証拠のルールは実在し、テストでカバーされています（`npm test`：510 件。隔離したサーバーに対する完全な HTTP 統合テストと、すべてのルートが OpenAPI ファイルに記載されていることの確認を含む）。CM5 テストベンチで日常的に動作しており、実際の MQTT ブローカー、ESP32-S3 基板上の実際のレーダーノードのファームウェア、実際の IP カメラ（ライブ映像、スナップショット、録画、Hi3510 機での PTZ）、Studio コンソール、Android アプリ、音声・観察サービスと組み合わせています。**まだ**証明されていないもの：実際の ONVIF カメラでの ONVIF、Jetson ハードウェア全般、実ノードでのソーラー・電気・警報盤・タッチパネルのルート（生成したメッセージでテスト：存在するのはレーダー基板のみ）、実際の Firebase プロジェクトでの Firebase プッシュ。",
  "bullets": [
   "**検証された受信：**あらゆる種類のノード（レーダー、ソーラー、電気、警報盤、ネットワーク）の HTTP・MQTT メッセージは、状態に届く前に共通のコントラクトで境界チェックされます。ノードは独自のトークン（共有トークンから導出）を持て、厳格モードではそれ以外を受け付けません。",
   "**正直なノード状態：**通信が止まったノードは、設定可能な時間を過ぎると*古い*・*オフライン*と表示され、古いデータでオンラインと見せることはありません。再接続したノードは古いメッセージではなく復帰時点から数えます。警戒解除で高レベルの警報はすぐに消えます。",
   "**カメラゲートウェイ：**暗号化したカメラの保管庫、ONVIF / Hi3510 / PSIA の PTZ、RTSP パスの探索、カメラごとに共有する FFmpeg リレー、スナップショットと MP4 録画、無応答のカメラをイベント（警戒中は警報）にするウォッチドッグ、**無視する映像ゾーン**、警戒中にカメラが何かを捉えたとき**自動で撮る写真と動画**。",
   "**証拠ライブラリ：**経過時間とサイズによる保持、決して削除されない**保護された証拠**、証拠保全用の SHA-256、サーバーが署名した**保管証明**ファイル。セキュリティ上重要な操作ごとに 1 行の監査記録（認証情報は除去）。",
   "**再起動後も残る状態：**セキュリティモードと各ノードの最後の観測は再起動後に復元されます（再起動で黙って警戒解除されることはありません）。ファイルはアトミックに書き込まれ、壊れたファイルは復旧されます。警報、ノード、モードの変化はすべてイベント履歴に残ります。",
   "**警報：**発生 / 確認 / 解除のライフサイクルを持つ警報センター、誰にも見られずに待つ重大警報のエスカレーション、**警戒前のチェック**（開いている、無応答、停止しているもの）、解除用 PIN（と強要時の PIN）、そしてノード・カメラ・デバイス・ソーラー・電気・ネットワーク・警報盤からの警報。Studio、スマートフォン（ntfy、Telegram、Home Assistant、署名付き Webhook、設定すれば Firebase プッシュ）、MQTT トピック `armor/server/alert` に届きます。",
   "**ユーザーとロール：**名前とパスワード（scrypt ハッシュ）、ユーザーを管理する `admin`、操作する `operator`、閲覧だけの `viewer`。パスワードやロールを変えると、そのユーザーの他のセッションは終了します。",
   "**デバイスとオートメーション：**煙、ガス、浸水、ドア、窓、動き、気候、プラグ、照明、サイレン、鍵、シャッター、門扉・ガレージドア、給湯器を MQTT または認証付きプッシュで扱い、正規化した状態、可用性、コマンドを持ちます。何かが起きたときにデバイスを切り替えるルール（しきい値トリガーも）。",
   "**エネルギー：**インバーターとバッテリースタック（各セルと容量を含む）、電気ノードが HTTP または MQTT で届き、共通コントラクトで検証され、履歴と日ごとのエネルギーとともに保存され、無応答なら古い扱いになり、警報（インバーター故障、バッテリー残量低下、系統喪失、電圧、スイッチ故障など）を出します。電気設計と回路を切り替えるルールはサーバーに保存されます。",
   "**警報盤：**ARMOR-ALARM ノードの状態、バージョン付きの**警報設計**、**ゾーンに結び付けた Zigbee デバイス**（サーバーが無線を持つ間、ゾーンの状態を警報盤に伝える）、警報盤への警戒・解除コマンド（`ARMOR_ALARM_COMMANDS=1` でなければオフ）。",
   "**ローカルネットワーク：**ARMOR-NETWORK ノードの報告（デバイス、インターネット、公開アドレスとその提供元）、ノードへの指示（スキャン、ping、ポート、あなたが渡したログインでデバイスを調べる）、名前、非表示・監視デバイス、そして**そのノードだけに封印されて**届くログイン情報。",
   "**音声、観察、保守：**文字と音声のコマンド（クローズドなリスト、8 言語、人に結び付いた確認）、観察サービス向けのコンテキスト（どのレーダーがどのカメラをカバーするか）、Studio から 1 台ずつ進捗付きで更新するノードのファームウェア、そして保守ヘルパー経由での GitHub からの設備自身の更新、システムの更新、任意の root コンソール。",
   "**家の外からの利用：**サーバーは家と外を区別し（VPN は家として扱う）、外からのセッションを短くし、2 段階認証（認証アプリ、復旧コード付き）を求め、重要な操作の前にパスワードを再度求めます。外からのセッションに許す操作（すべて、アラームの操作のみ、閲覧のみ）を選べ、新しい場所からのサインインを警報の通知先に知らせ、ノードのウェブパネルをサーバー経由で開きます（ノードの証明書に固定し、Cookie はサーバー側に保持）。ノードを公開することはありません。",
   "**ブローカーとの暗号化接続(mqtts、任意):** `ARMOR_MQTT_CA_FILE` で設備独自の認証局の証明書を指定します。`mqtts://` のアドレスではその認証局だけを信頼してブローカーの名前を確認し、ファイルが有効な証明書でない場合やアドレスが `mqtts://` でない場合は起動を拒否します。Studio は接続が暗号化されているかと認証局のフィンガープリントを表示します。TLS ブローカーの代役と実際の Mosquitto 2.0 で検証済みです。",
   "**ノードの状態と警戒モード:** 各ノードの最新の報告と再起動の記録を保持し、4 つの警告（メモリ不足、再起動の多さ、ブローカーの頻繁な切断、Wi-Fi 信号の弱さ）を出します。警戒プロファイル（外出、在宅、夜間、独自のもの）を保持し、選ばれたものを、対応すると申告したノードにだけ警戒コマンドに入れて送ります。警報の強弱はプロファイルに従い、プロファイルなしの警戒はこれまでどおりのコマンドです。",
   "**接続とシステムの履歴:** 警告・ノード・カメラ・デバイス・アラームに加えて、履歴は接続するデバイスとアプリ（Studio のセッション、Android アプリ、ノードのパネル、音声サービス。サインイン、拒否、サインアウト、期限切れ、第二要素の使用、初回と最終確認）と、システムのイベント（ファームウェア付きで現れたり消えたりするノード、ブローカー接続、変更された設定とその実行者、サービス、更新、プロファイル付きの警戒操作）を記録します。種類・カテゴリ・クライアント・ユーザーで絞り込め、アドレスとユーザーエージェントは管理者にだけ表示され、パスワード・トークン・クッキー・PIN は一切記録されません。"
  ],
  "intro": "**ARMOR-SERVER** は A.R.M.O.R. の信頼の中心です。フィールドノードがレーダー、光、ヘルスの観測を発行し、このサービスがそれを検証し、各ノードの最後に分かっている状態を保持して、Studio コンソールと Android クライアントに提供します。カメラに触れるすべてもここが持つので、**ブラウザーもスマートフォンもカメラのパスワードや RTSP アドレスを持つことはありません**。",
  "sections": [
   {
    "icon": "🔒",
    "title": "セキュリティモデル",
    "bullets": [
     "分離された秘密：**ingest**（ノードがメッセージを送る。各ノードは共有トークンから導出した独自トークンも持て、厳格モードではそれだけを受け付ける）、**control**（警戒 / 解除、イベント）、**operator**（オートメーション）、**Studio ログイン**。それぞれ定数時間で比較され、互いに代用できません。ネットワークノードに渡したログインはそのノードだけに封印されて届きます。",
     "3 つのロール：**admin**、**operator**、**viewer**（読むだけで変更しない）。設定、移動、撮影、録画、保護、削除、警戒を行うルートは operator が必要。ライブ映像は operator か、1 台のカメラに結び付いた短命のストリームチケットが必要です。危険なコマンド（解除、回路の切り替え、root コンソール）は管理者を要求し、解除には PIN も必要です。",
     "カメラのパスワードは `data/cameras.json` にのみ AES-256-GCM で暗号化して保存され、どの API も返しません。ONVIF のアドレスはカメラ自身のホストにとどまる必要があり、リダイレクトは拒否されます。",
     "Studio のセッションは HttpOnly かつ SameSite=Strict、ログインにはレート制限があり、エラーにスタックトレースは含まれません。",
     "サーバーは、意図して `ARMOR_HOST` を設定しない限り 127.0.0.1 で待ち受け、設定した場合は 12 文字未満の Studio パスワードが拒否されます。",
     "家の外から：2 段階認証（TOTP、RFC 6238）、ユーザー・ファームウェア・ノードパネルでの再認証、管理を家または VPN に限るポリシー、署名済みファームウェアのみ、そしてリクエストからアドレスを受け取らず必要なものだけを通し、信頼した証明書と異なるノードを拒否するノードパネル用プロキシ。"
    ]
   },
   {
    "icon": "🌐",
    "title": "API",
    "bullets": [
     "公開：`GET /healthz`。ログイン済みユーザー向け：状態、情報、カメラ、メディア、履歴、ルール、デバイス、警報、オートメーション、各種設計（サイト、警報、電気、ネットワーク）、ソーラーと電気の測定値、ローカルネットワーク、通知と設定。管理者向けにはユーザー、サービス、ファームウェア、アップデート、コンソール。",
     "ノード向け：ingest トークン付きの `POST /api/v1/telemetry`、`/health`、`/solar`、`/electrical/readings`、`/alarm/state`、`/network/state`、`/devices/state`、および MQTT トピック `armor/node/#`、`armor/solar/#`、`armor/electrical/#`、`armor/alarm/#`、`armor/network/#`。イベントは WebSocket `/api/v1/events` でコンソールに届きます。",
     "すべてのルート（現在 135 パス）、そのアクセスルール、スキーマは [ARMOR-COMMON](https://github.com/JuanenRac/ARMOR-COMMON) の OpenAPI ファイルにあり、抜けがないことをテストが確認します。"
    ]
   },
   {
    "icon": "⚙️",
    "title": "設定",
    "bullets": [
     "`.env.example` を `.env`（Git は無視）にコピーするか、`run.bat` / `run.sh` に初回実行時のランダムな秘密を生成させます。",
     "必須：`ARMOR_INGEST_TOKEN` と `ARMOR_CONTROL_TOKEN`（24 文字以上、すべて異なる）、および `ARMOR_STUDIO_USERNAME` / `ARMOR_STUDIO_PASSWORD`（最初の管理者）。",
     "よく使うもの：`ARMOR_HOST` / `ARMOR_PORT`、`ARMOR_DATA_DIR`、`ARMOR_FFMPEG_PATH`（ライブ映像と撮影）、`ARMOR_MQTT_URL`、`ARMOR_MQTT_CA_FILE`、`ARMOR_STUDIO_ORIGIN`、`ARMOR_NODE_STALE_AFTER_S`、`ARMOR_CAMERA_CHECK_S`、`ARMOR_ALERT_DWELL_MS`、`ARMOR_ALERT_WEBHOOK_URL`、`ARMOR_COOKIE_SECURE`（TLS の背後では `1`）。",
     "任意（すべて既定ではオフ）：`ARMOR_NTFY_URL`、`ARMOR_TELEGRAM_BOT_TOKEN`、`ARMOR_HOMEASSISTANT_URL`、`ARMOR_FCM_SERVICE_ACCOUNT`（設備自身の Firebase プロジェクト経由のプッシュ）、`ARMOR_ALARM_COMMANDS=1`（サーバーが警報盤を警戒・解除できるようにする）、`ARMOR_ELECTRICAL_SWITCHING`、`ARMOR_INGEST_STRICT=1`。"
    ]
   }
  ],
  "note": "CM5 テストベンチ（他のすべてのプロジェクトから隔離され、専用のユーザーとポートを持つ）へのインストールは [ARMOR-DEVOPS](https://github.com/JuanenRac/ARMOR-DEVOPS) を参照。",
  "fit": "ARMOR-SERVER はファミリーで唯一の信頼できる中心です。フィールドノード（[ARMOR-RADAR](https://github.com/JuanenRac/ARMOR-RADAR)、[ARMOR-SOLAR](https://github.com/JuanenRac/ARMOR-SOLAR)、[ARMOR-ELECTRICAL](https://github.com/JuanenRac/ARMOR-ELECTRICAL)、[ARMOR-ALARM](https://github.com/JuanenRac/ARMOR-ALARM)、[ARMOR-HMI](https://github.com/JuanenRac/ARMOR-HMI)）と [ARMOR-NETWORK](https://github.com/JuanenRac/ARMOR-NETWORK) は MQTT または HTTP で話しかけ、[ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) と [ARMOR-ANDROID-CONTROL](https://github.com/JuanenRac/ARMOR-ANDROID-CONTROL) はこれを読み取って指示を出し、[ARMOR-SERVER-AI](https://github.com/JuanenRac/ARMOR-SERVER-AI) はカメラの映像をレーダーと照らし合わせて推奨するだけ、[ARMOR-VOICE-AI](https://github.com/JuanenRac/ARMOR-VOICE-AI) は音声を閉じたコマンドの一覧に変え、[ARMOR-DEVOPS](https://github.com/JuanenRac/ARMOR-DEVOPS) はそのすべてを CM5 にインストール・更新します。決めるのはサーバーで、他の何も警戒・解除・切り替えを行いません。",
  "hardware": "CM5 テストベンチでの日常使用：実際の MQTT ブローカー、実際の IP カメラ、ESP32-S3 基板上の実際のレーダーノード、これに接続する Studio、Android アプリ、音声・観察サービス"
 },
 "pt": {
  "tagline": "Coordenador central de segurança: nós, alarmes, dispositivos, energia, câmaras, a rede local e a manutenção da instalação",
  "honest": "Cada rota, sessão, cifra e regra de provas abaixo é real e está coberta por testes (`npm test`: 510 testes, incluindo um conjunto completo de integração HTTP contra um servidor isolado e uma verificação de que cada rota está documentada no ficheiro OpenAPI). Funciona em uso diário na bancada de testes do CM5 com um broker MQTT real, o firmware de um nó radar real numa placa ESP32-S3, câmaras IP reais (vídeo em direto, fotografias, gravações, PTZ nas unidades Hi3510), a consola Studio, a aplicação Android e os serviços de voz e de observação. O que **ainda não** está provado: ONVIF com uma câmara ONVIF real, qualquer hardware Jetson, as rotas solares, elétricas, de centrais de alarme e de painel tátil com nós reais (testam-se com mensagens geradas: só existe a placa radar) e o push por Firebase com um projeto Firebase real.",
  "bullets": [
   "**Entrada validada:** as mensagens HTTP e MQTT de cada tipo de nó (radar, solar, elétrico, central de alarme, rede) são verificadas na fronteira pelo contrato partilhado antes de chegarem ao estado; um nó pode ter o seu próprio token (derivado do partilhado) e um modo estrito não aceita mais nada.",
   "**Estado honesto dos nós:** um nó que deixa de falar aparece como *desatualizado* e *desligado* após uma janela configurável, nunca como ligado com dados velhos; um que se volta a ligar conta desde o seu regresso, não desde as mensagens antigas. Desarmar limpa um alerta alto de imediato.",
   "**Porta de ligação das câmaras:** cofre cifrado das câmaras, PTZ ONVIF / Hi3510 / PSIA, descoberta de caminhos RTSP, um relé FFmpeg partilhado por câmara, fotografias e gravação MP4, um vigilante que transforma uma câmara muda num evento e, armado, num alarme, **zonas da imagem a ignorar** e **fotografias e vídeo feitos sozinhos** quando uma câmara vê algo estando armado.",
   "**Biblioteca de provas:** retenção por idade e tamanho, **provas protegidas** que nunca se apagam, um SHA-256 para a cadeia de custódia e um ficheiro de **prova de custódia** assinado pelo servidor. Uma linha de auditoria por ação relevante, com as credenciais removidas.",
   "**Estado que sobrevive:** o modo de segurança e a última observação de cada nó são restaurados após um reinício (um reinício nunca desarma o perímetro em silêncio); os ficheiros são escritos de forma atómica e um danificado é recuperado. Cada mudança de alerta, nó e modo fica guardada num histórico de eventos.",
   "**Alarmes:** um centro de alarmes com ciclo gerado / reconhecido / terminado, escalada de um alarme crítico que espera sem ser visto, uma **verificação antes de armar** (o que está aberto, mudo ou em baixo), um PIN para desarmar (e um PIN de coação) e alarmes de nós, câmaras, dispositivos, solar, elétrico, rede e centrais de alarme. Chegam ao Studio, aos telemóveis (ntfy, Telegram, Home Assistant, um webhook assinado, push por Firebase se o configurar) e ao tópico MQTT `armor/server/alert`.",
   "**Utilizadores e papéis:** nomes e palavras-passe (hashes scrypt), um papel `admin` que gere utilizadores, um papel `operator` que opera e um papel `viewer` que só observa; mudar a palavra-passe ou o papel termina as outras sessões desse utilizador.",
   "**Dispositivos e automatizações:** fumo, gás, inundação, porta, janela, movimento, clima, tomada, luz, sirene, fechadura, estore, portão ou porta de garagem e esquentador, por MQTT ou push autenticado, com estado normalizado, disponibilidade e comandos; regras que acionam dispositivos quando algo acontece (também por limiares).",
   "**Energia:** inversores e pilhas de baterias (com cada célula e as capacidades) e nós elétricos chegam por HTTP ou MQTT, são validados pelo contrato partilhado, guardados com histórico e energia por dia, marcados como desatualizados se calarem, e geram alarmes (avaria do inversor, bateria baixa, rede perdida, tensão, falha de comutação…). O desenho elétrico e as regras para comutar um circuito ficam no servidor.",
   "**Centrais de alarme:** o estado dos nós ARMOR-ALARM, o **desenho do alarme** com as suas versões, os **dispositivos Zigbee ligados às zonas** (o servidor diz a uma central como está uma zona enquanto tem o rádio) e comandos de armar / desarmar a uma central (desligados salvo `ARMOR_ALARM_COMMANDS=1`).",
   "**Rede local:** o que o nó ARMOR-NETWORK comunica (dispositivos, internet, o endereço público e quem o dá), ordens para o nó (varrimento, ping, portas, inspecionar um dispositivo com um acesso que você dá), nomes, dispositivos ocultos e vigiados, e acessos que viajam **selados só para o nó**.",
   "**Voz, observação e manutenção:** comandos escritos e falados (lista fechada, em oito idiomas, com uma confirmação ligada à pessoa), o contexto para o serviço de observação (que radares cobrem que câmara), o firmware dos nós atualizado a partir do Studio um a um com progresso, e as atualizações da própria instalação a partir do GitHub, as do sistema e uma consola root opcional, tudo através do assistente de manutenção.",
   "**Uso a partir de fora de casa:** o servidor distingue a casa do exterior (uma VPN conta como a casa), mantém sessões mais curtas a partir de fora, pede um segundo fator (uma app autenticadora, com códigos de recuperação) e a palavra-passe outra vez antes das ações críticas, deixa escolher o que uma sessão de fora pode fazer (tudo, só operar o alarme, só ver), avisa os destinos dos alarmes quando alguém entra de um sítio novo e abre o painel web de um nó através do servidor - fixado ao certificado do nó e com o seu cookie guardado no servidor - para que nenhum nó seja alguma vez publicado.",
   "**Ligação cifrada opcional ao broker (mqtts):** `ARMOR_MQTT_CA_FILE` indica o certificado da autoridade própria da instalação; com um endereço `mqtts://` o servidor confia só nessa autoridade e verifica o nome do broker, e recusa-se a arrancar se o ficheiro não for um certificado válido ou o endereço não for `mqtts://`. O Studio mostra se a ligação está cifrada e a impressão digital da autoridade. Testado contra um broker TLS de teste e contra um Mosquitto 2.0 real.",
   "**Saúde dos nós e modos de armar:** guarda o último relatório e o registo de reinícios de cada nó e levanta quatro avisos (pouca memória, reinícios demasiado frequentes, um broker que cai repetidamente, sinal Wi-Fi fraco); guarda os perfis de armar (Ausente, Em casa, Noite e os seus) e põe o escolhido dentro do comando de armar, só para um nó que diz entendê-los. Um alarme forte ou discreto segue o perfil; um armar sem perfil é o comando de sempre.",
   "**Histórico das ligações e do sistema:** além dos alertas, nós, câmaras, dispositivos e alarmes, o histórico regista que dispositivos e aplicações se ligam (sessões do Studio, a app Android, os painéis dos nós, o serviço de voz: inícios de sessão, recusas, saídas, sessões expiradas, uso do segundo fator, primeira e última vez vistos) e os eventos do sistema (nós que aparecem ou desaparecem com o seu firmware, a ligação ao broker, definições alteradas e por quem, serviços, atualizações, armar com o seu perfil). Filtra-se por tipo, categoria, cliente e utilizador; o endereço e o agente de utilizador só os veem os administradores, e nunca se regista uma palavra-passe, um token, um cookie nem um PIN."
  ],
  "intro": "O **ARMOR-SERVER** é o centro de confiança do A.R.M.O.R. Os nós de campo publicam observações de radar, luz e saúde; este serviço valida-as, guarda o último estado conhecido de cada nó e serve esse estado à consola Studio e ao cliente Android. É também dono de tudo o que toca numa câmara, para que **nenhum navegador nem telemóvel tenha alguma vez uma palavra-passe de câmara ou um endereço RTSP**.",
  "sections": [
   {
    "icon": "🔒",
    "title": "Modelo de segurança",
    "bullets": [
     "Segredos separados: **ingest** (os nós publicam as suas mensagens; cada nó pode ter ainda o seu próprio token, derivado do partilhado, e um modo estrito aceita só esses), **control** (armar / desarmar, eventos), **operator** (automatização) e o **login do Studio**; cada um é comparado em tempo constante e nenhum substitui outro. Um acesso dado a um nó de rede viaja selado só para esse nó.",
     "Três papéis: **admin**, **operator** e **viewer** (lê, nunca altera). Cada rota que configura, move, captura, grava, protege, apaga ou arma exige um operador; o vídeo em direto exige um operador ou um bilhete de emissão de curta duração ligado a uma câmara. Os comandos perigosos (desarmar, comutar um circuito, a consola root) pedem um administrador e, para desarmar, o PIN.",
     "As palavras-passe das câmaras vivem só em `data/cameras.json`, cifradas com AES-256-GCM, e nenhuma API as devolve; os endereços ONVIF têm de ficar no anfitrião da câmara e os redirecionamentos são recusados.",
     "As sessões do Studio são HttpOnly e SameSite=Strict, o login tem limite de tentativas e os erros nunca levam um rasto de pilha.",
     "O servidor escuta em 127.0.0.1 salvo se `ARMOR_HOST` for definido de propósito, e então uma palavra-passe do Studio com menos de 12 caracteres é recusada.",
     "A partir de fora de casa: segundo fator (TOTP, RFC 6238), uma nova prova de identidade para utilizadores, firmware e painéis dos nós, uma política que reserva a administração para a casa ou a VPN, só releases de firmware assinadas e um proxy de painéis de nós que nunca toma um endereço do pedido, só passa o necessário e recusa um nó cujo certificado não seja o de confiança."
    ]
   },
   {
    "icon": "🌐",
    "title": "API",
    "bullets": [
     "Pública: `GET /healthz`. Para um utilizador com sessão: estado, informação, câmaras, multimédia, histórico, regras, dispositivos, alarmes, automatizações, os desenhos (local, alarme, elétrico, rede), leituras solares e elétricas, a rede local, notificações e preferências, e para um administrador utilizadores, serviços, firmware, atualizações e a consola.",
     "Para os nós: `POST /api/v1/telemetry`, `/health`, `/solar`, `/electrical/readings`, `/alarm/state`, `/network/state` e `/devices/state` com o token de ingest, e os tópicos MQTT `armor/node/#`, `armor/solar/#`, `armor/electrical/#`, `armor/alarm/#` e `armor/network/#`. Os eventos chegam às consolas pelo WebSocket `/api/v1/events`.",
     "Cada rota (135 caminhos hoje), a sua regra de acesso e o seu esquema estão no ficheiro OpenAPI do [ARMOR-COMMON](https://github.com/JuanenRac/ARMOR-COMMON), e um teste verifica que nenhuma falta."
    ]
   },
   {
    "icon": "⚙️",
    "title": "Configuração",
    "bullets": [
     "Copie `.env.example` para `.env` (ignorado pelo Git), ou deixe o `run.bat` / `run.sh` gerar segredos aleatórios na primeira execução.",
     "Obrigatórios: `ARMOR_INGEST_TOKEN` e `ARMOR_CONTROL_TOKEN` (24 caracteres ou mais, todos diferentes) e `ARMOR_STUDIO_USERNAME` / `ARMOR_STUDIO_PASSWORD` (o primeiro administrador).",
     "Habituais: `ARMOR_HOST` / `ARMOR_PORT`, `ARMOR_DATA_DIR`, `ARMOR_FFMPEG_PATH` (vídeo em direto e captura), `ARMOR_MQTT_URL`, `ARMOR_MQTT_CA_FILE`, `ARMOR_STUDIO_ORIGIN`, `ARMOR_NODE_STALE_AFTER_S`, `ARMOR_CAMERA_CHECK_S`, `ARMOR_ALERT_DWELL_MS`, `ARMOR_ALERT_WEBHOOK_URL` e `ARMOR_COOKIE_SECURE` (a `1` atrás de TLS).",
     "Opcionais, todos desligados por defeito: `ARMOR_NTFY_URL`, `ARMOR_TELEGRAM_BOT_TOKEN`, `ARMOR_HOMEASSISTANT_URL`, `ARMOR_FCM_SERVICE_ACCOUNT` (push pelo projeto Firebase da própria instalação), `ARMOR_ALARM_COMMANDS=1` (deixa o servidor armar e desarmar as centrais), `ARMOR_ELECTRICAL_SWITCHING` e `ARMOR_INGEST_STRICT=1`."
    ]
   }
  ],
  "note": "Para instalar na bancada de testes CM5 (isolada de todos os outros projetos, utilizador próprio, portas próprias) veja o [ARMOR-DEVOPS](https://github.com/JuanenRac/ARMOR-DEVOPS).",
  "fit": "O ARMOR-SERVER é o único centro de confiança da família. Os nós de campo ([ARMOR-RADAR](https://github.com/JuanenRac/ARMOR-RADAR), [ARMOR-SOLAR](https://github.com/JuanenRac/ARMOR-SOLAR), [ARMOR-ELECTRICAL](https://github.com/JuanenRac/ARMOR-ELECTRICAL), [ARMOR-ALARM](https://github.com/JuanenRac/ARMOR-ALARM), [ARMOR-HMI](https://github.com/JuanenRac/ARMOR-HMI)) e o [ARMOR-NETWORK](https://github.com/JuanenRac/ARMOR-NETWORK) falam com ele por MQTT ou HTTP; o [ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) e o [ARMOR-ANDROID-CONTROL](https://github.com/JuanenRac/ARMOR-ANDROID-CONTROL) leem-no e dão-lhe ordens; o [ARMOR-SERVER-AI](https://github.com/JuanenRac/ARMOR-SERVER-AI) pesa o que as câmaras veem face aos radares e só recomenda; o [ARMOR-VOICE-AI](https://github.com/JuanenRac/ARMOR-VOICE-AI) transforma a voz numa lista fechada de comandos; o [ARMOR-DEVOPS](https://github.com/JuanenRac/ARMOR-DEVOPS) instala e atualiza tudo isso no CM5. O servidor decide: mais nada arma, desarma ou aciona o que quer que seja.",
  "hardware": "A bancada de testes do CM5, em uso diário: um broker MQTT real, câmaras IP reais, um nó radar real numa placa ESP32-S3, o Studio, a aplicação Android e os serviços de voz e observação contra ele"
 }
}
