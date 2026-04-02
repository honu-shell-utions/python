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
from sympy import nextprime
################################################################################
limit = 1000
counter = 0
current_prime = 2
while True:
    current_prime = nextprime(current_prime)
    if current_prime >= limit:
        break
    for n in range(1,limit):
        test = n**3 + n**2*current_prime
        if round(test ** (1/3))**3 == test:
            counter += 1
            print(current_prime,'\t---> '+str(n)+'^3 + ' +str(current_prime)+'*'+str(n)+'^2 = '+str(test))
            
print(counter,'solutions')
################################################################################
#solution:
################################################################################
