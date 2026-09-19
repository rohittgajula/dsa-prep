"""
355. Design Twitter
https://leetcode.com/problems/design-twitter/

Difficulty : Medium
Pattern    : Design DS
Tier       : Stretch   (optional - skip without guilt if the week is tight)
Scheduled  : Sat 03 Apr 2027  (week 29)

RECOGNITION HINT  (read only AFTER a real attempt)
    Hash maps for follows and tweets, then a k-way merge with a heap for
    the feed. A mini system design.

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

from typing import List


class TwitterBrute:
    """Simplest thing that works. Get it correct, then beat it."""

    def __init__(self):
        raise NotImplementedError

    def postTweet(self, userId: int, tweetId: int) -> None:
        raise NotImplementedError

    def getNewsFeed(self, userId: int) -> List[int]:
        raise NotImplementedError

    def follow(self, followerId: int, followeeId: int) -> None:
        raise NotImplementedError

    def unfollow(self, followerId: int, followeeId: int) -> None:
        raise NotImplementedError


class Twitter:
    """The version you would actually submit."""

    def __init__(self):
        raise NotImplementedError

    def postTweet(self, userId: int, tweetId: int) -> None:
        raise NotImplementedError

    def getNewsFeed(self, userId: int) -> List[int]:
        raise NotImplementedError

    def follow(self, followerId: int, followeeId: int) -> None:
        raise NotImplementedError

    def unfollow(self, followerId: int, followeeId: int) -> None:
        raise NotImplementedError


# ---------------------------------------------------------------------
#  TEST CASES  --  the operation sequence from the LeetCode page
# ---------------------------------------------------------------------
CLASS_BRUTE   = TwitterBrute
CLASS_OPTIMAL = Twitter

OPS      = ['Twitter', 'postTweet', 'getNewsFeed', 'follow', 'postTweet', 'getNewsFeed', 'unfollow', 'getNewsFeed']
ARGS     = [[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
EXPECTED = [None, None, [5], None, None, [6, 5], None, [5]]


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
