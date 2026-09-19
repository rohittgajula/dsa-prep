"""
40. Combination Sum Ii
https://leetcode.com/problems/combination-sum-ii/

Difficulty : Medium
Pattern    : Backtracking
Tier       : Stretch   (optional - skip without guilt if the week is tight)
Scheduled  : Wed 30 Dec 2026  (week 16)

INPUT
    candidates : list of integers
    target     : integer

RETURN
    grid of integers

EXAMPLE
    candidates = [10, 1, 2, 7, 6, 1, 5], target = 8
    ->  [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]

RECOGNITION HINT  (read only AFTER a real attempt)
    Each number used once (i+1) plus duplicate skipping. Sort first.

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
    def combinationSum2_brute(self, candidates: List[int], target: int) -> List[List[int]]:
        pass


    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        pass


METHOD      = 'combinationSum2'
PARAM_TYPES = ['integer[]', 'integer']
RETURN_TYPE = 'list<list<integer>>'
INPLACE_ARG = None

TESTS = [
    ([[10, 1, 2, 7, 6, 1, 5], 8], [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]),
    ([[2, 5, 2, 1, 2], 5], [[1, 2, 2], [5]]),
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
