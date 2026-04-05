#  -----------------------------------------------------------------------------
#  An engineers' dream come true
#  Problem 263
#  https://projecteuler.net/problem=263
#  -----------------------------------------------------------------------------
from sympy import primerange, factorint
from time import time
#  -----------------------------------------------------------------------------
def is_practical(n):
    if n & 1:
        return n == 1
    f = factorint(n)
    P = (2 << f.pop(2)) - 1
    for p in f:
        if p > 1 + P:
            return False
        P *= p**(f[p]+1)//(p-1)
    return True
#  -----------------------------------------------------------------------------
start = time()
limit = 10**8
primes = list(primerange(2,limit))
count = 0
total = 0
x = 1
while True:
    p1, p2, p3, p4 = primes[x], primes[x+1], primes[x+2], primes[x+3]
    x += 1
    if limit - p1 < 10**3:
        limit += 10**8
        primes = list(primerange(p1 + 1, limit))
        x = 0
    if (p4 - p3 == 6) and (p3 - p2 == 6) and (p2 - p1 == 6):
        n = p1 + 9
        if all([is_practical(z) for z in [n-8, n-4, n, n+4, n+8]]):
            count += 1
            total += n
            if count == 4:
                break
print(f'Solution: {total}, Run-Time: {time()-start}')
#  -----------------------------------------------------------------------------
#  solution: 2039506520
#  -----------------------------------------------------------------------------
