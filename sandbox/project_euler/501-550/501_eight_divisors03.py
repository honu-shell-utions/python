"""
501_eight_divisors.py
https://projecteuler.net/problem=501

Eight Divisors
The eight divisors of 24 are 1, 2, 3, 4, 6, 8, 12 and 24. The ten numbers not
exceeding 100 having exactly eight divisors are:
24, 30, 40, 42, 54, 56, 66, 70, 78 and 88.

Let f(n) be the count of numbers not exceeding n with exactly eight divisors.

You are given f(100) = 10, f(1000) = 180 and f(10^6) = 224427.

Find f(10^12).

page 11
difficulty 40%
pe_ans = 197912312715

solution by fakesson Sweden
Used Meissel–Lehmer's algorithm with sieved primes up to
n^(2/3)
"""
from bisect import bisect
from functools import lru_cache
from math import sqrt
from sympy import primerange
from time import time


@lru_cache(maxsize=None)
def phi(x, a):
    if a == 1:
        return (x + 1) // 2
    return phi(x, a - 1) - phi(x // primes[a - 1], a - 1)

@lru_cache(maxsize=None)
def pi(x):
    if x < p_limit:
        return bisect(primes, x)
    a = pi(int(x ** (1 / 4)))
    b = pi(int(sqrt(x)))
    c = pi(int(x ** (1 / 3)))
    res = phi(x, a) + (b + a - 2) * (b - a + 1) // 2
    for i in range(a + 1, b + 1):
        w = x // primes[i - 1]
        b_i = pi(int(sqrt(w)))
        res -= pi(w)
        if i <= c:
            for j in range(i, b_i + 1):
                res -= pi(w // primes[j - 1]) - j + 1
    return res

def euler501():
    r = pi(int(nmax**(1 / 7)))
    for a in primes:
        if 2 * a * a * a > nmax:
            break
        r += pi(nmax // (a * a * a))
    r -= pi(int(nmax**(1 / 4)))
    pLen = len(primes)
    for i in range(pLen):
        a = primes[i]
        if a * a * a > nmax:
            break
        for j in range(i + 1, pLen):
            b = primes[j]
            if a * b * b > nmax:
                break
            r += pi(nmax // (a * b)) - pi(b)
    return r

#  -----------------------------------------------------------------------------
for exp in [2,3,6,9,12]:
  start = time()
  nmax = 10**exp
  p_limit = int(nmax**(2/3))
  primes = tuple(primerange(2, p_limit))
  tally = euler501()
  print(f'For n = 10^{exp:2}: {tally:13}, Run-Time: {time()-start:.3f}')
#  -----------------------------------------------------------------------------
