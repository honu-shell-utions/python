#from Andy Math
#https://youtu.be/5ZoY3tXeQOs?si=jylEpV9W1utR6LoJ
#this is not a cool analytical solution like Andy provides but is more of
#a exploritory, it's a let's make a guess type of solution.  It's a fun way to play
#with the math and to learn some Python.
#  -----------------------------------------------------------------------------
#jim mccleery
#March 27, 2026
#Kona, HI
#  -----------------------------------------------------------------------------
from math import pi, sin, cos, sqrt, asin
from matplotlib.pyplot import *
import numpy as np
from random import uniform
#  -----------------------------------------------------------------------------
def plot_line(x1,y1,x2,y2):
    plot([x1,x2],[y1,y2])
#  -----------------------------------------------------------------------------
def distance(x1,y1,x2,y2):
    return sqrt( (x1-x2)**2 + (y1-y2)**2 )
#  -----------------------------------------------------------------------------
def plot_partial_circle(x,y,radius,start,stop):
    angle = np.linspace(start,stop,1500)
    x_arr = radius*np.cos(angle) + x 
    y_arr = radius*np.sin(angle) + y
    plot(x_arr,y_arr)
#  -----------------------------------------------------------------------------
def poly_area(vertices):
    n = len(vertices)  # Number of vertices
    area = 0
    
    # Iterate over all vertices
    for i in range(n):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % n]  # Next vertex (wraps around to the first vertex)
        area += x1 * y2 - y1 * x2
    
    return abs(area) / 2
#  -----------------------------------------------------------------------------
def poly_shade(vertices):
    # Separate the x and y coordinates
    x_coords, y_coords = zip(*vertices)
    # Close the polygon by appending the first vertex to the end
    x_coords = list(x_coords) + [x_coords[0]]
    y_coords = list(y_coords) + [y_coords[0]]
    return x_coords,y_coords
#  -----------------------------------------------------------------------------
tilt = pi/6
while True:
    #we start by making a guess for the radius of the circle centered on (x0,y0)
    r1 = uniform(4,5)
    h = 12/r1
    r2 = h/sin(tilt)
    x0,y0 = 0,0
    x1,y1 = -r1,0
    x2,y2 = r1,0
    x3,y3 = r2*cos(tilt),r2*sin(tilt)
    x4,y4 = 2*r2*cos(tilt),2*r2*sin(tilt)
    r3 = distance(x2,y2,x3,y3)
    theta = asin(r1*sin(tilt)/r3)
    x5,y5 = x2+r3*cos(-theta),y2+r3*sin(-theta)
    d = distance(x5,y5,x3,y3)
    #checking to see if (x3,y3) and (x2,y2) and (x5,y5) are colinear
    #if so we have a solution
    if abs(d-2*r3) < 0.00001:
        break

text(x0,y0-.5,'(x0,y0)')
text(x1-.2,y1+.5,'(x1,y1)')
text(x2+.2,y2,'(x2,y2)')
text(x3-.5,y3+.2,'(x3,y3)')
text(x4+.2,y4,'(x4,y4)')
text(x5,y5-.2,'(x5,y5)')
plot_line(x3,y3,x2,y2)
plot_line(x1,y1,x2,y2)
plot_line(x0,y0,x2,y2)
plot_line(x0,y0,x4,y4)
plot_line(x2,y2,x5,y5)
plot_line(x1,y1,x4,y4)
plot_line(x4,y4,x5,y5)
plot_line(x5,y5,x1,y1)

vertices = [(x1,y1),(x4,y4),(x5,y5)]
area = poly_area(vertices)
fill(*poly_shade(vertices), color='lightblue', edgecolor='blue', linewidth=2)
plot_partial_circle(x0,y0,r1,pi,2*pi)
plot_partial_circle(x3,y3,r2,tilt,pi+tilt)
plot_partial_circle(x2,y2,r3,-theta,pi-theta)
title('Shaded Area = '+str(round(area,2)))
axis('equal')
show()
