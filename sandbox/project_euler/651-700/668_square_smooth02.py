#  -----------------------------------------------------------------------------
#  Square root smooth Numbers
#  Problem 668
#  https://projecteuler.net/problem=668
#  -----------------------------------------------------------------------------
from math import floor, isqrt
from sympy import primepi
from time import time
#  -----------------------------------------------------------------------------
def euler_668(n):
    accum = 0
    for y in range(1,isqrt(n)):
        accum += primepi(n/y) - primepi(y-1)
    return int(n-accum)
#  -----------------------------------------------------------------------------
for exp in range(1,11):
    start = time()
    print(f'Solution for n^{exp:2}: {euler_668(10**exp):11}, Run-Time: {time()-start:8.3f}')
#  -----------------------------------------------------------------------------
#  solution: 2811077773
#  -----------------------------------------------------------------------------
