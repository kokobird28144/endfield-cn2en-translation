# 翻译规范与歧义处理

## 名称和简称

先使用 [community-aliases.md](community-aliases.md) 中的历史别名候选核对当前语义，再查 [game-terms.md](game-terms.md) 和 [official-names.md](official-names.md) 的名称配对。社区用语另查 [community-slang.md](community-slang.md)，机制术语查 [production-terms.md](production-terms.md)。所有局部读法都须与当前文档匹配，不携带作者或章节专用译名。

| 原文形式 | 处理方式 | 依据或限制 |
| --- | --- | --- |
| 小药 | 普通芽针针剂 → Yazhen Syringe [C]，或锦草软饮 → Jincao Drink | 用户确认两候选，按植物/配方判断；不固定为芽针针剂，不与优质[A]/Jincao Tea混淆 |
| 蓝药 | 武陵已明确配方中为芽针针剂 → Yazhen Syringe [C] | 不能把小药的两候选反向推广到全部蓝药；不按颜色猜成[B] |
| 大药、紫药 | 先核实是否优质芽针针剂 → Yazhen Syringe [A] | 只有配方或上下文能确认时才展开 |
| 中电、中容、中融武陵电池 | 武陵语境通常为中容武陵电池 → SC Wuling Battery | “中融”疑为笔误；涉及谷地时应为 SC Valley Battery，不能省略地区 |
| 蓝铁、铁 | 根据采矿、精炼、粉碎环节区分 Ferrium Ore / Ferrium / Ferrium Powder | “120蓝铁”可能表示原矿供给，不能一律改为 Ferrium；单位缺失时依上下文，不凭空补数值 |
| 赤铜、铜 | 区分 Cuprium Ore / Cuprium / Cuprium Powder | 不是普通 copper 的自动替换 |
| 灼铜、赫铜 | 指块状物料时 Pyrrolite / Hetonite | 灼件、赫件分别为 Pyrrolite Part / Hetonite Part |
| 息壤、壤晶 | Xiranite / Xircon | 两种不同物料，不可合并；“壤”单字简称仅在明确上下文中展开 |
| 废液 | 可能指 Xircon Effluent，也可能泛指废液 | 与惰性壤晶废液 Inert Xircon Effluent、污水 Sewage 分开；不要丢掉 Inert |
| 水 | 在相应反应配方中通常为清水 → Clean Water | 泛指水的物理性质时可用 water |
| 箱子、储存箱、存储箱 | 具体设施为 Protocol Stash；泛指箱式容器可用 storage box | 与 depot 和机器 buffer 区分 |
| 准入口、限速口 | 固体 Item Control Port；液体 Pipe Control Port | 上下文不明确时用 control port 并记待核，不翻译为 quasi-inlet |
| 洪炉、烘炉 | 确认指天有洪炉时 Forge of the Sky | 不因“炉”字把精炼炉 Refining Unit 也合并进来 |
| 液气机、固气机 | Fluid-Gas Transmuting Unit / Solid-Gas Transmuting Unit | 机械简称可在第一次全称之后简化为 transmuter，需避免歧义 |
| 存货口、存入口、取货口、出货口 | 仓库方向以 Depot Loader / Depot Unloader 表达 | 存入仓库是 Loader，取出仓库是 Unloader；机器出货口则为 output port |
| 暗管 | conduit | 专用入口/出口按 Conduit Inlet / Outlet；不能把普通地下概念一律替换为游戏设备 |
| 富集气 | 未在本次表中确认唯一同名物品；读配方后判断 | 不自动等同 Heavy Xiragen；可保留“富集气”并注明待核 |
| 绿矿及未登记的活动简称 | 查询对应版本、配方和上下文 | 颜色不足以确定游戏物品 ID；红矿等已登记别名按独立表处理 |

协议核心在同一版本的物品表显示 `Protocol Automation-Core (PAC)`，建筑表显示 `Automation-Core`。本词表以物品表作规范全称；翻译具体界面截图时尊重该界面名称，不能宣称两张表完全相同。

土豆苔/豆苔的用户解释仍是平薯叶/球豆壳的暂定候选；必须区分未粉碎副产物与Leaf/Pod Powder，不能凭内部moss字段直译苔。自动收割机已确认是具体游戏设备，只有英文正式名仍待配对。集成实训装备是实际AIC Fieldwork装备类别。双口的可能含义见独立别名表，计数与方向根据当前段落判断。

## 状态、数量和时序

- `30/min` 表示平均速率时写 `30 units/min`（固体可用 `items/min`）。只有原文明确均匀到达，才写 `one unit every 2 s`。不要把平均值补写成均匀节拍。
- `1 tick = 2 秒` 是部分文档的归一化约定，不能推广为引擎更新频率。其他章节的 tick 必须跟随当地定义。
- 完成反应是 `complete the reaction`；完成产物落地是 `transfer completed products from the completion buffer into the machine's material inventory`；从机器运走才是 `output/export`。落地不是地面掉落。
- 缺料是 `input starvation`；出料空间不足是 `output blocking`。`blocked` 不直接等于 `deadlocked`；后者需构成无法自行恢复的循环依赖。
- `15-`、`15+` 在流量理论中是有语义的标记，照抄并译出作者定义，不能作为排版错误删除。
- `毛产`、`净产` 要按原文确认是否扣除耗材、供电或自用；物品产率用 `gross/net production rate`，调度券收益用 `gross/net revenue`。不自行指定扣除口径。
- 气体名称、环境名称、设备工作模式是不同概念，不能拿 `Xiragen` 代替所有含“息壤”的环境或模式。

## 保持研究语气

| 中文 | 合适的英语表达 |
| --- | --- |
| 本轮观察到 | was observed in the present test |
| 在该条件下可以推断 | under these conditions, this suggests… |
| 尚未确定 | has not yet been established |
| 推测、猜想 | hypothesis / conjecture（依原文语境） |
| 原因未知 | the cause remains unknown |
| 已过时、已被修复 | outdated / fixed（保留所述版本与时间范围） |

阻尼理论等历史页面标为过时时，照译其历史内容并保留该提示，不用后来的解释替换原文。公式和不等式中的中文说明可以翻译，数学关系不可改变。

## 自编写校订样例

以下文字是虚构的通用技术例句，不引用社区作者或实际游戏机制。

原文：本次试验中，平均输入为 24 件/分钟。尚不能确定物料是否均匀到达。

译文：In this test, the average input rate was 24 items/min. It has not yet been established whether items arrive at uniform intervals.

检查要点：不将平均值改写为每 2.5 秒必到达一件。

原文：只有入口开放且缓冲区有空位时，设备才开始下一批。

译文：The machine starts the next batch only when the inlet is open and space is available in the buffer.

检查要点：两个条件共同成立；“只有”不能丢失。
