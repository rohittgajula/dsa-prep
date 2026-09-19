"""
733. Flood Fill
https://leetcode.com/problems/flood-fill/

Difficulty : Easy
Pattern    : Graph BFS/DFS
Tier       : Core
Scheduled  : Mon 01 Feb 2027  (week 21)

INPUT
    image : grid of integers
    sr    : integer
    sc    : integer
    color : integer

RETURN
    grid of integers

EXAMPLE
    image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]], sr = 1, sc = 1, color
    = 2
    ->  [[2, 2, 2], [2, 2, 0], [2, 0, 1]]

RECOGNITION HINT  (read only AFTER a real attempt)
    The simplest DFS on a grid. Guard against the start colour already
    equalling the new colour.

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
    def floodFill_brute(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        pass


    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        pass


METHOD      = 'floodFill'
PARAM_TYPES = ['integer[][]', 'integer', 'integer', 'integer']
RETURN_TYPE = 'integer[][]'
INPLACE_ARG = None

TESTS = [
    ([[[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2], [[2, 2, 2], [2, 2, 0], [2, 0, 1]]),
    ([[[0, 0, 0], [0, 0, 0]], 0, 0, 0], [[0, 0, 0], [0, 0, 0]]),
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
