"""
384. Shuffle An Array
https://leetcode.com/problems/shuffle-an-array/

Difficulty : Medium
Pattern    : Math
Tier       : Stretch   (optional - skip without guilt if the week is tight)
Scheduled  : Tue 23 Mar 2027  (week 28)

RECOGNITION HINT  (read only AFTER a real attempt)
    Fisher-Yates: for each i, swap with a random index in [i, n).

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


class SolutionBrute:
    """Simplest thing that works. Get it correct, then beat it."""

    def __init__(self, nums: List[int]):
        raise NotImplementedError

    def reset(self) -> List[int]:
        raise NotImplementedError

    def shuffle(self) -> List[int]:
        raise NotImplementedError


class Solution:
    """The version you would actually submit."""

    def __init__(self, nums: List[int]):
        raise NotImplementedError

    def reset(self) -> List[int]:
        raise NotImplementedError

    def shuffle(self) -> List[int]:
        raise NotImplementedError


#---------------------------------------------------------------------
#  HEADS UP - this problem has a custom judge on LeetCode.
#  Random by design - the expected output cannot be matched exactly. Check the
#  shuffle is a permutation of the original and that reset() restores it.
#---------------------------------------------------------------------
# ---------------------------------------------------------------------
#  TEST CASES  --  the operation sequence from the LeetCode page
# ---------------------------------------------------------------------
CLASS_BRUTE   = SolutionBrute
CLASS_OPTIMAL = Solution

OPS      = ['Solution', 'shuffle', 'reset', 'shuffle']
ARGS     = [[[1, 2, 3]], [], [], []]
EXPECTED = [None, [3, 1, 2], [1, 2, 3], [1, 3, 2]]


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
