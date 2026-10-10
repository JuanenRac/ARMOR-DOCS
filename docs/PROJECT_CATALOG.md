# A.R.M.O.R. project catalogue

| Repository | Version | Responsibility | Maturity |
|---|---|---|---|
| ARMOR-COMMON | 0.4.4 | Message contracts, validators, conformance vectors, generated types, OpenAPI, shared launcher | Functional |
| ARMOR-RADAR | 0.5.7 | ESP32-S3 field-node firmware, decoders for the LD2450, LD2461 and presence sensors, its host-tested core, updates from GitHub with a progress bar and a live map | Scaffolding |
| ARMOR-SOLAR | 0.3.2 | Solar gateway node: the ESP32-S3 firmware and its panel (ten serial ports in pairs that match the board's fitting, one LED each), and and the protocols of Voltronic / MPP Solar inverters and Pylontech and ANT-BMS batteries | Scaffolding |
| ARMOR-SERVER-AI | 0.2.3 | Motion-watching service, visual profile selection, explainable fusion policy, engine registry | Functional baseline |
| ARMOR-VOICE-AI | 0.2.5 | Offline voice service: fifteen commands in seven languages, arm and disarm confirmed with a signed token | Functional baseline |
| ARMOR-ELECTRICAL | 0.2.4 | Electrical node: the firmware (sixteen PZEM meters on one serial line, a Zigbee radio lent to Zigbee2MQTT with an optional fallback client, relay outputs and analog inputs of its base board, web panel, MQTT), the meters' frames, the message of the network's readings and the rules for switching | Scaffolding |
| ARMOR-ALARM | 0.2.0 | Alarm node and panel: the firmware (up to eight wired zones, the siren on a relay, the web panel in seven languages, the Zigbee radio lent to Zigbee2MQTT and taken over by the node, with its Zigbee sensors and sirens, when the server's client is away, the messages with the server and updates from GitHub) on the electrical node's base board, and the rules of arming, delays, alarm, siren and PIN, tested on a computer; the firmware has never run on a board | Scaffolding |
| ARMOR-HMI | 0.1.5 | Touch panel for the Waveshare ESP32-S3-Touch-LCD-7C-BOX: the system's state on a wall screen, arm/disarm/acknowledge, push-to-talk voice, and the web page of the node; the firmware has never run on a board | Scaffolding |
| ARMOR-NETWORK | 0.0.6 | Local network monitor: the devices on the house's network, the state of the internet (and whose side an outage is on), what changes; it only observes | Scaffolding |
| ARMOR-SERVER | 0.5.2 | Central state (persisted), users, event history, alarms, devices, automations, solar readings with their history and the energy of each day, electrical readings and switching, the local network, a log of what the nodes send, system services, camera watchdog, cameras, evidence, audit, node firmware updates, Telegram and Home Assistant notices, voice commands | Functional |
| ARMOR-STUDIO | 0.6.8 | Operations console: alarms, devices, automations, users, history, alert rules, PTZ, radar map, solar and electrical live menus, local network, system services, weather (with a live rain-and-cloud radar), a node finder, configuration, node firmware updates, notifications, and a 2D/3D site designer (buildings with floors by level and room, interior furniture, motorised cameras, energy per day) | Functional |
| ARMOR-ANDROID-CONTROL | 0.5.0 | Android operator client: arm and disarm, alarms, devices, live radar, solar inverters and batteries, history, alarm notifications, an assistant for written and spoken commands and the configurator of the nodes | Functional baseline |
| ARMOR-HARDWARE | 0.2.3 | Enclosure design and the bench acceptance matrix | Functional mechanical baseline |
| ARMOR-DEVOPS | 0.4.5 | Compose topology, CM5 test-bench installer, backup and restore, TLS profile, own MQTT broker, observation and voice services, administration agent | Functional |
| ARMOR-DOCS | 0.7.3 | Canonical documentation and the capability matrix | Functional |
| ARMOR-SIMULATOR | 0.2.3 | Scenarios and repeatable faults | Functional |
| ARMOR-UPDATER | 0.0.7 | Detects, installs and updates the ecosystem's repositories (atomic-by-verification, adapted for a private ecosystem) | Scaffolding |

## Dependency direction

`ARMOR-COMMON` is the source of message meaning. `ARMOR-RADAR`, `ARMOR-SOLAR`, `ARMOR-ELECTRICAL`, `ARMOR-ALARM`, `ARMOR-NETWORK` and `ARMOR-SIMULATOR` produce its
contracts. `ARMOR-SERVER`, the visual AI and the voice service consume them. Studio, Android and the touch panel (ARMOR-HMI)
are clients of the central server, not of the field network. DevOps deploys the service graph;
this repository records only validated interfaces and procedures, and what is proven
([capability matrix](CAPABILITY_MATRIX.md)).
