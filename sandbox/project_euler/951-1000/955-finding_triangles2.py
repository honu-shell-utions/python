"""
https://projecteuler.net/problem=955
"""

import math
from sympy import factorint


def T(n: int) -> int:
    """Return the nth triangular number."""
    return n * (n + 1) // 2


def divisors_from_factorization(fac: dict[int, int]) -> list[int]:
    """
    Build all positive divisors from a prime factorization.

    Example:
        {2: 3, 3: 1}  -> divisors of 2^3 * 3 = 24
    """
    divisors = [1]
    for p, e in fac.items():
        divisors = [d * (p ** k) for d in divisors for k in range(e + 1)]
    return divisors


def next_hit_from_triangle_index(t: int) -> tuple[int, int]:
    """
    Suppose the current triangular hit is T(t).

    Return (g, m), where:
        g = number of sequence steps until the next triangular hit
        m = index of that next triangular number, so the next hit is T(m)

    Method:
        From
            T(m) = T(t) + T(g),
        we derive
            (m - g)(m + g + 1) = t(t + 1).

        Thus if a*b = t(t+1), then
            g = (b - a - 1) // 2
            m = (a + b - 1) // 2,
        provided these are integers and g > 0.
    """
    N = t * (t + 1)

    # Factor t and t+1 separately, then combine.
    # Consecutive integers are coprime, so this is natural and efficient.
    fac = factorint(t)
    for p, e in factorint(t + 1).items():
        fac[p] = fac.get(p, 0) + e

    divisors = divisors_from_factorization(fac)
    root = math.isqrt(N)

    best_g = None
    best_m = None

    # For each divisor a <= sqrt(N), pair it with b = N // a.
    for a in divisors:
        if a > root:
            continue

        b = N // a

        # Need g = (b - a - 1)/2 to be an integer.
        if (b - a - 1) % 2 != 0:
            continue

        g = (b - a - 1) // 2
        m = (a + b - 1) // 2

        if g > 0 and (best_g is None or g < best_g):
            best_g = g
            best_m = m

    if best_g is None:
        raise ValueError(f"No valid next triangular hit found for t = {t}")

    return best_g, best_m


def find_nth_triangle_hit(n: int) -> tuple[int, int]:
    """
    Return (sequence_index, triangle_value), where triangle_value is the nth
    triangular number appearing in the sequence.

    The first triangular hit is 3 = T(2), which occurs at sequence index 0.
    """
    if n < 1:
        raise ValueError("n must be at least 1")

    hit_count = 1
    seq_index = 0
    t = 2

    while hit_count < n:
        g, t = next_hit_from_triangle_index(t)
        seq_index += g
        hit_count += 1

    return seq_index, T(t)


if __name__ == "__main__":
    idx10, val10 = find_nth_triangle_hit(10)
    print(f"10th triangular hit: index = {idx10}, value = {val10}")

    idx70, val70 = find_nth_triangle_hit(70)
    print(f"70th triangular hit: index = {idx70}, value = {val70}")
