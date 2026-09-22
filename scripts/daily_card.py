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
import random
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import prep_lib as L


# Fallback themes, so the card always carries something to think about even
# when nothing is available to write a fresh scenario. The scheduled task
# normally replaces the whole block with a real one.
THEMES = [
    "a counter that every user increments at once — celebrity post likes",
    "fan-out on write vs on read, when one account has 20M followers",
    "the same request arriving twice because the client retried",
    "one shard holding a key everyone reads — the hot partition",
    "a cache that all expires at the same second — the stampede",
    "a queue consumer that is slower than the producer, for hours",
    "a nightly job that now takes longer than a night",
    "two users editing the same row at the same moment",
    "a payment that must happen exactly once across two services",
    "a read replica lagging behind enough that users see stale data",
    "search that must stay fresh within seconds of a write",
    "rate limiting an API per user, per IP, and per endpoint at once",
    "a deploy that must not drop in-flight requests",
    "a feature flag read on every request, from every service",
    "uploading files far larger than any request timeout allows",
    "notifications that must not be sent twice after a crash",
    "a report query that locks the table everyone else needs",
    "sessions that must survive one server dying mid-request",
    "an autocomplete box hit on every keystroke by every user",
    "a webhook receiver whose downstream is down for an hour",
    "counting unique viewers of a live stream, in real time",
    "a schema migration on a table too big to lock",
    "geo-distributed users writing to one primary database",
    "a leaderboard updated thousands of times a second",
]


def written_block(today, open_m, close_m, placeholder=None):
    """Text the scheduled task has already written between two markers.

    The task replaces the script's placeholder with real prose. Running the
    script again later the same day must not throw that away, so anything
    written for today is carried through untouched. A body still starting with
    `placeholder` is the script's own filler and does not count as written.
    Yesterday's card is ignored outright.
    """
    path = L.NOTES / "daily-card.md"
    if not path.exists():
        return None
    text = path.read_text(encoding="utf-8")
    if not text.startswith(f"# {today:%a %d %b %Y}"):
        return None                                   # yesterday's card
    if open_m not in text or close_m not in text:
        return None
    body = text.split(open_m, 1)[1].split(close_m, 1)[0].strip()
    if not body:
        return None
    if placeholder and body.startswith(placeholder):
        return None
    return body


def existing_scenario(today):
    """Today's scenario, if one has already been written into the card."""
    return written_block(today, SCENARIO_OPEN, SCENARIO_CLOSE, "**Today's theme:**")


def scenario_block(today, seed=None, existing=None):
    """The daily system design scenario.

    Written between markers so the scheduled task can replace it with a fresh
    one. What the script puts here is the floor, not the intent: a theme to
    think about, so the card is never empty.
    """
    if existing:
        return ["## System design — 10 minutes, out loud", "",
                SCENARIO_OPEN, existing, SCENARIO_CLOSE]
    rng = random.Random(seed if seed is not None else today.toordinal())
    theme = rng.choice(THEMES)
    return [
        "## System design — 10 minutes, out loud", "",
        SCENARIO_OPEN,
        f"**Today's theme:** {theme}",
        "",
        "Set it up yourself: what is the scale, what breaks first, what do you",
        "change, and what does that change cost you?",
        SCENARIO_CLOSE,
    ]


# One component or idea a day, rotating across the four subjects. The scheduled
# task writes the actual explanation; this bank only decides the topic, so the
# rotation is the script's job and the prose is not.
CONCEPTS = [
    ("HLD", "L4 vs L7 load balancer"),
    ("HLD", "what a reverse proxy does that a load balancer does not"),
    ("HLD", "vector database - what it is and when you actually need one"),
    ("HLD", "Redis vs Memcached"),
    ("HLD", "Kafka vs RabbitMQ - a log is not a queue"),
    ("HLD", "consistent hashing, and what it fixes about modulo sharding"),
    ("HLD", "read replica vs sharding - which problem each one solves"),
    ("HLD", "bloom filter - where it saves a disk read"),
    ("HLD", "token bucket vs leaky bucket vs sliding window rate limits"),
    ("HLD", "CAP theorem - what the P actually means"),
    ("HLD", "idempotency keys, and why retries need them"),
    ("HLD", "long polling vs SSE vs WebSocket"),
    ("HLD", "blue-green vs canary deploys"),
    ("HLD", "object vs block vs file storage"),
    ("HLD", "OLTP vs OLAP, and why reports do not run on the primary"),
    ("HLD", "quorum reads and writes - why R + W > N"),
    ("HLD", "two-phase commit vs saga"),
    ("HLD", "circuit breaker, and what half-open is for"),
    ("HLD", "distributed lock - why a TTL alone is not enough"),
    ("HLD", "CDN - what happens on a cache miss"),
    ("HLD", "API gateway vs load balancer"),
    ("HLD", "write-ahead log - why the log is written before the data"),
    ("DBMS", "B-tree vs LSM tree"),
    ("DBMS", "composite index - why column order decides everything"),
    ("DBMS", "covering index, and the index-only scan"),
    ("DBMS", "isolation levels, and the anomaly each one still allows"),
    ("DBMS", "MVCC - how a reader avoids blocking a writer"),
    ("DBMS", "optimistic vs pessimistic locking"),
    ("DBMS", "how a database detects and breaks a deadlock"),
    ("DBMS", "normalization vs denormalization - what you pay either way"),
    ("DBMS", "connection pooling - why bigger is not better"),
    ("DBMS", "the N+1 query problem"),
    ("DBMS", "partitioning vs sharding"),
    ("DBMS", "why the planner picks a full scan over your index"),
    ("DBMS", "fsync, group commit, and what durability costs"),
    ("DBMS", "SQL vs NoSQL - what actually decides it"),
    ("DBMS", "columnar storage - why it is fast for aggregates"),
    ("OS", "process vs thread"),
    ("OS", "what a context switch actually costs"),
    ("OS", "virtual memory and the page fault"),
    ("OS", "mutex vs semaphore vs spinlock"),
    ("OS", "user space vs kernel space - the price of a syscall"),
    ("OS", "blocking vs non-blocking I/O, and what epoll changed"),
    ("OS", "copy-on-write fork"),
    ("OS", "sizing a thread pool - CPU bound vs I/O bound"),
    ("OS", "zombie and orphan processes"),
    ("OS", "cache lines and false sharing"),
    ("OS", "memory mapped files, and when mmap beats read()"),
    ("OS", "preemptive vs cooperative scheduling"),
    ("NET", "TCP vs UDP - what the handshake buys you"),
    ("NET", "the TLS handshake - what happens before the first byte"),
    ("NET", "HTTP/1.1 vs HTTP/2 vs HTTP/3"),
    ("NET", "head-of-line blocking, at both layers"),
    ("NET", "the DNS resolution path, from browser to authoritative"),
    ("NET", "TCP slow start and congestion control"),
    ("NET", "what a socket actually is"),
    ("NET", "keep-alive, and why connection reuse matters so much"),
    ("LLD", "the SOLID letter that actually gets violated most"),
    ("LLD", "strategy pattern vs a dict of functions"),
    ("LLD", "factory vs builder"),
    ("LLD", "observer pattern, and the leak it invites"),
    ("LLD", "why constructor injection beats the alternatives"),
    ("LLD", "composition over inheritance, with a real example"),
    ("LLD", "why singleton is a testing problem"),
    ("LLD", "repository pattern - what it buys and what it hides"),
    ("LLD", "value objects, and why immutability removes bugs"),
]


def covered_concepts():
    """Topics the card has already explained, read off the log."""
    path = L.NOTES / "concepts.md"
    if not path.exists():
        return set()
    seen = set()
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line.startswith("20"):
            continue
        if "\u2014" in line:
            seen.add(line.split("\u2014", 1)[1].strip().lower())
        elif " - " in line:
            seen.add(line.split(" - ", 1)[1].strip().lower())
    return seen


def pick_concept(today):
    """Today's topic: a stable rotation, skipping what has been covered.

    The order is shuffled once with a fixed seed rather than taken in file
    order, so the subjects interleave instead of arriving in four long runs.
    Once every topic has been covered the rotation simply starts again.
    """
    order = list(CONCEPTS)
    random.Random(20260922).shuffle(order)
    done = covered_concepts()
    fresh = [c for c in order if c[1].lower() not in done]
    if fresh:
        return fresh[0]
    return order[today.toordinal() % len(order)]   # all covered, go round again


def existing_concept(today):
    """Today's concept, if the task has already written one into the card."""
    return written_block(today, CONCEPT_OPEN, CONCEPT_CLOSE, "**Today's concept:**")


def concept_block(today, existing=None):
    """One component or idea, explained. Read, not drilled.

    Same contract as the scenario: markers so the scheduled task can replace
    the placeholder, and a placeholder good enough that the card still tells
    you what to go and look up if nothing ever does.
    """
    if existing:
        return ["## Concept — 5 minutes", "",
                CONCEPT_OPEN, existing, CONCEPT_CLOSE]
    area, topic = pick_concept(today)
    return [
        "## Concept — 5 minutes", "",
        CONCEPT_OPEN,
        f"**Today's concept:** {topic} *({area})*",
        "",
        "Nothing written yet. Say what it is, when you reach for it, and what",
        "it costs you — then go and check yourself.",
        CONCEPT_CLOSE,
    ]


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


SCENARIO_OPEN = "<!-- scenario -->"
SCENARIO_CLOSE = "<!-- /scenario -->"

CONCEPT_OPEN = "<!-- concept -->"
CONCEPT_CLOSE = "<!-- /concept -->"

# The recall question is regenerated from the repo each run, so a sharper one
# written by hand needs markers too - both the question and its answer.
RECALL_OPEN = "<!-- recall -->"
RECALL_CLOSE = "<!-- /recall -->"
RECALL_ANSWER_OPEN = "<!-- recall-answer -->"
RECALL_ANSWER_CLOSE = "<!-- /recall-answer -->"

CARDS = L.NOTES / "cards"
HEADER_DATE = re.compile(r"^#\s+\w{3}\s+(\d{2}\s+\w{3}\s+\d{4})")


def card_date(text):
    """The date a card was written for, read back off its heading."""
    m = HEADER_DATE.search(text)
    return L.parse_date(m.group(1)) if m else None


def archive(today, card):
    """Keep every card, not just the newest.

    notes/daily-card.md is always today - that is the link on the phone, so it
    has to stay put. Each card is also written to notes/cards/<date>.md, and a
    card left over from an earlier day is filed there before it is overwritten.
    """
    CARDS.mkdir(parents=True, exist_ok=True)
    written = []

    live = L.NOTES / "daily-card.md"
    if live.exists():
        old = live.read_text(encoding="utf-8")
        old_date = card_date(old)
        if old_date and old_date != today:
            dest = CARDS / f"{old_date:%Y-%m-%d}.md"
            if not dest.exists():
                dest.write_text(old, encoding="utf-8")
                written.append(dest)

    dest = CARDS / f"{today:%Y-%m-%d}.md"
    if not dest.exists() or dest.read_text(encoding="utf-8") != card:
        dest.write_text(card, encoding="utf-8")
        written.append(dest)

    index()
    return written


def index():
    """A dated list of every archived card, newest first."""
    cards = sorted(CARDS.glob("20*.md"), reverse=True)
    lines = ["# Card archive", "",
             "Every daily card, newest first. `../daily-card.md` is always today's.",
             ""]
    for c in cards:
        d = L.parse_date(c.stem)
        label = f"{d:%a %d %b %Y}" if d else c.stem
        first = ""
        for ln in c.read_text(encoding="utf-8").splitlines():
            if ln.startswith("**Solve**"):
                first = " — " + ln.replace("**Solve**", "").strip()[:60]
                break
        lines.append(f"- [{label}]({c.name}){first}")
    (CARDS / "README.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


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
    # A question the task rewrote today wins over the generated one, and its
    # answer travels with it - swapping only one of the two would be worse
    # than swapping neither.
    kept_q = written_block(today, RECALL_OPEN, RECALL_CLOSE)
    kept_a = written_block(today, RECALL_ANSWER_OPEN, RECALL_ANSWER_CLOSE)
    if kept_a:
        # stored with its label, re-emitted with one - strip so it is not doubled
        kept_a = re.sub(r"^\*\*Recall\*\*\s*[-\u2014]\s*", "", kept_a).strip()
    if kept_q and kept_a:
        question, answer = kept_q, kept_a
    out += ["", "## Recall", "", RECALL_OPEN, question, RECALL_CLOSE]

    drill = L.drill_pick(rows, 1, today)
    drill = drill[0] if drill else None
    if drill:
        out += ["", "## Name the pattern", "",
                f"*{drill['difficulty']}* — pattern, key insight, complexity. Do not solve it.",
                "", "```text", "INPUT", "    " + drill["statement"], "```"]

    out += [""] + scenario_block(today, existing=existing_scenario(today))

    out += [""] + concept_block(today, existing=existing_concept(today))

    out += ["", "<details>", "<summary>Answers</summary>", ""]
    if answer:
        out += [RECALL_ANSWER_OPEN, f"**Recall** — {answer}",
                RECALL_ANSWER_CLOSE, ""]
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
    filed = archive(today, card)
    path.write_text(card, encoding="utf-8")
    print(f"wrote {path.relative_to(L.ROOT)}")
    for f in filed:
        print(f"filed {f.relative_to(L.ROOT)}")

    if args.commit:
        # Everything a run can touch: today's card, the dated copies archive()
        # filed, and the index it rewrites. Staging the cards directory covers
        # the last two without having to name each file.
        rel = [str(path.relative_to(L.ROOT)), str(CARDS.relative_to(L.ROOT))]
        run = lambda *a: subprocess.run(a, cwd=L.ROOT, capture_output=True, text=True)

        def failed(step, proc):
            # git puts "nothing added to commit" and most push advice on stdout,
            # so reporting stderr alone leaves the reason blank.
            detail = (proc.stderr.strip() or proc.stdout.strip()).splitlines()
            print(f"{step}: {detail[0] if detail else 'no output'}", file=sys.stderr)
            for line in detail[1:]:
                print(f"  {line}", file=sys.stderr)

        # `git diff` reports nothing for an untracked file, so the very first
        # card looked unchanged and skipped its own commit. Ask status instead.
        if not run("git", "status", "--porcelain", "--", *rel).stdout.strip():
            print("card unchanged, nothing to commit")
            return 0
        add = run("git", "add", *rel)
        if add.returncode:
            failed("add failed", add)
            return 1
        commit = run("git", "commit", "-m", f"Daily card: {today:%Y-%m-%d}")
        if commit.returncode:
            failed("commit failed", commit)
            return 1

        # The remote may have moved since the last run. Replay the card on top
        # of it rather than pushing a stale branch and being rejected.
        branch = run("git", "rev-parse", "--abbrev-ref", "HEAD").stdout.strip()
        if not run("git", "fetch", "origin", branch).returncode:
            behind = run("git", "rev-list", "--count", f"HEAD..origin/{branch}").stdout.strip()
            if behind and behind != "0":
                print(f"{behind} commit(s) behind origin/{branch}, rebasing")
                rebase = run("git", "rebase", f"origin/{branch}")
                if rebase.returncode:
                    run("git", "rebase", "--abort")
                    failed("rebase failed, card committed but not pushed", rebase)
                    return 1

        push = run("git", "push", "origin", "HEAD")
        if push.returncode:
            failed("committed, but push failed", push)
            return 1
        print("committed and pushed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
