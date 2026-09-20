"""
167. Two Sum Ii Input Array Is Sorted
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

Difficulty : Medium
Pattern    : Two Pointers
Tier       : Core
Scheduled  : Fri 25 Sep 2026  (week 2)

INPUT
    numbers : list of integers
    target  : integer

RETURN
    list of integers

EXAMPLE
    numbers = [2, 7, 11, 15], target = 9
    ->  [1, 2]

RECOGNITION HINT  (read only AFTER a real attempt)
    SORTED is the signal. Sum too small means move left up; too big
    means move right down.

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

from typing import List


class Solution:
    def twoSum_brute(self, numbers: List[int], target: int) -> List[int]:
        pass


    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        pass


METHOD      = 'twoSum'
PARAM_TYPES = ['integer[]', 'integer']
RETURN_TYPE = 'integer[]'
INPLACE_ARG = None

TESTS = [
    ([[2, 7, 11, 15], 9], [1, 2]),
    ([[2, 3, 4], 6], [1, 3]),
    ([[-1, 0], -1], [1, 2]),
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
