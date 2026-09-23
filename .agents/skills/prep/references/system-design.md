# System Design

A design round is a conversation, not an essay. Teach the **order of moves**, because that order is what is actually scored.

## The order

```text
1. Requirements        functional, then non-functional. Ask, do not assume.
2. Scale estimate      users, QPS, read:write ratio, storage per year
3. API                 3-5 endpoints, request and response shape
4. Data model          entities, keys, access patterns
5. High level design   the one box diagram
6. Deep dive           the 1-2 pieces that actually carry the load
7. Bottlenecks         what breaks first, and how it is fixed
```

Never start at step 5. Jumping straight to boxes is the single most common failure, and it is the one interviewers notice.

## Scale estimates

Only what changes a decision. Rough numbers, stated out loud:

```text
100M users, 10% daily active       -> 10M DAU
each writes 2 posts/day            -> 20M writes/day ~ 230 writes/s
read:write 100:1                   -> ~23k reads/s
post ~ 1 KB                        -> 20 GB/day  ~ 7 TB/year
```

Then say what the numbers imply: 23k reads/s means cache, 7 TB/year means shard.

## The diagram

One ASCII block, the complete path. Draw the request going in and the response coming out.

```text
              Client
                |
              DNS / CDN          static assets stop here
                |
           Load Balancer
                |
        +-------+-------+
        |               |
   API Server      API Server     stateless, horizontally scaled
        |               |
        +-------+-------+
                |
        +-------+--------+---------------+
        |                |               |
      Cache          Database        Message Queue
     (Redis)       (primary +           (Kafka)
        |           replicas)              |
     miss -> DB                        Workers
                                     (async: feed
                                      fan-out, email)
```

Then talk through it: what is synchronous, what is async, what happens on a cache miss, what happens when a node dies.

## Always state trade-offs

Every choice is a trade, and saying the trade is what separates a pass from a fail:

- SQL vs NoSQL: joins and transactions vs write scale and flexible schema.
- Strong vs eventual consistency: correctness vs availability and latency.
- Sync vs async: simplicity and immediate feedback vs throughput and resilience.
- Cache write-through vs write-back vs cache-aside: freshness vs write latency vs complexity.
- Sharding key: even distribution vs query locality — and name the hot-key risk.
- Monolith vs services: operational simplicity vs independent scaling and deploys.

Never present one option as simply correct. Say what it costs.

## Building blocks he must be able to explain cold

Load balancer (L4 vs L7, algorithms), reverse proxy, CDN, cache (eviction, invalidation, stampede), database replication (leader-follower, lag, failover), sharding (range, hash, consistent hashing), message queue (at-least-once vs exactly-once, ordering, dead letter queue), rate limiting (token bucket, sliding window), CAP in practice, idempotency, pagination at scale, search index, blob storage, health checks and graceful shutdown, metrics/logs/traces.

## Classic questions

URL shortener, rate limiter, pastebin, news feed, chat/WhatsApp, Twitter timeline, YouTube/Netflix, Uber, ticket booking, notification service, web crawler, Google Docs, distributed cache, key-value store.

Start with the simple version that works, then scale it under pressure — same brute force -> optimal rhythm as DSA.

## LLD

Different round, different skill. Requirements -> classes and responsibilities -> relationships -> which SOLID principle each choice serves -> which design pattern fits and *why that one*. Write real class signatures, keep behaviour in the right class, and name the pattern out loud (strategy, observer, factory, state, singleton). Usual asks: parking lot, elevator, Splitwise, BookMyShow, rate limiter, vending machine, chess.
