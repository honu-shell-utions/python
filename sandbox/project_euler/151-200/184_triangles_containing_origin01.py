# p184_triangles_containing_origin.py
#
# triangles containing the origin
#
# Consider the set I(sub)r of points (x, y) with integer co-ordinates in the
# interior of the circle with radius r, centered at the origin,
# i.e. x^2 + y^2 < r^2.
#
# For a radius of 2, I(sub)2 contains the nine points (0,0), (1,0), (1,1),
# (0,1), (-1,1), (-1,0), (-1,-1), (0,-1) and (1,-1). There are eight triangles
# having all three vertices in I(sub)2 which contain the origin in the interior.
# Two of them are shown in pic, the others are obtained from these by rotation.
#
# For a radius of 3, there are 360 triangles containing the origin in the
# interior and having all vertices in I(sub)3 and for I(sub)5
# the number is 10600.
#
# How many triangles contain the origin in the interior and
# having all three vertices in I(sub)105?

# -----------------------------------------------------------------------------
# how do you check if a point lies in a triangle using vectors
# A simple way is to: find the vectors connecting the point to each of the
# triangle's three vertices and sum the angles between those vectors. If the
# sum of the angles is 2*pi then the point is inside the triangle.
# -----------------------------------------------------------------------------
from fractions import Fraction
from time import time
import numpy as np

# -----------------------------------------------------------------------------
def angle_between(vector_1,vector_2):
    unit_vector_1 = vector_1 / np.linalg.norm(vector_1)
    unit_vector_2 = vector_2 / np.linalg.norm(vector_2)
    dot_product = np.dot(unit_vector_1, unit_vector_2)
    dot_product = round(dot_product,8)
    if dot_product == 0:
        angle = np.pi/2
    else:
        angle = np.arccos(dot_product)
    return angle
# -----------------------------------------------------------------------------
def make_points():
    temp = []
    for x in range(-radius+1,radius):
        for y in range(-radius+1,radius):
            if 0 < x**2 + y**2 < radius**2:
                temp.append((x,y))
    return temp
# -----------------------------------------------------------------------------
def make_pairs():
    temp = []
    for p1 in points:
        for p2 in points:
            if p1 != p2 and (p2,p1) not in temp:
                temp.append((p1,p2))
    return temp
# -----------------------------------------------------------------------------
start = time()
radius = 10
points = make_points()
pairs = make_pairs()
count = 0
for p1,p2 in pairs:
    x1,y1 = p1
    x2,y2 = p2
    if (x1,y1) == (-x2,-y2):
        continue
    v = np.array([x1,y1])
    w = np.array([x2,y2])
    between = angle_between(v,w)
    pts_between = int(between/(2*np.pi)*len(points))
    count += pts_between
    #print(p1,p2,round(between*180/np.pi,2),pts_between)
    
print(f'Solution: {count//2}, Run-Time: {time()-start}')
# -----------------------------------------------------------------------------    
#solution: 1725323624056
# -----------------------------------------------------------------------------
