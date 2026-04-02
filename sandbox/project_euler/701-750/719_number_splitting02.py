#  -----------------------------------------------------------------------------
#  Number Splitting
#  Problem 719
#  https://projecteuler.net/problem=719
#  -----------------------------------------------------------------------------
from math import sqrt, isqrt
from time import time
#  -----------------------------------------------------------------------------
def get_splits(snum):
    if len(snum) == 1:
        return [snum]
    else:
        p = get_splits(snum[1:])
        lst = []
        for c in ['', '+']:
            for d in p:
                lst.append(snum[0] + c + d)
        return lst
#  -----------------------------------------------------------------------------
for exp in [4,6,8,10,12]:
    start = time()
    solution = 0
    for n in range(4,isqrt(10**exp)+1):
        if n % 9 not in [0,1]:
            continue
        sp = get_splits(str(n*n))
        for s in sp[1:]:
            nums = s.split('+')
            total = 0
            for x in nums:
                total += int(x)
            if total == n:
                solution += n*n
                break       
    print(f'Solution for 10^{exp:<2}: {solution:15}, Run-Time: {time()-start}')
#  -----------------------------------------------------------------------------
#  solution: 128088830547982
#  -----------------------------------------------------------------------------
