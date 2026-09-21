# Sun 20 Sep 2026 — week 1

**Solve** 27 Remove Element, 66 Plus One
**Read** theory/os/01-processes-and-threads.md
**Revise** 26 Remove Duplicates From Sorted Array (sweep 1)
**Mock** 45 minutes out loud: one problem, one system design prompt

## Recall

Arrays — in-place modification contract — what goes wrong here, and what is the fix?

## Name the pattern

*Easy* — pattern, key insight, complexity. Do not solve it.

```text
INPUT
    nums : list of integers

RETURN
    list of integers

EXAMPLE
    nums = [1, 2, 1]
    ->  [1, 2, 1, 1, 2, 1]
```

## System design — 10 minutes, out loud

<!-- scenario -->
**A food delivery app dispatches orders to couriers. One city at dinner peak:
900 orders/sec, about 40,000 couriers online, and for any given order only
~50 couriers are close enough to matter. Dispatch reads candidate couriers
from a Postgres read replica, picks the nearest free one, then runs
`UPDATE couriers SET status='assigned' WHERE id=?`. Support is now seeing the
same courier assigned to two orders, and couriers are rejecting jobs they
were never really given.**

1. What breaks first, and why?
2. What do you change?
3. What does that change cost you, or when does it stop working?

<details>
<summary>What a good answer covers</summary>

Replica lag makes the candidate set stale, but that is not the bug — the bug
is that the UPDATE is unconditional, so two dispatchers both "win". The
cheap fix is a conditional write: `WHERE id=? AND status='free'`, check rows
affected, re-pick on 0. That makes correctness safe but moves the pain to
contention: with 900/s fighting over ~50 hot couriers, losers retry and
retry rate climbs fast. The alternative is a single assigner per city or geo
cell, which removes contention entirely and lets you batch a 2s window for
better matching — at the cost of a failure domain, a hot cell at a stadium,
and added latency. Either way an assignment is not a boolean: the courier
must ack, so it needs a reservation with a TTL.
Push: the single assigner dies holding 200 unacked reservations — what
happens, and who notices?

</details>
<!-- /scenario -->

<details>
<summary>Answers</summary>

**Recall** — in-place problems score `nums[:k]`; write back with `nums[:len(sol)] = sol` — a bare slice is a no-op

**Pattern** — Array Basics. Trivial. Use it to check your language's list operations are second nature.

</details>
