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
  <img src="https://img.shields.io/badge/License-GPL%203.0-blue.svg" alt="GPL 3.0">
  <img src="https://img.shields.io/badge/Format-Markdown-083fa1.svg" alt="Format">
  <img src="https://img.shields.io/badge/Languages-8-00E5FF.svg" alt="Languages">
  <img src="https://img.shields.io/badge/Version-0.8.1.2-0f6cbd.svg" alt="Version">
  <img src="https://img.shields.io/badge/Maturity-established-2EA44F.svg" alt="Maturity">
</p>

---

**正直さのチェック - 今日動いているもの:** このリポジトリは検証済みのインターフェースと手順を文書化し、検証されていないものは率直に述べます。ある機能が「完成」と信じる前に[能力マトリクス](docs/CAPABILITY_MATRIX.md)を読んでください。各機能が、シミュレーションのみ、コンピューター上でのテスト、実機での検証のどれかを示しています。19 のリポジトリの README は 1 つのソース（`tools/readme_src/`）から 8 言語で作られ、各プロジェクトのバージョンと成熟度は自身のマニフェストから読み取るため、プロジェクトと違うことは書けません。

---

## 📋 ひと目で

| | |
|---|---|
| バージョン | `0.8.1.2` |
| 成熟度 | 確立 |
| 技術 | Markdown / Mermaid |
| 実機での確認 | 該当なし：ドキュメントで、他のリポジトリが実機で動かしたものを記録します |

## 🚦 プロジェクトの状況

各行はこのリポジトリの一部分で、信号は今日どこまで進んでいるかを示します。計画ではなく、リポジトリが示せるもの（テスト、ビルド、実行）に基づいて書かれています。

🟢 完了・検証済み · 🟡 動作する（既知の制限あり） · 🟠 一部のみ、または未検証 · 🔴 未実装または動作しない

| 領域 | 状態 | ここでの意味 |
|---|---|---|
| ソフトウェア | 🟢 | README、バナー、カタログ、機能マトリクスのジェネレーターと、各リポジトリにコピーする CI ツールは動作し、テスト済みです。 |
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

## 📂 リポジトリの構成

```text
ARMOR-DOCS/
├── docs/     CAPABILITY_MATRIX, ARCHITECTURE, SECURITY_BASELINE, PROJECT_CATALOG, INTERFACES, THREAT_MODEL, FIRST_VERTICAL_SLICE
├── tools/    make_readmes.py (+ readme_src/: the facts and the words of every repository in eight languages), make_catalog.py, make_brand.py (+ brand_banner.py), registry.py (reads the list of repositories of ARMOR-COMMON), publication_check.py, clean_history.py, sync_ci_tools.py, check_all.sh
├── tests/    the tests of these tools: the publication check, the history cleaner, the README, catalogue and brand generators, the copy of the CI tools and the shared workflow tool
├── brand/    the emblem
└── images/   this repository's banner, icon and the family picture
```

## 🛠️ 開発環境

**必要なもの:** ツール用の Python 3.11+

```bash
python tools/make_readmes.py --check      # the READMEs (8 languages) are current
python tools/make_catalog.py --check     # the versions and maturity of the catalogue are current
python tools/make_brand.py --check        # the banners and icons are current
python tools/publication_check.py         # nothing private would leave with a publication
bash tools/check_all.sh                   # every repository's own tests, in one run
python -m unittest discover -s tests     # the tests of these tools (they need no other repository)
```

## 🔗 関連プロジェクト

**A.R.M.O.R.**（Autonomous Radar & Multimodal Observation Range）は、独立したリポジトリで構成される周辺警備システムです。それぞれに独自のバージョン、テスト、README があります。ファミリーは次のとおりです：

* **[ARMOR-COMMON](https://github.com/JuanenRac/ARMOR-COMMON)** - メッセージ契約、検証器、適合性ベクトル、生成された型
* **[ARMOR-NODE-RADAR](https://github.com/JuanenRac/ARMOR-NODE-RADAR)** - ESP32-S3 用フィールドノードのファームウェア。レーダー 3 基と独自の Web パネル付き
* **[ARMOR-NODE-SOLAR](https://github.com/JuanenRac/ARMOR-NODE-SOLAR)** - 太陽光インバーターとバッテリーのプロトコル、およびゲートウェイノードのメッセージ
* **[ARMOR-NODE-ELECTRICAL](https://github.com/JuanenRac/ARMOR-NODE-ELECTRICAL)** - 電気ノード：電力量計、電力網の計測メッセージ、開閉のルール
* **[ARMOR-NODE-ALARM](https://github.com/JuanenRac/ARMOR-NODE-ALARM)** - 警報ノードと警報盤：警戒区域、警戒セット、遅延、サイレン、PIN。サーバーがあってもなくても
* **[ARMOR-NODE-HMI](https://github.com/JuanenRac/ARMOR-NODE-HMI)** - タッチパネル：壁面ディスプレイでのシステム状態表示、警戒・確認操作、音声アシスタントの拠点
* **[ARMOR-NETWORK](https://github.com/JuanenRac/ARMOR-NETWORK)** - ローカルネットワーク：機器、インターネット、そして変化
* **[ARMOR-SERVER](https://github.com/JuanenRac/ARMOR-SERVER)** - 中央コーディネーター：テレメトリ、アラーム、デバイス、太陽光の測定値、カメラ
* **[ARMOR-STUDIO](https://github.com/JuanenRac/ARMOR-STUDIO)** - Web コンソール：カメラ、レーダー、アラーム、太陽光発電、2D/3D サイト設計
* **[ARMOR-ANDROID-CONTROL](https://github.com/JuanenRac/ARMOR-ANDROID-CONTROL)** - リアルタイム 2D/3D レーダー付きの Android オペレータークライアント
* **[ARMOR-IOS-CONTROL](https://github.com/JuanenRac/ARMOR-IOS-CONTROL)** - iPhone オペレータークライアント
* **[ARMOR-SERVER-AI](https://github.com/JuanenRac/ARMOR-SERVER-AI)** - 判断を説明し、決して動作しない視覚推論ポリシー
* **[ARMOR-VISION](https://github.com/JuanenRac/ARMOR-VISION)** - Jetson Orin NX 向けのカメラのゾーン、マスク、検知ルール
* **[ARMOR-VOICE-AI](https://github.com/JuanenRac/ARMOR-VOICE-AI)** - 偽造できない確認を備えたオフライン音声インテント
* **[ARMOR-HARDWARE](https://github.com/JuanenRac/ARMOR-HARDWARE)** - 筐体、電子部品、ベンチ受け入れマトリクス
* **[ARMOR-DEVOPS](https://github.com/JuanenRac/ARMOR-DEVOPS)** - デプロイ、CM5 テストベンチ、バックアップ、TLS
* **[ARMOR-SIMULATOR](https://github.com/JuanenRac/ARMOR-SIMULATOR)** - 再現可能な故障を備えたオフラインのテレメトリシミュレーター
* **[ARMOR-UPDATER](https://github.com/JuanenRac/ARMOR-UPDATER)** - エコシステム自身のリポジトリを検出し、インストールし、更新する
* **ARMOR-DOCS** (このリポジトリ) - アーキテクチャ、セキュリティ基準、機能マトリクス

## 📚 ドキュメントとコミュニティ

詳しくは：

* [機能マトリクス：実証済みのものとそうでないもの](docs/CAPABILITY_MATRIX.md)
* [プロジェクト一覧：バージョンとリポジトリ間の依存関係](docs/PROJECT_CATALOG.md)
* [このリポジトリの変更履歴](CHANGELOG.md)
* [ライセンス（GPL-3.0-or-later）](LICENSE)
* 質問・提案・報告：electrohobby3d@gmail.com

## 👤 作者

**JuanenRac (Electro Hobby 3D)** · electrohobby3d@gmail.com

## 📜 ライセンス

GPL-3.0-or-later - [LICENSE](LICENSE) を参照。
