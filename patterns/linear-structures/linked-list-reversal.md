# Linked List Reversal

`Week 11` · Linear Structures

## Recognise it when

- Reverse the whole list, a **sublist**, or groups of **k**

## The insight

Reversal is just re-pointing each node backwards while **holding onto the next node** so you do not lose the rest of the list.

Three pointers is the minimum: `prev`, `cur`, `nxt`.

## Diagram

```
  start:   None   1 → 2 → 3 → 4 → None
           prev  cur

  step 1:  save nxt = 2
           1 → None          (cur.next = prev)
           None ← 1   2 → 3 → 4
                prev cur

  step 2:  save nxt = 3
           None ← 1 ← 2   3 → 4
                     prev cur

  step 3:  None ← 1 ← 2 ← 3   4
                         prev cur

  step 4:  None ← 1 ← 2 ← 3 ← 4     cur = None → stop
                             prev   ← return prev as the NEW HEAD
```

**The order inside the loop is fixed and non-negotiable:**

```
  1. nxt = cur.next      save it BEFORE you destroy the link
  2. cur.next = prev     reverse
  3. prev = cur          advance prev
  4. cur = nxt           advance cur
```

## Template

```python
def reverse_list(head):
    prev, cur = None, head
    while cur:
        nxt = cur.next        # 1. save
        cur.next = prev       # 2. reverse
        prev = cur            # 3. advance
        cur = nxt             # 4. advance
    return prev               # new head
```

### Reverse a sublist [m, n]

```python
def reverse_between(head, left: int, right: int):
    dummy = ListNode(0, head)
    before = dummy
    for _ in range(left - 1):
        before = before.next          # node just before the sublist

    prev, cur = None, before.next
    for _ in range(right - left + 1):
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt

    before.next.next = cur            # old sublist head → the tail remainder
    before.next = prev                # before → new sublist head
    return dummy.next
```

```
  1 → [2 → 3 → 4] → 5      reverse 2..4

  before  ─┐         ┌─ cur (5)
           ▼         ▼
      1    2 → 3 → 4   5
           └─ becomes ─┘
      1 →  4 → 3 → 2 → 5
           ▲       └── old sublist head now points at cur
           new sublist head (prev)
```

### Reverse in k-groups

```python
def reverse_k_group(head, k: int):
    node = head
    for _ in range(k):
        if not node:
            return head              # fewer than k remain - leave as is
        node = node.next
    prev, cur = None, head
    for _ in range(k):
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt
    head.next = reverse_k_group(cur, k)   # head is now the group's TAIL
    return prev
```

## Complexity

O(n) time, O(1) space (iterative). The recursive version is O(n) stack.

## Common mistakes

- Not saving `nxt` before overwriting `cur.next` — you lose the rest of the list
- Returning `head` instead of `prev`
- Not using a **dummy node** when the head can change

## Problems

- [206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) — Easy
- [92. Reverse Linked List II](https://leetcode.com/problems/reverse-linked-list-ii/) — Medium
- [25. Reverse Nodes in k-Group](https://leetcode.com/problems/reverse-nodes-in-k-group/) — Hard
