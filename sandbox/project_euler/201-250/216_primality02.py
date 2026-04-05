#-------------------------------------------------------------------------------
## Investigating the primality of numbers of the form 2n^2-1
## Problem 216
## Consider numbers t(n) of the form t(n) = 2n^2-1 with n > 1.
## The first such numbers are 7, 17, 31, 49, 71, 97, 127 and 161.
## It turns out that only 49 = 7*7 and 161 = 7*23 are not prime.
## For n ≤ 10000 there are 2202 numbers t(n) that are prime.
## 
## How many numbers t(n) are prime for n ≤ 50,000,000 ?
#-------------------------------------------------------------------------------
from sympy import nextprime
from math import sqrt
from time import time
#-------------------------------------------------------------------------------
start = time()
num_primes = 0
n_max = 50*10**6

current_prime = 2
while True:
    temp = sqrt((current_prime+1)/2)
    if temp > n_max:
        break
    if int(temp) == temp:
        num_primes += 1
    current_prime = nextprime(current_prime)
    
print(f'Solution: {num_primes}, Run-Time: {time()-start}')
#-------------------------------------------------------------------------------
# solution: 5437849
#-------------------------------------------------------------------------------
