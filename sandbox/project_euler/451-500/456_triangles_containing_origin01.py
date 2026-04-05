# -----------------------------------------------------------------------------
# Triangles containing the origin II
# Problem 456
# https://projecteuler.net/problem=456
# -----------------------------------------------------------------------------
from matplotlib.pyplot import *
from itertools import combinations
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
def plot_triangle(v1,v2,v3):
    x1,y1 = v1
    x2,y2 = v2
    x3,y3 = v3
    plot([x1,x2,x3,x1],[y1,y2,y3,y1])
# -----------------------------------------------------------------------------
coords = gen_coords(8)
vertices = combinations(coords,3)
for v1,v2,v3 in vertices:
    axis('off')
    axis('equal')
    plot(0,0,'o')
    plot_triangle(v1,v2,v3)
    if contains_origin(v1,v2,v3):
        title('Contains Origin')
    else:
        title('Does Not Contain Origin')
    show()
# -----------------------------------------------------------------------------
#solution: 333333208685971546
# -----------------------------------------------------------------------------
