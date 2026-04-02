#-------------------------------------------------------------------------------
## Luxury Hampers
## Problem 236
## 
## Suppliers 'A' and 'B' provided the following numbers
## of products for the luxury hamper market:
## 
## Product	            'A'	     'B'
## Beluga Caviar	            5248	     640
## Christmas Cake            1312     1888
## Gammon Joint	            2624     3776
## Vintage Port	            5760	    3776 
## Champagne Truffles        3936	    5664
## 
## Although the suppliers try very hard to ship their
## goods in perfect condition, there is inevitably some
## spoilage - i.e. products gone bad.
## 
## The suppliers compare their performance using two types of statistic:
## 
## The five per-product spoilage rates for each supplier are equal to the
## number of products gone bad divided by the number of products supplied,
## for each of the five products in turn.
## 
## The overall spoilage rate for each supplier is equal to the total number
## of products gone bad divided by the total number of products provided by
## that supplier.
## 
## To their surprise, the suppliers found that each of the five per-product
## spoilage rates was worse (higher) for 'B' than for 'A' by the same factor
## (ratio of spoilage rates), m > 1; and yet, paradoxically, the overall
## spoilage rate was worse for 'A' than for 'B', also by a factor of m.
## 
## There are thirty-five m > 1 for which this surprising result could have
## occurred, the smallest of which is 1476/1475.
## 
## What's the largest possible value of m?
## Give your answer as a fraction reduced to its lowest terms, in the
## form u/v.
## 
#-------------------------------------------------------------------------------
from fractions import Fraction
from time import time
#-------------------------------------------------------------------------------
def test(X0,Y0,x1,x2,m):
    for m1 in range(1,min(A[1]//x1.numerator,B[1]//x1.denominator)+1):
        for m2 in range(1,min(A[2]//x2.numerator,B[2]//x2.denominator)+1):
            X1 = m1*x1.numerator
            X2 = m2*x2.numerator
            Y1 = m1*x1.denominator
            Y2 = m2*x2.denominator
            if (X0+X1+X2) == S*m*(Y0+Y1+Y2):
                s.add(m)
                return
#-------------------------------------------------------------------------------
start = time()
A = [5248, 5760, 1312+2624+3936]
B = [640, 3776, 1888+3776+5664]
SA = sum(A)
SB = sum(B)
S = Fraction(SA,SB)
a = [Fraction(A[i],B[i]) for i in range(3)]
s = set([])

for X0 in range(59,A[0]+1,59):
    for Y0 in range(B[0]*X0//A[0],B[0]+1):
        x0=Fraction(X0,Y0)
        m = a[0]/x0
        if m in s or m<=1:
            continue
        x1 = a[1]/m
        x2 = a[2]/m
        test(X0,Y0,x1,x2,m)

L=list(s)   
L.sort()
print(f'Solution: {L[-1]}, Run-Time: {time()-start}')
#-------------------------------------------------------------------------------
# solution: 123/59
#-------------------------------------------------------------------------------
