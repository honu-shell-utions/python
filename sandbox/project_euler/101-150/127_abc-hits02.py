################################################################################
# 127_abc-hits.py
#
# The radical of n, rad(n), is the product of distinct prime factors of n.
# For example, 504 = 2^3 × 3^2 × 7, so rad(504) = 2 × 3 × 7 = 42.
#
# We shall define the triplet of positive integers (a, b, c) to be an
# abc-hit if:
# 1) GCD(a, b) = GCD(a, c) = GCD(b, c) = 1
# 2) a < b
# 3) a + b = c
# 4) rad(abc) < c
#
# For example, (5, 27, 32) is an abc-hit, because:
# 1) GCD(5, 27) = GCD(5, 32) = GCD(27, 32) = 1
# 2) 5 < 27
# 3) 5 + 27 = 32
# 4) rad(4320) = 30 < 32
# It turns out that abc-hits are quite rare and there are only thirty-one
# abc-hits for c < 1000, with ∑c = 12523.
#
# Find ∑c for c < 120_000
################################################################################
import math

# Here are some observations that lead to optimizations:
# - For each integer n >= 2, we have 2 <= rad(n) <= n.
# - By Euclid's GCD algorithm, gcd(c,b) = gcd(a+b,b) = gcd(a,b) = gcd(a,a+b) = gcd(a,c).
#   Hence gcd(a,b) = 1 if and only if gcd(a,c) = 1 and gcd(b,c) = 1.
#   We only need to compute and check one of these three GCDs.
# - Since {a, b, c} are mutually coprime, we have rad(a * b * c) = rad(a) * rad(b) * rad(c).
# - Instead of trying all 'a' values in the range [1, c), we only try promising 'a' values such that rad(a) * rad(c) < c.
#   If we try 'a' values in ascending order of rad(a), then we can stop the search early and not examine many values of 'a'.


def compute():
    LIMIT = 120_000
    # Modification of the sieve of Eratosthenes
    rads = [0] + [1] * (LIMIT - 1)
    for i in range(2, len(rads)):
        if rads[i] == 1:
            for j in range(i, len(rads), i):
                rads[j] *= i

	
    sortedrads = sorted((rad, n) for (n, rad) in enumerate(rads))
    sortedrads = sortedrads[1 : ]  # Get rid of the (0, 0) entry
	
    ans = 0

    for c in range(2, LIMIT):
        for (rad, a) in sortedrads:
            rad *= rads[c]
            if rad >= c:
                break
            b = c - a
            if a < b and rad * rads[b] < c and math.gcd(a, b) == 1:
                ans += c
                    
    return ans

print(compute())

#solution: 18407904
