#  -----------------------------------------------------------------------------
#  Pseudo Square Root
#  Problem 266
#  The divisors of 12 are: 1,2,3,4,6 and 12.
#  The largest divisor of 12 that does not exceed the square root of 12 is 3.
#  We shall call the largest divisor of an integer n that does not
#  exceed the square root of n the pseudo square root (PSR) of n.
#  It can be seen that PSR(3102) = 47.
#  
#  Let p be the product of the primes below 190.
#  Find PSR(p) mod 10^16.
#  -----------------------------------------------------------------------------
from itertools import chain, combinations
from sympy import primerange
from math import prod
from time import time
#  -----------------------------------------------------------------------------
def power_set(s):
  return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))
#  -----------------------------------------------------------------------------
start = time()
primes = list(primerange(2,190))
s1 = sorted(prod(s) for s in power_set(primes[:len(primes)//2]))
s2 = sorted(prod(s) for s in power_set(primes[len(primes)//2:]))
n = prod(primes)

best_root = 1
j = len(s2) - 1
for a in s1:
    while j >= 0 and (a * s2[j]) ** 2 > n:
        j -= 1
    if j >= 0:
        best_root = max(best_root, a * s2[j])

print(f'Solution: {best_root % (10 ** 16)}, Run-Time: {time()-start}')
#  -----------------------------------------------------------------------------
#  solution: 1096883702440585
#  -----------------------------------------------------------------------------
