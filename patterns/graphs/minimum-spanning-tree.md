# Minimum Spanning Tree

`Week 23` · Graphs

## Recognise it when

- *"Connect all nodes at minimum total cost"*
- *"Minimum cost to connect all points"*

## The insight

Both algorithms are **greedy**, and both are provably optimal:

- **Kruskal** — sort every edge by weight, greedily add any edge that does not create a cycle (union-find detects that)
- **Prim** — grow one tree, repeatedly taking the cheapest edge leaving it (heap)

## Diagram

```
  Kruskal on:        A ──1── B
                     │ ╲     │
                     4   3   2
                     │     ╲ │
                     C ──5── D

  edges sorted by weight:  (1,A,B) (2,B,D) (3,A,D) (4,A,C) (5,C,D)

  take (1,A,B)   A-B connected      ┌ A ─ B ┐        total 1
  take (2,B,D)   B-D connected      │       D        total 3
  take (3,A,D)   A and D ALREADY connected → CYCLE → skip
  take (4,A,C)   C joins            C added          total 7
  stop: 3 edges for 4 nodes  ✓      (MST always has V-1 edges)

           A ──1── B
           │       │
           4       2
           │       │
           C       D            total = 7
```

```
  Prim from A:       visited {A}      heap [(1,B), (4,C), (3,D)]
                     pop (1,B) → {A,B}, push B's edges → [(2,D), (3,D), (4,C)]
                     pop (2,D) → {A,B,D}, push D's edges → [(3,D)✗, (4,C), (5,C)]
                     pop (3,D) → already visited, SKIP
                     pop (4,C) → {A,B,D,C}  done, total = 1+2+4 = 7
```

Same tree, same cost — they just get there differently.

## Template — Kruskal (needs DSU)

```python
def kruskal(n: int, edges: list[tuple[int, int, int]]) -> int:
    """edges as (weight, u, v). Returns total MST weight."""
    edges.sort()
    dsu = DSU(n)
    total = used = 0
    for w, u, v in edges:
        if dsu.union(u, v):          # False means it would form a cycle
            total += w
            used += 1
            if used == n - 1:
                break                # MST complete
    return total if used == n - 1 else -1   # -1 = graph is disconnected
```

## Template — Prim (heap)

```python
import heapq

def prim(n: int, adj: list[list[tuple[int, int]]]) -> int:
    visited = [False] * n
    h = [(0, 0)]                     # (weight, node)
    total = count = 0
    while h and count < n:
        w, u = heapq.heappop(h)
        if visited[u]:
            continue                 # lazy deletion
        visited[u] = True
        total += w
        count += 1
        for v, wt in adj[u]:
            if not visited[v]:
                heapq.heappush(h, (wt, v))
    return total if count == n else -1
```

### Min cost to connect points (LC 1584)

The graph is **complete** — every pair of points has an edge of Manhattan distance:

```python
def min_cost_connect_points(points: list[list[int]]) -> int:
    n = len(points)
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            d = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
            edges.append((d, i, j))
    return kruskal(n, edges)
```

With n ≤ 1000 that is ~500k edges — fine. On a denser graph, Prim is the better choice.

## Kruskal vs Prim

| | Kruskal | Prim |
|---|---|---|
| Complexity | O(E log E) | O(E log V) |
| Better on | **sparse** graphs | **dense** graphs |
| Needs | union-find | heap |
| Works with | disconnected (gives a forest) | one component only |

## Common mistakes

- **An MST is not a shortest-path tree.** The MST path between two nodes may be far from their shortest path.
- Forgetting the `used == n - 1` check → silently returns a partial forest on a disconnected graph
- Attempting Kruskal without union-find (you need it for the cycle check)

## Problems

- [1584. Min Cost to Connect All Points](https://leetcode.com/problems/min-cost-to-connect-all-points/) — Medium
- [1697. Checking Existence of Edge Length Limited Paths](https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/) — Hard
- [1489. Find Critical and Pseudo-Critical Edges in MST](https://leetcode.com/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/) — Hard
