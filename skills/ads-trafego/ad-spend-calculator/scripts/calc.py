#!/usr/bin/env python3
"""Ad spend calculator — funnel math + viability flags + 3 scenarios.

Usage:
    python calc.py --revenue 10000 --aov 197 --margin 0.85 --cvr 0.03 --cpc 2.00
"""
import argparse


def calc(revenue_goal: float, aov: float, margin: float, cvr: float, cpc: float) -> dict:
    sales_needed = revenue_goal / aov
    clicks_needed = sales_needed / cvr
    ad_spend = clicks_needed * cpc
    cpa = ad_spend / sales_needed
    max_cpa = aov * margin
    roas = revenue_goal / ad_spend if ad_spend else 0
    profit = (revenue_goal * margin) - ad_spend

    flags = []
    if cpa > max_cpa:
        flags.append("ALERT: CPA exceeds margin — losing money on every sale")
    elif cpa > 0.5 * aov:
        flags.append("WARNING: CPA above 50% of AOV — tight margins")
    if roas > 5:
        flags.append("ALERT: required ROAS > 5x — aggressive, may be unachievable")
    if ad_spend > 10000:
        flags.append("NOTE: monthly spend > $10K — recommend phased scaling")

    return {
        "sales_needed": round(sales_needed, 1),
        "clicks_needed": round(clicks_needed),
        "ad_spend": round(ad_spend, 2),
        "cpa": round(cpa, 2),
        "max_cpa": round(max_cpa, 2),
        "roas": round(roas, 2),
        "profit": round(profit, 2),
        "flags": flags,
    }


def scenarios(revenue_goal: float, aov: float, margin: float, cvr: float, cpc: float) -> dict:
    return {
        "conservative": calc(revenue_goal * 0.6, aov, margin, cvr, cpc),
        "base": calc(revenue_goal, aov, margin, cvr, cpc),
        "aggressive": calc(revenue_goal * 1.5, aov, margin, cvr, cpc),
    }


def fmt(label: str, m: dict) -> str:
    lines = [f"\n--- {label} ---"]
    lines.append(f"  Sales needed:   {m['sales_needed']}")
    lines.append(f"  Clicks needed:  {m['clicks_needed']}")
    lines.append(f"  Ad spend:       ${m['ad_spend']:,}")
    lines.append(f"  CPA:            ${m['cpa']} (max viable: ${m['max_cpa']})")
    lines.append(f"  ROAS:           {m['roas']}x")
    lines.append(f"  Profit:         ${m['profit']:,}")
    for f in m["flags"]:
        lines.append(f"  {f}")
    return "\n".join(lines)


def main():
    p = argparse.ArgumentParser(description="Ad spend calculator")
    p.add_argument("--revenue", type=float, required=True, help="Monthly revenue goal ($)")
    p.add_argument("--aov", type=float, required=True, help="Average order value ($)")
    p.add_argument("--margin", type=float, default=0.60, help="Profit margin (0-1), default 0.60")
    p.add_argument("--cvr", type=float, default=0.02, help="Conversion rate (0-1), default 0.02")
    p.add_argument("--cpc", type=float, default=1.50, help="Avg cost per click ($), default 1.50")
    args = p.parse_args()

    s = scenarios(args.revenue, args.aov, args.margin, args.cvr, args.cpc)
    print(f"Inputs: revenue=${args.revenue:,} AOV=${args.aov} margin={args.margin*100:.0f}% "
          f"CVR={args.cvr*100:.1f}% CPC=${args.cpc}")
    print(fmt("CONSERVATIVE (60% of goal)", s["conservative"]))
    print(fmt("BASE CASE", s["base"]))
    print(fmt("AGGRESSIVE (150% of goal)", s["aggressive"]))


if __name__ == "__main__":
    main()
