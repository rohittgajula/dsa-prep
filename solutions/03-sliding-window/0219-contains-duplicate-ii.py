"""
219. Contains Duplicate Ii
https://leetcode.com/problems/contains-duplicate-ii/

Difficulty : Easy
Pattern    : Sliding Window
Tier       : Core
Scheduled  : Tue 29 Sep 2026  (week 3)

INPUT
    nums : list of integers
    k    : integer

RETURN
    true or false

EXAMPLE
    nums = [1, 2, 3, 1], k = 3
    ->  True

RECOGNITION HINT  (read only AFTER a real attempt)
    Fixed window of size k holding a set. The window bounds the index
    distance for you.

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
    def containsNearbyDuplicate_brute(self, nums: List[int], k: int) -> bool:
        pass


    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        pass


METHOD      = 'containsNearbyDuplicate'
PARAM_TYPES = ['integer[]', 'integer']
RETURN_TYPE = 'boolean'
INPLACE_ARG = None

TESTS = [
    ([[1, 2, 3, 1], 3], True),
    ([[1, 0, 1, 1], 1], True),
    ([[1, 2, 3, 1, 2, 3], 2], False),
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
