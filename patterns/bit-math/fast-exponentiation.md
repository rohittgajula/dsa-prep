# Fast Exponentiation & Modular Arithmetic

`Week 28` · Bit & Math

## Recognise it when

- *"Compute x^n"*, *"answer modulo 1e9+7"*, very large powers
- Matrix power (Fibonacci in O(log n))

## The insight

**Squaring halves the exponent** each step, so `n` multiplications become `log n`.

Take the modulus at **every** step to keep numbers small and avoid overflow in fixed-width languages.

## Diagram

```
  compute 3^13

  13 in binary = 1101

  3^13 = 3^8 · 3^4 · 3^1        only the SET bits contribute
         └─┬─┘ └─┬─┘ └─┬─┘
          bit3  bit2  bit0

  build the squares by repeated squaring:
      3^1  = 3
      3^2  = 3^1 · 3^1   = 9
      3^4  = 3^2 · 3^2   = 81
      3^8  = 3^4 · 3^4   = 6561

  walk the bits of n, low to high:

   n=13  1101   bit set → res = 1 · 3       = 3      x becomes 9
   n=6   110    bit 0   → skip                       x becomes 81
   n=3   11     bit set → res = 3 · 81      = 243    x becomes 6561
   n=1   1      bit set → res = 243 · 6561  = 1594323
   n=0   done

  3^13 = 1594323  ✓     4 multiplications instead of 13
```

## Template

```python
def power(x: int, n: int, mod: int = None) -> int:
    res = 1
    if n < 0:
        x, n = 1 / x, -n            # negative exponent
    while n > 0:
        if n & 1:                   # this bit is set
            res = res * x
            if mod: res %= mod
        x = x * x
        if mod: x %= mod
        n >>= 1
    return res
```

### LeetCode 50 — Pow(x, n)

```python
def my_pow(x: float, n: int) -> float:
    if n < 0:
        x, n = 1 / x, -n
    res = 1.0
    while n:
        if n & 1:
            res *= x
        x *= x
        n >>= 1
    return res
```

Watch `n = -2^31` in Java/C++ — negating it overflows. Cast to a wider type first.

## Modular arithmetic rules

```
  (a + b) % m  =  ((a % m) + (b % m)) % m
  (a - b) % m  =  ((a % m) - (b % m) + m) % m     ← the +m avoids negatives
  (a * b) % m  =  ((a % m) * (b % m)) % m

  (a / b) % m  ≠  ((a % m) / (b % m)) % m         ✗ DIVISION DOES NOT DISTRIBUTE

  For division, multiply by the MODULAR INVERSE:
      a / b  ≡  a · b^(m-2)  (mod m)        when m is prime (Fermat's little theorem)
```

```python
MOD = 10**9 + 7

def mod_inverse(b: int, mod: int = MOD) -> int:
    return power(b, mod - 2, mod)        # only valid for PRIME mod

def mod_divide(a: int, b: int, mod: int = MOD) -> int:
    return a * mod_inverse(b, mod) % mod
```

`10**9 + 7` is chosen because it is prime and fits comfortably in 32 bits when squared into a 64-bit accumulator.

### nCr mod p — precompute factorials

```python
MOD = 10**9 + 7

def build_factorials(n: int):
    fact = [1] * (n + 1)
    for i in range(1, n + 1):
        fact[i] = fact[i - 1] * i % MOD
    inv = [1] * (n + 1)
    inv[n] = power(fact[n], MOD - 2, MOD)
    for i in range(n, 0, -1):
        inv[i - 1] = inv[i] * i % MOD
    return fact, inv

def nCr(n: int, r: int, fact, inv) -> int:
    if r < 0 or r > n:
        return 0
    return fact[n] * inv[r] % MOD * inv[n - r] % MOD
```

## Complexity

**O(log n)** multiplications, O(1) space.

## Common mistakes

- Not taking the modulus at **every** multiplication → overflow in C++/Java
- Trying to divide under a modulus without the inverse
- Forgetting `n == 0` (answer 1) and negative `n`
- `-2^31` negation overflow

## Problems

- [50. Pow(x, n)](https://leetcode.com/problems/powx-n/) — Medium
- [372. Super Pow](https://leetcode.com/problems/super-pow/) — Medium
- [1922. Count Good Numbers](https://leetcode.com/problems/count-good-numbers/) — Medium
