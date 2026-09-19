"""
93. Restore Ip Addresses
https://leetcode.com/problems/restore-ip-addresses/

Difficulty : Medium
Pattern    : Backtracking
Tier       : Stretch   (optional - skip without guilt if the week is tight)
Scheduled  : Sat 02 Jan 2027  (week 16)

INPUT
    s : string

RETURN
    list of strings

EXAMPLE
    s = '25525511135'
    ->  ['255.255.11.135', '255.255.111.35']

RECOGNITION HINT  (read only AFTER a real attempt)
    Try segments of length 1-3 with validity checks; exactly four
    segments must consume the whole string.

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
    def restoreIpAddresses_brute(self, s: str) -> List[str]:
        pass


    def restoreIpAddresses(self, s: str) -> List[str]:
        pass


METHOD      = 'restoreIpAddresses'
PARAM_TYPES = ['string']
RETURN_TYPE = 'list<string>'
INPLACE_ARG = None

TESTS = [
    (['25525511135'], ['255.255.11.135', '255.255.111.35']),
    (['0000'], ['0.0.0.0']),
    (['101023'], ['1.0.10.23', '1.0.102.3', '10.1.0.23', '10.10.2.3', '101.0.2.3']),
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
