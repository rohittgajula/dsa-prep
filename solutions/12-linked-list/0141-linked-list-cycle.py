"""
141. Linked List Cycle
https://leetcode.com/problems/linked-list-cycle/

Difficulty : Easy
Pattern    : Linked List
Tier       : Core
Scheduled  : Thu 26 Nov 2026  (week 11)

INPUT
    head : head of a linked list

HEADS UP
    LeetCode's test data does not line up with this method.
    signature takes 1 arg(s), the judge feeds 2.
    The 'pos' in the LeetCode input is not a method parameter - it
    says where the tail links back to. Build the list, then wire
    tail.next to the node at pos.
    Build the real arguments by hand, then fill in TESTS below.

RAW JUDGE DATA
    inputs:
        [3,2,0,-4]
        1
        [1,2]
        0
        [1]
        -1
    outputs:
        true
        true
        false

RECOGNITION HINT  (read only AFTER a real attempt)
    Floyd. If fast ever equals slow there is a cycle; if fast hits null
    there is not.

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

Time taken: __ min      Solved unaided: Y / N      Hints used: __
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
    def hasCycle_brute(self, head: Optional[ListNode]) -> bool:
        pass


    def hasCycle(self, head: Optional[ListNode]) -> bool:
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
    for label, fname in (("BRUTE FORCE", 'hasCycle_brute'), ("OPTIMAL    ", 'hasCycle')):
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
