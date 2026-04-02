#  -----------------------------------------------------------------------------
#  2-Friendly
#  Problem 643
#  https://projecteuler.net/problem=643
#  -----------------------------------------------------------------------------
from math import log2, floor
from time import time
from sympy.ntheory.factor_ import totient
from functools import lru_cache
#  -----------------------------------------------------------------------------
@lru_cache(maxsize=None)
def A002088(n): # based on second formula in A018805
    if n == 0:
        return 0
    c, j = 0, 2
    k1 = n//j
    while k1 > 1:
        j2 = n//k1 + 1
        c += (j2-j)*(2*A002088(k1)-1)
        j, k1 = j2, n//j2
    return (n*(n-1)-c+j)//2
#  -----------------------------------------------------------------------------
MOD = 10**9 + 7
for exp in range(1,12,2):
    start = time()
    total = 0
    LIMIT = 10**exp
    for k in range(1,floor(log2(LIMIT))):
        total = (total + A002088(floor(LIMIT/2**k)) - 1) % MOD
    print(f'Solution for N = 10^{exp:2} --> {total:10}, Run-Time: {time()-start}')
#  -----------------------------------------------------------------------------
#  solution: 968274154
#  -----------------------------------------------------------------------------
