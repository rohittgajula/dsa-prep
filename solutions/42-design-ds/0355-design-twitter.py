"""
355. Design Twitter
https://leetcode.com/problems/design-twitter/

Difficulty : Medium
Pattern    : Design DS
Tier       : Stretch   (optional - skip without guilt if the week is tight)
Scheduled  : Sat 03 Apr 2027  (week 29)

OPERATIONS
    Twitter()
    postTweet(userId, tweetId)  ->  nothing
    getNewsFeed(userId)  ->  list of integers
    follow(followerId, followeeId)  ->  nothing
    unfollow(followerId, followeeId)  ->  nothing

RECOGNITION HINT  (read only AFTER a real attempt)
    Hash maps for follows and tweets, then a k-way merge with a heap for
    the feed. A mini system design.

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

from typing import List


class TwitterBrute:
    def __init__(self):
        pass


    def postTweet(self, userId: int, tweetId: int) -> None:
        pass


    def getNewsFeed(self, userId: int) -> List[int]:
        pass


    def follow(self, followerId: int, followeeId: int) -> None:
        pass


    def unfollow(self, followerId: int, followeeId: int) -> None:
        pass


class Twitter:
    def __init__(self):
        pass


    def postTweet(self, userId: int, tweetId: int) -> None:
        pass


    def getNewsFeed(self, userId: int) -> List[int]:
        pass


    def follow(self, followerId: int, followeeId: int) -> None:
        pass


    def unfollow(self, followerId: int, followeeId: int) -> None:
        pass


CLASS_BRUTE   = TwitterBrute
CLASS_OPTIMAL = Twitter

OPS      = ['Twitter', 'postTweet', 'getNewsFeed', 'follow', 'postTweet', 'getNewsFeed', 'unfollow', 'getNewsFeed']
ARGS     = [[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
EXPECTED = [None, None, [5], None, None, [6, 5], None, [5]]


if __name__ == "__main__":
    import ast
    import inspect
    import textwrap

    def _todo(cls):
        try:
            body = ast.parse(textwrap.dedent(inspect.getsource(cls.__init__))).body[0].body
        except (OSError, TypeError, SyntaxError, IndexError):
            return False
        return len(body) == 1 and isinstance(body[0], (ast.Pass, ast.Expr))

    def replay(cls, label):
        print(f"{label} :")
        if _todo(cls):
            print("    not written yet\n")
            return
        obj = None
        for n, (op, args) in enumerate(zip(OPS, ARGS)):
            want = EXPECTED[n] if n < len(EXPECTED) else "?"
            try:
                if n == 0:
                    obj = cls(*args)
                    got = None
                else:
                    got = getattr(obj, op)(*args)
            except Exception as exc:
                print(f"    {op}({args}) ERROR {type(exc).__name__}: {exc}")
                continue
            mark = "----" if want == "?" else ("PASS" if got == want else "FAIL")
            print(f"    {n:>2}. {op}({str(args)[1:-1]:<12}) -> {str(got):<8} want {str(want):<8} {mark}")
        print()

    for cls, label in ((CLASS_BRUTE, "BRUTE FORCE"), (CLASS_OPTIMAL, "OPTIMAL    ")):
        replay(cls, label)
