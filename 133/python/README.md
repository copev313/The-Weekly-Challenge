# Weekly Challenge 133

## TASK #1 › Integer Square Root

You are given a positive integer `$N`.

Write a script to calculate the integer square root of the given number.

Please avoid using built-in function. Find out more about it [here](https://en.wikipedia.org/wiki/Integer_square_root).


**Examples**

```
Input: $N = 10
Output: 3

Input: $N = 27
Output: 5

Input: $N = 85
Output: 9

Input: $N = 101
Output: 10

```

### Solution

```python
def int_sqrt(n: int) -> int:
    """Return the integer square root of n."""

    # [CASE] n is negative:
    if n < 0:
        raise ValueError("n must be >= 0")

    # Use exponential method to find the square root:
    sqrt = n ** (1/2)
    # Convert any float to int closest to zero:
    return int(sqrt)

```

---
## Task 2 > Smith Number

Write a script to generate the first 10 `Smith Numbers` in base 10.

According to Wikipedia:

> In number theory, a Smith number is a composite number for which, in a given
> number base, the sum of its digits is equal to the sum of the digits in its
> prime factorization in the given number base.

### Solution

You'll see I split the task into several parts and made use of some helper functions. 
For the sake of simplicity, I did not implement the ability to handle bases other than 10.
To see more comments on the code's thought processes, check out the `ch2.py` file.

```python
def prime_factors(n: int) -> list:
    """Returns a list of prime factors of n."""
    if n <= 0:
        raise ValueError("n must be a positive integer")
    
    factors = []
    test_prime = 2

    while test_prime ** 2 <= n:
        if n % test_prime != 0:
            test_prime += 1
        else:
            n //= test_prime
            factors.append(test_prime)

    if n > 1:
        factors.append(n)

    return factors


def smith_number(n: int) -> bool:
    """Returns whether a given integer is a Smith number."""
    if n <= 0:
        raise ValueError("n must be a positive integer")

    digits_sum = 0
    for digit in str(n):
        digits_sum += int(digit)

    prime_factors_list = prime_factors(n)
    primes_sum = 0
    for prime in prime_factors_list:
        for digit in str(prime):
            primes_sum += int(digit)

    if len(prime_factors_list) >= 2:
        return digits_sum == primes_sum

    return False


def generate_smith_numbers(n: int) -> list:
    """Returns a list of the first n Smith numbers."""
    if n < 0:
        raise ValueError("n must be a positive integer")

    results = []
    incr = 1
    while len(results) < n:
        if smith_number(incr):
            results.append(incr)

        incr += 1

    return results

```

