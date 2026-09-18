# In-Place Index Marking

`Week 9` · Arrays & Strings

## Recognise it when

- Array holds values in range **1..n** (or 0..n−1)
- Find missing / duplicate values
- The constraint says **O(1) extra space**

## The insight

The array **is** the hash table. Value `v` tells you to go mark index `v − 1`. Mark by negating the value there.

The constraint that values fit the index range is the entire enabler — check it first.

## Diagram

```
  nums = [4, 3, 2, 7, 8, 2, 3, 1]      n = 8, values in 1..8

  visit 4 → mark index 3 :  [4, 3, 2, -7, 8, 2, 3, 1]
  visit 3 → mark index 2 :  [4, 3, -2, -7, 8, 2, 3, 1]
  visit 2 → mark index 1 :  [4, -3, -2, -7, 8, 2, 3, 1]
  visit 7 → mark index 6 :  [4, -3, -2, -7, 8, 2, -3, 1]
  visit 8 → mark index 7 :  [4, -3, -2, -7, 8, 2, -3, -1]
  visit 2 → index 1 already negative → 2 is a DUPLICATE
  visit 3 → index 2 already negative → 3 is a DUPLICATE
  visit 1 → mark index 0 :  [-4, -3, -2, -7, 8, 2, -3, -1]

  index │  0   1   2   3   4   5   6   7
  sign  │  -   -   -   -   +   +   -   -
                            ▲   ▲
                    still positive → values 5 and 6 are MISSING
```

## Template

```python
def find_disappeared(nums: list[int]) -> list[int]:
    for x in nums:
        idx = abs(x) - 1            # abs() - x may already be negated
        if nums[idx] > 0:
            nums[idx] = -nums[idx]
    return [i + 1 for i, v in enumerate(nums) if v > 0]


def find_duplicates(nums: list[int]) -> list[int]:
    out = []
    for x in nums:
        idx = abs(x) - 1
        if nums[idx] < 0:           # already seen
            out.append(abs(x))
        else:
            nums[idx] = -nums[idx]
    return out
```

### First missing positive (LC 41)

Values are unbounded, so first clean the array, then cyclic-sort into place:

```python
def first_missing_positive(nums: list[int]) -> int:
    n = len(nums)
    for i in range(n):
        while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
            j = nums[i] - 1
            nums[i], nums[j] = nums[j], nums[i]   # swap into its home
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1
    return n + 1
```

## Complexity

O(n) time, **O(1) extra space** — that bound is the only reason to use this over a set.

## Common mistakes

- **Forgetting `abs()` when reading** — the value may already be negated
- Applying it when values fall outside `1..n`. Check the constraint first.
- In LC 41's swap loop, comparing **values** not indices (`nums[nums[i]-1] != nums[i]`), otherwise duplicates loop forever

## Problems

- [448. Find All Numbers Disappeared in an Array](https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/) — Easy
- [442. Find All Duplicates in an Array](https://leetcode.com/problems/find-all-duplicates-in-an-array/) — Medium
- [41. First Missing Positive](https://leetcode.com/problems/first-missing-positive/) — Hard
