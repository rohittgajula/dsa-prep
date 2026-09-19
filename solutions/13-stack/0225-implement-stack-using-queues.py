"""
225. Implement Stack Using Queues
https://leetcode.com/problems/implement-stack-using-queues/

Difficulty : Easy
Pattern    : Stack
Tier       : Stretch   (optional - skip without guilt if the week is tight)
Scheduled  : Wed 02 Dec 2026  (week 12)

OPERATIONS
    MyStack()
    push(x)  ->  nothing
    pop()  ->  integer
    top()  ->  integer
    empty()  ->  true or false

RECOGNITION HINT  (read only AFTER a real attempt)
    One queue, rotating after each push so the newest element sits at
    the front.

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


class MyStackBrute:
    def __init__(self):
        pass


    def push(self, x: int) -> None:
        pass


    def pop(self) -> int:
        pass


    def top(self) -> int:
        pass


    def empty(self) -> bool:
        pass


class MyStack:
    def __init__(self):
        pass


    def push(self, x: int) -> None:
        pass


    def pop(self) -> int:
        pass


    def top(self) -> int:
        pass


    def empty(self) -> bool:
        pass


CLASS_BRUTE   = MyStackBrute
CLASS_OPTIMAL = MyStack

OPS      = ['MyStack', 'push', 'push', 'top', 'pop', 'empty']
ARGS     = [[], [1], [2], [], [], []]
EXPECTED = [None, None, None, 2, 2, False]


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
