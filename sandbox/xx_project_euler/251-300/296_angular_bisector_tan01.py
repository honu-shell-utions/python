#  -----------------------------------------------------------------------------
#  Angular Bisector and Tangent
#  Problem 296
#  https://projecteuler.net/problem=296
#  -----------------------------------------------------------------------------
import numpy as np
from math import sqrt, inf, atan, pi, tan
from random import randint
import matplotlib.pyplot as plt
#  -----------------------------------------------------------------------------
def make_circle(x,y,r):
    return plt.Circle((x,y),r,fill=False)
#  -----------------------------------------------------------------------------
def get_slope(x1,y1,x2,y2):
    if x2 - x1 == 0:
        return inf
    else:
        return (y2-y1)/(x2-x1)
#  -----------------------------------------------------------------------------
def angle_between(M1, M2):	
    # Store the tan value of the angle
    tan_theta = (M2 - M1) / (1 + M1 * M2)
    # Calculate inverse tan
    angle = atan(tan_theta)
    if angle < 0:
        angle += pi
    return angle
#  -----------------------------------------------------------------------------
def create_circle(T):
    (x1, y1), (x2, y2), (x3, y3) = T
    A = np.array([[x3-x1,y3-y1],[x3-x2,y3-y2]])
    Y = np.array([(x3**2 + y3**2 - x1**2 - y1**2),(x3**2+y3**2 - x2**2-y2**2)])
    if np.linalg.det(A) == 0:
        return (0,0),0
    A_inv = np.linalg.inv(A)
    X = 0.5*np.dot(A_inv,Y)
    x,y = X[0],X[1]
    r = sqrt((x-x1)**2+(y-y1)**2)
    return (x,y),r
#  -----------------------------------------------------------------------------
for _ in range(10):
    #generate vertices
    #BC ≤ AC ≤ AB.
    while True:
        BC = randint(1,20)
        AC = randint(1,20)
        AB = randint(1,20)
        if BC <= AC and AC <= AB and BC+AC > AB and AC+AB > BC and BC+AB > AC:
            break
    x1 = 0
    y1 = 0
    x2 = AB
    y2 = 0
    x3 = (AB**2-BC**2+AC**2)/(2*AB)
    y3 = sqrt(AC**2 - x3**2)
            
    #create the circle
    T = ((x1, y1),(x2, y2),(x3, y3))
    center,radius = create_circle(T)

    #set display parameters & make the cricle
    fig, ax = plt.subplots()
    plt.axis('off')
    ax.set_aspect('equal', adjustable='datalim')
    x,y = center
    ax.add_patch(make_circle(x,y,radius))

    #plot the points
    plt.plot(x1,y1,'')
    plt.text(-1,y1,'A')
    
    plt.plot(x2,y2,'')
    plt.text(1.1*x2,y2,'B')
    
    plt.plot(x3,y3,'')
    plt.text(.9*x3,1.1*y3,'C')

    #plot the lines
    plt.plot([x1,x2],[y1,y2])
    plt.plot([x1,x3],[y1,y3])
    plt.plot([x2,x3],[y2,y3])
    plt.title(f'Vertices: ({x1},{y1}), ({x2},{y2}), ({round(x3,2)},{round(y3,2)})\n ')   

    #plot tangent to circle a point C
    m = get_slope(x,y,x3,y3)
    mt = -1/m
    plt.plot([0,AB+1],[mt*(-1-x3)+y3,mt*(AB+1-x3)+y3])
    plt.plot([0,AB+1],[mt*(-1-x2)+y2,mt*(AB+1-x2)+y2])

    #get slopes of AC and BC & angle between
    m_AC = get_slope(x1,y1,x3,y3)
    m_BC = get_slope(x3,y3,x2,y2)
    ang01 = angle_between(m_AC,m_BC)/2
    ang02 = angle_between(0,m_AC)
    m_CE = tan(ang01+ang02)
    plt.plot([0,AB],[m_CE*(0-x3)+y3,m_CE*(AB-x3)+y3])
    ax.plot()
    plt.show()
plt.close(fig)
#  -----------------------------------------------------------------------------
#  solution: 1137208419
#  -----------------------------------------------------------------------------
