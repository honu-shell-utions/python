#  -----------------------------------------------------------------------------
#  A bit of prime
#  Problem 734
#  https://projecteuler.net/problem=734
#  https://en.wikipedia.org/wiki/Fast_Walsh–Hadamard_transform
#  -----------------------------------------------------------------------------
from sympy import primerange
from time import time
#  -----------------------------------------------------------------------------
def FWT(a):
    N = len(a)
    i = 1
    while i < N:
        i1 = i << 1
        for j in range(0, N, i1):
            for k in range(i):
                p = a[j + k]
                q = a[i + j + k]
                tmp = p + q
                if tmp >= MOD:
                    tmp -= MOD
                a[i + j + k] = tmp
        i = i1
    return a
#  -----------------------------------------------------------------------------
def UFWT(a):
    N = len(a)
    i = 1
    while i < N:
        i1 = i << 1
        for j in range(0, N, i1):
            for k in range(i):
                p = a[j + k]
                q = a[i + j + k]
                tmp = q - p
                if tmp < 0:
                    tmp += MOD
                a[i + j + k] = tmp
        i = i1
    return a
#  -----------------------------------------------------------------------------
def euler_734(N, K):
    L = 1 << N.bit_length()
    primes = list(primerange(2,N))
    ret = [1] + [0] * (L - 1)
    ORs = [0] * L
    for p in primes:
        ORs[p] = 1
    ORs = FWT(ORs)
    ret = FWT(ret)
    while K:
        if K & 1:
            for i in range(L):
                ret[i] = ret[i] * ORs[i] % MOD
        K >>= 1
        for i in range(L):
            ORs[i] = ORs[i] * ORs[i] % MOD
    ret = UFWT(ret)
    tot = 0
    for p in primes:
        tot = tot + ret[p]
    return tot % MOD
#  -----------------------------------------------------------------------------
MOD = 10**9 + 7
for n,k in [(10**2,3),(10**3,10),(10**6,999983)]:
    start = time()
    print(f'Solution for (n,k) = ({n:7},{k:7}): {euler_734(n,k):10}, Run-Time: {time()-start:5.2f}')
#  -----------------------------------------------------------------------------
#  solution: 557988060
#  -----------------------------------------------------------------------------
