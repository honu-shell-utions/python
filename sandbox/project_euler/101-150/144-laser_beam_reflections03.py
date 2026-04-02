################################################################################
##Investigating multiple reflections of a laser beam
##Problem 144
##
##In laser physics, a "white cell" is a mirror system that
##acts as a delay line for the laser beam. The beam enters
##the cell, bounces around on the mirrors, and eventually works its way back out.
##
##The specific white cell we will be considering is an ellipse
##with the equation 4x^2 + y^2 = 100
##
##The section corresponding to −0.01 ≤ x ≤ +0.01 at the top is missing,
##allowing the light to enter and exit through the hole.
##
##The light beam in this problem starts at the point (0.0,10.1)
##just outside the white cell, and the beam first impacts the mirror at (1.4,-9.6).
##
##Each time the laser beam hits the surface of the ellipse, it follows
##the usual law of reflection "angle of incidence equals angle of reflection."
##That is, both the incident and reflected beams make the same angle with
##the normal line at the point of incidence.
##
##In the figure on the left, the red line shows the first two points of
##contact between the laser beam and the wall of the white cell; the blue
##line shows the line tangent to the ellipse at the point of incidence of
##the first bounce.
##
##The slope m of the tangent line at any point (x,y) of the given ellipse
##is: m = −4x/y
##
##The normal line is perpendicular to this tangent line at the point of incidence.
##
##The animation on the right shows the first 10 reflections of the beam.
##
##How many times does the beam hit the internal surface of the white cell
##before exiting?
################################################################################
from math import sqrt
from time import time

go = time()
xA = 0.0
yA = 10.1
xO = 1.4
yO = -9.6
hits_list = [(1.4,-9.6)]

while xO > 0.01 or xO < -0.01 or yO < 0:
    mA = (yO - yA) / (xO - xA)  # slope
    mO = -4*xO / yO             # slope ellipse tangent

    # slope of B
    tanA = (mA - mO) / (1 + mA*mO)
    mB = (mO - tanA)/ (1 + tanA*mO)

    interceptB = yO - mB * xO

    # solve the quadratic equation for finding the intersection of B and the
    # ellipse a*x^2 + b*x + c = 0
    a = 4 + mB**2
    b = 2 * mB * interceptB
    c = interceptB**2 - 100
    
    ans1 = (-b + sqrt(b**2 - 4 * a * c)) / (2 * a)
    ans2 = (-b - sqrt(b**2 - 4 * a * c)) / (2 * a)
    
    xA = xO
    yA = yO

    # take the solution which is furtherst from x0
    if abs(ans1 - xO) > abs(ans2 - xO):
        xO = ans1
    else:
        xO = ans2
    yO = mB * xO + interceptB
    hits_list.append((xO,yO))

print(f'The number of bounces is: {len(hits_list)-1:}, runtime: {time()-go}')
################################################################################
#solution: 354
################################################################################
