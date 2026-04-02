#  -----------------------------------------------------------------------------
#  Tangent Circles
#  Problem 510
#  https://projecteuler.net/problem=510
#  -----------------------------------------------------------------------------
from math import sqrt, isqrt, gcd
from time import time
#  -----------------------------------------------------------------------------
def S(n):
    total = 0
    for r1 in range(1,n+1):
        if sqrt(r1) != isqrt(r1):
            continue
        for r2 in range(r1,n+1):
            if sqrt(r2) != isqrt(r2):
                continue
            r3 = r1*r2/(sqrt(r1) + sqrt(r2))**2
            if r3 % 1 == 0 and gcd(r1,r2,int(r3)) == 1:
                m = n // r2
                total += (r1 + r2 + r3)*m*(m+1)/2
    return int(total)
#  -----------------------------------------------------------------------------
for limit in [5,10**2,10**5]:
    start = time()
    print(f'Solution for n = {limit:10}: {S(limit):19}, Run-Time: {time()-start}')
#  -----------------------------------------------------------------------------
#  solution: 315306518862563689
#  -----------------------------------------------------------------------------
