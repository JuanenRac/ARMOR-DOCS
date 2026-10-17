# Security baseline

This is a design baseline plus what the code already enforces. It is **not evidence of a
completed audit**.

## Network

| VLAN | Members | Rule |
|---|---|---|
| 10 (field) | Cameras, ESP32-S3 nodes, perimeter Wi-Fi | No internet. Reach only the broker, RTSP and the API paths the core needs |
| 20 (core) | The core machine: the server and the broker (the CM5 of the test bench); the AI and the voice, planned for a Jetson-class machine | Default deny in from the other VLANs except the paths above |
| 30 (clients) | Android, Studio | Restricted access through TLS or a VPN |

Default-deny between VLANs; allow only the explicitly required paths. Every field node needs a
unique identity and a broker ACL before an outdoor deployment.

The VLANs themselves are the router's and the switch's job and are still a design. What the software provides is the core machine's own side of it: `ARMOR-DEVOPS/scripts/firewall_core.sh` opens the
broker's port only to the field network and the server's and Studio's ports only to the clients' network (see that project's deployment notes). It has not been loaded on a machine.

## What the software already enforces

* Ingest, control, operator and Studio-login credentials are different; tokens are at least 24
  characters and are compared in constant time.
* A Studio password shorter than 12 characters is refused as soon as the server is reachable from
  the network.
* Every route that configures, moves, captures, records, protects or deletes needs an operator;
  live video needs an operator or a short ticket bound to one camera.
* Camera passwords are stored only in the server, AES-256-GCM encrypted with a key separate from
  every token, and no API returns them.
* An ONVIF address a camera advertises must stay on the configured camera host; HTTP redirects
  are refused.
* Discovery scans one private /24, sends no credentials and runs one scan at a time.
* Sessions and tickets are bounded in number and lifetime; login is rate limited.
* Every command is an allow-list: a node's three, the alarm's arm and disarm, the five actions of a switch, a relay's ON, OFF and TOGGLE, and the seven orders of the network node. The validators reject an unknown field in any message; the server, on its ingest routes, drops what it does not know and counts it, so that an old server keeps working with a node of a newer firmware.
* Solar and electrical nodes only read their equipment: no request that writes to an inverter, a battery or a meter is built anywhere. What a node can move is its relays (off by default in three places) and a source-transfer switch (a channel that is off by default, two steps, never both sources closed).
* A node's Bluetooth set-up channel writes only over an encrypted link (LE Secure Connections with a six-digit PIN derived from the node's set-up code); every operation but `hello` needs the set-up code or a login, changing anything needs an administrator, a phone that fails its login is blocked for 30 seconds (doubling to five minutes), twenty failures from all phones together block the channel, five failed pairings close the door for five minutes, and one phone connects at a time. The PIN does not change while the set-up code does not: **whoever learns the code can pair**.
* Disarming asks for the PIN of the signed-in user whenever the user has one (`ARMOR_DISARM_PIN=required` makes it compulsory): in the mode of the system, in a command to an alarm node and in the voice. Three wrong PINs lock the user for a minute, then five, then fifteen; the duress PIN disarms and warns in silence.
* The server's files are forced to the disk before they take their name; the state and the users keep their last good copy, and a server that finds its state unreadable starts armed.
* Erasing the history or every recording, and lowering how much a circuit matters, need an administrator; the list of the cameras needs a session.
* Security-relevant actions are written to an audit log with credentials scrubbed.
* Android sends a password only over HTTPS or over HTTP to a private-LAN IPv4 literal; a host *name*
  that merely starts like a private address is refused.
* The Studio static host (and the nginx of its container image) sends a strict Content-Security-Policy on every file and makes no third-party request, except the Weather menu's (Open-Meteo, RainViewer, EUMETSAT, ArcGIS), which asks nothing until the account has a place saved.

## Not done yet

The Bluetooth channel has not yet been recorded running between a board and a phone. TLS on every hop, a secret store, broker TLS and per-node certificates, an audited ACL, a signed
Android release channel, backups with retention rules, and any penetration test. Do not expose
A.R.M.O.R. beyond the loopback interface or a trusted test LAN until the end-to-end cookie test,
a proxy and TLS are decided.

## Application-level findings fixed

* The perimeter state (armed or not, and the targets) is no longer readable without an operator: `GET /api/v1/status` needs one, and `GET /api/v1/info` shows the mode only to an operator.
* A field node's ingest token no longer returns the perimeter state (the answer is `accepted` and a revision).
* Over MQTT the `node_id` in a message must equal the node of its topic, so a compromised node cannot impersonate a neighbour. Over HTTP all nodes share one ingest token, so a holder of it can still report as any node: use MQTT with one identity per node when that matters.
* At most 256 distinct nodes are accepted; a decommissioned node is forgotten with `DELETE /api/v1/nodes/:id`.
* Alarm webhooks do not follow redirects, are signed when a secret is set, and never block ingestion.
