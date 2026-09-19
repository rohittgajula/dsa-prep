"""
133. Clone Graph
https://leetcode.com/problems/clone-graph/

Difficulty : Medium
Pattern    : Graph BFS/DFS
Tier       : Core
Scheduled  : Sun 07 Feb 2027  (week 21)

RECOGNITION HINT  (read only AFTER a real attempt)
    DFS or BFS with a hashmap old->new. Create the copy BEFORE recursing
    or you loop forever.

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

from typing import List, Optional

#---------------------------------------------------------------------
#  HEADS UP - LeetCode's test data does not line up with this method.
#  arg 'edges' is really 'node'.
#  Uses LeetCode's Node class (val, neighbors). Input is an adjacency list.
#  Build the graph, clone it, then confirm no node object is shared with the original.
#---------------------------------------------------------------------


class Solution:
    # -----------------------------------------------------------------
    #  BRUTE FORCE   -- write this one first, even when it is obvious.
    #  Time  : O(?)      Space : O(?)
    # -----------------------------------------------------------------
    def cloneGraph_brute(self, node: Optional['Node']) -> Optional['Node']:
        raise NotImplementedError("brute force")

    # -----------------------------------------------------------------
    #  OPTIMAL       -- what does the brute force redo that it need not?
    #  Time  : O(?)      Space : O(?)
    # -----------------------------------------------------------------
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        raise NotImplementedError("optimal")


# ---------------------------------------------------------------------
#  The raw data LeetCode feeds its judge, for reference. Build the real
#  arguments from it by hand (see the heads-up above), then fill in TESTS.
# ---------------------------------------------------------------------
#  inputs :
#      [[2,4],[1,3],[2,4],[1,3]]
#      [[]]
#      []
#  outputs:
#      [[2,4],[1,3],[2,4],[1,3]]
#      [[]]
#      []

TESTS = [
    # ( [args...], expected )   <- write these yourself for this one
]


if __name__ == "__main__":
    if not TESTS:
        print("no test cases yet - see the heads-up at the top of this file")
    sol = Solution()
    for label, fname in (("BRUTE FORCE", 'cloneGraph_brute'), ("OPTIMAL    ", 'cloneGraph')):
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