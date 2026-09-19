"""
211. Design Add And Search Words Data Structure
https://leetcode.com/problems/design-add-and-search-words-data-structure/

Difficulty : Medium
Pattern    : Trie
Tier       : Core
Scheduled  : Tue 26 Jan 2027  (week 20)

OPERATIONS
    WordDictionary()
    addWord(word)  ->  nothing
    search(word)  ->  true or false

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
    def __init__(self):
        pass


    def addWord(self, word: str) -> None:
        pass


    def search(self, word: str) -> bool:
        pass


class WordDictionary:
    def __init__(self):
        pass


    def addWord(self, word: str) -> None:
        pass


    def search(self, word: str) -> bool:
        pass


CLASS_BRUTE   = WordDictionaryBrute
CLASS_OPTIMAL = WordDictionary

OPS      = ['WordDictionary', 'addWord', 'addWord', 'addWord', 'search', 'search', 'search', 'search']
ARGS     = [[], ['bad'], ['dad'], ['mad'], ['pad'], ['bad'], ['.ad'], ['b..']]
EXPECTED = [None, None, None, None, False, True, True, True]


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
