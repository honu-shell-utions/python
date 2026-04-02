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
from numpy import sqrt, array, linalg, arccos, pi
import time
import csv
################################################################################
def isTriangle(x1,y1,x2,y2,x3,y3):
    a = sqrt((x1-x2)**2 + (y1-y2)**2)
    b = sqrt((x1-x3)**2 + (y1-y3)**2)
    c = sqrt((x2-x3)**2 + (y2-y3)**2)
    s = (a + b + c)/2
    area = sqrt(s*(s-a)*(s-b)*(s-c))
    if area == 0:
        return False
    else:
        return True
################################################################################
class Triangle:
    def __init__(self,x1,y1,x2,y2,x3,y3):    
        self.pt1 = (x1,y1)
        self.pt2 = (x2,y2)
        self.pt3 = (x3,y3)
        self.v1 = array(self.pt1)
        self.v2 = array(self.pt2)
        self.v3 = array(self.pt3)
        self.n1 = linalg.norm(self.v1)
        self.n2 = linalg.norm(self.v2)
        self.n3 = linalg.norm(self.v3)

        alpha = arccos(self.v1.dot(self.v2)/(self.n1*self.n2))
        beta  = arccos(self.v1.dot(self.v3)/(self.n1*self.n3))
        gamma = arccos(self.v2.dot(self.v3)/(self.n2*self.n3))

        if abs(alpha + beta + gamma - 2 * pi) < DELTA:
            self.containsOrigin = True
        else:
            self.containsOrigin = False
        
    def printMe(self):
        print('Triangle vertices:',self.pt1,self.pt2,self.pt3)
        print('Triangle vectors :',self.v1,self.v2,self.v3)
      
################################################################################
def makeTriList():
    tempList = []
    with open('102-triangles.txt', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            x1,y1,x2,y2,x3,y3  = int(row[0]),int(row[1]),int(row[2]),\
                                 int(row[3]),int(row[4]),int(row[5])
            
            if isTriangle(x1,y1,x2,y2,x3,y3):
                tempList.append(Triangle(x1,y1,x2,y2,x3,y3))

    return(tempList)
################################################################################
DELTA = 10**-10
start = time.time()
triList = makeTriList()
count = 0
for tri in triList:
    if tri.containsOrigin:
        count += 1

print('Solution: ',count,'Run Time: ',time.time()-start)
################################################################################
# solution: 228
################################################################################













