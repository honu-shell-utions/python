#  -----------------------------------------------------------------------------
#  Numbers with a given prime factor sum
#  Problem 618
#  https://projecteuler.net/problem=618
#  -----------------------------------------------------------------------------
from sympy import factorint
from sympy import fibonacci as fib
#  -----------------------------------------------------------------------------
def prime_sum(k):
    fi = factorint(k)
    ps = 0
    for key, exp in fi.items():
        ps += key*exp
    return ps
#  -----------------------------------------------------------------------------
def S(k):
    total = 0
    for j in range(1,k**2):
        if prime_sum(j) == k:
            total += j
    return total
#  -----------------------------------------------------------------------------
total = 0
MOD = 10**9
for k in range(2,25):
    n = fib(k)
    s = S(n)
    total += s
    print(k,n,s,total % MOD)
#  -----------------------------------------------------------------------------
#  solution: 634212216
#  -----------------------------------------------------------------------------
