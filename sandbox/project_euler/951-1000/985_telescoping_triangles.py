# -----------------------------------------------------------------------------
# Jim McCleery
# May 17, 2026
# Kailua-Kona, HI
# -----------------------------------------------------------------------------
"""
https://projecteuler.net/problem=985

Experimental assumption:

    Odd target length  -> triangle is (a, a, a + 1)
    Even target length -> triangle is (a, a, a - 1)

For an isosceles triangle (a, a, c), use the ratio

    r = c / a

The next ratio is

    r_next = 2 - r*r

The next triangle exists exactly when

    0 < r < sqrt(2)

This avoids huge integers entirely.

Note:
    This program searches within the experimentally observed near-equilateral
    isosceles family. It does not, by itself, prove that this family contains
    the global Project Euler answer.
"""

from decimal import Decimal, getcontext


# -----------------------------------------------------------------------------
# Use high-precision decimal arithmetic because repeated iteration of
#
#     r -> 2 - r*r
#
# can magnify small numerical errors near the boundary of validity.
# -----------------------------------------------------------------------------
getcontext().prec = 100
SQRT2 = Decimal(2).sqrt()


# -----------------------------------------------------------------------------
def chain_length_near_equilateral(a, sign, stop_at=None):
    """
    Compute the chain length for the near-equilateral isosceles triangle:

        (a, a, a + sign)

    where:

        sign = +1 gives (a, a, a + 1)
        sign = -1 gives (a, a, a - 1)

    The function counts the starting triangle T0 as length 1.

    For example, if T0, T1, and T2 exist, but T3 does not, this function
    returns 3.

    Parameters:
        a:
            The repeated side length in the triangle (a, a, a + sign).

        sign:
            Either +1 or -1.

        stop_at:
            Optional early stopping value. This lets us avoid unnecessary
            iterations once we already know the chain is long enough.

    Returns:
        The number of triangles in the chain, counting T0.
    """

    # Initial side ratio r = c/a.
    r = Decimal(a + sign) / Decimal(a)

    # T0 exists by construction, so start the count at 1.
    n = 1

    while True:
        # Early exit for search purposes.
        if stop_at is not None and n > stop_at:
            return n

        # The next triangle exists exactly when the current ratio lies
        # between 0 and sqrt(2).
        if not (Decimal(0) < r < SQRT2):
            return n

        # Move to the next isosceles triangle ratio.
        r = Decimal(2) - r * r
        n += 1


# -----------------------------------------------------------------------------
def find_near_equilateral_target(target_length):
    """
    Find the smallest near-equilateral isosceles triangle matching target_length.

    Uses the observed pattern:

        odd target_length  -> (a, a, a + 1)
        even target_length -> (a, a, a - 1)

    The search uses two stages:

        1. Repeatedly double the upper bound until a triangle survives
           to the desired target length.

        2. Binary search to find the smallest such value of a.

    Parameters:
        target_length:
            Desired chain length, counting T0.

    Returns:
        A tuple:

            (perimeter, a, c, length)

        where the triangle is (a, a, c), or None if no exact match is found.
    """

    # Use the observed odd/even pattern to choose which near-equilateral
    # family to search.
    sign = 1 if target_length % 2 == 1 else -1

    # First find an upper bound for a.
    hi = 2

    while chain_length_near_equilateral(hi, sign, stop_at=target_length) < target_length:
        hi *= 2

    # The answer lies somewhere between hi//2 + 1 and hi.
    lo = hi // 2 + 1

    # Binary search for the smallest a that reaches the target length.
    while lo < hi:
        mid = (lo + hi) // 2
        length = chain_length_near_equilateral(mid, sign, stop_at=target_length)

        if length >= target_length:
            hi = mid
        else:
            lo = mid + 1

    # Candidate triangle.
    a = lo
    c = a + sign

    # Recompute with a little extra room to make sure the length is exactly
    # target_length, not merely at least target_length.
    length = chain_length_near_equilateral(a, sign, stop_at=target_length + 5)

    if length != target_length:
        return None

    perimeter = 2 * a + c
    return perimeter, a, c, length


# -----------------------------------------------------------------------------
def show_small_hits():
    """
    Print the smallest near-equilateral hits for small target lengths.

    This is mainly a diagnostic function. It displays the pattern that led to
    the experimental assumption:

        odd target length  -> third side is one longer
        even target length -> third side is one shorter
    """

    for target in range(3, 22):
        result = find_near_equilateral_target(target)

        if result is None:
            print(f"Target length {target}: no result found")
        else:
            perimeter, a, c, length = result
            print(
                f"Target length {target}: "
                f"Perimeter={perimeter}, Triangle=({a},{a},{c}), Length={length}"
            )


# -----------------------------------------------------------------------------
if __name__ == "__main__":
    # Display small cases first, both as a sanity check and as evidence for
    # the near-equilateral pattern.
    show_small_hits()

    print()

    # Project Euler 985 asks for T20 to exist but T21 not to exist.
    #
    # Since this program counts T0 as length 1, the corresponding target
    # length is 21.
    target = 21

    result = find_near_equilateral_target(target)

    if result is None:
        print(f"No result found for target length {target}")
    else:
        perimeter, a, c, length = result
        print("Candidate:")
        print(f"Perimeter: {perimeter}")
        print(f"Triangle: ({a}, {a}, {c})")
        print(f"Length: {length}")
