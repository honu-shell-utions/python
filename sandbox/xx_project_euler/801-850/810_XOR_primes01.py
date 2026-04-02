#  -----------------------------------------------------------------------------
#  XOR-Primes
#  Problem 810
#  https://projecteuler.net/problem=810
#  -----------------------------------------------------------------------------
from time import time
#  -----------------------------------------------------------------------------
def is_x_or_prime(n):
    for a in range(2,n+1):
        for b in range(2,n+1):
            xmul = x_or_mult(a,b)
            if xmul == n:
                return False
    return True
#  -----------------------------------------------------------------------------
def x_or_mult(a,b):
    results = 0
    while b != 0:
        results ^= a * (b & 1)
        a <<= 1
        b >>= 1
    return results
#  -----------------------------------------------------------------------------
def euler_810(n):
    val = 2
    count = 0
    while True:
        if is_x_or_prime(val):
            count += 1
            if count == n:
                return val
        val += 1
#  -----------------------------------------------------------------------------
for exp in range(1,11):
    start = time()
    n = 5*10**exp
    print(f'Solution for n = 5*10^{exp}: {euler_810(n):9}, Run-Time: {time()-start:10.3f} seconds.')
#  -----------------------------------------------------------------------------
#  solution: 124136381
#  -----------------------------------------------------------------------------
