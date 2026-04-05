#  -----------------------------------------------------------------------------
#  Number Splitting
#  Problem 719
#  https://projecteuler.net/problem=719
#  -----------------------------------------------------------------------------
from math import sqrt, isqrt
from time import time
#  -----------------------------------------------------------------------------
def get_splits(n):
    str_n=str(n)
    for cutpoints in range(2**(len(str_n)-1)):
        result = []
        lastcut = 0
        for i in range(len(str_n)-1):
            if (2**i) & cutpoints != 0:
                result.append(int(str_n[lastcut:(i+1)]))
                lastcut = i+1
        result.append(int(str_n[lastcut:]))
        yield result
#  -----------------------------------------------------------------------------
for exp in [4,6,8,10,12]:
    start = time()
    solution = 0
    for n in range(4,isqrt(10**exp)+1):
        if n % 9 not in [0,1]:
            continue
        sp = get_splits(str(n*n))
        for s in sp:
            if sum(s) == n:
                solution += n*n
                break       
    print(f'Solution for 10^{exp:<2}: {solution:15}, Run-Time: {time()-start}')
#  -----------------------------------------------------------------------------
#  solution: 128088830547982
#  -----------------------------------------------------------------------------
