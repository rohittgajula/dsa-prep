# BST — The Inorder Property

`Week 19` · Recursion & Trees

## Recognise it when

- It is a Binary **SEARCH** Tree
- Validate, kth smallest, LCA, range sum, find mode

## The insight

**Inorder traversal of a BST yields values in SORTED order.**

That one fact converts most BST problems into array problems you already know. And search is just binary search on a tree — O(h).

## Diagram

```
                (5)
               /    \
            (3)      (8)
           /   \    /   \
        (2)   (4) (7)   (9)

  inorder = left, node, right:

    2 → 3 → 4 → 5 → 7 → 8 → 9
    └──────── SORTED ────────┘

  So "kth smallest" = stop at the kth visit.
  So "validate"     = check the sequence is strictly increasing.
```

### Validation needs a RANGE, not a local check

```
  This tree passes a naive parent-vs-child check but is NOT a BST:

                (5)
               /    \
            (3)      (8)
                    /   \
                 (4)    (9)
                  ▲
          4 < 8 ✓ (local check passes)
          but 4 is in the RIGHT subtree of 5, so it must be > 5   ✗

  Every node carries an allowed interval:
                (5)          (-inf, +inf)
               /    \
     (-inf, 5) (3)   (8) (5, +inf)
                    /
              (5,8) (4)   ← 4 not in (5,8)  →  INVALID
```

## Template

```python
def inorder(node, visit) -> None:
    if not node:
        return
    inorder(node.left, visit)
    visit(node)                  # values arrive SORTED
    inorder(node.right, visit)
```

### Validate — pass the range down

```python
def is_valid_bst(root) -> bool:
    def check(node, lo=float('-inf'), hi=float('inf')) -> bool:
        if not node:
            return True
        if not (lo < node.val < hi):
            return False
        return (check(node.left,  lo, node.val) and
                check(node.right, node.val, hi))
    return check(root)
```

### Kth smallest — iterative inorder, stop early

```python
def kth_smallest(root, k: int) -> int:
    stack, cur = [], root
    while cur or stack:
        while cur:                 # walk the left spine
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        k -= 1
        if k == 0:
            return cur.val         # stop early - do not traverse the rest
        cur = cur.right
```

### LCA in a BST — O(h), much simpler than the general tree version

```python
def lowest_common_ancestor(root, p, q):
    cur = root
    while cur:
        if p.val < cur.val and q.val < cur.val:
            cur = cur.left          # both on the left
        elif p.val > cur.val and q.val > cur.val:
            cur = cur.right         # both on the right
        else:
            return cur              # they SPLIT here - this is the LCA
```

```
  find LCA(2, 4):        5      2<5 and 4<5 → go left
                        / \
                      3     8   2<3 but 4>3 → they SPLIT → LCA = 3
                     / \
                    2   4
```

## Complexity

| | |
|---|---|
| Search / insert / LCA | O(h) — O(log n) balanced, **O(n) degenerate** |
| Full traversal | O(n) |

## Common mistakes

- **Validating with only a parent-child comparison.** The classic wrong answer that passes small tests.
- Using the general-tree LCA algorithm when told it is a BST (O(n) instead of O(h))
- Not stopping early in kth-smallest

## Problems

- [98. Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/) — Medium
- [230. Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/) — Medium
- [235. LCA of a BST](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/) — Medium
