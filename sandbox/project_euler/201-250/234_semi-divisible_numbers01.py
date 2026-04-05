# ----------------------------------------------------------------------------
# 234_semi-divisible_numbers.py
#
# problem 234: semi-divisible numbers
# For an integer n ≥ 4, we define the lower prime square root of n, denoted by
# lps(n), as the largest prime ≤ √n and the upper prime square root of n,
# ups(n), as the smallest prime ≥ √n.
#
# So, for example, lps(4) = 2 = ups(4), lps(1000) = 31, ups(1000) = 37. Let us
# call an integer n ≥ 4 semi-divisible, if one of lps(n) and ups(n) divides n,
# but not both.
#
# The sum of the semi-divisible numbers not exceeding 15 is 30, the numbers are
# 8, 10 and 12
#
# 15 is not semi-divisible because it is a multiple of both lps(15) = 3
# and ups(15) = 5
#
# As a further example, the sum of the 92 semi-divisible numbers up to 1000
# is 34825
#
# What is the sum of all semi-divisible numbers not exceeding 999966663333?
# ans == 1259187438574927161
# ----------------------------------------------------------------------------
from sympy import primerange
from time import time
from math import isqrt
# ----------------------------------------------------------------------------
start = time()
nmax = 999966663333
primes = list(primerange(2,isqrt(nmax)+1))
sum_semi = 0

for i in range(len(primes) - 1):
    n = primes[i] ** 2
    if n > nmax:
        break 
    n += primes[i]
    while n < primes[i+1] ** 2:
        if n <= nmax and n % primes[i+1]:
            sum_semi += n
        n += primes[i]
        
    n = primes[i+1] ** 2 - primes[i+1]
    while n > primes[i] ** 2:
        if n <= nmax and n % primes[i]:
            sum_semi += n
        n -= primes[i+1]

print(f'Solution: {sum_semi}, Run-Time: {time()-start}')
# ----------------------------------------------------------------------------
# solution: 1259187438574927161
# ----------------------------------------------------------------------------
