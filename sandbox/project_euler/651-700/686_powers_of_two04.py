#  -----------------------------------------------------------------------------
#  Powers of Two 
#  Problem 686
#  https://projecteuler.net/problem=686
#  -----------------------------------------------------------------------------
from math import log10, log2, floor
from time import time
#  -----------------------------------------------------------------------------
def p(L,n):
    str_L = str(L)
    j = 1
    count = 0
    while True:
        res = 2**j
        if str_L == str(res)[:len(str_L)]:
            count += 1
            if count == n:
                return j
        j += 1
#  -----------------------------------------------------------------------------
def euler_686(limit):
    count = 0
    n = 10
    while True:
        num_d = floor(n * log10(2)) + 1
        power = n - (num_d - 3) * log2(10)
        val = floor(2 ** power)
        if val == 123:
            count += 1
            if count == limit:
                return n
                break
        n += 1
#  -----------------------------------------------------------------------------
print(p(12,1))
print(p(12,2))
print(euler_686(45))
start = time()
print(f'Solution: {euler_686(678910)}, Run-Time: {time()-start:.3f}')
#  -----------------------------------------------------------------------------
#  solution: 193060223
#  -----------------------------------------------------------------------------
