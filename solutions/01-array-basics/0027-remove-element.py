"""
27. Remove Element
https://leetcode.com/problems/remove-element/

Difficulty : Easy
Pattern    : Array Basics
Tier       : Core
Scheduled  : Sat 12 Sep 2026  (week 0)

INPUT
    nums : list of integers
    val  : integer

RETURN
    the new length k, and nums holds the k kept values at the front

EXAMPLE
    nums = [3, 2, 2, 3], val = 3
    ->  nums starts with [2, 2]

RECOGNITION HINT  (read only AFTER a real attempt)
    Same slow-write/fast-read shape as 26. The array beyond the slow
    pointer is allowed to be garbage.

------------------------------------------------------------------------
MY THINKING  (write this while you solve - raw, unedited)
    What the problem looked like at first:
        <>
    What I tried:
        <>
    Where I got stuck:
        for bruteforce got struck with returning the solution, because caller was expecting nums, i was returning newArr
    What made it click:
        <>

    Tutor review:
        Right: the optimal came out in the correct shape first try, and you switched
               conventions from 26 on purpose - slow as the write slot, not the last
               kept index - which is the right call when the test is against an
               outside value.
        Wrong turn: assumed a LeetCode Accepted meant the local file held the same
               code. It did not; one line differed. Diff before theorising.
        Ask yourself next time: is my loop variable an index or a value?

BRUTE FORCE
    Walk the array once and copy every element that is not val into a new list.
    Then write that list back over the front of nums and return its length.
    Time  : O(n)     one pass to filter, one to copy back - both linear
    Space : O(n)     newArr holds every kept element; if val never appears
                     that is the entire array

OPTIMAL
    Two pointers moving the same direction. fast reads every index; slow is the
    next slot to write. An element is written only when it is not val, so the
    kept values compact toward the front and slow ends as the count.
    The brute force pays O(n) memory to stage an answer that can be built inside
    the array itself - nothing beyond slow is ever needed again, so those slots
    are free to overwrite.
    Time  : O(n)     each element is read once and written at most once
    Space : O(1)     two integer counters, no second array

KEY INSIGHT
    The write pointer can never overtake the read pointer, so the array can be
    compacted into itself as it is scanned.

MISTAKES I MADE
    - Brute force did `nums, newArr = newArr, nums`, which swaps two local names
      and leaves the caller's list untouched. Needed `nums[:] = newArr`. Third
      variant of the same in-place slip in two days - see notes/weak-topics.md.
    - Started from the idea that a brute force is allowed to skip the in-place
      contract. It is not: brute describes wasted work, never a changed signature.
    - Optimal used `for fast in nums`, iterating values and then indexing by them.
      Case 1 passed by luck because every value in [3,2,2,3] is a valid index of a
      length-4 array; nums=[100,2] raises IndexError outright.

Time taken: 15 min      Solved unaided: Y      Hints used: Y
Solved on: 2026-09-21   Revised: __
------------------------------------------------------------------------
"""

from typing import List


class Solution:
    def removeElement_brute(self, nums: List[int], val: int) -> int:
        newArr = []
        for i in range(len(nums)):
            if nums[i] != val:
                newArr.append(nums[i])
        # nums, newArr = newArr, nums               # Swapping will not work, bcz caller check actual array.
        nums[:] = newArr
        return len(newArr)


    def removeElement(self, nums: List[int], val: int) -> int:
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
        return slow


METHOD      = 'removeElement'
PARAM_TYPES = ['integer[]', 'integer']
RETURN_TYPE = 'integer'
INPLACE_ARG = 0
INPLACE_PREFIX = True

TESTS = [
    ([[3, 2, 2, 3], 3], [2, 2]),
    ([[0, 1, 2, 2, 3, 0, 4, 2], 2], [0, 1, 4, 0, 3]),
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
            got = call[INPLACE_ARG][:got] if isinstance(got, int) else call[INPLACE_ARG]
            print(f"    case {n}: {_verdict(got, want):<20} got={got!r}  want={want!r}")
        print()
