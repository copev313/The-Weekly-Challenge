
def prime_factors(n: int) -> list:
    """Returns a list of prime factors of n."""
    # Input validation:
    if n <= 0:
        raise ValueError("n must be a positive integer")

    factors = []
    test_prime = 2

    while test_prime ** 2 <= n:
        # [CASE] Prime could be larger:
        if n % test_prime != 0:
            test_prime += 1
        # [CASE] Largest prime factor is found:
        else:
            n //= test_prime
            factors.append(test_prime)

    # Handle remaining factor:
    if n > 1:
        factors.append(n)

    return factors


def smith_number(n: int) -> bool:
    """Returns whether a given integer is a Smith number."""
    # Input validation:
    if n <= 0:
        raise ValueError("n must be a positive integer")

    # Calculate the sum of n's digits:
    digits_sum = 0
    for digit in str(n):
        digits_sum += int(digit)

    # Find prime factors:
    prime_factors_list = prime_factors(n)
    primes_sum = 0
    # Handle the sum of digits in the prime factorization:
    for prime in prime_factors_list:
        for digit in str(prime):
            primes_sum += int(digit)

    # [CHECK] Fits Definition:
    # The number is composite and the sum of its digits is equal to 
    # the sum of its prime factors' digits:
    if len(prime_factors_list) >= 2:
        return digits_sum == primes_sum

    return False


def generate_smith_numbers(n: int) -> list:
    """Returns a list of the first n Smith numbers."""
    # Input validation:
    if n < 0:
        raise ValueError("n must be a positive integer")

    # Initialize the list of Smith numbers:
    results = []
    incr = 1
    while len(results) < n:
        # Find the next Smith number:
        if smith_number(incr):
            results.append(incr)

        incr += 1

    return results
