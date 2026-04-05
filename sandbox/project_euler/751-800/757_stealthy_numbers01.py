#  -----------------------------------------------------------------------------
#  Stealthy Numbers
#  Problem 757
#  https://projecteuler.net/problem=757
#  -----------------------------------------------------------------------------
from itertools import combinations
from time import time
from sympy import divisors
from math import sqrt, isqrt
#  -----------------------------------------------------------------------------
def is_stealthy(n):
    divs = divisors(n)
    combos = []
    temp = combinations(divs,2)
    if isqrt(n) == sqrt(n):
        combos.append((isqrt(n),isqrt(n)))
    for x,y in temp:
        if x*y == n:
            combos.append((x,y))
    for a,b in combos:
        for c,d in combos:
            if a*b == c*d and a+b == c+d+1:
                return True
#  -----------------------------------------------------------------------------
start = time()
count = 0
limit = 10**6
for n in range(limit+1):
    if is_stealthy(n):
        count += 1

print(f'Solution: {count}, Run-Time: {time()-start}')
#  -----------------------------------------------------------------------------
#  solution for 10**6 = 2851
#  -----------------------------------------------------------------------------
