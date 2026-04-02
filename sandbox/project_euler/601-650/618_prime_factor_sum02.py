#  -----------------------------------------------------------------------------
#  Numbers with a given prime fibactor sum
#  Problem 618
#  https://projecteuler.net/problem=618
#  -----------------------------------------------------------------------------
##With S(5) = 11 and S(8) = 49 you can spot how S(8) = 3 * 11 + 16.
##In other words, running over the primes and totaling factors will work, using 
##  S(k) += p * S(k-p), like this:
##
##S initial: 1 0 0 ...
##process 2: 1 0 2 0 4  0  8  0 16 ...
##process 3: 1 0 2 3 4  6 17 12 34 ...
##process 5: 1 0 2 3 4 11 17 22 49 ...  
#  -----------------------------------------------------------------------------
from sympy import isprime, fibonacci as fibo
from time import time
#  -----------------------------------------------------------------------------
start = time()
modulus = 10**9
total = 0
largest_fib = fibo(24)
totals = [1]+[0]*largest_fib

for p in range(2,largest_fib+1):
  if isprime(p):
    for k in range(p,largest_fib+1):
        totals[k] = (totals[k] + p * totals[k - p]) % modulus
        #print(totals[:k+1])

for k in range(2,25):
    total += totals[fibo(k)]

print(f'Solution: {total % modulus}, Run-Time: {time()-start}')
#  -----------------------------------------------------------------------------
#  solution: 634212216
#  -----------------------------------------------------------------------------
