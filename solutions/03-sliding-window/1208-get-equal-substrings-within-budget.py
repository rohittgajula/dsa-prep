"""
1208. Get Equal Substrings Within Budget
https://leetcode.com/problems/get-equal-substrings-within-budget/

Difficulty : Medium
Pattern    : Sliding Window
Tier       : Stretch   (optional - skip without guilt if the week is tight)
Scheduled  : Fri 02 Oct 2026  (week 3)

RECOGNITION HINT  (read only AFTER a real attempt)
    Window valid while the accumulated cost stays within the budget.
    Shrink when it does not.

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
    # -----------------------------------------------------------------
    #  BRUTE FORCE   -- write this one first, even when it is obvious.
    #  Time  : O(?)      Space : O(?)
    # -----------------------------------------------------------------
    def equalSubstring_brute(self, s: str, t: str, maxCost: int) -> int:
        raise NotImplementedError("brute force")

    # -----------------------------------------------------------------
    #  OPTIMAL       -- what does the brute force redo that it need not?
    #  Time  : O(?)      Space : O(?)
    # -----------------------------------------------------------------
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        raise NotImplementedError("optimal")


# ---------------------------------------------------------------------
#  TEST CASES  --  taken from the examples on the LeetCode page
# ---------------------------------------------------------------------
METHOD      = 'equalSubstring'
PARAM_TYPES = ['string', 'string', 'integer']
RETURN_TYPE = 'integer'
INPLACE_ARG = None

TESTS = [
    # ( [args...], expected )
    (['abcd', 'bcdf', 3], 3),
    (['abcd', 'cdef', 3], 1),
    (['abcd', 'acde', 0], 1),
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
