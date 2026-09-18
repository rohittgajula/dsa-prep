# Quickselect

`Week 9` · Search & Sort

## Recognise it when

- **Kth largest / smallest** and you do **not** need the array fully sorted

## The insight

Quicksort recurses into **both** halves. Quickselect knows the answer lies in **only one** — so it discards the other entirely.

The work halves each round: `n + n/2 + n/4 + ... = 2n` → **O(n) average** instead of O(n log n).

## Diagram

```
  find the 2nd largest (k=1 in 0-indexed descending) of [7, 2, 9, 4, 1]

  partition around a random pivot, say 4:
      [2, 1] │ 4 │ [7, 9]
       <4         >4
                p=2 (final index of the pivot)

  We want index 3 (2nd largest in a 5-element ascending array).
  3 > 2  → recurse RIGHT only, discard the left half entirely

      [7, 9]   partition around 7:
      │ 7 │ [9]
       p=3

  p == 3 == k  → answer is 7

  Work done:  5 + 2  ≈ O(n),  never O(n log n)
```

## Template

```python
import random

def quickselect(a: list[int], k: int) -> int:
    """kth smallest, 0-indexed. Modifies `a` in place."""
    lo, hi = 0, len(a) - 1
    while True:
        if lo == hi:
            return a[lo]
        p = partition(a, lo, hi)
        if p == k:
            return a[p]
        elif p < k:
            lo = p + 1        # answer is to the RIGHT
        else:
            hi = p - 1        # answer is to the LEFT


def partition(a: list[int], lo: int, hi: int) -> int:
    r = random.randint(lo, hi)            # RANDOM pivot - critical
    a[r], a[hi] = a[hi], a[r]
    pivot = a[hi]
    i = lo
    for j in range(lo, hi):
        if a[j] < pivot:
            a[i], a[j] = a[j], a[i]
            i += 1
    a[i], a[hi] = a[hi], a[i]
    return i
```

### Kth largest = (n−k)th smallest

```python
def find_kth_largest(nums: list[int], k: int) -> int:
    return quickselect(nums, len(nums) - k)
```

## Complexity

| | |
|---|---|
| Average | **O(n)** |
| Worst case | O(n²) — a sorted input with a fixed pivot |
| Space | O(1) with the iterative form |

**Alternative:** a size-k min-heap gives O(n log k) with a guaranteed bound and much simpler code. Say the trade-off out loud in an interview — for small `k`, the heap is usually the better engineering answer.

## Common mistakes

- **Fixed pivot** (always `a[hi]`) → O(n²) on sorted input. Randomise.
- Off-by-one converting *kth largest* to *kth smallest*
- Forgetting that it mutates the input array

## Problems

- [215. Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/) — Medium
- [973. K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/) — Medium
- [347. Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) — Medium

---

## All problems in this pattern

**Sorting** — 13 problems (8 core). Full list with dates and checkboxes: [`solutions/09-sorting/`](../../solutions/09-sorting/)

| # | Problem | Diff | Tier |
|---|---|---|---|
| 41 | [First Missing Positive](https://leetcode.com/problems/first-missing-positive/) | Hard | **Core** |
| 164 | [Maximum Gap](https://leetcode.com/problems/maximum-gap/) | Medium | _opt_ |
| 179 | [Largest Number](https://leetcode.com/problems/largest-number/) | Medium | **Core** |
| 215 | [Kth Largest Element In An Array](https://leetcode.com/problems/kth-largest-element-in-an-array/) | Medium | **Core** |
| 268 | [Missing Number](https://leetcode.com/problems/missing-number/) | Easy | **Core** |
| 274 | [H Index](https://leetcode.com/problems/h-index/) | Medium | _opt_ |
| 315 | [Count Of Smaller Numbers After Self](https://leetcode.com/problems/count-of-smaller-numbers-after-self/) | Hard | _opt_ |
| 442 | [Find All Duplicates In An Array](https://leetcode.com/problems/find-all-duplicates-in-an-array/) | Medium | **Core** |
| 448 | [Find All Numbers Disappeared In An Array](https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/) | Easy | **Core** |
| 493 | [Reverse Pairs](https://leetcode.com/problems/reverse-pairs/) | Hard | _opt_ |
| 912 | [Sort An Array](https://leetcode.com/problems/sort-an-array/) | Medium | **Core** |
| 973 | [K Closest Points To Origin](https://leetcode.com/problems/k-closest-points-to-origin/) | Medium | **Core** |
| 2418 | [Sort The People](https://leetcode.com/problems/sort-the-people/) | Easy | _opt_ |
