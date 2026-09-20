"""
212. Word Search Ii
https://leetcode.com/problems/word-search-ii/

Difficulty : Hard
Pattern    : Trie
Tier       : Core
Scheduled  : Sat 30 Jan 2027  (week 20)

INPUT
    board : grid of characters
    words : list of strings

RETURN
    list of strings

EXAMPLE
    board = [['o', 'a', 'a', 'n'], ['e', 't', 'a', 'e']..., words =
    ['oath', 'pea', 'eat', 'rain']
    ->  ['eat', 'oath']

RECOGNITION HINT  (read only AFTER a real attempt)
    Build a trie of all words, then DFS the grid ONCE, pruning wherever
    the prefix leaves the trie.

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

from typing import List


class Solution:
    def findWords_brute(self, board: List[List[str]], words: List[str]) -> List[str]:
        pass


    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        pass


METHOD      = 'findWords'
PARAM_TYPES = ['character[][]', 'string[]']
RETURN_TYPE = 'list<string>'
INPLACE_ARG = None

TESTS = [
    ([[['o', 'a', 'a', 'n'], ['e', 't', 'a', 'e'], ['i', 'h', 'k', 'r'], ['i', 'f', 'l', 'v']], ['oath', 'pea', 'eat', 'rain']], ['eat', 'oath']),
    ([[['a', 'b'], ['c', 'd']], ['abcb']], []),
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
