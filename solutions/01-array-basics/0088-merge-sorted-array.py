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
    optimal : nothing is returned - nums1 itself is changed
    brute   : may return the finished result instead - the runner
              accepts either

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
        Right: filled from the back, which avoids shifting nums1's real values.
        Wrong turn: brute force needed a hint, so the first approach was not fully cold.
        Ask yourself next time: where is the spare space, and which direction avoids overwriting?

BRUTE FORCE
    Put nums2 after the first m real values in nums1, then sort the whole array.
    Time  : O((m + n) log(m + n))    sorting all m + n values dominates
    Space : O(1) extra               nums1 already has the buffer

OPTIMAL
    Merge from the back so the empty slots in nums1 are filled first and no shifting is needed.
    Time  : O(m + n)    each real value is copied at most once
    Space : O(1)        only three pointers are used

KEY INSIGHT
    Since nums1 has empty space at the end, compare the largest remaining values and write from right to left.

MISTAKES I MADE
    None recorded this session.

Time taken: 20 min      Solved unaided: Y      Hints used: Y
Solved on: 2026-09-23   Revised: __
------------------------------------------------------------------------
"""

from typing import List


class Solution:
    def merge_brute(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for i in range(n):
            nums1[m+i] = nums2[i]
        return nums1.sort()
        


    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = m-1
        j = n-1
        k = (m+n)-1

        while i >=0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
        return nums1



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
            if not (brute and got is not None):
                got = call[INPLACE_ARG]
            print(f"    case {n}: {_verdict(got, want):<20} got={got!r}  want={want!r}")
        print()
