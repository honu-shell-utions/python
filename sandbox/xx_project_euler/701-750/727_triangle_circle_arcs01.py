#  -----------------------------------------------------------------------------
#  Triangle of Circular Arcs
#  Problem 727
#  https://projecteuler.net/problem=727
#  -----------------------------------------------------------------------------
from matplotlib.pyplot import *
from random import *
import numpy as np
from math import sqrt,pi
from itertools import cycle
cycol = cycle('bgrcmk')
#  -----------------------------------------------------------------------------
def get_intersections(x0, y0, r0, x1, y1, r1):
    # circle 1: (x0, y0), radius r0
    # circle 2: (x1, y1), radius r1

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
        
        return (x3, y3, x4, y4)
#  -----------------------------------------------------------------------------
def get_radii():
    ra = randint(1,98)
    rb = randint(ra+1,99)
    rc = randint(rb+1,100)
    return ra,rb,rc
#  -----------------------------------------------------------------------------
def make_circle(x1,y1,radius):
    angle = np.linspace(0,2*pi,1500)
    x = radius*np.cos(angle) + x1 
    y = radius*np.sin(angle) + y1
    plot(x,y,next(cycol))
#  -----------------------------------------------------------------------------
for _ in range(5):
    axis('equal')
    ra,rb,rc = get_radii()
    x1 = 0
    y1 = 0
    make_circle(x1,y1,ra)

    x2 = ra + rb
    y2 = 0
    make_circle(x2,y2,rb)

    #create the third circle
    x,y3a,x3b,y3b = get_intersections(x1,y1,ra+rc,x2,y2,rb+rc)
    y = max(y3a,y3b)
    make_circle(x,y,rc)
    title('Project Euler # 727')
    show()
#  -----------------------------------------------------------------------------
#  solution: 3.64039141
#  -----------------------------------------------------------------------------
