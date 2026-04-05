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
#  -----------------------------------------------------------------------------
from math import floor, sqrt
from time import time
#  -----------------------------------------------------------------------------
def compute(u,v,k,N):
    ans = 0
    while u <= 2 * N:
        if v % 2 == k % 2 and v > k:
            ans += 1
        u, v = u * 2 + v * 3, u * 1 + v * 2
    return ans
#  -----------------------------------------------------------------------------
def euler_582(N):
    total = 0
    for k in range(1, 101):
        for u in range(1, k * 2 + 1, 1):
            if u <= k:
                continue
            v = floor(sqrt((1. * u * u - 1. * k * k) / 3))
            if u * u == 3 * v * v + k * k:
                total += compute(u,v,k,N)
    return total
#  -----------------------------------------------------------------------------
for exp in range(3,101):
    start = time()
    N = 10**exp
    print(f'Solution for N = 10^{exp:3}: {euler_582(N):6}, Run-Time: {time()-start:.3f}')
#  -----------------------------------------------------------------------------
#  solution: 19903
#  -----------------------------------------------------------------------------

