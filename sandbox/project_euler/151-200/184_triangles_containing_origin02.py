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
from fractions import Fraction
from collections import defaultdict

radius = 105

angle2count = defaultdict(int)

for i in range(1,radius):
    for j in range(-i, i):
        if i*i+j*j < radius*radius:
            angle2count[Fraction(j,i)] += 1

print (len(angle2count), "angles")
counts = [sum(x**p for x in angle2count.values()) for p in [1,2,3]]
print (counts)
print (int((8*counts[0]**3+4*counts[2])/3- 4*counts[1]*counts[0]) )
# -----------------------------------------------------------------------------    
#solution: 1725323624056
# -----------------------------------------------------------------------------
