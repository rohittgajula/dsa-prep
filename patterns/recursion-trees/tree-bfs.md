# Tree BFS (Level Order)

`Week 17` · Recursion & Trees

## Recognise it when

- Any problem containing the word **LEVEL**
- *"right side view"*, *"zigzag"*, *"minimum depth"*, *"maximum width"*

## The insight

A queue processes nodes in discovery order, which **is** level order.

Capturing the queue's **size at the top of each iteration** freezes one level — so you can group nodes by depth without storing depth on each node.

## Diagram

```
                (3)
               /    \
            (9)      (20)
                    /    \
                 (15)    (7)

  queue: [3]              size = 1  ── level 0 ──►  [3]
         pop 3, push 9, 20

  queue: [9, 20]          size = 2  ── level 1 ──►  [9, 20]
         pop 9  (no children)
         pop 20, push 15, 7

  queue: [15, 7]          size = 2  ── level 2 ──►  [15, 7]
         pop both, no children

  queue: []               done

  result: [[3], [9, 20], [15, 7]]

  ╔════════════════════════════════════════════════╗
  ║  size = len(q)  MUST be read BEFORE the inner  ║
  ║  loop. Reading it inside reads a GROWING queue ║
  ║  and merges every level into one.              ║
  ╚════════════════════════════════════════════════╝
```

## Template

```python
from collections import deque

def level_order(root) -> list[list[int]]:
    if not root:
        return []
    out, q = [], deque([root])
    while q:
        size = len(q)                 # FREEZE the level size
        level = []
        for _ in range(size):
            node = q.popleft()
            level.append(node.val)
            if node.left:  q.append(node.left)
            if node.right: q.append(node.right)
        out.append(level)
    return out
```

### Right side view — last node of each level

```python
def right_side_view(root) -> list[int]:
    if not root: return []
    out, q = [], deque([root])
    while q:
        size = len(q)
        for i in range(size):
            node = q.popleft()
            if i == size - 1:              # last in this level
                out.append(node.val)
            if node.left:  q.append(node.left)
            if node.right: q.append(node.right)
    return out
```

### Zigzag — reverse alternate levels

```python
def zigzag(root) -> list[list[int]]:
    if not root: return []
    out, q, ltr = [], deque([root]), True
    while q:
        level = []
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node.val)
            if node.left:  q.append(node.left)
            if node.right: q.append(node.right)
        out.append(level if ltr else level[::-1])
        ltr = not ltr
    return out
```

### Minimum depth — BFS beats DFS here

```python
def min_depth(root) -> int:
    if not root: return 0
    q, depth = deque([root]), 1
    while q:
        for _ in range(len(q)):
            node = q.popleft()
            if not node.left and not node.right:
                return depth                 # FIRST leaf found = shallowest
            if node.left:  q.append(node.left)
            if node.right: q.append(node.right)
        depth += 1
```

DFS would explore an entire deep branch before finding the shallow leaf. BFS returns immediately.

### Maximum width — heap-style indices

```python
def width_of_binary_tree(root) -> int:
    q, best = deque([(root, 0)]), 0
    while q:
        _, first = q[0]
        for _ in range(len(q)):
            node, idx = q.popleft()
            idx -= first                             # normalise to avoid overflow
            best = max(best, idx + 1)
            if node.left:  q.append((node.left, 2 * idx))
            if node.right: q.append((node.right, 2 * idx + 1))
    return best
```

## Complexity

O(n) time, O(w) space where `w` is the maximum width — up to n/2 for a full tree.

## Common mistakes

- Reading `len(q)` **inside** the inner loop
- Using DFS for minimum depth
- Not normalising indices in the width problem (overflows on deep trees in Java/C++)

## Problems

- [102. Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/) — Medium
- [199. Binary Tree Right Side View](https://leetcode.com/problems/binary-tree-right-side-view/) — Medium
- [103. Zigzag Level Order Traversal](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/) — Medium

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
