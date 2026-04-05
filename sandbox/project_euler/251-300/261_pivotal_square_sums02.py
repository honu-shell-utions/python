"""
Jim McCleery
April 4, 2026
Kailua-Kona, HI

Purpose:
    This program searches for all integers k in a given range for which
    isok(k) returns True.

    The code uses a few number-theoretic tests:
    1. A prime number is immediately rejected.
    2. A special quadratic-form test is applied.
    3. If that does not succeed, a more detailed search is performed.

    The goal here is clarity and readability rather than extreme brevity.
"""

from sympy import isprime
from sympy.core.intfunc import isqrt
from sympy.ntheory.primetest import is_square


def twice_pronic(n):
    """
    Return 2n(n + 1).

    A pronic number is a product of two consecutive integers:
        n(n + 1)

    This function returns twice that quantity:
        2n(n + 1)

    Example:
        twice_pronic(3) = 2 * 3 * 4 = 24
    """
    return 2 * n * (n + 1)


def is_special_form(n):
    """
    Return True when n has the form

        n = 2m(m + 1)

    for some integer m >= 0.

    Why this test works:
    --------------------
    Start with

        n = 2m(m + 1)

    Multiply out:

        n = 2m^2 + 2m

    Then

        2n + 1 = 4m^2 + 4m + 1 = (2m + 1)^2

    So n has the required form exactly when:
        1. n is even, and
        2. 2n + 1 is a perfect square.
    """
    return (n % 2 == 0) and is_square(2 * n + 1)


def isok(k):
    """
    Determine whether the integer k satisfies the target property.

    Overview of the logic:
    ----------------------
    1. If k is prime, reject it immediately.
    2. If k has the special form 2m(m + 1), accept it immediately.
    3. Otherwise, carry out a search over values of m.

    About the search:
    -----------------
    For each m, we begin with a quantity S and repeatedly decrease it.
    If S ever becomes exactly 0, then we have found a successful case
    and return True. If every search path fails, we return False.

    This function keeps the mathematical logic of the original program,
    but presents it in a more readable classroom style.
    """
    # Step 1: prime numbers are excluded immediately.
    if isprime(k):
        return False

    # Step 2: numbers of the form 2m(m + 1) are accepted immediately.
    if is_special_form(k):
        return True

    # We will use k^2 several times, so compute it once.
    k_squared = k * k

    # The original program searches m from 1 up to floor(sqrt(k) / 2).
    max_m = isqrt(k) // 2

    for m in range(1, max_m + 1):
        m_squared = m * m
        two_m = 2 * m

        # The variable h starts at k + 1 for each new choice of m.
        h = k + 1

        # Initial value of the quantity being reduced during the search.
        S = k_squared - k * twice_pronic(m)

        # Continue while S is still positive.
        # On each pass we subtract the next increment and then increase h.
        while S > 0:
            S -= m_squared + h * two_m
            h += 1

            # If S reaches 0 exactly, the search succeeds.
            if S == 0:
                return True

    # If no choice of m works, then k does not satisfy the property.
    return False


def main():
    """
    Compute the sum of all integers k with

        1 <= k < 1000

    such that isok(k) returns True.
    """
    total = 0

    for k in range(1, 1000):
        if isok(k):
            total += k

    print(total)


if __name__ == "__main__":
    main()
