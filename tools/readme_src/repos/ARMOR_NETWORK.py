# The facts that do not depend on the language, and the words of every language, of ARMOR-NETWORK, in the universal README layout.
# Copyright (C) 2026 JuanenRac (Electro Hobby 3D). GPL-3.0-or-later.
from readme_src._kit import *  # noqa: F401,F403

FACTS = {'emoji': '🛰️',
 'layout': 'universal',
 'license_badge': 'License-GPL%203.0--or--later-blue',
 'status': [['software', 'green'],
            ['tests', 'green'],
            ['protocols', 'yellow'],
            ['hardware', 'yellow'],
            ['security', 'yellow'],
            ['integration', 'yellow'],
            ['docs', 'green']],
 'badges': [['Language', 'Python%203.11%2B', '3776ab'], ['Dependencies', 'none', '2ea44f'], ['Tests', '187', '00E5FF']]}

# the sentences of the previous layout that the new one keeps (already written in the eight languages)
LEGACY = {'en': {'tagline': 'Watches the local network: the devices on it, whether the internet is there, what changes and what is new (a Python program with no dependencies; it '
                   'runs on a machine of the network and reports to ARMOR-SERVER)',
        'status': {'software': 'The scanner, the inventory that tells what changed, the internet check, the public-address look-up and the orders from Studio run as a '
                               'service on the CM5 test bench.',
                   'tests': '187 tests pass against a scripted network, and every message is accepted by the contract of ARMOR-COMMON.',
                   'protocols': 'What a device is (its kind, its system, its maker) is a guess, and nothing captures packets: traffic per device and intrusion detection '
                                'in the strict sense are not done.',
                   'hardware': 'It watches the real network of the CM5 test bench (a router, the phones and nodes of the house) but has not watched a whole house for '
                               'weeks.',
                   'security': 'It only asks the router and never configures it; the sealed logins are tested on the host, and there has been no independent review.',
                   'integration': 'Its messages reach the CM5 test bench server and Studio; the commands from Studio are tested against a scripted network.',
                   'docs': 'Eight languages and the changelog are up to date.'},
        'honest': 'The scanner, the inventory that tells what changed, the internet check, the public-address look-up, the orders from Studio and the sealed logins are '
                  "tested on a computer against a scripted network (187 tests; every message is accepted by ARMOR-COMMON's contract), and the program runs as a service "
                  'on the CM5 test bench, watching the real network the bench is on (a router, the phones and nodes of the house). It has not watched a whole house for '
                  'weeks, it only asks the router and never configures it, and what a device is (its kind, its system, its maker) is a guess. It does not capture '
                  "packets: it cannot see who talks to whom, and traffic per device and intrusion detection in the strict sense need the router's counters or a mirror "
                  'port, which is a later step.',
        'bullets': ['**What is on the network:** the neighbour table of the machine, a poke of every address so that it fills, an echo to each device found (latency and '
                    'TTL) and what devices announce about themselves (mDNS, UPnP, NetBIOS, reverse DNS). For each device: address, MAC, maker (from the IEEE register of '
                    '40,000 blocks), name, kind, system, open ports with what each says, and when it was first and last seen.',
                    '**Ports:** a TCP connection to 17 (or 44) ports of each device, twelve at a time, reading at most a few hundred bytes of what answers; never a '
                    'login, never an exploit. A new device is looked at at once, the others every quarter of an hour.',
                    '**What changes:** a device that appears (the first three sweeps only learn), goes quiet or comes back, changes its address, a port that opens or '
                    "closes, and two machines answering for one address (the router's above all). Every event has an id, so it is told once.",
                    '**The internet:** every few seconds an echo to the router, a TCP connection, two DNS questions to chosen resolvers and a web page. An outage takes '
                    'three rounds to be called one and two to be over, is dated from its first failed round and counted to the first good one, and says whose fault it '
                    "is: the provider's (the router answers and nothing beyond it does) or this side's (the router does not answer either). Latency, loss and the "
                    'outages of the last 24 hours.',
                    '**It only looks at your own network:** it refuses any address that is not private (10/8, 172.16/12, 192.168/16) and any range larger than a /22; a '
                    'skip list keeps it away from what is fragile; nothing is sent to a device that is not a question.',
                    '**The message** `armor/network/<node>/state`: the interface, the internet, every device and the latest events; it is in the shared contract (330 '
                    'vectors) and carries findings, never commands. `python -m armor_network scan` prints it as a table, `watch` tells ARMOR-SERVER, `demo` plays a '
                    'made-up house (a new device joins, a camera opens Telnet, the internet falls and comes back, someone answers for the router) without touching any '
                    'network.',
                    '**Where it shows:** the Network menu of ARMOR-STUDIO (the devices, the internet with its outages and latency, the traffic and the events; an '
                    "administrator names devices and marks the known ones, which quiets the alarm of a new device), the Network Designer (the drawing of the house's "
                    'network, compared with what was found, and able to draw it) and the Network screen of the Android app. ARMOR-SERVER raises the alarms.',
                    '**Orders from Studio:** a sweep now, a ping, a traceroute, a wake-up, the ports or the web page of one device and an inspection with a login you '
                    "give; orders arrive in the answer to the node's own message (never as a connection made to the node), each is checked before anything is done, and "
                    'nothing is run through a shell.',
                    '**Logins that stay safe:** the login of an inspection travels sealed for this node alone, is sent only over Digest or HTTPS (never Basic over plain '
                    'HTTP), only to the device whose HTTPS certificate was seen the first time, and is never echoed back.',
                    "**The public side:** the house's public address, who gives it and where it is (one HTTPS request to a fixed public service every few minutes; "
                    '`--no-public-info` turns it off). With `--dns-name` it also resolves the name the house is reached by from outside and says whether it points to '
                    'that address.',
                    '**A service:** it runs as a systemd unit on the CM5 test bench (written by hand, see the usage guide) and keeps its data in its own folder.',
                    "**Not yet:** the router's own counters (traffic per device), packet capture, controlling anything (blocking a device, closing a port, changing the "
                    'router) and weeks on a real network.'],
        'note': 'See the [usage](docs/USAGE.md) and the [design](docs/DESIGN.md).\n'
                '\n'
                'See the [design](docs/DESIGN.md), the [safety notes](docs/SAFETY.md), the [usage](docs/USAGE.md) and the [messages](docs/MESSAGES.md).',
        'hardware': 'Runs as a service on the CM5 test bench, watching its real network (a router, the phones and nodes of the house)',
        'fit': "ARMOR-NETWORK is the family's eye on the local network. It runs on a machine of the network (the CM5 on the bench), looks at what is there without "
               'touching it and reports to [ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER), which keeps the names, the hidden and watched devices and the '
               'outages; the *Network* menu and the *Network Designer* of [ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) and the Network screen of '
               '[ARMOR-ANDROID-CONTROL](https://github.com/JuanenRac/ARMOR-ANDROID-CONTROL) show it, and Studio can hand it orders. It never configures the router or '
               'any device.'},
 'es': {'tagline': 'Vigila la red local: los dispositivos que hay, si hay internet, qué cambia y qué es nuevo (un programa de Python sin dependencias; corre en una '
                   'máquina de la red e informa a ARMOR-SERVER)',
        'status': {'software': 'El escáner, el inventario que dice qué cambió, la comprobación de internet, la consulta de la dirección pública y las órdenes de Studio '
                               'funcionan como servicio en el banco de pruebas CM5.',
                   'tests': 'Pasan 187 pruebas contra una red guionizada, y cada mensaje lo acepta el contrato de ARMOR-COMMON.',
                   'protocols': 'Qué es un dispositivo (su tipo, su sistema, su fabricante) es una suposición, y nada captura paquetes: el tráfico por dispositivo y la '
                                'detección de intrusiones en sentido estricto no están hechos.',
                   'hardware': 'Vigila la red real del banco de pruebas CM5 (un router, los móviles y nodos de la casa) pero no ha vigilado una casa entera durante '
                               'semanas.',
                   'security': 'Solo pregunta al router y nunca lo configura; los accesos sellados están probados en el host y no ha habido una revisión independiente.',
                   'integration': 'Sus mensajes llegan al servidor del banco de pruebas CM5 y a Studio; las órdenes de Studio se prueban contra una red guionizada.',
                   'docs': 'Ocho idiomas y el historial de cambios están al día.'},
        'honest': 'El escáner, el inventario que dice qué cambió, la comprobación de internet, la consulta de la dirección pública, las órdenes desde Studio y los '
                  'accesos sellados se prueban en un ordenador contra una red guionizada (187 tests; cada mensaje lo acepta el contrato de ARMOR-COMMON), y el programa '
                  'corre como servicio en el banco de pruebas de la CM5, vigilando la red real en la que está el banco (un router, los móviles y los nodos de la casa). '
                  'No ha vigilado una casa entera durante semanas, solo pregunta al router y nunca lo configura, y qué es un dispositivo (su tipo, su sistema, su '
                  'fabricante) es una suposición. No captura paquetes: no puede ver quién habla con quién, y el tráfico por dispositivo y la detección de intrusos en '
                  'sentido estricto necesitan los contadores del router o un puerto espejo, que es un paso posterior.',
        'bullets': ['**Qué hay en la red:** la tabla de vecinos de la máquina, un toque a cada dirección para que se llene, un eco a cada dispositivo encontrado '
                    '(latencia y TTL) y lo que los dispositivos anuncian de sí mismos (mDNS, UPnP, NetBIOS, DNS inverso). De cada uno: dirección, MAC, fabricante (del '
                    'registro de la IEEE, 40.000 bloques), nombre, tipo, sistema, puertos abiertos con lo que dice cada uno y cuándo se vio por primera y por última '
                    'vez.',
                    '**Puertos:** una conexión TCP a 17 (o 44) puertos de cada dispositivo, de doce en doce, leyendo como mucho unos cientos de bytes de lo que '
                    'responde; nunca un inicio de sesión, nunca un exploit. Un dispositivo nuevo se mira enseguida, los demás cada cuarto de hora.',
                    '**Qué cambia:** un dispositivo que aparece (los tres primeros barridos solo aprenden), calla o vuelve, cambia de dirección, un puerto que se abre o '
                    'se cierra, y dos máquinas que responden por una misma dirección (sobre todo la del router). Cada evento tiene un id, así que se cuenta una vez.',
                    '**Internet:** cada pocos segundos un eco al router, una conexión TCP, dos preguntas DNS a resolvedores elegidos y una página web. Un corte necesita '
                    'tres rondas para llamarse así y dos para darse por terminado, se fecha desde su primera ronda fallida y se cuenta hasta la primera buena, y dice de '
                    'quién es la culpa: del operador (el router responde y nada más allá) o de este lado (el router tampoco responde). Latencia, pérdida y los cortes de '
                    'las últimas 24 horas.',
                    '**Solo mira tu propia red:** rechaza cualquier dirección que no sea privada (10/8, 172.16/12, 192.168/16) y cualquier rango mayor que un /22; una '
                    'lista de exclusión lo mantiene lejos de lo frágil; a un dispositivo no se le envía nada que no sea una pregunta.',
                    '**El mensaje** `armor/network/<nodo>/state`: la interfaz, internet, cada dispositivo y los últimos eventos; está en el contrato compartido (330 '
                    'vectores) y lleva hallazgos, nunca órdenes. `python -m armor_network scan` lo imprime como tabla, `watch` informa a ARMOR-SERVER y `demo` '
                    'representa una casa inventada (se une un dispositivo nuevo, una cámara abre Telnet, se cae internet y vuelve, alguien responde por el router) sin '
                    'tocar ninguna red.',
                    '**Dónde se ve:** el menú Red de ARMOR-STUDIO (los dispositivos, internet con sus cortes y su latencia, el tráfico y los eventos; un administrador '
                    'pone nombre a los dispositivos y marca los conocidos, que es lo que apaga la alarma de un dispositivo nuevo), el Diseñador de red (el dibujo de la '
                    'red de la casa, comparado con lo encontrado y capaz de dibujarlo) y la pantalla Red de la app Android. ARMOR-SERVER genera las alarmas.',
                    '**Órdenes desde Studio:** un barrido ya, un ping, un traceroute, una activación por red, los puertos o la página web de un dispositivo y una '
                    'inspección con un acceso que das; las órdenes llegan en la respuesta al propio mensaje del nodo (nunca como una conexión hecha al nodo), cada una '
                    'se comprueba antes de hacer nada y nada se ejecuta por un shell.',
                    '**Accesos que se mantienen seguros:** el acceso de una inspección viaja sellado solo para este nodo, se envía solo por Digest o HTTPS (nunca Basic '
                    'por HTTP plano), solo al dispositivo cuyo certificado HTTPS se vio la primera vez, y nunca se repite en la respuesta.',
                    '**El lado público:** la dirección pública de la casa, quién la da y dónde está (una petición HTTPS a un servicio público fijo cada pocos minutos; '
                    '`--no-public-info` la apaga). Con `--dns-name` resuelve además el nombre con el que se llega a la casa desde fuera y dice si apunta a esa '
                    'dirección.',
                    '**Un servicio:** corre como unidad systemd en el banco de pruebas de la CM5 (escrita a mano, véase la guía de uso) y guarda sus datos en su propia '
                    'carpeta.',
                    '**Todavía no:** los contadores del propio router (tráfico por dispositivo), la captura de paquetes, controlar nada (bloquear un dispositivo, cerrar '
                    'un puerto, cambiar el router) y semanas en una red real.'],
        'note': 'See the [usage](docs/USAGE.md) and the [design](docs/DESIGN.md).\n'
                '\n'
                'Véanse el [diseño](docs/DESIGN.md), las [notas de seguridad](docs/SAFETY.md), el [uso](docs/USAGE.md) y los [mensajes](docs/MESSAGES.md).',
        'hardware': 'Corre como servicio en el banco de pruebas de la CM5, vigilando su red real (un router, los móviles y los nodos de la casa)',
        'fit': 'ARMOR-NETWORK es el ojo de la familia sobre la red local. Corre en una máquina de la red (la CM5 en el banco), mira lo que hay sin tocarlo e informa a '
               '[ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER), que guarda los nombres, los dispositivos ocultos y vigilados y los cortes; el menú *Red* y el '
               '*Diseñador de red* de [ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) y la pantalla Red de '
               '[ARMOR-ANDROID-CONTROL](https://github.com/JuanenRac/ARMOR-ANDROID-CONTROL) lo muestran, y Studio puede darle órdenes. Nunca configura el router ni '
               'ningún dispositivo.',
        'requirements': ['Python 3.11+ (solo la biblioteca estándar)', 'una máquina de la red a vigilar (Linux, Windows o macOS)']},
 'fr': {'tagline': 'Surveille le réseau local : les appareils présents, si internet est là, ce qui change et ce qui est nouveau (un programme Python sans dépendances ; '
                   'il tourne sur une machine du réseau et rapporte à ARMOR-SERVER)',
        'status': {'software': "Le scanner, l'inventaire qui dit ce qui a changé, le contrôle d'internet, la recherche de l'adresse publique et les ordres de Studio "
                               "tournent comme service sur le banc d'essai CM5.",
                   'tests': "187 tests réussissent contre un réseau scénarisé, et chaque message est accepté par le contrat d'ARMOR-COMMON.",
                   'protocols': "Ce qu'est un appareil (son type, son système, son fabricant) est une supposition, et rien ne capture de paquets : le trafic par "
                                "appareil et la détection d'intrusion au sens strict ne sont pas faits.",
                   'hardware': "Il surveille le réseau réel du banc d'essai CM5 (un routeur, les téléphones et les nœuds de la maison) mais n'a pas surveillé une maison "
                               'entière pendant des semaines.',
                   'security': "Il ne fait qu'interroger le routeur et ne le configure jamais ; les identifiants scellés sont testés sur l'hôte et il n'y a pas eu de "
                               'revue indépendante.',
                   'integration': "Ses messages arrivent au serveur du banc d'essai CM5 et à Studio ; les ordres de Studio sont testés contre un réseau scénarisé.",
                   'docs': 'Huit langues et le journal des modifications sont à jour.'},
        'honest': "Le scanner, l'inventaire qui dit ce qui a changé, le contrôle d'internet, la recherche de l'adresse publique, les ordres depuis Studio et les "
                  "identifiants scellés sont testés sur un ordinateur contre un réseau scripté (187 tests ; chaque message est accepté par le contrat d'ARMOR-COMMON), "
                  'et le programme tourne comme service sur le banc de test CM5, en surveillant le vrai réseau où se trouve le banc (un routeur, les téléphones et les '
                  "nœuds de la maison). Il n'a pas surveillé une maison entière pendant des semaines, il ne fait que demander au routeur et ne le configure jamais, et "
                  "ce qu'est un appareil (son type, son système, son fabricant) est une supposition. Il ne capture pas de paquets : il ne voit pas qui parle à qui, et "
                  "le trafic par appareil et la détection d'intrusion au sens strict demandent les compteurs du routeur ou un port miroir, ce qui est une étape "
                  'ultérieure.',
        'bullets': ["**Ce qu'il y a sur le réseau :** la table de voisins de la machine, un coup sur chaque adresse pour qu'elle se remplisse, un écho à chaque appareil "
                    "trouvé (latence et TTL) et ce que les appareils annoncent d'eux-mêmes (mDNS, UPnP, NetBIOS, DNS inverse). Pour chacun : adresse, MAC, fabricant (du "
                    "registre de l'IEEE, 40 000 blocs), nom, type, système, ports ouverts avec ce que dit chacun, et quand il a été vu pour la première et la dernière "
                    'fois.',
                    "**Ports :** une connexion TCP à 17 (ou 44) ports de chaque appareil, douze à la fois, en lisant au plus quelques centaines d'octets de la réponse ; "
                    "jamais de connexion, jamais d'exploit. Un nouvel appareil est examiné aussitôt, les autres tous les quarts d'heure.",
                    "**Ce qui change :** un appareil qui apparaît (les trois premiers balayages ne font qu'apprendre), se tait ou revient, change d'adresse, un port qui "
                    "s'ouvre ou se ferme, et deux machines qui répondent pour une même adresse (surtout celle du routeur). Chaque événement a un id, il n'est donc dit "
                    "qu'une fois.",
                    '**Internet :** toutes les quelques secondes un écho au routeur, une connexion TCP, deux questions DNS à des résolveurs choisis et une page web. Une '
                    "coupure demande trois tours pour être déclarée et deux pour être finie, est datée du premier tour raté et comptée jusqu'au premier bon, et dit à "
                    'qui est la faute : au fournisseur (le routeur répond et rien au-delà) ou à ce côté-ci (le routeur ne répond pas non plus). Latence, perte et les '
                    'coupures des dernières 24 heures.',
                    "**Il ne regarde que votre propre réseau :** il refuse toute adresse non privée (10/8, 172.16/12, 192.168/16) et toute plage plus grande qu'un /22 ; "
                    "une liste d'exclusion le tient éloigné de ce qui est fragile ; rien n'est envoyé à un appareil qui ne soit une question.",
                    "**Le message** `armor/network/<nœud>/state` : l'interface, internet, chaque appareil et les derniers événements ; il est dans le contrat partagé "
                    "(330 vecteurs) et porte des constats, jamais des ordres. `python -m armor_network scan` l'imprime en tableau, `watch` informe ARMOR-SERVER, `demo` "
                    "joue une maison inventée (un nouvel appareil arrive, une caméra ouvre Telnet, internet tombe et revient, quelqu'un répond pour le routeur) sans "
                    'toucher aucun réseau.',
                    "**Où on le voit :** le menu Réseau d'ARMOR-STUDIO (les appareils, internet avec ses coupures et sa latence, le trafic et les événements ; un "
                    "administrateur nomme les appareils et marque les connus, ce qui apaise l'alarme d'un nouvel appareil), le Concepteur de réseau (le dessin du réseau "
                    "de la maison, comparé à ce qui a été trouvé et capable de le dessiner) et l'écran Réseau de l'app Android. ARMOR-SERVER déclenche les alarmes.",
                    "**Ordres depuis Studio :** un balayage tout de suite, un ping, un traceroute, un réveil réseau, les ports ou la page web d'un appareil et une "
                    'inspection avec un identifiant que vous donnez ; les ordres arrivent dans la réponse au propre message du nœud (jamais comme une connexion faite '
                    "vers le nœud), chacun est vérifié avant d'agir et rien n'est exécuté par un shell.",
                    "**Des identifiants qui restent sûrs :** l'identifiant d'une inspection voyage scellé pour ce seul nœud, n'est envoyé qu'en Digest ou HTTPS (jamais "
                    "Basic en HTTP clair), seulement à l'appareil dont le certificat HTTPS a été vu la première fois, et n'est jamais renvoyé en écho.",
                    "**Le côté public :** l'adresse publique de la maison, qui la donne et où elle se trouve (une requête HTTPS vers un service public fixe toutes les "
                    "quelques minutes ; `--no-public-info` la désactive). Avec `--dns-name`, il résout aussi le nom qui permet d'atteindre la maison depuis l'extérieur "
                    "et indique s'il pointe vers cette adresse.",
                    "**Un service :** il tourne comme unité systemd sur le banc de test CM5 (écrite à la main, voir le guide d'utilisation) et garde ses données dans "
                    'son propre dossier.',
                    '**Pas encore :** les compteurs du routeur lui-même (trafic par appareil), la capture de paquets, contrôler quoi que ce soit (bloquer un appareil, '
                    'fermer un port, changer le routeur) et des semaines sur un vrai réseau.'],
        'note': 'See the [usage](docs/USAGE.md) and the [design](docs/DESIGN.md).\n'
                '\n'
                "Voir la [conception](docs/DESIGN.md), les [notes de sécurité](docs/SAFETY.md), l'[usage](docs/USAGE.md) et les [messages](docs/MESSAGES.md).",
        'hardware': 'Tourne comme service sur le banc de test CM5, en surveillant son vrai réseau (un routeur, les téléphones et les nœuds de la maison)',
        'fit': "ARMOR-NETWORK est l'œil de la famille sur le réseau local. Il tourne sur une machine du réseau (la CM5 sur le banc), regarde ce qui s'y trouve sans y "
               'toucher et rapporte à [ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER), qui garde les noms, les appareils masqués et surveillés et les coupures '
               "; le menu *Réseau* et le *Concepteur réseau* d'[ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) et l'écran Réseau "
               "d'[ARMOR-ANDROID-CONTROL](https://github.com/JuanenRac/ARMOR-ANDROID-CONTROL) le montrent, et Studio peut lui donner des ordres. Il ne configure jamais "
               'le routeur ni aucun appareil.',
        'requirements': ['Python 3.11+ (bibliothèque standard uniquement)', 'une machine du réseau à surveiller (Linux, Windows ou macOS)']},
 'it': {'tagline': "Sorveglia la rete locale: i dispositivi presenti, se internet c'è, cosa cambia e cosa è nuovo (un programma Python senza dipendenze; gira su una "
                   'macchina della rete e riferisce ad ARMOR-SERVER)',
        'status': {'software': "Lo scanner, l'inventario che dice cosa è cambiato, il controllo di internet, la ricerca dell'indirizzo pubblico e gli ordini di Studio "
                               'girano come servizio sul banco di prova CM5.',
                   'tests': 'Superano 187 test contro una rete simulata da script, e ogni messaggio è accettato dal contratto di ARMOR-COMMON.',
                   'protocols': "Cosa sia un dispositivo (tipo, sistema, produttore) è un'ipotesi, e nulla cattura pacchetti: il traffico per dispositivo e il "
                                'rilevamento di intrusioni in senso stretto non sono fatti.',
                   'hardware': "Sorveglia la rete reale del banco di prova CM5 (un router, i telefoni e i nodi di casa) ma non ha sorvegliato un'intera casa per "
                               'settimane.',
                   'security': "Interroga soltanto il router e non lo configura mai; gli accessi sigillati sono testati sull'host e non c'è stata una revisione "
                               'indipendente.',
                   'integration': 'I suoi messaggi arrivano al server del banco di prova CM5 e a Studio; gli ordini di Studio sono provati contro una rete simulata da '
                                  'script.',
                   'docs': 'Otto lingue e il registro delle modifiche sono aggiornati.'},
        'honest': "Lo scanner, l'inventario che dice cosa è cambiato, il controllo di internet, la ricerca dell'indirizzo pubblico, gli ordini da Studio e gli accessi "
                  'sigillati sono provati su un computer contro una rete scriptata (187 test; ogni messaggio è accettato dal contratto di ARMOR-COMMON), e il programma '
                  'gira come servizio sul banco di prova CM5, sorvegliando la rete reale su cui si trova il banco (un router, i telefoni e i nodi della casa). Non ha '
                  'sorvegliato una casa intera per settimane, chiede solo al router e non lo configura mai, e cosa sia un dispositivo (il tipo, il sistema, il '
                  'produttore) è una supposizione. Non cattura pacchetti: non può vedere chi parla con chi, e il traffico per dispositivo e il rilevamento delle '
                  'intrusioni in senso stretto richiedono i contatori del router o una porta mirror, che è un passo successivo.',
        'bullets': ["**Cosa c'è in rete:** la tabella dei vicini della macchina, un tocco a ogni indirizzo perché si riempia, un'eco a ogni dispositivo trovato (latenza "
                    'e TTL) e ciò che i dispositivi annunciano di sé (mDNS, UPnP, NetBIOS, DNS inverso). Per ciascuno: indirizzo, MAC, produttore (dal registro IEEE, '
                    "40.000 blocchi), nome, tipo, sistema, porte aperte con ciò che dice ognuna e quando è stato visto la prima e l'ultima volta.",
                    '**Porte:** una connessione TCP a 17 (o 44) porte di ogni dispositivo, dodici alla volta, leggendo al più poche centinaia di byte della risposta; '
                    "mai un accesso, mai un exploit. Un dispositivo nuovo si guarda subito, gli altri ogni quarto d'ora.",
                    '**Cosa cambia:** un dispositivo che compare (le prime tre scansioni imparano soltanto), tace o torna, cambia indirizzo, una porta che si apre o si '
                    'chiude, e due macchine che rispondono per lo stesso indirizzo (soprattutto quello del router). Ogni evento ha un id, quindi si dice una volta sola.',
                    "**Internet:** ogni pochi secondi un'eco al router, una connessione TCP, due domande DNS a risolutori scelti e una pagina web. Un'interruzione "
                    'richiede tre giri per chiamarsi così e due per dirsi finita, si data dal primo giro fallito e si conta fino al primo buono, e dice di chi è la '
                    'colpa: del gestore (il router risponde e nulla oltre) o di questa parte (anche il router non risponde). Latenza, perdita e le interruzioni delle '
                    'ultime 24 ore.',
                    '**Guarda solo la tua rete:** rifiuta ogni indirizzo non privato (10/8, 172.16/12, 192.168/16) e ogni intervallo più grande di un /22; un elenco di '
                    'esclusione lo tiene lontano da ciò che è fragile; a un dispositivo non si invia nulla che non sia una domanda.',
                    "**Il messaggio** `armor/network/<nodo>/state`: l'interfaccia, internet, ogni dispositivo e gli ultimi eventi; è nel contratto condiviso (330 "
                    'vettori) e porta rilevazioni, mai comandi. `python -m armor_network scan` lo stampa come tabella, `watch` informa ARMOR-SERVER, `demo` recita una '
                    'casa inventata (si unisce un dispositivo nuovo, una telecamera apre Telnet, internet cade e torna, qualcuno risponde per il router) senza toccare '
                    'alcuna rete.',
                    '**Dove si vede:** il menu Rete di ARMOR-STUDIO (i dispositivi, internet con le sue interruzioni e la latenza, il traffico e gli eventi; un '
                    "amministratore dà un nome ai dispositivi e segna quelli noti, ciò che spegne l'allarme di un dispositivo nuovo), il Progettista di rete (il disegno "
                    "della rete di casa, confrontato con ciò che è stato trovato e capace di disegnarlo) e la schermata Rete dell'app Android. ARMOR-SERVER genera gli "
                    'allarmi.',
                    "**Ordini da Studio:** una scansione subito, un ping, un traceroute, un wake-up, le porte o la pagina web di un dispositivo e un'ispezione con un "
                    'accesso che dai; gli ordini arrivano nella risposta al messaggio del nodo stesso (mai come una connessione fatta verso il nodo), ognuno è '
                    'controllato prima di fare qualcosa e nulla è eseguito tramite una shell.',
                    "**Accessi che restano sicuri:** l'accesso di un'ispezione viaggia sigillato per questo solo nodo, è inviato solo via Digest o HTTPS (mai Basic su "
                    'HTTP in chiaro), solo al dispositivo il cui certificato HTTPS è stato visto la prima volta, e non è mai rimandato in eco.',
                    "**Il lato pubblico:** l'indirizzo pubblico della casa, chi lo dà e dove si trova (una richiesta HTTPS a un servizio pubblico fisso ogni pochi "
                    "minuti; `--no-public-info` la spegne). Con `--dns-name` risolve anche il nome con cui si raggiunge la casa dall'esterno e dice se punta a "
                    "quell'indirizzo.",
                    "**Un servizio:** gira come unità systemd sul banco di prova CM5 (scritta a mano, vedi la guida all'uso) e tiene i suoi dati nella propria cartella.",
                    '**Non ancora:** i contatori del router stesso (traffico per dispositivo), la cattura dei pacchetti, controllare qualcosa (bloccare un dispositivo, '
                    'chiudere una porta, cambiare il router) e settimane su una rete reale.'],
        'note': 'See the [usage](docs/USAGE.md) and the [design](docs/DESIGN.md).\n'
                '\n'
                "Vedi il [progetto](docs/DESIGN.md), le [note di sicurezza](docs/SAFETY.md), l'[uso](docs/USAGE.md) e i [messaggi](docs/MESSAGES.md).",
        'hardware': 'Gira come servizio sul banco di prova CM5, sorvegliando la sua rete reale (un router, i telefoni e i nodi della casa)',
        'fit': "ARMOR-NETWORK è l'occhio della famiglia sulla rete locale. Gira su una macchina della rete (la CM5 sul banco), guarda cosa c'è senza toccarlo e "
               'riferisce ad [ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER), che conserva i nomi, i dispositivi nascosti e sorvegliati e le interruzioni; il '
               'menu *Rete* e il *Progettista di rete* di [ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) e la schermata Rete di '
               '[ARMOR-ANDROID-CONTROL](https://github.com/JuanenRac/ARMOR-ANDROID-CONTROL) lo mostrano, e Studio può dargli ordini. Non configura mai il router né '
               'alcun dispositivo.',
        'requirements': ['Python 3.11+ (solo la libreria standard)', 'una macchina della rete da sorvegliare (Linux, Windows o macOS)']},
 'de': {'tagline': 'Beobachtet das lokale Netz: die Geräte darin, ob das Internet da ist, was sich ändert und was neu ist (ein Python-Programm ohne Abhängigkeiten; es '
                   'läuft auf einem Rechner des Netzes und meldet an ARMOR-SERVER)',
        'status': {'software': 'Der Scanner, das Inventar, das sagt, was sich geändert hat, die Internetprüfung, die Abfrage der öffentlichen Adresse und die Befehle '
                               'von Studio laufen als Dienst auf dem CM5-Prüfstand.',
                   'tests': '187 Tests bestehen gegen ein geskriptetes Netz, und jede Nachricht wird vom Vertrag von ARMOR-COMMON akzeptiert.',
                   'protocols': 'Was ein Gerät ist (Art, System, Hersteller), ist eine Vermutung, und nichts fängt Pakete ab: Verkehr pro Gerät und Einbruchserkennung '
                                'im strengen Sinn gibt es nicht.',
                   'hardware': 'Er überwacht das echte Netz des CM5-Prüfstands (ein Router, die Telefone und Knoten des Hauses), hat aber noch nie wochenlang ein ganzes '
                               'Haus überwacht.',
                   'security': 'Er fragt den Router nur ab und konfiguriert ihn nie; die versiegelten Zugangsdaten sind auf dem Host getestet, und es gab keine '
                               'unabhängige Prüfung.',
                   'integration': 'Seine Nachrichten erreichen den Server des CM5-Prüfstands und Studio; die Befehle von Studio sind gegen ein geskriptetes Netz '
                                  'getestet.',
                   'docs': 'Acht Sprachen und das Änderungsprotokoll sind aktuell.'},
        'honest': 'Der Scanner, das Inventar, das sagt, was sich geändert hat, die Internetprüfung, die Abfrage der öffentlichen Adresse, die Aufträge aus Studio und '
                  'die versiegelten Logins werden auf einem Computer gegen ein geskriptetes Netz getestet (187 Tests; jede Nachricht wird vom Vertrag von ARMOR-COMMON '
                  'akzeptiert), und das Programm läuft als Dienst am CM5-Testaufbau und beobachtet das echte Netz, in dem der Aufbau steht (ein Router, die Telefone und '
                  'Knoten des Hauses). Es hat noch kein ganzes Haus wochenlang beobachtet, es fragt nur den Router und konfiguriert ihn nie, und was ein Gerät ist (Art, '
                  'System, Hersteller), ist eine Vermutung. Es fängt keine Pakete ab: Es sieht nicht, wer mit wem spricht, und Verkehr pro Gerät und Einbruchserkennung '
                  'im strengen Sinn brauchen die Zähler des Routers oder einen Mirror-Port, was ein späterer Schritt ist.',
        'bullets': ['**Was im Netzwerk ist:** die Nachbartabelle des Rechners, ein Anstupsen jeder Adresse, damit sie sich füllt, ein Echo an jedes gefundene Gerät '
                    '(Latenz und TTL) und was Geräte über sich selbst ankündigen (mDNS, UPnP, NetBIOS, Reverse-DNS). Je Gerät: Adresse, MAC, Hersteller (aus dem '
                    'IEEE-Register mit 40.000 Blöcken), Name, Art, System, offene Ports mit dem, was jeder sagt, und wann es zuerst und zuletzt gesehen wurde.',
                    '**Ports:** eine TCP-Verbindung zu 17 (oder 44) Ports je Gerät, zwölf gleichzeitig, mit höchstens einigen hundert gelesenen Bytes der Antwort; nie '
                    'ein Login, nie ein Exploit. Ein neues Gerät wird sofort angesehen, die anderen alle Viertelstunde.',
                    '**Was sich ändert:** ein Gerät, das auftaucht (die ersten drei Scans lernen nur), verstummt oder zurückkommt, seine Adresse ändert, ein Port, der '
                    'sich öffnet oder schließt, und zwei Rechner, die für eine Adresse antworten (vor allem die des Routers). Jedes Ereignis hat eine ID und wird daher '
                    'nur einmal gemeldet.',
                    '**Das Internet:** alle paar Sekunden ein Echo an den Router, eine TCP-Verbindung, zwei DNS-Fragen an gewählte Resolver und eine Webseite. Ein '
                    'Ausfall braucht drei Runden, um so zu heißen, und zwei, um beendet zu sein, wird ab der ersten fehlgeschlagenen Runde datiert und bis zur ersten '
                    'guten gezählt und sagt, wessen Schuld es ist: die des Anbieters (der Router antwortet, dahinter nichts) oder die dieser Seite (auch der Router '
                    'antwortet nicht). Latenz, Verlust und die Ausfälle der letzten 24 Stunden.',
                    '**Es sieht nur Ihr eigenes Netzwerk:** es verweigert jede nicht private Adresse (10/8, 172.16/12, 192.168/16) und jeden Bereich über /22; eine '
                    'Ausschlussliste hält es von Empfindlichem fern; an ein Gerät wird nichts gesendet, was keine Frage ist.',
                    '**Die Nachricht** `armor/network/<Knoten>/state`: die Schnittstelle, das Internet, jedes Gerät und die letzten Ereignisse; sie steht im gemeinsamen '
                    'Vertrag (330 Vektoren) und trägt Befunde, nie Befehle. `python -m armor_network scan` druckt sie als Tabelle, `watch` meldet an ARMOR-SERVER, '
                    '`demo` spielt ein erfundenes Haus (ein neues Gerät kommt hinzu, eine Kamera öffnet Telnet, das Internet fällt aus und kommt zurück, jemand '
                    'antwortet für den Router) ohne ein Netzwerk zu berühren.',
                    '**Wo man es sieht:** das Netzwerk-Menü von ARMOR-STUDIO (die Geräte, das Internet mit Ausfällen und Latenz, der Datenverkehr und die Ereignisse; '
                    'ein Administrator benennt Geräte und markiert bekannte, was den Alarm eines neuen Geräts beruhigt), der Netzwerkplaner (die Zeichnung des '
                    'Hausnetzwerks, verglichen mit dem Gefundenen und fähig, es zu zeichnen) und der Netzwerk-Bildschirm der Android-App. ARMOR-SERVER löst die Alarme '
                    'aus.',
                    '**Aufträge aus Studio:** sofort ein Scan, ein Ping, ein Traceroute, ein Aufwecken, die Ports oder die Webseite eines Geräts und eine Prüfung mit '
                    'einem von Ihnen gegebenen Login; Aufträge kommen in der Antwort auf die eigene Nachricht des Knotens an (nie als Verbindung zum Knoten), jeder wird '
                    'geprüft, bevor etwas geschieht, und nichts läuft über eine Shell.',
                    '**Logins, die sicher bleiben:** der Login einer Prüfung reist nur für diesen Knoten versiegelt, wird nur per Digest oder HTTPS gesendet (nie Basic '
                    'über Klartext-HTTP), nur an das Gerät, dessen HTTPS-Zertifikat beim ersten Mal gesehen wurde, und nie zurückgespiegelt.',
                    '**Die öffentliche Seite:** die öffentliche Adresse des Hauses, wer sie liefert und wo sie liegt (alle paar Minuten eine HTTPS-Anfrage an einen '
                    'festen öffentlichen Dienst; `--no-public-info` schaltet sie ab). Mit `--dns-name` löst er außerdem den Namen auf, unter dem das Haus von außen '
                    'erreichbar ist, und meldet, ob er auf diese Adresse zeigt.',
                    '**Ein Dienst:** er läuft als systemd-Einheit am CM5-Testaufbau (von Hand geschrieben, siehe die Anleitung) und hält seine Daten in einem eigenen '
                    'Ordner.',
                    '**Noch nicht:** die Zähler des Routers selbst (Verkehr je Gerät), Paketmitschnitt, irgendetwas steuern (ein Gerät sperren, einen Port schließen, '
                    'den Router ändern) und Wochen in einem echten Netzwerk.'],
        'note': 'See the [usage](docs/USAGE.md) and the [design](docs/DESIGN.md).\n'
                '\n'
                'Siehe den [Entwurf](docs/DESIGN.md), die [Sicherheitshinweise](docs/SAFETY.md), die [Benutzung](docs/USAGE.md) und die [Nachrichten](docs/MESSAGES.md).',
        'hardware': 'Läuft als Dienst am CM5-Testaufbau und beobachtet sein echtes Netz (einen Router, die Telefone und Knoten des Hauses)',
        'fit': 'ARMOR-NETWORK ist das Auge der Familie auf das lokale Netz. Es läuft auf einem Rechner des Netzes (der CM5 am Aufbau), sieht an, was da ist, ohne es zu '
               'berühren, und meldet an [ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER), der Namen, versteckte und beobachtete Geräte und Ausfälle führt; das '
               'Menü *Netzwerk* und der *Netzwerk-Designer* von [ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) sowie der Netzwerk-Bildschirm von '
               '[ARMOR-ANDROID-CONTROL](https://github.com/JuanenRac/ARMOR-ANDROID-CONTROL) zeigen es, und Studio kann ihm Aufträge geben. Es konfiguriert nie den '
               'Router oder ein Gerät.',
        'requirements': ['Python 3.11+ (nur die Standardbibliothek)', 'ein zu überwachender Rechner im Netz (Linux, Windows oder macOS)']},
 'zh': {'tagline': '监视本地网络：上面有哪些设备、互联网是否可用、哪些发生了变化、哪些是新的（无依赖的 Python 程序；在网络中的一台机器上运行并向 ARMOR-SERVER 报告）',
        'status': {'software': '扫描器、记录变化的清单、互联网检查、公网地址查询和来自 Studio 的指令在 CM5 测试台上作为服务运行。',
                   'tests': '187 项测试针对脚本化网络通过，每条消息都被 ARMOR-COMMON 的契约接受。',
                   'protocols': '设备是什么（类型、系统、厂商）只是猜测，也不抓包：按设备统计流量和严格意义上的入侵检测尚未实现。',
                   'hardware': '它监视 CM5 测试台所在的真实网络（一台路由器以及家里的手机和节点），但还没有连续数周监视整栋房子。',
                   'security': '它只查询路由器，从不配置路由器；密封的登录信息已在主机上测试，没有经过独立审查。',
                   'integration': '它的消息送达 CM5 测试台的服务器和 Studio；来自 Studio 的指令已对照脚本化网络测试。',
                   'docs': '八种语言和更新日志均为最新。'},
        'honest': '扫描器、说明发生了什么变化的清单、互联网检查、公网地址查询、来自 Studio 的指令和加密封装的登录信息，都在计算机上对照脚本化网络测试（187 个测试；每条消息都被 ARMOR-COMMON 的契约接受），程序在 CM5 '
                  '测试台上作为服务运行，监视测试台所在的真实网络（一台路由器、住宅的手机和节点）。它还没有连续数周监视整个住宅，只询问路由器而从不配置它，设备是什么（类型、系统、厂商）只是猜测。它不抓包：看不到谁与谁通信，每个设备的流量和严格意义上的入侵检测需要路由器的计数器或镜像端口，那是以后的一步。',
        'bullets': ['**网络上有什么：** 本机的邻居表、为填充它而对每个地址的试探、对每个发现的设备的回显（延迟与 TTL），以及设备对自身的宣告（mDNS、UPnP、NetBIOS、反向 DNS）。每台设备：地址、MAC、厂商（来自 IEEE 的 40,000 '
                    '个块的登记表）、名称、类型、系统、开放端口及各自的应答内容，以及首次和最近一次看到的时间。',
                    '**端口：** 对每台设备的 17（或 44）个端口进行 TCP 连接，每次十二个，最多只读取应答的几百字节；从不登录，从不利用漏洞。新设备立即检查，其余每刻钟一次。',
                    '**变化：** 设备出现（前三次扫描只学习）、沉默或恢复、更改地址、端口打开或关闭，以及两台机器响应同一个地址（尤其是路由器的地址）。每个事件都有 id，因此只通报一次。',
                    '**互联网：** 每隔几秒对路由器回显、一次 TCP 连接、向选定解析器发出两个 DNS 问题以及一个网页。三轮才算中断、两轮才算结束，从第一轮失败起算、数到第一轮成功，并指出是谁的问题：运营商一侧（路由器有响应而其后没有）还是本地一侧（路由器也没有响应）。延迟、丢包和最近 24 小时的中断。',
                    '**只查看您自己的网络：** 拒绝任何非私有地址（10/8、172.16/12、192.168/16 之外）和大于 /22 的范围；排除列表让它远离脆弱的设备；不会向设备发送任何不是提问的内容。',
                    '**消息** `armor/network/<节点>/state`：接口、互联网、每台设备和最新事件；它在共享契约中（330 个向量），只携带发现，绝不携带命令。`python -m armor_network scan` 以表格打印，`watch` 通知 '
                    'ARMOR-SERVER，`demo` 演示一栋虚构的房子（新设备加入、摄像头打开 Telnet、互联网中断又恢复、有人冒充路由器应答），不触碰任何网络。',
                    '**在哪里显示：** ARMOR-STUDIO 的网络菜单（设备、带中断和延迟的互联网、流量和事件；管理员为设备命名并标记已知设备，这会平息新设备的警报）、网络设计器（家中网络的图纸，与发现的内容对比并能自动绘制）以及 Android 应用的网络界面。警报由 ARMOR-SERVER 发出。',
                    '**来自 Studio 的指令：**立即扫描、ping、traceroute、网络唤醒、某个设备的端口或网页，以及用你提供的登录信息进行检查；指令在对节点自身消息的应答中到达（绝不是向节点发起连接），每条在执行前都要检查，也不通过 shell 运行任何东西。',
                    '**始终安全的登录信息：**检查所用的登录信息仅为该节点加密封装后传输，只通过 Digest 或 HTTPS 发送（绝不通过明文 HTTP 的 Basic），只发给首次见到其 HTTPS 证书的设备，并且从不回显。',
                    '**公网一侧：**住宅的公网地址、提供者及其位置（每隔几分钟向一个固定的公共服务发一次 HTTPS 请求；`--no-public-info` 可关闭）。使用 `--dns-name` 时，还会解析从外部访问住宅所用的域名，并说明它是否指向该地址。',
                    '**一项服务：**它作为 systemd 单元在 CM5 测试台上运行（手写，见使用指南），数据保存在自己的文件夹中。',
                    '**尚未：** 路由器自身的计数器（按设备统计流量）、抓包、控制任何东西（封锁设备、关闭端口、修改路由器）以及在真实网络上运行数周。'],
        'note': 'See the [usage](docs/USAGE.md) and the [design](docs/DESIGN.md).\n'
                '\n'
                '参见[设计](docs/DESIGN.md)、[安全说明](docs/SAFETY.md)、[使用](docs/USAGE.md)和[消息](docs/MESSAGES.md)。',
        'hardware': '在 CM5 测试台上作为服务运行，监视其真实网络（路由器、住宅的手机和节点）',
        'fit': 'ARMOR-NETWORK 是家族观察本地网络的眼睛。它运行在网络中的一台机器上（测试台上的 CM5），只看不碰，并向 [ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER) '
               '报告，由后者保存名称、隐藏和监视的设备以及中断记录；[ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) 的*网络*菜单和*网络设计器*以及 '
               '[ARMOR-ANDROID-CONTROL](https://github.com/JuanenRac/ARMOR-ANDROID-CONTROL) 的网络界面显示这些内容，Studio 还可以给它下达指令。它从不配置路由器或任何设备。',
        'requirements': ['Python 3.11+（仅标准库）', '网络上需要监控的机器（Linux、Windows 或 macOS）']},
 'ja': {'tagline': 'ローカルネットワークを見張ります：接続されているデバイス、インターネットがあるか、何が変わり何が新しいか（依存ライブラリなしの Python プログラム。ネットワーク上のマシンで動き、ARMOR-SERVER に報告）',
        'status': {'software': 'スキャナー、変更点を示すインベントリ、インターネット確認、公開アドレスの取得、Studio からの命令は、CM5 テストベンチ上でサービスとして動いています。',
                   'tests': '187 件のテストがスクリプト化したネットワークに対して通り、すべてのメッセージが ARMOR-COMMON の契約に受理されます。',
                   'protocols': '機器の種類・システム・メーカーは推測で、パケットは取得しません。機器ごとのトラフィックと厳密な意味での侵入検知は未実装です。',
                   'hardware': 'CM5 テストベンチの実際のネットワーク（ルーター、家の電話機とノード）を監視していますが、家全体を数週間監視したことはありません。',
                   'security': 'ルーターに問い合わせるだけで設定は一切しません。封印されたログイン情報はホストでテスト済みで、独立したレビューはありません。',
                   'integration': 'メッセージは CM5 テストベンチのサーバーと Studio に届きます。Studio からの命令はスクリプト化したネットワークに対してテストしています。',
                   'docs': '8 言語と変更履歴は最新です。'},
        'honest': 'スキャナー、何が変わったかを伝えるインベントリ、インターネットの検査、公開アドレスの問い合わせ、Studio からの指示、封印されたログインは、スクリプト化したネットワークに対してコンピューター上でテストされ（187 件。すべてのメッセージが ARMOR-COMMON '
                  'のコントラクトに受け付けられる）、プログラムは CM5 '
                  'テストベンチ上でサービスとして動き、ベンチがつながる実際のネットワーク（ルーター、家のスマートフォンとノード）を見張っています。家全体を数週間見張ったことはなく、ルーターに尋ねるだけで設定は一切せず、デバイスが何か（種類、システム、メーカー）は推測です。パケットは取得しません。誰が誰と話しているかは見えず、デバイスごとのトラフィックや厳密な意味での侵入検知にはルーターのカウンターかミラーポートが必要で、それは今後の段階です。',
        'bullets': ['**ネットワーク上にあるもの：** マシンの近隣テーブル、それを満たすための各アドレスへの呼びかけ、見つかった各機器へのエコー（遅延と TTL）、機器自身の告知（mDNS、UPnP、NetBIOS、逆引き DNS）。機器ごとに、アドレス、MAC、メーカー（IEEE の 40,000 '
                    'ブロックの登録簿から）、名前、種類、OS、開いているポートとその応答内容、初回と最終の確認時刻を持ちます。',
                    '**ポート：** 各機器の 17（または 44）ポートに TCP 接続を 12 本ずつ行い、応答は数百バイトまでしか読みません。ログインも攻撃も行いません。新しい機器はすぐに、他は 15 分ごとに調べます。',
                    '**変化：** 機器の出現（最初の 3 回のスキャンは学習のみ）、沈黙、復帰、アドレスの変更、ポートの開閉、1 つのアドレスに 2 台が応答（特にルーターのアドレス）。各イベントには ID があり、一度だけ通知されます。',
                    '**インターネット：** 数秒ごとにルーターへのエコー、TCP 接続、選んだリゾルバーへの DNS 問い合わせ 2 件、ウェブページ 1 件。停止と判定するには 3 回、復旧と判定するには 2 '
                    '回の連続が必要で、最初の失敗の回から起算し最初の成功の回まで数え、原因がどちら側かも示します：プロバイダー側（ルーターは応答し、その先は応答しない）か、こちら側（ルーターも応答しない）。遅延、損失、過去 24 時間の停止。',
                    '**自分のネットワークだけを見ます：** プライベートでないアドレス（10/8、172.16/12、192.168/16 以外）と /22 より大きい範囲は拒否します。除外リストでデリケートな機器には触れず、機器には質問以外を送りません。',
                    '**メッセージ** `armor/network/<ノード>/state`：インターフェース、インターネット、全機器、最新のイベント。共有コントラクト（330 ベクター）にあり、発見だけを運び、命令は運びません。`python -m armor_network scan` '
                    'は表で表示、`watch` は ARMOR-SERVER に通知、`demo` は架空の家（新しい機器の参加、カメラが Telnet を開く、インターネットの断と復旧、ルーターになりすます応答）を、ネットワークに触れずに再生します。',
                    '**表示場所：** ARMOR-STUDIO '
                    'のネットワークメニュー（機器、停止と遅延のあるインターネット、トラフィック、イベント。管理者が機器に名前を付け既知として印を付けると、新しい機器の警報が静まります）、ネットワーク設計（家のネットワークの図面を、検出結果と比較し、描くこともできます）、Android '
                    'アプリのネットワーク画面。警報は ARMOR-SERVER が発します。',
                    '**Studio からの指示：**今すぐのスキャン、ping、traceroute、ウェイクアップ、1 台のデバイスのポートや Web '
                    'ページ、あなたが渡したログインでの検査。指示はノード自身のメッセージへの応答として届き（ノードへの接続としては決して来ません）、実行前にそれぞれ検査され、シェルを通して何かを実行することはありません。',
                    '**安全なままのログイン：**検査のログインはそのノードだけに封印されて届き、Digest または HTTPS でのみ送られ（平文 HTTP の Basic は決して使わない）、最初に HTTPS 証明書を見たデバイスにだけ送られ、エコーバックされません。',
                    '**公開側：**家の公開アドレス、その提供元と場所（数分ごとに固定の公開サービスへ HTTPS リクエストを 1 回。`--no-public-info` でオフ）。`--dns-name` を使うと、外から家に接続するための名前も解決し、そのアドレスを指しているかどうかを伝えます。',
                    '**サービス：**CM5 テストベンチで systemd ユニットとして動き（手書き、使い方ガイドを参照）、データは専用のフォルダーに保存します。',
                    '**まだ：** ルーター自身のカウンター（機器ごとのトラフィック）、パケットキャプチャ、何かを制御すること（機器のブロック、ポートを閉じる、ルーターの変更）、実ネットワークでの数週間の運用。'],
        'note': 'See the [usage](docs/USAGE.md) and the [design](docs/DESIGN.md).\n'
                '\n'
                '[設計](docs/DESIGN.md)、[安全性のメモ](docs/SAFETY.md)、[使い方](docs/USAGE.md)、[メッセージ](docs/MESSAGES.md)を参照してください。',
        'hardware': 'CM5 テストベンチ上でサービスとして動き、実際のネットワーク（ルーター、家のスマートフォンとノード）を見張っています',
        'fit': 'ARMOR-NETWORK はファミリーのローカルネットワークを見る目です。ネットワーク上のマシン（ベンチの CM5）で動き、そこにあるものに触れずに見て、[ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER) '
               'に報告します。サーバーが名前、非表示・監視デバイス、停止を保持し、[ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) '
               'の*ネットワーク*メニューと*ネットワークデザイナー*、[ARMOR-ANDROID-CONTROL](https://github.com/JuanenRac/ARMOR-ANDROID-CONTROL) のネットワーク画面が表示し、Studio '
               'から指示も出せます。ルーターやデバイスを設定することはありません。',
        'requirements': ['Python 3.11+（標準ライブラリのみ）', '監視対象のネットワーク上のマシン（Linux、Windows、macOS）']},
 'pt': {'tagline': 'Vigia a rede local: os dispositivos que nela estão, se há internet, o que muda e o que é novo (um programa Python sem dependências; corre numa '
                   'máquina da rede e reporta ao ARMOR-SERVER)',
        'status': {'software': 'O leitor da rede, o inventário que diz o que mudou, a verificação da internet, a consulta do endereço público e as ordens do Studio '
                               'funcionam como serviço na bancada de testes CM5.',
                   'tests': 'Passam 187 testes contra uma rede com guião, e cada mensagem é aceite pelo contrato do ARMOR-COMMON.',
                   'protocols': 'O que um dispositivo é (o tipo, o sistema, o fabricante) é um palpite, e nada captura pacotes: o tráfego por dispositivo e a deteção de '
                                'intrusões em sentido estrito não estão feitos.',
                   'hardware': 'Vigia a rede real da bancada de testes CM5 (um router, os telemóveis e os nós da casa), mas não vigiou uma casa inteira durante semanas.',
                   'security': 'Só pergunta ao router e nunca o configura; os acessos selados estão testados no anfitrião e não houve revisão independente.',
                   'integration': 'As suas mensagens chegam ao servidor da bancada de testes CM5 e ao Studio; as ordens do Studio são testadas contra uma rede com '
                                  'guião.',
                   'docs': 'Oito idiomas e o registo de alterações estão atualizados.'},
        'honest': 'O scanner, o inventário que diz o que mudou, a verificação da internet, a consulta do endereço público, as ordens do Studio e os acessos selados são '
                  'testados num computador contra uma rede guionizada (187 testes; cada mensagem é aceite pelo contrato do ARMOR-COMMON), e o programa corre como '
                  'serviço na bancada de testes do CM5, vigiando a rede real em que a bancada está (um router, os telemóveis e os nós da casa). Não vigiou uma casa '
                  'inteira durante semanas, só pergunta ao router e nunca o configura, e o que é um dispositivo (o tipo, o sistema, o fabricante) é um palpite. Não '
                  'captura pacotes: não pode ver quem fala com quem, e o tráfego por dispositivo e a deteção de intrusos em sentido estrito precisam dos contadores do '
                  'router ou de uma porta espelho, que é um passo posterior.',
        'bullets': ['**O que há na rede:** a tabela de vizinhos da máquina, um toque a cada endereço para que se preencha, um eco a cada dispositivo encontrado '
                    '(latência e TTL) e o que os dispositivos anunciam sobre si (mDNS, UPnP, NetBIOS, DNS inverso). Para cada dispositivo: endereço, MAC, fabricante (do '
                    'registo IEEE de 40 000 blocos), nome, tipo, sistema, portas abertas com o que cada uma diz, e quando foi visto pela primeira e última vez.',
                    '**Portas:** uma ligação TCP a 17 (ou 44) portas de cada dispositivo, doze de cada vez, lendo no máximo algumas centenas de bytes do que responde; '
                    'nunca um início de sessão, nunca uma exploração. Um dispositivo novo observa-se de imediato, os outros a cada quarto de hora.',
                    '**O que muda:** um dispositivo que aparece (as três primeiras pesquisas só aprendem), fica em silêncio ou volta, muda de endereço, uma porta que '
                    'abre ou fecha, e duas máquinas a responder por um endereço (sobretudo o do router). Cada evento tem um id, por isso diz-se uma só vez.',
                    '**A internet:** a cada poucos segundos um eco ao router, uma ligação TCP, duas perguntas DNS a resolvedores escolhidos e uma página web. Uma queda '
                    'precisa de três rondas para se considerar queda e duas para terminar, datada desde a sua primeira ronda falhada e contada até à primeira boa, e diz '
                    'de quem é a culpa: do operador (o router responde e nada para além dele) ou deste lado (o router também não responde). Latência, perda e as quedas '
                    'das últimas 24 horas.',
                    '**Só olha para a sua própria rede:** recusa qualquer endereço que não seja privado (10/8, 172.16/12, 192.168/16) e qualquer intervalo maior que um '
                    '/22; uma lista de exclusão mantém-no longe do que é frágil; nada se envia a um dispositivo que não seja uma pergunta.',
                    '**A mensagem** `armor/network/<node>/state`: a interface, a internet, cada dispositivo e os últimos eventos; está no contrato partilhado (330 '
                    'vetores) e leva constatações, nunca comandos. `python -m armor_network scan` imprime-a como tabela, `watch` informa o ARMOR-SERVER, `demo` '
                    'representa uma casa inventada (entra um dispositivo novo, uma câmara abre Telnet, a internet cai e volta, alguém responde pelo router) sem tocar em '
                    'nenhuma rede.',
                    '**Onde se mostra:** o menu Rede do ARMOR-STUDIO (os dispositivos, a internet com as suas quedas e latência, o tráfego e os eventos; um '
                    'administrador dá nome aos dispositivos e marca os conhecidos, o que silencia o alarme de dispositivo novo), o Desenhador de rede (o desenho da rede '
                    'da casa, comparado com o que foi encontrado, e capaz de o desenhar) e o ecrã Rede da aplicação Android. O ARMOR-SERVER dispara os alarmes.',
                    '**Ordens do Studio:** um varrimento já, um ping, um traceroute, um acordar, as portas ou a página web de um dispositivo e uma inspeção com um '
                    'acesso que der; as ordens chegam na resposta à própria mensagem do nó (nunca como uma ligação feita ao nó), cada uma é verificada antes de se fazer '
                    'algo e nada é executado por uma shell.',
                    '**Acessos que se mantêm seguros:** o acesso de uma inspeção viaja selado só para este nó, é enviado só por Digest ou HTTPS (nunca Basic por HTTP '
                    'simples), só ao dispositivo cujo certificado HTTPS foi visto da primeira vez, e nunca é devolvido em eco.',
                    '**O lado público:** o endereço público da casa, quem o dá e onde está (um pedido HTTPS a um serviço público fixo de poucos em poucos minutos; '
                    '`--no-public-info` desliga-o). Com `--dns-name` resolve também o nome com que se chega a casa a partir do exterior e diz se aponta para esse '
                    'endereço.',
                    '**Um serviço:** corre como unidade systemd na bancada de testes do CM5 (escrita à mão, veja o guia de uso) e guarda os seus dados na sua própria '
                    'pasta.',
                    '**Ainda não:** os contadores do próprio router (tráfego por dispositivo), captura de pacotes, controlar o que quer que seja (bloquear um '
                    'dispositivo, fechar uma porta, alterar o router) e semanas numa rede real.'],
        'note': 'Veja a [utilização](docs/USAGE.md) e o [desenho](docs/DESIGN.md).\n'
                '\n'
                'Veja o [desenho](docs/DESIGN.md), as [notas de segurança](docs/SAFETY.md), a [utilização](docs/USAGE.md) e as [mensagens](docs/MESSAGES.md).',
        'hardware': 'Corre como serviço na bancada de testes do CM5, vigiando a sua rede real (um router, os telemóveis e os nós da casa)',
        'fit': 'O ARMOR-NETWORK é o olho da família sobre a rede local. Corre numa máquina da rede (o CM5 na bancada), olha o que lá está sem lhe tocar e reporta ao '
               '[ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER), que guarda os nomes, os dispositivos ocultos e vigiados e as falhas; o menu *Rede* e o '
               '*Desenhador de rede* do [ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) e o ecrã Rede do '
               '[ARMOR-ANDROID-CONTROL](https://github.com/JuanenRac/ARMOR-ANDROID-CONTROL) mostram-no, e o Studio pode dar-lhe ordens. Nunca configura o router nem '
               'nenhum dispositivo.',
        'requirements': ['Python 3.11+ (apenas a biblioteca padrão)', 'uma máquina da rede a vigiar (Linux, Windows ou macOS)']}}

# the text tree of docs/structure.json (make_structure.py --tree <language>); the repository's own check fails when it and the file disagree
TREE = {'de': 'ARMOR-NETWORK/\n'
       '├── src/armor_network/\n'
       '│   ├── ipnet.py oui.py                      was geprüft werden darf; die Hersteller\n'
       '│   ├── system_io.py sim_io.py               das echte Netz; ein geskriptetes\n'
       '│   ├── neighbors.py parsers.py dnswire.py   was System und Geräte sagen\n'
       '│   ├── services.py                          Ports und Vermutungen\n'
       '│   ├── inventory.py internet.py             Geräte und Ereignisse; die Ausfallmaschine\n'
       '│   ├── agent.py publisher.py mqtt_out.py    was zu beobachten ist; wie berichtet wird\n'
       '│   ├── orders.py seal.py                    Aufträge aus Studio; versiegelte Logins\n'
       '│   ├── cli.py __main__.py                   scan, watch und demo\n'
       '│   └── data/                                oui.tsv.gz, das IEEE-Register\n'
       '├── tests/                                   187 Tests in 9 Modulen\n'
       '├── docs/                                    DESIGN, SAFETY, USAGE, MESSAGES\n'
       '├── tools/                                   fetch_oui.py erneuert das Herstellerregister; die gemeinsamen CI-Prüfungen und der Starter\n'
       '├── images/                                  Banner, Symbol und die Bilder des READMEs\n'
       '├── .github/                                 CI-Workflow, Dashboard-Hinweis, Vorlagen für Issues und Pull Requests\n'
       '├── armor.project.json                       Manifest: Version, Rolle, Reife\n'
       '├── pyproject.toml                           Paket-Metadaten, Einstiege\n'
       '├── CHANGELOG.md                             was sich in jeder Version geändert hat\n'
       '├── run.sh run.bat                           Start, gemeinsamer Ablauf\n'
       '├── build.sh build.bat                       Bauen und Testen, gemeinsamer Ablauf\n'
       '├── build-test.sh build-test.bat             Bauen, Testen und Verpacken\n'
       '├── test.sh test.bat                         nur die Tests, nie die Version\n'
       '└── SECURITY.md SUPPORT.md CONTRIBUTING.md CODE_OF_CONDUCT.md LICENSE',
 'en': 'ARMOR-NETWORK/\n'
       '├── src/armor_network/\n'
       '│   ├── ipnet.py oui.py                      what may be probed; the makers\n'
       '│   ├── system_io.py sim_io.py               the real network; a scripted one\n'
       '│   ├── neighbors.py parsers.py dnswire.py   what the system and devices say\n'
       '│   ├── services.py                          ports and guesses\n'
       '│   ├── inventory.py internet.py             devices and events; the outage machine\n'
       '│   ├── agent.py publisher.py mqtt_out.py    what to look at; how it reports\n'
       '│   ├── orders.py seal.py                    orders from Studio; sealed logins\n'
       '│   ├── cli.py __main__.py                   scan, watch and demo\n'
       '│   └── data/                                oui.tsv.gz, the IEEE register\n'
       '├── tests/                                   187 tests in 9 modules\n'
       '├── docs/                                    DESIGN, SAFETY, USAGE, MESSAGES\n'
       '├── tools/                                   fetch_oui.py refreshes the register of makers; the shared CI checks and launcher\n'
       '├── images/                                  banner, icon and the pictures of the README\n'
       '├── .github/                                 CI workflow, dashboard notice, issue and pull-request templates\n'
       '├── armor.project.json                       manifest: version, role, maturity\n'
       '├── pyproject.toml                           package metadata, entry points\n'
       '├── CHANGELOG.md                             what changed in each version\n'
       '├── run.sh run.bat                           start, shared workflow\n'
       '├── build.sh build.bat                       build and test, shared workflow\n'
       '├── build-test.sh build-test.bat             build, test and package\n'
       '├── test.sh test.bat                         only the tests, never the version\n'
       '└── SECURITY.md SUPPORT.md CONTRIBUTING.md CODE_OF_CONDUCT.md LICENSE',
 'es': 'ARMOR-NETWORK/\n'
       '├── src/armor_network/\n'
       '│   ├── ipnet.py oui.py                      qué se puede sondear; los fabricantes\n'
       '│   ├── system_io.py sim_io.py               la red real; una guionizada\n'
       '│   ├── neighbors.py parsers.py dnswire.py   lo que dicen el sistema y los equipos\n'
       '│   ├── services.py                          puertos y suposiciones\n'
       '│   ├── inventory.py internet.py             equipos y eventos; la máquina de caídas\n'
       '│   ├── agent.py publisher.py mqtt_out.py    qué mirar; cómo informa\n'
       '│   ├── orders.py seal.py                    órdenes de Studio; accesos sellados\n'
       '│   ├── cli.py __main__.py                   scan, watch y demo\n'
       '│   └── data/                                oui.tsv.gz, el registro IEEE\n'
       '├── tests/                                   187 pruebas en 9 módulos\n'
       '├── docs/                                    DESIGN, SAFETY, USAGE, MESSAGES\n'
       '├── tools/                                   fetch_oui.py renueva el registro de fabricantes; las comprobaciones de CI y el lanzador\n'
       '├── images/                                  banner, icono y las imágenes del README\n'
       '├── .github/                                 flujo de CI, aviso al panel, plantillas de incidencias y pull requests\n'
       '├── armor.project.json                       manifiesto: versión, función, madurez\n'
       '├── pyproject.toml                           metadatos del paquete, entradas\n'
       '├── CHANGELOG.md                             qué cambió en cada versión\n'
       '├── run.sh run.bat                           arrancar, flujo compartido\n'
       '├── build.sh build.bat                       construir y probar, flujo compartido\n'
       '├── build-test.sh build-test.bat             construir, probar y empaquetar\n'
       '├── test.sh test.bat                         solo las pruebas, nunca la versión\n'
       '└── SECURITY.md SUPPORT.md CONTRIBUTING.md CODE_OF_CONDUCT.md LICENSE',
 'fr': 'ARMOR-NETWORK/\n'
       '├── src/armor_network/\n'
       "│   ├── ipnet.py oui.py                      ce qu'on peut sonder ; les fabricants\n"
       '│   ├── system_io.py sim_io.py               le réseau réel ; un réseau scripté\n'
       '│   ├── neighbors.py parsers.py dnswire.py   ce que disent le système et les appareils\n'
       '│   ├── services.py                          ports et suppositions\n'
       '│   ├── inventory.py internet.py             appareils et événements ; la machine des pannes\n'
       '│   ├── agent.py publisher.py mqtt_out.py    quoi regarder ; comment il rapporte\n'
       '│   ├── orders.py seal.py                    ordres de Studio ; identifiants scellés\n'
       '│   ├── cli.py __main__.py                   scan, watch et demo\n'
       '│   └── data/                                oui.tsv.gz, le registre IEEE\n'
       '├── tests/                                   187 tests en 9 modules\n'
       '├── docs/                                    DESIGN, SAFETY, USAGE, MESSAGES\n'
       '├── tools/                                   fetch_oui.py rafraîchit le registre des fabricants ; les vérifications CI et le lanceur\n'
       '├── images/                                  bannière, icône et images du README\n'
       "├── .github/                                 workflow CI, avis au tableau de bord, modèles d'issues et de pull requests\n"
       '├── armor.project.json                       manifeste : version, rôle, maturité\n'
       '├── pyproject.toml                           métadonnées du paquet, entrées\n'
       '├── CHANGELOG.md                             ce qui a changé à chaque version\n'
       '├── run.sh run.bat                           démarrer, flux partagé\n'
       '├── build.sh build.bat                       construire et tester, flux partagé\n'
       '├── build-test.sh build-test.bat             construire, tester, empaqueter\n'
       '├── test.sh test.bat                         seulement les tests, jamais la version\n'
       '└── SECURITY.md SUPPORT.md CONTRIBUTING.md CODE_OF_CONDUCT.md LICENSE',
 'it': 'ARMOR-NETWORK/\n'
       '├── src/armor_network/\n'
       '│   ├── ipnet.py oui.py                      cosa si può sondare; i produttori\n'
       '│   ├── system_io.py sim_io.py               la rete reale; una guidata\n'
       '│   ├── neighbors.py parsers.py dnswire.py   cosa dicono il sistema e i dispositivi\n'
       '│   ├── services.py                          porte e supposizioni\n'
       '│   ├── inventory.py internet.py             dispositivi ed eventi; la macchina dei guasti\n'
       '│   ├── agent.py publisher.py mqtt_out.py    cosa guardare; come riferisce\n'
       '│   ├── orders.py seal.py                    ordini da Studio; accessi sigillati\n'
       '│   ├── cli.py __main__.py                   scan, watch e demo\n'
       '│   └── data/                                oui.tsv.gz, il registro IEEE\n'
       '├── tests/                                   187 test in 9 moduli\n'
       '├── docs/                                    DESIGN, SAFETY, USAGE, MESSAGES\n'
       "├── tools/                                   fetch_oui.py aggiorna il registro dei produttori; i controlli CI e l'avviatore\n"
       '├── images/                                  banner, icona e immagini del README\n'
       '├── .github/                                 workflow CI, avviso alla dashboard, modelli per issue e pull request\n'
       '├── armor.project.json                       manifesto: versione, ruolo, maturità\n'
       '├── pyproject.toml                           metadati del pacchetto, ingressi\n'
       '├── CHANGELOG.md                             cosa è cambiato in ogni versione\n'
       '├── run.sh run.bat                           avvio, flusso condiviso\n'
       '├── build.sh build.bat                       compila e prova, flusso condiviso\n'
       '├── build-test.sh build-test.bat             compila, prova e impacchetta\n'
       '├── test.sh test.bat                         solo i test, mai la versione\n'
       '└── SECURITY.md SUPPORT.md CONTRIBUTING.md CODE_OF_CONDUCT.md LICENSE',
 'ja': 'ARMOR-NETWORK/\n'
       '├── src/armor_network/\n'
       '│   ├── ipnet.py oui.py                      調べてよい範囲、メーカー\n'
       '│   ├── system_io.py sim_io.py               実ネットワークとスクリプト版\n'
       '│   ├── neighbors.py parsers.py dnswire.py   システムと機器の応答\n'
       '│   ├── services.py                          ポートと推測\n'
       '│   ├── inventory.py internet.py             機器とイベント、障害の状態機械\n'
       '│   ├── agent.py publisher.py mqtt_out.py    見る対象、報告方法\n'
       '│   ├── orders.py seal.py                    Studio からのオーダーと封印した認証情報\n'
       '│   ├── cli.py __main__.py                   scan・watch・demo\n'
       '│   └── data/                                oui.tsv.gz（IEEE 登録簿）\n'
       '├── tests/                                   9 モジュール 187 件\n'
       '├── docs/                                    DESIGN、SAFETY、USAGE、MESSAGES\n'
       '├── tools/                                   fetch_oui.py がメーカー登録簿を更新、共通の CI 検査とランチャー\n'
       '├── images/                                  バナー、アイコン、README の画像\n'
       '├── .github/                                 CI ワークフロー、ダッシュボード通知、Issue と Pull Request のテンプレート\n'
       '├── armor.project.json                       マニフェスト：版・役割・成熟度\n'
       '├── pyproject.toml                           パッケージ情報とエントリー\n'
       '├── CHANGELOG.md                             各バージョンの変更点\n'
       '├── run.sh run.bat                           起動（共通フロー）\n'
       '├── build.sh build.bat                       ビルドとテスト（共通フロー）\n'
       '├── build-test.sh build-test.bat             ビルド、テスト、パッケージ化\n'
       '├── test.sh test.bat                         テストのみ（版は変えません）\n'
       '└── SECURITY.md SUPPORT.md CONTRIBUTING.md CODE_OF_CONDUCT.md LICENSE',
 'pt': 'ARMOR-NETWORK/\n'
       '├── src/armor_network/\n'
       '│   ├── ipnet.py oui.py                      o que se pode sondar; os fabricantes\n'
       '│   ├── system_io.py sim_io.py               a rede real; uma com guião\n'
       '│   ├── neighbors.py parsers.py dnswire.py   o que dizem o sistema e os equipamentos\n'
       '│   ├── services.py                          portas e suposições\n'
       '│   ├── inventory.py internet.py             equipamentos e eventos; a máquina de quedas\n'
       '│   ├── agent.py publisher.py mqtt_out.py    o que olhar; como reporta\n'
       '│   ├── orders.py seal.py                    ordens do Studio; credenciais seladas\n'
       '│   ├── cli.py __main__.py                   scan, watch e demo\n'
       '│   └── data/                                oui.tsv.gz, o registo IEEE\n'
       '├── tests/                                   187 testes em 9 módulos\n'
       '├── docs/                                    DESIGN, SAFETY, USAGE, MESSAGES\n'
       '├── tools/                                   fetch_oui.py renova o registo de fabricantes; as verificações de CI e o lançador\n'
       '├── images/                                  faixa, ícone e as imagens do README\n'
       '├── .github/                                 fluxo de CI, aviso ao painel, modelos de issues e pull requests\n'
       '├── armor.project.json                       manifesto: versão, função, maturidade\n'
       '├── pyproject.toml                           metadados do pacote, entradas\n'
       '├── CHANGELOG.md                             o que mudou em cada versão\n'
       '├── run.sh run.bat                           arrancar, fluxo partilhado\n'
       '├── build.sh build.bat                       compilar e testar, fluxo partilhado\n'
       '├── build-test.sh build-test.bat             compilar, testar e empacotar\n'
       '├── test.sh test.bat                         só os testes, nunca a versão\n'
       '└── SECURITY.md SUPPORT.md CONTRIBUTING.md CODE_OF_CONDUCT.md LICENSE',
 'zh': 'ARMOR-NETWORK/\n'
       '├── src/armor_network/\n'
       '│   ├── ipnet.py oui.py                      可探测的范围；厂商\n'
       '│   ├── system_io.py sim_io.py               真实网络；脚本网络\n'
       '│   ├── neighbors.py parsers.py dnswire.py   系统和设备的回应\n'
       '│   ├── services.py                          端口与推测\n'
       '│   ├── inventory.py internet.py             设备与事件；中断状态机\n'
       '│   ├── agent.py publisher.py mqtt_out.py    看什么；如何上报\n'
       '│   ├── orders.py seal.py                    来自 Studio 的指令；密封凭据\n'
       '│   ├── cli.py __main__.py                   scan、watch 和 demo\n'
       '│   └── data/                                oui.tsv.gz（IEEE 注册表）\n'
       '├── tests/                                   9 个模块 187 项测试\n'
       '├── docs/                                    DESIGN、SAFETY、USAGE、MESSAGES\n'
       '├── tools/                                   fetch_oui.py 刷新厂商注册表；共用的 CI 检查与启动器\n'
       '├── images/                                  横幅图、图标和 README 的图片\n'
       '├── .github/                                 CI 工作流、仪表板通知、议题和 pull request 模板\n'
       '├── armor.project.json                       清单：版本、角色、成熟度\n'
       '├── pyproject.toml                           包元数据、入口\n'
       '├── CHANGELOG.md                             每个版本的变化\n'
       '├── run.sh run.bat                           启动（共用流程）\n'
       '├── build.sh build.bat                       构建并测试（共用流程）\n'
       '├── build-test.sh build-test.bat             构建、测试并打包\n'
       '├── test.sh test.bat                         只运行测试，不改版本\n'
       '└── SECURITY.md SUPPORT.md CONTRIBUTING.md CODE_OF_CONDUCT.md LICENSE'}

DIAGRAM = ''

NT = "187"
FACTS["badges"] = [x for x in FACTS["badges"] if x[0] != "Tests"] + [["Tests", NT + "%20passing", "2ea44f"]]


def fix(s):
    return s.replace("330", "111")


def L(lg, key):
    v = LEGACY[lg][key]
    return fix(v) if isinstance(v, str) else [fix(x) for x in v]


GLANCE = [
    (GL["role"], T("Local network node: what is on the network, what changed, the internet, orders from Studio | Nodo de red local: qué hay en la red, qué cambió, internet, órdenes de Studio | Knoten für das lokale Netz: was im Netz ist, was sich änderte, das Internet, Aufträge aus Studio | Nœud du réseau local : ce qu'il y a sur le réseau, ce qui a changé, internet, ordres de Studio | Nodo della rete locale: cosa c'è in rete, cosa è cambiato, internet, ordini da Studio | ローカルネットワークのノード：ネットワーク上の機器、変化、インターネット、Studio からのオーダー | 本地网络节点：网络上有什么、发生了什么变化、互联网、来自 Studio 的指令 | Nó da rede local: o que há na rede, o que mudou, a internet, ordens do Studio")),
    (GL["stack"], T("Python 3.11+, standard library only | Python 3.11+, solo biblioteca estándar | Python 3.11+, nur Standardbibliothek | Python 3.11+, bibliothèque standard seule | Python 3.11+, solo libreria standard | Python 3.11+（標準ライブラリのみ） | Python 3.11+，仅用标准库 | Python 3.11+, só biblioteca padrão")),
    (GL["tests"], T("187 (`python -m unittest discover -s tests`) | 187 (`python -m unittest discover -s tests`) | 187 (`python -m unittest discover -s tests`) | 187 (`python -m unittest discover -s tests`) | 187 (`python -m unittest discover -s tests`) | 187 件（`python -m unittest discover -s tests`） | 187 项（`python -m unittest discover -s tests`） | 187 (`python -m unittest discover -s tests`)")),
    (GL["contract"], T("Message `armor/network/<node>/state`, 111 conformance vectors (messages and orders) | Mensaje `armor/network/<nodo>/state`, 111 vectores de conformidad (mensajes y órdenes) | Nachricht `armor/network/<Knoten>/state`, 111 Konformitätsvektoren (Nachrichten und Aufträge) | Message `armor/network/<nœud>/state`, 111 vecteurs de conformité (messages et ordres) | Messaggio `armor/network/<nodo>/state`, 111 vettori di conformità (messaggi e ordini) | メッセージ `armor/network/<ノード>/state`、適合ベクター 111 件（メッセージとオーダー） | 消息 `armor/network/<节点>/state`，111 个一致性向量（消息与指令） | Mensagem `armor/network/<nó>/state`, 111 vetores de conformidade (mensagens e ordens)")),
    (GL["runs"], T("A machine of the network to be watched (Linux, Windows or macOS); the CM5 test bench as a service | Una máquina de la red a vigilar (Linux, Windows o macOS); el banco de la CM5 como servicio | Ein Rechner des überwachten Netzes (Linux, Windows oder macOS); der CM5-Prüfstand als Dienst | Une machine du réseau à surveiller (Linux, Windows ou macOS) ; le banc d'essai CM5 en service | Una macchina della rete da sorvegliare (Linux, Windows o macOS); il banco di prova CM5 come servizio | 監視対象ネットワーク上のマシン（Linux、Windows、macOS）。CM5 テストベンチではサービスとして | 被监视网络中的一台机器（Linux、Windows 或 macOS）；CM5 测试台上作为服务 | Uma máquina da rede a vigiar (Linux, Windows ou macOS); a bancada do CM5 como serviço")),
    (GL["hardware"], {lg: LEGACY[lg]["hardware"] for lg in LGS}),
    (GL["license"], LICENSE_VALUE),
]

ROLE_TABLE = [
    ("ARMOR-SERVER", T("HTTP `POST` with the ingest token (`--server-url`) | HTTP `POST` con el token de ingesta (`--server-url`) | HTTP-`POST` mit dem Ingest-Token (`--server-url`) | `POST` HTTP avec le jeton d'ingestion (`--server-url`) | `POST` HTTP con il token di ingestione (`--server-url`) | 取り込みトークン付きの HTTP `POST`（`--server-url`） | 带采集令牌的 HTTP `POST`（`--server-url`） | `POST` HTTP com o token de ingestão (`--server-url`)"), T("the state goes in; the orders come back in the answer | entra el estado; las órdenes vuelven en la respuesta | der Zustand geht hinein; die Aufträge kommen in der Antwort zurück | l'état entre ; les ordres reviennent dans la réponse | entra lo stato; gli ordini tornano nella risposta | 状態を送り、オーダーは応答で戻る | 发送状态；指令在响应中返回 | entra o estado; as ordens voltam na resposta")),
    ("MQTT", T("`--mqtt-url` (`mqtt://` or `mqtts://`) | `--mqtt-url` (`mqtt://` o `mqtts://`) | `--mqtt-url` (`mqtt://` oder `mqtts://`) | `--mqtt-url` (`mqtt://` ou `mqtts://`) | `--mqtt-url` (`mqtt://` o `mqtts://`) | `--mqtt-url`（`mqtt://` または `mqtts://`） | `--mqtt-url`（`mqtt://` 或 `mqtts://`） | `--mqtt-url` (`mqtt://` ou `mqtts://`)"), T("the same message also on the broker; the manual orders do not travel this way | el mismo mensaje también en el broker; las órdenes manuales no viajan así | dieselbe Nachricht auch am Broker; die manuellen Aufträge reisen nicht so | le même message aussi sur le broker ; les ordres manuels ne passent pas ainsi | lo stesso messaggio anche sul broker; gli ordini manuali non viaggiano così | 同じメッセージをブローカーにも送る（手動オーダーはこの経路では届かない） | 同一条消息也发到代理；手动指令不走这条路 | a mesma mensagem também no broker; as ordens manuais não viajam assim")),
    ("ARMOR-STUDIO", T("through the server | a través del servidor | über den Server | via le serveur | tramite il server | サーバー経由 | 经服务器 | através do servidor"), T("the Network menu and the Network Designer show it and hand it orders | el menú Red y el Diseñador de red lo muestran y le dan órdenes | das Netzwerk-Menü und der Netzwerk-Designer zeigen es und geben Aufträge | le menu Réseau et le concepteur réseau l'affichent et lui donnent des ordres | il menu Rete e il progettista di rete lo mostrano e gli danno ordini | ネットワークメニューとネットワークデザイナーが表示し、オーダーを渡す | 网络菜单和网络设计器显示它并向它下达指令 | o menu Rede e o desenhador de rede mostram-no e dão-lhe ordens")),
    ("ARMOR-ANDROID-CONTROL", T("through the server | a través del servidor | über den Server | via le serveur | tramite il server | サーバー経由 | 经服务器 | através do servidor"), T("the Network screen | la pantalla Red | der Netzwerk-Bildschirm | l'écran Réseau | la schermata Rete | ネットワーク画面 | 网络界面 | o ecrã Rede")),
    ("ARMOR-COMMON", T("the contract of the message and of the orders | el contrato del mensaje y de las órdenes | der Vertrag der Nachricht und der Aufträge | le contrat du message et des ordres | il contratto del messaggio e degli ordini | メッセージとオーダーの契約 | 消息与指令的契约 | o contrato da mensagem e das ordens"), T("`--validate` checks every message against it | `--validate` comprueba cada mensaje con él | `--validate` prüft jede Nachricht damit | `--validate` vérifie chaque message avec lui | `--validate` verifica ogni messaggio con esso | `--validate` で各メッセージを検査 | `--validate` 用它检查每条消息 | `--validate` verifica cada mensagem com ele")),
]


def S(a, b):
    return (T(a), T(b))


SECURITY_ROWS = [
    S("Scanning outside the house or another network | Escanear fuera de la casa o una red ajena | Scannen außerhalb des Hauses oder fremder Netze | Scanner hors de la maison ou un réseau étranger | Scansionare fuori casa o una rete altrui | 家の外や他人のネットワークのスキャン | 扫描屋外或他人的网络 | Varrer fora de casa ou uma rede alheia",
      "Only private ranges (10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16) and never more than 1024 addresses (a /22); `--cidr` is always private; the guard is `check_scan_range`, not an option | Solo rangos privados (10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16) y nunca más de 1024 direcciones (un /22); `--cidr` es siempre privado; la guarda es `check_scan_range`, no una opción | Nur private Bereiche (10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16) und nie mehr als 1024 Adressen (ein /22); `--cidr` ist immer privat; die Sperre ist `check_scan_range`, keine Option | Seulement des plages privées (10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16) et jamais plus de 1024 adresses (un /22) ; `--cidr` est toujours privé ; la garde est `check_scan_range`, pas une option | Solo intervalli privati (10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16) e mai più di 1024 indirizzi (un /22); `--cidr` è sempre privato; la guardia è `check_scan_range`, non un'opzione | プライベート範囲（10.0.0.0/8、172.16.0.0/12、192.168.0.0/16）のみで、1024 アドレス（/22）を超えません。`--cidr` も常にプライベート。ガードは `check_scan_range` で、オプションではありません | 只扫描私有网段（10.0.0.0/8、172.16.0.0/12、192.168.0.0/16），且绝不超过 1024 个地址（/22）；`--cidr` 也必须是私有网段；防护是 `check_scan_range`，不是选项 | Só intervalos privados (10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16) e nunca mais de 1024 endereços (um /22); `--cidr` é sempre privado; a guarda é `check_scan_range`, não uma opção"),
    S("Breaking something fragile | Romper algo frágil | Etwas Empfindliches stören | Casser quelque chose de fragile | Rompere qualcosa di fragile | 壊れやすい機器への悪影響 | 弄坏脆弱的设备 | Estragar algo frágil",
      "A skip list (`--skip IP`, repeatable); nothing is sent to a device that is not a question; never a login, never an exploit; 12 connections at a time reading a few hundred bytes | Una lista de exclusión (`--skip IP`, repetible); no se envía nada a un equipo que no sea una pregunta; nunca un login, nunca un exploit; 12 conexiones a la vez leyendo unos cientos de bytes | Eine Ausschlussliste (`--skip IP`, wiederholbar); an ein Gerät wird nichts gesendet, was keine Frage ist; nie ein Login, nie ein Exploit; 12 Verbindungen gleichzeitig, die wenige hundert Bytes lesen | Une liste d'exclusion (`--skip IP`, répétable) ; rien n'est envoyé à un appareil qui ne soit une question ; jamais d'identifiant, jamais d'exploit ; 12 connexions à la fois lisant quelques centaines d'octets | Una lista di esclusione (`--skip IP`, ripetibile); a un dispositivo non si manda nulla che non sia una domanda; mai un login, mai un exploit; 12 connessioni alla volta che leggono poche centinaia di byte | スキップリスト（`--skip IP`、複数可）。質問でないものは機器に送らず、ログインも攻撃コードも使いません。同時 12 接続で数百バイトだけ読みます | 跳过列表（`--skip IP`，可重复）；不向设备发送任何不是提问的内容；绝不登录、绝不利用漏洞；同时 12 个连接，只读几百字节 | Uma lista de exclusão (`--skip IP`, repetível); nada é enviado a um equipamento que não seja uma pergunta; nunca um login, nunca um exploit; 12 ligações de cada vez a ler umas centenas de bytes"),
    S("Risky open ports go unnoticed | Puertos abiertos de riesgo pasan inadvertidos | Riskante offene Ports bleiben unbemerkt | Des ports ouverts à risque passent inaperçus | Porte aperte a rischio passano inosservate | 危険な開放ポートに気付かない | 高风险开放端口被忽略 | Portas abertas de risco passam despercebidas",
      "They are marked: 21, 23, 3389, 5900, 6379, 3306, 5432, 7547 and 445 | Se marcan: 21, 23, 3389, 5900, 6379, 3306, 5432, 7547 y 445 | Sie werden markiert: 21, 23, 3389, 5900, 6379, 3306, 5432, 7547 und 445 | Elles sont marquées : 21, 23, 3389, 5900, 6379, 3306, 5432, 7547 et 445 | Sono segnalate: 21, 23, 3389, 5900, 6379, 3306, 5432, 7547 e 445 | 21、23、3389、5900、6379、3306、5432、7547、445 を印付けします | 会被标记：21、23、3389、5900、6379、3306、5432、7547 和 445 | São assinaladas: 21, 23, 3389, 5900, 6379, 3306, 5432, 7547 e 445"),
    S("Orders from the server that inject commands | Órdenes del servidor que inyecten comandos | Aufträge vom Server, die Befehle einschleusen | Des ordres du serveur qui injectent des commandes | Ordini dal server che iniettano comandi | コマンドを注入するサーバーからのオーダー | 注入命令的服务器指令 | Ordens do servidor que injetam comandos",
      "A closed list: `scan_now`, `ping`, `traceroute`, `wake`, `ports`, `http`, `inspect`; at most 4 at a time; an order id of letters, digits, `_` and `-` (32 at most); output cut at 2000; MAC checked; nothing is run through a shell; orders arrive in the answer to the node's own message, never as a connection made to the node | Una lista cerrada: `scan_now`, `ping`, `traceroute`, `wake`, `ports`, `http`, `inspect`; como mucho 4 a la vez; un id de orden de letras, dígitos, `_` y `-` (32 como máximo); salida cortada a 2000; MAC comprobada; nada pasa por un shell; las órdenes llegan en la respuesta al mensaje del propio nodo, nunca como una conexión hecha al nodo | Eine geschlossene Liste: `scan_now`, `ping`, `traceroute`, `wake`, `ports`, `http`, `inspect`; höchstens 4 gleichzeitig; eine Auftrags-ID aus Buchstaben, Ziffern, `_` und `-` (höchstens 32); Ausgabe bei 2000 gekappt; MAC geprüft; nichts läuft über eine Shell; Aufträge kommen in der Antwort auf die eigene Nachricht des Knotens, nie als Verbindung zum Knoten | Une liste fermée : `scan_now`, `ping`, `traceroute`, `wake`, `ports`, `http`, `inspect` ; 4 au plus à la fois ; un identifiant d'ordre en lettres, chiffres, `_` et `-` (32 au plus) ; sortie coupée à 2000 ; MAC vérifiée ; rien ne passe par un shell ; les ordres arrivent dans la réponse au message du nœud lui-même, jamais en connexion vers le nœud | Un elenco chiuso: `scan_now`, `ping`, `traceroute`, `wake`, `ports`, `http`, `inspect`; al massimo 4 alla volta; un id d'ordine di lettere, cifre, `_` e `-` (32 al massimo); output tagliato a 2000; MAC verificato; nulla passa da una shell; gli ordini arrivano nella risposta al messaggio del nodo stesso, mai come connessione verso il nodo | 固定のリスト：`scan_now`、`ping`、`traceroute`、`wake`、`ports`、`http`、`inspect`。同時 4 件まで、オーダー ID は英数字と `_` `-`（最大 32 文字）、出力は 2000 で切り詰め、MAC は検証、シェルは経由しません。オーダーはノード自身のメッセージへの応答で届き、ノードへ接続することはありません | 封闭列表：`scan_now`、`ping`、`traceroute`、`wake`、`ports`、`http`、`inspect`；同时最多 4 个；指令 ID 由字母、数字、`_` 和 `-` 组成（最多 32 个）；输出截断为 2000；校验 MAC；不经过 shell；指令随节点自己消息的响应到达，绝不通过连接到节点的方式 | Uma lista fechada: `scan_now`, `ping`, `traceroute`, `wake`, `ports`, `http`, `inspect`; no máximo 4 de cada vez; um id de ordem de letras, dígitos, `_` e `-` (32 no máximo); saída cortada em 2000; MAC verificado; nada passa por uma shell; as ordens chegam na resposta à mensagem do próprio nó, nunca como uma ligação feita ao nó"),
    S("The login of an inspection leaks | Se filtra el login de una inspección | Das Login einer Inspektion gelangt nach außen | L'identifiant d'une inspection fuit | Il login di un'ispezione trapela | 検査用ログインの漏えい | 检查所用登录信息泄露 | O login de uma inspeção vaza",
      "It travels sealed for this node alone, only over Digest or HTTPS (never Basic over plain HTTP), only to the device whose HTTPS certificate was seen the first time, and is never repeated in an answer; the factory logins it tries come from a fixed list | Viaja sellado solo para este nodo, solo por Digest o HTTPS (nunca Basic por HTTP plano), solo al equipo cuyo certificado HTTPS se vio la primera vez, y nunca se repite en una respuesta; los accesos de fábrica que prueba salen de una lista fija | Es reist nur für diesen Knoten versiegelt, nur über Digest oder HTTPS (nie Basic über einfaches HTTP), nur zum Gerät, dessen HTTPS-Zertifikat beim ersten Mal gesehen wurde, und wird nie in einer Antwort wiederholt; die Werkslogins, die es probiert, stammen aus einer festen Liste | Il voyage scellé pour ce seul nœud, seulement en Digest ou HTTPS (jamais Basic en HTTP simple), seulement vers l'appareil dont le certificat HTTPS a été vu la première fois, et n'est jamais répété dans une réponse ; les identifiants d'usine essayés viennent d'une liste fixe | Viaggia sigillato per questo solo nodo, solo con Digest o HTTPS (mai Basic su HTTP semplice), solo verso il dispositivo il cui certificato HTTPS è stato visto la prima volta, e non si ripete mai in una risposta; i login di fabbrica provati vengono da un elenco fisso | このノードだけ向けに封印され、Digest か HTTPS でのみ送られ（平文 HTTP の Basic は不可）、HTTPS 証明書を最初に確認した機器にだけ送られ、応答には決して繰り返されません。試す工場出荷時ログインは固定リストです | 仅为本节点密封传输，只通过 Digest 或 HTTPS（绝不在明文 HTTP 上用 Basic），只发给首次见到其 HTTPS 证书的设备，且绝不会在响应中重复；它尝试的出厂登录来自固定列表 | Viaja selado só para este nó, apenas por Digest ou HTTPS (nunca Basic em HTTP simples), só para o equipamento cujo certificado HTTPS foi visto da primeira vez, e nunca se repete numa resposta; os logins de fábrica que tenta vêm de uma lista fixa"),
    S("A request that leaves the house | Una petición que sale de la casa | Eine Anfrage, die das Haus verlässt | Une requête qui sort de la maison | Una richiesta che esce di casa | 家の外へ出るリクエスト | 离开屋子的请求 | Um pedido que sai de casa",
      "One HTTPS request to a fixed public service (`https://ipinfo.io/json` by default) every few minutes, for the public address; `--no-public-info` turns it off; `--dns-name` also checks that the name the house is reached by points to it | Una petición HTTPS a un servicio público fijo (`https://ipinfo.io/json` por defecto) cada pocos minutos, para la dirección pública; `--no-public-info` la apaga; `--dns-name` comprueba además que el nombre con el que se llega a la casa apunta a ella | Eine HTTPS-Anfrage an einen festen öffentlichen Dienst (standardmäßig `https://ipinfo.io/json`) alle paar Minuten für die öffentliche Adresse; `--no-public-info` schaltet sie ab; `--dns-name` prüft zusätzlich, dass der Name, unter dem das Haus erreichbar ist, darauf zeigt | Une requête HTTPS vers un service public fixe (`https://ipinfo.io/json` par défaut) toutes les quelques minutes, pour l'adresse publique ; `--no-public-info` la désactive ; `--dns-name` vérifie aussi que le nom par lequel on joint la maison y pointe | Una richiesta HTTPS a un servizio pubblico fisso (`https://ipinfo.io/json` di default) ogni pochi minuti, per l'indirizzo pubblico; `--no-public-info` la spegne; `--dns-name` verifica anche che il nome con cui si raggiunge la casa punti a quell'indirizzo | 公開アドレスのために、数分ごとに固定の公開サービス（既定 `https://ipinfo.io/json`）へ HTTPS リクエストを 1 回送ります。`--no-public-info` で無効化。`--dns-name` は外から家に届く名前がそのアドレスを指すかも確認します | 为获取公网地址，每隔几分钟向固定的公共服务（默认 `https://ipinfo.io/json`）发一次 HTTPS 请求；`--no-public-info` 可关闭；`--dns-name` 还会检查从外部访问家的名称是否指向该地址 | Um pedido HTTPS a um serviço público fixo (`https://ipinfo.io/json` por predefinição) a cada poucos minutos, para o endereço público; `--no-public-info` desliga-o; `--dns-name` verifica ainda que o nome pelo qual se chega à casa aponta para ele"),
]
SEC_TAIL = P("**What it never does:** configure the router, capture packets, block a device or close a port. What a device is (its kind, its system, its maker) is a guess. The safety notes are in [docs/SAFETY.md](docs/SAFETY.md); there has been no independent review.",
             "**Lo que nunca hace:** configurar el router, capturar paquetes, bloquear un equipo ni cerrar un puerto. Lo que es un equipo (su tipo, su sistema, su fabricante) es una suposición. Las notas de seguridad están en [docs/SAFETY.md](docs/SAFETY.md); no ha habido revisión independiente.",
             "**Was es nie tut:** den Router konfigurieren, Pakete mitschneiden, ein Gerät sperren oder einen Port schließen. Was ein Gerät ist (Art, System, Hersteller), ist eine Vermutung. Die Sicherheitshinweise stehen in [docs/SAFETY.md](docs/SAFETY.md); eine unabhängige Prüfung gab es nicht.",
             "**Ce qu'il ne fait jamais :** configurer le routeur, capturer des paquets, bloquer un appareil ou fermer un port. Ce qu'est un appareil (son type, son système, son fabricant) est une supposition. Les notes de sécurité sont dans [docs/SAFETY.md](docs/SAFETY.md) ; il n'y a pas eu de revue indépendante.",
             "**Cosa non fa mai:** configurare il router, catturare pacchetti, bloccare un dispositivo o chiudere una porta. Ciò che è un dispositivo (tipo, sistema, produttore) è una supposizione. Le note di sicurezza sono in [docs/SAFETY.md](docs/SAFETY.md); non c'è stata una revisione indipendente.",
             "**決してしないこと：** ルーターの設定、パケットキャプチャ、機器のブロック、ポートの閉鎖。機器が何であるか（種類、システム、メーカー）は推測です。安全上の注意は [docs/SAFETY.md](docs/SAFETY.md) にあります。第三者によるレビューはありません。",
             "**它绝不会：** 配置路由器、抓包、封锁设备或关闭端口。设备是什么（类型、系统、厂商）只是推测。安全说明见 [docs/SAFETY.md](docs/SAFETY.md)；没有独立审查。",
             "**O que nunca faz:** configurar o router, capturar pacotes, bloquear um equipamento nem fechar uma porta. O que um equipamento é (o seu tipo, o seu sistema, o seu fabricante) é uma suposição. As notas de segurança estão em [docs/SAFETY.md](docs/SAFETY.md); não houve revisão independente.")

IFACE = [
    ("`armor/network/<node>/state`", T("message | mensaje | Nachricht | message | messaggio | メッセージ | 消息 | mensagem"), T("the interface, the internet, every device and the latest events; it carries findings, never commands | la interfaz, internet, cada equipo y los últimos eventos; lleva hallazgos, nunca órdenes | die Schnittstelle, das Internet, jedes Gerät und die letzten Ereignisse; sie trägt Befunde, nie Befehle | l'interface, internet, chaque appareil et les derniers événements ; il porte des constats, jamais des ordres | l'interfaccia, internet, ogni dispositivo e gli ultimi eventi; porta rilievi, mai comandi | インターフェース、インターネット、全機器、最新イベント。所見のみで、コマンドは載せません | 接口、互联网、每台设备和最新事件；只带发现，绝不带命令 | a interface, a internet, cada equipamento e os últimos eventos; leva constatações, nunca ordens")),
    ("`python -m armor_network scan [--json]`", "-", T("look at the network once and print it as a table (or as the message) | mira la red una vez y la imprime como tabla (o como el mensaje) | das Netz einmal ansehen und als Tabelle (oder Nachricht) ausgeben | regarde le réseau une fois et l'imprime en tableau (ou en message) | guarda la rete una volta e la stampa come tabella (o come messaggio) | ネットワークを 1 回調べて表（またはメッセージ）で表示 | 查看一次网络并以表格（或消息）打印 | olha para a rede uma vez e imprime-a como tabela (ou como a mensagem)")),
    ("`python -m armor_network watch`", "-", T("keep watching; with `--server-url` and `--ingest-token` it tells ARMOR-SERVER, with `--mqtt-url` also the broker | sigue vigilando; con `--server-url` y `--ingest-token` informa a ARMOR-SERVER, con `--mqtt-url` también al broker | weiter beobachten; mit `--server-url` und `--ingest-token` meldet es an ARMOR-SERVER, mit `--mqtt-url` auch an den Broker | continue de surveiller ; avec `--server-url` et `--ingest-token` il informe ARMOR-SERVER, avec `--mqtt-url` aussi le broker | continua a sorvegliare; con `--server-url` e `--ingest-token` informa ARMOR-SERVER, con `--mqtt-url` anche il broker | 監視を続け、`--server-url` と `--ingest-token` で ARMOR-SERVER に、`--mqtt-url` でブローカーにも通知 | 持续监视；用 `--server-url` 和 `--ingest-token` 通知 ARMOR-SERVER，用 `--mqtt-url` 还通知代理 | continua a vigiar; com `--server-url` e `--ingest-token` informa o ARMOR-SERVER, com `--mqtt-url` também o broker")),
    ("`python -m armor_network demo [--count N]`", "-", T("a made-up house (a device joins, a camera opens Telnet, the internet falls): nothing on any network is touched | una casa inventada (entra un equipo, una cámara abre Telnet, cae internet): no se toca ninguna red | ein erfundenes Haus (ein Gerät tritt bei, eine Kamera öffnet Telnet, das Internet fällt aus): kein Netz wird berührt | une maison fictive (un appareil arrive, une caméra ouvre Telnet, internet tombe) : aucun réseau n'est touché | una casa inventata (entra un dispositivo, una telecamera apre Telnet, cade internet): nessuna rete viene toccata | 架空の家（機器の参加、カメラの Telnet 開放、インターネット断）。実ネットワークには触れません | 虚构的房子（设备加入、摄像头开放 Telnet、互联网中断）：不会触碰任何网络 | uma casa inventada (entra um equipamento, uma câmara abre Telnet, cai a internet): nenhuma rede é tocada")),
    ("`python -m armor_network internet`  `oui <mac>`", "-", T("one round of the internet check; who made a network card | una ronda de la comprobación de internet; quién fabricó una tarjeta de red | eine Runde der Internetprüfung; wer eine Netzwerkkarte gebaut hat | une ronde du contrôle d'internet ; qui a fabriqué une carte réseau | un giro del controllo di internet; chi ha prodotto una scheda di rete | インターネット確認を 1 回、ネットワークカードのメーカー照会 | 一轮互联网检查；某张网卡的厂商 | uma ronda da verificação da internet; quem fabricou uma placa de rede")),
]
IFACE_NOTE = P("The orders from Studio (`scan_now`, `ping`, `traceroute`, `wake`, `ports`, `http`, `inspect`) are queued by the routes `/api/v1/network/...` of ARMOR-SERVER and reach the node in the answer to its message; the contract of the message and of the orders is in ARMOR-COMMON (111 conformance vectors). See [docs/MESSAGES.md](docs/MESSAGES.md) and [docs/USAGE.md](docs/USAGE.md).",
               "Las órdenes de Studio (`scan_now`, `ping`, `traceroute`, `wake`, `ports`, `http`, `inspect`) las encola el servidor en las rutas `/api/v1/network/...` de ARMOR-SERVER y llegan al nodo en la respuesta a su mensaje; el contrato del mensaje y de las órdenes está en ARMOR-COMMON (111 vectores de conformidad). Mira [docs/MESSAGES.md](docs/MESSAGES.md) y [docs/USAGE.md](docs/USAGE.md).",
               "Die Aufträge aus Studio (`scan_now`, `ping`, `traceroute`, `wake`, `ports`, `http`, `inspect`) reiht der Server über die Routen `/api/v1/network/...` von ARMOR-SERVER ein; sie erreichen den Knoten in der Antwort auf seine Nachricht; der Vertrag der Nachricht und der Aufträge liegt in ARMOR-COMMON (111 Konformitätsvektoren). Siehe [docs/MESSAGES.md](docs/MESSAGES.md) und [docs/USAGE.md](docs/USAGE.md).",
               "Les ordres de Studio (`scan_now`, `ping`, `traceroute`, `wake`, `ports`, `http`, `inspect`) sont mis en file par les routes `/api/v1/network/...` d'ARMOR-SERVER et arrivent au nœud dans la réponse à son message ; le contrat du message et des ordres est dans ARMOR-COMMON (111 vecteurs de conformité). Voir [docs/MESSAGES.md](docs/MESSAGES.md) et [docs/USAGE.md](docs/USAGE.md).",
               "Gli ordini da Studio (`scan_now`, `ping`, `traceroute`, `wake`, `ports`, `http`, `inspect`) sono messi in coda dalle rotte `/api/v1/network/...` di ARMOR-SERVER e arrivano al nodo nella risposta al suo messaggio; il contratto del messaggio e degli ordini è in ARMOR-COMMON (111 vettori di conformità). Vedi [docs/MESSAGES.md](docs/MESSAGES.md) e [docs/USAGE.md](docs/USAGE.md).",
               "Studio からのオーダー（`scan_now`、`ping`、`traceroute`、`wake`、`ports`、`http`、`inspect`）は ARMOR-SERVER の `/api/v1/network/...` ルートがキューに入れ、ノードのメッセージへの応答で届きます。メッセージとオーダーの契約は ARMOR-COMMON（適合ベクター 111 件）にあります。[docs/MESSAGES.md](docs/MESSAGES.md) と [docs/USAGE.md](docs/USAGE.md) を参照。",
               "来自 Studio 的指令（`scan_now`、`ping`、`traceroute`、`wake`、`ports`、`http`、`inspect`）由 ARMOR-SERVER 的 `/api/v1/network/...` 路由排队，并在对节点消息的响应中送达；消息与指令的契约在 ARMOR-COMMON（111 个一致性向量）。见 [docs/MESSAGES.md](docs/MESSAGES.md) 和 [docs/USAGE.md](docs/USAGE.md)。",
               "As ordens do Studio (`scan_now`, `ping`, `traceroute`, `wake`, `ports`, `http`, `inspect`) são postas em fila pelas rotas `/api/v1/network/...` do ARMOR-SERVER e chegam ao nó na resposta à sua mensagem; o contrato da mensagem e das ordens está no ARMOR-COMMON (111 vetores de conformidade). Veja [docs/MESSAGES.md](docs/MESSAGES.md) e [docs/USAGE.md](docs/USAGE.md).")

CFG = [
    ("`--node-id`", "network-1", T("the name of this node in the messages (lowercase letters, digits, `-` and `_`) | el nombre de este nodo en los mensajes (minúsculas, dígitos, `-` y `_`) | der Name dieses Knotens in den Nachrichten (Kleinbuchstaben, Ziffern, `-` und `_`) | le nom de ce nœud dans les messages (minuscules, chiffres, `-` et `_`) | il nome di questo nodo nei messaggi (minuscole, cifre, `-` e `_`) | メッセージ中のこのノードの名前（小文字、数字、`-`、`_`） | 此节点在消息中的名称（小写字母、数字、`-` 和 `_`） | o nome deste nó nas mensagens (minúsculas, dígitos, `-` e `_`)")),
    ("`--profile {quick,standard}`", "quick", T("17 or 44 ports per device; a new device is looked at at once, the others every quarter of an hour | 17 o 44 puertos por equipo; un equipo nuevo se mira al instante, los demás cada cuarto de hora | 17 oder 44 Ports je Gerät; ein neues Gerät wird sofort angesehen, die anderen alle Viertelstunde | 17 ou 44 ports par appareil ; un nouvel appareil est examiné aussitôt, les autres tous les quarts d'heure | 17 o 44 porte per dispositivo; un dispositivo nuovo si guarda subito, gli altri ogni quarto d'ora | 機器ごとに 17 または 44 ポート。新しい機器はすぐ、他は 15 分ごと | 每台设备 17 或 44 个端口；新设备立即查看，其余每刻钟一次 | 17 ou 44 portas por equipamento; um equipamento novo olha-se logo, os outros a cada quarto de hora")),
    ("`--no-ports`  `--skip IP`  `--cidr`", "-", T("no ports at all; an address never to probe; the network to scan (private, at most 1024 addresses) | sin puertos; una dirección que no sondear nunca; la red a escanear (privada, como mucho 1024 direcciones) | keine Ports; eine nie zu prüfende Adresse; das zu scannende Netz (privat, höchstens 1024 Adressen) | aucun port ; une adresse à ne jamais sonder ; le réseau à scanner (privé, 1024 adresses au plus) | nessuna porta; un indirizzo da non sondare mai; la rete da scansionare (privata, al massimo 1024 indirizzi) | ポートを見ない、決して調べないアドレス、スキャン対象ネットワーク（プライベートで 1024 アドレス以下） | 完全不查端口；永不探测的地址；要扫描的网络（私有，最多 1024 个地址） | sem portas; um endereço a nunca sondar; a rede a varrer (privada, no máximo 1024 endereços)")),
    ("`--scan-every`  `--internet-every`", "60 s  5 s", T("seconds between sweeps and between internet checks | segundos entre barridos y entre comprobaciones de internet | Sekunden zwischen Durchläufen und Internetprüfungen | secondes entre balayages et contrôles d'internet | secondi tra scansioni e controlli di internet | スイープとインターネット確認の間隔（秒） | 扫描与互联网检查的间隔秒数 | segundos entre varrimentos e verificações da internet")),
    ("`--server-url`  `--ingest-token`  `--mqtt-url`  `--mqtt-user`", "-", T("where it tells; the token of this node (Studio shows it) or the shared ingest token, never written to a file | adónde informa; el token de este nodo (Studio lo muestra) o el token de ingesta compartido, nunca escrito en un fichero | wohin gemeldet wird; das Token dieses Knotens (Studio zeigt es) oder das gemeinsame Ingest-Token, nie in eine Datei geschrieben | où il informe ; le jeton de ce nœud (Studio l'affiche) ou le jeton d'ingestion partagé, jamais écrit dans un fichier | dove riferisce; il token di questo nodo (Studio lo mostra) o il token di ingestione condiviso, mai scritto in un file | 通知先、このノードのトークン（Studio に表示）または共有の取り込みトークン（ファイルには書かない） | 上报到哪里；本节点的令牌（Studio 会显示）或共享采集令牌，绝不写入文件 | para onde informa; o token deste nó (o Studio mostra-o) ou o token de ingestão partilhado, nunca escrito num ficheiro")),
    ("`--data-dir`", "armor-network-data", T("where the inventory and the outages are kept between runs | dónde se guardan el inventario y las caídas entre ejecuciones | wo Inventar und Ausfälle zwischen Läufen liegen | où l'inventaire et les pannes sont gardés entre les exécutions | dove restano inventario e interruzioni tra le esecuzioni | 実行間でインベントリと障害を保持する場所 | 运行之间保存清单与中断记录的位置 | onde o inventário e as quedas ficam entre execuções")),
    ("`--validate`  `--no-public-info`  `--public-info-url`  `--dns-name`", "-", T("check each message against ARMOR-COMMON; the public-address look-up (off, its address, the name to check) | comprueba cada mensaje con ARMOR-COMMON; la consulta de la dirección pública (apagarla, su dirección, el nombre a comprobar) | jede Nachricht gegen ARMOR-COMMON prüfen; die Abfrage der öffentlichen Adresse (abschalten, ihre Adresse, der zu prüfende Name) | vérifie chaque message avec ARMOR-COMMON ; la consultation de l'adresse publique (la couper, son adresse, le nom à vérifier) | verifica ogni messaggio con ARMOR-COMMON; la ricerca dell'indirizzo pubblico (spegnerla, il suo indirizzo, il nome da verificare) | 各メッセージを ARMOR-COMMON で検査、公開アドレスの照会（無効化、そのアドレス、確認する名前） | 用 ARMOR-COMMON 检查每条消息；公网地址查询（关闭、其地址、要检查的名称） | verifica cada mensagem com o ARMOR-COMMON; a consulta do endereço público (desligá-la, o seu endereço, o nome a verificar)")),
]
CFG_NOTE = P("All of it is set by command-line flags (see [docs/USAGE.md](docs/USAGE.md), which also shows the systemd unit that keeps it running). An outage is called after three failed rounds and ended after two good ones; the first three sweeps only learn what is there.",
             "Todo se fija con opciones de línea de órdenes (mira [docs/USAGE.md](docs/USAGE.md), que muestra también la unidad systemd que lo mantiene en marcha). Una caída se declara tras tres rondas fallidas y termina tras dos buenas; los tres primeros barridos solo aprenden lo que hay.",
             "Alles wird mit Kommandozeilenoptionen gesetzt (siehe [docs/USAGE.md](docs/USAGE.md), das auch die systemd-Einheit zeigt, die es am Laufen hält). Ein Ausfall wird nach drei fehlgeschlagenen Runden festgestellt und nach zwei guten beendet; die ersten drei Durchläufe lernen nur, was da ist.",
             "Tout se règle par des options de ligne de commande (voir [docs/USAGE.md](docs/USAGE.md), qui montre aussi l'unité systemd qui le maintient en marche). Une panne est déclarée après trois rondes ratées et terminée après deux bonnes ; les trois premiers balayages apprennent seulement ce qui est là.",
             "Tutto si imposta con opzioni da riga di comando (vedi [docs/USAGE.md](docs/USAGE.md), che mostra anche l'unità systemd che lo tiene in funzione). Un'interruzione si dichiara dopo tre giri falliti e termina dopo due buoni; le prime tre scansioni imparano soltanto cosa c'è.",
             "設定はすべてコマンドラインオプションで行います（常駐させる systemd ユニットも示す [docs/USAGE.md](docs/USAGE.md) を参照）。障害は 3 回連続の失敗で判定し、2 回の成功で終了とします。最初の 3 回のスイープは何があるかを学ぶだけです。",
             "全部通过命令行选项设置（见 [docs/USAGE.md](docs/USAGE.md)，其中也给出让它常驻运行的 systemd 单元）。连续三轮失败才判定为中断，连续两轮成功才算结束；前三次扫描只用来了解有什么。",
             "Tudo se define com opções da linha de comandos (veja [docs/USAGE.md](docs/USAGE.md), que mostra também a unidade systemd que o mantém a correr). Uma queda declara-se após três rondas falhadas e termina após duas boas; os três primeiros varrimentos só aprendem o que lá está.")

QUICK_LEAD = P("**Requirements:** Python 3.11+ (standard library only) and a machine on the network to be watched (Linux, Windows or macOS).", "**Requisitos:** Python 3.11+ (solo biblioteca estándar) y una máquina en la red a vigilar (Linux, Windows o macOS).", "**Voraussetzungen:** Python 3.11+ (nur Standardbibliothek) und ein Rechner im zu überwachenden Netz (Linux, Windows oder macOS).",
               "**Prérequis :** Python 3.11+ (bibliothèque standard seule) et une machine sur le réseau à surveiller (Linux, Windows ou macOS).", "**Requisiti:** Python 3.11+ (solo libreria standard) e una macchina nella rete da sorvegliare (Linux, Windows o macOS).", "**要件：** Python 3.11+（標準ライブラリのみ）と、監視対象ネットワーク上のマシン（Linux、Windows、macOS）。",
               "**要求：** Python 3.11+（仅标准库）和被监视网络中的一台机器（Linux、Windows 或 macOS）。", "**Requisitos:** Python 3.11+ (só biblioteca padrão) e uma máquina na rede a vigiar (Linux, Windows ou macOS).")
QUICK_CODE = [
    ("python -m unittest discover -s tests", T("187 tests: parsers with real samples, the guard on what may be probed, the inventory, the internet, the whole agent against a scripted house | 187 pruebas: analizadores con muestras reales, la guarda de lo que se puede sondear, el inventario, internet, el agente completo contra una casa guionizada | 187 Tests: Parser mit echten Proben, die Sperre dessen, was geprüft werden darf, das Inventar, das Internet, der ganze Agent gegen ein geskriptetes Haus | 187 tests : analyseurs avec échantillons réels, la garde de ce qu'on peut sonder, l'inventaire, internet, l'agent entier face à une maison scriptée | 187 test: parser con campioni reali, la guardia su cosa si può sondare, l'inventario, internet, l'intero agente contro una casa guidata | 187 件：実サンプルのパーサ、調べてよい範囲のガード、インベントリ、インターネット、スクリプト版の家に対するエージェント全体 | 187 项：用真实样本的解析器、可探测范围的防护、清单、互联网、对脚本化房子运行的完整代理 | 187 testes: analisadores com amostras reais, a guarda do que se pode sondar, o inventário, a internet, o agente completo contra uma casa com guião")),
    ("python -m armor_network scan", T("look at the network once and print it (only the private network of this machine) | mira la red una vez y la imprime (solo la red privada de esta máquina) | das Netz einmal ansehen und ausgeben (nur das private Netz dieses Rechners) | regarde le réseau une fois et l'imprime (seulement le réseau privé de cette machine) | guarda la rete una volta e la stampa (solo la rete privata di questa macchina) | ネットワークを 1 回調べて表示（このマシンのプライベートネットワークのみ） | 查看一次网络并打印（仅本机所在的私有网络） | olha para a rede uma vez e imprime-a (só a rede privada desta máquina)")),
    ("python -m armor_network watch --server-url http://127.0.0.1:8080 --ingest-token ...", T("keep watching and tell ARMOR-SERVER | sigue vigilando e informa a ARMOR-SERVER | weiter beobachten und ARMOR-SERVER melden | continue de surveiller et informe ARMOR-SERVER | continua a sorvegliare e informa ARMOR-SERVER | 監視を続けて ARMOR-SERVER に通知 | 持续监视并通知 ARMOR-SERVER | continua a vigiar e informa o ARMOR-SERVER")),
    ("python -m armor_network demo --count 3", T("a made-up house: nothing on any network is touched | una casa inventada: no se toca ninguna red | ein erfundenes Haus: kein Netz wird berührt | une maison fictive : aucun réseau n'est touché | una casa inventata: nessuna rete viene toccata | 架空の家：実ネットワークには触れない | 虚构的房子：不碰任何网络 | uma casa inventada: nenhuma rede é tocada")),
    ("python tools/fetch_oui.py", T("refresh the table of makers from the IEEE register (a person runs it, now and then) | renueva la tabla de fabricantes desde el registro IEEE (lo ejecuta una persona, de vez en cuando) | die Herstellertabelle aus dem IEEE-Register erneuern (von Hand, ab und zu) | rafraîchit la table des fabricants depuis le registre IEEE (lancé par une personne, de temps en temps) | aggiorna la tabella dei produttori dal registro IEEE (la lancia una persona, ogni tanto) | IEEE 登録簿からメーカー表を更新（人が時々実行） | 从 IEEE 注册表刷新厂商表（由人工不定期运行） | renova a tabela de fabricantes a partir do registo IEEE (uma pessoa executa-o, de vez em quando)")),
]
QUICK_AFTER = P("See the [usage](docs/USAGE.md) and the [design](docs/DESIGN.md).", "Mira el [uso](docs/USAGE.md) y el [diseño](docs/DESIGN.md).", "Siehe die [Benutzung](docs/USAGE.md) und den [Entwurf](docs/DESIGN.md).", "Voir l'[usage](docs/USAGE.md) et la [conception](docs/DESIGN.md).", "Vedi l'[uso](docs/USAGE.md) e il [progetto](docs/DESIGN.md).", "[使い方](docs/USAGE.md)と[設計](docs/DESIGN.md)を参照してください。", "请参阅[用法](docs/USAGE.md)和[设计](docs/DESIGN.md)。", "Consulte a [utilização](docs/USAGE.md) e o [desenho](docs/DESIGN.md).")

TEST_TABLE = [
    ("`test_network.py`", "56", T("the parsers with real samples, the guard on what may be probed, the inventory, the internet and the agent against a scripted house | los analizadores con muestras reales, la guarda de lo que se puede sondear, el inventario, internet y el agente contra una casa guionizada | die Parser mit echten Proben, die Sperre dessen, was geprüft werden darf, das Inventar, das Internet und der Agent gegen ein geskriptetes Haus | les analyseurs avec échantillons réels, la garde de ce qu'on peut sonder, l'inventaire, internet et l'agent face à une maison scriptée | i parser con campioni reali, la guardia su cosa si può sondare, l'inventario, internet e l'agente contro una casa guidata | 実サンプルのパーサ、調べてよい範囲のガード、インベントリ、インターネット、スクリプト版の家に対するエージェント | 用真实样本的解析器、可探测范围的防护、清单、互联网以及对脚本化房子运行的代理 | os analisadores com amostras reais, a guarda do que se pode sondar, o inventário, a internet e o agente contra uma casa com guião")),
    ("`test_system_io_layer.py`  `test_system_io.py`", "39", T("the real-network layer: neighbours, echoes, TCP, DNS | la capa de red real: vecinos, ecos, TCP, DNS | die Schicht des echten Netzes: Nachbarn, Echos, TCP, DNS | la couche réseau réel : voisins, échos, TCP, DNS | il livello della rete reale: vicini, echi, TCP, DNS | 実ネットワーク層：近隣、エコー、TCP、DNS | 真实网络层：邻居、回显、TCP、DNS | a camada da rede real: vizinhos, ecos, TCP, DNS")),
    ("`test_orders.py`  `test_orders_edges.py`", "56", T("the orders from Studio and their limits | las órdenes de Studio y sus límites | die Aufträge aus Studio und ihre Grenzen | les ordres de Studio et leurs limites | gli ordini da Studio e i loro limiti | Studio からのオーダーとその上限 | 来自 Studio 的指令及其限制 | as ordens do Studio e os seus limites")),
    ("`test_cli_commands.py`", "20", T("the command line | la línea de órdenes | die Kommandozeile | la ligne de commande | la riga di comando | コマンドライン | 命令行 | a linha de comandos")),
    ("`test_mqtt_out.py`  `test_seal.py`", "10", T("the MQTT output and the sealed logins | la salida MQTT y los accesos sellados | die MQTT-Ausgabe und die versiegelten Logins | la sortie MQTT et les identifiants scellés | l'uscita MQTT e gli accessi sigillati | MQTT 出力と封印した認証情報 | MQTT 输出与密封凭据 | a saída MQTT e as credenciais seladas")),
    ("`test_typing_behaviour.py`", "6", T("the behaviour the type annotations keep: the scan guard, the order parser and the vendor tables | el comportamiento que conservan las anotaciones de tipos: la guarda del escaneo, el analizador de órdenes y las tablas de fabricantes | das Verhalten, das die Typannotationen beibehalten: die Scan-Schranke, der Auftragsparser und die Herstellertabellen | le comportement que conservent les annotations de types : la garde du balayage, l'analyseur d'ordres et les tables de fabricants | il comportamento che le annotazioni di tipo conservano: la guardia della scansione, l'analizzatore degli ordini e le tabelle dei produttori | 型アノテーションが保つ動作：スキャンのガード、オーダーのパーサー、ベンダー表 | 类型注解所保持的行为：扫描保护、指令解析器和厂商表 | o comportamento que as anotações de tipos mantêm: a guarda da varredura, o analisador de ordens e as tabelas de fabricantes")),
]
TEST_NOTE = P("GitHub Actions runs the A.R.M.O.R. baseline on every push and pull request: the validation of the manifest, version, changelog and README parity, then the project's own build and tests. The sources also pass the type checker: `python -m mypy` (configured in `pyproject.toml`) reports nothing, and `test_typing_behaviour.py` fixes the behaviour the annotations keep.",
              "GitHub Actions ejecuta la base de A.R.M.O.R. en cada push y pull request: la validación del manifiesto, la versión, el registro de cambios y la paridad de los README, y luego la compilación y las pruebas del propio proyecto. Los fuentes también pasan el comprobador de tipos: `python -m mypy` (configurado en `pyproject.toml`) no informa de nada, y `test_typing_behaviour.py` fija el comportamiento que conservan las anotaciones.",
              "GitHub Actions führt bei jedem Push und Pull Request die A.R.M.O.R.-Basis aus: die Prüfung von Manifest, Version, Änderungsprotokoll und README-Parität, dann den eigenen Build und die eigenen Tests des Projekts. Die Quellen bestehen auch die Typprüfung: `python -m mypy` (in `pyproject.toml` konfiguriert) meldet nichts, und `test_typing_behaviour.py` hält das Verhalten fest, das die Annotationen beibehalten.",
              "GitHub Actions exécute la base A.R.M.O.R. à chaque push et pull request : la validation du manifeste, de la version, du journal des modifications et de la parité des README, puis le build et les tests propres au projet. Les sources passent aussi le vérificateur de types : `python -m mypy` (configuré dans `pyproject.toml`) ne signale rien, et `test_typing_behaviour.py` fixe le comportement que conservent les annotations.",
              "GitHub Actions esegue la base A.R.M.O.R. a ogni push e pull request: la validazione di manifesto, versione, registro delle modifiche e parità dei README, poi la compilazione e i test del progetto. Anche i sorgenti superano il controllo dei tipi: `python -m mypy` (configurato in `pyproject.toml`) non segnala nulla, e `test_typing_behaviour.py` fissa il comportamento che le annotazioni conservano.",
              "GitHub Actions は push と pull request のたびに A.R.M.O.R. の基本検査（マニフェスト、バージョン、変更履歴、README の一致）と、プロジェクト自身のビルドとテストを実行します。 ソースは型チェッカーも通ります。`python -m mypy`（`pyproject.toml` で設定）は何も報告せず、`test_typing_behaviour.py` がアノテーションの保つ動作を固定します。",
              "GitHub Actions 在每次推送和拉取请求时运行 A.R.M.O.R. 基线：清单、版本、更新日志和 README 一致性的校验，然后是项目自身的构建和测试。 源代码也通过类型检查：`python -m mypy`（在 `pyproject.toml` 中配置）没有任何报告，`test_typing_behaviour.py` 固定了注解所保持的行为。",
              "O GitHub Actions executa a base do A.R.M.O.R. em cada push e pull request: a validação do manifesto, da versão, do registo de alterações e da paridade dos README, e depois a compilação e os testes do próprio projeto. As fontes também passam o verificador de tipos: `python -m mypy` (configurado em `pyproject.toml`) não reporta nada, e `test_typing_behaviour.py` fixa o comportamento que as anotações mantêm.")

BUILD = P("It is plain Python: nothing to compile. The version lives in `pyproject.toml`, in `armor.project.json` and in the README badge (read from the manifest); each version has its entry in [CHANGELOG.md](CHANGELOG.md). Releases are published on GitHub.",
          "Es Python puro: no hay nada que compilar. La versión vive en `pyproject.toml`, en `armor.project.json` y en la insignia del README (leída del manifiesto); cada versión tiene su entrada en [CHANGELOG.md](CHANGELOG.md). Las versiones se publican en GitHub.",
          "Es ist reines Python: Es gibt nichts zu kompilieren. Die Version steht in `pyproject.toml`, in `armor.project.json` und im README-Badge (aus dem Manifest gelesen); jede Version hat ihren Eintrag in [CHANGELOG.md](CHANGELOG.md). Releases werden auf GitHub veröffentlicht.",
          "C'est du Python pur : rien à compiler. La version se trouve dans `pyproject.toml`, dans `armor.project.json` et dans le badge du README (lu depuis le manifeste) ; chaque version a son entrée dans [CHANGELOG.md](CHANGELOG.md). Les versions sont publiées sur GitHub.",
          "È Python puro: nulla da compilare. La versione risiede in `pyproject.toml`, in `armor.project.json` e nel badge del README (letto dal manifesto); ogni versione ha la sua voce in [CHANGELOG.md](CHANGELOG.md). Le versioni sono pubblicate su GitHub.",
          "純粋な Python なので、コンパイルするものはありません。バージョンは `pyproject.toml`、`armor.project.json`、README のバッジ（マニフェストから読み取り）にあり、各バージョンには [CHANGELOG.md](CHANGELOG.md) にエントリーがあります。リリースは GitHub で公開されます。",
          "这是纯 Python：无需编译。版本记录在 `pyproject.toml`、`armor.project.json` 和 README 徽章中（读取自清单）；每个版本在 [CHANGELOG.md](CHANGELOG.md) 中都有对应条目。发布版本发布在 GitHub 上。",
          "É Python puro: não há nada para compilar. A versão está em `pyproject.toml`, em `armor.project.json` e no emblema do README (lido do manifesto); cada versão tem a sua entrada em [CHANGELOG.md](CHANGELOG.md). As versões são publicadas no GitHub.")

TROUBLE = [
    (T("`... is not a private network` or `... has N addresses; at most 1024`  | `... is not a private network` o `... has N addresses; at most 1024` | `... is not a private network` oder `... has N addresses; at most 1024` | `... is not a private network` ou `... has N addresses; at most 1024` | `... is not a private network` o `... has N addresses; at most 1024` | `... is not a private network` または `... has N addresses; at most 1024` | `... is not a private network` 或 `... has N addresses; at most 1024` | `... is not a private network` ou `... has N addresses; at most 1024`".replace("  |", " |")),
     T("`--cidr` names a public range or one larger than a /22 | `--cidr` nombra un rango público o mayor que un /22 | `--cidr` nennt einen öffentlichen Bereich oder einen größer als /22 | `--cidr` désigne une plage publique ou plus grande qu'un /22 | `--cidr` indica un intervallo pubblico o più grande di un /22 | `--cidr` が公開範囲または /22 より大きい範囲を指している | `--cidr` 指定了公网网段或大于 /22 的网段 | `--cidr` indica um intervalo público ou maior que um /22"),
     T("use a private range of at most 1024 addresses | usa un rango privado de como mucho 1024 direcciones | einen privaten Bereich mit höchstens 1024 Adressen nehmen | utilisez une plage privée d'au plus 1024 adresses | usa un intervallo privato di al massimo 1024 indirizzi | 1024 アドレス以下のプライベート範囲を使う | 使用最多 1024 个地址的私有网段 | use um intervalo privado de no máximo 1024 endereços")),
    (T("Few or no devices found | Pocos equipos o ninguno | Wenige oder keine Geräte gefunden | Peu ou pas d'appareils trouvés | Pochi o nessun dispositivo trovato | 機器がほとんど、または全く見つからない | 找到的设备很少或没有 | Poucos ou nenhuns equipamentos encontrados"),
     T("the system's neighbour table is filled by a poke of every address, which needs the permission to ping or to read it | la tabla de vecinos del sistema se llena sondeando cada dirección, y eso necesita permiso para hacer ping o leerla | die Nachbartabelle des Systems füllt sich durch Anstoßen jeder Adresse, was die Erlaubnis zum Pingen oder Lesen braucht | la table de voisins du système se remplit en sondant chaque adresse, ce qui exige la permission de ping ou de lecture | la tabella dei vicini del sistema si riempie sondando ogni indirizzo, e serve il permesso di ping o di lettura | システムの近隣テーブルは全アドレスへの呼びかけで埋まり、ping や読み取りの権限が必要 | 系统邻居表靠向每个地址探测来填充，需要 ping 或读取权限 | a tabela de vizinhos do sistema enche-se sondando cada endereço, o que precisa de permissão para ping ou leitura"),
     T("run it with the permissions of a user that may ping and read the neighbour table | ejecútalo con los permisos de un usuario que pueda hacer ping y leer la tabla de vecinos | mit den Rechten eines Benutzers ausführen, der pingen und die Nachbartabelle lesen darf | lancez-le avec les droits d'un utilisateur pouvant faire un ping et lire la table de voisins | eseguilo con i permessi di un utente che può fare ping e leggere la tabella dei vicini | ping と近隣テーブルの読み取りができるユーザー権限で実行 | 以可 ping 并读取邻居表的用户权限运行 | execute-o com as permissões de um utilizador que possa fazer ping e ler a tabela de vizinhos")),
    (T("A fragile device misbehaves when scanned | Un equipo frágil se porta mal al escanearlo | Ein empfindliches Gerät verhält sich beim Scannen schlecht | Un appareil fragile se comporte mal quand on le scanne | Un dispositivo fragile si comporta male alla scansione | 壊れやすい機器がスキャンで不調になる | 脆弱设备在扫描时异常 | Um equipamento frágil porta-se mal ao ser varrido"),
     T("it does not like the ports being tried | no le gusta que se prueben puertos | es mag die Port-Versuche nicht | il n'aime pas qu'on essaie des ports | non gradisce che si provino le porte | ポートへの接続を嫌う | 不喜欢被尝试端口 | não gosta que se experimentem portas"),
     T("add `--skip <address>` (repeatable) or `--no-ports` | añade `--skip <dirección>` (repetible) o `--no-ports` | `--skip <Adresse>` (wiederholbar) oder `--no-ports` ergänzen | ajoutez `--skip <adresse>` (répétable) ou `--no-ports` | aggiungi `--skip <indirizzo>` (ripetibile) o `--no-ports` | `--skip <アドレス>`（複数可）または `--no-ports` を追加 | 添加 `--skip <地址>`（可重复）或 `--no-ports` | acrescente `--skip <endereço>` (repetível) ou `--no-ports`")),
    (T("Studio never gets a message | Studio nunca recibe un mensaje | Studio erhält nie eine Nachricht | Studio ne reçoit jamais de message | Studio non riceve mai un messaggio | Studio にメッセージが届かない | Studio 一直收不到消息 | O Studio nunca recebe uma mensagem"),
     T("the server cannot be reached or refuses the token (the problem is counted like any other: `unreachable`, `unauthorized`) | no se llega al servidor o este rechaza el token (el problema se cuenta como cualquier otro: `unreachable`, `unauthorized`) | der Server ist nicht erreichbar oder lehnt das Token ab (das Problem wird wie jedes andere gezählt: `unreachable`, `unauthorized`) | le serveur est injoignable ou refuse le jeton (le problème est compté comme les autres : `unreachable`, `unauthorized`) | il server non è raggiungibile o rifiuta il token (il problema si conta come gli altri: `unreachable`, `unauthorized`) | サーバーに届かない、またはトークンを拒否（他と同様に問題として数える：`unreachable`、`unauthorized`） | 无法连接服务器或服务器拒绝令牌（和其他问题一样被计数：`unreachable`、`unauthorized`） | o servidor não é alcançável ou recusa o token (o problema conta-se como qualquer outro: `unreachable`, `unauthorized`)"),
     T("check `--server-url` and the token (the one of this node that Studio shows, or the shared ingest token) | revisa `--server-url` y el token (el de este nodo que muestra Studio, o el token de ingesta compartido) | `--server-url` und das Token prüfen (das dieses Knotens, das Studio zeigt, oder das gemeinsame Ingest-Token) | vérifiez `--server-url` et le jeton (celui de ce nœud que Studio affiche, ou le jeton d'ingestion partagé) | controlla `--server-url` e il token (quello di questo nodo che Studio mostra, o il token di ingestione condiviso) | `--server-url` とトークン（Studio が示すこのノードのもの、または共有の取り込みトークン）を確認 | 检查 `--server-url` 和令牌（Studio 显示的本节点令牌，或共享采集令牌） | verifique `--server-url` e o token (o deste nó que o Studio mostra, ou o token de ingestão partilhado)")),
]

ROADMAP = P(
    "**Known limits today**\n\n* It has not watched a whole house for weeks.\n* It only asks the router and never configures it; what a device is (kind, system, maker) is a guess.\n* It does not capture packets, so it cannot see who talks to whom; traffic per device and intrusion detection in the strict sense need the router's counters or a mirror port.\n* No independent security review.\n\n**Next**\n\n* The router's own counters (traffic per device), packet capture and weeks on a real network.\n* Controlling something (blocking a device, closing a port, changing the router) is not planned without a documented risk review.",
    "**Límites conocidos hoy**\n\n* No ha vigilado una casa entera durante semanas.\n* Solo pregunta al router y nunca lo configura; lo que es un equipo (tipo, sistema, fabricante) es una suposición.\n* No captura paquetes, así que no ve quién habla con quién; el tráfico por equipo y la detección de intrusos en sentido estricto necesitan los contadores del router o un puerto espejo.\n* Sin revisión de seguridad independiente.\n\n**Lo siguiente**\n\n* Los contadores propios del router (tráfico por equipo), la captura de paquetes y semanas en una red real.\n* Controlar algo (bloquear un equipo, cerrar un puerto, cambiar el router) no está previsto sin una revisión de riesgos documentada.",
    "**Bekannte Grenzen heute**\n\n* Es hat noch nie ein ganzes Haus über Wochen überwacht.\n* Es fragt nur den Router und konfiguriert ihn nie; was ein Gerät ist (Art, System, Hersteller), ist eine Vermutung.\n* Es zeichnet keine Pakete auf und sieht daher nicht, wer mit wem spricht; Verkehr je Gerät und Einbruchserkennung im strengen Sinn brauchen die Zähler des Routers oder einen Spiegelport.\n* Keine unabhängige Sicherheitsprüfung.\n\n**Als Nächstes**\n\n* Die eigenen Zähler des Routers (Verkehr je Gerät), Paketmitschnitt und Wochen in einem echten Netz.\n* Etwas zu steuern (ein Gerät sperren, einen Port schließen, den Router ändern) ist ohne dokumentierte Risikoprüfung nicht geplant.",
    "**Limites connues aujourd'hui**\n\n* Il n'a pas surveillé une maison entière pendant des semaines.\n* Il ne fait qu'interroger le routeur et ne le configure jamais ; ce qu'est un appareil (type, système, fabricant) est une supposition.\n* Il ne capture pas de paquets, donc ne voit pas qui parle à qui ; le trafic par appareil et la détection d'intrusion au sens strict demandent les compteurs du routeur ou un port miroir.\n* Pas de revue de sécurité indépendante.\n\n**Prochainement**\n\n* Les compteurs propres du routeur (trafic par appareil), la capture de paquets et des semaines sur un vrai réseau.\n* Contrôler quelque chose (bloquer un appareil, fermer un port, modifier le routeur) n'est pas prévu sans une revue de risques documentée.",
    "**Limiti noti oggi**\n\n* Non ha sorvegliato una casa intera per settimane.\n* Interroga solo il router e non lo configura mai; ciò che è un dispositivo (tipo, sistema, produttore) è una supposizione.\n* Non cattura pacchetti, quindi non vede chi parla con chi; il traffico per dispositivo e il rilevamento di intrusioni in senso stretto richiedono i contatori del router o una porta mirror.\n* Nessuna revisione di sicurezza indipendente.\n\n**Prossimi passi**\n\n* I contatori propri del router (traffico per dispositivo), la cattura di pacchetti e settimane su una rete reale.\n* Controllare qualcosa (bloccare un dispositivo, chiudere una porta, cambiare il router) non è previsto senza una revisione dei rischi documentata.",
    "**現時点の既知の制限**\n\n* 家全体を何週間も監視したことはありません。\n* ルーターに問い合わせるだけで設定は一切せず、機器が何か（種類、システム、メーカー）は推測です。\n* パケットを取得しないので誰が誰と通信しているかは見えません。機器ごとの通信量や厳密な侵入検知にはルーターのカウンターかミラーポートが必要です。\n* 第三者によるセキュリティレビューはありません。\n\n**今後**\n\n* ルーター自身のカウンター（機器ごとの通信量）、パケット取得、実ネットワークでの数週間の運用。\n* 何かを制御する（機器のブロック、ポートの閉鎖、ルーターの変更）ことは、文書化したリスクレビューなしには予定していません。",
    "**当前已知限制**\n\n* 还没有对整栋房子连续监视数周。\n* 它只向路由器查询，从不配置路由器；设备是什么（类型、系统、厂商）只是推测。\n* 它不抓包，因此看不到谁在和谁通信；按设备统计流量和严格意义上的入侵检测需要路由器的计数器或镜像端口。\n* 没有独立的安全审查。\n\n**下一步**\n\n* 路由器自身的计数器（按设备的流量）、抓包以及在真实网络上运行数周。\n* 在没有文档化风险评审的情况下，不计划控制任何东西（封锁设备、关闭端口、修改路由器）。",
    "**Limites conhecidos hoje**\n\n* Nunca vigiou uma casa inteira durante semanas.\n* Só pergunta ao router e nunca o configura; o que um equipamento é (tipo, sistema, fabricante) é uma suposição.\n* Não captura pacotes, por isso não vê quem fala com quem; o tráfego por equipamento e a deteção de intrusão em sentido estrito precisam dos contadores do router ou de uma porta espelho.\n* Sem revisão de segurança independente.\n\n**A seguir**\n\n* Os contadores do próprio router (tráfego por equipamento), a captura de pacotes e semanas numa rede real.\n* Controlar algo (bloquear um equipamento, fechar uma porta, mudar o router) não está previsto sem uma revisão de riscos documentada.")

DOCS = [
    P("[Design](docs/DESIGN.md): how the node looks, remembers and decides", "[Diseño](docs/DESIGN.md): cómo mira, recuerda y decide el nodo", "[Entwurf](docs/DESIGN.md): wie der Knoten beobachtet, sich erinnert und entscheidet", "[Conception](docs/DESIGN.md) : comment le nœud regarde, se souvient et décide", "[Progetto](docs/DESIGN.md): come il nodo guarda, ricorda e decide", "[設計](docs/DESIGN.md)：ノードの観察、記憶、判断の仕組み", "[设计](docs/DESIGN.md)：节点如何观察、记忆和决策", "[Desenho](docs/DESIGN.md): como o nó olha, recorda e decide"),
    P("[Safety](docs/SAFETY.md): what it may touch and what it never does", "[Seguridad](docs/SAFETY.md): qué puede tocar y qué nunca hace", "[Sicherheit](docs/SAFETY.md): was es berühren darf und was nie", "[Sécurité](docs/SAFETY.md) : ce qu'il peut toucher et ce qu'il ne fait jamais", "[Sicurezza](docs/SAFETY.md): cosa può toccare e cosa non fa mai", "[安全](docs/SAFETY.md)：触れてよいものと決してしないこと", "[安全](docs/SAFETY.md)：它可以触碰什么，绝不做什么", "[Segurança](docs/SAFETY.md): o que pode tocar e o que nunca faz"),
    P("[Usage](docs/USAGE.md): the commands, the flags and the systemd unit", "[Uso](docs/USAGE.md): las órdenes, las opciones y la unidad systemd", "[Benutzung](docs/USAGE.md): die Befehle, die Optionen und die systemd-Einheit", "[Usage](docs/USAGE.md) : les commandes, les options et l'unité systemd", "[Uso](docs/USAGE.md): i comandi, le opzioni e l'unità systemd", "[使い方](docs/USAGE.md)：コマンド、オプション、systemd ユニット", "[用法](docs/USAGE.md)：命令、选项与 systemd 单元", "[Utilização](docs/USAGE.md): os comandos, as opções e a unidade systemd"),
    P("[Messages](docs/MESSAGES.md): the message of the node and its orders", "[Mensajes](docs/MESSAGES.md): el mensaje del nodo y sus órdenes", "[Nachrichten](docs/MESSAGES.md): die Nachricht des Knotens und seine Aufträge", "[Messages](docs/MESSAGES.md) : le message du nœud et ses ordres", "[Messaggi](docs/MESSAGES.md): il messaggio del nodo e i suoi ordini", "[メッセージ](docs/MESSAGES.md)：ノードのメッセージとオーダー", "[消息](docs/MESSAGES.md)：节点的消息及其指令", "[Mensagens](docs/MESSAGES.md): a mensagem do nó e as suas ordens"),
]


def build_lg(lg):
    bullets = "\n".join(f"* {b}" for b in L(lg, "bullets"))
    body = {
        "overview": bullets,
        "role": f"{L(lg, 'fit')}\n\n{table(lg, 'talks', ROLE_TABLE)}",
        "architecture": arch(lg, "ARMOR-NETWORK", "ARMOR-NETWORK architecture: the local network it looks at, the modules of the node and what it tells the server, Studio and the broker", None),
        "security": table(lg, "threat", SECURITY_ROWS) + "\n\n" + SEC_TAIL[lg],
        "interfaces": table(lg, "route", IFACE) + "\n\n" + IFACE_NOTE[lg],
        "configuration": table(lg, "setting", CFG) + "\n\n" + CFG_NOTE[lg],
        "quickstart": f"{QUICK_LEAD[lg]}\n\n" + code(lg, QUICK_CODE) + "\n\n" + QUICK_AFTER[lg],
        "testing": code(lg, [("python -m unittest discover -s tests", T("187 tests | 187 pruebas | 187 Tests | 187 tests | 187 test | 187 件 | 187 项 | 187 testes")), "python -I tools/armor_ci_validate.py"]) + "\n\n" + table(lg, "tests", TEST_TABLE) + "\n\n" + TEST_NOTE[lg],
        "build": BUILD[lg],
        "troubleshooting": table(lg, "trouble", TROUBLE),
        "structure": structure(lg, "ARMOR-NETWORK", tree=TREE[lg]),
        "roadmap": ROADMAP[lg],
    }
    return text_for(lg, tagline=L(lg, "tagline"), honest=L(lg, "honest"), glance=GLANCE, status={k: fix(v) for k, v in LEGACY[lg]["status"].items()}, docs=DOCS, contributing_first=CONTRIB, body=body)


TEXT = {lg: build_lg(lg) for lg in LGS}
