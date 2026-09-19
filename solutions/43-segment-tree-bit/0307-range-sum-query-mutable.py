"""
307. Range Sum Query Mutable
https://leetcode.com/problems/range-sum-query-mutable/

Difficulty : Medium
Pattern    : Segment Tree / BIT
Tier       : Core
Scheduled  : Wed 31 Mar 2027  (week 29)

OPERATIONS
    NumArray(nums)   with nums = list of integers
    update(index, val)  ->  nothing
    sumRange(left, right)  ->  integer

RECOGNITION HINT  (read only AFTER a real attempt)
    Range query WITH updates -> Fenwick tree or segment tree. Implement
    both at least once.

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


class NumArrayBrute:
    def __init__(self, nums: List[int]):
        pass


    def update(self, index: int, val: int) -> None:
        pass


    def sumRange(self, left: int, right: int) -> int:
        pass


class NumArray:
    def __init__(self, nums: List[int]):
        pass


    def update(self, index: int, val: int) -> None:
        pass


    def sumRange(self, left: int, right: int) -> int:
        pass


CLASS_BRUTE   = NumArrayBrute
CLASS_OPTIMAL = NumArray

OPS      = ['NumArray', 'sumRange', 'update', 'sumRange']
ARGS     = [[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]
EXPECTED = [None, 9, None, 8]


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
