# The facts that do not depend on the language, and the words of every language, of ARMOR-NETWORK.
# Copyright (C) 2026 JuanenRac (Electro Hobby 3D). GPL-3.0-or-later.

FACTS = {
 "emoji": "🛰️",
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
   "181",
   "00E5FF"
  ]
 ],
 "diagram": "",
 "build": "```bash\npython -m unittest discover -s tests                  # 181 tests: the parsers with real samples, the guard on what may be probed, the inventory, the internet, the whole agent against a scripted house\npython -m armor_network scan                          # look at the network once and print it (only the private network of this machine)\npython -m armor_network watch --server-url http://127.0.0.1:8080 --ingest-token ...    # keep watching and tell ARMOR-SERVER\npython -m armor_network demo --count 3                # a made-up house: nothing on any network is touched\npython tools/fetch_oui.py                             # refresh the table of makers from the IEEE register (run by a person, now and then)\n```",
 "structure": "```text\nARMOR-NETWORK/\n├── src/armor_network/  ipnet (what may be probed), oui (makers), neighbors + parsers + dnswire (what the system and the devices say), services (ports and guesses), inventory (devices and their events),\n│                       internet (the outage state machine), agent (what to look at and how often), system_io (the real network), sim_io (a scripted one), publisher, cli\n│   └── data/           oui.tsv.gz, the IEEE register of makers\n├── tools/              fetch_oui.py\n├── tests/              test_network.py\n├── docs/               DESIGN, SAFETY, USAGE, MESSAGES\n└── images/             brand assets\n```",
 "tests": "181 (`python -m unittest discover -s tests`)",
 "requirements": [
  "Python 3.11+ (standard library only)",
  "a machine on the network to be watched (Linux, Windows or macOS)"
 ]
}

TEXT = {
 "en": {
  "tagline": "Watches the local network: the devices on it, whether the internet is there, what changes and what is new (a Python program with no dependencies; it runs on a machine of the network and reports to ARMOR-SERVER)",
  "honest": "The scanner, the inventory that tells what changed, the internet check, the public-address look-up, the orders from Studio and the sealed logins are tested on a computer against a scripted network (181 tests; every message is accepted by ARMOR-COMMON's contract), and the program runs as a service on the CM5 test bench, watching the real network the bench is on (a router, the phones and nodes of the house). It has not watched a whole house for weeks, it only asks the router and never configures it, and what a device is (its kind, its system, its maker) is a guess. It does not capture packets: it cannot see who talks to whom, and traffic per device and intrusion detection in the strict sense need the router's counters or a mirror port, which is a later step.",
  "bullets": [
   "**What is on the network:** the neighbour table of the machine, a poke of every address so that it fills, an echo to each device found (latency and TTL) and what devices announce about themselves (mDNS, UPnP, NetBIOS, reverse DNS). For each device: address, MAC, maker (from the IEEE register of 40,000 blocks), name, kind, system, open ports with what each says, and when it was first and last seen.",
   "**Ports:** a TCP connection to 17 (or 44) ports of each device, twelve at a time, reading at most a few hundred bytes of what answers; never a login, never an exploit. A new device is looked at at once, the others every quarter of an hour.",
   "**What changes:** a device that appears (the first three sweeps only learn), goes quiet or comes back, changes its address, a port that opens or closes, and two machines answering for one address (the router's above all). Every event has an id, so it is told once.",
   "**The internet:** every few seconds an echo to the router, a TCP connection, two DNS questions to chosen resolvers and a web page. An outage takes three rounds to be called one and two to be over, is dated from its first failed round and counted to the first good one, and says whose fault it is: the provider's (the router answers and nothing beyond it does) or this side's (the router does not answer either). Latency, loss and the outages of the last 24 hours.",
   "**It only looks at your own network:** it refuses any address that is not private (10/8, 172.16/12, 192.168/16) and any range larger than a /22; a skip list keeps it away from what is fragile; nothing is sent to a device that is not a question.",
   "**The message** `armor/network/<node>/state`: the interface, the internet, every device and the latest events; it is in the shared contract (330 vectors) and carries findings, never commands. `python -m armor_network scan` prints it as a table, `watch` tells ARMOR-SERVER, `demo` plays a made-up house (a new device joins, a camera opens Telnet, the internet falls and comes back, someone answers for the router) without touching any network.",
   "**Where it shows:** the Network menu of ARMOR-STUDIO (the devices, the internet with its outages and latency, the traffic and the events; an administrator names devices and marks the known ones, which quiets the alarm of a new device), the Network Designer (the drawing of the house's network, compared with what was found, and able to draw it) and the Network screen of the Android app. ARMOR-SERVER raises the alarms.",
   "**Orders from Studio:** a sweep now, a ping, a traceroute, a wake-up, the ports or the web page of one device and an inspection with a login you give; orders arrive in the answer to the node's own message (never as a connection made to the node), each is checked before anything is done, and nothing is run through a shell.",
   "**Logins that stay safe:** the login of an inspection travels sealed for this node alone, is sent only over Digest or HTTPS (never Basic over plain HTTP), only to the device whose HTTPS certificate was seen the first time, and is never echoed back.",
   "**The public side:** the house's public address, who gives it and where it is (one HTTPS request to a fixed public service every few minutes; `--no-public-info` turns it off). With `--dns-name` it also resolves the name the house is reached by from outside and says whether it points to that address.",
   "**A service:** it runs as a systemd unit on the CM5 test bench (written by hand, see the usage guide) and keeps its data in its own folder.",
   "**Not yet:** the router's own counters (traffic per device), packet capture, controlling anything (blocking a device, closing a port, changing the router) and weeks on a real network."
  ],
  "note": "See the [usage](docs/USAGE.md) and the [design](docs/DESIGN.md).\n\nSee the [design](docs/DESIGN.md), the [safety notes](docs/SAFETY.md), the [usage](docs/USAGE.md) and the [messages](docs/MESSAGES.md).",
  "hardware": "Runs as a service on the CM5 test bench, watching its real network (a router, the phones and nodes of the house)",
  "fit": "ARMOR-NETWORK is the family's eye on the local network. It runs on a machine of the network (the CM5 on the bench), looks at what is there without touching it and reports to [ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER), which keeps the names, the hidden and watched devices and the outages; the *Network* menu and the *Network Designer* of [ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) and the Network screen of [ARMOR-ANDROID-CONTROL](https://github.com/JuanenRac/ARMOR-ANDROID-CONTROL) show it, and Studio can hand it orders. It never configures the router or any device."
 },
 "es": {
  "tagline": "Vigila la red local: los dispositivos que hay, si hay internet, qué cambia y qué es nuevo (un programa de Python sin dependencias; corre en una máquina de la red e informa a ARMOR-SERVER)",
  "honest": "El escáner, el inventario que dice qué cambió, la comprobación de internet, la consulta de la dirección pública, las órdenes desde Studio y los accesos sellados se prueban en un ordenador contra una red guionizada (181 tests; cada mensaje lo acepta el contrato de ARMOR-COMMON), y el programa corre como servicio en el banco de pruebas de la CM5, vigilando la red real en la que está el banco (un router, los móviles y los nodos de la casa). No ha vigilado una casa entera durante semanas, solo pregunta al router y nunca lo configura, y qué es un dispositivo (su tipo, su sistema, su fabricante) es una suposición. No captura paquetes: no puede ver quién habla con quién, y el tráfico por dispositivo y la detección de intrusos en sentido estricto necesitan los contadores del router o un puerto espejo, que es un paso posterior.",
  "bullets": [
   "**Qué hay en la red:** la tabla de vecinos de la máquina, un toque a cada dirección para que se llene, un eco a cada dispositivo encontrado (latencia y TTL) y lo que los dispositivos anuncian de sí mismos (mDNS, UPnP, NetBIOS, DNS inverso). De cada uno: dirección, MAC, fabricante (del registro de la IEEE, 40.000 bloques), nombre, tipo, sistema, puertos abiertos con lo que dice cada uno y cuándo se vio por primera y por última vez.",
   "**Puertos:** una conexión TCP a 17 (o 44) puertos de cada dispositivo, de doce en doce, leyendo como mucho unos cientos de bytes de lo que responde; nunca un inicio de sesión, nunca un exploit. Un dispositivo nuevo se mira enseguida, los demás cada cuarto de hora.",
   "**Qué cambia:** un dispositivo que aparece (los tres primeros barridos solo aprenden), calla o vuelve, cambia de dirección, un puerto que se abre o se cierra, y dos máquinas que responden por una misma dirección (sobre todo la del router). Cada evento tiene un id, así que se cuenta una vez.",
   "**Internet:** cada pocos segundos un eco al router, una conexión TCP, dos preguntas DNS a resolvedores elegidos y una página web. Un corte necesita tres rondas para llamarse así y dos para darse por terminado, se fecha desde su primera ronda fallida y se cuenta hasta la primera buena, y dice de quién es la culpa: del operador (el router responde y nada más allá) o de este lado (el router tampoco responde). Latencia, pérdida y los cortes de las últimas 24 horas.",
   "**Solo mira tu propia red:** rechaza cualquier dirección que no sea privada (10/8, 172.16/12, 192.168/16) y cualquier rango mayor que un /22; una lista de exclusión lo mantiene lejos de lo frágil; a un dispositivo no se le envía nada que no sea una pregunta.",
   "**El mensaje** `armor/network/<nodo>/state`: la interfaz, internet, cada dispositivo y los últimos eventos; está en el contrato compartido (330 vectores) y lleva hallazgos, nunca órdenes. `python -m armor_network scan` lo imprime como tabla, `watch` informa a ARMOR-SERVER y `demo` representa una casa inventada (se une un dispositivo nuevo, una cámara abre Telnet, se cae internet y vuelve, alguien responde por el router) sin tocar ninguna red.",
   "**Dónde se ve:** el menú Red de ARMOR-STUDIO (los dispositivos, internet con sus cortes y su latencia, el tráfico y los eventos; un administrador pone nombre a los dispositivos y marca los conocidos, que es lo que apaga la alarma de un dispositivo nuevo), el Diseñador de red (el dibujo de la red de la casa, comparado con lo encontrado y capaz de dibujarlo) y la pantalla Red de la app Android. ARMOR-SERVER genera las alarmas.",
   "**Órdenes desde Studio:** un barrido ya, un ping, un traceroute, una activación por red, los puertos o la página web de un dispositivo y una inspección con un acceso que das; las órdenes llegan en la respuesta al propio mensaje del nodo (nunca como una conexión hecha al nodo), cada una se comprueba antes de hacer nada y nada se ejecuta por un shell.",
   "**Accesos que se mantienen seguros:** el acceso de una inspección viaja sellado solo para este nodo, se envía solo por Digest o HTTPS (nunca Basic por HTTP plano), solo al dispositivo cuyo certificado HTTPS se vio la primera vez, y nunca se repite en la respuesta.",
   "**El lado público:** la dirección pública de la casa, quién la da y dónde está (una petición HTTPS a un servicio público fijo cada pocos minutos; `--no-public-info` la apaga). Con `--dns-name` resuelve además el nombre con el que se llega a la casa desde fuera y dice si apunta a esa dirección.",
   "**Un servicio:** corre como unidad systemd en el banco de pruebas de la CM5 (escrita a mano, véase la guía de uso) y guarda sus datos en su propia carpeta.",
   "**Todavía no:** los contadores del propio router (tráfico por dispositivo), la captura de paquetes, controlar nada (bloquear un dispositivo, cerrar un puerto, cambiar el router) y semanas en una red real."
  ],
  "note": "See the [usage](docs/USAGE.md) and the [design](docs/DESIGN.md).\n\nVéanse el [diseño](docs/DESIGN.md), las [notas de seguridad](docs/SAFETY.md), el [uso](docs/USAGE.md) y los [mensajes](docs/MESSAGES.md).",
  "hardware": "Corre como servicio en el banco de pruebas de la CM5, vigilando su red real (un router, los móviles y los nodos de la casa)",
  "fit": "ARMOR-NETWORK es el ojo de la familia sobre la red local. Corre en una máquina de la red (la CM5 en el banco), mira lo que hay sin tocarlo e informa a [ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER), que guarda los nombres, los dispositivos ocultos y vigilados y los cortes; el menú *Red* y el *Diseñador de red* de [ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) y la pantalla Red de [ARMOR-ANDROID-CONTROL](https://github.com/JuanenRac/ARMOR-ANDROID-CONTROL) lo muestran, y Studio puede darle órdenes. Nunca configura el router ni ningún dispositivo.",
  "requirements": [
   "Python 3.11+ (solo la biblioteca estándar)",
   "una máquina de la red a vigilar (Linux, Windows o macOS)"
  ]
 },
 "fr": {
  "tagline": "Surveille le réseau local : les appareils présents, si internet est là, ce qui change et ce qui est nouveau (un programme Python sans dépendances ; il tourne sur une machine du réseau et rapporte à ARMOR-SERVER)",
  "honest": "Le scanner, l'inventaire qui dit ce qui a changé, le contrôle d'internet, la recherche de l'adresse publique, les ordres depuis Studio et les identifiants scellés sont testés sur un ordinateur contre un réseau scripté (181 tests ; chaque message est accepté par le contrat d'ARMOR-COMMON), et le programme tourne comme service sur le banc de test CM5, en surveillant le vrai réseau où se trouve le banc (un routeur, les téléphones et les nœuds de la maison). Il n'a pas surveillé une maison entière pendant des semaines, il ne fait que demander au routeur et ne le configure jamais, et ce qu'est un appareil (son type, son système, son fabricant) est une supposition. Il ne capture pas de paquets : il ne voit pas qui parle à qui, et le trafic par appareil et la détection d'intrusion au sens strict demandent les compteurs du routeur ou un port miroir, ce qui est une étape ultérieure.",
  "bullets": [
   "**Ce qu'il y a sur le réseau :** la table de voisins de la machine, un coup sur chaque adresse pour qu'elle se remplisse, un écho à chaque appareil trouvé (latence et TTL) et ce que les appareils annoncent d'eux-mêmes (mDNS, UPnP, NetBIOS, DNS inverse). Pour chacun : adresse, MAC, fabricant (du registre de l'IEEE, 40 000 blocs), nom, type, système, ports ouverts avec ce que dit chacun, et quand il a été vu pour la première et la dernière fois.",
   "**Ports :** une connexion TCP à 17 (ou 44) ports de chaque appareil, douze à la fois, en lisant au plus quelques centaines d'octets de la réponse ; jamais de connexion, jamais d'exploit. Un nouvel appareil est examiné aussitôt, les autres tous les quarts d'heure.",
   "**Ce qui change :** un appareil qui apparaît (les trois premiers balayages ne font qu'apprendre), se tait ou revient, change d'adresse, un port qui s'ouvre ou se ferme, et deux machines qui répondent pour une même adresse (surtout celle du routeur). Chaque événement a un id, il n'est donc dit qu'une fois.",
   "**Internet :** toutes les quelques secondes un écho au routeur, une connexion TCP, deux questions DNS à des résolveurs choisis et une page web. Une coupure demande trois tours pour être déclarée et deux pour être finie, est datée du premier tour raté et comptée jusqu'au premier bon, et dit à qui est la faute : au fournisseur (le routeur répond et rien au-delà) ou à ce côté-ci (le routeur ne répond pas non plus). Latence, perte et les coupures des dernières 24 heures.",
   "**Il ne regarde que votre propre réseau :** il refuse toute adresse non privée (10/8, 172.16/12, 192.168/16) et toute plage plus grande qu'un /22 ; une liste d'exclusion le tient éloigné de ce qui est fragile ; rien n'est envoyé à un appareil qui ne soit une question.",
   "**Le message** `armor/network/<nœud>/state` : l'interface, internet, chaque appareil et les derniers événements ; il est dans le contrat partagé (330 vecteurs) et porte des constats, jamais des ordres. `python -m armor_network scan` l'imprime en tableau, `watch` informe ARMOR-SERVER, `demo` joue une maison inventée (un nouvel appareil arrive, une caméra ouvre Telnet, internet tombe et revient, quelqu'un répond pour le routeur) sans toucher aucun réseau.",
   "**Où on le voit :** le menu Réseau d'ARMOR-STUDIO (les appareils, internet avec ses coupures et sa latence, le trafic et les événements ; un administrateur nomme les appareils et marque les connus, ce qui apaise l'alarme d'un nouvel appareil), le Concepteur de réseau (le dessin du réseau de la maison, comparé à ce qui a été trouvé et capable de le dessiner) et l'écran Réseau de l'app Android. ARMOR-SERVER déclenche les alarmes.",
   "**Ordres depuis Studio :** un balayage tout de suite, un ping, un traceroute, un réveil réseau, les ports ou la page web d'un appareil et une inspection avec un identifiant que vous donnez ; les ordres arrivent dans la réponse au propre message du nœud (jamais comme une connexion faite vers le nœud), chacun est vérifié avant d'agir et rien n'est exécuté par un shell.",
   "**Des identifiants qui restent sûrs :** l'identifiant d'une inspection voyage scellé pour ce seul nœud, n'est envoyé qu'en Digest ou HTTPS (jamais Basic en HTTP clair), seulement à l'appareil dont le certificat HTTPS a été vu la première fois, et n'est jamais renvoyé en écho.",
   "**Le côté public :** l'adresse publique de la maison, qui la donne et où elle se trouve (une requête HTTPS vers un service public fixe toutes les quelques minutes ; `--no-public-info` la désactive). Avec `--dns-name`, il résout aussi le nom qui permet d'atteindre la maison depuis l'extérieur et indique s'il pointe vers cette adresse.",
   "**Un service :** il tourne comme unité systemd sur le banc de test CM5 (écrite à la main, voir le guide d'utilisation) et garde ses données dans son propre dossier.",
   "**Pas encore :** les compteurs du routeur lui-même (trafic par appareil), la capture de paquets, contrôler quoi que ce soit (bloquer un appareil, fermer un port, changer le routeur) et des semaines sur un vrai réseau."
  ],
  "note": "See the [usage](docs/USAGE.md) and the [design](docs/DESIGN.md).\n\nVoir la [conception](docs/DESIGN.md), les [notes de sécurité](docs/SAFETY.md), l'[usage](docs/USAGE.md) et les [messages](docs/MESSAGES.md).",
  "hardware": "Tourne comme service sur le banc de test CM5, en surveillant son vrai réseau (un routeur, les téléphones et les nœuds de la maison)",
  "fit": "ARMOR-NETWORK est l'œil de la famille sur le réseau local. Il tourne sur une machine du réseau (la CM5 sur le banc), regarde ce qui s'y trouve sans y toucher et rapporte à [ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER), qui garde les noms, les appareils masqués et surveillés et les coupures ; le menu *Réseau* et le *Concepteur réseau* d'[ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) et l'écran Réseau d'[ARMOR-ANDROID-CONTROL](https://github.com/JuanenRac/ARMOR-ANDROID-CONTROL) le montrent, et Studio peut lui donner des ordres. Il ne configure jamais le routeur ni aucun appareil.",
  "requirements": [
   "Python 3.11+ (bibliothèque standard uniquement)",
   "une machine du réseau à surveiller (Linux, Windows ou macOS)"
  ]
 },
 "it": {
  "tagline": "Sorveglia la rete locale: i dispositivi presenti, se internet c'è, cosa cambia e cosa è nuovo (un programma Python senza dipendenze; gira su una macchina della rete e riferisce ad ARMOR-SERVER)",
  "honest": "Lo scanner, l'inventario che dice cosa è cambiato, il controllo di internet, la ricerca dell'indirizzo pubblico, gli ordini da Studio e gli accessi sigillati sono provati su un computer contro una rete scriptata (181 test; ogni messaggio è accettato dal contratto di ARMOR-COMMON), e il programma gira come servizio sul banco di prova CM5, sorvegliando la rete reale su cui si trova il banco (un router, i telefoni e i nodi della casa). Non ha sorvegliato una casa intera per settimane, chiede solo al router e non lo configura mai, e cosa sia un dispositivo (il tipo, il sistema, il produttore) è una supposizione. Non cattura pacchetti: non può vedere chi parla con chi, e il traffico per dispositivo e il rilevamento delle intrusioni in senso stretto richiedono i contatori del router o una porta mirror, che è un passo successivo.",
  "bullets": [
   "**Cosa c'è in rete:** la tabella dei vicini della macchina, un tocco a ogni indirizzo perché si riempia, un'eco a ogni dispositivo trovato (latenza e TTL) e ciò che i dispositivi annunciano di sé (mDNS, UPnP, NetBIOS, DNS inverso). Per ciascuno: indirizzo, MAC, produttore (dal registro IEEE, 40.000 blocchi), nome, tipo, sistema, porte aperte con ciò che dice ognuna e quando è stato visto la prima e l'ultima volta.",
   "**Porte:** una connessione TCP a 17 (o 44) porte di ogni dispositivo, dodici alla volta, leggendo al più poche centinaia di byte della risposta; mai un accesso, mai un exploit. Un dispositivo nuovo si guarda subito, gli altri ogni quarto d'ora.",
   "**Cosa cambia:** un dispositivo che compare (le prime tre scansioni imparano soltanto), tace o torna, cambia indirizzo, una porta che si apre o si chiude, e due macchine che rispondono per lo stesso indirizzo (soprattutto quello del router). Ogni evento ha un id, quindi si dice una volta sola.",
   "**Internet:** ogni pochi secondi un'eco al router, una connessione TCP, due domande DNS a risolutori scelti e una pagina web. Un'interruzione richiede tre giri per chiamarsi così e due per dirsi finita, si data dal primo giro fallito e si conta fino al primo buono, e dice di chi è la colpa: del gestore (il router risponde e nulla oltre) o di questa parte (anche il router non risponde). Latenza, perdita e le interruzioni delle ultime 24 ore.",
   "**Guarda solo la tua rete:** rifiuta ogni indirizzo non privato (10/8, 172.16/12, 192.168/16) e ogni intervallo più grande di un /22; un elenco di esclusione lo tiene lontano da ciò che è fragile; a un dispositivo non si invia nulla che non sia una domanda.",
   "**Il messaggio** `armor/network/<nodo>/state`: l'interfaccia, internet, ogni dispositivo e gli ultimi eventi; è nel contratto condiviso (330 vettori) e porta rilevazioni, mai comandi. `python -m armor_network scan` lo stampa come tabella, `watch` informa ARMOR-SERVER, `demo` recita una casa inventata (si unisce un dispositivo nuovo, una telecamera apre Telnet, internet cade e torna, qualcuno risponde per il router) senza toccare alcuna rete.",
   "**Dove si vede:** il menu Rete di ARMOR-STUDIO (i dispositivi, internet con le sue interruzioni e la latenza, il traffico e gli eventi; un amministratore dà un nome ai dispositivi e segna quelli noti, ciò che spegne l'allarme di un dispositivo nuovo), il Progettista di rete (il disegno della rete di casa, confrontato con ciò che è stato trovato e capace di disegnarlo) e la schermata Rete dell'app Android. ARMOR-SERVER genera gli allarmi.",
   "**Ordini da Studio:** una scansione subito, un ping, un traceroute, un wake-up, le porte o la pagina web di un dispositivo e un'ispezione con un accesso che dai; gli ordini arrivano nella risposta al messaggio del nodo stesso (mai come una connessione fatta verso il nodo), ognuno è controllato prima di fare qualcosa e nulla è eseguito tramite una shell.",
   "**Accessi che restano sicuri:** l'accesso di un'ispezione viaggia sigillato per questo solo nodo, è inviato solo via Digest o HTTPS (mai Basic su HTTP in chiaro), solo al dispositivo il cui certificato HTTPS è stato visto la prima volta, e non è mai rimandato in eco.",
   "**Il lato pubblico:** l'indirizzo pubblico della casa, chi lo dà e dove si trova (una richiesta HTTPS a un servizio pubblico fisso ogni pochi minuti; `--no-public-info` la spegne). Con `--dns-name` risolve anche il nome con cui si raggiunge la casa dall'esterno e dice se punta a quell'indirizzo.",
   "**Un servizio:** gira come unità systemd sul banco di prova CM5 (scritta a mano, vedi la guida all'uso) e tiene i suoi dati nella propria cartella.",
   "**Non ancora:** i contatori del router stesso (traffico per dispositivo), la cattura dei pacchetti, controllare qualcosa (bloccare un dispositivo, chiudere una porta, cambiare il router) e settimane su una rete reale."
  ],
  "note": "See the [usage](docs/USAGE.md) and the [design](docs/DESIGN.md).\n\nVedi il [progetto](docs/DESIGN.md), le [note di sicurezza](docs/SAFETY.md), l'[uso](docs/USAGE.md) e i [messaggi](docs/MESSAGES.md).",
  "hardware": "Gira come servizio sul banco di prova CM5, sorvegliando la sua rete reale (un router, i telefoni e i nodi della casa)",
  "fit": "ARMOR-NETWORK è l'occhio della famiglia sulla rete locale. Gira su una macchina della rete (la CM5 sul banco), guarda cosa c'è senza toccarlo e riferisce ad [ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER), che conserva i nomi, i dispositivi nascosti e sorvegliati e le interruzioni; il menu *Rete* e il *Progettista di rete* di [ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) e la schermata Rete di [ARMOR-ANDROID-CONTROL](https://github.com/JuanenRac/ARMOR-ANDROID-CONTROL) lo mostrano, e Studio può dargli ordini. Non configura mai il router né alcun dispositivo.",
  "requirements": [
   "Python 3.11+ (solo la libreria standard)",
   "una macchina della rete da sorvegliare (Linux, Windows o macOS)"
  ]
 },
 "de": {
  "tagline": "Beobachtet das lokale Netz: die Geräte darin, ob das Internet da ist, was sich ändert und was neu ist (ein Python-Programm ohne Abhängigkeiten; es läuft auf einem Rechner des Netzes und meldet an ARMOR-SERVER)",
  "honest": "Der Scanner, das Inventar, das sagt, was sich geändert hat, die Internetprüfung, die Abfrage der öffentlichen Adresse, die Aufträge aus Studio und die versiegelten Logins werden auf einem Computer gegen ein geskriptetes Netz getestet (181 Tests; jede Nachricht wird vom Vertrag von ARMOR-COMMON akzeptiert), und das Programm läuft als Dienst am CM5-Testaufbau und beobachtet das echte Netz, in dem der Aufbau steht (ein Router, die Telefone und Knoten des Hauses). Es hat noch kein ganzes Haus wochenlang beobachtet, es fragt nur den Router und konfiguriert ihn nie, und was ein Gerät ist (Art, System, Hersteller), ist eine Vermutung. Es fängt keine Pakete ab: Es sieht nicht, wer mit wem spricht, und Verkehr pro Gerät und Einbruchserkennung im strengen Sinn brauchen die Zähler des Routers oder einen Mirror-Port, was ein späterer Schritt ist.",
  "bullets": [
   "**Was im Netzwerk ist:** die Nachbartabelle des Rechners, ein Anstupsen jeder Adresse, damit sie sich füllt, ein Echo an jedes gefundene Gerät (Latenz und TTL) und was Geräte über sich selbst ankündigen (mDNS, UPnP, NetBIOS, Reverse-DNS). Je Gerät: Adresse, MAC, Hersteller (aus dem IEEE-Register mit 40.000 Blöcken), Name, Art, System, offene Ports mit dem, was jeder sagt, und wann es zuerst und zuletzt gesehen wurde.",
   "**Ports:** eine TCP-Verbindung zu 17 (oder 44) Ports je Gerät, zwölf gleichzeitig, mit höchstens einigen hundert gelesenen Bytes der Antwort; nie ein Login, nie ein Exploit. Ein neues Gerät wird sofort angesehen, die anderen alle Viertelstunde.",
   "**Was sich ändert:** ein Gerät, das auftaucht (die ersten drei Scans lernen nur), verstummt oder zurückkommt, seine Adresse ändert, ein Port, der sich öffnet oder schließt, und zwei Rechner, die für eine Adresse antworten (vor allem die des Routers). Jedes Ereignis hat eine ID und wird daher nur einmal gemeldet.",
   "**Das Internet:** alle paar Sekunden ein Echo an den Router, eine TCP-Verbindung, zwei DNS-Fragen an gewählte Resolver und eine Webseite. Ein Ausfall braucht drei Runden, um so zu heißen, und zwei, um beendet zu sein, wird ab der ersten fehlgeschlagenen Runde datiert und bis zur ersten guten gezählt und sagt, wessen Schuld es ist: die des Anbieters (der Router antwortet, dahinter nichts) oder die dieser Seite (auch der Router antwortet nicht). Latenz, Verlust und die Ausfälle der letzten 24 Stunden.",
   "**Es sieht nur Ihr eigenes Netzwerk:** es verweigert jede nicht private Adresse (10/8, 172.16/12, 192.168/16) und jeden Bereich über /22; eine Ausschlussliste hält es von Empfindlichem fern; an ein Gerät wird nichts gesendet, was keine Frage ist.",
   "**Die Nachricht** `armor/network/<Knoten>/state`: die Schnittstelle, das Internet, jedes Gerät und die letzten Ereignisse; sie steht im gemeinsamen Vertrag (330 Vektoren) und trägt Befunde, nie Befehle. `python -m armor_network scan` druckt sie als Tabelle, `watch` meldet an ARMOR-SERVER, `demo` spielt ein erfundenes Haus (ein neues Gerät kommt hinzu, eine Kamera öffnet Telnet, das Internet fällt aus und kommt zurück, jemand antwortet für den Router) ohne ein Netzwerk zu berühren.",
   "**Wo man es sieht:** das Netzwerk-Menü von ARMOR-STUDIO (die Geräte, das Internet mit Ausfällen und Latenz, der Datenverkehr und die Ereignisse; ein Administrator benennt Geräte und markiert bekannte, was den Alarm eines neuen Geräts beruhigt), der Netzwerkplaner (die Zeichnung des Hausnetzwerks, verglichen mit dem Gefundenen und fähig, es zu zeichnen) und der Netzwerk-Bildschirm der Android-App. ARMOR-SERVER löst die Alarme aus.",
   "**Aufträge aus Studio:** sofort ein Scan, ein Ping, ein Traceroute, ein Aufwecken, die Ports oder die Webseite eines Geräts und eine Prüfung mit einem von Ihnen gegebenen Login; Aufträge kommen in der Antwort auf die eigene Nachricht des Knotens an (nie als Verbindung zum Knoten), jeder wird geprüft, bevor etwas geschieht, und nichts läuft über eine Shell.",
   "**Logins, die sicher bleiben:** der Login einer Prüfung reist nur für diesen Knoten versiegelt, wird nur per Digest oder HTTPS gesendet (nie Basic über Klartext-HTTP), nur an das Gerät, dessen HTTPS-Zertifikat beim ersten Mal gesehen wurde, und nie zurückgespiegelt.",
   "**Die öffentliche Seite:** die öffentliche Adresse des Hauses, wer sie liefert und wo sie liegt (alle paar Minuten eine HTTPS-Anfrage an einen festen öffentlichen Dienst; `--no-public-info` schaltet sie ab). Mit `--dns-name` löst er außerdem den Namen auf, unter dem das Haus von außen erreichbar ist, und meldet, ob er auf diese Adresse zeigt.",
   "**Ein Dienst:** er läuft als systemd-Einheit am CM5-Testaufbau (von Hand geschrieben, siehe die Anleitung) und hält seine Daten in einem eigenen Ordner.",
   "**Noch nicht:** die Zähler des Routers selbst (Verkehr je Gerät), Paketmitschnitt, irgendetwas steuern (ein Gerät sperren, einen Port schließen, den Router ändern) und Wochen in einem echten Netzwerk."
  ],
  "note": "See the [usage](docs/USAGE.md) and the [design](docs/DESIGN.md).\n\nSiehe den [Entwurf](docs/DESIGN.md), die [Sicherheitshinweise](docs/SAFETY.md), die [Benutzung](docs/USAGE.md) und die [Nachrichten](docs/MESSAGES.md).",
  "hardware": "Läuft als Dienst am CM5-Testaufbau und beobachtet sein echtes Netz (einen Router, die Telefone und Knoten des Hauses)",
  "fit": "ARMOR-NETWORK ist das Auge der Familie auf das lokale Netz. Es läuft auf einem Rechner des Netzes (der CM5 am Aufbau), sieht an, was da ist, ohne es zu berühren, und meldet an [ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER), der Namen, versteckte und beobachtete Geräte und Ausfälle führt; das Menü *Netzwerk* und der *Netzwerk-Designer* von [ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) sowie der Netzwerk-Bildschirm von [ARMOR-ANDROID-CONTROL](https://github.com/JuanenRac/ARMOR-ANDROID-CONTROL) zeigen es, und Studio kann ihm Aufträge geben. Es konfiguriert nie den Router oder ein Gerät.",
  "requirements": [
   "Python 3.11+ (nur die Standardbibliothek)",
   "ein zu überwachender Rechner im Netz (Linux, Windows oder macOS)"
  ]
 },
 "zh": {
  "tagline": "监视本地网络：上面有哪些设备、互联网是否可用、哪些发生了变化、哪些是新的（无依赖的 Python 程序；在网络中的一台机器上运行并向 ARMOR-SERVER 报告）",
  "honest": "扫描器、说明发生了什么变化的清单、互联网检查、公网地址查询、来自 Studio 的指令和加密封装的登录信息，都在计算机上对照脚本化网络测试（181 个测试；每条消息都被 ARMOR-COMMON 的契约接受），程序在 CM5 测试台上作为服务运行，监视测试台所在的真实网络（一台路由器、住宅的手机和节点）。它还没有连续数周监视整个住宅，只询问路由器而从不配置它，设备是什么（类型、系统、厂商）只是猜测。它不抓包：看不到谁与谁通信，每个设备的流量和严格意义上的入侵检测需要路由器的计数器或镜像端口，那是以后的一步。",
  "bullets": [
   "**网络上有什么：** 本机的邻居表、为填充它而对每个地址的试探、对每个发现的设备的回显（延迟与 TTL），以及设备对自身的宣告（mDNS、UPnP、NetBIOS、反向 DNS）。每台设备：地址、MAC、厂商（来自 IEEE 的 40,000 个块的登记表）、名称、类型、系统、开放端口及各自的应答内容，以及首次和最近一次看到的时间。",
   "**端口：** 对每台设备的 17（或 44）个端口进行 TCP 连接，每次十二个，最多只读取应答的几百字节；从不登录，从不利用漏洞。新设备立即检查，其余每刻钟一次。",
   "**变化：** 设备出现（前三次扫描只学习）、沉默或恢复、更改地址、端口打开或关闭，以及两台机器响应同一个地址（尤其是路由器的地址）。每个事件都有 id，因此只通报一次。",
   "**互联网：** 每隔几秒对路由器回显、一次 TCP 连接、向选定解析器发出两个 DNS 问题以及一个网页。三轮才算中断、两轮才算结束，从第一轮失败起算、数到第一轮成功，并指出是谁的问题：运营商一侧（路由器有响应而其后没有）还是本地一侧（路由器也没有响应）。延迟、丢包和最近 24 小时的中断。",
   "**只查看您自己的网络：** 拒绝任何非私有地址（10/8、172.16/12、192.168/16 之外）和大于 /22 的范围；排除列表让它远离脆弱的设备；不会向设备发送任何不是提问的内容。",
   "**消息** `armor/network/<节点>/state`：接口、互联网、每台设备和最新事件；它在共享契约中（330 个向量），只携带发现，绝不携带命令。`python -m armor_network scan` 以表格打印，`watch` 通知 ARMOR-SERVER，`demo` 演示一栋虚构的房子（新设备加入、摄像头打开 Telnet、互联网中断又恢复、有人冒充路由器应答），不触碰任何网络。",
   "**在哪里显示：** ARMOR-STUDIO 的网络菜单（设备、带中断和延迟的互联网、流量和事件；管理员为设备命名并标记已知设备，这会平息新设备的警报）、网络设计器（家中网络的图纸，与发现的内容对比并能自动绘制）以及 Android 应用的网络界面。警报由 ARMOR-SERVER 发出。",
   "**来自 Studio 的指令：**立即扫描、ping、traceroute、网络唤醒、某个设备的端口或网页，以及用你提供的登录信息进行检查；指令在对节点自身消息的应答中到达（绝不是向节点发起连接），每条在执行前都要检查，也不通过 shell 运行任何东西。",
   "**始终安全的登录信息：**检查所用的登录信息仅为该节点加密封装后传输，只通过 Digest 或 HTTPS 发送（绝不通过明文 HTTP 的 Basic），只发给首次见到其 HTTPS 证书的设备，并且从不回显。",
   "**公网一侧：**住宅的公网地址、提供者及其位置（每隔几分钟向一个固定的公共服务发一次 HTTPS 请求；`--no-public-info` 可关闭）。使用 `--dns-name` 时，还会解析从外部访问住宅所用的域名，并说明它是否指向该地址。",
   "**一项服务：**它作为 systemd 单元在 CM5 测试台上运行（手写，见使用指南），数据保存在自己的文件夹中。",
   "**尚未：** 路由器自身的计数器（按设备统计流量）、抓包、控制任何东西（封锁设备、关闭端口、修改路由器）以及在真实网络上运行数周。"
  ],
  "note": "See the [usage](docs/USAGE.md) and the [design](docs/DESIGN.md).\n\n参见[设计](docs/DESIGN.md)、[安全说明](docs/SAFETY.md)、[使用](docs/USAGE.md)和[消息](docs/MESSAGES.md)。",
  "hardware": "在 CM5 测试台上作为服务运行，监视其真实网络（路由器、住宅的手机和节点）",
  "fit": "ARMOR-NETWORK 是家族观察本地网络的眼睛。它运行在网络中的一台机器上（测试台上的 CM5），只看不碰，并向 [ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER) 报告，由后者保存名称、隐藏和监视的设备以及中断记录；[ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) 的*网络*菜单和*网络设计器*以及 [ARMOR-ANDROID-CONTROL](https://github.com/JuanenRac/ARMOR-ANDROID-CONTROL) 的网络界面显示这些内容，Studio 还可以给它下达指令。它从不配置路由器或任何设备。",
  "requirements": [
   "Python 3.11+（仅标准库）",
   "网络上需要监控的机器（Linux、Windows 或 macOS）"
  ]
 },
 "ja": {
  "tagline": "ローカルネットワークを見張ります：接続されているデバイス、インターネットがあるか、何が変わり何が新しいか（依存ライブラリなしの Python プログラム。ネットワーク上のマシンで動き、ARMOR-SERVER に報告）",
  "honest": "スキャナー、何が変わったかを伝えるインベントリ、インターネットの検査、公開アドレスの問い合わせ、Studio からの指示、封印されたログインは、スクリプト化したネットワークに対してコンピューター上でテストされ（181 件。すべてのメッセージが ARMOR-COMMON のコントラクトに受け付けられる）、プログラムは CM5 テストベンチ上でサービスとして動き、ベンチがつながる実際のネットワーク（ルーター、家のスマートフォンとノード）を見張っています。家全体を数週間見張ったことはなく、ルーターに尋ねるだけで設定は一切せず、デバイスが何か（種類、システム、メーカー）は推測です。パケットは取得しません。誰が誰と話しているかは見えず、デバイスごとのトラフィックや厳密な意味での侵入検知にはルーターのカウンターかミラーポートが必要で、それは今後の段階です。",
  "bullets": [
   "**ネットワーク上にあるもの：** マシンの近隣テーブル、それを満たすための各アドレスへの呼びかけ、見つかった各機器へのエコー（遅延と TTL）、機器自身の告知（mDNS、UPnP、NetBIOS、逆引き DNS）。機器ごとに、アドレス、MAC、メーカー（IEEE の 40,000 ブロックの登録簿から）、名前、種類、OS、開いているポートとその応答内容、初回と最終の確認時刻を持ちます。",
   "**ポート：** 各機器の 17（または 44）ポートに TCP 接続を 12 本ずつ行い、応答は数百バイトまでしか読みません。ログインも攻撃も行いません。新しい機器はすぐに、他は 15 分ごとに調べます。",
   "**変化：** 機器の出現（最初の 3 回のスキャンは学習のみ）、沈黙、復帰、アドレスの変更、ポートの開閉、1 つのアドレスに 2 台が応答（特にルーターのアドレス）。各イベントには ID があり、一度だけ通知されます。",
   "**インターネット：** 数秒ごとにルーターへのエコー、TCP 接続、選んだリゾルバーへの DNS 問い合わせ 2 件、ウェブページ 1 件。停止と判定するには 3 回、復旧と判定するには 2 回の連続が必要で、最初の失敗の回から起算し最初の成功の回まで数え、原因がどちら側かも示します：プロバイダー側（ルーターは応答し、その先は応答しない）か、こちら側（ルーターも応答しない）。遅延、損失、過去 24 時間の停止。",
   "**自分のネットワークだけを見ます：** プライベートでないアドレス（10/8、172.16/12、192.168/16 以外）と /22 より大きい範囲は拒否します。除外リストでデリケートな機器には触れず、機器には質問以外を送りません。",
   "**メッセージ** `armor/network/<ノード>/state`：インターフェース、インターネット、全機器、最新のイベント。共有コントラクト（330 ベクター）にあり、発見だけを運び、命令は運びません。`python -m armor_network scan` は表で表示、`watch` は ARMOR-SERVER に通知、`demo` は架空の家（新しい機器の参加、カメラが Telnet を開く、インターネットの断と復旧、ルーターになりすます応答）を、ネットワークに触れずに再生します。",
   "**表示場所：** ARMOR-STUDIO のネットワークメニュー（機器、停止と遅延のあるインターネット、トラフィック、イベント。管理者が機器に名前を付け既知として印を付けると、新しい機器の警報が静まります）、ネットワーク設計（家のネットワークの図面を、検出結果と比較し、描くこともできます）、Android アプリのネットワーク画面。警報は ARMOR-SERVER が発します。",
   "**Studio からの指示：**今すぐのスキャン、ping、traceroute、ウェイクアップ、1 台のデバイスのポートや Web ページ、あなたが渡したログインでの検査。指示はノード自身のメッセージへの応答として届き（ノードへの接続としては決して来ません）、実行前にそれぞれ検査され、シェルを通して何かを実行することはありません。",
   "**安全なままのログイン：**検査のログインはそのノードだけに封印されて届き、Digest または HTTPS でのみ送られ（平文 HTTP の Basic は決して使わない）、最初に HTTPS 証明書を見たデバイスにだけ送られ、エコーバックされません。",
   "**公開側：**家の公開アドレス、その提供元と場所（数分ごとに固定の公開サービスへ HTTPS リクエストを 1 回。`--no-public-info` でオフ）。`--dns-name` を使うと、外から家に接続するための名前も解決し、そのアドレスを指しているかどうかを伝えます。",
   "**サービス：**CM5 テストベンチで systemd ユニットとして動き（手書き、使い方ガイドを参照）、データは専用のフォルダーに保存します。",
   "**まだ：** ルーター自身のカウンター（機器ごとのトラフィック）、パケットキャプチャ、何かを制御すること（機器のブロック、ポートを閉じる、ルーターの変更）、実ネットワークでの数週間の運用。"
  ],
  "note": "See the [usage](docs/USAGE.md) and the [design](docs/DESIGN.md).\n\n[設計](docs/DESIGN.md)、[安全性のメモ](docs/SAFETY.md)、[使い方](docs/USAGE.md)、[メッセージ](docs/MESSAGES.md)を参照してください。",
  "hardware": "CM5 テストベンチ上でサービスとして動き、実際のネットワーク（ルーター、家のスマートフォンとノード）を見張っています",
  "fit": "ARMOR-NETWORK はファミリーのローカルネットワークを見る目です。ネットワーク上のマシン（ベンチの CM5）で動き、そこにあるものに触れずに見て、[ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER) に報告します。サーバーが名前、非表示・監視デバイス、停止を保持し、[ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) の*ネットワーク*メニューと*ネットワークデザイナー*、[ARMOR-ANDROID-CONTROL](https://github.com/JuanenRac/ARMOR-ANDROID-CONTROL) のネットワーク画面が表示し、Studio から指示も出せます。ルーターやデバイスを設定することはありません。",
  "requirements": [
   "Python 3.11+（標準ライブラリのみ）",
   "監視対象のネットワーク上のマシン（Linux、Windows、macOS）"
  ]
 },
 "pt": {
  "tagline": "Vigia a rede local: os dispositivos que nela estão, se há internet, o que muda e o que é novo (um programa Python sem dependências; corre numa máquina da rede e reporta ao ARMOR-SERVER)",
  "honest": "O scanner, o inventário que diz o que mudou, a verificação da internet, a consulta do endereço público, as ordens do Studio e os acessos selados são testados num computador contra uma rede guionizada (181 testes; cada mensagem é aceite pelo contrato do ARMOR-COMMON), e o programa corre como serviço na bancada de testes do CM5, vigiando a rede real em que a bancada está (um router, os telemóveis e os nós da casa). Não vigiou uma casa inteira durante semanas, só pergunta ao router e nunca o configura, e o que é um dispositivo (o tipo, o sistema, o fabricante) é um palpite. Não captura pacotes: não pode ver quem fala com quem, e o tráfego por dispositivo e a deteção de intrusos em sentido estrito precisam dos contadores do router ou de uma porta espelho, que é um passo posterior.",
  "bullets": [
   "**O que há na rede:** a tabela de vizinhos da máquina, um toque a cada endereço para que se preencha, um eco a cada dispositivo encontrado (latência e TTL) e o que os dispositivos anunciam sobre si (mDNS, UPnP, NetBIOS, DNS inverso). Para cada dispositivo: endereço, MAC, fabricante (do registo IEEE de 40 000 blocos), nome, tipo, sistema, portas abertas com o que cada uma diz, e quando foi visto pela primeira e última vez.",
   "**Portas:** uma ligação TCP a 17 (ou 44) portas de cada dispositivo, doze de cada vez, lendo no máximo algumas centenas de bytes do que responde; nunca um início de sessão, nunca uma exploração. Um dispositivo novo observa-se de imediato, os outros a cada quarto de hora.",
   "**O que muda:** um dispositivo que aparece (as três primeiras pesquisas só aprendem), fica em silêncio ou volta, muda de endereço, uma porta que abre ou fecha, e duas máquinas a responder por um endereço (sobretudo o do router). Cada evento tem um id, por isso diz-se uma só vez.",
   "**A internet:** a cada poucos segundos um eco ao router, uma ligação TCP, duas perguntas DNS a resolvedores escolhidos e uma página web. Uma queda precisa de três rondas para se considerar queda e duas para terminar, datada desde a sua primeira ronda falhada e contada até à primeira boa, e diz de quem é a culpa: do operador (o router responde e nada para além dele) ou deste lado (o router também não responde). Latência, perda e as quedas das últimas 24 horas.",
   "**Só olha para a sua própria rede:** recusa qualquer endereço que não seja privado (10/8, 172.16/12, 192.168/16) e qualquer intervalo maior que um /22; uma lista de exclusão mantém-no longe do que é frágil; nada se envia a um dispositivo que não seja uma pergunta.",
   "**A mensagem** `armor/network/<node>/state`: a interface, a internet, cada dispositivo e os últimos eventos; está no contrato partilhado (330 vetores) e leva constatações, nunca comandos. `python -m armor_network scan` imprime-a como tabela, `watch` informa o ARMOR-SERVER, `demo` representa uma casa inventada (entra um dispositivo novo, uma câmara abre Telnet, a internet cai e volta, alguém responde pelo router) sem tocar em nenhuma rede.",
   "**Onde se mostra:** o menu Rede do ARMOR-STUDIO (os dispositivos, a internet com as suas quedas e latência, o tráfego e os eventos; um administrador dá nome aos dispositivos e marca os conhecidos, o que silencia o alarme de dispositivo novo), o Desenhador de rede (o desenho da rede da casa, comparado com o que foi encontrado, e capaz de o desenhar) e o ecrã Rede da aplicação Android. O ARMOR-SERVER dispara os alarmes.",
   "**Ordens do Studio:** um varrimento já, um ping, um traceroute, um acordar, as portas ou a página web de um dispositivo e uma inspeção com um acesso que der; as ordens chegam na resposta à própria mensagem do nó (nunca como uma ligação feita ao nó), cada uma é verificada antes de se fazer algo e nada é executado por uma shell.",
   "**Acessos que se mantêm seguros:** o acesso de uma inspeção viaja selado só para este nó, é enviado só por Digest ou HTTPS (nunca Basic por HTTP simples), só ao dispositivo cujo certificado HTTPS foi visto da primeira vez, e nunca é devolvido em eco.",
   "**O lado público:** o endereço público da casa, quem o dá e onde está (um pedido HTTPS a um serviço público fixo de poucos em poucos minutos; `--no-public-info` desliga-o). Com `--dns-name` resolve também o nome com que se chega a casa a partir do exterior e diz se aponta para esse endereço.",
   "**Um serviço:** corre como unidade systemd na bancada de testes do CM5 (escrita à mão, veja o guia de uso) e guarda os seus dados na sua própria pasta.",
   "**Ainda não:** os contadores do próprio router (tráfego por dispositivo), captura de pacotes, controlar o que quer que seja (bloquear um dispositivo, fechar uma porta, alterar o router) e semanas numa rede real."
  ],
  "note": "Veja a [utilização](docs/USAGE.md) e o [desenho](docs/DESIGN.md).\n\nVeja o [desenho](docs/DESIGN.md), as [notas de segurança](docs/SAFETY.md), a [utilização](docs/USAGE.md) e as [mensagens](docs/MESSAGES.md).",
  "hardware": "Corre como serviço na bancada de testes do CM5, vigiando a sua rede real (um router, os telemóveis e os nós da casa)",
  "fit": "O ARMOR-NETWORK é o olho da família sobre a rede local. Corre numa máquina da rede (o CM5 na bancada), olha o que lá está sem lhe tocar e reporta ao [ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER), que guarda os nomes, os dispositivos ocultos e vigiados e as falhas; o menu *Rede* e o *Desenhador de rede* do [ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) e o ecrã Rede do [ARMOR-ANDROID-CONTROL](https://github.com/JuanenRac/ARMOR-ANDROID-CONTROL) mostram-no, e o Studio pode dar-lhe ordens. Nunca configura o router nem nenhum dispositivo.",
  "requirements": [
   "Python 3.11+ (apenas a biblioteca padrão)",
   "uma máquina da rede a vigiar (Linux, Windows ou macOS)"
  ]
 }
}
