"""
1898. Maximum Number Of Removable Characters
https://leetcode.com/problems/maximum-number-of-removable-characters/

Difficulty : Medium
Pattern    : Binary Search on Answer
Tier       : Stretch   (optional - skip without guilt if the week is tight)
Scheduled  : Sun 08 Nov 2026  (week 8)

INPUT
    s         : string
    p         : string
    removable : list of integers

RETURN
    integer

EXAMPLE
    s = 'abcacb', p = 'ab', removable = [3, 1, 0]
    ->  2

RECOGNITION HINT  (read only AFTER a real attempt)
    Search how many removals still leave p a subsequence. Monotonic:
    more removals is never easier.

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
    def maximumRemovals_brute(self, s: str, p: str, removable: List[int]) -> int:
        pass


    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        pass


METHOD      = 'maximumRemovals'
PARAM_TYPES = ['string', 'string', 'integer[]']
RETURN_TYPE = 'integer'
INPLACE_ARG = None

TESTS = [
    (['abcacb', 'ab', [3, 1, 0]], 2),
    (['abcbddddd', 'abcd', [3, 2, 1, 4, 5, 6]], 1),
    (['abcab', 'abc', [0, 1, 2, 3, 4]], 0),
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
