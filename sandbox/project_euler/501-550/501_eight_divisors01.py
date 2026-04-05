#  -----------------------------------------------------------------------------
#  Eight Divisors 
#  Problem 501
#  https://projecteuler.net/problem=501
#  -----------------------------------------------------------------------------
from math import isqrt
from sympy import primerange, nextprime, primepi
from time import time
#  -----------------------------------------------------------------------------
def f1(N):
  count = 0
  for p in primerange(2,N+1):
    for q in primerange(nextprime(p),N//p+1):
      num_r = primepi(N//(p*q)) - primepi(q)
      if num_r > 0:
        count += num_r
      else:
        break
  return int(count)
#  -----------------------------------------------------------------------------
def f2(N):
  count = 0
  for p in primerange(2,N+1):
    for q in primerange(nextprime(p),N//p+1):
      if p**3*q <= N and p*q**3 <= N:
        count += 2
      elif p**3*q <= N:
          count += 1
      elif p*q**3 <= N:
          count += 1
      else:
        break
  return count
#  -----------------------------------------------------------------------------
def f3(N):
  count = 0
  for p in primerange(2,N+1):
      if p**7 <= N:
        count += 1
      else:
        return count
#  -----------------------------------------------------------------------------
def f(N):
  return f1(N) + f2(N) + f3(N)
#  -----------------------------------------------------------------------------
for exp in [2,3,6,9,12]:
  start = time()
  N = 10**exp
  print(f'For n = 10^{exp:2}: {f(N):13}, Run-Time: {time()-start:.3f}')
#  -----------------------------------------------------------------------------
#  solution: 197912312715
#  -----------------------------------------------------------------------------
