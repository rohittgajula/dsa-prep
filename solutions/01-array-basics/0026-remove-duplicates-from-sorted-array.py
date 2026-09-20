"""
26. Remove Duplicates From Sorted Array
https://leetcode.com/problems/remove-duplicates-from-sorted-array/

Difficulty : Easy
Pattern    : Array Basics
Tier       : Core
Scheduled  : Fri 11 Sep 2026  (week 0)

INPUT
    nums : list of integers

RETURN
    the new length k, and nums holds the k kept values at the front

EXAMPLE
    nums = [1, 1, 2]
    ->  nums starts with [1, 2]

RECOGNITION HINT  (read only AFTER a real attempt)
    Two pointers, same direction: a slow WRITE pointer and a fast READ
    pointer. Slow only advances on a new value.

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
    def removeDuplicates_brute(self, nums: List[int]) -> int:
        sol = []
        for num in nums:
            print(num)
            if num not in sol:
                print(f"loop : {num}")
                sol.append(num)
        return sol


    def removeDuplicates(self, nums: List[int]) -> int:
        pass


METHOD      = 'removeDuplicates'
PARAM_TYPES = ['integer[]']
RETURN_TYPE = 'integer'
INPLACE_ARG = 0
INPLACE_PREFIX = True

TESTS = [
    ([[1, 1, 2]], [1, 2]),
    ([[0, 0, 1, 1, 1, 2, 2, 3, 3, 4]], [0, 1, 2, 3, 4]),
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
            got = call[INPLACE_ARG][:got] if isinstance(got, int) else call[INPLACE_ARG]
            print(f"    case {n}: {_verdict(got, want):<20} got={got!r}  want={want!r}")
        print()
