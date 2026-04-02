################################################################################
# 134-prime_pair_connection.py
#
# Consider the consecutive primes p1 = 19 and p2 = 23. It can be verified that
# 1219 is the smallest number such that the last digits are formed by p1 whilst
# also being divisible by p2.
# 
# In fact, with the exception of p1 = 3 and p2 = 5, for every pair of 
# consecutive primes, p2 > p1, there exist values of n for which the last
# digits are formed by p1 and n is divisible by p2. Let S be the smallest of
# these values of n.
# 
# Find ∑ S for every pair of consecutive primes with 5 ≤ p1 ≤ 1000000.
##
## let p1, p2 be consecutive primes such that p1 < p2
##
## we are looking for n = mk + p1, where k is the smallest
## power of 10 that exceeds p1 that is 10**len(str(p1)), we
## are looking to minimize m
##
## we see that n = mk + p1 mod p2 = 0 mod p2 = >  m = -p1 * k^-1 mod p2
## where k^-1 is the multiplicate inverse of k that is k * k^-1 = 1 mod p2
##
################################################################################
from time import time
from sympy import primerange

start_time = time()

primes = list(primerange(5,1000000+100))

def compute1(limit):
    total = 0
    for x in range(len(primes)-1):
        p1 = primes[x]
        p2 = primes[x+1]      
        if p1 > limit:
            break      
        k = 10**len(str(p1))
        m = -p1 * pow(k, -1, p2) % p2
        total += (m*k + p1)
    return total

print(compute1(1000000))
print("--- %s seconds ---" % (time() - start_time))
################################################################################
#solution: 18613426663617118
################################################################################
