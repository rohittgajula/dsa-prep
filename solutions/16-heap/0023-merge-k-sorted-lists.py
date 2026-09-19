"""
23. Merge K Sorted Lists
https://leetcode.com/problems/merge-k-sorted-lists/

Difficulty : Hard
Pattern    : Heap
Tier       : Core
Scheduled  : Sat 19 Dec 2026  (week 14)

INPUT
    lists : list of head of a linked lists

RETURN
    head of a linked list

EXAMPLE
    lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
    ->  [1, 1, 2, 3, 4, 4, 5, 6]

RECOGNITION HINT  (read only AFTER a real attempt)
    Heap of k current heads, or divide-and-conquer pairwise merging.
    Both are O(N log k).

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
    def mergeKLists_brute(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pass


    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pass


METHOD      = 'mergeKLists'
PARAM_TYPES = ['ListNode[]']
RETURN_TYPE = 'ListNode'
INPLACE_ARG = None

TESTS = [
    ([[[1, 4, 5], [1, 3, 4], [2, 6]]], [1, 1, 2, 3, 4, 4, 5, 6]),
    ([[]], []),
    ([[[]]], []),
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
            got = dump_list(got)
            print(f"    case {n}: {_verdict(got, want):<20} got={got!r}  want={want!r}")
        print()
