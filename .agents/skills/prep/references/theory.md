# OS, Networking, DBMS

These are asked as *verbal* questions. The goal is a clear 60-90 second spoken answer, not a complete chapter.

## Shape of an answer

```text
What is it        1-3 sentences, plain words
Why it exists     the problem it solves - always include this
How it works      the mechanism, stepwise, with a diagram if there is state or flow
Example           something concrete, ideally something he has touched
Remember          2-4 points
```

Skip any section that adds nothing. A question like "what is a zombie process" needs four lines, not five headings.

## Rules specific to these subjects

- **Lead with the problem, not the definition.** Paging makes sense only after "physical memory is smaller than what programs want, and programs must not see each other's memory".
- **Separate the confusable pairs explicitly.** Process vs thread, concurrency vs parallelism, mutex vs semaphore, paging vs segmentation, TCP vs UDP, blocking vs non-blocking vs async, authentication vs authorisation, latency vs bandwidth vs throughput, `SIGTERM` vs `SIGKILL`. A two-row table is usually enough.
- **Give numbers where they anchor intuition.** RAM access ~100 ns, SSD read ~100 us, disk seek ~10 ms, same-datacentre round trip ~0.5 ms, cross-continent ~150 ms. These make design trade-offs obvious.
- **Connect the layers.** OS LRU page replacement is LeetCode 146. Dijkstra is OSPF. `fsync` is the D in ACID. `epoll` is how one box holds 100k connections. The repo's `theory/README.md` keeps a cross-link table — reuse it and add to it.

## Diagrams that carry their weight

One ASCII block, complete flow. Typical subjects:

- Process states: new -> ready -> running -> waiting -> terminated, with what causes each edge.
- Virtual -> physical address translation, page table, TLB hit and miss.
- Deadlock: two threads, two locks, the cycle drawn.
- Packet going down the layers with headers added, and back up.
- TCP three-way handshake and teardown, with sequence numbers and state names.
- What happens when you type a URL: DNS -> TCP -> TLS -> HTTP -> render. The single most-asked networking question.

## Per subject, what interviews actually want

**Operating Systems** — process vs thread, context switch cost, scheduling algorithms and when each is used, race conditions, mutex/semaphore/condition variable, deadlock's four conditions and how to break them, virtual memory and paging, page faults, thrashing, TLB, user vs kernel mode and the system call boundary, fork/exec, zombies and orphans, memory layout of a process.

**Networking** — the layers and what lives at each, TCP vs UDP and when to choose which, handshake and teardown, flow vs congestion control, IP addressing and subnetting, NAT, ARP, DNS resolution end to end, HTTP/1.1 vs 2 vs 3, HTTPS and the TLS handshake, status codes, cookies and sessions, WebSockets vs polling vs SSE, load balancers and proxies, CDN, common ports.

**DBMS** — normalisation up to 3NF and when to denormalise, indexes and B+ trees, why an index can be skipped, ACID, isolation levels and the anomaly each prevents, locking vs MVCC, transactions and deadlocks, SQL vs NoSQL trade-offs, joins, query plans, sharding and replication.

## Follow-ups to anticipate

Good interviewers push one level past the definition. Prepare him for the push, not just the definition:

- "Why is a context switch expensive?" after process vs thread.
- "So why does TCP still have head-of-line blocking in HTTP/2?" after TCP vs UDP.
- "What does the OS actually do on a page fault?" after virtual memory.
- "Read committed prevents which anomaly, and which one does it still allow?" after isolation levels.

End a taught concept with the one follow-up he is most likely to get.
