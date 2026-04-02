#-------------------------------------------------------------------------------
## Rounded Square Roots
## Problem 255
## https://projecteuler.net/problem=255
#-------------------------------------------------------------------------------
from math import floor, ceil
from time import time
#-------------------------------------------------------------------------------
def heron(n):
    d = len(str(n))
    if d % 2 == 1:
        x0 = 2*10**((d-1)/2)
    else:
        x0 = 7*10**((d-2)/2)

    iterations = 0
    while True:
        iterations += 1
        x1 = floor((x0 + ceil(n/x0))/2)
        if x0 == x1:
            break
        x0 = x1
        
    return iterations
#-------------------------------------------------------------------------------
for D in [5,6,10,12,14]:
    start = time()
    begin = 10**(D-1)
    end = 10**D
    total_it = 0
    for k in range(begin,end):
        total_it += heron(k)
    print(f'Solution: {round(total_it/(end-begin),10)}, Run-Time: {time()-start}')

#-------------------------------------------------------------------------------
#D = 5  # Answer: 3.2102888889
#D = 6  # Answer: 3.3431844444
#D = 10  # Answer: 3.9456584348
#D = 12  # Answer: 4.2038288238
#D = 14  # Answer: 4.4474011180
#-------------------------------------------------------------------------------
