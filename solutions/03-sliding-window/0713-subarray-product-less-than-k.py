"""
713. Subarray Product Less Than K
https://leetcode.com/problems/subarray-product-less-than-k/

Difficulty : Medium
Pattern    : Sliding Window
Tier       : Core
Scheduled  : Tue 29 Sep 2026  (week 3)

INPUT
    nums : list of integers
    k    : integer

RETURN
    integer

EXAMPLE
    nums = [686, 28, 455, 675, 605, 29, 942, 48, 502, ..., k =
    515854
    ->  8

RECOGNITION HINT  (read only AFTER a real attempt)
    Window on a product. Each valid window ending at r contributes (r -
    l + 1) subarrays.

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
    def numSubarrayProductLessThanK_brute(self, nums: List[int], k: int) -> int:
        pass


    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        pass


METHOD      = 'numSubarrayProductLessThanK'
PARAM_TYPES = ['integer[]', 'integer']
RETURN_TYPE = 'integer'
INPLACE_ARG = None

TESTS = [
    ([[686, 28, 455, 675, 605, 29, 942, 48, 502, 889, 854, 206, 231, 796, 272, 565, 887, 969, 558, 13, 22, 455, 145, 804, 15], 515854], 8),
    (
        [[542, 433, 935, 193, 280, 849, 122, 107, 688, 913, 31, 311, 814, 507, 596, 109, 340, 981, 662, 145, 955, 692, 659, 46, 276, 734, 177, 727, 329, 320, 93, 78, 451, 129, 226, 491, 595, 175, 894, 662, 699, 871, 340, 375, 98, 38, 414, 306, 20, 548, 459, 577, 626, 942, 92, 322, 665, 497, 593, 877, 247, 487, 67, 320, 78, 775, 431, 193, 175, 957, 926, 816, 776, 967, 600, 114, 474, 810, 513, 43, 586, 559, 880, 540, 122, 95, 408, 621, 850, 598], 425740],
        0,
    ),
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
