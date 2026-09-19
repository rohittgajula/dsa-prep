"""
1283. Find The Smallest Divisor Given A Threshold
https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/

Difficulty : Medium
Pattern    : Binary Search on Answer
Tier       : Core
Scheduled  : Thu 05 Nov 2026  (week 8)

INPUT
    nums      : list of integers
    threshold : integer

RETURN
    integer

EXAMPLE
    nums = [1, 2, 5, 9], threshold = 6
    ->  5

RECOGNITION HINT  (read only AFTER a real attempt)
    Search the divisor in [1, max(nums)]. feasible = sum of ceilings <=
    threshold.

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
    def smallestDivisor_brute(self, nums: List[int], threshold: int) -> int:
        pass


    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        pass


METHOD      = 'smallestDivisor'
PARAM_TYPES = ['integer[]', 'integer']
RETURN_TYPE = 'integer'
INPLACE_ARG = None

TESTS = [
    ([[1, 2, 5, 9], 6], 5),
    ([[44, 22, 33, 11, 1], 5], 44),
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
