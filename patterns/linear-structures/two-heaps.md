# Two Heaps (Running Median)

`Week 14` · Linear Structures

## Recognise it when

- **Median of a stream**, or you need the middle element as data arrives

## The insight

Split the data at the median. A **max-heap** holds the smaller half, a **min-heap** the larger half.

The median is then always sitting at one or both tops — **O(1) to read**, O(log n) to maintain.

## Diagram

```
        LOW (max-heap)              HIGH (min-heap)
        smaller half                larger half

             5                           7
            / \                         / \
           3   4                       8   9
           ▲                           ▲
         top = 5                     top = 7
      biggest of the small        smallest of the large

        ─────────── 5 │ 7 ───────────
                   the median lives here

  odd  total → median = low.top            (low holds the extra one)
  even total → median = (low.top + high.top) / 2

  INVARIANT:  len(low) == len(high)   or   len(low) == len(high) + 1
```

### The insert dance — always in this order

```
  1. push x onto LOW
  2. move LOW's top over to HIGH        (guarantees ordering across the split)
  3. if HIGH is bigger, move its top back to LOW   (restores the size invariant)
```

Doing it in this fixed order means you never have to compare `x` against anything — step 2 sorts it out for you.

## Template

```python
import heapq

class MedianFinder:
    def __init__(self):
        self.low = []    # max-heap (negated values) - smaller half
        self.high = []   # min-heap                  - larger half

    def addNum(self, num: int) -> None:
        heapq.heappush(self.low, -num)                    # 1
        heapq.heappush(self.high, -heapq.heappop(self.low))  # 2
        if len(self.high) > len(self.low):                # 3
            heapq.heappush(self.low, -heapq.heappop(self.high))

    def findMedian(self) -> float:
        if len(self.low) > len(self.high):
            return -self.low[0]
        return (-self.low[0] + self.high[0]) / 2
```

## Complexity

O(log n) per insert, **O(1)** per median query.

## Common mistakes

- Doing the three steps out of order → the heaps drift apart and the median is wrong
- Forgetting to negate for Python's max-heap (both on push *and* read)
- Comparing `x` to the tops manually instead of trusting the push-transfer-rebalance dance

## Problems

- [295. Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/) — Hard
- [480. Sliding Window Median](https://leetcode.com/problems/sliding-window-median/) — Hard
- [502. IPO](https://leetcode.com/problems/ipo/) — Hard

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
