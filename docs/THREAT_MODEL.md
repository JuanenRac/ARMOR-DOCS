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
| A node's equipment being written to | The solar and electrical nodes only read their inverters, batteries and meters: no request that writes to that equipment is built anywhere. What a node can move is relays (off by default in three places: the node's setting, the broker's access list and a device the operator creates) and a source-transfer switch whose channel is off by default and needs a two-step command | When that is decided, it is the most dangerous change of the project |
| A relay left closed after the link is lost | Every relay starts open, always; after the time the setting says without the broker, every closed relay opens again | A relay driven by a central has no such fall back yet |
| A zone read wrongly raising a siren | A pin that cannot be read says nothing at all, never a tamper; a restart never sounds the siren | A cut wire is a tamper, on purpose |

### The broker

One identity per node and an access list that lets each write only its own topics; the services and the server have their own. Nothing here has had its list audited, and there is no TLS on the broker yet: on a trusted LAN the readings are in clear. The broker's accounts are managed from Studio through the admin agent.

### The machine, the admin agent and the supply chain

* **The admin agent** is the only privileged part: it listens on a Unix socket reachable only by the service group and does a **closed list** of things (start, stop, restart, pause and resume the known services, write a known settings file with a copy of the old one, add or remove a broker account). It is not a shell.
* **A stolen administrator session** can therefore restart services and change settings files: the damage is bounded by that list, not by what an attacker thinks of.
* **The services** run as an unprivileged user with the system's hardening options (no new privileges, a read-only system, only the paths they write); an option set too tight can break a service in ways a test machine does not show, so they are meant to be tried on the real one.
* **Dependencies**: the server and Studio have a small list (`npm audit` is run on them by hand before a release); the firmware builds with a fixed version of the toolchain; no dependency is fetched at run time.
* **The repositories**: commits are by one account; the CI of every repository checks the manifest, the version, the changelog, the READMEs in eight languages and the links, fetches ARMOR-COMMON next to it and fails when a comparison with the contracts cannot be made, and runs every host test the nodes register; the run of ARMOR-COMMON compares the firmware the five nodes share, and ARMOR-DOCS checks what it generates. Nothing signs a commit or a release.

## What this model says to do first

1. Keep the system on a trusted LAN until TLS on every hop, a protected store for the keys and an audited access list exist.
2. Give each node its own broker identity, and each wall panel its own `panel` account.
3. Leave every command that moves the real world **off** until it is needed, and read its audit trail.
4. Put the alarm node, the router and the wall panel on a battery backup: without power there is no alarm.
5. Treat the node tokens, the installation file and the set-up codes as secrets.

## Review

This page is to be redone when a new way in appears (a new protocol, a new command, a new account) and after any real incident. It names no date on purpose: it is a description of the code as it is, not of a day.
