"""
211. Design Add And Search Words Data Structure
https://leetcode.com/problems/design-add-and-search-words-data-structure/

Difficulty : Medium
Pattern    : Trie
Tier       : Core
Scheduled  : Tue 26 Jan 2027  (week 20)

RECOGNITION HINT  (read only AFTER a real attempt)
    '.' wildcard forces DFS across all children at that level instead of
    a single lookup.

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


class WordDictionaryBrute:
    """Simplest thing that works. Get it correct, then beat it."""

    def __init__(self):
        raise NotImplementedError

    def addWord(self, word: str) -> None:
        raise NotImplementedError

    def search(self, word: str) -> bool:
        raise NotImplementedError


class WordDictionary:
    """The version you would actually submit."""

    def __init__(self):
        raise NotImplementedError

    def addWord(self, word: str) -> None:
        raise NotImplementedError

    def search(self, word: str) -> bool:
        raise NotImplementedError


# ---------------------------------------------------------------------
#  TEST CASES  --  the operation sequence from the LeetCode page
# ---------------------------------------------------------------------
CLASS_BRUTE   = WordDictionaryBrute
CLASS_OPTIMAL = WordDictionary

OPS      = ['WordDictionary', 'addWord', 'addWord', 'addWord', 'search', 'search', 'search', 'search']
ARGS     = [[], ['bad'], ['dad'], ['mad'], ['pad'], ['bad'], ['.ad'], ['b..']]
EXPECTED = [None, None, None, None, False, True, True, True]


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
