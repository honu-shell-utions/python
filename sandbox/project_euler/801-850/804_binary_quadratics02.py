#  -----------------------------------------------------------------------------
## Counting Binary Quadratic Representations
## Problem 804
## https://projecteuler.net/problem=804
# x^2 + xy + 41*y^2 = (x + y/2)^2 + (41 - 1/4)y^2
#  -----------------------------------------------------------------------------
from time import time
from math import floor, ceil, sqrt
#  -----------------------------------------------------------------------------
def f(N):
    T = 2*floor(sqrt(N))
    y = 1
    while True:
        n = N - 40.75*y*y
        if n < 0:
            break
        r = sqrt(n)
        x1 = ceil(-r - 0.5*y)
        x2 = floor(r - 0.5*y)
        T += 2*(x2 - x1 + 1)
        y += 1           
    return T    
#  -----------------------------------------------------------------------------
for exp in range(1,17):
    start = time()
    solution = f(10**exp)
    print(f'Solution for n = 10^{exp:2}: {solution}, Run-Time: {round(time()-start,6)}')
#  -----------------------------------------------------------------------------
#  N = 10**3  # Answer: 474
#  N = 10**6  # Answer: 492128
#  N = 10**16  # Answer: 4921370551019052
#  -----------------------------------------------------------------------------
