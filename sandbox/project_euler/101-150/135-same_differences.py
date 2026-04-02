################################################################################
# 135-same_differences.py
#
# Given the positive integers, x, y, and z, are consecutive terms of an
# arithmetic progression, the least value of the positive integer, n, for which
# the equation, x^2 − y^2 − z^2 = n, has exactly two solutions is n = 27:
#
# 34^2 − 27^2 − 20^2 = 12^2 − 9^2 − 6^2 = 27
#
# It turns out that n = 1155 is the least value which has exactly
# ten solutions.
#
# How many values of n less than one million have exactly
# ten distinct solutions?
################################################################################
from time import time
################################################################################
def euler_135():
    max = 10**6
    keepers = [0]*(max+1)
    for u in range(1,max+1):
        for v in range(1,max+1):
            if u*v > max+1:
                break
            if (u + v) % 4 == 0 and 3 * v  > u and (3 * v - u) % 4 == 0:
                keepers[u * v] += 1              
    return keepers             
################################################################################
start = time()
results = euler_135()
total = results.count(10)
print('Solution:',total,'Run Time:',time()-start)
################################################################################
#solution: 4989
################################################################################
