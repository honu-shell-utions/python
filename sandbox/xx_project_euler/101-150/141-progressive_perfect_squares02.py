################################################################################
## Investigating progressive numbers, n, which are also square
## Problem 141
## A positive integer, n, is divided by d and the quotient and
## remainder are q and r respectively. In addition d, q, and r
## are consecutive positive integer terms in a geometric sequence,
## but not necessarily in that order.
##
## For example, 58 divided by 6 has quotient 9 and remainder 4.
## It can also be seen that 4, 6, 9 are consecutive terms in a
## geometric sequence (common ratio 3/2).
##
## We will call such numbers, n, progressive.
##
## Some progressive numbers, such as 9 and 10404 = 1022, happen
## to also be perfect squares.
##
## The sum of all progressive perfect squares below one hundred thousand is 124657.
##
## Find the sum of all progressive perfect squares below one trillion (10^12).
################################################################################
from math import sqrt, gcd
from time import time
################################################################################
def is_square(n):
    root = sqrt(n)
    if (int(root+0.5))**2 == n:
        return True
    else:
        return False
################################################################################
start = time()
limit = 10**12
c_limit = 10**4
progressive_squares = set()

for a in range(2, c_limit):
    for b in range(1,a):
        k = 1
        if a**3*b*k**2 + b**2*k >= limit:
            break
        if gcd(a, b) > 1:
            continue
        while True:
            n = a**3*b*k**2 + b**2*k
            if n >= limit:
                break
            if is_square(n):
                progressive_squares.add(n)
            k += 1

print('The solution:',sum(progressive_squares),'Run Time:',time()-start)
################################################################################
#solution: 878454337159
################################################################################
