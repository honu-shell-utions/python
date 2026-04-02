#  -----------------------------------------------------------------------------
#  Biclinic Integral Quadrilaterals
#  Problem 311
#  https://projecteuler.net/problem=311
#  -----------------------------------------------------------------------------
from matplotlib.pyplot import *
from random import randint
from math import sqrt
#  -----------------------------------------------------------------------------
def get_intersections(x0, y0, r0, x1, y1, r1):
    # circle 1: (x0, y0), radius r0
    # circle 2: (x1, y1), radius r1
    d = sqrt((x1-x0)**2 + (y1-y0)**2)
    # non intersecting
    if d > r0 + r1 :
        return 0,0,0,0,None
    # One circle within other
    if d < abs(r0-r1):
        return 0,0,0,0,None
    # coincident circles
    if d == 0 and r0 == r1:
        return 0,0,0,0,None
    else:
        a = (r0**2-r1**2+d**2)/(2*d)
        h = sqrt(r0**2-a**2)
        x = x0+a*(x1-x0)/d   
        y = y0+a*(y1-y0)/d
        
        x2 = x+h*(y1-y0)/d     
        y2 = y-h*(x1-x0)/d 
        x3 = x-h*(y1-y0)/d
        y3 = y+h*(x1-x0)/d
        
        return x2,y2,x3,y3,True
#  -----------------------------------------------------------------------------
def get_vertex(x0,y0,x1,y1):
    while True:
        r0 = randint(1,2*x1)
        r1 = randint(1,2*x1)
        x2,y2,x3,y3,res = get_intersections(x0, y0, r0, x1, y1, r1)
        if res and x0 < x2 < x1 and max(y2,y3) > 0:
            return x2,max(y2,y3)
#  -----------------------------------------------------------------------------
for _ in range(10**1):
    Bx = randint(-100,-1)
    By = 0
    text(Bx,By,'B')
    Dx = -Bx
    Dy = 0
    text(Dx,Dy,'D')
    text(0,0,'O')
    Ax,Ay = get_vertex(Bx,By,Dx,Dy)
    text(Ax,Ay,'A')
    Cx,Cy = get_vertex(Bx,By,Dx,Dy)
    Cy = -Cy
    text(Cx,Cy,'C')
    x_vals = [Ax,Bx,Cx,Dx,Ax]
    y_vals = [Ay,By,Cy,Dy,Ay]
    plot(x_vals,y_vals)
    x_vals = [0,Ax]
    y_vals = [0,Ay]
    plot(x_vals,y_vals,linestyle='dashed')
    x_vals = [0,Cx]
    y_vals = [0,Cy]
    plot(x_vals,y_vals,linestyle='dashed')
    x_vals = [Bx,Dx]
    y_vals = [By,Dy]
    plot(x_vals,y_vals)

    show()
#  -----------------------------------------------------------------------------
#  solution: 2466018557
#  -----------------------------------------------------------------------------
