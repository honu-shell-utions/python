#  -----------------------------------------------------------------------------
#  Square on the Inside
#  Problem 504
#  https://projecteuler.net/problem=504
#  -----------------------------------------------------------------------------
from math import sqrt
from time import time
#  -----------------------------------------------------------------------------
def f1(x,a,b,c,d):
    return -b*x/a + b
#  -----------------------------------------------------------------------------
def f2(x,a,b,c,d):
    return b*x/c + b
#  -----------------------------------------------------------------------------
def f3(x,a,b,c,d):
    return -d*x/c - d
#  -----------------------------------------------------------------------------
def f4(x,a,b,c,d):
    return d*x/a - d
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
def lattice_points(a,b,c,d):
    interior_pts = 0
    for x in range(-c+1,a):
        for y in range(-d+1,b):
            if y < f1(x,a,b,c,d) and y < f2(x,a,b,c,d) and\
               y > f3(x,a,b,c,d) and y > f4(x,a,b,c,d):
                interior_pts += 1
    return interior_pts
#  -----------------------------------------------------------------------------
def num_lattice_points(quads):
    count = 0
    for q in quads:
        temp = lattice_points(*q)
        if sqrt(temp) == int(sqrt(temp)):
            count += 1
    return count
#  -----------------------------------------------------------------------------
for n in [4,8,20]:
    start = time()
    quads = get_quads(n)
    num_points = num_lattice_points(quads)
    print(f'Solution for n = {n}: {num_points}, Run-Time: {time()-start}')
#  -----------------------------------------------------------------------------
#  solution: 694687
#  -----------------------------------------------------------------------------
