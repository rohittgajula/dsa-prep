"""
105. Construct Binary Tree From Preorder And Inorder Traversal
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

Difficulty : Medium
Pattern    : Binary Tree
Tier       : Core
Scheduled  : Fri 15 Jan 2027  (week 18)

INPUT
    preorder : list of integers
    inorder  : list of integers

RETURN
    root of a binary tree

EXAMPLE
    preorder = [3, 9, 20, 15, 7], inorder = [9, 3, 15, 20, 7]
    ->  [3, 9, 20, None, None, 15, 7]

RECOGNITION HINT  (read only AFTER a real attempt)
    Preorder gives the root; its index in inorder splits left from
    right. Hashmap the inorder indices.

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

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(vals):
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


class Solution:
    def buildTree_brute(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        pass


    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        pass


METHOD      = 'buildTree'
PARAM_TYPES = ['integer[]', 'integer[]']
RETURN_TYPE = 'TreeNode'
INPLACE_ARG = None

TESTS = [
    ([[3, 9, 20, 15, 7], [9, 3, 15, 20, 7]], [3, 9, 20, None, None, 15, 7]),
    ([[-1], [-1]], [-1]),
]


if __name__ == "__main__":
    import ast
    import copy
    import inspect
    import textwrap

    def _todo(fn):
        try:
            body = ast.parse(textwrap.dedent(inspect.getsource(fn))).body[0].body
        except (OSError, TypeError, SyntaxError, IndexError):
            return False
        return len(body) == 1 and isinstance(body[0], (ast.Pass, ast.Expr))

    def _verdict(got, want):
        if got == want:
            return "PASS"
        if isinstance(got, float) or isinstance(want, float):
            try:
                if abs(float(got) - float(want)) < 1e-5:
                    return "PASS"
            except (TypeError, ValueError):
                pass
        if isinstance(got, list) and isinstance(want, list):
            try:
                if sorted(map(repr, got)) == sorted(map(repr, want)):
                    return "PASS (order ignored)"
            except TypeError:
                pass
        return "FAIL"

    sol = Solution()
    for label, fname in (("BRUTE FORCE", METHOD + "_brute"), ("OPTIMAL    ", METHOD)):
        fn = getattr(sol, fname, None)
        if fn is None:
            continue
        print(f"{label} :")
        if _todo(fn):
            print("    not written yet\n")
            continue
        for n, (args, want) in enumerate(TESTS, 1):
            call = [copy.deepcopy(a) for a in args]
            try:
                got = fn(*call)
            except Exception as exc:
                print(f"    case {n}: ERROR  {type(exc).__name__}: {exc}")
                continue
            got = dump_tree(got)
            print(f"    case {n}: {_verdict(got, want):<20} got={got!r}  want={want!r}")
        print()
