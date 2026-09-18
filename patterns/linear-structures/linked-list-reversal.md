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

---

## All problems in this pattern

**Linked List** — 22 problems (13 core). Full list with dates and checkboxes: [`solutions/12-linked-list/`](../../solutions/12-linked-list/)

| # | Problem | Diff | Tier |
|---|---|---|---|
| 2 | [Add Two Numbers](https://leetcode.com/problems/add-two-numbers/) | Medium | **Core** |
| 19 | [Remove Nth Node From End Of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) | Medium | **Core** |
| 21 | [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/) | Easy | **Core** |
| 24 | [Swap Nodes In Pairs](https://leetcode.com/problems/swap-nodes-in-pairs/) | Medium | _opt_ |
| 25 | [Reverse Nodes In K Group](https://leetcode.com/problems/reverse-nodes-in-k-group/) | Hard | **Core** |
| 61 | [Rotate List](https://leetcode.com/problems/rotate-list/) | Medium | _opt_ |
| 82 | [Remove Duplicates From Sorted List Ii](https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/) | Medium | _opt_ |
| 83 | [Remove Duplicates From Sorted List](https://leetcode.com/problems/remove-duplicates-from-sorted-list/) | Easy | _opt_ |
| 92 | [Reverse Linked List Ii](https://leetcode.com/problems/reverse-linked-list-ii/) | Medium | **Core** |
| 138 | [Copy List With Random Pointer](https://leetcode.com/problems/copy-list-with-random-pointer/) | Medium | **Core** |
| 141 | [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) | Easy | **Core** |
| 142 | [Linked List Cycle Ii](https://leetcode.com/problems/linked-list-cycle-ii/) | Medium | **Core** |
| 143 | [Reorder List](https://leetcode.com/problems/reorder-list/) | Medium | **Core** |
| 148 | [Sort List](https://leetcode.com/problems/sort-list/) | Medium | _opt_ |
| 160 | [Intersection Of Two Linked Lists](https://leetcode.com/problems/intersection-of-two-linked-lists/) | Easy | **Core** |
| 203 | [Remove Linked List Elements](https://leetcode.com/problems/remove-linked-list-elements/) | Easy | _opt_ |
| 206 | [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) | Easy | **Core** |
| 234 | [Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/) | Easy | **Core** |
| 328 | [Odd Even Linked List](https://leetcode.com/problems/odd-even-linked-list/) | Medium | _opt_ |
| 430 | [Flatten A Multilevel Doubly Linked List](https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/) | Medium | _opt_ |
| 445 | [Add Two Numbers Ii](https://leetcode.com/problems/add-two-numbers-ii/) | Medium | _opt_ |
| 876 | [Middle Of The Linked List](https://leetcode.com/problems/middle-of-the-linked-list/) | Easy | **Core** |
