# Trie (Prefix Tree)

`Week 20` · Recursion & Trees

## Recognise it when

- **Prefix** matching, autocomplete, dictionary / wildcard search
- Maximising **XOR** (a binary trie over bits)

## The insight

Shared prefixes are stored **exactly once**, so lookup cost depends on **word length**, not dictionary size.

Combining a trie with grid DFS lets you prune whole search branches the moment a prefix cannot exist — that is what makes Word Search II tractable.

## Diagram

```
  insert: "cat", "car", "card", "dog"

                    (root)
                   /      \
                 c          d
                 │          │
                 a          o
                / \         │
               t   r        g■
               ■   │■
                   d■          ■ = is_end (a complete word)

  "car" and "card" share the path c→a→r   ← stored once
  "cat" and "car" share c→a                ← stored once

  search("ca")  → reaches node 'a', is_end == False → not a WORD
  prefix("ca")  → reaches node 'a'                  → prefix EXISTS  ✓

  ╔═══════════════════════════════════════════════════╗
  ║ Without is_end, "ca" would match as a word simply ║
  ║ because the path exists. The flag is not optional.║
  ╚═══════════════════════════════════════════════════╝
```

## Template

```python
class TrieNode:
    def __init__(self):
        self.kids: dict[str, TrieNode] = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for ch in word:
            cur = cur.kids.setdefault(ch, TrieNode())
        cur.is_end = True

    def _walk(self, s: str) -> TrieNode | None:
        cur = self.root
        for ch in s:
            if ch not in cur.kids:
                return None
            cur = cur.kids[ch]
        return cur

    def search(self, word: str) -> bool:
        node = self._walk(word)
        return node is not None and node.is_end

    def startsWith(self, prefix: str) -> bool:
        return self._walk(prefix) is not None
```

### Wildcard search — `.` forces a DFS across all children

```python
def search_wildcard(self, word: str) -> bool:
    def dfs(i: int, node: TrieNode) -> bool:
        if i == len(word):
            return node.is_end
        ch = word[i]
        if ch == ".":
            return any(dfs(i + 1, child) for child in node.kids.values())
        return ch in node.kids and dfs(i + 1, node.kids[ch])
    return dfs(0, self.root)
```

### Word Search II — trie + grid DFS, one pass

Searching each word separately is O(words × cells × 4^L) and times out. Insert every word into a trie, then walk the grid **once**, pruning wherever the prefix leaves the trie:

```python
def find_words(board: list[list[str]], words: list[str]) -> list[str]:
    root = TrieNode()
    for w in words:
        cur = root
        for ch in w:
            cur = cur.kids.setdefault(ch, TrieNode())
        cur.word = w                       # store the word at its end node

    R, C, out = len(board), len(board[0]), []

    def dfs(r: int, c: int, node: TrieNode):
        ch = board[r][c]
        if ch not in node.kids:
            return                          # PRUNE - no word has this prefix
        nxt = node.kids[ch]
        if getattr(nxt, "word", None):
            out.append(nxt.word)
            nxt.word = None                 # de-duplicate
        board[r][c] = "#"                   # mark visited
        for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C and board[nr][nc] != "#":
                dfs(nr, nc, nxt)
        board[r][c] = ch                    # restore

    for r in range(R):
        for c in range(C):
            dfs(r, c, root)
    return out
```

### Binary trie for maximum XOR

```
  To maximise a XOR, at each bit prefer the OPPOSITE bit:

      want bit 1 of x = 1 → walk toward a stored 0
                           (1 XOR 0 = 1, the best possible for this bit)

  Greedy from the most significant bit down is optimal, because a higher
  bit outweighs every lower bit combined.
```

## Complexity

| | |
|---|---|
| insert / search / prefix | **O(L)**, L = word length |
| Space | O(total characters × alphabet) |

## Common mistakes

- **Omitting `is_end`** — prefixes match as complete words
- Per-word grid search instead of one trie-driven pass (TLE on Word Search II)
- Not restoring the board cell after the DFS

## Problems

- [208. Implement Trie](https://leetcode.com/problems/implement-trie-prefix-tree/) — Medium
- [211. Design Add and Search Words](https://leetcode.com/problems/design-add-and-search-words-data-structure/) — Medium
- [212. Word Search II](https://leetcode.com/problems/word-search-ii/) — Hard

---

## All problems in this pattern

**Trie** — 11 problems (5 core). Full list with dates and checkboxes: [`solutions/21-trie/`](../../solutions/21-trie/)

| # | Problem | Diff | Tier |
|---|---|---|---|
| 208 | [Implement Trie Prefix Tree](https://leetcode.com/problems/implement-trie-prefix-tree/) | Medium | **Core** |
| 211 | [Design Add And Search Words Data Structure](https://leetcode.com/problems/design-add-and-search-words-data-structure/) | Medium | **Core** |
| 212 | [Word Search Ii](https://leetcode.com/problems/word-search-ii/) | Hard | **Core** |
| 421 | [Maximum Xor Of Two Numbers In An Array](https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/) | Medium | **Core** |
| 472 | [Concatenated Words](https://leetcode.com/problems/concatenated-words/) | Hard | _opt_ |
| 648 | [Replace Words](https://leetcode.com/problems/replace-words/) | Medium | _opt_ |
| 676 | [Implement Magic Dictionary](https://leetcode.com/problems/implement-magic-dictionary/) | Medium | _opt_ |
| 677 | [Map Sum Pairs](https://leetcode.com/problems/map-sum-pairs/) | Medium | _opt_ |
| 745 | [Prefix And Suffix Search](https://leetcode.com/problems/prefix-and-suffix-search/) | Hard | _opt_ |
| 1268 | [Search Suggestions System](https://leetcode.com/problems/search-suggestions-system/) | Medium | **Core** |
| 1707 | [Maximum Xor With An Element From Array](https://leetcode.com/problems/maximum-xor-with-an-element-from-array/) | Hard | _opt_ |
