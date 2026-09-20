"""
341. Flatten Nested List Iterator
https://leetcode.com/problems/flatten-nested-list-iterator/

Difficulty : Medium
Pattern    : Design DS
Tier       : Stretch   (optional - skip without guilt if the week is tight)
Scheduled  : Sun 04 Apr 2027  (week 29)

INPUT
    this one hands you a class or a ready-made interface to work
    against rather than plain arguments - open the problem page and
    copy the starter code in.

HEADS UP
    LeetCode's test data does not line up with this method.
    no python3 signature in the LeetCode snippet.
    Build the real arguments by hand, then fill in TESTS below.

RAW JUDGE DATA
    inputs:
        [[1,1],2,[1,1]]
        [1,[4,[6]]]
    outputs:
        [1,1,2,1,1]
        [1,4,6]

RECOGNITION HINT  (read only AFTER a real attempt)
    Stack of iterators, or flatten eagerly. Lazy evaluation is the
    better answer.

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


class Solution:
    def solve_brute(self, *args):
        pass


    def solve(self, *args):
        pass


TESTS = [
]


if __name__ == "__main__":
    import ast
    import copy
    import inspect
    import textwrap

    def _todo(fn):
        try:
            body = ast.parse(textwrap.dedent(inspect.getsource(fn))).body[0].body
        except (OSError, TypeError, SyntaxError, IndexError):
            return False
        return len(body) == 1 and isinstance(body[0], (ast.Pass, ast.Expr))

    sol = Solution()
    for label, fname in (("BRUTE FORCE", 'solve_brute'), ("OPTIMAL    ", 'solve')):
        fn = getattr(sol, fname, None)
        if fn is None:
            continue
        print(f"{label} :")
        if _todo(fn):
            print("    not written yet\n")
            continue
        if not TESTS:
            print("    no test cases yet - see HEADS UP at the top of this file\n")
            continue
        for n, (args, want) in enumerate(TESTS, 1):
            try:
                got = fn(*copy.deepcopy(args))
            except Exception as exc:
                print(f"    case {n}: ERROR  {type(exc).__name__}: {exc}")
                continue
            mark = "PASS" if got == want else "FAIL"
            print(f"    case {n}: {mark:<20} got={got!r}  want={want!r}")
        print()
