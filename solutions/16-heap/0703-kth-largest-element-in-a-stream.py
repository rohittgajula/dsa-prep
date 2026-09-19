"""
703. Kth Largest Element In A Stream
https://leetcode.com/problems/kth-largest-element-in-a-stream/

Difficulty : Easy
Pattern    : Heap
Tier       : Core
Scheduled  : Tue 15 Dec 2026  (week 14)

RECOGNITION HINT  (read only AFTER a real attempt)
    Maintain a min-heap of size exactly k. Its root is always the
    answer.

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


class KthLargestBrute:
    """Simplest thing that works. Get it correct, then beat it."""

    def __init__(self, k: int, nums: List[int], numsSize: int):
        raise NotImplementedError

    def add(self, val: int) -> int:
        raise NotImplementedError


class KthLargest:
    """The version you would actually submit."""

    def __init__(self, k: int, nums: List[int], numsSize: int):
        raise NotImplementedError

    def add(self, val: int) -> int:
        raise NotImplementedError


# ---------------------------------------------------------------------
#  TEST CASES  --  the operation sequence from the LeetCode page
# ---------------------------------------------------------------------
CLASS_BRUTE   = KthLargestBrute
CLASS_OPTIMAL = KthLargest

OPS      = ['KthLargest', 'add', 'add', 'add', 'add', 'add']
ARGS     = [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
EXPECTED = [None, 4, 5, 5, 8, 8]


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
