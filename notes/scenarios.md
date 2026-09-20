# System design scenarios

One line per scenario the daily card has asked, newest at the bottom. The
morning task reads this so it does not repeat itself, and it doubles as a bank
to re-answer later — a scenario you answered in October is worth a second pass
in February.

Format: `YYYY-MM-DD — <one line naming the situation and the pressure>`

---

2026-09-20 — payments webhook receiver holding 4,000 in-flight requests while fulfilment is down; sync receive path vs durable queue
2026-09-20 — delivery dispatch double-assigning couriers at 900 orders/sec; unconditional UPDATE vs conditional write contention vs single assigner per cell
