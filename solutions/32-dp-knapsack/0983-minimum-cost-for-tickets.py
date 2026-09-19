"""
983. Minimum Cost For Tickets
https://leetcode.com/problems/minimum-cost-for-tickets/

Difficulty : Medium
Pattern    : DP Knapsack
Tier       : Stretch   (optional - skip without guilt if the week is tight)
Scheduled  : Wed 03 Mar 2027  (week 25)

INPUT
    days  : list of integers
    costs : list of integers

RETURN
    integer

EXAMPLE
    days = [1, 4, 6, 7, 8, 20], costs = [2, 7, 15]
    ->  11

RECOGNITION HINT  (read only AFTER a real attempt)
    dp over days; from each travel day consider the 1, 7 and 30 day
    passes.

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
    def mincostTickets_brute(self, days: List[int], costs: List[int]) -> int:
        pass


    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        pass


METHOD      = 'mincostTickets'
PARAM_TYPES = ['integer[]', 'integer[]']
RETURN_TYPE = 'integer'
INPLACE_ARG = None

TESTS = [
    ([[1, 4, 6, 7, 8, 20], [2, 7, 15]], 11),
    ([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31], [2, 7, 15]], 17),
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
