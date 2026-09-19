"""
203. Remove Linked List Elements
https://leetcode.com/problems/remove-linked-list-elements/

Difficulty : Easy
Pattern    : Linked List
Tier       : Stretch   (optional - skip without guilt if the week is tight)
Scheduled  : Sat 28 Nov 2026  (week 11)

RECOGNITION HINT  (read only AFTER a real attempt)
    Textbook dummy node - the head itself may need removing.

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


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build_list(vals):
    """[1,2,3] -> 1 -> 2 -> 3"""
    head = None
    for v in reversed(vals or []):
        head = ListNode(v, head)
    return head


def dump_list(head, limit=500):
    """1 -> 2 -> 3 -> [1,2,3]   (limit guards against a cycle)"""
    out = []
    while head is not None and len(out) < limit:
        out.append(head.val)
        head = head.next
    return out


class Solution:
    # -----------------------------------------------------------------
    #  BRUTE FORCE   -- write this one first, even when it is obvious.
    #  Time  : O(?)      Space : O(?)
    # -----------------------------------------------------------------
    def removeElements_brute(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        raise NotImplementedError("brute force")

    # -----------------------------------------------------------------
    #  OPTIMAL       -- what does the brute force redo that it need not?
    #  Time  : O(?)      Space : O(?)
    # -----------------------------------------------------------------
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        raise NotImplementedError("optimal")


# ---------------------------------------------------------------------
#  TEST CASES  --  taken from the examples on the LeetCode page
# ---------------------------------------------------------------------
METHOD      = 'removeElements'
PARAM_TYPES = ['ListNode', 'integer']
RETURN_TYPE = 'ListNode'
INPLACE_ARG = None
NODE_BY_VALUE = []
RETURN_AS   = None

TESTS = [
    # ( [args...], expected )
    ([[1, 2, 6, 3, 4, 5, 6], 6], [1, 2, 3, 4, 5]),
    ([[], 1], []),
    ([[7, 7, 7, 7], 7], []),
]


# ---------------------------------------------------------------------
#  RUNNER  --  python3 this_file.py
#  Runs every test case against BOTH methods. A method you have not
#  written yet is skipped, so you can fill in brute force first.
# ---------------------------------------------------------------------
if __name__ == "__main__":
    import copy

    def _build(v, t):
        if t.startswith("ListNode"):
            return build_list(v)
        if t.startswith("TreeNode"):
            return build_tree(v)
        return v

    def _dump(v):
        if RETURN_TYPE.startswith("ListNode"):
            return dump_list(v)
        if RETURN_TYPE.startswith("TreeNode"):
            return dump_tree(v)
        return v

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
            call = [_build(copy.deepcopy(a), t) for a, t in zip(args, PARAM_TYPES)]
            for _i in NODE_BY_VALUE:          # judge sends a value, method wants the node
                call[_i] = find_node(call[0], call[_i])
            try:
                got = fn(*call)
            except NotImplementedError:
                print("    -- not written yet --")
                break
            except Exception as exc:
                print(f"    case {n}: ERROR  {type(exc).__name__}: {exc}")
                continue
            if INPLACE_ARG is not None:
                got = call[INPLACE_ARG]
            elif RETURN_AS == "node_val":
                got = got.val if got is not None else None
            else:
                got = _dump(got)
            print(f"    case {n}: {_verdict(got, want):<20} got={got!r}  want={want!r}")
        print()
