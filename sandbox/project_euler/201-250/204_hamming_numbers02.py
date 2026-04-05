#-------------------------------------------------------------------------------
## Generalised Hamming Numbers
## Problem 204
## 
## A Hamming number is a positive number which has
## no prime factor larger than 5.
## 
## So the first few Hamming numbers are 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15.
## There are 1105 Hamming numbers not exceeding 10^8.
## 
## We will call a positive number a generalised Hamming number of type n,
## if it has no prime factor larger than n.
## 
## Hence the Hamming numbers are the generalised Hamming numbers of type 5.
## 
## How many generalised Hamming numbers of type 100 are there
## which don't exceed 10^9?
#-------------------------------------------------------------------------------
from sympy import primerange
from time import time
from math import log
#-------------------------------------------------------------------------------
def k_smooth_numbers(limit):
    k_s_n = [1]
    for curr_prime in ok_primes:
        temp_k_s_n = []
        power_limit = int(log(limit, curr_prime)) + 1
        curr_multiples = [curr_prime**x for x in range(1, power_limit + 1)]
        for x in curr_multiples:
            for y in k_s_n:
                temp = x*y
                if temp <= limit:
                    temp_k_s_n.append(temp)
        k_s_n.extend(temp_k_s_n)
    return len(k_s_n)
#-------------------------------------------------------------------------------
start = time()
ham_type = 100
ok_primes = list(primerange(2,ham_type+1))
hammings = k_smooth_numbers(10**9)
print(f'Solution: {hammings}, Run-Time: {time()-start}')
#-------------------------------------------------------------------------------
# solution: 2944730
#-------------------------------------------------------------------------------
