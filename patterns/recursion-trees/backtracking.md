# Backtracking

`Week 16` · Recursion & Trees

## Recognise it when

- *"**ALL** possible / every combination / generate all / enumerate"*
- The output is a **list of lists**

## The insight

You are walking a **decision tree**. At each node you make a choice, recurse, then **undo it** so the next branch starts clean.

The undo is what lets one shared `path` array serve the entire tree instead of copying at every level.

## Diagram

```
  subsets of [1, 2, 3]        at each element: take it, or skip it

                          []
                 ┌────────┴────────┐
             take 1              skip 1
                │                   │
               [1]                 []
           ┌────┴────┐         ┌────┴────┐
        take2     skip2     take2      skip2
          │          │         │          │
        [1,2]       [1]       [2]        []
       ┌──┴──┐    ┌──┴──┐   ┌──┴──┐    ┌──┴──┐
     [1,2,3][1,2][1,3] [1] [2,3] [2]  [3]   []

  8 leaves = 2^3 subsets

  The path array over time:
      []  →  [1]  →  [1,2]  →  [1,2,3]  →  [1,2]  →  [1]  →  [1,3]  → ...
                                        ▲ pop        ▲ pop
                                   this is the "unchoose"
```

## Template

```python
def backtrack(start: int, path: list) -> None:
    if is_goal(path):
        res.append(path[:])          # COPY - not the reference
        return
    for i in range(start, n):
        if skip(i):
            continue                 # pruning / duplicate handling
        path.append(choices[i])      # CHOOSE
        backtrack(i + 1, path)       # EXPLORE   (i+1 = use once, i = reuse)
        path.pop()                   # UNCHOOSE
```

### Three dials that cover most problems

| Dial | Effect |
|---|---|
| `backtrack(i + 1, ...)` | each element used **once** (combinations) |
| `backtrack(i, ...)` | element may be **reused** (combination sum) |
| `used[]` boolean array | order matters (**permutations**) |

### Handling duplicates

```python
nums.sort()                                    # sort FIRST
...
for i in range(start, n):
    if i > start and nums[i] == nums[i - 1]:
        continue          # skip a duplicate at the SAME tree level
```

```
  [1, 2, 2]     without the guard:      with the guard:
                  [1,2] appears twice     [1,2] appears once
                  ▲  ▲
              from 2a and 2b - identical subsets
```

### Permutations

```python
def permute(nums: list[int]) -> list[list[int]]:
    res, path = [], []
    used = [False] * len(nums)

    def bt():
        if len(path) == len(nums):
            res.append(path[:])
            return
        for i, x in enumerate(nums):
            if used[i]:
                continue
            used[i] = True;  path.append(x)
            bt()
            path.pop();      used[i] = False
    bt()
    return res
```

### N-Queens — track attacks with sets

```python
def solve_n_queens(n: int) -> list[list[str]]:
    res, cols, diag, anti = [], set(), set(), set()
    board = [["."] * n for _ in range(n)]

    def bt(r: int):
        if r == n:
            res.append(["".join(row) for row in board]); return
        for c in range(n):
            if c in cols or (r - c) in diag or (r + c) in anti:
                continue
            cols.add(c); diag.add(r - c); anti.add(r + c); board[r][c] = "Q"
            bt(r + 1)
            cols.remove(c); diag.remove(r - c); anti.remove(r + c); board[r][c] = "."
    bt(0)
    return res
```

```
  diagonal identity:  r - c is constant along a ╲ diagonal
                      r + c is constant along a ╱ diagonal

       c=0 c=1 c=2          r-c:  0  -1  -2
  r=0   .   .   .                 1   0  -1
  r=1   .   .   .                 2   1   0
  r=2   .   .   .
```

## Complexity

| | |
|---|---|
| Subsets | O(2ⁿ · n) |
| Permutations | O(n! · n) |
| Combinations | O(C(n,k) · k) |

The `· n` is the cost of copying each result.

## Common mistakes

- **`res.append(path)` instead of `path[:]`** — every result ends up empty
- Forgetting to undo *all* the state you changed (board, sets, visited)
- Duplicate guard using `i > 0` instead of `i > start` — that wrongly skips across levels

## Problems

- [78. Subsets](https://leetcode.com/problems/subsets/) — Medium
- [46. Permutations](https://leetcode.com/problems/permutations/) — Medium
- [39. Combination Sum](https://leetcode.com/problems/combination-sum/) — Medium
