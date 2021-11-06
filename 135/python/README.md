# Weekly Challenge 135

## TASK #1 › Middle 3-digits

You are given an integer.

Write a script find out the middle 3-digits of the given integer, if possible otherwise throw sensible error.

**Example 1:**
```
Input: $n = 1234567
Output: 345
```

**Example 2:**
```
Input: $n = -123
Output: 123
```

**Example 3:**
```
Input: $n = 1
Output: too short
```

**Example 4:**
```
Input: $n = 10
Output: even number of digits
```

### Solution

Every example in this task proved to be a useful one, as each demonstrated a case that needed to be handled differently.
For more explanation on the flow of the solution, please refer to [ch1.py](135\python\ch1.py).

```python
def middle_three_digits(num: int) -> str:
    """Returns the middle three digits of a number if possible,
    otherwise throws an error.
    """
    if type(num) != int:
        raise TypeError("Input must be an integer.")

    num_as_str = str(num)

    if num_as_str[0] == "-":
        num_as_str = num_as_str[1:]

    if len(num_as_str) < 3:
        return "Number is too short."

    if len(num_as_str) % 2 == 0:
        return "Number is even."

    if len(num_as_str) == 3:
        return num_as_str

    start = (len(num_as_str) // 2) - 1
    end = (len(num_as_str) // 2) + 2

    # Leave result as string to account for leading zeros:
    return num_as_str[start:end]

```

---
## Task 2 > Validate SEDOL

You are given 7-characters alphanumeric SEDOL.

Write a script to validate the given SEDOL. Print 1 if it is a valid SEDOL otherwise 0.

For more information about SEDOL, please checkout the [wikipedia](https://en.wikipedia.org/wiki/SEDOL) page.

**Example 1:**
```
Input: $SEDOL = '2936921'
Output: 1
```

**Example 2:**
```
Input: $SEDOL = '1234567'
Output: 0
```

**Example 3:**
```
Input: $SEDOL = 'B0YBKL9'
Output: 1
```

### Solution

```python


```