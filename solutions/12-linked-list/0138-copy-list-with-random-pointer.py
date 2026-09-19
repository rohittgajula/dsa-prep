"""
138. Copy List With Random Pointer
https://leetcode.com/problems/copy-list-with-random-pointer/

Difficulty : Medium
Pattern    : Linked List
Tier       : Core
Scheduled  : Thu 26 Nov 2026  (week 11)

RECOGNITION HINT  (read only AFTER a real attempt)
    Hash map old->new in two passes, or the O(1)-space weave: interleave
    copies, set randoms, then split.

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
    """LeetCode's linked-list node with an extra random pointer."""

    def __init__(self, x: int, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

#---------------------------------------------------------------------
#  HEADS UP - LeetCode's test data does not line up with this method.
#  head: real type 'Optional[Node]', judge sends Optional[ListNode].
#  Uses LeetCode's Node class (val, next, random). Input pairs are [val, randomIndex].
#  Check the copy is a DEEP one: same values, but every node object is new.
#---------------------------------------------------------------------


class Solution:
    # -----------------------------------------------------------------
    #  BRUTE FORCE   -- write this one first, even when it is obvious.
    #  Time  : O(?)      Space : O(?)
    # -----------------------------------------------------------------
    def copyRandomList_brute(self, head: 'Optional[Node]') -> 'Optional[Node]':
        raise NotImplementedError("brute force")

    # -----------------------------------------------------------------
    #  OPTIMAL       -- what does the brute force redo that it need not?
    #  Time  : O(?)      Space : O(?)
    # -----------------------------------------------------------------
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        raise NotImplementedError("optimal")


# ---------------------------------------------------------------------
#  The raw data LeetCode feeds its judge, for reference. Build the real
#  arguments from it by hand (see the heads-up above), then fill in TESTS.
# ---------------------------------------------------------------------
#  inputs :
#      [[7,null],[13,0],[11,4],[10,2],[1,0]]
#      [[1,1],[2,1]]
#      [[3,null],[3,0],[3,null]]
#  outputs:
#      [[7,null],[13,0],[11,4],[10,2],[1,0]]
#      [[1,1],[2,1]]
#      [[3,null],[3,0],[3,null]]

TESTS = [
    # ( [args...], expected )   <- write these yourself for this one
]


if __name__ == "__main__":
    if not TESTS:
        print("no test cases yet - see the heads-up at the top of this file")
    sol = Solution()
    for label, fname in (("BRUTE FORCE", 'copyRandomList_brute'), ("OPTIMAL    ", 'copyRandomList')):
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