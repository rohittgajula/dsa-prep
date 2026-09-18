# Sliding Window — Fixed Size

`Week 3` · Arrays & Strings

## Recognise it when

- *"Subarray / substring of size **exactly k**"*
- The window length never changes

## The insight

Consecutive windows overlap in `k-1` elements. Recomputing each from scratch is O(nk) and throws that overlap away. Instead **add the entering element and remove the leaving one** — O(1) per step.

## Diagram

```
k = 3

  [ 2   1   5 ] 1   3   2        sum = 8
    └───────┘
        ↓ slide right by one

    2 [ 1   5   1 ] 3   2        sum = 8 - 2 + 1 = 7
      └───────┘                        ▲      ▲
                                    drop a[i-k]  add a[i]

    2   1 [ 5   1   3 ] 2        sum = 7 - 1 + 3 = 9   ← best
          └───────┘
```

Each element enters once and leaves once → **O(n) total**, not O(nk).

## Template

```python
def max_sum_window(a: list[int], k: int) -> int:
    s = sum(a[:k])            # build the FIRST window before the loop
    best = s
    for i in range(k, len(a)):
        s += a[i] - a[i - k]  # add new, drop old
        best = max(best, s)
    return best
```

### With a frequency map (anagram / permutation checks)

```python
from collections import Counter

def find_anagrams(s: str, p: str) -> list[int]:
    if len(p) > len(s):
        return []
    need, win = Counter(p), Counter(s[:len(p)])
    res = [0] if win == need else []
    for i in range(len(p), len(s)):
        win[s[i]] += 1
        out = s[i - len(p)]
        win[out] -= 1
        if win[out] == 0:
            del win[out]      # keep the dict clean or == will fail
        if win == need:
            res.append(i - len(p) + 1)
    return res
```

## Complexity

O(n) time, O(1) space (or O(alphabet) with a frequency map).

## Common mistakes

- **Off-by-one on the first window.** Build `a[:k]` *before* the loop, then start at index `k`.
- Not deleting zero-count keys from the Counter — `win == need` then fails even when the contents match.

## Problems

- [643. Maximum Average Subarray I](https://leetcode.com/problems/maximum-average-subarray-i/) — Easy
- [219. Contains Duplicate II](https://leetcode.com/problems/contains-duplicate-ii/) — Easy
- [567. Permutation in String](https://leetcode.com/problems/permutation-in-string/) — Medium

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
