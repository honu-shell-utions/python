#-------------------------------------------------------------------------------
## Squarefree Binomial Coefficients 
## Problem 203
#-------------------------------------------------------------------------------
from math import factorial
from sympy import nextprime
from time import time
#-------------------------------------------------------------------------------
def n_r(n,r):
    return factorial(n)//(factorial(r)*factorial(n-r))
#-------------------------------------------------------------------------------
def bin_coefficients(rows):
    distinct_nums = set()
    for r in range(rows):
        for c in range(r+1):
            distinct_nums.add(n_r(r,c))
    return distinct_nums
#-------------------------------------------------------------------------------
# A positive integer n is called squarefree if no square
# of a prime divides n
def sum_sf_nums(nums):
    bad_total = 0
    for n in nums:
        current_prime = 2
        while current_prime**2 <= n:
            if n % current_prime**2 == 0:
                bad_total += n
                break
            current_prime = nextprime(current_prime)
    return sum(nums) - bad_total
#-------------------------------------------------------------------------------
start = time()
nums = bin_coefficients(51)
sf_sum = sum_sf_nums(nums)
print(f'Solution: {sf_sum}, Run-Time: {time()-start}')
#-------------------------------------------------------------------------------
# solution: 34029210557338
#-------------------------------------------------------------------------------
