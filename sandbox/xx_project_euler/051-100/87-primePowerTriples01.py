################################################################################
##Prime power triples
##Problem 87
##
##The smallest number expressible as the sum of a prime square, prime cube,
##and prime fourth power is 28. In fact, there are exactly four numbers below
##fifty that can be expressed in such a way:
##
##28 = 2^2 + 2^3 + 2^4
##33 = 3^2 + 2^3 + 2^4
##49 = 5^2 + 2^3 + 2^4
##47 = 2^2 + 3^3 + 2^4
##
##How many numbers below fifty million can be expressed as the sum of
##a prime square, prime cube, and prime fourth power?
################################################################################
from sympy import primerange
import math
import time
primeSquareList = []
primeCubeList = []
primeFourthList = []
solutions = set()
################################################################################
def fillLists(n):
    pList = list(primerange(2,n))
    for p in pList:
        primeSquareList.append(p**2)
        primeCubeList.append(p**3)
        primeFourthList.append(p**4)
################################################################################
def euler87(limit):
    for pf in primeFourthList:
        for pc in primeCubeList:
            for ps in primeSquareList:
                sum = pf + pc + ps
                if sum < limit:
                    solutions.add(sum)
    
    return solutions
################################################################################
start = time.time()
fillLists(int(math.sqrt(50_000_000)))
print(len(euler87(50_000_000)))
print(time.time()-start)
################################################################################
#solution: 1097343
################################################################################
