# Operating Systems

`Weeks 1–5` of the prep plan.

| # | File | Topics |
|---|---|---|
| 01 | [Processes & Threads](01-processes-and-threads.md) | process vs thread, context switch, fork/exec, zombies, IPC, concurrency models |
| 02 | [CPU Scheduling](02-scheduling.md) | metrics, FCFS/SJF/RR/MLFQ, Gantt charts, priority inversion |
| 03 | [Concurrency](03-concurrency.md) | race conditions, mutex/semaphore/monitor, producer-consumer, deadlock |
| 04 | [Memory Management](04-memory-management.md) | paging, TLB, virtual memory, page faults, thrashing, replacement algorithms |
| 05 | [Storage, I/O & Linux](05-storage-io-and-linux.md) | inodes, disk scheduling, RAID, epoll, fsync, debugging a slow box |
| 06 | [**Kernel & System Calls**](06-kernel-and-system-calls.md) | protection rings, syscalls, interrupts vs traps vs exceptions, kernel architectures, boot, signals |
| 07 | [**Memory Performance & Caches**](07-memory-performance-and-caching.md) | cache hierarchy, cache lines, **false sharing**, MESI, NUMA, stack vs heap, allocators, GC, copy-on-write |
| 08 | [**Advanced Concurrency**](08-advanced-concurrency.md) | atomics, CAS, **ABA problem**, lock-free vs wait-free, memory barriers, `volatile`, RW locks, thread pools |
| 09 | [**Virtualisation & Security**](09-virtualisation-and-security.md) | hypervisors, **namespaces + cgroups**, image layers, DAC/MAC/RBAC, ASLR, RTOS |

## The questions that come up most

1. **Process vs thread** — recite the shared/private table
2. **Deadlock** — four Coffman conditions, and which strategy breaks which
3. **Producer–consumer** — from memory, semaphores in the right order
4. **Page replacement** — count faults for FIFO / LRU / Optimal
5. **Paging arithmetic** — offset bits, page table size, effective access time
6. **Containers vs VMs** — namespaces and cgroups by name
7. **SIGTERM vs SIGKILL** — and why Kubernetes sends both

## Connections to the rest of the prep

| OS concept | Where it reappears |
|---|---|
| LRU page replacement | [LRU Cache pattern](../../patterns/design/lru-lfu-cache.md) · LeetCode 146 |
| Stack depth | [Tree DFS](../../patterns/recursion-trees/tree-dfs.md) — why deep recursion overflows |
| Cache lines / locality | why an array scan beats a tree lookup at small n |
| `fsync` + WAL | [DBMS: durability](../dbms/02-transactions-and-concurrency.md) |
| Deadlock + lock ordering | [DBMS: 2PL](../dbms/02-transactions-and-concurrency.md) — same four conditions |
| epoll / C10K | [System Design](../system-design/) — how one server holds 100k connections |
| SIGTERM vs SIGKILL | [System Design](../system-design/08-reliability-and-observability.md) — graceful shutdown |
| GC pauses | [System Design](../system-design/08-reliability-and-observability.md) — p99 latency spikes |
| CAS / optimistic concurrency | [Coordination](../system-design/07-coordination-and-consistency.md) — the alternative to distributed locks |
| Containers | [System Design: scaling](../system-design/03-scaling.md) |
