from math import gcd, sqrt, isqrt
from time import time

start = time()
nmax = 10**8
cc = nmax // 3
for q in range(1, isqrt(nmax) + 1):
    for p in range(q + 1, int(sqrt(2)*q) + 1):
        if gcd(p, q) == 1:
            d = 2 if p % 2 == 0 else 1
            r = (p + q) * (p + 2 * q) // d
            cc += nmax // r
    for p in range(q + 1, int(sqrt(3)*q) + 1):
        if gcd(p, q) == 1:
            d = (3 if p % 3 == 0 else 1) * (2 if (p + q) % 2 == 0 else 1)
            r = (p + q) * (p + 3 * q) // d
            cc += nmax // r
print(f'Solution: {cc}, Run-Time: {time()-start}')

