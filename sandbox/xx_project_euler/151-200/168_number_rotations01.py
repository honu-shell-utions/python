##------------------------------------------------------------------------------
##Number Rotations
##Problem 168
##
##Consider the number 142857. We can right-rotate this
##number by moving the last digit (7) to the front of
##it, giving us 714285.
##
##It can be verified that 714285=5×142857.
##This demonstrates an unusual property of 142857: it
##is a divisor of its right-rotation.
##
##Find the last 5 digits of the sum of all
##integers n, 10 < n < 10^100, that have this property.
##------------------------------------------------------------------------------
from math import log10
##------------------------------------------------------------------------------
def rotate(n):
    n, last_digit = divmod(n,10)
    return last_digit*10**(int(log10(n))+1) + n 
##------------------------------------------------------------------------------
exp = 10
for n in range(10,2*10**exp):
    if n % 10 == 0:
        continue
    rotated_n = rotate(n)
    if rotated_n <= n:
        continue
    temp = rotated_n % n
    if temp == 0:
        print(f'{rotated_n}/{n} = {rotated_n//n}')
##------------------------------------------------------------------------------
##solution: 59206
##------------------------------------------------------------------------------
