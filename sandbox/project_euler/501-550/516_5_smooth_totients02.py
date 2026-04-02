#  -----------------------------------------------------------------------------
#  5-smooth totients
#  Problem 516
#  https://projecteuler.net/problem=516
#  -----------------------------------------------------------------------------
from sympy.ntheory.factor_ import totient
from sympy import isprime
from math import log
from time import time
#  -----------------------------------------------------------------------------
def make_hammings(L):
    pwrs2 = [2**k for k in range(int(log(L, 2))+1)]
    pwrs3 = [3**k for k in range(int(log(L, 3))+1)]
    pwrs5 = [5**k for k in range(int(log(L, 5))+1)]
    hamming = [a*b*c for a in pwrs2 for b in pwrs3 for c in pwrs5 if a*b*c <= L]
    return sorted(hamming)
#  -----------------------------------------------------------------------------
def make_primes(hams,L):
    primes = []
    for h in hams:
        if isprime(h+1) and h + 1 > 5:
            primes.append(h+1)
    return primes
#  -----------------------------------------------------------------------------
def S(hams,primes,L):
    for p in primes:
        for h in hams:
            if h * p > L:
                break
            hams.append(h * p)
        hams = sorted(hams)
    return sum(hams)
#  -----------------------------------------------------------------------------
start = time()
limit = 10**12
hams = make_hammings(limit)
primes = make_primes(hams,limit)
print(f'Solution: {S(hams,primes,limit) % 2**32}, Run-Time: {time()-start}')
#  -----------------------------------------------------------------------------
#  solution: 939087315
#  -----------------------------------------------------------------------------
