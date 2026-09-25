# Changelog

All notable changes to this project are documented here.

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
