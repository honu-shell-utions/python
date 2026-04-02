#  -----------------------------------------------------------------------------
#  Ascending subsequences
#  Problem 733
#  https://projecteuler.net/problem=733
#  -----------------------------------------------------------------------------
from itertools import combinations
from time import time
#  -----------------------------------------------------------------------------
def make_seq(n):
    x = []
    for i in range(1,n+1):
        x.append(153**i % MOD1)
    return x
#  -----------------------------------------------------------------------------
def make_subs(seq):
    combos = combinations(seq,4)
    keepers = []
    for c in combos:
        if list(c) == sorted(c):
            keepers.append(c)
    return keepers
#  -----------------------------------------------------------------------------
def S(n):
    seq = make_seq(n)
    res = make_subs(seq)
    total = 0
    for r in res:
        total += sum(r)
    return total % MOD2
#  -----------------------------------------------------------------------------
MOD1 = 10**7 + 19
MOD2 = 10**9 + 7
for exp in range(2,8):
    start = time()
    print(f'Solution for n = 10^{exp}: {S(10**exp):10}, Run-Time: {time()-start:7.3f}')
#  -----------------------------------------------------------------------------
#  solution: 574368578
#  -----------------------------------------------------------------------------
