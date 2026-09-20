"""
1. Two Sum
https://leetcode.com/problems/two-sum/

Difficulty : Easy
Pattern    : Array Basics
Tier       : Core
Scheduled  : Thu 10 Sep 2026  (week 0)

INPUT
    nums   : list of integers
    target : integer

RETURN
    list of integers

EXAMPLE
    nums = [2, 7, 11, 15], target = 9
    ->  [0, 1]

RECOGNITION HINT  (read only AFTER a real attempt)
    Brute force is O(n^2). Ask: what am I searching for? The complement.
    Hash map turns that search into O(1).

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
    Try every pair. For each index i, walk the rest of the array looking for a
    j where nums[i] + nums[j] == target.
    Time  : O(n^2)   for each of n starting points we scan up to n more elements
    Space : O(1)     only the two loop indices are kept

OPTIMAL
    One pass with a hash map. For each number the partner it needs is
    target - num, so ask the map whether that partner has already been seen.
    The brute force rescans the array to answer that same question every time.
    Time  : O(n)     one pass, each lookup and insert O(1) on average
    Space : O(n)     the map can hold every element in the worst case

KEY INSIGHT
    You are not searching for a pair, you are searching for one complement -
    and a hash map turns that search into a lookup.

MISTAKES I MADE
    Not recorded - solved on 19 Sep, before this field was being kept.

Time taken: __ min      Solved unaided: Y      Hints used: N
Solved on: 2026-09-19   Revised: __
------------------------------------------------------------------------
"""

from typing import List


class Solution:
    def twoSum_brute(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i in range(len(nums)):
            needed = target - nums[i]
            if needed in hashMap:
                return [hashMap[needed], i]
            else:
                hashMap[nums[i]] = i


METHOD      = 'twoSum'
PARAM_TYPES = ['integer[]', 'integer']
RETURN_TYPE = 'integer[]'
INPLACE_ARG = None

TESTS = [
    ([[2, 7, 11, 15], 9], [0, 1]),
    ([[3, 2, 4], 6], [1, 2]),
    ([[3, 3], 6], [0, 1]),
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
            print(f"    case {n}: {_verdict(got, want):<20} got={got!r}  want={want!r}")
        print()
