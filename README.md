# Endfield CN2EN Translation

[中文](#中文) · [English](#english)

## 中文

《明日方舟：终末地》工业、生产与物流文档的中英翻译 skill。帮助翻译者区分游戏名称、玩家简称和作者自定义术语，保留技术条件、数值、公式与不确定性。

**主要用于将中文社区产出的内容翻译成英文**，也支持英译中与双语校订。如果你有建议或想补充的信息，欢迎提 Issue 或 PR。

本仓库提供翻译流程、术语参考和离线查询工具。安装后即可查询游戏名称与别名，并结合当前原文确定译法。

### 内置内容

| 内容 | 范围 |
| --- | --- |
| [游戏名称配对](skills/endfield-cn2en-translation/references/game-terms.md) | 309 条分版本中英名称记录，附 CSV 主表 |
| [完整名称索引](skills/endfield-cn2en-translation/references/name-index.json) | 3,290 个文本 ID、3,685 个实体，覆盖物品、设施、角色、敌人、副本、活动与物品分类 |
| [真实别名](skills/endfield-cn2en-translation/references/community-aliases.md) | 22 组别名、简称、笔误与候选；保留确认/暂定差别 |
| [玩家黑话](skills/endfield-cn2en-translation/references/community-slang.md) | 22 条基建、抄作业、暗管、爆仓、设备睡觉等用语 |
| [生产机制术语](skills/endfield-cn2en-translation/references/production-terms.md) | 107 条生产、阻塞、缓存、时序、模型及均匀性条目 |
| [正式名称](skills/endfield-cn2en-translation/references/official-names.md) | 27 条游戏版本、地名、界面和装备类别名称 |
| [界面补充](skills/endfield-cn2en-translation/references/interface-terms-1.6.4.json) | 25 条 1.6.4 界面及话题名称 |

配对覆盖版本 `1.5.3@10024360-6`（143 条）和 `1.6.4@11123848-6`（166 条）；完整名称索引取 `1.6.4@11262943-8`，只收名称、不含对白与说明。来源与哈希见 [来源说明](skills/endfield-cn2en-translation/references/sources.md)。翻译时核对目标游戏版本；别名、笔误和候选含义须结合当前语境判断。

### 安装

将 [skills/endfield-cn2en-translation](skills/endfield-cn2en-translation/SKILL.md) 所在的整个目录复制到所用助手的 skills 目录，目录名保持 `endfield-cn2en-translation`。示例安装位置为用户目录下的 `.codex/skills/endfield-cn2en-translation/`；其他助手按各自 skill 配置安装。若已安装同名个人版，请先备份，或在隔离环境评估发布版。

在支持显式调用 skill 的助手中输入：

> 使用 $endfield-cn2en-translation 将指定文档翻译为英文，保留公式和资源链接，未核实的名称标注暂译。

该 skill 本身不要求 Python；运行查询脚本才需要 Python。代码目标为 Python 3.10+，本地验证版本为 Python 3.12.14，其他版本尚未逐一实测。仅使用标准库，无需安装依赖。

### 查询工具

从仓库根目录运行以下命令，默认查询内置真实词表：

```sh
python skills/endfield-cn2en-translation/scripts/lookup_terms.py "壤晶" --exact --json
python skills/endfield-cn2en-translation/scripts/lookup_terms.py "小药" --scope aliases
python skills/endfield-cn2en-translation/scripts/lookup_terms.py "帝江号" --scope official
python skills/endfield-cn2en-translation/scripts/lookup_terms.py "Xircon" --scope all --json
```

默认按文件优先读取安装目录的自用 `data/`，缺少该文件时回退到 `references/`。显式传入 `--data-dir` 时只查询指定目录。虚构格式示例见 `examples/data/`，格式说明见 [数据说明](skills/endfield-cn2en-translation/references/data-format.md)。查询在本地离线执行；黑话和生产机制表由 skill 按需阅读。

| 参数 | 含义 |
| --- | --- |
| `--scope game` | 查询 game-terms.csv，默认范围 |
| `--scope aliases` | 查询 community-aliases.json，保留确认状态 |
| `--scope official` | 查询 official-names.json，不替使用者核验来源 |
| `--scope all` | 查询本地实际存在的全部上述文件，并提示缺失文件 |
| `--exact` | 按完整字段匹配，忽略大小写 |
| `--json` | stdout 只输出 JSON 数组，缺失数据等说明写 stderr |
| `--data-dir PATH` | 只查询指定目录，替代默认内置/自用数据选择 |

退出码：成功查询（含零条命中）为 0；参数、文件缺失或数据格式错误为 2。`all` 模式可以跳过缺失文件，但没有任何可用文件时返回 2；现有文件格式错误不会静默跳过。各范围只加载自己的数据。

### 项目适配与验证

按当前任务配置输出格式、作者署名、项目术语和资源处理要求，参见 [项目适配说明](skills/endfield-cn2en-translation/references/project-adapter.md)。

```sh
python -B -m unittest discover -s tests -v
python -B tools/check_release.py
```

发布检查采用 [文件白名单](release-manifest.json)，验证数据数量、标记、术语表和链接。维护方式见 [CONTRIBUTING.md](CONTRIBUTING.md)。

### 建议与贡献

如果你有建议或想补充的信息，欢迎提 Issue 或 PR，包括术语纠正、新增中英名称配对、玩家黑话、翻译示例和流程改进。补充术语时请尽量提供来源、游戏版本和使用语境，并区分官方名称、社区用语与暂译。贡献说明见 [CONTRIBUTING.md](CONTRIBUTING.md)。

### 许可与范围

自编写流程、工具及虚构示例采用 [MIT License](LICENSE)。内置名称资料、第三方游戏文本及研究语义来源的范围见 [NOTICE](NOTICE) 和各数据来源记录；MIT 不代表对第三方权利的重新授权。本项目是非官方工具，不代表游戏发行商或社区作者。

## English

A translation skill for Chinese and English industrial, production, and logistics documentation for *Arknights: Endfield*. It helps distinguish game names, player shorthand, and author-defined terminology while preserving technical conditions, numbers, formulas, and uncertainty.

**Its primary purpose is to translate content created by the Chinese community into English.** It also supports English-to-Chinese translation and bilingual editing. If you have suggestions or information to add, please open an Issue or submit a PR.

This repository provides a translation workflow, terminology references, and an offline lookup tool. Game names and aliases are available immediately after installation, with translations selected in the context of the current source text.

### Included resources

| Resource | Coverage |
| --- | --- |
| [Game-name pairs](skills/endfield-cn2en-translation/references/game-terms.md) | 309 versioned Chinese–English name records, with a CSV master table |
| [Full name index](skills/endfield-cn2en-translation/references/name-index.json) | 3,290 text IDs and 3,685 entities across items, facilities, operators, enemies, dungeons, activities, and item categories |
| [Player aliases](skills/endfield-cn2en-translation/references/community-aliases.md) | 22 groups of aliases, shorthand, typos, and candidate meanings; confirmed and tentative interpretations remain distinct |
| [Community slang](skills/endfield-cn2en-translation/references/community-slang.md) | 22 entries covering factory setups, copying builds, underground pipes, full storage, idle machines, and more |
| [Production and logistics terminology](skills/endfield-cn2en-translation/references/production-terms.md) | 107 entries covering production, blocking, buffers, timing, models, and uniformity |
| [Verified names](skills/endfield-cn2en-translation/references/official-names.md) | 27 game-version, location, interface, and gear-category names |
| [Supplemental interface names](skills/endfield-cn2en-translation/references/interface-terms-1.6.4.json) | 25 interface and topic names from version 1.6.4 |

Name pairs cover versions `1.5.3@10024360-6` (143 records) and `1.6.4@11123848-6` (166 records); the full name index uses `1.6.4@11262943-8` and contains names only. See [Sources](skills/endfield-cn2en-translation/references/sources.md) for provenance and hashes. Check the target game version when translating, and interpret aliases, typos, and candidate meanings in the current context.

### Installation

Copy the entire [skills/endfield-cn2en-translation](skills/endfield-cn2en-translation/SKILL.md) directory into your assistant's skills directory, keeping its name as `endfield-cn2en-translation`. For Codex, an example location is `.codex/skills/endfield-cn2en-translation/` under your user directory. Follow the relevant configuration for other assistants. If you already have a personal edition with the same name, back it up first or evaluate this edition in an isolated environment.

In an assistant that supports explicit skill invocation, enter:

> Use $endfield-cn2en-translation to translate the specified document into English. Preserve formulas and resource links, and label unverified names as provisional translations.

The skill itself does not require Python; only the lookup script does. The code targets Python 3.10+ and has been tested locally on Python 3.12.14. Other versions have not been individually tested. It uses only the standard library, with no dependencies to install.

### Lookup tool

Run these commands from the repository root to search the bundled dictionaries:

```sh
python skills/endfield-cn2en-translation/scripts/lookup_terms.py "壤晶" --exact --json
python skills/endfield-cn2en-translation/scripts/lookup_terms.py "小药" --scope aliases
python skills/endfield-cn2en-translation/scripts/lookup_terms.py "帝江号" --scope official
python skills/endfield-cn2en-translation/scripts/lookup_terms.py "Xircon" --scope all --json
```

By default, each selected dictionary is loaded from the installed skill's personal `data/` directory when present; otherwise, the file in `references/` is used. An explicit `--data-dir` restricts the search to that directory. Fictional format examples are in `examples/data/`; see [Data format](skills/endfield-cn2en-translation/references/data-format.md) for details. Queries run locally and offline. Slang and production terminology are read directly by the skill as needed.

| Option | Behavior |
| --- | --- |
| `--scope game` | Search game-terms.csv; the default scope |
| `--scope aliases` | Search community-aliases.json while retaining confirmation status |
| `--scope official` | Search official-names.json; this does not independently verify its sources |
| `--scope all` | Search all available dictionaries above and report missing files |
| `--exact` | Match complete fields, ignoring case |
| `--json` | Write only a JSON array to stdout; diagnostics go to stderr |
| `--data-dir PATH` | Search only the specified directory instead of the default personal/bundled selection |

Exit codes: 0 for a successful search, including no matches; 2 for invalid arguments, missing required files, or malformed data. The `all` scope can skip missing files, but returns 2 if no selected dictionaries are available. Existing malformed files are never silently skipped. Each scope loads only its own data.

### Project adaptation and validation

Configure output format, attribution, local terminology, and resource handling for the current task; see [Project adaptation](skills/endfield-cn2en-translation/references/project-adapter.md).

```sh
python -B -m unittest discover -s tests -v
python -B tools/check_release.py
```

The release check uses a [file allowlist](release-manifest.json) to validate record counts, metadata, terminology tables, and links. See [CONTRIBUTING.md](CONTRIBUTING.md) for maintenance guidance.

### Suggestions and contributions

If you have suggestions or information to add, please open an Issue or submit a PR. Contributions can include terminology corrections, additional Chinese–English name pairs, community slang, translation examples, and workflow improvements. When adding terminology, please provide sources, the game version, and usage context where possible, and distinguish official names, community usage, and provisional translations. See [CONTRIBUTING.md](CONTRIBUTING.md).

### License and scope

The independently written workflow, tools, and fictional examples use the [MIT License](LICENSE). The scope of bundled name references, third-party game text, and research terminology sources is described in [NOTICE](NOTICE) and the individual source records. MIT does not relicense third-party rights. This is an unofficial tool and does not represent the game publisher or community authors.
