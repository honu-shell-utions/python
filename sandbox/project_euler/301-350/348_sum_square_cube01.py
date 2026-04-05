#  -----------------------------------------------------------------------------
#  Sum of a square and a cube
#  Problem 348
#  https://projecteuler.net/problem=348
#  -----------------------------------------------------------------------------
from math import isqrt
from time import time
#  -----------------------------------------------------------------------------
def find(limit):
    sols = {}
    for x in range(2,isqrt(limit)+1):
        for y in range(2,int(limit**(1/3))+1):
            val = x**2 + y**3
            if str(val) == str(val)[::-1]:
                if val in sols:
                    sols[val] += 1
                else:
                    sols[val] = 1
    return sols
#  -----------------------------------------------------------------------------
start = time()
sols = find(10**9)
total = 0
for p,count in sols.items():
    if count == 4:
        total += p
print(f'Solution: {total}, Run-Time: {time()-start}')
#  -----------------------------------------------------------------------------
#  solution: 1004195061
#  -----------------------------------------------------------------------------
