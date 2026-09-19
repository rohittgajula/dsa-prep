"""
705. Design Hashset
https://leetcode.com/problems/design-hashset/

Difficulty : Easy
Pattern    : Design DS
Tier       : Stretch   (optional - skip without guilt if the week is tight)
Scheduled  : Thu 01 Apr 2027  (week 29)

RECOGNITION HINT  (read only AFTER a real attempt)
    Array of buckets plus chaining. Understand collision handling and
    load factor.

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


class MyHashSetBrute:
    """Simplest thing that works. Get it correct, then beat it."""

    def __init__(self):
        raise NotImplementedError

    def add(self, key: int) -> None:
        raise NotImplementedError

    def remove(self, key: int) -> None:
        raise NotImplementedError

    def contains(self, key: int) -> bool:
        raise NotImplementedError


class MyHashSet:
    """The version you would actually submit."""

    def __init__(self):
        raise NotImplementedError

    def add(self, key: int) -> None:
        raise NotImplementedError

    def remove(self, key: int) -> None:
        raise NotImplementedError

    def contains(self, key: int) -> bool:
        raise NotImplementedError


# ---------------------------------------------------------------------
#  TEST CASES  --  the operation sequence from the LeetCode page
# ---------------------------------------------------------------------
CLASS_BRUTE   = MyHashSetBrute
CLASS_OPTIMAL = MyHashSet

OPS      = ['MyHashSet', 'add', 'add', 'add', 'remove', 'contains', 'add', 'add', 'add', 'remove', 'contains', 'add', 'add', 'add', 'remove', 'contains', 'add', 'add', 'add', 'remove', 'contains']
ARGS     = [[], [1], [10001], [1], [1], [1], [7], [10007], [7], [7], [7], [123], [10123], [123], [123], [123], [5000], [15000], [5000], [5000], [5000]]
EXPECTED = [None, None, None, True, False, None, True, None, False]


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
