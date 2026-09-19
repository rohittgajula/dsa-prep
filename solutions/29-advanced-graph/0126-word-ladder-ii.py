"""
126. Word Ladder Ii
https://leetcode.com/problems/word-ladder-ii/

Difficulty : Hard
Pattern    : Advanced Graph
Tier       : Stretch   (optional - skip without guilt if the week is tight)
Scheduled  : Thu 18 Feb 2027  (week 23)

RECOGNITION HINT  (read only AFTER a real attempt)
    BFS to build the level graph, then backtrack through parent pointers
    to reconstruct all shortest paths.

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
    # -----------------------------------------------------------------
    #  BRUTE FORCE   -- write this one first, even when it is obvious.
    #  Time  : O(?)      Space : O(?)
    # -----------------------------------------------------------------
    def findLadders_brute(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        raise NotImplementedError("brute force")

    # -----------------------------------------------------------------
    #  OPTIMAL       -- what does the brute force redo that it need not?
    #  Time  : O(?)      Space : O(?)
    # -----------------------------------------------------------------
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        raise NotImplementedError("optimal")


# ---------------------------------------------------------------------
#  TEST CASES  --  taken from the examples on the LeetCode page
# ---------------------------------------------------------------------
METHOD      = 'findLadders'
PARAM_TYPES = ['string', 'string', 'list<string>']
RETURN_TYPE = 'list<list<string>>'
INPLACE_ARG = None

TESTS = [
    # ( [args...], expected )
    (['hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log', 'cog']], [['hit', 'hot', 'dot', 'dog', 'cog'], ['hit', 'hot', 'lot', 'log', 'cog']]),
    (['hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log']], []),
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
