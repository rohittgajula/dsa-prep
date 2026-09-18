# LRU / LFU Cache

`Week 29` · Design

## Recognise it when

- *"O(1) get and put with eviction"*, *"design a cache"*, *"least recently used"*

## The insight

Neither structure alone can do it:

| Structure | Gives you | Missing |
|---|---|---|
| Hash map | O(1) lookup | no ordering |
| Doubly linked list | O(1) reorder & evict | no lookup |

**Combine them.** The map stores key → *node*, and the list maintains recency. Both operations become O(1).

This exact pairing answers a whole family of design questions.

## Diagram

```
  capacity 3, after put(1), put(2), put(3), get(1)

  HASH MAP                    DOUBLY LINKED LIST
  ┌─────┬──────┐              (most recent) ←──────────→ (least recent)
  │ key │ node │
  ├─────┼──────┤              HEAD ⇄ [1] ⇄ [3] ⇄ [2] ⇄ TAIL
  │  1  │  ●───┼──────────────────────┘      │      │
  │  2  │  ●───┼─────────────────────────────┼──────┘
  │  3  │  ●───┼─────────────────────────────┘
  └─────┴──────┘
                              get(1) → found via map in O(1)
                                     → unlink node 1, move to front, O(1)

  put(4) with capacity full:
      evict TAIL.prev = node 2      ← the least recently used
      delete map[2]
      insert 4 at the front

  HEAD ⇄ [4] ⇄ [1] ⇄ [3] ⇄ TAIL
```

### Why the list must be DOUBLY linked

```
  singly linked:  to unlink node X you need its PREDECESSOR
                  → O(n) scan to find it            ✗

  doubly linked:  node.prev and node.next are right there
                  → unlink in O(1)                  ✓
```

### Dummy head and tail sentinels

```
  WITHOUT sentinels: inserting into an empty list, removing the only
                     node, removing the head - three special cases.

  WITH sentinels:    HEAD ⇄ TAIL  (always present)
                     every real node always has a prev AND a next
                     → ONE uniform code path
```

## Template — LRU

```python
class Node:
    __slots__ = ("key", "val", "prev", "next")
    def __init__(self, key=0, val=0):
        self.key, self.val = key, val
        self.prev = self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.map: dict[int, Node] = {}
        self.head = Node()                 # sentinels
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add_front(self, node: Node) -> None:
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        node = self.map[key]
        self._remove(node)
        self._add_front(node)              # refresh recency
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self._remove(self.map[key])
        node = Node(key, value)
        self.map[key] = node
        self._add_front(node)
        if len(self.map) > self.cap:
            lru = self.tail.prev           # least recently used
            self._remove(lru)
            del self.map[lru.key]          # the node stores its KEY for this
```

> The node stores its **key** precisely so eviction can delete the map entry. Forgetting that field is the classic bug.

### Python shortcut — `OrderedDict`

```python
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.od = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.od:
            return -1
        self.od.move_to_end(key)
        return self.od[key]

    def put(self, key: int, value: int) -> None:
        if key in self.od:
            self.od.move_to_end(key)
        self.od[key] = value
        if len(self.od) > self.cap:
            self.od.popitem(last=False)
```

Fine in practice — but **write the manual version at least once**. Interviewers usually ask for it.

## LFU — one more level of indexing

```
  LFU evicts the LEAST FREQUENTLY used (ties broken by recency)

  freq → doubly linked list of keys at that frequency

    freq 1:  [d] ⇄ [c]        ← min_freq points here
    freq 2:  [b]
    freq 3:  [a]

  get(c):  remove c from list 1, append to list 2
           if list 1 becomes empty AND min_freq == 1 → min_freq = 2

  evict:   take the TAIL of the min_freq list
```

Needs three structures: `key → node`, `freq → list`, and a `min_freq` pointer. Considerably harder than LRU — expect it only at senior level.

## Complexity

**O(1)** for both `get` and `put`. O(capacity) space.

## Common mistakes

- Using a **singly** linked list
- Not storing the key inside the node → cannot clean up the map on eviction
- Omitting the sentinels and drowning in edge cases
- Forgetting that `get` must also refresh recency

## Connection to OS

This is exactly the **page replacement** policy from your OS notes — the same LRU, implemented for the same reason.

## Problems

- [146. LRU Cache](https://leetcode.com/problems/lru-cache/) — Medium
- [460. LFU Cache](https://leetcode.com/problems/lfu-cache/) — Hard
- [432. All O`one Data Structure](https://leetcode.com/problems/all-oone-data-structure/) — Hard
