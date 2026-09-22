"""
378. Kth Smallest Element In A Sorted Matrix
https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

Difficulty : Medium
Pattern    : Heap
Tier       : Core
Scheduled  : Fri 18 Dec 2026  (week 14)

INPUT
    matrix : grid of integers
    k      : integer

RETURN
    integer

EXAMPLE
    matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]], k = 8
    ->  13

RECOGNITION HINT  (read only AFTER a real attempt)
    Heap-based k-way merge, or binary search the VALUE and count
    elements <= it.

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
    def kthSmallest_brute(self, matrix: List[List[int]], k: int) -> int:
        pass


    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        pass


METHOD      = 'kthSmallest'
PARAM_TYPES = ['integer[][]', 'integer']
RETURN_TYPE = 'integer'
INPLACE_ARG = None

TESTS = [
    ([[[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8], 13),
    ([[[-5]], 1], -5),
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
    for label, fname, brute in (("BRUTE FORCE", METHOD + "_brute", True),
                                ("OPTIMAL    ", METHOD, False)):
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
