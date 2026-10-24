# 版本、地名与界面名称核验

核验日期：2026-10-19。发行商官网用语与同版本CN/EN字符串交叉核对。官网是发布方一手资料；本地游戏表来自社区镜像，二者来源身份不混同。完整name_id、原字符串和证据状态见 [official-names.json](official-names.json)，文件哈希见 [data-provenance-1.6.4.json](data-provenance-1.6.4.json)。

## 版本标题

| 中文 | 采用英文 | 证据及使用边界 |
| --- | --- | --- |
| 零号委托 | Zeroth Directive | [官方资料1](https://endfield.gryphline.com/en-us/news/3846)；同ID本地化配对。 |
| 新潮起，故渊离 | Old Deep Water Dies, by Rising Tide It is Denied | [官方资料1](https://endfield.gryphline.com/en-us/news/8907)；同ID本地化配对。 |
| 春晓时 | At the Wake of Spring | [官方资料1](https://endfield.gryphline.com/en-us/news/0751)；同ID本地化配对。 |
| 寻遗散记 | Sketches of Lost Heirlooms | [官方资料1](https://endfield.gryphline.com/en-us/news/0758)；同ID本地化配对。 |
| 向渊行 | Homecoming | [官方资料1](https://endfield.gryphline.com/en-us/news/5200)；同ID本地化配对。 |
| 雪凇幽梦 | Dreamscape of Wind and Snow | [官方资料1](https://endfield.gryphline.com/en-us/news/5209)；同ID本地化配对。 |
| 丹青渡 | Sanctuary of Ink | [官方资料1](https://endfield.gryphline.com/en-us/news/0744)；同ID本地化配对。 |

## 地区与地点

| 中文 | 采用英文 | 证据及使用边界 |
| --- | --- | --- |
| 景玉谷 | Jingyu Valley | 同ID本地化配对；无本轮找到的官网直接名称证据。已检索发行商官网，未找到独立公告短名称证据；采用同版本游戏文本配对，不称官网直接确认。 |
| 首墩 | Marker Stone | [官方资料1](https://endfield.gryphline.com/en-us/news/0751)；同ID本地化配对。 |
| 应龙关 | Yinglung Pass | [官方资料1](https://endfield.gryphline.com/en-us/news/5200)；同ID本地化配对。 |
| 北部禁区 | North Wuling Exclusion Zone | [官方资料1](https://endfield.gryphline.com/en-us/news/5200)；同ID本地化配对。 |
| 盈天台 | Xiranflow Cloudseeder | [官方资料1](https://endfield.gryphline.com/en-us/news/5200)；同ID本地化配对。地点短名为Xiranflow Cloudseeder；官方公告的完整据点名为Xiranflow Cloudseeder Station，按原文是否含建设站区分。 |
| 天王坪 | Sky King Flats | [官方资料1](https://endfield.gryphline.com/en-us/news/0758)；同ID本地化配对。地点短名Sky King Flats；援建点为Sky King Flats Construction Site，不能把后缀无条件加给地点。 |
| 武陵 | Wuling | [官方资料1](https://endfield.gryphline.com/en-us/news/5200)；同ID本地化配对。 |
| 四号谷地 | Valley IV | [官方资料1](https://endfield.gryphline.com/en-us/news/5200)；同ID本地化配对。 |

## 界面、载具与货品

| 中文 | 采用英文 | 证据及使用边界 |
| --- | --- | --- |
| 弹性物资 | elastic goods | [官方资料1](https://endfield.gryphline.com/en-us/news/0758)；同ID本地化配对。正文通用名小写；标题按标题大小写处理，不重新意译。 |
| 帝江号 | Dijiang | [官方资料1](https://endfield.gryphline.com/en-us)；[官方资料2](https://endfield.gryphline.com/en-us/news/5200)；同ID本地化配对。官网设定页完整称呼OMV Dijiang；日常访问/舱室等正文可用Dijiang。 |
| 气矿 | Gas Vent | 同ID本地化配对；无本轮找到的官网直接名称证据。用户确认指气体矿点，不是气态矿物；泛称可小写gas vent，明确气种时为Xiragen/Inergen vent。 |
| 净水节点 | Purification Node | [官方资料1](https://endfield.gryphline.com/en-us/news/0751)；同ID本地化配对。游戏界面/任务同名，避免Clean Water node混淆清水物品。 |
| 岳研避瘴茶 | Eureka Anti-smog Tincture | 同ID本地化配对；无本轮找到的官网直接名称证据。避瘴茶检索命中真实游戏名；现有数据不支持岳研为笔误。货组全称另见物品表Eureka Anti-smog Tincture [pkg]。 |

## 茶名与笔误判定

按“避瘴茶”检索，ItemTable的item_domainshop_cargo_jinlong_2对应完整中文“岳研避瘴茶货组”，同名ID英文为Eureka Anti-smog Tincture [pkg]；对话字符串6483378646732934334另含不带货组的“岳研避瘴茶 / Eureka Anti-smog Tincture”。因此现有数据支持“岳研”原名，不按笔误改字。“[pkg]”仅用于货组物品，正文谈茶时用不带该后缀的名称。

浸雾大臂是用户确认的浸雾大弩笔误；正式名称Haze-Soaked Ballista，物品item_drop_hvybow_1，name_id=-4437120287885568703。

地区短名、据点全名和泛称分开使用。Dijiang是官方正文常用短名，官网设定全称为OMV Dijiang；elastic goods也有官网正文证据，不再标为作者暂译。

## 用户补充后的地点及装备类别核验

以下仅以本地1.6.4同ID双语数据配对为证据，不冒充官网直接确认。

| 中文 | 采用英文 | 证据及使用边界 |
| --- | --- | --- |
| 心脏修缮站 | Cardiac Remediation Station | name_id=8530199970258623820；用户确认心脏站简称指此据点，勿译Heart Station。 |
| 集成实训 | AIC Fieldwork | name_id=4545517051165535353；实际装备类别，正文集成实训装备可写AIC Fieldwork gear，不直译training equipment。 |
| 集成实训装备组 | AIC Fieldwork Gear Pack | name_id=5836356262880106218；完整界面类名；原文只有集成实训装备时不强加Gear Pack后缀。 |

## 本轮审校的界面名称

以下仅同版本本地化数据配对，非本轮官网直接查询证据。

| 中文 | 采用英文 | 文本ID及边界 |
| --- | --- | --- |
| 调度券 | Stock Bill | 6456409470881217971；同版本完整CN/EN按精确字符串ID配对；泛指调度动作不机械改作系统名，基质不译数学matrix。 |
| 物资调度 | Stock Redistribution | -3743161453472781007；同版本完整CN/EN按精确字符串ID配对；泛指调度动作不机械改作系统名，基质不译数学matrix。 |
| 基质 | Essence | -5883046785278856930；同版本完整CN/EN按精确字符串ID配对；泛指调度动作不机械改作系统名，基质不译数学matrix。 |
| 基质蚀刻 | Essence Etching | 9003259202170401125；同版本完整CN/EN按精确字符串ID配对；泛指调度动作不机械改作系统名，基质不译数学matrix。 |
