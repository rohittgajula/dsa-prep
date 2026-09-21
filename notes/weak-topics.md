# Weak topics

What actually keeps going wrong. Revision aims here first.

Only repeated or costly slips belong in this file — a typo is not a weak topic.
A slip earns an entry the **second** time it happens, or the first time it costs
a whole problem.

## Entry format

```text
### <topic> — <pattern or subject>
**Slip:** what goes wrong, in one line
**Fix:** the correction, in one line
**Seen:** 2026-09-20, 2026-10-02
**Status:** <open | cooling | closed>
```

- **open** — still gets it wrong
- **cooling** — got it right once since; one more clean pass to close
- **closed** — right twice in a row, weeks apart. Moved to the bottom, kept as a record

Update `Seen` on an existing entry rather than adding a second entry for the
same slip. The repeat dates are the signal.

---

## Open

### Arrays — in-place modification contract
**Slip:** builds a new list and returns it, instead of mutating the input and returning k;
          three variants so far — returned the list (26), bare slice with no `=` (26),
          rebound the local name `nums, newArr = newArr, nums` (27)
**Fix:** mutate the OBJECT, not the name — `nums[:] = newArr`, then `return len(newArr)`.
         Assigning to a parameter name never reaches the caller. A brute force does NOT
         get to opt out of the contract; brute describes wasted work, not a changed signature.
**Seen:** 2026-09-20, 2026-09-21
**Status:** open (repeat confirmed — drill this on 283 Move Zeroes)

### DSA reasoning — ignoring a stated constraint
**Slip:** brute force works on unsorted input for a problem that hands you a *sorted* array
**Fix:** before optimising, ask which given constraint the brute force is not using yet
**Seen:** 2026-09-20
**Status:** open

## Cooling

_nothing logged yet_

## Closed

_nothing logged yet_
