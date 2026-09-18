# K-Way Merge

`Week 14` · Linear Structures

## Recognise it when

- Merge **k sorted** lists or arrays
- *"Kth smallest across k sorted things"*
- *"Smallest range covering all lists"*

## The insight

You only ever need the **smallest unconsumed element across all k lists**. A heap of exactly **k candidates** — one per list — gives it in O(log k), and you refill from whichever list you just consumed.

## Diagram

```
  lists:  A = [1, 4, 5]
          B = [1, 3, 4]
          C = [2, 6]

  heap holds ONE candidate per list: (value, list_id, index)

  init      heap = [(1,A,0), (1,B,0), (2,C,0)]
  pop (1,A,0) → output 1, refill from A index 1 → push (4,A,1)
            heap = [(1,B,0), (2,C,0), (4,A,1)]
  pop (1,B,0) → output 1, push (3,B,1)
            heap = [(2,C,0), (3,B,1), (4,A,1)]
  pop (2,C,0) → output 2, push (6,C,1)
            heap = [(3,B,1), (4,A,1), (6,C,1)]
  ...
  output: 1 1 2 3 4 4 5 6

       heap size stays at k  ──►  O(log k) per element
       total N elements      ──►  O(N log k)
```

Compare with merging pairwise one at a time: O(N·k). The heap turns the `k` into `log k`.

## Template

```python
import heapq

def merge_k_sorted(lists: list[list[int]]) -> list[int]:
    h = [(lst[0], i, 0) for i, lst in enumerate(lists) if lst]
    heapq.heapify(h)
    out = []
    while h:
        val, i, j = heapq.heappop(h)
        out.append(val)
        if j + 1 < len(lists[i]):
            heapq.heappush(h, (lists[i][j + 1], i, j + 1))
    return out
```

### Merge k linked lists

```python
def merge_k_lists(lists):
    h = [(node.val, i, node) for i, node in enumerate(lists) if node]
    heapq.heapify(h)
    dummy = tail = ListNode(0)
    while h:
        val, i, node = heapq.heappop(h)
        tail.next = node
        tail = node
        if node.next:
            heapq.heappush(h, (node.next.val, i, node.next))
    return dummy.next
```

> The **list index `i` is a tie-breaker**. Without it, Python compares the third element when values tie — and `ListNode` objects are not comparable, so it throws.

### Smallest range covering all lists

```python
def smallest_range(nums: list[list[int]]) -> list[int]:
    h = [(lst[0], i, 0) for i, lst in enumerate(nums)]
    heapq.heapify(h)
    cur_max = max(lst[0] for lst in nums)
    best = [-10**9, 10**9]
    while True:
        lo, i, j = heapq.heappop(h)
        if cur_max - lo < best[1] - best[0]:
            best = [lo, cur_max]
        if j + 1 == len(nums[i]):
            return best                      # one list exhausted - can't cover
        nxt = nums[i][j + 1]
        cur_max = max(cur_max, nxt)
        heapq.heappush(h, (nxt, i, j + 1))
```

## Complexity

O(N log k), where N is the total element count. O(k) space.

## Common mistakes

- **Missing tie-breaker** → `TypeError: '<' not supported between instances of 'ListNode'`
- Pushing whole lists into the heap instead of one candidate each — that loses the O(k) space bound
- Forgetting to skip empty lists during initialisation

## Problems

- [23. Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/) — Hard
- [378. Kth Smallest in a Sorted Matrix](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/) — Medium
- [632. Smallest Range Covering Elements from K Lists](https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/) — Hard
