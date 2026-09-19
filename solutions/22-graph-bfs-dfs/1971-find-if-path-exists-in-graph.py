"""
1971. Find If Path Exists In Graph
https://leetcode.com/problems/find-if-path-exists-in-graph/

Difficulty : Easy
Pattern    : Graph BFS/DFS
Tier       : Stretch   (optional - skip without guilt if the week is tight)
Scheduled  : Wed 03 Feb 2027  (week 21)

INPUT
    n           : integer
    edges       : grid of integers
    source      : integer
    destination : integer

RETURN
    true or false

EXAMPLE
    n = 3, edges = [[0, 1], [1, 2], [2, 0]], source = 0, destination
    = 2
    ->  True

RECOGNITION HINT  (read only AFTER a real attempt)
    Plain BFS/DFS reachability, or union-find.

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
    def validPath_brute(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        pass


    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        pass


METHOD      = 'validPath'
PARAM_TYPES = ['integer', 'integer[][]', 'integer', 'integer']
RETURN_TYPE = 'boolean'
INPLACE_ARG = None

TESTS = [
    ([3, [[0, 1], [1, 2], [2, 0]], 0, 2], True),
    ([6, [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], 0, 5], False),
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
