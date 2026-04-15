#!/usr/bin/env python3
"""
Fetch statement series for a China A-share company from cninfo data20 endpoints.

Example:
python3 fetch_cninfo_financials.py --scode 601336 --sign 4 --output xinhua.json
"""

from __future__ import annotations

import argparse
import json
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path


BASE = "https://www.cninfo.com.cn/data20/financialData"
ENDPOINTS = {
    "income": "getIncomeStatement",
    "balance": "getBalanceSheets",
    "cashflow": "getCashFlowStatement",
}
SERIES_MAP = {
    "year": "annual",
    "one": "quarterly_q1",
    "middle": "quarterly_h1",
    "three": "quarterly_q3",
}


def fetch_json(url: str) -> dict:
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0",
            "Referer": "https://www.cninfo.com.cn/",
        },
    )
    with urllib.request.urlopen(req, timeout=20) as response:
        return json.loads(response.read().decode("utf-8"))


def endpoint_url(name: str, scode: str, sign: str) -> str:
    query = urllib.parse.urlencode({"scode": scode, "sign": sign})
    return f"{BASE}/{ENDPOINTS[name]}?{query}"


def reshape_records(records: list[dict]) -> dict[str, dict[str, dict[str, float | None]]]:
    record = records[0]
    out: dict[str, dict[str, dict[str, float | None]]] = {}
    for source_key, target_key in SERIES_MAP.items():
        entries = record.get(source_key, [])
        series: dict[str, dict[str, float | None]] = {}
        for entry in entries:
            metric = entry.get("index")
            for period, value in entry.items():
                if period == "index":
                    continue
                series.setdefault(str(period), {})[metric] = value
        out[target_key] = series
    return out


def main():
    parser = argparse.ArgumentParser(description="Fetch cninfo statement series for one stock code.")
    parser.add_argument("--scode", required=True, help="Stock code, e.g. 601336")
    parser.add_argument(
        "--sign",
        default="4",
        help="Statement sign parameter used by cninfo. Defaults to 4.",
    )
    parser.add_argument("--output", required=True, help="Output JSON file path.")
    args = parser.parse_args()

    payload = {"scode": args.scode, "sign": args.sign, "sources": {}, "series": {}}

    for name in ENDPOINTS:
        url = endpoint_url(name, args.scode, args.sign)
        try:
            response = fetch_json(url)
        except urllib.error.URLError as exc:
            raise SystemExit(f"failed to fetch {name}: {exc}") from exc
        payload["sources"][name] = url
        payload["series"][name] = reshape_records(response["data"]["records"])

    Path(args.output).write_text(json.dumps(payload, indent=2, ensure_ascii=True))


if __name__ == "__main__":
    main()
