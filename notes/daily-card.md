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
**You run the webhook receiver for a payments product. The provider POSTs
`payment.succeeded`, you write a row and call your fulfilment service inline,
then return 200. Fulfilment has been down for 47 minutes. The provider retries
any non-200 with backoff for three days. Your receiver is holding 4,000
in-flight requests against a 200-connection pool.**

1. What gives out first — the provider's retries, your connection pool, or the
   database — and why?
2. Redesign the receive path so an hour of downstream failure costs you nothing.
3. Your new design returns 200 before fulfilment finishes. What can go wrong now
   that could not before, and what does fixing it cost?

<details>
<summary>What a good answer covers</summary>

- The pool goes first. 4,000 requests against 200 connections, each held open
  waiting on a dead service. Retries pile on while nothing drains, so backoff
  makes it worse before better. The database is fine — it is barely being asked.
- Receive path should do the minimum durable thing: verify the signature, write
  the event to a queue or an outbox row, return 200. Fulfilment becomes a
  consumer. An hour of downstream failure then costs queue depth, nothing else.
- You have traded synchronous confirmation for at-least-once delivery.
  Duplicates and out-of-order events are now real. Idempotency on the provider's
  event id with a unique constraint, and a consumer that no-ops on replay.
- Cost: you acknowledge before the work is done, so a poison event or a consumer
  bug is now silent. That buys you a dead-letter queue, lag alerting and a
  replay path you have actually tested.
- Where this gets pushed: two events for the same payment arriving out of order.
  A state machine that only moves forward, or a sequence check — not last-write-wins.

</details>
<!-- /scenario -->

<details>
<summary>Answers</summary>

**Recall** — in-place problems score `nums[:k]`; write back with `nums[:len(sol)] = sol` — a bare slice is a no-op

**Pattern** — Array Basics. Trivial. Use it to check your language's list operations are second nature.

</details>
