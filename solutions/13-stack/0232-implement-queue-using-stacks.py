"""
232. Implement Queue Using Stacks
https://leetcode.com/problems/implement-queue-using-stacks/

Difficulty : Easy
Pattern    : Stack
Tier       : Core
Scheduled  : Tue 01 Dec 2026  (week 12)

OPERATIONS
    MyQueue()
    push(x)  ->  nothing
    pop()  ->  integer
    peek()  ->  integer
    empty()  ->  true or false

RECOGNITION HINT  (read only AFTER a real attempt)
    Two stacks: in and out. Only move in->out when out is empty - that
    gives O(1) amortised.

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

Time taken: __ min      Solved unaided: Y / N
Solved on: __           Revised: __
------------------------------------------------------------------------
"""


class MyQueueBrute:
    def __init__(self):
        pass


    def push(self, x: int) -> None:
        pass


    def pop(self) -> int:
        pass


    def peek(self) -> int:
        pass


    def empty(self) -> bool:
        pass


class MyQueue:
    def __init__(self):
        pass


    def push(self, x: int) -> None:
        pass


    def pop(self) -> int:
        pass


    def peek(self) -> int:
        pass


    def empty(self) -> bool:
        pass


CLASS_BRUTE   = MyQueueBrute
CLASS_OPTIMAL = MyQueue

OPS      = ['MyQueue', 'push', 'push', 'peek', 'pop', 'empty']
ARGS     = [[], [1], [2], [], [], []]
EXPECTED = [None, None, None, 1, 1, False]


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
