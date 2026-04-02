#  -----------------------------------------------------------------------------
#  Pseudo-Fortunate Numbers
#  Problem 293
#  An even positive integer N will be called admissible, if it is
#  a power of 2 or its distinct prime factors are consecutive primes.
#  The first twelve admissible numbers are 2,4,6,8,12,16,18,24,30,32,36,48.
#  
#  If N is admissible, the smallest integer M > 1 such that N+M is prime,
#  will be called the pseudo-Fortunate number for N.
#  
#  For example, N=630 is admissible since it is even and its distinct
#  prime factors are the consecutive primes 2,3,5 and 7.
#  The next prime number after 631 is 641; hence, the pseudo-Fortunate
#  number for 630 is M=11.
#  It can also be seen that the pseudo-Fortunate number for 16 is 3.
#  
#  Find the sum of all distinct pseudo-Fortunate numbers for admissible
#  numbers N less than 10^9.
#  -----------------------------------------------------------------------------
from math import log, isqrt
from sympy import isprime, primerange, primefactors
#  -----------------------------------------------------------------------------
def is_power_of_two(n):
    return int(log(n,2)) == log(n,2)
#  -----------------------------------------------------------------------------
def consecutive_primes(n):
    n_primes = primefactors(n)
    indx = primes.index(n_primes[0])
    return n_primes == primes[indx:indx + len(n_primes)]
#  -----------------------------------------------------------------------------
def is_admissible(n):
    if n % 2 != 0:
        return False
    if is_power_of_two(n):
        return True
    if consecutive_primes(n):
        return True
    return False
#  -----------------------------------------------------------------------------
limit = 10**9
primes = list(primerange(2,isqrt(limit)+1))
set_M = set()
for N in range(2,limit,2):
    if is_admissible(N):
        M = 2
        while True:
            if isprime(N+M):
                break
            else:
                M += 1
        set_M.add(M)
        #print(M,'is pseudo-Fortunate for',N,'sum of M =',sum(set_M))
print(f'Sum of M = {sum(set_M)}')
#  -----------------------------------------------------------------------------
#  solution: 2209
#  -----------------------------------------------------------------------------
