# 生产与物流术语中英对照

这些是**工业与物流文档的建议译法**，按历史中文研究语料整理；不宣称官方命名或英语社区已有统一用法。中文定义有歧义时，以当前章节的定义为准。英文首现可附中文，尤其是 blocking-flow、damping 和各类均匀性定义。

背景主题简称见 [corpus-map.md](corpus-map.md)：C1=生产术语表，C2=阻塞生产入门，C3=两类阻塞，C4=阻塞端与流通端，C5=配平/自适应，C6=理想系统，C7=统一词典，C8=阻尼理论，C9=反应缓存补充，C10=反应池物流异常，C11=入口控制补充。一组中的通用工程译法也是编辑约定；来源证明中文语义，不证明英语译名。

## 生产、控制和流量

| 中文 | 建议英文 | 语义及使用边界 | 语义来源 |
| --- | --- | --- | --- |
| 物料 | material | 包括固体、液体、气体，不只原料 | C1 |
| 原料 | input material / raw material | 配方输入用 input material；自然采集原料可用 raw material | C1、C9 |
| 中间产物 | intermediate product | 后续配方仍需消耗的产物 | C9、C10 |
| 副产物 | by-product | 与主目标一同生成，不等同于废弃物 | C9 |
| 配方 | recipe | 游戏生产配方；化学公式另用 formula | C9 |
| 产线、生产线 | production line | 一套生产流程 | C1、C5 |
| 生产结构 | production network | 包含机器及物流连接的有边界结构 | C1 |
| 物流结构 | logistics network | 有明确输入/输出节点的运输元件组合 | C1 |
| 物流元件 | logistics component | 传送带、管道、分汇流器等 | C1、C8 |
| 节点 | node | 具体或抽象的连接位置 | C1 |
| 输入节点、输出节点 | input node / output node | 以所研究子系统边界判断 | C1 |
| 输入口、输出口 | input port / output port | 实体设备接口，与抽象节点区分 | C1 |
| 路径 | path | 沿作者定义判断可达性，不只当前可流通状态 | C1 |
| 支路、通路 | branch / route | branch 用于分叉支路，route 用于整条通路 | C3、C4 |
| 直接上游、直接下游 | immediate upstream / immediate downstream | 邻接关系 | C1 |
| 上游、下游 | upstream / downstream | 沿物料流向判断，不沿控制信号方向 | C1 |
| 流量 | flow rate | 单位时间数量；数学变量仍照原文 | C6 |
| 平均流量 | average flow rate | 不隐含物料到达均匀 | C3、C9 |
| 吞吐量 | throughput | 运输或处理能力；视上下文补 rate 或时间窗口 | C6 |
| 产能 | production capacity | 能力上限；实际产出速度用 production rate | C5、C9 |
| 有效产能 | effective production capacity | 受等待、竞争、阻塞影响的有效能力 | C9 |
| 毛产、毛产量 | gross production / gross output | 具体扣除口径见原文 | C5、C11 |
| 净产、净产量 | net production / net output | 不擅自添加供电等成本扣除 | C5、C11 |
| 最大价值产出 | maximum-value output | 价值目标，不能等同最大物品数量 | C5 |
| 配平 | production balancing | 此语料指给定供给被稳定消耗且至少经过一步加工 | C5 |
| 自动配平、自配平 | automatic production balancing | 系统自行实现上述配平 | C5 |
| 自适应 | adaptive operation | 随输入或阻塞条件变化；不隐含自动寻优 | C5 |
| 自适应产线 | adaptive production line | 首次说明适应的条件 | C5 |
| 智能切换 | automatic production switching | 无须玩家手动干预，不能译成 AI switching | C1、C2 |
| 阻塞、堵塞 | blocking / blockage | blocking 指状态/机制，blockage 指一次阻塞 | C2、C6 |
| 阻塞流 | blocking flow（本文定义） | 游戏物流阻塞流，不能未经说明套用 Dinic 算法的同名概念 | C6 |
| 阻塞生产 | production controlled by blocking | 解释后可简写 blocking-based production | C2 |
| 阻塞信号 | blocking signal | 由阻塞状态传递的控制信息 | C2 |
| 阻塞源 | source of blocking | 首先出现阻塞的下游节点 | C1 |
| 切换型阻塞 | switching-type blocking | 平均意义下全部流量改道、生产目标切换 | C3 |
| 平衡型阻塞 | balancing-type blocking | 平均意义下部分流量转移，达到平衡 | C3 |
| 阻塞端 | blocking branch | 分/汇流中的指定阻塞支路，不是设备损坏 | C4 |
| 流通端 | flowing branch | 相对角色，不能保证它永不阻塞 | C4 |
| 受控端、自由端 | controlled branch / free branch | 旧文作者用语；不自动替换成阻塞端/流通端 | C4及其前篇 |
| 反向传播 | upstream propagation | 阻塞沿物料流向的反方向传播；勿误写为 reverse material flow | C2、C4 |
| 溢流 | overflow / overflow routing | 因某出口阻塞而改道，不必然丢弃物料 | C1 |
| 加压 | oversupply to induce blocking | 指供给能力超过消耗形成阻塞，不是物理增压 | C1 |
| 分流、汇流 | splitting / merging | 动作用 merging；游戏“汇流器”名称是 Converger | C6 |
| 均分 | equal splitting | 等量分配，未必保证时间均匀 | C6、C7 |
| 硬分流、精确分流 | fixed-ratio splitting / exact-ratio splitting | 不将配平约束误解成化学方程配平 | C5 |
| 限流、限速 | flow limiting / rate limiting | 区别于普通传输延迟 | C10、C11 |
| 限流器 | flow limiter | 可指复合物流结构，不自动认定为 Control Port | C6、C11 |
| 回流 | recirculation | 物料绕回上游；信号反馈用 feedback | C11 |
| 入口回流限流 | inlet rate limiting through recirculation | 说明入口、回路和限流对象 | C11 |
| 反馈、前馈 | feedback / feedforward | 按原文定义与方向，不从物料回路直接推断控制分类 | C4 |
| 优先级 | priority | 明确对象是输入、输出还是汇入 | C7、C8 |
| 优先输出 | output priority | 不把原文解释提升为通用游戏规则 | C7、C8 |
| 优先输入 | input priority | 与汇入现象按章节区分 | C7 |
| 优先汇入 | merge priority | 汇流时某方向优先 | C7及相关研究页 |
| 轮询 | round-robin servicing | 用于循环依次服务端口；若只检查状态用 polling | C7、语料标题；C7条目尚未给完整定义 |
| 时钟信号 | clock signal | 生产控制节拍，不等于游戏引擎时钟 | C2 |
| 满速、半速 | full-rate / half-rate operation | 需有具体设备或产线的速率基准 | C10 |
| 满仓、爆仓 | full storage / reaching storage capacity | 技术解释不直译为 exploding warehouse | C2、C4 |
| 空仓 | empty storage | 不据此推出所有缓存均为空 | C4 |

## 缓存、反应和事件时序

| 中文 | 建议英文 | 语义及使用边界 | 语义来源 |
| --- | --- | --- | --- |
| 机器缓存 | machine buffer | 不是 CPU cache | C9 |
| 原料缓存、输出缓存 | input buffer / output buffer | 以原文角色命名，不合并为完成缓存 | C2、C9 |
| 池内库存 | in-crucible material inventory | 与尚未落地的产物分开 | C9 |
| 完成缓存 | completion buffer | 完成但尚未转入物料库存的产物暂存 | C9 |
| 完成阻塞 | completion-buffer blocking | 产物不能落地，不表示反应还未完成 | C9 |
| 落地 | transfer into material inventory | 首现说明是从完成缓存转入；勿译作 landing | C9 |
| 扣料 | consume inputs | 开始反应时扣除物料，不是物料外运 | C9 |
| 占槽 | occupying a material slot | 与数量容量区分，依作者具体模型 | C9 |
| 共享容量、共享空间 | shared storage capacity | 外部输入与内部生成争用的容量 | C9 |
| 启动条件 | start conditions | 含原料和缓存条件；勿只写 input availability | C9 |
| 原位反应 | in-situ reaction | 池内继续使用中间产物 | C10 |
| 原位底物、外源底物 | internally produced input / externally supplied input | 游戏说明通常不用过强的生物学术语 substrate | C10 |
| 并行反应 | parallel reactions | 不泛化为所有机器或所有配方均可并行 | C9 |
| 物流相位 | logistics phase | 离散事件的相对时序 | C9 |
| 启动同步、完成同步、落地同步 | synchronized starts / completions / inventory transfers | 三种不同事件，不统称 simultaneous production | C9 |
| 同刻事件 | simultaneous events | 相同时间戳不证明执行顺序 | C9 |
| 恢复延迟 | recovery delay | 区别于等下一次原料到达 | C9 |
| 缺料 | input starvation | 与输出阻塞分开 | C9 |
| 自锁 | self-locking state | 先描述状态；确定无法恢复才可称 deadlock | C11 |
| 启动过程、稳态 | startup transient / steady state | 稳态平均值不代表每个时刻相同 | C5、C9 |

## 理论模型、均匀性和历史名词

| 中文 | 建议英文 | 语义及使用边界 | 语义来源 |
| --- | --- | --- | --- |
| 理想系统 | idealized logistics system | 指带容量的有向图模型 | C6 |
| 有向多重图 | directed multigraph | 原数学结构 | C6 |
| 流量守恒 | flow conservation | 保留节点类别与求和范围 | C6 |
| 容量 | capacity | 图中边流量上限；非仓库数量上限 | C6 |
| 离散模型、连续模型 | discrete model / continuous model | 不用连续均值替代事件轨迹 | C9 |
| 混合整数线性规划 | mixed-integer linear programming (MILP) | 保留原模型假设 | C6 |
| 可满足性模理论 | satisfiability modulo theories (SMT) | 首现展开即可 | C6 |
| 阻尼 | damping（作者定义） | 历史模型中的物流元件计数，不是物理阻力系数 | C8 |
| 物流线 | logistics path（作者定义） | 该理论的特定路线概念 | C8 |
| 断尾物流线 | open-ended logistics path | 末尾不连接工厂入口 | C8 |
| 连接顺序 | connection order | 不是空间方向 | C8 |
| 放置顺序 | placement order | 区别于连接顺序 | C8及相关研究页 |
| 输出迟滞、4n卡1s | output lag / the “4n, 1 s stall” phenomenon | 原名保留，遵循原文条件，不套用热学滞后 | 相关异常研究页 |
| 整流器 | flow regularizer | 社区物流结构，不是电气 rectifier；具体定义以原文为准 | 相关整流器页 |
| 稳流器 | flow stabilizer | 不自动等同精确均匀输出 | C7及相关研究页 |
| 平均间隔 | mean interval | C7的极限定义，保留公式 | C7 |
| 依时波动幅度 | range of arrival-time deviation | 不是标准差，也不是单纯到达间隔极差 | C7 |
| 占空比 | duty cycle | 本文 d=K/L；保留“个/tick”等作者约定 | C7 |
| 完美均匀 | perfect uniformity（作者定义） | 不能删掉 ≤1 与严格 <1 的差异 | C7 |
| 局部均匀 | local uniformity | 按区间数量偏差定义 | C7 |
| Bresenham-M均匀 | Bresenham-M uniformity | 不改 M、不改绝对值约束 | C7 |
| Beatty-M均匀 | Beatty-M uniformity | 不换成另一作者的等价形式 | C7 |
| Cipolla-M物品均匀 | Cipolla-M item-count uniformity | 累积数量偏差极差 | C7 |
| Cipolla-M时间均匀 | Cipolla-M time uniformity | 到达时间偏差极差 | C7 |
| 计数树 | counting tree | 保留叶节点参数 N_leaf | C7 |
| 蓄电量极差 | range of stored energy | 最大值减最小值，不译为 variance | C7 |
| 取补 | binary complementation | 0/1 互换 | C7 |
| K-取商 | K-fold thinning | 保留作者定义“每 K 个保留第 1 个”，不是数值整除 | C7 |

“231理论”、未展开的算法简称等无明确定义时，保留原名加 `theory`，不得为使译文流畅而自行编出定义。


## 跨文档使用边界

术语表提供建议译法与适用条件，当前文档定义优先。以人名命名的数学或均匀性术语保留其名称。

整流、非阻塞等机制的确切读法从当前原文确认；共同前提、交替时段、均匀性不等式等均照原文保留。
