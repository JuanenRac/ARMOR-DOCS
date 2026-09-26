# A.R.M.O.R. project catalogue

| Repository | Version | Responsibility | Maturity |
|---|---|---|---|
| ARMOR-COMMON | 0.2.3 | Message contracts, validators, conformance vectors, generated types, OpenAPI, shared launcher | Functional |
| ARMOR-RADAR | 0.2.9 | ESP32-S3 field-node firmware, decoders for the LD2450, LD2461 and presence sensors, and its host-tested core | Scaffolding |
| ARMOR-SOLAR | 0.0.8 | Solar gateway node: the ESP32-S3 firmware and its panel (ten serial ports), and the protocols of Voltronic / MPP Solar inverters and Pylontech and ANT-BMS batteries | Scaffolding |
| ARMOR-SERVER-AI | 0.2.0 | Visual profile selection, explainable fusion policy, engine registry | Functional baseline |
| ARMOR-VOICE-AI | 0.2.0 | Offline voice intents with signed confirmation | Functional baseline |
| ARMOR-ELECTRICAL | 0.0.3 | Electrical node: the firmware (sixteen PZEM meters on one serial line, web panel, MQTT), the meters' frames, the message of the network's readings and the rules for switching | Scaffolding |
| ARMOR-SERVER | 0.2.8 | Central state (persisted), users, event history, alarms, devices, automations, solar readings, camera watchdog, cameras, evidence, audit | Functional |
| ARMOR-STUDIO | 0.3.5 | Operations console, alarms, devices, automations, users, history, alert rules, PTZ, radar map, solar menus (inverters, batteries, cells, capacities) and configuration, and a 2D/3D site designer | Functional |
| ARMOR-ANDROID-CONTROL | 0.3.3 | Android operator client: arm and disarm, alarms, devices, live radar, solar inverters and batteries, history and alarm notifications | Functional baseline |
| ARMOR-HARDWARE | 0.2.1 | Enclosure design and the bench acceptance matrix | Functional mechanical baseline |
| ARMOR-DEVOPS | 0.3.1 | Compose topology, CM5 test-bench installer, backup and restore, TLS profile, own MQTT broker | Functional |
| ARMOR-DOCS | 0.4.5 | Canonical documentation and the capability matrix | Functional |
| ARMOR-SIMULATOR | 0.2.2 | Scenarios and repeatable faults | Functional |

## Dependency direction

`ARMOR-COMMON` is the source of message meaning. `ARMOR-RADAR`, `ARMOR-SOLAR`, `ARMOR-ELECTRICAL` and `ARMOR-SIMULATOR` produce its
contracts. `ARMOR-SERVER`, the visual AI and the voice service consume them. Studio and Android
are clients of the central server, not of the field network. DevOps deploys the service graph;
this repository records only validated interfaces and procedures, and what is proven
([capability matrix](CAPABILITY_MATRIX.md)).
