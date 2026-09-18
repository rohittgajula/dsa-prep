# Operating Systems

`Weeks 1–5` of the prep plan.

| # | File | Topics |
|---|---|---|
| 01 | [Processes & Threads](01-processes-and-threads.md) | process vs thread, context switch, fork/exec, zombies, IPC, concurrency models |
| 02 | [CPU Scheduling](02-scheduling.md) | metrics, FCFS/SJF/RR/MLFQ, Gantt charts, priority inversion |
| 03 | [Concurrency](03-concurrency.md) | race conditions, mutex/semaphore/monitor, producer-consumer, deadlock |
| 04 | [Memory Management](04-memory-management.md) | paging, TLB, virtual memory, page faults, thrashing, replacement algorithms |
| 05 | [Storage, I/O & Linux](05-storage-io-and-linux.md) | inodes, disk scheduling, RAID, epoll, fsync, containers, debugging |

## The five questions that come up most

1. **Process vs thread** — recite the shared/private table
2. **Deadlock** — four Coffman conditions, and which strategy breaks which
3. **Producer–consumer** — write it from memory with the semaphores in the right order
4. **Page replacement** — count faults for FIFO / LRU / Optimal on a reference string
5. **Paging arithmetic** — offset bits, page table size, effective access time

## Connections to the rest of the prep

| OS concept | Where it reappears |
|---|---|
| LRU page replacement | [LRU Cache pattern](../../patterns/design/lru-lfu-cache.md) · LeetCode 146 |
| Recursion stack depth | [Tree DFS](../../patterns/recursion-trees/tree-dfs.md) — why deep DFS overflows |
| `fsync` durability | DBMS — the D in ACID, write-ahead logging |
| epoll / C10K | System Design — how servers hold many connections |
| SIGTERM vs SIGKILL | System Design — graceful shutdown in Kubernetes |
