# dsa-prep

Interview preparation: 454 curated problems, 53 patterns, and CS fundamentals.

**Timeline:** 10 Sep 2026 → 16 May 2027 (35 weeks)
**Target:** SDE-2 / backend roles at product companies

---

## Layout

| Folder | What's in it |
|---|---|
| [`patterns/`](patterns/) | **53 pattern guides** — recognition cue, the insight, diagrams, templates, pitfalls, every problem |
| [`solutions/`](solutions/) | **44 pattern folders, 454 runnable files** — two methods (brute force + optimal) and the real LeetCode test cases in each |
| [`theory/`](theory/) | **OS · Networks · DBMS · LLD · System Design · AI** — with Mermaid diagrams |
| [`templates/`](templates/) | Solution scaffold |
| [`notes/`](notes/) | Scratch notes, mock interview post-mortems |

## How I use this

1. Read the pattern guide **before** the first problem of a new topic
2. Attempt the problem cold — 25 min for Medium, 40 for Hard
3. Write the **brute force** method first, run it, get it green
4. Then write the **optimal** method and run both against the same cases
5. Timebox hit → read the editorial, close it, re-code from scratch
6. Fill in the docstring (both approaches, key insight, mistakes)
7. Paste the file link into the tracking sheet

### Running a problem

Every file runs on its own — no imports, no test framework, no setup:

```bash
python3 solutions/02-two-pointers/0011-container-with-most-water.py
```

```
BRUTE FORCE :
    case 1: PASS                 got=49  want=49
    case 2: PASS                 got=1   want=1

OPTIMAL     :
    -- not written yet --
```

Each file has:

- a docstring saying in plain words what the **input** is, what to **return**, and a worked **example**
- `<method>_brute` and `<method>` — the **same signature as LeetCode**, so working code pastes straight into the submission box, each body just `pass` for you to fill in
- `TESTS` — that problem's **own** example cases, pulled from its LeetCode page
- a runner that skips whichever method you have not written yet, so brute force first is the natural order

Outside that top docstring the files carry no comments — notes, approaches and
complexities all live in the docstring, so the code area stays clean.

Linked-list and tree problems include `build_list` / `build_tree` helpers, so a test case is written
as a plain list (`[3,9,20,None,None,15,7]`) and the runner builds the real structure for you.
In-place problems (`sortColors`, `rotate`, …) are checked on the mutated argument, not the return value.
Design problems (`MinStack`, `LRUCache`, …) get two classes and replay the LeetCode operation sequence.

**13 problems are the exception.** For things like `Linked List Cycle` or `Clone Graph`, LeetCode's judge
feeds data that does not match the method signature — `pos` is not a parameter, the graph arrives as an
adjacency list, `isBadVersion` is a hidden API. Those files carry the real signature, a **HEADS UP** note
explaining the mismatch, and the raw judge data as a comment, with `TESTS` left empty to fill in by hand.
Better an empty list than cases that fail for the wrong reason.

## Progress

| Phase | Weeks | Topic |
|---|---|---|
| Foundations | 1–10 | Arrays, two pointers, sliding window, prefix sum, hashing, strings, binary search, sorting |
| Linear structures | 11–14 | Linked lists, stacks, monotonic stack, queues, heaps |
| Recursion & trees | 15–20 | Recursion, backtracking, trees, BST, tries |
| Graphs | 21–23 | Traversal, topo sort, union-find, shortest path, MST |
| Greedy & DP | 24–27 | Greedy, 1D, knapsack, grid, strings, LIS, interval, tree, bitmask |
| Advanced | 28–29 | Bit manipulation, math, design data structures |
| Revision | 30–35 | Four sweeps, mocks, applications |

## Rules

- **Write the brute force down first.** In an interview you state it before optimising — that's what's being scored. Every file has a slot for it; run it before you touch the optimal one.
- **A hint is not a failure, but it is a flag.** `Solved unaided: Y` the moment it works, hints or not; `N` only for one I could not finish. `Hints used: Y` is what brings a problem back sooner.
- **The complexity is part of the answer.** Every solution's docstring states time and space.
