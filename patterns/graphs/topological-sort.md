# Topological Sort

`Week 22` · Graphs

## Recognise it when

- **Dependencies**, prerequisites, ordering, build order
- The graph is **directed**

## The insight

A node is safe to output once **nothing points at it any more**.

Kahn's algorithm repeatedly emits zero-indegree nodes and removes their edges. If you cannot empty the graph, the leftover nodes form a **cycle** — so this doubles as cycle detection.

## Diagram

```
  courses: 0 → 1 → 3
            ↘   ↗
              2

  indegree:  0:0   1:1   2:1   3:2

  queue = [0]                   (only 0 has indegree 0)
  ─────────────────────────────────────────────────────
  pop 0  → output [0]
           1.indeg 1→0  → queue [1]
           2.indeg 1→0  → queue [1,2]

  pop 1  → output [0,1]
           3.indeg 2→1

  pop 2  → output [0,1,2]
           3.indeg 1→0  → queue [3]

  pop 3  → output [0,1,2,3]     length 4 == n  ✓ no cycle
```

### Cycle detection falls out for free

```
  1 → 2
  ↑   ↓
  4 ← 3        every node has indegree 1 → the queue starts EMPTY

  output length 0 < 4  →  CYCLE EXISTS
```

## Template

```python
from collections import deque

def topo_sort(n: int, edges: list[list[int]]) -> list[int]:
    adj = [[] for _ in range(n)]
    indeg = [0] * n
    for u, v in edges:                 # u must come BEFORE v
        adj[u].append(v)
        indeg[v] += 1

    q = deque(i for i in range(n) if indeg[i] == 0)
    order = []
    while q:
        u = q.popleft()
        order.append(u)
        for v in adj[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)

    return order if len(order) == n else []   # [] means a cycle
```

### Course Schedule — just the boolean

```python
def can_finish(num_courses: int, prerequisites: list[list[int]]) -> bool:
    return len(topo_sort(num_courses, [[p, c] for c, p in prerequisites])) == num_courses
```

> Watch the edge direction. LeetCode gives `[course, prereq]`, meaning **prereq → course**. Reversing it silently gives the wrong answer on asymmetric graphs.

### DFS version — three-colour marking

```python
WHITE, GREY, BLACK = 0, 1, 2

def topo_dfs(n: int, adj: list[list[int]]) -> list[int] | None:
    colour = [WHITE] * n
    order = []

    def dfs(u: int) -> bool:
        colour[u] = GREY                    # currently on the stack
        for v in adj[u]:
            if colour[v] == GREY:
                return False                # back edge → CYCLE
            if colour[v] == WHITE and not dfs(v):
                return False
        colour[u] = BLACK
        order.append(u)                     # post-order
        return True

    for i in range(n):
        if colour[i] == WHITE and not dfs(i):
            return None
    return order[::-1]                      # reverse the post-order
```

```
  GREY  = in the current recursion stack  → meeting one means a cycle
  BLACK = fully explored, safe
  WHITE = untouched
```

## Complexity

O(V + E) time, O(V) space.

## Common mistakes

- **Forgetting the cycle check** (`len(order) == n`) — it is the entire answer to "can you finish all courses"
- Reversing the edge direction
- Applying it to an **undirected** graph — use union-find there instead

## Problems

- [207. Course Schedule](https://leetcode.com/problems/course-schedule/) — Medium
- [210. Course Schedule II](https://leetcode.com/problems/course-schedule-ii/) — Medium
- [802. Find Eventual Safe States](https://leetcode.com/problems/find-eventual-safe-states/) — Medium
