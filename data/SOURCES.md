# Sources and honesty

Rates in `scope-change-archetypes.csv` and `industry-loss-bench.csv` are **cited 2026 public medians**, not Dakota’s books and not claimed survey results.

## Rate medians used (`rate_usd`)

| trade | rate_usd | source |
| --- | ---: | --- |
| web_design | 105 | WhatShouldICharge 2026 median, Web Developers — https://whatshouldicharge.io/statistics/freelance-rates-2026 |
| graphic_design | 75 | same page, Graphic Designers |
| copywriting | 85 | same page, Copywriters |
| video_edit | 85 | same page, Video Editors |
| ui_ux | 120 | same page, UI/UX Designers |
| social_mgmt | 85 | same page, Social Media Managers |
| illustration | 100 | same page, Illustrators |
| photography | 150 | same page, Photographers |
| webflow | 100 | same page, Webflow Developers |
| dev_app | 140 | same page, Software Developers |
| dev_wordpress | 65 | TryPros 2026 median, WordPress Development — https://trypros.com/freelance-market-rates-2026/ |
| bookkeeping | 45 | TryPros 2026 median, Bookkeeping |

WhatShouldICharge states those medians are BLS-derived and free to republish with a link. TryPros aggregates platform ranges (Upwork, Fiverr, Toptal, Hubstaff, Jobbers, Payoneer, PayScale) through March 2026.

## What is *not* a measurement

- `hours_*` — engineering priors for one extra request on an already-sold job. Overwrite with your books.
- `seasonal_index` and `late_pay_factor` — labeled modeled priors, not a survey.
- Monthly leak dollars — `unpaid_h = round(0.5 * mean(med/high hours) * seasonal_index, 1)` then `creep = round(unpaid_h * rate)`.

## What *is* exact

- `fee_*_usd = round(hours * rate_usd)` for every row (checked at generate time).
- 12 trades × 16 requests = 192 unique archetype keys.
- 12 trades × 12 months = 144 bench rows.

If a public median moves, replace `rate_usd` and rerun `desk/loss-calculator.py`. Do not advertise these CSVs as “Dakota’s client data.”
