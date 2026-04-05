"""
Jim McCleery
April 4, 2026
Kailua-Kona, HI

This program finds integers k in a given range for which isok(k) is True.

The original version used compact expressions and short variable names.
Here the same ideas are written in a more explanatory style so that students
can follow the logic step by step.
"""

from sympy import isprime
from sympy.core.intfunc import isqrt
from sympy.ntheory.primetest import is_square


def twice_pronic(n):
    """
    Return 2*n*(n + 1).

    The product n*(n + 1) is called a pronic number, so this function returns
    twice a pronic number. This quantity appears repeatedly in the algorithm.
    """
    return 2 * n * (n + 1)


def is_of_special_form(n):
    """
    Return True when n has the form 2*m*(m + 1) for some integer m >= 0.

    Reason:
        If n = 2*m*(m + 1), then

            2n + 1 = 4m(m + 1) + 1 = (2m + 1)^2,

        so 2n + 1 must be a perfect square.

    Also, every number of the form 2*m*(m + 1) is even.
    """
    return (n % 2 == 0) and is_square(2 * n + 1)


def isok(k):
    """
    Decide whether k satisfies the property tested by this program.

    The logic is:

    1. If k is prime, reject it immediately.
    2. If k has the special form 2*m*(m + 1), accept it immediately.
    3. Otherwise, perform the search contained in the original program.

    The search works by trying values of m and updating a running quantity.
    If that quantity ever becomes exactly 0, then k is accepted.
    """
    # Step 1: primes are excluded immediately.
    if isprime(k):
        return False

    # Step 2: numbers of the special algebraic form are accepted immediately.
    if is_of_special_form(k):
        return True

    k_squared = k * k

    # The original program searched m up to floor(sqrt(k)/2).
    for m in range(1, (isqrt(k) >> 1) + 1):
        m_squared = m * m
        two_m = 2 * m
        h = k + 1

        # Starting value for the running subtraction process.
        running_total = k_squared - k * twice_pronic(m)

        # Continue until the running total is no longer positive.
        while running_total > 0:
            running_total -= m_squared + h * two_m
            h += 1

            # Success occurs when we land exactly on 0.
            if running_total == 0:
                return True

    # If no value of m succeeds, then k does not satisfy the condition.
    return False


def main():
    """
    Sum all integers k in the range 1 <= k < 1000 for which isok(k) is True,
    and print the result.
    """
    total = 0

    # This version is intentionally straightforward and readable.
    # It is not designed for very large upper bounds such as 10**10.
    for k in range(1, 10**3):
        if isok(k):
            total += k

    print(total)


if __name__ == "__main__":
    main()
