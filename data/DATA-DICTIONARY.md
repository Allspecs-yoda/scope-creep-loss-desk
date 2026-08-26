# Data dictionary

## `scope-change-archetypes.csv` (192 rows = 12 trades × 16 requests)

| column | meaning | accurate? |
| --- | --- | --- |
| rate_usd | 2026 public median for that trade | **cited** — see SOURCES.md |
| rate_source | URL/page the median came from | cited |
| hours_* | Extra hours for one mid-job request | **prior** — overwrite |
| fee_*_usd | `round(hours * rate_usd)` | **exact given hours and rate** |
| date_shift_days | 0 / 2 / 4 / 8 from hours bands; rush = -3 | rule, not a survey |
| absorb_unpaid_risk | low <4h, med <8h, high ≥8h | rule |
| default_move | change_order if hours_mid ≥ 3 else log_only | rule |

## `industry-loss-bench.csv` (144 rows)

| column | meaning | accurate? |
| --- | --- | --- |
| assumed_rate_usd | same cited median | cited |
| modeled_unpaid_scope_hours | `round(0.5 * mean(med/high hours) * seasonal_index, 1)` | formula |
| modeled_creep_loss_usd | `round(hours * rate)` | exact given inputs |
| late_pay_factor | modeled prior | **not a survey** |
| modeled_total_leak_usd | creep + late | exact given inputs |
