# 145-reversible_numbers.py
# How many reversible numbers are there below one-billion?
#
# Some positive integers n have the property that the sum [ n + reverse(n) ] 
# consists entirely of odd (decimal) digits. For instance, 
# 36 + 63 = 99 and 409 + 904 = 1313. We will call such numbers reversible; so
# 36, 63, 409, and 904 are reversible. Leading zeroes are not allowed in 
# either n or reverse(n).
#
# There are 120 reversible numbers below one-thousand.
#
# How many reversible numbers are there below one-billion (10^9)?
from time import time

def checkReversible(first):
    second = int(str(first)[::-1])
    if second % 2 != 0:
        return False
    total = first + second
    for d in str(total):
        if d not in ['1','3','5','7','9']:
            return False
    return True

start = time()
limit = 10**9
count = 0
for k in range(1,limit,2):
    if checkReversible(k):
        count += 1

print('The solution:',count*2,'Run Time:',time()-start)
#solution: 608720
