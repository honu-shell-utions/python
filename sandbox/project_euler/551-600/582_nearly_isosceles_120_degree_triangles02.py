"""
582_nearly_isosceles_120_degree_triangles.py
https://projecteuler.net/problem=582

Nearly Isosceles 120 Degree Triangles
    Let a, b and c be the sides of an integer sided triangle with one angle of
    120 degrees, a ≤ b ≤ c and b-a ≤ 100.

    Let T(n) be the number of such triangles with c ≤ n.

    T(1000) = 235 and T(10^8) = 1245

    Find T(10^100)
==============================================================================
page 12
difficulty 50%
pe_ans = 19903
==============================================================================

"""
#  -----------------------------------------------------------------------------
from matplotlib.pyplot import *
from math import sqrt, sin, cos, pi
from random import uniform
#  -----------------------------------------------------------------------------
def gen_trips(n):
    trips = []
    for a in range(1,n+1):
        for b in range(a,n+1):
            if b - a > 100:
                continue
            c = sqrt(a**2 + b**2 + a*b)
            if c <= b or c > n:
                continue
            if c == int(c):
                temp = sorted([a,b,int(c)])
                if temp not in trips:
                    trips.append(temp)
    return trips
#  -----------------------------------------------------------------------------
def two_circle_intersections(x0, y0, r0, x1, y1, r1):
    d = sqrt((x1-x0)**2 + (y1-y0)**2)   
    # non intersecting
    if d > r0 + r1 :
        return None
    # One circle within other
    if d < abs(r0-r1):
        return None
    # coincident circles
    if d == 0 and r0 == r1:
        return None
    else:
        a=(r0**2-r1**2+d**2)/(2*d)
        h=sqrt(r0**2-a**2)
        x2=x0+a*(x1-x0)/d   
        y2=y0+a*(y1-y0)/d   
        x3=x2+h*(y1-y0)/d     
        y3=y2-h*(x1-x0)/d 
        x4=x2-h*(y1-y0)/d
        y4=y2+h*(x1-x0)/d  
        return x3, y3, x4, y4
#  -----------------------------------------------------------------------------
def graph_trips(trips):
    x0,y0 = 0,0
    count = 0
    for t in trips:
        count += 1
        a,b,c = t
        theta = uniform(0,2*pi)
        x1 = a*cos(theta)
        y1 = b*sin(theta)
        x2,y2,_,_ = two_circle_intersections(x0, y0, b, x1, y1, c)
        plot([x0,x1,x2,x0],[y0,y1,y2,y0])
        title(f'A = {a}, B = {b}, C = {c}, Count = {count}')
        show()
#  ----------------------------------------------------------------------------- 
trips = gen_trips(10**3)
graph_trips(trips)
#  ----------------------------------------------------------------------------- 

