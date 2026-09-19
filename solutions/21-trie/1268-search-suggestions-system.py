"""
1268. Search Suggestions System
https://leetcode.com/problems/search-suggestions-system/

Difficulty : Medium
Pattern    : Trie
Tier       : Core
Scheduled  : Wed 27 Jan 2027  (week 20)

INPUT
    products   : list of strings
    searchWord : string

RETURN
    grid of strings

EXAMPLE
    products = ['mobile', 'mouse', 'moneypot', 'monitor', ...,
    searchWord = 'mouse'
    ->  [['mobile', 'moneypot', 'monitor'], ['mobil...

RECOGNITION HINT  (read only AFTER a real attempt)
    Insert all products, then at each prefix DFS for the three
    lexicographically smallest completions.

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
    def suggestedProducts_brute(self, products: List[str], searchWord: str) -> List[List[str]]:
        pass


    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        pass


METHOD      = 'suggestedProducts'
PARAM_TYPES = ['string[]', 'string']
RETURN_TYPE = 'list<list<string>>'
INPLACE_ARG = None

TESTS = [
    ([['mobile', 'mouse', 'moneypot', 'monitor', 'mousepad'], 'mouse'], [['mobile', 'moneypot', 'monitor'], ['mobile', 'moneypot', 'monitor'], ['mouse', 'mousepad'], ['mouse', 'mousepad'], ['mouse', 'mousepad']]),
    ([['havana'], 'havana'], [['havana'], ['havana'], ['havana'], ['havana'], ['havana'], ['havana']]),
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
