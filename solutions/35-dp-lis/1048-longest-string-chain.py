"""
1048. Longest String Chain
https://leetcode.com/problems/longest-string-chain/

Difficulty : Medium
Pattern    : DP LIS
Tier       : Stretch   (optional - skip without guilt if the week is tight)
Scheduled  : Tue 09 Mar 2027  (week 26)

INPUT
    words : list of strings

RETURN
    integer

EXAMPLE
    words = ['a', 'b', 'ba', 'bca', 'bda', 'bdca']
    ->  4

RECOGNITION HINT  (read only AFTER a real attempt)
    Sort by length, then dp over predecessors formed by deleting one
    character.

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
    def longestStrChain_brute(self, words: List[str]) -> int:
        pass


    def longestStrChain(self, words: List[str]) -> int:
        pass


METHOD      = 'longestStrChain'
PARAM_TYPES = ['string[]']
RETURN_TYPE = 'integer'
INPLACE_ARG = None

TESTS = [
    ([['a', 'b', 'ba', 'bca', 'bda', 'bdca']], 4),
    ([['xbc', 'pcxbcf', 'xb', 'cxbc', 'pcxbc']], 5),
    ([['abcd', 'dbqca']], 1),
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
