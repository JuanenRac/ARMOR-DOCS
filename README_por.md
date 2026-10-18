<p align="center">
  <img src="images/ARMOR_BANNER.svg" alt="ARMOR-DOCS banner" width="100%">
</p>

# 📚 ARMOR-DOCS

<p align="center">
  <a href="README.md">🇺🇸 English</a> |
  <a href="README_spa.md">🇪🇸 Español</a> |
  <a href="README_fra.md">🇫🇷 Français</a> |
  <a href="README_ita.md">🇮🇹 Italiano</a> |
  <a href="README_deu.md">🇩🇪 Deutsch</a> |
  <a href="README_zho.md">🇨🇳 简体中文</a> |
  <a href="README_jpn.md">🇯🇵 日本語</a> |
  🇵🇹 <b>Português</b>
</p>

### Arquitetura canónica, linha de base de segurança e a verdade sobre o que está provado

<p align="center">
  <img src="https://img.shields.io/badge/License-GPL%203.0-blue.svg" alt="GPL 3.0">
  <img src="https://img.shields.io/badge/Format-Markdown-083fa1.svg" alt="Format">
  <img src="https://img.shields.io/badge/Languages-8-00E5FF.svg" alt="Languages">
  <img src="https://img.shields.io/badge/Version-0.8.0.1-0f6cbd.svg" alt="Version">
  <img src="https://img.shields.io/badge/Maturity-established-2EA44F.svg" alt="Maturity">
</p>

---

**Verificação de honestidade - o que funciona hoje:** Este repositório documenta interfaces e procedimentos que foram validados, e diz claramente o que não foi. Leia a [matriz de capacidades](docs/CAPABILITY_MATRIX.md) antes de acreditar que uma funcionalidade está "feita": diz de cada uma se foi apenas simulada, testada num computador ou verificada em hardware real. Os README dos dezoito repositórios são escritos a partir de uma única fonte (`tools/readme_src/`) em oito idiomas, com a versão e a maturidade de cada um lidas do seu próprio manifesto, pelo que não podem dizer algo diferente do projeto.

---

## 📋 Num relance

| | |
|---|---|
| Versão | `0.8.0.1` |
| Maturidade | Estabelecido |
| Tecnologia | Markdown / Mermaid |
| Em hardware real | Não se aplica: é documentação; regista o que os outros repositórios correram em hardware real |

## 🎯 Visão geral

<p align="center">
  <img src="images/ARMOR_FAMILY.svg" alt="A.R.M.O.R. family" width="100%">
</p>

* [Matriz de capacidades](docs/CAPABILITY_MATRIX.md): de cada capacidade, está simulada, testada num computador ou verificada em hardware?
* [Arquitetura](docs/ARCHITECTURE.md): redes, limites de confiança, tempo e ordem.
* [Base de segurança](docs/SECURITY_BASELINE.md): o desenho de VLAN, o que o código impõe e o que ainda falta; e o [modelo de ameaças](docs/THREAT_MODEL.md).
* [Catálogo de projetos](docs/PROJECT_CATALOG.md): os dezoito repositórios, as suas versões e como dependem uns dos outros.
* [Interfaces](docs/INTERFACES.md): quem produz e consome cada interface e onde se confia nela.
* [Primeira fatia vertical](docs/FIRST_VERTICAL_SLICE.md): o que o teste do simulador à consola prova e o que não prova.
* **Ferramentas:** `make_readmes.py` escreve o README de cada repositório nos oito idiomas a partir de `readme_src/`, `make_catalog.py` escreve as versões do catálogo, `make_brand.py` o seu banner e ícone, `publication_check.py` procura qualquer coisa privada antes de uma publicação, `clean_history.py` faz uma cópia publicável de um repositório e `sync_ci_tools.py` mantém iguais as verificações de CI da família.

## 🧩 Papel no A.R.M.O.R.

O ARMOR-DOCS é a memória da família: é onde vivem a arquitetura, a base de segurança e a matriz de capacidades, e o sítio que diz, de cada repositório, o que correu mesmo em hardware. Guarda também a ferramenta que escreve os README dos dezoito repositórios a partir de uma só fonte, para que os oito idiomas não se separem.

## 📂 Estrutura do repositório

```text
ARMOR-DOCS/
├── docs/     CAPABILITY_MATRIX, ARCHITECTURE, SECURITY_BASELINE, PROJECT_CATALOG, INTERFACES, THREAT_MODEL, FIRST_VERTICAL_SLICE
├── tools/    make_readmes.py (+ readme_src/: the facts and the words of every repository in eight languages), make_catalog.py, make_brand.py, publication_check.py, clean_history.py, sync_ci_tools.py, check_all.sh
├── brand/    the emblem
└── images/   this repository's banner, icon and the family picture
```

## 🛠️ Ambiente de desenvolvimento

**Requisitos:** Python 3.11+ for the tools

```bash
python tools/make_readmes.py --check      # the READMEs (8 languages) are current
python tools/make_catalog.py --check     # the versions and maturity of the catalogue are current
python tools/make_brand.py --check        # the banners and icons are current
python tools/publication_check.py         # nothing private would leave with a publication
bash tools/check_all.sh                   # every repository's own tests, in one run
```

## 🔗 Projetos relacionados

O **A.R.M.O.R.** (Autonomous Radar & Multimodal Observation Range) é um sistema de segurança perimetral feito de repositórios independentes. Cada um tem a sua própria versão, os seus próprios testes e o seu próprio README; esta é a família:

* **[ARMOR-COMMON](https://github.com/JuanenRac/ARMOR-COMMON)** - Contratos de mensagens, validadores, vetores de conformidade e tipos gerados
* **[ARMOR-RADAR](https://github.com/JuanenRac/ARMOR-RADAR)** - Firmware de nó de campo para ESP32-S3 com três radares e o seu próprio painel web
* **[ARMOR-SOLAR](https://github.com/JuanenRac/ARMOR-SOLAR)** - Protocolos de inversores e baterias solares e as mensagens de um nó de ligação
* **[ARMOR-ELECTRICAL](https://github.com/JuanenRac/ARMOR-ELECTRICAL)** - Nó elétrico: contadores, a mensagem das leituras da rede e as regras de comutação
* **[ARMOR-ALARM](https://github.com/JuanenRac/ARMOR-ALARM)** - Nó e central de alarme: zonas, armar, atrasos, sirene e PIN, com o servidor ou sem ele
* **[ARMOR-HMI](https://github.com/JuanenRac/ARMOR-HMI)** - Painel tátil: o estado do sistema num ecrã de parede, armar e reconhecer, e a casa do assistente de voz
* **[ARMOR-NETWORK](https://github.com/JuanenRac/ARMOR-NETWORK)** - A rede local: os seus dispositivos, a internet e o que muda
* **[ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER)** - Coordenador central: telemetria, alarmes, dispositivos, leituras solares e câmaras
* **[ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO)** - Consola web: câmaras, radar, alarmes, energia solar e o desenhador de local 2D/3D
* **[ARMOR-ANDROID-CONTROL](https://github.com/JuanenRac/ARMOR-ANDROID-CONTROL)** - Cliente Android de operador com um radar 2D/3D em direto
* **[ARMOR-SERVER-AI](https://github.com/JuanenRac/ARMOR-SERVER-AI)** - Política de inferência visual que explica as suas decisões e nunca atua
* **[ARMOR-VISION](https://github.com/JuanenRac/ARMOR-VISION)** - Zonas de câmara, máscaras e regras de deteção para o Jetson Orin NX
* **[ARMOR-VOICE-AI](https://github.com/JuanenRac/ARMOR-VOICE-AI)** - Intenções de voz offline com uma confirmação que não se pode falsificar
* **[ARMOR-HARDWARE](https://github.com/JuanenRac/ARMOR-HARDWARE)** - Caixas, eletrónica e a matriz de aceitação de bancada
* **[ARMOR-DEVOPS](https://github.com/JuanenRac/ARMOR-DEVOPS)** - Implementação, a bancada de testes CM5, cópias de segurança e TLS
* **[ARMOR-SIMULATOR](https://github.com/JuanenRac/ARMOR-SIMULATOR)** - Simulador de telemetria offline com falhas repetíveis
* **[ARMOR-UPDATER](https://github.com/JuanenRac/ARMOR-UPDATER)** - Deteta, instala e atualiza os próprios repositórios do ecossistema
* **ARMOR-DOCS** (este repositório) - Arquitetura, linha de base de segurança e a matriz de capacidades

## 📚 Documentação e comunidade

Onde ler mais:

* [Matriz de capacidades: o que está provado e o que não](docs/CAPABILITY_MATRIX.md)
* [Catálogo de projetos: versões e como os repositórios dependem uns dos outros](docs/PROJECT_CATALOG.md)
* [Registo de alterações deste repositório](CHANGELOG.md)
* [Licença (GPL-3.0-or-later)](LICENSE)
* Perguntas, ideias e relatórios: electrohobby3d@gmail.com

## 👤 AUTOR

**JuanenRac (Electro Hobby 3D)** · electrohobby3d@gmail.com

## 📜 LICENÇA

GPL-3.0-or-later - veja [LICENSE](LICENSE).
