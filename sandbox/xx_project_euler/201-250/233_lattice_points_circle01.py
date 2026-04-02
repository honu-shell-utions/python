#-------------------------------------------------------------------------------
# 233_lattice_points_circle.py
#
# Lattice points on a circle
# Let f(N) be the number of points with integer coordinates that are on a
# circle passing through (0, 0), (N, 0),(0, N), and (N, N).
#
# It can be shown that f(10_000) = 36.
#
# What is the sum of all positive integers N ≤ 10**11 such that f(N) = 420?
#
# https://oeis.org/search?q=lattice+points+on+a+circle&sort=&language=&go=Search
#-------------------------------------------------------------------------------
from sympy import factorint
from time import time
#-------------------------------------------------------------------------------
def N(n):
    if n <= 0:
        return 0
    r = 1
    for p, e in factorint(n).items():
        if p % 4 == 1:
            r *= 2*e + 1
    return 4*r
#-------------------------------------------------------------------------------
start = time()
limit = 10**11
first_n_giving_420 = 359125
sum_of = 0
for n in range(first_n_giving_420,limit+1):
    result = N(n)
    if result == 420:
        sum_of += n       
print(f'Solution: {sum_of}, Run-Time: {time()-start}')
#-------------------------------------------------------------------------------
# solution: 271204031455541309
#-------------------------------------------------------------------------------
