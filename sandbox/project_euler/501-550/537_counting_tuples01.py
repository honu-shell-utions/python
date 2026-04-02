#  -----------------------------------------------------------------------------
#  Counting tuples
#  Problem 537
#  https://projecteuler.net/problem=537
#  -----------------------------------------------------------------------------
from time import time
from sympy import primepi
from itertools import product
#  -----------------------------------------------------------------------------
def make_dict(n):
    temp = {}
    k = 0
    while True:
        k += 1
        pk = primepi(k)
        if pk <= n:
            temp.update({k:pk})
        else:
            break
    return temp
#  -----------------------------------------------------------------------------
def T(n,k):
    hits = 0
    pd = make_dict(n)
    perms = product(pd,repeat=k)
    for perm in perms:
        total = 0
        for p in perm:
            total += pd[p]
        if total == n:
            hits += 1
    return hits % MOD
#  -----------------------------------------------------------------------------
MOD = 1004535809
for n in range(3,10):
    print(f'T({n},{n}) = ',T(n,n))
#  -----------------------------------------------------------------------------
#  solution: 779429131
#  -----------------------------------------------------------------------------
