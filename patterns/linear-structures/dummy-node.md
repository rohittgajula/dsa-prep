# Dummy Node Technique

`Week 11` · Linear Structures

## Recognise it when

- **Any** linked-list problem where the head itself might be removed or replaced

## The insight

A dummy node placed **before** the head means every real node has a predecessor.

That single change erases the *"what if it's the first node"* branch from your code — which is the biggest single source of linked-list bugs.

## Diagram

```
  WITHOUT a dummy - removing the head is a special case

      head
       ▼
       1 → 2 → 3          remove 1?  →  head = head.next
                          remove 2?  →  prev.next = prev.next.next
                          TWO different code paths


  WITH a dummy - one uniform path

    dummy   head
      ▼      ▼
      0  →   1 → 2 → 3    remove ANY node:  prev.next = prev.next.next
      ▲
      prev starts here, so node 1 has a predecessor too

    return dummy.next   ← NOT head (head may have been removed)
```

## Template

```python
def remove_elements(head, val: int):
    dummy = ListNode(0, head)
    prev = dummy
    while prev.next:
        if prev.next.val == val:
            prev.next = prev.next.next     # no head special case
        else:
            prev = prev.next
    return dummy.next                       # NOT head
```

### Remove the nth node from the end — gap technique

```python
def remove_nth_from_end(head, n: int):
    dummy = ListNode(0, head)
    fast = slow = dummy
    for _ in range(n):
        fast = fast.next          # open a gap of n
    while fast.next:
        fast = fast.next
        slow = slow.next          # slow lands just BEFORE the target
    slow.next = slow.next.next
    return dummy.next
```

```
  remove 2nd from end:  1 → 2 → 3 → 4 → 5

  dummy 0 → 1 → 2 → 3 → 4 → 5
        s         f                 gap of n=2

  advance both until fast.next is None:
  dummy 0 → 1 → 2 → 3 → 4 → 5
                    s         f
                    ▲ slow is just before node 4  ✓
```

### Merge two sorted lists

```python
def merge_two_lists(a, b):
    dummy = tail = ListNode(0)
    while a and b:
        if a.val <= b.val:
            tail.next, a = a, a.next
        else:
            tail.next, b = b, b.next
        tail = tail.next
    tail.next = a or b            # attach whatever remains
    return dummy.next
```

## Complexity

O(n) time, O(1) space. The dummy costs one node.

## Common mistakes

- **Returning `head` instead of `dummy.next`**
- Not using a dummy "because the head obviously won't change" — then discovering it can

> Use a dummy by **default** on any list problem that inserts or removes. It costs one line and removes a whole class of bugs.

## Problems

- [203. Remove Linked List Elements](https://leetcode.com/problems/remove-linked-list-elements/) — Easy
- [19. Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) — Medium
- [82. Remove Duplicates from Sorted List II](https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/) — Medium

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
