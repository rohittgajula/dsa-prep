"""
160. Intersection Of Two Linked Lists
https://leetcode.com/problems/intersection-of-two-linked-lists/

Difficulty : Easy
Pattern    : Linked List
Tier       : Core
Scheduled  : Fri 27 Nov 2026  (week 11)

INPUT
    headA : head of a linked list
    headB : head of a linked list

HEADS UP
    LeetCode's test data does not line up with this method.
    signature takes 2 arg(s), the judge feeds 5.
    LeetCode feeds this as (intersectVal, listA, listB, skipA,
    skipB) and prints 'Intersected at 8'. The method itself takes
    two heads. To test locally, build the two lists so they SHARE
    the tail node object, then check the returned node is that same
    object (identity, not value).
    Build the real arguments by hand, then fill in TESTS below.

RAW JUDGE DATA
    inputs:
        8
        [4,1,8,4,5]
        [5,6,1,8,4,5]
        2
        3
        2
        [1,9,1,2,4]
        [3,2,4]
        3
        1
        0
        [2,6,4]
    outputs:
        Intersected at '8'
        Intersected at '2'
        No intersection

RECOGNITION HINT  (read only AFTER a real attempt)
    Two pointers that switch lists on reaching the end - they equalise
    the path lengths and meet at the join.

------------------------------------------------------------------------
MY THINKING  (write this while you solve - raw, unedited)
    What the problem looked like at first:
        <>
    What I tried:
        <>
    Where I got stuck:
        <>
    What made it click:
        <>

    Tutor review:
        <>

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
Solved on: __           Revised: __
------------------------------------------------------------------------
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build_list(vals):
    head = None
    for v in reversed(vals or []):
        head = ListNode(v, head)
    return head


def dump_list(head, limit=500):
    out = []
    while head is not None and len(out) < limit:
        out.append(head.val)
        head = head.next
    return out


class Solution:
    def getIntersectionNode_brute(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        pass


    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
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
    for label, fname in (("BRUTE FORCE", 'getIntersectionNode_brute'), ("OPTIMAL    ", 'getIntersectionNode')):
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
