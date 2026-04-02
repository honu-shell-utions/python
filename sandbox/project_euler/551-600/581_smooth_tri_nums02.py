#  -----------------------------------------------------------------------------
#  47-smooth triangular numbers
#  Problem 581
#  https://projecteuler.net/problem=581
#  A number is p-smooth if it has no prime factors larger than p.
#  Let T be the sequence of triangular numbers, ie T(n)=n(n+1)/2.
#  Find the sum of all indices n such that T(n) is 47-smooth.
#  -----------------------------------------------------------------------------
from time import time
from sympy import primerange, sieve
#  -----------------------------------------------------------------------------
def all_products(limit, primes):
    res = [1]
    for p in primes:
        if p > limit:
            break
        lst = []
        pp = p
        while pp <= limit:
            for q in res:
                ppq = pp*q
                if ppq > limit:
                    break
                lst.append(ppq)
            pp *= p
        res += lst
        res.sort()
    return res
#  -----------------------------------------------------------------------------
def euler_581(p):
    primes = list(primerange(2,p+1))
    products = all_products(N, primes)
    sum_n = 0
    for i in range(len(products) - 1):
        if products[i+1] == products[i] + 1:
            sum_n += products[i]
    return sum_n
#  -----------------------------------------------------------------------------
N = 119089041053696 # from OEIS A002072

for p in sieve:
    if p == 2:
        continue
    if p > 67:
        break
    start = time()
    print(f'Solution for p = {p:3}, {euler_581(p):20}, Run-Time: {time()-start:12.2f}')
#  -----------------------------------------------------------------------------
#  solution: 2227616372734
#  -----------------------------------------------------------------------------
