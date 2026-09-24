# First vertical slice

This test proves data compatibility before hardware integration:

1. `ARMOR-SIMULATOR` emits deterministic JSON lines for a chosen scenario, and can inject
   repeatable faults (a silent node, out-of-order or duplicated messages, a flapping node, and
   deliberately invalid messages).
2. `ARMOR-COMMON` validates the topic, identity, numeric fields and track limit, and every
   implementation agrees with it through the shared conformance vectors.
3. `ARMOR-SERVER` stores the last validated observation per node, shows a silent node as stale
   and offline, and refuses what the contract refuses.
4. `ARMOR-STUDIO` renders the server status, and says so when it can only show demonstration data.

```powershell
python -m armor_simulator --count 60 --scenario two-intruders --server-url http://127.0.0.1:8080 --ingest-token <ingest token>
```

It does **not** prove MQTT connectivity, ESP32 UART decoding, camera inference, Jetson
performance, physical alarms or network security. Those are separate, evidence-based
milestones; see the [capability matrix](CAPABILITY_MATRIX.md).
