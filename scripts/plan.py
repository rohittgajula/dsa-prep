"""
What to study today, and what is coming next.

    python3 scripts/plan.py              today + the next 4 days
    python3 scripts/plan.py --days 7     a week ahead
    python3 scripts/plan.py --revise 5   just pull a revision set
    python3 scripts/plan.py --drill 5    name the pattern, do not solve
    python3 scripts/plan.py --drill 5 --answers
    python3 scripts/plan.py --json       machine readable

The plan is derived, never stored: it comes from which files have real code in
them, which theory files the study log says were read, when each solved problem
is next due for a sweep, and what is still open in notes/weak-topics.md. Solve
something, log it, and tomorrow's plan changes on its own.
"""
import argparse
import datetime as dt
import json
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import prep_lib as L

MAX_PER_DAY = 4


def build(rows, today=None, days=4):
    today = today or dt.date.today()
    week = L.current_week(today)

    behind = sorted([r for r in rows if r["tier"] == "Core"
                     and r["week"] < week and r["status"] != "done"],
                    key=lambda r: (r["week"], r["number"]))
    core_now = sorted([r for r in rows if r["week"] == week
                       and r["tier"] == "Core" and r["status"] != "done"],
                      key=lambda r: r["number"])
    stretch_now = sorted([r for r in rows if r["week"] == week
                          and r["tier"] != "Core" and r["status"] != "done"],
                         key=lambda r: r["number"])
    ahead = sorted([r for r in rows if r["week"] == week + 1
                    and r["tier"] == "Core" and r["status"] != "done"],
                   key=lambda r: r["number"])

    days_left = max(1, (L.week_start(week + 1) - today).days)
    per_day = min(MAX_PER_DAY, max(1, math.ceil(len(core_now) / days_left)))

    queue = behind + core_now + stretch_now + ahead

    done_theory = L.theory_done()
    track, files, expected, _ = L.theory_plan(week, done_theory)
    unread = [f for f in files if str(f.relative_to(L.ROOT)) not in done_theory]
    read_count = len(files) - len(unread)
    _, lo, hi = L.track_for_week(week)
    cadence = max(1, round(7 * (hi - lo + 1) / max(1, len(files))))

    theory_due = [t for t in L.theory_revision_pool(today) if t["overdue"] >= 0]
    pool = L.revision_pool(rows, today)
    shown = set()
    mixed_pool = L.interleave_pool(rows, today, exclude={r["file"] for r in queue})
    schedule, q, t = [], list(queue), list(unread)

    for offset in range(days):
        date = today + dt.timedelta(days=offset)
        take = q[:per_day]
        q = q[per_day:]

        theory = None
        if t and offset % cadence == 0:
            theory = t.pop(0)

        revise = []
        for r in pool:
            if r["file"] in shown:
                continue
            if r["due"] <= date:
                revise.append(r)
                shown.add(r["file"])
            if len(revise) >= 3:
                break
        if offset == 0 and not revise:
            for r in L.pick_revision(rows, 1, today):
                if r["file"] not in shown:
                    revise.append(r)
                    shown.add(r["file"])

        mixed = mixed_pool.pop(0) if (take and mixed_pool) else None
        schedule.append({"date": date, "solve": take, "theory": theory,
                         "revise": revise, "mixed": mixed,
                         "mock": date.weekday() == 6})

    return {
        "today": today, "week": week, "phase": L.phase_of(week),
        "days_left_in_week": days_left, "per_day": per_day,
        "behind": behind, "core_left": core_now, "schedule": schedule,
        "theory": {"track": track, "read": read_count, "total": len(files),
                   "expected": expected, "cadence": cadence},
        "theory_due": theory_due,
        "weak": [w for w in L.weak_topics() if w["status"] == "open"],
    }


def _p(row):
    return f"{row['number']:>4}  {row['title'][:38]:<38} {row['difficulty']:<7}"


def render(plan):
    t, week = plan["today"], plan["week"]
    print(f"\n  {t:%a %d %b %Y}   week {week} of {L.TOTAL_WEEKS}   {plan['phase']}")
    print(f"  {'-' * 68}")

    th = plan["theory"]
    lag = th["expected"] - th["read"]
    note = f"behind by {lag}" if lag > 0 else "on track"
    print(f"  theory {th['track']}: {th['read']}/{th['total']} read, "
          f"{th['expected']} due by end of week ({note})")
    print(f"  core this week: {len(plan['core_left'])} left over "
          f"{plan['days_left_in_week']} day(s) -> {plan['per_day']}/day")
    if plan["behind"]:
        print(f"  behind: {len(plan['behind'])} core problem(s) from earlier weeks — these go first")

    first = plan["schedule"][0]
    print(f"\n  TODAY")
    if first["theory"]:
        print(f"    read     {first['theory'].relative_to(L.ROOT)}")
    for i, r in enumerate(first["solve"]):
        label = "solve   " if i == 0 else "        "
        flag = "  <- behind" if r["week"] < week else ""
        flag += f"  ({r['status']} written)" if r["status"] in ("brute", "optimal") else ""
        print(f"    {label} {_p(r)}{flag}")
    for i, r in enumerate(first["revise"]):
        label = "revise  " if i == 0 else "        "
        when = "due today" if r["overdue"] == 0 else (
            f"{r['overdue']}d overdue" if r["overdue"] > 0 else "free pick")
        print(f"    {label} {_p(r)}sweep {r['reps'] + 1}, {when}")
    for t in plan["theory_due"][:2]:
        when = "due today" if t["overdue"] == 0 else f"{t['overdue']}d overdue"
        print(f"    re-read  {t['path']:<45} sweep {t['reps'] + 2}, {when}")
    if first["mixed"]:
        m = first["mixed"]
        print(f"    mixed    {m['number']:>4}  {m['title'][:38]:<38} {m['difficulty']:<7}"
              f"name the pattern first, then solve")
    if first["mock"]:
        print(f"    mock     45 min, out loud — one problem and one system design prompt")
    if not first["solve"] and not first["revise"] and not first["theory"]:
        print("    nothing scheduled — pull the next week forward, or revise")

    if plan["weak"]:
        print(f"\n  WEAK TOPICS  ({len(plan['weak'])} open — aim revision here)")
        for w in plan["weak"]:
            print(f"    {w['title'][:46]:<46} {w['slip'][:40]}")

    rest = plan["schedule"][1:]
    if rest:
        print(f"\n  NEXT DAYS")
        for day in rest:
            bits = []
            if day["solve"]:
                bits.append("solve " + ", ".join(str(r["number"]) for r in day["solve"]))
            if day["theory"]:
                bits.append("read " + str(day["theory"].relative_to(L.ROOT / "theory")))
            if day["revise"]:
                bits.append("revise " + ", ".join(str(r["number"]) for r in day["revise"]))
            if day["mixed"]:
                bits.append(f"mixed {day['mixed']['number']}")
            if day["mock"]:
                bits.append("MOCK")
            print(f"    {day['date']:%a %d %b}  {'   '.join(bits) if bits else '-'}")
    print()


def render_drill(picks, answers=False):
    print(f"\n  RECOGNITION DRILL  ({len(picks)})")
    print(f"  {'-' * 68}")
    print("  For each one: name the pattern, the key insight, and the complexity.")
    print("  60 seconds each. Do not solve it, do not open the file.\n")
    for i, r in enumerate(picks, 1):
        print(f"  {i}. {r['number']}  {r['title']}   [{r['difficulty']}]")
        for line in ("INPUT\n    " + r["statement"]).splitlines():
            print(f"       {line}")
        print()
    if answers:
        print(f"  {'-' * 68}\n  ANSWERS\n")
        for i, r in enumerate(picks, 1):
            print(f"  {i}. {r['pattern']}   ({r['folder']})")
            if r["recognition"]:
                print(f"       {r['recognition'][:200]}")
            print()
    else:
        print("  answers:  python3 scripts/plan.py --drill "
              f"{len(picks)} --answers\n")


def main():
    ap = argparse.ArgumentParser(description="What to study today, and next.")
    ap.add_argument("--days", type=int, default=4, help="how many days to plan (default 4)")
    ap.add_argument("--revise", type=int, metavar="N", help="just pull N problems to revise")
    ap.add_argument("--drill", type=int, metavar="N",
                    help="N problem statements with the pattern stripped — name it, do not solve")
    ap.add_argument("--answers", action="store_true", help="reveal the drill answers")
    ap.add_argument("--date", help="plan for this date instead of today (YYYY-MM-DD)")
    ap.add_argument("--json", action="store_true", help="machine readable")
    args = ap.parse_args()

    today = L.parse_date(args.date) if args.date else dt.date.today()
    rows = L.load()

    if args.drill:
        picks = L.drill_pick(rows, args.drill, today)
        if not picks:
            print("no covered patterns with unsolved problems yet", file=sys.stderr)
            return 1
        render_drill(picks, args.answers)
        return 0

    if args.revise:
        picks = L.pick_revision(rows, args.revise, today)
        if not picks:
            print("nothing solved yet — nothing to revise", file=sys.stderr)
            return 1
        print(f"\n  REVISE  ({len(picks)})")
        for r in picks:
            when = "due today" if r["overdue"] == 0 else (
                f"{r['overdue']}d overdue" if r["overdue"] > 0 else
                f"not due for {-r['overdue']}d, free pick")
            print(f"    {_p(r)}sweep {r['reps'] + 1}, {when}")
            print(f"          {r['file']}")
        print()
        return 0

    plan = build(rows, today, max(1, args.days))
    if args.json:
        json.dump(plan, sys.stdout, indent=2, default=str)
        print()
        return 0
    render(plan)
    return 0


if __name__ == "__main__":
    sys.exit(main())
