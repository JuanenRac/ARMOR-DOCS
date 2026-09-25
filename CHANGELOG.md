# Changelog

All notable changes to this project are documented here.

## [0.2.8] - Colours and camera view in the capability matrix

- One row for the designer's colours, names and per-camera field of view, with what was checked (tests and a rendered session) and that the 2D plan shows only some of the colours.

## [0.2.7] - Firmware and the 270° node in the capability matrix

- The field-node rows say what now exists (a firmware image that builds in the ESP-IDF container, the W5500 and VEML7700 drivers, the 270° node in Studio) and, unchanged, that none of it has run on a board.

## [0.2.6] - Android with alarms, devices and arming in the capability matrix

- The Android rows say what the phone can do now (arm and disarm, alarms, devices, device-alarm notifications) and what was checked, and the client boundary no longer says it cannot arm.

## [0.2.5] - Devices, alarms, automations and the shared design in the capability matrix

- Capability matrix rows for devices, alarms, automations, arm and disarm from Studio, the design kept on the server and the radar configuration, each with what it was checked against and what was not; the project catalogue shows the new versions.

## [0.2.4] - Studio users, the radar map and the designer in the capability matrix

- Capability matrix rows for user management, the radar map and the redesigned site designer, with what each was checked against and what was not; the project catalogue shows the new versions.

## [0.2.3] - PTZ, history and designer verified

- The capability matrix records PTZ against the real cameras (one answers, one refuses the stored login, two have no PTZ), the history management and the new designer.

## [0.2.2] - Second audit pass

- The audit document records the second pass: what was found, fixed and left open. The capability matrix and interfaces follow the new behaviour.

## [0.2.1] - Full audit and one-command checks

- `tools/check_all.sh` runs every check of every repository and prints one PASS, FAIL or SKIP line each.
- Added the general audit and updated the capability matrix, catalogue and interfaces.

## [0.2.0]

- Architecture, security baseline, project catalogue, interfaces, first vertical slice and capability matrix.
- Shared README generator for the family and brand tool with a `--check` mode.
