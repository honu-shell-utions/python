#  -----------------------------------------------------------------------------
#  Panaitopol Primes
#  Problem 291
#  https://projecteuler.net/problem=291
#  -----------------------------------------------------------------------------
from sympy import isprime
from time import time
#  -----------------------------------------------------------------------------
def count_pana(limit):
    primes = 0
    for n in range(1,limit+1):
        p = n**2 + (n+1)**2
        if p >= limit:
            return primes
        if isprime(p):
            primes += 1         
#  -----------------------------------------------------------------------------
for exp in [3,6,9,12,15]:
    start = time()
    limit = 5*10**exp
    result = count_pana(limit)
    print(f'Solution for n = 5*10^{exp:<2} = {result:8}, Run-Time: {time()-start}')
#  -----------------------------------------------------------------------------
#  solution: 4037526
#  -----------------------------------------------------------------------------
