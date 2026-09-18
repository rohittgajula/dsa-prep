# Tree Construction from Traversals

`Week 18` · Recursion & Trees

## Recognise it when

- *"Build the tree from preorder and inorder"* (or inorder + postorder)
- Serialize / deserialize

## The insight

**Preorder's first element is always the ROOT.** Finding that value in the inorder array **splits it** into exactly the left and right subtrees.

Recurse on those halves. A hashmap of value → inorder index removes the O(n) search, taking the whole thing from O(n²) to O(n).

## Diagram

```
  preorder = [3, 9, 20, 15, 7]
  inorder  = [9, 3, 15, 20, 7]

  preorder[0] = 3 = ROOT
  find 3 in inorder at index 1:

  inorder:  [ 9 ] 3 [ 15, 20, 7 ]
             └┬┘     └─────┬────┘
          LEFT (1)     RIGHT (3)
           subtree      subtree

  So the preorder splits the same way:
  preorder: 3 [ 9 ] [ 20, 15, 7 ]
              └┬┘    └─────┬────┘
            1 node       3 nodes

  Recurse:
                (3)
               /    \
             (9)    build([20,15,7], [15,20,7])
                         ↓
                        (20)
                       /    \
                    (15)    (7)
```

**Inorder alone cannot rebuild a tree** — many shapes share one inorder sequence. You always need two traversals.

## Template

```python
def build_tree(preorder: list[int], inorder: list[int]):
    idx = {v: i for i, v in enumerate(inorder)}     # O(1) lookup
    self_pre = 0

    def build(lo: int, hi: int):
        nonlocal self_pre
        if lo > hi:
            return None
        root_val = preorder[self_pre]
        self_pre += 1
        root = TreeNode(root_val)
        mid = idx[root_val]
        root.left  = build(lo, mid - 1)     # LEFT first - preorder order
        root.right = build(mid + 1, hi)
        return root

    return build(0, len(inorder) - 1)
```

The moving `self_pre` pointer avoids all the index arithmetic. Building left before right is what keeps it aligned with preorder.

### Inorder + postorder — root is the LAST element, build RIGHT first

```python
def build_from_post(inorder: list[int], postorder: list[int]):
    idx = {v: i for i, v in enumerate(inorder)}
    post = len(postorder) - 1

    def build(lo: int, hi: int):
        nonlocal post
        if lo > hi:
            return None
        root = TreeNode(postorder[post]); post -= 1
        mid = idx[root.val]
        root.right = build(mid + 1, hi)   # RIGHT first - postorder is reversed
        root.left  = build(lo, mid - 1)
        return root

    return build(0, len(inorder) - 1)
```

### Serialize / deserialize — preorder with null markers

```python
def serialize(root) -> str:
    out = []
    def dfs(node):
        if not node:
            out.append("#"); return      # explicit null marker
        out.append(str(node.val))
        dfs(node.left); dfs(node.right)
    dfs(root)
    return ",".join(out)

def deserialize(data: str):
    vals = iter(data.split(","))
    def build():
        v = next(vals)
        if v == "#":
            return None
        node = TreeNode(int(v))
        node.left  = build()
        node.right = build()
        return node
    return build()
```

The null markers are what make it unambiguous — without them you are back to needing two traversals.

## Complexity

O(n) time with the hashmap (O(n²) without), O(n) space.

## Common mistakes

- Building right before left in the preorder version
- Recomputing `index()` inside the recursion → O(n²)
- Omitting null markers in serialize, making the output ambiguous

## Problems

- [105. Construct from Preorder and Inorder](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/) — Medium
- [106. Construct from Inorder and Postorder](https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/) — Medium
- [297. Serialize and Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/) — Hard

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
