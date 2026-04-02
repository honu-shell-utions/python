#  -----------------------------------------------------------------------------
#  Ascending subsequences
#  Problem 733
#  https://projecteuler.net/problem=733
#  -----------------------------------------------------------------------------
from itertools import combinations
from time import time
#  -----------------------------------------------------------------------------
def seq_gen():
    a = 153
    while True:
        yield a
        a *= 153
        a %= MOD1
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
    sg = seq_gen()
    seq = []
    for k in range(n):
        seq.append(next(sg))
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
