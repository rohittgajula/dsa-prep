# Tree DFS (Recursive)

`Week 17` · Recursion & Trees

## Recognise it when

- Paths, depth, subtree properties
- *"Compute a value for each node from its children"*

## The insight

A tree is defined recursively, so recursion mirrors its structure exactly.

The discipline that matters: decide **what each call RETURNS UP** to its parent, and **what state you pass DOWN** as arguments. Most tree bugs are confusion between those two.

## Diagram

```
  Maximum path sum - the classic return-vs-record split

                 ┌─── the value you RECORD as the answer
                 │    may SPLIT through this node:
                 │    left + node + right
                 ▼
                (10)
               /    \
            (9)      (20)
                    /    \
                 (15)    (7)

    at node 20:
        returns UP:  20 + max(15, 7) = 35     ← a ONE-SIDED path
                     the parent can only extend through one child
        records:     15 + 20 + 7   = 42       ← the SPLIT path
                     valid as an answer but NOT usable by the parent

  ══════════════════════════════════════════════════
   return  ≠  record.  Conflating them is THE classic bug.
  ══════════════════════════════════════════════════
```

## Template

```python
def dfs(node):
    if not node:
        return base_case
    left  = dfs(node.left)
    right = dfs(node.right)
    return combine(node.val, left, right)
```

### Max path sum — return one side, record the split

```python
def max_path_sum(root) -> int:
    best = float('-inf')

    def gain(node) -> int:
        nonlocal best
        if not node:
            return 0
        l = max(gain(node.left), 0)     # clamp negatives to 0 - drop that branch
        r = max(gain(node.right), 0)
        best = max(best, node.val + l + r)   # RECORD the split
        return node.val + max(l, r)          # RETURN one side only

    gain(root)
    return best
```

### Diameter — same shape

```python
def diameter(root) -> int:
    best = 0
    def height(node) -> int:
        nonlocal best
        if not node:
            return 0
        l, r = height(node.left), height(node.right)
        best = max(best, l + r)     # record: edges through this node
        return 1 + max(l, r)        # return: height to the parent
    height(root)
    return best
```

### Passing state DOWN — path sum

```python
def has_path_sum(root, target: int) -> bool:
    if not root:
        return False
    if not root.left and not root.right:        # LEAF
        return target == root.val
    rem = target - root.val                     # state flows DOWN
    return has_path_sum(root.left, rem) or has_path_sum(root.right, rem)
```

> A node with **one** child is not a leaf. `min_depth` gets this wrong constantly.

## Complexity

O(n) time, O(h) stack space — O(log n) balanced, **O(n) worst case** (a degenerate list).

Python's default recursion limit is 1000. On a 10⁵-node skewed tree you must go iterative or raise the limit.

## Common mistakes

- **Returning the split path** — the parent cannot use it
- Forgetting to clamp negative child gains to 0
- Treating a one-child node as a leaf

## Problems

- [104. Maximum Depth](https://leetcode.com/problems/maximum-depth-of-binary-tree/) — Easy
- [543. Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/) — Easy
- [124. Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/) — Hard
