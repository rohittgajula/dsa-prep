"""
85. Maximal Rectangle
https://leetcode.com/problems/maximal-rectangle/

Difficulty : Hard
Pattern    : Monotonic Stack
Tier       : Stretch   (optional - skip without guilt if the week is tight)
Scheduled  : Fri 04 Dec 2026  (week 12)

INPUT
    matrix : grid of characters

RETURN
    integer

EXAMPLE
    matrix = [['1', '0', '1', '0', '0'], ['1', '0', '1',...
    ->  6

RECOGNITION HINT  (read only AFTER a real attempt)
    Treat each row as a histogram of heights above it, then apply 84 to
    every row.

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

from typing import List


class Solution:
    def maximalRectangle_brute(self, matrix: List[List[str]]) -> int:
        pass


    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        pass


METHOD      = 'maximalRectangle'
PARAM_TYPES = ['character[][]']
RETURN_TYPE = 'integer'
INPLACE_ARG = None

TESTS = [
    ([[['1', '0', '1', '0', '0'], ['1', '0', '1', '1', '1'], ['1', '1', '1', '1', '1'], ['1', '0', '0', '1', '0']]], 6),
    ([[['0']]], 0),
    ([[['1']]], 1),
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

    def _verdict(got, want):
        if got == want:
            return "PASS"
        if isinstance(got, float) or isinstance(want, float):
            try:
                if abs(float(got) - float(want)) < 1e-5:
                    return "PASS"
            except (TypeError, ValueError):
                pass
        if isinstance(got, list) and isinstance(want, list):
            try:
                if sorted(map(repr, got)) == sorted(map(repr, want)):
                    return "PASS (order ignored)"
            except TypeError:
                pass
        return "FAIL"

    sol = Solution()
    for label, fname in (("BRUTE FORCE", METHOD + "_brute"), ("OPTIMAL    ", METHOD)):
        fn = getattr(sol, fname, None)
        if fn is None:
            continue
        print(f"{label} :")
        if _todo(fn):
            print("    not written yet\n")
            continue
        for n, (args, want) in enumerate(TESTS, 1):
            call = [copy.deepcopy(a) for a in args]
            try:
                got = fn(*call)
            except Exception as exc:
                print(f"    case {n}: ERROR  {type(exc).__name__}: {exc}")
                continue
            print(f"    case {n}: {_verdict(got, want):<20} got={got!r}  want={want!r}")
        print()
