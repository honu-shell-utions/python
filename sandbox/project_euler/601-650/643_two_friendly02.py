#  -----------------------------------------------------------------------------
#  2-Friendly
#  Problem 643
#  https://projecteuler.net/problem=643
#  -----------------------------------------------------------------------------
from math import log2, floor
from time import time
from sympy.ntheory.factor_ import totient
#  -----------------------------------------------------------------------------
def totient_sum(n):
    sum_tots = 0
    for j in range(1,n+1):
        sum_tots += totient(j)
    return sum_tots
#  -----------------------------------------------------------------------------
MOD = 10**9 + 7
for exp in range(1,12,2):
    start = time()
    total = 0
    LIMIT = 10**exp
    for k in range(1,floor(log2(LIMIT))):
        total = (total + totient_sum(floor(LIMIT/2**k)) - 1) % MOD
    print(f'Solution for N = 10^{exp} --> {total:10}, Run-Time: {time()-start}')
#  -----------------------------------------------------------------------------
#  solution: 968274154
#  -----------------------------------------------------------------------------
