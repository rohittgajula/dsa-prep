# Merge Intervals / Sweep Line

`Week 10` · Arrays & Strings

## Recognise it when

- Input is a list of `[start, end]` pairs
- Merge, insert, count overlaps, *"minimum meeting rooms"*, *"fewest arrows"*

## The insight

**Sort by start time.** Any overlap must then be with the interval you just processed — so a single pass suffices.

For *"how many overlap at once"*, convert to **+1 / −1 events** sorted by time and track a running count. The maximum that counter reaches is your answer.

## Diagram

### Merging — sort by start

```
  input:  [1,3]  [2,6]  [8,10]  [15,18]

  after sorting by start:
        1───3
          2──────6
                    8──10
                            15───18
  timeline ──────────────────────────────►
        1 2 3 4 5 6 7 8 9 10 ... 15 ... 18

  [1,3] and [2,6] overlap (2 <= 3) → merge to [1,6]
  [8,10]  starts after 6           → new interval
  [15,18] starts after 10          → new interval

  output: [1,6]  [8,10]  [15,18]
```

### Sweep line — maximum concurrent

```
  meetings: [0,30] [5,10] [15,20]

  events (sorted by time):
    t=0   +1    count = 1
    t=5   +1    count = 2   ★ max
    t=10  -1    count = 1
    t=15  +1    count = 2   ★ max
    t=20  -1    count = 1
    t=30  -1    count = 0

  rooms needed = max count = 2
```

## Template

```python
def merge(intervals: list[list[int]]) -> list[list[int]]:
    intervals.sort(key=lambda x: x[0])
    out = [intervals[0]]
    for s, e in intervals[1:]:
        if s <= out[-1][1]:                    # overlap
            out[-1][1] = max(out[-1][1], e)    # max() - the next may be nested
        else:
            out.append([s, e])
    return out
```

### Minimum meeting rooms — heap of end times

```python
import heapq

def min_meeting_rooms(intervals: list[list[int]]) -> int:
    if not intervals:
        return 0
    intervals.sort(key=lambda x: x[0])
    ends = []                       # min-heap of end times
    for s, e in intervals:
        if ends and ends[0] <= s:   # a room has freed up
            heapq.heappop(ends)
        heapq.heappush(ends, e)
    return len(ends)
```

### Non-overlapping — sort by END (greedy)

```python
def erase_overlap_intervals(intervals: list[list[int]]) -> int:
    intervals.sort(key=lambda x: x[1])         # by END, not start
    end = float('-inf')
    kept = 0
    for s, e in intervals:
        if s >= end:
            kept += 1
            end = e
    return len(intervals) - kept
```

> **Merging sorts by START. Greedy "keep the most" sorts by END.** Mixing these up is the classic error.

## Complexity

O(n log n) — dominated by the sort.

## Common mistakes

- Sorting by start when the problem needs an end-sorted greedy
- `out[-1][1] = e` instead of `max(...)` — breaks on a nested interval like `[1,10] [2,3]`
- Not checking whether touching intervals (`[1,2]` and `[2,3]`) count as overlapping. The problem always says; it flips `<=` to `<`.

## Problems

- [56. Merge Intervals](https://leetcode.com/problems/merge-intervals/) — Medium
- [57. Insert Interval](https://leetcode.com/problems/insert-interval/) — Medium
- [435. Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/) — Medium
