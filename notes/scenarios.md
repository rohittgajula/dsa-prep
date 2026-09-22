# System design scenarios

One line per scenario the daily card has asked, newest at the bottom. The
morning task reads this so it does not repeat itself, and it doubles as a bank
to re-answer later — a scenario you answered in October is worth a second pass
in February.

Format: `YYYY-MM-DD — <one line naming the situation and the pressure>`

---

2026-09-20 — payments webhook receiver holding 4,000 in-flight requests while fulfilment is down; sync receive path vs durable queue
2026-09-20 — delivery dispatch double-assigning couriers at 900 orders/sec; unconditional UPDATE vs conditional write contention vs single assigner per cell
2026-09-21 — marketplace search typeahead at 120k req/sec, p99 40ms -> 310ms as the prefix cache miss rate grew; debounce vs in-process trie for the head vs ES for the tail, paid in staleness and no personalization
2026-09-22 — team chat messages table 1.9B rows/2.4TB with int4 serial ~6 weeks from overflow; in-place ALTER TYPE outage vs shadow bigint column with throttled backfill, paid in weeks of lead time and every dependent FK
