#  -----------------------------------------------------------------------------
#  Shifted Pythagorean Triples
#  Problem 730
#  https://projecteuler.net/problem=730
#  -----------------------------------------------------------------------------
from math import sqrt, gcd
from functools import lru_cache
import sys

sys.setrecursionlimit(10**4)

@lru_cache
def isqrt_ceil(n):
  x = int(sqrt(n))
  while x*x < n:
    x += 1
  return x

@lru_cache
def euler_730(m,n):
  res = 0
  for q in range(1,2*m+1):
    for p in range(1,q+1):
      gcd_pq = gcd(p,q)
      s = q*q + p*p
      r = isqrt_ceil(s)
      k = r*r - s
      while k <= m:
        if is_root(p,q,r) and gcd(r,gcd_pq) == 1:
          res += dfs(p,q,r,n)
        r += 1
        k = r*r - s
  return res

@lru_cache      
def is_root(p,q,r):
  u = 2*(p+q-r)
  return p >= u or q == u

@lru_cache
def dfs(p,q,r,n):
  res = 1
  g = 2*(p+q+r)
  d=g-p
  e=g-q
  f=g+r
  x = d+e+f - n 
  if x <= 0:
    res += dfs(d,e,f,n)
  p *= 2
  g = 2*p
  if x <= 5*p:
    res += dfs(d-p, e-g, f-g, n)
  q *= 2
  g = 2*q
  if p != q and x <= 5*q:
    res += dfs(d-g, e-q, f-g, n)
  return res

print(euler_730(10**2,10**8))
#  -----------------------------------------------------------------------------
#  solution: 1315965924
#  -----------------------------------------------------------------------------
