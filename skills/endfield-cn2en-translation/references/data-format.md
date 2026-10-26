# 本地数据格式

查询工具只读取本地数据。默认逐文件优先读取安装 skill 的 `data/`，缺文件时使用随包 `references/` 中对应的真实词表；显式 `--data-dir` 则只查询指定目录。只加载选定 scope 的文件，不补抓、生成或猜测缺失词条。自用覆盖文件损坏时报告错误，不悄悄改用内置数据。

用户自备数据不因使用本脚本而改变其权利或再分发条件。保留来源、版本、取用时间与证据状态，发布前另行检查许可。

## game-terms.csv

UTF-8 CSV，可带 BOM；必须包含以下表头，允许增加列：

```csv
category,zh,en,aliases_zh,item_id,name_id,version,status,notes
```

`zh`、`en`、`version`、`status` 为非空字符串，其他字段允许为空。`aliases_zh` 用分号分隔。所有字段均以字符串读取，尤其 `name_id` 不转换为浮点数或 JavaScript Number。

查询字段：`zh`、`en`、`item_id`、`name_id` 与 `aliases_zh`。额外列原样返回，不自动参与查询。记录状态由数据维护者提供，命中不意味着脚本核实过来源。

## community-aliases.json

根对象包含 `records` 数组；每条记录包含：

- `aliases`：至少一个非空字符串。
- `meaning_status`：`user-confirmed` 或 `user-suggested`。确认针对指定项目语义，不表示官方命名。
- `rule`：非空字符串，说明适用语境和消歧规则。
- `targets`：至少一个对象，各对象含非空 `zh`、`en`；可另有字符串 `item_id`、`name_id`、`version`、`status`。
- 可选 `user_meaning`、`scope`、`source` 等元数据。

查询字段：别名、`user_meaning`、各候选的 `zh`、`en`、`item_id`、`name_id`。原有确认状态与候选完整保留。

## official-names.json

根对象包含 `records` 数组；每条记录含非空字符串 `zh`、`en`、`version`、`status`，可含字符串 `item_id`、`name_id` 与来源说明等元数据。查询中英文名称及两个 ID。

`official` 是输入数据的分类名，不是查询工具对其真实性的认证。维护者须自行区分官网直接证据、社区镜像配对及其他来源。

## name-index.json

根对象含 `schema_version`（当前为 `1`）与 `records` 数组；每条记录对应一个游戏文本 ID：

- `name_id`：非空字符串，有符号 64 位整数按字符串保存。
- `zh`、`en`：非空字符串，同一 `name_id` 下不得出现第二种写法。
- `status`：非空字符串，内置数据为 `game-data-paired`。
- `entities`：至少一个对象，各对象含非空字符串 `id`、`table`、`category`；同一名称被多个实体共用时（如各类基质、成就奖章）在此列出全部实体。

查询字段：`zh`、`en`、`name_id` 及各实体的 `id`、`table`、`category`。中文串可能对应多条记录，例如「管理员」在角色表为 `Endministrator`、在物品表为 `The Endministrator`，脚本按记录逐条返回，不合并、不择优。

`entities` 中的 `id` 是配置表主键（如 `item_xiranite_poly`），不是界面路径；`table` 是来源表名，`category` 是内置分类。缺少英文时不得用中文或 ID 顶替，应不收录该条。

## 输出与缺失处理

`--json` 输出原记录并添加 `record_source` 分类标签；不会改变 `meaning_status`、`status` 或来源证据。错误和缺失说明发到 stderr。

按上述默认或显式目录选择后，单一 scope 缺文件时返回退出码 2；`all` 跳过缺失文件并提示，但若没有任何可用文件仍返回 2。任何选中且存在的数据文件格式错误都返回 2，避免把损坏数据表现为零命中。

仓库根目录的 `examples/data/` 是可复制的虚构格式示例，不是实际游戏词库，也不是安装后的依赖。实际内置数据位于 `references/`：游戏名称 309 条、名称索引 3,290 条、别名 22 组、正式名称 27 条。黑话和生产机制表供直接阅读；25 条界面补充暂不纳入脚本 scope。
