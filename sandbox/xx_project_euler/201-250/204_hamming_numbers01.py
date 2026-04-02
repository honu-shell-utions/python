#-------------------------------------------------------------------------------
## Generalised Hamming Numbers
## Problem 204
## 
## A Hamming number is a positive number which has
## no prime factor larger than 5.
## 
## So the first few Hamming numbers are 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15.
## There are 1105 Hamming numbers not exceeding 10^8.
## 
## We will call a positive number a generalised Hamming number of type n,
## if it has no prime factor larger than n.
## 
## Hence the Hamming numbers are the generalised Hamming numbers of type 5.
## 
## How many generalised Hamming numbers of type 100 are there
## which don't exceed 10^9?
#-------------------------------------------------------------------------------
from sympy import primerange, factorint
from time import time
#-------------------------------------------------------------------------------
def is_hamming(n):
    temp = factorint(n)
    bases = list(temp.keys())
    for b in bases:
        if b not in ok_primes:
            return False
    return True
#-------------------------------------------------------------------------------
start = time()
ham_type = 5
hammings = 0
ok_primes = list(primerange(2,ham_type+1))

for n in range(1,10**8+1):
    if is_hamming(n):
        hammings += 1

print(f'Solution: {hammings}, Run-Time: {time()-start}')

#-------------------------------------------------------------------------------
# solution: 2944730
#-------------------------------------------------------------------------------
