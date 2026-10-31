# The facts that do not depend on the language, and the words of every language, of ARMOR-COMMON, in the universal README layout.
# Copyright (C) 2026 JuanenRac (Electro Hobby 3D). GPL-3.0-or-later.
from readme_src._kit import *  # noqa: F401,F403

FACTS = {'emoji': '🧾',
 'layout': 'universal',
 'license_badge': 'License-GPL%203.0--or--later-blue',
 'status': [['software', 'green'],
            ['tests', 'green'],
            ['protocols', 'yellow'],
            ['integration', 'yellow'],
            ['hardware', 'orange'],
            ['security', 'yellow'],
            ['docs', 'green']],
 'badges': [['Language', 'Python%203.11%2B', '3776ab'], ['Dependencies', 'none', '2ea44f'], ['Vectors', '1228', '00E5FF']]}

# the sentences of the previous layout that the new one keeps (already written in the eight languages)
LEGACY = {'en': {'tagline': 'Message contracts, validation, the firmware base that the nodes share and the shared project launcher',
        'status': {'software': 'The schemas, the Python validator, the generated TypeScript and Kotlin types, the OpenAPI file of the server and the firmware base '
                               'shared by the five nodes are in place.',
                   'tests': '170 tests and 1228 conformance vectors pass; the JSON, Bluetooth and Improv parsers of the firmware are also fuzzed with libFuzzer.',
                   'protocols': "Only the radar node's messages are used every day with a real board and the server; those of the other nodes are checked against "
                                'stand-ins.',
                   'integration': 'The firmware base is checked to be identical in every node; the Kotlin types are generated but not yet used by the Android app, which '
                                  'keeps its own parsing.',
                   'hardware': 'Only the radar node has run this shared firmware on a board; the other four nodes have not.',
                   'security': 'The firmware signature check and the derivation of the Bluetooth PIN are tested on the host; there has been no independent review.',
                   'docs': 'Eight languages, the OpenAPI file, the conformance guide and the changelog are up to date.'},
        'honest': 'The schemas (telemetry, health, command, node information, solar inverter and battery, electrical, alarm with its command and result, and network), '
                  'the Python validator, the 1228 conformance vectors, the generated TypeScript and Kotlin types, the OpenAPI file of the server (190 paths), the '
                  'firmware base shared by the five nodes and the shared project launcher are real and tested (170 tests). The Kotlin file is generated but **not yet '
                  'consumed** by ARMOR-ANDROID-CONTROL (which keeps its own parsing), and the `set_thresholds` command carries a single `sensitivity` field because the '
                  'real radar parameters are not defined until firmware exists.',
        'bullets': ['**One source of truth:** JSON Schemas in `src/armor_common/schemas/` for telemetry, health, command, node information, the two solar messages '
                    '(inverter, battery with cells and capacities), the electrical messages (readings, command, result), the alarm messages (state, command, result) and '
                    'the network message. Unknown fields and impossible combinations are refused.',
                    '**A validator that cannot skip a rule:** it interprets the schema directly and refuses a schema that uses a keyword it does not implement.',
                    '**Conformance vectors:** 1228 accepted and rejected payloads run by every implementation (Python here, TypeScript in ARMOR-SERVER, the checks of '
                    'the firmware repositories), so drift fails a build.',
                    '**Generated clients:** TypeScript and Kotlin types come from the schemas (`tools/generate_types.py --check` keeps them current).',
                    '**HTTP contract:** `openapi/armor-server.yaml` describes every server route (190 paths, 245 operations), its access rule, and a named schema for '
                    'every request body, answer and error, and a test checks that the routes the server registers are exactly the ones it describes (method and path).',
                    '**Firmware base:** `firmware_base/` keeps each file the five nodes share (network, settings and users, web panel server and login, HTTPS '
                    'certificate, log, Bluetooth with PIN pairing, signed-update check; relays and Zigbee for the nodes that have them) once; '
                    '`tools/sync_firmware_base.py` writes it into every node and checks that no copy drifted ([the guide](docs/FIRMWARE_BASE.md), [signed '
                    'firmware](docs/SIGNED_FIRMWARE.md)).',
                    '**Shared launcher:** `tools/armor_project_tool.py` gives every repository of the family the same `build`, `build-test` and `run` workflow, and '
                    '`tools/armor_ci_validate.py` the same CI checks.',
                    '**Optional TLS link to the broker in the shared node base:** `firmware_base` carries the `mqtt.tls` switch and the `mqtt.ca_pem` text (one PEM '
                    "certificate, at most 2 KB, validated), the connection that trusts that authority only and checks the broker's name, and the host tests shared by "
                    'the five nodes; off by default.',
                    '**Node health and arming profiles:** the `node_health` message (the same report from a radar, a solar, an electrical, an alarm or a wall-panel '
                    'node) and the `arm_profile` (a named way of arming: which zones guard, the delays, the siren and how loudly the server tells people, carried inside '
                    'the arm command) have their schemas, conformance vectors, generated TypeScript and Kotlin types, OpenAPI routes and the shared firmware code that '
                    'builds the report.',
                    "**Connection and system events of the history:** the schemas `connection_event`, `system_event` and `connection_client` (what the server's history "
                    'says about the clients that connect and about the system itself, with a fixed vocabulary and no field where a secret could go), their conformance '
                    'vectors, the generated TypeScript and Kotlin types and the OpenAPI route that lists the clients.',
                    '**Diagnostics and reading quality in the contract:** the dirty-boot report, the core dump, the settings safety check, the diagnostic package, the '
                    'radar events and the read-only diagnostic token messages have their schemas, conformance vectors and generated types; a meter channel may carry the '
                    'age of its reading and its error count, and an inverter message may name the values the node held at a limit.'],
        'intro': '**ARMOR-COMMON** owns what every A.R.M.O.R. message means. Radar nodes, solar gateway nodes and the simulator produce these messages; the server, the '
                 'visual AI and the voice service consume them. If two projects disagree about a field, this repository decides.',
        'note': 'Broker topics: `armor/node/{node_id}/telemetry | health | command | info`, `armor/solar/{node_id}/{device}/state`, `armor/electrical/{node_id}/state | '
                'command | result`, `armor/alarm/{node_id}/state | command | result` and `armor/network/{node_id}/state`. See the [contracts guide](docs/CONTRACTS.md). '
                'The shared launcher creates an ignored `.env` on the first ARMOR-SERVER run with random secrets and a random administrator password; nothing is printed '
                'or committed.',
        'hardware': 'Only the radar node has run on a board: its messages are the ones the CM5 server, Studio and the Android app speak every day; the messages of the '
                    'other nodes are checked against stand-ins',
        'fit': 'ARMOR-COMMON is what keeps the family speaking the same language. Every message between a node and '
               "[ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER) is defined here once, with the vectors that every implementation must pass; the server's HTTP "
               'contract lives here too; and the firmware that the five nodes share ([ARMOR-NODE-RADAR](https://github.com/JuanenRac/ARMOR-NODE-RADAR), '
               '[ARMOR-NODE-SOLAR](https://github.com/JuanenRac/ARMOR-NODE-SOLAR), [ARMOR-NODE-ELECTRICAL](https://github.com/JuanenRac/ARMOR-NODE-ELECTRICAL), '
               '[ARMOR-NODE-ALARM](https://github.com/JuanenRac/ARMOR-NODE-ALARM), [ARMOR-NODE-HMI](https://github.com/JuanenRac/ARMOR-NODE-HMI)) is kept once and '
               'copied into them by a tool. It holds no secret and runs nothing in production.'},
 'es': {'tagline': 'Contratos de mensajes, validación, la base de firmware que comparten los nodos y el lanzador de proyectos compartido',
        'status': {'software': 'Los esquemas, el validador de Python, los tipos generados de TypeScript y Kotlin, el archivo OpenAPI del servidor y la base de firmware '
                               'compartida por los cinco nodos están hechos.',
                   'tests': 'Pasan 170 pruebas y 1228 vectores de conformidad; los analizadores de JSON, Bluetooth e Improv del firmware se prueban además con '
                            'libFuzzer.',
                   'protocols': 'Solo los mensajes del nodo radar se usan a diario con una placa real y el servidor; los de los demás nodos se comprueban contra '
                                'simulaciones.',
                   'integration': 'Se comprueba que la base de firmware sea idéntica en cada nodo; los tipos de Kotlin están generados pero la app de Android aún no los '
                                  'usa, porque conserva su propio análisis.',
                   'hardware': 'Solo el nodo radar ha ejecutado este firmware compartido en una placa; los otros cuatro nodos no.',
                   'security': 'La comprobación de la firma del firmware y la derivación del PIN Bluetooth están probadas en el host; no ha habido una revisión '
                               'independiente.',
                   'docs': 'Ocho idiomas, el archivo OpenAPI, la guía de conformidad y el historial de cambios están al día.'},
        'honest': 'Los esquemas (telemetría, salud, comando, información del nodo, inversor y batería solares, eléctrico, alarma con su comando y resultado, y red), el '
                  'validador de Python, los 1228 vectores de conformidad, los tipos generados de TypeScript y Kotlin, el fichero OpenAPI del servidor (190 rutas), la '
                  'base de firmware compartida por los cinco nodos y el lanzador de proyectos compartido son reales y están probados (170 tests). El fichero de Kotlin '
                  'está generado pero **todavía no lo consume** ARMOR-ANDROID-CONTROL (que conserva su propia lectura), y el comando `set_thresholds` lleva un único '
                  'campo `sensitivity` porque los parámetros reales del radar no se definen hasta que exista el firmware.',
        'bullets': ['**Una única fuente de verdad:** esquemas JSON en `src/armor_common/schemas/` para telemetría, salud, comando, información del nodo, los dos '
                    'mensajes solares (inversor, batería con celdas y capacidades), los mensajes eléctricos (lecturas, comando, resultado), los mensajes de alarma '
                    '(estado, comando, resultado) y el mensaje de red. Se rechazan los campos desconocidos y las combinaciones imposibles.',
                    '**Un validador que no puede saltarse una regla:** interpreta el esquema directamente y rechaza un esquema que use una palabra clave que no '
                    'implementa.',
                    '**Vectores de conformidad:** 1228 cargas aceptadas y rechazadas que ejecuta cada implementación (Python aquí, TypeScript en ARMOR-SERVER, las '
                    'comprobaciones de los repositorios de firmware), de modo que una deriva rompe la compilación.',
                    '**Clientes generados:** los tipos de TypeScript y Kotlin salen de los esquemas (`tools/generate_types.py --check` los mantiene al día).',
                    '**Contrato HTTP:** `openapi/armor-server.yaml` describe cada ruta del servidor (190 rutas, 245 operaciones), su regla de acceso y un esquema con '
                    'nombre para cada cuerpo de petición, respuesta y error, y un test comprueba que las rutas que registra el servidor son exactamente las que describe '
                    '(método y ruta).',
                    '**Base de firmware:** `firmware_base/` guarda una sola vez cada fichero que comparten los cinco nodos (red, ajustes y usuarios, servidor del panel '
                    'web y acceso, certificado HTTPS, registro, Bluetooth con emparejamiento por PIN, comprobación de actualizaciones firmadas; relés y Zigbee en los '
                    'nodos que los tienen); `tools/sync_firmware_base.py` lo escribe en cada nodo y comprueba que ninguna copia se desvíe ([la '
                    'guía](docs/FIRMWARE_BASE.md), [firmware firmado](docs/SIGNED_FIRMWARE.md)).',
                    '**Lanzador compartido:** `tools/armor_project_tool.py` da a cada repositorio de la familia el mismo flujo `build`, `build-test` y `run`, y '
                    '`tools/armor_ci_validate.py` las mismas comprobaciones de CI.',
                    '**Enlace TLS opcional con el broker en la base compartida de los nodos:** `firmware_base` lleva el interruptor `mqtt.tls` y el texto `mqtt.ca_pem` '
                    '(un certificado PEM, 2 KB como máximo, validado), la conexión que confía solo en esa autoridad y comprueba el nombre del broker, y las pruebas en '
                    'ordenador compartidas por los cinco nodos; desactivado por defecto.',
                    '**Salud de los nodos y perfiles de armado:** el mensaje `node_health` (el mismo informe de un nodo de radar, solar, eléctrico, de alarma o de panel '
                    'de pared) y el `arm_profile` (una forma con nombre de armar: qué zonas vigilan, los retardos, la sirena y con qué fuerza avisa el servidor, dentro '
                    'del comando de armar) tienen sus esquemas, vectores de conformidad, tipos generados de TypeScript y Kotlin, rutas OpenAPI y el código de firmware '
                    'compartido que construye el informe.',
                    '**Eventos de conexión y de sistema del historial:** los esquemas `connection_event`, `system_event` y `connection_client` (lo que el historial del '
                    'servidor dice de los clientes que se conectan y del propio sistema, con un vocabulario fijo y sin ningún campo donde pueda ir un secreto), sus '
                    'vectores de conformidad, los tipos TypeScript y Kotlin generados y la ruta de OpenAPI que lista los clientes.',
                    '**Diagnóstico y calidad de lectura en el contrato:** el informe de arranque sucio, el volcado de núcleo, la comprobación de seguridad de los '
                    'ajustes, el paquete de diagnóstico, los eventos del radar y los mensajes del token de diagnóstico de solo lectura tienen sus esquemas, vectores de '
                    'conformidad y tipos generados; un canal de medidor puede llevar la edad de su lectura y su contador de errores, y un mensaje de inversor puede '
                    'nombrar los valores que el nodo mantuvo en un límite.'],
        'intro': '**ARMOR-COMMON** es dueño de lo que significa cada mensaje de A.R.M.O.R. Los nodos de radar, los nodos pasarela solares y el simulador producen estos '
                 'mensajes; el servidor, la IA visual y el servicio de voz los consumen. Si dos proyectos discrepan sobre un campo, decide este repositorio.',
        'note': 'Temas del broker: `armor/node/{node_id}/telemetry | health | command | info`, `armor/solar/{node_id}/{device}/state`, `armor/electrical/{node_id}/state '
                '| command | result`, `armor/alarm/{node_id}/state | command | result` y `armor/network/{node_id}/state`. Véase la [guía de '
                'contratos](docs/CONTRACTS.md). El lanzador compartido crea un `.env` ignorado en la primera ejecución de ARMOR-SERVER con secretos aleatorios y una '
                'contraseña de administrador aleatoria; no se imprime ni se sube nada.',
        'hardware': 'Solo el nodo radar ha funcionado en una placa: sus mensajes son los que hablan cada día el servidor de la CM5, Studio y la app Android; los '
                    'mensajes de los demás nodos se comprueban contra sustitutos',
        'fit': 'ARMOR-COMMON es lo que mantiene a la familia hablando el mismo idioma. Cada mensaje entre un nodo y '
               '[ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER) se define aquí una vez, con los vectores que toda implementación debe pasar; aquí vive también '
               'el contrato HTTP del servidor; y el firmware que comparten los cinco nodos ([ARMOR-NODE-RADAR](https://github.com/JuanenRac/ARMOR-NODE-RADAR), '
               '[ARMOR-NODE-SOLAR](https://github.com/JuanenRac/ARMOR-NODE-SOLAR), [ARMOR-NODE-ELECTRICAL](https://github.com/JuanenRac/ARMOR-NODE-ELECTRICAL), '
               '[ARMOR-NODE-ALARM](https://github.com/JuanenRac/ARMOR-NODE-ALARM), [ARMOR-NODE-HMI](https://github.com/JuanenRac/ARMOR-NODE-HMI)) se guarda una vez y '
               'una herramienta lo copia en ellos. No guarda ningún secreto ni ejecuta nada en producción.',
        'requirements': ['Python 3.11+']},
 'fr': {'tagline': 'Contrats de messages, validation, la base firmware que partagent les nœuds et le lanceur de projet partagé',
        'status': {'software': 'Les schémas, le validateur Python, les types TypeScript et Kotlin générés, le fichier OpenAPI du serveur et la base de firmware partagée '
                               'par les cinq nœuds sont en place.',
                   'tests': '170 tests et 1228 vecteurs de conformité réussissent ; les analyseurs JSON, Bluetooth et Improv du firmware sont aussi soumis à du fuzzing '
                            'avec libFuzzer.',
                   'protocols': 'Seuls les messages du nœud radar sont utilisés chaque jour avec une vraie carte et le serveur ; ceux des autres nœuds sont vérifiés par '
                                'rapport à des simulations.',
                   'integration': "On vérifie que la base de firmware est identique dans chaque nœud ; les types Kotlin sont générés mais l'application Android ne les "
                                  'utilise pas encore, elle garde son propre analyseur.',
                   'hardware': "Seul le nœud radar a exécuté ce firmware partagé sur une carte ; les quatre autres nœuds ne l'ont pas fait.",
                   'security': "La vérification de la signature du firmware et la dérivation du PIN Bluetooth sont testées sur l'hôte ; il n'y a pas eu de revue "
                               'indépendante.',
                   'docs': 'Huit langues, le fichier OpenAPI, le guide de conformité et le journal des modifications sont à jour.'},
        'honest': 'Les schémas (télémétrie, santé, commande, information du nœud, onduleur et batterie solaires, électrique, alarme avec sa commande et son résultat, et '
                  'réseau), le validateur Python, les 1228 vecteurs de conformité, les types TypeScript et Kotlin générés, le fichier OpenAPI du serveur (190 chemins), '
                  'la base firmware partagée par les cinq nœuds et le lanceur de projet partagé sont réels et testés (170 tests). Le fichier Kotlin est généré mais '
                  '**pas encore consommé** par ARMOR-ANDROID-CONTROL (qui garde sa propre lecture), et la commande `set_thresholds` porte un seul champ `sensitivity` '
                  'car les vrais paramètres du radar ne sont définis que lorsque le firmware existe.',
        'bullets': ["**Une seule source de vérité :** schémas JSON dans `src/armor_common/schemas/` pour la télémétrie, la santé, la commande, l'information du nœud, "
                    'les deux messages solaires (onduleur, batterie avec cellules et capacités), les messages électriques (mesures, commande, résultat), les messages '
                    "d'alarme (état, commande, résultat) et le message réseau. Les champs inconnus et les combinaisons impossibles sont refusés.",
                    "**Un validateur qui ne peut sauter aucune règle :** il interprète le schéma directement et refuse un schéma qui utilise un mot-clé qu'il "
                    "n'implémente pas.",
                    '**Vecteurs de conformité :** 1228 charges acceptées et refusées exécutées par chaque implémentation (Python ici, TypeScript dans ARMOR-SERVER, les '
                    "vérifications des dépôts firmware), si bien qu'une dérive fait échouer une compilation.",
                    '**Clients générés :** les types TypeScript et Kotlin viennent des schémas (`tools/generate_types.py --check` les tient à jour).',
                    "**Contrat HTTP :** `openapi/armor-server.yaml` décrit chaque route du serveur (190 chemins, 245 opérations), sa règle d'accès et un schéma nommé "
                    "pour chaque corps de requête, réponse et erreur, et un test vérifie que les routes enregistrées par le serveur sont exactement celles qu'il décrit "
                    '(méthode et chemin).',
                    '**Base firmware :** `firmware_base/` garde une seule fois chaque fichier que partagent les cinq nœuds (réseau, réglages et utilisateurs, serveur du '
                    'panneau web et connexion, certificat HTTPS, journal, Bluetooth avec appairage par PIN, contrôle des mises à jour signées ; relais et Zigbee pour '
                    "les nœuds qui en ont) ; `tools/sync_firmware_base.py` l'écrit dans chaque nœud et vérifie qu'aucune copie n'a dérivé ([le "
                    'guide](docs/FIRMWARE_BASE.md), [firmware signé](docs/SIGNED_FIRMWARE.md)).',
                    '**Lanceur partagé :** `tools/armor_project_tool.py` donne à chaque dépôt de la famille le même flux `build`, `build-test` et `run`, et '
                    '`tools/armor_ci_validate.py` les mêmes contrôles de CI.',
                    "**Liaison TLS facultative avec le broker dans la base commune des nœuds :** `firmware_base` porte l'interrupteur `mqtt.tls` et le texte "
                    "`mqtt.ca_pem` (un certificat PEM, 2 Ko au plus, validé), la connexion qui ne fait confiance qu'à cette autorité et vérifie le nom du broker, et les "
                    'tests sur ordinateur communs aux cinq nœuds ; désactivée par défaut.',
                    "**Santé des nœuds et profils d'armement :** le message `node_health` (le même rapport d'un nœud radar, solaire, électrique, d'alarme ou de panneau "
                    "mural) et le `arm_profile` (une manière nommée d'armer : quelles zones surveillent, les temporisations, la sirène et l'insistance du serveur, dans "
                    "la commande d'armer) ont leurs schémas, vecteurs de conformité, types TypeScript et Kotlin générés, routes OpenAPI et le code de micrologiciel "
                    'partagé qui construit le rapport.',
                    "**Événements de connexion et de système de l'historique :** les schémas `connection_event`, `system_event` et `connection_client` (ce que "
                    "l'historique du serveur dit des clients qui se connectent et du système lui-même, avec un vocabulaire fixe et aucun champ où un secret pourrait "
                    'aller), leurs vecteurs de conformité, les types TypeScript et Kotlin générés et la route OpenAPI qui liste les clients.',
                    '**Diagnostic et qualité des mesures dans le contrat :** le rapport de démarrage non propre, le vidage mémoire, le contrôle de sécurité des '
                    'réglages, le paquet de diagnostic, les événements du radar et les messages du jeton de diagnostic en lecture seule ont leurs schémas, vecteurs de '
                    "conformité et types générés ; un canal de compteur peut porter l'âge de sa mesure et son compteur d'erreurs, et un message d'onduleur peut nommer "
                    'les valeurs que le nœud a retenues à une limite.'],
        'intro': "**ARMOR-COMMON** possède le sens de chaque message d'A.R.M.O.R. Les nœuds radar, les nœuds passerelles solaires et le simulateur produisent ces "
                 "messages ; le serveur, l'IA visuelle et le service vocal les consomment. Si deux projets divergent sur un champ, ce dépôt tranche.",
        'note': 'Sujets du broker : `armor/node/{node_id}/telemetry | health | command | info`, `armor/solar/{node_id}/{device}/state`, '
                '`armor/electrical/{node_id}/state | command | result`, `armor/alarm/{node_id}/state | command | result` et `armor/network/{node_id}/state`. Voir le '
                "[guide des contrats](docs/CONTRACTS.md). Le lanceur partagé crée un `.env` ignoré au premier lancement d'ARMOR-SERVER avec des secrets aléatoires et un "
                "mot de passe administrateur aléatoire ; rien n'est affiché ni versionné.",
        'hardware': "Seul le nœud radar a tourné sur une carte : ses messages sont ceux que parlent chaque jour le serveur CM5, Studio et l'application Android ; les "
                    'messages des autres nœuds sont vérifiés contre des substituts',
        'fit': 'ARMOR-COMMON est ce qui garde la famille dans la même langue. Chaque message entre un nœud et [ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER) '
               'est défini ici une fois, avec les vecteurs que toute implémentation doit passer ; le contrat HTTP du serveur vit aussi ici ; et le firmware que '
               'partagent les cinq nœuds ([ARMOR-NODE-RADAR](https://github.com/JuanenRac/ARMOR-NODE-RADAR), '
               '[ARMOR-NODE-SOLAR](https://github.com/JuanenRac/ARMOR-NODE-SOLAR), [ARMOR-NODE-ELECTRICAL](https://github.com/JuanenRac/ARMOR-NODE-ELECTRICAL), '
               '[ARMOR-NODE-ALARM](https://github.com/JuanenRac/ARMOR-NODE-ALARM), [ARMOR-NODE-HMI](https://github.com/JuanenRac/ARMOR-NODE-HMI)) est gardé une fois et '
               "copié en eux par un outil. Il ne contient aucun secret et n'exécute rien en production.",
        'requirements': ['Python 3.11+']},
 'it': {'tagline': 'Contratti dei messaggi, validazione, la base firmware condivisa dai nodi e il lanciatore di progetto condiviso',
        'status': {'software': 'Gli schemi, il validatore Python, i tipi TypeScript e Kotlin generati, il file OpenAPI del server e la base firmware condivisa dai '
                               'cinque nodi sono pronti.',
                   'tests': 'Superano 170 test e 1228 vettori di conformità; i parser JSON, Bluetooth e Improv del firmware sono sottoposti anche a fuzzing con '
                            'libFuzzer.',
                   'protocols': 'Solo i messaggi del nodo radar sono usati ogni giorno con una scheda reale e il server; quelli degli altri nodi sono verificati contro '
                                'simulazioni.',
                   'integration': "Si verifica che la base firmware sia identica in ogni nodo; i tipi Kotlin sono generati ma l'app Android non li usa ancora, perché "
                                  'mantiene il proprio parsing.',
                   'hardware': 'Solo il nodo radar ha eseguito questo firmware condiviso su una scheda; gli altri quattro nodi no.',
                   'security': "Il controllo della firma del firmware e la derivazione del PIN Bluetooth sono testati sull'host; non c'è stata una revisione "
                               'indipendente.',
                   'docs': 'Otto lingue, il file OpenAPI, la guida di conformità e il registro delle modifiche sono aggiornati.'},
        'honest': 'Gli schemi (telemetria, salute, comando, informazioni del nodo, inverter e batteria solari, elettrico, allarme con il suo comando e risultato, e '
                  'rete), il validatore Python, i 1228 vettori di conformità, i tipi TypeScript e Kotlin generati, il file OpenAPI del server (190 percorsi), la base '
                  'firmware condivisa dai cinque nodi e il lanciatore di progetto condiviso sono reali e provati (170 test). Il file Kotlin è generato ma **non ancora '
                  'consumato** da ARMOR-ANDROID-CONTROL (che mantiene una propria lettura), e il comando `set_thresholds` porta un solo campo `sensitivity` perché i '
                  'veri parametri del radar non sono definiti finché non esiste il firmware.',
        'bullets': ["**Un'unica fonte di verità:** schemi JSON in `src/armor_common/schemas/` per telemetria, salute, comando, informazioni del nodo, i due messaggi "
                    'solari (inverter, batteria con celle e capacità), i messaggi elettrici (letture, comando, risultato), i messaggi di allarme (stato, comando, '
                    'risultato) e il messaggio di rete. I campi sconosciuti e le combinazioni impossibili sono rifiutati.',
                    '**Un validatore che non può saltare una regola:** interpreta direttamente lo schema e rifiuta uno schema che usa una parola chiave che non '
                    'implementa.',
                    '**Vettori di conformità:** 1228 carichi accettati e rifiutati eseguiti da ogni implementazione (Python qui, TypeScript in ARMOR-SERVER, i controlli '
                    'dei repository firmware), così una deriva fa fallire una compilazione.',
                    '**Client generati:** i tipi TypeScript e Kotlin vengono dagli schemi (`tools/generate_types.py --check` li mantiene aggiornati).',
                    '**Contratto HTTP:** `openapi/armor-server.yaml` descrive ogni rotta del server (190 percorsi, 245 operazioni), la sua regola di accesso e uno '
                    'schema con nome per ogni corpo di richiesta, risposta ed errore, e un test verifica che le rotte registrate dal server siano esattamente quelle che '
                    'descrive (metodo e percorso).',
                    '**Base firmware:** `firmware_base/` tiene una sola volta ogni file condiviso dai cinque nodi (rete, impostazioni e utenti, server del pannello web '
                    'e accesso, certificato HTTPS, registro, Bluetooth con abbinamento a PIN, controllo degli aggiornamenti firmati; relè e Zigbee per i nodi che li '
                    'hanno); `tools/sync_firmware_base.py` lo scrive in ogni nodo e controlla che nessuna copia sia derivata ([la guida](docs/FIRMWARE_BASE.md), '
                    '[firmware firmato](docs/SIGNED_FIRMWARE.md)).',
                    '**Lanciatore condiviso:** `tools/armor_project_tool.py` dà a ogni repository della famiglia lo stesso flusso `build`, `build-test` e `run`, e '
                    '`tools/armor_ci_validate.py` gli stessi controlli di CI.',
                    "**Collegamento TLS facoltativo con il broker nella base comune dei nodi:** `firmware_base` porta l'interruttore `mqtt.tls` e il testo `mqtt.ca_pem` "
                    "(un certificato PEM, al massimo 2 KB, validato), la connessione che si fida solo di quell'autorità e verifica il nome del broker, e i test sul "
                    'computer condivisi dai cinque nodi; disattivato per impostazione predefinita.',
                    '**Salute dei nodi e profili di inserimento:** il messaggio `node_health` (lo stesso rapporto da un nodo radar, solare, elettrico, di allarme o a '
                    "pannello da parete) e l'`arm_profile` (un modo con nome di inserire: quali zone sorvegliano, i ritardi, la sirena e con quanta insistenza il server "
                    'avvisa, dentro il comando di inserimento) hanno schemi, vettori di conformità, tipi TypeScript e Kotlin generati, rotte OpenAPI e il codice '
                    'firmware condiviso che costruisce il rapporto.',
                    '**Eventi di connessione e di sistema della cronologia:** gli schemi `connection_event`, `system_event` e `connection_client` (ciò che la cronologia '
                    'del server dice dei client che si collegano e del sistema stesso, con un vocabolario fisso e nessun campo dove possa andare un segreto), i loro '
                    'vettori di conformità, i tipi TypeScript e Kotlin generati e la rotta OpenAPI che elenca i client.',
                    '**Diagnostica e qualità delle letture nel contratto:** il rapporto di avvio non pulito, il core dump, il controllo di sicurezza delle impostazioni, '
                    'il pacchetto di diagnostica, gli eventi del radar e i messaggi del token di diagnostica in sola lettura hanno i loro schemi, vettori di conformità '
                    "e tipi generati; un canale del contatore può portare l'età della sua lettura e il suo contatore di errori, e un messaggio dell'inverter può "
                    'nominare i valori che il nodo ha trattenuto a un limite.'],
        'intro': '**ARMOR-COMMON** possiede il significato di ogni messaggio di A.R.M.O.R. I nodi radar, i nodi gateway solari e il simulatore producono questi '
                 "messaggi; il server, l'IA visiva e il servizio vocale li consumano. Se due progetti non concordano su un campo, decide questo repository.",
        'note': 'Topic del broker: `armor/node/{node_id}/telemetry | health | command | info`, `armor/solar/{node_id}/{device}/state`, `armor/electrical/{node_id}/state '
                '| command | result`, `armor/alarm/{node_id}/state | command | result` e `armor/network/{node_id}/state`. Vedi la [guida ai '
                'contratti](docs/CONTRACTS.md). Il lanciatore condiviso crea un `.env` ignorato al primo avvio di ARMOR-SERVER con segreti casuali e una password di '
                'amministratore casuale; nulla è stampato né committato.',
        'hardware': "Solo il nodo radar ha girato su una scheda: i suoi messaggi sono quelli che parlano ogni giorno il server CM5, Studio e l'app Android; i messaggi "
                    'degli altri nodi sono controllati contro sostituti',
        'fit': 'ARMOR-COMMON è ciò che tiene la famiglia nella stessa lingua. Ogni messaggio fra un nodo e [ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER) è '
               'definito qui una volta, con i vettori che ogni implementazione deve superare; qui vive anche il contratto HTTP del server; e il firmware che i cinque '
               'nodi condividono ([ARMOR-NODE-RADAR](https://github.com/JuanenRac/ARMOR-NODE-RADAR), [ARMOR-NODE-SOLAR](https://github.com/JuanenRac/ARMOR-NODE-SOLAR), '
               '[ARMOR-NODE-ELECTRICAL](https://github.com/JuanenRac/ARMOR-NODE-ELECTRICAL), [ARMOR-NODE-ALARM](https://github.com/JuanenRac/ARMOR-NODE-ALARM), '
               '[ARMOR-NODE-HMI](https://github.com/JuanenRac/ARMOR-NODE-HMI)) è tenuto una volta e copiato in essi da uno strumento. Non contiene alcun segreto e non '
               'esegue nulla in produzione.',
        'requirements': ['Python 3.11+']},
 'de': {'tagline': 'Nachrichtenverträge, Validierung, die von den Knoten geteilte Firmware-Basis und der gemeinsame Projektstarter',
        'status': {'software': 'Die Schemas, der Python-Validator, die erzeugten TypeScript- und Kotlin-Typen, die OpenAPI-Datei des Servers und die von den fünf Knoten '
                               'gemeinsam genutzte Firmware-Basis sind vorhanden.',
                   'tests': '170 Tests und 1228 Konformitätsvektoren bestehen; die JSON-, Bluetooth- und Improv-Parser der Firmware werden außerdem mit libFuzzer '
                            'gefuzzt.',
                   'protocols': 'Nur die Nachrichten des Radar-Knotens werden täglich mit einer echten Platine und dem Server genutzt; die der anderen Knoten werden '
                                'gegen Nachbildungen geprüft.',
                   'integration': 'Es wird geprüft, dass die Firmware-Basis in jedem Knoten identisch ist; die Kotlin-Typen sind erzeugt, werden von der Android-App '
                                  'aber noch nicht genutzt, sie behält ihr eigenes Parsing.',
                   'hardware': 'Nur der Radar-Knoten hat diese gemeinsame Firmware auf einer Platine ausgeführt; die anderen vier Knoten nicht.',
                   'security': 'Die Prüfung der Firmware-Signatur und die Ableitung der Bluetooth-PIN sind auf dem Host getestet; es gab keine unabhängige Prüfung.',
                   'docs': 'Acht Sprachen, die OpenAPI-Datei, der Konformitätsleitfaden und das Änderungsprotokoll sind aktuell.'},
        'honest': 'Die Schemas (Telemetrie, Zustand, Befehl, Knoteninformation, Solar-Wechselrichter und -Batterie, Elektro, Alarm mit Befehl und Ergebnis sowie '
                  'Netzwerk), der Python-Validator, die 1228 Konformitätsvektoren, die erzeugten TypeScript- und Kotlin-Typen, die OpenAPI-Datei des Servers (190 '
                  'Pfade), die von den fünf Knoten geteilte Firmware-Basis und der gemeinsame Projektstarter sind real und getestet (170 Tests). Die Kotlin-Datei wird '
                  'erzeugt, aber **noch nicht verwendet** von ARMOR-ANDROID-CONTROL (das sein eigenes Parsen behält), und der Befehl `set_thresholds` trägt nur ein Feld '
                  '`sensitivity`, weil die echten Radarparameter erst definiert sind, wenn Firmware existiert.',
        'bullets': ['**Eine einzige Quelle der Wahrheit:** JSON-Schemas in `src/armor_common/schemas/` für Telemetrie, Zustand, Befehl, Knoteninformation, die beiden '
                    'Solar-Nachrichten (Wechselrichter, Batterie mit Zellen und Kapazitäten), die Elektro-Nachrichten (Messwerte, Befehl, Ergebnis), die '
                    'Alarmnachrichten (Zustand, Befehl, Ergebnis) und die Netzwerknachricht. Unbekannte Felder und unmögliche Kombinationen werden abgelehnt.',
                    '**Ein Validator, der keine Regel überspringen kann:** er interpretiert das Schema direkt und lehnt ein Schema ab, das ein nicht implementiertes '
                    'Schlüsselwort verwendet.',
                    '**Konformitätsvektoren:** 1228 akzeptierte und abgelehnte Nutzlasten, von jeder Implementierung ausgeführt (hier Python, TypeScript in '
                    'ARMOR-SERVER, die Prüfungen der Firmware-Repositories), sodass eine Abweichung einen Build scheitern lässt.',
                    '**Erzeugte Clients:** TypeScript- und Kotlin-Typen entstehen aus den Schemas (`tools/generate_types.py --check` hält sie aktuell).',
                    '**HTTP-Vertrag:** `openapi/armor-server.yaml` beschreibt jede Route des Servers (190 Pfade, 245 Operationen), ihre Zugriffsregel und ein benanntes '
                    'Schema für jeden Anfragekörper, jede Antwort und jeden Fehler, und ein Test prüft, dass die vom Server registrierten Routen genau die beschriebenen '
                    'sind (Methode und Pfad).',
                    '**Firmware-Basis:** `firmware_base/` hält jede von den fünf Knoten geteilte Datei einmal (Netzwerk, Einstellungen und Benutzer, Panel-Server und '
                    'Login, HTTPS-Zertifikat, Log, Bluetooth mit PIN-Kopplung, Prüfung signierter Updates; Relais und Zigbee in den Knoten, die sie haben); '
                    '`tools/sync_firmware_base.py` schreibt sie in jeden Knoten und prüft, dass keine Kopie abweicht ([die Anleitung](docs/FIRMWARE_BASE.md), [signierte '
                    'Firmware](docs/SIGNED_FIRMWARE.md)).',
                    '**Gemeinsamer Starter:** `tools/armor_project_tool.py` gibt jedem Repository der Familie denselben Ablauf `build`, `build-test` und `run`, und '
                    '`tools/armor_ci_validate.py` dieselben CI-Prüfungen.',
                    '**Optionale TLS-Verbindung zum Broker in der gemeinsamen Knotenbasis:** `firmware_base` enthält den Schalter `mqtt.tls` und den Text `mqtt.ca_pem` '
                    '(ein PEM-Zertifikat, höchstens 2 KB, geprüft), die Verbindung, die nur dieser Stelle vertraut und den Namen des Brokers prüft, und die Host-Tests, '
                    'die sich die fünf Knoten teilen; standardmäßig aus.',
                    '**Zustand der Knoten und Scharfschaltprofile:** Die Nachricht `node_health` (derselbe Bericht von einem Radar-, Solar-, Elektro-, Alarm- oder '
                    'Wandpanel-Knoten) und das `arm_profile` (eine benannte Art des Scharfschaltens: welche Zonen überwachen, die Verzögerungen, die Sirene und wie '
                    'nachdrücklich der Server informiert, im Scharfschaltbefehl) haben ihre Schemas, Konformitätsvektoren, erzeugte TypeScript- und Kotlin-Typen, '
                    'OpenAPI-Routen und den gemeinsamen Firmware-Code, der den Bericht baut.',
                    '**Verbindungs- und Systemereignisse des Verlaufs:** die Schemas `connection_event`, `system_event` und `connection_client` (was der Verlauf des '
                    'Servers über die sich verbindenden Clients und über das System selbst sagt, mit festem Vokabular und ohne Feld, in dem ein Geheimnis stehen '
                    'könnte), ihre Konformitätsvektoren, die erzeugten TypeScript- und Kotlin-Typen und die OpenAPI-Route, die die Clients auflistet.',
                    '**Diagnose und Messqualität im Vertrag:** Der Bericht über unsaubere Starts, das Core-Dump, die Sicherheitsprüfung der Einstellungen, das '
                    'Diagnosepaket, die Radar-Ereignisse und die Nachrichten des schreibgeschützten Diagnose-Tokens haben ihre Schemas, Konformitätsvektoren und '
                    'generierten Typen; ein Zählerkanal kann das Alter seiner Messung und seinen Fehlerzähler tragen, und eine Wechselrichter-Nachricht kann die Werte '
                    'nennen, die der Knoten an einer Grenze festgehalten hat.'],
        'intro': '**ARMOR-COMMON** besitzt die Bedeutung jeder A.R.M.O.R.-Nachricht. Radarknoten, Solar-Gateway-Knoten und der Simulator erzeugen diese Nachrichten; der '
                 'Server, die visuelle KI und der Sprachdienst verbrauchen sie. Wenn zwei Projekte über ein Feld uneins sind, entscheidet dieses Repository.',
        'note': 'Broker-Themen: `armor/node/{node_id}/telemetry | health | command | info`, `armor/solar/{node_id}/{device}/state`, `armor/electrical/{node_id}/state | '
                'command | result`, `armor/alarm/{node_id}/state | command | result` und `armor/network/{node_id}/state`. Siehe den '
                '[Vertragsleitfaden](docs/CONTRACTS.md). Der gemeinsame Starter legt beim ersten Start von ARMOR-SERVER eine ignorierte `.env` mit zufälligen '
                'Geheimnissen und einem zufälligen Administratorpasswort an; nichts wird ausgegeben oder eingecheckt.',
        'hardware': 'Nur der Radarknoten hat auf einer Platine gelaufen: Seine Nachrichten sind die, die der CM5-Server, Studio und die Android-App täglich sprechen; '
                    'die Nachrichten der anderen Knoten werden gegen Ersatz geprüft',
        'fit': 'ARMOR-COMMON sorgt dafür, dass die Familie dieselbe Sprache spricht. Jede Nachricht zwischen einem Knoten und '
               '[ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER) ist hier einmal definiert, mit den Vektoren, die jede Implementierung bestehen muss; hier lebt '
               'auch der HTTP-Vertrag des Servers; und die Firmware, die die fünf Knoten teilen ([ARMOR-NODE-RADAR](https://github.com/JuanenRac/ARMOR-NODE-RADAR), '
               '[ARMOR-NODE-SOLAR](https://github.com/JuanenRac/ARMOR-NODE-SOLAR), [ARMOR-NODE-ELECTRICAL](https://github.com/JuanenRac/ARMOR-NODE-ELECTRICAL), '
               '[ARMOR-NODE-ALARM](https://github.com/JuanenRac/ARMOR-NODE-ALARM), [ARMOR-NODE-HMI](https://github.com/JuanenRac/ARMOR-NODE-HMI)), wird einmal gehalten '
               'und von einem Werkzeug in sie kopiert. Es enthält kein Geheimnis und führt nichts in Produktion aus.',
        'requirements': ['Python 3.11+']},
 'zh': {'tagline': '消息契约、验证、各节点共用的固件基础和共享的项目启动器',
        'status': {'software': '模式、Python 验证器、生成的 TypeScript 和 Kotlin 类型、服务器的 OpenAPI 文件以及五个节点共用的固件基础均已就绪。',
                   'tests': '170 项测试和 1228 个一致性向量通过；固件的 JSON、蓝牙和 Improv 解析器还用 libFuzzer 做了模糊测试。',
                   'protocols': '只有雷达节点的消息每天在真实板子和服务器上使用；其他节点的消息是对照模拟检查的。',
                   'integration': '会检查固件基础在每个节点中完全相同；Kotlin 类型已生成，但 Android 应用尚未使用，它仍保留自己的解析。',
                   'hardware': '只有雷达节点在板子上运行过这套共用固件；其他四个节点没有。',
                   'security': '固件签名检查和蓝牙 PIN 的推导已在主机上测试；没有经过独立审查。',
                   'docs': '八种语言、OpenAPI 文件、一致性指南和更新日志均为最新。'},
        'honest': '各模式（遥测、健康、命令、节点信息、太阳能逆变器和电池、电气、带命令和结果的报警、网络）、Python 验证器、1228 个一致性向量、生成的 TypeScript 和 Kotlin 类型、服务器的 OpenAPI 文件（190 '
                  '个路径）、五个节点共用的固件基础以及共享的项目启动器都是真实的并经过测试（170 个测试）。Kotlin 文件已生成，但 ARMOR-ANDROID-CONTROL **尚未使用**（它保留自己的解析），`set_thresholds` 命令只带一个 `sensitivity` '
                  '字段，因为真实的雷达参数要等固件存在才能确定。',
        'bullets': ['**唯一的事实来源：**`src/armor_common/schemas/` 中的 JSON Schema，涵盖遥测、健康、命令、节点信息、两种太阳能消息（逆变器、含电芯和容量的电池）、电气消息（读数、命令、结果）、报警消息（状态、命令、结果）和网络消息。未知字段和不可能的组合会被拒绝。',
                    '**无法跳过规则的验证器：**它直接解释模式，并拒绝使用了它未实现的关键字的模式。',
                    '**一致性向量：**1228 个被接受和被拒绝的负载，由每个实现运行（这里是 Python，ARMOR-SERVER 中是 TypeScript，以及固件仓库的检查），因此偏差会让构建失败。',
                    '**生成的客户端：**TypeScript 和 Kotlin 类型来自模式（`tools/generate_types.py --check` 保持其最新）。',
                    '**HTTP 契约：**`openapi/armor-server.yaml` 描述服务器的每条路由（190 个路径、245 个操作）、其访问规则，以及每个请求体、响应和错误的具名模式；测试会检查服务器注册的路由与其描述的路由完全一致（方法和路径）。',
                    '**固件基础：**`firmware_base/` 把五个节点共用的每个文件只保存一次（网络、设置和用户、网页面板服务器和登录、HTTPS 证书、日志、带 PIN 配对的蓝牙、签名更新检查；继电器和 Zigbee 仅限具备它们的节点）；`tools/sync_firmware_base.py` '
                    '把它写入每个节点并检查没有副本偏离（[指南](docs/FIRMWARE_BASE.md)，[签名固件](docs/SIGNED_FIRMWARE.md)）。',
                    '**共享启动器：**`tools/armor_project_tool.py` 为家族的每个仓库提供相同的 `build`、`build-test` 和 `run` 流程，`tools/armor_ci_validate.py` 提供相同的 CI 检查。',
                    '**共享节点基础中可选的与代理的 TLS 连接:** `firmware_base` 包含 `mqtt.tls` 开关和 `mqtt.ca_pem` 文本(一个 PEM 证书,最大 2 KB,经过校验)、只信任该机构并检查代理名称的连接,以及五个节点共用的主机测试;默认关闭。',
                    '**节点健康与布防配置：** `node_health` 消息（雷达、太阳能、电气、报警或壁挂面板节点发送相同的报告）和 `arm_profile`（布防命令中带有的命名布防方式：哪些分区守护、延时、警笛以及服务器通知的力度）都有自己的模式、一致性向量、生成的 TypeScript 与 '
                    'Kotlin 类型、OpenAPI 路由，以及生成报告的共享固件代码。',
                    '**历史中的连接事件与系统事件：** 模式 `connection_event`、`system_event` 和 `connection_client`（服务器历史对连接的客户端和系统本身的描述，词汇固定，没有可以放入机密的字段）、其一致性向量、生成的 TypeScript 与 Kotlin '
                    '类型，以及列出客户端的 OpenAPI 路由。',
                    '**合同中的诊断与读数质量：** 不干净启动报告、核心转储、设置安全检查、诊断包、雷达事件和只读诊断令牌消息都有各自的模式、一致性向量和生成的类型；电表通道可以携带其读数的时间和错误计数，逆变器消息可以点名节点限制在上限的数值。'],
        'intro': '**ARMOR-COMMON** 掌管每条 A.R.M.O.R. 消息的含义。雷达节点、太阳能网关节点和模拟器产生这些消息；服务器、视觉 AI 和语音服务消费它们。如果两个项目对某个字段有分歧，由本仓库裁决。',
        'note': '代理主题：`armor/node/{node_id}/telemetry | health | command | info`、`armor/solar/{node_id}/{device}/state`、`armor/electrical/{node_id}/state | command | '
                'result`、`armor/alarm/{node_id}/state | command | result` 和 `armor/network/{node_id}/state`。参见[契约指南](docs/CONTRACTS.md)。共享启动器在 ARMOR-SERVER 首次运行时创建被忽略的 '
                '`.env`，其中有随机密钥和随机管理员密码；不会打印或提交任何内容。',
        'hardware': '只有雷达节点在电路板上运行过：它的消息就是 CM5 服务器、Studio 和 Android 应用每天使用的消息；其他节点的消息对照替身检查',
        'fit': 'ARMOR-COMMON 让整个家族说同一种语言。节点与 [ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER) 之间的每条消息都在这里只定义一次，并带有每个实现都必须通过的向量；服务器的 HTTP '
               '契约也在这里；五个节点共用的固件（[ARMOR-NODE-RADAR](https://github.com/JuanenRac/ARMOR-NODE-RADAR)、[ARMOR-NODE-SOLAR](https://github.com/JuanenRac/ARMOR-NODE-SOLAR)、[ARMOR-NODE-ELECTRICAL](https://github.com/JuanenRac/ARMOR-NODE-ELECTRICAL)、[ARMOR-NODE-ALARM](https://github.com/JuanenRac/ARMOR-NODE-ALARM)、[ARMOR-NODE-HMI](https://github.com/JuanenRac/ARMOR-NODE-HMI)）只保存一份，由工具复制进去。它不保存任何密钥，也不在生产中运行任何东西。',
        'requirements': ['Python 3.11+']},
 'ja': {'tagline': 'メッセージのコントラクト、検証、ノードが共有するファームウェア基盤、共通のプロジェクトランチャー',
        'status': {'software': 'スキーマ、Python の検証ツール、生成された TypeScript と Kotlin の型、サーバーの OpenAPI ファイル、5 つのノードが共有するファームウェアの基盤が揃っています。',
                   'tests': '170 件のテストと 1228 件の適合ベクターが通ります。ファームウェアの JSON、Bluetooth、Improv のパーサーは libFuzzer でファジングも行っています。',
                   'protocols': '毎日、実機のボードとサーバーで使われているのはレーダーノードのメッセージだけです。他のノードのメッセージは模擬に対して検証しています。',
                   'integration': 'ファームウェアの基盤が全ノードで同一であることを確認しています。Kotlin の型は生成済みですが、Android アプリは独自の解析を使っていて、まだ使っていません。',
                   'hardware': 'この共有ファームウェアをボード上で動かしたのはレーダーノードだけで、他の 4 つのノードはまだです。',
                   'security': 'ファームウェア署名の確認と Bluetooth の PIN の導出はホストでテスト済みです。独立したレビューはまだありません。',
                   'docs': '8 言語、OpenAPI ファイル、適合ガイド、変更履歴は最新です。'},
        'honest': 'スキーマ（テレメトリ、状態、コマンド、ノード情報、ソーラーのインバーターとバッテリー、電気、コマンドと結果を含む警報、ネットワーク）、Python の検証器、1228 個の適合ベクトル、生成された TypeScript と Kotlin の型、サーバーの OpenAPI ファイル（190 '
                  'パス）、5 つのノードが共有するファームウェア基盤、共通のプロジェクトランチャーは実在し、テストされています（170 件）。Kotlin ファイルは生成されますが ARMOR-ANDROID-CONTROL では**まだ使われていません**（独自の解析を保持）。`set_thresholds` '
                  'コマンドは `sensitivity` フィールド 1 つだけを持ちます。実際のレーダーパラメーターはファームウェアができるまで定義できないためです。',
        'bullets': ['**唯一の信頼できる情報源：**`src/armor_common/schemas/` の JSON Schema。テレメトリ、状態、コマンド、ノード情報、2 '
                    'つのソーラーメッセージ（インバーター、セルと容量を含むバッテリー）、電気メッセージ（測定値、コマンド、結果）、警報メッセージ（状態、コマンド、結果）、ネットワークメッセージ。未知のフィールドや不可能な組み合わせは拒否されます。',
                    '**ルールを飛ばせない検証器：**スキーマを直接解釈し、実装していないキーワードを使うスキーマを拒否します。',
                    '**適合ベクトル：**受理と拒否の 1228 個のペイロードをすべての実装（ここでは Python、ARMOR-SERVER では TypeScript、ファームウェアリポジトリの検査）が実行するため、ずれがあればビルドが失敗します。',
                    '**生成されるクライアント：**TypeScript と Kotlin の型はスキーマから作られます（`tools/generate_types.py --check` で最新に保ちます）。',
                    '**HTTP コントラクト：**`openapi/armor-server.yaml` はサーバーのすべてのルート（190 パス、245 '
                    '操作）、そのアクセスルール、そして各リクエスト本文・応答・エラーの名前付きスキーマを記述し、サーバーが登録するルートが記述と完全に一致すること（メソッドとパス）をテストが確認します。',
                    '**ファームウェア基盤：**`firmware_base/` は 5 つのノードが共有する各ファイル（ネットワーク、設定とユーザー、Web パネルのサーバーとログイン、HTTPS 証明書、ログ、PIN ペアリング付き Bluetooth、署名付きアップデートの検査、リレーと Zigbee '
                    'は備えるノードのみ）を 1 か所に保持し、`tools/sync_firmware_base.py` が各ノードに書き込んでコピーのずれがないか検査します（[ガイド](docs/FIRMWARE_BASE.md)、[署名付きファームウェア](docs/SIGNED_FIRMWARE.md)）。',
                    '**共通ランチャー：**`tools/armor_project_tool.py` はファミリーの全リポジトリに同じ `build`、`build-test`、`run` の流れを、`tools/armor_ci_validate.py` に同じ CI 検査を提供します。',
                    '**共有ノードベースの任意の TLS ブローカー接続:** `firmware_base` は `mqtt.tls` スイッチと `mqtt.ca_pem` テキスト(PEM 証明書 1 つ、最大 2 KB、検証済み)、その認証局だけを信頼してブローカーの名前を確認する接続、5 '
                    'つのノードで共有するホストテストを含みます。初期状態ではオフです。',
                    '**ノードの状態と警戒プロファイル:** `node_health` メッセージ（レーダー、太陽光、電気、警報、壁パネルのどのノードも同じ報告）と '
                    '`arm_profile`（警戒コマンドに入る名前付きの警戒方法：警戒するゾーン、遅延、サイレン、サーバーの通知の強さ）に、スキーマ、適合ベクター、生成された TypeScript と Kotlin の型、OpenAPI のルート、報告を作る共有ファームウェアコードがあります。',
                    '**履歴の接続イベントとシステムイベント:** スキーマ '
                    '`connection_event`・`system_event`・`connection_client`（接続するクライアントとシステム自体について、サーバーの履歴が何を伝えるか。語彙は固定で、秘密が入る欄はありません）、その適合ベクトル、生成された TypeScript と Kotlin '
                    'の型、クライアントを一覧する OpenAPI のルート。',
                    '**契約に含まれる診断と測定品質：** '
                    '正常でない起動のレポート、コアダンプ、設定の安全チェック、診断パッケージ、レーダーイベント、読み取り専用診断トークンのメッセージに、それぞれスキーマ、適合ベクトル、生成された型があります。メーターチャンネルは測定値の経過時間とエラー数を持て、インバーターのメッセージはノードが上限に留めた値を名指しできます。'],
        'intro': '**ARMOR-COMMON** は A.R.M.O.R. のすべてのメッセージの意味を所有します。レーダーノード、太陽光ゲートウェイノード、シミュレーターがこれらのメッセージを作り、サーバー、視覚 AI、音声サービスが使います。2 '
                 'つのプロジェクトがフィールドについて食い違ったら、このリポジトリが決めます。',
        'note': 'ブローカーのトピック：`armor/node/{node_id}/telemetry | health | command | info`、`armor/solar/{node_id}/{device}/state`、`armor/electrical/{node_id}/state | '
                'command | result`、`armor/alarm/{node_id}/state | command | result`、`armor/network/{node_id}/state`。[コントラクトガイド](docs/CONTRACTS.md)を参照してください。共通ランチャーは '
                'ARMOR-SERVER の初回実行時に、ランダムな秘密とランダムな管理者パスワードを持つ無視対象の `.env` を作成し、何も表示もコミットもしません。',
        'hardware': '基板上で動いたのはレーダーノードだけです。そのメッセージは CM5 サーバー、Studio、Android アプリが毎日話しているもので、他のノードのメッセージは代替に対して検査されます',
        'fit': 'ARMOR-COMMON はファミリーに同じ言葉を話させるものです。ノードと [ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER) の間のすべてのメッセージはここで 1 '
               '度だけ定義され、すべての実装が通らなければならないベクトルが付きます。サーバーの HTTP コントラクトもここにあり、5 '
               'つのノード（[ARMOR-NODE-RADAR](https://github.com/JuanenRac/ARMOR-NODE-RADAR)、[ARMOR-NODE-SOLAR](https://github.com/JuanenRac/ARMOR-NODE-SOLAR)、[ARMOR-NODE-ELECTRICAL](https://github.com/JuanenRac/ARMOR-NODE-ELECTRICAL)、[ARMOR-NODE-ALARM](https://github.com/JuanenRac/ARMOR-NODE-ALARM)、[ARMOR-NODE-HMI](https://github.com/JuanenRac/ARMOR-NODE-HMI)）が共有するファームウェアは '
               '1 か所に保持され、ツールで各ノードにコピーされます。秘密は持たず、本番では何も実行しません。',
        'requirements': ['Python 3.11+']},
 'pt': {'tagline': 'Contratos de mensagens, validação, a base de firmware que os nós partilham e o lançador de projetos partilhado',
        'status': {'software': 'Os esquemas, o validador de Python, os tipos gerados de TypeScript e Kotlin, o ficheiro OpenAPI do servidor e a base de firmware '
                               'partilhada pelos cinco nós estão feitos.',
                   'tests': 'Passam 170 testes e 1228 vetores de conformidade; os analisadores de JSON, Bluetooth e Improv do firmware são também testados com '
                            'libFuzzer.',
                   'protocols': 'Só as mensagens do nó radar são usadas todos os dias com uma placa real e o servidor; as dos outros nós são verificadas contra '
                                'simulações.',
                   'integration': 'Verifica-se que a base de firmware é idêntica em cada nó; os tipos de Kotlin estão gerados, mas a app Android ainda não os usa, '
                                  'porque mantém a sua própria análise.',
                   'hardware': 'Só o nó radar executou este firmware partilhado numa placa; os outros quatro nós não.',
                   'security': 'A verificação da assinatura do firmware e a derivação do PIN Bluetooth estão testadas no anfitrião; não houve revisão independente.',
                   'docs': 'Oito idiomas, o ficheiro OpenAPI, o guia de conformidade e o registo de alterações estão atualizados.'},
        'honest': 'Os esquemas (telemetria, saúde, comando, informação do nó, inversor e bateria solares, elétrico, alarme com o seu comando e resultado, e rede), o '
                  'validador Python, os 1228 vetores de conformidade, os tipos TypeScript e Kotlin gerados, o ficheiro OpenAPI do servidor (190 caminhos), a base de '
                  'firmware partilhada pelos cinco nós e o lançador de projetos partilhado são reais e testados (170 testes). O ficheiro Kotlin é gerado mas **ainda não '
                  'é consumido** pelo ARMOR-ANDROID-CONTROL (que mantém a sua própria leitura), e o comando `set_thresholds` leva um único campo `sensitivity` porque os '
                  'parâmetros reais do radar só ficam definidos quando existir firmware.',
        'bullets': ['**Uma única fonte de verdade:** esquemas JSON em `src/armor_common/schemas/` para telemetria, saúde, comando, informação do nó, as duas mensagens '
                    'solares (inversor, bateria com células e capacidades), as mensagens elétricas (leituras, comando, resultado), as mensagens de alarme (estado, '
                    'comando, resultado) e a mensagem de rede. Campos desconhecidos e combinações impossíveis são recusados.',
                    '**Um validador que não pode saltar uma regra:** interpreta o esquema diretamente e recusa um esquema que use uma palavra-chave que não implementa.',
                    '**Vetores de conformidade:** 1228 cargas aceites e recusadas executadas por cada implementação (Python aqui, TypeScript no ARMOR-SERVER, as '
                    'verificações dos repositórios de firmware), de modo que um desvio faz falhar uma compilação.',
                    '**Clientes gerados:** os tipos TypeScript e Kotlin saem dos esquemas (`tools/generate_types.py --check` mantém-nos atuais).',
                    '**Contrato HTTP:** `openapi/armor-server.yaml` descreve cada rota do servidor (190 caminhos, 245 operações), a sua regra de acesso e um esquema com '
                    'nome para cada corpo de pedido, resposta e erro, e um teste verifica que as rotas que o servidor regista são exatamente as que descreve (método e '
                    'caminho).',
                    '**Base de firmware:** `firmware_base/` guarda uma só vez cada ficheiro que os cinco nós partilham (rede, definições e utilizadores, servidor do '
                    'painel web e login, certificado HTTPS, registo, Bluetooth com emparelhamento por PIN, verificação de atualizações assinadas; relés e Zigbee nos nós '
                    'que os têm); `tools/sync_firmware_base.py` escreve-o em cada nó e verifica que nenhuma cópia se desviou ([o guia](docs/FIRMWARE_BASE.md), [firmware '
                    'assinado](docs/SIGNED_FIRMWARE.md)).',
                    '**Lançador partilhado:** `tools/armor_project_tool.py` dá a cada repositório da família o mesmo fluxo `build`, `build-test` e `run`, e '
                    '`tools/armor_ci_validate.py` as mesmas verificações de CI.',
                    '**Ligação TLS opcional ao broker na base partilhada dos nós:** `firmware_base` traz o interruptor `mqtt.tls` e o texto `mqtt.ca_pem` (um '
                    'certificado PEM, no máximo 2 KB, validado), a ligação que confia só nessa autoridade e verifica o nome do broker, e os testes no computador '
                    'partilhados pelos cinco nós; desativada por predefinição.',
                    '**Saúde dos nós e perfis de armar:** a mensagem `node_health` (o mesmo relatório de um nó de radar, solar, elétrico, de alarme ou de painel de '
                    'parede) e o `arm_profile` (uma forma com nome de armar: que zonas vigiam, os atrasos, a sirene e com que insistência o servidor avisa, dentro do '
                    'comando de armar) têm os seus esquemas, vetores de conformidade, tipos TypeScript e Kotlin gerados, rotas OpenAPI e o código de firmware partilhado '
                    'que constrói o relatório.',
                    '**Eventos de ligação e de sistema do histórico:** os esquemas `connection_event`, `system_event` e `connection_client` (o que o histórico do '
                    'servidor diz dos clientes que se ligam e do próprio sistema, com um vocabulário fixo e nenhum campo onde possa ir um segredo), os seus vetores de '
                    'conformidade, os tipos TypeScript e Kotlin gerados e a rota OpenAPI que lista os clientes.',
                    '**Diagnóstico e qualidade das leituras no contrato:** o relatório de arranque sujo, o core dump, a verificação de segurança das definições, o '
                    'pacote de diagnóstico, os eventos do radar e as mensagens do token de diagnóstico só de leitura têm os seus esquemas, vetores de conformidade e '
                    'tipos gerados; um canal de contador pode levar a idade da sua leitura e a sua contagem de erros, e uma mensagem de inversor pode nomear os valores '
                    'que o nó manteve num limite.'],
        'intro': 'O **ARMOR-COMMON** é dono do que significa cada mensagem do A.R.M.O.R. Os nós de radar, os nós de ligação solares e o simulador produzem estas '
                 'mensagens; o servidor, a IA visual e o serviço de voz consomem-nas. Se dois projetos discordarem sobre um campo, este repositório decide.',
        'note': 'Tópicos do broker: `armor/node/{node_id}/telemetry | health | command | info`, `armor/solar/{node_id}/{device}/state`, '
                '`armor/electrical/{node_id}/state | command | result`, `armor/alarm/{node_id}/state | command | result` e `armor/network/{node_id}/state`. Veja o [guia '
                'de contratos](docs/CONTRACTS.md). O lançador partilhado cria um `.env` ignorado na primeira execução do ARMOR-SERVER com segredos aleatórios e uma '
                'palavra-passe de administrador aleatória; nada é impresso nem enviado.',
        'hardware': 'Só o nó radar funcionou numa placa: as suas mensagens são as que o servidor do CM5, o Studio e a aplicação Android falam todos os dias; as '
                    'mensagens dos outros nós são verificadas contra substitutos',
        'fit': 'O ARMOR-COMMON é o que mantém a família a falar a mesma língua. Cada mensagem entre um nó e o [ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER) '
               'é definida aqui uma vez, com os vetores que toda a implementação tem de passar; aqui vive também o contrato HTTP do servidor; e o firmware que os cinco '
               'nós partilham ([ARMOR-NODE-RADAR](https://github.com/JuanenRac/ARMOR-NODE-RADAR), [ARMOR-NODE-SOLAR](https://github.com/JuanenRac/ARMOR-NODE-SOLAR), '
               '[ARMOR-NODE-ELECTRICAL](https://github.com/JuanenRac/ARMOR-NODE-ELECTRICAL), [ARMOR-NODE-ALARM](https://github.com/JuanenRac/ARMOR-NODE-ALARM), '
               '[ARMOR-NODE-HMI](https://github.com/JuanenRac/ARMOR-NODE-HMI)) é guardado uma vez e copiado para eles por uma ferramenta. Não guarda nenhum segredo e '
               'não executa nada em produção.',
        'requirements': ['Python 3.11+']}}

# the text tree of docs/structure.json (make_structure.py --tree <language>); the repository's own check fails when it and the file disagree
TREE = {'en': 'ARMOR-COMMON/\n'
       '├── src/armor_common/\n'
       '│   ├── contracts.py               topics and validators\n'
       '│   ├── schema.py                  the schema interpreter\n'
       '│   ├── envelope.py                the common envelope\n'
       '│   ├── voice.py                   the voice turn contract\n'
       '│   ├── schemas/                   34 JSON Schemas\n'
       '│   ├── alarm_codes.json           words of each alarm code\n'
       '│   └── battery_ops.json           battery operations\n'
       '├── firmware_base/                 the firmware that the five nodes share, once\n'
       '├── conformance/                   1228 accepted and rejected payloads\n'
       '├── generated/                     TypeScript and Kotlin types (generated, do not edit)\n'
       '├── openapi/                       armor-server.yaml, HTTP contract\n'
       '├── registry/                      repositories.json, the family list\n'
       '├── fuzz/                          libFuzzer targets\n'
       '├── scripts/                       armor-project launcher\n'
       '├── tools/                         generators, firmware sync and release, launcher, CI checks\n'
       '├── tests/                         237 tests\n'
       '├── docs/                          contracts, firmware, fuzzing\n'
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
 'es': 'ARMOR-COMMON/\n'
       '├── src/armor_common/\n'
       '│   ├── contracts.py               topics y validadores\n'
       '│   ├── schema.py                  el intérprete de esquemas\n'
       '│   ├── envelope.py                el sobre común\n'
       '│   ├── voice.py                   el contrato de voz\n'
       '│   ├── schemas/                   34 JSON Schema\n'
       '│   ├── alarm_codes.json           palabras de cada alarma\n'
       '│   └── battery_ops.json           operaciones de batería\n'
       '├── firmware_base/                 el firmware que comparten los cinco nodos, una sola vez\n'
       '├── conformance/                   1228 mensajes válidos e inválidos\n'
       '├── generated/                     tipos TypeScript y Kotlin (generados, no editar)\n'
       '├── openapi/                       armor-server.yaml, contrato HTTP\n'
       '├── registry/                      repositories.json, lista de la familia\n'
       '├── fuzz/                          objetivos libFuzzer\n'
       '├── scripts/                       lanzador armor-project\n'
       '├── tools/                         generadores, sincronía y publicación del firmware, lanzador, comprobaciones de CI\n'
       '├── tests/                         237 pruebas\n'
       '├── docs/                          contratos, firmware, fuzzing\n'
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
 'de': 'ARMOR-COMMON/\n'
       '├── src/armor_common/\n'
       '│   ├── contracts.py               Topics und Validatoren\n'
       '│   ├── schema.py                  der Schema-Interpreter\n'
       '│   ├── envelope.py                der gemeinsame Umschlag\n'
       '│   ├── voice.py                   der Sprachvertrag\n'
       '│   ├── schemas/                   34 JSON-Schemas\n'
       '│   ├── alarm_codes.json           Wörter je Alarmcode\n'
       '│   └── battery_ops.json           Batterieoperationen\n'
       '├── firmware_base/                 die Firmware, die die fünf Knoten teilen, nur einmal\n'
       '├── conformance/                   1228 gültige und ungültige Nachrichten\n'
       '├── generated/                     TypeScript- und Kotlin-Typen (erzeugt, nicht bearbeiten)\n'
       '├── openapi/                       armor-server.yaml, HTTP-Vertrag\n'
       '├── registry/                      repositories.json, Familienliste\n'
       '├── fuzz/                          libFuzzer-Ziele\n'
       '├── scripts/                       armor-project-Starter\n'
       '├── tools/                         Generatoren, Firmware-Abgleich und -Release, Starter, CI-Prüfungen\n'
       '├── tests/                         237 Tests\n'
       '├── docs/                          Verträge, Firmware, Fuzzing\n'
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
 'fr': 'ARMOR-COMMON/\n'
       '├── src/armor_common/\n'
       '│   ├── contracts.py               topics et validateurs\n'
       "│   ├── schema.py                  l'interpréteur de schémas\n"
       "│   ├── envelope.py                l'enveloppe commune\n"
       '│   ├── voice.py                   le contrat vocal\n'
       '│   ├── schemas/                   34 JSON Schema\n'
       '│   ├── alarm_codes.json           mots de chaque alarme\n'
       '│   └── battery_ops.json           opérations de batterie\n'
       '├── firmware_base/                 le firmware que les cinq nœuds partagent, une seule fois\n'
       '├── conformance/                   1228 messages valides et refusés\n'
       '├── generated/                     types TypeScript et Kotlin (générés, ne pas modifier)\n'
       '├── openapi/                       armor-server.yaml, contrat HTTP\n'
       '├── registry/                      repositories.json, liste de la famille\n'
       '├── fuzz/                          cibles libFuzzer\n'
       '├── scripts/                       lanceur armor-project\n'
       '├── tools/                         générateurs, synchronisation et publication du firmware, lanceur, vérifications CI\n'
       '├── tests/                         237 tests\n'
       '├── docs/                          contrats, firmware, fuzzing\n'
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
 'it': 'ARMOR-COMMON/\n'
       '├── src/armor_common/\n'
       '│   ├── contracts.py               topic e validatori\n'
       "│   ├── schema.py                  l'interprete di schemi\n"
       '│   ├── envelope.py                la busta comune\n'
       '│   ├── voice.py                   il contratto vocale\n'
       '│   ├── schemas/                   34 JSON Schema\n'
       '│   ├── alarm_codes.json           parole di ogni allarme\n'
       '│   └── battery_ops.json           operazioni batteria\n'
       '├── firmware_base/                 il firmware che i cinque nodi condividono, una volta sola\n'
       '├── conformance/                   1228 messaggi validi e rifiutati\n'
       '├── generated/                     tipi TypeScript e Kotlin (generati, non modificare)\n'
       '├── openapi/                       armor-server.yaml, contratto HTTP\n'
       '├── registry/                      repositories.json, elenco famiglia\n'
       '├── fuzz/                          target libFuzzer\n'
       '├── scripts/                       avviatore armor-project\n'
       '├── tools/                         generatori, sincronia e rilascio del firmware, avviatore, controlli CI\n'
       '├── tests/                         237 test\n'
       '├── docs/                          contratti, firmware, fuzzing\n'
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
 'ja': 'ARMOR-COMMON/\n'
       '├── src/armor_common/\n'
       '│   ├── contracts.py               トピックと検証\n'
       '│   ├── schema.py                  スキーマ解釈器\n'
       '│   ├── envelope.py                共通エンベロープ\n'
       '│   ├── voice.py                   音声の契約\n'
       '│   ├── schemas/                   34 個の JSON Schema\n'
       '│   ├── alarm_codes.json           アラームコードの文言\n'
       '│   └── battery_ops.json           バッテリー操作\n'
       '├── firmware_base/                 5 つのノードが共有するファームウェア（1 か所）\n'
       '├── conformance/                   受理・拒否 1228 件\n'
       '├── generated/                     TypeScript と Kotlin の型（生成物、編集不可）\n'
       '├── openapi/                       armor-server.yaml（HTTP 契約）\n'
       '├── registry/                      repositories.json（一覧）\n'
       '├── fuzz/                          libFuzzer ターゲット\n'
       '├── scripts/                       armor-project 起動\n'
       '├── tools/                         ジェネレーター、ファームウェアの同期とリリース、ランチャー、CI 検査\n'
       '├── tests/                         237 件のテスト\n'
       '├── docs/                          契約・FW・ファジング\n'
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
 'zh': 'ARMOR-COMMON/\n'
       '├── src/armor_common/\n'
       '│   ├── contracts.py               主题与校验\n'
       '│   ├── schema.py                  模式解释器\n'
       '│   ├── envelope.py                通用信封\n'
       '│   ├── voice.py                   语音契约\n'
       '│   ├── schemas/                   34 个 JSON Schema\n'
       '│   ├── alarm_codes.json           报警码的文字\n'
       '│   └── battery_ops.json           电池操作\n'
       '├── firmware_base/                 五个节点共用的固件（只此一份）\n'
       '├── conformance/                   1228 条有效与无效消息\n'
       '├── generated/                     TypeScript 和 Kotlin 类型（自动生成，勿编辑）\n'
       '├── openapi/                       armor-server.yaml（HTTP 契约）\n'
       '├── registry/                      repositories.json（清单）\n'
       '├── fuzz/                          libFuzzer 目标\n'
       '├── scripts/                       armor-project 启动器\n'
       '├── tools/                         生成器、固件同步与发布、启动器、CI 检查\n'
       '├── tests/                         237 项测试\n'
       '├── docs/                          契约、固件、模糊测试\n'
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
 'pt': 'ARMOR-COMMON/\n'
       '├── src/armor_common/\n'
       '│   ├── contracts.py               tópicos e validadores\n'
       '│   ├── schema.py                  o intérprete de esquemas\n'
       '│   ├── envelope.py                o envelope comum\n'
       '│   ├── voice.py                   o contrato de voz\n'
       '│   ├── schemas/                   34 JSON Schema\n'
       '│   ├── alarm_codes.json           palavras de cada alarme\n'
       '│   └── battery_ops.json           operações de bateria\n'
       '├── firmware_base/                 o firmware que os cinco nós partilham, uma só vez\n'
       '├── conformance/                   1228 mensagens válidas e recusadas\n'
       '├── generated/                     tipos TypeScript e Kotlin (gerados, não editar)\n'
       '├── openapi/                       armor-server.yaml, contrato HTTP\n'
       '├── registry/                      repositories.json, lista da família\n'
       '├── fuzz/                          alvos libFuzzer\n'
       '├── scripts/                       lançador armor-project\n'
       '├── tools/                         geradores, sincronia e publicação do firmware, lançador, verificações de CI\n'
       '├── tests/                         237 testes\n'
       '├── docs/                          contratos, firmware, fuzzing\n'
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

DIAGRAM = 'flowchart LR\n    S["JSON Schemas (source of truth)"] --> P["armor_common (Python validator)"]\n    S --> G["generated TS + Kotlin types"]\n    S --> V["conformance vectors"]\n    V --> P\n    V --> T["ARMOR-SERVER tests"]\n    V --> X["ARMOR-NODE-SOLAR and ARMOR-NODE-ELECTRICAL checks"]\n    S --> O["OpenAPI (HTTP contract)"]'

FACTS["badges"].append(["Tests", "237%20passing", "2ea44f"])
FACTS["badges"][2][1] = "1228"


def fix(s):
    """The figures of the previous layout that moved: tests 170 -> 237, paths 190 -> 195, operations 245 -> 253."""
    return s.replace("170", "237").replace("190", "195").replace("245", "253")


def L(lg, key):
    v = LEGACY[lg][key]
    return fix(v) if isinstance(v, str) else [fix(x) for x in v]


GLANCE = [
    (GL["role"], P("Shared contracts, validator and firmware base of the family", "Contratos compartidos, validador y base de firmware de la familia", "Gemeinsame Verträge, Validator und Firmware-Basis der Familie",
                   "Contrats partagés, validateur et base de firmware de la famille", "Contratti condivisi, validatore e base firmware della famiglia", "ファミリー共通の契約、検証器、ファームウェア基盤",
                   "家族共用的契约、校验器和固件基础", "Contratos partilhados, validador e base de firmware da família")),
    (GL["stack"], P("Python 3.11+, JSON Schema, OpenAPI; C++ firmware base (ESP-IDF)", "Python 3.11+, JSON Schema, OpenAPI; base de firmware en C++ (ESP-IDF)", "Python 3.11+, JSON Schema, OpenAPI; Firmware-Basis in C++ (ESP-IDF)",
                    "Python 3.11+, JSON Schema, OpenAPI ; base de firmware C++ (ESP-IDF)", "Python 3.11+, JSON Schema, OpenAPI; base firmware in C++ (ESP-IDF)", "Python 3.11+、JSON Schema、OpenAPI、C++ のファームウェア基盤（ESP-IDF）",
                    "Python 3.11+、JSON Schema、OpenAPI；C++ 固件基础（ESP-IDF）", "Python 3.11+, JSON Schema, OpenAPI; base de firmware em C++ (ESP-IDF)")),
    (GL["tests"], P("237 (`python -m unittest discover -s tests`), 1228 conformance vectors", "237 (`python -m unittest discover -s tests`), 1228 vectores de conformidad", "237 (`python -m unittest discover -s tests`), 1228 Konformitätsvektoren",
                    "237 (`python -m unittest discover -s tests`), 1228 vecteurs de conformité", "237 (`python -m unittest discover -s tests`), 1228 vettori di conformità", "237 件（`python -m unittest discover -s tests`）、適合ベクター 1228 件",
                    "237 项（`python -m unittest discover -s tests`），1228 个一致性向量", "237 (`python -m unittest discover -s tests`), 1228 vetores de conformidade")),
    (GL["contract"], P("34 JSON Schemas, 195 HTTP paths (253 operations)", "34 JSON Schema, 195 rutas HTTP (253 operaciones)", "34 JSON-Schemas, 195 HTTP-Pfade (253 Operationen)",
                       "34 JSON Schema, 195 chemins HTTP (253 opérations)", "34 JSON Schema, 195 percorsi HTTP (253 operazioni)", "JSON Schema 34 個、HTTP パス 195 本（253 操作）",
                       "34 个 JSON Schema，195 条 HTTP 路径（253 个操作）", "34 JSON Schema, 195 caminhos HTTP (253 operações)")),
    (GL["runs"], P("Any computer (library and tools); the firmware base runs inside the five nodes", "Cualquier ordenador (biblioteca y herramientas); la base de firmware funciona dentro de los cinco nodos", "Jeder Computer (Bibliothek und Werkzeuge); die Firmware-Basis läuft in den fünf Knoten",
                   "Tout ordinateur (bibliothèque et outils) ; la base de firmware tourne dans les cinq nœuds", "Qualsiasi computer (libreria e strumenti); la base firmware gira dentro i cinque nodi", "任意のコンピューター（ライブラリとツール）。ファームウェア基盤は 5 つのノード内で動作",
                   "任意计算机（库和工具）；固件基础运行在五个节点内", "Qualquer computador (biblioteca e ferramentas); a base de firmware corre dentro dos cinco nós")),
    (GL["hardware"], P("Only the radar node has run the shared firmware on a board; the other four have not", "Solo el nodo radar ha ejecutado el firmware compartido en una placa; los otros cuatro no", "Nur der Radar-Knoten hat die gemeinsame Firmware auf einer Platine ausgeführt; die anderen vier nicht",
                       "Seul le nœud radar a exécuté le firmware partagé sur une carte ; les quatre autres non", "Solo il nodo radar ha eseguito il firmware condiviso su una scheda; gli altri quattro no", "共通ファームウェアを実機で動かしたのはレーダーノードのみで、他の 4 つは未実施",
                       "只有雷达节点在开发板上运行过共用固件；其他四个没有", "Só o nó de radar executou o firmware partilhado numa placa; os outros quatro não")),
    (GL["license"], LICENSE_VALUE),
]

ROLE_TABLE = [
    ("ARMOR-SERVER", T("runs the vectors; implements every OpenAPI route | ejecuta los vectores; implementa cada ruta de OpenAPI | führt die Vektoren aus; setzt jede OpenAPI-Route um | exécute les vecteurs ; implémente chaque route OpenAPI | esegue i vettori; implementa ogni rotta OpenAPI | ベクターを実行し、OpenAPI の全ルートを実装 | 运行向量；实现每条 OpenAPI 路由 | executa os vetores; implementa cada rota OpenAPI"),
     T("vectors, OpenAPI | vectores, OpenAPI | Vektoren, OpenAPI | vecteurs, OpenAPI | vettori, OpenAPI | ベクター、OpenAPI | 向量、OpenAPI | vetores, OpenAPI")),
    ("ARMOR-STUDIO", T("keeps a copy of the generated types; a test fails on drift | guarda una copia de los tipos generados; una prueba falla si se desvía | hält eine Kopie der erzeugten Typen; ein Test schlägt bei Abweichung fehl | garde une copie des types générés ; un test échoue en cas de dérive | tiene una copia dei tipi generati; un test fallisce se divergono | 生成された型のコピーを保持し、ずれるとテストが失敗 | 保留生成类型的副本；偏离时测试失败 | guarda uma cópia dos tipos gerados; um teste falha se divergirem"),
     T("generated TypeScript | TypeScript generado | erzeugtes TypeScript | TypeScript généré | TypeScript generato | 生成された TypeScript | 生成的 TypeScript | TypeScript gerado")),
    ("ARMOR-ANDROID-CONTROL", T("has its own parsing; the Kotlin types are generated, not used | tiene su propio análisis; los tipos Kotlin se generan pero no se usan | hat eigenes Parsing; die Kotlin-Typen werden erzeugt, aber nicht genutzt | a son propre analyse ; les types Kotlin sont générés, non utilisés | ha un parsing proprio; i tipi Kotlin sono generati ma non usati | 独自の解析を持ち、Kotlin の型は生成のみで未使用 | 有自己的解析；Kotlin 类型已生成但未使用 | tem a sua análise; os tipos Kotlin são gerados mas não usados"),
     T("generated Kotlin | Kotlin generado | erzeugtes Kotlin | Kotlin généré | Kotlin generato | 生成された Kotlin | 生成的 Kotlin | Kotlin gerado")),
    ("ARMOR-NODE-RADAR, SOLAR, ELECTRICAL, ALARM, HMI", T("receive firmware_base by `tools/sync_firmware_base.py` | reciben firmware_base con `tools/sync_firmware_base.py` | erhalten firmware_base mit `tools/sync_firmware_base.py` | reçoivent firmware_base via `tools/sync_firmware_base.py` | ricevono firmware_base con `tools/sync_firmware_base.py` | `tools/sync_firmware_base.py` で firmware_base を受け取る | 通过 `tools/sync_firmware_base.py` 接收 firmware_base | recebem firmware_base com `tools/sync_firmware_base.py`"),
     T("copied firmware | firmware copiado | kopierte Firmware | firmware copié | firmware copiato | コピーされるファームウェア | 复制的固件 | firmware copiado")),
    ("ARMOR-DOCS, ARMOR-DEVOPS, ARMOR-UPDATER", T("read `registry/repositories.json`, the one list of repositories | leen `registry/repositories.json`, la lista única de repositorios | lesen `registry/repositories.json`, die eine Liste der Repositorys | lisent `registry/repositories.json`, la liste unique des dépôts | leggono `registry/repositories.json`, l'unico elenco dei repository | リポジトリの唯一の一覧 `registry/repositories.json` を読む | 读取唯一的仓库清单 `registry/repositories.json` | leem `registry/repositories.json`, a lista única de repositórios"),
     T("the registry | el registro | das Register | le registre | il registro | レジストリ | 注册表 | o registo")),
]

SECURITY_ROWS = [
    (T("An unknown field or an impossible combination | Un campo desconocido o una combinación imposible | Ein unbekanntes Feld oder eine unmögliche Kombination | Un champ inconnu ou une combinaison impossible | Un campo sconosciuto o una combinazione impossibile | 未知のフィールドや不可能な組み合わせ | 未知字段或不可能的组合 | Um campo desconhecido ou uma combinação impossível"),
     T("`additionalProperties: false`; the validator interprets the schema and refuses to load one that uses a keyword it does not implement | `additionalProperties: false`; el validador interpreta el esquema y se niega a cargar uno con una palabra clave que no implementa | `additionalProperties: false`; der Validator interpretiert das Schema und lehnt eines mit nicht umgesetztem Schlüsselwort ab | `additionalProperties: false` ; le validateur interprète le schéma et refuse d'en charger un qui utilise un mot-clé non géré | `additionalProperties: false`; il validatore interpreta lo schema e rifiuta di caricarne uno con una parola chiave non implementata | `additionalProperties: false`。検証器はスキーマを解釈し、未実装のキーワードを使うスキーマの読み込みを拒否 | `additionalProperties: false`；校验器直接解释模式，并拒绝加载使用了未实现关键字的模式 | `additionalProperties: false`; o validador interpreta o esquema e recusa carregar um que use uma palavra-chave que não implementa")),
    (T("Telemetry without a limit to exhaust a node | Telemetría sin tope para agotar un nodo | Telemetrie ohne Obergrenze, die einen Knoten erschöpft | Une télémétrie sans plafond qui épuise un nœud | Telemetria senza tetto che esaurisce un nodo | 上限のないテレメトリでノードを枯渇させる | 无上限的遥测耗尽节点 | Telemetria sem limite que esgote um nó"),
     T("At most 15 tracks (5 for each of 3 sensors) and lux 0 to 200 000 | Como máximo 15 pistas (5 por cada uno de 3 sensores) y lux de 0 a 200 000 | Höchstens 15 Spuren (5 je 3 Sensoren) und Lux 0 bis 200 000 | Au plus 15 pistes (5 par capteur, 3 capteurs) et lux de 0 à 200 000 | Al massimo 15 tracce (5 per ciascuno di 3 sensori) e lux da 0 a 200 000 | 最大 15 トラック（3 センサー × 5）、照度 0〜200 000 | 最多 15 条轨迹（3 个传感器各 5 条），照度 0 到 200 000 | No máximo 15 pistas (5 por cada um de 3 sensores) e lux de 0 a 200 000")),
    (T("A command outside the list | Una orden fuera de la lista | Ein Befehl außerhalb der Liste | Une commande hors liste | Un comando fuori elenco | リスト外のコマンド | 列表之外的命令 | Uma ordem fora da lista"),
     T("Allow-list: `calibrate`, `set_thresholds` (sensitivity 1 to 10), `restart`; the subscriber rejects the rest before the hardware | Lista cerrada: `calibrate`, `set_thresholds` (sensibilidad 1 a 10), `restart`; el suscriptor rechaza el resto antes del hardware | Positivliste: `calibrate`, `set_thresholds` (Empfindlichkeit 1 bis 10), `restart`; der Abonnent weist den Rest vor der Hardware ab | Liste fermée : `calibrate`, `set_thresholds` (sensibilité 1 à 10), `restart` ; l'abonné rejette le reste avant le matériel | Elenco chiuso: `calibrate`, `set_thresholds` (sensibilità da 1 a 10), `restart`; il sottoscrittore rifiuta il resto prima dell'hardware | 許可リスト：`calibrate`、`set_thresholds`（感度 1〜10）、`restart`。それ以外はハードウェアに届く前に購読側が拒否 | 允许列表：`calibrate`、`set_thresholds`（灵敏度 1 到 10）、`restart`；订阅方在触及硬件前拒绝其余命令 | Lista fechada: `calibrate`, `set_thresholds` (sensibilidade 1 a 10), `restart`; o subscritor recusa o resto antes do hardware")),
    (T("A topic that does not match the node id of the body | Un topic que no coincide con el id de nodo del cuerpo | Ein Topic, das nicht zur Knoten-ID im Inhalt passt | Un topic qui ne correspond pas à l'identifiant de nœud du corps | Un topic che non corrisponde all'id del nodo nel corpo | 本文のノード ID と一致しないトピック | 主题与消息体中的节点 ID 不一致 | Um tópico que não coincide com o id do nó do corpo"),
     T("The consumer rejects the mismatch | El consumidor rechaza la discrepancia | Der Verbraucher weist die Abweichung ab | Le consommateur rejette l'écart | Il consumatore rifiuta la discrepanza | 受信側は不一致を拒否 | 消费方拒绝不一致 | O consumidor recusa a discrepância")),
    (T("A fake firmware on GitHub | Un firmware falso en GitHub | Eine gefälschte Firmware auf GitHub | Un faux firmware sur GitHub | Un firmware falso su GitHub | GitHub 上の偽ファームウェア | GitHub 上的伪造固件 | Um firmware falso no GitHub"),
     T("The image must match its `.sha256` and carry an Ed25519 signature of that hash, checked with the public key built into `firmware_base/core/fw_trust.hpp`; without it nothing changes | La imagen debe coincidir con su `.sha256` y llevar una firma Ed25519 de ese hash, comprobada con la clave pública de `firmware_base/core/fw_trust.hpp`; sin ella no cambia nada | Das Image muss zu seiner `.sha256` passen und eine Ed25519-Signatur dieses Hashes tragen, geprüft mit dem öffentlichen Schlüssel in `firmware_base/core/fw_trust.hpp`; sonst ändert sich nichts | L'image doit correspondre à son `.sha256` et porter une signature Ed25519 de ce hash, vérifiée avec la clé publique de `firmware_base/core/fw_trust.hpp` ; sinon rien ne change | L'immagine deve corrispondere al suo `.sha256` e portare una firma Ed25519 di quell'hash, verificata con la chiave pubblica di `firmware_base/core/fw_trust.hpp`; senza, non cambia nulla | イメージは `.sha256` と一致し、そのハッシュの Ed25519 署名が必要です（`firmware_base/core/fw_trust.hpp` の公開鍵で検証）。なければ何も変わりません | 镜像必须与其 `.sha256` 一致，并带有该哈希的 Ed25519 签名，用 `firmware_base/core/fw_trust.hpp` 内置公钥验证；否则不做任何更改 | A imagem tem de coincidir com o seu `.sha256` e levar uma assinatura Ed25519 desse hash, verificada com a chave pública de `firmware_base/core/fw_trust.hpp`; sem isso nada muda")),
    (T("The private release key leaks | La clave privada de publicación se filtra | Der private Release-Schlüssel gelangt nach außen | La clé privée de publication fuit | La chiave privata di rilascio trapela | リリース用の秘密鍵の漏えい | 发布私钥泄露 | A chave privada de publicação vaza"),
     T("It lives outside every repository, CI and release (PKCS#8, mode 0600); `release_firmware.py` refuses to publish when the key is not the one the firmware trusts | Vive fuera de todo repositorio, CI y publicación (PKCS#8, modo 0600); `release_firmware.py` se niega a publicar si la clave no es la que el firmware reconoce | Sie liegt außerhalb jedes Repositorys, der CI und der Releases (PKCS#8, Modus 0600); `release_firmware.py` veröffentlicht nicht, wenn der Schlüssel nicht der ist, dem die Firmware vertraut | Elle vit hors de tout dépôt, CI et publication (PKCS#8, mode 0600) ; `release_firmware.py` refuse de publier si la clé n'est pas celle que le firmware reconnaît | Vive fuori da ogni repository, CI e rilascio (PKCS#8, modo 0600); `release_firmware.py` rifiuta di pubblicare se la chiave non è quella di cui il firmware si fida | どのリポジトリ・CI・リリースにも置かれません（PKCS#8、モード 0600）。`release_firmware.py` は鍵がファームウェアの信頼する鍵と違えば公開を拒否 | 它不在任何仓库、CI 或发布中（PKCS#8，权限 0600）；密钥与固件信任的不一致时 `release_firmware.py` 拒绝发布 | Vive fora de qualquer repositório, CI e publicação (PKCS#8, modo 0600); `release_firmware.py` recusa publicar se a chave não for a que o firmware reconhece")),
    (T("Node passwords and the Bluetooth PIN | Contraseñas de nodo y PIN de Bluetooth | Knotenpasswörter und Bluetooth-PIN | Mots de passe de nœud et PIN Bluetooth | Password dei nodi e PIN Bluetooth | ノードのパスワードと Bluetooth の PIN | 节点密码和蓝牙 PIN | Palavras-passe de nó e PIN Bluetooth"),
     T("Passwords: PBKDF2-HMAC-SHA256, 10 000 rounds. PIN: derived from the MAC and the fleet secret (`CONFIG_ARMOR_FLEET_SECRET`, empty in public firmware) | Contraseñas: PBKDF2-HMAC-SHA256, 10 000 rondas. PIN: derivado de la MAC y del secreto de flota (`CONFIG_ARMOR_FLEET_SECRET`, vacío en el firmware público) | Passwörter: PBKDF2-HMAC-SHA256, 10 000 Runden. PIN: aus MAC und Flottengeheimnis abgeleitet (`CONFIG_ARMOR_FLEET_SECRET`, in öffentlicher Firmware leer) | Mots de passe : PBKDF2-HMAC-SHA256, 10 000 tours. PIN : dérivé de la MAC et du secret de flotte (`CONFIG_ARMOR_FLEET_SECRET`, vide dans le firmware public) | Password: PBKDF2-HMAC-SHA256, 10 000 giri. PIN: derivato da MAC e segreto di flotta (`CONFIG_ARMOR_FLEET_SECRET`, vuoto nel firmware pubblico) | パスワード：PBKDF2-HMAC-SHA256、10 000 回。PIN：MAC とフリート秘密から導出（`CONFIG_ARMOR_FLEET_SECRET`、公開ファームウェアでは空） | 密码：PBKDF2-HMAC-SHA256，10 000 轮。PIN：由 MAC 和车队密钥派生（`CONFIG_ARMOR_FLEET_SECRET`，公开固件中为空） | Palavras-passe: PBKDF2-HMAC-SHA256, 10 000 rondas. PIN: derivado do MAC e do segredo de frota (`CONFIG_ARMOR_FLEET_SECRET`, vazio no firmware público)")),
    (T("Exposed parsers (JSON, Bluetooth frames, Improv) | Analizadores expuestos (JSON, tramas Bluetooth, Improv) | Offene Parser (JSON, Bluetooth-Frames, Improv) | Analyseurs exposés (JSON, trames Bluetooth, Improv) | Parser esposti (JSON, frame Bluetooth, Improv) | 外部に露出するパーサ（JSON、Bluetooth フレーム、Improv） | 暴露的解析器（JSON、蓝牙帧、Improv） | Analisadores expostos (JSON, tramas Bluetooth, Improv)"),
     T("Fuzzed with libFuzzer, AddressSanitizer and UndefinedBehaviorSanitizer (`fuzz/run_fuzz.sh`, Linux with clang) | Fuzzing con libFuzzer, AddressSanitizer y UndefinedBehaviorSanitizer (`fuzz/run_fuzz.sh`, Linux con clang) | Fuzzing mit libFuzzer, AddressSanitizer und UndefinedBehaviorSanitizer (`fuzz/run_fuzz.sh`, Linux mit clang) | Fuzzing avec libFuzzer, AddressSanitizer et UndefinedBehaviorSanitizer (`fuzz/run_fuzz.sh`, Linux avec clang) | Fuzzing con libFuzzer, AddressSanitizer e UndefinedBehaviorSanitizer (`fuzz/run_fuzz.sh`, Linux con clang) | libFuzzer、AddressSanitizer、UndefinedBehaviorSanitizer でファジング（`fuzz/run_fuzz.sh`、clang のある Linux） | 用 libFuzzer、AddressSanitizer 和 UndefinedBehaviorSanitizer 做模糊测试（`fuzz/run_fuzz.sh`，带 clang 的 Linux） | Fuzzing com libFuzzer, AddressSanitizer e UndefinedBehaviorSanitizer (`fuzz/run_fuzz.sh`, Linux com clang)")),
    (T("A node copy drifts from the shared one | Una copia de un nodo se desvía de la compartida | Die Kopie eines Knotens weicht von der gemeinsamen ab | La copie d'un nœud dérive de la copie partagée | La copia di un nodo diverge da quella condivisa | ノードのコピーが共有版とずれる | 节点副本与共用版本偏离 | A cópia de um nó diverge da partilhada"),
     T("`tools/sync_firmware_base.py check` fails if the five nodes are not identical | `tools/sync_firmware_base.py check` falla si los cinco nodos no son idénticos | `tools/sync_firmware_base.py check` schlägt fehl, wenn die fünf Knoten nicht identisch sind | `tools/sync_firmware_base.py check` échoue si les cinq nœuds ne sont pas identiques | `tools/sync_firmware_base.py check` fallisce se i cinque nodi non sono identici | 5 つのノードが同一でなければ `tools/sync_firmware_base.py check` が失敗 | 五个节点不一致时 `tools/sync_firmware_base.py check` 失败 | `tools/sync_firmware_base.py check` falha se os cinco nós não forem idênticos")),
]

SECURITY_NOT = P(
    "**What it does not cover.** A firmware uploaded by hand by an administrator is not checked. A node with a firmware older than this check installs the first signed release by its hash alone. The key protects releases, not boards: with physical access anyone can flash anything. If the key is lost, the GitHub updater is blocked until the public key is replaced by a manual upload or by cable. The signature check and the PIN are tested on the host; there has been no independent review. More in [docs/SIGNED_FIRMWARE.md](docs/SIGNED_FIRMWARE.md).",
    "**Lo que no cubre.** El firmware subido a mano por un administrador no se comprueba. Un nodo con un firmware anterior a esta comprobación instala la primera versión firmada solo por su hash. La clave protege las versiones, no las placas: con acceso físico cualquiera puede grabar lo que quiera. Si se pierde la clave, el actualizador de GitHub queda bloqueado hasta cambiar la clave pública con una subida manual o por cable. La comprobación de la firma y el PIN están probados en el equipo; no ha habido revisión independiente. Más en [docs/SIGNED_FIRMWARE.md](docs/SIGNED_FIRMWARE.md).",
    "**Was es nicht abdeckt.** Eine von Hand durch einen Administrator hochgeladene Firmware wird nicht geprüft. Ein Knoten mit einer Firmware vor dieser Prüfung installiert das erste signierte Release allein anhand des Hashes. Der Schlüssel schützt Releases, nicht Platinen: Mit physischem Zugriff kann jeder alles flashen. Geht der Schlüssel verloren, ist der GitHub-Updater blockiert, bis der öffentliche Schlüssel per manuellem Upload oder Kabel ersetzt wird. Die Signaturprüfung und die PIN sind auf dem Rechner getestet; eine unabhängige Prüfung gab es nicht. Mehr in [docs/SIGNED_FIRMWARE.md](docs/SIGNED_FIRMWARE.md).",
    "**Ce qu'il ne couvre pas.** Un firmware envoyé à la main par un administrateur n'est pas vérifié. Un nœud dont le firmware précède cette vérification installe la première version signée sur son seul hash. La clé protège les versions, pas les cartes : avec un accès physique, n'importe qui peut flasher n'importe quoi. Si la clé est perdue, le programme de mise à jour GitHub reste bloqué jusqu'au remplacement de la clé publique par un envoi manuel ou par câble. La vérification de la signature et le PIN sont testés sur l'hôte ; il n'y a pas eu de revue indépendante. Plus dans [docs/SIGNED_FIRMWARE.md](docs/SIGNED_FIRMWARE.md).",
    "**Cosa non copre.** Un firmware caricato a mano da un amministratore non viene verificato. Un nodo con un firmware precedente a questo controllo installa la prima versione firmata solo in base all'hash. La chiave protegge i rilasci, non le schede: con accesso fisico chiunque può scrivere qualsiasi cosa. Se la chiave si perde, l'aggiornatore GitHub resta bloccato finché la chiave pubblica non viene sostituita con un caricamento manuale o via cavo. Il controllo della firma e il PIN sono provati sull'host; non c'è stata una revisione indipendente. Altro in [docs/SIGNED_FIRMWARE.md](docs/SIGNED_FIRMWARE.md).",
    "**対象外のこと。** 管理者が手動でアップロードしたファームウェアは検証されません。この検証より古いファームウェアのノードは、最初の署名付きリリースをハッシュだけでインストールします。鍵が守るのはリリースであって基板ではありません。物理的に触れれば誰でも何でも書き込めます。鍵を失うと、公開鍵を手動アップロードかケーブルで入れ替えるまで GitHub 更新は止まります。署名検証と PIN はホスト上でテスト済みで、第三者によるレビューはありません。詳細は [docs/SIGNED_FIRMWARE.md](docs/SIGNED_FIRMWARE.md)。",
    "**不涵盖的内容。** 管理员手动上传的固件不会被检查。固件早于此检查的节点，只凭哈希安装第一个签名版本。密钥保护的是发布版本而不是开发板：能物理接触的人可以烧录任何东西。密钥丢失后，GitHub 更新程序会被阻止，直到通过手动上传或数据线更换公钥。签名检查和 PIN 已在主机上测试；没有独立审查。详见 [docs/SIGNED_FIRMWARE.md](docs/SIGNED_FIRMWARE.md)。",
    "**O que não cobre.** Um firmware enviado à mão por um administrador não é verificado. Um nó com um firmware anterior a esta verificação instala a primeira versão assinada só pelo seu hash. A chave protege as versões, não as placas: com acesso físico qualquer pessoa grava o que quiser. Se a chave se perder, o atualizador do GitHub fica bloqueado até a chave pública ser substituída por um envio manual ou por cabo. A verificação da assinatura e o PIN estão testados no anfitrião; não houve revisão independente. Mais em [docs/SIGNED_FIRMWARE.md](docs/SIGNED_FIRMWARE.md).")

TOPICS = [
    ("`armor/node/{node_id}/telemetry`  `health`  `command`  `info`", T("a radar node: tracks, health, commands and information | un nodo radar: pistas, salud, órdenes e información | ein Radar-Knoten: Spuren, Zustand, Befehle und Information | un nœud radar : pistes, santé, commandes et informations | un nodo radar: tracce, stato, comandi e informazioni | レーダーノード：トラック、状態、コマンド、情報 | 雷达节点：轨迹、健康、命令和信息 | um nó de radar: pistas, saúde, ordens e informação")),
    ("`armor/solar/{node_id}/{device}/state`", T("an inverter or a battery of a solar node | un inversor o una batería de un nodo solar | ein Wechselrichter oder eine Batterie eines Solar-Knotens | un onduleur ou une batterie d'un nœud solaire | un inverter o una batteria di un nodo solare | ソーラーノードのインバーターまたはバッテリー | 太阳能节点的逆变器或电池 | um inversor ou uma bateria de um nó solar")),
    ("`armor/electrical/{node_id}/state`  `command`  `result`", T("the electrical node: readings, command, result | el nodo eléctrico: lecturas, orden, resultado | der Elektro-Knoten: Messwerte, Befehl, Ergebnis | le nœud électrique : mesures, commande, résultat | il nodo elettrico: letture, comando, risultato | 電気ノード：測定値、コマンド、結果 | 电气节点：读数、命令、结果 | o nó elétrico: leituras, ordem, resultado")),
    ("`armor/alarm/{node_id}/state`  `command`  `result`", T("the alarm node (also `zigbee` and `policy` from the server) | el nodo de alarma (también `zigbee` y `policy` desde el servidor) | der Alarm-Knoten (auch `zigbee` und `policy` vom Server) | le nœud d'alarme (aussi `zigbee` et `policy` du serveur) | il nodo allarme (anche `zigbee` e `policy` dal server) | アラームノード（サーバーからの `zigbee` と `policy` も） | 报警节点（还有来自服务器的 `zigbee` 和 `policy`） | o nó de alarme (também `zigbee` e `policy` do servidor)")),
    ("`armor/network/{node_id}/state`", T("what a node sees on the network | lo que un nodo ve en la red | was ein Knoten im Netz sieht | ce qu'un nœud voit sur le réseau | ciò che un nodo vede in rete | ノードがネットワークで見るもの | 节点在网络上看到的内容 | o que um nó vê na rede")),
    ("`armor/health/{node_id}`", T("the health report of any node, and its last will | el informe de salud de cualquier nodo y su último testamento | der Zustandsbericht jedes Knotens und sein Letzter Wille | le rapport de santé de tout nœud et son testament | il rapporto di salute di ogni nodo e il suo testamento | 全ノードの健康レポートと遺言メッセージ | 任意节点的健康报告及其遗嘱 | o relatório de saúde de qualquer nó e a sua última vontade")),
    ("`armor/control/{node_id}/command`  `result`  `maintenance`  and `armor/control/all/command`", T("typed orders to one node or to all, their result and the planned-maintenance signal | órdenes tipadas a un nodo o a todos, su resultado y la señal de mantenimiento previsto | typisierte Befehle an einen oder alle Knoten, ihr Ergebnis und das Wartungssignal | ordres typés vers un nœud ou tous, leur résultat et le signal de maintenance prévue | ordini tipizzati a un nodo o a tutti, il loro risultato e il segnale di manutenzione programmata | 1 ノードまたは全ノードへの型付きオーダー、その結果、計画メンテナンスの信号 | 发给一个或全部节点的类型化指令、结果及计划维护信号 | ordens tipadas para um nó ou todos, o seu resultado e o sinal de manutenção prevista")),
    ("`armor/device/{node_id}/{relay}/set`  `state`  `availability`", T("a relay of a node | un relé de un nodo | ein Relais eines Knotens | un relais d'un nœud | un relè di un nodo | ノードのリレー | 节点的继电器 | um relé de um nó")),
    ("`armor/radar/{node_id}/events`  and  `armor/server/alert`", T("radar events; alerts the server sends to the panels | eventos del radar; alertas que el servidor envía a los paneles | Radar-Ereignisse; Alarme, die der Server an die Panels sendet | événements radar ; alertes que le serveur envoie aux panneaux | eventi del radar; avvisi che il server invia ai pannelli | レーダーイベントと、サーバーからパネルへの通知 | 雷达事件；服务器发给面板的警报 | eventos do radar; alertas que o servidor envia aos painéis")),
]

TOOLS = [
    ("`tools/armor_project_tool.py`", T("the shared `build`, `build-test` and `run` workflow | el flujo compartido `build`, `build-test` y `run` | der gemeinsame Ablauf `build`, `build-test` und `run` | le flux partagé `build`, `build-test` et `run` | il flusso condiviso `build`, `build-test` e `run` | 共通の `build`、`build-test`、`run` フロー | 共用的 `build`、`build-test` 和 `run` 流程 | o fluxo partilhado `build`, `build-test` e `run`")),
    ("`tools/generate_types.py [--check]`  `generate_rest_types.py [--check]`", T("TypeScript and Kotlin types, and the types of the HTTP contract | tipos TypeScript y Kotlin, y los del contrato HTTP | TypeScript- und Kotlin-Typen und die des HTTP-Vertrags | types TypeScript et Kotlin, et ceux du contrat HTTP | tipi TypeScript e Kotlin, e quelli del contratto HTTP | TypeScript と Kotlin の型、HTTP 契約の型 | TypeScript 和 Kotlin 类型以及 HTTP 契约的类型 | tipos TypeScript e Kotlin, e os do contrato HTTP")),
    ("`tools/make_conformance.py [--check]`", T("writes the conformance vectors from the case list | escribe los vectores de conformidad desde la lista de casos | schreibt die Konformitätsvektoren aus der Fallliste | écrit les vecteurs de conformité depuis la liste de cas | scrive i vettori di conformità dall'elenco dei casi | ケース一覧から適合ベクターを書き出す | 根据用例列表写出一致性向量 | escreve os vetores de conformidade a partir da lista de casos")),
    ("`tools/sync_firmware_base.py` (`check`, `sync`, `import`)", T("writes `firmware_base` into the five nodes, or checks they have not drifted | escribe `firmware_base` en los cinco nodos, o comprueba que no se han desviado | schreibt `firmware_base` in die fünf Knoten oder prüft, dass sie nicht abgewichen sind | écrit `firmware_base` dans les cinq nœuds, ou vérifie qu'ils n'ont pas dérivé | scrive `firmware_base` nei cinque nodi, o verifica che non siano divergenti | `firmware_base` を 5 ノードへ書き込む、またはずれがないか確認 | 把 `firmware_base` 写入五个节点，或检查是否偏离 | escreve `firmware_base` nos cinco nós, ou verifica que não divergiram")),
    ("`tools/release_firmware.py`  `tools/firmware_sign.mjs`", T("signs and publishes a firmware release | firma y publica una versión de firmware | signiert und veröffentlicht ein Firmware-Release | signe et publie une version de firmware | firma e pubblica una versione del firmware | ファームウェアリリースの署名と公開 | 签名并发布固件版本 | assina e publica uma versão de firmware")),
    ("`tools/voice_cases.py`", T("the voice cases shared with ARMOR-VOICE-AI | los casos de voz compartidos con ARMOR-VOICE-AI | die mit ARMOR-VOICE-AI geteilten Sprachfälle | les cas vocaux partagés avec ARMOR-VOICE-AI | i casi vocali condivisi con ARMOR-VOICE-AI | ARMOR-VOICE-AI と共有する音声ケース | 与 ARMOR-VOICE-AI 共用的语音用例 | os casos de voz partilhados com ARMOR-VOICE-AI")),
    ("`tools/make_architecture.py`  `tools/make_structure.py`  `tools/universal_readme_check.py`", T("the pictures and the layout check of the READMEs | las imágenes y la comprobación del formato de los README | die Bilder und die Layout-Prüfung der READMEs | les images et la vérification de la mise en page des README | le immagini e il controllo del formato dei README | README の図とレイアウトの検査 | README 的图片和版式检查 | as imagens e a verificação do formato dos README")),
]

INTERFACES_SCHEMAS = P(
    "### Schemas, vectors and OpenAPI\n\n* **34 JSON Schemas** in `src/armor_common/schemas/`: telemetry, health, command, node information, node health, node control (command and result), node maintenance, solar inverter and battery (with their commands and results), electrical (with command and result), alarm (state, command, result, policy and zone feed), network (with its orders), connection and system events, radar events, server alert, arming profile, device state, diagnostic tokens, and the voice turn.\n* **1228 conformance vectors** in `conformance/` (34 files, one per message), run by this repository, by ARMOR-SERVER and by the checks of the firmware repositories.\n* **OpenAPI** `openapi/armor-server.yaml`: 195 paths and 253 operations, each with its access rule and a named schema for every body, answer and error. A test checks that the routes the server registers are exactly the ones described. The voice turn travels as bytes (see [docs/CONTRACTS.md](docs/CONTRACTS.md)).",
    "### Esquemas, vectores y OpenAPI\n\n* **34 JSON Schema** en `src/armor_common/schemas/`: telemetría, salud, orden, información del nodo, salud del nodo, control del nodo (orden y resultado), mantenimiento del nodo, inversor y batería solares (con sus órdenes y resultados), eléctrico (con orden y resultado), alarma (estado, orden, resultado, política y zonas), red (con sus órdenes), eventos de conexión y del sistema, eventos de radar, alerta del servidor, perfil de armado, estado de dispositivo, tokens de diagnóstico y el turno de voz.\n* **1228 vectores de conformidad** en `conformance/` (34 ficheros, uno por mensaje), ejecutados por este repositorio, por ARMOR-SERVER y por las comprobaciones de los repositorios de firmware.\n* **OpenAPI** `openapi/armor-server.yaml`: 195 rutas y 253 operaciones, cada una con su regla de acceso y un esquema con nombre para cada cuerpo, respuesta y error. Una prueba comprueba que las rutas que registra el servidor son exactamente las descritas. El turno de voz viaja como bytes (ver [docs/CONTRACTS.md](docs/CONTRACTS.md)).",
    "### Schemas, Vektoren und OpenAPI\n\n* **34 JSON-Schemas** in `src/armor_common/schemas/`: Telemetrie, Zustand, Befehl, Knoteninformation, Knotenzustand, Knotensteuerung (Befehl und Ergebnis), Knotenwartung, Solar-Wechselrichter und -Batterie (mit Befehlen und Ergebnissen), Elektro (mit Befehl und Ergebnis), Alarm (Zustand, Befehl, Ergebnis, Richtlinie und Zonen), Netzwerk (mit Aufträgen), Verbindungs- und Systemereignisse, Radar-Ereignisse, Server-Alarm, Scharfschaltprofil, Gerätezustand, Diagnose-Token und der Sprachturn.\n* **1228 Konformitätsvektoren** in `conformance/` (34 Dateien, eine je Nachricht), ausgeführt von diesem Repository, von ARMOR-SERVER und von den Prüfungen der Firmware-Repositorys.\n* **OpenAPI** `openapi/armor-server.yaml`: 195 Pfade und 253 Operationen, jeweils mit Zugriffsregel und einem benannten Schema für jeden Inhalt, jede Antwort und jeden Fehler. Ein Test prüft, dass die vom Server registrierten Routen genau die beschriebenen sind. Der Sprachturn wird als Bytes übertragen (siehe [docs/CONTRACTS.md](docs/CONTRACTS.md)).",
    "### Schémas, vecteurs et OpenAPI\n\n* **34 JSON Schema** dans `src/armor_common/schemas/` : télémétrie, santé, commande, informations du nœud, santé du nœud, contrôle du nœud (commande et résultat), maintenance du nœud, onduleur et batterie solaires (avec leurs commandes et résultats), électrique (avec commande et résultat), alarme (état, commande, résultat, politique et zones), réseau (avec ses ordres), événements de connexion et système, événements radar, alerte du serveur, profil d'armement, état d'appareil, jetons de diagnostic et le tour de parole.\n* **1228 vecteurs de conformité** dans `conformance/` (34 fichiers, un par message), exécutés par ce dépôt, par ARMOR-SERVER et par les vérifications des dépôts de firmware.\n* **OpenAPI** `openapi/armor-server.yaml` : 195 chemins et 253 opérations, chacun avec sa règle d'accès et un schéma nommé pour chaque corps, réponse et erreur. Un test vérifie que les routes enregistrées par le serveur sont exactement celles décrites. Le tour de parole voyage en octets (voir [docs/CONTRACTS.md](docs/CONTRACTS.md)).",
    "### Schemi, vettori e OpenAPI\n\n* **34 JSON Schema** in `src/armor_common/schemas/`: telemetria, salute, comando, informazioni del nodo, salute del nodo, controllo del nodo (comando e risultato), manutenzione del nodo, inverter e batteria solari (con comandi e risultati), elettrico (con comando e risultato), allarme (stato, comando, risultato, politica e zone), rete (con i suoi ordini), eventi di connessione e di sistema, eventi radar, avviso del server, profilo di armamento, stato del dispositivo, token di diagnostica e il turno vocale.\n* **1228 vettori di conformità** in `conformance/` (34 file, uno per messaggio), eseguiti da questo repository, da ARMOR-SERVER e dai controlli dei repository firmware.\n* **OpenAPI** `openapi/armor-server.yaml`: 195 percorsi e 253 operazioni, ciascuno con la sua regola di accesso e uno schema con nome per ogni corpo, risposta ed errore. Un test verifica che le rotte registrate dal server siano esattamente quelle descritte. Il turno vocale viaggia come byte (vedi [docs/CONTRACTS.md](docs/CONTRACTS.md)).",
    "### スキーマ、ベクター、OpenAPI\n\n* **JSON Schema 34 個**（`src/armor_common/schemas/`）：テレメトリ、健康状態、コマンド、ノード情報、ノード健康、ノード制御（コマンドと結果）、ノードメンテナンス、ソーラーのインバーターとバッテリー（コマンドと結果を含む）、電気（コマンドと結果）、アラーム（状態、コマンド、結果、ポリシー、ゾーンフィード）、ネットワーク（オーダー）、接続・システムイベント、レーダーイベント、サーバー警報、警戒プロファイル、デバイス状態、診断トークン、音声ターン。\n* **適合ベクター 1228 件**（`conformance/`、メッセージごとに 1 ファイル、計 34 ファイル）。このリポジトリ、ARMOR-SERVER、ファームウェアリポジトリの検査が実行します。\n* **OpenAPI** `openapi/armor-server.yaml`：195 パス、253 操作。各操作にアクセス規則と、本文・応答・エラーごとの名前付きスキーマがあります。サーバーが登録するルートが記述と完全に一致することをテストが確認します。音声ターンはバイト列で送られます（[docs/CONTRACTS.md](docs/CONTRACTS.md) を参照）。",
    "### 模式、向量与 OpenAPI\n\n* **34 个 JSON Schema**（`src/armor_common/schemas/`）：遥测、健康、命令、节点信息、节点健康、节点控制（命令与结果）、节点维护、太阳能逆变器和电池（含命令与结果）、电气（含命令与结果）、报警（状态、命令、结果、策略和区域）、网络（含其指令）、连接与系统事件、雷达事件、服务器警报、布防配置、设备状态、诊断令牌以及语音轮次。\n* **1228 个一致性向量**（`conformance/`，34 个文件，每条消息一个），由本仓库、ARMOR-SERVER 和固件仓库的检查运行。\n* **OpenAPI** `openapi/armor-server.yaml`：195 条路径、253 个操作，每个都有访问规则，且每个请求体、响应和错误都有命名模式。测试确认服务器注册的路由与描述完全一致。语音轮次以字节传输（见 [docs/CONTRACTS.md](docs/CONTRACTS.md)）。",
    "### Esquemas, vetores e OpenAPI\n\n* **34 JSON Schema** em `src/armor_common/schemas/`: telemetria, saúde, ordem, informação do nó, saúde do nó, controlo do nó (ordem e resultado), manutenção do nó, inversor e bateria solares (com as suas ordens e resultados), elétrico (com ordem e resultado), alarme (estado, ordem, resultado, política e zonas), rede (com as suas ordens), eventos de ligação e do sistema, eventos de radar, alerta do servidor, perfil de armamento, estado do dispositivo, tokens de diagnóstico e o turno de voz.\n* **1228 vetores de conformidade** em `conformance/` (34 ficheiros, um por mensagem), executados por este repositório, pelo ARMOR-SERVER e pelas verificações dos repositórios de firmware.\n* **OpenAPI** `openapi/armor-server.yaml`: 195 caminhos e 253 operações, cada uma com a sua regra de acesso e um esquema com nome para cada corpo, resposta e erro. Um teste verifica que as rotas que o servidor regista são exatamente as descritas. O turno de voz viaja como bytes (ver [docs/CONTRACTS.md](docs/CONTRACTS.md)).")

TOPICS_INTRO = P("### Broker topics", "### Topics del broker", "### Broker-Topics", "### Topics du broker", "### Topic del broker", "### ブローカーのトピック", "### 代理主题", "### Tópicos do broker")
TOOLS_INTRO = P("### Command-line tools", "### Herramientas de línea de órdenes", "### Kommandozeilen-Werkzeuge", "### Outils en ligne de commande", "### Strumenti da riga di comando", "### コマンドラインツール", "### 命令行工具", "### Ferramentas de linha de comandos")

CONFIG_ROWS = [
    ("`CONFIG_ARMOR_NODE_ID`", '""', T("the node's name on the broker | el nombre del nodo en el broker | der Name des Knotens am Broker | le nom du nœud sur le broker | il nome del nodo sul broker | ブローカー上のノード名 | 节点在代理上的名称 | o nome do nó no broker")),
    ("`CONFIG_ARMOR_SETUP_CODE`", '""', T("the code that opens set-up | el código que abre la configuración | der Code, der die Einrichtung öffnet | le code qui ouvre la configuration | il codice che apre la configurazione | 設定を開くコード | 打开设置的代码 | o código que abre a configuração")),
    ("`CONFIG_ARMOR_FLEET_SECRET`", '""', T("fleet secret for the Bluetooth PIN; empty in public firmware | secreto de flota para el PIN Bluetooth; vacío en el firmware público | Flottengeheimnis für die Bluetooth-PIN; in öffentlicher Firmware leer | secret de flotte pour le PIN Bluetooth ; vide dans le firmware public | segreto di flotta per il PIN Bluetooth; vuoto nel firmware pubblico | Bluetooth PIN 用のフリート秘密。公開ファームウェアでは空 | 蓝牙 PIN 的车队密钥；公开固件中为空 | segredo de frota para o PIN Bluetooth; vazio no firmware público")),
    ("`CONFIG_ARMOR_BLE_SETUP_MINUTES`", "10 (1 to 120)", T("how long Bluetooth set-up stays open | cuánto tiempo queda abierta la configuración Bluetooth | wie lange die Bluetooth-Einrichtung offen bleibt | combien de temps la configuration Bluetooth reste ouverte | quanto resta aperta la configurazione Bluetooth | Bluetooth 設定を開いておく時間（分） | 蓝牙设置保持开启的时间 | quanto tempo a configuração Bluetooth fica aberta")),
    ("`CONFIG_ARMOR_ETH_SPI_HOST`", "1 (1 to 2)", T("SPI host of the Ethernet chip | host SPI del chip Ethernet | SPI-Host des Ethernet-Chips | hôte SPI de la puce Ethernet | host SPI del chip Ethernet | Ethernet チップの SPI ホスト | 以太网芯片的 SPI 主机 | host SPI do chip Ethernet")),
    ("`CONFIG_ARMOR_ETH_MOSI` `MISO` `SCLK` `CS` `INT` `RST`", "11, 12, 13, 14, 10, 9", T("pins of the Ethernet board (profile `s3-eth`) | pines de la placa Ethernet (perfil `s3-eth`) | Pins der Ethernet-Platine (Profil `s3-eth`) | broches de la carte Ethernet (profil `s3-eth`) | pin della scheda Ethernet (profilo `s3-eth`) | Ethernet 基板のピン（プロファイル `s3-eth`） | 以太网板引脚（配置 `s3-eth`） | pinos da placa Ethernet (perfil `s3-eth`)")),
    ("`CONFIG_ARMOR_ETH_SPI_MHZ`", "20 (1 to 40)", T("SPI clock of the Ethernet chip | reloj SPI del chip Ethernet | SPI-Takt des Ethernet-Chips | horloge SPI de la puce Ethernet | clock SPI del chip Ethernet | Ethernet チップの SPI クロック | 以太网芯片 SPI 时钟 | relógio SPI do chip Ethernet")),
    ("`CONFIG_ARMOR_MQTT_URI` `USERNAME` `PASSWORD`", '""', T("first broker address and credentials | dirección y credenciales iniciales del broker | erste Broker-Adresse und Zugangsdaten | adresse et identifiants initiaux du broker | indirizzo e credenziali iniziali del broker | 最初のブローカーのアドレスと認証情報 | 初始代理地址和凭据 | endereço e credenciais iniciais do broker")),
    ("`CONFIG_ARMOR_BOOT_FACTORY_RESET`", "y", T("allows the factory reset at boot | permite el restablecimiento de fábrica al arrancar | erlaubt das Zurücksetzen beim Start | autorise la réinitialisation d'usine au démarrage | consente il ripristino di fabbrica all'avvio | 起動時の初期化を許可 | 允许启动时恢复出厂设置 | permite a reposição de fábrica no arranque")),
    ("`CONFIG_ARMOR_NTP_SERVER`", "pool.ntp.org", T("time server | servidor de hora | Zeitserver | serveur de temps | server dell'ora | 時刻サーバー | 时间服务器 | servidor de hora")),
    ("`CONFIG_ARMOR_HEARTBEAT_S`", "10 (2 to 300)", T("seconds between heartbeats | segundos entre latidos | Sekunden zwischen Herzschlägen | secondes entre les battements | secondi tra i battiti | ハートビートの間隔（秒） | 心跳间隔（秒） | segundos entre batimentos")),
    ("`CONFIG_ARMOR_BOARD_S3_WIFI`  `CONFIG_ARMOR_BOARD_S3_ETH`", "S3_WIFI", T("the board profile of the image (`tools/build_node.sh NODE BOARD`) | el perfil de placa de la imagen (`tools/build_node.sh NODE BOARD`) | das Platinenprofil des Images (`tools/build_node.sh NODE BOARD`) | le profil de carte de l'image (`tools/build_node.sh NODE BOARD`) | il profilo di scheda dell'immagine (`tools/build_node.sh NODE BOARD`) | イメージの基板プロファイル（`tools/build_node.sh NODE BOARD`） | 镜像的开发板配置（`tools/build_node.sh NODE BOARD`） | o perfil de placa da imagem (`tools/build_node.sh NODE BOARD`)")),
]

CONFIG_NOTE = P(
    "The node's own TLS link to the broker is a setting of the node (not of the build): `mqtt.tls` (off by default) and `mqtt.ca_pem` (one PEM certificate, at most 2 KB, validated); the connection trusts that authority only and checks the broker's name. The Python library has no environment variables of its own; the shared launcher creates an ignored `.env` on the first ARMOR-SERVER run with random secrets and a random administrator password, and prints and commits nothing.",
    "El enlace TLS del nodo con el broker es un ajuste del nodo (no de la compilación): `mqtt.tls` (apagado por defecto) y `mqtt.ca_pem` (un certificado PEM, 2 KB como máximo, validado); la conexión solo confía en esa autoridad y comprueba el nombre del broker. La biblioteca Python no tiene variables de entorno propias; el lanzador compartido crea un `.env` ignorado en la primera ejecución de ARMOR-SERVER con secretos aleatorios y una contraseña de administrador aleatoria, y no imprime ni sube nada.",
    "Die TLS-Verbindung des Knotens zum Broker ist eine Einstellung des Knotens (nicht des Builds): `mqtt.tls` (standardmäßig aus) und `mqtt.ca_pem` (ein PEM-Zertifikat, höchstens 2 KB, geprüft); die Verbindung vertraut nur dieser Stelle und prüft den Namen des Brokers. Die Python-Bibliothek hat keine eigenen Umgebungsvariablen; der gemeinsame Starter legt beim ersten ARMOR-SERVER-Start eine ignorierte `.env` mit zufälligen Geheimnissen und einem zufälligen Administratorpasswort an und gibt oder versioniert nichts.",
    "La liaison TLS du nœud avec le broker est un réglage du nœud (pas du build) : `mqtt.tls` (désactivé par défaut) et `mqtt.ca_pem` (un certificat PEM, 2 Ko au plus, validé) ; la connexion ne fait confiance qu'à cette autorité et vérifie le nom du broker. La bibliothèque Python n'a pas de variables d'environnement propres ; le lanceur partagé crée un `.env` ignoré au premier lancement d'ARMOR-SERVER, avec des secrets aléatoires et un mot de passe administrateur aléatoire, sans rien afficher ni versionner.",
    "Il collegamento TLS del nodo con il broker è un'impostazione del nodo (non della compilazione): `mqtt.tls` (spento di default) e `mqtt.ca_pem` (un certificato PEM, al massimo 2 KB, validato); la connessione si fida solo di quell'autorità e verifica il nome del broker. La libreria Python non ha variabili d'ambiente proprie; l'avviatore condiviso crea un `.env` ignorato alla prima esecuzione di ARMOR-SERVER con segreti casuali e una password di amministratore casuale, senza stampare né versionare nulla.",
    "ノードとブローカーの TLS 接続はビルドではなくノードの設定です：`mqtt.tls`（既定はオフ）と `mqtt.ca_pem`（PEM 証明書 1 枚、最大 2 KB、検証あり）。接続はその認証局だけを信頼し、ブローカー名を確認します。Python ライブラリ自体の環境変数はありません。共通ランチャーは ARMOR-SERVER の初回実行時に、ランダムな秘密と管理者パスワードを入れた無視対象の `.env` を作り、何も表示せずコミットもしません。",
    "节点与代理之间的 TLS 链路是节点的设置（而非构建的设置）：`mqtt.tls`（默认关闭）和 `mqtt.ca_pem`（一份 PEM 证书，最大 2 KB，经过校验）；连接只信任该机构并检查代理名称。Python 库本身没有环境变量；共用启动器会在首次运行 ARMOR-SERVER 时创建被忽略的 `.env`，其中是随机密钥和随机管理员密码，不打印也不提交任何内容。",
    "A ligação TLS do nó ao broker é uma definição do nó (não da compilação): `mqtt.tls` (desligada por predefinição) e `mqtt.ca_pem` (um certificado PEM, no máximo 2 KB, validado); a ligação só confia nessa autoridade e verifica o nome do broker. A biblioteca Python não tem variáveis de ambiente próprias; o lançador partilhado cria um `.env` ignorado na primeira execução do ARMOR-SERVER com segredos aleatórios e uma palavra-passe de administrador aleatória, e não imprime nem envia nada.")


def config_body(lg):
    head = {"en": "### Firmware build options (Kconfig)", "es": "### Opciones de compilación del firmware (Kconfig)", "de": "### Build-Optionen der Firmware (Kconfig)", "fr": "### Options de compilation du firmware (Kconfig)",
            "it": "### Opzioni di compilazione del firmware (Kconfig)", "ja": "### ファームウェアのビルドオプション（Kconfig）", "zh": "### 固件构建选项（Kconfig）", "pt": "### Opções de compilação do firmware (Kconfig)"}[lg]
    return head + "\n\n" + table(lg, "setting", CONFIG_ROWS) + "\n\n" + CONFIG_NOTE[lg]


QUICK_CODE = [
    ("python -m pip install -e .", T("install the library | instala la biblioteca | die Bibliothek installieren | installe la bibliothèque | installa la libreria | ライブラリをインストール | 安装库 | instala a biblioteca")),
    ("python -m unittest discover -s tests", T("237 tests, 1228 conformance vectors | 237 pruebas, 1228 vectores | 237 Tests, 1228 Vektoren | 237 tests, 1228 vecteurs | 237 test, 1228 vettori | 237 件のテスト、1228 ベクター | 237 项测试、1228 个向量 | 237 testes, 1228 vetores")),
    ("python tools/generate_types.py --check", T("the generated types are current | los tipos generados están al día | die erzeugten Typen sind aktuell | les types générés sont à jour | i tipi generati sono aggiornati | 生成された型は最新 | 生成的类型是最新的 | os tipos gerados estão atualizados")),
    ("python tools/generate_rest_types.py --check", T("the types of the HTTP contract are current | los tipos del contrato HTTP están al día | die Typen des HTTP-Vertrags sind aktuell | les types du contrat HTTP sont à jour | i tipi del contratto HTTP sono aggiornati | HTTP 契約の型は最新 | HTTP 契约的类型是最新的 | os tipos do contrato HTTP estão atualizados")),
    ("python tools/make_conformance.py", T("regenerate the vectors after editing the case list (--check: they are current) | regenera los vectores tras editar la lista de casos (--check: están al día) | Vektoren nach Änderung der Fallliste neu erzeugen (--check: aktuell) | régénère les vecteurs après modification de la liste de cas (--check : à jour) | rigenera i vettori dopo aver modificato l'elenco dei casi (--check: aggiornati) | ケース一覧の編集後にベクターを再生成（--check：最新か確認） | 修改用例列表后重新生成向量（--check：检查是否最新） | regenera os vetores depois de editar a lista de casos (--check: estão atualizados)")),
    ("python tools/sync_firmware_base.py check", T("the firmware the nodes share has not drifted | el firmware compartido no se ha desviado | die geteilte Firmware ist nicht abgewichen | le firmware partagé n'a pas dérivé | il firmware condiviso non è divergente | 共有ファームウェアにずれなし | 共用固件没有偏离 | o firmware partilhado não divergiu")),
]

QUICK_LEAD = P("**Requirements:** Python 3.11+ (no other package). To check the firmware base the five node repositories must be next to this one.",
               "**Requisitos:** Python 3.11+ (ningún otro paquete). Para comprobar la base de firmware, los repositorios de los cinco nodos deben estar junto a este.",
               "**Voraussetzungen:** Python 3.11+ (kein weiteres Paket). Zur Prüfung der Firmware-Basis müssen die fünf Knoten-Repositorys neben diesem liegen.",
               "**Prérequis :** Python 3.11+ (aucun autre paquet). Pour vérifier la base de firmware, les dépôts des cinq nœuds doivent se trouver à côté de celui-ci.",
               "**Requisiti:** Python 3.11+ (nessun altro pacchetto). Per verificare la base firmware i repository dei cinque nodi devono stare accanto a questo.",
               "**要件：** Python 3.11+（他のパッケージは不要）。ファームウェア基盤を検査するには、5 つのノードのリポジトリをこのリポジトリの隣に置きます。",
               "**要求：** Python 3.11+（无需其他包）。检查固件基础时，五个节点仓库必须放在本仓库旁边。",
               "**Requisitos:** Python 3.11+ (nenhum outro pacote). Para verificar a base de firmware, os repositórios dos cinco nós têm de estar ao lado deste.")

FEATURES = P(
    "### Adding or changing a message\n\n1. Edit the schema in `src/armor_common/schemas/` (and `docs/CONTRACTS.md` if the meaning changes).\n2. Add the cases to the list and run `python tools/make_conformance.py`.\n3. Run `python tools/generate_types.py` and `python tools/generate_rest_types.py` to refresh the TypeScript and Kotlin types.\n4. Update `openapi/armor-server.yaml` when a route is involved; `tests/test_openapi.py` compares it with the routes of the server.\n5. The server and the nodes then run the same vectors, so a disagreement fails a build.\n\n### The firmware base\n\n`firmware_base/` keeps once every file the five nodes share: network, settings and users, the web panel server and its login, the HTTPS certificate, the log, Bluetooth with PIN pairing, the check of a signed update, the report of node health, the guard that restarts a node in trouble, the typed orders of the server and, for the nodes that have them, relays and Zigbee. `tools/sync_firmware_base.py` writes it into every node and checks that no copy drifted (see [docs/FIRMWARE_BASE.md](docs/FIRMWARE_BASE.md) and [docs/SIGNED_FIRMWARE.md](docs/SIGNED_FIRMWARE.md)). Its decisions that need no hardware live in `core/` and are tested on a computer; `main/` reads the real values.",
    "### Añadir o cambiar un mensaje\n\n1. Edita el esquema en `src/armor_common/schemas/` (y `docs/CONTRACTS.md` si cambia el significado).\n2. Añade los casos a la lista y ejecuta `python tools/make_conformance.py`.\n3. Ejecuta `python tools/generate_types.py` y `python tools/generate_rest_types.py` para renovar los tipos TypeScript y Kotlin.\n4. Actualiza `openapi/armor-server.yaml` si interviene una ruta; `tests/test_openapi.py` lo compara con las rutas del servidor.\n5. El servidor y los nodos ejecutan entonces los mismos vectores, así que un desacuerdo rompe la compilación.\n\n### La base de firmware\n\n`firmware_base/` guarda una sola vez cada fichero que comparten los cinco nodos: red, ajustes y usuarios, el servidor del panel web y su inicio de sesión, el certificado HTTPS, el registro, Bluetooth con emparejado por PIN, la comprobación de una actualización firmada, el informe de salud del nodo, el vigilante que reinicia un nodo en apuros, las órdenes tipadas del servidor y, en los nodos que los tienen, relés y Zigbee. `tools/sync_firmware_base.py` lo escribe en cada nodo y comprueba que ninguna copia se ha desviado (ver [docs/FIRMWARE_BASE.md](docs/FIRMWARE_BASE.md) y [docs/SIGNED_FIRMWARE.md](docs/SIGNED_FIRMWARE.md)). Sus decisiones que no necesitan hardware viven en `core/` y se prueban en un ordenador; `main/` lee los valores reales.",
    "### Eine Nachricht hinzufügen oder ändern\n\n1. Das Schema in `src/armor_common/schemas/` bearbeiten (und `docs/CONTRACTS.md`, wenn sich die Bedeutung ändert).\n2. Die Fälle in die Liste eintragen und `python tools/make_conformance.py` ausführen.\n3. `python tools/generate_types.py` und `python tools/generate_rest_types.py` ausführen, um die TypeScript- und Kotlin-Typen zu erneuern.\n4. `openapi/armor-server.yaml` aktualisieren, wenn eine Route beteiligt ist; `tests/test_openapi.py` vergleicht sie mit den Routen des Servers.\n5. Server und Knoten führen dann dieselben Vektoren aus, ein Widerspruch lässt also den Build scheitern.\n\n### Die Firmware-Basis\n\n`firmware_base/` hält jede Datei, die die fünf Knoten teilen, genau einmal: Netzwerk, Einstellungen und Benutzer, den Webpanel-Server samt Anmeldung, das HTTPS-Zertifikat, das Protokoll, Bluetooth mit PIN-Kopplung, die Prüfung eines signierten Updates, den Knotenzustandsbericht, den Wächter, der einen Knoten in Not neu startet, die typisierten Befehle des Servers und, wo vorhanden, Relais und Zigbee. `tools/sync_firmware_base.py` schreibt sie in jeden Knoten und prüft, dass keine Kopie abweicht (siehe [docs/FIRMWARE_BASE.md](docs/FIRMWARE_BASE.md) und [docs/SIGNED_FIRMWARE.md](docs/SIGNED_FIRMWARE.md)). Entscheidungen ohne Hardware stehen in `core/` und werden auf dem Rechner getestet; `main/` liest die echten Werte.",
    "### Ajouter ou modifier un message\n\n1. Modifier le schéma dans `src/armor_common/schemas/` (et `docs/CONTRACTS.md` si le sens change).\n2. Ajouter les cas à la liste et lancer `python tools/make_conformance.py`.\n3. Lancer `python tools/generate_types.py` et `python tools/generate_rest_types.py` pour renouveler les types TypeScript et Kotlin.\n4. Mettre à jour `openapi/armor-server.yaml` si une route est concernée ; `tests/test_openapi.py` le compare aux routes du serveur.\n5. Le serveur et les nœuds exécutent alors les mêmes vecteurs : un désaccord fait échouer le build.\n\n### La base de firmware\n\n`firmware_base/` garde une seule fois chaque fichier que partagent les cinq nœuds : réseau, réglages et utilisateurs, le serveur du panneau web et sa connexion, le certificat HTTPS, le journal, le Bluetooth avec appairage par PIN, la vérification d'une mise à jour signée, le rapport de santé du nœud, le garde qui redémarre un nœud en difficulté, les ordres typés du serveur et, pour les nœuds qui en ont, relais et Zigbee. `tools/sync_firmware_base.py` l'écrit dans chaque nœud et vérifie qu'aucune copie n'a dérivé (voir [docs/FIRMWARE_BASE.md](docs/FIRMWARE_BASE.md) et [docs/SIGNED_FIRMWARE.md](docs/SIGNED_FIRMWARE.md)). Ses décisions qui n'ont pas besoin de matériel vivent dans `core/` et sont testées sur un ordinateur ; `main/` lit les vraies valeurs.",
    "### Aggiungere o cambiare un messaggio\n\n1. Modifica lo schema in `src/armor_common/schemas/` (e `docs/CONTRACTS.md` se cambia il significato).\n2. Aggiungi i casi all'elenco ed esegui `python tools/make_conformance.py`.\n3. Esegui `python tools/generate_types.py` e `python tools/generate_rest_types.py` per rinnovare i tipi TypeScript e Kotlin.\n4. Aggiorna `openapi/armor-server.yaml` se è coinvolta una rotta; `tests/test_openapi.py` lo confronta con le rotte del server.\n5. Server e nodi eseguono poi gli stessi vettori, quindi un disaccordo fa fallire la compilazione.\n\n### La base firmware\n\n`firmware_base/` conserva una sola volta ogni file che i cinque nodi condividono: rete, impostazioni e utenti, il server del pannello web e il suo accesso, il certificato HTTPS, il registro, il Bluetooth con abbinamento a PIN, il controllo di un aggiornamento firmato, il rapporto di salute del nodo, la guardia che riavvia un nodo in difficoltà, gli ordini tipizzati del server e, per i nodi che li hanno, relè e Zigbee. `tools/sync_firmware_base.py` la scrive in ogni nodo e verifica che nessuna copia sia divergente (vedi [docs/FIRMWARE_BASE.md](docs/FIRMWARE_BASE.md) e [docs/SIGNED_FIRMWARE.md](docs/SIGNED_FIRMWARE.md)). Le decisioni che non richiedono hardware stanno in `core/` e si provano su un computer; `main/` legge i valori reali.",
    "### メッセージの追加と変更\n\n1. `src/armor_common/schemas/` のスキーマを編集します（意味が変わるなら `docs/CONTRACTS.md` も）。\n2. ケースを一覧に追加し、`python tools/make_conformance.py` を実行します。\n3. `python tools/generate_types.py` と `python tools/generate_rest_types.py` を実行し、TypeScript と Kotlin の型を更新します。\n4. ルートが関わる場合は `openapi/armor-server.yaml` を更新します。`tests/test_openapi.py` がサーバーのルートと照合します。\n5. サーバーとノードは同じベクターを実行するので、食い違いはビルドの失敗になります。\n\n### ファームウェア基盤\n\n`firmware_base/` は、5 つのノードが共有するファイルを 1 か所だけに置きます：ネットワーク、設定とユーザー、Web パネルサーバーとログイン、HTTPS 証明書、ログ、PIN ペアリング付き Bluetooth、署名付き更新の検証、ノード健康レポート、不調のノードを再起動する監視、サーバーからの型付きオーダー、そして該当ノードのリレーと Zigbee。`tools/sync_firmware_base.py` が各ノードへ書き込み、ずれがないか確認します（[docs/FIRMWARE_BASE.md](docs/FIRMWARE_BASE.md) と [docs/SIGNED_FIRMWARE.md](docs/SIGNED_FIRMWARE.md) を参照）。ハードウェア不要の判定は `core/` にあり、コンピューターでテストされます。`main/` が実際の値を読みます。",
    "### 添加或修改消息\n\n1. 编辑 `src/armor_common/schemas/` 中的模式（含义改变时同时改 `docs/CONTRACTS.md`）。\n2. 把用例加入列表并运行 `python tools/make_conformance.py`。\n3. 运行 `python tools/generate_types.py` 和 `python tools/generate_rest_types.py` 更新 TypeScript 和 Kotlin 类型。\n4. 涉及路由时更新 `openapi/armor-server.yaml`；`tests/test_openapi.py` 会把它与服务器的路由对比。\n5. 服务器和节点随后运行同样的向量，因此任何分歧都会使构建失败。\n\n### 固件基础\n\n`firmware_base/` 把五个节点共用的每个文件只保存一份：网络、设置和用户、网页面板服务器及其登录、HTTPS 证书、日志、带 PIN 配对的蓝牙、签名更新的检查、节点健康报告、让异常节点重启的守护、服务器的类型化指令，以及有此功能节点的继电器和 Zigbee。`tools/sync_firmware_base.py` 把它写入每个节点并检查没有副本偏离（见 [docs/FIRMWARE_BASE.md](docs/FIRMWARE_BASE.md) 和 [docs/SIGNED_FIRMWARE.md](docs/SIGNED_FIRMWARE.md)）。无需硬件的判定在 `core/` 中，在电脑上测试；`main/` 读取真实值。",
    "### Adicionar ou alterar uma mensagem\n\n1. Edite o esquema em `src/armor_common/schemas/` (e `docs/CONTRACTS.md` se o significado mudar).\n2. Adicione os casos à lista e execute `python tools/make_conformance.py`.\n3. Execute `python tools/generate_types.py` e `python tools/generate_rest_types.py` para renovar os tipos TypeScript e Kotlin.\n4. Atualize `openapi/armor-server.yaml` se houver uma rota envolvida; `tests/test_openapi.py` compara-o com as rotas do servidor.\n5. O servidor e os nós executam então os mesmos vetores, por isso um desacordo faz falhar a compilação.\n\n### A base de firmware\n\n`firmware_base/` guarda uma só vez cada ficheiro que os cinco nós partilham: rede, definições e utilizadores, o servidor do painel web e o seu início de sessão, o certificado HTTPS, o registo, Bluetooth com emparelhamento por PIN, a verificação de uma atualização assinada, o relatório de saúde do nó, o guarda que reinicia um nó em dificuldades, as ordens tipadas do servidor e, nos nós que os têm, relés e Zigbee. `tools/sync_firmware_base.py` escreve-a em cada nó e verifica que nenhuma cópia divergiu (ver [docs/FIRMWARE_BASE.md](docs/FIRMWARE_BASE.md) e [docs/SIGNED_FIRMWARE.md](docs/SIGNED_FIRMWARE.md)). As decisões que não precisam de hardware vivem em `core/` e testam-se num computador; `main/` lê os valores reais.")

TEST_FILES = [
    ("`test_contracts.py`", "68", T("every message, topic and splitter, with the conformance vectors | cada mensaje, topic y separador, con los vectores de conformidad | jede Nachricht, jedes Topic und jeder Zerleger, mit den Konformitätsvektoren | chaque message, topic et découpeur, avec les vecteurs de conformité | ogni messaggio, topic e separatore, con i vettori di conformità | 全メッセージ、トピック、分解処理と適合ベクター | 每条消息、主题和拆分器及一致性向量 | cada mensagem, tópico e separador, com os vetores de conformidade")),
    ("`test_task_safety_check.py`", "23", T("the scan that finds the tasks a node cannot do without | el escaneo que encuentra las tareas que un nodo no puede perder | der Scan, der die unverzichtbaren Tasks eines Knotens findet | le balayage qui trouve les tâches indispensables d'un nœud | la scansione che trova i task indispensabili di un nodo | ノードに不可欠なタスクを見つける走査 | 查找节点不可缺少的任务的扫描 | a varredura que encontra as tarefas indispensáveis de um nó")),
    ("`test_universal_readme_check.py`, `test_readme_tools.py`", "36", T("the layout check and the pictures of the READMEs | la comprobación del formato y las imágenes de los README | die Layout-Prüfung und die Bilder der READMEs | la vérification de mise en page et les images des README | il controllo del formato e le immagini dei README | README のレイアウト検査と図 | README 版式检查与图片 | a verificação do formato e as imagens dos README")),
    ("`test_firmware_base.py`", "13", T("the shared firmware base and its sync | la base de firmware compartida y su sincronía | die geteilte Firmware-Basis und ihr Abgleich | la base de firmware partagée et sa synchronisation | la base firmware condivisa e la sua sincronia | 共有ファームウェア基盤と同期 | 共用固件基础及其同步 | a base de firmware partilhada e a sua sincronia")),
    ("`test_openapi.py`", "13", T("the OpenAPI file against the routes of the server | el fichero OpenAPI frente a las rutas del servidor | die OpenAPI-Datei gegen die Routen des Servers | le fichier OpenAPI face aux routes du serveur | il file OpenAPI rispetto alle rotte del server | OpenAPI とサーバーのルートの照合 | OpenAPI 文件与服务器路由 | o ficheiro OpenAPI contra as rotas do servidor")),
    ("`test_release_firmware.py`", "12", T("the signing and publication of firmware | la firma y publicación del firmware | Signatur und Veröffentlichung der Firmware | la signature et la publication du firmware | la firma e la pubblicazione del firmware | ファームウェアの署名と公開 | 固件的签名与发布 | a assinatura e publicação do firmware")),
    ("`test_pretty_run.py`, `test_build_scripts.py`", "11", T("the live panel of the scripts | el panel en vivo de los scripts | das Live-Panel der Skripte | le panneau en direct des scripts | il pannello dal vivo degli script | スクリプトのライブパネル | 脚本的实时面板 | o painel em direto dos scripts")),
    ("`test_generated_types.py`, `test_repository_registry.py`, `test_voice_turn.py`", "21", T("the generated types, the repository list and the voice turn | los tipos generados, la lista de repositorios y el turno de voz | die erzeugten Typen, die Repository-Liste und der Sprachturn | les types générés, la liste des dépôts et le tour de parole | i tipi generati, l'elenco dei repository e il turno vocale | 生成型、リポジトリ一覧、音声ターン | 生成类型、仓库清单和语音轮次 | os tipos gerados, a lista de repositórios e o turno de voz")),
    ("`test_alarm_codes.py`, `test_collect_errors.py`, `test_project_manifest_doc.py`, `test_firmware_fuzz.py`, `test_fuzz_validator.py`", "17", T("alarm code words, error collection, the manifest guide and the fuzz harness | palabras de los códigos de alarma, recogida de errores, guía del manifiesto y banco de fuzzing | Alarmcode-Wörter, Fehlersammlung, Manifest-Leitfaden und Fuzz-Gerüst | mots des codes d'alarme, collecte d'erreurs, guide du manifeste et banc de fuzzing | parole dei codici di allarme, raccolta errori, guida al manifesto e banco di fuzzing | アラームコードの文言、エラー収集、マニフェスト解説、ファズ環境 | 报警码文字、错误收集、清单指南和模糊测试环境 | palavras dos códigos de alarme, recolha de erros, guia do manifesto e banco de fuzzing")),
]
TEST_NOTE = P(
    "The host tests of the shared firmware are in `firmware_base/tests/` (C++, no ESP-IDF needed) and run from the node repositories' own checks. `python tools/sync_firmware_base.py check` needs the five node repositories next to this one. GitHub Actions runs the A.R.M.O.R. baseline on every push and pull request: the validation of the manifest, version, changelog and README parity, then the project's own build and tests.",
    "Las pruebas de equipo del firmware compartido están en `firmware_base/tests/` (C++, sin ESP-IDF) y las ejecutan las comprobaciones de los propios repositorios de los nodos. `python tools/sync_firmware_base.py check` necesita los repositorios de los cinco nodos junto a este. GitHub Actions ejecuta la base de A.R.M.O.R. en cada push y pull request: la validación del manifiesto, la versión, el registro de cambios y la paridad de los README, y luego la compilación y las pruebas del propio proyecto.",
    "Die Host-Tests der gemeinsamen Firmware liegen in `firmware_base/tests/` (C++, ohne ESP-IDF) und laufen in den Prüfungen der Knoten-Repositorys. `python tools/sync_firmware_base.py check` braucht die fünf Knoten-Repositorys neben diesem. GitHub Actions führt bei jedem Push und Pull Request die A.R.M.O.R.-Basis aus: die Prüfung von Manifest, Version, Änderungsprotokoll und README-Parität, dann den eigenen Build und die eigenen Tests des Projekts.",
    "Les tests hôte du firmware partagé sont dans `firmware_base/tests/` (C++, sans ESP-IDF) et s'exécutent dans les vérifications des dépôts des nœuds. `python tools/sync_firmware_base.py check` a besoin des dépôts des cinq nœuds à côté de celui-ci. GitHub Actions exécute la base A.R.M.O.R. à chaque push et pull request : la validation du manifeste, de la version, du journal des modifications et de la parité des README, puis le build et les tests propres au projet.",
    "I test host del firmware condiviso sono in `firmware_base/tests/` (C++, senza ESP-IDF) e girano nei controlli dei repository dei nodi. `python tools/sync_firmware_base.py check` richiede i repository dei cinque nodi accanto a questo. GitHub Actions esegue la base A.R.M.O.R. a ogni push e pull request: la validazione di manifesto, versione, registro delle modifiche e parità dei README, poi la compilazione e i test del progetto.",
    "共有ファームウェアのホストテストは `firmware_base/tests/`（C++、ESP-IDF 不要）にあり、各ノードリポジトリの検査から実行されます。`python tools/sync_firmware_base.py check` には 5 つのノードのリポジトリがこのリポジトリの隣に必要です。GitHub Actions は push と pull request のたびに A.R.M.O.R. の基本検査（マニフェスト、バージョン、変更履歴、README の一致）と、プロジェクト自身のビルドとテストを実行します。",
    "共用固件的主机测试在 `firmware_base/tests/`（C++，无需 ESP-IDF），由各节点仓库自己的检查运行。`python tools/sync_firmware_base.py check` 需要五个节点仓库放在本仓库旁边。GitHub Actions 在每次推送和拉取请求时运行 A.R.M.O.R. 基线：清单、版本、更新日志和 README 一致性的校验，然后是项目自身的构建和测试。",
    "Os testes de anfitrião do firmware partilhado estão em `firmware_base/tests/` (C++, sem ESP-IDF) e correm nas verificações dos próprios repositórios dos nós. `python tools/sync_firmware_base.py check` precisa dos repositórios dos cinco nós ao lado deste. O GitHub Actions executa a base do A.R.M.O.R. em cada push e pull request: a validação do manifesto, da versão, do registo de alterações e da paridade dos README, e depois a compilação e os testes do próprio projeto.")

BUILD = P("It is plain Python and a set of tools: nothing to compile. The version lives in `pyproject.toml`, in `armor.project.json` and in the README badge (read from the manifest); each version has its entry in [CHANGELOG.md](CHANGELOG.md). Releases are published on GitHub. The firmware release tool (`tools/release_firmware.py`) signs and publishes the images of the nodes; the key it needs is never in a repository.",
          "Es Python puro y un conjunto de herramientas: no hay nada que compilar. La versión vive en `pyproject.toml`, en `armor.project.json` y en la insignia del README (leída del manifiesto); cada versión tiene su entrada en [CHANGELOG.md](CHANGELOG.md). Las versiones se publican en GitHub. La herramienta de publicación de firmware (`tools/release_firmware.py`) firma y publica las imágenes de los nodos; la clave que necesita nunca está en un repositorio.",
          "Es ist reines Python und eine Reihe von Werkzeugen: Es gibt nichts zu kompilieren. Die Version steht in `pyproject.toml`, in `armor.project.json` und im README-Badge (aus dem Manifest gelesen); jede Version hat ihren Eintrag in [CHANGELOG.md](CHANGELOG.md). Releases werden auf GitHub veröffentlicht. Das Firmware-Release-Werkzeug (`tools/release_firmware.py`) signiert und veröffentlicht die Images der Knoten; der nötige Schlüssel liegt nie in einem Repository.",
          "C'est du Python pur et un ensemble d'outils : rien à compiler. La version se trouve dans `pyproject.toml`, dans `armor.project.json` et dans le badge du README (lu depuis le manifeste) ; chaque version a son entrée dans [CHANGELOG.md](CHANGELOG.md). Les versions sont publiées sur GitHub. L'outil de publication de firmware (`tools/release_firmware.py`) signe et publie les images des nœuds ; la clé dont il a besoin n'est jamais dans un dépôt.",
          "È Python puro e un insieme di strumenti: nulla da compilare. La versione risiede in `pyproject.toml`, in `armor.project.json` e nel badge del README (letto dal manifesto); ogni versione ha la sua voce in [CHANGELOG.md](CHANGELOG.md). Le versioni sono pubblicate su GitHub. Lo strumento di rilascio del firmware (`tools/release_firmware.py`) firma e pubblica le immagini dei nodi; la chiave che richiede non sta mai in un repository.",
          "純粋な Python とツール群なので、コンパイルするものはありません。バージョンは `pyproject.toml`、`armor.project.json`、README のバッジ（マニフェストから読み取り）にあり、各バージョンには [CHANGELOG.md](CHANGELOG.md) にエントリーがあります。リリースは GitHub で公開されます。ファームウェアのリリースツール（`tools/release_firmware.py`）がノードのイメージに署名して公開します。必要な鍵はリポジトリに置かれません。",
          "这是纯 Python 加一组工具：无需编译。版本记录在 `pyproject.toml`、`armor.project.json` 和 README 徽章中（读取自清单）；每个版本在 [CHANGELOG.md](CHANGELOG.md) 中都有对应条目。发布版本发布在 GitHub 上。固件发布工具（`tools/release_firmware.py`）为节点镜像签名并发布；它所需的密钥从不在仓库里。",
          "É Python puro e um conjunto de ferramentas: não há nada para compilar. A versão está em `pyproject.toml`, em `armor.project.json` e no emblema do README (lido do manifesto); cada versão tem a sua entrada em [CHANGELOG.md](CHANGELOG.md). As versões são publicadas no GitHub. A ferramenta de publicação de firmware (`tools/release_firmware.py`) assina e publica as imagens dos nós; a chave de que precisa nunca está num repositório.")

TROUBLE = [
    ("`FIRMWARE_BASE=FAIL ... copies drifted`", T("a node changed a shared file by hand | un nodo cambió a mano un fichero compartido | ein Knoten hat eine geteilte Datei von Hand geändert | un nœud a modifié à la main un fichier partagé | un nodo ha modificato a mano un file condiviso | ノードが共有ファイルを手で変更した | 某节点手动改了共用文件 | um nó alterou à mão um ficheiro partilhado"),
     T("make the change in `firmware_base/` and run `sync`; or `import` to take the nodes' files as they are | haz el cambio en `firmware_base/` y ejecuta `sync`; o `import` para tomar los ficheros de los nodos tal cual | die Änderung in `firmware_base/` machen und `sync` ausführen; oder `import`, um die Dateien der Knoten zu übernehmen | faites le changement dans `firmware_base/` et lancez `sync` ; ou `import` pour reprendre les fichiers des nœuds tels quels | fai la modifica in `firmware_base/` ed esegui `sync`; oppure `import` per prendere i file dei nodi così come sono | `firmware_base/` で変更して `sync` を実行。ノード側のファイルをそのまま採用するなら `import` | 在 `firmware_base/` 中修改并运行 `sync`；或用 `import` 原样采用节点的文件 | faça a alteração em `firmware_base/` e execute `sync`; ou `import` para tomar os ficheiros dos nós tal como estão")),
    ("`ARMOR-NODE-HMI: main/secret_vault.cpp is missing`", T("the node repositories are not next to ARMOR-COMMON | los repositorios de los nodos no están junto a ARMOR-COMMON | die Knoten-Repositorys liegen nicht neben ARMOR-COMMON | les dépôts des nœuds ne sont pas à côté d'ARMOR-COMMON | i repository dei nodi non sono accanto ad ARMOR-COMMON | ノードのリポジトリが ARMOR-COMMON の隣にない | 节点仓库不在 ARMOR-COMMON 旁边 | os repositórios dos nós não estão ao lado do ARMOR-COMMON"),
     T("clone them side by side | clónalos uno junto al otro | nebeneinander klonen | clonez-les côte à côte | clonali affiancati | 並べてクローンする | 并排克隆 | clone-os lado a lado")),
    ("`generated types are out of date`", T("a schema or the OpenAPI file changed | cambió un esquema o el fichero OpenAPI | ein Schema oder die OpenAPI-Datei hat sich geändert | un schéma ou le fichier OpenAPI a changé | è cambiato uno schema o il file OpenAPI | スキーマまたは OpenAPI が変更された | 模式或 OpenAPI 文件变了 | mudou um esquema ou o ficheiro OpenAPI"),
     T("run `generate_types.py` and `generate_rest_types.py` without `--check` | ejecuta `generate_types.py` y `generate_rest_types.py` sin `--check` | `generate_types.py` und `generate_rest_types.py` ohne `--check` ausführen | lancez `generate_types.py` et `generate_rest_types.py` sans `--check` | esegui `generate_types.py` e `generate_rest_types.py` senza `--check` | `--check` なしで `generate_types.py` と `generate_rest_types.py` を実行 | 不带 `--check` 运行 `generate_types.py` 和 `generate_rest_types.py` | execute `generate_types.py` e `generate_rest_types.py` sem `--check`")),
    ("`TASK_SAFETY=FAIL no task found: the scan is broken`", T("the scan of the node sources found nothing | el escaneo de los fuentes de los nodos no encontró nada | der Scan der Knoten-Quellen fand nichts | le balayage des sources des nœuds n'a rien trouvé | la scansione dei sorgenti dei nodi non ha trovato nulla | ノードのソース走査で何も見つからない | 对节点源码的扫描什么也没找到 | a varredura dos fontes dos nós não encontrou nada"),
     T("check that the node repositories are next to this one | comprueba que los repositorios de los nodos están junto a este | prüfen, dass die Knoten-Repositorys neben diesem liegen | vérifiez que les dépôts des nœuds sont à côté de celui-ci | verifica che i repository dei nodi siano accanto a questo | ノードのリポジトリがここの隣にあるか確認 | 检查节点仓库是否在本仓库旁边 | verifique se os repositórios dos nós estão ao lado deste")),
    ("`no_signature`, `bad_signature`, `checksum_mismatch`, `wrong_firmware`", T("the node refused a release: missing or wrong signature, hash or board | el nodo rechazó una versión: firma, hash o placa ausentes o erróneos | der Knoten lehnte ein Release ab: Signatur, Hash oder Platine fehlt oder falsch | le nœud a refusé une version : signature, hash ou carte absents ou faux | il nodo ha rifiutato una versione: firma, hash o scheda mancanti o errati | ノードがリリースを拒否：署名、ハッシュ、基板の欠落または不一致 | 节点拒绝了某版本：签名、哈希或开发板缺失或错误 | o nó recusou uma versão: assinatura, hash ou placa em falta ou erradas"),
     T("publish with `tools/release_firmware.py` and the release key the firmware trusts | publica con `tools/release_firmware.py` y la clave que el firmware reconoce | mit `tools/release_firmware.py` und dem Schlüssel veröffentlichen, dem die Firmware vertraut | publiez avec `tools/release_firmware.py` et la clé que le firmware reconnaît | pubblica con `tools/release_firmware.py` e la chiave di cui il firmware si fida | `tools/release_firmware.py` とファームウェアが信頼するリリース鍵で公開 | 用 `tools/release_firmware.py` 和固件信任的发布密钥来发布 | publique com `tools/release_firmware.py` e a chave que o firmware reconhece")),
]

ROADMAP = P(
    "**Known limits today**\n\n* The Kotlin types are generated but **not yet used** by ARMOR-ANDROID-CONTROL, which keeps its own parsing.\n* The `set_thresholds` command carries a single `sensitivity` field: the real radar parameters are not defined until the firmware exists.\n* Only the radar node has run the shared firmware on a board; the other four nodes have not.\n* No independent security review.\n\n**Next**\n\n* Let the Android app use the generated Kotlin types.\n* Define the real radar parameters of `set_thresholds`.\n* Run the shared firmware on the boards of the other four nodes.",
    "**Límites conocidos hoy**\n\n* Los tipos Kotlin se generan pero **aún no se usan** en ARMOR-ANDROID-CONTROL, que mantiene su propio análisis.\n* La orden `set_thresholds` lleva un único campo `sensitivity`: los parámetros reales del radar no se definen hasta que exista el firmware.\n* Solo el nodo radar ha ejecutado el firmware compartido en una placa; los otros cuatro no.\n* Sin revisión de seguridad independiente.\n\n**Lo siguiente**\n\n* Que la aplicación Android use los tipos Kotlin generados.\n* Definir los parámetros reales del radar de `set_thresholds`.\n* Ejecutar el firmware compartido en las placas de los otros cuatro nodos.",
    "**Bekannte Grenzen heute**\n\n* Die Kotlin-Typen werden erzeugt, aber von ARMOR-ANDROID-CONTROL **noch nicht genutzt**; die App behält ihr eigenes Parsing.\n* Der Befehl `set_thresholds` hat nur ein Feld `sensitivity`: Die echten Radar-Parameter werden erst definiert, wenn die Firmware existiert.\n* Nur der Radar-Knoten hat die gemeinsame Firmware auf einer Platine ausgeführt; die anderen vier nicht.\n* Keine unabhängige Sicherheitsprüfung.\n\n**Als Nächstes**\n\n* Die Android-App soll die erzeugten Kotlin-Typen nutzen.\n* Die echten Radar-Parameter von `set_thresholds` festlegen.\n* Die gemeinsame Firmware auf den Platinen der anderen vier Knoten ausführen.",
    "**Limites connues aujourd'hui**\n\n* Les types Kotlin sont générés mais **pas encore utilisés** par ARMOR-ANDROID-CONTROL, qui garde sa propre analyse.\n* La commande `set_thresholds` n'a qu'un champ `sensitivity` : les vrais paramètres du radar ne sont définis qu'une fois le firmware existant.\n* Seul le nœud radar a exécuté le firmware partagé sur une carte ; les quatre autres non.\n* Pas de revue de sécurité indépendante.\n\n**Prochainement**\n\n* Que l'application Android utilise les types Kotlin générés.\n* Définir les vrais paramètres radar de `set_thresholds`.\n* Exécuter le firmware partagé sur les cartes des quatre autres nœuds.",
    "**Limiti noti oggi**\n\n* I tipi Kotlin sono generati ma **non ancora usati** da ARMOR-ANDROID-CONTROL, che mantiene il proprio parsing.\n* Il comando `set_thresholds` ha un solo campo `sensitivity`: i veri parametri del radar non sono definiti finché non esiste il firmware.\n* Solo il nodo radar ha eseguito il firmware condiviso su una scheda; gli altri quattro no.\n* Nessuna revisione di sicurezza indipendente.\n\n**Prossimi passi**\n\n* Far usare all'app Android i tipi Kotlin generati.\n* Definire i veri parametri radar di `set_thresholds`.\n* Eseguire il firmware condiviso sulle schede degli altri quattro nodi.",
    "**現時点の既知の制限**\n\n* Kotlin の型は生成されますが、ARMOR-ANDROID-CONTROL は**まだ使っておらず**、独自の解析を持っています。\n* `set_thresholds` コマンドのフィールドは `sensitivity` 1 つだけです。実際のレーダーパラメータはファームウェアができるまで定義されません。\n* 共通ファームウェアを実機で動かしたのはレーダーノードのみで、他の 4 つは未実施です。\n* 第三者によるセキュリティレビューはありません。\n\n**今後**\n\n* Android アプリで生成された Kotlin の型を使う。\n* `set_thresholds` の実際のレーダーパラメータを定義する。\n* 他の 4 ノードの基板で共通ファームウェアを動かす。",
    "**当前已知限制**\n\n* Kotlin 类型已生成，但 ARMOR-ANDROID-CONTROL **尚未使用**，它仍保留自己的解析。\n* `set_thresholds` 命令只有一个 `sensitivity` 字段：真实的雷达参数要等固件存在后才会定义。\n* 只有雷达节点在开发板上运行过共用固件；其他四个没有。\n* 没有独立的安全审查。\n\n**下一步**\n\n* 让 Android 应用使用生成的 Kotlin 类型。\n* 定义 `set_thresholds` 的真实雷达参数。\n* 在其他四个节点的开发板上运行共用固件。",
    "**Limites conhecidos hoje**\n\n* Os tipos Kotlin são gerados mas **ainda não são usados** pelo ARMOR-ANDROID-CONTROL, que mantém a sua própria análise.\n* A ordem `set_thresholds` tem um único campo `sensitivity`: os parâmetros reais do radar só se definem quando o firmware existir.\n* Só o nó de radar executou o firmware partilhado numa placa; os outros quatro não.\n* Sem revisão de segurança independente.\n\n**A seguir**\n\n* Fazer a aplicação Android usar os tipos Kotlin gerados.\n* Definir os parâmetros reais do radar de `set_thresholds`.\n* Executar o firmware partilhado nas placas dos outros quatro nós.")

DOCS = [
    P("[Contracts](docs/CONTRACTS.md): every message, topic and the way to change a contract", "[Contratos](docs/CONTRACTS.md): cada mensaje, topic y cómo cambiar un contrato", "[Verträge](docs/CONTRACTS.md): jede Nachricht, jedes Topic und wie man einen Vertrag ändert",
      "[Contrats](docs/CONTRACTS.md) : chaque message, topic et la façon de changer un contrat", "[Contratti](docs/CONTRACTS.md): ogni messaggio, topic e come cambiare un contratto", "[契約](docs/CONTRACTS.md)：全メッセージ、トピック、契約の変更方法",
      "[契约](docs/CONTRACTS.md)：每条消息、主题以及如何修改契约", "[Contratos](docs/CONTRACTS.md): cada mensagem, tópico e como alterar um contrato"),
    P("[Firmware base](docs/FIRMWARE_BASE.md): what the five nodes share and how it is synced", "[Base de firmware](docs/FIRMWARE_BASE.md): lo que comparten los cinco nodos y cómo se sincroniza", "[Firmware-Basis](docs/FIRMWARE_BASE.md): was die fünf Knoten teilen und wie es abgeglichen wird",
      "[Base de firmware](docs/FIRMWARE_BASE.md) : ce que partagent les cinq nœuds et comment c'est synchronisé", "[Base firmware](docs/FIRMWARE_BASE.md): cosa condividono i cinque nodi e come si sincronizza", "[ファームウェア基盤](docs/FIRMWARE_BASE.md)：5 ノードの共有内容と同期の方法",
      "[固件基础](docs/FIRMWARE_BASE.md)：五个节点共用什么以及如何同步", "[Base de firmware](docs/FIRMWARE_BASE.md): o que os cinco nós partilham e como se sincroniza"),
    P("[Signed firmware](docs/SIGNED_FIRMWARE.md): the signature of releases and what it does not cover", "[Firmware firmado](docs/SIGNED_FIRMWARE.md): la firma de las versiones y lo que no cubre", "[Signierte Firmware](docs/SIGNED_FIRMWARE.md): die Signatur der Releases und was sie nicht abdeckt",
      "[Firmware signé](docs/SIGNED_FIRMWARE.md) : la signature des versions et ce qu'elle ne couvre pas", "[Firmware firmato](docs/SIGNED_FIRMWARE.md): la firma dei rilasci e cosa non copre", "[署名付きファームウェア](docs/SIGNED_FIRMWARE.md)：リリース署名と対象外のこと",
      "[签名固件](docs/SIGNED_FIRMWARE.md)：发布版本的签名及其不涵盖的内容", "[Firmware assinado](docs/SIGNED_FIRMWARE.md): a assinatura das versões e o que não cobre"),
    P("[Fuzzing](docs/FUZZING.md): the three parser targets and how to run them", "[Fuzzing](docs/FUZZING.md): los tres objetivos de análisis y cómo ejecutarlos", "[Fuzzing](docs/FUZZING.md): die drei Parser-Ziele und wie man sie ausführt",
      "[Fuzzing](docs/FUZZING.md) : les trois cibles d'analyse et comment les lancer", "[Fuzzing](docs/FUZZING.md): i tre target dei parser e come eseguirli", "[ファジング](docs/FUZZING.md)：3 つのパーサ対象と実行方法",
      "[模糊测试](docs/FUZZING.md)：三个解析目标及运行方法", "[Fuzzing](docs/FUZZING.md): os três alvos de análise e como os executar"),
    P("[Project manifest](docs/PROJECT_MANIFEST.md): the `armor.project.json` every repository carries", "[Manifiesto del proyecto](docs/PROJECT_MANIFEST.md): el `armor.project.json` de cada repositorio", "[Projekt-Manifest](docs/PROJECT_MANIFEST.md): die `armor.project.json` jedes Repositorys",
      "[Manifeste du projet](docs/PROJECT_MANIFEST.md) : le `armor.project.json` de chaque dépôt", "[Manifesto del progetto](docs/PROJECT_MANIFEST.md): il `armor.project.json` di ogni repository", "[プロジェクトマニフェスト](docs/PROJECT_MANIFEST.md)：各リポジトリの `armor.project.json`",
      "[项目清单](docs/PROJECT_MANIFEST.md)：每个仓库的 `armor.project.json`", "[Manifesto do projeto](docs/PROJECT_MANIFEST.md): o `armor.project.json` de cada repositório"),
    P("[The pictures of the READMEs](docs/README_PICTURES.md): how Architecture and Repository Structure are drawn", "[Las imágenes de los README](docs/README_PICTURES.md): cómo se dibujan Architecture y Repository Structure", "[Die Bilder der READMEs](docs/README_PICTURES.md): wie Architektur und Repository-Struktur gezeichnet werden",
      "[Les images des README](docs/README_PICTURES.md) : comment Architecture et Structure du dépôt sont dessinées", "[Le immagini dei README](docs/README_PICTURES.md): come si disegnano Architettura e Struttura del repository", "[README の図](docs/README_PICTURES.md)：アーキテクチャとリポジトリ構造の描き方",
      "[README 的图片](docs/README_PICTURES.md)：架构图和仓库结构图如何绘制", "[As imagens dos README](docs/README_PICTURES.md): como se desenham a Arquitetura e a Estrutura do repositório"),
]

OVERVIEW_HEAD = P("What it holds:", "Qué contiene:", "Was es enthält:", "Ce qu'il contient :", "Cosa contiene:", "収録内容：", "包含内容：", "O que contém:")


def build_lg(lg):
    bullets = "\n".join(f"* {b}" for b in L(lg, "bullets"))
    status = {k: fix(v) for k, v in LEGACY[lg]["status"].items()}
    body = {
        "overview": f"{L(lg, 'intro')}\n\n{bullets}",
        "role": f"{L(lg, 'fit')}\n\n{table(lg, 'talks', ROLE_TABLE)}",
        "architecture": arch(lg, "ARMOR-COMMON", "ARMOR-COMMON architecture: who uses it, what the repository owns (schemas, vectors, validator, generated types, OpenAPI, firmware base) and who receives it", DIAGRAM),
        "features": FEATURES[lg],
        "security": table(lg, "threat", SECURITY_ROWS) + "\n\n" + SECURITY_NOT[lg],
        "interfaces": TOPICS_INTRO[lg] + "\n\n" + table(lg, "topic", TOPICS) + "\n\n" + INTERFACES_SCHEMAS[lg] + "\n\n" + TOOLS_INTRO[lg] + "\n\n" + table(lg, "tool", TOOLS),
        "configuration": config_body(lg),
        "quickstart": f"{QUICK_LEAD[lg]}\n\n" + code(lg, QUICK_CODE) + "\n\n",
        "testing": code(lg, [("python -m unittest discover -s tests", T("237 tests | 237 pruebas | 237 Tests | 237 tests | 237 test | 237 件 | 237 项 | 237 testes")), "python -I tools/armor_ci_validate.py"]) + "\n\n" + table(lg, "tests", TEST_FILES) + "\n\n" + TEST_NOTE[lg],
        "build": BUILD[lg],
        "troubleshooting": table(lg, "trouble", TROUBLE),
        "structure": structure(lg, "ARMOR-COMMON", tree=TREE[lg]),
        "roadmap": ROADMAP[lg],
    }
    return text_for(lg, tagline=L(lg, "tagline"), honest=L(lg, "honest"), glance=GLANCE, status=status,
                    docs=DOCS, contributing_first=CONTRIB, body=body)


TEXT = {lg: build_lg(lg) for lg in LGS}
