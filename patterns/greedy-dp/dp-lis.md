# DP — Longest Increasing Subsequence

`Week 26` · Greedy & DP

## Recognise it when

- *"Longest increasing subsequence"*, *"chain"*, *"russian doll envelopes"*, *"string chain"*

## The insight

**O(n²):** for each `i`, look back at every `j < i` and extend the best compatible one.

**O(n log n):** maintain `tails`, where `tails[k]` is the **smallest possible tail** of an increasing subsequence of length `k+1`. Keeping tails small maximises future extension room.

## Diagram

```
  nums = [10, 9, 2, 5, 3, 7, 101, 18]

  tails evolves (binary search for the insert position each time):

  10   → tails [10]                    length 1
   9   → replace 10  → [9]             a smaller tail is strictly better
   2   → replace 9   → [2]
   5   → append      → [2, 5]          length 2
   3   → replace 5   → [2, 3]          length still 2, but tail is smaller
   7   → append      → [2, 3, 7]       length 3
  101  → append      → [2, 3, 7, 101]  length 4
  18   → replace 101 → [2, 3, 7, 18]   length still 4

  answer = len(tails) = 4

  ╔══════════════════════════════════════════════════════════╗
  ║ tails is NOT an actual subsequence.                      ║
  ║ [2,3,7,18] is - by luck - but in general only its LENGTH ║
  ║ is meaningful. Never return tails itself.                ║
  ╚══════════════════════════════════════════════════════════╝
```

### Why replacing helps

```
  [2, 5]  vs  [2, 3]      both length 2

  Next value is 4:
      [2, 5] → 4 < 5, cannot extend
      [2, 3] → 4 > 3, extends to [2, 3, 4]   length 3  ✓

  A smaller tail is never worse. That is the greedy invariant.
```

## Template — O(n log n)

```python
from bisect import bisect_left

def length_of_lis(nums: list[int]) -> int:
    tails = []
    for x in nums:
        i = bisect_left(tails, x)       # first index with tails[i] >= x
        if i == len(tails):
            tails.append(x)             # x extends the longest run
        else:
            tails[i] = x                # x becomes a smaller tail
    return len(tails)
```

| Variant | Function |
|---|---|
| Strictly increasing | `bisect_left` |
| Non-decreasing (allows equals) | `bisect_right` |

## Template — O(n²), needed when you must reconstruct

```python
def lis_quadratic(nums: list[int]) -> int:
    n = len(nums)
    dp = [1] * n                        # every element alone is length 1
    for i in range(1, n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp) if dp else 0
```

### Russian Doll Envelopes — the sort trick

```python
def max_envelopes(envelopes: list[list[int]]) -> int:
    envelopes.sort(key=lambda e: (e[0], -e[1]))   # width ASC, height DESC
    return length_of_lis([h for _, h in envelopes])
```

```
  Why height DESCENDING for equal widths?

  [[3,4], [3,5]]  sorted height ASC → heights [4, 5] → LIS = 2  ✗
                  but two envelopes of width 3 CANNOT nest!

  sorted height DESC → heights [5, 4] → LIS = 1  ✓
  The descending order makes equal widths mutually non-extendable.
```

### Number of LIS — track length AND count

```python
def find_number_of_lis(nums: list[int]) -> int:
    n = len(nums)
    length = [1] * n
    count = [1] * n
    for i in range(n):
        for j in range(i):
            if nums[j] < nums[i]:
                if length[j] + 1 > length[i]:
                    length[i] = length[j] + 1
                    count[i] = count[j]          # new best - inherit the count
                elif length[j] + 1 == length[i]:
                    count[i] += count[j]         # tie - accumulate
    best = max(length)
    return sum(c for l, c in zip(length, count) if l == best)
```

## Complexity

| | Time | Reconstruct? |
|---|---|---|
| Patience / tails | **O(n log n)** | hard |
| Classic DP | O(n²) | easy |

## Common mistakes

- **Returning `tails`** as the subsequence
- `bisect_left` vs `bisect_right` for strict vs non-strict
- Sorting envelope heights ascending

## Problems

- [300. Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/) — Medium
- [354. Russian Doll Envelopes](https://leetcode.com/problems/russian-doll-envelopes/) — Hard
- [1048. Longest String Chain](https://leetcode.com/problems/longest-string-chain/) — Medium

---

## All problems in this pattern

**DP LIS** — 5 problems (2 core). Full list with dates and checkboxes: [`solutions/35-dp-lis/`](../../solutions/35-dp-lis/)

| # | Problem | Diff | Tier |
|---|---|---|---|
| 300 | [Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/) | Medium | **Core** |
| 354 | [Russian Doll Envelopes](https://leetcode.com/problems/russian-doll-envelopes/) | Hard | _opt_ |
| 646 | [Maximum Length Of Pair Chain](https://leetcode.com/problems/maximum-length-of-pair-chain/) | Medium | _opt_ |
| 673 | [Number Of Longest Increasing Subsequence](https://leetcode.com/problems/number-of-longest-increasing-subsequence/) | Medium | **Core** |
| 1048 | [Longest String Chain](https://leetcode.com/problems/longest-string-chain/) | Medium | _opt_ |
