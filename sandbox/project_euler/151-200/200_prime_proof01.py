#-------------------------------------------------------------------------------
## Find the 200th prime-proof sqube containing the
## contiguous sub-string "200"
## 
## Problem 200
## 
## We shall define a sqube to be a number of the form,
## p^2q^3, where p and q are distinct primes.
## 
## For example, 200 = 5^2*2^3 or 120072949 = 23^2*61^3.
## 
## The first five squbes are 72, 108, 200, 392, and 500.
## 
## Interestingly, 200 is also the first number for which
## you cannot change any single digit to make a prime; we
## shall call such numbers, prime-proof. The next prime-proof
## sqube which contains the contiguous sub-string "200" is 1992008.
## 
## Find the 200th prime-proof sqube containing the contiguous  
## sub-string "200".
#-------------------------------------------------------------------------------
from sympy import primerange, isprime
from time import time
#-------------------------------------------------------------------------------    
def generate_squbes():
    primes = tuple(primerange(2,10**6))
    squbes = []
    for p in primes:
        for q in primes:
            if p == q:
                continue
            x = p**2*q**3
            if '200' in str(x):
                squbes.append(x)
            if x > 10**12:
                break
    return squbes
#-------------------------------------------------------------------------------
def is_prime_proof(n):
    n_str = list(str(n))
    for pos in range(len(n_str)):
        save = n_str[pos]
        for d in ['0','1','2','3','4','5','6','7','8','9']:
            if pos == 0 and d == '0':
                continue
            n_str[pos] = d
            if isprime(int(''.join(n_str))):
                return False
            n_str[pos] = save    
    return True
#-------------------------------------------------------------------------------
start = time()
squbes = generate_squbes()
squbes.sort()
sols = []
for g in squbes:
    if is_prime_proof(g):
        sols.append(g)
        if len(sols) == 200:
            break

print(f'Solution: {sols[-1]}, Run-Time: {time()-start}')
#-------------------------------------------------------------------------------
# 229161792008
#-------------------------------------------------------------------------------

