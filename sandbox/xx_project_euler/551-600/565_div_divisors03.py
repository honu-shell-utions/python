#  -----------------------------------------------------------------------------
#  Divisibility of sum of divisors
#  Problem 565
#  https://projecteuler.net/problem=565
#  -----------------------------------------------------------------------------
from sympy import primerange, isprime
from time import time

def euler_565(N,D=2017):
    T = lambda n: n*(n+1)//2
    Q = lambda n: n*T(N//n)

    limit = N//12101 
    # 12101 = smallest prime p such that 2017 divides p+1

    s = 0
    primes = []

    for p in primerange(2, N**0.5):
      q = p**2
      a,k = 1+p+q,2 
      while q <= N:
        if a % D == 0:
          s += Q(q)-Q(p*q)
          if q <= limit:
              primes += [q]
        q *= p 
        k += 1 
        a += q
        
    for p in range(4033, N+1, 4034):
      if isprime(p):
        s += Q(p)
        if p <= limit:
            primes += [p]

    primes.sort()
    for i in range(len(primes)):
      if primes[i]**2 > N:
          break
      for j in range(i, len(primes)):
        x = primes[i]*primes[j]
        if x > N:
            break
        s -= Q(x)

    return s
#  -----------------------------------------------------------------------------
print('-'*70)
print('Problem 565')
print('-'*70)
for exp in [6,9,11]:
  start = time()
  n = 10**exp
  print(f'S(n,d) = ({n:12},2017): {euler_565(n):20}, Run-Time: {time()-start:.3f}')
print('-'*70)
#  -----------------------------------------------------------------------------
#  solution: 2992480851924313898
#  -----------------------------------------------------------------------------
