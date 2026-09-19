"""
34. Find First And Last Position Of Element In Sorted Array
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

Difficulty : Medium
Pattern    : Binary Search
Tier       : Core
Scheduled  : Fri 30 Oct 2026  (week 7)

INPUT
    nums   : list of integers
    target : integer

RETURN
    list of integers

EXAMPLE
    nums = [5, 7, 7, 8, 8, 10], target = 8
    ->  [3, 4]

RECOGNITION HINT  (read only AFTER a real attempt)
    Two searches: lower_bound(target) and lower_bound(target+1) - 1.

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

from typing import List


class Solution:
    def searchRange_brute(self, nums: List[int], target: int) -> List[int]:
        pass


    def searchRange(self, nums: List[int], target: int) -> List[int]:
        pass


METHOD      = 'searchRange'
PARAM_TYPES = ['integer[]', 'integer']
RETURN_TYPE = 'integer[]'
INPLACE_ARG = None

TESTS = [
    ([[5, 7, 7, 8, 8, 10], 8], [3, 4]),
    ([[5, 7, 7, 8, 8, 10], 6], [-1, -1]),
    ([[], 0], [-1, -1]),
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
            call = [copy.deepcopy(a) for a in args]
            try:
                got = fn(*call)
            except Exception as exc:
                print(f"    case {n}: ERROR  {type(exc).__name__}: {exc}")
                continue
            print(f"    case {n}: {_verdict(got, want):<20} got={got!r}  want={want!r}")
        print()
