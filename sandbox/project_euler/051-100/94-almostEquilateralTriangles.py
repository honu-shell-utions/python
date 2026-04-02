################################################################################
##Almost equilateral triangles 
##Problem 94
##It is easily proved that no equilateral triangle exists
##with integral length sides and integral area. However,
##the almost equilateral triangle 5-5-6 has an area of 12 square units.
##
##We shall define an almost equilateral triangle to be a triangle
##for which two sides are equal and the third differs by no more
##than one unit.
##
##Find the sum of the perimeters of all almost equilateral triangles
##with integral side lengths and area and whose perimeters do not
##exceed one billion (1,000,000,000).
################################################################################
import decimal
import time
################################################################################
def isValid(twoSides,otherSide):
    temp = 4*twoSides*twoSides - otherSide*otherSide
    temp = decimal.Decimal(temp).sqrt()
    if temp % 1 == 0:
        return True
    else:
        return False
################################################################################
def euler94():
    eqSides = 4
    totalPer = 0
    while True:
        eqSides += 1
        for otherSide in [eqSides-1,eqSides+1]:
            if isValid(eqSides,otherSide):
                per = 2*eqSides + otherSide
                #print(per)
                if per > 10**9:
                    return totalPer
                else:
                    totalPer += per
################################################################################
start = time.time()
print('The solution:',euler94(),'Run time:',time.time()-start)
################################################################################
#solution:518408346
################################################################################
