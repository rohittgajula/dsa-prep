"""
303. Range Sum Query Immutable
https://leetcode.com/problems/range-sum-query-immutable/

Difficulty : Easy
Pattern    : Prefix Sum
Tier       : Core
Scheduled  : Mon 05 Oct 2026  (week 4)

OPERATIONS
    NumArray(nums, numsSize)   with nums = list of integers,
    numsSize = integer
    sumRange(left, right)  ->  integer

RECOGNITION HINT  (read only AFTER a real attempt)
    Static array, many queries -> precompute prefix sums once.

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


class NumArrayBrute:
    def __init__(self, nums: List[int], numsSize: int):
        pass


    def sumRange(self, left: int, right: int) -> int:
        pass


class NumArray:
    def __init__(self, nums: List[int], numsSize: int):
        pass


    def sumRange(self, left: int, right: int) -> int:
        pass


CLASS_BRUTE   = NumArrayBrute
CLASS_OPTIMAL = NumArray

OPS      = ['NumArray', 'sumRange', 'sumRange', 'sumRange']
ARGS     = [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
EXPECTED = [None, 1, -1, -3]


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
