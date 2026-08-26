# Worked example — brochure site + surprise blog

Sold: $2,400 / 10-day five-page brochure site.
Day 4 Slack: “also add a blog and a member login.”

## Desk lookup (do this first)

```bash
python3 desk/loss-calculator.py --lookup cms_blog --trade web_design
python3 desk/loss-calculator.py --lookup auth_login --trade web_design
```

Modeled mid: blog is an 8-hour-class add; login is a later-phase auth job.

## What shipped to the client

- Blog → priced change order (hours from the desk, rate from the freelancer’s books).
- Login → **hold**, later phase.
- Date moved; unused revision round slid after blog launch.

## Why the data is here

The CSVs exist so you do not invent hours in the heat of the Slack thread. Overwrite them with your own books when you have them. Nothing in this example is a claimed sale.
