# Graph BFS — Shortest Path (Unweighted)

`Week 21` · Graphs

## Recognise it when

- **Shortest** path or **minimum number of steps** in an **unweighted** graph

## The insight

BFS explores in order of distance, so **the first time you reach a node is guaranteed to be via a shortest path**.

DFS gives no such guarantee. This is the single most important reason to pick BFS.

## Diagram

```
  find the shortest path A → F

        A ─── B ─── C
        │     │     │
        D ─── E ─── F

  BFS expands in RINGS of equal distance:

    distance 0:  {A}
    distance 1:  {B, D}          ← everything 1 step from A
    distance 2:  {C, E}          ← everything 2 steps
    distance 3:  {F}             ← FOUND, and it must be optimal
                                   because ring 2 didn't contain it

         ┌───────── ring 2 ─────────┐
         │   ┌──── ring 1 ────┐     │
         │   │   ┌─ A ─┐      │     │
         │   │ B       D      │     │
         │  C           E     │     │
         │            F ◄─────┴─ ring 3
         └──────────────────────────┘
```

### Mark visited on PUSH, not on POP

```
        A
       / \
      B   C
       \ /
        D

  Marking on POP:
      queue: [A] → [B, C] → [C, D] → [D, D]   ← D queued TWICE
      On a dense graph this degrades exponentially.

  Marking on PUSH:
      D is marked the moment it is first queued → enters once.
```

## Template

```python
from collections import deque

def shortest_path(start, target, neighbours) -> int:
    q = deque([(start, 0)])
    seen = {start}
    while q:
        node, d = q.popleft()
        if node == target:
            return d
        for nxt in neighbours(node):
            if nxt not in seen:
                seen.add(nxt)          # mark on PUSH
                q.append((nxt, d + 1))
    return -1
```

### Level-by-level form (when you need the step count separately)

```python
def min_steps(start, target, neighbours) -> int:
    q, seen, steps = deque([start]), {start}, 0
    while q:
        for _ in range(len(q)):        # one full level = one step
            node = q.popleft()
            if node == target:
                return steps
            for nxt in neighbours(node):
                if nxt not in seen:
                    seen.add(nxt)
                    q.append(nxt)
        steps += 1
    return -1
```

### Word Ladder — bucket by wildcard to avoid O(n²)

```python
def ladder_length(begin: str, end: str, word_list: list[str]) -> int:
    words = set(word_list)
    if end not in words:
        return 0
    from collections import defaultdict
    buckets = defaultdict(list)
    L = len(begin)
    for w in words:
        for i in range(L):
            buckets[w[:i] + "*" + w[i+1:]].append(w)

    q, seen = deque([(begin, 1)]), {begin}
    while q:
        word, d = q.popleft()
        for i in range(L):
            for nxt in buckets[word[:i] + "*" + word[i+1:]]:
                if nxt == end:
                    return d + 1
                if nxt not in seen:
                    seen.add(nxt)
                    q.append((nxt, d + 1))
    return 0
```

Comparing every pair of words is O(n²·L). The wildcard buckets make neighbour lookup O(L).

## Complexity

O(V + E) time, O(V) space.

## Common mistakes

- **Marking visited on pop** instead of push
- Using DFS for a shortest-path question
- Forgetting BFS only gives shortest paths when **all edges cost the same**. Weighted → [Dijkstra](dijkstra.md).

## Problems

- [1091. Shortest Path in Binary Matrix](https://leetcode.com/problems/shortest-path-in-binary-matrix/) — Medium
- [127. Word Ladder](https://leetcode.com/problems/word-ladder/) — Hard
- [752. Open the Lock](https://leetcode.com/problems/open-the-lock/) — Medium

---

## All problems in this pattern

**Graph BFS/DFS** — 18 problems (10 core). Full list with dates and checkboxes: [`solutions/22-graph-bfs-dfs/`](../../solutions/22-graph-bfs-dfs/)

| # | Problem | Diff | Tier |
|---|---|---|---|
| 130 | [Surrounded Regions](https://leetcode.com/problems/surrounded-regions/) | Medium | **Core** |
| 133 | [Clone Graph](https://leetcode.com/problems/clone-graph/) | Medium | **Core** |
| 200 | [Number Of Islands](https://leetcode.com/problems/number-of-islands/) | Medium | **Core** |
| 329 | [Longest Increasing Path In A Matrix](https://leetcode.com/problems/longest-increasing-path-in-a-matrix/) | Hard | _opt_ |
| 417 | [Pacific Atlantic Water Flow](https://leetcode.com/problems/pacific-atlantic-water-flow/) | Medium | **Core** |
| 463 | [Island Perimeter](https://leetcode.com/problems/island-perimeter/) | Easy | _opt_ |
| 542 | [01 Matrix](https://leetcode.com/problems/01-matrix/) | Medium | **Core** |
| 547 | [Number Of Provinces](https://leetcode.com/problems/number-of-provinces/) | Medium | **Core** |
| 695 | [Max Area Of Island](https://leetcode.com/problems/max-area-of-island/) | Medium | **Core** |
| 733 | [Flood Fill](https://leetcode.com/problems/flood-fill/) | Easy | **Core** |
| 797 | [All Paths From Source To Target](https://leetcode.com/problems/all-paths-from-source-to-target/) | Medium | _opt_ |
| 841 | [Keys And Rooms](https://leetcode.com/problems/keys-and-rooms/) | Medium | _opt_ |
| 994 | [Rotting Oranges](https://leetcode.com/problems/rotting-oranges/) | Medium | **Core** |
| 1020 | [Number Of Enclaves](https://leetcode.com/problems/number-of-enclaves/) | Medium | _opt_ |
| 1091 | [Shortest Path In Binary Matrix](https://leetcode.com/problems/shortest-path-in-binary-matrix/) | Medium | **Core** |
| 1254 | [Number Of Closed Islands](https://leetcode.com/problems/number-of-closed-islands/) | Medium | _opt_ |
| 1926 | [Nearest Exit From Entrance In Maze](https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/) | Medium | _opt_ |
| 1971 | [Find If Path Exists In Graph](https://leetcode.com/problems/find-if-path-exists-in-graph/) | Easy | _opt_ |
