"""
454. 4Sum Ii
https://leetcode.com/problems/4sum-ii/

Difficulty : Medium
Pattern    : Hashing
Tier       : Stretch   (optional - skip without guilt if the week is tight)
Scheduled  : Thu 15 Oct 2026  (week 5)

INPUT
    nums1 : list of integers
    nums2 : list of integers
    nums3 : list of integers
    nums4 : list of integers

RETURN
    integer

EXAMPLE
    nums1 = [1, 2], nums2 = [-2, -1], nums3 = [-1, 2], nums4 = [0,
    2]
    ->  2

RECOGNITION HINT  (read only AFTER a real attempt)
    Split 4 arrays into 2+2. Hash all sums of the first pair, then look
    up complements. O(n^2).

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
    def fourSumCount_brute(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        pass


    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        pass


METHOD      = 'fourSumCount'
PARAM_TYPES = ['integer[]', 'integer[]', 'integer[]', 'integer[]']
RETURN_TYPE = 'integer'
INPLACE_ARG = None

TESTS = [
    ([[1, 2], [-2, -1], [-1, 2], [0, 2]], 2),
    ([[0], [0], [0], [0]], 1),
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
