"""
26. Remove Duplicates From Sorted Array
https://leetcode.com/problems/remove-duplicates-from-sorted-array/

Difficulty : Easy
Pattern    : Array Basics
Tier       : Core
Scheduled  : Fri 11 Sep 2026  (week 0)

INPUT
    nums : list of integers

RETURN
    the new length k, and nums holds the k kept values at the front

EXAMPLE
    nums = [1, 1, 2]
    ->  nums starts with [1, 2]

RECOGNITION HINT  (read only AFTER a real attempt)
    Two pointers, same direction: a slow WRITE pointer and a fast READ
    pointer. Slow only advances on a new value.

------------------------------------------------------------------------
MY THINKING  (write this while you solve - raw, unedited)
    What the problem looked like at first:
        this is mostly a two pointer approach, initially i will start with fast & slow pointers, fast pointer itirates through all the elements
        slow pointer points at the place in which we need to replace with the non-duplicate num
    What I tried:
        <>
    Where I got stuck:
        <>
    What made it click:
        <>

    Tutor review:
        Right: pointer mechanics correct, and you stated precisely what slow points at
               - that is the part most people fumble. Your own convention, not a copy.
        Wrong turn: led with the technique ("this is mostly a two pointer approach")
               instead of the observation that sortedness makes duplicates adjacent.
        Ask yourself next time: what does the input guarantee, and what does that let me skip?
        Note: empty array returns 1, not 0. Outside this problem's constraints
               (n >= 1), so not a failure here - but the convention carries it.

BRUTE FORCE
    Collect the values not already kept, then write them back over the front of
    nums. Membership is tested by scanning what has been kept so far.
    Time  : O(n^2)   `num not in sol` scans the kept list once per element
    Space : O(n)     sol holds every unique value before it is written back

OPTIMAL
    Two pointers. slow is the last index already kept; fast walks the array.
    Because the input is sorted, duplicates sit next to each other, so one
    comparison against nums[slow] decides whether fast is a new value.
    The brute force searches everything already kept to answer that same
    question - the sortedness makes the search unnecessary.
    Time  : O(n)     fast crosses the array once, each step O(1)
    Space : O(1)     written in place, only the two indices are kept

KEY INSIGHT
    Sorted means duplicates are adjacent, so you never have to search what you
    already kept - comparing against the last kept value is enough.

MISTAKES I MADE
    - Returned a new list instead of mutating nums. The judge scores nums[:k],
      so building the answer somewhere else scores nothing.
    - Wrote `nums[:len(sol)]` with no `=`. A bare slice is an expression: it
      evaluates and is thrown away. Right k, untouched array - that combination
      is the signature of a missing in-place write.
    - The brute force never used the sorted constraint; it works fine on
      unsorted input. That was the tell that the whole optimisation was still
      on the table, and it was missed.
    - `slow + 1` assumes at least one element. The problem guarantees n >= 1 so
      it is safe here, but the convention needs a guard anywhere it is not.

Time taken: __ min      Solved unaided: N
Solved on: 2026-09-20   Revised: __
------------------------------------------------------------------------
"""

from typing import List


class Solution:
    def removeDuplicates_brute(self, nums: List[int]) -> int:
        sol = []
        for num in nums:
            # print(num)
            if num not in sol:
                # print(f"loop : {num}")
                sol.append(num)
        nums[:len(sol)] = sol
        return len(sol)


    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
        return slow + 1


METHOD      = 'removeDuplicates'
PARAM_TYPES = ['integer[]']
RETURN_TYPE = 'integer'
INPLACE_ARG = 0
INPLACE_PREFIX = True

TESTS = [
    ([[1, 1, 2]], [1, 2]),
    ([[0, 0, 1, 1, 1, 2, 2, 3, 3, 4]], [0, 1, 2, 3, 4]),
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
