#!/usr/bin/env bash
# ARMOR-DOCS - run every check of every ARMOR repository and print one line each.
# Copyright (C) 2026 JuanenRac (Electro Hobby 3D). GPL-3.0-or-later.
#
#   tools/check_all.sh              # everything that can run on this machine
#   tools/check_all.sh --android    # also the Gradle unit tests and debug build (slow)
#   tools/check_all.sh --compose    # also build and run the Docker Compose topology (needs Docker or WSL, slow)
#
# A check that needs a tool this machine lacks is reported as SKIP with the reason,
# never as PASS. The exit status is non-zero when any check FAILS.
set -uo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
ANDROID=0; COMPOSE=0
for argument in "$@"; do
  [[ "$argument" == "--android" ]] && ANDROID=1
  [[ "$argument" == "--compose" ]] && COMPOSE=1
done

PYTHON="${ARMOR_PYTHON:-$(command -v python3 || command -v python || true)}"
SEP="$("$PYTHON" -c 'import os; print(os.pathsep)' 2>/dev/null || echo ':')"
LOGS="$(mktemp -d)"
trap 'rm -rf -- "$LOGS"' EXIT
FAILED=0

# report NAME STATUS DETAIL
report() { printf '%-24s %-5s %s\n' "$1" "$2" "$3"; [[ "$2" == "FAIL" ]] && FAILED=1; return 0; }

# run NAME COMMAND... : runs in the repository directory (a subshell), captures the output.
run() {
  local name="$1"; shift
  if ( cd "$ROOT/$name" && "$@" ) >"$LOGS/$name.log" 2>&1; then
    report "$name" PASS "$(grep -E '(passed|Ran [0-9]+ tests|[0-9]+ checks|Tests +[0-9]+ passed|ℹ pass [0-9]+)' "$LOGS/$name.log" | tail -1 | sed 's/^ *//')"
  else
    report "$name" FAIL "see below"; sed 's/^/    | /' "$LOGS/$name.log" | tail -25
  fi
}
skip() { report "$1" SKIP "$2"; }
have() { command -v "$1" >/dev/null 2>&1; }

if have npm; then
  run ARMOR-SERVER bash -c 'npm run -s typecheck && npm test'
  run ARMOR-STUDIO bash -c 'npm run -s typecheck && npm test'
else skip ARMOR-SERVER "npm is not installed"; skip ARMOR-STUDIO "npm is not installed"; fi

if [[ -n "$PYTHON" ]]; then
  # the contracts, and the firmware the three node projects share: no copy may have drifted from ARMOR-COMMON/firmware_base
  run ARMOR-COMMON bash -c "PYTHONPATH=src \"$PYTHON\" -m unittest discover -s tests && \"$PYTHON\" tools/sync_firmware_base.py check"
  for repo in ARMOR-SIMULATOR ARMOR-SERVER-AI ARMOR-VOICE-AI; do
    run "$repo" env PYTHONPATH="src${SEP}../ARMOR-COMMON/src" "$PYTHON" -m unittest discover -s tests
  done
  run ARMOR-DOCS bash -c "\"$PYTHON\" tools/make_brand.py --check && \"$PYTHON\" tools/make_readmes.py --check"
else
  for repo in ARMOR-COMMON ARMOR-SIMULATOR ARMOR-SERVER-AI ARMOR-VOICE-AI ARMOR-DOCS; do skip "$repo" "python is not installed"; done
fi

if have cmake && (have g++ || have c++); then
  run ARMOR-RADAR bash -c 'B="$(mktemp -d)"; trap "rm -rf -- \"$B\"" EXIT; cmake -S tests -B "$B" >/dev/null && cmake --build "$B" >/dev/null && "$B/test_core" && "$B/test_node" && "$B/test_board_wifi" && "$B/test_sensors"'
  run ARMOR-SOLAR bash -c 'B="$(mktemp -d)"; trap "rm -rf -- \"$B\"" EXIT; cmake -S tests -B "$B" >/dev/null && cmake --build "$B" >/dev/null && "$B/test_solar" && "$B/test_node" && "$B/test_board_eth" && "$B/test_ble" && "$B/test_mux" && "$B/test_parallel" && "$B/test_console"'
  run ARMOR-ELECTRICAL bash -c 'B="$(mktemp -d)"; trap "rm -rf -- \"$B\"" EXIT; cmake -S tests -B "$B" >/dev/null && cmake --build "$B" >/dev/null && "$B/test_meters" && "$B/test_interlock" && "$B/test_config" && "$B/test_runner" && "$B/test_ble"'
else skip ARMOR-RADAR "no C++ compiler or cmake (the firmware itself also needs ESP-IDF)"; skip ARMOR-SOLAR "no C++ compiler or cmake"; skip ARMOR-ELECTRICAL "no C++ compiler or cmake"; fi

if have bash && have openssl; then
  run ARMOR-DEVOPS bash -c 'for f in scripts/*.sh; do bash -n "$f" || exit 1; done; bash scripts/test_backup.sh && bash scripts/test_firewall.sh'
else skip ARMOR-DEVOPS "openssl is not installed"; fi

# The Compose topology needs Docker; on Windows it lives in WSL, so it is run there when asked for.
if [[ "$COMPOSE" -eq 1 ]]; then
  if have docker; then run ARMOR-DEVOPS bash scripts/test_compose.sh
  elif have wsl; then run ARMOR-DEVOPS wsl -d Ubuntu-24.04 -- bash "$(wslpath -a "$ROOT" 2>/dev/null || echo "$ROOT")/ARMOR-DEVOPS/scripts/test_compose.sh"
  else skip "ARMOR-DEVOPS (compose)" "no Docker or WSL"; fi
else skip "ARMOR-DEVOPS (compose)" "pass --compose to build and run the topology (needs Docker, slow)"; fi

if [[ "$ANDROID" -eq 1 ]]; then
  if [[ -f "$ROOT/ARMOR-ANDROID-CONTROL/gradlew" ]]; then run ARMOR-ANDROID-CONTROL bash -c './gradlew testDebugUnitTest assembleDebug -q'
  else skip ARMOR-ANDROID-CONTROL "no Gradle wrapper"; fi
else skip ARMOR-ANDROID-CONTROL "pass --android to run it (slow)"; fi

skip ARMOR-HARDWARE "mechanical design: nothing to run without OpenSCAD and a printer"
echo
if [[ "$FAILED" -eq 0 ]]; then echo "ARMOR_CHECK_ALL=PASS"; else echo "ARMOR_CHECK_ALL=FAIL"; exit 1; fi
