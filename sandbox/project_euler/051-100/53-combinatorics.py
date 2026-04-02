################################################################################
# 53-combinatorics.py
#
# There are exactly ten ways of selecting three from five, 12345:
# 123, 124, 125, 134, 135, 145, 234, 235, 245, and 345
#
# In combinatorics, we use the notation: 5 Cr 3
# It is not until n = 23, that a value exceeds one-million (23 Cr 10)
#
# How many, not necessarily distinct, values of n Cr r for
# 1 <= n <= 100 are greater than one_million
################################################################################
import math
cutoff = 1_000_000
################################################################################
def numCombinations(n,r):
    result = math.factorial(n)/(math.factorial(n-r)*math.factorial(r))
    return(int(result))
################################################################################
counter = 0
for n in range(1,101):
    for r in range(1,n):
        value = numCombinations(n,r)
        if value > cutoff:
            counter += 1

print(counter)
################################################################################
#solution: 4075
################################################################################
 

