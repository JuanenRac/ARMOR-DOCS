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
* Security-relevant actions are written to an audit log with credentials scrubbed.
* Android sends a password only over HTTPS or over HTTP to a private-LAN IPv4 literal; a host *name*
  that merely starts like a private address is refused.
* The Studio static host sends a strict Content-Security-Policy and makes no third-party request.

## Not done yet

TLS on every hop, a secret store, broker TLS and per-node certificates, an audited ACL, a signed
Android release channel, backups with retention rules, and any penetration test. Do not expose
A.R.M.O.R. beyond the loopback interface or a trusted test LAN until the end-to-end cookie test,
a proxy and TLS are decided.
