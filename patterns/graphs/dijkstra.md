# Dijkstra's Algorithm

`Week 23` · Graphs

## Recognise it when

- **Shortest path** with **weighted, non-negative** edges

## The insight

BFS works on unweighted graphs because every edge costs 1, so "fewest edges" = "cheapest".

With weights that breaks. So you swap the queue for a **priority queue ordered by total cost**. Popping the cheapest unfinalised node guarantees its distance is final — nothing cheaper can reach it later, because all edges are non-negative.

**That non-negativity assumption is the whole proof.** Negative edges break it → use Bellman-Ford.

## Diagram

```
        A ──4── B
        │       │
        1       2
        │       │
        C ──5── D

  shortest A → D

  heap (cost, node)          dist
  ────────────────────       ──────────────────
  [(0,A)]                    A:0
  pop (0,A)   push (4,B) (1,C)
  [(1,C), (4,B)]             A:0  C:1
  pop (1,C)   push (6,D)   ← via C: 1 + 5 = 6
  [(4,B), (6,D)]             A:0  C:1  D:6
  pop (4,B)   push (6,D)   ← via B: 4 + 2 = 6  (equal, no improvement)
  [(6,D), (6,D)]             ← duplicate entries are FINE
  pop (6,D)   → D finalised at 6

  ╔═══════════════════════════════════════════════════════╗
  ║ Duplicates in the heap are normal. Skip a popped node ║
  ║ whose recorded distance is already better:            ║
  ║     if d > dist[u]: continue                          ║
  ║ This is "lazy deletion" - far simpler than decrease-key║
  ╚═══════════════════════════════════════════════════════╝
```

## Template

```python
import heapq

def dijkstra(n: int, adj: list[list[tuple[int, int]]], src: int) -> list[float]:
    dist = [float('inf')] * n
    dist[src] = 0
    h = [(0, src)]
    while h:
        d, u = heapq.heappop(h)
        if d > dist[u]:
            continue                       # stale entry - skip
        for v, w in adj[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(h, (nd, v))
    return dist
```

### Network delay time

```python
def network_delay_time(times: list[list[int]], n: int, k: int) -> int:
    adj = [[] for _ in range(n + 1)]
    for u, v, w in times:
        adj[u].append((v, w))
    dist = dijkstra(n + 1, adj, k)
    out = max(dist[1:])
    return -1 if out == float('inf') else out
```

### Path with minimum EFFORT — cost is the max edge, not the sum

```python
def minimum_effort_path(heights: list[list[int]]) -> int:
    R, C = len(heights), len(heights[0])
    effort = [[float('inf')] * C for _ in range(R)]
    effort[0][0] = 0
    h = [(0, 0, 0)]
    while h:
        e, r, c = heapq.heappop(h)
        if (r, c) == (R - 1, C - 1):
            return e
        if e > effort[r][c]:
            continue
        for dr, dc in ((1,0), (-1,0), (0,1), (0,-1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C:
                ne = max(e, abs(heights[nr][nc] - heights[r][c]))   # MAX not sum
                if ne < effort[nr][nc]:
                    effort[nr][nc] = ne
                    heapq.heappush(h, (ne, nr, nc))
    return 0
```

### When Dijkstra is WRONG: "at most K stops"

Cheapest-first can finalise a node via a path with too many stops. Use Bellman-Ford, relaxing exactly `k+1` times:

```python
def find_cheapest_price(n, flights, src, dst, k) -> int:
    dist = [float('inf')] * n
    dist[src] = 0
    for _ in range(k + 1):
        snapshot = dist[:]                 # snapshot - critical
        for u, v, w in flights:
            if snapshot[u] + w < dist[v]:
                dist[v] = snapshot[u] + w
    return -1 if dist[dst] == float('inf') else dist[dst]
```

The snapshot prevents using an edge relaxed in the *same* round, which would exceed the stop limit.

## Complexity

O(E log V) with a binary heap. O(V) space.

| Situation | Algorithm |
|---|---|
| Unweighted | BFS — O(V+E) |
| Weights 0 or 1 | 0-1 BFS with a deque |
| Non-negative weights | **Dijkstra** |
| Negative edges | Bellman-Ford — O(V·E) |
| All pairs | Floyd-Warshall — O(V³) |

## Common mistakes

- Using it with **negative weights**
- Trying to implement decrease-key instead of lazy deletion
- Using plain Dijkstra on "at most K stops"

## Problems

- [743. Network Delay Time](https://leetcode.com/problems/network-delay-time/) — Medium
- [1631. Path With Minimum Effort](https://leetcode.com/problems/path-with-minimum-effort/) — Medium
- [787. Cheapest Flights Within K Stops](https://leetcode.com/problems/cheapest-flights-within-k-stops/) — Medium

---

## All problems in this pattern

**Shortest Path** — 7 problems (4 core). Full list with dates and checkboxes: [`solutions/27-shortest-path/`](../../solutions/27-shortest-path/)

| # | Problem | Diff | Tier |
|---|---|---|---|
| 399 | [Evaluate Division](https://leetcode.com/problems/evaluate-division/) | Medium | **Core** |
| 743 | [Network Delay Time](https://leetcode.com/problems/network-delay-time/) | Medium | **Core** |
| 778 | [Swim In Rising Water](https://leetcode.com/problems/swim-in-rising-water/) | Hard | _opt_ |
| 787 | [Cheapest Flights Within K Stops](https://leetcode.com/problems/cheapest-flights-within-k-stops/) | Medium | **Core** |
| 1514 | [Path With Maximum Probability](https://leetcode.com/problems/path-with-maximum-probability/) | Medium | _opt_ |
| 1631 | [Path With Minimum Effort](https://leetcode.com/problems/path-with-minimum-effort/) | Medium | **Core** |
| 1976 | [Number Of Ways To Arrive At Destination](https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/) | Medium | _opt_ |
