#  ----------------------------------------------------------------------------
#  Idempotents
#  Problem 407
#  https://projecteuler.net/problem=407
#  ----------------------------------------------------------------------------
from time import time
from sympy import factorint
#  ----------------------------------------------------------------------------
def M(n):
    if len(factorint(n)) == 1:
        return 1
    largest = -1
    for a in range(0,n):
        res = a**2 % n
        if res == a and a > largest:
            largest = a
    return largest
#  ----------------------------------------------------------------------------
for exp in [2,3,4]:
    start = time()
    solution = 0
    for n in range(1,10**exp+1):
        solution += M(n)
    print(f'Solution: {solution}, Run-Time: {time()-start}')
#  ----------------------------------------------------------------------------
#  solution: 39782849136421
#  ----------------------------------------------------------------------------













