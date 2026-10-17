# A.R.M.O.R. project catalogue

<!-- catalog:begin -->
| Repository | Version | Responsibility | Maturity |
|---|---|---|---|
| ARMOR-COMMON | 0.5.5 | Shared contracts and validation library | Established |
| ARMOR-RADAR | 0.6.7 | ESP32-S3 PoE field-node firmware | Established |
| ARMOR-SOLAR | 0.4.2 | Solar gateway node: the firmware that reads inverters and batteries through up to ten serial ports, its web panel and the protocol library | Functional |
| ARMOR-ELECTRICAL | 0.3.4 | Electrical node: reads the voltages, currents, power and energy of the house's AC and DC network, and holds the rules for switching it | Functional |
| ARMOR-ALARM | 0.3.1 | Alarm node and panel: the zones, the arming, the delays, the siren and the PIN of the house's alarm, with the server or without it | Functional |
| ARMOR-HMI | 0.2.5 | Touch panel: shows the state of the system on a wall screen, arms, disarms and acknowledges from there, and is where the voice assistant will live | Functional |
| ARMOR-NETWORK | 0.1.1 | Local network monitor: the devices on the house's network, the internet's state and what changes | Established |
| ARMOR-SERVER | 0.6.6 | Central event coordinator and web API | Established |
| ARMOR-STUDIO | 0.8.0.0 | Web administration and calibration console | Established |
| ARMOR-ANDROID-CONTROL | 0.5.9 | Android operator client | Established |
| ARMOR-SERVER-AI | 0.2.6 | Camera movement observation service (CM5 today, Jetson planned) | Functional |
| ARMOR-VISION | 0.0.2 | Camera zones, masks and detection rules | Functional |
| ARMOR-VOICE-AI | 0.2.10 | Offline speech and intent gateway | Functional |
| ARMOR-HARDWARE | 0.2.4 | Open hardware and parametric enclosure designs | Functional |
| ARMOR-DEVOPS | 0.5.4 | Repeatable deployment and operations | Functional |
| ARMOR-SIMULATOR | 0.2.5 | Offline telemetry and environment simulator | Established |
| ARMOR-UPDATER | 0.1.2 | Detects, installs and updates the A.R.M.O.R. ecosystem's repositories on the machine it runs on | Established |
| ARMOR-DOCS | 0.7.8 | System architecture and operator documentation | Established |
<!-- catalog:end -->

## Dependency direction

`ARMOR-COMMON` is the source of message meaning and of the firmware base that the nodes share. `ARMOR-RADAR`, `ARMOR-SOLAR`, `ARMOR-ELECTRICAL`, `ARMOR-ALARM`, `ARMOR-HMI`,
`ARMOR-NETWORK` and `ARMOR-SIMULATOR` produce its contracts. `ARMOR-SERVER` consumes them, and the observation service (`ARMOR-SERVER-AI`, with the rules of `ARMOR-VISION`) and the
voice service (`ARMOR-VOICE-AI`) are asked by it and never act by themselves. Studio, Android and the touch panel (`ARMOR-HMI`) are clients of the central server, not of the field
network. `ARMOR-DEVOPS` installs and updates the service graph on the CM5 test bench, `ARMOR-UPDATER` does it for a developer's machine and `ARMOR-HARDWARE` holds the enclosures;
this repository records only validated interfaces and procedures, and what is proven ([capability matrix](CAPABILITY_MATRIX.md)). The versions and maturity above are read from each
repository's own manifest by `tools/make_catalog.py`.
