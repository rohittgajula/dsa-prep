"""
1314. Matrix Block Sum
https://leetcode.com/problems/matrix-block-sum/

Difficulty : Medium
Pattern    : Prefix Sum
Tier       : Stretch   (optional - skip without guilt if the week is tight)
Scheduled  : Thu 08 Oct 2026  (week 4)

INPUT
    mat : grid of integers
    k   : integer

RETURN
    grid of integers

EXAMPLE
    mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]], k = 1
    ->  [[12, 21, 16], [27, 45, 33], [24, 39, 28]]

RECOGNITION HINT  (read only AFTER a real attempt)
    Build a 2D prefix sum, then each answer is one inclusion-exclusion
    query with clamped bounds.

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
    def matrixBlockSum_brute(self, mat: List[List[int]], k: int) -> List[List[int]]:
        pass


    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        pass


METHOD      = 'matrixBlockSum'
PARAM_TYPES = ['integer[][]', 'integer']
RETURN_TYPE = 'integer[][]'
INPLACE_ARG = None

TESTS = [
    ([[[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1], [[12, 21, 16], [27, 45, 33], [24, 39, 28]]),
    ([[[1, 2, 3], [4, 5, 6], [7, 8, 9]], 2], [[45, 45, 45], [45, 45, 45], [45, 45, 45]]),
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
