# XOR Tricks

`Week 28` · Bit & Math

## Recognise it when

- *"Every element appears twice except one"*
- *"Find the missing number"*, *"find the single number"*

## The insight

XOR has two properties that do all the work:

```
  x ^ x = 0        a value cancels itself
  x ^ 0 = x        zero is the identity
```

XOR-ing everything therefore **cancels all pairs and leaves the loner**. It is also commutative and associative, so order never matters.

## Diagram

```
  nums = [4, 1, 2, 1, 2]

  4 ^ 1 ^ 2 ^ 1 ^ 2
  = 4 ^ (1 ^ 1) ^ (2 ^ 2)      reorder freely - XOR is commutative
  = 4 ^    0    ^    0
  = 4  ★

  bit by bit:
        4 = 1 0 0
        1 = 0 0 1
        2 = 0 1 0
        1 = 0 0 1
        2 = 0 1 0
        ────────── XOR each column (count of 1s mod 2)
            1 0 0  = 4
            ▲ ▲ ▲
            odd even even
```

### Two singletons — split into two groups

```
  nums = [1, 2, 1, 3, 2, 5]      two loners: 3 and 5

  Step 1: XOR everything  →  3 ^ 5 = 6 = 110

  Step 2: find the LOWEST SET BIT of 6:
              6  = 1 1 0
             -6  = 0 1 0   (two's complement)
          6 & -6 = 0 1 0 = 2

          That bit is 1 in exactly one of the two answers,
          because it is where they DIFFER.

  Step 3: partition by that bit and XOR each group:

          bit set (& 2):     2, 3, 2   → 3
          bit clear:         1, 1, 5   → 5
```

## Template

```python
def single_number(nums: list[int]) -> int:
    res = 0
    for x in nums:
        res ^= x
    return res
```

### Two singletons

```python
def single_number_iii(nums: list[int]) -> list[int]:
    xor_all = 0
    for x in nums:
        xor_all ^= x
    low_bit = xor_all & (-xor_all)     # isolate the lowest differing bit
    a = b = 0
    for x in nums:
        if x & low_bit:
            a ^= x
        else:
            b ^= x
    return [a, b]
```

### Appears three times — XOR does NOT work

Count each bit position mod 3 instead:

```python
def single_number_ii(nums: list[int]) -> int:
    ones = twos = 0
    for x in nums:
        ones = (ones ^ x) & ~twos
        twos = (twos ^ x) & ~ones
    return ones
```

Or, more readably:

```python
def single_number_ii_bits(nums: list[int]) -> int:
    res = 0
    for bit in range(32):
        count = sum((x >> bit) & 1 for x in nums) % 3
        if count:
            res |= (1 << bit)
    return res - (1 << 32) if res >= (1 << 31) else res   # sign fix
```

### Missing number — three valid approaches

```python
def missing_number(nums: list[int]) -> int:
    n = len(nums)
    # 1. XOR indices against values
    res = n
    for i, x in enumerate(nums):
        res ^= i ^ x
    return res
    # 2. sum formula:  n*(n+1)//2 - sum(nums)      (can overflow in C++/Java)
    # 3. cyclic sort                                (O(1) space, mutates input)
```

## Useful bit identities

| Expression | Effect |
|---|---|
| `x & (x - 1)` | clears the **lowest set bit** |
| `x & (-x)` | isolates the **lowest set bit** |
| `x & (x - 1) == 0` | x is a power of two (for x > 0) |
| `x ^ y` | bits where x and y **differ** |
| `x >> 1` | divide by 2 |

## Complexity

O(n) time, **O(1) space** — that space bound is the whole point versus a hash map.

## Common mistakes

- Using XOR for the **appears-three-times** variant
- Forgetting `x & -x` relies on two's complement (fine in Python, mind the width in C++)
- Sign handling for the 32-bit bit-counting approach in Python, where ints are arbitrary precision

## Problems

- [136. Single Number](https://leetcode.com/problems/single-number/) — Easy
- [260. Single Number III](https://leetcode.com/problems/single-number-iii/) — Medium
- [268. Missing Number](https://leetcode.com/problems/missing-number/) — Easy

---

## All problems in this pattern

**Bit Manipulation** — 9 problems (4 core). Full list with dates and checkboxes: [`solutions/40-bit-manipulation/`](../../solutions/40-bit-manipulation/)

| # | Problem | Diff | Tier |
|---|---|---|---|
| 89 | [Gray Code](https://leetcode.com/problems/gray-code/) | Medium | _opt_ |
| 136 | [Single Number](https://leetcode.com/problems/single-number/) | Easy | **Core** |
| 137 | [Single Number Ii](https://leetcode.com/problems/single-number-ii/) | Medium | _opt_ |
| 190 | [Reverse Bits](https://leetcode.com/problems/reverse-bits/) | Easy | _opt_ |
| 191 | [Number Of 1 Bits](https://leetcode.com/problems/number-of-1-bits/) | Easy | **Core** |
| 201 | [Bitwise And Of Numbers Range](https://leetcode.com/problems/bitwise-and-of-numbers-range/) | Medium | _opt_ |
| 260 | [Single Number Iii](https://leetcode.com/problems/single-number-iii/) | Medium | _opt_ |
| 338 | [Counting Bits](https://leetcode.com/problems/counting-bits/) | Easy | **Core** |
| 371 | [Sum Of Two Integers](https://leetcode.com/problems/sum-of-two-integers/) | Medium | **Core** |
