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
