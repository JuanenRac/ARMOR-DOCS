# The facts that do not depend on the language, and the words of every language, of ARMOR-VOICE-AI, in the universal README layout.
# Copyright (C) 2026 JuanenRac (Electro Hobby 3D). GPL-3.0-or-later.

FACTS = {
  "emoji": "🎙️",
  "layout": "universal",
  "license_badge": "License-GPL%203.0--or--later-blue",
  "status": [
    [
      "software",
      "yellow",
    ],
    [
      "tests",
      "green",
    ],
    [
      "hardware",
      "red",
    ],
    [
      "security",
      "yellow",
    ],
    [
      "integration",
      "yellow",
    ],
    [
      "docs",
      "green",
    ],
  ],
  "badges": [
    [
      "Language",
      "Python%203.11%2B",
      "3776ab",
    ],
    [
      "Mode",
      "offline",
      "2ea44f",
    ],
    [
      "Languages",
      "8",
      "00E5FF",
    ],
    [
      "Tests",
      "118%20passing",
      "2ea44f",
    ],
  ],
}

TEXT = {
 "en": {
   "tagline": "Offline voice intents in eight languages, with a confirmation the caller cannot forge",
   "honest": "The intent rules, the eight languages, the signed confirmation tied to its speaker, the silence policy, the local service, the turn endpoint and the audit are real and tested (118 tests), and the server asks the service on the CM5 test bench. **No speech recognition or synthesis engine is part of this repository**: `/v1/turn` runs the commands you configure for them, and none has been tried with a real microphone yet; the touch panel that is meant to carry the assistant has not run on a board.",
   "glance": [
     [
       "Role",
       "Offline speech and intent gateway (family: Core Services, parent: ARMOR-SERVER)",
     ],
     [
       "Stack",
       "Python 3.11+, standard library only",
     ],
     [
       "Tests",
       "118 (`python -m unittest discover -s tests`)",
     ],
     [
       "Commands",
       "15 (10 that ask, 5 that act), 420 phrases, 8 languages",
     ],
     [
       "Listens on",
       "`127.0.0.1:18090` (loopback only), with a token",
     ],
     [
       "Runs on",
       "The CM5 test bench (as a service) or any computer",
     ],
     [
       "On real hardware",
       "Running as a service on the CM5 test bench, asked by the server; no microphone or speech engine has been tried",
     ],
     [
       "License",
       "GPL-3.0-or-later",
     ],
   ],
   "status": {
     "software": "The intent rules, the local service and the turn endpoint run as a service on the CM5 test bench, but no speech recognition or synthesis engine is part of the repository: it runs the commands you configure for them.",
     "tests": "118 tests pass (`python -m unittest discover -s tests`): the intent rules, the eight languages, the signed confirmation tied to its speaker, the silence policy, the local service, the turn endpoint and the audit.",
     "hardware": "No microphone or speech engine has been tried, and the touch panel that is meant to carry the assistant has not run on a board.",
     "security": "The confirmation is signed and tied to its speaker, and the audit is tested on the host; there has been no independent review.",
     "integration": "The server asks the service on the CM5 test bench; the voice flow with the touch panel has not run.",
     "docs": "Eight languages and the changelog are up to date.",
   },
   "docs": [
     "[Voice safety](docs/SAFETY.md): what is understood, the confirmation, the wall-panel turn, what is recorded",
     "[The service](docs/SERVICE.md): routes, status codes and settings",
     "[Silencing by voice](docs/SILENCE_POLICY.md): the policy contract and the PIN",
   ],
   "contributing_first": "Before a pull request run `python -I tools/armor_ci_validate.py` and the tests: both must pass. See [CONTRIBUTING.md](CONTRIBUTING.md) and the [code of conduct](CODE_OF_CONDUCT.md).",
   "languages_extra": "Every sentence the service says back, every spoken command, every yes and no and every digit word of a PIN exists in all eight languages.",
   "body": {
     "overview": r"""ARMOR-VOICE-AI is the part of A.R.M.O.R. that turns **what a person says into one of fifteen commands, or into nothing**. It never does anything by itself: it decides, and [ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER) authenticates, authorises and carries out what was accepted, exactly as it would a click in the console.

The text that comes out of a speech recogniser is *untrusted input*. So it is not interpreted, searched for keywords or forwarded as a command: it is cleaned (accents, punctuation, polite filler) and must then be **exactly** one of 420 known phrases. Anything else, anything too long and any phrase that could mean two commands is *not understood*.

**What it does**

* Understands fifteen commands in **eight languages** (English, Spanish, German, French, Italian, Japanese, Chinese and Portuguese).
* Makes `arm` and `disarm` need a **second turn with a token the service signed**, tied to the intent and to the person who asked.
* Can make `silence` need a spoken **PIN** or a second confirming turn, when ARMOR-SERVER asks for it.
* Runs as a **local HTTP service** and as a **JSON-lines gateway** for adapters and tests.
* Takes the **audio of a turn** from the wall panel, runs the speech engines you configure and answers in text and, with a speech synthesiser, in audio.
* Records **decisions, never audio or words**: a SHA-256 of the transcript.

**What it does not do**

* It does not recognise or synthesise speech: those are programs the installation chooses.
* It does not arm, disarm or silence anything: an accepted command is a recommendation to ARMOR-SERVER.
* It does not disarm from the wall panel at all: the PIN is typed on the screen, never said aloud.""",
     "role": r"""[ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER) asks this service, then authenticates and authorises the command as it would a click in [ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO). It is meant to live behind the microphone of the [ARMOR-NODE-HMI](https://github.com/JuanenRac/ARMOR-NODE-HMI) wall panel (push to talk) and it answers the written and spoken assistant of [ARMOR-ANDROID-CONTROL](https://github.com/JuanenRac/ARMOR-ANDROID-CONTROL). On the test bench it is installed by [ARMOR-DEVOPS](https://github.com/JuanenRac/ARMOR-DEVOPS) (`scripts/install_cm5.sh --with-voice`).

| It talks to | How | What for |
|---|---|---|
| ARMOR-SERVER | `POST /v1/command`, `POST /v1/turn` in; `/api/v1/voice/command` out | Decide a phrase; hand the words of a spoken turn to the server's own voice route |
| ARMOR-NODE-HMI | audio of one turn (16 kHz mono PCM) | The wall panel's microphone and speaker |
| ARMOR-ANDROID-CONTROL | through the server | The written and spoken assistant |
| Speech engines | standard input and output | Hearing (e.g. whisper.cpp, Vosk) and speaking (e.g. Piper); chosen by the installation |""",
     "architecture": r"""<p align="center">
  <img src="images/architecture.svg" alt="ARMOR-VOICE-AI architecture: callers, ARMOR-SERVER, the voice service with its modules, and the speech engines chosen by the installation" width="100%">
</p>

**A spoken turn that arms the system** (the panel is asked twice, and disarming is refused):

<p align="center">
  <img src="images/turn-sequence.svg" alt="A spoken turn that arms the system: the wall panel, ARMOR-VOICE-AI, ARMOR-SERVER and the speech engines, in eleven numbered messages over two turns" width="100%">
</p>

<details>
<summary>Text version of the diagram (Mermaid)</summary>

```mermaid
sequenceDiagram
    autonumber
    participant P as Wall panel
    participant V as ARMOR-VOICE-AI
    participant E as Speech engines
    participant S as ARMOR-SERVER
    P->>V: POST /v1/turn (audio, language)
    V->>E: STT: WAV on stdin
    E-->>V: "arm the system"
    V->>S: /api/v1/voice/command {text, language}
    S-->>V: confirmation-needed + token
    V->>E: TTS: "Please confirm"
    V-->>P: heard, reply, audio
    P->>V: POST /v1/turn ("yes")
    V->>S: /api/v1/voice/command {text, confirmation}
    S-->>V: accepted
    V-->>P: "Command accepted"
    Note over V,S: "disarm" is refused here: it needs a PIN, typed on the screen
```

</details>

**Why it is built this way**

* **Why a closed list and not intent classification.** A recogniser makes mistakes and anyone can speak near a microphone. With 420 exact phrases the worst a wrong transcript can do is be ignored, and a test checks that no phrase belongs to two commands.
* **Why the service only decides.** Authentication, authorisation, the audit trail and the action stay in one place, ARMOR-SERVER; a bug here can wrongly accept a phrase but cannot touch an alarm.
* **Why the confirmation is a signed token the service issues.** A flag the caller sets (`confirmed: true`) proves nothing, so it is refused. The token is HMAC-SHA-256 signed, tied to the command and to the person, valid for 30 seconds and good once.
* **Why the speech engines are separate programs.** Models change faster than a security gateway should. They are run without a shell, with a short environment and a time limit, and the service's own secrets never reach them.
* **Why nothing is kept.** The log shows what was decided without keeping what was said.""",
     "features": r"""### The fifteen commands

| Command | Kind | Meaning | Confirmation |
|---|---|---|---|
| `status` | asks | The state of the system | no |
| `alarms` | asks | The alarms that are active | no |
| `nodes` | asks | The state of the nodes | no |
| `cameras` | asks | The state of the cameras | no |
| `radar` | asks | The state of the radars | no |
| `solar` | asks | The state of the solar system | no |
| `electrical` | asks | The electrical consumption | no |
| `network` | asks | The state of the network | no |
| `time` | asks | The time | no |
| `help` | asks | What can be said | no |
| `silence` | acts | Silence (acknowledge) the alarms | only if the server's policy asks (see below) |
| `lights_on` | acts | Turn the lights on | no |
| `lights_off` | acts | Turn the lights off | no |
| `arm` | acts | Arm the perimeter | **yes** |
| `disarm` | acts | Disarm the perimeter | **yes** |

The ten that *ask* change nothing. The five that *act* are carried out by ARMOR-SERVER with the session of the person who spoke, never by this service.

### Eight languages

English, Spanish, German, French, Italian, Japanese, Chinese and European Portuguese: the phrases (420 in all), the yes and no of a confirmation, the digit words of a spoken PIN and every sentence the service says back. Phrases are written the way a person says them and normalised when the module loads with the same function that normalises what is heard, so the two cannot drift apart. Polite filler (`please`, `por favor`, `bitte`, `s'il vous plaît`, `per favore`...) is dropped before comparing; Japanese and Chinese, written without spaces, list their phrases with and without the polite ending.

### The two-turn confirmation

1. The first turn for `arm` or `disarm` returns **no acceptance** and a `confirmation_token`.
2. The second turn echoes that token for the same intent, **for the same person**, within 30 seconds.
3. The token is signed with a secret the caller does not have, so it cannot be forged, altered, moved to another intent or another person; it works once and the nonces of the unexpired ones are never forgotten to make room for new ones (when there are too many at once, the new token is refused).

### Silencing by voice, with an optional PIN

"Silence" is accepted at once unless the installation asks for more. ARMOR-SERVER holds the setting `voice.silence_confirmation` and sends it as a policy:

| Mode | What happens on "silence" |
|---|---|
| `off` (default, and when no policy arrives) | Passed on at once |
| `double_turn` | Not carried out; the service asks to say yes, and a yes within 15 s from the same panel passes the original command on |
| `pin` | Not carried out; the service asks for the PIN, spoken as digits or as digit words in the eight languages; the right PIN within 20 s passes the command on |
| unreadable or unknown policy | `double_turn`: a broken setting never switches a protection off |

The PIN (4 to 12 digits, `ARMOR_VOICE_SILENCE_PIN`) is compared in constant time and is never logged, kept or echoed back. Three wrong PINs lock silencing by voice for **every** panel for five minutes; with `pin` asked for and no PIN set up, nothing is silenced by voice. The full contract is in [docs/SILENCE_POLICY.md](docs/SILENCE_POLICY.md).

### The wall-panel turn

`POST /v1/turn` takes the audio of one turn, runs the speech-to-text command, gives the words to ARMOR-SERVER's voice route, and answers with what was heard, what to say and, when a text-to-speech command is configured, a recording of it. The panel has no keyboard, so the question of `arm` is remembered per panel for 30 seconds and the next turn that says *yes* (in the language of the panel) confirms it and the next that says *no* cancels it. If the server answers `disarm`, the turn answers that disarming needs the PIN on the screen. Past nine seconds of listening nothing is asked of the server (the panel gives up at twelve), so what the person was told and what the house did cannot disagree.

### Decisions on record

With `--audit-file`, one JSON line per decision: time, intent, outcome and the SHA-256 of the transcript. Never audio and never the words.""",
     "security": r"""| Threat | Defence |
|---|---|
| A wrong or hostile transcript | Untrusted input: normalised, exact match against a closed list, 200 characters at most, ambiguous means *not understood*; never forwarded as a shell or device command |
| A caller claims a confirmation | `confirmed` is refused; only a token the service signed counts |
| A token is stolen, replayed or reused | Signed with HMAC-SHA-256, bound to intent and person, 30 s, single use; a token cannot outlive its issue time even if the clock jumps back |
| Another person uses someone's token | `wrong-subject` |
| Guessing the silence PIN | Constant-time comparison, 3 tries then 5 minutes locked for every panel, fails closed without a PIN |
| Someone on the network reaches the service | Loopback only (refuses another address without `--allow-remote`); token of at least 16 characters compared in constant time; 2 KB per request; a connection that stalls is closed after 15 s |
| A speech engine leaks or abuses secrets | Run without a shell, with a short environment (`PATH`, `HOME`, `LANG`, `TMPDIR`, `ARMOR_VOICE_ENGINE_*`), a time limit and a size limit; the service and server tokens never reach it |
| Exhausting the machine | At most two turns at once (a third gets 503); audio capped at 480 000 bytes |
| Logs reveal what was said | Never logged; the audit has a hash only |
| A stale turn acts late | Past nine seconds nothing is executed (504) |

Disarming by voice is **never** done from the wall panel. From the app it follows the server's `ARMOR_DISARM_PIN` (set it to `required`). Nothing here is a safety function: an accepted command is a recommendation that ARMOR-SERVER still authenticates and authorises. Read [docs/SAFETY.md](docs/SAFETY.md) for the full rules and [SECURITY.md](SECURITY.md) to report a vulnerability.""",
     "interfaces": r"""### HTTP service

| Route | Auth | What it does |
|---|---|---|
| `GET /healthz` | none | `{"ok": true, "service": "armor-voice"}` |
| `POST /v1/command` | header `X-Armor-Voice-Token` | Body `{text, language?, confirmation?, subject?, policy?, pin?}` (2 KB at most). Answers what was understood, a `confirmation_token` when a second turn is needed and `speech` in the language asked for |
| `POST /v1/turn` | same header | Body: raw 16 kHz 16-bit mono PCM, `Content-Type: audio/L16;rate=16000`, up to 480 000 bytes; headers `X-Armor-Language`, `X-Armor-Client`, `X-Armor-Policy`. Answers `{heard, reply, audio?}` |
| `POST /v1/speak` | same header | Body `{text, language}` (300 characters at most). Answers `{audio}`, the sentence said by the text-to-speech program as base64 of 16 kHz 16-bit mono PCM (it makes nothing happen and keeps nothing); 501 without that program |

A real exchange (the token is shortened):

```json
{"text": "arm the system", "subject": "u-1"}
{"accepted": false, "requires_confirmation": true, "intent": "arm", "outcome": "confirmation-needed", "confirmation_token": "eyJpIjoiYXJt...", "reason": "say it again with the confirmation within 30 s", "speech": "Please confirm"}

{"text": "arm the system", "subject": "u-1", "confirmation": "eyJpIjoiYXJt..."}
{"accepted": true, "requires_confirmation": false, "intent": "arm", "outcome": "accepted", "speech": "Command accepted"}

{"text": "open the garage"}
{"accepted": false, "requires_confirmation": false, "intent": null, "outcome": "not-understood", "reason": "the phrase is not one of the known commands", "speech": "Command not recognised"}
```

Outcomes: `accepted`, `confirmation-needed`, `confirmation-refused`, `pin-needed`, `pin-refused`, `not-understood`. A confirmation is refused as `invalid`, `expired`, `wrong-intent`, `wrong-subject` or `replayed`.

### Status codes of `/v1/turn`

| Code | Error | Meaning |
|---|---|---|
| 200 | | `{heard, reply, audio?}` |
| 401 | `unauthorized` | Missing or wrong token |
| 411 / 413 | `bad audio length` | No length, or more than 480 000 bytes |
| 415 | | Not `audio/L16;rate=16000` |
| 422 | `invalid language` | Not one of `en es de fr it ja zh pt` |
| 501 | `stt_unavailable` / `server_not_configured` | No speech-to-text command, or no server address |
| 502 | `engine_failed` / `server_<code>` / `server_not_answering` | A speech engine or the server failed |
| 503 | `busy` | Two turns are already running |
| 504 | `turn_too_slow` | The speech engine took so long that the server was not asked; nothing was executed |

### JSON-lines gateway

`python -m armor_voice_ai.gateway` reads one JSON object per line on standard input and writes the answer on standard output (2 KB per line; a line with bytes that are not UTF-8 is a line like any other). It is the same closed gateway, for speech adapters and tests.

### Contract with ARMOR-SERVER

* The server sends the silence policy on every request: `policy` in the body of `/v1/command` (and `pin` for the `pin` mode), the header `X-Armor-Policy` (a JSON object of at most 256 bytes) on `/v1/turn`.
* The server's voice route receives the words of a spoken turn at `/api/v1/voice/command` with the operator token of the installation, under the name of each panel (`X-Armor-Client`).
* Details: [docs/SERVICE.md](docs/SERVICE.md), [docs/SILENCE_POLICY.md](docs/SILENCE_POLICY.md).""",
     "configuration": r"""### Environment

| Variable | Needed | What it sets |
|---|---|---|
| `ARMOR_VOICE_TOKEN` | yes (16+ characters) | The token callers send in `X-Armor-Voice-Token` (or a line `ARMOR_VOICE_TOKEN=...` in the file of `--token-file`) |
| `ARMOR_VOICE_CONFIRM_SECRET` | recommended (16+ bytes) | Signs the confirmations. Without it a random secret is used and pending confirmations are lost when the process stops |
| `ARMOR_VOICE_STT_COMMAND` | for `/v1/turn` | The speech-to-text program: audio (WAV) on stdin, the words on stdout |
| `ARMOR_VOICE_TTS_COMMAND` | optional | The text-to-speech program: text on stdin, a 16 kHz 16-bit mono WAV on stdout |
| `ARMOR_VOICE_SERVER_URL`, `ARMOR_VOICE_SERVER_TOKEN` | for `/v1/turn` | ARMOR-SERVER and the operator token for its voice route |
| `ARMOR_VOICE_SILENCE_PIN` | for the `pin` mode | 4 to 12 digits. An invalid value stops the service at start-up without printing it |
| `ARMOR_VOICE_ENGINE_*` | optional | Passed on to the speech engines (together with `ARMOR_VOICE_LANGUAGE`, set per turn) |

### Command line

| Flag | Default | |
|---|---|---|
| `--host` | `127.0.0.1` | Address to listen on; anything but loopback is refused without `--allow-remote` |
| `--port` | `18090` | |
| `--token-file` | | File with a line `ARMOR_VOICE_TOKEN=...` |
| `--audit-file` | | Append one line per decision |
| `--allow-remote` | off | Listen on a non-loopback address (not recommended; only behind TLS) |

### Limits that are in the code

| Limit | Value |
|---|---|
| Confirmation validity | 30 s |
| Spoken question remembered per panel | 30 s |
| "Yes" after a silence question / PIN after asking | 15 s / 20 s |
| PIN tries before the lock / lock time | 3 / 5 min |
| Turn budget / panel gives up | 9 s / 12 s |
| Speech engine time limit | 25 s |
| Largest audio / largest reply audio | 480 000 bytes / 190 000 bytes |
| Request body (`/v1/command`) | 2 KB |
| Transcript length | 200 characters |
| Turns at once | 2 |

The service never writes what was said to a log, whatever the settings.""",
     "quickstart": "**Requirements:** Python 3.11+ (standard library only). Optional: a speech-to-text and a text-to-speech program for `/v1/turn`.\n\n```powershell\n$env:PYTHONPATH = \"src\"\n\n# 1. the tests\npython -m unittest discover -s tests                      # 118 tests\n\n# 2. the gateway, one JSON object per line\necho '{\"text\":\"arm the system\"}' | python -m armor_voice_ai.gateway\n\n# 3. the local HTTP service (loopback only)\n$env:ARMOR_VOICE_TOKEN = \"a-token-of-at-least-16-characters\"\npython -m armor_voice_ai.service --port 18090\n```\n\n```sh\ncurl -s http://127.0.0.1:18090/v1/command \\\n  -H \"X-Armor-Voice-Token: $ARMOR_VOICE_TOKEN\" \\\n  -d '{\"text\":\"status\",\"language\":\"de\"}'\n# {\"accepted\":true,\"requires_confirmation\":false,\"intent\":\"status\",\"outcome\":\"accepted\",\"speech\":\"Befehl akzeptiert\"}\n```\n\nTo hear and speak (`/v1/turn`), point the service at your engines and at the server:\n\n```sh\nexport ARMOR_VOICE_STT_COMMAND=\"/opt/armor/bin/hear\"        # WAV on stdin, words on stdout\nexport ARMOR_VOICE_TTS_COMMAND=\"/opt/armor/bin/speak\"       # text on stdin, WAV on stdout\nexport ARMOR_VOICE_SERVER_URL=\"https://armor-server.local\"\nexport ARMOR_VOICE_SERVER_TOKEN=\"...\"\npython -m armor_voice_ai.service --token-file /opt/armor/etc/armor.voice.env\n```\n\nThe wall panel is a device on the network and the service listens on the loopback only: either a proxy of the server forwards the turn, or `--allow-remote` is used behind TLS. The token and the audio must not cross the network in clear.\n\n`run.bat` / `run.sh` and `build.bat` / `build.sh` start the shared project workflow of [ARMOR-COMMON](https://github.com/JuanenRac/ARMOR-COMMON) (the repositories sit side by side). Pip users get the command `armor-voice-gateway`.",
     "testing": r"""```powershell
$env:PYTHONPATH = "src"
python -m unittest discover -s tests
python -I tools/armor_ci_validate.py        # manifest, version, changelog and README parity
```

| Test file | Tests | What it covers |
|---|---|---|
| `test_silence.py` | 31 | The silence policy, the spoken PIN in eight languages, the lock |
| `test_edges.py` | 29 | The line protocol, the service settings, the link to the server (a stand-in on the loopback), the engines' limits |
| `test_gateway.py` | 23 | The gateway, the confirmation, replays and forgeries |
| `test_turn.py` | 15 | The turn, the engines, the spoken yes and no, the time budget |
| `test_languages.py` | 11 | Phrases in normal form, no phrase for two commands, each language arms, disarms, asks and silences |
| `test_service.py` | 5 | The HTTP routes |

GitHub Actions runs the A.R.M.O.R. baseline on every push and pull request: the validation of the manifest, version, changelog and README parity, then the project's own build and tests.""",
     "build": "It is plain Python: nothing to compile. The version lives in `pyproject.toml`, in `armor.project.json` and in the README badge (read from the manifest); each version has its entry in [CHANGELOG.md](CHANGELOG.md). Releases are published on GitHub.",
     "troubleshooting": r"""| You see | Because | Do |
|---|---|---|
| `refusing to listen on a non-loopback address without --allow-remote` | `--host` is not `127.0.0.1`, `::1` or `localhost` | Keep loopback and let the server's proxy forward, or add `--allow-remote` behind TLS |
| `a token of at least 16 characters is needed` | `ARMOR_VOICE_TOKEN` is missing or short | Set it, or use `--token-file` |
| `ARMOR_VOICE_SILENCE_PIN is not valid` | Not 4 to 12 ASCII digits | Fix the value (it is never printed) |
| `ARMOR_VOICE_CONFIRM_SECRET is not set` (warning) | A random secret is in use | Set a secret of 16+ bytes if confirmations must survive a restart |
| 401 `unauthorized` | Missing or wrong `X-Armor-Voice-Token` | Send the token |
| 501 `stt_unavailable` | `ARMOR_VOICE_STT_COMMAND` is not set | Configure a speech-to-text program |
| 501 `server_not_configured` | No server address or token | Set `ARMOR_VOICE_SERVER_URL` and `ARMOR_VOICE_SERVER_TOKEN` |
| 502 `engine_failed` | The engine failed, timed out or answered too much (or a TTS WAV that is not 16 kHz 16-bit mono) | Run it by hand with the same input |
| 504 `turn_too_slow` | The speech engine took more than nine seconds | Use a faster model; nothing was executed |
| "Disarming needs your PIN" | Disarming is never done by voice from the panel | Use the screen |
| A spoken "yes" does nothing | The question was not remembered (it took over 12 s to ask, more than 30 s passed, or another panel answered) | Say the command again |""",
     "structure": r"""<p align="center">
  <img src="images/repository-structure.svg" alt="Repository structure of ARMOR-VOICE-AI" width="100%">
</p>

<details>
<summary>Text version of the tree</summary>

```text
ARMOR-VOICE-AI/
├── src/armor_voice_ai/        the code (standard library only)
│   ├── phrases.py             the 420 phrases of the fifteen commands, in eight languages
│   ├── intent.py              normalising and exact matching: the closed allow-list
│   ├── confirmation.py        signed, single-use, per-person confirmation tokens
│   ├── silence_policy.py      off / pin / double_turn, the spoken PIN, the lock
│   ├── session.py             the two-turn rule for each command
│   ├── gateway.py             JSON lines on stdin/stdout, the audit, the sentences said back
│   ├── service.py             the local HTTP service (/healthz, /v1/command, /v1/turn)
│   └── turn.py                one spoken turn: engines, yes/no, time budget
├── tests/                     118 tests: silence, edges, gateway, turn, languages, service
├── docs/                      SAFETY.md, SERVICE.md, SILENCE_POLICY.md
├── tools/                     the shared CI checks and project tooling
├── images/                    banner and icon
├── .github/                   CI workflow, dashboard notice, issue and pull-request templates
├── armor.project.json         manifest: version, role, maturity, build command
├── pyproject.toml             package metadata and the `armor-voice-gateway` command
├── run.sh run.bat             start through the shared project workflow
├── build.sh build.bat         build and test through the shared project workflow
├── CHANGELOG.md               what changed in each version
└── SECURITY.md SUPPORT.md CONTRIBUTING.md CODE_OF_CONDUCT.md LICENSE
```

</details>""",
     "roadmap": r"""**Known limits today**

* No speech engine ships with it, and none has been tried with a real microphone.
* The touch panel that is meant to carry the assistant has not run on a board; there is no wake word, it is push to talk.
* The turn does not say *which panel or which person* spoke: ARMOR-SERVER decides with the token it was given. Adding them to the request is a change of the contract between the server and the panel.
* No independent security review.

**Next**

* Try a real microphone and a real speech engine on the CM5 test bench.
* Run the voice flow with the touch panel once it has run on a board.
* Optional authenticated speaker or physical confirmation. A later deployment may add it, but the signed confirmation will not be removed without a documented risk review.""",
   },
 },
 "es": {
   "tagline": "Intenciones de voz sin conexión en ocho idiomas, con una confirmación que quien llama no puede falsificar",
   "honest": "Las reglas de intención, los ocho idiomas, la confirmación firmada ligada a quien habla, la política de silenciado, el servicio local, el punto de entrada de turnos y la auditoría son reales y están probados (118 pruebas), y el servidor consulta al servicio en el banco de pruebas de la CM5. **Ningún motor de reconocimiento ni de síntesis de voz forma parte de este repositorio**: `/v1/turn` ejecuta los comandos que tú configures para ello, y ninguno se ha probado todavía con un micrófono real; el panel táctil que debe llevar al asistente no ha funcionado en una placa.",
   "glance": [
     [
       "Función",
       "Pasarela de voz e intenciones sin conexión (familia: Core Services, padre: ARMOR-SERVER)",
     ],
     [
       "Tecnología",
       "Python 3.11+, solo biblioteca estándar",
     ],
     [
       "Pruebas",
       "118 (`python -m unittest discover -s tests`)",
     ],
     [
       "Comandos",
       "15 (10 que preguntan, 5 que actúan), 420 frases, 8 idiomas",
     ],
     [
       "Escucha en",
       "`127.0.0.1:18090` (solo bucle local), con token",
     ],
     [
       "Funciona en",
       "El banco de pruebas de la CM5 (como servicio) o cualquier ordenador",
     ],
     [
       "En hardware real",
       "Funciona como servicio en el banco de la CM5, consultado por el servidor; no se ha probado ningún micrófono ni motor de voz",
     ],
     [
       "Licencia",
       "GPL-3.0-or-later",
     ],
   ],
   "status": {
     "software": "Las reglas de intención, el servicio local y el punto de entrada de turnos funcionan como servicio en el banco de la CM5, pero ningún motor de reconocimiento ni síntesis de voz forma parte del repositorio: ejecuta los comandos que configures para ello.",
     "tests": "Pasan 118 pruebas (`python -m unittest discover -s tests`): las reglas de intención, los ocho idiomas, la confirmación firmada ligada a quien habla, la política de silenciado, el servicio local, el punto de entrada de turnos y la auditoría.",
     "hardware": "No se ha probado ningún micrófono ni motor de voz, y el panel táctil que debe llevar al asistente no ha funcionado en una placa.",
     "security": "La confirmación está firmada y ligada a quien habla, y la auditoría se prueba en el equipo anfitrión; no ha habido revisión independiente.",
     "integration": "El servidor consulta al servicio en el banco de la CM5; el flujo de voz con el panel táctil no ha funcionado.",
     "docs": "Los ocho idiomas y el registro de cambios están al día.",
   },
   "docs": [
     "[Seguridad de la voz](docs/SAFETY.md): qué se entiende, la confirmación, el turno del panel de pared, qué se registra",
     "[El servicio](docs/SERVICE.md): rutas, códigos de estado y ajustes",
     "[Silenciar por voz](docs/SILENCE_POLICY.md): el contrato de la política y el PIN",
   ],
   "contributing_first": "Antes de un pull request ejecuta `python -I tools/armor_ci_validate.py` y las pruebas: ambos deben pasar. Mira [CONTRIBUTING.md](CONTRIBUTING.md) y el [código de conducta](CODE_OF_CONDUCT.md).",
   "languages_extra": "Cada frase que el servicio responde, cada comando hablado, cada sí y no y cada palabra de dígito de un PIN existe en los ocho idiomas.",
   "body": {
     "overview": r"""ARMOR-VOICE-AI es la parte de A.R.M.O.R. que convierte **lo que dice una persona en uno de quince comandos, o en nada**. Nunca hace nada por sí misma: decide, y [ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER) autentica, autoriza y ejecuta lo aceptado, igual que haría con un clic en la consola.

El texto que sale de un reconocedor de voz es *entrada no fiable*. Por eso no se interpreta, ni se buscan palabras clave, ni se reenvía como comando: se limpia (acentos, puntuación, cortesías) y entonces debe ser **exactamente** una de 420 frases conocidas. Cualquier otra cosa, cualquier texto demasiado largo y cualquier frase que pudiera significar dos comandos *no se entiende*.

**Qué hace**

* Entiende quince comandos en **ocho idiomas** (inglés, español, alemán, francés, italiano, japonés, chino y portugués).
* Hace que `arm` y `disarm` necesiten un **segundo turno con un token que firmó el servicio**, ligado a la orden y a quien la pidió.
* Puede hacer que `silence` necesite un **PIN** hablado o un segundo turno de confirmación, cuando ARMOR-SERVER lo pide.
* Funciona como **servicio HTTP local** y como **pasarela de líneas JSON** para adaptadores y pruebas.
* Recibe el **audio de un turno** del panel de pared, ejecuta los motores de voz que configures y responde en texto y, con un sintetizador, en audio.
* Registra **decisiones, nunca audio ni palabras**: un SHA-256 de la transcripción.

**Qué no hace**

* No reconoce ni sintetiza voz: son programas que elige la instalación.
* No arma, desarma ni silencia nada: una orden aceptada es una recomendación para ARMOR-SERVER.
* No desarma desde el panel de pared en ningún caso: el PIN se teclea en la pantalla, nunca se dice en voz alta.""",
     "role": r"""[ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER) consulta a este servicio y luego autentica y autoriza el comando como haría con un clic en [ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO). Está pensado para vivir tras el micrófono del panel de pared [ARMOR-NODE-HMI](https://github.com/JuanenRac/ARMOR-NODE-HMI) (pulsar para hablar) y responde al asistente escrito y hablado de [ARMOR-ANDROID-CONTROL](https://github.com/JuanenRac/ARMOR-ANDROID-CONTROL). En el banco de pruebas lo instala [ARMOR-DEVOPS](https://github.com/JuanenRac/ARMOR-DEVOPS) (`scripts/install_cm5.sh --with-voice`).

| Habla con | Cómo | Para qué |
|---|---|---|
| ARMOR-SERVER | entra `POST /v1/command` y `POST /v1/turn`; sale `/api/v1/voice/command` | Decidir una frase; pasar las palabras de un turno hablado a la ruta de voz del servidor |
| ARMOR-NODE-HMI | audio de un turno (PCM mono 16 kHz) | El micrófono y el altavoz del panel de pared |
| ARMOR-ANDROID-CONTROL | a través del servidor | El asistente escrito y hablado |
| Motores de voz | entrada y salida estándar | Oír (p. ej. whisper.cpp, Vosk) y hablar (p. ej. Piper); los elige la instalación |""",
     "architecture": r"""<p align="center">
  <img src="images/architecture.svg" alt="Arquitectura de ARMOR-VOICE-AI: quien llama, ARMOR-SERVER, el servicio de voz con sus módulos y los motores de voz que elige la instalación" width="100%">
</p>

**Un turno hablado que arma el sistema** (al panel se le pregunta dos veces, y desarmar se rechaza):

<p align="center">
  <img src="images/turn-sequence.svg" alt="A spoken turn that arms the system: the wall panel, ARMOR-VOICE-AI, ARMOR-SERVER and the speech engines, in eleven numbered messages over two turns" width="100%">
</p>

<details>
<summary>Versión en texto del diagrama (Mermaid)</summary>

```mermaid
sequenceDiagram
    autonumber
    participant P as Wall panel
    participant V as ARMOR-VOICE-AI
    participant E as Speech engines
    participant S as ARMOR-SERVER
    P->>V: POST /v1/turn (audio, language)
    V->>E: STT: WAV on stdin
    E-->>V: "arm the system"
    V->>S: /api/v1/voice/command {text, language}
    S-->>V: confirmation-needed + token
    V->>E: TTS: "Please confirm"
    V-->>P: heard, reply, audio
    P->>V: POST /v1/turn ("yes")
    V->>S: /api/v1/voice/command {text, confirmation}
    S-->>V: accepted
    V-->>P: "Command accepted"
    Note over V,S: "disarm" is refused here: it needs a PIN, typed on the screen
```

</details>

**Por qué está construido así**

* **Por qué una lista cerrada y no clasificación de intenciones.** Un reconocedor se equivoca y cualquiera puede hablar cerca de un micrófono. Con 420 frases exactas lo peor que puede hacer una transcripción errónea es ser ignorada, y una prueba comprueba que ninguna frase pertenece a dos comandos.
* **Por qué el servicio solo decide.** La autenticación, la autorización, el registro de auditoría y la acción están en un único sitio, ARMOR-SERVER; un fallo aquí puede aceptar mal una frase, pero no puede tocar una alarma.
* **Por qué la confirmación es un token firmado que emite el servicio.** Una marca que pone quien llama (`confirmed: true`) no demuestra nada, así que se rechaza. El token va firmado con HMAC-SHA-256, ligado al comando y a la persona, vale 30 segundos y sirve una vez.
* **Por qué los motores de voz son programas aparte.** Los modelos cambian más deprisa de lo que debe cambiar una pasarela de seguridad. Se ejecutan sin shell, con un entorno corto y un límite de tiempo, y los secretos del propio servicio nunca les llegan.
* **Por qué no se guarda nada.** El registro muestra qué se decidió sin guardar qué se dijo.""",
     "features": r"""### Los quince comandos

| Comando | Tipo | Significado | Confirmación |
|---|---|---|---|
| `status` | pregunta | El estado del sistema | no |
| `alarms` | pregunta | Las alarmas activas | no |
| `nodes` | pregunta | El estado de los nodos | no |
| `cameras` | pregunta | El estado de las cámaras | no |
| `radar` | pregunta | El estado de los radares | no |
| `solar` | pregunta | El estado del sistema solar | no |
| `electrical` | pregunta | El consumo eléctrico | no |
| `network` | pregunta | El estado de la red | no |
| `time` | pregunta | La hora | no |
| `help` | pregunta | Qué se puede decir | no |
| `silence` | actúa | Silenciar (reconocer) las alarmas | solo si la política del servidor lo pide (ver abajo) |
| `lights_on` | actúa | Encender las luces | no |
| `lights_off` | actúa | Apagar las luces | no |
| `arm` | actúa | Armar el perímetro | **sí** |
| `disarm` | actúa | Desarmar el perímetro | **sí** |

Los diez que *preguntan* no cambian nada. Los cinco que *actúan* los ejecuta ARMOR-SERVER con la sesión de quien habló, nunca este servicio.

### Ocho idiomas

Inglés, español, alemán, francés, italiano, japonés, chino y portugués de Portugal: las frases (420 en total), el sí y el no de una confirmación, las palabras de los dígitos de un PIN hablado y cada frase que el servicio responde. Las frases se escriben como las dice una persona y se normalizan al cargar el módulo con la misma función que normaliza lo que se oye, así que no pueden separarse. Las cortesías (`please`, `por favor`, `bitte`, `s'il vous plaît`, `per favore`...) se descartan antes de comparar; el japonés y el chino, que se escriben sin espacios, listan sus frases con y sin la terminación cortés.

### La confirmación en dos turnos

1. El primer turno de `arm` o `disarm` devuelve **ninguna aceptación** y un `confirmation_token`.
2. El segundo turno repite ese token para la misma orden, **de la misma persona**, en 30 segundos.
3. El token va firmado con un secreto que quien llama no tiene, así que no se puede falsificar, alterar ni pasar a otra orden o a otra persona; funciona una sola vez y los identificadores de los que aún no han caducado nunca se olvidan para hacer sitio (si hay demasiados a la vez, se rechaza el nuevo).

### Silenciar por voz, con PIN opcional

"Silence" se acepta al instante salvo que la instalación pida más. ARMOR-SERVER guarda el ajuste `voice.silence_confirmation` y lo envía como política:

| Modo | Qué pasa con "silence" |
|---|---|
| `off` (por defecto, y si no llega política) | Se pasa al instante |
| `double_turn` | No se ejecuta; el servicio pide decir sí, y un sí en 15 s desde el mismo panel pasa la orden original |
| `pin` | No se ejecuta; el servicio pide el PIN, dicho en dígitos o en palabras en los ocho idiomas; el PIN correcto en 20 s pasa la orden |
| política ilegible o desconocida | `double_turn`: un ajuste roto nunca apaga una protección |

El PIN (de 4 a 12 dígitos, `ARMOR_VOICE_SILENCE_PIN`) se compara en tiempo constante y nunca se registra, guarda ni repite. Tres PIN erróneos bloquean el silenciado por voz en **todos** los paneles durante cinco minutos; con el modo `pin` pedido y sin PIN configurado, nada se silencia por voz. El contrato completo está en [docs/SILENCE_POLICY.md](docs/SILENCE_POLICY.md).

### El turno del panel de pared

`POST /v1/turn` recibe el audio de un turno, ejecuta el comando de voz a texto, entrega las palabras a la ruta de voz de ARMOR-SERVER y responde con lo oído, lo que hay que decir y, si hay un comando de texto a voz configurado, una grabación de la respuesta. El panel no tiene teclado, así que la pregunta de `arm` se recuerda por panel durante 30 segundos y el siguiente turno que diga *sí* (en el idioma del panel) la confirma y el que diga *no* la cancela. Si el servidor responde `disarm`, el turno contesta que para desarmar hace falta el PIN en la pantalla. Pasados nueve segundos de escucha no se consulta al servidor (el panel se rinde a los doce), así que lo que se le dijo a la persona y lo que hizo la casa no pueden contradecirse.

### Decisiones registradas

Con `--audit-file`, una línea JSON por decisión: hora, intención, resultado y el SHA-256 de la transcripción. Nunca audio y nunca las palabras.""",
     "security": r"""| Amenaza | Defensa |
|---|---|
| Una transcripción errónea u hostil | Entrada no fiable: se normaliza, coincidencia exacta con una lista cerrada, 200 caracteres como máximo, lo ambiguo *no se entiende*; nunca se reenvía como orden de shell o de dispositivo |
| Quien llama afirma una confirmación | `confirmed` se rechaza; solo cuenta un token que firmó el servicio |
| Un token robado, repetido o reutilizado | Firmado con HMAC-SHA-256, ligado a orden y persona, 30 s, un solo uso; un token no puede vivir más que su emisión aunque el reloj retroceda |
| Otra persona usa el token de alguien | `wrong-subject` |
| Adivinar el PIN de silenciado | Comparación en tiempo constante, 3 intentos y luego 5 minutos de bloqueo en todos los paneles, falla cerrado sin PIN |
| Alguien en la red alcanza el servicio | Solo bucle local (rechaza otra dirección sin `--allow-remote`); token de al menos 16 caracteres comparado en tiempo constante; 2 KB por petición; una conexión que se cuelga se cierra a los 15 s |
| Un motor de voz filtra o abusa de secretos | Se ejecuta sin shell, con entorno corto (`PATH`, `HOME`, `LANG`, `TMPDIR`, `ARMOR_VOICE_ENGINE_*`), límite de tiempo y de tamaño; los tokens del servicio y del servidor nunca le llegan |
| Agotar la máquina | Dos turnos a la vez como máximo (un tercero recibe 503); audio limitado a 480 000 bytes |
| Los registros revelan lo dicho | Nunca se registra; la auditoría solo tiene un hash |
| Un turno rancio actúa tarde | Pasados nueve segundos no se ejecuta nada (504) |

Desarmar por voz **nunca** se hace desde el panel de pared. Desde la app sigue el `ARMOR_DISARM_PIN` del servidor (ponlo en `required`). Nada de esto es una función de seguridad certificada: una orden aceptada es una recomendación que ARMOR-SERVER aún autentica y autoriza. Lee [docs/SAFETY.md](docs/SAFETY.md) para las reglas completas y [SECURITY.md](SECURITY.md) para informar de una vulnerabilidad.""",
     "interfaces": r"""### Servicio HTTP

| Ruta | Autenticación | Qué hace |
|---|---|---|
| `GET /healthz` | ninguna | `{"ok": true, "service": "armor-voice"}` |
| `POST /v1/command` | cabecera `X-Armor-Voice-Token` | Cuerpo `{text, language?, confirmation?, subject?, policy?, pin?}` (2 KB como máximo). Responde qué se entendió, un `confirmation_token` cuando hace falta un segundo turno y `speech` en el idioma pedido |
| `POST /v1/turn` | la misma cabecera | Cuerpo: PCM crudo mono de 16 bits a 16 kHz, `Content-Type: audio/L16;rate=16000`, hasta 480 000 bytes; cabeceras `X-Armor-Language`, `X-Armor-Client`, `X-Armor-Policy`. Responde `{heard, reply, audio?}` |
| `POST /v1/speak` | la misma cabecera | Cuerpo `{text, language}` (300 caracteres como máximo). Responde `{audio}`, la frase dicha por el programa de texto a voz como base64 de PCM mono de 16 bits a 16 kHz (no hace que nada ocurra y no guarda nada); 501 sin ese programa |

Un intercambio real (el token está acortado):

```json
{"text": "arm the system", "subject": "u-1"}
{"accepted": false, "requires_confirmation": true, "intent": "arm", "outcome": "confirmation-needed", "confirmation_token": "eyJpIjoiYXJt...", "reason": "say it again with the confirmation within 30 s", "speech": "Please confirm"}

{"text": "arm the system", "subject": "u-1", "confirmation": "eyJpIjoiYXJt..."}
{"accepted": true, "requires_confirmation": false, "intent": "arm", "outcome": "accepted", "speech": "Command accepted"}

{"text": "open the garage"}
{"accepted": false, "requires_confirmation": false, "intent": null, "outcome": "not-understood", "reason": "the phrase is not one of the known commands", "speech": "Command not recognised"}
```

Resultados: `accepted`, `confirmation-needed`, `confirmation-refused`, `pin-needed`, `pin-refused`, `not-understood`. Una confirmación se rechaza como `invalid`, `expired`, `wrong-intent`, `wrong-subject` o `replayed`.

### Códigos de estado de `/v1/turn`

| Código | Error | Significado |
|---|---|---|
| 200 | | `{heard, reply, audio?}` |
| 401 | `unauthorized` | Falta el token o es incorrecto |
| 411 / 413 | `bad audio length` | Sin longitud, o más de 480 000 bytes |
| 415 | | No es `audio/L16;rate=16000` |
| 422 | `invalid language` | No es uno de `en es de fr it ja zh pt` |
| 501 | `stt_unavailable` / `server_not_configured` | No hay comando de voz a texto, o no hay dirección de servidor |
| 502 | `engine_failed` / `server_<código>` / `server_not_answering` | Falló un motor de voz o el servidor |
| 503 | `busy` | Ya hay dos turnos en marcha |
| 504 | `turn_too_slow` | El motor de voz tardó tanto que no se consultó al servidor; no se ejecutó nada |

### Pasarela de líneas JSON

`python -m armor_voice_ai.gateway` lee un objeto JSON por línea por la entrada estándar y escribe la respuesta por la salida estándar (2 KB por línea; una línea con bytes que no son UTF-8 es una línea como otra cualquiera). Es la misma pasarela cerrada, para adaptadores de voz y pruebas.

### Contrato con ARMOR-SERVER

* El servidor envía la política de silenciado en cada petición: `policy` en el cuerpo de `/v1/command` (y `pin` para el modo `pin`), la cabecera `X-Armor-Policy` (un objeto JSON de 256 bytes como máximo) en `/v1/turn`.
* La ruta de voz del servidor recibe las palabras de un turno hablado en `/api/v1/voice/command` con el token de operador de la instalación, con el nombre de cada panel (`X-Armor-Client`).
* Detalles: [docs/SERVICE.md](docs/SERVICE.md), [docs/SILENCE_POLICY.md](docs/SILENCE_POLICY.md).""",
     "configuration": r"""### Entorno

| Variable | Necesaria | Qué fija |
|---|---|---|
| `ARMOR_VOICE_TOKEN` | sí (16+ caracteres) | El token que los clientes envían en `X-Armor-Voice-Token` (o una línea `ARMOR_VOICE_TOKEN=...` en el fichero de `--token-file`) |
| `ARMOR_VOICE_CONFIRM_SECRET` | recomendada (16+ bytes) | Firma las confirmaciones. Sin ella se usa un secreto aleatorio y las confirmaciones pendientes se pierden al parar el proceso |
| `ARMOR_VOICE_STT_COMMAND` | para `/v1/turn` | El programa de voz a texto: audio (WAV) por la entrada estándar, las palabras por la salida |
| `ARMOR_VOICE_TTS_COMMAND` | opcional | El programa de texto a voz: texto por la entrada estándar, un WAV mono de 16 bits a 16 kHz por la salida |
| `ARMOR_VOICE_SERVER_URL`, `ARMOR_VOICE_SERVER_TOKEN` | para `/v1/turn` | ARMOR-SERVER y el token de operador de su ruta de voz |
| `ARMOR_VOICE_SILENCE_PIN` | para el modo `pin` | De 4 a 12 dígitos. Un valor no válido detiene el servicio al arrancar sin imprimirlo |
| `ARMOR_VOICE_ENGINE_*` | opcional | Se pasan a los motores de voz (junto con `ARMOR_VOICE_LANGUAGE`, que se fija en cada turno) |

### Línea de órdenes

| Opción | Por defecto | |
|---|---|---|
| `--host` | `127.0.0.1` | Dirección en la que escuchar; cualquiera que no sea el bucle local se rechaza sin `--allow-remote` |
| `--port` | `18090` | |
| `--token-file` | | Fichero con una línea `ARMOR_VOICE_TOKEN=...` |
| `--audit-file` | | Añade una línea por decisión |
| `--allow-remote` | desactivado | Escucha en una dirección que no es de bucle local (no recomendado; solo tras TLS) |

### Límites que están en el código

| Límite | Valor |
|---|---|
| Validez de la confirmación | 30 s |
| Pregunta hablada que se recuerda por panel | 30 s |
| "Sí" tras una pregunta de silenciado / PIN tras pedirlo | 15 s / 20 s |
| Intentos de PIN antes del bloqueo / duración del bloqueo | 3 / 5 min |
| Presupuesto del turno / el panel se rinde | 9 s / 12 s |
| Límite de tiempo de un motor de voz | 25 s |
| Audio máximo / audio de respuesta máximo | 480 000 bytes / 190 000 bytes |
| Cuerpo de la petición (`/v1/command`) | 2 KB |
| Longitud de la transcripción | 200 caracteres |
| Turnos a la vez | 2 |

El servicio nunca escribe lo dicho en un registro, sean cuales sean los ajustes.""",
     "quickstart": "**Requisitos:** Python 3.11+ (solo biblioteca estándar). Opcional: un programa de voz a texto y otro de texto a voz para `/v1/turn`.\n\n```powershell\n$env:PYTHONPATH = \"src\"\n\n# 1. las pruebas\npython -m unittest discover -s tests                      # 118 pruebas\n\n# 2. la pasarela, un objeto JSON por línea\necho '{\"text\":\"arm the system\"}' | python -m armor_voice_ai.gateway\n\n# 3. el servicio HTTP local (solo bucle local)\n$env:ARMOR_VOICE_TOKEN = \"un-token-de-al-menos-16-caracteres\"\npython -m armor_voice_ai.service --port 18090\n```\n\n```sh\ncurl -s http://127.0.0.1:18090/v1/command \\\n  -H \"X-Armor-Voice-Token: $ARMOR_VOICE_TOKEN\" \\\n  -d '{\"text\":\"status\",\"language\":\"de\"}'\n# {\"accepted\":true,\"requires_confirmation\":false,\"intent\":\"status\",\"outcome\":\"accepted\",\"speech\":\"Befehl akzeptiert\"}\n```\n\nPara oír y hablar (`/v1/turn`), apunta el servicio a tus motores y al servidor:\n\n```sh\nexport ARMOR_VOICE_STT_COMMAND=\"/opt/armor/bin/hear\"        # WAV por la entrada, palabras por la salida\nexport ARMOR_VOICE_TTS_COMMAND=\"/opt/armor/bin/speak\"       # texto por la entrada, WAV por la salida\nexport ARMOR_VOICE_SERVER_URL=\"https://armor-server.local\"\nexport ARMOR_VOICE_SERVER_TOKEN=\"...\"\npython -m armor_voice_ai.service --token-file /opt/armor/etc/armor.voice.env\n```\n\nEl panel de pared es un dispositivo de la red y el servicio escucha solo en el bucle local: o bien un proxy del servidor reenvía el turno, o se usa `--allow-remote` tras TLS. El token y el audio no deben cruzar la red en claro.\n\n`run.bat` / `run.sh` y `build.bat` / `build.sh` lanzan el flujo de proyecto compartido de [ARMOR-COMMON](https://github.com/JuanenRac/ARMOR-COMMON) (los repositorios están uno junto a otro). Con pip se dispone del comando `armor-voice-gateway`.",
     "testing": r"""```powershell
$env:PYTHONPATH = "src"
python -m unittest discover -s tests
python -I tools/armor_ci_validate.py        # manifiesto, versión, registro de cambios y paridad del README
```

| Fichero de pruebas | Pruebas | Qué cubre |
|---|---|---|
| `test_silence.py` | 31 | La política de silenciado, el PIN hablado en ocho idiomas, el bloqueo |
| `test_edges.py` | 29 | El protocolo de líneas, los ajustes del servicio, el enlace con el servidor (un doble en el bucle local), los límites de los motores |
| `test_gateway.py` | 23 | La pasarela, la confirmación, repeticiones y falsificaciones |
| `test_turn.py` | 15 | El turno, los motores, el sí y el no hablados, el presupuesto de tiempo |
| `test_languages.py` | 11 | Frases en forma normal, ninguna frase para dos comandos, cada idioma arma, desarma, pregunta y silencia |
| `test_service.py` | 5 | Las rutas HTTP |

GitHub Actions ejecuta la base de A.R.M.O.R. en cada push y pull request: la validación del manifiesto, la versión, el registro de cambios y la paridad del README, y después la compilación y las pruebas propias del proyecto.""",
     "build": "Es Python puro: no hay nada que compilar. La versión vive en `pyproject.toml`, en `armor.project.json` y en la insignia del README (leída del manifiesto); cada versión tiene su entrada en [CHANGELOG.md](CHANGELOG.md). Las versiones se publican en GitHub.",
     "troubleshooting": r"""| Ves | Porque | Haz |
|---|---|---|
| `refusing to listen on a non-loopback address without --allow-remote` | `--host` no es `127.0.0.1`, `::1` ni `localhost` | Mantén el bucle local y deja que el proxy del servidor reenvíe, o añade `--allow-remote` tras TLS |
| `a token of at least 16 characters is needed` | Falta `ARMOR_VOICE_TOKEN` o es corto | Defínelo, o usa `--token-file` |
| `ARMOR_VOICE_SILENCE_PIN is not valid` | No son de 4 a 12 dígitos ASCII | Corrige el valor (nunca se imprime) |
| `ARMOR_VOICE_CONFIRM_SECRET is not set` (aviso) | Se usa un secreto aleatorio | Define un secreto de 16+ bytes si las confirmaciones deben sobrevivir a un reinicio |
| 401 `unauthorized` | Falta `X-Armor-Voice-Token` o es incorrecto | Envía el token |
| 501 `stt_unavailable` | `ARMOR_VOICE_STT_COMMAND` no está definido | Configura un programa de voz a texto |
| 501 `server_not_configured` | Falta la dirección o el token del servidor | Define `ARMOR_VOICE_SERVER_URL` y `ARMOR_VOICE_SERVER_TOKEN` |
| 502 `engine_failed` | El motor falló, agotó el tiempo o respondió demasiado (o un WAV de texto a voz que no es mono de 16 bits a 16 kHz) | Ejecútalo a mano con la misma entrada |
| 504 `turn_too_slow` | El motor de voz tardó más de nueve segundos | Usa un modelo más rápido; no se ejecutó nada |
| "Para desarmar hace falta tu PIN" | Desarmar nunca se hace por voz desde el panel | Usa la pantalla |
| Un "sí" hablado no hace nada | No se recordaba la pregunta (tardó más de 12 s en hacerse, pasaron más de 30 s, o contestó otro panel) | Di de nuevo la orden |""",
     "structure": r"""<p align="center">
  <img src="images/repository-structure.svg" alt="Estructura del repositorio ARMOR-VOICE-AI" width="100%">
</p>

<details>
<summary>Versión en texto del árbol</summary>

```text
ARMOR-VOICE-AI/
├── src/armor_voice_ai/        el código (solo biblioteca estándar)
│   ├── phrases.py             las 420 frases de los quince comandos, en ocho idiomas
│   ├── intent.py              normalización y coincidencia exacta: la lista cerrada
│   ├── confirmation.py        tokens de confirmación firmados, de un solo uso y por persona
│   ├── silence_policy.py      off / pin / double_turn, el PIN hablado, el bloqueo
│   ├── session.py             la regla de dos turnos de cada comando
│   ├── gateway.py             líneas JSON por stdin/stdout, la auditoría, las frases que se responden
│   ├── service.py             el servicio HTTP local (/healthz, /v1/command, /v1/turn)
│   └── turn.py                un turno hablado: motores, sí/no, presupuesto de tiempo
├── tests/                     118 pruebas: silencio, bordes, pasarela, turno, idiomas, servicio
├── docs/                      SAFETY.md, SERVICE.md, SILENCE_POLICY.md
├── tools/                     las comprobaciones de CI compartidas y la herramienta de proyecto
├── images/                    banner e icono
├── .github/                   flujo de CI, aviso al panel, plantillas de incidencias y de pull request
├── armor.project.json         manifiesto: versión, función, madurez, orden de compilación
├── pyproject.toml             metadatos del paquete y el comando `armor-voice-gateway`
├── run.sh run.bat             arrancan con el flujo de proyecto compartido
├── build.sh build.bat         compilan y prueban con el flujo de proyecto compartido
├── CHANGELOG.md               qué cambió en cada versión
└── SECURITY.md SUPPORT.md CONTRIBUTING.md CODE_OF_CONDUCT.md LICENSE
```

</details>""",
     "roadmap": r"""**Límites conocidos hoy**

* No incluye ningún motor de voz, y ninguno se ha probado con un micrófono real.
* El panel táctil que debe llevar al asistente no ha funcionado en una placa; no hay palabra de activación, es pulsar para hablar.
* El turno no dice *qué panel ni qué persona* habló: ARMOR-SERVER decide con el token que se le dio. Añadirlos a la petición es un cambio del contrato entre el servidor y el panel.
* No hay revisión de seguridad independiente.

**Lo siguiente**

* Probar un micrófono real y un motor de voz real en el banco de la CM5.
* Ejecutar el flujo de voz con el panel táctil cuando haya funcionado en una placa.
* Confirmación opcional por hablante autenticado o física. Un despliegue posterior puede añadirla, pero la confirmación firmada no se quitará sin una revisión de riesgos documentada.""",
   },
 },
 "fr": {
   "tagline": "Intentions vocales hors ligne en huit langues, avec une confirmation que l'appelant ne peut pas falsifier",
   "honest": "Les règles d'intention, les huit langues, la confirmation signée liée à son locuteur, la politique de mise en silence, le service local, le point d'entrée des tours et l'audit sont réels et testés (118 tests), et le serveur interroge le service sur le banc d'essai CM5. **Aucun moteur de reconnaissance ni de synthèse vocale ne fait partie de ce dépôt** : `/v1/turn` exécute les commandes que vous configurez pour cela, et aucune n'a encore été essayée avec un vrai microphone ; le panneau tactile censé porter l'assistant n'a pas tourné sur une carte.",
   "glance": [
     [
       "Rôle",
       "Passerelle vocale et d'intentions hors ligne (famille : Core Services, parent : ARMOR-SERVER)",
     ],
     [
       "Technologie",
       "Python 3.11+, bibliothèque standard uniquement",
     ],
     [
       "Tests",
       "118 (`python -m unittest discover -s tests`)",
     ],
     [
       "Commandes",
       "15 (10 qui interrogent, 5 qui agissent), 420 phrases, 8 langues",
     ],
     [
       "Écoute sur",
       "`127.0.0.1:18090` (boucle locale uniquement), avec un jeton",
     ],
     [
       "Fonctionne sur",
       "Le banc d'essai CM5 (comme service) ou n'importe quel ordinateur",
     ],
     [
       "Sur matériel réel",
       "Fonctionne comme service sur le banc d'essai CM5, interrogé par le serveur ; aucun microphone ni moteur vocal n'a été essayé",
     ],
     [
       "Licence",
       "GPL-3.0-or-later",
     ],
   ],
   "status": {
     "software": "Les règles d'intention, le service local et le point d'entrée des tours tournent comme service sur le banc d'essai CM5, mais aucun moteur de reconnaissance ni de synthèse vocale ne fait partie du dépôt : il exécute les commandes que vous configurez pour cela.",
     "tests": "118 tests réussissent (`python -m unittest discover -s tests`) : les règles d'intention, les huit langues, la confirmation signée liée à son locuteur, la politique de mise en silence, le service local, le point d'entrée des tours et l'audit.",
     "hardware": "Aucun microphone ni moteur vocal n'a été essayé, et le panneau tactile censé porter l'assistant n'a pas tourné sur une carte.",
     "security": "La confirmation est signée et liée à son locuteur, et l'audit est testé sur la machine hôte ; il n'y a pas eu de revue indépendante.",
     "integration": "Le serveur interroge le service sur le banc d'essai CM5 ; le flux vocal avec le panneau tactile n'a pas tourné.",
     "docs": "Huit langues et le journal des modifications sont à jour.",
   },
   "docs": [
     "[Sécurité vocale](docs/SAFETY.md) : ce qui est compris, la confirmation, le tour du panneau mural, ce qui est enregistré",
     "[Le service](docs/SERVICE.md) : routes, codes d'état et réglages",
     "[Mise en silence par la voix](docs/SILENCE_POLICY.md) : le contrat de la politique et le PIN",
   ],
   "contributing_first": "Avant une pull request, exécutez `python -I tools/armor_ci_validate.py` et les tests : les deux doivent réussir. Voir [CONTRIBUTING.md](CONTRIBUTING.md) et le [code de conduite](CODE_OF_CONDUCT.md).",
   "languages_extra": "Chaque phrase que le service répond, chaque commande vocale, chaque oui et non et chaque mot de chiffre d'un PIN existe dans les huit langues.",
   "body": {
     "overview": r"""ARMOR-VOICE-AI est la partie d'A.R.M.O.R. qui transforme **ce qu'une personne dit en l'une de quinze commandes, ou en rien**. Il ne fait jamais rien par lui-même : il décide, et [ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER) authentifie, autorise et exécute ce qui a été accepté, exactement comme pour un clic dans la console.

Le texte produit par un moteur de reconnaissance vocale est une *entrée non fiable*. Il n'est donc ni interprété, ni fouillé à la recherche de mots-clés, ni transmis comme commande : il est nettoyé (accents, ponctuation, formules de politesse) puis doit correspondre **exactement** à l'une des 420 phrases connues. Tout le reste, tout texte trop long et toute phrase qui pourrait signifier deux commandes *n'est pas compris*.

**Ce qu'il fait**

* Comprend quinze commandes en **huit langues** (anglais, espagnol, allemand, français, italien, japonais, chinois et portugais).
* Exige pour `arm` et `disarm` un **second tour avec un jeton signé par le service**, lié à l'intention et à la personne qui l'a demandée.
* Peut exiger pour `silence` un **code PIN** prononcé ou un second tour de confirmation, quand ARMOR-SERVER le demande.
* Fonctionne comme **service HTTP local** et comme **passerelle en lignes JSON** pour les adaptateurs et les tests.
* Reçoit l'**audio d'un tour** depuis le panneau mural, exécute les moteurs vocaux que vous configurez et répond en texte et, avec un synthétiseur vocal, en audio.
* Enregistre des **décisions, jamais l'audio ni les mots** : un SHA-256 de la transcription.

**Ce qu'il ne fait pas**

* Il ne reconnaît ni ne synthétise la parole : ce sont des programmes que choisit l'installation.
* Il n'arme, ne désarme ni ne met rien en silence : une commande acceptée est une recommandation pour ARMOR-SERVER.
* Il ne désarme jamais depuis le panneau mural : le PIN se saisit sur l'écran, il n'est jamais dit à voix haute.""",
     "role": r"""[ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER) interroge ce service, puis authentifie et autorise la commande comme pour un clic dans [ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO). Il est conçu pour vivre derrière le microphone du panneau mural [ARMOR-NODE-HMI](https://github.com/JuanenRac/ARMOR-NODE-HMI) (appuyer pour parler) et il répond à l'assistant écrit et vocal d'[ARMOR-ANDROID-CONTROL](https://github.com/JuanenRac/ARMOR-ANDROID-CONTROL). Sur le banc d'essai, il est installé par [ARMOR-DEVOPS](https://github.com/JuanenRac/ARMOR-DEVOPS) (`scripts/install_cm5.sh --with-voice`).

| Il parle à | Comment | Pour quoi faire |
|---|---|---|
| ARMOR-SERVER | `POST /v1/command`, `POST /v1/turn` en entrée ; `/api/v1/voice/command` en sortie | Décider d'une phrase ; transmettre les mots d'un tour vocal à la route vocale du serveur |
| ARMOR-NODE-HMI | audio d'un tour (PCM mono 16 kHz) | Le microphone et le haut-parleur du panneau mural |
| ARMOR-ANDROID-CONTROL | via le serveur | L'assistant écrit et vocal |
| Moteurs vocaux | entrée et sortie standard | Écouter (p. ex. whisper.cpp, Vosk) et parler (p. ex. Piper) ; choisis par l'installation |""",
     "architecture": r"""<p align="center">
  <img src="images/architecture.svg" alt="Architecture d'ARMOR-VOICE-AI : les appelants, ARMOR-SERVER, le service vocal avec ses modules et les moteurs vocaux choisis par l'installation" width="100%">
</p>

**Un tour vocal qui arme le système** (le panneau est interrogé deux fois, et le désarmement est refusé) :

<p align="center">
  <img src="images/turn-sequence.svg" alt="A spoken turn that arms the system: the wall panel, ARMOR-VOICE-AI, ARMOR-SERVER and the speech engines, in eleven numbered messages over two turns" width="100%">
</p>

<details>
<summary>Version texte du diagramme (Mermaid)</summary>

```mermaid
sequenceDiagram
    autonumber
    participant P as Wall panel
    participant V as ARMOR-VOICE-AI
    participant E as Speech engines
    participant S as ARMOR-SERVER
    P->>V: POST /v1/turn (audio, language)
    V->>E: STT: WAV on stdin
    E-->>V: "arm the system"
    V->>S: /api/v1/voice/command {text, language}
    S-->>V: confirmation-needed + token
    V->>E: TTS: "Please confirm"
    V-->>P: heard, reply, audio
    P->>V: POST /v1/turn ("yes")
    V->>S: /api/v1/voice/command {text, confirmation}
    S-->>V: accepted
    V-->>P: "Command accepted"
    Note over V,S: "disarm" is refused here: it needs a PIN, typed on the screen
```

</details>

**Pourquoi il est construit ainsi**

* **Pourquoi une liste fermée et non une classification d'intentions.** Un moteur de reconnaissance se trompe et n'importe qui peut parler près d'un microphone. Avec 420 phrases exactes, le pire qu'une mauvaise transcription puisse provoquer est d'être ignorée, et un test vérifie qu'aucune phrase n'appartient à deux commandes.
* **Pourquoi le service ne fait que décider.** L'authentification, l'autorisation, la piste d'audit et l'action restent en un seul endroit, ARMOR-SERVER ; un bogue ici peut accepter une phrase à tort, mais ne peut pas toucher à une alarme.
* **Pourquoi la confirmation est un jeton signé émis par le service.** Un indicateur fixé par l'appelant (`confirmed: true`) ne prouve rien, il est donc refusé. Le jeton est signé en HMAC-SHA-256, lié à la commande et à la personne, valable 30 secondes et utilisable une seule fois.
* **Pourquoi les moteurs vocaux sont des programmes séparés.** Les modèles évoluent plus vite qu'une passerelle de sécurité ne devrait le faire. Ils sont exécutés sans shell, avec un environnement réduit et une limite de temps, et les secrets propres au service ne leur parviennent jamais.
* **Pourquoi rien n'est conservé.** Le journal montre ce qui a été décidé sans conserver ce qui a été dit.""",
     "features": r"""### Les quinze commandes

| Commande | Type | Signification | Confirmation |
|---|---|---|---|
| `status` | interroge | L'état du système | non |
| `alarms` | interroge | Les alarmes actives | non |
| `nodes` | interroge | L'état des nœuds | non |
| `cameras` | interroge | L'état des caméras | non |
| `radar` | interroge | L'état des radars | non |
| `solar` | interroge | L'état du système solaire | non |
| `electrical` | interroge | La consommation électrique | non |
| `network` | interroge | L'état du réseau | non |
| `time` | interroge | L'heure | non |
| `help` | interroge | Ce qui peut être dit | non |
| `silence` | agit | Mettre en silence (acquitter) les alarmes | seulement si la politique du serveur le demande (voir ci-dessous) |
| `lights_on` | agit | Allumer les lumières | non |
| `lights_off` | agit | Éteindre les lumières | non |
| `arm` | agit | Armer le périmètre | **oui** |
| `disarm` | agit | Désarmer le périmètre | **oui** |

Les dix qui *interrogent* ne changent rien. Les cinq qui *agissent* sont exécutées par ARMOR-SERVER avec la session de la personne qui a parlé, jamais par ce service.

### Huit langues

Anglais, espagnol, allemand, français, italien, japonais, chinois et portugais européen : les phrases (420 au total), le oui et le non d'une confirmation, les mots des chiffres d'un PIN prononcé et chaque phrase que le service répond. Les phrases sont écrites comme une personne les dit et normalisées au chargement du module avec la même fonction que celle qui normalise ce qui est entendu, de sorte que les deux ne peuvent pas diverger. Les formules de politesse (`please`, `por favor`, `bitte`, `s'il vous plaît`, `per favore`...) sont écartées avant la comparaison ; le japonais et le chinois, écrits sans espaces, listent leurs phrases avec et sans la terminaison polie.

### La confirmation en deux tours

1. Le premier tour pour `arm` ou `disarm` renvoie **aucune acceptation** et un `confirmation_token`.
2. Le second tour répète ce jeton pour la même intention, **pour la même personne**, dans les 30 secondes.
3. Le jeton est signé avec un secret que l'appelant ne possède pas, de sorte qu'il ne peut être ni falsifié, ni modifié, ni transféré à une autre intention ou à une autre personne ; il ne fonctionne qu'une fois et les nonces de ceux qui n'ont pas expiré ne sont jamais oubliés pour faire de la place aux nouveaux (quand il y en a trop à la fois, le nouveau jeton est refusé).

### Mise en silence par la voix, avec un PIN facultatif

« Silence » est accepté immédiatement, sauf si l'installation exige davantage. ARMOR-SERVER détient le réglage `voice.silence_confirmation` et l'envoie sous forme de politique :

| Mode | Ce qui se passe pour « silence » |
|---|---|
| `off` (par défaut, et quand aucune politique n'arrive) | Transmis immédiatement |
| `double_turn` | Non exécuté ; le service demande de dire oui, et un oui dans les 15 s depuis le même panneau transmet la commande d'origine |
| `pin` | Non exécuté ; le service demande le PIN, dit en chiffres ou en mots dans les huit langues ; le bon PIN dans les 20 s transmet la commande |
| politique illisible ou inconnue | `double_turn` : un réglage cassé ne désactive jamais une protection |

Le PIN (de 4 à 12 chiffres, `ARMOR_VOICE_SILENCE_PIN`) est comparé en temps constant et n'est jamais journalisé, conservé ni répété. Trois mauvais PIN bloquent la mise en silence par la voix pour **tous** les panneaux pendant cinq minutes ; si le mode `pin` est demandé et qu'aucun PIN n'est configuré, rien n'est mis en silence par la voix. Le contrat complet se trouve dans [docs/SILENCE_POLICY.md](docs/SILENCE_POLICY.md).

### Le tour du panneau mural

`POST /v1/turn` reçoit l'audio d'un tour, exécute la commande de reconnaissance vocale, donne les mots à la route vocale d'ARMOR-SERVER et répond avec ce qui a été entendu, ce qu'il faut dire et, quand une commande de synthèse vocale est configurée, un enregistrement de la réponse. Le panneau n'a pas de clavier : la question d'`arm` est donc mémorisée par panneau pendant 30 secondes, et le tour suivant qui dit *oui* (dans la langue du panneau) la confirme, tandis que celui qui dit *non* l'annule. Si le serveur répond `disarm`, le tour répond que le désarmement exige le PIN sur l'écran. Au-delà de neuf secondes d'écoute, rien n'est demandé au serveur (le panneau abandonne à douze), de sorte que ce qui a été dit à la personne et ce que la maison a fait ne peuvent pas se contredire.

### Décisions consignées

Avec `--audit-file`, une ligne JSON par décision : heure, intention, résultat et SHA-256 de la transcription. Jamais l'audio et jamais les mots.""",
     "security": r"""| Menace | Défense |
|---|---|
| Une transcription erronée ou hostile | Entrée non fiable : normalisée, correspondance exacte avec une liste fermée, 200 caractères au maximum, l'ambigu *n'est pas compris* ; jamais transmise comme commande shell ou d'appareil |
| Un appelant revendique une confirmation | `confirmed` est refusé ; seul compte un jeton signé par le service |
| Un jeton est volé, rejoué ou réutilisé | Signé en HMAC-SHA-256, lié à l'intention et à la personne, 30 s, usage unique ; un jeton ne peut pas survivre à son heure d'émission même si l'horloge recule |
| Une autre personne utilise le jeton de quelqu'un | `wrong-subject` |
| Deviner le PIN de mise en silence | Comparaison en temps constant, 3 essais puis 5 minutes de blocage pour tous les panneaux, échec fermé sans PIN |
| Quelqu'un sur le réseau atteint le service | Boucle locale uniquement (refuse une autre adresse sans `--allow-remote`) ; jeton d'au moins 16 caractères comparé en temps constant ; 2 Ko par requête ; une connexion qui reste bloquée est fermée au bout de 15 s |
| Un moteur vocal divulgue ou abuse de secrets | Exécuté sans shell, avec un environnement réduit (`PATH`, `HOME`, `LANG`, `TMPDIR`, `ARMOR_VOICE_ENGINE_*`), une limite de temps et une limite de taille ; les jetons du service et du serveur ne lui parviennent jamais |
| Épuiser la machine | Deux tours à la fois au plus (un troisième reçoit 503) ; audio plafonné à 480 000 octets |
| Les journaux révèlent ce qui a été dit | Jamais journalisé ; l'audit ne contient qu'un hachage |
| Un tour périmé agit trop tard | Au-delà de neuf secondes, rien n'est exécuté (504) |

Le désarmement par la voix n'est **jamais** effectué depuis le panneau mural. Depuis l'application, il suit le `ARMOR_DISARM_PIN` du serveur (réglez-le sur `required`). Rien ici n'est une fonction de sécurité certifiée : une commande acceptée est une recommandation qu'ARMOR-SERVER authentifie et autorise encore. Lisez [docs/SAFETY.md](docs/SAFETY.md) pour les règles complètes et [SECURITY.md](SECURITY.md) pour signaler une vulnérabilité.""",
     "interfaces": r"""### Service HTTP

| Route | Authentification | Ce qu'elle fait |
|---|---|---|
| `GET /healthz` | aucune | `{"ok": true, "service": "armor-voice"}` |
| `POST /v1/command` | en-tête `X-Armor-Voice-Token` | Corps `{text, language?, confirmation?, subject?, policy?, pin?}` (2 Ko au plus). Répond ce qui a été compris, un `confirmation_token` quand un second tour est nécessaire et `speech` dans la langue demandée |
| `POST /v1/turn` | le même en-tête | Corps : PCM brut mono 16 bits à 16 kHz, `Content-Type: audio/L16;rate=16000`, jusqu'à 480 000 octets ; en-têtes `X-Armor-Language`, `X-Armor-Client`, `X-Armor-Policy`. Répond `{heard, reply, audio?}` |
| `POST /v1/speak` | le même en-tête | Corps `{text, language}` (300 caractères au plus). Répond `{audio}`, la phrase dite par le programme de synthèse vocale en base64 de PCM mono 16 bits à 16 kHz (elle ne déclenche rien et ne garde rien) ; 501 sans ce programme |

Un échange réel (le jeton est abrégé) :

```json
{"text": "arm the system", "subject": "u-1"}
{"accepted": false, "requires_confirmation": true, "intent": "arm", "outcome": "confirmation-needed", "confirmation_token": "eyJpIjoiYXJt...", "reason": "say it again with the confirmation within 30 s", "speech": "Please confirm"}

{"text": "arm the system", "subject": "u-1", "confirmation": "eyJpIjoiYXJt..."}
{"accepted": true, "requires_confirmation": false, "intent": "arm", "outcome": "accepted", "speech": "Command accepted"}

{"text": "open the garage"}
{"accepted": false, "requires_confirmation": false, "intent": null, "outcome": "not-understood", "reason": "the phrase is not one of the known commands", "speech": "Command not recognised"}
```

Résultats : `accepted`, `confirmation-needed`, `confirmation-refused`, `pin-needed`, `pin-refused`, `not-understood`. Une confirmation est refusée comme `invalid`, `expired`, `wrong-intent`, `wrong-subject` ou `replayed`.

### Codes d'état de `/v1/turn`

| Code | Erreur | Signification |
|---|---|---|
| 200 | | `{heard, reply, audio?}` |
| 401 | `unauthorized` | Jeton absent ou incorrect |
| 411 / 413 | `bad audio length` | Pas de longueur, ou plus de 480 000 octets |
| 415 | | Ce n'est pas `audio/L16;rate=16000` |
| 422 | `invalid language` | Ce n'est pas l'une de `en es de fr it ja zh pt` |
| 501 | `stt_unavailable` / `server_not_configured` | Aucune commande de reconnaissance vocale, ou aucune adresse de serveur |
| 502 | `engine_failed` / `server_<code>` / `server_not_answering` | Un moteur vocal ou le serveur a échoué |
| 503 | `busy` | Deux tours sont déjà en cours |
| 504 | `turn_too_slow` | Le moteur vocal a été si lent que le serveur n'a pas été interrogé ; rien n'a été exécuté |

### Passerelle en lignes JSON

`python -m armor_voice_ai.gateway` lit un objet JSON par ligne sur l'entrée standard et écrit la réponse sur la sortie standard (2 Ko par ligne ; une ligne contenant des octets qui ne sont pas de l'UTF-8 est une ligne comme les autres). C'est la même passerelle fermée, pour les adaptateurs vocaux et les tests.

### Contrat avec ARMOR-SERVER

* Le serveur envoie la politique de mise en silence à chaque requête : `policy` dans le corps de `/v1/command` (et `pin` pour le mode `pin`), l'en-tête `X-Armor-Policy` (un objet JSON de 256 octets au plus) sur `/v1/turn`.
* La route vocale du serveur reçoit les mots d'un tour vocal sur `/api/v1/voice/command` avec le jeton d'opérateur de l'installation, sous le nom de chaque panneau (`X-Armor-Client`).
* Détails : [docs/SERVICE.md](docs/SERVICE.md), [docs/SILENCE_POLICY.md](docs/SILENCE_POLICY.md).""",
     "configuration": r"""### Environnement

| Variable | Requise | Ce qu'elle définit |
|---|---|---|
| `ARMOR_VOICE_TOKEN` | oui (16+ caractères) | Le jeton que les appelants envoient dans `X-Armor-Voice-Token` (ou une ligne `ARMOR_VOICE_TOKEN=...` dans le fichier de `--token-file`) |
| `ARMOR_VOICE_CONFIRM_SECRET` | recommandée (16+ octets) | Signe les confirmations. Sans elle, un secret aléatoire est utilisé et les confirmations en attente sont perdues à l'arrêt du processus |
| `ARMOR_VOICE_STT_COMMAND` | pour `/v1/turn` | Le programme de reconnaissance vocale : audio (WAV) sur l'entrée standard, les mots sur la sortie standard |
| `ARMOR_VOICE_TTS_COMMAND` | facultative | Le programme de synthèse vocale : texte sur l'entrée standard, un WAV mono 16 bits à 16 kHz sur la sortie standard |
| `ARMOR_VOICE_SERVER_URL`, `ARMOR_VOICE_SERVER_TOKEN` | pour `/v1/turn` | ARMOR-SERVER et le jeton d'opérateur de sa route vocale |
| `ARMOR_VOICE_SILENCE_PIN` | pour le mode `pin` | De 4 à 12 chiffres. Une valeur non valide arrête le service au démarrage sans l'afficher |
| `ARMOR_VOICE_ENGINE_*` | facultative | Transmises aux moteurs vocaux (avec `ARMOR_VOICE_LANGUAGE`, fixée à chaque tour) |

### Ligne de commande

| Option | Par défaut | |
|---|---|---|
| `--host` | `127.0.0.1` | Adresse d'écoute ; toute autre que la boucle locale est refusée sans `--allow-remote` |
| `--port` | `18090` | |
| `--token-file` | | Fichier avec une ligne `ARMOR_VOICE_TOKEN=...` |
| `--audit-file` | | Ajoute une ligne par décision |
| `--allow-remote` | désactivé | Écoute sur une adresse hors boucle locale (déconseillé ; seulement derrière TLS) |

### Limites présentes dans le code

| Limite | Valeur |
|---|---|
| Validité de la confirmation | 30 s |
| Question vocale mémorisée par panneau | 30 s |
| « Oui » après une question de mise en silence / PIN après sa demande | 15 s / 20 s |
| Essais de PIN avant le blocage / durée du blocage | 3 / 5 min |
| Budget du tour / le panneau abandonne | 9 s / 12 s |
| Limite de temps d'un moteur vocal | 25 s |
| Audio maximal / audio de réponse maximal | 480 000 octets / 190 000 octets |
| Corps de la requête (`/v1/command`) | 2 Ko |
| Longueur de la transcription | 200 caractères |
| Tours simultanés | 2 |

Le service n'écrit jamais ce qui a été dit dans un journal, quels que soient les réglages.""",
     "quickstart": "**Prérequis :** Python 3.11+ (bibliothèque standard uniquement). Facultatif : un programme de reconnaissance vocale et un de synthèse vocale pour `/v1/turn`.\n\n```powershell\n$env:PYTHONPATH = \"src\"\n\n# 1. les tests\npython -m unittest discover -s tests                      # 118 tests\n\n# 2. la passerelle, un objet JSON par ligne\necho '{\"text\":\"arm the system\"}' | python -m armor_voice_ai.gateway\n\n# 3. le service HTTP local (boucle locale uniquement)\n$env:ARMOR_VOICE_TOKEN = \"a-token-of-at-least-16-characters\"\npython -m armor_voice_ai.service --port 18090\n```\n\n```sh\ncurl -s http://127.0.0.1:18090/v1/command \\\n  -H \"X-Armor-Voice-Token: $ARMOR_VOICE_TOKEN\" \\\n  -d '{\"text\":\"status\",\"language\":\"de\"}'\n# {\"accepted\":true,\"requires_confirmation\":false,\"intent\":\"status\",\"outcome\":\"accepted\",\"speech\":\"Befehl akzeptiert\"}\n```\n\nPour écouter et parler (`/v1/turn`), pointez le service vers vos moteurs et vers le serveur :\n\n```sh\nexport ARMOR_VOICE_STT_COMMAND=\"/opt/armor/bin/hear\"        # WAV sur l'entrée, mots sur la sortie\nexport ARMOR_VOICE_TTS_COMMAND=\"/opt/armor/bin/speak\"       # texte sur l'entrée, WAV sur la sortie\nexport ARMOR_VOICE_SERVER_URL=\"https://armor-server.local\"\nexport ARMOR_VOICE_SERVER_TOKEN=\"...\"\npython -m armor_voice_ai.service --token-file /opt/armor/etc/armor.voice.env\n```\n\nLe panneau mural est un appareil du réseau et le service n'écoute que sur la boucle locale : soit un proxy du serveur transmet le tour, soit `--allow-remote` est utilisé derrière TLS. Le jeton et l'audio ne doivent pas traverser le réseau en clair.\n\n`run.bat` / `run.sh` et `build.bat` / `build.sh` lancent le flux de projet partagé d'[ARMOR-COMMON](https://github.com/JuanenRac/ARMOR-COMMON) (les dépôts sont côte à côte). Avec pip, la commande `armor-voice-gateway` est disponible.",
     "testing": r"""```powershell
$env:PYTHONPATH = "src"
python -m unittest discover -s tests
python -I tools/armor_ci_validate.py        # manifeste, version, journal des modifications et parité des README
```

| Fichier de tests | Tests | Ce qu'il couvre |
|---|---|---|
| `test_silence.py` | 31 | La politique de mise en silence, le PIN prononcé en huit langues, le blocage |
| `test_edges.py` | 29 | Le protocole en lignes, les réglages du service, la liaison avec le serveur (un substitut sur la boucle locale), les limites des moteurs |
| `test_gateway.py` | 23 | La passerelle, la confirmation, les rejeux et les falsifications |
| `test_turn.py` | 15 | Le tour, les moteurs, le oui et le non prononcés, le budget de temps |
| `test_languages.py` | 11 | Phrases sous forme normale, aucune phrase pour deux commandes, chaque langue arme, désarme, interroge et met en silence |
| `test_service.py` | 5 | Les routes HTTP |

GitHub Actions exécute la base A.R.M.O.R. à chaque push et pull request : la validation du manifeste, de la version, du journal des modifications et de la parité des README, puis la compilation et les tests propres au projet.""",
     "build": "C'est du Python pur : rien à compiler. La version se trouve dans `pyproject.toml`, dans `armor.project.json` et dans le badge du README (lu depuis le manifeste) ; chaque version a son entrée dans [CHANGELOG.md](CHANGELOG.md). Les versions sont publiées sur GitHub.",
     "troubleshooting": r"""| Vous voyez | Parce que | Faites |
|---|---|---|
| `refusing to listen on a non-loopback address without --allow-remote` | `--host` n'est ni `127.0.0.1`, ni `::1`, ni `localhost` | Gardez la boucle locale et laissez le proxy du serveur transmettre, ou ajoutez `--allow-remote` derrière TLS |
| `a token of at least 16 characters is needed` | `ARMOR_VOICE_TOKEN` est absent ou trop court | Définissez-le, ou utilisez `--token-file` |
| `ARMOR_VOICE_SILENCE_PIN is not valid` | Ce ne sont pas 4 à 12 chiffres ASCII | Corrigez la valeur (elle n'est jamais affichée) |
| `ARMOR_VOICE_CONFIRM_SECRET is not set` (avertissement) | Un secret aléatoire est utilisé | Définissez un secret de 16+ octets si les confirmations doivent survivre à un redémarrage |
| 401 `unauthorized` | `X-Armor-Voice-Token` absent ou incorrect | Envoyez le jeton |
| 501 `stt_unavailable` | `ARMOR_VOICE_STT_COMMAND` n'est pas défini | Configurez un programme de reconnaissance vocale |
| 501 `server_not_configured` | Aucune adresse ni aucun jeton de serveur | Définissez `ARMOR_VOICE_SERVER_URL` et `ARMOR_VOICE_SERVER_TOKEN` |
| 502 `engine_failed` | Le moteur a échoué, dépassé le délai ou répondu trop (ou un WAV de synthèse vocale qui n'est pas mono 16 bits à 16 kHz) | Exécutez-le à la main avec la même entrée |
| 504 `turn_too_slow` | Le moteur vocal a mis plus de neuf secondes | Utilisez un modèle plus rapide ; rien n'a été exécuté |
| « Le désarmement exige votre PIN » | Le désarmement n'est jamais fait par la voix depuis le panneau | Utilisez l'écran |
| Un « oui » prononcé ne fait rien | La question n'a pas été mémorisée (elle a mis plus de 12 s à être posée, plus de 30 s se sont écoulées, ou un autre panneau a répondu) | Redites la commande |""",
     "structure": r"""<p align="center">
  <img src="images/repository-structure.svg" alt="Structure du dépôt ARMOR-VOICE-AI" width="100%">
</p>

<details>
<summary>Version texte de l'arborescence</summary>

```text
ARMOR-VOICE-AI/
├── src/armor_voice_ai/        le code (bibliothèque standard uniquement)
│   ├── phrases.py             les 420 phrases des quinze commandes, en huit langues
│   ├── intent.py              normalisation et correspondance exacte : la liste d'autorisation fermée
│   ├── confirmation.py        jetons de confirmation signés, à usage unique, par personne
│   ├── silence_policy.py      off / pin / double_turn, le PIN prononcé, le blocage
│   ├── session.py             la règle des deux tours pour chaque commande
│   ├── gateway.py             lignes JSON sur stdin/stdout, l'audit, les phrases répondues
│   ├── service.py             le service HTTP local (/healthz, /v1/command, /v1/turn)
│   └── turn.py                un tour vocal : moteurs, oui/non, budget de temps
├── tests/                     118 tests : silence, limites, passerelle, tour, langues, service
├── docs/                      SAFETY.md, SERVICE.md, SILENCE_POLICY.md
├── tools/                     les contrôles CI partagés et l'outillage du projet
├── images/                    bannière et icône
├── .github/                   workflow CI, avis du tableau de bord, modèles de tickets et de pull requests
├── armor.project.json         manifeste : version, rôle, maturité, commande de compilation
├── pyproject.toml             métadonnées du paquet et la commande `armor-voice-gateway`
├── run.sh run.bat             démarrent via le flux de projet partagé
├── build.sh build.bat         compilent et testent via le flux de projet partagé
├── CHANGELOG.md               ce qui a changé dans chaque version
└── SECURITY.md SUPPORT.md CONTRIBUTING.md CODE_OF_CONDUCT.md LICENSE
```

</details>""",
     "roadmap": r"""**Limites connues aujourd'hui**

* Aucun moteur vocal n'est fourni, et aucun n'a été essayé avec un vrai microphone.
* Le panneau tactile censé porter l'assistant n'a pas tourné sur une carte ; il n'y a pas de mot d'éveil, c'est appuyer pour parler.
* Le tour ne dit pas *quel panneau ni quelle personne* a parlé : ARMOR-SERVER décide avec le jeton qu'il a reçu. Les ajouter à la requête est un changement du contrat entre le serveur et le panneau.
* Pas de revue de sécurité indépendante.

**Prochainement**

* Essayer un vrai microphone et un vrai moteur vocal sur le banc d'essai CM5.
* Exécuter le flux vocal avec le panneau tactile une fois qu'il aura tourné sur une carte.
* Confirmation facultative par locuteur authentifié ou physique. Un déploiement ultérieur pourra l'ajouter, mais la confirmation signée ne sera pas supprimée sans une revue de risques documentée.""",
   },
 },
 "it": {
   "tagline": "Intenti vocali offline in otto lingue, con una conferma che chi chiama non può falsificare",
   "honest": "Le regole degli intenti, le otto lingue, la conferma firmata legata a chi parla, la politica di silenziamento, il servizio locale, l'endpoint dei turni e l'audit sono reali e testati (118 test), e il server interroga il servizio sul banco di prova CM5. **Nessun motore di riconoscimento o di sintesi vocale fa parte di questo repository**: `/v1/turn` esegue i comandi che configuri per questo, e nessuno è stato ancora provato con un vero microfono; il pannello touch che dovrebbe ospitare l'assistente non ha ancora girato su una scheda.",
   "glance": [
     [
       "Ruolo",
       "Gateway vocale e di intenti offline (famiglia: Core Services, genitore: ARMOR-SERVER)",
     ],
     [
       "Tecnologia",
       "Python 3.11+, solo libreria standard",
     ],
     [
       "Test",
       "118 (`python -m unittest discover -s tests`)",
     ],
     [
       "Comandi",
       "15 (10 che interrogano, 5 che agiscono), 420 frasi, 8 lingue",
     ],
     [
       "In ascolto su",
       "`127.0.0.1:18090` (solo loopback), con un token",
     ],
     [
       "Gira su",
       "Il banco di prova CM5 (come servizio) o qualsiasi computer",
     ],
     [
       "Su hardware reale",
       "Gira come servizio sul banco di prova CM5, interrogato dal server; nessun microfono né motore vocale è stato provato",
     ],
     [
       "Licenza",
       "GPL-3.0-or-later",
     ],
   ],
   "status": {
     "software": "Le regole degli intenti, il servizio locale e l'endpoint dei turni girano come servizio sul banco di prova CM5, ma nessun motore di riconoscimento o di sintesi vocale fa parte del repository: esegue i comandi che configuri per questo.",
     "tests": "Superano 118 test (`python -m unittest discover -s tests`): le regole degli intenti, le otto lingue, la conferma firmata legata a chi parla, la politica di silenziamento, il servizio locale, l'endpoint dei turni e l'audit.",
     "hardware": "Nessun microfono né motore vocale è stato provato, e il pannello touch che dovrebbe ospitare l'assistente non ha girato su una scheda.",
     "security": "La conferma è firmata e legata a chi parla, e l'audit è provato sull'host; non c'è stata una revisione indipendente.",
     "integration": "Il server interroga il servizio sul banco di prova CM5; il flusso vocale con il pannello touch non ha girato.",
     "docs": "Otto lingue e il registro delle modifiche sono aggiornati.",
   },
   "docs": [
     "[Sicurezza della voce](docs/SAFETY.md): cosa viene capito, la conferma, il turno del pannello a parete, cosa viene registrato",
     "[Il servizio](docs/SERVICE.md): rotte, codici di stato e impostazioni",
     "[Silenziare con la voce](docs/SILENCE_POLICY.md): il contratto della politica e il PIN",
   ],
   "contributing_first": "Prima di una pull request esegui `python -I tools/armor_ci_validate.py` e i test: devono passare entrambi. Vedi [CONTRIBUTING.md](CONTRIBUTING.md) e il [codice di condotta](CODE_OF_CONDUCT.md).",
   "languages_extra": "Ogni frase che il servizio dice in risposta, ogni comando vocale, ogni sì e no e ogni parola di cifra di un PIN esiste in tutte e otto le lingue.",
   "body": {
     "overview": r"""ARMOR-VOICE-AI è la parte di A.R.M.O.R. che trasforma **ciò che dice una persona in uno di quindici comandi, oppure in niente**. Non fa mai nulla da sé: decide, e [ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER) autentica, autorizza ed esegue ciò che è stato accettato, esattamente come farebbe con un clic nella console.

Il testo che esce da un riconoscitore vocale è un *input non attendibile*. Perciò non viene interpretato, né cercato per parole chiave, né inoltrato come comando: viene ripulito (accenti, punteggiatura, formule di cortesia) e deve poi corrispondere **esattamente** a una delle 420 frasi note. Tutto il resto, ogni testo troppo lungo e ogni frase che potrebbe significare due comandi *non viene capito*.

**Cosa fa**

* Capisce quindici comandi in **otto lingue** (inglese, spagnolo, tedesco, francese, italiano, giapponese, cinese e portoghese).
* Fa sì che `arm` e `disarm` richiedano un **secondo turno con un token firmato dal servizio**, legato all'intento e a chi l'ha richiesto.
* Può far sì che `silence` richieda un **PIN** pronunciato o un secondo turno di conferma, quando ARMOR-SERVER lo chiede.
* Gira come **servizio HTTP locale** e come **gateway a righe JSON** per adattatori e test.
* Riceve l'**audio di un turno** dal pannello a parete, esegue i motori vocali che configuri e risponde in testo e, con un sintetizzatore vocale, in audio.
* Registra **decisioni, mai audio né parole**: un SHA-256 della trascrizione.

**Cosa non fa**

* Non riconosce né sintetizza la voce: sono programmi scelti dall'installazione.
* Non inserisce, non disinserisce e non silenzia nulla: un comando accettato è una raccomandazione per ARMOR-SERVER.
* Non disinserisce mai dal pannello a parete: il PIN si digita sullo schermo, non si dice mai ad alta voce.""",
     "role": r"""[ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER) interroga questo servizio, poi autentica e autorizza il comando come farebbe con un clic in [ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO). È pensato per vivere dietro il microfono del pannello a parete [ARMOR-NODE-HMI](https://github.com/JuanenRac/ARMOR-NODE-HMI) (premi per parlare) e risponde all'assistente scritto e vocale di [ARMOR-ANDROID-CONTROL](https://github.com/JuanenRac/ARMOR-ANDROID-CONTROL). Sul banco di prova è installato da [ARMOR-DEVOPS](https://github.com/JuanenRac/ARMOR-DEVOPS) (`scripts/install_cm5.sh --with-voice`).

| Parla con | Come | A che scopo |
|---|---|---|
| ARMOR-SERVER | `POST /v1/command`, `POST /v1/turn` in ingresso; `/api/v1/voice/command` in uscita | Decidere una frase; passare le parole di un turno vocale alla rotta vocale del server |
| ARMOR-NODE-HMI | audio di un turno (PCM mono 16 kHz) | Il microfono e l'altoparlante del pannello a parete |
| ARMOR-ANDROID-CONTROL | tramite il server | L'assistente scritto e vocale |
| Motori vocali | input e output standard | Ascoltare (p. es. whisper.cpp, Vosk) e parlare (p. es. Piper); scelti dall'installazione |""",
     "architecture": r"""<p align="center">
  <img src="images/architecture.svg" alt="Architettura di ARMOR-VOICE-AI: i chiamanti, ARMOR-SERVER, il servizio vocale con i suoi moduli e i motori vocali scelti dall'installazione" width="100%">
</p>

**Un turno vocale che inserisce il sistema** (al pannello si chiede due volte, e il disinserimento viene rifiutato):

<p align="center">
  <img src="images/turn-sequence.svg" alt="A spoken turn that arms the system: the wall panel, ARMOR-VOICE-AI, ARMOR-SERVER and the speech engines, in eleven numbered messages over two turns" width="100%">
</p>

<details>
<summary>Versione testuale del diagramma (Mermaid)</summary>

```mermaid
sequenceDiagram
    autonumber
    participant P as Wall panel
    participant V as ARMOR-VOICE-AI
    participant E as Speech engines
    participant S as ARMOR-SERVER
    P->>V: POST /v1/turn (audio, language)
    V->>E: STT: WAV on stdin
    E-->>V: "arm the system"
    V->>S: /api/v1/voice/command {text, language}
    S-->>V: confirmation-needed + token
    V->>E: TTS: "Please confirm"
    V-->>P: heard, reply, audio
    P->>V: POST /v1/turn ("yes")
    V->>S: /api/v1/voice/command {text, confirmation}
    S-->>V: accepted
    V-->>P: "Command accepted"
    Note over V,S: "disarm" is refused here: it needs a PIN, typed on the screen
```

</details>

**Perché è costruito così**

* **Perché una lista chiusa e non una classificazione degli intenti.** Un riconoscitore sbaglia e chiunque può parlare vicino a un microfono. Con 420 frasi esatte il peggio che una trascrizione errata possa fare è essere ignorata, e un test verifica che nessuna frase appartenga a due comandi.
* **Perché il servizio si limita a decidere.** Autenticazione, autorizzazione, traccia di audit e azione restano in un solo posto, ARMOR-SERVER; un bug qui può accettare per errore una frase, ma non può toccare un allarme.
* **Perché la conferma è un token firmato emesso dal servizio.** Un flag impostato da chi chiama (`confirmed: true`) non prova nulla, quindi viene rifiutato. Il token è firmato con HMAC-SHA-256, legato al comando e alla persona, valido 30 secondi e utilizzabile una sola volta.
* **Perché i motori vocali sono programmi separati.** I modelli cambiano più in fretta di quanto dovrebbe fare un gateway di sicurezza. Vengono eseguiti senza shell, con un ambiente ridotto e un limite di tempo, e i segreti del servizio non li raggiungono mai.
* **Perché non si conserva nulla.** Il registro mostra cosa è stato deciso senza conservare cosa è stato detto.""",
     "features": r"""### I quindici comandi

| Comando | Tipo | Significato | Conferma |
|---|---|---|---|
| `status` | interroga | Lo stato del sistema | no |
| `alarms` | interroga | Gli allarmi attivi | no |
| `nodes` | interroga | Lo stato dei nodi | no |
| `cameras` | interroga | Lo stato delle telecamere | no |
| `radar` | interroga | Lo stato dei radar | no |
| `solar` | interroga | Lo stato dell'impianto solare | no |
| `electrical` | interroga | Il consumo elettrico | no |
| `network` | interroga | Lo stato della rete | no |
| `time` | interroga | L'ora | no |
| `help` | interroga | Cosa si può dire | no |
| `silence` | agisce | Silenziare (riconoscere) gli allarmi | solo se la politica del server lo richiede (vedi sotto) |
| `lights_on` | agisce | Accendere le luci | no |
| `lights_off` | agisce | Spegnere le luci | no |
| `arm` | agisce | Inserire il perimetro | **sì** |
| `disarm` | agisce | Disinserire il perimetro | **sì** |

I dieci che *interrogano* non cambiano nulla. I cinque che *agiscono* sono eseguiti da ARMOR-SERVER con la sessione di chi ha parlato, mai da questo servizio.

### Otto lingue

Inglese, spagnolo, tedesco, francese, italiano, giapponese, cinese e portoghese europeo: le frasi (420 in tutto), il sì e il no di una conferma, le parole delle cifre di un PIN pronunciato e ogni frase che il servizio dice in risposta. Le frasi sono scritte come le dice una persona e normalizzate al caricamento del modulo con la stessa funzione che normalizza ciò che si sente, così le due non possono divergere. Le formule di cortesia (`please`, `por favor`, `bitte`, `s'il vous plaît`, `per favore`...) vengono scartate prima del confronto; il giapponese e il cinese, scritti senza spazi, elencano le loro frasi con e senza la terminazione cortese.

### La conferma in due turni

1. Il primo turno per `arm` o `disarm` restituisce **nessuna accettazione** e un `confirmation_token`.
2. Il secondo turno ripete quel token per lo stesso intento, **per la stessa persona**, entro 30 secondi.
3. Il token è firmato con un segreto che chi chiama non possiede, così non può essere falsificato, alterato né spostato su un altro intento o un'altra persona; funziona una sola volta e i nonce di quelli non ancora scaduti non vengono mai dimenticati per far posto ai nuovi (quando ce ne sono troppi insieme, il nuovo token viene rifiutato).

### Silenziare con la voce, con PIN facoltativo

«Silence» viene accettato subito, a meno che l'installazione non chieda di più. ARMOR-SERVER conserva l'impostazione `voice.silence_confirmation` e la invia come politica:

| Modalità | Cosa succede con «silence» |
|---|---|
| `off` (predefinita, e quando non arriva alcuna politica) | Inoltrato subito |
| `double_turn` | Non eseguito; il servizio chiede di dire sì, e un sì entro 15 s dallo stesso pannello inoltra il comando originale |
| `pin` | Non eseguito; il servizio chiede il PIN, pronunciato a cifre o a parole nelle otto lingue; il PIN giusto entro 20 s inoltra il comando |
| politica illeggibile o sconosciuta | `double_turn`: un'impostazione guasta non disattiva mai una protezione |

Il PIN (da 4 a 12 cifre, `ARMOR_VOICE_SILENCE_PIN`) è confrontato in tempo costante e non viene mai registrato, conservato né ripetuto. Tre PIN errati bloccano il silenziamento vocale su **tutti** i pannelli per cinque minuti; con la modalità `pin` richiesta e nessun PIN impostato, nulla viene silenziato con la voce. Il contratto completo è in [docs/SILENCE_POLICY.md](docs/SILENCE_POLICY.md).

### Il turno del pannello a parete

`POST /v1/turn` riceve l'audio di un turno, esegue il comando di riconoscimento vocale, passa le parole alla rotta vocale di ARMOR-SERVER e risponde con ciò che è stato sentito, ciò che va detto e, quando è configurato un comando di sintesi vocale, una registrazione della risposta. Il pannello non ha tastiera, quindi la domanda di `arm` viene ricordata per pannello per 30 secondi e il turno successivo che dice *sì* (nella lingua del pannello) la conferma, mentre quello che dice *no* la annulla. Se il server risponde `disarm`, il turno risponde che per disinserire serve il PIN sullo schermo. Oltre i nove secondi di ascolto non si chiede nulla al server (il pannello rinuncia a dodici), così ciò che è stato detto alla persona e ciò che ha fatto la casa non possono contraddirsi.

### Decisioni registrate

Con `--audit-file`, una riga JSON per decisione: ora, intento, esito e SHA-256 della trascrizione. Mai l'audio e mai le parole.""",
     "security": r"""| Minaccia | Difesa |
|---|---|
| Una trascrizione errata o ostile | Input non attendibile: normalizzato, corrispondenza esatta con una lista chiusa, al massimo 200 caratteri, l'ambiguo *non viene capito*; mai inoltrato come comando di shell o di dispositivo |
| Chi chiama dichiara una conferma | `confirmed` viene rifiutato; conta solo un token firmato dal servizio |
| Un token viene rubato, riprodotto o riutilizzato | Firmato con HMAC-SHA-256, legato a intento e persona, 30 s, monouso; un token non può sopravvivere al proprio istante di emissione anche se l'orologio torna indietro |
| Un'altra persona usa il token di qualcuno | `wrong-subject` |
| Indovinare il PIN di silenziamento | Confronto in tempo costante, 3 tentativi poi 5 minuti di blocco per tutti i pannelli, fallisce in modo chiuso senza PIN |
| Qualcuno in rete raggiunge il servizio | Solo loopback (rifiuta un altro indirizzo senza `--allow-remote`); token di almeno 16 caratteri confrontato in tempo costante; 2 KB per richiesta; una connessione che si blocca viene chiusa dopo 15 s |
| Un motore vocale divulga o abusa dei segreti | Eseguito senza shell, con un ambiente ridotto (`PATH`, `HOME`, `LANG`, `TMPDIR`, `ARMOR_VOICE_ENGINE_*`), un limite di tempo e uno di dimensione; i token del servizio e del server non lo raggiungono mai |
| Esaurire la macchina | Al massimo due turni alla volta (un terzo riceve 503); audio limitato a 480 000 byte |
| I log rivelano ciò che è stato detto | Mai registrato; l'audit contiene solo un hash |
| Un turno scaduto agisce in ritardo | Oltre i nove secondi non viene eseguito nulla (504) |

Il disinserimento a voce **non** avviene mai dal pannello a parete. Dall'app segue l'`ARMOR_DISARM_PIN` del server (impostalo su `required`). Nulla qui è una funzione di sicurezza certificata: un comando accettato è una raccomandazione che ARMOR-SERVER autentica e autorizza comunque. Leggi [docs/SAFETY.md](docs/SAFETY.md) per le regole complete e [SECURITY.md](SECURITY.md) per segnalare una vulnerabilità.""",
     "interfaces": r"""### Servizio HTTP

| Rotta | Autenticazione | Cosa fa |
|---|---|---|
| `GET /healthz` | nessuna | `{"ok": true, "service": "armor-voice"}` |
| `POST /v1/command` | intestazione `X-Armor-Voice-Token` | Corpo `{text, language?, confirmation?, subject?, policy?, pin?}` (al massimo 2 KB). Risponde con ciò che è stato capito, un `confirmation_token` quando serve un secondo turno e `speech` nella lingua richiesta |
| `POST /v1/turn` | la stessa intestazione | Corpo: PCM grezzo mono a 16 bit e 16 kHz, `Content-Type: audio/L16;rate=16000`, fino a 480 000 byte; intestazioni `X-Armor-Language`, `X-Armor-Client`, `X-Armor-Policy`. Risponde `{heard, reply, audio?}` |
| `POST /v1/speak` | la stessa intestazione | Corpo `{text, language}` (al massimo 300 caratteri). Risponde `{audio}`, la frase pronunciata dal programma di sintesi vocale come base64 di PCM mono a 16 bit e 16 kHz (non fa accadere nulla e non conserva nulla); 501 senza quel programma |

Uno scambio reale (il token è abbreviato):

```json
{"text": "arm the system", "subject": "u-1"}
{"accepted": false, "requires_confirmation": true, "intent": "arm", "outcome": "confirmation-needed", "confirmation_token": "eyJpIjoiYXJt...", "reason": "say it again with the confirmation within 30 s", "speech": "Please confirm"}

{"text": "arm the system", "subject": "u-1", "confirmation": "eyJpIjoiYXJt..."}
{"accepted": true, "requires_confirmation": false, "intent": "arm", "outcome": "accepted", "speech": "Command accepted"}

{"text": "open the garage"}
{"accepted": false, "requires_confirmation": false, "intent": null, "outcome": "not-understood", "reason": "the phrase is not one of the known commands", "speech": "Command not recognised"}
```

Esiti: `accepted`, `confirmation-needed`, `confirmation-refused`, `pin-needed`, `pin-refused`, `not-understood`. Una conferma viene rifiutata come `invalid`, `expired`, `wrong-intent`, `wrong-subject` o `replayed`.

### Codici di stato di `/v1/turn`

| Codice | Errore | Significato |
|---|---|---|
| 200 | | `{heard, reply, audio?}` |
| 401 | `unauthorized` | Token mancante o errato |
| 411 / 413 | `bad audio length` | Nessuna lunghezza, o più di 480 000 byte |
| 415 | | Non è `audio/L16;rate=16000` |
| 422 | `invalid language` | Non è una tra `en es de fr it ja zh pt` |
| 501 | `stt_unavailable` / `server_not_configured` | Nessun comando di riconoscimento vocale, o nessun indirizzo del server |
| 502 | `engine_failed` / `server_<code>` / `server_not_answering` | Un motore vocale o il server ha fallito |
| 503 | `busy` | Ci sono già due turni in corso |
| 504 | `turn_too_slow` | Il motore vocale ci ha messo tanto che il server non è stato interrogato; non è stato eseguito nulla |

### Gateway a righe JSON

`python -m armor_voice_ai.gateway` legge un oggetto JSON per riga dallo standard input e scrive la risposta sullo standard output (2 KB per riga; una riga con byte che non sono UTF-8 è una riga come le altre). È lo stesso gateway chiuso, per adattatori vocali e test.

### Contratto con ARMOR-SERVER

* Il server invia la politica di silenziamento a ogni richiesta: `policy` nel corpo di `/v1/command` (e `pin` per la modalità `pin`), l'intestazione `X-Armor-Policy` (un oggetto JSON di al massimo 256 byte) su `/v1/turn`.
* La rotta vocale del server riceve le parole di un turno vocale su `/api/v1/voice/command` con il token operatore dell'installazione, con il nome di ciascun pannello (`X-Armor-Client`).
* Dettagli: [docs/SERVICE.md](docs/SERVICE.md), [docs/SILENCE_POLICY.md](docs/SILENCE_POLICY.md).""",
     "configuration": r"""### Ambiente

| Variabile | Necessaria | Cosa imposta |
|---|---|---|
| `ARMOR_VOICE_TOKEN` | sì (16+ caratteri) | Il token che i chiamanti inviano in `X-Armor-Voice-Token` (o una riga `ARMOR_VOICE_TOKEN=...` nel file di `--token-file`) |
| `ARMOR_VOICE_CONFIRM_SECRET` | consigliata (16+ byte) | Firma le conferme. Senza di essa si usa un segreto casuale e le conferme in sospeso si perdono quando il processo si ferma |
| `ARMOR_VOICE_STT_COMMAND` | per `/v1/turn` | Il programma di riconoscimento vocale: audio (WAV) sullo standard input, le parole sullo standard output |
| `ARMOR_VOICE_TTS_COMMAND` | facoltativa | Il programma di sintesi vocale: testo sullo standard input, un WAV mono a 16 bit e 16 kHz sullo standard output |
| `ARMOR_VOICE_SERVER_URL`, `ARMOR_VOICE_SERVER_TOKEN` | per `/v1/turn` | ARMOR-SERVER e il token operatore della sua rotta vocale |
| `ARMOR_VOICE_SILENCE_PIN` | per la modalità `pin` | Da 4 a 12 cifre. Un valore non valido ferma il servizio all'avvio senza stamparlo |
| `ARMOR_VOICE_ENGINE_*` | facoltativa | Passate ai motori vocali (insieme a `ARMOR_VOICE_LANGUAGE`, impostata a ogni turno) |

### Riga di comando

| Opzione | Predefinito | |
|---|---|---|
| `--host` | `127.0.0.1` | Indirizzo su cui ascoltare; qualunque indirizzo diverso dal loopback viene rifiutato senza `--allow-remote` |
| `--port` | `18090` | |
| `--token-file` | | File con una riga `ARMOR_VOICE_TOKEN=...` |
| `--audit-file` | | Aggiunge una riga per decisione |
| `--allow-remote` | disattivato | Ascolta su un indirizzo non loopback (sconsigliato; solo dietro TLS) |

### Limiti presenti nel codice

| Limite | Valore |
|---|---|
| Validità della conferma | 30 s |
| Domanda vocale ricordata per pannello | 30 s |
| «Sì» dopo una domanda di silenziamento / PIN dopo la richiesta | 15 s / 20 s |
| Tentativi di PIN prima del blocco / durata del blocco | 3 / 5 min |
| Budget del turno / il pannello rinuncia | 9 s / 12 s |
| Limite di tempo di un motore vocale | 25 s |
| Audio massimo / audio di risposta massimo | 480 000 byte / 190 000 byte |
| Corpo della richiesta (`/v1/command`) | 2 KB |
| Lunghezza della trascrizione | 200 caratteri |
| Turni contemporanei | 2 |

Il servizio non scrive mai ciò che è stato detto in un log, qualunque siano le impostazioni.""",
     "quickstart": "**Requisiti:** Python 3.11+ (solo libreria standard). Facoltativo: un programma di riconoscimento vocale e uno di sintesi vocale per `/v1/turn`.\n\n```powershell\n$env:PYTHONPATH = \"src\"\n\n# 1. i test\npython -m unittest discover -s tests                      # 118 test\n\n# 2. il gateway, un oggetto JSON per riga\necho '{\"text\":\"arm the system\"}' | python -m armor_voice_ai.gateway\n\n# 3. il servizio HTTP locale (solo loopback)\n$env:ARMOR_VOICE_TOKEN = \"a-token-of-at-least-16-characters\"\npython -m armor_voice_ai.service --port 18090\n```\n\n```sh\ncurl -s http://127.0.0.1:18090/v1/command \\\n  -H \"X-Armor-Voice-Token: $ARMOR_VOICE_TOKEN\" \\\n  -d '{\"text\":\"status\",\"language\":\"de\"}'\n# {\"accepted\":true,\"requires_confirmation\":false,\"intent\":\"status\",\"outcome\":\"accepted\",\"speech\":\"Befehl akzeptiert\"}\n```\n\nPer ascoltare e parlare (`/v1/turn`), punta il servizio ai tuoi motori e al server:\n\n```sh\nexport ARMOR_VOICE_STT_COMMAND=\"/opt/armor/bin/hear\"        # WAV sull'input, parole sull'output\nexport ARMOR_VOICE_TTS_COMMAND=\"/opt/armor/bin/speak\"       # testo sull'input, WAV sull'output\nexport ARMOR_VOICE_SERVER_URL=\"https://armor-server.local\"\nexport ARMOR_VOICE_SERVER_TOKEN=\"...\"\npython -m armor_voice_ai.service --token-file /opt/armor/etc/armor.voice.env\n```\n\nIl pannello a parete è un dispositivo della rete e il servizio ascolta solo sul loopback: o un proxy del server inoltra il turno, oppure si usa `--allow-remote` dietro TLS. Il token e l'audio non devono attraversare la rete in chiaro.\n\n`run.bat` / `run.sh` e `build.bat` / `build.sh` avviano il flusso di progetto condiviso di [ARMOR-COMMON](https://github.com/JuanenRac/ARMOR-COMMON) (i repository stanno affiancati). Con pip si ha il comando `armor-voice-gateway`.",
     "testing": r"""```powershell
$env:PYTHONPATH = "src"
python -m unittest discover -s tests
python -I tools/armor_ci_validate.py        # manifesto, versione, registro delle modifiche e parità dei README
```

| File di test | Test | Cosa copre |
|---|---|---|
| `test_silence.py` | 31 | La politica di silenziamento, il PIN pronunciato in otto lingue, il blocco |
| `test_edges.py` | 29 | Il protocollo a righe, le impostazioni del servizio, il collegamento al server (un sostituto sul loopback), i limiti dei motori |
| `test_gateway.py` | 23 | Il gateway, la conferma, i replay e le falsificazioni |
| `test_turn.py` | 15 | Il turno, i motori, il sì e il no pronunciati, il budget di tempo |
| `test_languages.py` | 11 | Frasi in forma normale, nessuna frase per due comandi, ogni lingua inserisce, disinserisce, interroga e silenzia |
| `test_service.py` | 5 | Le rotte HTTP |

GitHub Actions esegue la base A.R.M.O.R. a ogni push e pull request: la validazione del manifesto, della versione, del registro delle modifiche e della parità dei README, poi la compilazione e i test propri del progetto.""",
     "build": "È Python puro: nulla da compilare. La versione risiede in `pyproject.toml`, in `armor.project.json` e nel badge del README (letto dal manifesto); ogni versione ha la sua voce in [CHANGELOG.md](CHANGELOG.md). Le versioni sono pubblicate su GitHub.",
     "troubleshooting": r"""| Vedi | Perché | Fai |
|---|---|---|
| `refusing to listen on a non-loopback address without --allow-remote` | `--host` non è `127.0.0.1`, `::1` né `localhost` | Mantieni il loopback e lascia che il proxy del server inoltri, oppure aggiungi `--allow-remote` dietro TLS |
| `a token of at least 16 characters is needed` | `ARMOR_VOICE_TOKEN` manca o è corto | Impostalo, oppure usa `--token-file` |
| `ARMOR_VOICE_SILENCE_PIN is not valid` | Non sono da 4 a 12 cifre ASCII | Correggi il valore (non viene mai stampato) |
| `ARMOR_VOICE_CONFIRM_SECRET is not set` (avviso) | Si usa un segreto casuale | Imposta un segreto di 16+ byte se le conferme devono sopravvivere a un riavvio |
| 401 `unauthorized` | `X-Armor-Voice-Token` mancante o errato | Invia il token |
| 501 `stt_unavailable` | `ARMOR_VOICE_STT_COMMAND` non è impostato | Configura un programma di riconoscimento vocale |
| 501 `server_not_configured` | Nessun indirizzo o token del server | Imposta `ARMOR_VOICE_SERVER_URL` e `ARMOR_VOICE_SERVER_TOKEN` |
| 502 `engine_failed` | Il motore ha fallito, è scaduto o ha risposto troppo (o un WAV di sintesi vocale che non è mono a 16 bit e 16 kHz) | Eseguilo a mano con lo stesso input |
| 504 `turn_too_slow` | Il motore vocale ha impiegato più di nove secondi | Usa un modello più veloce; non è stato eseguito nulla |
| «Per disinserire serve il tuo PIN» | Il disinserimento non avviene mai a voce dal pannello | Usa lo schermo |
| Un «sì» pronunciato non fa nulla | La domanda non era stata ricordata (ci ha messo più di 12 s a essere posta, sono passati più di 30 s, o ha risposto un altro pannello) | Ripeti il comando |""",
     "structure": r"""<p align="center">
  <img src="images/repository-structure.svg" alt="Struttura del repository di ARMOR-VOICE-AI" width="100%">
</p>

<details>
<summary>Versione testuale dell'albero</summary>

```text
ARMOR-VOICE-AI/
├── src/armor_voice_ai/        il codice (solo libreria standard)
│   ├── phrases.py             le 420 frasi dei quindici comandi, in otto lingue
│   ├── intent.py              normalizzazione e corrispondenza esatta: la lista consentita chiusa
│   ├── confirmation.py        token di conferma firmati, monouso, per persona
│   ├── silence_policy.py      off / pin / double_turn, il PIN pronunciato, il blocco
│   ├── session.py             la regola dei due turni per ogni comando
│   ├── gateway.py             righe JSON su stdin/stdout, l'audit, le frasi dette in risposta
│   ├── service.py             il servizio HTTP locale (/healthz, /v1/command, /v1/turn)
│   └── turn.py                un turno vocale: motori, sì/no, budget di tempo
├── tests/                     118 test: silenzio, limiti, gateway, turno, lingue, servizio
├── docs/                      SAFETY.md, SERVICE.md, SILENCE_POLICY.md
├── tools/                     i controlli CI condivisi e gli strumenti del progetto
├── images/                    banner e icona
├── .github/                   workflow CI, avviso della dashboard, modelli di issue e di pull request
├── armor.project.json         manifesto: versione, ruolo, maturità, comando di compilazione
├── pyproject.toml             metadati del pacchetto e il comando `armor-voice-gateway`
├── run.sh run.bat             avviano tramite il flusso di progetto condiviso
├── build.sh build.bat         compilano e testano tramite il flusso di progetto condiviso
├── CHANGELOG.md               cosa è cambiato in ogni versione
└── SECURITY.md SUPPORT.md CONTRIBUTING.md CODE_OF_CONDUCT.md LICENSE
```

</details>""",
     "roadmap": r"""**Limiti noti oggi**

* Non include alcun motore vocale, e nessuno è stato provato con un vero microfono.
* Il pannello touch che dovrebbe ospitare l'assistente non ha girato su una scheda; non c'è una parola di attivazione, è premi per parlare.
* Il turno non dice *quale pannello o quale persona* ha parlato: ARMOR-SERVER decide con il token che gli è stato dato. Aggiungerli alla richiesta è una modifica del contratto tra il server e il pannello.
* Nessuna revisione di sicurezza indipendente.

**Prossimi passi**

* Provare un vero microfono e un vero motore vocale sul banco di prova CM5.
* Eseguire il flusso vocale con il pannello touch una volta che avrà girato su una scheda.
* Conferma facoltativa tramite parlante autenticato o fisica. Un rilascio successivo potrebbe aggiungerla, ma la conferma firmata non verrà rimossa senza una revisione dei rischi documentata.""",
   },
 },
 "de": {
   "tagline": "Offline-Sprachabsichten in acht Sprachen, mit einer Bestätigung, die der Aufrufer nicht fälschen kann",
   "honest": "Die Absichtsregeln, die acht Sprachen, die signierte, an ihren Sprecher gebundene Bestätigung, die Stummschaltungsrichtlinie, der lokale Dienst, der Turn-Endpunkt und das Audit sind real und getestet (118 Tests), und der Server fragt den Dienst auf dem CM5-Prüfstand ab. **Keine Spracherkennungs- oder Sprachsynthese-Engine ist Teil dieses Repositorys**: `/v1/turn` führt die Befehle aus, die du dafür konfigurierst, und keiner davon wurde bisher mit einem echten Mikrofon ausprobiert; das Touch-Panel, das den Assistenten tragen soll, lief noch nicht auf einer Platine.",
   "glance": [
     [
       "Rolle",
       "Offline-Sprach- und Absichts-Gateway (Familie: Core Services, übergeordnet: ARMOR-SERVER)",
     ],
     [
       "Technik",
       "Python 3.11+, nur Standardbibliothek",
     ],
     [
       "Tests",
       "118 (`python -m unittest discover -s tests`)",
     ],
     [
       "Befehle",
       "15 (10 fragen ab, 5 handeln), 420 Sätze, 8 Sprachen",
     ],
     [
       "Lauscht auf",
       "`127.0.0.1:18090` (nur Loopback), mit Token",
     ],
     [
       "Läuft auf",
       "Dem CM5-Prüfstand (als Dienst) oder jedem Computer",
     ],
     [
       "Auf echter Hardware",
       "Läuft als Dienst auf dem CM5-Prüfstand, vom Server abgefragt; kein Mikrofon und keine Sprach-Engine wurde ausprobiert",
     ],
     [
       "Lizenz",
       "GPL-3.0-or-later",
     ],
   ],
   "status": {
     "software": "Die Absichtsregeln, der lokale Dienst und der Turn-Endpunkt laufen als Dienst auf dem CM5-Prüfstand, aber keine Spracherkennungs- oder Sprachsynthese-Engine ist Teil des Repositorys: Es führt die Befehle aus, die du dafür konfigurierst.",
     "tests": "118 Tests bestehen (`python -m unittest discover -s tests`): die Absichtsregeln, die acht Sprachen, die signierte, an ihren Sprecher gebundene Bestätigung, die Stummschaltungsrichtlinie, der lokale Dienst, der Turn-Endpunkt und das Audit.",
     "hardware": "Kein Mikrofon und keine Sprach-Engine wurde ausprobiert, und das Touch-Panel, das den Assistenten tragen soll, lief nicht auf einer Platine.",
     "security": "Die Bestätigung ist signiert und an ihren Sprecher gebunden, und das Audit ist auf dem Host getestet; es gab keine unabhängige Prüfung.",
     "integration": "Der Server fragt den Dienst auf dem CM5-Prüfstand ab; der Sprachablauf mit dem Touch-Panel lief nicht.",
     "docs": "Acht Sprachen und das Änderungsprotokoll sind aktuell.",
   },
   "docs": [
     "[Sprachsicherheit](docs/SAFETY.md): was verstanden wird, die Bestätigung, der Turn des Wandpanels, was aufgezeichnet wird",
     "[Der Dienst](docs/SERVICE.md): Routen, Statuscodes und Einstellungen",
     "[Stummschalten per Sprache](docs/SILENCE_POLICY.md): der Richtlinienvertrag und die PIN",
   ],
   "contributing_first": "Führe vor einem Pull Request `python -I tools/armor_ci_validate.py` und die Tests aus: Beide müssen bestehen. Siehe [CONTRIBUTING.md](CONTRIBUTING.md) und den [Verhaltenskodex](CODE_OF_CONDUCT.md).",
   "languages_extra": "Jeder Satz, den der Dienst zurückspricht, jeder gesprochene Befehl, jedes Ja und Nein und jedes Ziffernwort einer PIN existiert in allen acht Sprachen.",
   "body": {
     "overview": r"""ARMOR-VOICE-AI ist der Teil von A.R.M.O.R., der **das, was eine Person sagt, in einen von fünfzehn Befehlen oder in nichts** verwandelt. Er tut nie etwas von sich aus: Er entscheidet, und [ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER) authentifiziert, autorisiert und führt aus, was akzeptiert wurde, genau wie bei einem Klick in der Konsole.

Der Text, der aus einer Spracherkennung kommt, ist eine *nicht vertrauenswürdige Eingabe*. Deshalb wird er weder interpretiert noch nach Schlüsselwörtern durchsucht noch als Befehl weitergeleitet: Er wird bereinigt (Akzente, Satzzeichen, Höflichkeitsfloskeln) und muss dann **genau** einem der 420 bekannten Sätze entsprechen. Alles andere, jeder zu lange Text und jeder Satz, der zwei Befehle bedeuten könnte, wird *nicht verstanden*.

**Was er tut**

* Versteht fünfzehn Befehle in **acht Sprachen** (Englisch, Spanisch, Deutsch, Französisch, Italienisch, Japanisch, Chinesisch und Portugiesisch).
* Verlangt für `arm` und `disarm` einen **zweiten Turn mit einem vom Dienst signierten Token**, gebunden an die Absicht und an die Person, die sie geäußert hat.
* Kann für `silence` eine gesprochene **PIN** oder einen zweiten Bestätigungs-Turn verlangen, wenn ARMOR-SERVER es anfordert.
* Läuft als **lokaler HTTP-Dienst** und als **JSON-Lines-Gateway** für Adapter und Tests.
* Nimmt das **Audio eines Turns** vom Wandpanel entgegen, führt die konfigurierten Sprach-Engines aus und antwortet als Text und, mit einem Sprachsynthesizer, als Audio.
* Zeichnet **Entscheidungen auf, nie Audio oder Wörter**: einen SHA-256 des Transkripts.

**Was er nicht tut**

* Er erkennt oder synthetisiert keine Sprache: Das sind Programme, die die Installation wählt.
* Er schaltet nichts scharf, unscharf oder stumm: Ein akzeptierter Befehl ist eine Empfehlung an ARMOR-SERVER.
* Er schaltet vom Wandpanel aus nie unscharf: Die PIN wird auf dem Bildschirm getippt, nie laut gesprochen.""",
     "role": r"""[ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER) fragt diesen Dienst ab und authentifiziert und autorisiert den Befehl dann wie bei einem Klick in [ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO). Er ist dafür gedacht, hinter dem Mikrofon des Wandpanels [ARMOR-NODE-HMI](https://github.com/JuanenRac/ARMOR-NODE-HMI) zu leben (Push-to-Talk), und beantwortet den geschriebenen und gesprochenen Assistenten von [ARMOR-ANDROID-CONTROL](https://github.com/JuanenRac/ARMOR-ANDROID-CONTROL). Auf dem Prüfstand wird er von [ARMOR-DEVOPS](https://github.com/JuanenRac/ARMOR-DEVOPS) installiert (`scripts/install_cm5.sh --with-voice`).

| Er spricht mit | Wie | Wozu |
|---|---|---|
| ARMOR-SERVER | `POST /v1/command`, `POST /v1/turn` eingehend; `/api/v1/voice/command` ausgehend | Einen Satz entscheiden; die Wörter eines gesprochenen Turns an die Sprachroute des Servers weitergeben |
| ARMOR-NODE-HMI | Audio eines Turns (16 kHz Mono-PCM) | Das Mikrofon und der Lautsprecher des Wandpanels |
| ARMOR-ANDROID-CONTROL | über den Server | Der geschriebene und gesprochene Assistent |
| Sprach-Engines | Standardeingabe und -ausgabe | Hören (z. B. whisper.cpp, Vosk) und Sprechen (z. B. Piper); von der Installation gewählt |""",
     "architecture": r"""<p align="center">
  <img src="images/architecture.svg" alt="Architektur von ARMOR-VOICE-AI: Aufrufer, ARMOR-SERVER, der Sprachdienst mit seinen Modulen und die von der Installation gewählten Sprach-Engines" width="100%">
</p>

**Ein gesprochener Turn, der das System scharf schaltet** (das Panel wird zweimal gefragt, und Unscharfschalten wird abgelehnt):

<p align="center">
  <img src="images/turn-sequence.svg" alt="A spoken turn that arms the system: the wall panel, ARMOR-VOICE-AI, ARMOR-SERVER and the speech engines, in eleven numbered messages over two turns" width="100%">
</p>

<details>
<summary>Textversion des Diagramms (Mermaid)</summary>

```mermaid
sequenceDiagram
    autonumber
    participant P as Wall panel
    participant V as ARMOR-VOICE-AI
    participant E as Speech engines
    participant S as ARMOR-SERVER
    P->>V: POST /v1/turn (audio, language)
    V->>E: STT: WAV on stdin
    E-->>V: "arm the system"
    V->>S: /api/v1/voice/command {text, language}
    S-->>V: confirmation-needed + token
    V->>E: TTS: "Please confirm"
    V-->>P: heard, reply, audio
    P->>V: POST /v1/turn ("yes")
    V->>S: /api/v1/voice/command {text, confirmation}
    S-->>V: accepted
    V-->>P: "Command accepted"
    Note over V,S: "disarm" is refused here: it needs a PIN, typed on the screen
```

</details>

**Warum er so gebaut ist**

* **Warum eine geschlossene Liste und keine Absichtsklassifikation.** Eine Spracherkennung macht Fehler, und jeder kann in der Nähe eines Mikrofons sprechen. Bei 420 exakten Sätzen kann ein falsches Transkript schlimmstenfalls ignoriert werden, und ein Test prüft, dass kein Satz zu zwei Befehlen gehört.
* **Warum der Dienst nur entscheidet.** Authentifizierung, Autorisierung, Audit-Spur und Aktion bleiben an einem Ort, ARMOR-SERVER; ein Fehler hier kann einen Satz fälschlich akzeptieren, aber keinen Alarm anrühren.
* **Warum die Bestätigung ein signierter, vom Dienst ausgestellter Token ist.** Ein Flag, das der Aufrufer setzt (`confirmed: true`), beweist nichts und wird deshalb abgelehnt. Der Token ist mit HMAC-SHA-256 signiert, an den Befehl und die Person gebunden, 30 Sekunden gültig und nur einmal verwendbar.
* **Warum die Sprach-Engines eigene Programme sind.** Modelle ändern sich schneller, als ein Sicherheits-Gateway es sollte. Sie laufen ohne Shell, mit kurzer Umgebung und Zeitlimit, und die eigenen Geheimnisse des Dienstes erreichen sie nie.
* **Warum nichts aufbewahrt wird.** Das Protokoll zeigt, was entschieden wurde, ohne zu speichern, was gesagt wurde.""",
     "features": r"""### Die fünfzehn Befehle

| Befehl | Art | Bedeutung | Bestätigung |
|---|---|---|---|
| `status` | fragt ab | Der Zustand des Systems | nein |
| `alarms` | fragt ab | Die aktiven Alarme | nein |
| `nodes` | fragt ab | Der Zustand der Knoten | nein |
| `cameras` | fragt ab | Der Zustand der Kameras | nein |
| `radar` | fragt ab | Der Zustand der Radare | nein |
| `solar` | fragt ab | Der Zustand der Solaranlage | nein |
| `electrical` | fragt ab | Der Stromverbrauch | nein |
| `network` | fragt ab | Der Zustand des Netzwerks | nein |
| `time` | fragt ab | Die Uhrzeit | nein |
| `help` | fragt ab | Was gesagt werden kann | nein |
| `silence` | handelt | Die Alarme stummschalten (quittieren) | nur wenn die Richtlinie des Servers es verlangt (siehe unten) |
| `lights_on` | handelt | Das Licht einschalten | nein |
| `lights_off` | handelt | Das Licht ausschalten | nein |
| `arm` | handelt | Den Perimeter scharf schalten | **ja** |
| `disarm` | handelt | Den Perimeter unscharf schalten | **ja** |

Die zehn, die *abfragen*, ändern nichts. Die fünf, die *handeln*, führt ARMOR-SERVER mit der Sitzung der Person aus, die gesprochen hat, nie dieser Dienst.

### Acht Sprachen

Englisch, Spanisch, Deutsch, Französisch, Italienisch, Japanisch, Chinesisch und europäisches Portugiesisch: die Sätze (insgesamt 420), das Ja und Nein einer Bestätigung, die Ziffernwörter einer gesprochenen PIN und jeder Satz, den der Dienst zurückspricht. Die Sätze sind so geschrieben, wie eine Person sie sagt, und werden beim Laden des Moduls mit derselben Funktion normalisiert, die das Gehörte normalisiert, sodass beide nicht auseinanderlaufen können. Höflichkeitsfloskeln (`please`, `por favor`, `bitte`, `s'il vous plaît`, `per favore`...) werden vor dem Vergleich entfernt; Japanisch und Chinesisch, ohne Leerzeichen geschrieben, listen ihre Sätze mit und ohne höfliche Endung.

### Die Bestätigung in zwei Turns

1. Der erste Turn für `arm` oder `disarm` liefert **keine Annahme** und einen `confirmation_token`.
2. Der zweite Turn gibt diesen Token für dieselbe Absicht, **für dieselbe Person**, innerhalb von 30 Sekunden zurück.
3. Der Token ist mit einem Geheimnis signiert, das der Aufrufer nicht hat, sodass er sich weder fälschen noch ändern noch auf eine andere Absicht oder eine andere Person übertragen lässt; er funktioniert nur einmal, und die Nonces der noch nicht abgelaufenen werden nie vergessen, um Platz für neue zu schaffen (sind zu viele gleichzeitig offen, wird der neue Token abgelehnt).

### Stummschalten per Sprache, mit optionaler PIN

„Silence“ wird sofort akzeptiert, sofern die Installation nicht mehr verlangt. ARMOR-SERVER hält die Einstellung `voice.silence_confirmation` und sendet sie als Richtlinie:

| Modus | Was bei „silence“ geschieht |
|---|---|
| `off` (Standard, und wenn keine Richtlinie eintrifft) | Sofort weitergegeben |
| `double_turn` | Nicht ausgeführt; der Dienst bittet darum, Ja zu sagen, und ein Ja innerhalb von 15 s vom selben Panel gibt den ursprünglichen Befehl weiter |
| `pin` | Nicht ausgeführt; der Dienst fragt nach der PIN, gesprochen als Ziffern oder als Ziffernwörter in den acht Sprachen; die richtige PIN innerhalb von 20 s gibt den Befehl weiter |
| unlesbare oder unbekannte Richtlinie | `double_turn`: Eine defekte Einstellung schaltet nie einen Schutz ab |

Die PIN (4 bis 12 Ziffern, `ARMOR_VOICE_SILENCE_PIN`) wird in konstanter Zeit verglichen und nie protokolliert, gespeichert oder zurückgegeben. Drei falsche PINs sperren das Stummschalten per Sprache für **alle** Panels fünf Minuten lang; ist der Modus `pin` verlangt und keine PIN eingerichtet, wird per Sprache nichts stummgeschaltet. Der vollständige Vertrag steht in [docs/SILENCE_POLICY.md](docs/SILENCE_POLICY.md).

### Der Turn des Wandpanels

`POST /v1/turn` nimmt das Audio eines Turns entgegen, führt den Spracherkennungsbefehl aus, gibt die Wörter an die Sprachroute von ARMOR-SERVER und antwortet mit dem Gehörten, dem zu Sagenden und, wenn ein Sprachsynthesebefehl konfiguriert ist, einer Aufnahme davon. Das Panel hat keine Tastatur, daher wird die Frage von `arm` pro Panel 30 Sekunden lang gemerkt, und der nächste Turn, der *Ja* sagt (in der Sprache des Panels), bestätigt sie, der nächste, der *Nein* sagt, bricht sie ab. Antwortet der Server `disarm`, antwortet der Turn, dass zum Unscharfschalten die PIN auf dem Bildschirm nötig ist. Nach neun Sekunden Zuhörzeit wird dem Server nichts mehr gefragt (das Panel gibt nach zwölf auf), sodass sich das, was der Person gesagt wurde, und das, was das Haus tat, nicht widersprechen können.

### Aufgezeichnete Entscheidungen

Mit `--audit-file` eine JSON-Zeile pro Entscheidung: Zeit, Absicht, Ergebnis und der SHA-256 des Transkripts. Nie Audio und nie die Wörter.""",
     "security": r"""| Bedrohung | Abwehr |
|---|---|
| Ein falsches oder feindliches Transkript | Nicht vertrauenswürdige Eingabe: normalisiert, exakter Abgleich mit einer geschlossenen Liste, höchstens 200 Zeichen, Mehrdeutiges wird *nicht verstanden*; nie als Shell- oder Geräte-Befehl weitergeleitet |
| Ein Aufrufer behauptet eine Bestätigung | `confirmed` wird abgelehnt; nur ein vom Dienst signierter Token zählt |
| Ein Token wird gestohlen, wiederholt oder wiederverwendet | Mit HMAC-SHA-256 signiert, an Absicht und Person gebunden, 30 s, einmalig; ein Token kann seine Ausstellungszeit nicht überdauern, auch wenn die Uhr zurückspringt |
| Eine andere Person verwendet den Token von jemandem | `wrong-subject` |
| Erraten der Stummschalt-PIN | Vergleich in konstanter Zeit, 3 Versuche, dann 5 Minuten Sperre für alle Panels, schlägt ohne PIN geschlossen fehl |
| Jemand im Netzwerk erreicht den Dienst | Nur Loopback (lehnt eine andere Adresse ohne `--allow-remote` ab); Token von mindestens 16 Zeichen in konstanter Zeit verglichen; 2 KB pro Anfrage; eine hängende Verbindung wird nach 15 s geschlossen |
| Eine Sprach-Engine gibt Geheimnisse preis oder missbraucht sie | Läuft ohne Shell, mit kurzer Umgebung (`PATH`, `HOME`, `LANG`, `TMPDIR`, `ARMOR_VOICE_ENGINE_*`), Zeitlimit und Größenlimit; die Tokens des Dienstes und des Servers erreichen sie nie |
| Die Maschine erschöpfen | Höchstens zwei Turns gleichzeitig (ein dritter erhält 503); Audio auf 480 000 Bytes begrenzt |
| Protokolle verraten, was gesagt wurde | Nie protokolliert; das Audit enthält nur einen Hash |
| Ein veralteter Turn handelt zu spät | Nach neun Sekunden wird nichts mehr ausgeführt (504) |

Unscharfschalten per Sprache geschieht **nie** vom Wandpanel aus. Aus der App folgt es dem `ARMOR_DISARM_PIN` des Servers (setze ihn auf `required`). Nichts davon ist eine zertifizierte Sicherheitsfunktion: Ein akzeptierter Befehl ist eine Empfehlung, die ARMOR-SERVER weiterhin authentifiziert und autorisiert. Lies [docs/SAFETY.md](docs/SAFETY.md) für die vollständigen Regeln und [SECURITY.md](SECURITY.md), um eine Schwachstelle zu melden.""",
     "interfaces": r"""### HTTP-Dienst

| Route | Authentifizierung | Was sie tut |
|---|---|---|
| `GET /healthz` | keine | `{"ok": true, "service": "armor-voice"}` |
| `POST /v1/command` | Header `X-Armor-Voice-Token` | Body `{text, language?, confirmation?, subject?, policy?, pin?}` (höchstens 2 KB). Antwortet mit dem Verstandenen, einem `confirmation_token`, wenn ein zweiter Turn nötig ist, und `speech` in der gewünschten Sprache |
| `POST /v1/turn` | derselbe Header | Body: rohes 16-kHz-16-Bit-Mono-PCM, `Content-Type: audio/L16;rate=16000`, bis zu 480 000 Bytes; Header `X-Armor-Language`, `X-Armor-Client`, `X-Armor-Policy`. Antwortet `{heard, reply, audio?}` |
| `POST /v1/speak` | derselbe Header | Body `{text, language}` (höchstens 300 Zeichen). Antwortet `{audio}`, den vom Sprachsyntheseprogramm gesprochenen Satz als Base64 von 16-kHz-16-Bit-Mono-PCM (löst nichts aus und speichert nichts); 501 ohne dieses Programm |

Ein echter Austausch (der Token ist gekürzt):

```json
{"text": "arm the system", "subject": "u-1"}
{"accepted": false, "requires_confirmation": true, "intent": "arm", "outcome": "confirmation-needed", "confirmation_token": "eyJpIjoiYXJt...", "reason": "say it again with the confirmation within 30 s", "speech": "Please confirm"}

{"text": "arm the system", "subject": "u-1", "confirmation": "eyJpIjoiYXJt..."}
{"accepted": true, "requires_confirmation": false, "intent": "arm", "outcome": "accepted", "speech": "Command accepted"}

{"text": "open the garage"}
{"accepted": false, "requires_confirmation": false, "intent": null, "outcome": "not-understood", "reason": "the phrase is not one of the known commands", "speech": "Command not recognised"}
```

Ergebnisse: `accepted`, `confirmation-needed`, `confirmation-refused`, `pin-needed`, `pin-refused`, `not-understood`. Eine Bestätigung wird abgelehnt als `invalid`, `expired`, `wrong-intent`, `wrong-subject` oder `replayed`.

### Statuscodes von `/v1/turn`

| Code | Fehler | Bedeutung |
|---|---|---|
| 200 | | `{heard, reply, audio?}` |
| 401 | `unauthorized` | Token fehlt oder ist falsch |
| 411 / 413 | `bad audio length` | Keine Länge oder mehr als 480 000 Bytes |
| 415 | | Nicht `audio/L16;rate=16000` |
| 422 | `invalid language` | Keine von `en es de fr it ja zh pt` |
| 501 | `stt_unavailable` / `server_not_configured` | Kein Spracherkennungsbefehl oder keine Serveradresse |
| 502 | `engine_failed` / `server_<code>` / `server_not_answering` | Eine Sprach-Engine oder der Server ist ausgefallen |
| 503 | `busy` | Es laufen bereits zwei Turns |
| 504 | `turn_too_slow` | Die Sprach-Engine brauchte so lange, dass der Server nicht gefragt wurde; nichts wurde ausgeführt |

### JSON-Lines-Gateway

`python -m armor_voice_ai.gateway` liest ein JSON-Objekt pro Zeile von der Standardeingabe und schreibt die Antwort auf die Standardausgabe (2 KB pro Zeile; eine Zeile mit Bytes, die kein UTF-8 sind, ist eine Zeile wie jede andere). Es ist dasselbe geschlossene Gateway, für Sprachadapter und Tests.

### Vertrag mit ARMOR-SERVER

* Der Server sendet die Stummschaltungsrichtlinie bei jeder Anfrage: `policy` im Body von `/v1/command` (und `pin` für den Modus `pin`), den Header `X-Armor-Policy` (ein JSON-Objekt von höchstens 256 Bytes) bei `/v1/turn`.
* Die Sprachroute des Servers erhält die Wörter eines gesprochenen Turns unter `/api/v1/voice/command` mit dem Operator-Token der Installation, unter dem Namen jedes Panels (`X-Armor-Client`).
* Details: [docs/SERVICE.md](docs/SERVICE.md), [docs/SILENCE_POLICY.md](docs/SILENCE_POLICY.md).""",
     "configuration": r"""### Umgebung

| Variable | Nötig | Was sie festlegt |
|---|---|---|
| `ARMOR_VOICE_TOKEN` | ja (16+ Zeichen) | Der Token, den Aufrufer in `X-Armor-Voice-Token` senden (oder eine Zeile `ARMOR_VOICE_TOKEN=...` in der Datei von `--token-file`) |
| `ARMOR_VOICE_CONFIRM_SECRET` | empfohlen (16+ Bytes) | Signiert die Bestätigungen. Ohne sie wird ein zufälliges Geheimnis verwendet, und ausstehende Bestätigungen gehen beim Beenden des Prozesses verloren |
| `ARMOR_VOICE_STT_COMMAND` | für `/v1/turn` | Das Spracherkennungsprogramm: Audio (WAV) auf der Standardeingabe, die Wörter auf der Standardausgabe |
| `ARMOR_VOICE_TTS_COMMAND` | optional | Das Sprachsyntheseprogramm: Text auf der Standardeingabe, eine 16-kHz-16-Bit-Mono-WAV auf der Standardausgabe |
| `ARMOR_VOICE_SERVER_URL`, `ARMOR_VOICE_SERVER_TOKEN` | für `/v1/turn` | ARMOR-SERVER und der Operator-Token für dessen Sprachroute |
| `ARMOR_VOICE_SILENCE_PIN` | für den Modus `pin` | 4 bis 12 Ziffern. Ein ungültiger Wert stoppt den Dienst beim Start, ohne ihn auszugeben |
| `ARMOR_VOICE_ENGINE_*` | optional | An die Sprach-Engines weitergegeben (zusammen mit `ARMOR_VOICE_LANGUAGE`, pro Turn gesetzt) |

### Kommandozeile

| Option | Standard | |
|---|---|---|
| `--host` | `127.0.0.1` | Adresse, auf der gelauscht wird; alles außer Loopback wird ohne `--allow-remote` abgelehnt |
| `--port` | `18090` | |
| `--token-file` | | Datei mit einer Zeile `ARMOR_VOICE_TOKEN=...` |
| `--audit-file` | | Hängt eine Zeile pro Entscheidung an |
| `--allow-remote` | aus | Lauscht auf einer Nicht-Loopback-Adresse (nicht empfohlen; nur hinter TLS) |

### Grenzen, die im Code stehen

| Grenze | Wert |
|---|---|
| Gültigkeit der Bestätigung | 30 s |
| Gemerkte gesprochene Frage pro Panel | 30 s |
| „Ja“ nach einer Stummschaltfrage / PIN nach der Aufforderung | 15 s / 20 s |
| PIN-Versuche vor der Sperre / Sperrdauer | 3 / 5 min |
| Zeitbudget des Turns / Panel gibt auf | 9 s / 12 s |
| Zeitlimit einer Sprach-Engine | 25 s |
| Größtes Audio / größtes Antwort-Audio | 480 000 Bytes / 190 000 Bytes |
| Anfrage-Body (`/v1/command`) | 2 KB |
| Länge des Transkripts | 200 Zeichen |
| Gleichzeitige Turns | 2 |

Der Dienst schreibt das Gesagte nie in ein Protokoll, egal welche Einstellungen gelten.""",
     "quickstart": "**Voraussetzungen:** Python 3.11+ (nur Standardbibliothek). Optional: ein Spracherkennungs- und ein Sprachsyntheseprogramm für `/v1/turn`.\n\n```powershell\n$env:PYTHONPATH = \"src\"\n\n# 1. die Tests\npython -m unittest discover -s tests                      # 118 Tests\n\n# 2. das Gateway, ein JSON-Objekt pro Zeile\necho '{\"text\":\"arm the system\"}' | python -m armor_voice_ai.gateway\n\n# 3. der lokale HTTP-Dienst (nur Loopback)\n$env:ARMOR_VOICE_TOKEN = \"a-token-of-at-least-16-characters\"\npython -m armor_voice_ai.service --port 18090\n```\n\n```sh\ncurl -s http://127.0.0.1:18090/v1/command \\\n  -H \"X-Armor-Voice-Token: $ARMOR_VOICE_TOKEN\" \\\n  -d '{\"text\":\"status\",\"language\":\"de\"}'\n# {\"accepted\":true,\"requires_confirmation\":false,\"intent\":\"status\",\"outcome\":\"accepted\",\"speech\":\"Befehl akzeptiert\"}\n```\n\nUm zu hören und zu sprechen (`/v1/turn`), richte den Dienst auf deine Engines und auf den Server:\n\n```sh\nexport ARMOR_VOICE_STT_COMMAND=\"/opt/armor/bin/hear\"        # WAV auf der Eingabe, Wörter auf der Ausgabe\nexport ARMOR_VOICE_TTS_COMMAND=\"/opt/armor/bin/speak\"       # Text auf der Eingabe, WAV auf der Ausgabe\nexport ARMOR_VOICE_SERVER_URL=\"https://armor-server.local\"\nexport ARMOR_VOICE_SERVER_TOKEN=\"...\"\npython -m armor_voice_ai.service --token-file /opt/armor/etc/armor.voice.env\n```\n\nDas Wandpanel ist ein Gerät im Netzwerk, und der Dienst lauscht nur auf Loopback: Entweder leitet ein Proxy des Servers den Turn weiter, oder `--allow-remote` wird hinter TLS verwendet. Der Token und das Audio dürfen das Netzwerk nicht im Klartext durchqueren.\n\n`run.bat` / `run.sh` und `build.bat` / `build.sh` starten den gemeinsamen Projektablauf von [ARMOR-COMMON](https://github.com/JuanenRac/ARMOR-COMMON) (die Repositorys liegen nebeneinander). Mit pip steht der Befehl `armor-voice-gateway` zur Verfügung.",
     "testing": r"""```powershell
$env:PYTHONPATH = "src"
python -m unittest discover -s tests
python -I tools/armor_ci_validate.py        # Manifest, Version, Änderungsprotokoll und README-Parität
```

| Testdatei | Tests | Was sie abdeckt |
|---|---|---|
| `test_silence.py` | 31 | Die Stummschaltungsrichtlinie, die gesprochene PIN in acht Sprachen, die Sperre |
| `test_edges.py` | 29 | Das Zeilenprotokoll, die Diensteinstellungen, die Anbindung an den Server (ein Stellvertreter auf Loopback), die Grenzen der Engines |
| `test_gateway.py` | 23 | Das Gateway, die Bestätigung, Wiederholungen und Fälschungen |
| `test_turn.py` | 15 | Der Turn, die Engines, das gesprochene Ja und Nein, das Zeitbudget |
| `test_languages.py` | 11 | Sätze in Normalform, kein Satz für zwei Befehle, jede Sprache schaltet scharf, unscharf, fragt ab und schaltet stumm |
| `test_service.py` | 5 | Die HTTP-Routen |

GitHub Actions führt bei jedem Push und Pull Request die A.R.M.O.R.-Basis aus: die Validierung von Manifest, Version, Änderungsprotokoll und README-Parität, danach den projekteigenen Build und die Tests.""",
     "build": "Es ist reines Python: Es gibt nichts zu kompilieren. Die Version steht in `pyproject.toml`, in `armor.project.json` und im README-Badge (aus dem Manifest gelesen); jede Version hat ihren Eintrag in [CHANGELOG.md](CHANGELOG.md). Releases werden auf GitHub veröffentlicht.",
     "troubleshooting": r"""| Du siehst | Weil | Tu |
|---|---|---|
| `refusing to listen on a non-loopback address without --allow-remote` | `--host` ist nicht `127.0.0.1`, `::1` oder `localhost` | Bleibe bei Loopback und lass den Proxy des Servers weiterleiten, oder füge `--allow-remote` hinter TLS hinzu |
| `a token of at least 16 characters is needed` | `ARMOR_VOICE_TOKEN` fehlt oder ist zu kurz | Setze ihn oder verwende `--token-file` |
| `ARMOR_VOICE_SILENCE_PIN is not valid` | Keine 4 bis 12 ASCII-Ziffern | Korrigiere den Wert (er wird nie ausgegeben) |
| `ARMOR_VOICE_CONFIRM_SECRET is not set` (Warnung) | Ein zufälliges Geheimnis ist im Einsatz | Setze ein Geheimnis von 16+ Bytes, wenn Bestätigungen einen Neustart überstehen sollen |
| 401 `unauthorized` | `X-Armor-Voice-Token` fehlt oder ist falsch | Sende den Token |
| 501 `stt_unavailable` | `ARMOR_VOICE_STT_COMMAND` ist nicht gesetzt | Konfiguriere ein Spracherkennungsprogramm |
| 501 `server_not_configured` | Keine Serveradresse oder kein Server-Token | Setze `ARMOR_VOICE_SERVER_URL` und `ARMOR_VOICE_SERVER_TOKEN` |
| 502 `engine_failed` | Die Engine ist ausgefallen, hat das Zeitlimit überschritten oder zu viel geantwortet (oder eine TTS-WAV, die nicht 16 kHz 16-Bit-Mono ist) | Führe sie von Hand mit derselben Eingabe aus |
| 504 `turn_too_slow` | Die Sprach-Engine brauchte mehr als neun Sekunden | Verwende ein schnelleres Modell; nichts wurde ausgeführt |
| „Zum Unscharfschalten brauchst du deine PIN“ | Unscharfschalten geschieht nie per Sprache vom Panel aus | Nutze den Bildschirm |
| Ein gesprochenes „Ja“ bewirkt nichts | Die Frage wurde nicht gemerkt (sie brauchte über 12 s, es vergingen mehr als 30 s, oder ein anderes Panel antwortete) | Sage den Befehl erneut |""",
     "structure": r"""<p align="center">
  <img src="images/repository-structure.svg" alt="Repository-Struktur von ARMOR-VOICE-AI" width="100%">
</p>

<details>
<summary>Textversion des Baums</summary>

```text
ARMOR-VOICE-AI/
├── src/armor_voice_ai/        der Code (nur Standardbibliothek)
│   ├── phrases.py             die 420 Sätze der fünfzehn Befehle, in acht Sprachen
│   ├── intent.py              Normalisierung und exakter Abgleich: die geschlossene Erlaubnisliste
│   ├── confirmation.py        signierte, einmalige Bestätigungs-Tokens pro Person
│   ├── silence_policy.py      off / pin / double_turn, die gesprochene PIN, die Sperre
│   ├── session.py             die Zwei-Turn-Regel für jeden Befehl
│   ├── gateway.py             JSON-Zeilen über stdin/stdout, das Audit, die zurückgesprochenen Sätze
│   ├── service.py             der lokale HTTP-Dienst (/healthz, /v1/command, /v1/turn)
│   └── turn.py                ein gesprochener Turn: Engines, Ja/Nein, Zeitbudget
├── tests/                     118 Tests: Stummschaltung, Grenzfälle, Gateway, Turn, Sprachen, Dienst
├── docs/                      SAFETY.md, SERVICE.md, SILENCE_POLICY.md
├── tools/                     die gemeinsamen CI-Prüfungen und Projektwerkzeuge
├── images/                    Banner und Symbol
├── .github/                   CI-Workflow, Dashboard-Hinweis, Vorlagen für Issues und Pull Requests
├── armor.project.json         Manifest: Version, Rolle, Reifegrad, Build-Befehl
├── pyproject.toml             Paketmetadaten und der Befehl `armor-voice-gateway`
├── run.sh run.bat             starten über den gemeinsamen Projektablauf
├── build.sh build.bat         bauen und testen über den gemeinsamen Projektablauf
├── CHANGELOG.md               was sich in jeder Version geändert hat
└── SECURITY.md SUPPORT.md CONTRIBUTING.md CODE_OF_CONDUCT.md LICENSE
```

</details>""",
     "roadmap": r"""**Bekannte Grenzen heute**

* Es wird keine Sprach-Engine mitgeliefert, und keine wurde mit einem echten Mikrofon ausprobiert.
* Das Touch-Panel, das den Assistenten tragen soll, lief nicht auf einer Platine; es gibt kein Aktivierungswort, es ist Push-to-Talk.
* Der Turn sagt nicht, *welches Panel oder welche Person* gesprochen hat: ARMOR-SERVER entscheidet mit dem Token, den es erhalten hat. Beides der Anfrage hinzuzufügen, ist eine Änderung des Vertrags zwischen Server und Panel.
* Keine unabhängige Sicherheitsprüfung.

**Als Nächstes**

* Ein echtes Mikrofon und eine echte Sprach-Engine auf dem CM5-Prüfstand ausprobieren.
* Den Sprachablauf mit dem Touch-Panel ausführen, sobald es auf einer Platine gelaufen ist.
* Optionale Bestätigung durch einen authentifizierten Sprecher oder physisch. Ein späterer Einsatz kann sie ergänzen, aber die signierte Bestätigung wird nicht ohne dokumentierte Risikoprüfung entfernt.""",
   },
 },
 "zh": {
   "tagline": "八种语言的离线语音意图，附带调用方无法伪造的确认",
   "honest": "意图规则、八种语言、与说话人绑定的签名确认、静音策略、本地服务、轮次接口和审计都是真实的，并有测试覆盖（118 项测试），服务器在 CM5 测试台上会向该服务发起查询。**本仓库不包含任何语音识别或语音合成引擎**：`/v1/turn` 运行的是你为它们配置的命令，目前没有任何一个用真实麦克风试过；用来承载该助手的触摸面板还没有在板子上运行过。",
   "glance": [
     [
       "角色",
       "离线语音与意图网关（系列：Core Services，上级：ARMOR-SERVER）",
     ],
     [
       "技术栈",
       "Python 3.11+，仅使用标准库",
     ],
     [
       "测试",
       "118 (`python -m unittest discover -s tests`)",
     ],
     [
       "命令",
       "15 个（10 个查询类，5 个执行类），420 个短语，8 种语言",
     ],
     [
       "监听地址",
       "`127.0.0.1:18090`（仅限本机回环），需要令牌",
     ],
     [
       "运行位置",
       "CM5 测试台（作为服务）或任意计算机",
     ],
     [
       "真实硬件",
       "在 CM5 测试台上作为服务运行，由服务器查询；尚未试过任何麦克风或语音引擎",
     ],
     [
       "许可证",
       "GPL-3.0-or-later",
     ],
   ],
   "status": {
     "software": "意图规则、本地服务和轮次接口在 CM5 测试台上作为服务运行，但本仓库不包含任何语音识别或语音合成引擎：它运行的是你为此配置的命令。",
     "tests": "118 项测试通过（`python -m unittest discover -s tests`）：意图规则、八种语言、与说话人绑定的签名确认、静音策略、本地服务、轮次接口和审计。",
     "hardware": "没有试过任何麦克风或语音引擎，用来承载该助手的触摸面板也还没有在板子上运行过。",
     "security": "确认经过签名并与说话人绑定，审计已在主机上测试；没有经过独立审查。",
     "integration": "服务器在 CM5 测试台上查询该服务；与触摸面板配合的语音流程尚未运行。",
     "docs": "八种语言和更新日志均为最新。",
   },
   "docs": [
     "[语音安全](docs/SAFETY.md)：能理解什么、确认、壁挂面板轮次、记录什么",
     "[服务](docs/SERVICE.md)：路由、状态码和设置",
     "[语音静音](docs/SILENCE_POLICY.md)：策略约定和 PIN",
   ],
   "contributing_first": "提交 pull request 之前，请运行 `python -I tools/armor_ci_validate.py` 和测试：两者都必须通过。请参阅 [CONTRIBUTING.md](CONTRIBUTING.md) 和[行为准则](CODE_OF_CONDUCT.md)。",
   "languages_extra": "服务回应的每一句话、每个语音命令、每个“是”和“否”以及 PIN 的每个数字词，都有这八种语言。",
   "body": {
     "overview": r"""ARMOR-VOICE-AI 是 A.R.M.O.R. 中负责把**人说的话转换为十五个命令之一，或者什么都不转换**的部分。它自己从不做任何事：它只负责判定，由 [ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER) 对被接受的内容进行认证、授权并执行，就像处理控制台上的一次点击一样。

语音识别器输出的文字是*不可信输入*。因此它不会被解释、不会按关键词搜索，也不会作为命令转发：它先被清理（重音、标点、客套用语），之后必须与 420 个已知短语之一**完全一致**。其他任何内容、任何过长的内容，以及任何可能对应两个命令的短语，都*不会被理解*。

**它做什么**

* 用**八种语言**（英语、西班牙语、德语、法语、意大利语、日语、汉语和葡萄牙语）理解十五个命令。
* 让 `arm` 和 `disarm` 需要**带有服务签名令牌的第二个轮次**，该令牌与意图以及提出请求的人绑定。
* 当 ARMOR-SERVER 要求时，可让 `silence` 需要口述的 **PIN** 或第二个确认轮次。
* 既作为**本地 HTTP 服务**运行，也作为面向适配器和测试的 **JSON 行网关**运行。
* 从壁挂面板接收**一个轮次的音频**，运行你配置的语音引擎，并以文字回答；配有语音合成器时还以音频回答。
* 记录**决策，绝不记录音频或原话**：只保存转写文本的 SHA-256。

**它不做什么**

* 它不识别也不合成语音：这些是由安装方选择的程序。
* 它不布防、不撤防，也不静音任何东西：被接受的命令只是对 ARMOR-SERVER 的一个建议。
* 它绝不从壁挂面板撤防：PIN 在屏幕上输入，绝不口述。""",
     "role": r"""[ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER) 先查询本服务，然后像处理 [ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) 中的一次点击那样，对命令进行认证和授权。它设计为放在 [ARMOR-NODE-HMI](https://github.com/JuanenRac/ARMOR-NODE-HMI) 壁挂面板的麦克风之后（按键说话），并为 [ARMOR-ANDROID-CONTROL](https://github.com/JuanenRac/ARMOR-ANDROID-CONTROL) 的文字和语音助手提供应答。在测试台上，它由 [ARMOR-DEVOPS](https://github.com/JuanenRac/ARMOR-DEVOPS) 安装（`scripts/install_cm5.sh --with-voice`）。

| 对话对象 | 方式 | 用途 |
|---|---|---|
| ARMOR-SERVER | 入：`POST /v1/command`、`POST /v1/turn`；出：`/api/v1/voice/command` | 判定一个短语；把语音轮次的文字交给服务器自己的语音路由 |
| ARMOR-NODE-HMI | 一个轮次的音频（16 kHz 单声道 PCM） | 壁挂面板的麦克风和扬声器 |
| ARMOR-ANDROID-CONTROL | 经由服务器 | 文字和语音助手 |
| 语音引擎 | 标准输入和输出 | 听（例如 whisper.cpp、Vosk）和说（例如 Piper）；由安装方选择 |""",
     "architecture": r"""<p align="center">
  <img src="images/architecture.svg" alt="ARMOR-VOICE-AI architecture: callers, ARMOR-SERVER, the voice service with its modules, and the speech engines chosen by the installation" width="100%">
</p>

**一个完成布防的语音轮次**（面板会被询问两次，撤防会被拒绝）：

<p align="center">
  <img src="images/turn-sequence.svg" alt="A spoken turn that arms the system: the wall panel, ARMOR-VOICE-AI, ARMOR-SERVER and the speech engines, in eleven numbered messages over two turns" width="100%">
</p>

<details>
<summary>图表的文本版本（Mermaid）</summary>

```mermaid
sequenceDiagram
    autonumber
    participant P as Wall panel
    participant V as ARMOR-VOICE-AI
    participant E as Speech engines
    participant S as ARMOR-SERVER
    P->>V: POST /v1/turn (audio, language)
    V->>E: STT: WAV on stdin
    E-->>V: "arm the system"
    V->>S: /api/v1/voice/command {text, language}
    S-->>V: confirmation-needed + token
    V->>E: TTS: "Please confirm"
    V-->>P: heard, reply, audio
    P->>V: POST /v1/turn ("yes")
    V->>S: /api/v1/voice/command {text, confirmation}
    S-->>V: accepted
    V-->>P: "Command accepted"
    Note over V,S: "disarm" is refused here: it needs a PIN, typed on the screen
```

</details>

**为什么这样构建**

* **为什么用封闭列表而不是意图分类。** 识别器会出错，任何人都可以在麦克风附近说话。有了 420 个精确短语，错误的转写最坏也只是被忽略，并且有一项测试检查没有任何短语同时属于两个命令。
* **为什么服务只负责判定。** 认证、授权、审计记录和动作都集中在 ARMOR-SERVER 一处；这里的缺陷可能错误地接受一个短语，但无法触碰报警。
* **为什么确认是服务签发的签名令牌。** 调用方自己设置的标记（`confirmed: true`）什么也证明不了，所以会被拒绝。令牌使用 HMAC-SHA-256 签名，与命令和人绑定，有效期 30 秒，且只能使用一次。
* **为什么语音引擎是独立的程序。** 模型的变化比安全网关应有的变化速度更快。它们在没有 shell、环境变量精简并带时间限制的条件下运行，服务自身的机密永远不会传给它们。
* **为什么什么都不保存。** 日志显示做出了什么决策，但不保存说过什么。""",
     "features": r"""### 十五个命令

| 命令 | 类型 | 含义 | 确认 |
|---|---|---|---|
| `status` | 查询 | 系统状态 | 否 |
| `alarms` | 查询 | 当前处于激活状态的报警 | 否 |
| `nodes` | 查询 | 节点状态 | 否 |
| `cameras` | 查询 | 摄像头状态 | 否 |
| `radar` | 查询 | 雷达状态 | 否 |
| `solar` | 查询 | 太阳能系统状态 | 否 |
| `electrical` | 查询 | 用电情况 | 否 |
| `network` | 查询 | 网络状态 | 否 |
| `time` | 查询 | 时间 | 否 |
| `help` | 查询 | 可以说什么 | 否 |
| `silence` | 执行 | 静音（确认）报警 | 仅当服务器策略要求时（见下文） |
| `lights_on` | 执行 | 开灯 | 否 |
| `lights_off` | 执行 | 关灯 | 否 |
| `arm` | 执行 | 对周界布防 | **是** |
| `disarm` | 执行 | 对周界撤防 | **是** |

十个*查询*类命令不会改变任何东西。五个*执行*类命令由 ARMOR-SERVER 使用说话人的会话来执行，绝不由本服务执行。

### 八种语言

英语、西班牙语、德语、法语、意大利语、日语、汉语和欧洲葡萄牙语：短语（共 420 个）、确认时的“是”和“否”、口述 PIN 的数字词，以及服务回应的每一句话。短语按人们的说法书写，并在模块加载时用与规范化听到内容相同的函数进行规范化，因此两者不会产生偏差。客套用语（`please`、`por favor`、`bitte`、`s'il vous plaît`、`per favore`……）在比较前会被丢弃；日语和汉语书写时没有空格，会分别列出带礼貌结尾和不带礼貌结尾的短语。

### 两轮确认

1. `arm` 或 `disarm` 的第一个轮次**不返回接受**，而是返回一个 `confirmation_token`。
2. 第二个轮次必须在 30 秒内，为同一个意图、**同一个人**回传该令牌。
3. 令牌用调用方没有的密钥签名，因此无法伪造、篡改，也无法转用于另一个意图或另一个人；它只能使用一次，且未过期令牌的随机数绝不会为腾出空间而被遗忘（同时存在过多时，新令牌会被拒绝）。

### 语音静音，可选 PIN

除非安装方要求更多，“Silence”会被立即接受。ARMOR-SERVER 保存设置 `voice.silence_confirmation`，并将其作为策略发送：

| 模式 | 对“silence”会发生什么 |
|---|---|
| `off`（默认，且在没有收到策略时） | 立即转交 |
| `double_turn` | 不执行；服务要求说“是”，来自同一面板的 15 秒内的“是”会转交原始命令 |
| `pin` | 不执行；服务要求 PIN，可用数字或八种语言的数字词说出；20 秒内说出正确的 PIN 即转交命令 |
| 无法读取或未知的策略 | `double_turn`：损坏的设置绝不会关闭防护 |

PIN（4 到 12 位数字，`ARMOR_VOICE_SILENCE_PIN`）以恒定时间比较，绝不会被记录、保存或回显。连续三次输错 PIN 会使**所有**面板的语音静音锁定五分钟；如果要求 `pin` 而没有设置 PIN，则任何东西都不会被语音静音。完整约定见 [docs/SILENCE_POLICY.md](docs/SILENCE_POLICY.md)。

### 壁挂面板轮次

`POST /v1/turn` 接收一个轮次的音频，运行语音转文字命令，把文字交给 ARMOR-SERVER 的语音路由，并返回听到的内容、要说的话，以及在配置了文字转语音命令时的一段录音。面板没有键盘，所以 `arm` 的询问会按面板记住 30 秒，之后说*是*（使用面板的语言）的下一个轮次会确认它，说*否*的下一个轮次会取消它。如果服务器回答 `disarm`，该轮次会回答撤防需要在屏幕上输入 PIN。收听超过九秒后不再询问服务器（面板在十二秒时放弃），因此对人说的话和房子实际做的事不会相互矛盾。

### 决策记录

使用 `--audit-file` 时，每个决策一行 JSON：时间、意图、结果以及转写文本的 SHA-256。绝不记录音频，也绝不记录原话。""",
     "security": r"""| 威胁 | 防御 |
|---|---|
| 错误或恶意的转写 | 不可信输入：规范化后与封闭列表精确匹配，最多 200 个字符，有歧义即*不理解*；绝不作为 shell 或设备命令转发 |
| 调用方声称已确认 | `confirmed` 会被拒绝；只有服务签名的令牌才算数 |
| 令牌被窃取、重放或重复使用 | 使用 HMAC-SHA-256 签名，绑定意图和人，30 秒，一次性；即使时钟回拨，令牌的存活时间也不会超过其签发时间 |
| 另一个人使用某人的令牌 | `wrong-subject` |
| 猜测静音 PIN | 恒定时间比较，3 次尝试后对所有面板锁定 5 分钟，没有 PIN 时默认拒绝 |
| 网络上的人访问到服务 | 仅限本机回环（没有 `--allow-remote` 时拒绝其他地址）；至少 16 个字符的令牌以恒定时间比较；每个请求 2 KB；停滞的连接在 15 秒后关闭 |
| 语音引擎泄露或滥用机密 | 无 shell，环境变量精简（`PATH`、`HOME`、`LANG`、`TMPDIR`、`ARMOR_VOICE_ENGINE_*`），有时间限制和大小限制；服务和服务器的令牌永远不会传给它 |
| 耗尽机器资源 | 同时最多两个轮次（第三个收到 503）；音频上限 480 000 字节 |
| 日志泄露说过的话 | 绝不记录；审计中只有哈希 |
| 过期的轮次延迟执行 | 超过九秒后不执行任何东西（504） |

语音撤防**绝不会**从壁挂面板进行。从应用发起时，则遵循服务器的 `ARMOR_DISARM_PIN`（将其设为 `required`）。这里的一切都不是安全功能：被接受的命令只是一个建议，ARMOR-SERVER 仍会对其认证和授权。完整规则请阅读 [docs/SAFETY.md](docs/SAFETY.md)，报告漏洞请见 [SECURITY.md](SECURITY.md)。""",
     "interfaces": r"""### HTTP 服务

| 路由 | 认证 | 作用 |
|---|---|---|
| `GET /healthz` | 无 | `{"ok": true, "service": "armor-voice"}` |
| `POST /v1/command` | 请求头 `X-Armor-Voice-Token` | 请求体 `{text, language?, confirmation?, subject?, policy?, pin?}`（最多 2 KB）。返回理解的内容、需要第二个轮次时的 `confirmation_token`，以及所请求语言的 `speech` |
| `POST /v1/turn` | 同一个请求头 | 请求体：原始 16 kHz 16 位单声道 PCM，`Content-Type: audio/L16;rate=16000`，最多 480 000 字节；请求头 `X-Armor-Language`、`X-Armor-Client`、`X-Armor-Policy`。返回 `{heard, reply, audio?}` |
| `POST /v1/speak` | 同一个请求头 | 请求体 `{text, language}`（最多 300 个字符）。返回 `{audio}`，即文字转语音程序说出的句子，为 16 kHz 16 位单声道 PCM 的 base64（不会触发任何操作，也不保存任何内容）；没有该程序时返回 501 |

一次真实的交互（令牌已缩短）：

```json
{"text": "arm the system", "subject": "u-1"}
{"accepted": false, "requires_confirmation": true, "intent": "arm", "outcome": "confirmation-needed", "confirmation_token": "eyJpIjoiYXJt...", "reason": "say it again with the confirmation within 30 s", "speech": "Please confirm"}

{"text": "arm the system", "subject": "u-1", "confirmation": "eyJpIjoiYXJt..."}
{"accepted": true, "requires_confirmation": false, "intent": "arm", "outcome": "accepted", "speech": "Command accepted"}

{"text": "open the garage"}
{"accepted": false, "requires_confirmation": false, "intent": null, "outcome": "not-understood", "reason": "the phrase is not one of the known commands", "speech": "Command not recognised"}
```

结果：`accepted`、`confirmation-needed`、`confirmation-refused`、`pin-needed`、`pin-refused`、`not-understood`。确认被拒绝的原因为 `invalid`、`expired`、`wrong-intent`、`wrong-subject` 或 `replayed`。

### `/v1/turn` 的状态码

| 代码 | 错误 | 含义 |
|---|---|---|
| 200 | | `{heard, reply, audio?}` |
| 401 | `unauthorized` | 缺少令牌或令牌错误 |
| 411 / 413 | `bad audio length` | 没有长度，或超过 480 000 字节 |
| 415 | | 不是 `audio/L16;rate=16000` |
| 422 | `invalid language` | 不是 `en es de fr it ja zh pt` 之一 |
| 501 | `stt_unavailable` / `server_not_configured` | 没有语音转文字命令，或没有服务器地址 |
| 502 | `engine_failed` / `server_<code>` / `server_not_answering` | 语音引擎或服务器失败 |
| 503 | `busy` | 已有两个轮次在运行 |
| 504 | `turn_too_slow` | 语音引擎耗时太长，以至于没有询问服务器；没有执行任何东西 |

### JSON 行网关

`python -m armor_voice_ai.gateway` 从标准输入每行读取一个 JSON 对象，并把应答写到标准输出（每行 2 KB；包含非 UTF-8 字节的行与其他行一样处理）。它是同一个封闭网关，供语音适配器和测试使用。

### 与 ARMOR-SERVER 的约定

* 服务器在每个请求中发送静音策略：在 `/v1/command` 的请求体中为 `policy`（`pin` 模式下还有 `pin`），在 `/v1/turn` 中为请求头 `X-Armor-Policy`（最多 256 字节的 JSON 对象）。
* 服务器的语音路由在 `/api/v1/voice/command` 接收语音轮次的文字，使用安装方的操作员令牌，并以每个面板的名称（`X-Armor-Client`）标识。
* 详情：[docs/SERVICE.md](docs/SERVICE.md)、[docs/SILENCE_POLICY.md](docs/SILENCE_POLICY.md)。""",
     "configuration": r"""### 环境变量

| 变量 | 是否必需 | 设置内容 |
|---|---|---|
| `ARMOR_VOICE_TOKEN` | 是（16 个以上字符） | 调用方在 `X-Armor-Voice-Token` 中发送的令牌（或 `--token-file` 所指文件中的一行 `ARMOR_VOICE_TOKEN=...`） |
| `ARMOR_VOICE_CONFIRM_SECRET` | 推荐（16 个以上字节） | 为确认签名。没有它时会使用随机密钥，进程停止时待处理的确认会丢失 |
| `ARMOR_VOICE_STT_COMMAND` | `/v1/turn` 需要 | 语音转文字程序：标准输入为音频（WAV），标准输出为文字 |
| `ARMOR_VOICE_TTS_COMMAND` | 可选 | 文字转语音程序：标准输入为文字，标准输出为 16 kHz 16 位单声道 WAV |
| `ARMOR_VOICE_SERVER_URL`, `ARMOR_VOICE_SERVER_TOKEN` | `/v1/turn` 需要 | ARMOR-SERVER 以及其语音路由的操作员令牌 |
| `ARMOR_VOICE_SILENCE_PIN` | `pin` 模式需要 | 4 到 12 位数字。无效值会使服务在启动时停止，且不会打印该值 |
| `ARMOR_VOICE_ENGINE_*` | 可选 | 传给语音引擎（连同每个轮次设置的 `ARMOR_VOICE_LANGUAGE`） |

### 命令行

| 选项 | 默认值 | |
|---|---|---|
| `--host` | `127.0.0.1` | 监听地址；没有 `--allow-remote` 时，回环以外的地址都会被拒绝 |
| `--port` | `18090` | |
| `--token-file` | | 包含一行 `ARMOR_VOICE_TOKEN=...` 的文件 |
| `--audit-file` | | 每个决策追加一行 |
| `--allow-remote` | 关闭 | 在非回环地址上监听（不推荐；仅限 TLS 之后） |

### 代码中的限制

| 限制 | 值 |
|---|---|
| 确认有效期 | 30 s |
| 每个面板记住的语音询问 | 30 s |
| 静音询问之后的“是” / 要求之后的 PIN | 15 s / 20 s |
| 锁定前的 PIN 尝试次数 / 锁定时间 | 3 / 5 min |
| 轮次预算 / 面板放弃 | 9 s / 12 s |
| 语音引擎时间限制 | 25 s |
| 最大音频 / 最大应答音频 | 480 000 字节 / 190 000 字节 |
| 请求体（`/v1/command`） | 2 KB |
| 转写长度 | 200 个字符 |
| 同时轮次数 | 2 |

无论如何设置，服务都不会把说过的话写入日志。""",
     "quickstart": "**要求：** Python 3.11+（仅使用标准库）。可选：用于 `/v1/turn` 的语音转文字程序和文字转语音程序。\n\n```powershell\n$env:PYTHONPATH = \"src\"\n\n# 1. 测试\npython -m unittest discover -s tests                      # 118 项测试\n\n# 2. 网关，每行一个 JSON 对象\necho '{\"text\":\"arm the system\"}' | python -m armor_voice_ai.gateway\n\n# 3. 本地 HTTP 服务（仅限本机回环）\n$env:ARMOR_VOICE_TOKEN = \"a-token-of-at-least-16-characters\"\npython -m armor_voice_ai.service --port 18090\n```\n\n```sh\ncurl -s http://127.0.0.1:18090/v1/command \\\n  -H \"X-Armor-Voice-Token: $ARMOR_VOICE_TOKEN\" \\\n  -d '{\"text\":\"status\",\"language\":\"de\"}'\n# {\"accepted\":true,\"requires_confirmation\":false,\"intent\":\"status\",\"outcome\":\"accepted\",\"speech\":\"Befehl akzeptiert\"}\n```\n\n要听和说（`/v1/turn`），请把服务指向你的引擎和服务器：\n\n```sh\nexport ARMOR_VOICE_STT_COMMAND=\"/opt/armor/bin/hear\"        # 标准输入为 WAV，标准输出为文字\nexport ARMOR_VOICE_TTS_COMMAND=\"/opt/armor/bin/speak\"       # 标准输入为文字，标准输出为 WAV\nexport ARMOR_VOICE_SERVER_URL=\"https://armor-server.local\"\nexport ARMOR_VOICE_SERVER_TOKEN=\"...\"\npython -m armor_voice_ai.service --token-file /opt/armor/etc/armor.voice.env\n```\n\n壁挂面板是网络上的设备，而服务只监听本机回环：要么由服务器的代理转发该轮次，要么在 TLS 之后使用 `--allow-remote`。令牌和音频不得在网络中明文传输。\n\n`run.bat` / `run.sh` 和 `build.bat` / `build.sh` 会启动 [ARMOR-COMMON](https://github.com/JuanenRac/ARMOR-COMMON) 的共享项目工作流（各仓库并排放置）。使用 pip 的用户可获得命令 `armor-voice-gateway`。",
     "testing": r"""```powershell
$env:PYTHONPATH = "src"
python -m unittest discover -s tests
python -I tools/armor_ci_validate.py        # 清单、版本、更新日志和 README 一致性
```

| 测试文件 | 测试数 | 覆盖内容 |
|---|---|---|
| `test_silence.py` | 31 | 静音策略、八种语言的口述 PIN、锁定 |
| `test_edges.py` | 29 | 行协议、服务设置、与服务器的连接（回环上的替身）、引擎的限制 |
| `test_gateway.py` | 23 | 网关、确认、重放和伪造 |
| `test_turn.py` | 15 | 轮次、引擎、口述的“是”和“否”、时间预算 |
| `test_languages.py` | 11 | 规范形式的短语、没有短语对应两个命令、每种语言都能布防、撤防、查询和静音 |
| `test_service.py` | 5 | HTTP 路由 |

GitHub Actions 在每次 push 和 pull request 时运行 A.R.M.O.R. 基线：先验证清单、版本、更新日志和 README 一致性，再运行项目自身的构建和测试。""",
     "build": "这是纯 Python：无需编译。版本记录在 `pyproject.toml`、`armor.project.json` 和 README 徽章中（读取自清单）；每个版本在 [CHANGELOG.md](CHANGELOG.md) 中都有对应条目。发布版本发布在 GitHub 上。",
     "troubleshooting": r"""| 你看到 | 原因 | 处理 |
|---|---|---|
| `refusing to listen on a non-loopback address without --allow-remote` | `--host` 不是 `127.0.0.1`、`::1` 或 `localhost` | 保持回环，让服务器的代理转发，或在 TLS 之后添加 `--allow-remote` |
| `a token of at least 16 characters is needed` | 缺少 `ARMOR_VOICE_TOKEN` 或其过短 | 设置它，或使用 `--token-file` |
| `ARMOR_VOICE_SILENCE_PIN is not valid` | 不是 4 到 12 位 ASCII 数字 | 修正该值（它绝不会被打印） |
| `ARMOR_VOICE_CONFIRM_SECRET is not set`（警告） | 正在使用随机密钥 | 如果确认需要在重启后保留，请设置 16 个以上字节的密钥 |
| 401 `unauthorized` | 缺少 `X-Armor-Voice-Token` 或其错误 | 发送令牌 |
| 501 `stt_unavailable` | 未设置 `ARMOR_VOICE_STT_COMMAND` | 配置一个语音转文字程序 |
| 501 `server_not_configured` | 没有服务器地址或令牌 | 设置 `ARMOR_VOICE_SERVER_URL` 和 `ARMOR_VOICE_SERVER_TOKEN` |
| 502 `engine_failed` | 引擎失败、超时或输出过多（或文字转语音的 WAV 不是 16 kHz 16 位单声道） | 用相同的输入手动运行它 |
| 504 `turn_too_slow` | 语音引擎耗时超过九秒 | 使用更快的模型；没有执行任何东西 |
| “Disarming needs your PIN” | 撤防绝不能通过面板上的语音完成 | 使用屏幕 |
| 说出的“是”没有任何反应 | 询问没有被记住（询问耗时超过 12 秒、已超过 30 秒，或由另一个面板作答） | 重新说一遍命令 |""",
     "structure": r"""<p align="center">
  <img src="images/repository-structure.svg" alt="Repository structure of ARMOR-VOICE-AI" width="100%">
</p>

<details>
<summary>目录树的文本版本</summary>

```text
ARMOR-VOICE-AI/
├── src/armor_voice_ai/        代码（仅使用标准库）
│   ├── phrases.py             十五个命令的 420 个短语，八种语言
│   ├── intent.py              规范化与精确匹配：封闭的允许列表
│   ├── confirmation.py        签名的、一次性的、按人区分的确认令牌
│   ├── silence_policy.py      off / pin / double_turn、口述 PIN、锁定
│   ├── session.py             每个命令的两轮规则
│   ├── gateway.py             stdin/stdout 上的 JSON 行、审计、回应的语句
│   ├── service.py             本地 HTTP 服务（/healthz、/v1/command、/v1/turn）
│   └── turn.py                一个语音轮次：引擎、是/否、时间预算
├── tests/                     118 项测试：静音、边界、网关、轮次、语言、服务
├── docs/                      SAFETY.md, SERVICE.md, SILENCE_POLICY.md
├── tools/                     共享的 CI 检查和项目工具
├── images/                    横幅和图标
├── .github/                   CI 工作流、仪表板通知、issue 和 pull request 模板
├── armor.project.json         清单：版本、角色、成熟度、构建命令
├── pyproject.toml             包元数据和 `armor-voice-gateway` 命令
├── run.sh run.bat             通过共享项目工作流启动
├── build.sh build.bat         通过共享项目工作流构建和测试
├── CHANGELOG.md               每个版本的变更
└── SECURITY.md SUPPORT.md CONTRIBUTING.md CODE_OF_CONDUCT.md LICENSE
```

</details>""",
     "roadmap": r"""**当前已知限制**

* 没有随附任何语音引擎，也没有任何一个用真实麦克风试过。
* 用来承载该助手的触摸面板还没有在板子上运行过；没有唤醒词，采用按键说话。
* 轮次不会说明是*哪个面板或哪个人*在说话：ARMOR-SERVER 根据拿到的令牌做出决定。把它们加入请求属于服务器与面板之间约定的变更。
* 没有独立的安全审查。

**下一步**

* 在 CM5 测试台上试用真实麦克风和真实语音引擎。
* 触摸面板在板子上运行之后，运行与它配合的语音流程。
* 可选的已认证说话人或实体确认。以后的部署可以加入它，但在没有记录在案的风险评审之前，不会移除签名确认。""",
   },
 },
 "ja": {
   "tagline": "8 言語に対応したオフライン音声インテント。呼び出し側が偽造できない確認つき",
   "honest": "インテントのルール、8 言語、話者に結び付いた署名付き確認、サイレンスのポリシー、ローカルサービス、ターンのエンドポイント、監査は実在し、テストされています（118 件のテスト）。サーバーは CM5 テストベンチ上でこのサービスに問い合わせます。**音声認識・音声合成のエンジンはこのリポジトリに含まれません**：`/v1/turn` は、あなたが設定したコマンドを実行します。そのどれも、実際のマイクではまだ試していません。アシスタントを載せる予定のタッチパネルは、ボード上ではまだ動いていません。",
   "glance": [
     [
       "役割",
       "オフラインの音声・インテントゲートウェイ（ファミリー：Core Services、親：ARMOR-SERVER）",
     ],
     [
       "技術",
       "Python 3.11+、標準ライブラリのみ",
     ],
     [
       "テスト",
       "118 (`python -m unittest discover -s tests`)",
     ],
     [
       "コマンド",
       "15（問い合わせ 10、操作 5）、420 フレーズ、8 言語",
     ],
     [
       "待ち受け",
       "`127.0.0.1:18090`（ループバックのみ）、トークンつき",
     ],
     [
       "動作環境",
       "CM5 テストベンチ（サービスとして）または任意のコンピューター",
     ],
     [
       "実機での確認",
       "CM5 テストベンチでサービスとして動作し、サーバーから問い合わせを受けています。マイクや音声エンジンは試していません",
     ],
     [
       "ライセンス",
       "GPL-3.0-or-later",
     ],
   ],
   "status": {
     "software": "インテントのルール、ローカルサービス、ターンのエンドポイントは CM5 テストベンチ上でサービスとして動作していますが、音声認識・音声合成のエンジンはリポジトリに含まれません。設定したコマンドを実行します。",
     "tests": "118 件のテストが通ります（`python -m unittest discover -s tests`）：インテントのルール、8 言語、話者に結び付いた署名付き確認、サイレンスのポリシー、ローカルサービス、ターンのエンドポイント、監査。",
     "hardware": "マイクも音声エンジンも試しておらず、アシスタントを載せる予定のタッチパネルもボード上では動いていません。",
     "security": "確認は署名され話者に結び付いており、監査はホスト上でテストされています。独立したレビューはありません。",
     "integration": "サーバーは CM5 テストベンチ上でこのサービスに問い合わせます。タッチパネルとの音声フローはまだ動いていません。",
     "docs": "8 言語と変更履歴は最新です。",
   },
   "docs": [
     "[音声の安全性](docs/SAFETY.md)：何が理解されるか、確認、壁面パネルのターン、何が記録されるか",
     "[サービス](docs/SERVICE.md)：ルート、ステータスコード、設定",
     "[音声でのサイレンス](docs/SILENCE_POLICY.md)：ポリシーのコントラクトと PIN",
   ],
   "contributing_first": "Pull Request の前に `python -I tools/armor_ci_validate.py` とテストを実行してください。どちらも通る必要があります。[CONTRIBUTING.md](CONTRIBUTING.md) と[行動規範](CODE_OF_CONDUCT.md)を参照してください。",
   "languages_extra": "サービスが返すすべての文、すべての音声コマンド、すべての「はい」と「いいえ」、PIN のすべての数字の言葉が、8 言語すべてに存在します。",
   "body": {
     "overview": r"""ARMOR-VOICE-AI は A.R.M.O.R. の一部で、**人が話したことを 15 のコマンドのどれか、または何でもないもの**に変換します。自分では何も実行しません。判断するだけで、受け入れられたものは [ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER) がコンソールでのクリックと同じように認証、認可、実行します。

音声認識器から出てくるテキストは*信頼できない入力*です。そのため解釈もキーワード検索もコマンドとしての転送もしません。まず整形（アクセント、句読点、丁寧な前置き）してから、既知の 420 フレーズのどれかと**完全に一致**しなければなりません。それ以外のもの、長すぎるもの、2 つのコマンドに取れるフレーズは*理解されません*。

**できること**

* 15 のコマンドを **8 言語**（英語、スペイン語、ドイツ語、フランス語、イタリア語、日本語、中国語、ポルトガル語）で理解します。
* `arm` と `disarm` には、インテントと依頼した人に結び付いた、**サービスが署名したトークンを伴う 2 回目のターン**を必要とします。
* ARMOR-SERVER が求めたとき、`silence` に音声での **PIN** または確認の 2 回目のターンを必要とさせることができます。
* **ローカル HTTP サービス**として、またアダプターとテスト用の **JSON Lines ゲートウェイ**として動作します。
* 壁面パネルから **1 ターン分の音声**を受け取り、設定した音声エンジンを実行して、テキストで、音声合成器があれば音声でも応答します。
* 記録するのは**判断だけで、音声も言葉も残しません**：書き起こしの SHA-256 のみです。

**できないこと**

* 音声の認識も合成もしません。それは設備が選ぶプログラムです。
* 警戒、解除、サイレンスは一切しません。受け入れられたコマンドは ARMOR-SERVER への推奨です。
* 壁面パネルからの解除は一切行いません。PIN は画面で入力するもので、声には出しません。""",
     "role": r"""[ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER) がこのサービスに問い合わせ、その後 [ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO) でのクリックと同じようにコマンドを認証、認可します。[ARMOR-NODE-HMI](https://github.com/JuanenRac/ARMOR-NODE-HMI) 壁面パネルのマイクの後ろ（プッシュトゥトーク）に置く想定で、[ARMOR-ANDROID-CONTROL](https://github.com/JuanenRac/ARMOR-ANDROID-CONTROL) の文字・音声アシスタントにも応答します。テストベンチでは [ARMOR-DEVOPS](https://github.com/JuanenRac/ARMOR-DEVOPS)（`scripts/install_cm5.sh --with-voice`）がインストールします。

| 連携先 | 方法 | 目的 |
|---|---|---|
| ARMOR-SERVER | 受信：`POST /v1/command`、`POST /v1/turn`。送信：`/api/v1/voice/command` | フレーズの判断。音声ターンの言葉をサーバー自身の音声ルートへ渡す |
| ARMOR-NODE-HMI | 1 ターン分の音声（16 kHz モノラル PCM） | 壁面パネルのマイクとスピーカー |
| ARMOR-ANDROID-CONTROL | サーバー経由 | 文字・音声アシスタント |
| 音声エンジン | 標準入力と標準出力 | 聞く（例：whisper.cpp、Vosk）と話す（例：Piper）。設備が選ぶ |""",
     "architecture": r"""<p align="center">
  <img src="images/architecture.svg" alt="ARMOR-VOICE-AI architecture: callers, ARMOR-SERVER, the voice service with its modules, and the speech engines chosen by the installation" width="100%">
</p>

**システムを警戒状態にする音声ターン**（パネルには 2 回尋ね、解除は拒否されます）：

<p align="center">
  <img src="images/turn-sequence.svg" alt="A spoken turn that arms the system: the wall panel, ARMOR-VOICE-AI, ARMOR-SERVER and the speech engines, in eleven numbered messages over two turns" width="100%">
</p>

<details>
<summary>図のテキスト版（Mermaid）</summary>

```mermaid
sequenceDiagram
    autonumber
    participant P as Wall panel
    participant V as ARMOR-VOICE-AI
    participant E as Speech engines
    participant S as ARMOR-SERVER
    P->>V: POST /v1/turn (audio, language)
    V->>E: STT: WAV on stdin
    E-->>V: "arm the system"
    V->>S: /api/v1/voice/command {text, language}
    S-->>V: confirmation-needed + token
    V->>E: TTS: "Please confirm"
    V-->>P: heard, reply, audio
    P->>V: POST /v1/turn ("yes")
    V->>S: /api/v1/voice/command {text, confirmation}
    S-->>V: accepted
    V-->>P: "Command accepted"
    Note over V,S: "disarm" is refused here: it needs a PIN, typed on the screen
```

</details>

**この作りにした理由**

* **インテント分類ではなく閉じたリストにする理由。** 認識器は間違えますし、マイクの近くでは誰でも話せます。420 の正確なフレーズなら、誤った書き起こしが起こせる最悪の事態は無視されることだけで、どのフレーズも 2 つのコマンドに属さないことはテストで確認しています。
* **サービスが判断だけをする理由。** 認証、認可、監査記録、アクションは ARMOR-SERVER の 1 か所にあります。ここのバグはフレーズを誤って受け入れることはあっても、警報には触れられません。
* **確認をサービスが発行する署名付きトークンにする理由。** 呼び出し側が立てるフラグ（`confirmed: true`）は何も証明しないので拒否されます。トークンは HMAC-SHA-256 で署名され、コマンドと人に結び付き、30 秒間有効で、一度だけ使えます。
* **音声エンジンを別プログラムにする理由。** モデルはセキュリティゲートウェイが変わるべき速度より速く変わります。シェルなし、短い環境変数、時間制限つきで実行し、サービス自身のシークレットは決して渡しません。
* **何も保存しない理由。** ログには何が判断されたかが残り、何が話されたかは残りません。""",
     "features": r"""### 15 のコマンド

| コマンド | 種類 | 意味 | 確認 |
|---|---|---|---|
| `status` | 問い合わせ | システムの状態 | なし |
| `alarms` | 問い合わせ | 有効な警報 | なし |
| `nodes` | 問い合わせ | ノードの状態 | なし |
| `cameras` | 問い合わせ | カメラの状態 | なし |
| `radar` | 問い合わせ | レーダーの状態 | なし |
| `solar` | 問い合わせ | ソーラーシステムの状態 | なし |
| `electrical` | 問い合わせ | 電気の消費量 | なし |
| `network` | 問い合わせ | ネットワークの状態 | なし |
| `time` | 問い合わせ | 時刻 | なし |
| `help` | 問い合わせ | 言えること | なし |
| `silence` | 操作 | 警報をサイレンス（確認応答）する | サーバーのポリシーが求める場合のみ（下記参照） |
| `lights_on` | 操作 | 照明をつける | なし |
| `lights_off` | 操作 | 照明を消す | なし |
| `arm` | 操作 | 境界を警戒状態にする | **あり** |
| `disarm` | 操作 | 境界の警戒を解除する | **あり** |

*問い合わせ*の 10 個は何も変更しません。*操作*の 5 個は、このサービスではなく ARMOR-SERVER が、話した人のセッションで実行します。

### 8 言語

英語、スペイン語、ドイツ語、フランス語、イタリア語、日本語、中国語、ヨーロッパポルトガル語：フレーズ（合計 420）、確認の「はい」と「いいえ」、音声 PIN の数字の言葉、そしてサービスが返すすべての文。フレーズは人が言う形で書かれ、モジュールの読み込み時に、聞き取った内容を整形するのと同じ関数で整形されるため、両者がずれることはありません。丁寧な前置き（`please`、`por favor`、`bitte`、`s'il vous plaît`、`per favore`…）は比較の前に取り除かれます。スペースなしで書く日本語と中国語は、丁寧な語尾ありとなしの両方のフレーズを並べています。

### 2 ターンの確認

1. `arm` または `disarm` の最初のターンは**受け入れを返さず**、`confirmation_token` を返します。
2. 2 回目のターンは、同じインテントについて、**同じ人**が、30 秒以内にそのトークンを返します。
3. トークンは呼び出し側が持たないシークレットで署名されるため、偽造も改ざんも、別のインテントや別の人への流用もできません。一度しか使えず、期限内のトークンのノンスは新しいものの場所を空けるために忘れられることはありません（同時に多すぎる場合は、新しいトークンが拒否されます）。

### 音声でのサイレンス、任意の PIN

設備がそれ以上を求めない限り、「Silence」はすぐに受け入れられます。ARMOR-SERVER は設定 `voice.silence_confirmation` を保持し、ポリシーとして送ります：

| モード | 「silence」で起きること |
|---|---|
| `off`（既定。ポリシーが届かないときも） | すぐに渡す |
| `double_turn` | 実行しない。サービスが「はい」と言うよう求め、同じパネルから 15 秒以内の「はい」で元のコマンドを渡す |
| `pin` | 実行しない。サービスが PIN を求め、数字または 8 言語の数字の言葉で話す。20 秒以内の正しい PIN でコマンドを渡す |
| 読み取れない、または未知のポリシー | `double_turn`：壊れた設定が保護をオフにすることはありません |

PIN（4〜12 桁、`ARMOR_VOICE_SILENCE_PIN`）は一定時間で比較され、記録も保存も復唱もされません。PIN を 3 回間違えると、**すべての**パネルで音声によるサイレンスが 5 分間ロックされます。`pin` が求められているのに PIN が設定されていない場合、音声では何もサイレンスされません。完全な仕様は [docs/SILENCE_POLICY.md](docs/SILENCE_POLICY.md) にあります。

### 壁面パネルのターン

`POST /v1/turn` は 1 ターン分の音声を受け取り、音声からテキストへのコマンドを実行し、その言葉を ARMOR-SERVER の音声ルートへ渡して、聞き取った内容、返すべき言葉、そしてテキストから音声へのコマンドが設定されていればその録音を返します。パネルにはキーボードがないため、`arm` の質問はパネルごとに 30 秒間記憶され、次に*はい*（パネルの言語で）と言うターンが確認し、*いいえ*と言うターンが取り消します。サーバーが `disarm` と答えた場合、そのターンは、解除には画面での PIN が必要だと返します。聞き取りに 9 秒を超えるとサーバーには何も問い合わせません（パネルは 12 秒で諦めます）。そのため、人に伝えた内容と家が実際にしたことが食い違うことはありません。

### 判断の記録

`--audit-file` を指定すると、判断ごとに 1 行の JSON を残します：時刻、インテント、結果、書き起こしの SHA-256。音声も言葉も決して残しません。""",
     "security": r"""| 脅威 | 防御 |
|---|---|
| 誤った、または悪意のある書き起こし | 信頼できない入力：整形し、閉じたリストと完全一致、最大 200 文字、曖昧なら*理解しない*。シェルやデバイスのコマンドとして転送することはありません |
| 呼び出し側が確認を主張する | `confirmed` は拒否。サービスが署名したトークンだけが有効 |
| トークンの盗用、リプレイ、再利用 | HMAC-SHA-256 で署名、インテントと人に結び付け、30 秒、一度だけ。時計が戻ってもトークンは発行時刻より長く生きられません |
| 別の人が誰かのトークンを使う | `wrong-subject` |
| サイレンス PIN の推測 | 一定時間での比較、3 回失敗で全パネルを 5 分ロック、PIN がなければフェイルクローズ |
| ネットワーク上の誰かがサービスに到達する | ループバックのみ（`--allow-remote` なしでは他のアドレスを拒否）。16 文字以上のトークンを一定時間で比較。1 リクエスト 2 KB。止まった接続は 15 秒で閉じる |
| 音声エンジンがシークレットを漏らす、悪用する | シェルなし、短い環境変数（`PATH`、`HOME`、`LANG`、`TMPDIR`、`ARMOR_VOICE_ENGINE_*`）、時間制限とサイズ制限。サービスとサーバーのトークンは決して渡さない |
| マシンの枯渇 | 同時に最大 2 ターン（3 つ目は 503）。音声は 480 000 バイトまで |
| ログから話した内容が分かる | 記録しない。監査にはハッシュのみ |
| 古くなったターンが遅れて動く | 9 秒を超えたら何も実行しない（504） |

音声での解除は、壁面パネルからは**決して**行いません。アプリからはサーバーの `ARMOR_DISARM_PIN` に従います（`required` に設定してください）。ここにある何ものも安全機能ではありません。受け入れられたコマンドは推奨であり、ARMOR-SERVER が引き続き認証と認可を行います。完全なルールは [docs/SAFETY.md](docs/SAFETY.md)、脆弱性の報告は [SECURITY.md](SECURITY.md) をお読みください。""",
     "interfaces": r"""### HTTP サービス

| ルート | 認証 | 内容 |
|---|---|---|
| `GET /healthz` | なし | `{"ok": true, "service": "armor-voice"}` |
| `POST /v1/command` | ヘッダー `X-Armor-Voice-Token` | ボディ `{text, language?, confirmation?, subject?, policy?, pin?}`（最大 2 KB）。理解した内容、2 回目のターンが必要なときの `confirmation_token`、要求された言語の `speech` を返す |
| `POST /v1/turn` | 同じヘッダー | ボディ：生の 16 kHz 16 ビットモノラル PCM、`Content-Type: audio/L16;rate=16000`、最大 480 000 バイト。ヘッダー `X-Armor-Language`、`X-Armor-Client`、`X-Armor-Policy`。`{heard, reply, audio?}` を返す |
| `POST /v1/speak` | 同じヘッダー | ボディ `{text, language}`（最大 300 文字）。`{audio}` を返す。音声合成プログラムが読み上げた文を 16 kHz 16 ビットモノラル PCM の base64 で返す（何も実行せず、何も保存しない）。そのプログラムがなければ 501 |

実際のやり取りの例（トークンは短縮しています）：

```json
{"text": "arm the system", "subject": "u-1"}
{"accepted": false, "requires_confirmation": true, "intent": "arm", "outcome": "confirmation-needed", "confirmation_token": "eyJpIjoiYXJt...", "reason": "say it again with the confirmation within 30 s", "speech": "Please confirm"}

{"text": "arm the system", "subject": "u-1", "confirmation": "eyJpIjoiYXJt..."}
{"accepted": true, "requires_confirmation": false, "intent": "arm", "outcome": "accepted", "speech": "Command accepted"}

{"text": "open the garage"}
{"accepted": false, "requires_confirmation": false, "intent": null, "outcome": "not-understood", "reason": "the phrase is not one of the known commands", "speech": "Command not recognised"}
```

結果：`accepted`、`confirmation-needed`、`confirmation-refused`、`pin-needed`、`pin-refused`、`not-understood`。確認は `invalid`、`expired`、`wrong-intent`、`wrong-subject`、`replayed` として拒否されます。

### `/v1/turn` のステータスコード

| コード | エラー | 意味 |
|---|---|---|
| 200 | | `{heard, reply, audio?}` |
| 401 | `unauthorized` | トークンがない、または誤り |
| 411 / 413 | `bad audio length` | 長さがない、または 480 000 バイト超 |
| 415 | | `audio/L16;rate=16000` ではない |
| 422 | `invalid language` | `en es de fr it ja zh pt` のどれでもない |
| 501 | `stt_unavailable` / `server_not_configured` | 音声からテキストへのコマンドがない、またはサーバーのアドレスがない |
| 502 | `engine_failed` / `server_<code>` / `server_not_answering` | 音声エンジンまたはサーバーが失敗した |
| 503 | `busy` | すでに 2 ターンが実行中 |
| 504 | `turn_too_slow` | 音声エンジンに時間がかかりすぎてサーバーに問い合わせなかった。何も実行されていない |

### JSON Lines ゲートウェイ

`python -m armor_voice_ai.gateway` は標準入力から 1 行に 1 つの JSON オブジェクトを読み、応答を標準出力に書きます（1 行 2 KB。UTF-8 でないバイトを含む行も他の行と同じ扱いです）。これは同じ閉じたゲートウェイで、音声アダプターとテスト用です。

### ARMOR-SERVER とのコントラクト

* サーバーはすべてのリクエストでサイレンスのポリシーを送ります：`/v1/command` ではボディの `policy`（`pin` モードでは `pin` も）、`/v1/turn` ではヘッダー `X-Armor-Policy`（最大 256 バイトの JSON オブジェクト）です。
* サーバーの音声ルートは、音声ターンの言葉を `/api/v1/voice/command` で、設備のオペレータートークンを使い、各パネルの名前（`X-Armor-Client`）で受け取ります。
* 詳細：[docs/SERVICE.md](docs/SERVICE.md)、[docs/SILENCE_POLICY.md](docs/SILENCE_POLICY.md)。""",
     "configuration": r"""### 環境変数

| 変数 | 必要 | 設定する内容 |
|---|---|---|
| `ARMOR_VOICE_TOKEN` | はい（16 文字以上） | 呼び出し側が `X-Armor-Voice-Token` で送るトークン（または `--token-file` のファイル内の `ARMOR_VOICE_TOKEN=...` という行） |
| `ARMOR_VOICE_CONFIRM_SECRET` | 推奨（16 バイト以上） | 確認に署名する。ない場合はランダムなシークレットが使われ、保留中の確認はプロセス停止時に失われる |
| `ARMOR_VOICE_STT_COMMAND` | `/v1/turn` に必要 | 音声からテキストへのプログラム：標準入力に音声（WAV）、標準出力に言葉 |
| `ARMOR_VOICE_TTS_COMMAND` | 任意 | テキストから音声へのプログラム：標準入力にテキスト、標準出力に 16 kHz 16 ビットモノラルの WAV |
| `ARMOR_VOICE_SERVER_URL`, `ARMOR_VOICE_SERVER_TOKEN` | `/v1/turn` に必要 | ARMOR-SERVER と、その音声ルート用のオペレータートークン |
| `ARMOR_VOICE_SILENCE_PIN` | `pin` モードに必要 | 4〜12 桁。無効な値だと値を出力せずに起動時にサービスが停止する |
| `ARMOR_VOICE_ENGINE_*` | 任意 | 音声エンジンへ渡される（ターンごとに設定される `ARMOR_VOICE_LANGUAGE` とともに） |

### コマンドライン

| フラグ | 既定値 | |
|---|---|---|
| `--host` | `127.0.0.1` | 待ち受けるアドレス。ループバック以外は `--allow-remote` なしでは拒否される |
| `--port` | `18090` | |
| `--token-file` | | `ARMOR_VOICE_TOKEN=...` の行を持つファイル |
| `--audit-file` | | 判断ごとに 1 行を追記する |
| `--allow-remote` | オフ | ループバック以外のアドレスで待ち受ける（非推奨。TLS の背後でのみ） |

### コードにある制限

| 制限 | 値 |
|---|---|
| 確認の有効期間 | 30 s |
| パネルごとに記憶される音声の質問 | 30 s |
| サイレンスの質問後の「はい」 / 求めた後の PIN | 15 s / 20 s |
| ロックまでの PIN 試行回数 / ロック時間 | 3 / 5 min |
| ターンの持ち時間 / パネルが諦めるまで | 9 s / 12 s |
| 音声エンジンの時間制限 | 25 s |
| 最大の音声 / 最大の応答音声 | 480 000 バイト / 190 000 バイト |
| リクエストボディ（`/v1/command`） | 2 KB |
| 書き起こしの長さ | 200 文字 |
| 同時ターン数 | 2 |

設定にかかわらず、サービスは話された内容をログに書きません。""",
     "quickstart": "**要件：** Python 3.11+（標準ライブラリのみ）。任意：`/v1/turn` 用の音声からテキストへのプログラムとテキストから音声へのプログラム。\n\n```powershell\n$env:PYTHONPATH = \"src\"\n\n# 1. テスト\npython -m unittest discover -s tests                      # 118 件のテスト\n\n# 2. ゲートウェイ、1 行に 1 つの JSON オブジェクト\necho '{\"text\":\"arm the system\"}' | python -m armor_voice_ai.gateway\n\n# 3. ローカル HTTP サービス（ループバックのみ）\n$env:ARMOR_VOICE_TOKEN = \"a-token-of-at-least-16-characters\"\npython -m armor_voice_ai.service --port 18090\n```\n\n```sh\ncurl -s http://127.0.0.1:18090/v1/command \\\n  -H \"X-Armor-Voice-Token: $ARMOR_VOICE_TOKEN\" \\\n  -d '{\"text\":\"status\",\"language\":\"de\"}'\n# {\"accepted\":true,\"requires_confirmation\":false,\"intent\":\"status\",\"outcome\":\"accepted\",\"speech\":\"Befehl akzeptiert\"}\n```\n\n聞いて話す（`/v1/turn`）には、サービスを自分のエンジンとサーバーに向けます：\n\n```sh\nexport ARMOR_VOICE_STT_COMMAND=\"/opt/armor/bin/hear\"        # 標準入力に WAV、標準出力に言葉\nexport ARMOR_VOICE_TTS_COMMAND=\"/opt/armor/bin/speak\"       # 標準入力にテキスト、標準出力に WAV\nexport ARMOR_VOICE_SERVER_URL=\"https://armor-server.local\"\nexport ARMOR_VOICE_SERVER_TOKEN=\"...\"\npython -m armor_voice_ai.service --token-file /opt/armor/etc/armor.voice.env\n```\n\n壁面パネルはネットワーク上のデバイスで、サービスはループバックでしか待ち受けません。サーバーのプロキシがターンを転送するか、TLS の背後で `--allow-remote` を使います。トークンと音声は平文でネットワークを通してはいけません。\n\n`run.bat` / `run.sh` と `build.bat` / `build.sh` は、[ARMOR-COMMON](https://github.com/JuanenRac/ARMOR-COMMON) の共通プロジェクトワークフローを起動します（リポジトリは並べて置きます）。pip を使う場合は `armor-voice-gateway` コマンドが使えます。",
     "testing": r"""```powershell
$env:PYTHONPATH = "src"
python -m unittest discover -s tests
python -I tools/armor_ci_validate.py        # マニフェスト、バージョン、変更履歴、README の整合
```

| テストファイル | テスト数 | 対象 |
|---|---|---|
| `test_silence.py` | 31 | サイレンスのポリシー、8 言語の音声 PIN、ロック |
| `test_edges.py` | 29 | 行プロトコル、サービスの設定、サーバーとの接続（ループバック上の代役）、エンジンの制限 |
| `test_gateway.py` | 23 | ゲートウェイ、確認、リプレイと偽造 |
| `test_turn.py` | 15 | ターン、エンジン、音声の「はい」と「いいえ」、時間の持ち時間 |
| `test_languages.py` | 11 | 正規形のフレーズ、2 つのコマンドに属するフレーズがないこと、各言語で警戒、解除、問い合わせ、サイレンスができること |
| `test_service.py` | 5 | HTTP ルート |

GitHub Actions は、push と pull request のたびに A.R.M.O.R. のベースラインを実行します：マニフェスト、バージョン、変更履歴、README の整合の検証に続き、プロジェクト自身のビルドとテストです。""",
     "build": "純粋な Python なので、コンパイルするものはありません。バージョンは `pyproject.toml`、`armor.project.json`、README のバッジ（マニフェストから読み取り）にあり、各バージョンには [CHANGELOG.md](CHANGELOG.md) にエントリーがあります。リリースは GitHub で公開されます。",
     "troubleshooting": r"""| 表示 | 原因 | 対処 |
|---|---|---|
| `refusing to listen on a non-loopback address without --allow-remote` | `--host` が `127.0.0.1`、`::1`、`localhost` ではない | ループバックのままにしてサーバーのプロキシに転送させるか、TLS の背後で `--allow-remote` を追加する |
| `a token of at least 16 characters is needed` | `ARMOR_VOICE_TOKEN` がない、または短い | 設定するか、`--token-file` を使う |
| `ARMOR_VOICE_SILENCE_PIN is not valid` | 4〜12 桁の ASCII 数字ではない | 値を直す（出力されることはありません） |
| `ARMOR_VOICE_CONFIRM_SECRET is not set`（警告） | ランダムなシークレットが使われている | 確認を再起動後も残したいなら、16 バイト以上のシークレットを設定する |
| 401 `unauthorized` | `X-Armor-Voice-Token` がない、または誤り | トークンを送る |
| 501 `stt_unavailable` | `ARMOR_VOICE_STT_COMMAND` が未設定 | 音声からテキストへのプログラムを設定する |
| 501 `server_not_configured` | サーバーのアドレスまたはトークンがない | `ARMOR_VOICE_SERVER_URL` と `ARMOR_VOICE_SERVER_TOKEN` を設定する |
| 502 `engine_failed` | エンジンが失敗した、タイムアウトした、または出力が多すぎた（あるいはテキストから音声への WAV が 16 kHz 16 ビットモノラルではない） | 同じ入力で手動実行してみる |
| 504 `turn_too_slow` | 音声エンジンが 9 秒以上かかった | より速いモデルを使う。何も実行されていない |
| "Disarming needs your PIN" | パネルからの音声による解除は一切行われない | 画面を使う |
| 話した「はい」が何も起こさない | 質問が記憶されていなかった（質問に 12 秒超かかった、30 秒以上経過した、または別のパネルが答えた） | コマンドをもう一度言う |""",
     "structure": r"""<p align="center">
  <img src="images/repository-structure.svg" alt="Repository structure of ARMOR-VOICE-AI" width="100%">
</p>

<details>
<summary>ツリーのテキスト版</summary>

```text
ARMOR-VOICE-AI/
├── src/armor_voice_ai/        コード（標準ライブラリのみ）
│   ├── phrases.py             15 のコマンドの 420 フレーズ、8 言語
│   ├── intent.py              整形と完全一致：閉じた許可リスト
│   ├── confirmation.py        署名付き・一度限り・人ごとの確認トークン
│   ├── silence_policy.py      off / pin / double_turn、音声 PIN、ロック
│   ├── session.py             コマンドごとの 2 ターンのルール
│   ├── gateway.py             stdin/stdout の JSON Lines、監査、返す文
│   ├── service.py             ローカル HTTP サービス（/healthz、/v1/command、/v1/turn）
│   └── turn.py                1 回の音声ターン：エンジン、はい/いいえ、時間の持ち時間
├── tests/                     118 件のテスト：サイレンス、エッジ、ゲートウェイ、ターン、言語、サービス
├── docs/                      SAFETY.md, SERVICE.md, SILENCE_POLICY.md
├── tools/                     共通の CI チェックとプロジェクトのツール
├── images/                    バナーとアイコン
├── .github/                   CI ワークフロー、ダッシュボード通知、Issue と Pull Request のテンプレート
├── armor.project.json         マニフェスト：バージョン、役割、成熟度、ビルドコマンド
├── pyproject.toml             パッケージのメタデータと `armor-voice-gateway` コマンド
├── run.sh run.bat             共通プロジェクトワークフローで起動
├── build.sh build.bat         共通プロジェクトワークフローでビルドとテスト
├── CHANGELOG.md               各バージョンの変更点
└── SECURITY.md SUPPORT.md CONTRIBUTING.md CODE_OF_CONDUCT.md LICENSE
```

</details>""",
     "roadmap": r"""**現時点の既知の制限**

* 音声エンジンは同梱されておらず、実際のマイクでどれも試していません。
* アシスタントを載せる予定のタッチパネルはボード上でまだ動いていません。ウェイクワードはなく、プッシュトゥトークです。
* ターンは*どのパネルか、誰か*が話したかを伝えません。ARMOR-SERVER は渡されたトークンで判断します。これらをリクエストに加えるのは、サーバーとパネルの間のコントラクトの変更です。
* 独立したセキュリティレビューはありません。

**今後**

* CM5 テストベンチで、実際のマイクと実際の音声エンジンを試す。
* タッチパネルがボード上で動いたら、それとの音声フローを動かす。
* 任意の認証済み話者または物理的な確認。将来の導入で追加されるかもしれませんが、署名付き確認は、文書化されたリスクレビューなしには取り除きません。""",
   },
 },
 "pt": {
   "tagline": "Intenções de voz offline em oito idiomas, com uma confirmação que quem chama não consegue falsificar",
   "honest": "As regras de intenção, os oito idiomas, a confirmação assinada ligada a quem fala, a política de silenciamento, o serviço local, o ponto de entrada de turnos e a auditoria são reais e estão testados (118 testes), e o servidor consulta o serviço na bancada de testes do CM5. **Nenhum motor de reconhecimento ou de síntese de voz faz parte deste repositório**: o `/v1/turn` executa os comandos que configurar para isso, e nenhum foi ainda experimentado com um microfone real; o painel tátil que deverá acolher o assistente não funcionou numa placa.",
   "glance": [
     [
       "Função",
       "Porta de ligação de voz e intenções offline (família: Core Services, pai: ARMOR-SERVER)",
     ],
     [
       "Tecnologia",
       "Python 3.11+, apenas biblioteca padrão",
     ],
     [
       "Testes",
       "118 (`python -m unittest discover -s tests`)",
     ],
     [
       "Comandos",
       "15 (10 que consultam, 5 que atuam), 420 frases, 8 idiomas",
     ],
     [
       "Escuta em",
       "`127.0.0.1:18090` (apenas loopback), com token",
     ],
     [
       "Funciona em",
       "A bancada de testes do CM5 (como serviço) ou em qualquer computador",
     ],
     [
       "Em hardware real",
       "Funciona como serviço na bancada do CM5, consultado pelo servidor; não se experimentou nenhum microfone nem motor de voz",
     ],
     [
       "Licença",
       "GPL-3.0-or-later",
     ],
   ],
   "status": {
     "software": "As regras de intenção, o serviço local e o ponto de entrada de turnos funcionam como serviço na bancada de testes do CM5, mas nenhum motor de reconhecimento ou de síntese de voz faz parte do repositório: executa os comandos que configurar para isso.",
     "tests": "Passam 118 testes (`python -m unittest discover -s tests`): as regras de intenção, os oito idiomas, a confirmação assinada ligada a quem fala, a política de silenciamento, o serviço local, o ponto de entrada de turnos e a auditoria.",
     "hardware": "Não se experimentou nenhum microfone nem motor de voz, e o painel tátil que deverá acolher o assistente não funcionou numa placa.",
     "security": "A confirmação é assinada e ligada a quem fala, e a auditoria é testada no equipamento anfitrião; não houve revisão independente.",
     "integration": "O servidor consulta o serviço na bancada de testes do CM5; o fluxo de voz com o painel tátil não funcionou.",
     "docs": "Os oito idiomas e o registo de alterações estão atualizados.",
   },
   "docs": [
     "[Segurança da voz](docs/SAFETY.md): o que é compreendido, a confirmação, o turno do painel de parede, o que se regista",
     "[O serviço](docs/SERVICE.md): rotas, códigos de estado e definições",
     "[Silenciar por voz](docs/SILENCE_POLICY.md): o contrato da política e o PIN",
   ],
   "contributing_first": "Antes de um pull request execute `python -I tools/armor_ci_validate.py` e os testes: ambos têm de passar. Consulte [CONTRIBUTING.md](CONTRIBUTING.md) e o [código de conduta](CODE_OF_CONDUCT.md).",
   "languages_extra": "Cada frase que o serviço diz em resposta, cada comando falado, cada sim e não e cada palavra de dígito de um PIN existe nos oito idiomas.",
   "body": {
     "overview": r"""O ARMOR-VOICE-AI é a parte do A.R.M.O.R. que transforma **o que uma pessoa diz num de quinze comandos, ou em nada**. Nunca faz nada por si: decide, e o [ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER) autentica, autoriza e executa o que foi aceite, exatamente como faria com um clique na consola.

O texto que sai de um reconhecedor de voz é *entrada não fiável*. Por isso não é interpretado, não se procuram palavras-chave nele nem é reenviado como comando: é limpo (acentos, pontuação, fórmulas de cortesia) e tem então de ser **exatamente** uma de 420 frases conhecidas. Qualquer outra coisa, qualquer texto demasiado longo e qualquer frase que pudesse significar dois comandos *não é compreendida*.

**O que faz**

* Compreende quinze comandos em **oito idiomas** (inglês, espanhol, alemão, francês, italiano, japonês, chinês e português).
* Faz com que `arm` e `disarm` precisem de um **segundo turno com um token que o serviço assinou**, ligado à intenção e a quem a pediu.
* Pode fazer com que `silence` precise de um **PIN** falado ou de um segundo turno de confirmação, quando o ARMOR-SERVER o pede.
* Funciona como **serviço HTTP local** e como **porta de ligação de linhas JSON** para adaptadores e testes.
* Recebe o **áudio de um turno** do painel de parede, executa os motores de voz que configurar e responde em texto e, com um sintetizador, em áudio.
* Regista **decisões, nunca áudio nem palavras**: um SHA-256 da transcrição.

**O que não faz**

* Não reconhece nem sintetiza voz: são programas que a instalação escolhe.
* Não arma, não desarma nem silencia nada: um comando aceite é uma recomendação para o ARMOR-SERVER.
* Não desarma de todo a partir do painel de parede: o PIN digita-se no ecrã, nunca se diz em voz alta.""",
     "role": r"""O [ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER) consulta este serviço e depois autentica e autoriza o comando como faria com um clique no [ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO). Destina-se a viver atrás do microfone do painel de parede [ARMOR-NODE-HMI](https://github.com/JuanenRac/ARMOR-NODE-HMI) (premir para falar) e responde ao assistente escrito e falado do [ARMOR-ANDROID-CONTROL](https://github.com/JuanenRac/ARMOR-ANDROID-CONTROL). Na bancada de testes é instalado pelo [ARMOR-DEVOPS](https://github.com/JuanenRac/ARMOR-DEVOPS) (`scripts/install_cm5.sh --with-voice`).

| Fala com | Como | Para quê |
|---|---|---|
| ARMOR-SERVER | entram `POST /v1/command` e `POST /v1/turn`; sai `/api/v1/voice/command` | Decidir uma frase; passar as palavras de um turno falado à rota de voz do servidor |
| ARMOR-NODE-HMI | áudio de um turno (PCM mono a 16 kHz) | O microfone e o altifalante do painel de parede |
| ARMOR-ANDROID-CONTROL | através do servidor | O assistente escrito e falado |
| Motores de voz | entrada e saída padrão | Ouvir (p. ex. whisper.cpp, Vosk) e falar (p. ex. Piper); escolhidos pela instalação |""",
     "architecture": r"""<p align="center">
  <img src="images/architecture.svg" alt="ARMOR-VOICE-AI architecture: callers, ARMOR-SERVER, the voice service with its modules, and the speech engines chosen by the installation" width="100%">
</p>

**Um turno falado que arma o sistema** (ao painel pergunta-se duas vezes, e desarmar é recusado):

<p align="center">
  <img src="images/turn-sequence.svg" alt="A spoken turn that arms the system: the wall panel, ARMOR-VOICE-AI, ARMOR-SERVER and the speech engines, in eleven numbered messages over two turns" width="100%">
</p>

<details>
<summary>Versão em texto do diagrama (Mermaid)</summary>

```mermaid
sequenceDiagram
    autonumber
    participant P as Wall panel
    participant V as ARMOR-VOICE-AI
    participant E as Speech engines
    participant S as ARMOR-SERVER
    P->>V: POST /v1/turn (audio, language)
    V->>E: STT: WAV on stdin
    E-->>V: "arm the system"
    V->>S: /api/v1/voice/command {text, language}
    S-->>V: confirmation-needed + token
    V->>E: TTS: "Please confirm"
    V-->>P: heard, reply, audio
    P->>V: POST /v1/turn ("yes")
    V->>S: /api/v1/voice/command {text, confirmation}
    S-->>V: accepted
    V-->>P: "Command accepted"
    Note over V,S: "disarm" is refused here: it needs a PIN, typed on the screen
```

</details>

**Porque é construído assim**

* **Porquê uma lista fechada e não classificação de intenções.** Um reconhecedor engana-se e qualquer pessoa pode falar perto de um microfone. Com 420 frases exatas, o pior que uma transcrição errada pode fazer é ser ignorada, e um teste verifica que nenhuma frase pertence a dois comandos.
* **Porquê o serviço apenas decide.** A autenticação, a autorização, o registo de auditoria e a ação ficam num único sítio, o ARMOR-SERVER; uma falha aqui pode aceitar mal uma frase, mas não consegue tocar num alarme.
* **Porquê a confirmação é um token assinado emitido pelo serviço.** Uma marca que quem chama define (`confirmed: true`) não prova nada, pelo que é recusada. O token é assinado com HMAC-SHA-256, ligado ao comando e à pessoa, válido durante 30 segundos e utilizável uma só vez.
* **Porquê os motores de voz são programas separados.** Os modelos mudam mais depressa do que uma porta de ligação de segurança deve mudar. Executam-se sem shell, com um ambiente reduzido e um limite de tempo, e os segredos do próprio serviço nunca lhes chegam.
* **Porquê não se guarda nada.** O registo mostra o que foi decidido sem guardar o que foi dito.""",
     "features": r"""### Os quinze comandos

| Comando | Tipo | Significado | Confirmação |
|---|---|---|---|
| `status` | consulta | O estado do sistema | não |
| `alarms` | consulta | Os alarmes que estão ativos | não |
| `nodes` | consulta | O estado dos nós | não |
| `cameras` | consulta | O estado das câmaras | não |
| `radar` | consulta | O estado dos radares | não |
| `solar` | consulta | O estado do sistema solar | não |
| `electrical` | consulta | O consumo elétrico | não |
| `network` | consulta | O estado da rede | não |
| `time` | consulta | A hora | não |
| `help` | consulta | O que se pode dizer | não |
| `silence` | atua | Silenciar (reconhecer) os alarmes | só se a política do servidor o pedir (ver abaixo) |
| `lights_on` | atua | Ligar as luzes | não |
| `lights_off` | atua | Desligar as luzes | não |
| `arm` | atua | Armar o perímetro | **sim** |
| `disarm` | atua | Desarmar o perímetro | **sim** |

Os dez que *consultam* não alteram nada. Os cinco que *atuam* são executados pelo ARMOR-SERVER com a sessão da pessoa que falou, nunca por este serviço.

### Oito idiomas

Inglês, espanhol, alemão, francês, italiano, japonês, chinês e português europeu: as frases (420 no total), o sim e o não de uma confirmação, as palavras dos dígitos de um PIN falado e cada frase que o serviço diz em resposta. As frases escrevem-se como uma pessoa as diz e normalizam-se quando o módulo carrega, com a mesma função que normaliza o que se ouve, para que as duas não se possam afastar. As fórmulas de cortesia (`please`, `por favor`, `bitte`, `s'il vous plaît`, `per favore`...) são descartadas antes de comparar; o japonês e o chinês, escritos sem espaços, listam as suas frases com e sem a terminação cortês.

### A confirmação em dois turnos

1. O primeiro turno de `arm` ou `disarm` devolve **nenhuma aceitação** e um `confirmation_token`.
2. O segundo turno repete esse token para a mesma intenção, **da mesma pessoa**, em 30 segundos.
3. O token é assinado com um segredo que quem chama não tem, pelo que não pode ser falsificado, alterado nem passado para outra intenção ou outra pessoa; funciona uma só vez e os identificadores únicos dos que ainda não expiraram nunca são esquecidos para dar lugar a novos (quando há demasiados em simultâneo, o novo token é recusado).

### Silenciar por voz, com PIN opcional

"Silence" é aceite de imediato, a menos que a instalação peça mais. O ARMOR-SERVER guarda a definição `voice.silence_confirmation` e envia-a como política:

| Modo | O que acontece com "silence" |
|---|---|
| `off` (por omissão, e quando não chega política) | Passa-se de imediato |
| `double_turn` | Não se executa; o serviço pede para dizer sim, e um sim em 15 s vindo do mesmo painel passa o comando original |
| `pin` | Não se executa; o serviço pede o PIN, dito em dígitos ou em palavras de dígitos nos oito idiomas; o PIN certo em 20 s passa o comando |
| política ilegível ou desconhecida | `double_turn`: uma definição estragada nunca desliga uma proteção |

O PIN (de 4 a 12 dígitos, `ARMOR_VOICE_SILENCE_PIN`) é comparado em tempo constante e nunca é registado, guardado nem repetido. Três PIN errados bloqueiam o silenciamento por voz em **todos** os painéis durante cinco minutos; com o modo `pin` pedido e nenhum PIN configurado, nada é silenciado por voz. O contrato completo está em [docs/SILENCE_POLICY.md](docs/SILENCE_POLICY.md).

### O turno do painel de parede

`POST /v1/turn` recebe o áudio de um turno, executa o comando de voz para texto, entrega as palavras à rota de voz do ARMOR-SERVER e responde com o que foi ouvido, o que há a dizer e, quando há um comando de texto para voz configurado, uma gravação da resposta. O painel não tem teclado, pelo que a pergunta de `arm` é recordada por painel durante 30 segundos e o turno seguinte que disser *sim* (no idioma do painel) confirma-a e o que disser *não* cancela-a. Se o servidor responder `disarm`, o turno responde que desarmar precisa do PIN no ecrã. Passados nove segundos de escuta não se consulta o servidor (o painel desiste aos doze), pelo que o que se disse à pessoa e o que a casa fez não se podem contradizer.

### Decisões registadas

Com `--audit-file`, uma linha JSON por decisão: hora, intenção, resultado e o SHA-256 da transcrição. Nunca áudio e nunca as palavras.""",
     "security": r"""| Ameaça | Defesa |
|---|---|
| Uma transcrição errada ou hostil | Entrada não fiável: normalizada, correspondência exata com uma lista fechada, 200 carateres no máximo, o ambíguo *não é compreendido*; nunca é reenviada como comando de shell ou de dispositivo |
| Quem chama alega uma confirmação | `confirmed` é recusado; só conta um token que o serviço assinou |
| Um token é roubado, repetido ou reutilizado | Assinado com HMAC-SHA-256, ligado à intenção e à pessoa, 30 s, uso único; um token não pode viver mais do que a sua emissão, mesmo que o relógio recue |
| Outra pessoa usa o token de alguém | `wrong-subject` |
| Adivinhar o PIN de silenciamento | Comparação em tempo constante, 3 tentativas e depois 5 minutos de bloqueio em todos os painéis, falha em segurança sem PIN |
| Alguém na rede alcança o serviço | Apenas loopback (recusa outro endereço sem `--allow-remote`); token de pelo menos 16 carateres comparado em tempo constante; 2 KB por pedido; uma ligação que bloqueia é fechada ao fim de 15 s |
| Um motor de voz divulga ou abusa de segredos | Executado sem shell, com ambiente reduzido (`PATH`, `HOME`, `LANG`, `TMPDIR`, `ARMOR_VOICE_ENGINE_*`), limite de tempo e de tamanho; os tokens do serviço e do servidor nunca lhe chegam |
| Esgotar a máquina | No máximo dois turnos em simultâneo (um terceiro recebe 503); áudio limitado a 480 000 bytes |
| Os registos revelam o que foi dito | Nunca se regista; a auditoria só tem um hash |
| Um turno antigo atua tarde | Passados nove segundos não se executa nada (504) |

Desarmar por voz **nunca** se faz a partir do painel de parede. A partir da app segue o `ARMOR_DISARM_PIN` do servidor (defina-o como `required`). Nada disto é uma função de segurança: um comando aceite é uma recomendação que o ARMOR-SERVER ainda autentica e autoriza. Leia [docs/SAFETY.md](docs/SAFETY.md) para as regras completas e [SECURITY.md](SECURITY.md) para comunicar uma vulnerabilidade.""",
     "interfaces": r"""### Serviço HTTP

| Rota | Autenticação | O que faz |
|---|---|---|
| `GET /healthz` | nenhuma | `{"ok": true, "service": "armor-voice"}` |
| `POST /v1/command` | cabeçalho `X-Armor-Voice-Token` | Corpo `{text, language?, confirmation?, subject?, policy?, pin?}` (2 KB no máximo). Responde o que foi compreendido, um `confirmation_token` quando é preciso um segundo turno e `speech` no idioma pedido |
| `POST /v1/turn` | o mesmo cabeçalho | Corpo: PCM bruto mono de 16 bits a 16 kHz, `Content-Type: audio/L16;rate=16000`, até 480 000 bytes; cabeçalhos `X-Armor-Language`, `X-Armor-Client`, `X-Armor-Policy`. Responde `{heard, reply, audio?}` |
| `POST /v1/speak` | o mesmo cabeçalho | Corpo `{text, language}` (no máximo 300 carateres). Responde `{audio}`, a frase dita pelo programa de texto para voz como base64 de PCM mono de 16 bits a 16 kHz (não faz nada acontecer e não guarda nada); 501 sem esse programa |

Uma troca real (o token está abreviado):

```json
{"text": "arm the system", "subject": "u-1"}
{"accepted": false, "requires_confirmation": true, "intent": "arm", "outcome": "confirmation-needed", "confirmation_token": "eyJpIjoiYXJt...", "reason": "say it again with the confirmation within 30 s", "speech": "Please confirm"}

{"text": "arm the system", "subject": "u-1", "confirmation": "eyJpIjoiYXJt..."}
{"accepted": true, "requires_confirmation": false, "intent": "arm", "outcome": "accepted", "speech": "Command accepted"}

{"text": "open the garage"}
{"accepted": false, "requires_confirmation": false, "intent": null, "outcome": "not-understood", "reason": "the phrase is not one of the known commands", "speech": "Command not recognised"}
```

Resultados: `accepted`, `confirmation-needed`, `confirmation-refused`, `pin-needed`, `pin-refused`, `not-understood`. Uma confirmação é recusada como `invalid`, `expired`, `wrong-intent`, `wrong-subject` ou `replayed`.

### Códigos de estado de `/v1/turn`

| Código | Erro | Significado |
|---|---|---|
| 200 | | `{heard, reply, audio?}` |
| 401 | `unauthorized` | Falta o token ou está errado |
| 411 / 413 | `bad audio length` | Sem comprimento, ou mais de 480 000 bytes |
| 415 | | Não é `audio/L16;rate=16000` |
| 422 | `invalid language` | Não é um de `en es de fr it ja zh pt` |
| 501 | `stt_unavailable` / `server_not_configured` | Não há comando de voz para texto, ou não há endereço do servidor |
| 502 | `engine_failed` / `server_<code>` / `server_not_answering` | Falhou um motor de voz ou o servidor |
| 503 | `busy` | Já estão a decorrer dois turnos |
| 504 | `turn_too_slow` | O motor de voz demorou tanto que o servidor não foi consultado; não se executou nada |

### Porta de ligação de linhas JSON

`python -m armor_voice_ai.gateway` lê um objeto JSON por linha na entrada padrão e escreve a resposta na saída padrão (2 KB por linha; uma linha com bytes que não são UTF-8 é uma linha como outra qualquer). É a mesma porta de ligação fechada, para adaptadores de voz e testes.

### Contrato com o ARMOR-SERVER

* O servidor envia a política de silenciamento em cada pedido: `policy` no corpo de `/v1/command` (e `pin` para o modo `pin`), o cabeçalho `X-Armor-Policy` (um objeto JSON de 256 bytes no máximo) em `/v1/turn`.
* A rota de voz do servidor recebe as palavras de um turno falado em `/api/v1/voice/command` com o token de operador da instalação, com o nome de cada painel (`X-Armor-Client`).
* Detalhes: [docs/SERVICE.md](docs/SERVICE.md), [docs/SILENCE_POLICY.md](docs/SILENCE_POLICY.md).""",
     "configuration": r"""### Ambiente

| Variável | Necessária | O que define |
|---|---|---|
| `ARMOR_VOICE_TOKEN` | sim (16+ carateres) | O token que os clientes enviam em `X-Armor-Voice-Token` (ou uma linha `ARMOR_VOICE_TOKEN=...` no ficheiro de `--token-file`) |
| `ARMOR_VOICE_CONFIRM_SECRET` | recomendada (16+ bytes) | Assina as confirmações. Sem ela usa-se um segredo aleatório e as confirmações pendentes perdem-se quando o processo pára |
| `ARMOR_VOICE_STT_COMMAND` | para `/v1/turn` | O programa de voz para texto: áudio (WAV) na entrada padrão, as palavras na saída padrão |
| `ARMOR_VOICE_TTS_COMMAND` | opcional | O programa de texto para voz: texto na entrada padrão, um WAV mono de 16 bits a 16 kHz na saída padrão |
| `ARMOR_VOICE_SERVER_URL`, `ARMOR_VOICE_SERVER_TOKEN` | para `/v1/turn` | O ARMOR-SERVER e o token de operador da sua rota de voz |
| `ARMOR_VOICE_SILENCE_PIN` | para o modo `pin` | De 4 a 12 dígitos. Um valor inválido pára o serviço no arranque sem o imprimir |
| `ARMOR_VOICE_ENGINE_*` | opcional | Passadas aos motores de voz (juntamente com `ARMOR_VOICE_LANGUAGE`, definida em cada turno) |

### Linha de comandos

| Opção | Por omissão | |
|---|---|---|
| `--host` | `127.0.0.1` | Endereço em que escutar; qualquer um que não seja loopback é recusado sem `--allow-remote` |
| `--port` | `18090` | |
| `--token-file` | | Ficheiro com uma linha `ARMOR_VOICE_TOKEN=...` |
| `--audit-file` | | Acrescenta uma linha por decisão |
| `--allow-remote` | desativada | Escuta num endereço que não é loopback (não recomendado; só atrás de TLS) |

### Limites que estão no código

| Limite | Valor |
|---|---|
| Validade da confirmação | 30 s |
| Pergunta falada recordada por painel | 30 s |
| "Sim" após uma pergunta de silenciamento / PIN após o pedir | 15 s / 20 s |
| Tentativas de PIN antes do bloqueio / duração do bloqueio | 3 / 5 min |
| Orçamento do turno / o painel desiste | 9 s / 12 s |
| Limite de tempo de um motor de voz | 25 s |
| Áudio máximo / áudio de resposta máximo | 480 000 bytes / 190 000 bytes |
| Corpo do pedido (`/v1/command`) | 2 KB |
| Comprimento da transcrição | 200 carateres |
| Turnos em simultâneo | 2 |

O serviço nunca escreve o que foi dito num registo, sejam quais forem as definições.""",
     "quickstart": "**Requisitos:** Python 3.11+ (apenas biblioteca padrão). Opcional: um programa de voz para texto e outro de texto para voz para `/v1/turn`.\n\n```powershell\n$env:PYTHONPATH = \"src\"\n\n# 1. os testes\npython -m unittest discover -s tests                      # 118 testes\n\n# 2. a porta de ligação, um objeto JSON por linha\necho '{\"text\":\"arm the system\"}' | python -m armor_voice_ai.gateway\n\n# 3. o serviço HTTP local (apenas loopback)\n$env:ARMOR_VOICE_TOKEN = \"a-token-of-at-least-16-characters\"\npython -m armor_voice_ai.service --port 18090\n```\n\n```sh\ncurl -s http://127.0.0.1:18090/v1/command \\\n  -H \"X-Armor-Voice-Token: $ARMOR_VOICE_TOKEN\" \\\n  -d '{\"text\":\"status\",\"language\":\"de\"}'\n# {\"accepted\":true,\"requires_confirmation\":false,\"intent\":\"status\",\"outcome\":\"accepted\",\"speech\":\"Befehl akzeptiert\"}\n```\n\nPara ouvir e falar (`/v1/turn`), aponte o serviço para os seus motores e para o servidor:\n\n```sh\nexport ARMOR_VOICE_STT_COMMAND=\"/opt/armor/bin/hear\"        # WAV na entrada, palavras na saída\nexport ARMOR_VOICE_TTS_COMMAND=\"/opt/armor/bin/speak\"       # texto na entrada, WAV na saída\nexport ARMOR_VOICE_SERVER_URL=\"https://armor-server.local\"\nexport ARMOR_VOICE_SERVER_TOKEN=\"...\"\npython -m armor_voice_ai.service --token-file /opt/armor/etc/armor.voice.env\n```\n\nO painel de parede é um dispositivo da rede e o serviço escuta apenas em loopback: ou um proxy do servidor reencaminha o turno, ou se usa `--allow-remote` atrás de TLS. O token e o áudio não devem atravessar a rede em claro.\n\n`run.bat` / `run.sh` e `build.bat` / `build.sh` iniciam o fluxo de projeto partilhado do [ARMOR-COMMON](https://github.com/JuanenRac/ARMOR-COMMON) (os repositórios estão lado a lado). Quem usa pip fica com o comando `armor-voice-gateway`.",
     "testing": r"""```powershell
$env:PYTHONPATH = "src"
python -m unittest discover -s tests
python -I tools/armor_ci_validate.py        # manifesto, versão, registo de alterações e paridade do README
```

| Ficheiro de testes | Testes | O que cobre |
|---|---|---|
| `test_silence.py` | 31 | A política de silenciamento, o PIN falado em oito idiomas, o bloqueio |
| `test_edges.py` | 29 | O protocolo de linhas, as definições do serviço, a ligação ao servidor (um substituto em loopback), os limites dos motores |
| `test_gateway.py` | 23 | A porta de ligação, a confirmação, repetições e falsificações |
| `test_turn.py` | 15 | O turno, os motores, o sim e o não falados, o orçamento de tempo |
| `test_languages.py` | 11 | Frases na forma normal, nenhuma frase para dois comandos, cada idioma arma, desarma, consulta e silencia |
| `test_service.py` | 5 | As rotas HTTP |

O GitHub Actions executa a base do A.R.M.O.R. em cada push e pull request: a validação do manifesto, da versão, do registo de alterações e da paridade do README, e depois a compilação e os testes do próprio projeto.""",
     "build": "É Python puro: não há nada para compilar. A versão está em `pyproject.toml`, em `armor.project.json` e no emblema do README (lido do manifesto); cada versão tem a sua entrada em [CHANGELOG.md](CHANGELOG.md). As versões são publicadas no GitHub.",
     "troubleshooting": r"""| Vê | Porque | Faça |
|---|---|---|
| `refusing to listen on a non-loopback address without --allow-remote` | `--host` não é `127.0.0.1`, `::1` nem `localhost` | Mantenha o loopback e deixe o proxy do servidor reencaminhar, ou acrescente `--allow-remote` atrás de TLS |
| `a token of at least 16 characters is needed` | Falta `ARMOR_VOICE_TOKEN` ou é curto | Defina-o, ou use `--token-file` |
| `ARMOR_VOICE_SILENCE_PIN is not valid` | Não são 4 a 12 dígitos ASCII | Corrija o valor (nunca é impresso) |
| `ARMOR_VOICE_CONFIRM_SECRET is not set` (aviso) | Está a usar-se um segredo aleatório | Defina um segredo de 16+ bytes se as confirmações tiverem de sobreviver a um reinício |
| 401 `unauthorized` | Falta `X-Armor-Voice-Token` ou está errado | Envie o token |
| 501 `stt_unavailable` | `ARMOR_VOICE_STT_COMMAND` não está definido | Configure um programa de voz para texto |
| 501 `server_not_configured` | Falta o endereço ou o token do servidor | Defina `ARMOR_VOICE_SERVER_URL` e `ARMOR_VOICE_SERVER_TOKEN` |
| 502 `engine_failed` | O motor falhou, esgotou o tempo ou respondeu demasiado (ou um WAV de texto para voz que não é mono de 16 bits a 16 kHz) | Execute-o à mão com a mesma entrada |
| 504 `turn_too_slow` | O motor de voz demorou mais de nove segundos | Use um modelo mais rápido; não se executou nada |
| "Disarming needs your PIN" | Desarmar nunca se faz por voz a partir do painel | Use o ecrã |
| Um "sim" falado não faz nada | A pergunta não foi recordada (demorou mais de 12 s a fazer-se, passaram mais de 30 s, ou respondeu outro painel) | Diga o comando outra vez |""",
     "structure": r"""<p align="center">
  <img src="images/repository-structure.svg" alt="Repository structure of ARMOR-VOICE-AI" width="100%">
</p>

<details>
<summary>Versão em texto da árvore</summary>

```text
ARMOR-VOICE-AI/
├── src/armor_voice_ai/        o código (apenas biblioteca padrão)
│   ├── phrases.py             as 420 frases dos quinze comandos, em oito idiomas
│   ├── intent.py              normalização e correspondência exata: a lista fechada
│   ├── confirmation.py        tokens de confirmação assinados, de uso único e por pessoa
│   ├── silence_policy.py      off / pin / double_turn, o PIN falado, o bloqueio
│   ├── session.py             a regra de dois turnos de cada comando
│   ├── gateway.py             linhas JSON em stdin/stdout, a auditoria, as frases dadas em resposta
│   ├── service.py             o serviço HTTP local (/healthz, /v1/command, /v1/turn)
│   └── turn.py                um turno falado: motores, sim/não, orçamento de tempo
├── tests/                     118 testes: silêncio, limites, porta de ligação, turno, idiomas, serviço
├── docs/                      SAFETY.md, SERVICE.md, SILENCE_POLICY.md
├── tools/                     as verificações de CI partilhadas e as ferramentas do projeto
├── images/                    faixa e ícone
├── .github/                   fluxo de CI, aviso do painel, modelos de issues e de pull requests
├── armor.project.json         manifesto: versão, função, maturidade, comando de compilação
├── pyproject.toml             metadados do pacote e o comando `armor-voice-gateway`
├── run.sh run.bat             arrancam pelo fluxo de projeto partilhado
├── build.sh build.bat         compilam e testam pelo fluxo de projeto partilhado
├── CHANGELOG.md               o que mudou em cada versão
└── SECURITY.md SUPPORT.md CONTRIBUTING.md CODE_OF_CONDUCT.md LICENSE
```

</details>""",
     "roadmap": r"""**Limites conhecidos hoje**

* Não inclui nenhum motor de voz, e nenhum foi experimentado com um microfone real.
* O painel tátil que deverá acolher o assistente não funcionou numa placa; não há palavra de ativação, é premir para falar.
* O turno não diz *que painel nem que pessoa* falou: o ARMOR-SERVER decide com o token que lhe foi dado. Acrescentá-los ao pedido é uma alteração do contrato entre o servidor e o painel.
* Não há revisão de segurança independente.

**A seguir**

* Experimentar um microfone real e um motor de voz real na bancada de testes do CM5.
* Executar o fluxo de voz com o painel tátil quando este tiver funcionado numa placa.
* Confirmação opcional por interlocutor autenticado ou física. Uma implantação posterior pode acrescentá-la, mas a confirmação assinada não será removida sem uma revisão de riscos documentada.""",
   },
 },
}
