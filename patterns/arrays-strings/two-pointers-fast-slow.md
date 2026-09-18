# Two Pointers — Fast & Slow (Floyd's)

`Week 2` · Arrays & Strings

## Recognise it when

- Detect a **cycle**
- Find the **middle** of a list in one pass
- *"Duplicate number in 1..n"* framed as a linked list
- You need O(1) space where a hash set would be O(n)

## The insight

If `fast` moves 2 steps and `slow` moves 1, the gap between them **closes by exactly 1 each step**. Inside a cycle the gap can never be skipped over — so they *must* meet.

The second part is the surprising bit: after they meet, the distance from **head → cycle start** equals the distance from **meeting point → cycle start**. That is why resetting one pointer to the head and walking both at speed 1 lands them together at the entry.

## Diagram

```
        head
         │
         ▼
   ①───►②───►③───►④
              ▲     │
              │     ▼
              ⑥◄───⑤          cycle of length 3

  step │ slow │ fast
  ─────┼──────┼──────
    0  │  ①   │  ①
    1  │  ②   │  ③
    2  │  ③   │  ⑤
    3  │  ④   │  ④   ← meet

  Now reset one pointer to head, advance BOTH by 1:
    ① → ② → ③        (from head)
    ④ → ⑤ → ⑥ → ③    (from meeting point)
                 ↑ they meet at ③ = cycle entry
```

### Why the maths works

Let `L` = head→entry, `C` = cycle length, `k` = entry→meeting point.

When they meet, slow has walked `L + k`, fast has walked `2(L + k)`.
Fast is also `L + k + nC` for some integer `n`.
So `2(L + k) = L + k + nC` → `L + k = nC` → **`L = nC − k`**.

`nC − k` is exactly the distance from the meeting point back round to the entry. Hence both pointers, moving at speed 1, arrive together.

## Template

```python
def detect_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:            # cycle confirmed
            slow = head
            while slow is not fast: # walk both at speed 1
                slow = slow.next
                fast = fast.next
            return slow             # entry node
    return None                     # fast hit the end - no cycle
```

### Middle of the list

```python
def middle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow      # for even length this is the SECOND middle
```

To get the *first* middle on even length, loop `while fast.next and fast.next.next`.

### Find the duplicate (LC 287)

Treat `nums[i]` as a "next pointer" — values in `1..n` guarantee a cycle:

```python
def find_duplicate(nums: list[int]) -> int:
    slow = fast = nums[0]
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    return slow
```

## Complexity

O(n) time, **O(1) space** — that space bound is the whole reason to use it.

## Common mistakes

- Not checking `fast and fast.next` → `NoneType` has no attribute `next`
- Assuming the meeting point *is* the cycle entry. It is not — you need the second walk.
- For "middle", the loop condition decides first vs second middle. Read the problem.

## Problems

- [141. Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) — Easy
- [142. Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/) — Medium
- [287. Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/) — Medium

---

## All problems in this pattern

**Two Pointers** — 16 problems (12 core). Full list with dates and checkboxes: [`solutions/02-two-pointers/`](../../solutions/02-two-pointers/)

| # | Problem | Diff | Tier |
|---|---|---|---|
| 11 | [Container With Most Water](https://leetcode.com/problems/container-with-most-water/) | Medium | **Core** |
| 15 | [3Sum](https://leetcode.com/problems/3sum/) | Medium | **Core** |
| 16 | [3Sum Closest](https://leetcode.com/problems/3sum-closest/) | Medium | _opt_ |
| 18 | [4Sum](https://leetcode.com/problems/4sum/) | Medium | _opt_ |
| 31 | [Next Permutation](https://leetcode.com/problems/next-permutation/) | Medium | **Core** |
| 42 | [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/) | Hard | _opt_ |
| 75 | [Sort Colors](https://leetcode.com/problems/sort-colors/) | Medium | **Core** |
| 80 | [Remove Duplicates From Sorted Array Ii](https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/) | Medium | **Core** |
| 125 | [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) | Easy | **Core** |
| 167 | [Two Sum Ii Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) | Medium | **Core** |
| 189 | [Rotate Array](https://leetcode.com/problems/rotate-array/) | Medium | **Core** |
| 287 | [Find The Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/) | Medium | **Core** |
| 344 | [Reverse String](https://leetcode.com/problems/reverse-string/) | Easy | **Core** |
| 680 | [Valid Palindrome Ii](https://leetcode.com/problems/valid-palindrome-ii/) | Easy | **Core** |
| 905 | [Sort Array By Parity](https://leetcode.com/problems/sort-array-by-parity/) | Easy | _opt_ |
| 977 | [Squares Of A Sorted Array](https://leetcode.com/problems/squares-of-a-sorted-array/) | Easy | **Core** |
