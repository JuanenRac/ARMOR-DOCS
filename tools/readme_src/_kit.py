# Small helpers shared by the universal README sources of the repositories (words that every source repeats, tables and the two pictures).
# Copyright (C) 2026 JuanenRac (Electro Hobby 3D). GPL-3.0-or-later.
from __future__ import annotations

import importlib.util
import json
from pathlib import Path

# the order of the arguments of P(): the eight languages of the family
LGS = ["en", "es", "de", "fr", "it", "ja", "zh", "pt"]
ROOT = Path(__file__).resolve().parents[3]


def P(en, es, de, fr, it, ja, zh, pt):
    """One text in the eight languages."""
    return dict(zip(LGS, (en, es, de, fr, it, ja, zh, pt)))


def pick(value, lg):
    """A text that is the same in every language (a string) or one per language (a mapping)."""
    return value[lg] if isinstance(value, dict) else value


# the column headings that the tables of every README share
HEAD = {
    "threat": P(["Threat", "Defence"], ["Amenaza", "Defensa"], ["Bedrohung", "Abwehr"], ["Menace", "Défense"], ["Minaccia", "Difesa"], ["脅威", "防御"], ["威胁", "防御"], ["Ameaça", "Defesa"]),
    "trouble": P(["You see", "Because", "Do"], ["Ves", "Porque", "Haz"], ["Du siehst", "Weil", "Tu"], ["Vous voyez", "Parce que", "Faites"], ["Vedi", "Perché", "Fai"],
                 ["表示", "原因", "対処"], ["你看到", "原因", "处理"], ["Vê", "Porque", "Faça"]),
    "tests": P(["Test file", "Tests", "What it covers"], ["Fichero de pruebas", "Pruebas", "Qué cubre"], ["Testdatei", "Tests", "Was sie abdeckt"],
               ["Fichier de tests", "Tests", "Ce qu'il couvre"], ["File di test", "Test", "Cosa copre"], ["テストファイル", "テスト数", "対象"],
               ["测试文件", "测试数", "覆盖内容"], ["Ficheiro de testes", "Testes", "O que cobre"]),
    "config": P(["Variable", "Needed", "What it sets"], ["Variable", "Necesaria", "Qué fija"], ["Variable", "Nötig", "Was sie festlegt"],
                ["Variable", "Requise", "Ce qu'elle définit"], ["Variabile", "Necessaria", "Cosa imposta"], ["変数", "必要", "設定する内容"],
                ["变量", "是否必需", "设置内容"], ["Variável", "Necessária", "O que define"]),
    "setting": P(["Setting", "Default", "What it does"], ["Ajuste", "Por defecto", "Qué hace"], ["Einstellung", "Standard", "Was sie tut"],
                 ["Réglage", "Par défaut", "Ce qu'il fait"], ["Impostazione", "Predefinito", "Cosa fa"], ["設定", "既定値", "内容"],
                 ["设置", "默认值", "作用"], ["Definição", "Predefinição", "O que faz"]),
    "route": P(["Route", "Auth", "What it does"], ["Ruta", "Autenticación", "Qué hace"], ["Route", "Authentifizierung", "Was sie tut"],
               ["Route", "Authentification", "Ce qu'elle fait"], ["Rotta", "Autenticazione", "Cosa fa"], ["ルート", "認証", "内容"],
               ["路由", "认证", "作用"], ["Rota", "Autenticação", "O que faz"]),
    "talks": P(["It talks to", "How", "What for"], ["Habla con", "Cómo", "Para qué"], ["Er spricht mit", "Wie", "Wozu"], ["Il parle à", "Comment", "Pour quoi faire"],
               ["Parla con", "Come", "A che scopo"], ["連携先", "方法", "目的"], ["对话对象", "方式", "用途"], ["Fala com", "Como", "Para quê"]),
    "limit": P(["Limit", "Value"], ["Límite", "Valor"], ["Grenze", "Wert"], ["Limite", "Valeur"], ["Limite", "Valore"], ["上限", "値"], ["限制", "值"], ["Limite", "Valor"]),
    "option": P(["Option", "What it does"], ["Opción", "Qué hace"], ["Option", "Was sie tut"], ["Option", "Ce qu'elle fait"], ["Opzione", "Cosa fa"], ["オプション", "内容"],
                ["选项", "作用"], ["Opção", "O que faz"]),
    "topic": P(["Topic", "What it carries"], ["Topic", "Qué lleva"], ["Topic", "Was es trägt"], ["Topic", "Ce qu'il porte"], ["Topic", "Cosa porta"], ["トピック", "内容"], ["主题", "内容"], ["Tópico", "O que leva"]),
    "tool": P(["Tool", "What it does"], ["Herramienta", "Qué hace"], ["Werkzeug", "Was es tut"], ["Outil", "Ce qu'il fait"], ["Strumento", "Cosa fa"], ["ツール", "内容"], ["工具", "作用"], ["Ferramenta", "O que faz"]),
    "area": P(["Area", "What it covers"], ["Área", "Qué cubre"], ["Bereich", "Was er abdeckt"], ["Domaine", "Ce qu'il couvre"], ["Area", "Cosa copre"], ["分野", "対象"], ["领域", "覆盖内容"], ["Área", "O que cobre"]),
    "item": P(["Item", "What it is"], ["Elemento", "Qué es"], ["Element", "Was es ist"], ["Élément", "Ce que c'est"], ["Elemento", "Cos'è"], ["項目", "内容"],
              ["项目", "说明"], ["Elemento", "O que é"]),
}
SUMMARY_DIAGRAM = P("Text version of the diagram (Mermaid)", "Versión en texto del diagrama (Mermaid)", "Textversion des Diagramms (Mermaid)", "Version texte du diagramme (Mermaid)",
                    "Versione testuale del diagramma (Mermaid)", "図のテキスト版（Mermaid）", "图表的文本版本（Mermaid）", "Versão em texto do diagrama (Mermaid)")
SUMMARY_TREE = P("Text version of the tree", "Versión en texto del árbol", "Textversion des Baums", "Version texte de l'arborescence", "Versione testuale dell'albero",
                 "ツリーのテキスト版", "目录树的文本版本", "Versão em texto da árvore")
LIMITS = P("**Known limits today**", "**Límites conocidos hoy**", "**Bekannte Grenzen heute**", "**Limites connues aujourd'hui**", "**Limiti noti oggi**", "**現時点の既知の制限**",
           "**当前已知限制**", "**Limites conhecidos hoje**")
NEXT = P("**Next**", "**Lo siguiente**", "**Als Nächstes**", "**Prochainement**", "**Prossimi passi**", "**今後**", "**下一步**", "**A seguir**")
DOES = P("**What it does**", "**Qué hace**", "**Was es tut**", "**Ce qu'il fait**", "**Cosa fa**", "**できること**", "**它做什么**", "**O que faz**")
DOES_NOT = P("**What it does not do**", "**Qué no hace**", "**Was es nicht tut**", "**Ce qu'il ne fait pas**", "**Cosa non fa**", "**できないこと**", "**它不做什么**", "**O que não faz**")
WHY = P("**Why it is built this way**", "**Por qué está hecho así**", "**Warum es so gebaut ist**", "**Pourquoi il est construit ainsi**", "**Perché è fatto così**", "**この作りにした理由**",
        "**为什么这样构建**", "**Porque é construído assim**")
REQ = P("**Requirements:**", "**Requisitos:**", "**Voraussetzungen:**", "**Prérequis :**", "**Requisiti:**", "**要件：**", "**要求：**", "**Requisitos:**")
RUN_NOTE = P("Run the repository's checks before a commit:", "Ejecuta las comprobaciones del repositorio antes de un commit:", "Führe vor einem Commit die Prüfungen des Repositorys aus:",
             "Lancez les vérifications du dépôt avant un commit :", "Esegui i controlli del repository prima di un commit:", "コミットの前にリポジトリの検査を実行します：",
             "提交前运行仓库的检查：", "Execute as verificações do repositório antes de um commit:")


def table(lg: str, head: str | list, rows) -> str:
    """A Markdown table. `head` is a key of HEAD or a list of column titles; each cell is a string or a mapping with the eight languages."""
    titles = HEAD[head][lg] if isinstance(head, str) else [pick(h, lg) for h in head]
    lines = ["| " + " | ".join(titles) + " |", "|" + "---|" * len(titles)]
    for row in rows:
        lines.append("| " + " | ".join(str(pick(cell, lg)).replace("\n", " ") for cell in row) + " |")
    return "\n".join(lines)


def arch(lg: str, repo: str, alt: str, mermaid: str | None = None, before: str = "", after: str = "") -> str:
    """The Architecture section: the picture and, when the repository had one, the Mermaid text inside <details>."""
    out = [before.strip(), f'<p align="center">\n  <img src="images/architecture.svg" alt="{alt}" width="100%">\n</p>'] if before.strip() else \
        [f'<p align="center">\n  <img src="images/architecture.svg" alt="{alt}" width="100%">\n</p>']
    if mermaid:
        out.append(f"<details>\n<summary>{SUMMARY_DIAGRAM[lg]}</summary>\n\n```mermaid\n{mermaid.strip()}\n```\n\n</details>")
    if after.strip():
        out.append(after.strip())
    return "\n\n".join(out)


def _structure_tool():
    path = ROOT / "ARMOR-DOCS" / "tools" / "make_structure.py"
    spec = importlib.util.spec_from_file_location("_a2_make_structure", path)
    module = importlib.util.module_from_spec(spec)
    import sys
    sys.path.insert(0, str(path.parent))
    spec.loader.exec_module(module)
    return module


def structure(lg: str, repo: str, tree: str | None = None, before: str = "", after: str = "") -> str:
    """The Repository Structure section: the picture and the text tree. The tree is the one of docs/structure.json of the repository, carried by the source of its README
    (a source must not read a sibling repository: in CI there is none); `make_structure.py --check --readmes` of the repository fails when the two disagree."""
    if tree is None:
        tool = _structure_tool()
        spec = json.loads((ROOT / repo / "docs" / "structure.json").read_text(encoding="utf-8"))
        tree = tool.render_tree(spec, lg)
    parts = []
    if before.strip():
        parts.append(before.strip())
    parts.append(f'<p align="center">'+chr(10)+f'  <img src="images/repository-structure.svg" alt="Repository structure of {repo}" width="100%">'+chr(10)+'</p>')
    parts.append('<details>'+chr(10)+f'<summary>{SUMMARY_TREE[lg]}</summary>'+chr(10)*2+'```text'+chr(10)+tree+chr(10)+'```'+chr(10)*2+'</details>')
    if after.strip():
        parts.append(after.strip())
    return (chr(10)*2).join(parts)


def code(lg: str, lines, shell: str = "powershell") -> str:
    """A code block. Each line is a command, or (command, comment) where the comment is a string or one per language; the comments line up."""
    items = [(line, "") if isinstance(line, str) else (line[0], pick(line[1], lg)) for line in lines]
    width = max([len(cmd) for cmd, note in items if note] or [0]) + 2
    body = (chr(10)).join((cmd.ljust(width) + "# " + note) if note else cmd for cmd, note in items)
    return "```" + shell + chr(10) + body + chr(10) + "```"


# the labels of the rows of At a glance, and the sentences that every ARMOR repository repeats
GL = {
    "role": P("Role", "Función", "Rolle", "Rôle", "Ruolo", "役割", "角色", "Função"),
    "stack": P("Stack", "Tecnología", "Technik", "Technologie", "Tecnologia", "技術", "技术栈", "Tecnologia"),
    "tests": P("Tests", "Pruebas", "Tests", "Tests", "Test", "テスト", "测试", "Testes"),
    "runs": P("Runs on", "Funciona en", "Läuft auf", "Fonctionne sur", "Gira su", "動作環境", "运行位置", "Funciona em"),
    "listens": P("Listens on", "Escucha en", "Lauscht auf", "Écoute sur", "In ascolto su", "待ち受け", "监听地址", "Escuta em"),
    "hardware": P("On real hardware", "En hardware real", "Auf echter Hardware", "Sur matériel réel", "Su hardware reale", "実機での確認", "真实硬件", "Em hardware real"),
    "license": P("License", "Licencia", "Lizenz", "Licence", "Licenza", "ライセンス", "许可证", "Licença"),
    "contract": P("Contract", "Contrato", "Vertrag", "Contrat", "Contratto", "契約", "契约", "Contrato"),
    "interfaces": P("Interfaces", "Interfaces", "Schnittstellen", "Interfaces", "Interfacce", "インターフェース", "接口", "Interfaces"),
    "listens_http": P("Serves", "Sirve", "Bietet", "Sert", "Serve", "提供", "提供", "Serve"),
    "default_port": P("Default port", "Puerto por defecto", "Standardport", "Port par défaut", "Porta predefinita", "既定のポート", "默认端口", "Porta predefinida"),
}
LICENSE_VALUE = "GPL-3.0-or-later"
DOCS_OK = P("Eight languages and the changelog are up to date.", "Los ocho idiomas y el registro de cambios están al día.", "Acht Sprachen und das Änderungsprotokoll sind aktuell.",
            "Huit langues et le journal des modifications sont à jour.", "Otto lingue e il registro delle modifiche sono aggiornati.", "8 言語と変更履歴は最新です。",
            "八种语言和更新日志均为最新。", "Os oito idiomas e o registo de alterações estão atualizados.")
CONTRIB = P("Before a pull request run `python -I tools/armor_ci_validate.py` and the tests: both must pass. See [CONTRIBUTING.md](CONTRIBUTING.md) and the [code of conduct](CODE_OF_CONDUCT.md).",
            "Antes de un pull request ejecuta `python -I tools/armor_ci_validate.py` y las pruebas: ambos deben pasar. Mira [CONTRIBUTING.md](CONTRIBUTING.md) y el [código de conducta](CODE_OF_CONDUCT.md).",
            "Führe vor einem Pull Request `python -I tools/armor_ci_validate.py` und die Tests aus: Beide müssen bestehen. Siehe [CONTRIBUTING.md](CONTRIBUTING.md) und den [Verhaltenskodex](CODE_OF_CONDUCT.md).",
            "Avant une pull request, exécutez `python -I tools/armor_ci_validate.py` et les tests : les deux doivent réussir. Voir [CONTRIBUTING.md](CONTRIBUTING.md) et le [code de conduite](CODE_OF_CONDUCT.md).",
            "Prima di una pull request esegui `python -I tools/armor_ci_validate.py` e i test: devono passare entrambi. Vedi [CONTRIBUTING.md](CONTRIBUTING.md) e il [codice di condotta](CODE_OF_CONDUCT.md).",
            "Pull Request の前に `python -I tools/armor_ci_validate.py` とテストを実行してください。どちらも通る必要があります。[CONTRIBUTING.md](CONTRIBUTING.md) と[行動規範](CODE_OF_CONDUCT.md)を参照してください。",
            "提交 pull request 之前，请运行 `python -I tools/armor_ci_validate.py` 和测试：两者都必须通过。请参阅 [CONTRIBUTING.md](CONTRIBUTING.md) 和[行为准则](CODE_OF_CONDUCT.md)。",
            "Antes de um pull request execute `python -I tools/armor_ci_validate.py` e os testes: ambos têm de passar. Consulte [CONTRIBUTING.md](CONTRIBUTING.md) e o [código de conduta](CODE_OF_CONDUCT.md).")


def text_for(lg: str, **parts) -> dict:
    """Builds the TEXT of one language from texts written as mappings of the eight languages (or plain strings), leaving out the parts that are None."""
    out = {}
    for key, value in parts.items():
        if value is None:
            continue
        if key == "body":
            out[key] = {k: pick(v, lg) for k, v in value.items() if v is not None}
        elif key in ("glance",):
            out[key] = [[pick(a, lg), pick(b, lg)] for a, b in value]
        elif key in ("status",):
            out[key] = {k: pick(v, lg) for k, v in value.items()}
        elif key == "docs":
            out[key] = [pick(v, lg) for v in value]
        else:
            out[key] = pick(value, lg)
    return out


def T(s: str) -> dict:
    """Eight short texts separated by ' | ' (en es de fr it ja zh pt); for table cells, never for text that contains a table."""
    parts = [x.strip() for x in s.split(" | ")]
    assert len(parts) == 8, s
    return P(*parts)
