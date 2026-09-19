"""
430. Flatten A Multilevel Doubly Linked List
https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/

Difficulty : Medium
Pattern    : Linked List
Tier       : Stretch   (optional - skip without guilt if the week is tight)
Scheduled  : Sat 28 Nov 2026  (week 11)

RECOGNITION HINT  (read only AFTER a real attempt)
    DFS with a stack. When a child exists, push next and descend, fixing
    prev pointers.

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
    """LeetCode's doubly linked list node with a child pointer."""

    def __init__(self, val, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

#---------------------------------------------------------------------
#  HEADS UP - LeetCode's test data does not line up with this method.
#  head: real type 'Optional[Node]', judge sends Optional[ListNode].
#---------------------------------------------------------------------


class Solution:
    # -----------------------------------------------------------------
    #  BRUTE FORCE   -- write this one first, even when it is obvious.
    #  Time  : O(?)      Space : O(?)
    # -----------------------------------------------------------------
    def flatten_brute(self, head: 'Optional[Node]') -> 'Optional[Node]':
        raise NotImplementedError("brute force")

    # -----------------------------------------------------------------
    #  OPTIMAL       -- what does the brute force redo that it need not?
    #  Time  : O(?)      Space : O(?)
    # -----------------------------------------------------------------
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        raise NotImplementedError("optimal")


# ---------------------------------------------------------------------
#  The raw data LeetCode feeds its judge, for reference. Build the real
#  arguments from it by hand (see the heads-up above), then fill in TESTS.
# ---------------------------------------------------------------------
#  inputs :
#      [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
#      [1,2,null,3]
#      []
#  outputs:
#      [1,2,3,7,8,11,12,9,10,4,5,6]
#      [1,3,2]
#      []

TESTS = [
    # ( [args...], expected )   <- write these yourself for this one
]


if __name__ == "__main__":
    if not TESTS:
        print("no test cases yet - see the heads-up at the top of this file")
    sol = Solution()
    for label, fname in (("BRUTE FORCE", 'flatten_brute'), ("OPTIMAL    ", 'flatten')):
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