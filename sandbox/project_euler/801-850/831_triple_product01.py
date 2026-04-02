#  -----------------------------------------------------------------------------
#  Triple Product
#  Problem 831
#  https://projecteuler.net/problem=831
#  -----------------------------------------------------------------------------
from time import time
#  -----------------------------------------------------------------------------
def g(n):
    res = 40+474*n + 1835*n**2 + 2085*n**3 + 765*n**4 + 81*n**5
    res = 7**n*res//40
    return res
#  -----------------------------------------------------------------------------
def convert_to_base(decimal_number, base):
    remainder_stack = []
    while decimal_number > 0:
        remainder = decimal_number % base
        remainder_stack.append(remainder)
        decimal_number = decimal_number // base
    new_digits = []
    while remainder_stack:
        new_digits.append(DIGITS[remainder_stack.pop()])
    return ''.join(new_digits)
#  -----------------------------------------------------------------------------
start = time()
DIGITS = '0123456789ABCDEF'
res = g(142857)
res = convert_to_base(res,7)
print(f'Solution: {str(res)[:10]}, Run-Time: {time()-start:.3f}')
#  -----------------------------------------------------------------------------
#  solution: 5226432553
#  -----------------------------------------------------------------------------
