#  -----------------------------------------------------------------------------
import itertools
from sympy import primerange
from time import time
#  -----------------------------------------------------------------------------
def factorize(M, s):
    f = [[] for _ in range(M)]
    for p in s:
        for x in range(p, M, p):
            f[x] += [p]
    return f
#  -----------------------------------------------------------------------------
def product(l):
    out = 1
    for x in l:
        out *= x
    return out
#  -----------------------------------------------------------------------------
# coprime to k less than m
def count_coprime(k, m, f):
    total = 0
    for i in range (1, len(f)+1):
        prefactor = (-1)**(i+1)
        for x in itertools.combinations(f, i):
            total += prefactor*(m//product(x))
    return m - total
#  -----------------------------------------------------------------------------
def count_triples(M, f):
    total = 0
    for i in range (2, int((M)**0.5) + 1, 2):
        total += count_coprime (i, int((M - i*i)**0.5), f[i])
    return total
#  -----------------------------------------------------------------------------
for M0 in [20,10**6,10**8,3141592653589793]:
    start = time()
    M = int(M0**0.5)+1
    s = primerange(2,M)
    f = factorize(M, s)
    print(f'Solution for n = {M0}: {count_triples(M0,f)}, Run-Time: {time()-start}')
#  -----------------------------------------------------------------------------
