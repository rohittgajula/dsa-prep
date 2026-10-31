"""
What to do when he sits down. Pull-based: there is no daily quota and nothing
is ever late. Take the next few off the queue, sweep whatever revision is due.

    python3 scripts/plan.py              a normal sitting
    python3 scripts/plan.py --n 3        a short sitting
    python3 scripts/plan.py --tier A     bad week: must-do spine only
    python3 scripts/plan.py --revise 5   just a revision set
    python3 scripts/plan.py --drill 5    name the pattern, do not solve
    python3 scripts/plan.py --drill 5 --answers
"""
import argparse
import datetime as dt
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import prep_lib as L

HI = "hellointerview.com/learn/code"


def show(r):
    asked = "" if r["asked"] == "-" else f"   [{r['asked']}]"
    print(f"    {r['order']:03d}  {r['number']:>5}  {r['title'][:44]:<44} {r['difficulty']:<7}{asked}")
    print(f"           {r['file']}")


def build(rows, today, n=4, tiers="ABC"):
    """The sitting, as data. Used by daily_card.py.

    No week, no quota, no "behind" - just the head of the queue plus whatever
    revision and theory is due.
    """
    nxt = L.up_next(rows, n, tiers)
    mixed = L.interleave_pool(rows, today, exclude=[r["file"] for r in nxt])
    done_theory = L.theory_done()
    nt = L.theory_next(done_theory, 1)
    return {
        "today": today,
        "section": L.current_folder(rows),
        "solve": nxt,
        "mixed": mixed[0] if mixed else None,
        "revise": L.revision_pool(rows, today),
        "theory": Path(nt[0]["path"]) if nt else None,
        "theory_due": L.theory_revision_pool(today),
        "left": sum(r["status"] == "todo" for r in rows),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=4)
    ap.add_argument("--tier", default="ABC")
    ap.add_argument("--revise", type=int)
    ap.add_argument("--drill", type=int)
    ap.add_argument("--answers", action="store_true")
    a = ap.parse_args()

    rows = L.load()
    today = dt.date.today()

    if a.drill:
        print("\n  DRILL - name the pattern, the key insight and the complexity.")
        print("  60 seconds each, out loud. Do not solve them.\n")
        for i, r in enumerate(L.drill_pick(rows, a.drill, today), 1):
            print(f"  {i}. {r['statement'].splitlines()[0][:70]}")
            if a.answers:
                print(f"     -> {r['pattern']}  ({r['title']})")
            print()
        return

    if a.revise:
        due = L.revision_pool(rows, today)[:a.revise]
        print("\n  REVISION - state the approach and complexity from memory FIRST,")
        print("  then open the file. If you cannot, it goes to weak-topics.\n")
        for r in due:
            show(r)
        if not due:
            print("    nothing due")
        print()
        return

    nxt = L.up_next(rows, a.n, a.tier)
    here = L.current_folder(rows)
    print(f"\n  {today:%a %d %b %Y}   section: {here}")

    lesson = next((r["lesson"] for r in nxt if r["lesson"]), None)
    if lesson:
        print(f"  Read the lesson first if this section is new: {lesson}")

    print(f"\n  SOLVE  (take as many as the sitting allows)")
    for r in nxt:
        show(r)

    mixed = L.interleave_pool(rows, today, exclude=[r["file"] for r in nxt])
    if mixed:
        print("\n  MIXED  (earlier pattern, unlabelled - name it before you write)")
        show(mixed[0])

    due = L.revision_pool(rows, today)
    if due:
        print(f"\n  SWEEP  ({len(due)} due - approach and complexity from memory first)")
        for r in due[:3]:
            print(f"    {r['number']:>5}  {r['title'][:44]:<44} {r['overdue']:>3}d")

    nt = L.theory_next(L.theory_done(), 1)
    if nt:
        print(f"\n  THEORY   {nt[0]['path']}")

    weak = L.weak_topics()
    open_ = [w for w in weak if str(w.get("status", "")).startswith("open")]
    if open_:
        print(f"\n  OPEN WEAK TOPICS  ({len(open_)})")
        for w in open_[:3]:
            print(f"    {w.get('title', '?')[:70]}")
    print()


if __name__ == "__main__":
    main()
