from sympy import nextprime
from time import time
from math import isqrt

start = time()
limit = 10**8
count = 0
stop1 = isqrt(limit)+1
stop2 = limit//2
p1 = 1
while p1 < stop1:
    p1 = nextprime(p1)
    p2 = p1
    while p2 < stop2:
        if p1*p2 < limit:
            count += 1
        else:
            break
        p2 = nextprime(p2)


print(f'Solution: {count}, Run-Time: {time()-start}')
#solution: 17427258
