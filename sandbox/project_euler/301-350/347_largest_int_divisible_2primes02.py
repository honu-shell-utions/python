#  -----------------------------------------------------------------------------
#  347_largest_int_divisible_2primes.py
#  https://projecteuler.net/problem=347
#  Largest Integer Divisible by Two Primes
#  The largest integer ≤ 100 that is only divisible by both the primes 2 and 3 is
#  96, as 96 = 32*3 = 2^5*3. For two distinct primes p and q let M(p, q, N) be
#  the largest positive integer ≤ N only divisible by both p and q and
#  M(p, q, N) = 0 if such a positive integer does not exist.
#  
#  M(2, 3, 100) = 96.
#  M(3, 5, 100) = 75 and not 90 because 90 is divisible by 2, 3 and 5.
#  
#  Also M(2, 73, 100) = 0 because there does not exist a positive integer ≤ 100
#  that is divisible by both 2 and 73.
#  
#  Let S(N) be the sum of all distinct M(p, q, N). S(100) = 2262.
#  
#  Find S(10_000_000).
#  
#  difficulty: 15%
#  pe_ans = 11_109_800_204_052
#  -----------------------------------------------------------------------------
from sympy import primerange
from time import time
#  -----------------------------------------------------------------------------
def best(p,q):
    a = 1
    maximum = 0
    while p**a * q <= LIMIT:
        b = 1
        while p**a * q**b <= LIMIT:
            maximum = max(maximum, p**a * q**b)
            b += 1
        a += 1
    return maximum
#  -----------------------------------------------------------------------------
start = time()
LIMIT = 10**7
primes = list(primerange(2,LIMIT//2))
total=0
for i in range(len(primes)):
    for j in range(i+1, len(primes)):
        if primes[i]*primes[j] > LIMIT:
            break
        total += best(primes[i], primes[j])           
print(f'Solution: {total:,}, Run-Time: {time()-start}')
#  -----------------------------------------------------------------------------
