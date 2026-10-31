# dsa-prep

Interview preparation for SDE-2 backend. Target: **Amazon and Google**, no fixed date.

System design is **not** here — that is Hello Interview premium. Two thinner copies
of the same material is worse than one good one.

## How this works

The sheet is a **queue, not a calendar**. 138 problems in one order; take the next
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

[SHEET.md](SHEET.md) — 138 problems, 21 sections.

- **Spine**: Hello Interview's 92 problems, in its order, each linked to its lesson.
- **Patch**: 46 problems covering what HI does not teach — hashing and strings,
  union-find, design-a-data-structure (LRU cache), bit and math, plus DP breadth
  (knapsack, coin change, edit distance) and the BST/tree problems Google asks.

Tiers: **A** (73) is the spine — a bad week still does these. **B** (45) is a normal
sitting. **C** (20) only if ahead.

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
