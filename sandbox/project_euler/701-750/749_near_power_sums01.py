#  -----------------------------------------------------------------------------
#  Near Power Sums
#  Problem 749
#  https://projecteuler.net/problem=749
#  -----------------------------------------------------------------------------
from time import time
from math import floor, ceil, log
#  -----------------------------------------------------------------------------
def near_power_sum(n,k):
    n_save = n
    p_sum = 0
    while n > 0:
        p_sum += (n % 10)**k
        n //= 10
    if p_sum == n_save - 1 or p_sum == n_save + 1:
        return True
    else:
        return False
#  -----------------------------------------------------------------------------
limit = 10**16
total = 0
for j in range(1,limit+1):
    for exp in range(1,17):
        val = near_power_sum(j,exp)
        if val:
            total += j
            print(f'Exponent: {exp:2}, Near Power Sum: {j:8}, Running Total: {total}')
#  -----------------------------------------------------------------------------
#  solution: 13459471903176422  
#  -----------------------------------------------------------------------------
