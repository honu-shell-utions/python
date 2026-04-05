################################################################################
# 139-pythagorean_tiles.py
# 
# Pythagorean tiles
# Let (a, b, c) represent the three sides of a right angle triangle with
# integral length sides. It is possible to place four such triangles together
# to form a square with length c.
#
# For example, (3, 4, 5) triangles can be placed together to form a 5 by 5
# square with a 1 by 1 hole in the middle and the 5 by 5 square can be tiled
# with twenty-five 1 by 1 squares.
#
# However, if (5, 12, 13) triangles were used then the hole would measure 7 x 7
# and these could not be used to tile the 13 by 13 square.
#
# Given that the perimeter of the right triangle is less than one-hundred
# million, how many Pythagorean triangles would allow such a tiling to take
# place? 
# one hundred million == 10**8
################################################################################
from math import gcd
from time import time
################################################################################
def get_prim_list(limit):
    a=0
    b=0
    c=0
    m=2
    prim_list = []
    while c < limit//2:
        for n in range(1,m):
            a=m*m-n*n
            b=2*m*n
            c=m*m+n*n
            if a+b+c > limit:
                break
            if gcd(a,b,c) == 1:
                prim_list.append(sorted([a,b,c]))           
        m += 1
    return prim_list

def get_trip_list(prim_list,limit):
    trip_list = []
    for p in prim_list:
        trip_list.append(p)
        k = 2
        while k*p[0] + k*p[1] + k*p[2] <= limit:
            trip_list.append([k*p[0],k*p[1],k*p[2]])
            k += 1
    return trip_list

start = time()
count = 0
limit = 10**8
p_list = get_prim_list(limit)
t_list = get_trip_list(p_list,limit)
for t in t_list:
    square_area = t[2]**2
    tri_area = 2 * t[0] * t[1]
    hole_area = square_area - tri_area
    if square_area % hole_area == 0:
        count += 1
    
print('Solution:',count,'Run Time:',time()-start)
#solution: 10057761
