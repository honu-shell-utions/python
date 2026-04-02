#  -----------------------------------------------------------------------------
#  Counting numbers with at least four distinct prime factors less than 100
#  Problem 268
#  It can be verified that there are 23 positive integers less
#  than 1000 that are divisible by at least four distinct primes less than 100.
#  
#  Find how many positive integers less than 10^16 are divisible
#  by at least four distinct primes less than 100.
#  -----------------------------------------------------------------------------
from sympy import primerange
primes = list(primerange(2,101))
#  -----------------------------------------------------------------------------
def num_prime_factors(n):
    prime_divs = 0
    for p in primes:
        if n/p == n//p:
            prime_divs += 1
            if prime_divs == 4:
                return True
    return False
#  -----------------------------------------------------------------------------
for exp in range(3,9):
    count = 0
    for n in range(2*3*5*7,10**exp):
        if num_prime_factors(n):
            count += 1
    print(count)
#  -----------------------------------------------------------------------------
# 10^3:  23
# 10^4:  811
# 10^5:  9280
# 10^6:  77579
# 10^7:  768778
# 10^8:  7881475
# 10^16: 785478606870985 (solution)
#  -----------------------------------------------------------------------------
