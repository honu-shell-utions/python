"""
582_nearly_isosceles_120_degree_triangles.py
https://projecteuler.net/problem=582

Nearly Isosceles 120 Degree Triangles
    Let a, b and c be the sides of an integer sided triangle with one angle of
    120 degrees, a ≤ b ≤ c and b-a ≤ 100.

    Let T(n) be the number of such triangles with c ≤ n.

    T(1000) = 235 and T(10^8) = 1245

    Find T(10^100)
==============================================================================
page 12
difficulty 50%
pe_ans = 19903
==============================================================================

"""
from sympy.solvers.diophantine.diophantine import diop_DN
from sympy import gcd
from math import sqrt
from time import time
#  -----------------------------------------------------------------------------
def solve(d):
    tc = 0
    # (r,s) = solution to x^2 + 3y^2 = 1
    r = 2
    s = 1
    D = 3
    a = diop_DN (D,d*d)
    for (p,q) in a:
        x1 = p
        # can get negative values from diop_DN
        while abs(x1) < N:
            x1,y1  = p*r + D*q*s, p*s + q*r
            a1,b1  = y1 - d, y1 + d
            g = gcd(a1,b1)
            a1, b1 = abs(a1//g), abs(b1//g)
            a1, b1 = min(a1,b1), max(a1,b1)
            if abs(b1 - a1) == d:
                c = int (sqrt(a1*a1 + b1*b1 + a1*b1))
                if  c < N:
                    cnt = min(100//d, N//c)
                    tc += cnt
            p,q = x1, y1
    return tc
#  -----------------------------------------------------------------------------
for exp in [3,8,100]:
    start = time()
    total = 0
    N = 10**exp
    for d in range (1,101):
        total += solve(d)
    print(f'Solution for N = 10^{exp:4}: {total:6}, Run-Time: {time()-start:.3f}')
#  -----------------------------------------------------------------------------
