"""
240. Search A 2D Matrix Ii
https://leetcode.com/problems/search-a-2d-matrix-ii/

Difficulty : Medium
Pattern    : Binary Search
Tier       : Core
Scheduled  : Sun 01 Nov 2026  (week 7)

RECOGNITION HINT  (read only AFTER a real attempt)
    Not fully sorted. Start at the TOP-RIGHT corner: too big means go
    left, too small means go down. O(m+n).

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
    # -----------------------------------------------------------------
    #  BRUTE FORCE   -- write this one first, even when it is obvious.
    #  Time  : O(?)      Space : O(?)
    # -----------------------------------------------------------------
    def searchMatrix_brute(self, matrix: List[List[int]], target: int) -> bool:
        raise NotImplementedError("brute force")

    # -----------------------------------------------------------------
    #  OPTIMAL       -- what does the brute force redo that it need not?
    #  Time  : O(?)      Space : O(?)
    # -----------------------------------------------------------------
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        raise NotImplementedError("optimal")


# ---------------------------------------------------------------------
#  TEST CASES  --  taken from the examples on the LeetCode page
# ---------------------------------------------------------------------
METHOD      = 'searchMatrix'
PARAM_TYPES = ['integer[][]', 'integer']
RETURN_TYPE = 'boolean'
INPLACE_ARG = None

TESTS = [
    # ( [args...], expected )
    ([[[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]], 5], True),
    ([[[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]], 20], False),
]


# ---------------------------------------------------------------------
#  RUNNER  --  python3 this_file.py
#  Runs every test case against BOTH methods. A method you have not
#  written yet is skipped, so you can fill in brute force first.
# ---------------------------------------------------------------------
if __name__ == "__main__":
    import copy

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
        for n, (args, want) in enumerate(TESTS, 1):
            call = [copy.deepcopy(a) for a in args]
            try:
                got = fn(*call)
            except NotImplementedError:
                print("    -- not written yet --")
                break
            except Exception as exc:
                print(f"    case {n}: ERROR  {type(exc).__name__}: {exc}")
                continue
            print(f"    case {n}: {_verdict(got, want):<20} got={got!r}  want={want!r}")
        print()
