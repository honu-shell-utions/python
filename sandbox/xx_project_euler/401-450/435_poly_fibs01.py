#  -----------------------------------------------------------------------------
#  Polynomials of Fibonacci numbers
#  Problem 435
#  https://projecteuler.net/problem=435
#  -----------------------------------------------------------------------------
from time import time
from math import factorial
#  -----------------------------------------------------------------------------
def fibo_mod(n, MOD):
    if n == 0:
        return 1,0
    a, b = fibo_mod(n//2, MOD)
    if n%2 == 0:
        return (a**2 + b**2) % MOD, (2*a*b + b**2) % MOD
    else:
        return (2*a*b + b**2) % MOD, (b**2 + (a + b)**2) % MOD
#  -----------------------------------------------------------------------------
start = time()
MOD = factorial(15)
n = 10**15
solution = 0
for x in range(0, 101):
    a = x**2 + x - 1
    f0 = fibo_mod(n, MOD*a)[1]
    f1 = fibo_mod(n + 1, MOD*a)[1]
    b = (f0*pow(x, n + 2, MOD*a) + f1*pow(x, n + 1, MOD*a) - x)%(MOD*a)
    solution += b//a
    solution %= MOD

print(f'Solution: {solution}, Run-Time: {time()-start}')
#  -----------------------------------------------------------------------------
#  solution: 252541322550
#  -----------------------------------------------------------------------------
