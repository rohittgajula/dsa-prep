"""
399. Evaluate Division
https://leetcode.com/problems/evaluate-division/

Difficulty : Medium
Pattern    : Shortest Path
Tier       : Core
Scheduled  : Thu 18 Feb 2027  (week 23)

INPUT
    equations : grid of strings
    values    : list of decimal numbers
    queries   : grid of strings

RETURN
    list of decimal numbers

EXAMPLE
    equations = [['a', 'b'], ['b', 'c']], values = [2.0, 3.0],
    queries = [['a', 'c'], ['b', 'a'], ['a', 'e'], ['a', ...
    ->  [6.0, 0.5, -1.0, 1.0, -1.0]

RECOGNITION HINT  (read only AFTER a real attempt)
    Build a weighted graph of ratios; each query is a DFS multiplying
    edge weights along the path.

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


class Solution:
    def calcEquation_brute(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        pass


    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        pass


METHOD      = 'calcEquation'
PARAM_TYPES = ['list<list<string>>', 'double[]', 'list<list<string>>']
RETURN_TYPE = 'double[]'
INPLACE_ARG = None

TESTS = [
    ([[['a', 'b'], ['b', 'c']], [2.0, 3.0], [['a', 'c'], ['b', 'a'], ['a', 'e'], ['a', 'a'], ['x', 'x']]], [6.0, 0.5, -1.0, 1.0, -1.0]),
    ([[['a', 'b'], ['b', 'c'], ['bc', 'cd']], [1.5, 2.5, 5.0], [['a', 'c'], ['c', 'b'], ['bc', 'cd'], ['cd', 'bc']]], [3.75, 0.4, 5.0, 0.2]),
    ([[['a', 'b']], [0.5], [['a', 'b'], ['b', 'a'], ['a', 'c'], ['x', 'y']]], [0.5, 2.0, -1.0, -1.0]),
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
