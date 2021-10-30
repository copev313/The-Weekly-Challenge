
def int_sqrt(n: int) -> int:
    """Return the integer square root of n."""

    # [CASE] n is negative:
    if n < 0:
        raise ValueError("n must be >= 0")

    # Use exponential method to find the square root:
    sqrt = n ** (1/2)
    # Convert any float to int closest to zero:
    return int(sqrt)
