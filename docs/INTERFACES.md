# Interfaces and ownership

| Producer | Interface | Consumer | Trust boundary |
|---|---|---|---|
| Field node | `armor/node/{id}/telemetry` and `/health` (MQTT) | Server | Broker identity and ACL, then schema validation |
| Server | `armor/node/{id}/command` (MQTT) | Field node | Only `armor-server` may write; allow-listed commands |
| Solar node | `armor/solar/{id}/{device}/state` (MQTT) or `POST /api/v1/solar` | Server | A broker identity that writes only its own subtree, then schema validation |
| Electrical node | `armor/electrical/{id}/state` (MQTT) or `POST /api/v1/electrical/readings` | Server | The same |
| Network node | `armor/network/{id}/state` (MQTT) or `POST /api/v1/network/state` | Server | The same |
| Android app | Bluetooth Low Energy: the set-up channel of a node (framed JSON on a GATT service) | Radar, solar and electrical nodes | Encrypted link, then the set-up code or a login; an administrator to change anything |
| Simulator | HTTP ingest with the ingest token | Server | The same validation as a real node |
| Server | Session-authenticated HTTP API, MJPEG, WebSocket events | Studio, Android | HttpOnly session or a camera-bound stream ticket |
| Camera | RTSP, ONVIF, Hi3510, PSIA | Server only | Credentials never leave the server |
| Server | `armor/server/alert` (MQTT) and a signed webhook | Alarm consumers | The broker ACL lets only `armor-server` write; the webhook body carries an HMAC |
| Vision service | Severity recommendation with reasons | Server | It can not actuate equipment |
| Voice service | Intent, then a service-issued confirmation for arm and disarm | Server | Allow-list and signed single-use confirmation |
| Server | Firmware of a node: the GitHub release or an uploaded file, pushed to the node's own update route with the node's login; progress is read back | Radar, solar and electrical nodes | An administrator; the SHA-256 published beside the firmware is checked |
| Server | Alarm messages: the Telegram bot API and a Home Assistant webhook | Telegram, Home Assistant | Tokens in the server's environment file, never in an answer or the audit trail |
| Observation service | Camera list and policy questions, `camera_motion` alarms | Server | A token of its own on `/api/v1/ai/*` |
| Studio | Services, broker and configuration files | Administration agent of the machine | A Unix socket for the `armor` group and a closed list of actions |

The contracts live in **ARMOR-COMMON**: JSON Schemas (`telemetry`, `health`, `command`, `info`, `solar_inverter`, `solar_battery`, `electrical`, `electrical_command`, `electrical_result`, `network`), the
OpenAPI file for the server, 330 conformance vectors (the server API, including `/history` and `/rules`, is in `armor-server-0.4.3.yaml`) and generated TypeScript and Kotlin types. Any
implementation change begins with a contract change and a conformance vector; consumers must not
infer fields from undocumented payloads. Unknown fields are rejected everywhere.
