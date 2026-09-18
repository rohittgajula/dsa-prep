# O(1) Insert / Delete / GetRandom

`Week 29` · Design

## Recognise it when

- *"Insert, delete AND get a uniformly random element, all in O(1)"*

## The insight

Random access in O(1) **requires an array** — you need to index by a random integer.

But deleting from an array is O(n)… **unless order does not matter**. Then you can swap the target with the **last** element and pop, which is O(1).

A hash map from value → index makes finding the target O(1).

## Diagram

```
  vals = [10, 20, 30, 40]        idx = {10:0, 20:1, 30:2, 40:3}
           0   1   2   3

  getRandom() → vals[randint(0, 3)]          O(1)  ✓

  remove(20):
     1. i = idx[20] = 1
     2. last = vals[-1] = 40
     3. move `last` into the hole:

        vals = [10, 40, 30, 40]     vals[1] = 40
                 0   1   2   3
                     ▲
                 the hole is filled

     4. update the moved element's index:  idx[40] = 1     ← EASY TO FORGET
     5. pop the tail and drop the old key:

        vals = [10, 40, 30]         idx = {10:0, 40:1, 30:2}

  Order is scrambled - which is fine, because nothing promised order.
```

### The edge case that bites

```
  remove the LAST element:

     vals = [10, 20]      remove(20)
     i = 1, last = vals[-1] = 20      ← the element IS the last one
     vals[1] = 20                      harmless self-assignment
     idx[20] = 1                       sets the key you are about to delete
     vals.pop()                        fine
     del idx[20]                       fine - deleted after, so no leak

  Order matters here: delete the map entry AFTER the reassignment,
  or you resurrect a stale key.
```

## Template

```python
import random

class RandomizedSet:
    def __init__(self):
        self.vals: list[int] = []
        self.idx: dict[int, int] = {}

    def insert(self, val: int) -> bool:
        if val in self.idx:
            return False
        self.idx[val] = len(self.vals)
        self.vals.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.idx:
            return False
        i = self.idx[val]
        last = self.vals[-1]
        self.vals[i] = last            # move the last element into the hole
        self.idx[last] = i             # update ITS index - the classic miss
        self.vals.pop()
        del self.idx[val]              # delete AFTER, not before
        return True

    def getRandom(self) -> int:
        return random.choice(self.vals)
```

### With duplicates allowed (LC 381)

The map now holds a **set of indices** per value:

```python
from collections import defaultdict

class RandomizedCollection:
    def __init__(self):
        self.vals: list[int] = []
        self.idx: dict[int, set[int]] = defaultdict(set)

    def insert(self, val: int) -> bool:
        absent = not self.idx[val]
        self.idx[val].add(len(self.vals))
        self.vals.append(val)
        return absent

    def remove(self, val: int) -> bool:
        if not self.idx[val]:
            return False
        i = self.idx[val].pop()
        last = self.vals[-1]
        self.vals[i] = last
        self.idx[last].add(i)
        self.idx[last].discard(len(self.vals) - 1)
        self.vals.pop()
        return True

    def getRandom(self) -> int:
        return random.choice(self.vals)
```

The `add` before `discard` ordering matters when `i` is already the last index.

## Complexity

**O(1)** average for all three operations. O(n) space.

## Common mistakes

- **Forgetting `idx[last] = i`** — the moved element's index goes stale and every later remove corrupts the structure
- Deleting the map entry before the reassignment
- Trying to preserve insertion order (you cannot, and nothing asked you to)

## Problems

- [380. Insert Delete GetRandom O(1)](https://leetcode.com/problems/insert-delete-getrandom-o1/) — Medium
- [381. ...Duplicates Allowed](https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed/) — Hard
- [384. Shuffle an Array](https://leetcode.com/problems/shuffle-an-array/) — Medium
