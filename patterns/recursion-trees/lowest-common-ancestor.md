# Lowest Common Ancestor

`Week 18` · Recursion & Trees

## Recognise it when

- *"Lowest common ancestor"*, *"nearest shared parent"*
- *"Distance between two nodes in a tree"* (LCA is the first half)

## The insight

**Post-order recursion.** If a node finds one target in its left subtree and the other in its right, that node **is** the LCA.

Otherwise it passes up whichever side found something. The first node where the two searches **converge** is the answer.

## Diagram

```
                (3)
               /    \
            (5)      (1)
           /   \    /   \
        (6)   (2) (0)   (8)
             /   \
          (7)    (4)

  LCA(7, 4):
      node 2: left returns 7, right returns 4
              BOTH non-null → node 2 IS the LCA ★

  LCA(5, 4):
      node 7 → None      node 4 → 4
      node 2: left=None, right=4  → pass up 4
      node 5: matches p itself     → return 5 immediately
      node 3: left=5, right=None   → pass up 5
      answer = 5   (a node can be its own ancestor)

  signal flowing UP:
          3          ← left=5, right=None → 5
        /   \
      5●     1       ← 5 matched, returns itself
     / \
    6   2            ← left=7●, right=4● → BOTH → LCA
       / \
      7●  4●
```

## Template

```python
def lowest_common_ancestor(root, p, q):
    if not root or root is p or root is q:
        return root                 # found one, or hit the bottom
    left  = lowest_common_ancestor(root.left,  p, q)
    right = lowest_common_ancestor(root.right, p, q)
    if left and right:
        return root                 # they SPLIT here → this is the LCA
    return left or right            # pass up whichever found something
```

Four lines. The elegance is that "found p or q" and "found the LCA" use the same return channel — and the `left and right` check distinguishes them.

### With parent pointers — becomes a linked-list intersection

```python
def lca_with_parents(p, q):
    a, b = p, q
    while a is not b:
        a = a.parent if a else q      # swap to the other list on hitting the top
        b = b.parent if b else p
    return a
```

### Distance between two nodes

```python
def distance(root, p, q) -> int:
    lca = lowest_common_ancestor(root, p, q)
    def depth(node, target, d=0):
        if not node: return -1
        if node is target: return d
        left = depth(node.left, target, d + 1)
        return left if left != -1 else depth(node.right, target, d + 1)
    return depth(lca, p) + depth(lca, q)
```

## Complexity

O(n) time, O(h) space. **In a BST use the O(h) descent instead** — see [bst-inorder.md](bst-inorder.md).

## Common mistakes

- Using this on a BST when the O(h) version applies
- Assuming both nodes exist. If one might be absent you need an explicit found-flag, otherwise you return the present node incorrectly.
- Forgetting a node can be its own ancestor

## Problems

- [236. LCA of a Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/) — Medium
- [235. LCA of a BST](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/) — Medium
- [1123. LCA of Deepest Leaves](https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/) — Medium

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
