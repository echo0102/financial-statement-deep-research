---
name: financial-statement-deep-research
description: 以财务报表为核心的深度公司研究技能，适用于任何上市公司或大型企业。用于分析最新年报或季报，与过去 5 个完整财年和最近 8 个季度进行对比，提取三大报表及附注中的关键参数，识别盈利质量与资产负债表风险，并在此基础上进一步展开估值、同业对比、股东结构、资本配置或行业周期分析。
---

# 财务报表深度研究

## 概述

采用“先报表、后观点”的研究流程。先从最新的官方披露文件入手，重建多期对比，提取容易被忽略的附注信息，之后再进入估值、股东结构、行业周期或主题分析。

## 工作流

1. 确认公司名称、上市地点、报告货币以及最新报告日期。
2. 优先收集官方披露文件。年报、中报、季报、业绩公告和监管披露优先于媒体报道或券商摘要。
3. 在写结论前先搭好对比框架：
   - 年度：最新报告期加上前 5 个完整财年
   - 季度：尽量覆盖最近 8 个季度
4. 提取并标准化三大报表，不只看 headline 指标。
5. 阅读最可能改变报表解读的附注参数。
6. 先完成财务分析，再叠加行业周期、估值、股东结构或风格化分析。

## 输出模式

除非用户要求更深入，默认输出轻量版报告。

- 轻量版报告：
  - 最新期概览
  - 5 年年度趋势
  - 8 个季度的节奏与波动
  - 核心比率与风险信号
  - 对盈利质量、现金创造、杠杆与资本配置的简明结论
- 深度版报告：
  - 附注层参数提取
  - 同业对比
  - 估值分析
  - 股东结构与资本配置
  - 行业周期位置
  - 必要时引入海外可比或历史可比
- 风格化附加层：
  - 巴菲特风格
  - 风险备忘录
  - 估值备忘录
  - 技术变革或结构变化影响备忘录

## 信息源优先级

使用二手材料前，先阅读 [references/source-priority.md](references/source-priority.md)。要明确区分哪些表述直接来自披露文件，哪些是基于披露文件作出的推断。

如果公司属于以下已覆盖行业，写结论前加载对应参考文件：

- 保险： [references/industry-insurance.md](references/industry-insurance.md)
- 银行： [references/industry-banks.md](references/industry-banks.md)
- 消费： [references/industry-consumer.md](references/industry-consumer.md)
- 工业： [references/industry-industrial.md](references/industry-industrial.md)
- 互联网与软件： [references/industry-internet-software.md](references/industry-internet-software.md)

## 财务报表核心

在解读管理层表述前，必须先重建以下核心项目。

### 利润表

- 收入及增速
- 毛利、毛利率、营业利润、营业利润率
- 净利润、净利率、归母利润
- 非经常性项目或一次性影响
- 重要时拆解业务结构与地域结构
- 费用率：销售、研发、管理、信用成本、赔付率、费用率，或行业对应指标

### 资产负债表

- 现金及短期流动性
- 应收、存货、合同资产与应付
- 资本开支相关资产、商誉、无形资产、投资
- 债务结构、租赁负债、表外承诺
- 营运资本结构及变化
- 权益、少数股东权益、账面净资产，必要时看有形净资产

### 现金流量表

- 经营现金流
- 资本开支与并购支出
- 自由现金流
- 融资现金流与再融资依赖
- 利润向现金的转化能力

详细清单参考 [references/statement-analysis-playbook.md](references/statement-analysis-playbook.md) 和 [references/note-analysis-playbook.md](references/note-analysis-playbook.md)。

## 强制对比项

除非源数据确实不存在，否则必须产出以下两张对比表：

- 5 年年度对比表
- 最近 8 个季度对比表

并解释以下变化的主要驱动因素：

- 同比变化
- 在有意义时解释环比变化
- 利润率变动
- 现金转化变化
- 杠杆变化
- 会计政策、合并范围、准备金或公允价值处理的变化

如果季度之间因季节性或商业模式导致不可比，要明确说明，并改用更合适的比较口径。

## 附注与隐藏参数

不要停留在报表主表层面。必须提取那些可能推翻或削弱 headline 结论的附注披露。

例如：

- 收入确认假设
- 坏账或减值假设
- 存货跌价政策
- 商誉或无形资产减值触发条件
- 公允价值层级与未实现收益
- 准备金假设
- 关联交易
- 养老金义务
- 或有负债、担保、契约约束与诉讼
- 分部变更、重述、处置或并购

如果涉及行业特定的附注分析，应在写结论前先读取对应行业参考文件。

## 行业周期是第二层

在财务分析稳定之后，再用 [references/industry-cycle-playbook.md](references/industry-cycle-playbook.md) 评估行业周期。

行业分析应回答：

- 公司当前是处于周期顺风、逆风，还是结构性改善中？
- 报告期表现中哪些更可能是周期性的，哪些更可能是可持续的？
- 当前阶段在历次行业周期或海外可比阶段中处于什么位置？

不要让行业叙事压过披露文件证据。

## 估值与股东

用户要求估值时，加载 [references/valuation-playbook.md](references/valuation-playbook.md)。用户询问大股东、回购、分红或激励时，加载 [references/shareholder-capital-allocation.md](references/shareholder-capital-allocation.md)。

对于“控盘”“操纵股价”之类的问题：

- 只基于已披露的持股、行动一致人、限售、质押、回购、定增、激励和交易限制信息作答
- 没有直接证据时，不得指控操纵
- 没有被公开披露证据支持的说法，要明确标注为“公开披露无法证实”

## 脚本辅助

在可以减少算术错误或重复格式化工作时，优先使用脚本。

- [scripts/analyze_financial_series.py](scripts/analyze_financial_series.py)
  - 通用多期分析器，适用于年度和季度 JSON 输入
  - 计算增速、利润率、杠杆、现金转化和基础风险提示
- [scripts/fetch_cninfo_financials.py](scripts/fetch_cninfo_financials.py)
  - 面向中国 A 股的辅助脚本，从 cninfo `data20` 接口抓取报表数据
  - 仅在目标公司由 cninfo 覆盖且标识已知时使用
  - 其他市场应手动或通过官方披露站点获取原始文件，再将标准化数据输入 `analyze_financial_series.py`

## 报告规则

- 事实与解释分开写
- 用户提到“最新”或相对日期时，要写明准确报告日期
- 标明单位和货币
- 说明指标是累计口径还是单季度口径
- 当季节性使环比失真时，要明确指出
- 多期比较优先用简洁表格而不是大段文字
- 如果数字来自附注而不是报表主表，要明确说明

## 交付结构

参考 [references/report-templates.md](references/report-templates.md) 中的模板。一个合格报告通常按以下顺序组织：

1. 当前结论
2. 财务报表发现
3. 附注层发现
4. 年度与季度趋势解读
5. 行业周期位置
6. 如有要求，再写估值或资本配置
7. 风险、待验证问题，以及哪些因素会改变当前判断
