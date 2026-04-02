#  -----------------------------------------------------------------------------
#  XOR-Primes
#  Problem 810
#  https://projecteuler.net/problem=810
#  -----------------------------------------------------------------------------
from time import time
#  -----------------------------------------------------------------------------
def euler_810(n=5*10**6):
    cur = 0
    m = 1
    while cur < n:
        cur += 2**m//m
        m += 1

    mm = 2**m
    arr = [True]*mm
    arr[0] = arr[1] = False

    for i in range(2, mm):
        if arr[i]:
            pi = i.bit_length()-1
            for pj in range(pi, m-pi):
                cur = i<<pj
                for t in range(2**pj):
                    arr[cur] = False
                    cur ^= i*(((t^(t+1))+1)>>1)

    irrp = [i for i,j in enumerate(arr) if j]
    return(irrp[n-1])
#  -----------------------------------------------------------------------------
for exp in range(1,11):
    start = time()
    n = 5*10**exp
    if exp == 6:
        print('-'*60)
    print(f'Solution for n = 5*10^{exp}: {euler_810(n):9}, Run-Time: {time()-start:10.3f} seconds.')
    if exp == 6:
        print('-'*60)
#  -----------------------------------------------------------------------------
#  solution: 124136381
#  -----------------------------------------------------------------------------
