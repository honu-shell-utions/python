from math import ceil, isqrt
from time import time

def Lucy_Hedgehog_sum(n, f=(lambda x: 1), sum_f=(lambda x: x)):
    r = isqrt(n)
    V = [n//i for i in range(1, r+1)]
    V += list(range(V[-1]-1, 0, -1))
    S = {i:sum_f(i)-1 for i in V}
    for p in range(2, r+1):
        if S[p] == S[p-1]:
            continue  # p not prime
        sp, p2, fp = S[p-1], p*p, f(p)
        for v in V:
            if v < p2:
                break
            S[v] -= fp*(S[v//p] - sp)
    return S

def primesBelow(n):
    if n <= 2:
        return []
    sieve = [True]*(n // 2)
    for i in range(3, isqrt(n)+1, 2):
        if not sieve[i // 2]:
            continue
        for j in range(i*i // 2, len(sieve), i):
            sieve[j] = False
    return [2]+[2*i+1 for i in range(1, n//2) if sieve[i]]

def smallPrimePart(N, P):
    S = 0
    for p in primesBelow(int(ceil(N**0.5))):
        pRow = [N]
        Q = N
        while Q:
            Q //= p
            pRow.append(Q)
        pRow = [pRow[i] - pRow[i+1] for i in range(len(pRow)-1)]
        for a in range(1, len(pRow)):
            for b in range(a):
                S = (S + (a-b)*pRow[a]*pRow[b]) % P
    return S

def largePrimePart(N, P):
    sqrtN = isqrt(N)
    pi = Lucy_Hedgehog_sum(N, lambda x: 1, lambda x: x)
    S = 0
    for z in range(sqrtN-1, 0, -1):
        S = (S + z*(N-z)*(pi[N//z] - pi[N//(z+1)])) % P
    return S

MOD = 10**9 + 7
for exp in range(2,13):
    start = time()
    N = 10**exp
    S = smallPrimePart(N, MOD) + largePrimePart(N, MOD)
    S = 2*S % MOD
    print(f'for n = 10^{exp:<2}: {S:10} Run-Time: {time()-start}')
#  -----------------------------------------------------------------------------
#  solution: 413876461
#  -----------------------------------------------------------------------------

