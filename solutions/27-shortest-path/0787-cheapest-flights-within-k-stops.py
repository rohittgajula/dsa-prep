"""
787. Cheapest Flights Within K Stops
https://leetcode.com/problems/cheapest-flights-within-k-stops/

Difficulty : Medium
Pattern    : Shortest Path
Tier       : Core
Scheduled  : Tue 16 Feb 2027  (week 23)

INPUT
    n       : integer
    flights : grid of integers
    src     : integer
    dst     : integer
    k       : integer

RETURN
    integer

EXAMPLE
    n = 4, flights = [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1,...,
    src = 0, dst = 3, k = 1
    ->  700

RECOGNITION HINT  (read only AFTER a real attempt)
    Dijkstra alone is WRONG with a stop limit - use Bellman-Ford for k+1
    rounds, or add stops to the state.

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
    def findCheapestPrice_brute(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        pass


    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        pass


METHOD      = 'findCheapestPrice'
PARAM_TYPES = ['integer', 'integer[][]', 'integer', 'integer', 'integer']
RETURN_TYPE = 'integer'
INPLACE_ARG = None

TESTS = [
    ([4, [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]], 0, 3, 1], 700),
    ([3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 1], 200),
    ([3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 0], 500),
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
