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
from matplotlib.pyplot import *
from math import sqrt,pi
import numpy as np
#  -----------------------------------------------------------------------------
def plot_circle(radius):
    angle = np.linspace(0,2*pi,1500)
    x_arr = radius*np.cos(angle)
    y_arr = radius*np.sin(angle)
    plot(x_arr,y_arr)
#  -----------------------------------------------------------------------------
def define_circle(v1,v2,v3):
    x1,y1 = v1
    x2,y2 = v2
    x3,y3 = v3
    temp = x2 * x2 + y2 * y2
    bc = (x1 * x1 + y1 * y1 - temp) / 2
    cd = (temp - x3 * x3 - y3 * y3) / 2
    det = (x1 - x2) * (y2 - y3) - (x2 - x3) * (y1 - y2)
    
    if abs(det) < 1.0e-6:
        return (None, np.inf)
    
    # Center of circle
    cx = (bc*(y2 - y3) - cd*(y1 - y2)) / det
    cy = ((x1 - x2) * cd - (x2 - x3) * bc) / det
    
    radius = sqrt((cx - x1)**2 + (cy - y1)**2)
    return cx,cy,radius
#  -----------------------------------------------------------------------------
def plot_triangle(v1,v2,v3):
    x1,y1 = v1
    x2,y2 = v2
    x3,y3 = v3
    plot([x1,x2,x3,x1],[y1,y2,y3,y1])
#  -----------------------------------------------------------------------------
def get_tri_perimeter(v1,v2,v3):
    x1,y1 = v1
    x2,y2 = v2
    x3,y3 = v3
    d = sqrt((x2-x1)**2 + (y2-y1)**2)
    d += sqrt((x2-x3)**2 + (y2-y3)**2)
    d += sqrt((x3-x1)**2 + (y3-y1)**2)
    return d
#  -----------------------------------------------------------------------------
def plot_oc_segments(v1,v2,v3):
    x1,y1 = v1
    x2,y2 = v2
    x3,y3 = v3

    m1 = (y2-y1)/(x2-x1)
    b1 = -m1*x1+y1
    m2 = -1/m1
    b2 = 5/m1
    x,y = line_intersect(m1,b1,m2,b2)
    plot([x3,x],[y3,y])

    m1 = (y3-y1)/(x3-x1)
    b1 = -m1*x1+y1
    m2 = -1/m1
    b2 = 5/m1
    x,y = line_intersect(m1,b1,m2,b2)
    plot([x2,x],[y2,y])

    m1 = (y2-y3)/(x2-x3)
    b1 = -m1*x2+y2
    m2 = -1/m1
    b2 = 5/m1
    x,y = line_intersect(m1,b1,m2,b2)
    plot([x1,x],[y1,y])
    
#  -----------------------------------------------------------------------------
def line_intersect(m1, b1, m2, b2):
    if m1 == m2:
        return None
    x = (b2 - b1) / (m1 - m2)
    y = m1 * x + b1
    return x,y
#  -----------------------------------------------------------------------------
total_p = 0
triangles = [((-4, 3),(5, 0), (4, -3)),\
             ((4, 3), (5, 0), (-4, -3)),\
             ((-3, 4),(5, 0), (3, -4)),\
             ((3, 4), (5, 0), (-3, -4)),\
             ((0, 5), (5, 0), (0, -5)),\
             ((1, 8), (8, -1),(-4, -7)),\
             ((8, 1), (1, -8),(-4, 7)),\
             ((2, 9), (9, -2),(-6, -7)),\
             ((9, 2), (2, -9),(-6, 7))]

for vertices in triangles:
    axis('equal')
    total_p += get_tri_perimeter(*vertices)
    plot_triangle(*vertices)
    x,y,r = define_circle(*vertices)
    plot_circle(r)
    plot(5,0,'o')
    text(5,0,'OC')
    title(f'Perimeter Accumulation: {round(total_p,4)}')
    if (5,0) not in vertices:
        plot_oc_segments(*vertices)
    grid()
    show()
#  -----------------------------------------------------------------------------
