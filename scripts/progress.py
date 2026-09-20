"""
Where the preparation actually stands, read from the files themselves.

    python3 scripts/progress.py                 summary + what needs attention
    python3 scripts/progress.py --week 3        one week
    python3 scripts/progress.py --folder 02     one pattern folder
    python3 scripts/progress.py --full          every row, nothing truncated
    python3 scripts/progress.py --json          machine readable

Status comes from the code, not from a checklist:

    todo      both methods are still `pass`
    brute     brute force written, optimal not
    done      both written

and the flags come from the docstring:

    hinted        `Hints used: Y`      -> shorter revision intervals
    unsolved      `Solved unaided: N`  -> could not finish it; shortest of all
    no notes      BRUTE FORCE / OPTIMAL / KEY INSIGHT still the template
    no thinking   MY THINKING never filled in
"""
import argparse
import datetime as dt
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import prep_lib as L


def _tags(row):
    tag = "  [brute only]" if row["status"] == "brute" else ""
    tag += "  [optimal only]" if row["status"] == "optimal" else ""
    tag += "" if row["notes_filled"] or row["status"] == "todo" else "  [no notes]"
    tag += "  [no thinking]" if row["status"] == "done" and not row["thinking_filled"] else ""
    tag += "  [hinted]" if row["hinted"] else ""
    tag += "  [unsolved]" if row["failed"] else ""
    return tag


def _line(row):
    return f"    {row['number']:>4}  {row['title'][:44]:<44} {row['difficulty']:<7}{_tags(row)}"


def _bar(done, total, width=22):
    filled = 0 if not total else round(width * done / total)
    return "#" * filled + "." * (width - filled)


def report(rows, full=False, today=None):
    today = today or dt.date.today()
    week = L.current_week(today)
    cap = 10_000 if full else 12

    done = [r for r in rows if r["status"] == "done"]
    core = [r for r in rows if r["tier"] == "Core"]
    core_done = [r for r in core if r["status"] == "done"]

    print(f"\n  {today:%a %d %b %Y}   week {week} of {L.TOTAL_WEEKS}   {L.phase_of(week)}")
    print(f"  {'-' * 68}")
    print(f"  all      {_bar(len(done), len(rows))}  {len(done):>3} / {len(rows)}")
    print(f"  core     {_bar(len(core_done), len(core))}  {len(core_done):>3} / {len(core)}")

    partial = [r for r in rows if r["status"] in ("brute", "optimal")]
    if partial:
        print(f"  started  {len(partial)} file(s) half written")

    print(f"\n  BY FOLDER")
    for name in sorted({r["folder"] for r in rows}):
        fr = [r for r in rows if r["folder"] == name]
        fd = [r for r in fr if r["status"] == "done"]
        weeks = sorted({r["week"] for r in fr})
        span = f"W{weeks[0]}" if len(weeks) == 1 else f"W{weeks[0]}-{weeks[-1]}"
        flag = "  <- now" if weeks[0] <= week <= weeks[-1] else ""
        print(f"    {name:<28} {span:<8} {_bar(len(fd), len(fr), 12)} {len(fd):>3}/{len(fr):<4}{flag}")

    behind = [r for r in rows
              if r["tier"] == "Core" and r["week"] < week and r["status"] != "done"]
    if behind:
        print(f"\n  BEHIND  ({len(behind)} core problems scheduled before this week)")
        for r in sorted(behind, key=lambda r: (r["week"], r["number"]))[:cap]:
            print(f"    W{r['week']:<3} {r['number']:>4}  {r['title'][:40]:<40} {r['folder']}{_tags(r)}")
        if len(behind) > cap:
            print(f"    ... and {len(behind) - cap} more   (--full to list)")

    this_week = [r for r in rows if r["week"] == week and r["status"] != "done"]
    if this_week:
        print(f"\n  THIS WEEK  ({len([r for r in this_week if r['tier'] == 'Core'])} core left)")
        for r in sorted(this_week, key=lambda r: (r["tier"] != "Core", r["number"]))[:cap]:
            star = "*" if r["tier"] == "Core" else " "
            print(f"   {star}{_line(r)[1:]}")
        if len(this_week) > cap:
            print(f"    ... and {len(this_week) - cap} more   (--full to list)")

    due = [r for r in L.revision_pool(rows, today) if r["overdue"] >= 0]
    if due:
        print(f"\n  REVISION DUE  ({len(due)})")
        for r in due[:cap]:
            when = "today" if r["overdue"] == 0 else f"{r['overdue']}d overdue"
            print(f"    {r['number']:>4}  {r['title'][:40]:<40} sweep {r['reps'] + 1}, {when}")

    resolve = [r for r in rows if r["hinted"] or r["failed"]]
    if resolve:
        print(f"\n  RE-SOLVE  (needed help, so these come back sooner)")
        for r in sorted(resolve, key=lambda r: r["week"])[:cap]:
            print(_line(r))

    thin = [r for r in rows if r["status"] == "done"
            and (not r["notes_filled"] or not r["thinking_filled"])]
    if thin:
        print(f"\n  WRITE-UP MISSING  ({len(thin)} solved, docstring still the template)")
        for r in sorted(thin, key=lambda r: r["week"])[:cap]:
            print(_line(r))
        if len(thin) > cap:
            print(f"    ... and {len(thin) - cap} more   (--full to list)")

    open_weak = [w for w in L.weak_topics() if w["status"] == "open"]
    if open_weak:
        print(f"\n  WEAK TOPICS  ({len(open_weak)} open)")
        for w in open_weak:
            print(f"    {w['title'][:50]:<50} {w['slip'][:40]}")
    print()


def main():
    ap = argparse.ArgumentParser(description="Where the dsa-prep preparation stands.")
    ap.add_argument("--week", type=int, help="only problems scheduled in this week")
    ap.add_argument("--folder", help="only this solutions/ folder (substring, e.g. 02)")
    ap.add_argument("--full", action="store_true", help="do not truncate lists")
    ap.add_argument("--json", action="store_true", help="dump rows as JSON")
    args = ap.parse_args()

    errors = []
    rows = L.load(args.folder, args.week, errors)
    for e in errors:
        print(f"!! could not parse {e['file']}: {e['error']}", file=sys.stderr)
    if not rows:
        print("no matching problems", file=sys.stderr)
        return 1
    if args.json:
        json.dump({"week": L.current_week(), "rows": rows}, sys.stdout, indent=2, default=str)
        print()
        return 0
    report(rows, full=args.full)
    return 0


if __name__ == "__main__":
    sys.exit(main())
