#-------------------------------------------------------------------------------
##Obtuse Angled Triangles
##Problem 210
##Consider the set S(r) of points (x,y) with integer
##coordinates satisfying |x| + |y| ≤ r.
##
##Let O be the point (0,0) and C the point (r/4,r/4). 
##Let N(r) be the number of points B in S(r), so that
##the triangle OBC has an obtuse angle, i.e. the largest
##angle α satisfies 90°<α<180°.
##
##So, for example, N(4)=24 and N(8)=100.
##
##What is N(1,000,000,000)?
#-------------------------------------------------------------------------------
import matplotlib.pyplot as plt
import numpy as np
#-------------------------------------------------------------------------------
#function to set the dimensions of the axes
def plot_points():
    ax = plt.gca()
    ax.axis(xmin=-radius,xmax=radius,ymin=-radius,ymax=radius) 
    ax.axes.xaxis.set_visible(False)
    ax.axes.yaxis.set_visible(False)
    ax.axes.set_aspect(1) 
    #plot the ordered pairs
    for x,y in hit_list:
        plt.plot(x,y,'.')
    plt.plot(0,0,marker='o')
    plt.plot(x1,y1,marker='o')
    plt.show()
#-------------------------------------------------------------------------------
def is_valid(x,y):
    if abs(x) + abs(y) <= radius:   
        return True
    else:
        return False
#-------------------------------------------------------------------------------
def is_obtuse(x,y):
    a_squared = x**2 + y**2
    b_squared = (x-x1)**2 + (y-y1)**2
    c_squared = x1**2 + y1**2

    if a_squared > b_squared + c_squared:
        return True
    if b_squared > a_squared + c_squared:
        return True
    if c_squared > a_squared + b_squared:
        return True
    return False
#-------------------------------------------------------------------------------
radius = 10**2
x1 = radius/4
y1 = radius/4
hit_list = []
for x in range(-radius,radius+1):
    for y in range(-radius,radius+1):
        if is_valid(x,y):
            if is_obtuse(x,y):
                hit_list.append((x,y))
plot_points()
print(len(hit_list)/(4*radius**2))
print(1598174770174689458/(4*10**18))
#-------------------------------------------------------------------------------
# solution: 1598174770174689458
#-------------------------------------------------------------------------------
