"""
Shared reading layer for the prep scripts.

Nothing in here prints. `progress.py` and `plan.py` do the printing; this file
just turns the repo into data: every solution file parsed, the study log, the
weak-topics list, the theory tracks, and when a problem is next due for revision.
"""
import ast
import datetime as dt
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOLUTIONS = ROOT / "solutions"
THEORY = ROOT / "theory"
NOTES = ROOT / "notes"
STUDY_LOG = NOTES / "study-log.md"
WEAK_TOPICS = NOTES / "weak-topics.md"

START = dt.date(2026, 9, 10)
TOTAL_WEEKS = 35

PHASES = [
    ("Foundations",       0, 10),
    ("Linear structures", 11, 14),
    ("Recursion & trees", 15, 20),
    ("Graphs",            21, 23),
    ("Greedy & DP",       24, 27),
    ("Advanced",          28, 29),
    ("Revision",          30, 35),
]

# theory track -> the weeks it is scheduled across (from theory/README.md)
TRACKS = [
    ("os",            1, 5),
    ("networks",      6, 10),
    ("dbms",          11, 13),
    ("lld",           14, 17),
    ("system-design", 18, 26),
    ("ai",            27, 35),
]

# days until the next sweep, by how many times it has been revised already
INTERVALS = [3, 7, 21, 60, 120]
INTERVALS_HINTED = [2, 5, 14, 40, 90]

PLACEHOLDER = re.compile(r"O\(\?\)|^\s*<.*>\s*$", re.M)
EMPTY = re.compile(r"^\s*(<>|<.*>)?\s*$")

HEADER = {
    "title":      re.compile(r"^\s*(\d+)\.\s+(.+?)\s*$", re.M),
    "difficulty": re.compile(r"^Difficulty\s*:\s*(\S+)", re.M),
    "pattern":    re.compile(r"^Pattern\s*:\s*(.+?)\s*$", re.M),
    "tier":       re.compile(r"^Tier\s*:\s*(\S+)", re.M),
    "scheduled":  re.compile(r"^Scheduled\s*:\s*(.+?)\s*\(week\s*(\d+)\)", re.M),
    "unaided":    re.compile(r"Solved unaided\s*:\s*(.+?)\s*$", re.M),
    "minutes":    re.compile(r"Time taken\s*:\s*(\S+)\s*min", re.M),
    "solved_on":  re.compile(r"^Solved on\s*:\s*(\S+)", re.M),
    "revised":    re.compile(r"Revised\s*:\s*(.+?)\s*$", re.M),
}

THINKING_FIELDS = [
    ("first_look", "What the problem looked like at first:"),
    ("tried",      "What I tried:"),
    ("stuck",      "Where I got stuck:"),
    ("clicked",    "What made it click:"),
    ("review",     "Tutor review:"),
]


# ---------------------------------------------------------------- calendar

def current_week(today=None):
    today = today or dt.date.today()
    return max(0, (today - START).days // 7)


def phase_of(week):
    for name, lo, hi in PHASES:
        if lo <= week <= hi:
            return name
    return "?"


def week_start(week):
    return START + dt.timedelta(weeks=week)


def parse_date(text):
    text = (text or "").strip()
    for fmt in ("%Y-%m-%d", "%d %b %Y", "%d-%b-%Y", "%d/%m/%Y"):
        try:
            return dt.datetime.strptime(text, fmt).date()
        except ValueError:
            continue
    return None


# ---------------------------------------------------------------- solutions

def _trivial(node):
    body = [n for n in node.body if not (isinstance(n, ast.Expr)
                                         and isinstance(n.value, ast.Constant)
                                         and isinstance(n.value.value, str))]
    return not body or all(isinstance(n, ast.Pass) for n in body)


def _written(classdef):
    methods = [n for n in classdef.body
               if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))]
    return any(not _trivial(m) for m in methods)


def _assigned(tree, target):
    for node in tree.body:
        if isinstance(node, ast.Assign):
            for t in node.targets:
                if isinstance(t, ast.Name) and t.id == target:
                    v = node.value
                    if isinstance(v, ast.Constant) and isinstance(v.value, str):
                        return v.value
                    if isinstance(v, ast.Name):
                        return v.id
    return None


def _code_status(tree):
    """(brute_written, optimal_written) for either file shape."""
    classes = {n.name: n for n in tree.body if isinstance(n, ast.ClassDef)}

    brute_cls, opt_cls = _assigned(tree, "CLASS_BRUTE"), _assigned(tree, "CLASS_OPTIMAL")
    if brute_cls and opt_cls:
        return (brute_cls in classes and _written(classes[brute_cls]),
                opt_cls in classes and _written(classes[opt_cls]))

    method, sol = _assigned(tree, "METHOD"), classes.get("Solution")
    if not method or sol is None:
        return False, False
    by_name = {n.name: n for n in sol.body
               if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))}
    brute, opt = by_name.get(method + "_brute"), by_name.get(method)
    return (brute is not None and not _trivial(brute),
            opt is not None and not _trivial(opt))


def _thinking(head):
    """Each MY THINKING sub-field -> text, or '' when still a placeholder."""
    block = head.split("MY THINKING", 1)
    if len(block) == 1:
        return {k: "" for k, _ in THINKING_FIELDS}
    block = block[1].split("\nBRUTE FORCE", 1)[0]

    out, labels = {}, [lab for _, lab in THINKING_FIELDS]
    for (key, label), nxt in zip(THINKING_FIELDS, labels[1:] + [None]):
        if label not in block:
            out[key] = ""
            continue
        chunk = block.split(label, 1)[1]
        if nxt and nxt in chunk:
            chunk = chunk.split(nxt, 1)[0]
        lines = [ln.strip() for ln in chunk.splitlines() if not EMPTY.match(ln)]
        out[key] = " ".join(lines).strip()
    return out


def parse(path):
    src = path.read_text(encoding="utf-8", errors="replace")
    head = src.split('"""')[1] if src.count('"""') >= 2 else src[:3000]

    def grab(key, group=1, default=""):
        m = HEADER[key].search(head)
        return m.group(group).strip() if m else default

    try:
        tree = ast.parse(src)
    except SyntaxError as exc:
        return {"file": str(path.relative_to(ROOT)), "error": f"{type(exc).__name__}: {exc}"}

    brute, optimal = _code_status(tree)
    status = ("done" if (brute and optimal) else
              "brute" if brute else "optimal" if optimal else "todo")

    unaided = grab("unaided")
    hinted = unaided.upper().startswith("N") and "/" not in unaided

    revised_raw = grab("revised")
    revised = [d for d in (parse_date(x) for x in re.split(r"[,;]", revised_raw)) if d]
    solved_on = parse_date(grab("solved_on"))
    estimated = False
    if status == "done" and solved_on is None:
        solved_on = dt.date.fromtimestamp(path.stat().st_mtime)
        estimated = True

    statement = ""
    if "INPUT" in head:
        statement = head.split("INPUT", 1)[1].split("RECOGNITION HINT", 1)[0].strip()
    recognition = ""
    if "RECOGNITION HINT" in head:
        chunk = head.split("RECOGNITION HINT", 1)[1]
        chunk = re.split(r"^-{10,}$", chunk, maxsplit=1, flags=re.M)[0]
        recognition = " ".join(ln.strip() for ln in chunk.splitlines()
                               if ln.strip() and not ln.strip().startswith("(")).strip()

    title = HEADER["title"].search(head)
    minutes = grab("minutes")
    thinking = _thinking(head)

    return {
        "file": str(path.relative_to(ROOT)),
        "folder": path.parent.name,
        "number": int(title.group(1)) if title else 0,
        "title": title.group(2) if title else path.stem,
        "difficulty": grab("difficulty", default="?"),
        "pattern": grab("pattern", default="?"),
        "tier": grab("tier", default="?"),
        "week": int(grab("scheduled", 2, "0") or 0),
        "status": status,
        "brute": brute,
        "optimal": optimal,
        "hinted": hinted,
        "unaided": unaided,
        "minutes": None if minutes in ("", "__") else minutes,
        "solved_on": solved_on,
        "solved_on_estimated": estimated,
        "revised": revised,
        "reps": len(revised),
        "notes_filled": status != "todo" and not PLACEHOLDER.search(head.split("BRUTE FORCE", 1)[-1]),
        "statement": statement,
        "recognition": recognition,
        "thinking": thinking,
        "thinking_filled": any(thinking[k] for k in ("first_look", "tried", "stuck", "clicked")),
        "reviewed": bool(thinking["review"]),
    }


def load(folder=None, week=None, errors=None):
    rows = []
    for path in sorted(SOLUTIONS.glob("*/*.py")):
        row = parse(path)
        if "error" in row:
            if errors is not None:
                errors.append(row)
            continue
        if folder and folder not in row["folder"]:
            continue
        if week is not None and row["week"] != week:
            continue
        rows.append(row)
    return rows


# ---------------------------------------------------------------- revision

def due_date(row):
    """When this problem should next be revised. None if it is not solved."""
    if row["status"] != "done" or row["solved_on"] is None:
        return None
    last = max([row["solved_on"], *row["revised"]])
    table = INTERVALS_HINTED if row["hinted"] else INTERVALS
    return last + dt.timedelta(days=table[min(row["reps"], len(table) - 1)])


def revision_pool(rows, today=None):
    """Solved problems, each with its due date and how overdue it is."""
    today = today or dt.date.today()
    pool = []
    for row in rows:
        due = due_date(row)
        if due is None:
            continue
        pool.append({**row, "due": due, "overdue": (today - due).days})
    return sorted(pool, key=lambda r: -r["overdue"])


def pick_revision(rows, n=3, today=None, seed=None):
    """Overdue first, then a random sample of the rest, so old topics resurface."""
    import random
    rng = random.Random(seed if seed is not None else (today or dt.date.today()).toordinal())
    pool = revision_pool(rows, today)
    due = [r for r in pool if r["overdue"] >= 0]
    rest = [r for r in pool if r["overdue"] < 0]
    picked = due[:n]
    if len(picked) < n and rest:
        rng.shuffle(rest)
        picked += rest[:n - len(picked)]
    return picked


# ---------------------------------------------------------------- theory

def track_for_week(week):
    for name, lo, hi in TRACKS:
        if lo <= max(week, 1) <= hi:
            return name, lo, hi
    return TRACKS[-1]


def theory_files(track):
    return sorted(p for p in (THEORY / track).glob("*.md") if p.name != "README.md")


def theory_plan(week, done=None):
    """(track, files, expected_by_now, next_unread) for this week."""
    done = done or set()
    track, lo, hi = track_for_week(week)
    files = theory_files(track)
    weeks = hi - lo + 1
    through = min(max(week - lo + 1, 1), weeks)
    expected = min(len(files), round(len(files) * through / weeks))
    unread = [f for f in files if str(f.relative_to(ROOT)) not in done]
    return track, files, expected, (unread[0] if unread else None)


# ---------------------------------------------------------------- notes

LOG_ENTRY = re.compile(r"^##\s*(\d{4}-\d{2}-\d{2})", re.M)


def study_log():
    """[{date, lines, theory:[paths], solved:[numbers]}], newest last."""
    if not STUDY_LOG.exists():
        return []
    text = STUDY_LOG.read_text(encoding="utf-8")
    entries, marks = [], list(LOG_ENTRY.finditer(text))
    for i, m in enumerate(marks):
        body = text[m.end():marks[i + 1].start() if i + 1 < len(marks) else len(text)]
        lines = [ln.strip("- ").strip() for ln in body.splitlines() if ln.strip().startswith("-")]
        theory = re.findall(r"theory/[\w./-]+\.md", body)
        solved = [int(x) for x in re.findall(r"^-\s*Solved\s*:\s*(\d+)", body, re.M)]
        entries.append({"date": parse_date(m.group(1)), "lines": lines,
                        "theory": theory, "solved": solved})
    return sorted(entries, key=lambda e: e["date"] or dt.date.min)


def theory_done():
    return {p for e in study_log() for p in e["theory"]}


def weak_topics():
    """[{title, slip, fix, seen, status}] from notes/weak-topics.md."""
    if not WEAK_TOPICS.exists():
        return []
    text = WEAK_TOPICS.read_text(encoding="utf-8")
    text = re.sub(r"```.*?```", "", text, flags=re.S)          # drop the format example
    out = []
    for block in re.split(r"^###\s*", text, flags=re.M)[1:]:
        lines = block.splitlines()
        def field(name):
            m = re.search(rf"\*\*{name}:\*\*\s*(.+)", block, re.I)
            return m.group(1).strip() if m else ""
        out.append({"title": lines[0].strip(), "slip": field("Slip"), "fix": field("Fix"),
                    "seen": field("Seen"), "status": field("Status").lower() or "open"})
    return out


# ---------------------------------------------------- theory revision

def theory_read_dates():
    """theory path -> the dates the study log says it was read, oldest first."""
    seen = {}
    for entry in study_log():
        if not entry["date"]:
            continue
        for path in entry["theory"]:
            seen.setdefault(path, []).append(entry["date"])
    return {k: sorted(v) for k, v in seen.items()}


def theory_revision_pool(today=None):
    """Theory files already read, with when each is next due for a re-read.

    Same decay assumption as the problems: the first read starts the clock and
    every later read pushes it out. Notes read once in week 3 are gone by the
    time the interviews land, which is the whole reason this exists.
    """
    today = today or dt.date.today()
    pool = []
    for path, dates in theory_read_dates().items():
        reps = len(dates) - 1
        due = dates[-1] + dt.timedelta(days=INTERVALS[min(reps, len(INTERVALS) - 1)])
        pool.append({"path": path, "first_read": dates[0], "last_read": dates[-1],
                     "reps": reps, "due": due, "overdue": (today - due).days})
    return sorted(pool, key=lambda r: -r["overdue"])


# ---------------------------------------------------- recognition drill

def covered_folders(rows, week=None):
    """Folders he has reached: scheduled at or before this week, or already started."""
    week = week if week is not None else current_week()
    started = {r["folder"] for r in rows if r["status"] != "todo"}
    return {r["folder"] for r in rows if r["week"] <= week} | started


def drill_pick(rows, n=5, today=None, seed=None):
    """Unsolved problems from patterns already covered.

    Recognition is the skill the folder names give away: open
    solutions/02-two-pointers and the answer is in the path. These come back
    with the pattern stripped, so naming it is the exercise.
    """
    import random
    today = today or dt.date.today()
    rng = random.Random(seed if seed is not None else today.toordinal())
    week = current_week(today)
    covered = covered_folders(rows, week)
    pool = [r for r in rows if r["folder"] in covered and r["status"] == "todo"
            and r["statement"]]
    rng.shuffle(pool)
    return pool[:n]


def interleave_pool(rows, today=None, exclude=(), seed=None):
    """Unsolved problems from EARLIER patterns, shuffled, to break up blocked practice.

    A week of nothing but two pointers trains execution and hides the choosing:
    the folder has already answered the only question an interview asks first.
    Anything already queued for this week is excluded — re-listing a problem he
    is about to solve anyway teaches nothing.
    """
    import random
    today = today or dt.date.today()
    week = current_week(today)
    rng = random.Random((seed if seed is not None else today.toordinal()) + 7)
    pool = [r for r in rows if r["week"] < week and r["status"] == "todo"
            and r["file"] not in set(exclude)]
    rng.shuffle(pool)
    return pool
