"""
381. Insert Delete Getrandom O1 Duplicates Allowed
https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed/

Difficulty : Hard
Pattern    : Design DS
Tier       : Stretch   (optional - skip without guilt if the week is tight)
Scheduled  : Mon 29 Mar 2027  (week 29)

OPERATIONS
    RandomizedCollection()
    insert(val)  ->  true or false
    remove(val)  ->  true or false
    getRandom()  ->  integer

RECOGNITION HINT  (read only AFTER a real attempt)
    Same as 380 but the map holds a SET of indices per value.

------------------------------------------------------------------------
MY THINKING  (write this while you solve - raw, unedited)
    What the problem looked like at first:
        <>
    What I tried:
        <>
    Where I got stuck:
        <>
    What made it click:
        <>

    Tutor review:
        <>

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

Time taken: __ min      Solved unaided: Y / N      Hints used: __
Solved on: __           Revised: __
------------------------------------------------------------------------
"""


class RandomizedCollectionBrute:
    def __init__(self):
        pass


    def insert(self, val: int) -> bool:
        pass


    def remove(self, val: int) -> bool:
        pass


    def getRandom(self) -> int:
        pass


class RandomizedCollection:
    def __init__(self):
        pass


    def insert(self, val: int) -> bool:
        pass


    def remove(self, val: int) -> bool:
        pass


    def getRandom(self) -> int:
        pass


CLASS_BRUTE   = RandomizedCollectionBrute
CLASS_OPTIMAL = RandomizedCollection

OPS      = ['RandomizedCollection', 'insert', 'insert', 'insert', 'getRandom', 'remove', 'getRandom']
ARGS     = [[], [1], [1], [2], [], [1], []]
EXPECTED = [None, True, False, True, 2, True, 1]


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
