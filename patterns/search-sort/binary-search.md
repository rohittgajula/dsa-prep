# Binary Search — Exact & Bounds

`Week 7` · Search & Sort

## Recognise it when

- Input is **sorted** (or rotated-sorted) and you need an element or a **boundary**

## The insight

Each comparison discards half the space. The hard part is never the halving — it is the **invariant**.

Commit to **one template** (half-open `[l, r)`) and derive every variant from it, rather than memorising four subtly different loops.

## Diagram

```
  a = [1, 3, 3, 5, 8, 8, 8, 11]      target = 8
       0  1  2  3  4  5  6   7

  half-open window [l, r)   ── r is EXCLUSIVE

  l=0        r=8    m=4   a[4]=8  not < 8  → r = 4
  ├───────────────────┤
  l=0    r=4          m=2   a[2]=3  < 8     → l = 3
  ├───────┤
      l=3 r=4         m=3   a[3]=5  < 8     → l = 4
        ├─┤
          l=r=4  →  loop ends, return 4   ← first index with a[i] >= 8

  lower_bound(8) = 4        first 8
  lower_bound(9) = 7        first index > all 8s  → last 8 is at 6
```

### The four questions, one template

| Question | Call |
|---|---|
| First index with `a[i] >= x` | `lower_bound(x)` |
| First index with `a[i] > x` | `lower_bound(x + 1)` |
| Last index with `a[i] <= x` | `lower_bound(x + 1) - 1` |
| Does `x` exist? | `i = lower_bound(x); i < n and a[i] == x` |

## Template

```python
def lower_bound(a: list[int], target: int) -> int:
    """First index i with a[i] >= target. Returns len(a) if none."""
    l, r = 0, len(a)                  # half-open [l, r)
    while l < r:
        m = l + (r - l) // 2          # avoids overflow in C++/Java
        if a[m] < target:
            l = m + 1
        else:
            r = m
    return l
```

### Rotated array — one half is always sorted

```
  [4, 5, 6, 7, 0, 1, 2]        target = 0
   └────sorted────┘ └sorted┘
            m

  Compare a[l] with a[m]:
    a[l] <= a[m]  → the LEFT half is sorted
    otherwise     → the RIGHT half is sorted
  Then ask whether the target lies inside the sorted half.
```

```python
def search_rotated(nums: list[int], target: int) -> int:
    l, r = 0, len(nums) - 1
    while l <= r:
        m = (l + r) // 2
        if nums[m] == target:
            return m
        if nums[l] <= nums[m]:                    # left half sorted
            if nums[l] <= target < nums[m]:
                r = m - 1
            else:
                l = m + 1
        else:                                     # right half sorted
            if nums[m] < target <= nums[r]:
                l = m + 1
            else:
                r = m - 1
    return -1
```

## Complexity

O(log n) time, O(1) space.

## Common mistakes

- **Infinite loop** from `l = m` instead of `l = m + 1`
- Mixing `[l, r)` and `[l, r]` conventions in the same function
- For rotated arrays, comparing `a[m]` to `a[r]` when finding the minimum but `a[l]` to `a[m]` when searching — know which you are doing and why

## Problems

- [704. Binary Search](https://leetcode.com/problems/binary-search/) — Easy
- [34. Find First and Last Position](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) — Medium
- [33. Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) — Medium

---

## All problems in this pattern

**Binary Search** — 16 problems (11 core). Full list with dates and checkboxes: [`solutions/07-binary-search/`](../../solutions/07-binary-search/)

| # | Problem | Diff | Tier |
|---|---|---|---|
| 33 | [Search In Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) | Medium | **Core** |
| 34 | [Find First And Last Position Of Element In Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) | Medium | **Core** |
| 35 | [Search Insert Position](https://leetcode.com/problems/search-insert-position/) | Easy | **Core** |
| 69 | [Sqrtx](https://leetcode.com/problems/sqrtx/) | Easy | **Core** |
| 74 | [Search A 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/) | Medium | **Core** |
| 81 | [Search In Rotated Sorted Array Ii](https://leetcode.com/problems/search-in-rotated-sorted-array-ii/) | Medium | _opt_ |
| 153 | [Find Minimum In Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) | Medium | **Core** |
| 154 | [Find Minimum In Rotated Sorted Array Ii](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/) | Hard | _opt_ |
| 162 | [Find Peak Element](https://leetcode.com/problems/find-peak-element/) | Medium | **Core** |
| 240 | [Search A 2D Matrix Ii](https://leetcode.com/problems/search-a-2d-matrix-ii/) | Medium | **Core** |
| 278 | [First Bad Version](https://leetcode.com/problems/first-bad-version/) | Easy | **Core** |
| 367 | [Valid Perfect Square](https://leetcode.com/problems/valid-perfect-square/) | Easy | _opt_ |
| 540 | [Single Element In A Sorted Array](https://leetcode.com/problems/single-element-in-a-sorted-array/) | Medium | **Core** |
| 658 | [Find K Closest Elements](https://leetcode.com/problems/find-k-closest-elements/) | Medium | _opt_ |
| 704 | [Binary Search](https://leetcode.com/problems/binary-search/) | Easy | **Core** |
| 852 | [Peak Index In A Mountain Array](https://leetcode.com/problems/peak-index-in-a-mountain-array/) | Medium | _opt_ |
