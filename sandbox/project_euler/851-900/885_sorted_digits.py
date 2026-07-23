# Jim McCleery
# July 23, 2026
# Kailua-Kona, HI
#
# https://projecteuler.net/problem=885

import math
from collections import Counter
from itertools import combinations_with_replacement

def S(N):
    # Precompute factorials for fast permutation counts: N! / (c0! * c1! * ... * c9!)
    fact = [math.factorial(i) for i in range(N + 1)]

    total_sum = 0

    # Generate all sorted digit combinations of length 18
    # e.g., (0, 0, ..., 1, 2, 3)
    for digits in combinations_with_replacement(range(10), N):
        
        # 1. Count how many times each digit (0-9) appears in this combination
        counts = Counter(digits)
        
        # 2. Calculate the number of distinct original numbers (permutations)
        #    that yield this exact combination
        denom = 1
        for c in counts.values():
            denom *= fact[c]
        permutations = fact[N] // denom

        # 3. Form the integer value f(x) by ignoring zeros
        #    e.g., (0, 0, 1, 3, 4) -> '134' -> 134
        non_zero_digits = [d for d in digits if d > 0]
        if non_zero_digits:
            f_val = int("".join(map(str, non_zero_digits)))
        else:
            f_val = 0

        # 4. Multiply f_val by its number of permutations and add to the total
        total_sum = (total_sum + f_val * permutations)

    return total_sum

print("S(1) =", S(1))
print("S(5) =", S(5))
print("S(18) % 1123455689 =", S(18) % 1123455689)








