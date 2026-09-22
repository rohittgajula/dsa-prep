"""
1697. Checking Existence Of Edge Length Limited Paths
https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/

Difficulty : Hard
Pattern    : MST
Tier       : Stretch   (optional - skip without guilt if the week is tight)
Scheduled  : Sun 21 Feb 2027  (week 23)

INPUT
    n        : integer
    edgeList : grid of integers
    queries  : grid of integers

RETURN
    list of booleans

EXAMPLE
    n = 3, edgeList = [[0, 1, 2], [1, 2, 4], [2, 0, 8], [1, 0, 16]],
    queries = [[0, 1, 2], [0, 2, 5]]
    ->  [False, True]

RECOGNITION HINT  (read only AFTER a real attempt)
    Sort queries AND edges by weight, then add edges incrementally with
    DSU (offline processing).

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

from typing import List


class Solution:
    def distanceLimitedPathsExist_brute(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        pass


    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        pass


METHOD      = 'distanceLimitedPathsExist'
PARAM_TYPES = ['integer', 'integer[][]', 'integer[][]']
RETURN_TYPE = 'boolean[]'
INPLACE_ARG = None

TESTS = [
    ([3, [[0, 1, 2], [1, 2, 4], [2, 0, 8], [1, 0, 16]], [[0, 1, 2], [0, 2, 5]]], [False, True]),
    ([5, [[0, 1, 10], [1, 2, 5], [2, 3, 9], [3, 4, 13]], [[0, 4, 14], [1, 4, 13]]], [True, False]),
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
    for label, fname, brute in (("BRUTE FORCE", METHOD + "_brute", True),
                                ("OPTIMAL    ", METHOD, False)):
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
