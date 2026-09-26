# A.R.M.O.R. - segunda vuelta de mejoras priorizadas

Fecha: 2026-09-24  
Alcance: los once proyectos ARMOR. Esta revision no modifica el codigo ni
declara operativa una camara, radar o sensor que no se haya probado fisicamente.

## Resumen ejecutivo

ARMOR ya tiene una primera vertical util: Studio persiste su configuracion de
interfaz, Server cifra las credenciales de camara en disco, puede descubrir
servicios locales, probar rutas RTSP, retransmitir MJPEG mediante FFmpeg,
capturar imagenes, grabar, listar evidencias y enviar PTZ por ONVIF/Hi3510/PSIA.
El siguiente salto de calidad no es sumar mas menus, sino cerrar sus limites de
seguridad, operacion y persistencia.

## P0 - corregir antes de exponer ARMOR fuera del equipo local

### P0.1 Autorizacion de operador para la API de camaras y multimedia

Actualmente `ARMOR-SERVER` protege telemetria, salud, control y WebSocket con
tokens, pero las rutas de configurar/descubrir camaras, PTZ, MJPEG, captura,
grabacion y borrado de evidencias no exigen identidad de operador. El proceso
escucha en `127.0.0.1`, lo cual limita la exposicion remota hoy, pero no es una
frontera suficiente si se incorpora un proxy, un tunel o una aplicacion local
no confiable.

Mejora:

1. Crear un rol `operator` independiente de `ingest` y de `control`.
2. Exigirlo en toda ruta que configure, mueva, capture, grabe o borre.
3. Mantener `/healthz` sin secreto; decidir expresamente si `status` puede ser
   publico local o tambien requiere operador.
4. No poner el secreto en URL, almacenamiento local ni exportacion del sitio.
   Para Studio local, usar una sesion de corta duracion emitida por el launcher
   o una autenticacion de bucle local bien definida.
5. Añadir una prueba negativa por familia de ruta, no una bateria interminable.

### P0.2 Limites de red para ONVIF, RTSP y descubrimiento

La respuesta ONVIF de una camara puede anunciar direcciones `XAddr`. Antes de
usar una direccion devuelta por el dispositivo, Server debe validar que sigue
siendo la camara configurada o una direccion incluida en una lista permitida.
De lo contrario una camara comprometida puede intentar redirigir peticiones del
servidor a otro destino interno. El descubrimiento tambien debe ser una accion
de operador y mostrar claramente el /24 que se va a sondear.

Mejora:

- Rechazar redirecciones HTTP y `XAddr` que cambien de host, puerto o esquema
  sin aprobacion explicita.
- Aceptar solo IP privadas/hosts permitidos configurados para cada camara.
- Limitar un descubrimiento concurrente por servidor, permitir cancelarlo y
  guardar solamente candidatos, nunca credenciales.

### P0.3 Clave de cifrado persistente separada del token de control

Las credenciales de camara se cifran correctamente con AES-GCM, pero la clave
se deriva de `ARMOR_CONTROL_TOKEN`. Si se rota ese token, las credenciales
almacenadas dejan de poder descifrarse. La rotacion de un secreto de control no
debe destruir la configuracion de camaras.

Mejora:

- Usar `ARMOR_CAMERA_CONFIG_KEY` como secreto separado y documentar su copia de
  seguridad/rotacion controlada, o proteger una clave aleatoria persistida con
  el almacen de secretos del sistema operativo.
- Versionar el sobre cifrado para poder migrarlo sin leer contrasenas en claro.

## P1 - fiabilidad real de monitorizacion y evidencia

### P1.1 Modelo de camara en servidor, no solo en Studio

El interruptor `enabled` vive actualmente en el estado de Studio. Al recargar,
la configuracion del Server puede reintroducir una camara y no existe una ruta
para eliminarla definitivamente del servidor. Esto produce una diferencia entre
lo que el operador ve como apagado/eliminado y lo que sigue configurado.

Mejora:

- Anadir `enabled`, posicion 2D/3D y metadatos no secretos a un documento de
  configuracion del sitio versionado en Server.
- Crear `DELETE /api/v1/cameras/:id`, bloquear la eliminacion si hay una
  grabacion activa o detenerla de forma limpia primero.
- Hacer que Studio sincronice, confirme y muestre errores de guardado, en vez de
  asumir que la persistencia local equivale a persistencia del sistema.

### P1.2 Gestor compartido de retransmision y presupuesto de FFmpeg

Cada visor MJPEG abre un proceso FFmpeg. Una cuadricula de ocho vistas puede
crear ocho procesos y varias pestañas pueden repetirlos. Es correcto para una
prueba inicial, pero no para el objetivo Jetson/television tactil.

Mejora:

- Crear un relay por camara reutilizable, con contador de suscriptores y cierre
  retardado al quedar sin observadores.
- Fijar limite global de transcodificaciones, resolucion/fps por perfil y estado
  `degradado` cuando se alcance el presupuesto.
- Incluir un watchdog de FFmpeg que cierre respuestas colgadas y no exponga el
  RTSP ni las credenciales en errores o logs.

### P1.3 Biblioteca de evidencias con retencion y espacio seguro

Las capturas y grabaciones se almacenan correctamente bajo directorios validados
y se filtran nombres de archivo. Falta una politica de capacidad: con camaras
reales el disco puede agotarse y la exploracion sincrona de muchos ficheros puede
bloquear el proceso Node.

Mejora:

- Definir cuota total, cuota por camara, antiguedad maxima y comportamiento al
  alcanzar el limite (no borrar evidencia protegida sin confirmacion).
- Mover inventario a un indice ligero o recorrido asincorno paginado.
- Asociar cada fichero a origen, periodo, integridad/hash y motivo de captura.

## P2 - compatibilidad de camaras y experiencia de operador

### P2.1 Adaptadores de camara declarativos

ONVIF, Hi3510 y PSIA estan bien planteados como caminos distintos, pero el
orden de prueba y los requisitos de cada camara estan mezclados en Server.

Mejora:

- Crear una ficha de capacidad: `stream`, `snapshot`, `ptz`, `audio`,
  `protocol`, `perfil ONVIF`, `autenticacion`, `latencia estimada`.
- Tras guardar una camara, ejecutar una comprobacion no destructiva y mostrar
  que capacidades funcionaron realmente; no marcar PTZ disponible solo por
  tener credenciales.
- Completar Digest RTSP/HTTP moderno (qop, nc, cnonce, stale) o delegarlo en
  una biblioteca mantenida. La implementacion minima actual no funcionara con
  todas las camaras.

### P2.2 Studio: estado operacional, no iconos optimistas

Mejora:

- Mostrar por camara `conectando`, `en directo`, `sin credenciales`, `RTSP no
  encontrado`, `FFmpeg no disponible`, `grabando`, `almacenamiento lleno` y
  ultimo error con hora.
- Mantener navegacion de camara maximizada, PTZ y Record, pero desactivar cada
  accion por capacidad confirmada por Server.
- En Site Designer, distinguir elementos decorativos de equipos ya registrados
  en Server y permitir importar/exportar un esquema con numero de version.

### P2.3 Siete idiomas coherentes con el ecosistema

Studio expone actualmente `en`, `es`, `de`, `fr`, `it`, `pt` y `ja`. El
conjunto de idiomas previsto usa ingles, espanol, aleman, frances, italiano, japones y
chino. Por tanto, falta chino y se incluyo portugues en su lugar. Ademas, varias
adiciones japonesas de Record/video recurren a ingles.

Mejora:

- Sustituir `pt` por `zh`/`zho` si ARMOR adopta el mismo compromiso de siete
  idiomas, y completar las cadenas japonesas que aun hacen fallback.
- Automatizar una comprobacion de claves: cada locale debe cubrir exactamente
  las claves inglesas, sin mostrar la clave tecnica al operador.

## P3 - madurez de los once proyectos

| Proyecto | Mejora realista de siguiente nivel |
| --- | --- |
| ARMOR-COMMON | Convertir los contratos Python/OpenAPI en artefactos generados desde una unica fuente. |
| ARMOR-SERVER | Aplicar P0/P1 y publicar API versionada para Studio y Android. |
| ARMOR-STUDIO | Sincronizar configuracion/estado con Server y cerrar idiomas/capacidades. |
| ARMOR-ANDROID-CONTROL | Pasar de scaffolding a cliente de solo observacion autenticado con alertas y reproduccion de evidencia. |
| ARMOR-RADAR | Pasar de scaffolding a adaptador LD2450 simulado con contrato de tracks, calidad y coordenadas. |
| ARMOR-SERVER-AI | Trabajar solo sobre eventos autorizados; devolver recomendaciones explicables, nunca movimiento directo. |
| ARMOR-VOICE-AI | Requerir confirmacion para armar, PTZ o borrar evidencia y guardar la decision, no audio completo por defecto. |
| ARMOR-SIMULATOR | Generar fallos repetibles de camara/radar/red para probar los estados de Studio. |
| ARMOR-DEVOPS | Añadir servicio de secretos, volumen de evidencia, cuota y proxy local documentado; no publicar puertos sin P0. |
| ARMOR-HARDWARE | Fijar matriz de camaras, radar, alimentacion y red con criterios de aceptacion de banco. |
| ARMOR-DOCS | Mantener una matriz funcional que diga que capacidades son simuladas, locales o comprobadas fisicamente. |

## Orden de ejecucion recomendado

1. P0.1, P0.2 y P0.3: cierran las fronteras antes de aumentar conectividad.
2. P1.1: eliminar/activar/desactivar camaras de manera persistente y unica.
3. P1.2 y P1.3: evitar saturacion de CPU/disco al pasar de demo a varias
   camaras reales.
4. P2.1/P2.2/P2.3: convertir la interfaz en un operador fiable y coherente.
5. Llevar Android, Radar, Simulator y AI desde sus contratos a una vertical
   simulada antes de conectar hardware de seguridad.
