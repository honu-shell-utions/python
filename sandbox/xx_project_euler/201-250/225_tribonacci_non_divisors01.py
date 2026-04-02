#-------------------------------------------------------------------------------
## Tribonacci non-divisors
## Problem 225
## The sequence 1, 1, 1, 3, 5, 9, 17, 31, 57, 105, 193, 355, 653, 1201 ...
## is defined by T1 = T2 = T3 = 1 and Tn = Tn-1 + Tn-2 + Tn-3.
## 
## It can be shown that 27 does not divide any terms of this sequence.
## In fact, 27 is the first odd number with this property.
## 
## Find the 124th odd number that does not divide any terms of the above sequence.
#-------------------------------------------------------------------------------
from time import time
#-------------------------------------------------------------------------------
def tribonacci_divisor(n):
    a, b, c = 1, 1, 1
    seen = set()
    while (a, b, c) not in seen:
        seen.add((a, b, c))
        a, b, c = b, c, (a+b+c) % n
        if c == 0:
            return True
    return False
#-------------------------------------------------------------------------------    
start = time()
i = 1
non_divisors = []

while len(non_divisors) < 124:
    if not tribonacci_divisor(i):
        non_divisors.append(i)	
    i += 2

print(f'Solution: {non_divisors}, Run-Time: {time()-start}')
#-------------------------------------------------------------------------------
# solution: 2009
#-------------------------------------------------------------------------------
