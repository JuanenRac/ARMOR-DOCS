# Interfaces and ownership

| Producer | Interface | Consumer | Trust boundary |
|---|---|---|---|
| Field node | `armor/node/{id}/telemetry` and `/health` (MQTT) | Server | Broker identity and ACL, then schema validation |
| Server | `armor/node/{id}/command` (MQTT) | Field node | Reserved: the access list allows it, but nothing publishes it and no node listens to it today |
| Field node | `armor/node/{id}/info` (MQTT): where its own panel is | Server | The same identity and topic rule |
| Solar node | `armor/solar/{id}/{device}/state` (MQTT) or `POST /api/v1/solar` | Server | A broker identity that writes only its own subtree, then schema validation |
| Electrical node | `armor/electrical/{id}/state` (MQTT) or `POST /api/v1/electrical/readings` | Server | The same |
| Alarm node | `armor/alarm/{id}/state` and `/result` (MQTT) | Server | The same; a state with the alarm phase and the mode disarmed is valid (a 24-hour zone, a tamper) |
| Server | `armor/alarm/{id}/command` (MQTT): arm or disarm a panel | Alarm node | Off by default in three places (the server, the node, the broker's list); the server asks for the signed-in user's PIN before a disarm and never sends it |
| Electrical node | `armor/electrical/{id}/result` and `/command` (MQTT) | Server | The command is off by default; see the switching rules |
| Relays of electrical and alarm nodes | `armor/device/{node}/{relay}/state`, `/availability` and `/set` (MQTT) | Server | Reachable only after `electrical-relays` or `alarm-relays` is run for that node |
| Network node | `armor/network/{id}/state` (MQTT) or `POST /api/v1/network/state` | Server | The same; the answer of the HTTP route carries the manual orders waiting for the node, with any login only sealed for that node |
| Server | `armor/control/{id}/command` (MQTT): one typed order to a node (restart, pause, resume, standby, identify, diagnostics, maintenance on or off) in two steps, arm then execute with a one-time token; `armor/control/all/command` carries only the first step | Every node | The broker's access list lets only `armor-server` write there; the node acts only on an execute with the token it gave for that operation within thirty seconds; no order erases settings or credentials or puts the node to deep sleep |
| Every node | `armor/control/{id}/result` (MQTT): armed, restarting, applied, diagnostics or rejected, with a typed reason | Server | A node writes only its own answer; the validators reject unknown fields |
| Studio, Android | `POST /api/v1/nodes/{id}/control`, `POST /api/v1/nodes/control`, `GET /api/v1/nodes/control/operations` | Server | An administrator with a fresh proof of identity; the node's name or a word typed again for a restart, a pause or a standby; rate limits; history and audit |
| Server | `armor/alarm/{id}/zigbee` (MQTT): the state of the Zigbee sensor of a zone, while the server holds the radio | Alarm node | Information only, never a command; the broker lets only the server write it |
| Wall panel (touch-panel node) | HTTP to the server with the session of its panel account (`studio/session`, `panel/summary`, `mode`, `alarms/acknowledge`), the read-only WebSocket `panel/events` that carries the same summary when it changes (an administrator can turn it off with `panel.live_events`; the panel asks as before without it), and `armor/node/{id}/health` and `/info` (MQTT) | Server | The `panel` role may do only those four things; the broker identity `hmi-node-*` may write only health and info |
| Wall panel (touch-panel node) | `POST /api/v1/voice/turn` (or `/api/v1/voice/v1/turn`): the audio of one spoken turn, as raw bytes in a multipart request (the older raw request when the server answers 415, 400 or 422) | Server, which passes it to the voice gateway on its own machine | The voice token the panel was given; the gateway listens on the loopback only |
| Android app | Bluetooth Low Energy: the set-up channel of a node (framed JSON on a GATT service) | Radar, solar, electrical, alarm and touch-panel nodes | Encrypted link, then the set-up code or a login; an administrator to change anything |
| Simulator | HTTP ingest with the ingest token | Server | The same validation as a real node |
| Server | Session-authenticated HTTP API, MJPEG, WebSocket events | Studio, Android | HttpOnly session or a camera-bound stream ticket |
| Camera | RTSP, ONVIF, Hi3510, PSIA | Server only | Credentials never leave the server |
| Server | `armor/server/alert` (MQTT) and a signed webhook | Alarm consumers | The broker ACL lets only `armor-server` write; the webhook body carries an HMAC |
| Vision service | Severity recommendation with reasons | Server | It can not actuate equipment |
| Voice service | Intent, then a service-issued confirmation for arm and disarm | Server | Allow-list and signed single-use confirmation |
| Server | Firmware of a node: the GitHub release or an uploaded file, pushed to the node's own update route with the node's login; progress is read back | Every node | An administrator; for a release the server checks the SHA-256 and the signed manifest (project, board, version, hash) and that the version is newer, because the node's upload route does not verify signatures; a file uploaded by hand is the administrator's own act |
| Server | Alarm messages: the Telegram bot API and a Home Assistant webhook | Telegram, Home Assistant | Tokens in the server's environment file, never in an answer or the audit trail |
| Observation service | Camera list and policy questions, `camera_motion` alarms | Server | A token of its own on `/api/v1/ai/*` |
| Studio | Services, broker and configuration files | Administration agent of the machine | A Unix socket for the `armor` group and a closed list of actions |

The contracts live in **ARMOR-COMMON**: JSON Schemas (`telemetry`, `health`, `command`, `info`, `solar_inverter`, `solar_battery`, `electrical`, `electrical_command`, `electrical_result`, `node_control_command`, `node_control_result`, `network`, `network_orders`, `alarm`, `alarm_command`, `alarm_result`, `alarm_zone_feed`, `device_state`, `server_alert`), the
OpenAPI file for the server, 685 conformance vectors (the server API, including `/history` and `/rules`, is in `armor-server.yaml`) and generated TypeScript and Kotlin types. Any
implementation change begins with a contract change and a conformance vector; consumers must not
infer fields from undocumented payloads. The validators of ARMOR-COMMON reject unknown fields; the server, reading what a node of a newer firmware says, ignores them and counts them. The continuous integration of every repository fetches ARMOR-COMMON next to it and fails when the vectors or the samples cannot be compared.
