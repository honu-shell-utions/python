#  -----------------------------------------------------------------------------
#  Strong Achilles Numbers
#  Problem 302
#  https://projecteuler.net/problem=302
#  -----------------------------------------------------------------------------
from sympy import factorint
from sympy.ntheory.factor_ import totient
from math import log
from time import time
#  -----------------------------------------------------------------------------
def is_powerful(n):
    return min(factorint(n).values()) >= 2
#  -----------------------------------------------------------------------------
def is_perfect_power(n):
    for base in range(2,n):
        exp = round(log(n,base),8)
        if int(exp) == exp:
            return True
    return False
#  -----------------------------------------------------------------------------
def is_achilles(n):
    return is_powerful(n) and not is_perfect_power(n)
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
for exp in range(2,9):
    limit = 10**exp
    start = time()
    print(f'Solutiion for n = 10^{exp}: {euler_302(limit):9}, Run-Time: {time()-start}')
#  -----------------------------------------------------------------------------
#  solution: 1170060
#  -----------------------------------------------------------------------------
