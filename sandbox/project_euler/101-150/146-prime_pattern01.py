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
    
    p1 = n**2 + 1
    if not isprime(p1):
        continue
    p2 = n**2 + 3
    if p2 != nextprime(p1):
        continue
    p3 = n**2 + 7
    if p3 != nextprime(p2):
        continue
    p4 = n**2 + 9
    if p4 != nextprime(p3):
        continue
    p5 = n**2 + 13
    if p5 != nextprime(p4):
        continue
    p6 = n**2 + 27
    if p6 != nextprime(p5):
        continue
    n_list.append(n)
    
print('The solution:',sum(n_list),'Run Time:',time()-start)
################################################################################
#solution: 676333270
################################################################################
