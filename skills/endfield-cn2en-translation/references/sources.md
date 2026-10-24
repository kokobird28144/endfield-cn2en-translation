# 来源、版本与维护

本文件记录内置术语的来源、版本与核验方法。使用时按目标文档的游戏版本选择名称。

## 内置数据

| 资料 | 数量与范围 | 历史证据 |
| --- | --- | --- |
| [game-terms.csv](game-terms.csv) / [阅读版](game-terms.md) | 309 条；1.5.3 为 143 条、1.6.4 为 166 条 | 同版本 ItemTable 与 CN/EN 本地化按 name.id 配对 |
| [community-aliases.json](community-aliases.json) / [阅读版](community-aliases.md) | 22 组别名/笔误，包含 2 组暂定解释 | 历史语义澄清，核定日期 2026-10-19；保留适用限制 |
| [community-slang.md](community-slang.md) | 攻略与讨论黑话及候选译法 | 历史观察整理，原记录于 2026-10-21 补充；不声称逐项官方核实 |
| [production-terms.md](production-terms.md) | 完整生产、物流、缓存、时序与模型术语表 | 中文语义背景见 [主题索引](corpus-map.md)，英文是建议译法 |
| [official-names.json](official-names.json) / [阅读版](official-names.md) | 27 条版本、地点、界面及装备类别名称 | 各记录保留官方链接或镜像配对的不同证据等级 |
| [interface-terms-1.6.4.json](interface-terms-1.6.4.json) | 25 条界面/话题名称 | 1.6.4 同 ID 双语配对 |

数据版本为 `1.5.3@10024360-6` 和 `1.6.4@11123848-6`，核验日期见各文件。名称记录包含实体 ID、版本与证据状态；别名记录包含确认状态、候选和适用条件。机制术语以当前文档的定义为准。

## 游戏名称来源与精度

原记录采用社区维护的 AKEDatabase 数据域，而不是把该镜像表述为发行商官方仓库：

- https://github.com/NagiYume/AKEDatabase
- https://data.akedata.wiki/public/1.5.3/10024360-6/TableCfg/ItemTable.json
- https://data.akedata.wiki/public/1.5.3/10024360-6/TableCfg/I18nTextTable_CN.json
- https://data.akedata.wiki/public/1.5.3/10024360-6/TableCfg/I18nTextTable_EN.json
- https://data.akedata.wiki/public/1.6.4/11123848-6/TableCfg/ItemTable.json
- https://data.akedata.wiki/public/1.6.4/11123848-6/TableCfg/I18nTextTable_CN.json
- https://data.akedata.wiki/public/1.6.4/11123848-6/TableCfg/I18nTextTable_EN.json

按 `ItemTable[item_id].name.id → CN[str(id)] / EN[str(id)]` 关联。64 位 ID 用 Python 整数解析，输出时保留为字符串，避免浮点精度损失。原文件的字节数、记录数与 SHA-256 见 [1.5.3 来源记录](data-provenance.json) 和 [1.6.4 来源记录](data-provenance-1.6.4.json)。其中条目数量是历史提取阶段的统计，不能覆盖后来增补后的当前 309 条总量。

来源链接与哈希说明出处，不表示已取得所有第三方内容的统一再许可。正式名称中的官网直接证据、社区镜像配对与暂译不可互相升级；单纯查到一行不能证明当前版本游戏界面已重新核实。

## 更新方法

1. 先确定目标文档的游戏版本，再选同版本数据，不用新版本名称覆盖历史文档。
2. 对齐同一实体/文本 ID 的中英文，区分物品名与建筑界面名；记录来源、版本、取用日期和状态。
3. 同步结构化主表与 Markdown 阅读版。别名保留多候选、暂定与局部范围；机制词服从当前原文定义。
4. 更新发布清单中的数据数量和必要测试。不能为通过检查把缺失英文、来源或语境填成推测的事实。

游戏名称与本地化文本的权利归相应游戏权利方；原创流程、工具与独立说明采用包内 MIT，第三方内容不因这一声明取得新的授权。详细范围见 [NOTICE](../NOTICE) 和 [LICENSE](../LICENSE)。
