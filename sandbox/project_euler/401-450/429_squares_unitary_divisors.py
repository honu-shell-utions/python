#  -----------------------------------------------------------------------------
#  Sum of squares of unitary divisors
#  Problem 429
#  https://projecteuler.net/problem=429
#  -----------------------------------------------------------------------------
from math import log, floor
from sympy import primerange
from time import time
#  -----------------------------------------------------------------------------
def S(n):
    sum_squares = 1
    for p in primerange(2,n):
        exp = 2*legendre(p,n)
        sum_squares = (sum_squares*(pow(p,exp,MOD)+1)) % MOD
    return sum_squares
#  -----------------------------------------------------------------------------
def legendre(p,n):
    total = 0
    for i in range(1,floor(log(n,p))+1):
        total += floor(n/p**i)
    return total   
#  -----------------------------------------------------------------------------
MOD = 10**9 + 9
for limit in [4,10,10**3,10**6,10**8]:
    start = time()
    print(f'Solution for N = {limit}: {S(limit)% MOD}, Run-Time: {time()-start}')
#  -----------------------------------------------------------------------------
#  solution: 98792821
#  -----------------------------------------------------------------------------
