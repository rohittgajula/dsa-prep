# Greedy — Interval Scheduling

`Week 24` · Greedy & DP

## Recognise it when

- *"Maximum non-overlapping"*, *"minimum removals"*, *"fewest arrows"*, *"maximum meetings"*

## The insight

**Sort by END time, not start.**

Taking the earliest-finishing interval always leaves the maximum room for everything after it. This is provable by an **exchange argument**: any optimal solution can be transformed to start with the earliest-finishing interval without getting worse.

Sorting by start is the classic wrong answer.

## Diagram

```
  intervals:   A ├────────────────┤
               B   ├───┤
               C        ├───┤
               D              ├───┤
               time ────────────────────►

  SORTED BY START → picks A first, blocks everything → 1 interval  ✗

  SORTED BY END:
               B   ├───┤              ends earliest → TAKE
               C        ├───┤          starts after B ends → TAKE
               D              ├───┤    starts after C ends → TAKE
               A ├────────────────┤    overlaps → skip
                                       → 3 intervals  ✓

  ╔══════════════════════════════════════════════════════════╗
  ║ Finishing early is never worse: it leaves a superset of  ║
  ║ the remaining choices compared to any later finish.      ║
  ╚══════════════════════════════════════════════════════════╝
```

## Template

```python
def max_non_overlapping(intervals: list[list[int]]) -> int:
    intervals.sort(key=lambda x: x[1])         # by END
    end = float('-inf')
    count = 0
    for s, e in intervals:
        if s >= end:                           # no overlap
            count += 1
            end = e
    return count
```

### Non-overlapping intervals (LC 435) — removals = total − kept

```python
def erase_overlap_intervals(intervals: list[list[int]]) -> int:
    return len(intervals) - max_non_overlapping(intervals)
```

### Minimum arrows (LC 452) — same greedy, `>` not `>=`

```python
def find_min_arrow_shots(points: list[list[int]]) -> int:
    points.sort(key=lambda x: x[1])
    arrows, end = 0, float('-inf')
    for s, e in points:
        if s > end:                # touching balloons SHARE an arrow
            arrows += 1
            end = e
    return arrows
```

### Jump Game — a different greedy, track the furthest reach

```python
def can_jump(nums: list[int]) -> bool:
    reach = 0
    for i, x in enumerate(nums):
        if i > reach:
            return False           # cannot even get here
        reach = max(reach, i + x)
    return True

def jump(nums: list[int]) -> int:
    jumps = cur_end = furthest = 0
    for i in range(len(nums) - 1):
        furthest = max(furthest, i + nums[i])
        if i == cur_end:           # exhausted the current jump's range
            jumps += 1
            cur_end = furthest
    return jumps
```

## When greedy FAILS

```
  coins = [1, 3, 4], target = 6

  greedy (largest first):  4 + 1 + 1  = 3 coins
  optimal:                 3 + 3      = 2 coins   ✗ greedy is wrong

  → no exchange argument exists → use DP (knapsack)
```

**If you cannot justify the greedy choice with an exchange argument, you probably need DP.** Say that out loud in an interview — it shows you know the difference rather than guessing.

## Complexity

O(n log n), dominated by the sort.

## Common mistakes

- **Sorting by start** for a "keep the most" problem
- `>=` vs `>` — decides whether touching intervals conflict. The problem always specifies.
- Applying greedy where no exchange argument holds

## Problems

- [435. Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/) — Medium
- [452. Minimum Arrows to Burst Balloons](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/) — Medium
- [55. Jump Game](https://leetcode.com/problems/jump-game/) — Medium
