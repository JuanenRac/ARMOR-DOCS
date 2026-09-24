# A.R.M.O.R. project catalogue

| Repository | Version | Responsibility | Maturity |
|---|---|---|---|
| ARMOR-COMMON | 0.2.0 | Message contracts, validators, conformance vectors, generated types, OpenAPI, shared launcher | Functional |
| ARMOR-RADAR | 0.2.0 | ESP32-S3 field-node firmware and its host-tested core | Scaffolding |
| ARMOR-SERVER-AI | 0.2.0 | Visual profile selection, explainable fusion policy, engine registry | Functional baseline |
| ARMOR-VOICE-AI | 0.2.0 | Offline voice intents with signed confirmation | Functional baseline |
| ARMOR-SERVER | 0.2.0 | Central state, cameras, evidence, audit | Functional |
| ARMOR-STUDIO | 0.2.0 | Operations and design console | Functional |
| ARMOR-ANDROID-CONTROL | 0.3.0 | Android operator client | Functional baseline |
| ARMOR-HARDWARE | 0.2.0 | Enclosure design and the bench acceptance matrix | Functional mechanical baseline |
| ARMOR-DEVOPS | 0.2.0 | Compose topology, CM5 test-bench installer | Functional |
| ARMOR-DOCS | 0.2.0 | Canonical documentation and the capability matrix | Functional |
| ARMOR-SIMULATOR | 0.2.0 | Scenarios and repeatable faults | Functional |

## Dependency direction

`ARMOR-COMMON` is the source of message meaning. `ARMOR-RADAR` and `ARMOR-SIMULATOR` produce its
contracts. `ARMOR-SERVER`, the visual AI and the voice service consume them. Studio and Android
are clients of the central server, not of the field network. DevOps deploys the service graph;
this repository records only validated interfaces and procedures, and what is proven
([capability matrix](CAPABILITY_MATRIX.md)).
