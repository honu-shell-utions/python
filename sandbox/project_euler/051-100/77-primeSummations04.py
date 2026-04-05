################################################################################
## Prime summations 
## Problem 77
## It is possible to write ten as the sum of primes in
## exactly five different ways:
##
## 7 + 3
## 5 + 5
## 5 + 3 + 2
## 3 + 3 + 2 + 2
## 2 + 2 + 2 + 2 + 2
##
## What is the first value which can be written
## as the sum of primes in over five thousand different ways?
################################################################################
from sympy import primefactors

l = [1, 0]
for n in range(2, 101):
    l.append(sum(sum(primefactors(k)) * l[n - k] for k in range(1, n + 1)) // n)

for ndx,n in enumerate(l):
    print(ndx,n)
    if n > 5000:
        break
################################################################################
#solution: 71
################################################################################
