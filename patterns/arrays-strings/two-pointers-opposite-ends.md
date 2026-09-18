# Two Pointers — Opposite Ends

`Week 2` · Arrays & Strings

## Recognise it when

- The array is **sorted** and you need a **pair / triplet** summing to a target
- Words like *container*, *reverse*, *palindrome*
- You are about to write a nested loop over all pairs

## The insight

On a sorted array, comparing the current result against the target tells you **unambiguously** which pointer to move. That certainty is what removes the inner loop — O(n²) collapses to O(n).

If the sum is too small, the only way to increase it is to move `l` right. Moving `r` left can only make it smaller. There is never a reason to try both.

## Diagram

```
target = 9        sorted array
                  ┌───┬───┬───┬───┬───┬───┐
                  │ 1 │ 3 │ 4 │ 6 │ 8 │ 11│
                  └───┴───┴───┴───┴───┴───┘
                    ↑                   ↑
                    l                   r     1 + 11 = 12  > 9  → r--

                  ┌───┬───┬───┬───┬───┬───┐
                  │ 1 │ 3 │ 4 │ 6 │ 8 │ 11│
                  └───┴───┴───┴───┴───┴───┘
                    ↑               ↑
                    l               r         1 +  8 =  9  ==    → FOUND
```

Why no pair is missed: every pair `(i, j)` with `i < j` is either *inside* the current window or was eliminated by a move that provably could not contain the answer.

## Template

```python
def two_sum_sorted(a: list[int], target: int) -> tuple[int, int] | None:
    l, r = 0, len(a) - 1
    while l < r:
        cur = a[l] + a[r]
        if cur == target:
            return l, r
        elif cur < target:
            l += 1          # need a bigger sum
        else:
            r -= 1          # need a smaller sum
    return None
```

### Container With Most Water variant

Area is bounded by the **shorter** wall, so moving the taller one can never help:

```python
def max_area(h: list[int]) -> int:
    l, r, best = 0, len(h) - 1, 0
    while l < r:
        best = max(best, (r - l) * min(h[l], h[r]))
        if h[l] < h[r]:
            l += 1          # always move the SHORTER wall
        else:
            r -= 1
    return best
```

### 3Sum — fix one, two-point the rest

```python
def three_sum(nums: list[int]) -> list[list[int]]:
    nums.sort()
    res, n = [], len(nums)
    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue                      # skip duplicate anchors
        if nums[i] > 0:
            break                         # sorted: no way back to zero
        l, r = i + 1, n - 1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s < 0:
                l += 1
            elif s > 0:
                r -= 1
            else:
                res.append([nums[i], nums[l], nums[r]])
                l += 1
                r -= 1
                while l < r and nums[l] == nums[l - 1]:
                    l += 1                # skip duplicate lefts
                while l < r and nums[r] == nums[r + 1]:
                    r -= 1                # skip duplicate rights
    return res
```

## Complexity

| | Time | Space |
|---|---|---|
| Two Sum (sorted) | O(n) | O(1) |
| 3Sum | O(n²) | O(1) excl. output |

## Common mistakes

- **Forgetting to sort.** The whole technique depends on order.
- **3Sum duplicates** — you must skip on *all three* pointers, not just the anchor.
- Moving the taller wall in Container With Most Water. It can only shrink the area.

## Problems

- [167. Two Sum II](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) — Medium
- [11. Container With Most Water](https://leetcode.com/problems/container-with-most-water/) — Medium
- [15. 3Sum](https://leetcode.com/problems/3sum/) — Medium
