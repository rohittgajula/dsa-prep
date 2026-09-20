"""
460. Lfu Cache
https://leetcode.com/problems/lfu-cache/

Difficulty : Hard
Pattern    : Design DS
Tier       : Core
Scheduled  : Sat 03 Apr 2027  (week 29)

OPERATIONS
    LFUCache(capacity)   with capacity = integer
    get(key)  ->  integer
    put(key, value)  ->  nothing

RECOGNITION HINT  (read only AFTER a real attempt)
    Map of key->node, map of freq->doubly linked list, plus a minFreq
    pointer. Considerably harder than LRU.

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


class LFUCacheBrute:
    def __init__(self, capacity: int):
        pass


    def get(self, key: int) -> int:
        pass


    def put(self, key: int, value: int) -> None:
        pass


class LFUCache:
    def __init__(self, capacity: int):
        pass


    def get(self, key: int) -> int:
        pass


    def put(self, key: int, value: int) -> None:
        pass


CLASS_BRUTE   = LFUCacheBrute
CLASS_OPTIMAL = LFUCache

OPS      = ['LFUCache', 'put', 'put', 'get', 'put', 'get', 'get', 'put', 'get', 'get', 'get']
ARGS     = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
EXPECTED = [None, None, None, 1, None, -1, 3, None, -1, 3, 4]


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
