"""
1514. Path With Maximum Probability
https://leetcode.com/problems/path-with-maximum-probability/

Difficulty : Medium
Pattern    : Shortest Path
Tier       : Stretch   (optional - skip without guilt if the week is tight)
Scheduled  : Sat 20 Feb 2027  (week 23)

INPUT
    n          : integer
    edges      : grid of integers
    succProb   : list of decimal numbers
    start_node : integer
    end_node   : integer

RETURN
    decimal number

EXAMPLE
    n = 3, edges = [[0, 1], [1, 2], [0, 2]], succProb = [0.5, 0.5,
    0.2], start_node = 0, end_node = 2
    ->  0.25

RECOGNITION HINT  (read only AFTER a real attempt)
    Dijkstra with a MAX-heap, multiplying probabilities instead of
    adding weights.

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
    def maxProbability_brute(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        pass


    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        pass


METHOD      = 'maxProbability'
PARAM_TYPES = ['integer', 'integer[][]', 'double[]', 'integer', 'integer']
RETURN_TYPE = 'double'
INPLACE_ARG = None

TESTS = [
    ([3, [[0, 1], [1, 2], [0, 2]], [0.5, 0.5, 0.2], 0, 2], 0.25),
    ([3, [[0, 1], [1, 2], [0, 2]], [0.5, 0.5, 0.3], 0, 2], 0.3),
    ([3, [[0, 1]], [0.5], 0, 2], 0.0),
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
