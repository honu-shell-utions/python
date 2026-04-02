#  -----------------------------------------------------------------------------
#  Eight Divisors 
#  Problem 501
#  https://projecteuler.net/problem=501
#  -----------------------------------------------------------------------------
from time import time
from sympy import primerange, nextprime
from sympy import primepi as pi
from sympy.ntheory.factor_ import totient as phi
#  -----------------------------------------------------------------------------
def euler_501(N):

  # p^7
  count = pi(int(N**(1/7)))   

  # q*p^3
  for p in primerange(2,N):        
    if p**3 > N:
      break
    x = N//(p**3)
    count += pi(x)-(p<=x)

  # p*q*r
  for p in primerange(2,N):
    if p**3 > N:
      break
    for q in primerange(nextprime(p),N):
      if p*q**2 > N:
        break
      count += pi(N//(p*q))-pi(q)

  return int(count)
#  -----------------------------------------------------------------------------
for exp in [2,3,6,9,12]:
  start = time()
  N = 10**exp
  print(f'For n = 10^{exp:2}: {euler_501(N):13}, Run-Time: {time()-start:.3f}')
#  -----------------------------------------------------------------------------
#  solution: 197912312715
#  -----------------------------------------------------------------------------
