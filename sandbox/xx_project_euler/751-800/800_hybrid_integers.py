#  -----------------------------------------------------------------------------
## Hybrid Integers
## Problem 800
## https://projecteuler.net/problem=800
#  -----------------------------------------------------------------------------
from sympy import primerange
from math import log2
from time import time
#  -----------------------------------------------------------------------------
def C(N):
    NLOG = N*log2(N)
    primes = list(primerange(2,int(NLOG-2)))
    r = 0
    j_max = len(primes)-1
    for i in range ((len(primes))//2):
        p = primes[i]
        for j in range(j_max, i, -1):
            q = primes[j]
            if p*log2(q)+q*log2(p) <= NLOG:
                r += j-i
                j_max = j
                break
    return r
#  -----------------------------------------------------------------------------
for N in [100,200,300,400,500,600,700,800,800800]:
    start = time()
    print(f'Solution for N = {N}: {C(N)}, Run-Time: {time()-start}')

#  -----------------------------------------------------------------------------
#  solution:  1412403576
#  -----------------------------------------------------------------------------
