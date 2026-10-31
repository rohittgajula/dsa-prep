# Sat 31 Oct 2026 — 01-two-pointers · 133 left on the sheet

**Next up** (take as many as the sitting allows) — 125 Valid Palindrome, 283 Move Zeroes, 167 Two Sum Ii Input Array Is Sorted, 11 Container With Most Water
**Read** theory/os/01-processes-and-threads.md
**Revise** 26 Remove Duplicates From Sorted Array (sweep 1), 1 Two Sum (sweep 1), 27 Remove Element (sweep 1)
**Mixed** 136 Single Number — name the pattern before you start

## Recall

<!-- recall -->
DSA reasoning — ignoring a stated constraint — what goes wrong here, and what is the fix?
<!-- /recall -->

## Name the pattern

*Hard* — pattern, key insight, complexity. Do not solve it.

```text
INPUT
    height : list of integers

RETURN
    integer

EXAMPLE
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    ->  6
```

## System design — 10 minutes, out loud

<!-- scenario -->
**Today's theme:** a webhook receiver whose downstream is down for an hour

Set it up yourself: what is the scale, what breaks first, what do you
change, and what does that change cost you?
<!-- /scenario -->

## Concept — 5 minutes

<!-- concept -->
**Today's concept:** connection pooling - why bigger is not better *(DBMS)*

Nothing written yet. Say what it is, when you reach for it, and what
it costs you — then go and check yourself.
<!-- /concept -->

<details>
<summary>Answers</summary>

<!-- recall-answer -->
**Recall** — before optimising, ask which given constraint the brute force is not using yet
<!-- /recall-answer -->

**Pattern** — Two Pointers. Water above index i = min(maxLeft, maxRight) - height[i]. Two pointers or a monotonic stack.

</details>
