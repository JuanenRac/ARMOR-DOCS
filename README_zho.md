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
  🇨🇳 <b>简体中文</b> |
  <a href="README_jpn.md">🇯🇵 日本語</a> |
  <a href="README_por.md">🇵🇹 Português</a>
</p>

### 规范的架构、安全基线，以及关于哪些已被证实的真相

<p align="center">
  <img src="https://img.shields.io/badge/License-GPL%203.0--or--later-blue.svg" alt="GPL 3.0 or later">
  <img src="https://img.shields.io/badge/Format-Markdown-083fa1.svg" alt="Format">
  <img src="https://img.shields.io/badge/Languages-8-00E5FF.svg" alt="Languages">
  <img src="https://img.shields.io/badge/Tests-199%20passing-2ea44f.svg" alt="Tests">
  <img src="https://img.shields.io/badge/Version-0.8.1.2-0f6cbd.svg" alt="Version">
  <img src="https://img.shields.io/badge/Maturity-established-2EA44F.svg" alt="Maturity">
</p>

---

**诚实性检查 - 今天真正能运行的部分：** 本仓库记录已验证的接口和流程，并明确说明哪些尚未验证。在相信某项功能“已完成”之前，请先阅读[能力矩阵](docs/CAPABILITY_MATRIX.md)：它对每一项说明它只是模拟过、在计算机上测试过，还是在真实硬件上验证过。十九个仓库的 README 来自同一个来源（`tools/readme_src/`），以八种语言编写，每个项目的版本和成熟度都读自它自己的清单，因此不会与项目说的不一样。

---

## 📋 速览

| | |
|---|---|
| 版本 | `0.8.1.2` |
| 成熟度 | 成熟 |
| 角色 | 文档中心：架构、安全基线、能力矩阵，以及生成 README、目录和横幅图的工具 |
| 技术栈 | Python 3.11+（工具，标准库）、Markdown |
| 测试 | 199 项（`python -m unittest discover -s tests`，约一分钟） |
| 接口 | `make_readmes.py`、`make_catalog.py`、`make_brand.py`、`publication_check.py`、`clean_history.py`、`sync_ci_tools.py`、`check_all.sh` |
| 运行位置 | 装有 Python 的任意计算机；家族的各仓库放在本仓库旁边 |
| 真实硬件 | 不适用：这是文档；它记录其他仓库在真实硬件上运行过的内容 |
| 许可证 | GPL-3.0-or-later |

**跳转到：** [概述](#-概述) · [架构](#-架构) · [安全](#-安全与防护) · [接口](#-接口) · [快速开始](#-快速开始) · [测试](#-测试) · [故障排除](#-故障排除) · [结构](#-仓库结构) · [相关项目](#-相关项目)

## 🚦 项目状态

每一行是本仓库的一个部分，灯号表示它今天做到了哪一步。内容依据仓库能够展示的证据（测试、构建、运行），而不是计划。

🟢 已完成并验证 · 🟡 可用，有已知限制 · 🟠 部分完成或尚未验证 · 🔴 未完成或不可用

| 领域 | 状态 | 在这里的含义 |
|---|---|---|
| 软件 | 🟢 | README、横幅、目录和能力矩阵的生成器，以及复制到每个仓库中的 CI 工具都能运行并经过测试。 |
| 测试 | 🟢 | 这些工具的 199 项测试通过（`python -m unittest discover -s tests`）：发布检查、历史清理器、README、目录和品牌的生成器、CI 工具的副本以及共用流程工具。 |
| 自动检查 | 🟢 | 每次推送都会检查 README、横幅和目录是否为最新，以及注册表中的每个仓库是否都有状态表。 |
| 集成 | 🟢 | 所有仓库的 README 都由同一份源文件生成，每个仓库的版本和成熟度均读取自其自身的清单。 |
| 文档 | 🟢 | 能力矩阵为每项功能说明它只是被模拟、在电脑上测试过，还是在真实硬件上验证过；八种语言和更新日志均为最新。 |

## 🎯 概述

<p align="center">
  <img src="images/ARMOR_FAMILY.svg" alt="A.R.M.O.R. family" width="100%">
</p>

* [能力矩阵](docs/CAPABILITY_MATRIX.md)：每项能力是模拟的、在计算机上测试的，还是在硬件上验证的？
* [架构](docs/ARCHITECTURE.md)：网络、信任边界、时间和顺序。
* [安全基线](docs/SECURITY_BASELINE.md)：VLAN 设计、代码强制实施的内容以及仍然缺少的内容；以及[威胁模型](docs/THREAT_MODEL.md)。
* [项目目录](docs/PROJECT_CATALOG.md)：十九个仓库、它们的版本以及相互依赖关系。
* [接口](docs/INTERFACES.md)：谁产生和使用每个接口，以及在哪里被信任。
* [第一个垂直切片](docs/FIRST_VERTICAL_SLICE.md)：从模拟器到控制台的测试证明了什么、没有证明什么。
* **工具：**`make_readmes.py` 从 `readme_src/` 以八种语言写出每个仓库的 README，`make_catalog.py` 写出目录中的版本，`make_brand.py` 写出其横幅和图标，`publication_check.py` 在发布前查找任何私有内容，`clean_history.py` 制作仓库的可发布副本，`sync_ci_tools.py` 让家族的 CI 检查保持一致。

## 🧩 在 A.R.M.O.R. 中的角色

ARMOR-DOCS 是家族的记忆：架构、安全基线和能力矩阵都在这里，也是说明每个仓库究竟在硬件上运行过什么的地方。它还保存着从同一个来源编写全部十九个仓库 README 的工具，使八种语言不会各行其是。

| 对话对象 | 方式 | 用途 |
|---|---|---|
| 家族的每个仓库 | 其 `armor.project.json` 和 README 文件 | 工具读取版本和成熟度，写出 README、横幅图和 CI 副本 |
| ARMOR-COMMON | `registry/repositories.json` | 家族仓库的唯一清单，由 `registry.py` 读取 |
| 发布者 | `publication_check.py`  `clean_history.py` | 会泄露什么，以及可发布的单提交副本 |

## 🏛️ 架构

<p align="center">
  <img src="images/architecture.svg" alt="ARMOR-DOCS architecture: what the tools read, the tools themselves and what they write in every repository" width="100%">
</p>

## 🔒 安全与防护

| 威胁 | 防御 |
|---|---|
| 发布私有内容 | `publication_check.py` 只读 git（已跟踪文件与历史，从不读被忽略的文件），且从不打印密钥。BLOCK：私钥、公网 IP 地址、个人邮箱、被跟踪的 `secrets/` 或 `.env`、带共同作者或 AI 尾注的提交、作者不是项目作者的提交；REVIEW：看起来像明文密码或令牌的行；出现任何 BLOCK 时退出码为 1 |
| 带残留物的历史 | `clean_history.py` 生成仓库的可发布副本，只有项目作者提交的一个提交 |
| 声称超过已证实的内容 | `docs/CAPABILITY_MATRIX.md` 分三级（Simulated、Local、Verified），另有 None、Absent 和 Local-not-activated；只有 Verified 行接触过硬件（日常使用的 CM5 测试台） |
| README 与项目说法不一致 | 每个 README 的版本和成熟度都从其自己的清单读取；每次推送都会检查 README、横幅图和目录是否最新，以及注册表中的每个仓库是否都有状态表 |

家族的安全文档是 [docs/SECURITY_BASELINE.md](docs/SECURITY_BASELINE.md)（VLAN 设计、代码强制执行的内容和仍缺少的部分）和 [docs/THREAT_MODEL.md](docs/THREAT_MODEL.md)。这里的任何内容都不能证明不存在密钥。

## 🔌 接口

| 路由 | 认证 | 作用 |
|---|---|---|
| `python tools/make_readmes.py [--check]` | - | 从 `tools/readme_src/` 写出每个仓库八种语言的 README；`--check` 在有过期时失败。它会重写所有文件：改源文件，不要改 README |
| `python tools/make_catalog.py [--check]`  `make_brand.py [--check]` | - | `docs/PROJECT_CATALOG.md` 的版本与成熟度，以及横幅图和图标 |
| `python tools/publication_check.py [REPO] [--no-history] [--ref=BRANCH]` | - | 如果公开这些仓库会泄露什么；出现 BLOCK 时退出码为 1 |
| `python tools/clean_history.py` | - | 只有一个提交的可发布仓库副本 |
| `python tools/sync_ci_tools.py [--check]` | - | 把共用的 CI 检查和启动器复制到每个仓库；副本偏离时 `--check` 失败 |
| `bash tools/check_all.sh [--android] [--compose]` | - | 一次运行每个仓库的测试；缺少工具的检查记为 SKIP，绝不是 PASS |

每个 README 的源文件是 `tools/readme_src/repos/<仓库>.py`（与语言无关的事实和八种语言的文字），README 周围的文字在 `ui.py`，截图在 `shots.py`。`tools/registry.py` 读取 ARMOR-COMMON 的仓库清单。另见 [docs/INTERFACES.md](docs/INTERFACES.md) 和 [docs/SETUP_CODE.md](docs/SETUP_CODE.md)。

## 🚀 快速开始

**要求：** 工具需要 Python 3.11+（仅标准库）；读取其他仓库的检查需要把家族的各仓库放在本仓库旁边。

```bash
python tools/make_readmes.py --check  # README（八种语言）是最新的
python tools/make_catalog.py --check  # 目录的版本与成熟度是最新的
python tools/make_brand.py --check    # 横幅图和图标是最新的
python tools/publication_check.py     # 发布时不会泄露私有内容
bash tools/check_all.sh               # 一次运行每个仓库的测试
python -m unittest discover -s tests  # 这些工具的 199 项测试；无需其他仓库
```

## 🧪 测试

| 领域 | 覆盖内容 |
|---|---|
| README 生成器 | 每个仓库的八种语言和各章节 |
| 目录与品牌 | `test_make_catalog_and_brand.py`、`test_repository_registry.py` |
| 发布 | 什么算 BLOCK 和 REVIEW，以及单提交副本 |
| CI 工具与启动器 | `test_ci_validate.py`、`test_sync_ci_tools.py`、`test_project_tool.py`、`test_check_all_script.py` |

GitHub Actions 在每次推送和拉取请求时运行 A.R.M.O.R. 基线：清单、版本、更新日志和 README 一致性的校验，然后是项目自身的构建和测试。

## 🏗️ 构建与发布

无需编译。版本记录在 `armor.project.json` 和 README 徽章中（读取自清单）；每个版本在 [CHANGELOG.md](CHANGELOG.md) 中都有对应条目。发布版本发布在 GitHub 上。

## 🩺 故障排除

| 你看到 | 原因 | 处理 |
|---|---|---|
| `READMEs out of date:` + a list | `tools/readme_src/` 的源文件或某个清单变了，而 README 没有重新生成 | 运行 `python tools/make_readmes.py`，查看每个仓库中变了什么并在该仓库提交 |
| `Status tables incomplete:` | 注册表中某个仓库的状态表缺少应有的行或颜色 | 补全其源文件中的 `FACTS["status"]` 和说明 |
| 某项检查显示 SKIP | 缺少其工具或本仓库旁边的仓库；缺少工具的检查绝不会是 PASS | 安装该工具，或把仓库克隆到本仓库旁边 |
| `publication_check.py` BLOCK | 发现了不能公开的内容（显示文件、行和类型，绝不显示值） | 删除它；如果在历史中，使用 `clean_history.py` |

## 📂 仓库结构

<p align="center">
  <img src="images/repository-structure.svg" alt="Repository structure of ARMOR-DOCS" width="100%">
</p>

<details>
<summary>目录树的文本版本</summary>

```text
ARMOR-DOCS/
├── tools/
│   ├── make_readmes.py                          由单一来源生成八种语言 README
│   ├── readme_src/                              每个仓库的事实与文字
│   ├── make_catalog.py make_brand.py            目录；横幅图与图标
│   ├── brand_banner.py registry.py              横幅图绘制；ARMOR-COMMON 的清单
│   ├── publication_check.py                     发布时不泄露私有内容
│   ├── clean_history.py sync_ci_tools.py        可发布的副本；统一的 CI 检查
│   ├── check_all.sh                             一次运行每个仓库的测试
│   ├── armor_ci_validate.py                     每个仓库自带的 CI 检查
│   ├── armor_project_tool.py pretty_run.py      启动器及其实时面板
│   ├── make_architecture.py make_structure.py   README 的两张图
│   └── universal_readme_check.py                README 版式检查
├── docs/                                        CAPABILITY_MATRIX、ARCHITECTURE、SECURITY_BASELINE、THREAT_MODEL、PROJECT_CATALOG、INTERFACES、FIRST_VERTICAL_SLICE、SETUP_CODE
├── tests/                                       这些工具的测试
├── brand/                                       徽标
├── images/                                      横幅图、图标、家族图和本 README 的图片
├── .github/                                     CI 工作流、仪表板通知、议题和 pull request 模板
├── armor.project.json                           清单：版本、角色、成熟度
├── CHANGELOG.md                                 每个版本的变化
├── run.sh run.bat                               启动（共用流程）
├── build.sh build.bat                           构建并测试（共用流程）
├── build-test.sh build-test.bat                 构建、测试并打包
├── test.sh test.bat                             只运行测试，不改版本
└── SECURITY.md SUPPORT.md CONTRIBUTING.md CODE_OF_CONDUCT.md LICENSE
```

</details>

## 🗺️ 路线图与已知限制

**当前已知限制**

* 能力矩阵是关于什么已经运行过的事实：某行在写成 Verified 之前，都没有接触过真实硬件。
* 只有雷达节点和 CM5 测试台在真实硬件上运行过。
* 没有独立的安全审查。

**下一步**

* 随着其他节点在各自开发板上运行，把矩阵中的行改为 Verified。

## 🌍 语言

README 和文本提供英语、西班牙语、法语、意大利语、德语、汉语、日语和欧洲葡萄牙语版本。

## 🔗 相关项目

**A.R.M.O.R.**（Autonomous Radar & Multimodal Observation Range）是一个由相互独立的仓库组成的周界安全系统。每个仓库都有自己的版本、自己的测试和自己的 README；这是整个系列：

* **[ARMOR-COMMON](https://github.com/JuanenRac/ARMOR-COMMON)** - 消息契约、验证器、一致性向量和生成的类型
* **[ARMOR-NODE-RADAR](https://github.com/JuanenRac/ARMOR-NODE-RADAR)** - 面向 ESP32-S3 的现场节点固件，配三个雷达和自带的网页面板
* **[ARMOR-NODE-SOLAR](https://github.com/JuanenRac/ARMOR-NODE-SOLAR)** - 太阳能逆变器和电池的协议，以及网关节点的消息
* **[ARMOR-NODE-ELECTRICAL](https://github.com/JuanenRac/ARMOR-NODE-ELECTRICAL)** - 电气节点：电表、电网读数的消息和切换规则
* **[ARMOR-NODE-ALARM](https://github.com/JuanenRac/ARMOR-NODE-ALARM)** - 报警节点与面板：防区、布防、延时、警笛和 PIN，可配合服务器也可独立使用
* **[ARMOR-NODE-HMI](https://github.com/JuanenRac/ARMOR-NODE-HMI)** - 触摸面板：壁挂屏幕上的系统状态、布防与确认，以及语音助手的所在
* **[ARMOR-NETWORK](https://github.com/JuanenRac/ARMOR-NETWORK)** - 本地网络：其设备、互联网以及变化
* **[ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER)** - 中央协调器：遥测、报警、设备、太阳能读数和摄像头
* **[ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO)** - 网页控制台：摄像头、雷达、报警、太阳能以及 2D/3D 场地设计器
* **[ARMOR-ANDROID-CONTROL](https://github.com/JuanenRac/ARMOR-ANDROID-CONTROL)** - 带实时 2D/3D 雷达的 Android 操作员客户端
* **[ARMOR-IOS-CONTROL](https://github.com/JuanenRac/ARMOR-IOS-CONTROL)** - iPhone 操作员客户端
* **[ARMOR-SERVER-AI](https://github.com/JuanenRac/ARMOR-SERVER-AI)** - 视觉推理策略，会解释其决策且从不驱动设备
* **[ARMOR-VISION](https://github.com/JuanenRac/ARMOR-VISION)** - 面向 Jetson Orin NX 的摄像头区域、遮罩和检测规则
* **[ARMOR-VOICE-AI](https://github.com/JuanenRac/ARMOR-VOICE-AI)** - 离线语音意图，附带无法伪造的确认
* **[ARMOR-HARDWARE](https://github.com/JuanenRac/ARMOR-HARDWARE)** - 外壳、电子器件和台架验收矩阵
* **[ARMOR-DEVOPS](https://github.com/JuanenRac/ARMOR-DEVOPS)** - 部署、CM5 测试台、备份和 TLS
* **[ARMOR-SIMULATOR](https://github.com/JuanenRac/ARMOR-SIMULATOR)** - 带可重复故障的离线遥测模拟器
* **[ARMOR-UPDATER](https://github.com/JuanenRac/ARMOR-UPDATER)** - 检测、安装和更新生态系统自身的仓库
* **ARMOR-DOCS**（本仓库） - 架构、安全基线和能力矩阵

## 📚 文档

* [ARCHITECTURE](docs/ARCHITECTURE.md)：网络、信任边界、时间与顺序
* [SECURITY_BASELINE](docs/SECURITY_BASELINE.md)：VLAN 设计、代码强制执行的内容和缺少的部分
* [THREAT_MODEL](docs/THREAT_MODEL.md)：防御什么、不防御什么
* [INTERFACES](docs/INTERFACES.md)：每个接口的生产者、消费者及信任位置
* [FIRST_VERTICAL_SLICE](docs/FIRST_VERTICAL_SLICE.md)：从模拟器到控制台的测试证明了什么、没有证明什么
* [SETUP_CODE](docs/SETUP_CODE.md)：节点的设置码
* [能力矩阵：哪些已被证明，哪些没有](docs/CAPABILITY_MATRIX.md)
* [项目目录：版本以及各仓库之间如何相互依赖](docs/PROJECT_CATALOG.md)
* [本仓库的更新日志](CHANGELOG.md)

## 🤝 参与贡献与社区

* 提交 pull request 之前，请运行 `python -I tools/armor_ci_validate.py` 和测试：两者都必须通过。请参阅 [CONTRIBUTING.md](CONTRIBUTING.md) 和[行为准则](CODE_OF_CONDUCT.md)。
* README 提供八种语言，由 ARMOR-DOCS 中的源文件生成：文本的修改在那里进行。
* 组件之间消息的变更从 ARMOR-COMMON 开始。
* 不要把仅仅构建过的东西描述为已在板子上运行。
* 请私下报告漏洞：[SECURITY.md](SECURITY.md)。问题、想法和报告：electrohobby3d@gmail.com（[SUPPORT.md](SUPPORT.md)）。

## 👤 作者

**JuanenRac (Electro Hobby 3D)** · electrohobby3d@gmail.com

## 📜 许可证

GPL-3.0-or-later - 见 [LICENSE](LICENSE)。
