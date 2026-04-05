#  -----------------------------------------------------------------------------
#  Strong Achilles Numbers
#  Problem 302
#  https://projecteuler.net/problem=302
#  -----------------------------------------------------------------------------
from sympy import factorint
from sympy.ntheory.factor_ import totient
from math import gcd
from time import time
#  -----------------------------------------------------------------------------
def is_achilles(n):
    fact_int = factorint(n).values()
    return min(fact_int) >= 2 and gcd(*fact_int) == 1
#  -----------------------------------------------------------------------------
def is_strong_achilles(n):
    if is_achilles(n) and is_achilles(totient(n)):
        return True
#  -----------------------------------------------------------------------------
def euler_302(limit):
    count = 0
    for n in range(2,limit):
        if is_strong_achilles(n):
            count += 1
    return count
#  -----------------------------------------------------------------------------
for exp in range(2,19):
    start = time()
    limit = 10**exp
    print(f'Solutiion for n = 10^{exp:<2}: {euler_302(limit):9}, Run-Time: {round(time()-start,3)}')
#  -----------------------------------------------------------------------------
#  solution: 1170060
#  -----------------------------------------------------------------------------
