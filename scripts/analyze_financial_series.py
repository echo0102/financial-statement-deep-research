#!/usr/bin/env python3
"""
Analyze multi-period financial statement data from normalized JSON.

Input JSON shape:
{
  "company": "Example Co",
  "currency": "CNY",
  "annual": [
    {"period": "2025", "revenue": 100, "net_income": 12, "operating_cash_flow": 15,
     "capex": 4, "total_assets": 120, "total_liabilities": 70, "equity": 50,
     "cash": 20, "debt": 25},
    ...
  ],
  "quarterly": [
    {"period": "2025Q4", "revenue": 30, "net_income": 3, "operating_cash_flow": 4,
     "capex": 1, "total_assets": 120, "total_liabilities": 70, "equity": 50,
     "cash": 20, "debt": 25},
    ...
  ]
}
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


KEYS = (
    "revenue",
    "gross_profit",
    "operating_income",
    "net_income",
    "operating_cash_flow",
    "capex",
    "total_assets",
    "total_liabilities",
    "equity",
    "cash",
    "debt",
)


@dataclass
class PeriodResult:
    period: str
    metrics: dict[str, float | int | None]
    derived: dict[str, float | None]
    alerts: list[str]


def load_series(path: Path) -> dict:
    with path.open() as handle:
        return json.load(handle)


def to_float(value):
    if value in (None, "", "NA", "N/A"):
        return None
    return float(value)


def pct_change(current, previous):
    if current is None or previous in (None, 0):
        return None
    return (current - previous) / abs(previous)


def ratio(numerator, denominator):
    if numerator is None or denominator in (None, 0):
        return None
    return numerator / denominator


def free_cash_flow(metrics: dict[str, float | None]) -> float | None:
    cfo = metrics.get("operating_cash_flow")
    capex = metrics.get("capex")
    if cfo is None or capex is None:
        return None
    return cfo - capex


def analyze_periods(periods: Iterable[dict]) -> list[PeriodResult]:
    normalized = []
    previous = None

    for raw in periods:
        metrics = {key: to_float(raw.get(key)) for key in KEYS}
        derived = {
            "free_cash_flow": free_cash_flow(metrics),
            "net_margin": ratio(metrics["net_income"], metrics["revenue"]),
            "cfo_to_net_income": ratio(metrics["operating_cash_flow"], metrics["net_income"]),
            "debt_to_equity": ratio(metrics["debt"], metrics["equity"]),
            "liability_to_asset": ratio(metrics["total_liabilities"], metrics["total_assets"]),
        }
        alerts = []

        if derived["cfo_to_net_income"] is not None and derived["cfo_to_net_income"] < 0.8:
            alerts.append("weak cash conversion")
        if derived["debt_to_equity"] is not None and derived["debt_to_equity"] > 1.5:
            alerts.append("high leverage")
        if derived["liability_to_asset"] is not None and derived["liability_to_asset"] > 0.75:
            alerts.append("balance sheet heavily leveraged")
        if (
            derived["free_cash_flow"] is not None
            and metrics["net_income"] is not None
            and metrics["net_income"] > 0
            and derived["free_cash_flow"] < 0
        ):
            alerts.append("profit positive but free cash flow negative")

        if previous:
            derived["revenue_yoy_or_seq"] = pct_change(metrics["revenue"], previous.metrics.get("revenue"))
            derived["net_income_yoy_or_seq"] = pct_change(
                metrics["net_income"], previous.metrics.get("net_income")
            )
        else:
            derived["revenue_yoy_or_seq"] = None
            derived["net_income_yoy_or_seq"] = None

        result = PeriodResult(period=str(raw.get("period")), metrics=metrics, derived=derived, alerts=alerts)
        normalized.append(result)
        previous = result

    return normalized


def format_pct(value):
    if value is None:
        return "n/a"
    return f"{value * 100:.1f}%"


def summarize(label: str, results: list[PeriodResult]) -> list[str]:
    lines = [f"{label}:"]
    for result in results:
        margin = format_pct(result.derived.get("net_margin"))
        growth = format_pct(result.derived.get("revenue_yoy_or_seq"))
        conversion = format_pct(result.derived.get("cfo_to_net_income"))
        fcf = result.derived.get("free_cash_flow")
        alerts = ", ".join(result.alerts) if result.alerts else "none"
        lines.append(
            "  - "
            f"{result.period}: revenue={result.metrics.get('revenue')}, "
            f"net_income={result.metrics.get('net_income')}, "
            f"net_margin={margin}, growth={growth}, "
            f"fcf={fcf}, cfo/net_income={conversion}, alerts={alerts}"
        )
    return lines


def main():
    parser = argparse.ArgumentParser(description="Analyze annual and quarterly financial series.")
    parser.add_argument("input", help="Path to normalized JSON input.")
    parser.add_argument(
        "--output-json",
        help="Optional path to write structured analysis JSON.",
    )
    args = parser.parse_args()

    payload = load_series(Path(args.input))
    annual = analyze_periods(payload.get("annual", []))
    quarterly = analyze_periods(payload.get("quarterly", []))

    print(f"Company: {payload.get('company', 'unknown')}")
    print(f"Currency: {payload.get('currency', 'unknown')}")
    for line in summarize("Annual", annual):
        print(line)
    for line in summarize("Quarterly", quarterly):
        print(line)

    if args.output_json:
        out = {
            "company": payload.get("company"),
            "currency": payload.get("currency"),
            "annual": [
                {"period": item.period, "metrics": item.metrics, "derived": item.derived, "alerts": item.alerts}
                for item in annual
            ],
            "quarterly": [
                {"period": item.period, "metrics": item.metrics, "derived": item.derived, "alerts": item.alerts}
                for item in quarterly
            ],
        }
        Path(args.output_json).write_text(json.dumps(out, indent=2, ensure_ascii=True))


if __name__ == "__main__":
    main()
