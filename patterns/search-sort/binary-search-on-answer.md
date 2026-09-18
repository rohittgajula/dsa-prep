# Binary Search on the Answer

`Week 8` · Search & Sort

## Recognise it when

- *"**Minimum / maximum** value X **such that** \<condition\> holds"*
- **The input is NOT sorted**
- Words like *capacity*, *speed*, *days*, *threshold*, *rate*

## The insight

You are not searching the array — you are searching the **range of possible answers**.

It works whenever `feasible(x)` is **monotonic**: if `x` works then every larger `x` also works. Then finding the boundary between False and True is just binary search.

**Prove monotonicity first.** If it does not hold, binary search is simply the wrong tool.

## Diagram

```
  Koko eating bananas: piles = [3,6,7,11], h = 8 hours
  What is the MINIMUM eating speed?

  speed  │ 1    2    3    4    5    6    7    8 ...
  hours  │ 27   15   10   8    6    5    5    4
  ok?    │ F    F    F    T    T    T    T    T
                          ▲
                          └── the boundary we want

         ┌───────── FALSE ────────┬──────── TRUE ─────────┐
         1                        4                      max(piles)
                                  ▲
                          binary search finds this edge

  Monotonic? Yes - eating FASTER never takes MORE hours.
  That is the property that licenses binary search.
```

## Template

```python
def min_feasible(lo: int, hi: int, feasible) -> int:
    """Smallest x in [lo, hi] with feasible(x) == True."""
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if feasible(mid):
            hi = mid          # works - try smaller
        else:
            lo = mid + 1      # does not work - must go bigger
    return lo
```

### Koko

```python
import math

def min_eating_speed(piles: list[int], h: int) -> int:
    def hours(speed: int) -> int:
        return sum(math.ceil(p / speed) for p in piles)

    lo, hi = 1, max(piles)        # speed 1 is the slowest sensible,
    while lo < hi:                # max(piles) always finishes in len(piles) hours
        mid = (lo + hi) // 2
        if hours(mid) <= h:
            hi = mid
        else:
            lo = mid + 1
    return lo
```

### Split array largest sum — MINIMISE the maximum

```python
def split_array(nums: list[int], k: int) -> int:
    def parts_needed(cap: int) -> int:
        parts, cur = 1, 0
        for x in nums:
            if cur + x > cap:
                parts += 1
                cur = x
            else:
                cur += x
        return parts

    lo, hi = max(nums), sum(nums)   # bounds matter: lo must fit the largest element
    while lo < hi:
        mid = (lo + hi) // 2
        if parts_needed(mid) <= k:
            hi = mid
        else:
            lo = mid + 1
    return lo
```

## Choosing `lo` and `hi`

| Problem shape | `lo` | `hi` |
|---|---|---|
| Eating / rate | 1 | max(array) |
| Capacity / split | max(array) | sum(array) |
| Distance / gap | 0 or 1 | max − min |

Getting the bounds wrong is as fatal as getting the loop wrong.

## Complexity

O(n log(range)) — `log(range)` iterations, each costing an O(n) feasibility check.

## Common mistakes

- **Not verifying monotonicity.** Say it out loud: *"if speed s works, does s+1 always work?"*
- `lo = max(nums)` vs `lo = 1` — capacity problems must be able to hold the biggest single item
- Writing `feasible` with an off-by-one (e.g. starting `parts = 0` instead of 1)

## Problems

- [875. Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/) — Medium
- [1011. Capacity To Ship Packages](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/) — Medium
- [410. Split Array Largest Sum](https://leetcode.com/problems/split-array-largest-sum/) — Hard

---

## All problems in this pattern

**Binary Search on Answer** — 13 problems (8 core). Full list with dates and checkboxes: [`solutions/08-binary-search-on-answer/`](../../solutions/08-binary-search-on-answer/)

| # | Problem | Diff | Tier |
|---|---|---|---|
| 4 | [Median Of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/) | Hard | **Core** |
| 410 | [Split Array Largest Sum](https://leetcode.com/problems/split-array-largest-sum/) | Hard | **Core** |
| 668 | [Kth Smallest Number In Multiplication Table](https://leetcode.com/problems/kth-smallest-number-in-multiplication-table/) | Hard | _opt_ |
| 719 | [Find K Th Smallest Pair Distance](https://leetcode.com/problems/find-k-th-smallest-pair-distance/) | Hard | _opt_ |
| 875 | [Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/) | Medium | **Core** |
| 1011 | [Capacity To Ship Packages Within D Days](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/) | Medium | **Core** |
| 1283 | [Find The Smallest Divisor Given A Threshold](https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/) | Medium | **Core** |
| 1300 | [Sum Of Mutated Array Closest To Target](https://leetcode.com/problems/sum-of-mutated-array-closest-to-target/) | Medium | _opt_ |
| 1482 | [Minimum Number Of Days To Make M Bouquets](https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/) | Medium | **Core** |
| 1552 | [Magnetic Force Between Two Balls](https://leetcode.com/problems/magnetic-force-between-two-balls/) | Medium | **Core** |
| 1642 | [Furthest Building You Can Reach](https://leetcode.com/problems/furthest-building-you-can-reach/) | Medium | **Core** |
| 1802 | [Maximum Value At A Given Index In A Bounded Array](https://leetcode.com/problems/maximum-value-at-a-given-index-in-a-bounded-array/) | Medium | _opt_ |
| 1898 | [Maximum Number Of Removable Characters](https://leetcode.com/problems/maximum-number-of-removable-characters/) | Medium | _opt_ |
