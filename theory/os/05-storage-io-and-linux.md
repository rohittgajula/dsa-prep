# Storage, I/O & Linux in Practice

`Week 5` · Operating Systems

## File systems and inodes

```mermaid
graph TB
    D["Directory<br/>(just a file mapping<br/>names → inode numbers)"] --> I["inode<br/>size, permissions, timestamps,<br/>link count, block pointers"]
    I --> B1[direct blocks ×12]
    I --> B2[single indirect]
    I --> B3[double indirect]
    I --> B4[triple indirect]
    B2 --> P1[block of pointers]
    B3 --> P2[block of pointers to<br/>blocks of pointers]
```

Small files use only direct pointers and stay cheap; huge files reach through the indirect levels.

### Hard link vs soft link

```
  HARD LINK — a second NAME for the same inode

    /a/file ──┐
              ├──► inode 42  (link count = 2)   data blocks
    /b/link ──┘

    delete /a/file → link count 1, data SURVIVES

  SOFT LINK (symlink) — a file containing a PATH

    /b/link ──► inode 99 ──► contents: "/a/file"
                                          │
                                          ▼
                             delete /a/file → link is BROKEN
```

Asked constantly. Hard links share the inode; soft links store a path.

## Disk scheduling

```
  requests: 98, 183, 37, 122, 14, 124, 65, 67     head at 53

  FCFS   : 53→98→183→37→122→14→124→65→67    total movement 640
  SSTF   : 53→65→67→37→14→98→122→124→183    total movement 236
  SCAN   : sweep one way, then reverse (elevator)
  C-SCAN : sweep one way, jump back to 0, sweep again
           → more UNIFORM waiting time
```

> **Say this:** disk scheduling is largely **irrelevant for SSDs** — there is no seek time. It shows current knowledge rather than recited textbook.

## RAID

```
  RAID 0  striping          A1 A2 | A3 A4        speed, ZERO redundancy
  RAID 1  mirroring         A1 A1 | A2 A2        survives 1 loss, 50% capacity
  RAID 5  striping+parity   A1 A2 Ap | B1 Bp B2  survives 1, write penalty
  RAID 6  double parity                          survives 2
  RAID 10 mirrored stripes                       speed + redundancy, 50%
```

**RAID IS NOT A BACKUP.** It protects against *disk failure*, not deletion, corruption or ransomware. Say it unprompted.

## Blocking vs non-blocking I/O — the C10K problem

```mermaid
graph TB
    subgraph NB["epoll / kqueue — O(ready)"]
        E[single thread] -->|kernel returns ONLY<br/>ready descriptors| R[handle them]
    end
    subgraph SP["select / poll — O(watched)"]
        S[scans ALL watched fds<br/>on EVERY call] --> S2[does not scale]
    end
    subgraph BL["blocking — one thread per connection"]
        T["1000 conns = 1000 threads<br/>× 1-8 MB stack each"]
    end
```

| | Cost per call |
|---|---|
| `select` / `poll` | **O(watched)** — rescans everything; `select` caps at 1024 fds |
| `epoll` / `kqueue` | **O(ready)** — register once, get back only what fired |
| `io_uring` | shared submission/completion rings, fewer syscalls still |

> *"epoll is O(ready) while select is O(watched)"* — one sentence that answers **"how does nginx handle 100k connections?"**

## Page cache and durability — `write()` is NOT durable

```mermaid
sequenceDiagram
    participant A as Application
    participant PC as Page Cache (RAM)
    participant D as Disk
    A->>PC: write() — copies into RAM
    PC-->>A: returns SUCCESS immediately
    Note over A,D: data is in RAM only.<br/>POWER LOSS HERE = DATA LOST
    PC->>D: kernel flushes later (seconds)
    A->>PC: fsync()
    PC->>D: forced flush
    D-->>A: only NOW is it durable
```

**This is the D in ACID.** It explains why `fsync` is the bottleneck in every database, and why databases batch commits (group commit) to amortise its cost.

Excellent bridge between OS and DBMS — make it explicitly.

## VMs vs containers

```mermaid
graph TB
    subgraph C["CONTAINERS"]
        CH[Host OS Kernel — SHARED] --> C1[Container A<br/>namespaces + cgroups]
        CH --> C2[Container B]
        CH --> C3[Container C]
    end
    subgraph V["VIRTUAL MACHINES"]
        HV[Hypervisor] --> V1[Guest OS + kernel]
        HV --> V2[Guest OS + kernel]
    end
```

| | VM | Container |
|---|---|---|
| Isolation | **hardware-level, strong** | kernel-level, weaker |
| Boot | minutes | **milliseconds** |
| Overhead | full guest OS each | negligible |
| Different OS? | ✅ | ❌ shares the host kernel |

Containers are **namespaces** (separate views of PIDs, network, mounts, users) plus **cgroups** (CPU/memory/IO limits). Naming those two specifically is what separates a real answer from a hand-wave.

**Security:** a kernel exploit escapes the container. That matters for untrusted multi-tenant code.

## Diagnosing a slow Linux box

```mermaid
graph LR
    A[Server is slow] --> B{Which resource?}
    B -->|CPU| C["top / htop<br/>user vs sys vs iowait"]
    B -->|Memory| D["free -h / dmesg<br/>check the OOM killer"]
    B -->|Disk| E["iostat / df -h<br/>high iowait?"]
    B -->|Network| F["ss -tulpn"]
    C --> G["per-process: strace, lsof, /proc/PID/"]
    D --> G
    E --> G
    F --> G
```

**Two facts that instantly signal real experience:**

1. **Linux load average includes processes blocked on I/O**, not just CPU. High load + low CPU = **I/O bound**, which surprises people.
2. **Low "free" memory is normal.** The kernel uses spare RAM as page cache. Look at **available**, not free.

## Interview checklist

- [ ] Hard vs soft link
- [ ] Compute total head movement for FCFS / SSTF / SCAN
- [ ] RAID levels — and that RAID is not a backup
- [ ] epoll vs select, and the C10K problem
- [ ] Why `write()` returning success is not durability
- [ ] VMs vs containers — namespaces and cgroups by name
- [ ] "The server is slow" — walk the four resources in order
