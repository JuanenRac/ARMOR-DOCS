# A.R.M.O.R. - auditoria posterior a mejoras

## Verificado en esta pasada

- `ARMOR-SERVER`: `npm run typecheck` correcto; `npm test` correcto (3/3).
- `ARMOR-STUDIO`: `npm run typecheck`, `npm test` (2/2) y `npm run build`
  correctos.
- Studio usa ahora los siete idiomas objetivo: en, es, de, fr, it, ja y zh.
- Las operaciones de camara/evidencia requieren sesion de operador; la sesion
  es HttpOnly y Studio no persiste el token.
- El servidor conserva evidencia al eliminar una conexion de camara, limita
  relays MJPEG por camara/capacidad y aplica retencion configurable.

## Hallazgos que permanecen

1. La cookie de operador se ha validado por compilacion, no por una prueba E2E
   real entre `localhost` y `127.0.0.1`. Antes de desplegar, usar el mismo host
   literal en Studio y Server y comprobar inicio, MJPEG y Record en Chromium.
2. El relay MJPEG comparte proceso por camara, pero aun requiere prueba de carga
   con cuatro u ocho flujos reales para ajustar `ARMOR_MAX_MJPEG_RELAYS`.
3. ONVIF y RTSP Digest se prueban contra rutas comunes; la variedad de firmware
   de camaras exige una matriz de compatibilidad real, especialmente Digest qop.
4. La retencion borra por antiguedad/capacidad. Falta una marca de evidencia
   protegida y una exportacion con hash para una cadena de custodia completa.
5. ARMOR-ANDROID-CONTROL y ARMOR-RADAR siguen en scaffolding: necesitan la
   vertical simulada contra Server antes de afirmar funcion de operador real.

## Siguiente bloque recomendado

Implementar una prueba E2E local con una camara de prueba o Simulator, y luego
llevar el mismo contrato de operador/capacidades a Android y Radar. No exponer
ARMOR fuera del bucle local hasta completar esa prueba y decidir el proxy/TLS.
