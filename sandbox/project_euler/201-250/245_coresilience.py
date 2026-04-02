#-------------------------------------------------------------------------------
## Coresilience
## Problem 245
#-------------------------------------------------------------------------------
from sympy.ntheory.factor_ import totient
from sympy import isprime
from fractions import Fraction
from time import time
from math import sqrt, isqrt
#-------------------------------------------------------------------------------
def coresilience(n):
    return Fraction(n - totient(n),n-1)
#-------------------------------------------------------------------------------
start = time()
limit = 2*10**11
total = 0
for n in range(5,limit+1,2):
    if sqrt(n) == isqrt(n) or isprime(n):
        continue
    res = coresilience(n)
    if res.numerator == 1:
        total += n
        print(n)

print(f'Solution: {total}, Run-Time: {time()-start}')
#-------------------------------------------------------------------------------
# solution: 288084712410001
#-------------------------------------------------------------------------------
