################################################################################
## Diophantine equation
## Problem 66
## Consider quadratic Diophantine equations of the form:
##
## x^2 – Dy^2 = 1
##
## For example, when D=13, the minimal solution in x is 6492 – 13×1802 = 1.
##
## It can be assumed that there are no solutions in positive integers
## when D is square.
##
## By finding minimal solutions in x for D = {2, 3, 5, 6, 7},
## we obtain the following:
##
## x^2 - D*y^2 = 1
## 3^2 – 2×2^2 = 1
## 2^2 – 3×1^2 = 1
## 9^2 – 5×4^2 = 1
## 5^2 – 6×2^2 = 1
## 8^2 – 7×3^2 = 1
##
## Hence, by considering minimal solutions in x for D ≤ 7,
## the largest x is obtained when D=5.
##
## Find the value of D ≤ 1000 in minimal solutions of x
## for which the largest value of x is obtained.
################################################################################
import math
from fractions import Fraction
################################################################################
def contFracForSqRoots(n):
    numerator1 = 1
    a = int(math.sqrt(n))
    aList = [a]
    while True:
        if n == a*a:
            break
        numerator2 = (n - a**2) / numerator1
        next = int((math.sqrt(n)+a)/numerator2)
        aList.append(next)
        if next == 2*math.isqrt(n):
            break
        denominator = next*numerator2 - a
        numerator1 = numerator2
        a = denominator
    return aList
################################################################################
def cf2rat(base, sequence):
    numerator = 1
    denominator = sequence[-1]
    for d in sequence[-2::-1]:
        temp = denominator
        denominator = d * denominator + numerator
        numerator = temp
    return Fraction(numerator + base * denominator, denominator)
################################################################################
def getP(q1,D,a0,p1):
    return q1*D - a0*p1
################################################################################
def getQ(p1,a0,q1):
    return p1 - a0*q1
################################################################################
maxX = -1
keepD = 2
for D in range(2,1001):
    #if D is a perfect square skip it
    if math.isqrt(D) == math.sqrt(D):
        continue
    #create a condinued fraction for sqrt(D)
    cf = contFracForSqRoots(D)
    #capture the first element of the cf list
    a0 = cf[0]
    #create a rational number (Fraction) from cf[1:]
    rat = cf2rat(cf[0],cf[1:])
    #get p
    p = getP(rat.denominator,D,a0,rat.numerator)
    #get q
    q = getQ(rat.numerator,a0,rat.denominator)
    #make a Fraction out of p and q, also reduces the fraction
    pq = Fraction(p,q)
    #extract the x
    x = pq.numerator
    #extract the y
    y = pq.denominator
    #if x**2 - D*y**2 == -1 we need to extend the cf another period
    if x**2 - D*y**2 == -1:
        for i in cf[1:]:
            cf.append(i)
        rat = cf2rat(cf[0],cf[1:])
        p = getP(rat.denominator,D,a0,rat.numerator)
        q = getQ(rat.numerator,a0,rat.denominator)
        pq = Fraction(p,q)
        x = pq.numerator
        y = pq.denominator
    #do this to reduce the fraction
    result = Fraction(x,y)
    x = result.numerator
    y = result.denominator
    #print('x=',x,'D=',D,'y=',y,'result=',x**2-D*y**2)
    if x > maxX:
        maxX = x
        keepD = D        
print('The solution:',keepD)
################################################################################
#solution: 661
################################################################################
