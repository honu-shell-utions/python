#  -----------------------------------------------------------------------------
#  Prime generating integers
#  Problem 357
#  Consider the divisors of 30: 1,2,3,5,6,10,15,30.
#  It can be seen that for every divisor d of 30, d+30/d is prime.
#  
#  Find the sum of all positive integers n not exceeding 100 000 000
#  such that for every divisor d of n, d+n/d is prime.
#  -----------------------------------------------------------------------------
from time import time
from sympy import divisors, isprime, primerange
#  -----------------------------------------------------------------------------
def all_good(n):
    if not isprime(n+1):
        return False
    if not isprime(2 + n//2):
        return False
    divs = divisors(n)
    divs = divs[:len(divs)//2]
    for d in divs:
        if not isprime(d + n//d):
            return False
    return True
#  -----------------------------------------------------------------------------
start = time()
total = 1
primes = primerange(3,10**8)
for p in primes:
    if p % 4 != 3:
        continue
    n = p - 1
    if all_good(n):
        total += n

print(f'Solution: {total}, Run-Time: {time()-start}')
#  -----------------------------------------------------------------------------
#  solution: 1739023853137
#  -----------------------------------------------------------------------------

