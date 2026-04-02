#  -----------------------------------------------------------------------------
#  x**y = y**x (mod n)
#  Problem 801
#  https://projecteuler.net/problem=801
#  -----------------------------------------------------------------------------
from time import time
from sympy import primerange,divisors,isprime
#  -----------------------------------------------------------------------------
#  J2 is a version of the Jordan totient
def J2(n):
    number = n**2
    for p in divisors(n):
        if isprime(p):
            number *= 1 - (1/(p**2))
    return number
#  -----------------------------------------------------------------------------
def f(p):
    temp_sum = 0
    divs = divisors(p-1)
    for d in divs:
        temp_sum += (p-1)/d * J2(d)
    return (p-1)*( (p-1) + temp_sum )
#  -----------------------------------------------------------------------------
def S(M,N):
    total = 0
    for p in primerange(M,N):
        total += int(f(p))
    return total % MOD
#  -----------------------------------------------------------------------------
MOD = 993353399
print(f(5))
print(f(97))
for M,N in [(1,10**2),(1,10**5),(10**16,10**16 + 10**6)]:
    start = time()
    print(f'Answer for (M,N)= ({M},{N}): {S(M,N):10}')
    print(f'Run-Time        = {(time() - start)//60} minutes.')
#  -----------------------------------------------------------------------------
#  solution: 638129754
#  -----------------------------------------------------------------------------
