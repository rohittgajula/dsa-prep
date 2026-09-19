"""
208. Implement Trie Prefix Tree
https://leetcode.com/problems/implement-trie-prefix-tree/

Difficulty : Medium
Pattern    : Trie
Tier       : Core
Scheduled  : Mon 25 Jan 2027  (week 20)

OPERATIONS
    Trie()
    insert(word)  ->  nothing
    search(word)  ->  true or false
    startsWith(prefix)  ->  true or false

RECOGNITION HINT  (read only AFTER a real attempt)
    Build the base structure. Children map plus an is_end flag -
    everything else builds on this.

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


class TrieBrute:
    def __init__(self):
        pass


    def insert(self, word: str) -> None:
        pass


    def search(self, word: str) -> bool:
        pass


    def startsWith(self, prefix: str) -> bool:
        pass


class Trie:
    def __init__(self):
        pass


    def insert(self, word: str) -> None:
        pass


    def search(self, word: str) -> bool:
        pass


    def startsWith(self, prefix: str) -> bool:
        pass


CLASS_BRUTE   = TrieBrute
CLASS_OPTIMAL = Trie

OPS      = ['Trie', 'insert', 'search', 'search', 'startsWith', 'insert', 'search']
ARGS     = [[], ['apple'], ['apple'], ['app'], ['app'], ['app'], ['app']]
EXPECTED = [None, None, True, False, True, None, True]


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
