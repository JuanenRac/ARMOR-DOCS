# Capability matrix

What each capability is *today*, in three honest levels:

* **Simulated**: works against the simulator or a test double only.
* **Local**: works and is tested on a computer (unit, integration or host tests) with no real device.
* **Verified**: proven on the real hardware, with a measurement record.

**Nothing is verified on hardware yet.** This page is updated with every change; a row moves to
*Verified* only with evidence (see [bench acceptance](../../ARMOR-HARDWARE/docs/BENCH_ACCEPTANCE.md)).

## Contracts and server

| Capability | Level | Evidence |
|---|---|---|
| Telemetry, health and command contracts (JSON Schema) | Local | 50 conformance vectors run by Python and by ARMOR-SERVER |
| HTTP ingest with an ingest token | Local | Server integration suite |
| MQTT ingress through a real broker | Local | Run on the CM5 against A.R.M.O.R.'s own Mosquitto: anonymous clients refused, a node's telemetry reached the server and raised an alert. The publishers were scripts, **not field-node firmware** |
| A node cannot speak for another over MQTT | Local | Topic/body check tested; the broker ACL restricting each node to its own topics was exercised on the CM5 |
| Node state, stale/offline detection, disarm clearing alerts | Local | Store tests (time is injected) |
| Offline via the node's MQTT last will | Simulated | Store rule tested; the firmware last will is not compiled or run |
| Arm / disarm | Local | Requires the control token; exercised over HTTP in tests |
| Audit trail | Local | Tests check that credentials are scrubbed |
| Camera watchdog (reachability, offline alarm) | Local | Unit tests with an injected probe, and a real unreachable address in a rendered check; **not run against your cameras being unplugged** |
| Operator-only status, minimal ingest answer, node cap | Local | HTTP tests |
| Load and chaos behaviour | Local | Seeded fuzzing, a 1000-message burst, random operations and crash cases in the test suite; **no soak test on the CM5** |
| State survives a restart (mode, nodes) | Local | Persistence tests, including damaged files and a restarted server |
| Event history | Local | Event log and HTTP tests |
| Alarm output (MQTT and signed webhook) | Local | Webhook tested against a local receiver (signature, retries, no retry on 4xx); **the MQTT alarm topic has not been seen by a real broker** |
| Alert rules: dwell time and ignore zones | Local | Store and validation tests; zone coordinates are unproven against real radar frames |

## Cameras and evidence

| Capability | Level | Evidence |
|---|---|---|
| Encrypted camera vault, migration between keys | Local | Vault tests |
| Digest authentication (RFC 7616) | Local | RFC 2617 worked example; **no camera firmware tested** |
| ONVIF endpoint containment | Local | Unit tests |
| PTZ over Hi3510, PSIA, ONVIF | Simulated | Command allow-list tested; real cameras answer differently |
| RTSP path discovery, network discovery | Local | Tested with fake probes; real network behaviour unproven |
| Live MJPEG through FFmpeg, snapshots, recordings | Simulated | Failure paths tested; **not run against a real stream on the test bench** (no FFmpeg there) |
| Evidence retention, protection, SHA-256 | Local | Evidence tests |

## Clients

| Capability | Level | Evidence |
|---|---|---|
| Studio console, history, alert rules with zones drawn on a plane, seven languages, site designer | Local | Unit tests and a rendered check of the console against a deployed server |
| Studio on the CM5 test bench | Local | Deployed and opened from another computer; no cameras attached |
| Android operator client | Local | Endpoint-safety and alarm-policy unit tests and a debug build; **not run on a phone against the server** |
| Android alarm notifications and background watch | Simulated | The decision logic is unit-tested; the permission flow and the foreground service were **never run on a device** |

## Field node and AI

| Capability | Level | Evidence |
|---|---|---|
| Node message serialiser | Local | Host tests and validation by ARMOR-COMMON |
| Radar frame decoding (LD2450/LD2461) | **Absent** | Needs the vendor protocol document and captured UART data |
| Dew point, heater and day/night logic | Local | Host tests |
| Static-reflector map | Local | Host tests |
| Firmware on the ESP32-S3 (UART, MQTT, SNTP, Ethernet) | **Not built** | Needs ESP-IDF and the board |
| Day/night vision profile, fusion policy | Local | Unit tests |
| TensorRT inference, RTSP ingestion on the Jetson | **Absent** | Needs the Jetson |
| Voice intents and signed confirmation | Local | Unit tests; no speech engine |

## Deployment

| Capability | Level | Evidence |
|---|---|---|
| CM5 test bench installer (isolated, own ports) | Local | Deployed and health-checked on a real CM5 running other software, which stayed healthy |
| Docker Compose topology and TLS profile | Simulated | Parsed as YAML only: **Docker is not installed on the development PC, so neither `docker compose config` nor a run has happened** |
| Encrypted backup and restore | Local | Round-trip test script (wrong passphrase, damaged archive, restore over existing data) |
| Network segmentation (VLANs, ACLs) | Absent | A design in [SECURITY_BASELINE](SECURITY_BASELINE.md) |
