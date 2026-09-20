"""
133. Clone Graph
https://leetcode.com/problems/clone-graph/

Difficulty : Medium
Pattern    : Graph BFS/DFS
Tier       : Core
Scheduled  : Sun 07 Feb 2027  (week 21)

INPUT
    node : node, see the problem page

HEADS UP
    LeetCode's test data does not line up with this method.
    arg 'edges' is really 'node'.
    Uses LeetCode's Node class (val, neighbors). Input is an
    adjacency list. Build the graph, clone it, then confirm no node
    object is shared with the original.
    Build the real arguments by hand, then fill in TESTS below.

RAW JUDGE DATA
    inputs:
        [[2,4],[1,3],[2,4],[1,3]]
        [[]]
        []
    outputs:
        [[2,4],[1,3],[2,4],[1,3]]
        [[]]
        []

RECOGNITION HINT  (read only AFTER a real attempt)
    DFS or BFS with a hashmap old->new. Create the copy BEFORE recursing
    or you loop forever.

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

from typing import Optional


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph_brute(self, node: Optional['Node']) -> Optional['Node']:
        pass


    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        pass


TESTS = [
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

    sol = Solution()
    for label, fname in (("BRUTE FORCE", 'cloneGraph_brute'), ("OPTIMAL    ", 'cloneGraph')):
        fn = getattr(sol, fname, None)
        if fn is None:
            continue
        print(f"{label} :")
        if _todo(fn):
            print("    not written yet\n")
            continue
        if not TESTS:
            print("    no test cases yet - see HEADS UP at the top of this file\n")
            continue
        for n, (args, want) in enumerate(TESTS, 1):
            try:
                got = fn(*copy.deepcopy(args))
            except Exception as exc:
                print(f"    case {n}: ERROR  {type(exc).__name__}: {exc}")
                continue
            mark = "PASS" if got == want else "FAIL"
            print(f"    case {n}: {mark:<20} got={got!r}  want={want!r}")
        print()
