"""
1249. Minimum Remove To Make Valid Parentheses
https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

Difficulty : Medium
Pattern    : Stack
Tier       : Core
Scheduled  : Sat 05 Dec 2026  (week 12)

INPUT
    s : string

RETURN
    string

EXAMPLE
    s = 'lee(t(c)o)de)'
    ->  'lee(t(c)o)de'

RECOGNITION HINT  (read only AFTER a real attempt)
    Stack of indices for unmatched brackets, then build the result
    skipping those indices.

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


class Solution:
    def minRemoveToMakeValid_brute(self, s: str) -> str:
        pass


    def minRemoveToMakeValid(self, s: str) -> str:
        pass


METHOD      = 'minRemoveToMakeValid'
PARAM_TYPES = ['string']
RETURN_TYPE = 'string'
INPLACE_ARG = None

TESTS = [
    (['lee(t(c)o)de)'], 'lee(t(c)o)de'),
    (['a)b(c)d'], 'ab(c)d'),
    (['))(('], ''),
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
