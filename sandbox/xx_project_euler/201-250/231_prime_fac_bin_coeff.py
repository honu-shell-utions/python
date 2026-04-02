## The prime factorisation of binomial coefficients
## Problem 231
## The binomial coefficient 

from sympy import primerange
from time import time

start = time()
n, r, s = 20*10**6, 15*10**6, 0

for p in primerange(2,n):
    pj = p
    while pj <= n:
        s += p * (n//pj - r//pj - (n - r)//pj)
        pj *= p

print(f'Solution: {s}, Run-Time: {time()-start}')

# 7526965179680
