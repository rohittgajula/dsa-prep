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

## 2026-09-21 (week 1)
- Solved: 27 Remove Element — unaided (Y), hints used, 15 min. Brute force and optimal both green.
- Note: brute force blocked on the in-place contract again — this time `nums, newArr = newArr, nums`,
  which rebinds local names only. Third variant of the same slip in two days. weak-topics updated.
- Note: came in believing a brute force is exempt from the in-place contract. Corrected — brute
  describes wasted work, not a changed signature.
- Note: optimal used `for fast in nums` (values) instead of `range(len(nums))` (indices). Passed
  case 1 by coincidence, raises IndexError when a value exceeds the array length.
- Note: assumed a LeetCode Accepted meant the local file was identical; one line differed.
  Lesson taken: diff before theorising about why "the same code" behaves differently.
- Note: stated O(n) time / O(1) space for the optimal correctly and unprompted. Missed the
  brute force's O(n) space until asked — that contrast is the reason the optimal exists.
- Note: MY THINKING block on 27 still empty.
- Solved: 66 Plus One — unaided (Y), 10 min. Right-to-left carry logic was the key move; all-9s case required the leading 1, with no hint used.

## 2026-09-23 (week 1)
- Solved: 88 Merge Sorted Array — unaided (Y), hints used, 20 min. Brute append-and-sort and optimal back-fill merge both green.
- Note: key insight was to use nums1's spare slots from the back, so merging does not overwrite unprocessed values.
