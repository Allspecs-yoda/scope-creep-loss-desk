# Scope Creep Loss Desk

A $49 freelancer desk: **192** priced change archetypes (cited 2026 median rates), a 144-row leak bench with published formulas, a local calculator, and send-today recap / change-order templates.

## Who it's for

Solo freelancers who keep absorbing “can you also…” in chat and want numbers — not another Notion OS.

## Multi-buyer (yes)

This is a **non-exclusive, resellable digital pack**. Checkout is reusable. Ten people can pay; ten people get the same zip. Your payment licenses your practice **and** lets you resell copies (see `LICENSE`).

Delivery is the GitHub repo (clone or Download ZIP). No Gamut account. No seat limit. No API key.

## What's included

- `data/scope-change-archetypes.csv` — 192 request × trade rows; `rate_usd` is a cited 2026 median; fees are `hours × rate`
- `data/industry-loss-bench.csv` — 12 trades × 12 months; formulas in the file and in `data/SOURCES.md` (not a survey)
- `desk/loss-calculator.py` — lookup, annual leak, and a jobs CSV scorer (offline)
- `templates/` — recap, emails, change order
- `examples/` — sample jobs + one worked brochure-site thread

## Quick start

```bash
python3 desk/loss-calculator.py --lookup cms_blog --trade web_design
python3 desk/loss-calculator.py --annual --trade web_design
python3 desk/loss-calculator.py --csv examples/sample-jobs.csv
```

Then paste `templates/recap-email.md` B and attach `templates/change-order.md`.

## Price

**$49 USD**, one-time, unlimited buyers.

Pay with the Stripe Payment Link in `PRICE.md`. After payment, open a GitHub issue titled `CLAIM: Scope Creep Loss Desk` and include the receipt last-4. If checkout is down, star + watch `foundry-ledger` and open the same CLAIM issue.

This listing does not claim any sales.

## Tail buyers

Watch **https://github.com/Allspecs-yoda/foundry-ledger** (GitHub Watch → All activity). New SKUs land on `OFFERS.md`, `catalog.json`, and `feed.xml`. No email list. No DMs.

## License

Commercial resale license — see `LICENSE`. Use on your jobs; resell copies if you keep SOURCES.md.

## Foundry

Shipped by Night Shift Foundry for Dakota (@Allspecs-yoda).
SKU: `NSF-20260826-SCOPE-LOSS-DESK` | Decision: list | Cycle: 2026-08-26 | Ticket: $49
