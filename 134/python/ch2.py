
def gen_mult_matrix(row: int, col: int) -> list:
    """Generate a multiplication matrix of size row x col."""
    if row <= 0 or col <= 0:
        raise ValueError("Matrix size must be positive")
    if type(row) != int or type(col) != int:
        raise TypeError("Matrix size must be integer values")

    matrix = []
    # Iterate over the rows:
    for r in range(1, row + 1):
        row_list = []
        # Iterate over the columns:
        for c in range(1, col + 1):
            row_list.append(r * c)
        matrix.append(row_list)

    return matrix


def print_results(matrix: list) -> None:
    """Print the results."""
    m = len(matrix)
    n = len(matrix[0])
    print(f"\nInput: $m = {m}, $n = {n}")
    print("Output:\n")

    # Handle strings row by row:
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

    # Get the distinct terms:
    distinct_terms = []
    for row in matrix:
        for term in row:
            if term not in distinct_terms:
                distinct_terms.append(term)

    stringed_terms = ", ".join(str(term) for term in sorted(distinct_terms))
    print(f"Distinct Terms: {stringed_terms}")
    print(f"Count: {len(distinct_terms)}")


# print(print_results(gen_mult_matrix(3, 3)))
