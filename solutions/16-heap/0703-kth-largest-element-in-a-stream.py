"""
703. Kth Largest Element In A Stream
https://leetcode.com/problems/kth-largest-element-in-a-stream/

Difficulty : Easy
Pattern    : Heap
Tier       : Core
Scheduled  : Tue 15 Dec 2026  (week 14)

OPERATIONS
    KthLargest(k, nums, numsSize)   with k = integer, nums = list of
    integers, numsSize = integer
    add(val)  ->  integer

RECOGNITION HINT  (read only AFTER a real attempt)
    Maintain a min-heap of size exactly k. Its root is always the
    answer.

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

from typing import List


class KthLargestBrute:
    def __init__(self, k: int, nums: List[int], numsSize: int):
        pass


    def add(self, val: int) -> int:
        pass


class KthLargest:
    def __init__(self, k: int, nums: List[int], numsSize: int):
        pass


    def add(self, val: int) -> int:
        pass


CLASS_BRUTE   = KthLargestBrute
CLASS_OPTIMAL = KthLargest

OPS      = ['KthLargest', 'add', 'add', 'add', 'add', 'add']
ARGS     = [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
EXPECTED = [None, 4, 5, 5, 8, 8]


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
