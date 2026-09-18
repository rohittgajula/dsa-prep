# Dutch National Flag (3-Way Partition)

`Week 2` · Arrays & Strings

## Recognise it when

- Sort or partition into exactly **three** categories, one pass, O(1) space
- *"Sort colors"*, *"move zeroes"*, 3-way quicksort partition

## The insight

Maintain **three regions** with three pointers. Everything before `low` is category 0, everything after `high` is category 2, and `mid` scans the unknown middle. Every swap shrinks the unknown region, so one pass suffices.

## Diagram

```
        ┌──────────┬──────────┬───────────────┬──────────┐
        │   all 0  │   all 1  │   UNKNOWN     │   all 2  │
        └──────────┴──────────┴───────────────┴──────────┘
                   ▲          ▲               ▲
                  low        mid            high

  Invariants:
    a[0    .. low-1 ]  == 0
    a[low  .. mid-1 ]  == 1
    a[mid  .. high  ]  == unexamined
    a[high+1 .. n-1 ]  == 2

  a[mid] == 0 → swap(low, mid), low++, mid++    (both advance)
  a[mid] == 1 → mid++                           (already in place)
  a[mid] == 2 → swap(mid, high), high--         (mid does NOT advance!)
```

### Why `mid` must not advance on a 2-swap

```
  [2, 0, 1]      low=0  mid=0  high=2
   ^mid

  a[mid]==2 → swap with high:
  [1, 0, 2]      high=1
   ^mid          the value 1 just arrived and is UNEXAMINED

  If you advanced mid here you would skip it entirely.
```

## Template

```python
def sort_colors(a: list[int]) -> None:
    low = mid = 0
    high = len(a) - 1
    while mid <= high:
        if a[mid] == 0:
            a[low], a[mid] = a[mid], a[low]
            low += 1
            mid += 1
        elif a[mid] == 2:
            a[mid], a[high] = a[high], a[mid]
            high -= 1              # deliberately do NOT advance mid
        else:
            mid += 1
```

## Complexity

O(n) time, O(1) space, single pass.

## Common mistakes

- **Advancing `mid` after swapping with `high`** — the classic bug
- Loop condition `mid < high` instead of `mid <= high` (misses the last element)

## Problems

- [75. Sort Colors](https://leetcode.com/problems/sort-colors/) — Medium
- [283. Move Zeroes](https://leetcode.com/problems/move-zeroes/) — Easy
- [905. Sort Array By Parity](https://leetcode.com/problems/sort-array-by-parity/) — Easy

---

## All problems in this pattern

**Two Pointers** — 16 problems (12 core). Full list with dates and checkboxes: [`solutions/02-two-pointers/`](../../solutions/02-two-pointers/)

| # | Problem | Diff | Tier |
|---|---|---|---|
| 11 | [Container With Most Water](https://leetcode.com/problems/container-with-most-water/) | Medium | **Core** |
| 15 | [3Sum](https://leetcode.com/problems/3sum/) | Medium | **Core** |
| 16 | [3Sum Closest](https://leetcode.com/problems/3sum-closest/) | Medium | _opt_ |
| 18 | [4Sum](https://leetcode.com/problems/4sum/) | Medium | _opt_ |
| 31 | [Next Permutation](https://leetcode.com/problems/next-permutation/) | Medium | **Core** |
| 42 | [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/) | Hard | _opt_ |
| 75 | [Sort Colors](https://leetcode.com/problems/sort-colors/) | Medium | **Core** |
| 80 | [Remove Duplicates From Sorted Array Ii](https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/) | Medium | **Core** |
| 125 | [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) | Easy | **Core** |
| 167 | [Two Sum Ii Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) | Medium | **Core** |
| 189 | [Rotate Array](https://leetcode.com/problems/rotate-array/) | Medium | **Core** |
| 287 | [Find The Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/) | Medium | **Core** |
| 344 | [Reverse String](https://leetcode.com/problems/reverse-string/) | Easy | **Core** |
| 680 | [Valid Palindrome Ii](https://leetcode.com/problems/valid-palindrome-ii/) | Easy | **Core** |
| 905 | [Sort Array By Parity](https://leetcode.com/problems/sort-array-by-parity/) | Easy | _opt_ |
| 977 | [Squares Of A Sorted Array](https://leetcode.com/problems/squares-of-a-sorted-array/) | Easy | **Core** |
