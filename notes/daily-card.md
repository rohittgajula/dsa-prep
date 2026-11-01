# Sun 01 Nov 2026 — 01-two-pointers · 295 left on the sheet

**Next up** (take as many as the sitting allows) — 125 Valid Palindrome, 283 Move Zeroes, 11 Container With Most Water, 15 3Sum
**Read** theory/os/01-processes-and-threads.md
**Revise** 26 Remove Duplicates From Sorted Array (sweep 1), 1 Two Sum (sweep 1), 27 Remove Element (sweep 1)
**Mixed** 14 Longest Common Prefix — name the pattern before you start

## Recall

<!-- recall -->
DSA reasoning — ignoring a stated constraint — what goes wrong here, and what is the fix?
<!-- /recall -->

## Name the pattern

*Easy* — pattern, key insight, complexity. Do not solve it.

```text
INPUT
    nums : list of integers

RETURN
    list of integers

EXAMPLE
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    ->  [5, 6]
```

## System design — 10 minutes, out loud

<!-- scenario -->
**Today's theme:** a cache that all expires at the same second — the stampede

Set it up yourself: what is the scale, what breaks first, what do you
change, and what does that change cost you?
<!-- /scenario -->

## Concept — 5 minutes

<!-- concept -->
**Today's concept:** process vs thread *(OS)*

Nothing written yet. Say what it is, when you reach for it, and what
it costs you — then go and check yourself.
<!-- /concept -->

<details>
<summary>Answers</summary>

<!-- recall-answer -->
**Recall** — before optimising, ask which given constraint the brute force is not using yet
<!-- /recall-answer -->

**Pattern** — Two Pointers. Values in 1..n with O(1) space -> mark index abs(v)-1 negative, then collect positives.

</details>
