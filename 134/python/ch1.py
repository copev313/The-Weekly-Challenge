

def is_pandigital(num: int) -> bool:
    """Returns whether a number is a pandigital number in base 10."""
    # Input validation:
    if type(num) != int:
        raise TypeError("num must an integer value")

    # Define our digit goals:
    base = 10
    digits_list = [str(i) for i in range(0, base)]

    # Convert the number in question into a string:
    num_as_string = str(num)

    return set(num_as_string) == set(digits_list)



def pandigital_nums(n: int) -> list:
    """Returns a list of the first n pandigital numbers in base 10."""
    # Input validation:
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
