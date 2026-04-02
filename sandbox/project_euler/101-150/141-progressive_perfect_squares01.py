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
from math import sqrt, isqrt
from time import time
################################################################################
def is_progressive(n):
    temp = []
    for d in range(2,n+1):
        q,r = divmod(n,d)
        if r*q == d*d:
            return True
    return False
################################################################################
start = time()
limit = 10**5
total = 0
sol_list = []
for n in range(1,isqrt(limit)):
    if is_progressive(n*n):
        total += n*n
        sol_list.append(n*n)

print(total)


################################################################################
#solution:
################################################################################
