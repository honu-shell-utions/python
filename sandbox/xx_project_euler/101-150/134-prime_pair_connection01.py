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
################################################################################
from sympy import primerange, nextprime
################################################################################          
def euler134():
    total = 0
    for pp in prime_pairs:
        n = 1
        while True:
            test = int(str(n) + str(pp[0]))
            if test % pp[1] == 0:
                total += test
                break
            n += 1
    return total      
################################################################################
limit = 10**6
primes = list(primerange(5,limit))
prime_pairs = []         
for p in primes:
    prime_pairs.append((p,nextprime(p)))
print(euler134())
################################################################################
#solution: 18613426663617118
################################################################################
