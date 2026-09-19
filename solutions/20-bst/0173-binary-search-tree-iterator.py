"""
173. Binary Search Tree Iterator
https://leetcode.com/problems/binary-search-tree-iterator/

Difficulty : Medium
Pattern    : BST
Tier       : Core
Scheduled  : Sat 23 Jan 2027  (week 19)

RECOGNITION HINT  (read only AFTER a real attempt)
    Controlled iterative inorder - keep a stack of left-spine nodes;
    next() pops and pushes the right subtree's left spine.

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


class BSTIteratorBrute:
    """Simplest thing that works. Get it correct, then beat it."""

    def __init__(self, root: Optional[TreeNode]):
        raise NotImplementedError

    def next(self) -> int:
        raise NotImplementedError

    def hasNext(self) -> bool:
        raise NotImplementedError


class BSTIterator:
    """The version you would actually submit."""

    def __init__(self, root: Optional[TreeNode]):
        raise NotImplementedError

    def next(self) -> int:
        raise NotImplementedError

    def hasNext(self) -> bool:
        raise NotImplementedError


# ---------------------------------------------------------------------
#  TEST CASES  --  the operation sequence from the LeetCode page
# ---------------------------------------------------------------------
CLASS_BRUTE   = BSTIteratorBrute
CLASS_OPTIMAL = BSTIterator

OPS      = ['BSTIterator', 'next', 'next', 'hasNext', 'next', 'hasNext', 'next', 'hasNext', 'next', 'hasNext']
ARGS     = [[[7, 3, 15, None, None, 9, 20]], [], [], [], [], [], [], [], [], []]
EXPECTED = [None, 3, 7, True, 9, True, 15, True, 20, False]


# ---------------------------------------------------------------------
#  RUNNER  --  python3 this_file.py
#  Replays the LeetCode operation sequence against both versions.
# ---------------------------------------------------------------------
if __name__ == "__main__":
    def replay(cls, label):
        print(f"{label} :")
        obj = None
        for n, (op, args) in enumerate(zip(OPS, ARGS)):
            want = EXPECTED[n] if n < len(EXPECTED) else "?"
            try:
                if n == 0:
                    obj = cls(*args)
                    got = None
                else:
                    got = getattr(obj, op)(*args)
            except NotImplementedError:
                print("    -- not written yet --")
                return
            except Exception as exc:
                print(f"    {op}({args}) ERROR {type(exc).__name__}: {exc}")
                continue
            mark = "PASS" if got == want else "FAIL"
            if want == "?":
                mark = "----"
            print(f"    {n:>2}. {op}({str(args)[1:-1]:<12}) -> {str(got):<8} want {str(want):<8} {mark}")
        print()

    for cls, label in ((CLASS_BRUTE, "BRUTE FORCE"), (CLASS_OPTIMAL, "OPTIMAL    ")):
        replay(cls, label)
