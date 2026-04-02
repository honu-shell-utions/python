################################################################################
##Square root digital expansion
##Problem 80
##It is well known that if the square root of a natural number
##is not an integer, then it is irrational. The decimal expansion
##of such square roots is infinite without any repeating pattern at all.
##
##The square root of two is 1.41421356237309504880..., and the digital
##sum of the first one hundred decimal digits is 475.
##
##For the first one hundred natural numbers, find the
##total of the digital sums of the first one hundred decimal
##digits for all the irrational square roots.
################################################################################
from decimal import getcontext, Decimal
from math import isqrt
import time
start = time.time()

getcontext().prec = 102
stop_at = 100
ans = 0
multiplier = pow(10, stop_at-1)

lst = [num for num in range(1, 101) if isqrt(num) ** 2 != num]

for num in lst:
    big_dec = Decimal(num).sqrt()
    huge_int = big_dec * multiplier
    for d in str(huge_int)[:stop_at]:
        ans += int(d)
        
print('The solution:',ans,'Run time:',time.time()-start)

################################################################################
#solution: 40886
################################################################################
