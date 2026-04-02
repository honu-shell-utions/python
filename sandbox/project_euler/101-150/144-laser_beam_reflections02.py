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
def norm(x,y):
    return y/(4*x)

def reflect(m1,n):
    return (2*n - m1 + m1*n**2)/(2*m1*n - n**2 + 1)

def line(m,x,y):
    return y - m*x

def quad(a,b,c):
    x0 = (-b + (b**2 - 4*a*c)**0.5)/(2*a)
    x1 = (-b - (b**2 - 4*a*c)**0.5)/(2*a)
    return [x0,x1]

def move(m,c,x_old):
    for i in range(2):
        x_new = quad(4+m**2,2*m*c,c**2-100)[i]
        if abs(x_old - x_new) >= 10**-10:
            y = m*x_new + c
            return [x_new,y]

p = [1.4,-9.6]
m1 = -(19.7 / 1.4)
count = 0

while not (abs(p[0]) <= .01 and p[1] > 0):
    n = norm(p[0],p[1])
    m3 = reflect(m1,n)
    c = line(m3,p[0],p[1])
    p = move(m3,c,p[0])
    m1 = m3
    count += 1

print(count)
################################################################################
#solution: 354
################################################################################
