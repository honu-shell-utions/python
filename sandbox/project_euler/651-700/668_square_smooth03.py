#  -----------------------------------------------------------------------------
#  Square root smooth Numbers
#  Problem 668
#  https://projecteuler.net/problem=668
#  -----------------------------------------------------------------------------
from sympy import primepi
from math import isqrt
from time import time
#  -----------------------------------------------------------------------------
def euler_668(n):
    total = 0
    for y in range(1,isqrt(n)):
        total += primepi(n//y) - primepi(y - 1)
    return int(n - total)
#  -----------------------------------------------------------------------------
for exp in [2,4,6,8,10]:
    start = time()
    n = 10**exp
    sol = euler_668(n)
    print(f'Solution for n = 10^{exp:2}: {sol:11}, Run-Time: {time()-start:.3f}')
#  -----------------------------------------------------------------------------
#  solution: 2811077773
#  -----------------------------------------------------------------------------
