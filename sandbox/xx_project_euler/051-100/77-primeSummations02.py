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
from itertools import count
from sympy import nextprime

for sum_value in count(1):
    p = nextprime(1)
    ways = [1] + [0] * sum_value
    while p <= sum_value:
        for i in range(p, sum_value + 1):
            ways[i] += ways[i - p]
        p = nextprime(p)
    if ways[sum_value] > 5000:
        break

print(sum_value)

################################################################################
#solution: 71
################################################################################
