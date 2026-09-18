# Kadane's Algorithm

`Week 1` · Arrays & Strings

## Recognise it when

- *"Maximum sum contiguous subarray"*
- The product variant, or a circular array

## The insight

At each index there are only **two choices**: extend the previous subarray, or start fresh here.

If the running sum ever goes **negative**, it can only hurt whatever comes next — so you drop it. That single local decision produces the global optimum.

## Diagram

```
  nums = [-2,  1, -3,  4, -1,  2,  1, -5,  4]

  i    │  -2    1   -3    4   -1    2    1   -5    4
  ─────┼────────────────────────────────────────────
  cur  │  -2    1   -2    4    3    5    6    1    5
         │      ▲    ▲    ▲                   ▲
         │      │    │    │                   │
         │   restart │  restart          extend (1 > -5+... )
         │  (1 > -2+1)  (4 > -2+4)
  best │  -2    1    1    4    4    5    6    6    6  ★

                        ┌──────────────────┐
  answer subarray:  ... │ 4  -1   2   1 │ ...    sum = 6
                        └──────────────────┘

  Rule at each step:   cur = max(x, cur + x)
                              └┬┘   └──┬──┘
                          start here  extend
```

## Template

```python
def max_subarray(nums: list[int]) -> int:
    cur = best = nums[0]          # NOT 0 - breaks on all-negative input
    for x in nums[1:]:
        cur = max(x, cur + x)     # restart, or extend
        best = max(best, cur)
    return best
```

### Maximum product — track the minimum too

A large negative times a negative becomes a large positive, so the running **minimum** can become the next maximum:

```python
def max_product(nums: list[int]) -> int:
    cur_max = cur_min = best = nums[0]
    for x in nums[1:]:
        if x < 0:
            cur_max, cur_min = cur_min, cur_max   # swap on a negative
        cur_max = max(x, cur_max * x)
        cur_min = min(x, cur_min * x)
        best = max(best, cur_max)
    return best
```

### Circular array

```python
def max_subarray_circular(nums: list[int]) -> int:
    total = sum(nums)
    cur_max = best_max = nums[0]
    cur_min = best_min = nums[0]
    for x in nums[1:]:
        cur_max = max(x, cur_max + x); best_max = max(best_max, cur_max)
        cur_min = min(x, cur_min + x); best_min = min(best_min, cur_min)
    if best_max < 0:               # all negative - the wrap answer is empty
        return best_max
    return max(best_max, total - best_min)
```

## Complexity

O(n) time, O(1) space.

## Common mistakes

- **Initialising to 0** instead of `nums[0]`. On `[-3, -1, -2]` you would return 0, which is wrong unless empty subarrays are allowed.
- For max product, forgetting to track the minimum
- For circular, forgetting the all-negative special case

## Problems

- [53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) — Medium
- [152. Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/) — Medium
- [918. Maximum Sum Circular Subarray](https://leetcode.com/problems/maximum-sum-circular-subarray/) — Medium

---

## All problems in this pattern

**Array Basics** — 14 problems (11 core). Full list with dates and checkboxes: [`solutions/01-array-basics/`](../../solutions/01-array-basics/)

| # | Problem | Diff | Tier |
|---|---|---|---|
| 1 | [Two Sum](https://leetcode.com/problems/two-sum/) | Easy | **Core** |
| 26 | [Remove Duplicates From Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) | Easy | **Core** |
| 27 | [Remove Element](https://leetcode.com/problems/remove-element/) | Easy | **Core** |
| 66 | [Plus One](https://leetcode.com/problems/plus-one/) | Easy | **Core** |
| 53 | [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) | Medium | **Core** |
| 88 | [Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/) | Easy | **Core** |
| 121 | [Best Time To Buy And Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) | Easy | **Core** |
| 169 | [Majority Element](https://leetcode.com/problems/majority-element/) | Easy | **Core** |
| 283 | [Move Zeroes](https://leetcode.com/problems/move-zeroes/) | Easy | **Core** |
| 485 | [Max Consecutive Ones](https://leetcode.com/problems/max-consecutive-ones/) | Easy | **Core** |
| 1480 | [Running Sum Of 1D Array](https://leetcode.com/problems/running-sum-of-1d-array/) | Easy | **Core** |
| 1512 | [Number Of Good Pairs](https://leetcode.com/problems/number-of-good-pairs/) | Easy | _opt_ |
| 1672 | [Richest Customer Wealth](https://leetcode.com/problems/richest-customer-wealth/) | Easy | _opt_ |
| 1929 | [Concatenation Of Array](https://leetcode.com/problems/concatenation-of-array/) | Easy | _opt_ |
