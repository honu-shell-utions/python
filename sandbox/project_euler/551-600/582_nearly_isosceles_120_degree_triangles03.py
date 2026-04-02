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
from math import sqrt
from math import ceil
from time import time
#  -----------------------------------------------------------------------------
def euler_582(LIMIT):
    num = 0
    for i in range (1,101):
        u=-3*i*i
        sol=[]
        L1 = ceil(sqrt(-u/12))
        L2 = int(sqrt(-u/3))
        for y in range (L1,L2+1):
            t = 12*y*y+u
            t1 = int(sqrt(t))
            if t1*t1 == t:
                sol.append([t1,y])
                if t1!=0:
                    sol.append([-t1,y])
        ss = set()
        for j in range (len(sol)):
            x,y=sol[j][0],sol[j][1]
            while y <= LIMIT:
                if x > 3*i and ((x,y) not in ss):
                    num+=1
                    ss.add((x,y))
                x,y = 7*x+24*y,2*x+7*y
    return num
#  -----------------------------------------------------------------------------
for exp in range(3,101):
    start = time()
    N = 10**exp
    print(f'Solution for N = 10^{exp:3}: {euler_582(N):6}, Run-Time: {time()-start:.3f}')
#  -----------------------------------------------------------------------------
#  solution: 19903
#  -----------------------------------------------------------------------------

