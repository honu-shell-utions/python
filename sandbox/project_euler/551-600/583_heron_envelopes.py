# -----------------------------------------------------------------------------
# Jim McCleery
# May 29, 2026
# Kailua-Kona, HI
#
# https://projecteuler.net/problem=583
# -----------------------------------------------------------------------------

from collections import defaultdict
from math import gcd, isqrt
from time import perf_counter

# -----------------------------------------------------------------------------
def build_pythagorean_lookup(limit):
    """
    Build a lookup table of Pythagorean triples.

    For each integer side length, we store pairs:

        other_leg, hypotenuse
    """

    lookup = defaultdict(list)

    for p in range(2, isqrt(limit) + 2):
        for q in range(1, p):

            if p * p + q * q > limit:
                break

            if gcd(p, q) != 1:
                continue

            if (p - q) % 2 == 0:
                continue

            leg1 = p * p - q * q
            leg2 = 2 * p * q
            hypotenuse = p * p + q * q

            multiplier = 1

            while multiplier * hypotenuse <= limit:
                a = multiplier * leg1
                b = multiplier * leg2
                c = multiplier * hypotenuse

                if a % 2 == 0:
                    lookup[a].append((b, c))

                if b % 2 == 0:
                    lookup[b].append((a, c))

                multiplier += 1

    return lookup


# -----------------------------------------------------------------------------
def solve(limit):
    """
    Return S(limit), the sum of the perimeters of all Heron envelopes
    with perimeter <= limit.
    """

    lookup = build_pythagorean_lookup(limit)

    total = 0

    for shared_side in lookup:

        available_other_legs = {
            other_leg for other_leg, hypotenuse in lookup[shared_side]
        }

        for other_leg_1, hypotenuse_1 in lookup[shared_side]:

            if hypotenuse_1 % 2 != 0:
                continue

            half_height = other_leg_1 // 2

            for other_leg_2, hypotenuse_2 in lookup[shared_side]:

                if other_leg_2 < half_height:
                    continue

                missing_diagonal = 2 * half_height + 2 * other_leg_2

                if missing_diagonal not in available_other_legs:
                    continue

                perimeter = hypotenuse_1 + shared_side + 2 * other_leg_2

                if perimeter <= limit:
                    total += perimeter

    return total


# -----------------------------------------------------------------------------
def main():
    """
    Run the program and print both the answer and the elapsed time.
    """

    max_perimeter = 10**7

    start_time = perf_counter()

    answer = solve(max_perimeter)

    end_time = perf_counter()
    elapsed_time = end_time - start_time

    print(f"Answer: {answer}")
    print(f"Elapsed time: {elapsed_time:.6f} seconds")


# -----------------------------------------------------------------------------
# Main program
# -----------------------------------------------------------------------------

if __name__ == "__main__":
    main()
