# Threat model

What A.R.M.O.R. protects, from whom, where its pieces trust each other, what each piece does about each threat, and what is left. It is written from what the code does, piece by piece; it is **not
the result of an audit or a penetration test**, and the software has not been run on a real installation with real attackers. Read it with the [security baseline](SECURITY_BASELINE.md), which lists what is
enforced and what is not done.

## What there is to protect

| Asset | Why it matters |
|---|---|
| The state of the alarm (armed or not, what triggered) | Whoever can change it can let someone in, or keep a house awake; whoever can read it knows when nobody is home |
| The ability to disarm, silence a siren, move a relay or a switch | The consequences are physical |
| Camera passwords, camera video and the evidence taken from it | Privacy of everyone in the picture |
| The layout of the house, the devices of the network, the power readings | They tell when the house is empty and what is in it |
| The identities of the nodes and of the services on the broker | A stolen identity speaks as that node |
| The firmware that runs on the nodes | Whoever controls it controls a device inside the house |
| The machine that runs the server (the Raspberry Pi Compute Module 5 of the test bench, with an agent that may restart services; the visual and voice services are planned for a Jetson-class machine) | It holds all of the above |

## Who might attack

* **Someone passive on the network** (a Wi-Fi guest, a compromised phone or television): listens and tries the services it can reach.
* **A compromised device on the same network**, including a camera: it can send anything to anything it can reach.
* **A compromised or stolen node**: it holds its broker identity and, if the node is configured, its settings.
* **Someone with physical access** to a node, to the USB cable of a node, or to the wall panel.
* **A person who steals a phone or a wall panel** that is signed in to the server.
* **A malicious or damaged firmware release** on the account the nodes update from, or a poisoned dependency.
* **The internet**, if the server is ever exposed to it. It is not meant to be: the baseline says to keep it on the loopback interface or a trusted LAN.

Out of scope: a determined attacker with long physical access to the machine or to a node (flash can be read; secrets are not protected against that), denial of service of the radio spectrum, and the router's
and switch's own security (the VLANs of the baseline are their job).

## Where the trust boundaries are

```
 field nodes ──(MQTT, HTTP ingest)──▶ broker ──▶ server ◀──(HTTPS or HTTP)── Studio, phone, wall panel
     │  ▲                                          │  ▲
     │  └─ the node's own panel (HTTP/HTTPS,       │  └─ admin agent (a Unix socket on the same machine, root, a closed list)
     │     Bluetooth, USB: Improv)                 └──▶ services of the machine (observation, voice, network watcher)
     └─ the equipment: inverters, batteries, meters, relays, sirens, sensors (serial lines, Zigbee, pins)
```

Every arrow is a boundary: what comes across is checked as if the other side were hostile.

## Threats and what is done about them

### The server

| Threat | What is done | What is left |
|---|---|---|
| Guessing or stealing a login | Different credentials for ingest, control, operator and Studio; tokens of at least 24 characters, compared in constant time; scrypt-hashed passwords with a salt; login is rate limited; sessions and tickets are bounded in number and lifetime | A password typed on a stolen phone is as strong as that phone's lock |
| An account doing more than it should | Roles: an administrator, an operator, a viewer who only looks, and a `panel` role for a wall panel that may only read the summary, change the mode and acknowledge alarms (every other route answers 403 for it); the last administrator cannot be removed | The roles are four: there is no per-camera or per-room permission |
| A node pretending to be another | Over MQTT the node id in a message must equal the node of its topic (the broker's access list lets a node write only its own topics); over HTTP all nodes share one ingest token, and its holder can report as any of them | Use MQTT with one identity per node when that matters |
| A message that overflows or poisons the state | Strict parsers with bounds on every number and every list; an unknown field is dropped and counted, never stored; at most 256 nodes; the log of what was refused is kept (without secrets) | A node with a newer firmware than the server has its new fields ignored, not understood |
| Camera passwords leaking | Stored only in the server, AES-256-GCM encrypted with a key apart from every token; no API returns them; the installation file never holds them; a camera that is imported must have its password typed in again | The key sits on the same machine as the data |
| The installation file | Administrators only, in the audit; no password, token or key in it (a test looks for them); importing replaces only the designs (which keep their versions), the rules and the alarm levels and only adds to the lists | Whoever holds the file knows the layout of the house |
| Server-side request forgery through cameras and discovery | An ONVIF address a camera advertises must stay on the configured host; redirects are refused; discovery scans one private /24, sends no credentials and runs one scan at a time; the update of nodes accepts only local addresses | A camera on the network can still be asked for its own pages |
| Commands that move the real world | Every one is **off by default**: the switching of the electrical node, arming and disarming of an alarm panel from the server (three independent switches must all agree; the server asks for the signed-in user's PIN before it sends a disarm, and the broker's access list still matters), the relays moved by the broker or by a central; each is in the audit | When one is turned on, whoever may publish on that topic has that power |
| Someone at a phone, a wall panel or an open Studio disarms | A PIN per user, checked by the server for every route that disarms (the mode, a command to an alarm node, the voice); three wrong PINs lock the user for a minute, then five, then fifteen; the duress PIN disarms and raises a critical alarm that is told to every channel; `ARMOR_DISARM_PIN=required` makes the PIN compulsory; the wall panel has a keypad | The PIN is short and numeric; by default it is asked only of a user who has one (the server warns at start); the Android voice screen does not send one yet, so for a user with a PIN it cannot disarm; an alarm node still obeys a disarm that comes from a server that was fooled |
| A power cut or a restart leaves the house open | The alarm node keeps its mode, its alarm and its excluded zones in flash and takes them back; the server forces its files to the disk and keeps the last good copy of the state and of the users, and starts armed when it has none; the "switch it back after N seconds" of the automations survives a restart | A node with no battery is dark during the cut; a recovered copy can be a minute old |
| A task that hangs unseen (a deadlock between a module and the broker's client) | Nothing publishes while holding a lock of its module (a queue and a task of their own); the watchdog restarts the board when the task that guards the outputs stops | A fault that the watchdog does not see, in a task that is not subscribed to it |
| A node runs out of internal memory (a browser opening many tabs, the Bluetooth radio) and stops doing its job without anyone noticing | The tasks it needs are made before Bluetooth starts and the guard looks for them; the Bluetooth stack lives in the external RAM and its set-up window closes by itself; new panel connections are refused while the memory is short; a failed allocation, or ten minutes without a message to a connected broker, restarts the node once cleanly (three an hour at most, then it stays up and says so); the health report carries the internal memory and the last error | Not measured on a board; a node that restarts for a reason the guard cannot see (a hardware fault) is still seen by the server through its restart log |
| Notifications used as a channel out | Webhooks are signed when a secret is set, do not follow redirects and never block ingestion; Telegram and Home Assistant secrets live in the server's settings file and are never shown again | A message tells whoever reads it that something happened at a time |
| Home Assistant discovery | Off by default; read-only sensors only (nothing with a command topic); it reads the topics the nodes already publish | The broker must give Home Assistant read access to `armor/#`, which includes the readings |

### Studio and the phone

* **The page** is served with a strict Content-Security-Policy, makes no third-party request (the weather menu only after it is turned on), and sessions are `HttpOnly` cookies with a name that cannot be shadowed from plain HTTP. A request that changes anything must carry a header a page from another site cannot add.
* **The phone** sends a password only over HTTPS or over HTTP to a private-LAN IPv4 literal; the session is kept encrypted with the phone's keystore. The release is signed with the key of the build machine, which is not a publication key (a lost key would force a reinstall).
* **Left**: nothing prevents a signed-in browser or phone from being used by whoever picks it up. The administration pages ask the server, and the server decides, but a session is a session.

### The field nodes

| Threat | What is done | What is left |
|---|---|---|
| Someone on the network opens the node's panel | A login with a salted hash; the first set-up needs a code printed by the node; wrong passwords throttle; HTTPS with a certificate the node makes for itself | A self-signed certificate is not trusted by browsers: the first visit is a leap of faith |
| Someone near the node uses Bluetooth | Writes only over an encrypted link; every operation but `hello` needs the set-up code or a login; changes need an administrator; a phone that gets its login wrong is blocked on its own (30 seconds, doubling to five minutes) and, from twenty failures together, the channel is; five failed pairings close the door for five minutes; one phone at a time | The pairing PIN (six digits) comes from the node's set-up code, which does not change: whoever learns the code can pair, and the code is on the node's label and in its panel |
| Someone with the USB cable | The log and the flashing come out of the same socket; **Improv** lets a web page give the node a Wi-Fi network over it (checked and stored like a change from the panel) | Physical access to a node's USB is full access: the flash can be read and rewritten |
| A central that talks to the node without a broker | Off by default; a token of at least 20 characters, compared in constant time, sent as `Authorization: Bearer`; a wrong, missing or unset token answers 401 without saying which; it moves only enabled relays by name and, on an alarm node, arms or disarms with the panel's own rules (a PIN to disarm, lockout after wrong PINs) | Whoever has the token moves the relays; keep it out of logs and screenshots; it is shown once and never again |
| Poisoned firmware | An update from GitHub installs only an image that hashes to the value its release publishes, whose manifest (project, board, version and hash) carries the maintainer's Ed25519 signature (the public key is in the firmware, the private one never leaves the maintainer's computer), whose version is newer than the one running and that is a file of the repository's own releases; one the node cannot confirm in thirty seconds is rolled back. ARMOR-SERVER checks the same manifest before it hands an image to a node; the update from Studio never stores the node's panel password and only reaches local addresses | One key signs the five projects and it is a file on one computer. Secure Boot and flash encryption are off: with a cable the flash can be read and rewritten. A file uploaded by an administrator in a node's panel is not checked |
| A node's equipment being written to | The solar and electrical nodes read their inverters and meters and never write to them. A Pylontech battery can be written to, but only as described in *Writing to a battery* below. What a node can move besides is relays (off by default in three places: the node's setting, the broker's access list and a device the operator creates) and a source-transfer switch whose channel is off by default and needs a two-step command | When that is decided, it is the most dangerous change of the project |
| A relay left closed after the link is lost | Every relay starts open, always; after the time the setting says without the broker, every closed relay opens again | A relay driven by a central has no such fall back yet |
| A zone read wrongly raising a siren | A pin that cannot be read says nothing at all, never a tamper; a restart never sounds the siren | A cut wire is a tamper, on purpose |

### Writing to a battery

A Pylontech battery can be asked to change its clock, its counters, its limits and protections, its outputs, its serial number, its memory and its firmware, through the console of a gateway node. A wrong
value can disable a protection, discharge into a short, or destroy the battery for good, so the capability is built to be hard to use by mistake and by an attacker, and it has not met a real battery.

| Threat | What is done | What is left |
|---|---|---|
| Someone orders a write who should not | Off by default in three independent places: the node's setting, the server (`ARMOR_BATTERY_WRITE=1`) and the broker's access list. Only an administrator, who has just proved who they are again (the password or the second factor, also from inside the house); the operator token is not enough; the remote policy treats the routes as administration | A signed-in administrator's session that is left open can still be used for five minutes after the proof |
| A stolen or replayed order on the broker | Two steps: `arm` makes a one-time token that only the exact same operation on the exact same battery, with the serial number typed again, can spend, within two minutes; a wrong attempt withdraws the arm; three wrong in ten minutes lock every order for five; orders are not retained and are sent at most once | A broker identity that can publish to the node can still try, within those limits |
| The wrong battery or the wrong port | The serial number the person types must be the one the battery reports (a battery with none: `NOSERIAL`, only for the operations that allow it); the node re-reads the battery when it executes and refuses if it is another | The serial number is on the label: it proves care, not authority |
| Writing while the battery is working | The operations that change how it measures or protects need the current near zero and no active protection (recoveries excepted); one operation at a time per port and a pause after a write | A battery that reports a wrong current |
| A value that harms | Typed operations only; every value bounded by the ranges the maker's tool states and, for limits, sent as a whole group in the order the tool states; disabling a protection needs the risk accepted; the expert console blocks the commands that have their own operation or must never be sent (`updata`, `eepe`, `eepw`, `tbar`, `flaw`, `mm` and more) | The ranges are the maker's loose bounds, not a safe design range: they stop a typing mistake, not an informed one |
| Firmware that destroys the battery | The chip is read twice (the battery's Board and characters 8 and 9 of its serial number) and the two must agree; the image's own header must name the board that chip needs; nothing is sent otherwise; the transfer is XMODEM-1K with CRC, never abandoned in the middle by this code, and checked for each failure (checksum request, silence, cancel, error text) | An image that is the right board and a wrong build, or a power cut during the transfer |
| The battery's service password leaks | It is a setting of the node (stored like its other secrets, never shown again), sent to nobody; every text kept (captures, transcript, results) has it replaced, even if the battery echoes it; no schema has a field for it; the tests use a made-up value | Whoever reads the node's flash reads it, as for its other secrets |
| A change that leaves no trace | Every operation is kept (who, when, which battery, the reads before and after, the difference and the transcript) and told to the history under *Batteries* | The history is as safe as the server |

### Controlling the nodes

An administrator can order a node to restart, pause, resume, go on standby (its work off while it stays connected), identify itself, give a diagnostic or enter maintenance, one node or all of them, from Studio and from the phone. A stolen administrator session could use this to make a restart storm, to leave the house unprotected by pausing or putting the alarm panel and the radars on standby, or to hide an outage by putting a node in maintenance. The contract has no operation that erases settings or credentials, no factory reset, no deep sleep and no wake timer, so none of those can be ordered by anyone.

| Threat | What is done | What is left |
|---|---|---|
| A restart storm: every node restarted again and again | Administrator only, and only after a fresh proof of identity (the password or the second factor, also from inside the house); the node's name (or the word RESTART for all) typed again; at most one restart a minute for each node and a limit on the orders a minute altogether; a restart of all nodes can be rolling, one node every thirty seconds with the alarm panels last, so the house is never without every guard at once | A signed-in administrator's session that is left open can still restart nodes one after another for five minutes after the proof, each for about a minute |
| The alarm panel or the radars paused or put on standby, leaving the house unprotected | The same proof; the node's name (or the word PAUSE or STANDBY for all) typed again; Studio and the phone say in plain words that the house is NOT protected; a pause ends by itself (60 to 3600 seconds, an hour when none is said); a standby is shown on the node's own panel, in its health report and in the node health of the server, Studio and the phone, with since when and by whom; electrical nodes hold every relay open (the safe state) and the alarm panel holds its siren relay open | A standby is meant to last until someone resumes it, even across a restart: nothing forces a person to look at the node health, and a stolen session can leave an alarm panel on standby |
| Maintenance mode hiding an outage | Maintenance only holds back the alert that a node is silent, for 60 to 28800 seconds (an hour when none is said); the alerts come back if the node is still silent when it ends; it does not change what the node does; it is shown in the node health and recorded in the history | Up to eight hours of silence about one node, if nobody looks at the node health |
| An order forged or replayed on the broker | Only the server's identity can publish on `armor/control/+/command` (the broker's access list); an order has two steps and the node acts only on an `execute` that carries the one-time token it gave for that very operation in the last thirty seconds; an execute for another operation is refused and spends the token; one token at a time for each node; orders are never retained and the broadcast topic only ever carries the first step; the token is never in an answer, the history, the audit trail, a log or the file where the orders are kept | Whoever holds the server's own broker identity |
| A node commanding the others | No node's block of the access list has a write on an order topic; a node reads only its own order topic and the broadcast one and writes only its own answer | A node's password is still the password of its own subtree |
| An order given while the node cannot take it | Restart, pause and standby are refused with a reason while the node installs a firmware, receives an upload, copies a slot or runs a battery operation; an order the node is already in (pause while paused) is refused as such | A node that does not answer is reported as not answering, never as done |
| An order that leaves no trace | Every step is a `system` event of the history (requested, acknowledged, applied, refused, back, lost) and the audit trail says who ordered what, from where; the state is also in `GET /api/v1/node-health` | The history is as safe as the server |

The rules of a node (the one-time token, the pause timer, the standby kept across a restart, the maintenance timer, the busy refusals and the restart rate) are one piece of code shared by the five kinds of node and tested on a computer; the server's part is tested with a fake broker. **None of it has run on a board or against a real broker with real nodes.**

### The broker

One identity per node and an access list that lets each write only its own topics; the services and the server have their own. Nothing here has had its list audited, and there is no TLS on the broker yet: on a trusted LAN the readings are in clear. The broker's accounts are managed from Studio through the admin agent.

### The machine, the admin agent and the supply chain

* **The admin agent** is the only privileged part: it listens on a Unix socket reachable only by the service group and does a **closed list** of things (start, stop, restart, pause and resume the known services, write a known settings file with a copy of the old one, add or remove a broker account). It is not a shell.
* **A stolen administrator session** can therefore restart services and change settings files: the damage is bounded by that list, not by what an attacker thinks of.
* **The services** run as an unprivileged user with the system's hardening options (no new privileges, a read-only system, only the paths they write); an option set too tight can break a service in ways a test machine does not show, so they are meant to be tried on the real one.
* **Dependencies**: the server and Studio have a small list (`npm audit` is run on them by hand before a release); the firmware builds with a fixed version of the toolchain; no dependency is fetched at run time.
* **The repositories**: commits are by one account; the CI of every repository checks the manifest, the version, the changelog, the READMEs in eight languages and the links, fetches ARMOR-COMMON next to it and fails when a comparison with the contracts cannot be made, and runs every host test the nodes register; the run of ARMOR-COMMON compares the firmware the five nodes share, and ARMOR-DOCS checks what it generates. Nothing signs a commit or a release.

### Using the system from outside the house

The system is built to be used on the home network. When the owner opens it to the Internet (a VPN into the house, or the server behind a certificate for a name), a new group of people can reach the sign-in form, and the model changes in these ways:

* **Guessing passwords.** The sign-in is limited per address and per account, with the real address of the client when a proxy is named (`ARMOR_TRUST_PROXY`); a second factor (a time-based code, with one-use recovery codes and a growing wait after wrong codes) can be required for every sign-in or only for those from outside (`ARMOR_TOTP_REQUIRED`).
* **A stolen session.** A session from outside is shorter (12 hours, 30 minutes without use), is listed and can be closed by its owner and by an administrator, and the sensitive acts (users, the PIN, a firmware update, opening the panel of a node) ask the password again for five minutes. The remote policy (`ARMOR_REMOTE_POLICY`: full, operate or view) decides what a session from outside may do at all.
* **A new place.** The first sign-in from an address never seen before is an alert on the alarm channels.
* **The panels of the nodes** are never exposed: the server passes them on, fixed to the certificate fingerprint learned when the node was adopted, and only from the addresses of the house.
* **What is not covered.** A phone that is stolen unlocked, a compromised router that sends the client to a copy of the server (the apps rely on the certificate they are given), and denial of service by anyone who can reach the port. Opening only a VPN port, and not the server, is the recommended way: see the remote access guide of ARMOR-DEVOPS.

## What this model says to do first

1. Keep the system on a trusted LAN until TLS on every hop, a protected store for the keys and an audited access list exist.
2. Give each node its own broker identity, and each wall panel its own `panel` account.
3. Leave every command that moves the real world **off** until it is needed, and read its audit trail.
4. Put the alarm node, the router and the wall panel on a battery backup: without power there is no alarm.
5. Treat the node tokens, the installation file and the set-up codes as secrets.

## Review

This page is to be redone when a new way in appears (a new protocol, a new command, a new account) and after any real incident. It names no date on purpose: it is a description of the code as it is, not of a day.
