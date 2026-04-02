#  -----------------------------------------------------------------------------
#  Ascending subsequences
#  Problem 733
#  https://projecteuler.net/problem=733
#  -----------------------------------------------------------------------------
from fenwick import FenwickTree
from time import time
#  -----------------------------------------------------------------------------
def S(n):
    counts = [FenwickTree(MOD1) for _ in range(4)]
    sums = [FenwickTree(MOD1) for _ in range(4)]
    counts[0].add(0, 1)
    ai = 1
    total = 0
    for _ in range(n):
            ai = ai * 153 % MOD1
            total += counts[3].prefix_sum(ai) * ai + sums[3].prefix_sum(ai)
            for l in range(2, -1, -1):
                counts[l+1].add(ai, counts[l].prefix_sum(ai))
                sums[l+1].add(ai, counts[l].prefix_sum(ai) * ai + sums[l].prefix_sum(ai))
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
