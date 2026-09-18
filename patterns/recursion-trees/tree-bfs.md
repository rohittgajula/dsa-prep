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
