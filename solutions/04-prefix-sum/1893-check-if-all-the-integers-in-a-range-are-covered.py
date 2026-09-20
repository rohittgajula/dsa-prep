"""
1893. Check If All The Integers In A Range Are Covered
https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/

Difficulty : Easy
Pattern    : Prefix Sum
Tier       : Stretch   (optional - skip without guilt if the week is tight)
Scheduled  : Tue 06 Oct 2026  (week 4)

INPUT
    ranges : grid of integers
    left   : integer
    right  : integer

RETURN
    true or false

EXAMPLE
    ranges = [[1, 2], [3, 4], [5, 6]], left = 2, right = 5
    ->  True

RECOGNITION HINT  (read only AFTER a real attempt)
    Difference array over the value range, then check the running sum is
    positive throughout.

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

from typing import List


class Solution:
    def isCovered_brute(self, ranges: List[List[int]], left: int, right: int) -> bool:
        pass


    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        pass


METHOD      = 'isCovered'
PARAM_TYPES = ['integer[][]', 'integer', 'integer']
RETURN_TYPE = 'boolean'
INPLACE_ARG = None

TESTS = [
    ([[[1, 2], [3, 4], [5, 6]], 2, 5], True),
    ([[[1, 10], [10, 20]], 21, 21], False),
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
