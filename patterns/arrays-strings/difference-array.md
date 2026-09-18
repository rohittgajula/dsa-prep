# Difference Array

`Week 4` · Arrays & Strings

## Recognise it when

- **Many range updates** (*"add v to everything from l to r"*), then read the array **once** at the end
- Flight bookings, car pooling, calendar/meeting counts

## The insight

The **inverse of prefix sum**. Instead of touching `r − l + 1` cells per update, mark only the two boundaries where the change starts and stops — then integrate once at the end.

Update becomes **O(1)**; you pay O(n) a single time to rebuild.

## Diagram

```
  n = 6, updates: (1,3,+5)  (2,5,+2)

  d = [0, 0, 0, 0, 0, 0, 0]          size n+1 - d[r+1] needs the slot
            ▲           ▲
  (1,3,+5): d[1] += 5 ; d[4] -= 5
  (2,5,+2): d[2] += 2 ; d[6] -= 2

  d = [0, +5, +2, 0, -5, 0, -2]

  running sum ──────────────────────────────────────►
  i      │  0    1    2    3    4    5
  d[i]   │  0   +5   +2    0   -5    0
  run    │  0    5    7    7    2    2
           ───  ───────────────  ─────────
  result = [0,   5,   7,   7,   2,   2]
                 └────────────┘
                 the +5 applies to 1..3 and stops at 4  ✓
```

## Template

```python
def apply_range_updates(n: int, updates: list[tuple[int, int, int]]) -> list[int]:
    d = [0] * (n + 1)              # n+1: d[r+1] must be addressable
    for l, r, val in updates:
        d[l] += val
        d[r + 1] -= val

    out, running = [0] * n, 0
    for i in range(n):
        running += d[i]
        out[i] = running
    return out
```

### Car pooling — capacity never exceeded

```python
def car_pooling(trips: list[list[int]], capacity: int) -> bool:
    d = [0] * 1001
    for num, start, end in trips:
        d[start] += num
        d[end] -= num              # passengers leave AT `end`, not after
    cur = 0
    for delta in d:
        cur += delta
        if cur > capacity:
            return False
    return True
```

## Complexity

| | |
|---|---|
| Per update | **O(1)** |
| Final rebuild | O(n), once |

vs the naive O(n) per update.

## Common mistakes

- Sizing the array `n` instead of `n+1` → index error on `d[r+1]`
- Only valid when **all updates come before any read**. Interleaved read/write needs a Fenwick tree or segment tree.
- Off-by-one on whether the range end is inclusive

## Problems

- [1109. Corporate Flight Bookings](https://leetcode.com/problems/corporate-flight-bookings/) — Medium
- [1094. Car Pooling](https://leetcode.com/problems/car-pooling/) — Medium
- [1893. Check if All the Integers in a Range Are Covered](https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/) — Easy

---

## All problems in this pattern

**Prefix Sum** — 14 problems (10 core). Full list with dates and checkboxes: [`solutions/04-prefix-sum/`](../../solutions/04-prefix-sum/)

| # | Problem | Diff | Tier |
|---|---|---|---|
| 238 | [Product Of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/) | Medium | **Core** |
| 303 | [Range Sum Query Immutable](https://leetcode.com/problems/range-sum-query-immutable/) | Easy | **Core** |
| 304 | [Range Sum Query 2D Immutable](https://leetcode.com/problems/range-sum-query-2d-immutable/) | Medium | **Core** |
| 523 | [Continuous Subarray Sum](https://leetcode.com/problems/continuous-subarray-sum/) | Medium | **Core** |
| 525 | [Contiguous Array](https://leetcode.com/problems/contiguous-array/) | Medium | **Core** |
| 560 | [Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/) | Medium | **Core** |
| 724 | [Find Pivot Index](https://leetcode.com/problems/find-pivot-index/) | Easy | **Core** |
| 930 | [Binary Subarrays With Sum](https://leetcode.com/problems/binary-subarrays-with-sum/) | Medium | _opt_ |
| 974 | [Subarray Sums Divisible By K](https://leetcode.com/problems/subarray-sums-divisible-by-k/) | Medium | **Core** |
| 1094 | [Car Pooling](https://leetcode.com/problems/car-pooling/) | Medium | **Core** |
| 1109 | [Corporate Flight Bookings](https://leetcode.com/problems/corporate-flight-bookings/) | Medium | _opt_ |
| 1248 | [Count Number Of Nice Subarrays](https://leetcode.com/problems/count-number-of-nice-subarrays/) | Medium | **Core** |
| 1314 | [Matrix Block Sum](https://leetcode.com/problems/matrix-block-sum/) | Medium | _opt_ |
| 1893 | [Check If All The Integers In A Range Are Covered](https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/) | Easy | _opt_ |
