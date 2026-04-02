#  -----------------------------------------------------------------------------
#  Exponent Difference
#  Problem 712
#  https://projecteuler.net/problem=712
#  -----------------------------------------------------------------------------
from sympy import nextprime, factorint
#  -----------------------------------------------------------------------------
def v(p,n):
    r = 0
    for k in range(1,n):
        if n % p**k == 0:
            r = k
    return r
#  -----------------------------------------------------------------------------        
def D(n,m):
    total_diff = 0
    prime = 2
    top = max(n,m)
    while prime <= top:
        total_diff += abs(v(prime,n) - v(prime,m))
        prime = nextprime(prime)
    return total_diff
#  -----------------------------------------------------------------------------
def S(N):
    total = 0
    for n in range(1,N+1):
        for m in range(1,N+1):
            if n == m:
                continue
            total += D(n,m)
    return total % MOD
#  -----------------------------------------------------------------------------
MOD = 10**9 + 7
for exp in range(1,3):
    limit = 10**exp
    print(f'for n = 10^{exp:<2} ---> {S(limit)}')
#  -----------------------------------------------------------------------------
#  solution: 413876461
#  -----------------------------------------------------------------------------
