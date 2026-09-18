# Monotonic Stack

`Week 12` · Linear Structures

## Recognise it when

- *"**Next** / **previous** greater or smaller element"*
- Histogram area, stock span, daily temperatures, trapping rain water
- You are comparing each element to the **nearest** bigger/smaller one

## The insight

Keep the stack **sorted**. When a new element arrives and violates that order, it is precisely the *"next greater"* element for everything you pop.

Each index is pushed once and popped once → **O(n)** despite the nested `while`.

## Diagram

```
  Daily temperatures: [73, 74, 75, 71, 69, 72, 76, 73]
  For each day, how many days until a warmer one?

  stack holds INDICES, temperatures DECREASING bottom→top

  i=0  73   stack: []        → push 0            [0]
  i=1  74   74 > 73 → pop 0, ans[0] = 1-0 = 1    [1]
  i=2  75   75 > 74 → pop 1, ans[1] = 2-1 = 1    [2]
  i=3  71   71 < 75 → push                       [2,3]
  i=4  69   69 < 71 → push                       [2,3,4]
  i=5  72   72 > 69 → pop 4, ans[4] = 5-4 = 1
            72 > 71 → pop 3, ans[3] = 5-3 = 2
            72 < 75 → push                       [2,5]
  i=6  76   76 > 72 → pop 5, ans[5] = 6-5 = 1
            76 > 75 → pop 2, ans[2] = 6-2 = 4
            push                                 [6]
  i=7  73   73 < 76 → push                       [6,7]

  leftovers [6,7] have no warmer day → ans stays 0

  result: [1, 1, 4, 2, 1, 1, 0, 0]

  stack profile (decreasing):
        75
        │  72
        │  │  76
     ───┴──┴──┴───
```

### Which direction?

| You want | Stack order | Pop when |
|---|---|---|
| Next **greater** | decreasing | incoming **>** top |
| Next **smaller** | increasing | incoming **<** top |
| Previous greater | decreasing | (read the stack top *before* pushing) |

## Template

```python
def next_greater(a: list[int]) -> list[int]:
    n = len(a)
    ans = [-1] * n
    stack = []                       # INDICES, values decreasing
    for i, x in enumerate(a):
        while stack and a[stack[-1]] < x:
            j = stack.pop()
            ans[j] = i               # x is j's next greater
        stack.append(i)
    return ans                       # leftovers keep -1
```

### Largest rectangle in a histogram

For each bar, how far can it extend left and right before hitting something shorter?

```
  heights = [2, 1, 5, 6, 2, 3]

              ┌─┐
            ┌─┤6│
            │5│ │      bar 5 extends over indices 2..3 → width 2, area 10
    ┌─┐     │ │ │ ┌─┐  bar 6 extends over index 3      → width 1, area 6
    │2│ ┌─┐ │ │ │ │3│
    │ │ │1│ │ │ │ │ │  ★ best = 5 * 2 = 10
    └─┴─┴─┴─┴─┴─┴─┴─┘
     0  1  2  3  4  5
```

```python
def largest_rectangle(heights: list[int]) -> int:
    stack = []                       # indices, heights INCREASING
    best = 0
    for i, h in enumerate(heights + [0]):    # sentinel flushes the stack
        while stack and heights[stack[-1]] > h:
            height = heights[stack.pop()]
            left = stack[-1] + 1 if stack else 0
            best = max(best, height * (i - left))
        stack.append(i)
    return best
```

> The trailing `[0]` sentinel is what flushes any remaining bars — without it you must repeat the pop loop after the main loop.

## Complexity

O(n) time — each index pushed and popped once. O(n) space.

## Common mistakes

- Storing **values** instead of **indices** — you then cannot compute distances
- Forgetting the leftovers after the loop (or the sentinel that flushes them)
- Picking the wrong stack direction. Derive it: *next greater* means you pop things smaller than the incoming value, so the stack must be decreasing.

## Problems

- [739. Daily Temperatures](https://leetcode.com/problems/daily-temperatures/) — Medium
- [496. Next Greater Element I](https://leetcode.com/problems/next-greater-element-i/) — Easy
- [84. Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/) — Hard
