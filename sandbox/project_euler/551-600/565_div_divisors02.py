#  -----------------------------------------------------------------------------
#  Divisibility of sum of divisors
#  Problem 565
#  https://projecteuler.net/problem=565
#  -----------------------------------------------------------------------------
from time import time
from math import isqrt
from itertools import count
from sympy import isprime, primerange
#  -----------------------------------------------------------------------------
def S(n,d):
    L= set() # primes list: p, p^2, p^3,...
    for m in count(d*2,d*2):
        if isprime(m-1):
            m1 = m - 1
            for j in range(1, (n // m1) + 1):
                if j % m1 != 0:
                    L.add(m1*j)
        if m > n:
            break

    PL = list(primerange(2, isqrt(n) + 1))
    for i in count(2):
        mmj = 0
        for m in PL:
            if (sum(m**j for j in range(0,i+1))) % d==0:
                mm = m**i
                for j in range(1, (n // mm) + 1):
                    if j % m != 0:
                        L.add(mm*j)
                        mmj += 1
                    if m ** i > n:
                        break
        if mmj == 0:
            break
    return sum(L)
#  -----------------------------------------------------------------------------
print('-'*70)
print('Problem 565')
print('-'*70)
for n,d in [(20,7),(10**6,2017),(10**9,2017),(10**11,2017)]:
  start = time()
  print(f'S(n,d) = ({n:12},{d:5}): {S(n,d):20}, Run-Time: {time()-start:.3f}')
print('-'*70)

#  -----------------------------------------------------------------------------
#  solution: 2992480851924313898
#  -----------------------------------------------------------------------------
