#-------------------------------------------------------------------------------
## Totient Chains
## Problem 214
## Let φ be Euler's totient function, i.e. for a natural number n,
## φ(n) is the number of k, 1 ≤ k ≤ n, for which gcd(k,n) = 1.
## 
## By iterating φ, each positive integer generates a decreasing
## chain of numbers ending in 1.
## 
## E.g. if we start with 5 the sequence 5,4,2,1 is generated.
## Here is a listing of all chains with length 4:
## 
##             5,4,2,1
##             7,6,2,1
##             8,4,2,1
##             9,6,2,1
##             10,4,2,1
##             12,4,2,1
##             14,6,2,1
##             18,6,2,1
##             
## Only two of these chains start with a prime, their sum is 12.
## 
## What is the sum of all primes less than 40,000,000 which
## generate a chain of length 25?
#-------------------------------------------------------------------------------
from sympy import primerange
from sympy.ntheory.factor_ import totient
from time import time
#-------------------------------------------------------------------------------
start = time()
primes = primerange(2,40*10**6)
total = 0
counter = 0
chain_size = 25
for current in primes:
    phi_list = [current]
    while True:
        current = totient(current)
        phi_list.append(current)
        if current == 1:
            break
        
    if len(phi_list) == chain_size:
        #print(phi_list)
        total += phi_list[0]
        counter += 1

print(f'Solution: {total} Count: {counter}, Run-Time: {time()-start}')
#-------------------------------------------------------------------------------
# solution: 1677366278943
#-------------------------------------------------------------------------------
