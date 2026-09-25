# Interfaces and ownership

| Producer | Interface | Consumer | Trust boundary |
|---|---|---|---|
| Field node | `armor/node/{id}/telemetry` and `/health` (MQTT) | Server | Broker identity and ACL, then schema validation |
| Server | `armor/node/{id}/command` (MQTT) | Field node | Only `armor-server` may write; allow-listed commands |
| Simulator | HTTP ingest with the ingest token | Server | The same validation as a real node |
| Server | Session-authenticated HTTP API, MJPEG, WebSocket events | Studio, Android | HttpOnly session or a camera-bound stream ticket |
| Camera | RTSP, ONVIF, Hi3510, PSIA | Server only | Credentials never leave the server |
| Server | `armor/server/alert` (MQTT) and a signed webhook | Alarm consumers | The broker ACL lets only `armor-server` write; the webhook body carries an HMAC |
| Vision service | Severity recommendation with reasons | Server | It can not actuate equipment |
| Voice service | Intent, then a service-issued confirmation for arm and disarm | Server | Allow-list and signed single-use confirmation |

The contracts live in **ARMOR-COMMON**: JSON Schemas (`telemetry`, `health`, `command`), the
OpenAPI file for the server, 68 conformance vectors (the server API, including `/history` and `/rules`, is in `armor-server-0.1.7.yaml`) and generated TypeScript and Kotlin types. Any
implementation change begins with a contract change and a conformance vector; consumers must not
infer fields from undocumented payloads. Unknown fields are rejected everywhere.
