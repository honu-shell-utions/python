#-------------------------------------------------------------------------------
## Ambiguous Numbers 
## Problem 198
## A best approximation to a real number x for the denominator bound d
## is a rational number r/s (in reduced form) with s ≤ d, so that any
## rational number p/q which is closer to x than r/s has q > d.
## 
## Usually the best approximation to a real number is uniquely
## determined for all denominator bounds. However, there are
## some exceptions, e.g. 9/40 has the two best approximations 
## 1/4 and 1/5 for the denominator bound 6. We shall call a real number 
## x ambiguous, if there is at least one denominator bound for which 
## x possesses two best approximations. Clearly, an ambiguous number
## is necessarily rational.
## 
## How many ambiguous numbers x = p/q, 0 < x < 1/100, are there whose denominator 
## q does not exceed 10^8?
#-------------------------------------------------------------------------------
from time import time
#-------------------------------------------------------------------------------
start = time()
bound = 10**8
states = [(0,1,1,50)]
total = 0
while len(states) != 0:
    a,b,c,d = states.pop()
    if 2*b*d <= bound:
        states.append((a,b,a+c,b+d))
        states.append((a+c,b+d,c,d))
        if 100*(a*d + b*c) < 2*b*d:
            total += 1

print(f'Solution: {total}, Run-Time: {time() - start}')
#-------------------------------------------------------------------------------
# solution: 52374425 
#-------------------------------------------------------------------------------
