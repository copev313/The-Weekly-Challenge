import math


def power_of_two(num: int) -> int:
    """Determines if a number is a (positive) power of two.
    Returns positive integer of the power if true, else 0.
    """
    if num <= 0:
        raise ValueError("Only positive integers allowed.")
    elif type(num) != int:
        raise TypeError("Only integers are allowed.")

    # [CASE] num is odd:
    if num % 2 != 0:
        return 0

    # [CASE] num is even:
    power = 1
    while num / 2 != 1:
        # [CASE] num not divisible by 2:
        if num % 2 != 0:
            return 0
        # [CASE] num divisible by 2:
        num = num // 2
        power += 1

    return power


def determine_two_friendly(m: int, n: int) -> str:
    """Determine if two numbers are 'Two Friendly'."""
    if m <= 0 or n <= 0:
        raise ValueError("Only positive integers allowed.")
    elif type(m) != int or type(n) != int:
        raise TypeError("Only integers are allowed.")

    # Find the greatest common divisor of m and n:
    gcd = math.gcd(m, n)
    power = power_of_two(gcd)
    is_friendly = bool(power)

    input_line = f"\nInput: $m = {m}, $n = {n}"
    output_line = f"\nOutput: {int(is_friendly)}"
    reason_line = f"\n\nReason: gcd({m}, {n}) = {gcd}"

    # Attach power reasoning when applicable:
    if is_friendly:
        reason_line += f" => 2 ^ {power}"

    return input_line + output_line + reason_line


# print(determine_two_friendly(8, 24))
