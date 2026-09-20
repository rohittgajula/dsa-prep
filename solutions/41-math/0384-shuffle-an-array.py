"""
384. Shuffle An Array
https://leetcode.com/problems/shuffle-an-array/

Difficulty : Medium
Pattern    : Math
Tier       : Stretch   (optional - skip without guilt if the week is tight)
Scheduled  : Tue 23 Mar 2027  (week 28)

OPERATIONS
    Solution(nums)   with nums = list of integers
    reset()  ->  list of integers
    shuffle()  ->  list of integers

HEADS UP
    Random by design - the expected output cannot be matched
    exactly. Check the shuffle is a permutation of the original and
    that reset() restores it.

RECOGNITION HINT  (read only AFTER a real attempt)
    Fisher-Yates: for each i, swap with a random index in [i, n).

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


class SolutionBrute:
    def __init__(self, nums: List[int]):
        pass


    def reset(self) -> List[int]:
        pass


    def shuffle(self) -> List[int]:
        pass


class Solution:
    def __init__(self, nums: List[int]):
        pass


    def reset(self) -> List[int]:
        pass


    def shuffle(self) -> List[int]:
        pass


CLASS_BRUTE   = SolutionBrute
CLASS_OPTIMAL = Solution

OPS      = ['Solution', 'shuffle', 'reset', 'shuffle']
ARGS     = [[[1, 2, 3]], [], [], []]
EXPECTED = [None, [3, 1, 2], [1, 2, 3], [1, 3, 2]]


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
