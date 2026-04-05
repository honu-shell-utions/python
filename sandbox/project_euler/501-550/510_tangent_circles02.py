#  -----------------------------------------------------------------------------
#  Tangent Circles
#  Problem 510
#  https://projecteuler.net/problem=510
#  -----------------------------------------------------------------------------
from math import gcd, isqrt
from time import time
#  -----------------------------------------------------------------------------
def euler_510(n):
    result = 0
    for a in range(1, isqrt(isqrt(n)) + 1):
        b_max = int(min(isqrt(n)/a - a, a))
        for b in range(1, b_max + 1):
            if gcd(a,b) == 1:
                ra = (a * (a + b)) ** 2
                rb = (b * (a + b)) ** 2
                rc = (a * b) ** 2
                i = n//ra
                result += (i * (i + 1) // 2) * (ra + rb + rc)
    return result
#  -----------------------------------------------------------------------------
for exp in range(1,10):
    limit = 10**exp
    start = time()
    print(f'Solution for n = 10^{exp}: {euler_510(limit):19}, Run-Time: {time()-start}')
#  -----------------------------------------------------------------------------
#  solution: 315306518862563689
#  -----------------------------------------------------------------------------
