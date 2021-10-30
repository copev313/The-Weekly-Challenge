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


## Task 2 > Smith Number

Write a script to generate the first 10 `Smith Numbers` in base 10.

According to Wikipedia:

> In number theory, a Smith number is a composite number for which, in a given
> number base, the sum of its digits is equal to the sum of the digits in its
> prime factorization in the given number base.

### Solution [In Progress]

```python


```

