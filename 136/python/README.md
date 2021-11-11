# Weekly Challenge 136

## TASK #1 › Two Friendly

You are given 2 positive numbers, `$m` and `$n`.

Write a script to find out if the given two numbers are `Two Friendly`.

> Two positive numbers, m and n are two friendly when gcd(m, n) = 2 ^ p where p > 0.

> The *greatest common divisor* (gcd) of a set of numbers is the largest positive number that divides all the numbers in the set without remainder.

**Example 1:**
```
    Input: $m = 8, $n = 24
    Output: 1

    Reason: gcd(8,24) = 8 => 2 ^ 3
```

**Example 2:**
```
    Input: $m = 26, $n = 39
    Output: 0

    Reason: gcd(26,39) = 13
```

**Example 3:**
```
    Input: $m = 4, $n = 10
    Output: 1

    Reason: gcd(4,10) = 2 => 2 ^ 1
```

### Solution

```python
import math


def power_of_two(num: int) -> int:
    """Determines if a number is a (positive) power of two.
    Returns positive integer of the power if true, else 0.
    """
    if num <= 0:
        raise ValueError("Only positive integers allowed.")
    elif type(num) != int:
        raise TypeError("Only integers are allowed.")

    if num % 2 != 0:
        return 0

    power = 1
    while num / 2 != 1:
        if num % 2 != 0:
            return 0

        num = num // 2
        power += 1

    return power


def determine_two_friendly(m: int, n: int) -> str:
    """Determine if two numbers are 'Two Friendly'."""
    if m <= 0 or n <= 0:
        raise ValueError("Only positive integers allowed.")
    elif type(m) != int or type(n) != int:
        raise TypeError("Only integers are allowed.")

    gcd = math.gcd(m, n)
    power = power_of_two(gcd)
    is_friendly = bool(power)

    input_line = f"\nInput: $m = {m}, $n = {n}"
    output_line = f"\nOutput: {int(is_friendly)}"
    reason_line = f"\n\nReason: gcd({m}, {n}) = {gcd}"

    if is_friendly:
        reason_line += f" => 2 ^ {power}"

    return input_line + output_line + reason_line

```

---
## Task 2 > Fibonacci Sequence

You are given a positive number `$n`.

Write a script to find how many different sequences you can create using Fibonacci numbers where the sum of unique numbers in each sequence are the same as the given number.

> Fibonacci Numbers: 1,2,3,5,8,13,21,34,55,89, …

**Example 1:**
```
Input:  $n = 16
Output: 4

Reason: There are 4 possible sequences that can be created using Fibonacci numbers
i.e. (3 + 13), (1 + 2 + 13), (3 + 5 + 8) and (1 + 2 + 5 + 8).
```

**Example 2:**
```
Input:  $n = 9
Output: 2

Reason: There are 2 possible sequences that can be created using Fibonacci numbers
i.e. (1 + 3 + 5) and (1 + 8).
```

**Example 3:**
```
Input:  $n = 15
Output: 2

Reason: There are 2 possible sequences that can be created using Fibonacci numbers
i.e. (2 + 5 + 8) and (2 + 13).
```





### Solution

```python


```