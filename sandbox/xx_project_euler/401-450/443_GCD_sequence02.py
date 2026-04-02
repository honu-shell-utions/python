#  -----------------------------------------------------------------------------
#  GCD sequence
#  Problem 443
#  https://projecteuler.net/problem=443
#  -----------------------------------------------------------------------------
from sympy import isprime
from time import time
from math import gcd
#  -----------------------------------------------------------------------------
def euler443(L):
  g = 13
  n = 4
  while n < L:
    if g == 3*n and isprime(2*n-1):
      x = 2*n-1
      if x <= L:
        n = 2*n-1
        g = 3*n
      else:
        y  = L-n
        n += y
        g += y
    else:
      n += 1
      g += gcd(n,g)
  return g
#  -----------------------------------------------------------------------------
for exp in range(2,16):
    start = time()
    N = 10**exp
    print(f'For n = 10^{exp:2}: {euler443(N):17}, Run-Time: {time()-start:.3f}')
#  -----------------------------------------------------------------------------
