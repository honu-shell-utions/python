#  -----------------------------------------------------------------------------
#  2-Friendly
#  Problem 643
#  https://projecteuler.net/problem=643
#  -----------------------------------------------------------------------------
from math import gcd, log2
from time import time
#  -----------------------------------------------------------------------------
def count_two_friendly(n):
    count = 0
    for p in range(2,n+1,2):
        for q in range(p+2,n+1,2):
            res = log2(gcd(p,q))
            if res == int(res):
                #print(p,q)
                count += 1
                count %= MOD
    return count % MOD
#  -----------------------------------------------------------------------------
MOD = 10**9 + 7
for exp in [2,3,4,5]:
    start = time()
    solution = count_two_friendly(10**exp)
    print(f'Solution for n = {10**exp:12} --> {solution:10}, Run-Time: {time()-start}')
#  -----------------------------------------------------------------------------
#  solution: 968274154
#  -----------------------------------------------------------------------------
