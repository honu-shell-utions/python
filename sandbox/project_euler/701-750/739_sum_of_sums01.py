#  -----------------------------------------------------------------------------
#  Summation of Summations
#  Problem 739
#  https://projecteuler.net/problem=739
#  -----------------------------------------------------------------------------
import numpy as np
from time import time
#  -----------------------------------------------------------------------------
def lucas_gen():
    lucas1 = 1
    lucas2 = 3
    yield lucas1
    yield lucas2
    while True:
        yield lucas1+lucas2
        lucas1,lucas2 = lucas2,lucas1+lucas2
#  -----------------------------------------------------------------------------
def make_seq(n):
    lucas_seq = np.zeros((n,n),dtype=int)
    lg = lucas_gen()
    for col in range(n):
        lucas_seq[0,col] = next(lg) % MOD
    return lucas_seq
#  -----------------------------------------------------------------------------
def f(n):
    lucas_seq = make_seq(n)
    for row in range(1,n):
        for col in range(row,n):
            lucas_seq[row,col] = lucas_seq[row-1,col]+lucas_seq[row,col-1]
    return int(lucas_seq[-1,-1] % MOD)
#  -----------------------------------------------------------------------------
MOD = 10**9 + 7
for n in [8,20]:
    start = time()
    print(f'Solution for n = {n:10}: {f(n):10}, Run-Time: {(time()-start)/60:5.3f} minutes.')
#  -----------------------------------------------------------------------------
#  solution: 711399016
#  -----------------------------------------------------------------------------
