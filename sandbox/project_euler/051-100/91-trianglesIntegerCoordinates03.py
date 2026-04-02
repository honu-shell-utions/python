################################################################################
##Right triangles with integer coordinates
##Problem 91
##The points P (x1, y1) and Q (x2, y2) are plotted at integer
##co-ordinates and are joined to the origin, O(0,0), to form ΔOPQ.
##
##There are exactly fourteen triangles containing a right
##angle that can be formed when each co-ordinate lies between 0 and 2 inclusive; that is,
##0 ≤ x1, y1, x2, y2 ≤ 2.
##
##Given that 0 ≤ x1, y1, x2, y2 ≤ 50, how many
##right triangles can be formed?
################################################################################
from math import sqrt
import time
################################################################################
def noTriangle(pt1,pt2):
    (x1,y1) = pt1
    (x2,y2) = pt2

    if (x1 == 0 and y1 == 0) or (x2 == 0 and y2 == 0):
        return True

    if (x1 == 0 and x2 == 0) or (y1 == 0 and y2 == 0):
        return True

    if x1 == 0 or x2 == 0:
        return False

    if y1/x1 == y2/x2:
        return True

################################################################################
def rightTriangle(p1,p2):
    (x1,y1) = pt1
    (x2,y2) = pt2
    a2 = x1**2+y1**2
    b2 = (x2-x1)**2 + (y2-y1)**2
    c2 = x2**2+y2**2
    h2 = max(a2,b2,c2)
    if h2 == a2 + b2 or h2 == a2 + c2 or h2 == b2 + c2:
        return True
    else:
        return False
################################################################################
def theTest(p1,p2):
    if not noTriangle(p1,p2) and rightTriangle(p1,p2):
        return True
    else:
        return False
################################################################################
start = time.time()
p1 = []
p2 = []
for x in range(51):
    for y in range(51):
        p1.append((x,y))
        p2.append((x,y))
count = 0
for pt1 in p1:
    for pt2 in p2:
        if theTest(pt1,pt2):
            count += 1
print('The solution:',count//2,'Run time:',time.time()-start)
################################################################################
#solution: 14234
################################################################################
