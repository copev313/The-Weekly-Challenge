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
def gen_mult_matrix(row: int, col: int) -> list:
    """Generate a multiplication matrix of size row x col."""
    if row <= 0 or col <= 0:
        raise ValueError("Matrix size must be positive")
    if type(row) != int or type(col) != int:
        raise TypeError("Matrix size must be integer values")

    matrix = []
    for r in range(1, row + 1):
        row_list = []
        for c in range(1, col + 1):
            row_list.append(r * c)
        matrix.append(row_list)

    return matrix


def print_results(matrix: list) -> None:
    """Print the results."""
    m = len(matrix)
    n = len(matrix[0])
    print(f"\nInput: m = {m}, n = {n}")
    print(f"Output:\n")

    first_row = " x | " + "  ".join([str(x) for x in range(1, n + 1)])
    second_row = "---+" + "---" * n
    generated_rows = ""
    for index, row in enumerate(matrix):
        nth_row = f" {index + 1} |"

        for x in row:
            # Extra spacing for single digit numbers:
            if len(str(x)) == 1:
                nth_row += " "

            nth_row += f"{x} "

        generated_rows += nth_row + "\n"

    print(first_row)
    print(second_row)
    print(generated_rows)

    distinct_terms = []
    for row in matrix:
        for term in row:
            if term not in distinct_terms:
                distinct_terms.append(term)

    stringed_terms = ", ".join(str(term) for term in sorted(distinct_terms))
    print(f"Distinct Terms: {stringed_terms}")
    print(f"Count: {len(distinct_terms)}")
```
