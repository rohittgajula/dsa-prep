# Top-K with a Heap

`Week 14` · Linear Structures

## Recognise it when

- *"K largest / K smallest / K most frequent / K closest"*

## The insight

You never need the whole array ordered — only the **K best**. A heap of size K discards everything else immediately: **O(n log k)** time, **O(k)** space.

**Counterintuitive but essential:** use a **MIN-heap to find the K LARGEST**. The root is the weakest survivor, so it is exactly what you evict when something better arrives.

## Diagram

```
  nums = [3, 1, 5, 12, 2, 11]     k = 3 largest

  min-heap of size 3 (root = smallest kept so far)

  push 3        [3]
  push 1        [1, 3]
  push 5        [1, 3, 5]
  push 12       [1, 3, 5, 12]  size 4 > 3 → pop root (1)  → [3, 5, 12]
  push 2        [2, 3, 5, 12]  size 4 > 3 → pop root (2)  → [3, 5, 12]
  push 11       [3, 5, 11, 12] size 4 > 3 → pop root (3)  → [5, 11, 12]

  heap =  [5, 11, 12]   ← the 3 largest
           ▲
           root = 5 = the Kth largest

           5          the root is the WEAKEST of the survivors,
          / \         so evicting it always discards the right one
        11   12
```

## Template

```python
import heapq

def k_largest(nums: list[int], k: int) -> list[int]:
    h = []
    for x in nums:
        heapq.heappush(h, x)          # MIN-heap for K LARGEST
        if len(h) > k:
            heapq.heappop(h)          # evict the smallest
    return h                          # h[0] is the kth largest
```

Python's `heapq` is **min-only**. For a max-heap, push `-x` and negate on the way out.

### Top K frequent — count then heap

```python
from collections import Counter

def top_k_frequent(nums: list[int], k: int) -> list[int]:
    cnt = Counter(nums)
    return [x for x, _ in heapq.nlargest(k, cnt.items(), key=lambda p: p[1])]
```

Bucket sort by frequency gives O(n) if you want to beat the heap.

### K closest points

```python
def k_closest(points: list[list[int]], k: int) -> list[list[int]]:
    h = []
    for x, y in points:
        d = x * x + y * y             # never take the square root
        heapq.heappush(h, (-d, x, y)) # max-heap via negation
        if len(h) > k:
            heapq.heappop(h)
    return [[x, y] for _, x, y in h]
```

## Complexity

O(n log k) time, O(k) space — vs O(n log n) for a full sort.

## Common mistakes

- Reaching for a **max**-heap to find the K largest. It is the other way round.
- Forgetting `heapq` is min-only in Python
- Taking square roots for distance comparisons (slower, and floating point)

## Problems

- [215. Kth Largest Element](https://leetcode.com/problems/kth-largest-element-in-an-array/) — Medium
- [347. Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) — Medium
- [973. K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/) — Medium

---

## All problems in this pattern

**Heap** — 14 problems (7 core). Full list with dates and checkboxes: [`solutions/16-heap/`](../../solutions/16-heap/)

| # | Problem | Diff | Tier |
|---|---|---|---|
| 23 | [Merge K Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/) | Hard | **Core** |
| 295 | [Find Median From Data Stream](https://leetcode.com/problems/find-median-from-data-stream/) | Hard | **Core** |
| 373 | [Find K Pairs With Smallest Sums](https://leetcode.com/problems/find-k-pairs-with-smallest-sums/) | Medium | _opt_ |
| 378 | [Kth Smallest Element In A Sorted Matrix](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/) | Medium | **Core** |
| 480 | [Sliding Window Median](https://leetcode.com/problems/sliding-window-median/) | Hard | _opt_ |
| 502 | [Ipo](https://leetcode.com/problems/ipo/) | Hard | _opt_ |
| 621 | [Task Scheduler](https://leetcode.com/problems/task-scheduler/) | Medium | **Core** |
| 632 | [Smallest Range Covering Elements From K Lists](https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/) | Hard | _opt_ |
| 703 | [Kth Largest Element In A Stream](https://leetcode.com/problems/kth-largest-element-in-a-stream/) | Easy | **Core** |
| 767 | [Reorganize String](https://leetcode.com/problems/reorganize-string/) | Medium | **Core** |
| 871 | [Minimum Number Of Refueling Stops](https://leetcode.com/problems/minimum-number-of-refueling-stops/) | Hard | _opt_ |
| 1046 | [Last Stone Weight](https://leetcode.com/problems/last-stone-weight/) | Easy | **Core** |
| 1834 | [Single Threaded Cpu](https://leetcode.com/problems/single-threaded-cpu/) | Medium | _opt_ |
| 2542 | [Maximum Subsequence Score](https://leetcode.com/problems/maximum-subsequence-score/) | Medium | _opt_ |
