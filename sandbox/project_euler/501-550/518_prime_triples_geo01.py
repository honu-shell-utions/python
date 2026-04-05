#  -----------------------------------------------------------------------------
#  Prime triples and geometric sequences
#  Problem 518
#  https://projecteuler.net/problem=518
#  -----------------------------------------------------------------------------
from sympy import primerange
from itertools import combinations
from time import time
#  -----------------------------------------------------------------------------
def make_trips(primes):
    combos = combinations(primes,3)
    return combos
#  -----------------------------------------------------------------------------
def is_geo(a,b,c):
    if (b+1)**2 == (a+1)*(c+1):
        return True
    else:
        return False
#  -----------------------------------------------------------------------------
for exp in range(2,6):
    start = time()
    n = 10**exp
    total = 0
    primes = list(primerange(2,n))
    combos = make_trips(primes)
    for combo in combos:
        if is_geo(*combo):
            total += sum(combo)
    print(f'Solution for n = 10^{exp} = {total:16}, Run-Time: {time()-start}')
#  -----------------------------------------------------------------------------
#  solution: 100315739184392
#  -----------------------------------------------------------------------------
