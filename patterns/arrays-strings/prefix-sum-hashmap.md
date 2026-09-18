# Prefix Sum + HashMap

`Week 4` · Arrays & Strings

## Recognise it when

- *"**Count** of subarrays with sum = k"* — counting, not a max length
- The array may contain **negatives** (which kills sliding window)
- *"Subarray divisible by k"*, *"equal number of 0s and 1s"*

## The insight

Any subarray sum is `prefix[j] − prefix[i]`.

So *"is there a subarray ending at j summing to k"* becomes *"have I seen the prefix value `current − k` before?"* A hashmap answers that in O(1).

This is the highest-value trick in the array section — it turns a family of O(n²) problems into O(n).

## Diagram

```
  nums = [1, 2, 3, -1, 2]      k = 5

  index   │  0   1   2   3   4
  value   │  1   2   3  -1   2
  prefix  │  1   3   6   5   7
                      │
  at i=2: prefix = 6, look for 6 - 5 = 1  →  seen at index 0
          so nums[1..2] = 2+3 = 5   ✓

  ┌──────────────── prefix = 6 ────────────────┐
  │ 1 │ 2 │ 3 │
  └───┘
   ^ prefix = 1
       └───────┘
        the gap between them sums to exactly k
```

### Why `seen = {0: 1}` is mandatory

```
  nums = [5, ...]   k = 5

  i=0: prefix = 5, look for 5 - 5 = 0
       Without {0:1} the map has never "seen" 0
       → the subarray that STARTS AT INDEX 0 is missed entirely
```

## Template

```python
def subarray_sum(nums: list[int], k: int) -> int:
    seen = {0: 1}            # prefix 0 has been seen once - CRITICAL
    cur = 0
    count = 0
    for x in nums:
        cur += x
        count += seen.get(cur - k, 0)   # count BEFORE inserting
        seen[cur] = seen.get(cur, 0) + 1
    return count
```

> **Order matters.** Count first, then insert. Inserting first lets a zero-length subarray match itself.

### Divisible by k — store the remainder

```python
def subarrays_div_by_k(nums: list[int], k: int) -> int:
    seen = {0: 1}
    cur = count = 0
    for x in nums:
        cur = (cur + x) % k      # Python's % is already non-negative
        count += seen.get(cur, 0)
        seen[cur] = seen.get(cur, 0) + 1
    return count
```

In Java/C++, `%` can return a negative — normalise with `((cur % k) + k) % k`.

### Equal 0s and 1s — map 0 → −1

```python
def find_max_length(nums: list[int]) -> int:
    first = {0: -1}          # store FIRST index for a longest-length answer
    cur = best = 0
    for i, x in enumerate(nums):
        cur += 1 if x == 1 else -1
        if cur in first:
            best = max(best, i - first[cur])
        else:
            first[cur] = i   # only record the first time
    return best
```

> **Counting problems store a count. Longest-length problems store the first index** and never overwrite it.

## Complexity

O(n) time, O(n) space.

## Common mistakes

- **Forgetting `seen = {0: 1}`** — silently drops every subarray starting at index 0
- Inserting the current prefix before counting
- Negative modulo in Java/C++
- Storing counts when you need first-index (or vice versa)

## Problems

- [560. Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/) — Medium
- [974. Subarray Sums Divisible by K](https://leetcode.com/problems/subarray-sums-divisible-by-k/) — Medium
- [525. Contiguous Array](https://leetcode.com/problems/contiguous-array/) — Medium
