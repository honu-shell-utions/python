#  -----------------------------------------------------------------------------
#  Square root smooth Numbers
#  Problem 668
#  https://projecteuler.net/problem=668
#  -----------------------------------------------------------------------------
from sympy import primefactors
from math import sqrt
from time import time
#  -----------------------------------------------------------------------------
def is_smooth(n):
    if n == 1:
        return True
    if max(primefactors(n)) >= sqrt(n):
        return False
    else:
        return True
#  -----------------------------------------------------------------------------
def euler_668(n):
    count = 0
    for k in range(1,n+1):
        if is_smooth(k):
            count += 1
    return count
#  -----------------------------------------------------------------------------
for exp in range(1,11):
    start = time()
    print(f'Solution for n^{exp:2}: {euler_668(10**exp):11}, Run-Time: {time()-start:8.3f}')
#  -----------------------------------------------------------------------------
#  solution: 2811077773
#  -----------------------------------------------------------------------------
