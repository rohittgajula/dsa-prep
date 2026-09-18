# DP — State Machine (Stock Problems)

`Week 27` · Greedy & DP

## Recognise it when

- You are always in one of a few **states** and each step transitions between them
- **Every one of the six stock problems is this same machine**

## The insight

Rather than tracking indices, track **states** and the best value achievable in each.

Once you draw the machine, the code writes itself.

## Diagram

```
  BASIC (unlimited transactions, LC 122)

           ┌──── buy: free - price ────┐
           ▼                           │
      ┌─────────┐                 ┌─────────┐
      │  FREE   │                 │  HOLD   │
      │ (no     │                 │ (own a  │
      │  stock) │                 │  stock) │
      └─────────┘                 └─────────┘
           ▲                           │
           └──── sell: hold + price ───┘

      free = max(free, hold + price)
      hold = max(hold, free - price)


  WITH COOLDOWN (LC 309) - one extra state

      ┌────────┐   buy    ┌────────┐   sell   ┌──────────┐
      │  FREE  │ ───────► │  HOLD  │ ───────► │ COOLDOWN │
      └────────┘          └────────┘          └──────────┘
           ▲                                        │
           └──────────── next day ──────────────────┘

      You cannot buy the day after selling, so `buy` must read
      FREE from TWO steps back, not one.


  AT MOST K TRANSACTIONS (LC 123, 188) - add a counter dimension

      hold[k]  = max(hold[k], free[k-1] - price)    uses up a transaction
      free[k]  = max(free[k], hold[k]  + price)
```

## Template

```python
def max_profit_unlimited(prices: list[int]) -> int:
    hold = float('-inf')            # best value while HOLDING
    free = 0                        # best value while holding NOTHING
    for p in prices:
        hold = max(hold, free - p)  # buy
        free = max(free, hold + p)  # sell
    return free
```

Initialising `hold` to `-inf` (not 0) encodes "you cannot start already holding a stock for free".

### With cooldown — keep the value from two steps back

```python
def max_profit_cooldown(prices: list[int]) -> int:
    hold, free, cooldown = float('-inf'), 0, 0
    for p in prices:
        prev_free = free
        hold = max(hold, free - p)       # `free` here is from BEFORE this sell
        free = max(free, cooldown)
        cooldown = prev_free + p if prev_free != float('-inf') else cooldown
    return max(free, cooldown)
```

Cleaner three-variable form:

```python
def max_profit_cooldown2(prices: list[int]) -> int:
    sold, held, rest = float('-inf'), float('-inf'), 0
    for p in prices:
        sold, held, rest = held + p, max(held, rest - p), max(rest, sold)
    return max(sold, rest)
```

### With a transaction fee

```python
def max_profit_fee(prices: list[int], fee: int) -> int:
    hold, free = float('-inf'), 0
    for p in prices:
        hold = max(hold, free - p)
        free = max(free, hold + p - fee)     # pay the fee on SELL
    return free
```

### At most k transactions

```python
def max_profit_k(k: int, prices: list[int]) -> int:
    n = len(prices)
    if k >= n // 2:                          # degenerates to unlimited
        return max_profit_unlimited(prices)
    hold = [float('-inf')] * (k + 1)
    free = [0] * (k + 1)
    for p in prices:
        for t in range(1, k + 1):
            hold[t] = max(hold[t], free[t - 1] - p)   # t-1: buying starts a txn
            free[t] = max(free[t], hold[t] + p)
    return free[k]
```

## The whole family

| Problem | Machine |
|---|---|
| 121 — one transaction | track the running minimum |
| 122 — unlimited | 2 states |
| 123 — at most 2 | 4 states |
| 188 — at most k | 2 states × k |
| 309 — cooldown | 3 states |
| 714 — fee | 2 states, fee on sell |

Learn the two-state machine and all six follow.

## Complexity

O(n) time, O(1) space for the unlimited/cooldown/fee variants; O(nk) time, O(k) space for the k-transaction ones.

## Common mistakes

- Initialising `hold = 0` instead of `-inf`
- For cooldown, reading `free` from the current step instead of two back
- For k transactions, decrementing the counter on the wrong side (it goes on **buy**)

## Problems

- [121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) — Easy
- [309. With Cooldown](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/) — Medium
- [188. At Most K Transactions](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/) — Hard
