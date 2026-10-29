# The facts that do not depend on the language, and the words of every language, of ARMOR-STUDIO, in the universal README layout.
# Copyright (C) 2026 JuanenRac (Electro Hobby 3D). GPL-3.0-or-later.
from readme_src._kit import *  # noqa: F401,F403

FACTS = {'emoji': '🎛️',
 'layout': 'universal',
 'license_badge': 'License-GPL%203.0--or--later-blue',
 'status': [['software', 'green'], ['tests', 'green'], ['ui', 'yellow'], ['hardware', 'yellow'], ['security', 'yellow'], ['integration', 'yellow'], ['docs', 'green']],
 'badges': [['Language', 'TypeScript', '3178c6'], ['UI', 'React%2019', '61dafb'], ['Languages', '8', '00E5FF'], ['Tests', '990%20passing', '2ea44f']]}

# the sentences of the previous layout that the new one keeps (already written in the eight languages)
LEGACY = {'en': {'tagline': 'Operations and design console: cameras, radar, alarms, energy, the local network, evidence, the site plan and the upkeep of the installation',
        'status': {'software': 'The console runs in daily use against the real server of the CM5 test bench.',
                   'tests': '990 unit tests pass (`npm test`) and the browser tests run: settings, camera merging, the solar charts, the geometry and checks of the '
                            "designers, the alarm announcer, the assistant's dictionary and every menu in the eight languages.",
                   'ui': 'Live video and PTZ are not proven against every possible camera, there has been no formal accessibility or usability review, and the pictures '
                         'of the Help are made with example data.',
                   'hardware': 'It is used daily with the real server, real IP cameras and a real radar node; the solar, electrical, alarm-panel and touch-panel menus '
                               'wait for real nodes.',
                   'security': 'Sessions, roles and the refusal of camera logins in addresses are covered by tests; there has been no independent review.',
                   'integration': 'While the server cannot be reached Studio shows demonstration data and says so in the top bar.',
                   'docs': 'Eight languages, the in-app Help and guided tours, the security notes and the changelog are up to date.'},
        'honest': 'Studio talks to [ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER) and is covered by 990 unit tests (settings parsing, camera merging, the '
                  "arithmetic of the solar charts, the geometry and checks of the designers, the alarm announcer, the assistant's dictionary, every menu rendered in the "
                  'eight languages, the static host) and by browser tests. It runs in daily use against the CM5 test bench with the real server, real IP cameras and a '
                  'radar node on its board; the pictures of the Help are made with example data. What has **not** been proven is live video and PTZ against every '
                  'possible camera, the solar, electrical, alarm-panel and touch-panel menus with real equipment (only the radar node exists) and a formal accessibility '
                  'or usability review. While the server cannot be reached Studio shows demonstration data and says so in the top bar.',
        'bullets': ['**Overview and system:** the state of the perimeter, a tile for every part (alarm panels, radar, cameras, devices, energy, network, server), a live '
                    'map of the design with every device and alarm, and what needs attention, all on one screen with no scrolling; a system page and an audit trail for '
                    'an administrator.',
                    '**Camera monitor:** 1, 2, 4, 6, 8, 9, 12 or 16 tiles that fit their frame (16:9, the whole matrix visible, no cropping), a maximized view with a '
                    'bounded PTZ pad, snapshot and MP4 record; a **record library** to filter, preview, play, protect and delete evidence and to download a **proof of '
                    'custody**.',
                    '**Alarms:** what needs a person right now, with acknowledge and the closed record; a **check before arming** and a PIN to disarm; alarms drawn on '
                    'the live map; a sound for every severity, a spoken voice with its own styles (plain, action hero, dark lord, theatrical) that also says when '
                    'something connects, pop-ups, a mute button beside Help, and an optional jump to the right menu.',
                    '**Devices and automations:** smoke, gas, flood, door, window, motion, climate, plug, light, siren, lock, shutter, gate, garage-door and '
                    'water-heater devices over Wi-Fi, Zigbee, Bluetooth or a wire (presets for Zigbee2MQTT, Tasmota and Shelly); rules from any alarm source, with '
                    'thresholds, that switch devices when something happens; a big arm / disarm button.',
                    '**Alarm panels and the Alarm Designer:** the state of every ARMOR-NODE-ALARM node, its zones and events, the Zigbee sensors tied to the zones, and '
                    "a designer where you draw the house's alarm (panels, contacts, motion, smoke, gas and flood detectors, sirens, keypads, wiring and radio links) and "
                    'tie each drawn element to a real zone.',
                    '**Solar and electrical energy:** the *Inverters* menu draws the house as an animated energy flow with gauges, readings and history charts; '
                    "*Batteries* shows each stack with its capacities, each module and every cell; *Electrical* shows the grid input, each channel and the meters' "
                    'alarms; in both you declare your equipment (Voltronic, MPP Solar, Pylontech, ANT-BMS…) and a *Show example readings* button lets you try the menu '
                    'first.',
                    "**Electrical Designer:** draw the house's electrical diagram (grid, meter, protections, transfer switches, distribution, PV, inverters, batteries "
                    'and loads, AC and DC), tie it to the solar devices the server reads to see live values, and let the checks review it (two sources on one line, '
                    'breakers and cables against the current…).',
                    '**Radar:** a live map drawn from your site design with the targets each radar reports, their recent path and the **zones of the picture to '
                    "ignore**; live node state, silent nodes shown as *stale*; each node's own panel one click away.",
                    '**Site Designer:** draw the terrain, buildings of several floors with five kinds of roof, doors, windows, lamps, chimneys, solar panels, masts, '
                    'roads and paths, then cameras and radars anywhere; a CAD-style 2D plan and an orbiting, floor-by-floor 3D view; undo and redo; versions of the '
                    'design.',
                    "**Local network:** the *Network* menu shows what the ARMOR-NETWORK node reports (devices, outages, the internet's state and the **public address** "
                    'with the provider and the place), lets you name, hide and watch devices, order a sweep, a ping or an inspection with a login you give, and the '
                    '*Network Designer* draws it.',
                    '**Automatic capture:** in *Configuration > Automatic capture*, photos and video taken by themselves when a camera sees something while the system '
                    "is armed (how many photos, how often, how long a clip), and the picture's zones to ignore drawn on the camera's frame.",
                    '**Node firmware and updates:** *Node firmware* updates the field nodes one by one, with a bar for the whole job and for every node, and keeps its '
                    "state if an alarm takes you to another menu; *Updates* installs Studio's and the server's own new versions from GitHub (showing the release notes "
                    "of the new version), the operating system's updates and an optional maintenance console.",
                    '**Configuration in groups:** General and Preferences; Users, Notifications and Automatic capture; Node firmware and Updates; Server, Services, MQTT '
                    'broker, Settings files, Installation and Console; each menu of the sidebar is also in foldable groups (Monitor, Security, Energy, House and '
                    'network, Design, Administration).',
                    '**Eight languages** (English, Spanish, German, French, Italian, Japanese, Chinese and Portuguese) and eleven themes, the default one called '
                    '*Armor*; language, theme and the weather place follow the account, not the browser. Roles: an administrator, an operator and a **viewer** who only '
                    'looks.',
                    '**A Help that knows the whole system:** a book with four levels of detail and a picture with example data of each main menu, a step-by-step tour '
                    'for every menu that goes control by control (what each button does, what to expect and the usual mistakes) with its own guide mascot and voice, a '
                    'Help that explains the field nodes in depth (set-up Wi-Fi, access point and station, Bluetooth PIN, firmware slots with rollback, signed updates, '
                    'the panel from outside), tooltips on everything, and an **assistant** (a mascot you can drag anywhere, pin where you want and ask in writing) with '
                    'a dictionary in eight languages and a bubble that opens on the side that has room. The menus where you are working stay open while you visit '
                    'another one.',
                    '**Outside access with choices, not files:** in Security an administrator sets up the WireGuard VPN, adds a phone by scanning a QR code, keeps a '
                    'name that follows the house (DuckDNS, Cloudflare or any address to call) and registers the nodes whose own panel can be opened from outside through '
                    'the server, comparing the certificate fingerprint before trusting it; every step explains itself in the eight languages and asks for the password '
                    'again when it is done from outside.',
                    '**Reaching the house from outside, step by step:** in Configuration > Security a guide of six steps shows whether the machine can do it, the VPN '
                    'exists, the house has a name, the port is open on the router and the phone is added, and how to try it from mobile data; the Security tab is laid '
                    'out in three titled sections.',
                    "**Broker encryption card:** Configuration > Broker shows whether the server's link to the broker is encrypted and the fingerprint of the "
                    "installation's own authority it trusts; nothing alarming is shown when the link is plain, because that is the default.",
                    '**Node health and arming modes:** System has a card with the health report of every node (uptime, why it restarted, memory, link and signal, broker '
                    'connections, last error, history and restarts) and Alarm panels has a mode picker (Away, Home, Night and your own) with an editor for the modes, '
                    'all in the eight languages with help, tour steps and assistant answers.',
                    "**Sign-in for password managers and a History with tabs:** the sign-in is a real form that the browser's or system's password manager can save and "
                    'fill, with an optional "Remember me" that keeps only the user name (never the password) and a note that says so; the History has the tabs All, '
                    'Alarms, Connections, Devices, System and Settings, with the list of every device and app that connects to the server (last seen, open sessions, '
                    'sign-ins and refusals) and the events of the nodes, the broker, services, updates and arming. Addresses are shown to administrators only.',
                    "**Battery maintenance (Configuration, administrators):** a four-step wizard - battery and operation, values, confirmation with the battery's serial "
                    'number typed, result - to change what a Pylontech battery keeps; limits in volts and degrees a whole group at a time, a firmware file read before '
                    'it is sent, the battery read before and after with the difference and the transcript, and an output put back as it was.',
                    '**Control of the nodes from the node health card:** each node has a menu (Restart, Pause or Resume, Standby - work off, still connected - or Power '
                    'on, Identify, Diagnostics, Maintenance on or off) and the card has the group actions Restart all (all at once, or one after another with the alarm '
                    "panel last), Pause all, Standby all and Resume all. The node's name (or the word RESTART, PAUSE or STANDBY for all) is typed again and a fresh "
                    'proof of identity is asked for; chips follow each node (sent, acknowledged, offline, back, applied) and show Paused, Standby since and by whom, and '
                    'Maintenance; and the warnings say when an alarm panel or a radar paused or on standby leaves the house unprotected. There is no factory reset, no '
                    'erase and no deep sleep.',
                    "**Live status:** Studio listens to the server's live channel (a WebSocket) and shows an alarm, an arming or a node coming back at once, asking for "
                    'the status only every twenty seconds as a safety net while the channel is open; the bottom bar says *Live*. The Alarm, Electrical and Network '
                    'designers answer F (fit), plus and minus (zoom) and Ctrl+D (duplicate) besides their other keys.'],
        'intro': "**ARMOR-STUDIO** is the operator's console. It never holds a camera password, an RTSP address or a token: it signs in to the server with a username "
                 'and password, receives an 8-hour **HttpOnly** session, and everything privileged travels through that session.',
        'sections': [{'icon': '🔒',
                      'title': 'Security model',
                      'bullets': ['**No secrets in the browser.** Camera passwords are entered once, sent to the server and shown afterwards only as a masked "stored" '
                                  'state. Site exports drop usernames and credential flags.',
                                  '**Stored settings are untrusted input.** They are parsed value by value: an invalid origin, theme, language or shape is dropped, '
                                  'positions are clamped and lists are capped.',
                                  "**No third-party requests.** Fonts are local stacks; the static host sends `Content-Security-Policy: default-src 'self'` limited to "
                                  "the configured server, `frame-ancestors 'none'`, `nosniff` and `no-referrer`.",
                                  'Live video is shown only through a stream address the server issues to an operator.'],
                      'raw': '* **No secrets in the browser.** Camera passwords are entered once, sent to the server and shown afterwards only as a masked "stored" '
                             'state. Site exports drop usernames and credential flags.\n'
                             '* **Stored settings are untrusted input.** They are parsed value by value: an invalid origin, theme, language or shape is dropped, '
                             'positions are clamped and lists are capped.\n'
                             "* **No third-party requests.** Fonts are local stacks; the static host sends `Content-Security-Policy: default-src 'self'` limited to the "
                             "configured server, `frame-ancestors 'none'`, `nosniff` and `no-referrer`.\n"
                             '* Live video is shown only through a stream address the server issues to an operator.'}],
        'note': '`tools/serve.mjs` reads `ARMOR_STUDIO_HOST` (default `127.0.0.1`), `ARMOR_STUDIO_PORT` (`5178`), `ARMOR_STUDIO_DIST` and `ARMOR_SERVER_ORIGIN`. To '
                'install the whole stack on the CM5 test bench see [ARMOR-DEVOPS](https://github.com/JuanenRac/ARMOR-DEVOPS).',
        'fit': "Studio is the operator's window on the whole system. It never talks to a node: everything goes through "
               "[ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER), which is the only thing that decides (the one exception is a link to each node's own panel). "
               "It is also where the site, the alarm, the electrical installation and the network are designed, where the nodes' firmware and the installation's own "
               'updates are driven from, and where the Help and the assistant live. The same server is used by '
               '[ARMOR-ANDROID-CONTROL](https://github.com/JuanenRac/ARMOR-ANDROID-CONTROL) on the phone.',
        'hardware': 'Used daily against the CM5 test bench (real server, real IP cameras, a real radar node); the solar, electrical, alarm-panel and touch-panel menus '
                    'wait for real nodes'},
 'es': {'tagline': 'Consola de operación y diseño: cámaras, radar, alarmas, energía, la red local, evidencias, el plano del sitio y el mantenimiento de la instalación',
        'status': {'software': 'La consola funciona a diario contra el servidor real del banco de pruebas CM5.',
                   'tests': 'Pasan 990 pruebas unitarias (`npm test`) y se ejecutan las pruebas de navegador: ajustes, fusión de cámaras, gráficas solares, geometría y '
                            'comprobaciones de los diseñadores, el anunciador de alarmas, el diccionario del asistente y cada menú en los ocho idiomas.',
                   'ui': 'El vídeo en vivo y el PTZ no están probados con todas las cámaras posibles, no ha habido una revisión formal de accesibilidad o usabilidad, y '
                         'las imágenes de la Ayuda se hacen con datos de ejemplo.',
                   'hardware': 'Se usa a diario con el servidor real, cámaras IP reales y un nodo radar real; los menús solar, eléctrico, de panel de alarma y de panel '
                               'táctil esperan nodos reales.',
                   'security': 'Las sesiones, los roles y el rechazo de credenciales de cámara en las direcciones están cubiertos por pruebas; no ha habido una revisión '
                               'independiente.',
                   'integration': 'Mientras no se puede alcanzar el servidor, Studio muestra datos de demostración y lo dice en la barra superior.',
                   'docs': 'Ocho idiomas, la Ayuda integrada y los recorridos guiados, las notas de seguridad y el historial de cambios están al día.'},
        'honest': 'Studio habla con [ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER) y está cubierto por 990 tests unitarios (lectura de ajustes, fusión de '
                  'cámaras, la aritmética de las gráficas solares, la geometría y las comprobaciones de los diseñadores, el anunciador de alarmas, el diccionario del '
                  'asistente, cada menú dibujado en los ocho idiomas, el servidor estático) y por pruebas en navegador. Funciona en uso diario contra el banco de '
                  'pruebas de la CM5 con el servidor real, cámaras IP reales y un nodo radar en su placa; las imágenes de la Ayuda se hacen con datos de ejemplo. Lo que '
                  '**no** se ha probado es el vídeo en directo y el PTZ con todas las cámaras posibles, los menús solar, eléctrico, de centrales de alarma y de panel '
                  'táctil con equipos reales (solo existe el nodo radar) y una revisión formal de accesibilidad o usabilidad. Mientras no se alcanza el servidor, Studio '
                  'muestra datos de demostración y lo dice en la barra superior.',
        'bullets': ['**Resumen y sistema:** el estado del perímetro, una tarjeta por cada parte (centrales de alarma, radar, cámaras, dispositivos, energía, red, '
                    'servidor), un mapa vivo del diseño con cada dispositivo y alarma, y lo que necesita atención, todo en una pantalla sin desplazamiento; una página '
                    'de sistema y un registro de auditoría para el administrador.',
                    '**Monitor de cámaras:** 1, 2, 4, 6, 8, 9, 12 o 16 teselas que se ajustan a su marco (16:9, toda la matriz visible, sin recortes), una vista '
                    'ampliada con mando PTZ acotado, captura y grabación MP4; una **biblioteca de grabaciones** para filtrar, previsualizar, reproducir, proteger y '
                    'borrar evidencias y descargar una **prueba de custodia**.',
                    '**Alarmas:** lo que necesita a una persona ahora, con reconocer y el registro cerrado; una **comprobación antes de armar** y un PIN para desarmar; '
                    'alarmas dibujadas en el mapa vivo; un sonido para cada gravedad, una voz hablada con sus propios estilos (neutro, héroe de acción, señor oscuro, '
                    'teatral) que también dice cuándo algo se conecta, avisos emergentes, un botón de silencio junto a la Ayuda y un salto opcional al menú adecuado.',
                    '**Dispositivos y automatizaciones:** humo, gas, inundación, puerta, ventana, movimiento, clima, enchufe, luz, sirena, cerradura, persiana, cancela, '
                    'puerta de garaje y calentador de agua por Wi-Fi, Zigbee, Bluetooth o cable (preajustes para Zigbee2MQTT, Tasmota y Shelly); reglas desde cualquier '
                    'fuente de alarma, con umbrales, que accionan dispositivos cuando algo ocurre; un botón grande de armar / desarmar.',
                    '**Centrales de alarma y el Diseñador de alarma:** el estado de cada nodo ARMOR-NODE-ALARM, sus zonas y eventos, los sensores Zigbee atados a las '
                    'zonas, y un diseñador donde dibujas la alarma de la casa (centrales, contactos, movimiento, detectores de humo, gas e inundación, sirenas, '
                    'teclados, cableado y enlaces de radio) y atas cada elemento dibujado a una zona real.',
                    '**Energía solar y eléctrica:** el menú *Inversores* dibuja la casa como un flujo de energía animado con relojes, lecturas y gráficas de historial; '
                    '*Baterías* muestra cada pila con sus capacidades, cada módulo y cada celda; *Eléctrico* muestra la entrada de red, cada canal y las alarmas de los '
                    'medidores; en ambos declaras tu equipo (Voltronic, MPP Solar, Pylontech, ANT-BMS…) y un botón *Mostrar lecturas de ejemplo* te deja probar el menú '
                    'antes.',
                    '**Diseñador eléctrico:** dibuja el esquema eléctrico de la casa (red, contador, protecciones, conmutadores, distribución, FV, inversores, baterías '
                    'y cargas, CA y CC), átalo a los dispositivos solares que lee el servidor para ver valores en vivo, y deja que las comprobaciones lo revisen (dos '
                    'fuentes en una línea, magnetotérmicos y cables frente a la corriente…).',
                    '**Radar:** un mapa vivo dibujado desde tu diseño del sitio con los objetivos que informa cada radar, su recorrido reciente y las **zonas de la '
                    'imagen que se ignoran**; estado vivo de los nodos, con los silenciosos como *obsoletos*; el panel propio de cada nodo a un clic.',
                    '**Diseñador del sitio:** dibuja el terreno, edificios de varias plantas con cinco tipos de tejado, puertas, ventanas, farolas, chimeneas, paneles '
                    'solares, mástiles, caminos y senderos, y después cámaras y radares donde quieras; un plano 2D estilo CAD y una vista 3D orbitable y por plantas; '
                    'deshacer y rehacer; versiones del diseño.',
                    '**Red local:** el menú *Red* muestra lo que informa el nodo ARMOR-NETWORK (dispositivos, cortes, el estado de internet y la **dirección pública** '
                    'con el proveedor y el lugar), te deja poner nombre, ocultar y vigilar dispositivos, ordenar un barrido, un ping o una inspección con un acceso que '
                    'das, y el *Diseñador de red* la dibuja.',
                    '**Captura automática:** en *Configuración > Captura automática*, fotos y vídeo hechos solos cuando una cámara ve algo con el sistema armado '
                    '(cuántas fotos, cada cuánto, cuánto dura un clip), y las zonas de la imagen que se ignoran dibujadas sobre el cuadro de la cámara.',
                    '**Firmware de nodos y actualizaciones:** *Firmware de nodos* actualiza los nodos de campo de uno en uno, con una barra para todo el trabajo y para '
                    'cada nodo, y conserva su estado si una alarma te lleva a otro menú; *Actualizaciones* instala las versiones nuevas de Studio y del servidor desde '
                    'GitHub (mostrando las novedades de la versión nueva), las del sistema operativo y una consola de mantenimiento opcional.',
                    '**Configuración en grupos:** General y Preferencias; Usuarios, Notificaciones y Captura automática; Firmware de nodos y Actualizaciones; Servidor, '
                    'Servicios, Broker MQTT, Ficheros de configuración, Instalación y Consola; y cada menú de la barra lateral también va en grupos plegables (Monitor, '
                    'Seguridad, Energía, Casa y red, Diseño, Administración).',
                    '**Ocho idiomas** (inglés, español, alemán, francés, italiano, japonés, chino y portugués) y once temas, el predeterminado llamado *Armor*; el '
                    'idioma, el tema y el lugar del tiempo siguen a la cuenta, no al navegador. Roles: administrador, operador y **viewer**, que solo mira.',
                    '**Una Ayuda que conoce todo el sistema:** un libro con cuatro niveles de detalle y una imagen con datos de ejemplo de cada menú principal, un '
                    'recorrido guiado paso a paso para cada menú que va control por control (qué hace cada botón, qué esperar y los errores habituales) con su propia '
                    'mascota y voz, una Ayuda que explica los nodos de campo a fondo (Wi-Fi de configuración, punto de acceso y estación, PIN de Bluetooth, ranuras de '
                    'firmware con vuelta atrás, actualizaciones firmadas, el panel desde fuera), ayudas emergentes en todo, y un **asistente** (una mascota que puedes '
                    'arrastrar a cualquier sitio, anclar donde quieras y a la que preguntar por escrito) con un diccionario en ocho idiomas y un globo que se abre en el '
                    'lado que tiene sitio. Los menús donde trabajas siguen abiertos mientras visitas otro.',
                    '**Acceso desde fuera con opciones, no archivos:** en Seguridad un administrador configura la VPN WireGuard, añade un móvil escaneando un código QR, '
                    'mantiene un nombre que sigue a la casa (DuckDNS, Cloudflare o cualquier dirección a la que llamar) y registra los nodos cuyo propio panel se puede '
                    'abrir desde fuera a través del servidor, comparando la huella del certificado antes de confiar en él; cada paso se explica solo en los ocho idiomas '
                    'y pide la contraseña de nuevo cuando se hace desde fuera.',
                    '**Llegar a casa desde fuera, paso a paso:** en Configuración > Seguridad una guía de seis pasos muestra si la máquina puede, si la VPN existe, si '
                    'la casa tiene nombre, si el puerto está abierto en el router y si el móvil está añadido, y cómo probarlo con datos móviles; la pestaña Seguridad '
                    'está ordenada en tres secciones con título.',
                    '**Tarjeta de cifrado del broker:** Configuración > Broker muestra si el enlace del servidor con el broker está cifrado y la huella de la autoridad '
                    'propia de la instalación en la que confía; no se muestra nada alarmante cuando el enlace es sin cifrar, porque es lo habitual.',
                    '**Salud de los nodos y modos de armado:** Sistema tiene una tarjeta con el informe de salud de cada nodo (tiempo encendido, motivo del reinicio, '
                    'memoria, enlace y señal, conexiones al broker, último error, historial y reinicios) y Centrales de alarma tiene un selector de modo (Fuera, En '
                    'casa, Noche y los tuyos) con un editor de modos, todo en ocho idiomas con ayuda, pasos de guía y respuestas del asistente.',
                    '**Inicio de sesión para gestores de contraseñas y un Historial con pestañas:** el inicio de sesión es un formulario de verdad que el gestor de '
                    'contraseñas del navegador o del sistema puede guardar y rellenar, con un "Recordarme" opcional que guarda solo el nombre de usuario (nunca la '
                    'contraseña) y una nota que lo dice; el Historial tiene las pestañas Todo, Alarmas, Conexiones, Dispositivos, Sistema y Ajustes, con la lista de '
                    'cada dispositivo y app que se conecta al servidor (última vez, sesiones abiertas, inicios de sesión y rechazos) y los eventos de los nodos, el '
                    'broker, los servicios, las actualizaciones y el armado. Las direcciones solo las ven los administradores.',
                    '**Mantenimiento de baterías (Configuración, administradores):** un asistente de cuatro pasos - batería y operación, valores, confirmación '
                    'escribiendo el número de serie de la batería, resultado - para cambiar lo que guarda una batería Pylontech; límites en voltios y grados un grupo '
                    'entero cada vez, un archivo de firmware leído antes de enviarlo, la batería leída antes y después con la diferencia y la transcripción, y una '
                    'salida que se puede dejar como estaba.',
                    '**Control de los nodos desde la tarjeta de salud:** cada nodo tiene un menú (Reiniciar, Pausar o Reanudar, Poner en espera - trabajo apagado, sigue '
                    'conectado - o Encender, Identificar, Diagnóstico, Mantenimiento activado o desactivado) y la tarjeta tiene las acciones de grupo Reiniciar todos (a '
                    'la vez, o uno tras otro con la central de alarma la última), Pausar todos, Poner todos en espera y Reanudar todos. Se vuelve a escribir el nombre '
                    'del nodo (o la palabra RESTART, PAUSE o STANDBY para todos) y se pide una prueba de identidad nueva; unas etiquetas siguen a cada nodo (enviada, '
                    'recibida, sin conexión, de vuelta, aplicada) y muestran En pausa, En espera desde cuándo y por quién, y Mantenimiento; y los avisos dicen cuándo '
                    'una central de alarma o un radar en pausa o en espera dejan la casa sin proteger. No existe restablecimiento de fábrica, borrado ni sueño profundo.',
                    '**Estado en vivo:** Studio escucha el canal en vivo del servidor (un WebSocket) y muestra al instante una alarma, un armado o un nodo que vuelve, y '
                    'pregunta el estado solo cada veinte segundos como red de seguridad mientras el canal está abierto; la barra inferior dice *En vivo*. Los '
                    'diseñadores de alarma, eléctrico y de red responden a F (encajar), más y menos (zoom) y Ctrl+D (duplicar) además de sus otras teclas.'],
        'intro': '**ARMOR-STUDIO** es la consola del operador. Nunca guarda una contraseña de cámara, una dirección RTSP ni un token: inicia sesión en el servidor con '
                 'usuario y contraseña, recibe una sesión **HttpOnly** de 8 horas y todo lo privilegiado viaja por esa sesión.',
        'sections': [{'icon': '🔒',
                      'title': 'Modelo de seguridad',
                      'bullets': ['**Ningún secreto en el navegador.** Las contraseñas de las cámaras se teclean una vez, se envían al servidor y después solo se ven '
                                  'como un estado "guardada" enmascarado. Las exportaciones del sitio omiten usuarios e indicadores de credenciales.',
                                  '**Los ajustes guardados son entrada no fiable.** Se leen valor a valor: un origen, tema, idioma o forma no válidos se descartan, las '
                                  'posiciones se acotan y las listas se limitan.',
                                  "**Ninguna petición a terceros.** Las fuentes son locales; el servidor estático envía `Content-Security-Policy: default-src 'self'` "
                                  "limitada al servidor configurado, `frame-ancestors 'none'`, `nosniff` y `no-referrer`.",
                                  'El vídeo en vivo solo se muestra mediante una dirección de emisión que el servidor entrega a un operador.'],
                      'raw': '* **Ningún secreto en el navegador.** Las contraseñas de las cámaras se teclean una vez, se envían al servidor y después solo se ven como '
                             'un estado "guardada" enmascarado. Las exportaciones del sitio omiten usuarios e indicadores de credenciales.\n'
                             '* **Los ajustes guardados son entrada no fiable.** Se leen valor a valor: un origen, tema, idioma o forma no válidos se descartan, las '
                             'posiciones se acotan y las listas se limitan.\n'
                             "* **Ninguna petición a terceros.** Las fuentes son locales; el servidor estático envía `Content-Security-Policy: default-src 'self'` "
                             "limitada al servidor configurado, `frame-ancestors 'none'`, `nosniff` y `no-referrer`.\n"
                             '* El vídeo en vivo solo se muestra mediante una dirección de emisión que el servidor entrega a un operador.'}],
        'note': '`tools/serve.mjs` lee `ARMOR_STUDIO_HOST` (por defecto `127.0.0.1`), `ARMOR_STUDIO_PORT` (`5178`), `ARMOR_STUDIO_DIST` y `ARMOR_SERVER_ORIGIN`. Para '
                'instalar toda la pila en el banco de pruebas de la CM5 véase [ARMOR-DEVOPS](https://github.com/JuanenRac/ARMOR-DEVOPS).',
        'fit': 'Studio es la ventana del operador a todo el sistema. Nunca habla con un nodo: todo pasa por [ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER), '
               'que es lo único que decide (la única excepción es un enlace al panel propio de cada nodo). También es donde se diseñan el sitio, la alarma, la '
               'instalación eléctrica y la red, desde donde se gobiernan el firmware de los nodos y las actualizaciones de la propia instalación, y donde viven la Ayuda '
               'y el asistente. El mismo servidor lo usa [ARMOR-ANDROID-CONTROL](https://github.com/JuanenRac/ARMOR-ANDROID-CONTROL) en el móvil.',
        'hardware': 'Usado a diario contra el banco de pruebas de la CM5 (servidor real, cámaras IP reales, un nodo radar real); los menús solar, eléctrico, de '
                    'centrales de alarma y de panel táctil esperan nodos reales',
        'requirements': ['Node.js 22+', 'un ARMOR-SERVER en marcha (si no, Studio muestra datos de demostración)']},
 'fr': {'tagline': "Console d'exploitation et de conception : caméras, radar, alarmes, énergie, réseau local, preuves, plan du site et entretien de l'installation",
        'status': {'software': "La console tourne au quotidien contre le vrai serveur du banc d'essai CM5.",
                   'tests': "990 tests unitaires réussissent (`npm test`) et les tests de navigateur s'exécutent : réglages, fusion des caméras, graphiques solaires, "
                            "géométrie et contrôles des concepteurs, annonceur d'alarmes, dictionnaire de l'assistant et chaque menu dans les huit langues.",
                   'ui': "La vidéo en direct et le PTZ ne sont pas prouvés avec toutes les caméras possibles, il n'y a pas eu de revue formelle d'accessibilité ou "
                         "d'utilisabilité, et les images de l'aide sont faites avec des données d'exemple.",
                   'hardware': 'Il est utilisé chaque jour avec le vrai serveur, de vraies caméras IP et un vrai nœud radar ; les menus solaire, électrique, de centrale '
                               "d'alarme et de panneau tactile attendent de vrais nœuds.",
                   'security': "Les sessions, les rôles et le refus des identifiants de caméra dans les adresses sont couverts par des tests ; il n'y a pas eu de revue "
                               'indépendante.',
                   'integration': 'Tant que le serveur est injoignable, Studio affiche des données de démonstration et le dit dans la barre du haut.',
                   'docs': "Huit langues, l'aide intégrée et les visites guidées, les notes de sécurité et le journal des modifications sont à jour."},
        'honest': 'Studio dialogue avec [ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER) et est couvert par 990 tests unitaires (lecture des réglages, fusion '
                  "des caméras, arithmétique des graphiques solaires, géométrie et vérifications des concepteurs, annonceur d'alarmes, dictionnaire de l'assistant, "
                  'chaque menu rendu dans les huit langues, hôte statique) et par des tests dans un navigateur. Il fonctionne en usage quotidien contre le banc de test '
                  "CM5 avec le vrai serveur, de vraies caméras IP et un nœud radar sur sa carte ; les images de l'Aide sont faites avec des données d'exemple. Ce qui "
                  "n'a **pas** été prouvé : la vidéo en direct et le PTZ avec toutes les caméras possibles, les menus solaire, électrique, centrales d'alarme et panneau "
                  "tactile avec du vrai matériel (seul le nœud radar existe) et une revue formelle d'accessibilité ou d'utilisabilité. Tant que le serveur est "
                  'injoignable, Studio affiche des données de démonstration et le dit dans la barre supérieure.',
        'bullets': ["**Aperçu et système :** l'état du périmètre, une tuile par partie (centrales d'alarme, radar, caméras, appareils, énergie, réseau, serveur), une "
                    'carte vivante du plan avec chaque appareil et alarme, et ce qui demande attention, le tout sur un seul écran sans défilement ; une page système et '
                    "un journal d'audit pour l'administrateur.",
                    '**Moniteur de caméras :** 1, 2, 4, 6, 8, 9, 12 ou 16 tuiles qui épousent leur cadre (16:9, toute la matrice visible, sans rognage), une vue '
                    "agrandie avec une télécommande PTZ bornée, capture et enregistrement MP4 ; une **bibliothèque d'enregistrements** pour filtrer, prévisualiser, "
                    'lire, protéger et supprimer des preuves et télécharger une **preuve de conservation**.',
                    '**Alarmes :** ce qui demande une personne tout de suite, avec acquittement et dossier clos ; une **vérification avant armement** et un PIN pour '
                    'désarmer ; des alarmes dessinées sur la carte vivante ; un son pour chaque gravité, une voix parlée avec ses propres styles (neutre, héros '
                    "d'action, seigneur des ténèbres, théâtral) qui dit aussi quand quelque chose se connecte, des fenêtres d'alerte, un bouton muet à côté de l'Aide et "
                    'un saut optionnel vers le bon menu.',
                    '**Appareils et automatisations :** fumée, gaz, inondation, porte, fenêtre, mouvement, climat, prise, lumière, sirène, serrure, volet, portail, '
                    'porte de garage et chauffe-eau en Wi-Fi, Zigbee, Bluetooth ou filaire (préréglages Zigbee2MQTT, Tasmota et Shelly) ; des règles depuis toute source '
                    "d'alarme, avec seuils, qui actionnent des appareils quand quelque chose arrive ; un grand bouton armer / désarmer.",
                    "**Centrales d'alarme et Concepteur d'alarme :** l'état de chaque nœud ARMOR-NODE-ALARM, ses zones et événements, les capteurs Zigbee liés aux "
                    "zones, et un concepteur où vous dessinez l'alarme de la maison (centrales, contacts, mouvement, détecteurs de fumée, gaz et inondation, sirènes, "
                    'claviers, câblage et liaisons radio) et liez chaque élément dessiné à une vraie zone.',
                    "**Énergie solaire et électrique :** le menu *Onduleurs* dessine la maison comme un flux d'énergie animé avec cadrans, mesures et courbes "
                    "d'historique ; *Batteries* montre chaque bloc avec ses capacités, chaque module et chaque cellule ; *Électrique* montre l'entrée réseau, chaque "
                    'canal et les alarmes des compteurs ; dans les deux vous déclarez votre matériel (Voltronic, MPP Solar, Pylontech, ANT-BMS…) et un bouton *Afficher '
                    "des mesures d'exemple* permet d'essayer le menu d'abord.",
                    '**Concepteur électrique :** dessinez le schéma électrique de la maison (réseau, compteur, protections, inverseurs, distribution, PV, onduleurs, '
                    'batteries et charges, AC et DC), liez-le aux appareils solaires que lit le serveur pour voir les valeurs en direct, et laissez les vérifications le '
                    'relire (deux sources sur une ligne, disjoncteurs et câbles face au courant…).',
                    "**Radar :** une carte vivante tracée d'après votre plan du site avec les cibles que rapporte chaque radar, leur trajet récent et les **zones de "
                    "l'image à ignorer** ; état vivant des nœuds, les silencieux affichés *périmés* ; le panneau propre de chaque nœud à un clic.",
                    '**Concepteur du site :** dessinez le terrain, des bâtiments de plusieurs étages avec cinq types de toit, portes, fenêtres, lampadaires, cheminées, '
                    'panneaux solaires, mâts, routes et chemins, puis caméras et radars où vous voulez ; un plan 2D de type CAO et une vue 3D orbitale étage par étage ; '
                    'annuler et rétablir ; versions du plan.',
                    "**Réseau local :** le menu *Réseau* montre ce que rapporte le nœud ARMOR-NETWORK (appareils, coupures, état d'internet et **adresse publique** avec "
                    "le fournisseur et le lieu), permet de nommer, masquer et surveiller des appareils, d'ordonner un balayage, un ping ou une inspection avec un "
                    'identifiant que vous donnez, et le *Concepteur réseau* le dessine.',
                    '**Capture automatique :** dans *Configuration > Capture automatique*, photos et vidéo prises seules quand une caméra voit quelque chose système '
                    "armé (combien de photos, à quel rythme, durée d'un clip), et les zones de l'image à ignorer dessinées sur le cadre de la caméra.",
                    '**Firmware des nœuds et mises à jour :** *Firmware des nœuds* met à jour les nœuds de terrain un par un, avec une barre pour tout le travail et '
                    'pour chaque nœud, et garde son état si une alarme vous emmène dans un autre menu ; *Mises à jour* installe les nouvelles versions de Studio et du '
                    "serveur depuis GitHub (en montrant les nouveautés de la version), celles du système d'exploitation et une console de maintenance optionnelle.",
                    '**Configuration en groupes :** Général et Préférences ; Utilisateurs, Notifications et Capture automatique ; Firmware des nœuds et Mises à jour ; '
                    'Serveur, Services, Broker MQTT, Fichiers de réglages, Installation et Console ; et chaque menu de la barre latérale est aussi en groupes repliables '
                    '(Surveillance, Sécurité, Énergie, Maison et réseau, Conception, Administration).',
                    "**Huit langues** (anglais, espagnol, allemand, français, italien, japonais, chinois et portugais) et onze thèmes, celui par défaut s'appelant "
                    '*Armor* ; la langue, le thème et le lieu météo suivent le compte, pas le navigateur. Rôles : administrateur, opérateur et **viewer**, qui ne fait '
                    'que regarder.',
                    "**Une Aide qui connaît tout le système :** un livre à quatre niveaux de détail avec une image de données d'exemple de chaque menu principal, une "
                    "visite guidée pas à pas pour chaque menu qui va contrôle par contrôle (ce que fait chaque bouton, à quoi s'attendre et les erreurs courantes) avec "
                    "sa propre mascotte et sa voix, une Aide qui explique en détail les nœuds de terrain (Wi-Fi de configuration, point d'accès et station, PIN "
                    "Bluetooth, emplacements de firmware avec retour arrière, mises à jour signées, le panneau depuis l'extérieur), des bulles d'aide partout, et un "
                    "**assistant** (une mascotte que vous pouvez glisser n'importe où, épingler où vous voulez et interroger par écrit) avec un dictionnaire en huit "
                    "langues et une bulle qui s'ouvre du côté qui a de la place. Les menus où vous travaillez restent ouverts pendant que vous en visitez un autre.",
                    '**Accès extérieur avec des choix, pas des fichiers :** dans Sécurité, un administrateur configure le VPN WireGuard, ajoute un téléphone en scannant '
                    'un code QR, garde un nom qui suit la maison (DuckDNS, Cloudflare ou toute adresse à appeler) et enregistre les nœuds dont le panneau propre peut '
                    "s'ouvrir depuis l'extérieur via le serveur, en comparant l'empreinte du certificat avant de lui faire confiance ; chaque étape s'explique en huit "
                    "langues et redemande le mot de passe depuis l'extérieur.",
                    "**Joindre la maison depuis l'extérieur, pas à pas :** dans Configuration > Sécurité un guide de six étapes montre si la machine en est capable, si "
                    "le VPN existe, si la maison a un nom, si le port est ouvert sur le routeur et si le téléphone est ajouté, et comment l'essayer en données mobiles ; "
                    "l'onglet Sécurité est organisé en trois sections titrées.",
                    "**Carte du chiffrement du broker :** Configuration > Broker montre si la liaison du serveur avec le broker est chiffrée et l'empreinte de "
                    "l'autorité propre à l'installation à laquelle il fait confiance ; rien d'alarmant n'est affiché quand la liaison est non chiffrée, car c'est le cas "
                    'par défaut.',
                    "**Santé des nœuds et modes d'armement :** Système a une carte avec le rapport de santé de chaque nœud (durée de marche, motif du redémarrage, "
                    "mémoire, liaison et signal, connexions au broker, dernière erreur, historique et redémarrages) et Centrales d'alarme a un sélecteur de mode "
                    "(Absent, Présent, Nuit et les vôtres) avec un éditeur de modes, le tout en huit langues avec aide, étapes de visite et réponses de l'assistant.",
                    '**Connexion pour gestionnaires de mots de passe et un Historique à onglets :** la connexion est un vrai formulaire que le gestionnaire de mots de '
                    "passe du navigateur ou du système peut enregistrer et remplir, avec un « Se souvenir de moi » facultatif qui ne retient que le nom d'utilisateur "
                    "(jamais le mot de passe) et une note qui le dit ; l'Historique a les onglets Tout, Alarmes, Connexions, Appareils, Système et Réglages, avec la "
                    'liste de chaque appareil et application qui se connecte au serveur (dernière fois vu, sessions ouvertes, connexions et refus) et les événements des '
                    "nœuds, du broker, des services, des mises à jour et de l'armement. Les adresses ne sont visibles que des administrateurs.",
                    '**Maintenance des batteries (Configuration, administrateurs) :** un assistant en quatre étapes - batterie et opération, valeurs, confirmation en '
                    'saisissant le numéro de série de la batterie, résultat - pour modifier ce que garde une batterie Pylontech ; limites en volts et en degrés un '
                    "groupe entier à la fois, un fichier de firmware lu avant d'être envoyé, la batterie lue avant et après avec la différence et la transcription, et "
                    "une sortie qu'on peut remettre comme avant.",
                    '**Commande des nœuds depuis la carte de santé :** chaque nœud a un menu (Redémarrer, Mettre en pause ou Reprendre, Mettre en veille - travail '
                    'arrêté, reste connecté - ou Rallumer, Identifier, Diagnostic, Maintenance activée ou désactivée) et la carte offre les actions de groupe Tout '
                    "redémarrer (en même temps, ou l'un après l'autre avec la centrale d'alarme en dernier), Tout mettre en pause, Tout mettre en veille et Tout "
                    "reprendre. Le nom du nœud (ou le mot RESTART, PAUSE ou STANDBY pour tous) est saisi de nouveau et une nouvelle preuve d'identité est demandée ; des "
                    'pastilles suivent chaque nœud (envoyé, reçu, hors ligne, de retour, appliqué) et montrent En pause, En veille depuis quand et par qui, et '
                    "Maintenance ; et les avertissements disent quand une centrale d'alarme ou un radar en pause ou en veille laisse la maison sans protection. Il "
                    "n'existe ni réinitialisation d'usine, ni effacement, ni sommeil profond.",
                    '**État en direct :** Studio écoute le canal en direct du serveur (un WebSocket) et affiche aussitôt une alarme, un armement ou un nœud qui revient, '
                    "et ne demande l'état que toutes les vingt secondes comme filet de sécurité tant que le canal est ouvert ; la barre du bas indique *En direct*. Les "
                    "concepteurs d'alarme, d'électricité et de réseau répondent aussi à F (ajuster), plus et moins (zoom) et Ctrl+D (dupliquer)."],
        'intro': "**ARMOR-STUDIO** est la console de l'opérateur. Elle ne détient jamais un mot de passe de caméra, une adresse RTSP ni un jeton : elle se connecte au "
                 'serveur avec un nom et un mot de passe, reçoit une session **HttpOnly** de 8 heures, et tout ce qui est privilégié passe par cette session.',
        'sections': [{'icon': '🔒',
                      'title': 'Modèle de sécurité',
                      'bullets': ['**Aucun secret dans le navigateur.** Les mots de passe des caméras sont saisis une fois, envoyés au serveur et ensuite affichés '
                                  "seulement comme un état « enregistré » masqué. Les exports du site suppriment les noms d'utilisateur et les indicateurs "
                                  "d'identifiants.",
                                  '**Les réglages stockés sont une entrée non fiable.** Ils sont lus valeur par valeur : une origine, un thème, une langue ou une forme '
                                  'invalides sont écartés, les positions sont bornées et les listes plafonnées.',
                                  "**Aucune requête vers un tiers.** Les polices sont locales ; l'hôte statique envoie `Content-Security-Policy: default-src 'self'` "
                                  "limitée au serveur configuré, `frame-ancestors 'none'`, `nosniff` et `no-referrer`.",
                                  "La vidéo en direct n'est montrée que par une adresse de flux que le serveur délivre à un opérateur."],
                      'raw': '* **Aucun secret dans le navigateur.** Les mots de passe des caméras sont saisis une fois, envoyés au serveur et ensuite affichés '
                             "seulement comme un état « enregistré » masqué. Les exports du site suppriment les noms d'utilisateur et les indicateurs d'identifiants.\n"
                             '* **Les réglages stockés sont une entrée non fiable.** Ils sont lus valeur par valeur : une origine, un thème, une langue ou une forme '
                             'invalides sont écartés, les positions sont bornées et les listes plafonnées.\n'
                             "* **Aucune requête vers un tiers.** Les polices sont locales ; l'hôte statique envoie `Content-Security-Policy: default-src 'self'` "
                             "limitée au serveur configuré, `frame-ancestors 'none'`, `nosniff` et `no-referrer`.\n"
                             "* La vidéo en direct n'est montrée que par une adresse de flux que le serveur délivre à un opérateur."}],
        'note': '`tools/serve.mjs` lit `ARMOR_STUDIO_HOST` (par défaut `127.0.0.1`), `ARMOR_STUDIO_PORT` (`5178`), `ARMOR_STUDIO_DIST` et `ARMOR_SERVER_ORIGIN`. Pour '
                "installer toute la pile sur le banc d'essai CM5, voir [ARMOR-DEVOPS](https://github.com/JuanenRac/ARMOR-DEVOPS).",
        'fit': "Studio est la fenêtre de l'opérateur sur tout le système. Il ne parle jamais à un nœud : tout passe par "
               "[ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER), seul à décider (la seule exception est un lien vers le panneau propre de chaque nœud). C'est "
               "aussi là que se conçoivent le site, l'alarme, l'installation électrique et le réseau, d'où se pilotent le firmware des nœuds et les mises à jour de "
               "l'installation elle-même, et où vivent l'Aide et l'assistant. Le même serveur est utilisé par "
               '[ARMOR-ANDROID-CONTROL](https://github.com/JuanenRac/ARMOR-ANDROID-CONTROL) sur le téléphone.',
        'hardware': 'Utilisé chaque jour sur le banc de test CM5 (vrai serveur, vraies caméras IP, un vrai nœud radar) ; les menus solaire, électrique, centrales '
                    "d'alarme et panneau tactile attendent de vrais nœuds",
        'requirements': ['Node.js 22+', 'un ARMOR-SERVER en marche (sinon Studio affiche des données de démonstration)']},
 'it': {'tagline': "Console di gestione e progettazione: telecamere, radar, allarmi, energia, rete locale, prove, planimetria del sito e manutenzione dell'impianto",
        'status': {'software': 'La console funziona ogni giorno contro il server reale del banco di prova CM5.',
                   'tests': 'Superano 990 test unitari (`npm test`) e girano i test nel browser: impostazioni, fusione delle telecamere, grafici solari, geometria e '
                            "controlli dei progettisti, annunciatore di allarmi, dizionario dell'assistente e ogni menu nelle otto lingue.",
                   'ui': "Il video dal vivo e il PTZ non sono provati con ogni telecamera possibile, non c'è stata una revisione formale di accessibilità o usabilità e "
                         'le immagini della Guida sono fatte con dati di esempio.',
                   'hardware': "È usato ogni giorno con il server reale, telecamere IP reali e un nodo radar reale; i menu solare, elettrico, della centralina d'allarme "
                               'e del pannello touch attendono nodi reali.',
                   'security': "Sessioni, ruoli e rifiuto delle credenziali delle telecamere negli indirizzi sono coperti da test; non c'è stata una revisione "
                               'indipendente.',
                   'integration': 'Finché il server non è raggiungibile, Studio mostra dati dimostrativi e lo dice nella barra superiore.',
                   'docs': 'Otto lingue, la Guida integrata e i percorsi guidati, le note di sicurezza e il registro delle modifiche sono aggiornati.'},
        'honest': 'Studio dialoga con [ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER) ed è coperto da 990 test unitari (lettura delle impostazioni, fusione '
                  "delle telecamere, aritmetica dei grafici solari, geometria e controlli dei progettisti, annunciatore degli allarmi, dizionario dell'assistente, ogni "
                  'menu reso nelle otto lingue, host statico) e da test nel browser. Funziona in uso quotidiano contro il banco di prova CM5 con il vero server, vere '
                  'telecamere IP e un nodo radar sulla sua scheda; le immagini della Guida sono fatte con dati di esempio. Ciò che **non** è stato provato è il video '
                  "dal vivo e il PTZ con tutte le telecamere possibili, i menu solare, elettrico, centrali d'allarme e pannello touch con apparecchi reali (esiste solo "
                  'il nodo radar) e una revisione formale di accessibilità o usabilità. Finché il server non è raggiungibile, Studio mostra dati dimostrativi e lo dice '
                  'nella barra superiore.',
        'bullets': ["**Panoramica e sistema:** lo stato del perimetro, una scheda per ogni parte (centrali d'allarme, radar, telecamere, dispositivi, energia, rete, "
                    'server), una mappa viva del progetto con ogni dispositivo e allarme, e ciò che richiede attenzione, tutto in una schermata senza scorrimento; una '
                    "pagina di sistema e un registro di audit per l'amministratore.",
                    '**Monitor delle telecamere:** 1, 2, 4, 6, 8, 9, 12 o 16 riquadri che si adattano alla cornice (16:9, tutta la matrice visibile, senza ritagli), una '
                    'vista ingrandita con pulsantiera PTZ limitata, istantanea e registrazione MP4; una **libreria delle registrazioni** per filtrare, anteprima, '
                    'riprodurre, proteggere e cancellare prove e scaricare una **prova di custodia**.',
                    '**Allarmi:** ciò che richiede una persona ora, con riconoscimento e archivio chiuso; un **controllo prima di inserire** e un PIN per disinserire; '
                    "allarmi disegnati sulla mappa viva; un suono per ogni gravità, una voce parlata con propri stili (neutro, eroe d'azione, signore oscuro, teatrale) "
                    'che dice anche quando qualcosa si connette, finestre di avviso, un pulsante muto accanto alla Guida e un salto facoltativo al menu giusto.',
                    '**Dispositivi e automazioni:** fumo, gas, allagamento, porta, finestra, movimento, clima, presa, luce, sirena, serratura, tapparella, cancello, '
                    'porta del garage e scaldabagno via Wi-Fi, Zigbee, Bluetooth o cavo (preset per Zigbee2MQTT, Tasmota e Shelly); regole da qualsiasi fonte di '
                    'allarme, con soglie, che azionano dispositivi quando succede qualcosa; un grande pulsante inserisci / disinserisci.',
                    "**Centrali d'allarme e Progettista dell'allarme:** lo stato di ogni nodo ARMOR-NODE-ALARM, le sue zone ed eventi, i sensori Zigbee legati alle "
                    "zone, e un progettista in cui disegni l'allarme della casa (centrali, contatti, movimento, rilevatori di fumo, gas e allagamento, sirene, tastiere, "
                    'cablaggio e collegamenti radio) e leghi ogni elemento disegnato a una zona reale.',
                    '**Energia solare ed elettrica:** il menu *Inverter* disegna la casa come un flusso di energia animato con indicatori, letture e grafici di storico; '
                    "*Batterie* mostra ogni pacco con le sue capacità, ogni modulo e ogni cella; *Elettrico* mostra l'ingresso di rete, ogni canale e gli allarmi dei "
                    'contatori; in entrambi dichiari le tue apparecchiature (Voltronic, MPP Solar, Pylontech, ANT-BMS…) e un pulsante *Mostra letture di esempio* ti '
                    'lascia provare prima il menu.',
                    '**Progettista elettrico:** disegna lo schema elettrico della casa (rete, contatore, protezioni, commutatori, distribuzione, FV, inverter, batterie '
                    'e carichi, CA e CC), legalo ai dispositivi solari che il server legge per vedere i valori in diretta, e lascia che i controlli lo rivedano (due '
                    'sorgenti su una linea, interruttori e cavi rispetto alla corrente…).',
                    '**Radar:** una mappa viva disegnata dal tuo progetto del sito con i bersagli che ogni radar riferisce, il loro percorso recente e le **zone '
                    "dell'immagine da ignorare**; stato vivo dei nodi, con quelli silenziosi mostrati come *obsoleti*; il pannello proprio di ogni nodo a un clic.",
                    '**Progettista del sito:** disegna il terreno, edifici di più piani con cinque tipi di tetto, porte, finestre, lampioni, camini, pannelli solari, '
                    'pali, strade e sentieri, poi telecamere e radar dove vuoi; una pianta 2D in stile CAD e una vista 3D orbitabile piano per piano; annulla e ripeti; '
                    'versioni del progetto.',
                    '**Rete locale:** il menu *Rete* mostra ciò che riferisce il nodo ARMOR-NETWORK (dispositivi, interruzioni, stato di internet e **indirizzo '
                    'pubblico** con il fornitore e il luogo), permette di dare nomi, nascondere e sorvegliare dispositivi, ordinare una scansione, un ping o '
                    "un'ispezione con un accesso che dai, e il *Progettista di rete* la disegna.",
                    '**Cattura automatica:** in *Configurazione > Cattura automatica*, foto e video fatti da soli quando una telecamera vede qualcosa a sistema inserito '
                    "(quante foto, ogni quanto, quanto dura un clip), e le zone dell'immagine da ignorare disegnate sul fotogramma della telecamera.",
                    '**Firmware dei nodi e aggiornamenti:** *Firmware dei nodi* aggiorna i nodi di campo uno alla volta, con una barra per tutto il lavoro e per ogni '
                    'nodo, e conserva il suo stato se un allarme ti porta in un altro menu; *Aggiornamenti* installa le nuove versioni di Studio e del server da GitHub '
                    '(mostrando le novità della nuova versione), quelle del sistema operativo e una console di manutenzione facoltativa.',
                    '**Configurazione in gruppi:** Generale e Preferenze; Utenti, Notifiche e Cattura automatica; Firmware dei nodi e Aggiornamenti; Server, Servizi, '
                    'Broker MQTT, File di impostazioni, Installazione e Console; e ogni menu della barra laterale è anche in gruppi comprimibili (Monitor, Sicurezza, '
                    'Energia, Casa e rete, Progetto, Amministrazione).',
                    '**Otto lingue** (inglese, spagnolo, tedesco, francese, italiano, giapponese, cinese e portoghese) e undici temi, quello predefinito chiamato '
                    "*Armor*; lingua, tema e luogo del meteo seguono l'account, non il browser. Ruoli: amministratore, operatore e **viewer**, che guarda soltanto.",
                    "**Una Guida che conosce tutto il sistema:** un libro con quattro livelli di dettaglio e un'immagine con dati di esempio di ogni menu principale, un "
                    'percorso guidato passo passo per ogni menu che va controllo per controllo (cosa fa ogni pulsante, cosa aspettarsi e gli errori comuni) con la '
                    'propria mascotte e voce, una Guida che spiega a fondo i nodi di campo (Wi-Fi di configurazione, punto di accesso e stazione, PIN Bluetooth, slot di '
                    'firmware con ripristino, aggiornamenti firmati, il pannello da fuori), suggerimenti su tutto, e un **assistente** (una mascotte che puoi trascinare '
                    'ovunque, fissare dove vuoi e a cui chiedere per iscritto) con un dizionario in otto lingue e un fumetto che si apre dal lato che ha spazio. I menu '
                    'in cui lavori restano aperti mentre ne visiti un altro.',
                    '**Accesso da fuori con scelte, non file:** in Sicurezza un amministratore configura la VPN WireGuard, aggiunge un telefono scansionando un codice '
                    'QR, mantiene un nome che segue la casa (DuckDNS, Cloudflare o qualsiasi indirizzo da chiamare) e registra i nodi il cui pannello può essere aperto '
                    "da fuori tramite il server, confrontando l'impronta del certificato prima di fidarsi; ogni passo si spiega in otto lingue e richiede di nuovo la "
                    'password da fuori.',
                    '**Raggiungere la casa da fuori, passo passo:** in Configurazione > Sicurezza una guida di sei passi mostra se la macchina può farlo, se la VPN '
                    'esiste, se la casa ha un nome, se la porta è aperta sul router e se il telefono è aggiunto, e come provarlo con i dati mobili; la scheda Sicurezza '
                    'è organizzata in tre sezioni con titolo.',
                    "**Scheda della cifratura del broker:** Configurazione > Broker mostra se il collegamento del server con il broker è cifrato e l'impronta "
                    "dell'autorità propria dell'installazione di cui si fida; non viene mostrato nulla di allarmante quando il collegamento non è cifrato, perché è la "
                    'condizione predefinita.',
                    '**Salute dei nodi e modalità di inserimento:** Sistema ha una scheda con il rapporto di salute di ogni nodo (tempo acceso, motivo del riavvio, '
                    "memoria, collegamento e segnale, connessioni al broker, ultimo errore, cronologia e riavvii) e Centrali d'allarme ha un selettore di modalità "
                    "(Fuori casa, In casa, Notte e le tue) con un editor delle modalità, tutto in otto lingue con aiuto, passi della guida e risposte dell'assistente.",
                    "**Accesso per gestori di password e una Cronologia a schede:** l'accesso è un vero modulo che il gestore di password del browser o del sistema può "
                    'salvare e compilare, con un "Ricordami" facoltativo che conserva solo il nome utente (mai la password) e una nota che lo dice; la Cronologia ha le '
                    "schede Tutto, Allarmi, Connessioni, Dispositivi, Sistema e Impostazioni, con l'elenco di ogni dispositivo e app che si collega al server (ultima "
                    'volta visto, sessioni aperte, accessi e rifiuti) e gli eventi di nodi, broker, servizi, aggiornamenti e inserimento. Gli indirizzi li vedono solo '
                    'gli amministratori.',
                    '**Manutenzione delle batterie (Configurazione, amministratori):** una procedura guidata in quattro passi - batteria e operazione, valori, conferma '
                    'digitando il numero di serie della batteria, risultato - per modificare ciò che conserva una batteria Pylontech; limiti in volt e gradi un gruppo '
                    "intero alla volta, un file firmware letto prima di essere inviato, la batteria letta prima e dopo con la differenza e la trascrizione, e un'uscita "
                    "che si può rimettere com'era.",
                    '**Controllo dei nodi dalla scheda di salute:** ogni nodo ha un menu (Riavvia, Pausa o Riprendi, Standby - lavoro spento, resta connesso - o '
                    'Accendi, Identifica, Diagnostica, Manutenzione attivata o disattivata) e la scheda ha le azioni di gruppo Riavvia tutti (insieme, o uno dopo '
                    "l'altro con la centrale d'allarme per ultima), Metti tutti in pausa, Metti tutti in standby e Riprendi tutti. Il nome del nodo (o la parola "
                    'RESTART, PAUSE o STANDBY per tutti) viene digitato di nuovo e si chiede una nuova prova di identità; delle etichette seguono ogni nodo (inviato, '
                    'ricevuto, offline, tornato, applicato) e mostrano In pausa, In standby da quando e da chi, e Manutenzione; e gli avvisi dicono quando una centrale '
                    "d'allarme o un radar in pausa o in standby lascia la casa senza protezione. Non esistono ripristino di fabbrica, cancellazione né sonno profondo.",
                    '**Stato in diretta:** Studio ascolta il canale in diretta del server (un WebSocket) e mostra subito un allarme, un inserimento o un nodo che torna, '
                    'e chiede lo stato solo ogni venti secondi come rete di sicurezza finché il canale è aperto; la barra in basso dice *In diretta*. I designer di '
                    'allarme, elettrico e rete rispondono anche a F (adatta), più e meno (zoom) e Ctrl+D (duplica).'],
        'intro': "**ARMOR-STUDIO** è la console dell'operatore. Non detiene mai una password di telecamera, un indirizzo RTSP o un token: accede al server con nome "
                 'utente e password, riceve una sessione **HttpOnly** di 8 ore e tutto ciò che è privilegiato passa da quella sessione.',
        'sections': [{'icon': '🔒',
                      'title': 'Modello di sicurezza',
                      'bullets': ['**Nessun segreto nel browser.** Le password delle telecamere si digitano una volta, si inviano al server e poi si vedono solo come '
                                  'stato «salvata» mascherato. Le esportazioni del sito omettono nomi utente e indicatori di credenziali.',
                                  "**Le impostazioni salvate sono input non attendibile.** Sono lette valore per valore: un'origine, un tema, una lingua o una forma non "
                                  'validi vengono scartati, le posizioni limitate e le liste contenute.',
                                  "**Nessuna richiesta a terzi.** I caratteri sono locali; l'host statico invia `Content-Security-Policy: default-src 'self'` limitata "
                                  "al server configurato, `frame-ancestors 'none'`, `nosniff` e `no-referrer`.",
                                  'Il video dal vivo si mostra solo tramite un indirizzo di flusso che il server rilascia a un operatore.'],
                      'raw': '* **Nessun segreto nel browser.** Le password delle telecamere si digitano una volta, si inviano al server e poi si vedono solo come stato '
                             '«salvata» mascherato. Le esportazioni del sito omettono nomi utente e indicatori di credenziali.\n'
                             "* **Le impostazioni salvate sono input non attendibile.** Sono lette valore per valore: un'origine, un tema, una lingua o una forma non "
                             'validi vengono scartati, le posizioni limitate e le liste contenute.\n'
                             "* **Nessuna richiesta a terzi.** I caratteri sono locali; l'host statico invia `Content-Security-Policy: default-src 'self'` limitata al "
                             "server configurato, `frame-ancestors 'none'`, `nosniff` e `no-referrer`.\n"
                             '* Il video dal vivo si mostra solo tramite un indirizzo di flusso che il server rilascia a un operatore.'}],
        'note': '`tools/serve.mjs` legge `ARMOR_STUDIO_HOST` (predefinito `127.0.0.1`), `ARMOR_STUDIO_PORT` (`5178`), `ARMOR_STUDIO_DIST` e `ARMOR_SERVER_ORIGIN`. Per '
                'installare tutto lo stack sul banco di prova CM5 vedi [ARMOR-DEVOPS](https://github.com/JuanenRac/ARMOR-DEVOPS).',
        'fit': "Studio è la finestra dell'operatore su tutto il sistema. Non parla mai con un nodo: tutto passa per "
               "[ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER), l'unico che decide (l'unica eccezione è un collegamento al pannello proprio di ogni nodo). È "
               "anche il luogo dove si progettano il sito, l'allarme, l'impianto elettrico e la rete, da cui si governano il firmware dei nodi e gli aggiornamenti "
               "dell'impianto stesso, e dove vivono la Guida e l'assistente. Lo stesso server è usato da "
               '[ARMOR-ANDROID-CONTROL](https://github.com/JuanenRac/ARMOR-ANDROID-CONTROL) sul telefono.',
        'hardware': "Usato ogni giorno sul banco di prova CM5 (vero server, vere telecamere IP, un vero nodo radar); i menu solare, elettrico, centrali d'allarme e "
                    'pannello touch attendono nodi reali',
        'requirements': ['Node.js 22+', 'un ARMOR-SERVER in esecuzione (altrimenti Studio mostra dati dimostrativi)']},
 'de': {'tagline': 'Betriebs- und Entwurfskonsole: Kameras, Radar, Alarme, Energie, das lokale Netz, Beweise, der Standortplan und die Wartung der Anlage',
        'status': {'software': 'Die Konsole läuft täglich gegen den echten Server des CM5-Prüfstands.',
                   'tests': '990 Unit-Tests bestehen (`npm test`) und die Browser-Tests laufen: Einstellungen, Zusammenführen der Kameras, Solardiagramme, Geometrie und '
                            'Prüfungen der Designer, Alarm-Ansager, Wörterbuch des Assistenten und jedes Menü in den acht Sprachen.',
                   'ui': 'Live-Video und PTZ sind nicht mit jeder möglichen Kamera belegt, es gab keine formale Prüfung der Barrierefreiheit oder Bedienbarkeit, und die '
                         'Bilder der Hilfe entstehen mit Beispieldaten.',
                   'hardware': 'Er wird täglich mit dem echten Server, echten IP-Kameras und einem echten Radar-Knoten genutzt; die Menüs für Solar, Elektrik, '
                               'Alarmzentrale und Touch-Panel warten auf echte Knoten.',
                   'security': 'Sitzungen, Rollen und die Ablehnung von Kamera-Zugangsdaten in Adressen sind durch Tests abgedeckt; es gab keine unabhängige Prüfung.',
                   'integration': 'Solange der Server nicht erreichbar ist, zeigt Studio Demodaten und sagt das in der oberen Leiste.',
                   'docs': 'Acht Sprachen, die eingebaute Hilfe und die geführten Rundgänge, die Sicherheitshinweise und das Änderungsprotokoll sind aktuell.'},
        'honest': 'Studio spricht mit [ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER) und wird von 990 Unit-Tests abgedeckt (Einstellungen lesen, Kameras '
                  'zusammenführen, die Arithmetik der Solardiagramme, Geometrie und Prüfungen der Entwurfswerkzeuge, der Alarmansager, das Wörterbuch des Assistenten, '
                  'jedes Menü in den acht Sprachen, der statische Host) sowie durch Browsertests. Es läuft im täglichen Einsatz am CM5-Testaufbau mit dem echten Server, '
                  'echten IP-Kameras und einem Radarknoten auf seiner Platine; die Bilder der Hilfe entstehen mit Beispieldaten. **Nicht** bewiesen sind Livevideo und '
                  'PTZ mit allen möglichen Kameras, die Menüs für Solar, Elektro, Alarmzentralen und Touchpanel mit echten Geräten (es gibt nur den Radarknoten) sowie '
                  'eine formale Prüfung auf Barrierefreiheit oder Bedienbarkeit. Solange der Server nicht erreichbar ist, zeigt Studio Demodaten und sagt das in der '
                  'oberen Leiste.',
        'bullets': ['**Überblick und System:** der Zustand des Perimeters, eine Kachel für jeden Teil (Alarmzentralen, Radar, Kameras, Geräte, Energie, Netzwerk, '
                    'Server), eine Live-Karte des Plans mit jedem Gerät und Alarm und was Aufmerksamkeit braucht, alles auf einem Bildschirm ohne Scrollen; eine '
                    'Systemseite und ein Audit-Protokoll für Administratoren.',
                    '**Kameramonitor:** 1, 2, 4, 6, 8, 9, 12 oder 16 Kacheln, die in ihren Rahmen passen (16:9, die ganze Matrix sichtbar, kein Beschnitt), eine '
                    'vergrößerte Ansicht mit begrenztem PTZ-Pad, Schnappschuss und MP4-Aufnahme; eine **Aufnahmebibliothek** zum Filtern, Ansehen, Abspielen, Schützen '
                    'und Löschen von Beweisen und zum Herunterladen eines **Verwahrungsnachweises**.',
                    '**Alarme:** was jetzt eine Person braucht, mit Quittieren und abgeschlossenem Protokoll; eine **Prüfung vor dem Scharfschalten** und eine PIN zum '
                    'Unscharfschalten; Alarme auf der Live-Karte; ein Ton für jede Stufe, eine gesprochene Stimme mit eigenen Stilen (neutral, Actionheld, dunkler Lord, '
                    'theatralisch), die auch sagt, wenn sich etwas verbindet, Hinweisfenster, eine Stumm-Taste neben der Hilfe und ein optionaler Sprung ins passende '
                    'Menü.',
                    '**Geräte und Automationen:** Rauch, Gas, Wasser, Tür, Fenster, Bewegung, Klima, Steckdose, Licht, Sirene, Schloss, Rollladen, Tor, Garagentor und '
                    'Warmwasserbereiter über WLAN, Zigbee, Bluetooth oder Kabel (Vorlagen für Zigbee2MQTT, Tasmota und Shelly); Regeln aus jeder Alarmquelle, auch mit '
                    'Schwellwerten, die Geräte schalten, wenn etwas geschieht; eine große Taste Scharf / Unscharf.',
                    '**Alarmzentralen und Alarm-Designer:** der Zustand jedes ARMOR-NODE-ALARM-Knotens, seine Zonen und Ereignisse, die den Zonen zugeordneten '
                    'Zigbee-Sensoren und ein Designer, in dem Sie die Alarmanlage des Hauses zeichnen (Zentralen, Kontakte, Bewegung, Rauch-, Gas- und Wassermelder, '
                    'Sirenen, Tastaturen, Verdrahtung und Funkverbindungen) und jedes gezeichnete Element einer echten Zone zuordnen.',
                    '**Solar- und Elektroenergie:** das Menü *Wechselrichter* zeichnet das Haus als animierten Energiefluss mit Anzeigen, Werten und Verlaufsdiagrammen; '
                    '*Batterien* zeigt jeden Stapel mit seinen Kapazitäten, jedes Modul und jede Zelle; *Elektro* zeigt den Netzeingang, jeden Kanal und die Alarme der '
                    'Zähler; in beiden melden Sie Ihre Geräte an (Voltronic, MPP Solar, Pylontech, ANT-BMS…), und eine Taste *Beispielwerte zeigen* lässt Sie das Menü '
                    'zuerst ausprobieren.',
                    '**Elektro-Designer:** zeichnen Sie den Elektroplan des Hauses (Netz, Zähler, Schutzorgane, Umschalter, Verteilung, PV, Wechselrichter, Batterien '
                    'und Lasten, AC und DC), verbinden Sie ihn mit den Solargeräten, die der Server liest, um Live-Werte zu sehen, und lassen Sie die Prüfungen ihn '
                    'durchsehen (zwei Quellen auf einer Leitung, Sicherungen und Kabel gegen den Strom…).',
                    '**Radar:** eine Live-Karte nach Ihrem Standortplan mit den Zielen, die jedes Radar meldet, ihrem letzten Weg und den **zu ignorierenden '
                    'Bildzonen**; Live-Zustand der Knoten, stumme als *veraltet*; das eigene Panel jedes Knotens einen Klick entfernt.',
                    '**Standort-Designer:** zeichnen Sie das Gelände, Gebäude mit mehreren Etagen und fünf Dacharten, Türen, Fenster, Lampen, Schornsteine, Solarmodule, '
                    'Masten, Straßen und Wege, dann Kameras und Radare, wo Sie möchten; ein 2D-Plan im CAD-Stil und eine drehbare 3D-Ansicht Etage für Etage; Rückgängig '
                    'und Wiederholen; Versionen des Plans.',
                    '**Lokales Netz:** das Menü *Netzwerk* zeigt, was der ARMOR-NETWORK-Knoten meldet (Geräte, Ausfälle, den Internetzustand und die **öffentliche '
                    'Adresse** mit Anbieter und Ort), lässt Sie Geräte benennen, verbergen und beobachten, einen Scan, einen Ping oder eine Prüfung mit einem von Ihnen '
                    'gegebenen Login beauftragen, und der *Netzwerk-Designer* zeichnet es.',
                    '**Automatische Aufnahme:** unter *Konfiguration > Automatische Aufnahme* von selbst gemachte Fotos und Videos, wenn eine Kamera bei scharfem System '
                    'etwas sieht (wie viele Fotos, wie oft, wie lang ein Clip), und die zu ignorierenden Bildzonen, auf den Kamerabildausschnitt gezeichnet.',
                    '**Knoten-Firmware und Updates:** *Knoten-Firmware* aktualisiert die Feldknoten nacheinander, mit einem Balken für die ganze Arbeit und für jeden '
                    'Knoten, und behält ihren Zustand, wenn Sie ein Alarm in ein anderes Menü führt; *Updates* installiert neue Versionen von Studio und Server von '
                    'GitHub (mit den Neuigkeiten der neuen Version), die des Betriebssystems und eine optionale Wartungskonsole.',
                    '**Konfiguration in Gruppen:** Allgemein und Einstellungen; Benutzer, Benachrichtigungen und Automatische Aufnahme; Knoten-Firmware und Updates; '
                    'Server, Dienste, MQTT-Broker, Einstellungsdateien, Installation und Konsole; und jedes Menü der Seitenleiste ist ebenfalls in einklappbaren Gruppen '
                    '(Überwachung, Sicherheit, Energie, Haus und Netz, Entwurf, Administration).',
                    '**Acht Sprachen** (Englisch, Spanisch, Deutsch, Französisch, Italienisch, Japanisch, Chinesisch und Portugiesisch) und elf Themen, das '
                    'Standardthema heißt *Armor*; Sprache, Thema und Wetterort folgen dem Konto, nicht dem Browser. Rollen: Administrator, Operator und **Viewer**, der '
                    'nur ansieht.',
                    '**Eine Hilfe, die das ganze System kennt:** ein Buch mit vier Detailstufen und einem Bild mit Beispieldaten für jedes Hauptmenü, eine geführte '
                    'Schritt-für-Schritt-Tour für jedes Menü, die Bedienelement für Bedienelement vorgeht (was jeder Knopf tut, was zu erwarten ist und die üblichen '
                    'Fehler) mit eigenem Maskottchen und eigener Stimme, eine Hilfe, die die Feldknoten im Detail erklärt (Einrichtungs-WLAN, Zugangspunkt und Station, '
                    'Bluetooth-PIN, Firmware-Slots mit Rückfall, signierte Updates, das Panel von außen), Hinweise zu allem und ein **Assistent** (ein Maskottchen, das '
                    'Sie überallhin ziehen, wo Sie wollen fixieren und schriftlich fragen können) mit einem Wörterbuch in acht Sprachen und einer Sprechblase, die sich '
                    'auf der Seite mit Platz öffnet. Die Menüs, in denen Sie arbeiten, bleiben offen, während Sie ein anderes besuchen.',
                    '**Zugriff von außen mit Auswahl statt Dateien:** In Sicherheit richtet ein Administrator das WireGuard-VPN ein, fügt ein Handy per QR-Code hinzu, '
                    'hält einen Namen aktuell, der dem Haus folgt (DuckDNS, Cloudflare oder eine beliebige Adresse), und trägt die Knoten ein, deren eigenes Panel von '
                    'außen über den Server geöffnet werden kann, wobei der Zertifikat-Fingerabdruck vor dem Vertrauen verglichen wird; jeder Schritt erklärt sich in '
                    'acht Sprachen und verlangt von außen erneut das Passwort.',
                    '**Von außen ins Haus, Schritt für Schritt:** in Konfiguration > Sicherheit zeigt eine Anleitung mit sechs Schritten, ob der Rechner es kann, das '
                    'VPN existiert, das Haus einen Namen hat, der Port am Router offen und das Handy hinzugefügt ist, und wie man es mit mobilen Daten testet; die '
                    'Registerkarte Sicherheit ist in drei Abschnitte mit Titel gegliedert.',
                    '**Karte zur Broker-Verschlüsselung:** Konfiguration > Broker zeigt, ob die Verbindung des Servers zum Broker verschlüsselt ist, und den '
                    'Fingerabdruck der eigenen Zertifizierungsstelle der Anlage, der er vertraut; bei unverschlüsselter Verbindung wird nichts Alarmierendes angezeigt, '
                    'denn das ist der Standard.',
                    '**Zustand der Knoten und Scharfschaltmodi:** System hat eine Karte mit dem Zustandsbericht jedes Knotens (Laufzeit, Neustartgrund, Speicher, '
                    'Verbindung und Signal, Brokerverbindungen, letzter Fehler, Verlauf und Neustarts), und Alarmzentralen hat eine Modusauswahl (Abwesend, Zuhause, '
                    'Nacht und eigene) mit einem Editor für die Modi, alles in acht Sprachen mit Hilfe, Tourschritten und Antworten des Assistenten.',
                    '**Anmeldung für Passwortmanager und ein Verlauf mit Reitern:** Die Anmeldung ist ein echtes Formular, das der Passwortmanager des Browsers oder '
                    'Systems speichern und ausfüllen kann, mit einem optionalen "Angemeldet bleiben", das nur den Benutzernamen (nie das Passwort) merkt, und einem '
                    'Hinweis dazu; der Verlauf hat die Reiter Alle, Alarme, Verbindungen, Geräte, System und Einstellungen, mit der Liste jedes Geräts und jeder App, '
                    'die sich mit dem Server verbindet (zuletzt gesehen, offene Sitzungen, Anmeldungen und Ablehnungen), und den Ereignissen der Knoten, des Brokers, '
                    'der Dienste, Updates und des Scharfschaltens. Adressen sehen nur Administratoren.',
                    '**Batteriewartung (Konfiguration, Administratoren):** ein Assistent in vier Schritten - Batterie und Operation, Werte, Bestätigung mit eingetippter '
                    'Seriennummer der Batterie, Ergebnis - um zu ändern, was eine Pylontech-Batterie speichert; Grenzwerte in Volt und Grad jeweils als ganze Gruppe, '
                    'eine Firmware-Datei wird vor dem Senden gelesen, die Batterie davor und danach mit Unterschied und Protokoll, und ein Ausgang lässt sich wie vorher '
                    'zurücksetzen.',
                    '**Steuerung der Knoten über die Gesundheitskarte:** Jeder Knoten hat ein Menü (Neustart, Pause oder Fortsetzen, Standby - Arbeit aus, bleibt '
                    'verbunden - oder Einschalten, Identifizieren, Diagnose, Wartung ein oder aus), und die Karte bietet die Gruppenaktionen Alle neu starten '
                    '(gleichzeitig oder nacheinander mit der Alarmzentrale zuletzt), Alle pausieren, Alle in Standby und Alle fortsetzen. Der Name des Knotens (oder das '
                    'Wort RESTART, PAUSE oder STANDBY für alle) wird erneut getippt, und es wird ein frischer Identitätsnachweis verlangt; Marken folgen jedem Knoten '
                    '(gesendet, bestätigt, offline, zurück, angewendet) und zeigen Pausiert, Standby seit wann und durch wen sowie Wartung; und die Warnungen sagen, '
                    'wann eine pausierte oder im Standby befindliche Alarmzentrale oder ein Radar das Haus ungeschützt lässt. Es gibt kein Zurücksetzen auf '
                    'Werkseinstellungen, kein Löschen und keinen Tiefschlaf.',
                    '**Live-Status:** Studio hört den Live-Kanal des Servers (ein WebSocket) ab und zeigt einen Alarm, ein Scharfschalten oder einen zurückkehrenden '
                    'Knoten sofort an; solange der Kanal offen ist, wird der Status nur alle zwanzig Sekunden als Sicherheitsnetz abgefragt, die untere Leiste zeigt '
                    '*Live*. Die Designer für Alarm, Elektrik und Netzwerk reagieren zusätzlich auf F (einpassen), Plus und Minus (Zoom) und Strg+D (duplizieren).'],
        'intro': '**ARMOR-STUDIO** ist die Konsole des Bedieners. Sie hält nie ein Kamerapasswort, eine RTSP-Adresse oder ein Token: sie meldet sich mit Benutzername '
                 'und Passwort am Server an, erhält eine **HttpOnly**-Sitzung von 8 Stunden, und alles Privilegierte läuft über diese Sitzung.',
        'sections': [{'icon': '🔒',
                      'title': 'Sicherheitsmodell',
                      'bullets': ['**Keine Geheimnisse im Browser.** Kamerapasswörter werden einmal eingegeben, an den Server gesendet und danach nur als maskierter '
                                  'Zustand „gespeichert“ gezeigt. Standortexporte lassen Benutzernamen und Zugangsdaten-Markierungen weg.',
                                  '**Gespeicherte Einstellungen sind nicht vertrauenswürdige Eingabe.** Sie werden Wert für Wert gelesen: ein ungültiger Ursprung, ein '
                                  'ungültiges Thema, eine ungültige Sprache oder Form wird verworfen, Positionen werden begrenzt und Listen gekappt.',
                                  "**Keine Anfragen an Dritte.** Schriften sind lokal; der statische Host sendet `Content-Security-Policy: default-src 'self'` "
                                  "beschränkt auf den konfigurierten Server, `frame-ancestors 'none'`, `nosniff` und `no-referrer`.",
                                  'Live-Video wird nur über eine Stream-Adresse gezeigt, die der Server einem Operator ausstellt.'],
                      'raw': '* **Keine Geheimnisse im Browser.** Kamerapasswörter werden einmal eingegeben, an den Server gesendet und danach nur als maskierter '
                             'Zustand „gespeichert“ gezeigt. Standortexporte lassen Benutzernamen und Zugangsdaten-Markierungen weg.\n'
                             '* **Gespeicherte Einstellungen sind nicht vertrauenswürdige Eingabe.** Sie werden Wert für Wert gelesen: ein ungültiger Ursprung, ein '
                             'ungültiges Thema, eine ungültige Sprache oder Form wird verworfen, Positionen werden begrenzt und Listen gekappt.\n'
                             "* **Keine Anfragen an Dritte.** Schriften sind lokal; der statische Host sendet `Content-Security-Policy: default-src 'self'` beschränkt "
                             "auf den konfigurierten Server, `frame-ancestors 'none'`, `nosniff` und `no-referrer`.\n"
                             '* Live-Video wird nur über eine Stream-Adresse gezeigt, die der Server einem Operator ausstellt.'}],
        'note': '`tools/serve.mjs` liest `ARMOR_STUDIO_HOST` (Standard `127.0.0.1`), `ARMOR_STUDIO_PORT` (`5178`), `ARMOR_STUDIO_DIST` und `ARMOR_SERVER_ORIGIN`. Zur '
                'Installation des ganzen Stacks auf dem CM5-Prüfstand siehe [ARMOR-DEVOPS](https://github.com/JuanenRac/ARMOR-DEVOPS).',
        'fit': 'Studio ist das Fenster des Bedieners auf das ganze System. Es spricht nie mit einem Knoten: alles läuft über '
               '[ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER), das als Einziges entscheidet (die einzige Ausnahme ist ein Link zum eigenen Panel jedes '
               'Knotens). Hier werden auch Standort, Alarmanlage, Elektroinstallation und Netzwerk entworfen, die Firmware der Knoten und die Updates der Anlage selbst '
               'gesteuert, und hier leben die Hilfe und der Assistent. Denselben Server nutzt '
               '[ARMOR-ANDROID-CONTROL](https://github.com/JuanenRac/ARMOR-ANDROID-CONTROL) auf dem Telefon.',
        'hardware': 'Täglich am CM5-Testaufbau im Einsatz (echter Server, echte IP-Kameras, ein echter Radarknoten); die Menüs für Solar, Elektro, Alarmzentralen und '
                    'Touchpanel warten auf echte Knoten',
        'requirements': ['Node.js 22+', 'ein laufender ARMOR-SERVER (sonst zeigt Studio Demodaten)']},
 'zh': {'tagline': '运营与设计控制台：摄像头、雷达、报警、能源、本地网络、证据、场地平面图和系统维护',
        'status': {'software': '控制台每天都对 CM5 测试台的真实服务器运行。',
                   'tests': '990 项单元测试通过（`npm test`）并运行浏览器测试：设置、摄像头合并、光伏图表、设计器的几何与检查、报警播报、助手词典以及八种语言的每个菜单。',
                   'ui': '实时视频和云台并未对所有可能的摄像头验证过，也没有做过正式的无障碍或可用性评审，帮助中的图片使用的是示例数据。',
                   'hardware': '每天与真实服务器、真实 IP 摄像头和真实雷达节点一起使用；光伏、电气、报警面板和触摸面板菜单在等待真实节点。',
                   'security': '会话、角色以及拒绝在地址中携带摄像头登录信息均有测试覆盖；没有经过独立审查。',
                   'integration': '在服务器无法连接时，Studio 会显示演示数据，并在顶部栏中说明。',
                   'docs': '八种语言、应用内帮助和引导导览、安全说明以及更新日志均为最新。'},
        'honest': 'Studio 与 [ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER) 通信，由 990 '
                  '个单元测试覆盖（设置解析、摄像头合并、太阳能图表的算术、设计器的几何与检查、报警播报器、助手的词典、八种语言的每个菜单、静态主机），并有浏览器测试。它在 CM5 测试台上日常运行，配有真实的服务器、真实的 IP '
                  '摄像头和板上的雷达节点；帮助中的图片使用示例数据制作。**尚未**证明的是：所有可能摄像头的实时视频和 PTZ、使用真实设备的太阳能、电气、报警主机和触摸屏菜单（目前只有雷达节点），以及正式的无障碍或可用性评审。当无法连接服务器时，Studio 会显示演示数据，并在顶部栏说明。',
        'bullets': ['**概览与系统：**周界状态、每个部分一块卡片（报警主机、雷达、摄像头、设备、能源、网络、服务器）、带有每个设备和报警的设计实时地图，以及需要关注的事项，全部在一个无需滚动的屏幕上；管理员还有系统页面和审计记录。',
                    '**摄像头监视器：**1、2、4、6、8、9、12 或 16 个适应画框的画面（16:9，整个矩阵可见，不裁剪）、带有限定范围云台面板的放大视图、快照和 MP4 录像；**录像库**可筛选、预览、播放、保护和删除证据，并下载**保管证明**。',
                    '**报警：**现在需要有人处理的事项，可确认并有已关闭记录；**布防前检查**和撤防 PIN；报警绘制在实时地图上；每种严重级别都有声音，朗读语音有自己的风格（中性、动作英雄、黑暗君主、戏剧化），并会说出有设备连接；弹窗、帮助旁的静音按钮，以及可选的跳转到相应菜单。',
                    '**设备与自动化：**烟雾、燃气、漏水、门、窗、移动、气候、插座、灯、警笛、门锁、卷帘、大门、车库门和热水器设备，通过 Wi-Fi、Zigbee、蓝牙或有线（带 Zigbee2MQTT、Tasmota 和 Shelly '
                    '的预设）；来自任何报警源的规则（含阈值）可在发生事件时切换设备；一个大的布防 / 撤防按钮。',
                    '**报警主机与报警设计器：**每个 ARMOR-NODE-ALARM 节点的状态、其防区和事件、绑定到防区的 Zigbee 传感器，以及可绘制住宅报警系统（主机、触点、移动、烟雾、燃气和漏水探测器、警笛、键盘、布线和无线链路）并把每个绘制的元素绑定到真实防区的设计器。',
                    '**太阳能与电气能源：***逆变器*菜单把住宅画成动画能量流，带仪表、读数和历史图表；*电池*显示每个电池组的容量、每个模块和每个电芯；*电气*显示电网输入、每个通道和电表报警；两者都可以声明你的设备（Voltronic、MPP '
                    'Solar、Pylontech、ANT-BMS……），并可先用*显示示例读数*按钮试用菜单。',
                    '**电气设计器：**绘制住宅的电气图（电网、电表、保护、转换开关、配电、光伏、逆变器、电池和负载，交流和直流），把它与服务器读取的太阳能设备关联以查看实时值，并让检查来审阅它（一条线上有两个电源、断路器和电缆与电流的匹配……）。',
                    '**雷达：**根据你的场地设计绘制的实时地图，显示每个雷达报告的目标、其近期轨迹以及**要忽略的画面区域**；节点实时状态，沉默的节点显示为*过期*；每个节点自己的面板只需点击一次。',
                    '**场地设计器：**绘制地形、多层建筑（五种屋顶）、门、窗、灯、烟囱、太阳能板、桅杆、道路和小径，然后在任意位置放置摄像头和雷达；CAD 风格的 2D 平面图以及可环绕、逐层查看的 3D 视图；撤销和重做；设计版本。',
                    '**本地网络：***网络*菜单显示 ARMOR-NETWORK 节点报告的内容（设备、中断、互联网状态以及带有运营商和地点的**公网地址**），可以命名、隐藏和监视设备，下达扫描、ping 或用你提供的登录信息进行检查的指令，*网络设计器*则把它画出来。',
                    '**自动抓拍：**在*配置 > 自动抓拍*中，系统布防且摄像头看到东西时自动拍照和录像（拍几张、多久一次、片段多长），并在摄像头画面上绘制要忽略的区域。',
                    '**节点固件与更新：***节点固件*逐个更新现场节点，整个任务和每个节点都有进度条，即使报警把你带到另一个菜单也会保留其状态；*更新*从 GitHub 安装 Studio 和服务器的新版本（显示新版本的更新内容）、操作系统更新以及可选的维护控制台。',
                    '**分组的配置：**常规和偏好设置；用户、通知和自动抓拍；节点固件和更新；服务器、服务、MQTT 代理、配置文件、安装和控制台；侧边栏的每个菜单也分为可折叠的组（监控、安防、能源、住宅与网络、设计、管理）。',
                    '**八种语言**（英语、西班牙语、德语、法语、意大利语、日语、中文和葡萄牙语）和十一种主题，默认主题名为 *Armor*；语言、主题和天气地点跟随账户，而不是浏览器。角色：管理员、操作员和只看不改的 **viewer**。',
                    '**了解整个系统的帮助：**一本有四个详细程度的书，每个主要菜单都有一张示例数据图片，每个菜单都有逐项讲解的分步导览（每个按钮的作用、预期结果和常见错误，带专属吉祥物和语音），帮助中对现场节点有深入说明（设置 Wi-Fi、接入点与终端、蓝牙 '
                    'PIN、带回滚的固件分区、签名更新、从外部访问面板），处处有提示，还有一个**助手**（可拖到任何位置、固定在想要的地方并可文字提问的吉祥物），带八种语言的词典，气泡会在有空位的一侧打开。你正在工作的菜单在你访问其他菜单时保持打开。',
                    '**用选项而非文件设置外部访问：**在“安全”中，管理员可设置 WireGuard VPN、扫描二维码添加手机、保持一个跟随家的域名（DuckDNS、Cloudflare '
                    '或任意可调用的地址），并登记可通过服务器从外部打开其自身面板的节点（信任前先比对证书指纹）；每一步都有八种语言的说明，从外部操作时会再次要求密码。',
                    '**从外部连接到家，逐步指引：** 在“配置 > 安全”中，六步向导会显示机器是否支持、VPN 是否存在、家是否有名称、路由器端口是否开放、手机是否已添加，以及如何用移动数据测试；安全页签整理为三个带标题的分区。',
                    '**代理加密卡片:** 配置 > 代理 显示服务器与代理的连接是否加密,以及它所信任的本安装自有证书颁发机构的指纹;连接未加密时不会显示任何警告,因为这是默认状态。',
                    '**节点健康与布防模式：** “系统”有一张卡片显示每个节点的健康报告（运行时间、重启原因、内存、连接与信号、代理连接、最后错误、历史与重启），“报警主机”有模式选择（离家、在家、夜间和自定义）及模式编辑器，全部提供八种语言，并带有帮助、引导步骤和助手回答。',
                    '**适配密码管理器的登录与带标签的历史：** '
                    '登录是真正的表单，浏览器或系统的密码管理器可以保存并填充；可选的“记住我”只记住用户名（绝不保存密码），并附有说明。历史有“全部”“报警”“连接”“设备”“系统”“设置”标签，列出所有连接服务器的设备和应用（最后出现、已打开的会话、登录与被拒），以及节点、代理、服务、更新和布防的事件。地址只显示给管理员。',
                    '**电池维护（配置，管理员）：** 四步向导——电池和操作、数值、输入电池序列号确认、结果——用于修改 Pylontech 电池保存的内容；限值以伏特和摄氏度输入并整组发送，固件文件在发送前先被读取，操作前后读取电池并显示差异和记录，输出可以恢复原状。',
                    '**在节点健康卡片上控制节点：** 每个节点都有一个菜单（重启、暂停或恢复、待机——停止工作，保持连接——或开机、识别、诊断、开启或关闭维护），卡片上有群组操作：全部重启（同时进行，或逐个进行并把报警主机放在最后）、全部暂停、全部待机和全部恢复。需要再次输入节点名称（对所有节点则输入单词 '
                    'RESTART、PAUSE 或 STANDBY），并要求新的身份验证；标签跟踪每个节点（已发送、已确认、离线、已恢复、已应用），并显示已暂停、自何时起由谁设为待机以及维护；警告会说明报警主机或雷达处于暂停或待机时，家中将失去保护。没有恢复出厂设置、擦除或深度睡眠。',
                    '**实时状态：** Studio 监听服务器的实时通道（WebSocket），报警、布防或节点恢复会立即显示；通道打开时，状态仅每二十秒轮询一次作为保底，底栏显示“实时”。报警、电气和网络设计器除原有按键外，还支持 F（适应窗口）、加减号（缩放）和 Ctrl+D（复制）。'],
        'intro': '**ARMOR-STUDIO** 是操作员的控制台。它从不持有摄像头密码、RTSP 地址或令牌：它用用户名和密码登录服务器，获得 8 小时的 **HttpOnly** 会话，一切特权操作都经由该会话。',
        'sections': [{'icon': '🔒',
                      'title': '安全模型',
                      'bullets': ['**浏览器中没有机密。** 摄像头密码只输入一次，发送到服务器，之后只显示为被遮蔽的“已保存”状态。场地导出会去掉用户名和凭据标志。',
                                  '**保存的设置属于不可信输入。** 它们被逐值解析：无效的源、主题、语言或形状会被丢弃，位置被限制范围，列表被限制大小。',
                                  "**没有第三方请求。** 字体来自本地；静态主机发送限于所配置服务器的 `Content-Security-Policy: default-src 'self'`、`frame-ancestors 'none'`、`nosniff` 和 `no-referrer`。",
                                  '实时视频只通过服务器发给操作员的视频流地址显示。'],
                      'raw': '* **浏览器中没有机密。** 摄像头密码只输入一次，发送到服务器，之后只显示为被遮蔽的“已保存”状态。场地导出会去掉用户名和凭据标志。\n'
                             '* **保存的设置属于不可信输入。** 它们被逐值解析：无效的源、主题、语言或形状会被丢弃，位置被限制范围，列表被限制大小。\n'
                             "* **没有第三方请求。** 字体来自本地；静态主机发送限于所配置服务器的 `Content-Security-Policy: default-src 'self'`、`frame-ancestors 'none'`、`nosniff` 和 `no-referrer`。\n"
                             '* 实时视频只通过服务器发给操作员的视频流地址显示。'}],
        'note': '`tools/serve.mjs` 读取 `ARMOR_STUDIO_HOST`（默认 `127.0.0.1`）、`ARMOR_STUDIO_PORT`（`5178`）、`ARMOR_STUDIO_DIST` 和 `ARMOR_SERVER_ORIGIN`。要把整套系统安装到 CM5 测试台，参见 '
                '[ARMOR-DEVOPS](https://github.com/JuanenRac/ARMOR-DEVOPS)。',
        'fit': 'Studio 是操作员观察整个系统的窗口。它从不直接与节点通信：一切都经过 '
               '[ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER)，只有它做决定（唯一的例外是指向每个节点自带面板的链接）。场地、报警、电气设施和网络也在这里设计，节点固件和系统自身的更新也从这里操作，帮助和助手也在这里。手机上的 '
               '[ARMOR-ANDROID-CONTROL](https://github.com/JuanenRac/ARMOR-ANDROID-CONTROL) 使用同一个服务器。',
        'hardware': '每天在 CM5 测试台上使用（真实服务器、真实 IP 摄像头、真实雷达节点）；太阳能、电气、报警主机和触摸屏菜单在等待真实节点',
        'requirements': ['Node.js 22+', '运行中的 ARMOR-SERVER（否则 Studio 显示演示数据）']},
 'ja': {'tagline': '運用・設計コンソール：カメラ、レーダー、警報、エネルギー、ローカルネットワーク、証拠、サイト図、設備の保守',
        'status': {'software': 'コンソールは CM5 テストベンチの実際のサーバーに対して毎日使われています。',
                   'tests': '990 件のユニットテストが通り（`npm test`）、ブラウザーテストも実行されます：設定、カメラの統合、太陽光のグラフ、デザイナーの図形と検査、警報アナウンス、アシスタントの辞書、8 言語すべてのメニュー。',
                   'ui': 'ライブ映像と PTZ はすべてのカメラで確認したわけではなく、アクセシビリティやユーザビリティの正式なレビューもありません。ヘルプの画像はサンプルデータで作っています。',
                   'hardware': '実際のサーバー、実際の IP カメラ、実際のレーダーノードとともに毎日使っています。太陽光・電気・警報パネル・タッチパネルのメニューは、実機のノードを待っています。',
                   'security': 'セッション、ロール、アドレスにカメラのログイン情報を含めることの拒否はテストでカバーされています。独立したレビューはありません。',
                   'integration': 'サーバーに接続できない間は、Studio はデモデータを表示し、上部のバーでそのことを知らせます。',
                   'docs': '8 言語、アプリ内ヘルプとガイドツアー、セキュリティ注記、変更履歴は最新です。'},
        'honest': 'Studio は [ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER) と通信し、990 件のユニットテスト（設定の解析、カメラの統合、ソーラーグラフの計算、設計ツールの幾何と検査、警報アナウンサー、アシスタントの辞書、8 '
                  '言語での全メニューの描画、静的ホスト）とブラウザテストでカバーされています。CM5 テストベンチで、実際のサーバー、実際の IP '
                  'カメラ、基板上のレーダーノードと組み合わせて日常的に動作しており、ヘルプの画像は例示データで作られています。**まだ**証明されていないもの：あらゆるカメラでのライブ映像と '
                  'PTZ、実機でのソーラー・電気・警報盤・タッチパネルのメニュー（存在するのはレーダーノードのみ）、正式なアクセシビリティ・ユーザビリティ評価。サーバーに接続できない間、Studio はデモデータを表示し、上部バーでそれを示します。',
        'bullets': ['**概要とシステム：**境界の状態、各部分のタイル（警報盤、レーダー、カメラ、デバイス、エネルギー、ネットワーク、サーバー）、すべてのデバイスと警報を載せた設計のライブマップ、注意が必要なもの。すべてスクロールなしの 1 画面で、管理者にはシステムページと監査記録があります。',
                    '**カメラモニター：**枠に収まる 1、2、4、6、8、9、12、16 タイル（16:9、マトリクス全体が見え、切り取りなし）、範囲を限った PTZ パッド付きの拡大表示、スナップショットと MP4 '
                    '録画。**録画ライブラリ**で証拠のフィルター、プレビュー、再生、保護、削除、**保管証明**のダウンロードができます。',
                    '**警報：**今すぐ人が必要なものを、確認と終了記録とともに表示。**警戒前のチェック**と解除用 '
                    'PIN、ライブマップ上の警報、重大度ごとの音、独自のスタイル（標準、アクションヒーロー、闇の支配者、劇的）を持つ音声読み上げ（何かが接続されたことも伝えます）、ポップアップ、ヘルプの隣のミュートボタン、適切なメニューへの任意のジャンプ。',
                    '**デバイスとオートメーション：**煙、ガス、浸水、ドア、窓、動き、気候、プラグ、照明、サイレン、鍵、シャッター、門扉、ガレージドア、給湯器を Wi-Fi、Zigbee、Bluetooth、有線で（Zigbee2MQTT、Tasmota、Shelly '
                    'のプリセット付き）。あらゆる警報源（しきい値も可）から、何かが起きたときにデバイスを切り替えるルール、大きな警戒 / 解除ボタン。',
                    '**警報盤と警報デザイナー：**各 ARMOR-NODE-ALARM ノードの状態、ゾーンとイベント、ゾーンに結び付けた Zigbee '
                    'センサー、そして家の警報（警報盤、接点、動き、煙・ガス・浸水検知器、サイレン、キーパッド、配線、無線リンク）を描き、描いた各要素を実際のゾーンに結び付けるデザイナー。',
                    '**ソーラーと電気のエネルギー：***インバーター*メニューは家をゲージ、数値、履歴グラフ付きのアニメーションするエネルギーフローとして描き、*バッテリー*は各スタックの容量、各モジュール、すべてのセルを表示し、*電気*は系統入力、各チャンネル、メーターの警報を表示します。どちらも機器（Voltronic、MPP '
                    'Solar、Pylontech、ANT-BMS など）を登録でき、*例示の測定値を表示*ボタンで先にメニューを試せます。',
                    '**電気デザイナー：**家の電気図（系統、メーター、保護、切替器、配電、PV、インバーター、バッテリー、負荷、AC と DC）を描き、サーバーが読むソーラー機器に結び付けてライブ値を見て、検査に見直させます（1 本の線に 2 つの電源、電流に対するブレーカーとケーブルなど）。',
                    '**レーダー：**サイト設計から描いたライブマップに、各レーダーが報告する対象、その最近の経路、**無視する映像ゾーン**を表示。ノードのライブ状態（無応答は*古い*と表示）、各ノード自身のパネルへ 1 クリック。',
                    '**サイトデザイナー：**地形、複数階の建物（5 種類の屋根）、ドア、窓、街灯、煙突、ソーラーパネル、マスト、道路や小道を描き、カメラとレーダーを好きな場所に配置。CAD 風の 2D 図面と、階ごとに回転できる 3D 表示、元に戻す・やり直し、設計のバージョン。',
                    '**ローカルネットワーク：***ネットワーク*メニューは ARMOR-NETWORK '
                    'ノードの報告（デバイス、停止、インターネットの状態、プロバイダーと場所付きの**公開アドレス**）を表示し、デバイスの命名、非表示、監視、スキャン・ping・あなたが渡したログインでの検査の指示ができ、*ネットワークデザイナー*がそれを描きます。',
                    '**自動撮影：***設定 > 自動撮影*で、システムが警戒中にカメラが何かを捉えると写真と動画を自動で撮影（枚数、間隔、クリップの長さ）し、無視する映像ゾーンをカメラのフレーム上に描きます。',
                    '**ノードファームウェアとアップデート：***ノードファームウェア*はフィールドノードを 1 台ずつ更新し、全体と各ノードにバーを表示し、警報で別メニューに移っても状態を保ちます。*アップデート*は GitHub から Studio '
                    'とサーバーの新バージョン（新バージョンの更新内容も表示）、OS の更新、任意の保守コンソールをインストールします。',
                    '**グループ化された設定：**一般と設定項目、ユーザー・通知・自動撮影、ノードファームウェアとアップデート、サーバー・サービス・MQTT '
                    'ブローカー・設定ファイル・インストール・コンソール。サイドバーの各メニューも折りたたみ可能なグループ（監視、セキュリティ、エネルギー、家とネットワーク、設計、管理）に分かれています。',
                    '**8 言語**（英語、スペイン語、ドイツ語、フランス語、イタリア語、日本語、中国語、ポルトガル語）と 11 のテーマ（既定は *Armor*）。言語、テーマ、天気の場所はブラウザではなくアカウントに従います。ロール：管理者、オペレーター、閲覧だけの **viewer**。',
                    '**システム全体を知っているヘルプ：**4 '
                    '段階の詳しさを持つ本と各主要メニューの例示データ付き画像、メニューごとのステップガイドツアー（ボタン1つ1つの働き、期待できる結果、よくある間違いまで説明し、専用のマスコットと音声付き）、現場ノードを詳しく説明するヘルプ（セットアップ用Wi-Fi、アクセスポイントとステーション、Bluetooth '
                    'PIN、ロールバック付きファームウェアスロット、署名付き更新、外部からのパネル）、あらゆるもののヒント、そして**アシスタント**（どこへでもドラッグでき、好きな場所に固定でき、文字で質問できるマスコット）。8 '
                    '言語の辞書と、空きのある側に開く吹き出し付き。作業中のメニューは、別のメニューを見ている間も開いたままです。',
                    '**ファイルではなく選択肢で設定する外部アクセス：**セキュリティで管理者が WireGuard VPN を設定し、QR '
                    'コードでスマホを追加し、家に付いてくる名前（DuckDNS、Cloudflare、または呼び出せる任意のアドレス）を維持し、サーバー経由で外から開けるノードを登録します（信頼する前に証明書のフィンガープリントを比較）。各ステップは 8 言語で説明され、外からの操作ではパスワードを再度求めます。',
                    '**外から家に届く方法を一歩ずつ：** 設定 > '
                    'セキュリティの6ステップのガイドが、マシンが対応しているか、VPNがあるか、家に名前があるか、ルーターでポートが開いているか、スマホが追加済みかを示し、モバイルデータでの試し方を説明します。セキュリティタブは見出し付きの3つのセクションに整理されています。',
                    '**ブローカー暗号化カード:** 設定 > ブローカー に、サーバーとブローカーの接続が暗号化されているかと、信頼している設備独自の認証局のフィンガープリントが表示されます。接続が暗号化なしの場合は、それが初期状態なので警告は表示されません。',
                    '**ノードの状態と警戒モード:** 「システム」には各ノードの状態報告（稼働時間、再起動の理由、メモリ、回線と信号、ブローカー接続、最後のエラー、履歴と再起動）のカードがあり、「警報盤」にはモード選択（外出、在宅、夜間、独自）とモードの編集があります。すべて 8 '
                    '言語で、ヘルプ、ツアーの手順、アシスタントの回答付きです。',
                    '**パスワードマネージャー対応のサインインとタブ付きの履歴:** サインインは本物のフォームで、ブラウザーや OS '
                    'のパスワードマネージャーが保存・入力できます。任意の「ユーザー名を記憶」はユーザー名だけを保存し（パスワードは決して保存しません）、その旨の注記があります。履歴には「すべて」「アラーム」「接続」「デバイス」「システム」「設定」のタブがあり、サーバーに接続するすべてのデバイスとアプリの一覧（最終確認、開いているセッション、サインインと拒否）と、ノード・ブローカー・サービス・更新・警戒操作のイベントが見られます。アドレスは管理者にだけ表示されます。',
                    '**バッテリーのメンテナンス（設定、管理者向け）：** '
                    '4段階のウィザード——バッテリーと操作、値、バッテリーのシリアル番号を入力して確認、結果——で、Pylontechバッテリーが保持する内容を変更します。制限値は電圧・温度で入力しグループ単位で送信、ファームウェアファイルは送信前に読み取り、前後のバッテリー状態を差分と記録とともに表示し、出力は元に戻せます。',
                    '**ノードの健全性カードからの制御：** '
                    '各ノードにメニュー（再起動、一時停止または再開、スタンバイ（動作停止、接続は維持）または電源オン、識別、診断、メンテナンスのオン／オフ）があり、カードにはグループ操作として、すべて再起動（同時、または警報パネルを最後にして順番に）、すべて一時停止、すべてスタンバイ、すべて再開があります。ノード名（全ノードの場合は '
                    'RESTART、PAUSE、STANDBY '
                    'のいずれかの単語）を再入力し、新たな本人確認も求められます。チップが各ノード（送信済み、受領、オフライン、復帰、適用）を追い、一時停止中、いつから誰によるスタンバイか、メンテナンスを表示し、警報パネルやレーダーが一時停止またはスタンバイのとき家が無防備になることを警告が知らせます。工場出荷時リセット、消去、ディープスリープはありません。',
                    '**ライブ状態：** Studio '
                    'はサーバーのライブチャネル（WebSocket）を受け取り、アラーム・警戒・ノードの復帰を即座に表示します。チャネルが開いている間は保険として20秒ごとにだけ状態を問い合わせ、下部バーに「ライブ」と表示します。アラーム・電気・ネットワークの各デザイナーは、既存のキーに加えて '
                    'F（全体表示）、プラス／マイナス（ズーム）、Ctrl+D（複製）にも反応します。'],
        'intro': '**ARMOR-STUDIO** はオペレーターのコンソールです。カメラのパスワード、RTSP アドレス、トークンを決して持ちません。ユーザー名とパスワードでサーバーにサインインし、8 時間の **HttpOnly** セッションを受け取り、権限の要る操作はすべてそのセッションを通ります。',
        'sections': [{'icon': '🔒',
                      'title': 'セキュリティモデル',
                      'bullets': ['**ブラウザーにシークレットはありません。** カメラのパスワードは一度入力してサーバーに送り、その後はマスクされた「保存済み」の状態でしか表示されません。サイトのエクスポートはユーザー名と認証情報のフラグを除きます。',
                                  '**保存された設定は信頼できない入力です。** 値ごとに読み取られ、無効なオリジン、テーマ、言語、形は捨てられ、位置は範囲内に収められ、リストは上限が設けられます。',
                                  "**サードパーティへのリクエストはありません。** フォントはローカルのものです。静的ホストは、設定されたサーバーに限定した `Content-Security-Policy: default-src 'self'`、`frame-ancestors "
                                  "'none'`、`nosniff`、`no-referrer` を送ります。",
                                  'ライブ映像は、サーバーがオペレーターに発行するストリームアドレスを通じてのみ表示されます。'],
                      'raw': '* **ブラウザーにシークレットはありません。** カメラのパスワードは一度入力してサーバーに送り、その後はマスクされた「保存済み」の状態でしか表示されません。サイトのエクスポートはユーザー名と認証情報のフラグを除きます。\n'
                             '* **保存された設定は信頼できない入力です。** 値ごとに読み取られ、無効なオリジン、テーマ、言語、形は捨てられ、位置は範囲内に収められ、リストは上限が設けられます。\n'
                             "* **サードパーティへのリクエストはありません。** フォントはローカルのものです。静的ホストは、設定されたサーバーに限定した `Content-Security-Policy: default-src 'self'`、`frame-ancestors "
                             "'none'`、`nosniff`、`no-referrer` を送ります。\n"
                             '* ライブ映像は、サーバーがオペレーターに発行するストリームアドレスを通じてのみ表示されます。'}],
        'note': '`tools/serve.mjs` は `ARMOR_STUDIO_HOST`（既定 `127.0.0.1`）、`ARMOR_STUDIO_PORT`（`5178`）、`ARMOR_STUDIO_DIST`、`ARMOR_SERVER_ORIGIN` を読みます。CM5 '
                'テストベンチにスタック全体をインストールするには [ARMOR-DEVOPS](https://github.com/JuanenRac/ARMOR-DEVOPS) を参照。',
        'fit': 'Studio はシステム全体を見渡すオペレーターの窓口です。ノードとは直接話さず、すべて [ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER) '
               'を通します（唯一の例外は各ノード自身のパネルへのリンク）。サイト、警報、電気設備、ネットワークの設計、ノードのファームウェアや設備自身のアップデートの操作、ヘルプとアシスタントもここにあります。同じサーバーを、スマートフォンの '
               '[ARMOR-ANDROID-CONTROL](https://github.com/JuanenRac/ARMOR-ANDROID-CONTROL) も使います。',
        'hardware': 'CM5 テストベンチ（実サーバー、実際の IP カメラ、実際のレーダーノード）で毎日使用。ソーラー・電気・警報盤・タッチパネルのメニューは実ノードを待っています',
        'requirements': ['Node.js 22+', '稼働中の ARMOR-SERVER（なければ Studio はデモデータを表示します）']},
 'pt': {'tagline': 'Consola de operação e desenho: câmaras, radar, alarmes, energia, a rede local, provas, a planta do local e a manutenção da instalação',
        'status': {'software': 'A consola funciona todos os dias contra o servidor real da bancada de testes CM5.',
                   'tests': 'Passam 990 testes unitários (`npm test`) e correm os testes de navegador: definições, fusão das câmaras, gráficos solares, geometria e '
                            'verificações dos desenhadores, anunciador de alarmes, dicionário do assistente e cada menu nos oito idiomas.',
                   'ui': 'O vídeo em direto e o PTZ não estão provados com todas as câmaras possíveis, não houve uma revisão formal de acessibilidade ou usabilidade, e '
                         'as imagens da Ajuda são feitas com dados de exemplo.',
                   'hardware': 'É usada todos os dias com o servidor real, câmaras IP reais e um nó radar real; os menus solar, elétrico, de painel de alarme e de '
                               'painel tátil esperam nós reais.',
                   'security': 'As sessões, os papéis e a recusa de credenciais de câmara nos endereços estão cobertos por testes; não houve revisão independente.',
                   'integration': 'Enquanto o servidor não puder ser alcançado, o Studio mostra dados de demonstração e di-lo na barra superior.',
                   'docs': 'Oito idiomas, a Ajuda integrada e os percursos guiados, as notas de segurança e o registo de alterações estão atualizados.'},
        'honest': 'O Studio fala com o [ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER) e está coberto por 990 testes unitários (leitura de definições, fusão '
                  'de câmaras, a aritmética dos gráficos solares, a geometria e as verificações dos desenhadores, o anunciador de alarmes, o dicionário do assistente, '
                  'cada menu desenhado nos oito idiomas, o servidor estático) e por testes no navegador. Funciona em uso diário contra a bancada de testes do CM5 com o '
                  'servidor real, câmaras IP reais e um nó radar na sua placa; as imagens da Ajuda são feitas com dados de exemplo. O que **não** foi provado é o vídeo '
                  'em direto e o PTZ com todas as câmaras possíveis, os menus solar, elétrico, de centrais de alarme e de painel tátil com equipamentos reais (só existe '
                  'o nó radar) e uma revisão formal de acessibilidade ou usabilidade. Enquanto o servidor não é alcançado, o Studio mostra dados de demonstração e di-lo '
                  'na barra superior.',
        'bullets': ['**Resumo e sistema:** o estado do perímetro, um cartão para cada parte (centrais de alarme, radar, câmaras, dispositivos, energia, rede, servidor), '
                    'um mapa vivo do desenho com cada dispositivo e alarme, e o que precisa de atenção, tudo num só ecrã sem deslocamento; uma página de sistema e um '
                    'registo de auditoria para o administrador.',
                    '**Monitor de câmaras:** 1, 2, 4, 6, 8, 9, 12 ou 16 mosaicos que se ajustam à moldura (16:9, toda a matriz visível, sem cortes), uma vista ampliada '
                    'com comando PTZ limitado, fotografia e gravação MP4; uma **biblioteca de gravações** para filtrar, pré-visualizar, reproduzir, proteger e apagar '
                    'provas e descarregar uma **prova de custódia**.',
                    '**Alarmes:** o que precisa de uma pessoa agora, com reconhecer e o registo fechado; uma **verificação antes de armar** e um PIN para desarmar; '
                    'alarmes desenhados no mapa vivo; um som para cada gravidade, uma voz falada com estilos próprios (neutro, herói de ação, senhor das trevas, '
                    'teatral) que também diz quando algo se liga, janelas de aviso, um botão de silêncio junto à Ajuda e um salto opcional para o menu certo.',
                    '**Dispositivos e automatizações:** fumo, gás, inundação, porta, janela, movimento, clima, tomada, luz, sirene, fechadura, estore, portão, porta de '
                    'garagem e esquentador por Wi-Fi, Zigbee, Bluetooth ou cabo (predefinições para Zigbee2MQTT, Tasmota e Shelly); regras a partir de qualquer fonte de '
                    'alarme, com limiares, que acionam dispositivos quando algo acontece; um botão grande de armar / desarmar.',
                    '**Centrais de alarme e o Desenhador de alarme:** o estado de cada nó ARMOR-NODE-ALARM, as suas zonas e eventos, os sensores Zigbee ligados às '
                    'zonas, e um desenhador onde desenha o alarme da casa (centrais, contactos, movimento, detetores de fumo, gás e inundação, sirenes, teclados, '
                    'cablagem e ligações por rádio) e liga cada elemento desenhado a uma zona real.',
                    '**Energia solar e elétrica:** o menu *Inversores* desenha a casa como um fluxo de energia animado com mostradores, leituras e gráficos de '
                    'histórico; *Baterias* mostra cada pilha com as suas capacidades, cada módulo e cada célula; *Elétrico* mostra a entrada de rede, cada canal e os '
                    'alarmes dos contadores; em ambos declara o seu equipamento (Voltronic, MPP Solar, Pylontech, ANT-BMS…) e um botão *Mostrar leituras de exemplo* '
                    'deixa-o experimentar o menu antes.',
                    '**Desenhador elétrico:** desenhe o esquema elétrico da casa (rede, contador, proteções, comutadores, distribuição, FV, inversores, baterias e '
                    'cargas, CA e CC), ligue-o aos dispositivos solares que o servidor lê para ver valores em direto, e deixe que as verificações o revejam (duas fontes '
                    'numa linha, disjuntores e cabos face à corrente…).',
                    '**Radar:** um mapa vivo desenhado a partir do seu desenho do local com os alvos que cada radar comunica, o seu percurso recente e as **zonas da '
                    'imagem a ignorar**; estado vivo dos nós, com os silenciosos como *desatualizados*; o painel próprio de cada nó a um clique.',
                    '**Desenhador do local:** desenhe o terreno, edifícios de vários pisos com cinco tipos de telhado, portas, janelas, candeeiros, chaminés, painéis '
                    'solares, mastros, estradas e caminhos, e depois câmaras e radares onde quiser; uma planta 2D ao estilo CAD e uma vista 3D orbitável piso a piso; '
                    'desfazer e refazer; versões do desenho.',
                    '**Rede local:** o menu *Rede* mostra o que o nó ARMOR-NETWORK comunica (dispositivos, falhas, o estado da internet e o **endereço público** com o '
                    'fornecedor e o local), deixa dar nomes, ocultar e vigiar dispositivos, ordenar um varrimento, um ping ou uma inspeção com um acesso que der, e o '
                    '*Desenhador de rede* desenha-a.',
                    '**Captura automática:** em *Configuração > Captura automática*, fotografias e vídeo feitos sozinhos quando uma câmara vê algo com o sistema armado '
                    '(quantas fotografias, com que frequência, quanto dura um clipe), e as zonas da imagem a ignorar desenhadas sobre o quadro da câmara.',
                    '**Firmware dos nós e atualizações:** *Firmware dos nós* atualiza os nós de campo um a um, com uma barra para todo o trabalho e para cada nó, e '
                    'mantém o seu estado se um alarme o levar a outro menu; *Atualizações* instala as novas versões do Studio e do servidor a partir do GitHub '
                    '(mostrando as novidades da nova versão), as do sistema operativo e uma consola de manutenção opcional.',
                    '**Configuração em grupos:** Geral e Preferências; Utilizadores, Notificações e Captura automática; Firmware dos nós e Atualizações; Servidor, '
                    'Serviços, Broker MQTT, Ficheiros de configuração, Instalação e Consola; e cada menu da barra lateral também está em grupos recolhíveis (Monitor, '
                    'Segurança, Energia, Casa e rede, Desenho, Administração).',
                    '**Oito idiomas** (inglês, espanhol, alemão, francês, italiano, japonês, chinês e português) e onze temas, o predefinido chamado *Armor*; o idioma, '
                    'o tema e o local do tempo seguem a conta, não o navegador. Papéis: administrador, operador e **viewer**, que só observa.',
                    '**Uma Ajuda que conhece todo o sistema:** um livro com quatro níveis de detalhe e uma imagem com dados de exemplo de cada menu principal, uma '
                    'visita guiada passo a passo para cada menu que vai controlo a controlo (o que faz cada botão, o que esperar e os erros habituais) com a sua própria '
                    'mascote e voz, uma Ajuda que explica os nós de campo a fundo (Wi-Fi de configuração, ponto de acesso e estação, PIN de Bluetooth, ranhuras de '
                    'firmware com retrocesso, atualizações assinadas, o painel de fora), dicas em tudo, e um **assistente** (uma mascote que pode arrastar para qualquer '
                    'lugar, fixar onde quiser e a quem perguntar por escrito) com um dicionário em oito idiomas e um balão que se abre do lado que tem espaço. Os menus '
                    'onde trabalha ficam abertos enquanto visita outro.',
                    '**Acesso de fora com escolhas, não ficheiros:** em Segurança um administrador configura a VPN WireGuard, adiciona um telemóvel lendo um código QR, '
                    'mantém um nome que acompanha a casa (DuckDNS, Cloudflare ou qualquer endereço a chamar) e regista os nós cujo próprio painel pode ser aberto de '
                    'fora através do servidor, comparando a impressão digital do certificado antes de confiar nele; cada passo explica-se nas oito línguas e volta a '
                    'pedir a palavra-passe quando é feito de fora.',
                    '**Chegar a casa a partir de fora, passo a passo:** em Configuração > Segurança um guia de seis passos mostra se a máquina consegue, se a VPN '
                    'existe, se a casa tem nome, se a porta está aberta no router e se o telemóvel está adicionado, e como o testar com dados móveis; o separador '
                    'Segurança está organizado em três secções com título.',
                    '**Cartão da cifragem do broker:** Configuração > Broker mostra se a ligação do servidor ao broker está cifrada e a impressão digital da autoridade '
                    'própria da instalação em que confia; não se mostra nada alarmante quando a ligação é sem cifra, porque é o habitual.',
                    '**Saúde dos nós e modos de armar:** Sistema tem um cartão com o relatório de saúde de cada nó (tempo ligado, motivo do reinício, memória, ligação e '
                    'sinal, ligações ao broker, último erro, histórico e reinícios) e Centrais de alarme tem um seletor de modo (Ausente, Em casa, Noite e os seus) com '
                    'um editor de modos, tudo em oito idiomas com ajuda, passos do guia e respostas do assistente.',
                    '**Início de sessão para gestores de palavras-passe e um Histórico com separadores:** o início de sessão é um formulário a sério que o gestor de '
                    'palavras-passe do navegador ou do sistema pode guardar e preencher, com um "Lembrar-me" opcional que guarda só o nome de utilizador (nunca a '
                    'palavra-passe) e uma nota que o diz; o Histórico tem os separadores Tudo, Alarmes, Ligações, Dispositivos, Sistema e Definições, com a lista de '
                    'cada dispositivo e aplicação que se liga ao servidor (última vez, sessões abertas, inícios de sessão e recusas) e os eventos dos nós, do broker, '
                    'dos serviços, das atualizações e do armar. Os endereços só os veem os administradores.',
                    '**Manutenção de baterias (Configuração, administradores):** um assistente de quatro passos - bateria e operação, valores, confirmação escrevendo o '
                    'número de série da bateria, resultado - para alterar o que uma bateria Pylontech guarda; limites em volts e graus um grupo inteiro de cada vez, um '
                    'ficheiro de firmware lido antes de ser enviado, a bateria lida antes e depois com a diferença e a transcrição, e uma saída que se pode repor como '
                    'estava.',
                    '**Controlo dos nós a partir do cartão de saúde:** cada nó tem um menu (Reiniciar, Pausar ou Retomar, Pôr em espera - trabalho desligado, continua '
                    'ligado - ou Ligar, Identificar, Diagnóstico, Manutenção ligada ou desligada) e o cartão tem as ações de grupo Reiniciar todos (de uma vez, ou um a '
                    'seguir ao outro com a central de alarme por último), Pausar todos, Pôr todos em espera e Retomar todos. O nome do nó (ou a palavra RESTART, PAUSE '
                    'ou STANDBY para todos) é escrito de novo e pede-se uma nova prova de identidade; etiquetas seguem cada nó (enviada, recebida, sem ligação, de '
                    'volta, aplicada) e mostram Em pausa, Em espera desde quando e por quem, e Manutenção; e os avisos dizem quando uma central de alarme ou um radar em '
                    'pausa ou em espera deixa a casa sem proteção. Não existe reposição de fábrica, apagamento nem sono profundo.',
                    '**Estado em direto:** o Studio escuta o canal em direto do servidor (um WebSocket) e mostra de imediato um alarme, um armar ou um nó que volta, e '
                    'só pergunta o estado de vinte em vinte segundos como rede de segurança enquanto o canal está aberto; a barra de baixo diz *Em direto*. Os '
                    'desenhadores de alarme, elétrico e de rede respondem também a F (ajustar), mais e menos (zoom) e Ctrl+D (duplicar).'],
        'intro': 'O **ARMOR-STUDIO** é a consola do operador. Nunca guarda uma palavra-passe de câmara, um endereço RTSP nem um token: inicia sessão no servidor com um '
                 'nome de utilizador e palavra-passe, recebe uma sessão **HttpOnly** de 8 horas, e tudo o que é privilegiado viaja por essa sessão.',
        'sections': [{'icon': '🔒',
                      'title': 'Modelo de segurança',
                      'bullets': ['**Sem segredos no navegador.** As palavras-passe das câmaras escrevem-se uma vez, enviam-se ao servidor e depois só se mostram como '
                                  'um estado «guardada» mascarado. As exportações do local retiram nomes de utilizador e indicadores de credenciais.',
                                  '**As definições guardadas são entrada não fiável.** Leem-se valor a valor: uma origem, tema, idioma ou forma inválidos descartam-se, '
                                  'as posições limitam-se e as listas têm tamanho máximo.',
                                  '**Sem pedidos a terceiros.** Os tipos de letra são pilhas locais; o servidor estático envia `Content-Security-Policy: default-src '
                                  "'self'` limitado ao servidor configurado, `frame-ancestors 'none'`, `nosniff` e `no-referrer`.",
                                  'O vídeo em direto só se mostra através de um endereço de emissão que o servidor emite para um operador.'],
                      'raw': '* **Sem segredos no navegador.** As palavras-passe das câmaras escrevem-se uma vez, enviam-se ao servidor e depois só se mostram como um '
                             'estado «guardada» mascarado. As exportações do local retiram nomes de utilizador e indicadores de credenciais.\n'
                             '* **As definições guardadas são entrada não fiável.** Leem-se valor a valor: uma origem, tema, idioma ou forma inválidos descartam-se, as '
                             'posições limitam-se e as listas têm tamanho máximo.\n'
                             '* **Sem pedidos a terceiros.** Os tipos de letra são pilhas locais; o servidor estático envia `Content-Security-Policy: default-src '
                             "'self'` limitado ao servidor configurado, `frame-ancestors 'none'`, `nosniff` e `no-referrer`.\n"
                             '* O vídeo em direto só se mostra através de um endereço de emissão que o servidor emite para um operador.'}],
        'note': 'O `tools/serve.mjs` lê `ARMOR_STUDIO_HOST` (predefinido `127.0.0.1`), `ARMOR_STUDIO_PORT` (`5178`), `ARMOR_STUDIO_DIST` e `ARMOR_SERVER_ORIGIN`. Para '
                'instalar todo o conjunto na bancada de testes CM5 veja o [ARMOR-DEVOPS](https://github.com/JuanenRac/ARMOR-DEVOPS).',
        'fit': 'O Studio é a janela do operador para todo o sistema. Nunca fala com um nó: tudo passa pelo [ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER), '
               'que é o único que decide (a única exceção é uma ligação ao painel próprio de cada nó). É também onde se desenham o local, o alarme, a instalação '
               'elétrica e a rede, de onde se governam o firmware dos nós e as atualizações da própria instalação, e onde vivem a Ajuda e o assistente. O mesmo servidor '
               'é usado pelo [ARMOR-ANDROID-CONTROL](https://github.com/JuanenRac/ARMOR-ANDROID-CONTROL) no telemóvel.',
        'hardware': 'Usado diariamente contra a bancada de testes do CM5 (servidor real, câmaras IP reais, um nó radar real); os menus solar, elétrico, de centrais de '
                    'alarme e de painel tátil esperam nós reais',
        'requirements': ['Node.js 22+', 'um ARMOR-SERVER em execução (senão o Studio mostra dados de demonstração)']}}

# the text tree of docs/structure.json (make_structure.py --tree <language>); the repository's own check fails when it and the file disagree
TREE = {'en': 'ARMOR-STUDIO/\n'
       '├── src/\n'
       '│   ├── App.tsx                       the shell: menus, groups, live status\n'
       '│   ├── api/                          the client of the server, one file per area\n'
       '│   ├── views/                        overview, cameras, radar, alarms, energy, network, system\n'
       '│   ├── components/                   camera tiles, top bar, sidebar, Help, site map\n'
       '│   ├── designer/                     the Site Designer, 2D plan and 3D view\n'
       '│   ├── electrical/ alarm/ network/   the Electrical, Alarm and Network Designers\n'
       '│   ├── alerts/ assistant/ tour/      sounds and voice, the mascot, guided tours\n'
       '│   ├── weather/ help/ preflight/     Weather menu, Help book, check before arming\n'
       '│   └── locales/                      the table of each language (generated)\n'
       '├── public/                           the pictures of the Help, one set per language\n'
       '├── nginx/                            web server of the image and its headers\n'
       '├── e2e/                              browser tests (Playwright)\n'
       '├── tools/                            serve.mjs (the static host), build_locales.mjs, the shared CI checks and launcher\n'
       '├── docs/                             the security model\n'
       '├── images/                           banner, icon and the pictures of the README\n'
       '├── .github/                          CI workflow, dashboard notice, issue and pull-request templates\n'
       '├── Dockerfile                        container image: Node build, nginx host\n'
       '├── armor.project.json                manifest: version, role, maturity\n'
       '├── CHANGELOG.md                      what changed in each version\n'
       '├── package.json package-lock.json    dependencies and scripts\n'
       '├── index.html                        the page Vite builds the app from\n'
       '├── vite.config.ts eslint.config.js   bundler and lint settings\n'
       '├── tsconfig.json tsconfig.app.json   TypeScript settings\n'
       '├── run.sh run.bat                    start, shared workflow\n'
       '├── build.sh build.bat                build and test, shared workflow\n'
       '├── build-test.sh build-test.bat      build, test and package\n'
       '├── test.sh test.bat                  only the tests, never the version\n'
       '└── SECURITY.md SUPPORT.md CONTRIBUTING.md CODE_OF_CONDUCT.md LICENSE',
 'es': 'ARMOR-STUDIO/\n'
       '├── src/\n'
       '│   ├── App.tsx                       el armazón: menús, grupos, estado en vivo\n'
       '│   ├── api/                          el cliente del servidor, un fichero por área\n'
       '│   ├── views/                        resumen, cámaras, radar, alarmas, energía, red, sistema\n'
       '│   ├── components/                   teselas de cámara, barra superior, lateral, Ayuda, mapa\n'
       '│   ├── designer/                     el Diseñador de emplazamiento, plano 2D y vista 3D\n'
       '│   ├── electrical/ alarm/ network/   los Diseñadores eléctrico, de alarma y de red\n'
       '│   ├── alerts/ assistant/ tour/      sonidos y voz, la mascota, visitas guiadas\n'
       '│   ├── weather/ help/ preflight/     menú del Tiempo, libro de Ayuda, comprobación previa\n'
       '│   └── locales/                      la tabla de cada idioma (generada)\n'
       '├── public/                           las imágenes de la Ayuda, un juego por idioma\n'
       '├── nginx/                            servidor web de la imagen y sus cabeceras\n'
       '├── e2e/                              pruebas de navegador (Playwright)\n'
       '├── tools/                            serve.mjs (el host estático), build_locales.mjs, las comprobaciones de CI y el lanzador\n'
       '├── docs/                             el modelo de seguridad\n'
       '├── images/                           banner, icono y las imágenes del README\n'
       '├── .github/                          flujo de CI, aviso al panel, plantillas de incidencias y pull requests\n'
       '├── Dockerfile                        imagen de contenedor: build Node, host nginx\n'
       '├── armor.project.json                manifiesto: versión, función, madurez\n'
       '├── CHANGELOG.md                      qué cambió en cada versión\n'
       '├── package.json package-lock.json    dependencias y scripts\n'
       '├── index.html                        la página desde la que Vite construye la app\n'
       '├── vite.config.ts eslint.config.js   ajustes del empaquetador y lint\n'
       '├── tsconfig.json tsconfig.app.json   ajustes de TypeScript\n'
       '├── run.sh run.bat                    arrancar, flujo compartido\n'
       '├── build.sh build.bat                construir y probar, flujo compartido\n'
       '├── build-test.sh build-test.bat      construir, probar y empaquetar\n'
       '├── test.sh test.bat                  solo las pruebas, nunca la versión\n'
       '└── SECURITY.md SUPPORT.md CONTRIBUTING.md CODE_OF_CONDUCT.md LICENSE',
 'de': 'ARMOR-STUDIO/\n'
       '├── src/\n'
       '│   ├── App.tsx                       die Hülle: Menüs, Gruppen, Live-Status\n'
       '│   ├── api/                          der Client des Servers, eine Datei je Bereich\n'
       '│   ├── views/                        Übersicht, Kameras, Radar, Alarme, Energie, Netz, System\n'
       '│   ├── components/                   Kamerakacheln, Kopfleiste, Seitenleiste, Hilfe, Karte\n'
       '│   ├── designer/                     der Standort-Designer, 2D-Plan und 3D-Ansicht\n'
       '│   ├── electrical/ alarm/ network/   die Elektro-, Alarm- und Netzwerk-Designer\n'
       '│   ├── alerts/ assistant/ tour/      Klänge und Stimme, das Maskottchen, geführte Touren\n'
       '│   ├── weather/ help/ preflight/     Wetter-Menü, Hilfebuch, Prüfung vor dem Scharfschalten\n'
       '│   └── locales/                      die Tabelle jeder Sprache (erzeugt)\n'
       '├── public/                           die Bilder der Hilfe, ein Satz je Sprache\n'
       '├── nginx/                            Webserver des Images und seine Header\n'
       '├── e2e/                              Browser-Tests (Playwright)\n'
       '├── tools/                            serve.mjs (der statische Host), build_locales.mjs, die gemeinsamen CI-Prüfungen und der Starter\n'
       '├── docs/                             das Sicherheitsmodell\n'
       '├── images/                           Banner, Symbol und die Bilder des READMEs\n'
       '├── .github/                          CI-Workflow, Dashboard-Hinweis, Vorlagen für Issues und Pull Requests\n'
       '├── Dockerfile                        Container-Image: Node-Build, nginx-Host\n'
       '├── armor.project.json                Manifest: Version, Rolle, Reife\n'
       '├── CHANGELOG.md                      was sich in jeder Version geändert hat\n'
       '├── package.json package-lock.json    Abhängigkeiten und Skripte\n'
       '├── index.html                        die Seite, aus der Vite die App baut\n'
       '├── vite.config.ts eslint.config.js   Einstellungen für Bundler und Lint\n'
       '├── tsconfig.json tsconfig.app.json   TypeScript-Einstellungen\n'
       '├── run.sh run.bat                    Start, gemeinsamer Ablauf\n'
       '├── build.sh build.bat                Bauen und Testen, gemeinsamer Ablauf\n'
       '├── build-test.sh build-test.bat      Bauen, Testen und Verpacken\n'
       '├── test.sh test.bat                  nur die Tests, nie die Version\n'
       '└── SECURITY.md SUPPORT.md CONTRIBUTING.md CODE_OF_CONDUCT.md LICENSE',
 'fr': 'ARMOR-STUDIO/\n'
       '├── src/\n'
       "│   ├── App.tsx                       l'ossature : menus, groupes, état en direct\n"
       '│   ├── api/                          le client du serveur, un fichier par domaine\n'
       '│   ├── views/                        aperçu, caméras, radar, alarmes, énergie, réseau, système\n'
       '│   ├── components/                   tuiles caméra, barre, panneau latéral, Aide, carte\n'
       '│   ├── designer/                     le concepteur de site, plan 2D et vue 3D\n'
       '│   ├── electrical/ alarm/ network/   les concepteurs électrique, alarme et réseau\n'
       '│   ├── alerts/ assistant/ tour/      sons et voix, la mascotte, visites guidées\n'
       "│   ├── weather/ help/ preflight/     menu Météo, livre d'Aide, contrôle avant armement\n"
       '│   └── locales/                      la table de chaque langue (générée)\n'
       "├── public/                           les images de l'Aide, un jeu par langue\n"
       "├── nginx/                            serveur web de l'image et ses en-têtes\n"
       '├── e2e/                              tests navigateur (Playwright)\n'
       "├── tools/                            serve.mjs (l'hôte statique), build_locales.mjs, les vérifications CI et le lanceur\n"
       '├── docs/                             le modèle de sécurité\n'
       '├── images/                           bannière, icône et images du README\n'
       "├── .github/                          workflow CI, avis au tableau de bord, modèles d'issues et de pull requests\n"
       '├── Dockerfile                        image de conteneur : build Node, hôte nginx\n'
       '├── armor.project.json                manifeste : version, rôle, maturité\n'
       '├── CHANGELOG.md                      ce qui a changé à chaque version\n'
       '├── package.json package-lock.json    dépendances et scripts\n'
       "├── index.html                        la page dont Vite construit l'application\n"
       '├── vite.config.ts eslint.config.js   réglages du bundler et lint\n'
       '├── tsconfig.json tsconfig.app.json   réglages TypeScript\n'
       '├── run.sh run.bat                    démarrer, flux partagé\n'
       '├── build.sh build.bat                construire et tester, flux partagé\n'
       '├── build-test.sh build-test.bat      construire, tester, empaqueter\n'
       '├── test.sh test.bat                  seulement les tests, jamais la version\n'
       '└── SECURITY.md SUPPORT.md CONTRIBUTING.md CODE_OF_CONDUCT.md LICENSE',
 'it': 'ARMOR-STUDIO/\n'
       '├── src/\n'
       "│   ├── App.tsx                       l'ossatura: menu, gruppi, stato dal vivo\n"
       '│   ├── api/                          il client del server, un file per area\n'
       '│   ├── views/                        panoramica, telecamere, radar, allarmi, energia, rete, sistema\n'
       '│   ├── components/                   riquadri camera, barra, laterale, Guida, mappa\n'
       '│   ├── designer/                     il progettista del sito, piano 2D e vista 3D\n'
       '│   ├── electrical/ alarm/ network/   i progettisti elettrico, allarme e rete\n'
       '│   ├── alerts/ assistant/ tour/      suoni e voce, la mascotte, tour guidati\n'
       "│   ├── weather/ help/ preflight/     menu Meteo, libro della Guida, controllo prima dell'armamento\n"
       '│   └── locales/                      la tabella di ogni lingua (generata)\n'
       '├── public/                           le immagini della Guida, un set per lingua\n'
       "├── nginx/                            server web dell'immagine e le sue intestazioni\n"
       '├── e2e/                              test nel browser (Playwright)\n'
       "├── tools/                            serve.mjs (l'host statico), build_locales.mjs, i controlli CI e l'avviatore\n"
       '├── docs/                             il modello di sicurezza\n'
       '├── images/                           banner, icona e immagini del README\n'
       '├── .github/                          workflow CI, avviso alla dashboard, modelli per issue e pull request\n'
       '├── Dockerfile                        immagine container: build Node, host nginx\n'
       '├── armor.project.json                manifesto: versione, ruolo, maturità\n'
       '├── CHANGELOG.md                      cosa è cambiato in ogni versione\n'
       '├── package.json package-lock.json    dipendenze e script\n'
       "├── index.html                        la pagina da cui Vite costruisce l'app\n"
       '├── vite.config.ts eslint.config.js   impostazioni di bundler e lint\n'
       '├── tsconfig.json tsconfig.app.json   impostazioni TypeScript\n'
       '├── run.sh run.bat                    avvio, flusso condiviso\n'
       '├── build.sh build.bat                compila e prova, flusso condiviso\n'
       '├── build-test.sh build-test.bat      compila, prova e impacchetta\n'
       '├── test.sh test.bat                  solo i test, mai la versione\n'
       '└── SECURITY.md SUPPORT.md CONTRIBUTING.md CODE_OF_CONDUCT.md LICENSE',
 'ja': 'ARMOR-STUDIO/\n'
       '├── src/\n'
       '│   ├── App.tsx                       骨格：メニュー、グループ、ライブ状態\n'
       '│   ├── api/                          サーバークライアント（分野ごとに 1 ファイル）\n'
       '│   ├── views/                        概要、カメラ、レーダー、アラーム、エネルギー、ネットワーク、システム\n'
       '│   ├── components/                   カメラタイル、上部バー、サイドバー、ヘルプ、地図\n'
       '│   ├── designer/                     サイトデザイナー（2D 図面と 3D）\n'
       '│   ├── electrical/ alarm/ network/   電気・アラーム・ネットワークデザイナー\n'
       '│   ├── alerts/ assistant/ tour/      音と声、マスコット、ガイドツアー\n'
       '│   ├── weather/ help/ preflight/     天気メニュー、ヘルプ、警戒前チェック\n'
       '│   └── locales/                      各言語の表（生成）\n'
       '├── public/                           ヘルプの画像（言語ごと）\n'
       '├── nginx/                            イメージの Web サーバーとヘッダー\n'
       '├── e2e/                              ブラウザーテスト（Playwright）\n'
       '├── tools/                            serve.mjs（静的ホスト）、build_locales.mjs、共通の CI 検査とランチャー\n'
       '├── docs/                             セキュリティモデル\n'
       '├── images/                           バナー、アイコン、README の画像\n'
       '├── .github/                          CI ワークフロー、ダッシュボード通知、Issue と Pull Request のテンプレート\n'
       '├── Dockerfile                        コンテナイメージ（Node ビルド、nginx）\n'
       '├── armor.project.json                マニフェスト：版・役割・成熟度\n'
       '├── CHANGELOG.md                      各バージョンの変更点\n'
       '├── package.json package-lock.json    依存関係とスクリプト\n'
       '├── index.html                        Vite がアプリを組み立てる元のページ\n'
       '├── vite.config.ts eslint.config.js   バンドラーと lint の設定\n'
       '├── tsconfig.json tsconfig.app.json   TypeScript 設定\n'
       '├── run.sh run.bat                    起動（共通フロー）\n'
       '├── build.sh build.bat                ビルドとテスト（共通フロー）\n'
       '├── build-test.sh build-test.bat      ビルド、テスト、パッケージ化\n'
       '├── test.sh test.bat                  テストのみ（版は変えません）\n'
       '└── SECURITY.md SUPPORT.md CONTRIBUTING.md CODE_OF_CONDUCT.md LICENSE',
 'zh': 'ARMOR-STUDIO/\n'
       '├── src/\n'
       '│   ├── App.tsx                       外壳：菜单、分组、实时状态\n'
       '│   ├── api/                          服务器客户端，每个领域一个文件\n'
       '│   ├── views/                        概览、摄像头、雷达、报警、能源、网络、系统\n'
       '│   ├── components/                   摄像头图块、顶栏、侧栏、帮助、地图\n'
       '│   ├── designer/                     场地设计器，2D 平面图与 3D 视图\n'
       '│   ├── electrical/ alarm/ network/   电气、报警和网络设计器\n'
       '│   ├── alerts/ assistant/ tour/      声音、吉祥物、导览\n'
       '│   ├── weather/ help/ preflight/     天气菜单、帮助手册、布防前检查\n'
       '│   └── locales/                      每种语言的表（自动生成）\n'
       '├── public/                           帮助图片（每种语言一套）\n'
       '├── nginx/                            镜像的 Web 服务器及其头\n'
       '├── e2e/                              浏览器测试（Playwright）\n'
       '├── tools/                            serve.mjs（静态主机）、build_locales.mjs、共用的 CI 检查和启动器\n'
       '├── docs/                             安全模型\n'
       '├── images/                           横幅图、图标和 README 的图片\n'
       '├── .github/                          CI 工作流、仪表板通知、议题和 pull request 模板\n'
       '├── Dockerfile                        容器镜像：Node 构建、nginx 主机\n'
       '├── armor.project.json                清单：版本、角色、成熟度\n'
       '├── CHANGELOG.md                      每个版本的变化\n'
       '├── package.json package-lock.json    依赖与脚本\n'
       '├── index.html                        Vite 据以构建应用的页面\n'
       '├── vite.config.ts eslint.config.js   打包器与 lint 设置\n'
       '├── tsconfig.json tsconfig.app.json   TypeScript 设置\n'
       '├── run.sh run.bat                    启动（共用流程）\n'
       '├── build.sh build.bat                构建并测试（共用流程）\n'
       '├── build-test.sh build-test.bat      构建、测试并打包\n'
       '├── test.sh test.bat                  只运行测试，不改版本\n'
       '└── SECURITY.md SUPPORT.md CONTRIBUTING.md CODE_OF_CONDUCT.md LICENSE',
 'pt': 'ARMOR-STUDIO/\n'
       '├── src/\n'
       '│   ├── App.tsx                       o esqueleto: menus, grupos, estado em direto\n'
       '│   ├── api/                          o cliente do servidor, um ficheiro por área\n'
       '│   ├── views/                        resumo, câmaras, radar, alarmes, energia, rede, sistema\n'
       '│   ├── components/                   mosaicos de câmara, barra, lateral, Ajuda, mapa\n'
       '│   ├── designer/                     o desenhador do local, planta 2D e vista 3D\n'
       '│   ├── electrical/ alarm/ network/   os desenhadores elétrico, de alarme e de rede\n'
       '│   ├── alerts/ assistant/ tour/      sons e voz, a mascote, visitas guiadas\n'
       '│   ├── weather/ help/ preflight/     menu do Tempo, livro de Ajuda, verificação antes de armar\n'
       '│   └── locales/                      a tabela de cada idioma (gerada)\n'
       '├── public/                           as imagens da Ajuda, um conjunto por idioma\n'
       '├── nginx/                            servidor web da imagem e os seus cabeçalhos\n'
       '├── e2e/                              testes de navegador (Playwright)\n'
       '├── tools/                            serve.mjs (o anfitrião estático), build_locales.mjs, as verificações de CI e o lançador\n'
       '├── docs/                             o modelo de segurança\n'
       '├── images/                           faixa, ícone e as imagens do README\n'
       '├── .github/                          fluxo de CI, aviso ao painel, modelos de issues e pull requests\n'
       '├── Dockerfile                        imagem de contentor: build Node, anfitrião nginx\n'
       '├── armor.project.json                manifesto: versão, função, maturidade\n'
       '├── CHANGELOG.md                      o que mudou em cada versão\n'
       '├── package.json package-lock.json    dependências e scripts\n'
       '├── index.html                        a página a partir da qual o Vite constrói a app\n'
       '├── vite.config.ts eslint.config.js   definições do empacotador e lint\n'
       '├── tsconfig.json tsconfig.app.json   definições do TypeScript\n'
       '├── run.sh run.bat                    arrancar, fluxo partilhado\n'
       '├── build.sh build.bat                compilar e testar, fluxo partilhado\n'
       '├── build-test.sh build-test.bat      compilar, testar e empacotar\n'
       '├── test.sh test.bat                  só os testes, nunca a versão\n'
       '└── SECURITY.md SUPPORT.md CONTRIBUTING.md CODE_OF_CONDUCT.md LICENSE'}

DIAGRAM = 'flowchart LR\n    B["Browser"] -->|"static files"| H["tools/serve.mjs (static host)"]\n    B -->|"HttpOnly session, JSON, MJPEG"| S["ARMOR-SERVER"]\n    H -->|"/armor-config.json"| B'

NT = "1004"
FACTS["badges"] = [x for x in FACTS["badges"] if x[0] != "Tests"] + [["Tests", NT + "%20passing", "2ea44f"]]

# the claims of the previous README that the code no longer supports, corrected in every language
SESSION = {"en": ("an 8-hour **HttpOnly** session", "a 7-day **HttpOnly** session"), "es": ("una sesión **HttpOnly** de 8 horas", "una sesión **HttpOnly** de 7 días"),
           "de": ("**HttpOnly**-Sitzung von 8 Stunden", "**HttpOnly**-Sitzung von 7 Tagen"), "fr": ("session **HttpOnly** de 8 heures", "session **HttpOnly** de 7 jours"),
           "it": ("sessione **HttpOnly** di 8 ore", "sessione **HttpOnly** di 7 giorni"), "ja": ("8 時間の **HttpOnly** セッション", "7 日間の **HttpOnly** セッション"),
           "zh": ("8 小时的 **HttpOnly** 会话", "7 天的 **HttpOnly** 会话"), "pt": ("sessão **HttpOnly** de 8 horas", "sessão **HttpOnly** de 7 dias")}
THEMES = {"en": ("eleven themes", "sixteen themes"), "es": ("once temas", "dieciséis temas"), "de": ("elf Themen", "sechzehn Themen"), "fr": ("onze thèmes", "seize thèmes"),
          "it": ("undici temi", "sedici temi"), "ja": ("11 のテーマ", "16 のテーマ"), "zh": ("十一种主题", "十六种主题"), "pt": ("onze temas", "dezasseis temas")}
WEATHER = P("**Only the Weather menu reaches other services.** Fonts are local stacks and nothing else asks a third party for anything. The Weather menu, and only for an account with a saved place, loads Open-Meteo (forecast, geocoding, air quality), RainViewer (radar), EUMETSAT (clouds) and ArcGIS (map tiles). The static host sends `Content-Security-Policy: default-src 'self'` limited to the configured server and those services, `frame-ancestors 'none'`, `nosniff` and `no-referrer`.",
            "**Solo el menú del Tiempo llega a otros servicios.** Las fuentes son locales y nada más pide algo a un tercero. El menú del Tiempo, y solo con una cuenta que tenga un lugar guardado, carga Open-Meteo (previsión, geocodificación, calidad del aire), RainViewer (radar), EUMETSAT (nubes) y ArcGIS (teselas del mapa). El servidor estático envía `Content-Security-Policy: default-src 'self'` limitada al servidor configurado y a esos servicios, `frame-ancestors 'none'`, `nosniff` y `no-referrer`.",
            "**Nur das Wetter-Menü erreicht andere Dienste.** Schriften sind lokal und sonst fragt nichts einen Dritten an. Das Wetter-Menü, und nur bei einem Konto mit gespeichertem Ort, lädt Open-Meteo (Vorhersage, Geokodierung, Luftqualität), RainViewer (Radar), EUMETSAT (Wolken) und ArcGIS (Kartenkacheln). Der statische Host sendet `Content-Security-Policy: default-src 'self'`, beschränkt auf den konfigurierten Server und diese Dienste, `frame-ancestors 'none'`, `nosniff` und `no-referrer`.",
            "**Seul le menu Météo atteint d'autres services.** Les polices sont locales et rien d'autre ne demande quoi que ce soit à un tiers. Le menu Météo, et seulement pour un compte ayant un lieu enregistré, charge Open-Meteo (prévisions, géocodage, qualité de l'air), RainViewer (radar), EUMETSAT (nuages) et ArcGIS (tuiles de carte). L'hôte statique envoie `Content-Security-Policy: default-src 'self'` limitée au serveur configuré et à ces services, `frame-ancestors 'none'`, `nosniff` et `no-referrer`.",
            "**Solo il menu Meteo raggiunge altri servizi.** I caratteri sono locali e nient'altro chiede qualcosa a terzi. Il menu Meteo, e solo per un account con un luogo salvato, carica Open-Meteo (previsioni, geocodifica, qualità dell'aria), RainViewer (radar), EUMETSAT (nuvole) e ArcGIS (tessere della mappa). L'host statico invia `Content-Security-Policy: default-src 'self'` limitata al server configurato e a quei servizi, `frame-ancestors 'none'`, `nosniff` e `no-referrer`.",
            "**他のサービスに接続するのは天気メニューだけです。** フォントはローカルで、ほかにサードパーティへ要求するものはありません。天気メニューは、場所を保存したアカウントでのみ、Open-Meteo（予報、ジオコーディング、大気質）、RainViewer（レーダー）、EUMETSAT（雲）、ArcGIS（地図タイル）を読み込みます。静的ホストは、設定されたサーバーとこれらのサービスに限定した `Content-Security-Policy: default-src 'self'`、`frame-ancestors 'none'`、`nosniff`、`no-referrer` を送ります。",
            "**只有天气菜单会访问其他服务。** 字体来自本地，其余部分不向第三方请求任何内容。天气菜单仅在账户保存了地点时才会加载 Open-Meteo（预报、地理编码、空气质量）、RainViewer（雷达）、EUMETSAT（云图）和 ArcGIS（地图瓦片）。静态主机发送限于所配置服务器和这些服务的 `Content-Security-Policy: default-src 'self'`、`frame-ancestors 'none'`、`nosniff` 和 `no-referrer`。",
            "**Só o menu do Tempo chega a outros serviços.** Os tipos de letra são locais e nada mais pede algo a terceiros. O menu do Tempo, e só numa conta com um local guardado, carrega Open-Meteo (previsão, geocodificação, qualidade do ar), RainViewer (radar), EUMETSAT (nuvens) e ArcGIS (mosaicos do mapa). O servidor estático envia `Content-Security-Policy: default-src 'self'` limitado ao servidor configurado e a esses serviços, `frame-ancestors 'none'`, `nosniff` e `no-referrer`.")


def fix(lg, s):
    a, b = SESSION[lg]
    c, d = THEMES[lg]
    return s.replace(a, b).replace(c, d).replace("990", NT).replace("982", NT).replace("961", NT)


def L(lg, key):
    v = LEGACY[lg][key]
    return fix(lg, v) if isinstance(v, str) else [fix(lg, x) for x in v]


def sec(lg):
    return [fix(lg, b) for b in LEGACY[lg]["sections"][0]["bullets"]]


GLANCE = [
    (GL["role"], T("Operations and design console of the family | Consola de operación y diseño de la familia | Bedien- und Entwurfskonsole der Familie | Console d'exploitation et de conception de la famille | Console di operatività e progettazione della famiglia | ファミリーの運用・設計コンソール | 家族的运维与设计控制台 | Consola de operação e desenho da família")),
    (GL["stack"], "React 19, TypeScript, Vite, Three.js, Leaflet"),
    (GL["tests"], T("NTESTS (`npm test`, Vitest) and browser tests (Playwright) | NTESTS (`npm test`, Vitest) y pruebas de navegador (Playwright) | NTESTS (`npm test`, Vitest) und Browser-Tests (Playwright) | NTESTS (`npm test`, Vitest) et tests navigateur (Playwright) | NTESTS (`npm test`, Vitest) e test nel browser (Playwright) | NTESTS 件（`npm test`、Vitest）とブラウザーテスト（Playwright） | NTESTS 项（`npm test`，Vitest）和浏览器测试（Playwright） | NTESTS (`npm test`, Vitest) e testes de navegador (Playwright)".replace("NTESTS", NT))),
    (GL["contract"], T("Talks only to ARMOR-SERVER (HTTP `/api/v1/*` with an HttpOnly session, WebSocket `/api/v1/events`) | Habla solo con ARMOR-SERVER (HTTP `/api/v1/*` con sesión HttpOnly, WebSocket `/api/v1/events`) | Spricht nur mit ARMOR-SERVER (HTTP `/api/v1/*` mit HttpOnly-Sitzung, WebSocket `/api/v1/events`) | Ne parle qu'à ARMOR-SERVER (HTTP `/api/v1/*` avec session HttpOnly, WebSocket `/api/v1/events`) | Parla solo con ARMOR-SERVER (HTTP `/api/v1/*` con sessione HttpOnly, WebSocket `/api/v1/events`) | ARMOR-SERVER とだけ通信（HttpOnly セッションの HTTP `/api/v1/*`、WebSocket `/api/v1/events`） | 只与 ARMOR-SERVER 通信（带 HttpOnly 会话的 HTTP `/api/v1/*`、WebSocket `/api/v1/events`） | Só fala com o ARMOR-SERVER (HTTP `/api/v1/*` com sessão HttpOnly, WebSocket `/api/v1/events`)")),
    (GL["listens"], T("`127.0.0.1:5178` (`tools/serve.mjs`) | `127.0.0.1:5178` (`tools/serve.mjs`) | `127.0.0.1:5178` (`tools/serve.mjs`) | `127.0.0.1:5178` (`tools/serve.mjs`) | `127.0.0.1:5178` (`tools/serve.mjs`) | `127.0.0.1:5178`（`tools/serve.mjs`） | `127.0.0.1:5178`（`tools/serve.mjs`） | `127.0.0.1:5178` (`tools/serve.mjs`)")),
    (GL["runs"], T("A browser; the files are served by `tools/serve.mjs` or by the nginx of the container | Un navegador; los ficheros los sirve `tools/serve.mjs` o el nginx del contenedor | Ein Browser; die Dateien liefert `tools/serve.mjs` oder das nginx des Containers | Un navigateur ; les fichiers sont servis par `tools/serve.mjs` ou par le nginx du conteneur | Un browser; i file li serve `tools/serve.mjs` o il nginx del container | ブラウザー。ファイルは `tools/serve.mjs` またはコンテナの nginx が配信 | 浏览器；文件由 `tools/serve.mjs` 或容器中的 nginx 提供 | Um navegador; os ficheiros são servidos por `tools/serve.mjs` ou pelo nginx do contentor")),
    (GL["hardware"], {lg: LEGACY[lg]["hardware"] for lg in LGS}),
    (GL["license"], LICENSE_VALUE),
]

ROLE_TABLE = [
    ("ARMOR-SERVER", T("HTTP, WebSocket and MJPEG with the HttpOnly session | HTTP, WebSocket y MJPEG con la sesión HttpOnly | HTTP, WebSocket und MJPEG mit der HttpOnly-Sitzung | HTTP, WebSocket et MJPEG avec la session HttpOnly | HTTP, WebSocket e MJPEG con la sessione HttpOnly | HttpOnly セッションでの HTTP、WebSocket、MJPEG | 带 HttpOnly 会话的 HTTP、WebSocket 和 MJPEG | HTTP, WebSocket e MJPEG com a sessão HttpOnly"),
     T("everything: state, orders, designs, cameras | todo: estado, órdenes, diseños, cámaras | alles: Zustand, Befehle, Entwürfe, Kameras | tout : état, ordres, conceptions, caméras | tutto: stato, ordini, progetti, telecamere | すべて：状態、オーダー、設計、カメラ | 一切：状态、指令、设计、摄像头 | tudo: estado, ordens, desenhos, câmaras")),
    (T("Each node's own panel | El panel propio de cada nodo | Das eigene Panel jedes Knotens | Le panneau propre de chaque nœud | Il pannello proprio di ogni nodo | 各ノード自身のパネル | 各节点自己的面板 | O painel próprio de cada nó"), T("a link, through the server's proxy | un enlace, a través del proxy del servidor | ein Link über den Proxy des Servers | un lien, via le proxy du serveur | un collegamento, tramite il proxy del server | サーバーのプロキシ経由のリンク | 经服务器代理的链接 | uma ligação, através do proxy do servidor"),
     T("the only exception to \"it never talks to a node\" | la única excepción a \"nunca habla con un nodo\" | die einzige Ausnahme von \"spricht nie mit einem Knoten\" | la seule exception à « ne parle jamais à un nœud » | l'unica eccezione a \"non parla mai con un nodo\" | 「ノードとは直接通信しない」の唯一の例外 | “从不直接与节点通信”的唯一例外 | a única exceção a \"nunca fala com um nó\"")),
    (T("Weather services | Servicios del tiempo | Wetterdienste | Services météo | Servizi meteo | 天気サービス | 天气服务 | Serviços do tempo"), "Open-Meteo, RainViewer, EUMETSAT, ArcGIS",
     T("only the Weather menu, only with a saved place | solo el menú del Tiempo, solo con lugar guardado | nur das Wetter-Menü, nur mit gespeichertem Ort | seulement le menu Météo, seulement avec un lieu enregistré | solo il menu Meteo, solo con luogo salvato | 天気メニューのみ、場所を保存した場合のみ | 仅天气菜单，仅在保存了地点时 | só o menu do Tempo, só com local guardado")),
    ("ARMOR-DEVOPS", T("installs the stack on the CM5 test bench | instala la pila en el banco de la CM5 | installiert den Stack auf dem CM5-Prüfstand | installe la pile sur le banc d'essai CM5 | installa lo stack sul banco di prova CM5 | CM5 テストベンチへスタックをインストール | 在 CM5 测试台上安装整套软件 | instala a pilha na bancada do CM5"),
     T("deployment | despliegue | Bereitstellung | déploiement | distribuzione | デプロイ | 部署 | implantação")),
]
ROLE_TABLE = [(a if not isinstance(a, tuple) else a, *rest) for a, *rest in ROLE_TABLE]


def S(threat, defence):
    return (T(threat), T(defence))


SECURITY_ROWS = [
    S("Secrets in the browser | Secretos en el navegador | Geheimnisse im Browser | Secrets dans le navigateur | Segreti nel browser | ブラウザー内の秘密 | 浏览器中的机密 | Segredos no navegador",
      "No password, token, session or camera credential is ever stored; a snapshot address with a login (`user:pass@` or `?pwd=`) is refused; signing out empties the console and the state of firmware jobs | Nunca se guarda contraseña, token, sesión ni credencial de cámara; se rechaza una dirección de instantánea con login (`user:pass@` o `?pwd=`); cerrar sesión vacía la consola y el estado de los trabajos de firmware | Nie werden Passwort, Token, Sitzung oder Kameraanmeldedaten gespeichert; eine Standbild-Adresse mit Login (`user:pass@` oder `?pwd=`) wird abgelehnt; beim Abmelden werden Konsole und Firmware-Aufträge geleert | Jamais de mot de passe, jeton, session ou identifiant de caméra stocké ; une adresse d'instantané avec identifiants (`user:pass@` ou `?pwd=`) est refusée ; se déconnecter vide la console et l'état des travaux de firmware | Mai salvati password, token, sessione o credenziali di telecamera; un indirizzo di istantanea con login (`user:pass@` o `?pwd=`) è rifiutato; uscire svuota la console e lo stato dei lavori firmware | パスワード、トークン、セッション、カメラの認証情報は一切保存しません。ログイン付きのスナップショットアドレス（`user:pass@` や `?pwd=`）は拒否し、サインアウトでコンソールとファームウェアジョブの状態を空にします | 从不保存密码、令牌、会话或摄像头凭据；带登录信息的快照地址（`user:pass@` 或 `?pwd=`）会被拒绝；退出登录会清空控制台和固件任务状态 | Nunca se guarda palavra-passe, token, sessão nem credencial de câmara; um endereço de instantâneo com login (`user:pass@` ou `?pwd=`) é recusado; terminar a sessão esvazia a consola e o estado das tarefas de firmware"),
    S("Session theft | Robo de sesión | Sitzungsdiebstahl | Vol de session | Furto di sessione | セッションの盗難 | 会话被盗 | Roubo de sessão",
      "HttpOnly, SameSite=Strict cookie set by the server (`armor_studio_sid`, or `__Host-armor_studio_sid` over HTTPS); Studio checks it every minute | Cookie HttpOnly y SameSite=Strict puesta por el servidor (`armor_studio_sid`, o `__Host-armor_studio_sid` con HTTPS); Studio la comprueba cada minuto | HttpOnly-Cookie mit SameSite=Strict vom Server gesetzt (`armor_studio_sid`, bei HTTPS `__Host-armor_studio_sid`); Studio prüft sie jede Minute | Cookie HttpOnly et SameSite=Strict posé par le serveur (`armor_studio_sid`, ou `__Host-armor_studio_sid` en HTTPS) ; Studio la vérifie chaque minute | Cookie HttpOnly e SameSite=Strict impostato dal server (`armor_studio_sid`, o `__Host-armor_studio_sid` con HTTPS); Studio la verifica ogni minuto | サーバーが設定する HttpOnly・SameSite=Strict の Cookie（`armor_studio_sid`、HTTPS では `__Host-armor_studio_sid`）。Studio は毎分確認します | 由服务器设置的 HttpOnly、SameSite=Strict Cookie（`armor_studio_sid`，HTTPS 下为 `__Host-armor_studio_sid`）；Studio 每分钟检查一次 | Cookie HttpOnly e SameSite=Strict definido pelo servidor (`armor_studio_sid`, ou `__Host-armor_studio_sid` com HTTPS); o Studio verifica-o a cada minuto"),
    S("Tampered browser storage | Almacenamiento del navegador manipulado | Manipulierter Browser-Speicher | Stockage du navigateur altéré | Archivio del browser manomesso | 改ざんされたブラウザー保存データ | 被篡改的浏览器存储 | Armazenamento do navegador adulterado",
      "Everything read from `localStorage` is parsed value by value: an invalid origin, theme, language or shape is dropped, positions are clamped and lists are capped; the storage schema is versioned | Todo lo leído de `localStorage` se analiza valor a valor: un origen, tema, idioma o forma inválidos se descarta, las posiciones se acotan y las listas tienen tope; el esquema de almacenamiento lleva versión | Alles aus `localStorage` wird Wert für Wert geprüft: ungültiger Ursprung, ungültiges Thema, ungültige Sprache oder Form wird verworfen, Positionen werden begrenzt, Listen gekappt; das Speicherschema ist versioniert | Tout ce qui est lu dans `localStorage` est analysé valeur par valeur : une origine, un thème, une langue ou une forme invalide est écarté, les positions sont bornées et les listes plafonnées ; le schéma de stockage est versionné | Tutto ciò che si legge da `localStorage` è analizzato valore per valore: un'origine, un tema, una lingua o una forma non valida viene scartata, le posizioni sono limitate e le liste hanno un tetto; lo schema di archiviazione è versionato | `localStorage` から読むものはすべて値ごとに解析し、不正なオリジン・テーマ・言語・形は破棄、位置は範囲内に収め、リストには上限があります。保存スキーマにはバージョンがあります | 从 `localStorage` 读取的内容逐项解析：无效的来源、主题、语言或结构会被丢弃，位置被限制范围，列表有上限；存储模式有版本号 | Tudo o que se lê de `localStorage` é analisado valor a valor: uma origem, tema, idioma ou forma inválidos é descartado, as posições são limitadas e as listas têm teto; o esquema de armazenamento tem versão"),
    S("A malicious server address | Una dirección de servidor maliciosa | Eine bösartige Serveradresse | Une adresse de serveur malveillante | Un indirizzo di server malevolo | 悪意のあるサーバーアドレス | 恶意的服务器地址 | Um endereço de servidor malicioso",
      "Only a plain `http(s)` origin: no credentials, path, query or fragment | Solo un origen `http(s)` simple: sin credenciales, ruta, consulta ni fragmento | Nur ein einfacher `http(s)`-Ursprung: ohne Zugangsdaten, Pfad, Query oder Fragment | Seulement une origine `http(s)` simple : sans identifiants, chemin, requête ni fragment | Solo un'origine `http(s)` semplice: senza credenziali, percorso, query o frammento | 素の `http(s)` オリジンのみ（認証情報、パス、クエリ、フラグメントなし） | 只接受纯 `http(s)` 来源：没有凭据、路径、查询或片段 | Só uma origem `http(s)` simples: sem credenciais, caminho, consulta nem fragmento"),
    S("Injection, clickjacking and leaks | Inyección, clickjacking y fugas | Injection, Clickjacking und Lecks | Injection, détournement de clic et fuites | Injection, clickjacking e fughe | インジェクション、クリックジャッキング、情報漏えい | 注入、点击劫持与泄露 | Injeção, clickjacking e fugas",
      "`Content-Security-Policy: default-src 'self'; script-src 'self'; object-src 'none'; base-uri 'none'; frame-ancestors 'none'`, `connect-src` only for the configured servers and the weather services, `nosniff`, `no-referrer`, `Cross-Origin-Opener-Policy: same-origin` and a `Permissions-Policy` that turns off camera, microphone and location | `Content-Security-Policy: default-src 'self'; script-src 'self'; object-src 'none'; base-uri 'none'; frame-ancestors 'none'`, `connect-src` solo para los servidores configurados y los servicios del tiempo, `nosniff`, `no-referrer`, `Cross-Origin-Opener-Policy: same-origin` y una `Permissions-Policy` que apaga cámara, micrófono y ubicación | `Content-Security-Policy: default-src 'self'; script-src 'self'; object-src 'none'; base-uri 'none'; frame-ancestors 'none'`, `connect-src` nur für die konfigurierten Server und die Wetterdienste, `nosniff`, `no-referrer`, `Cross-Origin-Opener-Policy: same-origin` und eine `Permissions-Policy`, die Kamera, Mikrofon und Standort abschaltet | `Content-Security-Policy: default-src 'self'; script-src 'self'; object-src 'none'; base-uri 'none'; frame-ancestors 'none'`, `connect-src` seulement pour les serveurs configurés et les services météo, `nosniff`, `no-referrer`, `Cross-Origin-Opener-Policy: same-origin` et une `Permissions-Policy` qui coupe caméra, micro et localisation | `Content-Security-Policy: default-src 'self'; script-src 'self'; object-src 'none'; base-uri 'none'; frame-ancestors 'none'`, `connect-src` solo per i server configurati e i servizi meteo, `nosniff`, `no-referrer`, `Cross-Origin-Opener-Policy: same-origin` e una `Permissions-Policy` che spegne fotocamera, microfono e posizione | `Content-Security-Policy: default-src 'self'; script-src 'self'; object-src 'none'; base-uri 'none'; frame-ancestors 'none'`、`connect-src` は設定済みサーバーと天気サービスのみ、`nosniff`、`no-referrer`、`Cross-Origin-Opener-Policy: same-origin`、カメラ・マイク・位置情報を無効にする `Permissions-Policy` | `Content-Security-Policy: default-src 'self'; script-src 'self'; object-src 'none'; base-uri 'none'; frame-ancestors 'none'`，`connect-src` 仅限所配置的服务器和天气服务，`nosniff`，`no-referrer`，`Cross-Origin-Opener-Policy: same-origin`，以及关闭摄像头、麦克风和定位的 `Permissions-Policy` | `Content-Security-Policy: default-src 'self'; script-src 'self'; object-src 'none'; base-uri 'none'; frame-ancestors 'none'`, `connect-src` só para os servidores configurados e os serviços do tempo, `nosniff`, `no-referrer`, `Cross-Origin-Opener-Policy: same-origin` e uma `Permissions-Policy` que desliga câmara, microfone e localização"),
    S("Security headers lost behind nginx | Cabeceras de seguridad perdidas tras nginx | Verlorene Sicherheits-Header hinter nginx | En-têtes de sécurité perdus derrière nginx | Intestazioni di sicurezza perse dietro nginx | nginx 配下で失われるセキュリティヘッダー | nginx 后丢失的安全头 | Cabeçalhos de segurança perdidos atrás do nginx",
      "`security_headers.conf` is included in every `location` (nginx only inherits `add_header` when a location has none of its own) | `security_headers.conf` se incluye en cada `location` (nginx solo hereda `add_header` si el `location` no tiene los suyos) | `security_headers.conf` ist in jedem `location` eingebunden (nginx erbt `add_header` nur, wenn der `location` keine eigenen hat) | `security_headers.conf` est inclus dans chaque `location` (nginx n'hérite d'`add_header` que si le `location` n'a pas les siens) | `security_headers.conf` è incluso in ogni `location` (nginx eredita `add_header` solo se il `location` non ne ha di propri) | `security_headers.conf` はすべての `location` に含めます（nginx は `location` 自身が持たない場合にしか `add_header` を継承しません） | `security_headers.conf` 被包含在每个 `location` 中（nginx 只有在 location 自身没有时才继承 `add_header`） | `security_headers.conf` está incluído em cada `location` (o nginx só herda `add_header` quando o `location` não tem os seus)"),
    S("Dangerous orders to the nodes | Órdenes peligrosas a los nodos | Gefährliche Befehle an die Knoten | Ordres dangereux vers les nœuds | Ordini pericolosi ai nodi | ノードへの危険なオーダー | 对节点的危险指令 | Ordens perigosas aos nós",
      "Administrators only; the node's name (or RESTART, PAUSE, STANDBY for all) is typed again and the password is asked again; there is no erase, factory reset or power-off order | Solo administradores; se teclea de nuevo el nombre del nodo (o RESTART, PAUSE, STANDBY para todos) y se pide otra vez la contraseña; no hay orden de borrado, restablecimiento de fábrica ni apagado | Nur Administratoren; der Knotenname (oder RESTART, PAUSE, STANDBY für alle) wird erneut getippt und das Passwort erneut verlangt; es gibt keinen Lösch-, Werksreset- oder Ausschaltbefehl | Administrateurs seulement ; le nom du nœud (ou RESTART, PAUSE, STANDBY pour tous) est retapé et le mot de passe redemandé ; il n'y a pas d'ordre d'effacement, de réinitialisation d'usine ni d'extinction | Solo amministratori; il nome del nodo (o RESTART, PAUSE, STANDBY per tutti) si digita di nuovo e si richiede ancora la password; non esiste un ordine di cancellazione, ripristino di fabbrica o spegnimento | 管理者のみ。ノード名（全ノードなら RESTART、PAUSE、STANDBY）を再入力し、パスワードも再度求めます。消去、初期化、電源オフのオーダーはありません | 仅限管理员；需再次输入节点名称（全部节点则输入 RESTART、PAUSE、STANDBY）并再次输入密码；没有擦除、恢复出厂或关机指令 | Só administradores; o nome do nó (ou RESTART, PAUSE, STANDBY para todos) é escrito de novo e a palavra-passe pedida outra vez; não há ordem de apagar, repor de fábrica nem desligar"),
    S("Roles | Roles | Rollen | Rôles | Ruoli | ロール | 角色 | Funções",
      "Administrator, operator, viewer (only looks) and wall panel (its account cannot use Studio); the `capabilities` of the session decide what is shown, and the server checks again | Administrador, operador, visor (solo mira) y panel de pared (su cuenta no puede usar Studio); las `capabilities` de la sesión deciden qué se muestra y el servidor vuelve a comprobar | Administrator, Bediener, Betrachter (schaut nur) und Wandpanel (sein Konto kann Studio nicht nutzen); die `capabilities` der Sitzung bestimmen, was angezeigt wird, und der Server prüft erneut | Administrateur, opérateur, lecteur (regarde seulement) et panneau mural (son compte ne peut pas utiliser Studio) ; les `capabilities` de la session décident de l'affichage et le serveur revérifie | Amministratore, operatore, visualizzatore (guarda soltanto) e pannello a muro (il suo account non può usare Studio); le `capabilities` della sessione decidono cosa si mostra e il server ricontrolla | 管理者、オペレーター、閲覧者（見るだけ）、壁面パネル（そのアカウントは Studio を使えません）。セッションの `capabilities` が表示を決め、サーバーが再検証します | 管理员、操作员、查看者（只看）和壁挂面板（其账户不能使用 Studio）；会话的 `capabilities` 决定显示内容，服务器会再次校验 | Administrador, operador, visualizador (só vê) e painel de parede (a sua conta não pode usar o Studio); as `capabilities` da sessão decidem o que se mostra e o servidor volta a verificar"),
]

SECURITY_TAIL = P(
    "**Switches.** *Configuration > Security* has a control for each of the 13 protections that ARMOR-SERVER lets an administrator tune (disarm PIN, silencing by voice, signature of the alarm design, zone feed, camera tunnel, network logins, wall-panel live events, device lock, node storage encryption and the audio limits), with a conservative default; the server keeps lowering one in its audit. Details in [docs/SECURITY_MODEL.md](docs/SECURITY_MODEL.md). There has been no independent security review.",
    "**Interruptores.** *Configuración > Seguridad* tiene un control para cada una de las 13 protecciones que ARMOR-SERVER deja ajustar a un administrador (PIN de desarme, silenciar por voz, firma del diseño de alarma, aviso de zonas, túnel de cámaras, accesos de red, eventos en vivo del panel de pared, bloqueo de dispositivo, cifrado del almacenamiento de nodos y los límites de audio), cada una con un valor por defecto conservador; el servidor deja en su auditoría que se baje una. Detalles en [docs/SECURITY_MODEL.md](docs/SECURITY_MODEL.md). No ha habido revisión de seguridad independiente.",
    "**Schalter.** *Konfiguration > Sicherheit* hat ein Bedienelement für jeden der 13 Schutzmechanismen, die ARMOR-SERVER einem Administrator zum Einstellen überlässt (Entschärf-PIN, Stummschalten per Sprache, Signatur des Alarmentwurfs, Zonen-Feed, Kameratunnel, Netzwerk-Logins, Live-Ereignisse des Wandpanels, Gerätesperre, Verschlüsselung des Knotenspeichers und die Audiogrenzen), jeweils mit konservativem Standard; der Server hält das Absenken im Audit fest. Einzelheiten in [docs/SECURITY_MODEL.md](docs/SECURITY_MODEL.md). Eine unabhängige Sicherheitsprüfung gab es nicht.",
    "**Interrupteurs.** *Configuration > Sécurité* a une commande pour chacune des 13 protections qu'ARMOR-SERVER laisse régler à un administrateur (PIN de désarmement, coupure par la voix, signature de la conception d'alarme, flux de zones, tunnel des caméras, identifiants réseau, événements en direct du panneau mural, verrouillage d'appareil, chiffrement du stockage des nœuds et limites audio), chacune avec un défaut prudent ; le serveur consigne dans son audit qu'on en abaisse une. Détails dans [docs/SECURITY_MODEL.md](docs/SECURITY_MODEL.md). Il n'y a pas eu de revue de sécurité indépendante.",
    "**Interruttori.** *Configurazione > Sicurezza* ha un controllo per ciascuna delle 13 protezioni che ARMOR-SERVER lascia regolare a un amministratore (PIN di disarmo, silenziamento a voce, firma del progetto di allarme, flusso delle zone, tunnel delle telecamere, accessi di rete, eventi dal vivo del pannello a muro, blocco del dispositivo, cifratura dell'archivio dei nodi e limiti audio), ciascuna con un default prudente; il server registra nell'audit che se ne abbassa una. Dettagli in [docs/SECURITY_MODEL.md](docs/SECURITY_MODEL.md). Non c'è stata una revisione di sicurezza indipendente.",
    "**スイッチ。** *設定 > セキュリティ* には、ARMOR-SERVER が管理者に調整を許す 13 の保護（解除 PIN、音声での消音、アラーム設計の署名、ゾーンフィード、カメラのトンネル、ネットワークのログイン、壁面パネルのライブイベント、デバイスロック、ノード保存領域の暗号化、音声の上限）それぞれのコントロールがあり、既定値は保守的です。下げた場合はサーバーの監査に残ります。詳細は [docs/SECURITY_MODEL.md](docs/SECURITY_MODEL.md)。第三者によるセキュリティレビューはありません。",
    "**开关。** *配置 > 安全* 为 ARMOR-SERVER 允许管理员调整的 13 项保护各提供一个控件（撤防 PIN、语音静音、报警设计签名、区域推送、摄像头隧道、网络登录、壁挂面板实时事件、设备锁、节点存储加密和音频限制），默认值都很保守；调低任何一项服务器都会写入审计。详见 [docs/SECURITY_MODEL.md](docs/SECURITY_MODEL.md)。没有独立的安全审查。",
    "**Interruptores.** *Configuração > Segurança* tem um controlo para cada uma das 13 proteções que o ARMOR-SERVER deixa um administrador ajustar (PIN de desarme, silenciar por voz, assinatura do desenho de alarme, feed de zonas, túnel das câmaras, credenciais de rede, eventos em direto do painel de parede, bloqueio de dispositivo, cifra do armazenamento dos nós e os limites de áudio), cada uma com um valor predefinido conservador; o servidor deixa na auditoria que se baixe uma. Detalhes em [docs/SECURITY_MODEL.md](docs/SECURITY_MODEL.md). Não houve revisão de segurança independente.")

IFACE = [
    ("`/api/v1/*`", T("session cookie | cookie de sesión | Sitzungs-Cookie | cookie de session | cookie di sessione | セッション Cookie | 会话 Cookie | cookie de sessão"), T("the client of the server, split by area in `src/api/`; `src/api/routes.test.ts` and `src/api/contract/` check it against the contract | el cliente del servidor, dividido por áreas en `src/api/`; `src/api/routes.test.ts` y `src/api/contract/` lo comprueban contra el contrato | der Client des Servers, nach Bereichen in `src/api/` geteilt; `src/api/routes.test.ts` und `src/api/contract/` prüfen ihn gegen den Vertrag | le client du serveur, découpé par domaine dans `src/api/` ; `src/api/routes.test.ts` et `src/api/contract/` le vérifient contre le contrat | il client del server, diviso per aree in `src/api/`; `src/api/routes.test.ts` e `src/api/contract/` lo verificano rispetto al contratto | サーバークライアント（`src/api/` に分野別）。`src/api/routes.test.ts` と `src/api/contract/` が契約と照合 | 服务器客户端，按领域拆分在 `src/api/` 中；`src/api/routes.test.ts` 和 `src/api/contract/` 对照契约检查 | o cliente do servidor, dividido por áreas em `src/api/`; `src/api/routes.test.ts` e `src/api/contract/` verificam-no contra o contrato")),
    ("`WS /api/v1/events`", T("session | sesión | Sitzung | session | sessione | セッション | 会话 | sessão"), T("live state: an alarm, an arming or a node coming back shows at once; while it is open the status is asked only every 20 seconds as a safety net (3 seconds without it); the bottom bar says *Live* | estado en vivo: una alarma, un armado o un nodo que vuelve se ven al instante; con el canal abierto el estado se pide solo cada 20 segundos como red de seguridad (3 segundos sin él); la barra inferior dice *En vivo* | Live-Status: ein Alarm, ein Scharfschalten oder ein zurückkehrender Knoten erscheint sofort; bei offenem Kanal wird der Status nur alle 20 Sekunden als Sicherheitsnetz abgefragt (ohne ihn alle 3 Sekunden); die untere Leiste zeigt *Live* | état en direct : une alarme, un armement ou un nœud qui revient s'affiche aussitôt ; canal ouvert, l'état n'est demandé que toutes les 20 secondes par sécurité (3 secondes sans lui) ; la barre du bas indique *En direct* | stato dal vivo: un allarme, un armamento o un nodo che torna si vedono subito; con il canale aperto lo stato si chiede solo ogni 20 secondi come rete di sicurezza (3 secondi senza); la barra in basso dice *Dal vivo* | ライブ状態：アラーム、警戒、ノード復帰が即座に表示されます。チャネルが開いている間は安全網として 20 秒ごとにだけ状態を問い合わせ（なければ 3 秒ごと）、下部バーに *ライブ* と表示 | 实时状态：报警、布防或节点恢复会立即显示；通道打开时仅每 20 秒查询一次状态作为保险（没有通道时每 3 秒）；底栏显示“实时” | estado em direto: um alarme, um armamento ou um nó que volta vê-se logo; com o canal aberto o estado só é pedido a cada 20 segundos como rede de segurança (3 segundos sem ele); a barra inferior diz *Em direto*")),
    (T("MJPEG, snapshots, records | MJPEG, instantáneas, grabaciones | MJPEG, Standbilder, Aufnahmen | MJPEG, instantanés, enregistrements | MJPEG, istantanee, registrazioni | MJPEG、スナップショット、録画 | MJPEG、快照、录像 | MJPEG, instantâneos, gravações"), T("stream ticket | ticket de transmisión | Stream-Ticket | ticket de flux | ticket di flusso | ストリームチケット | 流票据 | bilhete de transmissão"), T("live video is shown only through an address the server issues to an operator; the camera passwords never reach the browser | el vídeo en vivo solo se ve por una dirección que el servidor emite a un operador; las contraseñas de cámara nunca llegan al navegador | Live-Video nur über eine Adresse, die der Server an einen Bediener ausgibt; die Kamerapasswörter erreichen den Browser nie | la vidéo en direct ne passe que par une adresse que le serveur délivre à un opérateur ; les mots de passe des caméras n'atteignent jamais le navigateur | il video dal vivo passa solo da un indirizzo che il server emette a un operatore; le password delle telecamere non arrivano mai al browser | ライブ映像はサーバーがオペレーターに発行したアドレス経由のみ。カメラのパスワードはブラウザーに届きません | 实时视频只通过服务器发给操作员的地址显示；摄像头密码从不到达浏览器 | o vídeo em direto só se vê por um endereço que o servidor emite a um operador; as palavras-passe das câmaras nunca chegam ao navegador")),
    ("`GET /armor-config.json`", T("none | ninguna | keine | aucune | nessuna | なし | 无 | nenhuma"), T("`{\"serverOrigin\": \"<origin>\" | \"same-origin\"}`, written by `tools/serve.mjs` or by nginx | `{\"serverOrigin\": \"<origen>\" | \"same-origin\"}`, lo escribe `tools/serve.mjs` o nginx | `{\"serverOrigin\": \"<Ursprung>\" | \"same-origin\"}`, von `tools/serve.mjs` oder nginx geliefert | `{\"serverOrigin\": \"<origine>\" | \"same-origin\"}`, fourni par `tools/serve.mjs` ou nginx | `{\"serverOrigin\": \"<origine>\" | \"same-origin\"}`, fornito da `tools/serve.mjs` o nginx | `{\"serverOrigin\": \"<オリジン>\" | \"same-origin\"}`、`tools/serve.mjs` または nginx が返す | `{\"serverOrigin\": \"<来源>\" | \"same-origin\"}`，由 `tools/serve.mjs` 或 nginx 提供 | `{\"serverOrigin\": \"<origem>\" | \"same-origin\"}`, fornecido por `tools/serve.mjs` ou nginx".replace('" | "', '" / "'))),
]


CFG = [
    ("`ARMOR_STUDIO_HOST`", "127.0.0.1", T("address the static host listens on | dirección en la que escucha el host estático | Adresse, auf der der statische Host lauscht | adresse d'écoute de l'hôte statique | indirizzo su cui ascolta l'host statico | 静的ホストの待ち受けアドレス | 静态主机监听的地址 | endereço em que o anfitrião estático escuta")),
    ("`ARMOR_STUDIO_PORT`", "5178", T("port; the `studio_port` of a `connection.json` saved from Studio wins | puerto; gana el `studio_port` de un `connection.json` guardado desde Studio | Port; der `studio_port` einer aus Studio gespeicherten `connection.json` gewinnt | port ; le `studio_port` d'un `connection.json` enregistré depuis Studio l'emporte | porta; vince lo `studio_port` di un `connection.json` salvato da Studio | ポート。Studio から保存した `connection.json` の `studio_port` が優先 | 端口；从 Studio 保存的 `connection.json` 中的 `studio_port` 优先 | porta; ganha o `studio_port` de um `connection.json` guardado a partir do Studio")),
    ("`ARMOR_STUDIO_DIST`", "./dist", T("the folder of the build to serve | la carpeta de la build que se sirve | der Ordner des auszuliefernden Builds | le dossier du build à servir | la cartella della build da servire | 配信するビルドのフォルダー | 要提供的构建文件夹 | a pasta da compilação a servir")),
    ("`ARMOR_SERVER_ORIGIN`", T("empty | vacío | leer | vide | vuoto | 空 | 空 | vazio"), T("one or more origins (comma-separated) Studio starts with; it defines the `connect-src` of the policy; empty accepts the server you sign in to | uno o varios orígenes (separados por comas) con los que arranca Studio; define el `connect-src` de la política; vacío acepta el servidor al que inicias sesión | ein oder mehrere Ursprünge (kommagetrennt), mit denen Studio startet; legt das `connect-src` der Richtlinie fest; leer akzeptiert den Server, an dem man sich anmeldet | une ou plusieurs origines (séparées par des virgules) avec lesquelles Studio démarre ; elles définissent le `connect-src` de la politique ; vide accepte le serveur auquel vous vous connectez | una o più origini (separate da virgole) con cui parte Studio; definisce il `connect-src` della policy; vuoto accetta il server a cui accedi | Studio が起動時に使うオリジン（カンマ区切りで複数可）。ポリシーの `connect-src` を決めます。空ならサインインしたサーバーを受け入れます | Studio 启动时使用的一个或多个来源（逗号分隔），决定策略的 `connect-src`；为空则接受你登录的服务器 | uma ou mais origens (separadas por vírgulas) com que o Studio arranca; define o `connect-src` da política; vazio aceita o servidor em que inicia sessão")),
    ("`TLS_CERT_PATH`  `TLS_KEY_PATH`", T("off | apagado | aus | désactivé | spento | オフ | 关闭 | desligado"), T("both or none: native HTTPS of the static host | ambos o ninguno: HTTPS nativo del host estático | beide oder keines: natives HTTPS des statischen Hosts | les deux ou aucun : HTTPS natif de l'hôte statique | entrambi o nessuno: HTTPS nativo dell'host statico | 両方指定か両方なし：静的ホストのネイティブ HTTPS | 要么都设要么都不设：静态主机的原生 HTTPS | ambos ou nenhum: HTTPS nativo do anfitrião estático")),
    ("`ARMOR_PUBLIC_ORIGIN`  `ARMOR_SERVER_UPSTREAM`", "same-origin", T("in the container: what `/armor-config.json` says, and the `host:port` of the server that nginx proxies `/api/` to | en el contenedor: lo que dice `/armor-config.json` y el `host:puerto` del servidor al que nginx redirige `/api/` | im Container: was `/armor-config.json` sagt, und `host:port` des Servers, an den nginx `/api/` weiterleitet | dans le conteneur : ce que dit `/armor-config.json` et le `hôte:port` du serveur vers lequel nginx relaie `/api/` | nel container: cosa dice `/armor-config.json` e l'`host:porta` del server a cui nginx inoltra `/api/` | コンテナ内：`/armor-config.json` の内容と、nginx が `/api/` を中継するサーバーの `host:port` | 容器内：`/armor-config.json` 的内容，以及 nginx 把 `/api/` 转发到的服务器 `host:port` | no contentor: o que diz `/armor-config.json` e o `host:porta` do servidor para onde o nginx reencaminha `/api/`")),
]

CONFIG_NOTE = P(
    "Without a configured origin the client uses `http://127.0.0.1:8080`. The language, the theme (sixteen) and the weather place follow the account, not the browser. `tools/serve.mjs` reads the variables above; to install the whole stack on the CM5 test bench see [ARMOR-DEVOPS](https://github.com/JuanenRac/ARMOR-DEVOPS).",
    "Sin un origen configurado el cliente usa `http://127.0.0.1:8080`. El idioma, el tema (dieciséis) y el lugar del tiempo siguen a la cuenta, no al navegador. `tools/serve.mjs` lee las variables de arriba; para instalar toda la pila en el banco de la CM5 mira [ARMOR-DEVOPS](https://github.com/JuanenRac/ARMOR-DEVOPS).",
    "Ohne konfigurierten Ursprung nutzt der Client `http://127.0.0.1:8080`. Sprache, Thema (sechzehn) und Wetterort folgen dem Konto, nicht dem Browser. `tools/serve.mjs` liest die obigen Variablen; zur Installation des ganzen Stacks auf dem CM5-Prüfstand siehe [ARMOR-DEVOPS](https://github.com/JuanenRac/ARMOR-DEVOPS).",
    "Sans origine configurée, le client utilise `http://127.0.0.1:8080`. La langue, le thème (seize) et le lieu météo suivent le compte, pas le navigateur. `tools/serve.mjs` lit les variables ci-dessus ; pour installer toute la pile sur le banc d'essai CM5, voir [ARMOR-DEVOPS](https://github.com/JuanenRac/ARMOR-DEVOPS).",
    "Senza un'origine configurata il client usa `http://127.0.0.1:8080`. La lingua, il tema (sedici) e il luogo del meteo seguono l'account, non il browser. `tools/serve.mjs` legge le variabili sopra; per installare tutto lo stack sul banco di prova CM5 vedi [ARMOR-DEVOPS](https://github.com/JuanenRac/ARMOR-DEVOPS).",
    "オリジンを設定しない場合、クライアントは `http://127.0.0.1:8080` を使います。言語、テーマ（16 種類）、天気の場所はブラウザーではなくアカウントに従います。`tools/serve.mjs` は上の変数を読みます。CM5 テストベンチへスタック全体をインストールするには [ARMOR-DEVOPS](https://github.com/JuanenRac/ARMOR-DEVOPS) を参照してください。",
    "未配置来源时，客户端使用 `http://127.0.0.1:8080`。语言、主题（十六种）和天气地点跟随账户而不是浏览器。`tools/serve.mjs` 读取上面的变量；要在 CM5 测试台上安装整套软件，请见 [ARMOR-DEVOPS](https://github.com/JuanenRac/ARMOR-DEVOPS)。",
    "Sem origem configurada o cliente usa `http://127.0.0.1:8080`. O idioma, o tema (dezasseis) e o local do tempo seguem a conta, não o navegador. `tools/serve.mjs` lê as variáveis acima; para instalar toda a pilha na bancada do CM5 veja [ARMOR-DEVOPS](https://github.com/JuanenRac/ARMOR-DEVOPS).")

QUICK_LEAD = P("**Requirements:** Node.js 22+ and a running ARMOR-SERVER (otherwise Studio shows demonstration data and says so in the top bar).",
               "**Requisitos:** Node.js 22+ y un ARMOR-SERVER en marcha (si no, Studio muestra datos de demostración y lo dice en la barra superior).",
               "**Voraussetzungen:** Node.js 22+ und ein laufender ARMOR-SERVER (sonst zeigt Studio Demodaten und sagt das in der oberen Leiste).",
               "**Prérequis :** Node.js 22+ et un ARMOR-SERVER en marche (sinon Studio affiche des données de démonstration et le dit dans la barre du haut).",
               "**Requisiti:** Node.js 22+ e un ARMOR-SERVER in funzione (altrimenti Studio mostra dati dimostrativi e lo dice nella barra superiore).",
               "**要件：** Node.js 22+ と稼働中の ARMOR-SERVER（なければ Studio はデモデータを表示し、上部バーでそう伝えます）。",
               "**要求：** Node.js 22+ 和一个运行中的 ARMOR-SERVER（否则 Studio 显示演示数据，并在顶栏说明）。",
               "**Requisitos:** Node.js 22+ e um ARMOR-SERVER em funcionamento (senão o Studio mostra dados de demonstração e di-lo na barra superior).")
QUICK_CODE = [
    ("npm install", T("dependencies | dependencias | Abhängigkeiten | dépendances | dipendenze | 依存関係 | 依赖 | dependências")),
    ("npm run dev", T("http://127.0.0.1:5178 against a server on 127.0.0.1:8080 | http://127.0.0.1:5178 contra un servidor en 127.0.0.1:8080 | http://127.0.0.1:5178 gegen einen Server auf 127.0.0.1:8080 | http://127.0.0.1:5178 face à un serveur sur 127.0.0.1:8080 | http://127.0.0.1:5178 con un server su 127.0.0.1:8080 | 127.0.0.1:8080 のサーバーに対して http://127.0.0.1:5178 | http://127.0.0.1:5178 连接 127.0.0.1:8080 上的服务器 | http://127.0.0.1:5178 contra um servidor em 127.0.0.1:8080")),
    ("npm run typecheck", "tsc -b --noEmit"),
    ("npm run locales", T("write the table of each language after changing a phrase | escribe la tabla de cada idioma tras cambiar una frase | die Tabelle jeder Sprache nach einer Änderung schreiben | écrit la table de chaque langue après un changement de phrase | scrive la tabella di ogni lingua dopo aver cambiato una frase | 文言を変えたら各言語の表を書き出す | 修改文案后写出每种语言的表 | escreve a tabela de cada idioma depois de mudar uma frase")),
    ("npm test", T("NTESTS tests | NTESTS pruebas | NTESTS Tests | NTESTS tests | NTESTS test | NTESTS 件 | NTESTS 项 | NTESTS testes".replace("NTESTS", NT))),
    ("npm run build", "dist/"),
    ('$env:ARMOR_SERVER_ORIGIN = "http://192.168.0.180:18080"; node tools/serve.mjs', T("serve the build | sirve la build | den Build ausliefern | sert le build | serve la build | ビルドを配信 | 提供构建 | serve a compilação")),
]

TEST_TABLE = [
    (T("Settings, cameras and the radar map | Ajustes, cámaras y el mapa del radar | Einstellungen, Kameras und die Radarkarte | Réglages, caméras et la carte radar | Impostazioni, telecamere e la mappa radar | 設定、カメラ、レーダーマップ | 设置、摄像头与雷达地图 | Definições, câmaras e o mapa do radar"), T("parsing of stored settings, camera merging, radar targets and ignore zones | análisis de ajustes guardados, fusión de cámaras, objetivos del radar y zonas a ignorar | Auswertung gespeicherter Einstellungen, Kamera-Zusammenführung, Radarziele und Ignorierzonen | analyse des réglages enregistrés, fusion des caméras, cibles radar et zones à ignorer | analisi delle impostazioni salvate, fusione delle telecamere, bersagli radar e zone da ignorare | 保存設定の解析、カメラの統合、レーダー目標、無視ゾーン | 已存设置的解析、摄像头合并、雷达目标与忽略区 | análise das definições guardadas, fusão das câmaras, alvos do radar e zonas a ignorar")),
    (T("Energy | Energía | Energie | Énergie | Energia | エネルギー | 能源 | Energia"), T("the arithmetic of the solar charts, the batteries and the electrical menus | la aritmética de las gráficas solares y los menús de baterías y eléctrico | die Arithmetik der Solardiagramme und der Batterie- und Elektro-Menüs | l'arithmétique des graphiques solaires et des menus batteries et électrique | l'aritmetica dei grafici solari e dei menu batterie ed elettrico | 太陽光グラフの計算、バッテリーと電気のメニュー | 光伏图表的计算以及电池和电气菜单 | a aritmética dos gráficos solares e dos menus de baterias e elétrico")),
    (T("Designers | Diseñadores | Designer | Concepteurs | Progettisti | デザイナー | 设计器 | Desenhadores"), T("geometry, operations and checks of the Site, Electrical, Alarm and Network Designers | geometría, operaciones y comprobaciones de los Diseñadores de emplazamiento, eléctrico, de alarma y de red | Geometrie, Operationen und Prüfungen der Standort-, Elektro-, Alarm- und Netzwerk-Designer | géométrie, opérations et contrôles des concepteurs de site, électrique, alarme et réseau | geometria, operazioni e controlli dei progettisti di sito, elettrico, allarme e rete | サイト・電気・アラーム・ネットワークデザイナーの図形、操作、検査 | 场地、电气、报警和网络设计器的几何、操作与检查 | geometria, operações e verificações dos desenhadores do local, elétrico, de alarme e de rede")),
    (T("Alerts and assistant | Avisos y asistente | Alarme und Assistent | Alertes et assistant | Avvisi e assistente | 通知とアシスタント | 提醒与助手 | Alertas e assistente"), T("the announcer of alarms and connections, the assistant's dictionary and the tours | el anunciador de alarmas y conexiones, el diccionario del asistente y las visitas | der Ansager für Alarme und Verbindungen, das Wörterbuch des Assistenten und die Touren | l'annonceur d'alarmes et de connexions, le dictionnaire de l'assistant et les visites | l'annunciatore di allarmi e connessioni, il dizionario dell'assistente e i tour | 警報と接続のアナウンサー、アシスタントの辞書、ツアー | 报警与连接播报、助手词典和导览 | o anunciador de alarmes e ligações, o dicionário do assistente e as visitas")),
    (T("Every menu in eight languages | Cada menú en ocho idiomas | Jedes Menü in acht Sprachen | Chaque menu en huit langues | Ogni menu in otto lingue | 8 言語すべてのメニュー | 八种语言的每个菜单 | Cada menu em oito idiomas"), T("each screen is rendered in every language, with no phrase left as its raw key | cada pantalla se pinta en cada idioma, sin ninguna frase con su clave cruda | jeder Bildschirm wird in jeder Sprache gezeichnet, ohne Satz mit rohem Schlüssel | chaque écran est rendu dans chaque langue, sans phrase restée à l'état de clé brute | ogni schermata è disegnata in ogni lingua, senza frasi rimaste come chiave grezza | 各画面を全言語で描画し、生のキーのまま残る文言がないことを確認 | 每个界面都以每种语言渲染，不留下原始键名 | cada ecrã é desenhado em cada idioma, sem nenhuma frase com a chave em bruto")),
    (T("API client and static host | Cliente de API y host estático | API-Client und statischer Host | Client d'API et hôte statique | Client API e host statico | API クライアントと静的ホスト | API 客户端与静态主机 | Cliente da API e anfitrião estático"), T("the routes and contracts of `src/api/`, and `tools/serve.test.mjs` (headers, `/armor-config.json`, native TLS) | las rutas y contratos de `src/api/` y `tools/serve.test.mjs` (cabeceras, `/armor-config.json`, TLS nativo) | die Routen und Verträge von `src/api/` und `tools/serve.test.mjs` (Header, `/armor-config.json`, natives TLS) | les routes et contrats de `src/api/` et `tools/serve.test.mjs` (en-têtes, `/armor-config.json`, TLS natif) | le rotte e i contratti di `src/api/` e `tools/serve.test.mjs` (intestazioni, `/armor-config.json`, TLS nativo) | `src/api/` のルートと契約、`tools/serve.test.mjs`（ヘッダー、`/armor-config.json`、ネイティブ TLS） | `src/api/` 的路由与契约，以及 `tools/serve.test.mjs`（头、`/armor-config.json`、原生 TLS） | as rotas e contratos de `src/api/`, e `tools/serve.test.mjs` (cabeçalhos, `/armor-config.json`, TLS nativo)")),
    (T("Browser tests | Pruebas de navegador | Browser-Tests | Tests navigateur | Test nel browser | ブラウザーテスト | 浏览器测试 | Testes de navegador"), T("`e2e/tests` with Playwright against a stack with a real server (`e2e/README.md`) | `e2e/tests` con Playwright contra una pila con servidor real (`e2e/README.md`) | `e2e/tests` mit Playwright gegen einen Stack mit echtem Server (`e2e/README.md`) | `e2e/tests` avec Playwright contre une pile avec un vrai serveur (`e2e/README.md`) | `e2e/tests` con Playwright contro uno stack con server reale (`e2e/README.md`) | 実サーバーのスタックに対する Playwright の `e2e/tests`（`e2e/README.md`） | 针对带真实服务器的整套环境、用 Playwright 运行的 `e2e/tests`（`e2e/README.md`） | `e2e/tests` com Playwright contra uma pilha com servidor real (`e2e/README.md`)")),
]
TEST_NOTE = P(
    "The native-TLS test of the static host needs `openssl` installed. `npm run locales:check` fails when a table of a language is not generated from its phrases. GitHub Actions runs the A.R.M.O.R. baseline on every push and pull request: the validation of the manifest, version, changelog and README parity, then the project's own build and tests.",
    "La prueba del TLS nativo del host estático necesita `openssl` instalado. `npm run locales:check` falla si la tabla de un idioma no está generada desde sus frases. GitHub Actions ejecuta la base de A.R.M.O.R. en cada push y pull request: la validación del manifiesto, la versión, el registro de cambios y la paridad de los README, y luego la compilación y las pruebas del propio proyecto.",
    "Der Test des nativen TLS des statischen Hosts braucht installiertes `openssl`. `npm run locales:check` schlägt fehl, wenn die Tabelle einer Sprache nicht aus ihren Sätzen erzeugt ist. GitHub Actions führt bei jedem Push und Pull Request die A.R.M.O.R.-Basis aus: die Prüfung von Manifest, Version, Änderungsprotokoll und README-Parität, dann den eigenen Build und die eigenen Tests des Projekts.",
    "Le test du TLS natif de l'hôte statique demande `openssl` installé. `npm run locales:check` échoue si la table d'une langue n'est pas générée depuis ses phrases. GitHub Actions exécute la base A.R.M.O.R. à chaque push et pull request : la validation du manifeste, de la version, du journal des modifications et de la parité des README, puis le build et les tests propres au projet.",
    "Il test del TLS nativo dell'host statico richiede `openssl` installato. `npm run locales:check` fallisce se la tabella di una lingua non è generata dalle sue frasi. GitHub Actions esegue la base A.R.M.O.R. a ogni push e pull request: la validazione di manifesto, versione, registro delle modifiche e parità dei README, poi la compilazione e i test del progetto.",
    "静的ホストのネイティブ TLS テストには `openssl` が必要です。`npm run locales:check` は、ある言語の表がその文言から生成されていないと失敗します。GitHub Actions は push と pull request のたびに A.R.M.O.R. の基本検査（マニフェスト、バージョン、変更履歴、README の一致）と、プロジェクト自身のビルドとテストを実行します。",
    "静态主机的原生 TLS 测试需要安装 `openssl`。如果某种语言的表不是由其文案生成的，`npm run locales:check` 会失败。GitHub Actions 在每次推送和拉取请求时运行 A.R.M.O.R. 基线：清单、版本、更新日志和 README 一致性的校验，然后是项目自身的构建和测试。",
    "O teste do TLS nativo do anfitrião estático precisa de `openssl` instalado. `npm run locales:check` falha se a tabela de um idioma não for gerada a partir das suas frases. O GitHub Actions executa a base do A.R.M.O.R. em cada push e pull request: a validação do manifesto, da versão, do registo de alterações e da paridade dos README, e depois a compilação e os testes do próprio projeto.")

BUILD = P("`npm run build` writes the static site to `dist/`; the `Dockerfile` builds it with Node 22 and serves it with nginx (`nginx/`). The version lives in `package.json`, in `armor.project.json` and in the README badge (read from the manifest); each version has its entry in [CHANGELOG.md](CHANGELOG.md). Releases are published on GitHub.",
          "`npm run build` escribe el sitio estático en `dist/`; el `Dockerfile` lo construye con Node 22 y lo sirve con nginx (`nginx/`). La versión vive en `package.json`, en `armor.project.json` y en la insignia del README (leída del manifiesto); cada versión tiene su entrada en [CHANGELOG.md](CHANGELOG.md). Las versiones se publican en GitHub.",
          "`npm run build` schreibt die statische Seite nach `dist/`; das `Dockerfile` baut sie mit Node 22 und liefert sie mit nginx aus (`nginx/`). Die Version steht in `package.json`, in `armor.project.json` und im README-Badge (aus dem Manifest gelesen); jede Version hat ihren Eintrag in [CHANGELOG.md](CHANGELOG.md). Releases werden auf GitHub veröffentlicht.",
          "`npm run build` écrit le site statique dans `dist/` ; le `Dockerfile` le construit avec Node 22 et le sert avec nginx (`nginx/`). La version se trouve dans `package.json`, dans `armor.project.json` et dans le badge du README (lu depuis le manifeste) ; chaque version a son entrée dans [CHANGELOG.md](CHANGELOG.md). Les versions sont publiées sur GitHub.",
          "`npm run build` scrive il sito statico in `dist/`; il `Dockerfile` lo costruisce con Node 22 e lo serve con nginx (`nginx/`). La versione risiede in `package.json`, in `armor.project.json` e nel badge del README (letto dal manifesto); ogni versione ha la sua voce in [CHANGELOG.md](CHANGELOG.md). Le versioni sono pubblicate su GitHub.",
          "`npm run build` は静的サイトを `dist/` に書き出します。`Dockerfile` は Node 22 でビルドし、nginx（`nginx/`）で配信します。バージョンは `package.json`、`armor.project.json`、README のバッジ（マニフェストから読み取り）にあり、各バージョンには [CHANGELOG.md](CHANGELOG.md) にエントリーがあります。リリースは GitHub で公開されます。",
          "`npm run build` 把静态站点写入 `dist/`；`Dockerfile` 用 Node 22 构建并用 nginx（`nginx/`）提供。版本记录在 `package.json`、`armor.project.json` 和 README 徽章中（读取自清单）；每个版本在 [CHANGELOG.md](CHANGELOG.md) 中都有对应条目。发布版本发布在 GitHub 上。",
          "`npm run build` escreve o site estático em `dist/`; o `Dockerfile` constrói-o com Node 22 e serve-o com nginx (`nginx/`). A versão está em `package.json`, em `armor.project.json` e no emblema do README (lido do manifesto); cada versão tem a sua entrada em [CHANGELOG.md](CHANGELOG.md). As versões são publicadas no GitHub.")

TROUBLE = [
    (T("Demonstration data and a notice in the top bar | Datos de demostración y un aviso en la barra superior | Demodaten und ein Hinweis in der oberen Leiste | Données de démonstration et un avis dans la barre du haut | Dati dimostrativi e un avviso nella barra superiore | デモデータと上部バーの通知 | 演示数据和顶栏提示 | Dados de demonstração e um aviso na barra superior"), T("the server cannot be reached | no se llega al servidor | der Server ist nicht erreichbar | le serveur est injoignable | il server non è raggiungibile | サーバーに届かない | 无法连接服务器 | não se consegue chegar ao servidor"), T("start ARMOR-SERVER and check the origin you signed in with | arranca ARMOR-SERVER y revisa el origen con el que iniciaste sesión | ARMOR-SERVER starten und den Ursprung der Anmeldung prüfen | démarrez ARMOR-SERVER et vérifiez l'origine de connexion | avvia ARMOR-SERVER e controlla l'origine con cui hai effettuato l'accesso | ARMOR-SERVER を起動し、サインインに使ったオリジンを確認 | 启动 ARMOR-SERVER 并检查登录所用的来源 | inicie o ARMOR-SERVER e verifique a origem com que iniciou sessão")),
    (T("The browser blocks every request to the server | El navegador bloquea cada petición al servidor | Der Browser blockiert jede Anfrage an den Server | Le navigateur bloque toute requête vers le serveur | Il browser blocca ogni richiesta al server | ブラウザーがサーバーへのリクエストをすべて遮断する | 浏览器拦截了所有发往服务器的请求 | O navegador bloqueia todos os pedidos ao servidor"), T("the origin is not in the `connect-src` of the policy | el origen no está en el `connect-src` de la política | der Ursprung steht nicht im `connect-src` der Richtlinie | l'origine n'est pas dans le `connect-src` de la politique | l'origine non è nel `connect-src` della policy | オリジンがポリシーの `connect-src` にない | 来源不在策略的 `connect-src` 中 | a origem não está no `connect-src` da política"), T("add it to `ARMOR_SERVER_ORIGIN` (comma-separated) or serve Studio and the server from the same origin | añádelo a `ARMOR_SERVER_ORIGIN` (separado por comas) o sirve Studio y el servidor desde el mismo origen | in `ARMOR_SERVER_ORIGIN` ergänzen (kommagetrennt) oder Studio und Server vom selben Ursprung ausliefern | ajoutez-la à `ARMOR_SERVER_ORIGIN` (séparées par des virgules) ou servez Studio et le serveur depuis la même origine | aggiungila a `ARMOR_SERVER_ORIGIN` (separata da virgole) o servi Studio e il server dalla stessa origine | `ARMOR_SERVER_ORIGIN` に追加（カンマ区切り）するか、Studio とサーバーを同じオリジンで配信 | 加入 `ARMOR_SERVER_ORIGIN`（逗号分隔），或让 Studio 与服务器使用同一来源 | acrescente-a a `ARMOR_SERVER_ORIGIN` (separada por vírgulas) ou sirva o Studio e o servidor da mesma origem")),
    (T("An order is refused with `elevation_required` (403) | Una orden se rechaza con `elevation_required` (403) | Ein Befehl wird mit `elevation_required` (403) abgelehnt | Un ordre est refusé avec `elevation_required` (403) | Un ordine è rifiutato con `elevation_required` (403) | オーダーが `elevation_required`（403）で拒否される | 指令被 `elevation_required`（403）拒绝 | Uma ordem é recusada com `elevation_required` (403)"), T("a critical action needs a recent proof of identity | una acción crítica pide una prueba de identidad reciente | eine kritische Aktion braucht einen aktuellen Identitätsnachweis | une action critique exige une preuve d'identité récente | un'azione critica richiede una prova d'identità recente | 重要操作には直近の再認証が必要 | 关键操作需要最近的身份验证 | uma ação crítica pede uma prova de identidade recente"), T("Studio asks for the password again; enter it and repeat | Studio pide la contraseña otra vez; escríbela y repite | Studio fragt das Passwort erneut ab; eingeben und wiederholen | Studio redemande le mot de passe ; saisissez-le et recommencez | Studio chiede di nuovo la password; inseriscila e ripeti | Studio がパスワードを再度求めるので入力してやり直す | Studio 会再次要求密码；输入后重试 | o Studio pede a palavra-passe outra vez; introduza-a e repita")),
    (T("The password manager does not offer to save | El gestor de contraseñas no ofrece guardar | Der Passwortmanager bietet das Speichern nicht an | Le gestionnaire de mots de passe ne propose pas d'enregistrer | Il gestore di password non propone di salvare | パスワードマネージャーが保存を提案しない | 密码管理器没有提示保存 | O gestor de palavras-passe não oferece guardar"), T("the sign-in is a real form; some managers wait for the first successful sign-in | el inicio de sesión es un formulario real; algunos gestores esperan al primer inicio correcto | die Anmeldung ist ein echtes Formular; manche Manager warten auf die erste erfolgreiche Anmeldung | la connexion est un vrai formulaire ; certains gestionnaires attendent la première connexion réussie | l'accesso è un vero modulo; alcuni gestori aspettano il primo accesso riuscito | サインインは本物のフォームで、最初の成功まで待つマネージャーもある | 登录是真正的表单；有的管理器要等第一次成功登录 | o início de sessão é um formulário verdadeiro; alguns gestores esperam o primeiro início bem-sucedido"), T("sign in once; \"Remember me\" keeps only the user name, never the password | inicia sesión una vez; \"Recordarme\" solo guarda el usuario, nunca la contraseña | einmal anmelden; \"Angemeldet bleiben\" speichert nur den Benutzernamen, nie das Passwort | connectez-vous une fois ; « Se souvenir de moi » ne garde que le nom, jamais le mot de passe | accedi una volta; \"Ricordami\" conserva solo il nome utente, mai la password | 一度サインインする。「記憶する」はユーザー名のみで、パスワードは保存しない | 登录一次；“记住我”只保存用户名，从不保存密码 | inicie sessão uma vez; \"Lembrar-me\" guarda só o nome de utilizador, nunca a palavra-passe")),
]

ROADMAP = P(
    "**Known limits today**\n\n* Live video and PTZ are not proven against every possible camera.\n* The solar, electrical, alarm-panel and touch-panel menus wait for real nodes: only the radar node exists.\n* There has been no formal accessibility or usability review, and the pictures of the Help are made with example data.\n* No independent security review.\n\n**Next**\n\n* Try the menus of the other nodes with their boards.\n* Review accessibility and usability.",
    "**Límites conocidos hoy**\n\n* El vídeo en vivo y el PTZ no están probados con todas las cámaras posibles.\n* Los menús de solar, eléctrico, panel de alarma y panel táctil esperan nodos reales: solo existe el nodo radar.\n* No ha habido revisión formal de accesibilidad ni de usabilidad, y las imágenes de la Ayuda usan datos de ejemplo.\n* Sin revisión de seguridad independiente.\n\n**Lo siguiente**\n\n* Probar los menús de los demás nodos con sus placas.\n* Revisar accesibilidad y usabilidad.",
    "**Bekannte Grenzen heute**\n\n* Live-Video und PTZ sind nicht mit allen möglichen Kameras erprobt.\n* Die Menüs für Solar, Elektro, Alarmpanel und Touchpanel warten auf echte Knoten: Es gibt nur den Radar-Knoten.\n* Es gab keine formale Prüfung von Barrierefreiheit oder Bedienbarkeit, und die Bilder der Hilfe nutzen Beispieldaten.\n* Keine unabhängige Sicherheitsprüfung.\n\n**Als Nächstes**\n\n* Die Menüs der anderen Knoten mit ihren Platinen ausprobieren.\n* Barrierefreiheit und Bedienbarkeit prüfen.",
    "**Limites connues aujourd'hui**\n\n* La vidéo en direct et le PTZ ne sont pas éprouvés avec toutes les caméras possibles.\n* Les menus solaire, électrique, tableau d'alarme et écran tactile attendent de vrais nœuds : seul le nœud radar existe.\n* Il n'y a pas eu de revue formelle d'accessibilité ni d'ergonomie, et les images de l'Aide utilisent des données d'exemple.\n* Pas de revue de sécurité indépendante.\n\n**Prochainement**\n\n* Essayer les menus des autres nœuds avec leurs cartes.\n* Revoir l'accessibilité et l'ergonomie.",
    "**Limiti noti oggi**\n\n* Il video dal vivo e il PTZ non sono provati con tutte le telecamere possibili.\n* I menu solare, elettrico, pannello allarme e pannello touch attendono nodi reali: esiste solo il nodo radar.\n* Non c'è stata una revisione formale di accessibilità o usabilità, e le immagini della Guida usano dati di esempio.\n* Nessuna revisione di sicurezza indipendente.\n\n**Prossimi passi**\n\n* Provare i menu degli altri nodi con le loro schede.\n* Rivedere accessibilità e usabilità.",
    "**現時点の既知の制限**\n\n* ライブ映像と PTZ は、考えられるすべてのカメラで確認されたわけではありません。\n* ソーラー、電気、アラームパネル、タッチパネルのメニューは実際のノードを待っています。実機があるのはレーダーノードだけです。\n* アクセシビリティとユーザビリティの正式なレビューはなく、ヘルプの画像はサンプルデータで作られています。\n* 第三者によるセキュリティレビューはありません。\n\n**今後**\n\n* 他のノードのメニューを各基板で試す。\n* アクセシビリティとユーザビリティを見直す。",
    "**当前已知限制**\n\n* 实时视频和 PTZ 尚未在所有可能的摄像头上验证。\n* 太阳能、电气、报警面板和触摸面板的菜单在等待真实节点：目前只有雷达节点。\n* 没有做过正式的无障碍或可用性评审，帮助中的图片使用示例数据。\n* 没有独立的安全审查。\n\n**下一步**\n\n* 用其他节点的开发板试用它们的菜单。\n* 评审无障碍与可用性。",
    "**Limites conhecidos hoje**\n\n* O vídeo em direto e o PTZ não estão provados com todas as câmaras possíveis.\n* Os menus solar, elétrico, de painel de alarme e de painel tátil esperam nós reais: só existe o nó de radar.\n* Não houve revisão formal de acessibilidade nem de usabilidade, e as imagens da Ajuda usam dados de exemplo.\n* Sem revisão de segurança independente.\n\n**A seguir**\n\n* Experimentar os menus dos outros nós com as suas placas.\n* Rever acessibilidade e usabilidade.")

DOCS = [
    P("[Security model](docs/SECURITY_MODEL.md): what the browser keeps, the headers and the orders to the nodes", "[Modelo de seguridad](docs/SECURITY_MODEL.md): qué guarda el navegador, las cabeceras y las órdenes a los nodos", "[Sicherheitsmodell](docs/SECURITY_MODEL.md): was der Browser speichert, die Header und die Befehle an die Knoten",
      "[Modèle de sécurité](docs/SECURITY_MODEL.md) : ce que garde le navigateur, les en-têtes et les ordres aux nœuds", "[Modello di sicurezza](docs/SECURITY_MODEL.md): cosa conserva il browser, le intestazioni e gli ordini ai nodi", "[セキュリティモデル](docs/SECURITY_MODEL.md)：ブラウザーが保持するもの、ヘッダー、ノードへのオーダー",
      "[安全模型](docs/SECURITY_MODEL.md)：浏览器保存什么、响应头以及对节点的指令", "[Modelo de segurança](docs/SECURITY_MODEL.md): o que o navegador guarda, os cabeçalhos e as ordens aos nós"),
    P("[Browser tests](e2e/README.md): how to run them against a stack", "[Pruebas de navegador](e2e/README.md): cómo ejecutarlas contra una pila", "[Browser-Tests](e2e/README.md): wie man sie gegen einen Stack ausführt", "[Tests navigateur](e2e/README.md) : comment les lancer contre une pile", "[Test nel browser](e2e/README.md): come eseguirli contro uno stack", "[ブラウザーテスト](e2e/README.md)：スタックに対する実行方法", "[浏览器测试](e2e/README.md)：如何针对整套环境运行", "[Testes de navegador](e2e/README.md): como os executar contra uma pilha"),
]


def build_lg(lg):
    bullets = "\n".join(f"* {b}" for b in L(lg, "bullets"))
    sec_b = sec(lg)
    body = {
        "overview": f"{L(lg, 'intro')}\n\n{bullets}",
        "role": f"{L(lg, 'fit')}\n\n{table(lg, 'talks', ROLE_TABLE)}",
        "architecture": arch(lg, "ARMOR-STUDIO", "ARMOR-STUDIO architecture: the browser, the static host, the console with its menus and designers, ARMOR-SERVER and the weather services", DIAGRAM),
        "security": "\n".join(f"* {b}" for b in [sec_b[0], sec_b[1]]) + "\n\n" + table(lg, "threat", SECURITY_ROWS) + "\n\n" + WEATHER[lg] + "\n\n" + SECURITY_TAIL[lg],
        "interfaces": table(lg, "route", IFACE),
        "configuration": table(lg, "setting", CFG) + "\n\n" + CONFIG_NOTE[lg],
        "quickstart": f"{QUICK_LEAD[lg]}\n\n" + code(lg, QUICK_CODE),
        "testing": code(lg, [("npm run typecheck", "tsc -b --noEmit"), ("npm test", "vitest run"), ("npm run lint", "eslint src"), ("npm run locales:check", T("the eight tables are generated | las ocho tablas están generadas | die acht Tabellen sind erzeugt | les huit tables sont générées | le otto tabelle sono generate | 8 つの表が生成済み | 八张表均已生成 | as oito tabelas estão geradas")), "python -I tools/armor_ci_validate.py"]) + "\n\n" + table(lg, "area", TEST_TABLE) + "\n\n" + TEST_NOTE[lg],
        "build": BUILD[lg],
        "troubleshooting": table(lg, "trouble", TROUBLE),
        "structure": structure(lg, "ARMOR-STUDIO", tree=TREE[lg]),
        "roadmap": ROADMAP[lg],
    }
    return text_for(lg, tagline=L(lg, "tagline"), honest=L(lg, "honest"), glance=GLANCE, status={k: fix(lg, v) for k, v in LEGACY[lg]["status"].items()},
                    docs=DOCS, contributing_first=CONTRIB, body=body)


TEXT = {lg: build_lg(lg) for lg in LGS}
