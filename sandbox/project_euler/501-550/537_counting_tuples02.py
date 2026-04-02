#  -----------------------------------------------------------------------------
#  Counting tuples
#  Problem 537
#  https://projecteuler.net/problem=537
#  -----------------------------------------------------------------------------
from time import time
from sympy import nextprime
from functools import lru_cache
#  -----------------------------------------------------------------------------
def get_spacing(n):
    z = [0]*(n+1)
    z[0] = 1
    current_prime = 2
    for k in range(1,n+1):
        next_prime = nextprime(current_prime)
        spacing = next_prime - current_prime
        z[k]= spacing
        current_prime = next_prime
    return z
#  -----------------------------------------------------------------------------
@lru_cache(maxsize=None)
def T(n, k):
    if n == 1:
        return prime_spacing[k]
    total = 0
    s = n//2
    for a in range(k+1):
        b = k - a
        total += (T(s,a)*T(n-s,b)) % MOD
    return total % MOD
#  -----------------------------------------------------------------------------
MOD = 1004535809
for N in [3,10,10**3,20*10**3]:
    start = time()
    prime_spacing = get_spacing(N)
    print(f'Solution for N = {N:6}: {T(N,N):10}, Run-Time: {time()-start:.2f} seconds.')
#  -----------------------------------------------------------------------------
#  solution: 779429131
#  -----------------------------------------------------------------------------
