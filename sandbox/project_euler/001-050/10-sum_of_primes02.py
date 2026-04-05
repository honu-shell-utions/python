##The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
##Find the sum of all the primes below two million.
#jim.mccleery, November, 2021
###############################################################################
from sympy import primerange
from time import time
###############################################################################
start = time()
max_len = 2*10**6
primes = list(primerange(2,max_len))
print(f'Solution: {sum(primes)}, Run-Time: {time()-start}')
###############################################################################
#solution: 142913828922
###############################################################################
