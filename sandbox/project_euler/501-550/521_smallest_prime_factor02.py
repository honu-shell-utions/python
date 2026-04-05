#  -----------------------------------------------------------------------------
#  Smallest prime factor
#  Problem 521
#  Let smpf(n) be the smallest prime factor of n.
#  smpf(91)=7 because 91=7×13 and smpf(45)=3 because 45=3×3×5.
#  Let S(n) be the sum of smpf(i) for 2 ≤ i ≤ n.
#  E.g. S(100)=1257.
#  
#  Find S(10^12) mod 10^9.
#  
#  https://projecteuler.net/problem=521
#  -----------------------------------------------------------------------------
from time import time
from math import isqrt
#  -----------------------------------------------------------------------------
def sievecntsum(n):
    p = isqrt(n)
    if (p+1)**2 <= n:
        p += 1
    V = [n//i for i in range(1,p+1)]
    V += list(range(V[-1]-1,0,-1))
    S0 = {i:i-1          for i in V}
    S1 = {i:i*(i+1)//2-1 for i in V}
    SP = {i:i*(i+1)//2-1 for i in V}
    for p in range(2,p+1):
        if S0[p] > S0[p-1]: # p is prime
            p2 = p*p
            for v in V:
                if v < p2: break
                vmodp = v//p
                D0 =  S0[vmodp] - S0[p-1]
                D1 =  S1[vmodp] - S1[p-1]
                S0[v] -=    D0
                S1[v] -= p*(D1)
                SP[v] -= p*(D1-D0)
    return SP[n] % MOD
#  -----------------------------------------------------------------------------
MOD = 10**9
for exp in range(2,13):
    start = time()
    N = 10**exp
    print(f'Solution for n = 10^{exp:2}, {sievecntsum(N):10}, Run-Time: {time()-start:>8.3f}')
#  -----------------------------------------------------------------------------
#  solution: 44389811
#  -----------------------------------------------------------------------------
