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
