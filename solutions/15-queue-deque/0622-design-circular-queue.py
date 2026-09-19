"""
622. Design Circular Queue
https://leetcode.com/problems/design-circular-queue/

Difficulty : Medium
Pattern    : Queue / Deque
Tier       : Core
Scheduled  : Tue 08 Dec 2026  (week 13)

RECOGNITION HINT  (read only AFTER a real attempt)
    Fixed array with head, tail and size. Modulo arithmetic; track size
    to distinguish full from empty.

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


class MyCircularQueueBrute:
    """Simplest thing that works. Get it correct, then beat it."""

    def __init__(self, k: int):
        raise NotImplementedError

    def enQueue(self, value: int) -> bool:
        raise NotImplementedError

    def deQueue(self) -> bool:
        raise NotImplementedError

    def Front(self) -> int:
        raise NotImplementedError

    def Rear(self) -> int:
        raise NotImplementedError

    def isEmpty(self) -> bool:
        raise NotImplementedError

    def isFull(self) -> bool:
        raise NotImplementedError


class MyCircularQueue:
    """The version you would actually submit."""

    def __init__(self, k: int):
        raise NotImplementedError

    def enQueue(self, value: int) -> bool:
        raise NotImplementedError

    def deQueue(self) -> bool:
        raise NotImplementedError

    def Front(self) -> int:
        raise NotImplementedError

    def Rear(self) -> int:
        raise NotImplementedError

    def isEmpty(self) -> bool:
        raise NotImplementedError

    def isFull(self) -> bool:
        raise NotImplementedError


# ---------------------------------------------------------------------
#  TEST CASES  --  the operation sequence from the LeetCode page
# ---------------------------------------------------------------------
CLASS_BRUTE   = MyCircularQueueBrute
CLASS_OPTIMAL = MyCircularQueue

OPS      = ['MyCircularQueue', 'enQueue', 'enQueue', 'enQueue', 'enQueue', 'Rear', 'isFull', 'deQueue', 'enQueue', 'Rear']
ARGS     = [[3], [1], [2], [3], [4], [], [], [], [4], []]
EXPECTED = [None, True, True, True, False, 3, True, True, True, 4]


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
