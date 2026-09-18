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
