"""
264_triangle_centers.py
https://projecteuler.net/problem=264

Triangle Centers
Consider all the triangles having:
    • All their vertices on lattice points.
    • Circum-center at the origin O.
    • Ortho-center at the point H(5, 0).

There are nine such triangles having a perimeter ≤ 50.
Listed and shown in ascending order of their perimeter, they are:
see pdf for pictures/graphs
A(-4, 3), B(5, 0), C(4, -3)
A(4, 3), B(5, 0), C(-4, -3)
A(-3, 4), B(5, 0), C(3, -4)

A(3, 4), B(5, 0), C(-3, -4)
A(0, 5), B(5, 0), C(0, -5)
A(1, 8), B(8, -1), C(-4, -7)

A(8, 1), B(1, -8), C(-4, 7)
A(2, 9), B(9, -2), C(-6, -7)
A(9, 2), B(2, -9), C(-6, 7)

The sum of their perimeters, rounded to four decimal places, is 291.0089.

Find all such triangles with a perimeter ≤ 10^5. Enter as your answer the sum
of their perimeters rounded to four decimal places.

==============================================================================
page 6
difficulty 85%
pe_ans = 2816417.1055
"""
#  -----------------------------------------------------------------------------
from math import sqrt,isqrt
from time import time
#  -----------------------------------------------------------------------------
def solve(x, y):
    a = 4*((x-k)**2+y**2)
    if a == 0:
        return
    b = y*a
    c = y**4-((x+k)*(3*x-k)+2*y**2)*(x-k)**2
    d = b**2-4*a*c
    if d >= 0:
        dd = isqrt(d)
        if dd ** 2 == d:
            r = x**2+y**2
            def test(x1,y1):
                x2,y2 = k-x-x1,-y-y1
                if x2**2+y2**2 == r and (x1 != x or y1 != y) and (x2 != x or y2 != y) \
                   and (x2 != x1 or y2 != y1):
                    return x,y,x1,y1,x2,y2
                return None
            if (-b+dd) % (2*a) == 0:
                y1 = (-b+dd) // (2*a)
                xx1 = x**2+y**2-y1**2
                if xx1 >= 0:
                    x1 = isqrt(xx1)
                    if x1 ** 2 == xx1:
                        t = test(x1,y1)
                        if t:
                            yield t
                        if dd != 0:
                            t = test(-x1,y1)
                            if t:
                                yield t
#  -----------------------------------------------------------------------------
def d(a,b):
    return sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)
#  -----------------------------------------------------------------------------
def p(t):
    return d(t[0:2],t[2:4]) + d(t[2:4],t[4:6]) + d(t[4:6],t[0:2])
#  -----------------------------------------------------------------------------
def test(tt):
    global tr
    global s
    ttt = frozenset(tt)
    if ttt not in tr:
        tr.add(ttt)
        s += pp
#  -----------------------------------------------------------------------------
start = time()
k = 5
pmax = 10 ** 5
tr = set()
s = 0

for xy in range(pmax // 3):
    for x in range(xy + 1):
        for t in solve(x, xy - x):
            pp = p(t)
            if pp <= pmax:
                test(((t[0], t[1]), (t[2], t[3]), (t[4], t[5])))
                test(((t[0], -t[1]), (t[2], -t[3]), (t[4], -t[5])))

print(f'Solution: {round(s,4)}, Run-Time: {time()-start:.3f}')
#  -----------------------------------------------------------------------------
