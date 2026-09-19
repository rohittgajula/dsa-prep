"""
116. Populating Next Right Pointers In Each Node
https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

Difficulty : Medium
Pattern    : Binary Tree
Tier       : Core
Scheduled  : Tue 05 Jan 2027  (week 17)

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
    """LeetCode's perfect-binary-tree node, with a next pointer per level."""

    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

#---------------------------------------------------------------------
#  HEADS UP - LeetCode's test data does not line up with this method.
#  root: real type 'Optional[Node]', judge sends Optional[TreeNode].
#  Output uses '#' to mark the end of each level, which is not JSON. Verify by
#  walking the next-pointers level by level yourself.
#---------------------------------------------------------------------


class Solution:
    # -----------------------------------------------------------------
    #  BRUTE FORCE   -- write this one first, even when it is obvious.
    #  Time  : O(?)      Space : O(?)
    # -----------------------------------------------------------------
    def connect_brute(self, root: 'Optional[Node]') -> 'Optional[Node]':
        raise NotImplementedError("brute force")

    # -----------------------------------------------------------------
    #  OPTIMAL       -- what does the brute force redo that it need not?
    #  Time  : O(?)      Space : O(?)
    # -----------------------------------------------------------------
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        raise NotImplementedError("optimal")


# ---------------------------------------------------------------------
#  The raw data LeetCode feeds its judge, for reference. Build the real
#  arguments from it by hand (see the heads-up above), then fill in TESTS.
# ---------------------------------------------------------------------
#  inputs :
#      [1,2,3,4,5,6,7]
#      []
#  outputs:
#      [1,#,2,3,#,4,5,6,7,#]
#      []

TESTS = [
    # ( [args...], expected )   <- write these yourself for this one
]


if __name__ == "__main__":
    if not TESTS:
        print("no test cases yet - see the heads-up at the top of this file")
    sol = Solution()
    for label, fname in (("BRUTE FORCE", 'connect_brute'), ("OPTIMAL    ", 'connect')):
        fn = getattr(sol, fname, None)
        if fn is None:
            continue
        print(f"{label} :")
        for n, (args, want) in enumerate(TESTS, 1):
            try:
                got = fn(*args)
            except NotImplementedError:
                print("    -- not written yet --")
                break
            except Exception as exc:
                print(f"    case {n}: ERROR  {type(exc).__name__}: {exc}")
                continue
            print(f"    case {n}: {'PASS' if got == want else 'FAIL'}   got={got!r}  want={want!r}")
        print()