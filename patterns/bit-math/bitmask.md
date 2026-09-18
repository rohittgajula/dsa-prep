# Bitmask Enumeration & Bitmask DP

`Week 28` · Bit & Math

## Recognise it when

- **n is small** (roughly ≤ 20) and you need **all subsets**
- DP over *"which items have I already used"*

**The constraint is the signal.** `n <= 20` in the problem statement almost always means bitmask.

## The insight

With n ≤ 20 there are at most ~1 million subsets — tractable.

An integer's **bits ARE the subset**: bit `i` set means item `i` is included. That turns "set of used items" into a cheap integer DP key.

## Diagram

```
  n = 3, items [a, b, c]

  mask  binary   subset       mask & (1<<i) tests membership
  ────  ──────   ────────
   0     000     {}
   1     001     {a}          bit 0 → a
   2     010     {b}
   3     011     {a, b}
   4     100     {c}
   5     101     {a, c}
   6     110     {b, c}
   7     111     {a, b, c}

  2^3 = 8 subsets, counted simply by iterating 0..7


  Operations:

    set bit i        mask |  (1 << i)      001 → 011
    clear bit i      mask & ~(1 << i)      011 → 001
    test bit i       mask &  (1 << i)      != 0
    drop lowest set  mask & (mask - 1)     110 → 100
    count bits       bin(mask).count('1')
    iterate subsets  sub = (sub - 1) & mask
```

### Bitmask DP — travelling-salesman shape

```
  dp[mask][i] = best cost having visited exactly `mask`, currently at node i

                mask = 0011 (visited a and b), at b
                            │
                            ▼  extend to c
                mask = 0111 (visited a, b, c), at c

  transitions: for each unvisited j, dp[mask | 1<<j][j] = dp[mask][i] + cost(i,j)

  states: 2^n × n     transitions: n      →   O(2^n · n^2)
```

## Template — enumerate all subsets

```python
def subsets(nums: list[int]) -> list[list[int]]:
    n = len(nums)
    out = []
    for mask in range(1 << n):                     # 0 .. 2^n - 1
        out.append([nums[i] for i in range(n) if mask & (1 << i)])
    return out
```

### Shortest path visiting all nodes (LC 847) — BFS over (node, mask)

```python
from collections import deque

def shortest_path_length(graph: list[list[int]]) -> int:
    n = len(graph)
    full = (1 << n) - 1
    q = deque((i, 1 << i, 0) for i in range(n))    # start anywhere
    seen = {(i, 1 << i) for i in range(n)}
    while q:
        node, mask, dist = q.popleft()
        if mask == full:
            return dist
        for nxt in graph[node]:
            nmask = mask | (1 << nxt)
            if (nxt, nmask) not in seen:
                seen.add((nxt, nmask))
                q.append((nxt, nmask, dist + 1))
    return 0
```

The state is `(current node, set of visited nodes)` — revisiting a node is allowed, revisiting a *state* is not.

### Smallest sufficient team (LC 1125)

```python
def smallest_sufficient_team(req_skills: list[str], people: list[list[str]]) -> list[int]:
    idx = {s: i for i, s in enumerate(req_skills)}
    n = len(req_skills)
    masks = [sum(1 << idx[s] for s in p if s in idx) for p in people]

    dp = {0: []}                                   # skill mask → team
    for i, pm in enumerate(masks):
        if pm == 0:
            continue
        for have, team in list(dp.items()):
            combined = have | pm
            if combined == have:
                continue                           # this person adds nothing
            if combined not in dp or len(dp[combined]) > len(team) + 1:
                dp[combined] = team + [i]
    return dp[(1 << n) - 1]
```

### Iterate all sub-masks of a mask

```python
sub = mask
while sub:
    process(sub)
    sub = (sub - 1) & mask      # elegant: enumerates every subset of mask
```

Total work across all masks is O(3^n), not O(4^n).

## Complexity

| | |
|---|---|
| Enumerate subsets | O(2ⁿ · n) |
| Bitmask DP | O(2ⁿ · n²) typically |
| All sub-masks of all masks | O(3ⁿ) |

n ≤ 20 → about 1M states. n ≤ 12 for the n² variants.

## Common mistakes

- **Operator precedence in Python**: `mask & 1 << i` parses as `mask & (1 << i)` — correct here, but write the parentheses anyway; comparisons bite (`mask & (1<<i) != 0` parses wrongly)
- Forgetting the state includes both position *and* mask
- Using it when n is large — check the constraint first

## Problems

- [78. Subsets](https://leetcode.com/problems/subsets/) — Medium
- [1125. Smallest Sufficient Team](https://leetcode.com/problems/smallest-sufficient-team/) — Hard
- [847. Shortest Path Visiting All Nodes](https://leetcode.com/problems/shortest-path-visiting-all-nodes/) — Hard
