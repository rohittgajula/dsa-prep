# Cyclic Sort

`Week 9` · Search & Sort

## Recognise it when

- Array contains `n` numbers from the range **1..n** (or 0..n−1)
- Find missing / duplicate values in **O(n) time, O(1) space**

## The insight

Because values map **one-to-one onto indices**, every value has a correct home: value `v` belongs at index `v − 1`.

Repeatedly swap each value into its home. Whatever ends up out of place reveals the missing or duplicate value.

## Diagram

```
  nums = [3, 1, 5, 4, 2]        each value v belongs at index v-1

  i=0: nums[0]=3 → home is index 2, which holds 5 (≠3) → SWAP
       [5, 1, 3, 4, 2]          do NOT advance i
  i=0: nums[0]=5 → home is index 4, which holds 2 (≠5) → SWAP
       [2, 1, 3, 4, 5]          do NOT advance i
  i=0: nums[0]=2 → home is index 1, which holds 1 (≠2) → SWAP
       [1, 2, 3, 4, 5]          do NOT advance i
  i=0: nums[0]=1 → home is index 0 → already correct → i++
  i=1..4: all already in place → done

  final: [1, 2, 3, 4, 5]
          ▲  ▲  ▲  ▲  ▲
          every index i holds i+1  →  nothing missing
```

**Why it is O(n) despite the inner `while`:** every swap puts at least one value into its final position permanently. There are at most `n` such placements, so at most `n` swaps total.

## Template

```python
def cyclic_sort(nums: list[int]) -> None:
    i = 0
    n = len(nums)
    while i < n:
        j = nums[i] - 1                      # where nums[i] belongs
        if 0 <= j < n and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]   # swap, do NOT advance
        else:
            i += 1
```

> Compare **values** (`nums[i] != nums[j]`), not indices. With indices, duplicates loop forever.

### Missing number

```python
def missing_number(nums: list[int]) -> int:
    n = len(nums)
    i = 0
    while i < n:
        j = nums[i]                          # 0..n here, so home is index v
        if j < n and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
    for i in range(n):
        if nums[i] != i:
            return i
    return n
```

Also solvable by XOR or the sum formula `n(n+1)/2 − sum` — know all three.

## Complexity

O(n) time, O(1) space.

## Common mistakes

- **Advancing `i` after a swap** — the incoming value is unexamined
- Comparing indices instead of values → infinite loop on duplicates
- Not bounds-checking `j` when the input may contain values outside the range

## Problems

- [268. Missing Number](https://leetcode.com/problems/missing-number/) — Easy
- [448. Find All Numbers Disappeared](https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/) — Easy
- [41. First Missing Positive](https://leetcode.com/problems/first-missing-positive/) — Hard

---

## All problems in this pattern

**Sorting** — 13 problems (8 core). Full list with dates and checkboxes: [`solutions/09-sorting/`](../../solutions/09-sorting/)

| # | Problem | Diff | Tier |
|---|---|---|---|
| 41 | [First Missing Positive](https://leetcode.com/problems/first-missing-positive/) | Hard | **Core** |
| 164 | [Maximum Gap](https://leetcode.com/problems/maximum-gap/) | Medium | _opt_ |
| 179 | [Largest Number](https://leetcode.com/problems/largest-number/) | Medium | **Core** |
| 215 | [Kth Largest Element In An Array](https://leetcode.com/problems/kth-largest-element-in-an-array/) | Medium | **Core** |
| 268 | [Missing Number](https://leetcode.com/problems/missing-number/) | Easy | **Core** |
| 274 | [H Index](https://leetcode.com/problems/h-index/) | Medium | _opt_ |
| 315 | [Count Of Smaller Numbers After Self](https://leetcode.com/problems/count-of-smaller-numbers-after-self/) | Hard | _opt_ |
| 442 | [Find All Duplicates In An Array](https://leetcode.com/problems/find-all-duplicates-in-an-array/) | Medium | **Core** |
| 448 | [Find All Numbers Disappeared In An Array](https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/) | Easy | **Core** |
| 493 | [Reverse Pairs](https://leetcode.com/problems/reverse-pairs/) | Hard | _opt_ |
| 912 | [Sort An Array](https://leetcode.com/problems/sort-an-array/) | Medium | **Core** |
| 973 | [K Closest Points To Origin](https://leetcode.com/problems/k-closest-points-to-origin/) | Medium | **Core** |
| 2418 | [Sort The People](https://leetcode.com/problems/sort-the-people/) | Easy | _opt_ |
