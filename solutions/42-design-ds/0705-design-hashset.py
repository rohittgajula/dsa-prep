"""
705. Design Hashset
https://leetcode.com/problems/design-hashset/

Difficulty : Easy
Pattern    : Design DS
Tier       : Stretch   (optional - skip without guilt if the week is tight)
Scheduled  : Thu 01 Apr 2027  (week 29)

OPERATIONS
    MyHashSet()
    add(key)  ->  nothing
    remove(key)  ->  nothing
    contains(key)  ->  true or false

RECOGNITION HINT  (read only AFTER a real attempt)
    Array of buckets plus chaining. Understand collision handling and
    load factor.

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


class MyHashSetBrute:
    def __init__(self):
        pass


    def add(self, key: int) -> None:
        pass


    def remove(self, key: int) -> None:
        pass


    def contains(self, key: int) -> bool:
        pass


class MyHashSet:
    def __init__(self):
        pass


    def add(self, key: int) -> None:
        pass


    def remove(self, key: int) -> None:
        pass


    def contains(self, key: int) -> bool:
        pass


CLASS_BRUTE   = MyHashSetBrute
CLASS_OPTIMAL = MyHashSet

OPS      = ['MyHashSet', 'add', 'add', 'add', 'remove', 'contains', 'add', 'add', 'add', 'remove', 'contains', 'add', 'add', 'add', 'remove', 'contains', 'add', 'add', 'add', 'remove', 'contains']
ARGS     = [[], [1], [10001], [1], [1], [1], [7], [10007], [7], [7], [7], [123], [10123], [123], [123], [123], [5000], [15000], [5000], [5000], [5000]]
EXPECTED = [None, None, None, True, False, None, True, None, False]


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
