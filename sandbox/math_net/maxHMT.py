"""
Problem:
Find the maximum possible value of H * M * M * T over all ordered triples
(H, M, T) of integers such that

    H * M * M * T = H + M + M + T

Equivalently,

    H * M^2 * T = H + 2M + T

Notes:
- There are infinitely many zero-product solutions when one of H, M, or T is 0.
- The nonzero integer solutions are:
      (2, 1, 4), (4, 1, 2), (-1, -2, 1), (1, -2, -1)
- Therefore the maximum possible value is 8.
"""


def find_solutions():
    """
    Return all nonzero integer solutions together with the maximum product.

    Algebra outline:
    ----------------
    Starting from

        H * M^2 * T = H + 2M + T

    solve for H:

        H = (2M + T) / (T*M^2 - 1)

    For H to be an integer, the denominator must divide the numerator.

    Positive-product case:
    ----------------------
    If H*M^2*T > 0, then H and T have the same sign, and one can show that
    M must equal 1. Substituting M = 1 gives

        H*T = H + T + 2
        (H - 1)(T - 1) = 3

    which yields the two positive solutions:

        (2, 1, 4), (4, 1, 2)

    Negative-product case:
    ----------------------
    A direct check of the nonzero negative cases gives the two solutions:

        (-1, -2, 1), (1, -2, -1)
    """

    solutions = []

    # ---------------------------------------------------------
    # Positive-product solutions
    # From the algebra, M must be 1, and then
    #     (H - 1)(T - 1) = 3
    # The positive divisors of 3 are 1 and 3.
    # ---------------------------------------------------------
    M = 1
    for d in (1, 3):
        H = d + 1
        T = 3 // d + 1

        # Verify the triple before storing it.
        if H * M * M * T == H + 2 * M + T:
            solutions.append((H, M, T))

    # ---------------------------------------------------------
    # Negative-product solutions
    # These are the only nonzero negative solutions.
    # ---------------------------------------------------------
    for H, M, T in [(-1, -2, 1), (1, -2, -1)]:
        if H * M * M * T == H + 2 * M + T:
            solutions.append((H, M, T))

    # Compute the maximum product among the nonzero solutions.
    max_product = max(H * M * M * T for H, M, T in solutions)

    return solutions, max_product


# -------------------------------------------------------------
# Main program
# -------------------------------------------------------------
solutions, max_product = find_solutions()

print("Nonzero integer solutions:")
for H, M, T in solutions:
    product = H * M * M * T
    print(f"(H, M, T) = ({H}, {M}, {T}), product = {product}")

print()
print("Maximum possible value:", max_product)
