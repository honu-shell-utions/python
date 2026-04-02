#-------------------------------------------------------------------------------
# Python Program to evaluate
# Mobius def M(N) = 1 if N = 1
# M(N) = 0 if any prime factor
# of N is contained twice
# M(N) = (-1)^(no of distinct
# prime factors)
# Python Program to
# evaluate Mobius def
# M(N) = 1 if N = 1
# M(N) = 0 if any
# prime factor of
# N is contained twice
# M(N) = (-1)^(no of
# distinct prime factors)
#-------------------------------------------------------------------------------
## Squarefree Numbers
## Problem 193
## A positive integer n is called squarefree,
## if no square of a prime divides n, thus
## 1, 2, 3, 5, 6, 7, 10, 11 are squarefree,
## but not 4, 8, 9, 12.
## 
## How many squarefree numbers are there below 2^50?
#-------------------------------------------------------------------------------
from sympy import isprime
from time import time
#-------------------------------------------------------------------------------
def mobius(N):
    # Base Case
    if (N == 1):
        return 1
    # For a prime factor i
    # check if i^2 is also
    # a factor.
    p = 0
    for i in range(1, N + 1):
        if (N % i == 0 and isprime(i)):
            # Check if N is
            # divisible by i^2
            if (N % (i * i) == 0):
                return 0
            else:
                # i occurs only once,
                # increase f
                p = p + 1
    # All prime factors are
    # contained only once
    # Return 1 if p is even
    # else -1
    if(p % 2 != 0) :
        return -1
    else :
        return 1
#-------------------------------------------------------------------------------
start = time()
count = 0
for i in range(1, 2**25):
    if mobius(i) != 0:
        count += 1
        if count % 10**4 == 0:
            print(i,count)
        
print(f'Solution: {count}, Run-Time: {time()-start}')
#-------------------------------------------------------------------------------
# solution: 684465067343069
#-------------------------------------------------------------------------------
