# DP on Trees

`Week 27` · Greedy & DP

## Recognise it when

- *"Maximum sum in a tree with constraints"*
- *"House robber on a tree"*, *"binary tree cameras"*

## The insight

Post-order DFS where each node returns a **TUPLE of answers** — one per state.

The parent combines its children's tuples. It is 1D DP applied along **tree edges** instead of array indices.

**Trying to collapse the return to a single number is why people get stuck here.**

## Diagram

```
  House Robber III - cannot rob a node AND its direct child

                (3)
               /   \
            (2)     (3)
              \        \
              (3)      (1)

  Each node returns (rob_this, skip_this):

      rob  = node.val + left.skip + right.skip    children MUST be skipped
      skip = max(left) + max(right)               children free to choose

  leaf (3):   rob=3, skip=0   →  (3, 0)
  leaf (1):   rob=1, skip=0   →  (1, 0)

  node (2):   rob  = 2 + 0        = 2       (child 3 must be skipped)
              skip = max(3,0)     = 3       (child free → robs 3)
              → (2, 3)

  node (3)R:  rob  = 3 + 0        = 3
              skip = max(1,0)     = 1
              → (3, 1)

  root (3):   rob  = 3 + skip(2) + skip(3R) = 3 + 3 + 1 = 7  ★
              skip = max(2,3) + max(3,1)    = 3 + 3     = 6
              → answer = max(7, 6) = 7

  ╔═══════════════════════════════════════════════════════╗
  ║ Take the max ONLY at the very end, at the root.       ║
  ║ Taking it early loses the information the parent needs║
  ╚═══════════════════════════════════════════════════════╝
```

## Template

```python
def tree_dp(root) -> int:
    def dfs(node) -> tuple[int, int]:
        if not node:
            return (0, 0)                      # (take, skip)
        l = dfs(node.left)
        r = dfs(node.right)
        take = node.val + l[1] + r[1]          # children must be skipped
        skip = max(l) + max(r)                 # children choose freely
        return (take, skip)
    return max(dfs(root))                      # decide only at the root
```

### Binary Tree Cameras — greedy post-order, three states

```python
def min_camera_cover(root) -> int:
    NEEDS_COVER, HAS_CAMERA, COVERED = 0, 1, 2
    cameras = 0

    def dfs(node) -> int:
        nonlocal cameras
        if not node:
            return COVERED                     # None is trivially covered
        l, r = dfs(node.left), dfs(node.right)
        if l == NEEDS_COVER or r == NEEDS_COVER:
            cameras += 1                       # a child is exposed - must place here
            return HAS_CAMERA
        if l == HAS_CAMERA or r == HAS_CAMERA:
            return COVERED                     # a child's camera covers me
        return NEEDS_COVER                     # both children covered but not by me

    if dfs(root) == NEEDS_COVER:
        cameras += 1                           # the root itself is exposed
    return cameras
```

The greedy works because placing cameras as high as possible (at parents of leaves) always dominates.

### Tree diameter — same return/record split as [tree-dfs](../recursion-trees/tree-dfs.md)

```python
def diameter(root) -> int:
    best = 0
    def depth(node) -> int:
        nonlocal best
        if not node:
            return 0
        l, r = depth(node.left), depth(node.right)
        best = max(best, l + r)        # RECORD: the path through this node
        return 1 + max(l, r)           # RETURN: one side only
    depth(root)
    return best
```

## Complexity

O(n) time, O(h) stack space.

## Common mistakes

- **Returning a single value** instead of a state tuple
- Taking `max` at every node instead of only at the root
- Getting the base case wrong — for `None`, "covered" and "skip = 0" are the identity values

## Problems

- [337. House Robber III](https://leetcode.com/problems/house-robber-iii/) — Medium
- [124. Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/) — Hard
- [968. Binary Tree Cameras](https://leetcode.com/problems/binary-tree-cameras/) — Hard

---

## All problems in this pattern

**DP Tree** — 2 problems (1 core). Full list with dates and checkboxes: [`solutions/38-dp-tree/`](../../solutions/38-dp-tree/)

| # | Problem | Diff | Tier |
|---|---|---|---|
| 337 | [House Robber Iii](https://leetcode.com/problems/house-robber-iii/) | Medium | **Core** |
| 968 | [Binary Tree Cameras](https://leetcode.com/problems/binary-tree-cameras/) | Hard | _opt_ |
