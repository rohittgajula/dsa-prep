"""
304. Range Sum Query 2D Immutable
https://leetcode.com/problems/range-sum-query-2d-immutable/

Difficulty : Medium
Pattern    : Prefix Sum
Tier       : Core
Scheduled  : Sun 11 Oct 2026  (week 4)

OPERATIONS
    NumMatrix(matrix, matrixRowSize, matrixColSize)   with matrix =
    grid of integers, matrixRowSize = integer, matrixColSize =
    integer
    sumRegion(row1, col1, row2, col2)  ->  integer

RECOGNITION HINT  (read only AFTER a real attempt)
    2D prefix sum. Inclusion-exclusion: total - top - left + topleft.

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


class NumMatrixBrute:
    def __init__(self, matrix: List[List[int]], matrixRowSize: int, matrixColSize: int):
        pass


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        pass


class NumMatrix:
    def __init__(self, matrix: List[List[int]], matrixRowSize: int, matrixColSize: int):
        pass


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        pass


CLASS_BRUTE   = NumMatrixBrute
CLASS_OPTIMAL = NumMatrix

OPS      = ['NumMatrix', 'sumRegion', 'sumRegion', 'sumRegion']
ARGS     = [[[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]], [2, 1, 4, 3], [1, 1, 2, 2], [1, 2, 2, 4]]
EXPECTED = [None, 8, 11, 12]


if __name__ == "__main__":
    import ast
    import inspect
    import textwrap

    def _todo(cls):
        try:
            body = ast.parse(textwrap.dedent(inspect.getsource(cls.__init__))).body[0].body
        except (OSError, TypeError, SyntaxError, IndexError):
            return False
        return len(body) == 1 and isinstance(body[0], (ast.Pass, ast.Expr))

    def replay(cls, label):
        print(f"{label} :")
        if _todo(cls):
            print("    not written yet\n")
            return
        obj = None
        for n, (op, args) in enumerate(zip(OPS, ARGS)):
            want = EXPECTED[n] if n < len(EXPECTED) else "?"
            try:
                if n == 0:
                    obj = cls(*args)
                    got = None
                else:
                    got = getattr(obj, op)(*args)
            except Exception as exc:
                print(f"    {op}({args}) ERROR {type(exc).__name__}: {exc}")
                continue
            mark = "----" if want == "?" else ("PASS" if got == want else "FAIL")
            print(f"    {n:>2}. {op}({str(args)[1:-1]:<12}) -> {str(got):<8} want {str(want):<8} {mark}")
        print()

    for cls, label in ((CLASS_BRUTE, "BRUTE FORCE"), (CLASS_OPTIMAL, "OPTIMAL    ")):
        replay(cls, label)
