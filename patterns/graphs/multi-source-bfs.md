# Multi-Source BFS

`Week 21` · Graphs

## Recognise it when

- **Several starting points** spreading **simultaneously**
- *"Rotting oranges"*, *"distance to nearest 0"*, *"nearest exit"*, *"walls and gates"*

## The insight

Running BFS from each source separately is O(sources × V).

Instead, **seed the queue with ALL sources at distance 0**. The wavefronts expand together, so every cell is naturally reached first by its **nearest** source — one BFS, same cost as a single-source run.

## Diagram

```
  01-matrix: distance from every cell to the nearest 0

  input           ALL zeros seeded at once
  ┌───┬───┬───┐   ┌───┬───┬───┐
  │ 0 │ 0 │ 0 │   │ 0 │ 0 │ 0 │  ← queue = [(0,0),(0,1),(0,2),(1,0)]
  ├───┼───┼───┤   ├───┼───┼───┤     all at distance 0
  │ 0 │ 1 │ 1 │   │ 0 │ ? │ ? │
  ├───┼───┼───┤   ├───┼───┼───┤
  │ 1 │ 1 │ 1 │   │ ? │ ? │ ? │
  └───┴───┴───┘   └───┴───┴───┘

  wave 1 (distance 1)     wave 2 (distance 2)
  ┌───┬───┬───┐           ┌───┬───┬───┐
  │ 0 │ 0 │ 0 │           │ 0 │ 0 │ 0 │
  ├───┼───┼───┤           ├───┼───┼───┤
  │ 0 │ 1 │ 1 │           │ 0 │ 1 │ 1 │
  ├───┼───┼───┤           ├───┼───┼───┤
  │ 1 │ ? │ ? │           │ 1 │ 2 │ 2 │
  └───┴───┴───┘           └───┴───┴───┘

  Each cell gets the distance to its NEAREST zero for free,
  because the nearest wavefront simply arrives first.
```

**All sources must be queued BEFORE the loop starts.** Adding them during the loop breaks the distance ordering.

## Template

```python
from collections import deque

def multi_source_bfs(grid) -> list[list[int]]:
    R, C = len(grid), len(grid[0])
    dist = [[-1] * C for _ in range(R)]
    q = deque()

    for r in range(R):                       # seed EVERY source first
        for c in range(C):
            if grid[r][c] == 0:
                dist[r][c] = 0
                q.append((r, c))

    while q:
        r, c = q.popleft()
        for dr, dc in ((1,0), (-1,0), (0,1), (0,-1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C and dist[nr][nc] == -1:
                dist[nr][nc] = dist[r][c] + 1
                q.append((nr, nc))
    return dist
```

### Rotting oranges — count the time steps

```python
def oranges_rotting(grid: list[list[int]]) -> int:
    R, C = len(grid), len(grid[0])
    q, fresh = deque(), 0
    for r in range(R):
        for c in range(C):
            if grid[r][c] == 2: q.append((r, c))
            elif grid[r][c] == 1: fresh += 1

    if fresh == 0:
        return 0                      # nothing to rot

    minutes = 0
    while q and fresh:
        for _ in range(len(q)):       # one level = one minute
            r, c = q.popleft()
            for dr, dc in ((1,0), (-1,0), (0,1), (0,-1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh -= 1
                    q.append((nr, nc))
        minutes += 1

    return -1 if fresh else minutes   # unreachable fresh oranges → -1
```

> The `if fresh` in the loop condition stops you counting one extra minute after the last orange rots.

## Complexity

O(V + E) — identical to single-source BFS, regardless of how many sources there are.

## Common mistakes

- Seeding sources **inside** the loop instead of before it
- Off-by-one on the minute count (the level loop runs once more than needed unless you guard it)
- Forgetting the unreachable case (`return -1`)

## Problems

- [994. Rotting Oranges](https://leetcode.com/problems/rotting-oranges/) — Medium
- [542. 01 Matrix](https://leetcode.com/problems/01-matrix/) — Medium
- [1926. Nearest Exit from Entrance in Maze](https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/) — Medium
