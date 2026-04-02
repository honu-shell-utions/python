################################################################################
##Prime cube partnership
##Problem 131
##There are some prime values, p, for which there exists
##a positive integer, n, such that the expression n^3 + n^2*p
##is a perfect cube.
##
##For example, when p = 19, 8^3 + 8^2×19 = 12^3.
##
##What is perhaps most surprising is that for each prime
##with this property the value of n is unique, and there
##are only four such primes below one-hundred.
##
##How many primes below one million have this remarkable property?
################################################################################
from sympy import isprime
from time import time
################################################################################
def euler_131(limit):
    prime_list = []
    k = 1
    d = 7
    while d < limit:
        if isprime(d):
            prime_list.append(d)
        k += 1
        d = 1+3*k*(k+1)
    return prime_list

start = time()
prime_list = euler_131(10**6)
print('The solution:',len(prime_list),'Run Time:',time()-start)
################################################################################
#solution: 173
################################################################################
