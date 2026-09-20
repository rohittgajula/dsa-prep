"""
430. Flatten A Multilevel Doubly Linked List
https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/

Difficulty : Medium
Pattern    : Linked List
Tier       : Stretch   (optional - skip without guilt if the week is tight)
Scheduled  : Sat 28 Nov 2026  (week 11)

INPUT
    head : node, see the problem page

HEADS UP
    LeetCode's test data does not line up with this method.
    head: real type 'Optional[Node]', judge sends
    Optional[ListNode].
    Build the real arguments by hand, then fill in TESTS below.

RAW JUDGE DATA
    inputs:
        [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
        [1,2,null,3]
        []
    outputs:
        [1,2,3,7,8,11,12,9,10,4,5,6]
        [1,3,2]
        []

RECOGNITION HINT  (read only AFTER a real attempt)
    DFS with a stack. When a child exists, push next and descend, fixing
    prev pointers.

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


class Node:
    def __init__(self, val, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten_brute(self, head: 'Optional[Node]') -> 'Optional[Node]':
        pass


    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
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
    for label, fname in (("BRUTE FORCE", 'flatten_brute'), ("OPTIMAL    ", 'flatten')):
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
