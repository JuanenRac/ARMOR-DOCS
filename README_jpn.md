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
  🇯🇵 <b>日本語</b> |
  <a href="README_por.md">🇵🇹 Português</a>
</p>

### 正典のアーキテクチャ、セキュリティ基準、そして何が実証されているかの真実

<p align="center">
  <img src="https://img.shields.io/badge/License-GPL%203.0--or--later-blue.svg" alt="GPL 3.0 or later">
  <img src="https://img.shields.io/badge/Format-Markdown-083fa1.svg" alt="Format">
  <img src="https://img.shields.io/badge/Languages-8-00E5FF.svg" alt="Languages">
  <img src="https://img.shields.io/badge/Tests-199%20passing-2ea44f.svg" alt="Tests">
  <img src="https://img.shields.io/badge/Version-0.8.1.3-0f6cbd.svg" alt="Version">
  <img src="https://img.shields.io/badge/Maturity-established-2EA44F.svg" alt="Maturity">
</p>

---

**正直さのチェック - 今日動いているもの:** このリポジトリは検証済みのインターフェースと手順を文書化し、検証されていないものは率直に述べます。ある機能が「完成」と信じる前に[能力マトリクス](docs/CAPABILITY_MATRIX.md)を読んでください。各機能が、シミュレーションのみ、コンピューター上でのテスト、実機での検証のどれかを示しています。19 のリポジトリの README は 1 つのソース（`tools/readme_src/`）から 8 言語で作られ、各プロジェクトのバージョンと成熟度は自身のマニフェストから読み取るため、プロジェクトと違うことは書けません。

---

## 📋 ひと目で

| | |
|---|---|
| バージョン | `0.8.1.3` |
| 成熟度 | 確立 |
| 役割 | ドキュメントの拠点：アーキテクチャ、セキュリティ基盤、機能マトリクス、README・カタログ・バナーを書くツール |
| 技術 | Python 3.11+（ツール、標準ライブラリ）、Markdown |
| テスト | 199 件（`python -m unittest discover -s tests`、約 1 分） |
| インターフェース | `make_readmes.py`、`make_catalog.py`、`make_brand.py`、`publication_check.py`、`clean_history.py`、`sync_ci_tools.py`、`check_all.sh` |
| 動作環境 | Python のある任意のコンピューター（ファミリーのリポジトリをこの隣に置く） |
| 実機での確認 | 該当なし：ドキュメントで、他のリポジトリが実機で動かしたものを記録します |
| ライセンス | GPL-3.0-or-later |

**移動先：** [概要](#-概要) · [アーキテクチャ](#-アーキテクチャ) · [セキュリティ](#-セキュリティと安全) · [インターフェース](#-インターフェース) · [クイックスタート](#-クイックスタート) · [テスト](#-テスト) · [トラブルシューティング](#-トラブルシューティング) · [構成](#-リポジトリの構成) · [関連](#-関連プロジェクト)

## 🚦 プロジェクトの状況

各行はこのリポジトリの一部分で、信号は今日どこまで進んでいるかを示します。計画ではなく、リポジトリが示せるもの（テスト、ビルド、実行）に基づいて書かれています。

🟢 完了・検証済み · 🟡 動作する（既知の制限あり） · 🟠 一部のみ、または未検証 · 🔴 未実装または動作しない

| 領域 | 状態 | ここでの意味 |
|---|---|---|
| ソフトウェア | 🟢 | README、バナー、カタログ、機能マトリクスのジェネレーターと、各リポジトリにコピーする CI ツールは動作し、テスト済みです。 |
| テスト | 🟢 | ツールの 199 件のテストが通ります（`python -m unittest discover -s tests`）：公開前検査、履歴クリーナー、README・カタログ・ブランドのジェネレーター、CI ツールのコピー、共通ワークフローツール。 |
| 自動チェック | 🟢 | プッシュのたびに、README、バナー、カタログが最新であること、そしてレジストリのすべてのリポジトリに状況の表があることを確認します。 |
| 連携 | 🟢 | すべてのリポジトリの README は 1 つのソースから作られ、各リポジトリのバージョンと成熟度はそれぞれのマニフェストから読み取ります。 |
| ドキュメント | 🟢 | 機能マトリクスは、各機能がシミュレーションのみか、コンピューターでテスト済みか、実機で検証済みかを示します。8 言語と変更履歴は最新です。 |

## 🎯 概要

<p align="center">
  <img src="images/ARMOR_FAMILY.svg" alt="A.R.M.O.R. family" width="100%">
</p>

* [能力マトリクス](docs/CAPABILITY_MATRIX.md)：各能力はシミュレーションのみか、コンピューター上でテスト済みか、実機で検証済みか。
* [アーキテクチャ](docs/ARCHITECTURE.md)：ネットワーク、信頼境界、時刻と順序。
* [セキュリティベースライン](docs/SECURITY_BASELINE.md)：VLAN 設計、コードが強制するもの、まだ足りないもの。[脅威モデル](docs/THREAT_MODEL.md)も。
* [プロジェクトカタログ](docs/PROJECT_CATALOG.md)：19 のリポジトリ、そのバージョン、互いの依存関係。
* [インターフェース](docs/INTERFACES.md)：各インターフェースを誰が生成・利用し、どこで信頼されるか。
* [最初の垂直スライス](docs/FIRST_VERTICAL_SLICE.md)：シミュレーターからコンソールまでのテストが証明するものとしないもの。
* **ツール：**`make_readmes.py` は `readme_src/` から全リポジトリの README を 8 言語で作り、`make_catalog.py` はカタログのバージョンを書き、`make_brand.py` はバナーとアイコン、`publication_check.py` は公開前に非公開のものを探し、`clean_history.py` は公開用のコピーを作り、`sync_ci_tools.py` はファミリーの CI 検査を揃えます。

## 🧩 A.R.M.O.R. での役割

ARMOR-DOCS はファミリーの記憶です。アーキテクチャ、セキュリティベースライン、能力マトリクスがここにあり、各リポジトリで実際に実機で動いたものを示す場所です。19 のリポジトリすべての README を 1 つのソースから書くツールもここにあり、8 言語がずれないようにしています。

| 連携先 | 方法 | 目的 |
|---|---|---|
| ファミリーの全リポジトリ | 各 `armor.project.json` と README ファイル | ツールがバージョンと成熟度を読み、README、バナー、CI コピーを書く |
| ARMOR-COMMON | `registry/repositories.json` | ファミリーのリポジトリの唯一の一覧（`registry.py` が読む） |
| 公開する人 | `publication_check.py`  `clean_history.py` | 漏れるものと、公開できる 1 コミットのコピー |

## 🏛️ アーキテクチャ

<p align="center">
  <img src="images/architecture.svg" alt="ARMOR-DOCS architecture: what the tools read, the tools themselves and what they write in every repository" width="100%">
</p>

## 🔒 セキュリティと安全

| 脅威 | 防御 |
|---|---|
| 非公開情報の公開 | `publication_check.py` は git だけを読み（追跡ファイルと履歴。無視ファイルは読まない）、秘密は決して表示しません。BLOCK：秘密鍵、公開 IP アドレス、個人のメールアドレス、追跡された `secrets/` や `.env`、共著者や AI の行を含むコミット、プロジェクト以外の作者のコミット。REVIEW：平文のパスワードやトークンに見える行。BLOCK があれば終了コード 1 |
| 残骸の残る履歴 | `clean_history.py` は、プロジェクトの作者による 1 コミットだけの公開用コピーを作ります |
| 実証以上の主張 | `docs/CAPABILITY_MATRIX.md` は 3 段階（Simulated、Local、Verified）に None、Absent、Local-not-activated を加えたもの。実機に触れたのは Verified の行だけです（日常運用中の CM5 テストベンチ） |
| プロジェクトと食い違う README | 各 README のバージョンと成熟度は自身のマニフェストから読み取ります。push のたびに、README、バナー、カタログが最新で、レジストリの全リポジトリに状態表があることを検査します |

ファミリーのセキュリティ文書は [docs/SECURITY_BASELINE.md](docs/SECURITY_BASELINE.md)（VLAN 設計、コードが強制すること、まだ足りないこと）と [docs/THREAT_MODEL.md](docs/THREAT_MODEL.md) です。ここで秘密がないことが証明されるわけではありません。

## 🔌 インターフェース

| ルート | 認証 | 内容 |
|---|---|---|
| `python tools/make_readmes.py [--check]` | - | `tools/readme_src/` から全リポジトリの README を 8 言語で書き出す。`--check` は古いものがあると失敗。全ファイルを書き直すので、README ではなくソースを変更する |
| `python tools/make_catalog.py [--check]`  `make_brand.py [--check]` | - | `docs/PROJECT_CATALOG.md` のバージョンと成熟度、バナーとアイコン |
| `python tools/publication_check.py [REPO] [--no-history] [--ref=BRANCH]` | - | リポジトリを公開した場合に漏れるもの。BLOCK で終了コード 1 |
| `python tools/clean_history.py` | - | 1 コミットだけの公開用コピー |
| `python tools/sync_ci_tools.py [--check]` | - | 共通の CI 検査とランチャーを各リポジトリにコピー。コピーがずれると `--check` が失敗 |
| `bash tools/check_all.sh [--android] [--compose]` | - | 全リポジトリのテストを一度に実行。ツールがない検査は PASS ではなく SKIP |

各 README のソースは `tools/readme_src/repos/<リポジトリ>.py`（言語に依存しない事実と 8 言語の文言）で、README の周囲の文言は `ui.py`、スクリーンショットは `shots.py` にあります。`tools/registry.py` は ARMOR-COMMON のリポジトリ一覧を読みます。[docs/INTERFACES.md](docs/INTERFACES.md) と [docs/SETUP_CODE.md](docs/SETUP_CODE.md) も参照。

## 🚀 クイックスタート

**要件：** ツール用の Python 3.11+（標準ライブラリのみ）。それらを読む検査には、ファミリーのリポジトリをこの隣に置きます。

```bash
python tools/make_readmes.py --check  # README（8 言語）は最新
python tools/make_catalog.py --check  # カタログのバージョンと成熟度は最新
python tools/make_brand.py --check    # バナーとアイコンは最新
python tools/publication_check.py     # 公開しても非公開情報は出ない
bash tools/check_all.sh               # 各リポジトリのテストを一度に
python -m unittest discover -s tests  # これらのツールの 199 件のテスト（他のリポジトリは不要）
```

## 🧪 テスト

| 分野 | 対象 |
|---|---|
| README ジェネレーター | 各リポジトリの 8 言語とセクション |
| カタログとブランド | `test_make_catalog_and_brand.py`、`test_repository_registry.py` |
| 公開 | BLOCK と REVIEW の基準、1 コミットのコピー |
| CI ツールとランチャー | `test_ci_validate.py`、`test_sync_ci_tools.py`、`test_project_tool.py`、`test_check_all_script.py` |

GitHub Actions は push と pull request のたびに A.R.M.O.R. の基本検査（マニフェスト、バージョン、変更履歴、README の一致）と、プロジェクト自身のビルドとテストを実行します。

## 🏗️ ビルドとリリース

コンパイルするものはありません。バージョンは `armor.project.json` と README のバッジ（マニフェストから読み取り）にあり、各バージョンには [CHANGELOG.md](CHANGELOG.md) にエントリーがあります。リリースは GitHub で公開されます。

## 🩺 トラブルシューティング

| 表示 | 原因 | 対処 |
|---|---|---|
| `READMEs out of date:` + a list | `tools/readme_src/` のソースかマニフェストが変わり、README が書き直されていない | `python tools/make_readmes.py` を実行し、各リポジトリの変更を確認してそこでコミット |
| `Status tables incomplete:` | レジストリのリポジトリの状態表に、必要な行や色がない | そのソースの `FACTS["status"]` と注記を補う |
| 検査が SKIP と出る | そのツールまたは隣のリポジトリがない（ツールがない検査は PASS にならない） | ツールを入れるか、隣にリポジトリをクローンする |
| `publication_check.py` BLOCK | 公開してはならないものが見つかった（ファイル、行、種類を表示。値は表示しない） | 取り除き、履歴にある場合は `clean_history.py` を使う |

## 📂 リポジトリの構成

<p align="center">
  <img src="images/repository-structure.svg" alt="Repository structure of ARMOR-DOCS" width="100%">
</p>

<details>
<summary>ツリーのテキスト版</summary>

```text
ARMOR-DOCS/
├── tools/
│   ├── make_readmes.py                          1 つのソースから 8 言語の README
│   ├── readme_src/                              各リポジトリの事実と文言
│   ├── make_catalog.py make_brand.py            カタログ、バナーとアイコン
│   ├── brand_banner.py registry.py              バナーの描画、ARMOR-COMMON の一覧
│   ├── publication_check.py                     公開物に非公開情報を含めない
│   ├── clean_history.py sync_ci_tools.py        公開用コピー、同一の CI 検査
│   ├── check_all.sh                             各リポジトリのテストを一度に
│   ├── armor_ci_validate.py                     各リポジトリが持つ CI 検査
│   ├── armor_project_tool.py pretty_run.py      ランチャーとライブパネル
│   ├── make_architecture.py make_structure.py   README の 2 つの図
│   └── universal_readme_check.py                README のレイアウト検査
├── docs/                                        CAPABILITY_MATRIX、ARCHITECTURE、SECURITY_BASELINE、THREAT_MODEL、PROJECT_CATALOG、INTERFACES、FIRST_VERTICAL_SLICE、SETUP_CODE
├── tests/                                       これらのツールのテスト
├── brand/                                       エンブレム
├── images/                                      バナー、アイコン、ファミリーの図、この README の図
├── .github/                                     CI ワークフロー、ダッシュボード通知、Issue と Pull Request のテンプレート
├── armor.project.json                           マニフェスト：版・役割・成熟度
├── CHANGELOG.md                                 各バージョンの変更点
├── run.sh run.bat                               起動（共通フロー）
├── build.sh build.bat                           ビルドとテスト（共通フロー）
├── build-test.sh build-test.bat                 ビルド、テスト、パッケージ化
├── test.sh test.bat                             テストのみ（版は変えません）
└── SECURITY.md SUPPORT.md CONTRIBUTING.md CODE_OF_CONDUCT.md LICENSE
```

</details>

## 🗺️ ロードマップと既知の制限

**現時点の既知の制限**

* 機能マトリクスは、何が動いたかについての真実です。Verified と書かれるまで、その行は実機に触れていません。
* 実機で動いたのはレーダーノードと CM5 テストベンチだけです。
* 第三者によるセキュリティレビューはありません。

**今後**

* 他のノードが各基板で動いた分だけ、マトリクスの行を Verified にする。

## 🌍 言語

README とテキストは、英語、スペイン語、フランス語、イタリア語、ドイツ語、中国語、日本語、ヨーロッパポルトガル語で提供されています。

## 🔗 関連プロジェクト

**A.R.M.O.R.**（Autonomous Radar & Multimodal Observation Range）は、独立したリポジトリで構成される境界セキュリティシステムです。各リポジトリは独自のバージョン、テスト、README を持ちます。ファミリーは次のとおりです：

* **[ARMOR-COMMON](https://github.com/JuanenRac/ARMOR-COMMON)** - メッセージのコントラクト、バリデーター、適合ベクトル、生成された型
* **[ARMOR-NODE-RADAR](https://github.com/JuanenRac/ARMOR-NODE-RADAR)** - 3 つのレーダーと独自の Web パネルを備えた ESP32-S3 向けフィールドノードのファームウェア
* **[ARMOR-NODE-SOLAR](https://github.com/JuanenRac/ARMOR-NODE-SOLAR)** - ソーラーインバーターとバッテリーのプロトコル、ゲートウェイノードのメッセージ
* **[ARMOR-NODE-ELECTRICAL](https://github.com/JuanenRac/ARMOR-NODE-ELECTRICAL)** - 電気ノード：メーター、系統の読み取り値のメッセージ、切り替えのルール
* **[ARMOR-NODE-ALARM](https://github.com/JuanenRac/ARMOR-NODE-ALARM)** - 警報ノードとパネル：ゾーン、警戒、遅延、サイレン、PIN。サーバーありでもなしでも動作
* **[ARMOR-NODE-HMI](https://github.com/JuanenRac/ARMOR-NODE-HMI)** - タッチパネル：壁面画面でのシステムの状態、警戒と確認応答、そして音声アシスタントの置き場
* **[ARMOR-NETWORK](https://github.com/JuanenRac/ARMOR-NETWORK)** - ローカルネットワーク：そのデバイス、インターネット、そして変化
* **[ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER)** - 中央コーディネーター：テレメトリ、警報、デバイス、ソーラーの読み取り値、カメラ
* **[ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO)** - Web コンソール：カメラ、レーダー、警報、太陽光エネルギー、2D/3D のサイトデザイナー
* **[ARMOR-ANDROID-CONTROL](https://github.com/JuanenRac/ARMOR-ANDROID-CONTROL)** - ライブの 2D/3D レーダーを備えた Android オペレータークライアント
* **[ARMOR-IOS-CONTROL](https://github.com/JuanenRac/ARMOR-IOS-CONTROL)** - iPhone オペレータークライアント
* **[ARMOR-SERVER-AI](https://github.com/JuanenRac/ARMOR-SERVER-AI)** - 判断を説明し、決して作動させない視覚推論ポリシー
* **[ARMOR-VISION](https://github.com/JuanenRac/ARMOR-VISION)** - Jetson Orin NX 向けのカメラゾーン、マスク、検出ルール
* **[ARMOR-VOICE-AI](https://github.com/JuanenRac/ARMOR-VOICE-AI)** - 偽造できない確認つきのオフライン音声インテント
* **[ARMOR-HARDWARE](https://github.com/JuanenRac/ARMOR-HARDWARE)** - 筐体、電子回路、ベンチ受け入れマトリクス
* **[ARMOR-DEVOPS](https://github.com/JuanenRac/ARMOR-DEVOPS)** - デプロイ、CM5 テストベンチ、バックアップ、TLS
* **[ARMOR-SIMULATOR](https://github.com/JuanenRac/ARMOR-SIMULATOR)** - 再現可能な障害を持つオフラインのテレメトリシミュレーター
* **[ARMOR-UPDATER](https://github.com/JuanenRac/ARMOR-UPDATER)** - エコシステム自身のリポジトリを検出、インストール、更新
* **ARMOR-DOCS**（このリポジトリ） - アーキテクチャ、セキュリティのベースライン、機能マトリクス

## 📚 ドキュメント

* [ARCHITECTURE](docs/ARCHITECTURE.md)：ネットワーク、信頼境界、時刻と順序
* [SECURITY_BASELINE](docs/SECURITY_BASELINE.md)：VLAN 設計、コードが強制すること、足りないこと
* [THREAT_MODEL](docs/THREAT_MODEL.md)：守るものと守らないもの
* [INTERFACES](docs/INTERFACES.md)：各インターフェースの提供側と利用側、信頼する場所
* [FIRST_VERTICAL_SLICE](docs/FIRST_VERTICAL_SLICE.md)：シミュレーターからコンソールまでのテストが証明すること、しないこと
* [SETUP_CODE](docs/SETUP_CODE.md)：ノードの設定コード
* [機能マトリクス：何が証明され、何が証明されていないか](docs/CAPABILITY_MATRIX.md)
* [プロジェクトカタログ：バージョンと、リポジトリ同士の依存関係](docs/PROJECT_CATALOG.md)
* [このリポジトリの変更履歴](CHANGELOG.md)

## 🤝 コントリビュートとコミュニティ

* Pull Request の前に `python -I tools/armor_ci_validate.py` とテストを実行してください。どちらも通る必要があります。[CONTRIBUTING.md](CONTRIBUTING.md) と[行動規範](CODE_OF_CONDUCT.md)を参照してください。
* README は 8 言語で提供され、ARMOR-DOCS のソースから生成されます。文面の変更はそちらで行います。
* コンポーネント間のメッセージの変更は ARMOR-COMMON から始めます。
* ビルドしただけのものを、ボード上で動いているかのように書かないでください。
* 脆弱性は非公開で報告してください：[SECURITY.md](SECURITY.md)。質問、アイデア、報告：electrohobby3d@gmail.com（[SUPPORT.md](SUPPORT.md)）。

## 👤 作者

**JuanenRac (Electro Hobby 3D)** · electrohobby3d@gmail.com

## 📜 ライセンス

GPL-3.0-or-later - [LICENSE](LICENSE) を参照してください。
