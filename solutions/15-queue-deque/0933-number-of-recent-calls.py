"""
933. Number Of Recent Calls
https://leetcode.com/problems/number-of-recent-calls/

Difficulty : Easy
Pattern    : Queue / Deque
Tier       : Core
Scheduled  : Mon 07 Dec 2026  (week 13)

RECOGNITION HINT  (read only AFTER a real attempt)
    Queue; pop from the front while the timestamp falls outside the
    3000ms window.

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


class RecentCounterBrute:
    """Simplest thing that works. Get it correct, then beat it."""

    def __init__(self):
        raise NotImplementedError

    def ping(self, t: int) -> int:
        raise NotImplementedError


class RecentCounter:
    """The version you would actually submit."""

    def __init__(self):
        raise NotImplementedError

    def ping(self, t: int) -> int:
        raise NotImplementedError


# ---------------------------------------------------------------------
#  TEST CASES  --  the operation sequence from the LeetCode page
# ---------------------------------------------------------------------
CLASS_BRUTE   = RecentCounterBrute
CLASS_OPTIMAL = RecentCounter

OPS      = ['RecentCounter', 'ping', 'ping', 'ping', 'ping']
ARGS     = [[], [1], [100], [3001], [3002]]
EXPECTED = [None, 1, 2, 3, 3]


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
