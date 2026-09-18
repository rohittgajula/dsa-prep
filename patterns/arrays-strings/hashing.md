# Hashing / Frequency Map

`Week 5` · Arrays & Strings

## Recognise it when

- *anagram*, *duplicate*, *group by*, *count occurrences*, *have I seen this before*
- **Any time you are about to write a nested loop to search**

## The insight

A hash map turns *"search the collection"* from O(n) into O(1), collapsing a nested loop into a single pass.

The creative part is never the map — it is **choosing the key**. You want a *canonical form* that makes equivalent things collide deliberately.

## Diagram

```
  Group anagrams: ["eat", "tea", "tan", "ate", "nat", "bat"]

  word    canonical key        bucket
  ─────   ──────────────       ────────────────
  eat  →  sorted = "aet"   →   ┌─ "aet" ──────────┐
  tea  →  sorted = "aet"   →   │ eat, tea, ate    │
  ate  →  sorted = "aet"   →   └──────────────────┘
  tan  →  sorted = "ant"   →   ┌─ "ant" ──────────┐
  nat  →  sorted = "ant"   →   │ tan, nat         │
                               └──────────────────┘
  bat  →  sorted = "abt"   →   ┌─ "abt" ──────────┐
                               │ bat              │
                               └──────────────────┘

  Two key choices:
    sorted(word)       O(L log L)  - simple, fine for short words
    26-length count    O(L)        - faster for long words
```

## Template

```python
from collections import defaultdict, Counter

# frequency
freq = Counter(nums)

# grouping by a canonical key
groups = defaultdict(list)
for word in words:
    key = tuple(sorted(word))          # or the count tuple below
    groups[key].append(word)

# O(L) key instead of O(L log L)
def count_key(word: str) -> tuple:
    c = [0] * 26
    for ch in word:
        c[ord(ch) - ord('a')] += 1
    return tuple(c)                    # tuple - lists are unhashable
```

### Longest consecutive sequence — the O(n) trick

```python
def longest_consecutive(nums: list[int]) -> int:
    s = set(nums)
    best = 0
    for x in s:
        if x - 1 in s:
            continue                   # not a sequence START - skip
        length = 1
        while x + length in s:
            length += 1
        best = max(best, length)
    return best
```

> The `if x - 1 in s: continue` guard is what keeps this O(n). Without it, every element walks its whole run and you get O(n²).

## Complexity

O(n) time, O(n) space. Worst-case O(n) per lookup with adversarial hash collisions — irrelevant in interviews, worth knowing.

## Common mistakes

- **Lists are unhashable** in Python — convert to `tuple`
- Using `sorted()` as the key on long strings when a count tuple is O(L)
- Forgetting the "is this a sequence start" guard in LC 128

## Problems

- [242. Valid Anagram](https://leetcode.com/problems/valid-anagram/) — Easy
- [49. Group Anagrams](https://leetcode.com/problems/group-anagrams/) — Medium
- [128. Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/) — Medium
