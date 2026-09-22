"""
66. Plus One
https://leetcode.com/problems/plus-one/

Difficulty : Easy
Pattern    : Array Basics
Tier       : Core
Scheduled  : Sun 13 Sep 2026  (week 0)

INPUT
    digits : list of integers

RETURN
    list of integers

EXAMPLE
    digits = [1, 2, 3]
    ->  [1, 2, 4]

RECOGNITION HINT  (read only AFTER a real attempt)
    Only the trailing 9s matter. Walk from the right; the all-9s case
    needs one extra leading digit.

------------------------------------------------------------------------
MY THINKING  (write this while you solve - raw, unedited)
    What the problem looked like at first:
        - i will traverse from the end, if the digit is 9 i will replace it with 0 and if the digit is not 9 then increase by one.
    What I tried:
        <>
    Where I got stuck:
        <>
    What made it click:
        <>

    Tutor review:
        Right: the carry chain is the real shape of the problem, and the right-to-left
               walk is the clean way to enforce it.
        Good: the all-9s branch is handled by the final prepend, which is the only
              missing edge case once the carry drains.
        Next time: state the invariant out loud - once you find the first non-9,
                   increment it and stop, because the suffix is already settled.

BRUTE FORCE
    Convert the digit list to a single integer, add one, then convert it back to a
    list of digits.
    Time  : O(n)     each conversion walks the whole number
    Space : O(n)     the integer is stringified and rebuilt into a new list

OPTIMAL
    Walk from the end of the array. If a digit is not 9, increment it and return.
    If it is 9, set it to 0 and keep moving. After the loop, prepend 1.
    The brute force wastes time by re-creating the entire number as a single value,
    even though only the trailing carry path matters.
    Time  : O(n)     at most one pass across the digits
    Space : O(1)     constant extra state, aside from the final leading carry

KEY INSIGHT
    Only the first non-9 from the right matters; every digit after it is already
    fixed by the carry chain.

MISTAKES I MADE
    - Missed the all-9s case until the return path was explicitly reasoned through.
    - Treated the operation as a full-number update instead of a right-to-left carry.

Time taken: 10 min      Solved unaided: Y      Hints used: N
Solved on: 2026-09-21   Revised: __
------------------------------------------------------------------------
"""

from typing import List


class Solution:
    def plusOne_brute(self, digits: List[int]) -> List[int]:
        num = int("".join(map(str, digits)))
        num += 1
        return [int(digit) for digit in str(num)]


    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1, -1, -1):
            if digits[i] != 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
        return [1] + digits



METHOD      = 'plusOne'
PARAM_TYPES = ['integer[]']
RETURN_TYPE = 'integer[]'
INPLACE_ARG = None

TESTS = [
    ([[1, 2, 3]], [1, 2, 4]),
    ([[4, 3, 2, 1]], [4, 3, 2, 2]),
    ([[9]], [1, 0]),
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
    for label, fname, brute in (("BRUTE FORCE", METHOD + "_brute", True),
                                ("OPTIMAL    ", METHOD, False)):
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
