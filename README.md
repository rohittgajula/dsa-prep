# dsa-prep

Interview preparation: 454 curated problems, 53 patterns, and CS fundamentals.

**Timeline:** 10 Sep 2026 → 16 May 2027 (35 weeks)
**Target:** SDE-2 / backend roles at product companies

---

## Layout

| Folder | What's in it |
|---|---|
| [`patterns/`](patterns/) | **53 pattern guides** — recognition cue, the insight, diagrams, templates, pitfalls, every problem |
| [`solutions/`](solutions/) | **44 pattern folders, 454 stub files** — pre-filled with the problem, its date and a recognition hint |
| [`theory/`](theory/) | **OS · Networks · DBMS · LLD · System Design · AI** — with Mermaid diagrams |
| [`templates/`](templates/) | Solution scaffold |
| [`notes/`](notes/) | Scratch notes, mock interview post-mortems |

## How I use this

1. Read the pattern guide **before** the first problem of a new topic
2. Attempt the problem cold — 25 min for Medium, 40 for Hard
3. Timebox hit → read the editorial, close it, re-code from scratch
4. Commit the solution with the brute force **and** optimal approach in the docstring
5. Paste the file link into the tracking sheet

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

- **Write the brute force down first.** In an interview you state it before optimising — that's what's being scored.
- **Solved with a hint ≠ solved.** Flag it and re-solve within two weeks.
- **The complexity is part of the answer.** Every solution's docstring states time and space.
