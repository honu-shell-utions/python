################################################################################
# 104-PandigitalFibonacciBookends.py
#
# The Fibonacci sequence is defined by the recurrence relation:
# F(n) = F(n−1) + F(n−2), where F(1) = 1 and F(2) = 1.
# It turns out that F(541), which contains 113 digits, is the first Fibonacci
# number for which the last nine digits are 1-9 pandigital (contain all the
# digits 1 to 9, but not necessarily in order). And F(2749), which contains 575
# digits, is the first Fibonacci number for which the first nine digits are 1-9
# pandigital.
#
# Given that F()k is the first Fibonacci number for which the first nine digits
# AND the last nine digits are 1-9 pandigital, find k.
################################################################################
from sympy import fibonacci
from time import time
################################################################################
def isPanFront(fib):
    tempSet = set()
    strList = str(fib)[:9]
    for c in strList:
        tempSet.add(c)
        
    if len(tempSet) == 9 and '0' not in tempSet:
        return True
    else:
        return False
################################################################################
def isPanBack(fib):
    tempSet = set()
    for k in range(1,10):
        tempSet.add(fib % 10)
        fib //= 10

    if len(tempSet) == 9 and 0 not in tempSet:
        return True
    else:
        return False
################################################################################ 
start = time()
k = 2750
while True:
    testFib = fibonacci(k)
    if isPanBack(testFib):
        if isPanFront(testFib):
            print('The solution is:',k,'Run Time:',time()-start)
            break
    k += 1
################################################################################
#solution: 329468
################################################################################
