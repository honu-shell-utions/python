################################################################################
##Counting rectangles
##Problem 85
##By counting carefully it can be seen that a
##rectangular grid measuring 3 by 2 contains eighteen rectangles:
##
##Although there exists no rectangular grid that contains
##exactly two million rectangles, find the area of the grid
##with the nearest solution.
################################################################################
import math
solutions = []
################################################################################
def numRectangles(n,m):
    area = n*(n+1)*m*(m+1)//4
    return area
################################################################################
def findSolution(delta):
    for m in range(100):
        for n in range(100):
            numRec = numRectangles(n,m)
            if abs(numRec - max) <= delta:
                solutions.append([abs(numRec-max),n,m,n*m,numRec])
                if numRec > max:
                    return
################################################################################
max = 2_000_000

for delta in range(100,0,-1):
    findSolution(delta)

print(min(solutions))
################################################################################
#solution: 2772
################################################################################
