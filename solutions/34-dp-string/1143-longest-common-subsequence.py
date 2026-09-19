"""
1143. Longest Common Subsequence
https://leetcode.com/problems/longest-common-subsequence/

Difficulty : Medium
Pattern    : DP String
Tier       : Core
Scheduled  : Mon 08 Mar 2027  (week 26)

INPUT
    text1 : string
    text2 : string

RETURN
    integer

EXAMPLE
    text1 = 'abcde', text2 = 'ace'
    ->  3

RECOGNITION HINT  (read only AFTER a real attempt)
    The parent of the whole string-DP family. Match extends the
    diagonal; mismatch takes the best neighbour.

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


class Solution:
    def longestCommonSubsequence_brute(self, text1: str, text2: str) -> int:
        pass


    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        pass


METHOD      = 'longestCommonSubsequence'
PARAM_TYPES = ['string', 'string']
RETURN_TYPE = 'integer'
INPLACE_ARG = None

TESTS = [
    (['abcde', 'ace'], 3),
    (['abc', 'abc'], 3),
    (['abc', 'def'], 0),
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
