# p102_triangle_containment.py
#
# Three distinct points are plotted at random on a Cartesian plane, for which
# -1000 ≤ x, y ≤ 1000, such that a triangle is formed.
#
# Consider the following two triangles:
# A(-340,495), B(-153,-910), C(835,-947)
# X(-175,41), Y(-421,-714), Z(574,-645)
#
# It can be verified that triangle ABC contains the origin, whereas triangle
# XYZ does not.
# Using the p102_triangles.txt text file containing the co-ordinates of
# one thousand "random" triangles, find the number of triangles for which the
# interior contains the origin.
#
# NOTE: The first two examples in the file represent
#       the triangles in the example given above.
################################################################################
from numpy import array, cross
import time
import csv
################################################################################
def isTriangle(x1,y1,x2,y2,x3,y3):
    AB = array((x2-x1,y2-y1))
    AC = array((x3-x1,y3-y1))
    if cross(AB,AC) == 0:
        return False
    else:
        return True
################################################################################
class Triangle:
    def __init__(self,x1,y1,x2,y2,x3,y3):    
        AB = array((x1-x2,y1-y2))
        BC = array((x2-x3,y2-y3))
        CA = array((x3-x1,y3-y1))
        AP = array((x1,y1))
        BP = array((x2,y2))
        CP = array((x3,y3))
        cross01 = cross(AB,AP)
        cross02 = cross(BC,BP)
        cross03 = cross(CA,CP)
        if (cross01 > 0 and cross02 > 0 and cross03 > 0) or\
            cross01 < 0 and cross02 < 0 and cross03 < 0:
            self.containsOrigin = True
        else:
            self.containsOrigin = False    
################################################################################
def processFile():
    count = 0
    with open('102-triangles.txt', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            x1,y1,x2,y2,x3,y3 = int(row[0]),int(row[1]),int(row[2]),\
                                int(row[3]),int(row[4]),int(row[5])           
            if isTriangle(x1,y1,x2,y2,x3,y3):
                temp = Triangle(x1,y1,x2,y2,x3,y3)
                if temp.containsOrigin:
                    count += 1
    return(count)
################################################################################
start = time.time()
print('Solution: ',processFile(),'Run Time: ',time.time()-start)
################################################################################
# solution: 228
################################################################################













