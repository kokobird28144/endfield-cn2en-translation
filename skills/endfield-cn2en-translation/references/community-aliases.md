# 玩家别名、简称与原文笔误

收录 23 组别名/笔误与候选，保留确认和暂定状态。核定记录包括 2026-10-19 和 2026-10-31；本发布版整理不等于重新核验当前游戏版本。结构化主表见 [community-aliases.json](community-aliases.json)。

**通用使用边界**：历史用户确认只证明原语料中的读法。新文档须核对地区、配方、设备方向和局部定义；暂定、多候选与笔误条目不进行全局替换。

| 原文形式 | 候选含义与英文 | 历史状态 | 适用规则 |
| --- | --- | --- | --- |
| 可复现可空 | 可复现 → reproducible | 历史确认 | 历史语料曾确认“可复现可空”为多写文字，按“可复现”译为 reproducible。仅当前语境也能支持这一笔误判断时采用；不得在新文档中自动删除“可空”条件。 |
| 浸雾大臂 | 浸雾大弩 → Haze-Soaked Ballista | 历史确认 | 用户确认大臂是大弩笔误。保留中文原件，英译按浸雾大弩。 |
| 红矿 | 赤铜矿 → Cuprium Ore | 历史确认 | 在赤铜矿开采或供给语境中可指赤铜矿 Cuprium Ore；先核对地区、配方与物料阶段，不单凭颜色在新文档中确定矿物。 |
| 铜药 | 优质锦草软饮 → Jincao Tea / 优质芽针针剂 → Yazhen Syringe [A] | 历史确认 | 赤铜块加工得到的药品统称。按地区、植物及配方选择优质锦草软饮或优质芽针针剂；不能固定映射一种药。若仍缺上下文，说明两候选，勿凭颜色猜等级。 |
| 铜块 | 赤铜块 → Cuprium | 历史确认 | 赤铜块别名；与赤铜矿、赤铜粉区分。 |
| 气矿、气体矿点 | 气矿 → Gas Vent | 历史确认 | 指矿点而非物料；明确息壤气/惰气时可写Xiragen vent / Inergen vent。消耗气矿的口语段落须按上下文写该矿点供给的气体，不能把矿点本体送入机器。 |
| 禁区 | 北部禁区 → North Wuling Exclusion Zone | 历史确认 | 本语料一般简称北部禁区。禁区息壤气通常为Xiragen from the North Wuling Exclusion Zone；若句子另有明确禁区指称，尊重该局部定义。 |
| 折金票、折金券 | 折金票 → T-Creds | 历史确认 | 用户确认是同一货币，统一T-Creds；勿与调度券或烟火钱合并。 |
| 玉葫芦 | 息壤玉葫芦 → Xiranite Jade Gourd | 历史确认 | 指息壤玉葫芦，不再使用未识别Jade Gourd。 |
| 紫晶瓶 | 紫晶质瓶 → Amethyst Bottle | 历史确认 | 指紫晶质瓶；根据原文区分空瓶和装有物料的瓶子。 |
| 高晶瓶、晶质瓶 | 高晶质瓶 → Cryston Bottle | 历史确认 | 用户指晶质瓶这一对象；当前数据规范中文为高晶质瓶，英文Cryston Bottle。保留用户含义与数据写法差异，不改成紫晶质瓶。 |
| 钢零件、钢质零件 | 钢制零件 → Steel Part | 历史确认 | 用户指钢质零件这一对象；数据规范中文为钢制零件，英文Steel Part。质/制写法差异不另造物品。 |
| 紫电池 | 高容谷地电池 → HC Valley Battery | 历史确认 | 历史谷地语料指高容谷地电池 HC Valley Battery。新文档须核对地区和等级；不能仅凭颜色排除武陵或其他电池。 |
| 会馆钱 | 烟火钱 → Spirit Money | 历史确认 | 指烟火钱Spirit Money；与T-Creds及Stock Bills/调度券分开。 |
| 小药 | 芽针针剂 → Yazhen Syringe [C] / 锦草软饮 → Jincao Drink | 历史确认 | 普通芽针针剂或锦草软饮的类别简称。按植物、配方与地区选择Yazhen Syringe [C]或Jincao Drink；不固定为芽针针剂，不与铜药对应的优质[A]/Jincao Tea混淆。局部只有标题/图且无法区分时保留两个候选。 |
| 油菜 | 籽油花 → Oilseed Bloom | 历史确认 | 历史种植语料指籽油花 Oilseed Bloom。当前版本和种植对象一致时使用该名称；其他语料先核实植物，不对普通 rapeseed 作全局替换。 |
| 土豆苔 | 平薯叶 → Pingtuber Leaf | 暂定候选 | 用户暂定解释为平薯叶Pingtuber Leaf，原话“应该是”，不是确定物品ID的证据。若实际配方/内部ID指粉末，须区分平薯叶粉末Pingtuber Leaf Powder，不静默删除粉碎加工阶段；保留候选并继续按同版配方核对。 |
| 豆苔 | 球豆壳 → Ballpea Pod | 暂定候选 | 用户暂定解释为球豆壳Ballpea Pod，原话“应该是”，不是确定物品ID的证据。内部item_byproduct_bean_moss_1正式名称为球豆壳粉末Ballpea Pod Powder；依实际配方区分壳与粉末，不凭moss直译苔，也不将两阶段自动合并。 |
| 心脏站 | 心脏修缮站 → Cardiac Remediation Station | 历史确认 | 心脏修缮站简称，使用Cardiac Remediation Station，不再译Heart Station。 |
| 双口 | 两个存货口输入 → two Depot Loader inputs | 历史确认 | 当当前段落明确将“双口”定义为两个存货口输入时，可译为 two Depot Loader inputs；它不是固定设备名。计数按原文限定，不将结构数量、设备数量与端口总数混为一谈；Depot Loader 指输入仓库，方向另按当前系统边界核对。没有明确定义时保留歧义，不从历史方案推断。 |
| 集成实训装备 | 集成实训 → AIC Fieldwork | 历史确认 | 用户确认是实际装备类别，采用AIC Fieldwork gear；不是泛指integrated practical-training equipment。原文为完整“集成实训装备组”时用已配对AIC Fieldwork Gear Pack；具体钢甲/护手等继续查各自名称，不把全类别当作一件装备。 |
| 自动收割机 | 自动收割机 → automatic harvester | 历史确认 | 用户确认是具体游戏设备，不是玩家搭建的自动收获结构。当前同版本本地化尚未定位该中文设备名的精确CN/EN配对，automatic harvester仅暂译；不能仅凭Auto-Harvest功能文字擅自改成Auto-Farmer，也不能再称设备身份不明。 |
| 气体氛围机 | 气体散布机 → Gas Dispersing Unit | 2026-10-31 用户确认 | 指气体散布机的别名；英文使用已有同 ID 配对名称 Gas Dispersing Unit，不再使用 Gas Atmosphere Unit 暂译。保留中文原文别名，不把别名写成官方中文名称；在其他文档中仍核对指代对象。 |

查询名称时另见 [游戏词表](game-terms.md) 与 [正式名称](official-names.md)。确认别名的指代不等于取得其名称的官方证据；正式英文未配对的条目仍保留暂译。
