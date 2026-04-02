################################################################################
##Prime square remainders
##Problem 123
##
##Let pn be the nth prime: 2, 3, 5, 7, 11, ..., and
##let r be the remainder when (pn−1)^n + (pn+1)^n is divided by pn^2.
##
##For example, when n = 3, p3 = 5, and 4^3 + 6^3 = 280 ≡ 5 mod 25.
##
##The least value of n for which the remainder first exceeds 10^9 is 7037.
##
##Find the least value of n for which the remainder first exceeds 10^10.
################################################################################
from sympy import primerange
from time import time
################################################################################
start = time()
primes = list(primerange(2,10 ** 6))
for n in range(1, 1+len(primes)):
    p = primes[n-1]
    r = (pow(p-1, n, p**2) + pow(p+1, n, p**2)) % p**2
    if r > 10 ** 10:
        break
print(f'Solution: {n}, Run-Time: {time()-start:.3f}')
################################################################################
#solution: 21035
################################################################################
