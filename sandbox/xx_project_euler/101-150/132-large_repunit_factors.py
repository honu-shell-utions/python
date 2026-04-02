################################################################################
##Large repunit factors
##Problem 132
##A number consisting entirely of ones is called a repunit.
##We shall define R(k) to be a repunit of length k.
##
##For example, R(10) = 1111111111 = 11×41×271×9091, and
##the sum of these prime factors is 9414.
##
##Find the sum of the first forty prime factors of R(10^9).
################################################################################
from sympy import nextprime
from time import time
################################################################################
start = time()
prime_factors = []
current_prime = 2
max = 10**9
while True:
    if pow(10,max,9*current_prime) == 1:
        prime_factors.append(current_prime)
        if len(prime_factors) == 40:
            break
    current_prime = nextprime(current_prime)

print('The solution:',sum(prime_factors),'Run Time',time()-start)
################################################################################
#solution: 843296
################################################################################
