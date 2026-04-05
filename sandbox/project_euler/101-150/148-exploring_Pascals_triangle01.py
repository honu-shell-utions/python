###############################################################################
# p148_exploring_Pascals_triangle.py
#
# We can easily verify that none of the entries in the first seven rows of
# Pascal's triangle are divisible by 7:
# 
#  	 	 	 	 	 	 1
#  	 	 	 	 	 1	 	 1
#  	 	 	 	 1	 	 2	 	 1
#  	 	 	 1	 	 3	 	 3	 	 1
#  	 	 1	 	 4	 	 6	 	 4	 	 1
#  	 1	 	 5	 	10	 	10	 	 5	 	 1
# 1	 	 6	 	15	 	20	 	15	 	 6	 	 1
# However, if we check the first one hundred rows, we will find that only 2361
# of the 5050 entries are not divisible by 7.
# 
# Find the number of entries which are not divisible by 7 in the first one 
# billion (10^9) rows of Pascal's triangle.
###############################################################################
from time import time
DIGITS = '0123456789abcdef'
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
start = time()
total = 0
for row in range(10**9):
    x = convert_to_base(row,7)
    temp = 1
    for d in x:
        temp *= int(d)+1
    total += temp
print('The solution:',total,'Run Time',time()-start)
###############################################################################
# solution: 2129970655314432
###############################################################################
