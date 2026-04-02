#  -----------------------------------------------------------------------------
#  2%ω(n)
#  Problem 675
#  https://projecteuler.net/problem=675
#  https://www.ivl-projecteuler.com/overview-of-problems/25-difficulty/problem-675
#  -----------------------------------------------------------------------------
from sympy import factorint
from math import factorial
from time import time
#  -----------------------------------------------------------------------------
def d(n):
    res = 1
    for f in factorint(n).values():
        res *= (2*f+1)
    return res
#  -----------------------------------------------------------------------------
def F(n):
    total = 0
    for i in range(2,n+1):
        total += (d(factorial(i)) % MOD)
    return total % MOD
#  -----------------------------------------------------------------------------
MOD = 10**9 + 87
for limit in [10,10**2,10**3,10**4]:
    start = time()
    solution = F(limit)
    print(f'Solution: {solution:10}, Run-Time: {time()-start:.2f}')
#  -----------------------------------------------------------------------------
# n = 10**1 -> 4821
# n = 10**2 -> 930751395
# n = 10**3 -> 822391759
# n = 10**4 -> 979435692
# n = 10**7 -> 416146418
#  -----------------------------------------------------------------------------
