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
