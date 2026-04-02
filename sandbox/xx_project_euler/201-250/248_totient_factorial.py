#-------------------------------------------------------------------------------
## Numbers for which Euler’s totient function equals 13!
## Problem 248
## The first number n for which φ(n)=13! is 6227180929.
## 
## Find the 150,000th such number.
#-------------------------------------------------------------------------------
from math import factorial
from sympy import isprime
from time import time
#-------------------------------------------------------------------------------
start = time()
fact13 = factorial(13)
factors = []     # All factors n of 13! such that n+1 is prime
all_factors = [] # All factors of n
for p2 in range(0, 11):
  for p3 in range(0, 6):
    for p5 in range(0, 3):
      for p7 in range(0, 2):
        for p11 in range(0, 2):
          for p13 in range(0, 2):
            n = 2 ** p2 * 3 ** p3 * 5 ** p5 * 7 ** p7 * 11 ** p11 * 13 ** p13
            all_factors.append(n)
            if isprime(n+1) and n != 1:
              factors.append(n)

cache = {}
# Generate all the possible factorization of x with factors greater than min_x
def f(min_x, x):
  if x == 1: return [[]]
  key = (min_x, x)
  if key in cache: return cache[key]
  res = []
  for i in factors:
    if i <= min_x: continue
    if x % i == 0:
      tmp = f(i, x / i)
      for l in tmp:
        res.append(l + [i])
  cache[key] = res
  return res

res = []
for base in all_factors:
  tmp = f(0, base)
  for t_ in tmp:
    remainder = fact13 / base
    v = 1
    for t in t_:
      p = t + 1
      k = 1
      while remainder % p == 0:
        remainder /= p
        k += 1
      v *= p ** k
    if remainder == 1:
      res.append(v)
      res.append(2*v)
    elif remainder % 2 == 0:
      k = 1
      while remainder % 2 == 0:
        remainder /= 2
        k += 1
      v *= 2 ** k
      if remainder == 1:
        res.append(v)
res.sort()
#-------------------------------------------------------------------------------
print(f'Solution: {res[150000 - 1]}, Run-Time: {time()-start}')
#-------------------------------------------------------------------------------
# solution: 23507044290
#-------------------------------------------------------------------------------
