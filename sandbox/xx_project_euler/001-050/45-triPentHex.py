################################################################################
##Triangular, pentagonal, and hexagonal
##Problem 45
##Triangle, pentagonal, and hexagonal numbers are generated
##by the following formulae:
##
##Triangle	Tn=n(n+1)/2	 	1, 3, 6, 10, 15, ...
##Pentagonal	Pn=n(3n−1)/2	 	1, 5, 12, 22, 35, ...
##Hexagonal	Hn=n(2n−1)	 	1, 6, 15, 28, 45, ...
##
##It can be verified that T285 = P165 = H143 = 40755.
##Find the next triangle number that is also pentagonal and hexagonal.
################################################################################
import math
################################################################################
def makeTri(num):
    return((num*(num+1))//2)
################################################################################
def isPent(num):
    test = (1+math.sqrt(1+24*num))/6
    return(test == int(test))
################################################################################
def isHex(num):
    test = (1+math.sqrt(1+8*num))/4
    return(test == int(test))
################################################################################
START = 286
while True:
    tri = makeTri(START)
    if isPent(tri) and isHex(tri):
        print(tri)
        break
    else:
        START += 1
################################################################################
#solution:1533776805 
################################################################################
