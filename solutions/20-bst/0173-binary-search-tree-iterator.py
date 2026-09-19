"""
173. Binary Search Tree Iterator
https://leetcode.com/problems/binary-search-tree-iterator/

Difficulty : Medium
Pattern    : BST
Tier       : Core
Scheduled  : Sat 23 Jan 2027  (week 19)

RECOGNITION HINT  (read only AFTER a real attempt)
    Controlled iterative inorder - keep a stack of left-spine nodes;
    next() pops and pushes the right subtree's left spine.

------------------------------------------------------------------------
BRUTE FORCE
    <state it the way you would say it out loud in an interview>
    Time  : O(?)
    Space : O(?)

OPTIMAL
    <what does it exploit that the brute force wastes?>
    Time  : O(?)
    Space : O(?)

KEY INSIGHT
    <the one sentence that makes this collapse>

MISTAKES I MADE
    <the part worth re-reading in the revision sweeps>

Time taken: __ min      Solved unaided: Y / N
------------------------------------------------------------------------
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(vals):
    """LeetCode level-order list (None = missing child) -> root"""
    if not vals:
        return None
    root = TreeNode(vals[0])
    q, i = [root], 1
    while q and i < len(vals):
        node = q.pop(0)
        if i < len(vals):
            if vals[i] is not None:
                node.left = TreeNode(vals[i])
                q.append(node.left)
            i += 1
        if i < len(vals):
            if vals[i] is not None:
                node.right = TreeNode(vals[i])
                q.append(node.right)
            i += 1
    return root


def dump_tree(root):
    """root -> LeetCode level-order list, trailing Nones trimmed"""
    if root is None:
        return []
    out, q = [], [root]
    while q:
        node = q.pop(0)
        if node is None:
            out.append(None)
        else:
            out.append(node.val)
            q.append(node.left)
            q.append(node.right)
    while out and out[-1] is None:
        out.pop()
    return out


def find_node(root, val):
    """LeetCode hands some problems a VALUE where the method wants the NODE."""
    if root is None:
        return None
    q = [root]
    while q:
        n = q.pop(0)
        if n.val == val:
            return n
        if n.left:
            q.append(n.left)
        if n.right:
            q.append(n.right)
    return None


class BSTIteratorBrute:
    """Simplest thing that works. Get it correct, then beat it."""

    def __init__(self, root: Optional[TreeNode]):
        raise NotImplementedError

    def next(self) -> int:
        raise NotImplementedError

    def hasNext(self) -> bool:
        raise NotImplementedError


class BSTIterator:
    """The version you would actually submit."""

    def __init__(self, root: Optional[TreeNode]):
        raise NotImplementedError

    def next(self) -> int:
        raise NotImplementedError

    def hasNext(self) -> bool:
        raise NotImplementedError


# ---------------------------------------------------------------------
#  TEST CASES  --  the operation sequence from the LeetCode page
# ---------------------------------------------------------------------
CLASS_BRUTE   = BSTIteratorBrute
CLASS_OPTIMAL = BSTIterator

OPS      = ['BSTIterator', 'next', 'next', 'hasNext', 'next', 'hasNext', 'next', 'hasNext', 'next', 'hasNext']
ARGS     = [[[7, 3, 15, None, None, 9, 20]], [], [], [], [], [], [], [], [], []]
EXPECTED = [None, 3, 7, True, 9, True, 15, True, 20, False]


# ---------------------------------------------------------------------
#  RUNNER  --  python3 this_file.py
#  Replays the LeetCode operation sequence against both versions.
# ---------------------------------------------------------------------
if __name__ == "__main__":
    def replay(cls, label):
        print(f"{label} :")
        obj = None
        for n, (op, args) in enumerate(zip(OPS, ARGS)):
            want = EXPECTED[n] if n < len(EXPECTED) else "?"
            try:
                if n == 0:
                    obj = cls(*args)
                    got = None
                else:
                    got = getattr(obj, op)(*args)
            except NotImplementedError:
                print("    -- not written yet --")
                return
            except Exception as exc:
                print(f"    {op}({args}) ERROR {type(exc).__name__}: {exc}")
                continue
            mark = "PASS" if got == want else "FAIL"
            if want == "?":
                mark = "----"
            print(f"    {n:>2}. {op}({str(args)[1:-1]:<12}) -> {str(got):<8} want {str(want):<8} {mark}")
        print()

    for cls, label in ((CLASS_BRUTE, "BRUTE FORCE"), (CLASS_OPTIMAL, "OPTIMAL    ")):
        replay(cls, label)
