# A.R.M.O.R. project catalogue

<!-- catalog:begin -->
| Repository | Version | Responsibility | Maturity |
|---|---|---|---|
| ARMOR-COMMON | 0.7.7 | Shared contracts and validation library | Established |
| ARMOR-NODE-RADAR | 0.8.0.4 | ESP32-S3 PoE field-node firmware | Established |
| ARMOR-NODE-SOLAR | 0.5.8 | Solar gateway node: the firmware that reads inverters and batteries through up to ten serial ports, its web panel and the protocol library | Functional |
| ARMOR-NODE-ELECTRICAL | 0.4.9 | Electrical node: reads the voltages, currents, power and energy of the house's AC and DC network, and holds the rules for switching it | Functional |
| ARMOR-NODE-ALARM | 0.4.7 | Alarm node and panel: the zones, the arming, the delays, the siren and the PIN of the house's alarm, with the server or without it | Functional |
| ARMOR-NODE-HMI | 0.3.9 | Touch panel: shows the state of the system on a wall screen, arms, disarms and acknowledges from there, and is where the voice assistant will live | Functional |
| ARMOR-NETWORK | 0.1.4 | Local network monitor: the devices on the house's network, the internet's state and what changes | Established |
| ARMOR-SERVER | 0.8.0.6 | Central event coordinator and web API | Established |
| ARMOR-STUDIO | 0.8.1.0 | Web administration and calibration console | Established |
| ARMOR-ANDROID-CONTROL | 0.7.7 | Android operator client | Established |
| ARMOR-IOS-CONTROL | 0.0.1 | iPhone operator client | Scaffolding |
| ARMOR-SERVER-AI | 0.2.7 | Camera movement observation service (CM5 today, Jetson planned) | Established |
| ARMOR-VISION | 0.0.3 | Camera zones, masks and detection rules | Functional |
| ARMOR-VOICE-AI | 0.3.1 | Offline speech and intent gateway | Established |
| ARMOR-HARDWARE | 0.2.6 | Open hardware and parametric enclosure designs | Functional |
| ARMOR-DEVOPS | 0.6.7 | Repeatable deployment and operations | Established |
| ARMOR-SIMULATOR | 0.2.6 | Offline telemetry and environment simulator | Established |
| ARMOR-UPDATER | 0.1.5 | Detects, installs and updates the A.R.M.O.R. ecosystem's repositories on the machine it runs on | Established |
| ARMOR-DOCS | 0.8.1.2 | System architecture and operator documentation | Established |
<!-- catalog:end -->

## Dependency direction

`ARMOR-COMMON` is the source of message meaning and of the firmware base that the nodes share. `ARMOR-NODE-RADAR`, `ARMOR-NODE-SOLAR`, `ARMOR-NODE-ELECTRICAL`, `ARMOR-NODE-ALARM`, `ARMOR-NODE-HMI`,
`ARMOR-NETWORK` and `ARMOR-SIMULATOR` produce its contracts. `ARMOR-SERVER` consumes them, and the observation service (`ARMOR-SERVER-AI`) and the
voice service (`ARMOR-VOICE-AI`) are asked by it and never act by themselves. `ARMOR-VISION` holds the rules of camera zones, masks and detection as a library that no service imports yet. Studio, Android and the touch panel (`ARMOR-NODE-HMI`) are clients of the central server, not of the field
network. `ARMOR-DEVOPS` installs and updates the service graph on the CM5 test bench, `ARMOR-UPDATER` does it for a developer's machine and `ARMOR-HARDWARE` holds the enclosures;
this repository records only validated interfaces and procedures, and what is proven ([capability matrix](CAPABILITY_MATRIX.md)). The versions and maturity above are read from each
repository's own manifest by `tools/make_catalog.py`.
