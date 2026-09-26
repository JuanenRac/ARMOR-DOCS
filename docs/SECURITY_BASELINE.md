# Security baseline

This is a design baseline plus what the code already enforces. It is **not evidence of a
completed audit**.

## Network

| VLAN | Members | Rule |
|---|---|---|
| 10 (field) | Cameras, ESP32-S3 nodes, perimeter Wi-Fi | No internet. Reach only the broker, RTSP and the API paths the core needs |
| 20 (core) | Jetson: server, AI, voice; the broker | Default deny in from the other VLANs except the paths above |
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
* Field commands are an allow-list of three; unknown fields in any message are rejected.
* Solar and electrical nodes only read their equipment: no request that writes to an inverter, a battery or a meter is built anywhere, and the switching rules are not linked to any hardware.
* A node's Bluetooth set-up channel writes only over an encrypted link (LE Secure Connections, "just works"); every operation but `hello` needs the set-up code or a login, changing anything needs an administrator, wrong passwords lock the channel for 30 seconds (doubling to five minutes) and one phone connects at a time. "Just works" stops a passive listener, **not** someone present while the phone pairs.
* Security-relevant actions are written to an audit log with credentials scrubbed.
* Android sends a password only over HTTPS or over HTTP to a private-LAN IPv4 literal; a host *name*
  that merely starts like a private address is refused.
* The Studio static host sends a strict Content-Security-Policy and makes no third-party request.

## Not done yet

The Bluetooth channel has never run on a board or against a phone. TLS on every hop, a secret store, broker TLS and per-node certificates, an audited ACL, a signed
Android release channel, backups with retention rules, and any penetration test. Do not expose
A.R.M.O.R. beyond the loopback interface or a trusted test LAN until the end-to-end cookie test,
a proxy and TLS are decided.

## Application-level findings fixed in the second audit pass

* The perimeter state (armed or not, and the targets) is no longer readable without an operator: `GET /api/v1/status` needs one, and `GET /api/v1/info` shows the mode only to an operator.
* A field node's ingest token no longer returns the perimeter state (the answer is `accepted` and a revision).
* Over MQTT the `node_id` in a message must equal the node of its topic, so a compromised node cannot impersonate a neighbour. Over HTTP all nodes share one ingest token, so a holder of it can still report as any node: use MQTT with one identity per node when that matters.
* At most 256 distinct nodes are accepted; a decommissioned node is forgotten with `DELETE /api/v1/nodes/:id`.
* Alarm webhooks do not follow redirects, are signed when a secret is set, and never block ingestion.
