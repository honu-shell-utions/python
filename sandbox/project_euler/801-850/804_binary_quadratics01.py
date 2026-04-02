#  -----------------------------------------------------------------------------
## Counting Binary Quadratic Representations
## Problem 804
## https://projecteuler.net/problem=804
#  -----------------------------------------------------------------------------
from math import isqrt
from time import time
#  -----------------------------------------------------------------------------
def f(n): 
    counter = 2*isqrt(n)
    for z in range(1, n+1):
        desc = 4*n-163*z*z
        if desc < 0: 
            break
        upper = (-z+isqrt(desc))//2
        lower = -z-upper
        counter+=(upper-lower+1)*2
    return counter
#  -----------------------------------------------------------------------------
for exp in range(1,17):
    start = time()
    solution = f(10**exp)
    print(f'Solution for n = 10^{exp:2}: {solution}, Run-Time: {round(time()-start,6)}')
#  -----------------------------------------------------------------------------
#  solution: 4921370551019052
#  -----------------------------------------------------------------------------
