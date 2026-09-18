# Sliding Window — Variable Size

`Week 3` · Arrays & Strings

## Recognise it when

- *"**Longest** / **shortest** subarray or substring **such that** \<condition\>"*
- All values positive, or the condition is a character count
- **Not** for arrays with negatives — use [prefix sum + hashmap](prefix-sum-hashmap.md) there

## The insight

The window is a **monotonic predicate**: if a window is invalid, extending it right keeps it invalid. So the only way back to valid is to **shrink from the left**.

Each index enters once and leaves once, so despite the nested `while`, the whole thing is **O(n)** — not O(n²).

**The shrink condition is the entire problem.** Get that right and the rest is boilerplate.

## Diagram

```
"abcabcbb"  →  longest substring without repeats

 r=0  [a]                     window "a"        len 1
 r=1  [ab]                    window "ab"       len 2
 r=2  [abc]                   window "abc"      len 3  ★
 r=3  [abca]  'a' repeats  →  shrink from left
       ^l
        [bca]                 window "bca"      len 3
 r=4   [bcab] 'b' repeats  →  shrink
         ^l
         [cab]                window "cab"      len 3
 ...

        l ────────► r         l only ever moves RIGHT
        └──────────┘          → each index touched at most twice
```

## Template

```python
def longest_valid(a) -> int:
    l = 0
    best = 0
    state = {}                      # whatever "valid" needs

    for r in range(len(a)):
        add(a[r], state)            # expand right

        while not valid(state):     # shrink until valid again
            remove(a[l], state)
            l += 1

        best = max(best, r - l + 1) # record AFTER restoring validity
    return best
```

### Longest — record after the shrink

```python
def length_of_longest_substring(s: str) -> int:
    seen = {}
    l = best = 0
    for r, ch in enumerate(s):
        if ch in seen and seen[ch] >= l:
            l = seen[ch] + 1        # jump l past the previous occurrence
        seen[ch] = r
        best = max(best, r - l + 1)
    return best
```

### Shortest — record INSIDE the shrink

```python
def min_subarray_len(target: int, nums: list[int]) -> int:
    l = 0
    cur = 0
    best = float('inf')
    for r, x in enumerate(nums):
        cur += x
        while cur >= target:            # while still VALID
            best = min(best, r - l + 1) # record here
            cur -= nums[l]
            l += 1
    return 0 if best == float('inf') else best
```

> **Longest → update after the while. Shortest → update inside the while.** This single difference is where most bugs live.

## Complexity

O(n) time. Space O(1) or O(alphabet).

## Common mistakes

- Putting the answer update in the wrong place (see box above)
- Using it on arrays with **negative numbers** — adding an element can then *help*, so the monotonic property breaks
- Forgetting that `l` must never move backwards

## Problems

- [3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) — Medium
- [209. Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/) — Medium
- [76. Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) — Hard

---

## All problems in this pattern

**Sliding Window** — 16 problems (11 core). Full list with dates and checkboxes: [`solutions/03-sliding-window/`](../../solutions/03-sliding-window/)

| # | Problem | Diff | Tier |
|---|---|---|---|
| 3 | [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | Medium | **Core** |
| 30 | [Substring With Concatenation Of All Words](https://leetcode.com/problems/substring-with-concatenation-of-all-words/) | Hard | _opt_ |
| 76 | [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) | Hard | **Core** |
| 209 | [Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/) | Medium | **Core** |
| 219 | [Contains Duplicate Ii](https://leetcode.com/problems/contains-duplicate-ii/) | Easy | **Core** |
| 424 | [Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/) | Medium | **Core** |
| 438 | [Find All Anagrams In A String](https://leetcode.com/problems/find-all-anagrams-in-a-string/) | Medium | **Core** |
| 567 | [Permutation In String](https://leetcode.com/problems/permutation-in-string/) | Medium | **Core** |
| 643 | [Maximum Average Subarray I](https://leetcode.com/problems/maximum-average-subarray-i/) | Easy | **Core** |
| 713 | [Subarray Product Less Than K](https://leetcode.com/problems/subarray-product-less-than-k/) | Medium | **Core** |
| 904 | [Fruit Into Baskets](https://leetcode.com/problems/fruit-into-baskets/) | Medium | **Core** |
| 992 | [Subarrays With K Different Integers](https://leetcode.com/problems/subarrays-with-k-different-integers/) | Hard | _opt_ |
| 1004 | [Max Consecutive Ones Iii](https://leetcode.com/problems/max-consecutive-ones-iii/) | Medium | **Core** |
| 1208 | [Get Equal Substrings Within Budget](https://leetcode.com/problems/get-equal-substrings-within-budget/) | Medium | _opt_ |
| 1456 | [Maximum Number Of Vowels In A Substring Of Given Length](https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/) | Medium | _opt_ |
| 1493 | [Longest Subarray Of 1S After Deleting One Element](https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/) | Medium | _opt_ |
