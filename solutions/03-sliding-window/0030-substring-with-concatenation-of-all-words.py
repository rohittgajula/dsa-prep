"""
30. Substring With Concatenation Of All Words
https://leetcode.com/problems/substring-with-concatenation-of-all-words/

Difficulty : Hard
Pattern    : Sliding Window
Tier       : Stretch   (optional - skip without guilt if the week is tight)
Scheduled  : Sat 03 Oct 2026  (week 3)

INPUT
    s     : string
    words : list of strings

RETURN
    list of integers

EXAMPLE
    s = 'barfoothefoobarman', words = ['foo', 'bar']
    ->  [0, 9]

RECOGNITION HINT  (read only AFTER a real attempt)
    All words are the SAME length - that lets you window in word-sized
    steps with a frequency map.

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
    def findSubstring_brute(self, s: str, words: List[str]) -> List[int]:
        pass


    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        pass


METHOD      = 'findSubstring'
PARAM_TYPES = ['string', 'string[]']
RETURN_TYPE = 'list<integer>'
INPLACE_ARG = None

TESTS = [
    (['barfoothefoobarman', ['foo', 'bar']], [0, 9]),
    (['wordgoodgoodgoodbestword', ['word', 'good', 'best', 'word']], []),
    (['barfoofoobarthefoobarman', ['bar', 'foo', 'the']], [6, 9, 12]),
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
