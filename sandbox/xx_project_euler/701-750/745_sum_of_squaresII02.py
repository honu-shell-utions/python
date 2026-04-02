#  -----------------------------------------------------------------------------
#  Sum of Squares II
#  Problem 745
#  https://projecteuler.net/problem=745
#  
#  The basic idea was to generate a list of 10^7 zeroes,
#  then cycle x through the integers from 1 to 10^7, increment
#  their entries by their square, and then decrement the
#  entries of all other multiples of the integer by this new value.
#  At this stage, we add floor((10^14)/x) * (xth entry)
#  to the total. Two minute runtime in the end.
#  
#  (This was far from my first attempt; naive methods
#   hit a wall, and I was rather puzzled that this was
#   labeled as a 10% problem... is the rating based
#   primarily on some function of the first 100 solution times?)
#  -----------------------------------------------------------------------------
#import math
from time import time
#  -----------------------------------------------------------------------------
def euler_745(limit):
    cap = limit
    sqarr = [0]*(cap+1)
    bigcap = cap**2
    total = 0
    for x in range(1,cap+1):
        t = x**2
        sqarr[x] += t
        for y in range(2*x,cap+1,x):
            sqarr[y] -= sqarr[x]
        total += bigcap//t * sqarr[x]
        total %= MOD
    return total
#  -----------------------------------------------------------------------------        
MOD = 1000000007
for exp in range(1,8):
    start = time()
    N = 10**exp
    print(f'Solution for n = 10^{2*exp:2}, {euler_745(N):9}, Run-Time: {time()-start:>10.3f}')
#  -----------------------------------------------------------------------------
#  solution: 94586478
#  -----------------------------------------------------------------------------
