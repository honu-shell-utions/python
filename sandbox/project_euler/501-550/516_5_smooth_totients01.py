#  -----------------------------------------------------------------------------
#  5-smooth totients
#  Problem 516
#  https://projecteuler.net/problem=516
#  -----------------------------------------------------------------------------
from sympy.ntheory.factor_ import totient
from sympy import isprime
from math import log
#  -----------------------------------------------------------------------------
def make_hammings(L):
    pwrs2 = [2**k for k in range(int(log(L, 2))+1)]
    pwrs3 = [3**k for k in range(int(log(L, 3))+1)]
    pwrs5 = [5**k for k in range(int(log(L, 5))+1)]
    hamming = [a*b*c for a in pwrs2 for b in pwrs3 for c in pwrs5 if a*b*c < L]
    return hamming
#  -----------------------------------------------------------------------------
def make_primes(hams,L):
    primes = []
    hams = make_hammings(L)
    for h in hams:
        if isprime(h+1) and h + 1 > 5:
            primes.append(h+1)
    return primes
#  -----------------------------------------------------------------------------
def S(L):
    hams = make_hammings(L)
    sum_total = 0
    for n in range(1,L+1):
        if totient(n) in hams:
            sum_total += n
    return sum_total
#  -----------------------------------------------------------------------------
hams = make_hammings(10**12)
primes = make_primes(hams,10**12)
#print(S(100))
#  -----------------------------------------------------------------------------
#  solution: 939087315
#  -----------------------------------------------------------------------------
