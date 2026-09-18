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
