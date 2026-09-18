# Patterns

53 pattern guides. Each has: **how to recognise it → why it works → a diagram → template code → complexity → common mistakes → every problem in that pattern**.

**Read the guide before the first problem of a new pattern.** Then attempt cold.

## Arrays & Strings — `Weeks 1–10`

| Guide | Week |
|---|---|
| [Two Pointers — Opposite Ends](arrays-strings/two-pointers-opposite-ends.md) | 2 |
| [Two Pointers — Fast & Slow](arrays-strings/two-pointers-fast-slow.md) | 2 |
| [Dutch National Flag](arrays-strings/dutch-national-flag.md) | 2 |
| [Sliding Window — Fixed](arrays-strings/sliding-window-fixed.md) | 3 |
| [Sliding Window — Variable](arrays-strings/sliding-window-variable.md) | 3 |
| [Prefix Sum](arrays-strings/prefix-sum.md) | 4 |
| [Prefix Sum + HashMap](arrays-strings/prefix-sum-hashmap.md) | 4 |
| [Difference Array](arrays-strings/difference-array.md) | 4 |
| [Hashing](arrays-strings/hashing.md) | 5 |
| [Expand Around Centre](arrays-strings/expand-around-centre.md) | 6 |
| [In-place Index Marking](arrays-strings/in-place-index-marking.md) | 9 |
| [Merge Intervals / Sweep Line](arrays-strings/merge-intervals.md) | 10 |
| [Kadane's Algorithm](arrays-strings/kadane.md) | 1 |

## Search & Sort — `Weeks 7–9`

| Guide | Week |
|---|---|
| [Binary Search — Exact & Bounds](search-sort/binary-search.md) | 7 |
| [Binary Search on the Answer](search-sort/binary-search-on-answer.md) | 8 |
| [Cyclic Sort](search-sort/cyclic-sort.md) | 9 |
| [Quickselect](search-sort/quickselect.md) | 9 |
| [Merge Sort Counting](search-sort/merge-sort-counting.md) | 9 |

## Linear Structures — `Weeks 11–14`

| Guide | Week |
|---|---|
| [Linked List Reversal](linear-structures/linked-list-reversal.md) | 11 |
| [Dummy Node](linear-structures/dummy-node.md) | 11 |
| [Monotonic Stack](linear-structures/monotonic-stack.md) | 12 |
| [Monotonic Deque](linear-structures/monotonic-deque.md) | 13 |
| [Top-K with a Heap](linear-structures/heap-top-k.md) | 14 |
| [Two Heaps](linear-structures/two-heaps.md) | 14 |
| [K-Way Merge](linear-structures/k-way-merge.md) | 14 |

## Recursion & Trees — `Weeks 15–20`

| Guide | Week |
|---|---|
| [Backtracking](recursion-trees/backtracking.md) | 16 |
| [Tree DFS](recursion-trees/tree-dfs.md) | 17 |
| [Tree BFS](recursion-trees/tree-bfs.md) | 17 |
| [Lowest Common Ancestor](recursion-trees/lowest-common-ancestor.md) | 18 |
| [Tree Construction](recursion-trees/tree-construction.md) | 18 |
| [BST — Inorder Property](recursion-trees/bst-inorder.md) | 19 |
| [Trie](recursion-trees/trie.md) | 20 |

## Graphs — `Weeks 21–23`

| Guide | Week |
|---|---|
| [Graph DFS / Components](graphs/graph-dfs.md) | 21 |
| [Graph BFS — Shortest Path](graphs/graph-bfs.md) | 21 |
| [Multi-Source BFS](graphs/multi-source-bfs.md) | 21 |
| [Topological Sort](graphs/topological-sort.md) | 22 |
| [Union-Find](graphs/union-find.md) | 22 |
| [Dijkstra](graphs/dijkstra.md) | 23 |
| [Minimum Spanning Tree](graphs/minimum-spanning-tree.md) | 23 |

## Greedy & DP — `Weeks 24–27`

| Guide | Week |
|---|---|
| [Greedy — Interval Scheduling](greedy-dp/greedy-intervals.md) | 24 |
| [DP — 1D Linear](greedy-dp/dp-1d.md) | 24 |
| [DP — Knapsack](greedy-dp/dp-knapsack.md) | 25 |
| [DP — Grid](greedy-dp/dp-grid.md) | 25 |
| [DP — Two Strings](greedy-dp/dp-two-strings.md) | 26 |
| [DP — LIS](greedy-dp/dp-lis.md) | 26 |
| [DP — Interval](greedy-dp/dp-interval.md) | 27 |
| [DP — State Machine (Stocks)](greedy-dp/dp-state-machine.md) | 27 |
| [DP on Trees](greedy-dp/dp-on-trees.md) | 27 |

## Bit & Math — `Week 28`

| Guide |
|---|
| [XOR Tricks](bit-math/xor-tricks.md) |
| [Bitmask Enumeration & DP](bit-math/bitmask.md) |
| [Fast Exponentiation & Modular Arithmetic](bit-math/fast-exponentiation.md) |

## Design — `Week 29`

| Guide |
|---|
| [LRU / LFU Cache](design/lru-lfu-cache.md) |
| [O(1) Insert / Delete / GetRandom](design/o1-random-set.md) |

---

## The six that carry the most weight

1. **[Sliding window — variable](arrays-strings/sliding-window-variable.md)** — the shrink condition is the whole problem
2. **[Binary search on the answer](search-sort/binary-search-on-answer.md)** — high value, consistently under-practised
3. **[Monotonic stack](linear-structures/monotonic-stack.md)** — one template, 15+ problems
4. **[Backtracking](recursion-trees/backtracking.md)** — choose / explore / unchoose
5. **[Graph BFS](graphs/graph-bfs.md)** — first arrival = shortest path
6. **[DP knapsack](greedy-dp/dp-knapsack.md)** — the loop direction encodes reuse
