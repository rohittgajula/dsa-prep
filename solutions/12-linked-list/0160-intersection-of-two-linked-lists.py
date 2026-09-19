"""
160. Intersection Of Two Linked Lists
https://leetcode.com/problems/intersection-of-two-linked-lists/

Difficulty : Easy
Pattern    : Linked List
Tier       : Core
Scheduled  : Fri 27 Nov 2026  (week 11)

RECOGNITION HINT  (read only AFTER a real attempt)
    Two pointers that switch lists on reaching the end - they equalise
    the path lengths and meet at the join.

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


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build_list(vals):
    """[1,2,3] -> 1 -> 2 -> 3"""
    head = None
    for v in reversed(vals or []):
        head = ListNode(v, head)
    return head


def dump_list(head, limit=500):
    """1 -> 2 -> 3 -> [1,2,3]   (limit guards against a cycle)"""
    out = []
    while head is not None and len(out) < limit:
        out.append(head.val)
        head = head.next
    return out

#---------------------------------------------------------------------
#  HEADS UP - LeetCode's test data does not line up with this method.
#  signature takes 2 arg(s), the judge feeds 5.
#  LeetCode feeds this as (intersectVal, listA, listB, skipA, skipB) and prints
#  'Intersected at 8'. The method itself takes two heads. To test locally, build
#  the two lists so they SHARE the tail node object, then check the returned node
#  is that same object (identity, not value).
#---------------------------------------------------------------------


class Solution:
    # -----------------------------------------------------------------
    #  BRUTE FORCE   -- write this one first, even when it is obvious.
    #  Time  : O(?)      Space : O(?)
    # -----------------------------------------------------------------
    def getIntersectionNode_brute(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        raise NotImplementedError("brute force")

    # -----------------------------------------------------------------
    #  OPTIMAL       -- what does the brute force redo that it need not?
    #  Time  : O(?)      Space : O(?)
    # -----------------------------------------------------------------
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        raise NotImplementedError("optimal")


# ---------------------------------------------------------------------
#  The raw data LeetCode feeds its judge, for reference. Build the real
#  arguments from it by hand (see the heads-up above), then fill in TESTS.
# ---------------------------------------------------------------------
#  inputs :
#      8
#      [4,1,8,4,5]
#      [5,6,1,8,4,5]
#      2
#      3
#      2
#      [1,9,1,2,4]
#      [3,2,4]
#      3
#      1
#      0
#      [2,6,4]
#  outputs:
#      Intersected at '8'
#      Intersected at '2'
#      No intersection

TESTS = [
    # ( [args...], expected )   <- write these yourself for this one
]


if __name__ == "__main__":
    if not TESTS:
        print("no test cases yet - see the heads-up at the top of this file")
    sol = Solution()
    for label, fname in (("BRUTE FORCE", 'getIntersectionNode_brute'), ("OPTIMAL    ", 'getIntersectionNode')):
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