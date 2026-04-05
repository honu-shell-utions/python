# 70-totientPermutations.py
#
# Euler's Totient function, φ(n) [sometimes called the phi function], is used
# to determine the number of positive numbers less than or equal to n which  are
# relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than
# nine and relatively prime to nine, φ(9)=6.  The number 1 is considered to be
# relatively prime to every positive number,so φ(1) = 1
#
# Interestingly, φ(87109) = 79180, and it can be seen that 87109 is a permutation
# of 79180.
#
# Find the value of n, 1 < n < 10^7, for which φ(n) is a permutation of n and
# the ratio n/φ(n) produces a minimum.
#
#################################################################################
from sympy.ntheory.factor_ import totient
import time
import math
#################################################################################
def isPermut(a,b):
    aStr = str(a)
    bStr = str(b)
    if sorted(aStr) == sorted(bStr):
        return True
    else:
        return False
#################################################################################
stop_at = 10_000_000
min_ratio = stop_at
keeper_n = 0
start = time.time()
for n in range(2, stop_at):
    temp = totient(n)
    if isPermut(n,temp) and n/temp < min_ratio:
        keeper_n = n
        min_ratio = n/temp
        #print(n,temp,n/temp)
             
end = time.time()
print('Solution:',keeper_n,'Running Time:',end-start)


############################################################################################
#solution:
############################################################################################
