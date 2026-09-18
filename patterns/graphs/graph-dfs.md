# Graph DFS / Connected Components

`Week 21` · Graphs

## Recognise it when

- *"Number of islands / provinces / groups"*
- Flood fill, *"explore everything reachable"*

## The insight

DFS exhausts one branch fully before backtracking.

Counting components is then trivial: loop over every node, and **each time you start a fresh DFS you have found one new component**.

## Diagram

```
  grid = 1 1 0 0 0        DFS from (0,0) floods the whole
         1 1 0 0 0        top-left blob in one call
         0 0 1 0 0
         0 0 0 1 1

  ┌───┬───┬───┬───┬───┐
  │ 1 │ 1 │ . │ . │ . │   start (0,0) → mark, spread to
  ├───┼───┼───┼───┼───┤   (0,1), (1,0), (1,1) → island #1
  │ 1 │ 1 │ . │ . │ . │
  ├───┼───┼───┼───┼───┤
  │ . │ . │ 2 │ . │ . │   (2,2) unvisited → island #2
  ├───┼───┼───┼───┼───┤
  │ . │ . │ . │ 3 │ 3 │   (3,3) unvisited → island #3
  └───┴───┴───┴───┴───┘

  answer = 3
```

### Mark visited BEFORE recursing

```
  A ── B          if you mark AFTER the recursive call:
                    dfs(A) → dfs(B) → dfs(A) → dfs(B) → ...
                    infinite recursion
```

## Template

```python
def num_islands(grid: list[list[str]]) -> int:
    if not grid: return 0
    R, C = len(grid), len(grid[0])

    def dfs(r: int, c: int) -> None:
        if r < 0 or r >= R or c < 0 or c >= C or grid[r][c] != "1":
            return
        grid[r][c] = "0"                     # mark BEFORE recursing
        for dr, dc in ((1,0), (-1,0), (0,1), (0,-1)):
            dfs(r + dr, c + dc)

    count = 0
    for r in range(R):
        for c in range(C):
            if grid[r][c] == "1":
                dfs(r, c)
                count += 1                   # one fresh DFS = one component
    return count
```

### Iterative — avoids stack overflow on large grids

```python
def num_islands_iter(grid) -> int:
    R, C, count = len(grid), len(grid[0]), 0
    for r0 in range(R):
        for c0 in range(C):
            if grid[r0][c0] != "1":
                continue
            count += 1
            stack = [(r0, c0)]
            grid[r0][c0] = "0"
            while stack:
                r, c = stack.pop()
                for dr, dc in ((1,0), (-1,0), (0,1), (0,-1)):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == "1":
                        grid[nr][nc] = "0"   # mark on PUSH
                        stack.append((nr, nc))
    return count
```

> A 1000×1000 grid of all land is a 10⁶-deep recursion. Python's limit is 1000 — go iterative.

### Border-first trick (LC 130, 1020, 1254)

For *"regions NOT touching the edge"*, invert the problem:

```
  Step 1: flood from every BORDER 'O' and mark them SAFE
  Step 2: everything still 'O' is enclosed → flip it

    X X X X          X X X X
    X O O X    →     X X X X
    X X O X          X X X X
    X O X X          X O X X
      ▲                ▲
   touches the border → survives
```

## Complexity

O(V + E), or O(rows × cols) on a grid. Space O(V) for the visited set plus recursion.

## Common mistakes

- **Marking visited after the recursive call** → infinite recursion
- Recursive DFS on a large grid → `RecursionError`
- Forgetting bounds checks before indexing

## Problems

- [200. Number of Islands](https://leetcode.com/problems/number-of-islands/) — Medium
- [695. Max Area of Island](https://leetcode.com/problems/max-area-of-island/) — Medium
- [547. Number of Provinces](https://leetcode.com/problems/number-of-provinces/) — Medium
