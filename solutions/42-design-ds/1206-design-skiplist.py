"""
1206. Design Skiplist
https://leetcode.com/problems/design-skiplist/

Difficulty : Hard
Pattern    : Design DS
Tier       : Stretch   (optional - skip without guilt if the week is tight)
Scheduled  : Thu 01 Apr 2027  (week 29)

RECOGNITION HINT  (read only AFTER a real attempt)
    Probabilistic multi-level linked list. Rarely asked but excellent
    for understanding randomised structures.

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


class SkiplistBrute:
    """Simplest thing that works. Get it correct, then beat it."""

    def __init__(self):
        raise NotImplementedError

    def search(self, target: int) -> bool:
        raise NotImplementedError

    def add(self, num: int) -> None:
        raise NotImplementedError

    def erase(self, num: int) -> bool:
        raise NotImplementedError


class Skiplist:
    """The version you would actually submit."""

    def __init__(self):
        raise NotImplementedError

    def search(self, target: int) -> bool:
        raise NotImplementedError

    def add(self, num: int) -> None:
        raise NotImplementedError

    def erase(self, num: int) -> bool:
        raise NotImplementedError


# ---------------------------------------------------------------------
#  TEST CASES  --  the operation sequence from the LeetCode page
# ---------------------------------------------------------------------
CLASS_BRUTE   = SkiplistBrute
CLASS_OPTIMAL = Skiplist

OPS      = ['Skiplist', 'add', 'add', 'add', 'search', 'add', 'search', 'erase', 'erase', 'search']
ARGS     = [[], [1], [2], [3], [0], [4], [1], [0], [1], [1]]
EXPECTED = [None, None, None, None, False, None, True, False, True, False]


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
