#  -----------------------------------------------------------------------------
#  2%ω(n)
#  Problem 675
#  https://projecteuler.net/problem=675
#  -----------------------------------------------------------------------------
from time import time

start = time()
LIMIT = 10**7+1; MOD = 10**9+87
smallest_factor = [0]*LIMIT

for p in range(2, LIMIT):
    if not smallest_factor[p]:
        for mult in range(p, LIMIT, p):
            if not smallest_factor[mult]:
                smallest_factor[mult] = p
                
ans= 0
prod = 1
decomposition = dict()

for i in range(2, LIMIT):
    tmp = i
    while tmp > 1:
        div = smallest_factor[tmp]
        old_pwr = decomposition.get(div, 0)
        prod *= pow(2*old_pwr + 1, MOD-2, MOD)  # `MOD` is prime
        prod *= (2*old_pwr + 3)
        prod %= MOD
        decomposition[div] = old_pwr + 1
        tmp //= div
    ans += prod
    ans %= MOD

print(f'Solution: {ans}, Run-Time: {time()-start}')
#  -----------------------------------------------------------------------------
#  solution: 416146418
#  -----------------------------------------------------------------------------
