"""
677. Map Sum Pairs
https://leetcode.com/problems/map-sum-pairs/

Difficulty : Medium
Pattern    : Trie
Tier       : Stretch   (optional - skip without guilt if the week is tight)
Scheduled  : Sun 31 Jan 2027  (week 20)

RECOGNITION HINT  (read only AFTER a real attempt)
    Store values at terminal nodes, then DFS-sum the whole subtree under
    a prefix.

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


class MapSumBrute:
    """Simplest thing that works. Get it correct, then beat it."""

    def __init__(self):
        raise NotImplementedError

    def insert(self, key: str, val: int) -> None:
        raise NotImplementedError

    def sum(self, prefix: str) -> int:
        raise NotImplementedError


class MapSum:
    """The version you would actually submit."""

    def __init__(self):
        raise NotImplementedError

    def insert(self, key: str, val: int) -> None:
        raise NotImplementedError

    def sum(self, prefix: str) -> int:
        raise NotImplementedError


# ---------------------------------------------------------------------
#  TEST CASES  --  the operation sequence from the LeetCode page
# ---------------------------------------------------------------------
CLASS_BRUTE   = MapSumBrute
CLASS_OPTIMAL = MapSum

OPS      = ['MapSum', 'insert', 'sum', 'insert', 'sum']
ARGS     = [[], ['apple', 3], ['ap'], ['app', 2], ['ap']]
EXPECTED = [None, None, 3, None, 5]


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
