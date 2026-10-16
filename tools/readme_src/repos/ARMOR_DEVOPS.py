# The facts that do not depend on the language, and the words of every language, of ARMOR-DEVOPS.
# Copyright (C) 2026 JuanenRac (Electro Hobby 3D). GPL-3.0-or-later.

FACTS = {
 "emoji": "🚀",
 "badges": [
  [
   "Deploy",
   "Docker%20Compose",
   "2496ed"
  ],
  [
   "Bench",
   "systemd",
   "FFB020"
  ]
 ],
 "diagram": "",
 "build": "```bash\nscripts/generate_secrets.sh          # .env and secrets/ (Git-ignored)\nscripts/check-required-env.sh\ndocker compose config --quiet && docker compose up --build\nscripts/deploy_cm5.sh --host <cm5> --user <user> --key <key> --apply   # the test bench\nscripts/backup_data.sh --data-dir <data> --out-dir <backups> --passphrase-file <file>\n```",
 "structure": "```text\nARMOR-DEVOPS/\n├── docker-compose.yml, docker-compose.tls.yml, .env.example, mosquitto/ (broker, TLS profile, ACL example)\n├── caddy/     Caddyfile (TLS)\n├── scripts/   deploy_cm5, install_cm5, package_component, armor_admin_agent, armor_maintenance_agent, generate_secrets, check-required-env, backup_data, restore_data, firewall_core, mqtt_identity, tests of the agents, the backup, the firewall and the Compose topology\n│   └── dist-packages/   the packages of each release (Studio, server, network, observation, voice, DevOps) with their SHA-256\n└── docs/      DEPLOYMENT_BOUNDARY, CM5_TEST_BENCH, BACKUP_AND_TLS\n```",
 "requirements": [
  "Docker Engine with Compose (for the container topology)",
  "a CM5 or any Debian-based machine reachable by SSH (for the test bench)",
  "Bash, `ssh` and `tar` on the machine that deploys"
 ]
}

TEXT = {
 "en": {
  "tagline": "Deployment, the CM5 test bench, its updates from GitHub and the upkeep of the installation",
  "honest": "The CM5 bench installer has been run on a real CM5 that hosts other software, which stayed healthy, and the bench runs in daily use with the server, Studio, the network node, the observation and voice services, the broker and the two helpers below; updates of its components from GitHub (through Studio) have been done on it. The Docker Compose topology and its optional TLS profile have been built and run for real with Docker Engine in WSL (`scripts/test_compose.sh`), but **not on the Jetson**. The backup and restore scripts have a passing round-trip test, and the two helpers have their own tests. What is **not** proven: a clean install on a machine that has never seen the project, and the whole Docker topology on its target.",
  "bullets": [
   "**CM5 test bench:** `scripts/deploy_cm5.sh` builds in a clean copy, sends one archive and runs `scripts/install_cm5.sh`, which creates its own user, its own directory and systemd units on their own ports for the server and Studio, and, with options, the MQTT broker, the network node, the observation service, the voice gateway, the administration agent, the maintenance helper and the daily backup. It never touches what else the machine runs.",
   "**The maintenance helper** (`armor_maintenance_agent.py`): the updates of the installation's own components from GitHub (it downloads the release package, checks its SHA-256 and swaps it in with a rollback), the operating system's updates and an optional root console, all driven from Studio's *Updates* tab; the console is off unless turned on.",
   "**The administration agent** (`armor_admin_agent.py`): the one privileged part, with a closed list of services, settings files and broker accounts, so Studio never needs root.",
   "**Packages of each release:** `scripts/package_component.py` builds the package of a component (Studio, server, network, observation service, voice gateway, DevOps), writes its SHA-256 next to it and publishes it as a GitHub release.",
   "**Compose topology:** a non-anonymous Mosquitto broker with one identity per node and an ACL (including the alarm nodes and the Zigbee zones the server tells them), the server, and Studio behind an nginx that proxies `/api/`; only Studio is published, on loopback. Hardened containers, pinned images, an internal core network and named volumes for state.",
   "**TLS:** an optional `tls` Compose profile puts Caddy, with its own local certificate authority, in front of Studio, and a Mosquitto configuration over TLS is provided ([details](docs/BACKUP_AND_TLS.md)).",
   "**A host firewall for the core machine** (`scripts/firewall_core.sh`): the broker's port only from the field network, the server's and Studio's ports only from the clients' network (when it is given), in a table of its own that mentions nothing else.",
   "**Secrets:** `scripts/generate_secrets.sh` creates random secrets and prints none; `scripts/check-required-env.sh` refuses missing, placeholder, short or repeated values.",
   "**Backup and restore:** `scripts/backup_data.sh` makes an AES-256 encrypted, verified and checksummed archive of the server data (evidence excluded unless asked); `scripts/restore_data.sh` lists it or restores it without ever overwriting existing data."
  ],
  "note": "See the [deployment boundary](docs/DEPLOYMENT_BOUNDARY.md).",
  "fit": "ARMOR-DEVOPS is how everything else gets onto a machine and stays up to date. It installs the server, Studio, the network node, the observation and voice services and the broker on the CM5 test bench, makes the packages of each release that [ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO)'s *Updates* tab installs from GitHub, and holds the two small helpers that let Studio update the installation and manage its services without ever running as root.",
  "hardware": "Runs the CM5 test bench in daily use, on a real CM5 that hosts other software; not yet on the Jetson"
 },
 "es": {
  "tagline": "Despliegue, el banco de pruebas de la CM5, sus actualizaciones desde GitHub y el mantenimiento de la instalación",
  "honest": "El instalador del banco de la CM5 se ha ejecutado en una CM5 real que aloja otro software, que siguió sano, y el banco corre en uso diario con el servidor, Studio, el nodo de red, los servicios de observación y de voz, el broker y los dos ayudantes de abajo; en él se han hecho actualizaciones de sus componentes desde GitHub (a través de Studio). La topología Docker Compose y su perfil TLS opcional se han construido y ejecutado de verdad con Docker Engine en WSL (`scripts/test_compose.sh`), pero **no en la Jetson**. Los scripts de copia de seguridad y restauración tienen una prueba de ida y vuelta que pasa, y los dos ayudantes tienen sus propios tests. Lo que **no** está probado: una instalación limpia en una máquina que nunca ha visto el proyecto y toda la topología Docker en su destino.",
  "bullets": [
   "**Banco de pruebas de la CM5:** `scripts/deploy_cm5.sh` compila en una copia limpia, envía un archivo y ejecuta `scripts/install_cm5.sh`, que crea su propio usuario, su propio directorio y unidades systemd en sus propios puertos para el servidor y Studio y, con opciones, el broker MQTT, el nodo de red, el servicio de observación, la pasarela de voz, el agente de administración, el ayudante de mantenimiento y la copia de seguridad diaria. Nunca toca lo demás que corre la máquina.",
   "**El ayudante de mantenimiento** (`armor_maintenance_agent.py`): las actualizaciones de los componentes de la propia instalación desde GitHub (descarga el paquete de la versión, comprueba su SHA-256 y lo cambia con vuelta atrás), las del sistema operativo y una consola root opcional, todo gobernado desde la pestaña *Actualizaciones* de Studio; la consola está apagada salvo que se active.",
   "**El agente de administración** (`armor_admin_agent.py`): la única parte con privilegios, con una lista cerrada de servicios, ficheros de ajustes y cuentas del broker, de modo que Studio nunca necesita root.",
   "**Paquetes de cada versión:** `scripts/package_component.py` construye el paquete de un componente (Studio, servidor, red, servicio de observación, pasarela de voz, DevOps), escribe su SHA-256 al lado y lo publica como versión de GitHub.",
   "**Topología Compose:** un broker Mosquitto no anónimo con una identidad por nodo y una ACL (incluidos los nodos de alarma y las zonas Zigbee que les dice el servidor), el servidor y Studio tras un nginx que hace de proxy de `/api/`; solo Studio se publica, en loopback. Contenedores endurecidos, imágenes fijadas, una red interna del núcleo y volúmenes con nombre para el estado.",
   "**TLS:** un perfil `tls` opcional de Compose pone Caddy, con su propia autoridad certificadora local, delante de Studio, y se ofrece una configuración de Mosquitto sobre TLS ([detalles](docs/BACKUP_AND_TLS.md)).",
   "**Un cortafuegos de host para la máquina central** (`scripts/firewall_core.sh`): el puerto del broker solo desde la red de campo, los del servidor y Studio solo desde la red de los clientes (cuando se da), en una tabla propia que no menciona nada más.",
   "**Secretos:** `scripts/generate_secrets.sh` crea secretos aleatorios y no imprime ninguno; `scripts/check-required-env.sh` rechaza valores ausentes, de ejemplo, cortos o repetidos.",
   "**Copia de seguridad y restauración:** `scripts/backup_data.sh` hace un archivo cifrado con AES-256, verificado y con suma de comprobación de los datos del servidor (sin evidencias salvo que se pidan); `scripts/restore_data.sh` lo lista o lo restaura sin sobrescribir nunca datos existentes."
  ],
  "note": "Véase el [límite de despliegue](docs/DEPLOYMENT_BOUNDARY.md).",
  "fit": "ARMOR-DEVOPS es cómo todo lo demás llega a una máquina y se mantiene al día. Instala el servidor, Studio, el nodo de red, los servicios de observación y de voz y el broker en el banco de pruebas de la CM5, hace los paquetes de cada versión que la pestaña *Actualizaciones* de [ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) instala desde GitHub, y guarda los dos pequeños ayudantes que dejan a Studio actualizar la instalación y gestionar sus servicios sin ejecutarse nunca como root.",
  "hardware": "Gobierna el banco de pruebas de la CM5 en uso diario, en una CM5 real que aloja otro software; aún no en la Jetson"
 },
 "fr": {
  "tagline": "Déploiement, le banc de test CM5, ses mises à jour depuis GitHub et l'entretien de l'installation",
  "honest": "L'installateur du banc CM5 a été exécuté sur un vrai CM5 qui héberge d'autres logiciels, restés sains, et le banc fonctionne en usage quotidien avec le serveur, Studio, le nœud réseau, les services d'observation et de voix, le broker et les deux assistants ci-dessous ; des mises à jour de ses composants depuis GitHub (via Studio) y ont été faites. La topologie Docker Compose et son profil TLS facultatif ont été construits et exécutés pour de vrai avec Docker Engine dans WSL (`scripts/test_compose.sh`), mais **pas sur le Jetson**. Les scripts de sauvegarde et de restauration ont un test aller-retour qui passe, et les deux assistants ont leurs propres tests. Ce qui n'est **pas** prouvé : une installation propre sur une machine qui n'a jamais vu le projet et toute la topologie Docker sur sa cible.",
  "bullets": [
   "**Banc de test CM5 :** `scripts/deploy_cm5.sh` compile dans une copie propre, envoie une archive et lance `scripts/install_cm5.sh`, qui crée son propre utilisateur, son propre répertoire et des unités systemd sur leurs propres ports pour le serveur et Studio et, avec des options, le broker MQTT, le nœud réseau, le service d'observation, la passerelle vocale, l'agent d'administration, l'assistant de maintenance et la sauvegarde quotidienne. Il ne touche jamais à ce que la machine exécute par ailleurs.",
   "**L'assistant de maintenance** (`armor_maintenance_agent.py`) : les mises à jour des composants de l'installation depuis GitHub (il télécharge le paquet de la version, vérifie son SHA-256 et le remplace avec retour arrière), celles du système d'exploitation et une console root facultative, le tout piloté depuis l'onglet *Mises à jour* de Studio ; la console est désactivée sauf activation.",
   "**L'agent d'administration** (`armor_admin_agent.py`) : la seule partie privilégiée, avec une liste fermée de services, de fichiers de réglages et de comptes du broker, si bien que Studio n'a jamais besoin de root.",
   "**Paquets de chaque version :** `scripts/package_component.py` construit le paquet d'un composant (Studio, serveur, réseau, service d'observation, passerelle vocale, DevOps), écrit son SHA-256 à côté et le publie comme version GitHub.",
   "**Topologie Compose :** un broker Mosquitto non anonyme avec une identité par nœud et une ACL (y compris les nœuds d'alarme et les zones Zigbee que leur dit le serveur), le serveur et Studio derrière un nginx qui fait proxy de `/api/` ; seul Studio est publié, sur la boucle locale. Conteneurs durcis, images épinglées, un réseau interne du cœur et des volumes nommés pour l'état.",
   "**TLS :** un profil `tls` facultatif de Compose place Caddy, avec sa propre autorité de certification locale, devant Studio, et une configuration Mosquitto sur TLS est fournie ([détails](docs/BACKUP_AND_TLS.md)).",
   "**Un pare-feu d'hôte pour la machine centrale** (`scripts/firewall_core.sh`) : le port du broker seulement depuis le réseau de terrain, ceux du serveur et de Studio seulement depuis le réseau des clients (quand il est donné), dans une table à part qui ne mentionne rien d'autre.",
   "**Secrets :** `scripts/generate_secrets.sh` crée des secrets aléatoires et n'en imprime aucun ; `scripts/check-required-env.sh` refuse les valeurs absentes, d'exemple, courtes ou répétées.",
   "**Sauvegarde et restauration :** `scripts/backup_data.sh` produit une archive chiffrée AES-256, vérifiée et avec somme de contrôle des données du serveur (preuves exclues sauf demande) ; `scripts/restore_data.sh` la liste ou la restaure sans jamais écraser de données existantes."
  ],
  "note": "Voir la [frontière de déploiement](docs/DEPLOYMENT_BOUNDARY.md).",
  "fit": "ARMOR-DEVOPS est la façon dont tout le reste arrive sur une machine et reste à jour. Il installe le serveur, Studio, le nœud réseau, les services d'observation et de voix et le broker sur le banc de test CM5, fait les paquets de chaque version que l'onglet *Mises à jour* d'[ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) installe depuis GitHub, et garde les deux petits assistants qui permettent à Studio de mettre à jour l'installation et de gérer ses services sans jamais tourner en root.",
  "hardware": "Fait tourner le banc de test CM5 en usage quotidien, sur un vrai CM5 qui héberge d'autres logiciels ; pas encore sur le Jetson"
 },
 "it": {
  "tagline": "Distribuzione, il banco di prova CM5, i suoi aggiornamenti da GitHub e la manutenzione dell'impianto",
  "honest": "L'installatore del banco CM5 è stato eseguito su una vera CM5 che ospita altro software, rimasto sano, e il banco funziona in uso quotidiano con il server, Studio, il nodo di rete, i servizi di osservazione e di voce, il broker e i due assistenti qui sotto; vi sono stati fatti aggiornamenti dei suoi componenti da GitHub (tramite Studio). La topologia Docker Compose e il suo profilo TLS opzionale sono stati costruiti ed eseguiti davvero con Docker Engine in WSL (`scripts/test_compose.sh`), ma **non sul Jetson**. Gli script di backup e ripristino hanno un test di andata e ritorno che passa, e i due assistenti hanno i propri test. Ciò che **non** è provato: un'installazione pulita su una macchina che non ha mai visto il progetto e l'intera topologia Docker sulla sua destinazione.",
  "bullets": [
   "**Banco di prova CM5:** `scripts/deploy_cm5.sh` compila in una copia pulita, invia un archivio ed esegue `scripts/install_cm5.sh`, che crea il proprio utente, la propria directory e unità systemd su porte proprie per il server e Studio e, con opzioni, il broker MQTT, il nodo di rete, il servizio di osservazione, il gateway vocale, l'agente di amministrazione, l'assistente di manutenzione e il backup giornaliero. Non tocca mai ciò che la macchina esegue per altro.",
   "**L'assistente di manutenzione** (`armor_maintenance_agent.py`): gli aggiornamenti dei componenti dell'impianto da GitHub (scarica il pacchetto della versione, controlla il suo SHA-256 e lo sostituisce con ripristino), quelli del sistema operativo e una console root facoltativa, tutto guidato dalla scheda *Aggiornamenti* di Studio; la console è spenta salvo attivazione.",
   "**L'agente di amministrazione** (`armor_admin_agent.py`): l'unica parte privilegiata, con un elenco chiuso di servizi, file di impostazioni e account del broker, così Studio non ha mai bisogno di root.",
   "**Pacchetti di ogni versione:** `scripts/package_component.py` costruisce il pacchetto di un componente (Studio, server, rete, servizio di osservazione, gateway vocale, DevOps), scrive il suo SHA-256 accanto e lo pubblica come release GitHub.",
   "**Topologia Compose:** un broker Mosquitto non anonimo con un'identità per nodo e una ACL (compresi i nodi d'allarme e le zone Zigbee che il server dice loro), il server e Studio dietro un nginx che fa da proxy di `/api/`; solo Studio è pubblicato, su loopback. Container rinforzati, immagini fissate, una rete interna del nucleo e volumi con nome per lo stato.",
   "**TLS:** un profilo `tls` facoltativo di Compose mette Caddy, con la propria autorità di certificazione locale, davanti a Studio, ed è fornita una configurazione Mosquitto su TLS ([dettagli](docs/BACKUP_AND_TLS.md)).",
   "**Un firewall di host per la macchina centrale** (`scripts/firewall_core.sh`): la porta del broker solo dalla rete di campo, quelle del server e di Studio solo dalla rete dei client (quando data), in una tabella propria che non menziona nient'altro.",
   "**Segreti:** `scripts/generate_secrets.sh` crea segreti casuali e non ne stampa nessuno; `scripts/check-required-env.sh` rifiuta valori mancanti, di esempio, corti o ripetuti.",
   "**Backup e ripristino:** `scripts/backup_data.sh` produce un archivio cifrato AES-256, verificato e con checksum dei dati del server (prove escluse salvo richiesta); `scripts/restore_data.sh` lo elenca o lo ripristina senza mai sovrascrivere dati esistenti."
  ],
  "note": "Vedi il [confine di distribuzione](docs/DEPLOYMENT_BOUNDARY.md).",
  "fit": "ARMOR-DEVOPS è il modo in cui tutto il resto arriva su una macchina e resta aggiornato. Installa il server, Studio, il nodo di rete, i servizi di osservazione e di voce e il broker sul banco di prova CM5, fa i pacchetti di ogni versione che la scheda *Aggiornamenti* di [ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) installa da GitHub, e tiene i due piccoli assistenti che permettono a Studio di aggiornare l'impianto e gestire i suoi servizi senza mai girare come root.",
  "hardware": "Governa il banco di prova CM5 in uso quotidiano, su una vera CM5 che ospita altro software; non ancora sul Jetson"
 },
 "de": {
  "tagline": "Bereitstellung, der CM5-Testaufbau, seine Updates von GitHub und die Wartung der Anlage",
  "honest": "Der Installer des CM5-Testaufbaus wurde auf einem echten CM5 ausgeführt, der andere Software beherbergt und gesund blieb, und der Aufbau läuft im täglichen Einsatz mit dem Server, Studio, dem Netzwerkknoten, den Beobachtungs- und Sprachdiensten, dem Broker und den zwei Helfern unten; Updates seiner Komponenten von GitHub (über Studio) wurden darauf durchgeführt. Die Docker-Compose-Topologie und ihr optionales TLS-Profil wurden mit Docker Engine in WSL wirklich gebaut und ausgeführt (`scripts/test_compose.sh`), aber **nicht auf dem Jetson**. Die Sicherungs- und Wiederherstellungsskripte haben einen bestandenen Hin-und-zurück-Test, und die beiden Helfer haben eigene Tests. **Nicht** bewiesen: eine saubere Installation auf einer Maschine, die das Projekt noch nie gesehen hat, und die ganze Docker-Topologie auf ihrem Ziel.",
  "bullets": [
   "**CM5-Testaufbau:** `scripts/deploy_cm5.sh` baut in einer sauberen Kopie, sendet ein Archiv und führt `scripts/install_cm5.sh` aus, das einen eigenen Benutzer, ein eigenes Verzeichnis und systemd-Einheiten auf eigenen Ports für Server und Studio anlegt und, mit Optionen, den MQTT-Broker, den Netzwerkknoten, den Beobachtungsdienst, das Sprach-Gateway, den Administrationsagenten, den Wartungshelfer und die tägliche Sicherung. Es berührt nie, was die Maschine sonst ausführt.",
   "**Der Wartungshelfer** (`armor_maintenance_agent.py`): die Updates der eigenen Komponenten der Anlage von GitHub (er lädt das Release-Paket, prüft seinen SHA-256 und tauscht es mit Rückfall ein), die des Betriebssystems und eine optionale Root-Konsole, alles vom Reiter *Updates* in Studio aus gesteuert; die Konsole ist aus, solange sie nicht eingeschaltet wird.",
   "**Der Administrationsagent** (`armor_admin_agent.py`): der einzige privilegierte Teil, mit einer geschlossenen Liste von Diensten, Einstellungsdateien und Broker-Konten, sodass Studio nie Root braucht.",
   "**Pakete jeder Version:** `scripts/package_component.py` baut das Paket einer Komponente (Studio, Server, Netzwerk, Beobachtungsdienst, Sprach-Gateway, DevOps), schreibt seinen SHA-256 daneben und veröffentlicht es als GitHub-Release.",
   "**Compose-Topologie:** ein nicht anonymer Mosquitto-Broker mit einer Identität je Knoten und einer ACL (einschließlich der Alarmknoten und der Zigbee-Zonen, die der Server ihnen sagt), der Server und Studio hinter einem nginx, der `/api/` weiterleitet; nur Studio wird veröffentlicht, auf Loopback. Gehärtete Container, festgelegte Images, ein internes Kernnetz und benannte Volumes für den Zustand.",
   "**TLS:** ein optionales `tls`-Compose-Profil stellt Caddy mit eigener lokaler Zertifizierungsstelle vor Studio, und eine Mosquitto-Konfiguration über TLS wird mitgeliefert ([Details](docs/BACKUP_AND_TLS.md)).",
   "**Eine Host-Firewall für die Kernmaschine** (`scripts/firewall_core.sh`): der Broker-Port nur aus dem Feldnetz, die Ports von Server und Studio nur aus dem Netz der Clients (wenn angegeben), in einer eigenen Tabelle, die nichts anderes erwähnt.",
   "**Geheimnisse:** `scripts/generate_secrets.sh` erzeugt zufällige Geheimnisse und gibt keines aus; `scripts/check-required-env.sh` lehnt fehlende, Platzhalter-, zu kurze oder wiederholte Werte ab.",
   "**Sicherung und Wiederherstellung:** `scripts/backup_data.sh` erzeugt ein AES-256-verschlüsseltes, verifiziertes Archiv der Serverdaten mit Prüfsumme (Beweise nur auf Wunsch); `scripts/restore_data.sh` listet es auf oder stellt es wieder her, ohne je vorhandene Daten zu überschreiben."
  ],
  "note": "Siehe die [Bereitstellungsgrenze](docs/DEPLOYMENT_BOUNDARY.md).",
  "fit": "ARMOR-DEVOPS ist der Weg, auf dem alles andere auf eine Maschine kommt und aktuell bleibt. Es installiert Server, Studio, den Netzwerkknoten, die Beobachtungs- und Sprachdienste und den Broker am CM5-Testaufbau, erstellt die Pakete jeder Version, die der Reiter *Updates* von [ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) von GitHub installiert, und hält die zwei kleinen Helfer, mit denen Studio die Anlage aktualisieren und ihre Dienste verwalten kann, ohne je als Root zu laufen.",
  "hardware": "Betreibt den CM5-Testaufbau im täglichen Einsatz, auf einem echten CM5, der andere Software beherbergt; noch nicht auf dem Jetson"
 },
 "zh": {
  "tagline": "部署、CM5 测试台、来自 GitHub 的更新以及安装的维护",
  "honest": "CM5 测试台的安装程序已在一台托管其他软件的真实 CM5 上运行过，其他软件保持正常，测试台日常运行着服务器、Studio、网络节点、观察和语音服务、代理以及下面两个助手；其组件已通过 Studio 从 GitHub 更新过。Docker Compose 拓扑及其可选的 TLS 配置已在 WSL 的 Docker Engine 中真实构建并运行（`scripts/test_compose.sh`），但**没有在 Jetson 上**。备份和恢复脚本有通过的往返测试，两个助手有自己的测试。**尚未**证明的是：在从未见过该项目的机器上全新安装，以及整个 Docker 拓扑在目标设备上运行。",
  "bullets": [
   "**CM5 测试台：**`scripts/deploy_cm5.sh` 在干净副本中构建，发送一个归档并运行 `scripts/install_cm5.sh`，它为服务器和 Studio 创建自己的用户、自己的目录和使用独立端口的 systemd 单元，并可通过选项加入 MQTT 代理、网络节点、观察服务、语音网关、管理代理、维护助手和每日备份。它从不触碰机器上运行的其他东西。",
   "**维护助手**（`armor_maintenance_agent.py`）：从 GitHub 更新安装自身的组件（下载发布包，检查其 SHA-256，并带回滚地替换）、操作系统更新和可选的 root 控制台，全部从 Studio 的*更新*标签页驱动；控制台除非开启否则关闭。",
   "**管理代理**（`armor_admin_agent.py`）：唯一有特权的部分，只有一份封闭的服务、设置文件和代理账户列表，因此 Studio 从不需要 root。",
   "**每个版本的包：**`scripts/package_component.py` 构建某个组件（Studio、服务器、网络、观察服务、语音网关、DevOps）的包，在旁边写入其 SHA-256，并作为 GitHub 发布版发布。",
   "**Compose 拓扑：**每个节点一个身份并带 ACL 的非匿名 Mosquitto 代理（包括报警节点和服务器告诉它们的 Zigbee 防区）、服务器，以及位于代理 `/api/` 的 nginx 之后的 Studio；只有 Studio 对外发布，且在回环上。加固的容器、固定的镜像、内部核心网络和用于状态的命名卷。",
   "**TLS：**可选的 `tls` Compose 配置在 Studio 前放置带自有本地证书颁发机构的 Caddy，并提供基于 TLS 的 Mosquitto 配置（[详情](docs/BACKUP_AND_TLS.md)）。",
   "**核心机器的主机防火墙**（`scripts/firewall_core.sh`）：代理端口只对现场网络开放，服务器和 Studio 端口只对客户端网络开放（如果给出），放在不提及其他任何内容的独立表中。",
   "**密钥：**`scripts/generate_secrets.sh` 创建随机密钥且不打印任何一个；`scripts/check-required-env.sh` 拒绝缺失、占位、过短或重复的值。",
   "**备份与恢复：**`scripts/backup_data.sh` 生成服务器数据的 AES-256 加密、经验证并带校验和的归档（除非要求否则不含证据）；`scripts/restore_data.sh` 列出或恢复它，且从不覆盖已有数据。"
  ],
  "note": "参见[部署边界](docs/DEPLOYMENT_BOUNDARY.md)。",
  "fit": "ARMOR-DEVOPS 是其他一切到达机器并保持最新的途径。它在 CM5 测试台上安装服务器、Studio、网络节点、观察和语音服务以及代理，制作 [ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) 的*更新*标签页从 GitHub 安装的每个版本的包，并保存两个小助手，让 Studio 可以在不以 root 运行的情况下更新安装并管理其服务。",
  "hardware": "日常运行 CM5 测试台，在托管其他软件的真实 CM5 上；尚未在 Jetson 上"
 },
 "ja": {
  "tagline": "デプロイ、CM5 テストベンチ、GitHub からのアップデート、設備の保守",
  "honest": "CM5 ベンチのインストーラーは、他のソフトウェアも載っている実際の CM5 で実行され（それらは正常なまま）、ベンチはサーバー、Studio、ネットワークノード、観察・音声サービス、ブローカー、下記の 2 つのヘルパーとともに日常的に動いており、コンポーネントの GitHub からのアップデート（Studio 経由）も行われています。Docker Compose の構成とオプションの TLS プロファイルは WSL 上の Docker Engine で実際にビルド・実行されています（`scripts/test_compose.sh`）が、**Jetson 上ではありません**。バックアップと復元のスクリプトには合格する往復テストがあり、2 つのヘルパーにも独自のテストがあります。**証明されていないもの：**このプロジェクトを一度も見たことがないマシンでのクリーンインストールと、Docker 構成全体の対象機での動作。",
  "bullets": [
   "**CM5 テストベンチ：**`scripts/deploy_cm5.sh` はクリーンなコピーでビルドし、アーカイブを 1 つ送って `scripts/install_cm5.sh` を実行します。これはサーバーと Studio のために専用ユーザー、専用ディレクトリ、専用ポートの systemd ユニットを作り、オプションで MQTT ブローカー、ネットワークノード、観察サービス、音声ゲートウェイ、管理エージェント、保守ヘルパー、日次バックアップも作ります。マシンで動く他のものには一切触れません。",
   "**保守ヘルパー**（`armor_maintenance_agent.py`）：設備自身のコンポーネントの GitHub からのアップデート（リリースパッケージをダウンロードし、SHA-256 を確認し、ロールバック付きで入れ替え）、OS のアップデート、任意の root コンソール。すべて Studio の*アップデート*タブから操作し、コンソールは有効にしない限りオフです。",
   "**管理エージェント**（`armor_admin_agent.py`）：唯一の特権部分で、サービス、設定ファイル、ブローカーアカウントの閉じた一覧だけを扱うため、Studio が root を必要とすることはありません。",
   "**各リリースのパッケージ：**`scripts/package_component.py` はコンポーネント（Studio、サーバー、ネットワーク、観察サービス、音声ゲートウェイ、DevOps）のパッケージを作り、隣に SHA-256 を書き、GitHub リリースとして公開します。",
   "**Compose 構成：**ノードごとに 1 つの ID と ACL（アラームノードやサーバーが伝える Zigbee ゾーンを含む）を持つ匿名でない Mosquitto ブローカー、サーバー、`/api/` をプロキシする nginx の背後の Studio。公開されるのは Studio のみで、ループバック上です。堅牢化したコンテナー、固定したイメージ、内部のコアネットワーク、状態用の名前付きボリューム。",
   "**TLS：**オプションの `tls` Compose プロファイルが、独自のローカル認証局を持つ Caddy を Studio の前に置き、TLS 上の Mosquitto 設定も用意されています（[詳細](docs/BACKUP_AND_TLS.md)）。",
   "**中核マシン用のホストファイアウォール**（`scripts/firewall_core.sh`）：ブローカーのポートはフィールドネットワークからのみ、サーバーと Studio のポートはクライアントのネットワークからのみ（指定時）、他には何も触れない専用のテーブルで。",
   "**秘密：**`scripts/generate_secrets.sh` はランダムな秘密を作って何も表示しません。`scripts/check-required-env.sh` は未設定、プレースホルダー、短すぎる、重複した値を拒否します。",
   "**バックアップと復元：**`scripts/backup_data.sh` はサーバーデータの AES-256 暗号化・検証済み・チェックサム付きアーカイブを作り（求めない限り証拠は除外）、`scripts/restore_data.sh` はそれを一覧するか、既存データを上書きせずに復元します。"
  ],
  "note": "[デプロイの境界](docs/DEPLOYMENT_BOUNDARY.md)を参照。",
  "fit": "ARMOR-DEVOPS は、他のすべてがマシンに載り、最新に保たれる手段です。CM5 テストベンチにサーバー、Studio、ネットワークノード、観察・音声サービス、ブローカーをインストールし、[ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) の*アップデート*タブが GitHub からインストールする各リリースのパッケージを作り、Studio が root で動くことなく設備を更新しサービスを管理できるようにする 2 つの小さなヘルパーを保持します。",
  "hardware": "他のソフトウェアも載る実際の CM5 で CM5 テストベンチを日常的に運用。Jetson ではまだ"
 },
 "pt": {
  "tagline": "Implementação, a bancada de testes do CM5, as suas atualizações a partir do GitHub e a manutenção da instalação",
  "honest": "O instalador da bancada do CM5 foi executado num CM5 real que aloja outro software, que se manteve saudável, e a bancada corre em uso diário com o servidor, o Studio, o nó de rede, os serviços de observação e de voz, o broker e os dois assistentes abaixo; nela foram feitas atualizações dos seus componentes a partir do GitHub (através do Studio). A topologia Docker Compose e o seu perfil TLS opcional foram construídos e executados a sério com o Docker Engine no WSL (`scripts/test_compose.sh`), mas **não no Jetson**. Os scripts de cópia de segurança e restauro têm um teste de ida e volta que passa, e os dois assistentes têm os seus próprios testes. O que **não** está provado: uma instalação limpa numa máquina que nunca viu o projeto e toda a topologia Docker no seu destino.",
  "bullets": [
   "**Bancada de testes do CM5:** `scripts/deploy_cm5.sh` compila numa cópia limpa, envia um arquivo e executa `scripts/install_cm5.sh`, que cria o seu próprio utilizador, o seu próprio diretório e unidades systemd em portas próprias para o servidor e o Studio e, com opções, o broker MQTT, o nó de rede, o serviço de observação, a porta de ligação de voz, o agente de administração, o assistente de manutenção e a cópia de segurança diária. Nunca toca no que mais a máquina executa.",
   "**O assistente de manutenção** (`armor_maintenance_agent.py`): as atualizações dos componentes da própria instalação a partir do GitHub (descarrega o pacote da versão, verifica o seu SHA-256 e troca-o com reversão), as do sistema operativo e uma consola root opcional, tudo comandado a partir do separador *Atualizações* do Studio; a consola está desligada salvo se for ativada.",
   "**O agente de administração** (`armor_admin_agent.py`): a única parte com privilégios, com uma lista fechada de serviços, ficheiros de definições e contas do broker, de modo que o Studio nunca precisa de root.",
   "**Pacotes de cada versão:** `scripts/package_component.py` constrói o pacote de um componente (Studio, servidor, rede, serviço de observação, porta de ligação de voz, DevOps), escreve o seu SHA-256 ao lado e publica-o como versão do GitHub.",
   "**Topologia Compose:** um broker Mosquitto não anónimo com uma identidade por nó e uma ACL (incluindo os nós de alarme e as zonas Zigbee que o servidor lhes diz), o servidor e o Studio atrás de um nginx que faz proxy de `/api/`; só o Studio é publicado, em loopback. Contentores reforçados, imagens fixadas, uma rede interna do núcleo e volumes com nome para o estado.",
   "**TLS:** um perfil `tls` opcional do Compose põe o Caddy, com a sua própria autoridade certificadora local, à frente do Studio, e é fornecida uma configuração do Mosquitto sobre TLS ([detalhes](docs/BACKUP_AND_TLS.md)).",
   "**Uma firewall de anfitrião para a máquina central** (`scripts/firewall_core.sh`): a porta do broker só a partir da rede de campo, as do servidor e do Studio só a partir da rede dos clientes (quando indicada), numa tabela própria que não menciona mais nada.",
   "**Segredos:** `scripts/generate_secrets.sh` cria segredos aleatórios e não imprime nenhum; `scripts/check-required-env.sh` recusa valores em falta, de exemplo, curtos ou repetidos.",
   "**Cópia de segurança e restauro:** `scripts/backup_data.sh` faz um arquivo cifrado com AES-256, verificado e com soma de verificação dos dados do servidor (sem provas salvo se pedidas); `scripts/restore_data.sh` lista-o ou restaura-o sem nunca sobrescrever dados existentes."
  ],
  "note": "Veja a [fronteira de implementação](docs/DEPLOYMENT_BOUNDARY.md).",
  "fit": "O ARMOR-DEVOPS é como tudo o resto chega a uma máquina e se mantém atualizado. Instala o servidor, o Studio, o nó de rede, os serviços de observação e de voz e o broker na bancada de testes do CM5, faz os pacotes de cada versão que o separador *Atualizações* do [ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) instala a partir do GitHub, e guarda os dois pequenos assistentes que deixam o Studio atualizar a instalação e gerir os seus serviços sem nunca correr como root.",
  "hardware": "Faz correr a bancada de testes do CM5 em uso diário, num CM5 real que aloja outro software; ainda não no Jetson"
 }
}
