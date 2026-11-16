# Compatibility of the family

Release train: **eco-1** (a number that only goes up, one by one; `python tools/make_compatibility.py --new-train` starts the next one).

Version of the contracts (ARMOR-COMMON) when the train was prepared: **0.8.0.7**.

This table is a photograph of the train, not of today: the versions are those of the repositories when it was prepared, and `python tools/make_compatibility.py --check` lists the ones that have moved on since. A repository is listed with its own version and the version of the contracts it was last checked against by the reverse-dependency run of ARMOR-COMMON. A pin below the version of the contracts is marked `(behind)`: that repository had not been checked against those contracts yet. `docs/ecosystem.lock.json` carries the same table for tools. Both are written by `tools/make_compatibility.py` when a version of the family is prepared.

| Repository | Version | Contracts it was checked against |
|---|---|---|
| ARMOR-COMMON | 0.8.0.7 | - |
| ARMOR-NODE-RADAR | 0.8.0.8 | 0.8.0.7 |
| ARMOR-NODE-SOLAR | 0.6.2 | 0.8.0.7 |
| ARMOR-NODE-ELECTRICAL | 0.5.4 | 0.8.0.7 |
| ARMOR-NODE-ALARM | 0.5.2 | 0.8.0.7 |
| ARMOR-NODE-HMI | 0.4.3 | 0.8.0.7 |
| ARMOR-NETWORK | 0.1.6 | 0.8.0.7 |
| ARMOR-SERVER | 0.8.1.6 | 0.8.0.6 (behind) |
| ARMOR-STUDIO | 0.8.2.1 | 0.8.0.6 (behind) |
| ARMOR-ANDROID-CONTROL | 0.8.0.3 | 0.8.0.6 (behind) |
| ARMOR-IOS-CONTROL | 0.0.2 | 0.8.0.6 (behind) |
| ARMOR-SERVER-AI | 0.3.1 | 0.8.0.6 (behind) |
| ARMOR-VISION | 0.1.1 | 0.8.0.6 (behind) |
| ARMOR-VOICE-AI | 0.3.4 | 0.8.0.6 (behind) |
| ARMOR-HARDWARE | 0.2.8 | 0.8.0.7 |
| ARMOR-DEVOPS | 0.7.1 | 0.8.0.7 |
| ARMOR-SIMULATOR | 0.3.5 | 0.8.0.7 |
| ARMOR-UPDATER | 0.1.9 | 0.8.0.7 |
| ARMOR-DOCS | 0.8.1.6 | 0.8.0.7 |
