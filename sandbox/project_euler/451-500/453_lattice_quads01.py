#  -----------------------------------------------------------------------------
#  Lattice Quadrilaterals
#  Problem 453
#  https://projecteuler.net/problem=453
#  -----------------------------------------------------------------------------
from itertools import combinations, permutations
#  -----------------------------------------------------------------------------
def make_coords(m,n):
    coords = []
    for i in range(m+1):
        for j in range(n+1):
            coords.append((i,j))
    combos = permutations(coords,4)
    return combos
#  -----------------------------------------------------------------------------
def collinear(c):
    combos = combinations(c,3)
    for c in combos:
        (x1,y1),(x2,y2),(x3,y3) = c
        area = x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)
        if area == 0:
            return True
    return False
#  -----------------------------------------------------------------------------
def ccw(A,B,C):
    x0,y0 = A
    x1,y1 = B
    x2,y2 = C
    return (y2-y0)*(x1-x0) > (y1-y0)*(x2-x0)
#  -----------------------------------------------------------------------------
def intersect(A,B,C,D):
    return ccw(A,C,D) != ccw(B,C,D) and ccw(A,B,C) != ccw(A,B,D)
#  -----------------------------------------------------------------------------
def tidy_combos(combos):
    clean = []
    for c in combos:
        A,B,C,D = c
        if collinear(c) or intersect(A,B,C,D) or intersect(B,C,D,A):
            continue
        clean.append(c)
    return clean
#  -----------------------------------------------------------------------------
for m,n in [(2,2),(3,7),(12,3),(123,45)]:
    combos = tidy_combos(make_coords(m,n))
    print(f'For (m,n) = ({m:2},{n:2}): {len(list(combos))//8:10}')
#  -----------------------------------------------------------------------------
#  solution: 104354107 
#  -----------------------------------------------------------------------------
