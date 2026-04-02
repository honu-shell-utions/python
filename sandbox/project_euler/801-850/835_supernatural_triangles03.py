"""
835_supernatural_triangles.py
https://projecteuler.net/problem=835

Supernatural Triangles
A Pythagorean triangle is called supernatural if two of its three sides are
consecutive integers.

Let S(N) be the sum of the perimeters of all distinct supernatural triangles
with perimeters less than or equal to N.
For example, S(100) = 258 and S(10000) = 172004.

Find S(10^10^10). Give your answer MODulo 1234567891
==============================================================================
"""
#  -----------------------------------------------------------------------------
from math import sqrt
from time import time
#  -----------------------------------------------------------------------------
def f01(N):
    per_set = set()
    for x in range(1,10**100):
        y = sqrt(x**2 + (x+1)**2)
        if y != int(y):
            continue
        if 2*x + 1 + y > N:
            break
        per_set.add((x,x+1,int(y),int(2*x+1+y)))
    return per_set
#  -----------------------------------------------------------------------------
def f02(N):
    per_set = set()
    for x in range(1,10**100):
        y = sqrt((x+1)**2 - x**2)
        if y != int(y):
            continue
        if 2*x + 1 + y > N:
            break
        per_set.add((min(x,int(y)),max(x,int(y)),x+1,int(2*x+1+y)))
    return per_set
#  -----------------------------------------------------------------------------
def euler_835(N):
    return f01(N).union(f02(N))
#  -----------------------------------------------------------------------------
MOD = 1234567891
for exp in range(2,11):
    start = time()
    N = 10**exp
    res = euler_835(N)
    total = 0
    for x,y,z,p in res:
        total += p
        total %= MOD
    print(f'Solution for N = 10^{exp:2}: {total:11}, Run-Time: {time()-start:0.3f}')    
#  -----------------------------------------------------------------------------
#  solution: 1050923942
#  -----------------------------------------------------------------------------

