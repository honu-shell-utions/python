#  -----------------------------------------------------------------------------
#  Fermat Equation
#  Problem 753
#  https://projecteuler.net/problem=753
#  -----------------------------------------------------------------------------
from sympy import primerange
from time import time
#  -----------------------------------------------------------------------------
def get_primes(n):
    return list(primerange(2,n+1))
#  -----------------------------------------------------------------------------
def F(p):
    if p == 3:
        return 2
    if p % 3 == 2:
        return (p-1)*(p-2)
    hits = 0
    for a in range(1,p):
        for b in range(1,p):
            for c in range(1,p):
                if (a**3 + b**3) % p == c**3 % p:
                    hits += 1
    return hits
#  -----------------------------------------------------------------------------
for LIMIT in [5,7,10**2,10**3,10**4,6*10**6]:
    start = time()
    total = 0
    for p in get_primes(LIMIT):
        total += F(p)
    print(f'Solution for n = {LIMIT:7}: {total:20}, Run-Time: {time()-start:.3f}')
#  -----------------------------------------------------------------------------
#  solution: 4714126766770661630
#  -----------------------------------------------------------------------------
