#-------------------------------------------------------------------------------
## The hyperexponentiation of a number
## Problem 188
## The hyperexponentiation or tetration of a number a
## by a positive integer b, denoted by a↑↑b or ba,
## is recursively defined by:
## 
## a↑↑1 = a,
## a↑↑(k+1) = a^(a↑↑k).
## 
## Thus we have e.g. 3↑↑2 = 3^3 = 27, hence
## 3↑↑3 = 3^27 = 7625597484987 and 3↑↑4 is roughly 10^3.6383346400240996*10^12.
## 
## Find the last 8 digits of 1777↑↑1855.
#-------------------------------------------------------------------------------
from time import time
#-------------------------------------------------------------------------------
def tetration(base, n):
    """ Tetration, ^nx, by loop over decreasing exponent counter. """
    if n == 0:
        return 1
    new_base = base
    while n > 1:
        new_base = pow(base,new_base,10**8)
        n -= 1
    return new_base

start = time()
#-------------------------------------------------------------------------------
print(f'Solution: {tetration(1777, 1855)}, Run-Time: {time()-start}')
#-------------------------------------------------------------------------------
#solution: 95962097
#-------------------------------------------------------------------------------
