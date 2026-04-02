#  -----------------------------------------------------------------------------
#  Square on the Inside
#  Problem 504
#  https://projecteuler.net/problem=504
#  -----------------------------------------------------------------------------
from math import sqrt, gcd
from time import time
#  -----------------------------------------------------------------------------
def get_quads(m):
    quads = []
    for a in range(1,m+1):
        for b in range(1,m+1):
            for c in range(1,m+1):
                for d in range(1,m+1):
                    quads.append((a,b,c,d))
    return quads
#  -----------------------------------------------------------------------------
def picks_theorem(a,b,c,d):
    area = 0.5 * (a + c) * (b + d)
    boundary = gcd(a, b) + gcd(a, d) + gcd(c, b) + gcd(c, d)
    return 1 + area - boundary * 0.5
#  -----------------------------------------------------------------------------
def num_lattice_points(quads):
    count = 0
    for q in quads:
        temp = picks_theorem(*q)
        if sqrt(temp) == int(sqrt(temp)):
            count += 1
    return count
#  -----------------------------------------------------------------------------
for n in range(4,101,16):
    start = time()
    quads = get_quads(n)
    num_points = num_lattice_points(quads)
    print(f'Solution for n = {n:3} --> {num_points:7}, \tRun-Time: {time()-start}')
#  -----------------------------------------------------------------------------
#  solution: 694687
#  -----------------------------------------------------------------------------
