"""
752. Open The Lock
https://leetcode.com/problems/open-the-lock/

Difficulty : Medium
Pattern    : Graph BFS
Tier       : Stretch   (optional - skip without guilt if the week is tight)
Scheduled  : Thu 11 Feb 2027  (week 22)

INPUT
    deadends : list of strings
    target   : string

RETURN
    integer

EXAMPLE
    deadends = ['0201', '0101', '0102', '1212', '2002'], target =
    '0202'
    ->  6

RECOGNITION HINT  (read only AFTER a real attempt)
    BFS over a state space of 10^4 combinations. Deadends are just
    visited nodes seeded up front.

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
    def openLock_brute(self, deadends: List[str], target: str) -> int:
        pass


    def openLock(self, deadends: List[str], target: str) -> int:
        pass


METHOD      = 'openLock'
PARAM_TYPES = ['string[]', 'string']
RETURN_TYPE = 'integer'
INPLACE_ARG = None

TESTS = [
    ([['0201', '0101', '0102', '1212', '2002'], '0202'], 6),
    ([['8888'], '0009'], 1),
    ([['8887', '8889', '8878', '8898', '8788', '8988', '7888', '9888'], '8888'], -1),
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
