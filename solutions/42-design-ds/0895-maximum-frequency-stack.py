"""
895. Maximum Frequency Stack
https://leetcode.com/problems/maximum-frequency-stack/

Difficulty : Hard
Pattern    : Design DS
Tier       : Stretch   (optional - skip without guilt if the week is tight)
Scheduled  : Wed 31 Mar 2027  (week 29)

RECOGNITION HINT  (read only AFTER a real attempt)
    Map from frequency to a stack of values, plus a running max
    frequency. Elegant once seen.

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


class FreqStackBrute:
    """Simplest thing that works. Get it correct, then beat it."""

    def __init__(self):
        raise NotImplementedError

    def push(self, val: int) -> None:
        raise NotImplementedError

    def pop(self) -> int:
        raise NotImplementedError


class FreqStack:
    """The version you would actually submit."""

    def __init__(self):
        raise NotImplementedError

    def push(self, val: int) -> None:
        raise NotImplementedError

    def pop(self) -> int:
        raise NotImplementedError


# ---------------------------------------------------------------------
#  TEST CASES  --  the operation sequence from the LeetCode page
# ---------------------------------------------------------------------
CLASS_BRUTE   = FreqStackBrute
CLASS_OPTIMAL = FreqStack

OPS      = ['FreqStack', 'push', 'push', 'push', 'push', 'push', 'push', 'pop', 'pop', 'pop', 'pop']
ARGS     = [[], [5], [7], [5], [7], [4], [5], [], [], [], []]
EXPECTED = [None, None, None, None, None, None, None, 5, 7, 5, 4]


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
