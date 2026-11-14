# Installing in three levels

The same system is brought up in three steps, and a step is not left until its exit test passes. Each level says what is allowed to be connected and what is checked before the next one. Nothing here turns on a protection that was off by default: the options are changed in Studio, in Security, one at a time.

## Level 1: the bench

* **What:** the server, Studio and the broker on a bench computer or a CM5, with the simulator for what is not there, and one real node at a time on a bench supply with no load, no siren and no mains.
* **Do:** follow the [first vertical slice](FIRST_VERTICAL_SLICE.md); create the first administrator; adopt each node (see *Adding a node* in the [sequences](SEQUENCES.md)); read the capability level of each row in the [capability matrix](CAPABILITY_MATRIX.md).
* **Exit test:** the [bench acceptance](https://github.com/JuanenRac/ARMOR-HARDWARE/blob/main/docs/BENCH_ACCEPTANCE.md) of the hardware repository passes for every device that will go to the pilot house, with a [measurement record](https://github.com/JuanenRac/ARMOR-HARDWARE/blob/main/docs/MEASUREMENT_RECORD.md) filled in for each row.

## Level 2: the pilot house

* **What:** one house, the real network and the real nodes, with the siren disconnected or in test mode, the electrical switching and the commands still off, and the security options on their defaults.
* **Do:** put the nodes in their places; walk every zone with the walk test; check the mobile apps against the server; keep the siren, the load shedding and every command option off.
* **Exit test:** a week without an unexplained alarm or an offline node, the arming and disarming flow of the [sequences](SEQUENCES.md) tried from every client, the backup restored once in a scratch folder, and the [threat model](THREAT_MODEL.md) read against what is exposed.

## Level 3: production

* **What:** the same system with the siren connected and the options the owner chooses switched on one by one (HTTPS required, command signing, public access, load shedding, switching), each with its own exit test.
* **Do:** record the choice and the date of every option you switch on; sign and keep the update key where only you can reach it; follow the [security baseline](SECURITY_BASELINE.md).
* **Exit test:** a silent failure drill: pull the network cable and the power of the server, and check what each node does and what Studio says when it returns.
