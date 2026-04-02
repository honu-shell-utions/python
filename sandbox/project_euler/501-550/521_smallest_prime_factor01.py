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
from sympy import primefactors
#  -----------------------------------------------------------------------------
def smpf(n):
    return primefactors(n)[0]
#  -----------------------------------------------------------------------------
def S(n):
    total = 2 * (n // 2)
    for i in range(3,n+1,2):
        total += (smpf(i) % MOD)
    return total % MOD
#  -----------------------------------------------------------------------------
MOD = 10**9
for exp in range(2,13):
    start = time()
    N = 10**exp
    print(f'Solution for n = 10^{exp:2}, {S(N):10}, Run-Time: {time()-start:>8.3f}')
#  -----------------------------------------------------------------------------
#  solution: 44389811
#  -----------------------------------------------------------------------------
