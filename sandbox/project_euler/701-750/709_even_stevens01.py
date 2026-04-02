#  -----------------------------------------------------------------------------
#  Even Stevens 
#  Problem 709
#  https://projecteuler.net/problem=709
#  https://oeis.org/A000111
#  -----------------------------------------------------------------------------
from time import time
from itertools import accumulate
#  -----------------------------------------------------------------------------
def euler_709(n):
    A000111_list, blist = [1, 1], [1]
    for n in range(n+1):
        blist = list(reversed(list(accumulate(reversed(blist))))) + [0] \
                if n % 2 else [0]+list(accumulate(blist))
        A000111_list.append(sum(blist) % MOD)
    return A000111_list[N] % MOD
#  -----------------------------------------------------------------------------
MOD = 1020202009
LIMIT = 24680
for N in [4,6,8,100,1000,10000,LIMIT]:
    start = time()
    sol = euler_709(N)
    if N == 4 or N == 8 or N == LIMIT:
        print('-'*60)
    print(f'Solution for N = {N:8,}: {sol:12,}, Run-Time: {time()-start:.2f}')
    if N == 4 or N == 8 or N == LIMIT:
        print('-'*60)
    N += 4
#  -----------------------------------------------------------------------------
#  solution: 773479144 
#  -----------------------------------------------------------------------------
