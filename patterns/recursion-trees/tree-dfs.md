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

---

## All problems in this pattern

**Binary Tree** — 36 problems (21 core). Full list with dates and checkboxes: [`solutions/19-binary-tree/`](../../solutions/19-binary-tree/)

| # | Problem | Diff | Tier |
|---|---|---|---|
| 94 | [Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/) | Easy | **Core** |
| 100 | [Same Tree](https://leetcode.com/problems/same-tree/) | Easy | **Core** |
| 101 | [Symmetric Tree](https://leetcode.com/problems/symmetric-tree/) | Easy | **Core** |
| 102 | [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/) | Medium | **Core** |
| 103 | [Binary Tree Zigzag Level Order Traversal](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/) | Medium | **Core** |
| 107 | [Binary Tree Level Order Traversal Ii](https://leetcode.com/problems/binary-tree-level-order-traversal-ii/) | Medium | _opt_ |
| 110 | [Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/) | Easy | **Core** |
| 111 | [Minimum Depth Of Binary Tree](https://leetcode.com/problems/minimum-depth-of-binary-tree/) | Easy | _opt_ |
| 116 | [Populating Next Right Pointers In Each Node](https://leetcode.com/problems/populating-next-right-pointers-in-each-node/) | Medium | **Core** |
| 117 | [Populating Next Right Pointers In Each Node Ii](https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/) | Medium | _opt_ |
| 144 | [Binary Tree Preorder Traversal](https://leetcode.com/problems/binary-tree-preorder-traversal/) | Easy | **Core** |
| 145 | [Binary Tree Postorder Traversal](https://leetcode.com/problems/binary-tree-postorder-traversal/) | Easy | _opt_ |
| 199 | [Binary Tree Right Side View](https://leetcode.com/problems/binary-tree-right-side-view/) | Medium | **Core** |
| 222 | [Count Complete Tree Nodes](https://leetcode.com/problems/count-complete-tree-nodes/) | Easy | _opt_ |
| 515 | [Find Largest Value In Each Tree Row](https://leetcode.com/problems/find-largest-value-in-each-tree-row/) | Medium | _opt_ |
| 543 | [Diameter Of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/) | Easy | **Core** |
| 572 | [Subtree Of Another Tree](https://leetcode.com/problems/subtree-of-another-tree/) | Easy | **Core** |
| 617 | [Merge Two Binary Trees](https://leetcode.com/problems/merge-two-binary-trees/) | Easy | _opt_ |
| 637 | [Average Of Levels In Binary Tree](https://leetcode.com/problems/average-of-levels-in-binary-tree/) | Easy | _opt_ |
| 662 | [Maximum Width Of Binary Tree](https://leetcode.com/problems/maximum-width-of-binary-tree/) | Medium | _opt_ |
| 105 | [Construct Binary Tree From Preorder And Inorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/) | Medium | **Core** |
| 106 | [Construct Binary Tree From Inorder And Postorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/) | Medium | **Core** |
| 112 | [Path Sum](https://leetcode.com/problems/path-sum/) | Easy | **Core** |
| 113 | [Path Sum Ii](https://leetcode.com/problems/path-sum-ii/) | Medium | **Core** |
| 114 | [Flatten Binary Tree To Linked List](https://leetcode.com/problems/flatten-binary-tree-to-linked-list/) | Medium | **Core** |
| 124 | [Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/) | Hard | **Core** |
| 129 | [Sum Root To Leaf Numbers](https://leetcode.com/problems/sum-root-to-leaf-numbers/) | Medium | _opt_ |
| 236 | [Lowest Common Ancestor Of A Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/) | Medium | **Core** |
| 257 | [Binary Tree Paths](https://leetcode.com/problems/binary-tree-paths/) | Easy | _opt_ |
| 297 | [Serialize And Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/) | Hard | **Core** |
| 437 | [Path Sum Iii](https://leetcode.com/problems/path-sum-iii/) | Medium | **Core** |
| 863 | [All Nodes Distance K In Binary Tree](https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/) | Medium | **Core** |
| 889 | [Construct Binary Tree From Preorder And Postorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/) | Medium | _opt_ |
| 987 | [Vertical Order Traversal Of A Binary Tree](https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/) | Hard | _opt_ |
| 1123 | [Lowest Common Ancestor Of Deepest Leaves](https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/) | Medium | _opt_ |
| 1372 | [Longest Zigzag Path In A Binary Tree](https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/) | Medium | _opt_ |
