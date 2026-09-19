"""
867. Transpose Matrix
https://leetcode.com/problems/transpose-matrix/

Difficulty : Easy
Pattern    : Matrix
Tier       : Stretch   (optional - skip without guilt if the week is tight)
Scheduled  : Sat 21 Nov 2026  (week 10)

INPUT
    matrix : grid of integers

RETURN
    grid of integers

EXAMPLE
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    ->  [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

RECOGNITION HINT  (read only AFTER a real attempt)
    Swap a[i][j] with a[j][i]. Trivial, but the building block for
    rotation.

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
    def transpose_brute(self, matrix: List[List[int]]) -> List[List[int]]:
        pass


    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        pass


METHOD      = 'transpose'
PARAM_TYPES = ['integer[][]']
RETURN_TYPE = 'integer[][]'
INPLACE_ARG = None

TESTS = [
    ([[[1, 2, 3], [4, 5, 6], [7, 8, 9]]], [[1, 4, 7], [2, 5, 8], [3, 6, 9]]),
    ([[[1, 2, 3], [4, 5, 6]]], [[1, 4], [2, 5], [3, 6]]),
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
