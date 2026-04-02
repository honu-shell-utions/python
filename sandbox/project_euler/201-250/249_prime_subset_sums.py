#-------------------------------------------------------------------------------
## Prime Subset Sums                
## Problem 249
## Let S = {2, 3, 5, ..., 4999} be the set of prime numbers less than 5000.
## 
## Find the number of subsets of S, the sum of whose elements is a prime number.
## Enter the rightmost 16 digits as your answer.
#-------------------------------------------------------------------------------
from sympy import primerange, isprime
from collections import defaultdict
from time import time
#-------------------------------------------------------------------------------
def euler_249(limit = 5000):
    ss = defaultdict(int)
    ss[0] = 1 # empty set
    for p in primerange(2,limit):
        for s in sorted(ss.keys(), reverse=True):
            ss[s+p] += ss[s]
    return sum(ss[s] for s in ss if isprime(s))

start = time()
temp = str(euler_249())[-16:]
print(f'Solution: {temp}, Run-Time: {time()-start}')
#-------------------------------------------------------------------------------
# solution: 9275262564250418
#-------------------------------------------------------------------------------
