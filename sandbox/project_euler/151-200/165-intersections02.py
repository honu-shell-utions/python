# p165_intersections.py
#
# A segment is uniquely defined by its two endpoints.
# By considering two line segments in plane geometry there are three
# possibilities: the segments have zero points, one point, or infinitely many
# points in common.
#
# Moreover when two segments have exactly one point in common it might be the
# case that that common point is an endpoint of either one of the segments or
# of both. If a common point of two segments is not an endpoint of either of
# the segments it is an interior point of both segments.
#
# We will call a common point T of two segments L1 and L2 a true intersection
# point of L1 and L2 if T is the only common point of L1 and L2 and T is an
# interior point of both segments.
#
# Consider the three segments L1, L2, and L3:
# L1: (27, 44) to (12, 32)
# L2: (46, 53) to (17, 62)
# L3: (46, 70) to (22, 40)
#
# It can be verified that line segments L2 and L3 have a true intersection
# point. We note that as the one of the end points of L3: (22,40) lies on L1
# this is not considered to be a true point of intersection. L1 and L2 have
# no common point. So among the three line segments, we find one true
# intersection point.
#
# Now let us do the same for 5_000 line segments. To this end, we generate
# 20_000 numbers using the so-called "Blum Blum Shub" pseudo-random number
# generator.
#
# To create each line segment, we use four consecutive numbers tn. That is,
# the first line segment is given by:
#
# (t1, t2) to (t3, t4)
#
# The first four numbers computed according to the above generator should be:
# 27, 144, 12 and 232. The first segment would thus be (27, 144) to (12, 232).
#
# How many distinct true intersection points are found among the
# 5_000 line segments?
# -----------------------------------------------------------------------------
from time import time
from fractions import Fraction
# -----------------------------------------------------------------------------
go = time()
d_chk = {500: 29496, 700: 57909, 5_000: 2868868}

def blum_blum_shub(n):
    s = [290797]
    t = []
    tnum = n * 4
    for i in range(0, tnum):
        s.append((s[-1]*s[-1]) % 50515093)
        t.append(s[-1] % 500)

    lst_endpoints = []
    for j in range(0,tnum,4):
        lst_endpoints.append((t[j],t[j+1],t[j+2],t[j+3]))
    return lst_endpoints
# -----------------------------------------------------------------------------
def intersect(x1,y1, x2,y2, x3,y3, x4,y4):
    # check to be sure all the endpoints are unique
    if (x1, y1) == (x2, y2): return None
    if (x1, y1) == (x3, y3): return None
    if (x1, y1) == (x4, y4): return None
    if (x2, y2) == (x3, y3): return None
    if (x2, y2) == (x4, y4): return None
    if (x3, y3) == (x4, y4): return None

    # algebra to put the line into standard form Ax + By = C
    A1 = y1-y2
    B1 = x2-x1
    C1 = x2*y1-x1*y2
    A2 = y3-y4
    B2 = x4-x3
    C2 = x4*y3-x3*y4
    denom = A1*B2 - A2*B1  # zero denominator indicates parallel or the same line
    if denom == 0:
        return None
    x = Fraction(B2*C1 - B1*C2,denom)
    y = Fraction(A2*C1 - A1*C2,-denom)

    # check the intersection point is NOT the same as an endpoint
    if (x, y) == (x1, y1): return None
    if (x, y) == (x2, y2): return None
    if (x, y) == (x3, y3): return None
    if (x, y) == (x4, y4): return None

    # check the 'box' made with endpoints to be sure the intersection point
    # is inside the 'box'
    if x < min(x1, x2): return None
    if x < min(x3, x4): return None
    if x > max(x1, x2): return None
    if x > max(x3, x4): return None
    if y < min(y1, y2): return None
    if y < min(y3, y4): return None
    if y > max(y1, y2): return None
    if y > max(y3, y4): return None

    st_intersections.add((x,y))
    return True
# -----------------------------------------------------------------------------
print('number of line segments  number of intersections  verify  runtime') 
for k in d_chk.keys():
    t0 = time()
    end_points = blum_blum_shub(k)
    st_intersections = set()
    for x1, y1, x2, y2 in end_points:
        for x3, y3, x4, y4 in end_points:
           intersect(x1, y1, x2, y2, x3, y3, x4, y4)
    ans = len(st_intersections)
    print(f'{k:>23,}  {ans:>23,}    {ans == d_chk[k]}  {round(time()-t0,3)}')

rt = time()-go
m, s = divmod(rt, 60)
print()
print(f'total runtime: ~ {int(m)}-minutes {round(s)} seconds')
# -----------------------------------------------------------------------------
