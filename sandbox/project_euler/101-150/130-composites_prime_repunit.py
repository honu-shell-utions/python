################################################################################
##Composites with prime repunit property
##Problem 130
##A number consisting entirely of ones is called a repunit.
##We shall define R(k) to be a repunit of length k; for example, R(6) = 111111.
##
##Given that n is a positive integer and GCD(n, 10) = 1,
##it can be shown that there always exists a value, k, for
##which R(k) is divisible by n, and let A(n) be the least
##such value of k; for example, A(7) = 6 and A(41) = 5.
##
##You are given that for all primes, p > 5, that p − 1 is
##divisible by A(p). For example, when p = 41, A(41) = 5, and 40 is divisible by 5.
##
##However, there are rare composite values for which this is
##also true; the first five examples being 91, 259, 451, 481, and 703.
##
##Find the sum of the first twenty-five composite values of n for which
##GCD(n, 10) = 1 and n − 1 is divisible by A(n).
################################################################################
from math import gcd
from sympy import isprime
from time import time
################################################################################
def A(n):
    if gcd(n, 10) != 1:
        return 0
    x = 1
    k = 1
    while x != 0:
        x = (x * 10 + 1) % n
        k += 1
    return k
################################################################################
start = time()
limit = 25
found = 0

n = 1
result = 0

while found < limit:
    n += 1
    if isprime(n):
        continue
    a = A(n)
    if a != 0 and (n - 1) % a == 0:
        result += n
        found += 1

print('The solution:',result,'Run Time:',time()-start)
################################################################################
#solution: 149253
################################################################################
