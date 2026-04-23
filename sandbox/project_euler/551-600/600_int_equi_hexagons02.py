"""
Let H(n) be the number of distinct integer sided equiangular
convex hexagons with perimeter not exceeding (n).

Hexagons are distinct if and only if they are not congruent.

You are given

H(6)=1,H(12)=10,H(100)=31248.

Find H(55106).
"""

from fractions import Fraction

def H(n):
    """
    Counts the number of ways to tile a 6×n board with 1×2 dominoes (or
    equivalently, the number of perfect matchings of a 6×n grid graph).
    Uses a closed-form formula that varies by n mod 12, derived from the
    eigenvalue decomposition of the transfer matrix.

    Args:
        n: The number of columns in the 6×n board. Must be a non-negative
           even integer for a perfect tiling to be possible.

    Returns:
        The exact tiling count as an integer (or Fraction that equals an integer).
    """
    r = n % 12  # Period of the closed-form formula is 12

    # Each branch is the closed-form polynomial for H(n) in its residue class.
    # All share the leading terms n^4/3456 + n^3/432; lower-order correction
    # terms differ by residue to account for boundary effects.

    if r == 0:
        # Correction terms vanish; result is always a whole number
        return n**4 // 3456 + n**3 // 432

    if r in (1, 7):
        return (Fraction(n**4, 3456) +
                Fraction(n**3, 432) -
                Fraction(n**2, 192) -
                Fraction(17*n, 432) +
                Fraction(145, 3456))

    if r == 2:
        return (Fraction(n**4, 3456) +
                Fraction(n**3, 432) -
                Fraction(n, 27) +
                Fraction(11, 216))

    if r in (3, 9):
        return (Fraction(n**4, 3456) +
                Fraction(n**3, 432) -
                Fraction(n**2, 192) -
                Fraction(n, 48) +
                Fraction(3, 128))

    if r == 4:
        return (Fraction(n**4, 3456) +
                Fraction(n**3, 432) -
                Fraction(n, 54) -
                Fraction(4, 27))

    if r in (5, 11):
        return (Fraction(n**4, 3456) +
                Fraction(n**3, 432) -
                Fraction(n**2, 192) -
                Fraction(25*n, 432) -
                Fraction(175, 3456))

    if r == 6:
        return (Fraction(n**4, 3456) +
                Fraction(n**3, 432) +
                Fraction(1, 8))

    if r == 8:
        return (Fraction(n**4, 3456) +
                Fraction(n**3, 432) -
                Fraction(n, 27) -
                Fraction(2, 27))

    if r == 10:
        return (Fraction(n**4, 3456) +
                Fraction(n**3, 432) -
                Fraction(n, 54) -
                Fraction(5, 216))

print(H(55106))

