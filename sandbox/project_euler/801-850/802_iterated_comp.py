#  -----------------------------------------------------------------------------
#  Iterated Composition
#  Problem 802
#  https://projecteuler.net/problem=802
#  -----------------------------------------------------------------------------
from time import time
#  -----------------------------------------------------------------------------
start = time()
N = 10**7
MOD = 1020340567
is_prime = [1 for i in range(N + 1)]
mobius = [1 for i in range(N + 1)]
p = 2

while p <= N:
    for i in range(1, int(N / p) + 1):
        if i % p == 0:
            mobius[i * p] = 0
        else:
            mobius[i * p] *= -1
        is_prime[i * p] = 0
    p += 1
    while p <= N and not is_prime[p]:
        p += 1

sol = 0
for k in range(1, N+1):
    sol += mobius[k] * pow(2, int(N / k), MOD)
    sol %= MOD

print(f'Solution: {sol}, Run-Time: {time()-start:.4f}')
#  -----------------------------------------------------------------------------
#  solution: 973873727
#  -----------------------------------------------------------------------------
