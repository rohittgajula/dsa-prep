"""
322. Coin Change
https://leetcode.com/problems/coin-change/

Difficulty : Medium
Pattern    : DP Knapsack
Tier       : Core
Scheduled  : Mon 01 Mar 2027  (week 25)

RECOGNITION HINT  (read only AFTER a real attempt)
    Unbounded knapsack minimising count. dp[amount] = 1 + min over coins
    of dp[amount - coin].

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
