#  -----------------------------------------------------------------------------
#  Triangle of Circular Arcs
#  Problem 727
#  https://projecteuler.net/problem=727
#  -----------------------------------------------------------------------------
from matplotlib.pyplot import *
from random import randint,uniform
from math import sqrt,gcd,pi,atan2
from numpy import linspace,sin,cos
from itertools import cycle
#  -----------------------------------------------------------------------------
cycol = cycle('bgrcmk')
#  -----------------------------------------------------------------------------
def star_incircle(ra,rb,rc):
  #Decartes' Theorem to compute radius
  k1 = 1/ra
  k2 = 1/rb
  k3 = 1/rc
  k4 = k1 + k2 + k3 +2*sqrt(k1*k2+k1*k3+k2*k3)
  radius = 1/k4

  #solve two quadratics to compute the center
  x = ((ra+rb)**2+(ra+radius)**2-(rb+radius)**2)/(2*(ra+rb))
  y = sqrt((ra+radius)**2 - x**2)

  return x,y,radius
#  -----------------------------------------------------------------------------
def tri_incircle(xa,ya,xb,yb,xc,yc):    
    a = sqrt( (xb-xc)**2 + (yb-yc)**2)
    b = sqrt( (xa-xc)**2 + (ya-yc)**2)
    c = sqrt( (xb-xa)**2 + (yb-ya)**2)
    s = (a+b+c)/2
    m = sqrt(s*(s-a)*(s-b)*(s-c))
    n = a+b+c
    r = 2*m/n
    x = (a*xa+b*xb+c*xc)/n
    y = (a*ya+b*yb+c*yc)/n
    return x,y,r
#  -----------------------------------------------------------------------------
def get_intersections(x0, y0, r0, x1, y1, r1):
    d = sqrt((x1-x0)**2 + (y1-y0)**2)
    a = (r0**2-r1**2+d**2)/(2*d)
    h = sqrt(round(r0**2-a**2,5))
    x2 = x0+a*(x1-x0)/d   
    y2 = y0+a*(y1-y0)/d   
    x3 = x2+h*(y1-y0)/d     
    y3 = y2-h*(x1-x0)/d 
    x4 = x2-h*(y1-y0)/d
    y4 = y2+h*(x1-x0)/d
    return x3, y3, x4, y4
#  -----------------------------------------------------------------------------
def make_circle(x1,y1,radius):
    angle = linspace(0,2*pi,1500)
    x = radius*cos(angle) + x1 
    y = radius*sin(angle) + y1
    plot(x,y,next(cycol))
    plot(x1,y1,'o')
#  -----------------------------------------------------------------------------
LIMIT = 10
for ra in range(1,LIMIT-1):
    for rb in range(ra+1,LIMIT):
        for rc in range(rb+1,LIMIT+1):
            if gcd(ra,rb,rc) != 1:
                continue

            #set the axes equal
            axis('equal')

            #first circle
            x1 = 0
            y1 = 0
            make_circle(x1,y1,ra)

            #second circle
            x2 = ra + rb
            y2 = 0
            make_circle(x2,y2,rb)

            #third circle, use first of the two solutions
            x3,y3a,x3b,y3b = get_intersections(x1,y1,ra+rc,x2,y2,rb+rc)
            y3 = max(y3a,y3b)
            make_circle(x3,y3,rc)

            #find the center and radius of the incircle for the triangle
            #formed by the centers of the three circles
            x4,y4,radius = tri_incircle(x1,y1,x2,y2,x3,y3)
            make_circle(x4,y4,radius)

            #use Decartes' Theorem to compute the radius of the 'star' incircle
            #solve two quadratics to compute the center of the 'star' incircle
            x5,y5,radius = star_incircle(ra,rb,rc)
            make_circle(x5,y5,radius)

            #compute the distance between the two incenters
            d = sqrt( (x5-x4)**2 + (y5-y4)**2 )
            title(f'Project Euler # 727: Distance between centers: {round(d,8)}')
            show()
#  -----------------------------------------------------------------------------
#  solution: 3.64039141
#  -----------------------------------------------------------------------------
