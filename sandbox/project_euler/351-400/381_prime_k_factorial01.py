#  -----------------------------------------------------------------------------
#  (prime-k) factorial
#  Problem 381
#  https://projecteuler.net/problem=381
#  -----------------------------------------------------------------------------
from math import factorial
from sympy import primerange
from time import time
#  -----------------------------------------------------------------------------
def S(p):
    total = 0
    for k in range(1,6):
        total += factorial(p-k)
    return total % p
#  -----------------------------------------------------------------------------
for exp in [2,4,6,8]:
    start = time()
    primes = primerange(5,10**exp+1)
    total = 0
    for p in primes:
        total += S(p)
    print(f'Solution for limit = 10^{exp}: {total}, Run-Time: {time()-start}')
#  -----------------------------------------------------------------------------
#  solution: 139602943319822
#  -----------------------------------------------------------------------------
