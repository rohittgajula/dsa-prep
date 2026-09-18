# DP — Knapsack (0/1 and Unbounded)

`Week 25` · Greedy & DP

## Recognise it when

- Pick a **subset** of items to hit a target sum or capacity
- *"Can I make this amount"*, *"fewest coins"*, *"partition into equal halves"*

## The insight

For each item you have a **binary choice**: take it or skip it. `dp[c]` = the best achievable with capacity `c`.

**The iteration direction encodes reuse:**

| Direction | Meaning |
|---|---|
| Capacity **descending** | each item used **at most once** (0/1) |
| Capacity **ascending** | item may be **reused** (unbounded) |

This single line is the entire difference between the two problems. Get it backwards and you silently solve the wrong one.

## Diagram

```
  Why direction matters. items = [3], capacity 6, counting ways.

  ASCENDING (c = 3, 4, 5, 6):
      c=3:  dp[3] += dp[0]   → dp[3] = 1      "use one 3"
      c=6:  dp[6] += dp[3]   → dp[6] = 1      dp[3] ALREADY included this item
                                              → item 3 used TWICE  (unbounded ✓)

  DESCENDING (c = 6, 5, 4, 3):
      c=6:  dp[6] += dp[3]   → dp[3] is still from the PREVIOUS item round
                              → item 3 used at most ONCE  (0/1 ✓)
      c=3:  dp[3] += dp[0]   → dp[3] = 1

  ╔════════════════════════════════════════════════════════╗
  ║ Descending reads a dp[] that has not yet seen this     ║
  ║ item in this round. Ascending reads one that HAS.      ║
  ╚════════════════════════════════════════════════════════╝
```

### The 2D table it collapses from

```
  Subset sum: nums = [1, 5, 11, 5], target = 11

        c: 0  1  2  3  4  5  6  7  8  9 10 11
  ─────────────────────────────────────────────
  {}      T  F  F  F  F  F  F  F  F  F  F  F
  +1      T  T  F  F  F  F  F  F  F  F  F  F
  +5      T  T  F  F  F  T  T  F  F  F  F  F
  +11     T  T  F  F  F  T  T  F  F  F  F  T
  +5      T  T  F  F  F  T  T  F  F  F  T  T ★

  dp[11] = True → [1,5,5] sums to 11, the other half is [11]  ✓

  Each row only reads the row ABOVE → collapse to one row,
  iterating capacity DOWNWARD so you never read the current row.
```

## Template — 0/1 knapsack

```python
def can_partition(nums: list[int]) -> bool:
    total = sum(nums)
    if total % 2:
        return False                        # odd total - impossible
    target = total // 2
    dp = [False] * (target + 1)
    dp[0] = True
    for x in nums:
        for c in range(target, x - 1, -1):  # DESCENDING → each item once
            dp[c] = dp[c] or dp[c - x]
    return dp[target]
```

## Template — unbounded knapsack

```python
def coin_change(coins: list[int], amount: int) -> int:
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for coin in coins:
        for c in range(coin, amount + 1):   # ASCENDING → reuse allowed
            dp[c] = min(dp[c], dp[c - coin] + 1)
    return -1 if dp[amount] == float('inf') else dp[amount]
```

### Combinations vs permutations — the LOOP ORDER decides

```python
# COMBINATIONS: {1,2} and {2,1} count once   → coin loop OUTER
def change(amount: int, coins: list[int]) -> int:
    dp = [0] * (amount + 1); dp[0] = 1
    for coin in coins:                       # outer
        for c in range(coin, amount + 1):    # inner
            dp[c] += dp[c - coin]
    return dp[amount]

# PERMUTATIONS: {1,2} and {2,1} count twice  → target loop OUTER
def combination_sum4(nums: list[int], target: int) -> int:
    dp = [0] * (target + 1); dp[0] = 1
    for c in range(1, target + 1):           # outer
        for x in nums:                       # inner
            if x <= c:
                dp[c] += dp[c - x]
    return dp[target]
```

```
  Same recurrence, opposite loop nesting, completely different answer.
  LC 518 vs LC 377 exist purely to test this.
```

### Target Sum — reduces to subset sum

```
  Assign + or - to each number so the result is T.

  Let P = the positives, N = the negatives.
      P - N = T  and  P + N = sum
  →   P = (sum + T) / 2

  So: count subsets summing to (sum + T) / 2.
  Check parity and bounds first, or it is impossible.
```

## Complexity

O(n × capacity) time, O(capacity) space after the 1D collapse.

This is **pseudo-polynomial** — linear in the *value* of the capacity, not its bit length.

## Common mistakes

- **Iterating capacity in the wrong direction**
- Getting the loop nesting backwards for combinations vs permutations
- Forgetting the odd-total early exit in partition problems

## Problems

- [416. Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/) — Medium
- [322. Coin Change](https://leetcode.com/problems/coin-change/) — Medium
- [494. Target Sum](https://leetcode.com/problems/target-sum/) — Medium

---

## All problems in this pattern

**DP Knapsack** — 8 problems (4 core). Full list with dates and checkboxes: [`solutions/32-dp-knapsack/`](../../solutions/32-dp-knapsack/)

| # | Problem | Diff | Tier |
|---|---|---|---|
| 322 | [Coin Change](https://leetcode.com/problems/coin-change/) | Medium | **Core** |
| 377 | [Combination Sum Iv](https://leetcode.com/problems/combination-sum-iv/) | Medium | _opt_ |
| 416 | [Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/) | Medium | **Core** |
| 474 | [Ones And Zeroes](https://leetcode.com/problems/ones-and-zeroes/) | Medium | _opt_ |
| 494 | [Target Sum](https://leetcode.com/problems/target-sum/) | Medium | **Core** |
| 518 | [Coin Change Ii](https://leetcode.com/problems/coin-change-ii/) | Medium | **Core** |
| 983 | [Minimum Cost For Tickets](https://leetcode.com/problems/minimum-cost-for-tickets/) | Medium | _opt_ |
| 1049 | [Last Stone Weight Ii](https://leetcode.com/problems/last-stone-weight-ii/) | Medium | _opt_ |
