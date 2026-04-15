---
name: financial-statement-deep-research
description: Deep financial-statement-first company research for any listed company or large business. Use when Codex needs to analyze the latest annual or quarterly report, compare it against the prior 5 fiscal years and latest 8 quarters, extract core parameters from the three statements and notes, identify earnings quality and balance-sheet risks, and then optionally extend into valuation, peer comparison, shareholder structure, capital allocation, or industry-cycle analysis.
---

# Financial Statement Deep Research

## Overview

Run a financial-statement-first workflow. Start from the latest official filings, reconstruct multi-period comparisons, extract the note disclosures that are easy to miss, and only then move into valuation, shareholder structure, industry cycle, or thematic analysis.

## Workflow

1. Identify the company, listing venue, reporting currency, and latest report date.
2. Collect official source documents first. Prefer annual reports, interim reports, quarterly reports, earnings releases, and regulator filings over media or broker summaries.
3. Build the comparison base before writing conclusions:
   - annual: latest report plus prior 5 fiscal years
   - quarterly: latest 8 quarters when available
4. Extract and normalize the three statements. Do not rely on headline metrics alone.
5. Read notes for the parameters most likely to change the interpretation of the statements.
6. Write the financial analysis first. Industry cycle, valuation, shareholders, and style overlays come after the accounting picture is clear.

## Output Modes

Default to the light report unless the user asks for more depth.

- Light report:
  - latest period summary
  - 5-year annual trend
  - 8-quarter rhythm and volatility
  - core ratios and red flags
  - concise conclusion on earnings quality, cash generation, leverage, and capital allocation
- Deep report:
  - note-level parameter extraction
  - peer comparison
  - valuation
  - shareholder structure and capital allocation
  - industry-cycle positioning
  - overseas analogs or historical analogs when useful
- Style overlays:
  - Buffett-style
  - risk memo
  - valuation memo
  - technology or structural-change impact memo

## Source Priority

Read [references/source-priority.md](references/source-priority.md) before using secondary material. State clearly when a statement is sourced directly from filings versus inferred.

If the company is in a covered sector with special KPIs, load the matching reference file:

- insurance: [references/industry-insurance.md](references/industry-insurance.md)
- banks: [references/industry-banks.md](references/industry-banks.md)
- consumer: [references/industry-consumer.md](references/industry-consumer.md)
- industrial: [references/industry-industrial.md](references/industry-industrial.md)
- internet and software: [references/industry-internet-software.md](references/industry-internet-software.md)

## Financial Statement Core

Always reconstruct the following before you interpret management commentary.

### Income Statement

- revenue and growth rate
- gross profit, gross margin, operating profit, operating margin
- net profit, net margin, attributable profit
- non-recurring items or one-offs
- segment mix and geographic mix when material
- expense ratios: selling, R&D, G&A, credit cost, claims ratio, cost ratio, or sector equivalents

### Balance Sheet

- cash and short-term liquidity
- receivables, inventory, contract assets, and payables
- capex assets, goodwill, intangibles, investments
- debt structure, lease liabilities, off-balance-sheet commitments
- working-capital structure and changes
- equity, minority interest, book value, tangible book when relevant

### Cash Flow

- operating cash flow
- capex and acquisitions
- free cash flow
- financing cash flow and refinancing dependence
- conversion of profit to cash

Use [references/statement-analysis-playbook.md](references/statement-analysis-playbook.md) and [references/note-analysis-playbook.md](references/note-analysis-playbook.md) for the detailed checklist.

## Mandatory Comparisons

Produce both of these unless the source data genuinely does not exist:

- 5-year annual comparison table
- 8-quarter comparison table

Explain the main drivers of:

- year-over-year changes
- quarter-over-quarter changes where meaningful
- margin shifts
- cash conversion changes
- leverage changes
- changes in accounting policy, scope, reserves, or fair-value treatment

If a quarter is not comparable because of seasonality or the business model, say that explicitly and compare the more relevant periods instead.

## Notes and Hidden Parameters

Do not stop at the face statements. Pull the note disclosures that can reverse or weaken the headline conclusion.

Examples:

- revenue recognition assumptions
- bad debt or impairment assumptions
- inventory write-down policy
- goodwill or intangible impairment triggers
- fair-value hierarchy and unrealized gains
- reserve assumptions
- related-party transactions
- pension obligations
- contingent liabilities, guarantees, covenants, and litigation
- segment changes, restatements, disposals, or acquisitions

For sector-specific note work, load the relevant industry reference before writing conclusions.

## Industry Cycle Is Second Layer

After the financial analysis is stable, evaluate industry cycle using [references/industry-cycle-playbook.md](references/industry-cycle-playbook.md).

Industry work should answer:

- is the company riding a cyclical tailwind, fighting a headwind, or structurally improving?
- which part of the reported performance is likely cyclical versus durable?
- where does the current period sit versus prior industry cycles or overseas analogs?

Do not let cycle narratives override filing evidence.

## Valuation and Shareholders

When the user asks for valuation, load [references/valuation-playbook.md](references/valuation-playbook.md). When the user asks about major holders, buybacks, dividends, or incentives, load [references/shareholder-capital-allocation.md](references/shareholder-capital-allocation.md).

For control, manipulation, or "controlling the stock" questions:

- stick to disclosed holdings, concert parties, lockups, pledged shares, buybacks, placements, incentives, and trading restrictions
- do not allege manipulation without direct evidence
- label unsupported claims as not established by public filings

## Scripted Helpers

Use scripts when they reduce arithmetic errors or repetitive formatting.

- [scripts/analyze_financial_series.py](scripts/analyze_financial_series.py)
  - generic multi-period analyzer for annual and quarterly JSON input
  - computes growth, margins, leverage, cash conversion, and basic alerts
- [scripts/fetch_cninfo_financials.py](scripts/fetch_cninfo_financials.py)
  - China A-share helper that fetches statement data from cninfo `data20` endpoints
  - use only when the target company is covered by cninfo and identifiers are known
  - for other markets, collect official filings manually or via the relevant official site and then feed normalized data into `analyze_financial_series.py`

## Reporting Rules

- separate facts from interpretation
- mention the exact report dates when the user refers to "latest" or relative dates
- state the unit and currency
- explain whether a metric is cumulative year-to-date or single-quarter
- identify when seasonality makes a sequential comparison misleading
- prefer concise tables before prose when comparing many periods
- if a figure comes from a note instead of the face statements, say so

## Deliverable Shape

Use the templates in [references/report-templates.md](references/report-templates.md). A good report usually follows this order:

1. current conclusion
2. financial statement findings
3. note-level findings
4. annual and quarterly trend interpretation
5. industry-cycle position
6. valuation or capital allocation, if requested
7. risks, open questions, and what would change the view
