#  -----------------------------------------------------------------------------
#  Strong Achilles Numbers
#  Problem 302
#  https://projecteuler.net/problem=302
#  -----------------------------------------------------------------------------
from numpy import gcd, floor
from sympy import factorint
from sympy.ntheory import totient
from time import time
from functools import reduce

def euler_302(limit):
    # generate achilles numbers
    achs = set()
    for a in range(2, int(floor(limit**(1/2))+1)):
        for b in range(2, int(floor((limit / (a**2)) ** (1/3))+1)):
            n = (a**2) * (b**3)
            if reduce(gcd,factorint(n).values()) == 1:
                achs.add(n)
    # count strong achilles numbers
    count = 0
    for ach in achs:
        if totient(ach) in achs:
            count += 1
    return(count)
#  -----------------------------------------------------------------------------
for exp in range(4,19):
    start = time()
    limit = 10**exp
    print(f'Solutiion for n = 10^{exp:<2}: {euler_302(limit):9},\
 Run-Time: {round(time()-start,3)} seconds')
#  -----------------------------------------------------------------------------
#  solution: 1170060
#  -----------------------------------------------------------------------------
