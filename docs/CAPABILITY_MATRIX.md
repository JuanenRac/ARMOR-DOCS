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
| Arm / disarm | Local | Requires the control token, or a signed-in Studio session (audited with the user's name); exercised over HTTP in tests |
| Audit trail | Local | Tests check that credentials are scrubbed |
| Camera watchdog (reachability, offline alarm) | Local | Unit tests with an injected probe, and a real unreachable address in a rendered check; **not run against your cameras being unplugged** |
| Operator-only status, minimal ingest answer, node cap | Local | HTTP tests |
| Load and chaos behaviour | Local | Seeded fuzzing, a 1000-message burst, random operations and crash cases in the test suite; **no soak test on the CM5** |
| State survives a restart (mode, nodes) | Local | Persistence tests, including damaged files and a restarted server |
| Event history | Local | Event log and HTTP tests |
| Alarm output (MQTT and signed webhook) | Local | Webhook tested against a local receiver (signature, retries, no retry on 4xx); **the MQTT alarm topic has not been seen by a real broker** |
| Alert rules: dwell time and ignore zones | Local | Store and validation tests; zone coordinates are unproven against real radar frames |

## Devices, alarms and automation

| Capability | Level | Evidence |
|---|---|---|
| Devices of every kind (smoke, CO, gas, flood, panic, door, window, motion, glass-break, vibration, climate, light level, plugs, lights, switches, sirens, locks, valves) reporting by MQTT or push | Local | 13 server tests (state normalisation, field maps, availability, expected-interval offline) with MQTT messages injected through the bus, **not a real broker and not a real Zigbee2MQTT, Tasmota or Shelly device**; the presets follow those projects' documented topics |
| Commands to devices by MQTT and by HTTP (LAN addresses only) | Local | MQTT publishing checked with a test double and HTTP with a local receiver, including the refusal of a public address; **no real plug or light was switched** |
| Alarms from devices (always for smoke, CO, gas, flood, panic; only while armed for contacts, motion, glass-break, vibration), acknowledge and clear | Local | Server tests and a scripted browser session that triggered a device and watched the alarm, its badge and the overview |
| Automations (device, alarm or mode trigger, mode condition, up to six actions, revert after a time, rate limit) | Local | Server tests; **no siren or lamp was driven by a real rule** |
| Arm and disarm from the Studio top bar, the overview and the alarms menu | Local | Server tests and a scripted browser session |
| Site design kept on the server for every browser (revisions, conflict refusal) | Local | Server tests and a scripted session with two browsers: the second loaded the first one's design and picked up a third party's change |
| Radar (LD2450) configuration in Studio: node, channel, position, height, facing, tilt, mirror, zones | Local | Scripted browser session (add, rename, delete, persisted). It describes the installation; **it is not sent to the radar module** |
| Devices placed in the 2D and 3D designer | Local | Operation tests and a scripted browser session |

## Cameras and evidence

| Capability | Level | Evidence |
|---|---|---|
| Encrypted camera vault, migration between keys | Local | Vault tests |
| Digest authentication (RFC 7616) | Local | RFC 2617 worked example; **no camera firmware tested** |
| ONVIF endpoint containment | Local | Unit tests |
| PTZ over Hi3510, PSIA, ONVIF | Verified on one camera | Against the real cameras from the CM5: the Hi3510 unit (.210) confirms every command with `[Succeed]` and its picture changes; .203 and .204 answer nothing to Hi3510, PSIA or ONVIF (probably no PTZ hardware); .211 refuses the stored login for its web interface (its RTSP login works). A camera that confirms is the only one counted as moved; the auto-stop and press-and-hold are tested end to end in a browser against a stand-in camera |
| RTSP path discovery, network discovery | Local | Tested with fake probes; real network behaviour unproven |
| Live MJPEG through FFmpeg, snapshots, recordings | Verified on the bench | Run on the CM5 with FFmpeg 7.1 against the five real cameras: live frames from each (about 100 JPEG frames in 12 s), a snapshot and an MP4 recording saved. Not a soak test, and PTZ is a separate row |
| Evidence retention, protection, SHA-256 | Local | Evidence tests |

## Clients

| Capability | Level | Evidence |
|---|---|---|
| Studio console, history (search, filters, export, clearing), alert rules with zones drawn on a plane, PTZ in every camera view, status bar, 2D/3D site designer, seven languages | Local | Unit tests and a rendered check of the console against a deployed server |
| Studio users: create, rename, password, role, removal; your own account | Local | Store and HTTP tests (validation, last administrator, sessions ended on a password or role change, no password on disk) and a rendered check of the Configuration tab. Not tried with the Android client |
| Site designer: terrain, buildings with floors and roofs, openings, lamps, roof equipment, 2D and 3D editing, undo | Local | Geometry, operation and migration tests, and a scripted browser session (draw, reshape, rotate, drag, undo; 3D orbit, move, lift, place). No human usability test |
| Designer colours (terrain, walls, roof, doors, windows, roof equipment, lamps, every ground object), own names and a camera's own field of view and range | Local | Reading and shading tests, the defaults of every kind, a save-and-reload test through the settings and through the server document, and a scripted browser session that painted a house, the ground and a tree and saved it. The 3D view shows every colour; the 2D plan shows the ground and the walls only |
| Radar map on the site design | Local | Placement tests and a rendered check against telemetry posted to a real server. **The radar's sideways axis is an assumption** until a real LD2450 frame is compared with where a person stood |
| 270 degree node: three radars per node 75 degrees apart, created wired in Studio | Local | Geometry tests (the outer edges are 270 degrees apart, neighbours overlap 45), a test that the three sectors cover both sides of the middle radar and not the back, and a scripted browser session that created the node. **The radar's sideways axis is still an assumption** |
| Camera monitor filling its frame for every view count | Local | Layout tests and measured tile sizes in the browser at three window sizes |
| Studio on the CM5 test bench | Local | Deployed and opened from another computer; no cameras attached |
| Android operator client: arm and disarm, alarms (acknowledge), devices (state and commands), history | Local | 25 unit tests (endpoint safety, alarm policy, event, alarm and device parsing, device wording) and a debug build; the requests follow the routes the server tests cover. **Not run on a phone against the server** |
| Android alarm notifications (nodes, cameras and device alarms) and background watch | Simulated | The decision logic is unit-tested, including that a device alarm wakes the phone once and node and camera alarms are not announced twice; the permission flow and the foreground service were **never run on a device** |

## Field node and AI

| Capability | Level | Evidence |
|---|---|---|
| Node message serialiser | Local | Host tests and validation by ARMOR-COMMON |
| Ambient-light reading (VEML7700) | Local | Driver with range selection and the datasheet's correction; the conversion and the range ladder are host-tested against the datasheet's figures. **Never run on a sensor**: compare it with a reference lux meter on the bench. Without the sensor the firmware withholds telemetry (or sends an explicit, logged bench value) rather than invent one |
| LD2450 frame decoding | Local | Decoder written from the Hi-Link manual V1.00; the manual's worked example decodes to the manual's values, noisy streams resynchronise, and the resulting JSON is accepted by the contract. **No frame has been captured from a real module**, and a target's slot is not known to be a stable identity |
| LD2461 frame decoding | **Absent** | No document for the LD2461 |
| Dew point, heater and day/night logic | Local | Host tests |
| Static-reflector map | Local | Host tests |
| Firmware on the ESP32-S3-ETH (three UARTs, W5500 Ethernet, Wi-Fi, HTTP panel, MQTT, SNTP, radar statistics, mapped pins, OTA) | Local | **Builds** clean in the ESP-IDF 5.4.2 container into one image per node (about 1.3 MB with the panel), and building it found and fixed real faults. **Never run on a board**: the W5500 pins are the manufacturer's table, the radar pins are unproven until wired, and the first day of [docs/BENCH_BRINGUP.md](../../ARMOR-RADAR/docs/BENCH_BRINGUP.md) is what verifies it |
| Node web panel: set-up code, login, users, network, Wi-Fi, broker, radars, pins, update, log, in seven languages | Local | Exercised in a real browser (headless Edge) against a stand-in node: set-up, login, every page in every language with no untranslated text, saving with the node's field problems, pins, radar commands and phone width. The node side (HTTP server, sessions, storage) host-tests its logic (397 checks) and **builds**; it has never served a page from a board. **Plain HTTP** |
| Wi-Fi access point bridged to the Ethernet port, one SSID over several nodes on 1, 6 and 11 | Local | The network plan (five layouts, the channel by MAC, the set-up network) is host-tested; the driver code follows ESP-IDF's bridge example and builds. Throughput, roaming and the bridge on a real board are **unmeasured** |
| Pins mapped over the network (input, output with a safe state, PWM, analogue) as devices of the server | Local | Host tests of the command words, debounce, fall-back to the safe state, topics and reports, and of the pin table that keeps reserved pins out; the drivers build. **Never switched a real pin** |
| Over-the-air firmware update with rollback | Local | Two-slot partition table and rollback build; the upload path checks the image before switching. **Never done on a board** |
| LD2450 configuration from the node's panel (zones, one or three targets, Bluetooth, restart) | Local | Command frames built and answers parsed in host tests against the frames the public protocol documents. **Not checked against the manufacturer's document nor a module**; the panel says so and shows the raw answer |
| A link from a radar node in Studio to its own panel (the node information message) | Local | Contract vectors in ARMOR-COMMON, server and Studio tests, and the firmware's payload accepted by the contract. Not seen with a real node |
| Studio reached through a public address (several allowed origins) | Local | Tests of the origin list and of the policy; the refusal of the unlisted origin was observed against the running server. **Not yet deployed to the CM5**; plain HTTP over the Internet |
| Day/night vision profile, fusion policy | Local | Unit tests |
| TensorRT inference, RTSP ingestion on the Jetson | **Absent** | Needs the Jetson |
| Voice intents and signed confirmation | Local | Unit tests; no speech engine |

## Deployment

| Capability | Level | Evidence |
|---|---|---|
| CM5 test bench installer (isolated, own ports) | Local | Deployed and health-checked on a real CM5 running other software, which stayed healthy |
| Docker Compose topology and TLS profile | Local | Run for real with Docker Engine in WSL on the development PC (`scripts/test_compose.sh`, 12 checks): images built, broker, server (connected to the broker as `armor-server`) and Studio behind nginx answering, and HTTPS through Caddy answering. The first run found three real faults, now fixed. **Not run on the Jetson**, and the browser trust of Caddy's local authority is unverified |
| Encrypted backup and restore | Local | Round-trip test script (wrong passphrase, damaged archive, restore over existing data) |
| Network segmentation (VLANs, ACLs) | Absent | A design in [SECURITY_BASELINE](SECURITY_BASELINE.md) |
