# Expand Around Centre

`Week 6` · Arrays & Strings

## Recognise it when

- **Palindromic** substrings — longest, or count them all

## The insight

Every palindrome has a **centre**. There are only `2n − 1` possible centres — `n` single characters (odd length) and `n − 1` gaps between characters (even length).

Growing outward from each centre is O(n), so the whole thing is **O(n²) time with O(1) space** — better than the O(n²) space DP formulation.

## Diagram

```
  s = "babad"

  ODD centres (on a character)          EVEN centres (between characters)
  ────────────────────────────          ─────────────────────────────────
   b a b a d                             b a b a d
   ^                                      ^
   centre 0 → "b"                         centre 0|1 → "ba" ✗ stop

   b a b a d                             b a b a d
     ^                                      ^
     centre 1 → "a"  → "bab" ★               centre 1|2 → "ab" ✗ stop
       ←  →
     expand while s[l] == s[r]

  Expansion from centre 1:
      l=1 r=1   "a"          s[1]==s[1] ✓ → l=0 r=2
      l=0 r=2   "bab"        s[0]=='b' == s[2]=='b' ✓ → l=-1 r=3
      l=-1      out of bounds → stop, length = r - l - 1 = 3 - (-1) - 1 = 3
```

> **Forgetting the even centres is the single most common bug here.**

## Template

```python
def longest_palindrome(s: str) -> str:
    if not s:
        return ""
    start = end = 0

    def expand(l: int, r: int) -> tuple[int, int]:
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return l + 1, r - 1          # both overshot by one

    for i in range(len(s)):
        l1, r1 = expand(i, i)        # odd  length
        if r1 - l1 > end - start:
            start, end = l1, r1
        l2, r2 = expand(i, i + 1)    # even length
        if r2 - l2 > end - start:
            start, end = l2, r2

    return s[start:end + 1]
```

### Counting them all

```python
def count_substrings(s: str) -> int:
    total = 0
    def expand(l: int, r: int) -> int:
        n = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            n += 1
            l -= 1
            r += 1
        return n
    for i in range(len(s)):
        total += expand(i, i) + expand(i, i + 1)
    return total
```

## Complexity

O(n²) time, **O(1) space**. Manacher's algorithm does it in O(n) but is rarely expected.

## Common mistakes

- **Only handling odd-length centres**
- Off-by-one after the loop — `l` and `r` have each overshot by one
- Building substrings inside the loop instead of tracking indices (turns it O(n³))

## Problems

- [5. Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/) — Medium
- [647. Palindromic Substrings](https://leetcode.com/problems/palindromic-substrings/) — Medium
- [680. Valid Palindrome II](https://leetcode.com/problems/valid-palindrome-ii/) — Easy
