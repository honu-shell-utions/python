"""
835_supernatural_triangles.py
https://projecteuler.net/problem=835

Supernatural Triangles
A Pythagorean triangle is called supernatural if two of its three sides are
consecutive integers.

Let S(N) be the sum of the perimeters of all distinct supernatural triangles
with perimeters less than or equal to N.
For example, S(100) = 258 and S(10000) = 172004.

Find S(10^10^10). Give your answer modulo 1234567891
==============================================================================
"""
#  -----------------------------------------------------------------------------
from math import gcd
#  -----------------------------------------------------------------------------
def gen_trips(k):
    n,m = 1,2
    while m*m+1 < k:                # while z<k (for largest m producing z)
        if n >= m:
            n,m = m%2,m+1           # n reached m, advance m, reset n
        z = m*m+n*n                 # compute z 
        if z >= k:
            n = m
            continue                # skip remaining n when z >= k
        if gcd(n,m) == 1:           # trigger on coprimes
            yield m*m-n*n,2*m*n,z   # return x,y,z triple
        n += 2                      # advance n, odds with evens
#  -----------------------------------------------------------------------------
def is_super(A,B,C):
    return abs(A-B) == 1 or abs(A-C) == 1 or abs(B-C) == 1
#  -----------------------------------------------------------------------------
MOD = 1234567891
N = 10**4
for exp in range(2,11):
    N = 10**exp
    prims = gen_trips(N)
    total = 0
    while True:
        try:
            A,B,C = next(prims)
            if A + B + C > N:
                break
            if is_super(A,B,C):
                total += A + B + C
                #total %= MOD
        except:
            break
    print(exp,total)

#  -----------------------------------------------------------------------------
#  solution: 1050923942
#  -----------------------------------------------------------------------------

