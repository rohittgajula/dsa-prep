"""
<NUMBER>. <TITLE>
https://leetcode.com/problems/<slug>/

Difficulty : Easy | Medium | Hard
Pattern    : <pattern name>

------------------------------------------------------------------------
BRUTE FORCE
    <the obvious approach, stated the way you would say it out loud>
    Time  : O(?)
    Space : O(?)

OPTIMAL
    <the better approach and WHY - what does the brute force redo?>
    Time  : O(?)
    Space : O(?)

KEY INSIGHT
    <the one sentence that makes this problem collapse>

MISTAKES I MADE
    <what tripped you up - the part worth re-reading>

Time taken: __ min      Solved unaided: Y / N
------------------------------------------------------------------------
"""
from typing import List


class Solution:
    # -----------------------------------------------------------------
    #  BRUTE FORCE   -- write this one first, even when it is obvious.
    #  Time  : O(?)      Space : O(?)
    # -----------------------------------------------------------------
    def solve_brute(self, nums: List[int]) -> int:
        raise NotImplementedError("brute force")

    # -----------------------------------------------------------------
    #  OPTIMAL       -- what does the brute force redo that it need not?
    #  Time  : O(?)      Space : O(?)
    # -----------------------------------------------------------------
    def solve(self, nums: List[int]) -> int:
        raise NotImplementedError("optimal")


# ---------------------------------------------------------------------
#  TEST CASES  --  taken from the examples on the LeetCode page
# ---------------------------------------------------------------------
METHOD      = 'solve'
PARAM_TYPES = ['integer[]']
RETURN_TYPE = 'integer'
INPLACE_ARG = None      # index of the arg holding the answer, for in-place problems

TESTS = [
    # ( [args...], expected )
    ([[1, 2, 3]], 6),
]


# ---------------------------------------------------------------------
#  RUNNER  --  python3 this_file.py
#  Runs every test case against BOTH methods. A method you have not
#  written yet is skipped, so you can fill in brute force first.
# ---------------------------------------------------------------------
if __name__ == "__main__":
    import copy

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
        for n, (args, want) in enumerate(TESTS, 1):
            call = [copy.deepcopy(a) for a in args]
            try:
                got = fn(*call)
            except NotImplementedError:
                print("    -- not written yet --")
                break
            except Exception as exc:
                print(f"    case {n}: ERROR  {type(exc).__name__}: {exc}")
                continue
            print(f"    case {n}: {_verdict(got, want):<20} got={got!r}  want={want!r}")
        print()
