#  -----------------------------------------------------------------------------
#  Median of Products
#  Problem 793
#  https://projecteuler.net/problem=793
#  -----------------------------------------------------------------------------
from time import time
from numpy import zeros, sort
#  -----------------------------------------------------------------------------
def next_rand():
    previous = 290797
    yield previous
    while True:
        previous = pow(previous,2,50515093)
        yield previous
#  -----------------------------------------------------------------------------
def M(n):
    nr = next_rand()
    rand_arr = zeros(n,dtype=int)
    k = 0
    for rand in nr:
        rand_arr[k] = rand
        k += 1
        if k >= n:
            break
    prod_arr = zeros(n*(n-1)//2,dtype=int)
    k = 0
    for i in range(n):
        for j in range(i+1,n):
            prod_arr[k] = rand_arr[i]*rand_arr[j]
            k += 1
    p_arr = sort(prod_arr)
    size = len(p_arr)
    if size % 2 == 0:
        median = (p_arr[size//2]+p_arr[size//2+1])//2
    else:
        median = p_arr[size//2]
    return median
#  -----------------------------------------------------------------------------
for limit in [3,10**2+3,10**6+3]:
    start = time()
    print(f'Solution for n = {limit:10} is {M(limit):16}, Run-Time: {time()-start}')
#  -----------------------------------------------------------------------------
#  solution: 475808650131120
#  -----------------------------------------------------------------------------
