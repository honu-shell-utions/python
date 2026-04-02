#-------------------------------------------------------------------------------
## An Arithmetic Geometric sequence
## Problem 235
## Given is the arithmetic-geometric sequence u(k) = (900-3k)r^(k-1).
## Let s(n) = the sum of u(k) for k=1...n.
##
## Find the value of r for which s(5000) = -600,000,000,000.
##
## Give your answer rounded to 12 places behind the decimal point.
#-------------------------------------------------------------------------------
from time import time
#-------------------------------------------------------------------------------
start = time()
sn = 5000
sm = -2 * 10**11
s, r, d = 0, 1, 0.1

while abs(s - sm) > 1:
  s = sum((300 - k) * r**(k-1) for k in range(1, sn+1))
  r += d if s > sm else -d
  d /= 2

print(f'Solution: {round(r,12)}, Run-Time: {time()-start}')
#-------------------------------------------------------------------------------
# solution: 1.002322108633
#-------------------------------------------------------------------------------
