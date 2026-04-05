#  ----------------------------------------------------------------------------
#  Idempotents
#  Problem 407
#  https://projecteuler.net/problem=407
#  ----------------------------------------------------------------------------
from time import time
from collections import defaultdict
from functools import reduce
from itertools import combinations
from operator import mul
#  ----------------------------------------------------------------------------
def factorize(n):
    n = n + 1
    f = defaultdict(list)
    t = list(range(n))
    for p in range(2, n):
        if p not in f:
            t[p] = p - 1
            for i in range(p + p, n, p):
                j, k = i, 1
                while j % p == 0:
                    j //= p
                    k *= p
                f[i].append(k)
                t[i] = t[i] * (p - 1) // p
    return f, t
#  ----------------------------------------------------------------------------
def problem407(n):
    f, t = factorize(n + 1)
    yield 0 # i = 1
    for i in range(2, n + 1):
        if i not in f or len(f[i]) < 2:
            # prime or prime power
            yield 1
            continue
        def uw():
            for j in range(1, len(f[i])):
                for c in combinations(f[i], j):
                    u = reduce(mul, c)
                    v = i // u
                    w = pow(u, t[v] - 1, v)
                    yield u * w
        yield max(uw())
#  ----------------------------------------------------------------------------
for exp in [2,3,4,5,6,7]:
    start = time()
    solution = 0
    gen = problem407(10**exp)
    for s in gen:
      solution += s
    print(f'Solution: {solution}, Run-Time: {time()-start}')
#  ----------------------------------------------------------------------------
#  solution: 39782849136421
#  ----------------------------------------------------------------------------
