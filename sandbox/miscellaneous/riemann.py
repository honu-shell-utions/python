"""
https://en.wikipedia.org/wiki/Riemann_hypothesis
"""

from sympy import nextprime
from time import perf_counter
import math

N = 10**6

def zeta_sum(s, limit=N):
    """
    The straightforward definition:

        zeta(s) = sum 1/n^s
    """
    total = 0.0

    print("\n🐢 The Infinite Sum enters the arena...")
    start = perf_counter()

    for n in range(1, limit):
        total += 1 / (n ** s)

        if n in [10, 100, 1000, 10_000, 100_000]:
            print(f"   Sum has reached n = {n:,}... still trudging along.")

    elapsed = perf_counter() - start
    print(f"✅ Infinite Sum finished in {elapsed:.4f} seconds.")

    return total, elapsed


def zeta_prime_product(s, prime_limit=N):
    """
    Euler's product formula:

        zeta(s) = product over primes p of 1 / (1 - p^(-s))
    """
    product = 1.0
    p = 1
    prime_count = 0

    print("\n⚡ Euler's Prime Product bursts onto the scene...")
    start = perf_counter()

    while p < prime_limit:
        p = nextprime(p)
        product *= 1 / (1 - p ** (-s))
        prime_count += 1

        if prime_count in [1, 2, 3, 10, 100, 1000, 10_000]:
            print(f"   Prime #{prime_count:,}: p = {p:,}")

    elapsed = perf_counter() - start
    print(f"✅ Prime Product finished in {elapsed:.4f} seconds.")
    print(f"   It used {prime_count:,} primes.")

    return product, elapsed


def compare_zeta(s):
    print("=" * 60)
    print("        🧮  THE GREAT ZETA SHOWDOWN  🧮")
    print("=" * 60)
    print(f"\nWe are estimating ζ({s}).")
    print("Two contestants:")
    print("  1. The Infinite Sum")
    print("  2. Euler's Prime Product")
    print("\nLet the mathematical games begin.")

    sum_value, sum_time = zeta_sum(s)
    product_value, product_time = zeta_prime_product(s)

    print("\n" + "=" * 60)
    print("                 🏁 FINAL RESULTS")
    print("=" * 60)

    print(f"\nζ({s}) from the sum:           {sum_value:.17f}")
    print(f"ζ({s}) from the prime product: {product_value:.17f}")

    difference = abs(sum_value - product_value)

    print(f"\nAbsolute difference: {difference:.3e}")

    if difference == 0:
        print("🎯 They agree perfectly, at least to Python's floating-point eyes.")
    elif difference < 1e-12:
        print("🎯 They are practically indistinguishable.")
    else:
        print("🤔 They differ noticeably. Maybe the cutoff needs adjusting.")

    print("\nTiming:")
    print(f"  Infinite Sum:        {sum_time:.4f} seconds")
    print(f"  Prime Product:       {product_time:.4f} seconds")

    if sum_time < product_time:
        print("\n🏆 Winner by speed: The Infinite Sum!")
    elif product_time < sum_time:
        print("\n🏆 Winner by speed: Euler's Prime Product!")
    else:
        print("\n🏆 A dead heat! The math gods are amused.")

    print("\nFun fact:")
    print("For large s, ζ(s) gets extremely close to 1,")
    print("because 1/2^s, 1/3^s, 1/4^s, ... become microscopic.")
    print("=" * 60)


compare_zeta(10**3)
