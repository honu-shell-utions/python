#  -----------------------------------------------------------------------------
#  Divisibility of factorials
#  Problem 549
#  https://projecteuler.net/problem=549
#  -----------------------------------------------------------------------------
from math import log
from sympy import primerange
from time import time
#  -----------------------------------------------------------------------------
# find minimal d for powers of p
def findmind(N, p):
    e = int(log(N) / log(p))
    t = [1] * (e + 1)
    t[0] = 0
    n = p
    while n <= e:
        for m in range(n, e + 1, n):
            t[m] += 1
        n *= p
    d = []
    i, k = 0, 1
    for n in t:
        for j in range(n):
            d.append(p * i)
            k += 1
        if k > e:
            break
        i += 1
    return d[:e]
#  -----------------------------------------------------------------------------
start = time()
N = 10 ** 8
S = [0] * (N + 1)
P = list(primerange(2, N + 1))
#sieve
for p in P:
    f = p
    for m in findmind(N, p):
        for n in range(f, N + 1, f):
            S[n] = max(m, S[n])
        f *= p
print(f'Solution: {sum(S)}, Run-Time: {time()-start}')
#  -----------------------------------------------------------------------------
#  solution: 476001479068717
#  -----------------------------------------------------------------------------
