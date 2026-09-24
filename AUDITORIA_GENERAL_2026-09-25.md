# Auditoría general de ARMOR - 2026-09-25

Estado medido: typecheck limpio en SERVER y STUDIO, `npm audit` sin vulnerabilidades en producción, 0 TODO/FIXME
en el código, tests en verde en los 11 repos. Nada verificado en hardware real.

## Hallazgos

| # | Hallazgo | Gravedad | Evidencia |
|---|---|---|---|
| 1 | El estado se pierde al reiniciar: el modo armado/desarmado vuelve a `disarmed` y los nodos desaparecen hasta su siguiente mensaje. Un reinicio del servidor desarma el perímetro sin avisar. | Alta | `ArmorStore` (`src/store.ts`) guarda todo en memoria |
| 2 | No hay historial de eventos: las alertas `review`/`high` solo existen como estado actual, sin registro consultable de cuándo empezaron y terminaron. | Alta | ninguna ruta de eventos; solo el audit log de acciones |
| 3 | No hay salida de alarma: nada avisa (webhook, notificación push, sirena, MQTT de salida) cuando hay una alerta `high`. | Alta | sin código de notificación |
| 4 | Restos de un servidor Python anterior (`http_api.py`, `service.py`, `state.py`) y sus tests siguen dentro de ARMOR-SERVER, junto al servidor real en TypeScript. Dos implementaciones del mismo estado pueden divergir. | Media | `src/*.py`, `tests/test_state.py`, `tests/test_vertical_slice.py` |
| 5 | Sin CI: ningún repo tiene flujo automático que ejecute tests, typecheck y `make_brand --check`/`make_readmes --check`. Solo funciona si se recuerda ejecutarlo a mano. | Media | no existe `.github`; los repos son privados |
| 6 | Sin HTTPS: Studio y la API van en HTTP plano por la LAN, con cookies de sesión y contraseñas de cámara en el formulario. Aceptable en banco de pruebas, no en producción. | Media | `cookieSecure` depende de `ARMOR_COOKIE_SECURE=1` y no hay TLS delante |
| 7 | Sin copia de seguridad ni restauración de `data/` (bóveda de cámaras, evidencias, auditoría). Perder la clave de cámara o el disco pierde las cámaras configuradas. | Media | `install_cm5.sh` no incluye respaldo |
| 8 | La alerta depende solo del recuento de objetivos. No hay zonas, horarios ni tiempo mínimo de permanencia, así que un objetivo de un frame ya cuenta. | Media | `alertLevelFor(mode, targetCount)` |
| 9 | Sin `ffmpeg` en la CM5 no hay vídeo en directo. Pendiente del usuario. | Baja (conocido) | CM5 sin el paquete |
| 10 | Límite global de 240 peticiones por minuto también sobre ingesta: con muchos nodos o reintentos puede rechazar telemetría legítima. Hoy con 3 nodos no ocurre. | Baja | `src/app.ts` |

## Mejoras realistas, por orden

1. **Persistencia del estado (hallazgo 1).** Guardar modo y última observación por nodo en un fichero atómico bajo `data/`, con una marca de "restaurado" hasta que llegue telemetría nueva. Al arrancar tras un reinicio, conservar `armed`. Tamaño: pequeño. Es la mejora de mayor valor.
2. **Historial de eventos (hallazgo 2).** Registro append-only de cambios de nivel de alerta y de estado de nodo (JSON por líneas con rotación, como el audit log), una ruta `GET /api/v1/events` paginada y una vista en Studio. Tamaño: medio.
3. **Salida de alarma (hallazgo 3).** Un único canal para empezar: webhook configurable y publicación MQTT en `armor/server/alert`, con reintentos y sin bloquear la ingesta. Sirena y push van después. Tamaño: medio.
4. **Retirar el servidor Python antiguo (hallazgo 4).** Mover `src/*.py` y sus tests a `SONNET/_papelera`, ajustar la documentación y comprobar que nada los importa. Tamaño: pequeño.
5. **CI local (hallazgo 5).** Un script `tools/check_all.sh` en ARMOR-DOCS que recorre los 11 repos ejecutando tests, typecheck y las comprobaciones de marca y READMEs, con salida de PASS/FAIL. Tamaño: pequeño.
6. **Reglas de alerta (hallazgo 8).** Zonas por sensor, permanencia mínima (por ejemplo 2 s) y ventanas horarias; configuración validada por esquema en ARMOR-COMMON con vectores de conformidad. Tamaño: medio-grande, pero es lo que convierte el sistema en algo útil de verdad.
7. **HTTPS con proxy inverso (hallazgo 6)** y **copia de seguridad de `data/` (hallazgo 7).** Caddy o nginx con certificado propio para la LAN y un script de respaldo cifrado con verificación de restauración. Tamaño: medio.
8. **Límite de peticiones separado para la ingesta (hallazgo 10).** Pequeño.

## Lo que no añadiría todavía

- Reconocimiento facial o de matrículas, y cualquier IA que actúe sin confirmación: fuera del alcance de un perímetro y con riesgos legales.
- Aplicación iOS, o más pantallas en Android, antes de comprobar la actual en un teléfono real.
- Más cámaras o protocolos sin haber demostrado primero el vídeo en directo con las cinco que ya hay.
- Nuevas funciones de firmware antes de tener el documento del LD2450/LD2461 y una placa; sin ellos solo se acumula código sin comprobar.

## Resolución (2026-09-25, misma jornada)

| # | Estado | Cómo |
|---|---|---|
| 1 | Resuelto | `state.json` con escritura atómica; el modo se guarda al instante y se restaura al arrancar; los nodos restaurados quedan como "en silencio" hasta que hablan |
| 2 | Resuelto | `events.log` rotado + `GET /api/v1/history` + vista Historial en Studio |
| 3 | Resuelto | MQTT `armor/server/alert` y webhook firmado con HMAC, con reintentos y auditoría (MQTT sin probar con un broker real) |
| 4 | Resuelto | Python antiguo movido a `SONNET/_papelera/armor-server-python-legacy`; la prueba de extremo a extremo usa el simulador y el servidor reales |
| 5 | Resuelto | `tools/check_all.sh` |
| 6 | Parcial | Perfil `tls` de Compose con Caddy, **sin ejecutar** (no hay Docker en el PC de desarrollo) |
| 7 | Resuelto | `backup_data.sh` / `restore_data.sh` con prueba de ida y vuelta |
| 8 | Resuelto | Tiempo de permanencia (`ARMOR_ALERT_DWELL_MS`, 2 s por defecto) y zonas ignoradas, editables desde Studio |
| 9 | Pendiente | Lo instalará el usuario (`ffmpeg` en la CM5) |
| 10 | Resuelto | Límite de ingesta propio (1200/min) |
