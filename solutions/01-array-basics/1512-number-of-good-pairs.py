"""
1512. Number Of Good Pairs
https://leetcode.com/problems/number-of-good-pairs/

Difficulty : Easy
Pattern    : Array Basics
Tier       : Stretch   (optional - skip without guilt if the week is tight)
Scheduled  : Mon 14 Sep 2026  (week 1)

INPUT
    nums : list of integers

RETURN
    integer

EXAMPLE
    nums = [1, 2, 3, 1, 1, 3]
    ->  4

RECOGNITION HINT  (read only AFTER a real attempt)
    Count frequencies first. If a value appears k times it contributes
    k*(k-1)/2 pairs - no nested loop.

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
    def numIdenticalPairs_brute(self, nums: List[int]) -> int:
        pass


    def numIdenticalPairs(self, nums: List[int]) -> int:
        pass


METHOD      = 'numIdenticalPairs'
PARAM_TYPES = ['integer[]']
RETURN_TYPE = 'integer'
INPLACE_ARG = None

TESTS = [
    ([[1, 2, 3, 1, 1, 3]], 4),
    ([[1, 1, 1, 1]], 6),
    ([[1, 2, 3]], 0),
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
