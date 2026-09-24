<p align="center">
  <img src="images/ARMOR_BANNER.svg" alt="ARMOR-DOCS banner" width="100%">
</p>

# 📚 ARMOR-DOCS

<p align="center">🇺🇸 <b>English</b> | <a href="README_spa.md">🇪🇸 Español</a></p>

### 🗺️ Canonical architecture, security baseline and the truth about what is proven

---

**Honesty check:** this repository documents interfaces and procedures that have been
validated, and it says plainly what has not. Read the [capability matrix](docs/CAPABILITY_MATRIX.md)
before believing any feature is "done": nothing is verified on hardware yet.

## 1. 📖 CONTENTS

| Document | What it answers |
|---|---|
| [Capability matrix](docs/CAPABILITY_MATRIX.md) | For each capability: simulated, local or verified on hardware? |
| [Architecture](docs/ARCHITECTURE.md) | Networks, trust boundaries, time and ordering |
| [Security baseline](docs/SECURITY_BASELINE.md) | The VLAN design, what the code enforces and what is still missing |
| [Project catalogue](docs/PROJECT_CATALOG.md) | The eleven repositories, their versions and how they depend on each other |
| [Interfaces](docs/INTERFACES.md) | Who produces and consumes each interface and where it is trusted |
| [First vertical slice](docs/FIRST_VERTICAL_SLICE.md) | What the simulator-to-console test proves and what it does not |
| [Audits](AUDITORIA_MEJORAS_PRIORIZADAS_2026-09-24.md) | Prioritised improvements and the post-improvement audit (in Spanish) |

## 2. 🎨 BRAND

`tools/make_brand.py` generates the banner and icon of every repository in the family look
(near-black, cyan, amber); `--check` verifies they are current. Palette and use in [brand/](brand/).

## 👤 AUTHOR

**JuanenRac (Electro Hobby 3D)** · electrohobby3d@gmail.com

## 📜 LICENSE

GPL-3.0-or-later - see [LICENSE](LICENSE).
