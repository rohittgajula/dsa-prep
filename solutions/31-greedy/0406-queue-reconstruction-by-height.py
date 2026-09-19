"""
406. Queue Reconstruction By Height
https://leetcode.com/problems/queue-reconstruction-by-height/

Difficulty : Medium
Pattern    : Greedy
Tier       : Stretch   (optional - skip without guilt if the week is tight)
Scheduled  : Fri 26 Feb 2027  (week 24)

INPUT
    people : grid of integers

RETURN
    grid of integers

EXAMPLE
    people = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5...
    ->  [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7...

RECOGNITION HINT  (read only AFTER a real attempt)
    Sort by height descending and k ascending, then insert each person
    at index k.

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
    def reconstructQueue_brute(self, people: List[List[int]]) -> List[List[int]]:
        pass


    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        pass


METHOD      = 'reconstructQueue'
PARAM_TYPES = ['integer[][]']
RETURN_TYPE = 'integer[][]'
INPLACE_ARG = None

TESTS = [
    ([[[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]], [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]]),
    ([[[6, 0], [5, 0], [4, 0], [3, 2], [2, 2], [1, 4]]], [[4, 0], [5, 0], [2, 2], [3, 2], [1, 4], [6, 0]]),
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
