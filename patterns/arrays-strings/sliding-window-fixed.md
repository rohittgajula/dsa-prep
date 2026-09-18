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
