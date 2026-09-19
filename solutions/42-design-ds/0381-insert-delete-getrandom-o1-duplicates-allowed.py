"""
381. Insert Delete Getrandom O1 Duplicates Allowed
https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed/

Difficulty : Hard
Pattern    : Design DS
Tier       : Stretch   (optional - skip without guilt if the week is tight)
Scheduled  : Mon 29 Mar 2027  (week 29)

RECOGNITION HINT  (read only AFTER a real attempt)
    Same as 380 but the map holds a SET of indices per value.

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


class RandomizedCollectionBrute:
    """Simplest thing that works. Get it correct, then beat it."""

    def __init__(self):
        raise NotImplementedError

    def insert(self, val: int) -> bool:
        raise NotImplementedError

    def remove(self, val: int) -> bool:
        raise NotImplementedError

    def getRandom(self) -> int:
        raise NotImplementedError


class RandomizedCollection:
    """The version you would actually submit."""

    def __init__(self):
        raise NotImplementedError

    def insert(self, val: int) -> bool:
        raise NotImplementedError

    def remove(self, val: int) -> bool:
        raise NotImplementedError

    def getRandom(self) -> int:
        raise NotImplementedError


# ---------------------------------------------------------------------
#  TEST CASES  --  the operation sequence from the LeetCode page
# ---------------------------------------------------------------------
CLASS_BRUTE   = RandomizedCollectionBrute
CLASS_OPTIMAL = RandomizedCollection

OPS      = ['RandomizedCollection', 'insert', 'insert', 'insert', 'getRandom', 'remove', 'getRandom']
ARGS     = [[], [1], [1], [2], [], [1], []]
EXPECTED = [None, True, False, True, 2, True, 1]


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
