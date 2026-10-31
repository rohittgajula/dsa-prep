"""
6. Zigzag Conversion
https://leetcode.com/problems/zigzag-conversion/

Difficulty : Medium
Pattern    : Strings
Tier       : Stretch   (optional - skip without guilt if the week is tight)
Scheduled  : Fri 23 Oct 2026  (week 6)

INPUT
    s       : string
    numRows : integer

RETURN
    string

EXAMPLE
    s = 'PAYPALISHIRING', numRows = 3
    ->  'PAHNAPLSIIGYIR'

RECOGNITION HINT  (read only AFTER a real attempt)
    Simulate row by row with a direction that flips at the top and
    bottom rows.

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


class Solution:
    def convert_brute(self, s: str, numRows: int) -> str:
        pass


    def convert(self, s: str, numRows: int) -> str:
        pass


METHOD      = 'convert'
PARAM_TYPES = ['string', 'integer']
RETURN_TYPE = 'string'
INPLACE_ARG = None

TESTS = [
    (['PAYPALISHIRING', 3], 'PAHNAPLSIIGYIR'),
    (['PAYPALISHIRING', 4], 'PINALSIGYAHRPI'),
    (['A', 1], 'A'),
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
    for label, fname, brute in (("BRUTE FORCE", METHOD + "_brute", True),
                                ("OPTIMAL    ", METHOD, False)):
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
