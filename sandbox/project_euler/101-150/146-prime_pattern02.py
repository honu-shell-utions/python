################################################################################
## Investigating a Prime Pattern
## Problem 146
## The smallest positive integer n for which the numbers
## n^2+1, n^2+3, n^2+7, n^2+9, n^2+13, and n^2+27 are consecutive
## primes is 10. The sum of all such integers n below one-million is 1,242,490.
##
## What is the sum of all such integers n below 150 million?
################################################################################
from sympy import isprime, nextprime
from time import time
################################################################################
start = time()
n_list = []
for n in range(10,150*10**6,10):
    if n % 3 == 0: continue
    if n % 7 not in [3,4]: continue
    if n % 11 in [2,3,8,9]: continue
    if n % 13 not in [1,3,4,9,10,12]: continue
    if n % 17 in [2,4,5,12,13,15]: continue
    if n % 19 in [4,5,7,12,14,15]: continue
    if n % 23 in [4,19]: continue
    
    temp = n**2
    p_list1 = []
    for k in [1,3,7,9,13,27]:
        if not isprime(temp+k):
            break
        p_list1.append(temp+k)
    if len(p_list1) < 6:
        continue
    p_list2 = [temp+1]
    for k in [3,7,9,13,27]:
        p_list2.append(nextprime(p_list2[-1]))

    if p_list1 == p_list2:
        n_list.append(n)
        print('\tn = {:>12,} sum = {:>12,}'.format(n,sum(n_list)))
    
print('\n\tThe solution is {:>12,}, Run Time is {:>6,} seconds'\
      .format(sum(n_list),(time()-start)))
################################################################################
#solution: 676333270
################################################################################
