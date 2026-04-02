#-------------------------------------------------------------------------------
## Divisor Square Sum
## Problem 211
## For a positive integer n, let σ2(n) be the sum of
## the squares of its divisors. For example,
## 
## σ2(10) = 1 + 4 + 25 + 100 = 130.
## Find the sum of all n, 0 < n < 64,000,000 such
## that σ2(n) is a perfect square.
#-------------------------------------------------------------------------------
from sympy import divisors
from math import sqrt, isqrt
from time import time
#-------------------------------------------------------------------------------
def is_keeper(n):
    divs = divisors(n)
    div_square_sum = 0
    for d in divs:
        div_square_sum += d**2
    if sqrt(div_square_sum) == isqrt(div_square_sum):
        return True
    return False
#-------------------------------------------------------------------------------
start = time()
limit = 64*10**6
solution = 0
for n in range(1,limit):
    if is_keeper(n):
        solution += n
    
print(f'Solution: {solution}, Run-Time: {time()-start}')
#-------------------------------------------------------------------------------
# solution: 1922364685
#-------------------------------------------------------------------------------
