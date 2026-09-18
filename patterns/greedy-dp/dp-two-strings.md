# DP — Two Strings (LCS Family)

`Week 26` · Greedy & DP

## Recognise it when

- **Two strings** compared: edit distance, common subsequence, matching, delete operations

## The insight

`dp[i][j]` = the answer for the **first i characters of s1** and the **first j characters of s2**.

At each cell, either the characters **match** (extend the diagonal) or they do not (take the best of the neighbours). Every problem in this family is a variation on that one grid.

## Diagram

```
  LCS of "abcde" and "ace"

        ""  a   c   e
    ""   0  0   0   0
    a    0  1   1   1          match  → diagonal + 1
    b    0  1   1   1          no match → max(up, left)
    c    0  1   2   2
    d    0  1   2   2
    e    0  1   2   3 ★        LCS = "ace", length 3

  The three cells every recurrence reads:

        dp[i-1][j-1]   dp[i-1][j]
              ╲            │
               ╲           ▼
        dp[i][j-1] ──►  dp[i][j]

  MATCH:     dp[i][j] = dp[i-1][j-1] + 1      (consume BOTH characters)
  NO MATCH:  dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                            └─ drop s1[i]  └─ drop s2[j]
```

### Edit distance — three operations, three sources

```
  "horse" → "ros"

        ""  r   o   s
    ""   0  1   2   3
    h    1  1   2   3
    o    2  2   1   2
    r    3  2   2   2
    s    4  3   3   2
    e    5  4   4   3 ★  answer = 3

  no match → 1 + min( dp[i-1][j],     ── DELETE s1[i]
                      dp[i][j-1],     ── INSERT s2[j]
                      dp[i-1][j-1] )  ── REPLACE

  Know which cell maps to which operation - it is a standard follow-up.
```

## Template

```python
def lcs(a: str, b: str) -> int:
    m, n = len(a), len(b)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if a[i - 1] == b[j - 1]:            # 1-indexed dp, 0-indexed string
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[m][n]
```

### Edit distance

```python
def min_distance(a: str, b: str) -> int:
    m, n = len(a), len(b)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1): dp[i][0] = i          # delete everything
    for j in range(n + 1): dp[0][j] = j          # insert everything
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
    return dp[m][n]
```

### Longest palindromic SUBSEQUENCE — LCS with the reverse

```python
def longest_palindrome_subseq(s: str) -> int:
    return lcs(s, s[::-1])        # that is the whole solution
```

### Distinct subsequences — counting, so ADD instead of max

```python
def num_distinct(s: str, t: str) -> int:
    m, n = len(s), len(t)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = 1                           # one way to match the empty string
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            dp[i][j] = dp[i - 1][j]            # skip s[i]
            if s[i - 1] == t[j - 1]:
                dp[i][j] += dp[i - 1][j - 1]   # OR use it - ADD both
    return dp[m][n]
```

> **Matching problems take `max`. Counting problems take `+`.** Same grid, different combiner.

## Complexity

O(m × n) time and space. Space collapses to O(min(m, n)) with two rows, though the 2D version is easier to get right under pressure.

## Common mistakes

- **Off-by-one** — dp is 1-indexed, so the character is `s[i-1]`
- Forgetting to initialise row 0 and column 0 (match against the empty string)
- Using `max` on a counting problem

## Problems

- [1143. Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/) — Medium
- [72. Edit Distance](https://leetcode.com/problems/edit-distance/) — Medium
- [516. Longest Palindromic Subsequence](https://leetcode.com/problems/longest-palindromic-subsequence/) — Medium
