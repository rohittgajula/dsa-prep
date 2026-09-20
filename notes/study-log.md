# Study log

One entry per study day, newest at the bottom. `scripts/plan.py` reads this to
know which theory files are done, so the next plan moves on by itself.

Keep the `- Theory:` lines as real paths — that is the part the script parses.

```text
## YYYY-MM-DD (week N)
- Theory: theory/os/01-processes-and-threads.md
- Solved: 53 Maximum Subarray — unaided, 22 min
- Revised: 1 Two Sum — still solid
- Quiz: sliding window, 4/6 — missed the shrink condition
- Note: anything worth remembering about the session
```

---

## 2026-09-20 (week 1)
- Solved: 26 Remove Duplicates from Sorted Array — optimal written himself (see correction below)
- Note: brute force logic was correct (`num not in sol`) but violated the problem contract —
  returned a new list instead of mutating `nums` and returning k.
- Note: second attempt wrote `nums[:len(sol)]` with no `=`. Bare slice is an expression,
  evaluates and discards. Right k, untouched array — the signature of a missing in-place write.
- Note: brute force never used the sorted constraint. It works on unsorted input, which is the
  tell that the whole optimisation was still on the table. Did not derive the two-pointer
  solution independently.
- Note: MY THINKING block left empty during the attempt.
- CORRECTION (same session): he wrote the optimal himself. His version uses the
  `slow = last kept index` convention, structurally different from the one posted in chat,
  which supports the claim. Judgement call on the unaided flag: he HAD read the posted
  solution and the file's recognition hint earlier in the session, so this is logged as
  `unaided: N (hinted)` rather than a clean solve. Re-solve cold in the next sweep to settle it.
- Note: correct pointer mechanics, but empty-array edge case returns 1 instead of 0 —
  a consequence of his convention, not a typo. Did not test an edge case before declaring done.
- Note: thinking block opens with "this is mostly a two pointer approach" — recognising the
  SHAPE of the input, not deriving from the sortedness observation. This is rubric point 4.
