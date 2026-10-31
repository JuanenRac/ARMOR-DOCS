# The facts that do not depend on the language, and the words of every language, of ARMOR-SERVER, in the universal README layout.
# Copyright (C) 2026 JuanenRac (Electro Hobby 3D). GPL-3.0-or-later.
from readme_src._kit import *  # noqa: F401,F403

FACTS = {'emoji': '🛡️',
 'layout': 'universal',
 'license_badge': 'License-GPL%203.0--or--later-blue',
 'status': [['software', 'green'],
            ['tests', 'green'],
            ['protocols', 'yellow'],
            ['hardware', 'yellow'],
            ['security', 'yellow'],
            ['integration', 'yellow'],
            ['docs', 'green']],
 'badges': [['Language', 'TypeScript', '3178c6'], ['Runtime', 'Node%2022%2B', '43853d'], ['Tests', '696%20passing', '2ea44f']]}

# the sentences of the previous layout that the new one keeps (already written in the eight languages)
LEGACY = {'en': {'tagline': 'Central security coordinator: nodes, alarms, devices, energy, cameras, the local network and the upkeep of the installation',
        'status': {'software': 'The routes, sessions, encryption and evidence rules run in daily use on the CM5 test bench.',
                   'tests': '696 tests pass (`npm test`), including a full HTTP integration suite against an isolated server and a check that every route is documented '
                            'in the OpenAPI file.',
                   'protocols': 'The radar messages come from a real board; the solar, electrical, alarm-panel and touch-panel routes are tested with generated '
                                'messages, and ONVIF has not met a real ONVIF camera.',
                   'hardware': 'It runs on the CM5 test bench with a real MQTT broker, real IP cameras (live video, snapshots, recordings, PTZ on the Hi3510 units) and '
                               'a real radar node; nothing has run on a Jetson.',
                   'security': 'The sessions, encryption, evidence and login rules are covered by tests; there has been no independent review.',
                   'integration': 'Studio, the Android app and the voice and observation services use it every day on the bench; push through Firebase has never run '
                                  'against a real Firebase project.',
                   'docs': 'Eight languages, the route reference (OpenAPI and ROUTES), the environment and remote-access guides and the changelog are up to date.'},
        'honest': 'Every route, session, encryption and evidence rule below is real and covered by tests (`npm test`: 696 tests, including a full HTTP integration suite '
                  'against an isolated server and a check that every route is documented in the OpenAPI file). It runs in daily use on the CM5 test bench with a real '
                  'MQTT broker, the firmware of a real radar node on an ESP32-S3 board, real IP cameras (live video, snapshots, recordings, PTZ on the Hi3510 units), '
                  'the Studio console, the Android app and the voice and observation services. What is **not** proven yet: ONVIF against a real ONVIF camera, any Jetson '
                  'hardware, the solar, electrical, alarm-panel and touch-panel routes against real nodes (they are tested with generated messages: only the radar board '
                  'exists) and push through Firebase against a real Firebase project.',
        'bullets': ['**Validated ingest:** HTTP and MQTT messages of every kind of node (radar, solar, electrical, alarm panel, network) are checked at the boundary by '
                    'the shared contract before they reach the state; a node may have its own token (derived from the shared one) and a strict mode accepts nothing '
                    'else.',
                    '**Honest node state:** a node that stops talking is shown as *stale* and *offline* after a configurable window, never as online on old data; one '
                    'that reconnects is counted from its return, not from its old messages. Disarming clears a high alert at once.',
                    '**Camera gateway:** encrypted camera vault, ONVIF / Hi3510 / PSIA PTZ, RTSP path discovery, one shared FFmpeg relay per camera, snapshots and MP4 '
                    'recording, a watchdog that turns a silent camera into an event and, while armed, an alarm, **zones of the picture to ignore** and **photos and '
                    'video taken by themselves** when a camera sees something while armed.',
                    '**Evidence library:** oldest-first retention by age and size, **protected evidence** that is never pruned, a SHA-256 for chain of custody and a '
                    '**proof of custody** file signed by the server. One audit line per security-relevant action, with credentials scrubbed.',
                    "**State that survives:** the security mode and every node's last observation are restored after a restart (a restart never silently disarms the "
                    'perimeter); files are written atomically and a damaged one is recovered. Every alert, node and mode change is kept in an event history.',
                    '**Alarms:** one alarm centre with a raised / acknowledged / cleared lifecycle, escalation of a critical alarm that waits unseen, a **check before '
                    'arming** (what is open, silent or down), a PIN to disarm (and a duress PIN) and alarms from nodes, cameras, devices, solar, electrical, network and '
                    'alarm panels. They reach Studio, the phones (ntfy, Telegram, Home Assistant, a signed webhook, Firebase push when you configure it) and the MQTT '
                    'topic `armor/server/alert`.',
                    '**Users and roles:** names and passwords (scrypt hashes), an `admin` role that manages users, an `operator` role that operates and a `viewer` role '
                    "that only looks; a changed password or role ends that user's other sessions.",
                    '**Devices and automations:** smoke, gas, flood, door, window, motion, climate, plug, light, siren, lock, shutter, gate and garage-door, and '
                    'water-heater devices over MQTT or an authenticated push, with normalised state, availability and commands; rules that switch devices when anything '
                    'happens (including threshold triggers).',
                    '**Energy:** inverters and battery stacks (with each cell and the capacities) and electrical nodes arrive by HTTP or MQTT, are validated by the '
                    'shared contract, kept with a history and a per-day energy, marked stale when silent, and raise alarms (inverter fault, battery low, grid lost, '
                    'voltage, switch fault…). The electrical design and the rules for switching a circuit are kept on the server.',
                    '**Alarm panels:** the state of the ARMOR-NODE-ALARM nodes, the **design of the alarm** kept with its versions, the **Zigbee devices tied to the '
                    'zones** (the server tells a panel how a zone is while it holds the radio) and arm / disarm commands to a panel (off unless '
                    '`ARMOR_ALARM_COMMANDS=1`).',
                    '**Local network:** what the ARMOR-NETWORK node reports (devices, internet, the public address and who gives it), orders for the node (sweep, ping, '
                    'ports, inspect a device with a login you give), names, hidden and watched devices, and logins that travel **sealed for the node alone**.',
                    "**Voice, observation and the nodes' upkeep:** written and spoken commands (a closed list, in eight languages, with a confirmation bound to the "
                    'person), the context for the observation service (which radars cover which camera), the firmware of the nodes updated from Studio one by one with '
                    "progress, and the installation's own updates from GitHub, the system's updates and an optional root console, all through the maintenance helper.",
                    '**Using it from outside the house:** the server tells the house from the outside (a VPN counts as the house), keeps shorter sessions from outside, '
                    'asks for a second factor (an authenticator app, with recovery codes) and for the password again before critical actions, lets you choose what a '
                    'session from outside may do (everything, operate the alarm only, only look), tells the places the alarms go to when someone signs in from a new '
                    'place, and opens the web panel of a node through the server - pinned to the certificate of the node, with its cookie kept on the server - so that '
                    'no node is ever published.',
                    "**Optional encrypted link to the broker (mqtts):** `ARMOR_MQTT_CA_FILE` names the certificate of the installation's own authority; with an "
                    "`mqtts://` address the server trusts that authority only and checks the broker's name, and it refuses to start if the file is not one valid "
                    "certificate or the address is not `mqtts://`. Studio shows whether the link is encrypted and the authority's fingerprint. Tested against a TLS "
                    'broker stand-in and against a real Mosquitto 2.0.',
                    '**Node health and arming modes:** keeps the latest report and the restart log of every node and raises four warnings (low memory, restarting too '
                    'often, a broker that keeps dropping, a weak Wi-Fi signal); keeps the arming profiles (Away, Home, Night and your own) and puts the chosen one '
                    'inside the arm command, only for a node that says it understands them. A loud or a quiet alarm follows the profile; an arm without one is the '
                    'command it always was.',
                    '**History of connections and of the system:** besides the alerts, nodes, cameras, devices and alarms, the history records which devices and apps '
                    'connect (Studio sessions, the Android app, the panels of the nodes, the voice service: sign-ins, refusals, sign-outs, expired sessions, use of the '
                    'second factor, first and last seen) and the events of the system (nodes that appear or disappear with their firmware, the broker link, settings '
                    'changed and by whom, services, updates, arming with its profile). It can be filtered by kind, category, client and user; the address and the user '
                    'agent are shown to administrators only, and no password, token, cookie or PIN is ever recorded.',
                    '**Orders to write to a Pylontech battery (off unless `ARMOR_BATTERY_WRITE=1`):** for administrators who have just proved who they are again - arm, '
                    "execute with the battery's serial number typed again, cancel, put an output back, keep a firmware image for an hour - checked against the shared "
                    'table of operations and ranges, sent to the gateway node as `solar_battery_command`, with every operation kept (who, which battery, what was read '
                    'before and after, the difference and the transcript, never the service password) and told to the history under *Batteries*.',
                    '**Control of the nodes:** `POST /api/v1/nodes/{id}/control` and `POST /api/v1/nodes/control` give one order (restart, pause, resume, standby, '
                    'identify, diagnostics, maintenance on or off) to one node or to every node that reports, only for an administrator who proved themselves again a '
                    "moment ago, with the node's name (or the word RESTART, PAUSE or STANDBY for all) typed again where the house would be left less guarded. The server "
                    'arms the order, executes it with the one-time token the node gives for that operation, follows each node (sent, acknowledged, applied, back) in '
                    '`GET /api/v1/nodes/control/operations`, restarts the alarm panels last in a rolling restart, records who ordered what in the history and the audit '
                    'trail, and shows paused, standby (work off, still connected) and maintenance in the node health. There is no factory reset, no erase and no deep '
                    'sleep. It is tested with a fake broker; it has not been tried on a real node.',
                    '**Live state and a route table:** the server pushes the whole state to Studio down a WebSocket at `/api/v1/events` whenever something changes (a '
                    'burst of changes is one message, and a client that falls behind is dropped), and every route it registers, with who may call it, is listed in a '
                    'table generated from the code. The wall panel has its own, smaller channel at `/api/v1/panel/events` (the same few hundred bytes of summary as `GET '
                    '/api/v1/panel/summary`, sent when it changes and every five seconds, for the panel, operator and administrator accounts; an administrator turns it '
                    'off with `panel.live_events`).'],
        'intro': '**ARMOR-SERVER** is the trusted centre of A.R.M.O.R. Field nodes publish radar, light and health observations; this service validates them, keeps the '
                 'last known state of every node, and serves that state to the Studio console and the Android client. It also owns everything that touches a camera, so '
                 'that **no browser and no phone ever holds a camera password or an RTSP address**.',
        'sections': [{'icon': '🔒',
                      'title': 'Security model',
                      'bullets': ['Separate secrets: **ingest** (the nodes post their messages; each node may also have its own token, derived from the shared one, and '
                                  'a strict mode accepts only those), **control** (arm / disarm, events), **operator** (automation) and the **Studio login**; each is '
                                  'compared in constant time and none stands in for another. A login given to a network node travels sealed for that node alone.',
                                  'Three roles: **admin**, **operator** and **viewer** (reads, never changes). Every route that configures, moves, captures, records, '
                                  'protects, deletes or arms needs an operator; live video needs an operator or a short-lived stream ticket tied to one camera. '
                                  'Dangerous commands (disarming, switching a circuit, the root console) ask for an administrator and, for disarming, the PIN.',
                                  'Camera passwords live only in `data/cameras.json`, AES-256-GCM encrypted, and no API returns them; ONVIF addresses must stay on the '
                                  "camera's host and redirects are refused.",
                                  'Studio sessions are HttpOnly and SameSite=Strict, login is rate limited and errors never carry a stack trace.',
                                  'The server listens on 127.0.0.1 unless `ARMOR_HOST` is set on purpose, and then a Studio password shorter than 12 characters is '
                                  'refused.',
                                  'From outside the house: the second factor (TOTP, RFC 6238), a new proof of identity for users, firmware and the node panels, a policy '
                                  'that keeps administering in the house or on the VPN, only signed firmware releases, and a proxy for node panels that never takes an '
                                  'address from the request, only passes what is needed and refuses a node whose certificate is not the trusted one.']},
                     {'icon': '🌐',
                      'title': 'API',
                      'bullets': ['Public: `GET /healthz`. For a signed-in user: status, information, cameras, media, history, rules, devices, alarms, automations, the '
                                  'designs (site, alarm, electrical, network), solar and electrical readings, the local network, notifications and preferences, and for '
                                  'an administrator users, services, firmware, updates and the console.',
                                  'For the nodes: `POST /api/v1/telemetry`, `/health`, `/solar`, `/electrical/readings`, `/alarm/state`, `/network/state` and '
                                  '`/devices/state` with the ingest token, and the MQTT topics `armor/node/#`, `armor/solar/#`, `armor/electrical/#`, `armor/alarm/#` '
                                  'and `armor/network/#`. Events reach the consoles by the WebSocket `/api/v1/events`.',
                                  'Every route (135 paths today), its access rule and its schema is in the OpenAPI file of '
                                  '[ARMOR-COMMON](https://github.com/JuanenRac/ARMOR-COMMON), and a test checks that no route is missing from it.']},
                     {'icon': '⚙️',
                      'title': 'Configuration',
                      'bullets': ['Copy `.env.example` to `.env` (ignored by Git), or let `run.bat` / `run.sh` generate random secrets on the first run.',
                                  'Required: `ARMOR_INGEST_TOKEN` and `ARMOR_CONTROL_TOKEN` (24 characters or more, all different) and `ARMOR_STUDIO_USERNAME` / '
                                  '`ARMOR_STUDIO_PASSWORD` (the first administrator).',
                                  'Common: `ARMOR_HOST` / `ARMOR_PORT`, `ARMOR_DATA_DIR`, `ARMOR_FFMPEG_PATH` (live video and capture), `ARMOR_MQTT_URL`, '
                                  '`ARMOR_MQTT_CA_FILE`, `ARMOR_STUDIO_ORIGIN`, `ARMOR_NODE_STALE_AFTER_S`, `ARMOR_CAMERA_CHECK_S`, `ARMOR_ALERT_DWELL_MS`, '
                                  '`ARMOR_ALERT_WEBHOOK_URL` and `ARMOR_COOKIE_SECURE` (set it to `1` behind TLS).',
                                  'Optional, all off by default: `ARMOR_NTFY_URL`, `ARMOR_TELEGRAM_BOT_TOKEN`, `ARMOR_HOMEASSISTANT_URL`, `ARMOR_FCM_SERVICE_ACCOUNT` '
                                  "(push through the installation's own Firebase project), `ARMOR_ALARM_COMMANDS=1` (let the server arm and disarm alarm panels), "
                                  '`ARMOR_ELECTRICAL_SWITCHING` and `ARMOR_INGEST_STRICT=1`.']}],
        'note': 'To install on the CM5 test bench (isolated from every other project, own user, own ports) see '
                '[ARMOR-DEVOPS](https://github.com/JuanenRac/ARMOR-DEVOPS).',
        'fit': 'ARMOR-SERVER is the one trusted centre of the family. The field nodes ([ARMOR-NODE-RADAR](https://github.com/JuanenRac/ARMOR-NODE-RADAR), '
               '[ARMOR-NODE-SOLAR](https://github.com/JuanenRac/ARMOR-NODE-SOLAR), [ARMOR-NODE-ELECTRICAL](https://github.com/JuanenRac/ARMOR-NODE-ELECTRICAL), '
               '[ARMOR-NODE-ALARM](https://github.com/JuanenRac/ARMOR-NODE-ALARM), [ARMOR-NODE-HMI](https://github.com/JuanenRac/ARMOR-NODE-HMI)) and '
               '[ARMOR-NETWORK](https://github.com/JuanenRac/ARMOR-NETWORK) speak to it over MQTT or HTTP; [ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) and '
               '[ARMOR-ANDROID-CONTROL](https://github.com/JuanenRac/ARMOR-ANDROID-CONTROL) read it and give it orders; '
               '[ARMOR-SERVER-AI](https://github.com/JuanenRac/ARMOR-SERVER-AI) weighs what the cameras see against the radars and only recommends; '
               '[ARMOR-VOICE-AI](https://github.com/JuanenRac/ARMOR-VOICE-AI) turns speech into a closed list of commands; '
               '[ARMOR-DEVOPS](https://github.com/JuanenRac/ARMOR-DEVOPS) installs and updates all of it on the CM5. The server decides: nothing else arms, disarms or '
               'switches anything.',
        'hardware': 'The CM5 test bench, in daily use: a real MQTT broker, real IP cameras, a real radar node on an ESP32-S3 board, Studio, the Android app and the '
                    'voice and observation services against it'},
 'es': {'tagline': 'Coordinador central de seguridad: nodos, alarmas, dispositivos, energía, cámaras, la red local y el mantenimiento de la instalación',
        'status': {'software': 'Las rutas, sesiones, cifrado y reglas de evidencias funcionan a diario en el banco de pruebas CM5.',
                   'tests': 'Pasan 696 pruebas (`npm test`), incluida una suite de integración HTTP completa contra un servidor aislado y una comprobación de que cada '
                            'ruta está documentada en el archivo OpenAPI.',
                   'protocols': 'Los mensajes del radar vienen de una placa real; las rutas solar, eléctrica, de panel de alarma y de panel táctil se prueban con '
                                'mensajes generados, y ONVIF no se ha probado con una cámara ONVIF real.',
                   'hardware': 'Funciona en el banco de pruebas CM5 con un broker MQTT real, cámaras IP reales (vídeo en vivo, capturas, grabaciones, PTZ en las '
                               'unidades Hi3510) y un nodo radar real; nada ha funcionado en una Jetson.',
                   'security': 'Las reglas de sesiones, cifrado, evidencias y acceso están cubiertas por pruebas; no ha habido una revisión independiente.',
                   'integration': 'Studio, la app de Android y los servicios de voz y observación lo usan a diario en el banco; el push mediante Firebase nunca se ha '
                                  'ejecutado contra un proyecto Firebase real.',
                   'docs': 'Ocho idiomas, la referencia de rutas (OpenAPI y ROUTES), las guías de entorno y de acceso remoto y el historial de cambios están al día.'},
        'honest': 'Cada ruta, sesión, cifrado y regla de evidencias de abajo es real y está cubierta por tests (`npm test`: 696 tests, con una suite completa de '
                  'integración HTTP contra un servidor aislado y una comprobación de que cada ruta está documentada en el fichero OpenAPI). Funciona en uso diario en el '
                  'banco de pruebas de la CM5 con un broker MQTT real, el firmware de un nodo radar real en una placa ESP32-S3, cámaras IP reales (vídeo en directo, '
                  'capturas, grabaciones, PTZ en las unidades Hi3510), la consola Studio, la app Android y los servicios de voz y de observación. Lo que **todavía no** '
                  'está probado: ONVIF con una cámara ONVIF real, cualquier hardware Jetson, las rutas solares, eléctricas, de centrales de alarma y de panel táctil con '
                  'nodos reales (se prueban con mensajes generados: solo existe la placa radar) y el push por Firebase con un proyecto Firebase real.',
        'bullets': ['**Entrada validada:** los mensajes HTTP y MQTT de cada tipo de nodo (radar, solar, eléctrico, central de alarma, red) se comprueban en la frontera '
                    'con el contrato compartido antes de llegar al estado; un nodo puede tener su propio token (derivado del compartido) y un modo estricto no acepta '
                    'otra cosa.',
                    '**Estado honesto de los nodos:** un nodo que deja de hablar se muestra como *obsoleto* y *desconectado* tras una ventana configurable, nunca como '
                    'en línea con datos viejos; uno que se reconecta cuenta desde su regreso, no desde sus mensajes antiguos. Desarmar borra una alerta alta al '
                    'instante.',
                    '**Pasarela de cámaras:** bóveda cifrada de cámaras, PTZ ONVIF / Hi3510 / PSIA, descubrimiento de rutas RTSP, un relé FFmpeg compartido por cámara, '
                    'capturas y grabación MP4, un vigilante que convierte una cámara muda en un evento y, armado, en una alarma, **zonas de la imagen que se ignoran** y '
                    '**fotos y vídeo hechos solos** cuando una cámara ve algo estando armado.',
                    '**Biblioteca de evidencias:** retención por antigüedad y tamaño, **evidencias protegidas** que nunca se borran, un SHA-256 para la cadena de '
                    'custodia y un fichero de **prueba de custodia** firmado por el servidor. Una línea de auditoría por acción relevante, con las credenciales '
                    'borradas.',
                    '**Estado que sobrevive:** el modo de seguridad y la última observación de cada nodo se restauran tras un reinicio (un reinicio nunca desarma el '
                    'perímetro en silencio); los ficheros se escriben de forma atómica y uno dañado se recupera. Cada cambio de alerta, nodo y modo se guarda en un '
                    'historial de eventos.',
                    '**Alarmas:** un centro de alarmas con ciclo generada / reconocida / cerrada, escalado de una alarma crítica que espera sin verse, una '
                    '**comprobación antes de armar** (qué está abierto, mudo o caído), un PIN para desarmar (y un PIN de coacción) y alarmas de nodos, cámaras, '
                    'dispositivos, solar, eléctrico, red y centrales de alarma. Llegan a Studio, a los móviles (ntfy, Telegram, Home Assistant, un webhook firmado, push '
                    'por Firebase si lo configuras) y al tema MQTT `armor/server/alert`.',
                    '**Usuarios y roles:** nombres y contraseñas (hashes scrypt), un rol `admin` que gestiona usuarios, un rol `operator` que opera y un rol `viewer` '
                    'que solo mira; cambiar la contraseña o el rol cierra las demás sesiones de ese usuario.',
                    '**Dispositivos y automatizaciones:** humo, gas, inundación, puerta, ventana, movimiento, clima, enchufe, luz, sirena, cerradura, persiana, puerta '
                    'de garaje o cancela y calentador de agua, por MQTT o push autenticado, con estado normalizado, disponibilidad y comandos; reglas que accionan '
                    'dispositivos cuando algo ocurre (también por umbrales).',
                    '**Energía:** inversores y pilas de baterías (con cada celda y las capacidades) y nodos eléctricos llegan por HTTP o MQTT, se validan con el '
                    'contrato compartido, se guardan con historial y energía por día, se marcan obsoletos si callan y generan alarmas (avería de inversor, batería baja, '
                    'red perdida, tensión, fallo de conmutación…). El diseño eléctrico y las reglas para conmutar un circuito se guardan en el servidor.',
                    '**Centrales de alarma:** el estado de los nodos ARMOR-NODE-ALARM, el **diseño de la alarma** con sus versiones, los **dispositivos Zigbee atados a '
                    'las zonas** (el servidor le dice a una central cómo está una zona mientras él tiene la radio) y comandos de armar / desarmar a una central (apagado '
                    'salvo `ARMOR_ALARM_COMMANDS=1`).',
                    '**Red local:** lo que informa el nodo ARMOR-NETWORK (dispositivos, internet, la dirección pública y quién la da), órdenes para el nodo (barrido, '
                    'ping, puertos, inspeccionar un dispositivo con un acceso que tú das), nombres, dispositivos ocultos y vigilados, y accesos que viajan **sellados '
                    'solo para el nodo**.',
                    '**Voz, observación y mantenimiento:** comandos escritos y hablados (lista cerrada, en ocho idiomas, con una confirmación ligada a la persona), el '
                    'contexto para el servicio de observación (qué radares cubren qué cámara), el firmware de los nodos actualizado desde Studio de uno en uno con '
                    'progreso, y las actualizaciones de la propia instalación desde GitHub, las del sistema y una consola root opcional, todo por el ayudante de '
                    'mantenimiento.',
                    '**Uso desde fuera de casa:** el servidor distingue la casa del exterior (una VPN cuenta como la casa), mantiene sesiones más cortas desde fuera, '
                    'pide un segundo factor (una app autenticadora, con códigos de recuperación) y la contraseña otra vez antes de las acciones críticas, deja elegir '
                    'qué puede hacer una sesión de fuera (todo, solo operar la alarma, solo mirar), avisa a los sitios de las alarmas cuando alguien entra desde un '
                    'lugar nuevo y abre el panel web de un nodo a través del servidor -fijado al certificado del nodo y con su cookie guardada en el servidor- para que '
                    'ningún nodo se publique nunca.',
                    '**Enlace cifrado opcional con el broker (mqtts):** `ARMOR_MQTT_CA_FILE` indica el certificado de la autoridad propia de la instalación; con una '
                    'dirección `mqtts://` el servidor confía solo en esa autoridad y comprueba el nombre del broker, y se niega a arrancar si el fichero no es un '
                    'certificado válido o la dirección no es `mqtts://`. Studio muestra si el enlace está cifrado y la huella de la autoridad. Probado contra un broker '
                    'TLS de pruebas y contra un Mosquitto 2.0 real.',
                    '**Salud de los nodos y modos de armado:** guarda el último informe y el registro de reinicios de cada nodo y levanta cuatro avisos (poca memoria, '
                    'reinicios demasiado frecuentes, un broker que se corta una y otra vez, señal Wi-Fi débil); guarda los perfiles de armado (Fuera, En casa, Noche y '
                    'los tuyos) y pone el elegido dentro del comando de armar, solo para un nodo que dice entenderlos. Una alarma fuerte o discreta sigue el perfil; un '
                    'armado sin perfil es el comando de siempre.',
                    '**Historial de conexiones y del sistema:** además de las alertas, nodos, cámaras, dispositivos y alarmas, el historial registra qué dispositivos y '
                    'apps se conectan (sesiones de Studio, la app Android, los paneles de los nodos, el servicio de voz: inicios de sesión, rechazos, cierres, sesiones '
                    'caducadas, uso del segundo factor, primera y última vez vistos) y los eventos del sistema (nodos que aparecen o desaparecen con su firmware, el '
                    'enlace con el broker, ajustes cambiados y por quién, servicios, actualizaciones, armado con su perfil). Se filtra por tipo, categoría, cliente y '
                    'usuario; la dirección y el agente de usuario solo los ven los administradores, y nunca se registra una contraseña, un token, una cookie ni un PIN.',
                    '**Órdenes para escribir en una batería Pylontech (desactivadas salvo `ARMOR_BATTERY_WRITE=1`):** para administradores que acaban de demostrar de '
                    'nuevo quiénes son - preparar, ejecutar con el número de serie de la batería escrito otra vez, cancelar, dejar una salida como estaba, guardar una '
                    'imagen de firmware durante una hora - comprobadas con la tabla compartida de operaciones y rangos, enviadas al nodo pasarela como '
                    '`solar_battery_command`, con cada operación guardada (quién, qué batería, lo leído antes y después, la diferencia y la transcripción, nunca la '
                    'contraseña de servicio) y contada en el historial en *Baterías*.',
                    '**Control de los nodos:** `POST /api/v1/nodes/{id}/control` y `POST /api/v1/nodes/control` dan una orden (reiniciar, pausar, reanudar, poner en '
                    'espera, identificar, diagnóstico, mantenimiento activado o desactivado) a un nodo o a todos los que informan, solo a un administrador que acaba de '
                    'demostrar quién es otra vez, con el nombre del nodo (o la palabra RESTART, PAUSE o STANDBY para todos) escrito de nuevo donde la casa quedaría '
                    'menos vigilada. El servidor prepara la orden, la ejecuta con el token de un solo uso que el nodo da para esa operación, sigue a cada nodo (enviada, '
                    'recibida, aplicada, de vuelta) en `GET /api/v1/nodes/control/operations`, reinicia las centrales de alarma las últimas en un reinicio escalonado, '
                    'anota quién ordenó qué en el historial y en la auditoría, y muestra en la salud del nodo si está en pausa, en espera (trabajo apagado, sigue '
                    'conectado) o en mantenimiento. No existe restablecimiento de fábrica, borrado ni sueño profundo. Se prueba con un broker simulado; no se ha probado '
                    'en un nodo real.',
                    '**Estado en vivo y tabla de rutas:** el servidor empuja el estado completo a Studio por un WebSocket en `/api/v1/events` cada vez que algo cambia '
                    '(una ráfaga de cambios es un solo mensaje y un cliente que se queda atrás se descarta), y cada ruta que registra, con quién puede llamarla, figura '
                    'en una tabla generada desde el código. El panel de pared tiene su propio canal, más pequeño, en `/api/v1/panel/events` (el mismo resumen de unos '
                    'cientos de bytes que `GET /api/v1/panel/summary`, enviado cuando cambia y cada cinco segundos, para las cuentas de panel, operador y administrador; '
                    'un administrador lo desactiva con `panel.live_events`).'],
        'intro': '**ARMOR-SERVER** es el centro de confianza de A.R.M.O.R. Los nodos de campo publican observaciones de radar, luz y salud; este servicio las valida, '
                 'guarda el último estado conocido de cada nodo y lo sirve a la consola Studio y al cliente Android. También es dueño de todo lo que toca una cámara, de '
                 'modo que **ningún navegador ni teléfono guarda jamás una contraseña de cámara ni una dirección RTSP**.',
        'sections': [{'icon': '🔒',
                      'title': 'Modelo de seguridad',
                      'bullets': ['Secretos separados: **ingest** (los nodos publican sus mensajes; cada nodo puede tener además su propio token, derivado del '
                                  'compartido, y un modo estricto acepta solo esos), **control** (armar / desarmar, eventos), **operator** (automatización) y el **login '
                                  'de Studio**; cada uno se compara en tiempo constante y ninguno sustituye a otro. Un acceso dado a un nodo de red viaja sellado solo '
                                  'para ese nodo.',
                                  'Tres roles: **admin**, **operator** y **viewer** (lee, nunca cambia). Cada ruta que configura, mueve, captura, graba, protege, borra '
                                  'o arma necesita un operador; el vídeo en directo necesita un operador o un ticket de emisión de corta vida ligado a una cámara. Los '
                                  'comandos peligrosos (desarmar, conmutar un circuito, la consola root) piden un administrador y, para desarmar, el PIN.',
                                  'Las contraseñas de las cámaras viven solo en `data/cameras.json`, cifradas con AES-256-GCM, y ninguna API las devuelve; las '
                                  'direcciones ONVIF deben quedarse en el host de la cámara y las redirecciones se rechazan.',
                                  'Las sesiones de Studio son HttpOnly y SameSite=Strict, el login tiene límite de intentos y los errores nunca llevan traza de pila.',
                                  'El servidor escucha en 127.0.0.1 salvo que `ARMOR_HOST` se ponga a propósito, y entonces se rechaza una contraseña de Studio de menos '
                                  'de 12 caracteres.',
                                  'Desde fuera de casa: segundo factor (TOTP, RFC 6238), una prueba de identidad nueva para usuarios, firmware y paneles de nodos, una '
                                  'política que deja administrar solo desde casa o la VPN, solo releases de firmware firmadas y un proxy de paneles de nodos que nunca '
                                  'toma una dirección de la petición, solo pasa lo necesario y rechaza un nodo cuyo certificado no sea el de confianza.']},
                     {'icon': '🌐',
                      'title': 'API',
                      'bullets': ['Pública: `GET /healthz`. Para un usuario con sesión: estado, información, cámaras, medios, historial, reglas, dispositivos, alarmas, '
                                  'automatizaciones, los diseños (sitio, alarma, eléctrico, red), lecturas solares y eléctricas, la red local, notificaciones y '
                                  'preferencias, y para un administrador usuarios, servicios, firmware, actualizaciones y la consola.',
                                  'Para los nodos: `POST /api/v1/telemetry`, `/health`, `/solar`, `/electrical/readings`, `/alarm/state`, `/network/state` y '
                                  '`/devices/state` con el token de ingest, y los temas MQTT `armor/node/#`, `armor/solar/#`, `armor/electrical/#`, `armor/alarm/#` y '
                                  '`armor/network/#`. Los eventos llegan a las consolas por el WebSocket `/api/v1/events`.',
                                  'Cada ruta (135 rutas hoy), su regla de acceso y su esquema están en el fichero OpenAPI de '
                                  '[ARMOR-COMMON](https://github.com/JuanenRac/ARMOR-COMMON), y un test comprueba que no falta ninguna.']},
                     {'icon': '⚙️',
                      'title': 'Configuración',
                      'bullets': ['Copia `.env.example` a `.env` (ignorado por Git), o deja que `run.bat` / `run.sh` generen secretos aleatorios la primera vez.',
                                  'Obligatorios: `ARMOR_INGEST_TOKEN` y `ARMOR_CONTROL_TOKEN` (24 caracteres o más, todos distintos) y `ARMOR_STUDIO_USERNAME` / '
                                  '`ARMOR_STUDIO_PASSWORD` (el primer administrador).',
                                  'Habituales: `ARMOR_HOST` / `ARMOR_PORT`, `ARMOR_DATA_DIR`, `ARMOR_FFMPEG_PATH` (vídeo en directo y captura), `ARMOR_MQTT_URL`, '
                                  '`ARMOR_MQTT_CA_FILE`, `ARMOR_STUDIO_ORIGIN`, `ARMOR_NODE_STALE_AFTER_S`, `ARMOR_CAMERA_CHECK_S`, `ARMOR_ALERT_DWELL_MS`, '
                                  '`ARMOR_ALERT_WEBHOOK_URL` y `ARMOR_COOKIE_SECURE` (ponlo a `1` tras TLS).',
                                  'Opcionales, todos apagados por defecto: `ARMOR_NTFY_URL`, `ARMOR_TELEGRAM_BOT_TOKEN`, `ARMOR_HOMEASSISTANT_URL`, '
                                  '`ARMOR_FCM_SERVICE_ACCOUNT` (push por el proyecto Firebase de la propia instalación), `ARMOR_ALARM_COMMANDS=1` (deja que el servidor '
                                  'arme y desarme las centrales), `ARMOR_ELECTRICAL_SWITCHING` y `ARMOR_INGEST_STRICT=1`.']}],
        'note': 'Para instalar en el banco de pruebas de la CM5 (aislado de todo otro proyecto, con usuario y puertos propios) véase '
                '[ARMOR-DEVOPS](https://github.com/JuanenRac/ARMOR-DEVOPS).',
        'fit': 'ARMOR-SERVER es el único centro de confianza de la familia. Los nodos de campo ([ARMOR-NODE-RADAR](https://github.com/JuanenRac/ARMOR-NODE-RADAR), '
               '[ARMOR-NODE-SOLAR](https://github.com/JuanenRac/ARMOR-NODE-SOLAR), [ARMOR-NODE-ELECTRICAL](https://github.com/JuanenRac/ARMOR-NODE-ELECTRICAL), '
               '[ARMOR-NODE-ALARM](https://github.com/JuanenRac/ARMOR-NODE-ALARM), [ARMOR-NODE-HMI](https://github.com/JuanenRac/ARMOR-NODE-HMI)) y '
               '[ARMOR-NETWORK](https://github.com/JuanenRac/ARMOR-NETWORK) le hablan por MQTT o HTTP; [ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) y '
               '[ARMOR-ANDROID-CONTROL](https://github.com/JuanenRac/ARMOR-ANDROID-CONTROL) lo leen y le dan órdenes; '
               '[ARMOR-SERVER-AI](https://github.com/JuanenRac/ARMOR-SERVER-AI) sopesa lo que ven las cámaras frente a los radares y solo recomienda; '
               '[ARMOR-VOICE-AI](https://github.com/JuanenRac/ARMOR-VOICE-AI) convierte la voz en una lista cerrada de comandos; '
               '[ARMOR-DEVOPS](https://github.com/JuanenRac/ARMOR-DEVOPS) lo instala y actualiza todo en la CM5. El servidor decide: nada más arma, desarma ni acciona '
               'nada.',
        'hardware': 'El banco de pruebas de la CM5, en uso diario: un broker MQTT real, cámaras IP reales, un nodo radar real en una placa ESP32-S3, Studio, la app '
                    'Android y los servicios de voz y observación contra él',
        'requirements': ['Node.js 22+', 'FFmpeg (vídeo en directo y captura)', 'un broker MQTT (Mosquitto)']},
 'fr': {'tagline': "Coordinateur central de sécurité : nœuds, alarmes, appareils, énergie, caméras, réseau local et entretien de l'installation",
        'status': {'software': "Les routes, les sessions, le chiffrement et les règles de preuves tournent au quotidien sur le banc d'essai CM5.",
                   'tests': "696 tests réussissent (`npm test`), dont une suite d'intégration HTTP complète contre un serveur isolé et un contrôle que chaque route est "
                            'documentée dans le fichier OpenAPI.',
                   'protocols': "Les messages du radar viennent d'une vraie carte ; les routes solaire, électrique, de centrale d'alarme et de panneau tactile sont "
                                "testées avec des messages générés, et ONVIF n'a pas rencontré de vraie caméra ONVIF.",
                   'hardware': "Il tourne sur le banc d'essai CM5 avec un vrai courtier MQTT, de vraies caméras IP (vidéo en direct, captures, enregistrements, PTZ sur "
                               "les unités Hi3510) et un vrai nœud radar ; rien n'a tourné sur un Jetson.",
                   'security': "Les règles de sessions, de chiffrement, de preuves et de connexion sont couvertes par des tests ; il n'y a pas eu de revue indépendante.",
                   'integration': "Studio, l'application Android et les services de voix et d'observation l'utilisent chaque jour sur le banc ; le push via Firebase n'a "
                                  'jamais tourné contre un vrai projet Firebase.',
                   'docs': "Huit langues, la référence des routes (OpenAPI et ROUTES), les guides d'environnement et d'accès à distance et le journal des modifications "
                           'sont à jour.'},
        'honest': 'Chaque route, session, chiffrement et règle de preuves ci-dessous est réel et couvert par des tests (`npm test` : 696 tests, dont une suite complète '
                  "d'intégration HTTP contre un serveur isolé et une vérification que chaque route est documentée dans le fichier OpenAPI). Il fonctionne en usage "
                  "quotidien sur le banc de test CM5 avec un vrai broker MQTT, le firmware d'un vrai nœud radar sur une carte ESP32-S3, de vraies caméras IP (vidéo en "
                  "direct, captures, enregistrements, PTZ sur les unités Hi3510), la console Studio, l'application Android et les services de voix et d'observation. Ce "
                  "qui n'est **pas** encore prouvé : ONVIF avec une vraie caméra ONVIF, tout matériel Jetson, les routes solaires, électriques, de centrales d'alarme et "
                  'de panneau tactile avec de vrais nœuds (testées avec des messages générés : seule la carte radar existe) et le push via Firebase avec un vrai projet '
                  'Firebase.',
        'bullets': ["**Entrée validée :** les messages HTTP et MQTT de chaque type de nœud (radar, solaire, électrique, centrale d'alarme, réseau) sont vérifiés à la "
                    "frontière par le contrat partagé avant d'atteindre l'état ; un nœud peut avoir son propre jeton (dérivé du jeton partagé) et un mode strict "
                    "n'accepte rien d'autre.",
                    '**État honnête des nœuds :** un nœud qui se tait est affiché *périmé* et *hors ligne* après une fenêtre configurable, jamais en ligne sur de '
                    'vieilles données ; un nœud qui se reconnecte est compté depuis son retour, pas depuis ses anciens messages. Désarmer efface une alerte haute '
                    'aussitôt.',
                    '**Passerelle de caméras :** coffre chiffré des caméras, PTZ ONVIF / Hi3510 / PSIA, découverte des chemins RTSP, un relais FFmpeg partagé par '
                    "caméra, captures et enregistrement MP4, un chien de garde qui transforme une caméra muette en événement et, armé, en alarme, **zones de l'image à "
                    "ignorer** et **photos et vidéo prises seules** quand une caméra voit quelque chose pendant l'armement.",
                    '**Bibliothèque de preuves :** rétention par ancienneté et taille, **preuves protégées** jamais effacées, un SHA-256 pour la chaîne de conservation '
                    "et un fichier de **preuve de conservation** signé par le serveur. Une ligne d'audit par action sensible, avec les identifiants effacés.",
                    '**État qui survit :** le mode de sécurité et la dernière observation de chaque nœud sont restaurés après un redémarrage (un redémarrage ne désarme '
                    "jamais le périmètre en silence) ; les fichiers sont écrits de façon atomique et un fichier abîmé est récupéré. Chaque changement d'alerte, de nœud "
                    "et de mode est conservé dans un historique d'événements.",
                    "**Alarmes :** un centre d'alarmes avec cycle déclenchée / acquittée / terminée, escalade d'une alarme critique qui attend sans être vue, une "
                    '**vérification avant armement** (ce qui est ouvert, muet ou en panne), un PIN pour désarmer (et un PIN de contrainte) et des alarmes de nœuds, '
                    "caméras, appareils, solaire, électrique, réseau et centrales d'alarme. Elles arrivent à Studio, aux téléphones (ntfy, Telegram, Home Assistant, un "
                    'webhook signé, push Firebase si vous le configurez) et au sujet MQTT `armor/server/alert`.',
                    '**Utilisateurs et rôles :** noms et mots de passe (hachages scrypt), un rôle `admin` qui gère les utilisateurs, un rôle `operator` qui opère et un '
                    'rôle `viewer` qui ne fait que regarder ; changer le mot de passe ou le rôle ferme les autres sessions de cet utilisateur.',
                    '**Appareils et automatisations :** fumée, gaz, inondation, porte, fenêtre, mouvement, climat, prise, lumière, sirène, serrure, volet, portail ou '
                    'porte de garage et chauffe-eau, par MQTT ou push authentifié, avec état normalisé, disponibilité et commandes ; des règles qui actionnent des '
                    'appareils quand quelque chose arrive (aussi par seuils).',
                    '**Énergie :** onduleurs et blocs de batteries (avec chaque cellule et les capacités) et nœuds électriques arrivent par HTTP ou MQTT, sont validés '
                    "par le contrat partagé, conservés avec un historique et l'énergie par jour, marqués périmés s'ils se taisent, et déclenchent des alarmes (panne "
                    "d'onduleur, batterie faible, réseau perdu, tension, défaut de commutation…). Le schéma électrique et les règles pour commuter un circuit sont "
                    'conservés sur le serveur.',
                    "**Centrales d'alarme :** l'état des nœuds ARMOR-NODE-ALARM, la **conception de l'alarme** avec ses versions, les **appareils Zigbee liés aux "
                    "zones** (le serveur dit à une centrale l'état d'une zone tant qu'il tient la radio) et des commandes d'armement / désarmement vers une centrale "
                    '(désactivé sauf `ARMOR_ALARM_COMMANDS=1`).',
                    "**Réseau local :** ce que rapporte le nœud ARMOR-NETWORK (appareils, internet, l'adresse publique et qui la donne), des ordres pour le nœud "
                    '(balayage, ping, ports, inspecter un appareil avec un identifiant que vous donnez), noms, appareils masqués et surveillés, et identifiants qui '
                    'voyagent **scellés pour le seul nœud**.',
                    '**Voix, observation et entretien :** commandes écrites et parlées (liste fermée, en huit langues, avec une confirmation liée à la personne), le '
                    "contexte pour le service d'observation (quels radars couvrent quelle caméra), le firmware des nœuds mis à jour depuis Studio un par un avec "
                    "progression, et les mises à jour de l'installation depuis GitHub, celles du système et une console root optionnelle, le tout par l'assistant de "
                    'maintenance.',
                    "**Usage depuis l'extérieur :** le serveur distingue la maison de l'extérieur (un VPN compte comme la maison), garde des sessions plus courtes "
                    "depuis l'extérieur, demande un second facteur (une application d'authentification, avec des codes de récupération) et le mot de passe à nouveau "
                    "avant les actions critiques, permet de choisir ce qu'une session extérieure peut faire (tout, seulement manœuvrer l'alarme, seulement regarder), "
                    "prévient les destinations des alarmes quand quelqu'un se connecte depuis un nouvel endroit et ouvre le panneau web d'un nœud via le serveur - "
                    "épinglé au certificat du nœud, avec son cookie gardé sur le serveur - pour qu'aucun nœud ne soit jamais publié.",
                    "**Liaison chiffrée facultative avec le broker (mqtts) :** `ARMOR_MQTT_CA_FILE` désigne le certificat de l'autorité propre à l'installation ; avec "
                    "une adresse `mqtts://` le serveur ne fait confiance qu'à cette autorité et vérifie le nom du broker, et il refuse de démarrer si le fichier n'est "
                    "pas un certificat valide ou si l'adresse n'est pas `mqtts://`. Studio montre si la liaison est chiffrée et l'empreinte de l'autorité. Testé contre "
                    'un faux broker TLS et contre un vrai Mosquitto 2.0.',
                    "**Santé des nœuds et modes d'armement :** conserve le dernier rapport et le journal des redémarrages de chaque nœud et lève quatre avertissements "
                    "(peu de mémoire, redémarrages trop fréquents, un broker qui décroche à répétition, signal Wi-Fi faible) ; conserve les profils d'armement (Absent, "
                    "Présent, Nuit et les vôtres) et met celui choisi dans la commande d'armer, seulement pour un nœud qui dit les comprendre. Une alarme forte ou "
                    'discrète suit le profil ; un armement sans profil est la commande de toujours.',
                    "**Historique des connexions et du système :** en plus des alertes, nœuds, caméras, appareils et alarmes, l'historique enregistre quels appareils et "
                    'applications se connectent (sessions Studio, appli Android, panneaux des nœuds, service vocal : connexions, refus, déconnexions, sessions expirées, '
                    'usage du second facteur, première et dernière fois vus) et les événements du système (nœuds qui apparaissent ou disparaissent avec leur firmware, '
                    'lien avec le broker, réglages changés et par qui, services, mises à jour, armement avec son profil). Filtrable par type, catégorie, client et '
                    "utilisateur ; l'adresse et l'agent utilisateur ne sont visibles que des administrateurs, et aucun mot de passe, jeton, cookie ni PIN n'est jamais "
                    'enregistré.',
                    "**Ordres d'écriture sur une batterie Pylontech (désactivés sauf `ARMOR_BATTERY_WRITE=1`) :** pour des administrateurs qui viennent de prouver à "
                    'nouveau qui ils sont - préparer, exécuter avec le numéro de série de la batterie saisi de nouveau, annuler, remettre une sortie comme avant, garder '
                    'une image de firmware pendant une heure - vérifiés avec la table partagée des opérations et plages, envoyés au nœud passerelle en '
                    '`solar_battery_command`, chaque opération étant conservée (qui, quelle batterie, ce qui a été lu avant et après, la différence et la transcription, '
                    "jamais le mot de passe de service) et consignée dans l'historique sous *Batteries*.",
                    '**Commande des nœuds :** `POST /api/v1/nodes/{id}/control` et `POST /api/v1/nodes/control` donnent un ordre (redémarrer, mettre en pause, '
                    'reprendre, mettre en veille, identifier, diagnostic, maintenance activée ou désactivée) à un nœud ou à tous ceux qui rapportent, uniquement à un '
                    'administrateur qui vient de se prouver de nouveau, avec le nom du nœud (ou le mot RESTART, PAUSE ou STANDBY pour tous) saisi de nouveau là où la '
                    "maison serait moins bien gardée. Le serveur prépare l'ordre, l'exécute avec le jeton à usage unique que le nœud donne pour cette opération, suit "
                    "chaque nœud (envoyé, reçu, appliqué, de retour) dans `GET /api/v1/nodes/control/operations`, redémarre les centrales d'alarme en dernier lors d'un "
                    "redémarrage échelonné, consigne qui a ordonné quoi dans l'historique et le journal d'audit, et montre dans la santé du nœud s'il est en pause, en "
                    "veille (travail arrêté, reste connecté) ou en maintenance. Il n'existe ni réinitialisation d'usine, ni effacement, ni sommeil profond. Il est testé "
                    "avec un faux broker ; il n'a pas été essayé sur un vrai nœud.",
                    "**État en direct et table des routes :** le serveur pousse l'état complet vers Studio par un WebSocket sur `/api/v1/events` dès que quelque chose "
                    'change (une rafale de changements est un seul message, et un client qui prend du retard est abandonné), et chaque route enregistrée, avec qui peut '
                    "l'appeler, figure dans une table générée à partir du code. Le panneau mural a son propre canal, plus petit, sur `/api/v1/panel/events` (le même "
                    "résumé de quelques centaines d'octets que `GET /api/v1/panel/summary`, envoyé quand il change et toutes les cinq secondes, pour les comptes "
                    'panneau, opérateur et administrateur ; un administrateur le coupe avec `panel.live_events`).'],
        'intro': "**ARMOR-SERVER** est le centre de confiance d'A.R.M.O.R. Les nœuds de terrain publient des observations de radar, de lumière et de santé ; ce service "
                 'les valide, garde le dernier état connu de chaque nœud et le sert à la console Studio et au client Android. Il possède aussi tout ce qui touche une '
                 "caméra, de sorte qu'**aucun navigateur ni téléphone ne détient jamais un mot de passe de caméra ni une adresse RTSP**.",
        'sections': [{'icon': '🔒',
                      'title': 'Modèle de sécurité',
                      'bullets': ['Secrets séparés : **ingest** (les nœuds publient leurs messages ; chaque nœud peut aussi avoir son propre jeton, dérivé du jeton '
                                  "partagé, et un mode strict n'accepte que ceux-là), **control** (armer / désarmer, événements), **operator** (automatisation) et la "
                                  "**connexion Studio** ; chacun est comparé en temps constant et aucun n'en remplace un autre. Un identifiant donné à un nœud réseau "
                                  'voyage scellé pour ce seul nœud.',
                                  'Trois rôles : **admin**, **operator** et **viewer** (lit, ne change jamais). Toute route qui configure, déplace, capture, enregistre, '
                                  'protège, supprime ou arme exige un opérateur ; la vidéo en direct exige un opérateur ou un ticket de flux de courte durée lié à une '
                                  'caméra. Les commandes dangereuses (désarmer, commuter un circuit, la console root) demandent un administrateur et, pour désarmer, le '
                                  'PIN.',
                                  'Les mots de passe des caméras ne vivent que dans `data/cameras.json`, chiffrés en AES-256-GCM, et aucune API ne les renvoie ; les '
                                  "adresses ONVIF doivent rester sur l'hôte de la caméra et les redirections sont refusées.",
                                  'Les sessions Studio sont HttpOnly et SameSite=Strict, la connexion est limitée en débit et les erreurs ne portent jamais de trace de '
                                  'pile.',
                                  'Le serveur écoute sur 127.0.0.1 sauf si `ARMOR_HOST` est défini volontairement, et alors un mot de passe Studio de moins de 12 '
                                  'caractères est refusé.',
                                  "Depuis l'extérieur : second facteur (TOTP, RFC 6238), une nouvelle preuve d'identité pour les utilisateurs, le firmware et les "
                                  "panneaux des nœuds, une politique qui réserve l'administration à la maison ou au VPN, uniquement des versions de firmware signées et "
                                  'un proxy de panneaux de nœuds qui ne prend jamais une adresse dans la requête, ne transmet que le nécessaire et refuse un nœud dont '
                                  "le certificat n'est pas celui de confiance."]},
                     {'icon': '🌐',
                      'title': 'API',
                      'bullets': ['Publique : `GET /healthz`. Pour un utilisateur connecté : état, informations, caméras, médias, historique, règles, appareils, '
                                  'alarmes, automatisations, les conceptions (site, alarme, électrique, réseau), mesures solaires et électriques, le réseau local, '
                                  'notifications et préférences, et pour un administrateur utilisateurs, services, firmware, mises à jour et la console.',
                                  'Pour les nœuds : `POST /api/v1/telemetry`, `/health`, `/solar`, `/electrical/readings`, `/alarm/state`, `/network/state` et '
                                  "`/devices/state` avec le jeton d'ingestion, et les sujets MQTT `armor/node/#`, `armor/solar/#`, `armor/electrical/#`, `armor/alarm/#` "
                                  'et `armor/network/#`. Les événements atteignent les consoles par le WebSocket `/api/v1/events`.',
                                  "Chaque route (135 chemins aujourd'hui), sa règle d'accès et son schéma figurent dans le fichier OpenAPI "
                                  "d'[ARMOR-COMMON](https://github.com/JuanenRac/ARMOR-COMMON), et un test vérifie qu'aucune route n'y manque."]},
                     {'icon': '⚙️',
                      'title': 'Configuration',
                      'bullets': ['Copiez `.env.example` vers `.env` (ignoré par Git), ou laissez `run.bat` / `run.sh` générer des secrets aléatoires au premier '
                                  'lancement.',
                                  'Obligatoires : `ARMOR_INGEST_TOKEN` et `ARMOR_CONTROL_TOKEN` (24 caractères ou plus, tous différents) et `ARMOR_STUDIO_USERNAME` / '
                                  '`ARMOR_STUDIO_PASSWORD` (le premier administrateur).',
                                  'Courantes : `ARMOR_HOST` / `ARMOR_PORT`, `ARMOR_DATA_DIR`, `ARMOR_FFMPEG_PATH` (vidéo en direct et capture), `ARMOR_MQTT_URL`, '
                                  '`ARMOR_MQTT_CA_FILE`, `ARMOR_STUDIO_ORIGIN`, `ARMOR_NODE_STALE_AFTER_S`, `ARMOR_CAMERA_CHECK_S`, `ARMOR_ALERT_DWELL_MS`, '
                                  '`ARMOR_ALERT_WEBHOOK_URL` et `ARMOR_COOKIE_SECURE` (à `1` derrière TLS).',
                                  'Optionnelles, toutes désactivées par défaut : `ARMOR_NTFY_URL`, `ARMOR_TELEGRAM_BOT_TOKEN`, `ARMOR_HOMEASSISTANT_URL`, '
                                  "`ARMOR_FCM_SERVICE_ACCOUNT` (push via le projet Firebase propre à l'installation), `ARMOR_ALARM_COMMANDS=1` (laisse le serveur armer "
                                  'et désarmer les centrales), `ARMOR_ELECTRICAL_SWITCHING` et `ARMOR_INGEST_STRICT=1`.']}],
        'note': "Pour installer sur le banc d'essai CM5 (isolé de tout autre projet, avec utilisateur et ports propres), voir "
                '[ARMOR-DEVOPS](https://github.com/JuanenRac/ARMOR-DEVOPS).',
        'fit': "ARMOR-SERVER est l'unique centre de confiance de la famille. Les nœuds de terrain ([ARMOR-NODE-RADAR](https://github.com/JuanenRac/ARMOR-NODE-RADAR), "
               '[ARMOR-NODE-SOLAR](https://github.com/JuanenRac/ARMOR-NODE-SOLAR), [ARMOR-NODE-ELECTRICAL](https://github.com/JuanenRac/ARMOR-NODE-ELECTRICAL), '
               '[ARMOR-NODE-ALARM](https://github.com/JuanenRac/ARMOR-NODE-ALARM), [ARMOR-NODE-HMI](https://github.com/JuanenRac/ARMOR-NODE-HMI)) et '
               '[ARMOR-NETWORK](https://github.com/JuanenRac/ARMOR-NETWORK) lui parlent en MQTT ou HTTP ; [ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) et '
               '[ARMOR-ANDROID-CONTROL](https://github.com/JuanenRac/ARMOR-ANDROID-CONTROL) le lisent et lui donnent des ordres ; '
               '[ARMOR-SERVER-AI](https://github.com/JuanenRac/ARMOR-SERVER-AI) pèse ce que voient les caméras face aux radars et ne fait que recommander ; '
               '[ARMOR-VOICE-AI](https://github.com/JuanenRac/ARMOR-VOICE-AI) transforme la parole en une liste fermée de commandes ; '
               "[ARMOR-DEVOPS](https://github.com/JuanenRac/ARMOR-DEVOPS) installe et met à jour tout cela sur la CM5. Le serveur décide : rien d'autre n'arme, ne "
               'désarme ni ne commute quoi que ce soit.',
        'hardware': 'Le banc de test CM5, en usage quotidien : un vrai broker MQTT, de vraies caméras IP, un vrai nœud radar sur une carte ESP32-S3, Studio, '
                    "l'application Android et les services de voix et d'observation contre lui",
        'requirements': ['Node.js 22+', 'FFmpeg (vidéo en direct et capture)', 'un broker MQTT (Mosquitto)']},
 'it': {'tagline': "Coordinatore centrale di sicurezza: nodi, allarmi, dispositivi, energia, telecamere, rete locale e manutenzione dell'impianto",
        'status': {'software': 'Le route, le sessioni, la cifratura e le regole delle prove girano ogni giorno sul banco di prova CM5.',
                   'tests': 'Superano 696 test (`npm test`), compresa una suite di integrazione HTTP completa contro un server isolato e un controllo che ogni rotta sia '
                            'documentata nel file OpenAPI.',
                   'protocols': "I messaggi del radar vengono da una scheda reale; le rotte solare, elettrica, della centralina d'allarme e del pannello touch sono "
                                'provate con messaggi generati, e ONVIF non ha incontrato una vera telecamera ONVIF.',
                   'hardware': 'Gira sul banco di prova CM5 con un broker MQTT reale, telecamere IP reali (video dal vivo, istantanee, registrazioni, PTZ sulle unità '
                               'Hi3510) e un nodo radar reale; nulla ha girato su una Jetson.',
                   'security': "Le regole di sessioni, cifratura, prove e accesso sono coperte da test; non c'è stata una revisione indipendente.",
                   'integration': "Studio, l'app Android e i servizi di voce e osservazione lo usano ogni giorno sul banco; il push tramite Firebase non è mai stato "
                                  'eseguito contro un vero progetto Firebase.',
                   'docs': 'Otto lingue, il riferimento delle rotte (OpenAPI e ROUTES), le guide di ambiente e accesso remoto e il registro delle modifiche sono '
                           'aggiornati.'},
        'honest': 'Ogni rotta, sessione, cifratura e regola delle prove qui sotto è reale e coperta da test (`npm test`: 696 test, compresa una suite completa di '
                  'integrazione HTTP contro un server isolato e un controllo che ogni rotta sia documentata nel file OpenAPI). Funziona in uso quotidiano sul banco di '
                  'prova CM5 con un vero broker MQTT, il firmware di un vero nodo radar su una scheda ESP32-S3, vere telecamere IP (video dal vivo, istantanee, '
                  "registrazioni, PTZ sulle unità Hi3510), la console Studio, l'app Android e i servizi di voce e di osservazione. Ciò che **non** è ancora provato: "
                  "ONVIF con una vera telecamera ONVIF, qualsiasi hardware Jetson, le rotte solari, elettriche, delle centrali d'allarme e del pannello touch con nodi "
                  'reali (si provano con messaggi generati: esiste solo la scheda radar) e il push tramite Firebase con un vero progetto Firebase.',
        'bullets': ["**Ingresso validato:** i messaggi HTTP e MQTT di ogni tipo di nodo (radar, solare, elettrico, centrale d'allarme, rete) sono controllati al confine "
                    'dal contratto condiviso prima di arrivare allo stato; un nodo può avere il proprio token (derivato da quello condiviso) e una modalità rigorosa non '
                    'accetta altro.',
                    '**Stato onesto dei nodi:** un nodo che smette di parlare appare *obsoleto* e *offline* dopo una finestra configurabile, mai online su dati vecchi; '
                    'uno che si riconnette è contato dal suo ritorno, non dai vecchi messaggi. Disinserire cancella subito un allarme alto.',
                    '**Gateway delle telecamere:** cassaforte cifrata delle telecamere, PTZ ONVIF / Hi3510 / PSIA, scoperta dei percorsi RTSP, un relay FFmpeg condiviso '
                    'per telecamera, istantanee e registrazione MP4, un guardiano che trasforma una telecamera muta in un evento e, a impianto inserito, in un allarme, '
                    "**zone dell'immagine da ignorare** e **foto e video fatti da soli** quando una telecamera vede qualcosa a impianto inserito.",
                    '**Libreria delle prove:** conservazione per età e dimensione, **prove protette** mai cancellate, un SHA-256 per la catena di custodia e un file di '
                    '**prova di custodia** firmato dal server. Una riga di audit per azione rilevante, con le credenziali rimosse.',
                    "**Stato che sopravvive:** la modalità di sicurezza e l'ultima osservazione di ogni nodo sono ripristinate dopo un riavvio (un riavvio non "
                    'disinserisce mai il perimetro in silenzio); i file sono scritti in modo atomico e uno danneggiato viene recuperato. Ogni cambio di allarme, nodo e '
                    'modalità è conservato in uno storico degli eventi.',
                    '**Allarmi:** un centro allarmi con ciclo generato / riconosciuto / chiuso, escalation di un allarme critico che attende senza essere visto, un '
                    '**controllo prima di inserire** (cosa è aperto, muto o fermo), un PIN per disinserire (e un PIN di coercizione) e allarmi da nodi, telecamere, '
                    "dispositivi, solare, elettrico, rete e centrali d'allarme. Arrivano a Studio, ai telefoni (ntfy, Telegram, Home Assistant, un webhook firmato, push "
                    'Firebase se lo configuri) e al topic MQTT `armor/server/alert`.',
                    '**Utenti e ruoli:** nomi e password (hash scrypt), un ruolo `admin` che gestisce gli utenti, un ruolo `operator` che opera e un ruolo `viewer` che '
                    "guarda soltanto; cambiare la password o il ruolo chiude le altre sessioni di quell'utente.",
                    '**Dispositivi e automazioni:** fumo, gas, allagamento, porta, finestra, movimento, clima, presa, luce, sirena, serratura, tapparella, cancello o '
                    'porta del garage e scaldabagno, via MQTT o push autenticato, con stato normalizzato, disponibilità e comandi; regole che azionano dispositivi '
                    'quando succede qualcosa (anche a soglia).',
                    '**Energia:** inverter e pacchi batteria (con ogni cella e le capacità) e nodi elettrici arrivano via HTTP o MQTT, sono validati dal contratto '
                    'condiviso, conservati con storico ed energia per giorno, segnati obsoleti se tacciono, e generano allarmi (guasto inverter, batteria scarica, rete '
                    'persa, tensione, guasto di commutazione…). Lo schema elettrico e le regole per commutare un circuito sono conservati sul server.',
                    "**Centrali d'allarme:** lo stato dei nodi ARMOR-NODE-ALARM, il **progetto dell'allarme** con le sue versioni, i **dispositivi Zigbee legati alle "
                    "zone** (il server dice a una centrale com'è una zona mentre tiene la radio) e comandi di inserimento / disinserimento a una centrale (spenti salvo "
                    '`ARMOR_ALARM_COMMANDS=1`).',
                    "**Rete locale:** ciò che riferisce il nodo ARMOR-NETWORK (dispositivi, internet, l'indirizzo pubblico e chi lo dà), ordini per il nodo (scansione, "
                    'ping, porte, ispezionare un dispositivo con un accesso che dai tu), nomi, dispositivi nascosti e sorvegliati, e accessi che viaggiano **sigillati '
                    'per il solo nodo**.',
                    '**Voce, osservazione e manutenzione:** comandi scritti e parlati (elenco chiuso, in otto lingue, con una conferma legata alla persona), il contesto '
                    'per il servizio di osservazione (quali radar coprono quale telecamera), il firmware dei nodi aggiornato da Studio uno alla volta con avanzamento, e '
                    "gli aggiornamenti dell'impianto da GitHub, quelli del sistema e una console root opzionale, tutto tramite l'assistente di manutenzione.",
                    "**Uso da fuori casa:** il server distingue la casa dall'esterno (una VPN conta come la casa), mantiene sessioni più brevi da fuori, chiede un "
                    "secondo fattore (un'app di autenticazione, con codici di recupero) e di nuovo la password prima delle azioni critiche, permette di scegliere cosa "
                    "può fare una sessione esterna (tutto, solo gestire l'allarme, solo guardare), avvisa le destinazioni degli allarmi quando qualcuno accede da un "
                    'luogo nuovo e apre il pannello web di un nodo tramite il server - vincolato al certificato del nodo, con il suo cookie tenuto sul server - così '
                    'nessun nodo viene mai pubblicato.',
                    "**Collegamento cifrato facoltativo con il broker (mqtts):** `ARMOR_MQTT_CA_FILE` indica il certificato dell'autorità propria dell'installazione; "
                    "con un indirizzo `mqtts://` il server si fida solo di quell'autorità e controlla il nome del broker, e si rifiuta di partire se il file non è un "
                    "certificato valido o l'indirizzo non è `mqtts://`. Studio mostra se il collegamento è cifrato e l'impronta dell'autorità. Provato contro un broker "
                    'TLS di prova e contro un vero Mosquitto 2.0.',
                    "**Salute dei nodi e modalità di inserimento:** conserva l'ultimo rapporto e il registro dei riavvii di ogni nodo e solleva quattro avvisi (poca "
                    'memoria, riavvii troppo frequenti, un broker che cade di continuo, segnale Wi-Fi debole); conserva i profili di inserimento (Fuori casa, In casa, '
                    'Notte e i tuoi) e mette quello scelto dentro il comando di inserimento, solo per un nodo che dice di capirli. Un allarme forte o discreto segue il '
                    'profilo; un inserimento senza profilo è il comando di sempre.',
                    '**Cronologia delle connessioni e del sistema:** oltre ad avvisi, nodi, telecamere, dispositivi e allarmi, la cronologia registra quali dispositivi '
                    'e app si collegano (sessioni di Studio, app Android, pannelli dei nodi, servizio vocale: accessi, rifiuti, uscite, sessioni scadute, uso del '
                    'secondo fattore, prima e ultima volta visti) e gli eventi del sistema (nodi che appaiono o scompaiono con il loro firmware, il collegamento con il '
                    'broker, impostazioni cambiate e da chi, servizi, aggiornamenti, inserimento con il suo profilo). Si filtra per tipo, categoria, client e utente; '
                    'indirizzo e user agent li vedono solo gli amministratori, e non si registra mai una password, un token, un cookie o un PIN.',
                    '**Ordini di scrittura su una batteria Pylontech (disattivati salvo `ARMOR_BATTERY_WRITE=1`):** per amministratori che hanno appena dimostrato di '
                    "nuovo chi sono - prepara, esegui con il numero di serie della batteria digitato di nuovo, annulla, rimetti un'uscita com'era, conserva un'immagine "
                    "firmware per un'ora - verificati con la tabella condivisa di operazioni e intervalli, inviati al nodo gateway come `solar_battery_command`, con "
                    'ogni operazione conservata (chi, quale batteria, cosa è stato letto prima e dopo, la differenza e la trascrizione, mai la password di servizio) e '
                    'riportata nello storico sotto *Batterie*.',
                    '**Controllo dei nodi:** `POST /api/v1/nodes/{id}/control` e `POST /api/v1/nodes/control` danno un ordine (riavvio, pausa, ripresa, standby, '
                    'identificazione, diagnostica, manutenzione attivata o disattivata) a un nodo o a tutti quelli che riferiscono, solo a un amministratore che si è '
                    'appena dimostrato di nuovo, con il nome del nodo (o la parola RESTART, PAUSE o STANDBY per tutti) digitato di nuovo dove la casa resterebbe meno '
                    "sorvegliata. Il server prepara l'ordine, lo esegue con il token monouso che il nodo dà per quell'operazione, segue ogni nodo (inviato, ricevuto, "
                    "applicato, tornato) in `GET /api/v1/nodes/control/operations`, riavvia le centrali d'allarme per ultime in un riavvio scaglionato, registra chi ha "
                    'ordinato cosa nello storico e nel registro di audit, e mostra nella salute del nodo se è in pausa, in standby (lavoro spento, resta connesso) o in '
                    'manutenzione. Non esistono ripristino di fabbrica, cancellazione né sonno profondo. È provato con un broker finto; non è stato provato su un nodo '
                    'reale.',
                    '**Stato in diretta e tabella delle rotte:** il server invia lo stato completo a Studio tramite un WebSocket su `/api/v1/events` ogni volta che '
                    'qualcosa cambia (una raffica di cambiamenti è un solo messaggio e un client che resta indietro viene scartato), e ogni rotta registrata, con chi '
                    'può chiamarla, è elencata in una tabella generata dal codice. Il pannello a muro ha un canale proprio, più piccolo, su `/api/v1/panel/events` (lo '
                    'stesso riepilogo di poche centinaia di byte di `GET /api/v1/panel/summary`, inviato quando cambia e ogni cinque secondi, per gli account pannello, '
                    'operatore e amministratore; un amministratore lo disattiva con `panel.live_events`).'],
        'intro': '**ARMOR-SERVER** è il centro di fiducia di A.R.M.O.R. I nodi di campo pubblicano osservazioni di radar, luce e salute; questo servizio le valida, '
                 "conserva l'ultimo stato noto di ogni nodo e lo serve alla console Studio e al client Android. Possiede anche tutto ciò che tocca una telecamera, così "
                 '**nessun browser né telefono detiene mai una password di telecamera o un indirizzo RTSP**.',
        'sections': [{'icon': '🔒',
                      'title': 'Modello di sicurezza',
                      'bullets': ['Segreti separati: **ingest** (i nodi pubblicano i loro messaggi; ogni nodo può avere anche un proprio token, derivato da quello '
                                  'condiviso, e una modalità rigorosa accetta solo quelli), **control** (inserire / disinserire, eventi), **operator** (automazione) e '
                                  'il **login di Studio**; ciascuno è confrontato in tempo costante e nessuno sostituisce un altro. Un accesso dato a un nodo di rete '
                                  'viaggia sigillato per quel solo nodo.',
                                  'Tre ruoli: **admin**, **operator** e **viewer** (legge, non cambia mai). Ogni rotta che configura, sposta, cattura, registra, '
                                  'protegge, cancella o inserisce richiede un operatore; il video dal vivo richiede un operatore o un ticket di flusso di breve durata '
                                  'legato a una telecamera. I comandi pericolosi (disinserire, commutare un circuito, la console root) chiedono un amministratore e, per '
                                  'disinserire, il PIN.',
                                  'Le password delle telecamere vivono solo in `data/cameras.json`, cifrate con AES-256-GCM, e nessuna API le restituisce; gli indirizzi '
                                  "ONVIF devono restare sull'host della telecamera e i reindirizzamenti sono rifiutati.",
                                  'Le sessioni di Studio sono HttpOnly e SameSite=Strict, il login ha un limite di tentativi e gli errori non portano mai una traccia di '
                                  'stack.',
                                  'Il server ascolta su 127.0.0.1 a meno che `ARMOR_HOST` sia impostato di proposito, e allora una password di Studio di meno di 12 '
                                  'caratteri è rifiutata.',
                                  'Da fuori casa: secondo fattore (TOTP, RFC 6238), una nuova prova di identità per utenti, firmware e pannelli dei nodi, una politica '
                                  "che riserva l'amministrazione alla casa o alla VPN, solo release di firmware firmate e un proxy dei pannelli dei nodi che non prende "
                                  'mai un indirizzo dalla richiesta, passa solo il necessario e rifiuta un nodo il cui certificato non è quello attendibile.']},
                     {'icon': '🌐',
                      'title': 'API',
                      'bullets': ['Pubblica: `GET /healthz`. Per un utente autenticato: stato, informazioni, telecamere, media, storico, regole, dispositivi, allarmi, '
                                  'automazioni, i progetti (sito, allarme, elettrico, rete), letture solari ed elettriche, la rete locale, notifiche e preferenze, e per '
                                  'un amministratore utenti, servizi, firmware, aggiornamenti e la console.',
                                  'Per i nodi: `POST /api/v1/telemetry`, `/health`, `/solar`, `/electrical/readings`, `/alarm/state`, `/network/state` e '
                                  '`/devices/state` con il token di ingest, e i topic MQTT `armor/node/#`, `armor/solar/#`, `armor/electrical/#`, `armor/alarm/#` e '
                                  '`armor/network/#`. Gli eventi raggiungono le console via WebSocket `/api/v1/events`.',
                                  'Ogni rotta (135 percorsi oggi), la sua regola di accesso e il suo schema sono nel file OpenAPI di '
                                  '[ARMOR-COMMON](https://github.com/JuanenRac/ARMOR-COMMON), e un test controlla che nessuna manchi.']},
                     {'icon': '⚙️',
                      'title': 'Configurazione',
                      'bullets': ['Copia `.env.example` in `.env` (ignorato da Git), oppure lascia che `run.bat` / `run.sh` generino segreti casuali al primo avvio.',
                                  'Obbligatori: `ARMOR_INGEST_TOKEN` e `ARMOR_CONTROL_TOKEN` (24 caratteri o più, tutti diversi) e `ARMOR_STUDIO_USERNAME` / '
                                  '`ARMOR_STUDIO_PASSWORD` (il primo amministratore).',
                                  'Comuni: `ARMOR_HOST` / `ARMOR_PORT`, `ARMOR_DATA_DIR`, `ARMOR_FFMPEG_PATH` (video dal vivo e cattura), `ARMOR_MQTT_URL`, '
                                  '`ARMOR_MQTT_CA_FILE`, `ARMOR_STUDIO_ORIGIN`, `ARMOR_NODE_STALE_AFTER_S`, `ARMOR_CAMERA_CHECK_S`, `ARMOR_ALERT_DWELL_MS`, '
                                  '`ARMOR_ALERT_WEBHOOK_URL` e `ARMOR_COOKIE_SECURE` (a `1` dietro TLS).',
                                  'Opzionali, tutti spenti per impostazione predefinita: `ARMOR_NTFY_URL`, `ARMOR_TELEGRAM_BOT_TOKEN`, `ARMOR_HOMEASSISTANT_URL`, '
                                  "`ARMOR_FCM_SERVICE_ACCOUNT` (push tramite il progetto Firebase dell'impianto stesso), `ARMOR_ALARM_COMMANDS=1` (lascia che il server "
                                  'inserisca e disinserisca le centrali), `ARMOR_ELECTRICAL_SWITCHING` e `ARMOR_INGEST_STRICT=1`.']}],
        'note': 'Per installare sul banco di prova CM5 (isolato da ogni altro progetto, con utente e porte proprie) vedi '
                '[ARMOR-DEVOPS](https://github.com/JuanenRac/ARMOR-DEVOPS).',
        'fit': "ARMOR-SERVER è l'unico centro di fiducia della famiglia. I nodi di campo ([ARMOR-NODE-RADAR](https://github.com/JuanenRac/ARMOR-NODE-RADAR), "
               '[ARMOR-NODE-SOLAR](https://github.com/JuanenRac/ARMOR-NODE-SOLAR), [ARMOR-NODE-ELECTRICAL](https://github.com/JuanenRac/ARMOR-NODE-ELECTRICAL), '
               '[ARMOR-NODE-ALARM](https://github.com/JuanenRac/ARMOR-NODE-ALARM), [ARMOR-NODE-HMI](https://github.com/JuanenRac/ARMOR-NODE-HMI)) e '
               '[ARMOR-NETWORK](https://github.com/JuanenRac/ARMOR-NETWORK) gli parlano via MQTT o HTTP; [ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) e '
               '[ARMOR-ANDROID-CONTROL](https://github.com/JuanenRac/ARMOR-ANDROID-CONTROL) lo leggono e gli danno ordini; '
               '[ARMOR-SERVER-AI](https://github.com/JuanenRac/ARMOR-SERVER-AI) pesa ciò che vedono le telecamere rispetto ai radar e si limita a raccomandare; '
               '[ARMOR-VOICE-AI](https://github.com/JuanenRac/ARMOR-VOICE-AI) trasforma la voce in un elenco chiuso di comandi; '
               "[ARMOR-DEVOPS](https://github.com/JuanenRac/ARMOR-DEVOPS) installa e aggiorna tutto sulla CM5. Il server decide: nient'altro inserisce, disinserisce o "
               'aziona qualcosa.',
        'hardware': "Il banco di prova CM5, in uso quotidiano: un vero broker MQTT, vere telecamere IP, un vero nodo radar su una scheda ESP32-S3, Studio, l'app Android "
                    'e i servizi di voce e osservazione contro di esso',
        'requirements': ['Node.js 22+', 'FFmpeg (video in diretta e cattura)', 'un broker MQTT (Mosquitto)']},
 'de': {'tagline': 'Zentraler Sicherheitskoordinator: Knoten, Alarme, Geräte, Energie, Kameras, das lokale Netz und die Wartung der Anlage',
        'status': {'software': 'Die Routen, Sitzungen, Verschlüsselung und Beweisregeln laufen täglich auf dem CM5-Prüfstand.',
                   'tests': '696 Tests bestehen (`npm test`), darunter eine vollständige HTTP-Integrationssuite gegen einen isolierten Server und eine Prüfung, dass '
                            'jede Route in der OpenAPI-Datei dokumentiert ist.',
                   'protocols': 'Die Radar-Nachrichten stammen von einer echten Platine; die Routen für Solar, Elektrik, Alarmzentrale und Touch-Panel sind mit '
                                'erzeugten Nachrichten getestet, und ONVIF ist keiner echten ONVIF-Kamera begegnet.',
                   'hardware': 'Er läuft auf dem CM5-Prüfstand mit einem echten MQTT-Broker, echten IP-Kameras (Live-Video, Standbilder, Aufnahmen, PTZ an den '
                               'Hi3510-Geräten) und einem echten Radar-Knoten; auf einem Jetson lief nichts.',
                   'security': 'Die Regeln für Sitzungen, Verschlüsselung, Beweise und Anmeldung sind durch Tests abgedeckt; es gab keine unabhängige Prüfung.',
                   'integration': 'Studio, die Android-App und die Sprach- und Beobachtungsdienste nutzen ihn täglich auf dem Prüfstand; Push über Firebase lief nie '
                                  'gegen ein echtes Firebase-Projekt.',
                   'docs': 'Acht Sprachen, die Routenreferenz (OpenAPI und ROUTES), die Anleitungen zu Umgebung und Fernzugriff und das Änderungsprotokoll sind '
                           'aktuell.'},
        'honest': 'Jede Route, Sitzung, Verschlüsselung und Beweisregel unten ist real und durch Tests abgedeckt (`npm test`: 696 Tests, darunter eine vollständige '
                  'HTTP-Integrationssuite gegen einen isolierten Server und eine Prüfung, dass jede Route in der OpenAPI-Datei dokumentiert ist). Er läuft im täglichen '
                  'Einsatz auf dem CM5-Testaufbau mit einem echten MQTT-Broker, der Firmware eines echten Radarknotens auf einer ESP32-S3-Platine, echten IP-Kameras '
                  '(Livevideo, Schnappschüsse, Aufnahmen, PTZ an den Hi3510-Geräten), der Studio-Konsole, der Android-App sowie den Sprach- und Beobachtungsdiensten. '
                  'Was **noch nicht** bewiesen ist: ONVIF mit einer echten ONVIF-Kamera, jegliche Jetson-Hardware, die Solar-, Elektro-, Alarmzentralen- und '
                  'Touchpanel-Routen mit echten Knoten (sie werden mit erzeugten Nachrichten getestet: nur die Radarplatine existiert) und Push über Firebase mit einem '
                  'echten Firebase-Projekt.',
        'bullets': ['**Geprüfter Eingang:** HTTP- und MQTT-Nachrichten jeder Knotenart (Radar, Solar, Elektro, Alarmzentrale, Netzwerk) werden an der Grenze vom '
                    'gemeinsamen Vertrag geprüft, bevor sie den Zustand erreichen; ein Knoten kann ein eigenes Token haben (vom gemeinsamen abgeleitet), und ein '
                    'strenger Modus akzeptiert nichts anderes.',
                    '**Ehrlicher Knotenzustand:** ein Knoten, der verstummt, wird nach einem einstellbaren Fenster als *veraltet* und *offline* angezeigt, nie als '
                    'online mit alten Daten; ein sich wieder verbindender wird ab seiner Rückkehr gezählt, nicht ab seinen alten Nachrichten. Unscharfschalten löscht '
                    'einen hohen Alarm sofort.',
                    '**Kamera-Gateway:** verschlüsselter Kamera-Tresor, PTZ per ONVIF / Hi3510 / PSIA, RTSP-Pfadsuche, ein gemeinsames FFmpeg-Relay pro Kamera, '
                    'Schnappschüsse und MP4-Aufnahme, ein Wächter, der eine stumme Kamera zu einem Ereignis und, wenn scharf, zu einem Alarm macht, **zu ignorierende '
                    'Bildzonen** und **von selbst gemachte Fotos und Videos**, wenn eine Kamera im scharfen Zustand etwas sieht.',
                    '**Beweisbibliothek:** Aufbewahrung nach Alter und Größe, **geschützte Beweise**, die nie gelöscht werden, ein SHA-256 für die Beweiskette und eine '
                    'vom Server signierte **Verwahrungsnachweis**-Datei. Eine Audit-Zeile pro sicherheitsrelevanter Aktion, mit entfernten Zugangsdaten.',
                    '**Zustand, der überlebt:** der Sicherheitsmodus und die letzte Beobachtung jedes Knotens werden nach einem Neustart wiederhergestellt (ein Neustart '
                    'schaltet den Perimeter nie stillschweigend unscharf); Dateien werden atomar geschrieben und eine beschädigte wird wiederhergestellt. Jede Alarm-, '
                    'Knoten- und Moduswechsel steht in einem Ereignisverlauf.',
                    '**Alarme:** eine Alarmzentrale mit Lebenslauf ausgelöst / quittiert / beendet, Eskalation eines kritischen Alarms, der ungesehen wartet, eine '
                    '**Prüfung vor dem Scharfschalten** (was offen, stumm oder ausgefallen ist), eine PIN zum Unscharfschalten (und eine Nötigungs-PIN) sowie Alarme von '
                    'Knoten, Kameras, Geräten, Solar, Elektro, Netzwerk und Alarmzentralen. Sie erreichen Studio, die Telefone (ntfy, Telegram, Home Assistant, einen '
                    'signierten Webhook, Firebase-Push bei Konfiguration) und das MQTT-Thema `armor/server/alert`.',
                    '**Benutzer und Rollen:** Namen und Passwörter (scrypt-Hashes), eine Rolle `admin`, die Benutzer verwaltet, eine Rolle `operator`, die bedient, und '
                    'eine Rolle `viewer`, die nur ansieht; ein geändertes Passwort oder eine geänderte Rolle beendet die anderen Sitzungen dieses Benutzers.',
                    '**Geräte und Automationen:** Rauch, Gas, Wasser, Tür, Fenster, Bewegung, Klima, Steckdose, Licht, Sirene, Schloss, Rollladen, Tor oder Garagentor '
                    'und Warmwasserbereiter über MQTT oder authentifizierten Push, mit normalisiertem Zustand, Verfügbarkeit und Befehlen; Regeln, die Geräte schalten, '
                    'wenn etwas geschieht (auch per Schwellwert).',
                    '**Energie:** Wechselrichter und Batteriestapel (mit jeder Zelle und den Kapazitäten) sowie Elektroknoten kommen per HTTP oder MQTT, werden vom '
                    'gemeinsamen Vertrag geprüft, mit Verlauf und Energie pro Tag gespeichert, bei Schweigen als veraltet markiert und lösen Alarme aus '
                    '(Wechselrichterfehler, Batterie schwach, Netz verloren, Spannung, Schaltfehler…). Der Elektroplan und die Regeln zum Schalten eines Stromkreises '
                    'liegen auf dem Server.',
                    '**Alarmzentralen:** der Zustand der ARMOR-NODE-ALARM-Knoten, der **Alarmplan** mit seinen Versionen, die **den Zonen zugeordneten Zigbee-Geräte** '
                    '(der Server sagt einer Zentrale, wie eine Zone ist, solange er das Funkmodul hält) und Scharf-/Unscharf-Befehle an eine Zentrale (aus, außer mit '
                    '`ARMOR_ALARM_COMMANDS=1`).',
                    '**Lokales Netz:** was der ARMOR-NETWORK-Knoten meldet (Geräte, Internet, die öffentliche Adresse und wer sie liefert), Aufträge für den Knoten '
                    '(Scan, Ping, Ports, ein Gerät mit einem von Ihnen gegebenen Login prüfen), Namen, versteckte und beobachtete Geräte sowie Zugangsdaten, die **nur '
                    'für den Knoten versiegelt** reisen.',
                    '**Sprache, Beobachtung und Wartung:** geschriebene und gesprochene Befehle (geschlossene Liste, in acht Sprachen, mit einer an die Person '
                    'gebundenen Bestätigung), der Kontext für den Beobachtungsdienst (welche Radare welche Kamera abdecken), die Firmware der Knoten, von Studio aus '
                    'nacheinander mit Fortschritt aktualisiert, sowie die Updates der Anlage selbst von GitHub, die des Systems und eine optionale Root-Konsole, alles '
                    'über den Wartungshelfer.',
                    '**Nutzung von außerhalb des Hauses:** Der Server unterscheidet das Haus vom Außen (ein VPN zählt als Haus), hält Sitzungen von außen kürzer, '
                    'verlangt einen zweiten Faktor (Authenticator-App, mit Wiederherstellungscodes) und vor kritischen Aktionen erneut das Passwort, lässt wählen, was '
                    'eine Sitzung von außen darf (alles, nur den Alarm bedienen, nur ansehen), meldet den Alarmzielen, wenn sich jemand von einem neuen Ort anmeldet, '
                    'und öffnet das Web-Panel eines Knotens über den Server - an das Zertifikat des Knotens gebunden, mit seinem Cookie auf dem Server -, sodass nie ein '
                    'Knoten veröffentlicht wird.',
                    '**Optionale verschlüsselte Verbindung zum Broker (mqtts):** `ARMOR_MQTT_CA_FILE` nennt das Zertifikat der eigenen Zertifizierungsstelle der Anlage; '
                    'bei einer `mqtts://`-Adresse vertraut der Server nur dieser Stelle und prüft den Namen des Brokers, und er startet nicht, wenn die Datei kein '
                    'gültiges Zertifikat ist oder die Adresse nicht `mqtts://` lautet. Studio zeigt, ob die Verbindung verschlüsselt ist, und den Fingerabdruck der '
                    'Stelle. Getestet gegen einen TLS-Broker-Ersatz und gegen einen echten Mosquitto 2.0.',
                    '**Zustand der Knoten und Scharfschaltmodi:** speichert den letzten Bericht und das Neustartprotokoll jedes Knotens und löst vier Warnungen aus '
                    '(wenig Speicher, zu häufige Neustarts, ein Broker, der immer wieder abreißt, schwaches WLAN-Signal); verwaltet die Scharfschaltprofile (Abwesend, '
                    'Zuhause, Nacht und eigene) und legt das gewählte in den Scharfschaltbefehl, nur für einen Knoten, der sie versteht. Ein lauter oder leiser Alarm '
                    'folgt dem Profil; ein Scharfschalten ohne Profil ist der Befehl wie immer.',
                    '**Verlauf der Verbindungen und des Systems:** Neben Warnungen, Knoten, Kameras, Geräten und Alarmen zeichnet der Verlauf auf, welche Geräte und '
                    'Apps sich verbinden (Studio-Sitzungen, die Android-App, die Panels der Knoten, der Sprachdienst: Anmeldungen, Ablehnungen, Abmeldungen, abgelaufene '
                    'Sitzungen, Nutzung des zweiten Faktors, erste und letzte Sichtung) und die Ereignisse des Systems (Knoten, die mit ihrer Firmware auftauchen oder '
                    'verschwinden, die Broker-Verbindung, geänderte Einstellungen und von wem, Dienste, Updates, Scharfschalten mit Profil). Filter nach Art, Kategorie, '
                    'Client und Benutzer; Adresse und User-Agent sehen nur Administratoren, und nie wird ein Passwort, Token, Cookie oder PIN aufgezeichnet.',
                    '**Befehle zum Schreiben auf eine Pylontech-Batterie (aus, außer mit `ARMOR_BATTERY_WRITE=1`):** für Administratoren, die sich eben erneut '
                    'ausgewiesen haben - vorbereiten, mit nochmals eingetippter Seriennummer der Batterie ausführen, abbrechen, einen Ausgang zurücksetzen, ein '
                    'Firmware-Image eine Stunde lang aufbewahren - geprüft an der gemeinsamen Tabelle der Operationen und Bereiche, als `solar_battery_command` an den '
                    'Gateway-Knoten gesendet; jede Operation wird festgehalten (wer, welche Batterie, was davor und danach gelesen wurde, der Unterschied und das '
                    'Protokoll, nie das Service-Passwort) und im Verlauf unter *Batterien* gemeldet.',
                    '**Steuerung der Knoten:** `POST /api/v1/nodes/{id}/control` und `POST /api/v1/nodes/control` erteilen einen Befehl (Neustart, Pause, Fortsetzen, '
                    'Standby, Identifizieren, Diagnose, Wartung ein oder aus) an einen Knoten oder an alle, die sich melden, nur für einen Administrator, der sich '
                    'gerade erneut ausgewiesen hat, wobei der Name des Knotens (oder das Wort RESTART, PAUSE oder STANDBY für alle) dort erneut getippt wird, wo das '
                    'Haus weniger bewacht wäre. Der Server bereitet den Befehl vor, führt ihn mit dem Einmal-Token aus, das der Knoten für diese Operation gibt, '
                    'verfolgt jeden Knoten (gesendet, bestätigt, angewendet, zurück) in `GET /api/v1/nodes/control/operations`, startet bei einem gestaffelten Neustart '
                    'die Alarmzentralen zuletzt neu, hält im Verlauf und im Audit-Protokoll fest, wer was befohlen hat, und zeigt Pause, Standby (Arbeit aus, bleibt '
                    'verbunden) und Wartung im Knotenzustand. Es gibt kein Zurücksetzen auf Werkseinstellungen, kein Löschen und keinen Tiefschlaf. Getestet mit einem '
                    'Schein-Broker; auf einem echten Knoten wurde es nicht ausprobiert.',
                    '**Live-Zustand und Routentabelle:** Der Server schickt den gesamten Zustand über einen WebSocket unter `/api/v1/events` an Studio, sobald sich '
                    'etwas ändert (eine Folge von Änderungen ist eine einzige Nachricht, ein zurückfallender Client wird fallen gelassen), und jede registrierte Route '
                    'mit der Angabe, wer sie aufrufen darf, steht in einer aus dem Code erzeugten Tabelle. Das Wandpanel hat einen eigenen, kleineren Kanal unter '
                    '`/api/v1/panel/events` (dieselbe Zusammenfassung von wenigen hundert Bytes wie `GET /api/v1/panel/summary`, gesendet bei Änderung und alle fünf '
                    'Sekunden, für die Konten Panel, Operator und Administrator; ein Administrator schaltet ihn mit `panel.live_events` ab).'],
        'intro': '**ARMOR-SERVER** ist das vertrauenswürdige Zentrum von A.R.M.O.R. Feldknoten veröffentlichen Radar-, Licht- und Zustandsbeobachtungen; dieser Dienst '
                 'validiert sie, hält den letzten bekannten Zustand jedes Knotens und stellt ihn der Studio-Konsole und dem Android-Client bereit. Er besitzt auch '
                 'alles, was eine Kamera berührt, sodass **kein Browser und kein Telefon je ein Kamerapasswort oder eine RTSP-Adresse hält**.',
        'sections': [{'icon': '🔒',
                      'title': 'Sicherheitsmodell',
                      'bullets': ['Getrennte Geheimnisse: **ingest** (die Knoten senden ihre Nachrichten; jeder Knoten kann außerdem ein eigenes, vom gemeinsamen '
                                  'abgeleitetes Token haben, und ein strenger Modus akzeptiert nur diese), **control** (scharf / unscharf, Ereignisse), **operator** '
                                  '(Automation) und das **Studio-Login**; jedes wird in konstanter Zeit verglichen, und keines ersetzt ein anderes. Ein einem '
                                  'Netzwerkknoten gegebener Login reist nur für diesen Knoten versiegelt.',
                                  'Drei Rollen: **admin**, **operator** und **viewer** (liest, ändert nie). Jede Route, die konfiguriert, bewegt, aufnimmt, aufzeichnet, '
                                  'schützt, löscht oder scharf schaltet, braucht einen Operator; Livevideo braucht einen Operator oder ein kurzlebiges Stream-Ticket für '
                                  'eine Kamera. Gefährliche Befehle (Unscharfschalten, einen Stromkreis schalten, die Root-Konsole) verlangen einen Administrator und '
                                  'zum Unscharfschalten die PIN.',
                                  'Kamerapasswörter liegen nur in `data/cameras.json`, mit AES-256-GCM verschlüsselt, und keine API gibt sie zurück; ONVIF-Adressen '
                                  'müssen auf dem Host der Kamera bleiben, und Weiterleitungen werden abgelehnt.',
                                  'Studio-Sitzungen sind HttpOnly und SameSite=Strict, das Login ist ratenbegrenzt, und Fehler tragen nie einen Stacktrace.',
                                  'Der Server lauscht auf 127.0.0.1, außer `ARMOR_HOST` wird absichtlich gesetzt; dann wird ein Studio-Passwort unter 12 Zeichen '
                                  'abgelehnt.',
                                  'Von außerhalb des Hauses: zweiter Faktor (TOTP, RFC 6238), ein neuer Identitätsnachweis für Benutzer, Firmware und Knoten-Panels, '
                                  'eine Richtlinie, die Verwaltung nur im Haus oder über das VPN erlaubt, nur signierte Firmware-Releases und ein Proxy für '
                                  'Knoten-Panels, der nie eine Adresse aus der Anfrage übernimmt, nur das Nötige weiterreicht und einen Knoten ablehnt, dessen '
                                  'Zertifikat nicht das vertrauenswürdige ist.']},
                     {'icon': '🌐',
                      'title': 'API',
                      'bullets': ['Öffentlich: `GET /healthz`. Für einen angemeldeten Benutzer: Status, Informationen, Kameras, Medien, Verlauf, Regeln, Geräte, Alarme, '
                                  'Automationen, die Pläne (Standort, Alarm, Elektro, Netzwerk), Solar- und Elektrowerte, das lokale Netz, Benachrichtigungen und '
                                  'Einstellungen und für einen Administrator Benutzer, Dienste, Firmware, Updates und die Konsole.',
                                  'Für die Knoten: `POST /api/v1/telemetry`, `/health`, `/solar`, `/electrical/readings`, `/alarm/state`, `/network/state` und '
                                  '`/devices/state` mit dem Ingest-Token sowie die MQTT-Themen `armor/node/#`, `armor/solar/#`, `armor/electrical/#`, `armor/alarm/#` '
                                  'und `armor/network/#`. Ereignisse erreichen die Konsolen über den WebSocket `/api/v1/events`.',
                                  'Jede Route (heute 135 Pfade), ihre Zugriffsregel und ihr Schema stehen in der OpenAPI-Datei von '
                                  '[ARMOR-COMMON](https://github.com/JuanenRac/ARMOR-COMMON), und ein Test prüft, dass keine fehlt.']},
                     {'icon': '⚙️',
                      'title': 'Konfiguration',
                      'bullets': ['Kopieren Sie `.env.example` nach `.env` (von Git ignoriert), oder lassen Sie `run.bat` / `run.sh` beim ersten Start zufällige '
                                  'Geheimnisse erzeugen.',
                                  'Erforderlich: `ARMOR_INGEST_TOKEN` und `ARMOR_CONTROL_TOKEN` (24 Zeichen oder mehr, alle verschieden) sowie `ARMOR_STUDIO_USERNAME` / '
                                  '`ARMOR_STUDIO_PASSWORD` (der erste Administrator).',
                                  'Üblich: `ARMOR_HOST` / `ARMOR_PORT`, `ARMOR_DATA_DIR`, `ARMOR_FFMPEG_PATH` (Livevideo und Aufnahme), `ARMOR_MQTT_URL`, '
                                  '`ARMOR_MQTT_CA_FILE`, `ARMOR_STUDIO_ORIGIN`, `ARMOR_NODE_STALE_AFTER_S`, `ARMOR_CAMERA_CHECK_S`, `ARMOR_ALERT_DWELL_MS`, '
                                  '`ARMOR_ALERT_WEBHOOK_URL` und `ARMOR_COOKIE_SECURE` (auf `1` hinter TLS).',
                                  'Optional, alle standardmäßig aus: `ARMOR_NTFY_URL`, `ARMOR_TELEGRAM_BOT_TOKEN`, `ARMOR_HOMEASSISTANT_URL`, '
                                  '`ARMOR_FCM_SERVICE_ACCOUNT` (Push über das eigene Firebase-Projekt der Anlage), `ARMOR_ALARM_COMMANDS=1` (lässt den Server '
                                  'Alarmzentralen scharf und unscharf schalten), `ARMOR_ELECTRICAL_SWITCHING` und `ARMOR_INGEST_STRICT=1`.']}],
        'note': 'Zur Installation auf dem CM5-Prüfstand (isoliert von jedem anderen Projekt, eigener Benutzer, eigene Ports) siehe '
                '[ARMOR-DEVOPS](https://github.com/JuanenRac/ARMOR-DEVOPS).',
        'fit': 'ARMOR-SERVER ist das eine vertrauenswürdige Zentrum der Familie. Die Feldknoten ([ARMOR-NODE-RADAR](https://github.com/JuanenRac/ARMOR-NODE-RADAR), '
               '[ARMOR-NODE-SOLAR](https://github.com/JuanenRac/ARMOR-NODE-SOLAR), [ARMOR-NODE-ELECTRICAL](https://github.com/JuanenRac/ARMOR-NODE-ELECTRICAL), '
               '[ARMOR-NODE-ALARM](https://github.com/JuanenRac/ARMOR-NODE-ALARM), [ARMOR-NODE-HMI](https://github.com/JuanenRac/ARMOR-NODE-HMI)) und '
               '[ARMOR-NETWORK](https://github.com/JuanenRac/ARMOR-NETWORK) sprechen per MQTT oder HTTP mit ihm; '
               '[ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) und [ARMOR-ANDROID-CONTROL](https://github.com/JuanenRac/ARMOR-ANDROID-CONTROL) lesen es und '
               'geben ihm Befehle; [ARMOR-SERVER-AI](https://github.com/JuanenRac/ARMOR-SERVER-AI) wägt ab, was die Kameras sehen, gegen die Radare und empfiehlt nur; '
               '[ARMOR-VOICE-AI](https://github.com/JuanenRac/ARMOR-VOICE-AI) macht aus Sprache eine geschlossene Liste von Befehlen; '
               '[ARMOR-DEVOPS](https://github.com/JuanenRac/ARMOR-DEVOPS) installiert und aktualisiert alles auf dem CM5. Der Server entscheidet: nichts sonst schaltet '
               'scharf, unscharf oder irgendetwas.',
        'hardware': 'Der CM5-Testaufbau im täglichen Einsatz: ein echter MQTT-Broker, echte IP-Kameras, ein echter Radarknoten auf einer ESP32-S3-Platine, Studio, die '
                    'Android-App und die Sprach- und Beobachtungsdienste daran',
        'requirements': ['Node.js 22+', 'FFmpeg (Live-Video und Aufnahme)', 'ein MQTT-Broker (Mosquitto)']},
 'zh': {'tagline': '中央安全协调器：节点、报警、设备、能源、摄像头、本地网络和系统维护',
        'status': {'software': '路由、会话、加密和证据规则每天都在 CM5 测试台上运行。',
                   'tests': '696 项测试通过（`npm test`），包括针对隔离服务器的完整 HTTP 集成测试，以及检查每条路由都已写入 OpenAPI 文件。',
                   'protocols': '雷达消息来自真实的板子；光伏、电气、报警面板和触摸面板的路由是用生成的消息测试的，ONVIF 也没有遇到过真正的 ONVIF 摄像头。',
                   'hardware': '它在 CM5 测试台上运行，配有真实的 MQTT 代理、真实的 IP 摄像头（实时视频、截图、录像、Hi3510 机型的云台）和真实的雷达节点；还没有在 Jetson 上运行过。',
                   'security': '会话、加密、证据和登录规则均有测试覆盖；没有经过独立审查。',
                   'integration': 'Studio、Android 应用以及语音和观察服务每天在测试台上使用它；通过 Firebase 的推送从未对真实的 Firebase 项目运行过。',
                   'docs': '八种语言、路由参考（OpenAPI 和 ROUTES）、环境与远程访问指南以及更新日志均为最新。'},
        'honest': '下面的每条路由、会话、加密和证据规则都是真实的，并有测试覆盖（`npm test`：696 个测试，包括针对隔离服务器的完整 HTTP 集成测试套件，以及检查每条路由都已写入 OpenAPI 文件）。它在 CM5 测试台上日常运行，配有真实的 MQTT 代理、ESP32-S3 '
                  '板上真实雷达节点的固件、真实的 IP 摄像头（实时视频、快照、录像、Hi3510 设备上的 PTZ）、Studio 控制台、Android 应用以及语音和观察服务。**尚未**证明的是：用真实 ONVIF 摄像头测试 ONVIF、任何 Jetson '
                  '硬件、用真实节点测试太阳能、电气、报警主机和触摸屏的路由（它们用生成的消息测试：目前只有雷达板存在），以及用真实 Firebase 项目测试 Firebase 推送。',
        'bullets': ['**经过验证的接入：**每种节点（雷达、太阳能、电气、报警主机、网络）的 HTTP 和 MQTT 消息在到达状态之前，都由共享契约在边界处检查；节点可以有自己的令牌（由共享令牌派生），严格模式则不接受其他令牌。',
                    '**诚实的节点状态：**停止通信的节点在可配置的时间窗口后显示为*过期*和*离线*，绝不会用旧数据显示为在线；重新连接的节点从其返回时开始计时，而不是从旧消息算起。撤防会立即清除高级警报。',
                    '**摄像头网关：**加密的摄像头保险库、ONVIF / Hi3510 / PSIA 云台、RTSP 路径发现、每个摄像头一个共享的 FFmpeg 中继、快照和 MP4 '
                    '录像、把沉默的摄像头变成事件（布防时变成报警）的看门狗、**要忽略的画面区域**，以及摄像头在布防时看到东西时**自动拍照和录像**。',
                    '**证据库：**按时间和大小保留、**永不清理的受保护证据**、用于保管链的 SHA-256，以及由服务器签名的**保管证明**文件。每个安全相关操作一条审计记录，凭据已被清除。',
                    '**可延续的状态：**安全模式和每个节点的最后观测在重启后恢复（重启绝不会悄悄撤防）；文件以原子方式写入，损坏的文件会被恢复。每次警报、节点和模式变化都保存在事件历史中。',
                    '**报警：**一个报警中心，生命周期为触发 / 确认 / 解除，无人查看的严重报警会升级，**布防前检查**（哪些是打开、沉默或故障的）、撤防 PIN（以及胁迫 PIN），以及来自节点、摄像头、设备、太阳能、电气、网络和报警主机的报警。它们会送达 '
                    'Studio、手机（ntfy、Telegram、Home Assistant、签名的 webhook、配置后的 Firebase 推送）以及 MQTT 主题 `armor/server/alert`。',
                    '**用户与角色：**用户名和密码（scrypt 哈希）、管理用户的 `admin` 角色、负责操作的 `operator` 角色，以及只看不改的 `viewer` 角色；更改密码或角色会终止该用户的其他会话。',
                    '**设备与自动化：**烟雾、燃气、漏水、门、窗、移动、气候、插座、灯、警笛、门锁、卷帘、大门或车库门和热水器设备，通过 MQTT 或经认证的推送接入，状态规范化，带可用性和命令；在发生事件时（包括阈值触发）切换设备的规则。',
                    '**能源：**逆变器和电池组（含每个电芯和容量）以及电气节点通过 HTTP 或 MQTT 到达，由共享契约验证，保存历史和每日能量，沉默时标记为过期，并触发报警（逆变器故障、电池电量低、电网丢失、电压、开关故障……）。电气设计和切换回路的规则保存在服务器上。',
                    '**报警主机：**ARMOR-NODE-ALARM 节点的状态、带版本的**报警设计**、**绑定到防区的 Zigbee 设备**（服务器持有无线电时，由它告诉主机某防区的状态），以及发给主机的布防 / 撤防命令（除非设置 `ARMOR_ALARM_COMMANDS=1`，否则关闭）。',
                    '**本地网络：**ARMOR-NETWORK 节点报告的内容（设备、互联网、公网地址及其来源）、给节点的指令（扫描、ping、端口、用你提供的登录信息检查设备）、名称、隐藏和监视的设备，以及**仅为该节点加密封装**后传输的登录信息。',
                    '**语音、观察与维护：**文字和语音命令（封闭列表，八种语言，确认与人绑定）、观察服务的上下文（哪些雷达覆盖哪个摄像头）、从 Studio 逐个更新并显示进度的节点固件，以及通过维护助手完成的、来自 GitHub 的系统自身更新、操作系统更新和可选的 root 控制台。',
                    '**从家外使用：**服务器区分家中和外部（VPN 视为家中），外部会话更短，要求第二重验证（验证器应用，附恢复码），并在关键操作前再次要求密码；可选择外部会话能做什么（全部、仅操作警报、仅查看）；有人从新地点登录时通知警报接收渠道；并通过服务器打开节点的网页面板（绑定节点证书，其 Cookie '
                    '保存在服务器上），因此永远不需要公开任何节点。',
                    '**可选的与代理加密连接(mqtts):** `ARMOR_MQTT_CA_FILE` 指向本安装自有证书颁发机构的证书;使用 `mqtts://` 地址时,服务器只信任该机构并检查代理名称;如果文件不是有效证书或地址不是 `mqtts://`,服务器拒绝启动。Studio '
                    '显示连接是否加密以及机构的指纹。已针对 TLS 代理替身和真实的 Mosquitto 2.0 测试。',
                    '**节点健康与布防模式：** 保存每个节点的最新报告和重启记录，并发出四种警告（内存不足、重启过于频繁、代理反复断开、Wi-Fi 信号弱）；保存布防配置（离家、在家、夜间和您自己的），并把所选配置放进布防命令，只发给声明支持它的节点。警报的强弱遵循配置；不带配置的布防仍是原来的命令。',
                    '**连接与系统历史：** 除警报、节点、摄像头、设备和报警外，历史还记录哪些设备和应用连接了服务器（Studio 会话、Android '
                    '应用、节点面板、语音服务：登录、被拒、退出、会话过期、第二重验证的使用、首次与最近出现），以及系统事件（带固件版本出现或消失的节点、代理连接、被更改的设置及操作人、服务、更新、含方案的布防）。可按类型、类别、客户端和用户筛选；地址和用户代理只显示给管理员，密码、令牌、Cookie 和 PIN '
                    '绝不会被记录。',
                    '**写入 Pylontech 电池的指令（除非设置 `ARMOR_BATTERY_WRITE=1`，否则关闭）：** 仅限刚刚再次证明身份的管理员——准备、再次输入电池序列号后执行、取消、把输出恢复原状、保存固件镜像一小时——依据共享的操作与范围表检查，以 '
                    '`solar_battery_command` 发给网关节点；每次操作都会保存（谁、哪块电池、操作前后读到的内容、差异和记录，绝不含服务密码），并在历史的“电池”类别中记录。',
                    '**节点控制：** `POST /api/v1/nodes/{id}/control` 和 `POST /api/v1/nodes/control` '
                    '向一个节点或所有在上报的节点下达一条命令（重启、暂停、恢复、待机、识别、诊断、开启或关闭维护），仅限刚刚再次验证过身份的管理员；在会让家中防护减弱的地方，还要再次输入节点名称（对所有节点则输入单词 RESTART、PAUSE 或 '
                    'STANDBY）。服务器先准备命令，再用节点为该操作给出的一次性令牌执行，在 `GET /api/v1/nodes/control/operations` '
                    '中跟踪每个节点（已发送、已确认、已应用、已恢复），滚动重启时把报警主机放在最后，在历史和审计记录中记下谁下达了什么命令，并在节点健康中显示暂停、待机（停止工作，保持连接）和维护。没有恢复出厂设置、擦除或深度睡眠。已用模拟代理测试；尚未在真实节点上试过。',
                    '**实时状态与路由表：** 每当有变化，服务器就通过 `/api/v1/events` 的 WebSocket 把完整状态推送给 Studio（一连串变化合并为一条消息，落后的客户端会被断开），并且它注册的每条路由及可调用者都列在由代码生成的表中。壁挂面板有自己更小的通道 '
                    '`/api/v1/panel/events`（与 `GET /api/v1/panel/summary` 相同的几百字节摘要，在变化时以及每五秒发送，面向面板、操作员和管理员账户；管理员可用 `panel.live_events` 将其关闭）。'],
        'intro': '**ARMOR-SERVER** 是 A.R.M.O.R. 的可信中心。现场节点发布雷达、光照和健康观测；本服务验证它们，保存每个节点最后已知的状态，并提供给 Studio 控制台和 Android 客户端。它还掌管一切接触摄像头的事务，因此**没有任何浏览器或手机持有摄像头密码或 RTSP '
                 '地址**。',
        'sections': [{'icon': '🔒',
                      'title': '安全模型',
                      'bullets': ['彼此独立的密钥：**ingest**（节点发送消息；每个节点也可以有自己的、由共享令牌派生的令牌，严格模式只接受这些）、**control**（布防 / 撤防、事件）、**operator**（自动化）和 **Studio '
                                  '登录**；每一种都以恒定时间比较，且互不替代。给网络节点的登录信息仅为该节点加密封装后传输。',
                                  '三种角色：**admin**、**operator** 和 **viewer**（只读，从不修改）。所有配置、移动、抓拍、录像、保护、删除或布防的路由都需要 operator；实时视频需要 operator '
                                  '或绑定到某个摄像头的短期流票据。危险命令（撤防、切换回路、root 控制台）需要管理员，撤防还需要 PIN。',
                                  '摄像头密码只保存在 `data/cameras.json` 中，使用 AES-256-GCM 加密，任何 API 都不会返回它们；ONVIF 地址必须停留在摄像头自身的主机上，重定向会被拒绝。',
                                  'Studio 会话为 HttpOnly 和 SameSite=Strict，登录有速率限制，错误从不携带堆栈跟踪。',
                                  '服务器默认只监听 127.0.0.1，除非有意设置 `ARMOR_HOST`；此时短于 12 个字符的 Studio 密码会被拒绝。',
                                  '从家外使用：第二重验证（TOTP，RFC 6238）、对用户、固件和节点面板的重新身份验证、仅限家中或 VPN 管理的策略、只接受已签名的固件版本，以及节点面板代理——它从不从请求中获取地址、只转发必要内容，并拒绝证书与受信任证书不一致的节点。']},
                     {'icon': '🌐',
                      'title': 'API',
                      'bullets': ['公开：`GET /healthz`。对已登录用户：状态、信息、摄像头、媒体、历史、规则、设备、报警、自动化、各类设计（场地、报警、电气、网络）、太阳能和电气读数、本地网络、通知和偏好设置；对管理员还有用户、服务、固件、更新和控制台。',
                                  '面向节点：使用 ingest 令牌的 `POST /api/v1/telemetry`、`/health`、`/solar`、`/electrical/readings`、`/alarm/state`、`/network/state` 和 '
                                  '`/devices/state`，以及 MQTT 主题 `armor/node/#`、`armor/solar/#`、`armor/electrical/#`、`armor/alarm/#` 和 `armor/network/#`。事件通过 WebSocket '
                                  '`/api/v1/events` 送达控制台。',
                                  '每条路由（目前 135 个路径）、其访问规则和模式都写在 [ARMOR-COMMON](https://github.com/JuanenRac/ARMOR-COMMON) 的 OpenAPI 文件中，并有测试检查没有遗漏。']},
                     {'icon': '⚙️',
                      'title': '配置',
                      'bullets': ['把 `.env.example` 复制为 `.env`（被 Git 忽略），或让 `run.bat` / `run.sh` 在首次运行时生成随机密钥。',
                                  '必填：`ARMOR_INGEST_TOKEN` 和 `ARMOR_CONTROL_TOKEN`（24 个字符以上，彼此不同），以及 `ARMOR_STUDIO_USERNAME` / `ARMOR_STUDIO_PASSWORD`（第一位管理员）。',
                                  '常用：`ARMOR_HOST` / '
                                  '`ARMOR_PORT`、`ARMOR_DATA_DIR`、`ARMOR_FFMPEG_PATH`（实时视频和抓拍）、`ARMOR_MQTT_URL`、`ARMOR_MQTT_CA_FILE`、`ARMOR_STUDIO_ORIGIN`、`ARMOR_NODE_STALE_AFTER_S`、`ARMOR_CAMERA_CHECK_S`、`ARMOR_ALERT_DWELL_MS`、`ARMOR_ALERT_WEBHOOK_URL` '
                                  '和 `ARMOR_COOKIE_SECURE`（在 TLS 之后设为 `1`）。',
                                  '可选，默认全部关闭：`ARMOR_NTFY_URL`、`ARMOR_TELEGRAM_BOT_TOKEN`、`ARMOR_HOMEASSISTANT_URL`、`ARMOR_FCM_SERVICE_ACCOUNT`（通过本系统自己的 Firebase '
                                  '项目推送）、`ARMOR_ALARM_COMMANDS=1`（让服务器对报警主机布防和撤防）、`ARMOR_ELECTRICAL_SWITCHING` 和 `ARMOR_INGEST_STRICT=1`。']}],
        'note': '要安装到 CM5 测试台（与其他项目隔离，使用独立用户和端口），参见 [ARMOR-DEVOPS](https://github.com/JuanenRac/ARMOR-DEVOPS)。',
        'fit': 'ARMOR-SERVER '
               '是整个家族唯一可信的中心。现场节点（[ARMOR-NODE-RADAR](https://github.com/JuanenRac/ARMOR-NODE-RADAR)、[ARMOR-NODE-SOLAR](https://github.com/JuanenRac/ARMOR-NODE-SOLAR)、[ARMOR-NODE-ELECTRICAL](https://github.com/JuanenRac/ARMOR-NODE-ELECTRICAL)、[ARMOR-NODE-ALARM](https://github.com/JuanenRac/ARMOR-NODE-ALARM)、[ARMOR-NODE-HMI](https://github.com/JuanenRac/ARMOR-NODE-HMI)）和 '
               '[ARMOR-NETWORK](https://github.com/JuanenRac/ARMOR-NETWORK) 通过 MQTT 或 HTTP 与它通信；[ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) 和 '
               '[ARMOR-ANDROID-CONTROL](https://github.com/JuanenRac/ARMOR-ANDROID-CONTROL) 读取它并向它下达命令；[ARMOR-SERVER-AI](https://github.com/JuanenRac/ARMOR-SERVER-AI) '
               '把摄像头看到的与雷达对照权衡，只给出建议；[ARMOR-VOICE-AI](https://github.com/JuanenRac/ARMOR-VOICE-AI) '
               '把语音变成封闭的命令列表；[ARMOR-DEVOPS](https://github.com/JuanenRac/ARMOR-DEVOPS) 在 CM5 上安装并更新这一切。由服务器做决定：其他任何东西都不能布防、撤防或切换任何设备。',
        'hardware': 'CM5 测试台的日常使用：真实的 MQTT 代理、真实的 IP 摄像头、ESP32-S3 板上的真实雷达节点，以及与之配合的 Studio、Android 应用和语音、观察服务',
        'requirements': ['Node.js 22+', 'FFmpeg（实时视频与抓取）', 'MQTT broker（Mosquitto）']},
 'ja': {'tagline': '中央セキュリティコーディネーター：ノード、警報、デバイス、エネルギー、カメラ、ローカルネットワーク、設備の保守',
        'status': {'software': 'ルート、セッション、暗号化、証拠の規則は、CM5 テストベンチで毎日使われています。',
                   'tests': '696 件のテストが通ります（`npm test`）。隔離したサーバーに対する HTTP 統合テスト一式と、すべてのルートが OpenAPI ファイルに記載されているかの確認を含みます。',
                   'protocols': 'レーダーのメッセージは実機のボードから来ています。太陽光・電気・警報パネル・タッチパネルのルートは生成したメッセージでテストしており、ONVIF は本物の ONVIF カメラと接続していません。',
                   'hardware': 'CM5 テストベンチで、実際の MQTT ブローカー、実際の IP カメラ（ライブ映像、スナップショット、録画、Hi3510 機の PTZ）、実際のレーダーノードとともに動作しています。Jetson ではまだ何も動かしていません。',
                   'security': 'セッション、暗号化、証拠、ログインの規則はテストでカバーされています。独立したレビューはありません。',
                   'integration': 'Studio、Android アプリ、音声・観察サービスがテストベンチで毎日使っています。Firebase 経由のプッシュは、本物の Firebase プロジェクトに対して一度も実行していません。',
                   'docs': '8 言語、ルートのリファレンス（OpenAPI と ROUTES）、環境とリモートアクセスのガイド、変更履歴は最新です。'},
        'honest': '以下のすべてのルート、セッション、暗号化、証拠のルールは実在し、テストでカバーされています（`npm test`：696 件。隔離したサーバーに対する完全な HTTP 統合テストと、すべてのルートが OpenAPI ファイルに記載されていることの確認を含む）。CM5 '
                  'テストベンチで日常的に動作しており、実際の MQTT ブローカー、ESP32-S3 基板上の実際のレーダーノードのファームウェア、実際の IP カメラ（ライブ映像、スナップショット、録画、Hi3510 機での PTZ）、Studio コンソール、Android '
                  'アプリ、音声・観察サービスと組み合わせています。**まだ**証明されていないもの：実際の ONVIF カメラでの ONVIF、Jetson ハードウェア全般、実ノードでのソーラー・電気・警報盤・タッチパネルのルート（生成したメッセージでテスト：存在するのはレーダー基板のみ）、実際の '
                  'Firebase プロジェクトでの Firebase プッシュ。',
        'bullets': ['**検証された受信：**あらゆる種類のノード（レーダー、ソーラー、電気、警報盤、ネットワーク）の HTTP・MQTT メッセージは、状態に届く前に共通のコントラクトで境界チェックされます。ノードは独自のトークン（共有トークンから導出）を持て、厳格モードではそれ以外を受け付けません。',
                    '**正直なノード状態：**通信が止まったノードは、設定可能な時間を過ぎると*古い*・*オフライン*と表示され、古いデータでオンラインと見せることはありません。再接続したノードは古いメッセージではなく復帰時点から数えます。警戒解除で高レベルの警報はすぐに消えます。',
                    '**カメラゲートウェイ：**暗号化したカメラの保管庫、ONVIF / Hi3510 / PSIA の PTZ、RTSP パスの探索、カメラごとに共有する FFmpeg リレー、スナップショットと MP4 '
                    '録画、無応答のカメラをイベント（警戒中は警報）にするウォッチドッグ、**無視する映像ゾーン**、警戒中にカメラが何かを捉えたとき**自動で撮る写真と動画**。',
                    '**証拠ライブラリ：**経過時間とサイズによる保持、決して削除されない**保護された証拠**、証拠保全用の SHA-256、サーバーが署名した**保管証明**ファイル。セキュリティ上重要な操作ごとに 1 行の監査記録（認証情報は除去）。',
                    '**再起動後も残る状態：**セキュリティモードと各ノードの最後の観測は再起動後に復元されます（再起動で黙って警戒解除されることはありません）。ファイルはアトミックに書き込まれ、壊れたファイルは復旧されます。警報、ノード、モードの変化はすべてイベント履歴に残ります。',
                    '**警報：**発生 / 確認 / 解除のライフサイクルを持つ警報センター、誰にも見られずに待つ重大警報のエスカレーション、**警戒前のチェック**（開いている、無応答、停止しているもの）、解除用 PIN（と強要時の '
                    'PIN）、そしてノード・カメラ・デバイス・ソーラー・電気・ネットワーク・警報盤からの警報。Studio、スマートフォン（ntfy、Telegram、Home Assistant、署名付き Webhook、設定すれば Firebase プッシュ）、MQTT トピック '
                    '`armor/server/alert` に届きます。',
                    '**ユーザーとロール：**名前とパスワード（scrypt ハッシュ）、ユーザーを管理する `admin`、操作する `operator`、閲覧だけの `viewer`。パスワードやロールを変えると、そのユーザーの他のセッションは終了します。',
                    '**デバイスとオートメーション：**煙、ガス、浸水、ドア、窓、動き、気候、プラグ、照明、サイレン、鍵、シャッター、門扉・ガレージドア、給湯器を MQTT '
                    'または認証付きプッシュで扱い、正規化した状態、可用性、コマンドを持ちます。何かが起きたときにデバイスを切り替えるルール（しきい値トリガーも）。',
                    '**エネルギー：**インバーターとバッテリースタック（各セルと容量を含む）、電気ノードが HTTP または MQTT '
                    'で届き、共通コントラクトで検証され、履歴と日ごとのエネルギーとともに保存され、無応答なら古い扱いになり、警報（インバーター故障、バッテリー残量低下、系統喪失、電圧、スイッチ故障など）を出します。電気設計と回路を切り替えるルールはサーバーに保存されます。',
                    '**警報盤：**ARMOR-NODE-ALARM ノードの状態、バージョン付きの**警報設計**、**ゾーンに結び付けた Zigbee デバイス**（サーバーが無線を持つ間、ゾーンの状態を警報盤に伝える）、警報盤への警戒・解除コマンド（`ARMOR_ALARM_COMMANDS=1` '
                    'でなければオフ）。',
                    '**ローカルネットワーク：**ARMOR-NETWORK '
                    'ノードの報告（デバイス、インターネット、公開アドレスとその提供元）、ノードへの指示（スキャン、ping、ポート、あなたが渡したログインでデバイスを調べる）、名前、非表示・監視デバイス、そして**そのノードだけに封印されて**届くログイン情報。',
                    '**音声、観察、保守：**文字と音声のコマンド（クローズドなリスト、8 言語、人に結び付いた確認）、観察サービス向けのコンテキスト（どのレーダーがどのカメラをカバーするか）、Studio から 1 台ずつ進捗付きで更新するノードのファームウェア、そして保守ヘルパー経由での GitHub '
                    'からの設備自身の更新、システムの更新、任意の root コンソール。',
                    '**家の外からの利用：**サーバーは家と外を区別し（VPN は家として扱う）、外からのセッションを短くし、2 '
                    '段階認証（認証アプリ、復旧コード付き）を求め、重要な操作の前にパスワードを再度求めます。外からのセッションに許す操作（すべて、アラームの操作のみ、閲覧のみ）を選べ、新しい場所からのサインインを警報の通知先に知らせ、ノードのウェブパネルをサーバー経由で開きます（ノードの証明書に固定し、Cookie '
                    'はサーバー側に保持）。ノードを公開することはありません。',
                    '**ブローカーとの暗号化接続(mqtts、任意):** `ARMOR_MQTT_CA_FILE` で設備独自の認証局の証明書を指定します。`mqtts://` のアドレスではその認証局だけを信頼してブローカーの名前を確認し、ファイルが有効な証明書でない場合やアドレスが `mqtts://` '
                    'でない場合は起動を拒否します。Studio は接続が暗号化されているかと認証局のフィンガープリントを表示します。TLS ブローカーの代役と実際の Mosquitto 2.0 で検証済みです。',
                    '**ノードの状態と警戒モード:** 各ノードの最新の報告と再起動の記録を保持し、4 つの警告（メモリ不足、再起動の多さ、ブローカーの頻繁な切断、Wi-Fi '
                    '信号の弱さ）を出します。警戒プロファイル（外出、在宅、夜間、独自のもの）を保持し、選ばれたものを、対応すると申告したノードにだけ警戒コマンドに入れて送ります。警報の強弱はプロファイルに従い、プロファイルなしの警戒はこれまでどおりのコマンドです。',
                    '**接続とシステムの履歴:** 警告・ノード・カメラ・デバイス・アラームに加えて、履歴は接続するデバイスとアプリ（Studio のセッション、Android '
                    'アプリ、ノードのパネル、音声サービス。サインイン、拒否、サインアウト、期限切れ、第二要素の使用、初回と最終確認）と、システムのイベント（ファームウェア付きで現れたり消えたりするノード、ブローカー接続、変更された設定とその実行者、サービス、更新、プロファイル付きの警戒操作）を記録します。種類・カテゴリ・クライアント・ユーザーで絞り込め、アドレスとユーザーエージェントは管理者にだけ表示され、パスワード・トークン・クッキー・PIN '
                    'は一切記録されません。',
                    '**Pylontechバッテリーへの書き込み命令（`ARMOR_BATTERY_WRITE=1` でなければ無効）：** '
                    '直前にあらためて本人確認をした管理者のみ——準備、バッテリーのシリアル番号を再入力して実行、取り消し、出力を元に戻す、ファームウェアイメージを1時間保持——を、共有の操作・範囲表で検査し、`solar_battery_command` '
                    'としてゲートウェイノードへ送ります。各操作（誰が、どのバッテリーに、前後に読み取った内容、差分、記録。サービスパスワードは含まない）は保存され、履歴の「バッテリー」に記録されます。',
                    '**ノードの制御：** `POST /api/v1/nodes/{id}/control` と `POST /api/v1/nodes/control` は、1 '
                    '台のノード、または報告しているすべてのノードに命令（再起動、一時停止、再開、スタンバイ、識別、診断、メンテナンスのオン／オフ）を出します。対象は、直前にもう一度本人確認をした管理者だけで、家の防護が弱まる操作ではノード名（全ノードの場合は RESTART、PAUSE、STANDBY '
                    'のいずれかの単語）を再入力します。サーバーは命令を準備し、そのノードがその操作のために渡す使い捨てトークンで実行し、`GET /api/v1/nodes/control/operations` '
                    'で各ノード（送信済み、受領、適用、復帰）を追跡します。順次再起動では警報パネルを最後にし、誰が何を命じたかを履歴と監査記録に残し、ノードの健全性に一時停止、スタンバイ（動作停止、接続は維持）、メンテナンスを表示します。工場出荷時リセット、消去、ディープスリープはありません。模擬ブローカーでテストしており、実機のノードでは試していません。',
                    '**ライブ状態とルート表：** サーバーは何かが変わるたびに、`/api/v1/events` の WebSocket で状態全体を Studio '
                    'に送ります（変化の連続は1通にまとめ、遅れたクライアントは切り離します）。登録されている全ルートと呼び出せる主体は、コードから生成した表に載っています。壁掛けパネルには専用の小さなチャンネル `/api/v1/panel/events` があります（`GET '
                    '/api/v1/panel/summary` と同じ数百バイトの要約を、変化したときと5秒ごとに、パネル・オペレーター・管理者アカウント向けに送ります。管理者は `panel.live_events` で無効にできます）。'],
        'intro': '**ARMOR-SERVER** は A.R.M.O.R. の信頼の中心です。フィールドノードがレーダー、光、ヘルスの観測を発行し、このサービスがそれを検証し、各ノードの最後に分かっている状態を保持して、Studio コンソールと Android '
                 'クライアントに提供します。カメラに触れるすべてもここが持つので、**ブラウザーもスマートフォンもカメラのパスワードや RTSP アドレスを持つことはありません**。',
        'sections': [{'icon': '🔒',
                      'title': 'セキュリティモデル',
                      'bullets': ['分離された秘密：**ingest**（ノードがメッセージを送る。各ノードは共有トークンから導出した独自トークンも持て、厳格モードではそれだけを受け付ける）、**control**（警戒 / '
                                  '解除、イベント）、**operator**（オートメーション）、**Studio ログイン**。それぞれ定数時間で比較され、互いに代用できません。ネットワークノードに渡したログインはそのノードだけに封印されて届きます。',
                                  '3 つのロール：**admin**、**operator**、**viewer**（読むだけで変更しない）。設定、移動、撮影、録画、保護、削除、警戒を行うルートは operator が必要。ライブ映像は operator か、1 '
                                  '台のカメラに結び付いた短命のストリームチケットが必要です。危険なコマンド（解除、回路の切り替え、root コンソール）は管理者を要求し、解除には PIN も必要です。',
                                  'カメラのパスワードは `data/cameras.json` にのみ AES-256-GCM で暗号化して保存され、どの API も返しません。ONVIF のアドレスはカメラ自身のホストにとどまる必要があり、リダイレクトは拒否されます。',
                                  'Studio のセッションは HttpOnly かつ SameSite=Strict、ログインにはレート制限があり、エラーにスタックトレースは含まれません。',
                                  'サーバーは、意図して `ARMOR_HOST` を設定しない限り 127.0.0.1 で待ち受け、設定した場合は 12 文字未満の Studio パスワードが拒否されます。',
                                  '家の外から：2 段階認証（TOTP、RFC 6238）、ユーザー・ファームウェア・ノードパネルでの再認証、管理を家または VPN '
                                  'に限るポリシー、署名済みファームウェアのみ、そしてリクエストからアドレスを受け取らず必要なものだけを通し、信頼した証明書と異なるノードを拒否するノードパネル用プロキシ。']},
                     {'icon': '🌐',
                      'title': 'API',
                      'bullets': ['公開：`GET '
                                  '/healthz`。ログイン済みユーザー向け：状態、情報、カメラ、メディア、履歴、ルール、デバイス、警報、オートメーション、各種設計（サイト、警報、電気、ネットワーク）、ソーラーと電気の測定値、ローカルネットワーク、通知と設定。管理者向けにはユーザー、サービス、ファームウェア、アップデート、コンソール。',
                                  'ノード向け：ingest トークン付きの `POST '
                                  '/api/v1/telemetry`、`/health`、`/solar`、`/electrical/readings`、`/alarm/state`、`/network/state`、`/devices/state`、および MQTT トピック '
                                  '`armor/node/#`、`armor/solar/#`、`armor/electrical/#`、`armor/alarm/#`、`armor/network/#`。イベントは WebSocket `/api/v1/events` でコンソールに届きます。',
                                  'すべてのルート（現在 135 パス）、そのアクセスルール、スキーマは [ARMOR-COMMON](https://github.com/JuanenRac/ARMOR-COMMON) の OpenAPI ファイルにあり、抜けがないことをテストが確認します。']},
                     {'icon': '⚙️',
                      'title': '設定',
                      'bullets': ['`.env.example` を `.env`（Git は無視）にコピーするか、`run.bat` / `run.sh` に初回実行時のランダムな秘密を生成させます。',
                                  '必須：`ARMOR_INGEST_TOKEN` と `ARMOR_CONTROL_TOKEN`（24 文字以上、すべて異なる）、および `ARMOR_STUDIO_USERNAME` / `ARMOR_STUDIO_PASSWORD`（最初の管理者）。',
                                  'よく使うもの：`ARMOR_HOST` / '
                                  '`ARMOR_PORT`、`ARMOR_DATA_DIR`、`ARMOR_FFMPEG_PATH`（ライブ映像と撮影）、`ARMOR_MQTT_URL`、`ARMOR_MQTT_CA_FILE`、`ARMOR_STUDIO_ORIGIN`、`ARMOR_NODE_STALE_AFTER_S`、`ARMOR_CAMERA_CHECK_S`、`ARMOR_ALERT_DWELL_MS`、`ARMOR_ALERT_WEBHOOK_URL`、`ARMOR_COOKIE_SECURE`（TLS '
                                  'の背後では `1`）。',
                                  '任意（すべて既定ではオフ）：`ARMOR_NTFY_URL`、`ARMOR_TELEGRAM_BOT_TOKEN`、`ARMOR_HOMEASSISTANT_URL`、`ARMOR_FCM_SERVICE_ACCOUNT`（設備自身の Firebase '
                                  'プロジェクト経由のプッシュ）、`ARMOR_ALARM_COMMANDS=1`（サーバーが警報盤を警戒・解除できるようにする）、`ARMOR_ELECTRICAL_SWITCHING`、`ARMOR_INGEST_STRICT=1`。']}],
        'note': 'CM5 テストベンチ（他のすべてのプロジェクトから隔離され、専用のユーザーとポートを持つ）へのインストールは [ARMOR-DEVOPS](https://github.com/JuanenRac/ARMOR-DEVOPS) を参照。',
        'fit': 'ARMOR-SERVER '
               'はファミリーで唯一の信頼できる中心です。フィールドノード（[ARMOR-NODE-RADAR](https://github.com/JuanenRac/ARMOR-NODE-RADAR)、[ARMOR-NODE-SOLAR](https://github.com/JuanenRac/ARMOR-NODE-SOLAR)、[ARMOR-NODE-ELECTRICAL](https://github.com/JuanenRac/ARMOR-NODE-ELECTRICAL)、[ARMOR-NODE-ALARM](https://github.com/JuanenRac/ARMOR-NODE-ALARM)、[ARMOR-NODE-HMI](https://github.com/JuanenRac/ARMOR-NODE-HMI)）と '
               '[ARMOR-NETWORK](https://github.com/JuanenRac/ARMOR-NETWORK) は MQTT または HTTP で話しかけ、[ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) と '
               '[ARMOR-ANDROID-CONTROL](https://github.com/JuanenRac/ARMOR-ANDROID-CONTROL) '
               'はこれを読み取って指示を出し、[ARMOR-SERVER-AI](https://github.com/JuanenRac/ARMOR-SERVER-AI) '
               'はカメラの映像をレーダーと照らし合わせて推奨するだけ、[ARMOR-VOICE-AI](https://github.com/JuanenRac/ARMOR-VOICE-AI) '
               'は音声を閉じたコマンドの一覧に変え、[ARMOR-DEVOPS](https://github.com/JuanenRac/ARMOR-DEVOPS) はそのすべてを CM5 にインストール・更新します。決めるのはサーバーで、他の何も警戒・解除・切り替えを行いません。',
        'hardware': 'CM5 テストベンチでの日常使用：実際の MQTT ブローカー、実際の IP カメラ、ESP32-S3 基板上の実際のレーダーノード、これに接続する Studio、Android アプリ、音声・観察サービス',
        'requirements': ['Node.js 22+', 'FFmpeg（ライブ映像とキャプチャ）', 'MQTT ブローカー（Mosquitto）']},
 'pt': {'tagline': 'Coordenador central de segurança: nós, alarmes, dispositivos, energia, câmaras, a rede local e a manutenção da instalação',
        'status': {'software': 'As rotas, as sessões, a cifragem e as regras de provas funcionam todos os dias na bancada de testes CM5.',
                   'tests': 'Passam 696 testes (`npm test`), incluindo uma bateria de integração HTTP completa contra um servidor isolado e uma verificação de que cada '
                            'rota está documentada no ficheiro OpenAPI.',
                   'protocols': 'As mensagens do radar vêm de uma placa real; as rotas solar, elétrica, de painel de alarme e de painel tátil são testadas com mensagens '
                                'geradas, e o ONVIF não encontrou uma câmara ONVIF real.',
                   'hardware': 'Funciona na bancada de testes CM5 com um broker MQTT real, câmaras IP reais (vídeo em direto, capturas, gravações, PTZ nas unidades '
                               'Hi3510) e um nó radar real; nada funcionou num Jetson.',
                   'security': 'As regras de sessões, cifragem, provas e acesso estão cobertas por testes; não houve revisão independente.',
                   'integration': 'O Studio, a app Android e os serviços de voz e observação usam-no todos os dias na bancada; o push através do Firebase nunca correu '
                                  'contra um projeto Firebase real.',
                   'docs': 'Oito idiomas, a referência das rotas (OpenAPI e ROUTES), os guias de ambiente e de acesso remoto e o registo de alterações estão '
                           'atualizados.'},
        'honest': 'Cada rota, sessão, cifra e regra de provas abaixo é real e está coberta por testes (`npm test`: 696 testes, incluindo um conjunto completo de '
                  'integração HTTP contra um servidor isolado e uma verificação de que cada rota está documentada no ficheiro OpenAPI). Funciona em uso diário na '
                  'bancada de testes do CM5 com um broker MQTT real, o firmware de um nó radar real numa placa ESP32-S3, câmaras IP reais (vídeo em direto, fotografias, '
                  'gravações, PTZ nas unidades Hi3510), a consola Studio, a aplicação Android e os serviços de voz e de observação. O que **ainda não** está provado: '
                  'ONVIF com uma câmara ONVIF real, qualquer hardware Jetson, as rotas solares, elétricas, de centrais de alarme e de painel tátil com nós reais '
                  '(testam-se com mensagens geradas: só existe a placa radar) e o push por Firebase com um projeto Firebase real.',
        'bullets': ['**Entrada validada:** as mensagens HTTP e MQTT de cada tipo de nó (radar, solar, elétrico, central de alarme, rede) são verificadas na fronteira '
                    'pelo contrato partilhado antes de chegarem ao estado; um nó pode ter o seu próprio token (derivado do partilhado) e um modo estrito não aceita mais '
                    'nada.',
                    '**Estado honesto dos nós:** um nó que deixa de falar aparece como *desatualizado* e *desligado* após uma janela configurável, nunca como ligado com '
                    'dados velhos; um que se volta a ligar conta desde o seu regresso, não desde as mensagens antigas. Desarmar limpa um alerta alto de imediato.',
                    '**Porta de ligação das câmaras:** cofre cifrado das câmaras, PTZ ONVIF / Hi3510 / PSIA, descoberta de caminhos RTSP, um relé FFmpeg partilhado por '
                    'câmara, fotografias e gravação MP4, um vigilante que transforma uma câmara muda num evento e, armado, num alarme, **zonas da imagem a ignorar** e '
                    '**fotografias e vídeo feitos sozinhos** quando uma câmara vê algo estando armado.',
                    '**Biblioteca de provas:** retenção por idade e tamanho, **provas protegidas** que nunca se apagam, um SHA-256 para a cadeia de custódia e um '
                    'ficheiro de **prova de custódia** assinado pelo servidor. Uma linha de auditoria por ação relevante, com as credenciais removidas.',
                    '**Estado que sobrevive:** o modo de segurança e a última observação de cada nó são restaurados após um reinício (um reinício nunca desarma o '
                    'perímetro em silêncio); os ficheiros são escritos de forma atómica e um danificado é recuperado. Cada mudança de alerta, nó e modo fica guardada '
                    'num histórico de eventos.',
                    '**Alarmes:** um centro de alarmes com ciclo gerado / reconhecido / terminado, escalada de um alarme crítico que espera sem ser visto, uma '
                    '**verificação antes de armar** (o que está aberto, mudo ou em baixo), um PIN para desarmar (e um PIN de coação) e alarmes de nós, câmaras, '
                    'dispositivos, solar, elétrico, rede e centrais de alarme. Chegam ao Studio, aos telemóveis (ntfy, Telegram, Home Assistant, um webhook assinado, '
                    'push por Firebase se o configurar) e ao tópico MQTT `armor/server/alert`.',
                    '**Utilizadores e papéis:** nomes e palavras-passe (hashes scrypt), um papel `admin` que gere utilizadores, um papel `operator` que opera e um papel '
                    '`viewer` que só observa; mudar a palavra-passe ou o papel termina as outras sessões desse utilizador.',
                    '**Dispositivos e automatizações:** fumo, gás, inundação, porta, janela, movimento, clima, tomada, luz, sirene, fechadura, estore, portão ou porta '
                    'de garagem e esquentador, por MQTT ou push autenticado, com estado normalizado, disponibilidade e comandos; regras que acionam dispositivos quando '
                    'algo acontece (também por limiares).',
                    '**Energia:** inversores e pilhas de baterias (com cada célula e as capacidades) e nós elétricos chegam por HTTP ou MQTT, são validados pelo '
                    'contrato partilhado, guardados com histórico e energia por dia, marcados como desatualizados se calarem, e geram alarmes (avaria do inversor, '
                    'bateria baixa, rede perdida, tensão, falha de comutação…). O desenho elétrico e as regras para comutar um circuito ficam no servidor.',
                    '**Centrais de alarme:** o estado dos nós ARMOR-NODE-ALARM, o **desenho do alarme** com as suas versões, os **dispositivos Zigbee ligados às zonas** '
                    '(o servidor diz a uma central como está uma zona enquanto tem o rádio) e comandos de armar / desarmar a uma central (desligados salvo '
                    '`ARMOR_ALARM_COMMANDS=1`).',
                    '**Rede local:** o que o nó ARMOR-NETWORK comunica (dispositivos, internet, o endereço público e quem o dá), ordens para o nó (varrimento, ping, '
                    'portas, inspecionar um dispositivo com um acesso que o utilizador dá), nomes, dispositivos ocultos e vigiados, e acessos que viajam **selados só '
                    'para o nó**.',
                    '**Voz, observação e manutenção:** comandos escritos e falados (lista fechada, em oito idiomas, com uma confirmação ligada à pessoa), o contexto '
                    'para o serviço de observação (que radares cobrem que câmara), o firmware dos nós atualizado a partir do Studio um a um com progresso, e as '
                    'atualizações da própria instalação a partir do GitHub, as do sistema e uma consola root opcional, tudo através do assistente de manutenção.',
                    '**Uso a partir de fora de casa:** o servidor distingue a casa do exterior (uma VPN conta como a casa), mantém sessões mais curtas a partir de fora, '
                    'pede um segundo fator (uma app autenticadora, com códigos de recuperação) e a palavra-passe outra vez antes das ações críticas, deixa escolher o '
                    'que uma sessão de fora pode fazer (tudo, só operar o alarme, só ver), avisa os destinos dos alarmes quando alguém entra de um sítio novo e abre o '
                    'painel web de um nó através do servidor - fixado ao certificado do nó e com o seu cookie guardado no servidor - para que nenhum nó seja alguma vez '
                    'publicado.',
                    '**Ligação cifrada opcional ao broker (mqtts):** `ARMOR_MQTT_CA_FILE` indica o certificado da autoridade própria da instalação; com um endereço '
                    '`mqtts://` o servidor confia só nessa autoridade e verifica o nome do broker, e recusa-se a arrancar se o ficheiro não for um certificado válido ou '
                    'o endereço não for `mqtts://`. O Studio mostra se a ligação está cifrada e a impressão digital da autoridade. Testado contra um broker TLS de teste '
                    'e contra um Mosquitto 2.0 real.',
                    '**Saúde dos nós e modos de armar:** guarda o último relatório e o registo de reinícios de cada nó e levanta quatro avisos (pouca memória, reinícios '
                    'demasiado frequentes, um broker que cai repetidamente, sinal Wi-Fi fraco); guarda os perfis de armar (Ausente, Em casa, Noite e os seus) e põe o '
                    'escolhido dentro do comando de armar, só para um nó que diz entendê-los. Um alarme forte ou discreto segue o perfil; um armar sem perfil é o '
                    'comando de sempre.',
                    '**Histórico das ligações e do sistema:** além dos alertas, nós, câmaras, dispositivos e alarmes, o histórico regista que dispositivos e aplicações '
                    'se ligam (sessões do Studio, a app Android, os painéis dos nós, o serviço de voz: inícios de sessão, recusas, saídas, sessões expiradas, uso do '
                    'segundo fator, primeira e última vez vistos) e os eventos do sistema (nós que aparecem ou desaparecem com o seu firmware, a ligação ao broker, '
                    'definições alteradas e por quem, serviços, atualizações, armar com o seu perfil). Filtra-se por tipo, categoria, cliente e utilizador; o endereço e '
                    'o agente de utilizador só os veem os administradores, e nunca se regista uma palavra-passe, um token, um cookie nem um PIN.',
                    '**Ordens para escrever numa bateria Pylontech (desligadas salvo `ARMOR_BATTERY_WRITE=1`):** para administradores que acabaram de provar de novo '
                    'quem são - preparar, executar com o número de série da bateria escrito outra vez, cancelar, repor uma saída como estava, guardar uma imagem de '
                    'firmware durante uma hora - verificadas com a tabela partilhada de operações e intervalos, enviadas ao nó gateway como `solar_battery_command`, com '
                    'cada operação guardada (quem, que bateria, o lido antes e depois, a diferença e a transcrição, nunca a palavra-passe de serviço) e registada no '
                    'histórico em *Baterias*.',
                    '**Controlo dos nós:** `POST /api/v1/nodes/{id}/control` e `POST /api/v1/nodes/control` dão uma ordem (reiniciar, pausar, retomar, pôr em espera, '
                    'identificar, diagnóstico, manutenção ligada ou desligada) a um nó ou a todos os que reportam, só a um administrador que acabou de provar quem é '
                    'outra vez, com o nome do nó (ou a palavra RESTART, PAUSE ou STANDBY para todos) escrito de novo onde a casa ficaria menos vigiada. O servidor '
                    'prepara a ordem, executa-a com o token de uso único que o nó dá para essa operação, segue cada nó (enviada, recebida, aplicada, de volta) em `GET '
                    '/api/v1/nodes/control/operations`, reinicia as centrais de alarme por último num reinício escalonado, regista quem ordenou o quê no histórico e na '
                    'auditoria, e mostra na saúde do nó se está em pausa, em espera (trabalho desligado, continua ligado) ou em manutenção. Não existe reposição de '
                    'fábrica, apagamento nem sono profundo. É testado com um broker simulado; não foi experimentado num nó real.',
                    '**Estado em direto e tabela de rotas:** o servidor envia o estado completo ao Studio por um WebSocket em `/api/v1/events` sempre que algo muda (uma '
                    'rajada de alterações é uma só mensagem e um cliente que fica para trás é descartado), e cada rota que regista, com quem a pode chamar, consta de '
                    'uma tabela gerada a partir do código. O painel de parede tem o seu próprio canal, mais pequeno, em `/api/v1/panel/events` (o mesmo resumo de umas '
                    'centenas de bytes de `GET /api/v1/panel/summary`, enviado quando muda e de cinco em cinco segundos, para as contas de painel, operador e '
                    'administrador; um administrador desliga-o com `panel.live_events`).'],
        'intro': 'O **ARMOR-SERVER** é o centro de confiança do A.R.M.O.R. Os nós de campo publicam observações de radar, luz e saúde; este serviço valida-as, guarda o '
                 'último estado conhecido de cada nó e serve esse estado à consola Studio e ao cliente Android. É também dono de tudo o que toca numa câmara, para que '
                 '**nenhum navegador nem telemóvel tenha alguma vez uma palavra-passe de câmara ou um endereço RTSP**.',
        'sections': [{'icon': '🔒',
                      'title': 'Modelo de segurança',
                      'bullets': ['Segredos separados: **ingest** (os nós publicam as suas mensagens; cada nó pode ter ainda o seu próprio token, derivado do '
                                  'partilhado, e um modo estrito aceita só esses), **control** (armar / desarmar, eventos), **operator** (automatização) e o **login do '
                                  'Studio**; cada um é comparado em tempo constante e nenhum substitui outro. Um acesso dado a um nó de rede viaja selado só para esse '
                                  'nó.',
                                  'Três papéis: **admin**, **operator** e **viewer** (lê, nunca altera). Cada rota que configura, move, captura, grava, protege, apaga '
                                  'ou arma exige um operador; o vídeo em direto exige um operador ou um bilhete de emissão de curta duração ligado a uma câmara. Os '
                                  'comandos perigosos (desarmar, comutar um circuito, a consola root) pedem um administrador e, para desarmar, o PIN.',
                                  'As palavras-passe das câmaras vivem só em `data/cameras.json`, cifradas com AES-256-GCM, e nenhuma API as devolve; os endereços ONVIF '
                                  'têm de ficar no anfitrião da câmara e os redirecionamentos são recusados.',
                                  'As sessões do Studio são HttpOnly e SameSite=Strict, o login tem limite de tentativas e os erros nunca levam um rasto de pilha.',
                                  'O servidor escuta em 127.0.0.1 salvo se `ARMOR_HOST` for definido de propósito, e então uma palavra-passe do Studio com menos de 12 '
                                  'caracteres é recusada.',
                                  'A partir de fora de casa: segundo fator (TOTP, RFC 6238), uma nova prova de identidade para utilizadores, firmware e painéis dos nós, '
                                  'uma política que reserva a administração para a casa ou a VPN, só releases de firmware assinadas e um proxy de painéis de nós que '
                                  'nunca toma um endereço do pedido, só passa o necessário e recusa um nó cujo certificado não seja o de confiança.']},
                     {'icon': '🌐',
                      'title': 'API',
                      'bullets': ['Pública: `GET /healthz`. Para um utilizador com sessão: estado, informação, câmaras, multimédia, histórico, regras, dispositivos, '
                                  'alarmes, automatizações, os desenhos (local, alarme, elétrico, rede), leituras solares e elétricas, a rede local, notificações e '
                                  'preferências, e para um administrador utilizadores, serviços, firmware, atualizações e a consola.',
                                  'Para os nós: `POST /api/v1/telemetry`, `/health`, `/solar`, `/electrical/readings`, `/alarm/state`, `/network/state` e '
                                  '`/devices/state` com o token de ingest, e os tópicos MQTT `armor/node/#`, `armor/solar/#`, `armor/electrical/#`, `armor/alarm/#` e '
                                  '`armor/network/#`. Os eventos chegam às consolas pelo WebSocket `/api/v1/events`.',
                                  'Cada rota (135 caminhos hoje), a sua regra de acesso e o seu esquema estão no ficheiro OpenAPI do '
                                  '[ARMOR-COMMON](https://github.com/JuanenRac/ARMOR-COMMON), e um teste verifica que nenhuma falta.']},
                     {'icon': '⚙️',
                      'title': 'Configuração',
                      'bullets': ['Copie `.env.example` para `.env` (ignorado pelo Git), ou deixe o `run.bat` / `run.sh` gerar segredos aleatórios na primeira execução.',
                                  'Obrigatórios: `ARMOR_INGEST_TOKEN` e `ARMOR_CONTROL_TOKEN` (24 caracteres ou mais, todos diferentes) e `ARMOR_STUDIO_USERNAME` / '
                                  '`ARMOR_STUDIO_PASSWORD` (o primeiro administrador).',
                                  'Habituais: `ARMOR_HOST` / `ARMOR_PORT`, `ARMOR_DATA_DIR`, `ARMOR_FFMPEG_PATH` (vídeo em direto e captura), `ARMOR_MQTT_URL`, '
                                  '`ARMOR_MQTT_CA_FILE`, `ARMOR_STUDIO_ORIGIN`, `ARMOR_NODE_STALE_AFTER_S`, `ARMOR_CAMERA_CHECK_S`, `ARMOR_ALERT_DWELL_MS`, '
                                  '`ARMOR_ALERT_WEBHOOK_URL` e `ARMOR_COOKIE_SECURE` (a `1` atrás de TLS).',
                                  'Opcionais, todos desligados por defeito: `ARMOR_NTFY_URL`, `ARMOR_TELEGRAM_BOT_TOKEN`, `ARMOR_HOMEASSISTANT_URL`, '
                                  '`ARMOR_FCM_SERVICE_ACCOUNT` (push pelo projeto Firebase da própria instalação), `ARMOR_ALARM_COMMANDS=1` (deixa o servidor armar e '
                                  'desarmar as centrais), `ARMOR_ELECTRICAL_SWITCHING` e `ARMOR_INGEST_STRICT=1`.']}],
        'note': 'Para instalar na bancada de testes CM5 (isolada de todos os outros projetos, utilizador próprio, portas próprias) veja o '
                '[ARMOR-DEVOPS](https://github.com/JuanenRac/ARMOR-DEVOPS).',
        'fit': 'O ARMOR-SERVER é o único centro de confiança da família. Os nós de campo ([ARMOR-NODE-RADAR](https://github.com/JuanenRac/ARMOR-NODE-RADAR), '
               '[ARMOR-NODE-SOLAR](https://github.com/JuanenRac/ARMOR-NODE-SOLAR), [ARMOR-NODE-ELECTRICAL](https://github.com/JuanenRac/ARMOR-NODE-ELECTRICAL), '
               '[ARMOR-NODE-ALARM](https://github.com/JuanenRac/ARMOR-NODE-ALARM), [ARMOR-NODE-HMI](https://github.com/JuanenRac/ARMOR-NODE-HMI)) e o '
               '[ARMOR-NETWORK](https://github.com/JuanenRac/ARMOR-NETWORK) falam com ele por MQTT ou HTTP; o [ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) '
               'e o [ARMOR-ANDROID-CONTROL](https://github.com/JuanenRac/ARMOR-ANDROID-CONTROL) leem-no e dão-lhe ordens; o '
               '[ARMOR-SERVER-AI](https://github.com/JuanenRac/ARMOR-SERVER-AI) pesa o que as câmaras veem face aos radares e só recomenda; o '
               '[ARMOR-VOICE-AI](https://github.com/JuanenRac/ARMOR-VOICE-AI) transforma a voz numa lista fechada de comandos; o '
               '[ARMOR-DEVOPS](https://github.com/JuanenRac/ARMOR-DEVOPS) instala e atualiza tudo isso no CM5. O servidor decide: mais nada arma, desarma ou aciona o '
               'que quer que seja.',
        'hardware': 'A bancada de testes do CM5, em uso diário: um broker MQTT real, câmaras IP reais, um nó radar real numa placa ESP32-S3, o Studio, a aplicação '
                    'Android e os serviços de voz e observação contra ele',
        'requirements': ['Node.js 22+', 'FFmpeg (vídeo em direto e captura)', 'um broker MQTT (Mosquitto)']}}

# the text tree of docs/structure.json (make_structure.py --tree <language>); the repository's own check fails when it and the file disagree
TREE = {'de': 'ARMOR-SERVER/\n'
       '├── src/\n'
       '│   ├── server.ts app.ts              Start, Express-App, Ratenbegrenzung\n'
       '│   ├── config.ts                     jede Einstellung, beim Start geprüft\n'
       '│   ├── contracts.ts mqtt_router.ts   Prüfung an der Grenze\n'
       '│   ├── store.ts persistence.ts       Knotenzustand und was einen Neustart übersteht\n'
       '│   ├── alarms.ts escalation.ts       Alarmzentrale und Eskalation\n'
       '│   ├── users.ts totp.ts              Benutzer, Rollen, PIN und zweiter Faktor\n'
       '│   ├── security_settings.ts          die 17 Schalter aus Studio\n'
       '│   ├── voice.ts voice_turn.ts        geschriebene und gesprochene Befehle\n'
       '│   ├── firmware.ts installation.ts   Knoten-Firmware und eigene Updates\n'
       '│   ├── http/                         Sitzungen, Knoten-Tokens, versiegelte Logins\n'
       '│   ├── routes/                       eine Datei je Routengruppe\n'
       '│   ├── cameras/                      Tresor, PTZ, RTSP, Suche, Zustand\n'
       '│   ├── media/                        FFmpeg-Relais und Beweisbibliothek\n'
       '│   └── devices/                      Gerätemodell und MQTT-Brücke\n'
       '├── tests/                            755 Tests, Unit und HTTP-Integration\n'
       '├── docs/                             7 Leitfäden, Routentabelle, Umgebung\n'
       '├── tools/                            Generatoren für docs/ROUTES.md und docs/ENVIRONMENT.md, gemeinsame CI-Prüfungen, Starter\n'
       '├── images/                           Banner, Symbol und die Bilder des READMEs\n'
       '├── .github/                          CI-Workflow, Dashboard-Hinweis, Vorlagen für Issues und Pull Requests\n'
       '├── Dockerfile                        Container-Image des Servers\n'
       '├── armor.project.json                Manifest: Version, Rolle, Reife\n'
       '├── CHANGELOG.md                      was sich in jeder Version geändert hat\n'
       '├── package.json package-lock.json    Abhängigkeiten und Skripte\n'
       '├── tsconfig.json                     TypeScript-Einstellungen\n'
       '├── run.sh run.bat                    Start, gemeinsamer Ablauf\n'
       '├── build.sh build.bat                Bauen und Testen, gemeinsamer Ablauf\n'
       '├── build-test.sh build-test.bat      Bauen, Testen und Verpacken\n'
       '├── test.sh test.bat                  nur die Tests, nie die Version\n'
       '└── SECURITY.md SUPPORT.md CONTRIBUTING.md CODE_OF_CONDUCT.md LICENSE',
 'en': 'ARMOR-SERVER/\n'
       '├── src/\n'
       '│   ├── server.ts app.ts              start-up, Express app, rate limits\n'
       '│   ├── config.ts                     every setting, checked at start-up\n'
       '│   ├── contracts.ts mqtt_router.ts   validation at the boundary\n'
       '│   ├── store.ts persistence.ts       node state and what survives a restart\n'
       '│   ├── alarms.ts escalation.ts       alarm centre and escalation\n'
       '│   ├── users.ts totp.ts              users, roles, PIN and second factor\n'
       '│   ├── security_settings.ts          the 17 switches Studio changes\n'
       '│   ├── voice.ts voice_turn.ts        written and spoken commands\n'
       '│   ├── firmware.ts installation.ts   node firmware and own updates\n'
       '│   ├── http/                         sessions, per-node tokens, sealed logins\n'
       '│   ├── routes/                       one file per group of routes\n'
       '│   ├── cameras/                      vault, PTZ, RTSP, discovery, health\n'
       '│   ├── media/                        FFmpeg relay and evidence library\n'
       '│   └── devices/                      device model and its MQTT bridge\n'
       '├── tests/                            755 tests, unit and HTTP integration\n'
       '├── docs/                             7 guides, route table, environment\n'
       '├── tools/                            generators of docs/ROUTES.md and docs/ENVIRONMENT.md, shared CI checks, launcher\n'
       '├── images/                           banner, icon and the pictures of the README\n'
       '├── .github/                          CI workflow, dashboard notice, issue and pull-request templates\n'
       '├── Dockerfile                        container image of the server\n'
       '├── armor.project.json                manifest: version, role, maturity\n'
       '├── CHANGELOG.md                      what changed in each version\n'
       '├── package.json package-lock.json    dependencies and scripts\n'
       '├── tsconfig.json                     TypeScript settings\n'
       '├── run.sh run.bat                    start, shared workflow\n'
       '├── build.sh build.bat                build and test, shared workflow\n'
       '├── build-test.sh build-test.bat      build, test and package\n'
       '├── test.sh test.bat                  only the tests, never the version\n'
       '└── SECURITY.md SUPPORT.md CONTRIBUTING.md CODE_OF_CONDUCT.md LICENSE',
 'es': 'ARMOR-SERVER/\n'
       '├── src/\n'
       '│   ├── server.ts app.ts              arranque, aplicación Express, límites\n'
       '│   ├── config.ts                     cada ajuste, comprobado al arrancar\n'
       '│   ├── contracts.ts mqtt_router.ts   validación en el borde\n'
       '│   ├── store.ts persistence.ts       estado de nodos y lo que sobrevive a un reinicio\n'
       '│   ├── alarms.ts escalation.ts       centro de alarmas y escalado\n'
       '│   ├── users.ts totp.ts              usuarios, roles, PIN y segundo factor\n'
       '│   ├── security_settings.ts          los 17 interruptores de Studio\n'
       '│   ├── voice.ts voice_turn.ts        órdenes escritas y habladas\n'
       '│   ├── firmware.ts installation.ts   firmware de nodos y actualizaciones propias\n'
       '│   ├── http/                         sesiones, tokens por nodo, accesos sellados\n'
       '│   ├── routes/                       un fichero por grupo de rutas\n'
       '│   ├── cameras/                      caja fuerte, PTZ, RTSP, descubrimiento, salud\n'
       '│   ├── media/                        relé FFmpeg y biblioteca de evidencias\n'
       '│   └── devices/                      modelo de dispositivos y su puente MQTT\n'
       '├── tests/                            755 pruebas, unitarias e integración HTTP\n'
       '├── docs/                             7 guías, tabla de rutas, entorno\n'
       '├── tools/                            generadores de docs/ROUTES.md y docs/ENVIRONMENT.md, comprobaciones de CI, lanzador\n'
       '├── images/                           banner, icono y las imágenes del README\n'
       '├── .github/                          flujo de CI, aviso al panel, plantillas de incidencias y pull requests\n'
       '├── Dockerfile                        imagen de contenedor del servidor\n'
       '├── armor.project.json                manifiesto: versión, función, madurez\n'
       '├── CHANGELOG.md                      qué cambió en cada versión\n'
       '├── package.json package-lock.json    dependencias y scripts\n'
       '├── tsconfig.json                     ajustes de TypeScript\n'
       '├── run.sh run.bat                    arrancar, flujo compartido\n'
       '├── build.sh build.bat                construir y probar, flujo compartido\n'
       '├── build-test.sh build-test.bat      construir, probar y empaquetar\n'
       '├── test.sh test.bat                  solo las pruebas, nunca la versión\n'
       '└── SECURITY.md SUPPORT.md CONTRIBUTING.md CODE_OF_CONDUCT.md LICENSE',
 'fr': 'ARMOR-SERVER/\n'
       '├── src/\n'
       '│   ├── server.ts app.ts              démarrage, application Express, limites\n'
       '│   ├── config.ts                     chaque réglage, vérifié au démarrage\n'
       '│   ├── contracts.ts mqtt_router.ts   validation à la frontière\n'
       '│   ├── store.ts persistence.ts       état des nœuds et ce qui survit à un redémarrage\n'
       "│   ├── alarms.ts escalation.ts       centrale d'alarme et escalade\n"
       '│   ├── users.ts totp.ts              utilisateurs, rôles, PIN et second facteur\n'
       '│   ├── security_settings.ts          les 17 interrupteurs de Studio\n'
       '│   ├── voice.ts voice_turn.ts        commandes écrites et vocales\n'
       '│   ├── firmware.ts installation.ts   firmware des nœuds et mises à jour propres\n'
       '│   ├── http/                         sessions, jetons par nœud, identifiants scellés\n'
       '│   ├── routes/                       un fichier par groupe de routes\n'
       '│   ├── cameras/                      coffre, PTZ, RTSP, découverte, santé\n'
       '│   ├── media/                        relais FFmpeg et bibliothèque de preuves\n'
       "│   └── devices/                      modèle d'appareils et son pont MQTT\n"
       '├── tests/                            755 tests, unitaires et intégration HTTP\n'
       '├── docs/                             7 guides, table des routes, environnement\n'
       '├── tools/                            générateurs de docs/ROUTES.md et docs/ENVIRONMENT.md, vérifications CI, lanceur\n'
       '├── images/                           bannière, icône et images du README\n'
       "├── .github/                          workflow CI, avis au tableau de bord, modèles d'issues et de pull requests\n"
       '├── Dockerfile                        image de conteneur du serveur\n'
       '├── armor.project.json                manifeste : version, rôle, maturité\n'
       '├── CHANGELOG.md                      ce qui a changé à chaque version\n'
       '├── package.json package-lock.json    dépendances et scripts\n'
       '├── tsconfig.json                     réglages TypeScript\n'
       '├── run.sh run.bat                    démarrer, flux partagé\n'
       '├── build.sh build.bat                construire et tester, flux partagé\n'
       '├── build-test.sh build-test.bat      construire, tester, empaqueter\n'
       '├── test.sh test.bat                  seulement les tests, jamais la version\n'
       '└── SECURITY.md SUPPORT.md CONTRIBUTING.md CODE_OF_CONDUCT.md LICENSE',
 'it': 'ARMOR-SERVER/\n'
       '├── src/\n'
       '│   ├── server.ts app.ts              avvio, app Express, limiti\n'
       "│   ├── config.ts                     ogni impostazione, verificata all'avvio\n"
       '│   ├── contracts.ts mqtt_router.ts   validazione al confine\n'
       '│   ├── store.ts persistence.ts       stato dei nodi e ciò che sopravvive a un riavvio\n'
       '│   ├── alarms.ts escalation.ts       centrale allarmi ed escalation\n'
       '│   ├── users.ts totp.ts              utenti, ruoli, PIN e secondo fattore\n'
       '│   ├── security_settings.ts          i 17 interruttori di Studio\n'
       '│   ├── voice.ts voice_turn.ts        comandi scritti e vocali\n'
       '│   ├── firmware.ts installation.ts   firmware dei nodi e aggiornamenti propri\n'
       '│   ├── http/                         sessioni, token per nodo, accessi sigillati\n'
       '│   ├── routes/                       un file per gruppo di rotte\n'
       '│   ├── cameras/                      cassaforte, PTZ, RTSP, scoperta, salute\n'
       '│   ├── media/                        relè FFmpeg e libreria di prove\n'
       '│   └── devices/                      modello dei dispositivi e ponte MQTT\n'
       '├── tests/                            755 test, unitari e integrazione HTTP\n'
       '├── docs/                             7 guide, tabella delle rotte, ambiente\n'
       '├── tools/                            generatori di docs/ROUTES.md e docs/ENVIRONMENT.md, controlli CI, avviatore\n'
       '├── images/                           banner, icona e immagini del README\n'
       '├── .github/                          workflow CI, avviso alla dashboard, modelli per issue e pull request\n'
       '├── Dockerfile                        immagine container del server\n'
       '├── armor.project.json                manifesto: versione, ruolo, maturità\n'
       '├── CHANGELOG.md                      cosa è cambiato in ogni versione\n'
       '├── package.json package-lock.json    dipendenze e script\n'
       '├── tsconfig.json                     impostazioni TypeScript\n'
       '├── run.sh run.bat                    avvio, flusso condiviso\n'
       '├── build.sh build.bat                compila e prova, flusso condiviso\n'
       '├── build-test.sh build-test.bat      compila, prova e impacchetta\n'
       '├── test.sh test.bat                  solo i test, mai la versione\n'
       '└── SECURITY.md SUPPORT.md CONTRIBUTING.md CODE_OF_CONDUCT.md LICENSE',
 'ja': 'ARMOR-SERVER/\n'
       '├── src/\n'
       '│   ├── server.ts app.ts              起動、Express アプリ、レート制限\n'
       '│   ├── config.ts                     全設定を起動時に検証\n'
       '│   ├── contracts.ts mqtt_router.ts   境界での検証\n'
       '│   ├── store.ts persistence.ts       ノード状態と再起動後も残るもの\n'
       '│   ├── alarms.ts escalation.ts       アラームセンターとエスカレーション\n'
       '│   ├── users.ts totp.ts              ユーザー、ロール、PIN、2 要素\n'
       '│   ├── security_settings.ts          Studio で変える 17 のスイッチ\n'
       '│   ├── voice.ts voice_turn.ts        文字と音声のコマンド\n'
       '│   ├── firmware.ts installation.ts   ノードのファームウェアと自己更新\n'
       '│   ├── http/                         セッション、ノード別トークン、封印した認証情報\n'
       '│   ├── routes/                       ルート群ごとに 1 ファイル\n'
       '│   ├── cameras/                      金庫、PTZ、RTSP、探索、健全性\n'
       '│   ├── media/                        FFmpeg 中継と証拠ライブラリ\n'
       '│   └── devices/                      デバイスモデルと MQTT ブリッジ\n'
       '├── tests/                            755 件（単体と HTTP 結合）\n'
       '├── docs/                             7 つのガイド、ルート表、環境変数\n'
       '├── tools/                            docs/ROUTES.md と docs/ENVIRONMENT.md の生成、CI 検査、ランチャー\n'
       '├── images/                           バナー、アイコン、README の画像\n'
       '├── .github/                          CI ワークフロー、ダッシュボード通知、Issue と Pull Request のテンプレート\n'
       '├── Dockerfile                        サーバーのコンテナイメージ\n'
       '├── armor.project.json                マニフェスト：版・役割・成熟度\n'
       '├── CHANGELOG.md                      各バージョンの変更点\n'
       '├── package.json package-lock.json    依存関係とスクリプト\n'
       '├── tsconfig.json                     TypeScript 設定\n'
       '├── run.sh run.bat                    起動（共通フロー）\n'
       '├── build.sh build.bat                ビルドとテスト（共通フロー）\n'
       '├── build-test.sh build-test.bat      ビルド、テスト、パッケージ化\n'
       '├── test.sh test.bat                  テストのみ（版は変えません）\n'
       '└── SECURITY.md SUPPORT.md CONTRIBUTING.md CODE_OF_CONDUCT.md LICENSE',
 'pt': 'ARMOR-SERVER/\n'
       '├── src/\n'
       '│   ├── server.ts app.ts              arranque, aplicação Express, limites\n'
       '│   ├── config.ts                     cada definição, verificada no arranque\n'
       '│   ├── contracts.ts mqtt_router.ts   validação na fronteira\n'
       '│   ├── store.ts persistence.ts       estado dos nós e o que sobrevive a um reinício\n'
       '│   ├── alarms.ts escalation.ts       central de alarmes e escalada\n'
       '│   ├── users.ts totp.ts              utilizadores, funções, PIN e segundo fator\n'
       '│   ├── security_settings.ts          os 17 interruptores do Studio\n'
       '│   ├── voice.ts voice_turn.ts        ordens escritas e faladas\n'
       '│   ├── firmware.ts installation.ts   firmware dos nós e atualizações próprias\n'
       '│   ├── http/                         sessões, tokens por nó, credenciais seladas\n'
       '│   ├── routes/                       um ficheiro por grupo de rotas\n'
       '│   ├── cameras/                      cofre, PTZ, RTSP, descoberta, saúde\n'
       '│   ├── media/                        relé FFmpeg e biblioteca de provas\n'
       '│   └── devices/                      modelo de dispositivos e a sua ponte MQTT\n'
       '├── tests/                            755 testes, unitários e integração HTTP\n'
       '├── docs/                             7 guias, tabela de rotas, ambiente\n'
       '├── tools/                            geradores de docs/ROUTES.md e docs/ENVIRONMENT.md, verificações de CI, lançador\n'
       '├── images/                           faixa, ícone e as imagens do README\n'
       '├── .github/                          fluxo de CI, aviso ao painel, modelos de issues e pull requests\n'
       '├── Dockerfile                        imagem de contentor do servidor\n'
       '├── armor.project.json                manifesto: versão, função, maturidade\n'
       '├── CHANGELOG.md                      o que mudou em cada versão\n'
       '├── package.json package-lock.json    dependências e scripts\n'
       '├── tsconfig.json                     definições do TypeScript\n'
       '├── run.sh run.bat                    arrancar, fluxo partilhado\n'
       '├── build.sh build.bat                compilar e testar, fluxo partilhado\n'
       '├── build-test.sh build-test.bat      compilar, testar e empacotar\n'
       '├── test.sh test.bat                  só os testes, nunca a versão\n'
       '└── SECURITY.md SUPPORT.md CONTRIBUTING.md CODE_OF_CONDUCT.md LICENSE',
 'zh': 'ARMOR-SERVER/\n'
       '├── src/\n'
       '│   ├── server.ts app.ts              启动、Express 应用、限流\n'
       '│   ├── config.ts                     启动时校验每项设置\n'
       '│   ├── contracts.ts mqtt_router.ts   边界处的校验\n'
       '│   ├── store.ts persistence.ts       节点状态与重启后保留的内容\n'
       '│   ├── alarms.ts escalation.ts       报警中心与升级\n'
       '│   ├── users.ts totp.ts              用户、角色、PIN 与第二因素\n'
       '│   ├── security_settings.ts          Studio 修改的 17 个开关\n'
       '│   ├── voice.ts voice_turn.ts        文字和语音命令\n'
       '│   ├── firmware.ts installation.ts   节点固件与自身更新\n'
       '│   ├── http/                         会话、节点令牌、密封凭据\n'
       '│   ├── routes/                       每组路由一个文件\n'
       '│   ├── cameras/                      保险库、PTZ、RTSP、发现、健康\n'
       '│   ├── media/                        FFmpeg 中继与证据库\n'
       '│   └── devices/                      设备模型及其 MQTT 桥\n'
       '├── tests/                            755 项测试（单元与 HTTP 集成）\n'
       '├── docs/                             7 份指南、路由表、环境变量\n'
       '├── tools/                            docs/ROUTES.md 和 docs/ENVIRONMENT.md 的生成器、CI 检查、启动器\n'
       '├── images/                           横幅图、图标和 README 的图片\n'
       '├── .github/                          CI 工作流、仪表板通知、议题和 pull request 模板\n'
       '├── Dockerfile                        服务器容器镜像\n'
       '├── armor.project.json                清单：版本、角色、成熟度\n'
       '├── CHANGELOG.md                      每个版本的变化\n'
       '├── package.json package-lock.json    依赖与脚本\n'
       '├── tsconfig.json                     TypeScript 设置\n'
       '├── run.sh run.bat                    启动（共用流程）\n'
       '├── build.sh build.bat                构建并测试（共用流程）\n'
       '├── build-test.sh build-test.bat      构建、测试并打包\n'
       '├── test.sh test.bat                  只运行测试，不改版本\n'
       '└── SECURITY.md SUPPORT.md CONTRIBUTING.md CODE_OF_CONDUCT.md LICENSE'}

DIAGRAM = 'flowchart LR\n    N["Field nodes (ESP32-S3)"] -->|MQTT / HTTP + ingest token| S["ARMOR-SERVER"]\n    G["Solar gateway nodes"] -->|MQTT / HTTP + ingest token| S\n    E["Electrical nodes"] -->|MQTT / HTTP + ingest token| S\n    C["IP cameras"] -->|RTSP / ONVIF| S\n    S -->|"MJPEG, JSON, WebSocket"| U["ARMOR-STUDIO"]\n    S -->|"MJPEG, JSON"| A["ARMOR-ANDROID-CONTROL"]\n    S --> D[("data/: cameras.json (AES-GCM), media/, audit.log")]'

NEW_BULLETS = {
    'en': ['**Old readings set aside:** a channel of an electrical node whose own reading is over a minute old (its meter stopped answering and the node repeats the last good numbers) is left out of the grid figure and the graphs, listed in `stale_channels` of the node and counted in `totals.stale_readings`; the option `electrical.set_aside_old_readings` (on by default) turns it off.', "**The sign-in limit of a node and the right image for the right board:** an administrator reads and changes the wrong passwords per minute a node lets through (`POST /api/v1/admin/nodes/settings`, the panel login used once and never kept), and a firmware image whose file name says another board than the node's is refused with `wrong_board` before anything is sent."],
    'es': ['**Lecturas viejas apartadas:** un canal de un nodo eléctrico cuya propia lectura tiene más de un minuto (su contador dejó de responder y el nodo repite los últimos números buenos) queda fuera de la cifra de la red y de las gráficas, se lista en `stale_channels` del nodo y se cuenta en `totals.stale_readings`; la opción `electrical.set_aside_old_readings` (activada por defecto) lo desactiva.', '**El límite de acceso de un nodo y la imagen correcta para cada placa:** un administrador lee y cambia las contraseñas erróneas por minuto que deja pasar un nodo (`POST /api/v1/admin/nodes/settings`, con el acceso al panel usado una vez y nunca guardado), y una imagen de firmware cuyo nombre de fichero dice otra placa distinta de la del nodo se rechaza con `wrong_board` antes de enviar nada.'],
    'de': ['**Alte Messwerte beiseitegelegt:** Ein Kanal eines Elektro-Knotens, dessen eigener Messwert über eine Minute alt ist (sein Zähler antwortet nicht mehr und der Knoten wiederholt die letzten guten Zahlen), bleibt aus der Netzzahl und den Diagrammen heraus, wird in `stale_channels` des Knotens aufgeführt und in `totals.stale_readings` gezählt; die Option `electrical.set_aside_old_readings` (standardmäßig an) schaltet das ab.', '**Das Anmeldelimit eines Knotens und das richtige Image für die richtige Platine:** Ein Administrator liest und ändert die falschen Passwörter pro Minute, die ein Knoten durchlässt (`POST /api/v1/admin/nodes/settings`, die Panel-Anmeldung einmal benutzt und nie gespeichert), und ein Firmware-Image, dessen Dateiname eine andere Platine als die des Knotens nennt, wird mit `wrong_board` abgelehnt, bevor etwas gesendet wird.'],
    'fr': ["**Lectures anciennes mises de côté :** un canal d'un nœud électrique dont la propre lecture a plus d'une minute (son compteur ne répond plus et le nœud répète les derniers bons chiffres) reste hors du chiffre du réseau et des graphiques, est listé dans `stale_channels` du nœud et compté dans `totals.stale_readings` ; l'option `electrical.set_aside_old_readings` (activée par défaut) le désactive.", "**La limite de connexion d'un nœud et la bonne image pour la bonne carte :** un administrateur lit et change les mots de passe erronés par minute qu'un nœud laisse passer (`POST /api/v1/admin/nodes/settings`, l'identifiant du panneau utilisé une fois et jamais conservé), et une image de firmware dont le nom de fichier indique une autre carte que celle du nœud est refusée avec `wrong_board` avant que rien ne soit envoyé."],
    'it': ["**Letture vecchie messe da parte:** un canale di un nodo elettrico la cui lettura ha più di un minuto (il suo contatore ha smesso di rispondere e il nodo ripete gli ultimi numeri buoni) resta fuori dalla cifra della rete e dai grafici, è elencato in `stale_channels` del nodo e contato in `totals.stale_readings`; l'opzione `electrical.set_aside_old_readings` (attiva per default) lo disattiva.", "**Il limite di accesso di un nodo e l'immagine giusta per la scheda giusta:** un amministratore legge e cambia le password errate al minuto che un nodo lascia passare (`POST /api/v1/admin/nodes/settings`, con l'accesso al pannello usato una volta e mai conservato), e un'immagine firmware il cui nome di file indica una scheda diversa da quella del nodo viene rifiutata con `wrong_board` prima di inviare qualsiasi cosa."],
    'ja': ['**古い読み取り値は除外:** 電気ノードのチャンネルで、自身の読み取りが 1 分以上古いもの（メーターが応答しなくなり、ノードが最後の正常な値を繰り返している状態）は、系統の数値とグラフから外され、ノードの `stale_channels` に並び、`totals.stale_readings` に数えられます。オプション `electrical.set_aside_old_readings`（既定でオン）でオフにできます。', '**ノードのログイン上限と、ボードに合ったイメージ:** 管理者は、ノードが許す 1 分あたりの誤パスワード数を読み取り・変更できます（`POST /api/v1/admin/nodes/settings`。パネルのログイン情報は 1 回だけ使われ保存されません）。ファイル名がノードのボードと異なるボードを示すファームウェアイメージは、何も送る前に `wrong_board` で拒否されます。'],
    'zh': ['**搁置过旧的读数:** 电气节点中自身读数已超过一分钟的通道(其电表不再应答,节点只是重复最后一次正常的数值)不再计入电网数字和图表,列在节点的 `stale_channels` 中,并计入 `totals.stale_readings`;选项 `electrical.set_aside_old_readings`(默认开启)可将其关闭。', '**节点的登录限制与对应开发板的镜像:** 管理员可以读取和修改节点每分钟放行的错误密码次数(`POST /api/v1/admin/nodes/settings`,面板登录信息只使用一次、绝不保存);文件名所示开发板与节点开发板不同的固件镜像会在发送任何内容之前被 `wrong_board` 拒绝。'],
    'pt': ['**Leituras antigas postas de parte:** um canal de um nó elétrico cuja própria leitura tem mais de um minuto (o seu contador deixou de responder e o nó repete os últimos números bons) fica fora do valor da rede e dos gráficos, é listado em `stale_channels` do nó e contado em `totals.stale_readings`; a opção `electrical.set_aside_old_readings` (ativa por predefinição) desativa-o.', '**O limite de início de sessão de um nó e a imagem certa para a placa certa:** um administrador lê e altera as palavras-passe erradas por minuto que um nó deixa passar (`POST /api/v1/admin/nodes/settings`, com o acesso ao painel usado uma vez e nunca guardado), e uma imagem de firmware cujo nome de ficheiro indica outra placa que não a do nó é recusada com `wrong_board` antes de ser enviado o que quer que seja.'],
}
for _lg in NEW_BULLETS:
    LEGACY[_lg]["bullets"] = list(LEGACY[_lg]["bullets"]) + NEW_BULLETS[_lg]

NT = "755"
FACTS["badges"] = [x for x in FACTS["badges"] if x[0] != "Tests"] + [["Tests", NT + "%20passing", "2ea44f"]]


def fix(s):
    return s.replace("696", NT).replace("135", "195")


def L(lg, key):
    v = LEGACY[lg][key]
    return fix(v) if isinstance(v, str) else [fix(x) for x in v]


def sec(lg, i):
    return [fix(b) for b in LEGACY[lg]["sections"][i]["bullets"]]


GLANCE = [
    (GL["role"], T("Central security coordinator of the family: nodes, alarms, devices, energy, cameras, network | Coordinador central de seguridad de la familia: nodos, alarmas, dispositivos, energía, cámaras, red | Zentraler Sicherheitskoordinator der Familie: Knoten, Alarme, Geräte, Energie, Kameras, Netzwerk | Coordinateur central de sécurité de la famille : nœuds, alarmes, appareils, énergie, caméras, réseau | Coordinatore centrale di sicurezza della famiglia: nodi, allarmi, dispositivi, energia, telecamere, rete | ファミリーの中央セキュリティコーディネーター：ノード、アラーム、デバイス、エネルギー、カメラ、ネットワーク | 家族的中央安全协调器：节点、报警、设备、能源、摄像头、网络 | Coordenador central de segurança da família: nós, alarmes, dispositivos, energia, câmaras, rede")),
    (GL["stack"], "Node.js 22+, TypeScript, Express 5, MQTT, WebSocket, FFmpeg"),
    (GL["tests"], T("NTESTS (`npm test`: unit and full HTTP integration) | NTESTS (`npm test`: unitarias e integración HTTP completa) | NTESTS (`npm test`: Unit und volle HTTP-Integration) | NTESTS (`npm test` : unitaires et intégration HTTP complète) | NTESTS (`npm test`: unitari e integrazione HTTP completa) | NTESTS 件（`npm test`：単体と完全な HTTP 結合） | NTESTS 项（`npm test`：单元与完整 HTTP 集成） | NTESTS (`npm test`: unitários e integração HTTP completa)".replace("NTESTS", NT))),
    (GL["contract"], T("195 HTTP paths, 253 operations (OpenAPI in ARMOR-COMMON), route table in `docs/ROUTES.md` | 195 rutas HTTP, 253 operaciones (OpenAPI en ARMOR-COMMON), tabla de rutas en `docs/ROUTES.md` | 195 HTTP-Pfade, 253 Operationen (OpenAPI in ARMOR-COMMON), Routentabelle in `docs/ROUTES.md` | 195 chemins HTTP, 253 opérations (OpenAPI dans ARMOR-COMMON), table des routes dans `docs/ROUTES.md` | 195 percorsi HTTP, 253 operazioni (OpenAPI in ARMOR-COMMON), tabella delle rotte in `docs/ROUTES.md` | HTTP パス 195 本、253 操作（OpenAPI は ARMOR-COMMON）、ルート表は `docs/ROUTES.md` | 195 条 HTTP 路径、253 个操作（OpenAPI 在 ARMOR-COMMON 中），路由表见 `docs/ROUTES.md` | 195 caminhos HTTP, 253 operações (OpenAPI no ARMOR-COMMON), tabela de rotas em `docs/ROUTES.md`")),
    (GL["listens"], T("`127.0.0.1:8080` (`ARMOR_HOST`, `ARMOR_PORT`) | `127.0.0.1:8080` (`ARMOR_HOST`, `ARMOR_PORT`) | `127.0.0.1:8080` (`ARMOR_HOST`, `ARMOR_PORT`) | `127.0.0.1:8080` (`ARMOR_HOST`, `ARMOR_PORT`) | `127.0.0.1:8080` (`ARMOR_HOST`, `ARMOR_PORT`) | `127.0.0.1:8080`（`ARMOR_HOST`、`ARMOR_PORT`） | `127.0.0.1:8080`（`ARMOR_HOST`、`ARMOR_PORT`） | `127.0.0.1:8080` (`ARMOR_HOST`, `ARMOR_PORT`)")),
    (GL["runs"], T("The CM5 test bench (as a service, see ARMOR-DEVOPS) or any computer with Node.js | El banco de la CM5 (como servicio, ver ARMOR-DEVOPS) o cualquier ordenador con Node.js | Der CM5-Prüfstand (als Dienst, siehe ARMOR-DEVOPS) oder jeder Computer mit Node.js | Le banc d'essai CM5 (en service, voir ARMOR-DEVOPS) ou tout ordinateur avec Node.js | Il banco di prova CM5 (come servizio, vedi ARMOR-DEVOPS) o qualsiasi computer con Node.js | CM5 テストベンチ（サービスとして。ARMOR-DEVOPS 参照）または Node.js のある任意のコンピューター | CM5 测试台（作为服务，见 ARMOR-DEVOPS）或任何装有 Node.js 的计算机 | A bancada do CM5 (como serviço, ver ARMOR-DEVOPS) ou qualquer computador com Node.js")),
    (GL["hardware"], LEGACY["en"]["hardware"] and {lg: LEGACY[lg]["hardware"] for lg in LGS}),
    (GL["license"], LICENSE_VALUE),
]

ROLE_TABLE = [
    ("ARMOR-NODE-RADAR, SOLAR, ELECTRICAL, ALARM, HMI", T("MQTT `armor/*/#` or HTTP `POST` with the ingest token | MQTT `armor/*/#` o HTTP `POST` con el token de ingesta | MQTT `armor/*/#` oder HTTP `POST` mit dem Ingest-Token | MQTT `armor/*/#` ou HTTP `POST` avec le jeton d'ingestion | MQTT `armor/*/#` o HTTP `POST` con il token di ingestione | MQTT `armor/*/#` または取り込みトークン付きの HTTP `POST` | MQTT `armor/*/#` 或带采集令牌的 HTTP `POST` | MQTT `armor/*/#` ou HTTP `POST` com o token de ingestão"), T("their messages in, orders out | sus mensajes entran, las órdenes salen | ihre Nachrichten hinein, Befehle hinaus | leurs messages entrent, les ordres sortent | i loro messaggi entrano, gli ordini escono | メッセージの受信とオーダーの送信 | 接收其消息并下发指令 | as suas mensagens entram, as ordens saem")),
    ("ARMOR-NETWORK", T("state in, orders and sealed logins out | estado entra, órdenes y accesos sellados salen | Zustand hinein, Aufträge und versiegelte Logins hinaus | l'état entre, ordres et identifiants scellés sortent | lo stato entra, ordini e accessi sigillati escono | 状態の受信、オーダーと封印した認証情報の送信 | 接收状态，下发指令和密封凭据 | o estado entra, ordens e credenciais seladas saem"), T("the local network | la red local | das lokale Netz | le réseau local | la rete locale | ローカルネットワーク | 本地网络 | a rede local")),
    ("ARMOR-STUDIO, ARMOR-ANDROID-CONTROL", T("HTTP, MJPEG and the WebSocket `/api/v1/events` | HTTP, MJPEG y el WebSocket `/api/v1/events` | HTTP, MJPEG und der WebSocket `/api/v1/events` | HTTP, MJPEG et le WebSocket `/api/v1/events` | HTTP, MJPEG e il WebSocket `/api/v1/events` | HTTP、MJPEG、WebSocket `/api/v1/events` | HTTP、MJPEG 和 WebSocket `/api/v1/events` | HTTP, MJPEG e o WebSocket `/api/v1/events`"), T("the consoles | las consolas | die Konsolen | les consoles | le console | コンソール | 控制台 | as consolas")),
    ("ARMOR-VOICE-AI", T("`/v1/command`, `/v1/turn` with its own token | `/v1/command`, `/v1/turn` con su propio token | `/v1/command`, `/v1/turn` mit eigenem Token | `/v1/command`, `/v1/turn` avec son propre jeton | `/v1/command`, `/v1/turn` con il proprio token | 専用トークンで `/v1/command`、`/v1/turn` | 用其自己的令牌访问 `/v1/command`、`/v1/turn` | `/v1/command`, `/v1/turn` com o seu próprio token"), T("decides a phrase; the server acts | decide una frase; el servidor actúa | entscheidet über einen Satz; der Server handelt | décide d'une phrase ; le serveur agit | decide una frase; il server agisce | 発話を判定し、サーバーが実行 | 判定一句话，由服务器执行 | decide uma frase; o servidor age")),
    ("ARMOR-SERVER-AI", T("`ARMOR_AI_TOKEN`, `/api/v1/ai/...` | `ARMOR_AI_TOKEN`, `/api/v1/ai/...` | `ARMOR_AI_TOKEN`, `/api/v1/ai/...` | `ARMOR_AI_TOKEN`, `/api/v1/ai/...` | `ARMOR_AI_TOKEN`, `/api/v1/ai/...` | `ARMOR_AI_TOKEN`、`/api/v1/ai/...` | `ARMOR_AI_TOKEN`、`/api/v1/ai/...` | `ARMOR_AI_TOKEN`, `/api/v1/ai/...`"), T("observation of the cameras | observación de las cámaras | Beobachtung der Kameras | observation des caméras | osservazione delle telecamere | カメラの観察 | 摄像头观察 | observação das câmaras")),
    ("IP cameras | Cámaras IP | IP-Kameras | Caméras IP | Telecamere IP | IP カメラ | IP 摄像头 | Câmaras IP", T("RTSP, ONVIF, Hi3510, PSIA (the server calls them) | RTSP, ONVIF, Hi3510, PSIA (el servidor las llama) | RTSP, ONVIF, Hi3510, PSIA (der Server ruft sie auf) | RTSP, ONVIF, Hi3510, PSIA (le serveur les appelle) | RTSP, ONVIF, Hi3510, PSIA (il server le chiama) | RTSP、ONVIF、Hi3510、PSIA（サーバーが呼び出す） | RTSP、ONVIF、Hi3510、PSIA（由服务器调用） | RTSP, ONVIF, Hi3510, PSIA (o servidor chama-as)"), T("live video, snapshots, recording, PTZ | vídeo en vivo, instantáneas, grabación, PTZ | Live-Video, Standbilder, Aufnahme, PTZ | vidéo en direct, instantanés, enregistrement, PTZ | video dal vivo, istantanee, registrazione, PTZ | ライブ映像、スナップショット、録画、PTZ | 实时视频、快照、录制、PTZ | vídeo em direto, instantâneos, gravação, PTZ")),
]
ROLE_TABLE[5] = (T("IP cameras | Cámaras IP | IP-Kameras | Caméras IP | Telecamere IP | IP カメラ | IP 摄像头 | Câmaras IP"),) + ROLE_TABLE[5][1:]


def S(threat, defence):
    return (T(threat), T(defence))


SECURITY_ROWS = [
    S("Guessing the Studio password | Adivinar la contraseña de Studio | Erraten des Studio-Passworts | Deviner le mot de passe de Studio | Indovinare la password di Studio | Studio のパスワードの推測 | 猜测 Studio 密码 | Adivinhar a palavra-passe do Studio",
      "scrypt (N=16384, r=8, p=1), the same work whether the user exists or not; 12 tries per 15 minutes per person and address, 60 per address, 40 a minute overall; under 8 characters is refused (12 when the server is reachable from the network) | scrypt (N=16384, r=8, p=1), el mismo trabajo exista o no el usuario; 12 intentos por 15 minutos por persona y dirección, 60 por dirección, 40 por minuto en total; menos de 8 caracteres se rechaza (12 si el servidor es alcanzable desde la red) | scrypt (N=16384, r=8, p=1), gleicher Aufwand, ob der Benutzer existiert oder nicht; 12 Versuche je 15 Minuten je Person und Adresse, 60 je Adresse, 40 pro Minute insgesamt; unter 8 Zeichen wird abgelehnt (12, wenn der Server aus dem Netz erreichbar ist) | scrypt (N=16384, r=8, p=1), même travail que l'utilisateur existe ou non ; 12 essais par 15 minutes par personne et adresse, 60 par adresse, 40 par minute au total ; moins de 8 caractères refusé (12 si le serveur est joignable depuis le réseau) | scrypt (N=16384, r=8, p=1), stesso lavoro che l'utente esista o no; 12 tentativi ogni 15 minuti per persona e indirizzo, 60 per indirizzo, 40 al minuto in totale; sotto 8 caratteri è rifiutata (12 se il server è raggiungibile dalla rete) | scrypt（N=16384、r=8、p=1）。ユーザーの有無にかかわらず同じ処理量。人とアドレスごとに 15 分で 12 回、アドレスごとに 60 回、全体で毎分 40 回。8 文字未満は拒否（ネットワークから到達可能なら 12 文字未満） | scrypt（N=16384、r=8、p=1），无论用户是否存在都做同样的计算；每人每地址 15 分钟 12 次、每地址 60 次、全局每分钟 40 次；少于 8 个字符被拒绝（服务器可从网络访问时为 12 个） | scrypt (N=16384, r=8, p=1), o mesmo trabalho exista ou não o utilizador; 12 tentativas por 15 minutos por pessoa e endereço, 60 por endereço, 40 por minuto no total; menos de 8 caracteres é recusada (12 se o servidor for alcançável pela rede)"),
    S("A stolen cookie, a request from another site | Una cookie robada, una petición de otro sitio | Ein gestohlenes Cookie, eine Anfrage von einer anderen Seite | Un cookie volé, une requête d'un autre site | Un cookie rubato, una richiesta da un altro sito | Cookie の盗難、別サイトからのリクエスト | 被盗的 Cookie、来自其他站点的请求 | Um cookie roubado, um pedido de outro site",
      "HttpOnly, SameSite=Strict and Secure behind HTTPS; sessions last 7 days (Studio), 8 hours (operator) and 12 hours with 30 minutes idle from outside | HttpOnly, SameSite=Strict y Secure con HTTPS; las sesiones duran 7 días (Studio), 8 horas (operador) y 12 horas con 30 minutos de inactividad desde fuera | HttpOnly, SameSite=Strict und Secure hinter HTTPS; Sitzungen dauern 7 Tage (Studio), 8 Stunden (Bediener) und 12 Stunden mit 30 Minuten Leerlauf von außen | HttpOnly, SameSite=Strict et Secure derrière HTTPS ; les sessions durent 7 jours (Studio), 8 heures (opérateur) et 12 heures avec 30 minutes d'inactivité depuis l'extérieur | HttpOnly, SameSite=Strict e Secure dietro HTTPS; le sessioni durano 7 giorni (Studio), 8 ore (operatore) e 12 ore con 30 minuti di inattività dall'esterno | HttpOnly、SameSite=Strict、HTTPS では Secure。セッションは Studio 7 日、オペレーター 8 時間、外部からは 12 時間（無操作 30 分） | HttpOnly、SameSite=Strict，HTTPS 后使用 Secure；会话时长：Studio 7 天、操作员 8 小时、从外部访问 12 小时（空闲 30 分钟） | HttpOnly, SameSite=Strict e Secure atrás de HTTPS; as sessões duram 7 dias (Studio), 8 horas (operador) e 12 horas com 30 minutos de inatividade vindo de fora"),
    S("Timing attacks and weak secrets | Ataques de tiempo y secretos débiles | Zeitangriffe und schwache Geheimnisse | Attaques par le temps et secrets faibles | Attacchi temporali e segreti deboli | タイミング攻撃と弱い秘密 | 计时攻击与弱密钥 | Ataques de tempo e segredos fracos",
      "Secrets are compared in constant time, must have 24 characters or more and all differ (ingest, control, operator, camera key, AI, evidence key) | Los secretos se comparan en tiempo constante, deben tener 24 caracteres o más y ser todos distintos (ingesta, control, operador, clave de cámaras, IA, clave de evidencias) | Geheimnisse werden zeitkonstant verglichen, brauchen mindestens 24 Zeichen und müssen alle verschieden sein (Ingest, Steuerung, Bediener, Kameraschlüssel, KI, Beweisschlüssel) | Les secrets sont comparés en temps constant, ont 24 caractères ou plus et sont tous différents (ingestion, contrôle, opérateur, clé des caméras, IA, clé des preuves) | I segreti si confrontano in tempo costante, hanno almeno 24 caratteri e sono tutti diversi (ingestione, controllo, operatore, chiave delle telecamere, IA, chiave delle prove) | 秘密は定数時間で比較し、24 文字以上でそれぞれ別の値にする（取り込み、制御、オペレーター、カメラ鍵、AI、証拠鍵） | 密钥以恒定时间比较，至少 24 个字符且互不相同（采集、控制、操作员、摄像头密钥、AI、证据密钥） | Os segredos comparam-se em tempo constante, têm 24 ou mais caracteres e são todos diferentes (ingestão, controlo, operador, chave das câmaras, IA, chave das provas)"),
    S("Disarming without proof | Desarmar sin comprobar quién eres | Entschärfen ohne Nachweis | Désarmer sans preuve | Disarmare senza prova | 証明なしの解除 | 未经验证的撤防 | Desarmar sem prova",
      "A PIN of 4 to 10 digits by `alarm.disarm_pin` (never, if_set, always); 3 wrong tries lock for 60 s, 5 min, 15 min and then 1 h, kept on disk across restarts; a duress PIN is told apart silently; the control token disarms only with `ARMOR_CONTROL_DISARM=1` | Un PIN de 4 a 10 dígitos según `alarm.disarm_pin` (never, if_set, always); 3 fallos bloquean 60 s, 5 min, 15 min y luego 1 h, guardado en disco entre reinicios; un PIN de coacción se distingue sin avisar; el token de control desarma solo con `ARMOR_CONTROL_DISARM=1` | Eine PIN mit 4 bis 10 Ziffern gemäß `alarm.disarm_pin` (never, if_set, always); 3 Fehlversuche sperren 60 s, 5 min, 15 min, dann 1 h, auf Platte über Neustarts gespeichert; eine Zwangs-PIN wird still erkannt; das Steuer-Token entschärft nur mit `ARMOR_CONTROL_DISARM=1` | Un PIN de 4 à 10 chiffres selon `alarm.disarm_pin` (never, if_set, always) ; 3 échecs bloquent 60 s, 5 min, 15 min puis 1 h, conservé sur disque après redémarrage ; un PIN de contrainte est reconnu sans avertir ; le jeton de contrôle ne désarme qu'avec `ARMOR_CONTROL_DISARM=1` | Un PIN di 4-10 cifre secondo `alarm.disarm_pin` (never, if_set, always); 3 errori bloccano 60 s, 5 min, 15 min e poi 1 h, salvato su disco tra i riavvii; un PIN di coercizione si distingue in silenzio; il token di controllo disarma solo con `ARMOR_CONTROL_DISARM=1` | `alarm.disarm_pin`（never、if_set、always）による 4〜10 桁の PIN。3 回失敗で 60 秒、5 分、15 分、その後 1 時間ロックし、再起動後もディスクに保持。脅迫用 PIN は気付かれずに区別。制御トークンは `ARMOR_CONTROL_DISARM=1` のときだけ解除可 | 由 `alarm.disarm_pin`（never、if_set、always）决定的 4 到 10 位 PIN；错误 3 次后锁定 60 秒、5 分钟、15 分钟，之后 1 小时，重启后仍保存在磁盘；胁迫 PIN 会被悄悄区分；控制令牌仅在 `ARMOR_CONTROL_DISARM=1` 时可撤防 | Um PIN de 4 a 10 dígitos segundo `alarm.disarm_pin` (never, if_set, always); 3 falhas bloqueiam 60 s, 5 min, 15 min e depois 1 h, guardado em disco entre reinícios; um PIN de coação distingue-se sem avisar; o token de controlo só desarma com `ARMOR_CONTROL_DISARM=1`"),
    S("Camera passwords leaking | Filtración de contraseñas de cámaras | Kennwörter der Kameras gelangen nach außen | Fuite des mots de passe des caméras | Fuga delle password delle telecamere | カメラのパスワード漏えい | 摄像头密码泄露 | Fuga das palavras-passe das câmaras",
      "AES-256-GCM in `data/cameras.json`; no API returns them; FFmpeg goes through a local RTSP tunnel (`media.rtsp_proxy`) so the password is never on a command line; ONVIF redirects are refused | AES-256-GCM en `data/cameras.json`; ninguna API las devuelve; FFmpeg pasa por un túnel RTSP local (`media.rtsp_proxy`) para que la clave no vaya en la línea de órdenes; se rechazan las redirecciones ONVIF | AES-256-GCM in `data/cameras.json`; keine API gibt sie zurück; FFmpeg läuft über einen lokalen RTSP-Tunnel (`media.rtsp_proxy`), damit das Kennwort nie in der Kommandozeile steht; ONVIF-Weiterleitungen werden abgelehnt | AES-256-GCM dans `data/cameras.json` ; aucune API ne les renvoie ; FFmpeg passe par un tunnel RTSP local (`media.rtsp_proxy`) pour que le mot de passe ne soit jamais sur une ligne de commande ; les redirections ONVIF sont refusées | AES-256-GCM in `data/cameras.json`; nessuna API le restituisce; FFmpeg passa da un tunnel RTSP locale (`media.rtsp_proxy`) così la password non sta mai su una riga di comando; i reindirizzamenti ONVIF sono rifiutati | `data/cameras.json` に AES-256-GCM で保存し、どの API も返さない。FFmpeg はローカル RTSP トンネル（`media.rtsp_proxy`）経由でパスワードをコマンドラインに出さない。ONVIF のリダイレクトは拒否 | 以 AES-256-GCM 存于 `data/cameras.json`，任何 API 都不返回；FFmpeg 通过本地 RTSP 隧道（`media.rtsp_proxy`），密码绝不出现在命令行；拒绝 ONVIF 重定向 | AES-256-GCM em `data/cameras.json`; nenhuma API as devolve; o FFmpeg passa por um túnel RTSP local (`media.rtsp_proxy`) para a palavra-passe nunca ir numa linha de comandos; os redirecionamentos ONVIF são recusados"),
    S("Live video without signing in | Vídeo en vivo sin iniciar sesión | Live-Video ohne Anmeldung | Vidéo en direct sans connexion | Video dal vivo senza accesso | ログインなしのライブ映像 | 未登录观看实时视频 | Vídeo em direto sem iniciar sessão",
      "A stream ticket tied to one camera, issued only to an operator | Un ticket de transmisión atado a una sola cámara, emitido solo a un operador | Ein Stream-Ticket für genau eine Kamera, nur an Bediener ausgestellt | Un ticket de flux lié à une seule caméra, délivré seulement à un opérateur | Un ticket di flusso legato a una sola telecamera, emesso solo a un operatore | 1 台のカメラに限定したストリームチケット（オペレーターにのみ発行） | 仅绑定一台摄像头的流票据，只发给操作员 | Um bilhete de transmissão ligado a uma só câmara, emitido apenas a um operador"),
    S("Flooding the API | Inundar la API | Überfluten der API | Inondation de l'API | Inondazione dell'API | API の過剰リクエスト | 洪泛 API | Inundar a API",
      "240 requests a minute in general (node posts have their own budget of 6000 a minute); JSON bodies of 64 kB (9 MB for an installation file) | 240 peticiones por minuto en general (los POST de nodos tienen su propio presupuesto de 6000 por minuto); cuerpos JSON de 64 kB (9 MB para un fichero de instalación) | allgemein 240 Anfragen pro Minute (Knoten-POSTs haben ein eigenes Budget von 6000 pro Minute); JSON-Inhalte bis 64 kB (9 MB für eine Installationsdatei) | 240 requêtes par minute en général (les POST des nœuds ont leur propre budget de 6000 par minute) ; corps JSON de 64 ko (9 Mo pour un fichier d'installation) | 240 richieste al minuto in generale (i POST dei nodi hanno un budget proprio di 6000 al minuto); corpi JSON da 64 kB (9 MB per un file di installazione) | 通常は毎分 240 リクエスト（ノードの POST は別枠で毎分 6000）。JSON 本文は 64 kB（インストールファイルは 9 MB） | 通常每分钟 240 个请求（节点 POST 有单独的每分钟 6000 额度）；JSON 请求体 64 kB（安装文件 9 MB） | 240 pedidos por minuto em geral (os POST dos nós têm orçamento próprio de 6000 por minuto); corpos JSON de 64 kB (9 MB para um ficheiro de instalação)"),
    S("A false or malformed node message | Un mensaje de nodo falso o mal formado | Eine falsche oder fehlerhafte Knotennachricht | Un message de nœud faux ou mal formé | Un messaggio di nodo falso o malformato | 偽造または不正なノードメッセージ | 伪造或格式错误的节点消息 | Uma mensagem de nó falsa ou mal formada",
      "Checked at the boundary by the parsers of `src/contracts.ts`, tested with the shared vectors of ARMOR-COMMON: at most 15 tracks, lux up to 200 000, a node id of letters, digits, `_` and `-`; a token per node derived from the shared one and a strict mode (`ARMOR_INGEST_STRICT=1`) | Se comprueba en el borde con los analizadores de `src/contracts.ts`, probados con los vectores compartidos de ARMOR-COMMON: 15 pistas como máximo, lux hasta 200 000, un id de nodo de letras, dígitos, `_` y `-`; un token por nodo derivado del compartido y un modo estricto (`ARMOR_INGEST_STRICT=1`) | An der Grenze von den Parsern in `src/contracts.ts` geprüft, getestet mit den gemeinsamen Vektoren von ARMOR-COMMON: höchstens 15 Spuren, Lux bis 200 000, eine Knoten-ID aus Buchstaben, Ziffern, `_` und `-`; ein Token je Knoten, vom gemeinsamen abgeleitet, und ein strenger Modus (`ARMOR_INGEST_STRICT=1`) | Vérifié à la frontière par les analyseurs de `src/contracts.ts`, testés avec les vecteurs partagés d'ARMOR-COMMON : 15 pistes au plus, lux jusqu'à 200 000, un identifiant de nœud en lettres, chiffres, `_` et `-` ; un jeton par nœud dérivé du partagé et un mode strict (`ARMOR_INGEST_STRICT=1`) | Verificato al confine dai parser di `src/contracts.ts`, provati con i vettori condivisi di ARMOR-COMMON: al massimo 15 tracce, lux fino a 200 000, un id di nodo con lettere, cifre, `_` e `-`; un token per nodo derivato da quello condiviso e una modalità rigorosa (`ARMOR_INGEST_STRICT=1`) | `src/contracts.ts` のパーサーが境界で検査し、ARMOR-COMMON の共有ベクターでテスト済み：トラックは最大 15、照度は 200 000 まで、ノード ID は英数字と `_` `-`。共有トークンから導出したノード別トークンと厳格モード（`ARMOR_INGEST_STRICT=1`） | 由 `src/contracts.ts` 的解析器在边界检查，并用 ARMOR-COMMON 的共享向量测试：最多 15 条轨迹，照度至多 200 000，节点 ID 由字母、数字、`_` 和 `-` 组成；每个节点有由共享令牌派生的令牌，另有严格模式（`ARMOR_INGEST_STRICT=1`） | Verificada na fronteira pelos analisadores de `src/contracts.ts`, testados com os vetores partilhados do ARMOR-COMMON: no máximo 15 pistas, lux até 200 000, um id de nó com letras, dígitos, `_` e `-`; um token por nó derivado do partilhado e um modo estrito (`ARMOR_INGEST_STRICT=1`)"),
    S("A session from outside the house | Una sesión desde fuera de casa | Eine Sitzung von außerhalb des Hauses | Une session depuis l'extérieur | Una sessione da fuori casa | 家の外からのセッション | 来自屋外的会话 | Uma sessão vinda de fora de casa",
      "A second factor (`ARMOR_TOTP_REQUIRED`: off, remote, always), a policy for what it may do (`ARMOR_REMOTE_POLICY`: full, operate, view), proof of identity again for critical actions (5 minutes by default) and an alert on a sign-in from a new place | Segundo factor (`ARMOR_TOTP_REQUIRED`: off, remote, always), una política de lo que puede hacer (`ARMOR_REMOTE_POLICY`: full, operate, view), nueva prueba de identidad para acciones críticas (5 minutos por defecto) y aviso al entrar desde un sitio nuevo | Zweiter Faktor (`ARMOR_TOTP_REQUIRED`: off, remote, always), eine Richtlinie, was sie darf (`ARMOR_REMOTE_POLICY`: full, operate, view), erneuter Identitätsnachweis bei kritischen Aktionen (standardmäßig 5 Minuten) und ein Hinweis bei Anmeldung von einem neuen Ort | Second facteur (`ARMOR_TOTP_REQUIRED` : off, remote, always), une politique de ce qu'elle peut faire (`ARMOR_REMOTE_POLICY` : full, operate, view), nouvelle preuve d'identité pour les actions critiques (5 minutes par défaut) et alerte lors d'une connexion depuis un nouveau lieu | Secondo fattore (`ARMOR_TOTP_REQUIRED`: off, remote, always), una politica su cosa può fare (`ARMOR_REMOTE_POLICY`: full, operate, view), nuova prova d'identità per le azioni critiche (5 minuti di default) e avviso per un accesso da un luogo nuovo | 2 要素（`ARMOR_TOTP_REQUIRED`：off、remote、always）、できることの方針（`ARMOR_REMOTE_POLICY`：full、operate、view）、重要操作での再認証（既定 5 分）、新しい場所からのログイン通知 | 第二因素（`ARMOR_TOTP_REQUIRED`：off、remote、always）、可做事项的策略（`ARMOR_REMOTE_POLICY`：full、operate、view）、关键操作前重新验证身份（默认 5 分钟）以及从新地点登录时的提醒 | Segundo fator (`ARMOR_TOTP_REQUIRED`: off, remote, always), uma política do que pode fazer (`ARMOR_REMOTE_POLICY`: full, operate, view), nova prova de identidade para ações críticas (5 minutos por predefinição) e aviso ao entrar de um sítio novo"),
    S("A node panel used as an open proxy | Un panel de nodo usado como proxy abierto | Ein Knoten-Panel als offener Proxy | Un panneau de nœud utilisé comme proxy ouvert | Un pannello di nodo usato come proxy aperto | 開放プロキシとして使われるノードパネル | 被当作开放代理的节点面板 | Um painel de nó usado como proxy aberto",
      "The address never comes from the request; HTTPS is pinned to the SHA-256 fingerprint of the node's certificate | La dirección nunca sale de la petición; HTTPS queda fijado a la huella SHA-256 del certificado del nodo | Die Adresse stammt nie aus der Anfrage; HTTPS ist an den SHA-256-Fingerabdruck des Knotenzertifikats gebunden | L'adresse ne vient jamais de la requête ; HTTPS est épinglé à l'empreinte SHA-256 du certificat du nœud | L'indirizzo non arriva mai dalla richiesta; HTTPS è vincolato all'impronta SHA-256 del certificato del nodo | アドレスはリクエストから取らず、HTTPS はノード証明書の SHA-256 指紋に固定 | 地址从不取自请求；HTTPS 固定到节点证书的 SHA-256 指纹 | O endereço nunca vem do pedido; o HTTPS fica fixado à impressão digital SHA-256 do certificado do nó"),
    S("Voice: silencing without checking, long text, huge audio | Voz: silenciar sin comprobar, texto largo, audio enorme | Sprache: Stummschalten ohne Prüfung, langer Text, riesiges Audio | Voix : couper sans vérifier, texte long, audio énorme | Voce: silenziare senza verifica, testo lungo, audio enorme | 音声：確認なしの消音、長文、巨大な音声 | 语音：未确认就静音、超长文本、超大音频 | Voz: silenciar sem verificar, texto longo, áudio enorme",
      "The policy `voice.silence_confirmation` (off, pin, double_turn) travels with every turn; confirmation tied to the person; 200 characters, 8 languages, 30 requests a minute; audio of 480 000 bytes and a reply of 200 000 bytes at most | La política `voice.silence_confirmation` (off, pin, double_turn) viaja en cada turno; confirmación atada a la persona; 200 caracteres, 8 idiomas, 30 peticiones por minuto; audio de 480 000 bytes y respuesta de 200 000 bytes como máximo | Die Richtlinie `voice.silence_confirmation` (off, pin, double_turn) reist mit jedem Turn; Bestätigung an die Person gebunden; 200 Zeichen, 8 Sprachen, 30 Anfragen pro Minute; Audio höchstens 480 000 Bytes, Antwort höchstens 200 000 Bytes | La politique `voice.silence_confirmation` (off, pin, double_turn) accompagne chaque tour ; confirmation liée à la personne ; 200 caractères, 8 langues, 30 requêtes par minute ; audio de 480 000 octets et réponse de 200 000 octets au plus | La politica `voice.silence_confirmation` (off, pin, double_turn) viaggia con ogni turno; conferma legata alla persona; 200 caratteri, 8 lingue, 30 richieste al minuto; audio al massimo 480 000 byte e risposta 200 000 byte | ポリシー `voice.silence_confirmation`（off、pin、double_turn）を毎ターン送信。確認は本人に紐づく。200 文字、8 言語、毎分 30 リクエスト、音声は最大 480 000 バイト、応答は最大 200 000 バイト | 策略 `voice.silence_confirmation`（off、pin、double_turn）随每个轮次发送；确认与本人绑定；200 个字符、8 种语言、每分钟 30 个请求；音频最多 480 000 字节，回复最多 200 000 字节 | A política `voice.silence_confirmation` (off, pin, double_turn) viaja em cada turno; confirmação ligada à pessoa; 200 caracteres, 8 idiomas, 30 pedidos por minuto; áudio de 480 000 bytes e resposta de 200 000 bytes no máximo"),
    S("Dangerous writes by mistake | Escrituras peligrosas por error | Gefährliche Schreibzugriffe aus Versehen | Écritures dangereuses par erreur | Scritture pericolose per errore | 誤った危険な書き込み | 误操作的危险写入 | Escritas perigosas por engano",
      "Off unless `ARMOR_BATTERY_WRITE=1`, `ARMOR_ELECTRICAL_SWITCHING=1` or `ARMOR_ALARM_COMMANDS=1`, with a warning at start-up | Apagadas salvo `ARMOR_BATTERY_WRITE=1`, `ARMOR_ELECTRICAL_SWITCHING=1` o `ARMOR_ALARM_COMMANDS=1`, con aviso al arrancar | Aus, außer mit `ARMOR_BATTERY_WRITE=1`, `ARMOR_ELECTRICAL_SWITCHING=1` oder `ARMOR_ALARM_COMMANDS=1`, mit Warnung beim Start | Désactivées sauf `ARMOR_BATTERY_WRITE=1`, `ARMOR_ELECTRICAL_SWITCHING=1` ou `ARMOR_ALARM_COMMANDS=1`, avec avertissement au démarrage | Spente salvo `ARMOR_BATTERY_WRITE=1`, `ARMOR_ELECTRICAL_SWITCHING=1` o `ARMOR_ALARM_COMMANDS=1`, con avviso all'avvio | `ARMOR_BATTERY_WRITE=1`、`ARMOR_ELECTRICAL_SWITCHING=1`、`ARMOR_ALARM_COMMANDS=1` を設定しない限りオフ。起動時に警告 | 除非设置 `ARMOR_BATTERY_WRITE=1`、`ARMOR_ELECTRICAL_SWITCHING=1` 或 `ARMOR_ALARM_COMMANDS=1`，否则关闭；启动时给出警告 | Desligadas salvo `ARMOR_BATTERY_WRITE=1`, `ARMOR_ELECTRICAL_SWITCHING=1` ou `ARMOR_ALARM_COMMANDS=1`, com aviso no arranque"),
]

SECURITY_TAIL = P(
    "**Switches in Studio.** The protections that can be tuned are 17 settings kept in `security-settings.json` (mode 0600, atomic writes), each with a conservative default, and lowering one is written in the audit: `alarm.disarm_pin`, `voice.silence_confirmation`, `alarm.config_hash`, `server.zone_feed`, `server.zone_feed_signature`, `media.rtsp_proxy`, `network.login_secure_only`, `login.country_alert`, `electrical.set_aside_old_readings`, `voice.multipart_turn`, `panel.live_events`, `client.device_lock`, `nodes.nvs_encryption`, `alarm_audio.spoken`, `alarm_audio.custom_sounds`, `voice.turn_max_bytes` and `voice.reply_audio_max_bytes`.\n\n**What it never does:** return a camera password, keep the words that were spoken (only the command and its result), or write a PIN, a token or a cookie in a log. There has been no independent security review.",
    "**Interruptores en Studio.** Las protecciones que se pueden ajustar son 17 valores guardados en `security-settings.json` (modo 0600, escritura atómica), cada uno con un valor por defecto conservador, y bajar uno queda en la auditoría: `alarm.disarm_pin`, `voice.silence_confirmation`, `alarm.config_hash`, `server.zone_feed`, `server.zone_feed_signature`, `media.rtsp_proxy`, `network.login_secure_only`, `login.country_alert`, `electrical.set_aside_old_readings`, `voice.multipart_turn`, `panel.live_events`, `client.device_lock`, `nodes.nvs_encryption`, `alarm_audio.spoken`, `alarm_audio.custom_sounds`, `voice.turn_max_bytes` y `voice.reply_audio_max_bytes`.\n\n**Lo que nunca hace:** devolver una contraseña de cámara, guardar las palabras que se dijeron (solo el comando y su resultado) ni escribir un PIN, un token o una cookie en un registro. No ha habido revisión de seguridad independiente.",
    "**Schalter in Studio.** Die einstellbaren Schutzmaßnahmen sind 17 Werte in `security-settings.json` (Modus 0600, atomares Schreiben), jeweils mit konservativem Standard; das Absenken eines Werts landet im Audit: `alarm.disarm_pin`, `voice.silence_confirmation`, `alarm.config_hash`, `server.zone_feed`, `server.zone_feed_signature`, `media.rtsp_proxy`, `network.login_secure_only`, `login.country_alert`, `electrical.set_aside_old_readings`, `voice.multipart_turn`, `panel.live_events`, `client.device_lock`, `nodes.nvs_encryption`, `alarm_audio.spoken`, `alarm_audio.custom_sounds`, `voice.turn_max_bytes` und `voice.reply_audio_max_bytes`.\n\n**Was es nie tut:** ein Kamerakennwort zurückgeben, das Gesprochene speichern (nur Befehl und Ergebnis) oder eine PIN, ein Token oder ein Cookie in ein Protokoll schreiben. Eine unabhängige Sicherheitsprüfung gab es nicht.",
    "**Interrupteurs dans Studio.** Les protections réglables sont 17 valeurs conservées dans `security-settings.json` (mode 0600, écriture atomique), chacune avec un défaut prudent ; en abaisser une est inscrit dans l'audit : `alarm.disarm_pin`, `voice.silence_confirmation`, `alarm.config_hash`, `server.zone_feed`, `server.zone_feed_signature`, `media.rtsp_proxy`, `network.login_secure_only`, `login.country_alert`, `electrical.set_aside_old_readings`, `voice.multipart_turn`, `panel.live_events`, `client.device_lock`, `nodes.nvs_encryption`, `alarm_audio.spoken`, `alarm_audio.custom_sounds`, `voice.turn_max_bytes` et `voice.reply_audio_max_bytes`.\n\n**Ce qu'il ne fait jamais :** renvoyer un mot de passe de caméra, garder les paroles prononcées (seulement la commande et son résultat), ni écrire un PIN, un jeton ou un cookie dans un journal. Il n'y a pas eu de revue de sécurité indépendante.",
    "**Interruttori in Studio.** Le protezioni regolabili sono 17 valori in `security-settings.json` (modo 0600, scrittura atomica), ciascuno con un default prudente; abbassarne uno viene registrato nell'audit: `alarm.disarm_pin`, `voice.silence_confirmation`, `alarm.config_hash`, `server.zone_feed`, `server.zone_feed_signature`, `media.rtsp_proxy`, `network.login_secure_only`, `login.country_alert`, `electrical.set_aside_old_readings`, `voice.multipart_turn`, `panel.live_events`, `client.device_lock`, `nodes.nvs_encryption`, `alarm_audio.spoken`, `alarm_audio.custom_sounds`, `voice.turn_max_bytes` e `voice.reply_audio_max_bytes`.\n\n**Cosa non fa mai:** restituire una password di telecamera, conservare le parole dette (solo il comando e il suo risultato) né scrivere un PIN, un token o un cookie in un registro. Non c'è stata una revisione di sicurezza indipendente.",
    "**Studio のスイッチ。** 調整できる保護は `security-settings.json`（モード 0600、アトミック書き込み）にある 17 項目で、どれも保守的な既定値です。下げた場合は監査に記録されます：`alarm.disarm_pin`、`voice.silence_confirmation`、`alarm.config_hash`、`server.zone_feed`、`server.zone_feed_signature`、`media.rtsp_proxy`、`network.login_secure_only`、`login.country_alert`、`electrical.set_aside_old_readings`、`voice.multipart_turn`、`panel.live_events`、`client.device_lock`、`nodes.nvs_encryption`, `alarm_audio.spoken`, `alarm_audio.custom_sounds`、`voice.turn_max_bytes`、`voice.reply_audio_max_bytes`。\n\n**決してしないこと：** カメラのパスワードを返す、話した内容を保存する（コマンドと結果のみ）、PIN・トークン・Cookie をログに書く。第三者によるセキュリティレビューはありません。",
    "**Studio 中的开关。** 可调的保护措施是保存在 `security-settings.json`（权限 0600，原子写入）中的 17 项设置，每项都有保守的默认值，调低任何一项都会写入审计：`alarm.disarm_pin`、`voice.silence_confirmation`、`alarm.config_hash`、`server.zone_feed`、`server.zone_feed_signature`、`media.rtsp_proxy`、`network.login_secure_only`、`login.country_alert`、`electrical.set_aside_old_readings`、`voice.multipart_turn`、`panel.live_events`、`client.device_lock`、`nodes.nvs_encryption`, `alarm_audio.spoken`, `alarm_audio.custom_sounds`、`voice.turn_max_bytes` 和 `voice.reply_audio_max_bytes`。\n\n**它绝不会：** 返回摄像头密码、保存所说的话（只保留命令及其结果），或把 PIN、令牌或 Cookie 写进日志。没有独立的安全审查。",
    "**Interruptores no Studio.** As proteções ajustáveis são 17 valores guardados em `security-settings.json` (modo 0600, escrita atómica), cada um com um valor predefinido conservador; baixar um fica registado na auditoria: `alarm.disarm_pin`, `voice.silence_confirmation`, `alarm.config_hash`, `server.zone_feed`, `server.zone_feed_signature`, `media.rtsp_proxy`, `network.login_secure_only`, `login.country_alert`, `electrical.set_aside_old_readings`, `voice.multipart_turn`, `panel.live_events`, `client.device_lock`, `nodes.nvs_encryption`, `alarm_audio.spoken`, `alarm_audio.custom_sounds`, `voice.turn_max_bytes` e `voice.reply_audio_max_bytes`.\n\n**O que nunca faz:** devolver uma palavra-passe de câmara, guardar as palavras ditas (só o comando e o seu resultado) nem escrever um PIN, um token ou um cookie num registo. Não houve revisão de segurança independente.")

ROUTES = [
    ("`GET /healthz`", T("none | ninguna | keine | aucune | nessuna | なし | 无 | nenhuma"), T("alive and ready | vivo y listo | lebt und ist bereit | vivant et prêt | vivo e pronto | 稼働中 | 存活就绪 | vivo e pronto")),
    ("`POST /api/v1/telemetry`  `/health`  `/solar`  `/electrical/readings`  `/alarm/state`  `/network/state`  `/devices/state`", T("ingest token | token de ingesta | Ingest-Token | jeton d'ingestion | token di ingestione | 取り込みトークン | 采集令牌 | token de ingestão"), T("what the nodes post | lo que publican los nodos | was die Knoten senden | ce que les nœuds envoient | ciò che i nodi pubblicano | ノードが送る内容 | 节点上报的内容 | o que os nós publicam")),
    ("`WS /api/v1/events`", T("session | sesión | Sitzung | session | sessione | セッション | 会话 | sessão"), T("the whole state, whenever something changes (a burst is one message; a client that falls behind is dropped; 1 KB at most from the client) | todo el estado cuando algo cambia (una ráfaga es un mensaje; un cliente que se retrasa se descarta; 1 KB como máximo del cliente) | der ganze Zustand bei jeder Änderung (ein Schwung ist eine Nachricht; ein zurückfallender Client wird getrennt; höchstens 1 KB vom Client) | tout l'état à chaque changement (une rafale est un message ; un client en retard est coupé ; 1 Ko au plus du client) | tutto lo stato a ogni cambiamento (una raffica è un messaggio; un client in ritardo viene scartato; 1 KB al massimo dal client) | 変化のたびに全状態を送信（連続変化は 1 メッセージ、遅れたクライアントは切断、クライアントからは最大 1 KB） | 状态变化时推送完整状态（一阵变化合并为一条消息；落后的客户端会被断开；客户端最多发 1 KB） | todo o estado quando algo muda (uma rajada é uma mensagem; um cliente atrasado é descartado; 1 KB no máximo do cliente)")),
    ("`WS /api/v1/panel/events`", T("panel | panel | Panel | panneau | pannello | パネル | 面板 | painel"), T("a smaller channel for the wall panel (128 bytes at most from the client) | un canal más pequeño para el panel de pared (128 bytes como máximo del cliente) | ein kleinerer Kanal für das Wandpanel (höchstens 128 Bytes vom Client) | un canal plus petit pour le panneau mural (128 octets au plus du client) | un canale più piccolo per il pannello a muro (128 byte al massimo dal client) | 壁面パネル用の小さなチャネル（クライアントからは最大 128 バイト） | 壁挂面板用的较小通道（客户端最多 128 字节） | um canal mais pequeno para o painel de parede (128 bytes no máximo do cliente)")),
    ("`POST /api/v1/voice/command`", T("operator, 30 a minute | operador, 30 por minuto | Bediener, 30 pro Minute | opérateur, 30 par minute | operatore, 30 al minuto | オペレーター、毎分 30 | 操作员，每分钟 30 次 | operador, 30 por minuto"), T("a written or spoken command: `{text, language, confirmation?, pin?}`; answers `{accepted, executed, intent, outcome, speech, confirmation_token?, reason?, result?}` | una orden escrita o hablada: `{text, language, confirmation?, pin?}`; responde `{accepted, executed, intent, outcome, speech, confirmation_token?, reason?, result?}` | ein geschriebener oder gesprochener Befehl: `{text, language, confirmation?, pin?}`; Antwort `{accepted, executed, intent, outcome, speech, confirmation_token?, reason?, result?}` | une commande écrite ou vocale : `{text, language, confirmation?, pin?}` ; répond `{accepted, executed, intent, outcome, speech, confirmation_token?, reason?, result?}` | un comando scritto o vocale: `{text, language, confirmation?, pin?}`; risponde `{accepted, executed, intent, outcome, speech, confirmation_token?, reason?, result?}` | 文字または音声のコマンド `{text, language, confirmation?, pin?}`。応答は `{accepted, executed, intent, outcome, speech, confirmation_token?, reason?, result?}` | 文字或语音命令 `{text, language, confirmation?, pin?}`；返回 `{accepted, executed, intent, outcome, speech, confirmation_token?, reason?, result?}` | uma ordem escrita ou falada: `{text, language, confirmation?, pin?}`; responde `{accepted, executed, intent, outcome, speech, confirmation_token?, reason?, result?}`")),
    ("`POST /api/v1/voice/turn`  `/api/v1/voice/v1/turn`", T("header `X-Armor-Voice-Token` | cabecera `X-Armor-Voice-Token` | Header `X-Armor-Voice-Token` | en-tête `X-Armor-Voice-Token` | intestazione `X-Armor-Voice-Token` | ヘッダー `X-Armor-Voice-Token` | 请求头 `X-Armor-Voice-Token` | cabeçalho `X-Armor-Voice-Token`"), T("the audio of one turn (multipart); errors `unauthorized`, `multipart_turn_disabled` (415), `audio_too_large` (413), `bad_multipart` (400), `voice_bad_reply` (502) | el audio de un turno (multipart); errores `unauthorized`, `multipart_turn_disabled` (415), `audio_too_large` (413), `bad_multipart` (400), `voice_bad_reply` (502) | das Audio eines Turns (Multipart); Fehler `unauthorized`, `multipart_turn_disabled` (415), `audio_too_large` (413), `bad_multipart` (400), `voice_bad_reply` (502) | l'audio d'un tour (multipart) ; erreurs `unauthorized`, `multipart_turn_disabled` (415), `audio_too_large` (413), `bad_multipart` (400), `voice_bad_reply` (502) | l'audio di un turno (multipart); errori `unauthorized`, `multipart_turn_disabled` (415), `audio_too_large` (413), `bad_multipart` (400), `voice_bad_reply` (502) | 1 ターンの音声（multipart）。エラー：`unauthorized`、`multipart_turn_disabled`（415）、`audio_too_large`（413）、`bad_multipart`（400）、`voice_bad_reply`（502） | 一个轮次的音频（multipart）；错误 `unauthorized`、`multipart_turn_disabled`（415）、`audio_too_large`（413）、`bad_multipart`（400）、`voice_bad_reply`（502） | o áudio de um turno (multipart); erros `unauthorized`, `multipart_turn_disabled` (415), `audio_too_large` (413), `bad_multipart` (400), `voice_bad_reply` (502)")),
    ("`GET /api/v1/alarm-audio`", T("operator | operador | Operator | opérateur | operatore | オペレーター | 操作员 | operador"), T("what the sound of the alarms offers: the two options (off by default), whether a voice gateway is set up, the limits and the sounds stored | lo que ofrece el sonido de las alarmas: las dos opciones (desactivadas por defecto), si hay pasarela de voz, los límites y los sonidos guardados | was der Ton der Alarme bietet: die zwei Optionen (standardmäßig aus), ob ein Sprach-Gateway eingerichtet ist, die Grenzen und die gespeicherten Töne | ce qu'offre le son des alarmes : les deux options (désactivées par défaut), la présence d'une passerelle vocale, les limites et les sons enregistrés | ciò che offre il suono degli allarmi: le due opzioni (disattivate per default), se c'è un gateway vocale, i limiti e i suoni salvati | アラーム音の状態：2 つのオプション（既定はオフ）、音声ゲートウェイの有無、上限、保存済みの音 | 报警声音的状态：两个选项（默认关闭）、是否设置了语音网关、限制以及已保存的声音 | o que o som dos alarmes oferece: as duas opções (desligadas por defeito), se há porta de ligação de voz, os limites e os sons guardados")),
    ("`GET /api/v1/alarm-audio/spoken`", T("operator or the account of a wall panel | operador o la cuenta de un panel de pared | Operator oder das Konto eines Wandpanels | opérateur ou le compte d'un panneau mural | operatore o l'account di un pannello a parete | オペレーターまたは壁面パネルのアカウント | 操作员或壁挂面板的账户 | operador ou a conta de um painel de parede"), T("an alarm said out loud (origin, severity, alarm code; raw 16 kHz 16-bit mono PCM with its SHA-256), made by the voice gateway and kept in a cache; 404 `spoken_alarms_disabled` while the option is off | una alarma dicha en voz alta (origen, gravedad, código de alarma; PCM mono de 16 bits a 16 kHz con su SHA-256), hecha por la pasarela de voz y guardada en una caché; 404 `spoken_alarms_disabled` con la opción desactivada | ein laut gesprochener Alarm (Herkunft, Schweregrad, Alarmcode; rohes 16-kHz-16-Bit-Mono-PCM mit SHA-256), vom Sprach-Gateway erzeugt und in einem Cache gehalten; 404 `spoken_alarms_disabled`, solange die Option aus ist | une alarme dite à voix haute (origine, gravité, code d'alarme ; PCM mono 16 bits à 16 kHz avec son SHA-256), produite par la passerelle vocale et gardée dans un cache ; 404 `spoken_alarms_disabled` tant que l'option est désactivée | un allarme pronunciato ad alta voce (origine, gravità, codice di allarme; PCM mono a 16 bit e 16 kHz con il suo SHA-256), prodotto dal gateway vocale e tenuto in una cache; 404 `spoken_alarms_disabled` con l'opzione disattivata | 音声で読み上げたアラーム（発生元、重大度、アラームコード。SHA-256 付きの 16 kHz 16 ビットモノラル PCM）。音声ゲートウェイが作成しキャッシュに保持。オプションがオフの間は 404 `spoken_alarms_disabled` | 大声播报的报警（来源、严重程度、报警代码；带 SHA-256 的 16 kHz 16 位单声道 PCM），由语音网关生成并缓存；选项关闭时返回 404 `spoken_alarms_disabled` | um alarme dito em voz alta (origem, gravidade, código de alarme; PCM mono de 16 bits a 16 kHz com o seu SHA-256), feito pela porta de ligação de voz e guardado numa cache; 404 `spoken_alarms_disabled` com a opção desligada")),
    ("`GET` `PUT` `DELETE /api/v1/alarm-audio/sounds/{source}`", T("GET: operator or the account of a wall panel; PUT and DELETE: administrator (the proof of identity again from outside the house) | GET: operador o la cuenta de un panel de pared; PUT y DELETE: administrador (con nueva prueba de identidad desde fuera de casa) | GET: Operator oder das Konto eines Wandpanels; PUT und DELETE: Administrator (von außerhalb des Hauses mit erneutem Identitätsnachweis) | GET : opérateur ou le compte d'un panneau mural ; PUT et DELETE : administrateur (nouvelle preuve d'identité depuis l'extérieur) | GET: operatore o l'account di un pannello a parete; PUT e DELETE: amministratore (nuova prova di identità da fuori casa) | GET：オペレーターまたは壁面パネルのアカウント。PUT と DELETE：管理者（家の外からは再認証） | GET：操作员或壁挂面板的账户；PUT 和 DELETE：管理员（从屋外访问时需再次验证身份） | GET: operador ou a conta de um painel de parede; PUT e DELETE: administrador (nova prova de identidade a partir de fora de casa)"), T("the sound of an origin of alarm: a WAVE file of 16 kHz 16-bit mono PCM, read byte by byte (a tenth of a second up to `ARMOR_ALARM_SOUND_MAX_BYTES`, not silence), only its samples kept, served with its SHA-256; 409 `custom_sounds_disabled` while the option is off | el sonido de un origen de alarma: un archivo WAVE de PCM mono de 16 bits a 16 kHz, leído byte a byte (de una décima de segundo hasta `ARMOR_ALARM_SOUND_MAX_BYTES`, no silencio), solo se guardan sus muestras y se sirve con su SHA-256; 409 `custom_sounds_disabled` con la opción desactivada | der Ton einer Alarmherkunft: eine WAVE-Datei mit 16-kHz-16-Bit-Mono-PCM, Byte für Byte gelesen (eine Zehntelsekunde bis `ARMOR_ALARM_SOUND_MAX_BYTES`, keine Stille), nur die Samples werden gespeichert, ausgeliefert mit SHA-256; 409 `custom_sounds_disabled`, solange die Option aus ist | le son d'une origine d'alarme : un fichier WAVE en PCM mono 16 bits à 16 kHz, lu octet par octet (d'un dixième de seconde jusqu'à `ARMOR_ALARM_SOUND_MAX_BYTES`, pas de silence), seuls ses échantillons sont conservés, servi avec son SHA-256 ; 409 `custom_sounds_disabled` tant que l'option est désactivée | il suono di un'origine di allarme: un file WAVE in PCM mono a 16 bit e 16 kHz, letto byte per byte (da un decimo di secondo fino a `ARMOR_ALARM_SOUND_MAX_BYTES`, non silenzio), se ne conservano solo i campioni, servito con il suo SHA-256; 409 `custom_sounds_disabled` con l'opzione disattivata | アラームの発生元ごとの音：16 kHz 16 ビットモノラル PCM の WAVE ファイルを 1 バイトずつ検査（0.1 秒から `ARMOR_ALARM_SOUND_MAX_BYTES` まで、無音は不可）し、サンプルだけを保存して SHA-256 付きで配信。オプションがオフの間は 409 `custom_sounds_disabled` | 某个报警来源的声音：16 kHz 16 位单声道 PCM 的 WAVE 文件，逐字节检查（十分之一秒至 `ARMOR_ALARM_SOUND_MAX_BYTES`，不得为静音），只保存其采样，并附 SHA-256 提供；选项关闭时返回 409 `custom_sounds_disabled` | o som de uma origem de alarme: um ficheiro WAVE de PCM mono de 16 bits a 16 kHz, lido byte a byte (de um décimo de segundo até `ARMOR_ALARM_SOUND_MAX_BYTES`, não silêncio), só se guardam as suas amostras e é servido com o seu SHA-256; 409 `custom_sounds_disabled` com a opção desligada")),
    ("`POST /api/v1/nodes/{id}/control`  `POST /api/v1/nodes/control`", T("administrator who proved themselves a moment ago | administrador que se acaba de identificar de nuevo | Administrator, der sich eben erneut ausgewiesen hat | administrateur qui vient de se ré-identifier | amministratore che si è appena identificato di nuovo | 直前に再認証した管理者 | 刚刚重新验证身份的管理员 | administrador que acabou de provar quem é"), T("one order (restart, pause, resume, standby, identify, diagnostics, maintenance) to one node or to all | una orden (reiniciar, pausar, reanudar, espera, identificar, diagnóstico, mantenimiento) a un nodo o a todos | ein Befehl (Neustart, Pause, Fortsetzen, Standby, Identifizieren, Diagnose, Wartung) an einen Knoten oder alle | un ordre (redémarrer, pause, reprise, veille, identifier, diagnostic, maintenance) à un nœud ou à tous | un ordine (riavvio, pausa, ripresa, standby, identificazione, diagnostica, manutenzione) a un nodo o a tutti | 1 ノードまたは全ノードへのオーダー（再起動、一時停止、再開、スタンバイ、識別、診断、メンテナンス） | 向一个或所有节点下发一条指令（重启、暂停、恢复、待机、识别、诊断、维护） | uma ordem (reiniciar, pausar, retomar, espera, identificar, diagnóstico, manutenção) a um nó ou a todos")),
    ("`POST /api/v1/admin/nodes/settings`", T("administrator | administrador | Administrator | administrateur | amministratore | 管理者 | 管理员 | administrador"), T("reads, and changes if `login_limit_per_minute` is given (0 to 120 wrong passwords a minute), the sign-in limit of a node through the node's own panel; the panel login is used once and never kept, and the audit line does not carry it | lee y, si se da `login_limit_per_minute` (de 0 a 120 contraseñas erróneas por minuto), cambia el límite de acceso de un nodo a través del propio panel del nodo; el acceso al panel se usa una vez y no se guarda, y la línea de auditoría no lo lleva | liest und ändert, wenn `login_limit_per_minute` angegeben ist (0 bis 120 falsche Passwörter pro Minute), das Anmeldelimit eines Knotens über dessen eigenes Panel; die Panel-Anmeldung wird einmal benutzt und nie gespeichert, und die Audit-Zeile enthält sie nicht | lit et, si `login_limit_per_minute` est donné (0 à 120 mots de passe erronés par minute), change la limite de connexion d'un nœud par le panneau du nœud lui-même ; l'identifiant du panneau est utilisé une fois et jamais conservé, et la ligne d'audit ne le contient pas | legge e, se è dato `login_limit_per_minute` (da 0 a 120 password errate al minuto), cambia il limite di accesso di un nodo tramite il pannello del nodo stesso; l'accesso al pannello è usato una volta e mai conservato, e la riga di audit non lo contiene | ノード自身のパネルを通して、ノードのログイン上限を読み取り、`login_limit_per_minute`（1 分あたりの誤パスワード 0〜120 回）が渡されれば変更します。パネルのログイン情報は 1 回だけ使われ保存されず、監査行にも含まれません | 通过节点自己的面板读取节点的登录限制,若给出 `login_limit_per_minute`(每分钟 0 到 120 次错误密码)则修改它;面板登录信息只使用一次、绝不保存,审计行中也不含登录信息 | lê e, se `login_limit_per_minute` for dado (0 a 120 palavras-passe erradas por minuto), altera o limite de início de sessão de um nó através do painel do próprio nó; o acesso ao painel é usado uma vez e nunca guardado, e a linha de auditoria não o contém")),
    ("`POST /api/v1/admin/firmware/jobs`", T("administrator, fresh proof of identity | administrador, con prueba de identidad reciente | Administrator, frischer Identitätsnachweis | administrateur, preuve d'identité récente | amministratore, prova di identità recente | 管理者、直前の本人確認 | 管理员，刚刚完成身份确认 | administrador, prova de identidade recente"), T("installs a firmware image on the nodes one by one; an image whose file name says another board than the node's (`armor_<kind>-<board>.bin`) fails that node with `wrong_board` before anything is sent to it | instala una imagen de firmware en los nodos uno a uno; una imagen cuyo nombre de fichero dice otra placa distinta de la del nodo (`armor_<tipo>-<placa>.bin`) hace fallar ese nodo con `wrong_board` antes de enviarle nada | installiert ein Firmware-Image nacheinander auf den Knoten; ein Image, dessen Dateiname eine andere Platine als die des Knotens nennt (`armor_<Art>-<Platine>.bin`), lässt diesen Knoten mit `wrong_board` scheitern, bevor ihm etwas gesendet wird | installe une image de firmware sur les nœuds un par un ; une image dont le nom de fichier indique une autre carte que celle du nœud (`armor_<type>-<carte>.bin`) fait échouer ce nœud avec `wrong_board` avant de lui envoyer quoi que ce soit | installa un'immagine firmware sui nodi uno alla volta; un'immagine il cui nome di file indica una scheda diversa da quella del nodo (`armor_<tipo>-<scheda>.bin`) fa fallire quel nodo con `wrong_board` prima di inviargli qualsiasi cosa | ファームウェアイメージをノードへ 1 台ずつ書き込みます。ファイル名がノードのボードと異なるボードを示すイメージ（`armor_<種類>-<ボード>.bin`）は、何も送る前にそのノードを `wrong_board` で失敗させます | 逐个节点安装固件镜像;文件名所示开发板与节点开发板不同的镜像(`armor_<类型>-<开发板>.bin`)会在发送任何内容之前让该节点以 `wrong_board` 失败 | instala uma imagem de firmware nos nós um a um; uma imagem cujo nome de ficheiro indica outra placa que não a do nó (`armor_<tipo>-<placa>.bin`) faz esse nó falhar com `wrong_board` antes de lhe ser enviado o que quer que seja")),
    ("`POST /api/v1/cameras/{id}/stream-ticket`", T("operator | operador | Bediener | opérateur | operatore | オペレーター | 操作员 | operador"), T("a short-lived ticket for the live video of one camera | un ticket de vida corta para el vídeo en vivo de una cámara | ein kurzlebiges Ticket für das Live-Video einer Kamera | un ticket de courte durée pour la vidéo en direct d'une caméra | un ticket di breve durata per il video dal vivo di una telecamera | 1 台のカメラのライブ映像用の短命チケット | 单台摄像头实时视频的短期票据 | um bilhete de curta duração para o vídeo em direto de uma câmara")),
]

INTERFACES_LEAD = P(
    "The route table (`docs/ROUTES.md`, generated from the code) lists every route with who may call it; the OpenAPI file of ARMOR-COMMON describes 195 paths and 253 operations, and a test fails if a route is missing from it. The ones that matter most:",
    "La tabla de rutas (`docs/ROUTES.md`, generada del código) lista cada ruta con quién puede llamarla; el fichero OpenAPI de ARMOR-COMMON describe 195 rutas y 253 operaciones, y una prueba falla si falta alguna. Las que más importan:",
    "Die Routentabelle (`docs/ROUTES.md`, aus dem Code erzeugt) listet jede Route mit den Berechtigten; die OpenAPI-Datei von ARMOR-COMMON beschreibt 195 Pfade und 253 Operationen, und ein Test schlägt fehl, wenn eine Route fehlt. Die wichtigsten:",
    "La table des routes (`docs/ROUTES.md`, générée depuis le code) liste chaque route avec qui peut l'appeler ; le fichier OpenAPI d'ARMOR-COMMON décrit 195 chemins et 253 opérations, et un test échoue s'il en manque une. Les plus importantes :",
    "La tabella delle rotte (`docs/ROUTES.md`, generata dal codice) elenca ogni rotta con chi può chiamarla; il file OpenAPI di ARMOR-COMMON descrive 195 percorsi e 253 operazioni, e un test fallisce se ne manca una. Le più importanti:",
    "ルート表（`docs/ROUTES.md`、コードから生成）は各ルートと呼び出せる主体を一覧にします。ARMOR-COMMON の OpenAPI は 195 パス・253 操作を記述し、欠けているルートがあるとテストが失敗します。主なもの：",
    "路由表（`docs/ROUTES.md`，由代码生成）列出每条路由及可调用者；ARMOR-COMMON 的 OpenAPI 文件描述了 195 条路径和 253 个操作，缺少任何路由时测试会失败。最重要的几条：",
    "A tabela de rotas (`docs/ROUTES.md`, gerada do código) lista cada rota com quem a pode chamar; o ficheiro OpenAPI do ARMOR-COMMON descreve 195 caminhos e 253 operações, e um teste falha se faltar alguma. As mais importantes:")

CFG = [
    ("`ARMOR_INGEST_TOKEN`  `ARMOR_CONTROL_TOKEN`", T("yes (24+ characters, all different) | sí (24+ caracteres, todos distintos) | ja (24+ Zeichen, alle verschieden) | oui (24+ caractères, tous différents) | sì (24+ caratteri, tutti diversi) | 必須（24 文字以上、すべて別） | 是（24 个以上字符，互不相同） | sim (24+ caracteres, todos diferentes)"), T("what the nodes post with; what arms, disarms and reads events | con qué publican los nodos; qué arma, desarma y lee eventos | womit die Knoten senden; was schärft, entschärft und Ereignisse liest | avec quoi les nœuds publient ; ce qui arme, désarme et lit les événements | con cosa pubblicano i nodi; ciò che arma, disarma e legge gli eventi | ノードの送信用と、警戒・解除・イベント読み取り用 | 节点上报所用；布防、撤防和读取事件所用 | com o que os nós publicam; o que arma, desarma e lê eventos")),
    ("`ARMOR_STUDIO_USERNAME`  `ARMOR_STUDIO_PASSWORD`", T("yes | sí | ja | oui | sì | 必須 | 是 | sim"), T("the first administrator | el primer administrador | der erste Administrator | le premier administrateur | il primo amministratore | 最初の管理者 | 第一个管理员 | o primeiro administrador")),
    ("`ARMOR_HOST`  `ARMOR_PORT`", "127.0.0.1  8080", T("where it listens; a Studio password under 12 characters is refused when it is not loopback | dónde escucha; con otra dirección se rechaza una contraseña de Studio de menos de 12 caracteres | wo er lauscht; ein Studio-Passwort unter 12 Zeichen wird abgelehnt, wenn es nicht Loopback ist | où il écoute ; un mot de passe Studio de moins de 12 caractères est refusé hors boucle locale | dove ascolta; una password di Studio sotto 12 caratteri è rifiutata se non è loopback | 待ち受け先。ループバック以外では 12 文字未満の Studio パスワードを拒否 | 监听位置；非回环地址时拒绝少于 12 个字符的 Studio 密码 | onde escuta; uma palavra-passe do Studio com menos de 12 caracteres é recusada se não for loopback")),
    ("`ARMOR_DATA_DIR`  `ARMOR_FFMPEG_PATH`", "data/", T("state folder; FFmpeg for live video and capture | carpeta de estado; FFmpeg para vídeo en vivo y captura | Zustandsordner; FFmpeg für Live-Video und Aufnahme | dossier d'état ; FFmpeg pour la vidéo en direct et la capture | cartella di stato; FFmpeg per video dal vivo e cattura | 状態フォルダと、ライブ映像・撮影用の FFmpeg | 状态文件夹；用于实时视频和抓取的 FFmpeg | pasta de estado; FFmpeg para vídeo em direto e captura")),
    ("`ARMOR_MQTT_URL`  `ARMOR_MQTT_CA_FILE`", T("optional | opcional | optional | facultatif | facoltativo | 任意 | 可选 | opcional"), T("the broker; the installation's own authority for `mqtts://` (the server then trusts only it, checks the broker's name and refuses to start with a bad file) | el broker; la autoridad propia de la instalación para `mqtts://` (el servidor solo confía en ella, comprueba el nombre del broker y se niega a arrancar con un fichero erróneo) | der Broker; die eigene Stelle der Installation für `mqtts://` (der Server vertraut nur ihr, prüft den Brokernamen und startet bei falscher Datei nicht) | le broker ; l'autorité propre à l'installation pour `mqtts://` (le serveur ne se fie qu'à elle, vérifie le nom du broker et refuse de démarrer avec un mauvais fichier) | il broker; l'autorità propria dell'installazione per `mqtts://` (il server si fida solo di quella, verifica il nome del broker e non parte con un file errato) | ブローカー、および `mqtts://` 用の自前の認証局（サーバーはそれだけを信頼し、ブローカー名を確認し、不正なファイルでは起動しない） | 代理地址；`mqtts://` 使用的安装自有机构（服务器只信任它，检查代理名称，文件有误则拒绝启动） | o broker; a autoridade própria da instalação para `mqtts://` (o servidor só confia nela, verifica o nome do broker e recusa arrancar com um ficheiro errado)")),
    ("`ARMOR_NODE_STALE_AFTER_S`", "30 (5-3600)", T("seconds of silence before a node is stale | segundos de silencio antes de que un nodo esté obsoleto | Sekunden Stille, bis ein Knoten veraltet ist | secondes de silence avant qu'un nœud soit périmé | secondi di silenzio prima che un nodo sia obsoleto | ノードが古い扱いになるまでの無通信秒数 | 节点被视为过期前的静默秒数 | segundos de silêncio até um nó ficar obsoleto")),
    ("`ARMOR_ALERT_DWELL_MS`  `ARMOR_ALERT_MIN_TARGETS`", "2000 (0-60000)  1 (1-20)", T("how long and how many targets before a radar alert | cuánto tiempo y cuántos objetivos antes de una alerta de radar | wie lange und wie viele Ziele bis zu einem Radar-Alarm | combien de temps et de cibles avant une alerte radar | per quanto tempo e quanti bersagli prima di un avviso radar | レーダー警報までの時間と目標数 | 雷达警报前的持续时间和目标数 | quanto tempo e quantos alvos antes de um alerta de radar")),
    ("`ARMOR_ESCALATE_AFTER_MIN`", "0 = off (0-1440)", T("minutes before a critical alarm nobody sees is escalated | minutos antes de escalar una alarma crítica que nadie ve | Minuten, bis ein unbeachteter kritischer Alarm eskaliert | minutes avant d'escalader une alarme critique que personne ne voit | minuti prima di far salire un allarme critico non visto | 誰も見ていない重大アラームをエスカレーションするまでの分数 | 无人查看的严重报警升级前的分钟数 | minutos antes de escalar um alarme crítico que ninguém vê")),
    ("`ARMOR_MEDIA_RETENTION_DAYS`  `ARMOR_MEDIA_MAX_BYTES`", "30 (0-3650)  20 GiB", T("evidence kept by age and size, oldest first; protected evidence is never pruned | evidencias guardadas por edad y tamaño, las más viejas primero; la protegida nunca se borra | Beweise nach Alter und Größe, älteste zuerst; geschützte Beweise werden nie gelöscht | preuves conservées par âge et taille, les plus anciennes d'abord ; les preuves protégées ne sont jamais supprimées | prove conservate per età e dimensione, le più vecchie prima; quelle protette non vengono mai eliminate | 古い順に期間と容量で保持。保護された証拠は削除されない | 按时间和大小保留证据，先删最旧的；受保护的证据从不删除 | provas guardadas por idade e tamanho, as mais antigas primeiro; as protegidas nunca são apagadas")),
    ("`ARMOR_STUDIO_SESSION_TTL_MS`  `ARMOR_OPERATOR_SESSION_TTL_MS`  `ARMOR_REMOTE_SESSION_TTL_MS`  `ARMOR_REMOTE_IDLE_MS`  `ARMOR_ELEVATION_MS`", "7 d  8 h  12 h  30 min  5 min", T("session lengths and how long a new proof of identity lasts | duración de las sesiones y de una nueva prueba de identidad | Sitzungsdauer und Gültigkeit eines erneuten Nachweises | durée des sessions et d'une nouvelle preuve d'identité | durata delle sessioni e di una nuova prova d'identità | セッションの長さと再認証の有効時間 | 会话时长及重新验证身份的有效时间 | duração das sessões e de uma nova prova de identidade")),
    ("`ARMOR_TOTP_REQUIRED`  `ARMOR_REMOTE_POLICY`", "off  full", T("second factor and what a session from outside may do | segundo factor y lo que puede hacer una sesión desde fuera | zweiter Faktor und was eine Sitzung von außen darf | second facteur et ce qu'une session extérieure peut faire | secondo fattore e cosa può fare una sessione dall'esterno | 2 要素と外部セッションの権限 | 第二因素与外部会话可做的事 | segundo fator e o que uma sessão de fora pode fazer")),
    ("`ARMOR_ALERT_LANGUAGE`", "es", T("language of the alerts (one of the eight) | idioma de las alertas (uno de los ocho) | Sprache der Alarme (eine der acht) | langue des alertes (l'une des huit) | lingua degli avvisi (una delle otto) | 通知の言語（8 言語のいずれか） | 报警语言（八种之一） | idioma dos alertas (um dos oito)")),
    ("`ARMOR_NTFY_URL`  `ARMOR_TELEGRAM_BOT_TOKEN`  `ARMOR_HOMEASSISTANT_URL`  `ARMOR_ALERT_WEBHOOK_URL`  `ARMOR_FCM_SERVICE_ACCOUNT`", T("off | apagado | aus | désactivé | spento | オフ | 关闭 | desligado"), T("where the alarms are sent (all off by default) | adónde van las alarmas (todo apagado por defecto) | wohin die Alarme gehen (alles standardmäßig aus) | où vont les alarmes (tout désactivé par défaut) | dove vanno gli allarmi (tutto spento di default) | アラームの送信先（すべて既定でオフ） | 报警发往何处（默认全部关闭） | para onde vão os alarmes (tudo desligado por predefinição)")),
    ("`ARMOR_ALARM_COMMANDS`  `ARMOR_BATTERY_WRITE`  `ARMOR_ELECTRICAL_SWITCHING`  `ARMOR_INGEST_STRICT`  `ARMOR_CONTROL_DISARM`", "0", T("dangerous writes and strict modes, all off | escrituras peligrosas y modos estrictos, todo apagado | gefährliche Schreibzugriffe und strenge Modi, alles aus | écritures dangereuses et modes stricts, tout désactivé | scritture pericolose e modalità rigorose, tutto spento | 危険な書き込みと厳格モード（すべてオフ） | 危险写入与严格模式，全部关闭 | escritas perigosas e modos estritos, tudo desligado")),
    ("`ARMOR_COOKIE_SECURE`  `ARMOR_STUDIO_ORIGIN`", "-", T("set `1` behind TLS; the origin of Studio | pon `1` tras TLS; el origen de Studio | `1` hinter TLS setzen; der Ursprung von Studio | mettre `1` derrière TLS ; l'origine de Studio | metti `1` dietro TLS; l'origine di Studio | TLS の背後では `1`。Studio のオリジン | 在 TLS 之后设为 `1`；Studio 的来源 | pôr `1` atrás de TLS; a origem do Studio")),
]

CONFIG_LEAD = P(
    "Copy `.env.example` to `.env` (ignored by Git), or let `run.bat` / `run.sh` generate random secrets on the first run. The complete list of the variables, with their ranges, is in [docs/ENVIRONMENT.md](docs/ENVIRONMENT.md) (generated from the code) and the remote-access ones in [docs/REMOTE_ACCESS.md](docs/REMOTE_ACCESS.md). The values that protect the installation are not here but in Studio (see Security).",
    "Copia `.env.example` a `.env` (ignorado por Git), o deja que `run.bat` / `run.sh` generen secretos aleatorios en la primera ejecución. La lista completa de variables, con sus rangos, está en [docs/ENVIRONMENT.md](docs/ENVIRONMENT.md) (generada del código) y las de acceso remoto en [docs/REMOTE_ACCESS.md](docs/REMOTE_ACCESS.md). Los valores que protegen la instalación no están aquí sino en Studio (ver Seguridad).",
    "`.env.example` nach `.env` kopieren (von Git ignoriert) oder `run.bat` / `run.sh` beim ersten Start zufällige Geheimnisse erzeugen lassen. Die vollständige Liste der Variablen mit Bereichen steht in [docs/ENVIRONMENT.md](docs/ENVIRONMENT.md) (aus dem Code erzeugt), die des Fernzugriffs in [docs/REMOTE_ACCESS.md](docs/REMOTE_ACCESS.md). Die Werte, die die Installation schützen, stehen nicht hier, sondern in Studio (siehe Sicherheit).",
    "Copiez `.env.example` en `.env` (ignoré par Git), ou laissez `run.bat` / `run.sh` générer des secrets aléatoires au premier lancement. La liste complète des variables, avec leurs plages, est dans [docs/ENVIRONMENT.md](docs/ENVIRONMENT.md) (générée depuis le code) et celles de l'accès à distance dans [docs/REMOTE_ACCESS.md](docs/REMOTE_ACCESS.md). Les valeurs qui protègent l'installation ne sont pas ici mais dans Studio (voir Sécurité).",
    "Copia `.env.example` in `.env` (ignorato da Git), oppure lascia che `run.bat` / `run.sh` generino segreti casuali alla prima esecuzione. L'elenco completo delle variabili, con i loro intervalli, è in [docs/ENVIRONMENT.md](docs/ENVIRONMENT.md) (generato dal codice) e quelle dell'accesso remoto in [docs/REMOTE_ACCESS.md](docs/REMOTE_ACCESS.md). I valori che proteggono l'installazione non sono qui ma in Studio (vedi Sicurezza).",
    "`.env.example` を `.env`（Git は無視）にコピーするか、初回実行時に `run.bat` / `run.sh` がランダムな秘密を生成します。変数の完全な一覧と範囲は [docs/ENVIRONMENT.md](docs/ENVIRONMENT.md)（コードから生成）、リモートアクセス関連は [docs/REMOTE_ACCESS.md](docs/REMOTE_ACCESS.md) にあります。設備を守る値はここではなく Studio で変えます（セキュリティの節を参照）。",
    "把 `.env.example` 复制为 `.env`（Git 忽略），或让 `run.bat` / `run.sh` 在首次运行时生成随机密钥。变量的完整列表及范围见 [docs/ENVIRONMENT.md](docs/ENVIRONMENT.md)（由代码生成），远程访问相关变量见 [docs/REMOTE_ACCESS.md](docs/REMOTE_ACCESS.md)。保护安装的取值不在这里，而在 Studio 中修改（见安全部分）。",
    "Copie `.env.example` para `.env` (ignorado pelo Git), ou deixe `run.bat` / `run.sh` gerar segredos aleatórios na primeira execução. A lista completa das variáveis, com os seus intervalos, está em [docs/ENVIRONMENT.md](docs/ENVIRONMENT.md) (gerada do código) e as do acesso remoto em [docs/REMOTE_ACCESS.md](docs/REMOTE_ACCESS.md). Os valores que protegem a instalação não estão aqui mas no Studio (ver Segurança).")

QUICK_LEAD = P("**Requirements:** Node.js 22+, FFmpeg (live video and capture), an MQTT broker (Mosquitto).", "**Requisitos:** Node.js 22+, FFmpeg (vídeo en vivo y captura), un broker MQTT (Mosquitto).", "**Voraussetzungen:** Node.js 22+, FFmpeg (Live-Video und Aufnahme), ein MQTT-Broker (Mosquitto).",
               "**Prérequis :** Node.js 22+, FFmpeg (vidéo en direct et capture), un broker MQTT (Mosquitto).", "**Requisiti:** Node.js 22+, FFmpeg (video dal vivo e cattura), un broker MQTT (Mosquitto).", "**要件：** Node.js 22+、FFmpeg（ライブ映像と撮影）、MQTT ブローカー（Mosquitto）。",
               "**要求：** Node.js 22+、FFmpeg（实时视频和抓取）、MQTT 代理（Mosquitto）。", "**Requisitos:** Node.js 22+, FFmpeg (vídeo em direto e captura), um broker MQTT (Mosquitto).")
QUICK_CODE = [
    ("npm install", T("dependencies | dependencias | Abhängigkeiten | dépendances | dipendenze | 依存関係 | 依赖 | dependências")),
    ("npm run typecheck", "tsc --noEmit"),
    ("npm test", T("NTESTS tests: unit and full HTTP integration | NTESTS pruebas: unitarias e integración HTTP completa | NTESTS Tests: Unit und volle HTTP-Integration | NTESTS tests : unitaires et intégration HTTP complète | NTESTS test: unitari e integrazione HTTP completa | NTESTS 件：単体と完全な HTTP 結合 | NTESTS 项：单元与完整 HTTP 集成 | NTESTS testes: unitários e integração HTTP completa".replace("NTESTS", NT))),
    ("npm run build", "dist/server.mjs"),
    (".\\run.bat   (run.sh)", T("development server with hot reload | servidor de desarrollo con recarga en caliente | Entwicklungsserver mit Hot-Reload | serveur de développement avec rechargement à chaud | server di sviluppo con ricarica a caldo | ホットリロード付き開発サーバー | 带热重载的开发服务器 | servidor de desenvolvimento com recarga a quente")),
]
INSTALL = P("To install it on the CM5 test bench (isolated from every other project, own user, own ports) see [ARMOR-DEVOPS](https://github.com/JuanenRac/ARMOR-DEVOPS).",
            "Para instalarlo en el banco de la CM5 (aislado de todo otro proyecto, con usuario y puertos propios) mira [ARMOR-DEVOPS](https://github.com/JuanenRac/ARMOR-DEVOPS).",
            "Zur Installation auf dem CM5-Prüfstand (isoliert von jedem anderen Projekt, eigener Benutzer, eigene Ports) siehe [ARMOR-DEVOPS](https://github.com/JuanenRac/ARMOR-DEVOPS).",
            "Pour l'installer sur le banc d'essai CM5 (isolé de tout autre projet, utilisateur et ports propres), voir [ARMOR-DEVOPS](https://github.com/JuanenRac/ARMOR-DEVOPS).",
            "Per installarlo sul banco di prova CM5 (isolato da ogni altro progetto, utente e porte proprie) vedi [ARMOR-DEVOPS](https://github.com/JuanenRac/ARMOR-DEVOPS).",
            "CM5 テストベンチへのインストール（他のプロジェクトから分離、専用ユーザーと専用ポート）は [ARMOR-DEVOPS](https://github.com/JuanenRac/ARMOR-DEVOPS) を参照してください。",
            "在 CM5 测试台上安装（与其他项目隔离，独立用户和端口）请见 [ARMOR-DEVOPS](https://github.com/JuanenRac/ARMOR-DEVOPS)。",
            "Para o instalar na bancada do CM5 (isolado de qualquer outro projeto, com utilizador e portas próprios) veja [ARMOR-DEVOPS](https://github.com/JuanenRac/ARMOR-DEVOPS).")

TEST_ROWS = "TESTROWS"

BUILD = P("`npm run build` bundles the server into `dist/server.mjs` (the `Dockerfile` builds the container image from it). The version lives in `package.json`, in `armor.project.json` and in the README badge (read from the manifest); each version has its entry in [CHANGELOG.md](CHANGELOG.md). Releases are published on GitHub.",
          "`npm run build` empaqueta el servidor en `dist/server.mjs` (el `Dockerfile` construye la imagen de contenedor a partir de él). La versión vive en `package.json`, en `armor.project.json` y en la insignia del README (leída del manifiesto); cada versión tiene su entrada en [CHANGELOG.md](CHANGELOG.md). Las versiones se publican en GitHub.",
          "`npm run build` bündelt den Server in `dist/server.mjs` (das `Dockerfile` baut daraus das Container-Image). Die Version steht in `package.json`, in `armor.project.json` und im README-Badge (aus dem Manifest gelesen); jede Version hat ihren Eintrag in [CHANGELOG.md](CHANGELOG.md). Releases werden auf GitHub veröffentlicht.",
          "`npm run build` regroupe le serveur dans `dist/server.mjs` (le `Dockerfile` en construit l'image de conteneur). La version se trouve dans `package.json`, dans `armor.project.json` et dans le badge du README (lu depuis le manifeste) ; chaque version a son entrée dans [CHANGELOG.md](CHANGELOG.md). Les versions sont publiées sur GitHub.",
          "`npm run build` impacchetta il server in `dist/server.mjs` (il `Dockerfile` ne costruisce l'immagine container). La versione risiede in `package.json`, in `armor.project.json` e nel badge del README (letto dal manifesto); ogni versione ha la sua voce in [CHANGELOG.md](CHANGELOG.md). Le versioni sono pubblicate su GitHub.",
          "`npm run build` はサーバーを `dist/server.mjs` にまとめます（`Dockerfile` がそこからコンテナイメージを作ります）。バージョンは `package.json`、`armor.project.json`、README のバッジ（マニフェストから読み取り）にあり、各バージョンには [CHANGELOG.md](CHANGELOG.md) にエントリーがあります。リリースは GitHub で公開されます。",
          "`npm run build` 把服务器打包为 `dist/server.mjs`（`Dockerfile` 据此构建容器镜像）。版本记录在 `package.json`、`armor.project.json` 和 README 徽章中（读取自清单）；每个版本在 [CHANGELOG.md](CHANGELOG.md) 中都有对应条目。发布版本发布在 GitHub 上。",
          "`npm run build` empacota o servidor em `dist/server.mjs` (o `Dockerfile` constrói a imagem de contentor a partir dele). A versão está em `package.json`, em `armor.project.json` e no emblema do README (lido do manifesto); cada versão tem a sua entrada em [CHANGELOG.md](CHANGELOG.md). As versões são publicadas no GitHub.")

TROUBLE = [
    ("`ARMOR_INGEST_TOKEN must be at least 24 characters`", T("a secret is missing or short | falta un secreto o es corto | ein Geheimnis fehlt oder ist kurz | un secret manque ou est court | manca un segreto o è corto | 秘密がない、または短い | 缺少密钥或密钥太短 | falta um segredo ou é curto"), T("set it (24+ characters); `run.sh` can generate them | defínelo (24+ caracteres); `run.sh` puede generarlos | setzen (24+ Zeichen); `run.sh` kann sie erzeugen | définissez-le (24+ caractères) ; `run.sh` peut les générer | impostalo (24+ caratteri); `run.sh` può generarli | 24 文字以上で設定（`run.sh` が生成可能） | 设置它（24 个以上字符）；`run.sh` 可以生成 | defina-o (24+ caracteres); `run.sh` pode gerá-los")),
    ("`... and ... must be different values`", T("two secrets are equal | dos secretos son iguales | zwei Geheimnisse sind gleich | deux secrets sont identiques | due segreti sono uguali | 2 つの秘密が同じ | 两个密钥相同 | dois segredos são iguais"), T("give each its own value | da a cada uno su valor | jedem einen eigenen Wert geben | donnez à chacun sa valeur | dai a ciascuno il suo valore | それぞれ別の値にする | 给每个密钥单独的值 | dê a cada um o seu valor")),
    ("`ARMOR_STUDIO_PASSWORD must be at least 12 characters when the server is reachable from the network`", T("`ARMOR_HOST` is not loopback | `ARMOR_HOST` no es loopback | `ARMOR_HOST` ist nicht Loopback | `ARMOR_HOST` n'est pas la boucle locale | `ARMOR_HOST` non è loopback | `ARMOR_HOST` がループバックでない | `ARMOR_HOST` 不是回环地址 | `ARMOR_HOST` não é loopback"), T("use a longer password, or keep `127.0.0.1` | usa una contraseña más larga, o deja `127.0.0.1` | ein längeres Passwort nehmen oder `127.0.0.1` lassen | utilisez un mot de passe plus long, ou gardez `127.0.0.1` | usa una password più lunga, o lascia `127.0.0.1` | もっと長いパスワードにするか `127.0.0.1` のままにする | 使用更长的密码，或保持 `127.0.0.1` | use uma palavra-passe mais longa, ou deixe `127.0.0.1`")),
    ("`ARMOR_MQTT_CA_FILE needs an mqtts:// address in ARMOR_MQTT_URL`", T("the authority file is set but the broker address is not `mqtts://` | se dio el fichero de autoridad pero la dirección del broker no es `mqtts://` | die Datei der Stelle ist gesetzt, die Broker-Adresse aber nicht `mqtts://` | le fichier d'autorité est donné mais l'adresse du broker n'est pas `mqtts://` | il file dell'autorità c'è ma l'indirizzo del broker non è `mqtts://` | 認証局ファイルはあるがブローカーのアドレスが `mqtts://` でない | 设置了机构文件但代理地址不是 `mqtts://` | o ficheiro da autoridade está definido mas o endereço do broker não é `mqtts://`"), T("use an `mqtts://` address, or remove the file | usa una dirección `mqtts://`, o quita el fichero | eine `mqtts://`-Adresse verwenden oder die Datei entfernen | utilisez une adresse `mqtts://`, ou retirez le fichier | usa un indirizzo `mqtts://`, o rimuovi il file | `mqtts://` のアドレスにするか、ファイルを外す | 使用 `mqtts://` 地址，或移除该文件 | use um endereço `mqtts://`, ou retire o ficheiro")),
    ("`TLS_CERT_PATH and TLS_KEY_PATH must both be set`", T("only one of the two is set | solo se dio uno de los dos | nur eines von beiden ist gesetzt | un seul des deux est donné | ne è impostato solo uno | 片方しか設定されていない | 只设置了其中一个 | só um dos dois está definido"), T("set both for HTTPS, or neither for plain HTTP | define ambos para HTTPS, o ninguno para HTTP | beide für HTTPS setzen oder keines für einfaches HTTP | donnez les deux pour HTTPS, ou aucun pour HTTP | imposta entrambi per HTTPS, o nessuno per HTTP | HTTPS なら両方、HTTP なら両方とも未設定 | 要 HTTPS 就两个都设，要明文 HTTP 就都不设 | defina ambos para HTTPS, ou nenhum para HTTP simples")),
    ("`voice_unavailable`  `voice_not_answering` (503)", T("the voice service is not reachable | el servicio de voz no responde | der Sprachdienst ist nicht erreichbar | le service vocal est injoignable | il servizio vocale non risponde | 音声サービスに届かない | 语音服务不可达 | o serviço de voz não responde"), T("start ARMOR-VOICE-AI and check `ARMOR_VOICE_URL` and its token | arranca ARMOR-VOICE-AI y revisa `ARMOR_VOICE_URL` y su token | ARMOR-VOICE-AI starten und `ARMOR_VOICE_URL` samt Token prüfen | démarrez ARMOR-VOICE-AI et vérifiez `ARMOR_VOICE_URL` et son jeton | avvia ARMOR-VOICE-AI e controlla `ARMOR_VOICE_URL` e il suo token | ARMOR-VOICE-AI を起動し `ARMOR_VOICE_URL` とトークンを確認 | 启动 ARMOR-VOICE-AI 并检查 `ARMOR_VOICE_URL` 及其令牌 | inicie o ARMOR-VOICE-AI e verifique `ARMOR_VOICE_URL` e o seu token")),
]

ROADMAP = P(
    "**Known limits today**\n\n* ONVIF has not met a real ONVIF camera, and nothing has run on a Jetson.\n* The solar, electrical, alarm-panel and touch-panel routes are tested with generated messages: only the radar board exists.\n* Push through Firebase has never run against a real Firebase project.\n* The node control orders and native TLS with a public certificate have not run on a real node.\n* No independent security review.\n\n**Next**\n\n* Try ONVIF with a real camera and the routes of the other nodes with their boards.\n* Try the push through a real Firebase project.",
    "**Límites conocidos hoy**\n\n* ONVIF no ha conocido una cámara ONVIF real, y nada ha corrido en una Jetson.\n* Las rutas solar, eléctrica, de panel de alarma y de panel táctil se prueban con mensajes generados: solo existe la placa del radar.\n* El push por Firebase nunca ha corrido contra un proyecto Firebase real.\n* Las órdenes de control de nodos y el TLS nativo con certificado público no han corrido en un nodo real.\n* Sin revisión de seguridad independiente.\n\n**Lo siguiente**\n\n* Probar ONVIF con una cámara real y las rutas de los demás nodos con sus placas.\n* Probar el push con un proyecto Firebase real.",
    "**Bekannte Grenzen heute**\n\n* ONVIF ist keiner echten ONVIF-Kamera begegnet, und nichts lief auf einem Jetson.\n* Die Routen für Solar, Elektro, Alarmpanel und Touchpanel werden mit erzeugten Nachrichten getestet: Es gibt nur die Radar-Platine.\n* Push über Firebase lief nie gegen ein echtes Firebase-Projekt.\n* Die Steuerbefehle für Knoten und natives TLS mit öffentlichem Zertifikat liefen nicht auf einem echten Knoten.\n* Keine unabhängige Sicherheitsprüfung.\n\n**Als Nächstes**\n\n* ONVIF mit einer echten Kamera und die Routen der anderen Knoten mit ihren Platinen ausprobieren.\n* Push über ein echtes Firebase-Projekt ausprobieren.",
    "**Limites connues aujourd'hui**\n\n* ONVIF n'a pas rencontré de vraie caméra ONVIF, et rien n'a tourné sur un Jetson.\n* Les routes solaire, électrique, tableau d'alarme et écran tactile sont testées avec des messages générés : seule la carte radar existe.\n* Le push via Firebase n'a jamais tourné contre un vrai projet Firebase.\n* Les ordres de contrôle des nœuds et le TLS natif avec certificat public n'ont pas tourné sur un vrai nœud.\n* Pas de revue de sécurité indépendante.\n\n**Prochainement**\n\n* Essayer ONVIF avec une vraie caméra et les routes des autres nœuds avec leurs cartes.\n* Essayer le push avec un vrai projet Firebase.",
    "**Limiti noti oggi**\n\n* ONVIF non ha incontrato una vera telecamera ONVIF e nulla ha girato su un Jetson.\n* Le rotte solare, elettrica, pannello allarme e pannello touch sono provate con messaggi generati: esiste solo la scheda radar.\n* Il push via Firebase non è mai stato provato con un vero progetto Firebase.\n* Gli ordini di controllo dei nodi e il TLS nativo con certificato pubblico non hanno girato su un nodo reale.\n* Nessuna revisione di sicurezza indipendente.\n\n**Prossimi passi**\n\n* Provare ONVIF con una telecamera reale e le rotte degli altri nodi con le loro schede.\n* Provare il push con un vero progetto Firebase.",
    "**現時点の既知の制限**\n\n* ONVIF は実際の ONVIF カメラに接続したことがなく、Jetson 上では何も動かしていません。\n* ソーラー、電気、アラームパネル、タッチパネルのルートは生成メッセージでテストしています。実機があるのはレーダー基板だけです。\n* Firebase 経由のプッシュは実際の Firebase プロジェクトで動かしたことがありません。\n* ノード制御オーダーと公開証明書でのネイティブ TLS は実機ノードで動かしていません。\n* 第三者によるセキュリティレビューはありません。\n\n**今後**\n\n* 実際のカメラで ONVIF を、他のノードのルートを各基板で試す。\n* 実際の Firebase プロジェクトでプッシュを試す。",
    "**当前已知限制**\n\n* ONVIF 从未接触过真实的 ONVIF 摄像头，也没有任何东西在 Jetson 上运行过。\n* 太阳能、电气、报警面板和触摸面板的路由用生成的消息测试：只有雷达的开发板存在。\n* 通过 Firebase 的推送从未对真实的 Firebase 项目运行过。\n* 节点控制指令以及使用公共证书的原生 TLS 没有在真实节点上运行过。\n* 没有独立的安全审查。\n\n**下一步**\n\n* 用真实摄像头试 ONVIF，并用其他节点的开发板试它们的路由。\n* 用真实的 Firebase 项目试推送。",
    "**Limites conhecidos hoje**\n\n* O ONVIF nunca encontrou uma câmara ONVIF real, e nada correu num Jetson.\n* As rotas solar, elétrica, de painel de alarme e de painel tátil são testadas com mensagens geradas: só existe a placa do radar.\n* O push pelo Firebase nunca correu contra um projeto Firebase real.\n* As ordens de controlo dos nós e o TLS nativo com certificado público não correram num nó real.\n* Sem revisão de segurança independente.\n\n**A seguir**\n\n* Experimentar o ONVIF com uma câmara real e as rotas dos outros nós com as suas placas.\n* Experimentar o push com um projeto Firebase real.")

DOCS = [
    P("[Route table](docs/ROUTES.md): every route and who may call it (generated)", "[Tabla de rutas](docs/ROUTES.md): cada ruta y quién puede llamarla (generada)", "[Routentabelle](docs/ROUTES.md): jede Route und wer sie aufrufen darf (erzeugt)", "[Table des routes](docs/ROUTES.md) : chaque route et qui peut l'appeler (générée)", "[Tabella delle rotte](docs/ROUTES.md): ogni rotta e chi può chiamarla (generata)", "[ルート表](docs/ROUTES.md)：全ルートと呼び出せる主体（生成）", "[路由表](docs/ROUTES.md)：每条路由及可调用者（自动生成）", "[Tabela de rotas](docs/ROUTES.md): cada rota e quem a pode chamar (gerada)"),
    P("[Environment](docs/ENVIRONMENT.md): every variable with its range (generated)", "[Entorno](docs/ENVIRONMENT.md): cada variable con su rango (generado)", "[Umgebung](docs/ENVIRONMENT.md): jede Variable mit Bereich (erzeugt)", "[Environnement](docs/ENVIRONMENT.md) : chaque variable avec sa plage (généré)", "[Ambiente](docs/ENVIRONMENT.md): ogni variabile con il suo intervallo (generato)", "[環境変数](docs/ENVIRONMENT.md)：全変数と範囲（生成）", "[环境变量](docs/ENVIRONMENT.md)：每个变量及其范围（自动生成）", "[Ambiente](docs/ENVIRONMENT.md): cada variável com o seu intervalo (gerado)"),
    P("[Integration](docs/INTEGRATION.md): how nodes, apps and services talk to the server", "[Integración](docs/INTEGRATION.md): cómo hablan nodos, apps y servicios con el servidor", "[Integration](docs/INTEGRATION.md): wie Knoten, Apps und Dienste mit dem Server sprechen", "[Intégration](docs/INTEGRATION.md) : comment nœuds, applications et services parlent au serveur", "[Integrazione](docs/INTEGRATION.md): come nodi, app e servizi parlano con il server", "[連携](docs/INTEGRATION.md)：ノード、アプリ、サービスとサーバーの通信", "[集成](docs/INTEGRATION.md)：节点、应用和服务如何与服务器通信", "[Integração](docs/INTEGRATION.md): como nós, apps e serviços falam com o servidor"),
    P("[Remote access](docs/REMOTE_ACCESS.md): second factor, policy and the house from outside", "[Acceso remoto](docs/REMOTE_ACCESS.md): segundo factor, política y la casa desde fuera", "[Fernzugriff](docs/REMOTE_ACCESS.md): zweiter Faktor, Richtlinie und das Haus von außen", "[Accès à distance](docs/REMOTE_ACCESS.md) : second facteur, politique et la maison vue de l'extérieur", "[Accesso remoto](docs/REMOTE_ACCESS.md): secondo fattore, politica e la casa da fuori", "[リモートアクセス](docs/REMOTE_ACCESS.md)：2 要素、方針、外部からの利用", "[远程访问](docs/REMOTE_ACCESS.md)：第二因素、策略与从屋外访问", "[Acesso remoto](docs/REMOTE_ACCESS.md): segundo fator, política e a casa vista de fora"),
    P("[Camera and media gateway](docs/CAMERA_MEDIA_GATEWAY.md): the vault, PTZ, relay and evidence", "[Pasarela de cámaras y medios](docs/CAMERA_MEDIA_GATEWAY.md): la caja fuerte, PTZ, relé y evidencias", "[Kamera- und Medien-Gateway](docs/CAMERA_MEDIA_GATEWAY.md): Tresor, PTZ, Relais und Beweise", "[Passerelle caméras et médias](docs/CAMERA_MEDIA_GATEWAY.md) : coffre, PTZ, relais et preuves", "[Gateway telecamere e media](docs/CAMERA_MEDIA_GATEWAY.md): cassaforte, PTZ, relè e prove", "[カメラ・メディアゲートウェイ](docs/CAMERA_MEDIA_GATEWAY.md)：金庫、PTZ、中継、証拠", "[摄像头与媒体网关](docs/CAMERA_MEDIA_GATEWAY.md)：保险库、PTZ、中继与证据", "[Gateway de câmaras e media](docs/CAMERA_MEDIA_GATEWAY.md): cofre, PTZ, relé e provas"),
    P("[Node firmware](docs/NODE_FIRMWARE.md): updating the nodes from Studio", "[Firmware de nodos](docs/NODE_FIRMWARE.md): actualizar los nodos desde Studio", "[Knoten-Firmware](docs/NODE_FIRMWARE.md): die Knoten aus Studio aktualisieren", "[Firmware des nœuds](docs/NODE_FIRMWARE.md) : mettre à jour les nœuds depuis Studio", "[Firmware dei nodi](docs/NODE_FIRMWARE.md): aggiornare i nodi da Studio", "[ノードのファームウェア](docs/NODE_FIRMWARE.md)：Studio からのノード更新", "[节点固件](docs/NODE_FIRMWARE.md)：从 Studio 更新节点", "[Firmware dos nós](docs/NODE_FIRMWARE.md): atualizar os nós a partir do Studio"),
    P("[State machine](docs/STATE_MACHINE.md): the life of a node and of an alarm", "[Máquina de estados](docs/STATE_MACHINE.md): la vida de un nodo y de una alarma", "[Zustandsautomat](docs/STATE_MACHINE.md): das Leben eines Knotens und eines Alarms", "[Machine à états](docs/STATE_MACHINE.md) : la vie d'un nœud et d'une alarme", "[Macchina a stati](docs/STATE_MACHINE.md): la vita di un nodo e di un allarme", "[状態機械](docs/STATE_MACHINE.md)：ノードとアラームのライフサイクル", "[状态机](docs/STATE_MACHINE.md)：节点与报警的生命周期", "[Máquina de estados](docs/STATE_MACHINE.md): a vida de um nó e de um alarme"),
]
TEST_TABLE = []


def build_lg(lg):
    bullets = "\n".join(f"* {b}" for b in L(lg, "bullets"))
    api = sec(lg, 1)
    body = {
        "overview": f"{L(lg, 'intro')}\n\n{bullets}",
        "role": f"{L(lg, 'fit')}\n\n{table(lg, 'talks', ROLE_TABLE)}",
        "architecture": arch(lg, "ARMOR-SERVER", "ARMOR-SERVER architecture: the nodes, cameras, consoles and services that call it, the server and its modules, and what it keeps and calls", DIAGRAM),
        "security": "\n".join(f"* {b}" for b in sec(lg, 0)) + "\n\n" + table(lg, "threat", SECURITY_ROWS) + "\n\n" + SECURITY_TAIL[lg],
        "interfaces": INTERFACES_LEAD[lg] + "\n\n" + table(lg, "route", ROUTES) + "\n\n" + "\n".join(f"* {b}" for b in api[:2]),
        "configuration": CONFIG_LEAD[lg] + "\n\n" + table(lg, "setting", CFG) + "\n\n" + "\n".join(f"* {b}" for b in sec(lg, 2)[1:3]),
        "quickstart": f"{QUICK_LEAD[lg]}\n\n" + code(lg, QUICK_CODE) + "\n\n" + INSTALL[lg],
        "testing": code(lg, [("npm run typecheck", "tsc --noEmit"), ("npm test", "tsx --test tests/*.test.ts"), "python -I tools/armor_ci_validate.py"]) + "\n\n" + TEST_TABLE_TEXT[lg],
        "build": BUILD[lg],
        "troubleshooting": table(lg, "trouble", TROUBLE),
        "structure": structure(lg, "ARMOR-SERVER", tree=TREE[lg]),
        "roadmap": ROADMAP[lg],
    }
    return text_for(lg, tagline=L(lg, "tagline"), honest=L(lg, "honest"), glance=GLANCE, status={k: fix(v) for k, v in LEGACY[lg]["status"].items()},
                    docs=DOCS, contributing_first=CONTRIB, body=body)


TEST_TABLE_TEXT = P(
    "`npm test` runs every file of `tests/` (99 files): unit tests of each module and a full HTTP integration suite against an isolated server (`tests/vertical-slice.test.ts`). `tests/conformance.test.ts` runs the shared vectors of ARMOR-COMMON and checks that **the routes the server registers are exactly the operations the OpenAPI file describes**, by method and path, and that every answer says which body it has; it is skipped when ARMOR-COMMON is not next to this repository. The TLS tests need `openssl` installed. GitHub Actions runs the A.R.M.O.R. baseline on every push and pull request: the validation of the manifest, version, changelog and README parity, then the project's own build and tests.",
    "`npm test` ejecuta cada fichero de `tests/` (99 ficheros): pruebas unitarias de cada módulo y una batería de integración HTTP completa contra un servidor aislado (`tests/vertical-slice.test.ts`). `tests/conformance.test.ts` ejecuta los vectores compartidos de ARMOR-COMMON y comprueba que **las rutas que registra el servidor son exactamente las operaciones que describe el fichero OpenAPI**, por método y ruta, y que cada respuesta dice qué cuerpo lleva; se salta si ARMOR-COMMON no está junto a este repositorio. Las pruebas de TLS necesitan `openssl` instalado. GitHub Actions ejecuta la base de A.R.M.O.R. en cada push y pull request: la validación del manifiesto, la versión, el registro de cambios y la paridad de los README, y luego la compilación y las pruebas del propio proyecto.",
    "`npm test` führt jede Datei in `tests/` aus (99 Dateien): Unit-Tests jedes Moduls und eine volle HTTP-Integrationssuite gegen einen isolierten Server (`tests/vertical-slice.test.ts`). `tests/conformance.test.ts` führt die gemeinsamen Vektoren von ARMOR-COMMON aus und prüft, dass **die vom Server registrierten Routen genau die Operationen sind, die die OpenAPI-Datei beschreibt**, nach Methode und Pfad, und dass jede Antwort sagt, welchen Inhalt sie hat; er wird übersprungen, wenn ARMOR-COMMON nicht neben diesem Repository liegt. Die TLS-Tests brauchen installiertes `openssl`. GitHub Actions führt bei jedem Push und Pull Request die A.R.M.O.R.-Basis aus: die Prüfung von Manifest, Version, Änderungsprotokoll und README-Parität, dann den eigenen Build und die eigenen Tests des Projekts.",
    "`npm test` exécute chaque fichier de `tests/` (99 fichiers) : tests unitaires de chaque module et une suite d'intégration HTTP complète contre un serveur isolé (`tests/vertical-slice.test.ts`). `tests/conformance.test.ts` exécute les vecteurs partagés d'ARMOR-COMMON et vérifie que **les routes enregistrées par le serveur sont exactement les opérations décrites par le fichier OpenAPI**, par méthode et chemin, et que chaque réponse dit quel corps elle porte ; il est ignoré si ARMOR-COMMON n'est pas à côté de ce dépôt. Les tests TLS demandent `openssl` installé. GitHub Actions exécute la base A.R.M.O.R. à chaque push et pull request : la validation du manifeste, de la version, du journal des modifications et de la parité des README, puis le build et les tests propres au projet.",
    "`npm test` esegue ogni file di `tests/` (99 file): test unitari di ogni modulo e una suite di integrazione HTTP completa contro un server isolato (`tests/vertical-slice.test.ts`). `tests/conformance.test.ts` esegue i vettori condivisi di ARMOR-COMMON e verifica che **le rotte registrate dal server siano esattamente le operazioni descritte dal file OpenAPI**, per metodo e percorso, e che ogni risposta dica quale corpo ha; viene saltato se ARMOR-COMMON non è accanto a questo repository. I test TLS richiedono `openssl` installato. GitHub Actions esegue la base A.R.M.O.R. a ogni push e pull request: la validazione di manifesto, versione, registro delle modifiche e parità dei README, poi la compilazione e i test del progetto.",
    "`npm test` は `tests/` の全ファイル（99 個）を実行します：各モジュールの単体テストと、隔離したサーバーに対する完全な HTTP 結合テスト（`tests/vertical-slice.test.ts`）。`tests/conformance.test.ts` は ARMOR-COMMON の共有ベクターを実行し、**サーバーが登録するルートが OpenAPI の記述する操作と（メソッドとパスで）完全に一致すること**、各応答が本文の種類を示していることを確認します。ARMOR-COMMON がこのリポジトリの隣にないとスキップされます。TLS のテストには `openssl` が必要です。GitHub Actions は push と pull request のたびに A.R.M.O.R. の基本検査（マニフェスト、バージョン、変更履歴、README の一致）と、プロジェクト自身のビルドとテストを実行します。",
    "`npm test` 运行 `tests/` 的每个文件（99 个）：各模块的单元测试，以及针对隔离服务器的完整 HTTP 集成套件（`tests/vertical-slice.test.ts`）。`tests/conformance.test.ts` 运行 ARMOR-COMMON 的共享向量，并检查**服务器注册的路由与 OpenAPI 文件描述的操作（按方法和路径）完全一致**，以及每个响应都说明其请求体类型；ARMOR-COMMON 不在本仓库旁边时会跳过。TLS 测试需要安装 `openssl`。GitHub Actions 在每次推送和拉取请求时运行 A.R.M.O.R. 基线：清单、版本、更新日志和 README 一致性的校验，然后是项目自身的构建和测试。",
    "`npm test` executa cada ficheiro de `tests/` (99 ficheiros): testes unitários de cada módulo e uma bateria de integração HTTP completa contra um servidor isolado (`tests/vertical-slice.test.ts`). `tests/conformance.test.ts` executa os vetores partilhados do ARMOR-COMMON e verifica que **as rotas que o servidor regista são exatamente as operações que o ficheiro OpenAPI descreve**, por método e caminho, e que cada resposta diz que corpo tem; é saltado se o ARMOR-COMMON não estiver ao lado deste repositório. Os testes de TLS precisam de `openssl` instalado. O GitHub Actions executa a base do A.R.M.O.R. em cada push e pull request: a validação do manifesto, da versão, do registo de alterações e da paridade dos README, e depois a compilação e os testes do próprio projeto.")

TEXT = {lg: build_lg(lg) for lg in LGS}
