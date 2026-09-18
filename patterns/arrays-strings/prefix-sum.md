# Prefix Sum

`Week 4` · Arrays & Strings

## Recognise it when

- **Many** range-sum queries on a **static** array
- *"Sum from i to j"* asked repeatedly
- *"Product of everything except me"*

## The insight

Precompute cumulative sums once, then any range becomes a **single subtraction**. You trade O(n) space for O(1) queries.

## Diagram

```
  a    =  [ 3 ,  1 ,  4 ,  1 ,  5 ]
                                        pre[0] = 0  (the sentinel that
  pre  = [0,  3,   4,   8,   9,  14]     removes every edge case)
          │   │    │    │    │    │
          0   1    2    3    4    5

  sum(a[1..3])  =  pre[4] - pre[1]
                =    9    -   3     =  6
                     └────────┘
                 ┌───┬───┬───┬───┬───┐
                 │ 3 │ 1 │ 4 │ 1 │ 5 │
                 └───┴───┴───┴───┴───┘
                       └───────┘
                        1+4+1 = 6  ✓
```

**Use size `n+1` with `pre[0] = 0`.** It removes the "what if i == 0" branch entirely.

## Template

```python
def build_prefix(a: list[int]) -> list[int]:
    pre = [0] * (len(a) + 1)
    for i, x in enumerate(a):
        pre[i + 1] = pre[i] + x
    return pre

def range_sum(pre: list[int], i: int, j: int) -> int:
    """Sum of a[i..j] inclusive."""
    return pre[j + 1] - pre[i]
```

### 2D prefix sum — inclusion/exclusion

```
        ┌─────────────┬──────┐
        │      A      │  B   │      sum(D) = total
        ├─────────────┼──────┤              - above
        │      C      │  D   │              - left
        └─────────────┴──────┘              + top-left
                                     (added back because it was
                                      subtracted twice)
```

```python
def build_2d(m: list[list[int]]) -> list[list[int]]:
    R, C = len(m), len(m[0])
    pre = [[0] * (C + 1) for _ in range(R + 1)]
    for r in range(R):
        for c in range(C):
            pre[r+1][c+1] = m[r][c] + pre[r][c+1] + pre[r+1][c] - pre[r][c]
    return pre

def region(pre, r1, c1, r2, c2) -> int:
    return (pre[r2+1][c2+1] - pre[r1][c2+1] - pre[r2+1][c1] + pre[r1][c1])
```

### Product except self — prefix × suffix, no division

```python
def product_except_self(nums: list[int]) -> list[int]:
    n = len(nums)
    out = [1] * n
    left = 1
    for i in range(n):
        out[i] = left
        left *= nums[i]
    right = 1
    for i in range(n - 1, -1, -1):
        out[i] *= right
        right *= nums[i]
    return out
```

## Complexity

O(n) build, **O(1) per query**. O(n) extra space.

## Common mistakes

- Using a size-`n` array and then fighting `i == 0` everywhere. Use `n+1`.
- Mixing up inclusive/exclusive bounds — write the formula down once and reuse it.

## Problems

- [303. Range Sum Query — Immutable](https://leetcode.com/problems/range-sum-query-immutable/) — Easy
- [724. Find Pivot Index](https://leetcode.com/problems/find-pivot-index/) — Easy
- [238. Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/) — Medium
