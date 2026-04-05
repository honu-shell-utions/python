#  -----------------------------------------------------------------------------
#  Prime triples and geometric sequences
#  Problem 518
#  https://projecteuler.net/problem=518
#  -----------------------------------------------------------------------------
from sympy import isprime
from math import isqrt, gcd
from time import time
#  -----------------------------------------------------------------------------
for exp in range(2,9):
    start = time()
    total = 0
    limit = 10**exp
    for x in range(2, isqrt(limit+1)):
        for k in range(1, (limit - 1) // (x ** 2) + 1):
            c = k * x * x - 1
            if isprime(c):
                for y in range(1, x):
                    a = k * y * y - 1
                    b = k * x * y - 1
                    if c < limit and isprime(a) and isprime(b) and gcd(x, y) == 1:
                        total += a + b + c
    print(f'Solution for n = 10^{exp} = {total:16}, Run-Time: {time()-start}')
#  -----------------------------------------------------------------------------
# 100315739184392
#  -----------------------------------------------------------------------------
