# -----------------------------------------------------------------------------
# Triangles containing the origin II
# Problem 456
# https://projecteuler.net/problem=456
# -----------------------------------------------------------------------------
from time import time
# -----------------------------------------------------------------------------
def gen_coords(n):
    coord_list = []
    for k in range(1,n+1):
        x = (1248**k % 32323) - 16161
        y = (8421**k % 30103) - 15051
        coord_list.append((x,y))
    return coord_list
# -----------------------------------------------------------------------------
def area(x1, y1, x2, y2, x3, y3):
	return abs((x1 * (y2 - y3) + x2 * (y3 - y1)
				+ x3 * (y1 - y2)) / 2.0)
# -----------------------------------------------------------------------------
def contains_origin(v1,v2,v3):
    x1,y1 = v1
    x2,y2 = v2
    x3,y3 = v3

    # Calculate area of triangle 
    A = area (x1, y1, x2, y2, x3, y3)
    # Calculate area of triangle PBC
    A1 = area (0, 0, x2, y2, x3, y3)
    # Calculate area of triangle PAC
    A2 = area (x1, y1, 0, 0, x3, y3)
    # Calculate area of triangle PAB
    A3 = area (x1, y1, x2, y2, 0, 0)	
    # Check if sum of A1, A2 and A3
    # is same as A
    if(A == A1 + A2 + A3):
            return True
    else:
            return False
# -----------------------------------------------------------------------------
start = time()
for k in [8,600,4*10**4]:
    count = 0
    coords = gen_coords(k)
    for v1 in coords:
        for v2 in coords:
            if v1 == v2:
                continue
            for v3 in coords:
                if v3 == v1 or v3 == v2:
                    continue
                if contains_origin(v1,v2,v3):
                    count += 1
    print(f'Triangles containing the origin: {count//6}, Run-Time: {time()-start:.3f}')
# -----------------------------------------------------------------------------
#solution: 333333208685971546
# -----------------------------------------------------------------------------
