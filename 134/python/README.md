# Weekly Challenge 134

## TASK #1 › Pandigital Numbers

Write a script to generate first 5 `Pandigital Numbers` in base 10.

As per the [wikipedia](https://en.wikipedia.org/wiki/Pandigital_number), it says:

> A pandigital number is an integer that in a given base has among its significant digits each digit used in the base at least once.



### Solution

```python
def is_pandigital(num: int) -> bool:
	"""Returns whether a number is a pandigital number in base 10."""
    if type(num) != int:
        raise TypeError("num must an integer value")

    base = 10
    digits_list = [str(i) for i in range(0, base)]
    num_as_string = str(num)

    return set(num_as_string) == set(digits_list)



def pandigital_nums(n: int) -> list:
    """Returns a list of the first n pandigital numbers in base 10."""
    if n < 0:
        raise ValueError("n must be a positive integer")

    # Define first pandigital number (for performance):
    start = 1023456789
    results = []
    while len(results) < n:
        if is_pandigital(start):
            results.append(start)
        start += 1

    return results
	
```

---
## Task 2 > Distinct Terms Count

You are given 2 positive numbers, `$m` and `$n`.

Write a script to generate multiplcation table and display count of distinct terms.

**Example 1:**
```
Input: $m = 3, $n = 3
Output:

      x | 1 2 3
      --+------
      1 | 1 2 3
      2 | 2 4 6
      3 | 3 6 9

Distinct Terms: 1, 2, 3, 4, 6, 9
Count: 6
```


**Example 2:**
```
Input: $m = 3, $n = 5
Output:

      x | 1  2  3  4  5
      --+--------------
      1 | 1  2  3  4  5
      2 | 2  4  6  8 10
      3 | 3  6  9 12 15

Distinct Terms: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15
Count: 11
```



### Solution

```python


```