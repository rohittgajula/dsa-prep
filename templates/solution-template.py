"""
<NUMBER>. <TITLE>
https://leetcode.com/problems/<slug>/

Difficulty : Easy | Medium | Hard
Pattern    : <pattern name>

INPUT
    nums : list of integers

RETURN
    integer

EXAMPLE
    nums = [1, 2, 3]
    ->  6

RECOGNITION HINT  (read only AFTER a real attempt)
    <what in the problem statement points at this pattern>

------------------------------------------------------------------------
BRUTE FORCE
    <the obvious approach, stated the way you would say it out loud>
    Time  : O(?)
    Space : O(?)

OPTIMAL
    <the better approach and WHY - what does the brute force redo?>
    Time  : O(?)
    Space : O(?)

KEY INSIGHT
    <the one sentence that makes this problem collapse>

MISTAKES I MADE
    <what tripped you up - the part worth re-reading>

Time taken: __ min      Solved unaided: Y / N
------------------------------------------------------------------------
"""
from typing import List


class Solution:
    def solve_brute(self, nums: List[int]) -> int:
        pass


    def solve(self, nums: List[int]) -> int:
        pass


METHOD      = 'solve'
PARAM_TYPES = ['integer[]']
RETURN_TYPE = 'integer'
INPLACE_ARG = None

TESTS = [
    ([[1, 2, 3]], 6),
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
