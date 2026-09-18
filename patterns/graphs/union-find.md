# Union-Find (Disjoint Set Union)

`Week 22` · Graphs

## Recognise it when

- Connectivity, grouping, *"are these two connected"*
- Merging accounts, redundant edge, Kruskal's MST

## The insight

Each set is a **tree** with a representative root.

**Path compression** flattens those trees on every `find`, and **union by rank** keeps them shallow. Together they make operations effectively **O(1) amortised** — formally O(α(n)), the inverse Ackermann function, which is under 5 for any n you will ever see.

## Diagram

```
  union(1,2), union(3,4), union(2,4)

  start:   1   2   3   4         each is its own root
           ●   ●   ●   ●

  union(1,2):      2             union(3,4):      4
                   │                              │
                   1                              3

  union(2,4):      4             attach one root to the other
                  / \
                 2   3
                 │
                 1

  find(1) WITHOUT compression:  1 → 2 → 4      3 hops
  find(1) WITH compression:     1 ──────► 4    and 1 now points
                                             DIRECTLY at 4 forever

  after compression:     4
                       / | \
                      2  3  1        depth 1 - every later find is O(1)
```

### Cycle detection is free

```
  union(u, v) returns False  ⟺  u and v were ALREADY connected
                             ⟺  adding this edge CLOSES A CYCLE

  That single fact IS the answer to "Redundant Connection".
```

## Template

```python
class DSU:
    def __init__(self, n: int):
        self.p = list(range(n))
        self.rank = [0] * n
        self.count = n                 # number of components

    def find(self, x: int) -> int:
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]   # path compression (halving)
            x = self.p[x]
        return x

    def union(self, a: int, b: int) -> bool:
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False               # already connected → cycle
        if self.rank[ra] < self.rank[rb]:
            ra, rb = rb, ra
        self.p[rb] = ra                # attach the shorter tree under the taller
        if self.rank[ra] == self.rank[rb]:
            self.rank[ra] += 1
        self.count -= 1
        return True
```

### Redundant connection — four lines of logic

```python
def find_redundant_connection(edges: list[list[int]]) -> list[int]:
    dsu = DSU(len(edges) + 1)
    for u, v in edges:
        if not dsu.union(u, v):
            return [u, v]              # this edge closed the cycle
    return []
```

### Accounts merge — the canonical DSU application

```python
def accounts_merge(accounts: list[list[str]]) -> list[list[str]]:
    dsu = DSU(len(accounts))
    email_to_id: dict[str, int] = {}
    for i, acc in enumerate(accounts):
        for email in acc[1:]:
            if email in email_to_id:
                dsu.union(i, email_to_id[email])   # shared email → same person
            else:
                email_to_id[email] = i

    from collections import defaultdict
    groups = defaultdict(list)
    for email, i in email_to_id.items():
        groups[dsu.find(i)].append(email)

    return [[accounts[i][0]] + sorted(emails) for i, emails in groups.items()]
```

## Complexity

| Operation | Cost |
|---|---|
| find / union | **O(α(n)) ≈ O(1)** amortised |
| Without path compression | O(n) worst case |

## Common mistakes

- **Omitting path compression** → degenerates to a linked list, O(n) per find
- Not using the `union` return value for cycle detection
- Expecting DSU to handle **deletions** — it cannot. It only ever merges.

## Problems

- [684. Redundant Connection](https://leetcode.com/problems/redundant-connection/) — Medium
- [721. Accounts Merge](https://leetcode.com/problems/accounts-merge/) — Medium
- [1584. Min Cost to Connect All Points](https://leetcode.com/problems/min-cost-to-connect-all-points/) — Medium

---

## All problems in this pattern

**Union-Find** — 6 problems (2 core). Full list with dates and checkboxes: [`solutions/25-union-find/`](../../solutions/25-union-find/)

| # | Problem | Diff | Tier |
|---|---|---|---|
| 684 | [Redundant Connection](https://leetcode.com/problems/redundant-connection/) | Medium | **Core** |
| 685 | [Redundant Connection Ii](https://leetcode.com/problems/redundant-connection-ii/) | Hard | _opt_ |
| 721 | [Accounts Merge](https://leetcode.com/problems/accounts-merge/) | Medium | **Core** |
| 839 | [Similar String Groups](https://leetcode.com/problems/similar-string-groups/) | Hard | _opt_ |
| 990 | [Satisfiability Of Equality Equations](https://leetcode.com/problems/satisfiability-of-equality-equations/) | Medium | _opt_ |
| 1319 | [Number Of Operations To Make Network Connected](https://leetcode.com/problems/number-of-operations-to-make-network-connected/) | Medium | _opt_ |
