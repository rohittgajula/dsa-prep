"""
307. Range Sum Query Mutable
https://leetcode.com/problems/range-sum-query-mutable/

Difficulty : Medium
Pattern    : Segment Tree / BIT
Tier       : Core
Scheduled  : Wed 31 Mar 2027  (week 29)

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

from typing import List, Optional


class NumArrayBrute:
    """Simplest thing that works. Get it correct, then beat it."""

    def __init__(self, nums: List[int]):
        raise NotImplementedError

    def update(self, index: int, val: int) -> None:
        raise NotImplementedError

    def sumRange(self, left: int, right: int) -> int:
        raise NotImplementedError


class NumArray:
    """The version you would actually submit."""

    def __init__(self, nums: List[int]):
        raise NotImplementedError

    def update(self, index: int, val: int) -> None:
        raise NotImplementedError

    def sumRange(self, left: int, right: int) -> int:
        raise NotImplementedError


# ---------------------------------------------------------------------
#  TEST CASES  --  the operation sequence from the LeetCode page
# ---------------------------------------------------------------------
CLASS_BRUTE   = NumArrayBrute
CLASS_OPTIMAL = NumArray

OPS      = ['NumArray', 'sumRange', 'update', 'sumRange']
ARGS     = [[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]
EXPECTED = [None, 9, None, 8]


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
