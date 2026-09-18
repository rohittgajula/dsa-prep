# Processes & Threads

`Weeks 1–2` · Operating Systems

## Process vs Thread — the one question that always comes

Everything follows from **one** difference: a process has its **own address space**, threads **share** one.

```mermaid
graph TB
    subgraph P2["PROCESS B — separate address space"]
        C2[Code] --- H2[Heap] --- T3[Thread 1<br/>own stack]
    end
    subgraph P1["PROCESS A — one address space"]
        C1[Code] --- H1[Heap<br/>SHARED] --- T1[Thread 1<br/>own stack]
        H1 --- T2[Thread 2<br/>own stack]
    end
    P1 -.->|IPC required:<br/>pipe, socket, shared mem| P2
```

| | Shared between threads | Private per thread |
|---|---|---|
| Code / text | ✅ | |
| Heap, globals | ✅ | |
| Open file descriptors | ✅ | |
| **Stack** | | ✅ |
| **Registers, program counter** | | ✅ |
| **Thread-local storage** | | ✅ |

**Memorise that table.** It is asked verbatim.

## Process states

```mermaid
stateDiagram-v2
    [*] --> New
    New --> Ready: admitted
    Ready --> Running: scheduler dispatch
    Running --> Ready: timer interrupt<br/>(preempted)
    Running --> Waiting: I/O or event wait
    Waiting --> Ready: I/O complete
    Running --> Terminated: exit
    Terminated --> [*]
```

The **timer interrupt** is what makes `Running → Ready` possible. Without it a process could never be forced to yield — that is why preemptive multitasking needs hardware support.

## Context switch — where the cost hides

```
  Thread switch (same process)      Process switch (different address space)
  ────────────────────────────      ────────────────────────────────────────
  save registers + PC               save registers + PC
  restore the other thread's        SWITCH PAGE TABLES
                                    FLUSH or re-tag the TLB
                                    restore the other process's

  ~1 µs                             ~1-10 µs direct cost
                                    + the caches and TLB are now COLD
                                      ← this hidden cost is usually bigger
```

> The direct cost is measurable; the **cache pollution** is what actually hurts. That is the senior answer.

## fork / exec, zombies and orphans

```mermaid
sequenceDiagram
    participant P as Parent
    participant C as Child
    P->>C: fork() — duplicates the process
    Note over P,C: returns 0 in child,<br/>child PID in parent
    C->>C: exec() — replaces the image
    Note over C: between fork and exec the child can<br/>rewire file descriptors — THIS IS HOW<br/>SHELL PIPES AND REDIRECTION WORK
    C-->>P: exit()
    P->>P: wait() — reaps the exit status
```

| State | Meaning | Whose fault |
|---|---|---|
| **Zombie** | Child finished, parent never called `wait()` | **the parent's** — leaks PID table entries |
| **Orphan** | Parent died while the child still runs | nobody's — `init` (PID 1) adopts it |

Know these cold. *"Dead but not reaped"* vs *"alive with a dead parent"*.

## IPC — ranked by speed

```mermaid
graph LR
    A[Shared Memory<br/>fastest — no kernel copy] --> B[Pipes / Message Queues<br/>one copy through the kernel]
    B --> C[Unix Domain Sockets]
    C --> D[Network Sockets<br/>slowest — but works across machines]
```

The ranking is explained by **how many times the data is copied** through the kernel. Shared memory copies zero times — but you must then do your own synchronisation.

## Concurrency models — threads vs event loop

```mermaid
graph TB
    subgraph EL["EVENT LOOP — one thread"]
        L[Loop] -->|socket ready| H1[handler]
        L -->|socket ready| H2[handler]
        L -->|socket ready| H3[handler]
    end
    subgraph TH["THREAD PER CONNECTION"]
        T1[Thread 1<br/>~1-8 MB stack]
        T2[Thread 2]
        T3[Thread 3 ...]
    end
```

- **Threads** → CPU-**bound** parallelism. Real cores, real parallel work.
- **Event loop** → I/O-**bound** concurrency. 100k idle connections cost almost nothing.

**The trap:** one blocking call stalls the *entire* event loop. A single synchronous file read or CPU-heavy loop freezes every connection. That is the classic Node.js production incident.

## Interview checklist

- [ ] Process vs thread — recite the shared/private table
- [ ] Why is a process switch more expensive than a thread switch?
- [ ] Zombie vs orphan
- [ ] Why does `fork` return twice?
- [ ] Rank the IPC mechanisms and explain *why* that order
- [ ] Threads vs event loop — and the blocking-call trap
