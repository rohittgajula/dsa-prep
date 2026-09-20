"""
Write today's study card to notes/daily-card.md, for reading on a phone.

    python3 scripts/daily_card.py            write the file
    python3 scripts/daily_card.py --print    stdout only, write nothing
    python3 scripts/daily_card.py --commit   write, commit and push it

Everything here is derived from the repo, so the card exists whether or not
anything clever is available to write it: the plan, one thing to recall, and
one problem to classify. The answers sit inside a <details> block, which the
GitHub mobile app renders as a toggle - so glancing at the card does not spoil
the drill.
"""
import argparse
import datetime as dt
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import prep_lib as L


def recall_item(rows, today):
    """The one thing to pull from memory, most perishable first."""
    weak = [w for w in L.weak_topics() if w["status"] == "open"]
    if weak:
        w = weak[0]
        return (f"{w['title']} — what goes wrong here, and what is the fix?",
                w["fix"] or w["slip"] or "see notes/weak-topics.md")

    theory = [t for t in L.theory_revision_pool(today) if t["overdue"] >= 0]
    if theory:
        t = theory[0]
        name = Path(t["path"]).stem.split("-", 1)[-1].replace("-", " ")
        return (f"{name} — say the main idea out loud before re-reading {t['path']}.",
                f"Re-read {t['path']}. Last read {t['last_read']}.")

    due = [r for r in L.revision_pool(rows, today) if r["overdue"] >= 0]
    pick = due[0] if due else next(iter(L.pick_revision(rows, 1, today)), None)
    if pick:
        # an OPTIMAL section stripped back to its Time/Space lines carries no
        # actual answer - the write-up was never filled in
        prose = " ".join(w for w in pick["optimal_note"].split()
                         if not w.startswith(("Time", "Space", "O(", ":")))
        answer = pick["key_insight"] or (pick["optimal_note"] if prose.strip() else "")
        if not answer:
            answer = (f"The write-up in {pick['file']} is still the template — "
                      f"fill it in after you answer.")
        return (f"{pick['number']} {pick['title']} — state the optimal approach and "
                f"both complexities from memory, without opening the file.", answer)

    return ("Nothing solved yet — solve today's first problem and the card fills itself in.", "")


def build(rows, today):
    plan = __import__("plan").build(rows, today, days=1)
    day = plan["schedule"][0]
    week = plan["week"]

    out = [f"# {today:%a %d %b %Y} — week {week}", ""]

    if day["solve"]:
        out.append("**Solve** " + ", ".join(f"{r['number']} {r['title']}" for r in day["solve"]))
    if day["theory"]:
        out.append(f"**Read** {day['theory'].relative_to(L.ROOT)}")
    for t in plan["theory_due"][:1]:
        out.append(f"**Re-read** {t['path']} — {t['overdue']}d overdue")
    if day["revise"]:
        out.append("**Revise** " + ", ".join(
            f"{r['number']} {r['title']} (sweep {r['reps'] + 1})" for r in day["revise"]))
    if day["mixed"]:
        m = day["mixed"]
        out.append(f"**Mixed** {m['number']} {m['title']} — name the pattern before you start")
    if day["mock"]:
        out.append("**Mock** 45 minutes out loud: one problem, one system design prompt")
    if len(out) == 2:
        out.append("Nothing scheduled today.")

    question, answer = recall_item(rows, today)
    out += ["", "## Recall", "", question]

    drill = L.drill_pick(rows, 1, today)
    drill = drill[0] if drill else None
    if drill:
        out += ["", "## Name the pattern", "",
                f"*{drill['difficulty']}* — pattern, key insight, complexity. Do not solve it.",
                "", "```text", "INPUT", "    " + drill["statement"], "```"]

    out += ["", "<details>", "<summary>Answers</summary>", ""]
    if answer:
        out += [f"**Recall** — {answer}", ""]
    if drill:
        hint = drill["recognition"] or "no recognition hint written yet"
        out += [f"**Pattern** — {drill['pattern']}. {hint}", ""]
    out += ["</details>", ""]
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser(description="Today's study card.")
    ap.add_argument("--print", dest="show", action="store_true", help="stdout only")
    ap.add_argument("--commit", action="store_true", help="also commit and push the card")
    ap.add_argument("--date", help="build the card for this date (YYYY-MM-DD)")
    args = ap.parse_args()

    today = L.parse_date(args.date) if args.date else dt.date.today()
    card = build(L.load(), today)

    if args.show:
        print(card)
        return 0

    path = L.NOTES / "daily-card.md"
    path.write_text(card, encoding="utf-8")
    print(f"wrote {path.relative_to(L.ROOT)}")

    if args.commit:
        rel = str(path.relative_to(L.ROOT))
        run = lambda *a: subprocess.run(a, cwd=L.ROOT, capture_output=True, text=True)
        if not run("git", "diff", "--quiet", "--", rel).returncode:
            print("card unchanged, nothing to commit")
            return 0
        run("git", "add", rel)
        commit = run("git", "commit", "-m", f"Daily card: {today:%Y-%m-%d}")
        if commit.returncode:
            print(f"commit failed: {commit.stderr.strip()}", file=sys.stderr)
            return 1
        push = run("git", "push", "origin", "HEAD")
        if push.returncode:
            print(f"committed, but push failed: {push.stderr.strip()}", file=sys.stderr)
            return 1
        print("committed and pushed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
