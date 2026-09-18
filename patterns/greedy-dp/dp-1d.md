# DP — 1D Linear

`Week 24` · Greedy & DP

## Recognise it when

- *"Number of ways"* or *"min / max"*
- `dp[i]` depends on a **fixed few** previous entries

This is the gateway DP pattern. Get comfortable here before anything else.

## The insight

Define `dp[i]` as the answer for the first `i` elements, then find the **recurrence** — how `dp[i]` is built from earlier values.

**Write the recurrence in words before you write code.** That is 90% of DP.

## Diagram

```
  House Robber: nums = [2, 7, 9, 3, 1]
  Cannot rob two adjacent houses.

  At house i there are exactly TWO options:

      SKIP i        →  dp[i-1]                (best without this house)
      ROB  i        →  dp[i-2] + nums[i]      (must skip i-1)

      dp[i] = max(dp[i-1], dp[i-2] + nums[i])

  i      │  -   0    1    2    3    4
  nums   │  -   2    7    9    3    1
  ───────┼───────────────────────────────
  dp[i]  │  0   2    7   11   11   12
                │    │    │    │    │
                │    │    │    │    └─ max(11, 11+1) = 12  ★
                │    │    │    └────── max(11, 7+3)  = 11
                │    │    └─────────── max(7,  2+9)  = 11
                │    └──────────────── max(2,  0+7)  = 7
                └───────────────────── base case

  answer = 12   (rob houses 0, 2, 4 → 2 + 9 + 1 = 12)
```

### Space optimisation — you only ever look back 2

```
  dp[i] = f(dp[i-1], dp[i-2])

  → keep TWO variables, not an array

  prev2   prev1   cur
    0       2      7      slide right each iteration
            └──────┘
          prev2, prev1 = prev1, cur
```

## Template

```python
def dp_1d(nums: list[int]) -> int:
    n = len(nums)
    dp = [0] * (n + 1)
    dp[0] = base_0
    dp[1] = base_1
    for i in range(2, n + 1):
        dp[i] = combine(dp[i - 1], dp[i - 2], nums[i - 1])
    return dp[n]
```

### House Robber — space optimised

```python
def rob(nums: list[int]) -> int:
    prev2 = prev1 = 0
    for x in nums:
        prev2, prev1 = prev1, max(prev1, prev2 + x)
    return prev1
```

### House Robber II — circular, so run it twice

```python
def rob_circular(nums: list[int]) -> int:
    if len(nums) == 1:
        return nums[0]
    def line(a):
        p2 = p1 = 0
        for x in a:
            p2, p1 = p1, max(p1, p2 + x)
        return p1
    return max(line(nums[:-1]), line(nums[1:]))   # exclude last, or exclude first
```

### Decode Ways — the zero cases are where marks are lost

```python
def num_decodings(s: str) -> int:
    if not s or s[0] == "0":
        return 0
    prev2, prev1 = 1, 1                # dp[0]=1 (empty), dp[1]=1
    for i in range(1, len(s)):
        cur = 0
        if s[i] != "0":                    # single digit 1-9
            cur += prev1
        two = int(s[i-1:i+1])
        if 10 <= two <= 26:                # valid two-digit
            cur += prev2
        if cur == 0:
            return 0                       # e.g. "30" - unreachable
        prev2, prev1 = prev1, cur
    return prev1
```

### Word Break — dp over prefixes

```python
def word_break(s: str, word_dict: list[str]) -> bool:
    words = set(word_dict)                 # set, not list - O(1) lookup
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True                           # empty string is breakable
    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in words:
                dp[i] = True
                break
    return dp[n]
```

## The three-step method

1. **Memoise a recursion** — write the brute-force recursion, add `@cache`
2. **Tabulate** — turn it into a bottom-up loop
3. **Space-optimise** — collapse the array to the few values you actually read

Never skip straight to step 3.

## Complexity

O(n) time, O(n) → **O(1)** space after optimisation.

## Common mistakes

- **Wrong base cases** — verify `dp[0]` and `dp[1]` by hand before writing the loop
- Off-by-one between the string index and the dp index (dp is 1-indexed, so use `s[i-1]`)
- Using a list instead of a set for dictionary lookups

## Problems

- [70. Climbing Stairs](https://leetcode.com/problems/climbing-stairs/) — Easy
- [198. House Robber](https://leetcode.com/problems/house-robber/) — Medium
- [91. Decode Ways](https://leetcode.com/problems/decode-ways/) — Medium
