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
