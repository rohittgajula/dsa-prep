# Tue 22 Sep 2026 — week 1

**Solve** 53 Maximum Subarray, 88 Merge Sorted Array, 121 Best Time To Buy And Sell Stock, 169 Majority Element
**Read** theory/os/01-processes-and-threads.md
**Revise** 1 Two Sum (sweep 1), 26 Remove Duplicates From Sorted Array (sweep 1)

## Recall

<!-- recall -->
A function takes `nums` and must change it in place. Why does `nums = sorted(nums)` leave the caller's list untouched, while `nums[:] = sorted(nums)` changes it?
<!-- /recall -->

## Name the pattern

*Easy* — pattern, key insight, complexity. Do not solve it.

```text
INPUT
    nums : list of integers

RETURN
    optimal : nothing is returned - nums itself is changed
    brute   : may return the finished result instead - the runner
              accepts either

EXAMPLE
    nums = [0, 1, 0, 3, 12]
    ->  nums becomes [1, 3, 12, 0, 0]
```

## System design — 10 minutes, out loud

<!-- scenario -->
**A team chat product. Postgres 14, one primary and two read replicas. The
`messages` table is 1.9B rows and 2.4 TB, and its `id` column is a `serial` —
int4, ceiling 2,147,483,647. You write 40M messages/day and it is climbing, so
you have about six weeks before inserts start failing. Every channel open reads
this table; p99 is 45ms and product will not accept worse. The plan on the wiki
is `ALTER TABLE messages ALTER COLUMN id TYPE bigint` in a Sunday window.**

1. What happens when that ALTER runs, and how long is the site down?
2. How do you get to int8 without a long lock?
3. What does your version cost, and does it fit in six weeks?

<details>
<summary>What a good answer covers</summary>

`ALTER COLUMN TYPE` takes ACCESS EXCLUSIVE and rewrites the whole table plus
every index — 2.4 TB at ~150 MB/s is 4-6 hours of hard downtime, and the WAL
flood puts both replicas far behind. That is an outage, not a window.
The usual escape: add `id_new bigint` (instant), backfill in ~10k batches
throttled on replication lag, build a unique index CONCURRENTLY, then swap the
key and sequence under a seconds-long lock with `lock_timeout` set so it fails
instead of queueing behind a long read. Cost: ~3 weeks of backfill, double write
cost and vacuum pressure while both columns live, and every FK pointing at
`messages.id` needs the same treatment. Push: at cutover, what value does the
sequence restart at, and how do you avoid a duplicate or a gap?

</details>
<!-- /scenario -->

## Concept — 5 minutes

<!-- concept -->
**L4 vs L7 load balancer** *(HLD)*

A load balancer has to pick a backend. The question is how much of the request
it is allowed to read before deciding.

**L4** works at TCP level. It sees IP and port, nothing else. It picks a
backend, then shovels bytes both ways without understanding them. It cannot
read a URL or a header, because the payload may be encrypted and it never
terminates TLS. Cheap, fast, and it works for any protocol.

**L7** terminates the connection, parses the HTTP request, and decides using
what it read — path, host, cookie, header. `/api/*` to one pool, `/static/*`
to another. It can retry a failed request on a second backend, because it
still holds the parsed request. L4 cannot: it has already forwarded the bytes.

<details>
<summary>Deeper — when it matters, and what it costs</summary>

**When each one wins**

L7 whenever routing depends on request content, or you want per-path timeouts,
retries, canary splits by header, or one TLS certificate in front of many
services. That is most web traffic — and it is what an "API gateway" is.

L4 when you need raw throughput, non-HTTP protocols (databases, gRPC streams,
game traffic, SMTP), or true end-to-end encryption where the balancer must not
hold the private key. Also when connections are long-lived and the per-request
parse buys you nothing.

**What L7 costs**

It is a real proxy: it terminates TLS and re-encrypts to the backend, so you
pay CPU per request and add a hop of latency — usually 1-3ms, more under load.
It holds state per connection, so it is the thing that falls over first. And it
must now be scaled and made highly available itself.

**The follow-up**

"Your L7 terminates TLS — what does the backend see as the client IP?" Answer:
not the client. You need `X-Forwarded-For` or PROXY protocol, and the backend
must be configured to trust it, or you will rate-limit the load balancer's own
address instead of the caller.

</details>
<!-- /concept -->

<details>
<summary>Answers</summary>

<!-- recall-answer -->
**Recall** — `nums = ...` only rebinds the local name; the caller still holds the original object. `nums[:] = ...` is slice assignment, which overwrites the contents of that same object, so the caller sees it. Same reason rebinding via `nums, tmp = tmp, nums` never reaches the caller.
<!-- /recall-answer -->

**Pattern** — Array Basics. Slow write pointer places non-zeros; fill the rest with zeros. Same skeleton as 26 and 27.

</details>
