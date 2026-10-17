# The facts that do not depend on the language, and the words of every language, of ARMOR-HARDWARE.
# Copyright (C) 2026 JuanenRac (Electro Hobby 3D). GPL-3.0-or-later.

FACTS = {
 "emoji": "🧱",
 "badges": [
  [
   "CAD",
   "OpenSCAD",
   "f9d72c"
  ],
  [
   "Maturity",
   "mechanical%20baseline",
   "FFB020"
  ]
 ],
 "diagram": "",
 "build": "```powershell\nopenscad -o build/node_enclosure_radar.stl scad/node_enclosure_radar.scad\nopenscad -D 'part=\"both\"' -D 'preset=\"alarm\"' -o build/node_box_alarm.stl scad/node_box.scad   # presets: solar, electrical, alarm\n```",
 "structure": "```text\nARMOR-HARDWARE/\n├── scad/   node_enclosure_radar.scad (+ stl, amf, 3mf and two slicer projects: the base and the sliding cover), node_box.scad (the box of the solar, electrical and alarm nodes)\n├── docs/   DESIGN_INPUTS, VALIDATION, BENCH_ACCEPTANCE\n└── images/ brand assets\n```",
 "requirements": [
  "OpenSCAD 2021.01+ (to render the enclosures)",
  "a 3D printer (FDM) to try them"
 ]
}

TEXT = {
 "en": {
  "tagline": "Enclosures, electronics and the bench acceptance matrix",
  "honest": "The radar enclosure is a **printable mechanical starting point, not an IP, RF or thermal rating**, and the parametric box for the solar, electrical and alarm nodes is checked by the asserts of its source (the board fits, the cable holes fit, the lid clears the posts), but **none has been printed or measured** (the board sizes come from data sheets; the touch panel has no printed box, it keeps its factory enclosure). Every row of the [bench acceptance matrix](docs/BENCH_ACCEPTANCE.md) is *not tested*.",
  "bullets": [
   "**The radar enclosure is `scad/node_enclosure_radar.scad`** (with STL, 3MF and AMF exports and two slicer projects, the base and the sliding cover): a 90-degree corner base with a visor, roof and floor, retaining steps, a sliding 2 mm front cover and side flaps, all driven by named parameters.",
   "**A parametric box for the solar, electrical and alarm nodes** (`scad/node_box.scad`, presets `solar`, `electrical` and `alarm`): walls, posts for the board, cable-gland holes, a vent, a pocket for a tamper micro-switch under the lid and a lid with a ring-shaped lip. It is a low-voltage box, not an enclosure for mains wiring.",
   "**Holders** for three radar modules, a cable gland and drain holes. There are no volumes yet for the ESP32-S3-ETH-PoE board, the PoE magnetics, the PTC heater or the light-sensor window that the bench matrix wants to test. No metallic, conductive or carbon-loaded material in front of a 24 GHz aperture without measuring it first.",
   "**Bench acceptance matrix:** the radio, environment, power, network and camera checks with a method and a proposed pass criterion each, and a camera compatibility table to fill in.",
   "Before fabrication, record exact board outlines, connectors, screw positions, antenna keep-outs, the thermal path and the ingress target ([design inputs](docs/DESIGN_INPUTS.md))."
  ],
  "note": "See the [validation boundary](docs/VALIDATION.md). The intended hardware licence is CERN-OHL-S-2.0; add its full text before releasing the designs.",
  "fit": "ARMOR-HARDWARE is what holds the nodes. It carries the enclosure of the radar node, the parametric box of the solar, electrical, alarm and touch-panel nodes, and the bench acceptance matrix that says how a prototype is to be judged before it goes on a wall. Its designs are the starting point for the boards that [ARMOR-RADAR](https://github.com/JuanenRac/ARMOR-RADAR), [ARMOR-SOLAR](https://github.com/JuanenRac/ARMOR-SOLAR), [ARMOR-ELECTRICAL](https://github.com/JuanenRac/ARMOR-ELECTRICAL), [ARMOR-ALARM](https://github.com/JuanenRac/ARMOR-ALARM) and [ARMOR-HMI](https://github.com/JuanenRac/ARMOR-HMI) run on.",
  "hardware": "None yet: nothing has been printed or measured; the three boxes are only checked by the asserts of their source"
 },
 "es": {
  "tagline": "Carcasas, electrónica y la matriz de aceptación de banco",
  "honest": "La carcasa del radar es un **punto de partida mecánico imprimible, no una clasificación IP, RF ni térmica**, y la caja paramétrica para los nodos solar, eléctrico y de alarma está comprobada por los `assert` de su fuente (la placa cabe, los agujeros de cables caben, la tapa libra los postes), pero **ninguna se ha imprimido ni medido** (los tamaños de las placas salen de las hojas de datos; el panel táctil no tiene caja impresa, conserva su carcasa de fábrica). Cada fila de la [matriz de aceptación en banco](docs/BENCH_ACCEPTANCE.md) está *sin probar*.",
  "bullets": [
   "**La carcasa del radar es `scad/node_enclosure_radar.scad`** (con exportaciones STL, 3MF y AMF y dos proyectos de laminador, la base y la tapa corredera): una base de esquina de 90 grados con visera, techo y suelo, escalones de retención, una tapa frontal corredera de 2 mm y aletas laterales, todo gobernado por parámetros con nombre.",
   "**Una caja paramétrica para los nodos solar, eléctrico y de alarma** (`scad/node_box.scad`, preajustes `solar`, `electrical` y `alarm`): paredes, postes para la placa, agujeros para prensaestopas, una ventilación, un hueco para un microinterruptor antisabotaje bajo la tapa y una tapa con labio anular. Es una caja de baja tensión, no una envolvente para cableado de red.",
   "**Soportes** para tres módulos de radar, un prensaestopas y agujeros de drenaje. Todavía no hay volúmenes para la placa ESP32-S3-ETH-PoE, la magnética PoE, el calefactor PTC ni la ventana del sensor de luz que la matriz de banco quiere probar. Ningún material metálico, conductor o cargado de carbono delante de una apertura de 24 GHz sin medirlo antes.",
   "**Matriz de aceptación en banco:** las comprobaciones de radio, entorno, alimentación, red y cámara con un método y un criterio de aprobado propuesto cada una, y una tabla de compatibilidad de cámaras por rellenar.",
   "Antes de fabricar, anota los contornos exactos de las placas, conectores, posiciones de tornillos, zonas libres de antena, el camino térmico y el objetivo de protección ([datos de diseño](docs/DESIGN_INPUTS.md))."
  ],
  "note": "Véase el [límite de validación](docs/VALIDATION.md). La licencia de hardware prevista es CERN-OHL-S-2.0; añade su texto completo antes de publicar los diseños.",
  "fit": "ARMOR-HARDWARE es lo que contiene a los nodos. Lleva la carcasa del nodo radar, la caja paramétrica de los nodos solar, eléctrico, de alarma y de panel táctil, y la matriz de aceptación en banco que dice cómo juzgar un prototipo antes de ponerlo en una pared. Sus diseños son el punto de partida para las placas en las que corren [ARMOR-RADAR](https://github.com/JuanenRac/ARMOR-RADAR), [ARMOR-SOLAR](https://github.com/JuanenRac/ARMOR-SOLAR), [ARMOR-ELECTRICAL](https://github.com/JuanenRac/ARMOR-ELECTRICAL), [ARMOR-ALARM](https://github.com/JuanenRac/ARMOR-ALARM) y [ARMOR-HMI](https://github.com/JuanenRac/ARMOR-HMI).",
  "hardware": "Ninguno todavía: nada se ha impreso ni medido; las tres cajas solo las comprueban los `assert` de su fuente"
 },
 "fr": {
  "tagline": "Boîtiers, électronique et matrice d'acceptation sur banc",
  "honest": "Le boîtier du radar est un **point de départ mécanique imprimable, pas un classement IP, RF ou thermique**, et la boîte paramétrique pour les nœuds solaire, électrique et alarme est vérifiée par les `assert` de sa source (la carte tient, les trous de câbles tiennent, le couvercle dégage les plots), mais **aucune n'a été imprimée ni mesurée** (les dimensions des cartes viennent des fiches techniques ; le panneau tactile n'a pas de boîte imprimée, il garde son boîtier d'origine). Chaque ligne de la [matrice d'acceptation sur banc](docs/BENCH_ACCEPTANCE.md) est *non testée*.",
  "bullets": [
   "**Le boîtier du radar est `scad/node_enclosure_radar.scad`** (avec exports STL, 3MF et AMF et deux projets de trancheur, la base et le couvercle coulissant) : une base d'angle à 90 degrés avec visière, toit et plancher, des gradins de retenue, un couvercle avant coulissant de 2 mm et des volets latéraux, le tout piloté par des paramètres nommés.",
   "**Une boîte paramétrique pour les nœuds solaire, électrique et alarme** (`scad/node_box.scad`, préréglages `solar`, `electrical` et `alarm`) : parois, plots pour la carte, trous de presse-étoupe, une aération, un logement pour un micro-interrupteur anti-sabotage sous le couvercle et un couvercle à lèvre annulaire. C'est une boîte basse tension, pas un coffret pour câblage secteur.",
   "**Supports** pour trois modules radar, un presse-étoupe et des trous de drainage. Il n'y a pas encore de volumes pour la carte ESP32-S3-ETH-PoE, la magnétique PoE, le chauffage PTC ni la fenêtre du capteur de lumière que la matrice de banc veut tester. Aucun matériau métallique, conducteur ou chargé de carbone devant une ouverture 24 GHz sans l'avoir mesuré.",
   "**Matrice d'acceptation sur banc :** les contrôles radio, environnement, alimentation, réseau et caméra avec une méthode et un critère de réussite proposé chacun, et un tableau de compatibilité des caméras à remplir.",
   "Avant fabrication, notez les contours exacts des cartes, les connecteurs, les positions de vis, les zones libres d'antenne, le chemin thermique et l'objectif de protection ([données de conception](docs/DESIGN_INPUTS.md))."
  ],
  "note": "Voir la [frontière de validation](docs/VALIDATION.md). La licence matérielle prévue est CERN-OHL-S-2.0 ; ajoutez son texte complet avant de publier les conceptions.",
  "fit": "ARMOR-HARDWARE est ce qui contient les nœuds. Il porte le boîtier du nœud radar, la boîte paramétrique des nœuds solaire, électrique, alarme et panneau tactile, et la matrice d'acceptation sur banc qui dit comment juger un prototype avant de le mettre au mur. Ses conceptions sont le point de départ des cartes sur lesquelles tournent [ARMOR-RADAR](https://github.com/JuanenRac/ARMOR-RADAR), [ARMOR-SOLAR](https://github.com/JuanenRac/ARMOR-SOLAR), [ARMOR-ELECTRICAL](https://github.com/JuanenRac/ARMOR-ELECTRICAL), [ARMOR-ALARM](https://github.com/JuanenRac/ARMOR-ALARM) et [ARMOR-HMI](https://github.com/JuanenRac/ARMOR-HMI).",
  "hardware": "Aucun pour l'instant : rien n'a été imprimé ni mesuré ; les trois boîtes ne sont vérifiées que par les `assert` de leur source"
 },
 "it": {
  "tagline": "Contenitori, elettronica e matrice di accettazione da banco",
  "honest": "L'involucro del radar è un **punto di partenza meccanico stampabile, non una classificazione IP, RF o termica**, e la scatola parametrica per i nodi solare, elettrico e allarme è verificata dagli `assert` del suo sorgente (la scheda ci sta, i fori dei cavi ci stanno, il coperchio libera le colonnine), ma **nessuna è stata stampata né misurata** (le dimensioni delle schede vengono dai datasheet; il pannello touch non ha una scatola stampata, mantiene il suo involucro di fabbrica). Ogni riga della [matrice di accettazione al banco](docs/BENCH_ACCEPTANCE.md) è *non provata*.",
  "bullets": [
   "**L'involucro del radar è `scad/node_enclosure_radar.scad`** (con esportazioni STL, 3MF e AMF e due progetti dello slicer, la base e il coperchio scorrevole): una base d'angolo a 90 gradi con visiera, tetto e pavimento, gradini di ritenuta, un coperchio frontale scorrevole da 2 mm e alette laterali, tutto governato da parametri con nome.",
   "**Una scatola parametrica per i nodi solare, elettrico e allarme** (`scad/node_box.scad`, preset `solar`, `electrical` e `alarm`): pareti, colonnine per la scheda, fori per pressacavi, una ventilazione, un alloggiamento per un microinterruttore antimanomissione sotto il coperchio e un coperchio con labbro ad anello. È una scatola a bassa tensione, non un involucro per cablaggio di rete.",
   "**Supporti** per tre moduli radar, un pressacavo e fori di drenaggio. Non ci sono ancora volumi per la scheda ESP32-S3-ETH-PoE, la magnetica PoE, il riscaldatore PTC né la finestra del sensore di luce che la matrice di banco vuole provare. Nessun materiale metallico, conduttivo o caricato con carbonio davanti a un'apertura a 24 GHz senza averlo misurato.",
   "**Matrice di accettazione al banco:** i controlli di radio, ambiente, alimentazione, rete e telecamera con un metodo e un criterio di superamento proposto ciascuno, e una tabella di compatibilità delle telecamere da compilare.",
   "Prima della fabbricazione, registra i contorni esatti delle schede, i connettori, le posizioni delle viti, le zone libere d'antenna, il percorso termico e l'obiettivo di protezione ([dati di progetto](docs/DESIGN_INPUTS.md))."
  ],
  "note": "Vedi il [confine di validazione](docs/VALIDATION.md). La licenza hardware prevista è CERN-OHL-S-2.0; aggiungi il suo testo completo prima di pubblicare i progetti.",
  "fit": "ARMOR-HARDWARE è ciò che contiene i nodi. Porta l'involucro del nodo radar, la scatola parametrica dei nodi solare, elettrico, allarme e pannello touch, e la matrice di accettazione al banco che dice come giudicare un prototipo prima di metterlo a una parete. I suoi progetti sono il punto di partenza per le schede su cui girano [ARMOR-RADAR](https://github.com/JuanenRac/ARMOR-RADAR), [ARMOR-SOLAR](https://github.com/JuanenRac/ARMOR-SOLAR), [ARMOR-ELECTRICAL](https://github.com/JuanenRac/ARMOR-ELECTRICAL), [ARMOR-ALARM](https://github.com/JuanenRac/ARMOR-ALARM) e [ARMOR-HMI](https://github.com/JuanenRac/ARMOR-HMI).",
  "hardware": "Ancora nessuno: nulla è stato stampato né misurato; le tre scatole sono verificate solo dagli `assert` del sorgente"
 },
 "de": {
  "tagline": "Gehäuse, Elektronik und die Abnahmematrix am Prüfstand",
  "honest": "Das Radargehäuse ist ein **druckbarer mechanischer Ausgangspunkt, keine IP-, HF- oder Thermikeinstufung**, und die parametrische Box für die Knoten Solar, Elektro und Alarm wird von den `assert`-Prüfungen ihres Quelltexts geprüft (die Platine passt, die Kabellöcher passen, der Deckel liegt frei von den Pfosten), aber **keine wurde gedruckt oder vermessen** (die Platinengrößen stammen aus Datenblättern; das Touchpanel hat keine gedruckte Box, es behält sein Werksgehäuse). Jede Zeile der [Prüfstand-Abnahmematrix](docs/BENCH_ACCEPTANCE.md) ist *ungetestet*.",
  "bullets": [
   "**Das Radargehäuse ist `scad/node_enclosure_radar.scad`** (mit STL-, 3MF- und AMF-Exporten und zwei Slicer-Projekten, der Basis und dem Schiebedeckel): eine 90-Grad-Eckbasis mit Blende, Dach und Boden, Haltestufen, einem 2 mm dicken Schiebedeckel vorn und Seitenklappen, alles über benannte Parameter gesteuert.",
   "**Eine parametrische Box für die Knoten Solar, Elektro und Alarm** (`scad/node_box.scad`, Voreinstellungen `solar`, `electrical` und `alarm`): Wände, Pfosten für die Platine, Löcher für Kabelverschraubungen, eine Lüftung, eine Aufnahme für einen Sabotage-Mikroschalter unter dem Deckel und ein Deckel mit ringförmiger Lippe. Es ist eine Kleinspannungsbox, kein Gehäuse für Netzverdrahtung.",
   "**Halter** für drei Radarmodule, eine Kabelverschraubung und Ablaufbohrungen. Für die Platine ESP32-S3-ETH-PoE, die PoE-Magnetik, die PTC-Heizung und das Lichtsensorfenster, die die Prüfstandmatrix testen will, gibt es noch keine Volumina. Kein metallisches, leitendes oder kohlenstoffhaltiges Material vor einer 24-GHz-Öffnung, ohne es vorher zu messen.",
   "**Prüfstand-Abnahmematrix:** die Prüfungen für Funk, Umgebung, Stromversorgung, Netzwerk und Kamera, jeweils mit Methode und vorgeschlagenem Bestehenskriterium, und eine auszufüllende Kamera-Kompatibilitätstabelle.",
   "Vor der Fertigung genaue Platinenumrisse, Steckverbinder, Schraubpositionen, Antennenfreiräume, den Wärmepfad und das Schutzziel festhalten ([Entwurfsangaben](docs/DESIGN_INPUTS.md))."
  ],
  "note": "Siehe die [Validierungsgrenze](docs/VALIDATION.md). Die vorgesehene Hardware-Lizenz ist CERN-OHL-S-2.0; fügen Sie ihren vollständigen Text hinzu, bevor Sie die Entwürfe veröffentlichen.",
  "fit": "ARMOR-HARDWARE ist das, was die Knoten hält. Es enthält das Gehäuse des Radarknotens, die parametrische Box der Knoten Solar, Elektro, Alarm und Touchpanel und die Abnahmematrix, die sagt, wie ein Prototyp beurteilt wird, bevor er an die Wand kommt. Seine Entwürfe sind der Ausgangspunkt für die Platinen, auf denen [ARMOR-RADAR](https://github.com/JuanenRac/ARMOR-RADAR), [ARMOR-SOLAR](https://github.com/JuanenRac/ARMOR-SOLAR), [ARMOR-ELECTRICAL](https://github.com/JuanenRac/ARMOR-ELECTRICAL), [ARMOR-ALARM](https://github.com/JuanenRac/ARMOR-ALARM) und [ARMOR-HMI](https://github.com/JuanenRac/ARMOR-HMI) laufen.",
  "hardware": "Noch keiner: nichts wurde gedruckt oder vermessen; die drei Boxen werden nur durch die `assert`-Prüfungen ihres Quelltexts geprüft"
 },
 "zh": {
  "tagline": "外壳、电子器件和台架验收矩阵",
  "honest": "雷达外壳是**可打印的机械起点，不是 IP、射频或热学等级**；用于太阳能、电气和报警节点的参数化盒子由其源文件中的 `assert` 检查（板子放得下、电缆孔放得下、盖子避开立柱），但**都没有打印或测量过**（板子尺寸来自数据手册；触摸屏没有打印的盒子，沿用出厂外壳）。[台架验收矩阵](docs/BENCH_ACCEPTANCE.md)的每一行都是*未测试*。",
  "bullets": [
   "**雷达外壳是 `scad/node_enclosure_radar.scad`**（带 STL、3MF 和 AMF 导出以及两个切片项目：底座和滑动盖）：带遮阳罩、顶和底的 90 度转角底座、固定台阶、2 毫米的滑动前盖和侧翼，全部由命名参数驱动。",
   "**用于太阳能、电气和报警节点的参数化盒子**（`scad/node_box.scad`，预设 `solar`、`electrical` 和 `alarm`）：墙壁、板子立柱、电缆格兰头孔、通风孔、盖下的防拆微动开关槽，以及带环形唇边的盖子。这是低压盒子，不是市电布线的外壳。",
   "**支架**用于三个雷达模块、一个电缆格兰头和排水孔。台架矩阵要测试的 ESP32-S3-ETH-PoE 板、PoE 磁件、PTC 加热器和光传感器窗口还没有预留空间。未经测量，24 GHz 孔径前不要放置金属、导电或含碳的材料。",
   "**台架验收矩阵：**射频、环境、电源、网络和摄像头检查，每项都有方法和建议的通过标准，另有待填写的摄像头兼容性表。",
   "制造之前，记录板子的确切轮廓、连接器、螺丝位置、天线净空区、热路径和防护目标（[设计输入](docs/DESIGN_INPUTS.md)）。"
  ],
  "note": "参见[验证边界](docs/VALIDATION.md)。预期的硬件许可证是 CERN-OHL-S-2.0；发布设计前请加入其完整文本。",
  "fit": "ARMOR-HARDWARE 是容纳各节点的部分。它包含雷达节点的外壳、太阳能、电气、报警和触摸屏节点的参数化盒子，以及说明原型上墙前如何评判的台架验收矩阵。它的设计是 [ARMOR-RADAR](https://github.com/JuanenRac/ARMOR-RADAR)、[ARMOR-SOLAR](https://github.com/JuanenRac/ARMOR-SOLAR)、[ARMOR-ELECTRICAL](https://github.com/JuanenRac/ARMOR-ELECTRICAL)、[ARMOR-ALARM](https://github.com/JuanenRac/ARMOR-ALARM) 和 [ARMOR-HMI](https://github.com/JuanenRac/ARMOR-HMI) 所运行的板子的起点。",
  "hardware": "暂无：没有任何东西被打印或测量过；三个盒子只由源文件中的 `assert` 检查"
 },
 "ja": {
  "tagline": "筐体、電子部品、ベンチ受け入れマトリクス",
  "honest": "レーダーの筐体は**印刷できる機構の出発点であり、IP・RF・熱の等級ではなく**、太陽光・電気・警報ノード用のパラメトリックボックスはソースの `assert` で検査されています（基板が収まる、ケーブル穴が収まる、蓋がポストを避ける）が、**どれも印刷も計測もされていません**（基板の寸法はデータシート由来で、タッチパネルには印刷ボックスはなく、出荷時の筐体を使います）。[ベンチ受入マトリクス](docs/BENCH_ACCEPTANCE.md)のすべての行は*未テスト*です。",
  "bullets": [
   "**レーダーの筐体は `scad/node_enclosure_radar.scad`**（STL・3MF・AMF の出力と、ベースとスライドカバーの 2 つのスライサープロジェクト付き）：バイザー、屋根、床、固定用の段差、2 mm のスライド式フロントカバー、側面フラップを備えた 90 度コーナーのベースで、すべて名前付きパラメーターで動きます。",
   "**太陽光・電気・警報ノード用のパラメトリックボックス**（`scad/node_box.scad`、プリセット `solar`、`electrical`、`alarm`）：壁、基板用のポスト、ケーブルグランド用の穴、通気口、蓋の下の改ざん検知マイクロスイッチ用ポケット、リング状のリップ付きの蓋。低電圧用のボックスであり、商用電源配線用の筐体ではありません。",
   "**ホルダー**：3 つのレーダーモジュール、ケーブルグランド、排水穴用。ベンチマトリクスが試験したい ESP32-S3-ETH-PoE 基板、PoE マグネティクス、PTC ヒーター、光センサー窓の空間はまだありません。24 GHz の開口の前には、測定せずに金属・導電性・カーボン入りの材料を置かないでください。",
   "**ベンチ受入マトリクス：**無線、環境、電源、ネットワーク、カメラの検査それぞれに方法と合格基準の案があり、記入するカメラ互換表もあります。",
   "製作前に、基板の正確な外形、コネクター、ネジ位置、アンテナの禁止領域、熱経路、侵入保護の目標を記録します（[設計入力](docs/DESIGN_INPUTS.md)）。"
  ],
  "note": "[検証の境界](docs/VALIDATION.md)を参照してください。想定しているハードウェアライセンスは CERN-OHL-S-2.0 で、設計を公開する前に全文を追加してください。",
  "fit": "ARMOR-HARDWARE はノードを収めるものです。レーダーノードの筐体、太陽光・電気・警報・タッチパネルノードのパラメトリックボックス、壁に付ける前に試作品をどう評価するかを示すベンチ受入マトリクスを含みます。その設計は、[ARMOR-RADAR](https://github.com/JuanenRac/ARMOR-RADAR)、[ARMOR-SOLAR](https://github.com/JuanenRac/ARMOR-SOLAR)、[ARMOR-ELECTRICAL](https://github.com/JuanenRac/ARMOR-ELECTRICAL)、[ARMOR-ALARM](https://github.com/JuanenRac/ARMOR-ALARM)、[ARMOR-HMI](https://github.com/JuanenRac/ARMOR-HMI) が動く基板の出発点です。",
  "hardware": "まだありません：何も印刷も計測もされていません。3 つのボックスはソースの `assert` で検査されているだけです"
 },
 "pt": {
  "tagline": "Caixas, eletrónica e a matriz de aceitação de bancada",
  "honest": "A caixa do radar é um **ponto de partida mecânico imprimível, não uma classificação IP, RF ou térmica**, e a caixa paramétrica para os nós solar, elétrico e de alarme é verificada pelos `assert` do seu código (a placa cabe, os furos dos cabos cabem, a tampa liberta os pilares), mas **nenhuma foi impressa nem medida** (os tamanhos das placas vêm das folhas de dados; o painel tátil não tem caixa impressa, mantém a sua caixa de fábrica). Cada linha da [matriz de aceitação em bancada](docs/BENCH_ACCEPTANCE.md) está *por testar*.",
  "bullets": [
   "**A caixa do radar é `scad/node_enclosure_radar.scad`** (com exportações STL, 3MF e AMF e dois projetos de fatiador, a base e a tampa deslizante): uma base de canto de 90 graus com viseira, teto e chão, degraus de retenção, uma tampa frontal deslizante de 2 mm e abas laterais, tudo governado por parâmetros com nome.",
   "**Uma caixa paramétrica para os nós solar, elétrico e de alarme** (`scad/node_box.scad`, predefinidos `solar`, `electrical` e `alarm`): paredes, pilares para a placa, furos para bucins, uma ventilação, um espaço para um microinterruptor antissabotagem sob a tampa e uma tampa com lábio anular. É uma caixa de baixa tensão, não um invólucro para cablagem de rede.",
   "**Suportes** para três módulos de radar, um bucim e furos de drenagem. Ainda não há volumes para a placa ESP32-S3-ETH-PoE, a magnética PoE, o aquecedor PTC nem a janela do sensor de luz que a matriz de bancada quer testar. Nenhum material metálico, condutor ou carregado de carbono à frente de uma abertura de 24 GHz sem o medir.",
   "**Matriz de aceitação em bancada:** as verificações de rádio, ambiente, alimentação, rede e câmara com um método e um critério de aprovação proposto cada uma, e uma tabela de compatibilidade de câmaras por preencher.",
   "Antes de fabricar, registe os contornos exatos das placas, conectores, posições de parafusos, zonas livres de antena, o caminho térmico e o objetivo de proteção ([dados de desenho](docs/DESIGN_INPUTS.md))."
  ],
  "note": "Veja o [limite de validação](docs/VALIDATION.md). A licença de hardware prevista é CERN-OHL-S-2.0; acrescente o seu texto completo antes de publicar os desenhos.",
  "fit": "O ARMOR-HARDWARE é o que contém os nós. Leva a caixa do nó radar, a caixa paramétrica dos nós solar, elétrico, de alarme e de painel tátil, e a matriz de aceitação em bancada que diz como julgar um protótipo antes de o pôr numa parede. Os seus desenhos são o ponto de partida para as placas em que correm o [ARMOR-RADAR](https://github.com/JuanenRac/ARMOR-RADAR), o [ARMOR-SOLAR](https://github.com/JuanenRac/ARMOR-SOLAR), o [ARMOR-ELECTRICAL](https://github.com/JuanenRac/ARMOR-ELECTRICAL), o [ARMOR-ALARM](https://github.com/JuanenRac/ARMOR-ALARM) e o [ARMOR-HMI](https://github.com/JuanenRac/ARMOR-HMI).",
  "hardware": "Nenhum ainda: nada foi impresso nem medido; as três caixas só são verificadas pelos `assert` do seu código"
 }
}
