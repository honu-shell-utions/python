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
from sympy import primerange

lim = 101
primes = list(primerange(2, lim))

prime_sum = [0] * lim
prime_sum[0] = 1
for p in primes:
    for j in range(p, lim):
        prime_sum[j] += prime_sum[j-p]
        
print(min(x for x in range(lim) if prime_sum[x] > 5000))

################################################################################
#solution: 71
################################################################################
