# A.R.M.O.R. project catalogue

| Repository | Version | Responsibility | Maturity |
|---|---|---|---|
| ARMOR-COMMON | 0.2.9 | Message contracts, validators, conformance vectors, generated types, OpenAPI, shared launcher | Functional |
| ARMOR-RADAR | 0.3.0 | ESP32-S3 field-node firmware, decoders for the LD2450, LD2461 and presence sensors, and its host-tested core | Scaffolding |
| ARMOR-SOLAR | 0.0.9 | Solar gateway node: the ESP32-S3 firmware and its panel (ten serial ports), and the protocols of Voltronic / MPP Solar inverters and Pylontech and ANT-BMS batteries | Scaffolding |
| ARMOR-SERVER-AI | 0.2.1 | Visual profile selection, explainable fusion policy, engine registry | Functional baseline |
| ARMOR-VOICE-AI | 0.2.1 | Offline voice intents with signed confirmation | Functional baseline |
| ARMOR-ELECTRICAL | 0.0.5 | Electrical node: the firmware (sixteen PZEM meters on one serial line, web panel, MQTT), the meters' frames, the message of the network's readings and the rules for switching | Scaffolding |
| ARMOR-HMI | 0.0.1 | Touch panel for the Waveshare ESP32-S3-Touch-LCD-7C-BOX: the system's state on a wall screen, arm/disarm/acknowledge, push-to-talk voice, and the web page of the node; the firmware has never run on a board | Scaffolding |
| ARMOR-NETWORK | 0.0.5 | Local network monitor: the devices on the house's network, the state of the internet (and whose side an outage is on), what changes; it only observes | Scaffolding |
| ARMOR-SERVER | 0.3.6 | Central state (persisted), users, event history, alarms, devices, automations, solar readings, camera watchdog, cameras, evidence, audit | Functional |
| ARMOR-STUDIO | 0.4.4 | Operations console, alarms, devices, automations, users, history, alert rules, PTZ, radar map, solar menus (inverters, batteries, cells, capacities) and configuration, and a 2D/3D site designer | Functional |
| ARMOR-ANDROID-CONTROL | 0.3.7 | Android operator client: arm and disarm, alarms, devices, live radar, solar inverters and batteries, history and alarm notifications | Functional baseline |
| ARMOR-HARDWARE | 0.2.3 | Enclosure design and the bench acceptance matrix | Functional mechanical baseline |
| ARMOR-DEVOPS | 0.3.4 | Compose topology, CM5 test-bench installer, backup and restore, TLS profile, own MQTT broker | Functional |
| ARMOR-DOCS | 0.4.8 | Canonical documentation and the capability matrix | Functional |
| ARMOR-SIMULATOR | 0.2.3 | Scenarios and repeatable faults | Functional |
| ARMOR-UPDATER | 0.0.4 | Detects, installs and updates the ecosystem's repositories (atomic-by-verification, adapted for a private ecosystem) | Scaffolding |

## Dependency direction

`ARMOR-COMMON` is the source of message meaning. `ARMOR-RADAR`, `ARMOR-SOLAR`, `ARMOR-ELECTRICAL`, `ARMOR-NETWORK` and `ARMOR-SIMULATOR` produce its
contracts. `ARMOR-SERVER`, the visual AI and the voice service consume them. Studio, Android and the touch panel (ARMOR-HMI)
are clients of the central server, not of the field network. DevOps deploys the service graph;
this repository records only validated interfaces and procedures, and what is proven
([capability matrix](CAPABILITY_MATRIX.md)).
