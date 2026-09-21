# Mon 21 Sep 2026 — week 1

**Solve** 27 Remove Element, 66 Plus One, 53 Maximum Subarray
**Read** theory/os/01-processes-and-threads.md
**Revise** 1 Two Sum (sweep 1)

## Recall

An in-place array problem: your returned list holds the right values, but the
judge still fails you. What is it actually reading, and what must you return?

## Name the pattern

*Easy* — pattern, key insight, complexity. Do not solve it.

```text
INPUT
    prices : list of integers

RETURN
    integer

EXAMPLE
    prices = [7, 1, 5, 3, 6, 4]
    ->  5
```

## System design — 10 minutes, out loud

<!-- scenario -->
**A marketplace app shows search suggestions as you type. 3M daily users,
peak 120k suggest requests/sec, one request per keystroke. Each request is a
prefix query against Elasticsearch over 80M product titles, with a Redis cache
keyed on the exact prefix string (60% hit rate). p99 has gone from 40ms to
310ms over three months and the box now feels laggy on mobile.**

1. What breaks first here, and why did it get worse over three months?
2. What do you change?
3. What does that change cost you, and when does it stop working?

<details>
<summary>What a good answer covers</summary>

ES is doing 48k uncached prefix queries/sec against a growing index — the miss
rate is the problem, and misses grew because the long tail of prefixes grew
with the catalog. Cheapest win first: client-side debounce of 100-150ms cuts
QPS 3-4x for free, at the cost of the last keystroke feeling slower.
Real fix: precompute top-10 suggestions for the head prefixes into a trie/FST
and ship it in-process on every suggest node — ~1M prefixes is a few hundred MB,
no network hop, sub-ms. Send only the tail to ES.
The cost is staleness: new and trending items appear only at rebuild interval,
and a shared trie cannot rank per user. Push on where you cut head vs tail, what
rebuild time and memory look like at 3x catalog, and what serves the first
request after a deploy.

</details>
<!-- /scenario -->

<details>
<summary>Answers</summary>

**Recall** — the judge reads the first k slots of the input array, not your return value. Mutate the caller's array (`nums[:len(sol)] = sol`; a bare `nums = sol` rebinds a local and does nothing) and return k, the count.

**Pattern** — Array Basics. Track the minimum price seen so far; at each day ask what profit selling today would give.

</details>
