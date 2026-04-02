#-------------------------------------------------------------------------------
## Twenty-two Foolish Primes
## Problem 239
## A set of disks numbered 1 through 100 are placed in a line in random order.
## 
## What is the probability that we have a partial derangement such that exactly
## 22 prime number discs are found away from their natural positions?
## 
## (Any number of non-prime disks may also be found in or out of their
##  natural positions.)
## 
## Give your answer rounded to 12 places behind the decimal point in the
## form 0.abcdefghijkl.
#-------------------------------------------------------------------------------
from random import shuffle
from sympy import primerange
from time import time
#-------------------------------------------------------------------------------
def num_primes_out_of_order():
    out_of_order = 0
    for p in prime_list:
        if current_list[p] != p:
            out_of_order += 1
    return out_of_order
#-------------------------------------------------------------------------------
start = time()
list_size = 100
current_list = [x for x in range(1,list_size + 1)]
num_trials = 10**8
oo_target = 22
count = 0
prime_list = list(primerange(2,list_size + 1))
for trials in range(1,num_trials+1):
    shuffle(current_list)
    npoo = num_primes_out_of_order()
    if npoo == oo_target:
        count += 1
     
print(f'Solution: {round(count/(num_trials),12)}, Run-Time: {time()-start}')
#-------------------------------------------------------------------------------
# solution: 0.001887854841
#-------------------------------------------------------------------------------
