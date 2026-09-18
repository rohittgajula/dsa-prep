# DP — Grid

`Week 25` · Greedy & DP

## Recognise it when

- A 2D grid, movement restricted to right/down (or similar)
- Count paths, or minimise cost along a path

## The insight

Each cell is reachable only from a **fixed set of predecessors**, so `dp[i][j]` combines `dp[i-1][j]` and `dp[i][j-1]`.

Because you only ever read the **previous row**, the whole table collapses to a single row.

## Diagram

```
  Unique paths, 3x3 grid, moving only right or down

  Each cell = (paths from above) + (paths from the left)

      ┌───┬───┬───┐
      │ 1 │ 1 │ 1 │      top row: only one way (keep going right)
      ├───┼───┼───┤
      │ 1 │ 2 │ 3 │      dp[1][1] = 1 + 1 = 2
      ├───┼───┼───┤      dp[1][2] = 1 + 2 = 3
      │ 1 │ 3 │ 6 │      dp[2][2] = 3 + 3 = 6  ★
      └───┴───┴───┘
        ▲
      left column: only one way (keep going down)

             dp[i-1][j]
                 │
                 ▼
   dp[i][j-1] ─► dp[i][j]
```

### Maximal square — the min-of-three recurrence

```
  matrix            dp (side length of the square ENDING here)
  1 0 1 0 0         1 0 1 0 0
  1 0 1 1 1         1 0 1 1 1
  1 1 1 1 1   →     1 1 2 2 2
  1 0 0 1 0         1 0 0 3 0  ★ side 3 → area 9

  dp[i][j] = 1 + min( dp[i-1][j],     ── up
                      dp[i][j-1],     ── left
                      dp[i-1][j-1] )  ── up-left

  Why MIN: a square of side k needs ALL THREE neighbours
  to support side k-1. The weakest one is the bottleneck.

        ┌───┬───┐
        │ a │ b │      to make a 3x3 here, a, b and c must
        ├───┼───┤      each already be the corner of a 2x2
        │ c │ X │
        └───┴───┘
```

## Template

```python
def unique_paths(m: int, n: int) -> int:
    dp = [1] * n                      # top row is all 1s
    for _ in range(1, m):
        for j in range(1, n):
            dp[j] += dp[j - 1]        # dp[j] is "above", dp[j-1] is "left"
    return dp[-1]
```

### Minimum path sum

```python
def min_path_sum(grid: list[list[int]]) -> int:
    R, C = len(grid), len(grid[0])
    dp = [float('inf')] * C
    dp[0] = 0
    for r in range(R):
        dp[0] += grid[r][0]                       # first column accumulates
        for c in range(1, C):
            dp[c] = grid[r][c] + min(dp[c], dp[c - 1])
    return dp[-1]
```

### Maximal square

```python
def maximal_square(matrix: list[list[str]]) -> int:
    R, C = len(matrix), len(matrix[0])
    dp = [[0] * (C + 1) for _ in range(R + 1)]     # padded → no edge cases
    best = 0
    for r in range(1, R + 1):
        for c in range(1, C + 1):
            if matrix[r-1][c-1] == "1":
                dp[r][c] = 1 + min(dp[r-1][c], dp[r][c-1], dp[r-1][c-1])
                best = max(best, dp[r][c])
    return best * best
```

### Dungeon Game — you MUST go backwards

```
  Forward DP fails. "Maximum health at cell X" is not enough information:
  a path arriving with more health may have needed a higher STARTING health.

  Work backwards from the princess:
      dp[i][j] = minimum health needed ON ENTERING (i,j)
               = max(1, min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j])

  The max(1, ...) enforces "never drop to 0".
```

```python
def calculate_minimum_hp(dungeon: list[list[int]]) -> int:
    R, C = len(dungeon), len(dungeon[0])
    dp = [[float('inf')] * (C + 1) for _ in range(R + 1)]
    dp[R][C - 1] = dp[R - 1][C] = 1              # need 1 HP on exit
    for r in range(R - 1, -1, -1):
        for c in range(C - 1, -1, -1):
            need = min(dp[r + 1][c], dp[r][c + 1]) - dungeon[r][c]
            dp[r][c] = max(1, need)
    return dp[0][0]
```

## Complexity

O(m × n) time, O(n) space after collapsing to one row.

## Common mistakes

- Not padding the dp array, then fighting `i-1 < 0` everywhere
- Trying **forward** DP on Dungeon Game
- Forgetting `max(1, ...)` — health can never be zero or negative

## Problems

- [62. Unique Paths](https://leetcode.com/problems/unique-paths/) — Medium
- [64. Minimum Path Sum](https://leetcode.com/problems/minimum-path-sum/) — Medium
- [221. Maximal Square](https://leetcode.com/problems/maximal-square/) — Medium

---

## All problems in this pattern

**DP Grid** — 9 problems (4 core). Full list with dates and checkboxes: [`solutions/33-dp-grid/`](../../solutions/33-dp-grid/)

| # | Problem | Diff | Tier |
|---|---|---|---|
| 62 | [Unique Paths](https://leetcode.com/problems/unique-paths/) | Medium | **Core** |
| 63 | [Unique Paths Ii](https://leetcode.com/problems/unique-paths-ii/) | Medium | **Core** |
| 64 | [Minimum Path Sum](https://leetcode.com/problems/minimum-path-sum/) | Medium | **Core** |
| 120 | [Triangle](https://leetcode.com/problems/triangle/) | Medium | _opt_ |
| 174 | [Dungeon Game](https://leetcode.com/problems/dungeon-game/) | Hard | _opt_ |
| 221 | [Maximal Square](https://leetcode.com/problems/maximal-square/) | Medium | **Core** |
| 741 | [Cherry Pickup](https://leetcode.com/problems/cherry-pickup/) | Hard | _opt_ |
| 931 | [Minimum Falling Path Sum](https://leetcode.com/problems/minimum-falling-path-sum/) | Medium | _opt_ |
| 1277 | [Count Square Submatrices With All Ones](https://leetcode.com/problems/count-square-submatrices-with-all-ones/) | Medium | _opt_ |
