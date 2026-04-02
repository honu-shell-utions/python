###############################################################################
from time import time
DIGITS = '0123456789ABCDEF'
###############################################################################
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
###############################################################################
def triangle(n):
    return int(n*(n+1)/2)
###############################################################################
start = time()
start_base7 = convert_to_base(10**9,7)
length = len(start_base7)
count = 0
product = 1
for d in start_base7:
    length -= 1
    count += product*triangle(int(d))*28**length
    product *= int(d)+1
run_time = (time()-start)//60
if run_time < 1:
    print('Solution:',count,'run time under one second.')
else:
    print('Solution:',count,'run time:',run_time,'seconds.')
###############################################################################
#solution: 2129970655314432
###############################################################################
