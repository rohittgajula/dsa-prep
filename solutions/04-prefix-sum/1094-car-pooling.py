"""
1094. Car Pooling
https://leetcode.com/problems/car-pooling/

Difficulty : Medium
Pattern    : Prefix Sum
Tier       : Core
Scheduled  : Mon 05 Oct 2026  (week 4)

INPUT
    trips    : grid of integers
    capacity : integer

RETURN
    true or false

EXAMPLE
    trips = [[2, 1, 5], [3, 3, 7]], capacity = 4
    ->  False

RECOGNITION HINT  (read only AFTER a real attempt)
    Difference array over locations, or a sweep line of +/- events.
    Check capacity is never exceeded.

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
    def carPooling_brute(self, trips: List[List[int]], capacity: int) -> bool:
        pass


    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        pass


METHOD      = 'carPooling'
PARAM_TYPES = ['integer[][]', 'integer']
RETURN_TYPE = 'boolean'
INPLACE_ARG = None

TESTS = [
    ([[[2, 1, 5], [3, 3, 7]], 4], False),
    ([[[2, 1, 5], [3, 3, 7]], 5], True),
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
