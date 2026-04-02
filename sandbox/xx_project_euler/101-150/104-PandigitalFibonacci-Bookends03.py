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
def isPanBack(fib): 
    if set(str(fib % 10**9)) == target:
        return True
    else:
        return False
################################################################################
def isPanFront(fib):
    if set(str(fib)[:9]) == target:
        return True
    else:
        return False
################################################################################ 
start = time()
target = set('123456789')
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
