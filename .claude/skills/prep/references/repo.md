# The dsa-prep repo

This skill lives **inside** the repo, at `.claude/skills/prep/`, and is reached through a symlink from `~/.claude/skills/prep`. So the repo root is always two levels above this file — clone it anywhere and the skill comes with it.

That repo is the **source of truth** for his preparation. Read it before answering anything about progress, order, or what to study. Never invent a generic roadmap when this one exists.

Paths in this file are written as `~/Desktop/dsa-prep`, which is where it sits on his main machine. On any other machine, substitute wherever it is cloned — everything below is relative to the repo root.

## Layout

```text
dsa-prep/
  README.md        the plan: 35 weeks, 10 Sep 2026 -> 16 May 2027, SDE-2 backend
  patterns/        53 pattern guides, grouped by family
                   recognition cue -> insight -> diagram -> template -> pitfalls -> problems
  solutions/       44 numbered folders, 454 runnable Python files
  theory/          os/ networks/ dbms/ lld/ system-design/ ai/   (Mermaid diagrams)
  templates/       solution-template.py
  scripts/         prep_lib.py (shared parser), progress.py, plan.py
  notes/           study-log.md, weak-topics.md, mock interview post-mortems
```

Folders are numbered in study order (`01-array-basics` ... `44-advanced`), so the filesystem order *is* the roadmap order.

## Reading his progress

**Run the scraper. Do not guess, and do not hand-grep the files.**

```bash
cd ~/Desktop/dsa-prep && python3 scripts/progress.py
```

It parses all 454 files with `ast` and reports: overall and core counts, per-folder bars, the current week against the 10 Sep 2026 start, what is **behind**, what is left **this week**, the **re-solve** queue, and solved problems whose docstring is still the template.

```bash
python3 scripts/progress.py --week 3      # one week
python3 scripts/progress.py --folder 02   # one pattern folder
python3 scripts/progress.py --full        # nothing truncated
python3 scripts/progress.py --json        # rows, for filtering
```

Status comes from the code itself: `todo` (both bodies `pass`), `brute` (brute only), `done` (both). Two flags come from the docstring footer — `hinted` (`Solved unaided: N`, so it does not count yet and is re-solved within two weeks) and `no notes` (code written, docstring still placeholders).

Use `--json` when the question needs filtering the scraper does not do, for example "which Mediums did I take over 40 minutes on".

## Planning his day

```bash
python3 scripts/plan.py              # today + the next 4 days
python3 scripts/plan.py --days 7     # a week ahead
python3 scripts/plan.py --revise 5   # just a revision set
python3 scripts/plan.py --drill 5    # name the pattern, do not solve
python3 scripts/plan.py --drill 5 --answers
python3 scripts/plan.py --date 2026-10-05
```

The plan is **derived, never stored**: from which files have real code, which theory files `notes/study-log.md` says he has read, when each solved problem is next due for a sweep, and what is open in `notes/weak-topics.md`. Nothing to keep in sync — solve something, log it, and tomorrow's plan moves on by itself.

It decides the daily load from what is actually left: core problems remaining this week divided by days left in the week, capped at 4. Problems from earlier weeks go first. Theory is paced so the track finishes in its weeks.

**Run it, then adapt it out loud.** The script does not know he has 40 minutes tonight or that he is tired. Take its output and cut it to fit — say what you are dropping and why. If he is far behind, say so plainly and propose dropping Stretch problems rather than pretending the plan still fits.

## Recognition drill

The gap the repo could not close on its own: `solutions/02-two-pointers/` names the answer in the path, so solving from the folder trains execution and never trains **choosing**. In an interview the first 60 seconds are choosing.

`--drill N` hands back problem statements he has not solved, from patterns already covered, with the pattern, folder and recognition hint stripped. For each one he says: the pattern, the key insight, the complexity. Out loud, 60 seconds, no code.

Mark each answer as he gives it. What counts as right is the *reason*, not the label — "two pointers because it is an array" is wrong even when the label is correct. Push for the observation that forces the technique.

Never let a drill turn into a solving session. If he wants to solve one, that is a different sitting.

## Interleaving and mocks

Each day's plan carries a `mixed` problem: one unsolved problem from an **earlier** pattern, unlabelled. Blocked practice — a whole week of two pointers — feels productive and transfers badly. Make him name the pattern before he writes anything.

Sunday gets a `mock` slot: 45 minutes out loud, one problem and one system design prompt. Post-mortem goes in `notes/`, and anything vague goes to `weak-topics.md`.

## Revision

Spaced repetition, from the docstring dates. `Solved on:` starts the clock, each date in `Revised:` extends it. Sweeps land at **3, 7, 21, 60, 120 days** — shortened to 2, 5, 14, 40, 90 for anything marked `Solved unaided: N`, since a hinted problem is the one most likely to evaporate.

When `Solved on:` is blank the file's modification time stands in, so revision works even before he fills anything in. Ask him to fill the real date when it matters.

Revising means: **state the approach and complexity from memory, without opening the file.** Only then open it. If he cannot, that is the signal — it goes to `weak-topics.md` and the sweep count resets.

After a sweep, add today's date to the `Revised:` line in that file.

**Theory decays the same way** and is swept on the same intervals, counted from the read dates in `study-log.md`. OS notes read in week 3 are gone by week 20, which is when the interviews actually happen. `plan.py` lists theory that is due as `re-read`.

## Check-in

When he asks how he is doing, or at the start of a session after a gap:

1. Run `plan.py` and read the last few `study-log.md` entries.
2. Ask **4-6 questions, one at a time**, drawn from what he actually solved and read recently, plus the open weak topics. Not a quiz on things he has not touched.
3. Grade each answer as he gives it. Say what was missing rather than just "correct".
4. Finish with: what is solid, what is shaky, and the one thing to fix this week.
5. Log the result to `study-log.md` and update `weak-topics.md`.

Pull at least one question from something a few weeks old. Recent material always feels solid; the point is to find what has decayed.

## "What should I learn next?"

1. Run `python3 scripts/progress.py` — it gives the week, what is behind, and what is left.
2. Read `notes/weak-topics.md` for open entries.
3. Clear **behind** core problems before anything new; open weak topics outrank new material too.
4. Otherwise take this week's remaining core problems, and read the matching guide in `patterns/` first.
5. Answer with the actual topic, why it comes now, and 3-5 named problems from the right folder.

Answer with files and problem numbers, never with a generic "learn arrays then linked lists".

## Teaching a topic that already exists

Read the pattern guide first (`patterns/<family>/<name>.md`) and match its vocabulary, its template, and its stated key insight. Two different explanations of sliding window in two places is worse than one.

If the guide is thin or missing something interview-relevant, say so and offer to extend it — do not quietly teach a different version.

## Closing out a problem

The moment both methods pass, do all of this **without being asked**:

1. Run the file. Both methods green, or stop — a problem whose tests fail is not finished.
2. Ask him for the time and space complexity out loud before you write anything. Ten seconds, and it is the part an interview actually scores.
3. Fill every blank in the docstring.
4. Commit that one file and push.
5. Append a line to `notes/study-log.md`.

### What goes in each blank

| Field | What to write |
|---|---|
| `BRUTE FORCE` | the approach in a line or two, the way he would say it out loud |
| `Time` / `Space` | the notation **and** the reason, on the same line |
| `OPTIMAL` | the approach, and what the brute force was wasting |
| `KEY INSIGHT` | one sentence — the thing that makes the problem collapse |
| `MISTAKES I MADE` | what actually went wrong this session |
| `Solved on` | today, as `YYYY-MM-DD` |
| `Solved unaided` | `Y` once he gets it out, hints or not. `N` only if he could not finish it |
| `Hints used` | `Y` if he took any hint, read a posted solution, or read the recognition hint |
| `Tutor review` | three lines, see `references/dsa.md` |

Complexity keeps the shape already in the file, with the reason after the notation:

```text
    Time  : O(n)    one pass, each element visited once
    Space : O(n)    the map can hold every element in the worst case
```

If he wrote a complexity himself, leave it — unless it is wrong, in which case correct it, say so plainly, and treat it as a weak-topic candidate.

**`MISTAKES I MADE` is never invented.** Write what actually happened: the off-by-one he hit, the case he forgot, the first approach he abandoned. That is all in the session, so use it. If he solved it away from you and there is nothing to draw on, ask him one short question instead of writing something plausible. A plausible invented mistake is worse than a blank, because the revision sweeps trust this field.

**`Solved unaided` carries his meaning, not the README's older one.** `Y` the moment he produces a working solution, whether or not he needed help; `N` only when he could not finish it at all. He set that on 20 Sep 2026, overriding the repo's original "solved with a hint is not solved". Do not re-argue it.

**`Hints used` carries the signal instead**, and it is the one that matters for scheduling. `Y` if you gave him any rung of the hint ladder, or he read a posted solution or the file's recognition hint before finishing. Sweeps then run at 2/5/14/40/90 days instead of 3/7/21/60/120; a `Solved unaided: N` runs shorter still, at 1/3/7/21/60.

Ask him rather than assume. "Did you need a hint on that one?" is one question and it keeps the whole revision schedule honest.

**`MY THINKING` stays his.** Never fill in or rewrite those four prompts. Only the `Tutor review:` slot underneath is yours.

### Committing and pushing

He authorised this standing, on 20 Sep 2026: **when a problem is finished, commit and push it without asking.**

```bash
git add <that problem's file> notes/study-log.md
git commit -m "<message>"
git push origin HEAD
```

- Stage that problem's file and the study log, nothing else. Never `git add -A` — unrelated work in the tree is not yours to commit.
- Match the message style of the recent log (`git log --oneline -5`); it is his own.
- Never push a problem whose tests do not pass. Say it failed and stop.
- If the push fails, leave the commit in place, tell him exactly what git said, and do not retry in a loop.

This standing permission covers finished problems only. Anything else — a bulk edit, a script, a roadmap change — is still asked for first.

## Writing into the repo

- Markdown files use **Mermaid** diagrams (GitHub renders them). Chat answers use ASCII.
- Match the existing heading style and tone — short, direct, no filler.
- Do not reformat or reorganise files he did not ask about.
- `notes/` is the right home for mock interview post-mortems and weak-topic lists.

## notes/study-log.md

Append one entry per study day, newest at the bottom. **This is what makes the plan move** — `plan.py` parses the `- Theory:` lines to know what has been read.

```text
## 2026-09-20 (week 1)
- Theory: theory/os/01-processes-and-threads.md
- Solved: 53 Maximum Subarray — unaided, 22 min
- Revised: 1 Two Sum — still solid
- Quiz: sliding window, 4/6 — missed the shrink condition
- Note: anything worth remembering about the session
```

Write it at the end of a session without being asked, and say in one line that you did. Keep theory paths exact — a wrong path silently leaves that file looking unread.

## Roadmap changes

Allowed to suggest, never to apply silently. Format:

```text
Roadmap suggestion: <change>
Reason: <interview relevance | missing prerequisite | better progression | commonly tested pattern>
```

Also fair game: calling out a topic in the plan that is low value for SDE-2 backend interviews, or a topic that should be split into smaller subtopics.


## notes/weak-topics.md

His live list of recurring mistakes. **Read it before any revise, quiz, or mock session** and aim the questions at the open entries. The scraper prints the open count.

Append when a slip is real and repeated — the second occurrence, or the first that costs a whole problem. A typo is not a weak topic. Format:

```text
### <topic> — <pattern or subject>
**Slip:** what goes wrong, in one line
**Fix:** the correction, in one line
**Seen:** 2026-09-20, 2026-10-02
**Status:** open | cooling | closed
```

Rules:

- Same slip again -> add the date to `Seen` on the existing entry. Never a second entry for the same thing.
- He gets it right -> `open` becomes `cooling`. Right again, weeks later -> `closed`, moved to the Closed section.
- Say out loud when logging one, in a single line: *logged: records best length before restoring validity*. Never log silently.
- His words for the slip, not a polished rewrite.
- Entries are about *understanding*, not effort. "Forgot to run the file" is not a weak topic.


## The daily card

A scheduled task (`~/.claude/scheduled-tasks/dsa-daily-card/`) runs each morning, writes `notes/daily-card.md` — today's plan, one recall question, one recognition drill, answers hidden behind a `<details>` block — and pushes it so he can read it on the GitHub mobile app.

It runs while the desktop app is open; if the app was closed it runs at next launch. It is not a substitute for a real session — it is two minutes of retrieval before the day starts.

If he mentions the card, read the current `notes/daily-card.md` rather than guessing what it said.
