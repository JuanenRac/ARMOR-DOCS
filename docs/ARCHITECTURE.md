# A.R.M.O.R. architecture

```mermaid
flowchart LR
  subgraph field["VLAN 10 - field (no internet)"]
    N["ESP32-S3 field nodes<br/>3x radar, lux, climate"]
    SN["Solar nodes<br/>inverters and batteries, read only"]
    EN["Electrical nodes<br/>AC and DC meters, read only"]
    C["IP cameras (PTZ, RTSP)"]
  end
  subgraph core["VLAN 20 - core"]
    B["MQTT broker"]
    S["ARMOR-SERVER"]
    V["Visual AI (Jetson)"]
    P["Voice AI"]
  end
  subgraph clients["VLAN 30 - clients"]
    W["ARMOR-STUDIO"]
    A["ARMOR-ANDROID-CONTROL"]
  end
  N -->|"MQTT, one identity per node"| B
  SN -->|"MQTT, one identity per node"| B
  EN -->|"MQTT, one identity per node"| B
  B --> S
  C -->|"RTSP / ONVIF"| S
  C -->|"RTSP"| V
  V -->|"severity recommendation"| S
  P -->|"confirmed intent"| S
  S -->|"authenticated session"| W
  S -->|"authenticated session"| A
  A -.->|"Bluetooth: set-up only"| N
  A -.->|"Bluetooth: set-up only"| SN
  A -.->|"Bluetooth: set-up only"| EN
```

## Trust boundaries

* **Field nodes** publish observations and health. Each has its own broker identity and can
  write only its own topics; the broker is the boundary, and the server validates every payload
  again against the published contract. A node never receives an instruction it can execute
  without an allow-listed command.
* **The server is the only place that touches a camera.** No client receives a camera password
  or an RTSP address. Clients get JSON, MJPEG and files through an HttpOnly session.
* **The AI services recommend, they never act.** The visual policy returns a severity with
  reasons and `authorizes_action = false`; the voice service returns an intent and needs a
  service-issued confirmation for arm and disarm. The server authenticates and authorises
  every action.
* **Studio and Android are clients of the server**, not of the field network. They never reach
  a node's own configuration endpoint. The one exception is the set-up of a node from the Android
  app over **Bluetooth Low Energy** (below), which needs no network at all.
* **Solar and electrical nodes only read.** They publish what their inverters, batteries and
  meters report; no request that writes to a piece of equipment exists in their firmware, and the
  rules for switching an electrical source are tested but not linked to any hardware.
* **A phone sets a node up over Bluetooth** (name, Wi-Fi, address, broker): the same channel on the
  radar, the solar and the electrical node. The link is encrypted, every operation but `hello`
  needs the set-up code or a login, changing anything needs an administrator, and wrong
  passwords are throttled. The "just works" pairing does not stop someone present while the phone
  pairs; see the [security baseline](SECURITY_BASELINE.md).

## Time and ordering

Every message carries a wall-clock millisecond timestamp (SNTP on the node). The server ignores
a newer-than-received "online" message that is older than the last one it holds, always applies an
"offline" message (an MQTT last will cannot know the time of its own death) and never moves a node's
stored time backwards. A node that stops talking is shown *stale* and *offline* after a
configurable silence.

## Where each concern lives

| Concern | Project |
|---|---|
| What a message means | ARMOR-COMMON (JSON Schemas, conformance vectors, generated types, OpenAPI) |
| Sensing and field firmware | ARMOR-RADAR |
| Solar gateway nodes (inverters, batteries) | ARMOR-SOLAR |
| Electrical nodes (meters) and the rules for switching | ARMOR-ELECTRICAL |
| The local network: devices, internet, changes | ARMOR-NETWORK |
| State, cameras, evidence, audit | ARMOR-SERVER |
| Visual and voice decisions | ARMOR-SERVER-AI, ARMOR-VOICE-AI |
| Operator consoles | ARMOR-STUDIO, ARMOR-ANDROID-CONTROL |
| The touch panel on the wall (state, arming, the voice assistant) | ARMOR-HMI |
| Enclosures and electronics | ARMOR-HARDWARE |
| Deployment | ARMOR-DEVOPS |
| Ecosystem-wide CI baseline and cross-machine install/update | ARMOR-COMMON, ARMOR-UPDATER |
| Offline testing and faults | ARMOR-SIMULATOR |

See the [capability matrix](CAPABILITY_MATRIX.md) for what is simulated, local or verified.
