#  -----------------------------------------------------------------------------
#  Primonacci
#  Problem 304
#  For any positive integer n the function next_prime(n) returns the
#  smallest prime p such that p>n.
#  
#  The sequence a(n) is defined by:
#  a(1)=next_prime(10^14) and a(n)=next_prime(a(n-1)) for n>1.
#  
#  The fibonacci sequence f(n) is defined by: f(0)=0, f(1)=1 and
#  f(n)=f(n-1)+f(n-2) for n>1.
#  
#  The sequence b(n) is defined as f(a(n)).
#  
#  Find ∑ b(n) for 1≤n≤10**5. Give your answer mod 1234567891011.
#  -----------------------------------------------------------------------------
from sympy import nextprime
from time import time
#  -----------------------------------------------------------------------------
def fib(n):
    if n in fibs:
        return fibs[n]
    if n % 2 == 0:
        fibs[n] = ((2 * fib((n // 2) - 1)) + fib(n // 2)) * fib(n // 2)
    else:
        fibs[n] = (fib((n - 1) // 2) ** 2) + (fib((n+1) // 2) ** 2)
    fibs[n] %= MOD
    return fibs[n]
#  -----------------------------------------------------------------------------
MOD = 1234567891011
print('-'*70)
for exp in range(1,11):
    start = time()
    fibs = {0: 0, 1: 1}
    p = 10**14
    total = 0
    for n in range(1,10**exp+1):
        p = nextprime(p)
        total += fib(p)
    total %= MOD
    if exp == 5:
        print('-'*70)
    print(f'Solution for n = 10^{exp:2}: {total:14}, Run-Time: {time()-start:10.3f}')
    if exp == 5:
        print('-'*70)
print('-'*70)
#  -----------------------------------------------------------------------------
#  solution: 283988410192
#  -----------------------------------------------------------------------------
