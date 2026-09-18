# Monotonic Deque

`Week 13` · Linear Structures

## Recognise it when

- **Maximum or minimum of every sliding window**, in O(n)

## The insight

A heap gives O(n log k) — but you do not need full ordering, only the **maximum**.

A deque holding indices in decreasing value order keeps the max at the front. Anything smaller than an incoming element **can never be the max again** (the incoming one is bigger *and* lives longer), so you discard it permanently.

## Diagram

```
  nums = [1, 3, -1, -3, 5, 3, 6, 7]   k = 3

  deque holds INDICES, values decreasing front→back
  front = index of the current window maximum

  i=0  v=1   deque []      → push       [0]        (v: 1)
  i=1  v=3   3 >= 1 → pop 0, push 1     [1]        (v: 3)
  i=2  v=-1  -1 < 3 → push              [1,2]      (v: 3,-1)   window full → max = 3
  i=3  v=-3  push                       [1,2,3]    (v: 3,-1,-3) max = 3
  i=4  v=5   5 >= -3 pop, 5 >= -1 pop, 5 >= 3 pop  [4]  max = 5
  i=5  v=3   3 < 5 → push               [4,5]      max = 5
  i=6  v=6   6 >= 3 pop, 6 >= 5 pop     [6]        max = 6
  i=7  v=7   7 >= 6 pop                 [7]        max = 7

  output: [3, 3, 5, 5, 6, 7]

       pop from the BACK  ←── keeps the deque decreasing
       pop from the FRONT ──→ removes indices that fell out of the window
       ┌──────────────────────────┐
       │  front          back     │
       │   max                    │
       └──────────────────────────┘
```

## Template

```python
from collections import deque

def max_sliding_window(nums: list[int], k: int) -> list[int]:
    dq = deque()                       # indices, values decreasing
    out = []
    for r, x in enumerate(nums):
        while dq and nums[dq[-1]] <= x:
            dq.pop()                   # BACK: maintain ordering
        dq.append(r)

        if dq[0] <= r - k:
            dq.popleft()               # FRONT: expire out-of-window

        if r >= k - 1:
            out.append(nums[dq[0]])    # front is always the max
    return out
```

### Two deques — window max AND min (LC 1438)

```python
def longest_subarray(nums: list[int], limit: int) -> int:
    max_dq, min_dq = deque(), deque()
    l = best = 0
    for r, x in enumerate(nums):
        while max_dq and nums[max_dq[-1]] <= x: max_dq.pop()
        while min_dq and nums[min_dq[-1]] >= x: min_dq.pop()
        max_dq.append(r); min_dq.append(r)

        while nums[max_dq[0]] - nums[min_dq[0]] > limit:
            l += 1
            if max_dq[0] < l: max_dq.popleft()
            if min_dq[0] < l: min_dq.popleft()

        best = max(best, r - l + 1)
    return best
```

## Complexity

O(n) time — each index enters and leaves the deque once. O(k) space.

## Common mistakes

- Mixing up the two pops: **back for ordering, front for the window**
- Storing values instead of indices, so you cannot detect expiry
- Using `<` instead of `<=` when popping the back — equal values should be popped, otherwise stale duplicates linger

## Problems

- [239. Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/) — Hard
- [1438. Longest Subarray with Absolute Diff ≤ Limit](https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/) — Medium
- [862. Shortest Subarray with Sum at Least K](https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/) — Hard
