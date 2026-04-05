#  -----------------------------------------------------------------------------
#  A Stoneham Number
#  Problem 731
#  https://projecteuler.net/problem=731
#  -----------------------------------------------------------------------------
from itertools import count
from time import time
#  -----------------------------------------------------------------------------
def stone(top):
    total = 0.0
    for ix in count(1):
        if top < 3**ix + 1:
            break
        total += pow(10, top - 3**ix - 1, 3**ix)/3**ix
        total -= int(total)
    return total

for exp in range(2,17):
    top = 10**exp
    start = time()
    solution = int(stone(top)*10**10)
    print(f'Solution for n = 10^{exp:2}: {solution:20}, Run-Time: {time()-start:.3f}')
#  -----------------------------------------------------------------------------
#  solution: 6086371427
#  -----------------------------------------------------------------------------
