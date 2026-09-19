"""
304. Range Sum Query 2D Immutable
https://leetcode.com/problems/range-sum-query-2d-immutable/

Difficulty : Medium
Pattern    : Prefix Sum
Tier       : Core
Scheduled  : Sun 11 Oct 2026  (week 4)

RECOGNITION HINT  (read only AFTER a real attempt)
    2D prefix sum. Inclusion-exclusion: total - top - left + topleft.

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


class NumMatrixBrute:
    """Simplest thing that works. Get it correct, then beat it."""

    def __init__(self, matrix: List[List[int]], matrixRowSize: int, matrixColSize: int):
        raise NotImplementedError

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        raise NotImplementedError


class NumMatrix:
    """The version you would actually submit."""

    def __init__(self, matrix: List[List[int]], matrixRowSize: int, matrixColSize: int):
        raise NotImplementedError

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        raise NotImplementedError


# ---------------------------------------------------------------------
#  TEST CASES  --  the operation sequence from the LeetCode page
# ---------------------------------------------------------------------
CLASS_BRUTE   = NumMatrixBrute
CLASS_OPTIMAL = NumMatrix

OPS      = ['NumMatrix', 'sumRegion', 'sumRegion', 'sumRegion']
ARGS     = [[[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]], [2, 1, 4, 3], [1, 1, 2, 2], [1, 2, 2, 4]]
EXPECTED = [None, 8, 11, 12]


# ---------------------------------------------------------------------
#  RUNNER  --  python3 this_file.py
#  Replays the LeetCode operation sequence against both versions.
# ---------------------------------------------------------------------
if __name__ == "__main__":
    def replay(cls, label):
        print(f"{label} :")
        obj = None
        for n, (op, args) in enumerate(zip(OPS, ARGS)):
            want = EXPECTED[n] if n < len(EXPECTED) else "?"
            try:
                if n == 0:
                    obj = cls(*args)
                    got = None
                else:
                    got = getattr(obj, op)(*args)
            except NotImplementedError:
                print("    -- not written yet --")
                return
            except Exception as exc:
                print(f"    {op}({args}) ERROR {type(exc).__name__}: {exc}")
                continue
            mark = "PASS" if got == want else "FAIL"
            if want == "?":
                mark = "----"
            print(f"    {n:>2}. {op}({str(args)[1:-1]:<12}) -> {str(got):<8} want {str(want):<8} {mark}")
        print()

    for cls, label in ((CLASS_BRUTE, "BRUTE FORCE"), (CLASS_OPTIMAL, "OPTIMAL    ")):
        replay(cls, label)
