# Merge Sort — Divide & Conquer Counting

`Week 9` · Search & Sort

## Recognise it when

- Count **inversions**, *"smaller elements to the right"*, *"reverse pairs"*
- A counting problem a plain scan cannot do in under O(n²)

## The insight

During the **merge** step both halves are already sorted. That ordering lets you count cross-half pairs **in bulk**:

> when `left[i] > right[j]`, then *every remaining element* in the left half also beats `right[j]` — that is `mid − i` pairs counted in one step, not one at a time.

You get the counting for free alongside the sorting.

## Diagram

```
  counting inversions in [2, 4, 1, 3, 5]

              [2,4,1,3,5]
              /          \
        [2,4,1]          [3,5]
        /     \          /   \
     [2]    [4,1]      [3]   [5]
             /  \
           [4]  [1]        4 > 1 → 1 inversion, merge to [1,4]

  merge [2] and [1,4]:
      left=[2]  right=[1,4]
      2 > 1 → every remaining LEFT element beats 1
              len(left) - i = 1 - 0 = 1 inversion
      result [1,2,4]

  merge [1,2,4] and [3,5]:
      1<3 ok | 2<3 ok | 4>3 → remaining left = [4] → 1 inversion
      result [1,2,3,4,5]

  total inversions = 1 + 1 + 1 = 3
```

The key line:

```
  left:  [ 2  4  7 ]        right: [ 1  ... ]
           ▲                         ▲
           i                         j
  left[i]=2 > right[j]=1
  → 2, 4 AND 7 are all inversions with 1
  → add (len(left) - i) = 3 in ONE operation
```

## Template

```python
def sort_and_count(a: list[int]) -> tuple[list[int], int]:
    if len(a) <= 1:
        return a, 0
    mid = len(a) // 2
    left, cl = sort_and_count(a[:mid])
    right, cr = sort_and_count(a[mid:])

    merged, cm = [], 0
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i]); i += 1
        else:
            cm += len(left) - i        # bulk count - the whole trick
            merged.append(right[j]); j += 1
    merged += left[i:]
    merged += right[j:]
    return merged, cl + cr + cm
```

### Reverse pairs (LC 493) — count in a separate pass

The condition `left[i] > 2 * right[j]` is not the merge condition, so count **before** merging:

```python
def reverse_pairs(nums: list[int]) -> int:
    def sort_count(lo: int, hi: int) -> int:
        if hi - lo <= 1:
            return 0
        mid = (lo + hi) // 2
        cnt = sort_count(lo, mid) + sort_count(mid, hi)
        j = mid
        for i in range(lo, mid):                  # count pass
            while j < hi and nums[i] > 2 * nums[j]:
                j += 1
            cnt += j - mid
        nums[lo:hi] = sorted(nums[lo:hi])         # then merge
        return cnt
    return sort_count(0, len(nums))
```

## Complexity

O(n log n) time, O(n) space.

**Alternative:** a Fenwick tree (BIT) over coordinate-compressed values solves the same family and is often quicker to write correctly.

## Common mistakes

- Counting **after** merging has destroyed the half boundary
- Incrementing by 1 per pair instead of the bulk `len(left) - i`
- For reverse pairs, trying to fold the `2*` condition into the merge comparison

## Problems

- [493. Reverse Pairs](https://leetcode.com/problems/reverse-pairs/) — Hard
- [315. Count of Smaller Numbers After Self](https://leetcode.com/problems/count-of-smaller-numbers-after-self/) — Hard
- [912. Sort an Array](https://leetcode.com/problems/sort-an-array/) — Medium
