#-------------------------------------------------------------------------------
##  Resilience
##  Problem 243
##  A positive fraction whose numerator is less than its denominator
##  is called a proper fraction.
##  
##  For any denominator, d, there will be d−1 proper fractions; for
##  example, with d = 12:
##      
##  1/12 , 2/12 , 3/12 , 4/12 , 5/12 , 6/12 , 7/12 , 8/12 , 9/12 , 10/12 , 11/12 .
##  
##  We shall call a fraction that cannot be cancelled down a
##  resilient fraction.
##  Furthermore we shall define the resilience of a denominator,
##  R(d), to be the ratio of its proper fractions that are resilient;
##  for example, R(12) = 4/11 .
##  
##  In fact, d = 12 is the smallest denominator having a resilience R(d) < 4/10 .
##  
##  Find the smallest denominator d, having a resilience R(d) < 15499/94744 .
#-------------------------------------------------------------------------------
from fractions import Fraction
from time import time
#-------------------------------------------------------------------------------
def is_reduced(num,den):
    temp = Fraction(num,den)
    if num == temp.numerator:
        return True
    else:
        return False
#-------------------------------------------------------------------------------
def R(n):
    count = 0
    for k in range(1,n):
        if is_reduced(k,n):
            count += 1
    return Fraction(count,n-1)

#-------------------------------------------------------------------------------
start = time()
d = 2
while True:
    if R(d) < Fraction(4/10):
        print(f'Solution: {d}, Run-Time: {time()-start}')
        break
    else:
        d += 1
#-------------------------------------------------------------------------------
# solution: 892371480
#-------------------------------------------------------------------------------
