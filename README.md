# dsa-prep

Interview preparation for SDE-2 backend. No fixed date.

Targets: **Amazon**, **Google**, and **Indian product/startup companies** — Zomato, Swiggy,
CRED, Razorpay, Flipkart, PhonePe, Meesho, Groww, Zepto, Navi, Dream11.

System design is **not** here — that is Hello Interview premium. Two thinner copies
of the same material is worse than one good one.

## How this works

The sheet is a **queue, not a calendar**. 300 problems in one order; take the next
one when you sit down. Nothing is scheduled to a date, so nothing is ever late.

The previous version of this repo was a 35-week calendar over 454 problems. It
assigned work to days, and a busy stretch at the office turned into "60 problems
behind" — at which point it stopped being opened. 5 of 454 got solved. The queue
removes that failure mode entirely: a dead week costs position, not progress.

```bash
python3 scripts/plan.py           # what to do this sitting
python3 scripts/plan.py --n 2     # short sitting
python3 scripts/plan.py --tier A  # rough week: must-do spine only
python3 scripts/plan.py --revise 5
python3 scripts/plan.py --drill 5 # name the pattern, do not solve
python3 scripts/progress.py       # where you stand
```

## The sheet

[SHEET.md](SHEET.md) — 300 problems, 21 sections.

- **Spine**: Hello Interview's 92 problems, each linked to its lesson.
- **Patch**: 46 covering what HI does not teach — hashing and strings, union-find,
  design-a-data-structure (LRU cache), bit and math, DP breadth, BST/trees.
- **Depth**: 162 more that build the same patterns — the variants that teach a twist
  (80 after 26, 438 after 3, 235 after 236, 518 after 322) rather than new material.

| tier | meaning | count |
|---|---|---|
| A | the spine — a bad week still does these | 101 |
| B | core — normal sittings | 129 |
| C | useful depth — only if ahead | 40 |
| D | **least important in its section — drop these first** | 30 |

Within a section the order is A → B → C → D, easiest first, so working top-down always
does the important problems before the optional ones. **Dropping every C and D still
leaves all 21 patterns covered** — it costs depth, never a pattern. That is the point of
the tiers: the sheet shrinks under pressure instead of being abandoned.

```bash
python3 scripts/progress.py --tier D   # what you can safely skip
python3 scripts/plan.py --tier A       # rough week: spine only
```

## Company tags

Each problem's `Asked:` line carries `Amazon`, `Google` and/or `India`.

Amazon and Google tags are per-problem judgements. **The `India` tag is a rule, not scraped
data**: Easy/Medium, tier A or B, in the core sections. Those rounds are one or two DSA
interviews of standard problems plus LLD, and rarely reach Dijkstra, MST, bitmask DP or hard
graph work. 94 of 138 qualify. Nobody has a verified question bank for these companies — treat
the tag as "this is the shape of what they ask", never as "they asked this one".

```bash
python3 scripts/export_xlsx.py --out ~/Desktop/"Interview prep"/DSA_Queue_HI.xlsx
```

Regenerates the 3-tab spreadsheet (Queue, Progress, Patterns) **from this repo**. The repo is
the source of truth; the spreadsheet is a view. Editing the spreadsheet does not feed back —
re-run the export instead. Needs `openpyxl`, so use a venv if the system python refuses:

```bash
python3 -m venv ~/.venvs/xlsx && ~/.venvs/xlsx/bin/pip install openpyxl
```

## Layout

```text
SHEET.md        the queue
solutions/      21 sections, mirroring the sheet
patterns/       pattern guides
theory/         os, networks, dbms, lld
notes/          study-log.md, weak-topics.md
scripts/        prep_lib.py, plan.py, progress.py
archive/        the old 454-problem calendar, kept for reference
```

## Per-problem file

Each file carries the problem, a `MY THINKING` block filled in **while** solving,
and the brute-force → limitation → optimal progression written out afterwards.
Run it directly to test both methods:

```bash
python3 solutions/01-two-pointers/0011-container-with-most-water.py
```

`Solved unaided: Y` the moment a working solution comes out, hints or not.
`Hints used: Y` is the field that matters — it shortens the revision interval.

## Revision

Spaced from `Solved on:`, sweeping at 3/7/21/60/120 days — shortened to 2/5/14/40/90
when a hint was used. Revising means stating the approach and complexity **from
memory first**, then opening the file. If that fails, it goes to `notes/weak-topics.md`.
