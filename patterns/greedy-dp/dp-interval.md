# DP — Interval

`Week 27` · Greedy & DP

## Recognise it when

- The answer for a **range** is built from smaller ranges
- *"Burst balloons"*, *"cut sticks"*, *"matrix chain"*, *"stone game"*

## The insight

**Iterate by LENGTH, not by index** — so every smaller range is already solved when you need it.

The trick in burst-balloons style problems is to think about which element is handled **LAST** in the range, not first. That is what makes the two halves independent.

## Diagram

```
  Burst Balloons: [3, 1, 5, 8]      bursting i gives  left * i * right

  ✗ Thinking "which do I burst FIRST" fails:
       after bursting, the neighbours CHANGE, so the two sides
       are no longer independent subproblems.

  ✓ Thinking "which do I burst LAST in range (i, j)":
       if k is last, then everything in (i,k) and (k,j) is already gone,
       so k's neighbours are exactly the boundaries i and j.

       dp[i][j] = max over k in (i,j) of
                     dp[i][k] + dp[k][j] + a[i]*a[k]*a[j]
                     └──┬───┘   └──┬───┘   └─────┬──────┘
                    left half   right half    bursting k last

  Pad with 1s at both ends:  [1, 3, 1, 5, 8, 1]
                              ▲              ▲
                         virtual boundaries so i-1 / j+1 always exist

  Fill order - BY LENGTH:

  len 2:  (0,2) (1,3) (2,4) (3,5)       gaps with one balloon inside
  len 3:  (0,3) (1,4) (2,5)
  len 4:  (0,4) (1,5)
  len 5:  (0,5)  ★ the answer

     ┌──────────────── len 5 ────────────────┐
     │   ┌────────── len 4 ──────────┐       │
     │   │   ┌──── len 3 ────┐       │       │
     │   │   │  ┌ len 2 ┐    │       │       │
     1   3   1  5   8   1
```

## Template

```python
def interval_dp(a: list[int]) -> int:
    n = len(a)
    dp = [[0] * n for _ in range(n)]
    for length in range(2, n + 1):              # LENGTH first - non-negotiable
        for i in range(n - length + 1):
            j = i + length - 1
            for k in range(i + 1, j):           # split / last point
                dp[i][j] = max(dp[i][j],
                               dp[i][k] + dp[k][j] + cost(a, i, k, j))
    return dp[0][n - 1]
```

### Burst Balloons

```python
def max_coins(nums: list[int]) -> int:
    a = [1] + nums + [1]                        # virtual boundaries
    n = len(a)
    dp = [[0] * n for _ in range(n)]
    for length in range(2, n):
        for i in range(n - length):
            j = i + length
            for k in range(i + 1, j):
                dp[i][j] = max(dp[i][j],
                               dp[i][k] + dp[k][j] + a[i] * a[k] * a[j])
    return dp[0][n - 1]
```

### Minimum cost to cut a stick — identical shape

```python
def min_cost(n: int, cuts: list[int]) -> int:
    pts = sorted([0] + cuts + [n])              # sentinels at both ends
    m = len(pts)
    dp = [[0] * m for _ in range(m)]
    for length in range(2, m):
        for i in range(m - length):
            j = i + length
            dp[i][j] = min(dp[i][k] + dp[k][j] for k in range(i + 1, j)) \
                       + pts[j] - pts[i]        # cost of cutting this piece
    return dp[0][m - 1]
```

### Palindrome Partitioning II — precompute, then 1D dp

```python
def min_cut(s: str) -> int:
    n = len(s)
    is_pal = [[False] * n for _ in range(n)]
    for i in range(n - 1, -1, -1):              # backwards so i+1 is ready
        for j in range(i, n):
            if s[i] == s[j] and (j - i < 2 or is_pal[i + 1][j - 1]):
                is_pal[i][j] = True

    dp = [0] * n
    for i in range(n):
        if is_pal[0][i]:
            dp[i] = 0                            # whole prefix is a palindrome
        else:
            dp[i] = min(dp[j] + 1 for j in range(i) if is_pal[j + 1][i])
    return dp[n - 1]
```

## Complexity

O(n³) time, O(n²) space — three nested loops (length, start, split).

n ≤ ~500 in practice.

## Common mistakes

- **Iterating by index instead of length** — subproblems are not ready
- Thinking "first" instead of "last" in burst balloons
- Forgetting the sentinel padding, then fighting boundary conditions

## Problems

- [312. Burst Balloons](https://leetcode.com/problems/burst-balloons/) — Hard
- [1547. Minimum Cost to Cut a Stick](https://leetcode.com/problems/minimum-cost-to-cut-a-stick/) — Hard
- [132. Palindrome Partitioning II](https://leetcode.com/problems/palindrome-partitioning-ii/) — Hard
