"""
88. Merge Sorted Array
https://leetcode.com/problems/merge-sorted-array/

Difficulty : Easy
Pattern    : Array Basics
Tier       : Core
Scheduled  : Mon 14 Sep 2026  (week 1)

INPUT
    nums1 : list of integers
    m     : integer
    nums2 : list of integers
    n     : integer

RETURN
    nothing is returned - nums1 itself is changed

EXAMPLE
    nums1 = [1, 2, 3, 0, 0, 0], m = 3, nums2 = [2, 5, 6], n = 3
    ->  nums1 becomes [1, 2, 2, 3, 5, 6]

RECOGNITION HINT  (read only AFTER a real attempt)
    Merging forward needs shifting. Fill from the BACK where the spare
    space already is.

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
    def merge_brute(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        pass


    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        pass


METHOD      = 'merge'
PARAM_TYPES = ['integer[]', 'integer', 'integer[]', 'integer']
RETURN_TYPE = 'void'
INPLACE_ARG = 0

TESTS = [
    ([[1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3], [1, 2, 2, 3, 5, 6]),
    ([[1], 1, [], 0], [1]),
    ([[0], 0, [1], 1], [1]),
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
            got = call[INPLACE_ARG]
            print(f"    case {n}: {_verdict(got, want):<20} got={got!r}  want={want!r}")
        print()
