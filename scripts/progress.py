"""
Where he actually stands.

    python3 scripts/progress.py              the whole sheet
    python3 scripts/progress.py --section 09 one section
    python3 scripts/progress.py --tier A     just the must-do spine
    python3 scripts/progress.py --json       rows, for filtering

There is deliberately no "behind" count. The sheet is a queue, not a calendar:
nothing on it is late, it is simply still ahead of him.
"""
import argparse
import datetime as dt
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import prep_lib as L

BAR = 12
NAMES = {"A": "must-do", "B": "normal", "C": "if ahead"}


def bar(done, total, width=BAR):
    filled = 0 if not total else round(width * done / total)
    return "#" * filled + "." * (width - filled)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--section")
    ap.add_argument("--tier", choices="ABC")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--full", action="store_true")
    a = ap.parse_args()

    rows = L.load(folder=a.section, sheet=a.tier)
    rows.sort(key=lambda r: r["order"])
    if a.json:
        json.dump({"rows": rows}, sys.stdout, indent=2, default=str)
        return

    today = dt.date.today()
    done = [r for r in rows if r["status"] == "done"]
    print(f"\n  {today:%a %d %b %Y}   {len(done)} / {len(rows)} solved")

    for tier in "ABC":
        t = [r for r in rows if r["sheet"] == tier]
        if not t:
            continue
        d = sum(r["status"] == "done" for r in t)
        print(f"  tier {tier} {NAMES[tier]:<9} {bar(d, len(t))}  {d:>3} / {len(t)}")

    print("\n  BY SECTION")
    for folder in sorted({r["folder"] for r in rows}):
        s = [r for r in rows if r["folder"] == folder]
        d = sum(r["status"] == "done" for r in s)
        flag = "  <- here" if folder == L.current_folder(rows) else ""
        print(f"    {folder:<26} {bar(d, len(s))}  {d:>2}/{len(s):<3}{flag}")

    nxt = L.up_next(rows, 20 if a.full else 8)
    if nxt:
        print(f"\n  UP NEXT  ({sum(r['status'] == 'todo' for r in rows)} left on the sheet)")
        for r in nxt:
            asked = "" if r["asked"] == "-" else r["asked"]
            print(f"    {r['order']:03d} {r['number']:>5}  {r['title'][:42]:<42} "
                  f"{r['difficulty']:<7} {r['sheet']}  {asked}")

    due = L.revision_pool(rows, today)
    if due:
        print(f"\n  DUE FOR A SWEEP  ({len(due)})")
        for r in due[:8]:
            print(f"    {r['number']:>5}  {r['title'][:42]:<42} {r['overdue']:>3}d overdue")

    flagged = [r for r in done if not r["notes_filled"]]
    if flagged:
        print(f"\n  SOLVED BUT DOCSTRING STILL BLANK  ({len(flagged)})")
        for r in flagged[:8]:
            print(f"    {r['number']:>5}  {r['title'][:42]}")
    print()


if __name__ == "__main__":
    main()
