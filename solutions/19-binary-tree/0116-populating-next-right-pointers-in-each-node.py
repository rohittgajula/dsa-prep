"""
116. Populating Next Right Pointers In Each Node
https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

Difficulty : Medium
Pattern    : Binary Tree
Tier       : Core
Scheduled  : Tue 05 Jan 2027  (week 17)

INPUT
    root : node, see the problem page

HEADS UP
    LeetCode's test data does not line up with this method.
    root: real type 'Optional[Node]', judge sends
    Optional[TreeNode].
    Output uses '#' to mark the end of each level, which is not
    JSON. Verify by walking the next-pointers level by level
    yourself.
    Build the real arguments by hand, then fill in TESTS below.

RAW JUDGE DATA
    inputs:
        [1,2,3,4,5,6,7]
        []
    outputs:
        [1,#,2,3,#,4,5,6,7,#]
        []

RECOGNITION HINT  (read only AFTER a real attempt)
    Perfect tree, so you can link using already-established next
    pointers - O(1) space.

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


class Node:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect_brute(self, root: 'Optional[Node]') -> 'Optional[Node]':
        pass


    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        pass


TESTS = [
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

    sol = Solution()
    for label, fname in (("BRUTE FORCE", 'connect_brute'), ("OPTIMAL    ", 'connect')):
        fn = getattr(sol, fname, None)
        if fn is None:
            continue
        print(f"{label} :")
        if _todo(fn):
            print("    not written yet\n")
            continue
        if not TESTS:
            print("    no test cases yet - see HEADS UP at the top of this file\n")
            continue
        for n, (args, want) in enumerate(TESTS, 1):
            try:
                got = fn(*copy.deepcopy(args))
            except Exception as exc:
                print(f"    case {n}: ERROR  {type(exc).__name__}: {exc}")
                continue
            mark = "PASS" if got == want else "FAIL"
            print(f"    case {n}: {mark:<20} got={got!r}  want={want!r}")
        print()
