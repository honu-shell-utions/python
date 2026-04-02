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
from math import isqrt
from sympy import primerange
from time import time
# ----------------------------------------------------------------------------
def lps_ups(p1,p2):
    total = 0
    for x in range(p1**2+1,p2**2):
        if x > limit:
            break
        if (x % p1 == 0 and x % p2 != 0) or (x % p1 != 0 and x % p2 == 0):
            total += x
    return total
# ----------------------------------------------------------------------------
start = time()
limit = 10**3  #999966663333
total = 0
prime_list = list(primerange(2,isqrt(limit)+10))
prime_pairs = []
for j in range(len(prime_list)-1):
    prime_pairs.append((prime_list[j],prime_list[j+1]))
for p1, p2 in prime_pairs:
    total += lps_ups(p1,p2)
        
print(f'Solution: {total}, Run-Time: {time()-start}')
# ----------------------------------------------------------------------------
# solution: 1259187438574927161
# ----------------------------------------------------------------------------
