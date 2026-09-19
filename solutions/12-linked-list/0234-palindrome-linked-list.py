"""
234. Palindrome Linked List
https://leetcode.com/problems/palindrome-linked-list/

Difficulty : Easy
Pattern    : Linked List
Tier       : Core
Scheduled  : Sun 29 Nov 2026  (week 11)

INPUT
    head : head of a linked list

RETURN
    true or false

EXAMPLE
    head = [1, 2, 2, 1]
    ->  True

RECOGNITION HINT  (read only AFTER a real attempt)
    Find the middle, reverse the second half, compare, then restore.
    O(1) space.

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
    def isPalindrome_brute(self, head: Optional[ListNode]) -> bool:
        pass


    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        pass


METHOD      = 'isPalindrome'
PARAM_TYPES = ['ListNode']
RETURN_TYPE = 'boolean'
INPLACE_ARG = None

TESTS = [
    ([[1, 2, 2, 1]], True),
    ([[1, 2]], False),
]


if __name__ == "__main__":
    import ast
    import copy
    import inspect
    import textwrap

    def _build(v, t):
        if t.startswith("ListNode"):
            return build_list(v)
        return v

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
            call = [_build(copy.deepcopy(a), t) for a, t in zip(args, PARAM_TYPES)]
            try:
                got = fn(*call)
            except Exception as exc:
                print(f"    case {n}: ERROR  {type(exc).__name__}: {exc}")
                continue
            print(f"    case {n}: {_verdict(got, want):<20} got={got!r}  want={want!r}")
        print()
