#-------------------------------------------------------------------------------
# p183_max_prod_of_parts.py
# maximum product of parts
#
# Let N be a positive integer and let N be split into k equal parts, r = N/k,
# so that N = r + r + ... + r.
# Let P be the product of these parts, P = r × r × ... × r = r^k.
#
# For example, if 11 is split into five equal parts,
# 11 = 2.2 + 2.2 + 2.2 + 2.2 + 2.2, then P = 2.2^5 = 51.53632.
#
# Let M(N) = Pmax for a given value of N.
#
# It turns out that the maximum for N = 11 is found by splitting eleven into
# four equal parts which leads to Pmax = (11/4)^4; that is,
# M(11) = 14641/256 = 57.19140625, which is a terminating decimal.
#
# However, for N = 8 the maximum is achieved by splitting it into three equal
# parts, so M(8) = 512/27, which is a non-terminating decimal.
#
# Let D(N) = N if M(N) is a non-terminating decimal and D(N) = -N if M(N) is
# a terminating decimal.
#
# For example, ∑(N) for 5 ≤ N ≤ 100 is 2438.
#
# Find ∑(N) for 5 ≤ N ≤ 10000.
#-------------------------------------------------------------------------------
from math import e
from time import time
#-------------------------------------------------------------------------------
start = time()
limit = 10**4

#NOTE:
# p(k) = (n/k)^k
# differentiate this, set equal to zero & solve for k
# you get: max product happens when round(n/e)
# let k = round(n/e)
# the rational number terminates only if k is of the form 2^x * 5^y

def D(n):
    k = round(n/e)
    while k % 2 == 0:
        k //= 2
    while k % 5 == 0:
        k //= 5
    if n % k != 0:
        return n
    return -n

total = 0
for n in range(5,limit+1):
    total += D(n)

print(f'Solution: {total}, Run-Time: {time()-start}')
#-------------------------------------------------------------------------------
#solution: 48861552
#-------------------------------------------------------------------------------
