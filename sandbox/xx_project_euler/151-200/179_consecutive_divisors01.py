#-------------------------------------------------------------------------------
##Consecutive positive divisors
##Problem 179
##Find the number of integers 1 < n < 10^7, for
##which n and n + 1 have the same number of positive
##divisors. For example, 14 has the positive divisors
##1, 2, 7, 14 while 15 has 1, 3, 5, 15.
#-------------------------------------------------------------------------------
from sympy import divisors
from time import time
#-------------------------------------------------------------------------------
start = time()
count = 0
for k in range(2,10**7-1):
    if len(divisors(k)) == len(divisors(k+1)):
        count += 1
print(f'Solution: {count}, Run-Time: {time()-start}')
#-------------------------------------------------------------------------------
#solution: 986262
#-------------------------------------------------------------------------------
