#  -----------------------------------------------------------------------------
#  Median of Products
#  Problem 793
#  https://projecteuler.net/problem=793
#  -----------------------------------------------------------------------------
from time import time
#  -----------------------------------------------------------------------------
def next_rand():
    previous = 290797
    yield previous
    while True:
        previous = previous**2 % 50515093
        yield previous
#  -----------------------------------------------------------------------------
def M(n):
    nr = next_rand()
    rand_list = []
    for rand in nr:
        rand_list.append(rand)
        if len(rand_list) > n:
            break
    prod_list = []
    for i in range(n):
        for j in range(i+1,n):
            prod_list.append(rand_list[i]*rand_list[j])
    pl = sorted(prod_list)
    size = len(pl)
    if size % 2 == 0:
        median = (pl[size//2]+pl[size//2+1])//2
    else:
        median = pl[size//2]
    return median
#  -----------------------------------------------------------------------------
for exp in range(7):
    limit = 10**exp + 3
    start = time()
    print(f'Solution for n = 10^{exp:1}+3 is {M(limit):16}, Run-Time: {time()-start}')
#  -----------------------------------------------------------------------------
#  solution: 475808650131120
#  -----------------------------------------------------------------------------
