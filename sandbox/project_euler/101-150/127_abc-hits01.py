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
from time import time
from sympy import primefactors
from math import gcd, prod
################################################################################
def rad(n):
    p_factors = primefactors(n)
    return prod(p_factors)
################################################################################
def is_abc_hit(a,b,c):
    if gcd(a,b) == gcd(a,c) == gcd(b,c) == 1:
        if a < b:
            if a + b == c:
                if rad(a)*rad(b)*rad(c) < c:
                    return True
        return False
################################################################################
start = time()
sum_c = 0
max = 1000
for a in range(1,max):
    for b in range(a+1,max):
        for c in range(b+1,max):
            if is_abc_hit(a,b,c):
               sum_c += c
print('The solution:',sum_c,'Run-Time:',time()-start)
################################################################################
#solution: 18407904
################################################################################
