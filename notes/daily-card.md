# Sat 31 Oct 2026 — 01-two-pointers · 133 left on the sheet

**Next up** (take as many as the sitting allows) — 125 Valid Palindrome, 283 Move Zeroes, 167 Two Sum Ii Input Array Is Sorted, 11 Container With Most Water
**Read** theory/os/01-processes-and-threads.md
**Revise** 26 Remove Duplicates From Sorted Array (sweep 1), 1 Two Sum (sweep 1), 27 Remove Element (sweep 1)
**Mixed** 136 Single Number — name the pattern before you start

## Recall

<!-- recall -->
In 27 Remove Element you build `newArr`, then write `nums = newArr` and `return len(newArr)`. The judge marks it wrong. Why does the caller never see your change, and what one line fixes it?
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
**An ad server handles 60k won impressions/sec across 3 regions. On every
win it runs `UPDATE campaigns SET spend = spend + price WHERE id = ?` on one
Postgres primary. One big advertiser ($50k/day) gets 8k wins/sec on a single
row. p99 on that UPDATE is 900ms against a 100ms bid deadline. So last week
someone cached "budget left" for 30s per server. Yesterday that campaign
overspent by 12%, and you owe the refund.**

1. Why does one hot row hurt this badly, and where exactly does the 12% overspend come from?
2. Change the design so the bid path never waits on a shared counter, while overspend stays under 1%.
3. What does your design cost at the end of the day, and for a $200/day campaign?

<details>
<summary>What a good answer covers</summary>

- Each UPDATE takes the row lock for the whole transaction. 8k/sec on one row is fully serial, so the queue grows and p99 climbs. More replicas do not help: writes all go to the primary.
- Overspend = servers x 30s x their win rate, and none of them sees the others' spend. At 8k/sec that is about 240k impressions bid blind.
- The fix is budget leases. A central allocator gives each server a slice (say 1% of what is left). The server spends from a local counter with no lock, then asks for more. Worst-case overspend = the slices still out, which is bounded and tunable.
- The cost: near the end of the day, money sits stuck in idle servers' slices, so you underdeliver. Shrink slices as budget runs low, and reclaim on a heartbeat.
- A tiny campaign cannot be split 100 ways. Below some threshold, send it to one owner server (shard by campaign id).
- Push: the advertiser wants overspend at zero. That means a synchronous check on every win, so name the latency and the money you give up for it.

</details>
<!-- /scenario -->

## Concept — 5 minutes

<!-- concept -->
**Connection pooling - why bigger is not better** *(DBMS)*

Opening a Postgres connection is slow. It costs a TCP + TLS handshake, auth,
and a forked backend process with its own memory (several MB). A pool opens N
connections once. Each request borrows one, runs its queries, and gives it back.

The catch: the database can only do as much work at once as it has CPU cores
and disk I/O. Say 8 cores and 200 connections, all running queries. The OS
time-slices 200 processes over 8 cores. Every query gets slower, cache hit
rates drop, and lock waits pile up. Throughput goes *down* and latency goes up.

A smaller pool makes extra requests wait in the app, in a cheap queue, instead
of fighting inside the database. A common starting point is about
`cores x 2 + effective disk spindles`. That is often 10-30, not 200. Then
measure.

<details>
<summary>Deeper — when it matters, and what it costs</summary>

- **Many app instances multiply it.** 50 pods x 20 connections = 1,000 backends. Postgres can fall over from memory and context switching alone. That is why you put PgBouncer (or RDS Proxy) in the middle: thousands of client connections, a few dozen real ones.
- **Transaction mode vs session mode.** PgBouncer in transaction mode shares a real connection between clients one transaction at a time. That works well, but it breaks anything tied to a session: `SET` variables, advisory locks, `LISTEN`, and some prepared-statement setups.
- **A small pool's real failure is long holds.** One request that holds a connection while it calls a slow HTTP API blocks a slot for seconds. Rule: never do network I/O while holding a connection. Also set a checkout timeout so callers fail fast instead of piling up.
- **When bigger is right:** the work is mostly waiting, not CPU (high-latency remote DB, long I/O-bound queries). Even then, raise it step by step and watch DB CPU and p99.
- **Cost of the extra layer:** one more hop (sub-ms), one more thing to run and monitor, and a single point of failure unless you run it as a pair.

**Interviewer push:** "Traffic doubled and p99 is up. Someone raised the pool from 20 to 100 and it got worse. Why?"
Answer: the database was already at its CPU or lock limit. Five times more concurrent queries just means more contention and context switching inside the DB. Fix the slow queries or add capacity (read replicas, sharding). Let the app-side queue absorb bursts, and shed load when the wait gets too long.

</details>
<!-- /concept -->

<details>
<summary>Answers</summary>

<!-- recall-answer -->
**Recall** — `nums = newArr` only rebinds your local name; the caller still holds the old list object. Mutate the object: `nums[:] = newArr`, then `return len(newArr)`. Better still, overwrite in place with a write index for O(1) space.
<!-- /recall-answer -->

**Pattern** — Two Pointers. Water above index i = min(maxLeft, maxRight) - height[i]. Two pointers or a monotonic stack.

</details>
