"""
706. Design Hashmap
https://leetcode.com/problems/design-hashmap/

Difficulty : Easy
Pattern    : Design DS
Tier       : Stretch   (optional - skip without guilt if the week is tight)
Scheduled  : Fri 02 Apr 2027  (week 29)

OPERATIONS
    MyHashMap()
    put(key, value)  ->  nothing
    get(key)  ->  integer
    remove(key)  ->  nothing

RECOGNITION HINT  (read only AFTER a real attempt)
    Same as 705 but storing key-value pairs in each bucket.

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


class MyHashMapBrute:
    def __init__(self):
        pass


    def put(self, key: int, value: int) -> None:
        pass


    def get(self, key: int) -> int:
        pass


    def remove(self, key: int) -> None:
        pass


class MyHashMap:
    def __init__(self):
        pass


    def put(self, key: int, value: int) -> None:
        pass


    def get(self, key: int) -> int:
        pass


    def remove(self, key: int) -> None:
        pass


CLASS_BRUTE   = MyHashMapBrute
CLASS_OPTIMAL = MyHashMap

OPS      = ['MyHashMap', 'put', 'put', 'get', 'get', 'put', 'get', 'remove', 'get']
ARGS     = [[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
EXPECTED = [None, None, None, 1, -1, None, 1, None, -1]


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
