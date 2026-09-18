"""
343. Integer Break
https://leetcode.com/problems/integer-break/

Difficulty : Medium
Pattern    : DP 1D
Tier       : Stretch   (optional - skip without guilt if the week is tight)
Scheduled  : Sun 28 Feb 2027  (week 24)

RECOGNITION HINT  (read only AFTER a real attempt)
    dp[i] = max over j of j * max(i-j, dp[i-j]). Or the maths: break
    into as many 3s as possible.

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


class Solution:
    def solve(self):
        raise NotImplementedError


if __name__ == "__main__":
    s = Solution()
    # tests
    print("ok")
