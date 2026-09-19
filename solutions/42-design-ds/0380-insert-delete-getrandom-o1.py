"""
380. Insert Delete Getrandom O1
https://leetcode.com/problems/insert-delete-getrandom-o1/

Difficulty : Medium
Pattern    : Design DS
Tier       : Core
Scheduled  : Tue 30 Mar 2027  (week 29)

OPERATIONS
    RandomizedSet()
    insert(val)  ->  true or false
    remove(val)  ->  true or false
    getRandom()  ->  integer

HEADS UP
    getRandom is random, so the recorded expected values will not
    always match. Judge it by whether the value returned is present
    in the set.

RECOGNITION HINT  (read only AFTER a real attempt)
    Array for random access plus a map of value to index; delete by
    swapping with the last element.

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


class RandomizedSetBrute:
    def __init__(self):
        pass


    def insert(self, val: int) -> bool:
        pass


    def remove(self, val: int) -> bool:
        pass


    def getRandom(self) -> int:
        pass


class RandomizedSet:
    def __init__(self):
        pass


    def insert(self, val: int) -> bool:
        pass


    def remove(self, val: int) -> bool:
        pass


    def getRandom(self) -> int:
        pass


CLASS_BRUTE   = RandomizedSetBrute
CLASS_OPTIMAL = RandomizedSet

OPS      = ['RandomizedSet', 'insert', 'remove', 'insert', 'getRandom', 'remove', 'insert', 'getRandom']
ARGS     = [[], [1], [2], [2], [], [1], [2], []]
EXPECTED = [None, True, False, True, 2, True, False, 2]


if __name__ == "__main__":
    import ast
    import inspect
    import textwrap

    def _todo(cls):
        try:
            body = ast.parse(textwrap.dedent(inspect.getsource(cls.__init__))).body[0].body
        except (OSError, TypeError, SyntaxError, IndexError):
            return False
        return len(body) == 1 and isinstance(body[0], (ast.Pass, ast.Expr))

    def replay(cls, label):
        print(f"{label} :")
        if _todo(cls):
            print("    not written yet\n")
            return
        obj = None
        for n, (op, args) in enumerate(zip(OPS, ARGS)):
            want = EXPECTED[n] if n < len(EXPECTED) else "?"
            try:
                if n == 0:
                    obj = cls(*args)
                    got = None
                else:
                    got = getattr(obj, op)(*args)
            except Exception as exc:
                print(f"    {op}({args}) ERROR {type(exc).__name__}: {exc}")
                continue
            mark = "----" if want == "?" else ("PASS" if got == want else "FAIL")
            print(f"    {n:>2}. {op}({str(args)[1:-1]:<12}) -> {str(got):<8} want {str(want):<8} {mark}")
        print()

    for cls, label in ((CLASS_BRUTE, "BRUTE FORCE"), (CLASS_OPTIMAL, "OPTIMAL    ")):
        replay(cls, label)
