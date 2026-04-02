#-------------------------------------------------------------------------------
## Alexandrian Integers
## Problem 221
## We shall call a positive integer A an "Alexandrian integer",
## if there exist integers p, q, r such that:
## 
## A = p*q*r
## 
## and
##  
## 1/A = 1/p + 1/q + 1/r
## 
## For example,
## 630 is an Alexandrian integer (5,-7,-18).
## 
## In fact, 630 is the 6th Alexandrian integer,
## the first 6 Alexandrian integers being:
## 6, 42, 120, 156, 420, and 630.
## 
## Find the 150,000th Alexandrian integer.
#-------------------------------------------------------------------------------
from math import isqrt
from time import time
#-------------------------------------------------------------------------------
def divs(n):
    divs = []
    for i in range(1, isqrt(n) + 1):
        if n % i == 0:
            divs.append(i)
    return divs
#-------------------------------------------------------------------------------
def euler_221(n):
    alexandrian_integers = []
    p = 1
    while True:
        for k in divs(p*p + 1):
            temp = p*(p + k)*((p*p + 1)//k + p)
            alexandrian_integers.append(temp)
        p += 1
        if len(alexandrian_integers) > 5*10**5:
            return sorted(alexandrian_integers)
#-------------------------------------------------------------------------------
start = time()
sols = euler_221(15*10**4)
print(f'Solution: {sols[149999]}, Run-Time: {time()-start}')
#-------------------------------------------------------------------------------
# solution: 1884161251122450
#-------------------------------------------------------------------------------
