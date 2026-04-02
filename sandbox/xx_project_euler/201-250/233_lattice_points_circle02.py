#-------------------------------------------------------------------------------
from math import isqrt
from sympy import primerange
from time import time
#-------------------------------------------------------------------------------
def count(x, i = 0):
    global sum_total
    sum_total += x
    for j in range(i, len(bad_primes)):
        if x * bad_primes[j] > limit:
            break
        count(x * bad_primes[j], j)
#-------------------------------------------------------------------------------
start = time()
nmax = 5*10**6
limit = 10**11
sum_total = 0
prime_gen = primerange(2,nmax)
good_primes = []
bad_primes = []
for p in prime_gen:
    if p % 4 == 1:
        good_primes.append(p)
    else:
        bad_primes.append(p)        
#-------------------------------------------------------------------------------
for a in good_primes:
    if a ** 3 > limit:
        break
    for b in good_primes:
        if b != a:
            if a ** 3 * b ** 2 > limit:
                break
            for c in good_primes:
                if c != a and c != b:
                    if a ** 3 * b ** 2 * c > limit:
                        break
                    count(a ** 3 * b ** 2 * c)
#-------------------------------------------------------------------------------
for a in good_primes:
    if a ** 7 > limit:
        break
    for b in good_primes:
        if b != a:
            if a ** 7 * b ** 3 > limit:
                break
            count(a ** 7 * b ** 3)
#-------------------------------------------------------------------------------
for a in good_primes:
    if a ** 10 > limit:
        break
    for b in good_primes:
        if b != a:
            if a ** 10 * b ** 2 > limit:
                break
            count(a ** 10 * b ** 2)
#-------------------------------------------------------------------------------
print(f'Solution: {sum_total}, Run-Time: {time()-start}')
#-------------------------------------------------------------------------------
# 271204031455541309
#-------------------------------------------------------------------------------
