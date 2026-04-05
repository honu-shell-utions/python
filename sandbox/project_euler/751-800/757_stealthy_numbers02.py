#  -----------------------------------------------------------------------------
#  Stealthy Numbers
#  Problem 757
#  https://projecteuler.net/problem=757
#  -----------------------------------------------------------------------------
from time import time
from math import sqrt
#  -----------------------------------------------------------------------------
for limit in [10**6,10**14]:
    start = time()
    solutions = set()
    mx = int(limit**0.25)+1
    for x in range (1,mx):
        my = int(sqrt((limit/x/(x+1))))+1
        for y in range (x,my):
            tmp = x*(x+1)*y*(y+1)
            if tmp <= limit:
                solutions.add(tmp)                  
    print(f'Solution for n = {limit}: {len(solutions)}, Run-Time: {time()-start}')
#  -----------------------------------------------------------------------------
#  solution for 10**14 = 75737353
#  solution for 10**6 = 2851
#  -----------------------------------------------------------------------------
