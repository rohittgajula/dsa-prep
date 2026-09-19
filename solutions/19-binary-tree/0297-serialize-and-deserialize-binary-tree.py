"""
297. Serialize And Deserialize Binary Tree
https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

Difficulty : Hard
Pattern    : Binary Tree
Tier       : Core
Scheduled  : Sat 16 Jan 2027  (week 18)

RECOGNITION HINT  (read only AFTER a real attempt)
    Preorder with explicit null markers. Deserialise with an index
    pointer or an iterator.

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


#---------------------------------------------------------------------
#  HEADS UP - LeetCode's test data does not line up with this method.
#  no python3 signature in the LeetCode snippet.
#---------------------------------------------------------------------


class Solution:
    # -----------------------------------------------------------------
    #  BRUTE FORCE   -- write this one first, even when it is obvious.
    #  Time  : O(?)      Space : O(?)
    # -----------------------------------------------------------------
    def Codec_brute(self, *args):
        raise NotImplementedError("brute force")

    # -----------------------------------------------------------------
    #  OPTIMAL       -- what does the brute force redo that it need not?
    #  Time  : O(?)      Space : O(?)
    # -----------------------------------------------------------------
    def Codec(self, *args):
        raise NotImplementedError("optimal")


# ---------------------------------------------------------------------
#  The raw data LeetCode feeds its judge, for reference. Build the real
#  arguments from it by hand (see the heads-up above), then fill in TESTS.
# ---------------------------------------------------------------------
#  inputs :
#      [1,2,3,null,null,4,5]
#      []
#  outputs:
#      [1,2,3,null,null,4,5]
#      []

TESTS = [
    # ( [args...], expected )   <- write these yourself for this one
]


if __name__ == "__main__":
    if not TESTS:
        print("no test cases yet - see the heads-up at the top of this file")
    sol = Solution()
    for label, fname in (("BRUTE FORCE", 'Codec_brute'), ("OPTIMAL    ", 'Codec')):
        fn = getattr(sol, fname, None)
        if fn is None:
            continue
        print(f"{label} :")
        for n, (args, want) in enumerate(TESTS, 1):
            try:
                got = fn(*args)
            except NotImplementedError:
                print("    -- not written yet --")
                break
            except Exception as exc:
                print(f"    case {n}: ERROR  {type(exc).__name__}: {exc}")
                continue
            print(f"    case {n}: {'PASS' if got == want else 'FAIL'}   got={got!r}  want={want!r}")
        print()