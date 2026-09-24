<p align="center">
  <img src="images/ARMOR_BANNER.svg" alt="Banner de ARMOR-DOCS" width="100%">
</p>

# 📚 ARMOR-DOCS

<p align="center"><a href="README.md">🇺🇸 English</a> | 🇪🇸 <b>Español</b></p>

### 🗺️ Arquitectura canónica, base de seguridad y la verdad sobre lo que está demostrado

---

**Comprobación de honestidad:** este repositorio documenta interfaces y procedimientos que se han validado, y dice sin rodeos lo que no. Lee la [matriz de capacidades](docs/CAPABILITY_MATRIX.md) antes de creer que algo está "hecho": todavía no hay nada verificado en hardware.

## 1. 📖 CONTENIDO

| Documento | Qué responde |
|---|---|
| [Matriz de capacidades](docs/CAPABILITY_MATRIX.md) | Para cada capacidad: ¿simulada, local o verificada en hardware? |
| [Arquitectura](docs/ARCHITECTURE.md) | Redes, fronteras de confianza, tiempo y orden |
| [Base de seguridad](docs/SECURITY_BASELINE.md) | El diseño de VLAN, lo que el código impone y lo que falta |
| [Catálogo de proyectos](docs/PROJECT_CATALOG.md) | Los once repositorios, sus versiones y cómo dependen entre sí |
| [Interfaces](docs/INTERFACES.md) | Quién produce y consume cada interfaz y dónde se confía |
| [Primera vertical](docs/FIRST_VERTICAL_SLICE.md) | Qué demuestra la prueba simulador-consola y qué no |
| [Auditorías](AUDITORIA_MEJORAS_PRIORIZADAS_2026-09-24.md) | Mejoras priorizadas y la auditoría posterior |

## 2. 🎨 MARCA

`tools/make_brand.py` genera el banner y el icono de cada repositorio con el aspecto de la familia (casi negro, cian, ámbar); `--check` comprueba que están al día. Paleta y uso en [brand/](brand/).

## 👤 AUTOR

**JuanenRac (Electro Hobby 3D)** · electrohobby3d@gmail.com

## 📜 LICENCIA

GPL-3.0-or-later - véase [LICENSE](LICENSE).
