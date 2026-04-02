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
ps = list(primerange(2,10**6))
LIMIT = 10 ** 10
for i, p in enumerate(ps):
    if i > 0 and i < len(ps) - 1:
        mod = pow(p, 2)
        a = pow(p - 1, i, mod)
        b = pow(p + 1, i, mod)
        r = (a + b) % mod
        if r > LIMIT:
            break
print(f'Solution: {i}, Run-Time: {time()-start:.3f}')
################################################################################
#solution: 21035
################################################################################
