#  -----------------------------------------------------------------------------
#  A polynomial modulo the square of a prime
#  Problem 457
#  https://projecteuler.net/problem=457
#  -----------------------------------------------------------------------------
from sympy import sqrt_mod, isprime, legendre_symbol, primerange
from time import time
#  -----------------------------------------------------------------------------
def euler_457(n):
    total = 0
    for p in primerange(3,n+1):
        if legendre_symbol(13, p) == 1:
            # square root modulo p
            t = sqrt_mod(13, p)
            # hensel lift to sqrt mod p^2
            r = t + p * (((13 - t**2) // p) * pow(2 * t, -1, p) % p)
            if r % 2 == 0:
                r = p * p - r
            total += (r + 3) // 2
    return total
#  -----------------------------------------------------------------------------
print('-'*70)
for exp in range(1,9):
    start = time()
    sol = euler_457(10**exp)
    if exp == 7:
        print('-'*70)
    print(f'Solution for n = 10^{exp:2}: {sol:24}, Run-Time: {time()-start:>10.3f}')
    if exp == 7:
        print('-'*70)
print('-'*70)
#  -----------------------------------------------------------------------------
#  solution: 2647787126797397063
#  -----------------------------------------------------------------------------
