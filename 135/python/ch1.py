
def middle_three_digits(num: int) -> str:
    """Returns the middle three digits of a number if possible,
    otherwise throws an error.
    """
    if type(num) != int:
        raise TypeError("Input must be an integer.")

    num_as_str = str(num)

    # [CASE] Negative number:
    if num_as_str[0] == "-":
        num_as_str = num_as_str[1:]

    # [CASE] Too short:
    if len(num_as_str) < 3:
        return "Number is too short."

    # [CASE] Even number of digits:
    if len(num_as_str) % 2 == 0:
        return "Number is even."

    # [CASE] Exactly three digits:
    if len(num_as_str) == 3:
        return num_as_str

    # [CASE] Find middle three digits:
    start = (len(num_as_str) // 2) - 1
    end = (len(num_as_str) // 2) + 2

    # Leave result as string to account for leading zeros:
    return num_as_str[start:end]
