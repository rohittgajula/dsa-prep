# Thu 08 Oct 2026 — week 4

**Solve** 53 Maximum Subarray, 121 Best Time To Buy And Sell Stock
**Read** theory/os/01-processes-and-threads.md
**Revise** 1 Two Sum (sweep 1), 26 Remove Duplicates From Sorted Array (sweep 1), 27 Remove Element (sweep 1)
**Mixed** 42 Trapping Rain Water — name the pattern before you start

## Recall

<!-- recall -->
DSA reasoning — ignoring a stated constraint — what goes wrong here, and what is the fix?
<!-- /recall -->

## Name the pattern

*Medium* — pattern, key insight, complexity. Do not solve it.

```text
INPUT
    nums : list of integers
    k    : integer

RETURN
    integer

EXAMPLE
    nums = [4, 5, 0, -2, -3, 1], k = 5
    ->  7
```

## System design — 10 minutes, out loud

<!-- scenario -->
**Today's theme:** the same request arriving twice because the client retried

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

**Pattern** — Prefix Sum. Same remainder idea as 523, but COUNT the pairs. Careful with negative modulo.

</details>
