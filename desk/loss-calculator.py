#!/usr/bin/env python3
"""Scope creep loss desk.

Files only. No network. No Gamut. No API keys.

  python3 desk/loss-calculator.py
  python3 desk/loss-calculator.py --trade web_design --rate 120 --unpaid-hours 8
  python3 desk/loss-calculator.py --lookup extra_page --trade copywriting
  python3 desk/loss-calculator.py --csv jobs.csv
  python3 desk/loss-calculator.py --annual --trade web_design

jobs.csv columns: trade,request_code,unpaid_hours,rate_usd,absorbed (yes/no)
"""

from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARCH = ROOT / "data" / "scope-change-archetypes.csv"
BENCH = ROOT / "data" / "industry-loss-bench.csv"


def load_csv(path: Path) -> list[dict]:
    with path.open(encoding="utf-8") as f:
        return list(csv.DictReader(f))


def money(n: float) -> str:
    return f"${n:,.0f}"


def lookup(trade: str, code: str, rows: list[dict]) -> dict | None:
    trade = trade.lower()
    code = code.lower()
    for r in rows:
        if r["trade"] == trade and r["request_code"] == code:
            return r
    return None


def annual_leak(trade: str, bench: list[dict]) -> dict:
    sub = [r for r in bench if r["trade"] == trade]
    hours = sum(float(r["modeled_unpaid_scope_hours"]) for r in sub)
    creep = sum(int(r["modeled_creep_loss_usd"]) for r in sub)
    late = sum(int(r["modeled_late_pay_drag_usd"]) for r in sub)
    return {"months": len(sub), "hours": hours, "creep": creep, "late": late, "total": creep + late}


def score_job(unpaid_hours: float, rate: float, absorbed: bool) -> dict:
    leak = unpaid_hours * rate if absorbed else 0.0
    recovered = unpaid_hours * rate if not absorbed else 0.0
    return {"leak": leak, "recovered": recovered}


def print_table(headers: list[str], rows: list[list[str]]) -> None:
    widths = [len(h) for h in headers]
    for row in rows:
        for i, cell in enumerate(row):
            widths[i] = max(widths[i], len(cell))
    fmt = "  ".join(f"{{:<{w}}}" for w in widths)
    print(fmt.format(*headers))
    print(fmt.format(*["-" * w for w in widths]))
    for row in rows:
        print(fmt.format(*row))


def main() -> None:
    p = argparse.ArgumentParser(description="Scope creep loss desk")
    p.add_argument("--trade", default="web_design")
    p.add_argument("--rate", type=float)
    p.add_argument("--unpaid-hours", type=float)
    p.add_argument("--lookup", help="request_code to price from the archetype bench")
    p.add_argument("--csv", help="jobs file")
    p.add_argument("--annual", action="store_true")
    args = p.parse_args()

    arch = load_csv(ARCH)
    bench = load_csv(BENCH)

    if args.annual:
        a = annual_leak(args.trade, bench)
        print(f"Modeled 12-month leak for {args.trade} (not a survey):")
        print(f"  unpaid hours {a['hours']:.1f}")
        print(f"  creep {money(a['creep'])} + late-pay drag {money(a['late'])} = {money(a['total'])}")
        return

    if args.lookup:
        row = lookup(args.trade, args.lookup, arch)
        if not row:
            print(f"no archetype for trade={args.trade} request={args.lookup}", file=sys.stderr)
            sys.exit(1)
        rate = args.rate if args.rate is not None else float(row["rate_usd"])
        hours = float(row["hours_mid"])
        print(f"{row['archetype_id']}  {row['trade']} / {row['request_code']}")
        print(f"  {row['request_label']}")
        print(f"  hours {row['hours_low']}–{row['hours_high']} (mid {hours})")
        print(f"  fee at ${rate:.0f}/h mid: {money(hours * rate)}")
        print(f"  date shift {row['date_shift_days']}d  move={row['default_move']}  pause={row['pause_if_unsigned']}")
        print(f"  absorb risk: {row['absorb_unpaid_risk']}")
        return

    if args.csv:
        jobs = load_csv(Path(args.csv))
        leak = recovered = 0.0
        table = []
        for j in jobs:
            hours = float(j.get("unpaid_hours") or 0)
            rate = float(j.get("rate_usd") or args.rate or 0)
            absorbed = str(j.get("absorbed", "yes")).lower() in {"yes", "y", "true", "1"}
            s = score_job(hours, rate, absorbed)
            leak += s["leak"]
            recovered += s["recovered"]
            table.append(
                [
                    j.get("trade", ""),
                    j.get("request_code", ""),
                    f"{hours:.1f}h",
                    money(hours * rate),
                    "absorbed" if absorbed else "billed",
                ]
            )
        print_table(["trade", "request", "hours", "value", "status"], table)
        print()
        print(f"absorbed leak {money(leak)}   billed/recovered {money(recovered)}")
        return

    if args.unpaid_hours is not None:
        rate = args.rate
        if rate is None:
            hit = next((r for r in arch if r["trade"] == args.trade), None)
            rate = float(hit["rate_usd"]) if hit else 100.0
        print(f"{args.trade}: {args.unpaid_hours:.1f}h × ${rate:.0f} = {money(args.unpaid_hours * rate)} if absorbed unpaid")
        print("Send the change order before that number becomes a donation.")
        return

    print("Scope Creep Loss Desk — 12 trades, 192 archetypes, 144-row monthly bench")
    print("Examples:")
    print("  python3 desk/loss-calculator.py --annual --trade web_design")
    print("  python3 desk/loss-calculator.py --lookup cms_blog --trade web_design")
    print("  python3 desk/loss-calculator.py --unpaid-hours 8 --rate 120")
    print("  python3 desk/loss-calculator.py --csv examples/sample-jobs.csv")


if __name__ == "__main__":
    main()
