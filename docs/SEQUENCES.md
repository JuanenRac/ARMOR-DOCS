# Sequence diagrams of the critical flows

The four flows where a mistake costs the most, drawn from the contracts and checked against them: every route and every topic named below must exist in the OpenAPI file and the AsyncAPI document of ARMOR-COMMON (`python tools/check_sequences.py`, which the nightly family run executes). A route or topic that is renamed in the contracts makes the check fail until this page is updated.

## Arming and disarming with a PIN

The PIN of a disarm or a silence is checked by the server and never sent to the node; the node's own answer, not the 202, says whether the panel changed.

```mermaid
sequenceDiagram
  participant U as Person in Studio or app
  participant S as ARMOR-SERVER
  participant B as MQTT broker
  participant A as Alarm node
  U->>S: POST /api/v1/alarm/command with action and PIN
  S->>S: check the PIN and the lockout
  S->>B: armor/alarm/{node_id}/command without the PIN
  B->>A: command
  A->>B: armor/alarm/{node_id}/result
  A->>B: armor/alarm/{node_id}/state
  B->>S: result and state
  S->>U: GET /api/v1/alarm/state shows the real phase
```

## A signed firmware update

The image is uploaded, the update job runs one node at a time, and the node accepts only an image signed by the key it trusts.

```mermaid
sequenceDiagram
  participant U as Administrator
  participant S as ARMOR-SERVER
  participant N as Field node
  U->>S: POST /api/v1/admin/firmware/uploads with the image
  U->>S: POST /api/v1/admin/firmware/jobs with kind and login
  S->>N: the image through the node's own panel
  N->>N: verify the signature and boot the new slot
  N->>S: armor/health/{node_id} online with the new version
  S->>U: GET /api/v1/admin/firmware/jobs/{id} reports the result
```

## Closing a switch in two steps

Closing is two commands: arm, then close once the node accepted the arm. The one-time token of the node stays on the server.

```mermaid
sequenceDiagram
  participant U as Administrator
  participant S as ARMOR-SERVER
  participant E as Electrical node
  U->>S: POST /api/v1/electrical/switch with action arm
  S->>E: armor/electrical/{node_id}/command arm
  E->>S: armor/electrical/{node_id}/result accepted with a one-time token
  U->>S: POST /api/v1/electrical/switch with action close_a
  S->>E: armor/electrical/{node_id}/command close_a with the token
  E->>S: armor/electrical/{node_id}/state shows the contacts
```

## Adding a node

The node is adopted in one step: the server makes its broker account and writes the broker address and that account into the node's own panel. The login used for that is used once and never kept.

```mermaid
sequenceDiagram
  participant U as Administrator
  participant S as ARMOR-SERVER
  participant N as Field node
  participant B as MQTT broker
  U->>N: scan the QR code armor-provision
  U->>S: POST /api/v1/admin/nodes/provision with the node address
  S->>N: broker and account written to the panel
  N->>B: connects with its own account
  N->>B: armor/node/{node_id}/info
  B->>S: the node appears in GET /api/v1/nodes/{id}
```
