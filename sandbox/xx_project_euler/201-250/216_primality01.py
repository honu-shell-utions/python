#-------------------------------------------------------------------------------
## Investigating the primality of numbers of the form 2n2-1
## Problem 216
## Consider numbers t(n) of the form t(n) = 2n^2-1 with n > 1.
## The first such numbers are 7, 17, 31, 49, 71, 97, 127 and 161.
## It turns out that only 49 = 7*7 and 161 = 7*23 are not prime.
## For n ≤ 10000 there are 2202 numbers t(n) that are prime.
## 
## How many numbers t(n) are prime for n ≤ 50,000,000 ?
#-------------------------------------------------------------------------------
from sympy import isprime
from time import time
#-------------------------------------------------------------------------------
def t(n):
    if n < 2:
        return 0
    else:
        return 2*n**2-1
#------------------------------------------------------------------------------
start = time()
num_primes = 0 
for n in range(1,50*10**6+1):
    if isprime(t(n)):
        num_primes += 1

print(f'Solution: {num_primes}, Run-Time: {time()-start}')
#-------------------------------------------------------------------------------
# solution: 5437849
#-------------------------------------------------------------------------------
